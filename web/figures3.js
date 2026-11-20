/* Atomic Education — mathematics figure library (SVG, viewBox 480×320). Original Atomic artwork drawn from parameters.
   Use in a question as fig: { kind: 'shape', ... }. Each returns { svg, a } like figures.js. */
(function () {
  const AF = window.AtomicFig; if (!AF) return;
  const F = AF.F, INK = '#0B2545', BLUE = '#0149AF', RED = '#C0392B', FILL = '#EAF2FF', GOLD = '#F3BF69', GREY = '#8A94A6';
  let uid = 0;
  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const W = inner => `<svg viewBox="0 0 480 320" xmlns="http://www.w3.org/2000/svg" role="img" font-family="Figtree, Arial, sans-serif">${inner}</svg>`;
  const T = (x, y, s, o = {}) => `<text x="${(+x).toFixed(1)}" y="${(+y).toFixed(1)}" font-size="${o.size || 15}" fill="${o.fill || INK}" text-anchor="${o.anchor || 'middle'}" dominant-baseline="middle" ${o.bold ? 'font-weight="700"' : ''} ${o.italic ? 'font-style="italic"' : ''}>${esc(s)}</text>`;
  const L = (x1, y1, x2, y2, o = {}) => `<line x1="${(+x1).toFixed(1)}" y1="${(+y1).toFixed(1)}" x2="${(+x2).toFixed(1)}" y2="${(+y2).toFixed(1)}" stroke="${o.c || INK}" stroke-width="${o.w || 2}" ${o.dash ? `stroke-dasharray="${o.dash}"` : ''} ${o.m ? `marker-end="url(#${o.m})"` : ''}/>`;
  const arrow = (id, col) => `<defs><marker id="${id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="${col || INK}"/></marker></defs>`;
  // fit a list of points [x,y] (any units, y up) into a box, returning a mapper
  function fit(pts, box = [50, 30, 430, 290]) {
    const xs = pts.map(p => p[0]), ys = pts.map(p => p[1]); const x0 = Math.min(...xs), x1 = Math.max(...xs), y0 = Math.min(...ys), y1 = Math.max(...ys);
    const sc = Math.min((box[2] - box[0]) / ((x1 - x0) || 1), (box[3] - box[1]) / ((y1 - y0) || 1));
    const ox = box[0] + ((box[2] - box[0]) - (x1 - x0) * sc) / 2, oy = box[3] - ((box[3] - box[1]) - (y1 - y0) * sc) / 2;
    return p => [ox + (p[0] - x0) * sc, oy - (p[1] - y0) * sc];
  }
  const angleArc = (P, A, B, r, lab, right) => { // arc at P between rays to A and B
    const a1 = Math.atan2(A[1] - P[1], A[0] - P[0]), a2 = Math.atan2(B[1] - P[1], B[0] - P[0]);
    let d = a2 - a1; while (d <= -Math.PI) d += 2 * Math.PI; while (d > Math.PI) d -= 2 * Math.PI;
    if (right) { const u = [Math.cos(a1), Math.sin(a1)], v = [Math.cos(a2), Math.sin(a2)], k = 14;
      return `<path d="M${P[0] + u[0] * k} ${P[1] + u[1] * k} L${P[0] + (u[0] + v[0]) * k} ${P[1] + (u[1] + v[1]) * k} L${P[0] + v[0] * k} ${P[1] + v[1] * k}" fill="none" stroke="${INK}" stroke-width="1.5"/>`; }
    const s = [P[0] + r * Math.cos(a1), P[1] + r * Math.sin(a1)], e = [P[0] + r * Math.cos(a1 + d), P[1] + r * Math.sin(a1 + d)], mid = a1 + d / 2;
    return `<path d="M${s[0].toFixed(1)} ${s[1].toFixed(1)} A${r} ${r} 0 0 ${d > 0 ? 1 : 0} ${e[0].toFixed(1)} ${e[1].toFixed(1)}" fill="none" stroke="${BLUE}" stroke-width="1.8"/>` + (lab ? T(P[0] + (r + 16) * Math.cos(mid), P[1] + (r + 16) * Math.sin(mid), lab, { size: 14, fill: BLUE, bold: true }) : '');
  };

  // polygon from points (y up); o.v vertex labels, o.s side labels (side i joins point i and i+1), o.ang angle labels, o.right [i…] right angles, o.fill
  F.shape = (o) => {
    const pts = o.pts || [[0, 0], [4, 0], [0, 3]], n = pts.length, map = fit(pts, o.box || [70, 40, 410, 280]), P = pts.map(map);
    const cx = P.reduce((a, p) => a + p[0], 0) / n, cy = P.reduce((a, p) => a + p[1], 0) / n;
    let s = `<polygon points="${P.map(p => p.map(v => v.toFixed(1)).join(',')).join(' ')}" fill="${o.fill || FILL}" stroke="${INK}" stroke-width="2.4"/>`;
    (o.s || []).forEach((lab, i) => { if (!lab) return; const a = P[i], b = P[(i + 1) % n], mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2; const dx = mx - cx, dy = my - cy, d = Math.hypot(dx, dy) || 1; s += T(mx + dx / d * 20, my + dy / d * 18, lab, { size: 15, bold: true }); });
    (o.ang || []).forEach((lab, i) => { if (!lab && !(o.right || []).includes(i)) return; s += angleArc(P[i], P[(i + n - 1) % n], P[(i + 1) % n], 26, lab, (o.right || []).includes(i)); });
    (o.right || []).forEach(i => { if (!(o.ang || [])[i]) s += angleArc(P[i], P[(i + n - 1) % n], P[(i + 1) % n], 26, '', true); });
    (o.v || []).forEach((lab, i) => { if (!lab) return; const dx = P[i][0] - cx, dy = P[i][1] - cy, d = Math.hypot(dx, dy) || 1; s += T(P[i][0] + dx / d * 18, P[i][1] + dy / d * 18, lab, { bold: true, italic: true, size: 16 }); });
    (o.ticks || []).forEach((k, i) => { if (!k) return; const a = P[i], b = P[(i + 1) % n], mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, ang = Math.atan2(b[1] - a[1], b[0] - a[0]) + Math.PI / 2; for (let j = 0; j < k; j++) { const off = (j - (k - 1) / 2) * 6, ux = Math.cos(ang - Math.PI / 2) * off, uy = Math.sin(ang - Math.PI / 2) * off; s += L(mx + ux - Math.cos(ang) * 7, my + uy - Math.sin(ang) * 7, mx + ux + Math.cos(ang) * 7, my + uy + Math.sin(ang) * 7, { w: 1.6 }); } });
    if (o.note) s += T(240, 306, o.note, { size: 13, fill: GREY });
    return { svg: W(s), a: {} };
  };
  // two parallel lines cut by a transversal; o.labels: {a..h: text} at the 8 angle positions (a,b,c,d at top crossing clockwise from top-left)
  F.parallel = (o) => {
    const id = 'pa' + (++uid), y1 = 110, y2 = 220, sl = o.slope || 1.4, x1 = 210, x2 = x1 + (y2 - y1) / sl;
    let s = arrow(id) + L(40, y1, 440, y1, { w: 2.4 }) + L(40, y2, 440, y2, { w: 2.4 }) + L(x1 - 80 / sl, y1 - 80, x2 + 80 / sl, y2 + 80, { w: 2.4 });
    s += `<path d="M120 ${y1 - 5} l8 5 l-8 5 M126 ${y1 - 5} l8 5 l-8 5 M120 ${y2 - 5} l8 5 l-8 5 M126 ${y2 - 5} l8 5 l-8 5" fill="none" stroke="${INK}" stroke-width="2"/>`;
    const pos = (X, Y, k) => { const d = 30; return [[X - d, Y - 14], [X + d * 0.9, Y - 14], [X + d, Y + 16], [X - d * 0.9, Y + 16]][k]; };
    const lab = o.labels || {}; 'abcdefgh'.split('').forEach((c, i) => { if (!lab[c]) return; const [X, Y] = i < 4 ? [x1, y1] : [x2, y2]; const p = pos(X, Y, i % 4); s += T(p[0], p[1], lab[c], { bold: true, fill: BLUE }); });
    return { svg: W(s), a: {} };
  };
  // circle / semicircle / quarter circle / sector with radius or diameter labelled
  F.circle = (o) => {
    const cx = 240, cy = 165, r = 115, part = o.part || 'full', ang = o.angle || 360; let s = '';
    if (part === 'full') s += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${FILL}" stroke="${INK}" stroke-width="2.4"/>`;
    else { const a = part === 'semi' ? 180 : part === 'quarter' ? 90 : ang, e = a * Math.PI / 180; const ex = cx + r * Math.cos(-e), ey = cy + r * Math.sin(-e);
      s += `<path d="M${cx} ${cy} L${cx + r} ${cy} A${r} ${r} 0 ${a > 180 ? 1 : 0} 0 ${ex.toFixed(1)} ${ey.toFixed(1)} Z" fill="${FILL}" stroke="${INK}" stroke-width="2.4"/>`;
      if (part === 'sector' && o.showAngle !== false) s += angleArc([cx, cy], [cx + r, cy], [ex, ey], 30, a + '°'); }
    s += `<circle cx="${cx}" cy="${cy}" r="3.5" fill="${INK}"/>`;
    if (o.d) s += L(cx - r, cy, cx + r, cy, { c: RED, w: 2 }) + T(cx, cy + 18, o.d, { bold: true, fill: RED });
    else if (o.r) s += L(cx, cy, cx + r, cy, { c: RED, w: 2 }) + T(cx + r / 2, cy + 18, o.r, { bold: true, fill: RED });
    if (o.label) s += T(cx, 306, o.label, { size: 13, fill: GREY });
    return { svg: W(s), a: {} };
  };
  // coordinate grid; o.x=[min,max], o.y=[min,max]; o.lines=[{m,c,label}|{x:k}|{y:k}]; o.points=[{x,y,l}]; o.polys=[{pts,l,c}]; o.segs=[[x1,y1,x2,y2]]
  F.coord = (o) => {
    const X = o.x || [-5, 5], Y = o.y || [-5, 5], b = [50, 20, 450, 300];
    const sx = v => b[0] + (v - X[0]) / (X[1] - X[0]) * (b[2] - b[0]), sy = v => b[3] - (v - Y[0]) / (Y[1] - Y[0]) * (b[3] - b[1]);
    const stepX = o.sx || Math.max(1, Math.ceil((X[1] - X[0]) / 16)), stepY = o.sy || Math.max(1, Math.ceil((Y[1] - Y[0]) / 12));
    let s = '';
    for (let v = Math.ceil(X[0] / stepX) * stepX; v <= X[1]; v += stepX) s += L(sx(v), b[1], sx(v), b[3], { w: 0.7, c: '#D6E0EE' }) + (v !== 0 || Y[0] >= 0 ? T(sx(v), Math.min(b[3], Math.max(b[1], sy(Y[0] > 0 ? Y[0] : 0))) + 13, v, { size: 11, fill: GREY }) : '');
    for (let v = Math.ceil(Y[0] / stepY) * stepY; v <= Y[1]; v += stepY) s += L(b[0], sy(v), b[2], sy(v), { w: 0.7, c: '#D6E0EE' }) + (v !== 0 || X[0] >= 0 ? T(Math.min(b[2], Math.max(b[0], sx(X[0] > 0 ? X[0] : 0))) - 10, sy(v), v, { size: 11, fill: GREY, anchor: 'end' }) : '');
    const ax = Math.min(Math.max(0, X[0]), X[1]), ay = Math.min(Math.max(0, Y[0]), Y[1]);
    s += L(b[0], sy(ay), b[2], sy(ay), { w: 1.8 }) + L(sx(ax), b[1], sx(ax), b[3], { w: 1.8 }) + T(b[2] + 10, sy(ay), o.xl || 'x', { italic: true, anchor: 'start' }) + T(sx(ax), b[1] - 10, o.yl || 'y', { italic: true });
    const cols = [BLUE, RED, '#1E8E4E', '#7A4BD1'];
    (o.polys || []).forEach((p, i) => { const c = p.c || cols[i % 4]; s += `<polygon points="${p.pts.map(q => sx(q[0]).toFixed(1) + ',' + sy(q[1]).toFixed(1)).join(' ')}" fill="${c}" fill-opacity=".18" stroke="${c}" stroke-width="2.2"/>`; if (p.l) { const q = p.pts[0]; s += T(sx(q[0]) - 10, sy(q[1]) - 10, p.l, { bold: true, fill: c }); } });
    (o.lines || []).forEach((ln, i) => { const c = ln.col || cols[i % 4]; let a, z;
      if (ln.x != null) { a = [ln.x, Y[0]]; z = [ln.x, Y[1]]; } else if (ln.y != null) { a = [X[0], ln.y]; z = [X[1], ln.y]; }
      else { const f = x => ln.m * x + ln.c; const xs = [X[0], X[1]]; a = [xs[0], f(xs[0])]; z = [xs[1], f(xs[1])];
        const clip = (p, q) => { if (p[1] > Y[1]) return [(Y[1] - ln.c) / ln.m, Y[1]]; if (p[1] < Y[0]) return [(Y[0] - ln.c) / ln.m, Y[0]]; return p; }; a = clip(a, z); z = clip(z, a); }
      s += L(sx(a[0]), sy(a[1]), sx(z[0]), sy(z[1]), { c, w: 2.6, dash: ln.dash ? '7 5' : '' }); if (ln.label) s += T(sx(z[0]) - 8, sy(z[1]) + (z[1] >= Y[1] - 0.01 ? 14 : -12), ln.label, { bold: true, fill: c, anchor: 'end', size: 14 }); });
    (o.segs || []).forEach(g => { s += L(sx(g[0]), sy(g[1]), sx(g[2]), sy(g[3]), { c: INK, w: 2.4 }); });
    (o.points || []).forEach(p => { s += `<circle cx="${sx(p.x)}" cy="${sy(p.y)}" r="4.5" fill="${p.c || RED}"/>` + (p.l ? T(sx(p.x) + 10, sy(p.y) - 12, p.l, { bold: true, anchor: 'start', size: 14 }) : ''); });
    return { svg: W(s), a: {} };
  };
  // number line with an inequality: o.min,o.max; o.from {v, closed}, o.to {v, closed} (omit for an arrow to infinity)
  F.numline = (o) => {
    const mn = o.min != null ? o.min : -5, mx = o.max != null ? o.max : 5, x0 = 50, x1 = 430, y = 170, sx = v => x0 + (v - mn) / (mx - mn) * (x1 - x0), id = 'nl' + (++uid);
    let s = arrow(id) + L(x0 - 20, y, x1 + 20, y, { w: 2 }); for (let v = mn; v <= mx; v++) s += L(sx(v), y - 7, sx(v), y + 7, { w: 1.5 }) + T(sx(v), y + 24, v, { size: 13 });
    const a = o.from, b = o.to, yy = y - 34;
    if (a || b) { const xa = a ? sx(a.v) : x0 - 20, xb = b ? sx(b.v) : x1 + 20; s += L(xa, yy, xb, yy, { c: BLUE, w: 4, m: (!b ? id : '') }) + (!a ? `<path d="M${x0 - 14} ${yy - 6} l-10 6 l10 6" fill="${BLUE}"/>` : '');
      [a, b].forEach(p => { if (!p) return; s += `<circle cx="${sx(p.v)}" cy="${yy}" r="7" fill="${p.closed ? BLUE : '#fff'}" stroke="${BLUE}" stroke-width="3"/>`; }); }
    return { svg: W(s), a: {} };
  };
  // 3D solids: o.solid 'cuboid' | 'triprism' | 'cylinder' | 'pyramid' | 'cone'; o.labels {a,b,c,h,r,l}
  F.solid = (o) => {
    const k = o.solid || 'cuboid', lb = o.labels || {}; let s = '';
    const face = (pts, f) => `<polygon points="${pts.map(p => p.join(',')).join(' ')}" fill="${f}" stroke="${INK}" stroke-width="2.2" stroke-linejoin="round"/>`;
    const hid = (a, b) => L(a[0], a[1], b[0], b[1], { w: 1.5, dash: '5 4', c: GREY });
    if (k === 'cuboid') { s += hid([130, 250], [190, 190]) + hid([190, 190], [370, 190]) + hid([190, 190], [190, 90]) + face([[130, 250], [310, 250], [310, 150], [130, 150]], '#DCE8FB') + face([[130, 150], [190, 90], [370, 90], [310, 150]], '#EEF4FF') + face([[310, 250], [370, 190], [370, 90], [310, 150]], '#C7D9F5');
      s += T(220, 270, lb.a || '', { bold: true }) + T(355, 232, lb.b || '', { bold: true, anchor: 'start' }) + T(112, 200, lb.c || '', { bold: true, anchor: 'end' }); }
    else if (k === 'triprism') { s += hid([120, 250], [200, 180]) + hid([200, 180], [380, 180]) + face([[120, 250], [300, 250], [210, 110]], '#DCE8FB') + face([[300, 250], [380, 180], [290, 40], [210, 110]], '#C7D9F5');
      s += L(210, 110, 210, 250, { dash: '4 3', w: 1.5, c: RED }) + T(222, 190, lb.h || '', { bold: true, fill: RED, anchor: 'start' }) + T(210, 270, lb.a || '', { bold: true }) + T(350, 230, lb.l || '', { bold: true, anchor: 'start' }) + T(150, 175, lb.c || '', { bold: true, anchor: 'end' }); }
    else if (k === 'cylinder') { s += `<path d="M150 80 v170 a90 28 0 0 0 180 0 v-170" fill="#DCE8FB" stroke="${INK}" stroke-width="2.2"/><ellipse cx="240" cy="80" rx="90" ry="28" fill="#EEF4FF" stroke="${INK}" stroke-width="2.2"/><path d="M150 250 a90 28 0 0 1 180 0" fill="none" stroke="${GREY}" stroke-width="1.5" stroke-dasharray="5 4"/>`;
      s += L(240, 80, 330, 80, { c: RED }) + T(285, 66, lb.r || '', { bold: true, fill: RED }) + L(352, 80, 352, 250, { w: 1.2 }) + T(362, 165, lb.h || '', { bold: true, anchor: 'start' }); }
    else if (k === 'pyramid') { s += hid([130, 250], [200, 200]) + hid([200, 200], [350, 200]) + hid([200, 200], [240, 50]) + face([[130, 250], [280, 250], [240, 50]], '#DCE8FB') + face([[280, 250], [350, 200], [240, 50]], '#C7D9F5');
      s += L(240, 50, 240, 225, { dash: '4 3', w: 1.5, c: RED }) + T(250, 160, lb.h || '', { bold: true, fill: RED, anchor: 'start' }) + T(205, 270, lb.a || '', { bold: true }) + T(330, 240, lb.b || '', { bold: true, anchor: 'start' }) + T(170, 140, lb.l || '', { bold: true, anchor: 'end' }); }
    else if (k === 'cone') { s += `<path d="M150 240 L240 50 L330 240" fill="#DCE8FB" stroke="${INK}" stroke-width="2.2"/><ellipse cx="240" cy="240" rx="90" ry="26" fill="#EEF4FF" stroke="${INK}" stroke-width="2.2"/>` + L(240, 50, 240, 240, { dash: '4 3', w: 1.5, c: RED }) + L(240, 240, 330, 240, { c: RED }) + T(250, 150, lb.h || '', { bold: true, fill: RED, anchor: 'start' }) + T(285, 256, lb.r || '', { bold: true, fill: RED }); }
    if (o.note) s += T(240, 306, o.note, { size: 13, fill: GREY });
    return { svg: W(s), a: {} };
  };
  // bearings: o.from {l}, o.to {l}, o.bearing (deg), o.dist label
  F.bearing = (o) => {
    const b = (o.bearing || 60) * Math.PI / 180, A = [170, 210], R = 140, B = [A[0] + R * Math.sin(b), A[1] - R * Math.cos(b)], id = 'br' + (++uid);
    let s = arrow(id) + L(A[0], A[1] + 40, A[0], A[1] - 170, { w: 1.6, m: id }) + T(A[0], A[1] - 182, 'N', { bold: true });
    s += L(A[0], A[1], B[0], B[1], { w: 2.6, c: BLUE }) + `<circle cx="${A[0]}" cy="${A[1]}" r="5" fill="${INK}"/><circle cx="${B[0]}" cy="${B[1]}" r="5" fill="${INK}"/>` + T(A[0] - 14, A[1] + 14, o.from || 'A', { bold: true }) + T(B[0] + 14, B[1] - 10, o.to || 'B', { bold: true });
    if (o.showAngle !== false) { const r = 40, e = [A[0] + r * Math.sin(b), A[1] - r * Math.cos(b)]; s += `<path d="M${A[0]} ${A[1] - r} A${r} ${r} 0 ${b > Math.PI ? 1 : 0} 1 ${e[0].toFixed(1)} ${e[1].toFixed(1)}" fill="none" stroke="${RED}" stroke-width="2"/>` + T(A[0] + 56 * Math.sin(b / 2), A[1] - 56 * Math.cos(b / 2), o.angleLabel || (o.bearing + '°'), { bold: true, fill: RED }); }
    if (o.dist) s += T((A[0] + B[0]) / 2 + 18, (A[1] + B[1]) / 2 + 10, o.dist, { size: 14, anchor: 'start' });
    return { svg: W(s), a: {} };
  };
  // spinner with equal sectors: o.labels ['1','2','3',…], o.colours
  F.spinner = (o) => {
    const lb = o.labels || ['A', 'B', 'C', 'D'], n = lb.length, cx = 240, cy = 160, r = 120, cols = o.colours || ['#DCE8FB', '#FFF1CF', '#DFF3E6', '#F6DDE0', '#EADFF8', '#E3EEF3', '#FCE6D3', '#E8E8E8'];
    let s = ''; lb.forEach((t, i) => { const a1 = (i / n) * 2 * Math.PI - Math.PI / 2, a2 = ((i + 1) / n) * 2 * Math.PI - Math.PI / 2, m = (a1 + a2) / 2;
      s += `<path d="M${cx} ${cy} L${(cx + r * Math.cos(a1)).toFixed(1)} ${(cy + r * Math.sin(a1)).toFixed(1)} A${r} ${r} 0 ${n === 1 ? 1 : 0} 1 ${(cx + r * Math.cos(a2)).toFixed(1)} ${(cy + r * Math.sin(a2)).toFixed(1)} Z" fill="${cols[i % cols.length]}" stroke="${INK}" stroke-width="2"/>` + T(cx + r * 0.65 * Math.cos(m), cy + r * 0.65 * Math.sin(m), t, { bold: true, size: 18 }); });
    s += `<path d="M${cx} ${cy} L${cx + 12} ${cy - 70} L${cx - 4} ${cy - 66} z" fill="${INK}"/><circle cx="${cx}" cy="${cy}" r="8" fill="${GOLD}" stroke="${INK}" stroke-width="2"/>`;
    return { svg: W(s), a: {} };
  };
  // probability tree with two stages: o.a [[label, p], …] first branches; o.b [[label, p], …] second branches (same after each)
  F.tree = (o) => {
    const A = o.a || [['H', '1/2'], ['T', '1/2']], Bb = o.b || A; let s = ''; const x0 = 40, x1 = 190, x2 = 360;
    A.forEach((a, i) => { const ya = 160 + (i - (A.length - 1) / 2) * (280 / A.length); s += L(x0, 160, x1, ya, { w: 2 }) + T((x0 + x1) / 2 - 6, (160 + ya) / 2 - 10, a[1], { size: 13, fill: BLUE, bold: true }) + T(x1 + 14, ya, a[0], { bold: true });
      Bb.forEach((b, j) => { const yb = ya + (j - (Bb.length - 1) / 2) * (280 / A.length / Bb.length) * 0.95; s += L(x1 + 30, ya, x2, yb, { w: 1.6 }) + T((x1 + 30 + x2) / 2, (ya + yb) / 2 - 9, b[1], { size: 12, fill: BLUE, bold: true }) + T(x2 + 14, yb, b[0], { bold: true }) + (o.outcomes ? T(x2 + 40, yb, a[0] + b[0], { size: 12, fill: GREY, anchor: 'start' }) : ''); }); });
    return { svg: W(s), a: {} };
  };
  // stem-and-leaf (back-to-back if o.left given): o.stems [..], o.right [[leaves]], o.left [[leaves]], o.key text
  F.stemleaf = (o) => {
    const st = o.stems || [1, 2, 3], R = o.right || [], Lf = o.left, rowH = Math.min(36, 230 / st.length), x = Lf ? 240 : 150; let s = '';
    st.forEach((v, i) => { const y = 50 + i * rowH; s += T(x, y, v, { bold: true }) + (R[i] ? T(x + 30, y, R[i].join('  '), { anchor: 'start' }) : '') + (Lf && Lf[i] ? T(x - 30, y, Lf[i].slice().reverse().join('  '), { anchor: 'end' }) : ''); });
    s += L(x + 18, 30, x + 18, 50 + st.length * rowH - 16, { w: 2 }) + (Lf ? L(x - 18, 30, x - 18, 50 + st.length * rowH - 16, { w: 2 }) : '');
    if (o.titles) s += T(Lf ? x - 100 : x - 40, 16, o.titles[0] || '', { bold: true, size: 13 }) + T(x + 100, 16, o.titles[1] || '', { bold: true, size: 13 });
    if (o.key) s += T(240, 306, o.key, { size: 13, fill: GREY });
    return { svg: W(s), a: {} };
  };
})();
