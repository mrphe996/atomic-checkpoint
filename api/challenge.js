// POST /api/challenge  Maths Challenge practice mode (papers in content/src/ch-*.json, answer keys server-side only).
//   { action: 'check', learnerId, unit, form, qid, answer } → { ok, answer, reason }   marks one question and shows its full solution
//   { action: 'solutions', learnerId, unit, form }           → { solutions }   only after the paper has been sat (timed)
//   { action: 'state', learnerId, unit }                     → { done: [{ form, qid, ok }], solutions: { qid: {answer, reason} } }
// The first answer to each question is the one recorded. A paper that has been practised can no longer be sat as a timed
// paper (submit-test.js refuses it), so the solutions seen here never help a timed score.
import { send, readJson, getUser, db, loadPack, ownsLearner, billingOn, G } from './_lib/supa.js';

export const isChallenge = unit => /^ch-[a-z]+$/.test(String(unit));

export async function practised(learnerId, unit, form, f) {
  const r = await db(`challenge_practice?learner_id=eq.${learnerId}&unit=eq.${unit}&form=eq.${encodeURIComponent(form)}&select=qid&limit=1`, {}, f);
  return Array.isArray(r) && r.length > 0;
}

function sol(q) { return { answer: G.answerText(q), reason: q.reason || '' }; }

export async function handle(req, f = fetch) {
  if (req.method !== 'POST') return [405, { error: 'method' }];
  const user = await getUser(req, f); if (!user) return [401, { error: 'sign_in' }];
  const b = (await readJson(req)) || {};
  const { action, learnerId, unit, form, qid, answer } = b;
  if (!isChallenge(unit)) return [400, { error: 'unknown_unit' }];
  const learner = await ownsLearner(user.id, learnerId, f); if (!learner) return [403, { error: 'not_your_learner' }];
  let pack; try { pack = await loadPack(unit, f); } catch (e) { return [400, { error: 'unknown_unit' }]; }
  const byId = {}; for (const [k, p] of Object.entries(pack.papers)) for (const q of p) byId[q.id] = { q, form: k };

  if (action === 'state') {
    const rows = await db(`challenge_practice?learner_id=eq.${learnerId}&unit=eq.${unit}&select=form,qid,ok,answer`, {}, f);
    const solutions = {}; for (const r of rows || []) if (byId[r.qid]) solutions[r.qid] = sol(byId[r.qid].q);
    return [200, { done: (rows || []).map(r => ({ form: r.form, qid: r.qid, ok: r.ok, answer: r.answer })), solutions }];
  }
  if (action === 'solutions') {   // full worked solutions of a paper already sat in the exam room
    if (!pack.papers[form]) return [400, { error: 'wrong_paper' }];
    const at = await db(`attempts?learner_id=eq.${learnerId}&unit=eq.${unit}&form=eq.${encodeURIComponent(form)}&status=eq.final&select=id&limit=1`, {}, f);
    if (!at || !at.length) return [409, { error: 'not_taken' }];
    return [200, { solutions: Object.fromEntries(pack.papers[form].map(q => [q.id, sol(q)])) }];
  }
  if (action !== 'check') return [400, { error: 'bad_request' }];
  if (billingOn()) {   // courses are bought once: the Maths Challenge needs at least one open course
    const e = await db(`enrolments?learner_id=eq.${learnerId}&status=eq.active&select=stage&limit=1`, {}, f);
    if (!e || !e.length) return [402, { error: 'not_enrolled' }];
  }
  const hit = byId[qid]; if (!hit || hit.form !== form) return [400, { error: 'wrong_question' }];
  if (answer == null || JSON.stringify(answer).length > 500) return [400, { error: 'bad_request' }];
  // a paper already sat in the exam room can still be practised (as review); the first practice answer is kept
  const prev = await db(`challenge_practice?learner_id=eq.${learnerId}&unit=eq.${unit}&qid=eq.${encodeURIComponent(qid)}&select=ok,answer`, {}, f);
  if (prev && prev[0]) return [200, { ok: prev[0].ok, first: prev[0].answer, ...sol(hit.q), repeat: true }];
  const ok = !hit.q.voided && !!G.grade(hit.q, answer).ok;
  await db('challenge_practice?on_conflict=learner_id,unit,qid', { method: 'POST', body: { learner_id: learnerId, unit, form, qid, ok, answer }, prefer: 'resolution=ignore-duplicates' }, f);
  return [200, { ok, ...sol(hit.q) }];
}

export default async function handler(req, res) {
  try { const [s, b] = await handle(req); send(res, s, b); }
  catch (e) { console.error(e); send(res, e.status && e.status < 500 ? e.status : 500, { error: 'server' }); }
}
