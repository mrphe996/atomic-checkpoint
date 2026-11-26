-- One-time purchases (26/11/2026).
-- A course is bought once (Paddle, one-time price) and stays the learner's for as long as they keep studying.
-- If a learner does not study for 365 days, their bought courses expire (enrolments.status = 'expired') and must be bought again.
-- "Studying" = saving progress or sitting a Unit Test. The clock starts at the purchase.
-- Admin grants (method 'admin') and testers never expire.

-- 1. columns
alter table public.learners add column if not exists last_active_at timestamptz not null default now();
alter table public.enrolments add column if not exists provider_txn_id text;
alter table public.enrolments add column if not exists expired_at timestamptz;
alter table public.enrolments add column if not exists updated_at timestamptz not null default now();

-- 2. every Paddle transaction received by the webhook (idempotent on the transaction id)
create table if not exists public.purchases (
  provider_txn_id text primary key,
  learner_id uuid references public.learners (id) on delete set null,
  stages int[] not null default '{}',
  price_id text,
  amount text,
  currency text,
  status text not null,                 -- 'granted' | 'refunded' | 'needs_review'
  note text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
alter table public.purchases enable row level security;
create policy purchases_read on public.purchases for select using (public.owns_learner(learner_id));
grant select on public.purchases to authenticated;
grant all on public.purchases to service_role;

-- 3. a learner idle for a year loses their bought courses
create or replace function public.expire_if_idle(p_learner uuid)
returns int language plpgsql security definer set search_path = public as $$
declare n int := 0;
begin
  if exists (select 1 from public.testers where learner_id = p_learner) then return 0; end if;
  if (select last_active_at from public.learners where id = p_learner) < now() - interval '365 days' then
    update public.enrolments set status = 'expired', expired_at = now(), updated_at = now()
    where learner_id = p_learner and status = 'active' and method <> 'admin';
    get diagnostics n = row_count;
    if n > 0 then
      insert into public.notifications (parent_id, learner_id, kind, title, body)
      select coalesce(l.parent_id, l.user_id), l.id, 'billing', 'Your courses have expired',
             'You did not study for a year, so your courses were closed. Buy a course again to continue.'
      from public.learners l where l.id = p_learner;
    end if;
  end if;
  return n;
end $$;
revoke all on function public.expire_if_idle(uuid) from public, anon, authenticated;
grant execute on function public.expire_if_idle(uuid) to service_role;

-- the app calls this when a learner is opened: expired courses are closed before anything is shown
create or replace function public.check_access(p_learner uuid)
returns int language plpgsql security definer set search_path = public as $$
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  return public.expire_if_idle(p_learner);
end $$;
revoke all on function public.check_access(uuid) from public, anon;
grant execute on function public.check_access(uuid) to authenticated;

-- daily sweep of every idle learner
create or replace function public.expire_idle_all()
returns int language plpgsql security definer set search_path = public as $$
declare r record; n int := 0;
begin
  for r in select id from public.learners where last_active_at < now() - interval '365 days' loop n := n + public.expire_if_idle(r.id); end loop;
  return n;
end $$;
revoke all on function public.expire_idle_all() from public, anon, authenticated;

-- 4. activity: saving progress or sitting a test moves the clock (after closing an already-expired year)
create or replace function public.touch_learner()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  perform public.expire_if_idle(new.learner_id);
  update public.learners set last_active_at = now() where id = new.learner_id and last_active_at < now() - interval '1 hour';
  return new;
end $$;
drop trigger if exists progress_touch on public.progress;
create trigger progress_touch after insert or update on public.progress for each row execute function public.touch_learner();
drop trigger if exists attempts_touch on public.attempts;
create trigger attempts_touch after insert on public.attempts for each row execute function public.touch_learner();

-- 5. checks before the Paddle checkout opens (same level rule as enrol_stage)
create or replace function public.prepare_checkout(p_learner uuid, p_stages int[])
returns text language plpgsql security definer set search_path = public as $$
declare v_level int; v_cur int; v_has boolean; s int;
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  if p_stages is null or cardinality(p_stages) not between 1 and 3 then raise exception 'bad stages' using errcode = '22023'; end if;
  v_level := p_stages[1] % 10;
  foreach s in array p_stages loop
    if s not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29) or s % 10 <> v_level then
      raise exception 'bad stage' using errcode = '22023'; end if;
    if exists (select 1 from public.enrolments where learner_id = p_learner and stage = s and status = 'active') then
      raise exception 'already enrolled' using errcode = 'P0001'; end if;
  end loop;
  perform public.expire_if_idle(p_learner);
  select coalesce(stage, 7) into v_cur from public.learners where id = p_learner;
  select exists (select 1 from public.enrolments where learner_id = p_learner and status = 'active') into v_has;
  if v_has and v_level <> v_cur and public.level_tests_pct(p_learner, v_cur) < 80
     and not exists (select 1 from public.testers where learner_id = p_learner) then
    raise exception 'stage locked: finish 80%% of Stage % first', v_cur using errcode = 'P0001';
  end if;
  return 'ok';
end $$;
revoke all on function public.prepare_checkout(uuid, int[]) from public, anon;
grant execute on function public.prepare_checkout(uuid, int[]) to authenticated;

-- 6. the webhook (service role only) grants or refunds a paid transaction
create or replace function public.grant_purchase(p_learner uuid, p_stages int[], p_txn text, p_amount text)
returns text language plpgsql security definer set search_path = public as $$
declare s int;
begin
  foreach s in array p_stages loop
    insert into public.enrolments (learner_id, stage, method, amount, provider_txn_id, status)
    values (p_learner, s, 'paddle', p_amount, p_txn, 'active')
    on conflict (learner_id, stage) do update set status = 'active', method = 'paddle', amount = excluded.amount,
      provider_txn_id = excluded.provider_txn_id, expired_at = null, updated_at = now();
  end loop;
  update public.learners set stage = p_stages[1] % 10, last_active_at = now() where id = p_learner;
  insert into public.notifications (parent_id, learner_id, kind, title, body)
  select coalesce(l.parent_id, l.user_id), l.id, 'billing', 'Payment received – thank you',
         'Your course is open. It stays yours as long as you study at least once a year.'
  from public.learners l where l.id = p_learner;
  return 'ok';
end $$;
revoke all on function public.grant_purchase(uuid, int[], text, text) from public, anon, authenticated;
grant execute on function public.grant_purchase(uuid, int[], text, text) to service_role;

create or replace function public.revoke_purchase(p_txn text)
returns int language plpgsql security definer set search_path = public as $$
declare n int;
begin
  update public.enrolments set status = 'refunded', updated_at = now() where provider_txn_id = p_txn and status = 'active';
  get diagnostics n = row_count;
  update public.purchases set status = 'refunded', updated_at = now() where provider_txn_id = p_txn;
  return n;
end $$;
revoke all on function public.revoke_purchase(text) from public, anon, authenticated;
grant execute on function public.revoke_purchase(text) to service_role;

-- 7. test checkout (Test project only): an expired course can be bought again; the year starts at the purchase
create or replace function public.enrol_stage(p_learner uuid, p_stage int, p_amount text default null)
returns text language plpgsql security definer set search_path = public as $$
declare v_level int := p_stage % 10;
begin
  if coalesce((select value from private.app_secrets where name = 'mock_payments'), 'off') <> 'on' then
    raise exception 'payments are not open yet' using errcode = 'P0001';
  end if;
  perform public.prepare_checkout(p_learner, array[p_stage]);
  update public.learners set stage = v_level, last_active_at = now() where id = p_learner;
  insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'test', p_amount)
  on conflict (learner_id, stage) do update set status = 'active', method = 'test', amount = excluded.amount, expired_at = null, updated_at = now();
  insert into public.notifications (parent_id, learner_id, kind, title, body)
  select coalesce(l.parent_id, l.user_id), l.id, 'billing',
         'You are enrolled in Stage ' || v_level || case when p_stage >= 20 then ' English (ESL)' when p_stage >= 10 then ' Mathematics' else ' Science' end,
         'Test checkout – no money was taken.'
  from public.learners l where l.id = p_learner;
  return 'ok';
end $$;
revoke all on function public.enrol_stage(uuid, int, text) from public, anon;
grant execute on function public.enrol_stage(uuid, int, text) to authenticated;

-- level progress counts only courses still open
create or replace function public.level_tests_pct(p_learner uuid, p_level int)
returns numeric language sql stable security definer set search_path = public as $$
  with keys as (select stage from public.enrolments where learner_id = p_learner and status = 'active' and stage % 10 = p_level),
       need as (select count(*) n from public.stage_units u join keys k on k.stage = u.stage),
       have as (select count(*) n from public.unit_results r join public.stage_units u on u.unit = r.unit join keys k on k.stage = u.stage where r.learner_id = p_learner)
  select case when (select n from need) = 0 then 0 else round(100.0 * (select n from have) / (select n from need), 1) end
$$;
revoke all on function public.level_tests_pct(uuid, int) from public, anon, authenticated;

-- 8. daily sweep at 03:17 UTC
create extension if not exists pg_cron;
do $$ begin
  perform cron.unschedule(jobid) from cron.job where jobname = 'expire-idle-learners';
  perform cron.schedule('expire-idle-learners', '17 3 * * *', 'select public.expire_idle_all()');
end $$;
