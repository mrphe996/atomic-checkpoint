// Camday maths lesson video engine: builds a 1280×720 animated stage from a timed spec and exposes seek(t)
// so a headless browser can render every frame deterministically (Web Animations are created paused).
(function () {
  const W = 1280, H = 720, INK = '#1B2433', YEL = '#FFD84D', BLUE = '#2F6FEB', RED = '#E0483E', GREEN = '#1F9D61', GREY = '#8A94A6';
  const NS = 'http://www.w3.org/2000/svg';
  const stage = document.getElementById('stage');
  const anims = [];
  const anim = (node, frames, start, dur, opt) => { const a = node.animate(frames, Object.assign({ delay: start * 1000, duration: Math.max(1, dur * 1000), fill: 'both', easing: 'cubic-bezier(.22,.8,.3,1)' }, opt || {})); a.pause(); anims.push(a); return a; };
  const div = (cls, html, css) => { const d = document.createElement('div'); if (cls) d.className = cls; if (html != null) d.innerHTML = html; if (css) Object.assign(d.style, css); return d; };
  const svgEl = (tag, attrs) => { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); return e; };
  const tex = s => s.replace(/\$\$(.+?)\$\$/g, (_, t) => katex.renderToString(t, { throwOnError: false })).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
  // appear: fade + rise; hide: fade out
  const appear = (n, t, d = 0.5, from = 'translateY(18px)') => anim(n, [{ opacity: 0, transform: from }, { opacity: 1, transform: 'none' }], t, d);
  const hide = (n, t, d = 0.35) => anim(n, [{ opacity: 1 }, { opacity: 0 }], t, d, { fill: 'forwards' });

  function header(spec) {
    const h = div('hdr', `<img src="${spec.icon}"><span>${spec.stageLabel}</span><b>Lesson ${spec.lessonId} · ${spec.lessonTitle}</b>`);
    stage.append(h); appear(h, spec.introEnd - 0.4, 0.6, 'translateY(-20px)');
    const bar = div('prog'); stage.append(bar);
    anim(bar, [{ transform: 'scaleX(0)' }, { transform: 'scaleX(1)' }], 0, spec.total, { easing: 'linear' });
  }

  function intro(spec) {
    const box = div('intro'); stage.append(box);
    const logo = div('ilogo', `<img src="${spec.logo}">`); box.append(logo);
    anim(logo, [{ opacity: 0, transform: 'scale(.6) rotate(-6deg)' }, { opacity: 1, transform: 'scale(1.08)' }, { opacity: 1, transform: 'scale(1)' }], 0.2, 1.1);
    const band = div('iband'); box.append(band); anim(band, [{ transform: 'scaleX(0)' }, { transform: 'scaleX(1)' }], 0.9, 0.7);
    const st = div('istage', spec.stageLabel); box.append(st); appear(st, 1.2);
    const tt = div('ititle', `Lesson ${spec.lessonId}<br>${spec.lessonTitle}`); box.append(tt); appear(tt, 1.5, 0.7);
    hide(box, spec.introEnd - 0.4, 0.4);
  }

  // ---------- widgets ----------
  function numline(scene, a, t) {
    const x0 = a.x0 || 120, x1 = a.x1 || 1160, y = a.y || 520, mn = a.min, mx = a.max, sx = v => x0 + (v - mn) / (mx - mn) * (x1 - x0);
    const svg = svgEl('svg', { width: W, height: H, class: 'layer' }); scene.box.append(svg);
    const line = svgEl('line', { x1: x0 - 20, y1: y, x2: x1 + 20, y2: y, stroke: INK, 'stroke-width': 4, 'stroke-linecap': 'round' }); svg.append(line);
    const len = x1 - x0 + 40; line.style.strokeDasharray = len; anim(line, [{ strokeDashoffset: len }, { strokeDashoffset: 0 }], t, 0.8);
    for (let v = mn; v <= mx; v++) {
      const g = svgEl('g', {}); svg.append(g);
      g.append(svgEl('line', { x1: sx(v), y1: y - 10, x2: sx(v), y2: y + 10, stroke: v === 0 ? INK : GREY, 'stroke-width': v === 0 ? 4 : 2 }));
      if (!a.every || v % a.every === 0) { const tx = svgEl('text', { x: sx(v), y: y + 40, 'text-anchor': 'middle', class: 'nlt' + (v === 0 ? ' zero' : '') }); tx.textContent = v < 0 ? '−' + (-v) : v; g.append(tx); }
      appear(g, t + 0.3 + (v - mn) * 0.03, 0.3, 'translateY(6px)');
    }
    scene.nl[a.id] = { svg, sx, y };
  }
  function nlDot(scene, a, t) {
    const n = scene.nl[a.nl], x = n.sx(a.v), c = a.color || BLUE;
    const g = svgEl('g', {}); n.svg.append(g);
    g.append(svgEl('circle', { cx: x, cy: n.y, r: 13, fill: c }));
    if (a.label) { const tx = svgEl('text', { x, y: n.y - 26, 'text-anchor': 'middle', class: 'nll', fill: c }); tx.textContent = a.label; g.append(tx); }
    anim(g, [{ opacity: 0, transform: `translate(0,-30px)` }, { opacity: 1, transform: 'none' }], t, 0.45, { easing: 'cubic-bezier(.3,1.6,.5,1)' });
    if (a.out) hide(g, t + a.out);
  }
  function nlJump(scene, a, t) {
    // an arc from a.from to a.to drawn while a token travels along it; one hop per whole step when a.hops
    const n = scene.nl[a.nl], c = a.color || (a.to >= a.from ? GREEN : RED), xa = n.sx(a.from), xb = n.sx(a.to), y = n.y;
    const dur = a.dur || Math.min(3.2, 0.5 + Math.abs(a.to - a.from) * 0.22), hgt = Math.min(150, 40 + Math.abs(xb - xa) * 0.25);   // always above the line: labels sit below it
    const path = svgEl('path', { d: `M${xa} ${y} Q ${(xa + xb) / 2} ${y - 2 * hgt} ${xb} ${y}`, fill: 'none', stroke: c, 'stroke-width': 5, 'stroke-linecap': 'round' }); n.svg.append(path);
    const L = path.getTotalLength(); path.style.strokeDasharray = L; anim(path, [{ strokeDashoffset: L }, { strokeDashoffset: 0 }], t, dur, { easing: 'ease-in-out' });
    const head = svgEl('path', { d: `M${xb} ${y - 4} l ${xb > xa ? -16 : 16} -14 l 0 22 z`, fill: c }); n.svg.append(head); appear(head, t + dur - 0.1, 0.25, 'scale(.5)');
    const tok = svgEl('circle', { cx: 0, cy: 0, r: 11, fill: '#fff', stroke: c, 'stroke-width': 5 }); n.svg.append(tok);
    const kf = []; for (let i = 0; i <= 24; i++) { const p = path.getPointAtLength(L * i / 24); kf.push({ transform: `translate(${p.x}px,${p.y}px)`, opacity: i ? 1 : 0 }); }
    anim(tok, kf, t, dur, { easing: 'ease-in-out' });
    let tx = null; if (a.label) { tx = svgEl('text', { x: (xa + xb) / 2, y: hgt > 0 ? y - hgt - 14 : y - hgt + 30, 'text-anchor': 'middle', class: 'nll', fill: c }); tx.textContent = a.label; n.svg.append(tx); appear(tx, t + dur * 0.4, 0.4); }
    if (a.out) [path, head, tok, tx].filter(Boolean).forEach(e => hide(e, t + a.out));
  }
  function therm(scene, a, t) {
    // thermometer whose liquid rises/falls through the listed values: a.seq = [[time offset, value], ...]
    const x = a.x || 1050, top = a.top || 150, bot = a.bot || 560, mn = a.min, mx = a.max, sy = v => bot - (v - mn) / (mx - mn) * (bot - top);
    const svg = svgEl('svg', { width: W, height: H, class: 'layer' }); scene.box.append(svg);
    const g = svgEl('g', {}); svg.append(g);
    g.append(svgEl('rect', { x: x - 22, y: top - 20, width: 44, height: bot - top + 40, rx: 22, fill: '#fff', stroke: INK, 'stroke-width': 4 }));
    g.append(svgEl('circle', { cx: x, cy: bot + 40, r: 36, fill: RED, stroke: INK, 'stroke-width': 4 }));
    for (let v = mn; v <= mx; v += (a.step || 2)) {
      g.append(svgEl('line', { x1: x + 22, y1: sy(v), x2: x + 34, y2: sy(v), stroke: INK, 'stroke-width': 2 }));
      const tx = svgEl('text', { x: x + 42, y: sy(v) + 7, class: 'tht' + (v === 0 ? ' zero' : '') }); tx.textContent = (v < 0 ? '−' + (-v) : v) + '°'; g.append(tx);
    }
    const zero = svgEl('line', { x1: x - 60, y1: sy(0), x2: x + 22, y2: sy(0), stroke: BLUE, 'stroke-width': 2, 'stroke-dasharray': '6 6' }); g.append(zero);
    appear(g, t, 0.6, 'translateX(40px)');
    const full = bot + 20 - top, sc = v => (bot + 20 - sy(v)) / full;
    const liq = svgEl('rect', { x: x - 12, y: top, width: 24, height: full, fill: RED }); svg.append(liq);
    liq.style.transformBox = 'fill-box'; liq.style.transformOrigin = 'bottom'; liq.style.transform = `scaleY(${sc(a.seq[0][1])})`;
    anim(liq, [{ opacity: 0 }, { opacity: 1 }], t, 0.6);
    a.seq.forEach(([dt, v], i) => { if (i) anim(liq, [{ transform: `scaleY(${sc(a.seq[i - 1][1])})` }, { transform: `scaleY(${sc(v)})` }], t + dt, 1.2, { fill: 'forwards', easing: 'ease-in-out' }); });
    a.seq.forEach(([dt, v], i) => { const lb = div('thlabel', (v < 0 ? '−' + (-v) : v) + ' °C', { left: (x - 190) + 'px', top: (sy(v) - 24) + 'px' }); scene.box.append(lb); appear(lb, t + dt + (i ? 1.2 : 0.3), 0.4, 'translateX(-20px)'); if (i < a.seq.length - 1) hide(lb, t + a.seq[i + 1][0] + 0.4); });
  }
  function table(scene, a, t) {
    const tb = div('tbl'); Object.assign(tb.style, { left: (a.x || 80) + 'px', top: (a.y || 170) + 'px' });
    tb.innerHTML = `<table><tr>${a.head.map(h => `<th>${tex(h)}</th>`).join('')}</tr>${a.rows.map(r => `<tr>${r.map(c => `<td>${tex(c)}</td>`).join('')}</tr>`).join('')}</table>`;
    scene.box.append(tb); appear(tb.querySelector('tr'), t, 0.4);
    scene.rows[a.id] = [...tb.querySelectorAll('tr')].slice(1); scene.rows[a.id].forEach(r => r.style.opacity = 0);
  }
  function fig(scene, a, t) {
    const g = window.AtomicFig && window.AtomicFig.get(a.fig.kind, a.fig); if (!g) return;
    const d = div('figbox', g.svg, { left: (a.x || 700) + 'px', top: (a.y || 160) + 'px', width: (a.w || 500) + 'px' }); scene.box.append(d); appear(d, t, 0.6, 'scale(.92)');
  }

  // ---------- scenes ----------
  const CHIP = { hook: ['Start here', '#DDEEFF'], recall: ['Remember', '#EDEDED'], idea: ['Key idea', '#FFF1B8'], method: ['Method', '#F1E6F7'], example: ['Worked example', '#FFF1B8'],
    error: ['Spot the mistake', '#DFF4EA'], mistake: ['Common mistake', '#FDE2E2'], life: ['Real life', '#E4F6E4'], summary: ['Key points', '#FFD84D'], pause: ['Pause question', '#FFD84D'] };
  function scene(spec, sc) {
    const box = div('scene'); stage.append(box); const S = { box, nl: {}, rows: {}, items: {}, y: 150 };
    anim(box, [{ opacity: 0 }, { opacity: 1 }], sc.start, 0.35); if (sc.end < spec.total - 0.5) hide(box, sc.end - 0.35);
    if (sc.kind) { const c = CHIP[sc.kind] || ['', '#eee']; const h = div('shead', `<span class="chip" style="background:${c[1]}">${c[0]}</span><h2>${tex(sc.title || '')}</h2>`); box.append(h); appear(h, sc.start + 0.1, 0.5, 'translateX(-30px)'); }
    sc.steps.forEach(st => (st.do || []).forEach(a => {
      const t = st.start + (a.at || 0.15);
      if (a.a === 'text' || a.a === 'big' || a.a === 'math' || a.a === 'note') {
        const n = div('it ' + a.a, tex(a.html), {}); if (a.color) n.style.color = a.color;
        if (a.x != null) Object.assign(n.style, { left: a.x + 'px', top: a.y + 'px' }); else { n.style.left = '80px'; n.style.top = S.y + 'px'; S.y += a.a === 'big' ? 86 : a.a === 'math' ? 70 : 58; }
        if (a.w) n.style.width = a.w + 'px';
        box.append(n); appear(n, t, 0.5, a.from || 'translateY(18px)'); if (a.id) S.items[a.id] = n; if (a.out) hide(n, t + a.out);
      } else if (a.a === 'gap') S.y += a.h || 20;
      else if (a.a === 'reset') S.y = a.y || 150;
      else if (a.a === 'hl') { const n = S.items[a.id]; const r = div('hlbox'); n.append(r); anim(r, [{ opacity: 0, transform: 'scaleX(0)' }, { opacity: 1, transform: 'scaleX(1)' }], t, 0.5); if (a.out) hide(r, t + a.out); }
      else if (a.a === 'strike') { const n = S.items[a.id]; const r = div('strike'); n.append(r); anim(r, [{ transform: 'scaleX(0)' }, { transform: 'scaleX(1)' }], t, 0.5); }
      else if (a.a === 'tick' || a.a === 'cross') { const n = S.items[a.id]; const r = div('mark ' + a.a, a.a === 'tick' ? '✓' : '✗'); n.append(r); anim(r, [{ opacity: 0, transform: 'scale(2.2)' }, { opacity: 1, transform: 'scale(1)' }], t, 0.45, { easing: 'cubic-bezier(.3,1.6,.5,1)' }); }
      else if (a.a === 'fadeout') { hide(S.items[a.id], t); }
      else if (a.a === 'nl') numline(S, a, t);
      else if (a.a === 'dot') nlDot(S, a, t);
      else if (a.a === 'jump') nlJump(S, a, t);
      else if (a.a === 'therm') therm(S, a, t);
      else if (a.a === 'table') table(S, a, t);
      else if (a.a === 'row') appear(S.rows[a.id][a.i], t, 0.45, 'translateX(-24px)');
      else if (a.a === 'fig') fig(S, a, t);
      else if (a.a === 'pausecard') { const bd = div('backdrop'); box.append(bd); anim(bd, [{ opacity: 0 }, { opacity: 1 }], t, 0.4); const n = div('pausecard', `<div class="pc-ic">⏸</div><div><b>Your turn</b><p>${tex(a.html)}</p><small>The video stops so you can answer.</small></div>`); box.append(n); appear(n, t, 0.6, 'scale(.85)'); if (st.next) { hide(n, st.next - 0.3); hide(bd, st.next - 0.3); } }
      else if (a.a === 'emoji') { const n = div('emoji', a.html, { left: a.x + 'px', top: a.y + 'px', fontSize: (a.size || 90) + 'px' }); box.append(n); anim(n, [{ opacity: 0, transform: 'scale(.3) rotate(-20deg)' }, { opacity: 1, transform: 'scale(1.15)' }, { opacity: 1, transform: 'scale(1)' }], t, 0.7); if (a.out) hide(n, t + a.out); }
    }));
  }
  function outro(spec) {
    const box = div('intro'); stage.append(box); anim(box, [{ opacity: 0 }, { opacity: 1 }], spec.outroStart, 0.5);
    const logo = div('ilogo', `<img src="${spec.logo}">`); box.append(logo); appear(logo, spec.outroStart + 0.2, 0.6, 'scale(.8)');
    const t = div('ititle', 'Great work!<br><span style="font-size:30px;font-weight:500">Now practise Lesson ' + spec.lessonId + ' on Camday.</span>'); box.append(t); appear(t, spec.outroStart + 0.6, 0.6);
  }

  window.buildVideo = spec => { intro(spec); spec.scenes.forEach(sc => scene(spec, sc)); header(spec); outro(spec); window.seek(0); return anims.length; };
  // is anything moving at time t? (the progress bar is the only long animation; shortcut: it then advances in half-second steps, fine at 4 px/s)
  window.busy = t => anims.some(a => { const e = a.effect.getTiming(); return e.duration < 30000 && t * 1000 >= e.delay - 80 && t * 1000 <= e.delay + e.duration + 80; });
  window.seek = t => { for (const a of anims) a.currentTime = t * 1000; };
})();
