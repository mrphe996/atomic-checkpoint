"""Phone layout: every main page at 320, 360 and 390 px wide (touch phone, light and dark).
Checks that nothing widens the page past the screen, that no button or link is cut off,
that the header fits, and that buttons and links do not sit on top of each other.
Run with the default config: `node tools/write-config.mjs`."""
import os
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])

CHECK = r"""
(() => {
  const vw = document.documentElement.clientWidth, bad = [];
  if (innerWidth > vw + 1 || document.documentElement.scrollWidth > vw + 1) bad.push('page is ' + document.documentElement.scrollWidth + 'px wide');
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e); return r.width > 1 && r.height > 1 && s.visibility !== 'hidden' && +s.opacity > 0.2; };
  const name = e => (e.id ? '#' + e.id : e.tagName.toLowerCase() + (typeof e.className === 'string' && e.className ? '.' + e.className.trim().split(/\s+/)[0] : '')) + ' «' + (e.innerText || e.getAttribute('aria-label') || '').trim().slice(0, 24) + '»';
  const scroller = e => { for (let n = e.parentElement; n && n !== document.body; n = n.parentElement) if (/(auto|scroll)/.test(getComputedStyle(n).overflowX)) return true; return false; };
  const ctl = [...document.querySelectorAll('a.btn,button,.btn,input,select,header a,header button')].filter(e => vis(e) && !e.closest('.confetti,.toast,.xptoast,.lvtoast,.fig,.player,.a4'));
  for (const e of ctl) {
    const r = e.getBoundingClientRect();
    if (r.right > vw + 1 && !scroller(e)) bad.push(name(e) + ' runs off the screen');
    if (/^(A|BUTTON)$/.test(e.tagName) && (e.innerText || '').trim() && e.scrollWidth > e.clientWidth + 2 && getComputedStyle(e).overflowX !== 'visible') bad.push(name(e) + ' text is cut off');
  }
  const fixed = e => { for (let n = e; n && n !== document.body; n = n.parentElement) if (/fixed|sticky/.test(getComputedStyle(n).position)) return true; return false; };
  const solid = ctl.filter(e => /^(A|BUTTON|INPUT|SELECT)$/.test(e.tagName) && !fixed(e) && getComputedStyle(e).display !== 'inline').map(e => [e, e.getBoundingClientRect()]);
  for (let i = 0; i < solid.length; i++) for (let j = i + 1; j < solid.length; j++) {
    const [a, ra] = solid[i], [b, rb] = solid[j]; if (a.contains(b) || b.contains(a)) continue;
    const ox = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left), oy = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
    if (ox > 4 && oy > 4) bad.push(name(a) + ' overlaps ' + name(b));
  }
  return [...new Set(bad)].slice(0, 6);
})()
"""
def signup(pg):
    pg.evaluate("location.hash='signup'"); pg.wait_for_timeout(300)
    pg.fill('#suName', 'Mo Bile'); pg.fill('#suEmail', 'mobile@example.com'); pg.fill('#suPw', 'password123'); pg.click('#suNext1'); pg.wait_for_selector('#suYear')
    pg.select_option('#suYear', index=3); pg.select_option('#suGrade', index=2); pg.click('#suNext2'); pg.wait_for_selector('#suCountry')
    pg.select_option('#suCountry', 'SG'); pg.wait_for_timeout(200); pg.select_option('#suSchool', index=1); pg.check('#suTerms')
    ok(not pg.evaluate(CHECK), 'M0 The last sign-up step fits the phone screen')
    pg.click('#suBtn'); pg.wait_for_function("location.hash==='#home'"); pg.wait_for_timeout(500)
def unlock(pg):
    pg.evaluate("(()=>{const st=Core.cur();for(const s of Core.C.sections){st.video[s.id]={completed:true,stops:Object.fromEntries(s.stops.map(x=>[x.id,{done:true,ok:true,tries:1}]))}}Core.persist()})()")

GUEST = ['home', 'signin', 'signup', 'pricing', 'help', 'courses', 'stage-7', 'u-1', 'v-1-1', 'tests', 'bank', 'board']
LEARN = ['home', 'u-1', 'v-1-1', 'ex-1-1', 'ws-1-1', 'tests', 'test', 'final', 'checkpoint', 'map', 'profile', 'bank', 'board', 'cert', 'settings', 'words']
PRIM = ['home', 'u-1', 'v-1-1', 'ex-1-1', 'words', 'tests']
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); errs = []
    for w, dark in [(320, False), (360, True), (390, False)]:
        ctx = b.new_context(viewport={'width': w, 'height': 760}, is_mobile=True, has_touch=True, reduced_motion='reduce')
        pg = ctx.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto(BASE + '?reset=1'); pg.wait_for_selector('#heroStart')
        if dark: pg.evaluate("AtomicTheme.setMode('dark')")
        def run(tag, routes):
            for r in routes:
                pg.evaluate(f"location.hash='{r}'"); pg.wait_for_timeout(700)
                if pg.query_selector('#leaveAnyway'): pg.click('#leaveAnyway'); pg.wait_for_timeout(500); pg.evaluate(f"location.hash='{r}'"); pg.wait_for_timeout(700)
                bad = pg.evaluate(CHECK); ok(not bad, f'M {w}px {"dark" if dark else "light"} {tag} #{r} fits the phone' + (': ' + '; '.join(bad) if bad else ''))
        run('guest', GUEST)
        ok(pg.is_visible('#signUpLink') and pg.evaluate("document.querySelector('#signUpLink').getBoundingClientRect().right <= document.documentElement.clientWidth"), f'M {w}px Guest header shows Log in and Sign up in full')
        pg.click('.menu-btn'); pg.wait_for_timeout(200)
        ok(pg.is_visible('.mainnav .navmode'), f'M {w}px The light/dark switch is in the phone menu')
        pg.click('.menu-btn')
        signup(pg); unlock(pg)
        if dark: pg.evaluate("AtomicTheme.setMode('dark')")
        run('learner', LEARN)
        pg.evaluate("location.hash='checkout-3'"); pg.wait_for_timeout(700)
        if pg.query_selector('#leaveAnyway'): pg.click('#leaveAnyway'); pg.wait_for_timeout(700)   # the practice room asks before letting a learner leave
        pg.click('#payBtn'); pg.wait_for_function("Core.STAGE===3", timeout=8000); pg.wait_for_timeout(700); unlock(pg)
        run('stage 3', PRIM)
        ctx.close()
    ok(not errs, 'M9 No page errors' + (': ' + errs[0][:120] if errs else ''))
    b.close()
print(f"{sum(1 for l in LOG if l.startswith('PASS'))}/{len(LOG)} passed")
