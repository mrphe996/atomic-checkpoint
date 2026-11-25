"""Stages 1–2 checks (Science course keys 1, 2 · Mathematics 11, 12): picture lessons, tap-only practice, questions read aloud,
word games inside the course and the stage switcher."""
import os
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); ctx = b.new_context(viewport={'width': 1280, 'height': 900}, reduced_motion='reduce'); pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1#home'); pg.wait_for_timeout(800)
    pg.evaluate("""(async()=>{ await Backend.signUp({email:'yy@example.com',password:'password123',name:'Yen Young',birthYear:2019,grade:'Year 1',country:'VN',schoolOther:'Atomic'}); await Core.boot(Core.C); await Core.switchStage(1); await Core.switchUnit(1); location.hash='u-1'; })()""")
    pg.wait_for_timeout(3000)
    ok(all(g in pg.evaluate('Core.STAGES') for g in (1, 2, 11, 12)), 'Y1 Science Stages 1–2 and Mathematics Stages 1–2 are courses on the platform')
    ok(pg.evaluate("document.body.classList.contains('tiny')") and '1 Read the lesson' in pg.inner_text('.u4steps'), 'Y2 A Stage 1 unit uses the picture-lesson path: read, practise, word games, Unit Test')
    ok(pg.query_selector('a[href="#gm-1-1"]') is not None, 'Y3 Word games sit inside the course, next to Practice')
    pg.evaluate("location.hash='v-1-1'"); pg.wait_for_timeout(1800)
    ok(len(pg.query_selector_all('.lessonbody .qfig svg')) >= 2 and len(pg.query_selector_all('.lessonbody .readq')) >= 3, 'Y4 The lesson has pictures and a 🔊 Read to me button on every idea')
    ok(len(pg.query_selector_all('.lcheck .opt.pcard')) >= 2 and pg.query_selector('.lcheck input[type=text], .lcheck .mqf') is None, 'Y5 Check questions are answered by tapping picture cards (no typing)')
    # tap the right picture in the first check
    right = pg.evaluate("Core.sec('1.1').stops[0].q.options.find(o=>o.ok).t")
    pg.click(f'.lcheck >> nth=0 >> .opt.pcard[aria-label="{right}"]'); pg.wait_for_timeout(200)
    btn = pg.query_selector('.lcheck >> nth=0 >> button:has-text("Check")')
    if btn: btn.click(); pg.wait_for_timeout(500)
    ok('✓' in pg.inner_text('.lcheck >> nth=0') or pg.query_selector('.lcheck .fb.ok, .lcheck .good') is not None, 'Y6 Tapping the right picture is marked correct')
    pg.evaluate("location.hash='profile'"); pg.wait_for_timeout(1500); pg.click('#simAll'); pg.wait_for_timeout(800)
    pg.evaluate("location.hash='ex-1-1'"); pg.wait_for_timeout(1800)
    ok(pg.query_selector('.readq') is not None and pg.query_selector('input[type=text], .mqf') is None, 'Y7 Practice questions can be read aloud and never need typing')
    # every new unit: tap-only, word bank, two picture questions in Core, 15-question tests on the server only
    st = pg.evaluate("""(async()=>{ const out={units:0,typing:0,vocab:0,core:0,keys:0}; const TAP=['mcq','multi','grid','match','order'];
      for (const [k,n] of [[1,6],[2,6],[11,8],[12,8]]) for (let i=1;i<=n;i++) { const u = await fetch(`content/stage${k}-unit${String(i).padStart(2,'0')}.json`).then(r=>r.json()); out.units++;
        if (u.tests && (u.tests.A||[]).some(q=>q.options && q.options.some(o=>'ok' in o))) out.keys++;
        u.sections.forEach(s=>{ [...s.req,...s.prac,...s.adv,...(s.more||[]),...s.stops.map(x=>x.q)].forEach(q=>{ if(!TAP.includes(q.type)) out.typing++; });
          if ((s.vocab||[]).length>=3) out.vocab++; if (s.req.filter(q=>q.fig||q.pic||['grid','match','order'].includes(q.type)||(q.options||[]).some(o=>o.e)).length>=2) out.core++; }); }
      return out; })()""")
    ok(st['units'] == 28 and st['typing'] == 0, f"Y8 All 28 units ({st['units']}) are tap-only ({st['typing']} typed questions)")
    ok(st['vocab'] == 56 and st['core'] == 56, f"Y9 Every lesson has a word bank ({st['vocab']}/56) and picture questions in Core ({st['core']}/56)")
    ok(st['keys'] == 0, 'Y10 Unit Test answers are not sent to the browser')
    # Mathematics Stage 1: the clock lesson
    pg.evaluate("(async()=>{ await Core.switchStage(11); await Core.switchUnit(7); location.hash='profile'; })()"); pg.wait_for_timeout(2500); pg.click('#simAll'); pg.wait_for_timeout(800)
    pg.evaluate("location.hash='v-7-2'"); pg.wait_for_timeout(1800)
    ok(pg.query_selector('.lessonbody .qfig svg circle') is not None and 'o\'clock' in pg.inner_text('.lessonbody'), 'Y11 Maths Stage 1 Time: the lesson draws clocks')
    pg.evaluate("location.hash='ex-7-2'"); pg.wait_for_timeout(1800)
    ok(pg.query_selector('.qcard .opt') is not None and pg.query_selector('.mqf, input[type=text]') is None, 'Y12 Maths Stage 1 practice is tap-only (no keypad)')
    pg.evaluate("(async()=>{ await Core.switchStage(12); await Core.switchUnit(3); location.hash='u-3'; })()"); pg.wait_for_timeout(2500)
    ok('Multiplication' in pg.evaluate('document.body.innerText') and pg.query_selector('a[href="#gm-3-1"]') is not None, 'Y13 Maths Stage 2 unit page opens with its word games')
    pg.set_viewport_size({'width': 390, 'height': 844}); pg.evaluate("location.hash='v-3-1'"); pg.wait_for_timeout(1800)
    ok(pg.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 2"), 'Y14 Picture lessons fit a phone screen')
    pg.set_viewport_size({'width': 1280, 'height': 900}); pg.evaluate("location.hash='home'"); pg.wait_for_timeout(1500)
    ok(all(pg.query_selector(f'#stageSwitch [data-stage="{g}"]') is not None for g in (1, 2, 11, 12)), 'Y15 The course switcher lists Stage 1 and Stage 2 Science and Mathematics')
    ok(not errs, 'Y16 No page errors' + (': ' + errs[0] if errs else ''))
    b.close()
fails = [l for l in LOG if l.startswith('FAIL')]
print(f'{len(LOG) - len(fails)}/{len(LOG)} passed')
