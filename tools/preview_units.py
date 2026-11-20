"""Build the v4 design-sample unit pages (web/preview/unitNN.html) from the real course content.
Progress figures are illustrative only (demo learner)."""
import json, html, os

W = os.path.join(os.path.dirname(__file__), '..', 'web')
IDX = json.load(open(f'{W}/content/stage7.json'))
E = html.escape

# ---- illustrative learner progress -------------------------------------------------
DEMO = {
    1: dict(state='done', studied='4 h 52 min', score=86, secs={}),
    2: dict(state='done', studied='6 h 08 min', score=77, secs={}),
    3: dict(state='go', studied='1 h 12 min', score=None, secs={'3.1': 'done', '3.2': 'go'}),
    4: dict(state='new', studied='0 min', score=None, secs={}),
}

def fmt(sec):
    sec = round(sec); return f'{sec // 60}:{sec % 60:02d}'

def hrs(mins):
    return f'≈ {mins / 60:.1f} h'

# ---- illustrations (all original) --------------------------------------------------
ART = {
1: '''<rect width="380" height="380" fill="#EAF1FC"/>
<g stroke="#0E1B3D" stroke-width="5" stroke-linejoin="round" fill="#fff">
<path d="M150 70h50v70l55 120a20 20 0 0 1-18 28H113a20 20 0 0 1-18-28l55-120z"/>
<path d="M240 170h80v140a12 12 0 0 1-12 12h-56a12 12 0 0 1-12-12z"/></g>
<path d="M104 250l40-80h62l40 80a12 12 0 0 1-11 18H115a12 12 0 0 1-11-18z" fill="#4F7CE8" fill-opacity=".55"/>
<rect x="244" y="230" width="72" height="88" rx="8" fill="#F3BF69" fill-opacity=".8"/>
<g fill="#fff" stroke="#0E1B3D" stroke-width="3"><circle cx="170" cy="225" r="9"/><circle cx="196" cy="246" r="6"/><circle cx="182" cy="40" r="10"/><circle cx="205" cy="20" r="6"/></g>
<g stroke="#0E1B3D" stroke-width="3"><line x1="250" y1="200" x2="270" y2="200"/><line x1="250" y1="230" x2="270" y2="230"/><line x1="250" y1="260" x2="270" y2="260"/></g>''',
2: '''<rect width="380" height="380" fill="#FFF6E0"/>
<g transform="rotate(-18 190 190)"><rect x="40" y="200" width="300" height="60" rx="8" fill="#F3BF69" stroke="#0E1B3D" stroke-width="5"/>
<g stroke="#0E1B3D" stroke-width="3">''' + ''.join(f'<line x1="{60+i*14}" y1="200" x2="{60+i*14}" y2="{222 if i % 5 else 232}"/>' for i in range(20)) + '''</g></g>
<rect x="250" y="60" width="60" height="150" rx="6" fill="#fff" stroke="#0E1B3D" stroke-width="5"/>
<rect x="255" y="120" width="50" height="86" fill="#4F7CE8" fill-opacity=".55"/>
<g stroke="#0E1B3D" stroke-width="3"><line x1="250" y1="90" x2="270" y2="90"/><line x1="250" y1="120" x2="270" y2="120"/><line x1="250" y1="150" x2="270" y2="150"/><line x1="250" y1="180" x2="270" y2="180"/></g>
<circle cx="120" cy="110" r="50" fill="#fff" stroke="#0E1B3D" stroke-width="5"/><rect x="110" y="48" width="20" height="14" rx="3" fill="#0E1B3D"/>
<line x1="120" y1="110" x2="120" y2="76" stroke="#0149AF" stroke-width="5" stroke-linecap="round"/><line x1="120" y1="110" x2="146" y2="122" stroke="#0E1B3D" stroke-width="4" stroke-linecap="round"/>''',
3: '''<rect width="380" height="380" fill="#F3EBD3"/>
<g fill="#E6F2DC" stroke="#7FA86A" stroke-width="4"><path d="M20 70h110v95H20z"/><path d="M130 60h120v100H130z"/><path d="M250 70h120v95H250z"/><path d="M10 165h95v110H10z"/><path d="M105 160h130v115H105z"/><path d="M235 165h135v105H235z"/><path d="M20 275h120v95H20z"/><path d="M140 275h115v100H140z"/><path d="M255 270h115v100H255z"/></g>
<g fill="#7A4BD1" fill-opacity=".85"><circle cx="70" cy="110" r="11"/><circle cx="200" cy="96" r="11"/><circle cx="318" cy="128" r="11"/><circle cx="52" cy="226" r="11"/><circle cx="182" cy="208" r="11"/><circle cx="300" cy="230" r="11"/><circle cx="92" cy="318" r="11"/><circle cx="200" cy="330" r="11"/><circle cx="318" cy="306" r="11"/></g>
<g fill="#4FA35A"><circle cx="40" cy="88" r="5"/><circle cx="110" cy="146" r="5"/><circle cx="150" cy="136" r="5"/><circle cx="236" cy="78" r="5"/><circle cx="270" cy="150" r="5"/><circle cx="352" cy="88" r="5"/><circle cx="30" cy="258" r="5"/><circle cx="214" cy="256" r="5"/><circle cx="125" cy="180" r="5"/><circle cx="350" cy="250" r="5"/><circle cx="160" cy="355" r="5"/><circle cx="276" cy="290" r="5"/></g>''',
4: '''<rect width="380" height="380" fill="#E3F5EA"/>
<g stroke="#0E1B3D" stroke-width="4" fill="none"><path d="M190 80v60M190 140H100v60M190 140h90v60M100 200H60v50M100 200h40v50M280 200h-40v50M280 200h40v50"/></g>
<rect x="140" y="50" width="100" height="40" rx="20" fill="#0E1B3D"/><text x="190" y="76" text-anchor="middle" font-family="Outfit" font-weight="800" font-size="16" fill="#fff">Living?</text>
<g font-size="30" text-anchor="middle"><text x="60" y="292">🌿</text><text x="140" y="292">🍄</text><text x="240" y="292">🐟</text><text x="320" y="292">🐦</text></g>
<g fill="#fff" stroke="#0E1B3D" stroke-width="3"><circle cx="100" cy="200" r="9"/><circle cx="280" cy="200" r="9"/></g>''',
}
TAG = {1: 'Lab', 2: 'SI units', 3: '×400', 4: 'Key'}

# ---- small concept map from the real cmap --------------------------------------------
def mapmini(cm):
    nodes = [n for n in cm['nodes'] if n.get('k') in ('root', 'key')] or cm['nodes'][:6]
    ids = {n['id'] for n in nodes}
    rows = sorted({n['r'] for n in nodes}); rmap = {r: i for i, r in enumerate(rows)}
    pos = {n['id']: (48 + n['c'] * 86, 30 + rmap[n['r']] * 70) for n in nodes}
    h = 30 + len(rows) * 70
    out = [f'<svg viewBox="0 0 440 {h}" width="100%" font-family="Outfit,Arial" font-size="11" font-weight="700" aria-hidden="true"><g stroke="#9DB3DA" stroke-width="2">']
    for a, b, *_ in cm['links']:
        if a in ids and b in ids:
            (x1, y1), (x2, y2) = pos[a], pos[b]; out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    out.append('</g>')
    for n in nodes:
        x, y = pos[n['id']]; root = n.get('k') == 'root'; t = n['t'] if len(n['t']) <= 16 else n['t'][:15] + '…'
        out.append(f'<rect x="{x-42}" y="{y-15}" width="84" height="30" rx="{15 if root else 9}" fill="{"#F3BF69" if root else "#fff"}" stroke="{"#F3BF69" if root else "#0149AF"}" stroke-width="2"/>'
                   f'<text x="{x}" y="{y+4}" text-anchor="middle" fill="#0E1B3D">{E(t)}</text>')
    return ''.join(out) + '</svg>'

# ---- page -------------------------------------------------------------------------
def sidebar(cur):
    out = []
    for u in IDX['units']:
        n = u['n']; d = DEMO.get(n, dict(state='new', secs={}, score=None))
        badge = '✓' if d['state'] == 'done' else str(n)
        cls = ' class="cur" open' if n == cur else ''
        link = f'unit{n:02d}.html' if n in DEMO else '#'
        secs = ''
        for s in u['sections']:
            st = 'done' if d['state'] == 'done' else d['secs'].get(s['id'], '')
            dot = {'done': ' ok', 'go': ' half'}.get(st, '')
            secs += f'<a href="{link}"><span class="d{dot}"></span>{E(s["id"] + " " + s["t"])}</a>'
        test = f'★ Unit Test {n} · ' + (f'passed {d["score"]}%' if d['score'] else '45 min')
        secs += f'<a class="test" href="{link}">{test}</a>'
        if n == cur: secs = f'<a href="{link}" style="font-weight:700;color:var(--ink)">Unit overview</a>' + secs.replace('<a class="test"', '<a href="#">🧠 Concept map</a><a class="test"')
        out.append(f'<details{cls}><summary><span class="n{" done" if d["state"] == "done" else ""}">{badge}</span>{E(u["t"])}<span class="ch">›</span></summary><div class="secs">{secs}</div></details>')
    return ''.join(out)

def topic(c, s, d, objs):
    st = 'done' if d['state'] == 'done' else d['secs'].get(s['id'], 'new')
    num = '✓' if st == 'done' else s['id']
    pill = {'done': ('ok', 'Completed'), 'go': ('go', 'In progress'), 'new': ('no', 'Not started')}[st]
    desc = ' '.join(objs[o]['t'] for o in s['objs'])
    v = f'{fmt(s["video"]["dur"])} · {len(s["stops"])} pause questions'
    tiles = {
        'done': [('ok', '▶', 'Watch', v + ' ✓'), ('ok', '✓', 'Practise', '30/30 · 8/8 Core'), ('ok', '🖨', 'Worksheet', 'Printed')],
        'go': [('ok', '▶', 'Watch', v + ' ✓'), ('go', '✎', 'Practise', '12/30 · 5/8 Core<span class="mini"><i style="width:40%"></i></span>'), ('', '🖨', 'Worksheet', 'Print only')],
        'new': [('', '▶', 'Watch', v), ('', '✎', 'Practise', '0/30 · 0/8 Core'), ('', '🖨', 'Worksheet', 'Print only')],
    }[st]
    t = ''.join(f'<a class="tile {k}" href="#"><i>{ic}</i><span><b>{nm}</b><small>{sub}</small></span></a>' for k, ic, nm, sub in tiles)
    btn = {'done': f'<a class="btn sm ghost" href="#">Review {s["id"]}</a>', 'go': '<a class="btn sm blue" href="#">Continue practice →</a>',
           'new': f'<a class="btn sm outline" href="#">Start {s["id"]}</a>'}[st]
    mins = round(s['video']['dur'] / 60 * 3 + 40)
    foot = {'done': f'Studied {mins - 6} min', 'go': 'Studied 34 min · ≈ 25 min left', 'new': f'≈ {mins} min'}[st]
    return (f'<article class="topic {"done" if st == "done" else "cur" if st == "go" else ""}"><div class="num">{num}</div><div>'
            f'<div class="tt"><div><p class="eyebrow">Topic {s["id"]}</p><h3>{E(s["title"])}</h3></div><span class="st {pill[0]}">{pill[1]}</span></div>'
            f'<p class="d">{E(desc)}</p><div class="tiles">{t}</div><div class="tfoot"><span>{foot}</span>{btn}</div></div></article>')

def page(n):
    c = json.load(open(f'{W}/content/stage7-unit{n:02d}.json')); u = c['unit']; d = DEMO[n]; secs = c['sections']; objs = c['objectives']
    marks = sum(q.get('pts', 1) for q in c['tests']['A']); nobj = len(objs)
    secure = nobj if d['state'] == 'done' else sum(len(s['objs']) for s in secs if d['secs'].get(s['id']) == 'done')
    pct = {'done': 100, 'go': 38, 'new': 0}[d['state']]
    nxt = secs[0] if d['state'] != 'go' else next(s for s in secs if d['secs'].get(s['id']) != 'done')
    if d['state'] == 'done':
        cta = f'<a class="btn dark" href="#">Review Unit {n}</a><a class="btn outline" href="#">See my test result · {d["score"]}%</a>'
        float_ = f'<i>🏆</i><div><b>Unit passed</b>Unit Test {n}: {d["score"]}% · +100 XP</div>'
    elif d['state'] == 'go':
        cta = f'<a class="btn dark" href="#">▶ Continue: {nxt["id"]} practice</a><a class="btn outline" href="#">Open the concept map</a>'
        float_ = f'<i>⏸</i><div><b>Next up</b>{nxt["id"]} Practice · 18 questions left · ≈ 25 min</div>'
    else:
        cta = f'<a class="btn dark" href="#">▶ Start {nxt["id"]}: watch the video</a><a class="btn outline" href="#">Open the concept map</a>'
        float_ = f'<i>▶</i><div><b>Start here</b>{nxt["id"]} {E(nxt["title"])} · {fmt(nxt["video"]["dur"])} video</div>'
    studied_lbl = 'completed in' if d['state'] == 'done' else 'studied so far'
    objs_html = ''.join(f'<li class="{"ok" if (d["state"] == "done" or any(k in s["objs"] and d["secs"].get(s["id"]) == "done" for s in secs)) else ""}">{E(o["t"])}</li>' for k, o in objs.items())
    if d['score']:
        exam = (f'<section class="exam"><div><p class="eyebrow light">Final step · passed</p><h3>Unit Test {n} — {E(u["title"])}</h3>'
                f'<p style="margin:0">You passed this Unit Test. You can sit it again to practise — your first pass is what counts for the certificate.</p>'
                f'<div class="facts"><div><b>{d["score"]}%</b><span>your score</span></div><div><b>{marks}</b><span>marks</span></div><div><b>45 min</b><span>time allowed</span></div><div><b>+100 XP</b><span>earned</span></div></div></div>'
                f'<div class="clk"><div style="color:#7FD3A1">✓ Passed</div><br><a class="btn gold" href="#">Review my answers</a></div></section>')
    else:
        exam = (f'<section class="exam"><div><p class="eyebrow light">Final step · exam room</p><h3>Unit Test {n} — {E(u["title"])}</h3>'
                f'<p style="margin:0">A timed paper in the exam room. The clock keeps running if you leave the page, and the paper is handed in automatically at 0:00.</p>'
                f'<div class="facts"><div><b>45 min</b><span>time allowed</span></div><div><b>{marks}</b><span>marks</span></div><div><b>&gt; 70%</b><span>to pass</span></div><div><b>+100 XP</b><span>when you pass</span></div></div></div>'
                f'<div class="clk"><div>45:00</div><span>{"Open now (test phase)" if n == 3 else "Opens when all Core practice is done"}</span><br><br><a class="btn gold" href="#">Enter the exam room</a></div></section>')
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Atomic – Cambridge Stage 7 · Unit {n} sample (v4)</title>
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Figtree:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="preview.css">
<link rel="stylesheet" href="unit.css">
</head>
<body>
<header class="hdr">
  <div class="hdr-in">
    <a class="brand" href="index.html"><img src="../atomic_logo.png" alt="Atomic — home"></a>
    <nav class="nav"><a href="index.html">Dashboard</a><a class="on" href="unit{n:02d}.html">Course</a><a href="#">Question Bank</a><a href="#">Tests &amp; exams</a><a href="#">Progress</a></nav>
    <div class="hdr-r"><span class="lvl"><b>Lv 4</b><i style="--p:62%"></i></span><button class="btn sm ghost">Minh An</button></div>
  </div>
  <div class="crumbs"><div class="hdr-in">
    <a href="index.html">Dashboard</a><span>›</span><a href="#">Cambridge Lower Secondary</a><span>›</span><a href="#"><b class="cam">Cambridge</b> Stage 7</a><span>›</span><a href="unit{n:02d}.html"><b>Unit {n} · {E(u["title"])}</b></a>
  </div></div>
</header>
<div class="note">Bản mẫu trang <b>Unit {n}</b> (design v4, nội dung thật, số tiến độ minh hoạ). Bấm các unit ở thanh bên trái để chuyển giữa Unit 1–4.</div>
<section class="uhero">
  <div>
    <div class="kick"><span class="stage"><span class="cam">Cambridge</span><span>Stage 7</span></span><span class="t">Unit {n} of 14 · {E(u["strandShort"])}</span></div>
    <h1>{E(u["title"])}</h1>
    <p class="lead">{E(u["blurb"])}</p>
    <div class="facts"><div><b>{hrs(c["est"])}</b><span>estimated time</span></div><div><b>{d["studied"]}</b><span>{studied_lbl}</span></div><div><b>{secure} / {nobj}</b><span>objectives secure</span></div></div>
    <div class="uprog"><div class="top"><span>Unit progress</span><span>{pct}%</span></div><div class="bar"><i style="width:{pct}%;{"background:var(--ok)" if pct == 100 else ""}"></i></div></div>
    <div class="row">{cta}</div>
  </div>
  <div class="art">
    <div class="lens"><svg viewBox="0 0 380 380" width="380" height="380" aria-hidden="true">{ART[n]}</svg></div>
    <span class="tag">{TAG[n]}</span>
    <div class="float">{float_}</div>
  </div>
</section>
<section class="ubody"><div class="ugrid">
  <aside class="side">
    <div class="sbox"><h5>Your courses</h5><div class="stg">
      <a class="on" href="#"><span><span class="cam">Cambridge</span> Stage 7</span><small style="color:#fff">38%</small></a>
      <a href="#"><span><span class="cam">Cambridge</span> Stage 8</span><small>Enrol →</small></a>
      <a href="#"><span><span class="cam">Cambridge</span> Stage 9</span><small>Enrol →</small></a></div></div>
    <div class="sbox hrs"><h5>Cambridge Stage 7 course</h5><b>{hrs(IDX["est"])}</b>of learning · you have studied 12 h 12 min</div>
    <div class="sbox units"><h5>Units</h5>{sidebar(n)}</div>
  </aside>
  <div>
    <div class="phead"><div><p class="eyebrow">Cambridge Stage 7 · Unit {n}</p><h2>Your learning path</h2></div>
      <div class="steps"><span>1 Watch</span><span>2 Practise</span><span>3 Worksheet</span><span>4 Unit Test</span></div></div>
    {''.join(topic(c, s, d, objs) for s in secs)}
    {exam}
    <div class="two">
      <section class="panel"><h3>What you will learn</h3><span style="font-size:14px;color:var(--muted)">{secure} of {nobj} secure</span><ul class="objs">{objs_html}</ul></section>
      <section class="panel"><h3>Concept map</h3><span style="font-size:14px;color:var(--muted)">Tap a box to see its video and questions</span>
        <div class="mapmini">{mapmini(c["cmap"])}</div><a class="btn sm outline" href="#">Open the interactive map →</a></section>
    </div>
  </div>
</div></section>
<footer class="foot"><img src="../atomic_logo.png" alt=""><p>Written by the Atomic teaching team. Atomic courses follow the Cambridge Lower Secondary Science curriculum framework. Atomic is not part of, or endorsed by, Cambridge University Press &amp; Assessment.</p></footer>
</body>
</html>
'''

for n in DEMO:
    open(f'{W}/preview/unit{n:02d}.html', 'w').write(page(n)); print('unit', n)
