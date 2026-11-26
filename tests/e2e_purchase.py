"""Browser checks of one-time purchases, the free plan and the one-year expiry (demo build).
Run: npm run dev &  then  python3 tests/e2e_purchase.py"""
import os, sys
from playwright.sync_api import sync_playwright

BASE = os.environ.get('BASE', 'http://localhost:8765/')
LOG = []
def ok(cond, msg):
    LOG.append(('PASS' if cond else 'FAIL') + '  ' + msg); print(LOG[-1], flush=True)
def go(pg, r):
    pg.evaluate(f"(location.hash==='#{r}') ? AtomicApp.render() : (location.hash='{r}')"); pg.wait_for_timeout(700)
def txt(pg): return pg.inner_text('body')

def signup(pg, email):
    go(pg, 'signup'); pg.fill('#suName', 'Mai Tran'); pg.fill('#suEmail', email); pg.fill('#suPw', 'password123'); pg.click('#suNext1')
    pg.wait_for_selector('#suYear'); pg.select_option('#suYear', index=4); pg.select_option('#suGrade', 'Year 7 / Grade 6'); pg.fill('#suSchool', 'Home learner')
    pg.click('#suNext2'); pg.wait_for_selector('.su-stage'); pg.click('.su-stage[data-stage="7"]'); pg.click('#suNext3'); pg.wait_for_selector('.su-plan'); pg.click('.su-plan[data-plan="7"]')
    pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_function("location.hash==='#home' && !!document.getElementById('resumeBtn')"); pg.wait_for_timeout(400)

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': 1366, 'height': 860}, reduced_motion='reduce'); pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE); pg.wait_for_timeout(800)

    # pricing page: one-time, no subscription / trial wording
    go(pg, 'pricing'); t = txt(pg)
    ok('Pay once' in t and 'US$49' in t and 'US$119' in t and '365 days' in t, 'pricing: pay once, US$49 / US$119, the 365-day rule')
    ok('free trial' not in t.lower() and '/ month' not in t, 'pricing: no monthly plan or trial left')

    signup(pg, 'buyer@example.com')
    lid = pg.evaluate('Core.cur().id')
    ok(pg.evaluate('Core.myCourses()') == [7] and not pg.evaluate('Core.freeMode()'), 'test checkout at sign-up opens Science 7')
    ok(pg.evaluate('Core.C.sections[0].prac.length') > 0, 'bought course: Practice questions present')

    # a year without study → the course expires on the next visit
    pg.evaluate(f"Backend.devIdle('{lid}', 366)"); pg.reload(); pg.wait_for_timeout(1500)
    ok(pg.evaluate('Core.myCourses()') == [] and pg.evaluate('Core.expiredCourses()') == [7], 'after 366 idle days the course is expired')
    ok(pg.evaluate('Core.freeMode()'), 'expired learner falls back to the free plan')
    go(pg, 'home'); t = txt(pg)
    ok('Your course has expired' in t, 'dashboard explains the expiry')

    # free plan: Unit 3 only, videos + 8 Core questions, no Practice / Advanced, no Unit Test
    pg.evaluate('Core.switchUnit(3)'); pg.wait_for_timeout(600)
    ok(pg.evaluate('Core.UNO') == 3 and pg.evaluate("Core.C.sections.every(s => s.prac.length === 0 && s.adv.length === 0)"), 'free plan: Practice and Advanced removed')
    ok(pg.evaluate("Core.C.sections.every(s => s.req.length === 8)"), 'free plan: 8 Core questions per section')
    ok(pg.evaluate("Core.C.sections.every(s => Core.canOpen(s.id))"), 'free plan: every section of Unit 3 opens (video)')
    ok(pg.evaluate("Core.testState(Core.cur()).state") == 'paywall', 'free plan: Unit Test needs the course')
    go(pg, 'test'); ok('needs the Cambridge Stage 7 course' in txt(pg), 'Unit Test page shows the buy screen')
    n4 = pg.evaluate("Core.INDEX.units.find(u => u.n === 4 && u.ready) ? 4 : 0")
    if n4:
        pg.evaluate('Core.switchUnit(4)'); pg.wait_for_timeout(600)
        lock = pg.evaluate("Core.secLock(Core.cur(), Core.C.sections[0])")
        ok(lock and lock.get('paywall') and lock.get('route') == 'plans', 'free plan: Unit 4 is locked and points to #plans')
        pg.evaluate('Core.switchUnit(3)'); pg.wait_for_timeout(400)

    # buy again → the year restarts and everything opens
    go(pg, 'plans'); pg.wait_for_selector('#plans [data-course="7"]'); pg.click('#plans [data-course="7"]')
    pg.wait_for_function("location.hash==='#home'"); pg.wait_for_timeout(600)
    ok(pg.evaluate('Core.myCourses()') == [7] and not pg.evaluate('Core.freeMode()'), 'bought again: course open')
    ok(pg.evaluate('Core.C.sections[0].prac.length') > 0, 'bought again: Practice questions back')
    pg.reload(); pg.wait_for_timeout(1500)
    ok(pg.evaluate('Core.myCourses()') == [7], 'after reload the re-bought course stays open (year restarted)')

    ok(not errs, 'no JavaScript errors' + (': ' + '; '.join(errs[:3]) if errs else ''))
    b.close()

fails = [l for l in LOG if l.startswith('FAIL')]
print(f'\n{len(LOG) - len(fails)}/{len(LOG)} passed'); sys.exit(1 if fails else 0)
