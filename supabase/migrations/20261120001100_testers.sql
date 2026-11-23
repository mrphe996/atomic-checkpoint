-- Tester accounts (test environment): skip the learning-order, level and review locks so staff can check every page.
-- Only the service role (staff tools / SQL) can add a tester; a learner can only read their own flag.
create table if not exists public.testers (
  learner_id uuid primary key references public.learners (id) on delete cascade,
  note text,
  created_at timestamptz not null default now()
);
alter table public.testers enable row level security;
create policy testers_read on public.testers for select using (public.owns_learner(learner_id));
grant select on public.testers to authenticated;
grant all on public.testers to service_role;
