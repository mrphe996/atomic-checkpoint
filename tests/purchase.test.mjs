// One-time purchases via the Paddle webhook (node --test tests/purchase.test.mjs). Needs no answer keys.
import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
process.env.SUPABASE_URL = 'https://fake.supabase.co'; process.env.SUPABASE_SERVICE_ROLE_KEY = 'service'; process.env.PADDLE_WEBHOOK_SECRET = 'whsec';
process.env.PADDLE_PRICE_COURSE = 'pri_c'; process.env.PADDLE_PRICE_PAIR = 'pri_p'; process.env.PADDLE_PRICE_BUNDLE = 'pri_b';
const paddle = await import('../api/paddle-webhook.js');

const KID = '10000000-0000-0000-0000-000000000001';
const sign = (raw, ts) => `ts=${ts};h1=${crypto.createHmac('sha256', 'whsec').update(`${ts}:${raw}`).digest('hex')}`;
function fake() {
  const T = { purchases: [], enrolments: [], calls: [] };
  const f = async (url, opt = {}) => {
    const u = new URL(url), t = u.pathname.replace('/rest/v1/', ''), m = (opt.method || 'GET').toUpperCase();
    const json = (s, b) => ({ ok: s < 400, status: s, text: async () => (b == null ? '' : JSON.stringify(b)) });
    const body = opt.body ? JSON.parse(opt.body) : null;
    if (t === 'rpc/grant_purchase') { T.calls.push(['grant', body]); for (const s of body.p_stages) T.enrolments.push({ learner_id: body.p_learner, stage: s, status: 'active', provider_txn_id: body.p_txn }); return json(200, 'ok'); }
    if (t === 'rpc/revoke_purchase') { let n = 0; T.enrolments.forEach(e => { if (e.provider_txn_id === body.p_txn && e.status === 'active') { e.status = 'refunded'; n++; } }); return json(200, n); }
    if (t === 'purchases' && m === 'GET') { const id = decodeURIComponent(u.searchParams.get('provider_txn_id').slice(3)); return json(200, T.purchases.filter(p => p.provider_txn_id === id)); }
    if (t === 'purchases' && m === 'POST') { T.purchases.push(body); return json(201, null); }
    return json(404, {});
  };
  return { T, f };
}
const txn = (id, price, stages, extra = {}) => JSON.stringify({ event_type: 'transaction.completed', data: { id, currency_code: 'USD', items: [{ price: { id: price }, quantity: 1 }],
  custom_data: { learner_id: KID, stages }, details: { totals: { grand_total: '11900' } }, ...extra } });
const post = (raw, ts, f, now) => paddle.handle({ method: 'POST', headers: { 'paddle-signature': sign(raw, ts) }, body: raw }, f, now);

test('signature: wrong, missing and replayed notifications are refused', async () => {
  const { f } = fake(); const now = Date.now(), ts = Math.floor(now / 1000); const raw = txn('txn_1', 'pri_c', [7]);
  assert.equal((await paddle.handle({ method: 'POST', headers: { 'paddle-signature': `ts=${ts};h1=deadbeef` }, body: raw }, f, now))[0], 401);
  assert.equal((await paddle.handle({ method: 'POST', headers: {}, body: raw }, f, now))[0], 401);
  assert.equal((await post(raw, ts - 3600, f, now))[0], 401, 'old timestamp');
  assert.equal((await post(raw, ts, f, now))[0], 200);
});

test('one subject, two subjects and the whole stage open exactly what was paid for, once', async () => {
  const { T, f } = fake(); const now = Date.now(), ts = Math.floor(now / 1000);
  let [s, b] = await post(txn('txn_a', 'pri_c', [7]), ts, f, now); assert.equal(s, 200); assert.deepEqual(b.granted, [7]);
  [s, b] = await post(txn('txn_a', 'pri_c', [7]), ts, f, now); assert.equal(b.duplicate, true, 'Paddle retry grants nothing new');
  assert.equal(T.calls.length, 1);
  [, b] = await post(txn('txn_b', 'pri_p', [18, 28]), ts, f, now); assert.deepEqual(b.granted, [18, 28]);
  [, b] = await post(txn('txn_c', 'pri_b', [9, 19, 29]), ts, f, now); assert.deepEqual(b.granted, [9, 19, 29]);
  assert.equal(T.purchases.filter(p => p.status === 'granted').length, 3);
});

test('a changed custom_data cannot open more than was paid for', async () => {
  const { T, f } = fake(); const now = Date.now(), ts = Math.floor(now / 1000);
  const cases = [['txn_x1', 'pri_c', [7, 17, 27]], ['txn_x2', 'pri_b', [7, 18, 29]], ['txn_x3', 'pri_unknown', [7]], ['txn_x4', 'pri_c', [10]]];
  for (const [id, price, stages] of cases) { const [s, b] = await post(txn(id, price, stages), ts, f, now); assert.equal(s, 200); assert.equal(b.ok, false, id); }
  const [, b] = await post(txn('txn_x5', 'pri_c', [7], { items: [{ price: { id: 'pri_c' }, quantity: 3 }] }), ts, f, now); assert.equal(b.review, 'quantity');
  assert.equal(T.calls.length, 0, 'nothing granted'); assert.ok(T.purchases.every(p => p.status === 'needs_review' && p.learner_id === null));
});

test('an approved refund closes the courses of that transaction; other events are ignored', async () => {
  const { T, f } = fake(); const now = Date.now(), ts = Math.floor(now / 1000);
  await post(txn('txn_r', 'pri_p', [7, 17]), ts, f, now);
  const pending = JSON.stringify({ event_type: 'adjustment.created', data: { action: 'refund', status: 'pending_approval', transaction_id: 'txn_r' } });
  assert.equal((await post(pending, ts, f, now))[1].ignored, 'adjustment.created');
  const done = JSON.stringify({ event_type: 'adjustment.updated', data: { action: 'refund', status: 'approved', transaction_id: 'txn_r' } });
  assert.equal((await post(done, ts, f, now))[1].refunded, 2);
  assert.ok(T.enrolments.every(e => e.status === 'refunded'));
  const sub = JSON.stringify({ event_type: 'subscription.created', data: {} });
  assert.equal((await post(sub, ts, f, now))[1].ignored, 'subscription.created');
});
