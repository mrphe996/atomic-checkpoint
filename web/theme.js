/* Camday — theme switch. Loaded in <head> before the stylesheet.
   oak (default) = Camday "Design system B" from the Camday Science design file: Lexend, ink on white, mint / lemon / lavender bands.
   classic = the earlier Camday blue design (styles.css). styles-oak.css is generated from styles.css by tools/build-theme.mjs,
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
  /* Camday "Design system B" (the Camday Science design file): Lexend, ink #222 on white, pastel bands, 4–6 px corners.
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

  /* ---- light / dark: every colour in a declaration becomes var(--<role>-<hex>, <light value>); html.dark defines the dark value.
     Roles: t = text (color, fill, stroke) · b = background · l = lines (border, outline, box-shadow). ---- */
  const ROLE = p => (/^(color|fill|stroke|caret-color|text-decoration-color|-webkit-text-fill-color)$/.test(p) ? 't' : /^background/.test(p) ? 'b' : /^(border|outline|box-shadow|column-rule)/.test(p) ? 'l' : null);
  // light mode, softened so long study sessions are easier on the eyes (no pure white, calmer mint)
  const LIGHT = { b: {},
    l: {}, t: {} };   // true white pages and the full-strength pastels
  const DARK = { b: { '#FFFFFF': '#1F2329', '#F4F4F1': '#14171B', '#F9F9F9': '#252A31', '#F2F2F2': '#2B3038', '#E4E4E4': '#323840', '#CACACA': '#3B424B', '#222222': '#39404A', '#000000': '#4A525E', '#575757': '#4A525E', '#808080': '#5B6470',
      '#BEF2BD': '#1F3B2A', '#E8F9E8': '#1B3024', '#FFF7CC': '#3A3417', '#FFE555': '#544A16', '#0149AF': '#2F6FD6', '#013A8C': '#3B7BE2', '#FDECEC': '#3D2026', '#FFF8F8': '#332025' },
    t: { '#222222': '#ECEBE7', '#000000': '#FFFFFF', '#575757': '#B7BBC2', '#808080': '#8F959E', '#0149AF': '#8DB6FF', '#013A8C': '#B1CDFF', '#287C34': '#7FD88D', '#DD0035': '#FF8094' },
    l: { '#222222': '#8A919B', '#000000': '#A3AAB4', '#575757': '#6B737E', '#CACACA': '#3F4650', '#E4E4E4': '#333A43', '#D6D6D2': '#333A43', '#0149AF': '#5E97F5', '#BDBDB8': '#4A525E' } };
  function darkOf(role, hex) {
    if (DARK[role][hex]) return DARK[role][hex];
    const [h, s, l] = toHsl(hex);
    if (role === 't') { if (hex === '#FFFFFF') return hex; if (s < 0.15) return l < 0.6 ? fromHsl(0, 0, Math.min(0.93, 1 - l * 0.6)) : hex; return l < 0.5 ? fromHsl(h, Math.min(s, 0.75), 0.72) : hex; }
    if (role === 'b') { if (s < 0.15) return l > 0.5 ? fromHsl(215, 0.12, 0.13 + (1 - l) * 0.45) : fromHsl(215, 0.12, 0.26 + l * 0.2); return l > 0.6 ? fromHsl(h, Math.min(s, 0.42), 0.2) : hex; }
    if (s < 0.15) return l > 0.5 ? fromHsl(215, 0.1, 0.28) : fromHsl(215, 0.08, 0.6);
    return l > 0.6 ? fromHsl(h, 0.3, 0.32) : hex;
  }
  const defs = {}; let onDef = null;
  function roleHex(role, hex) {
    hex = hex.toUpperCase(); const light = LIGHT[role][hex] || hex, d = darkOf(role, hex);
    if (d === light) return light;
    const n = '--' + role + '-' + hex.slice(1); if (!defs[n]) { defs[n] = d; if (onDef) onDef(n, d); }
    return 'var(' + n + ',' + light + ')';
  }
  /* "prop:value;prop:value" (a style attribute or a whole stylesheet) → the same text with themed colours */
  const declText = t => typeof t !== 'string' ? t : t.replace(/(^|[;{]\s*)([a-zA-Z-]+)\s*:\s*([^;{}]*)/g, (m, pre, prop, val) => {
    const r = ROLE(prop.toLowerCase()); if (!r || val.indexOf('#') < 0) return m;
    return pre + prop + ':' + val.replace(/#[0-9a-fA-F]{6}\b/g, h => roleHex(r, h)); });

  let name = 'classic', mode = 'light';
  if (typeof document !== 'undefined') {
    let q = null, saved = null; try { q = new URLSearchParams(location.search).get('theme'); saved = localStorage.getItem('atomic.theme'); mode = localStorage.getItem('atomic.mode') === 'dark' ? 'dark' : 'light'; } catch (e) { }
    if (q === 'oak' || q === 'classic') { try { localStorage.setItem('atomic.theme', q); } catch (e) { } saved = q; }
    const cfg = (self.ATOMIC_CONFIG || {}).theme;
    name = saved || cfg || 'oak';
    if (name !== 'oak') { name = 'classic'; mode = 'light'; }
    const H = document.documentElement; H.classList.add('theme-' + name); if (mode === 'dark') H.classList.add('dark');
    document.write('<link rel="stylesheet" href="' + (name === 'oak' ? 'styles-oak.css' : 'styles.css') + '">');
    // colours first met in inline styles get their dark value here
    let tag = null; onDef = (n, d) => { if (!tag) { tag = document.createElement('style'); tag.id = 'atomic-dark-vars'; document.head.appendChild(tag); } tag.appendChild(document.createTextNode('html.dark{' + n + ':' + d + '}')); };
  }
  function setMode(m) {
    mode = m === 'dark' && name === 'oak' ? 'dark' : 'light'; try { localStorage.setItem('atomic.mode', mode); } catch (e) { }
    if (typeof document !== 'undefined') document.documentElement.classList.toggle('dark', mode === 'dark');
    return mode;
  }
  return { name, oak, mapText, declText, defs, setMode, get mode() { return mode; }, style: t => (name === 'oak' ? declText(mapText(t)) : t) };
});
