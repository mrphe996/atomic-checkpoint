"""One-off: turn the v1 single-device app.js into the v2 account-based app.js.
Usage: python3 assemble_app.py <web dir>"""
import sys, pathlib
W = pathlib.Path(sys.argv[1]); src = (W / 'app.js').read_text()
shell = (W / '_parts/shell.js').read_text(); account = (W / '_parts/account.js').read_text()

def rep(old, new, count=1):
    global src
    n = src.count(old)
    assert n == count, f'{n}x: {old[:80]}'
    src = src.replace(old, new)

def cut(start, end, new):
    """replace from the line containing start up to (not including) the line containing end"""
    global src
    i = src.index(start); i = src.rfind('\n', 0, i) + 1
    j = src.index(end, i); j = src.rfind('\n', 0, j) + 1
    src = src[:i] + new + src[j:]

rep("/* Atomic Education — Science Stage 7 · Unit 3 prototype. Views and routing.", "/* Atomic Education — Science Stage 7. Views and routing (v2: parent accounts, plans, server marking).")
rep("teacherOk: false,", "parentOk: false, staffTab: 'marking',")

# answer analytics (essential: needed to check question quality)
rep("const onCheck = card => (g) => { if (g.ok) burst(card); else { card.classList.remove('shake'); void card.offsetWidth; card.classList.add('shake'); } setTimeout(xpTick, 50); };",
    "const onCheck = (card, q, rec) => (g) => { if (g.ok) burst(card); else { card.classList.remove('shake'); void card.offsetWidth; card.classList.add('shake'); } setTimeout(xpTick, 50);\n"
    "    if (q && st) Backend.track('answer', { learner: st.id, unit: Core.UNIT, q: q.id, ok: !!g.ok, try: (rec && rec.tries) || 1 }); };")
rep("QE.practice(x.q, qh, { rec, seed: st.id, save: () => { Core.persist(); }, onCheck: onCheck(box),", "QE.practice(x.q, qh, { rec, seed: st.id, save: () => { Core.persist(); }, onCheck: onCheck(box, x.q, rec),")
rep("QE.practice(q, card, { rec, seed: st.id, save: () => Core.persist(), onCheck: onCheck(card),", "QE.practice(q, card, { rec, seed: st.id, save: () => Core.persist(), onCheck: onCheck(card, q, rec),")
rep("QE.practice(q, card, { rec, onCheck: onCheck(card), seed: st.id + 'r' + a.n,", "QE.practice(q, card, { rec, onCheck: onCheck(card, q, rec), seed: st.id + 'r' + a.n,")
rep("QE.practice(q, card, { rec, onCheck: onCheck(card), seed: st.id + d.ns,", "QE.practice(q, card, { rec, onCheck: onCheck(card, q, rec), seed: st.id + d.ns,")

# shell
cut("  function shell(opts) {", "  function tocBtn()", shell)

# toc
rep("us === 'sim' ? 'Simulated: passed (end-of-course test mode)'", "us === 'sim' ? 'Simulated: passed (preview tool)'")
rep("el('a', { href: '#map' }, '🧠 Mind map'), el('a', { href: '#result' }, '📊 Results & history'), el('a', { href: '#teacher' }, '🧑‍🏫 Teacher marking')",
    "el('a', { href: '#map' }, '🧠 Concept map'), el('a', { href: '#result' }, '📊 Results & history'), el('a', { href: '#bank' }, '🗂 Question Bank')")

# home: logged out -> landing; parent without learner -> who's learning
cut("    if (!st) {\n      const name = el('input'", "    const started = Object.keys(st.video)",
    "    if (!st) { if (Core.S.me) { go('learners'); return; } viewLanding(); return; }\n")
rep("el('h1', {}, `Hello, ${st.name.split(/\\s+/)[0]}! 👋`)", "el('h1', {}, `Hello, ${st.alias}! 👋`)")
rep("    m.append(el('div', { class: 'banner adv' }, el('b', {}, 'Trying the preview? ')",
    "    if (!Core.S.sub.active) m.append(el('div', { class: 'banner info', id: 'freeBanner' }, el('b', {}, 'Free plan: '), 'topic 3.1 is open. A grown-up can start a 7-day free trial to unlock all of Stage 7 and the Unit Test.', el('a', { class: 'btn small gold', href: '#pricing' }, 'See plans')));\n"
    "    if (Backend.mode === 'demo') m.append(el('div', { class: 'banner adv' }, el('b', {}, 'Trying the preview? ')")

# learning path: paywalled test card
rep("el('a', { class: 'btn small ' + (ts.state === 'locked' ? '' : 'primary shine'), href: ts.state === 'passed' ? '#result' : '#test', style: 'align-self:flex-start' }, ts.state === 'locked' ? 'See what\\'s missing' : ts.state === 'passed' ? 'See results' : 'Take the Unit Test', el('span', { class: 'arr' }, '→'))",
    "ts.state === 'paywall' ? el('a', { class: 'btn small gold', href: '#pricing', style: 'align-self:flex-start' }, 'Unlock with a Stage 7 plan', el('span', { class: 'arr' }, '→')) : el('a', { class: 'btn small ' + (ts.state === 'locked' ? '' : 'primary shine'), href: ts.state === 'passed' ? '#result' : '#test', style: 'align-self:flex-start' }, ts.state === 'locked' ? 'See what\\'s missing' : ts.state === 'passed' ? 'See results' : 'Take the Unit Test', el('span', { class: 'arr' }, '→'))")
rep("lock ? el('p', { class: 'muted', style: 'margin:0' }, '🔒 ' + lock.reason)",
    "lock ? el('p', { class: 'muted', style: 'margin:0' }, '🔒 ' + lock.reason, lock.paywall ? el('a', { href: '#pricing', style: 'margin-left:6px' }, 'See plans') : null)")

# unit page: no textbook resource map
cut("    const t = el('table', { class: 'grid' }, el('tr', {}, ...['Section', 'Objectives', \"Learner's Book\"", "  }\n  function resourcesTable() {", "")
cut("  function resourcesTable() {", "  /* ---------- lesson: video with pause questions", "")
rep("el('h2', { style: 'margin:0' }, 'Mind map'), el('a', { class: 'btn small', href: '#map' }, 'Open the interactive map'", "el('h2', { style: 'margin:0' }, 'Concept map'), el('a', { class: 'btn small', href: '#map' }, 'Open the interactive map'")

# video analytics
rep("const v = el('video', { playsinline: true, preload: 'auto', 'aria-label': `Lesson ${s.id} video` }); activeVideo = v;",
    "const v = el('video', { playsinline: true, preload: 'auto', 'aria-label': `Lesson ${s.id} video` }); activeVideo = v;\n"
    "    v.addEventListener('play', () => { if (!v._started) { v._started = true; Backend.track('video_start', { learner: st.id, unit: Core.UNIT, sec: sid }); } });")
rep("if (next()) return; if (!vs.completed) { vs.completed = true; Core.persist(); bumpXp(); }",
    "if (next()) return; if (!vs.completed) { vs.completed = true; Core.persist(); bumpXp(); Backend.track('video_complete', { learner: st.id, unit: Core.UNIT, sec: sid }); }")

# report a problem on question cards
rep("    card.append(el('p', { class: 'objline' }, el('b', { style: 'color:#1C2A3A' }, 'Learning objective: '), C.objectives[q.obj].t));\n  }",
    "    card.append(el('div', { class: 'btnrow between objline' }, el('span', {}, el('b', { style: 'color:#1C2A3A' }, 'Learning objective: '), C.objectives[q.obj].t, el('small', { class: 'muted' }, ` · ${C.objectives[q.obj].code || ''}`)),\n"
    "      el('button', { class: 'btn small ghost', type: 'button', id: 'reportQ', onclick: () => reportQuestion(q) }, '⚑ Report a problem')));\n  }")

# worksheets: no book page refs; paywall; British "Print"
rep("hdr(`Worksheet ${s.id} – ${s.title} (${s.lb})`)", "hdr(`Worksheet ${s.id} – ${s.title}`)")
rep("    const s = Core.sec(sid), m = $main(); if (!s) return go('home');\n    if (!st.ws.includes(sid))",
    "    const s = Core.sec(sid), m = $main(); if (!s) return go('home');\n    const lock = Core.secLock(st, s); if (lock && lock.paywall) { m.append(bar(`Unit 3 › ${s.id} › A4 worksheet`), lockScreen(`Worksheet ${s.id} is locked`, lock.reason, [lock])); return; }\n    if (!st.ws.includes(sid))")
rep("'🖨 In')", "'🖨 Print')", 2)

# certificate (server-issued, verifiable)
cut("  function viewCert() {", "  /* ---------- teacher ---------- */",
r"""  async function viewCert() {
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

""")
rep("g.fillText('Cambridge Lower Secondary Science · Atomic Checkpoint', 877, 850);", "g.fillText('Aligned to the Cambridge Lower Secondary Science curriculum framework', 877, 850);")
rep("g.fillText('ATOMIC EDUCATION · Compiled by Lưu Quang Nghĩa', 877, 1120);", "g.fillText('ATOMIC EDUCATION · Verify at atomic certificate check · not a Cambridge qualification', 877, 1120);")
# teacher view replaced by staff area
cut("  /* ---------- teacher ---------- */", "  /* ---------- question bank ---------- */", "")

# tester tools: server-side simulations
rep("""{ t: 'Reset', cls: 'primary', on: () => { const keep = { id: st.id, name: st.name, alias: st.alias }; Core.S.profiles[st.id] = null; delete Core.S.profiles[st.id]; Core.S.current = null; Core.newProfile(keep.name, keep.alias, keep.id); go('home'); } }""",
    """{ t: 'Reset', cls: 'primary', on: async () => { await Backend.demo.resetLearner(st.id); await Core.selectLearner(st.id); go('home'); } }""")
rep("  function testerTools() {\n", "  function testerTools() {\n    if (!Backend.demo) return null;\n")
rep("        btn('Complete all sections → Unit Test', () => { fill(C.sections.map(s => s.id)); }, 'simAll'),",
    "        btn('Complete all sections → Unit Test', () => { fill(C.sections.map(s => s.id)); }, 'simAll'),\n"
    "        el('button', { class: 'btn small', type: 'button', id: 'simOthers', onclick: async () => { await Backend.demo.simulateOtherUnits(st.id, 82); await Core.refreshResults(st); msg.textContent = 'Done – the other 13 units are marked as passed at 82%.'; setTimeout(render, 500); } }, 'Pass the other 13 units (82%)'),\n"
    "        el('button', { class: 'btn small', type: 'button', id: 'simStaff', onclick: () => { Backend.demo.setRole('admin'); msg.textContent = 'This account is now an administrator – open Staff from the parent menu.'; } }, 'Make this account staff'),")

# unit test: paywall, server marking
rep("    if (ts.state === 'locked') { m.append(bar('Unit 3 › Unit Test'),",
    "    if (ts.state === 'paywall') { m.append(bar('Unit 3 › Unit Test'), lockScreen('Unit Test 3 needs a Stage 7 plan', 'Unit Tests, marking and the certificate are part of the full course.', [{ what: 'a Stage 7 plan (7-day free trial)', route: 'pricing' }])); return; }\n"
    "    if (ts.state === 'locked') { m.append(bar('Unit 3 › Unit Test'),")
rep("has a written answer for your teacher to mark.", "has a written answer for an Atomic marker to mark. We will notify you when it is done.")
rep("'Solutions appear after you submit. The written answer is marked by your teacher.'", "'Solutions appear after you submit. Most questions are marked straight away; written answers are marked by an Atomic marker.'")
rep("${q.teacher ? ' · teacher-marked' : ''}", "${q.teacher ? ' · marked by an Atomic marker' : ''}")
rep("""{ t: 'Finish test', cls: 'primary', on: () => {
        if (st.test.submitting) return; st.test.submitting = true; // guard double submit
        const a = Core.gradeAttempt(st, form, draft.answers); st.test.attempts.push(a); delete st.test.drafts[form]; st.test.submitting = false; Core.persist();
        UI.testOn = false; UI.testIdx = 0; UI.flags = {}; UI.testStart = null; clearInterval(timer); if (a.status === 'final' && a.passed) confetti(); go('result');
      } }""",
"""{ t: 'Finish test', cls: 'primary', on: async () => {
        if (UI.submitting) return true; UI.submitting = true; // guard double submit; the server is idempotent on draft.key too
        draft.key = draft.key || (crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + Math.random()); Core.persist();
        const wait = modal('Marking your test…', 'Please keep this page open.', []);
        try {
          const r = await Core.submitTest(st, form, draft.answers, draft.key); delete st.test.drafts[form]; Core.persist(); Core.flush();
          UI.testOn = false; UI.testIdx = 0; UI.flags = {}; UI.testStart = null; clearInterval(timer); wait(); if (r.attempt.status === 'final' && r.attempt.passed) confetti(); go('result');
        } catch (x) { wait(); modal('Could not submit', errText(x) + ' Your answers are saved as a draft.', [{ t: 'OK', cls: 'primary' }]); }
        finally { UI.submitting = false; }
      } }""")

# results: refresh from server, solutions from the server
rep("    Core.pullGrades().then(ch => { if (ch && location.hash === '#result') render(); });",
    "    const before = JSON.stringify(Core.attempts(st).map(a => a.status));\n"
    "    Core.refreshAttempts(st).then(() => { if (JSON.stringify(Core.attempts(st).map(a => a.status)) !== before && location.hash === '#result') render(); }).catch(() => { });")
rep("'Your written answer is waiting for your teacher. Pass/not passed and unlocking Unit 4 are decided only when the final mark is in.'",
    "'Your written answer is waiting for an Atomic marker. Pass/not passed and unlocking Unit 4 are decided only when the final mark is in – you will get a notification.'")
rep("el('p', { class: 'muted' }, 'Answer: ' + QE.answerText(q))", "el('p', { class: 'muted' }, 'Answer: ' + (((st.solutions || {})[q.id] || {}).answer || 'shown on the device that submitted this attempt'))")

# concept map
rep("""el('h1', { style: 'margin:0;font-size:36px' }, 'Mind map'), el('p', { class: 'muted', style: 'margin:4px 0 0' }, "Redrawn from LET'S MAP IT in the Stage 7 Learner's Book (Atomic's own mind maps were not among the resources provided).")""",
    """el('h1', { style: 'margin:0;font-size:36px' }, 'Concept map'), el('p', { class: 'muted', style: 'margin:4px 0 0' }, 'How the big ideas of Unit 3 connect. Tap a branch to zoom in.')""")
rep("const m = $main(); if (st) m.append(bar('Unit 3 › Mind map'));", "const m = $main(); if (st) m.append(bar('Unit 3 › Concept map'));")
rep('aria-label="Cells mind map"', 'aria-label="Cells concept map"')

# profile
rep("el('span', { style: 'color:#DCE8FA' }, `Nickname “${st.alias}” · ` + (Core.cloud.ready && st.id.startsWith('c_') ? 'progress saved to your account' : 'progress saved on this device only'))",
    "el('span', { style: 'color:#DCE8FA' }, `Nickname “${st.alias}” · progress saved to your family account`)")
rep("el('h2', { style: 'margin:0;color:#fff' }, st.name)", "el('h2', { style: 'margin:0;color:#fff' }, st.alias)")
cut("    const tg = el('input', { type: 'checkbox', id: 'endMode' });", "    m.append(testerTools());", "")
rep("""el('button', { class: 'btn small ghost', type: 'button', id: 'switchStudent', onclick: () => { Core.S.current = null; st = null; Core.persist(); go('home'); } }, 'Sign out / choose another learner')""",
    """el('button', { class: 'btn small ghost', type: 'button', id: 'switchStudent', onclick: () => { Core.leaveLearner(); st = null; go('learners'); } }, 'Switch learner')""")
rep("(rs ? rs.score.toFixed(2) + '% (' + rs.units + ' Unit)' : 'none yet')", "(rs ? rs.score.toFixed(2) + '% (' + rs.units + (rs.units === 1 ? ' unit)' : ' units)') : 'none yet')")

# leaderboard from the server (opt-in only)
cut("    const holder = el('div'); m.append(holder);", "  /* ---------- router ---------- */",
r"""    const holder = el('div'); m.append(holder);
    const live = await Backend.leaderboard(7).catch(() => []);
    const rows = live.filter(r => r.score != null).map(r => ({ alias: r.nickname, score: Number(r.score), units: r.units, me: !!r.is_mine && st && r.nickname === st.alias, src: r.opted_in ? 'Shown' : 'Only you can see this' }));
    if (Backend.mode === 'demo') SAMPLE.forEach(r => rows.push({ ...r, src: 'sample data' }));
    Core.competitionRank(rows);
    hin.append(el('span', { class: 'eyebrow', style: 'color:#F3BF69' }, 'SCIENCE STAGE 7'), el('h1', {}, '🏆 Leaderboard'),
      el('div', { class: 'formula' }, el('b', { style: 'color:#fff' }, 'Ranking score = (Σ first-pass % of each unit) ÷ number of units'), ' — every unit counts equally. Your first-pass % is fixed the moment you first pass a unit; revising or retaking later never changes it. Equal scores share a rank. XP is just for fun and is not used for ranking.'));
    const top = rows.slice(0, 3); const order = [top[1], top[0], top[2]];
    hin.append(el('div', { class: 'podium' }, ...order.map((r, k) => r ? el('div', { class: 'p' }, k === 1 ? el('span', { style: 'font-size:30px;animation:floaty 2.2s ease-in-out infinite' }, '👑') : null, el('span', { class: 'av', style: r.me ? 'background:#F3BF69;color:#1C2A3A' : '' }, r.alias.replace('Sample · ', '').slice(0, 1).toUpperCase()), el('b', { class: 'lex' }, r.alias + (r.me ? ' (you)' : '')), el('small', { style: 'color:#C9D6EA' }, r.score.toFixed(2) + '%'),
      el('div', { class: 'blk', style: `height:${[130, 170, 100][k]}px;background:${['#2F6FD6', '#0149AF', '#5B8FDB'][k]}` }, el('b', {}, String(r.rank)))) : el('div', { class: 'p' }))));
    const hidden = st && !(st.learner && st.learner.leaderboard_opt_in);
    if (hidden) holder.append(el('div', { class: 'banner info', id: 'lbHidden' }, el('b', {}, 'You are hidden. '), 'Only you can see your own row. A grown-up can choose to show your nickname in the parent area.'));
    holder.append(el('div', { class: 'card lbtable' }, el('div', { class: 'lbrow h' }, el('span', {}, 'RANK'), el('span', {}, 'LEARNER'), el('span', {}, 'RANKING SCORE'), el('span', {}, 'UNITS'), el('span', { class: 'xpcol' }, 'VISIBILITY')),
      el('div', { id: 'boardTable' }, ...(rows.length ? rows.map(r => el('div', { class: 'lbrow' + (r.me ? ' me' : ''), role: 'row' }, el('span', { class: 'rk' }, String(r.rank)), el('span', { class: 'who' }, el('span', { class: 'a' }, r.alias.replace('Sample · ', '').slice(0, 1).toUpperCase()), el('b', {}, r.alias + (r.me ? ' (you)' : ''))), el('span', { class: 'sc' }, r.score.toFixed(2) + '%'), el('span', {}, String(r.units)), el('span', { class: 'xpcol muted' }, r.src))) : [el('p', { class: 'muted', style: 'padding:16px 24px' }, 'No ranked learners yet – pass a Unit Test to appear here.')]))),
      el('p', { class: 'muted' }, 'Only nicknames are shown, and only for learners whose parent has switched the leaderboard on.' + (Backend.mode === 'demo' ? ' Rows marked “sample data” are illustrations, not real learners.' : '')));
  }

""")
rep("  function viewBoard() {", "  async function viewBoard() {")

# account / parent / plans / help / legal / staff views
rep("  /* ---------- router ---------- */\n  const TOC_ROUTES", account + "\n  /* ---------- router ---------- */\n  const TOC_ROUTES")

cut("  const TOC_ROUTES = r =>", "  window.AtomicApp = {",
r"""  const TOC_ROUTES = r => r.startsWith('v-') || r.startsWith('ex-') || r.startsWith('ws-') || ['unit3', 'map', 'result', 'remedial', 'topic', 'drill', 'cert'].includes(r);
  const PUBLIC = { home: () => viewHome(), signin: viewSignin, signup: viewSignup, forgot: viewForgot, pricing: viewPricing, help: viewHelp, privacy: viewPrivacy, terms: viewTerms, cookies: viewCookies, verify: viewVerify };
  const PARENT = { learners: viewLearners, 'add-learner': viewAddLearner, parent: viewParent, settings: viewSettings, staff: viewStaff, teacher: viewStaff };
  const LEARNER = { home: viewHome, unit3: viewUnit, test: viewTest, result: viewResult, remedial: viewRemedial, map: viewMap, profile: viewProfile, topic: viewTopic, bank: viewBank, drill: viewDrill, board: viewBoard, cert: viewCert };
  let renderSeq = 0;
  async function render() {
    if (activeVideo) { try { activeVideo.pause(); } catch (e) { } activeVideo = null; }
    clearInterval(timer); const seq = ++renderSeq;
    st = Core.cur(); let r = location.hash.slice(1) || 'home';
    if (r !== 'test') UI.testOn = false;
    document.body.classList.remove('menu-open', 'toc-open');
    const me = Core.S.me;
    const needsLearner = !!LEARNER[r] && r !== 'home' || /^(v|ex|ws)-/.test(r);
    if (!me && (PARENT[r] || needsLearner)) { location.replace('#signin'); return; }
    if (me && !st && needsLearner) { location.replace('#learners'); return; }
    if (me && (r === 'signin' || r === 'signup')) { location.replace('#learners'); return; }
    shell({ toc: TOC_ROUTES(r) }); const m = $main();
    try {
      if (r.startsWith('v-')) viewVideo(secFromRoute(r)); else if (r.startsWith('ex-')) viewExercises(secFromRoute(r)); else if (r.startsWith('ws-')) viewWorksheet(secFromRoute(r));
      else if (st && LEARNER[r]) await LEARNER[r](); else if (PARENT[r]) await PARENT[r](); else if (PUBLIC[r]) await PUBLIC[r](); else viewHome();
    } catch (e) { console.error(e); if (seq === renderSeq) m.append(el('div', { class: 'banner adv', role: 'alert' }, 'Something went wrong loading this page. ', el('button', { class: 'btn small', type: 'button', onclick: () => render() }, 'Try again'))); }
    if (seq !== renderSeq) return;
    if (r === 'staff' || r === 'parent') document.title = 'Atomic – ' + (r === 'staff' ? 'Staff' : 'Parent area'); else document.title = 'Atomic Checkpoint – Science Stage 7';
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
""")
rep("window.AtomicApp = { render, go, get st() { return st; }, UI };", "window.AtomicApp = { render, go, get st() { return st; }, UI, get C() { return C; } };")

# remaining book / legacy references must be gone
for bad in ["Core.cloud", "Core.newProfile", "Core.gradeAttempt", "Core.pullGrades", "Core.certFor", "endMode", "s.lb", "LET'S MAP", "Learner's Book", "Core.init(", "teacherOk"]:
    assert bad not in src, bad
(W / 'app.js').write_text(src)
print('ok', len(src.splitlines()), 'lines')
