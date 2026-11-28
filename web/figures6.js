/* Camday — science lesson illustrations (SVG, viewBox 480×320), used in the "Read the lesson" part under a Science video
   and in the lesson document. Original Camday artwork. Gentle CSS animations (off for reduced motion and in print).
   Use in a lesson block as fig: { kind: 'sciGlass' }. Each returns { svg, a } like figures.js. */
(function () {
  const AF = window.AtomicFig; if (!AF) return;
  const F = AF.F, INK = '#0B2545', BLUE = '#0149AF', GOLD = '#F3BF69', GREEN = '#3FA34D', DGREEN = '#1F6F2B', RED = '#D64545', GREY = '#6B7A90', SKY = '#D6ECFF', SOFT = '#F4F7FB', ORANGE = '#F08A4B', PURPLE = '#7A4BD1';
  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const CSS = `<style>.sa{transform-box:view-box}.a-rise{animation:sr var(--t,3s) linear infinite}@keyframes sr{0%{transform:translate(0,0);opacity:0}15%{opacity:1}85%{opacity:1}100%{transform:translate(var(--dx,0),var(--dy,-30px));opacity:0}}
.a-spin{animation:ss var(--t,8s) linear infinite;transform-origin:var(--o)}@keyframes ss{to{transform:rotate(360deg)}}
.a-swing{animation:sw 2.4s ease-in-out infinite alternate;transform-origin:var(--o)}@keyframes sw{from{transform:rotate(-14deg)}to{transform:rotate(14deg)}}
.a-flow{stroke-dasharray:8 8;animation:sf 1.2s linear infinite}@keyframes sf{to{stroke-dashoffset:-16}}
.a-draw{stroke-dasharray:420;animation:sd 3s linear infinite}@keyframes sd{from{stroke-dashoffset:420}to{stroke-dashoffset:0}}
.a-pulse{animation:sp 2s ease-in-out infinite;transform-origin:var(--o)}@keyframes sp{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.12);opacity:.75}}
.a-blink{animation:sb var(--t,2.4s) ease-in-out infinite}@keyframes sb{0%,100%{opacity:.15}50%{opacity:1}}
@media (prefers-reduced-motion:reduce){.sa{animation:none!important}}@media print{.sa{animation:none!important}}</style>`;
  // colours written as rgb(): the site theme recolours #hex (blue → grey), but water, sky and plants must keep their real colours; a white card keeps the picture readable in dark mode
  const rgb = s => s.replace(/#([0-9a-fA-F]{6})\b/g, (m, h) => `rgb(${parseInt(h.slice(0, 2), 16)},${parseInt(h.slice(2, 4), 16)},${parseInt(h.slice(4), 16)})`);
  const W = inner => `<svg viewBox="0 0 480 320" xmlns="http://www.w3.org/2000/svg" role="img" font-family="Figtree, Arial, sans-serif">${CSS}<rect width="480" height="320" rx="10" fill="rgb(255,255,255)"/>${rgb(inner)}</svg>`;
  const T = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 13}" fill="${o.fill || INK}" text-anchor="${o.anchor || 'middle'}"${o.bold ? ' font-weight="700"' : ''}>${esc(s)}</text>`;
  const box = (x, y, w, h, fill, stroke) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="12" fill="${fill || SOFT}" stroke="${stroke || '#C9D4E3'}" stroke-width="1.5"/>`;
  const arrow = (x1, y1, x2, y2, c = INK, anim) => { const a = Math.atan2(y2 - y1, x2 - x1), h = 8;
    return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${c}" stroke-width="2.4"${anim ? ' class="sa a-flow"' : ''}/><path d="M${x2} ${y2} L${x2 - h * Math.cos(a - 0.45)} ${y2 - h * Math.sin(a - 0.45)} L${x2 - h * Math.cos(a + 0.45)} ${y2 - h * Math.sin(a + 0.45)}Z" fill="${c}"/>`; };

  // small icons (centred on x, y, about 50 px)
  const ICON = {
    leaf: (x, y) => `<path d="M${x - 22} ${y + 20} C${x - 26} ${y - 14} ${x} ${y - 26} ${x + 24} ${y - 24} C${x + 24} ${y} ${x + 6} ${y + 24} ${x - 22} ${y + 20}Z" fill="${GREEN}" stroke="${DGREEN}" stroke-width="2"/><path d="M${x - 22} ${y + 20} L${x + 14} ${y - 14}" stroke="${DGREEN}" stroke-width="2"/>`,
    flask: (x, y) => `<path d="M${x - 8} ${y - 24} V${y - 6} L${x - 24} ${y + 20} H${x + 24} L${x + 8} ${y - 6} V${y - 24}Z" fill="#fff" stroke="${INK}" stroke-width="2.4"/><path d="M${x - 18} ${y + 10} H${x + 18} L${x + 24} ${y + 20} H${x - 24}Z" fill="#B9E3C6"/>` +
      [0, 1, 2].map(i => `<circle cx="${x - 6 + i * 6}" cy="${y + 8}" r="2.5" fill="${GREEN}" class="sa a-rise" style="--dy:-28px;--t:2s;animation-delay:${i * 0.6}s"/>`).join(''),
    bolt: (x, y) => `<g class="sa a-pulse" style="--o:${x}px ${y}px"><path d="M${x + 4} ${y - 26} L${x - 14} ${y + 4} H${x} L${x - 6} ${y + 26} L${x + 16} ${y - 6} H${x + 2}Z" fill="${GOLD}" stroke="${INK}" stroke-width="2"/></g>`,
    volcano: (x, y) => `<path d="M${x - 28} ${y + 22} L${x - 8} ${y - 12} H${x + 8} L${x + 28} ${y + 22}Z" fill="#A1887F" stroke="${INK}" stroke-width="2"/><path d="M${x - 8} ${y - 12} Q${x} ${y - 4} ${x + 8} ${y - 12}" fill="${RED}"/>` +
      [0, 1].map(i => `<circle cx="${x - 2 + i * 6}" cy="${y - 16}" r="5" fill="#B0BEC5" class="sa a-rise" style="--dy:-16px;--dx:${6 - i * 10}px;--t:2.6s;animation-delay:${i * 1.2}s"/>`).join(''),
    planet: (x, y) => `<circle cx="${x}" cy="${y}" r="14" fill="${BLUE}"/><ellipse cx="${x}" cy="${y}" rx="26" ry="8" fill="none" stroke="${GOLD}" stroke-width="2.5"/><g class="sa a-spin" style="--o:${x}px ${y}px;--t:5s"><circle cx="${x + 24}" cy="${y - 14}" r="4" fill="${GREY}"/></g>`,
    plug: (x, y) => ICON.bolt(x, y),
    bottle: (x, y) => `<path d="M${x - 6} ${y - 26} H${x + 6} V${y - 16} Q${x + 14} ${y - 10} ${x + 14} ${y} V${y + 24} H${x - 14} V${y} Q${x - 14} ${y - 10} ${x - 6} ${y - 16}Z" fill="#CFE6FF" stroke="${INK}" stroke-width="2"/><rect x="${x - 14}" y="${y - 2}" width="28" height="10" fill="${BLUE}"/>`,
    car: (x, y) => `<path d="M${x - 28} ${y + 8} V${y - 2} L${x - 16} ${y - 4} L${x - 8} ${y - 16} H${x + 12} L${x + 20} ${y - 4} L${x + 28} ${y - 2} V${y + 8}Z" fill="${RED}" stroke="${INK}" stroke-width="2"/><circle cx="${x - 14}" cy="${y + 10}" r="6" fill="${INK}"/><circle cx="${x + 14}" cy="${y + 10}" r="6" fill="${INK}"/>`,
    pill: (x, y) => `<g transform="rotate(-35 ${x} ${y})"><rect x="${x - 24}" y="${y - 10}" width="48" height="20" rx="10" fill="#fff" stroke="${INK}" stroke-width="2"/><path d="M${x} ${y - 10} H${x + 14} A10 10 0 0 1 ${x + 14} ${y + 10} H${x}Z" fill="${RED}"/></g>`,
    smoke: (x, y) => [0, 1, 2].map(i => `<circle cx="${x + (i - 1) * 8}" cy="${y}" r="${7 + i}" fill="#9AA6B8" class="sa a-rise" style="--dy:-22px;--dx:${(i - 1) * 6}px;--t:3s;animation-delay:${i}s"/>`).join(''),
    sun: (x, y) => `<g class="sa a-spin" style="--o:${x}px ${y}px;--t:14s">${Array.from({ length: 8 }, (_, i) => { const a = i * Math.PI / 4; return `<line x1="${x + 16 * Math.cos(a)}" y1="${y + 16 * Math.sin(a)}" x2="${x + 24 * Math.cos(a)}" y2="${y + 24 * Math.sin(a)}" stroke="${ORANGE}" stroke-width="3" stroke-linecap="round"/>`; }).join('')}</g><circle cx="${x}" cy="${y}" r="12" fill="${GOLD}"/>`,
    bug: (x, y) => `<ellipse cx="${x}" cy="${y}" rx="16" ry="9" fill="#C5E1A5" stroke="${DGREEN}" stroke-width="2"/>` + [-10, 0, 10].map(d => `<line x1="${x + d}" y1="${y - 9}" x2="${x + d - 3}" y2="${y - 15}" stroke="${DGREEN}" stroke-width="2"/>`).join('')
  };

  // the cold glass: water vapour in the air moves to the cold glass and condenses into droplets; o.labels adds labels
  F.sciGlass = (o = {}) => {
    let s = `<rect x="0" y="262" width="480" height="58" fill="#E9DCC6"/>`;
    for (let i = 0; i < 14; i++) { const x = 40 + (i * 53) % 400, y = 40 + (i * 37) % 190, toL = x < 240;
      s += `<circle cx="${x}" cy="${y}" r="4" fill="${BLUE}" opacity=".8" class="sa a-rise" style="--dx:${toL ? 200 - x : 280 - x}px;--dy:${(160 - y) * 0.6}px;--t:${3 + (i % 4) * 0.6}s;animation-delay:${(i % 5) * 0.7}s"/>`; }
    s += `<path d="M190 70 L200 262 H280 L290 70Z" fill="#EAF6FF" stroke="${GREY}" stroke-width="3"/><path d="M196 120 L203 258 H277 L284 120Z" fill="#B3DDF7"/>`;
    s += `<rect x="214" y="128" width="22" height="18" rx="4" fill="#fff" stroke="#9CC9E8" transform="rotate(12 225 137)"/><rect x="246" y="150" width="20" height="17" rx="4" fill="#fff" stroke="#9CC9E8" transform="rotate(-10 256 158)"/>`;
    [[196, 110], [287, 128], [198, 170], [286, 190], [201, 220], [283, 236], [194, 150], [289, 160]].forEach(([x, y], i) =>
      s += `<g class="sa a-rise" style="--dy:26px;--t:${4 + i % 3}s;animation-delay:${i * 0.5}s"><path d="M${x} ${y - 6} Q${x + 5} ${y + 1} ${x} ${y + 5} Q${x - 5} ${y + 1} ${x} ${y - 6}Z" fill="${BLUE}"/></g>` + `<path d="M${x} ${y - 6} Q${x + 5} ${y + 1} ${x} ${y + 5} Q${x - 5} ${y + 1} ${x} ${y - 6}Z" fill="${BLUE}" opacity=".55"/>`);
    s += `<ellipse cx="240" cy="266" rx="56" ry="6" fill="#9CC9E8" opacity=".7"/>`;
    if (o.labels) s += T(80, 30, 'water vapour in the air', { size: 14, bold: true }) + arrow(96, 38, 120, 70, GREY) + T(400, 100, 'cold glass', { size: 14, bold: true }) + arrow(366, 104, 296, 120, GREY) +
      T(400, 214, 'droplets of water', { size: 14, bold: true }) + arrow(360, 218, 292, 232, GREY) + T(240, 306, 'water vapour condenses on the cold surface', { size: 14 });
    else s += T(240, 306, 'Where did the water on the outside come from?', { size: 15, bold: true });
    return { svg: W(s), a: {} };
  };

  // the two parts of science: what we know (a book of tested ideas) and how we find out (the cycle of enquiry, a dot runs round it)
  F.sciParts = () => {
    let s = box(14, 20, 200, 250, '#FFFBEA', '#E3B505') + T(114, 50, 'What we know', { size: 17, bold: true });
    s += `<path d="M44 110 Q79 96 114 110 V214 Q79 200 44 214Z" fill="#fff" stroke="${INK}" stroke-width="2.4"/><path d="M114 110 Q149 96 184 110 V214 Q149 200 114 214Z" fill="#fff" stroke="${INK}" stroke-width="2.4"/>`;
    for (let i = 0; i < 5; i++) s += `<line x1="56" y1="${128 + i * 16}" x2="102" y2="${124 + i * 16}" stroke="#B0BEC5" stroke-width="2"/><line x1="126" y1="${124 + i * 16}" x2="172" y2="${128 + i * 16}" stroke="#B0BEC5" stroke-width="2"/>`;
    s += `<g class="sa a-pulse" style="--o:114px 78px"><circle cx="114" cy="76" r="14" fill="${GOLD}" stroke="${INK}" stroke-width="2"/><rect x="108" y="88" width="12" height="8" fill="${GREY}"/></g>`;
    s += T(114, 244, 'ideas tested again and again', { size: 13 });
    s += box(232, 20, 234, 250, '#EEF6FF', '#9CC9E8') + T(349, 50, 'How we find out', { size: 17, bold: true });
    const P = [[349, 86, 'Ask a question'], [418, 150, 'Predict'], [349, 214, 'Test fairly'], [280, 150, 'Look at evidence']];
    s += `<circle cx="349" cy="150" r="64" fill="none" stroke="${BLUE}" stroke-width="2.4" class="sa a-flow"/>`;
    s += `<g class="sa a-spin" style="--o:349px 150px;--t:6s"><circle cx="349" cy="86" r="7" fill="${ORANGE}"/></g>`;
    P.forEach(([x, y, t]) => { const w = t.length * 6.4 + 16; s += `<rect x="${x - w / 2}" y="${y - 14}" width="${w}" height="26" rx="13" fill="#fff" stroke="${BLUE}" stroke-width="2"/>` + T(x, y + 4, t, { size: 11, bold: true }); });
    s += T(349, 254, 'new evidence can change our ideas', { size: 13 });
    return { svg: W(s), a: {} };
  };

  // science in daily life: four things we use, the problem each has caused, and how science can help
  F.sciImpact = () => {
    const cols = [['Electricity', 'bolt', 'smoke', 'carbon dioxide', 'sun', 'solar power'], ['Materials', 'bottle', 'bottle', 'plastic waste', 'recycle', 'recycling'],
      ['Transport', 'car', 'smoke', 'air pollution', 'plug', 'electric cars'], ['Medicine', 'pill', 'bug', 'resistant bacteria', 'pill', 'new medicines']];
    let s = T(6, 92, 'we use', { size: 11, anchor: 'start', fill: GREY }) + T(6, 176, 'problem', { size: 11, anchor: 'start', fill: RED }) + T(6, 266, 'solution', { size: 11, anchor: 'start', fill: DGREEN });
    cols.forEach(([name, a, b, bt, c, ct], i) => { const x = 110 + i * 100;
      s += `<rect x="${x - 46}" y="20" width="92" height="292" rx="12" fill="${SOFT}"/>` + T(x, 42, name, { size: 14, bold: true }) + ICON[a](x, 84);
      s += arrow(x, 116, x, 140, GREY) + `<circle cx="${x}" cy="172" r="26" fill="#FDE2E2"/>` + (b === 'bottle' ? ICON.bottle(x, 170) + `<path d="M${x - 26} 194 q8 -6 16 0 t16 0 t16 0" fill="none" stroke="${BLUE}" stroke-width="2"/>` : ICON[b](x, b === 'smoke' ? 178 : 172)) + T(x, 214, bt, { size: 10 });
      s += arrow(x, 222, x, 238, GREY) + (c === 'recycle' ? `<g class="sa a-spin" style="--o:${x}px 262px;--t:6s">${[0, 120, 240].map(r => `<path d="M${x} 248 A14 14 0 0 1 ${x + 12} 255" fill="none" stroke="${DGREEN}" stroke-width="4" transform="rotate(${r} ${x} 262)"/>`).join('')}</g>` : c === 'sun' ? ICON.sun(x, 262) : c === 'plug' ? ICON.car(x, 262).replace(RED, GREEN) : `<g transform="translate(0 0)">${ICON.pill(x, 262).replace(RED, GREEN)}</g>`) + T(x, 300, ct, { size: 11 }); });
    return { svg: W(s), a: {} };
  };

  // the five areas of study, each with its own picture (small animations: bubbles, a moon going round, smoke …)
  F.sciAreas = () => {
    const A = [['Biology', 'living things', 'leaf', '#E8F5E9'], ['Chemistry', 'substances', 'flask', '#E7F6EE'], ['Physics', 'energy and forces', 'bolt', '#FFF6D6'],
      ['Earth science', 'rocks and weather', 'volcano', '#F3EDE8'], ['Astronomy', 'space', 'planet', '#E8EEFF']];
    let s = '';
    A.forEach(([n, d, ic, bg], i) => { const x = 52 + i * 94, y = 130;
      s += `<circle cx="${x}" cy="${y}" r="42" fill="${bg}" stroke="${INK}" stroke-width="2"/>` + ICON[ic](x, y) + T(x, 200, n, { size: 13, bold: true }) + T(x, 218, d, { size: 11, fill: GREY }); });
    s += T(240, 40, 'Areas of study in science', { size: 17, bold: true }) + `<path d="M60 262 H420" stroke="#C9D4E3" stroke-width="2"/>` + T(240, 290, 'Real problems often need several areas together.', { size: 13 });
    return { svg: W(s), a: {} };
  };

  // four scientists at work today, each in a small animated scene
  F.sciJobs = () => {
    let s = '';
    const cell = (x, y, title, area, inner) => box(x, y, 226, 140, '#fff') + inner + T(x + 113, y + 118, title, { size: 13, bold: true }) + T(x + 113, y + 133, area, { size: 11, fill: GREY });
    // water scientist: a test tube of river water, changing colour
    s += cell(10, 10, 'Water scientist', 'chemistry', `<path d="M20 90 q20 -10 40 0 t40 0 t40 0 t40 0 t36 0 V100 H20Z" fill="${SKY}"/>` +
      `<rect x="160" y="22" width="22" height="70" rx="11" fill="#fff" stroke="${INK}" stroke-width="2"/><rect x="162" y="56" width="18" height="34" rx="9" fill="#90CAF9" class="sa a-blink" style="--t:3s"/><rect x="162" y="56" width="18" height="34" rx="9" fill="#A5D6A7" opacity=".5"/>` +
      T(100, 50, 'a sample of river water', { size: 11 }) + arrow(150, 52, 158, 60, GREY));
    // crop scientist: rice plants swaying in salty soil
    s += cell(244, 10, 'Crop scientist', 'biology', `<rect x="254" y="84" width="206" height="16" fill="#D7CCC8"/>` + [0, 1, 2, 3].map(i => { const x = 290 + i * 46;
      return `<g class="sa a-swing" style="--o:${x}px 86px;animation-delay:${i * 0.3}s"><path d="M${x} 86 Q${x - 4} 50 ${x - 10} 28 M${x} 86 Q${x + 4} 52 ${x + 12} 30 M${x} 86 V36" stroke="${GREEN}" stroke-width="3" fill="none"/><circle cx="${x + 12}" cy="30" r="4" fill="${GOLD}"/><circle cx="${x - 10}" cy="28" r="4" fill="${GOLD}"/></g>`; }).join(''));
    // seismologist: a trace that keeps moving
    s += cell(10, 166, 'Seismologist', 'Earth science (and physics)', `<rect x="30" y="180" width="186" height="76" rx="6" fill="${SOFT}"/>` +
      `<path d="M30 218 h30 l6 -18 l8 36 l8 -40 l8 44 l8 -30 l6 16 h20 l6 -10 l6 14 l6 -6 h60" fill="none" stroke="${RED}" stroke-width="2.4" class="sa a-draw"/>`);
    // sound engineer: sound waves from a road are stopped by a wall before the school
    s += cell(244, 166, 'Sound engineer', 'physics', `<rect x="256" y="234" width="60" height="16" fill="#90A4AE"/>` + ICON.car(286, 222) +
      [0, 1, 2].map(i => `<path d="M${318 + i * 12} 196 q10 20 0 40" fill="none" stroke="${BLUE}" stroke-width="2.4" class="sa a-blink" style="animation-delay:${i * 0.4}s;--t:1.6s"/>`).join('') +
      `<rect x="362" y="180" width="12" height="70" fill="#8D6E63"/><path d="M396 250 V206 L420 190 L444 206 V250Z" fill="#FFE0B2" stroke="${INK}" stroke-width="2"/>` + T(420, 240, 'school', { size: 10 }));
    return { svg: W(s), a: {} };
  };

  // scientists build on each other's work: a timeline, each discovery leads to the next
  F.sciTimeline = () => {
    const P = [['about 1000 years ago', 'Ibn al-Haytham', 'light and seeing'], ['early 1900s', 'Marie Curie', 'radioactivity'], ['1950s', 'Rosalind Franklin', 'shape of DNA'], ['1970s', 'Tu Youyou', 'malaria medicine']];
    let s = `<line x1="30" y1="170" x2="452" y2="170" stroke="${INK}" stroke-width="4"/>` + arrow(440, 170, 466, 170, INK) + `<circle cx="30" cy="170" r="6" fill="${ORANGE}" class="sa a-rise" style="--dx:420px;--dy:0px;--t:6s"/>`;
    const pic = [
      (x, y) => `<ellipse cx="${x}" cy="${y}" rx="22" ry="12" fill="#fff" stroke="${INK}" stroke-width="2"/><circle cx="${x}" cy="${y}" r="7" fill="${BLUE}"/>` + `<path d="M${x - 46} ${y - 18} L${x - 24} ${y - 4}" stroke="${GOLD}" stroke-width="3" class="sa a-flow"/>`,
      (x, y) => `<circle cx="${x}" cy="${y}" r="6" fill="${RED}"/>` + [0, 60, 120].map(r => `<ellipse cx="${x}" cy="${y}" rx="24" ry="9" fill="none" stroke="${PURPLE}" stroke-width="2" transform="rotate(${r} ${x} ${y})"/>`).join('') + `<g class="sa a-spin" style="--o:${x}px ${y}px;--t:3s"><circle cx="${x + 24}" cy="${y}" r="3.5" fill="${BLUE}"/></g>`,
      (x, y) => { let d = ''; for (let i = 0; i < 6; i++) { const yy = y - 24 + i * 9; d += `<line x1="${x - 12 * Math.cos(i * 0.9)}" y1="${yy}" x2="${x + 12 * Math.cos(i * 0.9)}" y2="${yy}" stroke="${GREY}" stroke-width="2"/>`; }
        return `<g class="sa a-swing" style="--o:${x}px ${y}px">${d}<path d="M${x - 12} ${y - 24} C${x + 22} ${y - 10} ${x - 22} ${y + 6} ${x + 12} ${y + 22}" fill="none" stroke="${BLUE}" stroke-width="3"/><path d="M${x + 12} ${y - 24} C${x - 22} ${y - 10} ${x + 22} ${y + 6} ${x - 12} ${y + 22}" fill="none" stroke="${RED}" stroke-width="3"/></g>`; },
      (x, y) => ICON.leaf(x - 12, y) + ICON.pill(x + 16, y + 10)];
    P.forEach(([when, who, what], i) => { const x = 78 + i * 108, up = i % 2 === 0, y = up ? 96 : 244;
      s += `<circle cx="${x}" cy="170" r="9" fill="${GOLD}" stroke="${INK}" stroke-width="2"/><line x1="${x}" y1="${up ? 160 : 180}" x2="${x}" y2="${up ? 130 : 210}" stroke="${GREY}" stroke-width="2"/>`;
      s += `<circle cx="${x}" cy="${y}" r="34" fill="#fff" stroke="#C9D4E3" stroke-width="2"/>` + pic[i](x, y);
      const ty = up ? 18 : 291; s += T(x, ty, who, { size: 12, bold: true }) + T(x, ty + 13, when, { size: 10, fill: GREY }) + T(x, ty + 26, what, { size: 10, fill: BLUE }); });
    return { svg: W(s), a: {} };
  };

  // ideas change with evidence: the old Earth-centred model and the Sun-centred model, both turning
  F.sciModels = () => {
    const orbit = (cx, cy, r, c, body, t) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#C9D4E3" stroke-width="2" stroke-dasharray="4 4"/><g class="sa a-spin" style="--o:${cx}px ${cy}px;--t:${t}s">${body(cx + r, cy)}</g>`;
    const earth = (x, y, r = 14) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${BLUE}"/><path d="M${x - r * 0.6} ${y - 3} q${r * 0.4} -${r * 0.5} ${r * 0.9} 0 q-${r * 0.2} ${r * 0.6} -${r * 0.9} 0Z" fill="${GREEN}"/>`;
    const sun = (x, y) => `<circle cx="${x}" cy="${y}" r="16" fill="${GOLD}" stroke="${ORANGE}" stroke-width="3"/>`;
    let s = box(12, 16, 220, 262, '#FFF4F4', '#F3B6B6') + T(122, 44, 'Old idea', { size: 16, bold: true, fill: RED }) + earth(122, 150, 18) + orbit(122, 150, 80, '', sun, 8) + T(122, 264, 'the Sun moves around the Earth', { size: 12 });
    s += box(248, 16, 220, 262, '#F0FAF3', '#A5D6A7') + T(358, 44, 'Idea today', { size: 16, bold: true, fill: DGREEN }) + `<circle cx="358" cy="150" r="22" fill="${GOLD}" stroke="${ORANGE}" stroke-width="3"/>` + orbit(358, 150, 80, '', (x, y) => earth(x, y), 8) + T(358, 264, 'the Earth moves around the Sun', { size: 12 });
    s += T(240, 308, 'Careful observations of the planets changed the idea.', { size: 13, bold: true });
    return { svg: W(s), a: {} };
  };
  // ---------- more icons (about 50 px, centred on x, y) for the lesson layouts below ----------
  const ring = (x, y, r, c) => `<circle cx="${x}" cy="${y}" r="${r}" fill="none" stroke="${c}" stroke-width="3"/>`;
  Object.assign(ICON, {
    magnifier: (x, y) => `<g class="sa a-swing" style="--o:${x}px ${y}px">${ring(x - 6, y - 6, 15, INK)}<line x1="${x + 5}" y1="${y + 5}" x2="${x + 20}" y2="${y + 20}" stroke="${INK}" stroke-width="6" stroke-linecap="round"/></g>`,
    mountain: (x, y) => `<path d="M${x - 26} ${y + 20} L${x - 4} ${y - 18} L${x + 6} ${y - 2} L${x + 12} ${y - 10} L${x + 26} ${y + 20}Z" fill="#B0BEC5" stroke="${INK}" stroke-width="2"/><path d="M${x - 4} ${y - 18} V${y - 30} L${x + 8} ${y - 26} L${x - 4} ${y - 22}" fill="${RED}" stroke="${INK}" stroke-width="1.5"/>`,
    ear: (x, y) => `<path d="M${x - 8} ${y + 18} C${x - 22} ${y + 6} ${x - 18} ${y - 22} ${x + 2} ${y - 22} C${x + 18} ${y - 22} ${x + 20} ${y - 2} ${x + 6} ${y + 6} C${x} ${y + 10} ${x + 4} ${y + 20} ${x - 8} ${y + 18}Z" fill="#FFD8B5" stroke="${INK}" stroke-width="2"/>` +
      [0, 1].map(i => `<path d="M${x + 16 + i * 8} ${y - 14} q8 10 0 20" fill="none" stroke="${BLUE}" stroke-width="2.4" class="sa a-blink" style="animation-delay:${i * 0.5}s"/>`).join(''),
    team: (x, y) => [-14, 14].map((d, i) => `<circle cx="${x + d}" cy="${y - 10}" r="9" fill="${i ? GOLD : '#90CAF9'}" stroke="${INK}" stroke-width="2"/><path d="M${x + d - 14} ${y + 20} q14 -26 28 0" fill="${i ? GOLD : '#90CAF9'}" stroke="${INK}" stroke-width="2"/>`).join('') + `<path d="M${x - 6} ${y + 8} h12" stroke="${INK}" stroke-width="3"/>`,
    flex: (x, y) => `<g class="sa a-spin" style="--o:${x}px ${y}px;--t:6s"><path d="M${x - 18} ${y} A18 18 0 0 1 ${x + 14} ${y - 11}" fill="none" stroke="${GREEN}" stroke-width="4"/><path d="M${x + 18} ${y} A18 18 0 0 1 ${x - 14} ${y + 11}" fill="none" stroke="${BLUE}" stroke-width="4"/><path d="M${x + 14} ${y - 21} l2 11 l-11 1" fill="none" stroke="${GREEN}" stroke-width="3"/><path d="M${x - 14} ${y + 21} l-2 -11 l11 -1" fill="none" stroke="${BLUE}" stroke-width="3"/></g>`,
    scales: (x, y) => `<line x1="${x}" y1="${y - 20}" x2="${x}" y2="${y + 20}" stroke="${INK}" stroke-width="3"/><path d="M${x - 14} ${y + 22} h28" stroke="${INK}" stroke-width="4"/><g class="sa a-swing" style="--o:${x}px ${y - 18}px"><line x1="${x - 24}" y1="${y - 18}" x2="${x + 24}" y2="${y - 18}" stroke="${INK}" stroke-width="3"/><path d="M${x - 32} ${y} h16 l-8 -18Z M${x + 16} ${y} h16 l-8 -18Z" fill="${GOLD}" stroke="${INK}" stroke-width="1.5"/></g>`,
    question: (x, y) => `<circle cx="${x}" cy="${y}" r="22" fill="#FFF6D6" stroke="${INK}" stroke-width="2"/><text x="${x}" y="${y + 10}" font-size="30" font-weight="700" fill="${INK}" text-anchor="middle" class="sa a-blink" style="--t:2s">?</text>`,
    tick: (x, y) => `<circle cx="${x}" cy="${y}" r="22" fill="#E3F4E6"/><path d="M${x - 11} ${y + 1} l7 8 l15 -17" fill="none" stroke="${DGREEN}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>`,
    cross: (x, y) => `<circle cx="${x}" cy="${y}" r="22" fill="#FDE2E2"/><path d="M${x - 9} ${y - 9} l18 18 M${x + 9} ${y - 9} l-18 18" stroke="${RED}" stroke-width="5" stroke-linecap="round"/>`,
    clock: (x, y) => `<circle cx="${x}" cy="${y}" r="22" fill="#fff" stroke="${INK}" stroke-width="2.5"/><line x1="${x}" y1="${y}" x2="${x}" y2="${y - 12}" stroke="${INK}" stroke-width="3"/><g class="sa a-spin" style="--o:${x}px ${y}px;--t:4s"><line x1="${x}" y1="${y}" x2="${x + 16}" y2="${y}" stroke="${RED}" stroke-width="2"/></g>`,
    thermo: (x, y) => `<rect x="${x - 6}" y="${y - 26}" width="12" height="42" rx="6" fill="#fff" stroke="${INK}" stroke-width="2"/><circle cx="${x}" cy="${y + 18}" r="9" fill="${RED}" stroke="${INK}" stroke-width="2"/><rect x="${x - 2.5}" y="${y - 14}" width="5" height="30" fill="${RED}" class="sa a-pulse" style="--o:${x}px ${y + 16}px"/>`,
    beaker: (x, y) => `<path d="M${x - 20} ${y - 24} V${y + 20} Q${x - 20} ${y + 24} ${x - 16} ${y + 24} H${x + 16} Q${x + 20} ${y + 24} ${x + 20} ${y + 20} V${y - 24}" fill="#fff" stroke="${INK}" stroke-width="2.4"/><rect x="${x - 18}" y="${y - 2}" width="36" height="24" fill="${SKY}"/>`,
    ruler: (x, y) => `<rect x="${x - 8}" y="${y - 26}" width="16" height="52" fill="${GOLD}" stroke="${INK}" stroke-width="2"/>` + Array.from({ length: 6 }, (_, i) => `<line x1="${x - 8}" y1="${y - 20 + i * 9}" x2="${x - (i % 2 ? 2 : -2)}" y2="${y - 20 + i * 9}" stroke="${INK}" stroke-width="1.5"/>`).join(''),
    plant: (x, y) => `<rect x="${x - 12}" y="${y + 8}" width="24" height="16" fill="#A1887F" stroke="${INK}" stroke-width="2"/><g class="sa a-swing" style="--o:${x}px ${y + 8}px"><path d="M${x} ${y + 8} V${y - 16}" stroke="${DGREEN}" stroke-width="3"/><path d="M${x} ${y - 4} q-16 -4 -16 -16 q14 0 16 12Z M${x} ${y - 12} q16 -4 16 -14 q-14 0 -16 12Z" fill="${GREEN}"/></g>`,
    sadplant: (x, y) => ICON.plant(x, y) + `<text x="${x + 22}" y="${y - 14}" font-size="22" font-weight="700" fill="${RED}">?</text>`,
    hairflame: (x, y) => `<circle cx="${x - 6}" cy="${y - 6}" r="13" fill="#FFD8B5" stroke="${INK}" stroke-width="2"/><path d="M${x - 19} ${y - 10} q-6 20 -2 34 M${x - 15} ${y - 14} q-4 22 0 36" stroke="#6D4C41" stroke-width="3" fill="none"/>` + ICON.flame(x + 16, y + 10),
    flame: (x, y) => `<g class="sa a-pulse" style="--o:${x}px ${y + 12}px"><path d="M${x} ${y - 18} C${x + 14} ${y - 2} ${x + 12} ${y + 12} ${x} ${y + 14} C${x - 12} ${y + 12} ${x - 14} ${y - 2} ${x} ${y - 18}Z" fill="${ORANGE}"/><path d="M${x} ${y - 4} C${x + 6} ${y + 4} ${x + 5} ${y + 10} ${x} ${y + 12} C${x - 5} ${y + 10} ${x - 6} ${y + 4} ${x} ${y - 4}Z" fill="${GOLD}"/></g>`,
    cup: (x, y) => `<path d="M${x - 14} ${y - 14} L${x - 10} ${y + 22} H${x + 10} L${x + 14} ${y - 14}Z" fill="#FFB74D" stroke="${INK}" stroke-width="2"/><line x1="${x + 4}" y1="${y - 14}" x2="${x + 10}" y2="${y - 30}" stroke="${RED}" stroke-width="3"/>`,
    tubeAt: (x, y) => `<g transform="rotate(-60 ${x} ${y})"><rect x="${x - 7}" y="${y - 24}" width="14" height="44" rx="7" fill="#fff" stroke="${INK}" stroke-width="2"/><rect x="${x - 5}" y="${y + 2}" width="10" height="16" rx="5" fill="${SKY}"/></g>` + ICON.flame(x - 6, y + 22) +
      [0, 1].map(i => `<circle cx="${x + 18}" cy="${y - 8}" r="3" fill="${BLUE}" class="sa a-rise" style="--dx:20px;--dy:-10px;--t:1.6s;animation-delay:${i * 0.8}s"/>`).join(''),
    nolabel: (x, y) => `<path d="M${x - 6} ${y - 26} H${x + 6} V${y - 16} L${x + 16} ${y - 6} V${y + 24} H${x - 16} V${y - 6} L${x - 6} ${y - 16}Z" fill="#E0E0E0" stroke="${INK}" stroke-width="2"/><rect x="${x - 12}" y="${y}" width="24" height="16" fill="#fff" stroke="${GREY}" stroke-dasharray="3 2"/><text x="${x}" y="${y + 13}" font-size="13" font-weight="700" fill="${RED}" text-anchor="middle">?</text>`,
    wheat: (x, y) => `<g class="sa a-swing" style="--o:${x}px ${y + 24}px"><path d="M${x} ${y + 24} V${y - 20}" stroke="#C49A3A" stroke-width="3"/>` + [0, 1, 2, 3].map(i => `<ellipse cx="${x - 6}" cy="${y - 16 + i * 8}" rx="6" ry="3.5" fill="${GOLD}" transform="rotate(-30 ${x - 6} ${y - 16 + i * 8})"/><ellipse cx="${x + 6}" cy="${y - 16 + i * 8}" rx="6" ry="3.5" fill="${GOLD}" transform="rotate(30 ${x + 6} ${y - 16 + i * 8})"/>`).join('') + `</g>`,
    phone: (x, y) => `<rect x="${x - 14}" y="${y - 24}" width="28" height="48" rx="5" fill="${INK}"/><rect x="${x - 11}" y="${y - 19}" width="22" height="34" fill="#90CAF9"/><path d="M${x - 6} ${y - 8} h12 v8 h-8 l-4 4Z" fill="#fff" class="sa a-blink"/>`,
    satellite: (x, y) => `<g class="sa a-swing" style="--o:${x}px ${y}px"><rect x="${x - 7}" y="${y - 7}" width="14" height="14" fill="${GREY}" stroke="${INK}" stroke-width="2"/><rect x="${x - 28}" y="${y - 5}" width="18" height="10" fill="${BLUE}"/><rect x="${x + 10}" y="${y - 5}" width="18" height="10" fill="${BLUE}"/></g>` + ICON.cloudrain(x, y + 18).replace(/r="10"/g, 'r="6"'),
    cloudrain: (x, y) => `<path d="M${x - 16} ${y} a8 8 0 0 1 4 -14 a11 11 0 0 1 21 -2 a8 8 0 0 1 7 16Z" fill="#CFD8DC"/>` + [0, 1, 2].map(i => `<line x1="${x - 8 + i * 8}" y1="${y + 4}" x2="${x - 11 + i * 8}" y2="${y + 11}" stroke="${BLUE}" stroke-width="2" class="sa a-rise" style="--dy:8px;--t:1s;animation-delay:${i * 0.3}s"/>`).join(''),
    scanner: (x, y) => `<rect x="${x - 26}" y="${y - 20}" width="52" height="34" rx="6" fill="#fff" stroke="${INK}" stroke-width="2"/><path d="M${x - 18} ${y - 3} h8 l4 -10 l6 20 l4 -10 h14" fill="none" stroke="${GREEN}" stroke-width="2.4" class="sa a-draw"/><rect x="${x - 6}" y="${y + 14}" width="12" height="10" fill="${GREY}"/>`,
    factory: (x, y) => `<path d="M${x - 26} ${y + 22} V${y - 2} L${x - 12} ${y + 6} V${y - 2} L${x + 2} ${y + 6} V${y - 20} H${x + 12} V${y + 22}Z" fill="#90A4AE" stroke="${INK}" stroke-width="2"/>` + ICON.smoke(x + 7, y - 24),
    turbine: (x, y) => `<line x1="${x}" y1="${y - 8}" x2="${x}" y2="${y + 26}" stroke="${INK}" stroke-width="3"/><g class="sa a-spin" style="--o:${x}px ${y - 8}px;--t:3s">${[0, 120, 240].map(r => `<path d="M${x} ${y - 8} L${x - 3} ${y - 32} L${x + 3} ${y - 32}Z" fill="#fff" stroke="${INK}" stroke-width="1.5" transform="rotate(${r} ${x} ${y - 8})"/>`).join('')}</g><circle cx="${x}" cy="${y - 8}" r="3" fill="${INK}"/>`,
    solar: (x, y) => `<path d="M${x - 24} ${y + 10} L${x - 14} ${y - 12} H${x + 24} L${x + 14} ${y + 10}Z" fill="${BLUE}" stroke="${INK}" stroke-width="2"/><path d="M${x - 19} ${y - 1} H${x + 19} M${x - 4} ${y - 12} L${x - 10} ${y + 10} M${x + 9} ${y - 12} L${x + 3} ${y + 10}" stroke="#90CAF9" stroke-width="1.5"/><line x1="${x}" y1="${y + 10}" x2="${x}" y2="${y + 24}" stroke="${INK}" stroke-width="3"/>`,
    report: (x, y) => `<rect x="${x - 18}" y="${y - 24}" width="36" height="48" rx="3" fill="#fff" stroke="${INK}" stroke-width="2"/>` + [0, 1, 2, 3].map(i => `<line x1="${x - 11}" y1="${y - 14 + i * 9}" x2="${x + 11}" y2="${y - 14 + i * 9}" stroke="#B0BEC5" stroke-width="2"/>`).join('') + `<path d="M${x - 8} ${y + 14} l18 -14" stroke="${GREEN}" stroke-width="3" class="sa a-draw"/>`,
    globe: (x, y) => `<circle cx="${x}" cy="${y}" r="22" fill="${SKY}" stroke="${INK}" stroke-width="2"/><g class="sa a-swing" style="--o:${x}px ${y}px"><path d="M${x - 12} ${y - 12} q8 4 4 12 q-8 2 -6 12 M${x + 6} ${y - 18} q6 8 12 6 M${x + 4} ${y + 6} q8 0 10 10" fill="none" stroke="${GREEN}" stroke-width="5" stroke-linecap="round"/></g>`,
    heart: (x, y) => `<g class="sa a-pulse" style="--o:${x}px ${y}px"><path d="M${x} ${y + 18} C${x - 30} ${y} ${x - 20} ${y - 24} ${x} ${y - 10} C${x + 20} ${y - 24} ${x + 30} ${y} ${x} ${y + 18}Z" fill="${RED}"/></g>`,
    megaphone: (x, y) => `<path d="M${x - 20} ${y - 6} L${x + 10} ${y - 20} V${y + 20} L${x - 20} ${y + 6}Z" fill="${GOLD}" stroke="${INK}" stroke-width="2"/><rect x="${x - 26}" y="${y - 6}" width="8" height="12" fill="${INK}"/>` + [0, 1].map(i => `<path d="M${x + 16 + i * 7} ${y - 10} q6 10 0 20" fill="none" stroke="${RED}" stroke-width="2.4" class="sa a-blink" style="animation-delay:${i * 0.4}s"/>`).join(''),
    goggles: (x, y) => `<rect x="${x - 26}" y="${y - 10}" width="52" height="22" rx="11" fill="#B3E5FC" stroke="${INK}" stroke-width="2.4"/><line x1="${x}" y1="${y - 10}" x2="${x}" y2="${y + 12}" stroke="${INK}" stroke-width="2"/><path d="M${x - 26} ${y} h-6 M${x + 26} ${y} h6" stroke="${INK}" stroke-width="3"/>`,
    hands: (x, y) => `<path d="M${x - 20} ${y + 16} V${y - 8} q0 -6 5 -6 q5 0 5 6 V${y + 2} V${y - 14} q0 -6 5 -6 q5 0 5 6 V${y + 2} V${y - 12} q0 -6 5 -6 q5 0 5 6 V${y + 16}Z" fill="#FFD8B5" stroke="${INK}" stroke-width="2"/>` + [0, 1, 2].map(i => `<circle cx="${x - 10 + i * 10}" cy="${y + 24}" r="3" fill="${BLUE}" class="sa a-rise" style="--dy:10px;--t:1.4s;animation-delay:${i * 0.4}s"/>`).join(''),
    book: (x, y) => `<path d="M${x - 24} ${y - 14} Q${x - 12} ${y - 20} ${x} ${y - 14} V${y + 18} Q${x - 12} ${y + 12} ${x - 24} ${y + 18}Z M${x + 24} ${y - 14} Q${x + 12} ${y - 20} ${x} ${y - 14} V${y + 18} Q${x + 12} ${y + 12} ${x + 24} ${y + 18}Z" fill="#fff" stroke="${INK}" stroke-width="2"/>`,
    dart: (x, y) => ring(x, y, 22, RED) + ring(x, y, 12, RED) + `<circle cx="${x}" cy="${y}" r="4" fill="${RED}"/>`,
    car2: (x, y) => ICON.car(x, y) + [0, 1].map(i => `<path d="M${x + 30 + i * 7} ${y - 8} q6 8 0 16" fill="none" stroke="${GREEN}" stroke-width="2.4" class="sa a-blink" style="animation-delay:${i * 0.4}s"/>`).join('')
  });
  const wrap = (t, n) => { const out = []; let line = ''; String(t).split(' ').forEach(w => { if ((line + ' ' + w).trim().length > n && line) { out.push(line); line = w; } else line = (line + ' ' + w).trim(); }); if (line) out.push(line); return out; };
  const lines = (x, y, t, n, o = {}) => wrap(t, n).map((l, i) => T(x, y + i * ((o.size || 12) + 3), l, o)).join('');

  // cards: o.title, o.cards = [{icon, t (title), d (short text), ok: true|false (tick or cross badge)}], o.cols (default: all in one row up to 4)
  F.sciCards = (o = {}) => {
    const C = o.cards || [], n = C.length, cols = o.cols || Math.min(n, 4), rows = Math.ceil(n / cols), top = o.title ? 34 : 8;
    const cw = (464 - (cols - 1) * 8) / cols, ch = (312 - top - (rows - 1) * 8) / rows, small = ch < 140;
    let s = o.title ? T(240, 24, o.title, { size: 16, bold: true }) : '';
    const tw = Math.max(10, Math.floor(cw / 8)), dw = Math.max(12, Math.floor(cw / 6.4));
    C.forEach((c, i) => { const x = 8 + (i % cols) * (cw + 8), y = top + Math.floor(i / cols) * (ch + 8), cx = x + cw / 2;
      const tall = (c.icon ? 60 : 0) + wrap(c.t, tw).length * 16 + (c.d ? wrap(c.d, dw).length * 14 + 4 : 0), iy = y + Math.max(small ? 30 : 34, (ch - tall) / 2 + 28);
      s += `<rect x="${x}" y="${y}" width="${cw}" height="${ch}" rx="12" fill="${c.ok === false ? '#FFF4F4' : c.ok ? '#F0FAF3' : SOFT}" stroke="${c.ok === false ? '#F3B6B6' : c.ok ? '#A5D6A7' : '#C9D4E3'}" stroke-width="1.5"/>`;
      if (c.icon && ICON[c.icon]) s += ICON[c.icon](cx, iy);
      if (c.ok != null) s += `<g transform="translate(${x + cw - 22} ${y + 22}) scale(.55) translate(${-(x + cw - 22)} ${-(y + 22)})">${ICON[c.ok ? 'tick' : 'cross'](x + cw - 22, y + 22)}</g>`;
      const ty = c.icon ? iy + 46 : iy - 12; s += lines(cx, ty, c.t, tw, { size: 13, bold: true });
      if (c.d) s += lines(cx, ty + 16 * wrap(c.t, tw).length + 2, c.d, dw, { size: 11, fill: GREY }); });
    return { svg: W(s), a: {} };
  };

  // a cycle of steps round a circle, with a dot going round: o.steps = [...], o.title, o.centre
  F.sciCycle = (o = {}) => {
    const P = o.steps || [], n = P.length, cx = 240, cy = o.title ? 174 : 162, r = 112, rx = n > 5 ? 172 : 140;   // an ellipse, so long labels do not touch
    let s = (o.title ? T(240, 22, o.title, { size: 16, bold: true }) : '') + `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${r}" fill="none" stroke="${BLUE}" stroke-width="2.4" class="sa a-flow"/>`;
    s += `<g transform="translate(${cx} ${cy}) scale(${rx / r} 1) translate(${-cx} ${-cy})"><g class="sa a-spin" style="--o:${cx}px ${cy}px;--t:${n * 1.6}s"><circle cx="${cx}" cy="${cy - r}" r="6" fill="${ORANGE}"/></g></g>`;
    if (o.centre) s += lines(cx, cy - 4, o.centre, 16, { size: 13, bold: true, fill: BLUE });
    P.forEach((t, i) => { const a = -Math.PI / 2 + i * 2 * Math.PI / n, x = cx + rx * Math.cos(a), y = cy + r * Math.sin(a), L = wrap(t, 14), w = Math.max(...L.map(l => l.length)) * 6.6 + 18, h = L.length * 14 + 10;
      s += `<rect x="${x - w / 2}" y="${y - h / 2}" width="${w}" height="${h}" rx="${Math.min(13, h / 2)}" fill="#fff" stroke="${BLUE}" stroke-width="2"/>` + T(x - w / 2 + 9, y - h / 2 - 2, String(i + 1), { size: 10, fill: ORANGE, bold: true, anchor: 'start' }) + lines(x, y - h / 2 + 17, t, 14, { size: 11.5, bold: true }); });
    return { svg: W(s), a: {} };
  };

  // steps in a row with arrows and a dot moving along: o.steps = [{icon, t}], o.title
  F.sciFlow = (o = {}) => {
    const P = o.steps || [], n = P.length, gap = 464 / n, y = o.title ? 150 : 130;
    let s = (o.title ? T(240, 26, o.title, { size: 16, bold: true }) : '') + `<line x1="${8 + gap / 2}" y1="${y}" x2="${8 + gap * (n - 0.5)}" y2="${y}" stroke="#C9D4E3" stroke-width="3"/>` +
      `<circle cx="${8 + gap / 2}" cy="${y}" r="6" fill="${ORANGE}" class="sa a-rise" style="--dx:${gap * (n - 1)}px;--dy:0px;--t:${n * 1.4}s"/>`;
    P.forEach((p, i) => { const x = 8 + gap * (i + 0.5);
      s += `<circle cx="${x}" cy="${y}" r="38" fill="#fff" stroke="${INK}" stroke-width="2"/>` + (ICON[p.icon] ? ICON[p.icon](x, y) : T(x, y + 9, i + 1, { size: 26, bold: true, fill: BLUE })) + lines(x, y + 62, p.t, Math.max(10, Math.floor(gap / 7.5)), { size: 12, bold: true });
      if (p.d) s += lines(x, y + 62 + 15 * wrap(p.t, Math.max(10, Math.floor(gap / 7.5))).length, p.d, Math.max(12, Math.floor(gap / 6.2)), { size: 10.5, fill: GREY });
      if (i < n - 1) s += arrow(x + 42, y, x + gap - 44, y, GREY); });
    return { svg: W(s), a: {} };
  };

  // fair test variables: o.change, o.measure, o.same (list), icons o.ic = [change, measure]
  F.sciVars = (o = {}) => {
    const col = (x, head, c, icon, items) => box(x, 40, 148, 270, '#fff', c) + `<rect x="${x}" y="40" width="148" height="34" rx="12" fill="${c}"/>` + T(x + 74, 62, head, { size: 13, bold: true, fill: '#fff' }) + (icon ? ICON[icon](x + 74, 124) : '') +
      items.map((t, i) => lines(x + 74, 186 + i * 34, t, 20, { size: 12 })).join('');
    let s = T(240, 26, o.title || 'Planning a fair test', { size: 16, bold: true });
    s += col(8, 'I change', BLUE, o.ic && o.ic[0], [o.change || '', '(independent variable)']) + col(166, 'I measure', ORANGE, o.ic && o.ic[1], [o.measure || '', '(dependent variable)']) + col(324, 'I keep the same', DGREEN, 'scales', (o.same || []).concat(['(control variables)']));
    return { svg: W(s), a: {} };
  };

  // accurate and precise: four targets with darts
  F.sciTargets = () => {
    const sets = [['accurate and precise', [[0, 0], [4, -3], [-3, 3], [2, 4]], true], ['precise, not accurate', [[30, -26], [34, -22], [27, -21], [32, -29]], false], ['accurate, not precise', [[-22, 8], [18, -20], [8, 24], [-12, -18]], false], ['neither', [[-34, 26], [22, 32], [36, -6], [-30, -30]], false]];
    let s = '';
    sets.forEach(([t, hits, best], i) => { const x = 62 + i * 118, y = 140;
      s += [52, 38, 24, 10].map((r, k) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${k % 2 ? '#fff' : (k === 3 ? RED : '#FDE2E2')}" stroke="${RED}" stroke-width="1.5"/>`).join('');
      hits.forEach(([dx, dy], k) => { s += `<g class="sa a-rise" style="--dx:0px;--dy:0px;--t:${3 + k * 0.3}s"><circle cx="${x + dx}" cy="${y + dy}" r="5" fill="${INK}"/></g>`; });
      s += lines(x, 222, t, 13, { size: 12, bold: true, fill: best ? DGREEN : INK }); });
    s += T(240, 34, 'Four students each measure the same thing four times', { size: 14, bold: true }) + T(240, 290, 'accurate = close to the true value  ·  precise = close to each other', { size: 12, fill: GREY });
    return { svg: W(s), a: {} };
  };

  // hazard symbols (red diamonds); o.only = list of keys to show
  const HZ = {
    toxic: ['Acutely toxic', (x, y) => `<circle cx="${x}" cy="${y - 6}" r="12" fill="${INK}"/><rect x="${x - 7}" y="${y + 2}" width="14" height="8" fill="${INK}"/><circle cx="${x - 5}" cy="${y - 7}" r="3.5" fill="#fff"/><circle cx="${x + 5}" cy="${y - 7}" r="3.5" fill="#fff"/><path d="M${x - 16} ${y + 12} L${x + 16} ${y + 22} M${x + 16} ${y + 12} L${x - 16} ${y + 22}" stroke="${INK}" stroke-width="4"/>`],
    harmful: ['Moderate hazard', (x, y) => `<rect x="${x - 4}" y="${y - 18}" width="8" height="24" rx="3" fill="${INK}"/><circle cx="${x}" cy="${y + 14}" r="5" fill="${INK}"/>`],
    flammable: ['Flammable', (x, y) => `<path d="M${x} ${y - 20} C${x + 16} ${y - 2} ${x + 12} ${y + 12} ${x} ${y + 14} C${x - 12} ${y + 12} ${x - 16} ${y - 2} ${x} ${y - 20}Z" fill="${INK}"/><rect x="${x - 16}" y="${y + 16}" width="32" height="5" fill="${INK}"/>`],
    corrosive: ['Corrosive', (x, y) => `<rect x="${x - 18}" y="${y - 20}" width="10" height="14" fill="${INK}" transform="rotate(30 ${x - 13} ${y - 13})"/><rect x="${x + 6}" y="${y - 20}" width="10" height="14" fill="${INK}" transform="rotate(-30 ${x + 11} ${y - 13})"/><circle cx="${x - 9}" cy="${y - 2}" r="2.5" fill="${INK}" class="sa a-rise" style="--dy:10px;--t:1.5s"/><circle cx="${x + 9}" cy="${y - 2}" r="2.5" fill="${INK}" class="sa a-rise" style="--dy:10px;--t:1.5s;animation-delay:.7s"/><path d="M${x - 20} ${y + 18} h14 l2 -6 l2 6 h22" stroke="${INK}" stroke-width="4" fill="none"/>`],
    environment: ['Hazard to the environment', (x, y) => `<path d="M${x - 10} ${y + 16} V${y - 8} M${x - 10} ${y - 4} l-8 -10 M${x - 10} ${y} l7 -12" stroke="${INK}" stroke-width="3" fill="none"/><path d="M${x + 2} ${y + 12} q8 -10 16 0 q-8 10 -16 0Z M${x + 18} ${y + 12} l5 -5 v10Z" fill="${INK}"/><path d="M${x - 20} ${y + 20} h40" stroke="${INK}" stroke-width="3"/>`],
    health: ['Health hazard', (x, y) => `<circle cx="${x}" cy="${y - 14}" r="6" fill="${INK}"/><path d="M${x - 10} ${y + 20} V${y - 2} q10 -8 20 0 V${y + 20}Z" fill="${INK}"/><path d="M${x} ${y} l3 6 l6 -2 l-3 6 l5 4 l-7 1 l0 6 l-4 -5 l-4 5 l0 -6 l-7 -1 l5 -4 l-3 -6 l6 2Z" fill="#fff"/>`]
  };
  F.sciHazards = (o = {}) => {
    const keys = o.only || Object.keys(HZ), n = keys.length, cols = Math.min(n, 3), rows = Math.ceil(n / cols);
    let s = '';
    keys.forEach((k, i) => { const cw = 480 / cols, x = cw * (i % cols) + cw / 2, y = rows > 1 ? 78 + Math.floor(i / cols) * 150 : 140;
      s += `<g class="${i === 0 ? '' : ''}"><path d="M${x} ${y - 46} L${x + 46} ${y} L${x} ${y + 46} L${x - 46} ${y}Z" fill="#fff" stroke="${RED}" stroke-width="6" stroke-linejoin="round"/></g>` + HZ[k][1](x, y) + T(x, y + 66, HZ[k][0], { size: 12.5, bold: true }); });
    return { svg: W(s), a: {} };
  };

  // laboratory apparatus with names; the Bunsen flame flickers
  F.sciApparatus = () => {
    let s = '';
    const base = 250, lab = (x, t) => lines(x, base + 26, t, 12, { size: 12, bold: true });
    // test tube in a rack
    s += `<rect x="38" y="90" width="18" height="120" rx="9" fill="#fff" stroke="${INK}" stroke-width="2.4"/><rect x="40" y="160" width="14" height="48" rx="7" fill="${SKY}"/><rect x="20" y="196" width="54" height="10" fill="#C99A5B"/><rect x="24" y="206" width="6" height="44" fill="#C99A5B"/><rect x="64" y="206" width="6" height="44" fill="#C99A5B"/>` + lab(47, 'test tube');
    // measuring cylinder
    s += `<path d="M118 70 V244 H150 V70" fill="#fff" stroke="${INK}" stroke-width="2.4"/><rect x="106" y="244" width="56" height="6" fill="${INK}"/><rect x="120" y="150" width="28" height="94" fill="${SKY}"/>` + Array.from({ length: 9 }, (_, i) => `<line x1="118" y1="${84 + i * 18}" x2="${i % 2 ? 126 : 132}" y2="${84 + i * 18}" stroke="${INK}" stroke-width="1.5"/>`).join('') + lab(134, 'measuring cylinder');
    // beaker
    s += `<path d="M200 150 V240 Q200 250 210 250 H262 Q272 250 272 240 V150 L278 144" fill="#fff" stroke="${INK}" stroke-width="2.4"/><rect x="202" y="196" width="68" height="52" fill="${SKY}"/>` + lab(236, 'beaker');
    // conical flask
    s += `<path d="M320 130 V170 L296 248 H368 L344 170 V130" fill="#fff" stroke="${INK}" stroke-width="2.4"/><path d="M306 216 H358 L366 246 H298Z" fill="#B9E3C6"/>` + lab(332, 'conical flask');
    // Bunsen burner
    s += `<rect x="410" y="150" width="16" height="92" fill="${GREY}" stroke="${INK}" stroke-width="2"/><rect x="392" y="240" width="52" height="10" rx="3" fill="${INK}"/><rect x="426" y="226" width="20" height="6" fill="${GREY}"/>` +
      `<g class="sa a-pulse" style="--o:418px 150px"><path d="M418 86 C432 112 430 138 418 148 C406 138 404 112 418 86Z" fill="#64B5F6" opacity=".85"/><path d="M418 112 C424 126 423 140 418 146 C413 140 412 126 418 112Z" fill="${BLUE}"/></g>` + lab(418, 'Bunsen burner');
    return { svg: W(s), a: {} };
  };

  // choose the right size: 20 cm³ in a 50 cm³ measuring cylinder and in a 500 cm³ beaker
  F.sciChoose = () => {
    let s = T(240, 26, 'Measuring 20 cm³ of water', { size: 16, bold: true });
    s += `<path d="M120 50 V262 H156 V50" fill="#fff" stroke="${INK}" stroke-width="2.4"/><rect x="108" y="262" width="60" height="6" fill="${INK}"/>`;
    for (let v = 0; v <= 50; v += 5) { const y = 258 - v * 4; s += `<line x1="120" y1="${y}" x2="${v % 10 ? 128 : 136}" y2="${y}" stroke="${INK}" stroke-width="1.5"/>` + (v % 10 ? '' : T(166, y + 4, v, { size: 10, anchor: 'start' })); }
    s += `<rect x="122" y="178" width="32" height="80" fill="${SKY}"/><line x1="112" y1="178" x2="164" y2="178" stroke="${RED}" stroke-width="2" class="sa a-blink"/>` + T(138, 292, '50 cm³ cylinder', { size: 12, bold: true }) + ICON.tick(70, 90);
    s += `<path d="M290 120 V250 Q290 262 302 262 H418 Q430 262 430 250 V120 L438 112" fill="#fff" stroke="${INK}" stroke-width="2.4"/>`;
    [100, 200, 300, 400].forEach((v, i) => { const y = 250 - (i + 1) * 30; s += `<line x1="290" y1="${y}" x2="302" y2="${y}" stroke="${INK}" stroke-width="1.5"/>` + T(306, y + 4, v, { size: 10, anchor: 'start' }); });
    s += `<rect x="292" y="254" width="136" height="6" fill="${SKY}"/>` + T(360, 292, '500 cm³ beaker', { size: 12, bold: true }) + ICON.cross(300, 62);
    s += lines(70, 136, 'small steps: easy to read 20', 14, { size: 11, fill: DGREEN }) + lines(390, 58, 'big steps: 20 is hard to see', 18, { size: 11, fill: RED });
    return { svg: W(s), a: {} };
  };

  // electricity: burning fossil fuels or using the Sun and the wind
  F.sciEnergy = () => {
    let s = box(8, 12, 224, 296, '#FFF4F4', '#F3B6B6') + T(120, 40, 'burning fossil fuels', { size: 14, bold: true, fill: RED });
    s += `<rect x="40" y="170" width="140" height="90" fill="#90A4AE" stroke="${INK}" stroke-width="2"/><rect x="140" y="96" width="22" height="74" fill="#78909C" stroke="${INK}" stroke-width="2"/>` + ICON.smoke(150, 82) + ICON.smoke(156, 70) + T(120, 284, 'adds carbon dioxide to the air', { size: 12 });
    s += box(248, 12, 224, 296, '#F0FAF3', '#A5D6A7') + T(360, 40, 'using the Sun and the wind', { size: 14, bold: true, fill: DGREEN });
    s += ICON.sun(300, 82) + ICON.turbine(330, 196) + ICON.turbine(400, 186) + ICON.solar(320, 250) + ICON.solar(392, 250) + T(360, 296, 'much less carbon dioxide', { size: 12 });
    return { svg: W(s), a: {} };
  };
  /* ---------------- Stage 7 Unit 2 Measurements ---------------- */
  const eye = (x, y, c = INK) => `<path d="M${x - 16} ${y} Q${x} ${y - 12} ${x + 16} ${y} Q${x} ${y + 12} ${x - 16} ${y}Z" fill="#fff" stroke="${c}" stroke-width="2"/><circle cx="${x}" cy="${y}" r="5" fill="${c}"/>`;
  // reading a rule: eyes at A (left), B (straight above), C (right); o.cm = true length, o.obj label
  F.sciParallax = (o = {}) => {
    const x0 = 50, k = 17, y = 230, L = o.cm || 20;   // 1 cm = 17 px, scale 0–22
    let s = T(240, 24, o.title || 'Where should your eye be?', { size: 15, bold: true });
    s += `<rect x="${x0}" y="${y - 30}" width="${L * k}" height="22" rx="4" fill="${GOLD}" stroke="${INK}" stroke-width="1.5"/>` + T(x0 + L * k / 2, y - 14, o.obj || 'pencil', { size: 11, bold: true });
    s += `<rect x="${x0 - 14}" y="${y}" width="${22 * k + 18}" height="40" fill="#FFF8E1" stroke="${INK}" stroke-width="1.5"/>`;
    for (let i = 0; i <= 22 * 10; i++) { const x = x0 + i * k / 10, big = i % 10 === 0, mid = i % 5 === 0; s += `<line x1="${x}" y1="${y}" x2="${x}" y2="${y + (big ? 14 : mid ? 9 : 5)}" stroke="${INK}" stroke-width="${big ? 1.4 : 0.7}"/>` + (big && (i / 10) % 2 === 0 ? T(x, y + 30, i / 10, { size: 10 }) : ''); }
    const xe = x0 + L * k;
    [["A", xe - 60, RED], ['B', xe, DGREEN], ['C', xe + 70, RED]].forEach(([l, ex, c]) => { s += eye(ex, 78, c) + T(ex, 58, l, { size: 14, bold: true, fill: c }) + `<line x1="${ex}" y1="90" x2="${xe + (xe - ex) * 0.22}" y2="${y + 4}" stroke="${c}" stroke-width="1.6" stroke-dasharray="5 4"${l === 'B' ? ' class="sa a-flow"' : ''}/>`; });
    s += T(240, 306, o.note || 'Only eye B, straight above the mark, reads the true length', { size: 12, fill: GREY });
    return { svg: W(s), a: {} };
  };
  // close-up of a measuring cylinder: meniscus, eye too high / level / too low; o.v reading at the bottom of the meniscus
  F.sciMeniscus = (o = {}) => {
    const v = o.v || 46, x = 190, w = 90, top = 40, bot = 290, lo = v - 6, sc = (bot - top) / 12, Y = t => bot - (t - lo) * sc;
    let s = `<path d="M${x} ${top - 10} V${bot} M${x + w} ${top - 10} V${bot}" stroke="${INK}" stroke-width="2.6" fill="none"/>`;
    const yl = Y(v); s += `<path d="M${x + 1.5} ${yl - 12} Q${x + w / 2} ${yl + 12} ${x + w - 1.5} ${yl - 12} V${bot} H${x + 1.5}Z" fill="${SKY}"/><path d="M${x + 1.5} ${yl - 12} Q${x + w / 2} ${yl + 12} ${x + w - 1.5} ${yl - 12}" fill="none" stroke="${BLUE}" stroke-width="2.4"/>`;
    for (let t = lo; t <= lo + 12; t++) { const y = Y(t), big = t % 5 === 0; s += `<line x1="${x}" y1="${y}" x2="${x + (big ? 26 : 14)}" y2="${y}" stroke="${INK}" stroke-width="${big ? 1.8 : 1}"/>` + (big ? T(x - 8, y + 4, t, { size: 12, anchor: 'end' }) : ''); }
    s += `<line x1="${x + w / 2 - 30}" y1="${yl}" x2="${x + w + 70}" y2="${yl}" stroke="${DGREEN}" stroke-width="2" stroke-dasharray="5 4" class="sa a-flow"/>` + eye(x + w + 92, yl, DGREEN) + T(x + w + 92, yl + 30, 'eye level', { size: 12, bold: true, fill: DGREEN });
    s += eye(x + w + 92, yl - 70, RED) + T(x + w + 92, yl - 92, 'too high', { size: 12, fill: RED }) + eye(x + w + 92, yl + 74, RED) + T(x + w + 92, yl + 104, 'too low', { size: 12, fill: RED });
    s += lines(78, 120, 'meniscus: read the bottom of the curve', 14, { size: 12, bold: true, fill: BLUE }) + arrow(110, 150, x + w / 2 - 6, yl + 2, BLUE) + T(240, 24, `Reading: ${v} cm³`, { size: 15, bold: true });
    return { svg: W(s), a: {} };
  };
  // a leaf on 1 cm squared paper: full squares dark, more-than-half squares light; o.full/o.half counts shown
  F.sciLeafGrid = (o = {}) => {
    const n = 10, sz = 24, x0 = 40, y0 = 40, cx = 5, cy = 5, rx = 4.4, ry = 3.0;
    const cover = (i, j) => { let c = 0; for (let a = 0; a < 6; a++) for (let b = 0; b < 6; b++) { const px = i + (a + 0.5) / 6 - cx, py = j + (b + 0.5) / 6 - cy, u = (px * 0.8 + py * 0.6), w2 = (-px * 0.6 + py * 0.8); if ((u / rx) ** 2 + (w2 / ry) ** 2 <= 1) c++; } return c / 36; };
    let s = '', full = 0, half = 0;
    for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) { const c = cover(i, j), f = c > 0.97 ? GREEN : c > 0.5 ? '#C5E8B7' : '#fff'; if (c > 0.97) full++; else if (c > 0.5) half++;
      s += `<rect x="${x0 + i * sz}" y="${y0 + j * sz}" width="${sz}" height="${sz}" fill="${f}" stroke="#B0BEC5" stroke-width="0.8"/>`; }
    s += `<ellipse cx="${x0 + cx * sz}" cy="${y0 + cy * sz}" rx="${rx * sz}" ry="${ry * sz}" transform="rotate(${Math.atan2(0.6, 0.8) * 180 / Math.PI} ${x0 + cx * sz} ${y0 + cy * sz})" fill="none" stroke="${DGREEN}" stroke-width="3"/>`;
    s += `<line x1="${x0 + 9.4 * sz}" y1="${y0 + 9.4 * sz}" x2="${x0 + 10.6 * sz}" y2="${y0 + 10.6 * sz}" stroke="${DGREEN}" stroke-width="3"/>`;
    const tx = 320; s += box(tx - 20, 50, 180, 210, SOFT) + `<rect x="${tx}" y="70" width="20" height="20" fill="${GREEN}"/>` + T(tx + 30, 85, `full: ${full}`, { anchor: 'start', bold: true }) + `<rect x="${tx}" y="104" width="20" height="20" fill="#C5E8B7" stroke="#B0BEC5"/>` + T(tx + 30, 119, `over half: ${half}`, { anchor: 'start', bold: true });
    s += `<rect x="${tx}" y="138" width="20" height="20" fill="#fff" stroke="#B0BEC5"/>` + T(tx + 30, 153, 'under half: ignore', { anchor: 'start', size: 12 }) + T(tx + 70, 196, `area ≈ ${full} + ${half}`, { bold: true }) + T(tx + 70, 220, `≈ ${full + half} cm²`, { size: 16, bold: true, fill: BLUE }) + T(tx + 70, 246, 'each square = 1 cm²', { size: 11, fill: GREY });
    return { svg: W(s), a: { full, half } };
  };
  // electronic balance with tare: 1 empty beaker, 2 press tare → 0.0 g, 3 add sand → o.g g
  F.sciTare = (o = {}) => {
    const g = o.g == null ? 36.5 : o.g, beak = o.beaker == null ? 52.4 : o.beaker;
    const bal = (x, read, fill, lab, note) => `<rect x="${x - 62}" y="216" width="124" height="44" rx="8" fill="#ECEFF1" stroke="${INK}" stroke-width="2"/><rect x="${x - 70}" y="206" width="140" height="10" rx="3" fill="${GREY}"/>`
      + `<rect x="${x - 40}" y="226" width="56" height="24" rx="4" fill="${INK}"/>` + T(x - 12, 243, read, { size: 13, bold: true, fill: '#7CFC9A' }) + `<circle cx="${x + 38}" cy="238" r="10" fill="${note ? ORANGE : '#B0BEC5'}" stroke="${INK}" stroke-width="1.5"${note ? ' class="sa a-pulse" style="--o:' + (x + 38) + 'px 238px"' : ''}/>` + T(x + 38, 266, 'tare', { size: 10 })
      + `<path d="M${x - 28} 130 V200 Q${x - 28} 206 ${x - 22} 206 H${x + 22} Q${x + 28} 206 ${x + 28} 200 V130" fill="#fff" stroke="${INK}" stroke-width="2.2"/>` + (fill ? `<path d="M${x - 26} 176 Q${x} 166 ${x + 26} 176 V200 Q${x + 26} 204 ${x + 22} 204 H${x - 22} Q${x - 26} 204 ${x - 26} 200Z" fill="#E0C48A"/>` : '')
      + lines(x, 290, lab, 18, { size: 12, bold: true });
    let s = T(240, 30, 'Using the tare button', { size: 16, bold: true }) + bal(80, beak.toFixed(1) + ' g', false, '1 empty beaker') + bal(240, '0.0 g', false, '2 press tare', true) + bal(400, g.toFixed(1) + ' g', true, '3 add the sand: only its mass');
    s += arrow(150, 160, 170, 160, GREY) + arrow(310, 160, 330, 160, GREY);
    return { svg: W(s), a: {} };
  };

  // label any other figure: o.base = figure kind, o.bo = its options, o.s = scale (the picture shrinks to make room),
  // o.labels = [[x, y, text, side]] with x, y in the base picture's own coordinates; side 'l' or 'r' (default: nearest edge)
  F.sciLabel = (o = {}) => {
    const g = AF.get(o.base, o.bo || {}).svg || '', i = g.indexOf('>', g.indexOf('<svg')) + 1, inner = g.slice(i, g.lastIndexOf('</svg>'));
    const s = o.s || 0.6, dx = 240 - 240 * s, dy = (o.title ? 172 : 160) - 160 * s, P = (x, y) => [dx + x * s, dy + y * s];
    let out = (o.title ? T(240, 22, o.title, { size: 15, bold: true }) : '') + `<g transform="translate(${dx} ${dy}) scale(${s})">${inner}</g>`;
    const L = (o.labels || []).map(([x, y, t, side]) => { const [px, py] = P(x, y); return { px, py, t, left: side ? side === 'l' : px < 240, ty: py }; });
    [true, false].forEach(sd => { const g2 = L.filter(l => l.left === sd).sort((a, b) => a.py - b.py);   // spread the text so labels never overlap
      g2.forEach((l, k) => { const gap = 14 + 15 * (k ? wrap(g2[k - 1].t, 12).length : 0); if (k && l.ty < g2[k - 1].ty + gap) l.ty = g2[k - 1].ty + gap; }); const over = g2.length ? g2[g2.length - 1].ty - 300 : 0;
      if (over > 0) g2.forEach(l => { l.ty -= over; }); });
    L.forEach(l => { const tx = l.left ? dx - 6 : 480 - dx + 6, ex = l.left ? tx + 4 : tx - 4;
      out += `<path d="M${l.px} ${l.py} L${ex} ${l.ty}" fill="none" stroke="${INK}" stroke-width="1.2"/><circle cx="${l.px}" cy="${l.py}" r="2.5" fill="${INK}"/>`
        + lines(l.left ? tx - 2 : tx + 2, l.ty + 4, l.t, 12, { size: 12, bold: true, anchor: l.left ? 'end' : 'start' }); });
    return { svg: W(out), a: {} };
  };

  /* ---------------- Stage 7 Unit 6 Materials and their structure ---------------- */
  // states of matter and the changes between them: solid, liquid, gas boxes with labelled arrows
  F.sciStates = (o = {}) => {
    const P = (cx, cy, st) => { let s = `<rect x="${cx - 52}" y="${cy - 44}" width="104" height="88" rx="8" fill="#fff" stroke="${INK}" stroke-width="2"/>`, k = 0;
      const dot = (x, y, c) => `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="6" fill="${c || BLUE}" stroke="${INK}" stroke-width="0.8"/>`, r = q => ((Math.sin(q * 12.9898) * 43758.5453) % 1 + 1) % 1;
      if (st === 'solid') for (let a = 0; a < 6; a++) for (let b = 0; b < 5; b++) s += `<g class="sa a-swing" style="--o:${cx - 40 + a * 16}px ${cy - 32 + b * 16}px">${dot(cx - 40 + a * 16, cy - 32 + b * 16)}</g>`;
      else if (st === 'liquid') for (k = 0; k < 18; k++) s += dot(cx - 42 + r(k) * 84, cy + 36 - (k % 4) * 13 - r(k + 40) * 4);
      else for (k = 0; k < 6; k++) s += `<g class="sa a-rise" style="--dx:${(r(k + 3) - 0.5) * 20}px;--dy:${(r(k + 7) - 0.5) * 20}px;--t:${2 + k * 0.3}s">${dot(cx - 40 + r(k) * 80, cy - 34 + r(k + 9) * 68)}</g>`;
      return s + T(cx, cy + 64, st, { size: 14, bold: true }); };
    let s = P(80, 210, 'solid') + P(400, 210, 'liquid') + P(240, 72, 'gas');
    const A = (x1, y1, x2, y2, t, tx, ty, c) => arrow(x1, y1, x2, y2, c) + T(tx, ty, t, { size: 12, bold: true, fill: c });
    s += A(140, 196, 338, 196, 'melting', 240, 186, RED) + A(338, 228, 140, 228, 'freezing', 240, 246, BLUE);
    s += A(384, 160, 300, 98, 'evaporating / boiling', 404, 118, RED) + arrow(282, 114, 366, 172, BLUE) + T(300, 158, 'condensing', { size: 12, bold: true, fill: BLUE, anchor: 'end' });
    s += T(240, 306, o.note || 'heating: red arrows · cooling: blue arrows', { size: 11, fill: GREY });
    return { svg: W(s), a: {} };
  };
  // particle diagrams: o.boxes = [{t: label, kind: 'atoms'|'mol'|'compound'|'mixture'|'mixel', a: colour, b: colour}]
  F.sciMatter = (o = {}) => {
    const bx = o.boxes || [{ t: 'element (atoms)', kind: 'atoms' }, { t: 'element (molecules)', kind: 'mol' }, { t: 'compound', kind: 'compound' }, { t: 'mixture', kind: 'mixture' }];
    const n = bx.length, gap = 472 / n, bw = Math.min(150, gap - 12), R = 9;
    const at = (x, y, c, rr) => `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${rr || R}" fill="${c}" stroke="${INK}" stroke-width="1"/>`, rn = q => ((Math.sin(q * 78.233) * 43758.5453) % 1 + 1) % 1;
    let s = '';
    bx.forEach((b, i) => { const x0 = 4 + gap * i + (gap - bw) / 2, y0 = 60, h = 180, ca = b.a || BLUE, cb = b.b || RED, cc = b.c || GOLD;
      s += `<rect x="${x0}" y="${y0}" width="${bw}" height="${h}" rx="8" fill="#fff" stroke="${INK}" stroke-width="2"/>`;
      const spots = []; for (let r = 0; r < 3; r++) for (let c = 0; c < 2; c++) spots.push([x0 + bw * (0.27 + c * 0.46) + (rn(i * 9 + r * 2 + c) - 0.5) * 14, y0 + 34 + r * 56 + (rn(i * 5 + r + c * 7) - 0.5) * 12]);
      spots.forEach(([x, y], k) => {
        if (b.kind === 'atoms') s += at(x, y, ca);
        else if (b.kind === 'mol') s += at(x - 8, y, ca) + at(x + 8, y, ca);
        else if (b.kind === 'compound') s += at(x - 9, y, cb) + at(x + 7, y - 7, ca, 7) + at(x + 7, y + 7, ca, 7);
        else if (b.kind === 'compound1') s += at(x - 8, y, cb) + at(x + 8, y, ca);
        else if (b.kind === 'mixel') s += k % 2 ? at(x, y, ca) : at(x, y, cc);
        else s += k % 3 === 0 ? at(x - 8, y, ca) + at(x + 8, y, ca) : k % 3 === 1 ? at(x - 9, y, cb) + at(x + 7, y - 7, ca, 7) + at(x + 7, y + 7, ca, 7) : at(x, y, cc); });
      s += lines(x0 + bw / 2, y0 + h + 24, b.t, 18, { size: 13, bold: true }); if (b.d) s += lines(x0 + bw / 2, y0 + h + 42, b.d, 22, { size: 11, fill: GREY }); });
    if (o.title) s += T(240, 34, o.title, { size: 15, bold: true });
    return { svg: W(s), a: {} };
  };
  // a simplified Periodic Table: metals / non-metals, o.mark = [symbol] highlighted, o.group / o.period highlighted
  const PT = ['H,,,,,,,,,,,,,,,,,He', 'Li,Be,,,,,,,,,,,B,C,N,O,F,Ne', 'Na,Mg,,,,,,,,,,,Al,Si,P,S,Cl,Ar', 'K,Ca,Sc,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zn,Ga,Ge,As,Se,Br,Kr', 'Rb,Sr,Y,Zr,Nb,Mo,Tc,Ru,Rh,Pd,Ag,Cd,In,Sn,Sb,Te,I,Xe'].map(r => r.split(','));
  const NONMETAL = 'H,He,B,C,N,O,F,Ne,Si,P,S,Cl,Ar,Ge,As,Se,Br,Kr,Sb,Te,I,Xe'.split(',');
  F.sciPeriodic = (o = {}) => {
    const cw = 25.5, ch = 38, x0 = 11, y0 = 52, mark = o.mark || [];
    let s = T(240, 26, o.title || 'The Periodic Table (first five periods)', { size: 15, bold: true });
    PT.forEach((row, p) => row.forEach((e, g) => { if (!e) return; const x = x0 + g * cw, y = y0 + p * ch, nm = NONMETAL.includes(e), hi = mark.includes(e) || o.group === g + 1 || o.period === p + 1;
      s += `<rect x="${x}" y="${y}" width="${cw - 2}" height="${ch - 3}" rx="3" fill="${hi ? GOLD : nm ? '#E3F2E1' : '#DCE8FB'}" stroke="${hi ? ORANGE : '#9FB3CC'}" stroke-width="${hi ? 2 : 1}"/>` + T(x + cw / 2 - 1, y + ch / 2 + 3, e, { size: 11, bold: true }); }));
    for (let g = 1; g <= 18; g++) s += T(x0 + (g - 0.5) * cw - 1, y0 - 6, g, { size: 8, fill: GREY });
    for (let p = 1; p <= 5; p++) s += T(x0 - 4, y0 + (p - 0.5) * ch + 3, p, { size: 8, fill: GREY, anchor: 'end' });
    s += `<rect x="60" y="${y0 + 5 * ch + 14}" width="16" height="12" fill="#DCE8FB" stroke="#9FB3CC"/>` + T(82, y0 + 5 * ch + 24, 'metals', { size: 12, anchor: 'start' })
      + `<rect x="170" y="${y0 + 5 * ch + 14}" width="16" height="12" fill="#E3F2E1" stroke="#9FB3CC"/>` + T(192, y0 + 5 * ch + 24, 'non-metals', { size: 12, anchor: 'start' })
      + T(300, y0 + 5 * ch + 24, 'columns = groups · rows = periods', { size: 11, fill: GREY, anchor: 'start' });
    return { svg: W(s), a: {} };
  };

  /* ---------------- Stage 7 Unit 7 Properties of materials ---------------- */
  // three test tubes with iron nails: A air + water, B dry air (drying agent), C boiled water under oil; o.after shows rust in A
  F.sciRust = (o = {}) => {
    const tube = (x, lab, water, oil, dry, rust, note) => {
      let s = `<path d="M${x - 26} 50 V236 A26 26 0 0 0 ${x + 26} 236 V50" fill="#fff" stroke="${INK}" stroke-width="2.4"/>`;
      if (water) s += `<path d="M${x - 24} ${oil ? 150 : 170} V236 A24 24 0 0 0 ${x + 24} 236 V${oil ? 150 : 170}Z" fill="${SKY}"/>`;
      if (oil) s += `<rect x="${x - 24}" y="134" width="48" height="16" fill="#F6D365"/>` + T(x + 40, 146, 'oil', { size: 11, anchor: 'start' });
      if (dry) s += [0, 1, 2, 3, 4, 5].map(i => `<circle cx="${x - 14 + (i % 3) * 14}" cy="${250 - Math.floor(i / 3) * 12}" r="6" fill="#ECEFF1" stroke="${GREY}"/>`).join('') + T(x + 40, 254, 'drying agent', { size: 10, anchor: 'start' });
      s += `<rect x="${x - 3}" y="${dry ? 80 : 90}" width="6" height="${dry ? 140 : 150}" fill="${rust ? '#B5541C' : '#90A4AE'}" stroke="${INK}" stroke-width="1"/><rect x="${x - 9}" y="${dry ? 76 : 86}" width="18" height="6" fill="${rust ? '#B5541C' : '#90A4AE'}"/>`;
      if (rust) s += [0, 1, 2, 3, 4].map(i => `<circle cx="${x + (i % 2 ? 5 : -5)}" cy="${110 + i * 24}" r="4" fill="#8D3A12" class="sa a-blink" style="animation-delay:${i * 0.4}s"/>`).join('');
      return s + `<rect x="${x - 30}" y="40" width="60" height="12" rx="3" fill="#A1887F"/>` + T(x, 30, lab, { size: 15, bold: true }) + lines(x, 286, note, 16, { size: 11.5, bold: true, fill: rust ? RED : INK });
    };
    const A = o.after !== false;
    return { svg: W(tube(80, 'A', true, false, false, A, 'air + water') + tube(240, 'B', false, false, true, false, 'dry air, no water') + tube(400, 'C', true, true, false, false, 'water, no air (boiled, oil on top)')), a: {} };
  };
  // atoms in layers: pure metal (layers slide) and an alloy (bigger atoms stop the sliding)
  F.sciAlloy = () => {
    const at = (x, y, r, c) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${c}" stroke="${INK}" stroke-width="1"/>`;
    let s = T(120, 28, 'pure metal', { size: 15, bold: true }) + T(360, 28, 'alloy', { size: 15, bold: true });
    for (let r = 0; r < 5; r++) { const shift = r < 2 ? '' : ' class="sa a-swing" style="--o:120px 400px"'; let row = ''; for (let c = 0; c < 7; c++) row += at(36 + c * 28, 80 + r * 28, 13, '#B0BEC5'); s += r === 2 ? `<g class="sa a-rise" style="--dx:14px;--dy:0px;--t:2.4s">${row}</g>` : `<g>${row}</g>`; }
    for (let r = 0; r < 5; r++) for (let c = 0; c < 7; c++) { const big = (r * 7 + c) % 5 === 2; s += at(276 + c * 28 + (big ? 2 : 0), 80 + r * 28 + (big ? -3 : 0), big ? 17 : 13, big ? GOLD : '#B0BEC5'); }
    s += arrow(30, 230, 210, 230, RED) + lines(120, 252, 'layers slide easily: soft, malleable', 26, { size: 12 }) + lines(360, 252, 'different-sized atoms stop the layers sliding: harder, stronger', 28, { size: 12 });
    return { svg: W(s), a: {} };
  };

  /* ---------------- Stage 7 Unit 10 Forces ---------------- */
  // force diagram: an object (o.obj label, o.shape 'box'|'ball'|'person') with arrows o.forces = [{dir:'up'|'down'|'left'|'right', t:'weight 20 N', n: relative size 1–5}]
  F.sciForce = (o = {}) => {
    const cx = 240, cy = o.title ? 172 : 160, w = 110, h = 70, C = { up: BLUE, down: RED, left: ORANGE, right: DGREEN };
    let s = o.title ? T(240, 24, o.title, { size: 15, bold: true }) : '';
    if (o.ground) s += `<rect x="20" y="${cy + h / 2}" width="440" height="10" fill="#C8B79A"/>`;
    s += o.shape === 'ball' ? `<circle cx="${cx}" cy="${cy}" r="${h / 2}" fill="${SKY}" stroke="${INK}" stroke-width="2"/>` : `<rect x="${cx - w / 2}" y="${cy - h / 2}" width="${w}" height="${h}" rx="8" fill="${SKY}" stroke="${INK}" stroke-width="2"/>`;
    s += lines(cx, cy + 4, o.obj || '', 14, { size: 13, bold: true });
    (o.forces || []).forEach(f => { const L = (f.dir === 'left' || f.dir === 'right' ? 10 : 24) + (f.n || 2) * 16, c = f.c || C[f.dir] || INK;
      if (f.dir === 'up') s += arrow(cx, cy - h / 2, cx, cy - h / 2 - L, c) + T(cx + 10, cy - h / 2 - L + 4, f.t, { size: 12.5, bold: true, fill: c, anchor: 'start' });
      if (f.dir === 'down') s += arrow(cx, cy + h / 2, cx, cy + h / 2 + L, c) + T(cx + 10, cy + h / 2 + L - 2, f.t, { size: 12.5, bold: true, fill: c, anchor: 'start' });
      if (f.dir === 'left') s += arrow(cx - (o.shape === 'ball' ? h / 2 : w / 2), cy, cx - w / 2 - L, cy, c) + lines(cx - w / 2 - L - 6, cy + 4, f.t, 12, { size: 12.5, bold: true, fill: c, anchor: 'end' });
      if (f.dir === 'right') s += arrow(cx + (o.shape === 'ball' ? h / 2 : w / 2), cy, cx + w / 2 + L, cy, c) + lines(cx + w / 2 + L + 6, cy + 4, f.t, 12, { size: 12.5, bold: true, fill: c, anchor: 'start' }); });
    if (o.note) s += T(240, 308, o.note, { size: 11, fill: GREY });
    return { svg: W(s), a: {} };
  };

  /* ---------------- Stage 7 Unit 11 Energy and sound ---------------- */
  // a sound wave: a vibrating loudspeaker and air particles bunched into compressions; o.medium label
  F.sciSound = (o = {}) => {
    let s = T(240, 26, o.title || 'Sound: vibrations passed from particle to particle', { size: 14, bold: true });
    s += `<g class="sa a-rise" style="--dx:6px;--dy:0px;--t:0.5s"><rect x="40" y="100" width="18" height="120" fill="${INK}"/><path d="M58 120 L84 92 V228 L58 200Z" fill="${GREY}" stroke="${INK}" stroke-width="2"/></g>`;
    for (let c = 0; c < 26; c++) { const x0 = 104 + c * 13.5, dx = 9 * Math.sin(c * 0.55); for (let r = 0; r < 8; r++) s += `<circle cx="${(x0 + dx).toFixed(1)}" cy="${104 + r * 16 + (c % 2) * 6}" r="3.6" fill="${BLUE}"/>`; }
    [0, 1].forEach(m => { const c = Math.PI * (2 * m + 1) / 0.55 - 0.5, x = 104 + c * 13.5; s += T(x, 258, 'compression', { size: 10.5, fill: GREY }) + T(x + 85, 258, 'rarefaction', { size: 10.5, fill: GREY }); });
    s += arrow(110, 286, 440, 286, DGREEN, true) + T(275, 306, o.medium || 'energy travels through the air to your ear', { size: 12, bold: true, fill: DGREEN });
    return { svg: W(s), a: {} };
  };

  /* ---------------- Stage 7 Unit 13 Earth ---------------- */
  // the layers of the Earth: a cut-away globe with labels
  F.sciEarth = () => {
    const cx = 170, cy = 165, R = [140, 120, 66, 30], col = ['#8D6E63', '#F4A259', '#E9573F', '#FDD835'], nm = ['crust (solid rock)', 'mantle (hot rock; upper part semi-molten)', 'outer core (liquid iron and nickel)', 'inner core (solid, hottest)'];
    let s = `<circle cx="${cx}" cy="${cy}" r="${R[0] + 4}" fill="#3A7BD5"/>` + R.map((r, i) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${col[i]}"/>`).join('');
    s += `<path d="M${cx} ${cy} L${cx + R[0] + 6} ${cy} A${R[0] + 6} ${R[0] + 6} 0 0 0 ${cx} ${cy - R[0] - 6}Z" fill="#fff" opacity="0"/>`;
    const ys = [42, 104, 186, 250], px = [cx + 100, cx + 96, cx + 42, cx + 10], py = [cy - 102, cy - 50, cy + 30, cy + 8];
    nm.forEach((t, i) => { s += `<path d="M${px[i]} ${py[i]} L330 ${ys[i]}" stroke="${INK}" stroke-width="1.2" fill="none"/><circle cx="${px[i]}" cy="${py[i]}" r="2.5" fill="${INK}"/>` + lines(334, ys[i] + 4, t, 20, { size: 12, bold: i === 3, anchor: 'start' }); });
    return { svg: W(s), a: {} };
  };

  /* ---------------- Stage 7 Unit 14 Earth and beyond ---------------- */
  // eclipses (not to scale): o.type 'solar' (Moon between Sun and Earth) or 'lunar' (Earth between Sun and Moon)
  F.sciEclipse = (o = {}) => {
    const solar = (o.type || 'solar') === 'solar', sy = 160;
    let s = T(240, 26, solar ? 'Solar eclipse: the Moon blocks the Sun' : 'Lunar eclipse: the Moon is in the Earth’s shadow', { size: 15, bold: true });
    s += `<circle cx="40" cy="${sy}" r="70" fill="${GOLD}"/>` + T(40, sy + 4, 'Sun', { size: 13, bold: true });
    const sm = solar ? [250, 28] : [260, 34], bg = solar ? [410, 40] : [420, 12];   // [x, r] of the small body in the middle and the body behind
    const [mx, mr] = sm, [ex, er] = bg;
    const X = 480, R0 = 70, k1 = (R0 - mr) / (mx - 40), k2 = (R0 + mr) / (mx - 40), tip = 40 + R0 / k1;
    s += `<path d="M${mx} ${sy - mr} L${X} ${sy - R0 + (X - 40) * k2} L${X} ${sy + R0 - (X - 40) * k2} L${mx} ${sy + mr}Z" fill="#90A4AE" opacity=".35"/>`;   // penumbra: partial shadow
    s += tip < X ? `<path d="M${mx} ${sy - mr} L${tip} ${sy} L${mx} ${sy + mr}Z" fill="#37474F" opacity=".8"/>` : `<path d="M${mx} ${sy - mr} L${X} ${sy - R0 + (X - 40) * k1} L${X} ${sy + R0 - (X - 40) * k1} L${mx} ${sy + mr}Z" fill="#37474F" opacity=".8"/>`;   // umbra
    s += `<circle cx="${mx}" cy="${sy}" r="${mr}" fill="${solar ? '#B0BEC5' : '#3A7BD5'}" stroke="${INK}"/>` + T(mx, sy - mr - 10, solar ? 'Moon' : 'Earth', { size: 13, bold: true });
    s += `<circle cx="${ex}" cy="${sy}" r="${er}" fill="${solar ? '#3A7BD5' : '#B5541C'}" stroke="${INK}"/>` + T(ex, sy - er - 10, solar ? 'Earth' : 'Moon (looks red)', { size: 13, bold: true });
    s += T(ex - 20, sy + (solar ? 70 : 60), 'umbra: total', { size: 11.5, fill: INK, anchor: 'end' }) + T(ex - 20, sy + (solar ? 88 : 78), 'penumbra: partial', { size: 11.5, fill: GREY, anchor: 'end' });
    return { svg: W(s + T(240, 308, 'not to scale', { size: 11, fill: GREY })), a: {} };
  };
  // tides: the Earth with two water bulges and the Moon; o.sun: 'line' (spring tides) or 'right' (neap tides)
  F.sciTides = (o = {}) => {
    const cx = 220, cy = 165, sun = o.sun;
    let s = T(240, 26, sun === 'line' ? 'Spring tides: Sun and Moon in line' : sun === 'right' ? 'Neap tides: Sun and Moon at right angles' : 'The Moon pulls the oceans into two bulges', { size: 14, bold: true });
    s += `<ellipse cx="${cx}" cy="${cy}" rx="${sun === 'right' ? 78 : 92}" ry="${sun === 'right' ? 70 : 62}" fill="#90CAF9" opacity=".85"/><circle cx="${cx}" cy="${cy}" r="56" fill="#66BB6A" stroke="${DGREEN}"/>` + T(cx, cy + 4, 'Earth', { size: 13, bold: true, fill: '#fff' });
    s += `<circle cx="420" cy="${cy}" r="18" fill="#B0BEC5" stroke="${INK}"/>` + T(420, cy + 36, 'Moon', { size: 12, bold: true }) + arrow(392, cy, 320, cy, BLUE) + T(356, cy - 10, 'gravity', { size: 11, fill: BLUE });
    if (sun === 'line') s += ICON.sun(40, cy) + T(40, cy + 44, 'Sun', { size: 12, bold: true });
    if (sun === 'right') s += ICON.sun(cx, 270) + T(cx + 40, 276, 'Sun', { size: 12, bold: true, anchor: 'start' });
    s += T(cx + 120, cy + 70, 'high tide', { size: 11, fill: BLUE }) + T(cx - 118, cy + 70, 'high tide', { size: 11, fill: BLUE });
    return { svg: W(s), a: {} };
  };

})();
