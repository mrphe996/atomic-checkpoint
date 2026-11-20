// POST /api/submit-test  { learnerId, unit, form, answers, clientKey }
// Marks a Unit Test or an end-of-year exam on the server: answer keys never reach the browser before submission.
// The exam room is timed from the moment the paper was opened (api/start-test.js).
import { send, readJson, getUser, db, loadUnit, ownsLearner, Rules, rowToAttempt, billingOn } from './supa.js';

const stageOf = unit => Number(String(unit).slice(5, 6));
export async function hasStage(learner, unit, f) {
  const s = stageOf(unit); if (!s || s === (learner.stage || 7)) return true;
  const e = await db(`enrolments?learner_id=eq.${learner.id}&stage=eq.${s}&status=eq.active&select=stage`, {}, f);
  return !!(e && e.length);
}
export async function learnerXp(learnerId, f) {
  const rows = await db(`progress?learner_id=eq.${learnerId}&select=unit,state`, {}, f);
  const passes = await db(`unit_results?learner_id=eq.${learnerId}&select=unit`, {}, f);
  return Rules.xpTotal(Object.fromEntries((rows || []).filter(r => !Rules.isFinal(r.unit)).map(r => [r.unit, r.state])), (passes || []).length);
}

export async function handle(req, f = fetch) {
  if (req.method !== 'POST') return [405, { error: 'method' }];
  const user = await getUser(req, f); if (!user) return [401, { error: 'sign_in' }];
  const b = await readJson(req);
  const { learnerId, unit, form, answers, clientKey } = b || {};
  if (!answers || typeof answers !== 'object' || !clientKey || String(clientKey).length > 64) return [400, { error: 'bad_request' }];
  const learner = await ownsLearner(user.id, learnerId, f); if (!learner) return [403, { error: 'not_your_learner' }];
  if (billingOn()) {
    const sub = await db('rpc/has_subscription', { method: 'POST', body: { p_parent: user.id } }, f);
    if (sub !== true) return [402, { error: 'subscription_required' }];
  }
  let pack; try { pack = loadUnit(unit); } catch (e) { return [400, { error: 'unknown_unit' }]; }
  if (!(await hasStage(learner, unit, f))) return [402, { error: 'not_enrolled' }];

  const prev = await db(`attempts?learner_id=eq.${learnerId}&unit=eq.${unit}&order=n.asc`, {}, f);
  const same = prev.find(r => r.client_key === clientKey);
  if (same) return [200, { attempt: rowToAttempt(same), solutions: Rules.solutions(pack.papers[same.form]), duplicate: true }];

  const last = prev[prev.length - 1];
  if (last && last.status === 'pending') return [409, { error: 'awaiting_marking' }];
  let state = {};
  if (pack.final) {
    if (!pack.papers[form]) return [409, { error: 'wrong_paper' }];
    if (prev.some(r => r.form === form)) return [409, { error: 'paper_done' }];
    const xp = await learnerXp(learnerId, f);
    if (Rules.levelOf(xp) < pack.level) return [409, { error: 'level_required', level: pack.level, have: Rules.levelOf(xp) }];
  } else {
    const prog = await db(`progress?learner_id=eq.${learnerId}&unit=eq.${unit}&select=state`, {}, f);
    state = (prog[0] && prog[0].state) || {};
    const missing = Rules.missingForTest(pack.content, state, unit);
    if (missing.length) return [409, { error: 'locked', missing }];
    if (prev.some(r => r.status === 'final' && r.passed)) return [409, { error: 'already_passed' }];
    if (last && last.status === 'final' && !last.passed) {
      const left = (last.remed || []).filter(id => !(((state.rem || {})[`rem${last.n}:${id}`]) || {}).done);
      if (left.length) return [409, { error: 'review_first', left }];
    }
    const expected = Rules.nextForm(prev.length);
    if (form !== expected) return [409, { error: 'wrong_paper', expected }];
  }

  // exam-room timing: from the moment the paper was opened
  const limit = (pack.final ? pack.minutes : Rules.UNIT_MINUTES) * 60;
  const st = await db(`test_starts?learner_id=eq.${learnerId}&unit=eq.${unit}&form=eq.${form}&select=started_at`, {}, f);
  const startedAt = st && st[0] ? st[0].started_at : null;
  const duration = startedAt ? Math.round((Date.now() - Date.parse(startedAt)) / 1000) : null;

  const paper = pack.papers[form];
  const raw = Rules.mark(paper, answers, { n: prev.length + 1, form });
  const a = pack.final ? Rules.finalizeFinal(raw, paper, pack.max, pack.pass) : Rules.finalize(raw, paper, pack.content, state);
  const row = { learner_id: learnerId, unit, n: a.n, form, client_key: clientKey, answers: a.answers, per: a.per, auto: a.auto,
    score: a.score, pct: a.pct, status: a.status, passed: a.status === 'final' ? a.passed : null, by_obj: a.byObj || null, weak: a.weak || null, remed: a.remed || null,
    finalised_at: a.status === 'final' ? new Date().toISOString() : null, started_at: startedAt, duration_s: duration, overtime: duration != null && duration > limit + Rules.GRACE_S };
  const saved = await db('attempts', { method: 'POST', body: row, prefer: 'return=representation' }, f);
  if (startedAt) await db(`test_starts?learner_id=eq.${learnerId}&unit=eq.${unit}&form=eq.${form}`, { method: 'DELETE' }, f);
  return [201, { attempt: rowToAttempt(saved[0]), solutions: Rules.solutions(paper) }];
}

