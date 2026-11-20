/* Atomic paper security: personal watermark, microprint, guilloche seal, copy codes.
   Used by the print-only worksheet view (and later by printed papers). */
window.Paper = (function () {
  'use strict';
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  function fnv(s) { let h = 2166136261; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
  const B32 = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';
  function code(s) { const a = fnv(s), b = fnv(s + '#'); let o = ''; for (let i = 0; i < 8; i++) { const v = i < 4 ? a : b; o += B32[(v >>> (i % 4 * 7)) % B32.length]; } return 'AE-' + o.slice(0, 4) + '-' + o.slice(4); }
  const pad = n => (n < 10 ? '0' : '') + n;
  const stamp = d => `${pad(d.getDate())}/${pad(d.getMonth() + 1)}/${d.getFullYear()} ${pad(d.getHours())}:${pad(d.getMinutes())}`;

  function micro(cls) { return `<div class="pmicro ${cls}" aria-hidden="true">${'ATOMICEDUCATION·VERIFIED·'.repeat(70)}</div>`; }
  function frame() { return micro('t') + micro('b') + micro('l') + micro('r'); }

  let wmN = 0;
  function watermark(info) {
    const id = 'pwm' + (++wmN), line = esc(`${info.name}  ·  ${info.lid}  ·  ${info.when}  ·  Copy #${info.serial}`);
    return `<div class="pwm" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 210 297" preserveAspectRatio="none"><defs>
      <pattern id="${id}" width="105" height="44" patternUnits="userSpaceOnUse" patternTransform="rotate(-32)">
      <text x="0" y="12" font-family="Figtree,Arial" font-size="3.4" font-weight="700" fill="#0149AF" fill-opacity=".11">${line}</text>
      <text x="52" y="34" font-family="Figtree,Arial" font-size="3.4" font-weight="700" fill="#0149AF" fill-opacity=".11">${line}</text></pattern></defs>
      <rect width="210" height="297" fill="url(#${id})"/>
      <text x="105" y="160" text-anchor="middle" transform="rotate(-38 105 150)" font-family="Outfit,Arial" font-weight="800" font-size="15" fill="#0E1B3D" fill-opacity=".05" letter-spacing="2">ATOMIC EDUCATION</text></svg></div>`;
  }
  function seal(c) {
    const h = fnv(c), cols = ['#0149AF', '#0E1B3D', '#B9842B', '#0149AF']; let paths = '';
    for (let k = 0; k < 4; k++) {
      const n = 14 + ((h >>> (k * 6)) % 13), a = 30 + k * 4, b = 4 + ((h >>> (k * 4 + 2)) % 5), ph = (h >>> (k * 3)) % 7, pts = [];
      for (let t = 0; t <= Math.PI * 2 + .01; t += 0.01) { const r = a + b * Math.cos(n * t + ph) + 1.5 * Math.sin((n * 2 + 1) * t); pts.push((50 + r * Math.cos(t)).toFixed(2) + ',' + (50 + r * Math.sin(t)).toFixed(2)); }
      paths += `<polyline points="${pts.join(' ')}" fill="none" stroke="${cols[k]}" stroke-width=".4" stroke-opacity=".85"/>`;
    }
    return `<svg class="pseal" viewBox="0 0 100 100" aria-hidden="true">${paths}<circle cx="50" cy="50" r="22" fill="#fff" stroke="#0E1B3D" stroke-width=".5"/><text x="50" y="49" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="9" fill="#0E1B3D">ATOMIC</text><text x="50" y="58" text-anchor="middle" font-family="Figtree" font-weight="700" font-size="5.5" fill="#0149AF">VERIFIED</text></svg>`;
  }
  function waves() {
    let s = '';
    for (let i = 0; i < 9; i++) { let p = ''; for (let x = 0; x <= 178; x += 2) p += (x ? ' L' : 'M') + x + ',' + (6 + Math.sin(x / (7 + i * .6) + i) * 3.2 + Math.cos(x / 13) * 1.2).toFixed(2);
      s += `<path d="${p}" fill="none" stroke="${i % 2 ? '#0149AF' : '#B9842B'}" stroke-width=".18" stroke-opacity=".7"/>`; }
    return `<svg class="pwaves" viewBox="0 0 178 12" preserveAspectRatio="none" aria-hidden="true">${s}</svg>`;
  }
  // one printed copy: fresh time + copy number + code
  function copyInfo(doc, learner, serial) {
    const d = new Date(), s = String(serial).padStart(6, '0'), when = stamp(d);
    return { name: learner.name || 'Learner', lid: learner.lid, date: d, when, serial: s, code: code(`${doc}|${learner.lid}|${s}|${when}`) };
  }
  // deterrents on a container: no context menu, copy, drag or select; Ctrl/Cmd+S blocked, Ctrl/Cmd+P → onPrint
  function guard(box, onPrint) {
    ['contextmenu', 'copy', 'cut', 'dragstart', 'selectstart'].forEach(ev => box.addEventListener(ev, e => e.preventDefault()));
    const key = e => { if (!document.body.contains(box)) { document.removeEventListener('keydown', key); return; }
      const k = (e.key || '').toLowerCase(); if ((e.ctrlKey || e.metaKey) && (k === 's' || k === 'p')) { e.preventDefault(); if (k === 'p') onPrint(); } };
    document.addEventListener('keydown', key);
  }
  return { code, stamp, frame, watermark, seal, waves, copyInfo, guard, esc };
})();
