// Atomic markers (role marker/admin) mark written test answers.
// GET  /api/marking               → queue of pending attempts with the mark scheme and an automatic suggestion
// POST /api/marking { attemptId, grades: { itemId: marks } } → final mark; the database trigger records the first pass
import { send, readJson, getUser, db, loadUnit, loadPack, role, Rules, rowToAttempt } from './supa.js';

export async function handle(req, f = fetch) {
  const user = await getUser(req, f); if (!user) return [401, { error: 'sign_in' }];
  const r = await role(user.id, f); if (r !== 'marker' && r !== 'admin') return [403, { error: 'staff_only' }];
  if (req.method === 'GET') {
    const rows = await db('attempts?status=eq.pending&order=created_at.asc&limit=50&select=id,unit,n,form,answers,per,created_at,learner_id', {}, f);
    const queue = await Promise.all(rows.map(async row => {
      const { papers } = await loadPack(row.unit, f);
      const items = Object.keys(row.per).filter(k => row.per[k].teacher).map(id => {
        const q = papers[row.form].find(x => x.id === id);
        const a = row.answers[id]; const ai = a && typeof a === 'object' && a.ai ? { points: a.ai, confidence: a.conf, feedback: a.fb } : null;
        return { id, prompt: q.prompt, max: q.pts, answer: (a && typeof a === 'object' ? a.text : a) || '', rubric: q.rubric.map(p => p.pt), model: q.model, suggest: row.per[id].suggest, ai };
      });
      return { attemptId: row.id, unit: row.unit, n: row.n, form: row.form, submitted: row.created_at, learner: 'Learner ' + row.learner_id.slice(0, 4), items };
    }));
    return [200, { queue }];
  }
  if (req.method !== 'POST') return [405, { error: 'method' }];
  const { attemptId, grades } = await readJson(req);
  const rows = await db(`attempts?id=eq.${encodeURIComponent(attemptId)}&status=eq.pending`, {}, f);
  if (!rows.length) return [404, { error: 'not_pending' }];
  const row = rows[0]; const pack = await loadPack(row.unit, f); const { content, papers } = pack; const paper = papers[row.form];
  const a = rowToAttempt(row);
  for (const id of a.pending) {
    const v = Number((grades || {})[id]); if (!isFinite(v)) return [400, { error: 'missing_mark', id }];
    a.per[id].pts = Math.max(0, Math.min(a.per[id].max, Math.round(v * 2) / 2));
  }
  const prog = await db(`progress?learner_id=eq.${row.learner_id}&unit=eq.${row.unit}&select=state`, {}, f);
  if (pack.final) Rules.finalizeFinal(a, paper, pack.max, pack.pass); else Rules.finalize(a, paper, content, (prog[0] && prog[0].state) || {});
  const saved = await db(`attempts?id=eq.${row.id}`, { method: 'PATCH', prefer: 'return=representation', body: {
    per: a.per, score: a.score, pct: a.pct, status: 'final', passed: a.passed, by_obj: a.byObj, weak: a.weak, remed: a.remed, marked_by: user.id, finalised_at: new Date().toISOString() } }, f);
  return [200, { attempt: rowToAttempt(saved[0]) }];
}

