/* Atomic Education — learner state, course rules and access.
   The learner's progress lives in the backend (Backend.saveProgress); marking happens on the server
   (Backend.submitTest) – this file only mirrors results for the screens. */
(function () {
  const STAGES = [3, 4, 5, 6, 7, 8, 9, 16, 17, 18, 19], STAGE_UNITS = 14;
  // course keys: 7–9 = Science Stages 7–9; 10 + N = Mathematics Stage N, 13–19 (same machinery, their own units, tests and certificates)
  const MATHS = g => g >= 10;
  // 3–6 = Cambridge Primary Science Stages 3 to 6 (animated lessons, listening and speaking checks, experiment rooms)
  const PRIMARY = g => g <= 6;
  const levelName = g => (PRIMARY(MATHS(g) ? g - 10 : g) ? 'Primary' : 'Lower Secondary');
  const stageNo = g => (MATHS(g) ? g - 10 : g);
  const subjectOf = g => (MATHS(g) ? 'Mathematics' : 'Science');
  const stageName = g => (MATHS(g) ? `Stage ${stageNo(g)} Mathematics` : `Stage ${g}`);
  const stageLabel = (g = STAGE) => (MATHS(g) ? `Stage ${stageNo(g)} Mathematics` : `Stage ${g} Science`);
  const unitCount = () => ((INDEX && INDEX.units && INDEX.units.length) || STAGE_UNITS);
  // the stage on screen (a learner can study every stage they are enrolled in)
  // stages switched off for learners (config lockedStages, e.g. Maths Stage 9 while it is reviewed); admins still open them
  const LOCKED = new Set((((window.ATOMIC_CONFIG || {}).lockedStages) || []).map(Number));
  const isAdminMe = me => !!(me && me.profile && me.profile.role === 'admin');
  const stageLocked = g => LOCKED.has(g) && !isAdminMe(S && S.me);
  let STAGE = (() => { try { const g = Number(localStorage.getItem('atomic.stage')); return STAGES.includes(g) ? g : 7; } catch (e) { return 7; } })();
  const pad2 = n => String(n).padStart(2, '0');
  const unitId = n => `stage${STAGE}-unit${pad2(n)}`;
  let UNO = 3;                       // the unit on screen
  let C = null, INDEX = null;        // C = that unit's content; INDEX = list of the stage's units
  const CACHE = {};
  const FREE_SECTIONS = { includes: id => /\.1$/.test(id) };   // the first topic of every unit is free
  const BILLING_OFF = ((window.ATOMIC_CONFIG || {}).billing || 'off') === 'off';
  const BETA = { active: true, status: 'beta', plan: 'beta' };
  const getSub = () => (BILLING_OFF ? Promise.resolve(BETA) : Backend.subscription());
  const S = { profiles: {}, current: null, me: null, learners: [], sub: { active: false, status: 'none' }, notes: [], states: {}, enrolments: [], final: null, finalAttempts: [] };

  const fresh = l => ({ id: l.id, name: l.certificate_name || l.nickname, alias: l.nickname, created: Date.parse(l.created_at) || Date.now(), ts: Date.now(),
    video: {}, items: {}, stopsWrong: {}, test: { drafts: {}, attempts: [] }, rem: {}, ws: [], last: null, cert: null, rank: {}, results: {}, days: [], time: 0 });
  const META = ['id', 'name', 'alias', 'results', 'cert', 'learner'];

  /* ---------- session ---------- */
  async function loadIndex() {
    if (INDEX) return INDEX;
    const setP = Backend.unitSettings().catch(() => []);
    let r = await fetch(`content/stage${STAGE}.json`);
    if (!r.ok && STAGE !== 7) { STAGE = 7; r = await fetch('content/stage7.json'); }
    INDEX = r.ok ? await r.json() : { units: [] };
    try { const hid = (await setP).filter(x => x.hidden).map(x => x.unit); INDEX.units.forEach(u => { if (hid.includes(`stage${STAGE}-unit${String(u.n).padStart(2, '0')}`)) { u.ready = false; u.hiddenByAdmin = true; } }); INDEX.hiddenExtra = hid; } catch (e) { }
    return INDEX;
  }
  // one request per unit even when the sidebar and the page ask for it at the same time; the content and its admin changes load side by side
  const PENDING = {};
  function fetchUnit(n) {
    if (CACHE[n]) return Promise.resolve(CACHE[n]);
    const id = unitId(n), key = id;
    if (!PENDING[key]) PENDING[key] = Promise.all([fetch(`content/${id}.json`).then(r => { if (!r.ok) throw new Error('content'); return r.json(); }), Backend.contentOverrides(id).catch(() => null)])
      .then(([pack, rows]) => { const out = applyRows(pack, rows); if (unitId(n) === id) CACHE[n] = out; return out; }).finally(() => { delete PENDING[key]; });
    return PENDING[key];
  }
  async function loadUnit(n) {
    await fetchUnit(n);
    UNO = n; C = CACHE[n]; try { sessionStorage.setItem('atomic.unit', String(n)); } catch (e) { }
    return C;
  }
  async function peekUnit(n) { return fetchUnit(n); }
  // admin changes (edited or withdrawn questions) are applied to the built content as it loads
  function applyRows(pack, rows) { try { if (!rows || !rows.length) return pack; const ov = {}; rows.forEach(r => { ov[r.question_id] = { hidden: r.hidden, patch: r.patch }; }); return GradeCore.applyOverrides(pack, ov); } catch (e) { return pack; } }
  async function withOv(unit, pack) { try { return applyRows(pack, await Backend.contentOverrides(unit)); } catch (e) { return pack; } }
  async function dropCache() { for (const k of Object.keys(CACHE)) delete CACHE[k]; FINAL = null; CP = null; if (UNO) { try { await loadUnit(UNO); } catch (e) { } } }
  const cached = n => CACHE[n] || null;
  let FINAL = null, CP = null;
  async function loadFinal() { if (!FINAL) { const r = await fetch(`content/stage${STAGE}-final.json`); FINAL = r.ok ? await withOv(`stage${STAGE}-final`, await r.json()) : null; } return FINAL; }
  const unitReady = n => !!((INDEX && INDEX.units.find(u => u.n === n)) || {}).ready;
  // open another unit: every unit is open at any time (no need to finish the one before)
  async function switchUnit(n) {
    if (n === UNO && C) return C;
    if (!unitReady(n)) throw new Error('not_ready');
    const was = cur(); flush();
    await loadUnit(n);
    if (S.guest) { const days = was ? was.days : []; startGuest(); const st = cur(); st.days = Array.from(new Set([...(st.days || []), ...(days || [])])); }
    else if (S.current) { const days = was ? was.days : []; await selectLearner(S.current); const st = cur(); st.days = Array.from(new Set([...(st.days || []), ...(days || [])])); }
    return C;
  }
  async function switchStage(g) {
    if (!STAGES.includes(g)) throw new Error('stage'); if (stageLocked(g)) throw new Error('locked'); if (g === STAGE && INDEX && C) return C;
    flush(); STAGE = g; INDEX = null; C = null; FINAL = null; CP = null; for (const k of Object.keys(CACHE)) delete CACHE[k];
    try { localStorage.setItem('atomic.stage', String(g)); sessionStorage.removeItem('atomic.unit'); } catch (e) { }
    await loadIndex(); await loadUnit((INDEX.units.find(u => u.ready) || { n: 1 }).n);
    if (S.guest) startGuest(); else if (S.current) await selectLearner(S.current);
    return C;
  }
  async function boot() {
    const meP = Backend.me(); meP.catch(() => { });   // the account and the course content load side by side
    if (LOCKED.has(STAGE)) { const me0 = await meP.catch(() => null); if (!isAdminMe(me0)) { STAGE = 7; INDEX = null; C = null; for (const k of Object.keys(CACHE)) delete CACHE[k]; try { localStorage.setItem('atomic.stage', '7'); sessionStorage.removeItem('atomic.unit'); } catch (e) { } } }
    await loadIndex();
    let want = null; try { want = Number(sessionStorage.getItem('atomic.unit')); } catch (e) { }
    await loadUnit(want && unitReady(want) ? want : (INDEX.units.find(u => u.ready) || { n: 3 }).n);
    S.me = await meP; S.profiles = {}; S.current = null; S.guest = false;
    if (!S.me) { if (guestSaved()) startGuest(); return S; }   // a returning visitor carries on where they stopped
    S.learners = await Backend.learners();
    S.sub = await getSub().catch(() => ({ active: false, status: 'none' }));
    const own = S.learners.find(l => l.user_id === S.me.user.id) || S.learners[0];
    let wantL = null; try { wantL = sessionStorage.getItem('atomic.learner'); } catch (e) { }
    const pick = (wantL && S.learners.find(l => l.id === wantL)) || own;
    if (pick) { await selectLearner(pick.id); await adoptGuest(); }
    return S;
  }

  /* ---------- guest: try topic 3.1 without an account (progress kept in this browser only) ---------- */
  const gkey = () => 'atomic.guest.v1' + (STAGE === 7 ? '' : '.s' + STAGE) + (UNO === 3 && STAGE === 7 ? '' : '.u' + UNO);
  const guestSaved = () => { try { return Object.keys(localStorage).some(k => k.startsWith('atomic.guest.v1')); } catch (e) { return false; } };
  function startGuest() {
    let saved = null; try { saved = JSON.parse(localStorage.getItem(gkey())); } catch (e) { }
    const st = Object.assign(fresh({ id: 'guest', nickname: 'Guest', created_at: new Date().toISOString() }), saved || {});
    st.id = 'guest'; st.alias = 'Guest'; st.name = 'Guest'; st.test = st.test || { drafts: {}, attempts: [] }; st.test.attempts = [];
    S.profiles = { guest: st }; S.current = 'guest'; S.guest = true;
    try { localStorage.setItem(gkey(), JSON.stringify(strip(st))); } catch (e) { }
    S.states = {}; try { for (const k of Object.keys(localStorage)) if (k.startsWith('atomic.guest.v1')) { const m = k.match(/\.u(\d+)$/), sg = k.match(/\.s(\d+)\./); if ((sg ? +sg[1] : 7) !== STAGE) continue; S.states[unitId(m ? +m[1] : 3)] = JSON.parse(localStorage.getItem(k)); } } catch (e) { }
    S.states[UNIT()] = strip(st); lastXp = xpNow();
    return st;
  }
  // after sign-up / sign-in: bring the guest's work into the new account (only if the account has nothing yet)
  async function adoptGuest() {
    if (!guestSaved()) return false; const st = cur(); if (!st) return false;
    let g = null; try { g = JSON.parse(localStorage.getItem(gkey())); } catch (e) { }
    const empty = !Object.keys(st.items || {}).length && !Object.values(st.video || {}).some(v => v && (v.completed || v.pos > 1 || Object.keys(v.stops || {}).length));
    if (g && empty) { for (const k of ['video', 'items', 'stopsWrong', 'ws', 'days', 'marks']) if (g[k]) st[k] = g[k]; dirty = true; flush(); }
    try { localStorage.removeItem(gkey()); } catch (e) { }
    return !!(g && empty);
  }
  const strip = st => { const c = {}; for (const k of Object.keys(st)) if (!META.includes(k)) c[k] = st[k]; c.test = { drafts: (st.test || {}).drafts || {} }; return c; };
  async function selectLearner(id) {
    const l = S.learners.find(x => x.id === id); if (!l) return null;
    const saved = await Backend.loadProgress(id, UNIT());
    const st = Object.assign(fresh(l), saved || {});
    st.id = l.id; st.name = l.certificate_name || l.nickname; st.alias = l.nickname; st.learner = l;
    st.test = st.test || { drafts: {}, attempts: [] };
    st.test.attempts = await Backend.attempts(id, UNIT());
    st.results = await Backend.unitResults(id);
    if (Backend.allDays) { try { st.days = Array.from(new Set([...(st.days || []), ...(await Backend.allDays(id))])); } catch (e) { } }  // the streak counts every unit
    st.cert = await Backend.certificate(id, STAGE);
    try { S.states = (Backend.allStates ? await Backend.allStates(id) : {}) || {}; } catch (e) { S.states = {}; }
    try { S.enrolments = Backend.enrolments ? await Backend.enrolments(id) : []; } catch (e) { S.enrolments = []; }
    try { S.tester = Backend.isTester ? await Backend.isTester(id) : false; } catch (e) { S.tester = false; }
    S.profiles = { [id]: st }; S.current = id; S.states[UNIT()] = strip(st); lastXp = xpNow();
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
    S.states[UNIT()] = strip(st);
    const x = xpNow(); if (lastXp != null && x > lastXp) { const L0 = TestRules.levelOf(lastXp), L1 = TestRules.levelOf(x); try { window.dispatchEvent(new CustomEvent('atomic:xp', { detail: { gain: x - lastXp, xp: x, level: L1, levelUp: L1 > L0 } })); } catch (e) { } }
    lastXp = x;
    dirty = true; clearTimeout(saveTimer); saveTimer = setTimeout(flush, 800);
  }
  /* ---------- XP & levels across every unit (same formula as the server) ---------- */
  let lastXp = null;
  const unitPasses = () => { const st = cur(); return st ? Object.keys(st.results || {}).filter(k => !/-final$/.test(k)).length : 0; };
  const xpNow = () => TestRules.xpTotal(S.states, unitPasses());
  function levelInfo() { const xp = xpNow(), L = TestRules.levelOf(xp), a = TestRules.xpForLevel(L), b = TestRules.xpForLevel(L + 1); return { xp, level: L, from: a, to: b, pct: Math.round((xp - a) / (b - a) * 100) }; }
  /* ---------- study time: active seconds per unit (counted only while the page is visible and in use) ---------- */
  let lastAct = Date.now();
  const activity = () => { lastAct = Date.now(); };
  ['pointerdown', 'keydown', 'scroll', 'touchstart'].forEach(e => window.addEventListener(e, activity, { passive: true }));
  setInterval(() => { const st = cur(); if (!st || document.hidden) return; const playing = !!document.querySelector('video') && [...document.querySelectorAll('video')].some(v => !v.paused);
    if (playing || Date.now() - lastAct < 120000) { st.time = (st.time || 0) + 15; if ((st.time % 60) === 0) persist(); else S.states[UNIT()] = strip(st); } }, 15000);
  const unitSeconds = n => ((S.states[unitId(n)] || {}).time) || 0;
  const totalSeconds = () => Object.entries(S.states || {}).filter(([k]) => k.startsWith(`stage${STAGE}-`)).reduce((a, [, x]) => a + ((x && x.time) || 0), 0);
  const estMinutes = n => (((INDEX && INDEX.units.find(u => u.n === n)) || {}).est) || 0;
  function flush() {
    const st = cur(); if (!st || !dirty) return; dirty = false;
    if (S.guest) { try { localStorage.setItem(gkey(), JSON.stringify(strip(st))); } catch (e) { } return; }
    Backend.saveProgress(st.id, UNIT(), strip(st)).catch(() => { dirty = true; }); // attempts live on the server
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
    if (!canOpen(s.id)) return S.guest ? { reason: `Guests can try the first topic of every unit. Create a free account to unlock topic ${s.id} and save your progress.`, what: 'a free account', route: 'signup', paywall: true, guest: true }
      : { reason: `This topic is part of the full Cambridge ${stageName(STAGE)} course.`, what: `a Cambridge ${stageName(STAGE)} plan (7-day free trial)`, route: 'pricing', paywall: true };
    return seqLock(C, st, s, UNIT());
  }
  const unitOpen = unit => !!S.tester || TestRules.OPEN_UNITS.includes(unit);
  // the sequential rule for any unit's content/state (used by the sidebar for units not on screen)
  function seqLock(content, st, s, unit) {
    if (unitOpen(unit)) return null;
    const i = content.sections.findIndex(x => x.id === s.id); if (i <= 0) return null;
    const prev = content.sections[i - 1]; if (secDone(st, prev)) return null;
    return { reason: `Finish section ${prev.id} first.`, ...firstMissingIn(st, prev) };
  }
  function firstMissingIn(st, s) {
    if (!videoDone(st, s)) return { what: s.lesson ? `Section ${s.id} lesson (${stopsLeft(st, s).length} check question(s) left${vstate(st, s.id).completed ? '' : ', not marked as finished'})` : `Section ${s.id} video (${stopsLeft(st, s).length} pause question(s) left${vstate(st, s.id).completed ? '' : ', not watched to the end'})`, route: 'v-' + s.id.replace('.', '-') };
    const q = reqLeft(st, s)[0]; if (!q) return null;
    const i = s.req.indexOf(q);
    return { what: `the “${QE.TYPE_VI[q.type]}” task (Core question ${i + 1}) in section ${s.id}`, route: 'ex-' + s.id.replace('.', '-'), idx: i, tab: 'req' };
  }
  function missingForTest(st) {
    const out = []; if (unitOpen(UNIT())) return out;
    for (const s of secs()) {
      if (!videoDone(st, s)) out.push({ what: `Section ${s.id} ${s.lesson ? 'lesson' : 'video'} – ${s.title}` + (stopsLeft(st, s).length ? ` (${stopsLeft(st, s).length} ${s.lesson ? 'check' : 'pause'} question(s) left)` : (s.lesson ? ' (not marked as finished)' : ' (not watched to the end)')), route: 'v-' + s.id.replace('.', '-') });
      reqLeft(st, s).forEach(q => { const i = s.req.indexOf(q); out.push({ what: `Section ${s.id} · Core question ${i + 1}: ${QE.TYPE_VI[q.type]} – “${q.prompt.slice(0, 60)}${q.prompt.length > 60 ? '…' : ''}”`, route: 'ex-' + s.id.replace('.', '-'), idx: i, tab: 'req' }); });
    }
    return out;
  }

  /* ---------- stages: the learner's own stage is included; other stages need an enrolment ---------- */
  const learnerStage = () => { const st = cur(); return (st && st.learner && st.learner.stage) || 7; };
  const enrolled = stage => stageLocked(stage) ? false : S.guest ? stage === 7 : (stage === learnerStage() || (S.enrolments || []).some(e => e.stage === stage && e.status !== 'canceled'));
  async function enrol(stage, amount) { const st = cur(); await Backend.enrol(st.id, stage, amount); S.enrolments = await Backend.enrolments(st.id); return true; }

  /* ---------- exam room clock (the server keeps the official start time) ---------- */
  async function startClock(unit, form) {
    const r = await Backend.startTest({ learnerId: cur().id, unit, form });
    const skew = r.now ? Date.now() - Date.parse(r.now) : 0;   // the device clock may differ from the server's
    return { deadline: Date.parse(r.deadline) + skew, minutes: r.minutes };
  }

  /* ---------- end-of-year exam ---------- */
  // Checkpoint-format practice papers (Atomic papers in the format of Cambridge 0893/01 and 0893/02)
  async function loadCp() { if (INDEX && !INDEX.cp) return null; if (!CP) { const r = await fetch(`content/stage${STAGE}-cp.json`); CP = r.ok ? await withOv(`stage${STAGE}-cp`, await r.json()) : null; } return CP; }
  async function refreshCp() { const st = cur(); if (!st || S.guest) { S.cpAttempts = []; return []; } S.cpAttempts = await Backend.attempts(st.id, `stage${STAGE}-cp`); return S.cpAttempts; }
  async function submitCp(form, answers, clientKey, meta) {
    const st = cur(); const r = await Backend.submitTest({ learnerId: st.id, unit: `stage${STAGE}-cp`, form, answers, clientKey, meta });
    await refreshCp(); st.solutions = Object.assign(st.solutions || {}, r.solutions); return r;
  }
  async function refreshFinal() { const st = cur(); if (!st || S.guest) { S.finalAttempts = []; return []; } S.finalAttempts = await Backend.attempts(st.id, `stage${STAGE}-final`); return S.finalAttempts; }
  const finalPassed = () => (S.finalAttempts || []).some(a => a.status === 'final' && a.passed);
  async function submitFinal(form, answers, clientKey, meta) {
    const st = cur(); const r = await Backend.submitTest({ learnerId: st.id, unit: `stage${STAGE}-final`, form, answers, clientKey, meta });
    await refreshFinal(); st.solutions = Object.assign(st.solutions || {}, r.solutions); return r;
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
  async function submitTest(st, form, answers, clientKey, meta, unitId) {
    flush(); dirty = true; await Backend.saveProgress(st.id, UNIT(), (() => { const c = {}; for (const k of Object.keys(st)) if (!META.includes(k)) c[k] = st[k]; c.test = { drafts: st.test.drafts }; return c; })());
    const r = await Backend.submitTest({ learnerId: st.id, unit: UNIT(), form, answers, clientKey, meta });
    const i = st.test.attempts.findIndex(a => a.id === r.attempt.id);
    if (i >= 0) st.test.attempts[i] = r.attempt; else st.test.attempts.push(r.attempt);
    st.solutions = Object.assign(st.solutions || {}, r.solutions);
    await refreshResults(st); return r;
  }
  async function refreshAttempts(st) { st.test.attempts = await Backend.attempts(st.id, UNIT()); await refreshResults(st); }
  async function refreshResults(st) { st.results = await Backend.unitResults(st.id); }
  const UNIT = () => unitId(UNO);

  /* ---------- course / ranking / certificate ---------- */
  function unitStatus(st, n) {
    if (st && st.results && st.results[unitId(n)]) return 'passed';
    return unitReady(n) ? 'open' : 'soon';
  }
  function rankScore(st) {
    const list = Object.entries(st.results || {}).filter(([k]) => k.startsWith(`stage${STAGE}-unit`)).map(([, r]) => r.pct);
    if (!list.length) return null;
    return { score: list.reduce((a, b) => a + b, 0) / list.length, units: list.length };
  }
  const stageComplete = st => Object.keys(st.results || {}).filter(k => k.startsWith(`stage${STAGE}-unit`)).length >= unitCount();
  async function certificate(st) { if (S.guest) return null; if (st.cert) return st.cert; if (!stageComplete(st)) return null; await refreshFinal(); if (!finalPassed()) return null; st.cert = await Backend.issueCertificate(st.id, unitCount(), STAGE); return st.cert; }
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
      if (lock) { if (lock.guest) return { label: `Sign up free to unlock topic ${s.id}`, route: 'signup' }; if (lock.paywall) return { label: 'Unlock the rest of Cambridge Stage 7', route: 'pricing' }; break; }
      if (!videoDone(st, s)) return { label: s.lesson ? `Read the section ${s.id} lesson` : `Watch the section ${s.id} video`, route: 'v-' + s.id.replace('.', '-') };
      const q = reqLeft(st, s)[0]; if (q) return { label: `Core practice for section ${s.id}`, route: 'ex-' + s.id.replace('.', '-'), tab: 'req', idx: s.req.indexOf(q) };
    }
    const ts = testState(st);
    if (ts.state === 'guest') return { label: 'Sign up free to take the Unit Test', route: 'signup' };
    if (ts.state === 'paywall') return { label: 'Unlock the Unit Test', route: 'pricing' };
    if (ts.state === 'ready') return { label: ts.retake ? `Retake the Unit Test (Paper ${ts.form})` : `Take Unit Test ${UNO}`, route: 'test' };
    if (ts.state === 'remediate') return { label: 'Do your review questions', route: 'remedial' };
    if (ts.state === 'pending') return { label: 'See your results (awaiting marking)', route: 'result' };
    if (stageComplete(st)) return { label: 'Get your certificate', route: 'cert' };
    return { label: `See your Unit ${UNO} results`, route: 'result' };
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
    get UNIT() { return UNIT(); }, get UNO() { return UNO; }, get INDEX() { return INDEX; }, STAGE_UNITS, FREE_SECTIONS, BILLING_OFF, get S() { return S; }, get C() { return C; }, get STAGE() { return STAGE; }, STAGES, switchStage, stageLocked, LOCKED, PRIMARY, levelName, get IS_PRIMARY() { return PRIMARY(STAGE); }, MATHS, stageNo, subjectOf, stageLabel, stageName, unitCount, get IS_MATHS() { return MATHS(STAGE); },
    unitId, unitReady, switchUnit, loadIndex, peekUnit, cached, loadFinal, get FINAL() { return FINAL; },
    xpNow, levelInfo, unitSeconds, totalSeconds, estMinutes, seqLock, unitOpen, learnerStage, enrolled, enrol, startClock, refreshFinal, finalPassed, submitFinal, loadCp, refreshCp, dropCache, withOv, submitCp, activity,
    boot, selectLearner, leaveLearner, refreshAccount, cur, persist, flush, canOpen,
    sec, secs, vstate, stopDone, stopsLeft, videoDone, reqLeft, secDone, secLock, firstMissingIn, missingForTest,
    attempts, lastAttempt, passed, isPass, nextForm, remKey, remLeft, testState, submitTest, refreshAttempts, refreshResults,
    unitStatus, rankScore, xp, streak, stageComplete, startGuest, adoptGuest,
    week, today, certificate, competitionRank, nextActivity, jpegPdf, saveFile
  };
})();
