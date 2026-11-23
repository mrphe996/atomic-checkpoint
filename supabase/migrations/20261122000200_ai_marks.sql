-- AI marking of paragraph answers: one row per AI mark, used for the per-user daily limit (api/ai-mark.js).
create table if not exists public.ai_marks (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users (id) on delete cascade,
  unit text not null,
  qid text not null,
  at timestamptz not null default now()
);
create index if not exists ai_marks_user_at on public.ai_marks (user_id, at desc);
alter table public.ai_marks enable row level security;   -- no policies: only the service role (Edge Function) reads and writes
revoke all on public.ai_marks from anon, authenticated;
