/* Camday — figure library, part 4: cells (SVG, viewBox 480×320). Original Camday artwork.
   Use in a question as fig: 'leafsection' or fig: { kind: 'plantAB' }. Each returns { svg, a } like figures.js. */
(function () {
  const AF = window.AtomicFig; if (!AF) return;
  const C = Object.assign({}, AF.C, { ink: '#0B2545', soil: '#EFE6DA', water: '#D6ECFF', cw: '#6D4C41' });
  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const W = (inner, extra) => `<svg viewBox="0 0 480 320" xmlns="http://www.w3.org/2000/svg" role="img" font-family="Figtree, Arial, sans-serif" ${extra || ''}>${inner}</svg>`;
  const T = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 13}" fill="${o.fill || C.ink}" text-anchor="${o.anchor || 'middle'}" ${o.bold ? 'font-weight="700"' : ''}>${esc(s)}</text>`;
  const chl = (x, y, s = 1) => `<ellipse cx="${x}" cy="${y}" rx="${7 * s}" ry="${4 * s}" fill="${C.green}" stroke="${C.dgreen}" stroke-width="1.2"/>`;
  const F = AF.F;

  // cross-section of a leaf: four tissues; anchors for labelling
  F.leafsection = () => {
    let s = '';
    for (let i = 0; i < 12; i++) s += `<rect x="${30 + i * 36}" y="40" width="34" height="22" rx="4" fill="#F1F8E9" stroke="#689F38" stroke-width="1.6"/>`;
    for (let i = 0; i < 13; i++) { s += `<rect x="${30 + i * 33}" y="66" width="30" height="86" rx="9" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.6"/>`; for (let j = 0; j < 5; j++) s += chl(39 + i * 33 + (j % 2) * 12, 78 + j * 15, 0.8); }
    for (let i = 0; i < 16; i++) s += `<ellipse cx="${45 + (i * 61) % 400}" cy="${176 + (i % 3) * 24}" rx="24" ry="15" fill="#E8F5E9" stroke="#43A047" stroke-width="1.6"/>${chl(45 + (i * 61) % 400, 176 + (i % 3) * 24, 0.6)}`;
    for (let i = 0; i < 12; i++) s += `<rect x="${30 + i * 36}" y="240" width="34" height="22" rx="4" fill="#F1F8E9" stroke="#689F38" stroke-width="1.6"/>`;
    s += `<path d="M228 262 q14 -12 28 0" fill="#fff" stroke="${C.ink}" stroke-width="2"/>` + T(242, 290, 'pore', { size: 12 });
    for (let i = 0; i < 4; i++) s += `<path d="M${70 + i * 110} 6 L${84 + i * 110} 36" stroke="#F9A825" stroke-width="3" stroke-dasharray="5 4"/>`;
    return { svg: W(s), a: { upper: [440, 51], palisade: [440, 110], spongy: [440, 200], lower: [440, 251] } };
  };

  // two plant cells: A with chloroplasts (leaf), B without (root / onion); o.labels shows A/B
  F.plantAB = () => {
    let a = `<rect x="30" y="60" width="180" height="190" rx="12" fill="${C.cyto}" stroke="${C.dgreen}" stroke-width="9"/><rect x="70" y="100" width="100" height="110" rx="24" fill="${C.vac}"/><circle cx="185" cy="225" r="13" fill="${C.nuc}"/>`;
    for (let i = 0; i < 9; i++) a += chl(52 + (i % 3) * 70 + (i > 5 ? 20 : 0), 80 + Math.floor(i / 3) * 75, 1.2);
    const b = `<rect x="270" y="80" width="180" height="150" rx="12" fill="#FAFAFA" stroke="${C.cw}" stroke-width="9"/><rect x="300" y="105" width="120" height="100" rx="24" fill="${C.vac}"/><circle cx="430" cy="210" r="13" fill="${C.nuc}"/>`;
    return { svg: W(a + b + T(120, 290, 'Cell A', { size: 18, bold: true }) + T(360, 290, 'Cell B', { size: 18, bold: true })), a: {} };
  };

  // root hair cell (path of water) with numbered places 1–4 along the path of water (shuffled by o.order, default wall, membrane, cytoplasm, vacuole)
  F.rootpath = (o) => {
    const at = { wall: [200, 80], membrane: [270, 93], cytoplasm: [180, 160], vacuole: [320, 150] };
    const nums = o && o.nums ? o.nums : {};
    let s = `<rect x="0" y="230" width="480" height="90" fill="${C.soil}"/>`;
    for (let i = 0; i < 14; i++) s += `<circle cx="${20 + (i * 71) % 460}" cy="${250 + (i * 29) % 60}" r="${8 + (i % 3) * 4}" fill="#D7CCC8"/>`;
    s += `<path d="M120 80 H440 V220 H120 V170 H20 Q8 170 8 158 Q8 146 20 146 H120Z" fill="#F4F9E6" stroke="${C.cw}" stroke-width="7"/>`;
    s += `<path d="M132 92 H428 V208 H132 V176 H24 Q18 170 18 158 Q18 140 24 140 H132Z" fill="none" stroke="#7CB342" stroke-width="2"/>`;
    s += `<rect x="230" y="105" width="170" height="90" rx="24" fill="${C.vac}"/><circle cx="410" cy="200" r="12" fill="${C.nuc}"/>`;
    s += T(60, 230, 'soil water', { size: 12 }) + `<path d="M40 210 L90 166" stroke="#0277BD" stroke-width="3"/>`;
    Object.entries(nums).forEach(([k, n]) => { const p = at[k]; s += `<circle cx="${p[0]}" cy="${p[1] - 40}" r="13" fill="#fff" stroke="${C.ink}" stroke-width="2"/>${T(p[0], p[1] - 35, n, { bold: true })}<path d="M${p[0]} ${p[1] - 27} V${p[1] - 6}" stroke="${C.ink}" stroke-width="1.5"/>`; });
    return { svg: W(s), a: { wall: at.wall, membrane: at.membrane, cytoplasm: at.cytoplasm, vacuole: at.vacuole } };
  };

  // three views down a microscope: A dark, B bright but blurred, C sharp
  F.microviews = () => {
    let cells = ''; for (let r = 0; r < 4; r++) for (let c = 0; c < 4; c++) cells += `<rect x="${-58 + c * 30 + (r % 2 ? 15 : 0)}" y="${-56 + r * 28}" width="28" height="24" rx="3" fill="#F3E5F5" stroke="#8E24AA" stroke-width="2"/><circle cx="${-48 + c * 30 + (r % 2 ? 15 : 0)}" cy="${-46 + r * 28}" r="3" fill="#6A1B9A"/>`;
    const v = (x, inner, l) => `<g transform="translate(${x} 150)"><clipPath id="mv${l}"><circle r="68"/></clipPath><g clip-path="url(#mv${l})">${inner}</g><circle r="68" fill="none" stroke="#263238" stroke-width="7"/></g>${T(x, 260, 'View ' + l, { size: 16, bold: true })}`;
    const defs = `<defs><filter id="mvbl"><feGaussianBlur stdDeviation="4"/></filter></defs>`;
    return { svg: W(defs + v(85, `<rect x="-70" y="-70" width="140" height="140" fill="#1A1A1A"/>`, 'A') + v(240, `<rect x="-70" y="-70" width="140" height="140" fill="#FFFDE7"/><g filter="url(#mvbl)">${cells}</g>`, 'B') + v(395, `<rect x="-70" y="-70" width="140" height="140" fill="#FFFDE7"/>${cells}`, 'C')), a: {} };
  };

  // staining set-up: slide, coverslip, dropper of stain at one edge, paper towel at the other edge
  F.stainsetup = () => {
    let s = `<rect x="40" y="190" width="400" height="40" rx="4" fill="#E3F2FD" stroke="#64B5F6" stroke-width="3"/>`;
    s += `<rect x="160" y="182" width="160" height="10" fill="#B3E5FC" stroke="#0277BD" stroke-width="2"/>`;
    s += `<ellipse cx="240" cy="198" rx="50" ry="5" fill="#CE93D8"/>`;
    s += `<path d="M120 60 h24 v70 l-12 26 l-12 -26z" fill="#ECEFF1" stroke="${C.ink}" stroke-width="2"/><rect x="116" y="40" width="32" height="24" rx="8" fill="#E57373"/><path d="M132 160 q-6 10 0 16 q6 -6 0 -16" fill="#1E88E5"/>`;
    s += `<path d="M330 150 h80 l-10 40 h-70z" fill="#FFF8E1" stroke="#BCAAA4" stroke-width="2"/>`;
    s += T(132, 30, 'stain', { size: 12, bold: true }) + T(370, 140, 'paper towel', { size: 12, bold: true }) + T(240, 260, 'microscope slide', { size: 12 }) + T(300, 172, 'coverslip', { size: 12 });
    return { svg: W(s), a: { dropper: [132, 100], coverslip: [300, 186], specimen: [215, 199], towel: [370, 170], slide: [90, 210] } };
  };

  // a simple pond animal (body wall of two cell layers, tentacles, a digestive cavity) — for cell / tissue / organ reasoning
  F.polyp = () => {
    let s = `<path d="M200 300 C190 220 190 140 210 100 L270 100 C290 140 290 220 280 300Z" fill="#FCE4EC" stroke="#AD1457" stroke-width="3"/>`;
    s += `<path d="M214 290 C206 220 206 150 222 112 L258 112 C274 150 274 220 266 290Z" fill="#FFF3E0" stroke="#EF6C00" stroke-width="2"/>`;
    for (let i = 0; i < 5; i++) s += `<path d="M${215 + i * 12} 100 C${170 + i * 35} 40 ${150 + i * 45} 30 ${140 + i * 50} ${20 + (i % 2) * 15}" fill="none" stroke="#AD1457" stroke-width="7" stroke-linecap="round"/>`;
    for (let i = 0; i < 14; i++) s += `<circle cx="${205 + (i % 2) * 70}" cy="${120 + i * 12}" r="3" fill="#6A1B9A"/>`;
    s += T(240, 205, 'cavity', { size: 12 }) + T(240, 92, 'mouth', { size: 11 });
    return { svg: W(s), a: { tentacle: [160, 40], outer: [200, 230], inner: [222, 200], cavity: [240, 190], mouth: [240, 102] } };
  };
})();
