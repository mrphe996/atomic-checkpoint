#!/usr/bin/env node
// Builds web/styles-oak.css from web/styles.css: same rules and layout, colours and corner radii mapped by web/theme.js to
// Camday "Design system B" (Camday Science design file), Lexend type, plus the component rules of that system.
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
:root{--band:#F4F4F1;--sh:0 1px 2px rgba(34,34,34,.10),0 10px 24px rgba(34,34,34,.12);--bd:1px solid #D6D6D2}
body{background:#F4F4F1;color:#222;line-height:1.55}
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
.card{border:1px solid #D6D6D2;border-radius:6px;box-shadow:0 1px 2px rgba(34,34,34,.10),0 10px 24px rgba(34,34,34,.12)}
.card.cur{border:2px solid #222}
.card.done{border-color:#BEF2BD;background:#E8F9E8;box-shadow:none}
.card.bad{box-shadow:none}
.card.feature{background:#BEF2BD;color:#222;border:3px solid #222;box-shadow:none}
.card.feature a,.card.feature .muted,.card.feature h2,.card.feature h3,.card.feature b{color:#222}
.btn{border-radius:4px;border:2px solid #0149AF;background:#fff;color:#0149AF;font-weight:600;box-shadow:none}
.btn:hover{background:#fff;text-decoration:underline;box-shadow:0 8px 8px rgba(92,92,92,.2);transform:translateY(-1px)}
.btn:active{transform:translateY(1px)!important;box-shadow:none!important}
.btn.primary,.btn.navy,.btn.sel{background:#0149AF;color:#fff;border:2px solid #0149AF;box-shadow:none}
.btn.primary:hover,.btn.navy:hover{background:#013A8C;border-color:#013A8C;box-shadow:0 8px 8px rgba(1,73,175,.25)}
.btn.gold{background:#FFE555;color:#222;border:2px solid #222;box-shadow:none}
.btn.gold:hover{background:#FFE555;box-shadow:0 8px 8px rgba(92,92,92,.2)}
.btn.ghost{background:#fff;color:#0149AF;border:2px solid #0149AF;box-shadow:none}
.btn.onblue{border:2px solid #fff;color:#fff;background:transparent;box-shadow:none}
.btn.onblue:hover{background:transparent}
.btn.small{border-radius:4px}.btn.big{border-radius:4px}
.btn:disabled{background:#808080;border-color:#808080;color:#fff;opacity:1;text-decoration:none}
.chip{border-radius:4px;border:1px solid #575757;font-weight:500;color:#222;box-shadow:none}
.chip:hover{border-color:#222;color:#222;text-decoration:underline}
.chip.on{background:#222;border-color:#222;color:#fff;box-shadow:none}
.tag{border-radius:4px}
.opt{border:2px solid #BDBDB8;border-radius:6px;box-shadow:0 1px 2px rgba(34,34,34,.08)}
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
.froom .flv.on b,.froom .flv.on small{color:#fff}
.lvx{border:1px solid #222;background:#fff}
.lvx-badge{background:#FFE555}
.lvx .lvbar,.xpg .lvbar{background:#fff;box-shadow:inset 0 0 0 1.5px #222;border-radius:4px}
.lvx .lvbar i,.xpg .lvbar i{background:#287C34;border-radius:0}
.xpg-now{background:#E8F9E8;border-radius:6px}
.xpg-row>b{color:#287C34}
.xpg-step{background:#F2F2F2;border-color:#CACACA}
.xpg-step.goal{background:#FFF7CC;border-color:#222}
.modal{border-radius:6px;box-shadow:0 20px 50px rgba(34,34,34,.3)}
/* ---- 26/11/2026 review against the reference design system: white pages, ink buttons, flat cards, pastel bands ---- */
body{background:#FFFFFF}
:root{--band:#F2F2F2}
[tabindex="-1"]:focus,[tabindex="-1"]:focus-visible,#main:focus-visible{outline:none!important;box-shadow:none!important}
.btn{border:2px solid #222;color:#222;background:#fff;font-weight:600;min-height:48px}
.btn:hover{background:#F2F2F2;box-shadow:none;transform:none;text-decoration:underline}
.btn.primary,.btn.navy,.btn.sel{background:#222;color:#fff;border:2px solid #222}
.btn.primary:hover,.btn.navy:hover{background:#575757;border-color:#575757;box-shadow:none}
.btn.ghost{background:#fff;color:#222;border:2px solid #222}
.btn.gold:hover{box-shadow:none}
.btn.small{min-height:40px}
.card{box-shadow:none;border:1px solid #CACACA}
.u4topic,.stsw{box-shadow:none}
.u4topic.cur{border:2px solid #222}.u4topic.cur .u4num{background:#222;border-color:#222}
.u4hero{background:#F5E9F2}
.u4hero .lens2{background:#DEB7D5}
.phero{background:#E3E9FB}
.sw{background:#E3E9FB;border:1px solid #A0B6F2;border-radius:6px;min-height:52px}
.sw:hover{background:#C6D1EF;box-shadow:none;transform:none}
.sw.on{background:#222;border-color:#222}
.stsw .sgrow{background:none;gap:10px;padding:0}
.sw .swn{background:transparent;border:0}
footer.foot{border-top:3px solid #222;margin-top:64px}
footer.foot::before{display:none}
.fcol a{color:#222}
.rmit{box-shadow:none}
.su-basket{background:#E3E9FB;border-color:#A0B6F2}
.su-plan.on{background:#E3E9FB;border-color:#222;box-shadow:none}
.su-plan.on .su-tick,.su-chip{border-color:#222}
.su-plan.on .su-tick{background:#222}
/* media in a heavy ink frame, light body copy, announcement strip */
.player,.lp-video,.dthumb,.vthumb,video{border:4px solid #222;border-radius:0}
.lp-hero p,.phero p,.dhero p,.u4hero .lead,.hero p{font-weight:300;font-size:20px}
.lp-hero h1{font-weight:600;font-size:56px}.lp-hero h1 span{color:#222}
.lp-pill{border-radius:4px;border:0;background:#fff}
.newsstrip{display:flex;justify-content:center;gap:28px;flex-wrap:wrap;background:#B0E2DE;border-bottom:2px solid #222;padding:12px 20px;font-size:17px;font-weight:300}
.newsstrip a{font-weight:700;color:#222;text-decoration:none}.newsstrip a:hover{text-decoration:underline}
.tsum,.lbtop{background:#E3E9FB}
.lb-example .lbtop{background:#FFF7CC}.lb-method .lbtop{background:#F5E9F2}.lb-tip .lbtop{background:#E8F9E8}.lb-mistake .lbtop{background:#FDE3E3}
.tready .pbar.mini{flex:none;height:8px;width:160px}
.qbsum{background:#E3E9FB;border:0}
.qbt .lbrow.picked{background:#FFF7CC}
html.theme-oak #splash{background:#fff}
html.theme-oak #splash .sp-in{color:#222}
html.theme-oak #splash .sp-bar{background:#F2F2F2}
html.theme-oak #splash .sp-bar i{background:#222}
`;
// resolve the :root colour variables to literals, so each use can take the right light / dark role
let all = css + extra;
const root = {}; for (const m of all.matchAll(/:root\{([^}]*)\}/g)) for (const d of m[1].split(';')) { const k = d.indexOf(':'); if (k > 0) root[d.slice(0, k).trim()] = d.slice(k + 1).trim(); }
for (let i = 0; i < 4; i++) all = all.replace(/var\((--[a-z0-9]+)\)/g, (m, n) => (root[n] != null ? root[n] : m));
all = all.replace(/#([0-9a-fA-F])([0-9a-fA-F])([0-9a-fA-F])\b(?![0-9a-fA-F])/g, (m, r, g, b) => ('#' + r + r + g + g + b + b).toUpperCase());   // #222 → #222222 so short colours are themed too
all = T.declText(all);
const dark = `
/* ---------- dark mode: values for the themed colours (generated) ---------- */
html.dark{color-scheme:dark;${Object.entries(T.defs).map(([n, d]) => n + ':' + d).join(';')}}
html.dark body{background:#14171B;color:#ECEBE7}
/* printed pages (worksheets, certificates) stay white paper in dark mode: their colours fall back to the light values */
html.dark .a4{color-scheme:light;${Object.keys(T.defs).map(n => n + ':initial').join(';')}}
html.dark .brand img{background:#FBFAF6;border-radius:6px;padding:2px 6px}
html.dark .fig,html.dark .pfig,html.dark .scope,html.dark .cmap svg,html.dark .ws{background:#F3F1EB;border-radius:6px;color:#222}
html.dark .fig *{color:#222}
html.dark img.thumb,html.dark video{filter:brightness(.92)}
html.dark .card,html.dark .modal{box-shadow:0 1px 2px rgba(0,0,0,.5),0 10px 24px rgba(0,0,0,.35)}
html.dark ::placeholder{color:#8F959E}
html.dark .drow b{color:#9CC2FF!important}
html.dark .qbbar{background:rgba(31,35,41,.95)}
.brand img{mix-blend-mode:multiply}
html.dark .brand img{mix-blend-mode:normal}
.mainnav a{padding:10px 9px}
.topright{gap:8px}
@media (max-width:1420px){.lvx .lvx-mid{display:none}}
@media (max-width:640px){.topright{gap:4px}}
@media (max-width:480px){.topright .pill.streak{display:none}}
.modebtn{width:44px;height:44px;flex:none;border-radius:50%;border:1px solid #222;background:#FBFAF6;cursor:pointer;display:grid;place-items:center;font-size:19px;line-height:1;padding:0}
html.dark .modebtn{background:#2B3038;border-color:#8A919B}
`;
fs.writeFileSync(path.join(ROOT, 'web/styles-oak.css'), '/* GENERATED by tools/build-theme.mjs from styles.css — do not edit */\n' + all + dark);
console.log('theme: web/styles-oak.css', all.length + dark.length, 'bytes ·', Object.keys(T.defs).length, 'themed colours');
