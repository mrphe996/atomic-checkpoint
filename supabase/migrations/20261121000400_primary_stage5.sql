-- Cambridge Primary Science Stage 5 (Atomic course, aligned to the 0097 framework). Course key 5 = units stage5-unit01 … stage5-unit06.
alter table public.enrolments drop constraint if exists enrolments_stage_check;
alter table public.enrolments add constraint enrolments_stage_check check (stage in (5, 6, 7, 8, 9, 19));

insert into public.stage_units (stage, unit, title, free_sections) values
 (5, 'stage5-unit01', 'Life cycles of flowering plants', array['1.1']),
 (5, 'stage5-unit02', 'Sound', array['2.1']),
 (5, 'stage5-unit03', 'States and properties of matter', array['3.1']),
 (5, 'stage5-unit04', 'The digestive system', array['4.1']),
 (5, 'stage5-unit05', 'Forces and magnetism', array['5.1']),
 (5, 'stage5-unit06', 'Seasons and adaptations', array['6.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

create or replace function public.enrol_stage(p_learner uuid, p_stage int, p_amount text default null)
returns text language plpgsql security definer set search_path = public as $$
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  if p_stage not in (5, 6, 7, 8, 9, 19) then raise exception 'bad stage' using errcode = '22023'; end if;
  if coalesce((select value from private.app_secrets where name = 'mock_payments'), 'off') <> 'on' then
    raise exception 'payments are not open yet' using errcode = 'P0001';
  end if;
  insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'test', p_amount)
  on conflict (learner_id, stage) do nothing;
  insert into public.notifications (parent_id, learner_id, kind, title, body)
  select coalesce(l.parent_id, l.user_id), l.id, 'billing',
         case when p_stage = 19 then 'You are enrolled in Stage 9 Mathematics' when p_stage in (5, 6) then 'You are enrolled in Stage ' || p_stage || ' Science (Primary)' else 'You are enrolled in Stage ' || p_stage end,
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
  if p_stage not in (5, 6, 7, 8, 9, 19) then raise exception 'bad stage' using errcode = '22023'; end if;
  if p_on then insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'admin', null) on conflict (learner_id, stage) do update set status = 'active';
  else delete from public.enrolments where learner_id = p_learner and stage = p_stage; end if;
  perform public.admin_log(case when p_on then 'enrol' else 'unenrol' end, p_learner::text, jsonb_build_object('stage', p_stage));
end $$;

-- testers get the new Primary course too
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, 5, 'test', 'tester' from public.testers t
on conflict (learner_id, stage) do nothing;
