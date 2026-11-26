/* Camday — figure library (SVG, viewBox 480×320).
   Each figure returns {svg, a} where a = {anchorId: [x, y]} for labelling questions. */
(function () {
  const C = { navy: '#0B2545', blue: '#0149AF', gold: '#F3BF69', green: '#3FA34D', dgreen: '#1F6F2B', lgreen: '#CDEFD0',
    cyto: '#FFF4D6', vac: '#CFE6FF', nuc: '#8E6CC9', mito: '#F08A4B', grey: '#6B7A90', lgrey: '#D9E2EC', red: '#D64545', pink: '#F7C6C6' };
  const W = (inner, extra) => `<svg viewBox="0 0 480 320" xmlns="http://www.w3.org/2000/svg" role="img" ${extra || ''}>${inner}</svg>`;
  const mito = (x, y, r = 0) => `<g transform="translate(${x} ${y}) rotate(${r})"><ellipse rx="13" ry="6" fill="${C.mito}" stroke="#A4501E" stroke-width="1.5"/><path d="M-9 0 q3 -4 6 0 t6 0 t6 0" fill="none" stroke="#A4501E" stroke-width="1.2"/></g>`;
  const chl = (x, y, r = 0) => `<g transform="translate(${x} ${y}) rotate(${r})"><ellipse rx="11" ry="6" fill="${C.green}" stroke="${C.dgreen}" stroke-width="1.5"/><path d="M-6 -2 h12 M-6 1 h12" stroke="${C.dgreen}" stroke-width="1"/></g>`;

  const F = {};
  F.microscope = () => ({
    svg: W(`
      <rect x="120" y="282" width="210" height="22" rx="6" fill="${C.navy}"/>
      <path d="M300 282 C 300 220, 330 190, 318 120 L 300 60" stroke="${C.navy}" stroke-width="22" fill="none" stroke-linecap="round"/>
      <rect x="150" y="40" width="34" height="96" rx="5" transform="rotate(-18 167 88)" fill="${C.grey}"/>
      <rect x="128" y="14" width="30" height="30" rx="4" transform="rotate(-18 143 29)" fill="${C.blue}"/>
      <path d="M190 134 l-8 28 h18 z" fill="${C.blue}"/><path d="M206 132 l2 24 h12 l-2 -24z" fill="${C.grey}"/>
      <rect x="140" y="178" width="170" height="12" rx="3" fill="${C.navy}"/>
      <path d="M160 176 l40 -6" stroke="${C.gold}" stroke-width="5" stroke-linecap="round"/>
      <rect x="176" y="192" width="44" height="8" rx="2" fill="${C.gold}"/>
      <circle cx="198" cy="252" r="14" fill="#FFE9A8" stroke="${C.gold}" stroke-width="4"/><path d="M198 232 v-26" stroke="#FFE9A8" stroke-width="5" stroke-dasharray="4 4"/>
      <circle cx="318" cy="210" r="17" fill="${C.lgrey}" stroke="${C.navy}" stroke-width="4"/>
      <circle cx="322" cy="244" r="9" fill="${C.lgrey}" stroke="${C.navy}" stroke-width="3"/>`),
    a: { eyepiece: [143, 26], objective: [191, 150], stage: [270, 184], clips: [182, 174], diaphragm: [198, 196], light: [198, 252], coarse: [318, 210], fine: [322, 244], arm: [312, 140], base: [150, 293] }
  });
  F.plantcell = () => ({
    svg: W(`
      <rect x="70" y="40" width="340" height="240" rx="18" fill="${C.lgreen}" stroke="${C.dgreen}" stroke-width="10"/>
      <rect x="84" y="54" width="312" height="212" rx="12" fill="${C.cyto}" stroke="#7A9A3A" stroke-width="2"/>
      <rect x="150" y="90" width="200" height="140" rx="40" fill="${C.vac}" stroke="#6A9FD8" stroke-width="2"/>
      <circle cx="118" cy="110" r="24" fill="${C.nuc}" stroke="#5B3E8F" stroke-width="2"/><circle cx="122" cy="106" r="7" fill="#5B3E8F"/>
      ${chl(372, 80, 20)}${chl(372, 230, -15)}${chl(120, 236, 10)}${chl(260, 70, 0)}${chl(370, 155, 90)}
      ${mito(115, 175, 70)}${mito(300, 248, 0)}`),
    a: { wall: [240, 40], membrane: [396, 120], cytoplasm: [130, 206], nucleus: [118, 110], vacuole: [250, 160], chloroplast: [372, 80], mito: [300, 248] }
  });
  F.animalcell = () => ({
    svg: W(`
      <path d="M110 120 C 120 50, 260 30, 330 70 C 400 105, 420 200, 360 250 C 300 300, 160 290, 115 240 C 80 205, 100 160, 110 120 Z" fill="${C.pink}" stroke="#B5546E" stroke-width="3"/>
      <circle cx="240" cy="160" r="38" fill="${C.nuc}" stroke="#5B3E8F" stroke-width="2"/><circle cx="246" cy="154" r="11" fill="#5B3E8F"/>
      ${mito(160, 130, 30)}${mito(330, 190, -20)}${mito(190, 240, 10)}`),
    a: { membrane: [118, 240], cytoplasm: [300, 110], nucleus: [240, 160], mito: [330, 190] }
  });
  F.roothair = () => ({
    svg: W(`
      <path d="M40 120 h170 c 30 0, 40 -4, 70 -4 h170 a 12 12 0 0 1 0 24 h-170 c -30 0 -40 6 -70 46 h-170 z" fill="${C.cyto}" stroke="${C.dgreen}" stroke-width="7"/>
      <rect x="60" y="134" width="120" height="40" rx="14" fill="${C.vac}" stroke="#6A9FD8" stroke-width="2"/>
      <circle cx="240" cy="132" r="15" fill="${C.nuc}" stroke="#5B3E8F" stroke-width="2"/>
      <path d="M0 210 h480" stroke="#8B6B3E" stroke-width="2" stroke-dasharray="6 6"/><text x="12" y="234" font-size="14" fill="#8B6B3E">soil particles</text>
      ${[300, 340, 380, 420, 455].map((x, i) => `<circle cx="${x}" cy="${i % 2 ? 104 : 152}" r="9" fill="#C9A66B"/>`).join('')}`),
    a: { extension: [380, 128], nucleus: [240, 132], vacuole: [120, 154], wall: [40, 150] }
  });
  F.neurone = () => ({
    svg: W(`
      <path d="M70 160 l-30 -40 M70 160 l-36 10 M70 160 l-26 40 M84 140 l-10 -50" stroke="${C.blue}" stroke-width="5" fill="none" stroke-linecap="round"/>
      <circle cx="90" cy="160" r="34" fill="#D7E6FB" stroke="${C.blue}" stroke-width="4"/><circle cx="92" cy="158" r="12" fill="${C.nuc}"/>
      <path d="M124 160 C 200 150, 300 175, 400 160" stroke="${C.blue}" stroke-width="9" fill="none" stroke-linecap="round"/>
      <path d="M400 160 l40 -34 M400 160 l46 0 M400 160 l38 34" stroke="${C.blue}" stroke-width="5" fill="none" stroke-linecap="round"/>
      ${[440, 446, 438].map((x, i) => `<circle cx="${x}" cy="${[126, 160, 194][i]}" r="6" fill="${C.gold}"/>`).join('')}`),
    a: { body: [90, 160], fibre: [260, 162], endings: [440, 160], nucleus: [92, 158] }
  });
  F.ciliated = () => ({
    svg: W(`
      <rect x="40" y="60" width="400" height="34" rx="12" fill="#E8F3C6" stroke="#9AB84A" stroke-width="2"/>
      ${[0, 1, 2].map(k => `<rect x="${70 + k * 120}" y="110" width="100" height="170" rx="10" fill="${C.cyto}" stroke="#B5546E" stroke-width="3"/>
        <circle cx="${120 + k * 120}" cy="220" r="16" fill="${C.nuc}"/>
        ${Array.from({ length: 9 }, (_, i) => `<path d="M${76 + k * 120 + i * 11} 110 q 4 -10 0 -16" stroke="#B5546E" stroke-width="2.5" fill="none"/>`).join('')}`).join('')}`),
    a: { mucus: [240, 77], cilia: [240, 100], nucleus: [240, 220] }
  });
  F.palisade = () => ({
    svg: W(`
      <rect x="170" y="30" width="140" height="262" rx="18" fill="${C.lgreen}" stroke="${C.dgreen}" stroke-width="8"/>
      <rect x="196" y="110" width="88" height="150" rx="20" fill="${C.vac}" stroke="#6A9FD8" stroke-width="2"/>
      <circle cx="240" cy="78" r="15" fill="${C.nuc}"/>
      ${[[195, 60], [285, 60], [196, 98], [284, 104], [190, 150], [290, 160], [190, 205], [290, 215], [196, 266], [284, 268], [215, 52], [265, 52]].map(([x, y], i) => chl(x, y, i * 37)).join('')}`),
    a: { wall: [170, 180], nucleus: [240, 78], chloroplast: [290, 160], vacuole: [240, 185] }
  });
  F.plant = () => ({
    svg: W(`
      <path d="M0 230 h480" stroke="#8B6B3E" stroke-width="3"/><rect x="0" y="230" width="480" height="90" fill="#F3E3C6"/>
      <path d="M240 230 V 70" stroke="${C.dgreen}" stroke-width="10"/>
      <path d="M240 160 C 190 120, 140 140, 130 160 C 170 180, 210 175, 240 160Z" fill="${C.green}"/>
      <path d="M240 130 C 290 90, 340 110, 350 130 C 310 150, 270 145, 240 130Z" fill="${C.green}"/>
      ${Array.from({ length: 8 }, (_, i) => `<ellipse cx="${240 + 22 * Math.cos(i * Math.PI / 4)}" cy="${55 + 22 * Math.sin(i * Math.PI / 4)}" rx="14" ry="9" transform="rotate(${i * 45} ${240 + 22 * Math.cos(i * Math.PI / 4)} ${55 + 22 * Math.sin(i * Math.PI / 4)})" fill="${C.gold}"/>`).join('')}
      <circle cx="240" cy="55" r="12" fill="#8B5A2B"/>
      <path d="M240 230 l-40 50 M240 230 l0 70 M240 230 l40 55 M220 255 l-30 10 M262 262 l30 6" stroke="#8B6B3E" stroke-width="5" fill="none" stroke-linecap="round"/>`),
    a: { flower: [240, 55], leaf: [300, 125], stem: [240, 200], root: [240, 285] }
  });
  F.body = () => ({
    svg: W(`
      <circle cx="240" cy="48" r="36" fill="#F6D7C0" stroke="${C.navy}" stroke-width="2"/>
      <path d="M180 92 h120 l18 150 h-156 z" fill="#F6D7C0" stroke="${C.navy}" stroke-width="2"/>
      <path d="M220 34 c 10 -14 30 -14 40 0 c 6 10 -4 26 -20 26 c -16 0 -26 -16 -20 -26z" fill="#F2A7B8" stroke="#B5546E" stroke-width="2"/>
      <path d="M200 110 c -14 20 -14 50 -4 64 c 10 6 26 2 30 -10 v-50 c -6 -10 -18 -12 -26 -4z" fill="#F5B3B3" stroke="${C.red}" stroke-width="2"/>
      <path d="M280 110 c 14 20 14 50 4 64 c -10 6 -26 2 -30 -10 v-50 c 6 -10 18 -12 26 -4z" fill="#F5B3B3" stroke="${C.red}" stroke-width="2"/>
      <path d="M246 140 c 8 -12 26 -4 16 12 l-16 18 l-16 -18 c -10 -16 8 -24 16 -12z" fill="${C.red}"/>
      <path d="M232 188 c 30 -8 50 6 40 26 c -10 18 -40 16 -46 0 c -4 -10 -2 -20 6 -26z" fill="#F3C47A" stroke="#B07A2A" stroke-width="2"/>`),
    a: { brain: [240, 36], lungs: [206, 140], heart: [246, 152], stomach: [252, 204] }
  });
  F.cellsAB = () => ({
    svg: W(`
      <rect x="30" y="60" width="190" height="200" rx="10" fill="${C.cyto}" stroke="${C.dgreen}" stroke-width="10"/>
      <rect x="64" y="92" width="122" height="136" rx="30" fill="${C.vac}" stroke="#6A9FD8" stroke-width="2"/>
      <circle cx="54" cy="100" r="14" fill="${C.nuc}"/>
      <path d="M270 110 C 290 50, 430 60, 440 130 C 452 210, 380 270, 320 250 C 260 236, 254 160, 270 110Z" fill="${C.pink}" stroke="#B5546E" stroke-width="2"/>
      <circle cx="350" cy="160" r="22" fill="${C.nuc}"/>
      <text x="125" y="300" font-size="26" font-weight="700" fill="${C.navy}" text-anchor="middle">A</text>
      <text x="355" y="300" font-size="26" font-weight="700" fill="${C.navy}" text-anchor="middle">B</text>`), a: {}
  });
  F.cylinder = (o) => {
    const top = 30, bot = 290, x0 = 200, w = 80, n = (o.max - o.min);
    const yv = v => bot - (v - o.min) / n * (bot - top);
    let ticks = '';
    for (let v = o.min; v <= o.max + 1e-9; v += o.minor) {
      const vv = Math.round(v * 1000) / 1000, major = Math.abs(vv / o.major - Math.round(vv / o.major)) < 1e-6;
      ticks += `<path d="M${x0} ${yv(vv)} h${major ? 30 : 16}" stroke="${C.navy}" stroke-width="${major ? 2 : 1}"/>`;
      if (major) ticks += `<text x="${x0 - 8}" y="${yv(vv) + 5}" font-size="15" text-anchor="end" fill="${C.navy}">${vv}</text>`;
    }
    const lv = yv(o.value);
    return {
      svg: W(`<rect x="${x0}" y="${top - 10}" width="${w}" height="${bot - top + 20}" rx="6" fill="#F7FBFF" stroke="${C.grey}" stroke-width="3"/>
        <path d="M${x0 + 2} ${lv - 6} Q ${x0 + w / 2} ${lv + 10} ${x0 + w - 2} ${lv - 6} V ${bot + 8} H ${x0 + 2} Z" fill="#9BC5F2" opacity=".8"/>
        ${ticks}<text x="${x0 + w + 14}" y="${top + 4}" font-size="16" fill="${C.navy}">${o.unit}</text>
        <rect x="${x0 - 40}" y="${bot + 10}" width="${w + 80}" height="10" rx="4" fill="${C.grey}"/>`, 'data-zoomable="1"'), a: {}, zoom: `${x0 - 50} ${lv - 34} ${w + 100} 68`
    };
  };
  /* microscope view used by the virtual experiment: onion epidermis, field of view radius 120 px */
  F.scopeView = (obj) => {
    const cellW = { 4: 24, 10: 60, 40: 240 }[obj];
    const cellH = cellW * 0.45;
    let cells = '';
    for (let y = -200; y < 520; y += cellH) {
      const off = (Math.round(y / cellH) % 2) * cellW / 2;
      for (let x = -260 - off; x < 760; x += cellW) {
        cells += `<rect x="${x}" y="${y}" width="${cellW}" height="${cellH}" fill="#F5EDD8" stroke="#8A6D3B" stroke-width="${obj === 40 ? 3 : 1.2}"/>`;
        if (obj >= 10) cells += `<ellipse cx="${x + cellW * 0.3}" cy="${y + cellH * 0.5}" rx="${cellW * 0.07}" ry="${cellH * 0.18}" fill="#B58A5A"/>`;
      }
    }
    return `<svg viewBox="0 0 320 320" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="fov"><circle cx="160" cy="160" r="150"/></clipPath></defs>
      <rect width="320" height="320" fill="#111"/><g clip-path="url(#fov)"><rect width="320" height="320" fill="#FFFBEF"/>${cells}
      <path d="M10 160 H310" stroke="#D64545" stroke-width="2" stroke-dasharray="6 4"/></g>
      <circle cx="160" cy="160" r="150" fill="none" stroke="#333" stroke-width="4"/></svg>`;
  };
  F.SCOPE_COUNT = { 4: 12, 10: 5, 40: 1.25 }; // cells across the 300 px diameter line (≈)

  window.AtomicFig = { get(name, opts) { const f = F[name]; return f ? f(opts || {}) : { svg: '', a: {} }; }, C, F };
})();
