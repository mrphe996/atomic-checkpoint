/* Atomic Education — mathematics figures, part 2 (SVG, viewBox 480×320): pie charts and more. Original Atomic artwork drawn from parameters.
   Use in a question as fig: { kind: 'pie', labels: [...], values: [...] }. Each returns { svg, a } like figures.js. */
(function () {
  const AF = window.AtomicFig; if (!AF) return;
  const F = AF.F, INK = '#0B2545', GREY = '#8A94A6';
  const COLS = ['#0149AF', '#F3BF69', '#1E8E4E', '#C0392B', '#7A4BD1', '#2BB3C0', '#E67E22', '#8A94A6'];
  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const W = inner => `<svg viewBox="0 0 480 320" xmlns="http://www.w3.org/2000/svg" role="img" font-family="Figtree, Arial, sans-serif">${inner}</svg>`;
  const T = (x, y, s, o = {}) => `<text x="${(+x).toFixed(1)}" y="${(+y).toFixed(1)}" font-size="${o.size || 14}" fill="${o.fill || INK}" text-anchor="${o.anchor || 'middle'}" dominant-baseline="middle"${o.bold ? ' font-weight="700"' : ''}>${esc(s)}</text>`;
  // pie chart: o.labels, o.values (any positive numbers; angles are drawn in proportion); o.angles true → write each angle; o.hide [i…] → no label for slice i
  F.pie = (o) => {
    const lb = o.labels || [], v = o.values || [], tot = v.reduce((a, b) => a + b, 0) || 1, cx = 170, cy = 160, r = 120; let a0 = -Math.PI / 2, s = '', key = '';
    v.forEach((x, i) => {
      const a = x / tot * 2 * Math.PI, a1 = a0 + a, big = a > Math.PI ? 1 : 0;
      const p0 = [cx + r * Math.cos(a0), cy + r * Math.sin(a0)], p1 = [cx + r * Math.cos(a1), cy + r * Math.sin(a1)];
      const fc = o.shade ? (o.shade.includes(i) ? '#3B7DD8' : '#FFFFFF') : COLS[i % 8], sk = o.shade ? '#1F2A37' : '#fff';
      s += v.length === 1 ? `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fc}" stroke="${sk}" stroke-width="2"/>`
        : `<path d="M${cx} ${cy} L${p0[0].toFixed(1)} ${p0[1].toFixed(1)} A${r} ${r} 0 ${big} 1 ${p1[0].toFixed(1)} ${p1[1].toFixed(1)} Z" fill="${fc}" stroke="${sk}" stroke-width="2"/>`;
      const m = a0 + a / 2;
      if (o.angles && !(o.hide || []).includes(i)) s += T(cx + r * 0.62 * Math.cos(m), cy + r * 0.62 * Math.sin(m), Math.round(x / tot * 360) + '°', { bold: true, fill: '#fff', size: 13 });
      if (o.angles && (o.hide || []).includes(i)) s += T(cx + r * 0.62 * Math.cos(m), cy + r * 0.62 * Math.sin(m), '?', { bold: true, fill: '#fff', size: 16 });
      if (!o.shade) key += `<rect x="320" y="${48 + i * 30}" width="18" height="18" rx="3" fill="${COLS[i % 8]}"/>` + T(346, 57 + i * 30, lb[i] || '', { anchor: 'start' });
      a0 = a1;
    });
    if (o.title) s += T(240, 306, o.title, { size: 13, fill: GREY });
    return { svg: W(o.shade ? `<g transform="translate(70 0)">${s}</g>` : s + key), a: {} };
  };
  // 10 × 10 grid with n squares shaded (percentages)
  F.waffle = (o) => {
    const n = o.n || 0, sz = 26, x0 = 240 - 5 * sz, y0 = 30; let s = '';
    for (let i = 0; i < 100; i++) { const r = Math.floor(i / 10), c = i % 10; s += `<rect x="${x0 + c * sz}" y="${y0 + r * sz}" width="${sz}" height="${sz}" fill="${i < n ? '#3B7DD8' : '#FFFFFF'}" stroke="#1F2A37" stroke-width="1"/>`; }
    if (o.title) s += T(240, 306, o.title, { size: 13, fill: GREY });
    return { svg: W(s), a: {} };
  };
  // angles on a straight line / around a point: o.angles [deg...] in order, o.labels [text...]; o.line draws the base line
  F.anglept = (o) => {
    const cx = 240, cy = o.line ? 230 : 160, R = 150, A = o.angles || [90, 90], lb = o.labels || [];
    let s = o.line ? `<line x1="${cx - 200}" y1="${cy}" x2="${cx + 200}" y2="${cy}" stroke="#1F2A37" stroke-width="3"/>` : '', a0 = o.line ? 0 : (o.start || 0);
    const ray = a => `<line x1="${cx}" y1="${cy}" x2="${(cx + R * Math.cos(a)).toFixed(1)}" y2="${(cy - R * Math.sin(a)).toFixed(1)}" stroke="#1F2A37" stroke-width="3"/>`;
    if (!o.line) s += ray(a0 * Math.PI / 180);
    A.forEach((d, i) => {
      const a1 = a0 + d, r0 = 34 + (i % 3) * 14, m = (a0 + d / 2) * Math.PI / 180, p = x => x * Math.PI / 180;
      s += `<path d="M${(cx + r0 * Math.cos(p(a0))).toFixed(1)} ${(cy - r0 * Math.sin(p(a0))).toFixed(1)} A${r0} ${r0} 0 ${d > 180 ? 1 : 0} 0 ${(cx + r0 * Math.cos(p(a1))).toFixed(1)} ${(cy - r0 * Math.sin(p(a1))).toFixed(1)}" fill="none" stroke="#3B7DD8" stroke-width="2.5"/>`;
      if (i < A.length - 1 || !o.line) s += ray(p(a1));
      s += T(cx + (r0 + 34) * Math.cos(m), cy - (r0 + 34) * Math.sin(m), lb[i] != null ? lb[i] : d + '°', { bold: true, size: 16, fill: '#3B7DD8' });
      a0 = a1;
    });
    s += `<circle cx="${cx}" cy="${cy}" r="4" fill="#1F2A37"/>`;
    return { svg: W(s), a: {} };
  };
  // squares on a grid (nets, patterns): o.cells [[col,row]...], o.cols, o.rows, o.grid (faint background grid), o.mirror {x|y: line position}
  F.cells = (o) => {
    const cs = o.cells || [], C = o.cols || Math.max(...cs.map(c => c[0]), 0) + 1, R = o.rows || Math.max(...cs.map(c => c[1]), 0) + 1;
    const sz = Math.min(400 / C, 280 / R, 60), x0 = 240 - C * sz / 2, y0 = 160 - R * sz / 2; let s = '';
    if (o.grid) for (let i = 0; i < C; i++) for (let j = 0; j < R; j++) s += `<rect x="${x0 + i * sz}" y="${y0 + j * sz}" width="${sz}" height="${sz}" fill="none" stroke="#C9D3E3" stroke-width="1"/>`;
    cs.forEach(([i, j]) => { s += `<rect x="${x0 + i * sz}" y="${y0 + j * sz}" width="${sz}" height="${sz}" fill="#DCE8FB" stroke="#1F2A37" stroke-width="2.4"/>`; });
    if (o.mirror && o.mirror.x != null) s += `<line x1="${x0 + o.mirror.x * sz}" y1="${y0 - 10}" x2="${x0 + o.mirror.x * sz}" y2="${y0 + R * sz + 10}" stroke="#D62F4B" stroke-width="3" stroke-dasharray="8 5"/>`;
    if (o.mirror && o.mirror.y != null) s += `<line x1="${x0 - 10}" y1="${y0 + o.mirror.y * sz}" x2="${x0 + C * sz + 10}" y2="${y0 + o.mirror.y * sz}" stroke="#D62F4B" stroke-width="3" stroke-dasharray="8 5"/>`;
    return { svg: W(s), a: {} };
  };

  // algebra tiles: o.rows [[label, [[kind, count], …], …]]; kind 'x' | 'y' (long rods) or '1' (unit squares); groups joined by '+'
  const TILE = { x: ['#3B7DD8', 'x'], y: ['#1E8E4E', 'y'], '1': ['#F3BF69', '1'], n: ['#D64545', '−1'] };
  function tileRow(groups, x0, y0) {
    let s = '', x = x0;
    groups.forEach((g, gi) => {
      if (gi) { s += T(x + 10, y0 + 22, '+', { size: 22, bold: true }); x += 26; }
      g.forEach(([k, n]) => { const [c, l] = TILE[k] || TILE.x; for (let i = 0; i < n; i++) {
        if (k === 'x' || k === 'y') { s += `<rect x="${x}" y="${y0}" width="18" height="46" rx="3" fill="${c}" stroke="#1F2A37" stroke-width="1.5"/>` + T(x + 9, y0 + 23, l, { size: 13, bold: true, fill: '#fff' }); x += 22; }
        else { s += `<rect x="${x}" y="${y0 + 26}" width="18" height="18" rx="3" fill="${c}" stroke="#1F2A37" stroke-width="1.5"/>` + T(x + 9, y0 + 35, l, { size: 11, bold: true, fill: k === 'n' ? '#fff' : INK }); x += 22; } } });
    });
    return { s, x };
  }
  F.tiles = (o) => {
    const rows = o.rows || []; const h = 64; let s = '';
    rows.forEach(([lab, groups], i) => { const y = 10 + i * h; s += T(8, y + 23, lab, { anchor: 'start', bold: true, size: 15 }); s += tileRow(groups, 120, y).s; });
    const H = 20 + rows.length * h + (o.title ? 22 : 0);
    if (o.title) s += T(240, H - 10, o.title, { size: 13, fill: GREY });
    return { svg: W(s).replace('viewBox="0 0 480 320"', `viewBox="0 0 480 ${H}"`), a: {} };
  };
  // a balance for equations: o.left / o.right as tile groups; level beam
  F.balance = (o) => {
    let s = `<polygon points="240,290 222,316 258,316" fill="#8A94A6"/><line x1="240" y1="120" x2="240" y2="292" stroke="#5B6478" stroke-width="6"/>`;
    s += `<line x1="40" y1="120" x2="440" y2="120" stroke="#1F2A37" stroke-width="6" stroke-linecap="round"/><circle cx="240" cy="120" r="8" fill="#1F2A37"/>`;
    [['left', 120], ['right', 360]].forEach(([k, cx]) => { s += `<line x1="${cx - 70}" y1="120" x2="${cx - 90}" y2="230" stroke="#8A94A6" stroke-width="2"/><line x1="${cx + 70}" y1="120" x2="${cx + 90}" y2="230" stroke="#8A94A6" stroke-width="2"/><path d="M${cx - 100} 230 Q${cx} 270 ${cx + 100} 230 Z" fill="#DCE8FA" stroke="#1F2A37" stroke-width="2"/>`;
      const g = o[k] || []; const w = g.reduce((a, [kk, n]) => a + n * 22, 0); const r = tileRow([g], cx - w / 2, 178); s += r.s; if (o[k + 'Label']) s += T(cx, 292, o[k + 'Label'], { bold: true, size: 15 }); });
    return { svg: W(s), a: {} };
  };
  // analogue clock: o.h (0-23), o.m
  F.clock = (o) => {
    const cx = 240, cy = 160, r = 120, h = (o.h || 0) % 12, m = o.m || 0; let s = `<circle cx="${cx}" cy="${cy}" r="${r}" fill="#FFFFFF" stroke="#1F2A37" stroke-width="4"/>`;
    for (let i = 0; i < 60; i++) { const a = i / 60 * 2 * Math.PI, r0 = i % 5 ? r - 8 : r - 16; s += `<line x1="${cx + r0 * Math.sin(a)}" y1="${cy - r0 * Math.cos(a)}" x2="${cx + (r - 2) * Math.sin(a)}" y2="${cy - (r - 2) * Math.cos(a)}" stroke="#1F2A37" stroke-width="${i % 5 ? 1 : 3}"/>`; }
    for (let i = 1; i <= 12; i++) { const a = i / 12 * 2 * Math.PI; s += T(cx + (r - 34) * Math.sin(a), cy - (r - 34) * Math.cos(a), String(i), { size: 18, bold: true }); }
    const ah = (h + m / 60) / 12 * 2 * Math.PI, am = m / 60 * 2 * Math.PI;
    s += `<line x1="${cx}" y1="${cy}" x2="${cx + 60 * Math.sin(ah)}" y2="${cy - 60 * Math.cos(ah)}" stroke="#1F2A37" stroke-width="8" stroke-linecap="round"/>`;
    s += `<line x1="${cx}" y1="${cy}" x2="${cx + 78 * Math.sin(am)}" y2="${cy - 78 * Math.cos(am)}" stroke="#3B7DD8" stroke-width="5" stroke-linecap="round"/><circle cx="${cx}" cy="${cy}" r="7" fill="#1F2A37"/>`;
    return { svg: W(s), a: {} };
  };
})();
