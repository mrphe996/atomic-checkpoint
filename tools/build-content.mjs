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
// the figure library, loaded the way the browser loads it, so every fig:{kind} in the content is checked
const FIGLIB = (() => { const win = {}; try { for (const f of ['web/figures.js', 'web/figures2.js', 'web/figures3.js', 'web/figures4.js']) { const p = path.join(ROOT, f); if (fs.existsSync(p)) new Function('window', fs.readFileSync(p, 'utf8'))(win); } } catch (e) { console.error('figure library:', e.message); } return win.AtomicFig; })();
const ANCHORS = { // label anchors each figure provides (keep in sync with web/figures.js)
  microscope: ['eyepiece', 'objective', 'stage', 'clips', 'diaphragm', 'light', 'coarse', 'fine', 'arm', 'base'],
  plantcell: ['wall', 'membrane', 'cytoplasm', 'nucleus', 'vacuole', 'chloroplast', 'mito'],
  animalcell: ['membrane', 'cytoplasm', 'nucleus', 'mito'], roothair: ['extension', 'nucleus', 'vacuole', 'wall'],
  neurone: ['body', 'fibre', 'endings', 'nucleus'], ciliated: ['mucus', 'cilia', 'nucleus'],
  palisade: ['wall', 'nucleus', 'chloroplast', 'vacuole'], plant: ['flower', 'leaf', 'stem', 'root'], body: ['brain', 'lungs', 'heart', 'stomach'] };
// figures4.js (and any later figure file) report their own anchors
for (const k of ['leafsection', 'stainsetup', 'rootpath', 'polyp']) { if (FIGLIB && FIGLIB.F[k]) ANCHORS[k] = Object.keys(FIGLIB.get(k, {}).a || {}); }
const TYPES = ['mcq', 'multi', 'num', 'scale', 'label', 'order', 'match', 'explain', 'grid', 'table', 'graph', 'sim', 'short', 'cloze', 'expr', 'say', 'para'];
const WRITTEN = q => q.type === 'explain' || q.type === 'para';

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
      case 'para': {
        if (!Array.isArray(q.rubric) || q.rubric.length < 2 || q.rubric.length > 8 || q.rubric.some(p => !p.pt || !Array.isArray(p.kw) || !p.kw.length)) errs.push(`${at}: para needs 2–8 mark-scheme points, each with a description and fallback key words`);
        if (!q.model) errs.push(`${at}: para needs a model answer`);
        if (!(q.need >= 1 && q.need <= (q.rubric || []).length)) errs.push(`${at}: para needs "need" (points for full marks)`);
        if (!Array.isArray(q.sentences) || !(q.sentences[0] >= 1)) errs.push(`${at}: para needs a sentence range [min, max]`);
        if (q.tier === 'ext' && !q.source) errs.push(`${at}: Extreme questions need a source ("Atomic original" or "Adapted from: …")`);
        if (!Array.isArray(q.partial) || q.partial.length < 2) warn.push(`${at}: para should carry 2+ part-mark examples`);
        (q.partial || []).forEach((x, i) => { const st = G.paraStats(x.text); if (st.sentences < q.sentences[0] || st.words < (q.minWords || 0)) errs.push(`${at}: part-mark example ${i + 1} is shorter than the length rule`); if (!(x.score >= 0 && x.score < q.rubric.length) || !x.why) errs.push(`${at}: part-mark example ${i + 1} needs a score below full marks and a reason`); });
        if (q.model) { const st = G.paraStats(q.model); if (st.sentences < q.sentences[0] || st.words < (q.minWords || 0)) errs.push(`${at}: the model answer is shorter than the length rule (${st.sentences} sentences, ${st.words} words)`); }
        break;
      }
      case 'grid': q.rows.forEach(r => { if (!r.a || !r.a.length) errs.push(`${at}: grid row without answer`); }); break;
      case 'table': if (!q.rows.some(r => r.some(c => c && typeof c === 'object'))) errs.push(`${at}: table has no blank`); break;
      case 'short': if (!Array.isArray(q.accept) || !q.accept.length || !G.answerText(q)) errs.push(`${at}: short answer needs accepted answers (the first plain one is the model)`); break;
      case 'say': if (!q.word || !q.audio) errs.push(`${at}: say needs the word and its audio`); break;
      case 'expr': if (!q.expr || !G.exprFn(q.expr)) errs.push(`${at}: expr needs a valid model expression`); break;
      case 'cloze': { const n = (String(q.text || '').match(/\{\d+\}/g) || []).length; if (!n || !Array.isArray(q.blanks) || q.blanks.length !== n || q.blanks.some(b => !b.length)) errs.push(`${at}: cloze needs one accepted-answer list per {n} gap`); break; }
    }
    if (q.fig && typeof q.fig === 'object' && FIGLIB) { const f = FIGLIB.F[q.fig.kind]; if (!f) errs.push(`${at}: unknown figure kind ${q.fig.kind}`); else { try { if (!FIGLIB.get(q.fig.kind, q.fig).svg) errs.push(`${at}: figure ${q.fig.kind} drew nothing`); } catch (e) { errs.push(`${at}: figure ${q.fig.kind} failed: ${e.message}`); } } }
    if (q.data && !(Array.isArray(q.data.head) && Array.isArray(q.data.rows) && q.data.rows.every(r => r.length === q.data.head.length))) errs.push(`${at}: data table rows must match its headings`);
    if (q.twin) checkQ(q.twin, at + ' twin');
    if (q.follow) checkQ(q.follow, at + ' follow-up');
  };
  for (const s of c.sections) {
    const ext = s.ext || [];
    const n = s.req.length + s.prac.length + s.adv.length;
    if (n < 30) errs.push(`section ${s.id}: ${n} questions (minimum 30)`);
    if (s.req.length !== 8) errs.push(`section ${s.id}: needs 8 Core questions (has ${s.req.length})`);
    const fig = s.req.filter(q => ['label', 'scale', 'grid', 'table', 'graph', 'sim'].includes(q.type) || q.skill === 'Data' || q.skill === 'Figure').length;
    if (c.unit && c.unit.primary) {
      // Primary: Core is the word check that unlocks the next lesson – listening and saying the key words
      if (s.req.filter(q => q.audio && q.type !== 'say').length < 3) errs.push(`section ${s.id}: Primary Core needs 3+ listening questions`);
      const more = s.prac.concat(s.adv); const fig2 = more.filter(q => ['label', 'scale', 'grid', 'table', 'graph', 'sim'].includes(q.type) || q.skill === 'Data' || q.skill === 'Figure').length;
      if (fig2 < 2) errs.push(`section ${s.id}: Practice needs 2+ diagram/data questions (has ${fig2})`);
      if (c.unit.young) {
        // Stages 3–4 (ages 7–9): they cannot type yet, so every answer is tapped; most questions have picture answers
        const TYPING = ['short', 'cloze', 'explain', 'para', 'num', 'expr', 'scale', 'table', 'graph', 'say'];
        const all = [...s.req, ...s.prac, ...s.adv, ...ext, ...(s.stops || []).flatMap(x => [x.q, x.twin]), ...((s.lab && s.lab.v && s.lab.v.qs) || []), ...((s.lab && s.lab.h && s.lab.h.qs) || [])];
        all.filter(q => q && TYPING.includes(q.type)).forEach(q => errs.push(`section ${s.id} ${q.id}: young learners cannot type – ${q.type} questions are not allowed`));
        const pics = all.filter(q => q && q.options && q.options.every(o => o.e)).length;
        if (pics < 15) errs.push(`section ${s.id}: young learners need 15+ picture-answer questions (has ${pics})`);
        if (!s.req.every(q => q.options && q.options.every(o => o.e))) errs.push(`section ${s.id}: every Core question must have picture answers`);
        if (s.lab && s.lab.v && s.lab.v.kind === 'test' && !s.lab.v.choose) errs.push(`section ${s.id}: the young-learner scale lab must use tap-to-choose readings`);
        if (s.lab && s.lab.h && s.lab.h.record && s.lab.h.record.rows.some(r => r.slice(1).some(c => !c.choices))) errs.push(`section ${s.id}: the home experiment results must be tapped, not typed`);
      } else {
        if (s.req.filter(q => q.type === 'say').length < 3) errs.push(`section ${s.id}: Primary Core needs 3+ say-the-word questions`);
        if (!more.some(WRITTEN)) errs.push(`section ${s.id}: Practice needs a written-reasoning question`);
      }
      if (!s.vocab || s.vocab.length < 4) errs.push(`section ${s.id}: Primary section needs a word bank (4+ words)`);
      if (!s.lab || !s.lab.v || !s.lab.h) errs.push(`section ${s.id}: Primary section needs an experiment room (virtual lab and home experiment)`);
      else [...(s.lab.v.qs || []), ...(s.lab.h.qs || [])].forEach(q => checkQ(q, `section ${s.id} lab`));
      if (s.lab && s.lab.v) { const V = s.lab.v;
        if (!['pulse', 'lungs', 'growth', 'germs', 'test', 'sort'].includes(V.kind)) errs.push(`section ${s.id}: unknown virtual lab kind ${V.kind}`);
        if (V.kind === 'test') (V.conds || []).forEach(c => { if (!(c.val >= 0 && c.val <= V.max)) errs.push(`section ${s.id} lab: ${c.t} value ${c.val} is off the scale (0–${V.max})`); if (Math.abs(c.val / V.step * 2 - Math.round(c.val / V.step * 2)) > 1e-9) errs.push(`section ${s.id} lab: ${c.t} value ${c.val} is not readable on a ${V.step} scale`); });
        if (V.kind === 'sort') (V.items || []).forEach(it => { if (!(it.g >= 0 && it.g < V.groups.length)) errs.push(`section ${s.id} lab: ${it.t} has no group`); }); }
    } else {
      if (fig < 2) errs.push(`section ${s.id}: Core needs 2+ diagram/data questions (has ${fig})`);
      if (!s.req.some(WRITTEN)) errs.push(`section ${s.id}: Core needs a written-reasoning question`);
      s.req.forEach(q => { if (!q.twin && q.type !== 'sim') warn.push(`section ${s.id} ${q.id}: Core question without a similar (twin) question`); });
    }
    s.adv.forEach(q => { if (!/^\* Advanced\./.test(q.prompt)) errs.push(`section ${s.id} ${q.id}: advanced prompt must start "* Advanced."`); });
    [...s.req, ...s.prac, ...s.adv].forEach(q => checkQ(q, `section ${s.id}`));
    ext.forEach(q => { checkQ({ ...q, tier: 'ext' }, `section ${s.id} extreme`); if (q.diff !== 'VH') errs.push(`section ${s.id} ${q.id}: Extreme questions are Very hard (VH)`); });
    if (ext.length && c.unit && !c.unit.young && c.unit.stage >= 5 && !ext.some(q => q.type === 'para')) errs.push(`section ${s.id}: Extreme needs a paragraph question from Stage 5`);
    (s.stops || []).forEach(st => { checkQ(st.q, `section ${s.id} stop`); if (!(st.t > 0 && st.t < s.video.dur)) errs.push(`section ${s.id} stop ${st.id}: time outside the clip`); });
  }
  for (const f of Object.keys(c.tests).filter(k => k.length === 1)) {
    const pts = c.tests[f].reduce((a, q) => a + q.pts, 0);
    if (c.unit && c.unit.young) c.tests[f].filter(q => ['short', 'cloze', 'explain', 'para', 'num', 'expr', 'scale', 'table', 'graph'].includes(q.type)).forEach(q => errs.push(`test ${f} ${q.id}: young learners cannot type – ${q.type} is not allowed`));
    if (pts !== 30) errs.push(`test ${f}: ${pts} marks (must be 30)`);
    if (!c.tests[f].some(q => ['label', 'grid', 'table', 'graph', 'scale'].includes(q.type) || q.fig || q.data)) errs.push(`test ${f}: needs a diagram or data question`);
    c.tests[f].forEach(q => checkQ(q, `test ${f}`));
    c.tests[f].filter(q => q.type === 'para' && !q.teacher).forEach(q => errs.push(`test ${f} ${q.id}: paragraph questions in a test must be teacher:true (the AI marks them first; unsure marks go to a teacher)`));
  }
  Object.entries(objs).forEach(([k, o]) => { if (!o.code) errs.push(`objective ${k}: curriculum code missing`); });
  return { errs, warn };
}

// estimated study time (minutes): videos + pause questions, 30 questions per section, a worksheet, the Unit Test
export function estimate(c) {
  const video = c.sections.reduce((a, x) => a + (x.video.dur || 0), 0) / 60;
  const pauses = c.sections.reduce((a, x) => a + x.stops.length, 0) * 1;
  const practice = c.sections.reduce((a, x) => a + (x.req.length + x.prac.length + x.adv.length) * 1.5, 0);
  const sheets = c.sections.length * 10;
  return Math.round(video + pauses + practice + sheets + 45);
}
// concept map laid out automatically from the unit's mind map (root in the middle, topics around it)
function autoMap(c) {
  const P = [[0, 1], [4, 1], [1, 2], [3, 2], [0, 3], [4, 3], [2, 3], [2, 2], [1, 4], [3, 4]];
  const kids = (c.mindmap.kids || []).slice(0, P.length);
  const nodes = [{ id: 'root', t: c.mindmap.t, s: c.sections[0].id, c: 2, r: 0, k: 'root' }].concat(kids.map((k, i) => ({ id: k.id, t: k.t, s: k.sec || c.sections[0].id, c: P[i][0], r: P[i][1], k: 'key', d: String(k.d || '').split('•').map(x => x.trim()).filter(Boolean).slice(0, 4) })));
  return { nodes, links: kids.map(k => ['root', k.id, '']) };
}
// end-of-year exams: papers only (no sections); same question rules, every paper worth c.max marks
export function validateFinal(c) {
  const errs = [], warn = [], ids = new Set();
  const fake = { objectives: c.objectives, sections: [], tests: {} };
  for (const [k, paper] of Object.entries(c.papers)) {
    const pts = paper.reduce((a, q) => a + q.pts, 0); if (pts !== c.max) errs.push(`paper ${k}: ${pts} marks (must be ${c.max})`);
    paper.forEach(q => { if (ids.has(q.id)) errs.push(`paper ${k} ${q.id}: duplicate id`); ids.add(q.id); });
    fake.tests['Z'] = paper; const r = validate({ ...fake, tests: { Z: paper.map(q => ({ ...q })) } });
    r.errs.filter(e => !/must be 30/.test(e)).forEach(e => errs.push(`paper ${k}: ${e}`));
  }
  const minPapers = c.kind === 'checkpoint' ? 2 : 10; if (Object.keys(c.papers).length < minPapers) errs.push(`needs at least ${minPapers} papers`);
  return { errs, warn };
}
function buildFinal(file, c, check) {
  const name = path.basename(file, '.json'); const { errs, warn } = validateFinal(c);
  if (!errs.length && !check) {
    const papers = Object.fromEntries(Object.entries(c.papers).map(([k, p]) => [k, p.map(G.stripKeys)]));
    const pub = { final: true, kind: c.kind || 'final', unit: c.unit, meta: c.meta || null, objectives: c.objectives, minutes: c.minutes, max: c.max, pass: c.pass, level: c.level, papers, build: { at: new Date().toISOString().slice(0, 10), unit: name } };
    fs.writeFileSync(path.join(ROOT, 'web/content', name + '.json'), JSON.stringify(pub));
    fs.writeFileSync(path.join(ROOT, 'server/private', name + '.tests.json'), JSON.stringify({ unit: name, final: true, kind: c.kind || 'final', max: c.max, pass: c.pass, level: c.level, minutes: c.minutes, papers: c.papers }));
    const demoDir = path.join(ROOT, 'web/content/demo');
    if (process.env.ATOMIC_MODE !== 'live') { fs.mkdirSync(demoDir, { recursive: true }); fs.writeFileSync(path.join(demoDir, name + '.tests.json'), JSON.stringify({ unit: name, final: true, kind: c.kind || 'final', max: c.max, pass: c.pass, level: c.level, minutes: c.minutes, papers: c.papers })); }
  }
  return { name, errs, warn };
}
export function build(file, { check = false } = {}) {
  const c = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (c.final) return buildFinal(file, c, check);
  const { errs, warn } = validate(c);
  const name = path.basename(file, '.json');
  if (!errs.length && !check) {
    const pub = JSON.parse(JSON.stringify(c));
    const papers = {}; for (const f of Object.keys(c.tests).filter(k => k.length === 1)) { papers[f] = c.tests[f].map(G.stripKeys); }
    pub.tests = { ...papers, pass: c.tests.pass };
    pub.build = { at: new Date().toISOString().slice(0, 10), unit: name };
    const cm = path.join(ROOT, 'content/authoring/cmaps.json'); const stg = Number((name.match(/^stage(\d+)/) || [0, 7])[1]); const un = stg === 7 ? String(Number(name.slice(-2))) : `${stg}-${Number(name.slice(-2))}`;
    if (fs.existsSync(cm)) { const maps = JSON.parse(fs.readFileSync(cm, 'utf8')); if (maps[un]) { const secIds = c.sections.map(x => x.id); maps[un].nodes.forEach(nd => { if (!secIds.includes(nd.s)) throw new Error(`${name}: concept map node ${nd.id} points to missing section ${nd.s}`); }); pub.cmap = maps[un]; } }
    if (!pub.cmap && c.mindmap) pub.cmap = autoMap(c);
    pub.est = estimate(c);
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
  if (!check) writeIndex();
  process.exit(bad ? 1 : 0);
}

// web/content/stage7.json – the stage's units; "ready" when a unit's content has been built
export function writeIndex() {
  const T = { 3: [['Plants Are Living Things', 'Biology'], ['Mixing Materials', 'Chemistry'], ['Light and Shadows', 'Physics'], ['Staying Alive', 'Biology'], ['Forces and Magnets', 'Physics'], ['The Earth and the Moon', 'Earth and Space']],
    4: [['Living Things', 'Biology'], ['Energy', 'Physics'], ['Materials', 'Chemistry'], ['Earth and Its Habitats', 'Earth and Space'], ['Light', 'Physics'], ['Electricity', 'Physics']],
    5: [['Life Cycles of Flowering Plants', 'Biology'], ['Sound', 'Physics'], ['States and Properties of Matter', 'Chemistry'], ['The Digestive System', 'Biology'], ['Forces and Magnetism', 'Physics'], ['Seasons and Adaptations', 'Earth and Space']],
    6: [['The Human Body', 'Biology'], ['Materials: Properties and Changes', 'Chemistry'], ['Rocks, the Rock Cycle and Soil', 'Earth and Space'], ['Food Chains and Food Webs', 'Biology'], ['Forces and Electricity', 'Physics'], ['Light and the Solar System', 'Physics']],
    7: [['Introducing Science', 'Enquiry'], ['Measurements', 'Enquiry'], ['Cells', 'Biology'], ['Classifying Living Things', 'Biology'], ['Food Chains and Food Webs', 'Biology'],
    ['Materials and Their Structure', 'Chemistry'], ['Properties of Materials', 'Chemistry'], ['Acids and Alkalis', 'Chemistry'], ['Chemical Reactions', 'Chemistry'], ['Forces', 'Physics'],
    ['Energy', 'Physics'], ['Electricity', 'Physics'], ['Earth Processes', 'Earth and Space'], ['Earth and Beyond', 'Earth and Space']],
    8: [['Diet and Growth', 'Biology'], ['Human Body Systems', 'Biology'], ['Ecosystems', 'Biology'], ['The Structure of an Atom', 'Chemistry'], ['Mixtures and Solubility', 'Chemistry'],
      ['Chemical Reactivity', 'Chemistry'], ['Exothermic and Endothermic Changes', 'Chemistry'], ['Forces and Motion', 'Physics'], ['Pressure and Diffusion', 'Physics'], ['Light', 'Physics'],
      ['Magnetism', 'Physics'], ['Renewable and Non-Renewable Energy Resources', 'Physics'], ['Weather and Climate', 'Earth and Space'], ['Planetary Systems', 'Earth and Space']],
    9: [['Photosynthesis and Transport in Plants', 'Biology'], ['Excretion', 'Biology'], ['Variation and Inheritance', 'Biology'], ['The Structure of the Atom and the Periodic Table', 'Chemistry'],
      ['Chemical Bonding and Structure of Materials', 'Chemistry'], ['Displacement Reactions', 'Chemistry'], ['Salts', 'Chemistry'], ['Rate of Reaction', 'Chemistry'], ['Density', 'Physics'],
      ['Transfer of Thermal Energy', 'Physics'], ['Sound', 'Physics'], ['Electrical Circuits', 'Physics'], ['Earth and Climate Change', 'Earth and Space'], ['Astronomy', 'Earth and Space']],
    // 19 = Mathematics Stage 9
    19: [['Number and Calculation', 'Number'], ['Expressions and Formulae', 'Algebra'], ['Decimals, Percentages and Rounding', 'Number'], ['Equations and Inequalities', 'Algebra'], ['Angles', 'Geometry'],
      ['Statistical Investigations', 'Statistics'], ['Shapes and Measurements', 'Geometry'], ['Fractions', 'Number'], ['Sequences and Functions', 'Algebra'], ['Graphs', 'Algebra'],
      ['Ratio and Proportion', 'Number'], ['Probability', 'Probability'], ['Position and Transformation', 'Geometry'], ['Volume, Surface Area and Symmetry', 'Geometry'], ['Interpreting and Discussing Results', 'Statistics']] };
  for (const [stage, list] of Object.entries(T)) {
    const units = list.map(([t, strand], i) => { const id = `stage${stage}-unit${String(i + 1).padStart(2, '0')}`; const f = path.join(ROOT, 'web/content', id + '.json');
      if (!fs.existsSync(f)) return { n: i + 1, id, t, strand, ready: false };
      const c = JSON.parse(fs.readFileSync(f, 'utf8'));
      return { n: i + 1, id, t, strand, ready: true, est: c.est || null, sections: c.sections.map(x => ({ id: x.id, t: x.title })), qs: c.sections.reduce((a, x) => a + x.req.length + x.prac.length + x.adv.length + (x.ext || []).length, 0) }; });
    const fin = path.join(ROOT, 'web/content', `stage${stage}-final.json`);
    const final = fs.existsSync(fin) ? (({ minutes, max, pass, level, papers }) => ({ id: `stage${stage}-final`, minutes, max, pass, level, papers: Object.keys(papers).length }))(JSON.parse(fs.readFileSync(fin, 'utf8'))) : null;
    const cpf = path.join(ROOT, 'web/content', `stage${stage}-cp.json`);
    const cp = fs.existsSync(cpf) ? (({ minutes, max, meta, unit }) => ({ id: `stage${stage}-cp`, minutes, max, syllabus: unit.syllabus, papers: Object.keys(meta || {}) }))(JSON.parse(fs.readFileSync(cpf, 'utf8'))) : null;
    const est = units.reduce((a, u) => a + (u.est || 0), 0) + (final ? final.minutes * 2 : 0);
    fs.writeFileSync(path.join(ROOT, 'web/content', `stage${stage}.json`), JSON.stringify({ stage: Number(stage), units, final, cp, est }));
  }
}
