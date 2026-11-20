// Parent data rights (UK GDPR, Singapore PDPA, Vietnam PDPL):
// GET  /api/account?export=1        → every row about this family as one JSON download
// POST /api/account { confirm: "DELETE MY ACCOUNT" } → deletes the auth user; foreign keys cascade to all family data.
//      An active Paddle subscription is cancelled first (if PADDLE_API_KEY is set).
import { send, readJson, getUser, db, env } from './_lib/supa.js';

const TABLES = [['profiles', 'id'], ['consents', 'parent_id'], ['learners', 'parent_id'], ['subscriptions', 'parent_id'], ['reports', 'reporter_id'], ['notifications', 'parent_id']];
const BY_LEARNER = ['progress', 'attempts', 'unit_results', 'certificates', 'events'];

export async function handle(req, f = fetch) {
  const user = await getUser(req, f); if (!user) return [401, { error: 'sign_in' }];
  if (req.method === 'GET') {
    const out = { exported_at: new Date().toISOString(), account: { id: user.id, email: user.email } };
    for (const [t, col] of TABLES) out[t] = await db(`${t}?${col}=eq.${user.id}`, {}, f);
    if (!out.learners.length) out.learners = await db(`learners?user_id=eq.${user.id}`, {}, f); // a student's own profile
    const ids = out.learners.map(l => l.id);
    for (const t of BY_LEARNER) out[t] = ids.length ? await db(`${t}?learner_id=in.(${ids.join(',')})`, {}, f) : [];
    return [200, out, { 'Content-Disposition': 'attachment; filename="atomic-data-export.json"' }];
  }
  if (req.method !== 'POST') return [405, { error: 'method' }];
  const { confirm } = await readJson(req);
  if (confirm !== 'DELETE MY ACCOUNT') return [400, { error: 'confirm' }];
  const subs = await db(`subscriptions?parent_id=eq.${user.id}&status=in.(trialing,active,past_due)`, {}, f);
  if (subs.length && env('PADDLE_API_KEY')) {
    for (const s of subs) await f(`${env('PADDLE_API_URL', 'https://api.paddle.com')}/subscriptions/${s.provider_subscription_id}/cancel`, {
      method: 'POST', headers: { Authorization: `Bearer ${env('PADDLE_API_KEY')}`, 'Content-Type': 'application/json' }, body: JSON.stringify({ effective_from: 'immediately' }) });
  }
  const key = env('SUPABASE_SERVICE_ROLE_KEY');
  const r = await f(`${env('SUPABASE_URL')}/auth/v1/admin/users/${user.id}`, { method: 'DELETE', headers: { apikey: key, Authorization: `Bearer ${key}` } });
  if (!r.ok) return [502, { error: 'delete_failed' }];
  return [200, { deleted: true, cancelled_subscriptions: subs.length }];
}

export default async function handler(req, res) {
  try { const [s, b, h] = await handle(req); send(res, s, b, h); }
  catch (e) { console.error(e); send(res, 500, { error: 'server' }); }
}
