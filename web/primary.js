/* Camday Primary (Stage 6): listening, read-aloud checks, the word bank and the experiment room.
   Written by the Camday teaching team. */
(function () {
  'use strict';
  const el = (...a) => window.QE.el(...a);
  const A = {};
  /* ---------------- audio ---------------- */
  let playing = null;
  function play(src, rate = 1) {
    try { if (playing) { playing.pause(); } const a = new Audio(src); a.playbackRate = rate; a.preservesPitch = true; playing = a; return a.play().catch(() => { }); } catch (e) { return Promise.resolve(); }
  }
  A.play = play;
  A.audioBar = function (src, slow) {
    const b1 = el('button', { type: 'button', class: 'btn small listen', onclick: () => play(src, 1) }, '🔊 Listen');
    const b2 = el('button', { type: 'button', class: 'btn small ghost', onclick: () => play(src, 0.75) }, '🐢 Slowly');
    return el('div', { class: 'audiobar', role: 'group', 'aria-label': 'Listen' }, b1, b2, el('span', { class: 'muted' }, 'Listen as many times as you like.'));
  };

  /* ---------------- matching what was heard ---------------- */
  const norm = s => String(s || '').toLowerCase().replace(/iz(e|ed|ing|ation)/g, 'is$1').replace(/[^a-z ]+/g, ' ').replace(/\s+/g, ' ').trim();
  function lev(a, b) { const m = a.length, n = b.length; if (!m) return n; if (!n) return m; const d = Array.from({ length: m + 1 }, (_, i) => [i]); for (let j = 1; j <= n; j++) d[0][j] = j;
    for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++) d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); return d[m][n]; }
  // a word counts as said when every part of it is in what the browser heard (small slips allowed for long words)
  function heardOk(target, alts) {
    const t = norm(target).split(' ');
    return alts.some(alt => { const a = norm(alt); if (!a) return false; if ((' ' + a + ' ').includes(' ' + t.join(' ') + ' ')) return true;
      const toks = a.split(' '); return t.every(w => toks.some(x => x === w || x === w + 's' || w === x + 's' || (w.length >= 5 && lev(x, w) <= Math.floor(w.length / 5)))); });
  }
  A.heardOk = heardOk;
  const SR = () => window.SpeechRecognition || window.webkitSpeechRecognition;

  /* ---------------- “Say the word” ---------------- */
  A.say = function (q, host, o, rec) {
    rec.heard = rec.heard || []; const MAX = 3;
    const head = el('div', { class: 'qhead' }, o.nested ? null : el('code', {}, q.id), el('span', { class: 'tag t-say' }, '🎤 Say the word'), el('span', { class: 'tag d-' + q.diff }, window.QE.DIFF[q.diff] || q.diff), el('span', { class: 'tag' }, q.obj));
    host.append(head, el('p', { class: 'qp' }, q.prompt));
    const card = el('div', { class: 'saycard' }, el('span', { class: 'sayemo', 'aria-hidden': 'true' }, q.emoji || '🔤'), el('b', { class: 'sayword' }, q.word), q.meaning ? el('span', { class: 'muted' }, q.meaning) : null);
    const hear = el('div', { class: 'audiobar' }, el('button', { type: 'button', class: 'btn small listen', onclick: () => play(q.audio, 1) }, '🔊 Hear it'), el('button', { type: 'button', class: 'btn small ghost', onclick: () => play(q.audio, 0.75) }, '🐢 Slowly'));
    const mic = el('button', { type: 'button', class: 'micbtn', 'aria-label': 'Tap and say the word' }, el('span', { class: 'mi', 'aria-hidden': 'true' }, '🎤'), el('span', { class: 'ml' }, 'Tap, then say the word'));
    const tries = el('div', { class: 'saytries', 'aria-hidden': 'true' });
    const fb = el('div', { class: 'fb', 'aria-live': 'polite' }); const typed = el('div');
    const note = el('p', { class: 'muted small' }, 'Your browser listens to check your word. Camday does not record or keep your voice.');
    host.append(card, hear, el('div', { class: 'sayrow' }, mic, tries), typed, fb, note);
    const drawTries = () => { tries.innerHTML = ''; for (let i = 0; i < MAX; i++) tries.append(el('i', { class: i < rec.tries ? (rec.ok && i === rec.tries - 1 ? 'ok' : 'bad') : '' })); };
    const finish = () => { mic.disabled = true; mic.classList.remove('on'); o.save(rec); o.onDone && o.onDone(rec); };
    function result(ok, heard) {
      rec.tries++; if (heard != null) rec.heard.push(heard); rec.resp = { ok, tries: rec.tries };
      o.onCheck && o.onCheck({ ok, frac: ok ? 1 : 0, fb: [], answered: true }, rec);
      fb.innerHTML = '';
      if (ok) { rec.ok = true; rec.done = true; rec.score = rec.tries === 1 ? 1 : rec.tries === 2 ? 0.5 : 0.25; fb.className = 'fb ok'; fb.append(el('b', {}, rec.tries === 1 ? '✓ Perfect! You said it clearly.' : '✓ Well done – you said it!')); drawTries(); finish(); return; }
      rec.wrong = (rec.wrong || 0) + 1; rec.everWrong = true; drawTries();
      if (rec.tries >= MAX) { rec.done = true; rec.ok = false; rec.assisted = true; rec.score = 0; fb.className = 'fb guide';
        fb.append(el('b', {}, 'Let\'s listen together.'), el('p', {}, `Listen slowly to “${q.word}” and say it with the teacher. You can carry on now, and practise this word again later.`)); play(q.audio, 0.75); finish(); return; }
      fb.className = 'fb bad'; fb.append(el('b', {}, heard ? `I heard “${heard}”.` : 'Not quite.'), el('p', {}, `Listen again, then say “${q.word}”. ${MAX - rec.tries} ${MAX - rec.tries === 1 ? 'try' : 'tries'} left.`)); play(q.audio, 0.85); o.save(rec);
    }
    // no microphone or no speech recognition in this browser: listen and type the word instead
    function typeMode(why) {
      rec.mode = 'typed'; mic.remove(); typed.innerHTML = '';
      const inp = el('input', { type: 'text', class: 'numin', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', 'aria-label': 'Type the word you hear' });
      const chk = el('button', { type: 'button', class: 'btn primary small' }, 'Check');
      chk.onclick = () => { const v = inp.value.trim(); if (!v) { inp.focus(); return; } result(norm(v) === norm(q.word) || (q.word.length >= 6 && lev(norm(v), norm(q.word)) <= 1), null); if (rec.done) { inp.disabled = true; chk.disabled = true; } else inp.select(); };
      inp.addEventListener('keydown', e => { if (e.key === 'Enter') chk.click(); });
      typed.append(el('div', { class: 'banner info' }, el('b', {}, why + ' '), 'Listen to the word, then type it.'), el('div', { class: 'numrow' }, inp, chk));
    }
    drawTries();
    if (rec.done) { mic.disabled = true; fb.className = rec.ok ? 'fb ok' : 'fb guide'; QE.setTxt(fb, rec.ok ? '✓ You said this word.' : 'You listened to this word with the teacher. Try saying it again any time.'); return rec; }
    const S = SR();
    if (!S) { typeMode('This browser cannot listen to speech (try Chrome, Edge or Safari).'); return rec; }
    let r = null, busy = false;
    mic.onclick = () => {
      if (busy) { try { r.stop(); } catch (e) { } return; }
      try { r = new S(); } catch (e) { typeMode('Speech checking is not available here.'); return; }
      r.lang = 'en-GB'; r.interimResults = false; r.maxAlternatives = 5; r.continuous = false;
      let got = false; busy = true; mic.classList.add('on'); mic.querySelector('.ml').textContent = 'Listening… say the word';
      r.onresult = e => { got = true; const alts = Array.from(e.results[0] || []).map(x => x.transcript); const ok = heardOk(q.word, alts); result(ok, alts[0] || ''); };
      r.onerror = e => { busy = false; mic.classList.remove('on'); mic.querySelector('.ml').textContent = 'Tap, then say the word';
        if (['not-allowed', 'service-not-allowed', 'audio-capture'].includes(e.error)) typeMode(e.error === 'audio-capture' ? 'No microphone was found.' : 'The microphone is switched off for this site.');
        else if (e.error === 'no-speech') { fb.className = 'fb warn'; fb.textContent = 'I didn\'t hear anything. Tap the microphone and say the word clearly.'; }
        else if (e.error === 'network') typeMode('Speech checking needs the internet.'); };
      r.onend = () => { busy = false; if (!rec.done) { mic.classList.remove('on'); mic.querySelector('.ml').textContent = 'Tap, then say the word'; } if (!got && !rec.done && fb.textContent === '') { fb.className = 'fb warn'; fb.textContent = 'I didn\'t catch that. Tap the microphone and try again.'; } };
      try { r.start(); } catch (e) { busy = false; typeMode('Speech checking could not start.'); }
    };
    return rec;
  };

  /* ---------------- word bank ---------------- */
  A.wordBank = function (s) {
    if (!s.vocab || !s.vocab.length) return null;
    return el('section', { class: 'card wordbank', id: 'wordBank' }, el('div', { class: 'wbhead' }, el('b', { class: 'lex' }, `📚 Words for ${s.id}`), el('span', { class: 'muted' }, 'Tap a card to hear the word. Tap ☆ Save to keep a word in My word book.')),
      el('div', { class: 'wbgrid' }, ...s.vocab.map(v => el('div', { class: 'wcard' }, el('button', { type: 'button', class: 'wplay', onclick: () => play(v.audio, 0.9) },
        el('span', { class: 'we', 'aria-hidden': 'true' }, v.emoji || '🔤'), el('b', {}, v.w), el('small', {}, v.def), el('span', { class: 'wp', 'aria-hidden': 'true' }, '🔊')), window.Words ? window.Words.star(v, s.id) : null))));
  };

  /* ---------------- experiment room ---------------- */
  // virtual labs: each draws an interactive experiment and calls done() when the learner has finished it
  const LABS = {};
  const svgEl = (tag, attrs) => { const e = document.createElementNS('http://www.w3.org/2000/svg', tag); for (const k in attrs) e.setAttribute(k, attrs[k]); return e; };
  const heartPath = 'M60 104 C20 78 8 48 22 30 C34 14 54 18 60 34 C66 18 86 14 98 30 C112 48 100 78 60 104 Z';
  let actx = null; const tick = () => { try { actx = actx || new (window.AudioContext || window.webkitAudioContext)(); const o = actx.createOscillator(), g = actx.createGain(); o.frequency.value = 160; g.gain.value = 0.15; o.connect(g); g.connect(actx.destination); o.start(); g.gain.exponentialRampToValueAtTime(0.001, actx.currentTime + 0.12); o.stop(actx.currentTime + 0.13); } catch (e) { } };

  // 1.1 pulse rate: watch the heart, tap each beat for 15 seconds, work out beats per minute
  LABS.pulse = function (box, L, state, save, done) {
    state.rows = state.rows || {}; const acts = L.acts; let timer = null;
    const svg = svgEl('svg', { viewBox: '0 0 120 120', width: 150, height: 150, class: 'labheart' }); const hp = svgEl('path', { d: heartPath, fill: '#E0444B', stroke: '#0E1B3D', 'stroke-width': 4 }); svg.append(hp);
    const pick = el('div', { class: 'btnrow' }); const stage = el('div', { class: 'labstage' }); const out = el('div'); const tbl = el('div');
    box.append(el('p', {}, L.intro), pick, el('div', { class: 'labrow' }, el('div', { class: 'labvis' }, svg, el('span', { class: 'muted', id: 'labAct' }, 'Choose an activity')), stage), out, tbl);
    let cur = null, beatT = null;
    const beatAt = bpm => { clearInterval(beatT); beatT = setInterval(() => { hp.animate([{ transform: 'scale(1)' }, { transform: 'scale(1.16)' }, { transform: 'scale(1)' }], { duration: 260, easing: 'ease-out' }); }, 60000 / bpm); };
    hp.style.transformOrigin = '60px 60px'; hp.style.transformBox = 'fill-box';
    const drawTable = () => { tbl.innerHTML = '';
      const t = el('table', { class: 'grid data labtable' }, el('tr', {}, el('th', {}, 'Activity'), el('th', {}, 'Beats in 15 s'), el('th', {}, 'Pulse rate (beats per minute)')));
      acts.forEach(a => { const r = state.rows[a.k]; t.append(el('tr', {}, el('td', {}, a.t), el('td', {}, r ? String(r.n) : '–'), el('td', {}, r && r.bpm ? String(r.bpm) : '–'))); });
      tbl.append(el('div', { class: 'tablewrap' }, t));
      if (acts.every(a => state.rows[a.k] && state.rows[a.k].bpm)) { const mx = Math.max(...acts.map(a => state.rows[a.k].bpm));
        tbl.append(el('div', { class: 'labbars', 'aria-label': 'Bar chart of your results' }, ...acts.map(a => el('div', { class: 'lb' }, el('i', { style: `height:${Math.round(state.rows[a.k].bpm / mx * 140)}px` }), el('b', {}, String(state.rows[a.k].bpm)), el('small', {}, a.t)))));
        done(); }
    };
    acts.forEach(a => pick.append(el('button', { type: 'button', class: 'chip' + (state.rows[a.k] ? ' on' : ''), onclick: () => start(a) }, (state.rows[a.k] ? '✓ ' : '') + a.t)));
    function start(a) {
      cur = a; clearInterval(timer); beatAt(a.bpm); document.getElementById('labAct').textContent = a.t + ' – watch the heart';
      stage.innerHTML = ''; out.innerHTML = ''; let n = 0, left = 15, on = false;
      const cnt = el('b', { class: 'labcount' }, '0'), clock = el('span', { class: 'labclock' }, '15 s');
      const tap = el('button', { type: 'button', class: 'btn gold big', disabled: true }, '💓 Beat!');
      const go = el('button', { type: 'button', class: 'btn primary' }, '▶ Start counting (15 seconds)');
      tap.onclick = () => { if (!on) return; n++; cnt.textContent = String(n); tick(); };
      go.onclick = () => { on = true; go.disabled = true; tap.disabled = false; tap.focus(); timer = setInterval(() => { left--; clock.textContent = left + ' s'; if (left <= 0) { clearInterval(timer); on = false; tap.disabled = true; ask(a, n); } }, 1000); };
      stage.append(el('p', {}, 'Press start, then tap “Beat!” every time the heart beats.'), go, el('div', { class: 'labtap' }, tap, el('span', {}, 'beats counted: ', cnt), clock));
    }
    function ask(a, n) {
      const want = Math.round(a.bpm / 4); const fair = Math.abs(n - want) <= 3;
      out.innerHTML = ''; const inp = el('input', { type: 'text', inputmode: 'numeric', class: 'numin s', 'aria-label': 'Beats per minute' }); const msg = el('p', { class: 'muted' });
      const ok = el('button', { type: 'button', class: 'btn primary small' }, 'Record');
      ok.onclick = () => { const v = Number(inp.value); if (!v) { inp.focus(); return; } if (Math.abs(v - n * 4) > 1) { msg.className = 'fb bad'; msg.textContent = `Not quite: you counted ${n} beats in 15 seconds. A minute is 4 × 15 seconds, so multiply ${n} by 4.`; return; }
        state.rows[a.k] = { n, bpm: v }; save(); out.innerHTML = ''; out.append(el('div', { class: 'banner ok' }, `✓ Recorded: ${a.t} – ${v} beats per minute.`)); pick.querySelectorAll('.chip').forEach((c, i) => { if (state.rows[acts[i].k]) { c.classList.add('on'); QE.setTxt(c, '✓ ' + acts[i].t); } }); drawTable(); };
      out.append(el('div', { class: 'card', style: 'padding:14px 18px' }, el('p', {}, fair ? `You counted ${n} beats in 15 seconds – good counting!` : `You counted ${n} beats in 15 seconds. (The heart really beat about ${want} times. Counting carefully matters – you can try again.)`),
        el('p', {}, el('b', {}, 'How many beats in one minute? '), 'Multiply by 4.'), el('div', { class: 'numrow' }, inp, el('span', {}, 'beats per minute'), ok), msg));
    }
    drawTable();
    return () => { clearInterval(timer); clearInterval(beatT); };
  };

  // 1.2 the bottle model of the lungs: pull the sheet down and up and watch the balloon
  LABS.lungs = function (box, L, state, save, done) {
    const svg = svgEl('svg', { viewBox: '0 0 300 300', width: 300, height: 300, class: 'labsvg' });
    svg.innerHTML = '<path d="M130 20 L170 20 L172 56 C240 70 240 90 240 120 L240 230 L60 230 L60 120 C60 90 60 70 128 56 Z" fill="rgba(220,232,250,.6)" stroke="#0E1B3D" stroke-width="4"/><rect x="146" y="6" width="8" height="110" fill="#F3BF69" stroke="#0E1B3D" stroke-width="2"/>';
    const bal = svgEl('ellipse', { cx: 150, cy: 140, rx: 26, ry: 30, fill: '#F7A3B2', stroke: '#0E1B3D', 'stroke-width': 3 }); const sheet = svgEl('path', { d: 'M60 230 Q150 230 240 230', fill: 'none', stroke: '#C0504D', 'stroke-width': 8 });
    const air = svgEl('text', { x: 190, y: 20, 'font-size': 18, 'font-weight': 700, fill: '#0149AF' }); svg.append(bal, sheet, air);
    const range = el('input', { type: 'range', min: 0, max: 100, value: 0, 'aria-label': 'Pull the rubber sheet down', class: 'labrange' });
    const seen = state.seen || { down: false, up: false };
    const set = () => { const f = range.value / 100; sheet.setAttribute('d', `M60 230 Q150 ${230 + 80 * f} 240 230`); bal.setAttribute('rx', (26 + 30 * f).toFixed(1)); bal.setAttribute('ry', (30 + 30 * f).toFixed(1));
      QE.setTxt(air, f > 0.6 ? '↓ air in' : f < 0.2 && seen.down ? '↑ air out' : ''); if (f > 0.8) seen.down = true; if (seen.down && f < 0.1) seen.up = true; state.seen = seen; save(); if (seen.down && seen.up) done(); };
    range.addEventListener('input', set);
    box.append(el('p', {}, L.intro), el('div', { class: 'labrow' }, el('div', { class: 'labvis' }, svg), el('div', { class: 'labstage' }, el('p', {}, el('b', {}, 'Pull the rubber sheet: '), 'drag the slider down to pull, then back up to let go.'), range, el('p', { class: 'muted' }, 'The bottle is the chest, the balloon is a lung, the straw is the windpipe and the rubber sheet is the diaphragm.'))));
    set();
  };

  // 1.3 growth data: plot a height chart is done in the questions; this lab measures a family's heights on a ruler
  LABS.growth = function (box, L, state, save, done) {
    const people = L.people; state.read = state.read || {};
    const wrap = el('div', { class: 'labruler' });
    const H = 260, top = 200;   // cm range 0..top
    const ruler = el('div', { class: 'rl' }, ...Array.from({ length: 11 }, (_, i) => el('span', { style: `bottom:${i * 20 / top * H}px` }, String(i * 20))));
    wrap.append(ruler, ...people.map(p => el('div', { class: 'rp' }, el('i', { style: `height:${p.h / top * H}px;background:${p.c}` }), el('small', {}, p.n))));
    const rows = el('div', { class: 'labinputs' }); const msg = el('p', { class: 'muted' });
    people.forEach((p, i) => { const inp = el('input', { type: 'text', inputmode: 'numeric', class: 'numin s', value: state.read[i] || '', 'aria-label': `Height of ${p.n} in cm` });
      inp.addEventListener('change', () => { state.read[i] = inp.value; save(); check(); }); rows.append(el('label', {}, p.n + ': ', inp, ' cm')); });
    function check() { const ok = people.every((p, i) => Math.abs(Number(state.read[i]) - p.h) <= 5); msg.className = ok ? 'fb ok' : 'muted'; QE.setTxt(msg, ok ? '✓ Good reading! Now answer the questions.' : 'Read each height from the ruler (to the nearest 5 cm).'); if (ok) done(); }
    box.append(el('p', {}, L.intro), wrap, rows, msg); check();
  };

  // 1.4 glitter germs: wash hands in different ways and count the glitter left
  LABS.germs = function (box, L, state, save, done) {
    state.rows = state.rows || {}; const M = L.methods;
    const svg = svgEl('svg', { viewBox: '0 0 200 220', width: 200, height: 220, class: 'labsvg' }); svg.innerHTML = '<path d="M50 200 C50 120 40 70 60 50 C70 20 90 30 92 60 L96 20 C100 0 120 0 120 20 L120 60 C124 30 146 30 146 60 L146 90 C150 70 170 74 168 96 C164 150 160 200 120 214 C90 220 60 214 50 200Z" fill="#F2C7A5" stroke="#0E1B3D" stroke-width="4"/>';
    const dots = []; for (let i = 0; i < 60; i++) { const d = svgEl('circle', { cx: 62 + (i * 37) % 96, cy: 70 + (i * 53) % 130, r: 3, fill: ['#F3BF69', '#E86A8E', '#2F6FD6'][i % 3] }); dots.push(d); svg.append(d); }
    const btns = el('div', { class: 'btnrow' }); const out = el('div'); const tbl = el('div');
    const draw = () => { tbl.innerHTML = ''; const t = el('table', { class: 'grid data labtable' }, el('tr', {}, el('th', {}, 'How I washed'), el('th', {}, 'Glitter pieces left')));
      M.forEach(m => t.append(el('tr', {}, el('td', {}, m.t), el('td', {}, state.rows[m.k] != null ? String(state.rows[m.k]) : '–')))); tbl.append(el('div', { class: 'tablewrap' }, t)); if (M.every(m => state.rows[m.k] != null)) done(); };
    M.forEach(m => btns.append(el('button', { type: 'button', class: 'chip', onclick: () => wash(m) }, m.t)));
    function wash(m) {
      out.innerHTML = ''; dots.forEach(d => d.setAttribute('opacity', 1)); const keep = Math.round(60 * m.left); let i = 60;
      const tmr = setInterval(() => { i -= 3; dots.forEach((d, k) => d.setAttribute('opacity', k < Math.max(keep, i) ? 1 : 0)); if (i <= keep) { clearInterval(tmr); count(m, keep * 4); } }, 60);
    }
    function count(m, n) { const inp = el('input', { type: 'text', inputmode: 'numeric', class: 'numin s', 'aria-label': 'Glitter left' }); const ok = el('button', { type: 'button', class: 'btn primary small' }, 'Record'); const msg = el('p', { class: 'muted' });
      ok.onclick = () => { if (Number(inp.value) !== n) { msg.className = 'fb bad'; msg.textContent = 'Read the counter again carefully.'; return; } state.rows[m.k] = n; save(); out.innerHTML = ''; out.append(el('div', { class: 'banner ok' }, `✓ Recorded: ${m.t} – ${n} pieces left.`)); draw(); };
      out.append(el('div', { class: 'card', style: 'padding:14px 18px' }, el('p', {}, `The magnifier counted `, el('b', { class: 'labcount' }, String(n)), ' pieces of glitter still on the hand.'), el('div', { class: 'numrow' }, el('span', {}, 'Type the number:'), inp, ok), msg)); }
    box.append(el('p', {}, L.intro), el('div', { class: 'labrow' }, el('div', { class: 'labvis' }, svg), el('div', { class: 'labstage' }, el('p', {}, el('b', {}, 'Change one thing: '), 'how you wash. Keep the same amount of glitter each time.'), btns, out)), tbl);
    draw();
  };
  // a fair test: choose each condition, watch the instrument, read the scale and record the result
  // L = {intro, change, measure, unit, max, step, tol, instr, conds:[{k, t, emoji, val}]}
  LABS.test = function (box, L, state, save, done) {
    state.rows = state.rows || {}; const C = L.conds, max = L.max, step = L.step, tol = L.tol != null ? L.tol : step / 2;
    const H = 220, scale = el('div', { class: 'labscale' }), fill = el('i'), ticks = [];
    for (let v = 0; v <= max + 1e-9; v += step) ticks.push(el('span', { style: `bottom:${v / max * H}px` }, String(+v.toFixed(2))));
    scale.append(el('div', { class: 'ls-tube' }, fill), ...ticks);
    const big = el('div', { class: 'labbig', 'aria-hidden': 'true' }, L.instr || '🔬'); const cap = el('span', { class: 'muted' }, 'Choose a test');
    const btns = el('div', { class: 'btnrow' }); const out = el('div'); const tbl = el('div');
    const draw = () => { tbl.innerHTML = '';
      const t = el('table', { class: 'grid data labtable' }, el('tr', {}, el('th', {}, L.change), el('th', {}, `${L.measure} (${L.unit})`)));
      C.forEach(c => t.append(el('tr', {}, el('td', { class: 'emo' }, (c.emoji ? c.emoji + ' ' : '') + c.t), el('td', {}, state.rows[c.k] != null ? String(state.rows[c.k]) : '–'))));
      tbl.append(el('div', { class: 'tablewrap' }, t));
      if (C.every(c => state.rows[c.k] != null)) { const mx = Math.max(...C.map(c => Number(state.rows[c.k]))) || 1;
        tbl.append(el('div', { class: 'labbars', 'aria-label': 'Bar chart of your results' }, ...C.map(c => el('div', { class: 'lb' }, el('i', { style: `height:${Math.round(Number(state.rows[c.k]) / mx * 140)}px` }), el('b', {}, String(state.rows[c.k])), el('small', {}, c.t)))));
        done(); }
      btns.querySelectorAll('.chip').forEach((b, i) => { const on = state.rows[C[i].k] != null; b.classList.toggle('on', on); QE.setTxt(b, (on ? '✓ ' : '') + C[i].t); });
    };
    C.forEach(c => btns.append(el('button', { type: 'button', class: 'chip', onclick: () => run(c) }, c.t)));
    let tmr = null;
    function run(c) {
      clearInterval(tmr); out.innerHTML = ''; big.textContent = c.emoji || L.instr || '🔬'; cap.textContent = c.t; fill.style.height = '0px';
      let f = 0; tmr = setInterval(() => { f = Math.min(1, f + 0.04); fill.style.height = (c.val / max * H * f) + 'px'; if (f >= 1) { clearInterval(tmr); ask(c); } }, 40);
    }
    function ask(c) {
      if (L.choose) {   // young learners: tap the reading instead of typing it
        const msg = el('p', { class: 'muted' }); const vals = [c.val, c.val + step, Math.max(0, c.val - step), c.val + 2 * step].filter((v, i, a) => a.indexOf(v) === i && v <= max + 1e-9).slice(0, 3).sort((a, b) => a - b);
        const row = el('div', { class: 'btnrow labchoose' }, ...vals.map(v => el('button', { type: 'button', class: 'btn big', onclick: () => {
          if (Math.abs(v - c.val) > tol + 1e-9) { msg.className = 'fb bad'; msg.textContent = `Not quite. Look at the top of the coloured bar. Which line is it next to?`; return; }
          state.rows[c.k] = c.val; save(); out.innerHTML = ''; out.append(el('div', { class: 'banner ok' }, `✓ Well done! ${c.t}: ${c.val} ${L.unit}.`)); draw(); } }, `${+v.toFixed(2)} ${v === 1 && /s$/.test(L.unit) ? L.unit.slice(0, -1) : L.unit}`)));
        out.append(el('div', { class: 'card', style: 'padding:14px 18px' }, el('p', {}, el('b', {}, 'Look at the scale. '), `Tap the ${L.measure.toLowerCase()}.`), row, msg)); return;
      }
      const inp = el('input', { type: 'text', inputmode: 'decimal', class: 'numin s', 'aria-label': `${L.measure} for ${c.t}` }); const msg = el('p', { class: 'muted' });
      const ok = el('button', { type: 'button', class: 'btn primary small' }, 'Record');
      ok.onclick = () => { const v = Number(String(inp.value).replace(',', '.')); if (!inp.value || !isFinite(v)) { inp.focus(); return; }
        if (Math.abs(v - c.val) > tol + 1e-9) { msg.className = 'fb bad'; msg.textContent = `Not quite. Look where the top of the coloured bar is against the scale. Each line is ${step} ${L.unit}.`; return; }
        state.rows[c.k] = c.val; save(); out.innerHTML = ''; out.append(el('div', { class: 'banner ok' }, `✓ Recorded: ${c.t} – ${c.val} ${L.unit}.`)); draw(); };
      inp.addEventListener('keydown', e => { if (e.key === 'Enter') ok.click(); });
      out.append(el('div', { class: 'card', style: 'padding:14px 18px' }, el('p', {}, el('b', {}, 'Read the scale. '), `What is the ${L.measure.toLowerCase()}?`), el('div', { class: 'numrow' }, inp, el('span', {}, L.unit), ok), msg));
    }
    box.append(el('p', {}, L.intro), el('div', { class: 'labrow' }, el('div', { class: 'labvis' }, big, cap), el('div', { class: 'labvis' }, scale), el('div', { class: 'labstage' }, el('p', {}, el('b', {}, 'Change one thing: '), L.change.toLowerCase() + '. Keep everything else the same.'), btns, out)), tbl);
    draw(); return () => clearInterval(tmr);
  };

  // sort it: put each card in the right group. L = {intro, groups:[..], items:[{t, emoji, g, why}]}
  LABS.sort = function (box, L, state, save, done) {
    state.put = state.put || {}; const G = L.groups, I = L.items; let sel = null;
    const pool = el('div', { class: 'sortpool' }); const bins = el('div', { class: 'sortbins' }); const msg = el('p', { class: 'muted' });
    const card = (it, i) => el('button', { type: 'button', class: 'sortcard' + (sel === i ? ' on' : ''), 'aria-pressed': String(sel === i), onclick: () => { sel = sel === i ? null : i; draw(); } }, el('span', { class: 'emo', 'aria-hidden': 'true' }, it.emoji || ''), ' ', it.t);
    function draw() {
      pool.innerHTML = ''; bins.innerHTML = '';
      I.forEach((it, i) => { if (state.put[i] == null) pool.append(card(it, i)); });
      G.forEach((g, gi) => { const b = el('div', { class: 'sortbin' + (sel != null ? ' ready' : ''), role: 'button', tabindex: 0, 'aria-label': 'Put in ' + g, onclick: () => drop(gi), onkeydown: e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); drop(gi); } } }, el('b', {}, g));
        I.forEach((it, i) => { if (state.put[i] === gi) b.append(el('span', { class: 'sortcard placed' }, el('span', { class: 'emo', 'aria-hidden': 'true' }, it.emoji || ''), ' ', it.t)); }); bins.append(b); });
      const n = Object.keys(state.put).length;
      if (n === I.length) { msg.className = 'fb ok'; QE.setTxt(msg, '✓ All sorted correctly!'); done(); }
      else if (!msg.classList.contains('bad')) { msg.className = 'muted'; msg.textContent = sel == null ? `Tap a card, then tap its group. ${I.length - n} left.` : 'Now tap the group it belongs in.'; }
    }
    function drop(gi) {
      if (sel == null) return; const it = I[sel];
      if (it.g !== gi) { msg.className = 'fb bad'; msg.textContent = `Not “${G[gi]}”. ${it.why || 'Think again.'}`; sel = null; draw(); return; }
      state.put[sel] = gi; sel = null; save(); msg.className = 'muted'; draw();
    }
    box.append(el('p', {}, L.intro), pool, bins, msg); draw();
  };
  A.LABS = LABS;

  // the room: a virtual lab with its questions, and an experiment to try at home
  A.labRoom = function (s, st, ctx) {
    const L = s.lab; st.labs = st.labs || {}; const LS = st.labs[s.id] = st.labs[s.id] || { v: {}, h: { vals: {} } };
    const root = el('div', { class: 'labroom' });
    const tab = ctx.tab || 'v';
    const tabs = el('div', { class: 'btnrow', role: 'tablist' }, ...[['v', `🧪 Virtual lab${LS.v.done ? ' ✓' : ''}`], ['h', `🏠 Try it at home${LS.h.done ? ' ✓' : ''}`]].map(([k, t]) => el('button', { type: 'button', role: 'tab', class: 'chip' + (k === tab ? ' on' : ''), 'aria-selected': String(k === tab), onclick: () => ctx.setTab(k) }, t)));
    root.append(tabs);
    const qBlock = (qs, after) => { const wrap = el('div', { class: 'labqs' }); const recs = qs.map(q => st.items[q.id] = st.items[q.id] || { tries: 0 });
      qs.forEach((q, i) => { const c = el('section', { class: 'card qcard' }); wrap.append(c); window.QE.practice(q, c, { rec: recs[i], seed: st.id, save: () => ctx.persist(), onDone: () => { recs[i].done = true; ctx.persist(); if (recs.every(r => r.done)) after(); } }); });
      if (recs.every(r => r.done)) setTimeout(after, 0); return wrap; };
    if (tab === 'v') {
      const V = L.v; const card = el('section', { class: 'card labcard' }, el('span', { class: 'eyebrow' }, 'VIRTUAL LAB'), el('h2', { style: 'margin:2px 0 8px' }, V.title));
      root.append(card); const qs = el('div'); const status = el('div');
      const finished = () => { if (!LS.v.done) { LS.v.done = true; ctx.persist(); ctx.toast && ctx.toast('Experiment complete – well done, scientist!'); } status.innerHTML = ''; status.append(el('div', { class: 'banner ok' }, el('b', {}, '✓ Virtual lab complete. '), 'Now try the experiment at home.', el('button', { type: 'button', class: 'btn small', onclick: () => ctx.setTab('h') }, 'Try it at home →'))); };
      const labDone = () => { if (!qs.childNodes.length) qs.append(el('h3', { style: 'margin:16px 0 6px' }, 'What did you find out?'), qBlock(V.qs || [], finished)); };
      const f = LABS[V.kind]; LS.v.state = LS.v.state || {};
      const stop = f ? f(card, V, LS.v.state, () => ctx.persist(), labDone) : null; ctx.onLeave && ctx.onLeave(stop);
      root.append(qs, status);
    } else {
      const Hm = L.h; LS.h.vals = LS.h.vals || {};
      const card = el('section', { class: 'card labcard' }, el('span', { class: 'eyebrow' }, 'TRY IT AT HOME'), el('h2', { style: 'margin:2px 0 8px' }, Hm.title), el('p', {}, Hm.intro));
      card.append(el('div', { class: 'labhome' }, el('div', {}, el('b', {}, 'You will need'), el('ul', {}, ...Hm.need.map(x => el('li', {}, x)))),
        el('div', { class: 'safety' }, el('b', {}, '⚠️ Stay safe'), el('ul', {}, ...Hm.safety.map(x => el('li', {}, x))))));
      card.append(el('b', {}, 'What to do'), el('ol', { class: 'labsteps' }, ...Hm.steps.map(x => el('li', {}, x))));
      const R = Hm.record; const msg = el('p', { class: 'muted' });
      const t = el('table', { class: 'grid data labtable' }, el('tr', {}, ...R.head.map(h => el('th', {}, h))));
      R.rows.forEach((row, i) => { const tr = el('tr', {}, el('td', {}, row[0])); row.slice(1).forEach((cell, j) => { const key = i + '_' + j;
        if (cell.choices) {   // tap a choice (for children who cannot type yet)
          const cs = el('div', { class: 'labchips', role: 'radiogroup', 'aria-label': `${row[0]} – ${R.head[j + 1]}` }, ...cell.choices.map(ch => { const b = el('button', { type: 'button', class: 'chip' + (LS.h.vals[key] === ch ? ' on' : ''), 'aria-pressed': String(LS.h.vals[key] === ch), onclick: () => { LS.h.vals[key] = ch; ctx.persist(); cs.querySelectorAll('.chip').forEach(x => { const on = x === b; x.classList.toggle('on', on); x.setAttribute('aria-pressed', String(on)); }); check(); } }, ch); return b; }));
          tr.append(el('td', {}, cs)); return; }
        const inp = el('input', { type: 'text', inputmode: 'decimal', class: 'numin s', value: LS.h.vals[key] || '', 'aria-label': `${row[0]} – ${R.head[j + 1]}` });
        inp.addEventListener('change', () => { LS.h.vals[key] = inp.value.trim(); ctx.persist(); check(); }); tr.append(el('td', {}, inp)); }); t.append(tr); });
      card.append(el('b', {}, 'Record your results'), el('div', { class: 'tablewrap' }, t), msg);
      const qs = el('div');
      function check() {
        const bad = []; R.rows.forEach((row, i) => row.slice(1).forEach((cell, j) => { if (cell.choices) { if (!cell.choices.includes(LS.h.vals[i + '_' + j])) bad.push(`${row[0]} (${R.head[j + 1]})`); return; } const v = Number(String(LS.h.vals[i + '_' + j] || '').replace(',', '.')); if (!isFinite(v) || LS.h.vals[i + '_' + j] === undefined || LS.h.vals[i + '_' + j] === '' || v < cell.min || v > cell.max) bad.push(`${row[0]} (${R.head[j + 1]})`); }));
        if (bad.length) { msg.className = 'muted'; msg.textContent = `Fill in every row with your own result. Check: ${bad.slice(0, 3).join(', ')}${bad.length > 3 ? '…' : ''}. ${R.hint || ''}`; return; }
        msg.className = 'fb ok'; QE.setTxt(msg, '✓ Results recorded. Now answer the questions about your experiment.');
        if (!qs.childNodes.length) qs.append(qBlock(Hm.qs || [], () => { if (!LS.h.done) { LS.h.done = true; ctx.persist(); ctx.toast && ctx.toast('Home experiment complete!'); } }));
      }
      root.append(card, qs); check();
    }
    return root;
  };
  window.Primary = A;
})();
