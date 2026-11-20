-- Table privileges for the Data API. New Supabase projects no longer grant these by default;
-- row level security (20261120000200_rls.sql) still decides WHICH rows each role can touch.
grant usage on schema public to anon, authenticated, service_role;
grant select, update on public.profiles to authenticated;
grant select, insert on public.consents to authenticated;
grant select, insert, update, delete on public.learners to authenticated;
grant select on public.stage_units to anon, authenticated;
grant select, insert, update, delete on public.progress to authenticated;
grant select on public.attempts, public.unit_results, public.certificates, public.subscriptions to authenticated;
grant select, insert, update on public.reports to authenticated;
grant select, update on public.notifications to authenticated;
grant select, insert on public.events to authenticated;
grant usage, select on all sequences in schema public to authenticated;
grant all on all tables in schema public to service_role;
grant usage, select on all sequences in schema public to service_role;
