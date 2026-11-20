"""Render the A4 worksheet PDFs from the app's own print layout (needs the site served on BASE)."""
import os, sys
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); OUT = sys.argv[1] if len(sys.argv) > 1 else 'web/worksheets'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=os.environ.get('CHROME', '/usr/bin/google-chrome'))
    pg = b.new_page(viewport={'width': 1200, 'height': 900}); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1'); pg.wait_for_timeout(600)
    pg.evaluate("""(async()=>{ await Backend.signUp({email:'ws@example.com',password:'password123',name:'Worksheets',birthYear:2014,grade:'Year 7 / Grade 6',country:'GB',schoolOther:'Atomic'});
      await Core.boot(Core.C); })()"""); pg.wait_for_timeout(400)
    for s in ['3-1', '3-2', '3-3', '3-4']:
        pg.evaluate(f"location.hash='ws-{s}'"); pg.wait_for_timeout(800)
        pg.emulate_media(media='print'); n = pg.evaluate("document.querySelectorAll('.a4').length")
        pg.pdf(path=f'{OUT}/Atomic_S7_U3_Worksheet_{s}.pdf', format='A4', print_background=True, prefer_css_page_size=True, page_ranges=f'1-{n}')
        pg.emulate_media(media='screen'); print(s, n, 'pages')
    print('errors:', errs); b.close()
