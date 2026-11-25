-- Atomic English as a Second Language, Stages 2–9: course keys 22–29.
alter table public.enrolments drop constraint if exists enrolments_stage_check;
alter table public.enrolments add constraint enrolments_stage_check check (stage in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29));

create or replace function public.enrol_stage(p_learner uuid, p_stage int, p_amount text default null)
returns text language plpgsql security definer set search_path = public as $$
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  if p_stage not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29) then raise exception 'bad stage' using errcode = '22023'; end if;
  if coalesce((select value from private.app_secrets where name = 'mock_payments'), 'off') <> 'on' then
    raise exception 'payments are not open yet' using errcode = 'P0001';
  end if;
  insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'test', p_amount)
  on conflict (learner_id, stage) do nothing;
  insert into public.notifications (parent_id, learner_id, kind, title, body)
  select coalesce(l.parent_id, l.user_id), l.id, 'billing',
         case when p_stage >= 20 then 'You are enrolled in Stage ' || (p_stage - 20) || ' English (ESL)' when p_stage >= 10 then 'You are enrolled in Stage ' || (p_stage - 10) || ' Mathematics'
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
  if p_stage not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29) then raise exception 'bad stage' using errcode = '22023'; end if;
  if p_on then insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'admin', null) on conflict (learner_id, stage) do update set status = 'active';
  else delete from public.enrolments where learner_id = p_learner and stage = p_stage; end if;
  perform public.admin_log(case when p_on then 'enrol' else 'unenrol' end, p_learner::text, jsonb_build_object('stage', p_stage));
end $$;

insert into public.stage_units (stage, unit, title, free_sections) values
 (22, 'stage22-unit01', 'My Family and Home', array['1.1']),
 (22, 'stage22-unit02', 'At School', array['2.1']),
 (22, 'stage22-unit03', 'Animals We Love', array['3.1']),
 (22, 'stage22-unit04', 'Food and Shopping', array['4.1']),
 (22, 'stage22-unit05', 'Weather and Clothes', array['5.1']),
 (22, 'stage22-unit06', 'Fun and Games', array['6.1']),
 (23, 'stage23-unit01', 'Friends and Feelings', array['1.1']),
 (23, 'stage23-unit02', 'Our Town', array['2.1']),
 (23, 'stage23-unit03', 'Amazing Animals', array['3.1']),
 (23, 'stage23-unit04', 'Stories from Long Ago', array['4.1']),
 (23, 'stage23-unit05', 'Poems and Sounds', array['5.1']),
 (23, 'stage23-unit06', 'Healthy Living', array['6.1']),
 (24, 'stage24-unit01', 'Stories and Characters', array['1.1']),
 (24, 'stage24-unit02', 'Our Amazing Planet', array['2.1']),
 (24, 'stage24-unit03', 'Poems with Pictures', array['3.1']),
 (24, 'stage24-unit04', 'News Reporters', array['4.1']),
 (24, 'stage24-unit05', 'On Stage', array['5.1']),
 (24, 'stage24-unit06', 'Food Around the World', array['6.1']),
 (25, 'stage25-unit01', 'Mystery Stories', array['1.1']),
 (25, 'stage25-unit02', 'Amazing Inventions', array['2.1']),
 (25, 'stage25-unit03', 'Poems from Many Places', array['3.1']),
 (25, 'stage25-unit04', 'Persuade Me!', array['4.1']),
 (25, 'stage25-unit05', 'Myths and Legends', array['5.1']),
 (25, 'stage25-unit06', 'Space Explorers', array['6.1']),
 (26, 'stage26-unit01', 'Adventure Fiction', array['1.1']),
 (26, 'stage26-unit02', 'Lives that Inspire', array['2.1']),
 (26, 'stage26-unit03', 'Images in Poetry', array['3.1']),
 (26, 'stage26-unit04', 'Our Planet, Our Choice', array['4.1']),
 (26, 'stage26-unit05', 'Behind the Headlines', array['5.1']),
 (26, 'stage26-unit06', 'Science Fiction', array['6.1']),
 (27, 'stage27-unit01', 'Journeys', array['1.1']),
 (27, 'stage27-unit02', 'Explaining the World', array['2.1']),
 (27, 'stage27-unit03', 'Figurative Language', array['3.1']),
 (27, 'stage27-unit04', 'Campaigns', array['4.1']),
 (27, 'stage27-unit05', 'Drama and Dialogue', array['5.1']),
 (27, 'stage27-unit06', 'Media and Advertising', array['6.1']),
 (28, 'stage28-unit01', 'Suspense and Tension', array['1.1']),
 (28, 'stage28-unit02', 'Travel Writing', array['2.1']),
 (28, 'stage28-unit03', 'Poems of Place and Memory', array['3.1']),
 (28, 'stage28-unit04', 'Debate and Discursive Writing', array['4.1']),
 (28, 'stage28-unit05', 'Classic Tales Retold', array['5.1']),
 (28, 'stage28-unit06', 'The Digital World', array['6.1']),
 (29, 'stage29-unit01', 'Narrative Voice', array['1.1']),
 (29, 'stage29-unit02', 'Ideas that Changed the World', array['2.1']),
 (29, 'stage29-unit03', 'Analysing Poetry', array['3.1']),
 (29, 'stage29-unit04', 'Speeches that Matter', array['4.1']),
 (29, 'stage29-unit05', 'Investigative Reports', array['5.1']),
 (29, 'stage29-unit06', 'Future Worlds', array['6.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

-- testers get the ESL courses too
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, s.stage, 'test', 'tester' from public.testers t cross join (values (22), (23), (24), (25), (26), (27), (28), (29)) s(stage)
on conflict (learner_id, stage) do nothing;
