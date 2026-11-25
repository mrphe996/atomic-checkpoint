"""ESL checks (course keys 22–29): course switcher, lesson videos with pause questions, practice, word games and Unit Tests."""
import os, glob
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
KEYS = sorted({int(os.path.basename(f)[5:7]) for f in glob.glob(os.path.join(os.path.dirname(__file__), '..', 'web', 'content', 'stage2[2-9]-unit01.json'))})
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); ctx = b.new_context(viewport={'width': 1280, 'height': 900}, reduced_motion='reduce'); pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1#home'); pg.wait_for_timeout(800)
    pg.evaluate("""(async()=>{ await Backend.signUp({email:'esl@example.com',password:'password123',name:'Eli English',birthYear:2016,grade:'Year 3',country:'VN',schoolOther:'Atomic',tester:true}); await Core.boot(Core.C); await Core.switchStage(22); await Core.switchUnit(1); location.hash='u-1'; })()""")
    pg.wait_for_timeout(3000)
    ok(all(k in pg.evaluate('Core.STAGES') for k in KEYS) and len(KEYS) >= 1, f'E1 ESL courses on the platform: keys {KEYS}')
    ok(pg.evaluate('Core.IS_ESL') and pg.evaluate('Core.stageLabel()') == 'Stage 2 English (ESL)', 'E2 Stage 2 ESL is open and named correctly')
    body = pg.evaluate('document.body.innerText')
    ok('My Family and Home' in body and pg.query_selector('a[href="#gm-1-1"]') is not None, 'E3 The unit page shows the unit and its word games')
    pg.evaluate("location.hash='v-1-1'"); pg.wait_for_timeout(2000)
    src = pg.evaluate("(document.querySelector('video')||{}).currentSrc || (document.querySelector('video')||{}).src || ''")
    ok('media/esl/s2/u1_s1.mp4' in src, f'E4 Lesson 1.1 plays its own lesson video ({src[-24:]})')
    dur = pg.evaluate("new Promise(r => { const v = document.querySelector('video'); if (v.readyState >= 1) r(v.duration); else v.addEventListener('loadedmetadata', () => r(v.duration)); setTimeout(() => r(0), 4000); })")
    ok(dur > 60, f'E5 The video loads ({dur:.0f} s)')
    s = pg.evaluate("(()=>{ const s = Core.sec('1.1'); return { stops: s.stops.length, t: s.stops.map(x => x.t), dur: s.video.dur, caps: s.captions.length, vocab: s.vocab.length } })()")
    ok(s['stops'] == 2 and all(0 < t < s['dur'] for t in s['t']) and s['caps'] > 10, f"E6 Two pause questions inside the video ({s['t']}) and {s['caps']} caption lines")
    pg.evaluate("location.hash='profile'"); pg.wait_for_timeout(1500); pg.click('#simAll'); pg.wait_for_timeout(800)
    pg.evaluate("location.hash='ex-1-1'"); pg.wait_for_timeout(1800)
    ok(pg.query_selector('.qcard .opt, .qcard .mt, .qcard select') is not None and pg.query_selector('.qcard input[type=text], .mqf') is None, 'E7 Stage 2 practice is tap-only')
    rd = pg.evaluate("Core.sec('1.1').req.concat(Core.sec('1.1').prac).filter(q => q.ctx).length")
    ok(rd >= 2, f'E8 Reading questions show the lesson text ({rd})')
    keys = pg.evaluate("""(async()=>{ let bad = 0, n = 0; for (const k of %s) for (let i = 1; i <= 6; i++) { const u = await fetch(`content/stage${k}-unit${String(i).padStart(2,'0')}.json`).then(r=>r.ok?r.json():null); if (!u) continue; n++; if ((u.tests.A||[]).some(q => (q.options||[]).some(o => 'ok' in o) || q.accept)) bad++; } return [n, bad]; })()""" % KEYS)
    ok(keys[1] == 0 and keys[0] >= 6, f'E9 {keys[0]} ESL units load and their Unit Test answers stay on the server')
    pg.evaluate("location.hash='home'"); pg.wait_for_timeout(1500)
    ok(pg.query_selector('#stageSwitch [data-stage="22"]') is not None, 'E10 The course switcher lists ESL Stage 2')
    ok(not errs, 'E11 No page errors' + (': ' + errs[0] if errs else ''))
    b.close()
fails = [l for l in LOG if l.startswith('FAIL')]
print(f'{len(LOG) - len(fails)}/{len(LOG)} passed')
