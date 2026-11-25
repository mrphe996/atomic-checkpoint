-- B2C plans: one stage per learner.
-- learners.stage is the learner's stage level (1–9). They study only the courses they bought for that level:
-- Science (enrolments.stage = N), Mathematics (10 + N) and ESL (20 + N), one by one or as the whole-stage bundle.
-- Another level opens only when 80 % of the Unit Tests of the courses at the current level are passed.
-- Certificates need 80 % of a course's Unit Tests (the app also asks for 80 % of the lessons); the end-of-year exam is optional.

-- 1. learners who signed up before this change keep the Science course of their stage
insert into public.enrolments (learner_id, stage, method, amount)
select l.id, coalesce(l.stage, 7), 'legacy', null from public.learners l
where not exists (select 1 from public.enrolments e where e.learner_id = l.id)
on conflict (learner_id, stage) do nothing;

-- 2. % of the Unit Tests passed in the learner's courses at one level
create or replace function public.level_tests_pct(p_learner uuid, p_level int)
returns numeric language sql stable security definer set search_path = public as $$
  with keys as (select stage from public.enrolments where learner_id = p_learner and status <> 'canceled' and stage % 10 = p_level),
       need as (select count(*) n from public.stage_units u join keys k on k.stage = u.stage),
       have as (select count(*) n from public.unit_results r join public.stage_units u on u.unit = r.unit join keys k on k.stage = u.stage where r.learner_id = p_learner)
  select case when (select n from need) = 0 then 0 else round(100.0 * (select n from have) / (select n from need), 1) end
$$;
revoke all on function public.level_tests_pct(uuid, int) from public, anon;
grant execute on function public.level_tests_pct(uuid, int) to authenticated;

-- 3. buying a course: same level always; another level only after 80 % of the current level's Unit Tests
create or replace function public.enrol_stage(p_learner uuid, p_stage int, p_amount text default null)
returns text language plpgsql security definer set search_path = public as $$
declare v_level int := p_stage % 10; v_cur int; v_has boolean;
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  if p_stage not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29) then raise exception 'bad stage' using errcode = '22023'; end if;
  if coalesce((select value from private.app_secrets where name = 'mock_payments'), 'off') <> 'on' then
    raise exception 'payments are not open yet' using errcode = 'P0001';
  end if;
  select coalesce(stage, 7) into v_cur from public.learners where id = p_learner;
  select exists (select 1 from public.enrolments where learner_id = p_learner and status <> 'canceled') into v_has;
  if v_has and v_level <> v_cur and public.level_tests_pct(p_learner, v_cur) < 80
     and not exists (select 1 from public.testers where learner_id = p_learner) then   -- testers (staff) may open any stage
    raise exception 'stage locked: finish 80%% of Stage % first', v_cur using errcode = 'P0001';
  end if;
  if not v_has or v_level <> v_cur then update public.learners set stage = v_level where id = p_learner; end if;
  insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'test', p_amount)
  on conflict (learner_id, stage) do update set status = 'active';
  insert into public.notifications (parent_id, learner_id, kind, title, body)
  select coalesce(l.parent_id, l.user_id), l.id, 'billing',
         'You are enrolled in Stage ' || (p_stage % 10) || case when p_stage >= 20 then ' English (ESL)' when p_stage >= 10 then ' Mathematics' else ' Science' end,
         'Test checkout – no money was taken.'
  from public.learners l where l.id = p_learner;
  return 'ok';
end $$;
revoke all on function public.enrol_stage(uuid, int, text) from public, anon;
grant execute on function public.enrol_stage(uuid, int, text) to authenticated;

-- 4. certificates at 80 % of a course's Unit Tests
create or replace function public.issue_certificate(p_learner uuid, p_stage int default 7)
returns text language plpgsql security definer set search_path = public as $$
declare v_code text; v_need int; v_have int; v_name text;
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  select code into v_code from public.certificates where learner_id = p_learner and stage = p_stage;
  if v_code is not null then return v_code; end if;
  select count(*) into v_need from public.stage_units where stage = p_stage;
  select count(*) into v_have from public.unit_results r join public.stage_units u on u.unit = r.unit and u.stage = p_stage where r.learner_id = p_learner;
  if v_need = 0 or v_have < ceil(v_need * 0.8) then raise exception 'stage not complete (% of % units passed, 80%% needed)', v_have, v_need using errcode = 'P0001'; end if;
  select coalesce(certificate_name, nickname) into v_name from public.learners where id = p_learner;
  v_code := (case when p_stage >= 20 then 'AE-E' || (p_stage - 20) when p_stage >= 10 then 'AE-M' || (p_stage - 10) else 'AE-S' || p_stage end) || '-' || to_char(now(), 'YYYY') || '-' || upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 8));
  insert into public.certificates (learner_id, stage, code, name_on_certificate) values (p_learner, p_stage, v_code, v_name)
  on conflict (learner_id, stage) do nothing;
  select code into v_code from public.certificates where learner_id = p_learner and stage = p_stage;
  return v_code;
end $$;
revoke all on function public.issue_certificate(uuid, int) from public, anon;
grant execute on function public.issue_certificate(uuid, int) to authenticated;
