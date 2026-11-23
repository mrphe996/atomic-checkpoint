-- Server-only secrets (e.g. the key that unseals the test answer keys). Never readable by anon/authenticated.
create schema if not exists private;
create table if not exists private.app_secrets (name text primary key, value text not null, updated_at timestamptz not null default now());
revoke all on schema private from public, anon, authenticated;
revoke all on private.app_secrets from public, anon, authenticated;
create or replace function public.get_app_secret(p_name text) returns text
  language sql stable security definer set search_path = '' as $$ select value from private.app_secrets where name = p_name $$;
revoke all on function public.get_app_secret(text) from public, anon, authenticated;
grant execute on function public.get_app_secret(text) to service_role;
