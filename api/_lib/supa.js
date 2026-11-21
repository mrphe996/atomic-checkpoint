// Small, dependency-free helpers for Vercel functions talking to Supabase (REST + Auth) with the service role.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
export const G = require('../../shared/grade-core.js');
export const Rules = require('../../shared/test-rules.js');

export const env = (k, d) => (process.env[k] != null && process.env[k] !== '' ? process.env[k] : d);
// 'off' = test phase: every family gets the full course free. Turns on only when BILLING=paddle (or Paddle is configured).
export const billingOn = () => env('BILLING', env('PADDLE_API_KEY') ? 'paddle' : 'off') === 'paddle';
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..');
const UNIT_RE = /^stage(5|6|7|8|9|19)-(unit\d{2}|final|cp)$/;

export function send(res, status, body, headers = {}) {
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store');
  for (const [k, v] of Object.entries(headers)) res.setHeader(k, v);
  res.end(JSON.stringify(body));
}

export async function readJson(req) {
  if (req.body && typeof req.body === 'object' && !Buffer.isBuffer(req.body)) return req.body;
  const raw = await readRaw(req); if (!raw) return {};
  try { return JSON.parse(raw); } catch { return {}; }
}
export async function readRaw(req) {
  if (typeof req.body === 'string') return req.body;
  if (Buffer.isBuffer(req.body)) return req.body.toString('utf8');
  const chunks = []; for await (const c of req) chunks.push(typeof c === 'string' ? Buffer.from(c) : c);
  return Buffer.concat(chunks).toString('utf8');
}

/** The signed-in Supabase user behind the request's bearer token, or null. */
export async function getUser(req, f = fetch) {
  const token = String(req.headers.authorization || '').replace(/^Bearer\s+/i, '');
  if (!token) return null;
  const r = await f(`${env('SUPABASE_URL')}/auth/v1/user`, { headers: { apikey: env('SUPABASE_ANON_KEY'), Authorization: `Bearer ${token}` } });
  if (!r.ok) return null;
  return r.json();
}

/** PostgREST call with the service role (bypasses RLS: every handler checks ownership itself). */
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
  if (!UNIT_RE.test(unit)) throw Object.assign(new Error('unknown unit'), { status: 400 });
  const pub = JSON.parse(fs.readFileSync(path.join(ROOT, 'web/content', unit + '.json'), 'utf8'));
  const priv = JSON.parse(fs.readFileSync(path.join(ROOT, 'server/private', unit + '.tests.json'), 'utf8'));
  if (priv.final) return { final: true, max: priv.max, pass: priv.pass, level: priv.level, minutes: priv.minutes, content: null, papers: priv.papers };
  return { content: pub, papers: priv.papers };
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

export function hmac(secret, data) { return crypto.createHmac('sha256', secret).update(data).digest('hex'); }
export function safeEqual(a, b) { const x = Buffer.from(String(a)), y = Buffer.from(String(b)); return x.length === y.length && crypto.timingSafeEqual(x, y); }

/** Map a DB attempt row to the shape the web app uses. */
export function rowToAttempt(r) {
  return { id: r.id, n: r.n, form: r.form, ts: Date.parse(r.created_at), answers: r.answers, per: r.per, auto: Number(r.auto), pending: Object.keys(r.per).filter(k => r.per[k].teacher),
    status: r.status, score: r.score == null ? null : Number(r.score), pct: r.pct == null ? null : Number(r.pct), passed: r.passed, byObj: r.by_obj, weak: r.weak || [], remed: r.remed || [],
    duration: r.duration_s == null ? null : Number(r.duration_s), overtime: !!r.overtime, leaves: Number(r.leaves || 0), autoSubmitted: !!r.auto_submitted };
}

/** The unit or exam pack with the admin's changes applied (question edits, withdrawn questions = full marks).
    Overrides are cached for 20 s; if they cannot be read the built pack is used unchanged. */
const OV_CACHE = {};
export async function overridesFor(unit, f) {
  const c = OV_CACHE[unit]; if (c && Date.now() - c.at < 20000) return c.ov;
  let ov = {};
  try {
    const rows = await db(`question_overrides?unit=eq.${encodeURIComponent(unit)}&select=question_id,hidden,key_patch`, {}, f);
    for (const r of rows || []) ov[r.question_id] = { hidden: !!r.hidden, patch: r.key_patch || null };
  } catch (e) { ov = {}; }
  OV_CACHE[unit] = { at: Date.now(), ov }; return ov;
}
export function clearOverrides(unit) { if (unit) delete OV_CACHE[unit]; else for (const k of Object.keys(OV_CACHE)) delete OV_CACHE[k]; }
export async function loadPack(unit, f) {
  const base = loadUnit(unit);
  const ov = await overridesFor(unit, f);
  return Object.keys(ov).length ? G.applyOverrides(base, ov, { voidHidden: true }) : base;
}
