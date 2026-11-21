/* Atomic Education — Science Stage 7. Views and routing (v3: student accounts, guest mode, server marking).
   Visual language: Atomic Cambridge Science Design System v3. */
(function () {
  const { el, esc } = QE;
  let C, st;
  const UI = { tab: {}, idx: {}, seek: null, drill: null, staffTab: 'marking', side: 'chapters', testIdx: 0, flags: {}, testOn: false, cc: true, speed: 1 };
  const $main = () => document.getElementById('main');
  const R = s => s.replace('.', '-');
  const secFromRoute = r => r.split('-').slice(1).join('.');
  const fmt = t => { t = Math.max(0, Math.round(t)); return `${Math.floor(t / 60)}:${String(t % 60).padStart(2, '0')}`; };
  const fullT = (s, t) => fmt(s.video.offset + t);
  const go = (r, opts) => { if (opts) Object.assign(UI, opts); if (location.hash.slice(1) === r) render(); else location.hash = r; };
  const svgI = (d, size = 16, stroke = 'currentColor', w = 2.2) => { const s = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); s.setAttribute('width', size); s.setAttribute('height', size); s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('aria-hidden', 'true'); s.innerHTML = `<path d="${d}" fill="none" stroke="${stroke}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>`; return s; };
  const I = { play: 'M8 5v14l11-7z', pause: 'M7 5h4v14H7z M13 5h4v14h-4z', check: 'M5 12l5 5 9-10', sheet: 'M6 3h8l4 4v14H6z M9 13h6 M9 17h6', lock: 'M6 11h12v10H6z M8 11V8a4 4 0 0 1 8 0v3', flag: 'M5 21V4 M5 4h11l-2 4 2 4H5', bulb: 'M9 18h6 M10 21h4 M12 3a6 6 0 0 0-4 10.5c1 1 1 2 1 3h6c0-1 0-2 1-3A6 6 0 0 0 12 3z', full: 'M4 9V4h5 M20 9V4h-5 M4 15v5h5 M20 15v5h-5' };
  const FLAME = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2c1 4 7 6 7 12a7 7 0 0 1-14 0c0-3 2-5 3-6 0 2 1 3 2 3 0-3-1-6 2-9z" fill="#F08A4B" stroke="#C2410C" stroke-width="1.2" stroke-linejoin="round"/></svg>';
  const STAR = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3 6.5 7 .8-5.2 4.8 1.4 7L12 17.6 5.8 21l1.4-7L2 9.3l7-.8z" fill="#F3BF69" stroke="#C48A2C" stroke-width="1.2" stroke-linejoin="round"/></svg>';
  /* topic icons from the Atomic design system (dark-blue outline + science-colour fill) */
  const IC = (function () {
    const dot = (x, y, r) => `M${x - r} ${y}a${r} ${r} 0 1 0 ${2 * r} 0a${r} ${r} 0 1 0 ${-2 * r} 0z`;
    let grid = ''; [7, 12, 17].forEach(y => [7, 12, 17].forEach(x => { grid += dot(x, y, 1.7) + ' '; }));
    return { 1: { o: 'M10 3h4 M11 3v8 M13 3v8 M9 11h6 M12 11v3 M5 21h14 M8 21a7 7 0 0 1 11-9', a: dot(16, 16.5, 2.2), c: '#F3BF69', bg: '#FFF4D6' }, 2: { o: 'M3 16 16 3l5 5L8 21z M7 12l2 2 M10 9l2 2 M13 6l2 2', a: 'M16 3l5 5-3 3-5-5z', c: '#F3BF69', bg: '#FFF4D6' }, 3: { o: 'M6 4h12a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3z M11 9h6v6h-6z', a: dot(7.5, 9, 2.2) + ' M11 9h6v6h-6z', c: '#8E6CC9', bg: '#E8F7EA' }, 4: { o: 'M12 19v-6 M12 13 6 8 M12 13l6-5', a: dot(6, 6, 2.2) + dot(18, 6, 2.2) + dot(12, 20, 2.2), c: '#3FA34D', bg: '#E8F7EA' }, 5: { o: 'M4 20c0-9 7-16 16-16 0 9-7 16-16 16z M4 20l9-9', a: 'M4 20c0-9 7-16 16-16 0 9-7 16-16 16z', c: '#BFE6C3', bg: '#E8F7EA' }, 6: { o: 'M3 3h18v18H3z', a: grid, c: '#2F6FD6', bg: '#E6EEFA' }, 7: { o: 'M12 3l8 4.5v9L12 21l-8-4.5v-9z M12 12l8-4.5 M12 12v9 M12 12 4 7.5', a: 'M12 3l8 4.5-8 4.5-8-4.5z', c: '#F3BF69', bg: '#FFF4D6' }, 8: { o: 'M6 3h12 M8 3v6l-4 9a2 2 0 0 0 2 3h12a2 2 0 0 0 2-3l-4-9V3', a: 'M5.6 14.5h12.8l1.5 3.5a1.4 1.4 0 0 1-1.3 2H5.4a1.4 1.4 0 0 1-1.3-2z', c: '#F7A8A8', bg: '#FDECEC' }, 9: { o: 'M9 3h6 M10 3v5L5 19a1.5 1.5 0 0 0 1.4 2h11.2a1.5 1.5 0 0 0 1.4-2L14 8V3', a: dot(11, 16, 1.8) + dot(14.5, 13.5, 1.3) + dot(13.5, 18, 1.1), c: '#F08A4B', bg: '#FFF1E0' }, 10: { o: 'M3 13h8v7H3z M13 16.5h8 M18 13.5l3 3-3 3', a: 'M3 13h8v7H3z', c: '#9CC0F0', bg: '#E6EEFA' }, 11: { o: 'M12 2v3 M12 19v3 M2 12h3 M19 12h3 M5 5l2 2 M17 17l2 2 M5 19l2-2 M17 7l2-2 ' + dot(12, 12, 4.5), a: dot(12, 12, 4.5), c: '#F3BF69', bg: '#FFF4D6' }, 12: { o: 'M13 2 4 14h7l-1 8 9-12h-7z', a: 'M13 2 4 14h7l-1 8 9-12h-7z', c: '#F3BF69', bg: '#FFF4D6' }, 13: { o: 'M2 20h20 M4 20l6-10h4l6 10 M10 7 9 4 M12 7V3 M14 7l1-3', a: 'M9 13.5h6L13.6 11h-3.2z', c: '#F08A4B', bg: '#FFF1E0' }, 14: { o: dot(12, 12, 5) + ' M3 15c1.5 2.5 16.5-2 18-6 M3 15c-1-2 2-4 4.5-5 M21 9c1 2-1.5 3.5-4 4.5', a: dot(12, 12, 5), c: '#CFE6FF', bg: '#E6EEFA' } };
  })();
  const MATH_IC = ['', '√', 'x²', '%', '=', '∠', '📊', '◯', '½', 'Σ', '↗', '∶', '🎲', '⇄', '▣', '📈'];
  const unitIcon = n => { if (Core.IS_MATHS || !IC[n]) return el('span', { class: 'ic mic', 'aria-hidden': 'true' }, MATH_IC[n] || String(n)); const i = IC[n]; const sp = el('span', { class: 'ic', style: `background:${i.bg}`, 'aria-hidden': 'true' }); sp.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24"><path d="${i.a}" fill="${i.c}"/><path d="${i.o}" fill="none" stroke="#013A8C" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>`; return sp; };
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
  let lastXp = null; // kept for older callers
  function toast(t) { const n = document.querySelectorAll('.toast').length; const x = el('div', { class: 'toast', role: 'status', style: `top:${84 + n * 58}px` }, t); document.body.append(x); setTimeout(() => x.remove(), 2700); }
  function xpTick() { }
  let xpAcc = 0, xpT = null;
  window.addEventListener('atomic:xp', e => {
    const d = e.detail; xpAcc += d.gain; clearTimeout(xpT);
    xpT = setTimeout(() => { if (xpAcc > 0) { const t = el('div', { class: 'xptoast', role: 'status' }, `+${xpAcc} XP`); document.body.append(t); setTimeout(() => t.remove(), 1600); } xpAcc = 0;
      const p = document.getElementById('levelPill'); if (p) { const li = Core.levelInfo(); p.querySelector('b').textContent = 'Lv ' + li.level; p.querySelector('.lvbar i').style.width = li.pct + '%'; } }, 500);
    if (d.levelUp) setTimeout(() => { confetti(); const t = el('div', { class: 'lvtoast', role: 'status' }, el('b', {}, `⭐ Level ${d.level}!`), el('span', {}, d.level >= TestRules.FINAL_LEVEL ? 'The end-of-year exams are open to you.' : `End-of-year exams open at level ${TestRules.FINAL_LEVEL}.`)); document.body.append(t); setTimeout(() => t.remove(), 4200); }, 600);
  });
  function initialChip(size) { return el('span', { class: 'ini', style: `width:${size}px;height:${size}px;font-size:${Math.round(size * .42)}px` }, ((st && st.alias) || '?').slice(0, 1).toUpperCase()); }
  const isGuest = () => !!Core.S.guest;
  function startGuest(n) { n = typeof n === 'number' ? n : 3; if (!Core.S.me && !Core.cur()) toast('Welcome! You are learning as a guest.'); go(`v-${n}-1`); }
  function guestWall(title) {
    return el('section', { class: 'card lockcard', id: 'guestWall' }, el('h2', {}, '✨ ' + title), el('p', {}, 'Create a free account to unlock every topic, take the Unit Test and join the leaderboard. What you have done as a guest comes with you.'),
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
    const area = r.startsWith('v-') || r.startsWith('ex-') || r.startsWith('ws-') || /^u-\d+$/.test(r) || /^stage-\d+$/.test(r) || /^checkout-\d+$/.test(r) || r === 'map' || r === 'level' ? 'course' : r === 'bank' || r === 'topic' || r === 'drill' ? 'bank' : r === 'test' || r === 'tests' || r === 'result' || r === 'remedial' || r === 'final' || /^f(x|res)-\d+$/.test(r) ? 'test' : r === 'profile' || r === 'cert' ? 'profile' : r === 'board' ? 'board' : r === 'home' ? 'home' : r;
    const right = el('span', { class: 'topright' });
    let nav;
    if (st) {
      const sk = Core.streak(st);
      const s = el('a', { class: 'pill streak', href: isGuest() ? '#home' : '#profile', title: `${sk}-day streak`, 'aria-label': `${sk}-day streak` }); s.innerHTML = FLAME; s.append(String(sk));
      const li = Core.levelInfo();
      const lv = el('a', { class: 'pill lvl', href: '#profile', id: 'levelPill', title: `Level ${li.level} · ${li.xp} XP (${TestRules.xpForLevel(li.level + 1) - li.xp} XP to level ${li.level + 1})`, 'aria-label': `Level ${li.level}, ${li.xp} XP` },
        el('b', {}, 'Lv ' + li.level), el('span', { class: 'lvbar' }, el('i', { style: `width:${li.pct}%` })));
      if (isGuest()) right.append(s, lv, el('a', { class: 'btn small ghost', href: '#signin', id: 'signInLink' }, 'Log in'), el('a', { class: 'btn small gold', href: '#signup', id: 'signUpLink' }, 'Sign up free'));
      else {
        const menu = el('div', { class: 'usermenu', hidden: true, id: 'userMenu' }, el('b', {}, st.name), el('a', { href: '#profile' }, 'My progress'), el('a', { href: '#settings', id: 'settingsLink' }, 'Settings'),
          ['marker', 'admin'].includes(me.profile.role) ? el('a', { href: '#staff' }, 'Staff') : null,
          el('button', { type: 'button', id: 'signOut', onclick: async () => { Core.flush(); await Backend.signOut(); await Core.boot(C); st = null; go('home'); } }, 'Sign out'));
        const av = el('button', { class: 'namechip', type: 'button', id: 'whoBtn', 'aria-label': 'Account menu', 'aria-haspopup': 'true', onclick: ev => { ev.stopPropagation(); menu.hidden = !menu.hidden; } }, initialChip(34), el('span', {}, st.alias));
        document.addEventListener('click', () => { menu.hidden = true; }, { once: true });
        right.append(s, lv, bell(), el('span', { class: 'userwrap' }, av, menu));
      }
      nav = [navLink('home', 'Dashboard', area === 'home'), navLink('u-' + Core.UNO, 'Course', area === 'course'), navLink('bank', 'Question Bank', area === 'bank'), navLink('tests', 'Tests & exams', area === 'test'), navLink('profile', 'Progress', area === 'profile'), navLink('board', 'Leaderboard', area === 'board')];
    } else if (me) {
      right.append(bell(), el('button', { class: 'btn small', type: 'button', id: 'signOut', onclick: async () => { await Backend.signOut(); await Core.boot(C); go('home'); } }, 'Sign out'));
      nav = [navLink('home', 'Home', area === 'home'), navLink('help', 'Help', area === 'help')];
      if (['marker', 'admin'].includes(me.profile.role)) nav.push(navLink('staff', 'Staff', area === 'staff'));
    } else {
      right.append(el('a', { class: 'btn small ghost', href: '#signin', id: 'signInLink' }, 'Log in'), el('a', { class: 'btn small gold', href: '#signup', id: 'signUpLink' }, 'Sign up free'));
      nav = [navLink('home', 'Home', area === 'home'), navLink('pricing', Core.BILLING_OFF ? 'Free test' : 'Pricing', area === 'pricing'), navLink('help', 'Help', area === 'help'), navLink('verify', 'Verify a certificate', area === 'verify')];
    }
    const header = el('header', { class: 'top' }, el('div', { class: 'top-in' },
      el('button', { class: 'menu-btn', type: 'button', 'aria-label': 'Menu', onclick: () => document.body.classList.toggle('menu-open') }, '☰'),
      el('a', { href: '#home', class: 'brand' }, el('img', { src: 'atomic_logo.png', alt: 'Atomic — home' })),
      el('nav', { class: 'mainnav', 'aria-label': 'Main' }, ...nav), right));
    const ENV = (window.ATOMIC_CONFIG || {}).env;
    const demoBar = Backend.mode === 'demo' ? el('div', { class: 'demobar', role: 'note' }, 'Preview mode: accounts, payments and marking are simulated and stored only in this browser.')
      : ENV === 'test' ? el('div', { class: 'demobar test', role: 'note', id: 'envBar' }, 'TEST environment – for trying the course only. Data may be reset at any time.') : null;
    const sub = el('div', { id: 'sub' });
    const side = el('aside', { class: 'toc', 'aria-label': 'Course contents' }); if (st && opts.toc) side.append(toc());
    const main = el('div', { class: 'content', id: 'main', tabindex: '-1' });
    const wrap = el('div', { class: 'wrap' + (opts.toc && st ? '' : ' nosidebar'), id: 'wrap' }, el('div', { class: 'layout' }, side, main));
    const foot = el('footer', { class: 'foot' }, el('div', { class: 'in' }, el('img', { src: 'atomic_logo.png', alt: 'Atomic — Quality Learning, Brighter Future.' }),
      el('nav', { class: 'footnav', 'aria-label': 'Legal and help' }, el('a', { href: '#privacy' }, 'Privacy'), el('a', { href: '#terms' }, 'Terms'), el('a', { href: '#cookies' }, 'Cookies'), el('a', { href: '#help' }, 'Help & contact'), el('a', { href: '#verify' }, 'Verify a certificate')),
      el('span', { class: 'tag2' }, el('b', {}, 'ATOMIC EDUCATION'), ' ✦ Quality Learning, Brighter Future. · Written by the Atomic teaching team'),
      el('p', { class: 'muted disclaimer' }, 'Atomic courses are written by Atomic Education and aligned to Cambridge curriculum frameworks (Lower Secondary Science 0893, Mathematics 0862). Checkpoint-format papers are written by Atomic – they are not Cambridge papers. Atomic is not affiliated with or endorsed by Cambridge University Press & Assessment.')));
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
      else sn.append(link('v-' + R(s.id), s.lesson ? 'Read' : 'Watch', vd), link('ex-' + R(s.id), `Practise · ${s.req.length - rl}/${s.req.length} Core`, rl === 0), link('ws-' + R(s.id), 'Worksheet', (ss.ws || []).includes(s.id)));
    });
    const passed = !!(st.results || {})[Core.unitId(n)];
    sn.append(el('a', { href: here ? '#test' : '#u-' + n, class: route === 'test' && here ? 'on' : '', onclick: here ? null : e => { e.preventDefault(); Core.switchUnit(n).then(() => go('test')); } }, el('span', { class: 'st' + (passed ? ' ok' : '') }, passed ? '✓' : '★'), `Unit Test ${n} · 45 min`));
    sn.append(el('a', { href: here ? '#map' : '#u-' + n, onclick: here ? null : e => { e.preventDefault(); Core.switchUnit(n).then(() => go('map')); } }, el('span', { class: 'st' }, '◎'), 'Concept map'));
    return sn;
  }
  function toc() {
    const route = location.hash.slice(1); const wrap = el('div', { style: 'display:flex;flex-direction:column;gap:12px' });
    UI.tocOpen = UI.tocOpen || {}; if (UI.tocUnit !== Core.UNO) { UI.tocOpen[Core.UNO] = true; UI.tocUnit = Core.UNO; }
    wrap.append(el('div', { class: 'card lvl subjlist' }, el('span', { class: 'h' }, 'SUBJECTS'),
      el('a', { class: 'it' + (Core.IS_MATHS ? '' : ' on'), href: '#courses-science' }, el('span', {}, '🔬 Science'), el('small', { class: 'sl' }, 'Lower Secondary')),
      el('a', { class: 'it' + (Core.IS_MATHS ? ' on' : ''), href: '#courses-maths', id: 'tocMaths' }, el('span', {}, '📐 Mathematics'), el('small', { class: 'sl' }, 'Stage 9')),
      el('a', { class: 'it', href: '#courses', style: 'font-size:13.5px' }, 'IGCSE & AS / A Level →')));
    wrap.append(el('div', { class: 'card lvl stagelist', role: 'group', 'aria-label': 'Your courses' }, el('span', { class: 'h' }, 'YOUR COURSES'),
      ...[7, 8, 9, 19].map(g => { const mine = g === Core.STAGE, en = mine || Core.enrolled(g), n = g >= 10 ? 15 : 14;
        return el('a', { class: 'it' + (mine ? ' on' : ''), href: '#stage-' + g, title: mine ? 'Open now' : en ? 'Enrolled – open this course' : 'Enrol to open' },
          el('span', {}, el('b', { class: 'cam' }, 'Cambridge'), ' ' + (g >= 10 ? '📐 Maths Stage ' + (g - 10) : 'Stage ' + g)), el('small', { class: 'sl' }, en ? Math.round(Object.keys((st && st.results) || {}).filter(k => k.startsWith(`stage${g}-unit`)).length / n * 100) + '%' : 'Enrol →')); })));
    const tot = Core.totalSeconds();
    wrap.append(el('div', { class: 'card tochrs' }, el('small', {}, `CAMBRIDGE ${Core.stageName(Core.STAGE).toUpperCase()} COURSE`), el('b', {}, `≈ ${estH(Core.INDEX.est || 0)} of learning`), el('small', { class: 'muted' }, `You have studied ${hrs(tot)}`)));
    const units = el('div', { class: 'units' });
    Core.INDEX.units.forEach(u => {
      const us = Core.unitStatus(st, u.n), open = !!UI.tocOpen[u.n], here = u.n === Core.UNO;
      if (us === 'soon') { units.append(el('div', { class: 'unit', title: 'Coming soon' }, unitIcon(u.n), el('span', {}, `${u.n}. ${u.t}`), el('span', { class: 'lk' }, svgI(I.lock, 14, '#8B98AB', 2)))); return; }
      const box = el('div', { class: 'unitbox' + (open ? ' open' : '') });
      const head = el('button', { type: 'button', class: 'unit' + (here ? ' on' : ''), 'aria-expanded': String(open), onclick: () => { UI.tocOpen[u.n] = !open; refreshToc(); } },
        unitIcon(u.n), el('span', {}, `${u.n}. ${u.t}`), us === 'passed' ? el('span', { class: 'lk', style: 'color:#1E8E4E;font-weight:800' }, '✓') : null, el('span', { class: 'chev', 'aria-hidden': 'true' }, open ? '▾' : '▸'));
      box.append(head);
      if (open) {
        const content = here ? C : Core.cached(u.n);
        box.append(el('div', { class: 'unitmeta' }, el('a', { href: '#u-' + u.n }, 'Unit overview'), el('small', { class: 'muted' }, `≈ ${estH(u.est || 0)} · you ${hrs(Core.unitSeconds(u.n))}`)));
        if (content) box.append(unitSecNav(u.n, content, Core.S.states[Core.unitId(u.n)], route));
        else { box.append(el('p', { class: 'muted', style: 'margin:4px 8px;font-size:13px' }, 'Loading…')); Core.peekUnit(u.n).then(refreshToc).catch(() => { }); }
      }
      units.append(box);
    });
    wrap.append(units, el('div', { class: 'card tocfoot' }, el('a', { href: '#tests' }, '📝 Tests & exams'), el('a', { href: '#final' }, '🏁 End-of-year exams'), el('a', { href: '#checkpoint' }, '🏛 Checkpoint exam room'), el('a', { href: '#bank' }, '🗂 Question Bank'), el('a', { href: '#cert' }, '🎓 Certificate')));
    return wrap;
  }
  function refreshToc() { const t = document.querySelector('.toc'); if (t && st && t.childElementCount) { t.innerHTML = ''; t.append(toc()); } }
  function goNext(nx) { go(nx.route, nx.tab ? { tab: { ...UI.tab, [nx.route]: nx.tab }, idx: { ...UI.idx, [nx.route + nx.tab]: nx.idx } } : null); }
  /* where am I / what remains / next button (shown on every learning screen) */
  // dotted page header shared by every student page (the "Home 01" look)
  function pageHero(eyebrow, title, sub, side) {
    const w = document.getElementById('wrap'); w.classList.add('landing');
    w.before(el('section', { class: 'phero dots' }, el('div', { class: 'phero-in' }, el('div', { class: 'phero-txt' }, el('span', { class: 'eyebrow' }, eyebrow), el('h1', {}, title), sub ? el('p', {}, sub) : null), side ? el('div', { class: 'phero-side' }, ...[].concat(side)) : null)));
  }
  const statCard = (icon, big, small, href) => el(href ? 'a' : 'div', { class: 'card dstat', href: href || null }, icon, el('span', {}, el('b', {}, big), el('br'), el('small', {}, small)));
  const ringIcon = pct => el('span', { class: 'dring', style: `background:conic-gradient(var(--blue) 0 ${pct}%, #E3EBF5 0)` }, el('i', {}, pct + '%'));
  const flameIcon = () => el('span', { class: 'bob', html: '<svg width="34" height="34" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3c1 4 6 6 6 11a6 6 0 0 1-12 0c0-3 2-5 3-6 0 2 1 3 2 3 0-3-1-5 1-8z" fill="#F3BF69" stroke="#0149AF" stroke-width="1.5" stroke-linejoin="round"/></svg>' });
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
        el('h1', {}, isGuest() ? 'Welcome to Atomic ' : `${greet}, ${st.alias} `, el('span', { class: 'wobble', style: 'display:inline-block;color:var(--gold)' }, '✦')),
        el('p', {}, started ? `You are on ${cur.id} ${cur.title} — next: ${nx.label.charAt(0).toLowerCase() + nx.label.slice(1)}.` : `Start with Unit ${Core.UNO}: ${C.unit.title} – topic ${C.sections[0] ? C.sections[0].id : '3.1'}. ${C.sections[0] && C.sections[0].lesson ? 'Read the lesson' : 'Watch the lesson'}, then practise.`)),
      el('div', { class: 'dstats' },
        el('a', { class: 'card dstat', href: '#profile', id: 'streakCard' }, el('span', { class: 'bob', html: '<svg width="34" height="34" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3c1 4 6 6 6 11a6 6 0 0 1-12 0c0-3 2-5 3-6 0 2 1 3 2 3 0-3-1-5 1-8z" fill="#F3BF69" stroke="#0149AF" stroke-width="1.5" stroke-linejoin="round"/></svg>' }),
          el('span', {}, el('b', {}, `${sk} day${sk === 1 ? '' : 's'}`), el('br'), el('small', {}, 'learning streak'))),
        el('div', { class: 'card dstat' }, el('span', { class: 'dring', style: `background:conic-gradient(var(--blue) 0 ${pct}%, #E3EBF5 0)` }, el('i', {}, pct + '%')),
          el('span', {}, el('b', {}, `${doneQ} / ${allQ}`), el('br'), el('small', {}, `Unit ${Core.UNO} questions done`))),
        el('a', { class: 'card dstat', href: '#profile', id: 'levelCard' }, el('span', { class: 'dring', style: `background:conic-gradient(var(--gold) 0 ${Core.levelInfo().pct}%, #E3EBF5 0)` }, el('i', {}, 'Lv' + Core.levelInfo().level)),
          el('span', {}, el('b', {}, `${Core.levelInfo().xp} XP`), el('br'), el('small', {}, `${TestRules.xpForLevel(Core.levelInfo().level + 1) - Core.levelInfo().xp} XP to level ${Core.levelInfo().level + 1}`))),
        el('a', { class: 'card dstat', href: `#stage-${Core.STAGE}`, id: 'hoursCard' }, el('span', { class: 'bob', style: 'font-size:30px' }, '⏱'),
          el('span', {}, el('b', {}, hrs(Core.totalSeconds())), el('br'), el('small', {}, `studied of ≈ ${estH(Core.INDEX.est || 0)} course`)))))));
    if (isGuest()) m.append(el('div', { class: 'banner info', id: 'guestBanner' }, el('b', {}, 'You are learning as a guest. '), 'Your progress is kept on this device only and topic 3.1 is open. Sign up free to save it and unlock every topic.', el('a', { class: 'btn small gold', href: '#signup' }, 'Sign up free')));
    else if (!Core.S.sub.active) m.append(el('div', { class: 'banner info', id: 'freeBanner' }, el('b', {}, 'Free plan: '), `the first topic of every unit is open. A Cambridge ${Core.stageName(Core.STAGE)} plan unlocks all topics and the Unit Test.`, el('a', { class: 'btn small gold', href: '#pricing' }, 'See plans')));
    if (Backend.mode === 'demo' && !isGuest()) m.append(el('div', { class: 'banner adv' }, el('b', {}, 'Trying the preview? '), 'Use the tester tools on the Progress page to unlock sections instantly.', el('a', { class: 'btn small', href: '#profile' }, 'Open tester tools')));
    const left = el('div', { class: 'dmain' }), aside = el('aside', { class: 'daside' });
    m.append(el('div', { class: 'dgrid' }, left, aside));
    // continue card
    const thumb = cur.lesson ? el('div', { class: 'dthumb lessonthumb', 'aria-hidden': 'true' }, el('span', { class: 'lp-play pulse' }, '📖')) : el('div', { class: 'dthumb', style: `background-image:url(${cur.video.src.replace('.mp4', '_poster.jpg')})` }, el('span', { class: 'lp-play pulse', 'aria-hidden': 'true' }, svgI(I.play, 28, '#1C2A3A', 2.6)));
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
    sug.append(sRow('o wobble', '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#9A4A00" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z M14 3v4h4 M9 13h6 M9 17h6"/></svg>',
      `Worksheet ${cur.id} · ${cur.title}`, 'Printable A4 worksheet with Core and practice questions', el('a', { class: 'btn small', href: '#ws-' + R(cur.id) }, 'Open')));
    sug.append(sRow('b pulse', '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#0149AF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a9 9 0 1 0 0 18a9 9 0 1 0 0-18z M12 7v5l3 2"/></svg>',
      wl.length ? 'Redo the questions you found tricky' : 'Revise by learning objective', wl.length ? `${wl.length} question${wl.length === 1 ? '' : 's'} you got wrong before` : 'Pick an objective and practise it',
      el('button', { class: 'btn primary small', type: 'button', id: 'tileWrong', onclick: () => wl.length ? startDrill('Redo wrong answers', wl, 'wrong') : go('topic') }, 'Start', el('span', { class: 'arr' }, ' →'))));
    left.append(sug);
    // aside: unit test card
    const ts = Core.testState(st), totalReq = C.sections.reduce((a, s) => a + 8 - Core.reqLeft(st, s).length, 0);
    aside.append(el('section', { class: 'dtest' }, el('div', { class: 'blob drift', 'aria-hidden': 'true' }),
      el('div', { class: 'dtest-h' }, el('span', { class: 'wobble', html: '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#F3BF69" stroke-width="2"><path d="M6 11h12v10H6z M8 11V8a4 4 0 0 1 8 0v3"/></svg>' }), el('b', {}, `Unit Test ${Core.UNO}`)),
      el('p', {}, ts.state === 'passed' ? 'Passed — well done! Your first-pass score counts towards the leaderboard.' : Core.unitOpen(Core.UNIT) ? `Open now · ${TestRules.UNIT_MINUTES} minutes in the exam room · pass above 70%.` : `Unlocks when you finish every ${C.sections[0] && C.sections[0].lesson ? 'lesson' : 'video'} and Core question in this unit · ${TestRules.UNIT_MINUTES} minutes · pass above 70%.`),
      el('div', { class: 'dsegs' }, ...C.sections.map(s => el('span', { class: Core.secDone(st, s) ? 'on' : (8 - Core.reqLeft(st, s).length) ? 'half' : '' }))),
      el('small', {}, `Core questions: ${totalReq} of ${C.sections.length * 8}`),
      el('a', { class: 'btn gold', href: isGuest() ? '#signup' : ts.state === 'passed' ? '#result' : '#tests', id: 'dashTest' }, isGuest() ? 'Sign up to take the test' : ts.state === 'passed' ? 'See my result' : ts.state === 'ready' ? 'Start the test' : 'Preview the test', el('span', { class: 'arr' }, ' →'))));
    // aside: leaderboard
    const lb = el('section', { class: 'card dside' }, el('div', { class: 'dth' }, el('b', { class: 'lex' }, 'Leaderboard'), el('span', { class: 'bob', html: '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#935A00" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8 M12 17v4 M7 4h10v5a5 5 0 0 1-10 0z M7 6H4a3 3 0 0 0 3 4 M17 6h3a3 3 0 0 1-3 4"/></svg>' })));
    const lbBody = el('div', { class: 'dlb' }, el('p', { class: 'muted', style: 'margin:0' }, 'Loading…')); lb.append(lbBody, el('a', { class: 'ul', href: '#board' }, 'Full leaderboard →'));
    aside.append(lb);
    if (!isGuest()) Backend.leaderboard(7).then(rows => { rows = (rows || []).filter(r => r.score != null).map(r => ({ alias: r.nickname, score: Number(r.score), me: !!r.is_mine })); Core.competitionRank(rows); lbBody.innerHTML = '';
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
    aside.append(el('section', { class: 'dknow' }, el('span', { class: 'pulse', html: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#013A8C" stroke-width="2" stroke-linecap="round"><path d="M9 18h6 M10 21h4 M12 3a6 6 0 0 0-4 10.5c1 1 1 2 1 3h6c0-1 0-2 1-3A6 6 0 0 0 12 3z"/></svg>' }),
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
    const box = el('div', { class: 'path4', style: 'display:flex;flex-direction:column;gap:16px' });
    C.sections.forEach(s => {
      const lock = Core.secLock(st, s), done = Core.secDone(st, s), vd = Core.videoDone(st, s), vs = Core.vstate(st, s.id);
      const reqDone = 8 - Core.reqLeft(st, s).length;
      const pracDone = s.req.concat(s.prac, s.adv).filter(q => (st.items[q.id] || {}).done).length;
      const ansStops = s.stops.filter(x => Core.stopDone(st, s.id, x)).length;
      const started = vd || ansStops || reqDone || pracDone;
      const state = lock ? 'lock' : done ? 'done' : started ? 'go' : 'new';
      const tile = (cls, ic, name, sub, href, locked, extra) => el('a', { class: 'u4tile ' + cls, href: locked ? null : href, 'aria-disabled': locked ? 'true' : null, style: locked ? 'opacity:.55;pointer-events:none' : null }, el('i', {}, ic), el('span', {}, el('b', {}, name), el('small', {}, sub), extra || null));
      const vlen = s.lesson ? `about ${Math.max(5, Math.round(s.video.dur / 60))} min · ${s.stops.length} check questions` : `${fmt(s.video.dur)} · ${s.stops.length} pause questions`;
      const tiles = el('div', { class: 'u4tiles' },
        tile(vd ? 'ok' : ansStops ? 'go' : '', s.lesson ? '📖' : '▶', s.lesson ? 'Read the lesson' : 'Watch', vd ? vlen + ' ✓' : ansStops ? `${ansStops} of ${s.stops.length} pauses · ${fmt(vs.pos || 0)}` : vlen, '#v-' + R(s.id), !!lock),
        tile(reqDone === 8 ? 'ok' : reqDone || pracDone ? 'go' : '', reqDone === 8 ? '✓' : '✎', 'Practise', `${pracDone}/30 · ${reqDone}/8 Core`, '#ex-' + R(s.id), !!lock || !vd, reqDone && reqDone < 8 ? el('span', { class: 'u4mini' }, el('i', { style: `width:${reqDone / 8 * 100}%` })) : null),
        tile(st.ws.includes(s.id) ? 'ok' : '', '🖨', 'Worksheet', st.ws.includes(s.id) ? 'Printed' : 'Print only', '#ws-' + R(s.id), !!lock));
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
      : ts.state === 'paywall' ? el('a', { class: 'btn gold', href: '#pricing' }, `Unlock with a Cambridge ${Core.stageName(Core.STAGE)} plan`)
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
    const meta = Core.INDEX.units.find(u => u.n === Core.UNO) || {}; const art = window.UnitArt ? UnitArt(Core.STAGE === 7 ? Core.UNO : 0, meta.strand) : { svg: '', tag: '' };
    const nobj = Object.keys(C.objectives).length, sec = Object.keys(C.objectives).filter(objSecure).length, pct = unitPct();
    const studied = Core.unitSeconds(Core.UNO);
    const crumbs4 = el('nav', { class: 'u4crumbs', 'aria-label': 'Breadcrumb' }, el('a', { href: '#home' }, 'Dashboard'), el('span', {}, '›'), el('a', { href: '#level' }, 'Cambridge Lower Secondary'), el('span', {}, '›'),
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
        Core.unitOpen(Core.UNIT) ? el('span', { class: 'opentag', style: 'margin-top:10px;display:inline-block' }, 'All topics open (test phase)') : null),
      el('div', { class: 'u4art', 'aria-hidden': 'true' }, el('div', { class: 'lens2', html: `<svg viewBox="0 0 380 380">${art.svg}</svg>` }), el('span', { class: 'tag' }, art.tag),
        el('div', { class: 'float' }, el('i', {}, Core.passed(st) ? '🏆' : '▶'), el('div', {}, el('b', {}, Core.passed(st) ? 'Unit passed' : 'Next up'), nx.label)))));
    document.getElementById('wrap').before(heroS);
    m.append(tocBtn(), el('div', { class: 'u4head' }, el('div', {}, el('p', { class: 'eyebrow', style: 'margin:0' }, `Cambridge ${Core.stageName(Core.STAGE)} · Unit ${Core.UNO}`), el('h2', {}, 'Your learning path')),
      el('div', { class: 'u4steps' }, el('span', {}, '1 Watch'), el('span', {}, '2 Practise'), el('span', {}, '3 Worksheet'), el('span', {}, '4 Unit Test'))), learningPath(), examBlock());
    m.append(el('div', { class: 'u4two' },
      el('section', { class: 'card' }, el('h2', { style: 'margin:0;font-size:22px' }, 'What you will learn'), el('span', { class: 'muted' }, `${sec} of ${nobj} secure`),
        el('ul', { class: 'u4objs objs' }, ...Object.entries(C.objectives).map(([k, o]) => el('li', { class: objSecure(k) ? 'ok' : '' }, o.t)))),
      el('section', { class: 'card' }, el('h2', { style: 'margin:0;font-size:22px' }, 'Concept map'), el('span', { class: 'muted' }, C.sections[0] && C.sections[0].lesson ? 'Tap a box to see its lesson and questions' : 'Tap a box to see its video and questions'),
        el('div', { class: 'u4map' }, mindmapSvg(false)), el('a', { class: 'btn small', href: '#map' }, 'Open the interactive map', el('span', { class: 'arr' }, ' →')))));
  }
  /* ---------- lesson: video with pause questions ---------- */
  let activeVideo = null;
  function viewVideo(sid) {
    const s = Core.sec(sid), m = $main(); if (!s) return go('home');
    if (s.lesson) return viewLesson(sid);
    const lock = Core.secLock(st, s);
    subbar('', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}: ${C.unit.title}`), el('span', { class: 'sep' }), el('span', { class: 'ttl' }, `Lesson ${s.id} · ${s.title}`));
    if (lock) { m.append(bar(`Section ${s.id} · Video`), lockScreen(`Section ${s.id} is locked`, lock.reason, [lock])); return; }
    const xp0 = Core.xp(st); const gchip = el('span', { class: 'gchip', html: FLAME + ` ${Core.streak(st)}-day streak` });
    document.querySelector('#sub .subbar-in').append(gchip);
    const bumpXp = () => { const e = document.getElementById('lessonXp'); if (e) e.textContent = Core.xp(st) - xp0; xpTick(); };
    st.last = { route: 'v-' + R(sid) }; Core.persist();
    const vs = Core.vstate(st, sid); const review = () => Core.videoDone(st, s);
    const v = el('video', { playsinline: true, preload: 'auto', 'aria-label': `Lesson ${s.id} video` }); activeVideo = v;
    v.addEventListener('play', () => { if (!v._started) { v._started = true; Backend.track('video_start', { learner: st.id, unit: Core.UNIT, sec: sid }); } });
    const player = el('div', { class: 'player' }, v);
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
    const lessonMain = el('section', { class: 'main' }, player, ctrl, panel, capP);
    // side panel: chapters / transcript / notes
    const tabsBox = el('div', { class: 'tabs', role: 'tablist', 'aria-label': 'Lesson panel' });
    const sideBody = el('div', { class: 'card', style: 'padding:14px' });
    const side = el('aside', { class: 'side' }, tabsBox, sideBody,
      el('div', { class: 'card', style: 'padding:18px 20px' }, el('b', { class: 'lex' }, 'This lesson\'s objectives'), el('ul', { style: 'margin:6px 0 0;padding-left:18px;font-size:15px' }, ...s.objs.map(o => el('li', {}, C.objectives[o].t)))),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn small', href: '#map' }, '🧠 Mind map'), el('a', { class: 'btn small', href: '#ws-' + R(sid) }, '📄 Worksheet')),
      el('div', { class: 'goal' }, el('span', { class: 'gi' }, svgI(I.bulb, 16, '#1C2A3A', 2)), el('span', {}, el('b', {}, 'Daily goal: '), `this video lasts ${fmt(s.video.dur)} with ${s.stops.length} pause questions – finish it to keep your streak going.`)));
    m.append(bar(`Unit ${Core.UNO} › ${s.id} › Video`), tocBtn(), el('div', { class: 'lesson' }, lessonMain, side));
    const drawSide = () => {
      tabsBox.innerHTML = ''; [['chapters', 'Chapters'], ['transcript', 'Transcript'], ['notes', 'My notes']].forEach(([k, t]) => tabsBox.append(el('button', { type: 'button', role: 'tab', 'aria-selected': String(UI.side === k), class: UI.side === k ? 'on' : '', onclick: () => { UI.side = k; drawSide(); } }, t)));
      sideBody.innerHTML = ''; const t = v.currentTime || 0;
      if (UI.side === 'chapters') {
        const items = s.chapters.map(c => ({ t: c[0], label: c[1], kind: 'ch' })).concat(s.stops.map((x, i) => ({ t: x.t, label: `Pause question ${i + 1}`, kind: 'stop', x }))).sort((a, b) => a.t - b.t);
        items.forEach((c, i) => { const nextT = (items[i + 1] || { t: s.video.dur }).t; const done = c.kind === 'stop' ? Core.stopDone(st, sid, c.x) : t >= nextT - 0.2 || review(); const cur = !done && t >= c.t - 0.2;
          sideBody.append(el('button', { type: 'button', class: 'chap' + (done ? ' done' : '') + (cur ? ' cur' : '') + (c.kind === 'stop' ? ' stopq' : ''), onclick: () => { segEnd = null; v.currentTime = c.t + (c.kind === 'stop' ? 0 : 0.01); } },
            el('span', { class: 'dt' }, done ? '✓' : c.kind === 'stop' ? '?' : String(s.chapters.findIndex(h => h[0] === c.t) + 1)), el('span', { style: 'flex:1' }, el('b', { style: 'font-size:15px' }, c.label), el('br'), el('small', { class: 'muted' }, fmt(c.t))))); });
      } else if (UI.side === 'transcript') {
        const box = el('div', { class: 'trans' }); s.captions.forEach((c, i) => { const nt = (s.captions[i + 1] || [s.video.dur])[0]; box.append(el('p', { class: t >= c[0] && t < nt ? 'cur' : '', onclick: () => { v.currentTime = c[0]; } }, el('code', {}, fmt(c[0])), ' ' + c[1])); }); sideBody.append(box);
      } else {
        st.notes = st.notes || {}; const ta = el('textarea', { rows: 8, 'aria-label': 'My notes', placeholder: 'e.g. Root hair cell – long extension → bigger surface area → absorbs water faster.' }); ta.value = st.notes[sid] || '';
        const ok = el('span', { class: 'muted' }); ta.oninput = () => { st.notes[sid] = ta.value; Core.persist(); ok.textContent = 'Saved'; };
        sideBody.append(el('label', { style: 'display:flex;flex-direction:column;gap:6px;font-weight:700;font-size:14px' }, `My notes for ${s.id}`, ta), ok);
      }
    };
    const drawMarks = () => { track.querySelectorAll('.mk').forEach(x => x.remove()); s.stops.forEach((x, i) => { const d = Core.stopDone(st, sid, x); track.append(el('button', { class: 'mk' + (d ? ' done' : ''), type: 'button', style: `left:${x.t / s.video.dur * 100}%`, title: `Pause question ${i + 1} · ${fmt(x.t)}`, 'aria-label': `Pause question ${i + 1} at ${fmt(x.t)}${d ? ' (answered)' : ''}`, onclick: e => { e.stopPropagation(); if (d || review()) { v.pause(); v.currentTime = x.t; showStop(x, true); } } }, String(i + 1))); }); };
    const next = () => s.stops.find(x => !Core.stopDone(st, sid, x));
    const syncUi = () => { const t = v.currentTime || 0; fill.style.width = (t / s.video.dur * 100) + '%'; time.textContent = `${fmt(t)} / ${fmt(s.video.dur)}`; track.setAttribute('aria-valuenow', Math.round(t));
      const playing = !v.paused; ppBtn.innerHTML = ''; const ic = svgI(playing ? I.pause : I.play, 16, '#fff', 0); ic.querySelector('path').setAttribute('fill', '#fff'); ppBtn.append(ic); ppBtn.setAttribute('aria-label', playing ? 'Pause' : 'Play');
      big.hidden = playing || !!openStop; player.classList.toggle('paused-q', !!openStop);
      const c = s.captions.filter(x => x[0] <= t + 0.05).pop(); capT.textContent = c ? c[1] : ''; };
    function showStop(x, again) {
      openStop = again ? null : x; panel.innerHTML = ''; const i = s.stops.indexOf(x);
      if (!again) { vs.pos = x.t; Core.persist(); }
      const rec = (vs.stops[x.id] = vs.stops[x.id] || { tries: 0 });
      const box = el('section', { class: 'card stop' }, el('div', { class: 'stopbar' }, el('span', { class: 'eyebrow' }, `⏸ PAUSE QUESTION ${i + 1} OF ${s.stops.length} · ${fmt(x.t)}`),
        el('button', { class: 'btn small ghost', type: 'button', onclick: () => { segEnd = null; v.currentTime = x.review[0]; v.play().catch(() => { }); } }, `↺ Rewatch ${fmt(x.review[0])}–${fmt(x.review[1])}`)));
      const qh = el('div'); box.append(qh); panel.append(box);
      if (again && rec.done) {
        QE.practice(x.q, qh, { rec: {}, seed: st.id, save: () => { }, onDone: () => { } });
        box.append(el('button', { class: 'btn small', type: 'button', onclick: () => { panel.innerHTML = ''; v.play().catch(() => { }); } }, 'Close & keep watching ▶'));
        return;
      }
      QE.practice(x.q, qh, { rec, seed: st.id, save: () => { Core.persist(); }, onCheck: onCheck(box, x.q, rec),
        onDone: () => {
          rec.done = true; if (rec.everWrong) st.stopsWrong[x.q.id] = true; Core.persist(); openStop = null; drawMarks(); drawSide(); bumpXp(); syncUi();
          box.append(el('button', { class: 'btn primary shine', type: 'button', id: 'continueVideo', onclick: () => { panel.innerHTML = ''; v.currentTime = x.t; v.play().catch(() => { }); } }, 'Keep watching', el('span', { class: 'arr' }, '→')));
        } });
      v.pause(); syncUi(); drawSide();
      setTimeout(() => panel.scrollIntoView({ block: 'nearest', behavior: 'smooth' }), 50);
    }
    function complete() {
      if (next()) return; if (!vs.completed) { vs.completed = true; Core.persist(); bumpXp(); Backend.track('video_complete', { learner: st.id, unit: Core.UNIT, sec: sid }); }
      panel.innerHTML = ''; panel.append(el('section', { class: 'card done' }, el('h3', {}, `✓ Lesson ${s.id} complete`),
        el('p', { style: 'margin:0 0 10px' }, `Next: 30 practice questions (8 Core) for section ${s.id}. You can now skip freely through the video to revise.`),
        el('button', { class: 'btn gold big shine', type: 'button', onclick: () => go('ex-' + R(sid)) }, `Practise ${s.id}`, el('span', { class: 'arr' }, '→'))));
      refreshToc(); drawSide();
    }
    const togglePlay = () => { if (openStop) { panel.querySelector('.stop') && panel.querySelector('.stop').classList.add('pulse'); return; } if (v.paused) v.play().catch(() => { }); else v.pause(); };
    ppBtn.onclick = togglePlay; big.onclick = togglePlay;
    track.addEventListener('click', e => { const r = track.getBoundingClientRect(); segEnd = null; v.currentTime = Math.max(0, Math.min(1, (e.clientX - r.left) / r.width)) * s.video.dur; });
    track.addEventListener('keydown', e => { if (e.key === 'ArrowRight') v.currentTime = Math.min(s.video.dur, v.currentTime + 5); if (e.key === 'ArrowLeft') v.currentTime = Math.max(0, v.currentTime - 5); if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); togglePlay(); } });
    spd.onclick = () => { UI.speed = UI.speed === 1 ? 1.25 : UI.speed === 1.25 ? 1.5 : UI.speed === 1.5 ? 2 : 1; v.playbackRate = UI.speed; spd.textContent = UI.speed + '×'; };
    cc.onclick = () => { UI.cc = !UI.cc; capP.hidden = !UI.cc; cc.classList.toggle('on', UI.cc); cc.setAttribute('aria-pressed', String(UI.cc)); };
    fs.onclick = () => { try { (player.requestFullscreen || player.webkitRequestFullscreen).call(player); } catch (e) { } };
    v.addEventListener('loadedmetadata', () => {
      v.playbackRate = UI.speed; let t0 = vs.pos || 0;
      if (UI.seek && UI.seek.sec === sid) { t0 = UI.seek.from; segEnd = UI.seek.to; UI.seek = null; panel.append(el('div', { class: 'banner info' }, `▶ Review clip ${fmt(t0)}–${fmt(segEnd)} – press play to watch.`)); }
      const nx = next();
      if (!review() && nx && t0 >= nx.t - 0.3) { v.currentTime = nx.t; showStop(nx); } else v.currentTime = Math.min(t0, s.video.dur - 0.5);
      if (vs.completed && !nx) complete();
      syncUi();
    });
    let lastSide = 0;
    v.addEventListener('timeupdate', () => {
      const t = v.currentTime;
      if (!review()) { const nx = next(); if (nx && t >= nx.t - 0.04 && openStop !== nx) { v.pause(); v.currentTime = nx.t; showStop(nx); } }
      if (segEnd != null && t >= segEnd) { v.pause(); segEnd = null; }
      if (Date.now() - lastSave > 2000) { vs.pos = t; lastSave = Date.now(); Core.persist(); }
      if (Date.now() - lastSide > 1500 && UI.side !== 'notes') { lastSide = Date.now(); drawSide(); }
      if (!next() && t >= s.video.dur - 0.6 && !vs.completed) complete();
      syncUi();
    });
    v.addEventListener('seeking', () => {
      if (review()) return; const nx = next();
      if (nx && v.currentTime > nx.t + 0.05) { v.currentTime = nx.t; if (openStop !== nx) showStop(nx); }
    });
    v.addEventListener('play', () => { if (openStop) { v.pause(); panel.querySelector('.stop') && panel.querySelector('.stop').classList.add('pulse'); } syncUi(); });
    v.addEventListener('pause', () => { vs.pos = v.currentTime; Core.persist(); syncUi(); });
    v.addEventListener('ended', () => complete());
    v.addEventListener('click', togglePlay);
    let triedBlob = false;
    v.addEventListener('error', async () => { if (triedBlob) return; triedBlob = true; try { const b = await (await fetch(s.video.src)).blob(); v.src = URL.createObjectURL(b); } catch (e) { panel.append(el('p', { class: 'err' }, 'The video could not be loaded.')); } });
    v.src = s.video.src; drawMarks(); drawSide(); syncUi();
  }

  /* ---------- reading lesson (Mathematics): key ideas, worked examples and check questions, no video ---------- */
  function viewLesson(sid) {
    const s = Core.sec(sid), m = $main();
    const lock = Core.secLock(st, s);
    subbar('', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}: ${C.unit.title}`), el('span', { class: 'sep' }), el('span', { class: 'ttl' }, `Lesson ${s.id} · ${s.title}`));
    if (lock) { m.append(bar(`Section ${s.id} · Lesson`), lockScreen(`Section ${s.id} is locked`, lock.reason, [lock])); return; }
    st.last = { route: 'v-' + R(sid) }; Core.persist();
    const vs = Core.vstate(st, sid); const xp0 = Core.xp(st);
    const head = el('section', { class: 'card lessonhead' }, el('p', { class: 'eyebrow', style: 'margin:0' }, `${Core.stageLabel()} · Unit ${Core.UNO} · Lesson ${s.id}`), el('h1', { style: 'margin:4px 0 6px' }, s.title),
      el('p', { class: 'muted', style: 'margin:0' }, `Read each idea and worked example, then answer the ${s.stops.length} check questions. About ${Math.max(5, Math.round(s.video.dur / 60))} minutes.`),
      el('ul', { class: 'lgoals' }, ...s.objs.map(o => el('li', {}, (C.objectives[o] || {}).t || o))));
    m.append(head);
    const body = el('div', { class: 'lessonbody' }); m.append(body);
    const status = el('div'); m.append(status);
    const drawStatus = () => { status.innerHTML = ''; const left = Core.stopsLeft(st, s).length;
      if (vs.completed && !left) { const i = C.sections.indexOf(s), nxt = C.sections[i + 1];
        status.append(el('div', { class: 'banner ok' }, el('b', {}, `✓ Lesson ${s.id} finished. `), 'Now practise: the Core questions unlock the next lesson.',
          el('button', { class: 'btn primary small', type: 'button', onclick: () => go('ex-' + R(s.id)) }, `Practise ${s.id}`, el('span', { class: 'arr' }, ' →'))));
        return; }
      status.append(el('section', { class: 'card', style: 'display:flex;gap:12px;align-items:center;flex-wrap:wrap' },
        el('span', {}, left ? `${left} check question${left > 1 ? 's' : ''} left in this lesson.` : 'You have answered every check question.'),
        el('button', { class: 'btn primary', type: 'button', id: 'lessonDone', disabled: !!left, onclick: () => { vs.completed = true; vs.pos = s.video.dur; Core.persist(); Backend.track('lesson_done', { learner: st.id, unit: Core.UNIT, sec: sid }); xpTick(); toast('Lesson finished – well done!'); drawStatus(); } }, 'I have finished this lesson ✓'))); };
    const stopFor = {}; s.stops.forEach(x => { (stopFor[x.after] = stopFor[x.after] || []).push(x); });
    const para = t => el('p', { class: 'lp' }, ...String(t).split(/(\*\*[^*]+\*\*)/).map(part => /^\*\*.*\*\*$/.test(part) ? el('b', {}, part.slice(2, -2)) : part));
    s.lesson.forEach((b, bi) => {
      const kind = b.k || 'idea', icon = { idea: '💡', example: '✏️', tip: '✅', mistake: '⚠️', method: '🧭' }[kind] || '💡';
      const card = el('section', { class: 'card lblock lb-' + kind, id: 'lb-' + bi }, el('h2', {}, el('span', { class: 'lbi', 'aria-hidden': 'true' }, icon), ' ', (kind === 'example' ? 'Worked example: ' : kind === 'mistake' ? 'Common mistake: ' : '') + b.t));
      (b.p || []).forEach(t => card.append(para(t)));
      if (b.fig) { const f = window.AtomicFig && window.AtomicFig.get ? window.AtomicFig.get(b.fig.kind, b.fig) : null; if (f) card.append(el('div', { class: 'qfig', html: f.svg })); }
      if (b.table) card.append(QE.dataTable ? QE.dataTable(b.table) : el('div'));
      if (b.q) card.append(el('p', { class: 'lq' }, el('b', {}, 'Question: '), b.q));
      if (b.steps) { const ol = el('ol', { class: 'lsteps' }); b.steps.forEach(([work, why]) => ol.append(el('li', {}, el('code', { class: 'mwork' }, work), why ? el('span', { class: 'why' }, ' ' + why) : null))); card.append(ol); }
      if (b.a) card.append(el('p', { class: 'lans' }, el('b', {}, 'Answer: '), b.a));
      body.append(card);
      (stopFor[bi] || []).forEach(x => {
        const i = s.stops.indexOf(x); const rec = (vs.stops[x.id] = vs.stops[x.id] || { tries: 0 });
        const box = el('section', { class: 'card stop lcheck' }, el('div', { class: 'stopbar' }, el('span', { class: 'eyebrow' }, `CHECK QUESTION ${i + 1} OF ${s.stops.length}`), rec.done ? el('span', { class: 'chip on' }, '✓ done') : null));
        const qh = el('div'); box.append(qh); body.append(box);
        QE.practice(x.q, qh, { rec, seed: st.id, save: () => { Core.persist(); }, onCheck: onCheck(box, x.q, rec),
          onDone: () => { rec.done = true; if (rec.everWrong) st.stopsWrong[x.q.id] = true; Core.persist(); xpTick(); drawStatus(); } });
      });
    });
    drawStatus();
  }

  /* ---------- exercises (question card + solution panel) ---------- */
  function viewExercises(sid) {
    const s = Core.sec(sid), m = $main(); if (!s) return go('home'); const route = 'ex-' + R(sid);
    const lock = Core.secLock(st, s);
    if (lock || !Core.videoDone(st, s)) {
      subbar('blue', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}: ${C.unit.title}`), el('span', { class: 'ttl' }, `${s.id} ${s.title} · Practice`));
      m.append(bar(`Section ${s.id} · Practice`), lock ? lockScreen(`Practice for section ${s.id} is locked`, lock.reason, [lock]) : lockScreen(`Practice for section ${s.id} is locked`, s.lesson ? 'Read the lesson and answer its check questions before you start the practice.' : 'Watch the whole video and answer its pause questions before you start the practice.', [Core.firstMissingIn(st, s)])); return;
    }
    const tab = UI.tab[route] || 'req'; const list = s[tab]; let idx = Math.min(UI.idx[route + tab] || 0, list.length - 1);
    st.last = { route, tab, idx }; Core.persist();
    const q = list[idx]; const go2 = i => { UI.idx[route + tab] = i; render(); };
    const pips = el('div', { class: 'pips', 'aria-hidden': 'true' }, ...list.map((x, i) => { const r = st.items[x.id] || {}; return el('span', { class: i === idx ? 'cur' : r.done ? (r.ok ? (r.tries === 1 ? 'ok' : 'half') : 'bad') : r.tries ? 'bad' : '' }); }));
    const tabName = { req: 'Core', prac: 'Practise', adv: '* Advanced' }[tab];
    subbar('blue', el('a', { class: 'back', href: '#u-' + Core.UNO }, `← Unit ${Core.UNO}`), el('span', { style: 'font-size:15px;color:#DCE8FA' }, `${s.id} ${s.title} · ${tabName} · `, el('b', { style: 'color:#fff' }, `Question ${idx + 1} of ${list.length}`)), pips,
      el('button', { class: 'btn small onblue', type: 'button', disabled: idx === 0, onclick: () => go2(idx - 1) }, '← Previous'),
      el('button', { class: 'btn small gold', type: 'button', id: 'nextQ', disabled: idx === list.length - 1, onclick: () => go2(idx + 1) }, 'Next', el('span', { class: 'arr' }, '→')));
    const tabs = el('div', { class: 'btnrow', role: 'tablist' }, ...[['req', `Core · ${8 - Core.reqLeft(st, s).length}/8`], ['prac', `Practice · ${s.prac.filter(x => (st.items[x.id] || {}).done).length}/${s.prac.length}`], ['adv', `* Advanced · ${s.adv.filter(x => (st.items[x.id] || {}).done).length}/${s.adv.length}`]]
      .map(([k, t]) => el('button', { class: 'chip' + (k === tab ? ' on' : ''), role: 'tab', type: 'button', 'aria-selected': String(k === tab), onclick: () => { UI.tab[route] = k; render(); } }, t)));
    st.marks = st.marks || {};
    const mk = el('button', { type: 'button', class: 'chip' + (st.marks[q.id] ? ' on' : ''), 'aria-pressed': String(!!st.marks[q.id]), style: 'margin-left:auto', onclick: () => { st.marks[q.id] = !st.marks[q.id]; Core.persist(); mk.classList.toggle('on'); mk.setAttribute('aria-pressed', String(!!st.marks[q.id])); } }, '★ Bookmark');
    tabs.append(mk);
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
      el('div', { class: 'goal' }, el('span', { class: 'gi' }, svgI(I.bulb, 16, '#1C2A3A', 2)), el('span', {}, tab === 'req' ? 'Right first time: 1 mark · second try: ½ mark. Two wrong tries: you get guided reasoning and a similar question.' : tab === 'adv' ? '* Advanced – optional. Written by Atomic from the real source named on each question.' : 'Practice – optional for unlocking, but it makes you stronger before the Unit Test.')));
    m.append(bar(`Unit ${Core.UNO} › ${s.id} › ${tabName} › question ${idx + 1}`), tocBtn(), doneBanner, tabs, chips, el('div', { class: 'exgrid' }, el('div', { class: 'q' }, card), aside));
    showBanner(); drawSol();
    QE.practice(q, card, { rec, seed: st.id, save: () => Core.persist(), onCheck: onCheck(card, q, rec), onDone: () => { rec.done = true; Core.persist(); showBanner(); refreshToc(); drawSol(); xpTick();
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
    const qs = s.req.concat(s.prac.slice(0, 6)); const doc = `S${Core.STAGE}-U${String(Core.UNO).padStart(2, '0')}-W${s.id.replace('.', '')}`;
    const mins = Math.max(15, Math.ceil(qs.length * 2.5 / 5) * 5);
    const out = el('div', { class: 'ws', id: 'wsPages' }); let pno = 0; const pages = [];
    const foot = last => el('div', { class: 'pfoot' }, el('div', {}, `© Atomic Education ${info.date.getFullYear()} · ${doc} · Copy #${info.serial} · ${info.code}`, el('br'), `Printed for ${info.name} (${info.lid}) on ${info.when}. Not for sharing or resale.`), el('b', {}, last ? 'End of worksheet' : '[Turn over'));
    const page = (...kids) => { pno++; const pg = el('div', { class: 'a4 paper4', html: Paper.frame() + Paper.watermark(info) }); pg.append(el('div', { class: 'pbody' }, ...kids)); pages.push(pg); return pg; };
    const runHead = () => el('div', { class: 'prun' }, el('span', {}, el('b', {}, 'Cambridge'), ` ${Core.stageLabel()} · Unit ${Core.UNO} · ${s.id} ${s.title}`), el('b', {}, String(pno + 1)));
    const boxes = (txt, n) => el('span', { class: 'pboxes' }, ...Array.from({ length: n }, (_, i) => el('i', {}, txt[i] || '')));
    const d = info.date, dd = String(d.getDate()).padStart(2, '0') + String(d.getMonth() + 1).padStart(2, '0') + d.getFullYear();
    // cover
    const cover = page(
      el('div', { class: 'pcv-h' }, el('img', { src: 'atomic_logo.png', alt: '' }), el('div', {}, el('div', { class: 'nm' }, 'ATOMIC EDUCATION'), el('div', { class: 'tg' }, el('b', {}, 'Cambridge'), ' Lower Secondary Science · Checkpoint preparation'))),
      el('div', { html: Paper.waves() }),
      el('div', { class: 'pcv-meta' }, 'Written by the Atomic teaching team · Videos, practice and Unit Tests online at Atomic'),
      el('div', { class: 'pcv-ttl' }, el('span', {}, 'PRACTICE WORKSHEET'), el('span', {}, `SCORE: ______ / ${qs.length}`)),
      el('table', { class: 'pgrid' }, el('tbody', {}, el('tr', {}, el('td', { class: 'k' }, 'LEARNER NAME'), el('td', { colspan: '3', class: 'pre' }, info.name)),
        el('tr', {}, el('td', { class: 'k' }, 'LEARNER ID'), el('td', {}, boxes(info.lid.replace(/-/g, ''), 8)), el('td', { class: 'k', style: 'width:22mm' }, 'DATE'), el('td', {}, boxes(dd, 8))))),
      el('div', { class: 'psubj' }, el('div', { class: 'ico', html: '<svg width="52" height="52" viewBox="0 0 56 56"><rect x="6" y="10" width="44" height="36" rx="10" fill="none" stroke="#0E1B3D" stroke-width="3"/><ellipse cx="28" cy="28" rx="13" ry="9" fill="#DCE8FA" stroke="#0149AF" stroke-width="2"/><circle cx="33" cy="27" r="4" fill="#0E1B3D"/></svg>' }),
        el('div', {}, el('div', { class: 'camline' }, el('b', {}, 'CAMBRIDGE'), ` ${Core.stageName(Core.STAGE).toUpperCase()} · SCIENCE`), el('div', {}, `Unit ${Core.UNO} · ${C.unit.title}`, el('br'), `${s.id} ${s.title}`)),
        el('div', { style: 'text-align:right' }, el('div', { class: 'code' }, doc), el('div', {}, `${mins} minutes`), el('small', {}, `${qs.length} questions`))),
      el('p', { style: 'margin:5mm 0 0' }, 'You must answer on this worksheet.'),
      el('div', { class: 'psec' }, 'INSTRUCTIONS'), el('ul', {}, el('li', {}, 'Answer ', el('b', {}, 'all'), ' questions. Questions 1–8 are Core; 9–14 are extra practice.'), el('li', {}, 'Use a black or dark blue pen. You may use an HB pencil for diagrams.'), el('li', {}, 'Write your answer to each question in the space provided. Show your working.'), el('li', {}, `When you finish, open topic ${s.id} on Atomic and check your answers with the worked solutions.`)),
      el('div', { class: 'psec' }, 'INFORMATION'), el('ul', {}, el('li', {}, `This worksheet has ${qs.length} questions.`), el('li', {}, 'Every printed copy carries the learner’s name, ID, date and a copy number.')),
      el('div', { class: 'pverify' }, el('span', { html: Paper.seal(info.code) }), el('div', {}, 'Verification code', el('br'), el('b', {}, info.code), el('br'), `Tied to this learner, this worksheet and copy #${info.serial}. Atomic keeps a record of every printed copy.`)));
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
    const qs = s.req.concat(s.prac.slice(0, 6)); const doc = `S${Core.STAGE}-U${String(Core.UNO).padStart(2, '0')}-W${s.id.replace('.', '')}`;
    const out = el('div', { class: 'ws', id: 'wsAns' }); mount.append(out);
    const foot = last => el('div', { class: 'pfoot' }, el('div', {}, `© Atomic Education ${info.date.getFullYear()} · ${doc} · ANSWERS · ${info.code}`, el('br'), `Opened by ${info.name} (${info.lid}) on ${info.when}. For self-marking only.`), el('b', {}, last ? 'End of answers' : '[Turn over'));
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
    const m = $main(); const a = Core.lastAttempt(st); const ts = Core.testState(st);
    m.append(bar(`Unit ${Core.UNO} › Review questions`));
    if (!a || !a.remed) { m.append(el('section', { class: 'card' }, el('p', {}, 'No review questions have been set yet.'))); return; }
    st.last = { route: 'remedial' }; Core.persist();
    const left = Core.remLeft(st, a);
    m.append(el('section', { class: 'card' }, el('h2', {}, `Review after attempt ${a.n}: ${a.remed.length - left.length}/${a.remed.length} done`), el('p', {}, 'Chosen from your weaker objectives: ' + a.weak.join(', ') + '. Finish them all to unlock the equivalent paper.'),
      ts.state === 'ready' ? el('a', { class: 'btn primary', href: '#test', id: 'goRetake' }, `Take the equivalent paper (Paper ${ts.form}) →`) : null));
    a.remed.forEach((id, i) => {
      const q = findQ(id); const card = el('section', { class: 'card qcard' }, el('p', { class: 'muted' }, `Review ${i + 1} of ${a.remed.length} · ${q.obj}`)); m.append(card);
      const k = Core.remKey(a, id); const rec = st.rem[k] = st.rem[k] || { tries: 0 };
      QE.practice(q, card, { rec, onCheck: onCheck(card, q, rec), seed: st.id + 'r' + a.n, save: () => Core.persist(), onDone: () => { rec.done = true; Core.persist(); if (!Core.remLeft(st, a).length) render(); } });
    });
  }
  function findQ(id) { for (const s of C.sections) for (const q of s.req.concat(s.prac, s.adv, s.stops.map(x => x.q))) if (q.id === id) return q; return null; }
  const allQs = () => C.sections.flatMap(s => s.req.concat(s.prac, s.adv));

  /* ---------- drills: wrong answers / by topic ---------- */
  function startDrill(title, qs, ns) { UI.drill = { title, ids: qs.map(q => q.id), ns }; go('drill'); }
  function viewDrill() {
    const m = $main(); const d = UI.drill; if (!d) return go('profile');
    m.append(bar('Progress › ' + d.title), el('h2', {}, d.title), el('p', { class: 'muted' }, 'Extra practice – it doesn\'t change scores you already have. Getting a question right first time removes it from your “wrong answers” list.'));
    if (!d.ids.length) { m.append(el('p', {}, 'No questions here.')); return; }
    d.ids.forEach((id, i) => { const q = findQ(id); const card = el('section', { class: 'card qcard' }, el('p', { class: 'muted' }, `${i + 1}/${d.ids.length}`)); m.append(card);
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
  // Stage certificate (A4 landscape). Atomic design: navy frame, gold rule, seal and the learner's achievements.
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
    return new Promise(res => { const img = new Image(); img.onload = done; img.onerror = done; img.src = 'atomic_logo.png';
      function done() {
        if (img.width) { const h = 120, w = img.width / img.height * h; g.drawImage(img, W / 2 - w / 2, 120, w, h); }
        center('CERTIFICATE OF ACHIEVEMENT', 320, '600 34px Outfit, Figtree, Arial', GOLD, 8);
        center(`Cambridge ${Core.stageLabel()}`, 410, '700 76px Outfit, Figtree, Arial', NAVY);
        center('Cambridge Lower Secondary Science (curriculum framework 0893)', 462, '28px Figtree, Arial', '#52627A');
        center('This is to certify that', 545, 'italic 32px Georgia, serif', '#3A4B63');
        center(c.name, 640, 'italic 700 96px Georgia, serif', BLUE);
        g.strokeStyle = GOLD; g.lineWidth = 2; g.beginPath(); g.moveTo(W / 2 - 420, 668); g.lineTo(W / 2 + 420, 668); g.stroke();
        center(`has completed the Atomic course for Cambridge ${Core.stageLabel()}:`, 718, '30px Figtree, Arial', NAVY); center(`all ${Core.unitCount()} units, every Unit Test and an end-of-year exam.`, 756, '30px Figtree, Arial', NAVY);
        // achievements row
        const stats = [[c.units || `${Core.unitCount()} / ${Core.unitCount()}`, 'units passed'], [c.avg || '—', 'Unit Test average'], [c.final || '—', 'end-of-year exam'], [c.hours || '—', 'hours of study'], [c.level || '—', 'level reached']];
        const bw = 250, gap = 22, x0 = W / 2 - (stats.length * bw + (stats.length - 1) * gap) / 2;
        stats.forEach(([b, t], i) => { const x = x0 + i * (bw + gap); g.fillStyle = '#FFFFFF'; g.strokeStyle = '#D9C59A'; g.lineWidth = 2; g.beginPath(); g.roundRect(x, 800, bw, 100, 18); g.fill(); g.stroke();
          g.textAlign = 'center'; g.fillStyle = BLUE; g.font = '700 40px Outfit, Figtree, Arial'; g.fillText(b, x + bw / 2, 852); g.fillStyle = '#52627A'; g.font = '22px Figtree, Arial'; g.fillText(t, x + bw / 2, 884); });
        // seal
        const sx = 300, sy = 1010; g.fillStyle = GOLD2; g.beginPath(); for (let i = 0; i < 48; i++) { const r = i % 2 ? 92 : 104, a = i / 48 * Math.PI * 2; g.lineTo(sx + r * Math.cos(a), sy + r * Math.sin(a)); } g.closePath(); g.fill();
        g.fillStyle = GOLD; g.beginPath(); g.arc(sx, sy, 80, 0, 7); g.fill(); g.strokeStyle = '#FFF4D6'; g.lineWidth = 3; g.beginPath(); g.arc(sx, sy, 68, 0, 7); g.stroke();
        g.fillStyle = '#FFFFFF'; g.textAlign = 'center'; g.font = '700 26px Outfit, Figtree, Arial'; g.fillText('ATOMIC', sx, sy - 8); g.font = '600 20px Figtree, Arial'; g.fillText(`CAMBRIDGE ${Core.stageName(Core.STAGE).toUpperCase()}`, sx, sy + 22); g.font = '22px Figtree'; g.fillText('★ ★ ★', sx, sy + 50);
        // signature + date + code
        g.strokeStyle = NAVY; g.lineWidth = 2; g.beginPath(); g.moveTo(W - 560, 1010); g.lineTo(W - 190, 1010); g.stroke();
        g.textAlign = 'center'; g.fillStyle = NAVY; g.font = 'italic 40px Georgia, serif'; g.fillText('The Atomic teaching team', W - 375, 995);
        g.font = '24px Figtree, Arial'; g.fillStyle = '#52627A'; g.fillText('Atomic Education', W - 375, 1045);
        g.textAlign = 'center'; g.fillStyle = NAVY; g.font = '600 24px Figtree, Arial'; g.fillText(`Awarded ${c.date}`, W / 2 - 60, 985); g.fillText(`Code ${c.code}`, W / 2 - 60, 1022);
        g.font = '20px Figtree, Arial'; g.fillStyle = '#6B7A90'; g.fillText('Check it at Atomic → “Verify a certificate”.', W / 2 - 60, 1060);
        g.fillText('Atomic courses follow the Cambridge Lower Secondary Science framework. This is an Atomic certificate, not a Cambridge qualification.', W / 2, 1120);
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
    const passedU = Object.keys(st.results || {}).length, fin = Core.finalPassed();
    if (!cert) {
      const items = [];
      if (passedU < Core.unitCount()) items.push({ what: `pass every Unit Test (${passedU} of ${Core.unitCount()} so far)`, route: 'tests' });
      if (!fin) items.push({ what: `pass an end-of-year exam (needs level ${TestRules.FINAL_LEVEL}; you are level ${Core.levelInfo().level})`, route: 'final' });
      m.append(lockScreen(`Your Cambridge ${Core.stageName(Core.STAGE)} certificate`, `The certificate is awarded when you have passed all ${Core.unitCount()} Unit Tests and one end-of-year exam. Here is how it will look:`, items));
      const img = el('img', { class: 'certimg', alt: `Preview of the Cambridge ${Core.stageName(Core.STAGE)} certificate` }); m.append(el('section', { class: 'card certwrap' }, img));
      drawCert({ name: st.name, code: 'AE-S7-XXXX-XXXXXXXX', date: '—', ...certStats() }, true).then(cv => { img.src = cv.toDataURL('image/png'); });
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
  const crumbs = (...tail) => el('nav', { class: 'crumb', 'aria-label': 'Breadcrumb' }, el('a', { href: '#home' }, 'Dashboard'), ' › ', el('a', { href: '#level' }, 'Lower Secondary'), ...tail.flatMap(t => [' › ', t]));
  // ---- course catalogue: subjects × levels (Science and Mathematics, Lower Secondary → IGCSE → AS & A Level) ----
  let CATALOG = null;
  async function loadCatalog() { if (!CATALOG) { try { const r = await fetch('content/catalog.json'); CATALOG = r.ok ? await r.json() : null; } catch (e) { CATALOG = null; } } return CATALOG; }
  const subjTag = (S0) => el('span', { class: 'subjtag', style: `--sc:${S0.color}` }, S0.icon + ' ' + S0.name);
  function courseCard(c, S0) {
    const isStage = !!c.stage && c.status !== 'soon'; const mine = isStage && st && c.stage === Core.learnerStage(), en = isStage && st && Core.enrolled(c.stage);
    const state = c.status === 'soon' ? 'soon' : mine ? 'mine' : en ? 'enrolled' : c.status === 'enrol' ? 'enrol' : 'open';
    const tag = { soon: 'COMING SOON', mine: 'YOUR COURSE', enrolled: 'ENROLLED', enrol: 'NOT ENROLLED', open: 'OPEN' }[state];
    const btn = state === 'soon' ? el('a', { class: 'btn small', href: '#course-' + c.id }, 'Details', el('span', { class: 'arr' }, ' →'))
      : state === 'mine' || state === 'enrolled' || state === 'open' ? el('a', { class: 'btn small primary', href: '#stage-' + c.stage }, 'Open', el('span', { class: 'arr' }, ' →'))
        : el('a', { class: 'btn small gold', href: '#checkout-' + c.stage }, `Enrol · ${PRICE}`, el('span', { class: 'arr' }, ' →'));
    return el('section', { class: 'card ccard ' + state + (mine ? ' cur' : ''), id: isStage ? 'stageCard' + c.stage : 'course-' + c.id, style: `--sc:${S0.color}` },
      el('div', { class: 'cchead' }, el('span', { class: 'cclv' }, c.stage ? String(c.badge || c.stage) : c.level === 'igcse' ? 'IG' : 'A'), el('span', { class: 'cccode' }, c.code)),
      el('span', { class: 'eyebrow', style: 'margin:0' }, tag), el('h3', { style: 'margin:0' }, c.title),
      el('p', { class: 'muted', style: 'margin:0;font-size:14px' }, mine ? `${Core.unitCount()} units · ≈ ${estH(Core.INDEX.est || 0)} of learning · Unit Tests, Checkpoint exam room, end-of-year exams and a certificate` : c.about || (c.stage ? `Cambridge Stage ${c.stage} – units are being prepared` : '')), btn);
  }
  async function viewCourses(subject) {
    const m = $main(); const K = await loadCatalog(); if (!K) { m.append(el('p', {}, 'Could not load the courses.')); return; }
    subject = subject || 'science'; const S0 = K.subjects.find(x => x.id === subject) || K.subjects[0];
    pageHero('ATOMIC COURSES', 'Subjects and levels', 'Choose a subject, then a level – from Cambridge Lower Secondary (Checkpoint) to IGCSE and AS & A Level. Each stage or course is enrolled separately.');
    m.append(el('nav', { class: 'subjtabs', role: 'tablist', 'aria-label': 'Subjects' }, ...K.subjects.map(x => el('a', { role: 'tab', class: 'subjtab' + (x.id === S0.id ? ' on' : ''), 'aria-selected': String(x.id === S0.id), href: '#courses-' + x.id, style: `--sc:${x.color}` }, x.icon + ' ' + x.name,
      el('small', {}, K.courses.some(c => c.subject === x.id && c.status !== 'soon') ? 'open now' : 'coming soon')))));
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
      el('p', { style: 'margin:0' }, `This course is being written by the Atomic teaching team. It will work like Cambridge ${Core.stageLabel()}: short lesson videos with pause questions, practice for every topic, print-only worksheets, timed Unit Tests in the exam room and a certificate.`));
    if (c.strands) box.append(el('div', {}, el('b', {}, 'Curriculum strands'), el('div', { class: 'chips' }, ...c.strands.map(x => el('span', { class: 'chip' }, x)))));
    if (c.exams) box.append(el('div', {}, el('b', {}, 'Checkpoint exam room (practice papers in this format)'), el('ul', { style: 'margin:6px 0 0' }, ...c.exams.map(e => el('li', {}, el('b', {}, `${S0.name} ${e.code}`), ` · ${e.name} · ${e.minutes} minutes · ${e.marks} marks · ${e.note}`)))));
    const msg = el('span', { class: 'muted' });
    box.append(el('div', { class: 'btnrow' }, st && !isGuest() ? el('button', { class: 'btn gold', type: 'button', id: 'notifyMe', onclick: () => { Backend.track('course_interest', { learner: st.id, course: c.id }); msg.textContent = '✓ Thank you – we will tell you when it opens.'; } }, '🔔 Tell me when it opens') : null, el('a', { class: 'btn', href: '#courses-' + S0.id }, 'All ' + S0.name + ' courses'), msg));
    m.append(box);
  }
  async function viewStage(g) {
    const m = $main();
    if (g !== Core.STAGE && Core.enrolled(g)) {   // an enrolled stage: open it (its units, tests and certificate)
      try { const r = await fetch(`content/stage${g}.json`); if (r.ok && (await r.json()).units.some(u => u.ready)) { await Core.switchStage(g); C = Core.C; st = Core.cur(); return render(); } } catch (e) { }
    }
    if (g !== Core.STAGE) {
      pageHero('LOWER SECONDARY', `Cambridge ${Core.stageName(g)}`, Core.enrolled(g) ? `You are enrolled in Cambridge ${Core.stageName(g)}.` : `Cambridge ${Core.stageName(g)} is a separate course.`);
      m.append(crumbs(`Cambridge ${Core.stageName(g)}`));
      if (!Core.enrolled(g)) { m.append(el('section', { class: 'card lockcard' }, el('h2', {}, `🔒 Enrol in Cambridge ${Core.stageName(g)}`), el('p', {}, `Each stage is its own course. Enrol and pay for Cambridge ${Core.stageName(g)} to open it on this account.`), el('a', { class: 'btn gold', href: '#checkout-' + g }, `Enrol · ${PRICE}`, el('span', { class: 'arr' }, ' →')))); return; }
      m.append(el('section', { class: 'card done' }, el('h2', {}, `✓ Enrolled in Cambridge ${Core.stageName(g)}`), el('p', {}, `The Cambridge ${Core.stageName(g)} units open here as soon as they have been reviewed. You will get a notification.`), el('a', { class: 'btn small', href: `#stage-${Core.STAGE}` }, `Back to Cambridge ${Core.stageName(Core.STAGE)}`)));
      return;
    }
    const tot = Core.totalSeconds(), passedN = Object.keys(st.results || {}).filter(k => k.startsWith(`stage${Core.STAGE}-unit`)).length;
    pageHero(Core.IS_MATHS ? 'CAMBRIDGE LOWER SECONDARY MATHEMATICS' : 'CAMBRIDGE LOWER SECONDARY SCIENCE', `Cambridge ${Core.stageLabel()}`, 'Open any unit at any time – you do not have to finish one before starting another.',
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
  function viewCheckout(g) {
    const m = $main();
    if (g === Core.STAGE || Core.enrolled(g)) return go('stage-' + g);
    pageHero('ENROL', `Cambridge ${Core.stageName(g)} course`, 'Each stage is a separate course with its own Unit Tests, end-of-year exams and certificate.');
    m.append(crumbs(el('a', { href: '#stage-' + g }, `Cambridge ${Core.stageName(g)}`), 'Checkout'));
    if (isGuest()) { m.append(guestWall('Create a free account first')); return; }
    const msg = errBox();
    m.append(el('section', { class: 'card narrow', id: 'checkout' }, el('h2', {}, 'Order summary'),
      el('div', { class: 'ordrow' }, el('span', {}, `Cambridge Lower Secondary Science · Cambridge ${Core.stageName(g)} (Atomic course)`), el('b', {}, PRICE)),
      el('div', { class: 'ordrow' }, el('span', {}, 'Learner'), el('b', {}, st.name)),
      el('div', { class: 'banner info' }, el('b', {}, 'Test checkout. '), 'This is the test server: pressing Pay enrols you straight away and no money is taken. The real payment page (Paddle) replaces this before launch.'),
      msg, el('button', { class: 'btn gold big', type: 'button', id: 'payBtn', onclick: async ev => { ev.currentTarget.disabled = true; msg.textContent = '';
        try { await Core.enrol(g, PRICE); confetti(); toast(`You are enrolled in Cambridge ${Core.stageName(g)}.`); go('stage-' + g); } catch (x) { ev.currentTarget.disabled = false; msg.textContent = x.code === 'payments_closed' ? 'Enrolment is not open yet on this server.' : errText(x); } } }, `Pay ${PRICE} (test)`)));
  }

  /* ---------- question bank ---------- */
  function viewBank() {
    const m = $main(); UI.bank = UI.bank || { sec: 'all', diff: 'all', type: 'all', status: 'all', tier: 'all' }; const F = UI.bank;
    pageHero(`CAMBRIDGE ${Core.stageName(Core.STAGE).toUpperCase()} · ALL ${Core.unitCount()} UNITS`, 'Question Bank', `Every practice question of Cambridge ${Core.stageName(Core.STAGE)}, unit by unit. Choose a unit, then filter by topic, difficulty and type. Every question you finish earns XP.`);
    const doneIn = n => Object.values((Core.S.states[Core.unitId(n)] || {}).items || {}).filter(x => x && x.done).length;
    m.append(el('section', { class: 'card', id: 'bankUnits' }, el('b', { class: 'lex' }, 'Choose a unit'),
      el('div', { class: 'bankunits' }, ...Core.INDEX.units.filter(u => u.ready).map(u => { const d = Math.min(doneIn(u.n), u.qs || 0), pct = u.qs ? Math.round(d / u.qs * 100) : 0;
        return el('button', { type: 'button', class: 'bunit' + (u.n === Core.UNO ? ' on' : ''), 'aria-pressed': String(u.n === Core.UNO), 'data-unit': u.n, onclick: () => { F.sec = 'all'; Core.switchUnit(u.n).then(() => render()); } },
          unitIcon(u.n), el('span', {}, el('b', {}, `Unit ${u.n}`), el('br'), el('small', {}, u.t)), el('span', { class: 'bpct' }, el('span', { class: 'pbar' }, el('i', { style: `width:${pct}%` })), el('small', {}, `${d}/${u.qs}`))); }))));
    m.append(el('div', {}, el('span', { class: 'eyebrow' }, `UNIT ${Core.UNO} · ${C.unit.title.toUpperCase()}`), el('h2', { style: 'margin:0;font-size:30px' }, `Unit ${Core.UNO} questions`),
      el('p', { class: 'muted', style: 'margin:4px 0 0' }, `${allQs().length} practice questions (${C.sections[0] ? C.sections[0].req.length + C.sections[0].prac.length + C.sections[0].adv.length : 30} per section: ${C.sections[0] ? C.sections[0].req.length : 8} Core, ${C.sections[0] ? C.sections[0].prac.length : 18} Practice, ${C.sections[0] ? C.sections[0].adv.length : 4} Advanced) plus ${C.sections.reduce((a, s) => a + s.stops.length, 0)} ${C.sections[0] && C.sections[0].lesson ? 'check' : 'pause'} questions. Practising here never changes your Core progress or test scores.`)));
    const chipRow = (label, key, opts) => el('div', { class: 'btnrow', role: 'group', 'aria-label': label }, el('b', { style: 'min-width:92px;font-size:14px' }, label), ...opts.map(([v, t]) => el('button', { type: 'button', class: 'chip' + (F[key] === v ? ' on' : ''), 'aria-pressed': String(F[key] === v), onclick: () => { F[key] = v; render(); } }, t)));
    m.append(el('section', { class: 'card' }, chipRow('Section', 'sec', [['all', 'All']].concat(C.sections.map(s => [s.id, s.id + ' ' + s.title.split(' ')[0]]))),
      chipRow('Set', 'tier', [['all', 'All'], ['req', 'Core'], ['prac', 'Practice'], ['adv', '* Advanced']]),
      chipRow('Difficulty', 'diff', [['all', 'All'], ['M', 'Medium'], ['H', 'Hard'], ['VH', 'Very hard']]),
      chipRow('Type', 'type', [['all', 'All'], ['fig', 'Diagrams & data'], ['calc', 'Calculations'], ['explain', 'Written'], ['mcq', 'Multiple choice']]),
      chipRow('Status', 'status', [['all', 'All'], ['todo', 'Not done'], ['wrong', 'Got wrong'], ['mark', '★ Bookmarked']])));
    const tierOf = q => C.sections.find(s => s.req.includes(q)) ? 'req' : q.adv ? 'adv' : 'prac';
    const secOf = q => C.sections.find(s => s.req.concat(s.prac, s.adv).includes(q)).id;
    const typeOk = q => F.type === 'all' || (F.type === 'fig' ? ['label', 'scale', 'graph', 'table', 'grid', 'sim'].includes(q.type) || !!q.fig : F.type === 'calc' ? ['num', 'scale', 'table'].includes(q.type) : F.type === 'explain' ? q.type === 'explain' : ['mcq', 'multi'].includes(q.type));
    st.marks = st.marks || {};
    const list = allQs().filter(q => (F.sec === 'all' || secOf(q) === F.sec) && (F.diff === 'all' || q.diff === F.diff) && (F.tier === 'all' || tierOf(q) === F.tier) && typeOk(q)
      && (F.status === 'all' || (F.status === 'todo' ? !(st.items[q.id] || {}).done : F.status === 'wrong' ? (st.items[q.id] || {}).everWrong : !!st.marks[q.id])));
    m.append(el('div', { class: 'btnrow between' }, el('b', { class: 'lex', id: 'bankCount' }, `${list.length} question${list.length === 1 ? '' : 's'}`),
      el('button', { class: 'btn primary small shine', type: 'button', disabled: !list.length, id: 'bankPractise', onclick: () => startDrill(`Question Bank · ${list.length > 15 ? 'first 15 of ' + list.length : list.length} questions`, list.slice(0, 15), 'bank') }, `Practise ${Math.min(15, list.length)}`, el('span', { class: 'arr' }, '→')),
      el('a', { class: 'btn small', href: '#topic' }, 'Revise by topic')));
    const tbl = el('div', { class: 'card lbtable' }, el('div', { class: 'lbrow h', style: 'grid-template-columns:90px 2.6fr 1fr 1fr 110px' }, el('span', {}, 'ID'), el('span', {}, 'QUESTION'), el('span', {}, 'SET'), el('span', {}, 'STATUS'), el('span', {}, '')));
    list.forEach(q => { const r = st.items[q.id] || {}; const t = tierOf(q);
      const mk = el('button', { type: 'button', class: 'chip' + (st.marks[q.id] ? ' on' : ''), 'aria-pressed': String(!!st.marks[q.id]), 'aria-label': 'Bookmark ' + q.id, style: 'min-height:38px;padding:0 10px', onclick: e => { e.stopPropagation(); st.marks[q.id] = !st.marks[q.id]; Core.persist(); mk.classList.toggle('on'); } }, '★');
      tbl.append(el('div', { class: 'lbrow', style: 'grid-template-columns:90px 2.6fr 1fr 1fr 110px' }, el('code', { style: 'font-size:13px;color:#52627A' }, q.id),
        el('span', { style: 'min-width:0' }, el('span', { style: 'display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis' }, q.prompt.replace(/^\* Advanced\.\s*/, '')), el('small', { class: 'muted' }, `${secOf(q)} · ${QE.TYPE_VI[q.type]} · ${QE.DIFF[q.diff]} · ${q.obj}`)),
        el('span', {}, el('span', { class: 'tag ' + (t === 'adv' ? 'adv' : t === 'req' ? 'd-M' : '') }, t === 'req' ? 'Core' : t === 'adv' ? '* Advanced' : 'Practice')),
        el('span', {}, r.done ? el('span', { class: 'status done' }, r.ok ? (r.tries === 1 ? 'Right 1st try' : 'Correct') : 'Completed') : r.tries ? el('span', { class: 'tag d-VH' }, 'In progress') : el('span', { class: 'status todo' }, 'Not done')),
        el('span', { style: 'display:flex;gap:6px' }, mk, el('button', { type: 'button', class: 'btn small', style: 'min-height:38px;padding:0 12px', onclick: () => startDrill(`Question ${q.id}`, [q], 'bank') }, 'Open')))); });
    if (!list.length) tbl.append(el('p', { class: 'muted', style: 'padding:16px 24px' }, 'No questions match these filters.'));
    m.append(tbl);
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
      el('div', { class: 'btnrow between', style: 'margin:0' }, el('span', { class: 'lex', style: 'font-weight:700;color:#556377' }, `Question ${i + 1} of ${qs.length} · ${q.pts} mark${q.pts > 1 ? 's' : ''}${q.teacher ? ' · marked by an Atomic marker' : ''}`),
        el('button', { class: 'chip' + (UI.flags[q.id] ? ' on' : ''), type: 'button', 'aria-pressed': String(!!UI.flags[q.id]), onclick: () => { UI.flags[q.id] = !UI.flags[q.id]; render(); } }, svgI(I.flag, 14), UI.flags[q.id] ? 'Flagged' : 'Flag')),
      el('h2', { class: 'qp', style: 'font-size:24px' }, q.prompt));
    QE.renderBody(q, card, { seed: X.seed, resp: draft.answers[q.id], onChange: r => { draft.answers[q.id] = r; draft.ts = Date.now(); X.save(); saved.textContent = 'Draft saved ' + new Date().toLocaleTimeString(); drawNav(); } });
    card.append(el('div', { class: 'btnrow between', style: 'padding-top:16px;border-top:1px solid #E6EEF8' }, el('button', { class: 'btn small', type: 'button', disabled: i === 0, onclick: () => { UI.testIdx = i - 1; render(); } }, '← Previous'), saved,
      i < qs.length - 1 ? el('button', { class: 'btn primary', type: 'button', id: 'testNext', onclick: () => { UI.testIdx = i + 1; render(); } }, 'Next question', el('span', { class: 'arr' }, '→')) : el('button', { class: 'btn navy', type: 'button', onclick: () => finish(false) }, 'Finish')));
    const nav = el('div', { class: 'navgrid' });
    const drawNav = () => { nav.innerHTML = ''; qs.forEach((x, k) => nav.append(el('button', { type: 'button', class: (UI.flags[x.id] ? 'flag' : answered(x) ? 'ans' : '') + (k === i ? ' on' : ''), 'aria-label': `Question ${k + 1}${answered(x) ? ', answered' : ''}${UI.flags[x.id] ? ', flagged' : ''}`, onclick: () => { UI.testIdx = k; render(); } }, String(k + 1)))); };
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
  function examIntro(t) {   // the "before you start" card
    return el('section', { class: 'card', style: 'max-width:760px;margin:0 auto;padding:40px;border-radius:28px;display:flex;flex-direction:column;gap:16px' },
      el('span', { class: 'eyebrow' }, 'EXAM ROOM · BEFORE YOU START'), el('h1', { style: 'margin:0;font-size:34px' }, t.title),
      el('div', { class: 'stats3' }, el('div', {}, el('b', {}, String(t.n)), el('br'), el('small', { class: 'muted' }, 'questions')), el('div', {}, el('b', {}, String(t.max)), el('br'), el('small', { class: 'muted' }, 'marks')),
        el('div', {}, el('b', {}, t.minutes + ' min'), el('br'), el('small', { class: 'muted' }, 'time allowed')), el('div', {}, el('b', {}, t.passTxt), el('br'), el('small', { class: 'muted' }, 'to pass'))),
      el('ul', { style: 'margin:0;padding-left:20px;color:#3A4B63' }, el('li', {}, `The clock starts when you press Start and keeps running if you leave the page or close the browser. At 0:00 your answers are submitted automatically.`),
        el('li', {}, 'No hints or videos during the paper. You can flag a question and come back to it; answers are saved as you go.'),
        el('li', {}, el('b', {}, 'Exam conditions: '), `the paper opens full screen and the rest of the site is closed. Leaving the exam room (another tab or app, leaving full screen, Back or reload) is recorded. After ${EXAM_MAX_LEAVES - 1} warnings, the ${EXAM_MAX_LEAVES === 3 ? 'third' : EXAM_MAX_LEAVES + 'th'} time you leave hands your paper in automatically.`), ...(t.extra || []).map(x => el('li', {}, x))),
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
    if (ts.state === 'paywall') { m.append(bar(where), lockScreen(`Unit Test ${Core.UNO} needs a Cambridge ${Core.stageName(Core.STAGE)} plan`, 'Unit Tests, marking and the certificate are part of the full course.', [{ what: `a Cambridge ${Core.stageName(Core.STAGE)} plan (7-day free trial)`, route: 'pricing' }])); return; }
    if (ts.state === 'locked') { m.append(bar(where), lockScreen(`Unit Test ${Core.UNO} is locked`, `The Unit Test opens when you have ${C.sections[0] && C.sections[0].lesson ? 'read every lesson' : 'watched every video'} and finished all ${totalCore} Core questions in this unit.`, ts.miss)); return; }
    if (ts.state === 'pending') { m.append(bar(where), el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, `Attempt ${ts.last.n} (Paper ${ts.last.form}) has a written answer for an Atomic marker to mark. We will notify you when it is done.`), el('a', { class: 'btn primary small', href: '#result' }, 'Results & history'))); return; }
    if (ts.state === 'remediate') { m.append(bar(where), lockScreen('You can\'t retake yet', 'Finish the review questions set for your weaker objectives before you take the equivalent paper.', [{ what: `${ts.left.length} review questions`, route: 'remedial' }])); return; }
    if (ts.state === 'passed') { m.append(bar(where), el('section', { class: 'card done' }, el('h2', {}, `✓ You have passed Unit Test ${Core.UNO}`), el('a', { class: 'btn primary small', href: '#result' }, 'See results'), el('a', { class: 'btn small', href: '#tests' }, 'All tests & exams'))); return; }
    const qs = C.tests[form];
    st.last = { route: 'test' };
    const draft = st.test.drafts[form] = st.test.drafts[form] || { answers: {}, ts: Date.now() };
    const running = !!draft.deadline;
    if (!UI.testOn) {
      m.append(bar(where), examIntro({ title: `Unit Test ${Core.UNO} · Paper ${form}${ts.retake ? ' (equivalent paper)' : ''}`, n: qs.length, max: 30, minutes: TestRules.UNIT_MINUTES, passTxt: '> 70%', resume: running,
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
      const status = res ? el('span', { class: 'status done' }, `✓ Passed · ${res.pct.toFixed(1)}%`) : ready ? el('span', { class: 'status cur' }, 'Ready to take') : el('span', { class: 'status todo' }, `${Math.min(coreDone, core)}/${core} Core done`);
      return el('div', { class: 'lbrow trow' }, el('span', {}, unitIcon(u.n)), el('span', {}, el('b', {}, `Unit Test ${u.n}`), el('br'), el('small', { class: 'muted' }, u.t)),
        el('span', { class: 'muted' }, `${TestRules.UNIT_MINUTES} min · 30 marks`), el('span', {}, status),
        el('button', { class: 'btn small ' + (res ? '' : 'primary'), type: 'button', 'data-unit': u.n, onclick: () => Core.switchUnit(u.n).then(() => go(res ? 'result' : 'test')) }, res ? 'Results' : 'Open', el('span', { class: 'arr' }, ' →')));
    });
    m.append(el('section', { class: 'card lbtable', id: 'testsTable' }, el('div', { class: 'lbrow h trow' }, el('span', {}, ''), el('span', {}, 'UNIT TEST'), el('span', {}, 'TIME'), el('span', {}, 'STATUS'), el('span', {}, '')), ...rows));
    if (F) m.append(finalCard(F, li));
    const P = await Core.loadCp(); if (P) { await Core.refreshCp().catch(() => { }); m.append(checkpointCard(P)); }
  }
  function finalCard(F, li) {
    const ok = (Core.S.tester || li.level >= F.level), done = (Core.S.finalAttempts || []).filter(a => a.status === 'final'), best = done.reduce((a, x) => Math.max(a, x.pct), 0);
    return el('section', { class: 'card finalcard', id: 'finalCard' }, el('span', { class: 'eyebrow' }, `END OF CAMBRIDGE ${Core.stageName(Core.STAGE).toUpperCase()}`), el('h2', { style: 'margin:2px 0' }, '🏁 End-of-year exams'),
      el('p', {}, `${Object.keys(F.papers).length} papers, each ${F.minutes} minutes and ${F.max} marks, covering all ${Core.unitCount()} units. Pass above ${Math.round(F.pass * 100)}%. Opens at level ${F.level}.`),
      el('div', { class: 'lvgate' }, el('b', {}, ok ? `✓ You are level ${li.level} – the exams are open.` : `You are level ${li.level}. Reach level ${F.level} (${TestRules.xpForLevel(F.level) - li.xp} more XP).`), el('div', { class: 'pbar' }, el('i', { style: `width:${Math.min(100, li.xp / TestRules.xpForLevel(F.level) * 100)}%` }))),
      done.length ? el('p', { class: 'muted' }, `${done.length} paper(s) taken · best ${best.toFixed(1)}%${Core.finalPassed() ? ' · passed ✓' : ''}`) : null,
      el('a', { class: 'btn ' + (ok ? 'gold shine' : ''), href: '#final' }, ok ? 'Choose a paper' : 'See the papers', el('span', { class: 'arr' }, ' →')));
  }

  /* ---------- Checkpoint exam room: Atomic papers in the format of Cambridge Lower Secondary Checkpoint ---------- */
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
        return el('div', { class: 'cprow' }, el('span', { class: 'cpcode' }, t.code), el('span', {}, el('b', {}, `${subj} · Paper ${t.paper}`), el('br'), el('small', { class: 'muted' }, `Atomic paper · Set ${set}${isM ? (mt.calculator ? ' · calculator allowed' : ' · no calculator') : ''}${mt.level === 'harder' ? (isM ? ' · harder' : ' · harder, investigation-based') : ''} · ${P.minutes} min · ${P.max} marks`)),
          a ? el('span', { class: 'status ' + (a.status === 'pending' ? 'cur' : 'done') }, a.status === 'pending' ? '⏳ Awaiting marking' : `${+a.score.toFixed(1)}/${P.max} · ${a.pct.toFixed(0)}%`) : d && d.deadline ? el('span', { class: 'status cur' }, 'In progress') : el('span', { class: 'status todo' }, 'Not taken'),
          a ? el('a', { class: 'btn small', href: '#cpr-' + k }, 'Results') : el('a', { class: 'btn small primary', href: '#cpx-' + k, id: 'cpOpen-' + k }, d && d.deadline ? 'Continue' : 'Enter', el('span', { class: 'arr' }, ' →'))); })));
    });
    const other = el('section', { class: 'card cpsubj soon' }, head(!isM),
      el('div', { class: 'cpset' }, el('a', { class: 'btn small', href: isM ? '#stage-9' : '#stage-19' }, isM ? 'Open the Science Stage 9 course for these papers →' : 'Open the Mathematics Stage 9 course for these papers →')));
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
        extra: [`An Atomic practice paper in the format of the Cambridge Lower Secondary Checkpoint ${t.subj} test.${Core.IS_MATHS ? (((P.meta || {})[k] || {}).calculator ? ' A calculator is allowed.' : ' Do not use a calculator.') : ''} One attempt per paper.`, 'Every answer, chosen or typed, is marked automatically; your results show your marks for each part of science.'],
        start: async ev => { ev.currentTarget.disabled = true; try { const c = await Core.startClock(`stage${Core.STAGE}-cp`, k); draft.deadline = c.deadline; save(); UI.testOn = true; UI.examKey = 'C' + k; UI.testIdx = 0; render(); } catch (x) { ev.currentTarget.disabled = false; modal('Could not open the paper', errText(x), [{ t: 'OK', cls: 'primary' }]); } } }));
      return;
    }
    examRoom({ title, badge: 'CHECKPOINT · SCIENCE ' + t.code, qs, max: P.max, draft, save, seed: st.id + 'C' + k, deadline: draft.deadline,
      onSubmit: async (answers, key, meta) => { await Core.submitCp(k, answers, key, meta); try { localStorage.removeItem(fdKey(dk)); } catch (e) { } UI.examKey = null; go('cpr-' + k); } });
  }
  async function viewCpResult(k) {
    const m = $main(); const P = await Core.loadCp(); await Core.refreshCp().catch(() => { });
    const a = (Core.S.cpAttempts || []).find(x => x.form === k); if (!a) return go('cpx-' + k); const t = cpTitle(P, k);
    m.append(el('nav', { class: 'crumb2' }, el('a', { href: '#tests' }, 'Tests & exams'), ' › ', el('a', { href: '#checkpoint' }, 'Checkpoint exam room'), ` › ${t.subj} ${t.code} · Set ${t.set}`));
    if (a.status === 'pending') { m.append(el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, 'A written answer is waiting for an Atomic marker. You will get a notification.'), leavesNote(a))); return; }
    m.append(el('section', { class: 'card' }, el('div', { class: 'resultbig' }, ring(a.pct, a.pct >= 50), el('div', {}, el('span', { class: 'eyebrow' }, `SCIENCE · PAPER ${t.paper} (${t.code} FORMAT) · SET ${t.set}`), el('h2', { style: 'margin:0' }, `${+a.score.toFixed(2)}/${P.max} (${a.pct.toFixed(1)}%)`),
      el('p', { style: 'margin:4px 0' }, a.duration != null ? `Time taken: ${Math.floor(a.duration / 60)} min ${a.duration % 60} s of ${P.minutes} min${a.overtime ? ' (after the time limit)' : ''}` : ''), leavesNote(a)))));
    const byS = Object.entries(a.byObj || {});
    m.append(el('section', { class: 'card' }, el('h2', {}, 'Marks by area of science'), el('div', { class: 'weak' }, ...byS.map(([o, b]) => { const pct = b.max ? b.got / b.max * 100 : 0;
      return el('div', { class: 'wk' }, el('b', {}, CP_STRAND[o] || o), el('div', { class: 'pbar' + (pct < 50 ? ' red' : '') }, el('i', { style: `width:${Math.max(2, pct)}%` })), el('small', { class: 'muted' }, `${+b.got.toFixed(2)}/${b.max} marks`)); })),
      el('a', { class: 'btn small primary', href: '#checkpoint' }, 'Back to the Checkpoint exam room')));
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
    if (a.status === 'pending') { m.append(el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, 'A written answer is waiting for an Atomic marker.'))); return; }
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
    if (a.status === 'pending') m.append(el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, 'Your written answer is waiting for an Atomic marker. Pass/not passed is decided only when the final mark is in – you will get a notification.')));
    else if (a.passed) m.append(el('section', { class: 'card done' }, el('div', { class: 'resultbig' }, ring(a.pct, true), el('div', {}, el('span', { class: 'eyebrow' }, 'PASSED'), el('h2', { style: 'margin:0' }, `${+a.score.toFixed(2)}/30 (${a.pct.toFixed(1)}%)`), el('p', { style: 'margin:4px 0' }, `Unit ${Core.UNO} complete in ${hrs(Core.unitSeconds(Core.UNO))} of study. Your ranking score for this unit = your first-pass %: ` + ((st.results || {})[Core.UNIT] ? st.results[Core.UNIT].pct.toFixed(1) : a.pct.toFixed(1)) + '%.' + (a.duration != null ? ` Time in the exam room: ${Math.floor(a.duration / 60)} min.` : '')))),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn primary small', href: '#board' }, '🏆 Leaderboard'), el('a', { class: 'btn small', href: '#cert' }, '🎓 Certificate'))));
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

  /* ---------- concept map (Atomic's own maps for every unit): tap a concept → its video and questions ---------- */
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
      else { const vid = el('video', { class: 'cmvideo', controls: true, preload: 'metadata', playsinline: true, src: s.video.src, poster: s.video.src.replace('.mp4', '_poster.jpg') });
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
      tile('🧩', 'Revise by topic', '9 objectives O1–O9', () => go('topic'), 'tileTopic'),
      tile('📄', 'Worksheets opened', st.ws.length ? st.ws.map(x => 'Section ' + x).join(', ') : 'none opened yet', () => go(st.ws.length ? 'ws-' + R(st.ws[st.ws.length - 1]) : 'ws-3-1'), 'tileWs')));
    if (st.ws.length) m.append(el('div', { class: 'btnrow' }, ...st.ws.map(x => el('a', { class: 'chip', href: '#ws-' + R(x) }, '📄 Worksheet ' + x))));
    m.append(el('section', { class: 'card' }, el('h2', {}, `Unit ${Core.UNO} progress`), ...C.sections.map(s => el('div', { style: 'margin:10px 0' }, el('div', { style: 'display:flex;justify-content:space-between;font-size:14px;font-weight:600' }, el('span', {}, `${s.id} ${s.title}`), el('span', { class: 'muted' }, `${s.lesson ? 'lesson' : 'video'} ${Core.videoDone(st, s) ? '✓' : '…'} · Core ${8 - Core.reqLeft(st, s).length}/8 · practice ${s.prac.filter(q => (st.items[q.id] || {}).done).length}/${s.prac.length} · advanced ${s.adv.filter(q => (st.items[q.id] || {}).done).length}/${s.adv.length}`)), el('div', { class: 'pbar' + (Core.secDone(st, s) ? ' ok' : '') }, el('i', { style: `width:${secPct(s)}%` })))),
      el('p', {}, `Unit Test: ${Core.attempts(st).length} attempt(s) · ${Core.passed(st) ? 'Passed' : 'not passed yet'} · Ranking score: ` + (rs ? rs.score.toFixed(2) + '% (' + rs.units + (rs.units === 1 ? ' unit)' : ' units)') : 'none yet')),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn small', href: '#result' }, 'Results & history'), el('a', { class: 'btn small', href: '#cert' }, '🎓 Certificate'), el('a', { class: 'btn small', href: '#board' }, '🏆 Leaderboard'))));
    m.append(testerTools());
    m.append(el('p', { class: 'muted' }, el('a', { href: '#privacy-kids' }, 'How Atomic looks after your data'), ' – the short version for learners.'));
  }

  /* ---------- leaderboard ---------- */
  const SAMPLE = [{ alias: 'Sample · Nova', score: 91.5, units: 14 }, { alias: 'Sample · Quark', score: 86.0, units: 14 }, { alias: 'Sample · Ion', score: 86.0, units: 14 }, { alias: 'Sample · Proton', score: 78.25, units: 14 }];
  async function viewBoard() {
    const m = $main();
    const hero = el('section', { class: 'lbhero' }); const hin = el('div', { class: 'in' }); hero.append(hin); document.getElementById('wrap').before(hero);
    const holder = el('div'); m.append(holder);
    const live = await Backend.leaderboard(7).catch(() => []);
    const rows = live.filter(r => r.score != null).map(r => ({ alias: r.nickname, score: Number(r.score), units: r.units, me: !!r.is_mine && st && r.nickname === st.alias, src: r.opted_in ? 'Shown' : 'Only you can see this' }));
    if (Backend.mode === 'demo') SAMPLE.forEach(r => rows.push({ ...r, src: 'sample data' }));
    Core.competitionRank(rows);
    hin.append(el('span', { class: 'eyebrow', style: 'color:#F3BF69' }, 'SCIENCE CAMBRIDGE STAGE 7'), el('h1', {}, '🏆 Leaderboard'),
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
  const ERR = { bad_email: 'Please enter a valid email address.', weak_password: 'Use at least 8 characters for your password.', email_taken: 'An account with this email already exists – sign in instead.',
    bad_credentials: 'That email and password do not match.', sign_in: 'Please sign in again.', parental_consent: 'Please tick the parental consent box.', bad_nickname: 'Use a nickname of 2–24 characters.',
    subscription_required: 'This needs a Cambridge Stage 7 plan.', locked: 'Finish every lesson or video and every Core question first.', awaiting_marking: 'Your last test is still being marked.', review_first: 'Finish your review questions first.',
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
    document.getElementById('wrap').before(el('section', { class: 'lp-hero dots' }, el('div', { class: 'lp-hero-in' },
      el('div', { class: 'lp-hero-txt' },
        el('span', { class: 'lp-pill' }, el('span', { class: 'lp-ping' }, el('i'), el('i')), 'Atomic Science · Checkpoint to A Level'),
        el('h1', {}, 'Try the whole course.', el('br'), el('span', {}, 'Right here, right now.')),
        el('p', {}, 'No sign-up. Watch a lesson, answer questions, sit a mini test and see your progress — all on this page.'),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn primary big shine', type: 'button', id: 'heroStart', onclick: scrollTry }, 'Start the tour ', el('span', { class: 'arr' }, '↓')),
          el('button', { class: 'btn big', type: 'button', id: 'heroGuest', onclick: startGuest }, 'Open topic 3.1'))),
      el('div', { class: 'lp-levels' }, el('span', { class: 'lp-eyebrow' }, 'OUR LEVELS'),
        level('7–9', 'Lower Secondary', 'Checkpoint · Stages 7, 8 and 9', 'Open now', true, startGuest),
        level('IG', 'Cambridge IGCSE', 'Biology · Chemistry · Physics', 'Coming soon'),
        level('A', 'AS & A Level', 'Biology · Chemistry · Physics', 'Coming soon')))));

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
        vid = el('video', { src: 'media/u3_s3.mp4', poster: 'media/u3_s3_poster.jpg', playsinline: true, preload: 'metadata', 'aria-label': 'Lesson video: specialised plant cells', class: 'lp-video' }); activeVideo = vid;
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
    const qa = [['Who is Atomic for?', 'Learners aged about 11–12 following Cambridge Lower Secondary Science Stage 7, at an international or bilingual school or studying at home.'],
      ['Do I need an account?', 'Not to try it: topic 3.1 is open to guests. Create a free account to save your progress, unlock every topic and take the Unit Test.'],
      ['Will my parents know how I am doing?', 'If you add a parent’s email when you sign up (it is optional), we send them a short email when you finish a unit. You can add or remove it any time in Settings.'],
      ['Am I on a public leaderboard?', 'Not unless you switch it on in Settings. Everyone is hidden by default, and only your nickname is ever shown.'],
      ['How are Unit Tests marked?', 'Multiple-choice, diagram and data questions are marked automatically. Written answers are marked by the Atomic teaching team; you get a notification when it is done.'],
      ['Can I delete my data?', 'Yes. In Settings you can download everything we hold about you or delete your account, which removes all your learning records.']];
    return el('section', { class: 'card' }, el('h2', {}, 'Questions'), ...qa.map(([q, a]) => el('details', { class: 'faq' }, el('summary', {}, q), el('p', {}, a))));
  }

  /* ---------- sign up (3 steps, Mathspace style) / sign in ---------- */
  const YEARS = ['Year 6 / Grade 5', 'Year 7 / Grade 6', 'Year 8 / Grade 7', 'Year 9 / Grade 8', 'Year 10 / Grade 9', 'Other'];
  async function schoolPicker(country, sel, other, value) {
    sel.innerHTML = ''; sel.append(el('option', { value: '' }, 'Loading schools…'));
    const list = country && country !== 'XX' ? await Backend.schools(country).catch(() => []) : [];
    sel.innerHTML = ''; sel.append(el('option', { value: '' }, list.length ? 'Choose your school' : 'No schools listed – type it below'));
    const grp = k => { const g = el('optgroup', { label: k === 'international' ? 'International schools' : 'Bilingual schools' }); list.filter(x => x.kind === k).forEach(x => g.append(el('option', { value: x.id }, x.name + (x.city ? ` (${x.city})` : '')))); return g.children.length ? g : null; };
    [grp('international'), grp('bilingual')].filter(Boolean).forEach(g => sel.append(g));
    sel.append(el('option', { value: 'other' }, 'My school isn’t listed'));
    if (value) sel.value = String(value); other.closest('label').hidden = sel.value !== 'other' && list.length > 0;
  }
  function viewSignup() {
    const m = $main(); const e = errBox(); const F = UI.su = UI.su || { step: 1 };
    const card = el('section', { class: 'card narrow signup' }); m.append(el('div', { class: 'authwrap dots' }, card)); document.getElementById('wrap').classList.add('authpage');
    const dots = () => el('div', { class: 'steps', 'aria-label': `Step ${F.step} of 3` }, ...[1, 2, 3].map(i => el('span', { class: i < F.step ? 'done' : i === F.step ? 'on' : '' }, String(i))));
    const next = () => { e.textContent = ''; F.step++; draw(); }, back = () => { e.textContent = ''; F.step--; draw(); };
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
        const by = el('select', { id: 'suYear' }, el('option', { value: '' }, 'Choose…'), ...Array.from({ length: 12 }, (_, i) => now - 8 - i).map(y => el('option', { value: y }, `${y} (about ${now - y} years old)`)));
        const gr = el('select', { id: 'suGrade' }, el('option', { value: '' }, 'Choose…'), ...YEARS.map(y => el('option', { value: y }, y)));
        by.value = F.birthYear || ''; gr.value = F.grade || '';
        card.append(dots(), el('h1', {}, 'About you'), el('p', { class: 'muted' }, 'This helps us check the course suits you. It is never shown to anyone.'),
          el('div', { class: 'form' }, field('Year of birth', by), field('School year', gr), e,
            el('div', { class: 'btnrow between' }, el('button', { class: 'btn ghost', type: 'button', onclick: back }, '← Back'),
              el('button', { class: 'btn primary', type: 'button', id: 'suNext2', onclick: () => { if (!by.value) { e.textContent = 'Please choose your year of birth.'; return; } if (!gr.value) { e.textContent = 'Please choose your school year.'; return; } Object.assign(F, { birthYear: Number(by.value), grade: gr.value }); next(); } }, 'Next', el('span', { class: 'arr' }, ' →')))));
      } else {
        const country = el('select', { id: 'suCountry' }, el('option', { value: '' }, 'Choose your country'), ...COUNTRIES.map(([v, t]) => el('option', { value: v }, t)));
        const school = el('select', { id: 'suSchool' }), other = el('input', { type: 'text', id: 'suSchoolOther', maxlength: 120, value: F.schoolOther || '' });
        const parent = el('input', { type: 'email', id: 'suParent', autocomplete: 'off', value: F.parentEmail || '', placeholder: 'optional' });
        const terms = el('input', { type: 'checkbox', id: 'suTerms' });
        country.value = F.country || ''; country.onchange = () => schoolPicker(country.value, school, other);
        school.onchange = () => { other.closest('label').hidden = school.value !== 'other'; };
        const b = el('button', { class: 'btn gold', type: 'button', id: 'suBtn', onclick: async () => {
          e.textContent = '';
          if (!country.value) { e.textContent = 'Please choose your country.'; return; }
          const sid = /^\d+$/.test(school.value) ? Number(school.value) : null;
          if (!sid && other.value.trim().length < 2) { e.textContent = 'Choose your school, or type its name.'; return; }
          const pe = parent.value.trim();
          if (pe && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(pe)) { e.textContent = 'That parent email does not look right – check it or leave it empty.'; return; }
          if (pe && pe.toLowerCase() === F.email.toLowerCase()) { e.textContent = 'The parent email must be different from your own.'; return; }
          if (!terms.checked) { e.textContent = 'Please agree to the Terms and the Privacy notice.'; return; }
          b.disabled = true;
          try {
            await Backend.signUp({ name: F.name, email: F.email, password: F.password, birthYear: F.birthYear, grade: F.grade, country: country.value, schoolId: sid, schoolOther: sid ? null : other.value.trim(), parentEmail: pe || null });
            const hadGuest = isGuest(); UI.su = null; await Core.boot(C); st = Core.cur();
            toast(hadGuest ? 'Account created – your guest progress is saved!' : 'Welcome to Atomic!'); confetti(); go('home');
          } catch (x) { e.textContent = errText(x); b.disabled = false; if (x && x.code === 'email_taken') { F.step = 1; } }
        } }, 'Create my account');
        card.append(dots(), el('h1', {}, 'Your school'), el('div', { class: 'form' }, field('Country', country), field('School', school, 'International and bilingual schools on Atomic.'), field('School name', other),
          field('Parent or guardian’s email (optional)', parent, 'If you add it, we send them one short email when you finish a unit – nothing else. You can change it in Settings.'),
          el('label', { class: 'check' }, terms, el('span', {}, 'I agree to the ', el('a', { href: '#terms', target: '_blank' }, 'Terms'), ' and have read the ', el('a', { href: '#privacy', target: '_blank' }, 'Privacy notice'), ' (', el('a', { href: '#privacy-kids', target: '_blank' }, 'short version'), ').')), e,
          el('div', { class: 'btnrow between' }, el('button', { class: 'btn ghost', type: 'button', onclick: back }, '← Back'), b)));
        schoolPicker(country.value, school, other, F.schoolId);
      }
      const f = card.querySelector('input,select'); if (f) f.focus();
    }
    draw();
  }
  function viewSignin() {
    const m = $main(); const e = errBox();
    const email = el('input', { type: 'email', id: 'siEmail', autocomplete: 'email' }), pw = el('input', { type: 'password', id: 'siPw', autocomplete: 'current-password' });
    const b = el('button', { class: 'btn primary', type: 'button', id: 'siBtn', onclick: async () => { e.textContent = ''; b.disabled = true;
      try { await Backend.signIn({ email: email.value, password: pw.value }); await Core.boot(C); st = Core.cur(); go('home'); } catch (x) { e.textContent = errText(x); b.disabled = false; } } }, 'Log in');
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
    const gr = el('select', { id: 'setGrade' }, el('option', { value: '' }, '—'), ...YEARS.map(y => el('option', { value: y }, y))); gr.value = l.grade || '';
    const country = el('select', { id: 'setCountry' }, ...COUNTRIES.map(([v, t]) => el('option', { value: v }, t))); country.value = l.country || 'XX';
    const school = el('select', { id: 'setSchool' }), other = el('input', { type: 'text', id: 'setSchoolOther', value: l.school_other || '', maxlength: 120 });
    const parent = el('input', { type: 'email', id: 'setParent', value: l.parent_email || '', placeholder: 'optional' });
    country.onchange = () => schoolPicker(country.value, school, other); school.onchange = () => { other.closest('label').hidden = school.value !== 'other'; };
    const save = el('button', { class: 'btn primary', type: 'button', id: 'setSave', onclick: async () => {
      e.textContent = ''; msg.textContent = '';
      const pe = parent.value.trim(); if (pe && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(pe)) { e.textContent = 'That parent email does not look right.'; return; }
      if (nick.value.trim().length < 2) { e.textContent = ERR.bad_nickname; return; }
      const sid = /^\d+$/.test(school.value) ? Number(school.value) : null;
      try { await Backend.updateLearner(l.id, { nickname: nick.value.trim(), certificate_name: full.value.trim() || null, grade: gr.value || null, school_id: sid, school_other: sid ? null : (other.value.trim() || null), parent_email: pe || null });
        await Core.refreshAccount(); const nl = Core.S.learners.find(x => x.id === l.id); if (nl) { st.learner = nl; st.alias = nl.nickname; st.name = nl.certificate_name || nl.nickname; } msg.textContent = 'Saved ✓'; } catch (x) { e.textContent = errText(x); }
    } }, 'Save changes');
    const lb = el('input', { type: 'checkbox', id: 'setBoard' }); lb.checked = !!l.leaderboard_opt_in;
    lb.onchange = () => { if (lb.checked) modal('Show me on the leaderboard?', 'Your nickname and ranking score will be visible to other Atomic learners. Nothing else is shown. You can switch this off at any time.', [{ t: 'Keep me hidden', cls: 'ghost', on: () => { lb.checked = false; } }, { t: 'Show my nickname', cls: 'primary', on: async () => { await Backend.updateLearner(l.id, { leaderboard_opt_in: true }); await Core.refreshAccount(); st.learner = Core.S.learners.find(x => x.id === l.id); } }]); else Backend.updateLearner(l.id, { leaderboard_opt_in: false }).then(async () => { await Core.refreshAccount(); st.learner = Core.S.learners.find(x => x.id === l.id); }); };
    pageHero('ACCOUNT', 'Settings', `Signed in as ${Core.S.me.user.email}`, statCard(initialChip(44), st.alias, l.grade || 'Cambridge Stage 7 learner'));
    m.append(
      el('section', { class: 'card' }, el('h2', {}, 'Profile'), el('div', { class: 'form' }, field('Nickname', nick, 'Shown in the app and, if you switch it on, on the leaderboard.'), field('Full name for the certificate', full), field('School year', gr), field('Country', country), field('School', school), field('School name', other))),
      el('section', { class: 'card' }, el('h2', {}, '📧 Parent or guardian'), el('div', { class: 'form' }, field('Parent or guardian’s email (optional)', parent, 'We send them one short email when you finish a unit. Leave empty to send nothing.'))),
      el('div', { class: 'btnrow' }, save, msg), e,
      el('section', { class: 'card' }, el('h2', {}, 'Leaderboard'), el('label', { class: 'switch' }, lb, el('span', {}, el('b', {}, 'Show me on the leaderboard'), el('br'), el('small', { class: 'muted' }, 'Off by default. Only your nickname and ranking score are shown.')))),
      el('section', { class: 'card' }, el('h2', {}, 'Your data'), el('p', {}, 'Download a copy of everything we hold about you, or delete your account and all learning records.'),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn small', type: 'button', id: 'exportBtn', onclick: async () => { const d = await Backend.exportData(); const r = await Core.saveFile('atomic-data-export.json', new Blob([JSON.stringify(d, null, 2)], { type: 'application/json' })); msg3.textContent = r === 'saved' ? 'Downloaded.' : 'Could not download.'; } }, '⬇ Download my data (JSON)'),
          el('button', { class: 'btn small ghost', type: 'button', id: 'deleteBtn', onclick: () => deleteAccountFlow() }, 'Delete account…')), el('p', { class: 'muted', id: 'msg3', 'aria-live': 'polite' })));
    const msg3 = m.querySelector('#msg3');
    schoolPicker(country.value, school, other, l.school_id || (l.school_other ? 'other' : ''));
  }
  function deleteAccountFlow() {
    const inp = el('input', { type: 'text', id: 'delConfirm', placeholder: 'DELETE MY ACCOUNT' }); const e = errBox();
    modal('Delete your account?', el('div', { class: 'form' }, el('p', {}, 'This deletes your account, all progress, tests and certificates. This cannot be undone.'), field('Type DELETE MY ACCOUNT to confirm', inp), e),
      [{ t: 'Cancel', cls: 'ghost' }, { t: 'Delete everything', cls: 'primary', on: async () => { try { await Backend.deleteAccount(inp.value.trim()); await Core.boot(C); st = null; go('home'); } catch (x) { e.textContent = errText(x); return true; } } }]);
  }

  /* ---------- plans & checkout ---------- */
  function viewPricing() {
    if (Core.BILLING_OFF) return viewBeta();
    const m = $main(); const L = (window.ATOMIC_CONFIG || {}).priceLabels || { monthly: '£9.99 / month', yearly: '£79 / year' }; const me = Core.S.me; const active = Core.S.sub.active;
    const plan = (id, name, price, pts, cta, hl) => el('div', { class: 'card plan' + (hl ? ' cur' : '') }, hl ? el('span', { class: 'tag adv' }, 'Best value') : null, el('h3', {}, name), el('div', { class: 'price' }, price), el('ul', {}, ...pts.map(p => el('li', {}, p))), cta);
    const buy = p => el('button', { class: 'btn ' + (p === 'yearly' ? 'gold' : 'primary'), type: 'button', id: 'buy-' + p, disabled: active, onclick: async () => {
      if (!me) { go('signup'); return; }
      if (Backend.mode === 'demo') modal('Checkout (preview)', el('div', {}, el('p', {}, `In the live site this opens Paddle checkout for the ${p} plan with a 7-day free trial. Paddle shows the local price and adds the right VAT/GST.`), el('p', { class: 'muted' }, 'Nothing is charged in this preview.')),
        [{ t: 'Cancel', cls: 'ghost' }, { t: 'Start free trial (preview)', cls: 'primary', on: async () => { await Backend.checkout(p); await Core.refreshAccount(); toast('Trial started – Cambridge Stage 7 unlocked'); go('u-' + Core.UNO); } }]);
      else await Backend.checkout(p);
    } }, active ? 'Your plan is active' : 'Start 7-day free trial');
    m.append(el('div', { style: 'text-align:center' }, el('span', { class: 'eyebrow' }, 'PLANS'), el('h1', { style: 'margin:4px 0' }, 'One plan, the whole of Cambridge Stage 7'), el('p', { class: 'muted' }, 'Cancel any time.')),
      el('div', { class: 'plans' }, plan('free', 'Free', '£0', ['First topic of every unit', 'Lesson videos with pause questions', '30 practice questions for that topic', 'Learning streak and progress report'], me ? el('a', { class: 'btn', href: '#home' }, 'Keep learning free') : el('a', { class: 'btn', href: '#signup' }, 'Start free')),
        plan('monthly', 'Cambridge Stage 7 – monthly', L.monthly, ['All 4 topics of every unit', 'Unit Tests marked by Atomic', 'A4 worksheets and concept maps', 'Cambridge Stage 7 certificate'], buy('monthly')),
        plan('yearly', 'Cambridge Stage 7 – yearly', L.yearly, ['Everything in monthly', 'About 2 months free', 'Price fixed for the year'], buy('yearly'), true)),
      el('p', { class: 'muted', style: 'text-align:center' }, 'Prices shown in GBP for guidance. At checkout Paddle, our reseller, shows the price in your currency including VAT/GST where it applies (UK VAT, Singapore GST, Malaysia SST, Thailand VAT, Vietnam, Indonesia and Philippines taxes).'), faq());
  }

  function viewBeta() {
    const m = $main(); const me = Core.S.me;
    m.append(narrow(el('span', { class: 'eyebrow' }, 'TEST PHASE'), el('h1', {}, 'Free while we test'), el('p', {}, 'Atomic is in a small private test. Every learner gets the whole Cambridge Stage 7 course – videos, practice, Unit Tests and the certificate – free of charge. No card is needed.'),
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
    m.append(narrow(el('h1', {}, 'Verify a certificate'), el('p', { class: 'muted' }, 'Enter the code printed on an Atomic certificate.'), el('div', { class: 'form' }, field('Certificate code', code),
      el('button', { class: 'btn primary', type: 'button', id: 'vfBtn', onclick: async () => { const r = await Backend.verifyCertificate(code.value); out.innerHTML = ''; out.append(r ? el('div', { class: 'banner ok' }, `✓ Genuine: ${r.name_on_certificate} completed the Atomic Education course for Cambridge Stage ${r.stage} Science on ${String(r.issued_at).slice(0, 10)}.`) : el('div', { class: 'banner adv' }, 'No certificate has this code.')); } }, 'Check'), out)));
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
    ['Who we are', 'Atomic Education (“Atomic”, “we”) runs the Atomic Checkpoint courses. Contact: ' + (((window.ATOMIC_CONFIG || {}).supportEmail) || 'support@example.com') + '.'],
    ['Who this notice is for', 'Learners who use Atomic and their parents or guardians.', ['A short version written for learners (see ', ['a', 'privacy-kids', 'For learners'], ').']],
    ['What we collect and why', ['Guests: nothing is sent to us. A guest’s progress is kept only in their own browser until they create an account.',
      'Account: name, email, password (stored hashed by our authentication provider), year of birth, school year, country and school – to run the account, check the course suits you and apply the right law.',
      'Optional parent or guardian email: used only to send one short email when the learner finishes a unit. It can be changed or removed at any time in Settings.',
      'Learning records: answers, progress, test results – to give feedback, mark tests, show progress and issue certificates.',
      'Payments (later, not during the test phase): handled by Paddle as Merchant of Record; we receive only the subscription status, not card details.']],
    ['High privacy by default', 'We follow the UK Age Appropriate Design Code (Children’s code): we collect the minimum, there is no advertising and no profiling for advertising, no geolocation and no public profile. Learners are hidden from the leaderboard unless they switch it on, and then only the nickname is shown.'],
    ['Where data is stored', 'Our database and authentication run on Supabase; the website runs on Vercel; emails will be sent by an email provider such as Resend. Data may be processed outside your country; we use contractual safeguards for international transfers.'],
    ['How long we keep data', 'While the account is open. When you delete the account, all your data is deleted at once; backups are overwritten within 30 days.'],
    ['Children and consent', 'Several of our markets require a parent’s or guardian’s consent before a child’s personal data is used (for example Singapore under 13, Vietnam under 16, Malaysia, Indonesia and the Philippines under 18, Thailand for younger minors). During the test phase learners sign up themselves; before Atomic is offered commercially we will add the parental-consent step each country requires. If you are a parent and want your child’s account removed, contact us and we will delete it.'],
    ['Your rights', 'Download a copy of your data or delete your account at any time from Settings. You can also ask us to correct data, object to or restrict processing, or complain to your data protection authority (UK: ICO; Singapore: PDPC; Vietnam: the Ministry of Public Security’s data protection authority).']]);
  function viewKidsPrivacy() {
    const m = $main(); const row = (i, t, d) => el('div', { class: 'card', style: 'display:flex;gap:14px;align-items:flex-start' }, el('span', { style: 'font-size:28px' }, i), el('div', {}, el('b', { class: 'lex' }, t), el('p', { style: 'margin:4px 0 0' }, d)));
    m.append(el('div', { style: 'max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:14px' }, el('span', { class: 'eyebrow' }, 'FOR LEARNERS'), el('h1', { style: 'margin:0' }, 'Your data at Atomic – the short version'),
      row('🙂', 'We only ask for what we need', 'Your name, email, age, school year and school. We never ask for your address, photo or where you are.'),
      row('📝', 'We keep your answers to help you learn', 'Your answers, scores and progress let us give you hints, mark your tests and show you how you are doing.'),
      row('📧', 'Your parent’s email is up to you', 'If you add it, we only send them a short message when you finish a unit.'),
      row('🙈', 'You are hidden on the leaderboard', 'Nobody else sees you unless you switch it on. Even then, they only see your nickname and score.'),
      row('🚫', 'No adverts, no selling', 'We never show you adverts and we never sell your information to anyone.'),
      row('🗑️', 'You can delete it', 'In Settings you can download or delete everything at any time.'),
      row('💬', 'Worried about something?', 'Talk to a grown-up you trust, or contact us through Help.'),
      el('p', { class: 'muted' }, 'This is a short summary of our ', el('a', { href: '#privacy' }, 'Privacy notice'), '.')));
  }
  const viewTerms = () => legal('Terms of use', [
    ['The service', 'Atomic provides online science courses for Cambridge Lower Secondary Science Stage 7 learners. Courses are written by Atomic and aligned to the Cambridge Lower Secondary Science curriculum framework (0893). Atomic is not affiliated with or endorsed by Cambridge University Press & Assessment.'],
    ['Who the course is for', 'The Cambridge Stage 7 course is designed for learners aged about 11 to 13. Anyone can try topic 3.1 as a guest. Learners create their own free account to save progress.'],
    ['Accounts', 'One account per learner. Keep your password private. If you are under the age of digital consent where you live, ask a parent or guardian before you sign up.'],
    ['Plans, trials and refunds', 'Plans renew automatically until cancelled. A free trial converts to a paid plan unless cancelled before it ends. Our order process is conducted by our online reseller Paddle.com, the Merchant of Record for all orders; Paddle provides customer service enquiries and handles returns.'],
    ['Fair use', 'Course content is for your own personal learning. Do not copy, share or resell videos, questions, tests or worksheets.'],
    ['Tests and certificates', 'Unit Tests and exams are marked automatically, including typed answers. A certificate confirms completion of the Atomic Stage 7 course; it is not a Cambridge qualification.'],
    ['Changes and contact', 'We will tell you about important changes by email. Questions: ' + (((window.ATOMIC_CONFIG || {}).supportEmail) || 'support@example.com') + '.']]);
  const viewCookies = () => legal('Cookies and local storage', [
    ['What we use', 'Only what the site needs to work: keeping you signed in, and keeping a guest’s progress on this device until they sign up. We do not use advertising or third-party tracking cookies, so we do not show a cookie banner.'],
    ['Payments', 'When you open checkout, Paddle may set cookies needed for secure payment and fraud prevention. See Paddle’s own cookie notice.']]);

  /* ---------- staff: marking, reports, item statistics ---------- */
  async function viewStaff() {
    const m = $main(); const role = Core.S.me && Core.S.me.profile.role;
    if (!['marker', 'admin'].includes(role)) { m.append(narrow(el('h1', {}, 'Staff area'), el('p', {}, 'This area is for Atomic markers and administrators.'), Backend.demo ? el('button', { class: 'btn small', type: 'button', id: 'becomeStaff', onclick: () => { Backend.demo.setRole('admin'); Core.refreshAccount().then(render); } }, 'Preview: make this account an administrator') : null)); return; }
    const tab = UI.staffTab || 'marking';
    m.append(el('h1', { style: 'margin:0' }, 'Staff'), el('div', { class: 'btnrow', role: 'tablist' }, ...[['marking', 'Marking queue'], ['reports', 'Question reports'], ['items', 'Question statistics']].map(([k, t]) => el('button', { class: 'chip' + (tab === k ? ' on' : ''), type: 'button', role: 'tab', onclick: () => { UI.staffTab = k; render(); } }, t))));
    if (tab === 'marking') {
      const q = await Backend.markingQueue();
      if (!q.length) { m.append(el('p', { class: 'muted', id: 'noPending' }, 'Nothing is waiting to be marked.')); return; }
      q.forEach(a => { const inputs = {};
        const box = el('section', { class: 'card' }, el('h3', {}, `${a.learner} · Paper ${a.form} · attempt ${a.n}`), el('small', { class: 'muted' }, 'Submitted ' + new Date(a.submitted).toLocaleString('en-GB')));
        a.items.forEach(it => { const inp = el('input', { type: 'number', min: 0, max: it.max, step: 0.5, class: 'numin s', value: it.suggest }); inputs[it.id] = inp;
          box.append(el('div', { class: 'sol' }, el('p', {}, el('b', {}, it.prompt)), el('blockquote', {}, it.answer || '(left blank)'), el('ul', {}, ...it.rubric.map(r => el('li', {}, r))), el('p', { class: 'muted' }, 'Model: ' + it.model), el('label', {}, `Mark (0–${it.max}; suggested from key words): `, inp))); });
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
  const TOC_ROUTES = r => r.startsWith('v-') || r.startsWith('ex-') || r.startsWith('ws-') || /^u-\d+$/.test(r) || ['map', 'result', 'remedial', 'topic', 'drill', 'cert', 'unit'].includes(r);
  const PUBLIC = { home: () => viewHome(), signin: viewSignin, signup: viewSignup, forgot: viewForgot, pricing: viewPricing, help: viewHelp, privacy: viewPrivacy, 'privacy-kids': viewKidsPrivacy, terms: viewTerms, cookies: viewCookies, verify: viewVerify };
  const ACCOUNT = { staff: viewStaff, teacher: viewStaff };
  const LEARNER = { home: viewHome, unit: viewUnit, test: viewTest, tests: viewTests, final: viewFinal, checkpoint: viewCheckpoint, level: viewLevel, result: viewResult, remedial: viewRemedial, map: viewMap, profile: viewProfile, topic: viewTopic, bank: viewBank, drill: viewDrill, board: viewBoard, cert: viewCert, settings: viewSettings };
  const GUEST_WALL = { board: 'Sign up free to join the leaderboard', cert: 'Sign up free to earn a certificate', result: 'Sign up free to take the Unit Test', remedial: 'Sign up free to take the Unit Test', settings: 'Sign up free to get your own account' };
  let renderSeq = 0;
  async function render() {
    if (activeVideo) { try { activeVideo.pause(); } catch (e) { } activeVideo = null; }
    clearInterval(timer); const seq = ++renderSeq;
    let r = location.hash.slice(1) || 'home';
    if (Guard.on && r !== Guard.route) { location.replace('#' + Guard.route); leave('navigate'); return; }   // Back / links are closed during an exam
    if (r === 'unit3') { location.replace('#u-3'); return; }
    // the unit is part of the address: u-4, v-4-1, ex-4-2, ws-4-3
    const um = r.match(/^u-(\d+)$/) || r.match(/^(?:v|ex|ws)-(\d+)-\d+$/);
    if (um && Number(um[1]) !== Core.UNO) { if (!Core.unitReady(Number(um[1]))) { location.replace('#home'); return; } try { await Core.switchUnit(Number(um[1])); } catch (e) { location.replace('#home'); return; } if (seq !== renderSeq) return; }
    C = Core.C; st = Core.cur(); if (/^u-\d+$/.test(r)) r = 'unit';
    if (r !== 'test' && !/^(fx|cpx)-/.test(r)) UI.testOn = false;
    document.body.classList.remove('menu-open', 'toc-open');
    const me = Core.S.me;
    const needsLearner = !!LEARNER[r] && r !== 'home' || /^(v|ex|ws)-/.test(r) || /^(stage|checkout|fx|fres)-\d+$/.test(r) || /^(cpx|cpr)-[A-Z]{1,2}\d$/.test(r);
    const freeTopic = /^(v|ex|ws)-\d+-1$/.test(location.hash.slice(1)) || r === 'unit';
    if (['learners', 'add-learner', 'parent'].includes(r)) { location.replace('#home'); return; }   // old parent-area links
    if (!me && !st && (ACCOUNT[r] || needsLearner)) { if (freeTopic) { Core.startGuest(); st = Core.cur(); } else { location.replace('#signin'); return; } }  // a link into topic 3.1 starts a guest session
    if (!me && ACCOUNT[r]) { location.replace('#signin'); return; }
    if (me && !st && needsLearner) { location.replace('#home'); return; }
    if (me && (r === 'signin' || r === 'signup')) { location.replace('#home'); return; }
    shell({ toc: TOC_ROUTES(r) }); const m = $main();
    try {
      const pm = r.match(/^(stage|checkout|fx|fres)-(\d+)$/); const cpm = r.match(/^(cpx|cpr)-([A-Z]{1,2}\d)$/);
      if (r.startsWith('v-')) viewVideo(secFromRoute(r)); else if (r.startsWith('ex-')) viewExercises(secFromRoute(r)); else if (r.startsWith('ws-')) viewWorksheet(secFromRoute(r));
      else if (/^courses(-\w+)?$/.test(r)) await viewCourses(r.split('-')[1]);
      else if (/^course-[a-z0-9-]+$/.test(r)) await viewCourse(r.slice(7));
      else if (cpm && st) { if (cpm[1] === 'cpx') await viewCpExam(cpm[2]); else await viewCpResult(cpm[2]); }
      else if (pm && st) { if (isGuest() && pm[1] !== 'stage') m.append(guestWall('Sign up free to continue')); else if (pm[1] === 'stage') await viewStage(+pm[2]); else if (pm[1] === 'checkout') viewCheckout(+pm[2]); else if (pm[1] === 'fx') await viewFinalExam(pm[2]); else await viewFinalResult(pm[2]); }
      else if (st && isGuest() && GUEST_WALL[r]) m.append(guestWall(GUEST_WALL[r]));
      else if (st && LEARNER[r]) await LEARNER[r](); else if (ACCOUNT[r]) await ACCOUNT[r](); else if (PUBLIC[r]) await PUBLIC[r](); else viewHome();
    } catch (e) { console.error(e); if (seq === renderSeq) m.append(el('div', { class: 'banner adv', role: 'alert' }, 'Something went wrong loading this page. ', el('button', { class: 'btn small', type: 'button', onclick: () => render() }, 'Try again'))); }
    if (seq !== renderSeq) return;
    if (r === 'staff') document.title = 'Atomic – Staff'; else document.title = `Atomic – Cambridge ${Core.stageLabel()}`;
    m.focus({ preventScroll: true }); window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', render);
  async function boot() {
    try {
      if (Backend.demo && location.search.includes('reset')) Backend.demo.reset();
      await Core.boot(); C = Core.C;
    } catch (e) { console.error(e); document.getElementById('app').innerHTML = '<p style="padding:24px;font-family:sans-serif">Sorry – the course could not load. Please check your connection and reload the page.</p>'; return; }
    render();
  }
  window.AtomicApp = { render, go, get st() { return st; }, UI, get C() { return C; } };
  boot();
})();
