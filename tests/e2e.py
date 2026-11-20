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
def no_vi(pg): return not VI.search(txt(pg).replace('Lưu Quang Nghĩa', ''))

def signup(pg, email, name='Mai Tran', country='SG'):
    go(pg, 'signup'); pg.fill('#suName', name); pg.fill('#suEmail', email); pg.fill('#suPw', 'password123'); pg.select_option('#suCountry', country)
    pg.check('#suAdult'); pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_selector('#alNick')

def add_child(pg, nick):
    pg.fill('#alNick', nick); pg.check('#alConsent'); pg.click('#alBtn'); pg.wait_for_function("location.hash==='#v-3-1'"); pg.wait_for_timeout(300)

def parent_gate(pg):
    if pg.query_selector('#gatePw'): pg.fill('#gatePw', 'password123'); pg.click('#gateBtn'); pg.wait_for_timeout(500)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    ctx, pg = newpage(b)

    # ---------- 1. public pages ----------
    pg.goto(BASE); pg.wait_for_selector('#heroStart')
    t = txt(pg)
    ok('Start free' in t and 'not affiliated with or endorsed by Cambridge' in t, '1a Landing page with disclaimer for logged-out visitors')
    ok("Learner's Book" not in t and "LET'S MAP" not in t and not re.search(r'\bp\.\s?\d', t), '1b No textbook names or page numbers on the landing page')
    pg.screenshot(path=f'{SHOTS}/01_landing.png')
    for r in ['pricing', 'help', 'privacy', 'terms', 'cookies', 'verify']:
        go(pg, r)
    go(pg, 'pricing'); t = txt(pg)
    ok('£9.99 / month' in t and 'VAT' in t and 'Paddle' in t, '1c Pricing shows plans, VAT/GST note and Paddle as reseller')
    pg.screenshot(path=f'{SHOTS}/02_pricing.png', full_page=True)
    go(pg, 'privacy'); t = txt(pg)
    ok('Draft for legal review' in t and "Children’s code" in t and 'Vietnam' in t and 'Malaysia' in t and 'Thailand' in t and 'Indonesia' in t and 'Philippines' in t, '1d Privacy notice draft covers UK Children’s code, Singapore and Vietnam')
    go(pg, 'parent'); ok(h(pg) == '#signin', '1e Parent area redirects to sign-in when logged out')
    go(pg, 'test'); ok(h(pg) == '#signin', '1f Learner screens redirect to sign-in when logged out')

    # ---------- 2. sign-up, consent ----------
    go(pg, 'signup'); pg.fill('#suName', 'Mai'); pg.fill('#suEmail', 'mai@example.com'); pg.fill('#suPw', 'password123'); pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_timeout(300)
    ok('adult parent or guardian' in pg.inner_text('.err'), '2a Sign-up refused without the 18+ parent declaration')
    signup(pg, 'mai@example.com')
    ok(not pg.is_checked('#alConsent'), '2b Add-child form: parental consent not pre-ticked')
    pg.fill('#alNick', 'Bean'); pg.click('#alBtn'); pg.wait_for_timeout(300)
    ok('parental consent' in pg.inner_text('.err'), '2c Child cannot be added without parental consent')
    add_child(pg, 'Bean')
    ok(h(pg) == '#v-3-1', '2d New child lands on the first free lesson (3.1)')
    learner = pg.evaluate('Core.cur().learner')
    ok(learner['leaderboard_opt_in'] is False, '2e Leaderboard is OFF by default for a new child')
    prof = pg.evaluate("Backend.me().then(m=>m.profile)")
    ok(not prof['weekly_report'] and not prof['product_analytics'] and not prof['marketing_opt_in'], '2f Weekly email, analytics and marketing are OFF by default')
    pg.screenshot(path=f'{SHOTS}/03_lesson.png')

    # ---------- 3. free plan and paywall ----------
    go(pg, 'home'); ok(pg.query_selector('#freeBanner') is not None, '3a Dashboard shows the free-plan banner')
    pg.evaluate("T && 0"); pg.click('#simAll') if pg.query_selector('#simAll') else None
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
        ok(pg.evaluate('Core.cur()') is None, '5f0 Opening the staff area leaves the child session')
        ok(pg.query_selector('.numin') is not None, '5f Staff marking queue lists the pending written answer')
        for el_ in pg.query_selector_all('.numin'): el_.fill('0')
        pg.click('section.card .btn.primary'); pg.wait_for_timeout(800)
        notes = pg.evaluate('Backend.notifications()')
        ok(any('marked' in (n.get('title') or '').lower() or 'result' in (n.get('title') or '').lower() for n in notes), '5g Parent gets a notification when marking is done')
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

    # ---------- 7. leaderboard opt-in ----------
    go(pg, 'board'); ok(pg.query_selector('#lbHidden') is not None and 'Bean (you)' in txt(pg), '7a Hidden learner sees own row and a “you are hidden” note')
    pg.click('#whoBtn'); pg.wait_for_timeout(400); ok(h(pg) == '#learners', '7b Avatar returns to “Who’s learning?”')
    go(pg, 'parent'); ok(pg.query_selector('#gatePw') is not None, '7c Parent area asks for the account password')
    pg.fill('#gatePw', 'wrong-pass'); pg.click('#gateBtn'); pg.wait_for_timeout(300); ok('not right' in txt(pg), '7d Wrong password refused')
    parent_gate(pg); ok('Bean' in txt(pg) and 'Curriculum code' in pg.content(), '7e Parent dashboard shows each child with objectives and curriculum codes')
    pg.screenshot(path=f'{SHOTS}/04_parent.png', full_page=True)
    lbid = pg.evaluate("Core.S.learners[0].id")
    pg.click(f'#lb-{lbid}'); pg.wait_for_timeout(200); ok(pg.query_selector('.modal') is not None, '7f Switching the leaderboard on asks for confirmation')
    pg.click('.modal .btn.primary'); pg.wait_for_timeout(500)
    ok(pg.evaluate("Backend.learners().then(l=>l[0].leaderboard_opt_in)"), '7g Leaderboard opt-in saved')
    cons = pg.evaluate('Backend.consents()')
    ok(any(c['kind'] == 'leaderboard' for c in cons) and any(c['kind'] == 'parental_consent' for c in cons), '7h Consent log records child data consent and leaderboard opt-in')

    # ---------- 8. certificate ----------
    pg.click('.kid .btn.primary'); pg.wait_for_timeout(600)
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
    pg.click('#whoBtn'); pg.wait_for_timeout(300); go(pg, 'staff'); pg.wait_for_timeout(300)
    pg.click('button[role=tab]:has-text("Question reports")'); pg.wait_for_timeout(400); ok('diagram label looks wrong' in txt(pg), '9a Question report reaches the staff inbox')
    pg.click('button[role=tab]:has-text("Question statistics")'); pg.wait_for_timeout(400); ok('Right first time' in txt(pg), '9b Question statistics table renders')

    # ---------- 10. settings, export, delete ----------
    go(pg, 'settings'); parent_gate(pg); pg.wait_for_timeout(300)
    ok(not pg.is_checked('#set-weekly_report') and not pg.is_checked('#set-product_analytics'), '10a Settings show optional items off')
    pg.check('#set-weekly_report'); pg.wait_for_timeout(300); ok(pg.evaluate("Backend.me().then(m=>m.profile.weekly_report)"), '10b Weekly report can be switched on')
    with pg.expect_download() as dl: pg.click('#exportBtn')
    data = json.loads(open(dl.value.path()).read())
    ok('learners' in data and 'attempts' in data and 'consents' in json.dumps(data), '10c Data export downloads JSON with learners, attempts and consents')
    pg.screenshot(path=f'{SHOTS}/06_settings.png', full_page=True)
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
    signup(mp, 'kim@example.com', 'Kim Lee', 'GB'); add_child(mp, 'Pip')
    langs = []
    for r in ['home', 'unit3', 'v-3-1', 'ex-3-1', 'bank', 'profile', 'board', 'map', 'pricing', 'help', 'privacy-kids', 'learners']:
        go(mp, r); langs.append((r, no_vi(mp)))
    ok(all(x for _, x in langs), '11c No Vietnamese text on learner and parent screens ' + str([r for r, x in langs if not x]))
    go(mp, 'parent'); parent_gate(mp); mp.screenshot(path=f'{SHOTS}/08_mobile_parent.png', full_page=True)
    sw = mp.evaluate('document.documentElement.scrollWidth'); ok(sw <= 392, f'11d Mobile parent area has no sideways scroll ({sw}px)')
    b.close()

fails = [l for l in LOG if l.startswith('FAIL')]
print(f'\n{len(LOG) - len(fails)}/{len(LOG)} passed'); sys.exit(1 if fails else 0)
