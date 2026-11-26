# -*- coding: utf-8 -*-
"""Build Camday ESL Stage N (course key 20 + N):  python3 build_esl.py 2 [3 …]
Writes content/src/stage2N-unitUU.json and the video scripts /home/claude/build/esl/sN/scripts.json.
Video timings (src, captions, pause times) are read from /home/claude/build/esl/sN/timing.json when present."""
import os, sys, json, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ekit
SRC = os.path.join(HERE, "..", "..", "src"); VID = "/home/claude/build/esl"
for a in sys.argv[1:]:
    st = int(a); mod = importlib.import_module(f"stage{st}")
    units = []
    for n, tup in enumerate(mod.UNITS, 1):
        title, strand, blurb = tup[:3]; lessons = []
        for x in tup[3:]: lessons += ekit.parse(x) if isinstance(x, str) else x
        units.append((n, title, strand, blurb, lessons))
    titles = [u[1] for u in units]
    tf = os.path.join(VID, f"s{st}", "timing.json"); timing = json.load(open(tf)) if os.path.exists(tf) else {}
    scripts = {}
    for n, title, strand, blurb, lessons in units:
        u = ekit.make_unit(st, n, title, strand, blurb, lessons)
        x = u.eexport(titles, timing.get(str(n)))
        key = 20 + st
        json.dump(x, open(os.path.join(SRC, f"stage{key}-unit{n:02d}.json"), "w"), ensure_ascii=False, indent=1)
        for L in lessons: scripts[f"{n}:{L['id']}"] = {"unit": n, "sid": L["id"], "title": L["title"], "scenes": ekit.script(L, st, title)}
        print(f"stage{key}-unit{n:02d}", title, "·", " ".join(f"{s['id']}:{len(s['req'])}/{len(s['prac'])}/{len(s['adv'])}/{len(s['more'])}" for s in x["sections"]), "· video" if timing.get(str(n)) else "· no video yet")
    os.makedirs(os.path.join(VID, f"s{st}"), exist_ok=True)
    json.dump(scripts, open(os.path.join(VID, f"s{st}", "scripts.json"), "w"), ensure_ascii=False, indent=1)
