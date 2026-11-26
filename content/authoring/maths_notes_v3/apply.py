# -*- coding: utf-8 -*-
"""Replace the lesson notes of Maths sections with the v3 notes (maths_notes_v3/s{stage}.py → NOTES[(unit, sid)]).
Used by build_maths.py after the unit is built, and by tools/apply_notes_v3.py on the published web/content JSON."""
import importlib, json

WPM = 110   # reading speed of a 9–14 year old on maths notes (words per minute)


def words(blocks):
    return len(" ".join(json.dumps(b, ensure_ascii=False) for b in blocks).split())


def notes_for(stage):
    try: return importlib.import_module(f"maths_notes_v3.s{stage}").NOTES
    except ModuleNotFoundError: return {}


def place(stops, old_n, new_n, at):
    for i, x in enumerate(stops):
        if at and i < len(at): x["after"] = min(at[i], new_n - 1); continue
        a = x.get("after", 0)
        x["after"] = max(0, min(new_n - 1, round((a + 1) / max(old_n, 1) * new_n) - 1))


def apply(stage, unit, data):
    N = notes_for(stage); n = 0
    for s in data["sections"]:
        v = N.get((unit, s["id"]))
        if not v or not s.get("lesson"): continue
        old = len(s["lesson"]); s["lesson"] = v["blocks"]; s["notes"] = "v3"
        place(s.get("stops") or [], old, len(s["lesson"]), v.get("at"))
        if s.get("video"): s["video"]["dur"] = max(300, round(words(s["lesson"]) / WPM * 60 / 60) * 60 + 60 * len(s.get("stops") or []))
        n += 1
    return data, n
