# -*- coding: utf-8 -*-
"""Build content/src/stage7-unitNN.json from content/authoring/units/s7uNN.py (+ private tests).
Usage: python3 build_unit.py 4 [5 ...]"""
import json, os, sys, importlib, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'units')); sys.path.insert(0, os.path.join(HERE, '..', 'private'))
PLAN = json.load(open('/home/claude/vid/sec/plan.json'))
TITLES = ["Introducing Science", "Measurements", "Cells", "Classifying Living Things", "Food Chains and Food Webs", "Materials and Their Structure", "Properties of Materials",
          "Acids and Alkalis", "Chemical Reactions", "Forces", "Energy", "Electricity", "Earth Processes", "Earth and Beyond"]
norm = lambda t: re.sub(r'[^a-z0-9]+', ' ', t.lower()).strip()

def build(n):
    U = importlib.import_module(f's7u{n:02d}'); T = importlib.import_module(f'tests_stage7_unit{n:02d}')
    plan = PLAN[str(n)]; secs = []
    assert [s['id'] for s in plan['sections']] == [s['id'] for s in U.SECTIONS], ('section ids differ from the video', [s['id'] for s in plan['sections']])
    for k, (ps, s) in enumerate(zip(plan['sections'], U.SECTIONS)):
        dur = round(ps['end'] - ps['start'], 3); caps = ps['caps']
        stops = []
        for st in U.STOPS[s['id']]:
            hit = [c for c in caps if norm(st['at']) in norm(c[2])]
            assert hit, (s['id'], st['id'], 'phrase not found in narration', st['at'])
            t = round(min(hit[0][1] + 0.3, dur - 1.0), 2)
            prev = [c for c in caps if c[1] <= t]
            rv = round(max(0.0, prev[-3][0] if len(prev) >= 3 else 0.0), 1)
            stops.append({"id": st['id'], "t": t, "review": [rv, t], "note": st.get('note') or f"Paused after: “{hit[0][2][:90]}”", "q": st['q']})
        req, prac, advq = U.POOLS[s['id']]
        for x in advq: x['adv'] = True
        chapters = [[0.0, ps['scenes'][0][1]]] + [[c[0], c[1]] for c in ps['scenes'][1:]]
        secs.append({"id": s['id'], "title": s['title'], "objs": s['objs'],
                     "video": {"src": f"media/u{n}_s{k + 1}.mp4", "offset": ps['start'], "dur": dur, "range": f"{int(ps['start'] // 60):02d}:{int(ps['start'] % 60):02d}–{int(ps['end'] // 60):02d}:{int(ps['end'] % 60):02d}"},
                     "stops": stops, "captions": [[c[0], c[2]] for c in caps], "chapters": chapters, "req": req, "prac": prac, "adv": advq})
    segs = {}
    for s in secs:
        for o in s['objs']: segs.setdefault(o, [s['id'], 0.0, s['video']['dur'], s['title']])
    for t in (T.TEST_A, T.TEST_B): assert sum(x['pts'] for x in t) == 30, sum(x['pts'] for x in t)
    data = {"course": {"id": "s7", "title": "Atomic Checkpoint Secondary Cambridge Science — Stage 7", "units": [{"n": i + 1, "t": t} for i, t in enumerate(TITLES)]},
            "unit": {"n": n, "title": TITLES[n - 1], "strandShort": U.STRAND, "blurb": U.BLURB, "strand": U.STRAND, "framework": "Cambridge Lower Secondary Science (0893), Stage 7"},
            "objectives": U.OBJECTIVES, "sections": secs, "segments": segs, "sources": getattr(U, 'SOURCES', []),
            "tests": {"A": T.TEST_A, "B": T.TEST_B, "pass": 0.7}, "mindmap": U.MINDMAP}
    out = os.path.join(HERE, '..', 'src', f'stage7-unit{n:02d}.json')
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
    print(n, [(s['id'], len(s['req']), len(s['prac']), len(s['adv']), len(s['stops'])) for s in secs])

if __name__ == '__main__':
    for a in sys.argv[1:]: build(int(a))
