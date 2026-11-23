// Test-phase sign-up (DIRECT_SIGNUP=on, the default). Generated with tools/build-edge.mjs from api/signup.js.
import { handle } from 'https://cdn.jsdelivr.net/gh/mrphe996/atomic-checkpoint@fac6b63827a9061ee02c820367672237df0c0f0b/supabase/functions/_shared/signup.js';
const H = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'authorization, content-type, apikey, x-client-info', 'Access-Control-Allow-Methods': 'POST, OPTIONS' };
Deno.serve(async (req: Request) => {
  if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: H });
  let body: unknown = {};
  if (req.method === 'POST') { try { body = await req.json(); } catch { body = {}; } }
  try {
    const [status, out] = await handle({ method: req.method, headers: {}, body });
    return new Response(JSON.stringify(out), { status, headers: { ...H, 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' } });
  } catch (e) { console.error(e); return new Response(JSON.stringify({ error: 'server' }), { status: 500, headers: H }); }
});
