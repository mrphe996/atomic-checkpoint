# -*- coding: utf-8 -*-
"""Build content/src/stage19-unitNN.json (Mathematics Stage 9) from math9/uNN.py + private tests.
Usage: python3 build_math.py 1 [2 …]   (no arguments: every unit that exists)"""
import json, os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "private"))
from kit import TITLES

def build(n):
    U = importlib.import_module(f"u{n:02d}").U
    import math9_tx as TX, mtest
    U.texp(*TX.EXP[n]); U.ttpl and [U.ttpl(sid, f) for sid, f in TX.TPL.get(n, [])]
    tests = mtest.assemble(U)       # 2026 format: 25 questions, sections A-D, 30 marks
    data = U.export(tests, TITLES)
    out = os.path.join(HERE, "..", "..", "src", f"stage19-unit{n:02d}.json")
    json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False)
    print(n, [(s["id"], len(s["req"]), len(s["prac"]), len(s["adv"]), len(s["stops"]), len(s["lesson"])) for s in data["sections"]])

if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or [n for n in range(1, 16) if os.path.exists(os.path.join(HERE, f"u{n:02d}.py"))]
    for n in ns: build(n)
