-- Atomic Checkpoint: whole database in one script (Supabase → SQL editor → Run). Generated from supabase/migrations + seed.

-- ===== supabase/migrations/20261120000100_init.sql =====
-- Atomic Checkpoint — core schema (Supabase / Postgres 15+)
-- Model: a PARENT account (adult, signs in, consents, pays) owns one or more LEARNER profiles (children).
-- Children never create accounts or give an email address: data minimisation for UK Children's Code,
-- Singapore PDPA (parental consent under 13) and Vietnam PDPL (parental consent under 16).

create extension if not exists pgcrypto;

-- ---------- accounts ----------
create table public.profiles (
  id uuid primary key references auth.users (id) on delete cascade,
  role text not null default 'parent' check (role in ('parent', 'marker', 'admin')),
  display_name text not null default '' check (char_length(display_name) <= 80),
  country text not null default 'GB' check (country ~ '^[A-Z]{2}$'),
  weekly_report boolean not null default false,      -- optional emails: OFF by default (high privacy by default)
  marketing_opt_in boolean not null default false,
  product_analytics boolean not null default false,   -- optional analytics: OFF by default
  created_at timestamptz not null default now()
);

create table public.consents (
  id bigint generated always as identity primary key,
  parent_id uuid not null references public.profiles (id) on delete cascade,
  learner_id uuid,
  kind text not null check (kind in ('terms', 'privacy', 'parental_consent', 'leaderboard', 'marketing', 'product_analytics')),
  version text not null,
  given boolean not null default true,
  at timestamptz not null default now()
);

create table public.learners (
  id uuid primary key default gen_random_uuid(),
  parent_id uuid not null references public.profiles (id) on delete cascade,
  nickname text not null check (char_length(nickname) between 2 and 24),
  certificate_name text check (certificate_name is null or char_length(certificate_name) <= 80),
  birth_year int check (birth_year is null or birth_year between 2005 and 2022),
  stage int not null default 7 check (stage between 7 and 9),
  leaderboard_opt_in boolean not null default false,  -- hidden from the leaderboard unless a parent switches it on
  created_at timestamptz not null default now()
);
create index on public.learners (parent_id);

-- ---------- learning ----------
create table public.stage_units (
  stage int not null,
  unit text not null,
  title text not null,
  free_sections text[] not null default '{3.1}',
  primary key (stage, unit)
);

create table public.progress (
  learner_id uuid not null references public.learners (id) on delete cascade,
  unit text not null,
  state jsonb not null default '{}'::jsonb,           -- videos, pause questions, practice records, notes
  updated_at timestamptz not null default now(),
  primary key (learner_id, unit)
);

create table public.attempts (
  id uuid primary key default gen_random_uuid(),
  learner_id uuid not null references public.learners (id) on delete cascade,
  unit text not null,
  n int not null,
  form text not null,
  client_key text not null,                           -- idempotency: a double submit returns the same attempt
  answers jsonb not null,
  per jsonb not null,
  auto numeric not null,
  score numeric,
  pct numeric,
  status text not null check (status in ('pending', 'final')),
  passed boolean,
  by_obj jsonb,
  weak text[],
  remed text[],
  marked_by uuid references public.profiles (id),
  created_at timestamptz not null default now(),
  finalised_at timestamptz,
  unique (learner_id, unit, client_key),
  unique (learner_id, unit, n)
);
create index on public.attempts (status) where status = 'pending';

create table public.unit_results (                    -- ranking input: % of the FIRST passing attempt, fixed forever
  learner_id uuid not null references public.learners (id) on delete cascade,
  unit text not null,
  stage int not null default 7,
  first_pass_pct numeric not null,
  first_pass_at timestamptz not null default now(),
  attempt_id uuid not null references public.attempts (id) on delete cascade,
  primary key (learner_id, unit)
);

create table public.certificates (
  learner_id uuid not null references public.learners (id) on delete cascade,
  stage int not null,
  code text not null unique,
  name_on_certificate text not null,
  issued_at timestamptz not null default now(),
  primary key (learner_id, stage)
);

-- ---------- money ----------
create table public.subscriptions (
  id bigint generated always as identity primary key,
  parent_id uuid not null references public.profiles (id) on delete cascade,
  provider text not null default 'paddle',
  provider_subscription_id text not null unique,
  plan text not null,                                 -- e.g. stage7_monthly, stage7_yearly
  status text not null,                               -- trialing, active, past_due, paused, canceled
  current_period_end timestamptz,
  updated_at timestamptz not null default now()
);
create index on public.subscriptions (parent_id);

-- ---------- support, notifications, analytics ----------
create table public.reports (
  id bigint generated always as identity primary key,
  reporter_id uuid not null references public.profiles (id) on delete cascade,
  learner_id uuid references public.learners (id) on delete set null,
  unit text,
  question_id text,
  kind text not null check (kind in ('wrong_answer', 'typo', 'unclear', 'video', 'bug', 'billing', 'other')),
  message text not null check (char_length(message) between 3 and 2000),
  status text not null default 'open' check (status in ('open', 'fixed', 'closed')),
  created_at timestamptz not null default now()
);

create table public.notifications (
  id bigint generated always as identity primary key,
  parent_id uuid not null references public.profiles (id) on delete cascade,
  learner_id uuid references public.learners (id) on delete cascade,
  kind text not null,
  title text not null,
  body text not null default '',
  read_at timestamptz,
  created_at timestamptz not null default now()
);

create table public.events (                          -- first-party only; no third-party trackers
  id bigint generated always as identity primary key,
  learner_id uuid references public.learners (id) on delete cascade,
  parent_id uuid references public.profiles (id) on delete cascade,
  name text not null,
  props jsonb not null default '{}'::jsonb,
  essential boolean not null default true,            -- essential = needed to run the course (e.g. answer stats)
  at timestamptz not null default now()
);
create index on public.events (name, at);

-- ---------- helpers ----------
create or replace function public.is_staff() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role in ('marker', 'admin'));
$$;

create or replace function public.owns_learner(l uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.learners where id = l and parent_id = auth.uid());
$$;

-- new auth user → profile row (display name and country from sign-up metadata)
create or replace function public.handle_new_user() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, display_name, country)
  values (new.id,
          coalesce(new.raw_user_meta_data ->> 'display_name', ''),
          coalesce(nullif(new.raw_user_meta_data ->> 'country', ''), 'GB'));
  return new;
end $$;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function public.handle_new_user();

-- first passing attempt fixes the ranking score for that unit (never changed by later attempts)
create or replace function public.record_first_pass() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if new.status = 'final' and new.passed then
    insert into public.unit_results (learner_id, unit, stage, first_pass_pct, attempt_id)
    values (new.learner_id, new.unit, coalesce((select stage from public.learners where id = new.learner_id), 7), new.pct, new.id)
    on conflict (learner_id, unit) do nothing;
    insert into public.notifications (parent_id, learner_id, kind, title, body)
    select l.parent_id, l.id, 'test_passed', l.nickname || ' passed ' || new.unit, 'Score ' || round(new.pct, 1) || '%'
    from public.learners l where l.id = new.learner_id;
  elsif new.status = 'final' and tg_op = 'UPDATE' and old.status = 'pending' then
    insert into public.notifications (parent_id, learner_id, kind, title, body)
    select l.parent_id, l.id, 'test_marked', l.nickname || '''s test has been marked', 'Score ' || round(new.pct, 1) || '%'
    from public.learners l where l.id = new.learner_id;
  end if;
  return new;
end $$;
create trigger attempts_first_pass after insert or update of status on public.attempts
  for each row execute function public.record_first_pass();

-- leaderboard: opted-in learners only, competition ranking (1, 2, 2, 4), formula = mean of first-pass % per unit
create or replace function public.leaderboard(p_stage int default 7)
returns table (rank bigint, nickname text, score numeric, units bigint, is_mine boolean)
language sql stable security definer set search_path = public as $$
  with s as (
    select l.id, l.nickname, l.parent_id, round(avg(r.first_pass_pct), 2) as score, count(*) as units
    from public.unit_results r join public.learners l on l.id = r.learner_id
    where r.stage = p_stage and (l.leaderboard_opt_in or l.parent_id = auth.uid())
    group by l.id, l.nickname, l.parent_id
  )
  select rank() over (order by score desc), nickname, score, units, parent_id = auth.uid()
  from s
  order by 1, 2;
$$;

-- certificate: one code per learner per stage, only when every unit of the stage has been passed
create or replace function public.issue_certificate(p_learner uuid, p_stage int default 7)
returns text language plpgsql security definer set search_path = public as $$
declare v_code text; v_need int; v_have int; v_name text;
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  select code into v_code from public.certificates where learner_id = p_learner and stage = p_stage;
  if v_code is not null then return v_code; end if;
  select count(*) into v_need from public.stage_units where stage = p_stage;
  select count(*) into v_have from public.unit_results r join public.stage_units u on u.unit = r.unit and u.stage = p_stage where r.learner_id = p_learner;
  if v_need = 0 or v_have < v_need then raise exception 'stage not complete (% of % units passed)', v_have, v_need using errcode = 'P0001'; end if;
  select coalesce(certificate_name, nickname) into v_name from public.learners where id = p_learner;
  v_code := 'AE-S' || p_stage || '-' || to_char(now(), 'YYYY') || '-' || upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 8));
  insert into public.certificates (learner_id, stage, code, name_on_certificate) values (p_learner, p_stage, v_code, v_name)
  on conflict (learner_id, stage) do nothing;
  select code into v_code from public.certificates where learner_id = p_learner and stage = p_stage;
  return v_code;
end $$;

-- public verification page: anyone with a code can confirm it is genuine (name + stage + date only)
create or replace function public.verify_certificate(p_code text)
returns table (name_on_certificate text, stage int, issued_at timestamptz)
language sql stable security definer set search_path = public as $$
  select name_on_certificate, stage, issued_at from public.certificates where code = upper(p_code);
$$;

-- access: active or trialing subscription
create or replace function public.has_subscription(p_parent uuid default auth.uid()) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.subscriptions where parent_id = p_parent and status in ('trialing', 'active', 'past_due')
                 and (current_period_end is null or current_period_end > now()));
$$;

-- staff: question statistics from answer events (first-try correct rate)
create or replace function public.item_stats(p_unit text)
returns table (question_id text, attempts bigint, first_try_correct numeric)
language sql stable security definer set search_path = public as $$
  select props ->> 'q', count(*), round(avg(case when (props ->> 'ok')::boolean and (props ->> 'try')::int = 1 then 1 else 0 end) * 100, 1)
  from public.events where name = 'answer' and props ->> 'unit' = p_unit and public.is_staff()
  group by 1 order by 3 asc;
$$;

-- ===== supabase/migrations/20261120000200_rls.sql =====
-- Row level security: every table is closed by default; parents see only their own family's rows.
alter table public.profiles enable row level security;
alter table public.consents enable row level security;
alter table public.learners enable row level security;
alter table public.stage_units enable row level security;
alter table public.progress enable row level security;
alter table public.attempts enable row level security;
alter table public.unit_results enable row level security;
alter table public.certificates enable row level security;
alter table public.subscriptions enable row level security;
alter table public.reports enable row level security;
alter table public.notifications enable row level security;
alter table public.events enable row level security;

-- profiles: own row; staff read all. Role can never be changed by the user.
create policy profiles_self_select on public.profiles for select using (id = auth.uid() or public.is_staff());
create policy profiles_self_update on public.profiles for update using (id = auth.uid())
  with check (id = auth.uid() and role = (select role from public.profiles p where p.id = auth.uid()));

create policy consents_own on public.consents for select using (parent_id = auth.uid());
create policy consents_insert on public.consents for insert with check (parent_id = auth.uid() and (learner_id is null or public.owns_learner(learner_id)));

create policy learners_own on public.learners for all using (parent_id = auth.uid()) with check (parent_id = auth.uid());
create policy learners_staff on public.learners for select using (public.is_staff());

create policy stage_units_read on public.stage_units for select using (true);

create policy progress_own on public.progress for all using (public.owns_learner(learner_id)) with check (public.owns_learner(learner_id));

-- attempts are written only by the server (api/submit-test, api/mark-attempt) with the service role
create policy attempts_read on public.attempts for select using (public.owns_learner(learner_id) or public.is_staff());

create policy results_read on public.unit_results for select using (public.owns_learner(learner_id));
create policy certs_read on public.certificates for select using (public.owns_learner(learner_id));
create policy subs_read on public.subscriptions for select using (parent_id = auth.uid());

create policy reports_insert on public.reports for insert with check (reporter_id = auth.uid() and (learner_id is null or public.owns_learner(learner_id)));
create policy reports_read on public.reports for select using (reporter_id = auth.uid() or public.is_staff());
create policy reports_staff_update on public.reports for update using (public.is_staff());

create policy notif_own on public.notifications for select using (parent_id = auth.uid());
create policy notif_mark_read on public.notifications for update using (parent_id = auth.uid()) with check (parent_id = auth.uid());

-- optional (non-essential) analytics only when the parent opted in
create policy events_insert on public.events for insert with check (
  (learner_id is null or public.owns_learner(learner_id)) and (parent_id is null or parent_id = auth.uid())
  and (essential or exists (select 1 from public.profiles where id = auth.uid() and product_analytics)));
create policy events_staff_read on public.events for select using (public.is_staff());

grant execute on function public.leaderboard(int), public.issue_certificate(uuid, int), public.has_subscription(uuid), public.item_stats(text) to authenticated;
grant execute on function public.verify_certificate(text) to anon, authenticated;

-- ===== supabase/migrations/20261120000300_harden.sql =====
-- Least privilege for functions: Postgres grants EXECUTE to PUBLIC by default.
revoke execute on function public.is_staff(), public.owns_learner(uuid), public.handle_new_user(), public.record_first_pass(),
  public.has_subscription(uuid), public.leaderboard(int), public.issue_certificate(uuid, int), public.item_stats(text),
  public.verify_certificate(text) from public, anon, authenticated;
-- called by signed-in parents / staff from the browser
grant execute on function public.leaderboard(int), public.issue_certificate(uuid, int), public.item_stats(text) to authenticated;
-- helpers used inside RLS policies must stay callable by the roles the policies run as
grant execute on function public.is_staff(), public.owns_learner(uuid) to authenticated;
-- public certificate check
grant execute on function public.verify_certificate(text) to anon, authenticated;
-- has_subscription is only called by the server (service role)
grant execute on function public.has_subscription(uuid) to service_role;

-- ===== supabase/migrations/20261120000400_grants.sql =====
-- Table privileges for the Data API. New Supabase projects no longer grant these by default;
-- row level security (20261120000200_rls.sql) still decides WHICH rows each role can touch.
grant usage on schema public to anon, authenticated, service_role;
grant select, update on public.profiles to authenticated;
grant select, insert on public.consents to authenticated;
grant select, insert, update, delete on public.learners to authenticated;
grant select on public.stage_units to anon, authenticated;
grant select, insert, update, delete on public.progress to authenticated;
grant select on public.attempts, public.unit_results, public.certificates, public.subscriptions to authenticated;
grant select, insert, update on public.reports to authenticated;
grant select, update on public.notifications to authenticated;
grant select, insert on public.events to authenticated;
grant usage, select on all sequences in schema public to authenticated;
grant all on all tables in schema public to service_role;
grant usage, select on all sequences in schema public to service_role;

-- ===== supabase/migrations/20261120000500_students.sql =====
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

-- ===== supabase/migrations/20261120000600_student_only.sql =====
-- Student-only model: students sign up themselves (country → school → grade), may add a parent's email,
-- and the parent gets an email when the student finishes a unit. No parent accounts are needed.

-- ---------- schools (bilingual and international schools offered at sign-up) ----------
create table public.schools (
  id bigint generated always as identity primary key,
  country text not null check (country ~ '^[A-Z]{2}$'),
  name text not null check (char_length(name) between 3 and 120),
  kind text not null default 'international' check (kind in ('international', 'bilingual')),
  city text,
  active boolean not null default true,
  unique (country, name)
);
alter table public.schools enable row level security;
create policy schools_read on public.schools for select using (active);
grant select on public.schools to anon, authenticated;
grant all on public.schools to service_role;

-- ---------- student profile ----------
alter table public.learners
  add column school_id bigint references public.schools (id) on delete set null,
  add column school_other text check (school_other is null or char_length(school_other) <= 120),
  add column grade text check (grade is null or char_length(grade) <= 40);

-- a student may change only these fields on their own row
create policy learners_student_update on public.learners for update using (user_id = auth.uid()) with check (user_id = auth.uid());
revoke update on public.learners from authenticated;
grant update (nickname, certificate_name, leaderboard_opt_in, parent_email, school_id, school_other, grade, birth_year) on public.learners to authenticated;

-- ---------- emails to parents (sent by the "mailer" function once an email provider is set up) ----------
create table public.email_outbox (
  id bigint generated always as identity primary key,
  learner_id uuid references public.learners (id) on delete cascade,
  to_email text not null,
  kind text not null,
  subject text not null,
  body text not null,
  status text not null default 'queued' check (status in ('queued', 'sent', 'failed', 'skipped')),
  error text,
  created_at timestamptz not null default now(),
  sent_at timestamptz
);
alter table public.email_outbox enable row level security;    -- no client policies: server only
grant all on public.email_outbox to service_role;

-- first pass of a unit: fix the ranking score, notify the student, queue the parent email
create or replace function public.record_first_pass() returns trigger
language plpgsql security definer set search_path = public as $$
declare v_l public.learners%rowtype; v_title text; v_n int;
begin
  select * into v_l from public.learners where id = new.learner_id;
  if new.status = 'final' and new.passed then
    insert into public.unit_results (learner_id, unit, stage, first_pass_pct, attempt_id)
    values (new.learner_id, new.unit, coalesce(v_l.stage, 7), new.pct, new.id)
    on conflict (learner_id, unit) do nothing;
    get diagnostics v_n = row_count;
    select title into v_title from public.stage_units where unit = new.unit;
    insert into public.notifications (parent_id, learner_id, kind, title, body)
    values (coalesce(v_l.parent_id, v_l.user_id), v_l.id, 'test_passed',
            'You passed Unit ' || ltrim(right(new.unit, 2), '0') || coalesce(': ' || v_title, '') || '!', 'Score ' || round(new.pct, 1) || '%');
    if v_n > 0 and v_l.parent_email is not null then
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
    values (coalesce(v_l.parent_id, v_l.user_id), v_l.id, 'test_marked', 'Your Unit Test has been marked', 'Score ' || round(new.pct, 1) || '%');
  end if;
  return new;
end $$;

-- ---------- starter list of schools (edit in the dashboard; students can also type a school that is not listed) ----------
insert into public.schools (country, name, kind, city) values
 ('VN', 'British International School Ho Chi Minh City', 'international', 'Ho Chi Minh City'),
 ('VN', 'British International School Hanoi', 'international', 'Hanoi'),
 ('VN', 'British Vietnamese International School Ho Chi Minh City', 'international', 'Ho Chi Minh City'),
 ('VN', 'British Vietnamese International School Hanoi', 'international', 'Hanoi'),
 ('VN', 'Saigon South International School', 'international', 'Ho Chi Minh City'),
 ('VN', 'International School Ho Chi Minh City', 'international', 'Ho Chi Minh City'),
 ('VN', 'Australian International School', 'international', 'Ho Chi Minh City'),
 ('VN', 'Renaissance International School Saigon', 'international', 'Ho Chi Minh City'),
 ('VN', 'United Nations International School of Hanoi', 'international', 'Hanoi'),
 ('VN', 'Hanoi International School', 'international', 'Hanoi'),
 ('VN', 'Concordia International School Hanoi', 'international', 'Hanoi'),
 ('VN', 'Reigate Grammar School Vietnam', 'international', 'Hanoi'),
 ('VN', 'QSI International School of Haiphong', 'international', 'Haiphong'),
 ('VN', 'Vinschool', 'bilingual', 'Hanoi / Ho Chi Minh City'),
 ('VN', 'Wellspring International Bilingual School', 'bilingual', 'Hanoi / Ho Chi Minh City'),
 ('VN', 'EMASI', 'bilingual', 'Ho Chi Minh City'),
 ('SG', 'Tanglin Trust School', 'international', 'Singapore'),
 ('SG', 'Dulwich College (Singapore)', 'international', 'Singapore'),
 ('SG', 'United World College of South East Asia', 'international', 'Singapore'),
 ('SG', 'Singapore American School', 'international', 'Singapore'),
 ('SG', 'Stamford American International School', 'international', 'Singapore'),
 ('SG', 'Dover Court International School', 'international', 'Singapore'),
 ('SG', 'Nexus International School (Singapore)', 'international', 'Singapore'),
 ('SG', 'Chatsworth International School', 'international', 'Singapore'),
 ('SG', 'Canadian International School', 'international', 'Singapore'),
 ('SG', 'Overseas Family School', 'international', 'Singapore'),
 ('MY', 'The Alice Smith School', 'international', 'Kuala Lumpur'),
 ('MY', 'Garden International School', 'international', 'Kuala Lumpur'),
 ('MY', 'ELC International School', 'international', 'Selangor'),
 ('MY', 'Kolej Tuanku Ja''afar', 'international', 'Negeri Sembilan'),
 ('MY', 'Epsom College in Malaysia', 'international', 'Negeri Sembilan'),
 ('MY', 'Marlborough College Malaysia', 'international', 'Johor'),
 ('MY', 'Nexus International School Malaysia', 'international', 'Putrajaya'),
 ('MY', 'Taylor''s International School', 'international', 'Kuala Lumpur'),
 ('MY', 'Sunway International School', 'international', 'Selangor'),
 ('TH', 'Shrewsbury International School Bangkok', 'international', 'Bangkok'),
 ('TH', 'Harrow International School Bangkok', 'international', 'Bangkok'),
 ('TH', 'Bangkok Patana School', 'international', 'Bangkok'),
 ('TH', 'NIST International School', 'international', 'Bangkok'),
 ('TH', 'International School Bangkok', 'international', 'Bangkok'),
 ('TH', 'Brighton College Bangkok', 'international', 'Bangkok'),
 ('TH', 'KIS International School', 'international', 'Bangkok'),
 ('ID', 'British School Jakarta', 'international', 'Jakarta'),
 ('ID', 'Jakarta Intercultural School', 'international', 'Jakarta'),
 ('ID', 'Sinarmas World Academy', 'international', 'Tangerang'),
 ('ID', 'Bali Island School', 'international', 'Bali'),
 ('ID', 'Mentari Intercultural School Jakarta', 'international', 'Jakarta'),
 ('PH', 'British School Manila', 'international', 'Manila'),
 ('PH', 'International School Manila', 'international', 'Manila'),
 ('PH', 'Brent International School', 'international', 'Manila'),
 ('PH', 'Southville International School and Colleges', 'international', 'Manila')
on conflict do nothing;

-- ===== supabase/seed.sql =====
-- Stage 7 units (Atomic course structure, aligned to the Cambridge Lower Secondary Science 0893 framework)
insert into public.stage_units (stage, unit, title) values
 (7, 'stage7-unit01', 'Introducing science'), (7, 'stage7-unit02', 'Measurements'), (7, 'stage7-unit03', 'Cells'),
 (7, 'stage7-unit04', 'Classifying living things'), (7, 'stage7-unit05', 'Food chains and food webs'),
 (7, 'stage7-unit06', 'Materials and their structure'), (7, 'stage7-unit07', 'Properties of materials'),
 (7, 'stage7-unit08', 'Acids and alkalis'), (7, 'stage7-unit09', 'Chemical reactions'), (7, 'stage7-unit10', 'Forces'),
 (7, 'stage7-unit11', 'Energy'), (7, 'stage7-unit12', 'Electricity'), (7, 'stage7-unit13', 'Earth processes'),
 (7, 'stage7-unit14', 'Earth and beyond')
on conflict do nothing;
