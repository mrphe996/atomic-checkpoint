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
    S.profiles = { guest: st }; S.current = 'guest'; S.guest = true; wallet(st); shop(st);
    try { localStorage.setItem(GKEY, JSON.stringify(strip(st))); } catch (e) { }
    return st;
  }
  // after sign-up / sign-in: bring the guest's work into the new account (only if the account has nothing yet)
  async function adoptGuest() {
    if (!guestSaved()) return false; const st = cur(); if (!st) return false;
    let g = null; try { g = JSON.parse(localStorage.getItem(GKEY)); } catch (e) { }
    const empty = !Object.keys(st.items || {}).length && !Object.values(st.video || {}).some(v => v && (v.completed || v.pos > 1 || Object.keys(v.stops || {}).length));
    if (g && empty) { for (const k of ['video', 'items', 'stopsWrong', 'ws', 'days', 'wallet', 'shop', 'marks']) if (g[k]) st[k] = g[k]; dirty = true; flush(); }
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
    S.profiles = { [id]: st }; S.current = id; wallet(st); shop(st);
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
    tick(st);
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
  /* ---------- bolts ⚡: earned only by doing the work, spent in the shop ----------
     Earned bolts come from the same rules as before (a right answer first time is worth more than a
     later one, so guessing does not pay). Each change is booked to the day it happened, which drives the
     daily goal, the streak and the daily challenges. Bonuses (challenges, streak milestones) are stored
     separately; spending is the price of the items the learner owns. */
  const DAILY_GOAL = 20;
  const pad = n => String(n).padStart(2, '0');
  const dstr = d => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  const today = () => dstr(new Date());
  const countFirstTry = st => Object.values(st.items || {}).filter(r => r && r.done && r.ok && (r.tries || 1) === 1).length;
  const countVideos = st => C ? C.sections.filter(s => vstate(st, s.id).completed).length : 0;
  function wallet(st) {
    if (!st.wallet) {   // first time: what was already earned counts, and every earlier active day keeps the streak
      st.wallet = { snap: { xp: xp(st), ft: countFirstTry(st), vid: countVideos(st) }, day: {}, bonus: 0, claims: {}, log: [] };
      (st.days || []).forEach(d => { st.wallet.day[d] = { e: DAILY_GOAL, ft: 0, vid: 0, legacy: 1 }; });
    }
    return st.wallet;
  }
  const dayRec = (w, d) => (w.day[d] = w.day[d] || { e: 0, ft: 0, vid: 0 });
  let onEarn = null;   // the screens subscribe to show "+10 ⚡"
  function tick(st) {
    const w = wallet(st), now = { xp: xp(st), ft: countFirstTry(st), vid: countVideos(st) }, r = dayRec(w, today());
    const de = Math.max(0, now.xp - w.snap.xp);
    r.e += de; r.ft += Math.max(0, now.ft - w.snap.ft); r.vid += Math.max(0, now.vid - w.snap.vid);
    w.snap = now;
    let bonus = 0;
    const s = streak(st);
    for (const [len, b] of STREAK_BONUS) if (s === len && !w.claims['streak' + len + '@' + today()]) { w.claims['streak' + len + '@' + today()] = 1; w.bonus += b; bonus += b; w.log.unshift({ d: today(), n: b, why: `${len}-day streak` }); }
    w.log = w.log.slice(0, 30);
    if ((de || bonus) && onEarn) onEarn(de + bonus, bonus ? 'streak' : 'work');
    return de + bonus;
  }
  const STREAK_BONUS = [[3, 30], [7, 80], [14, 200], [30, 500]];
  const spent = st => ((st.shop || {}).owned || []).reduce((t, id) => t + ((ITEMS.find(i => i.id === id) || {}).price || 0), 0);
  const bolts = st => { const w = wallet(st); return xp(st) + w.bonus - spent(st); };
  const earnedToday = st => (wallet(st).day[today()] || { e: 0 }).e;
  function streak(st) {
    const w = wallet(st); const met = d => (w.day[d] || { e: 0 }).e >= DAILY_GOAL;
    const d = new Date(); let n = 0;
    if (!met(dstr(d))) d.setDate(d.getDate() - 1);           // today does not break the streak until it is over
    while (met(dstr(d))) { n++; d.setDate(d.getDate() - 1); }
    return n;
  }
  function week(st) {   // last 7 days for the streak strip: [{d, label, met, today}]
    const w = wallet(st), out = [], d = new Date(); d.setDate(d.getDate() - 6);
    for (let i = 0; i < 7; i++) { const k = dstr(d); out.push({ d: k, label: 'SMTWTFS'[d.getDay()], met: (w.day[k] || { e: 0 }).e >= DAILY_GOAL, today: i === 6 }); d.setDate(d.getDate() + 1); }
    return out;
  }

  /* daily challenges: three a day, each claimed once */
  const CHALLENGES = [
    { id: 'earn50', label: 'Earn 50 ⚡ today', goal: 50, reward: 30, val: r => r.e },
    { id: 'first5', label: 'Get 5 questions right first time', goal: 5, reward: 20, val: r => r.ft },
    { id: 'video1', label: 'Finish a lesson video', goal: 1, reward: 20, val: r => r.vid }
  ];
  function challenges(st) {
    const w = wallet(st), r = w.day[today()] || { e: 0, ft: 0, vid: 0 };
    return CHALLENGES.map(c => ({ id: c.id, label: c.label, goal: c.goal, reward: c.reward, value: Math.min(c.goal, c.val(r)), done: c.val(r) >= c.goal, claimed: !!w.claims[c.id + '@' + today()] }));
  }
  function claim(st, id) {
    const c = challenges(st).find(x => x.id === id); if (!c || !c.done || c.claimed) return 0;
    const w = wallet(st); w.claims[id + '@' + today()] = 1; w.bonus += c.reward; w.log.unshift({ d: today(), n: c.reward, why: c.label }); persist(); return c.reward;
  }

  /* shop: original Atomic items (emoji art), bought with bolts */
  const ITEMS = [
    { id: 'av-atom', kind: 'avatar', icon: '⚛️', name: 'Atom', price: 0 },
    { id: 'av-fox', kind: 'avatar', icon: '🦊', name: 'Fox', price: 0 },
    { id: 'av-panda', kind: 'avatar', icon: '🐼', name: 'Panda', price: 100 },
    { id: 'av-owl', kind: 'avatar', icon: '🦉', name: 'Owl', price: 120 },
    { id: 'av-tiger', kind: 'avatar', icon: '🐯', name: 'Tiger', price: 150 },
    { id: 'av-octo', kind: 'avatar', icon: '🐙', name: 'Octopus', price: 200 },
    { id: 'av-robot', kind: 'avatar', icon: '🤖', name: 'Robot', price: 250 },
    { id: 'av-unicorn', kind: 'avatar', icon: '🦄', name: 'Unicorn', price: 300 },
    { id: 'av-alien', kind: 'avatar', icon: '👽', name: 'Alien', price: 400 },
    { id: 'ac-goggles', kind: 'accessory', icon: '🥽', name: 'Lab goggles', price: 80 },
    { id: 'ac-shades', kind: 'accessory', icon: '🕶️', name: 'Sunglasses', price: 120 },
    { id: 'ac-cap', kind: 'accessory', icon: '🎓', name: 'Graduation cap', price: 150 },
    { id: 'ac-flask', kind: 'accessory', icon: '🧪', name: 'Test tube', price: 160 },
    { id: 'ac-phones', kind: 'accessory', icon: '🎧', name: 'Headphones', price: 180 },
    { id: 'ac-scope', kind: 'accessory', icon: '🔬', name: 'Microscope', price: 220 },
    { id: 'ac-rocket', kind: 'accessory', icon: '🚀', name: 'Rocket', price: 350 },
    { id: 'ac-crown', kind: 'accessory', icon: '👑', name: 'Crown', price: 500 },
    { id: 'bg-sky', kind: 'background', icon: '🌤️', name: 'Clear sky', price: 0, css: 'linear-gradient(135deg,#DCEBFF,#F4F8FF)' },
    { id: 'bg-leaf', kind: 'background', icon: '🌿', name: 'Leaf cell', price: 100, css: 'linear-gradient(135deg,#D9F5E3,#F1FBF4)' },
    { id: 'bg-sunset', kind: 'background', icon: '🌅', name: 'Sunset', price: 150, css: 'linear-gradient(135deg,#FFE1C7,#FFF4E6)' },
    { id: 'bg-ocean', kind: 'background', icon: '🌊', name: 'Deep ocean', price: 200, css: 'linear-gradient(135deg,#BFE6F2,#E3F6FB)' },
    { id: 'bg-space', kind: 'background', icon: '🌌', name: 'Outer space', price: 300, css: 'linear-gradient(135deg,#2B2F6B,#5B4E9E)', dark: 1 },
    { id: 'bg-lab', kind: 'background', icon: '⚗️', name: 'Science lab', price: 250, css: 'linear-gradient(135deg,#E8E2FF,#F6F3FF)' }
  ];
  const shop = st => { st.shop = st.shop || { owned: [], equip: { avatar: 'av-atom', accessory: null, background: 'bg-sky' } }; return st.shop; };
  const owns = (st, id) => { const it = ITEMS.find(i => i.id === id); return !!it && (it.price === 0 || shop(st).owned.includes(id)); };
  function buy(st, id) {
    const it = ITEMS.find(i => i.id === id); if (!it) return { error: 'unknown' };
    if (owns(st, id)) return { error: 'owned' };
    if (bolts(st) < it.price) return { error: 'short', need: it.price - bolts(st) };
    shop(st).owned.push(id); equip(st, id); return { ok: true };
  }
  function equip(st, id) {
    const it = ITEMS.find(i => i.id === id); if (!it || !owns(st, id)) return false;
    const e = shop(st).equip; e[it.kind] = e[it.kind] === id && it.kind === 'accessory' ? null : id; persist(); return true;
  }
  const look = st => { const e = shop(st).equip, g = id => ITEMS.find(i => i.id === id); return { avatar: g(e.avatar) || ITEMS[0], accessory: e.accessory ? g(e.accessory) : null, background: g(e.background) || g('bg-sky') }; };
  const setOnEarn = fn => { onEarn = fn; };

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
    DAILY_GOAL, ITEMS, wallet, tick, bolts, earnedToday, week, challenges, claim, buy, equip, owns, look, shop, setOnEarn, today, certificate, competitionRank, nextActivity, jpegPdf, saveFile
  };
})();
