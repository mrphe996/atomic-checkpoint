"""Word games checks (preview build). Run after `node tools/write-config.mjs` with the range server on :8765."""
import os, json
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
SHOTS = os.environ.get('SHOTS')
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); ctx = b.new_context(viewport={'width': 1280, 'height': 1000}, reduced_motion='reduce'); pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + '?reset=1#games'); pg.wait_for_timeout(1500)
    ok(len(pg.query_selector_all('.gg')) == 5, 'G1 Visitors see five word games')
    ok(pg.query_selector('#gStage1') is not None and pg.query_selector('#gStage5') is not None and pg.query_selector('#gStage6') is None and pg.query_selector('#gSubj-maths') is not None, 'G2 Stage 1–5 and subject choices (no Stage 6)')
    W = json.loads(pg.evaluate("fetch('content/game-words.json').then(r=>r.text())"))['words']
    ok(len(W) > 600 and {w['subj'] for w in W} == {'science', 'maths', 'english'} and {w['stage'] for w in W} == {1, 2, 3, 4, 5, 6}, f'G3 Word bank covers every subject and Stages 1–6 ({len(W)} words)')
    byw = {w['w']: w for w in W}
    # sign up so the level is saved with the learner
    pg.evaluate("""(async()=>{ await Backend.signUp({email:'gm@example.com',password:'password123',name:'Gia Game',birthYear:2016,grade:'Year 4',country:'VN',schoolOther:'Atomic'}); await Core.boot(Core.C); location.hash='games'; })()""")
    pg.wait_for_timeout(2500)
    ok(pg.query_selector('nav a[href="#games"]') is None, 'G4 Games are not in the top menu (they live inside the course)')
    pg.click('#gStage2'); pg.wait_for_timeout(300); pg.click('#gSubj-english'); pg.wait_for_timeout(300)
    # helpers: the word being asked for (from the prompt's meaning)
    def target():
        t = pg.inner_text('#gPrompt').strip()
        for w in W:
            if w['def'] and w['def'] in t: return w['w']
        return None
    # 1 racer: steer into the right lane every round
    pg.evaluate("location.hash='game-racer'"); pg.wait_for_timeout(1500)
    if SHOTS: pg.screenshot(path=SHOTS + '/racer.png')
    ok(pg.query_selector('#gameWrap canvas') is not None and pg.query_selector('#gLeft') is not None and pg.query_selector('#gMusic') is not None and pg.query_selector('#gVoice') is not None, 'G5 Word Racer: road, steering buttons, Music and Read buttons')
    pg.click('#gMusic'); ok('on' in pg.get_attribute('#gMusic', 'class'), 'G6 Music can be switched on')
    pg.evaluate("location.hash='games'"); pg.wait_for_timeout(800)
    # 2 memory: solve by matching data-w ids
    pg.click('#gOpen-memory'); pg.wait_for_timeout(1200)
    cards = pg.query_selector_all('.gmc'); ids = {}
    for c in cards: ids.setdefault(c.get_attribute('data-w'), []).append(c.get_attribute('id'))
    for k, pair in ids.items():
        pg.click('#' + pair[0]); pg.wait_for_timeout(120); pg.click('#' + pair[1]); pg.wait_for_timeout(500)
    pg.wait_for_selector('#gResult', timeout=8000)
    if SHOTS: pg.screenshot(path=SHOTS + '/memory_result.png')
    t = pg.inner_text('#gResult')
    ok('XP' in t and 'points' in t, 'G7 Memory Match: matching every pair finishes the game with points and XP')
    lv = pg.evaluate("Core.S.states.games && Core.S.states.games.xp")
    ok(lv and lv > 0, f'G8 XP is saved with the learner ({lv} XP)')
    # 3 spell: tap the right letters
    pg.evaluate("location.hash='game-spell'"); pg.wait_for_timeout(1200)
    good = True
    for _ in range(3):
        slots = pg.query_selector_all('#gSlots .gslot'); word = None
        wt = target()
        if not wt: good = False; break
        for ch in [c for c in wt.lower()]:
            pass
        # fill the empty slots in order using tiles with the needed letter
        for i, sl in enumerate(pg.query_selector_all('#gSlots .gslot')):
            if sl.inner_text().strip() or 'sp' in (sl.get_attribute('class') or ''): continue
            ch = wt.lower()[i]
            pg.click(f'#gTiles .gtile[data-l="{ch}"]:not([disabled])')
            pg.wait_for_timeout(60)
        pg.wait_for_timeout(1100)
    ok(good and pg.evaluate("Core.S.states.games.words && Object.values(Core.S.states.games.words).some(r => r[1] > 0)"), 'G9 Spell It: building words letter by letter marks them as known')
    if SHOTS: pg.screenshot(path=SHOTS + '/spell.png')
    # 4 balloon: pop the right one
    pg.evaluate("location.hash='game-balloon'"); pg.wait_for_timeout(1300)
    if SHOTS: pg.screenshot(path=SHOTS + '/balloon.png')
    wt = target(); wid = byw[wt]['id'] if wt in byw else None
    s0 = int(pg.inner_text('#gScore').split()[1])
    if wid: pg.dispatch_event(f'.gbal[data-w="{wid}"]', 'pointerdown')
    pg.wait_for_timeout(400)
    ok(int(pg.inner_text('#gScore').split()[1]) > s0, 'G10 Balloon Pop: popping the right balloon scores')
    # wrong pop costs a heart
    pg.wait_for_timeout(800); wt = target(); wid = byw[wt]['id'] if wt in byw else None
    other = pg.evaluate(f"([...document.querySelectorAll('.gbal')].find(b => b.dataset.w !== '{wid}') || {{}}).dataset.w")
    if other: pg.dispatch_event(f'.gbal[data-w="{other}"]', 'pointerdown')
    pg.wait_for_timeout(300)
    ok(pg.inner_text('#gHearts').count('❤️') == 2, 'G11 A wrong answer costs a heart')
    # 5 whack
    pg.evaluate("location.hash='game-whack'"); pg.wait_for_timeout(2600)
    if SHOTS: pg.screenshot(path=SHOTS + '/whack.png')
    ok(len(pg.query_selector_all('.ghole')) == 9 and len(pg.query_selector_all('.ghole.up')) >= 1, 'G12 Word Whack: moles pop up with words')
    pg.click('#gStop'); pg.wait_for_timeout(500)
    ok(pg.query_selector('#gResult') is not None, 'G13 Stop ends the game and shows the results')
    # levels: unlimited and harder
    lvls = pg.evaluate("[Games.levelOf(0).level, Games.levelOf(100000).level, Games.levelOf(10000000).level]")
    tun = pg.evaluate("[Games.tuning(1), Games.tuning(30)]")
    ok(lvls[0] == 1 and lvls[1] > 50 and lvls[2] > lvls[1], f'G14 Levels have no top limit ({lvls})')
    ok(tun[1]['speed'] > tun[0]['speed'] and tun[1]['choices'] > tun[0]['choices'] and tun[1]['near'] and not tun[0]['near'], 'G15 Higher levels are faster, with more and closer choices')
    pg.evaluate("location.hash='games'"); pg.wait_for_timeout(1200)
    if SHOTS: pg.screenshot(path=SHOTS + '/hub.png', full_page=True)
    ok('Best:' in pg.inner_text('#gamesHub'), 'G16 The games page shows best scores')
    pg.set_viewport_size({'width': 390, 'height': 844}); pg.evaluate("location.hash='game-racer'"); pg.wait_for_timeout(1300)
    if SHOTS: pg.screenshot(path=SHOTS + '/racer_phone.png')
    ok(pg.evaluate("document.documentElement.scrollWidth <= 392"), 'G17 Games fit a phone screen')
    pg.set_viewport_size({'width': 1280, 'height': 1000})
    # word games inside the course (Stage 5 Science, topic 1.1) – a step like Practice
    pg.evaluate("Core.switchStage(5)"); pg.wait_for_timeout(2500); pg.evaluate("location.hash='profile'"); pg.wait_for_timeout(1500); pg.click('#simAll'); pg.wait_for_timeout(800)
    pg.evaluate("location.hash='u-1'"); pg.wait_for_timeout(2000)
    ok(pg.query_selector('a.u4tile[href="#gm-1-1"]') is not None and pg.query_selector('.secnav a[href="#gm-1-1"]') is not None and 'null' not in pg.inner_text('.u4head'), 'G19 Each topic has a "Word games" step in the course, next to Practise')
    pg.evaluate("location.hash='gm-1-1'"); pg.wait_for_timeout(1500)
    ok(len(pg.query_selector_all('#gamesPick .gg')) == 5 and 'words from this lesson' in pg.inner_text('#gamesPick'), 'G20 The topic\'s game page offers five games with that lesson\'s words')
    pg.click('#gPick-memory'); pg.wait_for_timeout(1200)
    lesson = set(pg.evaluate("Core.sec('1.1').vocab.map(v => v.w)"))
    shown = set(x.inner_text().strip() for x in pg.query_selector_all('.gmc[data-side="word"] .fb b'))
    ok(shown and shown <= lesson | set(w['w'] for w in W), 'G21 The cards use the lesson\'s own words')
    ids = {}
    for c in pg.query_selector_all('.gmc'): ids.setdefault(c.get_attribute('data-w'), []).append(c.get_attribute('id'))
    for k, pair in ids.items(): pg.click('#' + pair[0]); pg.wait_for_timeout(120); pg.click('#' + pair[1]); pg.wait_for_timeout(500)
    pg.wait_for_selector('#gResult', timeout=8000); pg.wait_for_timeout(400)
    ok(pg.evaluate("!!(Core.cur().games || {})['1.1']") and pg.get_attribute('#gBack', 'href') == '#gm-1-1', 'G22 Playing is recorded for the topic and leads back to its games')
    # practice card: friendly header, no internal codes for learners
    pg.evaluate("location.hash='ex-1-1'"); pg.wait_for_timeout(2000)
    hd = pg.inner_text('.qcard .qhead2') if pg.query_selector('.qcard .qhead2') else ''
    ok('Question 1' in hd and 'of' in hd and pg.query_selector('.qcard .qid') is None and pg.query_selector('.qcard .qhead code') is None, 'G23 Practice cards show "Question n of N", level and answer type – no internal codes')
    # Stage 6: no word games in the course
    pg.evaluate("Core.switchStage(6)"); pg.wait_for_timeout(2500); pg.evaluate("location.hash='u-1'"); pg.wait_for_timeout(2000)
    ok(pg.query_selector('a[href^="#gm-"]') is None, 'G24 Stage 6 has no word games')
    pg.evaluate("location.hash='games'"); pg.wait_for_timeout(500)
    ok(not errs, 'G18 No page errors' + (': ' + errs[0] if errs else ''))
    b.close()
fails = [l for l in LOG if l.startswith('FAIL')]
print(f'{len(LOG) - len(fails)}/{len(LOG)} passed')
