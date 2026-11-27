/* Camday — Science Stage 7. Views and routing (v3: student accounts, guest mode, server marking).
   Visual language: Camday Cambridge Science Design System v3. */
(function () {
  const { el, esc } = QE;
  let C, st;
  // The leaderboard is switched off (the user asked to remove it). Set to true to bring back the page, nav link, dashboard card and settings switch.
  const LEADERBOARD = false;
  const UI = { tab: {}, idx: {}, seek: null, drill: null, staffTab: 'marking', side: 'chapters', testIdx: 0, flags: {}, testOn: false, cc: true, speed: 1 };
  const $main = () => document.getElementById('main');
  const R = s => s.replace('.', '-');
  const secFromRoute = r => r.split('-').slice(1).join('.');
  const fmt = t => { t = Math.max(0, Math.round(t)); return `${Math.floor(t / 60)}:${String(t % 60).padStart(2, '0')}`; };
  const fullT = (s, t) => fmt(s.video.offset + t);
  const go = (r, opts) => { if (opts) Object.assign(UI, opts); if (location.hash.slice(1) === r) render(); else location.hash = r; };
  const svgI = (name, size = 16, color) => AtomicIcons.ic(name, { size, filled: /^player-/.test(name), color: color && color !== 'currentColor' && color !== '#1C2A3A' ? color : null });
  const I = { play: 'player-play', pause: 'player-pause', check: 'check', sheet: 'file-text', lock: 'lock', flag: 'flag', bulb: 'bulb', full: 'maximize' };
  const FLAME = AtomicIcons.html('flame', { filled: true, size: 18, color: '#E8590C' });
  const STAR = AtomicIcons.html('star', { filled: true, size: 16, color: '#E0A800' });
  const unitIcon = n => { const name = AtomicIcons.unit(Core.STAGE, n); if (!name) return el('span', { class: 'ic mic', 'aria-hidden': 'true' }, String(n)); const sp = el('span', { class: 'ic tic c' + (n % 5), 'aria-hidden': 'true' }); sp.append(AtomicIcons.ic(name)); return sp; };
  const STRAND = { 1: 'Enquiry', 2: 'Enquiry', 3: 'Biology', 4: 'Biology', 5: 'Biology', 6: 'Chemistry', 7: 'Chemistry', 8: 'Chemistry', 9: 'Chemistry', 10: 'Physics', 11: 'Physics', 12: 'Physics', 13: 'Earth and Space', 14: 'Earth and Space' };

  /* ---------- small UI helpers ---------- */
  function modal(title, body, buttons) {
    const bg = el('div', { class: 'modal-bg', role: 'dialog', 'aria-modal': 'true', 'aria-label': title });
    const close = () => bg.remove();
    const box = el('div', { class: 'modal' }, el('h3', {}, title), typeof body === 'string' ? el('p', {}, body) : body,
      el('div', { class: 'btnrow end' }, ...buttons.map(b => el('button', { class: 'btn small ' + (b.cls || ''), type: 'button', onclick: async ev => { const btn = ev.currentTarget; btn.disabled = true; let keep; try { keep = b.on && await b.on(); } finally { btn.disabled = false; } if (keep !== true) close(); } }, b.t))));
    bg.append(box); document.body.append(bg); const f = box.querySelector('button.primary') || box.querySelector('button'); f && f.focus();
    bg.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
    return close;
  }
  /* light / dark switch (new design only): the choice is remembered on this device */
  function modeBtn() {
    const T = window.AtomicTheme; if (!T || T.name !== 'oak') return '';
    const b = el('button', { class: 'modebtn', type: 'button', id: 'modeBtn' });
    const draw = () => { const d = T.mode === 'dark'; QE.setTxt(b, d ? '☀️' : '🌙'); b.title = d ? 'Switch to light mode' : 'Switch to dark mode'; b.setAttribute('aria-label', b.title); b.setAttribute('aria-pressed', String(d)); };
    b.onclick = () => { T.setMode(T.mode === 'dark' ? 'light' : 'dark'); draw(); };
    draw(); return b;
  }
  // the same switch as a row in the phone menu (the header has no room for it there)
  function navMode() {
    const T = window.AtomicTheme; if (!T || T.name !== 'oak') return null;
    const b = el('button', { class: 'navmode', type: 'button' });
    const draw = () => { const d = T.mode === 'dark'; b.replaceChildren(AtomicIcons.ic(d ? 'sun' : 'moon'), d ? 'Light mode' : 'Dark mode'); };
    b.onclick = () => { T.setMode(T.mode === 'dark' ? 'light' : 'dark'); draw(); };
    draw(); return b;
  }
  // A4 worksheets and certificates shrink to fit a phone screen (printing still uses the real size)
  const fitA4 = () => document.documentElement.style.setProperty('--a4z', String(Math.min(1, (document.documentElement.clientWidth - 24) / 794).toFixed(3)));
  fitA4(); addEventListener('resize', fitA4);
  /* XP guide: where the learner is, how XP is earned and what levels are for */
  function xpGuide() {
    const li = Core.levelInfo(), left = li.to - li.xp, FL = TestRules.FINAL_LEVEL;
    const row = (xp, what, note) => el('div', { class: 'xpg-row' }, el('b', {}, xp), el('span', {}, what, note ? el('small', {}, note) : null));
    const ladder = [li.level + 1, li.level + 2, li.level + 3].filter(L => L <= Math.max(FL, li.level + 1)).map(L => el('span', { class: 'xpg-step' + (L === FL ? ' goal' : '') }, el('b', {}, 'Level ' + L), el('small', {}, TestRules.xpForLevel(L).toLocaleString('en-GB') + ' XP')));
    modal('How XP and levels work', el('div', { class: 'xpg', id: 'xpGuide' },
      el('div', { class: 'xpg-now' }, el('span', { class: 'lvx-badge big', 'aria-hidden': 'true' }, el('i', {}, String(li.level))),
        el('span', { class: 'xpg-nowtxt' }, el('b', {}, `Level ${li.level} · ${li.xp.toLocaleString('en-GB')} XP`),
          el('span', { class: 'lvbar wide' }, el('i', { style: `width:${li.pct}%` })),
          el('small', {}, `${li.pct}% of the way to level ${li.level + 1} · ${left.toLocaleString('en-GB')} XP to go`))),
      el('h4', {}, 'How to earn XP'),
      row('+20', 'Watch a lesson video to the end'),
      row('+10', 'Answer a pause question right first time', '+5 if you need another try'),
      row('+12', 'Get a practice question right first time', '+7 on the second try, +2 for finishing it after that'),
      row('+5', 'Print a worksheet'),
      row('+100', 'Pass a Unit Test'),
      el('p', { class: 'muted', style: 'margin:6px 0 0' }, 'Each question earns XP once. Question Bank practice counts too, unless you have already done that question.'),
      el('h4', {}, 'What levels are for'),
      el('p', { style: 'margin:0' }, li.level >= FL ? `You have reached level ${FL}: the end-of-year exams are open to you.` : `Reach level ${FL} to open the end-of-year exams. Each level needs a little more XP than the one before.`),
      el('div', { class: 'xpg-ladder' }, ...ladder)),
      [{ t: 'See my progress', on: () => { go('profile'); } }, { t: 'Got it', cls: 'primary' }]);
  }
  let lastXp = null; // kept for older callers
  function toast(t) { const n = document.querySelectorAll('.toast').length; const x = el('div', { class: 'toast', role: 'status', style: `--n:${n}` }, t); document.body.append(x); setTimeout(() => x.remove(), 2700); }
  function xpTick() { }
  let xpAcc = 0, xpT = null;
  window.addEventListener('atomic:xp', e => {
    const d = e.detail; xpAcc += d.gain; clearTimeout(xpT);
    xpT = setTimeout(() => { if (xpAcc > 0) { const t = el('div', { class: 'xptoast', role: 'status' }, `+${xpAcc} XP`); document.body.append(t); setTimeout(() => t.remove(), 1600); } xpAcc = 0;
      const p = document.getElementById('levelPill'); if (p) { const li = Core.levelInfo(); p.querySelector('b').textContent = 'Level ' + li.level; p.querySelector('.lvx-badge i').textContent = li.level; p.querySelector('.lvx-pct').textContent = li.pct + '%'; p.querySelector('.lvbar i').style.width = li.pct + '%'; } }, 500);
    if (d.levelUp) setTimeout(() => { confetti(); const t = el('div', { class: 'lvtoast', role: 'status' }, el('b', {}, `⭐ Level ${d.level}!`), el('span', {}, d.level >= TestRules.FINAL_LEVEL ? 'The end-of-year exams are open to you.' : `End-of-year exams open at level ${TestRules.FINAL_LEVEL}.`)); document.body.append(t); setTimeout(() => t.remove(), 4200); }, 600);
  });
  function initialChip(size) { return el('span', { class: 'ini', style: `width:${size}px;height:${size}px;font-size:${Math.round(size * .42)}px` }, ((st && st.alias) || '?').slice(0, 1).toUpperCase()); }
  const isGuest = () => !!Core.S.guest;
  function startGuest(n) { n = typeof n === 'number' ? n : 3; if (!Core.S.me && !Core.cur()) toast('Welcome! You are learning as a guest.'); go(`v-${n}-1`); }
  function guestWall(title) {
    return el('section', { class: 'card lockcard', id: 'guestWall' }, el('h2', {}, '✨ ' + title), el('p', {}, 'Create a free account to unlock every topic and take the Unit Test. What you have done as a guest comes with you.'),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn gold', href: '#signup' }, 'Sign up free'), el('a', { class: 'btn ghost', href: '#signin' }, 'I already have an account')));
  }
  function burst(host) {
    const b = el('div', { class: 'burst', 'aria-hidden': 'true' }); const cols = ['#F3BF69', '#0149AF', '#1E8E4E', '#2F6FD6', '#8DB3EC'];
    for (let i = 0; i < 16; i++) { const w = el('span', { style: `transform:rotate(${i * 22.5}deg)` }); w.append(el('i', { style: `background:${cols[i % 5]};left:${(i % 3) * 14}px;animation-delay:${(i % 4) * .04}s` })); b.append(w); }
    host.append(b); setTimeout(() => b.remove(), 1100);
  }
  function confetti() { const c = el('div', { class: 'confetti', 'aria-hidden': 'true' }); const cols = ['#F3BF69', '#0149AF', '#1E8E4E', '#F08A4B', '#8E6CC9']; for (let i = 0; i < 60; i++) c.append(el('i', { style: `left:${Math.random() * 100}%;background:${cols[i % 5]};animation-delay:${Math.random() * .8}s` })); document.body.append(c); setTimeout(() => c.remove(), 3800); }
  const onCheck = (card, q, rec) => (g) => { if (g.ok) burst(card); else { card.classList.remove('shake'); void card.offsetWidth; card.classList.add('shake'); } setTimeout(xpTick, 50);
    if (q && st) Backend.track('answer', { learner: st.id, unit: Core.UNIT, q: q.id, ok: !!g.ok, try: (rec && rec.tries) || 1 }); };

  /* ---------- shell ---------- */
  function navLink(href, label, on) { return el('a', { href: '#' + href, class: on ? 'on' : '', 'aria-current': on ? 'page' : null }, label); }
  function shell(opts) {
    const r = location.hash.slice(1) || 'home'; const app = document.getElementById('app'); app.innerHTML = '';
    const me = Core.S.me;
    const area = r.startsWith('v-') || r.startsWith('vw-') || r.startsWith('sp-') || r.startsWith('ex-') || r.startsWith('ws-') || r.startsWith('lab-') || /^u-\d+$/.test(r) || /^stage-\d+$/.test(r) || /^checkout-\d+$/.test(r) || r === 'map' || r === 'level' ? 'course' : r === 'bank' || r === 'topic' || r === 'drill' ? 'bank' : r === 'test' || r === 'tests' || r === 'result' || r === 'remedial' || r === 'final' || /^f(x|res)-\d+$/.test(r) ? 'test' : r === 'profile' || r === 'cert' ? 'profile' : r === 'board' ? 'board' : r === 'home' ? 'home' : r === 'challenge' || /^ch[lxpr]-/.test(r) ? 'challenge' : r === 'games' || /^game-/.test(r) ? 'games' : r;
    const right = el('span', { class: 'topright' });
    let nav;
    if (st) {
      const sk = Core.streak(st);
      const s = el('a', { class: 'pill streak', href: isGuest() ? '#home' : '#profile', title: `${sk}-day streak`, 'aria-label': `${sk}-day streak` }); s.innerHTML = FLAME; s.append(String(sk));
      const li = Core.levelInfo();
      const lv = el('button', { class: 'lvx', type: 'button', id: 'levelPill', title: 'How XP and levels work', 'aria-label': `Level ${li.level}, ${li.pct}% of the way to level ${li.level + 1}. How XP works`, onclick: xpGuide },
        el('span', { class: 'lvx-badge', 'aria-hidden': 'true' }, el('i', {}, String(li.level))),
        el('span', { class: 'lvx-mid' }, el('b', {}, 'Level ' + li.level), el('span', { class: 'lvbar' }, el('i', { style: `width:${li.pct}%` }))),
        el('span', { class: 'lvx-pct' }, li.pct + '%'));
      right.append(modeBtn());
      if (isGuest()) right.append(s, lv, el('a', { class: 'btn small ghost', href: '#signin', id: 'signInLink' }, 'Log in'), el('a', { class: 'btn small gold', href: '#signup', id: 'signUpLink' }, 'Sign up free'));
      else {
        const menu = el('div', { class: 'usermenu', hidden: true, id: 'userMenu' }, el('b', {}, st.name), el('a', { href: '#profile' }, 'My progress'), el('a', { href: '#settings', id: 'settingsLink' }, 'Settings'),
          ['marker', 'admin'].includes(me.profile.role) ? el('a', { href: '#staff' }, 'Staff') : null,
          me.profile.role === 'admin' ? el('a', { href: '#admin', id: 'adminLink' }, 'Admin console') : null,
          el('button', { type: 'button', id: 'signOut', onclick: async () => { Core.flush(); await Backend.signOut(); await Core.boot(C); st = null; go('home'); } }, 'Sign out'));
        const av = el('button', { class: 'namechip', type: 'button', id: 'whoBtn', 'aria-label': 'Account menu', 'aria-haspopup': 'true', onclick: ev => { ev.stopPropagation(); menu.hidden = !menu.hidden; } }, initialChip(34), el('span', {}, st.alias));
        document.addEventListener('click', () => { menu.hidden = true; }, { once: true });
        right.append(s, lv, bell(), el('span', { class: 'userwrap' }, av, menu));
      }
      nav = [navLink('home', 'Dashboard', area === 'home'), navLink('u-' + Core.UNO, 'Course', area === 'course'), navLink('bank', 'Question Bank', area === 'bank'), navLink('tests', 'Tests & exams', area === 'test'), LEADERBOARD ? navLink('board', 'Leaderboard', area === 'board') : null].filter(Boolean);
      if (Core.IS_PRIMARY) { nav.splice(2, 0, navLink('words', '📒 My words', area === 'words')); nav[3].textContent = 'Questions'; nav[4].textContent = 'Tests'; }
    } else if (me) {
      right.append(modeBtn(), bell(), el('button', { class: 'btn small', type: 'button', id: 'signOut', onclick: async () => { await Backend.signOut(); await Core.boot(C); go('home'); } }, 'Sign out'));
      nav = [navLink('home', 'Home', area === 'home'), navLink('help', 'Help', area === 'help')];
      if (['marker', 'admin'].includes(me.profile.role)) nav.push(navLink('staff', 'Staff', area === 'staff'));
      if (me.profile.role === 'admin') nav.push(navLink('admin', 'Admin', area === 'admin'));
    } else {
      right.append(modeBtn(), el('a', { class: 'btn small ghost', href: '#signin', id: 'signInLink' }, 'Log in'), el('a', { class: 'btn small gold', href: '#signup', id: 'signUpLink' }, 'Sign up free'));
      nav = [navLink('home', 'Home', area === 'home'), navLink('pricing', Core.BILLING_OFF ? 'Free test' : 'Pricing', area === 'pricing'), navLink('help', 'Help', area === 'help'), navLink('verify', 'Verify a certificate', area === 'verify')];
    }
    if (st || !me) nav.splice(1, 0, stagesMenu());
    if (!st && !me || st && isGuest()) nav.push(el('a', { class: 'navlogin', href: '#signin' }, 'Log in'));
    nav.push(navMode());
    const header = el('header', { class: 'top' + (st && isGuest() || !st && !me ? ' guest' : '') }, el('div', { class: 'top-in' },
      el('button', { class: 'menu-btn', type: 'button', 'aria-label': 'Menu', onclick: () => document.body.classList.toggle('menu-open') }, '☰'),
      el('a', { href: '#home', class: 'brand' }, el('img', { src: 'camday_logo.svg', width: 162, height: 38, alt: 'Camday — home' })),
      el('nav', { class: 'mainnav', 'aria-label': 'Main' }, ...nav), right));
    const ENV = (window.ATOMIC_CONFIG || {}).env;
    const demoBar = Backend.mode === 'demo' ? el('div', { class: 'demobar', role: 'note' }, 'Preview mode: accounts, payments and marking are simulated and stored only in this browser.')
      : ENV === 'test' ? el('div', { class: 'demobar test', role: 'note', id: 'envBar' }, 'TEST environment – for trying the course only. Data may be reset at any time.') : null;
    const sub = el('div', { id: 'sub' });
    const side = el('aside', { class: 'toc', 'aria-label': 'Course contents' }); if (st && opts.toc) side.append(toc());
    const main = el('div', { class: 'content', id: 'main', tabindex: '-1' });
    const wrap = el('div', { class: 'wrap' + (opts.toc && st ? '' : ' nosidebar'), id: 'wrap' }, el('div', { class: 'layout' }, side, main));
    const fcol = (h, links) => el('nav', { class: 'fcol', 'aria-label': h }, el('h3', {}, h), el('ul', {}, ...links.map(([l, href]) => el('li', {}, el('a', { href }, l)))));
    const foot = el('footer', { class: 'foot' }, el('div', { class: 'in' },
      el('div', { class: 'fcols footnav' },
        fcol('Learners', [['All courses', '#courses'], [Core.BILLING_OFF ? 'Free test' : 'Pricing', '#pricing'], ['Verify a certificate', '#verify'], [me ? 'My progress' : 'Log in', me ? '#profile' : '#signin']]),
        fcol('Camday', [['Home', '#home'], ['News & roadmap', '#news'], ['Help & contact', '#help']]),
        fcol('Legal', [['Terms & conditions', '#terms'], ['Privacy policy', '#privacy'], ['Privacy for learners', '#privacy-kids'], ['Cookie policy', '#cookies']]),
        el('div', { class: 'fbrand' }, el('img', { src: 'camday_logo.svg', alt: 'Camday — Daily practice for Cambridge learners' }), el('span', { class: 'tag2' }, 'Daily practice for Cambridge learners'))),
      el('div', { class: 'fbase' },
        el('p', { class: 'muted disclaimer' }, 'Camday courses and lesson videos are produced by Atomic Education and aligned to Cambridge curriculum frameworks (Primary Science 0097, Lower Secondary Science 0893, Primary Mathematics 0096, Lower Secondary Mathematics 0862). Checkpoint-format papers are written by Camday – they are not Cambridge papers. Camday is not affiliated with or endorsed by Cambridge University Press & Assessment.'),
        el('p', { class: 'fcopy' }, el('b', {}, `© Atomic Education ${new Date().getFullYear()}`), el('br'), 'Written by the Camday teaching team · Camday is made by Atomic Education'))));
    app.append(...[demoBar, header, sub, wrap, foot].filter(Boolean));
    lastXp = null;
  }
  function bell() {
    const n = (Core.S.notes || []).filter(x => !x.read_at).length;
    const b = el('button', { class: 'bell', type: 'button', id: 'bellBtn', 'aria-label': `Notifications${n ? `, ${n} unread` : ''}`, onclick: () => openNotes() }, '🔔', n ? el('span', { class: 'dot' }, String(n)) : null);
    return b;
  }
  async function openNotes() {
    const list = await Backend.notifications(); Core.S.notes = list;
    modal('Notifications', list.length ? el('ul', { class: 'notes' }, ...list.map(x => el('li', { class: x.read_at ? '' : 'unread' }, el('b', {}, x.title), x.body ? el('span', {}, x.body) : null, el('small', { class: 'muted' }, new Date(x.created_at).toLocaleString('en-GB'))))) : el('p', { class: 'muted' }, 'Nothing new.'),
      [{ t: 'Close', cls: 'primary', on: async () => { await Backend.markNotificationsRead(); Core.S.notes.forEach(x => x.read_at = x.read_at || 1); const d = document.querySelector('#bellBtn .dot'); if (d) d.remove(); } }]);
  }
  function tocBtn() { return el('button', { class: 'btn small ghost tocbtn', type: 'button', onclick: () => document.body.classList.toggle('toc-open') }, '☰ Course contents'); }
  // sidebar: every unit can be opened in place to show all its sections (no need to go back to the course page)
  const hrs = sec => { const m = Math.ceil(sec / 60); return m < 60 ? `${m} min` : `${Math.floor(m / 60)} h${m % 60 ? ' ' + (m % 60) + ' min' : ''}`; };
  const estH = min => `${Math.ceil(min / 60)} h`;   // estimates are always rounded up to whole hours
  function unitSecNav(n, content, state, route) {
    const here = n === Core.UNO; const ss = here ? st : Object.assign({ video: {}, items: {}, ws: [] }, JSON.parse(JSON.stringify(state || {})));
    const sn = el('div', { class: 'secnav' });
    content.sections.forEach(s => {
      const lock = here ? Core.secLock(st, s) : Core.seqLock(content, ss, s, Core.unitId(n)), done = Core.secDone(ss, s), vd = Core.videoDone(ss, s), rl = Core.reqLeft(ss, s).length;
      sn.append(el('div', { class: 'sh' + (lock ? ' locked' : '') }, lock ? '🔒 ' : done ? '✓ ' : '', `${s.id} ${s.title}`));
      const link = (r, label, ok) => el('a', { href: '#' + r, class: route === r ? 'on' : '' }, el('span', { class: 'st' + (ok ? ' ok' : '') }, ok ? '✓' : ''), label);
      if (lock && lock.paywall) sn.append(el('div', { class: 'why' }, lock.reason));
      else if (lock) sn.append(el('div', { class: 'why' }, lock.reason), link('ws-' + R(s.id), 'Worksheet', (ss.ws || []).includes(s.id)));
      else sn.append(...[link('v-' + R(s.id), s.lesson ? 'Read' : 'Watch', vd), link('ex-' + R(s.id), `Practise · ${s.req.length - rl}/${s.req.length} Core`, rl === 0), s.lab ? link('lab-' + R(s.id), '🧪 Experiment', !!((ss.labs || {})[s.id] || {}).v && !!(((ss.labs || {})[s.id] || {}).v || {}).done) : null, secGameWords(s).length ? link('gm-' + R(s.id), '🎮 Word games', !!((ss.games || {})[s.id])) : null, link('ws-' + R(s.id), 'Worksheet', (ss.ws || []).includes(s.id))].filter(Boolean));
    });
    const passed = !!(st.results || {})[Core.unitId(n)];
    sn.append(el('a', { href: here ? '#test' : '#u-' + n, class: route === 'test' && here ? 'on' : '', onclick: here ? null : e => { e.preventDefault(); Core.switchUnit(n).then(() => go('test')); } }, el('span', { class: 'st' + (passed ? ' ok' : '') }, passed ? '✓' : '★'), `Unit Test ${n} · 45 min`));
    sn.append(el('a', { href: here ? '#map' : '#u-' + n, onclick: here ? null : e => { e.preventDefault(); Core.switchUnit(n).then(() => go('map')); } }, el('span', { class: 'st' }, '◎'), 'Concept map'));
    return sn;
  }
  // sidebar: a search box, the current course, and only the unit being studied (other units are picked from "Change unit")
  function tocSearch() {
    const box = el('div', { class: 'card tsearch' });
    const inp = el('input', { type: 'search', id: 'tocSearch', placeholder: 'Search lessons, units, words…', autocomplete: 'off', 'aria-label': 'Search this course' });
    const out = el('div', { class: 'tsres', role: 'listbox' });
    const norm = t => String(t || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    const items = () => {
      const L = [];
      Core.INDEX.units.forEach(u => { if (Core.unitStatus(st, u.n) === 'soon') return;
        L.push({ k: 'unit', t: `${u.n}. ${u.t}`, sub: 'Unit', n: u.n, to: 'u-' + u.n });
        (u.sections || []).forEach(x => L.push({ k: 'lesson', t: `${x.id} ${x.t}`, sub: `Unit ${u.n} · ${u.t}`, n: u.n, to: 'v-' + R(x.id) })); });
      if (C) C.sections.forEach(x => (x.vocab || []).forEach(v => L.push({ k: 'word', t: `${v.emoji || '🔤'} ${v.w}`, sub: `Word · ${x.id} ${x.title}`, n: Core.UNO, to: 'v-' + R(x.id) })));
      return L;
    };
    const open = it => { inp.value = ''; out.innerHTML = ''; document.body.classList.remove('toc-open');
      if (it.n === Core.UNO) go(it.to); else Core.switchUnit(it.n).then(() => go(it.to)).catch(() => toast('Could not open that unit.')); };
    inp.addEventListener('input', () => {
      out.innerHTML = ''; const q = norm(inp.value.trim()); if (q.length < 2) return;
      const hits = items().filter(it => norm(it.t + ' ' + it.sub).includes(q)).slice(0, 8);
      if (!hits.length) { out.append(el('p', { class: 'muted tsnone' }, 'Nothing found. Try another word.')); return; }
      hits.forEach(it => out.append(el('button', { type: 'button', class: 'tsit', role: 'option', onclick: () => open(it) }, el('span', { class: 'tsk' }, { unit: '📘', lesson: '▶', word: '🔤' }[it.k]), el('span', {}, el('b', {}, it.t), el('small', {}, it.sub)))));
    });
    inp.addEventListener('keydown', e => { if (e.key === 'Enter') { const b = out.querySelector('.tsit'); if (b) b.click(); } if (e.key === 'Escape') { inp.value = ''; out.innerHTML = ''; } });
    box.append(inp, out); return box;
  }
  function toc() {
    const route = location.hash.slice(1); const wrap = el('div', { style: 'display:flex;flex-direction:column;gap:12px' });
    wrap.append(tocSearch());
    // the current course, with a small menu to change it
    const g0 = Core.STAGE; const cmenu = el('div', { class: 'tmenu', hidden: true });
    // Only the learner's own courses: same subject first, at most 3 shown until "Show all".
    // The next stage is suggested only when the current course is finished.
    const subj = g => (g >= 20 ? 2 : g >= 10 ? 1 : 0);
    const cname = g => el('span', {}, el('b', { class: 'cam' }, 'Cambridge'), ' ' + (g >= 20 ? '🗣 ESL Stage ' + (g - 20) : g >= 10 ? '📐 Maths Stage ' + (g - 10) : 'Stage ' + g));
    const mine = Core.STAGES.filter(g => g !== g0 && !Core.stageLocked(g) && Core.enrolled(g))
      .sort((a, b) => (subj(a) !== subj(g0)) - (subj(b) !== subj(g0)) || Math.abs(a - g0) - Math.abs(b - g0));
    const myItem = g => el('a', { class: 'it', href: '#stage-' + g, onclick: ev => { ev.preventDefault(); pickStage(g, ev.currentTarget); } }, cname(g), el('small', { class: 'sl' }, stagePct(g) + '%'));
    // the next stage: suggested only when 80 % of this stage's lessons and Unit Tests are done (one stage per learner)
    const upnext = el('div', { class: 'tupnext' }); cmenu.append(upnext);
    if (st && !isGuest() && Core.myCourses().length) {
      const lv = Core.learnerStage(), nxt = Core.levelOf(g0) + 1 + (g0 - Core.levelOf(g0));
      Core.levelProgress(lv).then(p => { if (!p.ready || !Core.STAGES.includes(nxt) || Core.stageLocked(nxt) || Core.enrolled(nxt)) return;
        upnext.append(el('span', { class: 'h' }, `🎉 STAGE ${lv} ${p.lessons}% DONE – UP NEXT`), el('a', { class: 'it tnext', href: '#checkout-' + nxt }, cname(nxt), el('small', { class: 'sl' }, 'Enrol →'))); }).catch(() => { });
      const add = Core.subjectKeys(lv).filter(k => !Core.enrolled(k) && !Core.stageLocked(k));
      if (add.length) cmenu.append(el('span', { class: 'h' }, `ADD A SUBJECT TO STAGE ${lv}`), ...add.map(k => el('a', { class: 'it tadd', href: '#checkout-' + k }, cname(k), el('small', { class: 'sl' }, 'Add →'))));
    }
    if (mine.length) {
      cmenu.append(el('span', { class: 'h' }, 'YOUR OTHER COURSES'));
      mine.slice(0, 3).forEach(g => cmenu.append(myItem(g)));
      if (mine.length > 3) {
        const more = el('div', { class: 'tmore', hidden: true }, ...mine.slice(3).map(myItem));
        const tog = el('button', { type: 'button', class: 'it tshowall', 'aria-expanded': 'false', onclick: () => { more.hidden = !more.hidden; tog.setAttribute('aria-expanded', String(!more.hidden)); tog.firstChild.textContent = more.hidden ? `Show all my courses (${mine.length})` : 'Show fewer'; } },
          el('span', {}, `Show all my courses (${mine.length})`));
        cmenu.append(tog, more);
      }
    }
    cmenu.append(el('a', { class: 'it tbrowse', href: '#courses' }, 'Browse all courses →'));
    const cbtn = el('button', { type: 'button', class: 'tcourse', id: 'tocCourse', 'aria-expanded': 'false', onclick: () => { cmenu.hidden = !cmenu.hidden; cbtn.setAttribute('aria-expanded', String(!cmenu.hidden)); } },
      el('span', {}, el('small', {}, 'YOUR COURSE'), el('b', {}, el('span', { class: 'cam' }, 'Cambridge'), ' ' + Core.stageLabel())), el('span', { class: 'tpct' }, stagePct(g0) + '%'), el('span', { class: 'chev', 'aria-hidden': 'true' }, '▾'));
    wrap.append(el('div', { class: 'card lvl tcoursebox' }, cbtn, cmenu));
    // the unit being studied
    const u = Core.INDEX.units.find(x => x.n === Core.UNO) || Core.INDEX.units[0];
    const umenu = el('div', { class: 'tmenu tunits', hidden: true }, el('span', { class: 'h' }, 'CHOOSE A UNIT'),
      ...Core.INDEX.units.map(x => { const us = Core.unitStatus(st, x.n);
        if (us === 'soon') return el('span', { class: 'it lockedit' }, unitIcon(x.n), el('span', {}, `${x.n}. ${x.t}`), el('small', { class: 'lkd' }, '🔒'));
        return el('button', { type: 'button', class: 'it' + (x.n === Core.UNO ? ' on' : ''), onclick: () => { umenu.hidden = true; if (x.n === Core.UNO) return; Core.switchUnit(x.n).then(() => go('u-' + x.n)).catch(() => toast('Could not open that unit.')); } },
          unitIcon(x.n), el('span', {}, `${x.n}. ${x.t}`), us === 'passed' ? el('small', { style: 'color:#1E8E4E;font-weight:800' }, '✓') : null); }));
    const ubox = el('div', { class: 'card tunit' },
      el('div', { class: 'tuhead' }, unitIcon(u.n), el('div', {}, el('small', {}, `UNIT ${u.n} OF ${Core.INDEX.units.length}`), el('b', {}, u.t)),
        el('button', { type: 'button', class: 'btn small', id: 'changeUnit', onclick: () => { umenu.hidden = !umenu.hidden; } }, 'Change unit ▾')),
      umenu, el('div', { class: 'unitmeta' }, el('a', { href: '#u-' + u.n }, 'Unit overview'), el('small', { class: 'muted' }, `≈ ${estH(u.est || 0)} · you ${hrs(Core.unitSeconds(u.n))}`)));
    if (C) ubox.append(unitSecNav(u.n, C, Core.S.states[Core.unitId(u.n)], route));
    wrap.append(ubox, el('div', { class: 'card tocfoot' }, el('a', { href: '#tests' }, '📝 Tests & exams'), el('a', { href: '#final' }, '🏁 End-of-year exams'), el('a', { href: '#checkpoint' }, '🏛 Checkpoint exam room'), el('a', { href: '#bank' }, '🗂 Question Bank'), el('a', { href: '#words' }, '📒 My word book'), el('a', { href: '#cert' }, '🎓 Certificate')));
    return wrap;
  }
  function refreshToc() { const t = document.querySelector('.toc'); if (t && st && t.childElementCount) { t.innerHTML = ''; t.append(toc()); } }
  function goNext(nx) { go(nx.route, nx.tab ? { tab: { ...UI.tab, [nx.route]: nx.tab }, idx: { ...UI.idx, [nx.route + nx.tab]: nx.idx } } : null); }
  /* where am I / what remains / next button (shown on every learning screen) */
  // dotted page header shared by every student page (the "Home 01" look)
  /* ---------- course switcher: Science Stages 7–9 and Mathematics Stage 9 ---------- */
  const STAGE_N = { 1: 6, 2: 6, 11: 8, 12: 8, 13: 17, 14: 18, 15: 18, 16: 17, 17: 16, 18: 16, 19: 15 };
  const stagePct = g => Math.round(Object.keys((st && st.results) || {}).filter(k => k.startsWith(`stage${g}-unit`)).length / (STAGE_N[g] || (g >= 20 ? 6 : g >= 10 ? 15 : g <= 6 ? 6 : 14)) * 100);
  const stageShort = g => (g >= 10 ? `Stage ${Core.stageNo(g)}` : `Stage ${g}`);
  function stageSoon(g) {
    const m = $main();
    pageHero(g >= 20 ? (g <= 26 ? 'CAMBRIDGE PRIMARY ESL' : 'CAMBRIDGE LOWER SECONDARY ESL') : g >= 10 ? (g <= 16 ? 'CAMBRIDGE PRIMARY MATHEMATICS' : 'CAMBRIDGE LOWER SECONDARY MATHEMATICS') : g <= 6 ? 'PRIMARY' : 'LOWER SECONDARY', `Cambridge ${Core.stageLabel(g)}`, 'This course is being reviewed by the Camday teaching team and is not open yet.');
    m.append(crumbs(`Cambridge ${Core.stageName(g)}`), el('section', { class: 'card lockcard', id: 'stageSoon' }, el('h2', {}, `🔒 Cambridge ${Core.stageLabel(g)} – coming soon`),
      el('p', {}, 'Lessons, practice, Unit Tests and Checkpoint papers for this course open here once the review is finished. Your Science courses stay open as usual.'),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn primary small', href: `#stage-${Core.STAGE}` }, `Back to Cambridge ${Core.stageLabel()}`, el('span', { class: 'arr' }, ' →')))));
  }
  async function pickStage(g, btn) {
    const r = location.hash.slice(1);
    if (g === Core.STAGE) { if (!/^stage-\d+$/.test(r)) go('stage-' + g); return; }
    if (Core.stageLocked(g)) { if (btn) { btn.classList.remove('shake'); void btn.offsetWidth; btn.classList.add('shake'); } toast(`Cambridge ${Core.stageLabel(g)} is coming soon.`); return; }
    if (!Core.enrolled(g)) { go('stage-' + g); return; }
    if (btn) btn.classList.add('busy');
    try { await Loading.overlay(`Opening Cambridge ${Core.stageLabel(g)}`, Core.switchStage(g)); C = Core.C; st = Core.cur(); toast(`Now studying Cambridge ${Core.stageLabel(g)}`); }
    catch (e) { if (btn) btn.classList.remove('busy'); toast(errText(e)); return; }
    if (/^stage-\d+$/.test(r)) go('stage-' + g); else if (TOC_ROUTES(r) && r !== 'map') go('u-' + Core.UNO); else render();
  }
  // top menu: every stage, with Science, Mathematics and ESL listed separately under it
  function stagesMenu() {
    const panel = el('div', { class: 'stmenu', id: 'stagesMenu', hidden: true, role: 'menu' });
    const ic = d => `<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${d}</svg>`;
    const SUB = [[0, 'Science', 'sci', ic('<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.8 3h10.4a2 2 0 0 0 1.8-3l-5-9V3"/><path d="M7.5 15h9"/>')],
      [10, 'Mathematics', 'math', ic('<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 7h8M8 12h2M12 12h0M16 12h0M8 16h2M12 16h0M16 16h0"/>')],
      [20, 'English (ESL)', 'esl', ic('<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>')]];
    let sel = Core.levelOf ? Core.levelOf(Core.STAGE) : 7; if (!(sel >= 1 && sel <= 9)) sel = 7;
    const side = el('div', { class: 'stm-side', role: 'tablist', 'aria-label': 'Stage' }), pills = el('div', { class: 'stm-pills' }), head = el('div', { class: 'stm-head' });
    const pill = (n, [off, name, cls, svg]) => { const g = off + n;
      if (!Core.STAGES.includes(g)) return el('span', { class: 'stm-it stm-pill soon ' + cls, 'aria-disabled': 'true' }, el('i', { html: svg }), el('span', {}, el('b', {}, name), el('small', {}, 'Coming soon')));
      const lk = g !== Core.STAGE && Core.stageLocked(g), cur = st && g === Core.STAGE, mine = st && !isGuest() && Core.enrolled(g);
      return el('a', { class: 'stm-it stm-pill ' + cls + (cur ? ' on' : '') + (lk ? ' soon' : ''), href: '#stage-' + g, role: 'menuitem', 'data-stage': g,
        onclick: ev => { panel.hidden = true; if (mine && !lk) { ev.preventDefault(); pickStage(g); } } },
        el('i', { html: svg }), el('span', {}, el('b', {}, name), el('small', {}, lk ? 'Coming soon' : cur ? 'Studying now' : mine ? 'In your plan' : `Stage ${n}`))); };
    const draw = () => {
      side.querySelectorAll('.stm-tab').forEach(b => { const on = Number(b.dataset.n) === sel; b.classList.toggle('on', on); b.setAttribute('aria-selected', String(on)); });
      head.textContent = ''; head.append(el('span', { class: 'hl' }, sel <= 6 ? 'Cambridge Primary' : 'Cambridge Lower Secondary'), el('b', {}, `Stage ${sel}`));
      pills.textContent = ''; pills.append(...SUB.map(s => pill(sel, s))); };
    const tab = n => el('button', { type: 'button', class: 'stm-tab', role: 'tab', 'data-n': n, onclick: () => { sel = n; draw(); }, onmouseenter: () => { if (window.matchMedia('(hover:hover) and (min-width:901px)').matches) { sel = n; draw(); } } }, `Stage ${n}`, el('span', { 'aria-hidden': 'true' }, '›'));
    side.append(el('span', { class: 'stm-h' }, 'Primary'), ...[1, 2, 3, 4, 5, 6].map(tab), el('span', { class: 'stm-h' }, 'Lower Secondary'), ...[7, 8, 9].map(tab));
    panel.append(side, el('div', { class: 'stm-main' }, head, pills, el('a', { class: 'stm-all', href: '#courses', onclick: () => { panel.hidden = true; } }, 'See all courses  →')));
    draw();
    const b = el('button', { type: 'button', class: 'stm-btn', id: 'stagesBtn', 'aria-haspopup': 'true', 'aria-expanded': 'false',
      onclick: ev => { ev.stopPropagation(); panel.hidden = !panel.hidden; b.setAttribute('aria-expanded', String(!panel.hidden)); if (!panel.hidden) document.addEventListener('click', () => { panel.hidden = true; b.setAttribute('aria-expanded', 'false'); }, { once: true }); } }, 'Stages ▾');
    panel.addEventListener('click', ev => ev.stopPropagation());
    return el('span', { class: 'stm-wrap' }, b, panel);
  }
  // course switcher, one block per stage with each subject kept separate: Science, Mathematics (course key 10 + stage) and ESL
  const SUBJ = { sci: ['🔬', 'Science'], math: ['📐', 'Mathematics'], esl: ['🗣', 'ESL'] };
  function stageSwitcher() {
    const btn = (g, subj) => {
      const mine = g === Core.STAGE, lk = !mine && Core.stageLocked(g), en = mine || Core.enrolled(g), p = en ? stagePct(g) : 0, math = g >= 10 && g < 20, esl = g >= 20;
      const b = el('button', { type: 'button', class: 'sw' + (mine ? ' on' : '') + (lk ? ' locked' : en ? '' : ' enrol') + (math ? ' math' : '') + (esl ? ' esl' : ''), 'data-stage': g, 'aria-pressed': String(mine), 'aria-disabled': lk ? 'true' : null,
        title: lk ? 'Coming soon' : mine ? 'You are studying this course' : en ? 'Switch to this course' : 'Enrol to open', 'aria-label': `${SUBJ[subj][1]} ${stageShort(g)}`,
        onclick: () => pickStage(g, b) },
        el('span', { class: 'swn', 'aria-hidden': 'true' }, SUBJ[subj][0]), el('span', { class: 'swt' }, el('b', {}, SUBJ[subj][1]), el('small', {}, lk ? 'Coming soon' : !mine && !en ? 'Enrol to open' : mine ? 'Studying now' : `${p}% done`)),
        lk ? el('span', { class: 'swtag' }, '🔒') : en ? el('span', { class: 'swp', style: `--p:${p}`, 'data-p': p + '%', 'aria-hidden': 'true' }) : el('span', { class: 'swtag' }, 'Enrol'));
      return b;
    };
    // a subject that has no course for this stage yet: shown, but not a button
    const soon = subj => el('span', { class: 'swx', title: 'Not open yet' }, el('span', { class: 'swn', 'aria-hidden': 'true' }, SUBJ[subj][0]), el('span', { class: 'swt' }, el('b', {}, SUBJ[subj][1]), el('small', {}, 'Coming soon')));
    const block = n => el('div', { class: 'sg', 'data-stage-block': n }, el('small', {}, `Stage ${n}`), el('div', { class: 'sgrow' },
      Core.STAGES.includes(n) ? btn(n, 'sci') : soon('sci'), Core.STAGES.includes(10 + n) ? btn(10 + n, 'math') : soon('math'), Core.STAGES.includes(20 + n) ? btn(20 + n, 'esl') : soon('esl')));
    const level = (name, ns) => el('div', { class: 'swlevel' }, el('b', { class: 'swlh' }, name), el('div', { class: 'swlrow' }, ...ns.map(block)));
    // compact by default: only the stage being studied (its three subjects); "All stages" opens the full grid
    const cur = Core.stageNo(Core.STAGE);
    const nav = el('nav', { class: 'stsw bystage' + (UI.swOpen ? '' : ' compact'), id: 'stageSwitch', 'aria-label': 'Switch course' }, level('Lower Secondary', [7, 8, 9]), level('Primary', [1, 2, 3, 4, 5, 6]));
    nav.querySelectorAll('[data-stage-block]').forEach(b => { if (+b.getAttribute('data-stage-block') === cur) { b.classList.add('cur'); b.parentElement.parentElement.classList.add('cur'); } });
    const all = el('button', { type: 'button', class: 'btn small swall', id: 'swAll', 'aria-expanded': String(!!UI.swOpen), onclick: () => { UI.swOpen = !UI.swOpen; nav.classList.toggle('compact', !UI.swOpen); all.setAttribute('aria-expanded', String(UI.swOpen)); all.textContent = UI.swOpen ? 'Show less ▴' : 'All stages ▾'; } }, UI.swOpen ? 'Show less ▴' : 'All stages ▾');
    nav.append(all);
    return nav;
  }
  function pageHero(eyebrow, title, sub, side) {
    const w = document.getElementById('wrap'); w.classList.add('landing');
    w.before(el('section', { class: 'phero dots' }, el('div', { class: 'phero-in' }, el('div', { class: 'phero-txt' }, el('span', { class: 'eyebrow' }, eyebrow), el('h1', {}, title), sub ? el('p', {}, sub) : null), side ? el('div', { class: 'phero-side' }, ...[].concat(side)) : null)));
  }
  const statCard = (icon, big, small, href) => el(href ? 'a' : 'div', { class: 'card dstat', href: href || null }, icon, el('span', {}, el('b', {}, big), el('br'), el('small', {}, small)));
  const ringIcon = pct => el('span', { class: 'dring', style: `background:conic-gradient(var(--blue) 0 ${pct}%, #E3EBF5 0)` }, el('i', {}, pct + '%'));
  const flameIcon = () => el('span', { class: 'bob', html: AtomicIcons.html('flame', { filled: true, size: 34, color: '#E8590C' }) });
  function bar(where) {
    const left = []; let vids = 0, reqs = 0;
    C.sections.forEach(s => { if (!Core.videoDone(st, s)) vids++; reqs += Core.reqLeft(st, s).length; });
    if (vids) left.push(`${vids} ${C.sections[0] && C.sections[0].lesson ? 'lesson' : 'video'}${C.sections[0] && C.sections[0].lesson && vids > 1 ? 's' : ''}`); if (reqs) left.push(`${reqs} Core questions`); if (!Core.passed(st)) left.push('Unit Test');
    const nx = Core.nextActivity(st);
    return el('div', { class: 'where' }, el('div', {}, el('small', {}, 'You are here'), el('b', {}, where)),
      el('div', {}, el('small', {}, `Still to do in Unit ${Core.UNO}`), el('b', {}, left.length ? left.join(' · ') : 'All done 🎉')),
      el('button', { class: 'btn gold small', type: 'button', id: 'nextBtn', onclick: () => goNext(nx) }, 'Next: ' + nx.label, el('span', { class: 'arr' }, ' →')));
  }
  function lockScreen(title, reason, items) {
    return el('section', { class: 'card lockcard' }, el('h2', {}, el('span', { class: 'lockicon' }, '🔒'), ' ' + title), el('p', {}, reason),
      el('ul', { class: 'misslist' }, ...items.map(m => el('li', {}, el('span', {}, 'You still need to do ', el('b', {}, m.what)), el('button', { class: 'btn small primary', type: 'button', onclick: () => goNext(m) }, 'Go there', el('span', { class: 'arr' }, ' →'))))));
  }
  function subbar(cls, ...kids) { const s = document.getElementById('sub'); s.className = 'subbar ' + (cls || ''); s.append(el('div', { class: 'subbar-in' }, ...kids)); }
  const secPct = s => ((Core.videoDone(st, s) ? 1 : 0) * 0.3 + (8 - Core.reqLeft(st, s).length) / 8 * 0.7) * 100;
  const unitPct = () => { const p = C.sections.reduce((a, s) => a + secPct(s), 0) / C.sections.length; return Math.round(Core.passed(st) ? 100 : p * 0.9); };
  const objSecure = o => { const qs = C.sections.flatMap(s => s.req).filter(q => q.obj === o); return qs.length && qs.every(q => (st.items[q.id] || {}).ok); };

  /* ---------- home (dashboard) ---------- */
  function viewHome() {
    const m = $main();
    if (!st) { if (Core.S.me) { m.append(narrow(el('h1', {}, 'Welcome'), el('p', {}, 'This account has no learner profile.'), ['marker', 'admin'].includes(Core.S.me.profile.role) ? el('a', { class: 'btn primary', href: '#staff' }, 'Open Staff') : el('a', { class: 'btn', href: '#help' }, 'Contact us'))); return; } viewLanding(); return; }
    document.getElementById('wrap').classList.add('landing');
    Backend.announcements().then(list => { const mm = $main(); if (!mm) return; (list || []).filter(x => x.audience === 'all' || Number(x.audience) === Core.STAGE).slice(0, 3).reverse()
      .forEach(x => mm.prepend(el('div', { class: 'banner ' + (x.level === 'warn' ? 'adv' : 'info') + ' announce', role: 'status' }, el('b', {}, x.title + (x.body ? ' ' : '')), x.body || ''))); }).catch(() => { });
    const started = Object.keys(st.video).length || Object.keys(st.items).length;
    const nx = Core.nextActivity(st);
    const resume = () => {
      const l = st.last; let target = nx;
      if (l && l.route) {
        const s = l.route.startsWith('v-') || l.route.startsWith('ex-') ? Core.sec(secFromRoute(l.route)) : null;
        const unfinished = s ? (l.route.startsWith('v-') ? !Core.videoDone(st, s) : Core.reqLeft(st, s).length > 0) : (l.route === 'test' && Core.testState(st).state === 'ready') || (l.route === 'remedial' && Core.testState(st).state === 'remediate');
        if (unfinished && !(s && Core.secLock(st, s))) target = { route: l.route, tab: l.tab, idx: l.idx };
      }
      goNext(target);
    };
    // the topic in progress: first section not finished (or the last one)
    const cur = C.sections.find(s => !Core.secDone(st, s) && !Core.secLock(st, s)) || C.sections.find(s => !Core.secDone(st, s)) || C.sections[C.sections.length - 1];
    const vs = Core.vstate(st, cur.id), pausesDone = cur.stops.filter(t => (vs.stops[t.id] || {}).done).length, curLock = Core.secLock(st, cur);
    const allQ = C.sections.reduce((a, s) => a + s.req.length + s.prac.length + s.adv.length, 0), doneQ = C.sections.reduce((a, s) => a + s.req.concat(s.prac, s.adv).filter(q => (st.items[q.id] || {}).done).length, 0);
    const pct = allQ ? Math.round(doneQ / allQ * 100) : 0, sk = Core.streak(st), hr = new Date().getHours();
    const greet = hr < 12 ? 'Good morning' : hr < 18 ? 'Good afternoon' : 'Good evening';
    const dateTxt = new Date().toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' }).toUpperCase();
    // ---- dotted hero (Design 02) ----
    document.getElementById('wrap').before(el('section', { class: 'dhero dots' }, el('div', { class: 'dhero-in' },
      el('div', { class: 'dhero-txt' }, el('span', { class: 'eyebrow' }, isGuest() ? 'GUEST · TOPIC 3.1 IS OPEN' : dateTxt),
        el('h1', {}, isGuest() ? 'Welcome to Camday ' : `${greet}, ${st.alias} `, el('span', { class: 'wobble', style: 'display:inline-block;color:var(--gold)' }, '✦')),
        el('p', {}, started ? `You are on ${cur.id} ${cur.title} — next: ${nx.label.charAt(0).toLowerCase() + nx.label.slice(1)}.` : `Start with Unit ${Core.UNO}: ${C.unit.title} – topic ${C.sections[0] ? C.sections[0].id : '3.1'}. ${C.sections[0] && C.sections[0].lesson ? 'Read the lesson' : 'Watch the lesson'}, then practise.`)),
      el('div', { class: 'dstats' },
        el('a', { class: 'card dstat', href: '#profile', id: 'streakCard' }, el('span', { class: 'bob', html: AtomicIcons.html('flame', { filled: true, size: 34, color: '#E8590C' }) }),
          el('span', {}, el('b', {}, `${sk} day${sk === 1 ? '' : 's'}`), el('br'), el('small', {}, 'learning streak'))),
        el('div', { class: 'card dstat' }, el('span', { class: 'dring', style: `background:conic-gradient(var(--blue) 0 ${pct}%, #E3EBF5 0)` }, el('i', {}, pct + '%')),
          el('span', {}, el('b', {}, `${doneQ} / ${allQ}`), el('br'), el('small', {}, `Unit ${Core.UNO} questions done`))),
        el('a', { class: 'card dstat', href: '#profile', id: 'levelCard' }, el('span', { class: 'dring', style: `background:conic-gradient(var(--gold) 0 ${Core.levelInfo().pct}%, #E3EBF5 0)` }, el('i', {}, 'Lv' + Core.levelInfo().level)),
          el('span', {}, el('b', {}, `${Core.levelInfo().xp} XP`), el('br'), el('small', {}, `${Core.levelInfo().pct}% · ${TestRules.xpForLevel(Core.levelInfo().level + 1) - Core.levelInfo().xp} XP to level ${Core.levelInfo().level + 1}`))),
        el('a', { class: 'card dstat', href: `#stage-${Core.STAGE}`, id: 'hoursCard' }, el('span', { class: 'bob', style: 'font-size:30px' }, '⏱'),
          el('span', {}, el('b', {}, hrs(Core.totalSeconds())), el('br'), el('small', {}, `studied of ≈ ${estH(Core.INDEX.est || 0)} course`)))))));
    if (isGuest()) m.append(el('div', { class: 'banner info', id: 'guestBanner' }, el('b', {}, 'You are learning as a guest. '), 'Your progress is kept on this device only and topic 3.1 is open. Sign up free to save it and unlock every topic.', el('a', { class: 'btn small gold', href: '#signup' }, 'Sign up free')));
    else if (Core.freeMode()) m.append(el('div', { class: 'banner info', id: 'freeBanner' }, el('b', {}, Core.expiredCourses().length ? 'Your course has expired. ' : 'Free plan: '),
      Core.expiredCourses().length ? 'You did not study for a year, so the course closed. Buy it again to carry on – your free Unit 3 lessons stay open.'
        : `every lesson video of Unit ${Core.FREE_UNIT} and its Core questions (8 per section) are open. Buy Cambridge ${Core.stageName(Core.STAGE)} once to open every unit, all practice and the Unit Tests.`,
      el('a', { class: 'btn small gold', href: '#plans' }, 'See plans')));
    if (Backend.mode === 'demo' && !isGuest()) m.append(el('div', { class: 'banner adv' }, el('b', {}, 'Trying the preview? '), 'Use the tester tools on the Progress page to unlock sections instantly.', el('a', { class: 'btn small', href: '#profile' }, 'Open tester tools')));
    const left = el('div', { class: 'dmain' }), aside = el('aside', { class: 'daside' });
    m.append(el('div', { class: 'dgrid' }, left, aside));
    // continue card
    const thumb = cur.lesson ? el('div', { class: 'dthumb lessonthumb', 'aria-hidden': 'true' }, el('span', { class: 'lp-play pulse' }, '📖')) : el('div', { class: 'dthumb', style: `background-image:url(${(cur.video.poster || cur.video.src.replace('.mp4', '_poster.jpg'))})` }, el('span', { class: 'lp-play pulse', 'aria-hidden': 'true' }, svgI(I.play, 28, '#1C2A3A', 2.6)));
    left.append(el('section', { class: 'card lift dcont', 'aria-label': 'Continue learning', onclick: e => { if (e.target.closest('a,button')) return; resume(); } }, thumb,
      el('div', { class: 'dcont-txt' }, el('span', { class: 'eyebrow' }, `${started ? 'CONTINUE' : 'START'} · UNIT ${Core.UNO} › ${cur.id}`), el('h2', {}, cur.title),
        el('p', { class: 'muted', style: 'font-size:16px;margin:0' }, cur.objs.slice(0, 2).map(o => C.objectives[o].t).join(' ')),
        el('div', { class: 'dprog' }, el('div', { class: 'pbar' }, el('i', { style: `width:${cur.stops.length ? pausesDone / cur.stops.length * 100 : 0}%` })), el('small', {}, `${pausesDone} of ${cur.stops.length} ${cur.lesson ? 'check' : 'pause'} questions`)),
        curLock ? el('p', { class: 'muted', style: 'margin:0' }, '🔒 ' + curLock.reason) : null,
        el('div', { class: 'btnrow' }, el('button', { class: 'btn primary shine', type: 'button', id: 'resumeBtn', onclick: started ? resume : () => go('v-' + R(cur.id)) }, svgI(I.play, 16, '#fff', 2.6), started ? (vs.pos > 1 && !cur.lesson && !Core.videoDone(st, cur) ? `Resume at ${fmt(vs.pos)}` : 'Continue learning') : 'Start learning'),
          el('a', { class: 'btn', href: '#ex-' + R(cur.id) }, `Practise ${cur.id}`)))));
    // unit table
    const stCls = s => Core.secLock(st, s) ? ['todo', 'Locked'] : Core.secDone(st, s) ? ['done', 'Completed'] : (Core.videoDone(st, s) || Core.reqLeft(st, s).length < 8 || Object.keys(Core.vstate(st, s.id).stops).length) ? ['cur', 'In progress'] : ['todo', 'Not started'];
    left.append(el('section', { class: 'card dtable' }, el('div', { class: 'dth' }, el('h2', {}, `Unit ${Core.UNO} · ${C.unit.title}`), el('a', { href: '#u-' + Core.UNO, class: 'ul' }, 'Open the course →')),
      el('div', { class: 'tablewrap' }, el('div', { class: 'drows' }, el('div', { class: 'drow h' }, ...['Topic', 'Lesson', 'Core', 'Practice', 'Extension', 'Status'].map(t => el('span', {}, t))),
        ...C.sections.map(s => { const v = Core.vstate(st, s.id), core = 8 - Core.reqLeft(st, s).length, [c, t] = stCls(s), np = Object.values(v.stops).filter(x => x.done).length;
          return el('a', { class: 'drow', href: Core.secLock(st, s) ? '#u-' + Core.UNO : (Core.videoDone(st, s) ? '#ex-' : '#v-') + R(s.id) }, el('span', {}, el('b', { style: 'color:var(--blue)' }, s.id), ' ' + s.title),
            el('span', {}, Core.videoDone(st, s) ? (s.lesson ? 'Read' : 'Watched') : np ? `${np} of ${s.stops.length} ${s.lesson ? 'checks' : 'pauses'}` : '—'),
            el('span', { class: 'dcore' }, el('span', { class: 'pbar' }, el('i', { style: `width:${core / 8 * 100}%` })), `${core}/8`),
            el('span', {}, `${s.prac.filter(q => (st.items[q.id] || {}).done).length}/${s.prac.length}`), el('span', {}, `${s.adv.filter(q => (st.items[q.id] || {}).done).length}/${s.adv.length}`),
            el('span', {}, el('span', { class: 'status ' + c }, t))); })))));
    // every unit of the stage: open any of them at any time
    left.append(el('section', { class: 'card dtable', id: 'unitPicker' }, el('div', { class: 'dth' }, el('h2', {}, `Cambridge ${Core.stageName(Core.STAGE)} units`), el('small', { class: 'muted' }, 'Open any unit – you do not have to finish one first')),
      el('div', { class: 'lp-ugrid', style: 'padding:8px 32px 24px' }, ...Core.INDEX.units.map(u => { const us = Core.unitStatus(st, u.n);
        return el(us === 'soon' ? 'div' : 'a', us === 'soon' ? { class: 'card lp-unit off', title: 'Coming soon' } : { class: 'card lift lp-unit' + (u.n === Core.UNO ? ' cur' : ''), href: '#u-' + u.n, 'data-unit': u.n },
          unitIcon(u.n), el('span', { class: 'lp-ut' }, el('small', {}, 'UNIT ' + u.n), el('br'), el('b', {}, u.t)), us === 'passed' ? el('span', { class: 'lp-free', style: 'background:#1E8E4E' }, '✓') : u.n === Core.UNO ? el('span', { class: 'lp-free' }, 'Now') : us === 'soon' ? el('span', { class: 'lp-tag' }, 'Soon') : null); }))));
    // suggested next
    const wl = wrongList(), wsSec = st.ws.length ? null : cur;
    const sug = el('section', { class: 'card dsug' }, el('h2', {}, 'Suggested next'));
    const sRow = (cls, icon, t, d, btn) => el('div', { class: 'srow' }, el('span', { class: 'sic ' + cls, html: icon }), el('span', { class: 'st' }, el('b', {}, t), el('br'), el('small', { class: 'muted' }, d)), btn);
    sug.append(sRow('o wobble', AtomicIcons.html('file-text', { size: 26, color: '#9A4A00' }),
      `Worksheet ${cur.id} · ${cur.title}`, 'Printable A4 worksheet with Core and practice questions', el('a', { class: 'btn small', href: '#ws-' + R(cur.id) }, 'Open')));
    sug.append(sRow('b pulse', AtomicIcons.html('clock', { size: 26, color: '#0149AF' }),
      wl.length ? 'Redo the questions you found tricky' : 'Revise by learning objective', wl.length ? `${wl.length} question${wl.length === 1 ? '' : 's'} you got wrong before` : 'Pick an objective and practise it',
      el('button', { class: 'btn primary small', type: 'button', id: 'tileWrong', onclick: () => wl.length ? startDrill('Redo wrong answers', wl, 'wrong') : go('topic') }, 'Start', el('span', { class: 'arr' }, ' →'))));
    left.append(sug);
    // aside: unit test card
    const ts = Core.testState(st), totalReq = C.sections.reduce((a, s) => a + 8 - Core.reqLeft(st, s).length, 0);
    aside.append(el('section', { class: 'dtest' }, el('div', { class: 'blob drift', 'aria-hidden': 'true' }),
      el('div', { class: 'dtest-h' }, el('span', { class: 'wobble', html: AtomicIcons.html('lock', { size: 26, color: '#E0A800' }) }), el('b', {}, `Unit Test ${Core.UNO}`)),
      el('p', {}, ts.state === 'passed' ? (LEADERBOARD ? 'Passed — well done! Your first-pass score counts towards the leaderboard.' : 'Passed — well done!') : Core.unitOpen(Core.UNIT) ? `Open now · ${TestRules.UNIT_MINUTES} minutes in the exam room · pass above 70%.` : `Unlocks when you finish every ${C.sections[0] && C.sections[0].lesson ? 'lesson' : 'video'} and Core question in this unit · ${TestRules.UNIT_MINUTES} minutes · pass above 70%.`),
      el('div', { class: 'dsegs' }, ...C.sections.map(s => el('span', { class: Core.secDone(st, s) ? 'on' : (8 - Core.reqLeft(st, s).length) ? 'half' : '' }))),
      el('small', {}, `Core questions: ${totalReq} of ${C.sections.length * 8}`),
      el('a', { class: 'btn gold', href: isGuest() ? '#signup' : ts.state === 'passed' ? '#result' : '#tests', id: 'dashTest' }, isGuest() ? 'Sign up to take the test' : ts.state === 'passed' ? 'See my result' : ts.state === 'ready' ? 'Start the test' : 'Preview the test', el('span', { class: 'arr' }, ' →'))));
    // aside: leaderboard
    const lb = el('section', { class: 'card dside' }, el('div', { class: 'dth' }, el('b', { class: 'lex' }, 'Leaderboard'), el('span', { class: 'bob', html: AtomicIcons.html('trophy', { size: 24, color: '#935A00' }) })));
    const lbBody = el('div', { class: 'dlb' }, Loading.skeleton('lines')); lb.append(lbBody, el('a', { class: 'ul', href: '#board' }, 'Full leaderboard →'));
    if (LEADERBOARD) aside.append(lb);
    if (!LEADERBOARD) { } else if (!isGuest()) Backend.leaderboard(Core.STAGE).then(rows => { rows = (rows || []).filter(r => r.score != null).map(r => ({ alias: r.nickname, score: Number(r.score), me: !!r.is_mine })); Core.competitionRank(rows); lbBody.innerHTML = '';
      if (!rows.length) lbBody.append(el('p', { class: 'muted', style: 'margin:0' }, 'No ranked learners yet – pass a Unit Test to appear here.'));
      rows.slice(0, 4).forEach((r, i) => lbBody.append(el('div', { class: 'lbmini' + (r.me ? ' me' : '') }, el('b', { class: 'rk' }, String(r.rank)), el('span', { class: 'a', style: `background:${['#0149AF', '#F08A4B', '#3FA34D', '#0B2545'][i % 4]}` }, r.alias.slice(0, 1).toUpperCase()), el('span', { class: 'n' }, r.me ? 'You' : r.alias), el('b', { class: 'sc' }, r.score.toFixed(1) + '%')))); }).catch(() => { lbBody.innerHTML = ''; });
    else { lbBody.innerHTML = ''; lbBody.append(el('p', { class: 'muted', style: 'margin:0' }, 'Sign up free to join the leaderboard.')); }
    // aside: this week
    aside.append(el('section', { class: 'card dside' }, el('b', { class: 'lex' }, 'This week'), el('div', { class: 'dweek', id: 'weekStrip' }, ...Core.week(st).map((d, i) => el('div', { class: 'rise', style: `animation-delay:${i * .06}s` }, el('span', { class: 'wd' + (d.met ? ' met' : '') + (d.today ? ' today' : '') }, d.met ? '✓' : ''), el('small', {}, d.label)))),
      el('small', { class: 'muted' }, sk ? `${sk}-day streak – learn something every day to keep it going.` : 'Learn something today to start a streak.')));
    // aside: worth revising
    const objs = Object.entries(C.objectives).map(([k, o]) => { const qs = C.sections.flatMap(s => s.req.concat(s.prac, s.adv)).filter(q => q.obj === k); const tried = qs.filter(q => (st.items[q.id] || {}).done); const first = tried.filter(q => st.items[q.id].ok && (st.items[q.id].tries || 1) === 1).length;
      return { k, t: o.t, n: tried.length, pct: tried.length ? Math.round(first / tried.length * 100) : null }; }).filter(o => o.n >= 2 && o.pct < 80).sort((a, b) => a.pct - b.pct).slice(0, 3);
    aside.append(el('section', { class: 'card dside' }, el('b', { class: 'lex' }, 'Worth revising'),
      ...(objs.length ? objs.map(o => el('div', { class: 'wrev' }, el('span', { class: 'wt' }, el('span', {}, o.t), el('b', {}, o.pct + '%')), el('div', { class: 'pbar warn' }, el('i', { style: `width:${o.pct}%` })))) : [el('p', { class: 'muted', style: 'margin:0' }, 'Answer a few more questions and we will show the ideas worth revising here.')]),
      el('a', { class: 'ul', href: '#profile' }, 'See full report →')));
    aside.append(el('section', { class: 'dknow' }, el('span', { class: 'pulse', html: AtomicIcons.html('bulb', { size: 18 }) }),
      el('span', {}, el('b', {}, 'Did you know? '), Core.IS_MATHS ? '√2 cannot be written as a fraction – its decimal digits never end and never repeat.' : 'Some nerve cells are only about 0.1 mm wide but can be up to 1 metre long.')));
  }
  const statTile = (ic, big, small) => el('div', { class: 'tile', style: 'cursor:default' }, el('span', { class: 'ti' }, ic), el('b', {}, big), el('small', {}, small));
  function levelCards() {
    return el('div', { class: 'levelcards' }, el('div', { class: 'card lift' }, el('span', { class: 'lv' }, '7–9'), el('span', {}, el('b', { class: 'lex' }, 'Lower Secondary'), el('br'), el('small', { class: 'muted' }, `Checkpoint · Cambridge ${Core.stageName(Core.STAGE)} open now`))),
      el('div', { class: 'card off' }, el('span', { class: 'lv' }, 'IG'), el('span', {}, el('b', { class: 'lex' }, 'Cambridge IGCSE'), el('br'), el('small', { class: 'muted' }, 'Coming soon')), el('span', { class: 'lockicon' }, svgI(I.lock, 20, '#8B98AB', 2))),
      el('div', { class: 'card off' }, el('span', { class: 'lv' }, 'A'), el('span', {}, el('b', { class: 'lex' }, 'AS & A Level'), el('br'), el('small', { class: 'muted' }, 'Coming soon')), el('span', { class: 'lockicon' }, svgI(I.lock, 20, '#8B98AB', 2))));
  }
  function cellLens() {
    const on = el('div', { class: 'onion' }); for (let i = 0; i < 42; i++) on.append(el('span', { style: Math.floor(i / 6) % 2 ? 'margin-left:-12px' : '' }));
    return el('div', { class: 'cellview', 'aria-hidden': 'true' }, el('div', { class: 'ring' }), el('div', { class: 'lens' }, on), el('span', { class: 'mag' }, '×400'));
  }

  /* ---------- course page: learning path ---------- */
  // ---- unit page (Design v4) ----
  const ceil5 = m => Math.max(5, Math.ceil(m / 5) * 5);
  function secEst(s) {   // share of the unit estimate, weighted by video length; rounded up to 5 min
    const K = 600, tot = C.sections.reduce((a, x) => a + x.video.dur + K, 0), est = C.est || Core.estMinutes(Core.UNO);
    return ceil5(est * (s.video.dur + K) / tot);
  }
  const minTxt = m => m >= 60 ? `${Math.floor(m / 60)} h${m % 60 ? ' ' + (m % 60) + ' min' : ''}` : `${m} min`;
  function learningPath() {
    const box = el('div', { class: 'path4', style: 'display:flex;flex-direction:column;gap:16px' }); box.append(el('span', { class: 'pathtab' }, el('b', {}, String(C.sections.length)), ` topic${C.sections.length === 1 ? '' : 's'} in unit`));
    C.sections.forEach(s => {
      const lock = Core.secLock(st, s), done = Core.secDone(st, s), vd = Core.videoDone(st, s), vs = Core.vstate(st, s.id);
      const reqDone = 8 - Core.reqLeft(st, s).length;
      const pracDone = s.req.concat(s.prac, s.adv).filter(q => (st.items[q.id] || {}).done).length;
      const ansStops = s.stops.filter(x => Core.stopDone(st, s.id, x)).length;
      const started = vd || ansStops || reqDone || pracDone;
      const state = lock ? 'lock' : done ? 'done' : started ? 'go' : 'new';
      const tile = (cls, ic, name, sub, href, locked, extra) => el('a', { class: 'u4tile ' + cls, href: locked ? null : href, 'aria-disabled': locked ? 'true' : null, style: locked ? 'opacity:.55;pointer-events:none' : null }, el('i', {}, ...AtomicIcons.swap(ic, / go\b/.test(' ' + cls))), el('span', {}, el('b', {}, name), el('small', {}, sub), extra || null));
      const vlen = s.lesson ? `about ${Math.max(5, Math.round(s.video.dur / 60))} min · ${s.stops.length} check questions` : `${fmt(s.video.dur)} · ${s.stops.length} pause questions`;
      const tiles = el('div', { class: 'u4tiles' },
        tile(vd ? 'ok' : ansStops ? 'go' : '', s.lesson ? '📖' : '▶', s.lesson ? 'Read the lesson' : 'Watch', vd ? vlen + ' ✓' : ansStops ? `${ansStops} of ${s.stops.length} pauses · ${fmt(vs.pos || 0)}` : vlen, '#v-' + R(s.id), !!lock),
        tile(reqDone === 8 ? 'ok' : reqDone || pracDone ? 'go' : '', reqDone === 8 ? '✓' : s.vocab ? (C.unit.young ? '🎧' : '🎤') : '✎', s.vocab ? (C.unit.young ? 'Listen & practise' : 'Listen, say & practise') : 'Practise', `${pracDone}/${s.prac.length} · ${reqDone}/8 Core`, '#ex-' + R(s.id), !!lock || !vd, reqDone && reqDone < 8 ? el('span', { class: 'u4mini' }, el('i', { style: `width:${reqDone / 8 * 100}%` })) : null),
        s.lab ? (() => { const L = (st.labs || {})[s.id] || {}; const vdn = !!(L.v || {}).done, hdn = !!(L.h || {}).done; return tile(vdn && hdn ? 'ok' : vdn || hdn ? 'go' : '', '🧪', 'Experiment', vdn && hdn ? 'Lab + home ✓' : vdn ? 'Lab ✓ · try it at home' : 'Virtual lab + at home', '#lab-' + R(s.id), !!lock); })()
          : tile(st.ws.includes(s.id) ? 'ok' : '', '🖨', 'Worksheet', st.ws.includes(s.id) ? 'Printed' : 'Print only', '#ws-' + R(s.id), !!lock),
        Core.IS_ESL ? (() => { const sp = (st.speak || {})[s.id]; return tile(sp ? 'ok' : '', '🎤', 'Speaking', sp ? `${sp.n} talk${sp.n === 1 ? '' : 's'} · best ${'★'.repeat(sp.best)}` : 'Talk with the tutor', '#sp-' + R(s.id), !!lock); })() : null,
        secGameWords(s).length ? (() => { const gg = (st.games || {})[s.id]; return tile(gg ? 'ok' : '', '🎮', 'Word games', gg ? `${gg.n} played · best ${gg.best}` : `5 games · ${secGameWords(s).length} words`, '#gm-' + R(s.id), !!lock); })() : null);
      const pill = { lock: ['lock', '🔒 Locked'], done: ['ok', 'Completed'], go: ['go', 'In progress'], new: ['no', 'Not started'] }[state];
      const btn = lock ? (lock.paywall ? el('a', { class: 'btn small gold', href: '#' + lock.route }, lock.guest ? 'Sign up free' : 'See plans') : null)
        : done ? el('a', { class: 'btn small ghost', href: '#v-' + R(s.id) }, `Review ${s.id}`)
          : el('a', { class: 'btn small ' + (state === 'go' ? 'primary' : ''), href: vd ? '#ex-' + R(s.id) : '#v-' + R(s.id) }, vd ? `Continue practice ${s.id}` : vs.pos > 1 ? `Resume at ${fmt(vs.pos)}` : `Start ${s.id}`, el('span', { class: 'arr' }, ' →'));
      box.append(el('article', { class: 'u4topic' + (state === 'done' ? ' done' : state === 'go' ? ' cur' : ''), id: 'topic-' + R(s.id) },
        el('div', { class: 'u4num' }, done ? '✓' : s.id),
        el('div', {}, el('div', { class: 'u4tt' }, el('div', {}, el('p', { class: 'eyebrow', style: 'margin:0' }, 'Topic ' + s.id), el('h3', {}, s.title)), el('span', { class: 'u4st ' + pill[0] }, pill[1])),
          el('p', { class: 'd' }, lock ? '🔒 ' + lock.reason : s.objs.map(o => C.objectives[o].t).join(' ')),
          tiles, el('div', { class: 'u4foot' }, el('span', {}, `≈ ${minTxt(secEst(s))}`), btn))));
    });
    return box;
  }
  function examBlock() {
    const ts = Core.testState(st), totalReq = C.sections.reduce((a, s) => a + 8 - Core.reqLeft(st, s).length, 0);
    const res = (st.results || {})[Core.UNIT], pct = res ? Math.round(res.first_pass_pct || res.pct || 0) : null;
    const fact = (b, t) => el('div', {}, el('b', {}, b), el('span', {}, t));
    const btn = ts.state === 'guest' ? el('a', { class: 'btn gold', href: '#signup' }, 'Sign up free to take the test')
      : ts.state === 'paywall' ? el('a', { class: 'btn gold', href: '#plans' }, `Buy Cambridge ${Core.stageName(Core.STAGE)} to take the test`)
        : el('a', { class: 'btn gold', href: ts.state === 'passed' ? '#result' : '#test' }, ts.state === 'locked' ? 'See what\'s missing' : ts.state === 'passed' ? 'See results' : 'Enter the exam room');
    const passed = ts.state === 'passed';
    return el('section', { class: 'u4exam', id: 'unitTestCard' },
      el('div', {}, el('p', { class: 'eyebrow', style: 'margin:0' }, passed ? 'Final step · passed' : 'Final step · exam room'), el('h3', {}, `Unit Test ${Core.UNO} — ${C.unit.title}`),
        el('p', { style: 'margin:0' }, passed ? 'You passed this Unit Test. You can sit it again to practise – your first pass is what counts.'
          : Core.unitOpen(Core.UNIT) ? 'Open now (test phase). A timed paper in the exam room – the clock keeps running if you leave the page, and the paper is handed in automatically at 0:00.'
            : `Opens when every ${C.sections[0] && C.sections[0].lesson ? 'lesson' : 'video'} and Core question is done (${totalReq} of ${C.sections.length * 8} Core done). The clock keeps running if you leave the page.`),
        el('div', { class: 'u4facts' }, passed && pct != null ? fact(pct + '%', 'your score') : null, fact(TestRules.UNIT_MINUTES + ' min', 'time allowed'), fact('> 70%', 'to pass'), fact('+100 XP', passed ? 'earned' : 'when you pass'))),
      el('div', { class: 'u4clk' }, el('div', { style: passed ? 'color:#7FD3A1' : '' }, passed ? '✓ Passed' : `${TestRules.UNIT_MINUTES}:00`), el('span', {}, passed ? '' : ts.state === 'locked' ? 'Not open yet' : 'Ready when you are'), btn));
  }
  function viewUnit() {
    const m = $main(); const nx = Core.nextActivity(st);
    const meta = Core.INDEX.units.find(u => u.n === Core.UNO) || {}; const art = window.UnitArt ? UnitArt(Core.STAGE === 7 ? Core.UNO : 0, Core.IS_MATHS ? 'Maths:' + (meta.strand || '') : meta.strand) : { svg: '', tag: '' };
    const nobj = Object.keys(C.objectives).length, sec = Object.keys(C.objectives).filter(objSecure).length, pct = unitPct();
    const studied = Core.unitSeconds(Core.UNO);
    const crumbs4 = el('nav', { class: 'u4crumbs', 'aria-label': 'Breadcrumb' }, el('a', { href: '#home' }, 'Dashboard'), el('span', {}, '›'), el('a', { href: '#level' }, 'Cambridge ' + Core.levelName(Core.STAGE)), el('span', {}, '›'),
      el('a', { href: `#stage-${Core.STAGE}` }, el('b', { class: 'cam' }, 'Cambridge'), ` ${Core.stageName(Core.STAGE)}`), el('span', {}, '›'), el('a', { href: '#u-' + Core.UNO, 'aria-current': 'page' }, el('b', {}, `Unit ${Core.UNO} · ${C.unit.title}`)));
    const heroS = el('section', { class: 'u4hero' }, el('div', { class: 'u4hero-in' },
      el('div', {}, crumbs4,
        el('div', { class: 'u4kick' }, el('span', { class: 'stagetag' }, el('span', {}, 'Cambridge'), el('span', {}, `${Core.stageName(Core.STAGE)}`)), el('span', { class: 't' }, `Unit ${Core.UNO} of ${Core.unitCount()} · ${C.unit.strandShort || ''}`)),
        el('h1', {}, C.unit.title), el('p', { class: 'lead' }, C.unit.blurb || ''),
        el('div', { class: 'u4facts', id: 'unitHours' }, el('div', {}, el('b', {}, `≈ ${estH(C.est || Core.estMinutes(Core.UNO))}`), el('span', {}, 'estimated time')),
          el('div', {}, el('b', {}, hrs(studied)), el('span', {}, Core.passed(st) ? 'completed in' : 'studied so far')),
          el('div', {}, el('b', {}, `${sec} / ${nobj}`), el('span', {}, 'objectives secure'))),
        el('div', { class: 'u4prog' }, el('div', { class: 'top2' }, el('span', {}, 'Unit progress'), el('span', {}, pct + '%')), el('div', { class: 'pbar' + (pct === 100 ? ' ok' : '') }, el('i', { style: `width:${pct}%` }))),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn navy', type: 'button', onclick: () => goNext(nx) }, '▶ ' + nx.label), el('a', { class: 'btn', href: '#map' }, 'Open the concept map')),
        el('nav', { class: 'unav', 'aria-label': 'Units' },
          Core.UNO > 1 ? el('a', { class: 'btn small', href: '#u-' + (Core.UNO - 1), id: 'prevUnit' }, '← Previous unit') : null,
          Core.UNO < Core.unitCount() ? el('a', { class: 'btn small', href: '#u-' + (Core.UNO + 1), id: 'nextUnit' }, 'Next unit →') : null,
          el('a', { class: 'btn small', href: '#stage-' + Core.STAGE, id: 'allUnits' }, 'View all units')),
        Core.unitOpen(Core.UNIT) ? el('span', { class: 'opentag', style: 'margin-top:10px;display:inline-block' }, 'All topics open (test phase)') : null),
      el('div', { class: 'u4art', 'aria-hidden': 'true' }, el('div', { class: 'lens2', html: `<svg viewBox="0 0 380 380">${art.svg}</svg>` }), el('span', { class: 'tag' }, art.tag),
        el('div', { class: 'float' }, el('i', {}, Core.passed(st) ? '🏆' : '▶'), el('div', {}, el('b', {}, Core.passed(st) ? 'Unit passed' : 'Next up'), nx.label)))));
    document.getElementById('wrap').before(heroS);
    m.append(...[tocBtn(), el('div', { class: 'u4head' }, el('div', {}, el('p', { class: 'eyebrow', style: 'margin:0' }, `Cambridge ${Core.stageName(Core.STAGE)} · Unit ${Core.UNO}`), el('h2', {}, 'Your learning path')),
      el('div', { class: 'u4steps' }, ...(C.unit.tiny ? ['1 Read the lesson', '2 Practise', '3 Word games', '4 Unit Test'] : Core.IS_PRIMARY ? (Core.stageNo(Core.STAGE) <= 5 ? ['1 Watch', C.unit.young ? '2 Listen & practise' : '2 Listen & say', '3 Experiment', '4 Word games', '5 Unit Test'] : ['1 Watch', '2 Listen & say', '3 Experiment', '4 Unit Test']) : [C.unit.read ? '0 Read first' : null, Core.IS_MATHS ? '1 Read the lesson' : '1 Watch', '2 Practise', '3 Worksheet', '4 Unit Test'].filter(Boolean)).map(t => el('span', {}, t)))),
      C.unit.read ? el('section', { class: 'card readfirst', id: 'readFirst' }, el('div', { class: 'rfico', 'aria-hidden': 'true' }, '📘'),
        el('div', {}, el('p', { class: 'eyebrow', style: 'margin:0' }, Core.IS_MATHS ? 'Read before the lesson' : 'Read before you watch'), el('h3', { style: 'margin:2px 0 4px' }, `Unit ${Core.UNO} pre-reading pack (PDF)`),
          el('p', { class: 'muted', style: 'margin:0' }, Core.IS_MATHS ? 'The key ideas, methods and worked examples of every section, with “Try it” questions. Print it or read it before you start the unit.' : 'The key ideas of each video, the key words and “Think first” questions. Read a section before you watch its video.')),
        el('div', { class: 'btnrow', style: 'margin:0' }, hasNotes() ? el('button', { class: 'btn primary small', type: 'button', id: 'readSite', onclick: () => openReader(C.sections[0].id) }, '📖 Read on screen') : null,
          el('a', { class: 'btn small', id: 'readPdf', href: C.unit.read, target: '_blank', rel: 'noopener', download: '', onclick: () => Backend.track('read_pdf', { learner: st.id, unit: Core.UNIT }) }, '⬇ Download PDF'))) : null,
      learningPath(), examBlock(), Core.IS_MATHS ? challengeCard() : null].filter(Boolean));
    m.append(el('div', { class: 'u4two' },
      el('section', { class: 'card' }, el('h2', { style: 'margin:0;font-size:22px' }, 'What you will learn'), el('span', { class: 'muted' }, `${sec} of ${nobj} secure`),
        el('ul', { class: 'u4objs objs' }, ...Object.entries(C.objectives).map(([k, o]) => el('li', { class: objSecure(k) ? 'ok' : '' }, o.t)))),
      el('section', { class: 'card' }, el('h2', { style: 'margin:0;font-size:22px' }, 'Concept map'), el('span', { class: 'muted' }, C.sections[0] && C.sections[0].lesson ? 'Tap a box to see its lesson and questions' : 'Tap a box to see its video and questions'),
        el('div', { class: 'u4map' }, mindmapSvg(false)), el('a', { class: 'btn small', href: '#map' }, 'Open the interactive map', el('span', { class: 'arr' }, ' →')))));
  }
  /* ---------- lesson: video with pause questions ---------- */
  let activeVideo = null;
  function viewVideo(sid, watch) {
    let s = Core.sec(sid); const m = $main(); if (!s) return go('home');
    if (s.lesson && !(watch && s.lv)) return viewLesson(sid);
    // a Maths lesson's video: the same check questions, asked as pause questions at the video's own times
    if (s.lesson) s = Object.assign({}, s, { lesson: null, video: s.lv, captions: s.lv.captions, stops: s.stops.map(x => Object.assign({}, x, { t: s.lv.times[x.id] })) });
    const lock = Core.secLock(st, s);
    subbar('', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}: ${C.unit.title}`), el('span', { class: 'sep' }), el('span', { class: 'ttl' }, `Lesson ${s.id} · ${s.title}`));
    if (lock) { m.append(bar(`Section ${s.id} · Video`), lockScreen(`Section ${s.id} is locked`, lock.reason, [lock])); return; }
    const xp0 = Core.xp(st); const gchip = el('span', { class: 'gchip', html: FLAME + ` ${Core.streak(st)}-day streak` });
    document.querySelector('#sub .subbar-in').append(gchip);
    const bumpXp = () => { const e = document.getElementById('lessonXp'); if (e) e.textContent = Core.xp(st) - xp0; xpTick(); };
    st.last = { route: 'v-' + R(sid) }; Core.persist();
    const vs = Core.vstate(st, sid); const review = () => Core.videoDone(st, s);
    const v = el('video', { playsinline: true, preload: 'auto', poster: s.video.poster || null, 'aria-label': `Lesson ${s.id} video` }); activeVideo = v;
    v.addEventListener('play', () => { if (!v._started) { v._started = true; Backend.track('video_start', { learner: st.id, unit: Core.UNIT, sec: sid }); } });
    const player = el('div', { class: 'player' }, v);
    // the pause question is answered on the video itself (also in full screen), so young learners never have to leave the picture
    const qlayer = el('div', { class: 'qlayer', hidden: true, role: 'dialog', 'aria-modal': 'false', 'aria-label': 'Pause question' });
    const big = el('button', { class: 'bigplay', type: 'button', 'aria-label': 'Play lesson' }, svgI(I.play, 34, '#1C2A3A', 0)); big.querySelector('path').setAttribute('fill', '#1C2A3A'); player.append(big);
    const panel = el('div', { class: 'stoppanel', 'aria-live': 'polite' });
    const ppBtn = el('button', { class: 'btn primary small pp', type: 'button', 'aria-label': 'Play' }, svgI(I.play, 16, '#fff', 0)); ppBtn.querySelector('path').setAttribute('fill', '#fff');
    const fill = el('div', { class: 'fill' }); const track = el('div', { class: 'track', role: 'slider', tabindex: '0', 'aria-label': 'Video position', 'aria-valuemin': 0, 'aria-valuemax': Math.round(s.video.dur) }, fill);
    const time = el('span', { class: 'time' }, `0:00 / ${fmt(s.video.dur)}`);
    const spd = el('button', { class: 'chip', type: 'button', 'aria-label': 'Playback speed' }, UI.speed + '×');
    const cc = el('button', { class: 'chip' + (UI.cc ? ' on' : ''), type: 'button', 'aria-pressed': String(UI.cc) }, 'CC');
    const fs = el('button', { class: 'chip', type: 'button', 'aria-label': 'Full screen' }, svgI(I.full, 16));
    const ctrl = el('div', { class: 'card ctrl' }, ppBtn, track, time, spd, cc, fs);
    const capP = el('p', { class: 'cap', hidden: !UI.cc }); const capT = el('span'); capP.append(el('b', {}, 'Narrator: '), capT);
    let openStop = null, lastSave = 0, segEnd = null;
    player.append(qlayer);
    const wrap = el('div', { class: 'pwrap' }, player, ctrl);
    const lessonMain = el('section', { class: 'main' }, wrap, panel, capP);
    // on a normal page the player grows so the whole question fits without scrolling inside the video
    let qro = null; const fitQ = () => { const b = qlayer.firstChild; player.style.minHeight = ''; if (!b || isFs()) return; const need = b.scrollHeight + 36; if (need > player.clientHeight) player.style.minHeight = need + 'px'; };
    const closeQ = () => { qlayer.innerHTML = ''; qlayer.hidden = true; player.classList.remove('qopen'); player.style.minHeight = ''; if (qro) { qro.disconnect(); qro = null; } };
    const watchQ = () => { if (qro) qro.disconnect(); if (window.ResizeObserver && qlayer.firstChild) { qro = new ResizeObserver(() => fitQ()); qro.observe(qlayer.firstChild); } fitQ(); };
    const isFs = () => !!(document.fullscreenElement || document.webkitFullscreenElement) || wrap.classList.contains('fakefs');
    const fsIcon = () => { fs.innerHTML = ''; fs.append(isFs() ? el('span', { style: 'font-weight:800;font-size:15px' }, '✕ Exit full screen') : svgI(I.full, 16)); fs.setAttribute('aria-label', isFs() ? 'Exit full screen' : 'Full screen'); };
    const readAloud = q => { try { const ss = window.speechSynthesis; if (!ss) return; ss.cancel(); const txt = [q.prompt].concat((q.options || []).map((o, i) => String.fromCharCode(65 + i) + '. ' + o.t)).join('. ').replace(/<[^>]+>/g, ' '); const u = new SpeechSynthesisUtterance(txt); u.lang = 'en-GB'; u.rate = 0.85; const vv = ss.getVoices().find(x => /en-GB/i.test(x.lang)); if (vv) u.voice = vv; ss.speak(u); } catch (e) { } };
    // side panel: chapters / transcript / notes
    const tabsBox = el('div', { class: 'tabs', role: 'tablist', 'aria-label': 'Lesson panel' });
    const sideBody = el('div', { class: 'card', style: 'padding:14px' });
    const side = el('aside', { class: 'side' }, tabsBox, sideBody,
      el('div', { class: 'card', style: 'padding:18px 20px' }, el('b', { class: 'lex' }, 'This lesson\'s objectives'), el('ul', { style: 'margin:6px 0 0;padding-left:18px;font-size:15px' }, ...s.objs.map(o => el('li', {}, C.objectives[o].t)))),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn small', href: '#map' }, '🧠 Mind map'), el('a', { class: 'btn small', href: '#ws-' + R(sid) }, '📄 Worksheet')),
      el('div', { class: 'goal' }, el('span', { class: 'gi' }, svgI(I.bulb, 16, '#1C2A3A', 2)), el('span', {}, el('b', {}, 'Daily goal: '), `this video lasts ${fmt(s.video.dur)} with ${s.stops.length} pause questions – finish it to keep your streak going.`)));
    m.append(bar(`Unit ${Core.UNO} › ${s.id} › Video`), tocBtn(), el('div', { class: 'lesson' }, lessonMain, side));
    const drawSide = () => {
      tabsBox.innerHTML = ''; [['chapters', 'Chapters'], ['transcript', 'Transcript'], ['words', '⭐ Words'], ['notes', 'My notes']].forEach(([k, t]) => tabsBox.append(el('button', { type: 'button', role: 'tab', 'aria-selected': String(UI.side === k), class: UI.side === k ? 'on' : '', onclick: () => { UI.side = k; drawSide(); } }, t)));
      sideBody.innerHTML = ''; const t = v.currentTime || 0;
      if (UI.side === 'chapters') {
        const items = s.chapters.map(c => ({ t: c[0], label: c[1], kind: 'ch' })).concat(s.stops.map((x, i) => ({ t: x.t, label: x.kind === 'say' ? `🎤 Say “${x.q.word}”` : `Pause question ${i + 1}`, kind: 'stop', x }))).sort((a, b) => a.t - b.t);
        items.forEach((c, i) => { const nextT = (items[i + 1] || { t: s.video.dur }).t; const done = c.kind === 'stop' ? Core.stopDone(st, sid, c.x) : t >= nextT - 0.2 || review(); const cur = !done && t >= c.t - 0.2;
          sideBody.append(el('button', { type: 'button', class: 'chap' + (done ? ' done' : '') + (cur ? ' cur' : '') + (c.kind === 'stop' ? ' stopq' : ''), onclick: () => { segEnd = null; v.currentTime = c.t + (c.kind === 'stop' ? 0 : 0.01); } },
            el('span', { class: 'dt' }, done ? '✓' : c.kind === 'stop' ? '?' : String(s.chapters.findIndex(h => h[0] === c.t) + 1)), el('span', { style: 'flex:1' }, el('b', { style: 'font-size:15px' }, c.label), el('br'), el('small', { class: 'muted' }, fmt(c.t))))); });
      } else if (UI.side === 'transcript') {
        const box = el('div', { class: 'trans' }); s.captions.forEach((c, i) => { const nt = (s.captions[i + 1] || [s.video.dur])[0]; box.append(el('p', { class: t >= c[0] && t < nt ? 'cur' : '', onclick: () => { v.currentTime = c[0]; } }, el('code', {}, fmt(c[0])), ' ' + c[1])); }); sideBody.append(box);
      } else if (UI.side === 'words') {
        sideBody.append(el('p', { class: 'muted', style: 'margin:0 0 8px;font-size:14px' }, 'Tap ☆ to keep a word in My word book, so you can practise it later.'));
        const lw = el('div', { class: 'wside' }); (s.vocab || []).forEach(vv => lw.append(el('div', { class: 'wsrow' }, el('button', { type: 'button', class: 'wsplay', 'aria-label': 'Listen: ' + vv.w, onclick: () => Words.say(vv) }, el('span', { class: 'we' }, vv.emoji || '🔤'), el('b', {}, vv.w)), Words.star(vv, sid))));
        Words.list().filter(x => x.custom && x.sec === sid).forEach(x => lw.append(el('div', { class: 'wsrow' }, el('span', { class: 'wsplay' }, el('span', { class: 'we' }, x.emoji || '📝'), el('b', {}, x.w)), el('span', { class: 'muted' }, 'my word'))));
        sideBody.append(lw, Words.addForm(sid, () => drawSide()), el('a', { class: 'btn small', href: '#words', style: 'margin-top:8px' }, `📒 Open My word book (${Words.count()})`));
      } else {
        st.notes = st.notes || {}; const ta = el('textarea', { rows: 8, 'aria-label': 'My notes', placeholder: 'e.g. Root hair cell – long extension → bigger surface area → absorbs water faster.' }); ta.value = st.notes[sid] || '';
        const ok = el('span', { class: 'muted' }); ta.oninput = () => { st.notes[sid] = ta.value; Core.persist(); ok.textContent = 'Saved'; };
        sideBody.append(el('label', { style: 'display:flex;flex-direction:column;gap:6px;font-weight:700;font-size:14px' }, `My notes for ${s.id}`, ta), ok);
      }
    };
    const drawMarks = () => { track.querySelectorAll('.mk').forEach(x => x.remove()); s.stops.forEach((x, i) => { const d = Core.stopDone(st, sid, x); track.append(el('button', { class: 'mk' + (x.kind === 'say' ? ' say' : '') + (d ? ' done' : ''), type: 'button', style: `left:${x.t / s.video.dur * 100}%`, title: `${x.kind === 'say' ? 'Say the word' : 'Pause question'} ${i + 1} · ${fmt(x.t)}`, 'aria-label': `${x.kind === 'say' ? 'Say the word' : 'Pause question'} ${i + 1} at ${fmt(x.t)}${d ? ' (answered)' : ''}`, onclick: e => { e.stopPropagation(); if (d || review()) { v.pause(); v.currentTime = x.t; showStop(x, true); } } }, String(i + 1))); }); };
    const next = () => s.stops.find(x => !Core.stopDone(st, sid, x));
    const syncUi = () => { const t = v.currentTime || 0; fill.style.width = (t / s.video.dur * 100) + '%'; time.textContent = `${fmt(t)} / ${fmt(s.video.dur)}`; track.setAttribute('aria-valuenow', Math.round(t));
      const playing = !v.paused; ppBtn.innerHTML = ''; const ic = svgI(playing ? I.pause : I.play, 22, '#fff', 0); ic.querySelector('path').setAttribute('fill', '#fff'); ppBtn.append(ic); ppBtn.setAttribute('aria-label', playing ? 'Pause' : 'Play');
      big.hidden = playing || !!openStop; player.classList.toggle('paused-q', !!openStop);
      const c = s.captions.filter(x => x[0] <= t + 0.05).pop(); capT.textContent = c ? c[1] : ''; };
    function showStop(x, again) {
      openStop = again ? null : x; panel.innerHTML = ''; const i = s.stops.indexOf(x);
      if (!again) { vs.pos = x.t; Core.persist(); }
      const rec = (vs.stops[x.id] = vs.stops[x.id] || { tries: 0 });
      const box = el('section', { class: 'card stop' + (Core.IS_PRIMARY ? ' kid' : '') }, el('div', { class: 'stopbar' }, el('span', { class: 'eyebrow' }, `${Core.IS_PRIMARY ? '🤔' : '⏸'} QUESTION ${i + 1} OF ${s.stops.length}`),
        el('span', { class: 'sbtns' }, ('speechSynthesis' in window) ? el('button', { class: 'btn small ghost readme', type: 'button', onclick: () => readAloud(x.q) }, '🔊 Read to me') : null,
          el('button', { class: 'btn small ghost', type: 'button', onclick: () => { closeQ(); segEnd = null; v.currentTime = x.review[0]; v.play().catch(() => { }); } }, '↺ Watch again'))));
      const qh = el('div'); box.append(qh); qlayer.innerHTML = ''; qlayer.append(box); qlayer.hidden = false; player.classList.add('qopen'); setTimeout(watchQ, 0);
      if (again && rec.done) {
        QE.practice(x.q, qh, { rec: {}, seed: st.id, save: () => { }, onDone: () => { } });
        box.append(el('button', { class: 'btn primary big', type: 'button', onclick: () => { closeQ(); v.play().catch(() => { }); } }, 'Close & keep watching ▶'));
        return;
      }
      QE.practice(x.q, qh, { rec, seed: st.id, save: () => { Core.persist(); }, onCheck: onCheck(box, x.q, rec),
        onDone: () => {
          rec.done = true; if (rec.everWrong) st.stopsWrong[x.q.id] = true; Core.persist(); openStop = null; drawMarks(); drawSide(); bumpXp(); syncUi();
          const cont = el('button', { class: 'btn primary big shine', type: 'button', id: 'continueVideo', onclick: () => { closeQ(); try { window.speechSynthesis && speechSynthesis.cancel(); } catch (e) { } v.currentTime = x.t; v.play().catch(() => { }); } }, '▶ Keep watching');
          box.append(el('div', { class: 'controw' }, cont)); setTimeout(() => { try { cont.focus({ preventScroll: true }); box.scrollTop = box.scrollHeight; } catch (e) { } }, 60);
        } });
      v.pause(); syncUi(); drawSide();
      if (!isFs()) setTimeout(() => wrap.scrollIntoView({ block: 'nearest', behavior: 'smooth' }), 50);
    }
    function complete(opened) {   // opened: the page was opened on a finished video (no countdown then)
      if (next()) return; if (!vs.completed) { vs.completed = true; Core.persist(); bumpXp(); Backend.track('video_complete', { learner: st.id, unit: Core.UNIT, sec: sid }); }
      panel.innerHTML = ''; panel.append(el('section', { class: 'card done' }, el('h3', {}, `✓ Lesson ${s.id} complete`),
        el('p', { style: 'margin:0 0 10px' }, `Next: 30 practice questions (8 Core) for section ${s.id}. You can now skip freely through the video to revise.`),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn gold big shine', type: 'button', onclick: () => go('ex-' + R(sid)) }, `Practise ${s.id}`, el('span', { class: 'arr' }, '→')), s.lab ? el('a', { class: 'btn big', href: '#lab-' + R(sid) }, '🧪 Experiment room') : null)));
      refreshToc(); drawSide();
      // straight on to the practice: a short countdown, then the practice opens by itself (while the Core questions still need doing)
      if (!opened && Core.reqLeft(st, s).length && !s.lesson) {
        const route = location.hash; let n = 5; const lbl = el('b', {}, String(n));
        const cd = el('div', { class: 'banner info autogo', id: 'autoPractice' }, '▶ Practice starts in ', lbl, ' …', el('button', { type: 'button', class: 'btn small', onclick: () => { clearInterval(t); cd.remove(); } }, 'Stay here'));
        panel.querySelector('.card.done').append(cd);
        const t = setInterval(() => { if (location.hash !== route) { clearInterval(t); return; } n--; lbl.textContent = String(n); qlayer.querySelectorAll('.autogo b').forEach(x => x.textContent = String(n));
          if (n <= 0) { clearInterval(t); if (isFs()) fs.click(); closeQ(); go('ex-' + R(sid)); } }, 1000);
        if (isFs()) { qlayer.innerHTML = ''; qlayer.hidden = false; player.classList.add('qopen');
          qlayer.append(el('section', { class: 'card stop done kid' }, el('h3', { style: 'font-size:28px;margin:0 0 8px' }, '🎉 Well done! Lesson complete'),
            el('p', { class: 'autogo', style: 'font-size:20px' }, 'Practice starts in ', el('b', {}, String(n)), ' …'),
            el('div', { class: 'btnrow' }, el('button', { class: 'btn gold big shine', type: 'button', onclick: () => { clearInterval(t); fs.click(); closeQ(); go('ex-' + R(sid)); } }, `Practise now →`),
              el('button', { class: 'btn big', type: 'button', onclick: () => { clearInterval(t); cd.remove(); fs.click(); closeQ(); } }, 'Stay here')))); }
        return;
      }
      if (isFs()) { qlayer.innerHTML = ''; qlayer.hidden = false; player.classList.add('qopen');
        qlayer.append(el('section', { class: 'card stop done kid' }, el('h3', { style: 'font-size:28px;margin:0 0 8px' }, '🎉 Well done! Lesson complete'),
          el('div', { class: 'btnrow' }, el('button', { class: 'btn gold big shine', type: 'button', onclick: () => { fs.click(); closeQ(); go('ex-' + R(sid)); } }, `Practise ${s.id} →`),
            el('button', { class: 'btn big', type: 'button', onclick: () => { fs.click(); closeQ(); } }, 'Exit full screen')))); }
    }
    const nudge = () => { const b = qlayer.querySelector('.stop'); if (b) { b.classList.remove('pulse'); void b.offsetWidth; b.classList.add('pulse'); } };
    const togglePlay = () => { if (openStop) { nudge(); return; } if (v.paused) v.play().catch(() => { }); else v.pause(); };
    ppBtn.onclick = togglePlay; big.onclick = togglePlay;
    track.addEventListener('click', e => { const r = track.getBoundingClientRect(); segEnd = null; v.currentTime = Math.max(0, Math.min(1, (e.clientX - r.left) / r.width)) * s.video.dur; });
    track.addEventListener('keydown', e => { if (e.key === 'ArrowRight') v.currentTime = Math.min(s.video.dur, v.currentTime + 5); if (e.key === 'ArrowLeft') v.currentTime = Math.max(0, v.currentTime - 5); if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); togglePlay(); } });
    spd.onclick = () => { UI.speed = UI.speed === 1 ? 1.25 : UI.speed === 1.25 ? 1.5 : UI.speed === 1.5 ? 2 : 1; v.playbackRate = UI.speed; spd.textContent = UI.speed + '×'; };
    cc.onclick = () => { UI.cc = !UI.cc; capP.hidden = !UI.cc; cc.classList.toggle('on', UI.cc); cc.setAttribute('aria-pressed', String(UI.cc)); };
    // full screen covers the video, its controls and the question layer; where the browser cannot (iPhone), the page fakes it
    fs.onclick = () => {
      if (isFs()) { if (wrap.classList.contains('fakefs')) { wrap.classList.remove('fakefs'); document.body.classList.remove('nofscroll'); } else (document.exitFullscreen || document.webkitExitFullscreen).call(document); fsIcon(); return; }
      const req = wrap.requestFullscreen || wrap.webkitRequestFullscreen;
      if (req) { try { const r = req.call(wrap); if (r && r.catch) r.catch(() => { wrap.classList.add('fakefs'); document.body.classList.add('nofscroll'); fsIcon(); }); } catch (e) { wrap.classList.add('fakefs'); document.body.classList.add('nofscroll'); } }
      else { wrap.classList.add('fakefs'); document.body.classList.add('nofscroll'); }
      fsIcon(); };
    ['fullscreenchange', 'webkitfullscreenchange'].forEach(ev => document.addEventListener(ev, () => { if (document.body.contains(wrap)) { fsIcon(); fitQ(); } }));
    v.addEventListener('loadedmetadata', () => {
      v.playbackRate = UI.speed; let t0 = vs.pos || 0;
      if (UI.seek && UI.seek.sec === sid) { t0 = UI.seek.from; segEnd = UI.seek.to; UI.seek = null; panel.append(el('div', { class: 'banner info' }, `▶ Review clip ${fmt(t0)}–${fmt(segEnd)} – press play to watch.`)); }
      const nx = next();
      if (!review() && nx && t0 >= nx.t - 0.3) { v.currentTime = nx.t; showStop(nx); } else v.currentTime = Math.min(t0, s.video.dur - 0.5);
      if (vs.completed && !nx) complete(true);
      syncUi();
    });
    let lastSide = 0;
    v.addEventListener('timeupdate', () => {
      const t = v.currentTime;
      if (!review()) { const nx = next(); if (nx && t >= nx.t - 0.04 && openStop !== nx) { v.pause(); v.currentTime = nx.t; showStop(nx); } }
      if (segEnd != null && t >= segEnd) { v.pause(); segEnd = null; }
      if (Date.now() - lastSave > 2000) { vs.pos = t; lastSave = Date.now(); Core.persist(); }
      if (Date.now() - lastSide > 1500 && UI.side !== 'notes' && UI.side !== 'words') { lastSide = Date.now(); drawSide(); }
      if (!next() && t >= s.video.dur - 0.6 && !vs.completed) complete();
      syncUi();
    });
    v.addEventListener('seeking', () => {
      if (review()) return; const nx = next();
      if (nx && v.currentTime > nx.t + 0.05) { v.currentTime = nx.t; if (openStop !== nx) showStop(nx); }
    });
    v.addEventListener('play', () => { if (openStop) { v.pause(); nudge(); } else if (!qlayer.hidden) closeQ(); syncUi(); });
    v.addEventListener('pause', () => { vs.pos = v.currentTime; Core.persist(); syncUi(); });
    v.addEventListener('ended', () => complete());
    v.addEventListener('click', togglePlay);
    let triedBlob = false;
    v.addEventListener('error', async () => { if (triedBlob) return; triedBlob = true; try { const b = await (await fetch(s.video.src)).blob(); v.src = URL.createObjectURL(b); } catch (e) { panel.append(el('p', { class: 'err' }, 'The video could not be loaded.')); } });
    v.src = s.video.src; drawMarks(); drawSide(); syncUi();
  }

  /* ---------- lesson notes reader: the whole unit's notes on the site (the same content as the PDF reading pack).
     Opens at a section, zoom, full screen, remembers where each learner stopped; an overlay, so Practice answers stay as typed. ---------- */
  let READIDX = null;
  async function readIndex() { if (!READIDX) { try { READIDX = await (await fetch('media/read/index.json')).json(); } catch (e) { READIDX = {}; } } return READIDX; }
  const hasNotes = () => !!(C && C.sections && C.sections.some(s => (s.lesson || []).length));
  /* lesson blocks (Maths notes v3 + v4). v4 adds: hook (Start here), recall (Remember), try (Your turn, a live question),
     error (Spot the mistake: a wrong solution, find the first wrong line), summary (Key points); worked examples can say
     what we know / what we need / the plan, put a diagram next to a step, and end with a check. */
  const LB_KIND = { idea: 'Key idea', example: 'Worked example', tip: 'Exam tip', mistake: 'Common mistake', method: 'Method', hook: 'Start here', recall: 'Remember', try: 'Your turn', error: 'Spot the mistake', summary: 'Key points' };
  const LB_ICON = { idea: '💡', example: '✏️', tip: '✅', mistake: '⚠️', method: '🧭', hook: '🚀', recall: '🔁', try: '🖊️', error: '🔍', summary: '📌' };
  const rich = t => String(t).split(/(\*\*[^*]+\*\*)/).map(part => /^\*\*.*\*\*$/.test(part) ? el('b', {}, part.slice(2, -2)) : part);
  const figEl = f => { const g = f && window.AtomicFig && window.AtomicFig.get ? window.AtomicFig.get(f.kind, f) : null; return g ? el('div', { class: 'qfig', html: g.svg }) : null; };
  // the "Spot the mistake" question: which line is the first wrong one?
  const errQ = (b, id) => ({ id, type: 'mcq', fixed: true, prompt: 'Which line is the first one that is wrong?', hint: b.hint || 'Check each line in turn. Does it follow from the line before it?',
    options: b.lines.map((_, i) => ({ t: 'Line ' + (i + 1), ok: i === b.bad, fb: i < b.bad ? `Line ${i + 1} is correct. Read on.` : i > b.bad ? 'This line is wrong, but the mistake starts earlier.' : '' })), reason: b.why });
  // fill a lesson card. live(q, host, after) shows a question the learner can answer (lesson page); without it the answer is printed (notes reader).
  function fillBlock(card, b, live) {
    if (b.k === 'summary') card.append(el('ul', { class: 'lsum' }, ...(b.p || []).map(t => el('li', {}, ...rich(t)))));
    else (b.p || []).forEach(t => card.append(el('p', { class: 'lp' }, ...rich(t))));
    if (b.fig) { const f = figEl(b.fig); if (f) card.append(f); }
    if (b.table) card.append(QE.dataTable ? QE.dataTable(b.table) : el('div'));
    (b.p2 || []).forEach(t => card.append(el('p', { class: 'lp' }, ...rich(t))));   // text that comes after the table or diagram
    if (b.q) card.append(el('p', { class: 'lq' }, el('b', {}, b.k === 'error' ? 'Problem: ' : 'Question: '), ...rich(b.q)));
    if (b.given || b.find || b.plan) card.append(el('dl', { class: 'lgf' }, ...[['What we know', b.given], ['What we need', b.find], ['Plan', b.plan]].filter(x => x[1]).flatMap(([k, v]) => [el('dt', {}, k), el('dd', {}, ...rich(v))])));
    if (b.steps) { const ol = el('ol', { class: 'lsteps' }); b.steps.forEach(([work, why, fig]) => ol.append(el('li', {}, el('code', { class: 'mwork' }, work), why ? el('span', { class: 'why' }, ' ', ...rich(why)) : null, fig ? figEl(fig) : null))); card.append(ol); }
    if (b.a) card.append(el('p', { class: 'lans' }, el('b', {}, 'Answer: '), ...rich(b.a)));
    if (b.check) card.append(el('p', { class: 'lchk' }, el('b', {}, '✓ Check: '), ...rich(b.check)));
    if (b.k === 'error' && b.lines) {
      card.append(el('ol', { class: 'lerrlines' }, ...b.lines.map((t, i) => el('li', {}, el('span', { class: 'ln' }, 'Line ' + (i + 1)), el('code', { class: 'mwork' }, t)))));
      const fix = el('div', { class: 'lfix' }, el('b', {}, 'Why it is wrong: '), ...rich(b.why || ''),
        b.fix ? el('ol', { class: 'lsteps' }, ...b.fix.map(([w, y]) => el('li', {}, el('code', { class: 'mwork' }, w), y ? el('span', { class: 'why' }, ' ', ...rich(y)) : null))) : null);
      if (live) { const host = el('div', { class: 'ltry' }); card.append(host); fix.hidden = true; card.append(fix); live(errQ(b, b.id), host, () => { fix.hidden = false; }); }
      else card.append(el('p', { class: 'lp' }, el('b', {}, 'The first wrong line: '), 'Line ' + (b.bad + 1)), fix);
    }
    if (b.qq) {
      if (live) { const host = el('div', { class: 'ltry' }); card.append(host); live(b.qq, host); }
      else card.append(el('div', { class: 'rdtry' }, el('b', {}, 'Try it: '), ...rich(b.qq.prompt), el('details', {}, el('summary', {}, 'Answer'), el('p', {}, QE.answerText ? QE.answerText(b.qq) : ''), b.qq.reason ? el('p', { class: 'muted' }, b.qq.reason) : null)));
    }
    return card;
  }
  /* ---------- Read the PDF: the course book pages for a lesson, shown on Camday (page images, so they are sharp on phones).
     s.pdf = [{book, p0, p1, label, note, look:[…]}]; p0–p1 are pages of the book file (the printed page numbers are in the label).
     The viewer opens at the lesson's pages; the whole book can be read; zoom and full screen; an overlay, so Practice answers stay. ---------- */
  let BOOKS = null;
  async function bookIndex() { if (!BOOKS) { try { BOOKS = await (await fetch('media/books/index.json', { cache: 'no-cache' })).json(); } catch (e) { BOOKS = {}; } } return BOOKS; }
  const bookPage = (bk, n) => `${bk.dir}p${String(n).padStart(4, '0')}.${bk.ext || 'webp'}${bk.v ? '?v=' + bk.v : ''}`;   // v changes with every rebuild, so browsers never show old pages
  async function openBook(s, ref) {
    ref = ref || s.pdf[0]; const idx = await bookIndex(), bk = idx[ref.book];
    if (!bk) { toast('This book is not available yet.'); return; }
    const vs = Core.vstate(st, s.id); vs.pdf = true; Core.persist();
    const key = `atomic.book.${st ? st.id : 'guest'}.${ref.book}`; let saved = null; try { saved = JSON.parse(localStorage.getItem(key) || 'null'); } catch (e) { }
    let page = ref.p0, zoom = (saved && saved.zoom) || (window.innerWidth < 600 ? 1.6 : 1);   // phones open zoomed in, so the text is readable
    const img = el('img', { class: 'bkimg', alt: '', id: 'bookImg' }), wrap = el('div', { class: 'bkbody', id: 'bookBody' }, img);
    const ov = el('div', { class: 'rdover bkover', role: 'dialog', 'aria-modal': 'true', 'aria-label': bk.title, id: 'book' });
    const pg = el('input', { type: 'number', min: 1, max: bk.pages, class: 'bkpg', id: 'bookPage', 'aria-label': 'Page of the book file', onchange: () => show(+pg.value) });
    const inLesson = n => n >= ref.p0 && n <= ref.p1;
    const where = el('span', { class: 'bkwhere', id: 'bookWhere' });
    const close = () => { try { if (document.fullscreenElement) document.exitFullscreen(); } catch (e) { } ov.remove(); document.removeEventListener('keydown', keys); };
    const keys = e => { if (e.key === 'Escape') close(); else if (e.key === 'ArrowRight') show(page + 1); else if (e.key === 'ArrowLeft') show(page - 1); };
    const setZoom = z => { zoom = Math.max(1, Math.min(3, z)); img.style.width = `min(${zoom * 100}%, ${Math.round(980 * zoom)}px)`; save(); };   // never wider than the page was drawn for, so it stays sharp
    function save() { try { localStorage.setItem(key, JSON.stringify({ page, zoom })); } catch (e) { } }
    function show(n) { page = Math.max(1, Math.min(bk.pages, n || 1)); img.src = bookPage(bk, page); img.alt = `${bk.title}, page ${page} of the file`; pg.value = page;
      where.textContent = inLesson(page) ? `Lesson pages (${ref.label})` : 'Outside this lesson\'s pages'; where.className = 'bkwhere' + (inLesson(page) ? ' on' : ''); wrap.scrollTop = 0; save();
      if (page < bk.pages) { const pre = new Image(); pre.src = bookPage(bk, page + 1); } }
    const bar = el('div', { class: 'rdbar' }, el('b', { class: 'rdttl' }, '📄 ' + bk.title),
      el('button', { type: 'button', class: 'btn small ghost', id: 'bookPrev', 'aria-label': 'Previous page', onclick: () => show(page - 1) }, '←'), pg, el('span', { class: 'muted' }, `/ ${bk.pages}`),
      el('button', { type: 'button', class: 'btn small ghost', id: 'bookNext', 'aria-label': 'Next page', onclick: () => show(page + 1) }, '→'),
      el('button', { type: 'button', class: 'btn small ghost', id: 'bookLesson', onclick: () => show(ref.p0) }, 'Lesson pages'), where,
      el('span', { class: 'rdz' }, el('button', { type: 'button', class: 'btn small ghost', 'aria-label': 'Zoom out', id: 'bookSmall', onclick: () => setZoom(zoom - 0.25) }, '−'), el('button', { type: 'button', class: 'btn small ghost', 'aria-label': 'Zoom in', id: 'bookBig', onclick: () => setZoom(zoom + 0.25) }, '+')),
      el('button', { type: 'button', class: 'btn small ghost', id: 'bookFull', onclick: () => { try { document.fullscreenElement ? document.exitFullscreen() : ov.requestFullscreen(); } catch (e) { } } }, '⛶ Full screen'),
      el('button', { type: 'button', class: 'btn small primary', id: 'bookClose', onclick: close }, '✕ Close'));
    const guide = el('div', { class: 'bkguide' }, el('b', {}, `Read ${ref.label}. `), ref.note ? rich(ref.note) : null, ...(ref.look || []).map(t => el('p', { class: 'bklook' }, '👀 ', ...rich(t))));
    ov.append(bar, guide, wrap); document.body.append(ov); document.addEventListener('keydown', keys); setZoom(zoom); show(ref.p0);
  }
  // the lesson document at the top of the lesson: its pages one at a time, sharp on every screen; full screen opens the whole book
  function docPanel(s) {
    const ref = s.pdf[0], vs = Core.vstate(st, s.id); let page = ref.p0, bk = null;
    const n = ref.p1 - ref.p0 + 1, img = el('img', { class: 'docimg', id: 'docImg', alt: '' }), cnt = el('span', { class: 'docpg', id: 'docPg' });
    const prev = el('button', { type: 'button', class: 'btn small ghost', id: 'docPrev', 'aria-label': 'Previous page', onclick: () => show(page - 1) }, '← Previous');
    const next = el('button', { type: 'button', class: 'btn small ghost', id: 'docNext', 'aria-label': 'Next page', onclick: () => show(page + 1) }, 'Next →');
    const view = el('div', { class: 'docview' }, img);
    const tog = el('button', { type: 'button', class: 'btn small ghost', id: 'docToggle', 'aria-expanded': 'true' }, 'Hide');
    const nav = el('div', { class: 'docnav' }, prev, cnt, next);
    const box = el('section', { class: 'card docpanel', id: 'docPanel' },
      el('div', { class: 'dochead' }, el('div', {}, el('span', { class: 'eyebrow' }, 'LESSON DOCUMENT'), el('h2', {}, `${ref.title || 'Camday Maths'}, ${ref.label}`)),
        el('div', { class: 'btnrow' }, el('button', { type: 'button', class: 'btn small', id: 'docFull', onclick: () => openBook(s, Object.assign({}, ref, { p0: page })) }, '⛶ Full screen · whole book'), tog)),
      ref.note ? el('p', { class: 'docnote' }, ...rich(ref.note)) : null,
      ...(ref.look || []).map(t => el('p', { class: 'bklook' }, '👀 ', ...rich(t))), nav, view);
    const setOpen = o => { view.hidden = !o; nav.hidden = !o; tog.textContent = o ? 'Hide' : 'Show the document'; tog.setAttribute('aria-expanded', String(o)); vs.docShut = !o; Core.persist(); };
    tog.onclick = () => setOpen(view.hidden);
    function show(k) { if (!bk) return; page = Math.max(ref.p0, Math.min(ref.p1, k)); img.src = bookPage(bk, page); img.alt = `${ref.title}, page ${page}`;
      cnt.textContent = `Page ${page - ref.p0 + 1} of ${n}`; prev.disabled = page === ref.p0; next.disabled = page === ref.p1;
      if (page !== ref.p0 && !vs.pdf) { vs.pdf = true; Core.persist(); } }
    bookIndex().then(idx => { bk = idx[ref.book]; if (!bk) { box.remove(); return; } show(ref.p0); if (vs.docShut) setOpen(false);
      if (bk.pdf) box.querySelector('.dochead .btnrow').prepend(el('a', { class: 'btn small', id: 'docPdf', href: bk.pdf + '#page=' + ref.p0, target: '_blank', rel: 'noopener' }, '⬇ PDF (print quality)')); });
    return box;
  }
  // "On this page": the parts of a v4 lesson in groups, to jump to
  function lessonToc(s) {
    const G = [['hook', 'Start'], ['recall', 'Remember'], ['idea', 'Ideas'], ['method', 'Method'], ['example', 'Examples'], ['try', 'Your turn'], ['error', 'Spot the mistake'], ['mistake', 'Tips'], ['tip', 'Tips'], ['summary', 'Key points']];
    const seen = {}, items = [];
    s.lesson.forEach((b, i) => { const g = (G.find(x => x[0] === b.k) || [b.k, 'Ideas'])[1]; if (seen[g] == null) { seen[g] = items.length; items.push({ g, i, n: 0 }); } items[seen[g]].n++; });
    return el('nav', { class: 'ltoc', 'aria-label': 'Parts of this lesson' }, el('span', { class: 'eyebrow' }, 'ON THIS PAGE'),
      ...items.map(x => el('button', { type: 'button', class: 'chip', onclick: () => { const t = document.getElementById('lb-' + x.i); if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' }); } }, x.g + (x.n > 1 ? ` · ${x.n}` : ''))));
  }
  function pdfCard(s) {
    const vs = Core.vstate(st, s.id), r = s.pdf[0];
    return el('section', { class: 'card lblock lb-pdf', id: 'readPdf' }, el('div', { class: 'lbtop' }, el('span', { class: 'lbkind' }, 'Next steps'), vs.pdf ? el('span', { class: 'lbcount' }, '✓ document read') : null),
      el('h2', {}, 'Read the document, then practise'),
      el('p', { class: 'lp' }, 'Read ', el('b', {}, r.label), ' of the lesson document at the top of this page (or full screen), and try its practice on paper.'),
      el('div', { class: 'btnrow', style: 'margin-top:8px' },
        el('button', { class: 'btn', type: 'button', id: 'openPdf0', onclick: () => openBook(s, r) }, '📄 Open the document'),
        el('button', { class: 'btn gold shine', type: 'button', id: 'startPractice', onclick: () => {
          if (Core.stopsLeft(st, s).length) { toast('Answer the check questions in the lesson first.'); return; }
          if (!vs.completed) { vs.completed = true; vs.pos = s.video.dur; Core.persist(); Backend.track('lesson_done', { learner: st.id, unit: Core.UNIT, sec: s.id }); }
          go('ex-' + R(s.id)); } }, 'Start practice', el('span', { class: 'arr' }, ' →'))),
      el('p', { class: 'muted', style: 'margin:8px 0 0' }, 'In Practice, “Review the PDF” opens the document again and keeps your answers.'));
  }

  function noteBlock(b) {
    const kind = b.k || 'idea';
    const card = el('div', { class: 'lblock lb-' + kind }, el('h3', {}, el('span', { class: 'lbi', 'aria-hidden': 'true' }, LB_ICON[kind] || '💡'), ' ', (['example', 'mistake', 'method', 'tip', 'hook', 'recall', 'try', 'error', 'summary'].includes(kind) ? LB_KIND[kind] + ': ' : '') + b.t));
    return fillBlock(card, b);
  }
  async function openReader(sid) {
    if (!hasNotes()) return;
    const key = `atomic.read.${st ? st.id : 'guest'}.${Core.UNIT}`; let saved = null; try { saved = JSON.parse(localStorage.getItem(key) || 'null'); } catch (e) { }
    const idx = (await readIndex()); const pk = C.unit.read ? String(C.unit.read).split('/').pop().replace(/\.pdf$/, '') : ''; const pages = (idx[pk] || {}).secs || {};
    let zoom = (saved && saved.zoom) || 1;
    const body = el('div', { class: 'rdbody', id: 'readerBody' });
    const ov = el('div', { class: 'rdover', role: 'dialog', 'aria-modal': 'true', 'aria-label': 'Lesson notes', id: 'reader' });
    const close = () => { save(); try { if (document.fullscreenElement) document.exitFullscreen(); } catch (e) { } ov.remove(); document.removeEventListener('keydown', esc); };
    const esc = e => { if (e.key === 'Escape') close(); };
    const setZoom = z => { zoom = Math.max(0.85, Math.min(1.8, z)); body.style.setProperty('--rz', zoom); save(); };
    const pdfLink = s0 => C.unit.read ? C.unit.read + (pages[s0] ? '#page=' + pages[s0][0] : '') : null;
    const sel = el('select', { class: 'rdsel', 'aria-label': 'Go to section', id: 'readerSec', onchange: () => jump(sel.value) }, ...C.sections.map(s => el('option', { value: s.id }, `${s.id} ${s.title}${pages[s.id] ? ` · pages ${pages[s.id][0]}–${pages[s.id][1]}` : ''}`)));
    const dl = el('a', { class: 'btn small ghost', id: 'readerPdf', target: '_blank', rel: 'noopener', href: pdfLink(sid) || '#' }, '⬇ PDF');
    const bar = el('div', { class: 'rdbar' }, el('b', { class: 'rdttl' }, `📖 Unit ${Core.UNO} notes`), sel,
      el('span', { class: 'rdz' }, el('button', { type: 'button', class: 'btn small ghost', 'aria-label': 'Smaller', id: 'readerSmall', onclick: () => setZoom(zoom - 0.15) }, 'A−'), el('button', { type: 'button', class: 'btn small ghost', 'aria-label': 'Bigger', id: 'readerBig', onclick: () => setZoom(zoom + 0.15) }, 'A+')),
      el('button', { type: 'button', class: 'btn small ghost', id: 'readerFull', onclick: () => { try { document.fullscreenElement ? document.exitFullscreen() : ov.requestFullscreen(); } catch (e) { } } }, '⛶ Full screen'),
      C.unit.read ? dl : null, el('button', { type: 'button', class: 'btn small primary', id: 'readerClose', onclick: close }, '✕ Close'));
    body.append(el('header', { class: 'rdhead' }, el('p', { class: 'eyebrow' }, `${Core.stageLabel()} · Unit ${Core.UNO}`), el('h1', {}, C.unit.title), C.unit.blurb ? el('p', { class: 'muted' }, C.unit.blurb) : null));
    C.sections.forEach(s => {
      const sec = el('section', { class: 'rdsec', id: 'rd-' + R(s.id), 'data-sid': s.id }, el('h2', {}, `${s.id} ${s.title}`, pages[s.id] ? el('small', { class: 'rdpg' }, `PDF pages ${pages[s.id][0]}–${pages[s.id][1]}`) : null));
      (s.stops || []).filter(x => x.after === -1).forEach(x => sec.append(el('div', { class: 'rdtry' }, el('b', {}, 'Try it: '), x.q.prompt)));
      (s.lesson || []).forEach((b, bi) => { sec.append(noteBlock(b)); (s.stops || []).filter(x => x.after === bi).forEach(x => sec.append(el('div', { class: 'rdtry' }, el('b', {}, 'Try it: '), x.q.prompt))); });
      body.append(sec);
    });
    ov.append(bar, body); document.body.append(ov); document.addEventListener('keydown', esc); setZoom(zoom);
    function cur() { const top = body.scrollTop + 80; let c = C.sections[0].id; body.querySelectorAll('.rdsec').forEach(x => { if (x.offsetTop <= top) c = x.dataset.sid; }); return c; }
    function save() { try { localStorage.setItem(key, JSON.stringify({ top: body.scrollTop, sid: cur(), zoom, at: Date.now() })); } catch (e) { } }
    function jump(s0) { const t = body.querySelector('#rd-' + R(s0)); if (t) body.scrollTop = t.offsetTop - 10; sel.value = s0; dl.href = pdfLink(s0) || '#'; }
    let tm = null; body.addEventListener('scroll', () => { clearTimeout(tm); tm = setTimeout(() => { const c = cur(); sel.value = c; dl.href = pdfLink(c) || '#'; save(); }, 200); });
    // first time for this section: open at its start; otherwise where the learner stopped (if that was in this section)
    requestAnimationFrame(() => { if (saved && saved.sid === sid && saved.top != null) { body.scrollTop = saved.top; sel.value = sid; } else jump(sid || C.sections[0].id); });
    Backend.track && Backend.track('notes_open', { learner: st && st.id, unit: Core.UNIT, sec: sid });
  }

  /* ---------- reading lesson (Mathematics): key ideas, worked examples and check questions, no video ---------- */
  function viewLesson(sid) {
    const s = Core.sec(sid), m = $main();
    const lock = Core.secLock(st, s);
    subbar('', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}: ${C.unit.title}`), el('span', { class: 'sep' }), el('span', { class: 'ttl' }, `Lesson ${s.id} · ${s.title}`));
    if (lock) { m.append(bar(`Section ${s.id} · Lesson`), lockScreen(`Section ${s.id} is locked`, lock.reason, [lock])); return; }
    st.last = { route: 'v-' + R(sid) }; Core.persist();
    const vs = Core.vstate(st, sid); const xp0 = Core.xp(st);
    const mins = Math.max(5, Math.round(s.video.dur / 60)), nIdeas = s.lesson.length;
    const lprog = el('div', { class: 'lprog', id: 'lessonProg' });
    const drawProg = () => { const left = Core.stopsLeft(st, s).length, got = s.stops.length - left, fin = vs.completed && !left; lprog.innerHTML = '';
      const step = (n, label, state) => el('span', { class: 'lstep ' + state }, el('i', {}, state === 'done' ? '✓' : String(n)), label);
      lprog.append(el('div', { class: 'lsteprow' }, step(1, 'Read the lesson', fin || got ? 'done' : 'cur'), step(2, `Check questions ${got}/${s.stops.length}`, !left ? 'done' : got ? 'cur' : ''), s.pdf && s.pdf.length ? step(3, 'Read the PDF', vs.pdf ? 'done' : !left ? 'cur' : '') : null, step(s.pdf && s.pdf.length ? 4 : 3, `Practise ${s.id}`, fin ? 'cur' : '')),
        el('div', { class: 'pbar' + (!left ? ' ok' : '') }, el('i', { style: `width:${s.stops.length ? Math.round(got / s.stops.length * 100) : 100}%` }))); };
    const head = el('section', { class: 'card lessonhead' }, el('p', { class: 'eyebrow', style: 'margin:0' }, `${Core.stageLabel()} · Unit ${Core.UNO} · Lesson ${s.id}`), el('h1', { style: 'margin:4px 0 10px' }, s.title),
      el('div', { class: 'lmeta' }, el('span', {}, `About ${mins} minutes`), el('span', {}, `${nIdeas} part${nIdeas === 1 ? '' : 's'}`), el('span', {}, `${s.stops.length} check question${s.stops.length === 1 ? '' : 's'}`)),
      el('div', { class: 'lgoalbox' }, el('span', { class: 'hl' }, 'In this lesson you will learn to'), el('ul', { class: 'lgoals' }, ...s.objs.map(o => el('li', {}, (C.objectives[o] || {}).t || o)))), lprog);
    m.append(head);
    const v4 = s.notes === 'v4';
    if (s.lv) m.append(el('a', { class: 'card lvideo', href: '#vw-' + R(sid), id: 'lessonVideo' }, el('span', { class: 'lvthumb', style: `background-image:url(${s.lv.poster})` }, el('span', { class: 'lp-play pulse', 'aria-hidden': 'true' }, svgI(I.play, 28, '#1C2A3A', 2.6))),
      el('span', {}, el('b', {}, 'Watch the video lesson'), el('small', {}, `${fmt(s.lv.dur)} · animated, with ${s.stops.length} pause questions and captions`))));
    if (s.pdf && s.pdf.length) m.append(docPanel(s));   // the lesson document comes first: easy to find and read
    if (v4) m.append(lessonToc(s));
    const body = el('div', { class: 'lessonbody' + (v4 ? ' v4' : '') }); m.append(body);
    const status = el('div'); m.append(status);
    const drawStatus = () => { drawProg(); status.innerHTML = ''; const left = Core.stopsLeft(st, s).length;
      if (vs.completed && !left) { const i = C.sections.indexOf(s), nxt = C.sections[i + 1];
        status.append(el('section', { class: 'card lchoose', id: 'lessonChoose' }, el('b', {}, `✓ Lesson ${s.id} finished. What next? You choose the order.`),
          el('div', { class: 'lchoices' },
            el('button', { class: 'lch', type: 'button', id: 'readNotes', onclick: () => openReader(s.id) }, el('span', { 'aria-hidden': 'true' }, '📖'), el('b', {}, 'Read the lesson notes'), el('small', {}, 'The whole unit, on screen – opens at this lesson')),
            el('button', { class: 'lch go', type: 'button', id: 'toPractice', onclick: () => go('ex-' + R(s.id)) }, el('span', { 'aria-hidden': 'true' }, '✏️'), el('b', {}, `Practise ${s.id}`), el('small', {}, 'The Core questions unlock the next lesson')))));
        return; }
      status.append(el('section', { class: 'card', style: 'display:flex;gap:12px;align-items:center;flex-wrap:wrap' },
        el('span', {}, left ? `${left} check question${left > 1 ? 's' : ''} left in this lesson.` : 'You have answered every check question.'),
        el('button', { class: 'btn primary', type: 'button', id: 'lessonDone', disabled: !!left, onclick: () => { vs.completed = true; vs.pos = s.video.dur; Core.persist(); Backend.track('lesson_done', { learner: st.id, unit: Core.UNIT, sec: sid }); xpTick(); toast('Lesson finished – well done!'); drawStatus(); } }, 'I have finished this lesson ✓'))); };
    const stopFor = {}; s.stops.forEach(x => { (stopFor[x.after] = stopFor[x.after] || []).push(x); });
    const para = t => el('p', { class: 'lp' }, ...String(t).split(/(\*\*[^*]+\*\*)/).map(part => /^\*\*.*\*\*$/.test(part) ? el('b', {}, part.slice(2, -2)) : part));
    const addStop = x => {
        const i = s.stops.indexOf(x); const rec = (vs.stops[x.id] = vs.stops[x.id] || { tries: 0 });
        const box = el('section', { class: 'card stop lcheck' }, el('div', { class: 'stopbar' }, el('span', { class: 'eyebrow' }, `CHECK QUESTION ${i + 1} OF ${s.stops.length}`), rec.done ? el('span', { class: 'chip on' }, '✓ done') : null));
        const qh = el('div'); box.append(qh); body.append(box);
        QE.practice(x.q, qh, { rec, seed: st.id, save: () => { Core.persist(); }, onCheck: onCheck(box, x.q, rec),
          onDone: () => { rec.done = true; if (rec.everWrong) st.stopsWrong[x.q.id] = true; Core.persist(); xpTick(); drawStatus(); } });
      };
    (stopFor[-1] || []).forEach(addStop);   // "before you read on" questions that come before the first part
    // "Your turn" and "Spot the mistake" questions inside the notes: answers and tries are kept, they do not give XP or count as check questions
    vs.tries = vs.tries || {};
    const live = (q, host, after) => { const rec = (vs.tries[q.id] = vs.tries[q.id] || { tries: 0 });
      QE.practice(q, host, { rec, seed: st.id, nested: true, free: true, save: () => Core.persist(), onDone: () => { Core.persist(); after && after(); } });
      if (rec.done && after) after(); };
    s.lesson.forEach((b, bi) => {
      const kind = b.k || 'idea';
      const card = el('section', { class: 'card lblock lb-' + kind, id: 'lb-' + bi }, el('div', { class: 'lbtop' }, el('span', { class: 'lbkind' }, LB_KIND[kind] || 'Key idea'), el('span', { class: 'lbcount' }, `Part ${bi + 1} of ${s.lesson.length}`)), el('h2', {}, b.t));
      if (C.unit.tiny && ('speechSynthesis' in window)) card.append(el('button', { type: 'button', class: 'btn small ghost readq', onclick: () => QE.speak([b.t].concat(b.p || [], b.q ? [b.q] : [], b.a ? [b.a] : []).join('. ')) }, '🔊 Read to me'));
      fillBlock(card, b, live);
      body.append(card);
      (stopFor[bi] || []).forEach(addStop);
    });
    if (s.pdf && s.pdf.length) body.append(pdfCard(s));   // at the end: back to the document, then Start practice
    drawStatus();
  }

  /* ---------- Speaking room (ESL): a spoken conversation with the Camday tutor about the lesson topic ----------
     The browser turns speech into text (Web Speech API) and reads the tutor's reply aloud; typing always works too.
     Replies come from the AI tutor (api/speak.js) when the learner is signed in; otherwise a scripted partner built from the lesson's words answers. */
  const SPEAK_TURNS = 6;
  function viewSpeak(sid) {
    const s = Core.sec(sid), m = $main(); if (!s || !Core.IS_ESL) return go('u-' + Core.UNO);
    const lock = Core.secLock(st, s);
    subbar('', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}: ${C.unit.title}`), el('span', { class: 'sep' }), el('span', { class: 'ttl' }, `Speaking ${s.id} · ${s.title}`));
    if (lock) { m.append(bar(`Section ${s.id} · Speaking`), lockScreen(`Section ${s.id} is locked`, lock.reason, [lock])); return; }
    st.last = { route: 'sp-' + R(sid) }; st.speak = st.speak || {}; Core.persist();
    const lv = Core.stageNo(Core.STAGE), goal = s.objs.map(o => (C.objectives[o] || {}).t || '').filter(Boolean).join(' '), words = (s.vocab || []).map(v => v.w).slice(0, 10);
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    const T = { hist: [], used: {}, fixes: [], n: 0, busy: false, over: false, ai: false, lens: [] };
    const norm = x => String(x).toLowerCase().replace(/[^a-z' ]+/g, ' ');
    const markUsed = text => { const a = ' ' + norm(text) + ' '; words.forEach(w => { const k = norm(w).trim(); if (k && (a.includes(' ' + k + ' ') || a.includes(' ' + k + 's '))) T.used[w] = true; }); };
    // the scripted partner: asks about the topic, then asks for the lesson's words one by one
    const left = () => words.filter(w => !T.used[w]);
    const script = last => {
      if (!T.hist.length) return { reply: `Hello! Let us talk about ${s.title.toLowerCase()}. Tell me one thing about it.` };
      const short = last.trim().split(/\s+/).length < (lv <= 3 ? 2 : 4), w = left()[0];
      const praise = short ? 'Good start. Try a longer answer next time.' : ['Well done.', 'Good answer.', 'Nice sentence.', 'Great.'][T.n % 4];
      const ask = T.n === SPEAK_TURNS - 1 ? 'Last one: what is the best thing you learned in this lesson?' : w ? `Can you say a sentence with the word “${w}”?` : T.n % 2 ? `Tell me more about ${s.title.toLowerCase()}.` : 'Now ask me a question about it.';
      return { reply: praise + ' ' + ask };
    };
    const ask = async end => { let r = null;
      if (Backend.speak && me && !isGuest()) r = await Backend.speak({ stage: lv, topic: `${C.unit.title}: ${s.title}`, goal, words, history: T.hist, end: !!end });
      if (r && r.via === 'ai') { T.ai = true; return r; }
      return null; };

    const wordsBox = el('div', { class: 'spwords' }), turnsBox = el('span', { class: 'spturn', id: 'spTurn' });
    const drawHead = () => { wordsBox.textContent = ''; words.forEach(w => wordsBox.append(el('span', { class: 'spw' + (T.used[w] ? ' on' : '') }, T.used[w] ? '✓ ' : '', w))); turnsBox.textContent = T.over ? 'Finished' : `Turn ${Math.min(T.n + 1, SPEAK_TURNS)} of ${SPEAK_TURNS}`; };
    m.append(el('section', { class: 'card sphead' }, el('p', { class: 'eyebrow', style: 'margin:0' }, `${Core.stageLabel()} · Unit ${Core.UNO} · Speaking ${s.id}`), el('h1', { style: 'margin:4px 0 10px' }, `Talk about: ${s.title}`),
      el('div', { class: 'lmeta' }, el('span', {}, `${SPEAK_TURNS} turns`), el('span', {}, 'About 5 minutes'), turnsBox),
      el('div', { class: 'lgoalbox' }, el('span', { class: 'hl' }, 'Try to use these words'), words.length ? wordsBox : el('p', { class: 'muted', style: 'margin:4px 0 0' }, goal))));
    const chat = el('div', { class: 'spchat', id: 'spChat', 'aria-live': 'polite' });
    const input = el('input', { type: 'text', id: 'spInput', maxlength: 300, autocomplete: 'off', placeholder: SR ? 'Tap the microphone and speak, or type here' : 'Type your answer here', 'aria-label': 'Your answer' });
    const send = el('button', { class: 'btn primary', type: 'button', id: 'spSend' }, 'Send', el('span', { class: 'arr' }, ' →'));
    const mic = SR ? el('button', { class: 'spmic', type: 'button', id: 'spMic', 'aria-label': 'Speak your answer', 'aria-pressed': 'false', html: '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>' }) : null;
    const status = el('p', { class: 'spstatus muted', id: 'spStatus' }, SR ? 'Tap the microphone, speak, then stop. You can also type.' : 'This browser cannot listen. Type your answers, or open Camday in Chrome to speak.');
    const row = el('div', { class: 'sprow' }, mic, input, send);
    const room = el('section', { class: 'card sproom' }, chat, row, status,
      el('p', { class: 'muted small', style: 'margin:6px 0 0' }, 'Your browser turns your voice into text. Camday does not record or keep your voice. Do not share your full name, address or school.'));
    m.append(room);
    const bubble = (who, text, fix) => { const b = el('div', { class: 'spb ' + who }, el('small', {}, who === 'a' ? 'Camday tutor' : st.alias || 'You'), el('p', {}, text),
      who === 'a' ? el('button', { type: 'button', class: 'sphear', 'aria-label': 'Hear it again', onclick: () => QE.speak(text) }, 'Hear again') : null);
      chat.append(b); if (fix) chat.append(el('div', { class: 'spfix' }, el('b', {}, 'A better way to say it: '), fix.better)); chat.scrollTop = chat.scrollHeight; return b; };
    const typing = () => { const t = el('div', { class: 'spb a wait' }, el('small', {}, 'Camday tutor'), el('p', {}, '…')); chat.append(t); chat.scrollTop = chat.scrollHeight; return t; };
    const setBusy = on => { T.busy = on; send.disabled = on; input.disabled = on; if (mic) mic.disabled = on; };
    const tutorSay = (r) => { T.hist.push({ r: 'a', t: r.reply }); bubble('a', r.reply); try { QE.speak(r.reply); } catch (e) { } };
    async function finish() {
      T.over = true; drawHead(); row.hidden = true; status.hidden = true; const w = typing();
      const r = await ask(true); w.remove();
      const usedN = Object.keys(T.used).length, avg = T.lens.length ? T.lens.reduce((a, b) => a + b, 0) / T.lens.length : 0;
      const stars = r ? r.stars : (usedN >= Math.min(3, words.length) && avg >= (lv <= 3 ? 3 : 5) ? 3 : usedN >= 1 || avg >= 3 ? 2 : 1);
      const fixes = (r && r.fixes && r.fixes.length ? r.fixes : T.fixes).slice(0, 3);
      const prev = st.speak[s.id] || { n: 0, best: 0 }; st.speak[s.id] = { n: prev.n + 1, best: Math.max(prev.best, stars), at: Date.now() }; Core.persist();
      Backend.track('speak_done', { learner: st.id, unit: Core.UNIT, sec: sid, stars, ai: T.ai });
      room.append(el('div', { class: 'spsum', id: 'spSummary' }, el('span', { class: 'hl' }, 'Conversation finished'), el('h2', {}, '★'.repeat(stars) + '☆'.repeat(3 - stars) + (stars === 3 ? '  Excellent speaking' : stars === 2 ? '  Good speaking' : '  A good start')),
        el('p', {}, r && r.summary ? r.summary : `You answered ${T.lens.length} times and used ${usedN} of the ${words.length} lesson words.`),
        (r && r.good && r.good.length) ? el('ul', { class: 'spgood' }, ...r.good.map(x => el('li', {}, x))) : null,
        fixes.length ? el('div', { class: 'spfixes' }, el('b', {}, 'Say it better next time'), ...fixes.map(x => el('p', {}, el('s', {}, x.said), ' → ', el('b', {}, x.better)))) : null,
        left().length ? el('p', { class: 'muted' }, 'Words to try next time: ' + left().join(', ')) : null,
        el('div', { class: 'btnrow' }, el('button', { class: 'btn primary', type: 'button', id: 'spAgain', onclick: () => render() }, 'Talk again'), el('a', { class: 'btn', href: '#u-' + Core.UNO }, 'Back to the unit'))));
      confetti && stars === 3 && confetti();
    }
    async function say(text) {
      text = String(text || '').trim().slice(0, 300); if (!text || T.busy || T.over) return;
      input.value = ''; setBusy(true); markUsed(text); T.lens.push(text.split(/\s+/).length); T.n++;
      const mine = bubble('u', text); T.hist.push({ r: 'u', t: text }); drawHead();
      if (T.n >= SPEAK_TURNS) { setBusy(false); return finish(); }
      const w = typing(); const r = (await ask(false)) || script(text); w.remove();
      if (r.fix) { T.fixes.push(r.fix); mine.after(el('div', { class: 'spfix' }, el('b', {}, 'A better way to say it: '), r.fix.better)); }
      tutorSay(r); setBusy(false); input.focus();
    }
    send.addEventListener('click', () => say(input.value)); input.addEventListener('keydown', e => { if (e.key === 'Enter') say(input.value); });
    if (mic) { let rec = null, on = false;
      const stop = () => { on = false; mic.classList.remove('on'); mic.setAttribute('aria-pressed', 'false'); try { rec && rec.stop(); } catch (e) { } };
      mic.addEventListener('click', () => { if (on) return stop();
        try { window.speechSynthesis && window.speechSynthesis.cancel(); rec = new SR(); rec.lang = 'en-GB'; rec.interimResults = true; rec.maxAlternatives = 1;
          let fin = '';
          rec.onresult = ev => { let txt = ''; for (let i = 0; i < ev.results.length; i++) { txt += ev.results[i][0].transcript; if (ev.results[i].isFinal) fin = txt; } input.value = txt; };
          rec.onerror = ev => { status.textContent = ev.error === 'not-allowed' ? 'The microphone is blocked. Allow it in your browser, or type your answer.' : 'I could not hear you. Try again, or type your answer.'; stop(); };
          rec.onend = () => { const v = (fin || input.value).trim(); stop(); if (v) say(v); };
          rec.start(); on = true; mic.classList.add('on'); mic.setAttribute('aria-pressed', 'true'); status.textContent = 'Listening… speak now, then tap the microphone to stop.';
        } catch (e) { status.textContent = 'The microphone did not start. Type your answer instead.'; } });
      window.addEventListener('hashchange', stop, { once: true }); }
    drawHead(); setBusy(true); const w0 = typing();
    ask(false).then(r => { w0.remove(); tutorSay(r || script('')); setBusy(false); });
  }

  /* ---------- exercises (question card + solution panel) ---------- */
  /* ---------- experiment room (Primary): a virtual lab and an experiment to try at home ---------- */
  let labStop = null;
  /* ---------- Primary focus room: practice and experiments open full screen, one thing at a time.
     Learners can leave whenever they like; if the round is not finished, a reminder asks them to finish it first. ---------- */
  const Focus = { on: false, route: '', left: () => 0, what: '' };
  const ROUND = 8;
  function focusOff() { Focus.on = false; Focus.route = ''; document.body.classList.remove('focus-mode'); }
  function focusOn(route, left, what) { Focus.on = true; Focus.route = route; Focus.left = left; Focus.what = what; document.body.classList.add('focus-mode'); }
  // what is still to do, in words a young learner understands
  function leftText(what, n) { return what === 'lab' ? 'You have not finished the virtual lab yet.' : `You still have ${n} Easy question${n > 1 ? 's' : ''} to do.`; }
  // Leaving before the round is finished: a reminder, then the learner decides. Answers are already saved.
  let leaveAsk = null;
  function confirmLeave(to, done) {
    if (leaveAsk) leaveAsk(); const n = Focus.left(), what = Focus.what;
    const body = el('div', { class: 'leaveask' }, el('p', { class: 'big' }, leftText(what, n)),
      el('p', {}, what === 'lab' ? 'Finish the experiment to complete this topic.' : 'Finish them to open the next lesson.'),
      el('p', { class: 'muted' }, 'Your work is saved, so you can come back and finish any time.'));
    leaveAsk = modal('Not finished yet!', body, [
      { t: 'Leave for now', cls: 'ghost', on: () => { leaveAsk = null; if (done) done(); focusOff(); go(to); } },
      { t: 'Keep going', cls: 'primary', on: () => { leaveAsk = null; } }]);
    const kg = [...document.querySelectorAll('.modal .btn')].pop(); if (kg) { kg.id = 'keepGoing'; kg.previousElementSibling && (kg.previousElementSibling.id = 'leaveAnyway'); kg.focus(); }
  }
  // the room's own exit button: leaves straight away when the round is done, otherwise reminds first
  function exitBtn(to, done) {
    return el('button', { type: 'button', class: 'btn small fexit', id: 'leaveRoom', title: 'Leave the room', onclick: () => { if (Focus.left() > 0) confirmLeave(to, done); else { if (done) done(); focusOff(); go(to); } } }, '✕ Exit');
  }
  function focusFrame(icon, title, sub) {
    const room = el('div', { class: 'froom', role: 'dialog', 'aria-modal': 'true', 'aria-label': title });
    const head = el('div', { class: 'fhead' }, el('span', { class: 'fico', 'aria-hidden': 'true' }, icon), el('div', { class: 'ftitle' }, el('b', {}, title), el('small', {}, sub)));
    const prog = el('div', { class: 'fprog' }); const body = el('div', { class: 'fbody' }); const foot = el('div', { class: 'ffoot' });
    room.append(head, prog, body, foot); $main().append(room); return { room, head, prog, body, foot };
  }
  function focusDone(F, title, text, btns) {
    F.body.innerHTML = ''; F.foot.innerHTML = ''; burst(F.body);
    F.body.append(el('section', { class: 'card fdone' }, el('div', { class: 'fbig', 'aria-hidden': 'true' }, '🎉'), el('h2', {}, title), el('p', {}, text),
      el('div', { class: 'fchoices' }, ...btns.map(b => el('button', { type: 'button', class: 'btn big ' + (b.cls || ''), id: b.id || null, onclick: b.on }, b.t)))));
  }
  function viewFocusPractice(s) {
    // full-screen practice room: choose Easy (Core), Medium (Practice) or Hard (Challenge) and any question, like a worksheet task.
    // The room closes only when the Core questions are done (then "Exit task" opens).
    const route = 'ex-' + R(s.id); UI.fl = UI.fl || {}; const key = `${Core.STAGE}:${Core.UNO}:${route}`;
    const LV = [['req', 'Easy', '🟢', 'Core'], ['prac', 'Medium', '🟡', 'Practice'], ['adv', 'Hard', '🔴', 'Challenge'], ['ext', 'Extreme', '⚫', 'Extreme'], ['more', 'Extra', '🔵', 'More practice']].filter(([k]) => s[k] && s[k].length);
    const notDone = q => !(st.items[q.id] || {}).done;
    let P = UI.fl[key]; if (!P) { const k0 = Core.reqLeft(st, s).length ? 'req' : (s.prac.some(notDone) ? 'prac' : 'req'); P = UI.fl[key] = { tab: k0, i: Math.max(0, s[k0].findIndex(notDone)) }; }
    const coreLeft = () => Core.reqLeft(st, s).length;
    focusOn(route, coreLeft, 'practice');
    const F = focusFrame('🎯', `${s.id} ${s.title}`, 'Practice room · pick a level and any question');
    const leaveBtn = exitBtn('u-' + Core.UNO, () => { if (!coreLeft()) UI.fl[key] = null; });
    if (s.vocab && s.vocab.length && window.Primary) {   // the lesson's words, in a drawer inside the room
      const wb = Primary.wordBank(s); const fresh = !s.req.some(q => (st.items[q.id] || {}).tries);
      const drawer = el('div', { class: 'fwords' }, wb);
      const wbtn = el('button', { type: 'button', class: 'btn small fwbtn' + (fresh ? ' glow' : ''), id: 'wordsBtn', 'aria-expanded': 'false', onclick: () => { const o = drawer.classList.toggle('open'); wbtn.classList.remove('glow'); wbtn.setAttribute('aria-expanded', String(o)); QE.setTxt(wbtn, o ? '✕ Close words' : '📒 Words'); } }, '📒 Words');
      F.head.append(wbtn); F.head.after(drawer);
    }
    if (hasNotes()) F.head.append(el('button', { type: 'button', class: 'btn small fwbtn', id: 'reviewNotes', onclick: () => openReader(s.id) }, '📖 Notes'));
    if (s.pdf && s.pdf.length) F.head.append(el('button', { type: 'button', class: 'btn small fwbtn', id: 'reviewPdf', onclick: () => openBook(s) }, '📄 Review the PDF'));
    const repBtn = el('button', { type: 'button', class: 'btn small ghost fexit', id: 'reportQ', title: 'Report a problem with this question', 'aria-label': 'Report a problem with this question' }, '⚑');
    F.head.append(repBtn, leaveBtn);
    const levels = el('div', { class: 'flevels', role: 'tablist' }); const strip = el('div', { class: 'fstrip' });
    F.prog.append(levels, strip);
    const list = () => s[P.tab];
    const drawTop = () => {
      levels.innerHTML = ''; strip.innerHTML = '';
      LV.forEach(([k, name, dot, what]) => { const qs = s[k], d = qs.filter(q => !notDone(q)).length;
        levels.append(el('button', { type: 'button', role: 'tab', class: 'flv lv-' + k + (P.tab === k ? ' on' : ''), 'aria-selected': String(P.tab === k), id: 'lv-' + k, onclick: () => { P.tab = k; P.i = Math.max(0, qs.findIndex(notDone)); show(); } },
          el('span', { class: 'fdot', 'aria-hidden': 'true' }, dot), el('b', {}, name), el('small', {}, `${what} · ${d}/${qs.length}`), k === 'req' && d < qs.length ? el('i', { class: 'fneed' }, 'needed') : null)); });
      const qs = list(); const d = qs.filter(q => !notDone(q)).length;
      strip.append(el('div', { class: 'fpct' }, el('span', { style: `width:${Math.round(d / qs.length * 100)}%` })), el('small', { class: 'fpctn' }, `${Math.round(d / qs.length * 100)}%`),
        el('div', { class: 'fqs' }, ...qs.map((q, i) => { const r = st.items[q.id] || {};
          return el('button', { type: 'button', class: 'fq' + (i === P.i ? ' cur' : '') + (r.done ? (r.ok ? ' ok' : ' half') : r.tries ? ' bad' : ''), 'aria-label': `Question ${i + 1}${r.done ? ', done' : ''}`, onclick: () => { P.i = i; show(); } }, 'Q' + (i + 1)); })));
      leaveBtn.title = coreLeft() ? `Leave the room (${coreLeft()} Easy questions still to do)` : 'Leave the practice room';
    };
    const levelDone = () => {
      const qs = list(); const k = P.tab; const right = qs.filter(q => (st.items[q.id] || {}).ok && (st.items[q.id] || {}).tries === 1).length;
      const i = C.sections.indexOf(s), nxt = C.sections[i + 1]; const exit = to => () => { focusOff(); UI.fl[key] = null; go(to); };
      const btns = []; LV.forEach(([k2, name]) => { if (k2 !== k && s[k2].some(notDone)) btns.push({ t: `Try ${name} ▶`, cls: k2 === 'prac' ? 'gold' : '', id: 'go-' + k2, on: () => { P.tab = k2; P.i = Math.max(0, s[k2].findIndex(notDone)); show(); } }); });
      if (s.lab) btns.push({ t: '🧪 Experiment room', id: 'toLab', on: exit('lab-' + R(s.id)) });
      if (nxt && Core.secDone(st, s)) btns.push({ t: `Next lesson ${nxt.id} →`, cls: 'primary', on: exit('v-' + R(nxt.id)) });
      if (!coreLeft()) btns.push({ t: 'Exit task', id: 'finishRoom', on: exit('u-' + Core.UNO) });
      const name = (LV.find(x => x[0] === k) || [])[1];
      focusDone(F, `${name} questions finished!`, `⭐ ${right} of ${qs.length} right first time. ${k === 'req' && nxt ? `Lesson ${nxt.id} is now open.` : ''}`, btns);
      drawTop(); xpTick(); refreshToc();
    };
    function gameBreak(after) {
      const words = secGameWords(s); P.games = (P.games || 0) + 1; const G = Games.GAMES[(P.games - 1) % Games.GAMES.length];
      F.body.innerHTML = ''; F.foot.innerHTML = '';
      const back = () => { P.sinceGame = 0; after(); };
      F.body.append(el('section', { class: 'card gbreak', id: 'gameBreak', style: 'text-align:center;padding:30px' }, el('div', { style: 'font-size:56px', 'aria-hidden': 'true' }, G.icon),
        el('h2', { style: 'margin:6px 0' }, `Game time: ${G.name}!`), el('p', { class: 'muted' }, `A quick round with the words from ${s.id} – ${words.slice(0, 5).map(w => w.w).join(', ')}${words.length > 5 ? '…' : ''}. Then back to your questions.`),
        el('div', { class: 'btnrow', style: 'justify-content:center' }, el('button', { type: 'button', class: 'btn big gold shine', id: 'gbPlay', onclick: () => {
          F.body.innerHTML = ''; const host = el('div'); F.body.append(host); st.games = st.games || {}; const rec0 = st.games[s.id] || { n: 0, best: 0, by: {} };
          Games.play(host, Object.assign(gameCtx(), { pool: words, short: true, cont: { label: 'Back to practice ▶', fn: back },
            onFinish: r => { rec0.n++; rec0.best = Math.max(rec0.best, r.score); rec0.by[r.id] = Math.max(rec0.by[r.id] || 0, r.score); st.games[s.id] = rec0; Core.persist(); refreshToc(); } }), G.id); } }, '▶ Play'),
          el('button', { type: 'button', class: 'btn big ghost', id: 'gbSkip', onclick: back }, 'Skip for now'))));
    }
    function show() {
      st.last = { route, tab: P.tab, idx: P.i }; Core.persist();
      drawTop(); F.body.innerHTML = ''; F.foot.innerHTML = '';
      const qs = list(); P.i = Math.min(Math.max(0, P.i), qs.length - 1); const q = qs[P.i]; const rec = st.items[q.id] = st.items[q.id] || { tries: 0 };
      const card = el('section', { class: 'card qcard fcard' }); F.body.append(card);
      const prev = el('button', { type: 'button', class: 'btn big ghost', disabled: P.i === 0, onclick: () => { P.i--; show(); } }, '◀ Back');
      const last = P.i === qs.length - 1;
      const next = el('button', { type: 'button', class: 'btn big gold shine', id: 'nextQ', disabled: !rec.done }, last ? 'Finish ✓' : 'Next ▶');
      const advance = () => { if (!qs.some(notDone)) { levelDone(); return; } const j = qs.findIndex((x, k) => k > P.i && notDone(x)); P.i = j >= 0 ? j : qs.findIndex(notDone); show(); F.room.scrollTop = 0; };
      // Stages 1–5: every 4 questions, a short word game with this lesson's words, then back to the practice
      next.onclick = () => { if (!rec.done) return; if ((P.sinceGame || 0) >= 4 && secGameWords(s).length && qs.some(notDone)) { gameBreak(advance); return; } advance(); };
      F.foot.append(prev, next); repBtn.onclick = () => reportQuestion(q);
      const lvI = LV.find(x => x[0] === P.tab) || [];
      QE.practice(q, card, { num: P.i + 1, of: qs.length, level: lvI[1], levelKey: 'lv-' + P.tab, rec, seed: st.id, save: () => Core.persist(), onCheck: onCheck(card, q, rec), onDone: () => { rec.done = true; P.sinceGame = (P.sinceGame || 0) + 1; Core.persist(); next.disabled = false; drawTop(); xpTick(); refreshToc(); setTimeout(() => next.scrollIntoView({ block: 'nearest', behavior: 'smooth' }), 150); } });
    }
    show();
  }
  function viewLab(sid) {
    const s = Core.sec(sid), m = $main(); if (!s || !s.lab) return go('u-' + Core.UNO);
    if (Core.IS_PRIMARY && !Core.secLock(st, s)) {   // the experiment room opens full screen until the virtual lab is finished
      if (labStop) { try { labStop(); } catch (e) { } labStop = null; }
      st.last = { route: 'lab-' + R(sid) }; Core.persist(); UI.labTab = UI.labTab || {};
      const LS = () => ((st.labs || {})[s.id] || {}); const route = 'lab-' + R(sid);
      focusOn(route, () => (LS().v || {}).done ? 0 : 1, 'lab');
      const F = focusFrame('🧪', `${s.id} ${s.lab.title}`, 'Experiment room · do the virtual lab, then try it at home');
      F.head.append(exitBtn('u-' + Core.UNO));
      const leaveRow = () => { F.foot.innerHTML = ''; if (!(LS().v || {}).done) { F.foot.append(el('span', { class: 'muted' }, 'Finish the virtual lab to complete this topic.')); return; }
        const i = C.sections.indexOf(s), nxt = C.sections[i + 1];
        F.foot.append(el('button', { type: 'button', class: 'btn big', id: 'finishLab', onclick: () => { focusOff(); go('u-' + Core.UNO); } }, 'Finish'),
          nxt && Core.secDone(st, s) ? el('button', { type: 'button', class: 'btn big primary', onclick: () => { focusOff(); go('v-' + R(nxt.id)); } }, `Next lesson ${nxt.id} →`) : null); };
      F.body.append(Primary.labRoom(s, st, { tab: UI.labTab[sid] || 'v', setTab: k => { UI.labTab[sid] = k; render(); }, persist: () => { Core.persist(); xpTick(); refreshToc(); leaveRow(); }, toast, onLeave: f => { labStop = f; } }));
      leaveRow(); return;
    }
    if (labStop) { try { labStop(); } catch (e) { } labStop = null; }
    const lock = Core.secLock(st, s);
    subbar('blue', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}: ${C.unit.title}`), el('span', { class: 'ttl' }, `${s.id} ${s.title} · Experiment room`));
    if (lock) { m.append(bar(`Section ${s.id} · Experiments`), lockScreen(`The experiments for ${s.id} are locked`, lock.reason, [lock])); return; }
    st.last = { route: 'lab-' + R(sid) }; Core.persist();
    UI.labTab = UI.labTab || {};
    m.append(bar(`Unit ${Core.UNO} › ${s.id} › Experiment room`), tocBtn(), el('section', { class: 'card lessonhead' }, el('p', { class: 'eyebrow', style: 'margin:0' }, `${Core.stageLabel()} · Unit ${Core.UNO} · ${s.id}`), el('h1', { style: 'margin:4px 0 6px' }, `🧪 ${s.lab.title}`),
      el('p', { class: 'muted', style: 'margin:0' }, 'Work like a scientist: predict, change one thing, measure, record and conclude. Do the virtual lab here, then try the real experiment at home with an adult.')),
      Primary.labRoom(s, st, { tab: UI.labTab[sid] || 'v', setTab: k => { UI.labTab[sid] = k; render(); }, persist: () => { Core.persist(); xpTick(); refreshToc(); }, toast, onLeave: f => { labStop = f; } }));
  }
  function viewExercises(sid) {
    const s = Core.sec(sid), m = $main(); if (!s) return go('home'); const route = 'ex-' + R(sid);
    const lock = Core.secLock(st, s);
    if (lock || !Core.videoDone(st, s)) {
      subbar('blue', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}: ${C.unit.title}`), el('span', { class: 'ttl' }, `${s.id} ${s.title} · Practice`));
      m.append(bar(`Section ${s.id} · Practice`), lock ? lockScreen(`Practice for section ${s.id} is locked`, lock.reason, [lock]) : lockScreen(`Practice for section ${s.id} is locked`, s.lesson ? 'Read the lesson and answer its check questions before you start the practice.' : 'Watch the whole video and answer its pause questions before you start the practice.', [Core.firstMissingIn(st, s)])); return;
    }
    return viewFocusPractice(s);   // every course practises inside the full-screen practice room (Maths too, from 27/11/2026)
    let tab = UI.tab[route] || 'req'; if (!(s[tab] || []).length) tab = 'req'; const list = s[tab]; let idx = Math.min(UI.idx[route + tab] || 0, list.length - 1);
    st.last = { route, tab, idx }; Core.persist();
    const q = list[idx]; const go2 = i => { UI.idx[route + tab] = i; render(); };
    const pips = el('div', { class: 'pips', 'aria-hidden': 'true' }, ...list.map((x, i) => { const r = st.items[x.id] || {}; return el('span', { class: i === idx ? 'cur' : r.done ? (r.ok ? (r.tries === 1 ? 'ok' : 'half') : 'bad') : r.tries ? 'bad' : '' }); }));
    const tabName = { req: 'Core', prac: 'Practise', adv: '* Advanced', ext: 'Extreme', more: 'More practice' }[tab];
    subbar('blue', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}`), el('span', { style: 'font-size:15px;color:#DCE8FA' }, `${s.id} ${s.title} · ${tabName} · `, el('b', { style: 'color:#fff' }, `Question ${idx + 1} of ${list.length}`)), pips,
      el('button', { class: 'btn small onblue', type: 'button', disabled: idx === 0, onclick: () => go2(idx - 1) }, '← Previous'),
      el('button', { class: 'btn small gold', type: 'button', id: 'nextQ', disabled: idx === list.length - 1, onclick: () => go2(idx + 1) }, 'Next', el('span', { class: 'arr' }, '→')));
    const tabs = el('div', { class: 'btnrow', role: 'tablist' }, ...[['req', `Core · ${8 - Core.reqLeft(st, s).length}/8`], ['prac', `Practice · ${s.prac.filter(x => (st.items[x.id] || {}).done).length}/${s.prac.length}`], ['adv', `* Advanced · ${s.adv.filter(x => (st.items[x.id] || {}).done).length}/${s.adv.length}`]].concat((s.more || []).length ? [['more', `More practice · ${s.more.filter(x => (st.items[x.id] || {}).done).length}/${s.more.length}`]] : [], (s.ext || []).length ? [['ext', `⚫ Extreme · ${s.ext.filter(x => (st.items[x.id] || {}).done).length}/${s.ext.length}`]] : [])
      .map(([k, t]) => el('button', { class: 'chip' + (k === tab ? ' on' : ''), role: 'tab', type: 'button', 'aria-selected': String(k === tab), onclick: () => { UI.tab[route] = k; render(); } }, t)));
    st.marks = st.marks || {};
    const mk = el('button', { type: 'button', class: 'chip' + (st.marks[q.id] ? ' on' : ''), 'aria-pressed': String(!!st.marks[q.id]), style: 'margin-left:auto', onclick: () => { st.marks[q.id] = !st.marks[q.id]; Core.persist(); mk.classList.toggle('on'); mk.setAttribute('aria-pressed', String(!!st.marks[q.id])); } }, '★ Bookmark');
    tabs.append(mk); if (hasNotes()) tabs.append(el('button', { type: 'button', class: 'chip', id: 'reviewNotes', onclick: () => openReader(s.id) }, '📖 Review the notes'));
    if (s.pdf && s.pdf.length) tabs.append(el('button', { type: 'button', class: 'chip', id: 'reviewPdf', onclick: () => openBook(s) }, '📄 Review the PDF'));
    const chips = el('div', { class: 'qnav' }, ...list.map((x, i) => { const r = st.items[x.id] || {}; return el('button', { class: 'qc' + (i === idx ? ' on' : '') + (r.done ? (r.ok ? ' ok' : ' half') : r.tries ? ' bad' : ''), type: 'button', 'aria-label': `Question ${i + 1}${r.done ? ', done' : ''}`, onclick: () => go2(i) }, String(i + 1)); }));
    const card = el('section', { class: 'card qcard' });
    const doneBanner = el('div');
    const showBanner = () => {
      doneBanner.innerHTML = ''; if (!Core.secDone(st, s)) return;
      const i = C.sections.indexOf(s), nxt = C.sections[i + 1];
      doneBanner.append(el('div', { class: 'banner ok' }, el('b', {}, `✓ You have finished the Core questions for section ${s.id}. `), nxt ? `Section ${nxt.id} is now unlocked. ` : 'The Unit Test opens once every section is done. ', 'Practice and * Advanced questions stay open and are optional.',
        el('button', { class: 'btn primary small', type: 'button', onclick: () => go(nxt ? 'v-' + R(nxt.id) : 'test') }, nxt ? `Go to section ${nxt.id}` : 'Take the Unit Test', el('span', { class: 'arr' }, '→'))));
    };
    // aside: solution / video tabs + objective
    const solBody = el('div', { class: 'card solx', style: 'padding:22px' }); let solTab = 'sol';
    const solTabs = el('div', { class: 'tabs', role: 'tablist' });
    const rec = st.items[q.id] = st.items[q.id] || { tries: 0 };
    const sg = C.segments[q.obj]; const segS = Core.sec(sg[0]);
    const drawSol = () => {
      solTabs.innerHTML = ''; [['sol', 'Worked solution'], ['video', segS && segS.lesson ? 'Lesson notes' : 'Video solution']].forEach(([k, t]) => solTabs.append(el('button', { type: 'button', class: solTab === k ? 'on' : '', role: 'tab', 'aria-selected': String(solTab === k), onclick: () => { solTab = k; drawSol(); } }, t)));
      solBody.innerHTML = '';
      if (solTab === 'sol') {
        if (!rec.done) solBody.append(el('b', { class: 'lex' }, 'Solution'), el('p', { class: 'muted' }, 'The worked solution appears once you have finished this question. Stuck? Press “Check answer” for a step-by-step hint.'));
        else solBody.append(el('b', { class: 'lex', style: 'font-size:18px' }, 'Worked solution'), ...(q.reason ? [el('p', { class: 'reason' }, q.reason)] : []), el('div', { class: 'banner ok', style: 'margin-top:8px' }, el('b', {}, 'Answer: '), QE.answerText(q)));
      } else if (segS && segS.lesson) solBody.append(el('b', { class: 'lex' }, `Lesson ${segS.id}: ${segS.title}`), el('p', { class: 'muted' }, 'Re-read the key ideas and worked examples for this objective.'), el('button', { class: 'btn primary small', type: 'button', onclick: () => go('v-' + R(segS.id)) }, '📖 Open the lesson'));
      else solBody.append(el('b', { class: 'lex' }, `Video clip: ${sg[3]}`), el('p', { class: 'muted' }, `Lesson ${segS.id} · ${fullT(segS, sg[1])}–${fullT(segS, sg[2])} in the full video`), el('button', { class: 'btn primary small', type: 'button', onclick: () => go('v-' + R(segS.id), { seek: { sec: segS.id, from: sg[1], to: sg[2] } }) }, svgI(I.play, 16, '#fff', 2.6), 'Watch this clip'));
    };
    const aside = el('aside', { class: 'aside' }, solTabs, solBody,
      el('div', { class: 'card', style: 'padding:18px 20px' }, el('b', { class: 'lex' }, 'Learning objective'), el('p', { style: 'margin:4px 0 0;font-size:15px' }, `${q.obj}: ${C.objectives[q.obj].t}`)),
      el('div', { class: 'goal' }, el('span', { class: 'gi' }, svgI(I.bulb, 16, '#1C2A3A', 2)), el('span', {}, tab === 'req' ? 'Right first time: 1 mark · second try: ½ mark. Two wrong tries: you get guided reasoning and a similar question.' : tab === 'adv' ? '* Advanced – optional. Written by Camday from the real source named on each question.' : tab === 'ext' ? 'Extreme – optional and very hard: new situations, several steps and written paragraphs. Each one you finish earns a badge.' : 'Practice – optional for unlocking, but it makes you stronger before the Unit Test.')));
    m.append(...[bar(`Unit ${Core.UNO} › ${s.id} › ${tabName} › question ${idx + 1}`), tocBtn(), doneBanner, tab === 'req' && window.Primary ? Primary.wordBank(s) : null, tabs, chips, el('div', { class: 'exgrid' }, el('div', { class: 'q' }, card), aside)].filter(Boolean));
    if (s.lab) tabs.append(el('a', { class: 'chip', href: '#lab-' + R(sid), id: 'labLink' }, '🧪 Experiment'));
    showBanner(); drawSol();
    QE.practice(q, card, { num: idx + 1, of: list.length, level: { req: 'Core', prac: 'Practice', adv: 'Advanced', ext: 'Extreme', more: 'More practice' }[tab], levelKey: 'lv-' + tab, rec, seed: st.id, save: () => Core.persist(), onCheck: onCheck(card, q, rec), onDone: () => { rec.done = true; Core.persist(); showBanner(); refreshToc(); drawSol(); xpTick();
      const c = chips.children[idx]; if (c) c.className = 'qc on ' + (rec.ok ? 'ok' : 'half'); } });
    card.append(el('div', { class: 'btnrow between objline' }, el('span', {}, el('b', { style: 'color:#1C2A3A' }, 'Learning objective: '), C.objectives[q.obj].t, el('small', { class: 'muted' }, ` · ${C.objectives[q.obj].code || ''}`)),
      el('button', { class: 'btn small ghost', type: 'button', id: 'reportQ', onclick: () => reportQuestion(q) }, '⚑ Report a problem')));
  }

  function printQ(q, n) {
    const box = el('div', { class: 'pq' }, el('p', {}, el('b', {}, n + '. '), q.prompt.replace(/^\* Advanced\.\s*/, '* ').replace(/ Choose a label, then tap.*$/, '').replace(/\(tap the grid;.*?\)/, ''), ' ', el('i', { class: 'pts' }, `[${q.obj}]`)));
    const figHtml = (name, o) => { const d = el('div', { class: 'pfig' }); d.innerHTML = AtomicFig.get(name, o).svg; return d; };
    const lines = k => el('div', { class: 'lines' }, ...Array.from({ length: k }, () => el('div', { class: 'ln' })));
    if (q.ctx || q.data) { const cx = el('div', { class: 'qctx' }); if (q.ctx) String(q.ctx).split('\n').forEach(t => cx.append(el('p', {}, t)));
      if (q.fig && q.fig.kind && q.type !== 'scale') cx.append(figHtml(q.fig.kind, q.fig)); if (q.data) cx.append(QE.dataTable(q.data)); box.prepend(cx); }
    else if (q.fig && q.fig.kind && !['mcq', 'multi', 'scale', 'label'].includes(q.type)) box.append(figHtml(q.fig.kind, q.fig));
    switch (q.type) {
      case 'short': case 'expr': box.append(el('p', {}, (q.lhs ? q.lhs + ' = ' : 'Answer: ') + '________________________________')); break;
      case 'cloze': box.append(el('p', { class: 'cloze' }, String(q.text).replace(/\{\d+\}/g, ' ______________ '))); break;
      case 'mcq': case 'multi': if (q.fig && q.fig.kind && !q.ctx && !q.data) box.append(figHtml(q.fig.kind, q.fig)); box.append(el('ol', { class: 'abc' }, ...q.options.map(o => el('li', {}, '☐ ' + o.t)))); break;
      case 'label': { const f = AtomicFig.get(q.fig); const d = el('div', { class: 'pfig' }); d.innerHTML = f.svg; const svg = d.querySelector('svg'); Object.keys(q.spots).forEach((k, i) => { const [x, y] = f.a[k]; svg.insertAdjacentHTML('beforeend', `<circle cx="${x}" cy="${y}" r="11" fill="#fff" stroke="#0B2545" stroke-width="2"/><text x="${x}" y="${y + 5}" text-anchor="middle" font-size="13" font-weight="700">${i + 1}</text>`); });
        box.append(d, el('p', {}, 'Labels: ' + QE.shuffle(Object.values(q.spots), 'p' + q.id).join(' · ')), el('div', { class: 'cols2' }, ...Object.keys(q.spots).map((k, i) => el('div', {}, `${i + 1}. ____________________`)))); break; }
      case 'scale': box.append(figHtml(q.fig.kind, q.fig), el('p', {}, 'Reading: __________  Unit: ______')); break;
      case 'num': box.append(el('p', { class: 'muted' }, 'Working:'), lines(3), el('p', {}, `Answer: __________ ${q.unit === '×' ? '' : '(unit: ____)'}`)); break;
      case 'order': box.append(el('p', {}, 'Number the boxes 1–' + q.items.length + ':'), el('ul', { class: 'abc' }, ...QE.shuffle(q.items, 'p' + q.id).map(t => el('li', {}, '☐ ' + t)))); break;
      case 'match': { const rs = QE.shuffle(q.pairs.map(p => p.r), 'p' + q.id); box.append(el('table', { class: 'grid' }, ...q.pairs.map((p, i) => el('tr', {}, el('td', {}, p.l + '  •'), el('td', {}, '•  ' + String.fromCharCode(65 + i) + '. ' + rs[i]))))); break; }
      case 'explain': box.append(lines(5)); break;
      case 'para': box.append(...(q.frame ? [el('p', { class: 'muted' }, 'Writing frame: ' + q.frame)] : []), lines(Math.max(8, (q.sentences || [4])[0] * 2))); break;
      case 'grid': box.append(el('table', { class: 'grid' }, el('tr', {}, el('th', {}, ''), ...(QE.isTick(q) ? q.cols : ['Answer (' + q.cols.join(' / ') + ')']).map(c => el('th', {}, c))), ...q.rows.map(r => el('tr', {}, el('th', {}, r.l), ...(QE.isTick(q) ? q.cols : ['']).map(() => el('td', {}, '')))))); break;
      case 'table': box.append(el('table', { class: 'grid' }, el('tr', {}, ...q.head.map(h => el('th', {}, h))), ...q.rows.map(r => el('tr', {}, ...r.map(c => el('td', {}, c && typeof c === 'object' ? '' : c)))))); break;
      case 'graph': { if (q.table_rows) box.append(el('table', { class: 'grid' }, el('tr', {}, el('th', {}, q.x.label), el('th', {}, q.y.label)), ...q.table_rows.map(r => el('tr', {}, el('td', {}, r[0]), el('td', {}, r[1]))))); const d = el('div', { class: 'pgraph' }); box.append(d); if (q.follow) box.append(el('p', {}, q.follow.prompt), lines(2)); break; }
      case 'sim': box.append(el('p', {}, 'Use the virtual microscope on the website, then record:'), el('table', { class: 'grid' }, el('tr', {}, el('th', {}, 'Trial'), el('th', {}, 'Total magnification'), el('th', {}, 'Cells across the line')), ...[1, 2, 3].map(i => el('tr', {}, el('td', {}, i), el('td', {}, ''), el('td', {}, '')))), el('p', {}, 'Prediction:'), lines(1), el('p', {}, 'Conclusion:'), lines(2)); break;
    }
    return box;
  }
  // print-only worksheet (Design v4 paper): personal watermark on every page, microprint frame, copy code — no PDF download
  function wsLearner() { return { name: st.name || st.alias || 'Learner', lid: 'L-' + String(st.id || 'guest').replace(/-/g, '').slice(0, 7).toUpperCase() }; }
  function worksheetPages(s, info, mount) {
    const qs = s.vocab ? s.prac.filter(q => q.type !== 'say' && !q.audio).slice(0, 14) : s.req.concat(s.prac.slice(0, 6), s.prac.slice(6).filter(q => q.ws).slice(0, 20)); /* + the school revision set */ const doc = `S${Core.STAGE}-U${String(Core.UNO).padStart(2, '0')}-W${s.id.replace('.', '')}`;
    const mins = Math.max(15, Math.ceil(qs.length * 2.5 / 5) * 5);
    const out = el('div', { class: 'ws', id: 'wsPages' }); let pno = 0; const pages = [];
    const foot = last => el('div', { class: 'pfoot' }, el('div', {}, `© Camday ${info.date.getFullYear()} · ${doc} · Copy #${info.serial} · ${info.code}`, el('br'), `Printed for ${info.name} (${info.lid}) on ${info.when}. Not for sharing or resale.`), el('b', {}, last ? 'End of worksheet' : '[Turn over'));
    const page = (...kids) => { pno++; const pg = el('div', { class: 'a4 paper4', html: Paper.frame() + Paper.watermark(info) }); pg.append(el('div', { class: 'pbody' }, ...kids)); pages.push(pg); return pg; };
    const runHead = () => el('div', { class: 'prun' }, el('span', {}, el('b', {}, 'Cambridge'), ` ${Core.stageLabel()} · Unit ${Core.UNO} · ${s.id} ${s.title}`), el('b', {}, String(pno + 1)));
    const boxes = (txt, n) => el('span', { class: 'pboxes' }, ...Array.from({ length: n }, (_, i) => el('i', {}, txt[i] || '')));
    const d = info.date, dd = String(d.getDate()).padStart(2, '0') + String(d.getMonth() + 1).padStart(2, '0') + d.getFullYear();
    // cover
    const cover = page(
      el('div', { class: 'pcv-h' }, el('img', { src: 'camday_logo.png', alt: '' }), el('div', {}, el('div', { class: 'nm' }, 'CAMDAY'), el('div', { class: 'tg' }, el('b', {}, 'Cambridge'), ` ${Core.levelName(Core.STAGE)} ${Core.subjectOf(Core.STAGE)}` + (Core.IS_PRIMARY ? '' : ' · Checkpoint preparation')))),
      el('div', { html: Paper.waves() }),
      el('div', { class: 'pcv-meta' }, 'Written by the Camday teaching team · Videos, practice and Unit Tests online at Camday'),
      el('div', { class: 'pcv-ttl' }, el('span', {}, 'PRACTICE WORKSHEET'), el('span', {}, `SCORE: ______ / ${qs.length}`)),
      el('table', { class: 'pgrid' }, el('tbody', {}, el('tr', {}, el('td', { class: 'k' }, 'LEARNER NAME'), el('td', { colspan: '3', class: 'pre' }, info.name)),
        el('tr', {}, el('td', { class: 'k' }, 'LEARNER ID'), el('td', {}, boxes(info.lid.replace(/-/g, ''), 8)), el('td', { class: 'k', style: 'width:22mm' }, 'DATE'), el('td', {}, boxes(dd, 8))))),
      el('div', { class: 'psubj' }, el('div', { class: 'ico', html: '<svg width="52" height="52" viewBox="0 0 56 56"><rect x="6" y="10" width="44" height="36" rx="10" fill="none" stroke="#0E1B3D" stroke-width="3"/><ellipse cx="28" cy="28" rx="13" ry="9" fill="#DCE8FA" stroke="#0149AF" stroke-width="2"/><circle cx="33" cy="27" r="4" fill="#0E1B3D"/></svg>' }),
        el('div', {}, el('div', { class: 'camline' }, el('b', {}, 'CAMBRIDGE'), ` ${Core.stageLabel(Core.STAGE).toUpperCase()}`), el('div', {}, `Unit ${Core.UNO} · ${C.unit.title}`, el('br'), `${s.id} ${s.title}`)),
        el('div', { style: 'text-align:right' }, el('div', { class: 'code' }, doc), el('div', {}, `${mins} minutes`), el('small', {}, `${qs.length} questions`))),
      el('p', { style: 'margin:5mm 0 0' }, 'You must answer on this worksheet.'),
      el('div', { class: 'psec' }, 'INSTRUCTIONS'), el('ul', {}, el('li', {}, 'Answer ', el('b', {}, 'all'), ' questions. Questions 1–8 are Core; 9–14 are extra practice.'), el('li', {}, 'Use a black or dark blue pen. You may use an HB pencil for diagrams.'), el('li', {}, 'Write your answer to each question in the space provided. Show your working.'), el('li', {}, `When you finish, open topic ${s.id} on Camday and check your answers with the worked solutions.`)),
      el('div', { class: 'psec' }, 'INFORMATION'), el('ul', {}, el('li', {}, `This worksheet has ${qs.length} questions.`), el('li', {}, 'Every printed copy carries the learner’s name, ID, date and a copy number.')),
      el('div', { class: 'pverify' }, el('span', { html: Paper.seal(info.code) }), el('div', {}, 'Verification code', el('br'), el('b', {}, info.code), el('br'), `Tied to this learner, this worksheet and copy #${info.serial}. Camday keeps a record of every printed copy.`)));
    cover.querySelector('.pbody').append(foot(false)); out.append(cover); if (mount) mount.append(out);
    // question pages: filled by measuring, so nothing is ever cut off at the bottom of a page
    let p = page(runHead()); let pb = p.querySelector('.pbody'); let ft = foot(false); pb.append(ft); out.append(p); let onPage = 0;
    qs.forEach((q, i) => {
      const node = printQ(q, i + 1); pb.insertBefore(node, ft);
      if (pb.scrollHeight > pb.clientHeight + 1 && onPage > 0) { node.remove(); p = page(runHead()); pb = p.querySelector('.pbody'); ft = foot(false); pb.append(ft); out.append(p); pb.insertBefore(node, ft); onPage = 0; }
      onPage++;
    });
    const endq = el('div', { class: 'pend' }, `— End of questions · ${qs.length} questions —`); pb.insertBefore(endq, ft); if (pb.scrollHeight > pb.clientHeight + 1) endq.remove();
    ft.replaceWith(foot(true));
    return out;
  }
  function wsAnswers(s, info, mount) {
    const qs = s.vocab ? s.prac.filter(q => q.type !== 'say' && !q.audio).slice(0, 14) : s.req.concat(s.prac.slice(0, 6), s.prac.slice(6).filter(q => q.ws).slice(0, 20)); /* + the school revision set */ const doc = `S${Core.STAGE}-U${String(Core.UNO).padStart(2, '0')}-W${s.id.replace('.', '')}`;
    const out = el('div', { class: 'ws', id: 'wsAns' }); mount.append(out);
    const foot = last => el('div', { class: 'pfoot' }, el('div', {}, `© Camday ${info.date.getFullYear()} · ${doc} · ANSWERS · ${info.code}`, el('br'), `Opened by ${info.name} (${info.lid}) on ${info.when}. For self-marking only.`), el('b', {}, last ? 'End of answers' : '[Turn over'));
    const page = () => { const pg = el('div', { class: 'a4 paper4', html: Paper.frame() + Paper.watermark(info) }); const pb = el('div', { class: 'pbody' }, el('div', { class: 'prun' }, el('span', {}, el('b', {}, 'ANSWERS'), ` · Cambridge ${Core.stageLabel()} · Unit ${Core.UNO} · ${s.id} ${s.title}`), el('b', {}, 'Mark scheme'))); pg.append(pb); out.append(pg); return pb; };
    let pb = page(); let ft = foot(false); pb.append(ft); let list = el('ol', { class: 'ans' }); pb.insertBefore(list, ft);
    qs.forEach((q, i) => {
      const li = el('li', { value: String(i + 1) }, QE.answerText(q), q.reason ? el('div', { class: 'muted' }, q.reason) : null); list.append(li);
      if (pb.scrollHeight > pb.clientHeight + 1 && list.children.length > 1) { li.remove(); pb = page(); ft = foot(false); pb.append(ft); list = el('ol', { class: 'ans' }); pb.insertBefore(list, ft); list.append(li); }
    });
    ft.replaceWith(foot(true)); return out;
  }
  function viewWorksheet(sid) {
    const s = Core.sec(sid), m = $main(); if (!s) return go('home');
    const lock = Core.secLock(st, s); if (lock && lock.paywall) { m.append(bar(`Unit ${Core.UNO} › ${s.id} › Worksheet`), lockScreen(`Worksheet ${s.id} is locked`, lock.reason, [lock])); return; }
    const msg = el('span', { class: 'muted' }); const holder = el('div'); const ansBox = el('div', { class: 'ansbox' });
    const L = wsLearner(); const doc = `S${Core.STAGE}-U${Core.UNO}-W${s.id}`;
    const draw = serial => { holder.innerHTML = ''; worksheetPages(s, Paper.copyInfo(doc, L, serial), holder); };
    const doPrint = () => {
      st.prints = (st.prints || 0) + 1; if (!st.ws.includes(sid)) st.ws.push(sid); Core.persist();
      draw(st.prints); Backend.track('worksheet_print', { learner: st.id, unit: Core.UNIT, sec: sid, copy: st.prints });
      setTimeout(() => { try { window.print(); } catch (e) { msg.textContent = 'This browser blocked printing.'; } }, 80);
    };
    m.append(bar(`Unit ${Core.UNO} › ${s.id} › Worksheet`),
      el('section', { class: 'card noprint wsbar' }, el('div', {}, el('p', { class: 'eyebrow', style: 'margin:0' }, 'Worksheet · print only'), el('h2', { style: 'margin:2px 0 4px' }, el('span', { class: 'cam' }, 'Cambridge'), ` ${Core.stageName(Core.STAGE)} · ${s.id} ${s.title}`),
        el('p', { class: 'muted', style: 'margin:0' }, 'Worksheets are printed, not downloaded. Each printed copy carries your name, learner ID, the date and a copy number.')),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn gold', type: 'button', id: 'printWs' }, '🖨 Print worksheet'), el('button', { class: 'btn', type: 'button', id: 'showAns' }, '🔑 Get the answers'), msg)),
      holder, ansBox);
    m.querySelector('#printWs').onclick = doPrint;
    const showAns = () => {
      ansBox.innerHTML = ''; st.wsAns = st.wsAns || []; if (!st.wsAns.includes(sid)) st.wsAns.push(sid); Core.persist();
      Backend.track('worksheet_answers', { learner: st.id, unit: Core.UNIT, sec: sid });
      ansBox.append(el('section', { class: 'card noprint wsbar', id: 'ansBar' }, el('div', {}, el('p', { class: 'eyebrow', style: 'margin:0' }, 'Answers · self-marking'), el('h2', { style: 'margin:2px 0 4px' }, `Answers – Worksheet ${s.id}`), el('p', { class: 'muted', style: 'margin:0' }, 'Mark your printed worksheet with a different coloured pen, then read the reasons for anything you got wrong.')),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn', type: 'button', id: 'printAns', onclick: () => { document.body.classList.add('print-ans'); setTimeout(() => { try { window.print(); } catch (e) { } }, 60); } }, '🖨 Print answers'), el('button', { class: 'btn ghost', type: 'button', onclick: () => { ansBox.innerHTML = ''; } }, 'Hide answers'))));
      Paper.guard(ansBox, () => { }); wsAnswers(s, Paper.copyInfo(doc + '-A', L, st.prints || 0), ansBox);
      ansBox.querySelector('#ansBar').scrollIntoView({ behavior: 'smooth', block: 'start' });
    };
    m.querySelector('#showAns').onclick = () => modal('Get the answers?', el('p', {}, 'Answers are for checking your own work. Finish the worksheet first – looking at the answers before you try will not help you learn.'),
      [{ t: 'Not yet', cls: 'ghost' }, { t: 'I have finished – show the answers', cls: 'primary', on: showAns }]);
    window.addEventListener('afterprint', () => document.body.classList.remove('print-ans'), { once: false });
    draw(st.prints || 0); Paper.guard(holder, doPrint);
  }

  /* ---------- unit test ---------- */
  function viewRemedial() {
    const m = $main(); const a = Core.lastAttempt(st);
    m.append(bar(`Unit ${Core.UNO} › Review questions`));
    if (!a || !a.remed) { m.append(el('section', { class: 'card' }, el('p', {}, 'No review questions have been set yet.'))); return; }
    a.remed.forEach(id => { if (!findQ(id)) { const k = Core.remKey(a, id); st.rem[k] = Object.assign(st.rem[k] || { tries: 0 }, { done: true, gone: true }); } });   // a question no longer in the course never blocks the retake
    st.last = { route: 'remedial' }; Core.persist(); const ts = Core.testState(st);
    const left = Core.remLeft(st, a);
    m.append(el('section', { class: 'card' }, el('h2', {}, `Review after attempt ${a.n}: ${a.remed.length - left.length}/${a.remed.length} done`), el('p', {}, 'Chosen from your weaker objectives: ' + a.weak.join(', ') + '. Finish them all to unlock the equivalent paper.'),
      ts.state === 'ready' ? el('a', { class: 'btn primary', href: '#test', id: 'goRetake' }, `Take the equivalent paper (Paper ${ts.form}) →`) : null));
    a.remed.forEach((id, i) => {
      const q = findQ(id); const k = Core.remKey(a, id); const rec = st.rem[k] = st.rem[k] || { tries: 0 };
      if (!q) return;
      const card = el('section', { class: 'card qcard' }, el('p', { class: 'muted' }, `Review ${i + 1} of ${a.remed.length} · ${q.obj}`)); m.append(card);
      QE.practice(q, card, { rec, onCheck: onCheck(card, q, rec), seed: st.id + 'r' + a.n, save: () => Core.persist(), onDone: () => { rec.done = true; Core.persist(); if (!Core.remLeft(st, a).length) render(); } });
    });
  }
  // retired = questions replaced in a content revision, kept only so review lists made before the revision still open
  function findQ(id) { for (const s of C.sections) for (const q of s.req.concat(s.prac, s.adv, s.more || [], s.ext || [], s.stops.map(x => x.q), s.retired || [])) if (q.id === id) return q; return null; }
  const allQs = () => C.sections.flatMap(s => s.req.concat(s.prac, s.adv, s.more || [], s.ext || []));

  /* ---------- drills: wrong answers / by topic ---------- */
  function startDrill(title, qs, ns) { UI.drill = { title, ids: qs.map(q => q.id), ns }; go('drill'); }
  function viewDrill() {
    const m = $main(); const d = UI.drill; if (!d) return go('profile');
    m.append(bar('Progress › ' + d.title), el('h2', {}, d.title), el('p', { class: 'muted' }, 'Extra practice – it doesn\'t change scores you already have. Getting a question right first time removes it from your “wrong answers” list.'));
    if (!d.ids.length) { m.append(el('p', {}, 'No questions here.')); return; }
    d.ids.forEach((id, i) => { const q = findQ(id); if (!q) return; const card = el('section', { class: 'card qcard' }, el('p', { class: 'muted' }, `${i + 1}/${d.ids.length}`)); m.append(card);
      const k = d.ns + ':' + id; st.drill = st.drill || {}; const rec = st.drill[k] = st.drill[k] || { tries: 0 };
      QE.practice(q, card, { rec, onCheck: onCheck(card, q, rec), seed: st.id + d.ns, save: () => Core.persist(), onDone: () => { if (rec.ok && rec.tries === 1) { (st.mastered = st.mastered || {})[id] = true; } Core.persist(); } }); });
  }
  const wrongList = () => allQs().concat(C.sections.flatMap(s => s.stops.map(x => x.q))).filter(q => ((st.items[q.id] || {}).everWrong || st.stopsWrong[q.id]) && !(st.mastered || {})[q.id]);

  /* ---------- profile ---------- */
  function viewTopic() {
    const m = $main(); m.append(bar('Question Bank › Revise by topic'), el('h2', {}, 'Revise by topic (objective)'));
    Object.keys(C.objectives).forEach(o => {
      const qs = allQs().filter(q => q.obj === o); const tried = qs.filter(q => st.items[q.id] && st.items[q.id].done); const okc = tried.filter(q => st.items[q.id].ok).length;
      const sg = C.segments[o], s = Core.sec(sg[0]);
      m.append(el('section', { class: 'card topic' }, el('b', {}, `${o} (${s.id}) – ${C.objectives[o].t}`),
        el('p', { class: 'muted' }, `${qs.length} questions · ${tried.length} done · ${okc} correct`),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn small', type: 'button', onclick: () => go('v-' + R(s.id), { seek: { sec: s.id, from: sg[1], to: sg[2] } }) }, `▶ Video ${fullT(s, sg[1])}–${fullT(s, sg[2])}`), el('button', { class: 'btn small primary', type: 'button', onclick: () => startDrill(`Revise topic ${o}`, qs.filter(q => !q.adv).slice(0, 10), 'topic' + o) }, 'Practise 10 questions'))));
    });
  }

  /* ---------- leaderboard ---------- */
  // Stage certificate (A4 landscape). Camday design: navy frame, gold rule, seal and the learner's achievements.
  function drawCert(c, preview) {
    const W = 1754, H = 1240, cv = document.createElement('canvas'); cv.width = W; cv.height = H; const g = cv.getContext('2d');
    const NAVY = '#0B2545', BLUE = '#0149AF', GOLD = '#C9962E', GOLD2 = '#F3BF69';
    g.fillStyle = '#FBF8F1'; g.fillRect(0, 0, W, H);
    // soft dotted pattern
    g.fillStyle = 'rgba(1,73,175,0.05)'; for (let y = 60; y < H; y += 34) for (let x = 60; x < W; x += 34) { g.beginPath(); g.arc(x, y, 2, 0, 7); g.fill(); }
    g.strokeStyle = NAVY; g.lineWidth = 22; g.strokeRect(36, 36, W - 72, H - 72);
    g.strokeStyle = GOLD; g.lineWidth = 3; g.strokeRect(70, 70, W - 140, H - 140); g.lineWidth = 1.5; g.strokeRect(80, 80, W - 160, H - 160);
    // corner ornaments
    [[80, 80, 0], [W - 80, 80, 1], [W - 80, H - 80, 2], [80, H - 80, 3]].forEach(([x, y, k]) => { g.save(); g.translate(x, y); g.rotate(k * Math.PI / 2); g.strokeStyle = GOLD; g.lineWidth = 3;
      g.beginPath(); g.arc(0, 0, 70, 0, Math.PI / 2); g.stroke(); g.beginPath(); g.arc(0, 0, 52, 0, Math.PI / 2); g.stroke(); g.fillStyle = GOLD2; g.beginPath(); g.arc(24, 24, 7, 0, 7); g.fill(); g.restore(); });
    const center = (t, y, font, color, spacing) => { g.font = font; g.fillStyle = color; g.textAlign = 'center'; if (spacing) { g.letterSpacing = spacing + 'px'; } g.fillText(t, W / 2, y); g.letterSpacing = '0px'; };
    return new Promise(res => { const img = new Image(); img.onload = done; img.onerror = done; img.src = 'camday_logo.png';
      function done() {
        if (img.width) { const h = 120, w = img.width / img.height * h; g.drawImage(img, W / 2 - w / 2, 120, w, h); }
        center('CERTIFICATE OF ACHIEVEMENT', 320, '600 34px Outfit, Figtree, Arial', GOLD, 8);
        center(`Cambridge ${Core.stageLabel()}`, 410, '700 76px Outfit, Figtree, Arial', NAVY);
        center(Core.IS_ESL ? (Core.STAGE <= 26 ? 'Cambridge Primary English as a Second Language (curriculum framework 0057)' : 'Cambridge Lower Secondary English as a Second Language (curriculum framework 0876)') : Core.IS_MATHS ? (Core.STAGE <= 16 ? 'Cambridge Primary Mathematics (curriculum framework 0096)' : 'Cambridge Lower Secondary Mathematics (curriculum framework 0862)') : Core.IS_PRIMARY ? 'Cambridge Primary Science (curriculum framework 0097)' : 'Cambridge Lower Secondary Science (curriculum framework 0893)', 462, '28px Figtree, Arial', '#52627A');
        center('This is to certify that', 545, 'italic 32px Georgia, serif', '#3A4B63');
        center(c.name, 640, 'italic 700 96px Georgia, serif', BLUE);
        g.strokeStyle = GOLD; g.lineWidth = 2; g.beginPath(); g.moveTo(W / 2 - 420, 668); g.lineTo(W / 2 + 420, 668); g.stroke();
        center(`has completed the Camday course for Cambridge ${Core.stageLabel()}:`, 718, '30px Figtree, Arial', NAVY); center(`all ${Core.unitCount()} units, every Unit Test and an end-of-year exam.`, 756, '30px Figtree, Arial', NAVY);
        // achievements row
        const stats = [[c.units || `${Core.unitCount()} / ${Core.unitCount()}`, 'units passed'], [c.avg || '—', 'Unit Test average'], [c.final || '—', 'end-of-year exam'], [c.hours || '—', 'hours of study'], [c.level || '—', 'level reached']];
        const bw = 250, gap = 22, x0 = W / 2 - (stats.length * bw + (stats.length - 1) * gap) / 2;
        stats.forEach(([b, t], i) => { const x = x0 + i * (bw + gap); g.fillStyle = '#FFFFFF'; g.strokeStyle = '#D9C59A'; g.lineWidth = 2; g.beginPath(); g.roundRect(x, 800, bw, 100, 18); g.fill(); g.stroke();
          g.textAlign = 'center'; g.fillStyle = BLUE; g.font = '700 40px Outfit, Figtree, Arial'; g.fillText(b, x + bw / 2, 852); g.fillStyle = '#52627A'; g.font = '22px Figtree, Arial'; g.fillText(t, x + bw / 2, 884); });
        // seal
        const sx = 300, sy = 1010; g.fillStyle = GOLD2; g.beginPath(); for (let i = 0; i < 48; i++) { const r = i % 2 ? 92 : 104, a = i / 48 * Math.PI * 2; g.lineTo(sx + r * Math.cos(a), sy + r * Math.sin(a)); } g.closePath(); g.fill();
        g.fillStyle = GOLD; g.beginPath(); g.arc(sx, sy, 80, 0, 7); g.fill(); g.strokeStyle = '#FFF4D6'; g.lineWidth = 3; g.beginPath(); g.arc(sx, sy, 68, 0, 7); g.stroke();
        g.fillStyle = '#FFFFFF'; g.textAlign = 'center'; g.font = '700 26px Outfit, Figtree, Arial'; g.fillText('CAMDAY', sx, sy - 8); g.font = '600 20px Figtree, Arial'; g.fillText(`CAMBRIDGE ${Core.stageName(Core.STAGE).toUpperCase()}`, sx, sy + 22); g.font = '22px Figtree'; g.fillText('★ ★ ★', sx, sy + 50);
        // signature + date + code
        g.strokeStyle = NAVY; g.lineWidth = 2; g.beginPath(); g.moveTo(W - 560, 1010); g.lineTo(W - 190, 1010); g.stroke();
        g.textAlign = 'center'; g.fillStyle = NAVY; g.font = 'italic 40px Georgia, serif'; g.fillText('The Camday teaching team', W - 375, 995);
        g.font = '24px Figtree, Arial'; g.fillStyle = '#52627A'; g.fillText('Camday', W - 375, 1045);
        g.textAlign = 'center'; g.fillStyle = NAVY; g.font = '600 24px Figtree, Arial'; g.fillText(`Awarded ${c.date}`, W / 2 - 60, 985); g.fillText(`Code ${c.code}`, W / 2 - 60, 1022);
        g.font = '20px Figtree, Arial'; g.fillStyle = '#6B7A90'; g.fillText('Check it at Camday → “Verify a certificate”.', W / 2 - 60, 1060);
        g.fillText(`Camday courses follow the Cambridge ${Core.levelName(Core.STAGE)} ${Core.IS_ESL ? 'English as a Second Language' : Core.IS_MATHS ? 'Mathematics' : 'Science'} framework. This is an Camday certificate, not a Cambridge qualification.`, W / 2, 1120);
        if (preview) { g.save(); g.translate(W / 2, H / 2); g.rotate(-0.35); g.font = '800 190px Outfit, Figtree, Arial'; g.fillStyle = 'rgba(201,58,58,0.13)'; g.textAlign = 'center'; g.fillText('PREVIEW', 0, 60); g.restore(); }
        res(cv);
      } });
  }
  function certStats() {
    const rs = Core.rankScore(st); const best = (Core.S.finalAttempts || []).filter(a => a.status === 'final' && a.passed).reduce((a, x) => Math.max(a, x.pct), 0);
    return { units: `${Math.min(Core.unitCount(), Object.keys(st.results || {}).filter(k => k.startsWith(`stage${Core.STAGE}-unit`)).length)} / ${Core.unitCount()}`, avg: rs ? rs.score.toFixed(0) + '%' : '—', final: best ? best.toFixed(0) + '%' : '—', hours: (Core.totalSeconds() / 3600).toFixed(1), level: String(Core.levelInfo().level) };
  }
  async function viewCert() {
    const m = $main(); m.append(bar(`Cambridge ${Core.stageName(Core.STAGE)} certificate`));
    await Core.refreshFinal().catch(() => { });
    let cert = null; try { cert = await Core.certificate(st); } catch (e) { cert = null; }
    const passedU = Object.keys(st.results || {}).filter(k => k.startsWith(`stage${Core.STAGE}-unit`)).length;
    if (!cert) {
      const items = [], needU = Math.ceil(Core.unitCount() * Core.MOVE_ON / 100), pr = await Core.courseProgress(Core.STAGE, st).catch(() => ({ lessons: 0 }));
      if (passedU < needU) items.push({ what: `pass ${needU} of the ${Core.unitCount()} Unit Tests (${Core.MOVE_ON}%) – ${passedU} so far`, route: 'tests' });
      if (pr.lessons < Core.MOVE_ON) items.push({ what: `finish ${Core.MOVE_ON}% of the lessons – ${pr.lessons}% so far`, route: 'u-' + Core.UNO });
      m.append(lockScreen(`Your Cambridge ${Core.stageName(Core.STAGE)} certificate`, `The certificate is awarded when you have finished ${Core.MOVE_ON}% of the lessons and passed ${Core.MOVE_ON}% of the Unit Tests. It also opens the next stage. Here is how it will look:`, items));
      const img = el('img', { class: 'certimg', alt: `Preview of the Cambridge ${Core.stageName(Core.STAGE)} certificate` }); m.append(el('section', { class: 'card certwrap' }, img));
      drawCert({ name: st.name, code: `AE-${Core.IS_ESL ? 'E' + Core.stageNo(Core.STAGE) : Core.IS_MATHS ? 'M' + Core.stageNo(Core.STAGE) : 'S' + Core.STAGE}-XXXX-XXXXXXXX`, date: '—', ...certStats() }, true).then(cv => { img.src = cv.toDataURL('image/png'); });
      return;
    }
    const c = { name: cert.name, code: cert.code, date: new Date(cert.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }), ...certStats() };
    const img = el('img', { class: 'certimg', alt: `Certificate for ${c.name}, code ${c.code}` }); const msg = el('span', { class: 'muted' });
    m.append(el('section', { class: 'card certwrap' }, el('h2', {}, `🎓 Your Cambridge ${Core.stageName(Core.STAGE)} certificate`), el('p', {}, 'Certificate code: ', el('b', { id: 'certCode' }, c.code), ' · Awarded: ' + c.date),
      el('p', { class: 'muted' }, 'Anyone can check this certificate at ', el('a', { href: '#verify' }, 'Verify a certificate'), ' using the code.'), img,
      el('div', { class: 'btnrow' }, el('button', { class: 'btn primary', type: 'button', id: 'dlCert', onclick: async () => { const cv = await drawCert(c); const j = cv.toDataURL('image/jpeg', 0.92); const bytes = Uint8Array.from(atob(j.split(',')[1]), x => x.charCodeAt(0)); const pdf = Core.jpegPdf(bytes, cv.width, cv.height, 842, 595); const r = await Core.saveFile(`Atomic_Certificate_${c.code}.pdf`, new Blob([pdf], { type: 'application/pdf' })); msg.textContent = r === 'saved' ? 'Downloaded.' : r === 'declined' ? 'Download cancelled.' : 'Could not download.'; } }, '⬇ Download PDF'), msg)));
    drawCert(c).then(cv => { img.src = cv.toDataURL('image/png'); });
  }

  /* ---------- Lower Secondary → Stage → Unit (every level of the breadcrumb is a page) ---------- */
  const PRICE = (window.ATOMIC_CONFIG || {}).stagePrice || 'US$49';
  const PAID = ((window.ATOMIC_CONFIG || {}).billing || 'off') === 'paddle';   // real Paddle checkout (one-time prices)
  const buyErr = x => ({ payments_closed: 'Payments are not open yet.', checkout_closed: 'The payment window was closed – nothing was charged.', payment_pending: 'Payment received – your course opens in a minute. Reload the page if it does not.',
    stage_locked: 'This stage opens after 80 % of your current stage.', already_enrolled: 'You already have this course.', payments_unavailable: 'The payment page could not load. Check your connection and try again.' }[x && x.code] || errText(x));
  const crumbs = (...tail) => el('nav', { class: 'crumb', 'aria-label': 'Breadcrumb' }, el('a', { href: '#home' }, 'Dashboard'), ' › ', el('a', { href: '#level' }, Core.levelName(Core.STAGE)), ...tail.flatMap(t => [' › ', t]));
  // ---- course catalogue: subjects × levels (Science and Mathematics, Lower Secondary → IGCSE → AS & A Level) ----
  let CATALOG = null;
  async function loadCatalog() { if (!CATALOG) { try { const r = await fetch('content/catalog.json'); CATALOG = r.ok ? await r.json() : null; } catch (e) { CATALOG = null; } } return CATALOG; }
  const subjTag = (S0) => el('span', { class: 'subjtag', style: `--sc:${S0.color}` }, S0.icon + ' ' + S0.name);
  function courseCard(c, S0) {
    const isStage = !!c.stage && c.status !== 'soon' && !Core.stageLocked(c.stage); const en = isStage && st && !isGuest() && Core.enrolled(c.stage), mine = en;
    const other = isStage && st && !isGuest() && !en && Core.myCourses().length && Core.levelOf(c.stage) !== Core.learnerStage();   // one stage per learner
    const state = c.status === 'soon' || (c.stage && Core.stageLocked(c.stage)) ? 'soon' : mine ? 'mine' : other ? 'locked' : c.status === 'enrol' || isStage ? 'enrol' : 'open';
    const tag = { soon: 'COMING SOON', mine: 'YOUR COURSE', enrolled: 'ENROLLED', enrol: 'NOT ENROLLED', open: 'OPEN', locked: `LOCKED · FINISH STAGE ${Core.learnerStage()} FIRST` }[state];
    const btn = state === 'soon' ? el('a', { class: 'btn small', href: c.stage ? '#stage-' + c.stage : '#course-' + c.id }, 'Details', el('span', { class: 'arr' }, ' →'))
      : state === 'locked' ? el('a', { class: 'btn small', href: '#stage-' + c.stage }, '🔒 Locked')
      : state === 'mine' || state === 'enrolled' || state === 'open' ? el('a', { class: 'btn small primary', href: '#stage-' + c.stage }, 'Open', el('span', { class: 'arr' }, ' →'))
        : el('a', { class: 'btn small gold', href: '#checkout-' + c.stage }, `Enrol · ${PRICE}`, el('span', { class: 'arr' }, ' →'));
    return el('section', { class: 'card ccard ' + state + (mine ? ' cur' : ''), id: isStage ? 'stageCard' + c.stage : 'course-' + c.id, style: `--sc:${S0.color}` },
      el('div', { class: 'cchead' }, el('span', { class: 'cclv' }, c.stage ? String(c.badge || c.stage) : c.level === 'igcse' ? 'IG' : 'A'), el('span', { class: 'cccode' }, c.code)),
      el('span', { class: 'eyebrow', style: 'margin:0' }, tag), el('h3', { style: 'margin:0' }, c.title),
      el('p', { class: 'muted', style: 'margin:0;font-size:14px' }, mine && c.stage === Core.STAGE ? `${Core.unitCount()} units · ≈ ${estH(Core.INDEX.est || 0)} of learning · Unit Tests, Checkpoint exam room, end-of-year exams and a certificate` : c.about || (c.stage ? `Cambridge Stage ${c.stage} – units are being prepared` : '')), btn);
  }
  async function viewCourses(subject) {
    const m = $main(); const K = await loadCatalog(); if (!K) { m.append(el('p', {}, 'Could not load the courses.')); return; }
    subject = subject || 'science'; const S0 = K.subjects.find(x => x.id === subject) || K.subjects[0];
    pageHero('CAMDAY COURSES', 'Subjects and levels', 'Choose a subject, then a level – from Cambridge Lower Secondary (Checkpoint) to IGCSE and AS & A Level. Each stage or course is enrolled separately.');
    m.append(el('nav', { class: 'subjtabs', role: 'tablist', 'aria-label': 'Subjects' }, ...K.subjects.map(x => el('a', { role: 'tab', class: 'subjtab' + (x.id === S0.id ? ' on' : ''), 'aria-selected': String(x.id === S0.id), href: '#courses-' + x.id, style: `--sc:${x.color}` }, x.icon + ' ' + x.name,
      el('small', {}, K.courses.some(c => c.subject === x.id && c.status !== 'soon' && !(c.stage && Core.stageLocked(c.stage))) ? 'open now' : 'coming soon')))));
    K.levels.forEach(L => {
      const list = K.courses.filter(c => c.subject === S0.id && c.level === L.id); if (!list.length) return;
      m.append(el('section', { class: 'lvlgroup' }, el('div', { class: 'lvlhead' }, el('h2', { style: 'margin:0' }, L.name), el('span', { class: 'muted' }, `${L.ages} · ${L.note}`)),
        el('div', { class: 'ccgrid' }, ...list.map(c => courseCard(c, S0)))));
    });
  }
  function viewLevel() { return viewCourses('science'); }
  async function viewCourse(id) {
    const m = $main(); const K = await loadCatalog(); const c = K && K.courses.find(x => x.id === id); if (!c) return go('courses');
    if (c.status !== 'soon' && c.stage) return go('stage-' + c.stage);
    const S0 = K.subjects.find(x => x.id === c.subject), L = K.levels.find(x => x.id === c.level);
    pageHero(`${S0.name.toUpperCase()} · ${L.short.toUpperCase()} · SYLLABUS ${c.code}`, c.title, c.about || `${L.name} ${S0.name}.`);
    m.append(el('nav', { class: 'crumb2' }, el('a', { href: '#courses-' + S0.id }, S0.name), ' › ', L.short, ' › ', c.title));
    const box = el('section', { class: 'card', style: 'display:flex;flex-direction:column;gap:14px' }, el('div', { class: 'cphead' }, subjTag(S0), el('span', { class: 'status todo' }, 'Coming soon')),
      el('p', { style: 'margin:0' }, `This course is being written by the Camday teaching team. It will work like Cambridge ${Core.stageLabel()}: short lesson videos with pause questions, practice for every topic, print-only worksheets, timed Unit Tests in the exam room and a certificate.`));
    if (c.strands) box.append(el('div', {}, el('b', {}, 'Curriculum strands'), el('div', { class: 'chips' }, ...c.strands.map(x => el('span', { class: 'chip' }, x)))));
    if (c.exams) box.append(el('div', {}, el('b', {}, 'Checkpoint exam room (practice papers in this format)'), el('ul', { style: 'margin:6px 0 0' }, ...c.exams.map(e => el('li', {}, el('b', {}, `${S0.name} ${e.code}`), ` · ${e.name} · ${e.minutes} minutes · ${e.marks} marks · ${e.note}`)))));
    const msg = el('span', { class: 'muted' });
    box.append(el('div', { class: 'btnrow' }, st && !isGuest() ? el('button', { class: 'btn gold', type: 'button', id: 'notifyMe', onclick: () => { Backend.track('course_interest', { learner: st.id, course: c.id }); QE.setTxt(msg, '✓ Thank you – we will tell you when it opens.'); } }, '🔔 Tell me when it opens') : null, el('a', { class: 'btn', href: '#courses-' + S0.id }, 'All ' + S0.name + ' courses'), msg));
    m.append(box);
  }
  async function viewStage(g) {
    const m = $main();
    if (g !== Core.STAGE && Core.stageLocked(g)) { stageSoon(g); return; }
    if (g !== Core.STAGE && Core.enrolled(g)) {   // an enrolled stage: open it (its units, tests and certificate)
      try { const r = await fetch(`content/stage${g}.json`); if (r.ok && (await r.json()).units.some(u => u.ready)) { await Loading.overlay(`Opening Cambridge ${Core.stageLabel(g)}`, Core.switchStage(g)); C = Core.C; st = Core.cur(); return render(); } } catch (e) { }
    }
    if (g !== Core.STAGE) {
      pageHero(Core.levelName(g).toUpperCase(), `Cambridge ${Core.stageName(g)}`, Core.enrolled(g) ? `You are enrolled in Cambridge ${Core.stageName(g)}.` : `Cambridge ${Core.stageName(g)} is a separate course.`);
      m.append(crumbs(`Cambridge ${Core.stageName(g)}`));
      if (!Core.enrolled(g)) { m.append(await buyOrLockCard(g)); return; }
      m.append(el('section', { class: 'card done' }, el('h2', {}, `✓ Enrolled in Cambridge ${Core.stageName(g)}`), el('p', {}, `The Cambridge ${Core.stageName(g)} units open here as soon as they have been reviewed. You will get a notification.`), el('a', { class: 'btn small', href: `#stage-${Core.STAGE}` }, `Back to Cambridge ${Core.stageName(Core.STAGE)}`)));
      return;
    }
    const tot = Core.totalSeconds(), passedN = Object.keys(st.results || {}).filter(k => k.startsWith(`stage${Core.STAGE}-unit`)).length;
    pageHero(Core.IS_ESL ? (Core.STAGE <= 26 ? 'CAMBRIDGE PRIMARY ESL' : 'CAMBRIDGE LOWER SECONDARY ESL') : Core.IS_MATHS ? (Core.STAGE <= 16 ? 'CAMBRIDGE PRIMARY MATHEMATICS' : 'CAMBRIDGE LOWER SECONDARY MATHEMATICS') : Core.IS_PRIMARY ? 'CAMBRIDGE PRIMARY SCIENCE' : 'CAMBRIDGE LOWER SECONDARY SCIENCE', `Cambridge ${Core.stageLabel()}`, 'Open any unit at any time – you do not have to finish one before starting another.',
      [statCard(el('span', { class: 'ti big' }, '⏱'), `≈ ${estH(Core.INDEX.est || 0)}`, 'whole course'), statCard(el('span', { class: 'ti big' }, '📚'), hrs(tot), 'you have studied'), statCard(ringIcon(Math.round(passedN / Core.unitCount() * 100)), `${passedN} / ${Core.unitCount()}`, 'units completed')]);
    m.append(crumbs(`Cambridge ${Core.stageName(Core.STAGE)}`));
    const rows = Core.INDEX.units.map(u => { const res = (st.results || {})[u.id], sec = Core.unitSeconds(u.n);
      return el('a', { class: 'lbrow srow2', href: '#u-' + u.n, 'data-unit': u.n }, el('span', {}, unitIcon(u.n)), el('span', {}, el('b', {}, `Unit ${u.n} · ${u.t}`), el('br'), el('small', { class: 'muted' }, `${u.strand} · ${(u.sections || []).length} topics · ${u.qs || 0} questions`)),
        el('span', {}, el('small', { class: 'muted' }, 'Estimated'), el('br'), el('b', {}, estH(u.est || 0))), el('span', {}, el('small', { class: 'muted' }, res ? 'Completed in' : 'Studied'), el('br'), el('b', {}, hrs(sec))),
        el('span', {}, res ? el('span', { class: 'status done' }, `✓ ${res.pct.toFixed(0)}%`) : sec ? el('span', { class: 'status cur' }, 'In progress') : el('span', { class: 'status todo' }, 'Not started'))); });
    m.append(el('section', { class: 'card lbtable', id: 'stageUnits' }, el('div', { class: 'lbrow h srow2' }, el('span', {}, ''), el('span', {}, 'UNIT'), el('span', {}, 'ESTIMATED'), el('span', {}, 'YOUR TIME'), el('span', {}, 'STATUS')), ...rows,
      el('div', { class: 'lbrow srow2 tot' }, el('span', {}, ''), el('b', {}, 'Whole course (with 2 end-of-year papers)'), el('b', {}, estH(Core.INDEX.est || 0)), el('b', {}, hrs(tot)), el('span', {}))));
    Core.loadFinal().then(F => { if (F) m.append(finalCard(F, Core.levelInfo())); });
  }
  // one stage per learner: a course of the learner's own stage can be added; another stage opens after 80 % of the current one
  async function buyOrLockCard(g) {
    const lv = Core.learnerStage(), same = Core.levelOf(g) === lv || !Core.myCourses().length;
    if (isGuest()) return guestWall('Create a free account first');
    if (same) return el('section', { class: 'card lockcard', id: 'addCourse' }, el('h2', {}, `➕ Add ${Core.subjectOf(g)} to your Stage ${Core.levelOf(g)}`),
      el('p', {}, `You study Stage ${lv}. You can add ${Core.subjectOf(g)} Stage ${Core.levelOf(g)} to your plan at any time.`), el('a', { class: 'btn gold', href: '#checkout-' + g }, `Add · ${PRICE}`, el('span', { class: 'arr' }, ' →')));
    const p = await Core.levelProgress(lv);
    if (p.ready) return el('section', { class: 'card done', id: 'moveOn' }, el('h2', {}, `🎉 You can move on to Cambridge ${Core.stageName(g)}`),
      el('p', {}, `You have finished ${p.lessons}% of the lessons and ${p.tests}% of the Unit Tests of Stage ${lv}.`), el('a', { class: 'btn gold', href: '#checkout-' + g }, `Enrol · ${PRICE}`, el('span', { class: 'arr' }, ' →')));
    const bar = (label, v) => el('div', { class: 'mvbar' }, el('span', {}, label), el('span', { class: 'pbar' }, el('i', { style: `width:${Math.min(100, v)}%` })), el('b', {}, `${v}% / ${Core.MOVE_ON}%`));
    return el('section', { class: 'card lockcard', id: 'stageLocked' }, el('h2', {}, `🔒 Cambridge ${Core.stageName(g)} is locked`),
      el('p', {}, `You are studying Stage ${lv}. Each learner studies one stage at a time. Finish at least ${Core.MOVE_ON}% of the lessons and ${Core.MOVE_ON}% of the Unit Tests of Stage ${lv} to get your certificate and open the next stage.`),
      bar('Lessons finished', p.lessons), bar('Unit Tests passed', p.tests),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn primary small', href: '#stage-' + Core.STAGE }, `Back to my Stage ${lv}`, el('span', { class: 'arr' }, ' →'))));
  }
  // choose (or complete) a plan for the learner's stage: one subject, or every subject of the stage
  async function viewPlans() {
    const m = $main(); const lv = Core.learnerStage(); const e = errBox();
    const avail = Core.subjectKeys(lv).filter(k => !Core.stageLocked(k)), todo = avail.filter(k => !Core.enrolled(k));
    pageHero('YOUR PLAN', `Cambridge Stage ${lv}`, Core.myCourses().length ? 'Add another subject of your stage.' : 'Choose what you want to study in your stage.');
    if (!todo.length) { m.append(el('section', { class: 'card done' }, el('h2', {}, `✓ You have every subject of Stage ${lv}`), el('a', { class: 'btn primary small', href: '#home' }, 'Go to my dashboard'))); return; }
    const buy = async (keys, amount, btn) => { e.textContent = ''; btn.disabled = true; btn.classList.add('busy');
      try { await Core.buy(keys, amount); await Core.ensureOwnStage(); C = Core.C; st = Core.cur(); confetti(); toast(`You are enrolled in Stage ${lv}.`); go('home'); }
      catch (x) { btn.disabled = false; btn.classList.remove('busy'); e.textContent = buyErr(x); } };
    const sec = el('section', { class: 'card narrow', id: 'plans' }, el('h2', {}, 'Choose your plan'));
    if (todo.length >= 2) { const b = el('button', { class: 'btn gold', type: 'button', id: 'buyBundle', onclick: () => buy(todo, `Stage ${lv} · ${todo.length} subjects ${priceFor(todo.length)}`, b) }, `${todo.length === avail.length ? 'Whole Stage ' + lv : 'All ' + todo.length + ' subjects'} · ${priceFor(todo.length)}`);
      sec.append(el('div', { class: 'ordrow' }, el('span', {}, `⭐ Every subject of Stage ${lv}: ${todo.map(SUBJ_NAME).join(', ')}`), b)); }
    todo.forEach(k => { const b = el('button', { class: 'btn', type: 'button', 'data-course': k, onclick: () => buy([k], PRICE, b) }, `${PRICE}`);
      sec.append(el('div', { class: 'ordrow' }, el('span', {}, `${SUBJ_ICON(k)} ${SUBJ_NAME(k)} · Stage ${lv}`), b)); });
    sec.append(el('p', { class: 'muted', id: 'oneTimeNote' }, 'Pay once – no subscription. Your course stays open as long as you study at least once a year; after 365 days without study it closes and must be bought again.'),
      PAID ? el('div', {}) : el('div', { class: 'banner info' }, el('b', {}, 'Test checkout. '), 'No money is taken on the test server.'), e);
    m.append(sec);
  }
  async function viewCheckout(g) {
    const m = $main();
    if (Core.stageLocked(g)) return go('stage-' + g);
    if (Core.enrolled(g)) return go('stage-' + g);
    if (!isGuest() && !(await Core.canBuy(g))) { pageHero('ENROL', `Cambridge ${Core.stageName(g)} course`, ''); m.append(await buyOrLockCard(g)); return; }
    pageHero('ENROL', `Cambridge ${Core.stageName(g)} course`, 'Each stage is a separate course with its own Unit Tests, end-of-year exams and certificate.');
    m.append(crumbs(el('a', { href: '#stage-' + g }, `Cambridge ${Core.stageName(g)}`), 'Checkout'));
    if (isGuest()) { m.append(guestWall('Create a free account first')); return; }
    const msg = errBox();
    m.append(el('section', { class: 'card narrow', id: 'checkout' }, el('h2', {}, 'Order summary'),
      el('div', { class: 'ordrow' }, el('span', {}, `Cambridge ${Core.levelName(g)} ${Core.subjectOf(g)} · Cambridge ${Core.stageName(g)} (Camday course)`), el('b', {}, PRICE)),
      el('div', { class: 'ordrow' }, el('span', {}, 'Learner'), el('b', {}, st.name)),
      el('p', { class: 'muted' }, 'Pay once – no subscription. The course stays open as long as you study at least once a year.'),
      PAID ? el('div', {}) : el('div', { class: 'banner info' }, el('b', {}, 'Test checkout. '), 'This is the test server: pressing Pay enrols you straight away and no money is taken.'),
      msg, el('button', { class: 'btn gold big', type: 'button', id: 'payBtn', onclick: async ev => { const pb = ev.currentTarget; pb.disabled = true; pb.classList.add('busy'); msg.textContent = '';
        try { await Core.buy([g], PRICE); pb.classList.remove('busy'); confetti(); toast(`You are enrolled in Cambridge ${Core.stageName(g)}.`); go('stage-' + g); } catch (x) { pb.disabled = false; pb.classList.remove('busy'); msg.textContent = buyErr(x); } } }, PAID ? `Pay ${PRICE}` : `Pay ${PRICE} (test)`)));
  }

  /* ---------- question bank ---------- */
  function viewBank() {
    const m = $main();
    const DEF = { sec: 'all', tier: 'all', diff: 'all', type: 'all', status: 'all', obj: 'all' };
    UI.bank = Object.assign({}, DEF, { q: '', sort: 'id', n: 40, sel: {} }, UI.bank || {}); const F = UI.bank;
    if (F.unit !== Core.UNIT) { F.sel = {}; F.n = 40; F.unit = Core.UNIT; if (F.sec !== 'all' && !C.sections.some(s => s.id === F.sec)) F.sec = 'all'; }
    pageHero(`CAMBRIDGE ${Core.stageName(Core.STAGE).toUpperCase()} · ALL ${Core.unitCount()} UNITS`, 'Question Bank', `Every practice question of Cambridge ${Core.stageName(Core.STAGE)}, unit by unit. Choose a unit, then narrow the list with the filters. Tick questions to practise exactly the ones you want.`);
    const doneIn = n => Object.values((Core.S.states[Core.unitId(n)] || {}).items || {}).filter(x => x && x.done).length;
    const strip = el('div', { class: 'bankunits' });
    const nudge = d => strip.scrollBy({ left: d * Math.max(220, strip.clientWidth * 0.8), behavior: 'smooth' });
    m.append(el('section', { class: 'card bkpick', id: 'bankUnits' }, el('div', { class: 'bkhead' }, el('b', { class: 'lex' }, 'Choose a unit'), el('span', { class: 'muted' }, `${Core.INDEX.units.filter(u => u.ready).length} units`), el('span', { class: 'grow' }),
      el('button', { type: 'button', class: 'bkarrow', 'aria-label': 'Earlier units', onclick: () => nudge(-1) }, '‹'), el('button', { type: 'button', class: 'bkarrow', 'aria-label': 'Later units', onclick: () => nudge(1) }, '›')), strip));
    strip.append(...Core.INDEX.units.filter(u => u.ready).map(u => { const d = Math.min(doneIn(u.n), u.qs || 0), pct = u.qs ? Math.round(d / u.qs * 100) : 0;
        const b = el('button', { type: 'button', class: 'bunit' + (u.n === Core.UNO ? ' on' : ''), 'aria-pressed': String(u.n === Core.UNO), 'data-unit': u.n, onclick: () => { if (u.n === Core.UNO) return; F.sec = 'all'; F.obj = 'all'; b.classList.add('busy'); Loading.busy(b, Core.switchUnit(u.n)).then(() => render()); } },
          unitIcon(u.n), el('span', {}, el('b', {}, `Unit ${u.n}`), el('br'), el('small', {}, u.t)), el('span', { class: 'bpct' }, el('span', { class: 'pbar' }, el('i', { style: `width:${pct}%` })), el('small', {}, `${d}/${u.qs}`)));
        return b; }));
    requestAnimationFrame(() => { const on = strip.querySelector('.bunit.on'); if (on) strip.scrollLeft = Math.max(0, on.offsetLeft - strip.offsetLeft - 12); });
    const s0 = C.sections[0];
    const sumBox = el('section', { class: 'card qbsum', id: 'bankSummary' }); m.append(sumBox);

    // ---- what each filter means ----
    st.marks = st.marks || {};
    const ALL = allQs();
    const SEC = {}, TIER = {}; C.sections.forEach(s => { s.req.forEach(q => { SEC[q.id] = s.id; TIER[q.id] = 'req'; }); s.prac.forEach(q => { SEC[q.id] = s.id; TIER[q.id] = q.adv ? 'adv' : 'prac'; }); s.adv.forEach(q => { SEC[q.id] = s.id; TIER[q.id] = 'adv'; }); (s.more || []).forEach(q => { SEC[q.id] = s.id; TIER[q.id] = 'prac'; }); (s.ext || []).forEach(q => { SEC[q.id] = s.id; TIER[q.id] = 'ext'; }); });
    const isFig = q => ['label', 'scale', 'graph', 'table', 'grid', 'sim'].includes(q.type) || !!q.fig;
    const TYPE = { fig: isFig, calc: q => ['num', 'scale', 'table', 'expr'].includes(q.type), explain: q => q.type === 'explain' || q.type === 'para', mcq: q => ['mcq', 'multi'].includes(q.type), other: q => !['mcq', 'multi', 'num', 'scale', 'table', 'expr', 'explain', 'para'].includes(q.type) && !isFig(q) };
    const STATUS = { todo: q => !(st.items[q.id] || {}).done, done: q => !!(st.items[q.id] || {}).done, wrong: q => !!(st.items[q.id] || {}).everWrong, first: q => { const r = st.items[q.id] || {}; return !!(r.done && r.ok && r.tries === 1); }, mark: q => !!st.marks[q.id] };
    const objs = Array.from(new Set(ALL.map(q => q.obj).filter(Boolean))).sort((x, y) => x.localeCompare(y, 'en', { numeric: true }));
    const DIMS = [
      { k: 'sec', label: 'Section', opts: [['all', 'All sections']].concat(C.sections.map(s => [s.id, `${s.id} ${s.title}`])), test: (q, v) => SEC[q.id] === v },
      { k: 'tier', label: 'Set', opts: [['all', 'All sets'], ['req', 'Core'], ['prac', 'Practice'], ['adv', '* Advanced'], ['ext', 'Extreme']], test: (q, v) => TIER[q.id] === v },
      { k: 'diff', label: 'Difficulty', opts: [['all', 'Any difficulty'], ['M', 'Medium'], ['H', 'Hard'], ['VH', 'Very hard']], test: (q, v) => q.diff === v },
      { k: 'type', label: 'Question type', opts: [['all', 'Any type'], ['mcq', 'Multiple choice'], ['calc', 'Calculations'], ['fig', 'Diagrams & data'], ['explain', 'Written'], ['other', 'Other (match, order…)']], test: (q, v) => TYPE[v](q) },
      { k: 'status', label: 'My progress', opts: [['all', 'Everything'], ['todo', 'Not done yet'], ['done', 'Done'], ['wrong', 'Got wrong before'], ['first', 'Right first try'], ['mark', '★ Bookmarked']], test: (q, v) => STATUS[v](q) },
      { k: 'obj', label: 'Learning objective', opts: [['all', 'All objectives']].concat(objs.map(o => [o, o])), test: (q, v) => q.obj === v }];
    const text = q => (q.id + ' ' + q.prompt + ' ' + (q.ctx || '') + ' ' + ((q.options || []).map(o => o.t).join(' '))).toLowerCase();
    const TXT = {}; ALL.forEach(q => { TXT[q.id] = text(q); });
    const okExcept = (q, skip) => DIMS.every(d => d.k === skip || F[d.k] === 'all' || d.test(q, F[d.k])) && (!F.q || TXT[q.id].includes(F.q.toLowerCase()));
    const DORD = { M: 1, H: 2, VH: 3 };
    const SORT = { id: null, easy: (a, b) => (DORD[a.diff] || 0) - (DORD[b.diff] || 0), hard: (a, b) => (DORD[b.diff] || 0) - (DORD[a.diff] || 0), todo: (a, b) => (STATUS.done(a) ? 1 : 0) - (STATUS.done(b) ? 1 : 0), wrong: (a, b) => (STATUS.wrong(b) ? 1 : 0) - (STATUS.wrong(a) ? 1 : 0) };

    // ---- unit summary: how much is done, and one-tap sets ----
    const nDone = ALL.filter(STATUS.done).length, nWrong = ALL.filter(STATUS.wrong).length, nMark = ALL.filter(STATUS.mark).length, pctU = ALL.length ? Math.round(nDone / ALL.length * 100) : 0;
    const quick = (id, n, label, sub, v) => el('button', { type: 'button', class: 'qbquick', id, 'data-v': v, onclick: () => { F.status = F.status === v ? 'all' : v; F.n = 40; update(); } }, el('b', {}, String(n)), el('span', {}, label), el('small', {}, sub));
    sumBox.append(el('div', { class: 'qbsum-l' }, el('span', { class: 'hl' }, `Unit ${Core.UNO}`), el('h2', {}, C.unit.title),
        el('p', {}, `${ALL.length} questions. Practising here never changes your Core progress or test scores.`),
        el('div', { class: 'qbsum-bar' }, el('div', { class: 'pbar' + (pctU === 100 ? ' ok' : '') }, el('i', { style: `width:${pctU}%` })), el('b', {}, `${nDone} of ${ALL.length} done`))),
      el('div', { class: 'qbquicks' }, quick('qkTodo', ALL.length - nDone, 'Not done yet', 'Start with these', 'todo'), quick('qkWrong', nWrong, 'Got wrong before', 'Worth another try', 'wrong'), quick('qkMark', nMark, 'Bookmarked', 'Saved by you', 'mark')));
    // section and set as tabs (the same filters as the menus below)
    const tabRow = (k, label) => { const d = DIMS.find(x => x.k === k); return el('div', { class: 'qbtabs', 'data-k': k, role: 'group', 'aria-label': label }, el('span', { class: 'qbtabl' }, label),
      ...d.opts.map(([v, tx]) => el('button', { type: 'button', class: 'chip', 'data-v': v, onclick: () => { F[k] = v; F.n = 40; update(); } }, k === 'sec' && v !== 'all' ? v : tx.replace('* ', '')))); };
    const tabs = el('div', { class: 'qbtabwrap', id: 'bankTabs' }, tabRow('sec', 'Topic'), tabRow('tier', 'Set'));

    // ---- the filter panel ----
    const selects = {};
    const grid = el('div', { class: 'qbgrid' }, ...DIMS.map(d => { const id = 'bf-' + d.k;
      const sel = el('select', { id, onchange: () => { F[d.k] = sel.value; F.n = 40; update(); } }); selects[d.k] = sel;
      return el('div', { class: 'qbsel', 'data-k': d.k }, el('label', { for: id }, d.label), sel); }));
    const sIn = el('input', { type: 'search', id: 'bankSearch', placeholder: 'Search words in the question', value: F.q || '', 'aria-label': 'Search the questions', autocomplete: 'off' });
    const sX = el('button', { type: 'button', class: 'qbx', 'aria-label': 'Clear the search', hidden: !F.q, onclick: () => { sIn.value = ''; F.q = ''; sX.hidden = true; update(); sIn.focus(); } }, '×');
    let sT = null; const runSearch = () => { clearTimeout(sT); const v = sIn.value.trim(); sX.hidden = !v; if (v === (F.q || '')) return; F.q = v; F.n = 40; update(); };
    sIn.addEventListener('input', () => { clearTimeout(sT); sT = setTimeout(runSearch, 180); }); sIn.addEventListener('keydown', e => { if (e.key === 'Enter') runSearch(); }); sIn.addEventListener('search', runSearch);
    const search = el('div', { class: 'qbsearch', role: 'search' }, el('span', { html: AtomicIcons.html('search', { size: 18, color: '#575757' }) }), sIn, sX);
    const active = el('div', { class: 'qbactive', 'aria-live': 'polite' });
    const panel = el('section', { class: 'card qbf' + (UI.bankFold ? ' closed' : ''), id: 'bankFilters', 'aria-label': 'Filters' },
      el('div', { class: 'qbf-top' }, el('b', { class: 'lex', style: 'font-size:18px' }, 'Filters'), search,
        el('button', { type: 'button', class: 'btn small ghost qbfold', 'aria-expanded': String(!UI.bankFold), onclick: e => { UI.bankFold = !UI.bankFold; panel.classList.toggle('closed', UI.bankFold); e.currentTarget.setAttribute('aria-expanded', String(!UI.bankFold)); e.currentTarget.textContent = UI.bankFold ? 'Show filters' : 'Hide filters'; } }, UI.bankFold ? 'Show filters' : 'Hide filters')),
      tabs, grid, active);
    m.append(panel);

    // ---- results bar: count, sort, selection, practise ----
    const count = el('span', { class: 'qbcount', id: 'bankCount' });
    const sortSel = el('select', { id: 'bankSort', 'aria-label': 'Sort the questions', onchange: () => { F.sort = sortSel.value; update(); } },
      ...[['id', 'Course order'], ['easy', 'Easiest first'], ['hard', 'Hardest first'], ['todo', 'Not done first'], ['wrong', 'Got wrong first']].map(([v, t]) => el('option', { value: v, selected: F.sort === v }, t)));
    const allBox = el('input', { type: 'checkbox', id: 'bankAll', 'aria-label': 'Tick every question in the list' });
    const pickBtn = el('button', { class: 'btn small navy', type: 'button', id: 'bankPick' });
    const pracBtn = el('button', { class: 'btn primary small shine', type: 'button', id: 'bankPractise' });
    const selIds = () => Object.keys(F.sel).filter(k => F.sel[k]);
    m.append(el('div', { class: 'qbbar' }, count, el('span', { class: 'grow' }),
      el('div', { class: 'qbsel' }, el('label', { for: 'bankSort', style: 'margin:0' }, 'Sort'), sortSel), pickBtn, pracBtn,
      el('a', { class: 'btn small', href: '#topic' }, 'Revise by topic')));
    const tbl = el('div', { class: 'card lbtable qbt', id: 'bankTable' });
    m.append(tbl);

    const dots = d => el('span', { class: 'dd ' + d, title: QE.DIFF[d] || d, 'aria-label': QE.DIFF[d] || d }, ...[1, 2, 3].map(i => el('i', { class: i <= (DORD[d] || 1) ? 'f' : '' })));
    let list = [];
    function row(q) {
      const r = st.items[q.id] || {}, t = TIER[q.id];
      const cb = el('input', { type: 'checkbox', 'aria-label': 'Choose ' + q.id, checked: !!F.sel[q.id] });
      const line = el('div', { class: 'lbrow' + (F.sel[q.id] ? ' picked' : ''), 'data-q': q.id });
      cb.addEventListener('change', () => { F.sel[q.id] = cb.checked; line.classList.toggle('picked', cb.checked); bar(); });
      const mk = el('button', { type: 'button', class: 'chip' + (st.marks[q.id] ? ' on' : ''), 'aria-pressed': String(!!st.marks[q.id]), 'aria-label': 'Bookmark ' + q.id, style: 'min-height:44px;min-width:44px;padding:0 10px', onclick: e => { e.stopPropagation(); st.marks[q.id] = !st.marks[q.id]; Core.persist(); mk.classList.toggle('on'); mk.setAttribute('aria-pressed', String(!!st.marks[q.id])); } },AtomicIcons.ic('star'));
      line.append(el('span', {}, cb), el('span', { class: 'c-id qbnum', title: q.id }, String(ALL.indexOf(q) + 1)),
        el('span', { style: 'min-width:0' }, el('span', { class: 'qbq' }, q.prompt.replace(/^\* Advanced\.\s*/, '')), el('small', { class: 'qbmeta' }, el('span', { class: 'qbm' }, `Topic ${SEC[q.id]}`), el('span', { class: 'qbm' }, QE.TYPE_VI[q.type]), el('span', { class: 'qbm' }, dots(q.diff), ` ${QE.DIFF[q.diff] || ''}`))),
        el('span', { class: 'c-set' }, el('span', { class: 'tag ' + (t === 'adv' ? 'adv' : t === 'req' ? 'd-M' : '') }, t === 'req' ? 'Core' : t === 'adv' ? '* Advanced' : t === 'ext' ? 'Extreme' : 'Practice')),
        el('span', { class: 'c-st' }, r.done ? el('span', { class: 'status done' }, r.ok ? (r.tries === 1 ? 'Right 1st try' : 'Correct') : 'Completed') : r.tries ? el('span', { class: 'tag d-VH' }, 'In progress') : el('span', { class: 'status todo' }, 'Not done')),
        el('span', { class: 'qbacts' }, mk, el('button', { type: 'button', class: 'btn small' + (r.done ? '' : ' primary'), style: 'padding:0 14px', onclick: () => startDrill(`Question ${ALL.indexOf(q) + 1}`, [q], 'bank') }, r.done ? 'Redo' : 'Answer')));
      return line;
    }
    function bar() {
      const shown = list.slice(0, F.n), picked = selIds();
      count.textContent = ''; count.append(`${list.length} question${list.length === 1 ? '' : 's'}`, el('small', {}, list.length === ALL.length ? 'all of this unit' : `of ${ALL.length}`));
      pickBtn.textContent = picked.length ? `Practise ticked (${picked.length})` : 'Tick questions to choose'; pickBtn.disabled = !picked.length;
      pickBtn.onclick = () => { const qs = ALL.filter(q => F.sel[q.id]).slice(0, 30); startDrill(`Question Bank · ${qs.length} chosen question${qs.length === 1 ? '' : 's'}`, qs, 'bank'); };
      pracBtn.textContent = ''; pracBtn.append(`Practise ${Math.min(15, list.length)}`, el('span', { class: 'arr' }, '→')); pracBtn.disabled = !list.length;
      pracBtn.onclick = () => startDrill(`Question Bank · ${list.length > 15 ? 'first 15 of ' + list.length : list.length} questions`, list.slice(0, 15), 'bank');
      allBox.checked = shown.length > 0 && shown.every(q => F.sel[q.id]); allBox.indeterminate = !allBox.checked && shown.some(q => F.sel[q.id]);
    }
    allBox.addEventListener('change', () => { list.slice(0, F.n).forEach(q => { F.sel[q.id] = allBox.checked; }); tbl.querySelectorAll('.lbrow[data-q]').forEach(x => { x.classList.toggle('picked', allBox.checked); const c = x.querySelector('input'); if (c) c.checked = allBox.checked; }); bar(); });
    function update() {
      // each option shows how many questions it would leave, given the other filters
      DIMS.forEach(d => { const sel = selects[d.k], base = ALL.filter(q => okExcept(q, d.k)); sel.textContent = '';
        d.opts.forEach(([v, t]) => { const n = v === 'all' ? base.length : base.filter(q => d.test(q, v)).length; sel.append(el('option', { value: v, selected: F[d.k] === v, disabled: !n && F[d.k] !== v && v !== 'all' }, `${t} (${n})`)); });
        sel.value = F[d.k]; sel.closest('.qbsel').classList.toggle('set', F[d.k] !== 'all'); });
      tabs.querySelectorAll('.qbtabs').forEach(g => g.querySelectorAll('.chip').forEach(c => { const onn = F[g.dataset.k] === c.dataset.v; c.classList.toggle('on', onn); c.setAttribute('aria-pressed', String(onn)); }));
      sumBox.querySelectorAll('.qbquick').forEach(b => { const onn = F.status === b.dataset.v; b.classList.toggle('on', onn); b.setAttribute('aria-pressed', String(onn)); });
      active.textContent = '';
      const on = DIMS.filter(d => F[d.k] !== 'all');
      on.forEach(d => { const o = d.opts.find(x => x[0] === F[d.k]); active.append(el('span', { class: 'qbpill' }, `${d.label}: ${o ? o[1] : F[d.k]}`, el('button', { type: 'button', 'aria-label': `Remove the ${d.label} filter`, onclick: () => { F[d.k] = 'all'; F.n = 40; update(); } }, '×'))); });
      if (F.q) active.append(el('span', { class: 'qbpill' }, `Search: “${F.q}”`, el('button', { type: 'button', 'aria-label': 'Clear the search', onclick: () => { F.q = ''; sIn.value = ''; sX.hidden = true; update(); } }, '×')));
      if (on.length || F.q) active.append(el('button', { type: 'button', class: 'qbclear', id: 'bankClear', onclick: () => { Object.assign(F, DEF, { q: '', n: 40 }); sIn.value = ''; sX.hidden = true; update(); } }, 'Clear all'));
      else active.append(el('span', { class: 'qbhint' }, 'Tip: each choice shows how many questions it leaves. Combine filters to find exactly what you need.'));
      list = ALL.filter(q => okExcept(q, null)); if (SORT[F.sort]) list = list.slice().sort(SORT[F.sort]);
      tbl.textContent = '';
      tbl.append(el('div', { class: 'lbrow h' }, el('span', {}, allBox), el('span', { class: 'c-id' }, 'NO.'), el('span', {}, 'QUESTION'), el('span', { class: 'c-set' }, 'SET'), el('span', { class: 'c-st' }, 'STATUS'), el('span', {}, '')));
      list.slice(0, F.n).forEach(q => tbl.append(row(q)));
      if (!list.length) tbl.append(el('div', { class: 'qbempty' }, el('b', { class: 'lex', style: 'font-size:18px' }, 'No questions match these filters'), el('span', { class: 'muted' }, 'Remove a filter or clear them all to see more.'),
        el('button', { type: 'button', class: 'btn small', onclick: () => { Object.assign(F, DEF, { q: '', n: 40 }); sIn.value = ''; sX.hidden = true; update(); } }, 'Clear all filters')));
      if (list.length > F.n) tbl.append(el('div', { class: 'qbmore' }, el('button', { type: 'button', class: 'btn small', id: 'bankMore', onclick: () => { F.n += 40; update(); } }, `Show ${Math.min(40, list.length - F.n)} more (${list.length - F.n} left)`)));
      bar();
    }
    update();
  }

  /* ---------- tester tools (preview only) ---------- */
  function testerTools() {
    if (!Backend.demo) return null;
    const msg = el('span', { class: 'muted', 'aria-live': 'polite' });
    const fill = (sids, opts) => { sids.forEach(sid => { const s = Core.sec(sid), vs = Core.vstate(st, sid); s.stops.forEach(x => vs.stops[x.id] = vs.stops[x.id] && vs.stops[x.id].done ? vs.stops[x.id] : { done: true, ok: true, tries: 1, sim: true }); vs.completed = true; vs.pos = 0;
      s.req.forEach(q => { if (!(st.items[q.id] || {}).done) st.items[q.id] = { done: true, ok: true, tries: 1, score: 1, sim: true }; }); }); Core.persist(); };
    const btn = (t, f, id) => el('button', { class: 'btn small', type: 'button', id, onclick: () => { f(); msg.textContent = 'Done – ' + t + '.'; setTimeout(render, 500); } }, t);
    return el('section', { class: 'card', style: 'border:2px dashed #F3BF69' }, el('span', { class: 'eyebrow' }, 'PREVIEW ONLY'), el('h3', { style: 'margin:2px 0 6px' }, 'Tester tools'),
      el('p', { class: 'muted', style: 'margin:0 0 8px' }, `Jump ahead to try every feature without answering all ${C.sections.reduce((a, s) => a + s.req.length + s.prac.length + s.adv.length, 0)} questions.` + ' Simulated items count as done with full marks and are flagged “sim” in the data.'),
      el('div', { class: 'btnrow' }, ...C.sections.map(s => btn(`Complete ${s.id}`, () => fill([s.id]), 'sim' + R(s.id))),
        btn('Complete all sections → Unit Test', () => { fill(C.sections.map(s => s.id)); }, 'simAll'),
        el('button', { class: 'btn small', type: 'button', id: 'simOthers', onclick: async () => { await Backend.demo.simulateOtherUnits(st.id, 82); await Core.refreshResults(st); msg.textContent = `Done – the other ${Core.unitCount() - 1} units are marked as passed at 82%.`; setTimeout(render, 500); } }, 'Pass the other 13 units (82%)'),
        el('button', { class: 'btn small', type: 'button', id: 'simLessons', onclick: async () => { for (const u of Core.INDEX.units) { const key = Core.unitId(u.n), s0 = key === Core.UNIT ? st : (Core.S.states[key] || {}); s0.video = s0.video || {};
          for (const s of u.sections || []) s0.video[s.id] = Object.assign({ pos: 0, stops: {} }, s0.video[s.id], { completed: true }); if (key !== Core.UNIT) { Core.S.states[key] = s0; await Backend.saveProgress(st.id, key, s0); } }
          Core.persist(); msg.textContent = 'Done – every lesson of this stage is marked as finished.'; setTimeout(render, 500); } }, 'Finish every lesson'),
        el('button', { class: 'btn small', type: 'button', id: 'simFinal', onclick: async () => { Backend.demo.simulateFinal(st.id, 80); await Core.refreshFinal(); msg.textContent = 'Done – an end-of-year exam is marked as passed at 80%.'; setTimeout(render, 500); } }, 'Pass an end-of-year exam (80%)'),
        el('button', { class: 'btn small', type: 'button', id: 'simXp', onclick: async () => { Backend.demo.simulateXp(st.id, 400); await Core.selectLearner(st.id); msg.textContent = 'Done – +4 800 XP (level 10).'; setTimeout(render, 500); } }, 'Add XP to reach level 10'),
        el('button', { class: 'btn small', type: 'button', id: 'simStaff', onclick: () => { Backend.demo.setRole('admin'); msg.textContent = 'This account is now an administrator – open Staff from the account menu.'; } }, 'Make this account staff'),
        el('button', { class: 'btn small ghost', type: 'button', id: 'resetUnit', onclick: () => modal(`Reset Unit ${Core.UNO}?`, `This clears all Unit ${Core.UNO} progress, tests, certificate and ranking score for this learner.`, [{ t: 'Cancel', cls: 'ghost' }, { t: 'Reset', cls: 'primary', on: async () => { await Backend.demo.resetLearner(st.id); await Core.selectLearner(st.id); go('home'); } }]) }, `Reset Unit ${Core.UNO} progress`)), msg);
  }

  /* ---------- router ---------- */

  /* ---------- exam room: shared by Unit Tests (45 min) and end-of-year exams (60 min) ---------- */
  let timer = null;
  const mmss = t => { t = Math.max(0, Math.ceil(t / 1000)); return `${Math.floor(t / 60)}:${String(t % 60).padStart(2, '0')}`; };
  /* ---------- strict exam room: full screen, the site is closed, leaving is recorded; the 3rd time away hands the paper in ---------- */
  const EXAM_MAX_LEAVES = 3;
  const Guard = { on: false, route: '', draft: null, save: null, submit: null, last: 0, exiting: false };
  function fsOn() { const d = document.documentElement; try { if (!document.fullscreenElement && d.requestFullscreen) d.requestFullscreen({ navigationUI: 'hide' }).catch(() => { }); } catch (e) { } }
  function guardOn(route, draft, save) { Guard.on = true; Guard.route = route; Guard.draft = draft; Guard.save = save; document.body.classList.add('exam-mode'); }
  function guardOff() {
    Guard.on = false; Guard.draft = null; Guard.submit = null; document.body.classList.remove('exam-mode'); document.querySelectorAll('.leavewarn').forEach(x => x.remove());
    if (document.fullscreenElement && document.exitFullscreen) { Guard.exiting = true; document.exitFullscreen().catch(() => { }).finally(() => { setTimeout(() => { Guard.exiting = false; }, 300); }); }
  }
  function leaveWarn(d) {
    document.querySelectorAll('.leavewarn').forEach(x => x.remove());
    const left = EXAM_MAX_LEAVES - d.leaves;
    const box = el('div', { class: 'leavewarn', role: 'alertdialog', 'aria-modal': 'true', 'aria-label': 'You left the exam room' }, el('div', { class: 'lwbox' },
      el('span', { class: 'eyebrow', style: 'color:#B42318' }, `WARNING ${d.leaves} OF ${EXAM_MAX_LEAVES - 1}`), el('h2', {}, '⚠ You left the exam room'),
      el('p', {}, `The clock kept running. This has been recorded with your paper. If you leave ${left === 1 ? 'once more' : left + ' more times'}, your paper is handed in automatically.`),
      el('button', { class: 'btn primary big', type: 'button', id: 'backToExam', onclick: () => { fsOn(); box.remove(); } }, 'Return to the exam')));
    document.body.append(box); box.querySelector('button').focus();
  }
  function leave(kind) {
    if (!Guard.on || !Guard.draft || UI.submitting) return; const now = Date.now(); if (now - Guard.last < 2000) return; Guard.last = now;
    const d = Guard.draft; d.leaves = (d.leaves || 0) + 1; (d.leaveLog = d.leaveLog || []).push({ kind, at: new Date().toISOString() }); Guard.save();
    if (d.leaves >= EXAM_MAX_LEAVES) {
      document.querySelectorAll('.leavewarn').forEach(x => x.remove());
      modal('Paper handed in', `You left the exam room ${d.leaves} times, so your paper has been handed in automatically.`, []);
      setTimeout(() => { document.querySelectorAll('.modal-bg').forEach(b => b.remove()); if (Guard.submit) Guard.submit('leaves'); }, 1200); return;
    }
    leaveWarn(d);
  }
  document.addEventListener('visibilitychange', () => { if (document.hidden) leave('tab'); });
  document.addEventListener('fullscreenchange', () => { if (!document.fullscreenElement && !Guard.exiting) leave('fullscreen'); });
  window.addEventListener('beforeunload', e => { if (Guard.on) { e.preventDefault(); e.returnValue = ''; } });
  const leavesNote = a => a && a.leaves ? el('p', { class: 'muted', style: 'margin:4px 0' }, `Left the exam room ${a.leaves} time${a.leaves > 1 ? 's' : ''}${a.autoSubmitted ? ' – the paper was handed in automatically' : ''}.`) : null;
  function examRoom(X) {   // X: { title, badge, qs, max, minutes, draft, save, seed, deadline, onSubmit(answers) }
    const m = $main(); const qs = X.qs, draft = X.draft; const route = location.hash.slice(1);
    if (!Guard.on || Guard.route !== route) {
      if (draft.inRoom) { draft.leaves = (draft.leaves || 0) + 1; (draft.leaveLog = draft.leaveLog || []).push({ kind: 'reopened', at: new Date().toISOString() }); }   // the page was closed or reloaded mid-paper
      draft.inRoom = true; X.save(); guardOn(route, draft, X.save);
      if ((draft.leaves || 0) > 0 && draft.leaves < EXAM_MAX_LEAVES) setTimeout(() => leaveWarn(draft), 50);
    }
    Guard.submit = reason => send(reason);
    if ((draft.leaves || 0) >= EXAM_MAX_LEAVES) setTimeout(() => send('leaves'), 50);
    const clock = el('span', { class: 'examclock', id: 'examClock', role: 'timer', 'aria-live': 'off' });
    subbar('', el('span', { class: 'ttl' }, X.title), el('span', { class: 'exam-badge' }, X.badge || 'EXAM ROOM'), clock);
    const i = Math.min(UI.testIdx || 0, qs.length - 1), q = qs[i];
    const answered = x => draft.answers[x.id] != null && draft.answers[x.id] !== '' && !(Array.isArray(draft.answers[x.id]) && !draft.answers[x.id].length);
    let warned = false, done = false;
    const tick = () => { const left = X.deadline - Date.now(); clock.textContent = '⏱ ' + mmss(left) + ' left'; clock.classList.toggle('warn', left < 5 * 60000); clock.classList.toggle('crit', left < 60000);
      if (left < 5 * 60000 && !warned) { warned = true; toast('5 minutes left – check your answers.'); }
      if (left <= 0 && !done) { done = true; clearInterval(timer); finish(true); } };
    clearInterval(timer); timer = setInterval(tick, 1000); tick();
    const saved = el('span', { class: 'muted', 'aria-live': 'polite' });
    const card = el('section', { class: 'card qcard', style: 'flex:999 1 600px;min-width:0' },
      el('div', { class: 'btnrow between', style: 'margin:0' }, el('span', { class: 'lex', style: 'font-weight:700;color:#556377' }, `Question ${i + 1} of ${qs.length} · ${q.pts} mark${q.pts > 1 ? 's' : ''}${q.teacher ? (q.type === 'para' ? ' · written paragraph: checked against the mark scheme, a teacher marks it if needed' : ' · marked by an Camday marker') : ''}`),
        el('button', { class: 'chip' + (UI.flags[q.id] ? ' on' : ''), type: 'button', 'aria-pressed': String(!!UI.flags[q.id]), onclick: () => { UI.flags[q.id] = !UI.flags[q.id]; render(); } }, svgI(I.flag, 14), UI.flags[q.id] ? 'Flagged' : 'Flag')),
      el('h2', { class: 'qp', style: 'font-size:24px' }, q.prompt));
    if (q.sec) card.insertBefore(el('div', { class: 'examsec', id: 'examSec' }, el('b', {}, `Section ${q.sec.split(' · ')[0]}`), ' · ' + (q.sec.split(' · ')[1] || '')), card.firstChild);
    QE.renderBody(q, card, { seed: X.seed, resp: draft.answers[q.id], onChange: r => { draft.answers[q.id] = r; draft.ts = Date.now(); X.save(); saved.textContent = 'Draft saved ' + new Date().toLocaleTimeString(); drawNav(); } });
    card.append(el('div', { class: 'btnrow between', style: 'padding-top:16px;border-top:1px solid #E6EEF8' }, el('button', { class: 'btn small', type: 'button', disabled: i === 0, onclick: () => { UI.testIdx = i - 1; render(); } }, '← Previous'), saved,
      i < qs.length - 1 ? el('button', { class: 'btn primary', type: 'button', id: 'testNext', onclick: () => { UI.testIdx = i + 1; render(); } }, 'Next question', el('span', { class: 'arr' }, '→')) : el('button', { class: 'btn navy', type: 'button', onclick: () => finish(false) }, 'Finish')));
    const nav = el('div', { class: 'navgrid' });
    const drawNav = () => { nav.innerHTML = ''; qs.forEach((x, k) => (x.sec && (k === 0 || qs[k - 1].sec !== x.sec) ? nav.append(el('span', { class: 'navsec' }, 'Section ' + x.sec.split(' · ')[0])) : null, nav.append(el('button', { type: 'button', class: (UI.flags[x.id] ? 'flag' : answered(x) ? 'ans' : '') + (k === i ? ' on' : ''), 'aria-label': `Question ${k + 1}${answered(x) ? ', answered' : ''}${UI.flags[x.id] ? ', flagged' : ''}`, onclick: () => { UI.testIdx = k; render(); } }, String(k + 1))))); };
    drawNav();
    async function send(reason) {
      if (UI.submitting) return true; UI.submitting = true; reason = typeof reason === 'string' ? reason : 'student';
      draft.key = draft.key || (crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + Math.random()); X.save();
      const wait = modal('Marking…', 'Please keep this page open.', []);
      try { clearInterval(timer); const meta = { leaves: draft.leaves || 0, auto: reason !== 'student', reason }; guardOff(); await X.onSubmit(draft.answers, draft.key, meta); UI.testOn = false; UI.testIdx = 0; UI.flags = {}; wait(); }
      catch (x) { wait(); guardOn(route, draft, X.save); Guard.submit = r => send(r); modal('Could not submit', errText(x) + ' Your answers are saved as a draft – try again.', [{ t: 'OK', cls: 'primary' }]); }
      finally { UI.submitting = false; }
    }
    function finish(timeUp) {
      if (timeUp) { modal('Time is up', 'Your answers are being submitted now.', []); setTimeout(() => { document.querySelectorAll('.modal-bg').forEach(b => b.remove()); send('time'); }, 900); return; }
      const blank = qs.filter(x => !answered(x)).length;
      modal('Submit your paper?', blank ? `You have ${blank} unanswered question(s) and ${mmss(X.deadline - Date.now())} left. Submit now?` : 'After you submit you will see your score and the solutions.', [{ t: 'Go back', cls: 'ghost' }, { t: 'Submit', cls: 'primary', on: send }]);
    }
    m.append(el('div', { style: 'display:flex;flex-wrap:wrap;gap:26px;align-items:flex-start' }, card,
      el('aside', { class: 'card', style: 'flex:1 1 260px;min-width:0;display:flex;flex-direction:column;gap:14px' }, el('b', { class: 'lex' }, 'Questions'), nav,
        el('div', { class: 'legend' }, el('span', {}, el('i', { style: 'background:#0149AF' }), 'Answered'), el('span', {}, el('i', { style: 'background:#F3BF69' }), 'Flagged'), el('span', {}, el('i', { style: 'border:2px solid #D3E0F4' }), 'Not answered')),
        el('p', { class: 'muted', style: 'margin:0;font-size:13px' }, `When the clock reaches 0:00 your paper is submitted automatically. ${X.max} marks in total.`),
        el('button', { class: 'btn navy small', type: 'button', id: 'submitTest', onclick: () => finish(false) }, 'Finish and submit'))));
  }
  function paperSecs(qs) {   // sections of a paper: [{name, from, to, marks}] (question numbers are 1-based)
    const out = []; (qs || []).forEach((q, k) => { if (!q.sec) return; const l = out[out.length - 1];
      if (l && l.name === 'Section ' + q.sec) { l.to = k + 1; l.marks += q.pts || 0; } else out.push({ name: 'Section ' + q.sec, from: k + 1, to: k + 1, marks: q.pts || 0 }); });
    return out;
  }
  function examIntro(t) {   // the "before you start" card
    return el('section', { class: 'card', style: 'max-width:760px;margin:0 auto;padding:40px;border-radius:28px;display:flex;flex-direction:column;gap:16px' },
      el('span', { class: 'eyebrow' }, 'EXAM ROOM · BEFORE YOU START'), el('h1', { style: 'margin:0;font-size:34px' }, t.title),
      el('div', { class: 'stats3' }, el('div', {}, el('b', {}, String(t.n)), el('br'), el('small', { class: 'muted' }, 'questions')), el('div', {}, el('b', {}, String(t.max)), el('br'), el('small', { class: 'muted' }, 'marks')),
        el('div', {}, el('b', {}, t.minutes + ' min'), el('br'), el('small', { class: 'muted' }, 'time allowed')), el('div', {}, el('b', {}, t.passTxt), el('br'), el('small', { class: 'muted' }, 'to pass'))),
      el('ul', { style: 'margin:0;padding-left:20px;color:#3A4B63' }, el('li', {}, `The clock starts when you press Start and keeps running if you leave the page or close the browser. At 0:00 your answers are submitted automatically.`),
        el('li', {}, 'No hints or videos during the paper. You can flag a question and come back to it; answers are saved as you go.'),
        el('li', {}, el('b', {}, 'Exam conditions: '), `the paper opens full screen and the rest of the site is closed. Leaving the exam room (another tab or app, leaving full screen, Back or reload) is recorded. After ${EXAM_MAX_LEAVES - 1} warnings, the ${EXAM_MAX_LEAVES === 3 ? 'third' : EXAM_MAX_LEAVES + 'th'} time you leave hands your paper in automatically.`), ...(t.extra || []).map(x => el('li', {}, x))),
      t.secs && t.secs.length ? el('table', { class: 'examsecs', id: 'examSecs' }, el('tr', {}, el('th', {}, 'Section'), el('th', {}, 'Questions'), el('th', {}, 'Marks')), ...t.secs.map(x => el('tr', {}, el('td', {}, x.name), el('td', {}, x.from === x.to ? String(x.from) : `${x.from}–${x.to}`), el('td', {}, String(x.marks))))) : null,
      t.resume ? el('div', { class: 'banner info', id: 'draftNote' }, 'This paper is already running – carry on where you stopped. The clock has not stopped.') : null,
      el('button', { class: 'btn primary big shine', type: 'button', id: 'startTest', style: 'align-self:flex-start', onclick: ev => { fsOn(); t.start(ev); } }, t.resume ? 'Back to the exam room' : 'Start – the clock begins', el('span', { class: 'arr' }, '→')));
  }

  /* ---------- Unit Test ---------- */
  function viewTest() {
    const m = $main(); const ts = Core.testState(st);
    const form = ts.form || (ts.last && ts.last.form) || 'A';
    const where = `Unit ${Core.UNO} › Unit Test`;
    const totalCore = C.sections.reduce((a, s) => a + s.req.length, 0);
    if (ts.state === 'guest') { m.append(bar(where), guestWall('Sign up free to take the Unit Test')); return; }
    if (ts.state === 'paywall') { m.append(bar(where), lockScreen(`Unit Test ${Core.UNO} needs the Cambridge ${Core.stageName(Core.STAGE)} course`, 'Unit Tests, marking and the certificate are part of the full course. You buy it once.', [{ what: `the Cambridge ${Core.stageName(Core.STAGE)} course`, route: 'plans' }])); return; }
    if (ts.state === 'locked') { m.append(bar(where), lockScreen(`Unit Test ${Core.UNO} is locked`, `The Unit Test opens when you have ${C.sections[0] && C.sections[0].lesson ? 'read every lesson' : 'watched every video'} and finished all ${totalCore} Core questions in this unit.`, ts.miss)); return; }
    if (ts.state === 'pending') { m.append(bar(where), el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, `Attempt ${ts.last.n} (Paper ${ts.last.form}) has a written answer for an Camday marker to mark. We will notify you when it is done.`), el('a', { class: 'btn primary small', href: '#result' }, 'Results & history'))); return; }
    if (ts.state === 'remediate') { m.append(bar(where), lockScreen('You can\'t retake yet', 'Finish the review questions set for your weaker objectives before you take the equivalent paper.', [{ what: `${ts.left.length} review questions`, route: 'remedial' }])); return; }
    if (ts.state === 'passed') { m.append(bar(where), el('section', { class: 'card done' }, el('h2', {}, `✓ You have passed Unit Test ${Core.UNO}`), el('a', { class: 'btn primary small', href: '#result' }, 'See results'), el('a', { class: 'btn small', href: '#tests' }, 'All tests & exams'))); return; }
    const qs = C.tests[form];
    st.last = { route: 'test' };
    const draft = st.test.drafts[form] = st.test.drafts[form] || { answers: {}, ts: Date.now() };
    const running = !!draft.deadline;
    if (!UI.testOn) {
      m.append(bar(where), examIntro({ title: `Unit Test ${Core.UNO} · Paper ${form}${ts.retake ? ' (equivalent paper)' : ''}`, n: qs.length, max: 30, secs: paperSecs(qs), minutes: TestRules.UNIT_MINUTES, passTxt: '> 70%', resume: running,
        extra: [`Pass to complete Unit ${Core.UNO} and earn +100 XP. Every answer – chosen or typed – is marked automatically the moment you hand the paper in.`],
        start: async ev => { ev.currentTarget.disabled = true; try { const c = await Core.startClock(Core.UNIT, form); draft.deadline = c.deadline; Core.persist(); UI.testOn = true; render(); } catch (x) { ev.currentTarget.disabled = false; modal('Could not open the paper', errText(x), [{ t: 'OK', cls: 'primary' }]); } } }));
      return;
    }
    examRoom({ title: `Unit Test ${Core.UNO} · ${C.unit.title} · Paper ${form}`, qs, max: 30, draft, save: () => Core.persist(), seed: st.id + form, deadline: draft.deadline,
      onSubmit: async (answers, key, meta) => { const r = await Core.submitTest(st, form, answers, key, meta); delete st.test.drafts[form]; Core.persist(); Core.flush(); if (r.attempt.status === 'final' && r.attempt.passed) confetti(); go('result'); } });
  }

  /* ---------- Tests & exams hub: every Unit Test of the stage + the end-of-year exams ---------- */
  async function viewTests() {
    const m = $main(); await Core.refreshFinal().catch(() => { });
    const li = Core.levelInfo(), F = await Core.loadFinal();
    pageHero(`CAMBRIDGE ${Core.stageName(Core.STAGE).toUpperCase()} · EXAM ROOM`, 'Tests & exams', `Every Unit Test is timed (${TestRules.UNIT_MINUTES} minutes, 30 marks, pass above 70%). Open any unit's test whenever you are ready.`,
      [statCard(el('span', { class: 'ti big' }, '📝'), `${Object.keys(st.results || {}).filter(k => k.startsWith(`stage${Core.STAGE}-unit`)).length} / ${Core.unitCount()}`, 'Unit Tests passed'), statCard(el('span', { class: 'ti big' }, '⭐'), `Level ${li.level}`, `${li.xp} XP`)]);
    const rows = Core.INDEX.units.map(u => {
      const res = (st.results || {})[u.id]; const state = Core.S.states[u.id] || {}; const core = u.sections ? u.sections.length * 8 : 32;
      const coreDone = Object.entries(state.items || {}).filter(([k, v]) => v && v.done && /r\d+$/.test(k)).length;
      const open = Core.unitOpen(u.id); const ready = open || coreDone >= core;
      const pctCore = Math.round(Math.min(coreDone, core) / core * 100);
      const status = res ? el('span', { class: 'status done' }, `✓ Passed · ${res.pct.toFixed(1)}%`) : ready ? el('span', { class: 'status cur' }, 'Ready to take') : el('span', { class: 'tready' }, el('span', { class: 'pbar mini' }, el('i', { style: `width:${pctCore}%` })), el('small', {}, `${Math.min(coreDone, core)}/${core} Core questions`));
      return el('div', { class: 'lbrow trow' + (res ? ' passed' : '') }, el('span', {}, unitIcon(u.n)), el('span', {}, el('b', {}, `Unit Test ${u.n}`), el('br'), el('small', { class: 'muted' }, u.t)),
        el('span', { class: 'tmeta' }, el('b', {}, `${TestRules.UNIT_MINUTES} min`), el('small', { class: 'muted' }, '30 marks · pass above 70%')), el('span', {}, status),
        el('button', { class: 'btn small ' + (res ? '' : ready ? 'primary' : ''), type: 'button', 'data-unit': u.n, onclick: () => Core.switchUnit(u.n).then(() => go(res ? 'result' : 'test')) }, res ? 'Results' : ready ? 'Start' : 'Preview', el('span', { class: 'arr' }, ' →')));
    });
    const passedN = Object.keys(st.results || {}).filter(k => k.startsWith(`stage${Core.STAGE}-unit`)).length, need = Math.ceil(Core.unitCount() * Core.MOVE_ON / 100);
    m.append(el('section', { class: 'card tsum', id: 'testsSummary' },
      el('div', {}, el('span', { class: 'hl' }, 'How Unit Tests work'), el('h2', {}, 'Finish the Core questions, then sit the test')),
      el('ol', { class: 'tsteps' }, el('li', {}, el('b', {}, 'Get ready'), el('span', {}, 'Finish every lesson and Core question of the unit.')), el('li', {}, el('b', {}, 'Sit the test'), el('span', {}, `${TestRules.UNIT_MINUTES} minutes in the exam room. The clock keeps running.`)), el('li', {}, el('b', {}, 'Pass above 70%'), el('span', {}, `Pass ${need} of ${Core.unitCount()} tests for your certificate – you have ${passedN}.`)))));
    m.append(el('section', { class: 'card lbtable', id: 'testsTable' }, el('div', { class: 'lbrow h trow' }, el('span', {}, ''), el('span', {}, 'UNIT TEST'), el('span', {}, 'TIME'), el('span', {}, 'READINESS'), el('span', {}, '')), ...rows));
    if (F) m.append(finalCard(F, li));
    const P = await Core.loadCp(); if (P) { await Core.refreshCp().catch(() => { }); m.append(checkpointCard(P)); }
    if (Core.IS_MATHS) m.append(challengeCard());
  }
  // Maths Challenge sits inside the Maths course (Tests & exams, unit pages), not in the top menu
  function challengeCard() {
    return el('section', { class: 'card finalcard', id: 'challengeCard' }, el('span', { class: 'eyebrow' }, 'PROBLEM SOLVING · FOR ABLE MATHEMATICIANS'), el('h2', { style: 'margin:2px 0' }, '🏆 Maths Challenge'),
      el('p', {}, 'Competition-style papers – Primary, Junior and Intermediate Challenge, Kangaroo and Olympiad rounds. Sit one against the clock for an award, or practise question by question with full solutions.'),
      el('a', { class: 'btn gold', href: '#challenge', id: 'openChallenge' }, 'Open Maths Challenge', el('span', { class: 'arr' }, ' →')));
  }
  function finalCard(F, li) {
    const ok = (Core.S.tester || li.level >= F.level), done = (Core.S.finalAttempts || []).filter(a => a.status === 'final'), best = done.reduce((a, x) => Math.max(a, x.pct), 0);
    return el('section', { class: 'card finalcard', id: 'finalCard' }, el('span', { class: 'eyebrow' }, `END OF CAMBRIDGE ${Core.stageName(Core.STAGE).toUpperCase()}`), el('h2', { style: 'margin:2px 0' }, '🏁 End-of-year exams'),
      el('p', {}, `${Object.keys(F.papers).length} papers, each ${F.minutes} minutes and ${F.max} marks, covering all ${Core.unitCount()} units. Pass above ${Math.round(F.pass * 100)}%. Opens at level ${F.level}.`),
      el('div', { class: 'lvgate' }, el('b', {}, ok ? `✓ You are level ${li.level} – the exams are open.` : `You are level ${li.level}. Reach level ${F.level} (${TestRules.xpForLevel(F.level) - li.xp} more XP).`), el('div', { class: 'pbar' }, el('i', { style: `width:${Math.min(100, li.xp / TestRules.xpForLevel(F.level) * 100)}%` }))),
      done.length ? el('p', { class: 'muted' }, `${done.length} paper(s) taken · best ${best.toFixed(1)}%${Core.finalPassed() ? ' · passed ✓' : ''}`) : null,
      el('a', { class: 'btn ' + (ok ? 'gold shine' : ''), href: '#final' }, ok ? 'Choose a paper' : 'See the papers', el('span', { class: 'arr' }, ' →')));
  }

  /* ---------- Checkpoint exam room: Camday papers in the format of Cambridge Lower Secondary Checkpoint ---------- */
  const CP_STRAND = { BIO: 'Biology', CHE: 'Chemistry', PHY: 'Physics', ESS: 'Earth and space', TWS: 'Thinking and working scientifically' };
  const cpTitle = (P, k) => { const mt = (P.meta || {})[k] || {}; return { subj: Core.IS_MATHS ? 'Mathematics' : 'Science', code: mt.format || (Core.IS_MATHS ? '0862' : '0893'), paper: mt.paper || 1, set: mt.set || k[0] }; };
  function checkpointCard(P) {
    const done = (Core.S.cpAttempts || []).filter(a => a.status === 'final').length;
    return el('section', { class: 'card finalcard cpcard', id: 'cpCard' }, el('span', { class: 'eyebrow' }, 'CAMBRIDGE LOWER SECONDARY CHECKPOINT · PRACTICE'), el('h2', { style: 'margin:2px 0' }, '🏛 Checkpoint exam room'),
      el('p', {}, `${Core.IS_MATHS ? 'Mathematics papers in the format of 0862/01 and 0862/02' : 'Science papers in the format of 0893/01 and 0893/02'} – ${P.minutes} minutes and ${P.max} marks each, under full exam conditions. ${Object.keys(P.papers).length} papers so far${done ? ` · you have taken ${done}` : ''}.`),
      el('a', { class: 'btn gold', href: '#checkpoint' }, 'Enter the Checkpoint exam room', el('span', { class: 'arr' }, ' →')));
  }
  async function viewCheckpoint() {
    const m = $main(); const P = await Core.loadCp(); await Core.refreshCp().catch(() => { });
    pageHero('CAMBRIDGE LOWER SECONDARY CHECKPOINT', 'Checkpoint exam room', 'Practise the real exam: the same paper format, timing and marks as the Cambridge Lower Secondary Checkpoint tests, under exam conditions – full screen, a countdown clock and no leaving the room.');
    if (!P) { m.append(el('section', { class: 'card' }, el('p', {}, 'Checkpoint papers are in the Stage 7 exam room (Stage 7 content) and the Stage 9 exam room (full Stages 7–9 papers). Switch stage in Your courses to open them.'))); return; }
    if (isGuest()) { m.append(guestWall('Sign up free to use the Checkpoint exam room')); return; }
    const isM = Core.IS_MATHS, subj = isM ? 'Mathematics' : 'Science';
    m.append(el('div', { class: 'banner info' }, el('b', {}, 'About these papers: '), P.unit.note + (isM ? ' They cover Stages 7–9 Mathematics, with most marks on Stage 9, like the real Checkpoint test.' : Core.STAGE === 9 ? ' These papers cover Cambridge Stages 7, 8 and 9, like the real Checkpoint test taken at the end of Stage 9.' : ` They cover Cambridge ${Core.stageName(Core.STAGE)} content. Full papers covering Stages 7–9 are in the Stage 9 exam room.`)));
    const sets = {}; Object.keys(P.papers).forEach(k => { const t = cpTitle(P, k); (sets[t.set] = sets[t.set] || []).push(k); });
    const head = (m_) => el('div', { class: 'cphead' }, el('span', { class: 'cpsubjtag ' + (m_ ? 'math' : 'sci') }, m_ ? 'MATHEMATICS' : 'SCIENCE'), el('div', {}, el('h2', { style: 'margin:0' }, m_ ? 'Mathematics · syllabus 0862' : 'Science · syllabus 0893'), el('p', { class: 'muted', style: 'margin:0' }, m_ ? 'Paper 1 (0862/01 format, no calculator) and Paper 2 (0862/02 format, calculator allowed) · 60 minutes · 50 marks each' : `Paper 1 (0893/01 format) and Paper 2 (0893/02 format) · ${isM ? 45 : P.minutes} minutes · 50 marks each`)));
    const mine = el('section', { class: 'card cpsubj' }, head(isM));
    Object.entries(sets).forEach(([set, ks]) => {
      mine.append(el('div', { class: 'cpset' }, el('b', { class: 'lex' }, 'Set ' + set), ...ks.map(k => { const t = cpTitle(P, k); const a = (Core.S.cpAttempts || []).find(x => x.form === k); const d = fdLoad('cp' + k); const mt = (P.meta || {})[k] || {};
        return el('div', { class: 'cprow' }, el('span', { class: 'cpcode' }, t.code), el('span', {}, el('b', {}, `${subj} · Paper ${t.paper}`), el('br'), el('small', { class: 'muted' }, `Camday paper · Set ${set}${isM ? (mt.calculator ? ' · calculator allowed' : ' · no calculator') : ''}${mt.level === 'harder' ? (isM ? ' · harder' : ' · harder, investigation-based') : ''} · ${P.minutes} min · ${P.max} marks`)),
          a ? el('span', { class: 'status ' + (a.status === 'pending' ? 'cur' : 'done') }, a.status === 'pending' ? '⏳ Awaiting marking' : `${+a.score.toFixed(1)}/${P.max} · ${a.pct.toFixed(0)}%`) : d && d.deadline ? el('span', { class: 'status cur' }, 'In progress') : el('span', { class: 'status todo' }, 'Not taken'),
          a ? el('a', { class: 'btn small', href: '#cpr-' + k }, 'Results') : el('a', { class: 'btn small primary', href: '#cpx-' + k, id: 'cpOpen-' + k }, d && d.deadline ? 'Continue' : 'Enter', el('span', { class: 'arr' }, ' →'))); })));
    });
    const other = el('section', { class: 'card cpsubj soon' }, head(!isM),
      el('div', { class: 'cpset' }, !isM && Core.stageLocked(19) ? el('span', { class: 'status todo' }, '🔒 Mathematics Stage 9 – coming soon') : el('a', { class: 'btn small', href: isM ? '#stage-9' : '#stage-19' }, isM ? 'Open the Science Stage 9 course for these papers →' : 'Open the Mathematics Stage 9 course for these papers →')));
    m.append(mine, other);
  }
  async function viewCpExam(k) {
    const m = $main(); const P = await Core.loadCp(); await Core.refreshCp().catch(() => { });
    if (!P || !P.papers[k]) return go('checkpoint');
    if (isGuest()) { m.append(guestWall('Sign up free to use the Checkpoint exam room')); return; }
    if ((Core.S.cpAttempts || []).some(a => a.form === k)) return go('cpr-' + k);
    const t = cpTitle(P, k); const dk = 'cp' + k;
    const draft = fdLoad(dk) || { answers: {}, ts: Date.now() }; const save = () => fdSave(dk, draft); const qs = P.papers[k];
    const title = `${t.subj} · Paper ${t.paper} (${t.code} format) · Set ${t.set}`;
    if (!UI.testOn || UI.examKey !== 'C' + k) {
      UI.testOn = false;
      m.append(examIntro({ title, n: qs.length, max: P.max, minutes: P.minutes, passTxt: 'Score', resume: !!draft.deadline,
        extra: [`An Camday practice paper in the format of the Cambridge Lower Secondary Checkpoint ${t.subj} test.${Core.IS_MATHS ? (((P.meta || {})[k] || {}).calculator ? ' A calculator is allowed.' : ' Do not use a calculator.') : ''} One attempt per paper.`, 'Every answer, chosen or typed, is marked automatically; your results show your marks for each part of science.'],
        start: async ev => { ev.currentTarget.disabled = true; try { const c = await Core.startClock(`stage${Core.STAGE}-cp`, k); draft.deadline = c.deadline; save(); UI.testOn = true; UI.examKey = 'C' + k; UI.testIdx = 0; render(); } catch (x) { ev.currentTarget.disabled = false; modal('Could not open the paper', errText(x), [{ t: 'OK', cls: 'primary' }]); } } }));
      return;
    }
    examRoom({ title, badge: 'CHECKPOINT · ' + Core.subjectOf(Core.STAGE).toUpperCase() + ' ' + t.code, qs, max: P.max, draft, save, seed: st.id + 'C' + k, deadline: draft.deadline,
      onSubmit: async (answers, key, meta) => { await Core.submitCp(k, answers, key, meta); try { localStorage.removeItem(fdKey(dk)); } catch (e) { } UI.examKey = null; go('cpr-' + k); } });
  }
  async function viewCpResult(k) {
    const m = $main(); const P = await Core.loadCp(); await Core.refreshCp().catch(() => { });
    const a = (Core.S.cpAttempts || []).find(x => x.form === k); if (!a) return go('cpx-' + k); const t = cpTitle(P, k);
    m.append(el('nav', { class: 'crumb2' }, el('a', { href: '#tests' }, 'Tests & exams'), ' › ', el('a', { href: '#checkpoint' }, 'Checkpoint exam room'), ` › ${t.subj} ${t.code} · Set ${t.set}`));
    if (a.status === 'pending') { m.append(el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, 'A written answer is waiting for an Camday marker. You will get a notification.'), leavesNote(a))); return; }
    m.append(el('section', { class: 'card' }, el('div', { class: 'resultbig' }, ring(a.pct, a.pct >= 50), el('div', {}, el('span', { class: 'eyebrow' }, `SCIENCE · PAPER ${t.paper} (${t.code} FORMAT) · SET ${t.set}`), el('h2', { style: 'margin:0' }, `${+a.score.toFixed(2)}/${P.max} (${a.pct.toFixed(1)}%)`),
      el('p', { style: 'margin:4px 0' }, a.duration != null ? `Time taken: ${Math.floor(a.duration / 60)} min ${a.duration % 60} s of ${P.minutes} min${a.overtime ? ' (after the time limit)' : ''}` : ''), leavesNote(a)))));
    const byS = Object.entries(a.byObj || {});
    m.append(el('section', { class: 'card' }, el('h2', {}, 'Marks by area of science'), el('div', { class: 'weak' }, ...byS.map(([o, b]) => { const pct = b.max ? b.got / b.max * 100 : 0;
      return el('div', { class: 'wk' }, el('b', {}, CP_STRAND[o] || o), el('div', { class: 'pbar' + (pct < 50 ? ' red' : '') }, el('i', { style: `width:${Math.max(2, pct)}%` })), el('small', { class: 'muted' }, `${+b.got.toFixed(2)}/${b.max} marks`)); })),
      el('a', { class: 'btn small primary', href: '#checkpoint' }, 'Back to the Checkpoint exam room')));
  }

  /* ---------- word games (Stages 1–6, every subject): one player level, saved with the learner ---------- */
  function gameCtx() {
    const signed0 = () => !!(st && !isGuest()), lkey = () => 'atomic.games.v1' + (st ? '.' + st.id : '');
    const dflt = () => { const s = st ? Core.STAGE : 3; return { xp: 0, stage: s >= 1 && s <= 5 ? s : (s >= 11 && s <= 15) || (s >= 22 && s <= 25) ? Core.stageNo(s) : s >= 6 ? 5 : 3, subj: 'all', best: {}, words: {}, played: 0 }; };
    return { get signedIn() { return signed0(); }, get name() { return st ? st.alias || st.name : ''; }, go,
      load: () => { const signed = signed0(), lk = lkey(); let s = null; if (signed) s = (Core.S.states || {}).games; if (!s) { try { s = JSON.parse(localStorage.getItem(lk) || 'null'); } catch (e) { } } return Object.assign(dflt(), s || {}); },
      save: S => { const signed = signed0(), lk = lkey(); try { localStorage.setItem(lk, JSON.stringify(S)); } catch (e) { } if (signed) { Core.S.states = Core.S.states || {}; Core.S.states.games = S; Backend.saveProgress(st.id, 'games', S).catch(() => { }); } } };
  }
  // a lesson's key words as game words (Stages 1–6: the lesson word bank)
  function secGameWords(s) {
    const stg = Core.stageNo(Core.STAGE);
    if (!s || !Array.isArray(s.vocab) || s.vocab.length < 3 || stg > 5) return [];   // word games: Stages 1–5 only
    const subj = Core.IS_ESL ? 'english' : Core.IS_MATHS ? 'maths' : 'science';
    return s.vocab.filter(v => v.w && v.def).map(v => ({ id: `${subj[0]}${stg}-${String(v.w).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')}`, w: v.w, def: v.def, emoji: v.emoji || '📘', audio: v.audio || '', subj, stage: stg, topic: s.title }));
  }
  async function viewSecGames(sid) {
    const s = Core.sec(sid), m = $main(); if (!s) return go('home');
    const words = secGameWords(s); if (!words.length) return go('ex-' + R(sid));
    const lock = Core.secLock(st, s);
    subbar('blue', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}: ${C.unit.title}`), el('span', { class: 'ttl' }, `${s.id} ${s.title} · Word games`));
    if (lock) { m.append(bar(`Section ${s.id} · Word games`), lockScreen(`Word games for section ${s.id} are locked`, lock.reason, [lock])); return; }
    st.last = { route: 'gm-' + R(sid) }; Core.persist();
    const host = el('div', { style: 'padding-bottom:30px' });
    m.append(bar(`Section ${s.id} · Word games`), tocBtn(), host);
    st.games = st.games || {}; const rec = st.games[s.id] || { n: 0, best: 0, by: {} };
    const ctx = Object.assign(gameCtx(), { pool: words, title: `${s.id} ${s.title} · word games`, back: '#gm-' + R(sid), best: rec.by,
      onFinish: r => { rec.n++; rec.best = Math.max(rec.best, r.score); rec.by[r.id] = Math.max(rec.by[r.id] || 0, r.score); st.games[s.id] = rec; Core.persist(); refreshToc(); } });
    await Games.picker(host, ctx);
  }
  async function viewGames() {
    const m = $main();
    pageHero('LEARN WORDS BY PLAYING · STAGES 1–5', 'Word games', 'Five games for Science, Maths and English words. Every game you finish earns XP – there is no top level, and every level is a little faster and trickier.');
    const host = el('div'); m.append(host); await Games.hub(host, gameCtx());
  }
  async function viewGame(id) {
    const m = $main(); m.append(el('nav', { class: 'crumb2' }, el('a', { href: '#games' }, 'Word games'), ' › ' + ((Games.GAMES.find(g => g.id === id) || {}).name || '')));
    const host = el('div', { style: 'padding:8px 0 30px' }); m.append(host); await Games.play(host, gameCtx(), id);
  }

  /* ---------- Maths Challenge: problem-solving competition papers (Camday originals, keys on the server) ---------- */
  const CH = [
    { id: 'primary', icon: '🦉', color: '#1F9D5C' }, { id: 'junior', icon: '🦊', color: '#0149AF' }, { id: 'inter', icon: '🐺', color: '#7A4BD1' },
    { id: 'kangaroo', icon: '🦘', color: '#D9722A' }, { id: 'olympiad', icon: '🏆', color: '#B9842B' }];
  const CH_AWARDS = { olympiad: [[60, 'Distinction', '🏅', 'gold'], [40, 'Merit', '🎖', 'silver']], _: [[65, 'Gold', '🥇', 'gold'], [45, 'Silver', '🥈', 'silver'], [30, 'Bronze', '🥉', 'bronze']] };
  const chAward = (id, pct) => (CH_AWARDS[id] || CH_AWARDS._).find(b => pct >= b[0]) || null;
  const CHP = {};
  async function chPack(id) { if (!CHP[id]) { const r = await fetch(`content/ch-${id}.json`); if (!r.ok) throw new Error('missing'); CHP[id] = await Core.withOv('ch-' + id, await r.json()); } return CHP[id]; }
  const chSigned = () => !!(st && !isGuest());
  async function chAttempts(id) { if (!chSigned()) return []; try { return await Backend.attempts(st.id, 'ch-' + id); } catch (e) { return []; } }
  async function chState(id) { if (!chSigned()) return { done: [], solutions: {} }; try { return await Backend.challenge({ action: 'state', learnerId: st.id, unit: 'ch-' + id }); } catch (e) { return { done: [], solutions: {} }; } }
  const chPaperName = (P, k) => `${P.unit.title} · Paper ${Number(k)}`;
  function chAwardChip(id, a) { if (!a || a.status !== 'final') return null; const b = chAward(id, a.pct); return b ? el('span', { class: 'chaward ' + b[3] }, b[2] + ' ' + b[1]) : el('span', { class: 'chaward none' }, 'Certificate of participation'); }
  function chRules(P, id) {
    const olymp = id === 'olympiad', n = P.papers['01'].length;
    return [`${n} questions · ${P.minutes} minutes · ${P.max} marks. ` + (olymp ? 'Questions 1–4 are worth 5 marks and 5–12 are worth 10 marks.' : 'Questions 1–15 are worth 5 marks and 16–25 are worth 6 marks.') + ' A wrong answer simply scores 0.',
      P.unit.format === 'num' ? 'There are no options: type a whole number from 0 to 999 for each answer.' : 'Choose one answer, A to E, for each question.',
      'Calculators are not allowed. Have pencil and rough paper ready – these problems need thinking, not just calculating.',
      'Awards: ' + (CH_AWARDS[id] || CH_AWARDS._).map(b => `${b[2]} ${b[1]} from ${b[0]}%`).join(' · ') + '.'];
  }
  async function viewChallenge() {
    const m = $main();
    pageHero('PROBLEM SOLVING · FOR ABLE MATHEMATICIANS', 'Maths Challenge', 'Competition-style papers that stretch strong mathematicians: clever problems, not routine exercises. Sit a paper against the clock and win an award, or practise it question by question with full worked solutions.');
    const grid = el('div', { class: 'chgrid', id: 'chGrid' });
    const packs = await Promise.all(CH.map(c => chPack(c.id).catch(() => null)));
    const tries = await Promise.all(CH.map(c => chAttempts(c.id)));
    CH.forEach((c, i) => { const P = packs[i]; if (!P) return; const at = tries[i].filter(a => a.status === 'final'); const best = at.reduce((b, a) => (!b || a.pct > b.pct ? a : b), null);
      grid.append(el('a', { class: 'chfolder', href: '#chl-' + c.id, id: 'chFolder-' + c.id, style: `--c:${c.color}` },
        el('span', { class: 'chico', 'aria-hidden': 'true' }, c.icon),
        el('span', { class: 'chft' }, el('b', {}, P.unit.title), el('small', {}, `${Object.keys(P.papers).length} papers · ${P.unit.ages}`)),
        el('span', { class: 'chfa' }, P.unit.about),
        el('span', { class: 'chfp' }, at.length ? [`${at.length} sat`, best ? ' · best ' + best.pct.toFixed(0) + '%' : ''].join('') : 'Not started', best ? chAwardChip(c.id, best) : null))); });
    m.append(grid);
    m.append(el('section', { class: 'card chhow' }, el('h2', {}, 'How it works'),
      el('div', { class: 'chhow3' },
        el('div', {}, el('b', {}, '⏱ Sit the paper'), el('p', {}, 'Full screen, against the clock, like the real competition. Your score and award appear straight away, with a worked solution to every question.')),
        el('div', {}, el('b', {}, '🧩 Practise question by question'), el('p', {}, 'No clock. Answer one question, check it at once and read the full solution. A paper you practise cannot then be sat as a timed paper – so try the timed paper first if you want an award.')),
        el('div', {}, el('b', {}, '📈 Which level?'), el('p', {}, 'Primary for Stages 5–6, Junior for Stages 7–8, Intermediate for Stage 9 and IGCSE. The Kangaroo and Olympiad rounds are the next step for anyone who scores Gold.'))),
      el('p', { class: 'muted', style: 'margin:16px 0 0;font-size:14px' }, 'Every problem is an original written by the Camday teaching team in the style of national maths challenges. These are not UKMT papers.')));
    if (!chSigned()) m.append(el('div', { class: 'banner info' }, 'You can look at every paper. ', el('a', { href: '#signup' }, 'Sign up free'), ' to sit papers, practise and keep your awards.'));
  }
  async function viewChList(id) {
    const m = $main(); const c = CH.find(x => x.id === id); if (!c) return go('challenge');
    const P = await chPack(id); const [tries, S] = await Promise.all([chAttempts(id), chState(id)]);
    m.append(el('nav', { class: 'crumb2' }, el('a', { href: '#challenge' }, 'Maths Challenge'), ` › ${P.unit.title}`));
    m.append(el('section', { class: 'card chhead', style: `--c:${c.color}` }, el('span', { class: 'chico big', 'aria-hidden': 'true' }, c.icon),
      el('div', {}, el('h1', { style: 'margin:0' }, P.unit.title), el('p', { class: 'muted', style: 'margin:2px 0 8px' }, `${P.unit.ages} · ${P.unit.about}`), el('ul', { class: 'chrules' }, ...chRules(P, id).map(t => el('li', {}, t))))));
    const list = el('div', { class: 'chpapers', id: 'chPapers' });
    Object.keys(P.papers).sort().forEach(k => {
      const a = tries.find(x => x.form === k); const pr = S.done.filter(x => x.form === k); const n = P.papers[k].length; const d = chSigned() ? fdLoad('ch' + id + k) : null;
      const status = a ? (a.status === 'final' ? el('span', { class: 'status done' }, `${+a.score.toFixed(0)}/${P.max} · ${a.pct.toFixed(0)}%`) : el('span', { class: 'status cur' }, '⏳ Marking'))
        : pr.length ? el('span', { class: 'status cur' }, `Practising · ${pr.filter(x => x.ok).length}/${pr.length} right · ${n - pr.length} left`) : d && d.deadline ? el('span', { class: 'status cur' }, 'Timed paper running') : el('span', { class: 'status todo' }, 'Not tried');
      const btns = !chSigned() ? [el('a', { class: 'btn small primary', href: '#signup' }, 'Sign up to start')]
        : a ? [el('a', { class: 'btn small primary', href: `#chr-${id}-${k}`, id: `chRes-${id}-${k}` }, 'Results & solutions'), el('a', { class: 'btn small', href: `#chp-${id}-${k}` }, 'Practise again')]
        : pr.length ? [el('a', { class: 'btn small primary', href: `#chp-${id}-${k}`, id: `chPrac-${id}-${k}` }, pr.length < n ? 'Carry on practising' : 'Review')]
        : [el('a', { class: 'btn small gold', href: `#chx-${id}-${k}`, id: `chSit-${id}-${k}` }, d && d.deadline ? 'Back to the paper' : '⏱ Sit the paper'), d && d.deadline ? null : el('a', { class: 'btn small', href: `#chp-${id}-${k}`, id: `chPrac-${id}-${k}` }, '🧩 Practise')];
      list.append(el('div', { class: 'chpaper' }, el('span', { class: 'chdoc', 'aria-hidden': 'true' }, '📄'),
        el('span', { class: 'chpt' }, el('b', {}, chPaperName(P, k)), el('small', { class: 'muted' }, `${n} questions · ${P.minutes} min · ${P.max} marks`)),
        el('span', { class: 'chps' }, status, chAwardChip(id, a)), el('span', { class: 'btnrow', style: 'margin:0' }, ...btns)));
    });
    m.append(list);
  }
  async function viewChExam(id, k) {
    const m = $main(); const P = await chPack(id); if (!P.papers[k]) return go('chl-' + id);
    if (isGuest()) { m.append(guestWall('Sign up free to sit Maths Challenge papers')); return; }
    const tries = await chAttempts(id); if (tries.some(a => a.form === k)) return go(`chr-${id}-${k}`);
    const unit = 'ch-' + id, dk = 'ch' + id + k, qs = P.papers[k];
    const draft = fdLoad(dk) || { answers: {}, ts: Date.now() }; const save = () => fdSave(dk, draft);
    if (!draft.deadline) { const S = await chState(id); if (S.done.some(x => x.form === k)) { m.append(el('section', { class: 'card' }, el('h2', {}, 'You have practised this paper'), el('p', {}, 'You have already seen solutions to some of its questions, so it can no longer be sat as a timed paper. Choose another paper for an award.'), el('div', { class: 'btnrow' }, el('a', { class: 'btn primary small', href: `#chp-${id}-${k}` }, 'Carry on practising'), el('a', { class: 'btn small', href: '#chl-' + id }, 'All papers')))); return; } }
    const title = chPaperName(P, k);
    if (!UI.testOn || UI.examKey !== 'H' + id + k) {
      UI.testOn = false;
      m.append(examIntro({ title, n: qs.length, max: P.max, minutes: P.minutes, passTxt: (CH_AWARDS[id] || CH_AWARDS._).slice(-1)[0][0] + '%', resume: !!draft.deadline,
        extra: chRules(P, id).concat('One timed attempt per paper. Afterwards you can review every question with its worked solution.'),
        start: async ev => { ev.currentTarget.disabled = true; try { const c = await Core.startClock(unit, k); draft.deadline = c.deadline; save(); UI.testOn = true; UI.examKey = 'H' + id + k; UI.testIdx = 0; render(); } catch (x) { ev.currentTarget.disabled = false; modal('Could not open the paper', errText(x), [{ t: 'OK', cls: 'primary' }]); } } }));
      const pt = m.querySelector('.stats3 > div:last-child small'); if (pt) pt.textContent = 'for an award';
      return;
    }
    examRoom({ title, badge: 'MATHS CHALLENGE · ' + P.unit.title.toUpperCase(), qs, max: P.max, draft, save, seed: st.id + 'H' + id + k, deadline: draft.deadline,
      onSubmit: async (answers, key, meta) => { const r = await Backend.submitTest({ learnerId: st.id, unit, form: k, answers, clientKey: key, meta }); try { localStorage.removeItem(fdKey(dk)); } catch (e) { }
        UI.chSol = Object.assign(UI.chSol || {}, r.solutions || {}); UI.examKey = null; const b = r.attempt && r.attempt.status === 'final' && chAward(id, r.attempt.pct); if (b && b[3] === 'gold') confetti(); go(`chr-${id}-${k}`); } });
  }
  function chYour(q, v) {
    if (v == null || v === '') return '—';
    if (q.type === 'mcq') return q.options[v] ? `${String.fromCharCode(65 + v)}  ${q.options[v].t}` : '—';
    if (typeof v === 'object') return String(v.v || '').trim() || '—';
    return String(v);
  }
  function chReview(q, i, your, sol, ok, pts) {
    const card = el('div', { class: 'chrev ' + (ok ? 'ok' : your == null || your === '' ? 'blank' : 'no'), id: 'chRev-' + q.id });
    card.append(el('div', { class: 'chrevh' }, el('b', {}, `Question ${i + 1}`), el('span', { class: 'chmark' }, ok ? `✓ ${pts != null ? pts + ' marks' : 'Right'}` : your == null || your === '' ? 'Not answered' : '✗ Not right')),
      el('p', { class: 'qp' }, q.prompt));
    const body = el('div'); card.append(body);
    const qq = q.type === 'mcq' && sol ? { ...q, options: q.options.map(o => ({ ...o, ok: o.t === sol.answer })) } : q;
    const api = QE.renderBody(qq, body, { seed: 'rev', resp: your }); api.lock(); if (api.markOpts && sol) api.markOpts();
    if (sol) card.append(el('div', { class: 'chsol' }, el('p', { style: 'margin:0 0 4px' }, el('b', {}, 'Answer: '), q.type === 'mcq' ? `${String.fromCharCode(65 + q.options.findIndex(o => o.t === sol.answer))}  ${sol.answer}` : sol.answer, q.type !== 'mcq' && your != null ? el('span', { class: 'muted' }, ` · you wrote ${chYour(q, your)}`) : null),
      el('p', { style: 'margin:0' }, el('b', {}, 'Solution: '), sol.reason || '—')));
    return card;
  }
  async function viewChResult(id, k) {
    const m = $main(); const P = await chPack(id); const tries = await chAttempts(id); const a = tries.find(x => x.form === k); if (!a) return go(`chx-${id}-${k}`);
    m.append(el('nav', { class: 'crumb2' }, el('a', { href: '#challenge' }, 'Maths Challenge'), ' › ', el('a', { href: '#chl-' + id }, P.unit.title), ` › Paper ${Number(k)}`));
    if (a.status !== 'final') { m.append(el('section', { class: 'card' }, el('h2', {}, '⏳ Being marked'), el('p', {}, 'Your paper is being marked. Check back in a moment.'))); return; }
    const b = chAward(id, a.pct); const right = P.papers[k].filter(q => (a.per[q.id] || {}).pts > 0).length;
    m.append(el('section', { class: 'card chresult' + (b ? ' ' + b[3] : '') }, el('div', { class: 'resultbig' }, ring(a.pct, !!b),
      el('div', {}, el('span', { class: 'eyebrow' }, chPaperName(P, k).toUpperCase()), el('h2', { style: 'margin:0' }, `${+a.score.toFixed(0)}/${P.max} marks · ${right} of ${P.papers[k].length} right`),
        el('p', { class: 'chbig' }, b ? `${b[2]} ${b[1]} award` : 'Certificate of participation – keep going!'),
        el('p', { style: 'margin:4px 0' }, a.duration != null ? `Time taken: ${Math.floor(a.duration / 60)} min ${a.duration % 60} s of ${P.minutes} min${a.overtime ? ' (after the time limit)' : ''}` : ''), leavesNote(a),
        el('div', { class: 'btnrow' }, el('a', { class: 'btn primary small', href: '#chl-' + id }, 'All papers'), el('a', { class: 'btn small', href: '#challenge' }, 'Maths Challenge'))))));
    const byO = Object.entries(a.byObj || {});
    m.append(el('section', { class: 'card' }, el('h2', {}, 'Marks by area'), el('div', { class: 'weak' }, ...byO.map(([o, x]) => { const pct = x.max ? x.got / x.max * 100 : 0;
      return el('div', { class: 'wk' }, el('b', {}, (P.objectives[o] || {}).t || o), el('div', { class: 'pbar' + (pct < 50 ? ' red' : '') }, el('i', { style: `width:${Math.max(2, pct)}%` })), el('small', { class: 'muted' }, `${+x.got.toFixed(0)}/${x.max} marks`)); }))));
    let sols = UI.chSol || {}; if (!P.papers[k].every(q => sols[q.id])) { try { sols = Object.assign({}, sols, (await Backend.challenge({ action: 'solutions', learnerId: st.id, unit: 'ch-' + id, form: k })).solutions); UI.chSol = sols; } catch (e) { } }
    const sec = el('section', { class: 'card' }, el('h2', {}, 'Every question, with its solution'));
    P.papers[k].forEach((q, i) => { const p = a.per[q.id] || {}; sec.append(chReview(q, i, (a.answers || {})[q.id], sols[q.id], p.pts > 0, p.pts)); });
    m.append(sec);
  }
  async function viewChPractice(id, k) {
    const m = $main(); const P = await chPack(id); if (!P.papers[k]) return go('chl-' + id);
    if (isGuest()) { m.append(guestWall('Sign up free to practise Maths Challenge papers')); return; }
    const qs = P.papers[k]; const [S, tries] = await Promise.all([chState(id), chAttempts(id)]);
    const sat = tries.some(a => a.form === k); const done = Object.fromEntries(S.done.filter(x => x.form === k).map(x => [x.qid, x]));
    const sols = S.solutions || {};
    if (!sat && !Object.keys(done).length && UI.chOk !== id + k) {
      m.append(el('nav', { class: 'crumb2' }, el('a', { href: '#challenge' }, 'Maths Challenge'), ' › ', el('a', { href: '#chl-' + id }, P.unit.title), ` › Paper ${Number(k)}`));
      m.append(el('section', { class: 'card', style: 'max-width:720px;margin:0 auto', id: 'chPracGate' }, el('span', { class: 'eyebrow' }, 'PRACTISE QUESTION BY QUESTION'), el('h2', {}, chPaperName(P, k)),
        el('p', {}, 'You will see whether each answer is right, and its full worked solution, straight away. Because you will have seen the solutions, ', el('b', {}, 'this paper can then no longer be sat as a timed paper for an award.')),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn primary', type: 'button', id: 'chPracGo', onclick: () => { UI.chOk = id + k; UI.chIdx = 0; render(); } }, 'Start practising', el('span', { class: 'arr' }, ' →')), el('a', { class: 'btn gold', href: `#chx-${id}-${k}` }, '⏱ Sit it timed instead'))));
      return;
    }
    const i = Math.min(UI.chIdx || 0, qs.length - 1), q = qs[i]; const got = done[q.id];
    const nOk = Object.values(done).filter(x => x.ok).length;
    m.append(el('nav', { class: 'crumb2' }, el('a', { href: '#challenge' }, 'Maths Challenge'), ' › ', el('a', { href: '#chl-' + id }, P.unit.title), ` › Paper ${Number(k)} · practice`));
    const card = el('section', { class: 'card qcard', style: 'flex:999 1 600px;min-width:0', id: 'chPracCard' },
      el('div', { class: 'btnrow between', style: 'margin:0' }, el('span', { class: 'lex', style: 'font-weight:700;color:#556377' }, `Question ${i + 1} of ${qs.length} · ${q.pts} marks`), el('span', { class: 'tag d-' + q.diff }, { M: 'Warm-up', H: 'Harder', VH: 'Hardest' }[q.diff] || '')),
      el('h2', { class: 'qp', style: 'font-size:22px' }, q.prompt));
    const fbBox = el('div', { 'aria-live': 'polite' }); let resp = got ? got.answer : null;
    const show = (ok, sol, your) => {
      fbBox.innerHTML = '';
      fbBox.append(el('div', { class: 'chfb ' + (ok ? 'ok' : 'no'), id: 'chFb' }, el('b', {}, ok ? '✓ Right!' : '✗ Not quite.'),
        el('p', { style: 'margin:6px 0 0' }, el('b', {}, 'Answer: '), q.type === 'mcq' ? `${String.fromCharCode(65 + q.options.findIndex(o => o.t === sol.answer))}  ${sol.answer}` : sol.answer, !ok && your != null ? el('span', { class: 'muted' }, ` · you answered ${chYour(q, your)}`) : null),
        el('p', { style: 'margin:6px 0 0' }, el('b', {}, 'Solution: '), sol.reason)));
    };
    const qq = got && sols[q.id] && q.type === 'mcq' ? { ...q, options: q.options.map(o => ({ ...o, ok: o.t === sols[q.id].answer })) } : q;
    const api = QE.renderBody(qq, card, { seed: st.id + 'P' + id + k, resp, onChange: r => { resp = r; } });
    if (got && sols[q.id]) { api.lock(); if (api.markOpts) api.markOpts(); show(got.ok, sols[q.id], got.answer); }
    const check = el('button', { class: 'btn primary', type: 'button', id: 'chCheck', hidden: !!got, onclick: async ev => {
      if (resp == null || resp === '' || (typeof resp === 'object' && resp.v != null && !String(resp.v).trim())) { toast('Answer the question first.'); return; }
      ev.currentTarget.disabled = true;
      try { const r = await Backend.challenge({ action: 'check', learnerId: st.id, unit: 'ch-' + id, form: k, qid: q.id, answer: resp });
        done[q.id] = { qid: q.id, form: k, ok: r.ok, answer: r.first != null ? r.first : resp }; sols[q.id] = { answer: r.answer, reason: r.reason };
        api.lock(); if (q.type === 'mcq' && api.markOpts) { q.options.forEach(o => { o.ok = o.t === r.answer; }); api.markOpts(); q.options.forEach(o => { delete o.ok; }); }
        show(r.ok, sols[q.id], done[q.id].answer); check.hidden = true; drawNav(); if (r.ok) toast('✓ Right!');
      } catch (x) { ev.currentTarget.disabled = false; modal('Could not check', errText(x), [{ t: 'OK', cls: 'primary' }]); } } }, 'Check answer');
    card.append(fbBox, el('div', { class: 'btnrow between', style: 'padding-top:16px;border-top:1px solid #E6EEF8' },
      el('button', { class: 'btn small', type: 'button', disabled: i === 0, onclick: () => { UI.chIdx = i - 1; render(); } }, '← Previous'), check,
      i < qs.length - 1 ? el('button', { class: 'btn small', type: 'button', id: 'chNext', onclick: () => { UI.chIdx = i + 1; render(); } }, 'Next', el('span', { class: 'arr' }, ' →')) : el('a', { class: 'btn small navy', href: '#chl-' + id }, 'Finish')));
    const nav = el('div', { class: 'navgrid' });
    const drawNav = () => { nav.innerHTML = ''; qs.forEach((x, j) => nav.append(el('button', { type: 'button', class: (done[x.id] ? (done[x.id].ok ? 'okq' : 'noq') : '') + (j === i ? ' on' : ''), 'aria-label': `Question ${j + 1}${done[x.id] ? (done[x.id].ok ? ', right' : ', not right') : ''}`, onclick: () => { UI.chIdx = j; render(); } }, String(j + 1)))); };
    drawNav();
    m.append(el('div', { style: 'display:flex;flex-wrap:wrap;gap:26px;align-items:flex-start' }, card,
      el('aside', { class: 'card', style: 'flex:1 1 260px;min-width:0;display:flex;flex-direction:column;gap:14px' }, el('b', { class: 'lex' }, 'Questions'), nav,
        el('div', { class: 'legend' }, el('span', {}, el('i', { style: 'background:#1E8E4E' }), 'Right'), el('span', {}, el('i', { style: 'background:#C93A3A' }), 'Not right'), el('span', {}, el('i', { style: 'border:2px solid #D3E0F4' }), 'Not tried')),
        el('p', { class: 'muted', style: 'margin:0', id: 'chTally' }, `${Object.keys(done).length} of ${qs.length} tried · ${nOk} right`),
        sat ? el('p', { class: 'muted', style: 'margin:0;font-size:13px' }, 'You have sat this paper; practice here does not change your award.') : el('p', { class: 'muted', style: 'margin:0;font-size:13px' }, 'Your first answer to each question is the one that counts. Rough paper helps!'))));
  }

  /* ---------- end-of-year exams ---------- */
  const fdKey = f => `atomic.fdraft.${st.id}.${f}`;
  const fdLoad = f => { try { return JSON.parse(localStorage.getItem(fdKey(f))) || null; } catch (e) { return null; } };
  const fdSave = (f, d) => { try { localStorage.setItem(fdKey(f), JSON.stringify(d)); } catch (e) { } };
  async function viewFinal() {
    const m = $main(); const F = await Core.loadFinal(); await Core.refreshFinal().catch(() => { }); const li = Core.levelInfo();
    pageHero(`CAMBRIDGE ${Core.stageName(Core.STAGE).toUpperCase()} · END OF YEAR`, 'End-of-year exams', `${Object.keys(F.papers).length} papers covering every unit · ${F.minutes} minutes · ${F.max} marks · pass above ${Math.round(F.pass * 100)}%. Passing one paper (with all ${Core.unitCount()} Unit Tests) earns your Cambridge ${Core.stageName(Core.STAGE)} certificate.`,
      [statCard(el('span', { class: 'ti big' }, '⭐'), `Level ${li.level}`, (Core.S.tester || li.level >= F.level) ? 'exams open' : `level ${F.level} needed`)]);
    if (isGuest()) { m.append(guestWall('Sign up free to take the end-of-year exams')); return; }
    if ((!Core.S.tester && li.level < F.level)) m.append(el('section', { class: 'card lockcard', id: 'levelGate' }, el('h2', {}, `🔒 Reach level ${F.level} first`), el('p', {}, `You are level ${li.level} with ${li.xp} XP. You need ${TestRules.xpForLevel(F.level)} XP – ${TestRules.xpForLevel(F.level) - li.xp} more. Every question you finish earns XP (up to 12 XP each, more for ${Core.IS_MATHS ? 'check questions and lessons' : 'pause questions and videos'}).`),
      el('div', { class: 'pbar' }, el('i', { style: `width:${Math.min(100, li.xp / TestRules.xpForLevel(F.level) * 100)}%` })), el('a', { class: 'btn primary small', href: '#bank' }, 'Practise in the Question Bank', el('span', { class: 'arr' }, ' →'))));
    const grid = el('div', { class: 'papergrid' });
    Object.keys(F.papers).sort().forEach(k => { const a = (Core.S.finalAttempts || []).find(x => x.form === k); const d = fdLoad(k);
      grid.append(el('div', { class: 'card lift paper' + (a ? (a.passed ? ' ok' : ' bad') : '') }, el('span', { class: 'eyebrow' }, 'PAPER ' + k), el('b', { class: 'lex' }, `${F.max} marks · ${F.minutes} min`),
        a ? el('span', {}, a.status === 'pending' ? '⏳ Awaiting marking' : `${+a.score.toFixed(1)}/${F.max} · ${a.pct.toFixed(1)}% ${a.passed ? '✓' : ''}`) : d && d.deadline ? el('span', { class: 'status cur' }, 'In progress') : el('span', { class: 'muted' }, 'Not taken'),
        a ? el('a', { class: 'btn small', href: '#fres-' + k }, 'Results') : el('a', { class: 'btn small ' + ((Core.S.tester || li.level >= F.level) ? 'primary' : ''), href: '#fx-' + k, 'aria-disabled': (Core.S.tester || li.level >= F.level) ? null : 'true' }, d && d.deadline ? 'Continue' : 'Open'))); });
    m.append(grid);
  }
  async function viewFinalExam(k) {
    const m = $main(); const F = await Core.loadFinal(); await Core.refreshFinal().catch(() => { }); const li = Core.levelInfo();
    if (!F || !F.papers[k]) return go('final');
    if (isGuest()) { m.append(guestWall('Sign up free to take the end-of-year exams')); return; }
    if ((Core.S.finalAttempts || []).some(a => a.form === k)) return go('fres-' + k);
    if ((!Core.S.tester && li.level < F.level)) { m.append(lockScreen(`Paper ${k} opens at level ${F.level}`, `You are level ${li.level}. Keep practising to earn XP.`, [{ what: `${TestRules.xpForLevel(F.level) - li.xp} more XP`, route: 'bank' }])); return; }
    const draft = fdLoad(k) || { answers: {}, ts: Date.now() }; const save = () => fdSave(k, draft); const qs = F.papers[k];
    if (!UI.testOn || UI.examKey !== 'F' + k) {
      UI.testOn = false;
      m.append(examIntro({ title: `End-of-year exam · Paper ${k}`, n: qs.length, max: F.max, minutes: F.minutes, passTxt: `> ${Math.round(F.pass * 100)}%`, resume: !!draft.deadline,
        extra: ['One attempt per paper. There are ' + Object.keys(F.papers).length + ' papers, so you can try another one later.', 'Results show your marks for every unit.'],
        start: async ev => { ev.currentTarget.disabled = true; try { const c = await Core.startClock(`stage${Core.STAGE}-final`, k); draft.deadline = c.deadline; save(); UI.testOn = true; UI.examKey = 'F' + k; UI.testIdx = 0; render(); } catch (x) { ev.currentTarget.disabled = false; modal('Could not open the paper', errText(x), [{ t: 'OK', cls: 'primary' }]); } } }));
      return;
    }
    examRoom({ title: `End-of-year exam · Paper ${k}`, badge: 'END-OF-YEAR EXAM', qs, max: F.max, draft, save, seed: st.id + 'F' + k, deadline: draft.deadline,
      onSubmit: async (answers, key, meta) => { const r = await Core.submitFinal(k, answers, key, meta); try { localStorage.removeItem(fdKey(k)); } catch (e) { } UI.examKey = null; if (r.attempt.passed) confetti(); go('fres-' + k); } });
  }
  async function viewFinalResult(k) {
    const m = $main(); const F = await Core.loadFinal(); await Core.refreshFinal().catch(() => { });
    const a = (Core.S.finalAttempts || []).find(x => x.form === k); if (!a) return go('fx-' + k);
    m.append(el('nav', { class: 'crumb2' }, el('a', { href: '#tests' }, 'Tests & exams'), ' › ', el('a', { href: '#final' }, 'End-of-year exams'), ` › Paper ${k}`));
    if (a.status === 'pending') { m.append(el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, 'A written answer is waiting for an Camday marker.'))); return; }
    m.append(el('section', { class: 'card ' + (a.passed ? 'done' : 'bad') }, el('div', { class: 'resultbig' }, ring(a.pct, a.passed), el('div', {}, el('span', { class: 'eyebrow' }, a.passed ? 'PASSED' : `NOT PASSED · YOU NEED ABOVE ${Math.round(F.pass * 100)}%`), el('h2', { style: 'margin:0' }, `${+a.score.toFixed(2)}/${F.max} (${a.pct.toFixed(1)}%)`),
      el('p', { style: 'margin:4px 0' }, a.duration != null ? `Time taken: ${Math.floor(a.duration / 60)} min ${a.duration % 60} s${a.overtime ? ' (after the time limit)' : ''}` : ''),
      leavesNote(a),
      el('p', { style: 'margin:4px 0' }, a.passed ? (Core.stageComplete(st) ? 'You have passed every Unit Test too – collect your certificate!' : `Pass every Unit Test as well to earn your Cambridge ${Core.stageName(Core.STAGE)} certificate.`) : 'Revise the units below and try another paper.'))),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn primary small', href: a.passed && Core.stageComplete(st) ? '#cert' : '#final' }, a.passed && Core.stageComplete(st) ? '🎓 Certificate' : 'All papers'))));
    const byU = Object.entries(a.byObj || {}).sort((x, y) => Number(x[0].slice(1)) - Number(y[0].slice(1)));
    m.append(el('section', { class: 'card' }, el('h2', {}, 'Marks by unit'), el('div', { class: 'weak' }, ...byU.map(([u, b]) => { const n = Number(u.slice(1)); const pct = b.max ? b.got / b.max * 100 : 0;
      return el('div', { class: 'wk' }, el('b', {}, `Unit ${n} · ${(Core.INDEX.units.find(x => x.n === n) || {}).t || ''}`), el('div', { class: 'pbar' + (pct < 50 ? ' red' : '') }, el('i', { style: `width:${Math.max(2, pct)}%` })), el('small', { class: 'muted' }, `${+b.got.toFixed(2)}/${b.max} marks`),
        pct < 50 ? el('a', { class: 'btn small', href: '#u-' + n, style: 'align-self:flex-start' }, `Revise Unit ${n}`) : null); }))));
    const det = el('details', { class: 'card' }, el('summary', {}, `Solutions – Paper ${k}`));
    F.papers[k].forEach((q, i) => { const p = a.per[q.id] || {}; det.append(el('div', { class: 'sol' }, el('p', {}, el('b', {}, `Question ${i + 1} (${q.obj.replace('U', 'Unit ')}, ${q.pts} mark${q.pts > 1 ? 's' : ''}): `), q.prompt), el('p', {}, 'Mark: ', el('b', {}, p.pts == null ? 'awaiting marking' : `${p.pts}/${p.max}`)), el('p', { class: 'muted' }, 'Answer: ' + (((st.solutions || {})[q.id] || {}).answer || 'shown on the device that submitted this paper')))); });
    m.append(det);
  }

  function attemptRow(a) { return el('tr', {}, el('td', {}, a.n), el('td', {}, a.form), el('td', {}, new Date(a.ts).toLocaleString('en-GB')), el('td', {}, a.status === 'final' ? `${+a.score.toFixed(2)}/30` : `${a.auto} + ?`), el('td', {}, a.status === 'final' ? a.pct.toFixed(1) + '%' : '—'), el('td', {}, a.status === 'pending' ? el('span', { class: 'status cur' }, '⏳ Awaiting marking') : a.passed ? el('span', { class: 'status done' }, '✓ Passed') : el('span', { class: 'tag d-VH' }, '✗ Not passed'))); }
  function ring(pct, ok) { const r = 46, c = 2 * Math.PI * r; const s = document.createElement('span'); s.className = 'ring'; s.innerHTML = `<svg viewBox="0 0 110 110" width="110" height="110"><circle cx="55" cy="55" r="${r}" fill="none" stroke="#DCE8FA" stroke-width="12"/><circle cx="55" cy="55" r="${r}" fill="none" stroke="${ok ? '#1E8E4E' : '#C93A3A'}" stroke-width="12" stroke-linecap="round" stroke-dasharray="${c * pct / 100} ${c}" transform="rotate(-90 55 55)"/><text x="55" y="62" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="22" fill="#1C2A3A">${Math.round(pct)}%</text></svg>`; return s; }
  function viewResult() {
    const m = $main(); m.append(bar(`Unit ${Core.UNO} › Results & history`));
    const before = JSON.stringify(Core.attempts(st).map(a => a.status));
    Core.refreshAttempts(st).then(() => { if (JSON.stringify(Core.attempts(st).map(a => a.status)) !== before && location.hash === '#result') render(); }).catch(() => { });
    const at = Core.attempts(st);
    if (!at.length) { m.append(el('section', { class: 'card' }, el('h2', {}, 'No tests taken yet'), el('a', { class: 'btn primary small', href: '#test' }, 'Go to the Unit Test'))); return; }
    const a = at[at.length - 1];
    if (a.leaves) m.append(el('div', { class: 'banner info' }, leavesNote(a)));
    if (a.status === 'pending') m.append(el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, 'Your written answer is waiting for an Camday marker. Pass/not passed is decided only when the final mark is in – you will get a notification.')));
    else if (a.passed) m.append(el('section', { class: 'card done' }, el('div', { class: 'resultbig' }, ring(a.pct, true), el('div', {}, el('span', { class: 'eyebrow' }, 'PASSED'), el('h2', { style: 'margin:0' }, `${+a.score.toFixed(2)}/30 (${a.pct.toFixed(1)}%)`), el('p', { style: 'margin:4px 0' }, `Unit ${Core.UNO} complete in ${hrs(Core.unitSeconds(Core.UNO))} of study. Your ranking score for this unit = your first-pass %: ` + ((st.results || {})[Core.UNIT] ? st.results[Core.UNIT].pct.toFixed(1) : a.pct.toFixed(1)) + '%.' + (a.duration != null ? ` Time in the exam room: ${Math.floor(a.duration / 60)} min.` : '')))),
      el('div', { class: 'btnrow' }, LEADERBOARD ? el('a', { class: 'btn primary small', href: '#board' }, '🏆 Leaderboard') : null, el('a', { class: 'btn small', href: '#cert' }, '🎓 Certificate'))));
    else {
      const left = Core.remLeft(st, a);
      m.append(el('section', { class: 'card bad' }, el('div', { class: 'resultbig' }, ring(a.pct, false), el('div', {}, el('span', { class: 'eyebrow', style: 'color:#B42318' }, 'NOT PASSED · YOU NEED ABOVE 70%'), el('h2', { style: 'margin:0' }, `${+a.score.toFixed(2)}/30 (${a.pct.toFixed(1)}%)`), el('p', { style: 'margin:4px 0' }, 'Here is where you went wrong and what to do next:'))),
        el('div', { class: 'weak' }, ...a.weak.map(o => { const sg = C.segments[o]; const s = Core.sec(sg[0]); const b = a.byObj[o];
          return el('div', { class: 'wk' }, el('b', {}, `${o} – ${C.objectives[o].t}`), el('div', { class: 'pbar red' }, el('i', { style: `width:${Math.max(2, b.got / b.max * 100)}%` })), el('small', { class: 'muted' }, `${+b.got.toFixed(2)}/${b.max} marks`),
            el('button', { class: 'btn small', type: 'button', style: 'align-self:flex-start', onclick: () => go('v-' + R(s.id), { seek: { sec: s.id, from: sg[1], to: sg[2] } }) }, svgI(I.play, 14, '#0149AF', 2.6), `Rewatch lesson ${s.id}: ${sg[3]} (${fullT(s, sg[1])}–${fullT(s, sg[2])})`)); })),
        el('p', {}, el('b', {}, `Review questions set: ${a.remed.length - left.length} of ${a.remed.length} done.`)),
        el('div', { class: 'btnrow' }, left.length ? el('a', { class: 'btn primary shine', href: '#remedial', id: 'goRemedial' }, 'Do the review questions', el('span', { class: 'arr' }, '→')) : el('a', { class: 'btn gold shine', href: '#test', id: 'goRetake' }, `Take the equivalent paper (Paper ${Core.nextForm(st)})`, el('span', { class: 'arr' }, '→')))));
    }
    m.append(el('section', { class: 'card' }, el('h2', {}, 'Attempt history'), el('p', { class: 'muted', style: 'margin-top:-6px' }, 'Every attempt is kept.'), el('div', { class: 'tablewrap' }, el('table', { class: 'grid', id: 'history' }, el('tr', {}, ...['Attempt', 'Paper', 'Date', 'Score', '%', 'Result'].map(h => el('th', {}, h))), ...at.map(attemptRow)))));
    at.slice().reverse().forEach(x => {
      const qs = C.tests[x.form]; const det = el('details', { class: 'card' }, el('summary', {}, `Solutions – attempt ${x.n} (Paper ${x.form})`));
      qs.forEach((q, i) => { const p = x.per[q.id]; det.append(el('div', { class: 'sol' }, el('p', {}, el('b', {}, `Question ${i + 1} (${q.obj}, ${q.pts} mark${q.pts > 1 ? 's' : ''}): `), q.prompt), el('p', {}, 'Mark: ', el('b', {}, p.pts == null ? 'awaiting marking' : `${p.pts}/${p.max}`)), el('p', { class: 'muted' }, 'Answer: ' + (((st.solutions || {})[q.id] || {}).answer || 'shown on the device that submitted this attempt')))); });
      m.append(det);
    });
  }

  /* ---------- concept map (Camday's own maps for every unit): tap a concept → its video and questions ---------- */
  function cmapLayout(cm) {
    const COLW = 220, X0 = 110, W = { root: 210, key: 196, node: 184, info: 196 }, CH = { root: 22, key: 26, node: 27, info: 29 };
    const wrap = (t, n) => { const out = []; let line = ''; String(t).split(' ').forEach(w => { if ((line + ' ' + w).trim().length > n) { if (line) out.push(line); line = w; } else line = (line + ' ' + w).trim(); }); if (line) out.push(line); return out; };
    const nodes = cm.nodes.map(n => { const w = W[n.k] || 184, title = wrap(n.t, n.k === 'root' ? 18 : 22), det = (n.d || []).flatMap(x => wrap(x, CH[n.k] || 26).map((l, i) => (i ? '  ' : '• ') + l));
      const h = 18 + title.length * (n.k === 'root' ? 24 : 19) + (det.length ? 8 + det.length * 17 : 0) + 10; return { ...n, w, h, title, det }; });
    const rows = {}; nodes.forEach(n => { rows[n.r] = Math.max(rows[n.r] || 0, n.h); });
    const ys = {}; let y = 30; Object.keys(rows).map(Number).sort((a, b) => a - b).forEach(r => { ys[r] = y; y += rows[r] + 74; });
    nodes.forEach(n => { n.x = X0 + n.c * COLW; n.y = ys[n.r] + (rows[n.r] - n.h) / 2; });
    return { nodes, W: X0 * 2 + 4 * COLW, H: y - 30, by: Object.fromEntries(nodes.map(n => [n.id, n])) };
  }
  function cmapSvg(cm, interactive) {
    const L = cmapLayout(cm); let svg = `<svg viewBox="0 0 ${L.W} ${L.H}" xmlns="http://www.w3.org/2000/svg" class="cmsvg" ${interactive ? 'id="mmsvg"' : ''} role="img" aria-label="${esc(C.unit.title)} concept map"><defs><marker id="cmarr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#8DA6CC"/></marker></defs>`;
    cm.links.forEach(([a, b, lab], i) => { const p = L.by[a], q = L.by[b]; let x1, y1, x2, y2, d;
      if (q.r > p.r) { x1 = p.x; y1 = p.y + p.h; x2 = q.x; y2 = q.y; const my = (y1 + y2) / 2; d = `M${x1} ${y1} C${x1} ${my} ${x2} ${my} ${x2} ${y2 - 2}`; }
      else if (q.r < p.r) { x1 = p.x; y1 = p.y; x2 = q.x; y2 = q.y + q.h; const my = (y1 + y2) / 2; d = `M${x1} ${y1} C${x1} ${my} ${x2} ${my} ${x2} ${y2 + 2}`; }
      else { const dir = q.x > p.x ? 1 : -1; x1 = p.x + dir * p.w / 2; y1 = p.y + p.h / 2; x2 = q.x - dir * q.w / 2; y2 = q.y + q.h / 2; d = `M${x1} ${y1} C${(x1 + x2) / 2} ${y1} ${(x1 + x2) / 2} ${y2} ${x2 - dir * 2} ${y2}`; }
      svg += `<path d="${d}" class="cml" marker-end="url(#cmarr)" style="animation-delay:${i * .05}s"/>`;
      if (lab) { const lx = (x1 + x2) / 2, ly = (y1 + y2) / 2; const tw = lab.length * 6.4 + 12; svg += `<g class="cmlab"><rect x="${lx - tw / 2}" y="${ly - 10}" width="${tw}" height="19" rx="9"/><text x="${lx}" y="${ly + 4}" text-anchor="middle">${esc(lab)}</text></g>`; } });
    L.nodes.forEach(n => { const x = n.x - n.w / 2; let t = `<g class="cmn k-${n.k}" data-id="${n.id}" ${interactive ? 'tabindex="0" role="button"' : ''} aria-label="${esc(n.t)} – topic ${n.s}"><rect x="${x}" y="${n.y}" width="${n.w}" height="${n.h}" rx="${n.k === 'root' ? 26 : 14}"/>`;
      let yy = n.y + (n.k === 'root' ? 30 : 24); n.title.forEach(l => { t += `<text x="${n.x}" y="${yy}" text-anchor="middle" class="tt">${esc(l)}</text>`; yy += n.k === 'root' ? 24 : 19; });
      if (n.det.length) { yy += 4; n.det.forEach(l => { t += `<text x="${x + 12}" y="${yy}" class="dd">${esc(l)}</text>`; yy += 17; }); }
      t += `<text x="${x + n.w - 10}" y="${n.y + 14}" text-anchor="end" class="sec">${n.s}</text></g>`; svg += t; });
    const box = el('div', { class: 'mmbox cmbox', html: svg + '</svg>' }); box._L = L; return box;
  }
  function mindmapSvg(interactive) {   // used on the unit page (static preview → opens the full map)
    if (!C.cmap) return el('p', { class: 'muted' }, 'Concept map coming soon.');
    const box = cmapSvg(C.cmap, false);
    box.querySelectorAll('.cmn').forEach(g => g.addEventListener('click', () => { UI.mmPick = g.dataset.id; go('map'); }));
    return box;
  }
  /* ---------- My word book ---------- */
  function viewWords() {
    const m = $main(); const all = () => Words.list();
    const tricky = [];   // lesson words the learner found hard in the Core listening and speaking checks
    (C.sections || []).forEach(s => (s.req || []).forEach(q => { const r = st.items[q.id]; const v = q.word && (s.vocab || []).find(x => x.w === q.word); if (v && r && r.done && (!r.ok || r.assisted || r.tries > 1) && !Words.has(v.w) && !tricky.some(t => t.v.w === v.w)) tricky.push({ v, sec: s.id }); }));
    const filt = UI.wf || 'all';
    const head = el('section', { class: 'card whero' }, el('div', {}, el('h1', {}, '📒 My word book'),
      el('p', { class: 'lead' }, 'Keep the words you want to remember. Listen to them, write a note, and play the word game. Tap “I know it” when a word is easy for you.')),
      el('div', { class: 'wstats' }, el('div', {}, el('b', {}, String(all().length)), el('span', {}, 'words saved')), el('div', {}, el('b', {}, String(all().filter(x => !x.known).length)), el('span', {}, 'still learning')), el('div', {}, el('b', {}, String(all().filter(x => x.known).length)), el('span', {}, 'I know it ✓'))));
    m.append(bar('My word book'), head);
    const gameHost = el('div');
    const playBtn = el('button', { type: 'button', class: 'btn gold big shine', disabled: all().length < 1 ? true : null, onclick: () => {
      const learning = all().filter(x => !x.known); const words = learning.length ? learning : all();
      const pool = all().concat((C.sections || []).flatMap(s => s.vocab || []).map(v => Object.assign({}, v))).filter((x, i, a) => a.findIndex(y => y.w.toLowerCase() === x.w.toLowerCase()) === i);
      list.hidden = true; tools.hidden = true; gameHost.hidden = false; Words.game(gameHost, words, pool, () => { gameHost.hidden = true; list.hidden = false; tools.hidden = false; draw(); }); } }, '🎮 Practise my words');
    const tabs = el('div', { class: 'tabs', role: 'tablist' }, ...[['all', 'All'], ['learn', 'Still learning'], ['known', 'I know it ✓']].map(([k, t]) => el('button', { type: 'button', role: 'tab', 'aria-selected': String(filt === k), class: filt === k ? 'on' : '', onclick: () => { UI.wf = k; render(); } }, t)));
    const tools = el('div', { class: 'wtools' }, playBtn, tabs);
    const list = el('div', { class: 'wlist' });
    m.append(tools, gameHost, list);
    if (tricky.length) m.append(el('section', { class: 'card wtricky' }, el('b', { class: 'lex' }, `💡 Words you found tricky in Unit ${Core.UNO}`), el('p', { class: 'muted', style: 'margin:4px 0 10px' }, 'Save them so you can practise them again.'),
      el('div', { class: 'wbgrid' }, ...tricky.map(t => el('div', { class: 'wcard' }, el('button', { type: 'button', class: 'wplay', onclick: () => Words.say(t.v) }, el('span', { class: 'we' }, t.v.emoji || '🔤'), el('b', {}, t.v.w), el('small', {}, t.v.def)), Words.star(t.v, t.sec, () => setTimeout(render, 400)))))));
    m.append(Words.addForm(null, () => render()));
    if (C.sections && C.sections.some(s => (s.vocab || []).length)) m.append(el('section', { class: 'card' }, el('b', { class: 'lex' }, `📚 All the words of Unit ${Core.UNO}`), el('p', { class: 'muted', style: 'margin:4px 0 10px' }, 'Tap ☆ to save a word.'),
      ...C.sections.filter(s => (s.vocab || []).length).map(s => el('div', { class: 'wunit' }, el('h4', {}, `${s.id} ${s.title}`), el('div', { class: 'wbgrid' }, ...s.vocab.map(v => el('div', { class: 'wcard' }, el('button', { type: 'button', class: 'wplay', onclick: () => Words.say(v) }, el('span', { class: 'we' }, v.emoji || '🔤'), el('b', {}, v.w), el('small', {}, v.def)), Words.star(v, s.id, () => draw()))))))));
    function draw() {
      list.innerHTML = ''; const ws = all().filter(x => filt === 'all' || (filt === 'learn' ? !x.known : x.known));
      if (!ws.length) { list.append(el('div', { class: 'card wempty' }, el('div', { class: 'big' }, '⭐'), el('p', {}, all().length ? 'No words here yet.' : 'Your word book is empty. Tap ☆ Save on a word in a lesson, or add your own word below.'))); return; }
      let lastU = null;
      ws.forEach(x => {
        if (x.unit !== lastU) { lastU = x.unit; list.append(el('h3', { class: 'wuh' }, x.unit ? `Unit ${x.unit}` : 'My own words')); }
        const note = el('textarea', { rows: 2, maxlength: 300, placeholder: 'My note…', 'aria-label': 'My note for ' + x.w }); note.value = x.note || ''; let tm = null; note.oninput = () => { clearTimeout(tm); tm = setTimeout(() => Words.update(x.w, { note: note.value }), 400); };
        list.append(el('div', { class: 'card wentry' + (x.known ? ' known' : '') },
          el('button', { type: 'button', class: 'wbig', 'aria-label': 'Listen: ' + x.w, onclick: () => Words.say(x) }, el('span', { class: 'we' }, x.emoji || '🔤'), el('span', { class: 'wp' }, '🔊')),
          el('div', { class: 'wtext' }, el('b', {}, x.w), x.def ? el('p', {}, x.def) : null, x.sec ? el('small', { class: 'muted' }, 'Lesson ' + x.sec) : null, note),
          el('div', { class: 'wacts' }, el('button', { type: 'button', class: 'btn small' + (x.known ? ' ok' : ''), 'aria-pressed': String(!!x.known), onclick: () => { Words.update(x.w, { known: !x.known }); render(); } }, x.known ? '✓ I know it' : 'I know it'),
            el('button', { type: 'button', class: 'btn small ghost', 'aria-label': 'Remove ' + x.w, onclick: () => { Words.remove(x.w); render(); } }, '🗑'))));
      });
    }
    draw();
  }

  function viewMap() {
    const m = $main(); if (st) m.append(bar(`Unit ${Core.UNO} › Concept map`));
    m.append(el('div', {}, el('span', { class: 'eyebrow' }, `UNIT ${Core.UNO} · ${C.unit.title.toUpperCase()}`), el('h1', { style: 'margin:0;font-size:36px' }, 'Concept map'), el('p', { class: 'muted', style: 'margin:4px 0 0' }, `How the big ideas of Unit ${Core.UNO} connect. Tap any box to ${C.sections[0] && C.sections[0].lesson ? 'read' : 'watch'} that part of the lesson and answer its questions.`)));
    if (!C.cmap) { m.append(el('p', { class: 'muted' }, 'Concept map coming soon.')); return; }
    const box = cmapSvg(C.cmap, true), L = box._L, svgEl = box.querySelector('svg');
    let vb = [0, 0, L.W, L.H]; const setVB = () => svgEl.setAttribute('viewBox', vb.map(v => Math.round(v)).join(' '));
    const zoom = f => { const c = [vb[0] + vb[2] / 2, vb[1] + vb[3] / 2]; vb[2] = Math.min(L.W, Math.max(260, vb[2] * f)); vb[3] = vb[2] * L.H / L.W; vb[0] = c[0] - vb[2] / 2; vb[1] = c[1] - vb[3] / 2; setVB(); };
    const detail = el('section', { class: 'card mmdetail', id: 'cmDetail', 'aria-live': 'polite' });
    const drawer = el('aside', { class: 'cmdrawer', hidden: true, role: 'dialog', 'aria-label': 'Concept details' }, el('button', { class: 'btn small ghost cmclose', type: 'button', onclick: () => { drawer.hidden = true; drawer.querySelectorAll('video').forEach(v => v.pause()); box.querySelectorAll('.cmn').forEach(x => x.classList.remove('on')); } }, '✕ Close'), detail);
    m.append(el('div', { class: 'btnrow' }, el('button', { class: 'chip', type: 'button', onclick: () => zoom(0.75) }, '＋ Zoom in'), el('button', { class: 'chip', type: 'button', onclick: () => zoom(1.33) }, '－ Zoom out'),
      el('button', { class: 'chip', type: 'button', onclick: () => { vb = [0, 0, L.W, L.H]; setVB(); box.querySelectorAll('.cmn').forEach(n => n.classList.remove('on')); } }, 'Show all')), box, drawer);
    const pick = id => {
      const n = L.by[id]; if (!n) return; const g = box.querySelector(`.cmn[data-id="${id}"]`); box.querySelectorAll('.cmn').forEach(x => x.classList.toggle('on', x === g));
      const s = Core.sec(n.s); const lock = st ? Core.secLock(st, s) : null; drawer.hidden = false; drawer.scrollTop = 0;
      detail.innerHTML = ''; detail.append(el('span', { class: 'eyebrow' }, `TOPIC ${s.id} · ${s.title.toUpperCase()}`), el('h3', { style: 'margin:2px 0 6px;font-size:24px' }, n.t), ...(n.d || []).map(x => el('p', { style: 'margin:0 0 4px' }, '• ' + x)));
      if (lock && lock.paywall) { detail.append(el('p', { class: 'muted' }, '🔒 ' + lock.reason), el('a', { class: 'btn small gold', href: '#' + lock.route }, lock.guest ? 'Sign up free' : 'See plans')); return; }
      if (s.lesson) { const idea = (s.lesson || []).find(b => b.k === 'idea'); detail.append(...(idea ? [el('div', { class: 'lblock lb-idea', style: 'margin:8px 0' }, el('b', {}, idea.t), ...idea.p.slice(0, 2).map(t => el('p', { style: 'margin:4px 0' }, ...String(t).split(/(\*\*[^*]+\*\*)/).map(part => /^\*\*.*\*\*$/.test(part) ? el('b', {}, part.slice(2, -2)) : part))))] : []),
        el('div', { class: 'btnrow' }, el('a', { class: 'btn primary small', href: '#v-' + R(s.id) }, `📖 Lesson ${s.id} with check questions`), el('a', { class: 'btn small', href: '#ex-' + R(s.id) }, `All questions for ${s.id}`))); }
      else { const vid = el('video', { class: 'cmvideo', controls: true, preload: 'metadata', playsinline: true, src: s.video.src, poster: s.video.poster || s.video.src.replace('.mp4', '_poster.jpg') });
      detail.append(el('div', { class: 'cmvid' }, vid), el('div', { class: 'btnrow' }, el('a', { class: 'btn primary small', href: '#v-' + R(s.id) }, svgI(I.play, 14, '#fff', 2.6), `Full lesson ${s.id} with pause questions`), el('a', { class: 'btn small', href: '#ex-' + R(s.id) }, `All questions for ${s.id}`))); }
      if (!st) return;
      if (lock) { detail.append(el('p', { class: 'muted' }, '🔒 Questions for this topic open after: ' + lock.reason)); return; }
      const pool = s.req.concat(s.prac).filter(q => !(st.items[q.id] || {}).done); const qs = (pool.length ? pool : s.req).slice(0, 3);
      detail.append(el('h4', { style: 'margin:14px 0 4px' }, `Try ${qs.length} question${qs.length === 1 ? '' : 's'} on this idea`));
      qs.forEach(q => { const card = el('div', { class: 'card qcard cmq' }); detail.append(card); const rec = st.items[q.id] = st.items[q.id] || { tries: 0 };
        QE.practice(q, card, { rec, seed: st.id, save: () => Core.persist(), onCheck: onCheck(card, q, rec), onDone: () => { rec.done = true; Core.persist(); refreshToc(); } }); });
    };
    box.querySelectorAll('.cmn').forEach(g => { const act = () => pick(g.dataset.id); g.addEventListener('click', act); g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); act(); } }); });
    if (UI.mmPick != null) { pick(UI.mmPick); UI.mmPick = null; }
  }

  /* ---------- progress / profile ---------- */
  function viewProfile() {
    const m = $main(); const wl = wrongList(); const nx = Core.nextActivity(st);
    const rs = Core.rankScore(st);
    const coreDone = C.sections.reduce((a, s) => a + 8 - Core.reqLeft(st, s).length, 0), sk = Core.streak(st);
    pageHero(isGuest() ? 'GUEST · THIS DEVICE ONLY' : 'PROGRESS', isGuest() ? 'Your progress' : `${st.alias}'s progress`, isGuest() ? 'Sign up free to keep your progress on any device.' : `Everything you have done in Unit ${Core.UNO}, what is next, and what is worth revising.`,
      [statCard(flameIcon(), `${sk} day${sk === 1 ? '' : 's'}`, 'learning streak'), statCard(ringIcon(Core.levelInfo().pct), `Level ${Core.levelInfo().level}`, `${Core.levelInfo().xp} XP`), statCard(el('span', { class: 'ti big' }, '⏱'), hrs(Core.totalSeconds()), `studied · ≈ ${estH(Core.INDEX.est || 0)} course`)]);
    const tile = (icon, t, sub, on, id) => el('button', { class: 'tile lift', type: 'button', onclick: on, id }, el('span', { class: 'ti' }, icon), el('b', {}, t), el('small', {}, sub));
    m.append(el('div', { class: 'tiles' },
      tile('▶', 'Continue learning', nx.label, () => { location.hash = 'home'; setTimeout(() => document.getElementById('resumeBtn') && document.getElementById('resumeBtn').click(), 0); }, 'tileResume'),
      tile('↺', 'Redo wrong answers', `${wl.length} question${wl.length === 1 ? '' : 's'}`, () => startDrill('Redo wrong answers', wl, 'wrong'), 'tileWrong'),
      tile('🧩', 'Revise by topic', `${Object.keys(C.objectives).length} learning objectives`, () => go('topic'), 'tileTopic'),
      tile('📄', 'Worksheets opened', st.ws.length ? st.ws.map(x => 'Section ' + x).join(', ') : 'none opened yet', () => go(st.ws.length ? 'ws-' + R(st.ws[st.ws.length - 1]) : 'ws-3-1'), 'tileWs')));
    if (st.ws.length) m.append(el('div', { class: 'btnrow' }, ...st.ws.map(x => el('a', { class: 'chip', href: '#ws-' + R(x) }, '📄 Worksheet ' + x))));
    // certificate progress for the whole stage (80 % of lessons and 80 % of Unit Tests)
    const certBox = el('section', { class: 'card pcert', id: 'certProgress' }); m.append(certBox);
    if (!isGuest()) Core.levelProgress().then(p => { const row = (label, v) => el('div', { class: 'pc-row' }, el('span', {}, label), el('div', { class: 'pbar goal' + (v >= Core.MOVE_ON ? ' ok' : '') }, el('i', { style: `width:${Math.min(100, v)}%` }), el('em', { style: `left:${Core.MOVE_ON}%`, 'aria-hidden': 'true' })), el('b', {}, `${v}%`));
      certBox.append(el('div', { class: 'pc-head' }, el('div', {}, el('span', { class: 'hl' }, `Stage ${Core.learnerStage()} certificate`), el('h2', {}, p.ready ? 'You have earned your certificate' : `Reach ${Core.MOVE_ON}% in both to earn your certificate`)), el('a', { class: 'btn small', href: '#cert' }, p.ready ? 'Open my certificate' : 'About the certificate', el('span', { class: 'arr' }, ' →'))),
        row('Lessons finished', p.lessons), row('Unit Tests passed', p.tests)); }).catch(() => certBox.remove()); else certBox.remove();
    const cell = (done, total) => el('span', { class: 'pt-cell' }, el('b', {}, `${done}/${total}`), el('span', { class: 'pbar mini' + (total && done >= total ? ' ok' : '') }, el('i', { style: `width:${total ? Math.round(done / total * 100) : 0}%` })));
    const rowsP = C.sections.map(s => { const vd = Core.videoDone(st, s), core = 8 - Core.reqLeft(st, s).length, pr = s.prac.filter(q => (st.items[q.id] || {}).done).length, ad = s.adv.filter(q => (st.items[q.id] || {}).done).length, done = Core.secDone(st, s), started = vd || core || pr || ad;
      return el('a', { class: 'pt-row', href: '#v-' + R(s.id) }, el('span', { class: 'pt-topic' }, el('span', { class: 'pt-num' }, s.id), el('b', {}, s.title)),
        el('span', { class: 'pt-cell' }, vd ? el('span', { class: 'status done' }, '✓ Done') : el('span', { class: 'status todo' }, 'Not yet')), cell(core, 8), cell(pr, s.prac.length), cell(ad, s.adv.length),
        el('span', {}, done ? el('span', { class: 'status done' }, '✓ Complete') : started ? el('span', { class: 'status cur' }, 'In progress') : el('span', { class: 'status todo' }, 'Not started'))); });
    const att = Core.attempts(st).length;
    m.append(el('section', { class: 'card ptable', id: 'unitProgress' }, el('div', { class: 'pc-head' }, el('div', {}, el('span', { class: 'hl' }, `Unit ${Core.UNO}`), el('h2', {}, C.unit.title)), el('a', { class: 'btn small', href: '#u-' + Core.UNO }, 'Open the unit', el('span', { class: 'arr' }, ' →'))),
      el('div', { class: 'pt-row h' }, el('span', {}, 'TOPIC'), el('span', {}, C.sections[0] && C.sections[0].lesson ? 'LESSON' : 'VIDEO'), el('span', {}, 'CORE'), el('span', {}, 'PRACTICE'), el('span', {}, 'ADVANCED'), el('span', {}, 'STATUS')), ...rowsP,
      el('div', { class: 'pt-test' }, el('div', {}, el('b', {}, `Unit Test ${Core.UNO}`), el('span', { class: 'muted' }, Core.passed(st) ? 'Passed' : att ? 'Not passed yet' : 'Not taken yet')),
        el('div', {}, el('b', {}, String(att)), el('span', { class: 'muted' }, att === 1 ? 'attempt' : 'attempts')),
        el('div', {}, el('b', {}, rs ? rs.score.toFixed(1) + '%' : '–'), el('span', { class: 'muted' }, 'average first-pass score')),
        el('div', { class: 'btnrow', style: 'margin:0' }, el('a', { class: 'btn small', href: '#result' }, 'Results & history'), el('a', { class: 'btn small primary', href: '#test' }, 'Unit Test', el('span', { class: 'arr' }, ' →'))))));
    const tt = testerTools(); if (tt) m.append(tt);
    m.append(el('p', { class: 'muted' }, el('a', { href: '#privacy-kids' }, 'How Camday looks after your data'), ' – the short version for learners.'));
  }

  /* ---------- leaderboard ---------- */
  const SAMPLE = [{ alias: 'Sample · Nova', score: 91.5, units: 14 }, { alias: 'Sample · Quark', score: 86.0, units: 14 }, { alias: 'Sample · Ion', score: 86.0, units: 14 }, { alias: 'Sample · Proton', score: 78.25, units: 14 }];
  async function viewBoard() {
    const m = $main();
    const hero = el('section', { class: 'lbhero' }); const hin = el('div', { class: 'in' }); hero.append(hin); document.getElementById('wrap').before(hero);
    const holder = el('div'); m.append(holder);
    const live = await Backend.leaderboard(Core.STAGE).catch(() => []);
    const rows = live.filter(r => r.score != null).map(r => ({ alias: r.nickname, score: Number(r.score), units: r.units, me: !!r.is_mine && st && r.nickname === st.alias, src: r.opted_in ? 'Shown' : 'Only you can see this' }));
    if (Backend.mode === 'demo') SAMPLE.forEach(r => rows.push({ ...r, src: 'sample data' }));
    Core.competitionRank(rows);
    hin.append(el('span', { class: 'eyebrow', style: 'color:#F3BF69' }, `CAMBRIDGE ${Core.stageLabel().toUpperCase()}`), el('h1', {}, '🏆 Leaderboard'),
      el('div', { class: 'formula' }, el('b', { style: 'color:#fff' }, 'Ranking score = (Σ first-pass % of each unit) ÷ number of units'), ' — every unit counts equally. Your first-pass % is fixed the moment you first pass a unit; revising or retaking later never changes it. Equal scores share a rank.'));
    const top = rows.slice(0, 3); const order = [top[1], top[0], top[2]];
    hin.append(el('div', { class: 'podium' }, ...order.map((r, k) => r ? el('div', { class: 'p' }, k === 1 ? el('span', { style: 'font-size:30px;animation:floaty 2.2s ease-in-out infinite' }, '👑') : null, el('span', { class: 'av', style: r.me ? 'background:#F3BF69;color:#1C2A3A' : '' }, r.alias.replace('Sample · ', '').slice(0, 1).toUpperCase()), el('b', { class: 'lex' }, r.alias + (r.me ? ' (you)' : '')), el('small', { style: 'color:#C9D6EA' }, r.score.toFixed(2) + '%'),
      el('div', { class: 'blk', style: `height:${[130, 170, 100][k]}px;background:${['#2F6FD6', '#0149AF', '#5B8FDB'][k]}` }, el('b', {}, String(r.rank)))) : el('div', { class: 'p' }))));
    const hidden = st && !(st.learner && st.learner.leaderboard_opt_in);
    if (hidden) holder.append(el('div', { class: 'banner info', id: 'lbHidden' }, el('b', {}, 'You are hidden. '), 'Only you can see your own row. You can show your nickname in ', el('a', { href: '#settings' }, 'Settings'), '.'));
    holder.append(el('div', { class: 'card lbtable' }, el('div', { class: 'lbrow h' }, el('span', {}, 'RANK'), el('span', {}, 'LEARNER'), el('span', {}, 'RANKING SCORE'), el('span', {}, 'UNITS'), el('span', { class: 'xpcol' }, 'VISIBILITY')),
      el('div', { id: 'boardTable' }, ...(rows.length ? rows.map(r => el('div', { class: 'lbrow' + (r.me ? ' me' : ''), role: 'row' }, el('span', { class: 'rk' }, String(r.rank)), el('span', { class: 'who' }, el('span', { class: 'a' }, r.alias.replace('Sample · ', '').slice(0, 1).toUpperCase()), el('b', {}, r.alias + (r.me ? ' (you)' : ''))), el('span', { class: 'sc' }, r.score.toFixed(2) + '%'), el('span', {}, String(r.units)), el('span', { class: 'xpcol muted' }, r.src))) : [el('p', { class: 'muted', style: 'padding:16px 24px' }, 'No ranked learners yet – pass a Unit Test to appear here.')]))),
      el('p', { class: 'muted' }, 'Only nicknames are shown, and only for learners who have switched the leaderboard on.' + (Backend.mode === 'demo' ? ' Rows marked “sample data” are illustrations, not real learners.' : '')));
  }


  /* =====================================================================
     ACCOUNT, PLANS, HELP, LEGAL  (P0 / P1 screens)
     ===================================================================== */
  const ERR = { practised: 'You have practised this paper, so it can no longer be sat as a timed paper.', not_taken: 'Sit this paper first to see all its solutions.', wrong_question: 'That question is not on this paper.', locked: 'This course is not open yet.', bad_email: 'Please enter a valid email address.', weak_password: 'Use at least 8 characters for your password.', email_taken: 'An account with this email already exists – sign in instead.',
    bad_credentials: 'That email and password do not match.', account_disabled: 'This account has been switched off by Camday. Please contact us via Help & contact.', user_banned: 'This account has been switched off by Camday. Please contact us via Help & contact.', admin_only: 'Only administrators can do this.', own_admin: 'You cannot remove your own administrator role.', own_account: 'You cannot switch off your own account.', sign_in: 'Please sign in again.', parental_consent: 'Please tick the parental consent box.', bad_nickname: 'Use a nickname of 2–24 characters.',
    subscription_required: 'This needs an Camday course plan.', locked: 'Finish every lesson or video and every Core question first.', awaiting_marking: 'Your last test is still being marked.', review_first: 'Finish your review questions first.',
    already_passed: 'You have already passed this test.', wrong_paper: 'Please reload the page and try again.', confirm: 'Type the confirmation exactly as shown.', staff_only: 'Staff only.', message: 'Please write a short message.' };
  const errText = e => ERR[e && e.code] || (e && e.detail) || 'Something went wrong. Please try again.';
  const COUNTRIES = [['GB', 'United Kingdom'], ['SG', 'Singapore'], ['MY', 'Malaysia'], ['TH', 'Thailand'], ['VN', 'Vietnam'], ['ID', 'Indonesia'], ['PH', 'Philippines'], ['XX', 'Another country']];
  const field = (label, input, hint) => el('label', { class: 'field' }, el('span', {}, label), input, hint ? el('small', { class: 'muted' }, hint) : null);
  const errBox = () => el('p', { class: 'err', role: 'alert' });
  const narrow = (...kids) => el('section', { class: 'card narrow' }, ...kids);

  /* ---------- public landing (Design: "Main" – try the course in small boxes, no sign-up) ---------- */
  const DEMO_PQ = [['Its surface area', true], ['The thickness of its cell wall', false], ['The number of nuclei', false]];
  const DEMO_PRAC = [
    { id: 'p1', diff: 'M', p: 'What is a microorganism?', o: [['Any organism with one organ', 'That is not the definition.'], ['An organism so small you need a microscope to see it', 'Correct!'], ['A part of a cell', 'Parts of cells are not organisms.'], ['Only bacteria', 'Yeast and amoebae are microorganisms too.']], ok: 1 },
    { id: 'p2', diff: 'H', p: 'Which change would make a root hair cell absorb water more slowly?', o: [['A longer extension', 'That would speed absorption up.'], ['More root hairs', 'That would speed absorption up.'], ['A shorter extension (smaller surface area)', 'Correct! Less surface area, slower absorption.'], ['Wetter soil', 'Wetter soil means more water to absorb.']], ok: 2 },
    { id: 'p3', diff: 'H', p: 'Palisade cells are near the upper surface of a leaf. Why is this useful?', o: [['It is where most light reaches, so chloroplasts absorb more light energy', 'Correct!'], ['It is closest to the soil water', 'Roots are closest to soil water.'], ['It protects the leaf from insects', 'That is the job of the epidermis.'], ['It is where oxygen is stored', 'Leaves do not store oxygen there.']], ok: 0 },
    { id: 'p4', diff: 'VH', p: 'Algae are unicellular, live in water and contain chloroplasts. Which statement is correct?', o: [['They are animals because they move', 'Moving alone does not make them animals.'], ['They are plants because they have chloroplasts', 'Plants are multicellular; these algae are not.'], ['They cannot make food', 'Chloroplasts let them make food.'], ['They can photosynthesise, but they are not plants because plants are multicellular', 'Correct!']], ok: 3 }];
  const DEMO_TEST = [{ q: 'Which organism is unicellular?', o: ['Elephant', 'Paramecium', 'Sunflower', 'Mushroom'], ok: 1 },
    { q: 'Which part contains the instructions (DNA) passed from parents to offspring?', o: ['Cytoplasm', 'Vacuole', 'Nucleus', 'Cell wall'], ok: 2 },
    { q: 'Which is a limitation of a 2D cell diagram?', o: ['Real cells are 3D', 'It has labels', 'It shows the nucleus', 'It is easy to learn from'], ok: 0 }];
  const DIFF_L = { M: 'Standard', H: 'Challenging', VH: 'Stretch' };
  const UNIT_NAMES = [[1, 'Introducing Science'], [2, 'Measurements'], [3, 'Cells'], [4, 'Classifying Living Things'], [5, 'Food Chains and Food Webs'], [6, 'Materials and Their Structure'], [7, 'Properties of Materials'], [8, 'Acids and Alkalis'], [9, 'Chemical Reactions'], [10, 'Forces'], [11, 'Energy'], [12, 'Electricity'], [13, 'Earth Processes'], [14, 'Earth and Beyond']];
  const PQ_AT = 30; // seconds into the 3.3 video: the root hair cell has been explained
  const demoInit = () => ({ step: 'watch', vt: 0, pqPick: -1, pqDone: false, vidDone: false, diff: 'all', open: 'p2', prac: {}, test: 'idle', ti: 0, tAns: [], tPick: -1, tLeft: 60 });
  function viewLanding() {
    const m = $main(); document.getElementById('wrap').classList.add('landing');
    const D = UI.demo = UI.demo || demoInit();
    const level = (badge, t, d, tag, open, on) => el(open ? 'button' : 'div', { class: 'card lift lp-level' + (open ? '' : ' off'), type: open ? 'button' : null, onclick: on || null },
      el('span', { class: 'pop lp-badge' + (open ? ' on' : '') }, badge), el('span', { class: 'lp-lt' }, el('b', {}, t), el('br'), el('small', {}, d)), el('span', { class: 'lp-tag' + (open ? ' open' : '') }, tag));
    const scrollTry = () => document.getElementById('try').scrollIntoView({ behavior: 'smooth', block: 'start' });
    document.getElementById('wrap').before(el('div', { class: 'newsstrip' }, el('span', {}, 'New: choose one, two or all three subjects for your stage'), el('a', { href: '#news' }, 'See what is new  ›')));
    document.getElementById('wrap').before(el('section', { class: 'lp-hero dots' }, el('div', { class: 'lp-hero-in' },
      el('div', { class: 'lp-hero-txt' },
        el('span', { class: 'lp-pill' }, el('span', { class: 'lp-ping' }, el('i'), el('i')), 'Science · Mathematics · English · Stages 1 to 9'),
        el('h1', {}, 'Try the whole course.', el('br'), el('span', {}, 'Right here, right now.')),
        el('p', {}, 'No sign-up. Watch a lesson, answer questions, sit a mini test and see your progress — all on this page.'),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn primary big shine', type: 'button', id: 'heroStart', onclick: scrollTry }, 'Start the tour ', el('span', { class: 'arr' }, '↓')),
          el('button', { class: 'btn big', type: 'button', id: 'heroGuest', onclick: startGuest }, 'Open topic 3.1'))),
      (() => { // course picker: subject + stage → the course page
        const subj = el('select', { id: 'pickSubj', 'aria-label': 'Subject' }, el('option', { value: '0' }, 'Science'), el('option', { value: '10' }, 'Mathematics'), el('option', { value: '20' }, 'English (ESL)'));
        const stg = el('select', { id: 'pickStage', 'aria-label': 'Stage' }, ...[1, 2, 3, 4, 5, 6, 7, 8, 9].map(n => el('option', { value: n, selected: n === 7 ? '' : null }, `Stage ${n}`)));
        const view = () => { const g = Number(subj.value) + Number(stg.value); go(Core.subjectKeys(Number(stg.value)).includes(g) && !Core.stageLocked(g) ? 'stage-' + g : 'courses'); };
        const feat = (svg, t) => el('span', { class: 'lp-feat' }, el('i', { 'aria-hidden': 'true', html: svg }), el('b', {}, t));
        const ic = d => `<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${d}</svg>`;
        return el('div', { class: 'lp-levels' },
          el('b', { class: 'lp-picklab' }, 'Explore the courses for Cambridge Stages 1 to 9'),
          el('div', { class: 'lp-pick', id: 'coursePick' }, el('span', { class: 'lp-picktag' }, 'Choose a course'),
            el('label', { class: 'lp-pf' }, el('span', {}, 'Subject'), subj), el('label', { class: 'lp-pf' }, el('span', {}, 'Stage'), stg),
            el('button', { class: 'btn primary', type: 'button', id: 'pickView', onclick: view }, 'View ', el('span', { class: 'arr' }, '→'))),
          el('div', { class: 'lp-feats' }, feat(ic('<path d="M8 5v14l11-7z"/>'), 'Lessons that ask questions'), feat(ic('<path d="M4 20h16M6 16l10-10 3 3-10 10H6z"/>'), 'Practice for every topic'), feat(ic('<circle cx="12" cy="9" r="5"/><path d="M9 13.5 8 21l4-2 4 2-1-7.5"/>'), 'Unit Tests and a certificate')));
      })())));

    // ---- the four-box demo ----
    const panel = el('div', { class: 'lp-panel' }), nav = el('nav', { class: 'lp-steps', 'aria-label': 'Demo steps' }), badge = el('span', { class: 'lp-count' });
    m.append(el('section', { id: 'try', class: 'lp-try' }, el('div', { class: 'lp-head' }, el('h2', {}, 'Learn it, practise it, prove it'), el('p', {}, 'A real lesson from Cambridge Stage 7, Unit 3: Cells. Go through the four steps — it takes about two minutes.')),
      el('div', { class: 'card lp-demo' }, el('div', { class: 'lp-bar' }, el('span', { class: 'lp-dots', 'aria-hidden': 'true' }, el('i'), el('i'), el('i')), el('span', {}, 'Cambridge Stage 7 · Unit 3: Cells · 3.3 Cells with special jobs'), badge),
        el('div', { class: 'lp-body' }, nav, panel))));
    const set = p => { Object.assign(D, p); draw(); };
    const optEl = (k, t, state, on) => el('button', { type: 'button', class: 'lp-opt ' + state, onclick: on }, el('span', { class: 'k' }, k), el('span', { class: 't' }, t));
    let vid = null;
    function draw() {
      const watched = D.vidDone, practised = Object.keys(D.prac).length >= 2, tested = D.test === 'done';
      const done = { watch: watched, practise: practised, test: tested, progress: tested && D.step === 'progress' };
      badge.textContent = `Demo · ${Object.values(done).filter(Boolean).length} of 4 steps done`;
      nav.innerHTML = '';
      [['watch', 'Watch', 'A lesson that pauses to ask you'], ['practise', 'Practise', 'Questions with instant feedback'], ['test', 'Test', 'A timed mini Unit Test'], ['progress', 'Progress', 'See what you have mastered']].forEach(([k, t, d], i) => {
        const cur = D.step === k; nav.append(el('button', { type: 'button', class: 'lp-step' + (cur ? ' cur' : ''), 'aria-current': cur ? 'step' : null, 'data-step': k, onclick: () => { if (vid && k !== 'watch') vid.pause(); set({ step: k }); } },
          el('span', { class: 'lp-dot' + (done[k] ? ' done' : cur ? ' cur' : '') }, done[k] ? '✓' : String(i + 1)), el('span', {}, el('b', {}, t), el('br'), el('small', {}, d))));
      });
      if (D.step !== 'watch' || !vid) { panel.innerHTML = ''; vid = null; }
      if (D.step === 'watch') drawWatch(); else if (D.step === 'practise') drawPractise(); else if (D.step === 'test') drawTest(); else drawProgress();
    }
    function drawWatch() {
      if (!vid) {
        vid = el('video', { src: 'media/demo_u3_s3.mp4', poster: 'media/demo_u3_s3_poster.jpg', playsinline: true, preload: 'metadata', 'aria-label': 'Lesson video: specialised plant cells', class: 'lp-video' }); activeVideo = vid;
        const ov = el('div', { class: 'lp-ov', hidden: true }), playBig = el('button', { type: 'button', class: 'lp-play pulse', 'aria-label': 'Play lesson', onclick: () => vid.play() }, svgI(I.play, 32, '#1C2A3A', 2.6));
        const pbar = el('i'), time = el('span', { class: 'lp-time' }, '0:00 / 1:28'), pp = el('button', { type: 'button', class: 'btn primary small lp-pp', 'aria-label': 'Play or pause' }, svgI(I.play, 16, '#fff', 2.6));
        pp.onclick = () => { if (ov.hidden === false && !D.pqDone) return; vid.paused ? vid.play() : vid.pause(); };
        const syncBtn = () => { pp.innerHTML = ''; pp.append(svgI(vid.paused ? I.play : I.pause, 16, '#fff', 2.6)); playBig.hidden = !vid.paused || !ov.hidden; };
        vid.addEventListener('play', syncBtn); vid.addEventListener('pause', syncBtn);
        vid.addEventListener('timeupdate', () => {
          const t = vid.currentTime, dur = vid.duration || 88; D.vt = t; pbar.style.width = (t / dur * 100) + '%'; time.textContent = `${fmt(t)} / ${fmt(dur)}`;
          if (!D.pqDone && t >= PQ_AT) { vid.pause(); showPQ(); }
        });
        vid.addEventListener('ended', () => { D.vidDone = true; ov.hidden = false; ov.innerHTML = ''; ov.append(el('div', { class: 'lp-done' }, el('span', { class: 'lp-tick' }, '✓'), el('b', {}, 'Lesson complete'), el('button', { type: 'button', class: 'btn gold', id: 'demoNext1', onclick: () => set({ step: 'practise' }) }, 'Next: practise ', el('span', { class: 'arr' }, '→')))); draw(); });
        function showPQ() {
          ov.hidden = false; ov.innerHTML = ''; syncBtn();
          const ok = D.pqPick >= 0 && DEMO_PQ[D.pqPick][1];
          const box = el('div', { class: 'lp-pq' }, el('span', { class: 'lp-eyebrow gold' }, 'PAUSE QUESTION'), el('b', {}, 'What does the long extension of a root hair cell increase?'),
            ...DEMO_PQ.map((p, i) => optEl('ABC'[i], p[0], D.pqPick < 0 ? 'idle' : p[1] && D.pqPick === i ? 'ok' : D.pqPick === i ? 'bad' : 'idle', () => { if (D.pqPick < 0 || !ok) { D.pqPick = i; showPQ(); } })));
          if (D.pqPick >= 0) box.append(el('div', { class: 'btnrow', style: 'margin:0' }, el('span', { class: 'lp-fb ' + (ok ? 'ok' : 'bad') }, ok ? 'Correct — a bigger surface area means faster absorption.' : 'Not quite — think about what the extension adds to the cell.'),
            el('button', { type: 'button', class: 'btn primary small', id: 'pqGo', onclick: () => { if (ok) { D.pqDone = true; ov.hidden = true; vid.currentTime = PQ_AT + 0.3; vid.play(); } else { D.pqPick = -1; showPQ(); } } }, ok ? 'Keep watching →' : 'Try again')));
          ov.append(box);
        }
        panel.append(el('div', { class: 'lp-watch' }, el('div', { class: 'lp-screen' }, vid, playBig, ov),
          el('div', { class: 'lp-controls' }, pp, el('div', { class: 'lp-track' }, pbar, el('span', { class: 'lp-mark', title: 'Pause question', style: `left:${PQ_AT / 87.7 * 100}%` })), time),
          el('p', { class: 'muted', style: 'margin:0' }, 'The video stops halfway to ask you a question — answer it to keep watching.')));
        if (D.vidDone) vid.dispatchEvent(new Event('ended')); else if (D.vt) { vid.currentTime = D.vt; if (!D.pqDone && D.vt >= PQ_AT) showPQ(); }
      }
    }
    function drawPractise() {
      const box = el('div', { class: 'lp-prac' }); panel.append(box);
      box.append(el('div', { class: 'btnrow between', style: 'margin:0' }, el('div', { class: 'lp-chips', role: 'group', 'aria-label': 'Difficulty' }, ...[['all', 'All'], ['M', 'Standard'], ['H', 'Challenging'], ['VH', 'Stretch']].map(([k, t]) => el('button', { type: 'button', class: 'lp-chip' + (D.diff === k ? ' on' : ''), 'aria-pressed': String(D.diff === k), onclick: () => set({ diff: k }) }, t))),
        el('small', { class: 'muted' }, `${Object.keys(D.prac).length} of 4 answered`)));
      DEMO_PRAC.filter(q => D.diff === 'all' || q.diff === D.diff).forEach(q => {
        const a = D.prac[q.id], open = D.open === q.id, answered = a !== undefined;
        const card = el('div', { class: 'card lp-q' }, el('button', { type: 'button', class: 'lp-qh', 'aria-expanded': String(open), onclick: () => set({ open: open ? '' : q.id }) },
          el('span', { class: 'lp-qd' + (answered ? (a === q.ok ? ' ok' : ' bad') : '') }), el('span', { class: 'lp-qp' }, q.p), el('span', { class: 'lp-diff ' + q.diff }, DIFF_L[q.diff]), el('span', { class: 'lp-chev' + (open ? ' up' : '') }, '⌄')));
        if (open) card.append(el('div', { class: 'lp-qb' }, ...q.o.map((o, i) => optEl('ABCD'[i], o[0], !answered ? 'idle' : i === q.ok ? 'ok' : i === a ? 'bad' : 'idle', () => { if (!answered) set({ prac: Object.assign({}, D.prac, { [q.id]: i }) }); })),
          answered ? el('div', { class: 'lp-fbbox ' + (a === q.ok ? 'ok' : 'bad') }, q.o[a][1]) : null));
        box.append(card);
      });
      box.append(el('button', { type: 'button', class: 'btn gold', id: 'demoNext2', style: 'align-self:flex-end', onclick: () => set({ step: 'test' }) }, 'Next: mini test ', el('span', { class: 'arr' }, '→')));
    }
    function drawTest() {
      clearInterval(timer);
      const box = el('div', { class: 'lp-test' }); panel.append(box);
      const start = () => { set({ test: 'run', ti: 0, tAns: [], tPick: -1, tLeft: 60 }); };
      if (D.test === 'idle') { box.append(el('div', { class: 'lp-center' }, el('span', { class: 'lp-clock floaty', 'aria-hidden': 'true' }, el('i')), el('h3', {}, 'Mini Unit Test'), el('p', { class: 'muted' }, '3 questions · 60 seconds · no hints. Score above 70% to “unlock” the next unit.'), el('button', { type: 'button', class: 'btn primary big shine', id: 'demoStartTest', onclick: start }, 'Start the test'))); return; }
      if (D.test === 'run') {
        const T = DEMO_TEST[D.ti]; const clock = el('span', { class: 'lp-timer' + (D.tLeft <= 10 ? ' low' : '') }, `⏱ ${fmt(D.tLeft)}`), tb = el('i', { style: `width:${D.tLeft / 60 * 100}%` });
        box.append(el('div', { class: 'btnrow between', style: 'margin:0' }, el('b', { class: 'lex' }, `Question ${D.ti + 1} of 3`), clock), el('div', { class: 'lp-track t' }, tb), el('b', { class: 'lp-tq' }, T.q),
          ...T.o.map((o, i) => optEl('ABCD'[i], o, D.tPick === i ? 'sel' : 'idle', () => set({ tPick: i }))),
          el('button', { type: 'button', class: 'btn primary', id: 'demoTNext', disabled: D.tPick < 0, style: 'align-self:flex-end', onclick: () => { const ans = D.tAns.concat([D.tPick]); if (D.ti === 2) { clearInterval(timer); set({ test: 'done', tAns: ans }); } else set({ tAns: ans, ti: D.ti + 1, tPick: -1 }); } }, D.ti === 2 ? 'Submit →' : 'Next question →'));
        timer = setInterval(() => { if (D.step !== 'test' || D.test !== 'run') return clearInterval(timer); D.tLeft--; if (D.tLeft <= 0) { clearInterval(timer); set({ test: 'done' }); return; } clock.textContent = `⏱ ${fmt(D.tLeft)}`; clock.classList.toggle('low', D.tLeft <= 10); tb.style.width = (D.tLeft / 60 * 100) + '%'; }, 1000);
        return;
      }
      const score = D.tAns.filter((a, i) => a === DEMO_TEST[i].ok).length, pct = Math.round(score / 3 * 100), pass = pct > 70;
      if (pass) confetti();
      box.append(el('div', { class: 'lp-center' }, el('span', { class: 'lp-ring', style: `background:conic-gradient(${pass ? '#1E8E4E' : '#0149AF'} 0 ${pct}%, #DCE8FA 0)` }, el('b', { id: 'demoScore' }, pct + '%')),
        el('h3', {}, pass ? 'Passed — next unit unlocked!' : 'Nearly there'), el('p', { class: 'muted' }, pass ? 'You scored above 70%. In the full course this opens the next unit straight away.' : 'Below 70% — in the full course we show you exactly which ideas to revise, then let you sit Paper B.'),
        el('div', { class: 'btnrow', style: 'justify-content:center' }, el('button', { type: 'button', class: 'btn', onclick: start }, 'Try again'), el('button', { type: 'button', class: 'btn gold', id: 'demoNext3', onclick: () => set({ step: 'progress' }) }, 'See my progress →'))));
    }
    function drawProgress() {
      const tested = D.test === 'done', pct = Math.round(D.tAns.filter((a, i) => a === DEMO_TEST[i].ok).length / 3 * 100);
      const right = DEMO_PRAC.filter(q => D.prac[q.id] === q.ok).length, n = Object.keys(D.prac).length;
      const b1 = (D.vidDone ? 40 : 10) + (D.prac.p2 === 2 ? 30 : 0) + (D.prac.p3 === 0 ? 30 : 0), b2 = (D.prac.p1 === 1 ? 50 : 0) + (D.tAns[0] === 1 ? 50 : 0), b3 = (D.tAns[1] === 2 ? 50 : 0) + (D.tAns[2] === 0 ? 50 : 0);
      const col = v => v >= 80 ? '#1E8E4E' : v >= 50 ? '#0149AF' : '#F08A4B';
      panel.append(el('div', { class: 'lp-progress' },
        el('div', { class: 'lp-kpis' }, ...[['Lesson', D.vidDone ? 'Watched' : Math.round(D.vt / 87.7 * 100) + '%'], ['Practice', `${right} / ${n} correct`], ['Mini test', tested ? pct + '%' : 'Not taken']].map(([l, v]) => el('div', { class: 'card lp-kpi' }, el('small', {}, l), el('b', {}, v)))),
        el('b', { class: 'lex' }, 'How secure is each idea?'),
        ...[['Cells with special jobs', b1], ['Microorganisms', b2], ['Cell structure and models', b3]].map(([t, v]) => el('div', { class: 'lp-barrow' }, el('span', {}, t), el('div', { class: 'lp-track' }, el('i', { style: `width:${v}%;background:${col(v)}` })), el('b', {}, v + '%'))),
        el('div', { class: 'lp-cta' }, el('span', {}, el('b', {}, 'That was one topic from Unit 3. Cambridge Stage 7 has 14 units.'), el('br'), el('span', {}, 'Carry on with topic 3.1 now – no sign-up – or create a free account to save your progress.')),
          el('div', { class: 'btnrow', style: 'margin:0' }, el('button', { type: 'button', class: 'btn gold', id: 'demoGuest', onclick: startGuest }, 'Start learning now →'), el('a', { class: 'btn onblue', href: '#signup' }, 'Sign up free'))),
        el('button', { type: 'button', class: 'lp-link', onclick: () => { Object.assign(D, demoInit()); vid = null; panel.innerHTML = ''; draw(); } }, 'Restart the demo')));
    }
    draw();

    // ---- all 14 units as small boxes ----
    m.append(el('section', { class: 'lp-units' }, el('div', { class: 'btnrow between', style: 'margin:0 0 18px' }, el('h2', { style: 'margin:0' }, 'Everything in Cambridge Stage 7'), el('button', { type: 'button', class: 'btn small', onclick: startGuest }, 'Open the course →')),
      el('div', { class: 'lp-ugrid' }, ...Core.INDEX.units.map(({ n, t, ready }) => el(ready ? 'button' : 'div', ready ? { type: 'button', class: 'card lift lp-unit', onclick: () => startGuest(n) } : { class: 'card lp-unit off', title: 'Coming soon' },
        unitIcon(n), el('span', { class: 'lp-ut' }, el('small', {}, 'UNIT ' + n), el('br'), el('b', {}, t)), ready ? el('span', { class: 'lp-free' }, 'Try free') : el('span', { class: 'lp-tag' }, 'Soon'))))));
    // ---- how it works ----
    const step = (n, cls, t, d) => el('div', { class: 'card lift lp-how' }, el('span', { class: 'lp-num ' + cls }, String(n)), el('b', {}, t), el('p', { class: 'muted', style: 'margin:0' }, d));
    m.append(el('section', { class: 'lp-hows' }, el('div', { style: 'text-align:center' }, el('small', { class: 'lp-eyebrow gold' }, 'HOW IT WORKS'), el('h2', { style: 'margin:6px 0 0' }, 'Three steps to start')),
      el('div', { class: 'lp-hgrid' }, step(1, 'b', 'Try it straight away', 'Open topic 3.1 – no account needed. Watch and practise; your progress is kept on this device.'),
        step(2, 'g', 'Sign up free in a minute', 'Your name and email, your age and school year, then your country and school. A parent’s email is optional.'),
        step(3, 'gr', 'Learn, keep your streak, pass the test', 'Lessons, practice and a Unit Test for every topic. Learn a little every day to grow your streak.')),
      el('div', { style: 'text-align:center' }, el('a', { class: 'btn gold', href: '#signup' }, 'Create a free account'))));
    m.append(faq());
  }
  function faq() {
    const qa = [['Who is Camday for?', 'Learners aged about 7–14 following Cambridge Primary or Lower Secondary Science (Stages 3 to 9) or Mathematics (Stages 3 to 9), at an international or bilingual school or studying at home.'],
      ['Do I need an account?', 'Not to try it: topic 3.1 is open to guests. A free account opens every lesson video of Unit 3 and its Core questions and saves your progress.'],
      ['Is it a subscription?', 'No. You pay once for a subject or a whole stage. The course stays open as long as you study at least once a year. After 365 days without any study it closes, and you can buy it again.'],
      ['Will my parents know how I am doing?', 'If you add a parent’s email when you sign up (it is optional), we send them a short email when you finish a unit. You can add or remove it any time in Settings.'],
      ['How are Unit Tests marked?', 'Multiple-choice, diagram and data questions are marked automatically. Written answers are marked by the Camday teaching team; you get a notification when it is done.'],
      ['Can I delete my data?', 'Yes. In Settings you can download everything we hold about you or delete your account, which removes all your learning records.']];
    return el('section', { class: 'card' }, el('h2', {}, 'Questions'), ...qa.map(([q, a]) => el('details', { class: 'faq' }, el('summary', {}, q), el('p', {}, a))));
  }

  /* ---------- sign up (3 steps, Mathspace style) / sign in ---------- */
  // ---- News: announcements + the roadmap of coming features (admins edit both in Admin → News & roadmap) ----
  async function viewNews() {
    const m = $main();
    pageHero('NEWS', 'What’s new and what’s coming', 'Announcements from the Camday team and the features we are building next. Dates are our current plan and may move.');
    const [ann, road] = await Promise.all([Backend.announcements().catch(() => []), (Backend.roadmap ? Backend.roadmap() : Promise.resolve([])).catch(() => [])]);
    const when = d => { try { return new Date(d).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }); } catch (e) { return ''; } };
    m.append(el('section', { class: 'card', id: 'newsList' }, el('h2', {}, 'Latest news'),
      ann.length ? el('div', { class: 'newslist' }, ...ann.map(a => el('article', { class: 'newsit' + (a.level === 'warn' ? ' warn' : '') }, el('small', { class: 'muted' }, when(a.created_at)), el('h3', {}, a.title), a.body ? el('p', {}, a.body) : null)))
        : el('p', { class: 'muted' }, 'No news right now – check back soon.')));
    // a timeline: what is live, what we are building now, what comes next
    const COLS = [['released', 'Released', 'Already on Camday'], ['building', 'Being built', 'What we are working on now'], ['planned', 'Planned', 'What comes next']];
    const tl = el('div', { class: 'roadmap tline', id: 'roadmap' }, ...COLS.map(([k, h, sub]) => { const items = road.filter(x => x.status === k);
      return el('section', { class: 'rmcol rm-' + k }, el('span', { class: 'rmdot', 'aria-hidden': 'true' }), el('span', { class: 'rmlab' }, h), el('h3', {}, sub),
        ...(items.length ? items.map(x => el('article', { class: 'rmit' }, el('b', {}, x.title), el('div', { class: 'rmmeta' }, x.target ? el('span', { class: 'rmwhen' }, x.target) : null, x.tag ? el('span', { class: 'rmtag' }, x.tag) : null), x.body ? el('p', {}, x.body) : null))
          : [el('p', { class: 'muted' }, 'Nothing here yet.')])); }));
    m.append(el('section', { class: 'card rmcard' }, el('span', { class: 'rmlab big' }, 'Roadmap'), el('h2', {}, 'What is live, and what comes next'), tl));
  }
  // ---- sign-up (B2C): account → about you and your school → choose ONE stage → choose a plan (one subject or the whole stage) ----
  const SCHOOL_YEARS = [['Year 1 / Kindergarten', 1], ['Year 2 / Grade 1', 2], ['Year 3 / Grade 2', 3], ['Year 4 / Grade 3', 4], ['Year 5 / Grade 4', 5], ['Year 6 / Grade 5', 6], ['Year 7 / Grade 6', 7], ['Year 8 / Grade 7', 8], ['Year 9 / Grade 8', 9], ['Year 10 / Grade 9', 9], ['Other', 0]];
  const SUBJ_NAME = k => (k >= 20 ? 'English (ESL)' : k >= 10 ? 'Mathematics' : 'Science'), SUBJ_ICON = k => (k >= 20 ? '🗣' : k >= 10 ? '📐' : '🔬');
  const priceNum = s => Number(String(s).replace(/[^\d.]/g, '')) || 0;
  const money = (n, like) => { const m = String(like).match(/^(\D*)[\d.,]+(.*)$/) || ['', '', '']; return m[1] + n.toLocaleString('en-GB') + m[2]; };
  const BUNDLE = () => (window.ATOMIC_CONFIG || {}).bundlePrice || 'US$119';
  const PAIR = () => (window.ATOMIC_CONFIG || {}).pairPrice || 'US$95';
  const priceFor = n => (n <= 0 ? '–' : n === 1 ? PRICE : n === 2 ? PAIR() : BUNDLE());   // 1 subject, 2 subjects, 3 subjects (whole stage)
  const lvName = lv => (lv <= 6 ? 'Cambridge Primary' : 'Cambridge Lower Secondary');
  function viewSignup() {
    const m = $main(); const e = errBox(); const F = UI.su = UI.su || { step: 1 };
    const card = el('section', { class: 'card narrow signup' }); m.append(el('div', { class: 'authwrap dots' }, card)); document.getElementById('wrap').classList.add('authpage');
    const dots = () => el('div', { class: 'steps', 'aria-label': `Step ${F.step} of 4` }, ...[1, 2, 3, 4].map(i => el('span', { class: i < F.step ? 'done' : i === F.step ? 'on' : '' }, String(i))));
    const next = () => { e.textContent = ''; F.step++; draw(); }, back = () => { e.textContent = ''; F.step--; draw(); };
    const open = lv => Core.subjectKeys(lv).filter(k => !Core.stageLocked(k));
    function draw() {
      card.innerHTML = '';
      if (F.step === 1) {
        const name = el('input', { type: 'text', id: 'suName', autocomplete: 'name', value: F.name || '', maxlength: 80 }), email = el('input', { type: 'email', id: 'suEmail', autocomplete: 'email', value: F.email || '' }), pw = el('input', { type: 'password', id: 'suPw', autocomplete: 'new-password', value: F.password || '' });
        card.append(dots(), el('h1', {}, 'Create your account'), el('p', { class: 'muted' }, 'It takes a minute. You can start learning straight after.'),
          el('div', { class: 'form' }, field('Your full name', name, 'Printed on your certificate. Only your first name is shown in the app.'), field('Email', email), field('Password', pw, 'At least 8 characters.'), e,
            el('button', { class: 'btn primary', type: 'button', id: 'suNext1', onclick: () => {
              if (name.value.trim().length < 2) { e.textContent = 'Please enter your name.'; return; }
              if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) { e.textContent = ERR.bad_email; return; }
              if (pw.value.length < 8) { e.textContent = ERR.weak_password; return; }
              Object.assign(F, { name: name.value.trim(), email: email.value.trim(), password: pw.value }); next(); } }, 'Next', el('span', { class: 'arr' }, ' →'))),
          el('p', { class: 'muted' }, 'Already have an account? ', el('a', { href: '#signin' }, 'Log in')));
      } else if (F.step === 2) {
        const now = new Date().getFullYear();
        const by = el('select', { id: 'suYear' }, el('option', { value: '' }, 'Choose…'), ...Array.from({ length: 13 }, (_, i) => now - 5 - i).map(y => el('option', { value: y }, `${y} (about ${now - y} years old)`)));
        const gr = el('select', { id: 'suGrade' }, el('option', { value: '' }, 'Choose…'), ...SCHOOL_YEARS.map(([y]) => el('option', { value: y }, y)));
        const school = el('input', { type: 'text', id: 'suSchool', maxlength: 120, value: F.school || '', placeholder: 'e.g. Hanoi International School', autocomplete: 'organization' });
        const town = el('input', { type: 'text', id: 'suTown', maxlength: 80, value: F.town || '', placeholder: 'optional – e.g. Hanoi, Vietnam' });
        const parent = el('input', { type: 'email', id: 'suParent', autocomplete: 'off', value: F.parentEmail || '', placeholder: 'optional' });
        by.value = F.birthYear || ''; gr.value = F.grade || '';
        card.append(dots(), el('h1', {}, 'About you and your school'), el('p', { class: 'muted' }, 'This helps us suggest the right stage. It is never shown to anyone.'),
          el('div', { class: 'form' }, field('Year of birth', by), field('School year', gr), field('Your school', school, 'Type the name of your school.'), field('Town and country', town),
            field('Parent or guardian’s email (optional)', parent, 'If you add it, we send them one short email when you finish a unit – nothing else. You can change it in Settings.'), e,
            el('div', { class: 'btnrow between' }, el('button', { class: 'btn ghost', type: 'button', onclick: back }, '← Back'),
              el('button', { class: 'btn primary', type: 'button', id: 'suNext2', onclick: () => {
                if (!by.value) { e.textContent = 'Please choose your year of birth.'; return; }
                if (!gr.value) { e.textContent = 'Please choose your school year.'; return; }
                if (school.value.trim().length < 2) { e.textContent = 'Please type the name of your school.'; return; }
                const pe = parent.value.trim();
                if (pe && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(pe)) { e.textContent = 'That parent email does not look right – check it or leave it empty.'; return; }
                if (pe && pe.toLowerCase() === F.email.toLowerCase()) { e.textContent = 'The parent email must be different from your own.'; return; }
                const sug = (SCHOOL_YEARS.find(([y]) => y === gr.value) || [0, 0])[1];
                Object.assign(F, { birthYear: Number(by.value), grade: gr.value, school: school.value.trim(), town: town.value.trim(), parentEmail: pe });
                if (!F.stage && sug && open(sug).length) F.stage = sug; next(); } }, 'Next', el('span', { class: 'arr' }, ' →')))));
      } else if (F.step === 3) {
        const sug = (SCHOOL_YEARS.find(([y]) => y === F.grade) || [0, 0])[1];
        const grid = el('div', { class: 'su-stages', role: 'radiogroup', 'aria-label': 'Stage' });
        const pick = lv => { F.stage = lv; F.plan = null; grid.querySelectorAll('.su-stage').forEach(b => { const on = Number(b.dataset.stage) === lv; b.classList.toggle('on', on); b.setAttribute('aria-checked', String(on)); }); };
        for (let lv = 1; lv <= 9; lv++) {
          const ks = open(lv), ok = ks.length > 0;
          grid.append(el('button', { type: 'button', class: 'su-stage' + (F.stage === lv ? ' on' : '') + (ok ? '' : ' off'), role: 'radio', 'aria-checked': String(F.stage === lv), 'data-stage': lv, disabled: !ok, onclick: () => pick(lv) },
            el('b', {}, `Stage ${lv}`), el('small', {}, lvName(lv).replace('Cambridge ', '')), el('small', { class: 'su-subj' }, ok ? ks.map(SUBJ_ICON).join(' ') : 'coming soon'),
            lv === sug ? el('span', { class: 'su-tag' }, 'Suggested') : null));
        }
        card.append(dots(), el('h1', {}, 'Choose your stage'), el('p', { class: 'muted' }, 'You study one stage at a time. When you have finished 80% of its lessons and Unit Tests, you get your certificate and can move on to the next stage.'),
          el('div', { class: 'form' }, grid, e, el('div', { class: 'btnrow between' }, el('button', { class: 'btn ghost', type: 'button', onclick: back }, '← Back'),
            el('button', { class: 'btn primary', type: 'button', id: 'suNext3', onclick: () => { if (!F.stage) { e.textContent = 'Please choose your stage.'; return; } next(); } }, 'Next', el('span', { class: 'arr' }, ' →')))));
      } else {
        const lv = F.stage, keys = Core.subjectKeys(lv), avail = open(lv), bundleOk = avail.length >= 2;
        // parents drag the subjects their child will study into the plan (or tap them): 1 subject, 2 subjects or the whole stage
        if (!Array.isArray(F.pick) || F.pickStage !== lv) { F.pick = []; F.pickStage = lv; }
        const isAll = () => avail.length > 1 && avail.every(k => F.pick.includes(k));
        const total = el('b', { id: 'suTotal' }), totalNote = el('small', { class: 'muted', id: 'suTotalNote' }); const terms = el('input', { type: 'checkbox', id: 'suTerms' });
        const chosen = () => avail.filter(k => F.pick.includes(k));
        const opts = el('div', { class: 'su-plans', role: 'group', 'aria-label': 'Subjects' });
        const basket = el('div', { class: 'su-basket', id: 'suBasket', 'aria-live': 'polite' });
        const set = (k, on) => { F.pick = on ? (F.pick.includes(k) ? F.pick : F.pick.concat(k)) : F.pick.filter(x => x !== k); refresh(); };
        const refresh = () => {
          opts.querySelectorAll('.su-plan').forEach(b => { const id = b.dataset.plan, on = id === 'bundle' ? isAll() : F.pick.includes(Number(id)); b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); });
          const ch = chosen(), n = ch.length;
          basket.textContent = '';
          basket.append(el('b', { class: 'su-bh' }, `Your child’s Stage ${lv} plan`),
            n ? el('div', { class: 'su-chips' }, ...ch.map(k => el('span', { class: 'su-chip', draggable: 'true', 'data-k': k, ondragstart: ev => { ev.dataTransfer.setData('text/plain', 'out:' + k); } },
              SUBJ_ICON(k) + ' ' + SUBJ_NAME(k), el('button', { type: 'button', class: 'su-x', 'aria-label': `Remove ${SUBJ_NAME(k)}`, onclick: () => set(k, false) }, '×'))))
              : el('p', { class: 'muted su-empty' }, 'Drag subjects here, or tap them.'));
          total.textContent = priceFor(n);
          totalNote.textContent = !n ? 'Choose at least one subject.' : `${n} subject${n > 1 ? 's' : ''}${isAll() && n > 2 ? ' · whole stage' : ''}${n > 1 ? ` (instead of ${money(priceNum(PRICE) * n, PRICE)})` : ''}`;
        };
        basket.addEventListener('dragover', ev => { ev.preventDefault(); basket.classList.add('over'); });
        basket.addEventListener('dragleave', () => basket.classList.remove('over'));
        basket.addEventListener('drop', ev => { ev.preventDefault(); basket.classList.remove('over'); const d = ev.dataTransfer.getData('text/plain');
          if (d === 'bundle') { F.pick = avail.slice(); refresh(); } else if (/^\d+$/.test(d) && avail.includes(Number(d))) set(Number(d), true); });
        opts.addEventListener('dragover', ev => ev.preventDefault());
        opts.addEventListener('drop', ev => { ev.preventDefault(); const d = ev.dataTransfer.getData('text/plain'); if (/^out:\d+$/.test(d)) set(Number(d.slice(4)), false); });
        const toggle = id => { if (id === 'bundle') F.pick = isAll() ? [] : avail.slice(); else { const k = Number(id); F.pick = F.pick.includes(k) ? F.pick.filter(x => x !== k) : F.pick.concat(k); } refresh(); };
        const plan = (id, icon, title, sub, price, ok) => el('button', { type: 'button', class: 'su-plan' + (ok ? '' : ' off') + (id === 'bundle' ? ' bundle' : ' subj'), 'aria-pressed': 'false', 'data-plan': id, disabled: !ok, draggable: ok ? 'true' : 'false',
            ondragstart: ev => { ev.dataTransfer.setData('text/plain', id); ev.dataTransfer.effectAllowed = 'copy'; }, onclick: () => toggle(id) },
          el('span', { class: 'su-grip', 'aria-hidden': 'true' }, '⠿'), el('span', { class: 'su-pi', 'aria-hidden': 'true' }, icon), el('span', { class: 'su-pt' }, el('b', {}, title), el('small', {}, sub)), el('b', { class: 'su-pp' }, ok ? price : 'Soon'), el('span', { class: 'su-tick', 'aria-hidden': 'true' }, '✓'));
        keys.forEach(k => opts.append(plan(String(k), SUBJ_ICON(k), `${SUBJ_NAME(k)} · Stage ${lv}`, `${lvName(lv)} ${SUBJ_NAME(k)}`, PRICE, avail.includes(k))));
        if (avail.length > 1) opts.append(plan('bundle', '⭐', `All ${avail.length} subjects`, avail.map(SUBJ_NAME).join(' + '), priceFor(avail.length), true));
        const priceList = el('p', { class: 'muted su-prices' }, `1 subject ${PRICE} · 2 subjects ${PAIR()}` + (Core.subjectKeys(lv).length > 2 ? ` · all 3 subjects ${BUNDLE()}` : ''));
        const b = el('button', { class: 'btn gold', type: 'button', id: 'suBtn', onclick: async () => {
          e.textContent = '';
          if (!chosen().length) { e.textContent = 'Please choose at least one subject.'; return; }
          if (!terms.checked) { e.textContent = 'Please agree to the Terms and the Privacy notice.'; return; }
          b.disabled = true; b.classList.add('busy'); setTimeout(() => b.classList.remove('busy'), 20000);
          const courses = chosen(), all = isAll(), amount = courses.length > 1 ? `Stage ${lv} · ${courses.length} subjects ${priceFor(courses.length)}` : PRICE;
          try {
            await Backend.signUp({ name: F.name, email: F.email, password: F.password, birthYear: F.birthYear, grade: F.grade, stage: lv, country: 'XX', schoolId: null,
              schoolOther: [F.school, F.town].filter(Boolean).join(', ').slice(0, 120), parentEmail: F.parentEmail || null });
            const hadGuest = isGuest(); UI.su = null; await Core.boot(C); st = Core.cur();
            let paid = true; try { await Core.buy(courses, amount); } catch (x) { paid = false; }
            if (paid) { try { await Core.ensureOwnStage(); } catch (x) { } C = Core.C; st = Core.cur(); }
            if (!paid) { try { await Core.ensureOwnStage(true); } catch (x) { } C = Core.C; st = Core.cur(); }
            toast(paid ? `Welcome to Camday! You are enrolled in ${all ? 'the whole of Stage ' + lv : courses.map(SUBJ_NAME).join(' and ') + ' Stage ' + lv}.` : (hadGuest ? 'Account created – your guest progress is saved! ' : 'Account created! ') + `You are on the free plan: Unit ${Core.FREE_UNIT} is open.`);
            confetti(); go('home');
          } catch (x) { e.textContent = errText(x); b.disabled = false; if (x && x.code === 'email_taken') { F.step = 1; draw(); } }
        } }, 'Create my account and enrol');
        card.append(dots(), el('h1', {}, `Stage ${lv}: choose your plan`), el('p', { class: 'muted' }, 'Drag the subjects your child will study into the plan, or tap them. The more subjects, the lower the price per subject. You can add another subject later.'),
          el('div', { class: 'form su-form4' }, priceList, el('div', { class: 'su-dnd' }, opts, basket), el('div', { class: 'ordrow su-total' }, el('span', {}, 'Total', el('br'), totalNote), total),
            el('p', { class: 'muted' }, `Pay once – no subscription. Closing the payment window keeps you on the free plan (Unit ${Core.FREE_UNIT} lessons and Core questions).`),
            PAID ? el('div', {}) : el('div', { class: 'banner info' }, el('b', {}, 'Test checkout. '), 'This is the test server: no money is taken.'),
            el('label', { class: 'check' }, terms, el('span', {}, 'I agree to the ', el('a', { href: '#terms', target: '_blank' }, 'Terms'), ' and have read the ', el('a', { href: '#privacy', target: '_blank' }, 'Privacy notice'), ' (', el('a', { href: '#privacy-kids', target: '_blank' }, 'short version'), ').')), e,
            el('div', { class: 'btnrow between' }, el('button', { class: 'btn ghost', type: 'button', onclick: back }, '← Back'), b)));
        refresh();
      }
      const f = card.querySelector('input,select'); if (f) f.focus();
    }
    draw();
  }
  function viewSignin() {
    const m = $main(); const e = errBox();
    const email = el('input', { type: 'email', id: 'siEmail', autocomplete: 'email' }), pw = el('input', { type: 'password', id: 'siPw', autocomplete: 'current-password' });
    const b = el('button', { class: 'btn primary', type: 'button', id: 'siBtn', onclick: async () => { e.textContent = ''; b.disabled = true; b.classList.add('busy');
      try { await Backend.signIn({ email: email.value, password: pw.value }); await Core.boot(C); st = Core.cur(); go('home'); } catch (x) { e.textContent = errText(x); b.disabled = false; b.classList.remove('busy'); } } }, 'Log in');
    pw.addEventListener('keydown', ev => { if (ev.key === 'Enter') b.click(); });
    document.getElementById('wrap').classList.add('authpage'); m.append(el('div', { class: 'authwrap dots' }, narrow(el('span', { class: 'eyebrow' }, 'WELCOME BACK'), el('h1', {}, 'Log in'), el('div', { class: 'form' }, field('Email', email), field('Password', pw), e, b),
      el('p', { class: 'muted' }, el('a', { href: '#forgot' }, 'Forgotten your password?'), ' · New here? ', el('a', { href: '#signup' }, 'Sign up free')))));
  }
  function viewForgot() {
    const m = $main(); const e = errBox(); const email = el('input', { type: 'email', id: 'fpEmail' });
    const b = el('button', { class: 'btn primary', type: 'button', onclick: async () => { try { await Backend.resetPassword(email.value); m.innerHTML = ''; m.append(narrow(el('h2', {}, 'Check your email'), el('p', {}, 'If an account exists for that address, we have sent a link to reset the password.'))); } catch (x) { e.textContent = errText(x); } } }, 'Send reset link');
    m.append(narrow(el('h1', {}, 'Reset your password'), el('div', { class: 'form' }, field('Email', email), e, b)));
  }

  /* ---------- student settings & privacy ---------- */
  async function viewSettings() {
    const m = $main(); await Core.refreshAccount(); const l = (Core.S.learners.find(x => x.id === st.id)) || st.learner || {};
    const msg = el('span', { class: 'muted', 'aria-live': 'polite' }); const e = errBox();
    const nick = el('input', { type: 'text', id: 'setNick', value: l.nickname || '', maxlength: 24 }), full = el('input', { type: 'text', id: 'setName', value: l.certificate_name || '', maxlength: 80 });
    const gr = el('select', { id: 'setGrade' }, el('option', { value: '' }, '—'), ...SCHOOL_YEARS.map(([y]) => el('option', { value: y }, y))); if (l.grade && !SCHOOL_YEARS.some(([y]) => y === l.grade)) gr.append(el('option', { value: l.grade }, l.grade)); gr.value = l.grade || '';
    const school = el('input', { type: 'text', id: 'setSchool', value: l.school_other || '', maxlength: 120, placeholder: 'Type the name of your school' });
    const parent = el('input', { type: 'email', id: 'setParent', value: l.parent_email || '', placeholder: 'optional' });
    const save = el('button', { class: 'btn primary', type: 'button', id: 'setSave', onclick: async () => {
      e.textContent = ''; msg.textContent = '';
      const pe = parent.value.trim(); if (pe && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(pe)) { e.textContent = 'That parent email does not look right.'; return; }
      if (nick.value.trim().length < 2) { e.textContent = ERR.bad_nickname; return; }
      try { await Backend.updateLearner(l.id, { nickname: nick.value.trim(), certificate_name: full.value.trim() || null, grade: gr.value || null, school_id: null, school_other: school.value.trim() || null, parent_email: pe || null });
        await Core.refreshAccount(); const nl = Core.S.learners.find(x => x.id === l.id); if (nl) { st.learner = nl; st.alias = nl.nickname; st.name = nl.certificate_name || nl.nickname; } QE.setTxt(msg, 'Saved ✓'); } catch (x) { e.textContent = errText(x); }
    } }, 'Save changes');
    const lb = el('input', { type: 'checkbox', id: 'setBoard' }); lb.checked = !!l.leaderboard_opt_in;
    lb.onchange = () => { if (lb.checked) modal('Show me on the leaderboard?', 'Your nickname and ranking score will be visible to other Camday learners. Nothing else is shown. You can switch this off at any time.', [{ t: 'Keep me hidden', cls: 'ghost', on: () => { lb.checked = false; } }, { t: 'Show my nickname', cls: 'primary', on: async () => { await Backend.updateLearner(l.id, { leaderboard_opt_in: true }); await Core.refreshAccount(); st.learner = Core.S.learners.find(x => x.id === l.id); } }]); else Backend.updateLearner(l.id, { leaderboard_opt_in: false }).then(async () => { await Core.refreshAccount(); st.learner = Core.S.learners.find(x => x.id === l.id); }); };
    pageHero('ACCOUNT', 'Settings', `Signed in as ${Core.S.me.user.email}`, statCard(initialChip(44), st.alias, l.grade || `Cambridge ${Core.stageLabel()} learner`));
    m.append(
      el('section', { class: 'card' }, el('h2', {}, 'Profile'), el('div', { class: 'form' }, field('Nickname', nick, LEADERBOARD ? 'Shown in the app and, if you switch it on, on the leaderboard.' : 'Shown in the app.'), field('Full name for the certificate', full), field('School year', gr), field('Your school', school))),
      el('section', { class: 'card' }, el('h2', {}, '📧 Parent or guardian'), el('div', { class: 'form' }, field('Parent or guardian’s email (optional)', parent, 'We send them one short email when you finish a unit. Leave empty to send nothing.'))),
      el('div', { class: 'btnrow' }, save, msg), e,
      !LEADERBOARD ? null : el('section', { class: 'card' }, el('h2', {}, 'Leaderboard'), el('label', { class: 'switch' }, lb, el('span', {}, el('b', {}, 'Show me on the leaderboard'), el('br'), el('small', { class: 'muted' }, 'Off by default. Only your nickname and ranking score are shown.')))),
      el('section', { class: 'card' }, el('h2', {}, 'Your data'), el('p', {}, 'Download a copy of everything we hold about you, or delete your account and all learning records.'),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn small', type: 'button', id: 'exportBtn', onclick: async () => { const d = await Backend.exportData(); const r = await Core.saveFile('atomic-data-export.json', new Blob([JSON.stringify(d, null, 2)], { type: 'application/json' })); msg3.textContent = r === 'saved' ? 'Downloaded.' : 'Could not download.'; } }, '⬇ Download my data (JSON)'),
          el('button', { class: 'btn small ghost', type: 'button', id: 'deleteBtn', onclick: () => deleteAccountFlow() }, 'Delete account…')), el('p', { class: 'muted', id: 'msg3', 'aria-live': 'polite' })));
    const msg3 = m.querySelector('#msg3');
  }
  function deleteAccountFlow() {
    const inp = el('input', { type: 'text', id: 'delConfirm', placeholder: 'DELETE MY ACCOUNT' }); const e = errBox();
    modal('Delete your account?', el('div', { class: 'form' }, el('p', {}, 'This deletes your account, all progress, tests and certificates. This cannot be undone.'), field('Type DELETE MY ACCOUNT to confirm', inp), e),
      [{ t: 'Cancel', cls: 'ghost' }, { t: 'Delete everything', cls: 'primary', on: async () => { try { await Backend.deleteAccount(inp.value.trim()); await Core.boot(C); st = null; go('home'); } catch (x) { e.textContent = errText(x); return true; } } }]);
  }

  /* ---------- plans & checkout ---------- */
  // plans: bought once (no subscription). A course closes after 365 days without study and must then be bought again.
  function viewPricing() {
    const m = $main(); const me = Core.S.me;
    const plan = (name, price, pts, cta, hl) => el('div', { class: 'card plan' + (hl ? ' cur' : '') }, hl ? el('span', { class: 'tag adv' }, 'Best value') : null, el('h3', {}, name), el('div', { class: 'price' }, price), el('ul', {}, ...pts.map(p => el('li', {}, p))), cta);
    const cta = (t, cls) => me ? el('a', { class: 'btn ' + cls, href: '#plans' }, t) : el('a', { class: 'btn ' + cls, href: '#signup' }, t);
    m.append(el('div', { style: 'text-align:center' }, el('span', { class: 'eyebrow' }, 'PLANS'), el('h1', { style: 'margin:4px 0' }, 'Pay once. Keep learning.'),
      el('p', { class: 'muted', id: 'oneTimeNote' }, 'No subscription. A course stays yours as long as you study at least once a year; after 365 days without study it closes and must be bought again.')),
      el('div', { class: 'plans' },
        plan('Free', '$0', [`Unit ${Core.FREE_UNIT} of your stage`, 'Every lesson video of that unit, with pause questions', '8 Core questions in each section', 'Learning streak and progress'], me ? el('a', { class: 'btn', href: '#home' }, 'Keep learning free') : el('a', { class: 'btn', href: '#signup' }, 'Start free')),
        plan('One subject', PRICE, ['One subject of your stage (Science, Mathematics or ESL)', 'Every unit, all practice and * Advanced questions', 'Unit Tests marked by Camday', 'Certificate'], cta('Choose a subject', 'primary')),
        plan('Whole stage', BUNDLE(), ['Every subject of your stage', `Two subjects: ${PAIR()}`, 'Everything in One subject', 'Move on to the next stage at 80 %'], cta('Choose the whole stage', 'gold'), true)),
      el('p', { class: 'muted', style: 'text-align:center' }, 'Prices in US dollars. At checkout Paddle, our reseller, shows the price in your currency including VAT/GST where it applies.'), faq());
  }

  function viewBeta() {
    const m = $main(); const me = Core.S.me;
    m.append(narrow(el('span', { class: 'eyebrow' }, 'TEST PHASE'), el('h1', {}, 'Free while we test'), el('p', {}, 'Camday is in a small private test. Every learner gets the whole Cambridge Stage 7 course – videos, practice, Unit Tests and the certificate – free of charge. No card is needed.'),
      el('p', { class: 'muted', id: 'betaNote' }, 'Paid plans will be introduced later. We will tell you by email before anything changes, and nothing will be charged without your agreement.'),
      el('div', { class: 'btnrow' }, me ? el('a', { class: 'btn primary', href: '#home' }, 'Go to learning') : el('a', { class: 'btn primary', href: '#signup' }, 'Sign up free'), el('a', { class: 'btn', href: '#help' }, 'Send feedback'))), faq());
  }

  /* ---------- help, reports ---------- */
  function viewHelp() {
    const m = $main(); const e = errBox(); const ok = el('p', { class: 'muted', 'aria-live': 'polite' });
    const kind = el('select', { id: 'helpKind' }, ...[['bug', 'Something is not working'], ['billing', 'Plans and payments'], ['other', 'Something else']].map(([v, t]) => el('option', { value: v }, t)));
    const msg = el('textarea', { rows: 5, id: 'helpMsg' });
    m.append(el('div', {}, el('span', { class: 'eyebrow' }, 'HELP CENTRE'), el('h1', { style: 'margin:4px 0' }, 'How can we help?')), faq(),
      el('section', { class: 'card' }, el('h2', {}, 'Contact us'),
        Core.S.me ? el('div', { class: 'form' }, field('Topic', kind), field('Message', msg), e, el('button', { class: 'btn primary', type: 'button', id: 'helpSend', onclick: async () => { try { await Backend.report({ kind: kind.value, message: msg.value.trim() }); msg.value = ''; ok.textContent = 'Thanks – we have your message and will reply by email.'; } catch (x) { e.textContent = errText(x); } } }, 'Send'), ok)
          : el('p', {}, 'Email ', el('b', {}, ((window.ATOMIC_CONFIG || {}).supportEmail) || 'support@example.com'), ' or ', el('a', { href: '#signin' }, 'sign in'), ' to send a message from here.')));
  }
  function reportQuestion(q) {
    const kind = el('select', {}, ...[['wrong_answer', 'The marked answer looks wrong'], ['unclear', 'The question is unclear'], ['typo', 'Spelling or typing mistake'], ['video', 'Problem with the video'], ['other', 'Something else']].map(([v, t]) => el('option', { value: v }, t)));
    const msg = el('textarea', { rows: 4, placeholder: 'What did you notice?' }); const e = errBox();
    modal('Report a problem with this question', el('div', { class: 'form' }, el('p', { class: 'muted' }, `Question ${q.id}. Our teaching team reads every report.`), field('What kind of problem?', kind), field('Details', msg), e),
      [{ t: 'Cancel', cls: 'ghost' }, { t: 'Send report', cls: 'primary', on: async () => { try { await Backend.report({ learnerId: st && st.id, unit: Core.UNIT, questionId: q.id, kind: kind.value, message: msg.value.trim() }); toast('Thanks – report sent'); } catch (x) { e.textContent = errText(x); return true; } } }]);
  }

  /* ---------- certificate verification (public) ---------- */
  function viewVerify() {
    const m = $main(); const code = el('input', { type: 'text', id: 'vfCode', placeholder: 'AE-S7-2026-XXXXXXXX' }); const out = el('div', { 'aria-live': 'polite' });
    m.append(narrow(el('h1', {}, 'Verify a certificate'), el('p', { class: 'muted' }, 'Enter the code printed on an Camday certificate.'), el('div', { class: 'form' }, field('Certificate code', code),
      el('button', { class: 'btn primary', type: 'button', id: 'vfBtn', onclick: async () => { const r = await Backend.verifyCertificate(code.value); out.innerHTML = ''; out.append(r ? el('div', { class: 'banner ok' }, `✓ Genuine: ${r.name_on_certificate} completed the Camday course for Cambridge Stage ${r.stage} Science on ${String(r.issued_at).slice(0, 10)}.`) : el('div', { class: 'banner adv' }, 'No certificate has this code.')); } }, 'Check'), out)));
  }

  /* ---------- legal (drafts – to be reviewed by a lawyer before launch) ---------- */
  function li(items) { // a string, or a run [text, ['a', route, label], text] that ends at a closing ')' item
    const out = []; let cur = null;
    items.forEach(x => { if (Array.isArray(x)) { cur.append(el('a', { href: '#' + x[1] }, x[2])); } else if (cur && x === ').') { cur.append(x); cur = null; } else { cur = el('li', {}, x); out.push(cur); } });
    return out;
  }
  function legal(title, sections) {
    const m = $main();
    m.append(el('article', { class: 'card legal' }, el('div', { class: 'banner adv' }, 'Draft for legal review – not yet in force. Version ' + ((window.ATOMIC_CONFIG || {}).legalVersion || '2026-11-draft') + '.'),
      el('h1', {}, title), ...sections.flatMap(([h, ...ps]) => [el('h2', {}, h), ...ps.map(p => Array.isArray(p) ? el('ul', {}, ...li(p)) : el('p', {}, p))])));
  }
  const viewPrivacy = () => legal('Privacy notice', [
    ['Who we are', 'Camday (“Camday”, “we”) runs the Camday Checkpoint courses. Contact: ' + (((window.ATOMIC_CONFIG || {}).supportEmail) || 'support@example.com') + '.'],
    ['Who this notice is for', 'Learners who use Camday and their parents or guardians.', ['A short version written for learners (see ', ['a', 'privacy-kids', 'For learners'], ').']],
    ['What we collect and why', ['Guests: nothing is sent to us. A guest’s progress is kept only in their own browser until they create an account.',
      'Account: name, email, password (stored hashed by our authentication provider), year of birth, school year, country and school – to run the account, check the course suits you and apply the right law.',
      'Optional parent or guardian email: used only to send one short email when the learner finishes a unit. It can be changed or removed at any time in Settings.',
      'Learning records: answers, progress, test results – to give feedback, mark tests, show progress and issue certificates.',
      'Payments (later, not during the test phase): handled by Paddle as Merchant of Record; we receive only the subscription status, not card details.']],
    ['High privacy by default', 'We follow the UK Age Appropriate Design Code (Children’s code): we collect the minimum, there is no advertising and no profiling for advertising, no geolocation and no public profile.'],
    ['Where data is stored', 'Our database and authentication run on Supabase; the website runs on Vercel; emails will be sent by an email provider such as Resend. Data may be processed outside your country; we use contractual safeguards for international transfers.'],
    ['How long we keep data', 'While the account is open. When you delete the account, all your data is deleted at once; backups are overwritten within 30 days.'],
    ['Children and consent', 'Several of our markets require a parent’s or guardian’s consent before a child’s personal data is used (for example Singapore under 13, Vietnam under 16, Malaysia, Indonesia and the Philippines under 18, Thailand for younger minors). During the test phase learners sign up themselves; before Camday is offered commercially we will add the parental-consent step each country requires. If you are a parent and want your child’s account removed, contact us and we will delete it.'],
    ['Your rights', 'Download a copy of your data or delete your account at any time from Settings. You can also ask us to correct data, object to or restrict processing, or complain to your data protection authority (UK: ICO; Singapore: PDPC; Vietnam: the Ministry of Public Security’s data protection authority).']]);
  function viewKidsPrivacy() {
    const m = $main(); const row = (i, t, d) => el('div', { class: 'card', style: 'display:flex;gap:14px;align-items:flex-start' }, el('span', { style: 'font-size:28px' }, i), el('div', {}, el('b', { class: 'lex' }, t), el('p', { style: 'margin:4px 0 0' }, d)));
    m.append(el('div', { style: 'max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:14px' }, el('span', { class: 'eyebrow' }, 'FOR LEARNERS'), el('h1', { style: 'margin:0' }, 'Your data at Camday – the short version'),
      row('🙂', 'We only ask for what we need', 'Your name, email, age, school year and school. We never ask for your address, photo or where you are.'),
      row('📝', 'We keep your answers to help you learn', 'Your answers, scores and progress let us give you hints, mark your tests and show you how you are doing.'),
      row('📧', 'Your parent’s email is up to you', 'If you add it, we only send them a short message when you finish a unit.'),
      LEADERBOARD ? row('🙈', 'You are hidden on the leaderboard', 'Nobody else sees you unless you switch it on. Even then, they only see your nickname and score.') : null,
      row('🚫', 'No adverts, no selling', 'We never show you adverts and we never sell your information to anyone.'),
      row('🗑️', 'You can delete it', 'In Settings you can download or delete everything at any time.'),
      row('💬', 'Worried about something?', 'Talk to a grown-up you trust, or contact us through Help.'),
      el('p', { class: 'muted' }, 'This is a short summary of our ', el('a', { href: '#privacy' }, 'Privacy notice'), '.')));
  }
  const viewTerms = () => legal('Terms of use', [
    ['The service', 'Camday provides online courses for Cambridge Primary and Lower Secondary learners: Science Stages 3 to 9 and Mathematics Stages 3 to 9. Courses are written by Camday and aligned to the Cambridge Primary Science (0097), Lower Secondary Science (0893), Primary Mathematics (0096) and Lower Secondary Mathematics (0862) curriculum frameworks. Camday is not affiliated with or endorsed by Cambridge University Press & Assessment.'],
    ['Who the course is for', 'The courses are designed for learners aged about 11 to 14. Anyone can try topic 3.1 of Science Stage 7 as a guest. Learners create their own free account to save progress; each course is a separate enrolment.'],
    ['Accounts', 'One account per learner. Keep your password private. If you are under the age of digital consent where you live, ask a parent or guardian before you sign up.'],
    ['Plans, trials and refunds', 'Plans renew automatically until cancelled. A free trial converts to a paid plan unless cancelled before it ends. Our order process is conducted by our online reseller Paddle.com, the Merchant of Record for all orders; Paddle provides customer service enquiries and handles returns.'],
    ['Fair use', 'Course content is for your own personal learning. Do not copy, share or resell videos, questions, tests or worksheets.'],
    ['Tests and certificates', 'Unit Tests and exams are marked automatically, including typed answers. A certificate confirms completion of an Camday course; it is not a Cambridge qualification.'],
    ['Changes and contact', 'We will tell you about important changes by email. Questions: ' + (((window.ATOMIC_CONFIG || {}).supportEmail) || 'support@example.com') + '.']]);
  const viewCookies = () => legal('Cookies and local storage', [
    ['What we use', 'Only what the site needs to work: keeping you signed in, and keeping a guest’s progress on this device until they sign up. We do not use advertising or third-party tracking cookies, so we do not show a cookie banner.'],
    ['Payments', 'When you open checkout, Paddle may set cookies needed for secure payment and fraud prevention. See Paddle’s own cookie notice.']]);

  /* ---------- staff: marking, reports, item statistics ---------- */
  async function viewStaff() {
    const m = $main(); const role = Core.S.me && Core.S.me.profile.role;
    if (!['marker', 'admin'].includes(role)) { m.append(narrow(el('h1', {}, 'Staff area'), el('p', {}, 'This area is for Camday markers and administrators.'), Backend.demo ? el('button', { class: 'btn small', type: 'button', id: 'becomeStaff', onclick: () => { Backend.demo.setRole('admin'); Core.refreshAccount().then(render); } }, 'Preview: make this account an administrator') : null)); return; }
    const tab = UI.staffTab || 'marking';
    m.append(el('h1', { style: 'margin:0' }, 'Staff'), el('div', { class: 'btnrow', role: 'tablist' }, ...[['marking', 'Marking queue'], ['reports', 'Question reports'], ['items', 'Question statistics']].map(([k, t]) => el('button', { class: 'chip' + (tab === k ? ' on' : ''), type: 'button', role: 'tab', onclick: () => { UI.staffTab = k; render(); } }, t))));
    if (tab === 'marking') {
      const q = await Backend.markingQueue();
      if (!q.length) { m.append(el('p', { class: 'muted', id: 'noPending' }, 'Nothing is waiting to be marked.')); return; }
      q.forEach(a => { const inputs = {};
        const box = el('section', { class: 'card' }, el('h3', {}, `${a.learner} · Paper ${a.form} · attempt ${a.n}`), el('small', { class: 'muted' }, 'Submitted ' + new Date(a.submitted).toLocaleString('en-GB')));
        a.items.forEach(it => { const inp = el('input', { type: 'number', min: 0, max: it.max, step: 0.5, class: 'numin s', value: it.suggest }); inputs[it.id] = inp;
          box.append(el('div', { class: 'sol' }, el('p', {}, el('b', {}, it.prompt)), el('blockquote', {}, it.answer || '(left blank)'), el('ul', {}, ...it.rubric.map(r => el('li', {}, r))), el('p', { class: 'muted' }, 'Model: ' + it.model), it.ai ? el('p', { class: 'muted' }, `AI check (${Math.round((it.ai.confidence || 0) * 100)}% sure): points ${it.ai.points.map((x, i) => (x ? '✓' : '✗') + (i + 1)).join(' ')}${it.ai.feedback ? ' — ' + it.ai.feedback : ''}`) : '', el('label', {}, `Mark (0–${it.max}; suggested${it.ai ? ' by the AI check' : ' from key words'}): `, inp))); });
        box.append(el('button', { class: 'btn primary small', type: 'button', onclick: async () => { const g = {}; for (const k in inputs) g[k] = Number(inputs[k].value); await Backend.markAttempt(a.attemptId, g); toast('Mark saved'); render(); } }, 'Save final mark'));
        m.append(box); });
    } else if (tab === 'reports') {
      const r = await Backend.reports();
      m.append(el('div', { class: 'card lbtable' }, ...(r.length ? r.map(x => el('div', { class: 'lbrow', style: 'grid-template-columns:110px 1fr 2.4fr 120px' }, el('code', {}, x.question_id || x.kind), el('span', { class: 'tag' }, x.kind.replace('_', ' ')), el('span', {}, x.message), el('span', {}, x.status === 'open' ? el('button', { class: 'btn small', type: 'button', onclick: async () => { await Backend.setReportStatus(x.id, 'fixed'); render(); } }, 'Mark fixed') : el('span', { class: 'status done' }, x.status)))) : [el('p', { class: 'muted', style: 'padding:16px 24px' }, 'No reports.')])));
    } else {
      const s = await Backend.itemStats(Core.UNIT);
      m.append(el('p', { class: 'muted' }, 'First-try correct rate from learners’ answers. Below 30% may be too hard or wrongly keyed; above 95% may be too easy.'),
        el('div', { class: 'tablewrap' }, el('table', { class: 'grid' }, el('tr', {}, el('th', {}, 'Question'), el('th', {}, 'Answers'), el('th', {}, 'Right first time'), el('th', {}, 'Flag')),
          ...(s.length ? s.map(x => el('tr', {}, el('td', {}, el('code', {}, x.question_id)), el('td', {}, String(x.attempts)), el('td', {}, x.first_try_correct + '%'), el('td', {}, Number(x.first_try_correct) < 30 ? el('span', { class: 'tag d-VH' }, 'check: hard') : Number(x.first_try_correct) > 95 ? el('span', { class: 'tag' }, 'check: easy') : ''))) : [el('tr', {}, el('td', { colspan: 4 }, 'No answers yet.'))]))));
    }
  }

  /* ---------- router ---------- */
  const TOC_ROUTES = r => r.startsWith('v-') || r.startsWith('sp-') || r.startsWith('ex-') || r.startsWith('ws-') || r.startsWith('lab-') || /^u-\d+$/.test(r) || ['map', 'result', 'remedial', 'topic', 'drill', 'cert', 'unit', 'words'].includes(r);
  const PUBLIC = { news: viewNews, home: () => viewHome(), signin: viewSignin, signup: viewSignup, forgot: viewForgot, pricing: viewPricing, help: viewHelp, privacy: viewPrivacy, 'privacy-kids': viewKidsPrivacy, terms: viewTerms, cookies: viewCookies, verify: viewVerify, challenge: viewChallenge, games: viewGames };
  const viewAdmin = window.AtomicAdmin ? window.AtomicAdmin({ modal, toast, errText: e => errText(e), $main, render: () => render() }) : null;
  const ACCOUNT = { staff: viewStaff, teacher: viewStaff, admin: () => viewAdmin && viewAdmin() };
  const LEARNER = { words: viewWords, home: viewHome, unit: viewUnit, test: viewTest, tests: viewTests, final: viewFinal, checkpoint: viewCheckpoint, level: viewLevel, result: viewResult, remedial: viewRemedial, map: viewMap, profile: viewProfile, topic: viewTopic, bank: viewBank, drill: viewDrill, board: viewBoard, cert: viewCert, settings: viewSettings, plans: viewPlans };
  const GUEST_WALL = { board: 'Sign up free to join the leaderboard', cert: 'Sign up free to earn a certificate', result: 'Sign up free to take the Unit Test', remedial: 'Sign up free to take the Unit Test', settings: 'Sign up free to get your own account' };
  let renderSeq = 0;
  // Stages 7–9 practise on normal pages: leaving a practice or experiment page with work left shows a reminder.
  let lastWork = null;
  function remindUnfinished(r) {
    const prev = lastWork; lastWork = /^(ex|lab)-\d+-\d+$/.test(r) ? r : null;
    if (!prev || prev === r || !st || !C || Focus.on || Core.IS_PRIMARY) return;
    const m = prev.match(/^(ex|lab)-(\d+)-(\d+)$/); if (Number(m[2]) !== Core.UNO) return;
    const s = Core.sec(m[2] + '.' + m[3]); if (!s || Core.secLock(st, s)) return;
    if (m[1] === 'ex') { const n = Core.reqLeft(st, s).length; if (n && Core.videoDone(st, s)) toast(`Remember to finish ${s.id}: ${n} Core question${n > 1 ? 's' : ''} left`); }
    else if (s.lab && !(((st.labs || {})[s.id] || {}).v || {}).done) toast(`Remember to finish the ${s.id} experiment`);
  }
  async function render() {
    if (labStop) { try { labStop(); } catch (e) { } labStop = null; }
    if (activeVideo) { try { activeVideo.pause(); } catch (e) { } activeVideo = null; }
    if (window.Games) Games.stop();
    clearInterval(timer); const seq = ++renderSeq;
    let r = location.hash.slice(1) || 'home';
    if (Guard.on && r !== Guard.route) { location.replace('#' + Guard.route); leave('navigate'); return; }   // Back / links are closed during an exam
    if (Focus.on && r !== Focus.route) {   // leaving an unfinished room (Back button, a link): stay, and ask first
      if (Focus.left() > 0) { history.replaceState(null, '', '#' + Focus.route); confirmLeave(r); return; }
      focusOff();
    }
    remindUnfinished(r);
    if (r === 'unit3') { location.replace('#u-3'); return; }
    // the unit is part of the address: u-4, v-4-1, ex-4-2, ws-4-3
    const um = r.match(/^u-(\d+)$/) || r.match(/^(?:v|ex|ws|lab|gm)-(\d+)-\d+$/);
    if (um && Number(um[1]) !== Core.UNO) { if (!Core.unitReady(Number(um[1]))) { location.replace('#home'); return; } try { await Core.switchUnit(Number(um[1])); } catch (e) { location.replace('#home'); return; } if (seq !== renderSeq) return; }
    C = Core.C; st = Core.cur(); if (/^u-\d+$/.test(r)) r = 'unit';
    document.body.classList.toggle('young', !!(C && C.unit && C.unit.young));
    document.body.classList.toggle('tiny', !!(C && C.unit && C.unit.tiny));   // Stages 1–2: picture lessons, questions read aloud   // Stages 3–4: bigger, simpler question cards
    if (r !== 'test' && !/^(fx|cpx|chx)-/.test(r)) UI.testOn = false;
    document.body.classList.remove('menu-open', 'toc-open');
    const me = Core.S.me; if (window.QE) QE.showIds = !!(me && me.profile && ['marker', 'admin'].includes(me.profile.role));
    if (me && me.profile && me.profile.disabled) { try { Core.flush && Core.flush(); } catch (e) { } await Backend.signOut(); await Core.boot(C); st = null; location.replace('#signin'); setTimeout(() => toast(ERR.account_disabled), 300); return; }
    const needsLearner = !!LEARNER[r] && r !== 'home' || /^(v|ex|ws|lab|gm)-/.test(r) || /^(stage|checkout|fx|fres)-\d+$/.test(r) || /^(cpx|cpr)-[A-Z]{1,2}\d$/.test(r) || /^ch[xpr]-[a-z]+-\d{2}$/.test(r);
    const freeTopic = /^(v|ex|ws|lab)-\d+-1$/.test(location.hash.slice(1)) || r === 'unit';
    if (['learners', 'add-learner', 'parent'].includes(r)) { location.replace('#home'); return; }
    if (r === 'board' && !LEADERBOARD) { location.replace('#home'); return; }   // old parent-area links
    if (!me && !st && (ACCOUNT[r] || needsLearner)) { if (freeTopic) { Core.startGuest(); st = Core.cur(); } else { location.replace('#signin'); return; } }  // a link into topic 3.1 starts a guest session
    if (!me && ACCOUNT[r]) { location.replace('#signin'); return; }
    if (me && !st && needsLearner) { location.replace('#home'); return; }
    if (me && (r === 'signin' || r === 'signup')) { location.replace('#home'); return; }
    // one stage per learner: a student studies only the courses they bought
    const plainStudent = me && st && !isGuest() && !['marker', 'admin'].includes(me.profile.role) && !Core.S.tester;
    if (plainStudent && !Core.myCourses().length && Core.levelOf(Core.STAGE) !== Core.learnerStage()) { await Core.ensureOwnStage(); C = Core.C; st = Core.cur(); }   // free plan: the learner's own stage
    if (plainStudent && Core.myCourses().length && !Core.enrolled(Core.STAGE)) { await Core.ensureOwnStage(); C = Core.C; st = Core.cur(); }
    shell({ toc: TOC_ROUTES(r) }); const m = $main();
    // a placeholder in the shape of the page if it takes a moment (removed as soon as real content arrives)
    let skel = null; const skT = setTimeout(() => { if (seq !== renderSeq || m.children.length) return; skel = Loading.skeleton(/^stage-|^(bank|board|tests|checkpoint|final|profile)$/.test(r) ? 'rows' : 'cards'); m.append(skel); }, 140);
    const mo = new MutationObserver(recs => { if (skel && recs.some(x => [...x.addedNodes].some(n => n !== skel))) { skel.remove(); skel = null; mo.disconnect(); } }); mo.observe(m, { childList: true });
    try {
      const pm = r.match(/^(stage|checkout|fx|fres)-(\d+)$/); const cpm = r.match(/^(cpx|cpr)-([A-Z]{1,2}\d)$/); const chm = r.match(/^chl-([a-z]+)$/) ? ['', 'chl', r.slice(4)] : r.match(/^(chx|chp|chr)-([a-z]+)-(\d{2})$/);
      if (r.startsWith('gm-')) await viewSecGames(secFromRoute(r)); else if (r.startsWith('v-')) viewVideo(secFromRoute(r)); else if (r.startsWith('vw-')) viewVideo(secFromRoute(r), true); else if (r.startsWith('sp-')) viewSpeak(secFromRoute(r)); else if (r.startsWith('ex-')) viewExercises(secFromRoute(r)); else if (r.startsWith('ws-')) viewWorksheet(secFromRoute(r)); else if (r.startsWith('lab-')) viewLab(secFromRoute(r));
      else if (/^courses(-\w+)?$/.test(r)) await viewCourses(r.split('-')[1]);
      else if (/^course-[a-z0-9-]+$/.test(r)) await viewCourse(r.slice(7));
      else if (cpm && st) { if (cpm[1] === 'cpx') await viewCpExam(cpm[2]); else await viewCpResult(cpm[2]); }
      else if (/^game-[a-z]+$/.test(r)) await viewGame(r.slice(5));
      else if (chm) { if (chm[1] === 'chl') await viewChList(chm[2]); else if (!st) go('signin'); else if (chm[1] === 'chx') await viewChExam(chm[2], chm[3]); else if (chm[1] === 'chp') await viewChPractice(chm[2], chm[3]); else await viewChResult(chm[2], chm[3]); }
      else if (pm && st) { if (isGuest() && pm[1] !== 'stage') m.append(guestWall('Sign up free to continue')); else if (pm[1] === 'stage') await viewStage(+pm[2]); else if (pm[1] === 'checkout') await viewCheckout(+pm[2]); else if (pm[1] === 'fx') await viewFinalExam(pm[2]); else await viewFinalResult(pm[2]); }
      else if (st && isGuest() && GUEST_WALL[r]) m.append(guestWall(GUEST_WALL[r]));
      else if (st && LEARNER[r]) await LEARNER[r](); else if (ACCOUNT[r]) await ACCOUNT[r](); else if (PUBLIC[r]) await PUBLIC[r](); else viewHome();
    } catch (e) { console.error(e); if (seq === renderSeq) m.append(el('div', { class: 'banner adv', role: 'alert' }, 'Something went wrong loading this page. ', el('button', { class: 'btn small', type: 'button', onclick: () => render() }, 'Try again'))); }
    clearTimeout(skT); mo.disconnect(); if (skel) { skel.remove(); skel = null; }
    if (seq !== renderSeq) return;
    if (st && !isGuest() && (/^stage-\d+$/.test(r) || ['home', 'bank', 'tests', 'checkpoint', 'final', 'profile', 'board'].includes(r)) && !document.getElementById('stageSwitch') && !m.querySelector('.lockcard#stageSoon')) m.prepend(stageSwitcher());
    if (r === 'admin') document.title = 'Camday – Admin'; else if (r === 'staff') document.title = 'Camday – Staff'; else document.title = `Camday – Cambridge ${Core.stageLabel()}`;
    m.focus({ preventScroll: true }); window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', render);
  if (window.Words) {
    const wk = () => 'words-stage' + Core.STAGE;
    Words.init({ stage: () => Core.STAGE,
      book: () => { const S = Core.S; if (!S.states) S.states = {}; const k = wk();
        if (!S.states[k] && S.guest) { try { S.states[k] = JSON.parse(localStorage.getItem('atomic.words.v1.' + k) || 'null'); } catch (e) { } }
        S.states[k] = S.states[k] || {}; S.states[k].words = S.states[k].words || {}; return S.states[k].words; },
      save: () => { const s0 = Core.cur(); if (!s0) return; const k = wk(), state = { words: (Core.S.states[k] || {}).words || {} };
        if (Core.S.guest) { try { localStorage.setItem('atomic.words.v1.' + k, JSON.stringify(state)); } catch (e) { } return; }
        Backend.saveProgress(s0.id, k, state).catch(() => { }); } });
    window.addEventListener('pagehide', () => Words.flush());
    window.toastWord = t => toast(t);
  }
  async function boot() {
    // paragraph answers in practice are marked on the server (AI against the mark scheme) once signed in
    if (Backend.aiMark && window.QE) QE.aiMark = (q, text) => Backend.aiMark({ unit: Core.UNIT, qid: q.id, text: String(text || '') });
    try {
      if (Backend.demo && location.search.includes('reset')) Backend.demo.reset();
      await Core.boot(); C = Core.C;
    } catch (e) { console.error(e); Loading.hideSplash(); document.getElementById('app').innerHTML = '<p style="padding:24px;font-family:sans-serif">Sorry – the course could not load. Please check your connection and reload the page.</p>'; return; }
    render().finally(() => Loading.hideSplash());
  }
  window.AtomicApp = { render, go, get st() { return st; }, UI, get C() { return C; } };
  boot();
})();
