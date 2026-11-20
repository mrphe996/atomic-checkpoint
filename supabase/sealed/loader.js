// Loads the sealed answer keys at cold start: fetch ciphertext (commit-pinned) → AES-GCM decrypt with UNITS_KEY → gunzip.
const b64 = (s) => Uint8Array.from(atob(s.trim()), (c) => c.charCodeAt(0));
export async function loadUnits(url) {
  const k = Deno.env.get('UNITS_KEY'); if (!k) throw new Error('UNITS_KEY missing');
  const res = await fetch(url); if (!res.ok) throw new Error('sealed keys fetch ' + res.status);
  const raw = b64(await res.text());
  const key = await crypto.subtle.importKey('raw', b64(k), 'AES-GCM', false, ['decrypt']);
  const gz = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: raw.slice(0, 12) }, key, raw.slice(12));
  const txt = await new Response(new Blob([gz]).stream().pipeThrough(new DecompressionStream('gzip'))).text();
  return JSON.parse(txt);
}
