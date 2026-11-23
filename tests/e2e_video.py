"""Video player against the real media files: every pause question stops the video at its time, in a gap in the
narration, and the video ends cleanly (real file length = declared length, completion fires, the clock never passes
the total). Checks every section of the units listed in UNITS (default Stage 7 Unit 3).
Run with the default config: `node tools/write-config.mjs`, then `python3 tests/e2e_video.py`."""
import os, json, subprocess
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); WEB = os.path.join(os.path.dirname(__file__), '..', 'web')
UNITS = [(7, 3)]; LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
def silences(path):
    r = subprocess.run(['ffmpeg', '-i', path, '-vn', '-af', 'silencedetect=n=-38dB:d=0.3', '-f', 'null', '-'], capture_output=True, text=True).stderr
    s = [float(l.split('silence_start: ')[1]) for l in r.splitlines() if 'silence_start' in l]
    e = [float(l.split('silence_end: ')[1].split()[0]) for l in r.splitlines() if 'silence_end' in l]
    return list(zip(s, e))
def signup(pg):
    pg.evaluate("location.hash='signup'"); pg.wait_for_timeout(300)
    pg.fill('#suName', 'Vic Video'); pg.fill('#suEmail', 'video@example.com'); pg.fill('#suPw', 'password123'); pg.click('#suNext1'); pg.wait_for_selector('#suYear')
    pg.select_option('#suYear', index=3); pg.select_option('#suGrade', index=2); pg.click('#suNext2'); pg.wait_for_selector('#suCountry')
    pg.select_option('#suCountry', 'SG'); pg.wait_for_timeout(200); pg.select_option('#suSchool', index=1); pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_function("location.hash==='#home'")
FILL = """(sid)=>{const st=Core.cur(); for (const s of Core.C.sections){ if (s.id===sid) break; const vs=Core.vstate(st,s.id);
  s.stops.forEach(x=>vs.stops[x.id]={done:true,ok:true,tries:1,sim:true}); vs.completed=true; vs.pos=0;
  s.req.forEach(q=>st.items[q.id]={done:true,ok:true,tries:1,score:1,sim:true}); } Core.persist();}"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--autoplay-policy=no-user-gesture-required'])
    pg = b.new_page(viewport={'width': 1300, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1'); pg.wait_for_selector('#heroStart'); signup(pg)
    for stage, unit in UNITS:
        if pg.evaluate("Core.STAGE") != stage:
            pg.evaluate(f"location.hash='checkout-{stage}'"); pg.wait_for_timeout(600); pg.click('#payBtn'); pg.wait_for_function(f"Core.STAGE==={stage}", timeout=8000)
        if not pg.query_selector(f'#payBtn') and pg.evaluate("Core.canOpen ? true : true"):
            pass
        pg.evaluate(f"location.hash='checkout-{stage}'"); pg.wait_for_timeout(500)
        if pg.query_selector('#payBtn'): pg.click('#payBtn'); pg.wait_for_timeout(800)
        pg.evaluate(f"Core.switchUnit({unit})"); pg.wait_for_function(f"Core.UNO==={unit}", timeout=8000)
        secs = pg.evaluate("Core.C.sections.map(s=>({id:s.id,video:s.video,stops:s.stops.map(x=>({id:x.id,t:x.t}))}))")
        for s in secs:
            tag = f"S{stage} U{unit} {s['id']}"; path = os.path.join(WEB, s['video']['src'].split('?')[0])
            real = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path], capture_output=True, text=True).stdout)
            ok(abs(real - s['video']['dur']) < 0.15, f"{tag} declared length {s['video']['dur']:.2f}s matches the file ({real:.2f}s)")
            sil = silences(path)
            for x in s['stops']:
                gap = any(a - 0.05 <= x['t'] <= e2 + 0.05 for a, e2 in sil)
                ok(gap, f"{tag} pause {x['id']} at {x['t']:.2f}s falls in a gap in the narration")
            pg.evaluate(FILL, s['id']); pg.evaluate(f"location.hash='v-{s['id'].replace('.', '-')}'")
            pg.wait_for_selector('video'); pg.wait_for_function("document.querySelector('video').readyState>=1", timeout=15000)
            ok(abs(pg.evaluate("document.querySelector('video').duration") - real) < 0.15, f"{tag} the browser loads the new file (duration {real:.1f}s)")
            for i, x in enumerate(s['stops']):
                pg.evaluate(f"(()=>{{const v=document.querySelector('video'); v.muted=true; v.currentTime={max(0, x['t'] - 2.5)}; v.play();}})()")
                try:
                    pg.wait_for_function("document.querySelector('.stop') && document.querySelector('video').paused", timeout=12000); stopped = True
                except Exception: stopped = False
                t = pg.evaluate("document.querySelector('video').currentTime"); n = pg.inner_text('.stop .eyebrow') if stopped else ''
                ok(stopped and abs(t - x['t']) < 0.06 and f'QUESTION {i + 1} OF' in n, f"{tag} pause {i + 1} ({x['id']}) stops at {x['t']:.2f}s (got {t:.2f}s)")
                pg.evaluate(f"(()=>{{const st=Core.cur(); Core.vstate(st,'{s['id']}').stops['{x['id']}']={{done:true,ok:true,tries:1,sim:true}}; Core.persist();}})()")
                pg.evaluate(f"location.hash='home'"); pg.wait_for_timeout(150); pg.evaluate(f"location.hash='v-{s['id'].replace('.', '-')}'")
                pg.wait_for_selector('video'); pg.wait_for_function("document.querySelector('video').readyState>=1", timeout=15000)
            # the end
            pg.evaluate(f"(()=>{{const v=document.querySelector('video'); v.muted=true; v.currentTime={real - 2.0}; v.play();}})()")
            pg.wait_for_function("document.querySelector('video').ended", timeout=15000)
            pg.wait_for_timeout(400)
            done = pg.evaluate(f"Core.vstate(Core.cur(),'{s['id']}').completed")
            clock = pg.inner_text('.time') if pg.query_selector('.time') else ''
            a, _, tot = clock.partition(' / ')
            ok(done and a.strip() == tot.strip(), f"{tag} plays to the end, the lesson is marked watched and the clock reads {clock!r}")
    ok(not errs, 'No page errors' + (': ' + errs[0] if errs else ''))
    b.close()
fails = [l for l in LOG if l.startswith('FAIL')]
print(f"{len(LOG) - len(fails)}/{len(LOG)} passed")
