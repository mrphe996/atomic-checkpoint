"""Loading feedback, the course switcher, the Mathematics Stage 9 lock and the Question Bank filters.
Run with the default config (Mathematics Stage 9 locked): `node tools/write-config.mjs`."""
import os, sys
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
def signup(pg):
    pg.evaluate("location.hash='signup'"); pg.wait_for_timeout(300)
    pg.fill('#suName', 'Uma Interface'); pg.fill('#suEmail', 'ui@example.com'); pg.fill('#suPw', 'password123'); pg.click('#suNext1'); pg.wait_for_selector('#suYear')
    pg.select_option('#suYear', index=3); pg.select_option('#suGrade', index=2); pg.click('#suNext2'); pg.wait_for_selector('#suCountry')
    pg.select_option('#suCountry', 'SG'); pg.wait_for_timeout(200); pg.select_option('#suSchool', index=1); pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_function("location.hash==='#home'")
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(reduced_motion='reduce', viewport={'width': 1300, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    # a returning visitor who last studied Mathematics Stage 9 lands on Science while it is locked
    pg.goto(BASE + '?reset=1'); pg.wait_for_selector('#heroStart')
    pg.evaluate("localStorage.setItem('atomic.stage','19')"); pg.reload(); pg.wait_for_selector('#heroStart')
    ok(pg.evaluate("Core.STAGE") == 7 and pg.evaluate("Core.stageLocked(19)"), 'U1 Mathematics Stage 9 is locked; a saved stage 19 opens Stage 7')
    pg.wait_for_timeout(600); ok(pg.query_selector('#splash') is None, 'U2 The loading screen goes away once the page is drawn')
    ok(pg.evaluate("typeof Loading.overlay === 'function' && typeof Loading.skeleton === 'function'"), 'U3 Loading helpers are in place')
    signup(pg)
    sw = pg.query_selector('#stageSwitch')
    ok(sw is not None and len(pg.query_selector_all('#stageSwitch .sw')) == pg.evaluate('Core.STAGES.length') and pg.query_selector('#stageSwitch .sw.on[data-stage="7"]') is not None, 'U4 Dashboard shows the course switcher with Stage 7 current')
    ok(pg.query_selector('#stageSwitch .sw.locked[data-stage="19"]') is not None, 'U5 Mathematics Stage 9 shows as locked in the switcher')
    pg.evaluate("document.querySelector('#stageSwitch .sw[data-stage=\"19\"]').click()"); pg.wait_for_timeout(500)
    ok(pg.evaluate("Core.STAGE") == 7, 'U6 Clicking the locked course does not switch')
    pg.evaluate("location.hash='stage-19'"); pg.wait_for_timeout(700)
    ok(pg.query_selector('#stageSoon') is not None and pg.evaluate("Core.STAGE") == 7, 'U7 The Mathematics Stage 9 page says coming soon')
    pg.evaluate("location.hash='checkout-19'"); pg.wait_for_timeout(700)
    ok(pg.query_selector('#payBtn') is None, 'U8 Mathematics Stage 9 cannot be bought while locked')
    ok(pg.evaluate("Core.switchStage(19).then(()=>'open',e=>e.message)") == 'locked', 'U9 Switching to stage 19 in code is refused')
    pg.evaluate("location.hash='courses-maths'"); pg.wait_for_timeout(700)
    ok('COMING SOON' in pg.inner_text('#stageCard19, #course-maths-ls9') if pg.query_selector('#stageCard19, #course-maths-ls9') else 'coming soon' in pg.inner_text('.subjtabs').lower(), 'U10 The course list shows Mathematics as coming soon')
    # enrol Stage 8 and switch through the switcher
    pg.evaluate("location.hash='checkout-8'"); pg.wait_for_timeout(600); pg.click('#payBtn'); pg.wait_for_function("Core.STAGE===8", timeout=8000)
    pg.evaluate("location.hash='bank'"); pg.wait_for_timeout(900)
    pg.evaluate("document.querySelector('#stageSwitch .sw[data-stage=\"7\"]').click()"); pg.wait_for_function("Core.STAGE===7", timeout=8000); pg.wait_for_timeout(500)
    ok(pg.evaluate("location.hash") == '#bank' and pg.query_selector('#bankFilters') is not None, 'U11 Switching course keeps you on the Question Bank')
    # Question Bank filters
    n0 = int(pg.inner_text('#bankCount').split()[0])
    pg.select_option('#bf-diff', 'H'); pg.wait_for_timeout(250); n1 = int(pg.inner_text('#bankCount').split()[0])
    lab = pg.evaluate("[...document.querySelectorAll('#bf-diff option')].find(o=>o.value==='H').textContent")
    ok(0 < n1 < n0 and f'({n1})' in lab, f'U12 Difficulty filter narrows the list and shows its count ({n0} → {n1}, “{lab}”)')
    pg.select_option('#bf-tier', 'req'); pg.wait_for_timeout(250); n2 = int(pg.inner_text('#bankCount').split()[0])
    ok(n2 <= n1 and len(pg.query_selector_all('.qbpill')) == 2, 'U13 Filters combine and each shows as a removable pill')
    pg.click('.qbpill:has-text("Difficulty") button'); pg.wait_for_timeout(250)
    ok(len(pg.query_selector_all('.qbpill')) == 1 and pg.eval_on_selector('#bf-diff', 'e=>e.value') == 'all', 'U14 Removing a pill clears that filter')
    pg.fill('#bankSearch', 'zzzz-no-such-words'); pg.wait_for_timeout(500)
    ok(pg.inner_text('#bankCount').startswith('0') and pg.query_selector('.qbempty') is not None, 'U15 Live search with no match explains what to do')
    pg.click('#bankClear'); pg.wait_for_timeout(300)
    ok(int(pg.inner_text('#bankCount').split()[0]) == n0 and pg.eval_on_selector('#bankSearch', 'e=>e.value') == '', 'U16 Clear all restores every question')
    pg.select_option('#bankSort', 'hard'); pg.wait_for_timeout(250)
    first = pg.eval_on_selector('#bankTable .lbrow[data-q]', 'e=>e.dataset.q'); fd = pg.evaluate(f"(()=>{{const q=Core.C.sections.flatMap(s=>s.req.concat(s.prac,s.adv)).find(x=>x.id==='{first}');return q.diff}})()")
    ok(fd == 'VH' or not pg.evaluate("Core.C.sections.flatMap(s=>s.req.concat(s.prac,s.adv)).some(q=>q.diff==='VH')"), 'U17 Sorting hardest first puts a very hard question at the top')
    rows = len(pg.query_selector_all('#bankTable .lbrow[data-q]'))
    if pg.query_selector('#bankMore'): pg.click('#bankMore'); pg.wait_for_timeout(300)
    ok(rows <= 40 and len(pg.query_selector_all('#bankTable .lbrow[data-q]')) > rows or n0 <= 40, 'U18 Long lists load 40 at a time with Show more')
    pg.check('#bankTable .lbrow[data-q] input >> nth=0'); pg.check('#bankTable .lbrow[data-q] input >> nth=1'); pg.wait_for_timeout(150)
    ok('(2)' in pg.inner_text('#bankPick') and not pg.eval_on_selector('#bankPick', 'e=>e.disabled'), 'U19 Ticking questions enables “Practise ticked (2)”')
    pg.click('#bankPick'); pg.wait_for_timeout(800)
    ok(pg.evaluate("location.hash") == '#drill', 'U20 Practise ticked opens a drill with the chosen questions')
    # mobile: the switcher scrolls and the filters can be folded
    pg.set_viewport_size({'width': 390, 'height': 800}); pg.evaluate("location.hash='bank'"); pg.wait_for_timeout(800)
    fold = pg.query_selector('.qbfold'); ok(fold is not None and fold.is_visible(), 'U21 On a phone the filters can be hidden')
    # Stage 7 practice opens in the full-screen practice room: leaving with Core questions left asks first, then lets the learner go
    pg.evaluate("(()=>{const st=Core.cur(); const s=Core.C.sections[0]; const vs=Core.vstate(st,s.id); vs.completed=true; s.stops.forEach(x=>vs.stops[x.id]={done:true,tries:1}); Core.persist();})()")
    pg.evaluate("location.hash='ex-1-1'"); pg.wait_for_timeout(900)
    room = pg.query_selector('.froom') is not None and pg.query_selector('#lv-req') is not None and pg.query_selector('#reportQ') is not None
    pg.evaluate("location.hash='home'"); pg.wait_for_timeout(500)
    asked = pg.query_selector('#leaveAnyway') is not None and 'Not finished yet' in pg.inner_text('.modal')
    pg.click('#leaveAnyway'); pg.wait_for_timeout(500)
    ok(room and asked and pg.evaluate("location.hash") == '#home', 'U23 Stage 7 practice opens in the practice room; leaving with Core left asks first, then is allowed')
    # the sidebar course menu lists only the learner's own courses (3 at a time) and suggests the next stage only after finishing
    pg.set_viewport_size({'width': 1300, 'height': 900}); pg.evaluate("location.hash='u-1'"); pg.wait_for_selector('#tocCourse'); pg.click('#tocCourse'); pg.wait_for_timeout(300)
    one = pg.eval_on_selector_all('.tcoursebox .tmenu .it', "els=>els.filter(e=>e.offsetParent).length")
    pg.evaluate("Core.S.enrolments=[8,9,3,4,5].map(s=>({stage:s,status:'active'}))"); pg.evaluate("location.hash='home'"); pg.wait_for_timeout(500)
    pg.evaluate("location.hash='u-1'"); pg.wait_for_selector('#tocCourse'); pg.wait_for_timeout(400); pg.click('#tocCourse'); pg.wait_for_timeout(300)
    shown = pg.eval_on_selector_all('.tcoursebox .tmenu > a.it', "els=>els.filter(e=>e.offsetParent).map(e=>e.getAttribute('href'))")
    ok(one <= 2 and len(shown) == 4 and shown[0] == '#stage-8' and shown[-1] == '#courses' and pg.query_selector('.tshowall') is not None and pg.query_selector('.tnext') is None,
       'U24 The sidebar course menu shows only the learner\'s own courses (3 + "Show all"), no suggestion before finishing')
    pg.evaluate("Core.S.enrolments=[]")
    ok(not errs, 'U22 No page errors ' + '; '.join(errs[:3])); b.close()
f = [l for l in LOG if l.startswith('FAIL')]; print(f'{len(LOG)-len(f)}/{len(LOG)} passed'); sys.exit(1 if f else 0)
