/* Atomic Education — learner state, course rules and access.
   The learner's progress lives in the backend (Backend.saveProgress); marking happens on the server
   (Backend.submitTest) – this file only mirrors results for the screens. */
(function () {
  const UNIT = 'stage7-unit03';
  const STAGE_UNITS = 14;
  const FREE_SECTIONS = ['3.1'];
  let C = null;
  const BILLING_OFF = ((window.ATOMIC_CONFIG || {}).billing || 'off') === 'off';
  const BETA = { active: true, status: 'beta', plan: 'beta' };
  const getSub = () => (BILLING_OFF ? Promise.resolve(BETA) : Backend.subscription());
  const S = { profiles: {}, current: null, me: null, learners: [], sub: { active: false, status: 'none' }, notes: [] };

  const fresh = l => ({ id: l.id, name: l.certificate_name || l.nickname, alias: l.nickname, created: Date.parse(l.created_at) || Date.now(), ts: Date.now(),
    video: {}, items: {}, stopsWrong: {}, test: { drafts: {}, attempts: [] }, rem: {}, ws: [], last: null, cert: null, rank: {}, results: {}, days: [] });
  const META = ['id', 'name', 'alias', 'results', 'cert', 'learner'];

  /* ---------- session ---------- */
  async function boot(content) {
    C = content; S.me = await Backend.me(); S.profiles = {}; S.current = null; S.guest = false;
    if (!S.me) { if (guestSaved()) startGuest(); return S; }   // a returning visitor carries on where they stopped
    S.learners = await Backend.learners();
    S.sub = await getSub().catch(() => ({ active: false, status: 'none' }));
    const own = S.learners.find(l => l.user_id === S.me.user.id) || S.learners[0];
    let want = null; try { want = sessionStorage.getItem('atomic.learner'); } catch (e) { }
    const pick = (want && S.learners.find(l => l.id === want)) || own;
    if (pick) { await selectLearner(pick.id); await adoptGuest(); }
    return S;
  }

  /* ---------- guest: try topic 3.1 without an account (progress kept in this browser only) ---------- */
  const GKEY = 'atomic.guest.v1';
  const guestSaved = () => { try { return !!localStorage.getItem(GKEY); } catch (e) { return false; } };
  function startGuest() {
    let saved = null; try { saved = JSON.parse(localStorage.getItem(GKEY)); } catch (e) { }
    const st = Object.assign(fresh({ id: 'guest', nickname: 'Guest', created_at: new Date().toISOString() }), saved || {});
    st.id = 'guest'; st.alias = 'Guest'; st.name = 'Guest'; st.test = st.test || { drafts: {}, attempts: [] }; st.test.attempts = [];
    S.profiles = { guest: st }; S.current = 'guest'; S.guest = true;
    try { localStorage.setItem(GKEY, JSON.stringify(strip(st))); } catch (e) { }
    return st;
  }
  // after sign-up / sign-in: bring the guest's work into the new account (only if the account has nothing yet)
  async function adoptGuest() {
    if (!guestSaved()) return false; const st = cur(); if (!st) return false;
    let g = null; try { g = JSON.parse(localStorage.getItem(GKEY)); } catch (e) { }
    const empty = !Object.keys(st.items || {}).length && !Object.values(st.video || {}).some(v => v && (v.completed || v.pos > 1 || Object.keys(v.stops || {}).length));
    if (g && empty) { for (const k of ['video', 'items', 'stopsWrong', 'ws', 'days', 'marks']) if (g[k]) st[k] = g[k]; dirty = true; flush(); }
    try { localStorage.removeItem(GKEY); } catch (e) { }
    return !!(g && empty);
  }
  const strip = st => { const c = {}; for (const k of Object.keys(st)) if (!META.includes(k)) c[k] = st[k]; c.test = { drafts: (st.test || {}).drafts || {} }; return c; };
  async function selectLearner(id) {
    const l = S.learners.find(x => x.id === id); if (!l) return null;
    const saved = await Backend.loadProgress(id, UNIT);
    const st = Object.assign(fresh(l), saved || {});
    st.id = l.id; st.name = l.certificate_name || l.nickname; st.alias = l.nickname; st.learner = l;
    st.test = st.test || { drafts: {}, attempts: [] };
    st.test.attempts = await Backend.attempts(id, UNIT);
    st.results = await Backend.unitResults(id); st.rank = { u3: st.results[UNIT] ? st.results[UNIT].pct : null };
    st.cert = await Backend.certificate(id);
    S.profiles = { [id]: st }; S.current = id;
    try { sessionStorage.setItem('atomic.learner', id); } catch (e) { }
    return st;
  }
  function leaveLearner() { flush(); S.current = null; S.profiles = {}; try { sessionStorage.removeItem('atomic.learner'); } catch (e) { } }
  async function refreshAccount() { S.me = await Backend.me(); if (!S.me) return; S.learners = await Backend.learners(); S.sub = await getSub().catch(() => S.sub); }

  const cur = () => (S.current ? S.profiles[S.current] : null);
  let saveTimer = null, dirty = false;
  function persist() {
    const st = cur(); if (!st) return;
    st.ts = Date.now(); const d = today(); st.days = st.days || []; if (!st.days.includes(d)) st.days.push(d);
    dirty = true; clearTimeout(saveTimer); saveTimer = setTimeout(flush, 800);
  }
  function flush() {
    const st = cur(); if (!st || !dirty) return; dirty = false;
    if (S.guest) { try { localStorage.setItem(GKEY, JSON.stringify(strip(st))); } catch (e) { } return; }
    Backend.saveProgress(st.id, UNIT, strip(st)).catch(() => { dirty = true; }); // attempts live on the server
  }
  window.addEventListener('pagehide', flush);

  /* ---------- access ---------- */
  const canOpen = secId => FREE_SECTIONS.includes(secId) || (!S.guest && !!S.sub.active);

  /* ---------- progress rules ---------- */
  const secs = () => C.sections;
  const sec = id => C.sections.find(s => s.id === id);
  const vstate = (st, sid) => (st.video[sid] = st.video[sid] || { pos: 0, stops: {}, completed: false });
  const stopDone = (st, sid, stop) => !!((vstate(st, sid).stops[stop.id] || {}).done);
  const stopsLeft = (st, s) => s.stops.filter(x => !stopDone(st, s.id, x));
  const videoDone = (st, s) => vstate(st, s.id).completed && stopsLeft(st, s).length === 0;
  const reqLeft = (st, s) => s.req.filter(q => !((st.items[q.id] || {}).done));
  const secDone = (st, s) => videoDone(st, s) && reqLeft(st, s).length === 0;
  const secIndex = sid => C.sections.findIndex(s => s.id === sid);
  function secLock(st, s) {
    if (!canOpen(s.id)) return S.guest ? { reason: 'Guests can try topic 3.1. Create a free account to unlock every topic and save your progress.', what: 'a free account', route: 'signup', paywall: true, guest: true }
      : { reason: 'This topic is part of the full Stage 7 course.', what: 'a Stage 7 plan (7-day free trial)', route: 'pricing', paywall: true };
    const i = secIndex(s.id); if (i <= 0) return null;
    const prev = C.sections[i - 1]; if (secDone(st, prev)) return null;
    return { reason: `Finish section ${prev.id} first.`, ...firstMissingIn(st, prev) };
  }
  function firstMissingIn(st, s) {
    if (!videoDone(st, s)) return { what: `Section ${s.id} video (${stopsLeft(st, s).length} pause question(s) left${vstate(st, s.id).completed ? '' : ', not watched to the end'})`, route: 'v-' + s.id.replace('.', '-') };
    const q = reqLeft(st, s)[0]; if (!q) return null;
    const i = s.req.indexOf(q);
    return { what: `the “${QE.TYPE_VI[q.type]}” task (Core question ${i + 1}) in section ${s.id}`, route: 'ex-' + s.id.replace('.', '-'), idx: i, tab: 'req' };
  }
  function missingForTest(st) {
    const out = [];
    for (const s of secs()) {
      if (!videoDone(st, s)) out.push({ what: `Section ${s.id} video – ${s.title}` + (stopsLeft(st, s).length ? ` (${stopsLeft(st, s).length} pause question(s) left)` : ' (not watched to the end)'), route: 'v-' + s.id.replace('.', '-') });
      reqLeft(st, s).forEach(q => { const i = s.req.indexOf(q); out.push({ what: `Section ${s.id} · Core question ${i + 1}: ${QE.TYPE_VI[q.type]} – “${q.prompt.slice(0, 60)}${q.prompt.length > 60 ? '…' : ''}”`, route: 'ex-' + s.id.replace('.', '-'), idx: i, tab: 'req' }); });
    }
    return out;
  }

  /* ---------- test (marked on the server) ---------- */
  const attempts = st => st.test.attempts;
  const lastAttempt = st => attempts(st)[attempts(st).length - 1] || null;
  const passed = st => attempts(st).some(a => a.status === 'final' && a.passed);
  const isPass = (score, max) => TestRules.isPass(score, max);
  const nextForm = st => TestRules.nextForm(attempts(st).length);
  const remKey = (a, qid) => `rem${a.n}:${qid}`;
  const remLeft = (st, a) => (a.remed || []).filter(id => !((st.rem[remKey(a, id)] || {}).done));
  function testState(st) {
    if (S.guest) return { state: 'guest' };
    if (!S.sub.active) return { state: 'paywall' };
    const miss = missingForTest(st); if (miss.length) return { state: 'locked', miss };
    const la = lastAttempt(st);
    if (passed(st)) return { state: 'passed', last: la };
    if (!la) return { state: 'ready', form: 'A' };
    if (la.status === 'pending') return { state: 'pending', last: la };
    if (remLeft(st, la).length) return { state: 'remediate', last: la, left: remLeft(st, la) };
    return { state: 'ready', form: nextForm(st), retake: true };
  }
  async function submitTest(st, form, answers, clientKey) {
    flush(); dirty = true; await Backend.saveProgress(st.id, UNIT, (() => { const c = {}; for (const k of Object.keys(st)) if (!META.includes(k)) c[k] = st[k]; c.test = { drafts: st.test.drafts }; return c; })());
    const r = await Backend.submitTest({ learnerId: st.id, unit: UNIT, form, answers, clientKey });
    const i = st.test.attempts.findIndex(a => a.id === r.attempt.id);
    if (i >= 0) st.test.attempts[i] = r.attempt; else st.test.attempts.push(r.attempt);
    st.solutions = Object.assign(st.solutions || {}, r.solutions);
    await refreshResults(st); return r;
  }
  async function refreshAttempts(st) { st.test.attempts = await Backend.attempts(st.id, UNIT); await refreshResults(st); }
  async function refreshResults(st) { st.results = await Backend.unitResults(st.id); st.rank = { u3: st.results[UNIT] ? st.results[UNIT].pct : null }; }

  /* ---------- course / ranking / certificate ---------- */
  function unitStatus(st, n) {
    if (n === 3) return passed(st) ? 'passed' : 'open';
    const u = 'stage7-unit' + String(n).padStart(2, '0');
    if (st.results && st.results[u]) return 'sim';
    if (n === 4) return passed(st) ? 'unlocked' : 'locked';
    return 'na';
  }
  function rankScore(st) {
    const list = Object.values(st.results || {}).map(r => r.pct);
    if (!list.length) return null;
    return { score: list.reduce((a, b) => a + b, 0) / list.length, units: list.length };
  }
  const stageComplete = st => Object.keys(st.results || {}).length >= STAGE_UNITS;
  async function certificate(st) { if (S.guest) return null; if (st.cert) return st.cert; if (!stageComplete(st)) return null; st.cert = await Backend.issueCertificate(st.id, STAGE_UNITS); return st.cert; }
  function competitionRank(rows) {
    rows.sort((a, b) => b.score - a.score);
    let prev = null, rank = 0; rows.forEach((r, i) => { const k = Math.round(r.score * 100); if (k !== prev) { rank = i + 1; prev = k; } r.rank = rank; });
    return rows;
  }

  /* ---------- XP & streak (motivation only; never used for ranking) ---------- */
  function xp(st) {
    let x = 0;
    C.sections.forEach(s => {
      const vs = vstate(st, s.id); s.stops.forEach(t => { const r = vs.stops[t.id]; if (r && r.done) x += r.ok && r.tries === 1 ? 10 : 5; });
      if (vs.completed) x += 20;
      s.req.concat(s.prac, s.adv).forEach(q => { const r = st.items[q.id]; if (r && r.done) x += Math.round((r.score || 0) * 10) + 2 + (q.adv && r.ok ? 10 : 0); });
    });
    if (passed(st)) x += 100; x += (st.ws || []).length * 5;
    return x;
  }
  /* ---------- streak: consecutive days with any learning activity ---------- */
  const pad = n => String(n).padStart(2, '0');
  const dstr = d => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  const today = () => dstr(new Date());
  function streak(st) {
    const days = new Set(st.days || []); let n = 0; const d = new Date();
    if (!days.has(dstr(d))) d.setDate(d.getDate() - 1);   // today does not break the streak until it is over
    while (days.has(dstr(d))) { n++; d.setDate(d.getDate() - 1); }
    return n;
  }
  function week(st) {   // Monday→Sunday of this week: [{d, label, met, today}]
    const days = new Set(st.days || []), out = [], d = new Date(); const t = dstr(d); d.setDate(d.getDate() - ((d.getDay() + 6) % 7));
    for (let i = 0; i < 7; i++) { const k = dstr(d); out.push({ d: k, label: 'MTWTFSS'[i], met: days.has(k), today: k === t }); d.setDate(d.getDate() + 1); }
    return out;
  }


  /* ---------- next activity ---------- */
  function nextActivity(st) {
    for (const s of secs()) {
      const lock = secLock(st, s);
      if (lock) { if (lock.guest) return { label: 'Sign up free to unlock topic 3.2', route: 'signup' }; if (lock.paywall) return { label: 'Unlock the rest of Stage 7', route: 'pricing' }; break; }
      if (!videoDone(st, s)) return { label: `Watch the section ${s.id} video`, route: 'v-' + s.id.replace('.', '-') };
      const q = reqLeft(st, s)[0]; if (q) return { label: `Core practice for section ${s.id}`, route: 'ex-' + s.id.replace('.', '-'), tab: 'req', idx: s.req.indexOf(q) };
    }
    const ts = testState(st);
    if (ts.state === 'guest') return { label: 'Sign up free to take the Unit Test', route: 'signup' };
    if (ts.state === 'paywall') return { label: 'Unlock the Unit Test', route: 'pricing' };
    if (ts.state === 'ready') return { label: ts.retake ? `Retake the Unit Test (Paper ${ts.form})` : 'Take Unit Test 3', route: 'test' };
    if (ts.state === 'remediate') return { label: 'Do your review questions', route: 'remedial' };
    if (ts.state === 'pending') return { label: 'See your results (awaiting marking)', route: 'result' };
    if (stageComplete(st)) return { label: 'Get your certificate', route: 'cert' };
    return { label: 'See your Unit 3 results', route: 'result' };
  }

  /* ---------- tiny PDF writer (one JPEG page) ---------- */
  function jpegPdf(jpegBytes, w, h, pageW, pageH) {
    const enc = new TextEncoder(); const parts = []; const offs = []; let len = 0;
    const push = b => { const u = typeof b === 'string' ? enc.encode(b) : b; parts.push(u); len += u.length; };
    push('%PDF-1.4\n');
    const obj = (n, body) => { offs[n] = len; push(`${n} 0 obj\n`); body(); push('\nendobj\n'); };
    obj(1, () => push('<< /Type /Catalog /Pages 2 0 R >>'));
    obj(2, () => push('<< /Type /Pages /Kids [3 0 R] /Count 1 >>'));
    obj(3, () => push(`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${pageW} ${pageH}] /Resources << /XObject << /Im0 4 0 R >> >> /Contents 5 0 R >>`));
    obj(4, () => { push(`<< /Type /XObject /Subtype /Image /Width ${w} /Height ${h} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length ${jpegBytes.length} >>\nstream\n`); push(jpegBytes); push('\nendstream'); });
    const cs = `q ${pageW} 0 0 ${pageH} 0 0 cm /Im0 Do Q`;
    obj(5, () => push(`<< /Length ${cs.length} >>\nstream\n${cs}\nendstream`));
    const xref = len; let x = 'xref\n0 6\n0000000000 65535 f \n'; for (let i = 1; i <= 5; i++) x += String(offs[i]).padStart(10, '0') + ' 00000 n \n';
    push(x + `trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF`);
    const out = new Uint8Array(len); let p = 0; parts.forEach(u => { out.set(u, p); p += u.length; }); return out;
  }
  async function saveFile(filename, data) {
    try {
      const dl = window.claude && claude.use ? await Promise.race([claude.use('downloads'), new Promise(r => setTimeout(() => r(null), 3000))]) : null;
      if (dl) { await dl.save({ filename, data }); return 'saved'; }
    } catch (e) { if (e && e.code === 'declined') return 'declined'; }
    try { const blob = data instanceof Blob ? data : new Blob([data]); const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = filename; document.body.append(a); a.click(); a.remove(); return 'saved'; }
    catch (e) { return 'failed'; }
  }

  window.Core = {
    UNIT, STAGE_UNITS, FREE_SECTIONS, BILLING_OFF, get S() { return S; }, get C() { return C; },
    boot, selectLearner, leaveLearner, refreshAccount, cur, persist, flush, canOpen,
    sec, secs, vstate, stopDone, stopsLeft, videoDone, reqLeft, secDone, secLock, firstMissingIn, missingForTest,
    attempts, lastAttempt, passed, isPass, nextForm, remKey, remLeft, testState, submitTest, refreshAttempts, refreshResults,
    unitStatus, rankScore, xp, streak, stageComplete, startGuest, adoptGuest,
    week, today, certificate, competitionRank, nextActivity, jpegPdf, saveFile
  };
})();
