/* Atomic Education — question engine.
   Renders every question type, collects a response, grades it and gives
   misconception-specific feedback. Content lives in content/unit3.json. */
(function () {
  const Fig = window.AtomicFig;
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  function el(tag, attrs, ...kids) {
    const e = document.createElement(tag);
    for (const k in (attrs || {})) {
      const v = attrs[k];
      if (v == null || v === false) continue;
      if (k === 'class') e.className = v; else if (k === 'html') e.innerHTML = v;
      else if (k.startsWith('on')) e.addEventListener(k.slice(2), v); else e.setAttribute(k, v === true ? '' : v);
    }
    for (const c of kids.flat()) if (c != null && c !== false) e.append(c.nodeType ? c : document.createTextNode(c));
    return e;
  }
  function rng(seedStr) { let h = 2166136261; for (const ch of seedStr) { h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619); } return () => { h ^= h << 13; h ^= h >>> 17; h ^= h << 5; return ((h >>> 0) % 100000) / 100000; }; }
  function shuffle(arr, seed) { const r = rng(seed), a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  const TYPE_VI = { mcq: 'Diagnostic multiple choice', multi: 'Select all that apply', num: 'Calculation', scale: 'Instrument reading', label: 'Label the diagram', order: 'Put in order', match: 'Matching', explain: 'Explain (mark scheme)', grid: 'Classification table', table: 'Data table', graph: 'Plot & read a graph', sim: 'Virtual experiment' };
  const DIFF = { M: 'Medium', H: 'Hard', VH: 'Very hard' };
  const near = (a, b, tol) => Math.abs(a - b) <= Math.max(tol || 0, 1e-9 * Math.max(1, Math.abs(b)));
  const parseNum = s => { if (s == null) return null; const t = String(s).replace(/[×x,\s]/gi, m => m === ',' ? '.' : '').trim(); if (t === '') return null; const v = Number(t); return isFinite(v) ? v : null; };
  const LEN = { 'µm': 0.001, 'mm': 1, 'cm': 10 };

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
        else out.fb.push('Not quite. Write the formula first, substitute the numbers, then check the answer makes sense (should the image be bigger or smaller than the object?).');
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
        q.rows.forEach((row, ri) => row.forEach((c, ci) => { if (c && typeof c === 'object') { tot++; const v = parseNum((r[ri] || {})[ci]); if (v != null && near(v, c.ans, c.tol || 1e-9)) good++; } }));
        out.frac = good / tot; out.ok = good === tot; out.detail = `${good}/${tot} cells correct`;
        if (!out.ok) out.fb.push(q.hint || 'Find the pattern between the columns in the complete rows, then apply it to the blank cells.'); break;
      }
      case 'graph': {
        const want = new Set(q.pts.map(p => p.join(','))), got = new Set((r.pts || []).map(p => p.join(',')));
        let good = 0, extra = 0; got.forEach(k => want.has(k) ? good++ : extra++);
        const plotFrac = Math.max(0, (good - extra) / want.size);
        let fOk = true; if (q.follow) { const o = q.follow.options[r.f]; fOk = !!(o && o.ok); if (o && !o.ok && o.fb) out.fb.push(o.fb); if (r.f == null) out.fb.push('Please answer the question about the trend shown by your graph.'); }
        out.frac = q.follow ? (plotFrac * 0.5 + (fOk ? 0.5 : 0)) : plotFrac; out.ok = plotFrac === 1 && fOk;
        if (plotFrac < 1) out.fb.push(`Correct points: ${good}/${want.size}${extra ? `, ${extra} extra point(s)` : ''}. For each row of the table: go along the x-axis to the value, then up to the y value.`); break;
      }
      case 'sim': {
        const t = r.trials || []; const objs = new Set(t.map(x => x.obj));
        const countsOk = t.length >= 2 && t.every(x => { const exp = Fig.F.SCOPE_COUNT[x.obj]; const v = parseNum(x.count); return v != null && Math.abs(v - exp) <= Math.max(1, exp * 0.2); });
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
  const isTick = q => q.rows.every(r => r.a.length === q.cols.length && r.a.every(a => a === '✓' || a === '✗'));
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
      case 'graph': return 'Points: ' + q.pts.map(p => `(${p[0]}, ${p[1]})`).join(' ') + (q.follow ? ' — ' + q.follow.options.find(o => o.ok).t : '');
      case 'sim': return '×4 ≈ 12 cells, ×10 ≈ 5 cells, ×40 ≈ 1 cell across the line → higher magnification: cells look bigger, fewer fit across the field of view.';
    }
    return '';
  }

  /* ---------------- renderers ---------------- */
  function figureBox(name, opts, extra) {
    const f = Fig.get(name, opts); const box = el('div', { class: 'fig' }); box.innerHTML = f.svg; if (extra) box.append(extra); return { box, f };
  }
  function renderBody(q, host, ctx) {
    const seed = (ctx.seed || 's') + q.id; let resp = ctx.resp != null ? JSON.parse(JSON.stringify(ctx.resp)) : null;
    const changed = () => { ctx.onChange && ctx.onChange(resp); };
    const api = { get: () => resp, lock() { host.classList.add('locked'); host.querySelectorAll('input,select,textarea,button.opt,button.chip,button.mv,button.cell').forEach(x => x.disabled = true); } };
    const W = el('div', { class: 'qbody' }); host.append(W);
    if (q.fig && typeof q.fig === 'object' && q.type !== 'scale') { W.append(figureBox(q.fig.kind, q.fig).box); }
    switch (q.type) {
      case 'mcq': case 'multi': {
        const order = shuffle(q.options.map((_, i) => i), seed); const multi = q.type === 'multi';
        if (multi) resp = resp || [];
        const list = el('div', { class: 'opts', role: multi ? 'group' : 'radiogroup' });
        order.forEach((oi, k) => {
          const b = el('button', { class: 'opt', type: 'button', 'aria-pressed': 'false', 'data-oi': oi },
            el('span', { class: 'key' }, String.fromCharCode(65 + k)), el('span', {}, q.options[oi].t));
          const sync = () => { const on = multi ? resp.includes(oi) : resp === oi; b.classList.toggle('sel', on); b.setAttribute('aria-pressed', on); };
          b.onclick = () => { if (multi) { resp = resp.includes(oi) ? resp.filter(x => x !== oi) : resp.concat(oi); } else resp = oi; list.querySelectorAll('.opt').forEach(x => x._sync()); changed(); };
          b._sync = sync; sync(); list.append(b);
        });
        if (multi) W.append(el('p', { class: 'muted' }, 'Select all the correct answers.'));
        W.append(list); api.markOpts = (g) => list.querySelectorAll('.opt').forEach(b => { const o = q.options[+b.dataset.oi]; if (o.ok) b.classList.add('right'); else if (b.classList.contains('sel')) b.classList.add('wrong'); });
        break;
      }
      case 'num': case 'scale': {
        resp = resp || { v: '', u: q.unit === '×' ? '×' : '' };
        if (q.type === 'scale') {
          const zoomBtn = el('button', { class: 'btn small', type: 'button' }, '🔍 Zoom in on the scale');
          const { box, f } = figureBox(q.fig.kind, q.fig);
          const zoom = el('div', { class: 'zoom', hidden: true }); zoom.innerHTML = f.svg.replace('viewBox="0 0 480 320"', `viewBox="${f.zoom}"`);
          zoomBtn.onclick = () => { zoom.hidden = !zoom.hidden; zoomBtn.textContent = zoom.hidden ? '🔍 Zoom in on the scale' : 'Zoom out'; };
          W.append(el('div', { class: 'scalewrap' }, box, el('div', {}, zoomBtn, zoom)));
        }
        const inp = el('input', { type: 'text', inputmode: 'decimal', class: 'numin', 'aria-label': 'Value', value: resp.v, placeholder: 'value' });
        inp.oninput = () => { resp.v = inp.value; changed(); };
        const row = el('div', { class: 'numrow' }, inp);
        if (q.unit !== '×') {
          const sel = el('select', { 'aria-label': 'Unit' }, el('option', { value: '' }, '– unit –'), ...shuffle(q.units, seed + 'u').map(u => el('option', { value: u }, u)));
          sel.value = resp.u || ''; sel.onchange = () => { resp.u = sel.value; changed(); }; row.append(sel);
        } else row.append(el('span', { class: 'unit' }, '× (no unit)'));
        W.append(row); break;
      }
      case 'label': {
        resp = resp || {}; const keys = Object.keys(q.spots); const labels = shuffle(Object.values(q.spots), seed);
        const { box, f } = figureBox(q.fig, {}); let picked = null;
        const svg = box.querySelector('svg'); const NS = 'http://www.w3.org/2000/svg';
        const pool = el('div', { class: 'chips', role: 'listbox', 'aria-label': 'Labels' });
        const selects = {};
        const redraw = () => {
          svg.querySelectorAll('.spot').forEach(g => { const k = g.dataset.k; g.querySelector('text.lab').textContent = resp[k] ? resp[k] : ''; g.classList.toggle('filled', !!resp[k]); });
          pool.querySelectorAll('.chip').forEach(c => { c.classList.toggle('used', Object.values(resp).includes(c.dataset.l)); c.classList.toggle('picked', picked === c.dataset.l); });
          keys.forEach(k => selects[k].value = resp[k] || '');
        };
        const place = (k, l) => { for (const kk in resp) if (resp[kk] === l) delete resp[kk]; if (l) resp[k] = l; else delete resp[k]; picked = null; redraw(); changed(); };
        keys.forEach((k, i) => {
          const [x, y] = f.a[k]; const g = document.createElementNS(NS, 'g'); g.setAttribute('class', 'spot'); g.dataset.k = k; g.setAttribute('tabindex', '0'); g.setAttribute('role', 'button'); g.setAttribute('aria-label', 'Position ' + (i + 1));
          const lx = x < 240 ? 8 : 472, anchor = x < 240 ? 'start' : 'end';
          g.innerHTML = `<line x1="${x}" y1="${y}" x2="${x < 240 ? x - 6 : x + 6}" y2="${y}" stroke="#0B2545" stroke-width="1.5"/><circle cx="${x}" cy="${y}" r="13" class="dot"/><text x="${x}" y="${y + 5}" text-anchor="middle" class="num">${i + 1}</text><text x="${x}" y="${y + (y > 260 ? -18 : 30)}" text-anchor="middle" class="lab"></text>`;
          const act = () => { if (picked) place(k, picked); else if (resp[k]) place(k, null); };
          g.addEventListener('click', act); g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); act(); } });
          g.addEventListener('dragover', e => e.preventDefault()); g.addEventListener('drop', e => { e.preventDefault(); place(k, e.dataTransfer.getData('text/plain')); });
          svg.append(g);
          selects[k] = el('select', { 'aria-label': 'Label for position ' + (i + 1) }, el('option', { value: '' }, '—'), ...labels.map(l => el('option', { value: l }, l)));
          selects[k].onchange = () => place(k, selects[k].value);
        });
        labels.forEach(l => { const c = el('button', { class: 'chip', type: 'button', draggable: 'true', 'data-l': l }, l); c.onclick = () => { picked = picked === l ? null : l; redraw(); }; c.ondragstart = e => e.dataTransfer.setData('text/plain', l); pool.append(c); });
        W.append(el('p', { class: 'muted' }, 'Tap a label, then tap a number on the diagram (or drag and drop, or choose from the lists below).'), pool, box,
          el('div', { class: 'selgrid' }, ...keys.map((k, i) => el('label', {}, el('b', {}, (i + 1) + '. '), selects[k]))));
        api.markSpots = () => svg.querySelectorAll('.spot').forEach(g => g.classList.add(resp[g.dataset.k] === q.spots[g.dataset.k] ? 'ok' : 'bad'));
        redraw(); break;
      }
      case 'order': {
        if (!resp) { let s = shuffle(q.items, seed); if (s.join() === q.items.join()) s = s.slice().reverse(); resp = s; }
        const ol = el('ol', { class: 'order' });
        const draw = () => { ol.innerHTML = ''; resp.forEach((it, i) => ol.append(el('li', {}, el('span', {}, it),
          el('span', { class: 'mvs' }, el('button', { class: 'mv', type: 'button', 'aria-label': 'Up', disabled: i === 0, onclick: () => { [resp[i - 1], resp[i]] = [resp[i], resp[i - 1]]; draw(); changed(); } }, '▲'),
            el('button', { class: 'mv', type: 'button', 'aria-label': 'Down', disabled: i === resp.length - 1, onclick: () => { [resp[i + 1], resp[i]] = [resp[i], resp[i + 1]]; draw(); changed(); } }, '▼'))))); };
        draw(); W.append(ol); break;
      }
      case 'match': {
        resp = resp || {}; const rights = shuffle(q.pairs.map(p => p.r), seed);
        const tb = el('div', { class: 'match' });
        q.pairs.forEach(p => { const s = el('select', { 'aria-label': p.l }, el('option', { value: '' }, '— choose —'), ...rights.map(r => el('option', { value: r }, r))); s.value = resp[p.l] || ''; s.onchange = () => { resp[p.l] = s.value; changed(); }; tb.append(el('div', { class: 'mrow' }, el('b', {}, p.l), s)); });
        W.append(tb); break;
      }
      case 'explain': {
        const ta = el('textarea', { rows: 5, 'aria-label': 'Your answer', placeholder: 'Write your answer in English (full sentences, use because / so).' }); ta.value = resp || '';
        ta.oninput = () => { resp = ta.value; changed(); }; W.append(ta); break;
      }
      case 'grid': {
        const tick = isTick(q); resp = resp || q.rows.map(() => tick ? q.cols.map(() => '') : ['']);
        const t = el('table', { class: 'grid' }); t.append(el('tr', {}, el('th', {}, ''), ...(tick ? q.cols : ['Choose']).map(c => el('th', {}, c))));
        q.rows.forEach((row, ri) => {
          const tr = el('tr', {}, el('th', { scope: 'row' }, row.l));
          if (tick) q.cols.forEach((c, ci) => { const b = el('button', { class: 'cell', type: 'button', 'aria-label': `${row.l} – ${c}` }, resp[ri][ci] || '·'); b.onclick = () => { const v = resp[ri][ci]; resp[ri][ci] = v === '' ? '✓' : v === '✓' ? '✗' : ''; b.textContent = resp[ri][ci] || '·'; changed(); }; tr.append(el('td', {}, b)); });
          else { const s = el('select', { 'aria-label': row.l }, el('option', { value: '' }, '—'), ...q.cols.map(c => el('option', { value: c }, c))); s.value = resp[ri][0] || ''; s.onchange = () => { resp[ri] = [s.value]; changed(); }; tr.append(el('td', {}, s)); }
          t.append(tr);
        });
        if (tick) W.append(el('p', { class: 'muted' }, 'Tap a cell to change it: · → ✓ (present) → ✗ (absent).'));
        W.append(el('div', { class: 'tablewrap' }, t)); break;
      }
      case 'table': {
        resp = resp || {}; const t = el('table', { class: 'grid' }); t.append(el('tr', {}, ...q.head.map(h => el('th', {}, h))));
        q.rows.forEach((row, ri) => t.append(el('tr', {}, ...row.map((c, ci) => { if (c && typeof c === 'object') { const i = el('input', { type: 'text', inputmode: typeof c.ans === 'string' ? 'text' : 'decimal', class: 'cellin', 'aria-label': `${q.head[ci]} row ${ri + 1}`, value: (resp[ri] || {})[ci] || '' }); i.oninput = () => { (resp[ri] = resp[ri] || {})[ci] = i.value; changed(); }; return el('td', {}, i); } return el('td', {}, c); }))));
        W.append(el('div', { class: 'tablewrap' }, t)); break;
      }
      case 'graph': {
        resp = resp || { pts: [], f: null };
        if (q.table_rows) { const t = el('table', { class: 'grid small' }); t.append(el('tr', {}, el('th', {}, q.x.label), el('th', {}, q.y.label))); q.table_rows.forEach(r => t.append(el('tr', {}, el('td', {}, r[0]), el('td', {}, r[1])))); W.append(t); }
        const X0 = 60, Y0 = 280, Wd = 400, Ht = 250, nx = (q.x.max - q.x.min) / q.x.step, ny = (q.y.max - q.y.min) / q.y.step;
        const px = v => X0 + (v - q.x.min) / (q.x.max - q.x.min) * Wd, py = v => Y0 - (v - q.y.min) / (q.y.max - q.y.min) * Ht;
        const box = el('div', { class: 'fig graph' }); const NS = 'http://www.w3.org/2000/svg';
        let g = ''; for (let i = 0; i <= nx; i++) { const v = q.x.min + i * q.x.step; g += `<line x1="${px(v)}" y1="${Y0}" x2="${px(v)}" y2="${Y0 - Ht}" class="gl"/><text x="${px(v)}" y="${Y0 + 18}" text-anchor="middle" class="tk">${v}</text>`; }
        for (let j = 0; j <= ny; j++) { const v = q.y.min + j * q.y.step; g += `<line x1="${X0}" y1="${py(v)}" x2="${X0 + Wd}" y2="${py(v)}" class="gl"/><text x="${X0 - 8}" y="${py(v) + 4}" text-anchor="end" class="tk">${v}</text>`; }
        box.innerHTML = `<svg viewBox="0 0 480 330" xmlns="${NS}">${g}<line x1="${X0}" y1="${Y0}" x2="${X0 + Wd}" y2="${Y0}" class="ax"/><line x1="${X0}" y1="${Y0}" x2="${X0}" y2="${Y0 - Ht}" class="ax"/><text x="${X0 + Wd / 2}" y="${Y0 + 42}" text-anchor="middle" class="al">${esc(q.x.label)}</text><text transform="translate(16 ${Y0 - Ht / 2}) rotate(-90)" text-anchor="middle" class="al">${esc(q.y.label)}</text><g class="plotted"></g><g class="hit"></g></svg>`;
        const svg = box.querySelector('svg'), plotted = svg.querySelector('.plotted'), hit = svg.querySelector('.hit');
        const draw = () => { plotted.innerHTML = resp.pts.map(p => `<circle cx="${px(p[0])}" cy="${py(p[1])}" r="7" class="pt"/>`).join('') + (resp.pts.length > 1 ? `<polyline points="${resp.pts.slice().sort((a, b) => a[0] - b[0]).map(p => px(p[0]) + ',' + py(p[1])).join(' ')}" class="pl"/>` : ''); };
        for (let i = 0; i <= nx; i++) for (let j = 0; j <= ny; j++) {
          const xv = +(q.x.min + i * q.x.step).toFixed(6), yv = +(q.y.min + j * q.y.step).toFixed(6);
          const c = document.createElementNS(NS, 'circle'); c.setAttribute('cx', px(xv)); c.setAttribute('cy', py(yv)); c.setAttribute('r', 9); c.setAttribute('class', 'hitc'); c.setAttribute('data-p', xv + ',' + yv);
          c.addEventListener('click', () => { const k = xv + ',' + yv; const i2 = resp.pts.findIndex(p => p.join(',') === k); if (i2 >= 0) resp.pts.splice(i2, 1); else resp.pts.push([xv, yv]); draw(); changed(); });
          hit.append(c);
        }
        // keyboard alternative
        const kx = el('input', { type: 'text', inputmode: 'decimal', class: 'numin s', 'aria-label': 'x' }), ky = el('input', { type: 'text', inputmode: 'decimal', class: 'numin s', 'aria-label': 'y' });
        const add = el('button', { class: 'btn small', type: 'button', onclick: () => { const a = parseNum(kx.value), b = parseNum(ky.value); if (a == null || b == null) return; const k = a + ',' + b; if (!resp.pts.some(p => p.join(',') === k)) resp.pts.push([a, b]); draw(); changed(); kx.value = ky.value = ''; } }, 'Add point');
        const clr = el('button', { class: 'btn small ghost', type: 'button', onclick: () => { resp.pts = []; draw(); changed(); } }, 'Clear all');
        W.append(box, el('div', { class: 'numrow' }, el('span', {}, 'Or type: x ='), kx, el('span', {}, 'y ='), ky, add, clr));
        draw();
        if (q.follow) {
          const f = q.follow, fl = el('div', { class: 'opts' }); W.append(el('p', { class: 'qp' }, f.prompt), fl);
          shuffle(f.options.map((_, i) => i), seed + 'f').forEach((oi, k) => { const b = el('button', { class: 'opt', type: 'button', 'data-oi': oi }, el('span', { class: 'key' }, String.fromCharCode(65 + k)), el('span', {}, f.options[oi].t)); b.onclick = () => { resp.f = oi; fl.querySelectorAll('.opt').forEach(x => x.classList.toggle('sel', +x.dataset.oi === oi)); changed(); }; if (resp.f === oi) b.classList.add('sel'); fl.append(b); });
        }
        break;
      }
      case 'sim': {
        resp = resp || { pred: null, trials: [], concl: null }; let cur = 10;
        const view = el('div', { class: 'scope' }); const setView = () => { view.innerHTML = Fig.F.scopeView(cur); objBtns.forEach(b => b.classList.toggle('sel', +b.dataset.o === cur)); mag.textContent = `Eyepiece ×10 · Objective ×${cur} → Total magnification ×${10 * cur}`; };
        const steps = el('ol', { class: 'simsteps' });
        const predOpts = [['more', 'More cells across the field of view'], ['fewer', 'Fewer cells across the field of view'], ['same', 'The same number of cells']];
        const pred = el('div', { class: 'opts' }, ...predOpts.map(([v, t]) => { const b = el('button', { class: 'opt' + (resp.pred === v ? ' sel' : ''), type: 'button' }, t); b.onclick = () => { resp.pred = v; pred.querySelectorAll('.opt').forEach(x => x.classList.remove('sel')); b.classList.add('sel'); changed(); }; return b; }));
        const objBtns = [4, 10, 40].map(o => el('button', { class: 'btn small', type: 'button', 'data-o': o, onclick: () => { cur = o; setView(); } }, '×' + o));
        const mag = el('p', { class: 'muted' });
        const cnt = el('input', { type: 'text', inputmode: 'decimal', class: 'numin s', 'aria-label': 'Number of cells' });
        const rec = el('table', { class: 'grid small' });
        const drawRec = () => { rec.innerHTML = '<tr><th>Trial</th><th>Total magnification</th><th>Cells on the red line</th></tr>' + resp.trials.map((t, i) => `<tr><td>${i + 1}</td><td>×${10 * t.obj}</td><td>${esc(t.count)}</td></tr>`).join(''); };
        const recBtn = el('button', { class: 'btn small', type: 'button', onclick: () => { if (parseNum(cnt.value) == null) { cnt.focus(); return; } resp.trials.push({ obj: cur, count: cnt.value }); cnt.value = ''; drawRec(); changed(); } }, 'Record result');
        const redo = el('button', { class: 'btn small ghost', type: 'button', onclick: () => { resp.trials = []; drawRec(); changed(); } }, 'Start again');
        const conc = el('div', { class: 'opts' }, ...[['fewer', 'Higher magnification → cells look bigger → FEWER cells fit across the field of view.'], ['more', 'Higher magnification → MORE cells fit across the field of view.'], ['same', 'Magnification does not change what we see.']].map(([v, t]) => { const b = el('button', { class: 'opt' + (resp.concl === v ? ' sel' : ''), type: 'button' }, t); b.onclick = () => { resp.concl = v; conc.querySelectorAll('.opt').forEach(x => x.classList.remove('sel')); b.classList.add('sel'); changed(); }; return b; }));
        steps.append(
          el('li', {}, el('b', {}, 'Predict: '), 'If you change from a low-power to a high-power objective lens, what will you see?', pred),
          el('li', {}, el('b', {}, 'Change ONE variable: '), 'choose the objective lens (keep the ×10 eyepiece and the onion epidermis slide the same).', el('div', { class: 'btnrow' }, ...objBtns), mag, view),
          el('li', {}, el('b', {}, 'Observe & record: '), 'count the cells sitting on the red line (estimate and round).', el('div', { class: 'numrow' }, cnt, recBtn, redo), rec),
          el('li', {}, el('b', {}, 'Conclude: '), 'Compare at least 2 trials.', conc));
        W.append(steps); setView(); drawRec(); break;
      }
    }
    return api;
  }

  /* Practice controller: tries, hints, guided reasoning and a twin after two wrong tries. */
  function practice(q, host, o) {
    // o: {rec, save(rec), seed, onDone(rec), mode:'stop'|'ex'}
    const rec = o.rec || {}; rec.tries = rec.tries || 0;
    host.innerHTML = '';
    const head = el('div', { class: 'qhead' }, o.nested ? null : el('code', {}, q.id),
      el('span', { class: 'tag t-' + q.type }, TYPE_VI[q.type] || q.type), el('span', { class: 'tag d-' + q.diff }, DIFF[q.diff] || q.diff), el('span', { class: 'tag' }, q.obj),
      q.adv ? el('span', { class: 'tag adv' }, '* Advanced') : null);
    host.append(head, el('p', { class: 'qp' }, q.prompt.replace(/^\* Advanced\.\s*/, '')));
    if (q.src) host.append(el('p', { class: 'src' }, 'Source: ', el('a', { href: q.src.url, target: '_blank', rel: 'noopener' }, q.src.name)));
    const body = el('div'); host.append(body);
    const api = renderBody(q, body, { seed: o.seed, resp: rec.resp, onChange: r => { rec.resp = r; } });
    const fb = el('div', { class: 'fb', 'aria-live': 'polite' }); const add = (...k) => fb.append(...k.filter(x => x != null && x !== false)); const actions = el('div', { class: 'btnrow' });
    const checkBtn = el('button', { class: 'btn primary shine', type: 'button' }, 'Check answer');
    actions.append(checkBtn); host.append(actions, fb);
    const finish = (msg) => { api.lock(); checkBtn.remove(); o.save(rec); o.onDone && o.onDone(rec, msg); };
    function showSolved(g) {
      fb.className = 'fb ok'; fb.innerHTML = '';
      add(el('b', {}, rec.tries === 1 ? '✓ Spot on!' : '✓ Correct (attempt ' + rec.tries + ').'), g.fb.length && q.type === 'mcq' ? el('p', {}, g.fb[0]) : null,
        q.reason ? el('p', { class: 'reason' }, '💡 ', q.reason) : null,
        q.type === 'explain' ? rubricView(q, g) : null);
      api.markOpts && api.markOpts(); api.markSpots && api.markSpots();
    }
    if (rec.done) { const g = grade(q, rec.resp); if (rec.ok) showSolved(g); else showReveal(g, true); api.lock(); checkBtn.remove(); return; }
    function showReveal(g, quiet) {
      fb.className = 'fb guide'; fb.innerHTML = '';
      if (!quiet && g && g.fb && g.fb.length) add(el('div', { class: 'fb bad' }, ...g.fb.slice(0, 3).map(t => el('p', {}, t))));
      add(el('b', {}, 'Let\'s reason it through step by step'), el('p', { class: 'reason' }, q.reason || q.hint || 'Re-read the question, underline the key words and rule out the wrong answers.'),
        el('p', {}, el('b', {}, 'Answer: '), answerText(q)), q.type === 'explain' ? rubricView(q, g) : null);
      api.markOpts && api.markOpts(); api.markSpots && api.markSpots();
      if (quiet) return;
      if (q.twin) {
        const tw = el('div', { class: 'twin' }); add(el('p', { class: 'muted' }, 'Now try a similar question to make sure you\'ve got it:'), tw);
        const twRec = rec.twin || {}; rec.twin = twRec;
        practice(q.twin, tw, { rec: twRec, seed: o.seed, save: () => o.save(rec), onDone: () => { rec.done = true; o.save(rec); o.onDone && o.onDone(rec); }, nested: true });
      } else {
        add(el('button', { class: 'btn', type: 'button', onclick: () => { rec.done = true; o.save(rec); o.onDone && o.onDone(rec); } }, 'I understand – continue'));
      }
    }
    checkBtn.onclick = () => {
      const g = grade(q, api.get());
      if (!g.answered) { fb.className = 'fb warn'; fb.textContent = g.fb[0] || 'Please answer first.'; return; }
      rec.tries++; rec.resp = api.get();
      o.onCheck && o.onCheck(g, rec);
      if (g.ok) { rec.ok = true; rec.done = true; rec.score = rec.tries === 1 ? 1 : rec.tries === 2 ? 0.5 : 0; showSolved(g); finish(); return; }
      rec.wrong = (rec.wrong || 0) + 1; rec.everWrong = true;
      if (rec.tries >= 2) { rec.score = 0; checkBtn.remove(); api.lock(); showReveal(g); o.save(rec); return; }
      fb.className = 'fb bad'; fb.innerHTML = '';
      add(el('b', {}, g.detail ? `Not all correct yet (${g.detail}).` : 'Not quite.'), ...g.fb.slice(0, 4).map(t => el('p', {}, t)), q.hint ? el('p', { class: 'hint' }, '👉 Hint: ', q.hint) : null,
        el('p', { class: 'muted' }, 'Change your answer, then press “Check answer” again.'));
      checkBtn.textContent = 'Check again'; o.save(rec);
    };
    return rec;
  }
  function rubricView(q, g) {
    return el('div', { class: 'rubric' }, el('b', {}, 'Mark scheme (1 mark per point):'),
      el('ul', {}, ...q.rubric.map((p, i) => el('li', { class: g.hits && g.hits[i] ? 'hit' : '' }, (g.hits && g.hits[i] ? '✓ ' : '○ ') + p.pt))),
      el('p', {}, el('b', {}, 'Model answer: '), q.model));
  }

  window.QE = { el, esc, grade, renderBody, practice, answerText, TYPE_VI, DIFF, shuffle, isTick, parseNum };
})();
