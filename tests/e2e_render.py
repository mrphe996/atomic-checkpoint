# Every Unit Test question of every course, in the form the browser receives it (no answer keys), must render in the exam room.
from playwright.sync_api import sync_playwright
import os
BASE = os.environ.get('BASE', 'http://localhost:8765/')
files = sorted(f for f in os.listdir(os.path.join(os.path.dirname(__file__), '..', 'web', 'content')) if 'unit' in f and f.endswith('.json'))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1'); pg.wait_for_timeout(1500)
    res = pg.evaluate("""async(files)=>{ const out=[]; let n=0, units=0;
      for (const f of files) { const c=await fetch('content/'+f).then(r=>r.json()).catch(()=>null); if(!c||!c.tests) continue; units++;
        for (const [form,qs] of Object.entries(c.tests)) if (Array.isArray(qs)) for (const q of qs) { n++; const d=document.createElement('div'); document.body.appendChild(d);
          try { QE.renderBody(q, d, { seed:'x', resp: undefined, onChange(){} }); if (!d.children.length) throw new Error('nothing drawn'); } catch(e) { out.push([f,form,q.id,q.type,String(e).slice(0,120)]); } d.remove(); } }
      return {n,units,out}; }""", files)
    bad = res['out']
    print(('PASS' if not bad and res['n'] > 5000 else 'FAIL') + f"  R1 All {res['n']} Unit Test questions of {res['units']} units render without their keys" + (': ' + str(bad[:3]) if bad else ''))
    print(('PASS' if not errs else 'FAIL') + '  R2 No page errors')
    print(f"{2 - (1 if bad or res['n'] <= 5000 else 0) - (1 if errs else 0)}/2 passed")
    b.close()
