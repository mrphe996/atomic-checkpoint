/* Camday — admin console (#admin). Role 'admin' only; every change goes through Backend.admin and is written to the audit log.
   Tabs: Overview · Users · Content · Exams · Reports · Announcements · Settings · Audit log. */
(function () {
  const { el } = QE;
  const COURSES = [[1, 'Science Stage 1 (Primary)'], [2, 'Science Stage 2 (Primary)'], [3, 'Science Stage 3 (Primary)'], [4, 'Science Stage 4 (Primary)'], [5, 'Science Stage 5 (Primary)'], [6, 'Science Stage 6 (Primary)'], [7, 'Science Stage 7'], [8, 'Science Stage 8'], [9, 'Science Stage 9'], [11, 'Mathematics Stage 1 (Primary)'], [12, 'Mathematics Stage 2 (Primary)'], [13, 'Mathematics Stage 3 (Primary)'], [14, 'Mathematics Stage 4 (Primary)'], [15, 'Mathematics Stage 5 (Primary)'], [16, 'Mathematics Stage 6 (Primary)'], [17, 'Mathematics Stage 7'], [18, 'Mathematics Stage 8'], [19, 'Mathematics Stage 9'], ...[2, 3, 4, 5, 6, 7, 8, 9].map(n => [20 + n, `ESL Stage ${n}${n <= 6 ? ' (Primary)' : ''}`])];
  const courseName = g => (COURSES.find(c => c[0] === g) || [0, 'Stage ' + g])[1];
  const unitCourse = u => Number((String(u).match(/^stage(\d+)/) || [0, 0])[1]);
  const unitLabel = u => { const g = unitCourse(u), m = String(u).match(/-(unit(\d+)|final|cp)$/); return `${courseName(g)} · ${m ? (m[2] ? 'Unit ' + Number(m[2]) : m[1] === 'final' ? 'End-of-year exam' : 'Checkpoint') : u}`; };
  const day = t => (t ? new Date(t).toLocaleString('en-GB', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' }) : '—');
  const num = v => (v == null ? '—' : String(+(+v).toFixed(2)));
  const A = { show: 60, tab: 'overview', userQ: '', userId: null, course: 19, unit: '', qFilter: '', pool: 'all', examCourse: 19, examUnit: '', examStatus: '' };

  window.AtomicAdmin = function (H) {
    const { modal, toast, errText, $main, render } = H;
    const B = () => Backend.admin;
    const busy = async (fn, ok) => { try { const r = await fn(); if (ok) toast(ok); return r; } catch (e) { console.error(e); toast(errText(e)); throw e; } };
    const table = (head, rows, cls) => el('div', { class: 'tablewrap' }, el('table', { class: 'grid admintable ' + (cls || '') }, el('tr', {}, ...head.map(h => el('th', {}, h))), ...rows));
    const tag = (t, kind) => el('span', { class: 'tag ' + (kind || '') }, t);
    const stat = (big, small, href) => el(href ? 'a' : 'div', { class: 'card adstat', href: href || null }, el('b', {}, String(big)), el('small', {}, small));

    async function view() {
      const m = $main(); const me = Core.S.me;
      if (!me || me.profile.role !== 'admin') {
        m.append(el('section', { class: 'card narrow' }, el('h1', {}, 'Admin console'), el('p', {}, 'This area is for Camday administrators.'),
          Backend.demo ? el('button', { class: 'btn small', type: 'button', id: 'becomeAdmin', onclick: () => { Backend.demo.setRole('admin'); Core.S.me.profile.role = 'admin'; render(); } }, 'Make this preview account an administrator') : null));
        return;
      }
      const tabs = [['overview', 'Overview'], ['users', 'Users'], ['content', 'Content'], ['exams', 'Exams'], ['reports', 'Reports'], ['news', 'News & roadmap'], ['settings', 'Settings'], ['errors', 'Page errors'], ['audit', 'Audit log']];
      m.append(el('div', { class: 'adhead' }, el('div', {}, el('span', { class: 'eyebrow' }, 'CAMDAY'), el('h1', { style: 'margin:0' }, 'Admin console')),
        el('a', { class: 'btn small', href: '#staff' }, 'Marking queue →')),
        el('div', { class: 'btnrow adtabs', role: 'tablist' }, ...tabs.map(([k, t]) => el('button', { class: 'chip' + (A.tab === k ? ' on' : ''), type: 'button', role: 'tab', id: 'adTab-' + k, 'aria-selected': String(A.tab === k), onclick: () => { A.tab = k; render(); } }, t))));
      const box = el('div', { class: 'adbody', id: 'adBody' }); m.append(box);
      box.append(el('p', { class: 'muted' }, 'Loading…'));
      try { const f = { overview, users, content, exams, reports, news, settings, errors, audit }[A.tab]; const kids = await f(); box.innerHTML = ''; box.append(...[].concat(kids)); }
      catch (e) { console.error(e); box.innerHTML = ''; box.append(el('div', { class: 'banner adv', role: 'alert' }, errText(e))); }
    }

    /* ---------- overview ---------- */
    async function overview() {
      const o = await B().overview();
      const enr = o.enrolments || {}, roles = o.by_role || {};
      const maxD = Math.max(1, ...(o.signups_14d || []).map(d => d.n));
      return [
        el('div', { class: 'adstats' }, stat(o.accounts, `accounts · ${roles.student || 0} students · ${roles.parent || 0} parents · ${(roles.marker || 0) + (roles.admin || 0)} staff`, null),
          stat(o.learners, `learners · ${o.testers} testers`), stat(o.active_7d, `active learners (7 days) · ${o.active_30d} in 30 days`), stat(o.attempts_7d, `tests submitted (7 days) · ${o.attempts_total} total`),
          stat(o.pending_marking, 'waiting to be marked', '#staff'), stat(o.open_reports, 'open question reports'), stat(o.certificates, 'certificates issued'), stat(o.disabled, 'accounts switched off'),
          stat(o.overrides, 'questions edited or withdrawn'), stat(o.hidden_units, 'units hidden from learners')),
        el('section', { class: 'card' }, el('h3', { style: 'margin-top:0' }, 'Enrolments by course'),
          el('div', { class: 'adstats small' }, ...COURSES.map(([g, n]) => stat(enr[g] || 0, n)))),
        el('section', { class: 'card' }, el('h3', { style: 'margin-top:0' }, 'New accounts – last 14 days'),
          el('div', { class: 'adbars', role: 'img', 'aria-label': 'New accounts per day' }, ...(o.signups_14d || []).map(d => el('div', { class: 'adbar', title: `${d.day}: ${d.n}` }, el('b', {}, d.n ? String(d.n) : ''), el('i', { style: `height:${Math.round(d.n / maxD * 85)}%` }), el('small', {}, d.day.slice(8)))))),
        el('section', { class: 'card' }, el('h3', { style: 'margin-top:0' }, 'Results by unit and exam'),
          (o.units || []).length ? table(['Unit / exam', 'Finished attempts', 'Passed', 'Pass rate', 'Average'], o.units.map(u => el('tr', {}, el('td', {}, unitLabel(u.unit)), el('td', {}, String(u.attempts)), el('td', {}, String(u.passed)),
            el('td', {}, u.attempts ? Math.round(u.passed / u.attempts * 100) + '%' : '—'), el('td', {}, u.avg_pct == null ? '—' : u.avg_pct + '%')))) : el('p', { class: 'muted' }, 'No finished tests yet.'))
      ];
    }

    /* ---------- users ---------- */
    async function users() {
      const q = el('input', { type: 'search', class: 'adsearch', placeholder: 'Search email, name, nickname or role (student, parent, marker, admin)', value: A.userQ, id: 'adUserQ' });
      const out = el('div', {}); const detail = el('div', { id: 'adUserDetail' });
      const load = async () => {
        A.userQ = q.value.trim(); const rows = await B().users(A.userQ, 100, 0); out.innerHTML = '';
        out.append(el('p', { class: 'muted' }, `${rows.length ? rows[0].total : 0} account(s)${rows.length === 100 ? ' – showing the newest 100' : ''}`),
          table(['Email', 'Name', 'Role', 'Learners', 'Created', 'Status', ''], rows.map(u => el('tr', { class: A.userId === u.id ? 'on' : '' }, el('td', {}, u.email || '—'), el('td', {}, u.display_name || ''), el('td', {}, tag(u.role, 'r-' + u.role)),
            el('td', {}, String(u.learners)), el('td', {}, day(u.created_at)), el('td', {}, u.disabled ? tag('switched off', 'd-VH') : tag('active', 'd-M')),
            el('td', {}, el('button', { class: 'btn small', type: 'button', onclick: async () => { A.userId = u.id; await showUser(detail); detail.scrollIntoView({ behavior: 'smooth' }); } }, 'Open'))))));
      };
      q.addEventListener('keydown', e => { if (e.key === 'Enter') load(); });
      await load(); if (A.userId) await showUser(detail).catch(() => { });
      return [el('div', { class: 'btnrow' }, q, el('button', { class: 'btn small primary', type: 'button', id: 'adUserGo', onclick: load }, 'Search')), out, detail];
    }
    async function showUser(host) {
      const d = await B().user(A.userId); const p = d.profile; host.innerHTML = '';
      const roleSel = el('select', { id: 'adRole' }, ...['student', 'parent', 'marker', 'admin'].map(r => el('option', { value: r, selected: r === p.role }, r)));
      const card = el('section', { class: 'card aduser' }, el('div', { class: 'adhead' }, el('div', {}, el('span', { class: 'eyebrow' }, 'ACCOUNT'), el('h2', { style: 'margin:0' }, p.display_name || p.email), el('p', { class: 'muted', style: 'margin:0' }, `${p.email || ''} · ${p.country || ''} · created ${day(p.created_at)}${p.last_sign_in_at ? ' · last sign-in ' + day(p.last_sign_in_at) : ''}`)),
          p.disabled ? tag('switched off', 'd-VH') : tag('active', 'd-M')),
        el('div', { class: 'btnrow' }, el('label', {}, 'Role ', roleSel), el('button', { class: 'btn small', type: 'button', id: 'adSaveRole', onclick: () => busy(() => B().setRole(p.id, roleSel.value), 'Role saved').then(() => showUser(host)) }, 'Save role'),
          el('button', { class: 'btn small ' + (p.disabled ? 'primary' : 'ghost'), type: 'button', id: 'adDisable', onclick: () => modal(p.disabled ? 'Switch this account back on?' : 'Switch this account off?', p.disabled ? 'The person can sign in again.' : 'The person is signed out and cannot sign in until you switch the account back on. Nothing is deleted.',
            [{ t: 'Cancel', cls: 'ghost' }, { t: p.disabled ? 'Switch on' : 'Switch off', cls: 'primary', on: () => busy(() => B().setDisabled(p.id, !p.disabled), 'Saved').then(() => showUser(host)) }]) }, p.disabled ? 'Switch account on' : 'Switch account off')),
        d.subscription ? el('p', { class: 'muted' }, `Subscription: ${d.subscription.status}${d.subscription.plan ? ' · ' + d.subscription.plan : ''}`) : null);
      (d.learners || []).forEach(x => {
        const l = x.learner; const enrolled = g => (x.enrolments || []).some(e => e.stage === g);
        const lc = el('div', { class: 'adlearner' }, el('h3', {}, `${l.nickname}`, el('small', { class: 'muted' }, ` · sign-up stage ${l.stage}${l.birth_year ? ' · born ' + l.birth_year : ''}${l.parent_email ? ' · parent ' + l.parent_email : ''}`)),
          el('div', { class: 'btnrow' }, el('label', { class: 'adtoggle' }, (() => { const c = el('input', { type: 'checkbox', checked: x.tester, id: 'adTester-' + l.id }); c.onchange = () => busy(() => B().setTester(l.id, c.checked), c.checked ? 'Tester on – locks skipped' : 'Tester off'); return c; })(), ' Tester (skips locks)'),
            (() => { const s = el('select', { id: 'adStage-' + l.id }, ...[1, 2, 3, 4, 5, 6, 7, 8, 9].map(n => el('option', { value: n, selected: n === (l.stage || 7) }, 'Stage ' + n)));
              return el('label', { class: 'adtoggle' }, 'Stage level ', s, el('button', { class: 'btn small', type: 'button', onclick: () => busy(() => B().setLearnerStage(l.id, Number(s.value)), 'Stage level saved') }, 'Save')); })(),
            ...COURSES.map(([g, n]) => el('label', { class: 'adtoggle' }, (() => { const c = el('input', { type: 'checkbox', checked: enrolled(g) }); c.onchange = () => busy(() => B().setEnrolment(l.id, g, c.checked), c.checked ? `Enrolled in ${n}` : `Removed from ${n}`); return c; })(), ' ' + n))),
          el('h4', {}, `Unit results (${(x.results || []).length})`),
          (x.results || []).length ? el('div', { class: 'adchips' }, ...x.results.map(r => tag(`${unitLabel(r.unit).replace(/^.*· /, unitCourse(r.unit) >= 20 ? 'E' + (unitCourse(r.unit) - 20) + ' ' : unitCourse(r.unit) >= 10 ? 'M' + (unitCourse(r.unit) - 10) + ' ' : 'S' + unitCourse(r.unit) + ' ')}: ${num(r.pct)}%`, 'd-M'))) : el('p', { class: 'muted' }, 'No unit passed yet.'),
          el('h4', {}, `Test attempts (${(x.attempts || []).length})`),
          (x.attempts || []).length ? attemptTable(x.attempts.map(a => ({ ...a, nickname: l.nickname })), () => showUser(host)) : el('p', { class: 'muted' }, 'No tests taken.'),
          el('h4', {}, 'Saved progress'),
          (x.progress || []).length ? table(['Unit', 'Questions done', ''], x.progress.map(g => el('tr', {}, el('td', {}, unitLabel(g.unit)), el('td', {}, String(g.items)),
            el('td', {}, el('button', { class: 'btn small ghost', type: 'button', onclick: () => modal('Reset this progress?', `All saved progress of ${l.nickname} in ${unitLabel(g.unit)} is deleted. Test attempts are kept.`, [{ t: 'Cancel', cls: 'ghost' }, { t: 'Reset', cls: 'primary', on: () => busy(() => B().resetProgress(l.id, g.unit), 'Progress reset').then(() => showUser(host)) }]) }, 'Reset'))))) : el('p', { class: 'muted' }, 'Nothing saved yet.'),
          (x.certificates || []).length ? el('p', {}, '🎓 Certificates: ', ...(x.certificates.map(c => tag(c.code, 'd-M')))) : null);
        card.append(lc);
      });
      if (!(d.learners || []).length) card.append(el('p', { class: 'muted' }, 'This account has no learner profile.'));
      host.append(card);
    }

    /* ---------- exams ---------- */
    function attemptTable(rows, after) {
      return table(['Date', 'Learner', 'Unit / exam', 'Paper', 'Status', 'Score', 'Flags', ''], rows.map(a => el('tr', {}, el('td', {}, day(a.created_at)), el('td', {}, a.nickname || '', a.email ? el('br') : null, a.email ? el('small', { class: 'muted' }, a.email) : null),
        el('td', {}, unitLabel(a.unit)), el('td', {}, `${a.form}${a.n ? ' · #' + a.n : ''}`), el('td', {}, a.status === 'pending' ? tag('waiting for marking', 'd-H') : a.passed ? tag('passed', 'd-M') : tag('not passed', 'd-VH')),
        el('td', {}, a.score == null ? '—' : `${num(a.score)} · ${num(a.pct)}%`), el('td', {}, [a.leaves ? `left room ×${a.leaves}` : '', a.overtime ? 'over time' : ''].filter(Boolean).join(', ') || '—'),
        el('td', { class: 'nowrap' }, el('button', { class: 'btn small', type: 'button', title: 'Mark again with the current answer keys', onclick: () => busy(() => B().regrade(a.id)).then(r => { const x = r.result || r; toast(x.changed ? `Re-marked: ${num(x.from)} → ${num(x.to)}` : 'Re-marked: no change'); after && after(); }) }, 'Re-mark'),
          el('button', { class: 'btn small ghost', type: 'button', onclick: () => modal('Delete this attempt?', 'The attempt and any unit result it earned are removed, so the learner can sit the paper again. This cannot be undone.', [{ t: 'Cancel', cls: 'ghost' }, { t: 'Delete attempt', cls: 'primary', on: () => busy(() => B().voidAttempt(a.id), 'Attempt deleted').then(() => after && after()) }]) }, 'Delete')))));
    }
    async function unitsOf(g) { const r = await fetch(`content/stage${g}.json`); const ix = r.ok ? await r.json() : { units: [] }; const list = ix.units.map(u => ({ id: `stage${g}-unit${String(u.n).padStart(2, '0')}`, t: `Unit ${u.n}: ${u.t}` })); if (ix.final) list.push({ id: `stage${g}-final`, t: 'End-of-year exam' }); if (ix.cp) list.push({ id: `stage${g}-cp`, t: 'Checkpoint papers' }); return list; }
    async function exams() {
      const cs = el('select', { id: 'adExamCourse' }, el('option', { value: '' }, 'All courses'), ...COURSES.map(([g, n]) => el('option', { value: g, selected: A.examCourse === g }, n)));
      const us = el('select', { id: 'adExamUnit' }, el('option', { value: '' }, 'All units and exams'));
      const ss = el('select', { id: 'adExamStatus' }, ...[['', 'Any status'], ['pending', 'Waiting for marking'], ['final', 'Marked']].map(([v, t]) => el('option', { value: v, selected: A.examStatus === v }, t)));
      const out = el('div', {});
      const fillUnits = async () => { us.innerHTML = ''; us.append(el('option', { value: '' }, 'All units and exams')); if (A.examCourse) (await unitsOf(A.examCourse)).forEach(u => us.append(el('option', { value: u.id, selected: A.examUnit === u.id }, u.t))); };
      const load = async () => { const filter = A.examUnit || (A.examCourse ? `stage${A.examCourse}` : ''); const rows = await B().attempts(filter, A.examStatus); out.innerHTML = '';
        out.append(el('p', { class: 'muted' }, `${rows.length} attempt(s)`), rows.length ? attemptTable(rows, load) : el('p', { class: 'muted' }, 'No attempts match.')); };
      cs.onchange = async () => { A.examCourse = cs.value ? +cs.value : 0; A.examUnit = ''; await fillUnits(); load(); };
      us.onchange = () => { A.examUnit = us.value; load(); }; ss.onchange = () => { A.examStatus = ss.value; load(); };
      await fillUnits(); await load();
      const regAll = el('button', { class: 'btn small', type: 'button', id: 'adRegradeUnit', onclick: () => { if (!A.examUnit) return toast('Choose one unit or exam first.'); modal('Re-mark every attempt?', `Every marked attempt of ${unitLabel(A.examUnit)} is marked again with the current answer keys (edited and withdrawn questions included). Teacher marks for written answers are kept.`,
        [{ t: 'Cancel', cls: 'ghost' }, { t: 'Re-mark all', cls: 'primary', on: () => busy(() => B().regradeUnit(A.examUnit)).then(r => { toast(`${r.attempts} attempt(s) checked, ${r.changed} changed`); load(); }) }]); } }, 'Re-mark all in this unit');
      return [el('div', { class: 'btnrow' }, cs, us, ss, regAll), out];
    }

    /* ---------- content: units, questions and the question editor ---------- */
    async function content() {
      const cs = el('select', { id: 'adCourse' }, ...COURSES.map(([g, n]) => el('option', { value: g, selected: A.course === g }, n)));
      cs.onchange = () => { A.course = +cs.value; A.unit = ''; render(); };
      const units = await unitsOf(A.course); const settings = await Backend.unitSettings(); const hid = u => (settings.find(s => s.unit === u) || {}).hidden;
      const list = table(['Unit / exam', 'Shown to learners', ''], units.map(u => el('tr', { class: A.unit === u.id ? 'on' : '' }, el('td', {}, u.t),
        el('td', {}, (() => { const c = el('input', { type: 'checkbox', checked: !hid(u.id), 'aria-label': 'Shown to learners' }); c.onchange = () => busy(() => B().setUnit(u.id, !c.checked, null), c.checked ? 'Unit shown to learners' : 'Unit hidden from learners'); return c; })()),
        el('td', {}, el('button', { class: 'btn small' + (A.unit === u.id ? ' primary' : ''), type: 'button', onclick: () => { A.unit = u.id; render(); } }, 'Questions')))));
      const kids = [el('div', { class: 'btnrow' }, el('label', {}, 'Course ', cs)), el('p', { class: 'muted' }, 'Hidden units show as “coming soon” and cannot be opened. Edits take effect for learners the next time they open the unit; tests are marked with the edited keys straight away.'), list];
      if (A.unit) kids.push(await questionList(A.unit));
      return kids;
    }
    async function loadUnitAll(unit) {
      const pub = await (await fetch(`content/${unit}.json`)).json();
      let keyed = null; try { keyed = await B().papers(unit); } catch (e) { keyed = null; }
      const rows = await B().overrides(unit); const ov = Object.fromEntries((rows || []).map(r => [r.question_id, r]));
      const items = [];
      (pub.sections || []).forEach(s => {
        (s.stops || []).forEach(x => x.q && items.push({ pool: 'Check / pause', sec: s.id, q: x.q, test: false }));
        ['req', 'prac', 'adv'].forEach(k => (s[k] || []).forEach(q => items.push({ pool: { req: 'Core', prac: 'Practice', adv: 'Advanced' }[k], sec: s.id, q, test: false })));
      });
      const papers = (keyed && keyed.papers) || pub.papers || pub.tests || {};
      Object.entries(papers).forEach(([k, list]) => (list || []).forEach(q => items.push({ pool: pub.papers ? `Paper ${k}` : `Unit Test ${k}`, sec: '', q, test: true, keyed: !!(keyed && keyed.papers) })));
      return { pub, items, ov };
    }
    async function questionList(unit) {
      const { items, ov } = await loadUnitAll(unit);
      const pools = ['all', ...new Set(items.map(i => i.pool))];
      const ps = el('select', { id: 'adPool' }, ...pools.map(p => el('option', { value: p, selected: A.pool === p }, p === 'all' ? 'All question pools' : p)));
      const qs = el('input', { type: 'search', class: 'adsearch', placeholder: 'Search id or wording', value: A.qFilter, id: 'adQ' });
      const out = el('div', {});
      const draw = (more) => { if (!more) A.show = 60; A.pool = ps.value; A.qFilter = qs.value.trim().toLowerCase(); out.innerHTML = '';
        const shown = items.filter(i => (A.pool === 'all' || i.pool === A.pool) && (!A.qFilter || i.q.id.toLowerCase().includes(A.qFilter) || String(i.q.prompt).toLowerCase().includes(A.qFilter) || A.qFilter === 'edited' && ov[i.q.id]));
        out.append(el('p', { class: 'muted' }, `${shown.length} of ${items.length} questions · ${Object.keys(ov).length} edited or withdrawn (type “edited” to list them)`),
          table(['Id', 'Pool', 'Type', 'Level', 'Question', 'State', ''], shown.slice(0, A.show).map(i => { const o = ov[i.q.id]; const q = o && o.key_patch ? Object.assign({}, i.q, o.key_patch) : i.q;
            return el('tr', {}, el('td', {}, el('code', {}, i.q.id)), el('td', {}, i.pool + (i.sec ? ' ' + i.sec : '')), el('td', {}, GradeCore.TYPE_VI[q.type] || q.type), el('td', {}, q.diff || ''),
              el('td', { class: 'adq' }, String(q.prompt || '').replace(/^\* Advanced\.\s*/, '').slice(0, 140)), el('td', {}, o ? (o.hidden ? tag(i.test ? 'withdrawn (full marks)' : 'hidden', 'd-VH') : tag('edited', 'd-H')) : ''),
              el('td', { class: 'nowrap' }, el('button', { class: 'btn small', type: 'button', onclick: () => editor(unit, i, o) }, 'Edit'),
                el('button', { class: 'btn small ghost', type: 'button', onclick: () => busy(() => B().saveQuestion(i.q.id, unit, i.test, !(o && o.hidden), o ? o.public_patch : null, o ? o.key_patch : null), o && o.hidden ? 'Question shown again' : (i.test ? 'Question withdrawn – everyone gets its marks' : 'Question hidden')).then(async () => { Core.dropCache && await Core.dropCache(); render(); }) }, o && o.hidden ? 'Show' : (i.test ? 'Withdraw' : 'Hide')))); })),
          shown.length > A.show ? el('button', { class: 'btn small', type: 'button', id: 'adMore', onclick: () => { A.show += 60; draw(true); } }, `Show more (${shown.length - A.show} left)`) : null);
      };
      ps.onchange = () => draw(); qs.addEventListener('input', () => { clearTimeout(qs._t); qs._t = setTimeout(() => draw(), 200); }); draw();
      return el('section', { class: 'card' }, el('h3', { style: 'margin-top:0' }, unitLabel(unit)), el('div', { class: 'btnrow' }, ps, qs), out);
    }

    // the question editor: a form for the common fields + the full question as JSON, with a live preview
    function editor(unit, item, o) {
      const base = item.q; let q = JSON.parse(JSON.stringify(o && o.key_patch ? Object.assign({}, base, o.key_patch) : base));
      const keyless = item.test && !item.keyed;
      const fields = el('div', { class: 'adform' }); const prev = el('div', { class: 'adprev' }); const json = el('textarea', { class: 'adjson', rows: 14, spellcheck: 'false', id: 'adJson' });
      const hidden = el('input', { type: 'checkbox', checked: !!(o && o.hidden) });
      const syncJson = () => { json.value = JSON.stringify(q, null, 2); };
      const text = (label, k, rows) => { const t = el(rows ? 'textarea' : 'input', { value: q[k] == null ? '' : String(q[k]), rows: rows || null, 'data-k': k }); if (rows) t.value = q[k] == null ? '' : String(q[k]); t.oninput = () => { if (t.value === '') delete q[k]; else q[k] = t.value; syncJson(); preview(); }; return el('label', {}, label, t); };
      const numf = (label, k) => { const t = el('input', { type: 'text', inputmode: 'decimal', value: q[k] == null ? '' : String(q[k]) }); t.oninput = () => { const v = GradeCore.parseNum(t.value); if (t.value === '') delete q[k]; else if (v != null) q[k] = v; syncJson(); preview(); }; return el('label', {}, label, t); };
      const drawFields = () => {
        fields.innerHTML = '';
        fields.append(el('div', { class: 'admeta' }, el('code', {}, q.id), tag(GradeCore.TYPE_VI[q.type] || q.type), item.test ? tag('test question', 'd-H') : tag(item.pool)),
          text('Question', 'prompt', 3));
        if (item.test || q.ctx) fields.append(text('Shared context (question stem)', 'ctx', 2));
        const lv = el('select', {}, ...['M', 'H', 'VH', 'E'].map(d => el('option', { value: d, selected: q.diff === d }, d))); lv.onchange = () => { q.diff = lv.value; syncJson(); };
        fields.append(el('div', { class: 'btnrow' }, el('label', {}, 'Level ', lv), q.pts != null ? numf('Marks', 'pts') : null));
        if (keyless) fields.append(el('div', { class: 'banner info' }, 'The answer key of this test question is kept on the server and could not be loaded. You can still change the wording or withdraw it.'));
        else if (q.type === 'num' || q.type === 'scale') fields.append(el('div', { class: 'btnrow' }, numf('Correct answer', 'answer'), text('Unit', 'unit'), numf('Tolerance (±)', 'tol')));
        else if (q.type === 'mcq' || q.type === 'multi') {
          const ob = el('div', { class: 'adopts' });
          const drawOpts = () => { ob.innerHTML = ''; (q.options || []).forEach((op, i) => { const t = el('input', { value: op.t, 'aria-label': 'Option ' + (i + 1) }); t.oninput = () => { op.t = t.value; syncJson(); preview(); };
            const ok = el('input', { type: q.type === 'mcq' ? 'radio' : 'checkbox', name: 'adok', checked: !!op.ok, 'aria-label': 'Correct' }); ok.onchange = () => { if (q.type === 'mcq') q.options.forEach(x => { x.ok = false; }); op.ok = ok.checked; syncJson(); preview(); };
            const fb = el('input', { value: op.fb || '', placeholder: 'Feedback when chosen' }); fb.oninput = () => { op.fb = fb.value; syncJson(); };
            const del = el('button', { class: 'btn small ghost', type: 'button', onclick: () => { q.options.splice(i, 1); drawOpts(); syncJson(); preview(); } }, '✕');
            ob.append(el('div', { class: 'adopt' }, ok, t, fb, del)); });
            ob.append(el('button', { class: 'btn small', type: 'button', onclick: () => { (q.options = q.options || []).push({ t: 'New option', ok: false, fb: '' }); drawOpts(); syncJson(); } }, '+ Option')); };
          drawOpts(); fields.append(el('b', {}, 'Options (tick the correct one' + (q.type === 'multi' ? 's' : '') + ')'), ob);
        } else if (q.type === 'expr') fields.append(el('div', { class: 'btnrow' }, text('Model answer (typed form, e.g. 3x^2+2x-5)', 'expr'), text('Shown as', 'show'), text('Left side (y, x…)', 'lhs'), text('Letters used', 'vars')));
        else if (q.type === 'short') { const t = el('textarea', { rows: 2 }); t.value = (q.accept || []).join('\n'); t.oninput = () => { q.accept = t.value.split('\n').map(x => x.trim()).filter(Boolean); syncJson(); preview(); }; fields.append(el('label', {}, 'Accepted answers (one per line; /regex/ allowed)', t)); }
        else if (q.type === 'explain') fields.append(text('Model answer', 'model', 3), el('p', { class: 'muted' }, 'Edit the mark scheme (rubric) in the JSON below.'));
        else fields.append(el('p', { class: 'muted' }, 'Edit the answers of this question type in the JSON below.'));
        if (!keyless) fields.append(text('Worked solution / reason shown after answering', 'reason', 2), text('Hint', 'hint', 1));
      };
      const preview = () => { prev.innerHTML = ''; try { const host = el('div', {}); QE.practice(JSON.parse(JSON.stringify(q)), host, { rec: {}, seed: 'admin-preview', save: () => { }, onDone: () => { } }); prev.append(el('span', { class: 'eyebrow' }, 'PREVIEW – try answering'), host); window.AtomicMath && AtomicMath.typeset(prev); } catch (e) { prev.append(el('p', { class: 'err' }, 'Preview failed: ' + e.message)); } };
      json.oninput = () => { try { const v = JSON.parse(json.value); if (v.id !== base.id) throw new Error('the id cannot change'); q = v; json.classList.remove('bad'); drawFields(); preview(); } catch (e) { json.classList.add('bad'); } };
      drawFields(); syncJson(); preview();
      const body = el('div', { class: 'adeditor' }, el('div', { class: 'adcols' }, el('div', {}, fields, el('details', {}, el('summary', {}, 'Full question (JSON, advanced)'), json)), prev),
        el('label', { class: 'adtoggle' }, hidden, item.test ? ' Withdraw this question (every learner gets its marks)' : ' Hide this question from learners'));
      modal(`Edit ${q.id}`, body, [
        o ? { t: 'Undo all changes', cls: 'ghost', on: () => busy(() => B().resetQuestion(q.id, unit), 'Back to the original question').then(async () => { Core.dropCache && await Core.dropCache(); render(); }) } : null,
        { t: 'Cancel', cls: 'ghost' },
        { t: 'Save', cls: 'primary', on: async () => {
          if (json.classList.contains('bad')) { toast('Fix the JSON first.'); return true; }
          const full = JSON.parse(JSON.stringify(q));
          if (!keyless) { const chk = checkKey(full); if (chk) { toast(chk); return true; } }
          let pub, key;
          if (item.test) { pub = GradeCore.stripKeys(full); delete pub.id; key = keyless ? null : full; if (keyless) { pub = { prompt: full.prompt, ctx: full.ctx }; } }
          else { pub = full; key = full; }
          await busy(() => B().saveQuestion(full.id, unit, item.test, hidden.checked, pub, key), 'Question saved');
          Core.dropCache && await Core.dropCache();
          if (item.test) modal('Re-mark finished attempts?', 'Learners who already sat this paper keep their old marks until you re-mark them.', [{ t: 'Not now', cls: 'ghost' }, { t: 'Re-mark all', cls: 'primary', on: () => busy(() => B().regradeUnit(unit)).then(r => toast(`${r.attempts} checked, ${r.changed} changed`)) }]);
          render();
        } }
      ].filter(Boolean));
      document.querySelector('.modal') && document.querySelector('.modal').classList.add('wide');
    }
    // the edited question must still mark its own model answer as right
    function checkKey(q) {
      try {
        let ans = null;
        switch (q.type) {
          case 'mcq': if ((q.options || []).filter(o => o.ok).length !== 1) return 'Tick exactly one correct option.'; ans = q.options.findIndex(o => o.ok); break;
          case 'multi': if (!(q.options || []).some(o => o.ok)) return 'Tick at least one correct option.'; ans = q.options.map((o, i) => (o.ok ? i : -1)).filter(i => i >= 0); break;
          case 'num': case 'scale': if (q.answer == null || !isFinite(q.answer)) return 'Enter the correct answer as a number.'; ans = { v: String(q.answer), u: q.unit }; break;
          case 'expr': if (!q.expr) return 'Enter the model answer.'; ans = q.expr; break;
          case 'short': if (!(q.accept || []).length) return 'Add at least one accepted answer.'; return null;
          default: return null;
        }
        const g = GradeCore.grade(q, ans); return g && g.ok ? null : 'The model answer is not marked correct – check the answer fields.';
      } catch (e) { return 'This question cannot be checked: ' + e.message; }
    }

    /* ---------- reports ---------- */
    async function reports() {
      const r = await Backend.reports();
      if (!r.length) return el('p', { class: 'muted' }, 'No reports from learners yet.');
      return table(['Date', 'Kind', 'Unit', 'Question', 'Message', 'Status'], r.map(x => { const s = el('select', {}, ...['open', 'fixed', 'closed'].map(v => el('option', { value: v, selected: x.status === v }, v)));
        s.onchange = () => busy(() => B().setReport(x.id, s.value), 'Report updated');
        return el('tr', {}, el('td', {}, day(x.created_at)), el('td', {}, tag(String(x.kind).replace('_', ' '))), el('td', {}, x.unit ? unitLabel(x.unit) : '—'),
          el('td', {}, x.question_id ? el('button', { class: 'btn small ghost', type: 'button', onclick: () => { A.tab = 'content'; A.course = unitCourse(x.unit) || A.course; A.unit = x.unit || ''; A.qFilter = String(x.question_id).toLowerCase(); A.pool = 'all'; render(); } }, x.question_id) : '—'),
          el('td', { class: 'adq' }, x.message), el('td', {}, s)); }));
    }

    /* ---------- announcements ---------- */
    async function news() {
      const list = await B().allAnnouncements(); const road = B().roadmap ? await B().roadmap() : [];
      const t = el('input', { placeholder: 'Title', id: 'adNewsTitle', maxlength: 120 }); const b = el('textarea', { rows: 3, placeholder: 'Message (optional)', id: 'adNewsBody', maxlength: 1000 });
      const au = el('select', { id: 'adNewsAud' }, el('option', { value: 'all' }, 'Everyone'), ...COURSES.map(([g, n]) => el('option', { value: String(g) }, n)));
      const lv = el('select', {}, el('option', { value: 'info' }, 'Information'), el('option', { value: 'warn' }, 'Important'));
      return [el('section', { class: 'card' }, el('h3', { style: 'margin-top:0' }, 'New announcement'), el('p', { class: 'muted' }, 'Shown as a banner on learners’ dashboards until you switch it off.'), t, b,
        el('div', { class: 'btnrow' }, el('label', {}, 'Who sees it ', au), el('label', {}, 'Style ', lv), el('button', { class: 'btn small primary', type: 'button', id: 'adNewsGo', onclick: () => { if (t.value.trim().length < 2) return toast('Add a title.'); busy(() => B().announce(t.value.trim(), b.value.trim(), au.value, lv.value), 'Announcement published').then(render); } }, 'Publish'))),
        list.length ? table(['Date', 'Title', 'Who', 'Shown'], list.map(x => el('tr', {}, el('td', {}, day(x.created_at)), el('td', {}, el('b', {}, x.title), x.body ? el('br') : null, x.body ? el('small', { class: 'muted' }, x.body) : null),
          el('td', {}, x.audience === 'all' ? 'Everyone' : courseName(+x.audience)), el('td', {}, (() => { const c = el('input', { type: 'checkbox', checked: x.active }); c.onchange = () => busy(() => B().setAnnouncement(x.id, c.checked), c.checked ? 'Shown' : 'Hidden'); return c; })())))) : el('p', { class: 'muted' }, 'No announcements yet.'),
        roadmapEditor(road)];
    }
    // roadmap on the public News page (#news): what is coming, being built, or just released
    const RSTATUS = [['planned', 'Planned'], ['building', 'Being built'], ['released', 'Released']];
    function roadmapEditor(road) {
      const form = (x = {}) => {
        const ti = el('input', { placeholder: 'Feature title', maxlength: 120, value: x.title || '', class: 'rmTitle' }), bo = el('textarea', { rows: 2, maxlength: 1000, placeholder: 'One or two sentences for learners and parents' }); bo.value = x.body || '';
        const stt = el('select', {}, ...RSTATUS.map(([v, n]) => el('option', { value: v, selected: v === (x.status || 'planned') }, n)));
        const tg = el('input', { placeholder: 'When, e.g. December 2026', maxlength: 40, value: x.target || '' }), tag = el('input', { placeholder: 'Area, e.g. Mathematics', maxlength: 40, value: x.tag || '' });
        const so = el('input', { type: 'number', value: x.sort != null ? x.sort : (road.length + 1) * 10, style: 'width:80px' }), pub = el('input', { type: 'checkbox', checked: x.published !== false });
        const save = () => { if (ti.value.trim().length < 2) return toast('Add a title.'); busy(() => B().saveRoadmap({ id: x.id, title: ti.value.trim(), body: bo.value.trim(), status: stt.value, target: tg.value.trim(), tag: tag.value.trim(), sort: Number(so.value) || 0, published: pub.checked }), 'Roadmap saved').then(render); };
        return el('div', { class: 'adrm' + (x.id ? '' : ' new'), 'data-id': x.id || '' }, ti, bo, el('div', { class: 'btnrow' }, el('label', {}, 'Status ', stt), tg, tag, el('label', {}, 'Order ', so), el('label', { class: 'adtoggle' }, pub, ' Published'),
          el('button', { class: 'btn small primary', type: 'button', onclick: save }, x.id ? 'Save' : 'Add to roadmap'),
          x.id ? el('button', { class: 'btn small ghost', type: 'button', onclick: () => { if (confirm('Delete this roadmap item?')) busy(() => B().deleteRoadmap(x.id), 'Deleted').then(render); } }, 'Delete') : null));
      };
      return el('section', { class: 'card', id: 'adRoadmap' }, el('h3', { style: 'margin-top:0' }, 'Roadmap on the News page'), el('p', { class: 'muted' }, 'Learners and parents see these on the public News page (#news), grouped as Being built, Planned and Released.'),
        form(), ...road.map(x => form(x)));
    }

    /* ---------- settings ---------- */
    async function settings() {
      const s = await B().settings(); const cfg = window.ATOMIC_CONFIG || {};
      const mp = el('input', { type: 'checkbox', checked: s.mock_payments === 'on', id: 'adMockPay' }); mp.onchange = () => busy(() => B().setSetting('mock_payments', mp.checked ? 'on' : 'off'), mp.checked ? 'Test checkout switched on' : 'Test checkout switched off');
      return el('section', { class: 'card' }, el('h3', { style: 'margin-top:0' }, 'Settings'),
        el('label', { class: 'adtoggle' }, mp, ' Test checkout (learners can enrol in other courses without paying)'),
        el('p', { class: 'muted' }, `Data: ${Backend.mode === 'live' ? 'live database' : 'preview (this browser only)'} · Billing: ${cfg.billing || 'off'} · Server: ${cfg.apiBase || '/api'}`),
        el('p', { class: 'muted' }, 'Payment keys, email and other secrets are set in the hosting dashboards and are never shown here.'));
    }

    /* ---------- page errors reported by learners' browsers ---------- */
    async function errors() {
      const rows = await B().errors();
      if (!rows.length) return el('section', { class: 'card' }, el('h3', { style: 'margin-top:0' }, 'Page errors'), el('p', { class: 'muted' }, 'No page errors reported. Errors that happen in a learner\'s browser appear here (kept for 90 days).'));
      const byMsg = {}; rows.forEach(x => { byMsg[x.msg] = (byMsg[x.msg] || 0) + 1; });
      const top = Object.entries(byMsg).sort((a, b) => b[1] - a[1]).slice(0, 5);
      return [el('section', { class: 'card' }, el('h3', { style: 'margin-top:0' }, 'Most common'), el('ul', {}, ...top.map(([m, c]) => el('li', {}, tag(c + '×'), ' ', el('code', {}, m))))),
        table(['When', 'Who', 'Error', 'Where', 'Page'], rows.map(x => el('tr', {}, el('td', {}, day(x.at)), el('td', {}, x.email || 'guest'), el('td', { class: 'adq' }, x.msg), el('td', {}, el('code', {}, (x.src || '') + (x.line ? ':' + x.line : ''))), el('td', {}, el('code', {}, x.route || '')))))];
    }

    /* ---------- audit log ---------- */
    async function audit() {
      const rows = await B().audit();
      if (!rows.length) return el('p', { class: 'muted' }, 'No admin actions yet.');
      return table(['When', 'Who', 'Action', 'Target', 'Details'], rows.map(x => el('tr', {}, el('td', {}, day(x.at)), el('td', {}, x.actor_email || '—'), el('td', {}, tag(String(x.action).replace(/_/g, ' '))), el('td', {}, el('code', {}, String(x.target || ''))), el('td', { class: 'adq' }, Object.keys(x.detail || {}).length ? JSON.stringify(x.detail) : ''))));
    }

    return view;
  };
})();
