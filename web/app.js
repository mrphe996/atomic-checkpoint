/* Atomic Education — Science Stage 7. Views and routing (v3: student accounts, guest mode, bolts and shop, server marking).
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
  const unitIcon = n => { const i = IC[n]; const sp = el('span', { class: 'ic', style: `background:${i.bg}`, 'aria-hidden': 'true' }); sp.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24"><path d="${i.a}" fill="${i.c}"/><path d="${i.o}" fill="none" stroke="#013A8C" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>`; return sp; };
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
  const BOLT = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2L4 14h7l-1 8 9-12h-7z" fill="#F3BF69" stroke="#B7791F" stroke-width="1.4" stroke-linejoin="round"/></svg>';
  function xpTick() { if (!st) return; const p = document.getElementById('xpPill'); if (p) p.lastChild.textContent = Core.bolts(st).toLocaleString('en-GB'); const g = document.getElementById('goalBar'); if (g) g.style.width = Math.min(100, Core.earnedToday(st) / Core.DAILY_GOAL * 100) + '%'; }
  Core.setOnEarn((n, why) => { toast(why === 'streak' ? `🔥 Streak bonus! +${n} ⚡` : `+${n} ⚡`); setTimeout(xpTick, 0); });
  // the learner's look: avatar + accessory on their background
  function avatarEl(size, extra) {
    const lk = Core.look(st); const a = el('span', { class: 'mascot' + (extra ? ' ' + extra : ''), style: `width:${size}px;height:${size}px;font-size:${Math.round(size * .55)}px;background:${lk.background.css}`, 'aria-hidden': 'true' }, lk.avatar.icon);
    if (lk.accessory) a.append(el('span', { class: 'acc', style: `font-size:${Math.round(size * .32)}px` }, lk.accessory.icon));
    return a;
  }
  const isGuest = () => !!Core.S.guest;
  function startGuest() { Core.startGuest(); st = Core.cur(); toast('Welcome! You are learning as a guest.'); go('v-3-1'); }
  function guestWall(title) {
    return el('section', { class: 'card lockcard', id: 'guestWall' }, el('h2', {}, '✨ ' + title), el('p', {}, 'Create a free account to unlock every topic, take the Unit Test, join the leaderboard and keep your ⚡ bolts. What you have done as a guest comes with you.'),
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
    const area = r.startsWith('v-') || r.startsWith('ex-') || r.startsWith('ws-') || r === 'unit3' || r === 'map' ? 'course' : r === 'bank' || r === 'topic' || r === 'drill' ? 'bank' : r === 'test' || r === 'result' || r === 'remedial' ? 'test' : r === 'profile' || r === 'cert' ? 'profile' : r === 'board' ? 'board' : r === 'home' ? 'home' : r;
    const right = el('span', { class: 'topright' });
    let nav;
    if (st) {
      const sk = Core.streak(st);
      const s = el('a', { class: 'pill streak', href: '#home', title: `${sk}-day streak`, 'aria-label': `${sk}-day streak` }); s.innerHTML = FLAME; s.append(String(sk));
      const x = el('a', { class: 'pill xp bolts', id: 'xpPill', href: '#shop', title: 'Bolts – spend them in the shop', 'aria-label': 'Bolts' }); x.innerHTML = BOLT; x.append(Core.bolts(st).toLocaleString('en-GB'));
      if (isGuest()) right.append(s, x, el('a', { class: 'btn small ghost', href: '#signin', id: 'signInLink' }, 'Log in'), el('a', { class: 'btn small gold', href: '#signup', id: 'signUpLink' }, 'Sign up free'));
      else {
        const menu = el('div', { class: 'usermenu', hidden: true, id: 'userMenu' }, el('b', {}, st.name), el('a', { href: '#profile' }, '📈 My progress'), el('a', { href: '#shop' }, '🛍️ Shop'), el('a', { href: '#settings', id: 'settingsLink' }, '⚙️ Settings'),
          ['marker', 'admin'].includes(me.profile.role) ? el('a', { href: '#staff' }, '🧑‍🏫 Staff') : null,
          el('button', { type: 'button', id: 'signOut', onclick: async () => { Core.flush(); await Backend.signOut(); await Core.boot(C); st = null; go('home'); } }, '↩ Sign out'));
        const av = el('button', { class: 'avatarbtn', type: 'button', id: 'whoBtn', 'aria-label': 'Account menu', 'aria-haspopup': 'true', onclick: ev => { ev.stopPropagation(); menu.hidden = !menu.hidden; } }, avatarEl(38));
        document.addEventListener('click', () => { menu.hidden = true; }, { once: true });
        right.append(s, x, bell(), el('span', { class: 'userwrap' }, av, menu));
      }
      nav = [navLink('home', 'Dashboard', area === 'home'), navLink('unit3', 'Courses', area === 'course'), navLink('bank', 'Question Bank', area === 'bank'), navLink('test', 'Unit Test', area === 'test'), navLink('shop', 'Shop', area === 'shop'), navLink('board', 'Leaderboard', area === 'board')];
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
      el('p', { class: 'muted disclaimer' }, 'Atomic courses are written by Atomic Education and aligned to the Cambridge Lower Secondary Science curriculum framework (0893). Atomic is not affiliated with or endorsed by Cambridge University Press & Assessment.')));
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
  function toc() {
    const route = location.hash.slice(1); const wrap = el('div', { style: 'display:flex;flex-direction:column;gap:12px' });
    wrap.append(el('div', { class: 'card lvl' }, el('span', { class: 'h' }, 'LEVEL'), el('div', { class: 'it on' }, 'Lower Secondary'),
      el('div', { class: 'it', title: 'Coming soon' }, 'Cambridge IGCSE ', svgI(I.lock, 15, '#8B98AB', 2)), el('div', { class: 'it', title: 'Coming soon' }, 'AS & A Level ', svgI(I.lock, 15, '#8B98AB', 2))));
    wrap.append(el('div', { class: 'stagechips', role: 'group', 'aria-label': 'Stage' }, el('span', { class: 'chip on' }, 'Stage 7'), el('span', { class: 'chip dim', title: 'Opens after approval' }, 'Stage 8'), el('span', { class: 'chip dim', title: 'Opens after approval' }, 'Stage 9')));
    const units = el('div', { class: 'units' });
    C.course.units.forEach(u => {
      const us = Core.unitStatus(st, u.n);
      if (u.n !== 3) {
        const why = u.n === 4 && us === 'locked' ? 'Locked: pass Unit Test 3 (above 70%)' : us === 'unlocked' ? 'Unlocked – content arrives once the Unit 3 pilot is approved' : us === 'sim' ? 'Simulated: passed (preview tool)' : 'Not in this preview';
        units.append(el('div', { class: 'unit', title: why }, unitIcon(u.n), el('span', {}, `${u.n}. ${u.t}`), us === 'sim' ? el('span', { class: 'lk', style: 'color:#1E8E4E;font-weight:800' }, '✓') : us === 'unlocked' ? el('span', { class: 'lk' }, '🔓') : el('span', { class: 'lk' }, svgI(I.lock, 14, '#8B98AB', 2))));
        return;
      }
      units.append(el('a', { class: 'unit on', href: '#unit3', 'aria-current': route === 'unit3' ? 'page' : null }, unitIcon(3), el('span', {}, '3. Cells')));
      const sn = el('div', { class: 'secnav' });
      C.sections.forEach(s => {
        const lock = Core.secLock(st, s), done = Core.secDone(st, s), vd = Core.videoDone(st, s), rl = Core.reqLeft(st, s).length;
        sn.append(el('div', { class: 'sh' + (lock ? ' locked' : '') }, lock ? '🔒 ' : done ? '✓ ' : '', `${s.id} ${s.title}`));
        const link = (r, label, ok) => el('a', { href: '#' + r, class: route === r ? 'on' : '' }, el('span', { class: 'st' + (ok ? ' ok' : '') }, ok ? '✓' : ''), label);
        if (lock) sn.append(el('div', { class: 'why' }, lock.reason));
        else sn.append(link('v-' + R(s.id), 'Watch', vd), link('ex-' + R(s.id), `Practise · ${8 - rl}/8 Core`, rl === 0), link('ws-' + R(s.id), 'Worksheet', st.ws.includes(s.id)));
      });
      const ts = Core.testState(st);
      sn.append(el('a', { href: '#test', class: route === 'test' ? 'on' : '' }, el('span', { class: 'st' + (ts.state === 'passed' ? ' ok' : '') }, ts.state === 'passed' ? '✓' : '★'), ts.state === 'locked' ? 'Unit Test 3 (locked)' : 'Unit Test 3'));
      units.append(sn);
    });
    wrap.append(units, el('div', { class: 'card tocfoot' }, el('a', { href: '#map' }, '🧠 Concept map'), el('a', { href: '#result' }, '📊 Results & history'), el('a', { href: '#bank' }, '🗂 Question Bank')));
    return wrap;
  }
  function refreshToc() { const t = document.querySelector('.toc'); if (t && st && t.childElementCount) { t.innerHTML = ''; t.append(toc()); } }
  function goNext(nx) { go(nx.route, nx.tab ? { tab: { ...UI.tab, [nx.route]: nx.tab }, idx: { ...UI.idx, [nx.route + nx.tab]: nx.idx } } : null); }
  /* where am I / what remains / next button (shown on every learning screen) */
  function bar(where) {
    const left = []; let vids = 0, reqs = 0;
    C.sections.forEach(s => { if (!Core.videoDone(st, s)) vids++; reqs += Core.reqLeft(st, s).length; });
    if (vids) left.push(`${vids} video`); if (reqs) left.push(`${reqs} Core questions`); if (!Core.passed(st)) left.push('Unit Test');
    const nx = Core.nextActivity(st);
    return el('div', { class: 'where' }, el('div', {}, el('small', {}, 'You are here'), el('b', {}, where)),
      el('div', {}, el('small', {}, 'Still to do in Unit 3'), el('b', {}, left.length ? left.join(' · ') : 'All done 🎉')),
      el('button', { class: 'btn gold small', type: 'button', id: 'nextBtn', onclick: () => goNext(nx) }, 'Next: ' + nx.label, el('span', { class: 'arr' }, ' →')));
  }
  function lockScreen(title, reason, items) {
    return el('section', { class: 'card lockcard' }, el('h2', {}, el('span', { class: 'lockicon' }, '🔒'), ' ' + title), el('p', {}, reason),
      el('ul', { class: 'misslist' }, ...items.map(m => el('li', {}, el('span', {}, 'You still need to do ', el('b', {}, m.what)), el('button', { class: 'btn small primary', type: 'button', onclick: () => goNext(m) }, 'Go there', el('span', { class: 'arr' }, ' →'))))));
  }
  function subbar(cls, ...kids) { const s = document.getElementById('sub'); s.className = 'subbar ' + (cls || ''); s.append(el('div', { class: 'subbar-in' }, ...kids)); }
  const secPct = s => ((Core.videoDone(st, s) ? 1 : 0) * 0.3 + (8 - Core.reqLeft(st, s).length) / 8 * 0.7) * 100;
  const unitPct = () => { const p = C.sections.reduce((a, s) => a + secPct(s), 0) / 4; return Math.round(Core.passed(st) ? 100 : p * 0.9); };
  const objSecure = o => { const qs = C.sections.flatMap(s => s.req).filter(q => q.obj === o); return qs.length && qs.every(q => (st.items[q.id] || {}).ok); };

  /* ---------- home (dashboard) ---------- */
  function viewHome() {
    const m = $main();
    if (!st) { if (Core.S.me) { m.append(narrow(el('h1', {}, 'Welcome'), el('p', {}, 'This account has no learner profile.'), ['marker', 'admin'].includes(Core.S.me.profile.role) ? el('a', { class: 'btn primary', href: '#staff' }, 'Open Staff') : el('a', { class: 'btn', href: '#help' }, 'Contact us'))); return; } viewLanding(); return; }
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
    const today = Core.earnedToday(st), goal = Core.DAILY_GOAL, sk = Core.streak(st);
    const weekStrip = el('div', { class: 'week', 'aria-label': 'This week' }, ...Core.week(st).map(d => el('span', { class: 'wd' + (d.met ? ' met' : '') + (d.today ? ' today' : ''), title: d.d }, el('i', {}, d.met ? '⚡' : ''), el('small', {}, d.label))));
    const heroS = el('section', { class: 'hero small dash' }, el('div', { class: 'hero-in' }, el('div', { class: 'txt' }, el('span', { class: 'eyebrow' }, isGuest() ? 'GUEST · TRY TOPIC 3.1' : 'DASHBOARD'),
      el('h1', {}, isGuest() ? 'Welcome to Atomic! 👋' : `Hello, ${st.alias}! 👋`), el('p', {}, started ? 'You\'ll pick up exactly where you left off.' : 'Start with Unit 3: Cells – section 3.1. Answer questions to earn ⚡ bolts.'),
      el('div', { class: 'btnrow' }, el('button', { class: 'btn gold big shine', type: 'button', id: 'resumeBtn', onclick: started ? resume : () => go('v-3-1') }, svgI(I.play, 18, '#0149AF', 2.6), started ? 'Continue learning' : 'Start learning'),
        el('span', { style: 'color:#DCE8FA' }, 'Next: ', el('b', { style: 'color:#fff' }, nx.label)))),
      el('div', { class: 'goalcard' }, avatarEl(96, 'bob'),
        el('div', { class: 'goaltxt' }, el('b', {}, today >= goal ? '🎉 Daily goal reached!' : `Daily goal: ${Math.min(today, goal)} / ${goal} ⚡`), el('div', { class: 'pbar gold' }, el('i', { id: 'goalBar', style: `width:${Math.min(100, today / goal * 100)}%` })),
          el('small', {}, sk ? `🔥 ${sk}-day streak – earn ${goal} ⚡ every day to keep it` : `Earn ${goal} ⚡ today to start a streak`), weekStrip))));
    document.getElementById('wrap').before(heroS);
    const ts = Core.testState(st);
    if (isGuest()) m.append(el('div', { class: 'banner info', id: 'guestBanner' }, el('b', {}, 'You are learning as a guest. '), 'Your progress is kept on this device only and topic 3.1 is open. Sign up free to save it, unlock every topic and keep your bolts.', el('a', { class: 'btn small gold', href: '#signup' }, 'Sign up free')));
    else if (!Core.S.sub.active) m.append(el('div', { class: 'banner info', id: 'freeBanner' }, el('b', {}, 'Free plan: '), 'topic 3.1 is open. A Stage 7 plan unlocks all topics and the Unit Test.', el('a', { class: 'btn small gold', href: '#pricing' }, 'See plans')));
    if (Backend.mode === 'demo' && !isGuest()) m.append(el('div', { class: 'banner adv' }, el('b', {}, 'Trying the preview? '), 'Use the tester tools on the Progress page to unlock sections instantly and test the Unit Test, certificate and leaderboard.', el('a', { class: 'btn small', href: '#profile' }, 'Open tester tools')));
    // daily challenges + shop teaser, side by side
    const ch = Core.challenges(st);
    const chCard = el('section', { class: 'card challenges', id: 'challenges' }, el('div', { class: 'btnrow between', style: 'margin:0' }, el('h2', { style: 'margin:0' }, '🎯 Daily challenges'), el('small', { class: 'muted' }, 'New ones every day')),
      ...ch.map(c => el('div', { class: 'chal' + (c.claimed ? ' claimed' : c.done ? ' ready' : '') }, el('div', { class: 'ct' }, el('b', {}, c.label), el('div', { class: 'pbar' }, el('i', { style: `width:${c.value / c.goal * 100}%` })), el('small', { class: 'muted' }, `${c.value} / ${c.goal}`)),
        c.claimed ? el('span', { class: 'status done' }, '✓ Claimed') : el('button', { class: 'btn small ' + (c.done ? 'gold shine' : ''), type: 'button', disabled: !c.done, 'data-claim': c.id, onclick: () => { const n = Core.claim(st, c.id); if (n) { toast(`Challenge complete! +${n} ⚡`); confetti(); render(); } } }, `+${c.reward} ⚡`))));
    const cheapest = Core.ITEMS.filter(i => i.price > 0 && !Core.owns(st, i.id)).sort((a, b) => a.price - b.price)[0];
    const shopCard = el('section', { class: 'card shopteaser' }, el('h2', { style: 'margin:0' }, '🛍️ Shop'), el('div', { class: 'bal' }, el('span', { html: BOLT.replace(/16/g, '28') }), el('b', {}, Core.bolts(st).toLocaleString('en-GB')), el('small', { class: 'muted' }, 'bolts to spend')),
      cheapest ? el('p', { class: 'muted', style: 'margin:0' }, `Next up: ${cheapest.icon} ${cheapest.name} for ${cheapest.price} ⚡`) : el('p', { class: 'muted' }, 'You own everything – amazing!'),
      el('a', { class: 'btn primary small', href: '#shop', id: 'openShop' }, 'Open the shop', el('span', { class: 'arr' }, '→')));
    m.append(el('div', { class: 'dashgrid' }, chCard, shopCard));
    m.append(el('div', { class: 'tiles' },
      statTile('🔥', `${sk} day${sk === 1 ? '' : 's'}`, 'Learning streak'),
      statTile('⚡', `${Core.bolts(st).toLocaleString('en-GB')}`, 'Bolts to spend'),
      statTile('🎯', `${C.sections.reduce((a, s) => a + 8 - Core.reqLeft(st, s).length, 0)}/32`, 'Core questions done'),
      statTile('★', isGuest() ? 'Sign up' : ts.state === 'passed' ? 'Passed' : ts.state === 'locked' ? 'Locked' : ts.state === 'pending' ? 'Awaiting marking' : 'Ready', 'Unit Test 3')));
    m.append(el('h2', { style: 'margin:8px 0 0' }, 'What\'s next today?'), learningPath());
  }

  /* ---------- shop ---------- */
  function viewShop() {
    const m = $main(); const tab = UI.shopTab || 'avatar';
    const tabs = [['avatar', 'Avatars'], ['accessory', 'Accessories'], ['background', 'Backgrounds']];
    m.append(el('section', { class: 'card shophead' }, avatarEl(120, 'bob'), el('div', {}, el('span', { class: 'eyebrow' }, 'SHOP'), el('h1', { style: 'margin:0' }, 'Spend your bolts'),
      el('p', { class: 'muted', style: 'margin:4px 0 0' }, 'Earn ⚡ by watching lessons and answering questions – right first time earns the most. Daily challenges and streaks give bonus bolts.'),
      el('div', { class: 'bal' }, el('span', { html: BOLT.replace(/16/g, '28') }), el('b', { id: 'shopBal' }, Core.bolts(st).toLocaleString('en-GB')), el('small', { class: 'muted' }, 'bolts')))));
    m.append(el('div', { class: 'tabs', role: 'tablist' }, ...tabs.map(([k, t]) => el('button', { class: 'tab' + (k === tab ? ' on' : ''), type: 'button', role: 'tab', 'aria-selected': k === tab ? 'true' : 'false', onclick: () => { UI.shopTab = k; render(); } }, t))));
    const eq = Core.shop(st).equip;
    m.append(el('div', { class: 'shopgrid', id: 'shopGrid' }, ...Core.ITEMS.filter(i => i.kind === tab).map(it => {
      const owned = Core.owns(st, it.id), on = eq[it.kind] === it.id, short = Core.bolts(st) < it.price;
      const btn = on ? el('button', { class: 'btn small', type: 'button', disabled: it.kind !== 'accessory', onclick: () => { Core.equip(st, it.id); render(); } }, it.kind === 'accessory' ? 'Take off' : '✓ Using')
        : owned ? el('button', { class: 'btn small primary', type: 'button', onclick: () => { Core.equip(st, it.id); render(); } }, 'Use')
          : el('button', { class: 'btn small ' + (short ? '' : 'gold'), type: 'button', disabled: short, 'data-buy': it.id, onclick: () => modal(`Buy ${it.name}?`, `${it.icon} ${it.name} costs ${it.price} ⚡. You have ${Core.bolts(st)} ⚡.`, [{ t: 'Not now', cls: 'ghost' }, { t: `Buy for ${it.price} ⚡`, cls: 'primary', on: () => { const r = Core.buy(st, it.id); if (r.ok) { toast(`${it.icon} ${it.name} is yours!`); confetti(); render(); } } }]) }, short ? `🔒 ${it.price} ⚡` : `${it.price} ⚡`);
      return el('div', { class: 'card item' + (on ? ' on' : '') }, el('span', { class: 'ii', style: it.css ? `background:${it.css}` : '' }, it.icon), el('b', {}, it.name), el('small', { class: 'muted' }, it.price ? (owned ? 'Owned' : `${it.price} bolts`) : 'Free'), btn);
    })));
    if (isGuest()) m.append(el('p', { class: 'muted' }, 'Guest purchases are kept on this device. Sign up free and they move into your account.'));
  }
  const statTile = (ic, big, small) => el('div', { class: 'tile', style: 'cursor:default' }, el('span', { class: 'ti' }, ic), el('b', {}, big), el('small', {}, small));
  function levelCards() {
    return el('div', { class: 'levelcards' }, el('div', { class: 'card lift' }, el('span', { class: 'lv' }, '7–9'), el('span', {}, el('b', { class: 'lex' }, 'Lower Secondary'), el('br'), el('small', { class: 'muted' }, 'Checkpoint · Stage 7 open now'))),
      el('div', { class: 'card off' }, el('span', { class: 'lv' }, 'IG'), el('span', {}, el('b', { class: 'lex' }, 'Cambridge IGCSE'), el('br'), el('small', { class: 'muted' }, 'Coming soon')), el('span', { class: 'lockicon' }, svgI(I.lock, 20, '#8B98AB', 2))),
      el('div', { class: 'card off' }, el('span', { class: 'lv' }, 'A'), el('span', {}, el('b', { class: 'lex' }, 'AS & A Level'), el('br'), el('small', { class: 'muted' }, 'Coming soon')), el('span', { class: 'lockicon' }, svgI(I.lock, 20, '#8B98AB', 2))));
  }
  function cellLens() {
    const on = el('div', { class: 'onion' }); for (let i = 0; i < 42; i++) on.append(el('span', { style: Math.floor(i / 6) % 2 ? 'margin-left:-12px' : '' }));
    return el('div', { class: 'cellview', 'aria-hidden': 'true' }, el('div', { class: 'ring' }), el('div', { class: 'lens' }, on), el('span', { class: 'mag' }, '×400'));
  }

  /* ---------- course page: learning path ---------- */
  function learningPath() {
    const ol = el('ol', { class: 'path' });
    const ts = Core.testState(st);
    C.sections.forEach((s, i) => {
      const lock = Core.secLock(st, s), done = Core.secDone(st, s), vd = Core.videoDone(st, s), vs = Core.vstate(st, s.id);
      const curr = !lock && !done; const reqDone = 8 - Core.reqLeft(st, s).length;
      const pracDone = s.req.concat(s.prac, s.adv).filter(q => (st.items[q.id] || {}).done).length;
      const stCls = lock ? 'lock' : done ? 'done' : 'cur';
      const ansStops = s.stops.filter(x => Core.stopDone(st, s.id, x)).length;
      const act = (on, t, sub, d, href, locked) => el('a', { class: 'act lift' + (on ? ' on' : '') + (locked ? ' lock' : ''), href, 'aria-disabled': locked ? 'true' : null }, el('span', { class: 'ai' }, svgI(d)), el('span', {}, el('b', {}, t), el('small', {}, sub)));
      ol.append(el('li', { style: `animation-delay:${i * .1}s` }, el('span', { class: 'node ' + stCls }, done ? '✓' : s.id),
        el('article', { class: 'card pcard' + (curr ? ' cur breathe' : '') },
          el('div', { class: 'hd' }, el('div', {}, el('small', { class: 'eyebrow' }, 'TOPIC ' + s.id), el('h3', {}, s.title)), el('span', { class: 'status ' + (lock ? 'lock' : done ? 'done' : 'cur') }, lock ? 'Locked' : done ? 'Completed' : 'In progress')),
          lock ? el('p', { class: 'muted', style: 'margin:0' }, '🔒 ' + lock.reason, lock.paywall ? el('a', { href: '#' + lock.route, style: 'margin-left:6px' }, lock.guest ? 'Sign up free' : 'See plans') : null) : el('p', { style: 'margin:0;color:#3A4B63;font-size:15px' }, s.objs.map(o => C.objectives[o].t).join(' ')),
          el('div', { class: 'acts' }, act(vd || ansStops, 'Watch', vd ? 'Watched' : ansStops ? `${ansStops} of ${s.stops.length} pauses` : 'Not started', I.play, '#v-' + R(s.id), !!lock),
            act(reqDone > 0, 'Practise', `${pracDone}/30 · ${reqDone}/8 Core`, I.check, '#ex-' + R(s.id), !!lock || !vd),
            act(st.ws.includes(s.id), 'Worksheet', st.ws.includes(s.id) ? 'Opened' : 'A4 · PDF', I.sheet, '#ws-' + R(s.id), !!lock)),
          curr && !lock ? el('a', { class: 'btn primary small shine', href: vd ? '#ex-' + R(s.id) : '#v-' + R(s.id), style: 'align-self:flex-start' }, vd ? `Practise ${s.id}` : vs.pos > 1 ? `Resume at ${fmt(vs.pos)}` : `Start ${s.id}`, el('span', { class: 'arr' }, '→')) : null)));
    });
    const totalReq = C.sections.reduce((a, s) => a + 8 - Core.reqLeft(st, s).length, 0);
    ol.append(el('li', { style: 'animation-delay:.4s' }, el('span', { class: 'node ' + (ts.state === 'passed' ? 'done' : ts.state === 'locked' ? 'lock' : 'cur') }, ts.state === 'passed' ? '✓' : '★'),
      el('article', { class: 'card pcard test' }, el('div', { class: 'hd' }, el('div', {}, el('small', { class: 'eyebrow' }, 'FINAL STEP'), el('h3', {}, 'Unit Test 3')), el('span', { class: 'status todo' }, `${totalReq} of 32 Core done`)),
        el('p', { style: 'margin:0;color:#3A4B63;font-size:15px' }, 'Unlocks when every video and Core question is done. Score above 70% to open Unit 4.'),
        ts.state === 'guest' ? el('a', { class: 'btn small gold', href: '#signup', style: 'align-self:flex-start' }, 'Sign up free to take the test', el('span', { class: 'arr' }, '→')) : ts.state === 'paywall' ? el('a', { class: 'btn small gold', href: '#pricing', style: 'align-self:flex-start' }, 'Unlock with a Stage 7 plan', el('span', { class: 'arr' }, '→')) : el('a', { class: 'btn small ' + (ts.state === 'locked' ? '' : 'primary shine'), href: ts.state === 'passed' ? '#result' : '#test', style: 'align-self:flex-start' }, ts.state === 'locked' ? 'See what\'s missing' : ts.state === 'passed' ? 'See results' : 'Take the Unit Test', el('span', { class: 'arr' }, '→')))));
    return ol;
  }
  function viewUnit() {
    const m = $main(); const nx = Core.nextActivity(st);
    const heroS = el('section', { class: 'hero' }, el('div', { class: 'hero-in' }, el('nav', { class: 'crumb', 'aria-label': 'Breadcrumb' }, el('a', { href: '#home' }, 'Dashboard'), ' › Lower Secondary › Stage 7 › Unit 3'),
      el('div', { class: 'txt' }, el('span', { class: 'eyebrow' }, 'UNIT 3 / 14 · BIOLOGY'), el('h1', {}, 'Cells'), el('p', {}, 'The basic units of life — from using a microscope to how cells build tissues, organs and organ systems.'),
        el('div', { class: 'btnrow', style: 'gap:22px' }, el('div', { class: 'prog' }, el('span', { style: 'display:flex;justify-content:space-between;font-weight:600;font-size:14px' }, el('span', {}, 'Unit progress'), el('span', {}, unitPct() + '%')), el('div', { class: 'pbar' }, el('i', { style: `width:${unitPct()}%` }))),
          el('button', { class: 'btn gold shine', type: 'button', onclick: () => goNext(nx) }, svgI(I.play, 16, '#0149AF', 2.6), nx.label))), cellLens()));
    document.getElementById('wrap').before(heroS);
    m.append(tocBtn(), el('div', { style: 'display:flex;justify-content:space-between;align-items:end;gap:12px;flex-wrap:wrap' }, el('h2', { style: 'margin:0;font-size:30px' }, 'Your learning path'), el('span', { class: 'muted' }, 'Watch → Practise → Test, one topic at a time')), learningPath());
    const sec = Object.keys(C.objectives).filter(objSecure).length;
    m.append(el('section', { class: 'card' }, el('h2', {}, 'What you will learn ', el('span', { class: 'muted' }, `· ${sec} of 9 secure`)),
      el('ul', { class: 'objs' }, ...Object.entries(C.objectives).map(([k, o]) => el('li', {}, el('span', { class: 'bd' + (objSecure(k) ? ' ok' : '') }, objSecure(k) ? '✓' : ''), el('span', {}, o.t))))));
    m.append(el('section', { class: 'card' }, el('div', { class: 'hd', style: 'display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap' }, el('h2', { style: 'margin:0' }, 'Concept map'), el('a', { class: 'btn small', href: '#map' }, 'Open the interactive map', el('span', { class: 'arr' }, '→'))), mindmapSvg(false)));
  }
  /* ---------- lesson: video with pause questions ---------- */
  let activeVideo = null;
  function viewVideo(sid) {
    const s = Core.sec(sid), m = $main(); if (!s) return go('home');
    const lock = Core.secLock(st, s);
    subbar('', el('a', { class: 'back', href: '#unit3' }, '← Unit 3: Cells'), el('span', { class: 'sep' }), el('span', { class: 'ttl' }, `Lesson ${s.id} · ${s.title}`));
    if (lock) { m.append(bar(`Section ${s.id} · Video`), lockScreen(`Section ${s.id} is locked`, lock.reason, [lock])); return; }
    const xp0 = Core.xp(st); const gchip = el('span', { class: 'gchip', html: FLAME + ` ${Core.streak(st)} · +<b id="lessonXp">0</b> ⚡ this lesson` });
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
    m.append(bar(`Unit 3 › ${s.id} › Video`), tocBtn(), el('div', { class: 'lesson' }, lessonMain, side));
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

  /* ---------- exercises (question card + solution panel) ---------- */
  function viewExercises(sid) {
    const s = Core.sec(sid), m = $main(); if (!s) return go('home'); const route = 'ex-' + R(sid);
    const lock = Core.secLock(st, s);
    if (lock || !Core.videoDone(st, s)) {
      subbar('blue', el('a', { class: 'back', href: '#unit3' }, '← Unit 3: Cells'), el('span', { class: 'ttl' }, `${s.id} ${s.title} · Practice`));
      m.append(bar(`Section ${s.id} · Practice`), lock ? lockScreen(`Practice for section ${s.id} is locked`, lock.reason, [lock]) : lockScreen(`Practice for section ${s.id} is locked`, 'Watch the whole video and answer its pause questions before you start the practice.', [Core.firstMissingIn(st, s)])); return;
    }
    const tab = UI.tab[route] || 'req'; const list = s[tab]; let idx = Math.min(UI.idx[route + tab] || 0, list.length - 1);
    st.last = { route, tab, idx }; Core.persist();
    const q = list[idx]; const go2 = i => { UI.idx[route + tab] = i; render(); };
    const pips = el('div', { class: 'pips', 'aria-hidden': 'true' }, ...list.map((x, i) => { const r = st.items[x.id] || {}; return el('span', { class: i === idx ? 'cur' : r.done ? (r.ok ? (r.tries === 1 ? 'ok' : 'half') : 'bad') : r.tries ? 'bad' : '' }); }));
    const tabName = { req: 'Core', prac: 'Practise', adv: '* Advanced' }[tab];
    subbar('blue', el('a', { class: 'back', href: '#unit3' }, '← Unit 3'), el('span', { style: 'font-size:15px;color:#DCE8FA' }, `${s.id} ${s.title} · ${tabName} · `, el('b', { style: 'color:#fff' }, `Question ${idx + 1} of ${list.length}`)), pips,
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
    const solBody = el('div', { class: 'card', style: 'padding:22px' }); let solTab = 'sol';
    const solTabs = el('div', { class: 'tabs', role: 'tablist' });
    const rec = st.items[q.id] = st.items[q.id] || { tries: 0 };
    const sg = C.segments[q.obj]; const segS = Core.sec(sg[0]);
    const drawSol = () => {
      solTabs.innerHTML = ''; [['sol', 'Worked solution'], ['video', 'Video solution']].forEach(([k, t]) => solTabs.append(el('button', { type: 'button', class: solTab === k ? 'on' : '', role: 'tab', 'aria-selected': String(solTab === k), onclick: () => { solTab = k; drawSol(); } }, t)));
      solBody.innerHTML = '';
      if (solTab === 'sol') {
        if (!rec.done) solBody.append(el('b', { class: 'lex' }, 'Solution'), el('p', { class: 'muted' }, 'The worked solution appears once you have finished this question. Stuck? Press “Check answer” for a step-by-step hint.'));
        else solBody.append(el('b', { class: 'lex', style: 'font-size:18px' }, 'Worked solution'), q.reason ? el('p', { class: 'reason' }, q.reason) : null, el('div', { class: 'banner ok', style: 'margin-top:8px' }, el('b', {}, 'Answer: '), QE.answerText(q)));
      } else solBody.append(el('b', { class: 'lex' }, `Video clip: ${sg[3]}`), el('p', { class: 'muted' }, `Lesson ${segS.id} · ${fullT(segS, sg[1])}–${fullT(segS, sg[2])} in the full video`), el('button', { class: 'btn primary small', type: 'button', onclick: () => go('v-' + R(segS.id), { seek: { sec: segS.id, from: sg[1], to: sg[2] } }) }, svgI(I.play, 16, '#fff', 2.6), 'Watch this clip'));
    };
    const aside = el('aside', { class: 'aside' }, solTabs, solBody,
      el('div', { class: 'card', style: 'padding:18px 20px' }, el('b', { class: 'lex' }, 'Learning objective'), el('p', { style: 'margin:4px 0 0;font-size:15px' }, `${q.obj}: ${C.objectives[q.obj].t}`)),
      el('div', { class: 'goal' }, el('span', { class: 'gi' }, svgI(I.bulb, 16, '#1C2A3A', 2)), el('span', {}, tab === 'req' ? 'Right first time: 1 mark · second try: ½ mark. Two wrong tries: you get guided reasoning and a similar question.' : tab === 'adv' ? '* Advanced – optional. Written by Atomic from the real source named on each question.' : 'Practice – optional for unlocking, but it makes you stronger before the Unit Test.')));
    m.append(bar(`Unit 3 › ${s.id} › ${tabName} › question ${idx + 1}`), tocBtn(), doneBanner, tabs, chips, el('div', { class: 'exgrid' }, el('div', { class: 'q' }, card), aside));
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
    switch (q.type) {
      case 'mcq': case 'multi': if (q.fig && q.fig.kind) box.append(figHtml(q.fig.kind, q.fig)); box.append(el('ol', { class: 'abc' }, ...q.options.map(o => el('li', {}, '☐ ' + o.t)))); break;
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
  function worksheetPages(s) {
    const qs = s.req.concat(s.prac.slice(0, 6));
    const page = (...kids) => el('div', { class: 'a4' }, ...kids);
    const hdr = (t) => el('div', { class: 'a4h' }, el('img', { src: 'atomic_logo.png', alt: '' }), el('div', {}, el('b', {}, 'ATOMIC EDUCATION · Science Stage 7'), el('div', {}, t)), el('div', { class: 'a4name' }, 'Name: ____________________  Class: ______  Date: ________'));
    const out = el('div', { class: 'ws' });
    let p = page(hdr(`Worksheet ${s.id} – ${s.title}`), el('p', { class: 'muted' }, 'Questions 1–8 = required · 9–14 = practice. Show your working.'));
    let n = 0; qs.forEach((q, i) => { if (n >= 3) { out.append(p); p = page(hdr(`Worksheet ${s.id} (continued)`)); n = 0; } p.append(printQ(q, i + 1)); n += (q.type === 'label' || q.type === 'scale' || q.fig || q.type === 'graph' || q.type === 'sim') ? 2 : 1; });
    out.append(p);
    out.append(page(hdr(`ANSWERS – Worksheet ${s.id} (separate page for teachers / self-marking)`), el('ol', { class: 'ans' }, ...qs.map(q => el('li', {}, QE.answerText(q), q.reason ? el('div', { class: 'muted' }, q.reason) : null))),
      el('p', { class: 'foot2' }, 'ATOMIC EDUCATION · Written by the Atomic teaching team')));
    return out;
  }
  function viewWorksheet(sid) {
    const s = Core.sec(sid), m = $main(); if (!s) return go('home');
    const lock = Core.secLock(st, s); if (lock && lock.paywall) { m.append(bar(`Unit 3 › ${s.id} › A4 worksheet`), lockScreen(`Worksheet ${s.id} is locked`, lock.reason, [lock])); return; }
    if (!st.ws.includes(sid)) { st.ws.push(sid); Core.persist(); }
    const msg = el('span', { class: 'muted' });
    m.append(bar(`Unit 3 › ${s.id} › A4 worksheet`), el('div', { class: 'btnrow noprint' },
      el('button', { class: 'btn primary', type: 'button', id: 'dlws', onclick: async () => {
        msg.textContent = 'Preparing…';
        try { const r = await fetch(`worksheets/Atomic_S7_U3_Worksheet_${R(sid)}.pdf`); if (!r.ok) throw 0; const b = await r.blob(); const res = await Core.saveFile(`Atomic_S7_U3_Worksheet_${R(sid)}.pdf`, b); msg.textContent = res === 'saved' ? 'Downloaded.' : res === 'declined' ? 'Download cancelled.' : 'Could not download.'; }
        catch (e) { msg.textContent = 'PDF file not found.'; }
      } }, '⬇ Download PDF (A4)'),
      el('button', { class: 'btn', type: 'button', onclick: () => { try { window.print(); } catch (e) { msg.textContent = 'This viewer blocks printing – please use Download PDF.'; } } }, '🖨 Print'), msg), worksheetPages(s));
  }

  /* ---------- unit test ---------- */
  function viewRemedial() {
    const m = $main(); const a = Core.lastAttempt(st); const ts = Core.testState(st);
    m.append(bar('Unit 3 › Review questions'));
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
  function drawCert(cert) {
    const cv = document.createElement('canvas'); cv.width = 1754; cv.height = 1240; const g = cv.getContext('2d');
    g.fillStyle = '#fff'; g.fillRect(0, 0, 1754, 1240); g.strokeStyle = '#0149AF'; g.lineWidth = 18; g.strokeRect(40, 40, 1674, 1160); g.strokeStyle = '#F3BF69'; g.lineWidth = 6; g.strokeRect(80, 80, 1594, 1080);
    return new Promise(res => { const img = new Image(); img.onload = () => {
      const h = 170, w = img.width / img.height * h; g.drawImage(img, 877 - w / 2, 130, w, h);
      g.textAlign = 'center'; g.fillStyle = '#0B2545'; g.font = '700 74px Inter, Arial'; g.fillText('CERTIFICATE OF COMPLETION', 877, 420);
      g.font = '36px Inter, Arial'; g.fillText('This certifies that', 877, 500);
      g.fillStyle = '#0149AF'; g.font = '700 92px Inter, Arial'; g.fillText(cert.name, 877, 620);
      g.fillStyle = '#0B2545'; g.font = '36px Inter, Arial'; g.fillText('has successfully completed', 877, 700);
      g.font = '700 58px Inter, Arial'; g.fillText('Atomic Education – Science Stage 7', 877, 790);
      g.font = '32px Inter, Arial'; g.fillText('Aligned to the Cambridge Lower Secondary Science curriculum framework', 877, 850);
      g.textAlign = 'left'; g.font = '30px Inter, Arial'; g.fillText('Completion date: ' + cert.date, 180, 1050); g.textAlign = 'right'; g.fillText('Certificate code: ' + cert.code, 1574, 1050);
      g.textAlign = 'center'; g.font = '24px Inter, Arial'; g.fillStyle = '#6B7A90'; g.fillText('ATOMIC EDUCATION · Verify at atomic certificate check · not a Cambridge qualification', 877, 1120); res(cv); }; img.src = 'atomic_logo.png'; });
  }
  async function viewCert() {
    const m = $main(); m.append(bar('Stage 7 certificate'));
    const cert = await Core.certificate(st);
    if (!cert) {
      const items = []; if (!Core.passed(st)) items.push({ what: 'pass Unit Test 3 (above 70%)', route: Core.testState(st).state === 'locked' ? (Core.missingForTest(st)[0] || {}).route || 'test' : 'test' });
      const done = Object.keys(st.results || {}).length; if (done < Core.STAGE_UNITS) items.push({ what: `the other Stage 7 units (${done} of ${Core.STAGE_UNITS} passed so far)`, route: 'unit3' });
      m.append(lockScreen('Certificate locked', 'The certificate is issued when every Unit Test in Stage 7 has been passed.', items)); return;
    }
    const c = { name: cert.name, code: cert.code, date: new Date(cert.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }) };
    const img = el('img', { class: 'certimg', alt: `Certificate for ${c.name}, code ${c.code}` }); const msg = el('span', { class: 'muted' });
    m.append(el('section', { class: 'card certwrap' }, el('h2', {}, '🎓 Certificate of completion'), el('p', {}, 'Certificate code: ', el('b', { id: 'certCode' }, c.code), ' · Completion date: ' + c.date),
      el('p', { class: 'muted' }, 'Anyone can check this certificate at ', el('a', { href: '#verify' }, 'Verify a certificate'), ' using the code.'), img,
      el('div', { class: 'btnrow' }, el('button', { class: 'btn primary', type: 'button', id: 'dlCert', onclick: async () => { const cv = await drawCert(c); const j = cv.toDataURL('image/jpeg', 0.92); const bytes = Uint8Array.from(atob(j.split(',')[1]), x => x.charCodeAt(0)); const pdf = Core.jpegPdf(bytes, cv.width, cv.height, 842, 595); const r = await Core.saveFile(`Atomic_Certificate_${c.code}.pdf`, new Blob([pdf], { type: 'application/pdf' })); msg.textContent = r === 'saved' ? 'Downloaded.' : r === 'declined' ? 'Download cancelled.' : 'Could not download.'; } }, '⬇ Download PDF'), msg)));
    drawCert(c).then(cv => { img.src = cv.toDataURL('image/png'); });
  }

  /* ---------- question bank ---------- */
  function viewBank() {
    const m = $main(); UI.bank = UI.bank || { sec: 'all', diff: 'all', type: 'all', status: 'all', tier: 'all' }; const F = UI.bank;
    m.append(bar('Question Bank'));
    m.append(el('div', {}, el('span', { class: 'eyebrow' }, 'UNIT 3 · CELLS'), el('h1', { style: 'margin:0;font-size:36px' }, 'Question Bank'),
      el('p', { class: 'muted', style: 'margin:4px 0 0' }, `${allQs().length} practice questions (30 per section: 8 Core, 18 Practice, 4 Advanced) plus ${C.sections.reduce((a, s) => a + s.stops.length, 0)} pause questions. Practising here never changes your Core progress or test scores.`)));
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
      el('p', { class: 'muted', style: 'margin:0 0 8px' }, 'Jump ahead to try every feature without answering all 120 questions. Simulated items count as done with full marks and are flagged “sim” in the data.'),
      el('div', { class: 'btnrow' }, ...C.sections.map(s => btn(`Complete ${s.id}`, () => fill([s.id]), 'sim' + R(s.id))),
        btn('Complete all sections → Unit Test', () => { fill(C.sections.map(s => s.id)); }, 'simAll'),
        el('button', { class: 'btn small', type: 'button', id: 'simOthers', onclick: async () => { await Backend.demo.simulateOtherUnits(st.id, 82); await Core.refreshResults(st); msg.textContent = 'Done – the other 13 units are marked as passed at 82%.'; setTimeout(render, 500); } }, 'Pass the other 13 units (82%)'),
        el('button', { class: 'btn small', type: 'button', id: 'simStaff', onclick: () => { Backend.demo.setRole('admin'); msg.textContent = 'This account is now an administrator – open Staff from the account menu.'; } }, 'Make this account staff'),
        el('button', { class: 'btn small ghost', type: 'button', id: 'resetUnit', onclick: () => modal('Reset Unit 3?', 'This clears all Unit 3 progress, tests, certificate and ranking score for this learner.', [{ t: 'Cancel', cls: 'ghost' }, { t: 'Reset', cls: 'primary', on: async () => { await Backend.demo.resetLearner(st.id); await Core.selectLearner(st.id); go('home'); } }]) }, 'Reset Unit 3 progress')), msg);
  }

  /* ---------- router ---------- */

  /* ---------- unit test (exam mode) ---------- */
  let timer = null;
  function viewTest() {
    const m = $main(); const ts = Core.testState(st);
    const form = ts.form || (ts.last && ts.last.form) || 'A';
    const clock = el('span', { class: 'gchip', style: 'margin-left:auto', hidden: true });
    subbar('', el('span', { class: 'ttl' }, `Unit Test 3 · Cells · Paper ${form}`), el('span', { class: 'exam-badge' }, 'EXAM MODE'), clock);
    if (ts.state === 'guest') { m.append(bar('Unit 3 › Unit Test'), guestWall('Sign up free to take the Unit Test')); return; }
    if (ts.state === 'paywall') { m.append(bar('Unit 3 › Unit Test'), lockScreen('Unit Test 3 needs a Stage 7 plan', 'Unit Tests, marking and the certificate are part of the full course.', [{ what: 'a Stage 7 plan (7-day free trial)', route: 'pricing' }])); return; }
    if (ts.state === 'locked') { m.append(bar('Unit 3 › Unit Test'), lockScreen('Unit Test 3 is locked', 'The Unit Test opens only when you have watched every video and finished every Core question in all 4 sections.', ts.miss)); return; }
    if (ts.state === 'pending') { m.append(bar('Unit 3 › Unit Test'), el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, `Attempt ${ts.last.n} (Paper ${ts.last.form}) has a written answer for an Atomic marker to mark. We will notify you when it is done. Automatic marks: ${ts.last.auto}/${30 - ts.last.pending.reduce((a, id) => a + ts.last.per[id].max, 0)}. Unit 4 opens only once the final mark is in.`), el('a', { class: 'btn primary small', href: '#result' }, 'Results & history'))); return; }
    if (ts.state === 'remediate') { m.append(bar('Unit 3 › Unit Test'), lockScreen('You can\'t retake yet', 'Finish the review questions set for your weaker objectives before you take the equivalent paper.', [{ what: `${ts.left.length} review questions`, route: 'remedial' }])); return; }
    if (ts.state === 'passed') { m.append(bar('Unit 3 › Unit Test'), el('section', { class: 'card done' }, el('h2', {}, '✓ You have passed Unit Test 3'), el('a', { class: 'btn primary small', href: '#result' }, 'See results'))); return; }
    const qs = C.tests[form];
    st.last = { route: 'test' };
    const draft = st.test.drafts[form] = st.test.drafts[form] || { answers: {}, ts: Date.now() };
    const hasDraft = Object.keys(draft.answers).length > 0;
    if (!UI.testOn) {
      m.append(el('section', { class: 'card', style: 'max-width:740px;margin:0 auto;padding:40px;border-radius:28px;display:flex;flex-direction:column;gap:16px' },
        el('span', { class: 'eyebrow' }, 'BEFORE YOU START'), el('h1', { style: 'margin:0;font-size:36px' }, `Unit Test 3 · Paper ${form}${ts.retake ? ' (equivalent paper)' : ''}`),
        el('div', { class: 'stats3' }, el('div', {}, el('b', {}, String(qs.length)), el('br'), el('small', { class: 'muted' }, 'questions')), el('div', {}, el('b', {}, '30'), el('br'), el('small', { class: 'muted' }, 'marks')), el('div', {}, el('b', {}, '> 70%'), el('br'), el('small', { class: 'muted' }, 'to pass (21/30 is not a pass)'))),
        el('ul', { style: 'margin:0;padding-left:20px;color:#3A4B63' }, el('li', {}, 'No hints or videos during the test.'), el('li', {}, 'You can flag a question and come back to it. Your answers are saved as a draft automatically.'), el('li', {}, 'Solutions appear after you submit. Most questions are marked straight away; written answers are marked by an Atomic marker.'), el('li', {}, 'Pass to unlock Unit 4 and earn ', el('b', { style: 'color:#0149AF' }, '+100 XP'), '.')),
        hasDraft ? el('div', { class: 'banner info', id: 'draftNote' }, 'Your draft has been restored – carry on from where you stopped.') : null,
        el('button', { class: 'btn primary big shine', type: 'button', id: 'startTest', style: 'align-self:flex-start', onclick: () => { UI.testOn = true; UI.testStart = UI.testStart || Date.now(); render(); } }, hasDraft ? 'Resume the test' : 'Start the test', el('span', { class: 'arr' }, '→'))));
      return;
    }
    const i = Math.min(UI.testIdx || 0, qs.length - 1), q = qs[i];
    clock.hidden = false; const tick = () => { const s = Math.floor((Date.now() - (UI.testStart || Date.now())) / 1000); clock.textContent = '⏱ ' + fmt(s); };
    clearInterval(timer); timer = setInterval(tick, 1000); tick();
    const saved = el('span', { class: 'muted', 'aria-live': 'polite' });
    const answered = x => draft.answers[x.id] != null && draft.answers[x.id] !== '' && !(Array.isArray(draft.answers[x.id]) && !draft.answers[x.id].length);
    const card = el('section', { class: 'card qcard', style: 'flex:999 1 600px;min-width:0' },
      el('div', { class: 'btnrow between', style: 'margin:0' }, el('span', { class: 'lex', style: 'font-weight:700;color:#556377' }, `Question ${i + 1} of ${qs.length} · ${q.pts} mark${q.pts > 1 ? 's' : ''}${q.teacher ? ' · marked by an Atomic marker' : ''}`),
        el('button', { class: 'chip' + (UI.flags[q.id] ? ' on' : ''), type: 'button', 'aria-pressed': String(!!UI.flags[q.id]), onclick: () => { UI.flags[q.id] = !UI.flags[q.id]; render(); } }, svgI(I.flag, 14), UI.flags[q.id] ? 'Flagged' : 'Flag')),
      el('h2', { class: 'qp', style: 'font-size:24px' }, q.prompt));
    QE.renderBody(q, card, { seed: st.id + form, resp: draft.answers[q.id], onChange: r => { draft.answers[q.id] = r; draft.ts = Date.now(); Core.persist(); saved.textContent = 'Draft saved ' + new Date().toLocaleTimeString(); drawNav(); } });
    card.append(el('div', { class: 'btnrow between', style: 'padding-top:16px;border-top:1px solid #E6EEF8' }, el('button', { class: 'btn small', type: 'button', disabled: i === 0, onclick: () => { UI.testIdx = i - 1; render(); } }, '← Previous'), saved,
      i < qs.length - 1 ? el('button', { class: 'btn primary', type: 'button', id: 'testNext', onclick: () => { UI.testIdx = i + 1; render(); } }, 'Next question', el('span', { class: 'arr' }, '→')) : el('button', { class: 'btn navy', type: 'button', onclick: () => submit() }, 'Finish test')));
    const nav = el('div', { class: 'navgrid' });
    const drawNav = () => { nav.innerHTML = ''; qs.forEach((x, k) => nav.append(el('button', { type: 'button', class: (UI.flags[x.id] ? 'flag' : answered(x) ? 'ans' : '') + (k === i ? ' on' : ''), 'aria-label': `Question ${k + 1}${answered(x) ? ', answered' : ''}${UI.flags[x.id] ? ', flagged' : ''}`, onclick: () => { UI.testIdx = k; render(); } }, String(k + 1)))); };
    drawNav();
    function submit() {
      const blank = qs.filter(x => !answered(x)).length;
      modal('Submit your test?', blank ? `You have ${blank} unanswered question(s). Submit now?` : 'After you submit you will see your score and the solutions.', [{ t: 'Go back', cls: 'ghost' }, { t: 'Finish test', cls: 'primary', on: async () => {
        if (UI.submitting) return true; UI.submitting = true; // guard double submit; the server is idempotent on draft.key too
        draft.key = draft.key || (crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + Math.random()); Core.persist();
        const wait = modal('Marking your test…', 'Please keep this page open.', []);
        try {
          const r = await Core.submitTest(st, form, draft.answers, draft.key); delete st.test.drafts[form]; Core.persist(); Core.flush();
          UI.testOn = false; UI.testIdx = 0; UI.flags = {}; UI.testStart = null; clearInterval(timer); wait(); if (r.attempt.status === 'final' && r.attempt.passed) confetti(); go('result');
        } catch (x) { wait(); modal('Could not submit', errText(x) + ' Your answers are saved as a draft.', [{ t: 'OK', cls: 'primary' }]); }
        finally { UI.submitting = false; }
      } }]);
    }
    m.append(el('div', { style: 'display:flex;flex-wrap:wrap;gap:26px;align-items:flex-start' }, card,
      el('aside', { class: 'card', style: 'flex:1 1 260px;min-width:0;display:flex;flex-direction:column;gap:14px' }, el('b', { class: 'lex' }, 'Questions'), nav,
        el('div', { class: 'legend' }, el('span', {}, el('i', { style: 'background:#0149AF' }), 'Answered'), el('span', {}, el('i', { style: 'background:#F3BF69' }), 'Flagged'), el('span', {}, el('i', { style: 'border:2px solid #D3E0F4' }), 'Not answered')),
        el('button', { class: 'btn navy small', type: 'button', id: 'submitTest', onclick: () => submit() }, 'Finish test'))));
  }
  function attemptRow(a) { return el('tr', {}, el('td', {}, a.n), el('td', {}, a.form), el('td', {}, new Date(a.ts).toLocaleString('en-GB')), el('td', {}, a.status === 'final' ? `${+a.score.toFixed(2)}/30` : `${a.auto} + ?`), el('td', {}, a.status === 'final' ? a.pct.toFixed(1) + '%' : '—'), el('td', {}, a.status === 'pending' ? el('span', { class: 'status cur' }, '⏳ Awaiting marking') : a.passed ? el('span', { class: 'status done' }, '✓ Passed') : el('span', { class: 'tag d-VH' }, '✗ Not passed'))); }
  function ring(pct, ok) { const r = 46, c = 2 * Math.PI * r; const s = document.createElement('span'); s.className = 'ring'; s.innerHTML = `<svg viewBox="0 0 110 110" width="110" height="110"><circle cx="55" cy="55" r="${r}" fill="none" stroke="#DCE8FA" stroke-width="12"/><circle cx="55" cy="55" r="${r}" fill="none" stroke="${ok ? '#1E8E4E' : '#C93A3A'}" stroke-width="12" stroke-linecap="round" stroke-dasharray="${c * pct / 100} ${c}" transform="rotate(-90 55 55)"/><text x="55" y="62" text-anchor="middle" font-family="Lexend" font-weight="800" font-size="22" fill="#1C2A3A">${Math.round(pct)}%</text></svg>`; return s; }
  function viewResult() {
    const m = $main(); m.append(bar('Unit 3 › Results & history'));
    const before = JSON.stringify(Core.attempts(st).map(a => a.status));
    Core.refreshAttempts(st).then(() => { if (JSON.stringify(Core.attempts(st).map(a => a.status)) !== before && location.hash === '#result') render(); }).catch(() => { });
    const at = Core.attempts(st);
    if (!at.length) { m.append(el('section', { class: 'card' }, el('h2', {}, 'No tests taken yet'), el('a', { class: 'btn primary small', href: '#test' }, 'Go to the Unit Test'))); return; }
    const a = at[at.length - 1];
    if (a.status === 'pending') m.append(el('section', { class: 'card' }, el('h2', {}, '⏳ Awaiting marking'), el('p', {}, 'Your written answer is waiting for an Atomic marker. Pass/not passed and unlocking Unit 4 are decided only when the final mark is in – you will get a notification.')));
    else if (a.passed) m.append(el('section', { class: 'card done' }, el('div', { class: 'resultbig' }, ring(a.pct, true), el('div', {}, el('span', { class: 'eyebrow' }, 'PASSED · +100 ⚡'), el('h2', { style: 'margin:0' }, `${+a.score.toFixed(2)}/30 (${a.pct.toFixed(1)}%)`), el('p', { style: 'margin:4px 0' }, 'Unit 4 is now unlocked. Your Unit 3 ranking score = % of your first pass: ' + st.rank.u3.toFixed(1) + '%.'))),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn primary small', href: '#board' }, '🏆 Leaderboard'), el('a', { class: 'btn small', href: '#cert' }, '🎓 Certificate'))));
    else {
      const left = Core.remLeft(st, a);
      m.append(el('section', { class: 'card bad' }, el('div', { class: 'resultbig' }, ring(a.pct, false), el('div', {}, el('span', { class: 'eyebrow', style: 'color:#B42318' }, 'NOT PASSED · YOU NEED ABOVE 70%'), el('h2', { style: 'margin:0' }, `${+a.score.toFixed(2)}/30 (${a.pct.toFixed(1)}%)`), el('p', { style: 'margin:4px 0' }, 'Unit 4 stays locked. Here is where you went wrong and what to do next:'))),
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

  /* ---------- mind map ---------- */
  function mindmapSvg(interactive) {
    const mm = C.mindmap; const Wd = 960, Ht = 560, cx = 480, cy = 280;
    const pos = mm.kids.map((k, i) => { const a = -Math.PI / 2 + i * 2 * Math.PI / mm.kids.length; return [cx + 340 * Math.cos(a), cy + 205 * Math.sin(a)]; });
    let svg = `<svg viewBox="0 0 ${Wd} ${Ht}" xmlns="http://www.w3.org/2000/svg" ${interactive ? 'id="mmsvg"' : ''} role="img" aria-label="Cells concept map">`;
    pos.forEach(([x, y], i) => svg += `<path d="M${cx} ${cy} Q ${(cx + x) / 2} ${cy} ${x} ${y}" class="mml" style="animation-delay:${i * .12}s"/>`);
    svg += `<g class="mmroot"><rect x="${cx - 85}" y="${cy - 34}" width="170" height="68" rx="34"/><text x="${cx}" y="${cy + 9}" text-anchor="middle">Cells</text></g>`;
    mm.kids.forEach((k, i) => { const [x, y] = pos[i]; svg += `<g class="mmn" data-i="${i}" ${interactive ? 'tabindex="0" role="button"' : ''} aria-label="${esc(k.t)}"><rect x="${x - 108}" y="${y - 32}" width="216" height="64" rx="16"/><text x="${x}" y="${y - 4}" text-anchor="middle">${esc(k.t.length > 26 ? k.t.slice(0, 24) + '…' : k.t)}</text><text x="${x}" y="${y + 16}" text-anchor="middle" class="sm">${k.sec} · ${k.obj}</text></g>`; });
    const box = el('div', { class: 'mmbox', html: svg + '</svg>' });
    if (!interactive) box.querySelectorAll('.mmn').forEach(g => g.addEventListener('click', () => { UI.mmPick = +g.dataset.i; go('map'); }));
    box._pos = pos; box._dims = [Wd, Ht]; return box;
  }
  function viewMap() {
    const m = $main(); if (st) m.append(bar('Unit 3 › Concept map'));
    const mm = C.mindmap; const box = mindmapSvg(true); const pos = box._pos; const [Wd, Ht] = box._dims;
    const detail = el('div', { class: 'card', 'aria-live': 'polite' }, el('p', { class: 'muted', style: 'margin:0' }, 'Tap a branch to zoom in, read it and jump to the video clip or practice.')); detail.className = 'card mmdetail';
    let vb = [0, 0, Wd, Ht];
    const setVB = () => box.querySelector('svg').setAttribute('viewBox', vb.map(v => Math.round(v)).join(' '));
    const zoom = f => { const c = [vb[0] + vb[2] / 2, vb[1] + vb[3] / 2]; vb[2] = Math.min(Wd, Math.max(240, vb[2] * f)); vb[3] = vb[2] * Ht / Wd; vb[0] = c[0] - vb[2] / 2; vb[1] = c[1] - vb[3] / 2; setVB(); };
    m.append(el('div', {}, el('span', { class: 'eyebrow' }, 'UNIT 3 · CELLS'), el('h1', { style: 'margin:0;font-size:36px' }, 'Concept map'), el('p', { class: 'muted', style: 'margin:4px 0 0' }, 'How the big ideas of Unit 3 connect. Tap a branch to zoom in.')),
      el('div', { class: 'btnrow' }, el('button', { class: 'chip', type: 'button', onclick: () => zoom(0.75) }, '＋ Zoom in'), el('button', { class: 'chip', type: 'button', onclick: () => zoom(1.33) }, '－ Zoom out'), el('button', { class: 'chip', type: 'button', onclick: () => { vb = [0, 0, Wd, Ht]; setVB(); box.querySelectorAll('.mmn').forEach(n => n.classList.remove('on')); } }, 'Show all')), box, detail);
    const pick = i => {
      const g = box.querySelector(`.mmn[data-i="${i}"]`); const k = mm.kids[i], [x, y] = pos[i]; vb = [x - 220, y - 138, 440, 275]; setVB();
      box.querySelectorAll('.mmn').forEach(n => n.classList.toggle('on', n === g));
      const sg = C.segments[k.obj], s = Core.sec(sg[0]);
      detail.innerHTML = ''; detail.append(el('span', { class: 'eyebrow' }, `${k.sec} · ${k.obj}`), el('h3', { style: 'margin:2px 0 6px;font-size:22px' }, k.t), el('p', { style: 'margin:0 0 4px' }, k.d), el('p', { class: 'muted' }, C.objectives[k.obj].t),
        el('div', { class: 'btnrow' }, el('button', { class: 'btn primary small', type: 'button', onclick: () => go('v-' + R(s.id), { seek: { sec: s.id, from: sg[1], to: sg[2] } }) }, svgI(I.play, 14, '#fff', 2.6), `Video clip ${s.id} (${fullT(s, sg[1])}–${fullT(s, sg[2])})`),
          st ? el('button', { class: 'btn small', type: 'button', onclick: () => go('ex-' + R(s.id)) }, `Practise section ${s.id}`) : null, st ? el('button', { class: 'btn small ghost', type: 'button', onclick: () => startDrill(`Revise topic ${k.obj}`, allQs().filter(q => q.obj === k.obj && !q.adv).slice(0, 10), 'topic' + k.obj) }, 'Revise by topic') : null));
    };
    box.querySelectorAll('.mmn').forEach(g => { const act = () => pick(+g.dataset.i); g.addEventListener('click', act); g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); act(); } }); });
    if (UI.mmPick != null) { pick(UI.mmPick); UI.mmPick = null; }
  }

  /* ---------- progress / profile ---------- */
  function viewProfile() {
    const m = $main(); const wl = wrongList(); const nx = Core.nextActivity(st);
    const rs = Core.rankScore(st);
    m.append(bar('Your progress'), el('section', { class: 'card feature', style: 'display:flex;gap:20px;align-items:center;flex-wrap:wrap' },
      avatarEl(72),
      el('div', { style: 'flex:1;min-width:200px' }, el('h2', { style: 'margin:0;color:#fff' }, st.alias), el('span', { style: 'color:#DCE8FA' }, isGuest() ? 'Guest – progress kept on this device only' : `Nickname “${st.alias}” · progress saved to your account`)),
      el('div', { style: 'display:flex;gap:10px;flex-wrap:wrap' }, el('span', { class: 'pill streak', html: FLAME + ' ' + Core.streak(st) + ' days' }), el('a', { class: 'pill xp', href: '#shop', html: BOLT + ' ' + Core.bolts(st).toLocaleString('en-GB') + ' bolts' }))));
    const tile = (icon, t, sub, on, id) => el('button', { class: 'tile lift', type: 'button', onclick: on, id }, el('span', { class: 'ti' }, icon), el('b', {}, t), el('small', {}, sub));
    m.append(el('div', { class: 'tiles' },
      tile('▶', 'Continue learning', nx.label, () => { location.hash = 'home'; setTimeout(() => document.getElementById('resumeBtn') && document.getElementById('resumeBtn').click(), 0); }, 'tileResume'),
      tile('↺', 'Redo wrong answers', `${wl.length} question${wl.length === 1 ? '' : 's'}`, () => startDrill('Redo wrong answers', wl, 'wrong'), 'tileWrong'),
      tile('🧩', 'Revise by topic', '9 objectives O1–O9', () => go('topic'), 'tileTopic'),
      tile('📄', 'Worksheets opened', st.ws.length ? st.ws.map(x => 'Section ' + x).join(', ') : 'none opened yet', () => go(st.ws.length ? 'ws-' + R(st.ws[st.ws.length - 1]) : 'ws-3-1'), 'tileWs')));
    if (st.ws.length) m.append(el('div', { class: 'btnrow' }, ...st.ws.map(x => el('a', { class: 'chip', href: '#ws-' + R(x) }, '📄 Worksheet ' + x))));
    m.append(el('section', { class: 'card' }, el('h2', {}, 'Unit 3 progress'), ...C.sections.map(s => el('div', { style: 'margin:10px 0' }, el('div', { style: 'display:flex;justify-content:space-between;font-size:14px;font-weight:600' }, el('span', {}, `${s.id} ${s.title}`), el('span', { class: 'muted' }, `video ${Core.videoDone(st, s) ? '✓' : '…'} · Core ${8 - Core.reqLeft(st, s).length}/8 · practice ${s.prac.filter(q => (st.items[q.id] || {}).done).length}/18 · advanced ${s.adv.filter(q => (st.items[q.id] || {}).done).length}/4`)), el('div', { class: 'pbar' + (Core.secDone(st, s) ? ' ok' : '') }, el('i', { style: `width:${secPct(s)}%` })))),
      el('p', {}, `Unit Test: ${Core.attempts(st).length} attempt(s) · ${Core.passed(st) ? 'Passed' : 'not passed yet'} · Ranking score: ` + (rs ? rs.score.toFixed(2) + '% (' + rs.units + (rs.units === 1 ? ' unit)' : ' units)') : 'none yet')),
      el('div', { class: 'btnrow' }, el('a', { class: 'btn small', href: '#result' }, 'Results & history'), el('a', { class: 'btn small', href: '#cert' }, '🎓 Certificate'), el('a', { class: 'btn small', href: '#board' }, '🏆 Leaderboard'))));
    m.append(testerTools());
    if (!isGuest()) {
      const w = Core.wallet(st);
      m.append(el('section', { class: 'card' }, el('h3', {}, '⚡ Recent bonuses'), w.log.length ? el('ul', {}, ...w.log.slice(0, 8).map(x => el('li', {}, `${x.d} · +${x.n} ⚡ · ${x.why}`))) : el('p', { class: 'muted' }, 'Complete daily challenges and keep your streak going to earn bonus bolts.'),
        el('p', { class: 'muted', style: 'margin:8px 0 0' }, el('a', { href: '#privacy-kids' }, 'How Atomic looks after your data'), ' – the short version for learners.')));
    }
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
    hin.append(el('span', { class: 'eyebrow', style: 'color:#F3BF69' }, 'SCIENCE STAGE 7'), el('h1', {}, '🏆 Leaderboard'),
      el('div', { class: 'formula' }, el('b', { style: 'color:#fff' }, 'Ranking score = (Σ first-pass % of each unit) ÷ number of units'), ' — every unit counts equally. Your first-pass % is fixed the moment you first pass a unit; revising or retaking later never changes it. Equal scores share a rank. Bolts are just for fun and are not used for ranking.'));
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
    subscription_required: 'This needs a Stage 7 plan.', locked: 'Finish every video and Core question first.', awaiting_marking: 'Your last test is still being marked.', review_first: 'Finish your review questions first.',
    already_passed: 'You have already passed this test.', wrong_paper: 'Please reload the page and try again.', confirm: 'Type the confirmation exactly as shown.', staff_only: 'Staff only.', message: 'Please write a short message.' };
  const errText = e => ERR[e && e.code] || (e && e.detail) || 'Something went wrong. Please try again.';
  const COUNTRIES = [['GB', 'United Kingdom'], ['SG', 'Singapore'], ['MY', 'Malaysia'], ['TH', 'Thailand'], ['VN', 'Vietnam'], ['ID', 'Indonesia'], ['PH', 'Philippines'], ['XX', 'Another country']];
  const field = (label, input, hint) => el('label', { class: 'field' }, el('span', {}, label), input, hint ? el('small', { class: 'muted' }, hint) : null);
  const errBox = () => el('p', { class: 'err', role: 'alert' });
  const narrow = (...kids) => el('section', { class: 'card narrow' }, ...kids);

  /* ---------- public landing ---------- */
  function viewLanding() {
    const m = $main();
    document.getElementById('wrap').before(el('section', { class: 'hero' }, el('div', { class: 'hero-in' }, el('div', { class: 'txt' },
      el('span', { class: 'eyebrow' }, 'CAMBRIDGE LOWER SECONDARY SCIENCE · STAGE 7'), el('h1', {}, 'Science that clicks – learn at your own pace.'),
      el('p', {}, 'Short lesson videos that stop and ask you questions, 30 practice questions per topic with step-by-step hints, Unit Tests and a certificate. Earn ⚡ bolts as you learn and spend them in the shop.'),
      el('div', { class: 'btnrow' }, el('button', { class: 'btn gold big shine', type: 'button', id: 'heroStart', onclick: startGuest }, 'Start learning now', el('span', { class: 'arr' }, '→')), el('a', { class: 'btn onblue', href: '#signup', id: 'heroSignup' }, 'Sign up free')),
      el('small', { style: 'color:#DCE8FA' }, 'No sign-up needed to try topic 3.1.')), cellLens())));
    const step = (n, t, d) => el('div', { class: 'card' }, el('span', { class: 'node done', style: 'width:44px;height:44px' }, String(n)), el('h3', {}, t), el('p', { class: 'muted', style: 'margin:0' }, d));
    m.append(el('h2', { style: 'margin:0' }, 'How it works'), el('div', { class: 'tiles' }, step(1, 'Try it straight away', 'Open topic 3.1 as a guest – no account needed. When you like it, sign up free to save your progress.'),
      step(2, 'Watch → practise → test', 'Every topic: a lesson video with pause questions, 30 practice questions (8 Core), then a Unit Test marked by the Atomic teaching team.'),
      step(3, 'Earn bolts, keep your streak', 'Answers earn ⚡ bolts. Hit your daily goal to grow your streak, finish challenges and spend bolts on avatars and backgrounds.')));
    const feat = (i, t, d) => el('div', { class: 'card' }, el('span', { class: 'ti', style: 'font-size:26px' }, i), el('b', { class: 'lex' }, t), el('p', { class: 'muted', style: 'margin:4px 0 0' }, d));
    m.append(el('h2', { style: 'margin:8px 0 0' }, 'What is inside Stage 7'), el('div', { class: 'tiles' },
      feat('▶', 'Lesson videos that ask', 'The video pauses at key moments; wrong answers get a specific hint, not just “try again”.'), feat('🧪', '12 kinds of question', 'Label diagrams, read instruments, plot graphs, run a virtual microscope, explain your reasoning.'),
      feat('★', 'Unit Tests marked properly', 'Two equivalent papers per unit. Written answers are marked by Atomic teachers. Pass above 70%.'), feat('📧', 'Keep your family in the loop', 'Add a parent’s email if you like – we let them know when you finish a unit.')));
    m.append(el('section', { class: 'card' }, el('h2', {}, 'Free to try'), el('p', {}, Core.BILLING_OFF ? 'During our test phase the whole Stage 7 course is free – no card needed.' : 'The first topic of every unit is free – no card needed.'),
      el('div', { class: 'btnrow' }, el('button', { class: 'btn primary', type: 'button', onclick: startGuest }, 'Start learning now'), el('a', { class: 'btn', href: '#signup' }, 'Create a free account'))));
    m.append(faq());
  }
  function faq() {
    const qa = [['Who is Atomic for?', 'Learners aged about 11–12 following Cambridge Lower Secondary Science Stage 7, at an international or bilingual school or studying at home.'],
      ['Do I need an account?', 'Not to try it: topic 3.1 is open to guests. Create a free account to save your progress, unlock every topic, take the Unit Test and keep your bolts.'],
      ['What are bolts ⚡?', 'Points you earn by doing the work – watching lessons and answering questions (right first time earns the most). Spend them in the shop on avatars, accessories and backgrounds. They are just for fun and do not affect your ranking.'],
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
    const card = el('section', { class: 'card narrow signup' }); m.append(card);
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
    m.append(narrow(el('h1', {}, 'Log in'), el('div', { class: 'form' }, field('Email', email), field('Password', pw), e, b),
      el('p', { class: 'muted' }, el('a', { href: '#forgot' }, 'Forgotten your password?'), ' · New here? ', el('a', { href: '#signup' }, 'Sign up free'))));
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
    m.append(el('div', {}, el('span', { class: 'eyebrow' }, 'ACCOUNT'), el('h1', { style: 'margin:4px 0 0' }, 'Settings'), el('p', { class: 'muted', style: 'margin:0' }, Core.S.me.user.email)),
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
    modal('Delete your account?', el('div', { class: 'form' }, el('p', {}, 'This deletes your account, all progress, tests, bolts, shop items and certificates. This cannot be undone.'), field('Type DELETE MY ACCOUNT to confirm', inp), e),
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
        [{ t: 'Cancel', cls: 'ghost' }, { t: 'Start free trial (preview)', cls: 'primary', on: async () => { await Backend.checkout(p); await Core.refreshAccount(); toast('Trial started – Stage 7 unlocked'); go('unit3'); } }]);
      else await Backend.checkout(p);
    } }, active ? 'Your plan is active' : 'Start 7-day free trial');
    m.append(el('div', { style: 'text-align:center' }, el('span', { class: 'eyebrow' }, 'PLANS'), el('h1', { style: 'margin:4px 0' }, 'One plan, the whole of Stage 7'), el('p', { class: 'muted' }, 'Cancel any time.')),
      el('div', { class: 'plans' }, plan('free', 'Free', '£0', ['First topic of every unit', 'Lesson videos with pause questions', '30 practice questions for that topic', 'Daily challenges, bolts and the shop'], me ? el('a', { class: 'btn', href: '#home' }, 'Keep learning free') : el('a', { class: 'btn', href: '#signup' }, 'Start free')),
        plan('monthly', 'Stage 7 – monthly', L.monthly, ['All 4 topics of every unit', 'Unit Tests marked by Atomic', 'A4 worksheets and concept maps', 'Stage 7 certificate'], buy('monthly')),
        plan('yearly', 'Stage 7 – yearly', L.yearly, ['Everything in monthly', 'About 2 months free', 'Price fixed for the year'], buy('yearly'), true)),
      el('p', { class: 'muted', style: 'text-align:center' }, 'Prices shown in GBP for guidance. At checkout Paddle, our reseller, shows the price in your currency including VAT/GST where it applies (UK VAT, Singapore GST, Malaysia SST, Thailand VAT, Vietnam, Indonesia and Philippines taxes).'), faq());
  }

  function viewBeta() {
    const m = $main(); const me = Core.S.me;
    m.append(narrow(el('span', { class: 'eyebrow' }, 'TEST PHASE'), el('h1', {}, 'Free while we test'), el('p', {}, 'Atomic is in a small private test. Every learner gets the whole Stage 7 course – videos, practice, Unit Tests and the certificate – free of charge. No card is needed.'),
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
      el('button', { class: 'btn primary', type: 'button', id: 'vfBtn', onclick: async () => { const r = await Backend.verifyCertificate(code.value); out.innerHTML = ''; out.append(r ? el('div', { class: 'banner ok' }, `✓ Genuine: ${r.name_on_certificate} completed Atomic Education – Science Stage ${r.stage} on ${String(r.issued_at).slice(0, 10)}.`) : el('div', { class: 'banner adv' }, 'No certificate has this code.')); } }, 'Check'), out)));
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
      'Learning records: answers, progress, bolts, shop items, test results – to give feedback, mark tests, show progress and issue certificates.',
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
    ['Who the course is for', 'The Stage 7 course is designed for learners aged about 11 to 13. Anyone can try topic 3.1 as a guest. Learners create their own free account to save progress.'],
    ['Accounts', 'One account per learner. Keep your password private. If you are under the age of digital consent where you live, ask a parent or guardian before you sign up.'],
    ['Plans, trials and refunds', 'Plans renew automatically until cancelled. A free trial converts to a paid plan unless cancelled before it ends. Our order process is conducted by our online reseller Paddle.com, the Merchant of Record for all orders; Paddle provides customer service enquiries and handles returns.'],
    ['Fair use', 'Course content is for your own personal learning. Do not copy, share or resell videos, questions, tests or worksheets.'],
    ['Bolts and the shop', 'Bolts are earned by learning and can only be spent on items inside Atomic. They have no money value, cannot be bought, sold or exchanged, and are not used for ranking.'],
    ['Tests and certificates', 'Unit Tests are marked automatically and, for written answers, by Atomic markers. A certificate confirms completion of the Atomic Stage 7 course; it is not a Cambridge qualification.'],
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
  const TOC_ROUTES = r => r.startsWith('v-') || r.startsWith('ex-') || r.startsWith('ws-') || ['unit3', 'map', 'result', 'remedial', 'topic', 'drill', 'cert'].includes(r);
  const PUBLIC = { home: () => viewHome(), signin: viewSignin, signup: viewSignup, forgot: viewForgot, pricing: viewPricing, help: viewHelp, privacy: viewPrivacy, 'privacy-kids': viewKidsPrivacy, terms: viewTerms, cookies: viewCookies, verify: viewVerify };
  const ACCOUNT = { staff: viewStaff, teacher: viewStaff };
  const LEARNER = { home: viewHome, unit3: viewUnit, test: viewTest, result: viewResult, remedial: viewRemedial, map: viewMap, profile: viewProfile, topic: viewTopic, bank: viewBank, drill: viewDrill, board: viewBoard, cert: viewCert, shop: viewShop, settings: viewSettings };
  const GUEST_WALL = { board: 'Sign up free to join the leaderboard', cert: 'Sign up free to earn a certificate', result: 'Sign up free to take the Unit Test', remedial: 'Sign up free to take the Unit Test', settings: 'Sign up free to get your own account' };
  let renderSeq = 0;
  async function render() {
    if (activeVideo) { try { activeVideo.pause(); } catch (e) { } activeVideo = null; }
    clearInterval(timer); const seq = ++renderSeq;
    st = Core.cur(); let r = location.hash.slice(1) || 'home';
    if (r !== 'test') UI.testOn = false;
    document.body.classList.remove('menu-open', 'toc-open');
    const me = Core.S.me;
    const needsLearner = !!LEARNER[r] && r !== 'home' || /^(v|ex|ws)-/.test(r);
    if (['learners', 'add-learner', 'parent'].includes(r)) { location.replace('#home'); return; }   // old parent-area links
    if (!me && !st && (ACCOUNT[r] || needsLearner)) { if (/^(v|ex|ws)-3-1$/.test(r) || r === 'unit3') { Core.startGuest(); st = Core.cur(); } else { location.replace('#signin'); return; } }  // a link into topic 3.1 starts a guest session
    if (!me && ACCOUNT[r]) { location.replace('#signin'); return; }
    if (me && !st && needsLearner) { location.replace('#home'); return; }
    if (me && (r === 'signin' || r === 'signup')) { location.replace('#home'); return; }
    shell({ toc: TOC_ROUTES(r) }); const m = $main();
    try {
      if (r.startsWith('v-')) viewVideo(secFromRoute(r)); else if (r.startsWith('ex-')) viewExercises(secFromRoute(r)); else if (r.startsWith('ws-')) viewWorksheet(secFromRoute(r));
      else if (st && isGuest() && GUEST_WALL[r]) m.append(guestWall(GUEST_WALL[r]));
      else if (st && LEARNER[r]) await LEARNER[r](); else if (ACCOUNT[r]) await ACCOUNT[r](); else if (PUBLIC[r]) await PUBLIC[r](); else viewHome();
    } catch (e) { console.error(e); if (seq === renderSeq) m.append(el('div', { class: 'banner adv', role: 'alert' }, 'Something went wrong loading this page. ', el('button', { class: 'btn small', type: 'button', onclick: () => render() }, 'Try again'))); }
    if (seq !== renderSeq) return;
    if (r === 'staff') document.title = 'Atomic – Staff'; else document.title = 'Atomic Checkpoint – Science Stage 7';
    m.focus({ preventScroll: true }); window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', render);
  async function boot() {
    try {
      const res = await fetch('content/stage7-unit03.json'); if (!res.ok) throw new Error('content'); C = await res.json();
      if (Backend.demo && location.search.includes('reset')) Backend.demo.reset();
      await Core.boot(C);
    } catch (e) { console.error(e); document.getElementById('app').innerHTML = '<p style="padding:24px;font-family:sans-serif">Sorry – the course could not load. Please check your connection and reload the page.</p>'; return; }
    render();
  }
  window.AtomicApp = { render, go, get st() { return st; }, UI, get C() { return C; } };
  boot();
})();
