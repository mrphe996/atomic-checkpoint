// API tests with an in-memory fake of Supabase Auth + PostgREST (node --test tests/api.test.mjs)
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
process.env.SUPABASE_URL = 'https://fake.supabase.co'; process.env.SUPABASE_ANON_KEY = 'anon'; process.env.SUPABASE_SERVICE_ROLE_KEY = 'service';
process.env.PADDLE_WEBHOOK_SECRET = 'whsec'; process.env.CRON_SECRET = 'cron'; process.env.BILLING = 'paddle';
// EDGE=1 runs the same tests against the Supabase Edge Function build (supabase/functions/api)
const EDGE = !!process.env.EDGE;
if (EDGE) { globalThis.self = globalThis; globalThis.Deno = { env: { get: (k) => process.env[k] } }; }
const base = EDGE ? '../supabase/functions/_shared/' : '../api/';
if (EDGE) { const { setUnits } = await import('../supabase/functions/_shared/supa.js'); setUnits((await import('../supabase/functions/api/units.js')).UNITS); }
const submit = await import(base + 'submit-test.js');
const start = await import(base + 'start-test.js');
const marking = await import(base + 'marking.js');
const paddle = await import('../api/paddle-webhook.js');
const account = await import(base + 'account.js');
const signup = await import(base + 'signup.js');
const weekly = await import('../api/weekly-report.js');
const { hmac } = await import('../api/_lib/supa.js');
const content = JSON.parse(fs.readFileSync(new URL('../web/content/stage7-unit03.json', import.meta.url)));
const keys = JSON.parse(fs.readFileSync(new URL('../server/private/stage7-unit03.tests.json', import.meta.url))).papers;
const G = require('../shared/grade-core.js');

const PARENT = '00000000-0000-0000-0000-00000000000a', OTHER = '00000000-0000-0000-0000-00000000000b', MARKER = '00000000-0000-0000-0000-00000000000c';
const KID = '10000000-0000-0000-0000-000000000001';
function fakeSupabase() {
  const T = { profiles: [{ id: PARENT, role: 'parent', weekly_report: true, display_name: 'Ana' }, { id: OTHER, role: 'parent' }, { id: MARKER, role: 'marker' }],
    learners: [{ id: KID, parent_id: PARENT, nickname: 'Neutron', stage: 7 }], progress: [], attempts: [], subscriptions: [], consents: [], reports: [], notifications: [], unit_results: [], certificates: [], events: [], deleted: [], test_starts: [], enrolments: [] };
  const tokens = { tA: PARENT, tB: OTHER, tM: MARKER };
  const split = s => { const out = []; let d = 0, cur = ''; for (const ch of s) { if (ch === '(') d++; if (ch === ')') d--; if (ch === ',' && d === 0) { out.push(cur); cur = ''; } else cur += ch; } out.push(cur); return out; };
  const cond = (row, c) => { const g = /^(and|or)\((.*)\)$/.exec(c); if (g) return g[1] === 'and' ? split(g[2]).every(x => cond(row, x)) : split(g[2]).some(x => cond(row, x));
    const [k, op, ...v] = c.split('.'); const val = v.join('.'); return op === 'eq' ? String(row[k]) === val : op === 'neq' ? String(row[k]) !== val : true; };
  const match = (row, q) => [...q.entries()].every(([k, v]) => {
    if (['select', 'order', 'limit', 'on_conflict'].includes(k)) return true;
    if (k === 'or' || k === 'and') return cond(row, k + v);
    const [op, ...rest] = v.split('.'); const val = rest.join('.');
    if (op === 'eq') return String(row[k]) === val;
    if (op === 'in') return val.replace(/[()]/g, '').split(',').includes(String(row[k]));
    return true;
  });
  const f = async (url, opt = {}) => {
    const u = new URL(url); const m = (opt.method || 'GET').toUpperCase();
    const json = (s, b) => ({ ok: s < 400, status: s, json: async () => b, text: async () => (b == null ? '' : JSON.stringify(b)) });
    if (u.pathname === '/auth/v1/user') { const id = tokens[(opt.headers.Authorization || '').slice(7)]; return id ? json(200, { id, email: id.slice(-1) + '@test' }) : json(401, {}); }
    if (u.pathname.startsWith('/auth/v1/admin/users/')) { const id = u.pathname.split('/').pop(); if (m === 'DELETE') { T.deleted.push(id); return json(200, {}); } return json(200, { id, email: 'parent@test' }); }
    const t = u.pathname.replace('/rest/v1/', '');
    if (t === 'rpc/has_subscription') return json(200, T.subscriptions.some(s => s.parent_id === JSON.parse(opt.body).p_parent && ['active', 'trialing'].includes(s.status)));
    const rows = T[t]; if (!rows) return json(404, {});
    if (m === 'GET') { let r = rows.filter(x => match(x, u.searchParams)); if (u.searchParams.get('order') === 'n.asc') r = r.sort((a, b) => a.n - b.n); return json(200, r); }
    if (m === 'POST') { const b = JSON.parse(opt.body); const row = { id: crypto.randomUUID(), created_at: new Date().toISOString(), ...b };
      if (t === 'attempts' && rows.some(r => r.learner_id === b.learner_id && r.client_key === b.client_key)) return json(409, {});
      if (t === 'test_starts') { const ex = rows.find(r => r.learner_id === b.learner_id && r.unit === b.unit && r.form === b.form); if (ex) return json(201, []); row.started_at = row.created_at; }
      if (t === 'subscriptions') { const i = rows.findIndex(r => r.provider_subscription_id === b.provider_subscription_id); if (i >= 0) { rows[i] = { ...rows[i], ...b }; return json(201, [rows[i]]); } }
      rows.push(row); return json(201, [row]); }
    if (m === 'DELETE') { const keep = rows.filter(x => !match(x, u.searchParams)); T[t] = keep; return json(200, null); }
    if (m === 'PATCH') { const r = rows.filter(x => match(x, u.searchParams)); r.forEach(x => Object.assign(x, JSON.parse(opt.body))); return json(200, r); }
    return json(405, {});
  };
  return { T, f };
}
const req = (method, token, body, headers = {}) => ({ method, headers: { authorization: token ? 'Bearer ' + token : '', ...headers }, body });
const fullState = () => { const st = { video: {}, items: {}, rem: {} }; content.sections.forEach(s => { st.video[s.id] = { completed: true, stops: Object.fromEntries(s.stops.map(x => [x.id, { done: true }])) }; s.req.forEach(q => st.items[q.id] = { done: true, ok: true }); }); return st; };
const right = q => { switch (q.type) { case 'mcq': return q.options.findIndex(o => o.ok); case 'multi': return q.options.map((o, i) => (o.ok ? i : -1)).filter(i => i >= 0);
  case 'num': case 'scale': return { v: String(q.answer), u: q.unit }; case 'label': return { ...q.spots }; case 'order': return q.items.slice(); case 'match': return Object.fromEntries(q.pairs.map(p => [p.l, p.r]));
  case 'explain': return q.model; case 'grid': return q.rows.map(r => r.a.slice()); case 'table': { const o = {}; q.rows.forEach((row, ri) => row.forEach((c, ci) => { if (c && typeof c === 'object') (o[ri] = o[ri] || {})[ci] = String(c.ans); })); return o; }
  case 'short': return G.answerText(q); case 'expr': return q.expr; case 'cloze': return q.blanks.map(b => b.find(a => !(a[0] === '/' && a.lastIndexOf('/') > 0)) || '');
  case 'graph': return { pts: (q.plot || q.pts).map(p => p.slice()), f: q.follow ? q.follow.options.findIndex(o => o.ok) : null }; } };

test('submit-test: auth, ownership, subscription and unlock rules', async () => {
  const { T, f } = fakeSupabase();
  const body = { learnerId: KID, unit: 'stage7-unit04', form: 'A', answers: {}, clientKey: 'k1' };
  assert.equal((await submit.handle(req('POST', null, body), f))[0], 401);
  assert.equal((await submit.handle(req('POST', 'tB', body), f))[0], 403, 'another parent cannot submit for this child');
  assert.equal((await submit.handle(req('POST', 'tA', body), f))[0], 402, 'no subscription → payment required');
  T.subscriptions.push({ parent_id: PARENT, status: 'active', provider_subscription_id: 'sub_1' });
  const [s, b] = await submit.handle(req('POST', 'tA', body), f);
  assert.equal(s, 409); assert.equal(b.error, 'locked'); assert.ok(b.missing.length > 30, 'every unfinished activity is listed');
});

test('submit-test: test phase (BILLING=off) needs no subscription', async () => {
  const { f } = fakeSupabase(); process.env.BILLING = 'off';
  try {
    const [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit04', form: 'A', answers: {}, clientKey: 'k9' }), f);
    assert.equal(s, 409); assert.equal(b.error, 'locked', 'goes straight to the learning rules, no 402');
  } finally { process.env.BILLING = 'paddle'; }
});

test('submit-test: server marks 15/30, keeps both attempts, idempotent, first pass then locked', async () => {
  const { T, f } = fakeSupabase();
  T.subscriptions.push({ parent_id: PARENT, status: 'active', provider_subscription_id: 'sub_1' });
  T.progress.push({ learner_id: KID, unit: 'stage7-unit03', state: fullState() });
  // answer parts worth exactly 15 marks correctly; get every multiple-choice part wrong and leave the rest blank
  const ansA = {}; let got = 0;
  keys.A.forEach(q => { if (got + q.pts <= 15 && q.type !== 'mcq') { ansA[q.id] = right(q); got += q.pts; } else if (q.type === 'mcq') ansA[q.id] = q.options.findIndex(o => !o.ok); });
  keys.A.forEach(q => { if (got < 15 && q.type === 'mcq' && got + q.pts <= 15) { ansA[q.id] = right(q); got += q.pts; } });
  assert.equal(got, 15);
  const firstRight = keys.A.find(q => ansA[q.id] !== undefined && q.type !== 'mcq').id;
  let [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A', answers: ansA, clientKey: 'k1' }), f);
  assert.equal(s, 201); assert.equal(b.attempt.status, 'final', 'every part is marked automatically'); assert.equal(b.attempt.auto, 15);
  assert.equal(b.attempt.score, 15); assert.equal(b.attempt.passed, false); assert.ok(b.attempt.remed.length > 0);
  assert.ok(String(b.solutions[firstRight].answer).length > 0, 'solutions returned after submission');
  const [s2, b2] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A', answers: ansA, clientKey: 'k1' }), f);
  assert.equal(s2, 200); assert.equal(b2.duplicate, true); assert.equal(T.attempts.length, 1, 'double submit creates no second attempt');
  // parents cannot open the marking queue, and there is nothing left to mark by hand
  assert.equal((await marking.handle(req('GET', 'tA'), f))[0], 403);
  const [, q] = await marking.handle(req('GET', 'tM'), f); assert.equal(q.queue.length, 0);
  // retake blocked until review questions done, then Paper B is required
  [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'B', answers: {}, clientKey: 'k3' }), f);
  assert.equal(b.error, 'review_first');
  const st = T.progress[0].state; T.attempts[0].remed.forEach(id => st.rem[`rem1:${id}`] = { done: true });
  assert.equal((await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A', answers: {}, clientKey: 'k4' }), f))[1].error, 'wrong_paper');
  const ansB = Object.fromEntries(keys.B.map(qq => [qq.id, right(qq)]));
  [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'B', answers: ansB, clientKey: 'k5' }), f);
  assert.equal(s, 201); assert.equal(b.attempt.auto, 30); assert.equal(b.attempt.score, 30); assert.equal(b.attempt.passed, true);
  assert.equal(T.attempts.length, 2, 'history keeps both attempts');
  assert.equal((await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A', answers: {}, clientKey: 'k6' }), f))[1].error, 'already_passed');
});

test('pass rule is strictly above 70 % of the raw score', () => {
  const R = require('../shared/test-rules.js');
  assert.deepEqual([R.isPass(21), R.isPass(21.5), R.isPass(14, 20), R.isPass(15, 20)], [false, true, false, true]);
});

test('public content never contains test answer keys', () => {
  const s = JSON.stringify(content.tests);
  for (const k of ['"ok"', '"answer"', '"model"', '"rubric"', '"spots"', '"ans"', '"fb"']) assert.ok(!s.includes(k), k + ' leaked');
  assert.equal(G.stripKeys(keys.A.find(q => q.type === 'mcq')).options[0].ok, undefined);
});

test('paddle webhook: signature checked, subscription mirrored', async () => {
  const { T, f } = fakeSupabase(); const now = Date.now(); const ts = Math.floor(now / 1000);
  const raw = JSON.stringify({ event_type: 'subscription.created', data: { id: 'sub_9', status: 'trialing', custom_data: { parent_id: PARENT }, items: [{ price: { id: 'pri_yearly' } }], current_billing_period: { ends_at: '2027-11-20T00:00:00Z' } } });
  assert.equal((await paddle.handle({ method: 'POST', headers: { 'paddle-signature': `ts=${ts};h1=deadbeef` }, body: raw }, f, now))[0], 401);
  const ok = await paddle.handle({ method: 'POST', headers: { 'paddle-signature': `ts=${ts};h1=${hmac('whsec', `${ts}:${raw}`)}` }, body: raw }, f, now);
  assert.equal(ok[0], 200); assert.equal(T.subscriptions[0].plan, 'stage7_yearly'); assert.equal(T.subscriptions[0].status, 'trialing');
  const raw2 = raw.replace('trialing', 'canceled');
  await paddle.handle({ method: 'POST', headers: { 'paddle-signature': `ts=${ts};h1=${hmac('whsec', `${ts}:${raw2}`)}` }, body: raw2 }, f, now);
  assert.equal(T.subscriptions.length, 1); assert.equal(T.subscriptions[0].status, 'canceled');
  const old = await paddle.handle({ method: 'POST', headers: { 'paddle-signature': `ts=${ts - 3600};h1=${hmac('whsec', `${ts - 3600}:${raw}`)}` }, body: raw }, f, now);
  assert.equal(old[0], 401, 'replayed (old) notifications are refused');
});

test('account: export and delete need the parent, delete needs the exact confirmation', async () => {
  const { T, f } = fakeSupabase();
  const [s, b] = await account.handle(req('GET', 'tA'), f);
  assert.equal(s, 200); assert.equal(b.learners.length, 1); assert.ok('attempts' in b && 'progress' in b);
  assert.equal((await account.handle(req('POST', 'tA', { confirm: 'yes' }), f))[0], 400);
  assert.equal((await account.handle(req('POST', 'tA', { confirm: 'DELETE MY ACCOUNT' }), f))[0], 200);
  assert.deepEqual(T.deleted, [PARENT]);
});

test('weekly report: cron secret required; only opted-in parents; dry run without mail key', async () => {
  const { f } = fakeSupabase();
  assert.equal((await weekly.handle(req('GET', 'nope'), f))[0], 401);
  const [s, b] = await weekly.handle({ method: 'GET', headers: { authorization: 'Bearer cron' } }, f);
  assert.equal(s, 200); assert.equal(b.dryRun, true); assert.equal(b.preview.length, 1); assert.match(b.preview[0].text, /Neutron/);
});

test('signup: a student creates a confirmed account with school, grade and an optional parent email', async () => {
  const { T, f: fake } = fakeSupabase(); const seen = [];
  const f = async (url, init) => { if (String(url).endsWith('/auth/v1/admin/users')) { const b = JSON.parse(init.body); seen.push(b); const dup = b.email === 'taken@school.org';
    return new Response(JSON.stringify(dup ? { msg: 'A user with this email address has already been registered' } : { id: 'stud-' + seen.length }), { status: dup ? 422 : 200 }); } return fake(url, init); };
  const y = new Date().getFullYear(); const ok = { name: 'Bao  Tran', email: 'Bao@School.org', password: 'password123', birthYear: y - 12, grade: 'Year 7', country: 'VN', schoolId: 5, parentEmail: 'Mum@Family.org' };
  const call = (b) => signup.handle({ method: 'POST', headers: {}, body: b }, f);
  assert.equal((await call({ ...ok, email: 'bad' }))[1].error, 'bad_email');
  assert.equal((await call({ ...ok, password: 'short' }))[1].error, 'weak_password');
  assert.equal((await call({ ...ok, name: 'A' }))[1].error, 'bad_name');
  assert.equal((await call({ ...ok, birthYear: undefined }))[1].error, 'bad_birth_year');
  assert.equal((await call({ ...ok, parentEmail: 'nope' }))[1].error, 'bad_parent_email');
  const [s1] = await call(ok); assert.equal(s1, 201);
  assert.equal(seen.at(-1).email_confirm, true); assert.equal(seen.at(-1).user_metadata.role, 'student'); assert.equal(seen.at(-1).email, 'bao@school.org');
  const l = T.learners.find(x => x.user_id === 'stud-' + seen.length);
  assert.deepEqual([l.nickname, l.certificate_name, l.school_id, l.grade, l.parent_email, l.consent_status], ['Bao', 'Bao Tran', 5, 'Year 7', 'mum@family.org', 'not_required']);
  const [s2] = await call({ ...ok, email: 'solo@school.org', parentEmail: '', schoolId: null, schoolOther: 'Home school' }); assert.equal(s2, 201);
  const l2 = T.learners.find(x => x.user_id === 'stud-' + seen.length); assert.equal(l2.parent_email, null); assert.equal(l2.school_other, 'Home school');
  assert.equal((await call({ ...ok, email: 'taken@school.org' }))[1].error, 'email_taken');
  process.env.DIRECT_SIGNUP = 'off'; try { assert.equal((await call(ok))[0], 404); } finally { delete process.env.DIRECT_SIGNUP; }
});

test('submit-test: a student can submit for themself only after parental consent', async () => {
  const { T, f } = fakeSupabase(); const STU = '00000000-0000-0000-0000-0000000000d1', LID = '10000000-0000-0000-0000-0000000000d1';
  T.profiles.push({ id: STU, role: 'student' }); T.learners.push({ id: LID, user_id: STU, parent_id: null, nickname: 'Kid', consent_status: 'pending' });
  const tok = 'tS'; const f2 = async (url, init = {}) => { if (String(url).endsWith('/auth/v1/user') && (init.headers.Authorization || '').endsWith(tok)) return { ok: true, status: 200, json: async () => ({ id: STU }) }; return f(url, init); };
  const body = { learnerId: LID, unit: 'stage7-unit04', form: 'A', answers: {}, clientKey: 'ks' };
  assert.equal((await submit.handle(req('POST', tok, body), f2))[0], 403, 'pending consent → not allowed');
  T.learners.find(l => l.id === LID).consent_status = 'approved'; process.env.BILLING = 'off';
  const [s, b] = await submit.handle(req('POST', tok, body), f2); process.env.BILLING = 'paddle'; assert.equal(s, 409); assert.equal(b.error, 'locked', 'approved → normal unlock rules');
  assert.equal((await submit.handle(req('POST', 'tB', body), f2))[0], 403, 'an unrelated parent still cannot');
});

test('Unit 3 is open in the test phase: no unlock rules for its Unit Test', async () => {
  const { f } = fakeSupabase(); process.env.BILLING = 'off';
  try {
    const ans = Object.fromEntries(keys.A.map(q => [q.id, right(q)]));
    const [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A', answers: ans, clientKey: 'o1' }), f);
    assert.equal(s, 201); assert.equal(b.attempt.auto, 30);
  } finally { process.env.BILLING = 'paddle'; }
});

test('exam room: the server times the paper from when it was opened', async () => {
  const { T, f } = fakeSupabase(); process.env.BILLING = 'off';
  try {
    const [s, b] = await start.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A' }), f);
    assert.equal(s, 200); assert.equal(b.minutes, 45); assert.ok(Date.parse(b.deadline) - Date.parse(b.startedAt) === 45 * 60000);
    const [, b2] = await start.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A' }), f);
    assert.equal(b2.startedAt, b.startedAt, 'reopening keeps the same clock');
    T.test_starts[0].started_at = new Date(Date.now() - 50 * 60000).toISOString();   // opened 50 minutes ago
    const [s3, b3] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A', answers: {}, clientKey: 't1' }), f);
    assert.equal(s3, 201); assert.ok(b3.attempt.duration >= 2999); assert.equal(b3.attempt.overtime, true);
    assert.equal(T.test_starts.length, 0, 'clock cleared after submitting');
  } finally { process.env.BILLING = 'paddle'; }
});

test('end-of-year exam: needs Level 10, one attempt per paper, marked out of 50', async () => {
  const { T, f } = fakeSupabase(); process.env.BILLING = 'off';
  const fk = JSON.parse(fs.readFileSync(new URL('../server/private/stage7-final.tests.json', import.meta.url))).papers;
  try {
    const ans = Object.fromEntries(fk['03'].map(q => [q.id, right(q)]));
    let [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-final', form: '03', answers: ans, clientKey: 'f1' }), f);
    assert.equal(s, 409); assert.equal(b.error, 'level_required'); assert.equal(b.level, 10);
    const items = {}; for (let i = 0; i < 400; i++) items['q' + i] = { done: true, ok: true, score: 1, tries: 1 };   // 400 × 12 XP = Level 10
    T.progress.push({ learner_id: KID, unit: 'stage7-unit02', state: { items } });
    [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-final', form: '03', answers: ans, clientKey: 'f2' }), f);
    assert.equal(s, 201); assert.equal(b.attempt.status, 'final'); assert.equal(b.attempt.score, 50); assert.equal(b.attempt.passed, true);
    assert.equal(Object.keys(b.attempt.byObj).length, 14, 'scored by unit');
    [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-final', form: '03', answers: ans, clientKey: 'f3' }), f);
    assert.equal(b.error, 'paper_done');
  } finally { process.env.BILLING = 'paddle'; }
});

test('a stage the learner is not enrolled in is refused', async () => {
  const { T, f } = fakeSupabase(); process.env.BILLING = 'off';
  try {
    T.learners[0].stage = 8;
    const [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A', answers: {}, clientKey: 'e1' }), f);
    assert.equal(s, 402); assert.equal(b.error, 'not_enrolled');
    T.enrolments.push({ learner_id: KID, stage: 7, status: 'active' });
    assert.equal((await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-unit03', form: 'A', answers: {}, clientKey: 'e2' }), f))[0], 201);
  } finally { process.env.BILLING = 'paddle'; }
});

test('Checkpoint-format papers: 45 minutes, no level gate, marked by strand, leaving the room is recorded', async () => {
  const { T, f } = fakeSupabase(); process.env.BILLING = 'off';
  const ck = JSON.parse(fs.readFileSync(new URL('../server/private/stage7-cp.tests.json', import.meta.url)));
  try {
    assert.equal(ck.minutes, 45); assert.equal(ck.max, 50); assert.ok(Object.keys(ck.papers).length >= 4);
    const [s0, b0] = await start.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-cp', form: 'A1' }), f);
    assert.equal(s0, 200); assert.equal(b0.minutes, 45);
    const ans = Object.fromEntries(ck.papers.A1.map(q => [q.id, right(q)]));
    let [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-cp', form: 'A1', answers: ans, clientKey: 'c1', meta: { leaves: 2, auto: false } }), f);
    assert.equal(s, 201); assert.equal(b.attempt.score, 50);
    assert.deepEqual(Object.keys(b.attempt.byObj).sort(), ['BIO', 'CHE', 'ESS', 'PHY', 'TWS']);
    assert.equal(T.attempts[0].leaves, 2); assert.equal(T.attempts[0].auto_submitted, false);
    [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-cp', form: 'A1', answers: ans, clientKey: 'c2' }), f);
    assert.equal(b.error, 'paper_done');
    [s, b] = await submit.handle(req('POST', 'tA', { learnerId: KID, unit: 'stage7-cp', form: 'B2', answers: {}, clientKey: 'c3', meta: { leaves: 3, auto: true } }), f);
    assert.equal(s, 201); assert.equal(T.attempts[1].auto_submitted, true);
  } finally { process.env.BILLING = 'paddle'; }
});

test('admin: only admins; key overrides and withdrawn questions change the marking', async () => {
  const admin = await import(base + 'admin.js');
  const { T, f } = fakeSupabase(); T.question_overrides = []; T.admin_audit = [];
  assert.equal((await admin.handle({ method: 'GET', headers: { authorization: 'Bearer tA' }, query: { unit: 'stage7-unit03' } }, f))[0], 403, 'a parent is not an admin');
  assert.equal((await admin.handle({ method: 'GET', headers: { authorization: 'Bearer tM' }, query: { unit: 'stage7-unit03' } }, f))[0], 403, 'a marker is not an admin');
  T.profiles.find(p => p.id === MARKER).role = 'admin';
  const [s, b] = await admin.handle({ method: 'GET', headers: { authorization: 'Bearer tM' }, query: { unit: 'stage7-unit03' } }, f);
  assert.equal(s, 200); assert.ok(b.papers.A.length > 5, 'admins see the keyed papers');
  // a finished attempt that answered everything right, then the admin withdraws one question and changes another's key
  const paper = keys.A; const answers = Object.fromEntries(paper.map(q => [q.id, right(q)]));
  const auto = paper.filter(q => !q.teacher);
  const pick = auto.find(q => q.type === 'mcq');
  T.attempts.push({ id: 'att1', learner_id: KID, unit: 'stage7-unit03', n: 1, form: 'A', client_key: 'x', answers, per: {}, auto: 30, score: 30, pct: 100, status: 'final', passed: true, created_at: new Date().toISOString() });
  T.question_overrides.push({ question_id: pick.id, unit: 'stage7-unit03', hidden: false, key_patch: { ...pick, options: pick.options.map(o => ({ ...o, ok: !o.ok })) } });
  const [s2, r2] = await admin.handle({ method: 'POST', headers: { authorization: 'Bearer tM' }, body: { action: 'regrade', attemptId: 'att1' } }, f);
  assert.equal(s2, 200); assert.ok(r2.result.changed && r2.result.to < 30, 'the changed key costs the learner those marks');
  T.question_overrides[0].hidden = true;
  const [, r3] = await admin.handle({ method: 'POST', headers: { authorization: 'Bearer tM' }, body: { action: 'regrade_unit', unit: 'stage7-unit03' } }, f);
  assert.equal(r3.attempts, 1); assert.equal(T.attempts[0].score, 30, 'a withdrawn question gives everyone full marks');
  assert.ok(T.admin_audit.length >= 2, 'admin actions are logged');
});
