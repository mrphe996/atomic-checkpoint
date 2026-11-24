/* Atomic Education — maths typesetting and maths input for the Mathematics courses (rendered with KaTeX, MIT licence, web/vendor/katex).
   1. AtomicMath.tex(expr)      plain or Unicode maths ("3x^2 − 2x", "(y+5)/3", "√50", "x²") → TeX, or null if it does not parse
   2. AtomicMath.typeset(root)  finds the maths inside text (prompts, options, lessons, tables) and renders it like a textbook
   3. AtomicMath.input(opts)    a maths answer box with a live typeset preview and an on-screen maths keypad
   Answers typed by learners are never changed: they are only shown typeset. Written by the Atomic teaching team. */
(function () {
  const SUP = '⁰¹²³⁴⁵⁶⁷⁸⁹⁻', SUPN = '0123456789-';
  const UNITS = new Set(['mm', 'cm', 'km', 'kg', 'ml', 'cl', 'mg', 'm', 'g', 'l', 'h', 's', 'min', 'ha', 'mph', 'kmh']);
  const K = () => window.katex;

  /* ---------- 1. expression → TeX ---------- */
  function lex(src) {
    const s = String(src).replace(/[−–]/g, '-').replace(/\*\*/g, '^').replace(/sqrt/gi, '√').replace(/≦/g, '≤').replace(/≧/g, '≥');
    const t = []; let i = 0;
    while (i < s.length) {
      const c = s[i];
      if (/\s/.test(c)) { if (t.length) t[t.length - 1].sp = true; i++; continue; }
      if (/[0-9.]/.test(c)) { let j = i; while (j < s.length && /[0-9.\u0307]/.test(s[j])) j++;
        // thousands written with a space: 12 000
        while (/^ \d{3}(?!\d)/.test(s.slice(j))) j += 4;
        t.push({ k: 'n', v: s.slice(i, j) }); i = j; continue; }
      if (SUP.includes(c)) { let j = i; while (j < s.length && SUP.includes(s[j])) j++; t.push({ k: '^' }, { k: 'n', v: s.slice(i, j).split('').map(x => SUPN[SUP.indexOf(x)]).join(''), sup: true }); i = j; continue; }
      if (/[A-Za-z]/.test(c)) { let j = i; while (j < s.length && /[A-Za-z]/.test(s[j])) j++; t.push({ k: 'v', v: s.slice(i, j) }); i = j; continue; }
      if ('+-×·*÷/=<>≤≥≠±^()[]√∛π°%'.includes(c)) { t.push({ k: c }); i++; continue; }
      return null;
    }
    return t;
  }
  const numTex = v => v.replace(/(\d)\u0307/g, '\\dot{$1}').replace(/ (?=\d{3})/g, '\\,');
  function parse(src, live) {
    const t = lex(src); if (!t || !t.length) return null;
    let p = 0; const peek = () => t[p], eat = k => (t[p] && t[p].k === k ? t[p++] : null);
    const bare = s => (s.startsWith('\\left(') && s.endsWith('\\right)') && depthOk(s.slice(6, -7)) ? s.slice(6, -7) : s);
    function depthOk(s) { let d = 0; for (const m of s.matchAll(/\\left\(|\\right\)/g)) { d += m[0] === '\\left(' ? 1 : -1; if (d < 0) return false; } return d === 0; }
    function atom() {
      const x = peek(); if (!x) { if (live) return '\\square'; throw 0; }
      if (x.k === 'n') { p++; return numTex(x.v); }
      if (x.k === 'v') { const pr = t[p - 1]; p++;
        if (UNITS.has(x.v) && (x.v.length > 1 || (pr && pr.k === 'n' && pr.sp))) return `\\,\\mathrm{${x.v}}`;   // 5 cm², 60 m
        return x.v.length > 1 && !/^[a-z]{1,3}$/.test(x.v) ? `\\text{${x.v}}` : x.v; }
      if (x.k === 'π') { p++; return '\\pi'; }
      if (x.k === '(' || x.k === '[') { p++; const e = rel(); if (!eat(x.k === '(' ? ')' : ']')) { if (!live) throw 0; } return x.k === '(' ? `\\left(${e}\\right)` : `\\left[${e}\\right]`; }
      if (x.k === '√' || x.k === '∛') { p++; const a = power(); return `\\sqrt${x.k === '∛' ? '[3]' : ''}{${bare(a)}}`; }
      if (live) return '\\square';
      throw 0;
    }
    function power() {
      let a = atom();
      for (;;) {
        if (eat('°')) { a += '^{\\circ}'; continue; }
        if (eat('%')) { a += '\\%'; continue; }
        if (peek() && peek().k === '^') { p++; let e; if (eat('-')) e = '-' + atom(); else e = atom(); a = `{${a}}^{${bare(e)}}`; continue; }
        return a;
      }
    }
    function unary() { if (eat('-')) return '-' + unary(); if (eat('+')) return '+' + unary(); if (eat('±')) return '\\pm ' + unary(); return power(); }
    function term() {
      let out = unary();
      for (;;) {
        const x = peek(); if (!x) return out;
        if (x.k === '*' || x.k === '·' || x.k === '×') { p++; out += ' \\times ' + unary(); continue; }
        if (x.k === '÷') { p++; out += ' \\div ' + unary(); continue; }
        if (x.k === '/') { p++; out = `\\frac{${bare(out)}}{${bare(unary())}}`; continue; }
        if (x.k === 'n' || x.k === 'v' || x.k === '(' || x.k === '√' || x.k === '∛' || x.k === 'π') {
          const prev = t[p - 1];
          // two numbers side by side: a mixed number 2 1/2, otherwise not maths
          if (x.k === 'n' && prev && prev.k === 'n') { if (t[p + 1] && t[p + 1].k === '/' && t[p + 2] && t[p + 2].k === 'n') { p++; p++; const d = t[p++]; out += `\\tfrac{${x.v}}{${d.v}}`; continue; } throw 0; }
          out += (x.k === 'n' ? ' \\times ' : x.k === 'v' && prev && prev.k === 'v' ? '\\,' : '') + power(); continue;
        }
        return out;
      }
    }
    function sum() { let out = term(); for (;;) { if (eat('+')) out += ' + ' + term(); else if (eat('-')) out += ' - ' + term(); else if (eat('±')) out += ' \\pm ' + term(); else return out; } }
    function rel() { let out = sum(); const R = { '=': '=', '<': '<', '>': '>', '≤': '\\le', '≥': '\\ge', '≠': '\\ne' };
      for (;;) { const x = peek(); if (x && R[x.k]) { p++; out += ` ${R[x.k]} ` + (peek() || !live ? sum() : '\\square'); } else return out; } }
    try { const r = rel(); if (p < t.length) return null; return r; } catch (e) { return null; }
  }
  function tex(src, live) {
    let r = parse(src, false); if (r != null || !live) return r;
    // while typing: close open brackets and show an empty box where something is still missing
    let s = String(src); const open = (s.match(/\(/g) || []).length - (s.match(/\)/g) || []).length;
    for (let k = 0; k < open; k++) s += ')';
    return parse(s, true);
  }
  function render(t, el, display) {
    if (!K() || t == null) { el.textContent = ''; return false; }
    try { K().render(t, el, { throwOnError: false, displayMode: !!display, strict: 'ignore', output: 'html' }); return true; } catch (e) { el.textContent = ''; return false; }
  }

  /* ---------- 2. maths inside text ---------- */
  const SKIP = 'input,textarea,select,svg,script,style,.katex,.mt,.notex,.mathprev,.mxin,.mkpad,.chip,.tag,code';
  const OK = '.qp,.qctx,.qbody,.opt,.fb,.reason,.hint,.rubric,.match,.order,.grid,.tablewrap,.lblock,.lcheck,.lans,.solx,.mrow,.qdata,table';
  const TOK = /(\d{1,3}(?: \d{3})+(?!\d)|\d+(?:\.\d+)?\u0307?\d*\u0307?)|([A-Za-z]+)|([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)|([ \u00a0]+)|([+−\-×÷=<>≤≥≠±()√∛π°\/^])|([\s\S])/g;
  const OPS = '+−-×÷=<>≤≥≠±';
  const CUE = /[⁰¹²³⁴⁵⁶⁷⁸⁹√∛π×÷=≤≥≠^\u0307]|\d\s*\/\s*\d|[a-z)]\/\d|\d\/[a-z(]|\d[a-z]|[a-z]\s*[+−\-]\s*[a-z\d(]|[\d)]\s*[+−\-]\s*\d/;
  function runs(text) {
    const toks = []; let m; TOK.lastIndex = 0;
    while ((m = TOK.exec(text))) { const [s, num, word, sup, sp, op] = m; toks.push({ s, i: m.index, k: num ? 'n' : word ? 'w' : sup ? 'sup' : sp ? 'sp' : op ? 'op' : 'x' }); }
    const cand = (tk, j) => {
      if (tk.k === 'n' || tk.k === 'sup' || tk.k === 'op') return true;
      if (tk.k !== 'w') return false;
      const prev = toks[j - 1], next = toks[j + 1];
      const glued = (prev && prev.k !== 'sp' && prev.k !== 'x') || (next && (next.k === 'sup' || (next.k === 'op' && next.s !== '/' ? true : next.k === 'n')));
      if (tk.s.length === 1) {
        if (/^[aAI]$/.test(tk.s)) { const pp = toks[j - 1] && toks[j - 1].k === 'sp' ? toks[j - 2] : prev, nn = next && next.k === 'sp' ? toks[j + 2] : next; return !!((pp && pp.k === 'op' && pp.s !== '(') || (nn && nn.k === 'op' && nn.s !== '(' && nn.s !== '/') || glued); }
        return true;
      }
      if (tk.s.length <= 3 && glued) return true;
      return false;
    };
    const out = []; let cur = null;
    toks.forEach((tk, j) => {
      if (cand(tk, j) || (tk.k === 'sp' && cur)) { if (!cur) cur = { a: tk.i, toks: [] }; cur.toks.push(tk); cur.b = tk.i + tk.s.length; }
      else if (cur) { out.push(cur); cur = null; }
    });
    if (cur) out.push(cur);
    return out.map(r => {
      // a run cut off by bold text or punctuation: leave hanging signs (3 × n = **3n**) as text
      while (r.toks.length && (r.toks[r.toks.length - 1].k === 'sp' || /^[=+−\-×÷<>≤≥≠±(√∛\/^]$/.test(r.toks[r.toks.length - 1].s))) r.toks.pop();
      while (r.toks.length && (r.toks[0].k === 'sp' || /^[=+×÷<>≤≥≠)\/^]$/.test(r.toks[0].s))) { r.a += r.toks[0].s.length; r.toks.shift(); }
      const s = r.toks.map(x => x.s).join(''); return { a: r.a, b: r.a + s.length, s }; })
      .filter(r => r.s.trim() && CUE.test(r.s) && !/^[\d\s]+$/.test(r.s));
  }
  function unitsIn(s) {   // "5 cm²" → mark cm as a unit so it is not set in italics
    return s.replace(/(\d)(\s+)(mm|cm|km|kg|ml|mg|ha|m|g|l)(?![A-Za-z])/g, '$1$2⟦$3⟧');
  }
  function runTex(s) {
    const u = unitsIn(s);
    if (u.includes('⟦')) { const parts = u.split(/⟦(\w+)⟧/); let outT = ''; for (let i = 0; i < parts.length; i++) { if (i % 2) outT += `\\,\\mathrm{${parts[i]}}`; else if (parts[i].trim()) { const sup = parts[i].match(/^([⁰¹²³⁴⁵⁶⁷⁸⁹]+)(.*)$/s); if (sup && i) { outT += '^{' + sup[1].split('').map(x => SUPN[SUP.indexOf(x)]).join('') + '}'; if (sup[2].trim()) { const r = parse(sup[2]); if (r == null) return null; outT += ' ' + r; } } else { const r = parse(parts[i]); if (r == null) return null; outT += r; } } } return outT; }
    return parse(s);
  }
  function typesetText(node) {
    const t = node.nodeValue; if (!t || !CUE.test(t)) return;
    const p = node.parentElement; if (!p || p.closest(SKIP) || !p.closest(OK)) return;
    const rs = runs(t); if (!rs.length) return;
    const frag = document.createDocumentFragment(); let last = 0, any = false;
    rs.forEach(r => {
      // keep a leading or trailing space outside the maths
      let a = r.a, b = r.b; while (/\s/.test(t[a])) a++; while (b > a && /\s/.test(t[b - 1])) b--;
      const src = t.slice(a, b); const tx = runTex(src); if (tx == null) return;
      if (a > last) frag.append(t.slice(last, a));
      const sp = document.createElement('span'); sp.className = 'mt'; sp.setAttribute('data-src', src);
      if (!render(tx, sp)) { sp.textContent = src; } frag.append(sp); last = b; any = true;
    });
    if (!any) return;
    if (last < t.length) frag.append(t.slice(last));
    node.replaceWith(frag);
  }
  function typeset(root) {
    if (!root || !(window.Core && Core.IS_MATHS) || !K()) return;
    if (root.nodeType === 3) { typesetText(root); return; }
    if (root.nodeType !== 1 || (root.closest && root.closest(SKIP))) return;
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT); const list = []; let n;
    while ((n = w.nextNode())) if (CUE.test(n.nodeValue)) list.push(n);
    list.forEach(typesetText);
  }

  /* ---------- 3. maths answer box with keypad ---------- */
  function input(o) {
    // o: { value, vars ('xy'), lhs, onInput(value), placeholder }
    const vars = (o.vars || 'x').split('').filter(c => /[a-z]/i.test(c));
    const inp = document.createElement('input');
    Object.assign(inp, { type: 'text', className: 'shortin mathin', autocomplete: 'off', spellcheck: false, value: o.value || '', placeholder: o.placeholder || 'Type or use the keypad' });
    inp.setAttribute('aria-label', 'Your answer'); inp.setAttribute('autocapitalize', 'off');
    const prev = document.createElement('div'); prev.className = 'mathprev'; prev.setAttribute('aria-live', 'polite');
    const pv = document.createElement('span'); pv.className = 'mpv';
    const hint = document.createElement('small'); hint.className = 'mphint';
    prev.append(pv, hint);
    const show = () => {
      const v = inp.value.trim();
      if (!v) { pv.textContent = ''; hint.textContent = ''; prev.classList.remove('bad', 'on'); return; }
      const full = tex(v, false), t = full != null ? full : tex(v, true);
      prev.classList.add('on'); prev.classList.toggle('bad', t == null);
      if (t == null) { pv.textContent = ''; hint.textContent = 'Check how you typed it: use the keypad for powers, fractions and roots.'; return; }
      render('\\displaystyle ' + (o.lhs ? o.lhs + ' = ' : '') + t, pv, false);
      hint.textContent = full == null ? 'Keep going… (finish the empty box)' : '';
    };
    const put = (txt, back) => {
      const a = inp.selectionStart != null ? inp.selectionStart : inp.value.length, b = inp.selectionEnd != null ? inp.selectionEnd : a;
      inp.value = inp.value.slice(0, a) + txt + inp.value.slice(b); const c = a + txt.length - (back || 0);
      inp.focus(); try { inp.setSelectionRange(c, c); } catch (e) { /* some inputs */ } fire();
    };
    const fire = () => { show(); o.onInput && o.onInput(inp.value); };
    const keyTex = { '^2': 'x^{2}', '^()': 'x^{\\square}', '()/()': '\\frac{\\square}{\\square}', '√()': '\\sqrt{\\square}', '*': '\\times', '/': '\\div', '-': '-', '+': '+', '=': '=', '(': '(', ')': ')', 'π': '\\pi' };
    // keypad laid out like a calculator: digits on the left, operations in the middle, maths templates and editing on the right
    const V = (vars.length ? vars : ['x']).slice(0, 3).map(v => [v, v]);
    while (V.length < 3) V.push(null);
    const keys = [
      ['7', '7'], ['8', '8'], ['9', '9'], ['/', '/'], ['(', '('], [')', ')'], ['^2', '^2'], ['⌫', 'BS'],
      ['4', '4'], ['5', '5'], ['6', '6'], ['*', '*'], ['()/()', '()/()', 4], ['√()', '√()', 1], ['^()', '^()', 1], ['←', 'L'],
      ['1', '1'], ['2', '2'], ['3', '3'], ['-', '-'], V[0], V[1], V[2], ['→', 'R'],
      ['0', '0'], ['.', '.'], ['=', '='], ['+', '+'], null, null, null, ['Clear', 'CLR']];
    const pad = document.createElement('div'); pad.className = 'mkpad'; pad.setAttribute('role', 'group'); pad.setAttribute('aria-label', 'Maths keypad');
    keys.forEach(k => {
      if (!k) { const g = document.createElement('span'); g.className = 'mkgap'; pad.append(g); return; }
      const [lab, ins, back] = k;
      const b = document.createElement('button'); b.type = 'button'; b.className = 'mkey' + (/^\d$/.test(lab) ? ' num' : /^(L|R|BS|CLR)$/.test(ins) ? ' nav' : vars.includes(lab) ? ' var' : ' op');
      if (keyTex[lab] && K()) render(keyTex[lab], b); else b.textContent = lab;
      b.setAttribute('aria-label', { '^2': 'squared', '^()': 'power', '()/()': 'fraction', '√()': 'square root', '*': 'times', '/': 'divide', '-': 'minus', L: 'left', R: 'right', BS: 'delete', CLR: 'clear' }[ins] || lab);
      b.onmousedown = e => e.preventDefault();
      b.onclick = () => {
        const a = inp.selectionStart != null ? inp.selectionStart : inp.value.length;
        if (ins === 'L') { inp.focus(); inp.setSelectionRange(Math.max(0, a - 1), Math.max(0, a - 1)); return; }
        if (ins === 'R') { inp.focus(); inp.setSelectionRange(a + 1, a + 1); return; }
        if (ins === 'BS') { const b2 = inp.selectionEnd; if (b2 > a) { inp.value = inp.value.slice(0, a) + inp.value.slice(b2); } else if (a > 0) { inp.value = inp.value.slice(0, a - 1) + inp.value.slice(a); inp.focus(); inp.setSelectionRange(a - 1, a - 1); } fire(); return; }
        if (ins === 'CLR') { inp.value = ''; inp.focus(); fire(); return; }
        put(ins, back);
      };
      pad.append(b);
    });
    const tog = document.createElement('button'); tog.type = 'button'; tog.className = 'mktog'; tog.setAttribute('aria-expanded', 'true');
    render('{}^{-\\times}_{+=}', tog); tog.title = 'Show or hide the maths keypad';
    tog.onclick = () => { pad.hidden = !pad.hidden; tog.setAttribute('aria-expanded', String(!pad.hidden)); };
    inp.addEventListener('input', fire);
    const row = document.createElement('div'); row.className = 'mxin';
    if (o.lhs) { const l = document.createElement('span'); l.className = 'lhs'; render(o.lhs + ' =', l); row.append(l); }
    row.append(inp, tog);
    const box = document.createElement('div'); box.className = 'mxbox'; box.append(row, prev, pad);
    show();
    return { el: box, input: inp };
  }

  const obs = new MutationObserver(ms => { if (!(window.Core && Core.IS_MATHS)) return; ms.forEach(m => m.addedNodes.forEach(typeset)); });
  function start() { obs.observe(document.body, { childList: true, subtree: true }); typeset(document.body); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
  window.AtomicMath = { typeset, tex, render, input, runs };
})();
