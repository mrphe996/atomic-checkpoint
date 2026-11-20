#!/usr/bin/env node
/* Atomic content build.
   content/src/<unit>.json  (authoring source, full keys)
     → web/content/<unit>.json            public: practice + pause questions (keys kept for instant feedback),
                                           Unit Test papers WITHOUT keys
     → server/private/<unit>.tests.json   test papers WITH keys (read only by api/submit-test.js)
   Also validates the Atomic content rules; exits 1 on any error.
   Usage: node tools/build-content.mjs [--check]                                   */
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const G = require('../shared/grade-core.js');
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SRC = path.join(ROOT, 'content/src');
const ANCHORS = { // label anchors each figure provides (keep in sync with web/figures.js)
  microscope: ['eyepiece', 'objective', 'stage', 'clips', 'diaphragm', 'light', 'coarse', 'fine', 'arm', 'base'],
  plantcell: ['wall', 'membrane', 'cytoplasm', 'nucleus', 'vacuole', 'chloroplast', 'mito'],
  animalcell: ['membrane', 'cytoplasm', 'nucleus', 'mito'], roothair: ['extension', 'nucleus', 'vacuole', 'wall'],
  neurone: ['body', 'fibre', 'endings', 'nucleus'], ciliated: ['mucus', 'cilia', 'nucleus'],
  palisade: ['wall', 'nucleus', 'chloroplast', 'vacuole'], plant: ['flower', 'leaf', 'stem', 'root'], body: ['brain', 'lungs', 'heart', 'stomach'] };
const TYPES = ['mcq', 'multi', 'num', 'scale', 'label', 'order', 'match', 'explain', 'grid', 'table', 'graph', 'sim'];

export function validate(c) {
  const errs = [], warn = [];
  const ids = new Set();
  const objs = c.objectives || {};
  const checkQ = (q, where) => {
    const at = `${where} ${q.id}`;
    if (!q.id) errs.push(`${where}: question without id`);
    if (ids.has(q.id)) errs.push(`${at}: duplicate id`); ids.add(q.id);
    if (!TYPES.includes(q.type)) errs.push(`${at}: unknown type ${q.type}`);
    if (!objs[q.obj]) errs.push(`${at}: objective ${q.obj} not defined`);
    if (!['M', 'H', 'VH'].includes(q.diff)) errs.push(`${at}: difficulty must be M, H or VH (medium to very hard)`);
    if (!q.prompt || q.prompt.length < 8) errs.push(`${at}: prompt missing`);
    if (/[ăâđêôơưạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]/.test(JSON.stringify(q))) errs.push(`${at}: non-English text`);
    if (/Learner's Book|Workbook|LET'S MAP IT|\bp\.\s?\d/.test(JSON.stringify(q))) errs.push(`${at}: textbook reference`);
    switch (q.type) {
      case 'mcq': if (q.options.filter(o => o.ok).length !== 1) errs.push(`${at}: mcq needs exactly one correct option`);
        q.options.filter(o => !o.ok && !o.fb).forEach(() => warn.push(`${at}: wrong option without misconception feedback`)); break;
      case 'multi': if (!q.options.some(o => o.ok)) errs.push(`${at}: multi needs at least one correct option`); break;
      case 'num': case 'scale': if (!q.units.includes(q.unit)) errs.push(`${at}: unit not in unit list`); if (typeof q.answer !== 'number') errs.push(`${at}: numeric answer missing`); break;
      case 'label': { const a = ANCHORS[q.fig] || []; Object.keys(q.spots).forEach(k => { if (!a.includes(k)) errs.push(`${at}: figure ${q.fig} has no anchor "${k}"`); }); break; }
      case 'order': if (!q.items || q.items.length < 3) errs.push(`${at}: order needs 3+ items`); break;
      case 'match': if (!q.pairs || q.pairs.length < 2) errs.push(`${at}: match needs 2+ pairs`); break;
      case 'explain': if (!q.rubric || !q.model) errs.push(`${at}: explain needs a mark scheme and a model answer`); break;
      case 'grid': q.rows.forEach(r => { if (!r.a || !r.a.length) errs.push(`${at}: grid row without answer`); }); break;
      case 'table': if (!q.rows.some(r => r.some(c => c && typeof c === 'object'))) errs.push(`${at}: table has no blank`); break;
    }
    if (q.twin) checkQ(q.twin, at + ' twin');
    if (q.follow) checkQ(q.follow, at + ' follow-up');
  };
  for (const s of c.sections) {
    const n = s.req.length + s.prac.length + s.adv.length;
    if (n < 30) errs.push(`section ${s.id}: ${n} questions (minimum 30)`);
    if (s.req.length !== 8) errs.push(`section ${s.id}: needs 8 Core questions (has ${s.req.length})`);
    const fig = s.req.filter(q => ['label', 'scale', 'grid', 'table', 'graph', 'sim'].includes(q.type) || q.skill === 'Data' || q.skill === 'Figure').length;
    if (fig < 2) errs.push(`section ${s.id}: Core needs 2+ diagram/data questions (has ${fig})`);
    if (!s.req.some(q => q.type === 'explain')) errs.push(`section ${s.id}: Core needs a written-reasoning question`);
    s.req.forEach(q => { if (!q.twin && q.type !== 'sim') warn.push(`section ${s.id} ${q.id}: Core question without a similar (twin) question`); });
    s.adv.forEach(q => { if (!/^\* Advanced\./.test(q.prompt)) errs.push(`section ${s.id} ${q.id}: advanced prompt must start "* Advanced."`); });
    [...s.req, ...s.prac, ...s.adv].forEach(q => checkQ(q, `section ${s.id}`));
    (s.stops || []).forEach(st => { checkQ(st.q, `section ${s.id} stop`); if (!(st.t > 0 && st.t < s.video.dur)) errs.push(`section ${s.id} stop ${st.id}: time outside the clip`); });
  }
  for (const f of Object.keys(c.tests).filter(k => k.length === 1)) {
    const pts = c.tests[f].reduce((a, q) => a + q.pts, 0);
    if (pts !== 30) errs.push(`test ${f}: ${pts} marks (must be 30)`);
    if (!c.tests[f].some(q => ['label', 'grid', 'table', 'graph', 'scale'].includes(q.type))) errs.push(`test ${f}: needs a diagram or data question`);
    c.tests[f].forEach(q => checkQ(q, `test ${f}`));
  }
  Object.entries(objs).forEach(([k, o]) => { if (!o.code) errs.push(`objective ${k}: curriculum code missing`); });
  return { errs, warn };
}

export function build(file, { check = false } = {}) {
  const c = JSON.parse(fs.readFileSync(file, 'utf8'));
  const { errs, warn } = validate(c);
  const name = path.basename(file, '.json');
  if (!errs.length && !check) {
    const pub = JSON.parse(JSON.stringify(c));
    const papers = {}; for (const f of Object.keys(c.tests).filter(k => k.length === 1)) { papers[f] = c.tests[f].map(G.stripKeys); }
    pub.tests = { ...papers, pass: c.tests.pass };
    pub.build = { at: new Date().toISOString().slice(0, 10), unit: name };
    fs.mkdirSync(path.join(ROOT, 'web/content'), { recursive: true });
    fs.mkdirSync(path.join(ROOT, 'server/private'), { recursive: true });
    fs.writeFileSync(path.join(ROOT, 'web/content', name + '.json'), JSON.stringify(pub));
    fs.writeFileSync(path.join(ROOT, 'server/private', name + '.tests.json'), JSON.stringify({ unit: name, pass: c.tests.pass, papers: Object.fromEntries(Object.keys(papers).map(f => [f, c.tests[f]])) }));
    // demo bundle: keys included so the preview can mark tests without a server. Never shipped in live mode.
    const demoDir = path.join(ROOT, 'web/content/demo');
    if (process.env.ATOMIC_MODE === 'live') fs.rmSync(demoDir, { recursive: true, force: true });
    else {
      fs.mkdirSync(demoDir, { recursive: true });
      fs.writeFileSync(path.join(demoDir, name + '.tests.json'), JSON.stringify({ unit: name, papers: Object.fromEntries(Object.keys(papers).map(f => [f, c.tests[f]])) }));
    }
  }
  if (!check) { // the browser uses the same marking/test rules as the server
    const out = path.join(ROOT, 'web/shared'); fs.mkdirSync(out, { recursive: true });
    for (const f of ['grade-core.js', 'test-rules.js']) fs.copyFileSync(path.join(ROOT, 'shared', f), path.join(out, f));
  }
  return { name, errs, warn };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const check = process.argv.includes('--check'); let bad = 0;
  for (const f of fs.readdirSync(SRC).filter(f => f.endsWith('.json'))) {
    const r = build(path.join(SRC, f), { check });
    console.log(`${r.name}: ${r.errs.length} error(s), ${r.warn.length} warning(s)`);
    r.errs.forEach(e => console.log('  ERROR ' + e)); r.warn.slice(0, 20).forEach(w => console.log('  warn  ' + w));
    bad += r.errs.length;
  }
  process.exit(bad ? 1 : 0);
}
