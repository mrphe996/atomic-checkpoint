/* Camday — maths typesetting and maths input for the Mathematics courses (rendered with KaTeX, MIT licence, web/vendor/katex).
   1. AtomicMath.tex(expr)      plain or Unicode maths ("3x^2 − 2x", "(y+5)/3", "√50", "x²") → TeX, or null if it does not parse
   2. AtomicMath.typeset(root)  finds the maths inside text (prompts, options, lessons, tables) and renders it like a textbook
   3. AtomicMath.input(opts)    a maths answer box with a live typeset preview and an on-screen maths keypad
   4. AtomicMath.field(opts)    a maths answer box you type straight into: fractions, powers and roots build as you type (like a textbook)
   Answers typed by learners are never changed: they are only shown typeset. Written by the Camday teaching team. */
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
  const SKIP = 'input,textarea,select,svg,script,style,.katex,.mt,.notex,.mathprev,.mxin,.mkpad,.mqf,.chip,.tag,code';
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

  /* ---------- 4. WYSIWYG maths field: type straight into the formula (fractions, powers and roots build as you type) ---------- */
  // model: a row is an array of items; an item is a one-character string or { t: 'frac'|'sup'|'sqrt', a: row, b?: row }
  const FOPS = { '*': '\\times ', '×': '\\times ', '/': '\\div ', '÷': '\\div ', '-': '-', '−': '-', '+': '+', '=': '=', '<': '<', '>': '>', '≤': '\\le ', '≥': '\\ge ', '≠': '\\ne ', '(': '(', ')': ')', '.': '.', ',': ',', 'π': '\\pi ', '%': '\\%', '°': '^{\\circ}', '±': '\\pm ', ' ': '\\,' };
  const slots = it => (it.t === 'frac' ? [it.a, it.b] : [it.a]);
  function fromPlain(s) {
    // plain answer text → model (so a saved answer reopens as a formula)
    s = String(s || '').replace(/sqrt/gi, '√').replace(/\*\*/g, '^').replace(/−/g, '-');
    let i = 0;
    const atom = () => {              // one item, a bracket group (kept with its brackets) or a √ root
      if (s[i] === '(') { let d = 0, j = i; do { if (s[j] === '(') d++; else if (s[j] === ')') d--; j++; } while (j < s.length && d > 0); const inner = s.slice(i + 1, j - 1); i = j; return { grp: row(inner) }; }
      if (s[i] === '√') { i++; const g = atom(); return { t: 'sqrt', a: g && g.grp ? g.grp : g ? [].concat(flat(g)) : [] }; }
      const c = s[i++]; return c;
    };
    const flat = g => (g && g.grp ? ['(', ...g.grp, ')'] : [g]);
    function row(str) { const save = [s, i]; s = str; i = 0; const out = [];
      while (i < s.length) {
        let a = atom(); if (a == null) break;
        // digits stay together as the base of a power or the top of a fraction
        if (s[i] === '^') { i++; let e; if (s[i] === '(') e = atom().grp; else { e = []; if (s[i] === '-' && /[0-9]/.test(s[i + 1] || '')) e.push(s[i++]); while (i < s.length && /[0-9]/.test(s[i])) e.push(s[i++]); if (!e.length && i < s.length) e.push(s[i++]); }
          out.push(...flat(a), { t: 'sup', a: e }); continue; }
        const den = () => { let bot = []; if (s[i] === '(') bot = atom().grp; else if (/[0-9.]/.test(s[i] || '')) { while (i < s.length && /[0-9.]/.test(s[i])) bot.push(s[i++]); } else if (/[A-Za-zπ]/.test(s[i] || '')) bot.push(s[i++]); return bot; };
        if (s[i] === '/' && a && a.grp) { i++; out.push({ t: 'frac', a: a.grp, b: den() }); continue; }
        if (a === '/' && out.length) {
          // 2x/5 → fraction: the numbers, letters and powers just before, over the number, letter or bracket just after
          let k = out.length; while (k > 0 && (typeof out[k - 1] !== 'string' ? out[k - 1].t === 'sup' : /[0-9.A-Za-zπ]/.test(out[k - 1]))) k--;
          const top = out.splice(k); out.push({ t: 'frac', a: top, b: den() }); continue;
        }
        out.push(...flat(a));
      }
      [s, i] = save; return out; }
    return row(s);
  }
  function toPlain(r) {
    // as few brackets as possible, so form checks (no brackets / a single fraction) still see what the learner meant
    return r.map(it => {
      if (typeof it === 'string') return it;
      const p = toPlain(it.a);
      if (it.t === 'frac') { const q = toPlain(it.b);
        return (/^[0-9.A-Za-zπ^]+$/.test(p) ? p : '(' + p + ')') + '/' + (/^[0-9.]+$|^[A-Za-zπ]$/.test(q) ? q : '(' + q + ')'); }
      if (it.t === 'sup') return '^' + (/^-?[0-9]+$|^[A-Za-z]$/.test(p) ? p : '(' + p + ')');
      if (it.t === 'sqrt') return '√' + (/^[0-9.]+$|^[A-Za-z]$/.test(p) ? p : '(' + p + ')');
      return '';
    }).join('');
  }
  function field(o) {
    // o: { value, vars ('xy'), lhs, onInput(value) } → { el, input } (input.value holds the plain answer, like input())
    const vars = (o.vars || 'x').split('').filter(c => /[a-z]/i.test(c));
    let root = fromPlain(o.value || ''), cur = { r: root, i: root.length };
    const parents = new Map();      // row → [parentRow, index of the structure in it]
    const index = () => { parents.clear(); const walk = r => r.forEach((it, k) => { if (typeof it !== 'string') slots(it).forEach(sl => { parents.set(sl, [r, k, it]); walk(sl); }); }); walk(root); };
    const box = document.createElement('div'); box.className = 'mxbox mqbox';
    const fld = document.createElement('div'); fld.className = 'mqf'; fld.setAttribute('role', 'textbox'); fld.setAttribute('aria-label', 'Your answer (maths)'); fld.tabIndex = -1;
    const view = document.createElement('span'); view.className = 'mqv';
    const ta = document.createElement('textarea'); ta.className = 'mqta'; ta.setAttribute('autocapitalize', 'off'); ta.setAttribute('autocomplete', 'off'); ta.setAttribute('autocorrect', 'off'); ta.spellcheck = false; ta.setAttribute('aria-label', 'Your answer');
    const coarse = window.matchMedia && matchMedia('(pointer: coarse)').matches;
    if (coarse) ta.setAttribute('inputmode', 'none');
    const sr = document.createElement('span'); sr.className = 'sr-only'; sr.setAttribute('aria-live', 'polite');
    const hidden = { value: toPlain(root) };
    const reg = [];
    // TeX for a row, with the cursor and clickable places (\htmlData, allowed only for our own data-mq attribute)
    function rtex(r, top) {
      let s = '';
      const caret = '\\htmlClass{mqcur}{\\rule[-0.2em]{0.09em}{1.05em}}';
      if (!r.length && cur.r !== r) return '\\htmlClass{mqempty}{\\square}';
      r.forEach((it, k) => {
        if (cur.r === r && cur.i === k) s += caret;
        const id = reg.push([r, k + 1]) - 1;
        let body;
        if (typeof it === 'string') {
          if (/[0-9]/.test(it)) body = it; else if (/[A-Za-z]/.test(it)) body = it; else body = FOPS[it] != null ? FOPS[it] : '\\text{' + it.replace(/[\\{}]/g, '') + '}';
          const bin = '+-−=<>≤≥≠×*÷/±'.includes(it);
          s += `\\htmlData{mq=${id}}{${bin ? (/[=<>≤≥≠]/.test(it) ? '\\mathrel{' + body + '}' : '\\mathbin{' + body + '}') : body}}`;
        } else if (it.t === 'frac') s += `\\htmlData{mq=${id}}{\\dfrac{${rtex(it.a)}}{${rtex(it.b)}}}`;
        else if (it.t === 'sup') s += `\\htmlData{mq=${id}}{{}^{${rtex(it.a)}}}`;
        else if (it.t === 'sqrt') s += `\\htmlData{mq=${id}}{\\sqrt{${rtex(it.a)}}}`;
      });
      if (cur.r === r && cur.i === r.length) s += caret;
      return s || '\\,';
    }
    function draw() {
      index(); reg.length = 0;
      const t = (o.lhs ? o.lhs + ' = ' : '') + rtex(root, true);
      if (K()) { try { K().render('\\displaystyle ' + t, view, { throwOnError: false, strict: 'ignore', output: 'html', trust: c => c.command === '\\htmlData' || c.command === '\\htmlClass' }); } catch (e) { view.textContent = toPlain(root); } }
      else view.textContent = toPlain(root);
      fld.classList.toggle('empty', !root.length);
      const v = toPlain(root); if (v !== hidden.value) { hidden.value = v; o.onInput && o.onInput(v); }
      sr.textContent = v ? 'Answer: ' + v.replace(/\*/g, ' times ').replace(/\//g, ' over ').replace(/\^/g, ' to the power ').replace(/√/g, ' root ') : '';
    }
    const isAtom = it => typeof it === 'string' && /[0-9A-Za-z.π]/.test(it);
    function insert(ch) {
      const r = cur.r;
      // a power of digits ends when an operator or a letter follows (x^2+1), so pupils need not press →
      const par = parents.get(r);
      if (par && par[2].t === 'sup' && cur.i === r.length && r.length && r.every(c => /^[0-9]$/.test(c)) && /[+\-−=<>*×÷\/)A-Za-z ]/.test(ch)) { cur = { r: par[0], i: par[1] + 1 }; return insert(ch); }
      if (ch === '/' ) {
        // the number or letters just before the cursor become the top of the fraction
        let k = cur.i; while (k > 0 && (isAtom(r[k - 1]) || (typeof r[k - 1] !== 'string' && r[k - 1].t !== 'frac'))) k--;
        if (k > 0 && r[k - 1] === ')') { let d = 0, j = k - 1; for (; j >= 0; j--) { if (r[j] === ')') d++; else if (r[j] === '(') { d--; if (!d) break; } } if (j >= 0) { const g = r.slice(j + 1, k - 1); r.splice(j, k - j); const f = { t: 'frac', a: g, b: [] }; r.splice(j, 0, f); cur = { r: f.b, i: 0 }; return; } }
        const top = r.splice(k, cur.i - k); const f = { t: 'frac', a: top, b: [] }; r.splice(k, 0, f); cur = top.length ? { r: f.b, i: 0 } : { r: f.a, i: 0 }; return;
      }
      if (ch === '^') { const sp = { t: 'sup', a: [] }; r.splice(cur.i, 0, sp); cur = { r: sp.a, i: 0 }; return; }
      if (ch === '√') { const q = { t: 'sqrt', a: [] }; r.splice(cur.i, 0, q); cur = { r: q.a, i: 0 }; return; }
      r.splice(cur.i, 0, ch); cur.i++;
    }
    function left() {
      const r = cur.r;
      if (cur.i > 0) { const it = r[cur.i - 1]; if (typeof it !== 'string') { const sl = slots(it); const last = sl[sl.length - 1]; cur = { r: last, i: last.length }; } else cur.i--; return; }
      const par = parents.get(r); if (!par) return;
      const [pr, k, it] = par;
      if (it.t === 'frac' && r === it.b) { cur = { r: it.a, i: it.a.length }; return; }
      cur = { r: pr, i: k };
    }
    function right() {
      const r = cur.r;
      if (cur.i < r.length) { const it = r[cur.i]; if (typeof it !== 'string') cur = { r: slots(it)[0], i: 0 }; else cur.i++; return; }
      const par = parents.get(r); if (!par) return;
      const [pr, k, it] = par;
      if (it.t === 'frac' && r === it.a) { cur = { r: it.b, i: 0 }; return; }
      cur = { r: pr, i: k + 1 };
    }
    function vert(down) {
      let r = cur.r;
      while (r) { const par = parents.get(r); if (!par) return; const it = par[2];
        if (it.t === 'frac') { if (down && r === it.a) { cur = { r: it.b, i: Math.min(cur.r === r ? cur.i : 0, it.b.length) }; return; } if (!down && r === it.b) { cur = { r: it.a, i: Math.min(cur.r === r ? cur.i : 0, it.a.length) }; return; } }
        r = par[0]; }
    }
    function back() {
      const r = cur.r;
      if (cur.i > 0) { const it = r[cur.i - 1];
        if (typeof it === 'string') { r.splice(cur.i - 1, 1); cur.i--; return; }
        if (slots(it).every(sl => !sl.length)) { r.splice(cur.i - 1, 1); cur.i--; return; }
        const sl = slots(it); const last = sl[sl.length - 1]; cur = { r: last, i: last.length }; return; }
      const par = parents.get(r); if (!par) return;
      // at the start of a box: take the box apart and keep what was written in it
      const [pr, k, it] = par; const keep = [].concat(...slots(it));
      const before = it.t === 'frac' && r === it.b ? it.a.length : 0;
      pr.splice(k, 1, ...keep); cur = { r: pr, i: k + before };
    }
    function key(cmd) {
      if (cmd === 'L') left(); else if (cmd === 'R') right(); else if (cmd === 'U') vert(false); else if (cmd === 'D') vert(true);
      else if (cmd === 'BS') back();
      else if (cmd === 'CLR') { root.length = 0; cur = { r: root, i: 0 }; }
      else if (cmd === 'FRAC') { const f = { t: 'frac', a: [], b: [] }; cur.r.splice(cur.i, 0, f); cur = { r: f.a, i: 0 }; }
      else if (cmd === 'SQ') { insert('^'); insert('2'); right(); }
      else if (cmd === 'HOME') cur = { r: root, i: 0 }; else if (cmd === 'END') cur = { r: root, i: root.length };
      else String(cmd).split('').forEach(ch => { index(); insert(ch); });
      index(); draw();
    }
    ta.addEventListener('keydown', e => {
      const m = { ArrowLeft: 'L', ArrowRight: 'R', ArrowUp: 'U', ArrowDown: 'D', Backspace: 'BS', Home: 'HOME', End: 'END' }[e.key];
      if (m) { e.preventDefault(); key(m); return; }
      if (e.key === 'Tab' && parents.get(cur.r)) { e.preventDefault(); right(); index(); draw(); }
    });
    ta.addEventListener('input', () => {
      const v = ta.value; ta.value = '';
      if (!v) return;
      if (v.length > 1 && /[()^\/√]/.test(v)) { fromPlain(v).forEach(it => { cur.r.splice(cur.i, 0, it); cur.i++; }); index(); draw(); return; }   // pasted
      v.replace(/\*/g, '×').split('').forEach(ch => { if (/[0-9A-Za-z+\-−=<>().,π%^\/√×÷≤≥ ]/.test(ch)) { index(); insert(ch); } });
      index(); draw();
    });
    const focus = () => { ta.focus({ preventScroll: true }); fld.classList.add('on'); };
    ta.addEventListener('focus', () => fld.classList.add('on')); ta.addEventListener('blur', () => fld.classList.remove('on'));
    fld.addEventListener('mousedown', e => {
      e.preventDefault(); focus();
      const hit = e.target.closest && e.target.closest('[data-mq]');
      if (hit) { const [r, k] = reg[+hit.getAttribute('data-mq')] || []; if (r) { const b = hit.getBoundingClientRect(); cur = { r, i: e.clientX < b.left + b.width / 2 ? k - 1 : k }; } }
      else cur = { r: root, i: root.length };
      index(); draw();
    });
    fld.append(view, ta, sr);
    // keypad: the same calculator layout as input(), but each key edits the formula
    const V = (vars.length ? vars : ['x']).slice(0, 3).map(v => [v, v]); while (V.length < 3) V.push(null);
    const keys = [
      ['7', '7'], ['8', '8'], ['9', '9'], ['÷', '÷'], ['(', '('], [')', ')'], ['^2', 'SQ'], ['⌫', 'BS'],
      ['4', '4'], ['5', '5'], ['6', '6'], ['×', '×'], ['()/()', 'FRAC'], ['√()', '√'], ['^()', '^'], ['←', 'L'],
      ['1', '1'], ['2', '2'], ['3', '3'], ['-', '-'], V[0], V[1], V[2], ['→', 'R'],
      ['0', '0'], ['.', '.'], ['=', '='], ['+', '+'], ['π', 'π'], ['↑', 'U'], ['↓', 'D'], ['Clear', 'CLR']];
    const keyTex = { '^2': 'x^{2}', '^()': 'x^{\\square}', '()/()': '\\frac{\\square}{\\square}', '√()': '\\sqrt{\\square}', '×': '\\times', '÷': '\\div', 'π': '\\pi' };
    const pad = document.createElement('div'); pad.className = 'mkpad'; pad.setAttribute('role', 'group'); pad.setAttribute('aria-label', 'Maths keypad');
    keys.forEach(k => {
      if (!k) { const g = document.createElement('span'); g.className = 'mkgap'; pad.append(g); return; }
      const [lab, cmd] = k;
      const b = document.createElement('button'); b.type = 'button'; b.className = 'mkey' + (/^\d$/.test(lab) ? ' num' : /^(L|R|U|D|BS|CLR)$/.test(cmd) ? ' nav' : vars.includes(lab) ? ' var' : ' op');
      if (keyTex[lab] && K()) render(keyTex[lab], b); else b.textContent = lab;
      b.setAttribute('aria-label', { SQ: 'squared', '^': 'power', FRAC: 'fraction', '√': 'square root', '×': 'times', '÷': 'divide', '-': 'minus', L: 'left', R: 'right', U: 'up', D: 'down', BS: 'delete', CLR: 'clear' }[cmd] || lab);
      b.onmousedown = e => e.preventDefault();
      b.onclick = () => { if (!coarse) focus(); key(cmd); };
      pad.append(b);
    });
    const tog = document.createElement('button'); tog.type = 'button'; tog.className = 'mktog'; tog.setAttribute('aria-expanded', 'true');
    render('{}^{-\\times}_{+=}', tog); tog.title = 'Show or hide the maths keypad';
    tog.onclick = () => { pad.hidden = !pad.hidden; tog.setAttribute('aria-expanded', String(!pad.hidden)); if (coarse) ta.setAttribute('inputmode', pad.hidden ? 'text' : 'none'); };
    const rowEl = document.createElement('div'); rowEl.className = 'mxin'; rowEl.append(fld, tog);
    box.append(rowEl, pad);
    index(); draw(); hidden.value = toPlain(root);
    return { el: box, input: hidden, focus, set: v => { root = fromPlain(v); cur = { r: root, i: root.length }; index(); draw(); } };
  }

  const obs = new MutationObserver(ms => { if (!(window.Core && Core.IS_MATHS)) return; ms.forEach(m => m.addedNodes.forEach(typeset)); });
  function start() { obs.observe(document.body, { childList: true, subtree: true }); typeset(document.body); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
  window.AtomicMath = { typeset, tex, render, input, field, toPlain, fromPlain, runs };
})();
