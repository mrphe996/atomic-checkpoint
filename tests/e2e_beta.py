"""Test-phase build (BILLING=off): everything open, no payment screens. Run after `node tools/write-config.mjs`."""
import os, sys
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(reduced_motion='reduce'); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1'); pg.wait_for_selector('#heroStart')
    ok('No sign-up' in pg.inner_text('body') and 'Free test' in pg.inner_text('header'), 'B1 Landing and menu say the course is free while testing')
    pg.evaluate("location.hash='pricing'"); pg.wait_for_timeout(400)
    ok(pg.query_selector('#betaNote') is not None and pg.query_selector('#buy-monthly') is None, 'B2 Plans page replaced by the free test page (no buy buttons)')
    pg.evaluate("location.hash='signup'"); pg.wait_for_timeout(300)
    pg.fill('#suName', 'Zed Tester'); pg.fill('#suEmail', 't@example.com'); pg.fill('#suPw', 'password123'); pg.click('#suNext1'); pg.wait_for_selector('#suYear')
    pg.select_option('#suYear', index=3); pg.select_option('#suGrade', 'Year 7 / Grade 6'); pg.fill('#suSchool', 'Test School'); pg.click('#suNext2'); pg.wait_for_selector('.su-stage')
    pg.click('.su-stage[data-stage="7"]'); pg.click('#suNext3'); pg.wait_for_selector('.su-plan'); pg.click('.su-plan[data-plan="7"]'); pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_function("location.hash==='#home'")
    ok(pg.evaluate("Core.S.sub.status") == 'beta' and not pg.evaluate("Core.secLock(Core.cur(), Core.C.sections[1]) && Core.secLock(Core.cur(), Core.C.sections[1]).paywall"), 'B3 No paywall on any section')
    pg.evaluate("location.hash='home'"); pg.wait_for_timeout(400); ok(pg.query_selector('#freeBanner') is None, 'B4 No “free plan” upsell banner')
    pg.evaluate("location.hash='profile'"); pg.wait_for_timeout(400); pg.click('#simAll'); pg.wait_for_timeout(900)
    pg.evaluate("location.hash='test'"); pg.wait_for_timeout(500); ok(pg.query_selector('#startTest') is not None, 'B5 Unit Test opens without a plan')
    pg.evaluate("location.hash='settings'"); pg.wait_for_timeout(600)
    ok(pg.query_selector('#setParent') is not None and pg.query_selector('#billingCard') is None, 'B6 Student settings show the optional parent email and no billing')
    ok(not errs, 'B7 No page errors ' + '; '.join(errs[:3])); b.close()
f = [l for l in LOG if l.startswith('FAIL')]; print(f'{len(LOG)-len(f)}/{len(LOG)} passed'); sys.exit(1 if f else 0)
