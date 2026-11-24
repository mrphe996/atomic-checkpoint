-- Cambridge Mathematics Stages 3-8 (Atomic courses; Primary 0096 for Stages 3-6, Lower Secondary 0862 for Stages 7-8).
-- Course key 10 + N = Mathematics Stage N (13 … 18), like 19 = Stage 9. This migration opens every key and adds the Stage 8 units;
-- later migrations add the units of the other Mathematics stages as they are published.

alter table public.enrolments drop constraint if exists enrolments_stage_check;
alter table public.enrolments add constraint enrolments_stage_check check (stage in (3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19));

alter table public.announcements drop constraint if exists announcements_audience_check;
alter table public.announcements add constraint announcements_audience_check check (audience in ('all', '3', '4', '5', '6', '7', '8', '9', '13', '14', '15', '16', '17', '18', '19'));

insert into public.stage_units (stage, unit, title, free_sections) values
 (18, 'stage18-unit01', 'Integers', array['1.1']),
 (18, 'stage18-unit02', 'Expressions, formulae and equations', array['2.1']),
 (18, 'stage18-unit03', 'Place value and rounding', array['3.1']),
 (18, 'stage18-unit04', 'Decimals', array['4.1']),
 (18, 'stage18-unit05', 'Angles and constructions', array['5.1']),
 (18, 'stage18-unit06', 'Collecting data', array['6.1']),
 (18, 'stage18-unit07', 'Fractions', array['7.1']),
 (18, 'stage18-unit08', 'Shapes and symmetry', array['8.1']),
 (18, 'stage18-unit09', 'Sequences and functions', array['9.1']),
 (18, 'stage18-unit10', 'Percentages', array['10.1']),
 (18, 'stage18-unit11', 'Graphs', array['11.1']),
 (18, 'stage18-unit12', 'Ratio and proportion', array['12.1']),
 (18, 'stage18-unit13', 'Probability', array['13.1']),
 (18, 'stage18-unit14', 'Position and transformation', array['14.1']),
 (18, 'stage18-unit15', 'Distance, area and volume', array['15.1']),
 (18, 'stage18-unit16', 'Interpreting and discussing results', array['16.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

create or replace function public.enrol_stage(p_learner uuid, p_stage int, p_amount text default null)
returns text language plpgsql security definer set search_path = public as $$
begin
  if not public.owns_learner(p_learner) then raise exception 'not your learner' using errcode = '42501'; end if;
  if p_stage not in (3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19) then raise exception 'bad stage' using errcode = '22023'; end if;
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
  if p_stage not in (3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19) then raise exception 'bad stage' using errcode = '22023'; end if;
  if p_on then insert into public.enrolments (learner_id, stage, method, amount) values (p_learner, p_stage, 'admin', null) on conflict (learner_id, stage) do update set status = 'active';
  else delete from public.enrolments where learner_id = p_learner and stage = p_stage; end if;
  perform public.admin_log(case when p_on then 'enrol' else 'unenrol' end, p_learner::text, jsonb_build_object('stage', p_stage));
end $$;

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
        || case when v_stage >= 10 then ' of Cambridge ' || case when v_stage <= 16 then 'Primary' else 'Lower Secondary' end || ' Mathematics Stage ' || (v_stage - 10) else ' of Cambridge ' || case when v_stage <= 6 then 'Primary' else 'Lower Secondary' end || ' Science Stage ' || v_stage end
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

-- testers get Mathematics Stage 8 too
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, 18, 'test', 'tester' from public.testers t
on conflict (learner_id, stage) do nothing;
