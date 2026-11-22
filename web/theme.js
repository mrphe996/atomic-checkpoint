/* Atomic — theme switch. Loaded in <head> before the stylesheet.
   oak (default) = Atomic "Design system B" from the Atomic Science design file: Lexend, ink on white, mint / lemon / lavender bands.
   classic = the earlier Atomic blue design (styles.css). styles-oak.css is generated from styles.css by tools/build-theme.mjs,
   so the layout is the same. Switch with ?theme=classic or ?theme=oak (remembered), or ATOMIC_CONFIG.theme. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.AtomicTheme = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  const hex2 = v => Math.round(Math.max(0, Math.min(255, v))).toString(16).padStart(2, '0').toUpperCase();
  function toHsl(hex) {
    const r = parseInt(hex.slice(1, 3), 16) / 255, g = parseInt(hex.slice(3, 5), 16) / 255, b = parseInt(hex.slice(5, 7), 16) / 255;
    const mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2, d = mx - mn; let h = 0, s = 0;
    if (d) { s = d / (1 - Math.abs(2 * l - 1)); h = mx === r ? ((g - b) / d) % 6 : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h = (h * 60 + 360) % 360; }
    return [h, s, l];
  }
  function fromHsl(h, s, l) {
    const c = (1 - Math.abs(2 * l - 1)) * s, x = c * (1 - Math.abs((h / 60) % 2 - 1)), m = l - c / 2;
    const [r, g, b] = h < 60 ? [c, x, 0] : h < 120 ? [x, c, 0] : h < 180 ? [0, c, x] : h < 240 ? [0, x, c] : h < 300 ? [x, 0, c] : [c, 0, x];
    return '#' + hex2((r + m) * 255) + hex2((g + m) * 255) + hex2((b + m) * 255);
  }
  /* Atomic "Design system B" (the Atomic Science design file): Lexend, ink #222 on white, pastel bands, 4–6 px corners.
     Named tokens map exactly; any other colour keeps its lightness so every contrast pair still works. */
  const FIX = { '#0149AF': '#222222', '#013A8C': '#000000', '#013C90': '#000000', '#0A58CA': '#000000', '#00306F': '#000000', '#2F6FD6': '#575757',
    '#A9C6F2': '#CACACA', '#BFD3F0': '#CACACA', '#DCE8FA': '#F2F2F2', '#EAF1FC': '#F2F2F2', '#F3F7FD': '#F9F9F9', '#F3F8FF': '#FFF7CC', '#F2F7FF': '#F2F2F2',
    '#F7FAFE': '#FFFFFF', '#0B2545': '#222222', '#0E1B3D': '#222222', '#1C2A3A': '#222222', '#000F24': '#000000',
    '#556377': '#575757', '#5B6478': '#575757', '#52627A': '#575757', '#3E4558': '#575757', '#3A4B63': '#575757', '#8B98AB': '#808080',
    '#D3E0F4': '#CACACA', '#D3E0F2': '#575757', '#D6E2F0': '#CACACA', '#D5DCE8': '#CACACA', '#C9D6E6': '#575757', '#E6EEF8': '#E4E4E4', '#E1E6EF': '#E4E4E4', '#E3EAF3': '#E4E4E4',
    '#EEF4FB': '#F2F2F2', '#F6F7FB': '#F9F9F9',
    '#F3BF69': '#FFE555', '#F7CC84': '#FFE555', '#C48A2C': '#222222', '#935A00': '#222222', '#6B4300': '#222222', '#FFF4D6': '#FFF7CC', '#FFF6E0': '#FFF7CC',
    '#1E8E4E': '#287C34', '#1E7A45': '#287C34', '#E5F6EC': '#E8F9E8', '#9ED5B4': '#BEF2BD', '#C93A3A': '#DD0035', '#B42318': '#DD0035' };
  function oak(hex) {
    if (hex.length === 4) hex = '#' + hex[1] + hex[1] + hex[2] + hex[2] + hex[3] + hex[3];
    hex = hex.toUpperCase(); if (FIX[hex]) return FIX[hex];
    const [h, s, l] = toHsl(hex);
    if (s < 0.1) return hex;
    if (h >= 195 && h <= 252) {                        // the blue / navy family → ink and greys
      if (l >= 0.965) return '#FFFFFF';
      if (l < 0.42) return '#222222';
      return fromHsl(0, 0, l);
    }
    if (h >= 26 && h <= 50 && s > 0.3) {               // spark gold → lemon
      if (l > 0.85) return '#FFF7CC';
      if (l > 0.55) return '#FFE555';
      return '#222222';
    }
    return hex;
  }
  const cache = {};
  const radius = t => t.replace(/border-radius:\s*(\d+)px(?=\s*[;}"'`]|$)/g, (m, n) => (+n >= 90 || +n < 7 ? m : 'border-radius:6px'));
  const mapText = t => typeof t !== 'string' ? t : radius(t.replace(/#[0-9a-fA-F]{6}\b/g, m => cache[m] || (cache[m] = oak(m)))
    .replace(/rgba\(\s*1\s*,\s*73\s*,\s*175\s*,/g, 'rgba(92,92,92,').replace(/rgba\(\s*11\s*,\s*37\s*,\s*69\s*,/g, 'rgba(92,92,92,'));

  let name = 'classic';
  if (typeof document !== 'undefined') {
    let q = null, saved = null; try { q = new URLSearchParams(location.search).get('theme'); saved = localStorage.getItem('atomic.theme'); } catch (e) { }
    if (q === 'oak' || q === 'classic') { try { localStorage.setItem('atomic.theme', q); } catch (e) { } saved = q; }
    const cfg = (self.ATOMIC_CONFIG || {}).theme;
    name = saved || cfg || 'oak';
    if (name !== 'oak') name = 'classic';
    document.documentElement.classList.add('theme-' + name);
    document.write('<link rel="stylesheet" href="' + (name === 'oak' ? 'styles-oak.css' : 'styles.css') + '">');
  }
  return { name, oak, mapText, style: t => (name === 'oak' ? mapText(t) : t) };
});
