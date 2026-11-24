-- Operations: page errors from learners' browsers, so the team sees problems without an outside monitoring service.
-- Anyone may report (rate-limited, trimmed, no personal data beyond the account id); only admins can read.
create table if not exists public.client_errors (
  id bigint generated always as identity primary key,
  at timestamptz not null default now(),
  user_id uuid references auth.users(id) on delete set null,
  msg text not null,
  src text,
  line int,
  route text,
  ua text,
  release text
);
create index if not exists client_errors_at on public.client_errors (at desc);
alter table public.client_errors enable row level security;
create policy client_errors_admin_read on public.client_errors for select using (public.is_admin());

create or replace function public.log_client_error(p_msg text, p_src text default null, p_line int default null, p_route text default null, p_ua text default null, p_release text default null)
returns void language plpgsql security definer set search_path = public as $$
begin
  if p_msg is null or length(trim(p_msg)) = 0 then return; end if;
  -- at most 20 reports per account (or 200 anonymous) in 10 minutes, and 5000 a day overall
  if auth.uid() is not null and (select count(*) from client_errors where user_id = auth.uid() and at > now() - interval '10 minutes') >= 20 then return; end if;
  if auth.uid() is null and (select count(*) from client_errors where user_id is null and at > now() - interval '10 minutes') >= 200 then return; end if;
  if (select count(*) from client_errors where at > now() - interval '1 day') >= 5000 then return; end if;
  insert into client_errors (user_id, msg, src, line, route, ua, release)
  values (auth.uid(), left(p_msg, 500), left(p_src, 300), p_line, left(regexp_replace(coalesce(p_route, ''), '[?].*$', ''), 120), left(p_ua, 200), left(p_release, 40));
end $$;
revoke all on function public.log_client_error(text, text, int, text, text, text) from public;
grant execute on function public.log_client_error(text, text, int, text, text, text) to anon, authenticated;

create or replace function public.admin_client_errors(p_limit int default 200)
returns table (at timestamptz, email text, msg text, src text, line int, route text, ua text, release text)
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'admin only' using errcode = '42501'; end if;
  return query select e.at, u.email::text, e.msg, e.src, e.line, e.route, e.ua, e.release
    from client_errors e left join auth.users u on u.id = e.user_id
    order by e.at desc limit least(greatest(p_limit, 1), 1000);
end $$;
revoke all on function public.admin_client_errors(int) from public, anon;
grant execute on function public.admin_client_errors(int) to authenticated;

-- keep 90 days
create or replace function public.prune_client_errors() returns void language sql security definer set search_path = public as $$
  delete from client_errors where at < now() - interval '90 days';
$$;
revoke all on function public.prune_client_errors() from public, anon, authenticated;
