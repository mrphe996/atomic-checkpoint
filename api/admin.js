// Admin console server actions (role admin only). Answer keys stay on the server; only admins can read them here.
// GET  /api/admin?unit=stage19-unit01           → the built test papers WITH keys + the current overrides (for the question editor)
// POST /api/admin { action: 'regrade', attemptId } → re-mark one attempt with the current keys (after an admin fixed a question)
// POST /api/admin { action: 'regrade_unit', unit } → re-mark every finished attempt of a unit or exam
// POST /api/admin { action: 'refresh' }            → drop the cached overrides on this server instance
import { send, readJson, getUser, db, loadUnit, loadPack, overridesFor, clearOverrides, role, Rules, rowToAttempt } from './_lib/supa.js';

async function audit(actor, action, target, detail, f) {
  try { await db('admin_audit', { method: 'POST', body: { actor, action, target, detail: detail || {} } }, f); } catch (e) { /* the action itself succeeded */ }
}

async function regradeRow(row, f) {
  const pack = await loadPack(row.unit, f); const paper = pack.papers[row.form];
  if (!paper) return { id: row.id, skipped: 'paper_missing' };
  const old = rowToAttempt(row);
  const a = Rules.mark(paper, row.answers || {}, { n: row.n, form: row.form });
  // keep marks a teacher already gave to written answers
  for (const id of a.pending) if (old.per[id] && old.per[id].pts != null) a.per[id].pts = old.per[id].pts;
  if (pack.final) Rules.finalizeFinal(a, paper, pack.max, pack.pass);
  else { const prog = await db(`progress?learner_id=eq.${row.learner_id}&unit=eq.${row.unit}&select=state`, {}, f); Rules.finalize(a, paper, pack.content, (prog[0] && prog[0].state) || {}); }
  const changed = a.score !== old.score || a.passed !== old.passed || a.status !== old.status;
  if (!changed) return { id: row.id, changed: false, score: a.score };
  await db(`attempts?id=eq.${row.id}`, { method: 'PATCH', body: { per: a.per, auto: a.auto, score: a.score, pct: a.pct, status: a.status, passed: a.status === 'final' ? a.passed : null,
    by_obj: a.byObj || null, weak: a.weak || null, remed: a.remed || null, finalised_at: a.status === 'final' ? new Date().toISOString() : null } }, f);
  if (old.passed && !a.passed) await db(`unit_results?attempt_id=eq.${row.id}`, { method: 'DELETE' }, f);
  return { id: row.id, changed: true, from: old.score, to: a.score, passed: a.passed };
}

export async function handle(req, f = fetch) {
  const user = await getUser(req, f); if (!user) return [401, { error: 'sign_in' }];
  if ((await role(user.id, f)) !== 'admin') return [403, { error: 'admin_only' }];
  if (req.method === 'GET') {
    const unit = String((req.query || {}).unit || '');
    let base; try { base = loadUnit(unit); } catch (e) { return [400, { error: 'unknown_unit' }]; }
    clearOverrides(unit);
    const ov = await overridesFor(unit, f);
    return [200, { unit, final: !!base.final, papers: base.papers, overrides: ov }];
  }
  if (req.method !== 'POST') return [405, { error: 'method' }];
  const b = (await readJson(req)) || {};
  if (b.action === 'refresh') { clearOverrides(b.unit); return [200, { ok: true }]; }
  if (b.action === 'regrade') {
    const rows = await db(`attempts?id=eq.${encodeURIComponent(String(b.attemptId || ''))}`, {}, f);
    if (!rows || !rows.length) return [404, { error: 'not_found' }];
    clearOverrides(rows[0].unit);
    const r = await regradeRow(rows[0], f);
    await audit(user.id, 'regrade', String(b.attemptId), r, f);
    const fresh = await db(`attempts?id=eq.${rows[0].id}`, {}, f);
    return [200, { result: r, attempt: fresh && fresh[0] ? rowToAttempt(fresh[0]) : null }];
  }
  if (b.action === 'regrade_unit') {
    const unit = String(b.unit || ''); try { loadUnit(unit); } catch (e) { return [400, { error: 'unknown_unit' }]; }
    clearOverrides(unit);
    const rows = await db(`attempts?unit=eq.${unit}&status=eq.final&order=created_at.asc&limit=1000`, {}, f);
    const out = []; for (const row of rows || []) out.push(await regradeRow(row, f));
    const changed = out.filter(x => x.changed);
    await audit(user.id, 'regrade_unit', unit, { attempts: out.length, changed: changed.length }, f);
    return [200, { attempts: out.length, changed: changed.length, results: changed }];
  }
  return [400, { error: 'bad_action' }];
}

export default async function handler(req, res) {
  try {
    const url = new URL(req.url, 'http://x'); req.query = req.query || Object.fromEntries(url.searchParams);
    const [s, b] = await handle(req); send(res, s, b);
  } catch (e) { console.error(e); send(res, e.status && e.status < 500 ? e.status : 500, { error: 'server' }); }
}
