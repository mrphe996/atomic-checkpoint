"""Primary Science Stages 5 and 6: animated lessons, listening and read-aloud word checks, the word bank and the experiment room.
Run with the default config: `node tools/write-config.mjs`."""
import os, sys
from playwright.sync_api import sync_playwright
BASE = os.environ.get('BASE', 'http://localhost:8765/'); LOG = []
def ok(c, m): LOG.append(('PASS' if c else 'FAIL') + '  ' + m); print(LOG[-1])
# a stand-in for the browser's speech recognition: it "hears" whatever window.__heard holds
FAKE_SR = """window.__heard = 'heart'; window.webkitSpeechRecognition = class { start() { setTimeout(() => { const alt = [{ transcript: window.__heard }]; alt.length = 1; this.onresult && this.onresult({ results: [alt] }); this.onend && this.onend(); }, 30); } stop() {} }; window.SpeechRecognition = window.webkitSpeechRecognition;"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(reduced_motion='reduce', viewport={'width': 1300, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.add_init_script(FAKE_SR)
    pg.goto(BASE + '?reset=1'); pg.wait_for_selector('#heroStart')
    pg.evaluate("location.hash='signup'"); pg.wait_for_timeout(300)
    pg.fill('#suName', 'Pia Primary'); pg.fill('#suEmail', 'pia@example.com'); pg.fill('#suPw', 'password123'); pg.click('#suNext1'); pg.wait_for_selector('#suYear')
    pg.select_option('#suYear', index=3); pg.select_option('#suGrade', index=2); pg.click('#suNext2'); pg.wait_for_selector('#suCountry')
    pg.select_option('#suCountry', 'SG'); pg.wait_for_timeout(200); pg.select_option('#suSchool', index=1); pg.check('#suTerms'); pg.click('#suBtn'); pg.wait_for_function("location.hash==='#home'")
    ok(pg.query_selector('#stageSwitch .sw[data-stage="6"]') is not None, 'P1 The course switcher offers Primary Science Stage 6')
    pg.evaluate("location.hash='checkout-6'"); pg.wait_for_timeout(600); pg.click('#payBtn'); pg.wait_for_function("Core.STAGE===6", timeout=10000); pg.wait_for_timeout(600)
    ok(pg.evaluate("Core.IS_PRIMARY && Core.unitCount()===6 && Core.INDEX.units.every(u => u.ready)"), 'P2 Stage 6 has 6 units, all open')
    s = pg.evaluate("Core.C.sections.map(s => ({id: s.id, req: s.req.length, say: s.req.filter(q => q.type==='say').length, aud: s.req.filter(q => q.audio && q.type!=='say').length, lab: !!s.lab, vocab: (s.vocab||[]).length, stops: s.stops.length, src: s.video.src}))")
    ok(len(s) == 4 and all(x['req'] == 8 and x['say'] == 4 and x['aud'] == 4 and x['lab'] and x['vocab'] >= 7 and x['stops'] >= 2 for x in s), 'P3 Every topic: video with pause questions, 4 listening + 4 say-the-word Core, word bank and experiment room')
    st = pg.evaluate("fetch(Core.C.sections[0].video.src, {method:'HEAD'}).then(r => r.status)"); ok(st == 200, 'P4 The animated lesson video is served')
    pg.evaluate("location.hash='u-1'"); pg.wait_for_timeout(800)
    ok('Listen' in pg.inner_text('#topic-1-1') and 'Experiment' in pg.inner_text('#topic-1-1'), 'P5 The unit page shows Watch, Listen & say and Experiment for each topic')
    pg.evaluate("location.hash='ex-1-1'"); pg.wait_for_timeout(600)
    ok(pg.query_selector('#wordBank') is None and 'locked' in pg.inner_text('#main').lower(), 'P6 Practice is locked until the video is watched')
    pg.evaluate("(()=>{const st=Core.cur(); const s=Core.C.sections[0]; const vs=Core.vstate(st,s.id); vs.completed=true; s.stops.forEach(x=>vs.stops[x.id]={done:true,tries:1}); Core.persist();})()")
    pg.evaluate("location.hash='ex-1-1'"); pg.wait_for_timeout(600); pg.evaluate("location.hash='home'"); pg.wait_for_timeout(300); pg.evaluate("location.hash='ex-1-1'"); pg.wait_for_timeout(800)
    ok(pg.query_selector('#wordBank') is not None and len(pg.query_selector_all('#wordBank .wcard')) == 9, 'P7 The word bank shows the 9 words of 1.1 with sound')
    ok(pg.query_selector('.audiobar .listen') is not None, 'P8 Listening questions have Listen and Slowly buttons')
    ok(pg.evaluate("Core.secLock(Core.cur(), Core.C.sections[1]) !== null"), 'P9 Lesson 1.2 is locked before the word checks are done')
    # answer the 4 listening questions
    for i in range(4):
        q = pg.evaluate(f"Core.C.sections[0].req[{i}]")
        if q['type'] == 'mcq':
            right = [o['t'] for o in q['options'] if o['ok']][0]; pg.click(f'.qcard .opt span:text-is("{right}")')
        else: pg.fill('.qcard input[type=text]', q['accept'][0])
        pg.click('.qcard .btn.primary'); pg.wait_for_timeout(300); pg.click('#nextQ'); pg.wait_for_timeout(500)
    ok(pg.evaluate("[0,1,2,3].every(i => (Core.cur().items[Core.C.sections[0].req[i].id]||{}).ok)"), 'P10 The four listening questions can be answered and are marked')
    # say-the-word: right word first time
    w = pg.evaluate("Core.C.sections[0].req[4].word"); pg.evaluate(f"window.__heard = 'my {w}'")
    ok(pg.query_selector('.micbtn') is not None and pg.inner_text('.sayword') == w, f'P11 Say-the-word shows the word “{w}” and a microphone button')
    pg.click('.micbtn'); pg.wait_for_timeout(400)
    ok(pg.evaluate("(Core.cur().items[Core.C.sections[0].req[4].id]||{}).ok === true") and 'Perfect' in pg.inner_text('.qcard .fb'), 'P12 Saying the word correctly passes it')
    # wrong three times: the teacher reads it slowly, then the learner may carry on
    pg.click('#nextQ'); pg.wait_for_timeout(500); pg.evaluate("window.__heard = 'banana'")
    for _ in range(3): pg.click('.micbtn'); pg.wait_for_timeout(400)
    r = pg.evaluate("Core.cur().items[Core.C.sections[0].req[5].id]")
    ok(r['done'] and not r['ok'] and r.get('assisted') and r['tries'] == 3 and 'Listen' in pg.inner_text('.qcard .fb'), 'P13 After 3 tries the word is read slowly and the learner can carry on (marked as helped)')
    # no speech recognition: listen and type instead
    pg.evaluate("delete window.webkitSpeechRecognition; delete window.SpeechRecognition"); pg.click('#nextQ'); pg.wait_for_timeout(500)
    w7 = pg.evaluate("Core.C.sections[0].req[6].word")
    ok(pg.query_selector('.micbtn') is None and pg.query_selector('.qcard input[type=text]') is not None, 'P14 Without speech recognition, the learner listens and types the word')
    pg.fill('.qcard input[type=text]', w7); pg.click('.qcard .numrow .btn'); pg.wait_for_timeout(300)
    ok(pg.evaluate("(Core.cur().items[Core.C.sections[0].req[6].id]||{}).ok === true"), 'P15 Typing the word correctly passes it')
    pg.click('#nextQ'); pg.wait_for_timeout(500); w8 = pg.evaluate("Core.C.sections[0].req[7].word"); pg.fill('.qcard input[type=text]', w8); pg.click('.qcard .numrow .btn'); pg.wait_for_timeout(400)
    ok(pg.evaluate("Core.secLock(Core.cur(), Core.C.sections[1]) === null"), 'P16 Finishing the word checks unlocks lesson 1.2')
    ok(pg.evaluate("Primary.heardOk('fertilisation', ['fertilization']) && Primary.heardOk('breathing rate', ['my breathing rate']) && !Primary.heardOk('heart', ['hat'])"), 'P17 Speech matching accepts US spelling and extra words, rejects a different word')
    # experiment room
    pg.evaluate("location.hash='lab-1-2'"); pg.wait_for_timeout(800)
    ok(pg.query_selector('.labrange') is not None, 'P18 The 1.2 virtual lab has a working lung model')
    pg.eval_on_selector('.labrange', "e => { e.value = 100; e.dispatchEvent(new Event('input')); e.value = 0; e.dispatchEvent(new Event('input')); }"); pg.wait_for_timeout(400)
    ok(len(pg.query_selector_all('.labqs .qcard')) == 3, 'P19 Using the model opens the lab questions')
    pg.evaluate("location.hash='lab-1-4'"); pg.wait_for_timeout(800)
    pg.evaluate("(()=>{const st=Core.cur(); Core.C.sections.forEach(s=>{const vs=Core.vstate(st,s.id); vs.completed=true; s.stops.forEach(x=>vs.stops[x.id]={done:true,tries:1}); s.req.forEach(q=>st.items[q.id]={done:true,ok:true,tries:1});}); Core.persist();})()")
    pg.evaluate("location.hash='home'"); pg.wait_for_timeout(300); pg.evaluate("location.hash='lab-1-4'"); pg.wait_for_timeout(800)
    for k in range(3):
        pg.click(f'.labcard .btnrow .chip >> nth={k}'); pg.wait_for_timeout(1700)
        n = pg.inner_text('.labcard .labcount'); pg.fill('.labcard .numrow input', n); pg.click('.labcard .numrow .btn'); pg.wait_for_timeout(300)
    ok(len(pg.query_selector_all('.labtable tr')) == 4 and len(pg.query_selector_all('.labqs .qcard')) == 3, 'P20 Glitter lab: three ways of washing are recorded and the questions open')
    pg.click('.labroom [role=tab] >> nth=1'); pg.wait_for_timeout(500)
    ins = pg.query_selector_all('.labtable input'); [i.fill('40') or i.dispatch_event('change') for i in ins]; pg.wait_for_timeout(300)
    ok('Results recorded' in pg.inner_text('.labroom') and len(pg.query_selector_all('.labqs .qcard')) == 1, 'P21 Home experiment: results are recorded and its question opens')
    # the reading-a-scale lab (3.1 crystal sizes): run each test, read the scale and record it
    pg.evaluate("location.hash='lab-3-1'"); pg.wait_for_timeout(1200)
    vals = pg.evaluate("Core.C.sections.find(s => s.id==='3.1').lab.v.conds.map(c => c.val)")
    for k, v in enumerate(vals):
        pg.click(f'.labcard .btnrow .chip >> nth={k}'); pg.wait_for_timeout(1400)
        if k == 0: pg.fill('.labcard .numrow input', str(v + 30)); pg.click('.labcard .numrow .btn'); pg.wait_for_timeout(200); ok('Not quite' in pg.inner_text('.labcard'), 'P23 Scale lab: a wrong reading is caught')
        pg.fill('.labcard .numrow input', str(v)); pg.click('.labcard .numrow .btn'); pg.wait_for_timeout(250)
    ok(len(pg.query_selector_all('.labtable tr')) == 4 and len(pg.query_selector_all('.labbars .lb')) == 3 and len(pg.query_selector_all('.labqs .qcard')) == 2, 'P24 Scale lab: readings fill the table and bar chart, and the questions open')
    # the sorting lab (4.1 who is who in the food web)
    pg.evaluate("location.hash='lab-4-1'"); pg.wait_for_timeout(1200)
    items = pg.evaluate("Core.C.sections.find(s => s.id==='4.1').lab.v.items.map(i => [i.t, i.g])")
    t0, g0 = items[0]; wrong = (g0 + 1) % 3
    pg.click(f'.sortcard:has-text("{t0}")'); pg.click(f'.sortbin >> nth={wrong}'); pg.wait_for_timeout(150)
    ok('Not “' in pg.inner_text('.labcard'), 'P25 Sorting lab: a card put in the wrong group is explained')
    for t, g in items:
        pg.click(f'.sortpool .sortcard:has-text("{t}")'); pg.click(f'.sortbin >> nth={g}'); pg.wait_for_timeout(80)
    ok('All sorted correctly' in pg.inner_text('.labcard') and len(pg.query_selector_all('.labqs .qcard')) == 2, 'P26 Sorting lab: when every card is sorted the questions open')
    ok(pg.evaluate("Core.INDEX.units.length===6") and pg.evaluate("fetch('media/s6/w/igneous-rock.mp3', {method:'HEAD'}).then(r => r.status)") == 200, 'P27 Unit 3 word audio is served')
    # no speaking inside the video (removed at the owner's request): videos only stop for pause questions
    ns = pg.evaluate("Core.C.sections.reduce((n, s) => n + s.stops.filter(x => x.kind==='say').length, 0)")
    pg.evaluate("location.hash='u-2'"); pg.wait_for_timeout(900)
    ns += pg.evaluate("Core.C.sections.reduce((n, s) => n + s.stops.filter(x => x.kind==='say').length, 0)")
    ok(ns == 0, 'P28 The lesson videos have no speaking stops, only pause questions')
    kinds = pg.evaluate("[...new Set(Core.C.sections.find(s => s.id==='2.1').prac.map(q => q.type))]")
    n = pg.evaluate("Core.C.sections.find(s => s.id==='2.1').prac.length")
    ok(n >= 28 and all(k in kinds for k in ['say', 'match', 'cloze', 'order', 'short', 'grid', 'mcq']), f'P31 Practice is larger and varied: {n} questions, types {sorted(kinds)}')
    # worksheet prints practice questions (not the speaking checks)
    pg.evaluate("location.hash='ws-1-1'"); pg.wait_for_timeout(900)
    # ---- Primary Science Stage 5 ----
    pg.evaluate("location.hash='home'"); pg.wait_for_timeout(700)
    ok(pg.query_selector('#stageSwitch .sw[data-stage="5"]') is not None, 'P32 The course switcher offers Primary Science Stage 5')
    pg.evaluate("location.hash='checkout-5'"); pg.wait_for_timeout(600); pg.click('#payBtn'); pg.wait_for_function("Core.STAGE===5", timeout=10000); pg.wait_for_timeout(800)
    ok(pg.evaluate("Core.IS_PRIMARY && Core.unitCount()===6 && Core.INDEX.units.every(u => u.ready)"), 'P33 Stage 5 has 6 units, all open')
    tot = 0; bad = []
    for u in range(1, 7):
        pg.evaluate(f"location.hash='u-{u}'"); pg.wait_for_timeout(700)
        s5 = pg.evaluate("Core.C.sections.map(s => ({id: s.id, req: s.req.length, say: s.req.filter(q => q.type==='say').length, lab: !!s.lab, vocab: (s.vocab||[]).length, stops: s.stops.length, says: s.stops.filter(x => x.kind==='say').length, prac: s.prac.length, src: s.video.src}))")
        tot += len(s5); bad += [x['id'] for x in s5 if not (x['req'] == 8 and x['say'] == 4 and x['lab'] and x['vocab'] >= 5 and x['stops'] >= 2 and x['says'] == 0 and x['prac'] >= 24 and '/s5/' in x['src'])]
    ok(tot == 24 and not bad, f'P34 All 24 Stage 5 topics have a video with pause questions (no speaking stops), 8 Core checks, a lab, a word bank and 24+ practice questions (problems: {bad})')
    st = pg.evaluate("fetch(Core.C.sections[0].video.src, {method:'HEAD'}).then(r => r.status)")
    wa = pg.evaluate("Promise.all(['media/s5/w/pollination.mp3','media/s5/w/d-camouflage.mp3','media/s5/w/e-upthrust.mp3'].map(u => fetch(u, {method:'HEAD'}).then(r => r.status)))")
    ok(st == 200 and wa == [200, 200, 200], 'P35 Stage 5 videos and word audio are served')
    pg.evaluate("location.hash='u-5'"); pg.wait_for_timeout(700)
    pg.evaluate("(()=>{const st=Core.cur(); Core.C.sections.forEach(s=>{const vs=Core.vstate(st,s.id); vs.completed=true; s.stops.forEach(x=>vs.stops[x.id]={done:true,tries:1}); s.req.forEach(q=>st.items[q.id]={done:true,ok:true,tries:1});}); Core.persist();})()")
    tl = pg.evaluate("(Core.C.sections.find(s => s.lab && s.lab.v && s.lab.v.kind==='test') || {}).id")
    if tl:
        pg.evaluate(f"location.hash='lab-{tl.replace('.', '-')}'"); pg.wait_for_timeout(1200)
        vals = pg.evaluate(f"Core.C.sections.find(s => s.id==='{tl}').lab.v.conds.map(c => c.val)")
        for k, v in enumerate(vals):
            pg.click(f'.labcard .btnrow .chip >> nth={k}'); pg.wait_for_timeout(1400)
            pg.fill('.labcard .numrow input', str(v)); pg.click('.labcard .numrow .btn'); pg.wait_for_timeout(250)
    ok(tl and len(pg.query_selector_all('.labtable tr')) == len(vals) + 1 and len(pg.query_selector_all('.labqs .qcard')) >= 1, f'P36 Stage 5 scale lab ({tl}) can be run and its questions open')
    # ---- answering on the video itself, also in full screen ----
    pg.evaluate("location.hash='u-1'"); pg.wait_for_timeout(800)
    pg.evaluate("(()=>{const st=Core.cur(); Core.C.sections.forEach(s=>{const vs=Core.vstate(st,s.id); s.req.forEach(q=>st.items[q.id]={done:true,ok:true,tries:1}); if (s.id==='1.2') { vs.completed=false; vs.pos=0; vs.stops={}; } else { vs.completed=true; s.stops.forEach(x=>vs.stops[x.id]={done:true,tries:1}); }}); Core.persist();})()")
    pg.evaluate("location.hash='v-1-2'"); pg.wait_for_timeout(1500)
    pg.wait_for_function("document.querySelector('video') && document.querySelector('video').readyState >= 1", timeout=15000)
    stops = pg.evaluate("Core.C.sections.find(s => s.id==='1.2').stops.map(x => ({t: x.t, type: x.q.type, ok: (x.q.options||[]).findIndex(o => o.ok), opts: (x.q.options||[]).map(o => o.t)}))")
    def reach(t):
        pg.evaluate(f"(() => {{ const v = document.querySelector('video'); v.muted = true; v.currentTime = {t}; v.dispatchEvent(new Event('timeupdate')); }})()"); pg.wait_for_timeout(700)
    def answer(q):
        if q['type'] == 'mcq': pg.click(f'.qlayer .opt:has-text("{q["opts"][q["ok"]][:30]}")')
        pg.click('.qlayer .card.stop .btn.primary'); pg.wait_for_timeout(500)
    reach(stops[0]['t'])
    ok(pg.query_selector('.player .qlayer:not([hidden]) .card.stop') is not None and pg.query_selector('#main > .lesson .stoppanel .card.stop') is None, 'P37 The pause question opens on top of the video, not below it')
    ok(pg.query_selector('.qlayer .readme') is not None and pg.evaluate("document.querySelector('.qlayer .stop.kid') !== null"), 'P38 Young learners get large answer buttons and a “Read to me” button')
    answer(stops[0])
    ok(pg.query_selector('.qlayer #continueVideo') is not None, 'P39 After answering, “Keep watching” is on the video')
    pg.click('.qlayer #continueVideo'); pg.wait_for_timeout(500)
    ok(pg.evaluate("document.querySelector('.qlayer').hidden"), 'P40 “Keep watching” closes the question and goes back to the video')
    pg.click('.pwrap .ctrl .chip[aria-label="Full screen"]'); pg.wait_for_timeout(700)
    fsok = pg.evaluate("!!(document.fullscreenElement && document.fullscreenElement.classList.contains('pwrap')) || document.querySelector('.pwrap.fakefs') !== null")
    if len(stops) > 1: reach(stops[1]['t'])
    inside = pg.evaluate("(() => { const f = document.fullscreenElement || document.querySelector('.pwrap.fakefs'); return !!(f && f.querySelector('.qlayer:not([hidden]) .card.stop')); })()")
    ok(fsok and inside, 'P41 In full screen the next question appears inside the full-screen video')
    if len(stops) > 1: answer(stops[1]); pg.click('.qlayer #continueVideo'); pg.wait_for_timeout(300)
    pg.click('.pwrap .ctrl .chip[aria-label="Exit full screen"]'); pg.wait_for_timeout(600)
    ok(pg.evaluate("!document.fullscreenElement && !document.querySelector('.pwrap.fakefs')"), 'P42 The full-screen button turns into “Exit full screen” and leaves it')
    # ---- My word book ----
    pg.evaluate("location.hash='ex-1-1'"); pg.wait_for_timeout(1200)
    w0 = pg.evaluate("Core.C.sections[0].vocab[0].w")
    pg.click('#wordBank .wcard >> nth=0 >> .wsave'); pg.wait_for_timeout(300)
    ok(pg.evaluate("Words.has(Core.C.sections[0].vocab[0].w)") and '⭐ Saved' in pg.inner_text('#wordBank .wcard >> nth=0'), 'P43 Tapping ☆ Save on a word card keeps it in My word book')
    ok(pg.query_selector('nav a[href="#words"]') is not None, 'P44 Primary learners have “📒 My words” in the menu')
    pg.evaluate("location.hash='u-2'"); pg.wait_for_timeout(900); pg.evaluate("location.hash='words'"); pg.wait_for_timeout(900)
    ok(w0 in pg.inner_text('.wlist'), 'P45 My word book shows saved words from every unit (saved in Unit 1, opened from Unit 2)')
    pg.fill('.wentry textarea', 'yellow flowers make seeds'); pg.wait_for_timeout(900)
    ok(pg.evaluate(f"Words.list().find(x => x.w === {w0!r}).note") == 'yellow flowers make seeds', 'P46 A note can be written for a saved word')
    pg.fill('.waddform input >> nth=0', 'buzz'); pg.fill('.waddform input >> nth=1', 'the sound a bee makes'); pg.click('.waddform .wpic >> nth=4'); pg.click('.waddform .btn.primary'); pg.wait_for_timeout(700)
    ok(pg.evaluate("!!Words.list().find(x => x.w === 'buzz' && x.custom && x.emoji === '🐞')") and 'buzz' in pg.inner_text('.wlist'), 'P47 Learners can add their own word with a note and a picture')
    pg.click('.wtools .btn.gold'); pg.wait_for_timeout(700)
    ok(len(pg.query_selector_all('.wgame .pcard')) >= 2 and pg.query_selector('.wgame input') is None, 'P48 The word game uses picture cards to tap (no typing)')
    for _ in range(2):
        if pg.query_selector('.wgame.done'): break
        target = pg.evaluate("(() => { const q = document.querySelector('.wgame .qp').textContent; const all = Words.list(); return (all.find(x => q.includes(x.w)) || all.find(x => x.note && q.includes(x.note)) || {}).w || ''; })()")
        cards = pg.query_selector_all('.wgame .pcard'); pick = next((c for c in cards if target and c.inner_text().strip().endswith(target)), None)
        if pick is None:
            wl = pg.evaluate("Words.list().map(x => x.w)"); pick = next((c for c in cards if any(c.inner_text().strip().endswith(w) for w in wl)), cards[0])
        pick.click(); pg.wait_for_timeout(1700)
    ok(pg.query_selector('.wgame.done') is not None, 'P49 The game ends with a score and “Play again”')
    pg.goto(BASE + '#home'); pg.wait_for_timeout(2500)   # (not ?reset=1: that would wipe this browser's preview data)
    if pg.evaluate("location.hash") == '#signin' or pg.query_selector('#siEmail'):
        pg.evaluate("location.hash='signin'"); pg.wait_for_timeout(400); pg.fill('#siEmail', 'pia@example.com'); pg.fill('#siPw', 'password123'); pg.click('#siBtn'); pg.wait_for_timeout(1500)
        if pg.query_selector('.lpick, .learnerpick'): pg.click('.lpick button >> nth=0')
    pg.evaluate("location.hash='words'"); pg.wait_for_timeout(1500)
    ok(w0 in pg.inner_text('#main') and 'buzz' in pg.inner_text('#main'), 'P50 Saved words are still there after logging in again')
    ok(not errs, 'P22 No page errors ' + '; '.join(errs[:3])); b.close()
f = [l for l in LOG if l.startswith('FAIL')]; print(f'{len(LOG)-len(f)}/{len(LOG)} passed'); sys.exit(1 if f else 0)
