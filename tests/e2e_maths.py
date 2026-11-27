"""Maths upgrade checks (preview build, Mathematics open): deeper lessons, one question per kind in Practice,
More practice, the lesson-notes reader and keeping a typed answer while the notes are open."""
import os, re
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); ctx = b.new_context(viewport={'width': 1280, 'height': 900}, reduced_motion='reduce'); pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1#home'); pg.wait_for_timeout(800)
    pg.evaluate("""(async()=>{ await Backend.signUp({email:'mx@example.com',password:'password123',name:'Max Maths',birthYear:2013,grade:'Year 7',country:'VN',schoolOther:'Camday',tester:true}); await Core.boot(Core.C); await Core.switchStage(17); await Core.switchUnit(2); location.hash='profile'; })()""")
    pg.wait_for_timeout(3500); pg.click('#simAll'); pg.wait_for_timeout(800)
    sec = pg.evaluate("(()=>{ const s=Core.sec('2.3'); return { kinds: s.lesson.map(b=>b.k), figs: s.lesson.filter(b=>b.fig).map(b=>b.fig.kind), checks: s.stops.length, prac: s.prac.map(q=>q.prompt), deep: s.prac.concat(s.adv||[]).filter(q=>q.type==='explain'||/Test|missing|TWO|mistake|statement|says|magic/i.test(q.prompt)).length + s.lesson.filter(b=>b.k==='error').length, more: (s.more||[]).length } })()")
    ok('example' in sec['kinds'] and 'method' in sec['kinds'] and 'tiles' in sec['figs'] and sec['checks'] >= 2, f"M1 Lesson 2.3 explains with tiles, a worked contrast example, a method and {sec['checks']} prediction checks")
    shape = [re.sub(r'[−-]?\d+', '#', t) for t in sec['prac']]
    ok(len(shape) == len(set(shape)), f"M2 Main Practice has one question of each kind ({len(shape)} different kinds, no number-swapped repeats)")
    ok(sec['more'] >= 6, f"M3 The extra variants are kept as More practice ({sec['more']})")
    deep = sec['deep']
    ok(deep >= 4, f"M4 Lesson + Practice include reasoning tasks: explain, missing term, test a claim, spot the mistake ({deep})")
    # stage 3–8 units that are not rewritten yet also stop repeating one method
    rep = pg.evaluate("""(async()=>{ const r = await fetch('content/stage17-unit05.json').then(x=>x.json()); let worst = 0;
      r.sections.forEach(s => { const c = {}; s.prac.forEach(q => { const k = q.prompt.replace(/[−-]?\\d+(\\.\\d+)?/g, '#'); c[k] = (c[k] || 0) + 1; worst = Math.max(worst, c[k]); }); }); return worst; })()""")
    ok(rep <= 2, f'M5 Other units: a question shape appears at most twice in main Practice (worst {rep})')
    # lesson: finishing offers notes or practice
    pg.evaluate("location.hash='v-2-3'"); pg.wait_for_timeout(2000)
    ok(pg.query_selector('#lessonChoose #readNotes') is not None and pg.query_selector('#lessonChoose #toPractice') is not None, 'M6 After the lesson: choose "Read the lesson notes" or "Practise"')
    ok(pg.query_selector('.lb-idea .qfig svg') is not None, 'M7 The tile picture is drawn in the lesson')
    pg.click('#readNotes'); pg.wait_for_timeout(900)
    top = pg.evaluate("(()=>{ const b=document.querySelector('#readerBody'), t=document.querySelector('#rd-2-3'); return Math.abs(t.offsetTop - b.scrollTop) })()")
    ok(pg.query_selector('#reader') is not None and top < 40 and pg.input_value('#readerSec') == '2.3', f'M8 The notes open at lesson 2.3 (offset {top}px)')
    ok(len(pg.query_selector_all('#reader .rdsec')) == 6 and 'PDF pages' in pg.inner_text('#rd-2-3 h2'), 'M9 The whole unit can be scrolled; each lesson shows its PDF pages')
    fs0 = pg.evaluate("parseFloat(getComputedStyle(document.querySelector('#readerBody')).fontSize)"); pg.click('#readerBig'); pg.click('#readerBig'); pg.wait_for_timeout(200)
    fs1 = pg.evaluate("parseFloat(getComputedStyle(document.querySelector('#readerBody')).fontSize)")
    ok(fs1 > fs0 and '#page=' in (pg.get_attribute('#readerPdf', 'href') or ''), f'M10 Zoom works ({fs0:.0f}px → {fs1:.0f}px) and the PDF link opens at the right page')
    pg.evaluate("document.querySelector('#readerBody').scrollTop = document.querySelector('#rd-2-5').offsetTop + 50"); pg.wait_for_timeout(500)
    pg.click('#readerClose'); pg.wait_for_timeout(300)
    pg.evaluate("location.hash='v-2-5'"); pg.wait_for_timeout(1500); pg.click('#readNotes'); pg.wait_for_timeout(800)
    ok(pg.input_value('#readerSec') == '2.5', 'M11 Reopening continues where the learner stopped')
    pg.click('#readerClose')
    # practice: a typed answer survives opening the notes
    pg.evaluate("location.hash='ex-2-3'"); pg.wait_for_timeout(1500)
    pg.click('#lv-prac'); pg.wait_for_timeout(500)   # Maths practises in the full-screen practice room
    ok(pg.query_selector('#lv-more') is not None, 'M12 Maths practice room has a More practice level')
    i = pg.evaluate("Core.sec('2.3').prac.findIndex(q => q.type === 'expr')")
    pg.locator('.fqs .fq').nth(i).click(); pg.wait_for_timeout(400)
    pg.click('.qcard .mqf'); pg.keyboard.type('4a'); pg.wait_for_timeout(200)
    before = pg.inner_text('.qcard .mqf')
    pg.click('#reviewNotes'); pg.wait_for_timeout(700); pg.click('#readerClose'); pg.wait_for_timeout(300)
    ok(pg.query_selector('.qcard .mqf') is not None and pg.inner_text('.qcard .mqf') == before and '4' in before, 'M13 Opening and closing the notes keeps the answer being typed')
    pg.set_viewport_size({'width': 390, 'height': 844}); pg.click('#reviewNotes'); pg.wait_for_timeout(700)
    ok(pg.evaluate("document.querySelector('#readerBody').scrollWidth <= document.querySelector('#readerBody').clientWidth + 2"), 'M14 The notes fit a phone screen')
    pg.click('#readerClose')
    pg.set_viewport_size({'width': 1280, 'height': 900}); pg.evaluate("location.hash='tests'"); pg.wait_for_timeout(1500)
    ok(pg.query_selector('#challengeCard a[href="#challenge"]') is not None, 'M16 Maths Challenge opens from Tests & exams inside the Maths course')
    pg.evaluate("location.hash='u-2'"); pg.wait_for_timeout(1500)
    ok(pg.query_selector('#challengeCard') is not None and pg.query_selector('nav a[href="#challenge"]') is None, 'M17 …and from the Maths unit page, not the top menu')
    # Phase 2: lesson 1.1 has a video; the Read page links to it and the player pauses on the lesson's own check questions
    pg.evaluate("(async()=>{ await Core.switchUnit(1); location.hash='v-1-1'; })()"); pg.wait_for_timeout(2500)
    ok(pg.get_attribute('#lessonVideo', 'href') == '#vw-1-1', 'M18 Lesson 1.1 shows a "Watch the video lesson" card')
    pg.click('#lessonVideo'); pg.wait_for_timeout(2500)
    v = pg.evaluate("(()=>{ const v=document.querySelector('video'); return v && { src: v.currentSrc || v.src, dur: v.duration } })()")
    ok(v and v['src'].endswith('1-1.mp4') and v['dur'] > 200, f'M19 The video lesson plays in the app player ({v})')
    ok(not errs, 'M15 No page errors' + (': ' + errs[0] if errs else ''))
    b.close()
fails = [l for l in LOG if l.startswith('FAIL')]
print(f'{len(LOG) - len(fails)}/{len(LOG)} passed')
