"""Paragraph answers and the Extreme tier (pilot: Science Stage 8 Unit 7). Run with the default config: `node tools/write-config.mjs`."""
import os
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
def go(pg, r): pg.evaluate(f"location.hash='{r}'"); pg.wait_for_timeout(700)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(reduced_motion='reduce', viewport={'width': 1300, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1'); pg.wait_for_selector('#heroStart')
    go(pg, 'signup')
    pg.fill('#suName', 'Pia Paragraph'); pg.fill('#suEmail', 'para@example.com'); pg.fill('#suPw', 'password123'); pg.click('#suNext1'); pg.wait_for_selector('#suYear')
    pg.select_option('#suYear', index=3); pg.select_option('#suGrade', 'Year 7 / Grade 6'); pg.fill('#suSchool', 'Test School'); pg.click('#suNext2'); pg.wait_for_selector('.su-stage')
    pg.click('.su-stage[data-stage="8"]'); pg.click('#suNext3'); pg.wait_for_selector('.su-plan'); pg.click('.su-plan[data-plan="8"]'); pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_function("location.hash==='#home'")
    pg.wait_for_function("Core.STAGE===8", timeout=8000)   # one stage per learner: this learner signs up for Stage 8
    pg.evaluate("Core.switchUnit(7)"); pg.wait_for_function("Core.UNO===7 && Core.C && Core.C.sections[0].ext", timeout=8000)
    go(pg, 'profile'); pg.click('#simAll'); pg.wait_for_timeout(900)
    go(pg, 'ex-7-1'); pg.wait_for_selector('.qcard')
    tab = pg.query_selector('#lv-ext')
    ok(tab is not None, 'X1 Stage 8 Unit 7 practice room has an Extreme level')
    tab.click(); pg.wait_for_timeout(500)
    ok(pg.query_selector('textarea.para') is not None and pg.query_selector('.pcount') is not None, 'X2 The first Extreme question is a paragraph with a word and sentence counter')
    pg.fill('textarea.para', 'It gets hotter.'); pg.wait_for_timeout(150)
    ok('3 words' in pg.inner_text('.pcount') and '1 sentence' in pg.inner_text('.pcount'), 'X3 The counter counts words and sentences as you type')
    pg.click('.qcard .btn.primary'); pg.wait_for_timeout(300)
    ok(pg.query_selector('.fb.warn') is not None and 'at least 4 sentences' in pg.inner_text('.fb.warn'), 'X4 A too-short answer is asked for more, without using a try')
    ok(pg.evaluate("(Core.cur().items['s8u07s1x01']||{}).tries||0") == 0, 'X5 No try counted for a too-short answer')
    pg.click('button:has-text("Show a writing frame")'); pg.wait_for_timeout(150)
    ok(pg.query_selector('.pframe:not([hidden])') is not None, 'X6 The writing frame opens on request')
    model = pg.evaluate("Core.C.sections[0].ext[0].model")
    pg.fill('textarea.para', model); pg.wait_for_timeout(150); pg.click('.qcard .btn.primary'); pg.wait_for_timeout(500)
    ok(pg.query_selector('.fb.ok') is not None and pg.query_selector('.rubric li.hit') is not None, 'X7 A full answer is marked correct against the mark scheme (keywords in preview mode)')
    # Hard tab carries paragraph questions too
    pg.click('#lv-adv'); pg.wait_for_timeout(400)
    ok(pg.evaluate("Core.C.sections[0].adv.filter(q=>q.type==='para').length") >= 2, 'X8 Hard (* Advanced) has paragraph questions with data')
    # Question Bank: Extreme set filter
    go(pg, 'bank'); pg.wait_for_timeout(600)
    if pg.query_selector('#leaveAnyway'): pg.click('#leaveAnyway'); pg.wait_for_timeout(500); go(pg, 'bank')
    pg.click('.qbtabs[data-k="tier"] .chip[data-v="ext"]'); pg.wait_for_timeout(250)
    ok(int(pg.inner_text('#bankCount').split()[0]) == 8, 'X9 The Question Bank filters the 8 Extreme questions')
    # Unit Test: the 6-mark paragraph question is written in a large box
    go(pg, 'test'); pg.wait_for_selector('#startTest'); pg.click('#startTest'); pg.wait_for_timeout(500)
    pg.evaluate("AtomicApp.UI.testIdx = Core.C.tests.A.findIndex(q=>q.type==='para'); AtomicApp.render()"); pg.wait_for_timeout(500)
    ok(pg.query_selector('textarea.para') is not None and 'checked against the mark scheme' in pg.inner_text('.qcard'), 'X10 Unit Test A has the 6-mark paragraph question')
    pub = pg.evaluate("JSON.stringify(Core.C.tests)")
    ok('"rubric"' not in pub and '"partial"' not in pub and '"model"' not in pub, 'X11 The paper sent to the browser has no mark scheme or examples')
    ok(not errs, 'X12 No page errors ' + '; '.join(errs[:3])); b.close()
print(f"{sum(1 for l in LOG if l.startswith('PASS'))}/{len(LOG)} passed")
