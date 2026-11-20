// POST /api/signup { email, password, displayName, country }                        → parent account
//      /api/signup { role:'student', email, password, nickname, birthYear, country, parentEmail? } → student account + learner profile
// Test phase only (DIRECT_SIGNUP=on): creates an already-confirmed parent account, so no confirmation email is needed.
// Turn off (DIRECT_SIGNUP=off) once a real email sender is set up; the app then uses Supabase's normal sign-up.
import { send, readJson, env, db } from './mini.js';

const COUNTRIES = ['GB', 'SG', 'MY', 'TH', 'VN', 'ID', 'PH', 'XX'];
// Age below which a parent must consent, by country (UK GDPR/Children's code 13, SG PDPC 13, MY PDPA 18, TH PDPA 20, VN PDPL 16, ID PDP 18, PH DPA 18, otherwise 16)
export const CONSENT_AGE = { GB: 13, SG: 13, MY: 18, TH: 20, VN: 16, ID: 18, PH: 18, XX: 16 };
export const needsParent = (country, birthYear, now = new Date()) => (now.getFullYear() - birthYear - 1) < (CONSENT_AGE[country] || 16); // counts a child as the younger age if their birthday has not come yet
const CODE_ABC = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';
const inviteCode = () => Array.from(crypto.getRandomValues(new Uint8Array(8)), b => CODE_ABC[b % CODE_ABC.length]).join('');
export async function handle(req, f = fetch) {
  if (req.method !== 'POST') return [405, { error: 'method' }];
  if (env('DIRECT_SIGNUP', 'on') !== 'on') return [404, { error: 'not_found' }];
  const body = (await readJson(req)) || {};
  const { email, password, displayName, country } = body; const student = body.role === 'student';
  const e = String(email || '').trim().toLowerCase();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(e) || e.length > 200) return [400, { error: 'bad_email' }];
  if (typeof password !== 'string' || password.length < 8 || password.length > 72) return [400, { error: 'weak_password' }];
  const c = COUNTRIES.includes(country) ? country : 'XX';
  const nick = String(body.nickname || '').trim(); const by = Number(body.birthYear); const thisYear = new Date().getFullYear();
  if (student && (nick.length < 2 || nick.length > 24)) return [400, { error: 'bad_nickname' }];
  if (student && !(by >= 2005 && by <= thisYear - 5)) return [400, { error: 'bad_birth_year' }];
  const parentEmail = String(body.parentEmail || '').trim().toLowerCase().slice(0, 200) || null;
  const name = student ? nick : String(displayName || '').trim().slice(0, 80);
  const key = env('SUPABASE_SERVICE_ROLE_KEY');
  const r = await f(`${env('SUPABASE_URL')}/auth/v1/admin/users`, { method: 'POST', headers: { apikey: key, Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: e, password, email_confirm: true, user_metadata: { display_name: name, country: c, role: student ? 'student' : 'parent' } }) });
  const j = await r.json().catch(() => ({}));
  if (!r.ok) {
    const msg = String(j.msg || j.message || j.error_description || j.error || '');
    if (r.status === 422 || /already/i.test(msg)) return [409, { error: 'email_taken' }];
    if (/password/i.test(msg)) return [400, { error: 'weak_password' }];
    return [502, { error: 'signup_failed' }];
  }
  if (!student) return [201, { created: true, role: 'parent' }];
  const pending = needsParent(c, by);
  const row = { user_id: j.id, nickname: nick, birth_year: by, country: c, parent_email: parentEmail, consent_status: pending ? 'pending' : 'not_required', invite_code: pending ? inviteCode() : null };
  try { await db('learners', { method: 'POST', body: row, prefer: 'return=minimal' }, f); }
  catch (x) { row.invite_code = pending ? inviteCode() : null; await db('learners', { method: 'POST', body: row, prefer: 'return=minimal' }, f); } // invite code clash: try once more
  return [201, { created: true, role: 'student', consent: row.consent_status, inviteCode: row.invite_code }];
}

