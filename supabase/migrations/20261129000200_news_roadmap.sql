-- News page: public announcements + a roadmap of features that are coming (or just released), edited by admins.
-- Also: announcements may target any course key, and admins can move a learner to another stage level.

-- 1. announcements for any course (the old check only allowed 7, 8, 9 and 19)
alter table public.announcements drop constraint if exists announcements_audience_check;
alter table public.announcements add constraint announcements_audience_check
  check (audience = 'all' or audience ~ '^(1|2|3|4|5|6|7|8|9|11|12|13|14|15|16|17|18|19|22|23|24|25|26|27|28|29)$');
-- news shows the date the announcement was published; the public page lists the active ones

-- 2. roadmap
create table if not exists public.roadmap (
  id bigint generated always as identity primary key,
  title text not null check (char_length(title) between 2 and 120),
  body text not null default '' check (char_length(body) <= 1000),
  status text not null default 'planned' check (status in ('planned', 'building', 'released')),
  target text not null default '' check (char_length(target) <= 40),      -- e.g. 'December 2026', 'Early 2027'
  tag text not null default '' check (char_length(tag) <= 40),            -- e.g. 'Mathematics', 'Account', 'App'
  sort int not null default 0,
  published boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
alter table public.roadmap enable row level security;
drop policy if exists roadmap_read on public.roadmap;
create policy roadmap_read on public.roadmap for select using (published);
drop policy if exists roadmap_admin_read on public.roadmap;
create policy roadmap_admin_read on public.roadmap for select to authenticated using (public.is_admin());   -- drafts: admins only (anon cannot call is_admin)
grant select on public.roadmap to anon, authenticated;
grant all on public.roadmap to service_role;

create or replace function public.admin_roadmap_save(p_id bigint, p_title text, p_body text, p_status text, p_target text, p_tag text, p_sort int, p_published boolean)
returns bigint language plpgsql security definer set search_path = public as $$
declare v bigint := p_id;
begin
  perform public.admin_guard();
  if v is null then
    insert into public.roadmap (title, body, status, target, tag, sort, published)
    values (p_title, coalesce(p_body, ''), coalesce(p_status, 'planned'), coalesce(p_target, ''), coalesce(p_tag, ''), coalesce(p_sort, 0), coalesce(p_published, true)) returning id into v;
  else
    update public.roadmap set title = p_title, body = coalesce(p_body, ''), status = coalesce(p_status, 'planned'), target = coalesce(p_target, ''), tag = coalesce(p_tag, ''),
      sort = coalesce(p_sort, 0), published = coalesce(p_published, true), updated_at = now() where id = v;
  end if;
  perform public.admin_log('roadmap_save', v::text, jsonb_build_object('title', p_title, 'status', p_status));
  return v;
end $$;

create or replace function public.admin_roadmap_delete(p_id bigint) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  delete from public.roadmap where id = p_id;
  perform public.admin_log('roadmap_delete', p_id::text, '{}'::jsonb);
end $$;

-- 3. admins can move a learner to another stage level (one stage per learner)
create or replace function public.admin_set_learner_stage(p_learner uuid, p_stage int) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public.admin_guard();
  if p_stage not between 1 and 9 then raise exception 'bad stage' using errcode = '22023'; end if;
  update public.learners set stage = p_stage where id = p_learner;
  perform public.admin_log('learner_stage', p_learner::text, jsonb_build_object('stage', p_stage));
end $$;

do $$ declare f text; begin
  foreach f in array array['admin_roadmap_save(bigint, text, text, text, text, text, int, boolean)', 'admin_roadmap_delete(bigint)', 'admin_set_learner_stage(uuid, int)']
  loop
    execute format('revoke all on function public.%s from public, anon', f);
    execute format('grant execute on function public.%s to authenticated', f);
  end loop;
end $$;

-- 4. first roadmap (admins edit it in Admin → Announcements & roadmap)
insert into public.roadmap (title, body, status, target, tag, sort) values
 ('One stage per learner, with subject plans', 'Choose your stage when you sign up, then one subject or the whole stage. The next stage opens when 80% of your lessons and Unit Tests are done.', 'released', 'November 2026', 'Account', 10),
 ('Primary Mathematics: deeper lessons', 'Every Stage 3–6 lesson now explains why each method works, with a worked example, a method box and reasoning questions.', 'released', 'November 2026', 'Mathematics', 20),
 ('Science reasoning questions', 'Predict, spot the mistake, plan a fair test and “always, sometimes or never” questions in every Science lesson, Stages 3–9.', 'released', 'November 2026', 'Science', 30),
 ('English (ESL) Stages 2–9', 'Narrated lessons with reading, listening and writing practice for every unit.', 'released', 'November 2026', 'English', 40),
 ('Online payment', 'Pay for a subject or a whole stage by card and other local methods.', 'building', 'December 2026', 'Account', 50),
 ('Sign in with Google and Apple', 'Log in with one tap, without a new password.', 'planned', 'December 2026', 'Account', 60),
 ('Weekly report for parents', 'A short email each week: time spent, lessons finished and Unit Test results.', 'planned', 'January 2027', 'Parents', 70),
 ('Install Atomic on your phone', 'Add Atomic to your home screen and keep studying when the internet is slow.', 'planned', 'Early 2027', 'App', 80),
 ('Practice that adapts to you', 'Extra questions chosen from the objectives you find hardest, with spaced review.', 'planned', 'Early 2027', 'Learning', 90),
 ('Cambridge IGCSE Science', 'The next level after Lower Secondary, starting with Biology.', 'planned', '2027', 'Science', 100);
