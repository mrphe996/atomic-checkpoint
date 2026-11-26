# -*- coding: utf-8 -*-
"""Replace the lesson notes of Maths sections with the v3 notes (maths_notes_v3/s{stage}.py → NOTES[(unit, sid)]).
Used by build_maths.py after the unit is built, and by tools/apply_notes_v3.py on the published web/content JSON."""
import importlib, json, re

WPM = 110   # reading speed of a 9–14 year old on maths notes (words per minute)


def words(blocks):
    return len(" ".join(json.dumps(b, ensure_ascii=False) for b in blocks).split())


def notes_for(stage):
    try: return importlib.import_module(f"maths_notes_v3.s{stage}").NOTES
    except ModuleNotFoundError: return {}


NUM = re.compile(r"\d+(?:\.\d+)?(?:/\d+)?")


def leaks(prompt, b):
    """does block b already show the numbers of this check question (so it would give the answer away)?"""
    pn = set(NUM.findall(prompt))
    if not pn: return False
    rows = [" ".join(r) for r in ((b.get("table") or {}).get("rows") or [])]
    txt = " ".join([b.get("q") or ""] + list(b.get("p", [])) + [w for w, _ in b.get("steps", [])] + [b.get("a") or ""] + rows)
    common = pn & set(NUM.findall(txt))
    return len(common) >= max(2, len(pn)) or (len(pn) == 1 and pn <= common and b["k"] == "example")


def place(stops, old_n, new_n, at, blocks=None):
    for i, x in enumerate(stops):
        if at and i < len(at): x["after"] = min(at[i], new_n - 1)
        else:
            a = x.get("after", 0)
            x["after"] = max(0, min(new_n - 1, round((a + 1) / max(old_n, 1) * new_n) - 1))
        # a "before you read on" question must come before the block that explains its answer (-1 = before the first block)
        p = (x.get("q") or {}).get("prompt", "")
        if blocks and re.search(r"before you", p, re.I):
            for j, b in enumerate(blocks[: x["after"] + 1]):
                if leaks(p, b): x["after"] = j - 1; break


def carry(blocks, figs, old_n, where=None):
    """keep the diagrams of the old notes (number lines, shapes, graphs …): each goes on the matching new block without a diagram.
    where = {old block index: new block index} to choose the place yourself"""
    n = len(blocks)
    for i, f in figs:
        if where and i in where: blocks[where[i]]["fig"] = f; continue
        t = min(n - 1, round(i / max(old_n, 1) * n))
        for j in list(range(t, n)) + list(range(0, t)):
            if not blocks[j].get("fig") and blocks[j]["k"] in ("idea", "example"): blocks[j]["fig"] = f; break


def apply(stage, unit, data):
    N = notes_for(stage); n = 0
    for s in data["sections"]:
        v = N.get((unit, s["id"]))
        if not v or not s.get("lesson"): continue
        old = len(s["lesson"]); figs = [(i, b["fig"]) for i, b in enumerate(s["lesson"]) if b.get("fig")]
        s["lesson"] = [dict(b) for b in v["blocks"]]; s["notes"] = "v3"
        carry(s["lesson"], figs, old, v.get("figs"))
        place(s.get("stops") or [], old, len(s["lesson"]), v.get("at"), s["lesson"])
        if s.get("stops"): s["stops"].sort(key=lambda x: x["after"])   # numbered in reading order
        if s.get("video"): s["video"]["dur"] = max(300, round(words(s["lesson"]) / WPM * 60 / 60) * 60 + 60 * len(s.get("stops") or []))
        n += 1
    return data, n
