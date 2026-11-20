/* Atomic — test rules shared by the server (api/) and the demo backend.
   - pass: score / 30 strictly above 70 % on the raw score (21/30 is not a pass)
   - weak objectives: below 70 % of the marks available for that objective
   - remediation: up to 3 Core/Practice questions per weak objective, wrong-before first
   - unlock check: every section video watched + every Core question done */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(require('./grade-core.js'));
  else root.TestRules = factory(root.GradeCore);
})(typeof self !== 'undefined' ? self : this, function (G) {
  const PASS = 0.7, MAX = 30;
  const isPass = (score, max = MAX) => score / max > PASS;

  function missingForTest(content, state) {
    const out = []; state = state || {}; const video = state.video || {}, items = state.items || {};
    for (const s of content.sections) {
      const vs = video[s.id] || {}; const stopsLeft = s.stops.filter(x => !((vs.stops || {})[x.id] || {}).done).length;
      if (!vs.completed || stopsLeft) out.push({ kind: 'video', sec: s.id });
      s.req.forEach((q, i) => { if (!(items[q.id] || {}).done) out.push({ kind: 'core', sec: s.id, idx: i, id: q.id }); });
    }
    return out;
  }

  function pickRemediation(content, weak, state) {
    const items = (state && state.items) || {}; const out = [];
    weak.forEach(o => {
      const pool = []; content.sections.forEach(s => s.req.concat(s.prac).forEach(q => { if (q.obj === o) pool.push(q); }));
      pool.sort((a, b) => ((items[b.id] || {}).everWrong ? 1 : 0) - ((items[a.id] || {}).everWrong ? 1 : 0));
      pool.slice(0, 3).forEach(q => out.push(q.id));
    });
    return out.slice(0, 9);
  }

  /* Complete an attempt once every mark is known. Mutates and returns a. */
  function finalize(a, paper, content, state) {
    if (a.pending.some(id => a.per[id].pts == null)) { a.status = 'pending'; a.score = null; return a; }
    a.score = Math.round(Object.values(a.per).reduce((s, p) => s + p.pts, 0) * 100) / 100;
    a.pct = a.score / MAX * 100; a.passed = isPass(a.score); a.status = 'final';
    a.byObj = {};
    paper.forEach(q => { const o = (a.byObj[q.obj] = a.byObj[q.obj] || { got: 0, max: 0 }); o.got += a.per[q.id].pts; o.max += q.pts; });
    a.weak = Object.keys(a.byObj).filter(k => a.byObj[k].got / a.byObj[k].max < PASS);
    if (!a.passed) {
      if (!a.weak.length) a.weak = Object.keys(a.byObj).sort((x, y) => a.byObj[x].got / a.byObj[x].max - a.byObj[y].got / a.byObj[y].max).slice(0, 2);
      a.remed = pickRemediation(content, a.weak, state);
    } else a.remed = [];
    return a;
  }

  /* Build a fresh attempt from answers (marks every automatic item). */
  function mark(paper, answers, meta) {
    const r = G.scoreTest(paper, answers);
    const a = Object.assign({ ts: Date.now(), answers: JSON.parse(JSON.stringify(answers)), per: r.per, auto: r.auto, pending: r.pending, status: r.pending.length ? 'pending' : 'final' }, meta);
    return a;
  }
  /* What the learner sees after submitting: correct answers + the reasoning, item by item. */
  function solutions(paper) { return Object.fromEntries(paper.map(q => [q.id, { answer: G.answerText(q), reason: q.reason || q.model || '' }])); }
  const nextForm = n => (n % 2 === 0 ? 'A' : 'B');

  return { PASS, MAX, isPass, missingForTest, pickRemediation, finalize, mark, solutions, nextForm };
});
