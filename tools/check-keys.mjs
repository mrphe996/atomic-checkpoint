#!/usr/bin/env node
// Marks every paper's own model answers with the shared marker: each paper must score full marks.
// Catches mark-scheme keywords that miss the model answer, typed answers whose model is not accepted, etc.
import fs from 'node:fs'; import path from 'node:path'; import { createRequire } from 'node:module';
const require = createRequire(import.meta.url); const G = require('../shared/grade-core.js');
const dir = path.join(path.dirname(new URL(import.meta.url).pathname), '..', 'server/private');
const right = q => { switch (q.type) {
  case 'mcq': return q.options.findIndex(o => o.ok); case 'multi': return q.options.map((o, i) => o.ok ? i : -1).filter(i => i >= 0);
  case 'num': case 'scale': return { v: String(q.answer), u: q.unit }; case 'label': return { ...q.spots }; case 'order': return q.items.slice();
  case 'match': return Object.fromEntries(q.pairs.map(p => [p.l, p.r])); case 'explain': return q.model; case 'grid': return q.rows.map(r => r.a.slice());
  case 'table': { const o = {}; q.rows.forEach((row, ri) => row.forEach((c, ci) => { if (c && typeof c === 'object') (o[ri] = o[ri] || {})[ci] = String(c.ans); })); return o; }
  case 'short': return G.answerText(q); case 'cloze': return q.blanks.map(b => b.find(a => !(a[0] === '/' && a.lastIndexOf('/') > 0)) || '');
  case 'graph': return { pts: (q.plot || q.pts).map(p => p.slice()), f: q.follow ? q.follow.options.findIndex(o => o.ok) : null }; } return null; };
let bad = 0, n = 0;
for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.tests.json'))) {
  const pack = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
  for (const [k, paper] of Object.entries(pack.papers)) { n++;
    const ans = Object.fromEntries(paper.map(q => [q.id, right(q)])); const r = G.scoreTest(paper, ans);
    const want = paper.filter(q => !q.teacher).reduce((a, q) => a + q.pts, 0);
    if (Math.abs(r.auto - want) > 1e-6) { bad++; const miss = paper.filter(q => r.per[q.id] && r.per[q.id].pts < q.pts).map(q => `${q.id} ${r.per[q.id].pts}/${q.pts}`); console.log(`✗ ${f.replace('.tests.json', '')} ${k}: ${r.auto}/${want}  ${miss.join(', ')}`); } }
}
console.log(`${n} papers checked, ${bad} with model answers below full marks`);
// practice questions in every unit: each must be marked correct when given its own model answer
const src = path.join(path.dirname(new URL(import.meta.url).pathname), '..', 'content/src'); let pb = 0, pn = 0;
if (fs.existsSync(src)) for (const f of fs.readdirSync(src).filter(f => /unit\d+\.json$/.test(f))) {
  const d = JSON.parse(fs.readFileSync(path.join(src, f), 'utf8'));
  for (const s of d.sections) for (const q of [...s.req, ...s.prac, ...s.adv]) { if (q.type === 'sim') continue; pn++;
    const r = G.grade(q, right(q)); if (!r.ok) { pb++; console.log(`✗ ${f.replace('.json', '')} ${q.id} (${q.type}) ${r.detail || ''}`); } } }
console.log(`${pn} practice questions checked, ${pb} not marked correct with their model answer`);
process.exit(bad || pb ? 1 : 0);
