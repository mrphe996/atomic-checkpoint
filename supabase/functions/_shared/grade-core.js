/* Atomic — shared grading core (browser + Node). One source of truth for marking.
   Used by: web/qengine.js (practice feedback, demo mode), api/submit-test.js (server-side marking),
   tools/build-content.mjs (strips answer keys from the public content). */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.GradeCore = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  const SCOPE_COUNT = { 4: 12, 10: 5, 40: 1.25 };
  function rng(seedStr) { let h = 2166136261; for (const ch of seedStr) { h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619); } return () => { h ^= h << 13; h ^= h >>> 17; h ^= h << 5; return ((h >>> 0) % 100000) / 100000; }; }
  function shuffle(arr, seed) { const r = rng(seed), a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  const TYPE_VI = { mcq: 'Diagnostic multiple choice', multi: 'Select all that apply', num: 'Calculation', scale: 'Instrument reading', label: 'Label the diagram', order: 'Put in order', match: 'Matching', explain: 'Explain (mark scheme)', grid: 'Classification table', table: 'Data table', graph: 'Plot & read a graph', sim: 'Virtual experiment', short: 'Short answer (typed)', expr: 'Algebra (typed)', cloze: 'Complete the sentences (typed)' };
  const DIFF = { M: 'Medium', H: 'Hard', VH: 'Very hard' };
  const near = (a, b, tol) => Math.abs(a - b) <= Math.max(tol || 0, 1e-9 * Math.max(1, Math.abs(b)));
  // numbers: plain, decimal comma, fractions (3/4, -1 2/3), standard form (3.2 × 10^5, 3.2e5, 3.2×10⁵), and "x = 4" answers
  const SUP = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-' };
  const parseNum = s => { if (s == null) return null;
    let t = String(s).replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+/g, m => '^' + m.split('').map(c => SUP[c]).join('')).replace(/[−–]/g, '-').trim().replace(/^[a-z]\s*=\s*/i, '');
    let m = t.match(/^(-?\d+(?:[.,]\d+)?)\s*(?:[×x*]|\\times)\s*10\s*\^\s*\(?\s*(-?\d+)\s*\)?$/i); if (m) return Number(m[1].replace(',', '.')) * Math.pow(10, Number(m[2]));
    m = t.match(/^(-?)(?:(\d+)\s+)?(\d+)\s*\/\s*(\d+)$/); if (m) { const v = (m[2] ? Number(m[2]) : 0) + Number(m[3]) / Number(m[4]); return Number(m[4]) ? (m[1] ? -v : v) : null; }
    t = t.replace(/[×x,\s]/gi, c => c === ',' ? '.' : ''); if (t === '') return null; const v = Number(t); return isFinite(v) ? v : null; };
  /* algebra: a small, safe expression evaluator used to mark typed expressions by value.
     Supports numbers, single-letter variables, + − × ÷ * / ^ ² ³, brackets, implicit multiplication (2x, 3(x+1), (a+b)(a−b)) and √. */
  function exprFn(src) {
    let s = String(src == null ? '' : src).toLowerCase().replace(/[−–]/g, '-').replace(/[×·]/g, '*').replace(/÷/g, '/').replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+/g, m => '^(' + m.split('').map(c => SUP[c]).join('') + ')').replace(/\s+/g, '').replace(/\*\*/g, '^');
    if (!s || /[^0-9a-z.+\-*/^()√]/.test(s)) return null;
    const tk = []; for (let i = 0; i < s.length;) { const c = s[i];
      if (/[0-9.]/.test(c)) { let j = i; while (j < s.length && /[0-9.]/.test(s[j])) j++; tk.push({ n: Number(s.slice(i, j)) }); i = j; }
      else if (/[a-z]/.test(c)) { tk.push({ v: c }); i++; } else { tk.push({ o: c }); i++; } }
    if (tk.some(t => t.n != null && !isFinite(t.n))) return null;
    // implicit multiplication between value-ending and value-starting tokens
    const T = []; tk.forEach((t, i) => { const p = T[T.length - 1]; const pEnd = p && (p.n != null || p.v || p.o === ')'); const tStart = t.n != null || t.v || t.o === '(' || t.o === '√'; if (pEnd && tStart) T.push({ o: '*' }); T.push(t); });
    let k = 0; const peek = () => T[k], eat = o => (T[k] && T[k].o === o ? (k++, true) : false);
    function E() { let f = Tm(); for (;;) { if (eat('+')) { const a = f, b = Tm(); f = x => a(x) + b(x); } else if (eat('-')) { const a = f, b = Tm(); f = x => a(x) - b(x); } else return f; } }
    function Tm() { let f = U(); for (;;) { if (eat('*')) { const a = f, b = U(); f = x => a(x) * b(x); } else if (eat('/')) { const a = f, b = U(); f = x => a(x) / b(x); } else return f; } }
    function U() { if (eat('-')) { const a = U(); return x => -a(x); } if (eat('+')) return U(); return P(); }
    function P() { const b = A(); if (eat('^')) { const e = U(); return x => Math.pow(b(x), e(x)); } return b; }
    function A() { const t = peek(); if (!t) throw 0; k++;
      if (t.n != null) return () => t.n; if (t.v) return x => (t.v in x ? x[t.v] : NaN);
      if (t.o === '(') { const f = E(); if (!eat(')')) throw 0; return f; }
      if (t.o === '√') { const a = A(); return x => Math.sqrt(a(x)); } throw 0; }
    try { const f = E(); if (k !== T.length) return null; return f; } catch (e) { return null; }
  }
  const PTS = [[1.37, -0.62, 2.11], [-2.3, 1.9, 0.47], [0.83, 3.1, -1.4], [2.6, -1.15, 1.72], [-0.71, 0.58, -2.9]];
  function exprSame(a, b, vars) {
    const fa = exprFn(a), fb = exprFn(b); if (!fa || !fb) return false; const vs = Array.from(new Set((vars || 'xyz').toLowerCase().split('')));
    let tried = 0; for (const p of PTS) { const sc = {}; vs.forEach((v, i) => sc[v] = p[i % 3] + i * 0.31); const u = fa(sc), w = fb(sc); if (!isFinite(u) || !isFinite(w)) continue; tried++; if (Math.abs(u - w) > 1e-6 * Math.max(1, Math.abs(w))) return false; }
    return tried >= 3;
  }
  const exprClean = (raw, lhs) => { let t = String(raw || '').trim(); if (lhs) t = t.replace(new RegExp('^\\s*' + lhs + '\\s*=\\s*', 'i'), ''); return t; };
  const LEN = { 'µm': 0.001, 'mm': 1, 'cm': 10 };

  /* typed answers: case, spaces, punctuation and a leading "the/a/an" are ignored; a small spelling slip is accepted
     (1 letter in words of 5+ letters, 2 in words of 9+). Accepted answers starting and ending with "/" are regular expressions. */
  const normText = s => String(s == null ? '' : s).toLowerCase().replace(/[‘’`]/g, "'").replace(/[“”]/g, '"').replace(/₂/g, '2').replace(/₃/g, '3').replace(/₄/g, '4')
    .replace(/[^a-z0-9+\-./'%° ]+/g, ' ').replace(/\s+/g, ' ').trim().replace(/^(the|a|an) /, '').replace(/[.]+$/, '');
  function lev(a, b) { // edit distance; swapping two neighbouring letters counts as one slip
    if (a === b) return 0; const m = a.length, n = b.length; if (!m || !n) return m || n; const d = Array.from({ length: m + 1 }, (_, i) => [i]);
    for (let j = 1; j <= n; j++) d[0][j] = j;
    for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++) { d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1); }
    return d[m][n]; }
  function typedOk(raw, accept) {
    const t = normText(raw); if (!t) return false;
    return (accept || []).some(a => { a = String(a);
      if (a.length > 2 && a[0] === '/' && a.lastIndexOf('/') > 0) { const k = a.lastIndexOf('/'); try { return new RegExp(a.slice(1, k), a.slice(k + 1) || 'i').test(String(raw)); } catch (e) { return false; } }
      const w = normText(a); if (t === w) return true; if (/\d/.test(w)) return false; const tol = w.length >= 9 ? 2 : w.length >= 5 ? 1 : 0; return tol > 0 && lev(t, w) <= tol; });
  }
  const plainOf = list => (list || []).find(a => !(String(a)[0] === '/' && String(a).lastIndexOf('/') > 0)) || '';

  /* ---------------- grading ---------------- */
  function grade(q, r) {
    const out = { ok: false, frac: 0, fb: [], answered: r != null };
    if (r == null) { out.fb.push('You haven\'t answered yet.'); return out; }
    switch (q.type) {
      case 'mcq': {
        const o = q.options[r]; out.ok = !!(o && o.ok); out.frac = out.ok ? 1 : 0; if (o && o.fb) out.fb.push(o.fb); break;
      }
      case 'multi': {
        const sel = new Set(r), nOk = q.options.filter(o => o.ok).length; let good = 0, bad = 0;
        q.options.forEach((o, i) => { if (sel.has(i)) { if (o.ok) good++; else { bad++; if (o.fb) out.fb.push('✗ “' + o.t + '” – ' + o.fb); } } });
        out.ok = good === nOk && bad === 0; out.frac = Math.max(0, (good - bad) / nOk);
        if (!out.ok && good < nOk) out.fb.push(`You have chosen ${good} of the ${nOk} correct statements. Re-read each one: is it true in EVERY case?`);
        break;
      }
      case 'num': case 'scale': {
        const v = parseNum(r.v), u = r.u || q.unit;
        if (v == null) { out.fb.push('Please enter a number.'); out.answered = false; break; }
        let vInQ = v, unitOk = u === q.unit;
        if (!unitOk && LEN[u] && LEN[q.unit]) { vInQ = v * LEN[u] / LEN[q.unit]; }
        if (near(vInQ, q.answer, q.tol)) {
          if (unitOk || (LEN[u] && LEN[q.unit])) { out.ok = true; out.frac = 1; if (!unitOk) out.fb.push(`Correct (unit converted: ${v} ${u} = ${q.answer} ${q.unit}).`); }
          else { out.frac = 0.5; out.unitErr = true; out.fb.push(q.unitFb || `The value is right but the unit is not. What unit is this quantity measured in?`); }
          break;
        }
        const e = (q.errs || []).find(e => near(v, e.v, 1e-6) || near(vInQ, e.v, 1e-6));
        if (e) { out.fb.push(e.fb); out.divErr = q.type === 'scale'; }
        else if (q.type === 'scale') out.fb.push('Not quite. Step 1: find the two numbered marks nearest the liquid level. Step 2: count the small spaces between them. Step 3: how many mL is each space worth?');
        else out.fb.push(q.hint || 'Not quite. Write the method first, substitute the numbers, then check the answer makes sense.');
        if (!unitOk && !(LEN[u] && LEN[q.unit])) out.fb.push(q.unitFb || 'Check the unit as well.');
        break;
      }
      case 'label': {
        const keys = Object.keys(q.spots); let good = 0;
        keys.forEach((k, i) => {
          const want = q.spots[k], got = r[k];
          if (got === want) { good++; return; }
          const cf = q.confuse || {}; const key = Object.keys(cf).find(c => { const [a, b] = c.split('|'); return (a === want && b === got) || (a === got && b === want); });
          out.fb.push(`Position ${i + 1}: ` + (got ? (key ? `you have mixed up “${got}” and “${want}”. ${cf[key]}` : `“${got}” is not in the right place. Where is this position on the diagram, and what job does that part do?`) : 'not labelled yet.'));
        });
        out.frac = good / keys.length; out.ok = good === keys.length; out.detail = `${good}/${keys.length} positions correct`; break;
      }
      case 'order': {
        let good = 0; q.items.forEach((it, i) => { if (r[i] === it) good++; });
        out.frac = good / q.items.length; out.ok = good === q.items.length;
        if (!out.ok) out.fb.push(`${good}/${q.items.length} in the right place. Start with the SMALLEST item / the FIRST step, then ask: what is made from it next?`); break;
      }
      case 'match': {
        let good = 0; q.pairs.forEach(p => { if (r[p.l] === p.r) good++; else if (r[p.l]) out.fb.push(`“${p.l}” is not matched correctly. What is its main job?`); });
        out.frac = good / q.pairs.length; out.ok = good === q.pairs.length; out.detail = `${good}/${q.pairs.length} pairs correct`; break;
      }
      case 'explain': {
        const txt = String(r || ''); const hits = q.rubric.map(p => p.kw.some(k => new RegExp(k, 'i').test(txt)));
        const n = hits.filter(Boolean).length; out.hits = hits; out.frac = Math.min(1, n / q.need); out.ok = n >= q.need;
        if (txt.trim().split(/\s+/).length < 6) { out.ok = false; out.frac = 0; out.fb.push('Your answer is too short – write full sentences using “because” or “so”.'); }
        else if (!out.ok) out.fb.push(`You have ${n} of the ${q.need} points needed. Missing point: ` + q.rubric.filter((p, i) => !hits[i]).map(p => p.pt).slice(0, 1).join(' '));
        break;
      }
      case 'grid': {
        const tick = isTick(q); let good = 0, tot = 0;
        q.rows.forEach((row, ri) => {
          if (tick) row.a.forEach((a, ci) => { tot++; if ((r[ri] || [])[ci] === a) good++; });
          else { tot++; if ((r[ri] || [])[0] === row.a[0]) good++; else if ((r[ri] || [])[0]) out.fb.push(`Row “${row.l}” is not right. Which feature decides the column it belongs in?`); }
        });
        out.frac = good / tot; out.ok = good === tot; out.detail = `${good}/${tot} cells correct`;
        if (!out.ok && tick) out.fb.push(`${good}/${tot} cells correct. For each part, ask: does this cell need it, and what for?`); break;
      }
      case 'table': {
        let good = 0, tot = 0;
        q.rows.forEach((row, ri) => row.forEach((c, ci) => { if (c && typeof c === 'object') { tot++; const raw = (r[ri] || {})[ci];
          if (typeof c.ans === 'string') { if (String(raw || '').trim().toLowerCase().replace(/\s+/g, ' ') === c.ans.trim().toLowerCase()) good++; }
          else { const v = parseNum(raw); if (v != null && near(v, c.ans, c.tol || 1e-9)) good++; } } }));
        out.frac = good / tot; out.ok = good === tot; out.detail = `${good}/${tot} cells correct`;
        if (!out.ok) out.fb.push(q.hint || 'Find the pattern between the columns in the complete rows, then apply it to the blank cells.'); break;
      }
      case 'graph': {
        const want = new Set((q.plot || q.pts).map(p => p.join(','))), got = new Set((r.pts || []).map(p => p.join(',')));
        let good = 0, extra = 0; got.forEach(k => want.has(k) ? good++ : extra++);
        const plotFrac = Math.max(0, (good - extra) / want.size);
        let fOk = true; if (q.follow) { const o = q.follow.options[r.f]; fOk = !!(o && o.ok); if (o && !o.ok && o.fb) out.fb.push(o.fb); if (r.f == null) out.fb.push('Please answer the question about the trend shown by your graph.'); }
        out.frac = q.follow ? (plotFrac * 0.5 + (fOk ? 0.5 : 0)) : plotFrac; out.ok = plotFrac === 1 && fOk;
        if (plotFrac < 1) out.fb.push(`Correct points: ${good}/${want.size}${extra ? `, ${extra} extra point(s)` : ''}. For each row of the table: go along the x-axis to the value, then up to the y value.`); break;
      }
      case 'short': {
        const txt = String(r || ''); if (!txt.trim()) { out.answered = false; out.fb.push('Type your answer in the box.'); break; }
        out.ok = typedOk(txt, q.accept); out.frac = out.ok ? 1 : 0;
        if (!out.ok) out.fb.push(q.hint || 'Not quite. Check the key word from the topic and its spelling.'); break;
      }
      case 'expr': {
        const txt = exprClean(r, q.lhs); if (!txt) { out.answered = false; out.fb.push('Type your answer in the box.'); break; }
        const f = exprFn(txt); if (!f) { out.fb.push('Check how you typed it: use x^2 for x², * or nothing for ×, / for ÷ and brackets ( ).'); break; }
        const same = exprSame(txt, q.expr, q.vars); const compact = txt.toLowerCase().replace(/\s+/g, '');
        const formOk = (q.must || []).every(re => new RegExp(re, 'i').test(compact)) && !(q.mustNot || []).some(re => new RegExp(re, 'i').test(compact));
        out.ok = same && formOk; out.frac = out.ok ? 1 : 0;
        if (same && !formOk) out.fb.push(q.formFb || 'Your answer has the right value but is not in the form asked for. Read the question again.');
        else if (!same) out.fb.push(q.hint || 'Not quite. Check each step: signs, brackets and like terms.');
        break;
      }
      case 'cloze': {
        const a = Array.isArray(r) ? r : []; if (!a.some(x => String(x || '').trim())) { out.answered = false; out.fb.push('Type a word in each gap.'); break; }
        const hits = q.blanks.map((b, i) => typedOk(a[i], b)); const good = hits.filter(Boolean).length;
        out.hits = hits; out.frac = good / q.blanks.length; out.ok = good === q.blanks.length; out.detail = `${good}/${q.blanks.length} gaps correct`;
        if (!out.ok) out.fb.push(q.hint || 'Re-read the whole sentence: which science word makes it true?'); break;
      }
      case 'sim': {
        const t = r.trials || []; const objs = new Set(t.map(x => x.obj));
        const countsOk = t.length >= 2 && t.every(x => { const exp = SCOPE_COUNT[x.obj]; const v = parseNum(x.count); return v != null && Math.abs(v - exp) <= Math.max(1, exp * 0.2); });
        const conclOk = r.concl === 'fewer';
        out.ok = objs.size >= 2 && countsOk && conclOk && !!r.pred; out.frac = out.ok ? 1 : (objs.size >= 2 ? 0.3 : 0) + (countsOk ? 0.3 : 0) + (conclOk ? 0.4 : 0);
        if (objs.size < 2) out.fb.push('You need at least 2 trials with 2 DIFFERENT objective lenses to compare.');
        if (t.length >= 2 && !countsOk) out.fb.push('Count again: count the cells sitting on the red line, from the left edge to the right edge of the field of view.');
        if (r.concl && !conclOk) out.fb.push('Compare your results table: when the magnification goes UP, does the number of cells on the red line go up or down?');
        break;
      }
    }
    return out;
  }
  const isTick = q => q.mode ? q.mode === 'tick' : q.rows.every(r => r.a && r.a.length === q.cols.length && r.a.every(a => a === '✓' || a === '✗'));
  function answerText(q) {
    switch (q.type) {
      case 'mcq': return q.options.find(o => o.ok).t;
      case 'multi': return q.options.filter(o => o.ok).map(o => o.t).join(' • ');
      case 'num': case 'scale': return `${q.answer} ${q.unit}`;
      case 'label': return Object.values(q.spots).map((v, i) => `${i + 1} = ${v}`).join('; ');
      case 'order': return q.items.join(' → ');
      case 'match': return q.pairs.map(p => `${p.l} → ${p.r}`).join('; ');
      case 'explain': return q.model;
      case 'grid': return q.rows.map(r => `${r.l}: ${r.a.join(' / ')}`).join('; ');
      case 'table': return q.rows.map(r => r.map(c => c && typeof c === 'object' ? `[${c.ans}]` : c).join(' | ')).join(' ; ');
      case 'graph': return 'Points: ' + (q.plot || q.pts).map(p => `(${p[0]}, ${p[1]})`).join(' ') + (q.follow ? ' — ' + q.follow.options.find(o => o.ok).t : '');
      case 'short': return plainOf(q.accept);
      case 'expr': return (q.lhs ? q.lhs + ' = ' : '') + (q.show || q.expr);
      case 'cloze': { let i = 0; return String(q.text).replace(/\{\d+\}/g, () => '[' + plainOf(q.blanks[i++]) + ']'); }
      case 'sim': return '×4 ≈ 12 cells, ×10 ≈ 5 cells, ×40 ≈ 1 cell across the line → higher magnification: cells look bigger, fewer fit across the field of view.';
    }
    return '';
  }


  /* Mark a whole test paper. items carry pts; teacher-marked items are left pending. */
  function scoreTest(items, answers) {
    let auto = 0; const per = {}; const pending = [];
    for (const q of items) {
      const r = answers[q.id];
      if (q.teacher) { pending.push(q.id); const g = r != null ? grade(q, r) : null; per[q.id] = { pts: null, max: q.pts, teacher: true, suggest: g ? Math.round(q.pts * g.frac * 2) / 2 : 0 }; continue; }
      const g = grade(q, r == null ? null : r);
      let frac = g.frac; if ((q.type === 'num' || q.type === 'scale') && !g.ok) frac = g.unitErr ? 0.5 : 0;
      if (q.type === 'mcq') frac = g.ok ? 1 : 0;
      const pts = Math.round(q.pts * frac * 100) / 100; per[q.id] = { pts, max: q.pts }; auto += pts;
    }
    return { per, auto: Math.round(auto * 100) / 100, pending };
  }
  /* A copy of a question safe to show before submission: no keys, no feedback, no model answers. */
  function stripKeys(q) {
    const s = { id: q.id, type: q.type, prompt: q.prompt, diff: q.diff, obj: q.obj, skill: q.skill };
    if (q.pts != null) s.pts = q.pts; if (q.teacher) s.teacher = true; if (q.fig) s.fig = q.fig; if (q.ctx) s.ctx = q.ctx; if (q.data) s.data = q.data;
    switch (q.type) {
      case 'mcq': case 'multi': s.options = q.options.map(o => ({ t: o.t })); break;
      case 'num': case 'scale': s.unit = q.unit; s.units = q.units; if (q.bare) s.bare = true; break;
      case 'label': s.anchors = Object.keys(q.spots); s.labels = shuffle(Object.values(q.spots), 'k' + q.id); break;
      case 'order': { let it = shuffle(q.items, 'k' + q.id); if (it.join() === q.items.join()) it = it.slice().reverse(); s.items = it; break; }
      case 'match': s.lefts = q.pairs.map(p => p.l); s.rights = shuffle(q.pairs.map(p => p.r), 'k' + q.id); break;
      case 'grid': s.cols = q.cols; s.mode = isTick(q) ? 'tick' : 'classify'; s.rows = q.rows.map(r => ({ l: r.l })); break;
      case 'table': s.head = q.head; s.rows = q.rows.map(r => r.map(c => c && typeof c === 'object' ? { blank: true } : c)); break;
      case 'explain': break;
      case 'graph': s.x = q.x; s.y = q.y; if (q.table_rows) s.table_rows = q.table_rows; if (q.follow) s.follow = { prompt: q.follow.prompt, options: q.follow.options.map(o => ({ t: o.t })) }; break;
      case 'sim': s.sim = q.sim; break;
      case 'short': if (q.width) s.width = q.width; break;
      case 'expr': if (q.lhs) s.lhs = q.lhs; if (q.vars) s.vars = q.vars; break;
      case 'cloze': s.text = q.text; s.n = q.blanks.length; break;
    }
    return s;
  }
  return { grade, answerText, scoreTest, stripKeys, isTick, shuffle, rng, parseNum, near, typedOk, normText, exprFn, exprSame, TYPE_VI, DIFF, SCOPE_COUNT };
});
