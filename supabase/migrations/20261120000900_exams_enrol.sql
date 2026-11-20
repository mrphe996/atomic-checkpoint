-- Exam room timer, end-of-year exams, stage enrolment (test checkout) and the stage certificate rule.

-- ---------- exam room: when each paper was opened (the server times the attempt) ----------
create table if not exists public.test_starts (
  learner_id uuid not null references public.learners (id) on delete cascade,
  unit text not null,
  form text not null,
  started_at timestamptz not null default now(),
  primary key (learner_id, unit, form)
);
alter table public.test_starts enable row level security;
create policy test_starts_read on public.test_starts for select using (public.owns_learner(learner_id));
grant select on public.test_starts to authenticated;
grant all on public.test_starts to service_role;

alter table public.attempts add column if not exists started_at timestamptz;
alter table public.attempts add column if not exists duration_s int;
alter table public.attempts add column if not exists overtime boolean not null default false;

-- ---------- end-of-year exams are not units: keep them out of unit_results / the leaderboard ----------
create or replace function public.record_first_pass() returns trigger
language plpgsql security definer set search_path = public as $$
declare v_l public.learners%rowtype; v_title text; v_n int; v_final boolean := new.unit like '%-final';
begin
  select * into v_l from public.learners where id = new.learner_id;
  if new.status = 'final' and new.passed then
    if not v_final then
      insert into public.unit_results (learner_id, unit, stage, first_pass_pct, attempt_id)
      values (new.learner_id, new.unit, coalesce(v_l.stage, 7), new.pct, new.id)
      on conflict (learner_id, unit) do nothing;
      get diagnostics v_n = row_count;
      select title into v_title from public.stage_units where unit = new.unit;
    end if;
    insert into public.notifications (parent_id, learner_id, kind, title, body)
    values (coalesce(v_l.parent_id, v_l.user_id), v_l.id, 'test_passed',
            case when v_final then 'You passed the end-of-year exam (paper ' || new.form || ')!'
                 else 'You passed Unit ' || ltrim(right(new.unit, 2), '0') || coalesce(': ' || v_title, '') || '!' end,
            'Score ' || round(new.pct, 1) || '%');
    if not v_final and v_n > 0 and v_l.parent_email is not null then
      insert into public.email_outbox (learner_id, to_email, kind, subject, body)
      values (v_l.id, v_l.parent_email, 'unit_complete',
        v_l.nickname || ' has finished Unit ' || ltrim(right(new.unit, 2), '0') || coalesce(': ' || v_title, '') || ' on Atomic',
        'Hello,' || E'\n\n' || v_l.nickname || ' has just finished Unit ' || ltrim(right(new.unit, 2), '0') || coalesce(' (' || v_title || ')', '')
        || ' of Cambridge Lower Secondary Science Stage ' || coalesce(v_l.stage, 7) || ' on Atomic, passing the Unit Test with ' || round(new.pct, 1) || '%.'
        || E'\n\n' || 'You are receiving this because ' || v_l.nickname || ' added your email address when signing up. They can remove it at any time in their settings.'
        || E'\n\n' || 'The Atomic teaching team');
    end if;
  elsif new.status = 'final' and tg_op = 'UPDATE' and old.status = 'pending' then
    insert into public.notifications (parent_id, learner_id, kind, title, body)
    values (coalesce(v_l.parent_id, v_l.user_id), v_l.id, 'test_marked', 'Your test has been marked', 'Score ' || round(new.pct, 1) || '%');
  end if;
  return new;
end $$;

-- ---------- stage enrolment: the stage chosen at sign-up is included; any other stage needs an enrolment ----------
create table if not exists public.enrolments (
  learner_id uuid not null references public.learners (id) on delete cascade,
  stage int not null check (stage between 7 and 9),
  method text not null default 'test',          -- 'test' (simulated checkout) or 'paddle'
  amount text,
  status text not null default 'active',
  created_at timestamptz not null default now(),
  primary key (learner_id, stage)
);
alter table public.enrolments enable row level security;
create policy enrolments_read on public.enrolments for select using (public.owns_learner(learner_id));
grant select on public.enrolments to authenticated;
grant all on public.enrolments to service_role;

-- simulated checkout: only works where the 'mock_payments' setting is 'on' (the Test project)
create or replace function public.enrol_stage(p_learner uuid, p_stage int, p_amount text default null)
returns text language plpgsql security definer set search_path = public as $$
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  if p_stage not between 7 and 9 then raise exception 'bad stage' using errcode = '22023'; end if;
  if coalesce((select value from private.app_secrets where name = 'mock_payments'), 'off') <> 'on' then
    raise exception 'payments are not open yet' using errcode = 'P0001';
  end if;
  insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'test', p_amount)
  on conflict (learner_id, stage) do nothing;
  insert into public.notifications (parent_id, learner_id, kind, title, body)
  select coalesce(l.parent_id, l.user_id), l.id, 'billing', 'You are enrolled in Stage ' || p_stage, 'Test checkout – no money was taken.'
  from public.learners l where l.id = p_learner;
  return 'ok';
end $$;
revoke all on function public.enrol_stage(uuid, int, text) from public, anon;
grant execute on function public.enrol_stage(uuid, int, text) to authenticated;

-- ---------- certificate: every unit of the stage passed AND an end-of-year exam passed ----------
create or replace function public.issue_certificate(p_learner uuid, p_stage int default 7)
returns text language plpgsql security definer set search_path = public as $$
declare v_code text; v_need int; v_have int; v_name text; v_final boolean;
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  select code into v_code from public.certificates where learner_id = p_learner and stage = p_stage;
  if v_code is not null then return v_code; end if;
  select count(*) into v_need from public.stage_units where stage = p_stage;
  select count(*) into v_have from public.unit_results r join public.stage_units u on u.unit = r.unit and u.stage = p_stage where r.learner_id = p_learner;
  if v_need = 0 or v_have < v_need then raise exception 'stage not complete (% of % units passed)', v_have, v_need using errcode = 'P0001'; end if;
  select exists (select 1 from public.attempts where learner_id = p_learner and unit = 'stage' || p_stage || '-final' and status = 'final' and passed) into v_final;
  if not v_final then raise exception 'end-of-year exam not passed yet' using errcode = 'P0001'; end if;
  select coalesce(certificate_name, nickname) into v_name from public.learners where id = p_learner;
  v_code := 'AE-S' || p_stage || '-' || to_char(now(), 'YYYY') || '-' || upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 8));
  insert into public.certificates (learner_id, stage, code, name_on_certificate) values (p_learner, p_stage, v_code, v_name)
  on conflict (learner_id, stage) do nothing;
  select code into v_code from public.certificates where learner_id = p_learner and stage = p_stage;
  return v_code;
end $$;
