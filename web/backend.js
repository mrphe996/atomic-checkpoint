/* Atomic — data layer. One interface, two implementations:
   - DemoBackend: everything in this browser (localStorage). For previews and design reviews; no server needed.
   - LiveBackend: Supabase Auth + PostgREST (row-level security) + Vercel functions (/api/*) for marking,
     payments, data export and deletion. No SDK: plain fetch, so the page has no build step.
   window.Backend is chosen from window.ATOMIC_CONFIG.mode. */
(function () {
  const CFG = window.ATOMIC_CONFIG || { mode: 'demo' };
  const LEGAL = CFG.legalVersion || '2026-11-draft';
  const uuid = () => (crypto.randomUUID ? crypto.randomUUID() : 'xxxxxxxx-xxxx-4xxx-8xxx-xxxxxxxxxxxx'.replace(/x/g, () => (Math.random() * 16 | 0).toString(16)));
  const sha = async s => { const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode('atomic-demo:' + s)); return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join(''); };
  const err = (code, extra) => Object.assign(new Error(code), { code }, extra || {});
  const unitPack = {};
  async function loadPublic(unit) { if (!unitPack[unit]) unitPack[unit] = await (await fetch(`content/${unit}.json`)).json(); return unitPack[unit]; }

  /* ===================== DEMO ===================== */
  function DemoBackend() {
    const KEY = 'atomic.v2';
    let D; try { D = JSON.parse(localStorage.getItem(KEY)) || null; } catch (e) { D = null; }
    D = D || { accounts: {}, session: null, progress: {}, attempts: {}, results: {}, certs: {}, events: [] };
    const save = () => { try { localStorage.setItem(KEY, JSON.stringify(D)); } catch (e) { } };
    const acct = () => (D.session ? D.accounts[D.session] : null);
    const need = () => { const a = acct(); if (!a) throw err('sign_in'); return a; };
    const ownerOf = lid => Object.values(D.accounts).find(a => a.learners.some(l => l.id === lid));
    const mine = lid => { const a = need(); const l = a.learners.find(x => x.id === lid); if (!l) throw err('not_your_learner'); return l; };
    const note = (a, learner, kind, title, body) => a.notifications.unshift({ id: uuid(), kind, title, body: body || '', learner_id: learner, created_at: new Date().toISOString(), read_at: null });
    const subActive = a => !!(a.subscription && ['trialing', 'active', 'past_due'].includes(a.subscription.status) && (!a.subscription.current_period_end || Date.parse(a.subscription.current_period_end) > Date.now()));
    function recordFinal(lid, unit, at) {
      const a = ownerOf(lid); const l = a.learners.find(x => x.id === lid);
      if (at.status === 'final' && at.passed) {
        D.results[lid] = D.results[lid] || {};
        if (!D.results[lid][unit]) D.results[lid][unit] = { pct: at.pct, at: new Date().toISOString(), stage: 7 };
        const first = !D.results[lid][unit + ':notified']; D.results[lid][unit + ':notified'] = true;
        const un = Number(unit.slice(-2)), ut = (((window.Core && Core.INDEX) || { units: [] }).units.find(u => u.n === un) || {}).t || ''; const uname = `Unit ${un}${ut ? ': ' + ut : ''}`;
        note(a, lid, 'test_passed', `You passed ${uname}!`, `Score ${at.pct.toFixed(1)}%`);
        if (first && l.parent_email) (D.outbox = D.outbox || []).push({ to_email: l.parent_email, kind: 'unit_complete', subject: `${l.nickname} has finished ${uname} on Atomic`, created_at: new Date().toISOString(), status: 'queued' });
      } else if (at.status === 'final') note(a, lid, 'test_marked', 'Your Unit Test has been marked', `Score ${at.pct.toFixed(1)}%`);
    }
    return {
      mode: 'demo', label: 'Preview – data stays in this browser',
      async me() { const a = acct(); return a ? { user: { id: a.id, email: a.email }, profile: a.profile } : null; },
      async signUp(form) { // same checks as api/signup.js
        const email = String(form.email || '').trim().toLowerCase(), name = String(form.name || '').trim().replace(/\s+/g, ' ');
        const EM = /^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/, y = new Date().getFullYear(), by = Number(form.birthYear);
        if (!EM.test(email)) throw err('bad_email');
        if (String(form.password || '').length < 8) throw err('weak_password');
        if (name.length < 2) throw err('bad_name');
        if (!(by >= 2005 && by <= y - 5)) throw err('bad_birth_year');
        const pe = String(form.parentEmail || '').trim().toLowerCase(); if (pe && !EM.test(pe)) throw err('bad_parent_email'); if (pe && pe === email) throw err('parent_email_same');
        if (D.accounts[email]) throw err('email_taken');
        const id = uuid(), now = new Date().toISOString();
        D.accounts[email] = { id, email, pw: await sha(form.password), profile: { id, role: 'student', display_name: name, country: form.country || 'XX', weekly_report: false, marketing_opt_in: false, product_analytics: false, created_at: now },
          consents: [{ kind: 'terms', version: LEGAL, given: true, at: now }, { kind: 'privacy', version: LEGAL, given: true, at: now }],
          learners: [{ id: uuid(), user_id: id, parent_id: null, nickname: name.split(' ')[0].slice(0, 24), certificate_name: name, birth_year: by, grade: form.grade || null, country: form.country || 'XX',
            school_id: form.schoolId || null, school_other: form.schoolId ? null : (form.schoolOther || null), parent_email: pe || null, consent_status: 'not_required', stage: 7, leaderboard_opt_in: false, created_at: now }],
          subscription: null, notifications: [], reports: [] };
        D.session = email; save(); return this.me();
      },
      async schools(country) { return (window.ATOMIC_SCHOOLS || []).filter(s => s.country === country); },
      async signIn({ email, password }) { email = String(email || '').trim().toLowerCase(); const a = D.accounts[email]; if (!a || a.pw !== await sha(password)) throw err('bad_credentials'); D.session = email; save(); return this.me(); },
      async signOut() { D.session = null; save(); },
      async resetPassword(email) { return { sent: true, demo: true, email }; },
      async verifyPassword(password) { const a = need(); return a.pw === await sha(password); },
      async updateProfile(patch) { const a = need(); const allowed = ['display_name', 'country', 'weekly_report', 'marketing_opt_in', 'product_analytics'];
        for (const k of allowed) if (k in patch) { a.profile[k] = patch[k]; if (['marketing_opt_in', 'product_analytics'].includes(k)) a.consents.push({ kind: k === 'marketing_opt_in' ? 'marketing' : 'product_analytics', version: LEGAL, given: !!patch[k], at: new Date().toISOString() }); }
        save(); return a.profile; },
      async learners() { return need().learners.slice(); },
      async addLearner({ nickname, birthYear, certificateName, consent }) {
        const a = need(); if (!consent) throw err('parental_consent');
        nickname = String(nickname || '').trim(); if (nickname.length < 2 || nickname.length > 24) throw err('bad_nickname');
        const l = { id: uuid(), parent_id: a.id, nickname, certificate_name: certificateName || null, birth_year: birthYear || null, stage: 7, leaderboard_opt_in: false, created_at: new Date().toISOString() };
        a.learners.push(l); a.consents.push({ kind: 'parental_consent', learner_id: l.id, version: LEGAL, given: true, at: new Date().toISOString() }); save(); return l;
      },
      async updateLearner(id, patch) { const l = mine(id); for (const k of ['nickname', 'certificate_name', 'birth_year', 'leaderboard_opt_in', 'parent_email', 'school_id', 'school_other', 'grade']) if (k in patch) l[k] = patch[k];
        if ('leaderboard_opt_in' in patch) need().consents.push({ kind: 'leaderboard', learner_id: id, version: LEGAL, given: !!patch.leaderboard_opt_in, at: new Date().toISOString() });
        save(); return l; },
      async removeLearner(id) { const a = need(); mine(id); a.learners = a.learners.filter(l => l.id !== id); delete D.progress[id]; delete D.attempts[id]; delete D.results[id]; delete D.certs[id]; D.events = D.events.filter(e => e.learner_id !== id); save(); },
      async loadProgress(lid, unit) { mine(lid); return ((D.progress[lid] || {})[unit]) || null; },
      async allDays(lid) { mine(lid); return [].concat(...Object.values(D.progress[lid] || {}).map(p => (p && p.days) || [])); },
      async allStates(lid) { mine(lid); return JSON.parse(JSON.stringify(D.progress[lid] || {})); },
      async enrolments(lid) { mine(lid); return ((D.enrol || {})[lid] || []).slice(); },
      async enrol(lid, stage, amount) { mine(lid); D.enrol = D.enrol || {}; const l = (D.enrol[lid] = D.enrol[lid] || []); if (!l.some(e => e.stage === stage)) l.push({ stage, method: 'test', amount: amount || null, status: 'active', created_at: new Date().toISOString() });
        note(need(), lid, 'billing', `You are enrolled in Cambridge Stage ${stage}`, 'Test checkout – no money was taken.'); save(); return 'ok'; },
      async startTest({ learnerId, unit, form }) { mine(learnerId); D.starts = D.starts || {}; const k = `${learnerId}|${unit}|${form}`; D.starts[k] = D.starts[k] || new Date().toISOString(); save();
        const minutes = /-final$/.test(unit) ? 60 : /-cp$/.test(unit) ? 45 : TestRules.UNIT_MINUTES; return { startedAt: D.starts[k], minutes, deadline: new Date(Date.parse(D.starts[k]) + minutes * 60000).toISOString(), now: new Date().toISOString() }; },
      async saveProgress(lid, unit, state) { mine(lid); (D.progress[lid] = D.progress[lid] || {})[unit] = JSON.parse(JSON.stringify(state)); save(); },
      async attempts(lid, unit) { mine(lid); return ((D.attempts[lid] || {})[unit] || []).slice(); },
      async submitTest({ learnerId, unit, form, answers, clientKey, meta }) { // same rules as api/submit-test.js
        const a = need(); const l = mine(learnerId);
        if ((CFG.billing || 'off') !== 'off' && !subActive(a)) throw err('subscription_required');
        const stage = Number(unit.slice(5, 6)); if (stage !== (l.stage || 7) && !(((D.enrol || {})[learnerId]) || []).some(e => e.stage === stage)) throw err('not_enrolled');
        const list = ((D.attempts[learnerId] = D.attempts[learnerId] || {})[unit] = D.attempts[learnerId][unit] || []);
        const keys = await (await fetch(`content/demo/${unit}.tests.json`)).json();
        const same = list.find(x => x.clientKey === clientKey);
        if (same) return { attempt: same, solutions: TestRules.solutions(keys.papers[same.form]), duplicate: true };
        D.starts = D.starts || {}; const sk = `${learnerId}|${unit}|${form}`; const started = D.starts[sk] || null; const duration = started ? Math.round((Date.now() - Date.parse(started)) / 1000) : null;
        if (keys.final) {
          const lastF = list[list.length - 1]; if (lastF && lastF.status === 'pending') throw err('awaiting_marking');
          if (!keys.papers[form]) throw err('wrong_paper'); if (list.some(x => x.form === form)) throw err('paper_done');
          const passes = Object.keys(D.results[learnerId] || {}).filter(k => !k.includes(':')).length;
          const xp = TestRules.xpTotal(D.progress[learnerId] || {}, passes); if (TestRules.levelOf(xp) < keys.level) throw err('level_required', { level: keys.level, have: TestRules.levelOf(xp) });
          const paper = keys.papers[form];
          const at = TestRules.finalizeFinal(TestRules.mark(paper, answers, { n: list.length + 1, form, id: uuid(), clientKey }), paper, keys.max, keys.pass);
          at.duration = duration; at.overtime = duration != null && duration > (keys.minutes || 60) * 60 + TestRules.GRACE_S; at.leaves = (meta && meta.leaves) || 0; at.autoSubmitted = !!(meta && meta.auto); delete D.starts[sk];
          list.push(at); if (at.status === 'final' && at.passed) note(a, learnerId, 'test_passed', `You passed the end-of-year exam (paper ${form})!`, `Score ${at.pct.toFixed(1)}%`); save();
          return { attempt: at, solutions: TestRules.solutions(paper) };
        }
        const content = await loadPublic(unit);
        const state = ((D.progress[learnerId] || {})[unit]) || {};
        const missing = TestRules.missingForTest(content, state, unit); if (missing.length) throw err('locked', { missing });
        const last = list[list.length - 1];
        if (list.some(x => x.status === 'final' && x.passed)) throw err('already_passed');
        if (last && last.status === 'pending') throw err('awaiting_marking');
        if (last && !last.passed) { const left = (last.remed || []).filter(id => !(((state.rem || {})[`rem${last.n}:${id}`]) || {}).done); if (left.length) throw err('review_first', { left }); }
        if (form !== TestRules.nextForm(list.length)) throw err('wrong_paper');
        const paper = keys.papers[form];
        const at = TestRules.finalize(TestRules.mark(paper, answers, { n: list.length + 1, form, id: uuid(), clientKey }), paper, content, state);
        at.duration = duration; at.overtime = duration != null && duration > TestRules.UNIT_MINUTES * 60 + TestRules.GRACE_S; at.leaves = (meta && meta.leaves) || 0; at.autoSubmitted = !!(meta && meta.auto); delete D.starts[sk];
        list.push(at); if (at.status === 'final') recordFinal(learnerId, unit, at); save();
        return { attempt: at, solutions: TestRules.solutions(paper) };
      },
      async markingQueue() {
        const a = need(); if (!['marker', 'admin'].includes(a.profile.role)) throw err('staff_only');
        const out = [];
        for (const [lid, units] of Object.entries(D.attempts)) for (const [unit, list] of Object.entries(units)) for (const at of list) if (at.status === 'pending') {
          const keys = await (await fetch(`content/demo/${unit}.tests.json`)).json();
          out.push({ attemptId: at.id, unit, n: at.n, form: at.form, submitted: new Date(at.ts).toISOString(), learner: (ownerOf(lid).learners.find(l => l.id === lid) || {}).nickname || 'Learner',
            items: at.pending.map(id => { const q = keys.papers[at.form].find(x => x.id === id); return { id, prompt: q.prompt, max: q.pts, answer: at.answers[id] || '', rubric: q.rubric.map(p => p.pt), model: q.model, suggest: at.per[id].suggest }; }) });
        }
        return out;
      },
      async markAttempt(attemptId, grades) {
        const a = need(); if (!['marker', 'admin'].includes(a.profile.role)) throw err('staff_only');
        for (const [lid, units] of Object.entries(D.attempts)) for (const [unit, list] of Object.entries(units)) { const at = list.find(x => x.id === attemptId); if (!at) continue;
          at.pending.forEach(id => { at.per[id].pts = Math.max(0, Math.min(at.per[id].max, Math.round(Number(grades[id]) * 2) / 2)); });
          const keys = await (await fetch(`content/demo/${unit}.tests.json`)).json();
          if (keys.final) { TestRules.finalizeFinal(at, keys.papers[at.form], keys.max, keys.pass); save(); return at; }
          TestRules.finalize(at, keys.papers[at.form], await loadPublic(unit), ((D.progress[lid] || {})[unit]) || {}); recordFinal(lid, unit, at); save(); return at; }
        throw err('not_found');
      },
      async leaderboard(stage = 7) {
        const a = acct(); const rows = [];
        for (const acc of Object.values(D.accounts)) for (const l of acc.learners) {
          const r = D.results[l.id]; if (!r) continue; const own = a && acc.id === a.id;
          if (!l.leaderboard_opt_in && !own) continue;
          const pcts = Object.values(r).filter(x => x.stage === stage).map(x => x.pct); if (!pcts.length) continue;
          rows.push({ nickname: l.nickname, score: Math.round(pcts.reduce((s, x) => s + x, 0) / pcts.length * 100) / 100, units: pcts.length, is_mine: own, opted_in: l.leaderboard_opt_in });
        }
        return rows;
      },
      async unitResults(lid) { mine(lid); return Object.fromEntries(Object.entries(D.results[lid] || {}).filter(([k]) => !k.includes(':'))); },
      async issueCertificate(lid, stageUnits, stage = 7) {
        const l = mine(lid); const key = stage === 7 ? lid : `${lid}:s${stage}`; if (D.certs[key]) return D.certs[key];
        const have = Object.keys(D.results[lid] || {}).filter(k => !k.includes(':') && k.startsWith(`stage${stage}-unit`)).length; if (have < stageUnits) throw err('stage_incomplete', { have, need: stageUnits });
        if (!(((D.attempts[lid] || {})[`stage${stage}-final`]) || []).some(x => x.status === 'final' && x.passed)) throw err('final_required');
        const hex = [...crypto.getRandomValues(new Uint8Array(4))].map(x => x.toString(16).padStart(2, '0')).join('').toUpperCase();
        D.certs[key] = { code: `AE-S${stage}-${new Date().getFullYear()}-${hex}`, name: l.certificate_name || l.nickname, date: new Date().toISOString().slice(0, 10), stage }; save(); return D.certs[key];
      },
      async certificate(lid, stage = 7) { mine(lid); return D.certs[stage === 7 ? lid : `${lid}:s${stage}`] || null; },
      async verifyCertificate(code) { const c = Object.values(D.certs).find(x => x.code === String(code || '').trim().toUpperCase()); return c ? { name_on_certificate: c.name, stage: c.stage || 7, issued_at: c.date } : null; },
      async subscription() { const a = need(); return { active: subActive(a), ...(a.subscription || { status: 'none' }) }; },
      async checkout(plan) { const a = need(); const end = new Date(Date.now() + 7 * 864e5).toISOString(); a.subscription = { plan: 'stage7_' + plan, status: 'trialing', current_period_end: end, provider: 'demo' }; note(a, null, 'billing', 'Your 7-day free trial has started', 'Cambridge Stage 7 is unlocked for every child on your account.'); save(); return a.subscription; },
      async cancelSubscription() { const a = need(); if (a.subscription) a.subscription.status = 'canceled'; save(); },
      async consents() { return need().consents.slice().reverse(); },
      async exportData() { const a = need(); const ids = a.learners.map(l => l.id);
        return { exported_at: new Date().toISOString(), account: { id: a.id, email: a.email }, profile: a.profile, consents: a.consents, learners: a.learners, subscription: a.subscription, reports: a.reports, notifications: a.notifications,
          progress: Object.fromEntries(ids.map(i => [i, D.progress[i] || {}])), attempts: Object.fromEntries(ids.map(i => [i, D.attempts[i] || {}])), results: Object.fromEntries(ids.map(i => [i, D.results[i] || {}])), certificates: Object.fromEntries(ids.map(i => [i, D.certs[i] || null])), events: D.events.filter(e => ids.includes(e.learner_id)) }; },
      async deleteAccount(confirm) { if (confirm !== 'DELETE MY ACCOUNT') throw err('confirm'); const a = need(); for (const l of a.learners) await this.removeLearner(l.id); delete D.accounts[a.email]; D.session = null; save(); return { deleted: true }; },
      async report(r) { const a = need(); const row = { id: uuid(), reporter_id: a.id, status: 'open', created_at: new Date().toISOString(), ...r }; if (!row.message || row.message.length < 3) throw err('message'); a.reports.unshift(row); save(); return row; },
      async reports() { const a = need(); if (['marker', 'admin'].includes(a.profile.role)) return Object.values(D.accounts).flatMap(x => x.reports); return a.reports; },
      async setReportStatus(id, status) { for (const x of Object.values(D.accounts)) { const r = x.reports.find(y => y.id === id); if (r) r.status = status; } save(); },
      async notifications() { return acct() ? acct().notifications.slice(0, 30) : []; },
      async markNotificationsRead() { const a = acct(); if (a) a.notifications.forEach(n => n.read_at = n.read_at || new Date().toISOString()); save(); },
      track(name, props, essential = true) { const a = acct(); if (!a) return; if (!essential && !a.profile.product_analytics) return; D.events.push({ name, props, essential, learner_id: props && props.learner, at: new Date().toISOString() }); if (D.events.length > 5000) D.events.splice(0, 1000); save(); },
      async itemStats(unit) { const a = need(); if (!['marker', 'admin'].includes(a.profile.role)) throw err('staff_only');
        const m = {}; D.events.filter(e => e.name === 'answer' && e.props.unit === unit).forEach(e => { const x = (m[e.props.q] = m[e.props.q] || { attempts: 0, first: 0 }); x.attempts++; if (e.props.ok && e.props.try === 1) x.first++; });
        return Object.entries(m).map(([q, x]) => ({ question_id: q, attempts: x.attempts, first_try_correct: Math.round(x.first / x.attempts * 1000) / 10 })).sort((p, q) => p.first_try_correct - q.first_try_correct); },
      async videoStats(unit) { const m = {}; D.events.filter(e => e.name === 'video_complete' && e.props.unit === unit).forEach(e => { m[e.props.sec] = (m[e.props.sec] || 0) + 1; }); const starts = {}; D.events.filter(e => e.name === 'video_start' && e.props.unit === unit).forEach(e => { starts[e.props.sec] = (starts[e.props.sec] || 0) + 1; }); return Object.keys(starts).sort().map(s => ({ sec: s, started: starts[s], completed: m[s] || 0 })); },
      /* tester tools (demo only) */
      demo: { setRole(r) { const a = need(); a.profile.role = r; save(); }, reset() { try { localStorage.removeItem(KEY); } catch (e) { } D = { accounts: {}, session: null, progress: {}, attempts: {}, results: {}, certs: {}, events: [] }; },
        simulateOtherUnits(lid, pct) { D.results[lid] = D.results[lid] || {}; for (let n = 1; n <= 14; n++) { const u = 'stage7-unit' + String(n).padStart(2, '0'); if (u !== 'stage7-unit03' && !D.results[lid][u]) D.results[lid][u] = { pct, at: new Date().toISOString(), stage: 7, simulated: true }; } save(); },
        outbox() { return (D.outbox || []).slice(); },
        simulateFinal(lid, pct) { const l = ((D.attempts[lid] = D.attempts[lid] || {})['stage7-final'] = D.attempts[lid]['stage7-final'] || []); if (!l.some(x => x.passed)) l.push({ id: uuid(), n: l.length + 1, form: '10', ts: Date.now(), status: 'final', passed: true, score: pct / 2, pct, per: {}, auto: pct / 2, pending: [], byObj: {}, simulated: true }); save(); },
        simulateXp(lid, n) { const p = ((D.progress[lid] = D.progress[lid] || {})['stage7-unit02'] = D.progress[lid]['stage7-unit02'] || {}); p.items = p.items || {}; for (let i = 0; i < n; i++) p.items['sim' + i] = { done: true, ok: true, score: 1, tries: 1, sim: true }; save(); },
        resetLearner(lid) { mine(lid); delete D.progress[lid]; delete D.attempts[lid]; delete D.results[lid]; delete D.certs[lid]; save(); },
        clearSimulated(lid) { for (const [u, r] of Object.entries(D.results[lid] || {})) if (r.simulated) delete D.results[lid][u]; save(); } }
    };
  }

  /* ===================== LIVE (Supabase + Vercel) ===================== */
  function LiveBackend() {
    const URL_ = CFG.supabaseUrl.replace(/\/$/, ''), ANON = CFG.supabaseAnonKey, SKEY = 'atomic.session';
    let S; try { S = JSON.parse(localStorage.getItem(SKEY)); } catch (e) { S = null; }
    const keep = s => { S = s; try { if (s) localStorage.setItem(SKEY, JSON.stringify(s)); else localStorage.removeItem(SKEY); } catch (e) { } };
    async function auth(path, body) {
      const r = await fetch(`${URL_}/auth/v1/${path}`, { method: 'POST', headers: { apikey: ANON, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      const j = await r.json().catch(() => ({})); if (!r.ok) throw err(j.error_code || j.error || 'auth_failed', { status: r.status, detail: j.msg || j.error_description }); return j;
    }
    const sessionFrom = j => ({ access_token: j.access_token, refresh_token: j.refresh_token, expires_at: Date.now() + (j.expires_in || 3600) * 1000 - 60000, user: j.user });
    async function token() {
      if (!S) throw err('sign_in');
      if (Date.now() > S.expires_at) { try { keep(sessionFrom(await auth('token?grant_type=refresh_token', { refresh_token: S.refresh_token }))); } catch (e) { keep(null); throw err('sign_in'); } }
      return S.access_token;
    }
    async function rest(path, { method = 'GET', body, prefer } = {}) {
      const h = { apikey: ANON, Authorization: `Bearer ${await token()}`, 'Content-Type': 'application/json' }; if (prefer) h.Prefer = prefer;
      const r = await fetch(`${URL_}/rest/v1/${path}`, { method, headers: h, body: body == null ? undefined : JSON.stringify(body) });
      const t = await r.text(); if (!r.ok) throw err('db', { status: r.status, detail: t.slice(0, 200) }); return t ? JSON.parse(t) : null;
    }
    const rpc = (fn, args) => rest(`rpc/${fn}`, { method: 'POST', body: args || {} });
    async function api(path, { method = 'GET', body } = {}) {
      const r = await fetch(`${CFG.apiBase || '/api'}/${path}`, { method, headers: { Authorization: `Bearer ${await token()}`, 'Content-Type': 'application/json' }, body: body == null ? undefined : JSON.stringify(body) });
      const j = await r.json().catch(() => ({})); if (!r.ok) throw err(j.error || 'server', j); return j;
    }
    const uid = () => S && S.user && S.user.id;
    let profileCache = null;
    return {
      mode: 'live', label: '',
      async me() { if (!S) return null; try { await token(); const p = await rest(`profiles?id=eq.${uid()}`); profileCache = p[0]; return { user: { id: uid(), email: S.user.email }, profile: p[0] }; } catch (e) { return null; } },
      async signUp(form) { // the sign-up function creates the confirmed login + the student's profile, then we sign in
        const r = await fetch(CFG.signupUrl || `${CFG.apiBase || '/api'}/signup`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(form) });
        const j = await r.json().catch(() => ({})); if (!r.ok) throw err(j.error || 'signup_failed');
        keep(sessionFrom(await auth('token?grant_type=password', { email: form.email, password: form.password })));
        return this.me();
      },
      async schools(country) { const r = await fetch(`${URL_}/rest/v1/schools?country=eq.${encodeURIComponent(country)}&select=id,name,kind,city&order=name.asc`, { headers: { apikey: ANON } }); return r.ok ? r.json() : []; },
      async signIn({ email, password }) { keep(sessionFrom(await auth('token?grant_type=password', { email, password }))); return this.me(); },
      async signOut() { try { await fetch(`${URL_}/auth/v1/logout`, { method: 'POST', headers: { apikey: ANON, Authorization: `Bearer ${S && S.access_token}` } }); } catch (e) { } keep(null); },
      async resetPassword(email) { await auth('recover', { email }); return { sent: true }; },
      async verifyPassword(password) { try { await auth('token?grant_type=password', { email: S.user.email, password }); return true; } catch (e) { return false; } },
      async updateProfile(patch) { const r = await rest(`profiles?id=eq.${uid()}`, { method: 'PATCH', prefer: 'return=representation', body: patch });
        for (const [k, kind] of [['marketing_opt_in', 'marketing'], ['product_analytics', 'product_analytics']]) if (k in patch) await rest('consents', { method: 'POST', body: { parent_id: uid(), kind, version: LEGAL, given: !!patch[k] } });
        return r[0]; },
      async learners() { return rest(`learners?or=(user_id.eq.${uid()},parent_id.eq.${uid()})&order=created_at.asc`); },
      async addLearner({ nickname, birthYear, certificateName, consent }) { if (!consent) throw err('parental_consent');
        const l = (await rest('learners', { method: 'POST', prefer: 'return=representation', body: { parent_id: uid(), nickname, birth_year: birthYear || null, certificate_name: certificateName || null } }))[0];
        await rest('consents', { method: 'POST', body: { parent_id: uid(), learner_id: l.id, kind: 'parental_consent', version: LEGAL } }); return l; },
      async updateLearner(id, patch) { const r = await rest(`learners?id=eq.${id}`, { method: 'PATCH', prefer: 'return=representation', body: patch });
        if ('leaderboard_opt_in' in patch) await rest('consents', { method: 'POST', body: { parent_id: uid(), learner_id: id, kind: 'leaderboard', version: LEGAL, given: !!patch.leaderboard_opt_in } }); return r[0]; },
      async removeLearner(id) { await rest(`learners?id=eq.${id}`, { method: 'DELETE' }); },
      async loadProgress(lid, unit) { const r = await rest(`progress?learner_id=eq.${lid}&unit=eq.${unit}&select=state`); return r[0] ? r[0].state : null; },
      async allDays(lid) { const r = await rest(`progress?learner_id=eq.${lid}&select=days:state->days`); return [].concat(...r.map(x => x.days || [])); },
      async allStates(lid) { const r = await rest(`progress?learner_id=eq.${lid}&select=unit,state`); return Object.fromEntries(r.filter(x => !/-final$/.test(x.unit)).map(x => [x.unit, x.state])); },
      async enrolments(lid) { return rest(`enrolments?learner_id=eq.${lid}&select=stage,method,status,created_at`); },
      async enrol(lid, stage, amount) { try { return await rpc('enrol_stage', { p_learner: lid, p_stage: stage, p_amount: amount || null }); } catch (e) { throw err(/not open/.test(e.detail || '') ? 'payments_closed' : 'enrol_failed', { detail: e.detail }); } },
      async startTest(b) { return api('start-test', { method: 'POST', body: b }); },
      async saveProgress(lid, unit, state) { await rest('progress?on_conflict=learner_id,unit', { method: 'POST', prefer: 'resolution=merge-duplicates', body: { learner_id: lid, unit, state, updated_at: new Date().toISOString() } }); },
      async attempts(lid, unit) { const rows = await rest(`attempts?learner_id=eq.${lid}&unit=eq.${unit}&order=n.asc`);
        return rows.map(r => ({ id: r.id, n: r.n, form: r.form, ts: Date.parse(r.created_at), answers: r.answers, per: r.per, auto: Number(r.auto), pending: Object.keys(r.per).filter(k => r.per[k].teacher), status: r.status, score: r.score == null ? null : Number(r.score), pct: r.pct == null ? null : Number(r.pct), passed: r.passed, byObj: r.by_obj, weak: r.weak || [], remed: r.remed || [], duration: r.duration_s, overtime: !!r.overtime, leaves: Number(r.leaves || 0), autoSubmitted: !!r.auto_submitted })); },
      async submitTest(b) { return api('submit-test', { method: 'POST', body: b }); },
      async markingQueue() { return (await api('marking')).queue; },
      async markAttempt(attemptId, grades) { return (await api('marking', { method: 'POST', body: { attemptId, grades } })).attempt; },
      async leaderboard(stage = 7) { return rpc('leaderboard', { p_stage: stage }); },
      async unitResults(lid) { const r = await rest(`unit_results?learner_id=eq.${lid}`); return Object.fromEntries(r.map(x => [x.unit, { pct: Number(x.first_pass_pct), at: x.first_pass_at, stage: x.stage }])); },
      async issueCertificate(lid, units, stage = 7) { const code = await rpc('issue_certificate', { p_learner: lid, p_stage: stage }); return this.certificate(lid, stage).then(c => c || { code }); },
      async certificate(lid, stage = 7) { const r = await rest(`certificates?learner_id=eq.${lid}&stage=eq.${stage}`); return r[0] ? { code: r[0].code, name: r[0].name_on_certificate, date: r[0].issued_at.slice(0, 10) } : null; },
      async verifyCertificate(code) { const r = await fetch(`${URL_}/rest/v1/rpc/verify_certificate`, { method: 'POST', headers: { apikey: ANON, 'Content-Type': 'application/json' }, body: JSON.stringify({ p_code: code }) }); const j = await r.json(); return j && j[0] ? j[0] : null; },
      async subscription() { const r = await rest(`subscriptions?parent_id=eq.${uid()}&order=updated_at.desc&limit=1`); const s = r[0];
        const active = !!(s && ['trialing', 'active', 'past_due'].includes(s.status) && (!s.current_period_end || Date.parse(s.current_period_end) > Date.now())); return { active, ...(s || { status: 'none' }) }; },
      async checkout(plan) { // Paddle Billing overlay checkout; the webhook (api/paddle-webhook.js) records the subscription
        if (!window.Paddle) await new Promise((ok, no) => { const s = document.createElement('script'); s.src = 'https://cdn.paddle.com/paddle/v2/paddle.js'; s.onload = ok; s.onerror = no; document.head.append(s); });
        if (CFG.paddle.env === 'sandbox') Paddle.Environment.set('sandbox'); Paddle.Initialize({ token: CFG.paddle.token });
        Paddle.Checkout.open({ items: [{ priceId: CFG.paddle.prices[plan], quantity: 1 }], customer: { email: S.user.email }, customData: { parent_id: uid() } });
        return { opened: true };
      },
      async cancelSubscription() { throw err('use_paddle_portal'); },
      async consents() { return rest(`consents?parent_id=eq.${uid()}&order=at.desc`); },
      async exportData() { return api('account?export=1'); },
      async deleteAccount(confirm) { const r = await api('account', { method: 'POST', body: { confirm } }); keep(null); return r; },
      async report(r) { return (await rest('reports', { method: 'POST', prefer: 'return=representation', body: { reporter_id: uid(), learner_id: r.learnerId || null, unit: r.unit || null, question_id: r.questionId || null, kind: r.kind, message: r.message } }))[0]; },
      async reports() { return rest('reports?order=created_at.desc&limit=100'); },
      async setReportStatus(id, status) { await rest(`reports?id=eq.${id}`, { method: 'PATCH', body: { status } }); },
      async notifications() { if (!S) return []; return rest(`notifications?parent_id=eq.${uid()}&order=created_at.desc&limit=30`); },
      async markNotificationsRead() { await rest(`notifications?parent_id=eq.${uid()}&read_at=is.null`, { method: 'PATCH', body: { read_at: new Date().toISOString() } }); },
      track(name, props, essential = true) { if (!S) return; if (!essential && !(profileCache && profileCache.product_analytics)) return;
        rest('events', { method: 'POST', body: { learner_id: props && props.learner || null, parent_id: uid(), name, props, essential } }).catch(() => { }); },
      async itemStats(unit) { return rpc('item_stats', { p_unit: unit }); },
      async videoStats() { return []; },
      demo: null
    };
  }

  window.Backend = CFG.mode === 'live' && CFG.supabaseUrl ? LiveBackend() : DemoBackend();
})();
