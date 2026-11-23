// Builds web/icons.js: the Tabler Icons (MIT, https://tabler.io/icons) that the site uses, with the glyph
// table that turns the old emoji / text symbols into icons.
//   node tools/build-icons.mjs [path/to/tabler-icons/icons]
// Without a path it reuses the icon data already in web/icons.js (so a fresh clone builds offline).
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';

const ROOT = path.dirname(path.dirname(new URL(import.meta.url).pathname));
const OUT = path.join(ROOT, 'web/icons.js');

// Glyphs replaced wherever they appear in interface text. Picture emoji in questions and word cards stay pictures.
// name* = use the filled variant always. [name, colour] = fixed colour.
export const GLYPHS = {
  '→': 'arrow-right', '←': 'arrow-left', '↑': 'arrow-up', '↓': 'arrow-down', '⬇': 'download', '↗': 'arrow-up-right',
  '⇄': 'arrows-exchange', '↺': 'rotate', '🔁': 'repeat', '▲': 'chevron-up', '▼': 'chevron-down', '▾': 'chevron-down',
  '◀': 'arrow-left', '▶': 'player-play', '⏸': 'player-pause',
  '✓': 'check', '✅': 'circle-check', '✗': 'x', '✕': 'x',
  '★': 'star*', '☆': 'star', '⭐': 'star*', '🌟': 'star*', '✦': 'sparkles', '✨': 'sparkles',
  '🔒': 'lock', '🔔': 'bell', '🔍': 'search', '☰': 'menu-2',
  '🎧': 'headphones', '🎤': 'microphone', '🔊': 'volume', '📖': 'book', '👀': 'eye', '📒': 'notebook', '📝': 'notes',
  '🧪': 'flask', '🖨': 'printer', '📄': 'file-text', '🎓': 'school', '🏆': 'trophy', '🏁': 'flag-3', '🏛': 'building-bank',
  '🗂': 'folders', '📘': 'book-2', '📚': 'books', '🧠': 'brain', '✏️': 'pencil', '✎': 'pencil', '💡': 'bulb', '🎉': 'confetti',
  '🔤': 'abc', '🤔': 'help-circle', '⚠️': 'alert-triangle', '⚠': 'alert-triangle', '🔑': 'key', '🗑️': 'trash', '🗑': 'trash',
  '🎯': 'target-arrow', '⚑': 'flag', '🧭': 'compass', '🧩': 'puzzle', '👑': 'crown', '🙂': 'mood-smile', '🙈': 'eye-off',
  '🚫': 'ban', '💬': 'message-circle', '🏠': 'home', '🐞': 'bug', '🔥': 'flame', '🎵': 'music', '🎮': 'device-gamepad-2',
  '📧': 'mail', '📐': 'ruler-2', '🔬': 'microscope', '◎': 'topology-star-3', '☀️': 'sun', '🌙': 'moon', '👉': 'hand-finger-right',
  '💪': 'barbell', '○': 'circle', '◯': 'circle', '☐': 'square', '▣': 'square-dot', '📊': 'chart-bar', '📈': 'chart-line',
  '🎲': 'dice', '👤': 'user', '💓': 'heartbeat', '🐢': 'snail',
  '🟢': ['circle*', '#287C34'], '🟡': ['circle*', '#E0A800'], '🔴': ['circle*', '#DD0035'], '⚫': ['circle*', '#222222'],
};

// Unit (topic) icons by stage. Stage 19 = Maths.
export const UNITS = {
  3: ['seedling', 'bowl-spoon', 'sun', 'heart', 'magnet', 'moon-stars'],
  4: ['paw', 'bolt', 'cube', 'world', 'bulb', 'plug-connected'],
  5: ['flower', 'ear', 'droplet-half', 'apple', 'magnet', 'sun-wind'],
  6: ['body-scan', 'test-pipe', 'mountain', 'fish', 'circuit-bulb', 'planet'],
  7: ['microscope', 'ruler-measure', 'cell', 'hierarchy-2', 'fish', 'atom-2', 'cube', 'test-pipe', 'flask', 'arrows-move', 'bolt', 'plug-connected', 'volcano', 'planet'],
  8: ['apple', 'lungs', 'trees', 'atom', 'droplet-half', 'flame', 'temperature', 'gauge', 'wind', 'prism-light', 'magnet', 'solar-panel', 'cloud-rain', 'planet'],
  9: ['plant-2', 'droplet', 'dna-2', 'atom-2', 'grain', 'replace', 'salt', 'stopwatch', 'weight', 'temperature-plus', 'wave-sine', 'circuit-battery', 'temperature-sun', 'telescope'],
  19: ['calculator', 'math-function', 'percentage', 'equal', 'angle', 'chart-bar', 'ruler-2', 'divide', 'list-numbers', 'chart-line', 'scale', 'dice', 'arrows-move', 'box', 'presentation-analytics'],
};

// Icons used directly by name in the code (besides the two tables above).
const EXTRA = ['player-play', 'player-pause', 'check', 'file-text', 'lock', 'flag', 'bulb', 'maximize', 'flame', 'star', 'clock',
  'trophy', 'search', 'x', 'sun', 'moon', 'chevron-right', 'circle-check', 'help-circle', 'arrow-right'];

const names = new Set(EXTRA);
for (const v of Object.values(GLYPHS)) names.add(String(Array.isArray(v) ? v[0] : v).replace('*', ''));
for (const l of Object.values(UNITS)) l.forEach(n => names.add(n));

const inner = file => fs.readFileSync(file, 'utf8').replace(/<!--[\s\S]*?-->/g, '').replace(/^[\s\S]*?<svg[^>]*>/, '').replace(/<\/svg>[\s\S]*$/, '')
  .replace(/\s*<path d="M0 0h24v24H0z" fill="none"\s*\/>/g, '').replace(/\s+/g, ' ').replace(/> </g, '><').trim();

let O = {}, F = {};
const src = process.argv[2];
if (src) {
  for (const n of [...names].sort()) {
    const o = path.join(src, 'outline', n + '.svg'), f = path.join(src, 'filled', n + '.svg');
    if (fs.existsSync(o)) O[n] = inner(o);
    if (fs.existsSync(f)) F[n] = inner(f);
    if (!O[n] && !F[n]) throw new Error('Tabler has no icon called ' + n);
  }
} else {
  const ctx = { window: {} }; vm.runInNewContext(fs.readFileSync(OUT, 'utf8'), ctx);
  O = ctx.window.AtomicIcons.O; F = ctx.window.AtomicIcons.F;
  const miss = [...names].filter(n => !O[n] && !F[n]); if (miss.length) throw new Error('Missing icons (pass the Tabler icons folder): ' + miss.join(', '));
}

const RE_SRC = '(' + Object.keys(GLYPHS).sort((a, b) => b.length - a.length).map(k => k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')\uFE0F?';
const js = `/* Atomic Education — interface icons. Generated by tools/build-icons.mjs; do not edit by hand.
   Icons: Tabler Icons (https://tabler.io/icons), MIT License, Copyright (c) 2020-2025 Paweł Kuna. */
(function () {
  const O = ${JSON.stringify(O)};
  const F = ${JSON.stringify(F)};
  const GLYPHS = ${JSON.stringify(GLYPHS)};
  const UNITS = ${JSON.stringify(UNITS)};
  const NS = 'http://www.w3.org/2000/svg';
  const RE = new RegExp(${JSON.stringify(RE_SRC)}, 'gu');
  // ic('flask') · ic('star', {filled:true, size:20, color:'#287C34', label:'Starred'})
  function ic(name, o) {
    o = o || {}; const fill = (o.filled && F[name]) || !O[name];
    const s = document.createElementNS(NS, 'svg');
    s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('class', 'ti-i' + (fill ? ' ti-f' : '') + (o.cls ? ' ' + o.cls : ''));
    if (o.size) { s.setAttribute('width', o.size); s.setAttribute('height', o.size); }
    if (fill) s.setAttribute('fill', 'currentColor');
    else { s.setAttribute('fill', 'none'); s.setAttribute('stroke', 'currentColor'); s.setAttribute('stroke-width', o.weight || 2); s.setAttribute('stroke-linecap', 'round'); s.setAttribute('stroke-linejoin', 'round'); }
    if (o.color) s.style.color = o.color;
    if (o.label) { s.setAttribute('role', 'img'); s.setAttribute('aria-label', o.label); } else s.setAttribute('aria-hidden', 'true');
    s.innerHTML = fill ? F[name] : O[name];
    return s;
  }
  // the same icon as an HTML string (for places that build markup)
  function html(name, o) { const d = document.createElement('div'); d.append(ic(name, o)); return d.innerHTML; }
  const has = s => typeof s === 'string' && (RE.lastIndex = 0, RE.test(s));
  // A text with interface glyphs → [text, svg, text…]. filled: the element is the active / current one.
  function swap(s, filled) {
    if (!has(s)) return [s];
    const out = []; let last = 0; RE.lastIndex = 0; let m;
    while ((m = RE.exec(s))) {
      if (m.index > last) out.push(s.slice(last, m.index));
      let g = GLYPHS[m[1]], color = null; if (Array.isArray(g)) { color = g[1]; g = g[0]; }
      let name = g.replace('*', ''); const f = g.endsWith('*') || filled;
      // "Next ▶" (a triangle after the words) means "go on", not "play"
      if (m[1] === '▶' && m.index > 0 && !s.slice(m.index + m[0].length).trim()) name = 'arrow-right';
      out.push(ic(name, { filled: f, color }));
      last = m.index + m[0].length;
    }
    if (last < s.length) out.push(s.slice(last));
    // "✓ Done" → icon + "Done": keep one space between, none at the edges of a lone icon
    return out.filter(x => x !== '');
  }
  function unit(stage, n) { const l = UNITS[stage] || UNITS[stage >= 10 ? 19 : 7]; return l && l[n - 1] || null; }
  window.AtomicIcons = { O, F, GLYPHS, UNITS, ic, html, swap, has, unit };
})();
`;
fs.writeFileSync(OUT, js);
console.log(`web/icons.js: ${Object.keys(O).length} outline + ${Object.keys(F).length} filled icons, ${Object.keys(GLYPHS).length} glyphs`);
