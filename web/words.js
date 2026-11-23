/* Atomic — My word book: words a learner saves from lessons (or adds), with their own notes, and a no-typing practice game.
   Saved words live in the learner's progress (st.words), so they follow the learner to any device.
   Written by the Atomic teaching team. */
(function () {
  'use strict';
  const el = (...a) => window.QE.el(...a);
  const W = {};
  // the book is one progress record per course ("words-stage5"), so it covers every unit and follows the learner to any device
  let CTX = null, stage = () => 0;
  W.init = ctx => { CTX = ctx; stage = ctx.stage; };
  const book = () => (CTX ? CTX.book() : {});
  // saved straight away: a word is saved by one tap, and the page may switch units right after
  const persist = () => { CTX && CTX.save(); };
  W.flush = () => { };
  const key = w => stage() + ':' + String(w).trim().toLowerCase();
  W.has = w => !!book()[key(w)];
  W.count = () => Object.values(book()).filter(x => x.stage === stage()).length;
  W.toLearn = () => Object.values(book()).filter(x => x.stage === stage() && !x.known).length;
  // save a lesson word (from the word bank or the lesson's word list); returns true when it is now saved
  W.toggle = (v, sec) => {
    const b = book(), k = key(v.w);
    if (b[k]) { delete b[k]; persist(); return false; }
    b[k] = { w: v.w, def: v.def || '', audio: v.audio || '', emoji: v.emoji || '', sec: sec || '', unit: sec ? Number(String(sec).split('.')[0]) : 0, stage: stage(), note: '', known: false, custom: false, added: Date.now() };
    persist(); return true;
  };
  W.addOwn = (w, note, emoji, sec) => {
    w = String(w || '').trim().slice(0, 40); if (!w) return false; const b = book(), k = key(w);
    b[k] = Object.assign(b[k] || { def: '', audio: '', sec: sec || '', unit: sec ? Number(String(sec).split('.')[0]) : 0, stage: stage(), known: false, added: Date.now() }, { w, note: String(note || '').slice(0, 300), emoji: emoji || (b[k] && b[k].emoji) || '📝', custom: !(b[k] && b[k].audio) });
    persist(); return true;
  };
  W.list = () => Object.values(book()).filter(x => x.stage === stage()).sort((a, b) => (a.unit - b.unit) || String(a.sec).localeCompare(String(b.sec)) || a.added - b.added);
  W.update = (w, patch) => { const b = book(), k = key(w); if (b[k]) { Object.assign(b[k], patch); persist(); } };
  W.remove = w => { delete book()[key(w)]; persist(); };

  const say = (x, rate) => {
    if (x.audio && window.Primary) return window.Primary.play(x.audio, rate || 0.9);
    try { const ss = window.speechSynthesis; if (!ss) return; ss.cancel(); const u = new SpeechSynthesisUtterance(x.w); u.lang = 'en-GB'; u.rate = rate ? rate * 0.9 : 0.8; const v = ss.getVoices().find(z => /en-GB/i.test(z.lang)); if (v) u.voice = v; ss.speak(u); } catch (e) { }
  };
  W.say = say;

  // the star on a word card: tap to save the word in My word book
  W.star = (v, sec, onChange) => {
    const b = el('button', { type: 'button', class: 'wsave', 'aria-pressed': 'false' });
    const sync = () => { const on = W.has(v.w); b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); b.setAttribute('aria-label', (on ? 'Remove “' : 'Save “') + v.w + (on ? '” from My word book' : '” to My word book')); QE.setTxt(b, on ? '⭐ Saved' : '☆ Save'); };
    b.onclick = e => { e.stopPropagation(); const on = W.toggle(v, sec); sync(); if (window.toastWord) window.toastWord(on ? `⭐ “${v.w}” is in My word book` : `“${v.w}” removed`); onChange && onChange(on); };
    sync(); return b;
  };

  const PICS = ['📝', '⭐', '🌱', '🌸', '🐞', '💧', '🔥', '🧲', '🌍', '☀️', '🎵', '🍎', '🦴', '🧪', '🐟', '❄️'];
  // a small form to add your own word (older children or a parent can type it); a picture can be chosen with one tap
  W.addForm = (sec, onAdd) => {
    let pic = '📝';
    const wi = el('input', { type: 'text', maxlength: 40, placeholder: 'A word, e.g. pollen', 'aria-label': 'Word', autocomplete: 'off' });
    const ni = el('input', { type: 'text', maxlength: 300, placeholder: 'My note (what it means, how to remember it)', 'aria-label': 'My note', autocomplete: 'off' });
    const pics = el('div', { class: 'wpics', role: 'radiogroup', 'aria-label': 'Choose a picture' }, ...PICS.map(p => { const b = el('button', { type: 'button', class: 'wpic' + (p === pic ? ' on' : ''), 'aria-label': 'Picture ' + p, onclick: () => { pic = p; pics.querySelectorAll('.wpic').forEach(x => x.classList.toggle('on', x === b)); } }, p); return b; }));
    const msg = el('span', { class: 'muted', role: 'status' });
    const add = el('button', { type: 'button', class: 'btn primary', onclick: () => { if (!W.addOwn(wi.value, ni.value, pic, sec)) { msg.textContent = 'Write a word first.'; wi.focus(); return; } QE.setTxt(msg, `⭐ “${wi.value.trim()}” added`); wi.value = ''; ni.value = ''; onAdd && onAdd(); } }, '+ Add to My word book');
    return el('div', { class: 'card waddform' }, el('b', { class: 'lex' }, '✏️ Add my own word'), el('div', { class: 'wrow' }, wi, ni), pics, el('div', { class: 'btnrow' }, add, msg));
  };

  // practice without typing: hear the word (or see its picture and meaning) and tap the right card
  W.game = (host, words, pool, onEnd) => {
    const rnd = a => a.slice().sort(() => Math.random() - 0.5);
    const qs = rnd(words).slice(0, 10); let i = 0, score = 0;
    const others = w => rnd(pool.filter(x => x.w.toLowerCase() !== w.w.toLowerCase())).slice(0, 2);
    const next = () => {
      host.innerHTML = '';
      if (i >= qs.length) {
        host.append(el('div', { class: 'wgame done' }, el('div', { class: 'big' }, score === qs.length ? '🏆' : score >= qs.length / 2 ? '🌟' : '💪'),
          el('h3', {}, `You got ${score} out of ${qs.length}!`), el('p', { class: 'muted' }, score === qs.length ? 'Amazing! You know all these words.' : 'Practise again to remember them even better.'),
          el('div', { class: 'btnrow' }, el('button', { type: 'button', class: 'btn primary big', onclick: () => { i = 0; score = 0; next(); } }, '🔁 Play again'), el('button', { type: 'button', class: 'btn big', onclick: () => onEnd && onEnd() }, 'Back to my words'))));
        return;
      }
      const w = qs[i], opts = rnd([w].concat(others(w))); const byPic = !w.audio && !(window.speechSynthesis);
      const fb = el('p', { class: 'wfb', role: 'status' });
      const cards = opts.map(o => el('button', { type: 'button', class: 'opt pcard', onclick: () => {
        if (host.querySelector('.pcard.right')) return;
        const good = o.w === w.w; if (good) score++; const card = cards[opts.indexOf(o)];
        card.classList.add(good ? 'right' : 'wrong'); if (!good) cards[opts.indexOf(w)].classList.add('right');
        QE.setTxt(fb, good ? '✓ Yes! That\'s “' + w.w + '”.' : '✗ Not quite. It was “' + w.w + '”.'); fb.className = 'wfb ' + (good ? 'ok' : 'no');
        if (good && !w.custom) W.update(w.w, { right: (w.right || 0) + 1, known: (w.right || 0) + 1 >= 3 ? true : w.known });
        setTimeout(() => { i++; next(); }, 1500);
      } }, el('span', { class: 'pe' }, o.emoji || '🔤'), el('span', { class: 'pt' }, o.w)));
      const prompt = byPic || !w.audio && !w.def ? el('p', { class: 'qp' }, w.note ? `Which word means: “${w.note}”?` : `Find the word “${w.w}”.`)
        : el('div', {}, el('p', { class: 'qp' }, '🔊 Listen. Which word do you hear?'), w.def ? el('p', { class: 'muted' }, 'Clue: ' + w.def) : null,
          el('button', { type: 'button', class: 'btn small listen', onclick: () => say(w) }, '🔊 Listen again'));
      host.append(el('div', { class: 'wgame' }, el('div', { class: 'wgtop' }, el('b', {}, `Word ${i + 1} of ${qs.length}`), el('span', { class: 'muted' }, `⭐ ${score}`)), prompt, el('div', { class: 'opts pics n3' }, ...cards), fb));
      if (!byPic) setTimeout(() => say(w), 250);
    };
    next();
  };
  window.Words = W;
})();
