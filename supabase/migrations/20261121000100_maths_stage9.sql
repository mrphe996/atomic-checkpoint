-- Cambridge Stage 9 Mathematics (Atomic course, aligned to the 0862 framework).
-- Course key 19 = Mathematics Stage 9: units stage19-unit01 … stage19-unit15, stage19-final, stage19-cp.
-- Enrolled like a stage (enrolments.stage = 19); learners.stage (the Science stage chosen at sign-up) is unchanged.

alter table public.enrolments drop constraint if exists enrolments_stage_check;
alter table public.enrolments add constraint enrolments_stage_check check (stage in (7, 8, 9, 19));

insert into public.stage_units (stage, unit, title, free_sections) values
 (19, 'stage19-unit01', 'Number and calculation', array['1.1']),
 (19, 'stage19-unit02', 'Expressions and formulae', array['2.1']),
 (19, 'stage19-unit03', 'Decimals, percentages and rounding', array['3.1']),
 (19, 'stage19-unit04', 'Equations and inequalities', array['4.1']),
 (19, 'stage19-unit05', 'Angles', array['5.1']),
 (19, 'stage19-unit06', 'Statistical investigations', array['6.1']),
 (19, 'stage19-unit07', 'Shapes and measurements', array['7.1']),
 (19, 'stage19-unit08', 'Fractions', array['8.1']),
 (19, 'stage19-unit09', 'Sequences and functions', array['9.1']),
 (19, 'stage19-unit10', 'Graphs', array['10.1']),
 (19, 'stage19-unit11', 'Ratio and proportion', array['11.1']),
 (19, 'stage19-unit12', 'Probability', array['12.1']),
 (19, 'stage19-unit13', 'Position and transformation', array['13.1']),
 (19, 'stage19-unit14', 'Volume, surface area and symmetry', array['14.1']),
 (19, 'stage19-unit15', 'Interpreting and discussing results', array['15.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

create or replace function public.enrol_stage(p_learner uuid, p_stage int, p_amount text default null)
returns text language plpgsql security definer set search_path = public as $$
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  if p_stage not in (7, 8, 9, 19) then raise exception 'bad stage' using errcode = '22023'; end if;
  if coalesce((select value from private.app_secrets where name = 'mock_payments'), 'off') <> 'on' then
    raise exception 'payments are not open yet' using errcode = 'P0001';
  end if;
  insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'test', p_amount)
  on conflict (learner_id, stage) do nothing;
  insert into public.notifications (parent_id, learner_id, kind, title, body)
  select coalesce(l.parent_id, l.user_id), l.id, 'billing',
         case when p_stage = 19 then 'You are enrolled in Stage 9 Mathematics' else 'You are enrolled in Stage ' || p_stage end,
         'Test checkout – no money was taken.'
  from public.learners l where l.id = p_learner;
  return 'ok';
end $$;
revoke all on function public.enrol_stage(uuid, int, text) from public, anon;
grant execute on function public.enrol_stage(uuid, int, text) to authenticated;

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
  v_code := (case when p_stage >= 10 then 'AE-M' || (p_stage - 10) else 'AE-S' || p_stage end) || '-' || to_char(now(), 'YYYY') || '-' || upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 8));
  insert into public.certificates (learner_id, stage, code, name_on_certificate) values (p_learner, p_stage, v_code, v_name)
  on conflict (learner_id, stage) do nothing;
  select code into v_code from public.certificates where learner_id = p_learner and stage = p_stage;
  return v_code;
end $$;
revoke all on function public.issue_certificate(uuid, int) from public, anon;
grant execute on function public.issue_certificate(uuid, int) to authenticated;

-- testers get every course, including Mathematics
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, 19, 'test', 'tester' from public.testers t
on conflict (learner_id, stage) do nothing;
