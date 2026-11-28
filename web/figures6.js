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
})();
