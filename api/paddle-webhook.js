// POST /api/paddle-webhook — Paddle Billing notifications (Paddle is merchant of record: it charges UK VAT / SEA GST/VAT).
// Courses are bought ONCE (one-time prices, no subscription):
//   PADDLE_PRICE_COURSE  one subject of a stage   (US$49)
//   PADDLE_PRICE_PAIR    two subjects of a stage  (US$95)
//   PADDLE_PRICE_BUNDLE  the whole stage          (US$119)
// The checkout sends custom_data { learner_id, stages: [..] }. The price decides HOW MANY courses were paid for, so a changed
// custom_data cannot buy more than was paid: a mismatch is stored as 'needs_review' and nothing is opened.
// transaction.completed → grant_purchase(); an approved refund (adjustment.*) → revoke_purchase().
// Signature: Paddle-Signature header "ts=…;h1=HMAC-SHA256(secret, ts + ':' + rawBody)". Web Crypto, so the same file runs on Node and Deno.
import { readRaw, db, env } from './_lib/supa.js';

const MAX_SKEW_S = 300;
const VALID = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29]);
export const coursesFor = () => ({ [env('PADDLE_PRICE_COURSE', 'pri_course')]: 1, [env('PADDLE_PRICE_PAIR', 'pri_pair')]: 2, [env('PADDLE_PRICE_BUNDLE', 'pri_bundle')]: 3 });

async function hmacHex(secret, data) {
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return Array.from(new Uint8Array(await crypto.subtle.sign('HMAC', key, enc.encode(data)))).map(b => b.toString(16).padStart(2, '0')).join('');
}
function sameText(a, b) { a = String(a); b = String(b); if (a.length !== b.length) return false; let d = 0; for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i); return d === 0; }

export async function verify(raw, header, secret, now = Date.now()) {
  const parts = Object.fromEntries(String(header || '').split(';').map(p => p.split('=')));
  if (!parts.ts || !parts.h1 || !secret) return false;
  if (Math.abs(now / 1000 - Number(parts.ts)) > MAX_SKEW_S) return false;
  return sameText(await hmacHex(secret, `${parts.ts}:${raw}`), parts.h1);
}

// which courses a paid transaction opens, or why it cannot be granted automatically
export function check(d) {
  const cd = d.custom_data || {};
  const learner = String(cd.learner_id || '');
  if (!/^[0-9a-f-]{36}$/i.test(learner)) return { error: 'no_learner' };
  const stages = Array.isArray(cd.stages) ? [...new Set(cd.stages.map(Number))] : [];
  const items = d.items || [];
  if (items.length !== 1) return { learner, stages, error: 'items' };
  const price = (items[0].price && items[0].price.id) || items[0].price_id;
  const n = coursesFor()[price];
  if (!n) return { learner, stages, price, error: 'unknown_price' };
  if (Number(items[0].quantity || 1) !== 1) return { learner, stages, price, error: 'quantity' };
  if (stages.length !== n || !stages.every(s => VALID.has(s)) || new Set(stages.map(s => s % 10)).size !== 1) return { learner, stages, price, error: 'stages_do_not_match_price' };
  return { learner, stages, price };
}

export async function handle(req, f = fetch, now = Date.now()) {
  if (req.method !== 'POST') return [405, { error: 'method' }];
  const raw = await readRaw(req);
  if (!(await verify(raw, req.headers['paddle-signature'], env('PADDLE_WEBHOOK_SECRET'), now))) return [401, { error: 'bad_signature' }];
  let evt; try { evt = JSON.parse(raw); } catch { return [400, { error: 'bad_json' }]; }
  const type = evt.event_type || '', d = evt.data || {}, stamp = new Date(now).toISOString();

  if (/^adjustment\./.test(type)) {   // refunds: Paddle approves them first, then we close the courses of that transaction
    if (d.action === 'refund' && d.status === 'approved' && d.transaction_id) {
      const n = await db('rpc/revoke_purchase', { method: 'POST', body: { p_txn: d.transaction_id } }, f);
      return [200, { ok: true, refunded: n }];
    }
    return [200, { ignored: type }];
  }
  if (type !== 'transaction.completed') return [200, { ignored: type }];

  const prev = await db(`purchases?provider_txn_id=eq.${encodeURIComponent(d.id)}&select=status`, {}, f);
  if (prev && prev.length) return [200, { ok: true, duplicate: true, status: prev[0].status }];   // Paddle retries: grant once
  const c = check(d);
  const totals = d.details && d.details.totals || {};
  const amount = totals.grand_total != null ? `${totals.grand_total} ${d.currency_code || ''}`.trim() : null;
  // a transaction that needs review keeps the claimed learner in the note only (it may not exist)
  const row = { provider_txn_id: d.id, learner_id: c.error ? null : c.learner, stages: c.stages || [], price_id: c.price || null,
    amount, currency: d.currency_code || null, status: c.error ? 'needs_review' : 'granted', note: c.error ? `${c.error}; learner ${c.learner || '-'}` : null, updated_at: stamp };
  if (c.error) { await db('purchases', { method: 'POST', body: row, prefer: 'resolution=ignore-duplicates' }, f); console.error('paddle: needs review', d.id, c.error); return [200, { ok: false, review: c.error }]; }
  await db('rpc/grant_purchase', { method: 'POST', body: { p_learner: c.learner, p_stages: c.stages, p_txn: d.id, p_amount: amount } }, f);
  await db('purchases', { method: 'POST', body: row, prefer: 'resolution=ignore-duplicates' }, f);
  return [200, { ok: true, granted: c.stages }];
}

export default async function handler(req, res) {
  const { send } = await import('./_lib/supa.js');
  try { const [s, b] = await handle(req); send(res, s, b); }
  catch (e) { console.error(e); send(res, 500, { error: 'server' }); }
}
