#!/usr/bin/env python3
"""Put the Maths lesson notes v3 into the published course files (web/content/stage1N-unitUU.json).
build_maths.py does the same at build time; this script updates the site without the private sources.
Usage: python3 tools/apply_notes_v3.py [stage …]   (default: every stage that has notes)"""
import glob, json, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "content", "authoring"))
from maths_notes_v3.apply import apply, notes_for

stages = [int(a) for a in sys.argv[1:]] or [s for s in range(3, 10) if notes_for(s)]
for st in stages:
    tot = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "web", "content", f"stage{10 + st}-unit[0-9][0-9].json"))):
        unit = int(f[-7:-5]); d = json.load(open(f, encoding="utf-8"))
        d, n = apply(st, unit, d)
        if n: json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False); tot += n
    print(f"Maths Stage {st}: {tot} sections with v3 notes")
