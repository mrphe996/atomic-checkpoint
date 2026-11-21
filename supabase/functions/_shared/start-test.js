// POST /api/start-test  { learnerId, unit, form }
// Opens the exam room: records when the paper was first opened (kept until the paper is submitted) and returns the
// deadline, so a reload or another device keeps the same countdown.
import { send, readJson, getUser, db, loadUnit, loadPack, ownsLearner, Rules } from './supa.js';

export async function handle(req, f = fetch) {
  if (req.method !== 'POST') return [405, { error: 'method' }];
  const user = await getUser(req, f); if (!user) return [401, { error: 'sign_in' }];
  const { learnerId, unit, form } = (await readJson(req)) || {};
  const learner = await ownsLearner(user.id, learnerId, f); if (!learner) return [403, { error: 'not_your_learner' }];
  let pack; try { pack = await loadPack(unit, f); } catch (e) { return [400, { error: 'unknown_unit' }]; }
  if (!pack.papers[form]) return [400, { error: 'wrong_paper' }];
  await db('test_starts?on_conflict=learner_id,unit,form', { method: 'POST', body: { learner_id: learnerId, unit, form }, prefer: 'resolution=ignore-duplicates' }, f);
  const r = await db(`test_starts?learner_id=eq.${learnerId}&unit=eq.${unit}&form=eq.${form}&select=started_at`, {}, f);
  const minutes = pack.final ? pack.minutes : Rules.UNIT_MINUTES;
  const started = r[0].started_at;
  return [200, { startedAt: started, minutes, deadline: new Date(Date.parse(started) + minutes * 60000).toISOString(), now: new Date().toISOString() }];
}

