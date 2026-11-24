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
      s += v.length === 1 ? `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${COLS[i % 8]}" stroke="#fff" stroke-width="2"/>`
        : `<path d="M${cx} ${cy} L${p0[0].toFixed(1)} ${p0[1].toFixed(1)} A${r} ${r} 0 ${big} 1 ${p1[0].toFixed(1)} ${p1[1].toFixed(1)} Z" fill="${COLS[i % 8]}" stroke="#fff" stroke-width="2"/>`;
      const m = a0 + a / 2;
      if (o.angles && !(o.hide || []).includes(i)) s += T(cx + r * 0.62 * Math.cos(m), cy + r * 0.62 * Math.sin(m), Math.round(x / tot * 360) + '°', { bold: true, fill: '#fff', size: 13 });
      if (o.angles && (o.hide || []).includes(i)) s += T(cx + r * 0.62 * Math.cos(m), cy + r * 0.62 * Math.sin(m), '?', { bold: true, fill: '#fff', size: 16 });
      key += `<rect x="320" y="${48 + i * 30}" width="18" height="18" rx="3" fill="${COLS[i % 8]}"/>` + T(346, 57 + i * 30, lb[i] || '', { anchor: 'start' });
      a0 = a1;
    });
    if (o.title) s += T(240, 306, o.title, { size: 13, fill: GREY });
    return { svg: W(s + key), a: {} };
  };
})();
