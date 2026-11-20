// Seal the test answer keys for the edge function: gzip + AES-256-GCM.
// Output: supabase/sealed/units.enc (ciphertext only – safe to commit). The key lives in content/private/edge-key.txt
// (git-ignored) and in the Supabase secret UNITS_KEY. Without the key the file is unreadable.
import fs from 'node:fs'; import zlib from 'node:zlib'; import { webcrypto as C } from 'node:crypto';
import { UNITS } from '../supabase/functions/api/units.js';
const kf = 'content/private/edge-key.txt';
if (!fs.existsSync(kf)) fs.writeFileSync(kf, Buffer.from(C.getRandomValues(new Uint8Array(32))).toString('base64') + '\n');
const raw = Buffer.from(fs.readFileSync(kf, 'utf8').trim(), 'base64');
const key = await C.subtle.importKey('raw', raw, 'AES-GCM', false, ['encrypt']);
const iv = C.getRandomValues(new Uint8Array(12));
const gz = zlib.gzipSync(JSON.stringify(UNITS), { level: 9 });
const ct = new Uint8Array(await C.subtle.encrypt({ name: 'AES-GCM', iv }, key, gz));
fs.mkdirSync('supabase/sealed', { recursive: true });
fs.writeFileSync('supabase/sealed/units.enc', Buffer.concat([Buffer.from(iv), Buffer.from(ct)]).toString('base64') + '\n');
console.log('sealed', Object.keys(UNITS).length, 'units,', ct.length, 'bytes');
