# -*- coding: utf-8 -*-
"""Maths lesson notes v3 (26/11/2026): full revision notes in the style of the best revision sites.
Each section answers the questions a learner asks, in order:
  What is …?  (definitions with bold key words and many small examples)
  How do I …? (a numbered method)
  Worked examples (an easy one, then an exam-style one, every step explained)
  Common mistake, Exam tip.
Helpers build the lesson blocks the site and the reading packs already know (idea, method, example, mistake, tip).
**bold** marks key words. No Vietnamese text (content checker)."""


def Q(t, *p, table=None, fig=None):
    """a 'What is …?' / 'Why …?' block: short paragraphs or bullet-like sentences"""
    b = {"k": "idea", "t": t, "p": list(p)}
    if table: b["table"] = {"head": table[0], "rows": table[1:]}
    if fig: b["fig"] = fig
    return b


def M(t, *steps, note=None):
    """'How do I …?': numbered steps (the renderer shows each as a line)"""
    p = [f"Step {i + 1}: {s}" for i, s in enumerate(steps)]
    if note: p.append(note)
    return {"k": "method", "t": t, "p": p}


def E(t, q, steps, a, *p):
    """worked example: question, steps [(working, reason)], answer"""
    return {"k": "example", "t": t, "p": list(p), "q": q, "steps": [list(s) if isinstance(s, (list, tuple)) else [s, ""] for s in steps], "a": a}


def X(t, *p):
    return {"k": "mistake", "t": t, "p": list(p)}


def T(t, *p):
    return {"k": "tip", "t": t, "p": list(p)}


def S(*blocks, at=None):
    """one section's notes. at = block index after which each check question is shown (default: spread through the notes)"""
    return {"blocks": list(blocks), "at": list(at) if at else None}
