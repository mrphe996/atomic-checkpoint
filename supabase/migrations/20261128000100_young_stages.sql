-- Cambridge Primary Stages 1 and 2 (Atomic picture courses for ages 5–7): Science course keys 1, 2; Mathematics course keys 11, 12.
alter table public.enrolments drop constraint if exists enrolments_stage_check;
alter table public.enrolments add constraint enrolments_stage_check check (stage in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19));

create or replace function public.enrol_stage(p_learner uuid, p_stage int, p_amount text default null)
returns text language plpgsql security definer set search_path = public as $$
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  if p_stage not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19) then raise exception 'bad stage' using errcode = '22023'; end if;
  if coalesce((select value from private.app_secrets where name = 'mock_payments'), 'off') <> 'on' then
    raise exception 'payments are not open yet' using errcode = 'P0001';
  end if;
  insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'test', p_amount)
  on conflict (learner_id, stage) do nothing;
  insert into public.notifications (parent_id, learner_id, kind, title, body)
  select coalesce(l.parent_id, l.user_id), l.id, 'billing',
         case when p_stage >= 10 then 'You are enrolled in Stage ' || (p_stage - 10) || ' Mathematics'
              when p_stage <= 6 then 'You are enrolled in Stage ' || p_stage || ' Science (Primary)' else 'You are enrolled in Stage ' || p_stage end,
         'Test checkout – no money was taken.'
  from public.learners l where l.id = p_learner;
  return 'ok';
end $$;
revoke all on function public.enrol_stage(uuid, int, text) from public, anon;
grant execute on function public.enrol_stage(uuid, int, text) to authenticated;

create or replace function public.admin_set_enrolment(p_learner uuid, p_stage int, p_on boolean) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  if p_stage not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19) then raise exception 'bad stage' using errcode = '22023'; end if;
  if p_on then insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'admin', null) on conflict (learner_id, stage) do update set status = 'active';
  else delete from public.enrolments where learner_id = p_learner and stage = p_stage; end if;
  perform public.admin_log(case when p_on then 'enrol' else 'unenrol' end, p_learner::text, jsonb_build_object('stage', p_stage));
end $$;

insert into public.stage_units (stage, unit, title, free_sections) values
 (1, 'stage1-unit01', 'Living Things', array['1.1']),
 (1, 'stage1-unit02', 'Ourselves', array['2.1']),
 (1, 'stage1-unit03', 'Materials', array['3.1']),
 (1, 'stage1-unit04', 'Pushes and Pulls', array['4.1']),
 (1, 'stage1-unit05', 'Sound', array['5.1']),
 (1, 'stage1-unit06', 'Earth and Sky', array['6.1']),
 (2, 'stage2-unit01', 'Living Things and Habitats', array['1.1']),
 (2, 'stage2-unit02', 'Growing Up and Staying Healthy', array['2.1']),
 (2, 'stage2-unit03', 'Using Materials', array['3.1']),
 (2, 'stage2-unit04', 'Light and Dark', array['4.1']),
 (2, 'stage2-unit05', 'Electricity', array['5.1']),
 (2, 'stage2-unit06', 'Rocks, Soil and Weather', array['6.1']),
 (11, 'stage11-unit01', 'Numbers to 10', array['1.1']),
 (11, 'stage11-unit02', 'Numbers to 20', array['2.1']),
 (11, 'stage11-unit03', 'Addition', array['3.1']),
 (11, 'stage11-unit04', 'Subtraction', array['4.1']),
 (11, 'stage11-unit05', 'Shapes', array['5.1']),
 (11, 'stage11-unit06', 'Measures', array['6.1']),
 (11, 'stage11-unit07', 'Time', array['7.1']),
 (11, 'stage11-unit08', 'Halves, Patterns and Data', array['8.1']),
 (12, 'stage12-unit01', 'Numbers to 100', array['1.1']),
 (12, 'stage12-unit02', 'Addition and Subtraction', array['2.1']),
 (12, 'stage12-unit03', 'Multiplication and Division', array['3.1']),
 (12, 'stage12-unit04', 'Fractions', array['4.1']),
 (12, 'stage12-unit05', 'Shapes and Symmetry', array['5.1']),
 (12, 'stage12-unit06', 'Measures', array['6.1']),
 (12, 'stage12-unit07', 'Time', array['7.1']),
 (12, 'stage12-unit08', 'Data', array['8.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

-- testers get the four new courses too
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, s.stage, 'test', 'tester' from public.testers t cross join (values (1), (2), (11), (12)) s(stage)
on conflict (learner_id, stage) do nothing;
