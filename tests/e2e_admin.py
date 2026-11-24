"""Admin console + Maths course checks (preview build). Run after `node tools/write-config.mjs` with the range server on :8765."""
import os, sys
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1360, 'height': 1000}, reduced_motion='reduce'); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1'); pg.wait_for_timeout(700)
    pg.evaluate("""(async()=>{ await Backend.signUp({email:'adm@example.com',password:'password123',name:'Ada Admin',birthYear:2011,grade:'Year 9',country:'VN',schoolOther:'Atomic'}); await Core.boot(Core.C); location.hash='checkout-19'; })()""")
    pg.wait_for_timeout(1500); pg.click('#payBtn'); pg.wait_for_timeout(1500)
    ok(pg.evaluate("Core.STAGE") == 19 and pg.evaluate("Core.unitCount()") == 15, 'A1 Enrolled in Mathematics Stage 9 (15 units)')
    # a learner is refused, an admin gets the console
    pg.evaluate("location.hash='admin'"); pg.wait_for_timeout(900)
    ok(pg.query_selector('#adTab-overview') is None and pg.query_selector('#becomeAdmin') is not None, 'A2 A learner cannot open the admin console')
    pg.click('#becomeAdmin'); pg.wait_for_timeout(1200)
    tabs = ['overview', 'users', 'content', 'exams', 'reports', 'news', 'settings', 'audit']
    good = True
    for t in tabs:
        pg.click(f'#adTab-{t}'); pg.wait_for_timeout(900)
        if 'went wrong' in pg.inner_text('#adBody') or pg.query_selector('#adBody .banner.adv'): good = False
    ok(good, 'A3 Every admin tab opens without an error')
    # edit a lesson check question → the learner sees the change
    pg.evaluate("""(async()=>{ await Backend.admin.saveQuestion('m9u01s1k01','stage19-unit01',false,false,{prompt:'EDITED CHECK'},{prompt:'EDITED CHECK'}); await Core.dropCache(); })()"""); pg.wait_for_timeout(600)
    pg.evaluate("location.hash='v-1-1'"); pg.wait_for_timeout(1500)
    ok('EDITED CHECK' in pg.inner_text('#main'), 'A4 An edited question reaches the learner')
    # hide a unit, publish an announcement
    pg.evaluate("""(async()=>{ await Backend.admin.setUnit('stage19-unit15', true); await Backend.admin.announce('Maintenance tonight', 'Slow from 21:00.', '19', 'warn'); })()"""); pg.wait_for_timeout(400)
    pg.goto(BASE + '#home'); pg.wait_for_timeout(2500)
    ok(pg.query_selector('.announce') is not None, 'A5 Announcement shown on the dashboard')
    ok(pg.evaluate("Core.unitReady(15)") is False and pg.evaluate("Core.unitReady(14)") is True, 'A6 A hidden unit is closed to learners')
    ok(len(pg.evaluate("Backend.admin.audit()")) >= 3, 'A7 Admin actions are in the audit log')
    # maths display: stacked fractions, worked solutions, question bank search
    pg.evaluate("location.hash='profile'"); pg.wait_for_timeout(800); pg.click('#simAll'); pg.wait_for_timeout(600)
    pg.evaluate("location.hash='v-1-1'"); pg.wait_for_timeout(1200)
    pg.evaluate("location.hash='u-8'"); pg.wait_for_timeout(1200); pg.evaluate("location.hash='v-8-1'"); pg.wait_for_timeout(1500)
    ok(pg.query_selector('.mt .katex .mfrac') is not None, 'A8 Fractions are typeset (KaTeX) in maths lessons')
    pg.evaluate("location.hash='bank'"); pg.wait_for_timeout(1200)
    n0 = int(pg.inner_text('#bankCount').split()[0]); pg.fill('#bankSearch', 'recurring'); pg.press('#bankSearch', 'Enter'); pg.wait_for_timeout(900)
    n1 = int(pg.inner_text('#bankCount').split()[0])
    ok(0 < n1 < n0, f'A9 Question Bank search narrows the list ({n0} → {n1})')
    pg.evaluate("location.hash='board'"); pg.wait_for_timeout(900)
    ok('MATHEMATICS' in pg.inner_text('.lbhero').upper(), 'A10 Leaderboard is for the current course')
    pg.evaluate("location.hash='cert'"); pg.wait_for_timeout(1500)
    ok('Mathematics' in pg.inner_text('#main') or 'MATHEMATICS' in pg.inner_text('#main').upper(), 'A11 Certificate page is for Mathematics')
    pg.evaluate("""(()=>{ const m = AtomicMath.field({ value: '', vars: 'x', onInput: v => { window.__mq = v; } }); m.el.id = 'mqT'; document.body.prepend(m.el); })()""")
    pg.click('#mqT .mqf'); pg.keyboard.type('3x^2+x/2'); pg.keyboard.press('ArrowRight'); pg.keyboard.type('-1')
    v = pg.evaluate('window.__mq')
    ok(v == '3x^2+x/2-1' and pg.query_selector('#mqT .mqf .katex .mfrac') is not None and pg.query_selector('#mqT .mqf .katex .msupsub') is not None, f'A13 Maths field builds powers and fractions as you type ({v})')
    pg.click('#mqT .mkey[aria-label=clear]'); pg.click('#mqT .mkey[aria-label="square root"]'); pg.keyboard.type('50')
    ok(pg.evaluate('window.__mq') == '√50', 'A14 Keypad root key builds √50')
    ok(not errs, 'A12 No page errors ' + '; '.join(errs[:3])); b.close()
f = [l for l in LOG if l.startswith('FAIL')]; print(f'{len(LOG)-len(f)}/{len(LOG)} passed'); sys.exit(1 if f else 0)
