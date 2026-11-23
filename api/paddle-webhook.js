// POST /api/paddle-webhook — Paddle Billing notifications (Paddle is merchant of record: it charges UK VAT / SEA GST/VAT).
// Verifies the Paddle-Signature header (ts=…;h1=HMAC-SHA256(secret, ts + ":" + rawBody)) and mirrors the subscription.
import { send, readRaw, db, env, hmac, safeEqual } from './_lib/supa.js';

const PLANS = () => ({ [env('PADDLE_PRICE_MONTHLY', 'pri_monthly')]: 'stage7_monthly', [env('PADDLE_PRICE_YEARLY', 'pri_yearly')]: 'stage7_yearly' });
const MAX_SKEW_S = 300;

export function verify(raw, header, secret, now = Date.now()) {
  const parts = Object.fromEntries(String(header || '').split(';').map(p => p.split('=')));
  if (!parts.ts || !parts.h1 || !secret) return false;
  if (Math.abs(now / 1000 - Number(parts.ts)) > MAX_SKEW_S) return false;
  return safeEqual(hmac(secret, `${parts.ts}:${raw}`), parts.h1);
}

export async function handle(req, f = fetch, now = Date.now()) {
  if (req.method !== 'POST') return [405, { error: 'method' }];
  const raw = await readRaw(req);
  if (!verify(raw, req.headers['paddle-signature'], env('PADDLE_WEBHOOK_SECRET'), now)) return [401, { error: 'bad_signature' }];
  const evt = JSON.parse(raw);
  if (!/^subscription\./.test(evt.event_type || '')) return [200, { ignored: evt.event_type }];
  const d = evt.data || {};
  const parentId = d.custom_data && d.custom_data.parent_id;
  if (!/^[0-9a-f-]{36}$/i.test(String(parentId))) return [200, { ignored: 'no_parent' }];
  const price = d.items && d.items[0] && d.items[0].price && d.items[0].price.id;
  const row = { parent_id: parentId, provider: 'paddle', provider_subscription_id: d.id, plan: PLANS()[price] || price || 'unknown',
    status: d.status, current_period_end: d.current_billing_period ? d.current_billing_period.ends_at : null, updated_at: new Date(now).toISOString() };
  await db('subscriptions?on_conflict=provider_subscription_id', { method: 'POST', prefer: 'resolution=merge-duplicates', body: row }, f);
  return [200, { ok: true, status: d.status }];
}

export default async function handler(req, res) {
  try { const [s, b] = await handle(req); send(res, s, b); }
  catch (e) { console.error(e); send(res, 500, { error: 'server' }); }
}
