/* Atomic word games — five games that help learners remember key words (Stages 1–6, Science, Maths and English).
   One player level for all games, with no top limit: every level makes the games faster and the words harder.
   Sound effects and music are made in the browser (Web Audio); words are read aloud from the lesson recordings
   or by the browser's English voice. Written by the Atomic teaching team. */
window.Games = (function () {
  'use strict';
  const GAMES = [
    { id: 'racer', name: 'Word Racer', icon: '🏎️', color: '#E2463A', about: 'Steer your car into the lane with the right word. The road gets faster every level.' },
    { id: 'balloon', name: 'Balloon Pop', icon: '🎈', color: '#7A4BD1', about: 'Pop the balloon that matches the meaning before it floats away.' },
    { id: 'memory', name: 'Memory Match', icon: '🃏', color: '#1F9D5C', about: 'Turn the cards over and match each word with its meaning.' },
    { id: 'spell', name: 'Spell It', icon: '🔤', color: '#0149AF', about: 'Build the word letter by letter. Fewer clues at higher levels.' },
    { id: 'whack', name: 'Word Whack', icon: '🔨', color: '#D9722A', about: 'Whack the mole holding the right word – quick, before it hides!' }];
  const SUBJ = { all: 'All subjects', science: 'Science', maths: 'Maths', english: 'English' };
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  function h(tag, attrs, ...kids) {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) { if (v == null || v === false) continue; if (k.startsWith('on')) n.addEventListener(k.slice(2), v); else if (k === 'html') n.innerHTML = v; else n.setAttribute(k, v === true ? '' : v); }
    for (const c of kids.flat()) if (c != null && c !== false) n.append(c.nodeType ? c : document.createTextNode(String(c)));
    return n;
  }
  const rnd = n => Math.floor(Math.random() * n);
  const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = rnd(i + 1); [a[i], a[j]] = [a[j], a[i]]; } return a; };

  /* ---------- levels: unlimited; each level needs a little more XP than the last ---------- */
  const need = L => 60 + 30 * L;                       // XP to go from level L to L + 1
  function levelOf(xp) { let L = 1, x = xp; while (x >= need(L)) { x -= need(L); L++; } return { level: L, into: x, need: need(L) }; }
  function tuning(L) {   // how hard the games are at level L
    return {
      mode: L <= 3 ? 'pic' : L <= 7 ? 'def' : (L <= 14 ? (Math.random() < 0.35 ? 'hear' : 'def') : (Math.random() < 0.6 ? 'hear' : 'def')),
      near: L >= 6,                                           // wrong answers from the same topic (harder to tell apart)
      choices: Math.min(6, 3 + Math.floor((L - 1) / 4)),
      speed: Math.min(3.2, 1 + 0.08 * (L - 1)),
      rounds: Math.min(20, 10 + Math.floor(L / 4)),
      pairs: Math.min(10, 4 + Math.floor((L - 1) / 2)),
      extra: Math.min(7, 1 + Math.floor(L / 2)), reveal: L <= 2 ? 0.5 : L <= 5 ? 'first' : 0,
      upTime: Math.max(0.85, 2.4 - 0.09 * (L - 1)),
      newer: Math.min(0.9, 0.5 + 0.04 * L)                    // share of words from the chosen stage (the rest revise earlier stages)
    };
  }

  /* ---------- sound: effects + a little looping tune, all synthesised ---------- */
  const Snd = { ac: null, music: false, voice: true, timer: null, step: 0 };
  function ac() { if (!Snd.ac) { try { Snd.ac = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { Snd.ac = null; } } if (Snd.ac && Snd.ac.state === 'suspended') Snd.ac.resume().catch(() => { }); return Snd.ac; }
  function tone(f, t0, dur, type = 'sine', vol = 0.18) { const a = ac(); if (!a) return; const o = a.createOscillator(), g = a.createGain(); o.type = type; o.frequency.setValueAtTime(f, a.currentTime + t0);
    g.gain.setValueAtTime(0.0001, a.currentTime + t0); g.gain.exponentialRampToValueAtTime(vol, a.currentTime + t0 + 0.015); g.gain.exponentialRampToValueAtTime(0.0001, a.currentTime + t0 + dur);
    o.connect(g); g.connect(a.destination); o.start(a.currentTime + t0); o.stop(a.currentTime + t0 + dur + 0.05); }
  const SFX = {
    right: () => { tone(660, 0, 0.12, 'triangle'); tone(990, 0.09, 0.18, 'triangle'); },
    wrong: () => { tone(180, 0, 0.22, 'sawtooth', 0.12); tone(140, 0.12, 0.25, 'sawtooth', 0.1); },
    pop: () => { tone(900, 0, 0.06, 'square', 0.1); tone(400, 0.03, 0.08, 'triangle', 0.12); },
    flip: () => tone(520, 0, 0.06, 'triangle', 0.1),
    tap: () => tone(740, 0, 0.05, 'sine', 0.12),
    whack: () => { tone(220, 0, 0.08, 'square', 0.14); tone(330, 0.05, 0.1, 'triangle', 0.12); },
    star: () => { tone(1320, 0, 0.08, 'sine', 0.1); tone(1760, 0.06, 0.1, 'sine', 0.08); },
    level: () => [523, 659, 784, 1047, 1319].forEach((f, i) => tone(f, i * 0.11, 0.28, 'triangle', 0.16)),
    end: () => [784, 659, 523, 659, 784].forEach((f, i) => tone(f, i * 0.1, 0.2, 'triangle', 0.13)) };
  function sfx(k) { try { SFX[k] && SFX[k](); } catch (e) { } }
  const TUNE = [523, 659, 784, 659, 587, 698, 880, 698, 523, 659, 784, 1047, 988, 784, 659, 587];
  function musicOn(on) {
    Snd.music = on; clearInterval(Snd.timer); Snd.timer = null;
    if (on && ac()) Snd.timer = setInterval(() => { const f = TUNE[Snd.step++ % TUNE.length]; tone(f, 0, 0.22, 'triangle', 0.045); if (Snd.step % 2 === 0) tone(f / 2, 0, 0.3, 'sine', 0.04); }, 260);
  }
  let curAudio = null;
  function say(text, file) {
    if (!Snd.voice) return;
    try { if (curAudio) { curAudio.pause(); curAudio = null; } window.speechSynthesis && speechSynthesis.cancel(); } catch (e) { }
    if (file) { curAudio = new Audio(file); curAudio.play().catch(() => speak(text)); return; }
    speak(text);
  }
  function speak(text) { try { const ss = window.speechSynthesis; if (!ss) return; const u = new SpeechSynthesisUtterance(text); u.lang = 'en-GB'; u.rate = 0.85; const v = ss.getVoices().find(x => /en-GB/i.test(x.lang)); if (v) u.voice = v; ss.speak(u); } catch (e) { } }

  /* ---------- words ---------- */
  let WORDS = null;
  async function words() { if (!WORDS) { const r = await fetch('content/game-words.json'); WORDS = (await r.json()).words; } return WORDS; }
  function pool(S) {
    const all = WORDS.filter(w => (S.subj === 'all' || w.subj === S.subj) && w.stage <= S.stage);
    return all.length >= 8 ? all : WORDS.filter(w => w.stage <= Math.max(S.stage, 2));
  }
  function mastery(S, w) { const m = (S.words || {})[w.id]; return m ? m[1] / Math.max(1, m[0]) : 0; }
  function pickTarget(S, P, T, avoid) {   // weak and new words come up more often; most words come from the chosen stage
    const cur = P.filter(w => w.stage === S.stage && !avoid.has(w.id)), old = P.filter(w => w.stage < S.stage && !avoid.has(w.id));
    const from = (cur.length && (Math.random() < T.newer || !old.length)) ? cur : old.length ? old : P.filter(w => !avoid.has(w.id)).concat(P).slice(0, Math.max(1, P.length));
    const wts = from.map(w => { const m = (S.words || {})[w.id]; return m ? 0.4 + 2 * (1 - m[1] / Math.max(1, m[0])) : 2.4; });
    let x = Math.random() * wts.reduce((a, b) => a + b, 0); for (let i = 0; i < from.length; i++) { x -= wts[i]; if (x <= 0) return from[i]; } return from[from.length - 1];
  }
  function distractors(P, target, n, near) {
    const same = P.filter(w => w.id !== target.id && w.w.toLowerCase() !== target.w.toLowerCase() && w.emoji !== target.emoji);
    const pref = near ? shuffle(same.filter(w => w.topic === target.topic)) : [];
    const rest = shuffle(same.filter(w => !pref.includes(w)));
    const out = []; for (const w of pref.concat(rest)) { if (out.length >= n) break; if (!out.some(o => o.w === w.w)) out.push(w); } return out;
  }
  function round(S, P, T, used) {
    const t = pickTarget(S, P, T, used); used.add(t.id);
    const opts = shuffle([t].concat(distractors(P, t, T.choices - 1, T.near)));
    return { t, opts, mode: T.mode };
  }

  /* ---------- styles (not themed: the games keep their own bright colours) ---------- */
  const CSS = `
.gw{--gn:#0E2A52;background:linear-gradient(180deg,#123766,#0E2A52);border-radius:28px;padding:18px;color:#fff;max-width:620px;margin:0 auto;font-family:Outfit,Figtree,sans-serif;position:relative;user-select:none;-webkit-user-select:none;touch-action:manipulation}
.gw .gtop{display:flex;align-items:center;gap:8px;margin-bottom:12px}.gw .gtop h2{flex:1;margin:0;font-size:24px;line-height:1.1;color:#fff}
.gw .gbtn{border:0;border-radius:999px;background:#DDE6F3;color:#0E2A52;font:700 15px Outfit,sans-serif;padding:10px 14px;cursor:pointer;box-shadow:0 3px 0 #9FB3CF}
.gw .gbtn.on{background:#FFD25A}.gw .gbtn:active{transform:translateY(2px);box-shadow:0 1px 0 #9FB3CF}
.gw .gcard{background:#fff;color:#0E2A52;border-radius:20px;padding:12px 16px;box-shadow:0 6px 0 rgba(0,0,0,.15);margin-bottom:12px;position:relative}
.gw .ghud{display:flex;justify-content:space-between;align-items:center;font-weight:800;font-size:15px}
.gw .gprompt{display:flex;align-items:center;justify-content:center;gap:12px;min-height:64px;text-align:center;font-size:20px;font-weight:800;line-height:1.25;padding:4px 0}
.gw .gprompt .ge{font-size:42px}.gw .gprompt .hear{border:0;background:#0149AF;color:#fff;border-radius:999px;font:800 18px Outfit;padding:10px 16px;cursor:pointer}
.gw .gbar{height:8px;background:#E3EAF5;border-radius:9px;overflow:hidden}.gw .gbar i{display:block;height:100%;background:#2FA8F5;border-radius:9px;transition:width .3s}
.gw .garena{position:relative;border-radius:22px;overflow:hidden;background:#fff;border:6px solid #fff}
.gw canvas{display:block;width:100%;height:auto;margin:0 auto;touch-action:none}
.gw .garena:has(canvas){background:#5DBB63}
.gw .gctrl{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}.gw .gctrl button{height:74px;border:0;border-radius:20px;background:#fff;box-shadow:0 6px 0 #9DB8D9;font-size:34px;color:#E2463A;cursor:pointer}
.gw .gctrl button:active{transform:translateY(3px);box-shadow:0 3px 0 #9DB8D9}
.gw .float{position:absolute;font:900 26px Outfit;color:#FFD25A;text-shadow:0 2px 0 #0008;pointer-events:none;animation:gfl 0.9s ease-out forwards}
@keyframes gfl{to{transform:translateY(-60px);opacity:0}}
.gw .shake{animation:gsh .35s}@keyframes gsh{25%{transform:translateX(-8px)}75%{transform:translateX(8px)}}
.gsky{height:min(460px,calc(100vh - 330px));min-height:320px;background:linear-gradient(#8FD3FF,#D9F1FF)}
.gbal{position:absolute;width:118px;height:140px;cursor:pointer;display:flex;align-items:flex-start;justify-content:center;border:0;background:none;padding:0}
.gbal span{display:flex;align-items:center;justify-content:center;width:112px;height:126px;border-radius:50% 50% 46% 46%;color:#fff;font:800 16px Outfit;text-align:center;padding:10px;box-shadow:inset -10px -12px 0 rgba(0,0,0,.12);word-break:break-word;line-height:1.1}
.gbal:after{content:'';position:absolute;left:58px;top:124px;width:2px;height:30px;background:#7A8699}
.gbal.popped span{animation:gpop .25s forwards}@keyframes gpop{to{transform:scale(1.6);opacity:0}}
.gmem{display:grid;gap:10px;padding:10px;background:#E9F6EE}
.gmc{aspect-ratio:3/4;border:0;border-radius:14px;cursor:pointer;perspective:600px;background:none;padding:0;font-family:Outfit}
.gmc .in{position:relative;width:100%;height:100%;transition:transform .35s;transform-style:preserve-3d}.gmc.open .in,.gmc.done .in{transform:rotateY(180deg)}
.gmc .fa,.gmc .fb{position:absolute;inset:0;border-radius:14px;display:flex;align-items:center;justify-content:center;backface-visibility:hidden;-webkit-backface-visibility:hidden;padding:6px;text-align:center}
.gmc .fa{background:linear-gradient(135deg,#1F9D5C,#16794A);color:#fff;font-size:30px;box-shadow:0 4px 0 #0F5C38}
.gmc .fb{background:#fff;color:#0E2A52;transform:rotateY(180deg);font-weight:800;font-size:15px;line-height:1.15;box-shadow:0 4px 0 #B7C6DA;flex-direction:column;gap:2px}
.gmc .fb b{font-size:28px}.gmc .fb small{font-weight:600;font-size:12px}.gmc.done .fb{background:#DDF5E6;box-shadow:0 4px 0 #7BC79A}
.gsp{padding:18px;background:#EEF4FD;min-height:330px;display:flex;flex-direction:column;gap:18px;align-items:center}
.gslots{display:flex;flex-wrap:wrap;justify-content:center;gap:6px}.gslot{width:40px;height:50px;border-radius:10px;background:#fff;border:3px solid #9DB8D9;display:flex;align-items:center;justify-content:center;font:900 26px Outfit;color:#0E2A52;text-transform:lowercase}
.gslot.sp{border:0;background:none;width:16px}.gslot.cur{border-color:#0149AF;box-shadow:0 0 0 3px #A9C6F2}.gslot.ok{background:#DDF5E6;border-color:#1F9D5C}
.gtiles{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;max-width:460px}.gtile{width:52px;height:56px;border:0;border-radius:12px;background:#0149AF;color:#fff;font:900 26px Outfit;cursor:pointer;box-shadow:0 4px 0 #013A8C;text-transform:lowercase}
.gtile:disabled{opacity:.25;cursor:default}
.gholes{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:16px;background:linear-gradient(#7CCB6B,#4FAE52);min-height:400px}
.ghole{position:relative;height:118px;border-radius:50%/40%;background:radial-gradient(ellipse at 50% 80%,#3A2716 0 45%,transparent 46%);overflow:hidden;border:0;padding:0;cursor:pointer}
.gmole{position:absolute;left:8%;right:8%;bottom:-100%;height:92%;border-radius:46% 46% 12% 12%;background:#9C6B43;transition:bottom .18s;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:10px;color:#fff;font:800 14px Outfit;text-align:center}
.gmole:before{content:'• •';display:block;font-size:20px;line-height:1;margin-bottom:2px}.gmole b{font-family:Outfit,sans-serif;background:#fff;color:#0E2A52;border-radius:8px;padding:2px 6px;font-size:14px;line-height:1.15;max-width:96%;word-break:break-word}
.ghole.up .gmole{bottom:0}.ghole.hit .gmole{background:#4BB46B}.ghole.bad .gmole{background:#C93A3A}
.gres{text-align:center;padding:24px 18px}.gres h3{font-size:30px;margin:6px 0;color:#0E2A52}.gres .big{font-size:56px}
.gxp{height:16px;border-radius:9px;background:#E3EAF5;overflow:hidden;margin:6px 0}.gxp i{display:block;height:100%;background:linear-gradient(90deg,#FFB800,#FFD25A);transition:width 1.2s ease}
.gwl{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:10px 0}.gwl button{border:0;border-radius:999px;background:#FDECEC;color:#B42318;font:700 14px Figtree;padding:6px 12px;cursor:pointer}
.ghub .gsel{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:6px 0}.ghub .chip{border:2px solid #D3E0F4;background:#fff;border-radius:999px;padding:6px 14px;font:700 15px Figtree;cursor:pointer;color:#1C2A3A}.ghub .chip.on{background:#0149AF;border-color:#0149AF;color:#fff}
.ghub .glist{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px;margin-top:16px}
.ghub .gg{display:flex;flex-direction:column;gap:8px;padding:18px;border-radius:22px;text-decoration:none;color:#fff;background:var(--c);box-shadow:0 6px 0 rgba(0,0,0,.18);transition:transform .15s}
.ghub .gg:hover{transform:translateY(-3px)}.ghub .gg .gi{font-size:44px;line-height:1}.ghub .gg b{font:800 22px Outfit}.ghub .gg span{font-size:14px;opacity:.95}.ghub .gg small{font-weight:700;background:rgba(255,255,255,.22);border-radius:999px;padding:3px 10px;align-self:flex-start}
.ghub .gplayer{display:flex;gap:18px;align-items:center;flex-wrap:wrap}.ghub .glv{width:86px;height:86px;border-radius:50%;background:linear-gradient(135deg,#FFD25A,#FFB800);display:flex;flex-direction:column;align-items:center;justify-content:center;font:900 30px Outfit;color:#5A3D00;box-shadow:0 5px 0 #C48A2C}
.ghub .glv small{font-size:11px;letter-spacing:.08em}.ghub .gpx{flex:1;min-width:220px}
@media (max-width:520px){.gw{padding:12px;border-radius:20px}.gw .gtop h2{font-size:19px}.gw .gbtn{padding:8px 11px;font-size:13px}.gbal{width:96px}.gbal span{width:92px;height:110px;font-size:14px}.gslot{width:32px;height:44px;font-size:22px}.gtile{width:44px;height:50px}}
.gconf{position:fixed;inset:0;pointer-events:none;z-index:99}.gconf i{position:absolute;top:-10px;width:10px;height:14px;animation:gcf 1.6s linear forwards}@keyframes gcf{to{transform:translateY(105vh) rotate(720deg)}}`;
  function styles() { if (!document.getElementById('gamesCss')) document.head.append(h('style', { id: 'gamesCss' }, CSS)); }
  function confetti() { const c = h('div', { class: 'gconf' }); const cols = ['#FFD25A', '#E2463A', '#2FA8F5', '#1F9D5C', '#7A4BD1']; for (let i = 0; i < 70; i++) c.append(h('i', { style: `left:${Math.random() * 100}%;background:${cols[i % 5]};animation-delay:${Math.random() * 0.6}s` })); document.body.append(c); setTimeout(() => c.remove(), 2600); }

  /* ---------- running game bookkeeping ---------- */
  let RUN = null;   // { stop() }
  function stop() { if (RUN) { try { RUN.stop(); } catch (e) { } RUN = null; } musicOn(false); try { window.speechSynthesis && speechSynthesis.cancel(); if (curAudio) curAudio.pause(); } catch (e) { } }

  /* ---------- hub ---------- */
  async function hub(host, ctx) {
    styles(); stop(); await words(); const S = ctx.load(); const lv = levelOf(S.xp || 0);
    const wrap = h('div', { class: 'ghub', id: 'gamesHub' });
    const sel = () => { wrap.innerHTML = ''; draw(); };
    function draw() {
      const P = pool(S), learned = P.filter(w => mastery(S, w) >= 0.75 && ((S.words || {})[w.id] || [0])[0] >= 2).length;
      wrap.append(h('section', { class: 'card' }, h('div', { class: 'gplayer' }, h('div', { class: 'glv', id: 'gLevel' }, h('small', {}, 'LEVEL'), String(lv.level)),
        h('div', { class: 'gpx' }, h('b', { style: 'font-family:Outfit;font-size:20px' }, (ctx.name ? ctx.name + ' · ' : '') + `Level ${lv.level} word champion`),
          h('div', { class: 'gxp' }, h('i', { style: `width:${Math.round(lv.into / lv.need * 100)}%` })), h('small', { class: 'muted' }, `${lv.into}/${lv.need} XP to level ${lv.level + 1} · ${S.xp || 0} XP in all · ${S.played || 0} games played · no top level – every level is a little harder`)),
        h('div', { style: 'text-align:center' }, h('b', { style: 'font:900 28px Outfit;color:#1F9D5C' }, String(learned)), h('br'), h('small', { class: 'muted' }, `of ${P.length} words learned`))),
        h('div', { class: 'gsel', role: 'group', 'aria-label': 'Stage' }, h('b', {}, 'Stage:'), ...[1, 2, 3, 4, 5, 6].map(n => h('button', { type: 'button', class: 'chip' + (S.stage === n ? ' on' : ''), id: 'gStage' + n, onclick: () => { S.stage = n; ctx.save(S); sel(); } }, String(n)))),
        h('div', { class: 'gsel', role: 'group', 'aria-label': 'Subject' }, h('b', {}, 'Words from:'), ...Object.entries(SUBJ).map(([k, t]) => h('button', { type: 'button', class: 'chip' + (S.subj === k ? ' on' : ''), id: 'gSubj-' + k, onclick: () => { S.subj = k; ctx.save(S); sel(); } }, t))),
        ctx.signedIn ? null : h('p', { class: 'muted', style: 'margin:6px 0 0;font-size:14px' }, 'Your level is saved on this device. Sign in to keep it on every device.')));
      wrap.append(h('div', { class: 'glist' }, ...GAMES.map(g => h('a', { class: 'gg', href: '#game-' + g.id, id: 'gOpen-' + g.id, style: `--c:${g.color}` }, h('span', { class: 'gi', 'aria-hidden': 'true' }, g.icon), h('b', {}, g.name), h('span', {}, g.about), h('small', {}, (S.best || {})[g.id] ? `Best: ${S.best[g.id]} points` : 'Not played yet')))));
      wrap.append(h('section', { class: 'card', style: 'margin-top:18px' }, h('h3', { style: 'margin:0 0 6px' }, 'How the levels work'),
        h('p', { style: 'margin:0', class: 'muted' }, 'Levels 1–3: a picture and the meaning. From level 4: only the meaning. From level 8: sometimes you only hear the word. Wrong answers come from the same topic from level 6, and every level makes the games faster with more choices. Words you get wrong come back more often until you know them.')));
    }
    draw(); host.append(wrap);
  }

  /* ---------- one game ---------- */
  async function play(host, ctx, id) {
    styles(); stop(); await words();
    const G = GAMES.find(g => g.id === id); if (!G) { ctx.go('games'); return; }
    const S = ctx.load(); const L = levelOf(S.xp || 0).level; const P = pool(S);
    const st = { score: 0, right: 0, wrong: 0, combo: 0, hearts: 3, n: 0, missed: [], seen: [], done: false };
    if (Snd.music === undefined) Snd.music = false;
    const btn = (label, on, idv, fn) => h('button', { type: 'button', class: 'gbtn' + (on ? ' on' : ''), id: idv, onclick: fn }, label);
    const musicB = btn('♪ Music', Snd.music, 'gMusic', () => { musicOn(!Snd.music); musicB.classList.toggle('on', Snd.music); });
    const voiceB = btn('🔊 Read', Snd.voice, 'gVoice', () => { Snd.voice = !Snd.voice; voiceB.classList.toggle('on', Snd.voice); });
    const stopB = btn('■ Stop', false, 'gStop', () => finish());
    const W = h('div', { class: 'gw', id: 'gameWrap' }, h('div', { class: 'gtop' }, h('h2', {}, `${G.icon} ${G.name}`), musicB, voiceB, stopB));
    const hearts = h('span', { id: 'gHearts' }), pts = h('span', { id: 'gScore' }), lvl = h('span', {}, `Level ${L}`), bar = h('i', { style: 'width:0%' });
    const promptBox = h('div', { class: 'gprompt', id: 'gPrompt', 'aria-live': 'polite' });
    const card = h('div', { class: 'gcard' }, h('div', { class: 'ghud' }, hearts, lvl, pts), promptBox, h('div', { class: 'gbar' }, bar));
    const arena = h('div', { class: 'garena', id: 'gArena' });
    W.append(card, arena); host.innerHTML = ''; host.append(W);
    const hud = () => { hearts.textContent = id === 'memory' || id === 'spell' ? `✔ ${st.right}` : '❤️'.repeat(Math.max(0, st.hearts)) + '🤍'.repeat(Math.max(0, 3 - st.hearts)); pts.textContent = `⭐ ${st.score} points`; };
    hud();
    const T = () => tuning(L);
    function showPrompt(r) {   // what to look for: picture + meaning, meaning only, or the word read aloud
      promptBox.innerHTML = ''; const w = r.t;
      if (r.mode === 'hear') { promptBox.append(h('button', { type: 'button', class: 'hear', id: 'gHear', onclick: () => { const v = Snd.voice; Snd.voice = true; say(w.w, w.audio); Snd.voice = v; } }, '🔊 Listen'), h('span', {}, 'Find the word you hear')); const v = Snd.voice; Snd.voice = true; say(w.w, w.audio); Snd.voice = v; }
      else { if (r.mode === 'pic') promptBox.append(h('span', { class: 'ge', 'aria-hidden': 'true' }, w.emoji)); promptBox.append(h('span', {}, w.def)); if (Snd.voice) speak(w.def); }
    }
    function float(text, x, y) { const f = h('div', { class: 'float', style: `left:${x}px;top:${y}px` }, text); arena.append(f); setTimeout(() => f.remove(), 950); }
    function mark(w, ok) { const m = (S.words = S.words || {}); const r = m[w.id] || [0, 0, 0]; r[0]++; if (ok) r[1]++; r[2] = Date.now(); m[w.id] = r; st.seen.push(w); if (!ok && !st.missed.some(x => x.id === w.id)) st.missed.push(w); }
    function good(w, x, y) { st.combo++; st.right++; const p = 10 + Math.min(10, st.combo - 1) * 2 + Math.floor(L / 2); st.score += p; mark(w, true); sfx('right'); if (x != null) float('+' + p, x, y); hud(); }
    function bad(w, hit) { st.combo = 0; st.wrong++; if (hit !== false) st.hearts--; mark(w, false); sfx('wrong'); arena.classList.remove('shake'); void arena.offsetWidth; arena.classList.add('shake'); hud(); if (st.hearts <= 0) setTimeout(finish, 500); }
    const progress = (n, of) => { bar.style.width = Math.round(n / of * 100) + '%'; };

    function finish() {
      if (st.done) return; st.done = true; stop();
      const before = levelOf(S.xp || 0); const gain = Math.max(5, Math.round(st.score * 0.6) + (st.hearts > 0 ? 10 : 0));
      S.xp = (S.xp || 0) + gain; S.played = (S.played || 0) + 1; S.best = S.best || {}; const newBest = st.score > (S.best[id] || 0); if (newBest) S.best[id] = st.score;
      const k = Object.keys(S.words || {}); if (k.length > 1500) { k.sort((a, b) => S.words[a][2] - S.words[b][2]).slice(0, k.length - 1500).forEach(x => delete S.words[x]); }
      ctx.save(S); const after = levelOf(S.xp);
      sfx(after.level > before.level ? 'level' : 'end'); if (after.level > before.level || newBest) confetti();
      const res = h('div', { class: 'gcard gres', id: 'gResult' },
        h('div', { class: 'big', 'aria-hidden': 'true' }, after.level > before.level ? '🏆' : st.right >= st.wrong * 2 ? '🌟' : '💪'),
        h('h3', {}, after.level > before.level ? `Level up! You are level ${after.level}` : 'Well played!'),
        h('p', { style: 'margin:0;font-weight:700' }, `${st.score} points · ${st.right} right · ${st.wrong} to practise${newBest ? ' · new best!' : ''}`),
        h('p', { style: 'margin:8px 0 2px;font-weight:800;color:#C48A2C', id: 'gXp' }, `+${gain} XP`),
        h('div', { class: 'gxp' }, h('i', { id: 'gXpBar', style: `width:${after.level > before.level ? 0 : Math.round(before.into / before.need * 100)}%` })),
        h('small', { class: 'muted' }, `Level ${after.level}: ${after.into}/${after.need} XP to level ${after.level + 1}`),
        st.missed.length ? h('div', {}, h('p', { style: 'margin:12px 0 0;font-weight:700' }, 'Words to practise – tap to hear them:'), h('div', { class: 'gwl' }, ...st.missed.slice(0, 12).map(w => h('button', { type: 'button', title: w.def, onclick: () => { const v = Snd.voice; Snd.voice = true; say(w.w, w.audio); Snd.voice = v; } }, `${w.emoji} ${w.w}`)))) : null,
        h('div', { style: 'display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:14px' },
          h('button', { type: 'button', class: 'gbtn on', id: 'gAgain', onclick: () => play(host, ctx, id) }, '↻ Play again'), h('a', { class: 'gbtn', href: '#games', id: 'gBack', style: 'text-decoration:none' }, 'All games')));
      arena.innerHTML = ''; arena.append(res); arena.style.background = '#fff'; card.style.display = 'none';
      setTimeout(() => { const b = document.getElementById('gXpBar'); if (b) b.style.width = Math.round(after.into / after.need * 100) + '%'; }, 80);
    }
    const api = { S, P, L, T, st, arena, showPrompt, good, bad, finish, progress, hud, float, sfx, say };
    RUN = ({ racer, balloon, memory, spell, whack })[id](api) || { stop() { } };
    const prevStop = RUN.stop; RUN.stop = () => { prevStop(); st.done = true; };
  }

  /* ===== 1. Word Racer: steer into the lane with the right word ===== */
  function racer(A) {
    const T = A.T(), CW = 360, CH = 520, lanes = 3, lw = 240 / lanes, roadX = 60;
    const cv = h('canvas', { width: CW * 2, height: CH * 2, 'aria-label': 'Road with three lanes' }); const c = cv.getContext('2d'); c.scale(2, 2);
    A.arena.append(cv);
    const ctrl = h('div', { class: 'gctrl' }, h('button', { type: 'button', id: 'gLeft', 'aria-label': 'Left', onpointerdown: e => { e.preventDefault(); move(-1); } }, '◀'), h('button', { type: 'button', id: 'gRight', 'aria-label': 'Right', onpointerdown: e => { e.preventDefault(); move(1); } }, '▶'));
    A.arena.after(ctrl);
    // the whole road and both buttons stay on screen, even on a small phone
    const fit = () => { const wrap = document.getElementById('gameWrap'); if (!wrap) return; const top = cv.getBoundingClientRect().top - wrap.getBoundingClientRect().top;
      const room = window.innerHeight - top - 120, wmax = A.arena.clientWidth - 12; const w = Math.max(200, Math.min(wmax, room * CW / CH)); cv.style.width = w + 'px'; };
    if (window.innerWidth < 760) setTimeout(() => { const wrap = document.getElementById('gameWrap'); if (wrap) wrap.scrollIntoView({ block: 'start' }); }, 120);
    fit(); window.addEventListener('resize', fit);
    let lane = 1, carX = roadX + lw * 1.5, offset = 0, rowY = -60, R = null, n = 0, raf = 0, last = 0, judged = false, stars = [], parts = [];
    const total = T.rounds, speed = () => (110 + 26 * A.L) * Math.min(3.2, T.speed) / 2 + 40;
    function move(d) { lane = Math.max(0, Math.min(lanes - 1, lane + d)); A.sfx('tap'); }
    const key = e => { if (e.key === 'ArrowLeft') { move(-1); e.preventDefault(); } if (e.key === 'ArrowRight') { move(1); e.preventDefault(); } };
    document.addEventListener('keydown', key);
    let sx = null; cv.addEventListener('pointerdown', e => { sx = e.clientX; }); cv.addEventListener('pointerup', e => { if (sx == null) return; const dx = e.clientX - sx; if (Math.abs(dx) > 30) move(dx > 0 ? 1 : -1); else { const r = cv.getBoundingClientRect(); move((e.clientX - r.left) / r.width < 0.5 ? -1 : 1); } sx = null; });
    function next() {
      if (n >= total) { A.finish(); return; }
      const t = Object.assign({}, T, { choices: lanes }); R = round(A.S, A.P, Object.assign(t, { mode: A.T().mode }), new Set(A.st.seen.slice(-6).map(w => w.id))); R.opts = R.opts.slice(0, lanes);
      while (R.opts.length < lanes) R.opts.push(distractors(A.P, R.t, 1, false)[0] || R.t);
      if (!R.opts.includes(R.t)) R.opts[rnd(lanes)] = R.t;
      rowY = -70; judged = false; A.showPrompt(R); A.progress(n, total); n++;
      if (Math.random() < 0.6) stars.push({ lane: rnd(lanes), y: -240 - Math.random() * 120 });
    }
    function rr(x, y, w, hh, r) { c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + hh, r); c.arcTo(x + w, y + hh, x, y + hh, r); c.arcTo(x, y + hh, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
    function draw() {
      c.fillStyle = '#5DBB63'; c.fillRect(0, 0, CW, CH);
      for (let y = -40; y < CH; y += 40) { c.fillStyle = (Math.floor((y + offset) / 40) % 2) ? '#56B25C' : '#62C268'; }
      c.fillStyle = '#4A4F5C'; c.fillRect(roadX, 0, 240, CH);
      for (let y = -40 + (offset % 40); y < CH; y += 40) { c.fillStyle = (Math.round((y - offset) / 40) % 2) ? '#E53935' : '#fff'; c.fillRect(roadX - 10, y, 10, 40); c.fillRect(roadX + 240, y, 10, 40); }
      c.fillStyle = '#fff'; for (let i = 1; i < lanes; i++) for (let y = -60 + (offset % 60); y < CH; y += 60) c.fillRect(roadX + i * lw - 2, y, 4, 34);
      c.fillStyle = '#3E9447'; for (let y = -120 + (offset % 120); y < CH; y += 120) { c.beginPath(); c.arc(24, y + 30, 16, 0, 7); c.arc(CW - 24, y + 90, 18, 0, 7); c.fill(); }
      c.font = '26px serif'; c.textAlign = 'center'; c.textBaseline = 'middle'; stars.forEach(s => c.fillText('⭐', roadX + lw * (s.lane + 0.5), s.y));
      if (R) R.opts.forEach((w, i) => { const x = roadX + lw * i + 6, ww = lw - 12;
        c.fillStyle = 'rgba(0,0,0,.2)'; rr(x, rowY + 4, ww, 46, 12); c.fill(); c.fillStyle = '#FFFFFF'; rr(x, rowY, ww, 46, 12); c.fill();
        c.fillStyle = '#0E2A52'; let fs = 17; c.font = `800 ${fs}px Outfit, sans-serif`; while (c.measureText(w.w).width > ww - 10 && fs > 10) { fs--; c.font = `800 ${fs}px Outfit, sans-serif`; } c.fillText(w.w, x + ww / 2, rowY + 24); });
      const tx = roadX + lw * (lane + 0.5); carX += (tx - carX) * 0.25; const cy = CH - 90;
      c.fillStyle = 'rgba(0,0,0,.25)'; rr(carX - 23, cy + 6, 46, 74, 14); c.fill();
      c.fillStyle = '#E53935'; rr(carX - 24, cy, 48, 74, 16); c.fill(); c.fillStyle = '#fff'; c.fillRect(carX - 4, cy, 8, 74);
      c.fillStyle = '#8FD3FF'; rr(carX - 16, cy + 14, 32, 16, 6); c.fill(); c.fillStyle = '#FFD25A'; c.beginPath(); c.arc(carX, cy + 40, 9, 0, 7); c.fill(); c.fillStyle = '#B71C1C'; c.font = '800 12px Outfit'; c.fillText(String(Math.min(99, A.L)), carX, cy + 41);
      c.fillStyle = '#222'; c.fillRect(carX - 28, cy + 10, 5, 16); c.fillRect(carX + 23, cy + 10, 5, 16); c.fillRect(carX - 28, cy + 50, 5, 16); c.fillRect(carX + 23, cy + 50, 5, 16);
      c.fillStyle = '#FFE082'; c.beginPath(); c.arc(carX - 14, cy + 2, 4, 0, 7); c.arc(carX + 14, cy + 2, 4, 0, 7); c.fill();
      parts = parts.filter(p => (p.t -= 1) > 0); parts.forEach(p => { c.globalAlpha = p.t / 30; c.fillStyle = p.c; c.fillRect(p.x, p.y += p.vy, 4, 4); p.x += p.vx; c.globalAlpha = 1; });
    }
    function tick(ts) {
      if (A.st.done) return; const dt = Math.min(0.05, (ts - (last || ts)) / 1000); last = ts; const v = speed() * dt;
      offset += v; rowY += v; stars.forEach(s => s.y += v);
      const carY = CH - 90;
      stars = stars.filter(s => { if (s.y > carY - 10 && s.y < carY + 60 && s.lane === lane) { A.st.score += 2; A.sfx('star'); A.hud(); return false; } return s.y < CH + 30; });
      if (!judged && R && rowY + 46 >= carY) { judged = true; const w = R.opts[lane]; const r = cv.getBoundingClientRect(), sc = r.width / CW;
        if (w.id === R.t.id) { A.good(R.t, (roadX + lw * (lane + 0.5)) * sc - 20, carY * sc - 40); for (let i = 0; i < 16; i++) parts.push({ x: carX, y: carY, vx: (Math.random() - 0.5) * 4, vy: -Math.random() * 3, t: 30, c: '#FFD25A' }); }
        else { A.bad(R.t); } }
      if (judged && rowY > CH + 10) { if (A.st.done) return; next(); }
      draw(); raf = requestAnimationFrame(tick);
    }
    next(); raf = requestAnimationFrame(tick);
    return { stop() { cancelAnimationFrame(raf); document.removeEventListener('keydown', key); window.removeEventListener('resize', fit); } };
  }

  /* ===== 2. Balloon Pop ===== */
  function balloon(A) {
    const T = A.T(); const sky = h('div', { class: 'gsky' }); A.arena.append(sky);
    const COL = ['#E2463A', '#7A4BD1', '#1F9D5C', '#0149AF', '#D9722A', '#D6336C'];
    let n = 0, raf = 0, last = 0, bs = [], R = null, over = false; const total = T.rounds;
    function next() {
      if (A.st.done) return; if (n >= total) { A.finish(); return; }
      sky.innerHTML = ''; bs = []; over = false; R = round(A.S, A.P, A.T(), new Set(A.st.seen.slice(-6).map(w => w.id))); A.showPrompt(R); A.progress(n, total); n++;
      const W = sky.clientWidth || 560, k = R.opts.length, slot = (W - 20) / k;
      R.opts.forEach((w, i) => { const b = h('button', { type: 'button', class: 'gbal', 'aria-label': w.w, 'data-w': w.id }, h('span', { style: `background:${COL[(i + n) % COL.length]}` }, w.w));
        const o = { el: b, w, x: 10 + slot * i + (slot - 118) / 2 + (Math.random() - 0.5) * 10, y: 330 + Math.random() * 110, v: (38 + 9 * A.L) * (0.8 + Math.random() * 0.4), ph: Math.random() * 6, gone: false };
        b.addEventListener('pointerdown', e => { e.preventDefault(); hit(o); }); sky.append(b); bs.push(o); });
    }
    function hit(o) {
      if (over || o.gone) return; A.sfx('pop'); o.gone = true; o.el.classList.add('popped');
      if (o.w.id === R.t.id) { over = true; A.good(R.t, o.x + 40, Math.max(10, o.y)); setTimeout(next, 650); }
      else { o.el.querySelector('span').style.background = '#8A94A6'; A.bad(R.t); if (A.st.hearts > 0) { over = true; const r = bs.find(b => b.w.id === R.t.id); if (r) r.el.querySelector('span').style.boxShadow = '0 0 0 5px #FFD25A'; setTimeout(next, 1100); } }
    }
    function tick(ts) {
      if (A.st.done) return; const dt = Math.min(0.05, (ts - (last || ts)) / 1000); last = ts;
      bs.forEach(o => { if (o.gone && o.w.id !== (R && R.t.id)) return; o.y -= o.v * dt; o.ph += dt * 2; o.el.style.transform = `translate(${o.x + Math.sin(o.ph) * 8}px, ${o.y}px)`; });
      if (!over && R) { const t = bs.find(o => o.w.id === R.t.id); if (t && t.y < -150) { over = true; A.bad(R.t); setTimeout(next, 500); } }
      raf = requestAnimationFrame(tick);
    }
    next(); raf = requestAnimationFrame(tick);
    return { stop() { cancelAnimationFrame(raf); } };
  }

  /* ===== 3. Memory Match ===== */
  function memory(A) {
    const T = A.T(); const pairs = T.pairs; const used = new Set(); const ws = [];
    while (ws.length < pairs && ws.length < A.P.length) { const w = pickTarget(A.S, A.P, T, used); used.add(w.id); if (!ws.some(x => x.w === w.w || x.emoji === w.emoji)) ws.push(w); if (used.size > A.P.length + 20) break; }
    const showPic = A.L < 10;
    const cards = shuffle(ws.flatMap(w => [{ w, side: 'word' }, { w, side: 'mean' }]));
    const cols = cards.length <= 8 ? 4 : cards.length <= 12 ? 4 : cards.length <= 16 ? 4 : 5;
    const grid = h('div', { class: 'gmem', style: `grid-template-columns:repeat(${cols},1fr)` }); A.arena.append(grid);
    const secs = Math.round(pairs * Math.max(5, 11 - A.L * 0.35)); let left = secs, open = [], found = 0, lock = false;
    const prompt = () => { const p = document.getElementById('gPrompt'); if (p) { p.innerHTML = ''; p.append(h('span', {}, `Match each word with its meaning · ⏱ ${left}s`)); } };
    prompt(); A.progress(0, pairs);
    cards.forEach((cd, i) => { const b = h('button', { type: 'button', class: 'gmc', id: 'gCard' + i, 'aria-label': 'Card ' + (i + 1), 'data-w': cd.w.id, 'data-side': cd.side },
      h('div', { class: 'in' }, h('div', { class: 'fa' }, '★'), h('div', { class: 'fb' }, cd.side === 'word' ? h('b', { style: 'font-size:18px' }, cd.w.w) : [showPic ? h('b', {}, cd.w.emoji) : null, h('small', {}, cd.w.def)])));
      b.addEventListener('click', () => flip(b, cd)); grid.append(b); });
    function flip(b, cd) {
      if (lock || A.st.done || b.classList.contains('open') || b.classList.contains('done')) return;
      A.sfx('flip'); b.classList.add('open'); if (cd.side === 'word') A.say(cd.w.w, cd.w.audio); open.push({ b, cd });
      if (open.length === 2) { lock = true; const [x, y] = open; open = [];
        if (x.cd.w.id === y.cd.w.id && x.cd.side !== y.cd.side) { setTimeout(() => { x.b.classList.add('done'); y.b.classList.add('done'); A.good(x.cd.w); found++; A.progress(found, pairs); lock = false; if (found === pairs) { A.st.score += left * 2; A.hud(); setTimeout(A.finish, 600); } }, 350); }
        else { setTimeout(() => { x.b.classList.remove('open'); y.b.classList.remove('open'); A.st.combo = 0; A.st.wrong++; A.sfx('wrong'); const m = x.cd.w; const r = (A.S.words = A.S.words || {})[m.id] || [0, 0, 0]; r[0]++; A.S.words[m.id] = r; if (!A.st.missed.includes(m)) A.st.missed.push(m); A.hud(); lock = false; }, 900); } }
    }
    const tm = setInterval(() => { if (A.st.done) return clearInterval(tm); left--; prompt(); if (left <= 0) { clearInterval(tm); ws.filter(w => !grid.querySelector(`.gmc.done[data-w="${w.id}"]`)).forEach(w => { if (!A.st.missed.includes(w)) A.st.missed.push(w); }); A.finish(); } }, 1000);
    return { stop() { clearInterval(tm); } };
  }

  /* ===== 4. Spell It ===== */
  function spell(A) {
    const T = A.T(); const total = Math.min(12, 6 + Math.floor(A.L / 4)); let n = 0, w = null, filled = [], tries = 0, pos = 0;
    const box = h('div', { class: 'gsp' }); A.arena.append(box);
    const ABC = 'abcdefghijklmnopqrstuvwxyz';
    function next() {
      if (A.st.done) return; if (n >= total) { A.finish(); return; }
      const used = new Set(A.st.seen.map(x => x.id)); let t = null; for (let k = 0; k < 40; k++) { t = pickTarget(A.S, A.P, T, used); if (/^[a-z' -]+$/i.test(t.w) && t.w.length <= 14) break; }
      w = t; n++; tries = 0; A.progress(n - 1, total);
      const letters = w.w.toLowerCase().split(''); filled = letters.map(ch => (ch === ' ' || ch === '-' || ch === "'") ? ch : null);
      if (T.reveal === 'first') filled[0] = letters[0]; else if (T.reveal) letters.forEach((ch, i) => { if (filled[i] == null && i % 2 === 0) filled[i] = ch; });
      pos = filled.indexOf(null);
      const mode = A.L >= 8 && Math.random() < 0.4 ? 'hear' : A.L <= 3 ? 'pic' : 'def';
      A.showPrompt({ t: w, mode: mode === 'hear' ? 'hear' : mode }); if (mode !== 'hear') { const p = document.getElementById('gPrompt'); p.append(h('button', { type: 'button', class: 'hear', style: 'font-size:14px;padding:6px 10px', onclick: () => { const v = Snd.voice; Snd.voice = true; A.say(w.w, w.audio); Snd.voice = v; } }, '🔊')); }
      const need = letters.filter((ch, i) => filled[i] == null);
      const extra = []; while (extra.length < T.extra) extra.push(ABC[rnd(26)]);
      const tiles = shuffle(need.concat(extra));
      box.innerHTML = '';
      const slots = h('div', { class: 'gslots', id: 'gSlots' }, ...filled.map((ch, i) => h('div', { class: 'gslot' + (letters[i] === ' ' ? ' sp' : '') + (ch != null && letters[i] !== ' ' ? ' ok' : '') + (i === pos ? ' cur' : '') }, ch && ch !== ' ' ? ch : '')));
      const tl = h('div', { class: 'gtiles', id: 'gTiles' }, ...tiles.map(ch => { const b = h('button', { type: 'button', class: 'gtile', 'data-l': ch }, ch); b.addEventListener('click', () => tap(b, ch, letters)); return b; }));
      box.append(slots, tl, h('small', { style: 'color:#556377' }, `Word ${n} of ${total} · ${letters.filter(c => c !== ' ').length} letters`));
    }
    function tap(b, ch, letters) {
      if (A.st.done || pos < 0) return;
      if (ch === letters[pos]) { A.sfx('tap'); b.disabled = true; filled[pos] = ch; const s = document.querySelectorAll('#gSlots .gslot'); s[pos].textContent = ch; s[pos].classList.add('ok'); s[pos].classList.remove('cur');
        pos = filled.indexOf(null); if (pos >= 0) s[pos].classList.add('cur');
        else { if (tries === 0) A.good(w, 140, 80); else { A.st.right++; A.st.score += 4; A.hud(); A.sfx('right'); const m = A.S.words[w.id] = A.S.words[w.id] || [0, 0, 0]; m[0]++; A.st.seen.push(w); if (!A.st.missed.includes(w)) A.st.missed.push(w); } A.say(w.w, w.audio); setTimeout(next, 900); } }
      else { tries++; A.st.combo = 0; A.sfx('wrong'); b.classList.add('shake'); setTimeout(() => b.classList.remove('shake'), 400);
        if (tries >= 3) { A.st.wrong++; const s = document.querySelectorAll('#gSlots .gslot'); letters.forEach((c, i) => { if (filled[i] == null) { s[i].textContent = c; s[i].style.background = '#FDECEC'; } }); const m = (A.S.words = A.S.words || {}); const r = m[w.id] || [0, 0, 0]; r[0]++; m[w.id] = r; A.st.seen.push(w); if (!A.st.missed.includes(w)) A.st.missed.push(w); pos = -1; A.hud(); A.say(w.w, w.audio); setTimeout(next, 1600); } }
    }
    next(); return { stop() { } };
  }

  /* ===== 5. Word Whack ===== */
  function whack(A) {
    const T = A.T(); const holes = []; const field = h('div', { class: 'gholes' }); A.arena.append(field);
    for (let i = 0; i < 9; i++) { const b = h('button', { type: 'button', class: 'ghole', 'aria-label': 'Hole ' + (i + 1) }, h('div', { class: 'gmole' }, h('b', {}, ''))); b.addEventListener('pointerdown', e => { e.preventDefault(); hit(i); }); field.append(b); holes.push({ el: b, w: null }); }
    const total = T.rounds; let n = 0, R = null, timers = [], over = false;
    const clear = () => { timers.forEach(clearTimeout); timers = []; holes.forEach(o => { o.el.classList.remove('up', 'hit', 'bad'); o.w = null; }); };
    function next() {
      if (A.st.done) return; clear(); if (n >= total) { A.finish(); return; }
      R = round(A.S, A.P, A.T(), new Set(A.st.seen.slice(-6).map(w => w.id))); A.showPrompt(R); A.progress(n, total); n++; over = false;
      const spots = shuffle([0, 1, 2, 3, 4, 5, 6, 7, 8]).slice(0, Math.min(R.opts.length, 6)); const up = T.upTime * 1000;
      R.opts.slice(0, spots.length).forEach((w, k) => { const o = holes[spots[k]]; const at = 450 + k * Math.max(220, 520 - A.L * 18) + Math.random() * 200;
        timers.push(setTimeout(() => { if (over) return; o.w = w; o.el.querySelector('b').textContent = w.w; o.el.classList.add('up'); }, at));
        timers.push(setTimeout(() => { if (o.w === w) { o.el.classList.remove('up'); o.w = null; if (!over && w.id === R.t.id) { over = true; A.bad(R.t); timers.push(setTimeout(next, 700)); } } }, at + up + (w.id === R.t.id ? 500 : 0))); });
      if (!R.opts.slice(0, spots.length).includes(R.t)) { const o = holes[spots[0]]; timers.push(setTimeout(() => { o.w = R.t; o.el.querySelector('b').textContent = R.t.w; o.el.classList.add('up'); }, 400)); }
    }
    function hit(i) {
      const o = holes[i]; if (over || !o.w || A.st.done) return; A.sfx('whack');
      if (o.w.id === R.t.id) { over = true; o.el.classList.add('hit'); const r = o.el.getBoundingClientRect(), a = A.arena.getBoundingClientRect(); A.good(R.t, r.left - a.left + 30, r.top - a.top); timers.push(setTimeout(next, 700)); }
      else { o.el.classList.add('bad'); o.w = null; setTimeout(() => o.el.classList.remove('up', 'bad'), 300); A.bad(R.t); if (A.st.hearts <= 0) over = true; }
    }
    next(); return { stop() { clear(); } };
  }

  return { GAMES, hub, play, stop, levelOf, tuning, need, _words: () => WORDS };
})();
