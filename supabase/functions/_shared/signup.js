// POST /api/signup  – a student creates their own account (test phase: no confirmation email needed)
// { name, email, password, birthYear, grade, country, schoolId? | schoolOther?, parentEmail? }
// Creates the login (already confirmed) and the student's learner profile. A parent's email is optional:
// if given, the parent gets an email each time the student finishes a unit.
// Turn off with DIRECT_SIGNUP=off once a real email sender is set up.
import { send, readJson, env, db } from './mini.js';

const COUNTRIES = ['GB', 'SG', 'MY', 'TH', 'VN', 'ID', 'PH', 'XX'];
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export async function handle(req, f = fetch) {
  if (req.method !== 'POST') return [405, { error: 'method' }];
  if (env('DIRECT_SIGNUP', 'on') !== 'on') return [404, { error: 'not_found' }];
  const b = (await readJson(req)) || {};
  const e = String(b.email || '').trim().toLowerCase();
  if (!EMAIL.test(e) || e.length > 200) return [400, { error: 'bad_email' }];
  const password = b.password;
  if (typeof password !== 'string' || password.length < 8 || password.length > 72) return [400, { error: 'weak_password' }];
  const name = String(b.name || '').trim().replace(/\s+/g, ' ');
  if (name.length < 2 || name.length > 80) return [400, { error: 'bad_name' }];
  const thisYear = new Date().getFullYear(); const by = Number(b.birthYear);
  if (!(by >= 2005 && by <= thisYear - 5)) return [400, { error: 'bad_birth_year' }];
  const grade = String(b.grade || '').trim().slice(0, 40) || null;
  const country = COUNTRIES.includes(b.country) ? b.country : 'XX';
  const schoolId = Number.isInteger(Number(b.schoolId)) && Number(b.schoolId) > 0 ? Number(b.schoolId) : null;
  const schoolOther = schoolId ? null : String(b.schoolOther || '').trim().slice(0, 120) || null;
  const parentEmail = String(b.parentEmail || '').trim().toLowerCase();
  if (parentEmail && (!EMAIL.test(parentEmail) || parentEmail.length > 200)) return [400, { error: 'bad_parent_email' }];
  if (parentEmail && parentEmail === e) return [400, { error: 'parent_email_same' }];
  const nickname = name.split(' ')[0].slice(0, 24).padEnd(2, '.');

  const key = env('SUPABASE_SERVICE_ROLE_KEY');
  const r = await f(`${env('SUPABASE_URL')}/auth/v1/admin/users`, { method: 'POST', headers: { apikey: key, Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: e, password, email_confirm: true, user_metadata: { display_name: name, country, role: 'student' } }) });
  const j = await r.json().catch(() => ({}));
  if (!r.ok) {
    const msg = String(j.msg || j.message || j.error_description || j.error || '');
    if (r.status === 422 || /already/i.test(msg)) return [409, { error: 'email_taken' }];
    if (/password/i.test(msg)) return [400, { error: 'weak_password' }];
    return [502, { error: 'signup_failed' }];
  }
  await db('learners', { method: 'POST', prefer: 'return=minimal', body: {
    user_id: j.id, nickname, certificate_name: name, birth_year: by, grade, country, school_id: schoolId, school_other: schoolOther,
    parent_email: parentEmail || null, consent_status: 'not_required' } }, f);
  await db('consents', { method: 'POST', prefer: 'return=minimal', body: [{ parent_id: j.id, kind: 'terms', version: 'signup' }, { parent_id: j.id, kind: 'privacy', version: 'signup' }] }, f);
  return [201, { created: true }];
}

