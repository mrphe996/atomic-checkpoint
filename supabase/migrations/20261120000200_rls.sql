-- Row level security: every table is closed by default; parents see only their own family's rows.
alter table public.profiles enable row level security;
alter table public.consents enable row level security;
alter table public.learners enable row level security;
alter table public.stage_units enable row level security;
alter table public.progress enable row level security;
alter table public.attempts enable row level security;
alter table public.unit_results enable row level security;
alter table public.certificates enable row level security;
alter table public.subscriptions enable row level security;
alter table public.reports enable row level security;
alter table public.notifications enable row level security;
alter table public.events enable row level security;

-- profiles: own row; staff read all. Role can never be changed by the user.
create policy profiles_self_select on public.profiles for select using (id = auth.uid() or public.is_staff());
create policy profiles_self_update on public.profiles for update using (id = auth.uid())
  with check (id = auth.uid() and role = (select role from public.profiles p where p.id = auth.uid()));

create policy consents_own on public.consents for select using (parent_id = auth.uid());
create policy consents_insert on public.consents for insert with check (parent_id = auth.uid() and (learner_id is null or public.owns_learner(learner_id)));

create policy learners_own on public.learners for all using (parent_id = auth.uid()) with check (parent_id = auth.uid());
create policy learners_staff on public.learners for select using (public.is_staff());

create policy stage_units_read on public.stage_units for select using (true);

create policy progress_own on public.progress for all using (public.owns_learner(learner_id)) with check (public.owns_learner(learner_id));

-- attempts are written only by the server (api/submit-test, api/mark-attempt) with the service role
create policy attempts_read on public.attempts for select using (public.owns_learner(learner_id) or public.is_staff());

create policy results_read on public.unit_results for select using (public.owns_learner(learner_id));
create policy certs_read on public.certificates for select using (public.owns_learner(learner_id));
create policy subs_read on public.subscriptions for select using (parent_id = auth.uid());

create policy reports_insert on public.reports for insert with check (reporter_id = auth.uid() and (learner_id is null or public.owns_learner(learner_id)));
create policy reports_read on public.reports for select using (reporter_id = auth.uid() or public.is_staff());
create policy reports_staff_update on public.reports for update using (public.is_staff());

create policy notif_own on public.notifications for select using (parent_id = auth.uid());
create policy notif_mark_read on public.notifications for update using (parent_id = auth.uid()) with check (parent_id = auth.uid());

-- optional (non-essential) analytics only when the parent opted in
create policy events_insert on public.events for insert with check (
  (learner_id is null or public.owns_learner(learner_id)) and (parent_id is null or parent_id = auth.uid())
  and (essential or exists (select 1 from public.profiles where id = auth.uid() and product_analytics)));
create policy events_staff_read on public.events for select using (public.is_staff());

grant execute on function public.leaderboard(int), public.issue_certificate(uuid, int), public.has_subscription(uuid), public.item_stats(text) to authenticated;
grant execute on function public.verify_certificate(text) to anon, authenticated;
