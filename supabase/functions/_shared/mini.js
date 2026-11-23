// Minimal Deno helpers for the sign-up function (no answer keys bundled here).
export const env = (k, d) => { const v = Deno.env.get(k); return v != null && v !== '' ? v : d; };
export function send() { throw new Error('not used in the edge runtime'); }
export async function readJson(req) { return req.body && typeof req.body === 'object' ? req.body : {}; }
export async function db(p, { method = 'GET', body, prefer } = {}, f = fetch) {
  const key = env('SUPABASE_SERVICE_ROLE_KEY');
  const headers = { apikey: key, Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' };
  if (prefer) headers.Prefer = prefer;
  const r = await f(`${env('SUPABASE_URL')}/rest/v1/${p}`, { method, headers, body: body == null ? undefined : JSON.stringify(body) });
  const text = await r.text();
  if (!r.ok) { const e = new Error(`db ${method} ${p.split('?')[0]} → ${r.status}: ${text.slice(0, 200)}`); e.status = r.status; throw e; }
  return text ? JSON.parse(text) : null;
}
