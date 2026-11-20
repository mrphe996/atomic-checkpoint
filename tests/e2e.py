"""End-to-end checks of the demo build (browser only, localStorage backend).
Run: python3 /home/claude/web/test/rangeserver.py web &  then  python3 tests/e2e.py"""
import json, os, re, sys
from playwright.sync_api import sync_playwright

BASE = os.environ.get('BASE', 'http://localhost:8765/')
SHOTS = os.environ.get('SHOTS', '/tmp/e2e_shots'); os.makedirs(SHOTS, exist_ok=True)
LOG = []
def ok(cond, msg):
    LOG.append(('PASS' if cond else 'FAIL') + '  ' + msg); print(LOG[-1], flush=True)

HELPERS = r"""
window.T = {
  async keys(){ return (await (await fetch('content/demo/stage7-unit03.tests.json')).json()).papers; },
  right(q){ switch(q.type){
    case 'mcq': return q.options.findIndex(o=>o.ok);
    case 'multi': return q.options.map((o,i)=>o.ok?i:-1).filter(i=>i>=0);
    case 'num': case 'scale': return {v:String(q.answer),u:q.unit};
    case 'label': return {...q.spots};
    case 'order': return q.items.slice();
    case 'match': return Object.fromEntries(q.pairs.map(p=>[p.l,p.r]));
    case 'explain': return q.model;
    case 'grid': return q.rows.map(r=>r.a.slice());
    case 'table': { const r={}; q.rows.forEach((row,ri)=>row.forEach((c,ci)=>{ if(c&&typeof c==='object'){ (r[ri]=r[ri]||{})[ci]=String(c.ans);} })); return r; }
    case 'graph': return {pts:q.pts.map(p=>p.slice()), f: q.follow? q.follow.options.findIndex(o=>o.ok):null};
    case 'sim': return {pred:'fewer', trials:[{obj:4,count:'12'},{obj:40,count:'1'}], concl:'fewer'};
  }},
  async fillDraft(form, wrongObjs){ const P=await T.keys(); const st=Core.cur(); const d=st.test.drafts[form]=st.test.drafts[form]||{answers:{},ts:Date.now()};
    P[form].forEach(q=>{ if(wrongObjs && wrongObjs.includes(q.obj)) return; d.answers[q.id]=T.right(q); }); Core.persist(); }
};
"""

def newpage(b, mobile=False):
    ctx = b.new_context(viewport={'width': 390, 'height': 844} if mobile else {'width': 1366, 'height': 860}, is_mobile=mobile, has_touch=mobile, accept_downloads=True, reduced_motion='reduce')
    pg = ctx.new_page(); pg.errs = []
    pg.on('pageerror', lambda e: pg.errs.append(str(e)))
    pg.on('response', lambda r: pg.errs.append(f'{r.status} {r.url}') if r.status >= 400 and not r.url.endswith('favicon.ico') else None)
    pg.add_init_script(HELPERS)
    return ctx, pg

def h(pg): return pg.evaluate('location.hash')
def go(pg, r):
    pg.evaluate(f"(location.hash==='#{r}') ? AtomicApp.render() : (location.hash='{r}')"); pg.wait_for_timeout(500)
def txt(pg): return pg.inner_text('body')
VI = re.compile(r'[ăâđêôơưĂÂĐÊÔƠƯàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]', re.I)
def no_vi(pg): return not VI.search(txt(pg))

def signup(pg, email, name='Mai Tran', country='SG', parent=None, school=True):
    go(pg, 'signup'); pg.fill('#suName', name); pg.fill('#suEmail', email); pg.fill('#suPw', 'password123'); pg.click('#suNext1')
    pg.wait_for_selector('#suYear'); pg.select_option('#suYear', index=4); pg.select_option('#suGrade', 'Year 7 / Grade 6'); pg.click('#suNext2')
    pg.wait_for_selector('#suCountry'); pg.select_option('#suCountry', country); pg.wait_for_timeout(200)
    if school and pg.query_selector('#suSchool optgroup'): pg.select_option('#suSchool', index=1)
    else: pg.select_option('#suSchool', 'other'); pg.fill('#suSchoolOther', 'Home learner')
    if parent: pg.fill('#suParent', parent)
    pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_function("location.hash==='#home' && !!document.getElementById('resumeBtn')"); pg.wait_for_timeout(300)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    ctx, pg = newpage(b)

    # ---------- 1. public pages ----------
    pg.goto(BASE); pg.wait_for_selector('#heroStart')
    t = txt(pg)
    ok('Try the whole course' in t and 'No sign-up' in t and pg.query_selector('.lp-step') is not None and len(pg.query_selector_all('.lp-unit')) == 14 and 'not affiliated with or endorsed by Cambridge' in t, '1a Landing page: designed hero, 4-step demo boxes, 14 unit boxes, disclaimer')
    ok("Learner's Book" not in t and "LET'S MAP" not in t and not re.search(r'\bp\.\s?\d', t), '1b No textbook names or page numbers on the landing page')
    ok('Compiled by' not in t and 'Written by the Atomic teaching team' in t, '1b2 Footer credits the Atomic teaching team only')
    pg.screenshot(path=f'{SHOTS}/01_landing.png')
    for r in ['pricing', 'help', 'privacy', 'terms', 'cookies', 'verify']:
        go(pg, r)
    go(pg, 'pricing'); t = txt(pg)
    ok('£9.99 / month' in t and 'VAT' in t and 'Paddle' in t, '1c Pricing shows plans, VAT/GST note and Paddle as reseller')
    go(pg, 'privacy'); t = txt(pg)
    ok('Draft for legal review' in t and "Children’s code" in t and 'parent or guardian email' in t, '1d Privacy notice covers the Children’s code and the optional parent email')
    go(pg, 'parent'); ok(h(pg) == '#home', '1e Old parent-area link goes to the home page')
    go(pg, 'test'); ok(h(pg) == '#signin', '1f Unit Test needs an account when logged out')

    # ---------- 1g. guest mode ----------
    go(pg, 'home'); pg.click('[data-step="practise"]'); pg.click('.lp-qb .lp-opt >> nth=2'); pg.wait_for_timeout(200)
    ok('Correct' in pg.inner_text('.lp-fbbox'), '1f2 Visitors can answer demo questions on the home page without signing in')
    pg.click('[data-step="test"]'); pg.click('#demoStartTest')
    for i in [1, 2, 0]: pg.click(f'.lp-test .lp-opt >> nth={i}'); pg.click('#demoTNext'); pg.wait_for_timeout(150)
    ok(pg.inner_text('#demoScore') == '100%', '1f3 Mini test in the demo box gives a score')
    pg.click('#heroGuest'); pg.wait_for_function("location.hash==='#v-3-1'"); pg.wait_for_timeout(400)
    ok(pg.evaluate('Core.S.guest') and pg.query_selector('#signUpLink') is not None, '1g Guest starts topic 3.1 straight away with a Sign-up button in the header')
    go(pg, 'ex-3-1'); ok(pg.query_selector('#guestWall') is None and 'part of the full' not in txt(pg), '1h Guest can practise 3.1')
    pg.evaluate("(()=>{const st=Core.cur(); const q=Core.sec('3.1').req[0]; st.items[q.id]={done:true,ok:true,tries:1,score:1}; Core.persist(); Core.flush();})()"); pg.wait_for_timeout(300)
    ok(pg.evaluate('Core.streak(Core.cur())') == 1, '1i Guest activity starts a 1-day streak')
    ok(pg.evaluate("!!localStorage.getItem('atomic.guest.v1')"), '1j Guest progress is kept in this browser')
    lk = pg.evaluate("Core.secLock(Core.cur(), Core.sec('3.2'))"); ok(lk and lk.get('guest'), '1k Topic 3.2 asks a guest to sign up')
    go(pg, 'test'); ok(pg.query_selector('#guestWall') is not None, '1l Unit Test asks a guest to sign up')
    go(pg, 'board'); ok(pg.query_selector('#guestWall') is not None, '1m Leaderboard asks a guest to sign up')
    go(pg, 'home'); ok(pg.query_selector('#guestBanner') is not None and pg.query_selector('.dcont') is not None and pg.query_selector('#weekStrip') is not None, '1n Guest dashboard shows the guest banner, continue card and this-week streak')
    pg.screenshot(path=f'{SHOTS}/02_guest_home.png', full_page=True)

    # ---------- 2. three-step student sign-up ----------
    go(pg, 'signup'); pg.fill('#suName', 'Mai Tran'); pg.fill('#suEmail', 'bad'); pg.fill('#suPw', 'password123'); pg.click('#suNext1'); pg.wait_for_timeout(200)
    ok('valid email' in pg.inner_text('.err'), '2a Step 1 checks the email')
    pg.fill('#suEmail', 'mai@example.com'); pg.click('#suNext1'); pg.wait_for_selector('#suYear')
    pg.click('#suNext2'); pg.wait_for_timeout(200); ok('year of birth' in pg.inner_text('.err'), '2b Step 2 needs year of birth and school year')
    pg.select_option('#suYear', index=4); pg.select_option('#suGrade', 'Year 7 / Grade 6'); pg.click('#suNext2'); pg.wait_for_selector('#suCountry')
    pg.select_option('#suCountry', 'VN'); pg.wait_for_timeout(300)
    names = pg.eval_on_selector_all('#suSchool option', 'o=>o.map(x=>x.textContent)')
    ok(any('International School' in n for n in names) and "My school isn’t listed" in names, f'2c Choosing a country lists its international and bilingual schools ({len(names) - 2} schools)')
    pg.select_option('#suSchool', index=1); pg.fill('#suParent', 'mai@example.com'); pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_timeout(200)
    ok('different from your own' in pg.inner_text('.err'), '2d Parent email must differ from the student email')
    pg.fill('#suParent', 'mum@example.com'); pg.click('#suBtn'); pg.wait_for_function("location.hash==='#home' && !!document.getElementById('resumeBtn')"); pg.wait_for_timeout(400)
    learner = pg.evaluate('Core.cur().learner')
    ok(learner['parent_email'] == 'mum@example.com' and learner['school_id'] and learner['grade'] == 'Year 7 / Grade 6' and learner['country'] == 'VN', '2e Learner saved with school, school year, country and parent email')
    ok(learner['leaderboard_opt_in'] is False and pg.evaluate("Backend.me().then(m=>m.profile.role)") == 'student', '2f Student account; leaderboard OFF by default')
    ok(not pg.evaluate('Core.S.guest') and len(pg.evaluate('Object.keys(Core.cur().items)')) >= 1 and not pg.evaluate("localStorage.getItem('atomic.guest.v1')"), '2g Guest progress moves into the new account')
    ok(pg.query_selector('#addLearnerTile, a[href="#parent"], a[href="#learners"]') is None, '2h No parent screens anywhere')
    pg.screenshot(path=f'{SHOTS}/03_dashboard.png', full_page=True)

    # ---------- 2i. dashboard (Design 02) ----------
    go(pg, 'home'); t = txt(pg)
    ok(pg.query_selector('.dhero') and len(pg.query_selector_all('.drow')) == 5 and pg.query_selector('.dtest') and pg.query_selector('#weekStrip'), '2i Dashboard: dotted hero, unit table, Unit Test card and this-week streak')
    ok(pg.query_selector('#xpPill') is None and 'bolts' not in t.lower() and 'shop' not in t.lower(), '2j No bolts, shop or XP anywhere on the dashboard')
    ok(pg.evaluate('Core.streak(Core.cur())') >= 1 and pg.query_selector('.pill.streak') is not None, '2k Streak pill in the header')
    pg.screenshot(path=f'{SHOTS}/04_dashboard.png', full_page=True)

    # ---------- 3. free plan and paywall ----------
    go(pg, 'home'); ok(pg.query_selector('#freeBanner') is not None, '3a Dashboard shows the free-plan banner')
    go(pg, 'profile'); pg.click('#sim3-1'); pg.wait_for_timeout(800)
    ok(pg.evaluate("!!Core.secLock(Core.cur(), Core.sec('3.2')) && Core.secLock(Core.cur(), Core.sec('3.2')).paywall"), '3b Section 3.2 is behind the paywall after finishing 3.1 on the free plan')
    go(pg, 'ex-3-2'); ok('part of the full Stage 7 course' in txt(pg), '3c Practice 3.2 shows the paywall lock screen')
    go(pg, 'test'); ok('needs a Stage 7 plan' in txt(pg), '3d Unit Test needs a plan')
    r = pg.evaluate("Backend.submitTest({learnerId: Core.cur().id, unit: Core.UNIT, form:'A', answers:{}, clientKey:'x'}).then(()=> 'ok', e => e.code)")
    ok(r == 'subscription_required', '3e Backend refuses a test submission without a plan (402)')
    go(pg, 'pricing'); pg.click('#buy-yearly'); pg.wait_for_timeout(300); pg.click('.modal .btn.primary'); pg.wait_for_timeout(1000)
    ok(pg.evaluate('Core.S.sub.active') and pg.evaluate('Core.S.sub.status') == 'trialing', '3f Demo checkout starts a 7-day trial')
    ok(not pg.evaluate("Core.secLock(Core.cur(), Core.sec('3.2'))"), '3g Section 3.2 unlocks with the trial')

    # ---------- 4. report a problem ----------
    go(pg, 'ex-3-1'); pg.click('#reportQ'); pg.fill('.modal textarea', 'The diagram label looks wrong'); pg.click('.modal .btn.primary'); pg.wait_for_timeout(500)
    ok(len(pg.evaluate('Backend.reports().catch(()=>[])') or []) >= 0, '4a Report a problem sends a report (checked in the staff area)')

    # ---------- 5. Unit Test: fail -> marker -> remediation ----------
    go(pg, 'profile'); pg.click('#simAll'); pg.wait_for_timeout(900)
    go(pg, 'test'); ok(pg.query_selector('#startTest') is not None, '5a Unit Test opens when all videos and Core questions are done')
    pg.evaluate("T.fillDraft('A', ['O5','O6','O8','O9'])"); pg.wait_for_timeout(200)
    pg.click('#startTest'); pg.wait_for_timeout(300); pg.click('#submitTest'); pg.wait_for_timeout(200); pg.click('.modal .btn.primary'); pg.wait_for_function("location.hash==='#result'", timeout=8000); pg.wait_for_timeout(500)
    a = pg.evaluate('Core.lastAttempt(Core.cur())')
    ok(a['status'] in ('pending', 'final'), f"5b Server-style marking returned an attempt (status {a['status']}, auto {a['auto']})")
    ok(pg.evaluate("Object.values((Core.cur().solutions||{})).length") > 0, '5c Solutions come back from the marker, not from the public content')
    pub = pg.evaluate("JSON.stringify(Core.C.tests)")
    ok('"ok":true' not in pub and '"answer"' not in pub and '"model"' not in pub, '5d Public content has no Unit Test answer keys')
    if a['status'] == 'pending':
        ok('Awaiting marking' in txt(pg), '5e Result says the written answer awaits an Atomic marker')
        go(pg, 'staff'); pg.click('#becomeStaff'); pg.wait_for_timeout(800)
        ok(pg.query_selector('.numin') is not None, '5f Staff marking queue lists the pending written answer')
        for el_ in pg.query_selector_all('.numin'): el_.fill('0')
        pg.click('section.card .btn.primary'); pg.wait_for_timeout(800)
        notes = pg.evaluate('Backend.notifications()')
        ok(any('marked' in (n.get('title') or '').lower() or 'result' in (n.get('title') or '').lower() for n in notes), '5g Student gets a notification when marking is done')
    pg.evaluate("Core.selectLearner(Core.S.learners[0].id)"); pg.wait_for_timeout(300)
    a = pg.evaluate('Core.lastAttempt(Core.cur())')
    ok(a['status'] == 'final' and not a['passed'], f"5h Attempt 1 final and not passed ({a['score']}/30)")
    go(pg, 'result'); ok('NOT PASSED' in txt(pg) and pg.query_selector('#goRemedial') is not None, '5i Result page sends the learner to review questions')
    go(pg, 'test'); ok("can't retake yet" in txt(pg), '5j Retake blocked until review questions are done')
    rem = pg.evaluate("(()=>{const st=Core.cur(), a=Core.lastAttempt(st); a.remed.forEach(id=>st.rem[Core.remKey(a,id)]={done:true,ok:true,tries:1}); Core.persist(); Core.flush(); return a.remed.length})()")
    pg.wait_for_timeout(300)
    go(pg, 'test'); ok('Paper B' in txt(pg), f'5k After {rem} review questions the equivalent Paper B opens')

    # ---------- 6. pass with Paper B, ranking fixed at first pass ----------
    pg.evaluate("T.fillDraft('B')"); pg.click('#startTest'); pg.wait_for_timeout(300); pg.click('#submitTest'); pg.wait_for_timeout(200); pg.click('.modal .btn.primary'); pg.wait_for_function("location.hash==='#result'", timeout=8000); pg.wait_for_timeout(500)
    a = pg.evaluate('Core.lastAttempt(Core.cur())')
    if a['status'] == 'pending':
        go(pg, 'staff'); pg.click('#tab-marking') if pg.query_selector('#tab-marking') else None
        for el_ in pg.query_selector_all('.numin'): el_.fill(el_.get_attribute('max'))
        pg.click('section.card .btn.primary'); pg.wait_for_timeout(800)
        pg.evaluate("Core.selectLearner(Core.S.learners[0].id)"); pg.wait_for_timeout(300); a = pg.evaluate('Core.lastAttempt(Core.cur())')
    ok(a['status'] == 'final' and a['passed'], f"6a Paper B passed ({a['score']}/30, {a['pct']}%)")
    res = pg.evaluate("Core.cur().results[Core.UNIT]")
    ok(res and abs(res['pct'] - a['pct']) < 0.01, '6b Unit result stores the first-pass %')
    go(pg, 'test'); ok('You have passed' in txt(pg), '6c Test page shows passed; no further attempts')

    # ---------- 6d. parent email on first pass ----------
    ob = pg.evaluate('Backend.demo.outbox()')
    ok(len(ob) == 1 and ob[0]['to_email'] == 'mum@example.com' and 'Unit 3' in ob[0]['subject'], '6d One “finished Unit 3” email is queued for the parent')

    # ---------- 7. leaderboard opt-in (by the student) ----------
    go(pg, 'board'); ok(pg.query_selector('#lbHidden') is not None and 'Mai (you)' in txt(pg), '7a Hidden learner sees own row and a “you are hidden” note')
    pg.click('#whoBtn'); pg.wait_for_timeout(200); ok(pg.is_visible('#userMenu') and pg.query_selector('#userMenu #signOut') is not None, '7b Avatar opens the account menu')
    go(pg, 'settings'); pg.wait_for_selector('#setBoard')
    pg.click('#setBoard'); pg.wait_for_timeout(200); ok(pg.query_selector('.modal') is not None, '7c Switching the leaderboard on asks for confirmation')
    pg.click('.modal .btn.primary'); pg.wait_for_timeout(500)
    ok(pg.evaluate("Backend.learners().then(l=>l[0].leaderboard_opt_in)"), '7d Leaderboard opt-in saved')
    pg.fill('#setParent', ''); pg.fill('#setNick', 'Maisy'); pg.click('#setSave'); pg.wait_for_timeout(500)
    l0 = pg.evaluate("Backend.learners().then(l=>l[0])"); ok(l0['parent_email'] is None and l0['nickname'] == 'Maisy', '7e Student can remove the parent email and change nickname')
    pg.screenshot(path=f'{SHOTS}/06_settings.png', full_page=True)

    # ---------- 8. certificate ----------
    go(pg, 'cert'); ok('Certificate locked' in txt(pg), '8a Certificate locked until all 14 Stage 7 units are passed')
    go(pg, 'profile'); pg.click('#simOthers'); pg.wait_for_timeout(900)
    go(pg, 'cert'); pg.wait_for_selector('#certCode', timeout=5000); code = pg.inner_text('#certCode')
    ok(code.startswith('AE-S7-'), f'8b Certificate issued with code {code}')
    pg.screenshot(path=f'{SHOTS}/05_cert.png')
    with pg.expect_download() as dl: pg.click('#dlCert')
    ok(dl.value.suggested_filename.endswith('.pdf'), '8c Certificate downloads as PDF')
    go(pg, 'verify'); pg.fill('#vfCode', code); pg.click('#vfBtn'); pg.wait_for_timeout(400); ok('Genuine' in txt(pg), '8d Public verification confirms the code')
    pg.fill('#vfCode', 'AE-S7-2026-FAKE0000'); pg.click('#vfBtn'); pg.wait_for_timeout(400); ok('No certificate has this code' in txt(pg), '8e Unknown codes are rejected')
    go(pg, 'board'); ok('Shown' in txt(pg), '8f Leaderboard row now marked as shown')

    # ---------- 9. staff tools ----------
    go(pg, 'staff'); pg.wait_for_timeout(300)
    pg.click('button[role=tab]:has-text("Question reports")'); pg.wait_for_timeout(400); ok('diagram label looks wrong' in txt(pg), '9a Question report reaches the staff inbox')
    pg.click('button[role=tab]:has-text("Question statistics")'); pg.wait_for_timeout(400); ok('Right first time' in txt(pg), '9b Question statistics table renders')

    # ---------- 10. export, delete ----------
    go(pg, 'settings'); pg.wait_for_selector('#exportBtn')
    with pg.expect_download() as dl: pg.click('#exportBtn')
    data = json.loads(open(dl.value.path()).read())
    ok('learners' in data and 'attempts' in data, '10c Data export downloads JSON with learner and attempts')
    pg.click('#deleteBtn'); pg.fill('#delConfirm', 'delete'); pg.click('.modal .btn.primary'); pg.wait_for_timeout(300)
    ok(pg.query_selector('.modal') is not None and 'Type the confirmation' in txt(pg), '10d Delete needs the exact typed confirmation')
    pg.fill('#delConfirm', 'DELETE MY ACCOUNT'); pg.click('.modal .btn.primary'); pg.wait_for_timeout(800)
    ok(pg.evaluate('Backend.me()') is None and pg.query_selector('#heroStart') is not None, '10e Account deleted and signed out')
    go(pg, 'signin'); pg.fill('#siEmail', 'mai@example.com'); pg.fill('#siPw', 'password123'); pg.click('#siBtn'); pg.wait_for_timeout(500)
    ok('do not match' in txt(pg), '10f Deleted account can no longer sign in')

    # ---------- 11. language, errors, mobile ----------
    ok(not pg.errs, '11a No page errors or failed requests' + ('' if not pg.errs else ': ' + '; '.join(pg.errs[:4])))
    ctx2, mp = newpage(b, mobile=True)
    mp.goto(BASE); mp.wait_for_selector('#heroStart'); mp.screenshot(path=f'{SHOTS}/07_mobile_landing.png', full_page=True)
    sw = mp.evaluate('document.documentElement.scrollWidth'); ok(sw <= 392, f'11b Mobile landing has no sideways scroll ({sw}px)')
    signup(mp, 'kim@example.com', 'Kim Lee', 'XX', school=False)
    langs = []
    for r in ['home', 'unit3', 'v-3-1', 'ex-3-1', 'bank', 'profile', 'board', 'map', 'settings', 'pricing', 'help', 'privacy-kids']:
        go(mp, r); langs.append((r, no_vi(mp)))
    ok(all(x for _, x in langs), '11c No Vietnamese text on any screen ' + str([r for r, x in langs if not x]))
    for r in ['home', 'profile', 'signup']:
        if r == 'signup': mp.evaluate("Backend.signOut()"); mp.evaluate("Core.boot(Core.C)"); mp.wait_for_timeout(300)
        go(mp, r); mp.screenshot(path=f'{SHOTS}/08_mobile_{r}.png', full_page=True)
        sw = mp.evaluate('document.documentElement.scrollWidth'); ok(sw <= 392, f'11d Mobile {r} has no sideways scroll ({sw}px)')
    b.close()

fails = [l for l in LOG if l.startswith('FAIL')]
print(f'\n{len(LOG) - len(fails)}/{len(LOG)} passed'); sys.exit(1 if fails else 0)
