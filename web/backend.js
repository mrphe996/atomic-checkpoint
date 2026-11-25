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
    const keyedDemo = (unit, k) => { const ov = {}; Object.entries(((D.admin || {}).overrides) || {}).forEach(([id, o]) => { if (o.unit === unit) ov[id] = { hidden: o.hidden, patch: o.key_patch }; }); return Object.keys(ov).length ? GradeCore.applyOverrides(k, ov, { voidHidden: true }) : k; };
    function recordFinal(lid, unit, at) {
      const a = ownerOf(lid); const l = a.learners.find(x => x.id === lid);
      if (at.status === 'final' && at.passed) {
        D.results[lid] = D.results[lid] || {};
        if (!D.results[lid][unit]) D.results[lid][unit] = { pct: at.pct, at: new Date().toISOString(), stage: Number((unit.match(/^stage(\d+)/) || [0, 7])[1]) };
        const first = !D.results[lid][unit + ':notified']; D.results[lid][unit + ':notified'] = true;
        const un = Number(unit.slice(-2)), ut = (((window.Core && Core.INDEX) || { units: [] }).units.find(u => u.n === un) || {}).t || ''; const uname = `Unit ${un}${ut ? ': ' + ut : ''}`;
        note(a, lid, 'test_passed', `You passed ${uname}!`, `Score ${at.pct.toFixed(1)}%`);
        if (first && l.parent_email) (D.outbox = D.outbox || []).push({ to_email: l.parent_email, kind: 'unit_complete', subject: `${l.nickname} has finished ${uname} on Atomic`, created_at: new Date().toISOString(), status: 'queued' });
      } else if (at.status === 'final') note(a, lid, 'test_marked', 'Your Unit Test has been marked', `Score ${at.pct.toFixed(1)}%`);
    }
    const roadmapAll = () => { if (!D.roadmap) { D.roadmap = [['One stage per learner, with subject plans', 'Choose your stage when you sign up, then one subject or the whole stage. The next stage opens when 80% of your lessons and Unit Tests are done.', 'released', 'November 2026', 'Account'],
          ['Primary Mathematics: deeper lessons', 'Every Stage 3–6 lesson now explains why each method works, with a worked example, a method box and reasoning questions.', 'released', 'November 2026', 'Mathematics'],
          ['Online payment', 'Pay for a subject or a whole stage by card and other local methods.', 'building', 'December 2026', 'Account'],
          ['Sign in with Google and Apple', 'Log in with one tap, without a new password.', 'planned', 'December 2026', 'Account'],
          ['Weekly report for parents', 'A short email each week: time spent, lessons finished and Unit Test results.', 'planned', 'January 2027', 'Parents']].map(([title, body, status, target, tag], i) => ({ id: i + 1, title, body, status, target, tag, sort: (i + 1) * 10, published: true })); }
      return D.roadmap.slice().sort((a, b) => a.sort - b.sort); };
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
            school_id: form.schoolId || null, school_other: form.schoolId ? null : (form.schoolOther || null), parent_email: pe || null, consent_status: 'not_required', stage: [1, 2, 3, 4, 5, 6, 7, 8, 9].includes(Number(form.stage)) ? Number(form.stage) : 7, leaderboard_opt_in: false, created_at: now }],
          subscription: null, notifications: [], reports: [] };
        if (form.tester) { D.admin = D.admin || { overrides: {}, units: {}, ann: [], audit: [], settings: { mock_payments: 'on' } }; (D.admin.testers = D.admin.testers || {})[D.accounts[email].learners[0].id] = true; }   // preview only (automated tests)
        D.session = email; save(); return this.me();
      },
      async schools(country) { return (window.ATOMIC_SCHOOLS || []).filter(s => s.country === country); },
      async signIn({ email, password }) { email = String(email || '').trim().toLowerCase(); const a = D.accounts[email]; if (!a || a.pw !== await sha(password)) throw err('bad_credentials'); if (a.profile.disabled) throw err('account_disabled'); D.session = email; save(); return this.me(); },
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
      async isTester(lid) { return !!((((D.admin || {}).testers) || {})[lid]); },
      isMultiStage(lid) { return !!(D.multiStage || {})[lid]; },
      devMultiStage(lid) { (D.multiStage = D.multiStage || {})[lid] = true; save(); },   // preview only: lets automated tests buy courses of several stages (no other rule changes)
      devTester(lid) { D.admin = D.admin || { overrides: {}, units: {}, ann: [], audit: [], settings: { mock_payments: 'on' } }; (D.admin.testers = D.admin.testers || {})[lid] = true; save(); },   // preview only: lets the automated tests study several stages
      async enrolments(lid) { mine(lid); return ((D.enrol || {})[lid] || []).slice(); },
      async enrol(lid, stage, amount) { const lr = mine(lid); D.enrol = D.enrol || {}; const l = (D.enrol[lid] = D.enrol[lid] || []);
        // one stage per learner (same rule as enrol_stage): another level only after 80 % of the current level's Unit Tests are passed
        const lv = stage % 10, cur = lr.stage || 7, own = l.filter(e => e.status !== 'canceled');
        if (own.length && lv !== cur && !((D.admin || {}).testers || {})[lid] && !(D.multiStage || {})[lid]) {   // testers (staff) may open any stage
          let need = 0, have = 0;
          for (const k of own.map(e => e.stage).filter(k => k % 10 === cur)) {
            const ix = await fetch(`content/stage${k}.json`).then(r => r.ok ? r.json() : { units: [] }).catch(() => ({ units: [] }));
            need += (ix.units || []).length; have += Object.keys(D.results[lid] || {}).filter(u => !u.includes(':') && u.startsWith(`stage${k}-unit`)).length;
          }
          if (!need || have < Math.ceil(need * 0.8)) throw err('stage_locked', { have, need });
        }
        lr.stage = lv;
        if (!l.some(e => e.stage === stage)) l.push({ stage, method: 'test', amount: amount || null, status: 'active', created_at: new Date().toISOString() });
        note(need(), lid, 'billing', `You are enrolled in Cambridge Stage ${stage}`, 'Test checkout – no money was taken.'); save(); return 'ok'; },
      async startTest({ learnerId, unit, form }) { mine(learnerId); D.starts = D.starts || {}; const k = `${learnerId}|${unit}|${form}`; D.starts[k] = D.starts[k] || new Date().toISOString(); save();
        const minutes = /^ch-/.test(unit) ? ({ 'ch-primary': 45, 'ch-olympiad': 90 }[unit] || 60) : /-final$/.test(unit) ? 60 : /-cp$/.test(unit) ? 45 : TestRules.UNIT_MINUTES; return { startedAt: D.starts[k], minutes, deadline: new Date(Date.parse(D.starts[k]) + minutes * 60000).toISOString(), now: new Date().toISOString() }; },
      async saveProgress(lid, unit, state) { mine(lid); (D.progress[lid] = D.progress[lid] || {})[unit] = JSON.parse(JSON.stringify(state)); save(); },
      // Maths Challenge practice (same rules as api/challenge.js): first answer kept, full solution returned
      async challenge({ action, learnerId, unit, form, qid, answer }) { need(); mine(learnerId); if (!/^ch-[a-z]+$/.test(String(unit))) throw err('unknown_unit');
        const keys = keyedDemo(unit, await (await fetch(`content/demo/${unit}.tests.json`)).json()); const byId = {}; for (const [k, p] of Object.entries(keys.papers)) for (const q of p) byId[q.id] = { q, form: k };
        const mineP = (((D.chp = D.chp || {})[learnerId] = D.chp[learnerId] || {})[unit] = D.chp[learnerId][unit] || {}); const sol = q => ({ answer: GradeCore.answerText(q), reason: q.reason || '' });
        if (action === 'state') { const solutions = {}; Object.keys(mineP).forEach(id => { if (byId[id]) solutions[id] = sol(byId[id].q); }); return { done: Object.entries(mineP).map(([id, x]) => ({ form: x.form, qid: id, ok: x.ok, answer: x.answer })), solutions }; }
        if (action === 'solutions') { if (!keys.papers[form]) throw err('wrong_paper'); if (!(((D.attempts[learnerId] || {})[unit]) || []).some(x => x.form === form && x.status === 'final')) throw err('not_taken'); return { solutions: Object.fromEntries(keys.papers[form].map(q => [q.id, sol(q)])) }; }
        const hit = byId[qid]; if (!hit || hit.form !== form) throw err('wrong_question');
        if (mineP[qid]) return { ok: mineP[qid].ok, first: mineP[qid].answer, ...sol(hit.q), repeat: true };
        const ok = !hit.q.voided && !!GradeCore.grade(hit.q, answer).ok; mineP[qid] = { form, ok, answer }; save(); return { ok, ...sol(hit.q) }; },
      async attempts(lid, unit) { mine(lid); return ((D.attempts[lid] || {})[unit] || []).slice(); },
      async submitTest({ learnerId, unit, form, answers, clientKey, meta }) { // same rules as api/submit-test.js
        const a = need(); const l = mine(learnerId);
        if ((CFG.billing || 'off') !== 'off' && !subActive(a)) throw err('subscription_required');
        const stage = Number((unit.match(/^stage(\d+)/) || [0, 0])[1]); if (stage && stage !== (l.stage || 7) && !(((D.enrol || {})[learnerId]) || []).some(e => e.stage === stage)) throw err('not_enrolled');
        const list = ((D.attempts[learnerId] = D.attempts[learnerId] || {})[unit] = D.attempts[learnerId][unit] || []);
        const keys = keyedDemo(unit, await (await fetch(`content/demo/${unit}.tests.json`)).json());
        const same = list.find(x => x.clientKey === clientKey);
        if (same) return { attempt: same, solutions: TestRules.solutions(keys.papers[same.form]), duplicate: true };
        D.starts = D.starts || {}; const sk = `${learnerId}|${unit}|${form}`; const started = D.starts[sk] || null; const duration = started ? Math.round((Date.now() - Date.parse(started)) / 1000) : null;
        if (keys.final) {
          const lastF = list[list.length - 1]; if (lastF && lastF.status === 'pending') throw err('awaiting_marking');
          if (!keys.papers[form]) throw err('wrong_paper'); if (list.some(x => x.form === form)) throw err('paper_done');
          if (/^ch-/.test(unit) && Object.values(((D.chp || {})[learnerId] || {})[unit] || {}).some(x => x.form === form)) throw err('practised');
          const passes = Object.keys(D.results[learnerId] || {}).filter(k => !k.includes(':')).length;
          const xp = TestRules.xpTotal(D.progress[learnerId] || {}, passes); if (TestRules.levelOf(xp) < keys.level) throw err('level_required', { level: keys.level, have: TestRules.levelOf(xp) });
          const paper = keys.papers[form];
          const at = TestRules.finalizeFinal(TestRules.mark(paper, answers, { n: list.length + 1, form, id: uuid(), clientKey }), paper, keys.max, keys.pass);
          at.duration = duration; at.overtime = duration != null && duration > (keys.minutes || 60) * 60 + TestRules.GRACE_S; at.leaves = (meta && meta.leaves) || 0; at.autoSubmitted = !!(meta && meta.auto); delete D.starts[sk];
          list.push(at); if (at.status === 'final' && at.passed && !/^ch-/.test(unit)) note(a, learnerId, 'test_passed', `You passed the end-of-year exam (paper ${form})!`, `Score ${at.pct.toFixed(1)}%`); save();
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
        const have = Object.keys(D.results[lid] || {}).filter(k => !k.includes(':') && k.startsWith(`stage${stage}-unit`)).length; if (have < Math.ceil(stageUnits * 0.8)) throw err('stage_incomplete', { have, need: Math.ceil(stageUnits * 0.8) });   // 80 % of the Unit Tests (same rule as issue_certificate)
        const hex = [...crypto.getRandomValues(new Uint8Array(4))].map(x => x.toString(16).padStart(2, '0')).join('').toUpperCase();
        D.certs[key] = { code: `AE-${stage >= 20 ? 'E' + (stage - 20) : stage >= 10 ? 'M' + (stage - 10) : 'S' + stage}-${new Date().getFullYear()}-${hex}`, name: l.certificate_name || l.nickname, date: new Date().toISOString().slice(0, 10), stage }; save(); return D.certs[key];
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

      /* content changes made in the admin console (shared by every account in this browser) */
      logError(e) { D.errors = (D.errors || []).concat([{ at: new Date().toISOString(), email: (D.session && D.accounts[D.session] || {}).email || null, ...e }]).slice(-200); save(); },
      async contentOverrides(unit) { const A = D.admin || {}; return Object.entries(A.overrides || {}).filter(([, o]) => o.unit === unit).map(([id, o]) => ({ question_id: id, hidden: o.hidden, patch: o.is_test ? o.public_patch : (o.key_patch || o.public_patch) })); },
      async unitSettings() { return Object.entries((D.admin || {}).units || {}).map(([unit, u]) => ({ unit, ...u })); },
      async announcements() { return ((D.admin || {}).ann || []).filter(x => x.active); },
      // news page: the roadmap of coming features (preview data is seeded once; admins edit it)
      async roadmap() { return roadmapAll().filter(x => x.published); },
      admin: (() => {
        const A = () => (D.admin = D.admin || { overrides: {}, units: {}, ann: [], audit: [], settings: { mock_payments: 'on' } });
        const guard = () => { const a = need(); if (a.profile.role !== 'admin') throw err('admin_only'); return a; };
        const log = (action, target, detail) => { A().audit.unshift({ id: A().audit.length + 1, at: new Date().toISOString(), actor_email: need().email, action, target, detail: detail || {} }); if (A().audit.length > 1000) A().audit.length = 1000; };
        const allLearners = () => Object.values(D.accounts).flatMap(acc => acc.learners.map(l => ({ acc, l })));
        const allAttempts = () => Object.entries(D.attempts).flatMap(([lid, units]) => Object.entries(units).flatMap(([unit, list]) => list.map(at => ({ lid, unit, at }))));
        const keysFor = async unit => { const k = await (await fetch(`content/demo/${unit}.tests.json`)).json(); const ov = {}; Object.entries(A().overrides).forEach(([id, o]) => { if (o.unit === unit) ov[id] = { hidden: o.hidden, patch: o.key_patch }; }); return { raw: k, keyed: GradeCore.applyOverrides(k, ov, { voidHidden: true }) }; };
        return {
          keysFor,
          async overview() { guard(); const accs = Object.values(D.accounts); const by = {}; accs.forEach(a => { by[a.profile.role] = (by[a.profile.role] || 0) + 1; });
            const days = [...Array(14)].map((_, i) => { const d = new Date(Date.now() - (13 - i) * 864e5).toISOString().slice(0, 10); return { day: d, n: accs.filter(a => (a.profile.created_at || '').slice(0, 10) === d).length }; });
            const atts = allAttempts(); const units = {}; atts.filter(x => x.at.status === 'final').forEach(({ unit, at }) => { const u = (units[unit] = units[unit] || { unit, attempts: 0, passed: 0, sum: 0 }); u.attempts++; if (at.passed) u.passed++; u.sum += at.pct || 0; });
            const enr = {}; Object.values(D.enrol || {}).flat().forEach(e => { enr[e.stage] = (enr[e.stage] || 0) + 1; });
            const week = Date.now() - 7 * 864e5;
            return { accounts: accs.length, by_role: by, disabled: accs.filter(a => a.profile.disabled).length, learners: allLearners().length, testers: Object.keys(A().testers || {}).length,
              active_7d: Object.keys(D.progress).length, active_30d: Object.keys(D.progress).length, signups_14d: days, attempts_7d: atts.filter(x => x.at.ts > week).length, attempts_total: atts.length,
              pending_marking: atts.filter(x => x.at.status === 'pending').length, open_reports: accs.flatMap(a => a.reports).filter(r => r.status === 'open').length, enrolments: enr, certificates: Object.keys(D.certs).length,
              units: Object.values(units).map(u => ({ unit: u.unit, attempts: u.attempts, passed: u.passed, avg_pct: Math.round(u.sum / u.attempts * 10) / 10 })).sort((x, y) => x.unit.localeCompare(y.unit)),
              overrides: Object.keys(A().overrides).length, hidden_units: Object.values(A().units).filter(u => u.hidden).length };
          },
          async users(q = '', limit = 50, offset = 0) { guard(); q = String(q || '').toLowerCase();
            const rows = Object.values(D.accounts).filter(a => !q || a.email.includes(q) || (a.profile.display_name || '').toLowerCase().includes(q) || a.profile.role === q || a.learners.some(l => l.nickname.toLowerCase().includes(q)))
              .sort((x, y) => (y.profile.created_at || '').localeCompare(x.profile.created_at || ''));
            return rows.slice(offset, offset + limit).map(a => ({ id: a.id, email: a.email, role: a.profile.role, display_name: a.profile.display_name, country: a.profile.country, disabled: !!a.profile.disabled, created_at: a.profile.created_at, last_sign_in_at: null, learners: a.learners.length, total: rows.length })); },
          async user(id) { guard(); const a = Object.values(D.accounts).find(x => x.id === id); if (!a) throw err('not_found');
            return { profile: { ...a.profile, email: a.email }, subscription: a.subscription, learners: a.learners.map(l => ({ learner: l, tester: !!(A().testers || {})[l.id], enrolments: ((D.enrol || {})[l.id] || []).slice(),
              results: Object.entries(D.results[l.id] || {}).filter(([k]) => !k.includes(':')).map(([unit, r]) => ({ unit, pct: r.pct, at: r.at })),
              attempts: Object.entries(D.attempts[l.id] || {}).flatMap(([unit, list]) => list.map(at => ({ id: at.id, unit, n: at.n, form: at.form, status: at.status, score: at.score, pct: at.pct, passed: at.passed, created_at: new Date(at.ts).toISOString(), leaves: at.leaves || 0, overtime: !!at.overtime }))).reverse(),
              progress: Object.entries(D.progress[l.id] || {}).map(([unit, st]) => ({ unit, updated_at: null, items: Object.keys((st && st.items) || {}).length })),
              certificates: Object.entries(D.certs).filter(([k]) => k.startsWith(l.id)).map(([, c]) => c) })) }; },
          async setRole(id, role) { const me = guard(); if (id === me.id && role !== 'admin') throw err('own_admin'); Object.values(D.accounts).find(x => x.id === id).profile.role = role; log('set_role', id, { role }); save(); },
          async setDisabled(id, on) { const me = guard(); if (id === me.id) throw err('own_account'); Object.values(D.accounts).find(x => x.id === id).profile.disabled = !!on; log(on ? 'disable_account' : 'enable_account', id); save(); },
          async setTester(lid, on) { guard(); const t = (A().testers = A().testers || {}); if (on) t[lid] = true; else delete t[lid]; log(on ? 'tester_on' : 'tester_off', lid); save(); },
          async roadmap() { guard(); return roadmapAll(); },
          async saveRoadmap(x) { guard(); roadmapAll(); const it = x.id ? D.roadmap.find(y => y.id === x.id) : null; const v = { title: x.title, body: x.body || '', status: x.status || 'planned', target: x.target || '', tag: x.tag || '', sort: Number(x.sort) || 0, published: x.published !== false };
            if (it) Object.assign(it, v); else D.roadmap.push({ id: Math.max(0, ...D.roadmap.map(y => y.id)) + 1, ...v }); log('roadmap_save', x.title); save(); },
          async deleteRoadmap(id) { guard(); roadmapAll(); D.roadmap = D.roadmap.filter(y => y.id !== id); log('roadmap_delete', String(id)); save(); },
          async setLearnerStage(lid, stage) { guard(); const x = allLearners().find(y => y.l.id === lid); if (x) x.l.stage = stage; log('learner_stage', lid); save(); },
          async setEnrolment(lid, stage, on) { guard(); D.enrol = D.enrol || {}; const l = (D.enrol[lid] = D.enrol[lid] || []); if (on) { if (!l.some(e => e.stage === stage)) l.push({ stage, method: 'admin', status: 'active', created_at: new Date().toISOString() }); } else D.enrol[lid] = l.filter(e => e.stage !== stage); log(on ? 'enrol' : 'unenrol', lid, { stage }); save(); },
          async resetProgress(lid, unit) { guard(); if (D.progress[lid]) delete D.progress[lid][unit]; log('reset_progress', lid, { unit }); save(); },
          async attempts(unit = '', status = '') { guard(); return allAttempts().filter(x => (!unit || x.unit === unit || x.unit.startsWith(unit + '-')) && (!status || x.at.status === status)).map(({ lid, unit, at }) => { const o = allLearners().find(y => y.l.id === lid) || {};
            return { id: at.id, learner_id: lid, nickname: o.l ? o.l.nickname : '?', email: o.acc ? o.acc.email : '', unit, n: at.n, form: at.form, status: at.status, score: at.score, pct: at.pct, passed: at.passed, created_at: new Date(at.ts).toISOString(), leaves: at.leaves || 0, overtime: !!at.overtime, duration_s: at.duration }; }).sort((x, y) => y.created_at.localeCompare(x.created_at)); },
          async voidAttempt(id) { guard(); for (const [lid, units] of Object.entries(D.attempts)) for (const [unit, list] of Object.entries(units)) { const i = list.findIndex(x => x.id === id); if (i < 0) continue; const at = list[i]; list.splice(i, 1);
            if (at.passed && D.results[lid] && D.results[lid][unit]) delete D.results[lid][unit]; log('void_attempt', id, { unit, form: at.form, score: at.score }); save(); return; } throw err('not_found'); },
          async regrade(id) { guard(); for (const [lid, units] of Object.entries(D.attempts)) for (const [unit, list] of Object.entries(units)) { const at = list.find(x => x.id === id); if (!at) continue;
            const { keyed } = await keysFor(unit); const paper = keyed.papers[at.form]; const from = at.score; const was = at.passed;
            const fresh = TestRules.mark(paper, at.answers || {}, { n: at.n, form: at.form, id: at.id, clientKey: at.clientKey });
            for (const q of fresh.pending) if (at.per[q] && at.per[q].pts != null) fresh.per[q].pts = at.per[q].pts;
            if (keyed.final) TestRules.finalizeFinal(fresh, paper, keyed.max, keyed.pass); else TestRules.finalize(fresh, paper, await loadPublic(unit), ((D.progress[lid] || {})[unit]) || {});
            Object.assign(at, { per: fresh.per, auto: fresh.auto, score: fresh.score, pct: fresh.pct, passed: fresh.passed, status: fresh.status, byObj: fresh.byObj, weak: fresh.weak, remed: fresh.remed });
            if (was && !at.passed && D.results[lid]) delete D.results[lid][unit];
            if (!was && at.passed) { D.results[lid] = D.results[lid] || {}; if (!D.results[lid][unit] && !keyed.final) D.results[lid][unit] = { pct: at.pct, at: new Date().toISOString(), stage: Number(unit.match(/^stage(\d+)/)[1]) }; }
            const r = { id, changed: from !== at.score || was !== at.passed, from, to: at.score, passed: at.passed }; log('regrade', id, r); save(); return { result: r, attempt: at }; } throw err('not_found'); },
          async regradeUnit(unit) { guard(); const ids = allAttempts().filter(x => x.unit === unit && x.at.status === 'final').map(x => x.at.id); const out = []; for (const id of ids) out.push((await this.regrade(id)).result);
            const changed = out.filter(x => x.changed); log('regrade_unit', unit, { attempts: out.length, changed: changed.length }); save(); return { attempts: out.length, changed: changed.length, results: changed }; },
          async setUnit(unit, hidden, note) { guard(); A().units[unit] = { hidden: !!hidden, note: note || null, updated_at: new Date().toISOString() }; log(hidden ? 'hide_unit' : 'show_unit', unit, { note }); save(); },
          async overrides(unit) { guard(); return Object.entries(A().overrides).filter(([, o]) => o.unit === unit).map(([question_id, o]) => ({ question_id, ...o })); },
          async papers(unit) { guard(); const { raw } = await keysFor(unit); const ov = {}; Object.entries(A().overrides).forEach(([id, o]) => { if (o.unit === unit) ov[id] = { hidden: o.hidden, patch: o.key_patch }; }); return { unit, final: !!raw.final, papers: raw.papers, overrides: ov }; },
          async saveQuestion(qid, unit, isTest, hidden, pub, key) { guard(); if (isTest && pub && ['answer', 'model', 'rubric', 'accept', 'expr'].some(k => k in pub)) throw err('answers_in_public');
            A().overrides[qid] = { unit, is_test: !!isTest, hidden: !!hidden, public_patch: pub || null, key_patch: key || null, updated_at: new Date().toISOString() }; log('edit_question', qid, { unit, hidden: !!hidden, edited: !!key }); save(); },
          async resetQuestion(qid) { guard(); delete A().overrides[qid]; log('reset_question', qid); save(); },
          async announce(title, body, audience, level) { guard(); const x = { id: Date.now(), title, body: body || '', audience: audience || 'all', level: level || 'info', active: true, created_at: new Date().toISOString() }; A().ann.unshift(x); log('announce', String(x.id), { title, audience }); save(); return x.id; },
          async setAnnouncement(id, active) { guard(); const x = A().ann.find(y => y.id === id); if (x) x.active = !!active; log(active ? 'announcement_on' : 'announcement_off', String(id)); save(); },
          async allAnnouncements() { guard(); return A().ann.slice(); },
          async settings() { guard(); return { ...A().settings }; },
          async setSetting(name, value) { guard(); if (name !== 'mock_payments' || !['on', 'off'].includes(value)) throw err('setting'); A().settings[name] = value; log('setting', name, { value }); save(); },
          async audit() { guard(); return A().audit.slice(); },
          async errors() { guard(); return (D.errors || []).slice().reverse(); },
          async setReport(id, status) { guard(); for (const x of Object.values(D.accounts)) { const r = x.reports.find(y => y.id === id); if (r) r.status = status; } log('report_status', String(id), { status }); save(); }
        };
      })(),
      /* tester tools (demo only) */
      demo: { setRole(r) { const a = need(); a.profile.role = r; save(); }, reset() { try { localStorage.removeItem(KEY); } catch (e) { } D = { accounts: {}, session: null, progress: {}, attempts: {}, results: {}, certs: {}, events: [] }; },
        simulateOtherUnits(lid, pct) { const g = (window.Core && Core.STAGE) || 7, cur = window.Core && Core.UNIT, n0 = (window.Core && Core.unitCount()) || 14; D.results[lid] = D.results[lid] || {}; for (let n = 1; n <= n0; n++) { const u = `stage${g}-unit` + String(n).padStart(2, '0'); if (u !== cur && !D.results[lid][u]) D.results[lid][u] = { pct, at: new Date().toISOString(), stage: g, simulated: true }; } save(); },
        outbox() { return (D.outbox || []).slice(); },
        simulateFinal(lid, pct) { const fu = `stage${(window.Core && Core.STAGE) || 7}-final`; const l = ((D.attempts[lid] = D.attempts[lid] || {})[fu] = D.attempts[lid][fu] || []); if (!l.some(x => x.passed)) l.push({ id: uuid(), n: l.length + 1, form: '10', ts: Date.now(), status: 'final', passed: true, score: pct / 2, pct, per: {}, auto: pct / 2, pending: [], byObj: {}, simulated: true }); save(); },
        simulateXp(lid, n) { const xu = `stage${(window.Core && Core.STAGE) || 7}-unit02`; const p = ((D.progress[lid] = D.progress[lid] || {})[xu] = D.progress[lid][xu] || {}); p.items = p.items || {}; for (let i = 0; i < n; i++) p.items['sim' + i] = { done: true, ok: true, score: 1, tries: 1, sim: true }; save(); },
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
      async isTester(lid) { const r = await rest(`testers?learner_id=eq.${lid}&select=learner_id`); return Array.isArray(r) && r.length > 0; },
      async enrol(lid, stage, amount) { try { return await rpc('enrol_stage', { p_learner: lid, p_stage: stage, p_amount: amount || null }); } catch (e) { throw err(/not open/.test(e.detail || '') ? 'payments_closed' : /stage locked/.test(e.detail || '') ? 'stage_locked' : 'enrol_failed', { detail: e.detail }); } },
      async startTest(b) { return api('start-test', { method: 'POST', body: b }); },
      async saveProgress(lid, unit, state) { await rest('progress?on_conflict=learner_id,unit', { method: 'POST', prefer: 'resolution=merge-duplicates', body: { learner_id: lid, unit, state, updated_at: new Date().toISOString() } }); },
      async attempts(lid, unit) { const rows = await rest(`attempts?learner_id=eq.${lid}&unit=eq.${unit}&order=n.asc`);
        return rows.map(r => ({ id: r.id, n: r.n, form: r.form, ts: Date.parse(r.created_at), answers: r.answers, per: r.per, auto: Number(r.auto), pending: Object.keys(r.per).filter(k => r.per[k].teacher), status: r.status, score: r.score == null ? null : Number(r.score), pct: r.pct == null ? null : Number(r.pct), passed: r.passed, byObj: r.by_obj, weak: r.weak || [], remed: r.remed || [], duration: r.duration_s, overtime: !!r.overtime, leaves: Number(r.leaves || 0), autoSubmitted: !!r.auto_submitted })); },
      async submitTest(b) { return api('submit-test', { method: 'POST', body: b }); },
      async aiMark(b) { return api('ai-mark', { method: 'POST', body: b }); },
      async challenge(b) { return api('challenge', { method: 'POST', body: b }); },
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
      logError(e) { const h = { apikey: ANON, 'Content-Type': 'application/json', Authorization: `Bearer ${S && Date.now() < S.expires_at ? S.access_token : ANON}` };
        fetch(`${URL_}/rest/v1/rpc/log_client_error`, { method: 'POST', headers: h, body: JSON.stringify({ p_msg: e.msg, p_src: e.src || null, p_line: e.line || null, p_route: e.route || null, p_ua: e.ua || null, p_release: e.release || null }) }).catch(() => { }); },
      async contentOverrides(unit) { const r = await fetch(`${URL_}/rest/v1/rpc/content_overrides`, { method: 'POST', headers: { apikey: ANON, 'Content-Type': 'application/json', ...(S ? { Authorization: `Bearer ${S.access_token}` } : {}) }, body: JSON.stringify({ p_unit: unit }) }); return r.ok ? r.json() : []; },
      async unitSettings() { const r = await fetch(`${URL_}/rest/v1/unit_settings?select=unit,hidden,note`, { headers: { apikey: ANON } }); return r.ok ? r.json() : []; },
      async announcements() { const r = await fetch(`${URL_}/rest/v1/announcements?active=eq.true&order=created_at.desc&limit=5`, { headers: { apikey: ANON } }); return r.ok ? r.json() : []; },
      async roadmap() { const r = await fetch(`${URL_}/rest/v1/roadmap?published=eq.true&order=sort.asc`, { headers: { apikey: ANON } }); return r.ok ? r.json() : []; },
      admin: {
        overview: () => rpc('admin_overview'),
        errors: () => rpc('admin_client_errors', { p_limit: 300 }),
        users: (q = '', limit = 50, offset = 0) => rpc('admin_users', { p_q: q, p_limit: limit, p_offset: offset }),
        user: id => rpc('admin_user', { p_id: id }),
        setRole: (id, role) => rpc('admin_set_role', { p_user: id, p_role: role }),
        setDisabled: (id, on) => rpc('admin_set_disabled', { p_user: id, p_on: !!on }),
        setTester: (lid, on) => rpc('admin_set_tester', { p_learner: lid, p_on: !!on }),
        setEnrolment: (lid, stage, on) => rpc('admin_set_enrolment', { p_learner: lid, p_stage: stage, p_on: !!on }),
        roadmap: () => rest('roadmap?order=sort.asc'),
        saveRoadmap: x => rpc('admin_roadmap_save', { p_id: x.id || null, p_title: x.title, p_body: x.body || '', p_status: x.status || 'planned', p_target: x.target || '', p_tag: x.tag || '', p_sort: Number(x.sort) || 0, p_published: x.published !== false }),
        deleteRoadmap: id => rpc('admin_roadmap_delete', { p_id: id }),
        setLearnerStage: (lid, stage) => rpc('admin_set_learner_stage', { p_learner: lid, p_stage: stage }),
        resetProgress: (lid, unit) => rpc('admin_reset_progress', { p_learner: lid, p_unit: unit }),
        attempts: (unit = '', status = '') => rpc('admin_attempts', { p_unit: unit, p_status: status, p_limit: 300 }),
        voidAttempt: id => rpc('admin_void_attempt', { p_attempt: id }),
        regrade: id => api('admin', { method: 'POST', body: { action: 'regrade', attemptId: id } }),
        regradeUnit: unit => api('admin', { method: 'POST', body: { action: 'regrade_unit', unit } }),
        setUnit: (unit, hidden, note) => rpc('admin_set_unit', { p_unit: unit, p_hidden: !!hidden, p_note: note || null }),
        overrides: unit => rpc('admin_overrides', { p_unit: unit }),
        papers: unit => api('admin?unit=' + encodeURIComponent(unit)),
        async saveQuestion(qid, unit, isTest, hidden, pub, key) { await rpc('admin_save_question', { p_qid: qid, p_unit: unit, p_is_test: !!isTest, p_hidden: !!hidden, p_public: pub || null, p_key: key || null }); try { await api('admin', { method: 'POST', body: { action: 'refresh', unit } }); } catch (e) { } },
        async resetQuestion(qid, unit) { await rpc('admin_reset_question', { p_qid: qid }); try { await api('admin', { method: 'POST', body: { action: 'refresh', unit } }); } catch (e) { } },
        announce: (title, body, audience, level) => rpc('admin_announce', { p_title: title, p_body: body || '', p_audience: audience || 'all', p_level: level || 'info' }),
        setAnnouncement: (id, active) => rpc('admin_set_announcement', { p_id: id, p_active: !!active }),
        allAnnouncements: () => rest('announcements?order=created_at.desc&limit=50'),
        settings: () => rpc('admin_settings'),
        setSetting: (name, value) => rpc('admin_set_setting', { p_name: name, p_value: value }),
        audit: () => rpc('admin_audit_log', { p_limit: 300 }),
        setReport: (id, status) => rpc('admin_set_report', { p_id: id, p_status: status })
      },
      demo: null
    };
  }

  window.Backend = CFG.mode === 'live' && CFG.supabaseUrl ? LiveBackend() : DemoBackend();
  // page errors are reported (at most 10 per page view) so the team can see problems learners meet
  (function () {
    let n = 0; const seen = new Set();
    const send = (msg, src, line) => { msg = String(msg || '').slice(0, 500); if (!msg || n >= 10 || seen.has(msg)) return; seen.add(msg); n++;
      try { window.Backend.logError({ msg, src: src ? String(src).replace(location.origin, '') : null, line: line || null, route: location.hash.slice(0, 120), ua: navigator.userAgent.slice(0, 200), release: CFG.release || null }); } catch (e) { /* never break the page */ } };
    window.addEventListener('error', e => { if (e && e.message) send(e.message, e.filename, e.lineno); });
    window.addEventListener('unhandledrejection', e => { const r = e && e.reason; if (r && (r.code === 'sign_in' || r.name === 'AbortError')) return; send('Unhandled: ' + ((r && (r.message || r.code)) || String(r)), null, null); });
  })();
})();
