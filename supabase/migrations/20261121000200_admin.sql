-- Admin console: user management, course/question overrides, exam control, announcements, settings and an audit log.
-- Every admin action goes through a security-definer function that checks public.is_admin() and writes public.admin_audit.

-- ---------- helpers ----------
create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.profiles where id = auth.uid() and role = 'admin');
$$;
revoke all on function public.is_admin() from public, anon;
grant execute on function public.is_admin() to authenticated;

alter table public.profiles add column if not exists disabled boolean not null default false;

create table if not exists public.admin_audit (
  id bigint generated always as identity primary key,
  at timestamptz not null default now(),
  actor uuid,
  action text not null,
  target text,
  detail jsonb not null default '{}'::jsonb
);
create index if not exists admin_audit_at on public.admin_audit (at desc);
alter table public.admin_audit enable row level security;
create policy admin_audit_read on public.admin_audit for select using (public.is_admin());
grant select on public.admin_audit to authenticated;
grant all on public.admin_audit to service_role;

create or replace function public.admin_log(p_action text, p_target text, p_detail jsonb default '{}'::jsonb) returns void
language sql security definer set search_path = public as $$
  insert into public.admin_audit (actor, action, target, detail) values (auth.uid(), p_action, p_target, coalesce(p_detail, '{}'::jsonb));
$$;
revoke all on function public.admin_log(text, text, jsonb) from public, anon, authenticated;

create or replace function public.admin_guard() returns void
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'admin only' using errcode = '42501'; end if;
end $$;
revoke all on function public.admin_guard() from public, anon, authenticated;

-- ---------- course and question overrides ----------
create table if not exists public.unit_settings (
  unit text primary key check (unit ~ '^stage[0-9]+-(unit[0-9]{2}|final|cp)$'),
  hidden boolean not null default false,
  note text,
  updated_at timestamptz not null default now(),
  updated_by uuid
);
alter table public.unit_settings enable row level security;
create policy unit_settings_read on public.unit_settings for select using (true);
grant select on public.unit_settings to anon, authenticated;
grant all on public.unit_settings to service_role;

-- public_patch: what any learner may see (for test questions: no answers); key_patch: the full question incl. answers.
-- Rows are read by learners only through content_overrides() (no answers of test questions); the server reads them directly.
create table if not exists public.question_overrides (
  question_id text primary key check (char_length(question_id) between 1 and 80),
  unit text not null,
  is_test boolean not null default false,
  hidden boolean not null default false,
  public_patch jsonb,
  key_patch jsonb,
  updated_at timestamptz not null default now(),
  updated_by uuid
);
create index if not exists question_overrides_unit on public.question_overrides (unit);
alter table public.question_overrides enable row level security;
create policy question_overrides_admin on public.question_overrides for select using (public.is_admin());
grant select on public.question_overrides to authenticated;
grant all on public.question_overrides to service_role;

create or replace function public.content_overrides(p_unit text)
returns table (question_id text, hidden boolean, patch jsonb)
language sql stable security definer set search_path = public as $$
  select o.question_id, o.hidden, case when o.is_test then o.public_patch else coalesce(o.key_patch, o.public_patch) end
  from public.question_overrides o where o.unit = p_unit;
$$;
revoke all on function public.content_overrides(text) from public;
grant execute on function public.content_overrides(text) to anon, authenticated;

-- ---------- announcements ----------
create table if not exists public.announcements (
  id bigint generated always as identity primary key,
  title text not null check (char_length(title) between 2 and 120),
  body text not null default '' check (char_length(body) <= 1000),
  audience text not null default 'all' check (audience in ('all', '7', '8', '9', '19')),
  level text not null default 'info' check (level in ('info', 'warn')),
  active boolean not null default true,
  created_at timestamptz not null default now(),
  created_by uuid
);
alter table public.announcements enable row level security;
create policy announcements_read on public.announcements for select using (active or public.is_admin());
grant select on public.announcements to anon, authenticated;
grant all on public.announcements to service_role;

-- ---------- disabled accounts cannot use the course ----------
create or replace function public.is_disabled() returns boolean
language sql stable security definer set search_path = public as $$
  select coalesce((select disabled from public.profiles where id = auth.uid()), false);
$$;
grant execute on function public.is_disabled() to authenticated;

-- ---------- overview ----------
create or replace function public.admin_overview() returns jsonb
language plpgsql stable security definer set search_path = public, auth as $$
declare r jsonb;
begin
  perform public.admin_guard();
  select jsonb_build_object(
    'accounts', (select count(*) from public.profiles),
    'by_role', (select coalesce(jsonb_object_agg(role, n), '{}') from (select role, count(*) n from public.profiles group by role) x),
    'disabled', (select count(*) from public.profiles where disabled),
    'learners', (select count(*) from public.learners),
    'testers', (select count(*) from public.testers),
    'active_7d', (select count(distinct learner_id) from public.progress where updated_at > now() - interval '7 days'),
    'active_30d', (select count(distinct learner_id) from public.progress where updated_at > now() - interval '30 days'),
    'signups_14d', (select coalesce(jsonb_agg(jsonb_build_object('day', d, 'n', n) order by d), '[]') from (
        select to_char(g::date, 'YYYY-MM-DD') d, (select count(*) from public.profiles p where p.created_at::date = g::date) n
        from generate_series(current_date - 13, current_date, interval '1 day') g) s),
    'attempts_7d', (select count(*) from public.attempts where created_at > now() - interval '7 days'),
    'attempts_total', (select count(*) from public.attempts),
    'pending_marking', (select count(*) from public.attempts where status = 'pending'),
    'open_reports', (select count(*) from public.reports where status = 'open'),
    'enrolments', (select coalesce(jsonb_object_agg(stage, n), '{}') from (select stage, count(*) n from public.enrolments where status = 'active' group by stage) x),
    'certificates', (select count(*) from public.certificates),
    'units', (select coalesce(jsonb_agg(jsonb_build_object('unit', unit, 'attempts', a, 'passed', p, 'avg_pct', avg_pct) order by unit), '[]') from (
        select unit, count(*) a, count(*) filter (where passed) p, round(avg(pct), 1) avg_pct from public.attempts where status = 'final' group by unit) u),
    'overrides', (select count(*) from public.question_overrides),
    'hidden_units', (select count(*) from public.unit_settings where hidden)
  ) into r;
  return r;
end $$;

-- ---------- users ----------
create or replace function public.admin_users(p_q text default '', p_limit int default 50, p_offset int default 0)
returns table (id uuid, email text, role text, display_name text, country text, disabled boolean, created_at timestamptz, last_sign_in_at timestamptz, learners bigint, total bigint)
language plpgsql stable security definer set search_path = public, auth as $$
begin
  perform public.admin_guard();
  return query
  with m as (
    select p.id, u.email::text, p.role, p.display_name, p.country, p.disabled, p.created_at, u.last_sign_in_at
    from public.profiles p left join auth.users u on u.id = p.id
    where coalesce(p_q, '') = '' or u.email ilike '%' || p_q || '%' or p.display_name ilike '%' || p_q || '%' or p.role = p_q
       or exists (select 1 from public.learners l where (l.user_id = p.id or l.parent_id = p.id) and l.nickname ilike '%' || p_q || '%'))
  select m.*, (select count(*) from public.learners l where l.user_id = m.id or l.parent_id = m.id), count(*) over ()
  from m order by m.created_at desc limit least(greatest(p_limit, 1), 200) offset greatest(p_offset, 0);
end $$;

create or replace function public.admin_user(p_id uuid) returns jsonb
language plpgsql stable security definer set search_path = public, auth as $$
declare r jsonb;
begin
  perform public.admin_guard();
  select jsonb_build_object(
    'profile', to_jsonb(p) || jsonb_build_object('email', u.email, 'last_sign_in_at', u.last_sign_in_at),
    'subscription', (select to_jsonb(s) from public.subscriptions s where s.parent_id = p.id order by s.updated_at desc limit 1),
    'learners', (select coalesce(jsonb_agg(jsonb_build_object(
        'learner', to_jsonb(l),
        'tester', exists (select 1 from public.testers t where t.learner_id = l.id),
        'enrolments', (select coalesce(jsonb_agg(to_jsonb(e)), '[]') from public.enrolments e where e.learner_id = l.id),
        'results', (select coalesce(jsonb_agg(jsonb_build_object('unit', r.unit, 'pct', r.first_pass_pct, 'at', r.first_pass_at) order by r.unit), '[]') from public.unit_results r where r.learner_id = l.id),
        'attempts', (select coalesce(jsonb_agg(jsonb_build_object('id', a.id, 'unit', a.unit, 'n', a.n, 'form', a.form, 'status', a.status, 'score', a.score, 'pct', a.pct, 'passed', a.passed, 'created_at', a.created_at, 'leaves', a.leaves, 'overtime', a.overtime) order by a.created_at desc), '[]') from public.attempts a where a.learner_id = l.id),
        'progress', (select coalesce(jsonb_agg(jsonb_build_object('unit', g.unit, 'updated_at', g.updated_at, 'items', (select count(*) from jsonb_object_keys(coalesce(g.state -> 'items', '{}'::jsonb)))) order by g.unit), '[]') from public.progress g where g.learner_id = l.id),
        'certificates', (select coalesce(jsonb_agg(to_jsonb(c)), '[]') from public.certificates c where c.learner_id = l.id)
      )), '[]') from public.learners l where l.user_id = p.id or l.parent_id = p.id)
  ) into r
  from public.profiles p left join auth.users u on u.id = p.id where p.id = p_id;
  if r is null then raise exception 'not found' using errcode = 'P0002'; end if;
  return r;
end $$;

create or replace function public.admin_set_role(p_user uuid, p_role text) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  if p_role not in ('parent', 'student', 'marker', 'admin') then raise exception 'bad role' using errcode = '22023'; end if;
  if p_user = auth.uid() and p_role <> 'admin' then raise exception 'you cannot remove your own admin role' using errcode = 'P0001'; end if;
  update public.profiles set role = p_role where id = p_user;
  perform public.admin_log('set_role', p_user::text, jsonb_build_object('role', p_role));
end $$;

create or replace function public.admin_set_disabled(p_user uuid, p_on boolean) returns void
language plpgsql security definer set search_path = public, auth as $$
begin
  perform public.admin_guard();
  if p_user = auth.uid() then raise exception 'you cannot disable your own account' using errcode = 'P0001'; end if;
  update public.profiles set disabled = p_on where id = p_user;
  update auth.users set banned_until = case when p_on then 'infinity'::timestamptz else null end where id = p_user;
  perform public.admin_log(case when p_on then 'disable_account' else 'enable_account' end, p_user::text, '{}');
end $$;

create or replace function public.admin_set_tester(p_learner uuid, p_on boolean) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  if p_on then insert into public.testers (learner_id, note) values (p_learner, 'set by admin') on conflict do nothing;
  else delete from public.testers where learner_id = p_learner; end if;
  perform public.admin_log(case when p_on then 'tester_on' else 'tester_off' end, p_learner::text, '{}');
end $$;

create or replace function public.admin_set_enrolment(p_learner uuid, p_stage int, p_on boolean) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  if p_stage not in (7, 8, 9, 19) then raise exception 'bad stage' using errcode = '22023'; end if;
  if p_on then insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'admin', null) on conflict (learner_id, stage) do update set status = 'active';
  else delete from public.enrolments where learner_id = p_learner and stage = p_stage; end if;
  perform public.admin_log(case when p_on then 'enrol' else 'unenrol' end, p_learner::text, jsonb_build_object('stage', p_stage));
end $$;

create or replace function public.admin_reset_progress(p_learner uuid, p_unit text) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  delete from public.progress where learner_id = p_learner and unit = p_unit;
  perform public.admin_log('reset_progress', p_learner::text, jsonb_build_object('unit', p_unit));
end $$;

-- ---------- exams ----------
create or replace function public.admin_attempts(p_unit text default '', p_status text default '', p_limit int default 100)
returns table (id uuid, learner_id uuid, nickname text, email text, unit text, n int, form text, status text, score numeric, pct numeric, passed boolean, created_at timestamptz, leaves int, overtime boolean, duration_s int)
language plpgsql stable security definer set search_path = public, auth as $$
begin
  perform public.admin_guard();
  return query
  select a.id, a.learner_id, l.nickname::text, u.email::text, a.unit, a.n, a.form, a.status, a.score, a.pct, a.passed, a.created_at, a.leaves, a.overtime, a.duration_s
  from public.attempts a join public.learners l on l.id = a.learner_id left join auth.users u on u.id = coalesce(l.user_id, l.parent_id)
  where (coalesce(p_unit, '') = '' or a.unit = p_unit or a.unit like p_unit || '-%') and (coalesce(p_status, '') = '' or a.status = p_status)
  order by a.created_at desc limit least(greatest(p_limit, 1), 500);
end $$;

create or replace function public.admin_void_attempt(p_attempt uuid) returns void
language plpgsql security definer set search_path = public as $$
declare v public.attempts%rowtype;
begin
  perform public.admin_guard();
  select * into v from public.attempts where id = p_attempt;
  if not found then raise exception 'not found' using errcode = 'P0002'; end if;
  delete from public.attempts where id = p_attempt;   -- unit_results of this attempt go with it (on delete cascade)
  perform public.admin_log('void_attempt', p_attempt::text, jsonb_build_object('learner', v.learner_id, 'unit', v.unit, 'form', v.form, 'score', v.score));
end $$;

-- ---------- content ----------
create or replace function public.admin_set_unit(p_unit text, p_hidden boolean, p_note text default null) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  insert into public.unit_settings (unit, hidden, note, updated_at, updated_by) values (p_unit, p_hidden, p_note, now(), auth.uid())
  on conflict (unit) do update set hidden = excluded.hidden, note = excluded.note, updated_at = now(), updated_by = auth.uid();
  perform public.admin_log(case when p_hidden then 'hide_unit' else 'show_unit' end, p_unit, jsonb_build_object('note', p_note));
end $$;

create or replace function public.admin_overrides(p_unit text)
returns setof public.question_overrides
language plpgsql stable security definer set search_path = public as $$
begin
  perform public.admin_guard();
  return query select * from public.question_overrides where unit = p_unit order by question_id;
end $$;

create or replace function public.admin_save_question(p_qid text, p_unit text, p_is_test boolean, p_hidden boolean, p_public jsonb, p_key jsonb) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  if p_unit !~ '^stage[0-9]+-(unit[0-9]{2}|final|cp)$' then raise exception 'bad unit' using errcode = '22023'; end if;
  if p_public is not null and (p_public ? 'answer' or p_public ? 'model' or p_public ? 'rubric' or p_public ? 'accept' or p_public ? 'expr') and p_is_test then
    raise exception 'public patch of a test question must not contain answers' using errcode = '22023'; end if;
  insert into public.question_overrides (question_id, unit, is_test, hidden, public_patch, key_patch, updated_at, updated_by)
  values (p_qid, p_unit, p_is_test, coalesce(p_hidden, false), p_public, p_key, now(), auth.uid())
  on conflict (question_id) do update set unit = excluded.unit, is_test = excluded.is_test, hidden = excluded.hidden,
    public_patch = excluded.public_patch, key_patch = excluded.key_patch, updated_at = now(), updated_by = auth.uid();
  perform public.admin_log('edit_question', p_qid, jsonb_build_object('unit', p_unit, 'hidden', p_hidden, 'edited', p_key is not null));
end $$;

create or replace function public.admin_reset_question(p_qid text) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  delete from public.question_overrides where question_id = p_qid;
  perform public.admin_log('reset_question', p_qid, '{}');
end $$;

-- ---------- announcements & settings ----------
create or replace function public.admin_announce(p_title text, p_body text, p_audience text default 'all', p_level text default 'info') returns bigint
language plpgsql security definer set search_path = public as $$
declare v bigint;
begin
  perform public.admin_guard();
  insert into public.announcements (title, body, audience, level, created_by) values (p_title, coalesce(p_body, ''), coalesce(p_audience, 'all'), coalesce(p_level, 'info'), auth.uid()) returning id into v;
  perform public.admin_log('announce', v::text, jsonb_build_object('title', p_title, 'audience', p_audience));
  return v;
end $$;

create or replace function public.admin_set_announcement(p_id bigint, p_active boolean) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  update public.announcements set active = p_active where id = p_id;
  perform public.admin_log(case when p_active then 'announcement_on' else 'announcement_off' end, p_id::text, '{}');
end $$;

create or replace function public.admin_settings() returns jsonb
language plpgsql stable security definer set search_path = public, private as $$
begin
  perform public.admin_guard();
  return jsonb_build_object('mock_payments', coalesce((select value from private.app_secrets where name = 'mock_payments'), 'off'));
end $$;

create or replace function public.admin_set_setting(p_name text, p_value text) returns void
language plpgsql security definer set search_path = public, private as $$
begin
  perform public.admin_guard();
  if p_name <> 'mock_payments' or p_value not in ('on', 'off') then raise exception 'setting not allowed' using errcode = '22023'; end if;
  insert into private.app_secrets (name, value) values (p_name, p_value) on conflict (name) do update set value = excluded.value;
  perform public.admin_log('setting', p_name, jsonb_build_object('value', p_value));
end $$;

create or replace function public.admin_audit_log(p_limit int default 200)
returns table (id bigint, at timestamptz, actor_email text, action text, target text, detail jsonb)
language plpgsql stable security definer set search_path = public, auth as $$
begin
  perform public.admin_guard();
  return query select a.id, a.at, u.email::text, a.action, a.target, a.detail from public.admin_audit a left join auth.users u on u.id = a.actor
  order by a.at desc limit least(greatest(p_limit, 1), 1000);
end $$;

-- staff may change the status of a report (open → fixed / closed)
create or replace function public.admin_set_report(p_id bigint, p_status text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_staff() then raise exception 'staff only' using errcode = '42501'; end if;
  update public.reports set status = p_status where id = p_id;
  if public.is_admin() then perform public.admin_log('report_status', p_id::text, jsonb_build_object('status', p_status)); end if;
end $$;

do $$ declare f text; begin
  foreach f in array array['admin_overview()', 'admin_users(text, int, int)', 'admin_user(uuid)', 'admin_set_role(uuid, text)', 'admin_set_disabled(uuid, boolean)',
    'admin_set_tester(uuid, boolean)', 'admin_set_enrolment(uuid, int, boolean)', 'admin_reset_progress(uuid, text)', 'admin_attempts(text, text, int)', 'admin_void_attempt(uuid)',
    'admin_set_unit(text, boolean, text)', 'admin_overrides(text)', 'admin_save_question(text, text, boolean, boolean, jsonb, jsonb)', 'admin_reset_question(text)',
    'admin_announce(text, text, text, text)', 'admin_set_announcement(bigint, boolean)', 'admin_settings()', 'admin_set_setting(text, text)', 'admin_audit_log(int)', 'admin_set_report(bigint, text)']
  loop
    execute format('revoke all on function public.%s from public, anon', f);
    execute format('grant execute on function public.%s to authenticated', f);
  end loop;
end $$;

-- ---------- maths stage numbers: 'stage19-unit01' is stage 19, not 1 ----------
create or replace function public.record_first_pass() returns trigger
language plpgsql security definer set search_path = public as $$
declare v_l public.learners%rowtype; v_title text; v_n int; v_final boolean := new.unit like '%-final' or new.unit like '%-cp';
        v_stage int := coalesce(substring(new.unit from 'stage(\d+)')::int, 7);
begin
  select * into v_l from public.learners where id = new.learner_id;
  if new.status = 'final' and new.passed then
    if not v_final then
      insert into public.unit_results (learner_id, unit, stage, first_pass_pct, attempt_id)
      values (new.learner_id, new.unit, v_stage, new.pct, new.id)
      on conflict (learner_id, unit) do nothing;
      get diagnostics v_n = row_count;
      select title into v_title from public.stage_units where unit = new.unit;
    end if;
    insert into public.notifications (parent_id, learner_id, kind, title, body)
    values (coalesce(v_l.parent_id, v_l.user_id), v_l.id, 'test_passed',
            case when new.unit like '%-cp' then 'Checkpoint practice paper ' || new.form || ' marked'
                 when v_final then 'You passed the end-of-year exam (paper ' || new.form || ')!'
                 else 'You passed Unit ' || ltrim(right(new.unit, 2), '0') || coalesce(': ' || v_title, '') || '!' end,
            'Score ' || round(new.pct, 1) || '%');
    if not v_final and v_n > 0 and v_l.parent_email is not null then
      insert into public.email_outbox (learner_id, to_email, kind, subject, body)
      values (v_l.id, v_l.parent_email, 'unit_complete',
        v_l.nickname || ' has finished Unit ' || ltrim(right(new.unit, 2), '0') || coalesce(': ' || v_title, '') || ' on Atomic',
        'Hello,' || E'\n\n' || v_l.nickname || ' has just finished Unit ' || ltrim(right(new.unit, 2), '0') || coalesce(' (' || v_title || ')', '')
        || case when v_stage >= 10 then ' of Cambridge Lower Secondary Mathematics Stage ' || (v_stage - 10) else ' of Cambridge Lower Secondary Science Stage ' || v_stage end
        || ' on Atomic, passing the Unit Test with ' || round(new.pct, 1) || '%.'
        || E'\n\n' || 'You are receiving this because ' || v_l.nickname || ' added your email address when signing up. They can remove it at any time in their settings.'
        || E'\n\n' || 'The Atomic teaching team');
    end if;
  elsif new.status = 'final' and tg_op = 'UPDATE' and old.status = 'pending' then
    insert into public.notifications (parent_id, learner_id, kind, title, body)
    values (coalesce(v_l.parent_id, v_l.user_id), v_l.id, 'test_marked', 'Your test has been marked', 'Score ' || round(new.pct, 1) || '%');
  end if;
  return new;
end $$;
update public.unit_results set stage = 19 where unit like 'stage19-%' and stage <> 19;
