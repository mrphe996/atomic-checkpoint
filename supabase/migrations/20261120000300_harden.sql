-- Least privilege for functions: Postgres grants EXECUTE to PUBLIC by default.
revoke execute on function public.is_staff(), public.owns_learner(uuid), public.handle_new_user(), public.record_first_pass(),
  public.has_subscription(uuid), public.leaderboard(int), public.issue_certificate(uuid, int), public.item_stats(text),
  public.verify_certificate(text) from public, anon, authenticated;
-- called by signed-in parents / staff from the browser
grant execute on function public.leaderboard(int), public.issue_certificate(uuid, int), public.item_stats(text) to authenticated;
-- helpers used inside RLS policies must stay callable by the roles the policies run as
grant execute on function public.is_staff(), public.owns_learner(uuid) to authenticated;
-- public certificate check
grant execute on function public.verify_certificate(text) to anon, authenticated;
-- has_subscription is only called by the server (service role)
grant execute on function public.has_subscription(uuid) to service_role;
