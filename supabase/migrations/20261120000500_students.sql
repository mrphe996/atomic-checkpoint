-- Students sign up themselves (email + password). Under the parental-consent age of their country the account
-- stays "pending" until a parent opens the approval link and consents; until then the app keeps the child's
-- progress only in their own browser and only the free topic is open.

alter table public.profiles drop constraint if exists profiles_role_check;
alter table public.profiles add constraint profiles_role_check check (role in ('parent', 'student', 'marker', 'admin'));

alter table public.learners alter column parent_id drop not null;
alter table public.learners
  add column user_id uuid unique references public.profiles (id) on delete cascade,     -- the student's own login (null = child added by a parent)
  add column consent_status text not null default 'approved' check (consent_status in ('pending', 'approved', 'not_required')),
  add column invite_code text unique,                                                    -- parent approval link, cleared once approved
  add column parent_email text check (parent_email is null or char_length(parent_email) <= 200),
  add column country text check (country is null or country ~ '^[A-Z]{2}$');
alter table public.learners add constraint learners_has_owner check (parent_id is not null or user_id is not null);
create index on public.learners (user_id);

-- new auth user → profile; only 'parent' or 'student' can come from sign-up metadata (never staff roles)
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, display_name, country, role)
  values (new.id,
          coalesce(new.raw_user_meta_data ->> 'display_name', ''),
          coalesce(nullif(new.raw_user_meta_data ->> 'country', ''), 'GB'),
          case when new.raw_user_meta_data ->> 'role' = 'student' then 'student' else 'parent' end);
  return new;
end $$;

-- "can use this learner's records": the parent, or the student once consent is settled
create or replace function public.owns_learner(l uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.learners where id = l
                 and (parent_id = auth.uid() or (user_id = auth.uid() and consent_status <> 'pending')));
$$;

-- learners: a student can read their own row (to show approval status and link); only parents change rows
drop policy if exists learners_own on public.learners;
create policy learners_parent_all on public.learners for all using (parent_id = auth.uid()) with check (parent_id = auth.uid());
create policy learners_student_read on public.learners for select using (user_id = auth.uid());

-- parent side of the approval link
create or replace function public.learner_invite(p_code text)
returns table (nickname text, birth_year int, country text, created_at timestamptz)
language sql stable security definer set search_path = public as $$
  select nickname, birth_year, country, created_at from public.learners
  where invite_code = upper(p_code) and consent_status = 'pending';
$$;

create or replace function public.approve_learner(p_code text)
returns uuid language plpgsql security definer set search_path = public as $$
declare v_id uuid; v_role text;
begin
  select role into v_role from public.profiles where id = auth.uid();
  if v_role is distinct from 'parent' then raise exception 'only a parent account can approve' using errcode = '42501'; end if;
  update public.learners set parent_id = auth.uid(), consent_status = 'approved', invite_code = null
   where invite_code = upper(p_code) and consent_status = 'pending' returning id into v_id;
  if v_id is null then raise exception 'invite not found or already used' using errcode = 'P0002'; end if;
  insert into public.consents (parent_id, learner_id, kind, version) values (auth.uid(), v_id, 'parental_consent', 'approval-link');
  insert into public.notifications (parent_id, learner_id, kind, title, body)
  select auth.uid(), v_id, 'approved', nickname || ' is now linked to your account', 'You can see their progress in the parent area.' from public.learners where id = v_id;
  return v_id;
end $$;

-- leaderboard: a student also sees their own row
create or replace function public.leaderboard(p_stage int default 7)
returns table (rank bigint, nickname text, score numeric, units bigint, is_mine boolean)
language sql stable security definer set search_path = public as $$
  with s as (
    select l.id, l.nickname, (l.parent_id = auth.uid() or l.user_id = auth.uid()) as mine,
           round(avg(r.first_pass_pct), 2) as score, count(*) as units
    from public.unit_results r join public.learners l on l.id = r.learner_id
    where r.stage = p_stage and (l.leaderboard_opt_in or l.parent_id = auth.uid() or l.user_id = auth.uid())
    group by l.id, l.nickname, l.parent_id, l.user_id
  )
  select rank() over (order by score desc), nickname, score, coalesce(units, 0), coalesce(mine, false) from s order by 1, 2;
$$;

revoke execute on function public.learner_invite(text), public.approve_learner(text), public.leaderboard(int), public.owns_learner(uuid), public.handle_new_user() from public, anon;
grant execute on function public.learner_invite(text), public.approve_learner(text), public.leaderboard(int), public.owns_learner(uuid) to authenticated;
