// POST /api/submit-test  { learnerId, unit, form, answers, clientKey, meta: { leaves, auto } }
// Marks a Unit Test or an end-of-year exam on the server: answer keys never reach the browser before submission.
// The exam room is timed from the moment the paper was opened (api/start-test.js).
import { send, readJson, getUser, db, loadUnit, loadPack, ownsLearner, Rules, rowToAttempt, billingOn } from './_lib/supa.js';
import { aiGrade, confident } from './ai-mark.js';
import { isChallenge, practised } from './challenge.js';

const stageOf = unit => Number((String(unit).match(/^stage(\d+)/) || [0, 0])[1]);
export async function hasStage(learner, unit, f) {
  const s = stageOf(unit); if (!s) return true;   // one stage per learner: only the courses they bought (sign-up no longer opens a course for free)
  const e = await db(`enrolments?learner_id=eq.${learner.id}&stage=eq.${s}&status=eq.active&select=stage`, {}, f);
  return !!(e && e.length);
}
export async function learnerXp(learnerId, f) {
  const rows = await db(`progress?learner_id=eq.${learnerId}&select=unit,state`, {}, f);
  const passes = await db(`unit_results?learner_id=eq.${learnerId}&select=unit`, {}, f);
  return Rules.xpTotal(Object.fromEntries((rows || []).filter(r => !Rules.isFinal(r.unit)).map(r => [r.unit, r.state])), (passes || []).length);
}

// accounts flagged as testers (public.testers, staff-only) skip the learning-order, level and review locks
export async function isTester(learnerId, f) {
  try { const r = await db(`testers?learner_id=eq.${learnerId}&select=learner_id`, {}, f); return Array.isArray(r) && r.length > 0; } catch (e) { return false; }
}

export async function handle(req, f = fetch) {
  if (req.method !== 'POST') return [405, { error: 'method' }];
  const user = await getUser(req, f); if (!user) return [401, { error: 'sign_in' }];
  const b = await readJson(req);
  const { learnerId, unit, form, answers, clientKey, meta } = b || {};
  const leaves = Math.max(0, Math.min(99, Math.floor(Number((meta || {}).leaves) || 0))), autoSub = !!(meta && meta.auto);
  if (!answers || typeof answers !== 'object' || !clientKey || String(clientKey).length > 64) return [400, { error: 'bad_request' }];
  const learner = await ownsLearner(user.id, learnerId, f); if (!learner) return [403, { error: 'not_your_learner' }];
  if (billingOn()) {
    const sub = await db('rpc/has_subscription', { method: 'POST', body: { p_parent: user.id } }, f);
    if (sub !== true) return [402, { error: 'subscription_required' }];
  }
  let pack; try { pack = await loadPack(unit, f); } catch (e) { return [400, { error: 'unknown_unit' }]; }
  if (!(await hasStage(learner, unit, f))) return [402, { error: 'not_enrolled' }];
  // Maths Challenge: a paper practised question by question (solutions seen) cannot then be sat as a timed paper
  if (isChallenge(unit) && pack.papers[form] && await practised(learnerId, unit, form, f)) return [409, { error: 'practised' }];

  const prev = await db(`attempts?learner_id=eq.${learnerId}&unit=eq.${unit}&order=n.asc`, {}, f);
  const same = prev.find(r => r.client_key === clientKey);
  if (same) return [200, { attempt: rowToAttempt(same), solutions: Rules.solutions(pack.papers[same.form]), duplicate: true }];

  const last = prev[prev.length - 1];
  if (last && last.status === 'pending') return [409, { error: 'awaiting_marking' }];
  let state = {};
  const tester = await isTester(learnerId, f);
  if (pack.final) {
    if (!pack.papers[form]) return [409, { error: 'wrong_paper' }];
    if (prev.some(r => r.form === form)) return [409, { error: 'paper_done' }];
    const xp = await learnerXp(learnerId, f);
    if (!tester && Rules.levelOf(xp) < pack.level) return [409, { error: 'level_required', level: pack.level, have: Rules.levelOf(xp) }];
  } else {
    const prog = await db(`progress?learner_id=eq.${learnerId}&unit=eq.${unit}&select=state`, {}, f);
    state = (prog[0] && prog[0].state) || {};
    const missing = Rules.missingForTest(pack.content, state, unit);
    if (missing.length && !tester) return [409, { error: 'locked', missing }];
    if (prev.some(r => r.status === 'final' && r.passed)) return [409, { error: 'already_passed' }];
    if (last && last.status === 'final' && !last.passed) {
      const left = (last.remed || []).filter(id => !(((state.rem || {})[`rem${last.n}:${id}`]) || {}).done);
      if (left.length && !tester) return [409, { error: 'review_first', left }];
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
  // paragraph questions: marked by AI against the mark scheme; a confident mark is final, otherwise a teacher marks it with the AI suggestion
  const ans = { ...answers }; let marked = paper;
  const paras = paper.filter(q => q.type === 'para' && !q.voided && typeof answers[q.id] === 'string' && answers[q.id].trim());
  if (paras.length) {
    const res = await Promise.all(paras.map(q => aiGrade(q, String(answers[q.id]).slice(0, 3000), f)));
    const sure = new Set();
    paras.forEach((q, i) => { const g = res[i]; if (g.ai) { ans[q.id] = { text: String(answers[q.id]), ai: g.ai, conf: g.confidence, fb: g.fb || '' }; if (confident(g)) sure.add(q.id); } });
    marked = paper.map(q => (sure.has(q.id) ? { ...q, teacher: false } : q));
  }
  const raw = Rules.mark(marked, ans, { n: prev.length + 1, form });
  for (const q of marked) if (q.type === 'para' && ans[q.id] && ans[q.id].ai && raw.per[q.id]) raw.per[q.id].ai = !q.teacher ? 'final' : 'suggest';
  const a = pack.final ? Rules.finalizeFinal(raw, paper, pack.max, pack.pass) : Rules.finalize(raw, paper, pack.content, state);
  const row = { learner_id: learnerId, unit, n: a.n, form, client_key: clientKey, answers: a.answers, per: a.per, auto: a.auto,
    score: a.score, pct: a.pct, status: a.status, passed: a.status === 'final' ? a.passed : null, by_obj: a.byObj || null, weak: a.weak || null, remed: a.remed || null,
    finalised_at: a.status === 'final' ? new Date().toISOString() : null, started_at: startedAt, duration_s: duration, overtime: duration != null && duration > limit + Rules.GRACE_S, leaves, auto_submitted: autoSub };
  const saved = await db('attempts', { method: 'POST', body: row, prefer: 'return=representation' }, f);
  if (startedAt) await db(`test_starts?learner_id=eq.${learnerId}&unit=eq.${unit}&form=eq.${form}`, { method: 'DELETE' }, f);
  return [201, { attempt: rowToAttempt(saved[0]), solutions: Rules.solutions(paper) }];
}

export default async function handler(req, res) {
  try { const [s, b] = await handle(req); send(res, s, b); }
  catch (e) { console.error(e); send(res, e.status && e.status < 500 ? e.status : 500, { error: 'server' }); }
}
