# -*- coding: utf-8 -*-
"""Maths lesson notes v4 (27/11/2026): each lesson is a complete self-study lesson, the way a teacher would teach it.
Order: Start here (a situation to try) → Remember (the prior knowledge it needs, with a quick try) → Key ideas (from examples
to the general rule, terms and symbols, why the method works) → Method → Worked examples (what we know / need / plan,
every step with its reason, a check) → Your turn (live questions, hints, worked solution) → Spot the mistake → Key points.
Then Read the PDF (course book pages) and Practise. British English, no Vietnamese text (content checker).
Helpers return the lesson blocks the site knows; v3 helpers (Q, M, X, T) are reused."""
from maths_notes_v3.kit import Q, M, X, T  # noqa: F401


def H(t, *p, table=None, fig=None):
    """Start here: a situation, picture or question to try straight away"""
    b = {"k": "hook", "t": t, "p": list(p)}
    if table: b["table"] = {"head": table[0], "rows": table[1:]}
    if fig: b["fig"] = fig
    return b


def R(t, *p, qq=None, table=None):
    """Remember: the prior knowledge the lesson uses, optionally with a quick live question"""
    b = {"k": "recall", "t": t, "p": list(p)}
    if table: b["table"] = {"head": table[0], "rows": table[1:]}
    if qq: b["qq"] = qq
    return b


def I(t, *p, table=None, fig=None, then=()):
    """Key idea (same as v3 Q); then = paragraphs shown after the table or diagram"""
    b = Q(t, *p, table=table, fig=fig)
    if then: b["p2"] = list(then)
    return b


def W(t, q, steps, a, given=None, find=None, plan=None, check=None, p=(), table=None, fig=None):
    """Worked example. steps = [(working, reason)] or [(working, reason, fig)]"""
    b = {"k": "example", "t": t, "p": list(p), "q": q, "steps": [list(s) if isinstance(s, (list, tuple)) else [s, ""] for s in steps], "a": a}
    for k, v in (("given", given), ("find", find), ("plan", plan), ("check", check)):
        if v: b[k] = v
    if table: b["table"] = {"head": table[0], "rows": table[1:]}
    if fig: b["fig"] = fig
    return b


def Y(t, qq, *p):
    """Your turn: a live question with a hint, error feedback and a worked solution"""
    return {"k": "try", "t": t, "p": list(p), "qq": qq}


def ER(t, q, lines, bad, why, fix, *p, id=None, hint=None):
    """Spot the mistake: a wrong solution; bad = index of the first wrong line; why; fix = corrected steps [(working, reason)]"""
    b = {"k": "error", "t": t, "p": list(p), "q": q, "lines": list(lines), "bad": bad, "why": why, "fix": [list(s) for s in fix], "id": id}
    if hint: b["hint"] = hint
    return b


def K(t, *points):
    """Key points (summary)"""
    return {"k": "summary", "t": t, "p": list(points)}


# ---- question helpers (the site's question engine; every question has a hint and a worked solution) ----
def num(id, prompt, answer, hint, reason, errs=(), diff="M", obj="O1", skill="Application", **kw):
    q = {"id": id, "type": "num", "prompt": prompt, "diff": diff, "obj": obj, "skill": skill, "answer": answer, "unit": "×", "units": ["×"], "tol": 0,
         "errs": [{"v": v, "fb": f} for v, f in errs], "bare": True, "hint": hint, "reason": reason}
    q.update(kw); return q


def mcq(id, prompt, options, hint, reason, diff="M", obj="O1", skill="Reasoning", fixed=False, **kw):
    """options = [(text, ok, feedback)]"""
    q = {"id": id, "type": "mcq", "prompt": prompt, "diff": diff, "obj": obj, "skill": skill, "hint": hint, "reason": reason,
         "options": [{"t": t, "ok": ok, "fb": f} for t, ok, f in options]}
    if fixed: q["fixed"] = True
    q.update(kw); return q


def table(id, prompt, head, rows, hint, reason, diff="M", obj="O1", skill="Data", **kw):
    """rows: cells; a number in a list [n] is an answer cell"""
    rr = [[{"ans": c[0]} if isinstance(c, list) else c for c in r] for r in rows]
    q = {"id": id, "type": "table", "prompt": prompt, "diff": diff, "obj": obj, "skill": skill, "head": head, "rows": rr, "hint": hint, "reason": reason}
    q.update(kw); return q


def short(id, prompt, accept, hint, reason, diff="M", obj="O1", skill="Knowledge", **kw):
    q = {"id": id, "type": "short", "prompt": prompt, "diff": diff, "obj": obj, "skill": skill, "accept": list(accept), "hint": hint, "reason": reason}
    q.update(kw); return q


def explain(id, prompt, rubric, need, model, hint, diff="H", obj="O1", skill="Reasoning", **kw):
    """rubric = [(point, [regex keywords])]"""
    q = {"id": id, "type": "explain", "prompt": prompt, "diff": diff, "obj": obj, "skill": skill, "rubric": [{"pt": p, "kw": k} for p, k in rubric],
         "need": need, "model": model, "hint": hint, "reason": model}
    q.update(kw); return q


def L(*blocks, stops=None, at=None, pdf=None, practice=None):
    """one v4 lesson. stops = new check questions [(after_block_index, question)] (replace the old ones);
    at = placement of the old check questions (if stops is None); pdf = [{book, p0, p1, label, note, look}];
    practice = {"req": [...], "prac": [...], "adv": [...], "more": [...]} replaces those lists (keeps any list not given)"""
    return {"blocks": list(blocks), "stops": stops, "at": list(at) if at else None, "pdf": pdf, "practice": practice, "v": 4}


def grid(id, prompt, cols, rows, hint, reason, diff="M", obj="O1", skill="Data", **kw):
    """sort each row into one column. rows = [(label, column)]"""
    q = {"id": id, "type": "grid", "prompt": prompt, "diff": diff, "obj": obj, "skill": skill, "cols": list(cols),
         "rows": [{"l": l, "a": [c]} for l, c in rows], "mode": "classify", "hint": hint, "reason": reason}
    q.update(kw); return q


def expr(id, prompt, answer, hint, reason, vars="xy", lhs="y", errs_fb=None, diff="M", obj="O1", skill="Application", **kw):
    """an expression or formula to type; any equivalent form is accepted (the site compares values)"""
    q = {"id": id, "type": "expr", "prompt": prompt, "diff": diff, "obj": obj, "skill": skill, "expr": answer, "vars": vars, "show": answer, "hint": hint, "reason": reason}
    if lhs: q["lhs"] = lhs
    q.update(kw); return q


def tiles(*patterns, rows=None, gap=1):
    """a 'cells' diagram of growing patterns drawn side by side. patterns = lists of (col, row) cells, each from 0"""
    cells, x = [], 0
    R = rows or (max(r for p in patterns for _, r in p) + 1)
    for p in patterns:
        w = max(c for c, _ in p) + 1
        cells += [[x + c, r] for c, r in p]; x += w + gap
    return {"kind": "cells", "cells": cells, "cols": x - gap, "rows": R}
