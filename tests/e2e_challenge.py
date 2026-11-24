"""Maths Challenge checks (preview build). Run after `node tools/write-config.mjs` with the range server on :8765."""
import os, json
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = json.load(open(os.path.join(ROOT, 'web/content/demo/ch-junior.tests.json')))
KANG = json.load(open(os.path.join(ROOT, 'web/content/demo/ch-kangaroo.tests.json')))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); ctx = b.new_context(viewport={'width': 1360, 'height': 1000}, reduced_motion='reduce'); pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    # a visitor can browse
    pg.goto(BASE + '?reset=1#challenge'); pg.wait_for_timeout(1500)
    ok(len(pg.query_selector_all('.chfolder')) == 5, 'C1 Visitors see the five Maths Challenge competitions')
    pg.click('#chFolder-junior'); pg.wait_for_timeout(1200)
    ok(len(pg.query_selector_all('.chpaper')) == 6 and 'Sign up' in pg.inner_text('#chPapers'), 'C2 A competition lists its papers; sitting one needs an account')
    # sign up
    pg.evaluate("""(async()=>{ await Backend.signUp({email:'mc@example.com',password:'password123',name:'Mia Challenge',birthYear:2013,grade:'Year 7',country:'VN',schoolOther:'Atomic'}); await Core.boot(Core.C); location.hash='challenge'; })()""")
    pg.wait_for_timeout(2500)
    ok(pg.query_selector('nav a[href="#challenge"]') is not None, 'C3 "Maths Challenge" is in the main menu')
    # timed paper: every answer right → Gold
    pg.evaluate("location.hash='chl-junior'"); pg.wait_for_timeout(1200)
    pg.click('#chSit-junior-01'); pg.wait_for_timeout(1200)
    ok(pg.query_selector('#startTest') is not None and '60 min' in pg.inner_text('#main'), 'C4 The timed paper opens with the exam-room briefing')
    pg.click('#startTest'); pg.wait_for_timeout(900)
    paper = KEYS['papers']['01']; labels_ok = True
    for i, q in enumerate(paper):
        right = next(j for j, o in enumerate(q['options']) if o['ok'])
        keys = [x.inner_text().strip() for x in pg.query_selector_all('.qcard .opt .key')]
        if keys != ['A', 'B', 'C', 'D', 'E']: labels_ok = False
        texts = [x.inner_text().strip() for x in pg.query_selector_all('.qcard .opt .ot')]
        if texts != [o['t'] for o in q['options']]: labels_ok = False
        pg.click(f'.qcard .opt[data-oi="{right}"]')
        if i < len(paper) - 1: pg.click('#testNext'); pg.wait_for_timeout(120)
    ok(labels_ok, 'C5 Options keep their A–E order (smallest number first), as in a real challenge')
    pg.click('#submitTest'); pg.wait_for_timeout(300); pg.click('.modal .btn.primary')
    pg.wait_for_function("location.hash==='#chr-junior-01'", timeout=10000); pg.wait_for_timeout(1800)
    t = pg.inner_text('#main')
    ok('135/135' in t and 'Gold' in t, 'C6 A perfect paper scores 135/135 and a Gold award')
    ok(len(pg.query_selector_all('.chrev')) == 25 and 'Solution:' in t and len(pg.query_selector_all('.chrev .opt.right')) == 25, 'C7 The results show all 25 questions with the right answer and a worked solution')
    # reload: solutions come back from the server
    p2 = ctx.new_page(); p2.goto(BASE + '#chr-junior-01'); p2.wait_for_timeout(2500)
    ok(p2.inner_text('#main').count('Solution:') == 25, 'C8 Solutions come back from the server in a new tab'); p2.close()
    # practice mode on paper 02
    pg.evaluate("location.hash='chp-junior-02'"); pg.wait_for_timeout(1200)
    ok(pg.query_selector('#chPracGate') is not None, 'C9 Practising first explains that the paper then cannot be sat for an award')
    pg.click('#chPracGo'); pg.wait_for_timeout(900)
    q = KEYS['papers']['02'][0]; wrong = next(j for j, o in enumerate(q['options']) if not o['ok'])
    pg.click(f'.qcard .opt[data-oi="{wrong}"]'); pg.click('#chCheck'); pg.wait_for_timeout(900)
    fb = pg.inner_text('#chFb')
    ok('Not quite' in fb and 'Solution:' in fb and pg.query_selector('.qcard .opt.right') is not None and pg.query_selector('.qcard .opt.wrong') is not None, 'C10 Checking an answer marks it at once and shows the worked solution')
    pg.click('#chNext'); pg.wait_for_timeout(600)
    q2 = KEYS['papers']['02'][1]; right2 = next(j for j, o in enumerate(q2['options']) if o['ok'])
    pg.click(f'.qcard .opt[data-oi="{right2}"]'); pg.click('#chCheck'); pg.wait_for_timeout(900)
    ok('Right' in pg.inner_text('#chFb') and pg.query_selector('.navgrid button.okq') is not None and pg.query_selector('.navgrid button.noq') is not None, 'C11 Right and wrong answers are coloured in the question grid')
    pg.evaluate("location.hash='chl-junior'"); pg.wait_for_timeout(1200)
    ok('Practising · 1/2 right' in pg.inner_text('#chPapers'), 'C12 Practice progress is saved')
    pg.evaluate("location.hash='chx-junior-02'"); pg.wait_for_timeout(1200)
    ok('You have practised this paper' in pg.inner_text('#main'), 'C13 A practised paper cannot be opened as a timed paper')
    err = pg.evaluate("""(async()=>{ try { await Backend.startTest({ learnerId: Core.cur().id, unit: 'ch-junior', form: '02' }); await Backend.submitTest({ learnerId: Core.cur().id, unit: 'ch-junior', form: '02', answers: {}, clientKey: 'x1', meta: {} }); return 'none'; } catch (e) { return e.code; } })()""")
    ok(err == 'practised', f'C14 The server refuses a timed attempt after practice ({err})')
    # Kangaroo: typed whole-number answers
    pg.evaluate("location.hash='chp-kangaroo-01'"); pg.wait_for_timeout(1200); pg.click('#chPracGo'); pg.wait_for_timeout(800)
    kq = KANG['papers']['01'][0]
    pg.fill('.qcard .numin', str(kq['answer'])); pg.click('#chCheck'); pg.wait_for_timeout(900)
    ok('Right' in pg.inner_text('#chFb'), 'C15 Kangaroo answers are typed whole numbers, marked on the spot')
    pg.evaluate("location.hash='challenge'"); pg.wait_for_timeout(1500)
    ok('best 100%' in pg.inner_text('#chFolder-junior') and 'Gold' in pg.inner_text('#chFolder-junior'), 'C16 The overview shows the best score and award')
    # public files have no keys
    pub = pg.evaluate("fetch('content/ch-junior.json').then(r=>r.text())")
    ok('"ok"' not in pub and '"reason"' not in pub, 'C17 The published papers carry no answers or solutions')
    pg.set_viewport_size({'width': 390, 'height': 844}); pg.evaluate("location.hash='chl-inter'"); pg.wait_for_timeout(1200)
    ok(pg.evaluate("document.documentElement.scrollWidth <= 392"), 'C18 Paper list fits a phone screen')
    ok(not errs, 'C19 No page errors' + (': ' + errs[0] if errs else ''))
    b.close()
fails = [l for l in LOG if l.startswith('FAIL')]
print(f'{len(LOG) - len(fails)}/{len(LOG)} passed')
