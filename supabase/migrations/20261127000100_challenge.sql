-- Maths Challenge (problem-solving competitions): question-by-question practice answers.
-- Written only by the API (service role). A paper with practice answers can no longer be sat as a timed paper.
create table if not exists public.challenge_practice (
  learner_id uuid not null references public.learners(id) on delete cascade,
  unit text not null check (unit ~ '^ch-[a-z]+$'),
  form text not null check (length(form) <= 8),
  qid text not null check (length(qid) <= 32),
  ok boolean not null,
  answer jsonb,
  created_at timestamptz not null default now(),
  primary key (learner_id, unit, qid)
);
create index if not exists challenge_practice_form on public.challenge_practice (learner_id, unit, form);
alter table public.challenge_practice enable row level security;
create policy challenge_practice_read on public.challenge_practice for select using (public.owns_learner(learner_id));
grant select on public.challenge_practice to authenticated;
grant all on public.challenge_practice to service_role;

-- Challenge papers are not units: no unit result, their own notification
create or replace function public.record_first_pass() returns trigger
language plpgsql security definer set search_path = public as $$
declare v_l public.learners%rowtype; v_title text; v_n int; v_final boolean := new.unit like '%-final' or new.unit like '%-cp' or new.unit like 'ch-%';
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
                 when new.unit like 'ch-%' then 'Maths Challenge paper ' || new.form || ' marked'
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
