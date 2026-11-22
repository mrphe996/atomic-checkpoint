#!/usr/bin/env node
// Builds web/styles-oak.css from web/styles.css: same rules and layout, colours and corner radii mapped by web/theme.js to
// Atomic "Design system B" (Atomic Science design file), Lexend type, plus the component rules of that system.
import fs from 'node:fs'; import path from 'node:path'; import { createRequire } from 'node:module'; import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const mod = { exports: {} }; new Function('module', 'self', fs.readFileSync(path.join(ROOT, 'web/theme.js'), 'utf8'))(mod, {}); const T = mod.exports;   // the browser file, loaded as CommonJS
let css = fs.readFileSync(path.join(ROOT, 'web/styles.css'), 'utf8');
css = T.mapText(css).replace(/#([0-9a-fA-F])([0-9a-fA-F])([0-9a-fA-F])\b(?![0-9a-fA-F])/g, (m) => T.oak(m))
  .replace(/Outfit,\s*Figtree,\s*sans-serif/g, 'Lexend,system-ui,sans-serif').replace(/Outfit,\s*sans-serif/g, 'Lexend,system-ui,sans-serif')
  .replace(/Figtree,\s*system-ui/g, 'Lexend,system-ui').replace(/\bFigtree\b/g, 'Lexend').replace(/\bOutfit\b/g, 'Lexend');
// flat look: drop the 3D "0 Npx 0 colour" ledges, soften the big glows
css = css.replace(/box-shadow:([^;}]+)/g, (m, v) => 'box-shadow:' + v.split(/,(?![^(]*\))/).map(x => x.trim())
  .map(x => (/^0 \d+px 0 (?!0)/.test(x) && !/inset/.test(x) ? '0 0 0 transparent' : x)).join(','));
const extra = `
/* ---------- Design system B (generated: edit tools/build-theme.mjs) ---------- */
body{background:#fff;color:#222;line-height:1.55}
h1,h2,h3,.lex{font-family:Lexend,system-ui,sans-serif;font-weight:600;letter-spacing:-.01em}
a{color:#0149AF;text-underline-offset:3px}a:hover{color:#013A8C}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,summary:focus-visible,[tabindex]:focus-visible{outline:none;box-shadow:0 0 0 2px #FFE555,0 0 0 5px #575757!important}
.dots{background-image:none}
.dhero,.phero,.u4hero,.hero,.lp-hero{background:#BEF2BD;background-image:none;border-bottom:0}
.dhero h1,.phero h1,.u4hero h1,.hero h1,.lp-hero h1{font-weight:600}
.dhero p,.phero p,.u4hero .lead,.hero p{color:#222}
.hero .crumb,.hero .crumb a,.hero .eyebrow{color:#222}
.demobar{background:#F2F2F2;color:#222;border-bottom:1px solid #CACACA}
.top{border-bottom:3px solid #222}
.mainnav a{border-radius:6px;color:#222}
.mainnav a:hover{background:#F2F2F2;color:#222;text-decoration:underline}
.mainnav a.on{background:#F2F2F2;color:#222;font-weight:700}
.pill,.pill.xp,.pill.streak{background:#fff;border:1px solid #222;color:#222;box-shadow:none;font-weight:500}
.avatar{background:#FFE555;border:2px solid #222;color:#222;box-shadow:none}
.menu-btn{background:#fff;border:1.5px solid #CACACA;border-radius:6px;color:#222}
.toast{background:#FFE555;color:#222;border:2px solid #222;border-radius:6px;box-shadow:0 8px 8px rgba(92,92,92,.2)}
.subbar,.subbar.blue{background:#222;color:#fff}
.subbar .gchip{background:#FFE555;color:#222}
.card{border:1px solid transparent;border-radius:6px;box-shadow:0 8px 8px rgba(92,92,92,.12)}
.card.cur{border:2px solid #222}
.card.done{border-color:#BEF2BD;background:#E8F9E8;box-shadow:none}
.card.bad{box-shadow:none}
.card.feature{background:#BEF2BD;color:#222;border:3px solid #222;box-shadow:none}
.card.feature a,.card.feature .muted,.card.feature h2,.card.feature h3,.card.feature b{color:#222}
.btn{border-radius:4px;border:2px solid #222;background:#fff;color:#222;font-weight:600;box-shadow:none}
.btn:hover{background:#fff;text-decoration:underline;box-shadow:0 8px 8px rgba(92,92,92,.2);transform:translateY(-1px)}
.btn:active{transform:translateY(1px)!important;box-shadow:none!important}
.btn.primary,.btn.navy,.btn.sel{background:#222;color:#fff;border:2px solid #222;box-shadow:none}
.btn.primary:hover,.btn.navy:hover{background:#222;box-shadow:0 8px 8px rgba(92,92,92,.2)}
.btn.gold{background:#FFE555;color:#222;border:2px solid #222;box-shadow:none}
.btn.gold:hover{background:#FFE555;box-shadow:0 8px 8px rgba(92,92,92,.2)}
.btn.ghost{background:#fff;color:#222;border:2px solid #222;box-shadow:none}
.btn.onblue{border:2px solid #fff;color:#fff;background:transparent;box-shadow:none}
.btn.onblue:hover{background:transparent}
.btn.small{border-radius:4px}.btn.big{border-radius:4px}
.btn:disabled{background:#808080;border-color:#808080;color:#fff;opacity:1;text-decoration:none}
.chip{border-radius:4px;border:1px solid #575757;font-weight:500;color:#222;box-shadow:none}
.chip:hover{border-color:#222;color:#222;text-decoration:underline}
.chip.on{background:#222;border-color:#222;color:#fff;box-shadow:none}
.tag{border-radius:4px}
.opt{border:2px solid #CACACA;border-radius:6px;box-shadow:none}
.opt:hover{border-color:#222}
.opt .key{border-radius:50%;background:#F2F2F2;color:#222}
.opt.sel{border-color:#222;background:#FFF7CC;box-shadow:none;transform:none}
.opt.sel .key{background:#222;color:#fff}
.opt.right{box-shadow:none}.opt.wrong{box-shadow:none}
.banner{border-radius:6px}
.banner.info{background:#F2F2F2}
.banner.adv{background:#FFF7CC;border-color:#FFF7CC}
.banner.ok{background:#E8F9E8;border-color:#E8F9E8}
.eyebrow{color:#222;letter-spacing:.04em}
.pbar{border-radius:4px;background:#fff;box-shadow:inset 0 0 0 2px #222}
.pbar i{background:#287C34;border-radius:0}
.pbar.red i{background:#DD0035}
input[type=text],input[type=password],input[type=number],input[type=email],select,textarea{border:1px solid #575757;border-radius:4px;color:#222}
input[type=checkbox],input[type=radio]{accent-color:#222}
.tabs{border-bottom:2px solid #CACACA;gap:4px;padding:0;background:none;border-radius:0}
.tabs button{border-radius:0;background:none;color:#575757;border:0;border-bottom:4px solid transparent;margin-bottom:-2px;font-weight:600;box-shadow:none}
.tabs button.on{color:#222;border-bottom-color:#222;background:none}
.lbrow:hover{background:#FFF7CC}
.froom .flv.on{background:#222;color:#fff;border-color:#222}
html.theme-oak #splash{background:#fff}
html.theme-oak #splash .sp-in{color:#222}
html.theme-oak #splash .sp-bar{background:#F2F2F2}
html.theme-oak #splash .sp-bar i{background:#222}
`;
fs.writeFileSync(path.join(ROOT, 'web/styles-oak.css'), '/* GENERATED by tools/build-theme.mjs from styles.css — do not edit */\n' + css + extra);
console.log('theme: web/styles-oak.css', (css.length + extra.length), 'bytes');
