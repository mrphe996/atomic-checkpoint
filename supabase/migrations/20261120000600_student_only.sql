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
