/* Camday — experiment figure library, part 2 (SVG, viewBox 480×320).
   Every drawing is original Camday artwork, made from parameters so one figure kind serves many questions.
   Use in a question as fig: { kind: 'pondweed', dist: 10, ... }. Each returns { svg, a } like figures.js. */
(function () {
  const AF = window.AtomicFig; if (!AF) return;
  const C = Object.assign({}, AF.C, { water: '#D6ECFF', glass: '#5B6B82', sol: '#CFE3F7', wood: '#C99A5B', sand: '#EAD7A6', ink: '#0B2545', soft: '#F4F7FB', orange: '#F08A4B' });
  let uid = 0;
  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const W = (inner, vb) => `<svg viewBox="${vb || '0 0 480 320'}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="Figtree, Arial, sans-serif">${inner}</svg>`;
  const T = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 13}" fill="${o.fill || C.ink}" text-anchor="${o.anchor || 'middle'}" ${o.bold ? 'font-weight="700"' : ''} ${o.rot ? `transform="rotate(${o.rot} ${x} ${y})"` : ''}>${esc(s)}</text>`;
  const L = (x1, y1, x2, y2, o = {}) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${o.c || C.ink}" stroke-width="${o.w || 2}" ${o.dash ? `stroke-dasharray="${o.dash}"` : ''} ${o.cap ? 'stroke-linecap="round"' : ''} ${o.m ? `marker-end="url(#${o.m})"` : ''}/>`;
  const arrowDef = (id, col) => `<defs><marker id="${id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="${col || C.ink}"/></marker></defs>`;
  const lab = (x, y, s, tx, ty, anchor) => L(x, y, tx, ty, { w: 1.2 }) + T(tx + (anchor === 'end' ? -4 : 4), ty + 4, s, { anchor: anchor || 'start', size: 12 });
  const letter = (x, y, s) => `<circle cx="${x}" cy="${y}" r="11" fill="#fff" stroke="${C.ink}" stroke-width="2"/>` + T(x, y + 4.5, s, { size: 13, bold: true });
  // apparatus pieces
  const beaker = (x, y, w, h, fill, lvl) => `<path d="M${x} ${y} v${h} q0 8 8 8 h${w - 16} q8 0 8 -8 v${-h}" fill="none" stroke="${C.glass}" stroke-width="3"/>` + (fill ? `<path d="M${x + 1.5} ${y + h * (1 - lvl)} v${h * lvl} q0 6.5 6.5 6.5 h${w - 16} q6.5 0 6.5 -6.5 v${-h * lvl}z" fill="${fill}" opacity=".9"/>` : '');
  const flask = (cx, by, s, fill) => { const w = 90 * s, h = 100 * s, n = 22 * s; return `<path d="M${cx - n / 2} ${by - h} v${h * 0.35} L${cx - w / 2} ${by - 4} q0 4 4 4 h${w - 8} q4 0 4 -4 L${cx + n / 2} ${by - h * 0.65} v${-h * 0.35}" fill="none" stroke="${C.glass}" stroke-width="3"/>` + (fill ? `<path d="M${cx - w * 0.36} ${by - h * 0.28} L${cx - w / 2 + 2} ${by - 4} q0 2.5 3 2.5 h${w - 10} q3 0 3 -2.5 L${cx + w * 0.36} ${by - h * 0.28}z" fill="${fill}"/>` : ''); };
  const tube = (x, y, h, fill, lvl, w = 26) => `<path d="M${x} ${y} v${h - w / 2} a${w / 2} ${w / 2} 0 0 0 ${w} 0 v${-(h - w / 2)}" fill="none" stroke="${C.glass}" stroke-width="2.5"/>` + (fill ? `<path d="M${x + 1.5} ${y + h * (1 - lvl)} v${h * lvl - w / 2} a${w / 2 - 1.5} ${w / 2 - 1.5} 0 0 0 ${w - 3} 0 v${-(h * lvl - w / 2)}z" fill="${fill}"/>` : '');
  const bunsen = (cx, by) => `<rect x="${cx - 22}" y="${by - 8}" width="44" height="8" rx="2" fill="${C.ink}"/><rect x="${cx - 7}" y="${by - 58}" width="14" height="50" fill="${C.grey}"/><path d="M${cx} ${by - 60} c-12 -14 -6 -30 0 -42 c6 12 12 28 0 42z" fill="#7DB7FF" opacity=".9"/><path d="M${cx} ${by - 62} c-5 -7 -3 -15 0 -21 c3 6 5 14 0 21z" fill="#1E5FD8"/>`;
  const tripod = (cx, top, by) => `<rect x="${cx - 52}" y="${top - 4}" width="104" height="5" fill="${C.grey}"/>` + L(cx - 44, top, cx - 56, by, { w: 4 }) + L(cx + 44, top, cx + 56, by, { w: 4 }) + `<path d="M${cx - 50} ${top - 4} h100" stroke="#999" stroke-width="2" stroke-dasharray="3 3"/>`;
  const thermo = (x, top, len) => `<rect x="${x - 4}" y="${top}" width="8" height="${len}" rx="4" fill="#fff" stroke="${C.glass}" stroke-width="1.5"/><circle cx="${x}" cy="${top + len + 3}" r="7" fill="${C.red}"/><rect x="${x - 1.5}" y="${top + len * 0.45}" width="3" height="${len * 0.55}" fill="${C.red}"/>`;
  const bench = y => `<rect x="10" y="${y}" width="460" height="10" rx="3" fill="${C.wood}" opacity=".55"/>`;
  const bubbles = (x, y, n, sp) => Array.from({ length: n }, (_, i) => `<circle cx="${x + (i % 2 ? 4 : -3)}" cy="${y - i * (sp || 12)}" r="${2.5 + (i % 3) * 0.8}" fill="#fff" stroke="${C.blue}" stroke-width="1"/>`).join('');
  const lamp = (x, y) => `<path d="M${x} ${y} l-26 -18 h-10 v36 h10 z" fill="${C.gold}" stroke="${C.ink}" stroke-width="2"/><rect x="${x - 70}" y="${y - 6}" width="34" height="12" fill="${C.grey}"/><rect x="${x - 76}" y="${y - 6}" width="8" height="${110}" fill="${C.grey}"/><rect x="${x - 96}" y="${y + 100}" width="48" height="10" fill="${C.ink}"/>` + [[-1, -1], [0, -1.4], [1, -1]].map(([a, b]) => L(x + 6, y + a * 10, x + 26, y + a * 20 + b, { c: C.gold, w: 3, cap: 1 })).join('');
  const F = AF.F;

  /* ---------------- biology ---------------- */
  // pondweed in water under a funnel; gas collected in a test tube or gas syringe; lamp at a distance
  F.pondweed = (o) => {
    const d = o.dist != null ? o.dist : 10, syr = o.collect === 'syringe';
    const s = `${bench(286)}${lamp(80, 196)}
      ${L(84, 270, 236, 270, { w: 1.5 })}${L(84, 264, 84, 276, { w: 1.5 })}${L(236, 264, 236, 276, { w: 1.5 })}${T(160, 262, `distance = ${d} cm`, { size: 13 })}
      ${beaker(236, 120, 150, 158, C.water, 0.85)}
      <path d="M262 266 l26 -50 h40 l26 50" fill="none" stroke="${C.glass}" stroke-width="3"/><rect x="304" y="${syr ? 120 : 96}" width="8" height="${syr ? 96 : 120}" fill="none" stroke="${C.glass}" stroke-width="2.5"/>
      <path d="M300 262 c-10 -20 6 -30 0 -48 M310 262 c14 -18 -6 -32 6 -50 M320 262 c-6 -16 12 -28 2 -46" stroke="${C.dgreen}" stroke-width="4" fill="none"/>
      <path d="M296 240 l-12 -6 M314 230 l12 -8 M322 248 l12 -4 M304 222 l-12 -2" stroke="${C.green}" stroke-width="5" stroke-linecap="round"/>
      ${bubbles(308, 200, 6, 13)}
      ${syr ? `<path d="M308 120 v-30 h52" fill="none" stroke="${C.glass}" stroke-width="3"/><rect x="360" y="78" width="96" height="24" fill="#fff" stroke="${C.glass}" stroke-width="2.5"/><rect x="${360 + (o.vol || 30) / 50 * 90}" y="74" width="6" height="32" fill="${C.grey}"/>${L(366 + (o.vol || 30) / 50 * 90, 90, 470, 90, { w: 3, c: C.grey })}${T(408, 70, 'gas syringe', { size: 12 })}`
        : `<path d="M300 40 v120 a8 8 0 0 0 16 0 v-120" fill="none" stroke="${C.glass}" stroke-width="2.5"/><rect x="302" y="44" width="12" height="${o.gas || 34}" fill="#fff"/><rect x="302" y="${44 + (o.gas || 34)}" width="12" height="${116 - (o.gas || 34)}" fill="${C.water}"/>${T(330, 52, 'gas', { anchor: 'start', size: 12 })}`}
      ${lab(332, 240, 'pondweed', 404, 222)}${lab(248, 160, 'water', 196, 130, 'end')}${lab(346, 222, 'funnel', 404, 196)}`;
    return { svg: W(arrowDef('a' + (++uid)) + s), a: { lamp: [60, 196], weed: [310, 240], gas: [308, 60] } };
  };
  // a leaf, half covered (black paper or foil) or variegated, before/after iodine
  F.leaf = (o) => {
    const mode = o.mode || 'covered', iod = !!o.iodine;
    const path = 'M240 40 C 330 60, 400 150, 240 290 C 80 150, 150 60, 240 40 Z';
    const green = iod ? '#2B2B44' : C.green, pale = iod ? '#C98A3A' : '#E8F3C8';
    let fill = `<path d="${path}" fill="${mode === 'variegated' ? pale : green}" stroke="${C.dgreen}" stroke-width="3"/>`;
    if (mode === 'variegated') fill += `<path d="M240 70 C 300 90, 330 150, 240 250 C 160 160, 190 90, 240 70 Z" fill="${green}"/>`;
    if (mode === 'covered') fill += `<clipPath id="lc${++uid}"><path d="${path}"/></clipPath><rect x="240" y="30" width="200" height="270" fill="${iod ? pale : '#1C1C1C'}" clip-path="url(#lc${uid})" opacity="${iod ? 1 : 0.92}"/>`;
    const labels = mode === 'covered' ? (iod ? lab(170, 150, 'part A (was uncovered)', 30, 60) + lab(310, 170, 'part B (was covered)', 360, 300, 'start') : lab(310, 170, 'black paper', 370, 290)) : lab(250, 150, iod ? 'part A' : 'green part', 380, 60) + lab(190, 220, iod ? 'part B' : 'white part', 60, 290);
    return { svg: W(fill + L(240, 290, 240, 315, { w: 4, c: C.dgreen }) + L(240, 60, 240, 285, { w: 2, c: C.dgreen }) + labels), a: {} };
  };
  // two bell-jar set-ups: plant with a carbon-dioxide absorber vs. water
  F.belljars = (o) => {
    const jar = (cx, lbl, inside) => `<path d="M${cx - 80} 270 v-150 q0 -70 80 -70 q80 0 80 70 v150" fill="${C.soft}" fill-opacity=".4" stroke="${C.glass}" stroke-width="3"/><rect x="${cx - 95}" y="270" width="190" height="8" fill="${C.grey}"/>
      <path d="M${cx - 20} 268 l6 -34 h28 l6 34z" fill="${C.orange}"/><path d="M${cx} 236 c-4 -40 -2 -70 0 -100" stroke="${C.dgreen}" stroke-width="4" fill="none"/><ellipse cx="${cx - 22}" cy="160" rx="22" ry="9" fill="${C.green}" transform="rotate(-25 ${cx - 22} 160)"/><ellipse cx="${cx + 22}" cy="190" rx="22" ry="9" fill="${C.green}" transform="rotate(25 ${cx + 22} 190)"/><ellipse cx="${cx + 18}" cy="140" rx="18" ry="8" fill="${C.green}" transform="rotate(20 ${cx + 18} 140)"/>
      <rect x="${cx + 34}" y="246" width="34" height="22" fill="none" stroke="${C.glass}" stroke-width="2"/><rect x="${cx + 35}" y="252" width="32" height="15" fill="${inside === 'absorber' ? '#E8E8E8' : C.water}"/>
      ${T(cx, 300, lbl, { bold: true })}${lab(cx + 51, 252, inside === 'absorber' ? (o.absorber || 'soda lime') : 'water', cx + 70, 214, 'end')}`;
    return { svg: W(jar(120, o.a || 'Set-up A', 'absorber') + jar(360, o.b || 'Set-up B', 'water')), a: {} };
  };
  // two test tubes with a plant cutting / no plant, water covered by an oil layer
  F.oiltubes = (o) => {
    const one = (x, plant, lbl, lvl) => `${tube(x, 70, 190, C.water, lvl, 44)}<rect x="${x + 2}" y="${70 + 190 * (1 - lvl) - 10}" width="40" height="10" fill="#F6D365"/>${plant ? `<path d="M${x + 22} 250 v-210" stroke="${C.dgreen}" stroke-width="4"/><ellipse cx="${x + 2}" cy="50" rx="22" ry="9" fill="${C.green}" transform="rotate(-20 ${x + 2} 50)"/><ellipse cx="${x + 42}" cy="40" rx="22" ry="9" fill="${C.green}" transform="rotate(20 ${x + 42} 40)"/>` : ''}${T(x + 22, 300, lbl, { bold: true })}`;
    return { svg: W(one(130, false, o.a || 'Set-up A', o.la || 0.8) + one(300, true, o.b || 'Set-up B', o.lb || 0.8) + lab(342, 70 + 190 * (1 - (o.lb || 0.8)) - 5, 'oil', 400, 120) + lab(136, 200, 'water', 60, 230, 'end')), a: {} };
  };
  // the human excretory system with letters
  F.excretory = (o) => {
    const k = (x) => `<path d="M${x} 90 c-38 0 -46 70 -6 84 c14 4 20 -10 14 -22 c-8 -16 -8 -30 4 -42 c8 -10 2 -20 -12 -20z" fill="#B5546E" stroke="#7A2F44" stroke-width="2"/>`;
    const L2 = o.letters !== false;
    return { svg: W(`${k(170)}<g transform="translate(480 0) scale(-1 1)">${k(170)}</g>
      <path d="M184 150 C 200 200, 220 210, 226 236 M296 150 C 280 200, 260 210, 254 236" stroke="#E0B54A" stroke-width="5" fill="none"/>
      <path d="M210 236 q30 -14 60 0 q16 30 -10 46 h-40 q-26 -16 -10 -46z" fill="#F6E3A1" stroke="#B08A2A" stroke-width="2"/><path d="M240 282 v30" stroke="#E0B54A" stroke-width="5"/>
      <path d="M240 20 v280" stroke="${C.red}" stroke-width="7" opacity=".85"/><path d="M226 20 v280" stroke="#3A5BD9" stroke-width="7" opacity=".85"/>
      <path d="M240 120 h-60" stroke="${C.red}" stroke-width="4"/><path d="M226 134 h-48" stroke="#3A5BD9" stroke-width="4"/>
      ${L2 ? letter(120, 130, 'A') + letter(200, 200, 'B') + letter(290, 262, 'C') + letter(262, 306, 'D') + letter(208, 112, 'E') : ''}`), a: { kidney: [120, 130], ureter: [200, 200], bladder: [290, 262], urethra: [262, 306], artery: [208, 112] } };
  };
  // a simple carbon cycle with lettered arrows
  F.carboncycle = () => {
    const id = 'cc' + (++uid);
    const box = (x, y, w, s) => `<rect x="${x}" y="${y}" width="${w}" height="40" rx="10" fill="#fff" stroke="${C.blue}" stroke-width="2.5"/>` + T(x + w / 2, y + 25, s, { bold: true, size: 13 });
    const ar = (x1, y1, x2, y2) => L(x1, y1, x2, y2, { w: 2.5, m: id, c: C.blue });
    return { svg: W(arrowDef(id, C.blue) + box(150, 14, 180, 'carbon dioxide in air') + box(20, 140, 110, 'plants') + box(185, 140, 110, 'animals') + box(350, 140, 110, 'fossil fuels') + box(170, 266, 140, 'dead matter')
      + ar(170, 56, 90, 136) + letter(112, 90, 'A') + ar(110, 140, 190, 58) + letter(166, 104, 'B') + ar(132, 160, 182, 160) + letter(157, 182, 'C')
      + ar(250, 138, 250, 58) + letter(266, 100, 'D') + ar(400, 138, 300, 56) + letter(372, 94, 'E') + ar(80, 182, 184, 276) + ar(240, 182, 240, 262) + ar(234, 284, 412, 182) + letter(330, 240, 'F')), a: {} };
  };
  // Punnett-style grid of sex chromosomes
  F.punnett = (o) => {
    const top = o.top || ['X', 'Y'], left = o.left || ['X', 'X'], cells = o.cells || [['XX', '?'], ['?', '?']];
    let s = `<rect x="160" y="70" width="240" height="200" fill="#fff" stroke="${C.ink}" stroke-width="2"/>` + L(280, 70, 280, 270) + L(160, 170, 400, 170);
    s += T(220, 58, top[0], { bold: true, size: 18 }) + T(340, 58, top[1], { bold: true, size: 18 }) + T(140, 126, left[0], { bold: true, size: 18 }) + T(140, 226, left[1], { bold: true, size: 18 });
    s += T(280, 30, o.topLabel || 'sperm (father)', { size: 13 }) + T(70, 175, o.leftLabel || 'eggs (mother)', { size: 13, rot: -90 });
    [[220, 126], [340, 126], [220, 226], [340, 226]].forEach(([x, y], i) => { s += T(x, y, cells[i >> 1][i & 1], { size: 20, bold: true, fill: cells[i >> 1][i & 1] === '?' ? C.grey : C.blue }); });
    return { svg: W(s), a: {} };
  };

  /* ---------------- chemistry ---------------- */
  // conical flask (with or without cotton wool / bung) on an electronic balance
  F.flaskbalance = (o) => {
    const top = o.bung ? `<rect x="226" y="72" width="28" height="16" rx="3" fill="#7A4A2A"/>` : o.cotton !== false ? `<path d="M226 80 q14 -16 28 0 q-4 10 -14 10 q-10 0 -14 -10z" fill="#fff" stroke="#bbb"/>` : '';
    return { svg: W(`${bench(296)}<rect x="130" y="250" width="220" height="44" rx="6" fill="${C.ink}"/><rect x="150" y="244" width="180" height="8" rx="2" fill="${C.grey}"/><rect x="190" y="262" width="100" height="24" rx="3" fill="#C8F7C5"/>${T(240, 280, o.reading || '0.00 g', { size: 16, bold: true, fill: C.ink })}
      ${flask(240, 244, 1.5, o.fill || C.sol)}${top}${o.solid ? `<path d="M206 236 q34 -10 68 0 v6 h-68z" fill="${o.solid}"/>` : ''}${o.label ? lab(270, 210, o.label, 360, 160) : ''}${o.cotton !== false && !o.bung ? lab(254, 80, 'cotton wool', 330, 60) : ''}`), a: {} };
  };
  // flask with delivery tube to a gas syringe (reading in cm³)
  F.gassyringe = (o) => {
    const max = o.max || 100, v = Math.max(0, Math.min(max, o.vol || 0)), x0 = 250, len = 190, px = x0 + v / max * len;
    let ticks = ''; for (let i = 0; i <= max; i += max / 10) { const x = x0 + i / max * len; ticks += L(x, 108, x, i % (max / 5) === 0 ? 96 : 101, { w: 1 }); if (i % (max / 5) === 0) ticks += T(x, 90, i, { size: 10 }); }
    return { svg: W(`${bench(290)}${flask(120, 290, 1.3, o.fill || C.sol)}<rect x="106" y="148" width="28" height="18" rx="3" fill="#7A4A2A"/><path d="M120 148 v-38 h130" fill="none" stroke="${C.glass}" stroke-width="3"/>
      <rect x="${x0}" y="96" width="${len}" height="28" fill="#fff" stroke="${C.glass}" stroke-width="2.5"/>${ticks}<rect x="${px}" y="92" width="6" height="36" fill="${C.grey}"/>${L(px + 6, 110, px + 60 > 470 ? 470 : px + 60, 110, { w: 4, c: C.grey })}
      ${T(x0 + len / 2, 150, 'gas syringe (cm³)', { size: 12 })}${o.label ? lab(132, 262, o.label, 200, 220) : ''}${o.clamp !== false ? `<rect x="452" y="124" width="10" height="166" fill="${C.grey}"/><rect x="420" y="104" width="40" height="8" fill="${C.grey}"/>` : ''}`), a: {} };
  };
  // gas collected over water in an upturned measuring cylinder
  F.overwater = (o) => {
    const g = o.gas || 30;
    return { svg: W(`${bench(290)}${flask(100, 290, 1.2, o.fill || C.sol)}<rect x="88" y="168" width="24" height="16" rx="3" fill="#7A4A2A"/><path d="M100 168 v-30 h170 v120 h30" fill="none" stroke="${C.glass}" stroke-width="3"/>
      ${beaker(220, 170, 200, 110, C.water, 0.85)}<rect x="290" y="60" width="40" height="200" fill="${C.water}" stroke="${C.glass}" stroke-width="2.5"/><rect x="291.5" y="61.5" width="37" height="${g * 1.6}" fill="#fff"/>
      ${Array.from({ length: 9 }, (_, i) => L(290, 80 + i * 20, 302, 80 + i * 20, { w: 1 })).join('')}${bubbles(310, 250, 4, 14)}${lab(330, 90, 'gas collected', 370, 60)}${lab(296, 230, 'upturned measuring cylinder', 250, 312, 'end')}${o.label ? lab(112, 262, o.label, 40, 120, 'start') : ''}`), a: {} };
  };
  // a row of test tubes: metal strips in solutions, with optional coating / colour change
  F.tubes = (o) => {
    const it = o.items || [], n = it.length || 1, gap = 440 / n;
    let s = `<rect x="20" y="96" width="440" height="12" rx="3" fill="${C.wood}"/>`;
    it.forEach((t, i) => {
      const x = 20 + gap * i + gap / 2 - 15; const fill = t.colour || C.sol;
      s += tube(x, 60, 170, fill, 0.6, 30);
      if (t.metal) s += `<rect x="${x + 11}" y="50" width="8" height="150" fill="${t.metalColour || '#9AA7B5'}"/>` + (t.coat ? `<rect x="${x + 10}" y="140" width="10" height="60" fill="${t.coat === true ? '#B5651D' : t.coat}" opacity=".9"/>` : '');
      if (t.gas) s += bubbles(x + 22, 190, 4, 11);
      s += T(x + 15, 252, t.label || String.fromCharCode(65 + i), { bold: true, size: 15 });
      if (t.metal) s += T(x + 15, 272, t.metal, { size: 11 }); if (t.solution) s += T(x + 15, 288, t.solution, { size: 11 });
      if (t.note) s += T(x + 15, 304, t.note, { size: 11, fill: C.blue });
    });
    return { svg: W(s), a: {} };
  };
  // filtration
  F.filtration = (o) => {
    const Lt = o.letters;
    return { svg: W(`${bench(296)}<rect x="330" y="40" width="10" height="256" fill="${C.grey}"/><rect x="250" y="120" width="90" height="10" fill="${C.grey}"/>
      <path d="M170 90 h140 l-58 70 v40 h-24 v-40z" fill="#fff" stroke="${C.glass}" stroke-width="3"/><path d="M184 98 h112 l-56 62z" fill="#F5F5F0" stroke="#bbb" stroke-dasharray="4 3"/><path d="M200 110 h80 l-40 40z" fill="#B88A55" opacity=".7"/>
      ${beaker(180, 200, 120, 90, C.water, 0.45)}<path d="M240 200 v40" stroke="${C.blue}" stroke-width="3" stroke-dasharray="4 4"/>
      ${Lt ? letter(150, 110, 'A') + letter(120, 150, 'B') + letter(150, 270, 'C') + L(160, 110, 200, 116, { w: 1 }) + L(130, 150, 212, 150, { w: 1 }) + L(160, 270, 200, 270, { w: 1 })
        : lab(220, 116, o.residue || 'residue', 120, 70, 'end') + lab(196, 104, 'filter paper', 100, 110, 'end') + lab(200, 270, o.filtrate || 'filtrate', 110, 250, 'end') + lab(170, 96, 'filter funnel', 110, 160, 'end')}`), a: {} };
  };
  // evaporating dish heated by a Bunsen burner
  F.evaporation = (o) => ({ svg: W(`${bench(296)}${tripod(240, 170, 296)}${bunsen(240, 296)}<path d="M180 166 q60 30 120 0" fill="#fff" stroke="${C.glass}" stroke-width="3"/><path d="M188 168 q52 24 104 0z" fill="${o.fill || C.sol}"/>
    ${o.steam !== false ? '<path d="M220 150 c-8 -12 8 -18 0 -30 M240 146 c-8 -12 8 -18 0 -30 M260 150 c-8 -12 8 -18 0 -30" stroke="#9BB" stroke-width="2" fill="none"/>' : ''}${o.crystals ? '<path d="M210 172 l6 -6 6 6z M236 176 l6 -7 6 7z M262 172 l6 -6 6 6z" fill="#3D7FD0"/>' : ''}
    ${o.letters ? letter(150, 160, 'A') + letter(150, 210, 'B') + letter(300, 250, 'C') + L(160, 160, 186, 166, { w: 1 }) + L(160, 210, 190, 172, { w: 1 }) + L(290, 250, 252, 250, { w: 1 }) : lab(296, 164, 'evaporating dish', 350, 130) + lab(200, 174, 'gauze', 120, 196, 'end') + lab(252, 250, 'Bunsen burner', 330, 250)}`), a: {} });
  // simple distillation
  F.distillation = (o) => {
    const Lt = o.letters;
    return { svg: W(`${bench(296)}${tripod(110, 200, 296)}${bunsen(110, 296)}<circle cx="110" cy="160" r="40" fill="${C.sol}" stroke="${C.glass}" stroke-width="3"/><rect x="100" y="70" width="20" height="56" fill="none" stroke="${C.glass}" stroke-width="3"/>
      ${thermo(110, 36, 60)}<path d="M120 96 L330 176" stroke="${C.glass}" stroke-width="8"/><path d="M160 96 l190 72 v20 l-190 -72z" fill="#E6F3FF" stroke="${C.glass}" stroke-width="2" opacity=".9"/>
      <path d="M180 108 v-26 M318 160 v34" stroke="${C.blue}" stroke-width="4"/>${T(180, 76, 'water out', { size: 11 })}${T(330, 210, 'water in', { size: 11 })}
      <path d="M330 176 l30 12" stroke="${C.glass}" stroke-width="5"/>${beaker(350, 200, 70, 90, C.water, 0.3)}${bubbles(110, 172, 3, 10)}
      ${Lt ? letter(56, 70, 'A') + L(66, 70, 104, 70, { w: 1 }) + letter(40, 160, 'B') + L(50, 160, 70, 160, { w: 1 }) + letter(250, 100, 'C') + L(250, 112, 250, 128, { w: 1 }) + letter(440, 260, 'D') + L(430, 260, 412, 262, { w: 1 })
        : lab(104, 60, 'thermometer', 30, 30, 'start') + lab(78, 172, o.mixture || 'salty water', 20, 230, 'start') + lab(250, 130, 'condenser', 250, 70) + lab(400, 266, o.distillate || 'pure water', 430, 186, 'end')}`), a: {} };
  };
  // paper chromatography: samples (columns of spot heights 0..1), baseline and solvent front
  F.chromatogram = (o) => {
    const samples = o.samples || [], labs = o.labels || samples.map((_, i) => String.fromCharCode(65 + i)), n = samples.length || 1;
    const x0 = 120, x1 = 360, yb = 260, yf = 260 - (o.front || 0.85) * 200, cols = ['#E14E4E', '#2F80ED', '#F2C94C', '#27AE60', '#9B51E0', '#EB8F3C'];
    let s = `<rect x="${x0}" y="40" width="${x1 - x0}" height="250" fill="#fff" stroke="${C.grey}" stroke-width="2"/>${beaker(x0 - 30, 30, x1 - x0 + 60, 262, '#E6F3FF', 0.07)}`;
    s += L(x0 + 6, yb, x1 - 6, yb, { w: 1.5, dash: '6 4', c: '#555' }) + L(x0, yf, x1, yf, { w: 1.2, dash: '2 3', c: C.blue });
    const heights = [...new Set(samples.flat().map(h => Array.isArray(h) ? h[0] : h))].sort();
    samples.forEach((sp, i) => { const x = x0 + (x1 - x0) * (i + 0.5) / n; s += T(x, yb + 22, labs[i], { bold: true }); if (o.showBase !== false) s += `<circle cx="${x}" cy="${yb}" r="3" fill="#555"/>`;
      sp.forEach((h) => { const hh = Array.isArray(h) ? h[0] : h; const c = Array.isArray(h) ? h[1] : cols[heights.indexOf(hh) % cols.length]; s += `<ellipse cx="${x}" cy="${yb - hh * 200}" rx="9" ry="6" fill="${c}"/>`; }); });
    s += lab(x1, yf, 'solvent front', x1 + 22, yf - 14) + lab(x1 - 6, yb, 'pencil line', x1 + 22, yb - 20) + (o.ruler ? Array.from({ length: 11 }, (_, i) => L(x0 - 16, yb - i * 20, x0 - 6, yb - i * 20, { w: 1 }) + (i % 2 === 0 ? T(x0 - 26, yb - i * 20 + 4, i, { size: 10 }) : '')).join('') + T(x0 - 26, 30, 'cm', { size: 10 }) : '');
    return { svg: W(s), a: {} };
  };
  // Bohr model of an atom or ion
  F.atom = (o) => {
    const sh = o.shells || [2, 8, 1], cx = 240, cy = 160, R = [52, 86, 120, 150];
    let s = `<circle cx="${cx}" cy="${cy}" r="30" fill="${C.gold}" stroke="${C.ink}" stroke-width="2"/>` + T(cx, cy - 2, o.p != null ? `${o.p}p` : '', { size: 13, bold: true }) + T(cx, cy + 14, o.n != null ? `${o.n}n` : '', { size: 12 });
    sh.forEach((k, i) => { s += `<circle cx="${cx}" cy="${cy}" r="${R[i]}" fill="none" stroke="${C.grey}" stroke-width="1.5"/>`; for (let j = 0; j < k; j++) { const a = (j / k) * Math.PI * 2 - Math.PI / 2 + i * 0.3; s += `<circle cx="${cx + R[i] * Math.cos(a)}" cy="${cy + R[i] * Math.sin(a)}" r="6" fill="${C.blue}"/>` + T(cx + R[i] * Math.cos(a), cy + R[i] * Math.sin(a) + 4, '−', { size: 11, fill: '#fff', bold: true }); } });
    if (o.ion) s = `<path d="M${cx - 168} 10 h-10 v300 h10 M${cx + 168} 10 h10 v300 h-10" fill="none" stroke="${C.ink}" stroke-width="2.5"/>` + s + T(cx + 196, 26, o.ion, { size: 18, bold: true });
    if (o.title) s += T(60, 30, o.title, { bold: true, anchor: 'start' });
    return { svg: W(s), a: {} };
  };
  // dot-and-cross diagrams of simple molecules (outer shells only)
  F.dotcross = (o) => {
    const mol = o.mol || 'H2O';
    const atom = (x, y, r, sym) => `<circle cx="${x}" cy="${y}" r="${r}" fill="none" stroke="${C.grey}" stroke-width="2"/>` + T(x, y + 6, sym, { size: 20, bold: true });
    const e = (x, y, cross) => cross ? `<path d="M${x - 5} ${y - 5} l10 10 M${x + 5} ${y - 5} l-10 10" stroke="${C.red}" stroke-width="2.5"/>` : `<circle cx="${x}" cy="${y}" r="5" fill="${C.blue}"/>`;
    let s = '';
    if (mol === 'H2' || mol === 'HCl' || mol === 'Cl2') {
      const L1 = mol === 'Cl2' ? 'Cl' : 'H', L2 = mol === 'H2' ? 'H' : 'Cl', r1 = L1 === 'H' ? 46 : 70, r2 = L2 === 'H' ? 46 : 70; const x1 = 240 - r1 + 18, x2 = 240 + r2 - 18;
      s += atom(x1, 160, r1, L1) + atom(x2, 160, r2, L2) + e(240, 150, false) + e(240, 170, true);
      if (L2 === 'Cl') [[0, -1], [0, 1], [1, 0]].forEach(([a, b], i) => { s += e(x2 + a * (r2 - 8) - (a ? 0 : 6), 160 + b * (r2 - 8), true) + e(x2 + a * (r2 - 8) + (a ? 0 : 6), 160 + b * (r2 - 8) + (a ? 12 : 0), true); });
      if (L1 === 'Cl') [[0, -1], [0, 1], [-1, 0]].forEach(([a, b]) => { s += e(x1 + a * (r1 - 8) - (a ? 0 : 6), 160 + b * (r1 - 8), false) + e(x1 + a * (r1 - 8) + (a ? 0 : 6), 160 + b * (r1 - 8) + (a ? 12 : 0), false); });
    } else {
      const cfg = { H2O: { c: 'O', hs: [[-1, 0.7], [1, 0.7]], lone: 2 }, NH3: { c: 'N', hs: [[-1, 0.5], [1, 0.5], [0, 1]], lone: 1 }, CH4: { c: 'C', hs: [[-1, 0], [1, 0], [0, -1], [0, 1]], lone: 0 } }[mol];
      const R = 62; s += atom(240, 160, R, cfg.c);
      cfg.hs.forEach(([dx, dy]) => { const n = Math.hypot(dx, dy), ux = dx / n, uy = dy / n, hx = 240 + ux * (R + 22), hy = 160 + uy * (R + 22); s += atom(hx, hy, 40, 'H'); const bx = 240 + ux * (R - 6), by = 160 + uy * (R - 6); s += e(bx - uy * 8, by + ux * 8, false) + e(bx + uy * 8, by - ux * 8, true); });
      const free = [[0, -1], [-0.7, -0.7], [0.7, -0.7]].slice(0, cfg.lone); free.forEach(([dx, dy]) => { const n = Math.hypot(dx, dy), ux = dx / n, uy = dy / n, bx = 240 + ux * (R - 10), by = 160 + uy * (R - 10); s += e(bx - uy * 8, by + ux * 8, false) + e(bx + uy * 8, by - ux * 8, false); });
    }
    s += T(30, 300, o.key === false ? '' : `•  electron from ${o.k1 || 'one atom'}    ×  electron from ${o.k2 || 'the other atom'}`, { anchor: 'start', size: 12 });
    return { svg: W(s), a: {} };
  };
  // pH colour chart with an arrow at a value
  F.phchart = (o) => {
    const cols = ['#E52521', '#EE4B2B', '#F47C2C', '#F8A531', '#FBCB3A', '#F2E44A', '#A9D243', '#4CB848', '#2EA67A', '#2394B5', '#2B6CB0', '#3C4FA3', '#4B3A8F', '#5B2D82', '#4A1F6E'];
    let s = cols.map((c, i) => `<rect x="${15 + i * 30}" y="120" width="30" height="60" fill="${c}"/>` + T(30 + i * 30, 200, i, { size: 12 })).join('') + T(60, 100, 'strong acid', { size: 12 }) + T(240, 100, 'neutral', { size: 12 }) + T(420, 100, 'strong alkali', { size: 12 });
    (o.marks || []).forEach(m => { const x = 30 + m.ph * 30; s += L(x, 270, x, 212, { w: 2.5, m: 'ph' + uid }) + T(x, 290, m.label, { bold: true }); });
    return { svg: W(arrowDef('ph' + (uid)) + s), a: {} };
  };

  /* ---------------- physics ---------------- */
  // circuit diagrams with standard symbols. o.type 'series' (o.parts along the loop) or 'parallel' (o.branches: [[parts]..], o.main: [parts])
  const SYM = {
    cell: (x, y) => `${L(x - 30, y, x - 4, y)}${L(x - 4, y - 16, x - 4, y + 16, { w: 3 })}${L(x + 4, y - 8, x + 4, y + 8, { w: 5 })}${L(x + 4, y, x + 30, y)}`,
    battery: (x, y) => `${L(x - 30, y, x - 14, y)}${L(x - 14, y - 16, x - 14, y + 16, { w: 3 })}${L(x - 6, y - 8, x - 6, y + 8, { w: 5 })}${L(x - 6, y, x + 6, y, { dash: '3 3' })}${L(x + 6, y - 16, x + 6, y + 16, { w: 3 })}${L(x + 14, y - 8, x + 14, y + 8, { w: 5 })}${L(x + 14, y, x + 30, y)}`,
    lamp: (x, y) => `${L(x - 30, y, x - 14, y)}<circle cx="${x}" cy="${y}" r="14" fill="#fff" stroke="${C.ink}" stroke-width="2"/>${L(x - 10, y - 10, x + 10, y + 10)}${L(x - 10, y + 10, x + 10, y - 10)}${L(x + 14, y, x + 30, y)}`,
    switch: (x, y) => `${L(x - 30, y, x - 14, y)}<circle cx="${x - 14}" cy="${y}" r="3" fill="${C.ink}"/><circle cx="${x + 14}" cy="${y}" r="3" fill="${C.ink}"/>${L(x - 14, y, x + 12, y - 14)}${L(x + 14, y, x + 30, y)}`,
    closed: (x, y) => `${L(x - 30, y, x + 30, y)}<circle cx="${x - 14}" cy="${y}" r="3" fill="${C.ink}"/><circle cx="${x + 14}" cy="${y}" r="3" fill="${C.ink}"/>`,
    resistor: (x, y) => `${L(x - 30, y, x - 18, y)}<rect x="${x - 18}" y="${y - 8}" width="36" height="16" fill="#fff" stroke="${C.ink}" stroke-width="2"/>${L(x + 18, y, x + 30, y)}`,
    variable: (x, y) => `${L(x - 30, y, x - 18, y)}<rect x="${x - 18}" y="${y - 8}" width="36" height="16" fill="#fff" stroke="${C.ink}" stroke-width="2"/>${L(x - 20, y + 16, x + 22, y - 16, { w: 1.8 })}<path d="M${x + 22} ${y - 16} l-9 2 5 5z" fill="${C.ink}"/>${L(x + 18, y, x + 30, y)}`,
    ammeter: (x, y, t) => `${L(x - 30, y, x - 14, y)}<circle cx="${x}" cy="${y}" r="14" fill="#fff" stroke="${C.ink}" stroke-width="2"/>${T(x, y + 5, 'A', { bold: true, size: 14 })}${L(x + 14, y, x + 30, y)}`,
    voltmeter: (x, y) => `${L(x - 30, y, x - 14, y)}<circle cx="${x}" cy="${y}" r="14" fill="#fff" stroke="${C.ink}" stroke-width="2"/>${T(x, y + 5, 'V', { bold: true, size: 14 })}${L(x + 14, y, x + 30, y)}`,
    buzzer: (x, y) => `${L(x - 30, y, x - 12, y)}${L(x - 12, y, x - 12, y - 12)}${L(x + 12, y, x + 12, y - 12)}<path d="M${x - 16} ${y - 12} a16 16 0 0 1 32 0z" fill="#fff" stroke="${C.ink}" stroke-width="2"/>${L(x + 12, y, x + 30, y)}`,
    motor: (x, y) => `${L(x - 30, y, x - 14, y)}<circle cx="${x}" cy="${y}" r="14" fill="#fff" stroke="${C.ink}" stroke-width="2"/>${T(x, y + 5, 'M', { bold: true, size: 14 })}${L(x + 14, y, x + 30, y)}`,
    wire: (x, y) => L(x - 30, y, x + 30, y),
    gap: (x, y) => `${L(x - 30, y, x - 12, y)}<circle cx="${x - 12}" cy="${y}" r="4" fill="#fff" stroke="${C.ink}" stroke-width="2"/><circle cx="${x + 12}" cy="${y}" r="4" fill="#fff" stroke="${C.ink}" stroke-width="2"/>${L(x + 12, y, x + 30, y)}`
  };
  const LETTERED = { ammeter: 'A', voltmeter: 'V', motor: 'M' };
  const part = (p, x, y, vert) => { const k = typeof p === 'string' ? p : p.k; const lb = typeof p === 'object' && p.l; let g = (SYM[k] || SYM.wire)(x, y); if (vert && LETTERED[k]) g = g.replace(/<text[^>]*>[AVM]<\/text>/, ''); return (vert ? `<g transform="rotate(90 ${x} ${y})">${g}</g>` + (LETTERED[k] ? T(x, y + 5, LETTERED[k], { bold: true, size: 14 }) : '') : g) + (lb ? T(x + (vert ? 30 : 0), y + (vert ? 5 : -22), lb, { size: 13, bold: true, fill: C.blue, anchor: vert ? 'start' : 'middle' }) : ''); };
  F.circuit = (o) => {
    let s = ''; const x0 = 60, x1 = 420, y0 = 60, y1 = 260;
    if ((o.type || 'series') === 'series') {
      const top = o.top || ['cell'], right = o.right || [], bottom = o.bottom || [], left = o.left || [];
      const seg = (list, a, b, fixed, horiz) => { const n = list.length; if (!n) return horiz ? L(a, fixed, b, fixed) : L(fixed, a, fixed, b); let g = ''; const step = (b - a) / n; list.forEach((p, i) => { const c = a + step * (i + 0.5); g += horiz ? part(p, c, fixed) : part(p, fixed, c, true); g += horiz ? L(a + step * i, fixed, c - 30, fixed) + L(c + 30, fixed, a + step * (i + 1), fixed) : L(fixed, a + step * i, fixed, c - 30) + L(fixed, c + 30, fixed, a + step * (i + 1)); }); return g; };
      s += seg(top, x0, x1, y0, true) + seg(right, y0, y1, x1, false) + seg(bottom, x0, x1, y1, true) + seg(left, y0, y1, x0, false);
    } else {
      const br = o.branches || [['lamp'], ['lamp']], main = o.main || ['cell'], n = br.length, ys = br.map((_, i) => y0 + 70 + i * ((y1 - y0 - 40) / Math.max(1, n - 1 || 1)) * (n > 1 ? 1 : 0));
      const yb = n === 1 ? [y0 + 120] : br.map((_, i) => 130 + i * (130 / (n - 1)));
      s += L(x0, y0, x0, yb[n - 1]) + L(x1, y0, x1, yb[n - 1]);
      const ms = (x1 - x0) / main.length; main.forEach((p, i) => { const c = x0 + ms * (i + 0.5); s += part(p, c, y0) + L(x0 + ms * i, y0, c - 30, y0) + L(c + 30, y0, x0 + ms * (i + 1), y0); });
      const mx = 140, bx0 = 140, bx1 = 340; br.forEach((list, j) => { const y = yb[j]; s += L(x0, y, bx0, y) + L(bx1, y, x1, y) + `<circle cx="${x0}" cy="${y}" r="${j < n - 1 ? 4 : 0}" fill="${C.ink}"/><circle cx="${x1}" cy="${y}" r="${j < n - 1 ? 4 : 0}" fill="${C.ink}"/>`; const st = (bx1 - bx0) / list.length; list.forEach((p, i) => { const c = bx0 + st * (i + 0.5); s += part(p, c, y) + L(bx0 + st * i, y, c - 30, y) + L(c + 30, y, bx0 + st * (i + 1), y); }); });
      if (o.pre) { s = s + ''; }
    }
    (o.points || []).forEach(p => { s += `<circle cx="${p.x}" cy="${p.y}" r="5" fill="${C.red}"/>` + T(p.x + (p.dx || 0), p.y + (p.dy || -12), p.l, { size: 13, bold: true, fill: C.red }); });
    return { svg: W(s), a: {} };
  };
  // analogue meter (ammeter / voltmeter / newton meter dial)
  F.meter = (o) => {
    const max = o.max || 1, v = o.value || 0, unit = o.unit || 'A', cx = 240, cy = 230, R = 150, a0 = Math.PI * 0.85, a1 = Math.PI * 0.15;
    const ang = x => a0 - (a0 - a1) * x / max; let s = `<rect x="40" y="40" width="400" height="250" rx="16" fill="#fff" stroke="${C.ink}" stroke-width="3"/>`;
    const step = o.minor || max / 20; for (let x = 0; x <= max + 1e-9; x += step) { const a = ang(x), big = Math.abs(x / (o.major || max / 5) - Math.round(x / (o.major || max / 5))) < 1e-6; s += L(cx + R * Math.cos(a), cy - R * Math.sin(a), cx + (R - (big ? 18 : 9)) * Math.cos(a), cy - (R - (big ? 18 : 9)) * Math.sin(a), { w: big ? 2.5 : 1.2 }); if (big) s += T(cx + (R - 34) * Math.cos(a), cy - (R - 34) * Math.sin(a) + 5, +x.toFixed(3), { size: 13 }); }
    const a = ang(v); s += L(cx, cy, cx + (R - 6) * Math.cos(a), cy - (R - 6) * Math.sin(a), { w: 3, c: C.red, cap: 1 }) + `<circle cx="${cx}" cy="${cy}" r="9" fill="${C.ink}"/>` + T(cx, cy - 40, unit, { size: 26, bold: true });
    return { svg: W(s), a: {} };
  };
  // thermometer reading (vertical scale)
  F.thermometer = (o) => {
    const mn = o.min != null ? o.min : 0, mx = o.max != null ? o.max : 100, v = o.value != null ? o.value : 25, y0 = 280, y1 = 30, x = 240, sc = (y0 - y1) / (mx - mn);
    let s = `<rect x="${x - 12}" y="${y1 - 10}" width="24" height="${y0 - y1 + 20}" rx="12" fill="#fff" stroke="${C.glass}" stroke-width="2"/><circle cx="${x}" cy="${y0 + 18}" r="16" fill="${C.red}"/><rect x="${x - 4}" y="${y0 - (v - mn) * sc}" width="8" height="${(v - mn) * sc + 18}" fill="${C.red}"/>`;
    const minor = o.minor || 1, major = o.major || 10; for (let t = mn; t <= mx + 1e-9; t += minor) { const y = y0 - (t - mn) * sc; const big = Math.abs(t / major - Math.round(t / major)) < 1e-6; s += L(x + 12, y, x + 12 + (big ? 20 : 10), y, { w: big ? 2 : 1 }); if (big) s += T(x + 40, y + 5, t, { size: 13, anchor: 'start' }); }
    return { svg: W(s + T(x + 80, 20, '°C', { size: 16, bold: true })), a: {} };
  };
  // newton meter (spring balance) hanging an object
  F.newtonmeter = (o) => {
    const max = o.max || 10, v = o.value || 0, y0 = 50, y1 = 240, sc = (y1 - y0) / max;
    let s = `<rect x="200" y="20" width="80" height="250" rx="10" fill="#fff" stroke="${C.ink}" stroke-width="3"/><path d="M240 6 v14" stroke="${C.ink}" stroke-width="3"/>`;
    for (let t = 0; t <= max + 1e-9; t += (o.minor || max / 20)) { const y = y0 + t * sc, big = Math.abs(t / (o.major || max / 5) - Math.round(t / (o.major || max / 5))) < 1e-6; s += L(250, y, 250 + (big ? 22 : 12), y, { w: big ? 2 : 1 }); if (big) s += T(232, y + 5, +t.toFixed(2), { size: 12, anchor: 'end' }); }
    const py = y0 + v * sc; s += `<path d="M240 ${y0 - 20} v${py - y0 + 10}" stroke="${C.grey}" stroke-width="3" stroke-dasharray="3 2"/><rect x="226" y="${py - 4}" width="40" height="8" fill="${C.red}"/>` + L(240, py, 240, 300, { w: 2 }) + `<rect x="212" y="292" width="56" height="26" rx="4" fill="${C.blue}"/>` + T(305, 40, 'N', { size: 16, bold: true });
    return { svg: W(s), a: {} };
  };
  // plane mirror with incident ray and normal
  F.mirror = (o) => {
    const i = (o.i != null ? o.i : 40) * Math.PI / 180, id = 'm' + (++uid), cx = 240, cy = 250, R = 190;
    let s = arrowDef(id, C.red) + `<rect x="60" y="250" width="360" height="10" fill="#B9D8F5" stroke="${C.ink}" stroke-width="2"/>` + Array.from({ length: 18 }, (_, k) => L(66 + k * 20, 262, 56 + k * 20, 276, { w: 1.2 })).join('');
    s += L(cx, cy, cx, 40, { dash: '6 5', w: 1.5 }) + T(cx, 32, 'normal', { size: 12 });
    s += L(cx - R * Math.sin(i), cy - R * Math.cos(i), cx - 10 * Math.sin(i), cy - 10 * Math.cos(i), { c: C.red, w: 3, m: id }) + T(cx - R * Math.sin(i) - 6, cy - R * Math.cos(i) - 8, 'incident ray', { size: 12, anchor: 'end' });
    if (o.reflected !== false) s += L(cx, cy, cx + R * Math.sin(i), cy - R * Math.cos(i), { c: C.red, w: 3, m: id });
    if (o.showAngle !== false) s += `<path d="M${cx} ${cy - 60} A60 60 0 0 0 ${cx - 60 * Math.sin(i)} ${cy - 60 * Math.cos(i)}" fill="none" stroke="${C.blue}" stroke-width="2"/>` + T(cx - 34 * Math.sin(i / 2) - 4, cy - 76 * Math.cos(i / 2), o.label || `${o.i != null ? o.i : 40}°`, { size: 13, bold: true, fill: C.blue });
    return { svg: W(s + T(400, 300, 'mirror', { size: 12 })), a: {} };
  };
  // ray through a rectangular glass block
  F.glassblock = (o) => {
    const i = (o.i != null ? o.i : 40) * Math.PI / 180, r = Math.asin(Math.sin(i) / 1.5), id = 'g' + (++uid);
    const x0 = 180, y0 = 120, h = 110, xin = x0 + 40; const xout = xin + h * Math.tan(r);
    let s = arrowDef(id, C.red) + `<rect x="110" y="${y0}" width="260" height="${h}" fill="#DDF0FF" stroke="${C.ink}" stroke-width="2"/>` + T(340, y0 + 20, 'glass', { size: 12 }) + T(340, y0 - 10, 'air', { size: 12 });
    s += L(xin, y0 - 90, xin, y0 + 30, { dash: '6 5', w: 1.3 }) + L(xin - 120 * Math.tan(i), y0 - 120, xin - 4 * Math.tan(i), y0 - 4, { c: C.red, w: 3, m: id });
    if (o.refracted !== false) { s += L(xin, y0, xout, y0 + h, { c: C.red, w: 3 }) + L(xout, y0 + h, xout + 90 * Math.tan(i), y0 + h + 90, { c: C.red, w: 3, m: id }) + L(xout, y0 + h - 30, xout, y0 + h + 70, { dash: '6 5', w: 1.3 }); }
    if (o.letters) s += letter(xin - 70, y0 - 50, 'A') + letter(xin + 34, y0 + 70, 'B') + letter(xout + 70, y0 + h + 40, 'C');
    return { svg: W(s), a: {} };
  };
  // white light dispersed by a prism
  F.prism = (o) => {
    const cols = ['#E52521', '#F47C2C', '#F2E44A', '#4CB848', '#2B6CB0', '#4B3A8F', '#8E44AD'];
    let s = `<path d="M240 50 L340 250 H140 Z" fill="#E7F3FF" stroke="${C.ink}" stroke-width="2"/>` + L(30, 200, 196, 156, { w: 4, c: '#999' }) + T(70, 222, 'white light', { size: 12 });
    cols.forEach((c, k) => { s += L(196, 156, 290, 160 + k * 3, { c, w: 2.5 }) + L(290, 160 + k * 3, 450, 120 + k * 18, { c, w: 3 }); });
    if (o.letters !== false) s += letter(462, 120, 'A') + letter(462, 228, 'B');
    if (o.screen) s += `<rect x="452" y="100" width="8" height="150" fill="${C.grey}"/>`;
    return { svg: W(s), a: {} };
  };
  // oscilloscope traces (waveforms) on a grid; o.traces: [{amp (squares), cycles (in the screen), label}]
  F.waves = (o) => {
    const tr = o.traces || [{ amp: 2, cycles: 2 }], n = tr.length, h = 280 / n, gw = 400;
    let s = ''; tr.forEach((t, k) => {
      const top = 20 + k * h, mid = top + h / 2 - 6, sq = (h - 30) / 6;
      for (let gx = 0; gx <= 20; gx++) s += L(60 + gx * 20, top, 60 + gx * 20, top + h - 20, { w: 0.6, c: '#C9D7EA' }); for (let gy = 0; gy <= 6; gy++) s += L(60, top + gy * sq, 460, top + gy * sq, { w: gy === 3 ? 1.2 : 0.6, c: gy === 3 ? '#7C93B8' : '#C9D7EA' });
      let d = ''; for (let x = 0; x <= gw; x += 2) { const y = mid - (t.amp || 1) * sq * Math.sin((x / gw) * (t.cycles || 1) * Math.PI * 2) + (3 * sq - (h - 20) / 2 + 6); d += (x ? 'L' : 'M') + (60 + x) + ' ' + y.toFixed(1); }
      s += `<path d="${d}" fill="none" stroke="${C.blue}" stroke-width="2.6"/>` + (t.label ? T(30, top + (h - 20) / 2 + 4, t.label, { bold: true, size: 16 }) : '');
    });
    return { svg: W(s), a: {} };
  };
  // see-saw / beam balanced on a pivot with loads at distances (metres)
  F.seesaw = (o) => {
    const len = o.len || 4, sc = 380 / len, cx = 240, y = 170; let s = `<rect x="${cx - 190}" y="${y - 8}" width="380" height="12" rx="3" fill="${C.wood}" stroke="${C.ink}" stroke-width="1.5"/><path d="M${cx - 26} 240 L${cx} ${y + 4} L${cx + 26} 240z" fill="${C.grey}"/>` + bench(240) + T(cx, 266, 'pivot', { size: 12 });
    const load = (side, it) => { const x = cx + side * it.d * sc; s += `<rect x="${x - 22}" y="${y - 50}" width="44" height="42" rx="4" fill="${it.c || C.blue}"/>` + T(x, y - 23, it.w != null ? it.w + ' N' : '?', { size: 13, bold: true, fill: '#fff' }) + L(cx, y + 30, x, y + 30, { w: 1.2 }) + L(x, y + 24, x, y + 36, { w: 1.2 }) + T((cx + x) / 2, y + 48, it.d != null && !it.hideD ? it.d + ' m' : (it.dl || '?'), { size: 12 }); };
    (o.left || []).forEach(it => load(-1, it)); (o.right || []).forEach(it => load(1, it));
    return { svg: W(s), a: {} };
  };
  // cuboid with dimensions (and optional mass on a balance)
  F.cuboid = (o) => {
    const l = o.l || 5, w = o.w || 3, h = o.h || 2, u = o.unit || 'cm';
    const s = `<path d="M130 170 h180 v100 h-180z" fill="${o.colour || '#B8C4D6'}" stroke="${C.ink}" stroke-width="2"/><path d="M130 170 l60 -60 h180 l-60 60z" fill="#D5DEEA" stroke="${C.ink}" stroke-width="2"/><path d="M310 170 l60 -60 v100 l-60 60z" fill="#9FAEC4" stroke="${C.ink}" stroke-width="2"/>`
      + L(130, 292, 310, 292, { w: 1.2 }) + T(220, 310, `${l} ${u}`, { bold: true }) + L(330, 288, 390, 228, { w: 1.2 }) + T(392, 270, `${w} ${u}`, { bold: true, anchor: 'start' }) + L(112, 170, 112, 270, { w: 1.2 }) + T(100, 224, `${h} ${u}`, { bold: true, anchor: 'end' })
      + (o.mass ? T(240, 40, `mass = ${o.mass}`, { size: 15, bold: true, fill: C.blue }) : '');
    return { svg: W(s), a: {} };
  };
  // measuring cylinder before/after an object is lowered in (displacement)
  F.displacement = (o) => {
    const mx = o.max || 100, b = o.before, a = o.after;
    const cyl = (x, v, obj) => { let s = `<rect x="${x}" y="40" width="60" height="230" fill="none" stroke="${C.glass}" stroke-width="2.5"/><rect x="${x - 14}" y="270" width="88" height="10" rx="3" fill="${C.glass}"/>`; const y = v2y(v); s += `<rect x="${x + 1.5}" y="${y}" width="57" height="${270 - y}" fill="${C.water}"/>`; for (let t = 0; t <= mx; t += mx / 10) { const yy = v2y(t); s += L(x, yy, x + (t % (mx / 5) === 0 ? 18 : 10), yy, { w: 1 }); if (t % (mx / 5) === 0) s += T(x - 6, yy + 4, t, { size: 11, anchor: 'end' }); } if (obj) s += `<path d="M${x + 30} 10 v${230 - 20}" stroke="#555" stroke-width="1.5"/><path d="M${x + 16} 230 l10 -16 h12 l10 12 l-6 14 h-20z" fill="${o.objColour || '#8C7B6B'}"/>`; return s; };
    const v2y = v => 270 - v / mx * 220;
    return { svg: W(cyl(120, b, false) + cyl(300, a, true) + T(150, 304, 'before', { size: 12 }) + T(330, 304, 'after', { size: 12 }) + T(240, 20, 'cm³', { size: 12 })), a: {} };
  };
  // metal rods heated at one end with pins held on by wax
  F.rods = (o) => {
    const m = o.metals || ['copper', 'iron', 'aluminium'], fallen = o.fallen || m.map(() => 0);
    let s = `<rect x="40" y="40" width="12" height="240" fill="${C.grey}"/>` + bench(282) + bunsen(400, 282);
    m.forEach((name, i) => { const y = 90 + i * 60; s += `<rect x="52" y="${y - 5}" width="370" height="10" rx="4" fill="${['#C46A2B', '#8A8F98', '#C9CED6', '#B8860B'][i % 4]}"/>` + T(140, y - 12, name, { size: 12, anchor: 'start' });
      for (let p = 0; p < 5; p++) { const x = 380 - p * 60; const down = p < fallen[i]; s += down ? `<path d="M${x} ${y + 38} l14 10" stroke="${C.ink}" stroke-width="2.5"/>` : `<circle cx="${x}" cy="${y + 8}" r="4" fill="#F6E3A1"/>${L(x, y + 10, x, y + 30, { w: 2.5 })}`; } });
    s += T(400, 300, 'heat', { size: 12 }); return { svg: W(s), a: {} };
  };
  // cans or cups with thermometers (insulation / colour of surface)
  F.cans = (o) => {
    const it = o.items || [{ label: 'black can', colour: '#222' }, { label: 'white can', colour: '#F4F4F4' }], n = it.length, gap = 440 / n;
    let s = bench(290) + (o.heater ? `<rect x="190" y="10" width="100" height="26" rx="6" fill="${C.ink}"/>` + T(240, 28, 'heat lamp', { size: 12, fill: '#fff' }) : '');
    it.forEach((c, i) => { const x = 20 + gap * i + gap / 2; const w = 70; const lay = c.layers || 0; for (let k = lay; k > 0; k--) s += `<rect x="${x - w / 2 - k * 7}" y="${150 - k * 4}" width="${w + k * 14}" height="${140 + k * 4}" rx="6" fill="${k % 2 ? '#F2E1C2' : '#E5CFA6'}" stroke="#B9965F"/>`;
      s += `<rect x="${x - w / 2}" y="150" width="${w}" height="140" rx="6" fill="${c.colour || '#C9D7EA'}" stroke="${C.ink}" stroke-width="2"/>` + thermo(x, 70, 160) + T(x, 312, c.label || String.fromCharCode(65 + i), { size: 12, bold: true }); if (c.lid) s += `<rect x="${x - w / 2 - 4}" y="142" width="${w + 8}" height="10" rx="3" fill="${C.grey}"/>`; });
    return { svg: W(s), a: {} };
  };
  // beaker on a tripod over a Bunsen burner with a thermometer
  F.heating = (o) => ({ svg: W(`${bench(296)}${tripod(240, 196, 296)}${bunsen(240, 296)}${beaker(185, 100, 110, 92, o.fill || C.water, 0.7)}${o.thermometer !== false ? thermo(250, 40, 130) : ''}${o.stir ? L(222, 60, 236, 186, { w: 3, c: C.grey }) : ''}${o.label ? lab(200, 160, o.label, 110, 130, 'end') : ''}`), a: {} });
  // ball dropped into a tray of sand (crater model)
  F.crater = (o) => ({ svg: W(`${bench(290)}<rect x="120" y="230" width="240" height="60" fill="${C.sand}" stroke="${C.ink}" stroke-width="2"/><path d="M${240 - (o.d || 40)} 230 q${o.d || 40} ${(o.d || 40) * 0.5} ${(o.d || 40) * 2} 0" fill="#C9B37A"/><circle cx="240" cy="70" r="16" fill="${o.colour || '#8A8F98'}"/>
    ${L(80, 70, 80, 230, { w: 1.5 })}${L(72, 70, 88, 70, { w: 1.5 })}${L(72, 230, 88, 230, { w: 1.5 })}${T(70, 150, o.h ? `drop height ${o.h}` : 'drop height', { size: 12, anchor: 'end' })}<rect x="370" y="40" width="14" height="250" fill="#F6E3A1" stroke="${C.ink}"/>${Array.from({ length: 13 }, (_, i) => L(370, 50 + i * 18, 378, 50 + i * 18, { w: 1 })).join('')}
    ${lab(260, 238, 'crater', 420, 220)}${lab(160, 270, 'sand', 60, 290, 'end')}`), a: {} });
  // cross-section of plates: crust over mantle with convection currents
  F.plates = (o) => {
    const id = 'p' + (++uid), div = (o.boundary || 'divergent') === 'divergent';
    let s = arrowDef(id, C.red) + `<rect x="20" y="70" width="440" height="40" fill="#A47148"/><rect x="20" y="110" width="440" height="190" fill="#F4A259" opacity=".55"/>` + T(60, 96, 'crust', { size: 12, fill: '#fff', anchor: 'start' }) + T(60, 290, 'mantle', { size: 12, anchor: 'start' });
    const loop = (sx) => { const k = div ? 1 : -1; const P = (x, y) => [240 + sx * x, y];
      const seg = (a, b) => { const [x1, y1] = P(...a), [x2, y2] = P(...b); return k > 0 ? L(x1, y1, x2, y2, { c: C.red, w: 3, m: id }) : L(x2, y2, x1, y1, { c: C.red, w: 3, m: id }); };
      return seg([12, 270], [12, 140]) + seg([30, 126], [150, 130]) + seg([180, 150], [184, 250]) + seg([160, 276], [40, 284]); };
    s += loop(-1) + loop(1);
    s += div ? `<path d="M232 70 l8 -16 8 16" fill="#E14E4E"/>${L(150, 50, 90, 50, { w: 3, m: id })}${L(330, 50, 390, 50, { w: 3, m: id })}${T(240, 30, o.top || 'plates move apart', { size: 12 })}` : `${L(90, 50, 200, 50, { w: 3, m: id })}${L(390, 50, 280, 50, { w: 3, m: id })}${T(240, 30, o.top || 'plates push together', { size: 12 })}`;
    if (o.letters) s += letter(440, 90, 'A') + letter(440, 200, 'B') + letter(300, 160, 'C');
    return { svg: W(s), a: {} };
  };
  // electromagnet: coil of wire round an iron nail, cells, paper clips picked up
  F.electromagnet = (o) => {
    const turns = o.turns || 10, clips = o.clips || 4; let coil = ''; for (let k = 0; k < turns; k++) { const x = 150 + k * (180 / turns); coil += `<ellipse cx="${x}" cy="150" rx="7" ry="22" fill="none" stroke="#C46A2B" stroke-width="3"/>`; }
    let s = `<rect x="130" y="140" width="230" height="20" rx="4" fill="#8A8F98"/><path d="M360 140 l20 10 -20 10z" fill="#8A8F98"/>${coil}` + `<path d="M150 128 v-70 h60 M330 128 v-70 h-60" fill="none" stroke="${C.ink}" stroke-width="2"/>` + SYM[o.cells > 1 ? 'battery' : 'cell'](240, 58);
    for (let k = 0; k < clips; k++) s += `<rect x="${372 + (k % 2) * 8}" y="${172 + k * 22}" width="14" height="24" rx="6" fill="none" stroke="${C.grey}" stroke-width="2.5"/>`;
    s += T(240, 230, `${turns} turns · ${o.cells || 1} cell${o.cells > 1 ? 's' : ''}`, { size: 13, bold: true }) + lab(200, 160, 'iron nail', 120, 210, 'end');
    return { svg: W(s), a: {} };
  };
  // toy car released from a ramp of height h
  F.ramp = (o) => ({ svg: W(`${bench(280)}<path d="M40 280 L240 280 L40 ${280 - (o.h || 100)}z" fill="${C.wood}" opacity=".7" stroke="${C.ink}" stroke-width="2"/><rect x="50" y="${270 - (o.h || 100)}" width="40" height="18" rx="5" fill="${C.red}" transform="rotate(${Math.atan((o.h || 100) / 200) * 180 / Math.PI} 70 ${280 - (o.h || 100)})"/>
    ${L(26, 280, 26, 280 - (o.h || 100), { w: 1.5 })}${T(20, 280 - (o.h || 100) / 2, 'h', { anchor: 'end', bold: true })}${L(240, 296, 440, 296, { w: 1.5 })}${T(340, 314, o.dl || 'distance travelled', { size: 12 })}<rect x="${240 + (o.d || 150)}" y="262" width="40" height="18" rx="5" fill="${C.red}" opacity=".5"/>`), a: {} });
  // line graph of given data (x/y axes, several series)
  F.linegraph = (o) => {
    const X = o.x || { min: 0, max: 10, step: 2, label: 'x' }, Y = o.y || { min: 0, max: 10, step: 2, label: 'y' }, px0 = 70, px1 = 450, py0 = 270, py1 = 20;
    const sx = v => px0 + (v - X.min) / (X.max - X.min) * (px1 - px0), sy = v => py0 - (v - Y.min) / (Y.max - Y.min) * (py0 - py1);
    let s = ''; for (let v = X.min; v <= X.max + 1e-9; v += X.step) s += L(sx(v), py0, sx(v), py1, { w: 0.6, c: '#D6E0EE' }) + T(sx(v), py0 + 18, +v.toFixed(3), { size: 11 });
    for (let v = Y.min; v <= Y.max + 1e-9; v += Y.step) s += L(px0, sy(v), px1, sy(v), { w: 0.6, c: '#D6E0EE' }) + T(px0 - 8, sy(v) + 4, +v.toFixed(3), { size: 11, anchor: 'end' });
    s += L(px0, py0, px1, py0) + L(px0, py0, px0, py1) + T((px0 + px1) / 2, 314, X.label, { size: 12, bold: true }) + T(16, (py0 + py1) / 2, Y.label, { size: 12, bold: true, rot: -90 });
    const cols = [C.blue, C.red, C.dgreen, C.orange];
    (o.series || []).forEach((sr, k) => { const c = sr.c || cols[k % 4]; if (sr.line !== false) s += `<path d="${sr.pts.map((p, i) => (i ? 'L' : 'M') + sx(p[0]).toFixed(1) + ' ' + sy(p[1]).toFixed(1)).join('')}" fill="none" stroke="${c}" stroke-width="2.5" ${sr.dash ? 'stroke-dasharray="7 5"' : ''}/>`;
      if (sr.dots !== false) sr.pts.forEach(p => { s += `<path d="M${sx(p[0]) - 5} ${sy(p[1]) - 5} l10 10 M${sx(p[0]) + 5} ${sy(p[1]) - 5} l-10 10" stroke="${c}" stroke-width="2"/>`; });
      if (sr.label) { const p = sr.pts[sr.pts.length - 1]; s += T(sx(p[0]) - 6, sy(p[1]) - 10, sr.label, { size: 13, bold: true, fill: c, anchor: 'end' }); } });
    return { svg: W(s), a: {} };
  };
  // bar chart
  F.barchart = (o) => {
    const lb = o.labels || [], v = o.values || [], ymax = o.ymax || Math.max(...v, 1), step = o.step || ymax / 5, px0 = 70, px1 = 450, py0 = 260, py1 = 20, bw = (px1 - px0) / Math.max(1, lb.length);
    const sy = x => py0 - x / ymax * (py0 - py1); let s = '';
    for (let y = 0; y <= ymax + 1e-9; y += step) s += L(px0, sy(y), px1, sy(y), { w: 0.6, c: '#D6E0EE' }) + T(px0 - 8, sy(y) + 4, +y.toFixed(2), { size: 11, anchor: 'end' });
    const ng = o.gap === false, f0 = ng ? 0 : 0.18, fw = ng ? 1 : 0.64; lb.forEach((l, i) => { const x = px0 + bw * i + bw * f0; s += `<rect x="${x}" y="${sy(v[i])}" width="${bw * fw}" height="${py0 - sy(v[i])}" fill="${(o.colours || [])[i] || C.blue}"${ng ? ' stroke="#fff" stroke-width="1.5"' : ''}/>` + T(x + bw * fw / 2, py0 + 18, l, { size: 11 }); });
    s += L(px0, py0, px1, py0) + L(px0, py0, px0, py1) + T(16, (py0 + py1) / 2, o.ylabel || '', { size: 12, bold: true, rot: -90 }) + T((px0 + px1) / 2, 312, o.xlabel || '', { size: 12, bold: true });
    return { svg: W(s), a: {} };
  };
  // Solar System / orbit sketch kept simple: Sun, planet orbit, asteroid belt
  F.orbits = (o) => {
    const n = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']; let s = `<circle cx="40" cy="160" r="34" fill="${C.gold}"/>` + T(40, 210, 'Sun', { size: 12 });
    n.forEach((p, i) => { const x = 110 + i * 70 + (i > 3 ? 60 : 0); s += `<circle cx="${x}" cy="160" r="${[5, 9, 9, 7, 22][i]}" fill="${['#9A9A9A', '#E8C27A', '#3A7BD5', '#C1440E', '#D8A26B'][i]}"/>` + T(x, 200, o.letters ? String.fromCharCode(65 + i) : p, { size: 12, bold: !!o.letters }); });
    for (let k = 0; k < 40; k++) s += `<circle cx="${370 + (k * 37) % 50}" cy="${100 + (k * 53) % 120}" r="2" fill="${C.grey}"/>`;
    s += T(395, 90, o.letters ? 'X' : 'asteroid belt', { size: 12, bold: !!o.letters });
    return { svg: W(s), a: {} };
  };

  /* ---------------- part 3: general diagrams for Stages 7–8 ---------------- */
  // boxes joined by arrows (food chains and webs, cycles, systems); nodes: [{t, x, y, c}], edges: [[from, to, label]]
  F.flow = (o) => {
    const id = 'f' + (++uid), N = o.nodes || [], E = o.edges || [], bw = o.w || 96, bh = 34;
    let s = arrowDef(id, C.ink);
    E.forEach(([a, b, lb]) => { const A = N[a], Bn = N[b]; if (!A || !Bn) return; const dx = Bn.x - A.x, dy = Bn.y - A.y, d = Math.hypot(dx, dy) || 1;
      const kx = Math.abs(dx) * bh > Math.abs(dy) * bw ? (bw / 2) / Math.abs(dx) * d : (bh / 2) / Math.abs(dy || 1) * d; const k = Math.min(kx, d / 2 - 4) + 4;
      s += L(A.x + dx / d * k, A.y + dy / d * k, Bn.x - dx / d * k, Bn.y - dy / d * k, { w: 2, m: id }) + (lb ? T((A.x + Bn.x) / 2 + 6, (A.y + Bn.y) / 2 - 6, lb, { size: 11, fill: C.blue, anchor: 'start' }) : ''); });
    N.forEach((n) => { s += `<rect x="${n.x - bw / 2}" y="${n.y - bh / 2}" width="${bw}" height="${bh}" rx="8" fill="${n.c || '#EAF3FF'}" stroke="${C.ink}" stroke-width="1.6"/>` + T(n.x, n.y + 4.5, n.t, { size: 12, bold: true }); });
    return { svg: W(s, o.vb), a: {} };   // o.vb: a shorter viewBox for one-row machines
  };
  // particle diagrams in boxes; boxes: [{state: solid|liquid|gas|mixture, label}]
  F.particles = (o) => {
    const bx = o.boxes || [{ state: 'solid' }, { state: 'liquid' }, { state: 'gas' }], n = bx.length, gap = 460 / n, bw = Math.min(130, gap - 20);
    let s = ''; bx.forEach((b, i) => { const x = 10 + gap * i + (gap - bw) / 2, y = 50, h = 200; s += `<rect x="${x}" y="${y}" width="${bw}" height="${h}" fill="#fff" stroke="${C.ink}" stroke-width="2"/>`;
      const P = (cx, cy, c) => `<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="8" fill="${c || C.blue}" stroke="${C.ink}" stroke-width="1"/>`;
      const st = b.state || 'solid', r = (k) => ((Math.sin(k * 12.9898 + i * 7.1) * 43758.5453) % 1 + 1) % 1;
      if (st === 'solid') for (let a = 0; a < 5; a++) for (let c = 0; c < 6; c++) s += P(x + 18 + a * ((bw - 36) / 4), y + h - 18 - c * 17);
      else if (st === 'liquid') { for (let k = 0; k < 22; k++) s += P(x + 14 + r(k) * (bw - 28), y + h - 14 - (k % 6) * 15 - r(k + 50) * 6); }
      else if (st === 'gas') { for (let k = 0; k < 7; k++) s += P(x + 16 + r(k) * (bw - 32), y + 16 + r(k + 9) * (h - 32)); }
      else { for (let k = 0; k < 14; k++) s += P(x + 16 + r(k) * (bw - 32), y + 16 + r(k + 9) * (h - 32), k % 2 ? C.red : C.blue); }
      s += T(x + bw / 2, y + h + 26, b.label || String.fromCharCode(65 + i), { bold: true, size: 14 }); });
    return { svg: W(s), a: {} };
  };
  // bar magnets with field lines or a second magnet; o.pair: 'attract' | 'repel' | undefined; o.compass: true
  F.barmagnet = (o) => {
    const mag = (x, y, l, r) => `<rect x="${x}" y="${y}" width="70" height="34" fill="${l === 'N' ? '#E14E4E' : '#2F80ED'}"/><rect x="${x + 70}" y="${y}" width="70" height="34" fill="${r === 'N' ? '#E14E4E' : '#2F80ED'}"/>` + T(x + 35, y + 23, l, { fill: '#fff', bold: true, size: 18 }) + T(x + 105, y + 23, r, { fill: '#fff', bold: true, size: 18 });
    let s = '';
    if (o.pair) { const rep = o.pair === 'repel'; s += mag(30, 143, 'S', 'N') + mag(310, 143, rep ? 'N' : 'S', rep ? 'S' : 'N');
      if (o.lines !== false) for (let k = -2; k <= 2; k++) s += rep ? `<path d="M170 ${160 + k * 6} q60 ${k * 30} 0 ${k * 60 + (k ? 0 : 1)}" fill="none" stroke="${C.grey}" stroke-width="1.5"/>`.replace(/q60 (-?\d+) 0 (-?\d+)/, `q50 ${k * 22} 50 ${k * 40}`) + `<path d="M310 ${160 + k * 6} q-50 ${k * 22} -50 ${k * 40}" fill="none" stroke="${C.grey}" stroke-width="1.5"/>` : L(170, 160 + k * 6, 310, 160 + k * 6, { w: 1.5, c: C.grey });
    } else { s += mag(170, 143, o.left || 'N', o.left === 'S' ? 'N' : 'S');
      for (let k = 1; k <= 4; k++) { const h = 22 + k * 26; s += `<path d="M178 ${143} C${150 - k * 20} ${143 - h} ${330 + k * 20} ${143 - h} ${302} 143" fill="none" stroke="${C.grey}" stroke-width="1.5"/><path d="M178 177 C${150 - k * 20} ${177 + h} ${330 + k * 20} ${177 + h} 302 177" fill="none" stroke="${C.grey}" stroke-width="1.5"/>`; }
      s += L(100, 160, 170, 160, { w: 1.5, c: C.grey }) + L(310, 160, 380, 160, { w: 1.5, c: C.grey });
      if (o.compass) [[90, 110, 'A'], [240, 70, 'B'], [400, 200, 'C']].forEach(([x, y, l]) => { s += `<circle cx="${x}" cy="${y}" r="16" fill="#fff" stroke="${C.ink}" stroke-width="2"/>` + letter(x + 26, y - 18, l); }); }
    return { svg: W(s), a: {} };
  };
  // bell-jar model of the lungs; o.sheet: 'down' (breathing in) | 'up' (breathing out); o.letters
  F.lungmodel = (o) => {
    const down = (o.sheet || 'down') === 'down', r = down ? 34 : 20;
    let s = `<path d="M140 280 V100 Q140 40 240 40 Q340 40 340 100 V280" fill="#F4F9FF" stroke="${C.glass}" stroke-width="3"/><rect x="232" y="14" width="16" height="70" fill="#fff" stroke="${C.glass}" stroke-width="2"/>`
      + `<path d="M240 84 v30 M240 114 l-40 30 M240 114 l40 30" stroke="${C.glass}" stroke-width="5" fill="none"/>`
      + `<ellipse cx="196" cy="${150 + r}" rx="${r}" ry="${r + 6}" fill="#F7B2B7" stroke="#B5525A" stroke-width="2"/><ellipse cx="284" cy="${150 + r}" rx="${r}" ry="${r + 6}" fill="#F7B2B7" stroke="#B5525A" stroke-width="2"/>`
      + `<path d="M140 280 Q240 ${down ? 330 : 250} 340 280" fill="none" stroke="${C.ink}" stroke-width="5"/>` + L(240, down ? 304 : 266, 240, down ? 318 : 280, { w: 3 });
    s += o.letters ? L(248, 40, 284, 30, { w: 1.2 }) + letter(296, 30, 'A') + L(312, 176, 378, 150, { w: 1.2 }) + letter(390, 150, 'B') + L(340, 232, 378, 232, { w: 1.2 }) + letter(390, 232, 'C') + L(300, 296, 340, 304, { w: 1.2 }) + letter(352, 304, 'D')
      : lab(248, 50, 'glass tube (trachea)', 330, 24) + lab(284, 150, 'balloon (lung)', 380, 130) + lab(330, 200, 'bell jar (ribcage)', 368, 210) + lab(300, 290, 'rubber sheet (diaphragm)', 300, 314);
    return { svg: W(s), a: {} };
  };
  // spring hanging from a clamp beside a ruler, with a load
  F.spring = (o) => {
    const rd = o.reading != null ? o.reading : 6 + (o.ext != null ? o.ext : 4), len = rd * 10, top = 50; let coil = '';
    for (let k = 0; k <= 12; k++) coil += (k ? 'L' : 'M') + (240 + (k % 2 ? 14 : -14) * (k && k < 12 ? 1 : 0)) + ' ' + (top + k * len / 12);
    let s = `<rect x="120" y="30" width="200" height="12" fill="${C.grey}"/><rect x="120" y="30" width="12" height="270" fill="${C.grey}"/>` + bench(300) + `<path d="${coil}" fill="none" stroke="${C.ink}" stroke-width="2.5"/>`
      + `<rect x="222" y="${top + len}" width="36" height="${16 + (o.load || 2) * 3}" rx="3" fill="${C.blue}"/>` + T(240, top + len + 13 + (o.load || 2) * 1.5, o.loadLabel || `${o.load || 2} N`, { size: 12, fill: '#fff', bold: true });
    s += `<rect x="300" y="40" width="26" height="250" fill="#F6E3A1" stroke="${C.ink}"/>`; for (let i = 0; i <= 24; i++) s += L(300, 50 + i * 10, 300 + (i % 5 === 0 ? 12 : 6), 50 + i * 10, { w: 1 }) + (i % 5 === 0 ? T(340, 54 + i * 10, i, { size: 11, anchor: 'start' }) : '');
    s += L(258, top + len, 300, top + len, { w: 1.2, dash: '4 3', c: C.red }) + T(372, 30, 'cm', { size: 11 });
    return { svg: W(s), a: {} };
  };
  // conical flasks with balloons over the neck (gas made by yeast or a reaction); items: [{label, balloon (0..1), note}]
  F.balloons = (o) => {
    const it = o.items || [], n = it.length || 1, gap = 460 / n; let s = bench(290);
    it.forEach((t, i) => { const cx = 10 + gap * i + gap / 2, r = 8 + (t.balloon || 0) * 34;
      s += `<path d="M${cx - 10} 170 v30 L${cx - 44} 286 h88 L${cx + 10} 200 v-30" fill="none" stroke="${C.glass}" stroke-width="3"/><path d="M${cx - 36} 262 L${cx - 44} 286 h88 L${cx + 36} 262z" fill="${t.colour || '#F2E1C2'}"/>`;
      s += `<ellipse cx="${cx}" cy="${168 - r}" rx="${r * 0.85}" ry="${r}" fill="${['#E14E4E', '#F2C94C', '#27AE60', '#9B51E0', '#2F80ED'][i % 5]}" opacity=".85"/><rect x="${cx - 11}" y="160" width="22" height="12" fill="${C.ink}" opacity=".5"/>`;
      s += T(cx, 308, t.label || String.fromCharCode(65 + i), { bold: true, size: 13 }) + (t.note ? T(cx, 30, t.note, { size: 11, fill: C.blue }) : ''); });
    return { svg: W(s), a: {} };
  };
})();
