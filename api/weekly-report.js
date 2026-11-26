// GET /api/weekly-report — Vercel Cron (see vercel.json), Monday 08:00 UTC.
// Emails a short weekly summary ONLY to parents who switched it on (weekly_report = true, off by default).
// Without RESEND_API_KEY it runs as a dry run and returns what it would send.
import { send, db, env, safeEqual } from './_lib/supa.js';

export function summary(learner, prog, attempts, since) {
  const st = (prog && prog.state) || {}; const items = st.items || {};
  const done = Object.values(items).filter(r => r.done).length;
  const recent = attempts.filter(a => Date.parse(a.created_at) >= since);
  const lines = [`${learner.nickname}: ${done} questions completed in Unit 3 so far.`];
  if (prog && Date.parse(prog.updated_at) < since) lines.push('No learning activity this week.');
  recent.forEach(a => lines.push(`Unit Test (Paper ${a.form}): ${a.status === 'pending' ? 'awaiting marking' : `${Math.round(a.pct)}% – ${a.passed ? 'passed' : 'not passed yet'}`}`));
  return lines.join('\n');
}

export async function handle(req, f = fetch, now = Date.now()) {
  const auth = String(req.headers.authorization || '');
  if (!env('CRON_SECRET') || !safeEqual(auth, `Bearer ${env('CRON_SECRET')}`)) return [401, { error: 'cron_only' }];
  const since = now - 7 * 864e5;
  const parents = await db('profiles?weekly_report=eq.true&select=id,display_name', {}, f);
  const out = [];
  for (const p of parents) {
    const users = await f(`${env('SUPABASE_URL')}/auth/v1/admin/users/${p.id}`, { headers: { apikey: env('SUPABASE_SERVICE_ROLE_KEY'), Authorization: `Bearer ${env('SUPABASE_SERVICE_ROLE_KEY')}` } });
    const email = users.ok ? (await users.json()).email : null; if (!email) continue;
    const kids = await db(`learners?parent_id=eq.${p.id}&select=id,nickname`, {}, f);
    const parts = [];
    for (const k of kids) {
      const prog = (await db(`progress?learner_id=eq.${k.id}&unit=eq.stage7-unit03&select=state,updated_at`, {}, f))[0];
      const att = await db(`attempts?learner_id=eq.${k.id}&select=form,status,pct,passed,created_at`, {}, f);
      parts.push(summary(k, prog, att, since));
    }
    const text = `Hello ${p.display_name || ''},\n\nHere is this week's Camday summary:\n\n${parts.join('\n\n')}\n\nYou can switch these emails off in Parent area → Settings.\n— Camday`;
    if (env('RESEND_API_KEY')) {
      await f('https://api.resend.com/emails', { method: 'POST', headers: { Authorization: `Bearer ${env('RESEND_API_KEY')}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({ from: env('MAIL_FROM', 'Camday <hello@example.com>'), to: [email], subject: 'Your weekly Camday summary', text }) });
    }
    out.push({ to: email, text });
  }
  return [200, { sent: env('RESEND_API_KEY') ? out.length : 0, dryRun: !env('RESEND_API_KEY'), preview: out.slice(0, 3) }];
}

export default async function handler(req, res) {
  try { const [s, b] = await handle(req); send(res, s, b); }
  catch (e) { console.error(e); send(res, 500, { error: 'server' }); }
}
