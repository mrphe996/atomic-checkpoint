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
