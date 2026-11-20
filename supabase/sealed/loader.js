// Loads the sealed answer keys at cold start: fetch ciphertext (commit-pinned) → AES-GCM decrypt → gunzip.
// The key comes from the UNITS_KEY secret or, if unset, from public.get_app_secret('units_key') (service role only).
const b64 = (s) => Uint8Array.from(atob(s.trim()), (c) => c.charCodeAt(0));
async function unitsKey() {
  const k = Deno.env.get('UNITS_KEY'); if (k) return k;
  const url = Deno.env.get('SUPABASE_URL'), sk = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY');
  const r = await fetch(`${url}/rest/v1/rpc/get_app_secret`, { method: 'POST', headers: { apikey: sk, Authorization: `Bearer ${sk}`, 'Content-Type': 'application/json' }, body: JSON.stringify({ p_name: 'units_key' }) });
  if (!r.ok) throw new Error('units key lookup ' + r.status);
  const v = await r.json(); if (!v) throw new Error('units key missing'); return v;
}
export async function loadUnits(url) {
  const res = await fetch(url); if (!res.ok) throw new Error('sealed keys fetch ' + res.status);
  const raw = b64(await res.text());
  const key = await crypto.subtle.importKey('raw', b64(await unitsKey()), 'AES-GCM', false, ['decrypt']);
  const gz = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: raw.slice(0, 12) }, key, raw.slice(12));
  const txt = await new Response(new Blob([gz]).stream().pipeThrough(new DecompressionStream('gzip'))).text();
  return JSON.parse(txt);
}
