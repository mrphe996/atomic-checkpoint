// One Edge Function, three routes: /api/submit-test, /api/marking, /api/account  (+ /api/health self-check)
// Shared code is imported from the commit-pinned public repo; answer keys come from ./units.js locally, or are unsealed at cold start (sealed.js) when built with EDGE_SEALED=1.
import { handle as submitTest } from '__LIB__/submit-test.js';
import { handle as marking } from '__LIB__/marking.js';
import { handle as account } from '__LIB__/account.js';
import { G, setUnits } from '__LIB__/supa.js';
import { UNITS } from '__UNITS__';
setUnits(UNITS);

const ROUTES: Record<string, (req: unknown) => Promise<[number, unknown, Record<string, string>?]>> = { 'submit-test': submitTest, marking, account };
const ORIGINS = (Deno.env.get('ALLOWED_ORIGINS') || '*').split(',').map((s) => s.trim());

function cors(origin: string | null) {
  const allow = ORIGINS.includes('*') ? '*' : origin && ORIGINS.includes(origin) ? origin : ORIGINS[0];
  return { 'Access-Control-Allow-Origin': allow, 'Access-Control-Allow-Headers': 'authorization, content-type, apikey, x-client-info', 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', Vary: 'Origin' };
}

Deno.serve(async (req: Request) => {
  const h = cors(req.headers.get('origin'));
  if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: h });
  const url = new URL(req.url);
  const name = url.pathname.split('/').filter(Boolean).pop() || '';
  const route = ROUTES[name];
  if (name === 'health') return Response.json(await health(), { headers: h });
  if (!route) return Response.json({ error: 'not_found' }, { status: 404, headers: h });
  let body: unknown = {};
  if (req.method === 'POST') { try { body = await req.json(); } catch { body = {}; } }
  const r = { method: req.method, headers: { authorization: req.headers.get('authorization') || '' }, body, query: Object.fromEntries(url.searchParams) };
  try {
    const [status, out, extra] = await route(r);
    return new Response(JSON.stringify(out), { status, headers: { ...h, ...(extra || {}), 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' } });
  } catch (e) {
    console.error(e);
    const s = (e as { status?: number }).status;
    return Response.json({ error: 'server' }, { status: s && s < 500 ? s : 500, headers: h });
  }
});

// Deployment self-check: answer-key checksum + every paper marked with its own keys must score full automatic marks.
async function health() {
  const buf = new TextEncoder().encode(JSON.stringify(UNITS));
  const sha = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', buf))).map((b) => b.toString(16).padStart(2, '0')).join('');
  const papers: Record<string, unknown> = {};
  for (const [u, pack] of Object.entries(UNITS as Record<string, { papers: Record<string, any[]> }>)) for (const [f, paper] of Object.entries(pack.papers)) {
    const answers: Record<string, unknown> = {};
    for (const q of paper) answers[q.id] = right(q);
    const r = G.scoreTest(paper, answers);
    papers[u + ':' + f] = { auto: r.auto, pending: r.pending.length, expectedAuto: paper.filter((q) => !q.teacher).reduce((s, q) => s + q.pts, 0) };
  }
  return { ok: true, sha256: sha, papers };
}
// deno-lint-ignore no-explicit-any
function right(q: any): unknown {
  switch (q.type) {
    case 'mcq': return q.options.findIndex((o: any) => o.ok);
    case 'multi': return q.options.map((o: any, i: number) => (o.ok ? i : -1)).filter((i: number) => i >= 0);
    case 'num': case 'scale': return { v: String(q.answer), u: q.unit };
    case 'label': return { ...q.spots };
    case 'order': return q.items.slice();
    case 'match': return Object.fromEntries(q.pairs.map((p: any) => [p.l, p.r]));
    case 'explain': return q.model;
    case 'grid': return q.rows.map((r: any) => r.a.slice());
    case 'table': { const o: Record<string, Record<string, string>> = {}; q.rows.forEach((row: any[], ri: number) => row.forEach((c: any, ci: number) => { if (c && typeof c === 'object') (o[ri] = o[ri] || {})[ci] = String(c.ans); })); return o; }
    case 'graph': return { pts: q.pts.map((p: number[]) => p.slice()), f: q.follow ? q.follow.options.findIndex((o: any) => o.ok) : null };
  }
  return null;
}
