# -*- coding: utf-8 -*-
"""Build Stages 1-2 Science (course keys 1, 2) and Mathematics (11, 12) into content/src. Written by the Atomic teaching team."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import science, maths
SRC = os.path.join(HERE, "..", "..", "src")
which = sys.argv[1:] or ["1", "2", "11", "12"]
for key in which:
    k = int(key); st = k % 10
    mod = maths if k >= 10 else science
    units = (mod.stage1 if st == 1 else mod.stage2)()
    titles = mod.TITLES[st]
    for u in units:
        x = u.yexport(titles)
        n = sum(len(s["req"]) + len(s["prac"]) + len(s["adv"]) + len(s["more"]) for s in x["sections"])
        json.dump(x, open(os.path.join(SRC, f"stage{k}-unit{u.n:02d}.json"), "w"), ensure_ascii=False, indent=1)
        print(f"stage{k}-unit{u.n:02d}", u.title, "·", " ".join(f"{s['id']}:{len(s['req'])}/{len(s['prac'])}/{len(s['adv'])}/{len(s['more'])}" for s in x["sections"]), "· total", n, "· tests 2×15")
