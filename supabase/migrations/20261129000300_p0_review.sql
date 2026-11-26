-- P0 review 26/11/2026: level_tests_pct is only used inside enrol_stage (security definer); signed-in users must not read other learners' progress through it.
revoke execute on function public.level_tests_pct(uuid, int) from authenticated;
-- Guests could not read announcements: the read policy called is_admin(), which anon may not execute. Split it like the roadmap policies.
alter policy announcements_read on public.announcements using (active);
drop policy if exists announcements_admin_read on public.announcements;
create policy announcements_admin_read on public.announcements for select to authenticated using (public.is_admin());
