// Supabase Edge Function (Deno) version of api/_lib/supa.js – same exports, no Node APIs.
// SUPABASE_URL, SUPABASE_ANON_KEY and SUPABASE_SERVICE_ROLE_KEY are provided by Supabase automatically.
import './grade-core.js';
import './test-rules.js';

export const G = globalThis.GradeCore;
export const Rules = globalThis.TestRules;
export const env = (k, d) => { const v = Deno.env.get(k); return v != null && v !== '' ? v : d; };
export const billingOn = () => env('BILLING', env('PADDLE_API_KEY') ? 'paddle' : 'off') === 'paddle';
const UNIT_RE = /^stage[7-9]-(unit\d{2}|final)$/;
// answer keys are not in this shared (public) file: the deployed function passes them in with setUnits()
let UNITS = {};
export function setUnits(u) { UNITS = u; }

export function send() { throw new Error('not used in the edge runtime'); }
export async function readJson(req) { return req.body && typeof req.body === 'object' ? req.body : {}; }
export async function readRaw(req) { return typeof req.body === 'string' ? req.body : JSON.stringify(req.body || {}); }

export async function getUser(req, f = fetch) {
  const token = String(req.headers.authorization || '').replace(/^Bearer\s+/i, '');
  if (!token) return null;
  const r = await f(`${env('SUPABASE_URL')}/auth/v1/user`, { headers: { apikey: env('SUPABASE_ANON_KEY'), Authorization: `Bearer ${token}` } });
  if (!r.ok) return null;
  return r.json();
}
export async function db(p, { method = 'GET', body, prefer } = {}, f = fetch) {
  const key = env('SUPABASE_SERVICE_ROLE_KEY');
  const headers = { apikey: key, Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' };
  if (prefer) headers.Prefer = prefer;
  const r = await f(`${env('SUPABASE_URL')}/rest/v1/${p}`, { method, headers, body: body == null ? undefined : JSON.stringify(body) });
  const text = await r.text();
  if (!r.ok) { const e = new Error(`db ${method} ${p.split('?')[0]} → ${r.status}: ${text.slice(0, 200)}`); e.status = r.status; throw e; }
  return text ? JSON.parse(text) : null;
}
export function loadUnit(unit) {
  if (!UNIT_RE.test(unit) || !UNITS[unit]) throw Object.assign(new Error('unknown unit'), { status: 400 });
  return UNITS[unit];
}
export async function ownsLearner(userId, learnerId, f) {
  if (!/^[0-9a-f-]{36}$/i.test(String(learnerId))) return null;
  // the parent, or the student themself once parental consent is settled
  const rows = await db(`learners?id=eq.${learnerId}&or=(parent_id.eq.${userId},and(user_id.eq.${userId},consent_status.neq.pending))&select=id,nickname,stage`, {}, f);
  return rows && rows[0] ? rows[0] : null;
}
export async function role(userId, f) {
  const rows = await db(`profiles?id=eq.${userId}&select=role`, {}, f);
  return rows && rows[0] ? rows[0].role : null;
}
export function rowToAttempt(r) {
  return { id: r.id, n: r.n, form: r.form, ts: Date.parse(r.created_at), answers: r.answers, per: r.per, auto: Number(r.auto), pending: Object.keys(r.per).filter(k => r.per[k].teacher),
    status: r.status, score: r.score == null ? null : Number(r.score), pct: r.pct == null ? null : Number(r.pct), passed: r.passed, byObj: r.by_obj, weak: r.weak || [], remed: r.remed || [],
    duration: r.duration_s == null ? null : Number(r.duration_s), overtime: !!r.overtime };
}
