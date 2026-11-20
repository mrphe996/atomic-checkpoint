# -*- coding: utf-8 -*-
"""Short-hand authoring helpers for Stage 7 units (written by the Atomic teaching team).
Every question uses the same JSON shape as c_base (mcq, multi, num, order, match, explain, grid, table, graph)."""
import hashlib
from c_base import O, mcq, multi, num, order, match, explain, grid, table, graph, B

def _rot(id, n):
    return int(hashlib.md5(id.encode()).hexdigest(), 16) % n

def _opts(id, right, wrongs):
    r = right if isinstance(right, tuple) else (right, "Correct.")
    opts = [O(w[0], False, w[1]) for w in wrongs]
    k = _rot(id, len(opts) + 1)
    opts.insert(k, O(r[0], True, r[1]))
    return opts

def mc(id, diff, obj, prompt, right, wrongs, hint="", reason="", skill="Knowledge", **kw):
    """right: 'text' or ('text', 'feedback'); wrongs: [('text', 'why it is wrong'), ...]"""
    return mcq(id, prompt, _opts(id, right, wrongs), diff, obj, skill, hint=hint, reason=reason, **kw)

def ms(id, diff, obj, prompt, rights, wrongs, hint="", reason="", skill="Knowledge", **kw):
    opts = [O(t, True, "") for t in rights] + [O(w[0], False, w[1]) for w in wrongs]
    k = _rot(id, len(opts)); opts = opts[k:] + opts[:k]
    return multi(id, prompt, opts, diff, obj, skill, hint=hint or f"{len(rights)} statements are correct.", reason=reason, **kw)

def nm(id, diff, obj, prompt, answer, unit, units=None, tol=0.0, errs=None, hint="", reason="", skill="Application", **kw):
    return num(id, prompt, answer, unit, diff, obj, skill, tol=tol, units=units or [unit], errs=[{"v": v, "fb": f} for v, f in (errs or [])], hint=hint, reason=reason, **kw)

def od(id, diff, obj, prompt, items, hint="", reason="", skill="Knowledge", **kw):
    return order(id, prompt, items, diff, obj, skill, hint=hint, reason=reason, **kw)

def mt(id, diff, obj, prompt, pairs, hint="", reason="", skill="Knowledge", **kw):
    return match(id, prompt, pairs, diff, obj, skill, hint=hint, reason=reason, **kw)

def ex(id, diff, obj, prompt, rubric, model, hint="", reason="", skill="Reasoning", need=None, **kw):
    return explain(id, prompt, rubric, model, diff, obj, skill, need=need, hint=hint, reason=reason, **kw)

def gd(id, diff, obj, prompt, cols, rows, hint="", reason="", skill="Data", extra=None, **kw):
    """Tick grid: cols = column headings, answers '✓'/'✗'. Classify grid: give one heading (e.g. ["Group"]);
    the drop-down choices become every answer used (plus `extra` distractors)."""
    tick = all(len(a) == len(cols) and all(x in ("✓", "✗") for x in a) for _, a in rows)
    if not tick:
        ch = []
        for _, a in rows:
            if a[0] not in ch: ch.append(a[0])
        cols = ch + [x for x in (extra or []) if x not in ch]
    return grid(id, prompt, cols, rows, diff, obj, skill, hint=hint, reason=reason, **kw)

def tb(id, diff, obj, prompt, head, rows, hint="", reason="", skill="Data", **kw):
    return table(id, prompt, head, rows, diff, obj, skill, hint=hint, reason=reason, **kw)

def gr(id, diff, obj, prompt, x, y, pts, follow=None, hint="", reason="", skill="Data", **kw):
    return graph(id, prompt, x, y, pts, diff, obj, skill, follow=follow, hint=hint, reason=reason, **kw)

def adv(q):
    """Advanced (*) questions: prompt starts with '* Advanced.'"""
    if not q["prompt"].startswith("* Advanced."): q["prompt"] = "* Advanced. " + q["prompt"]
    return q

def stop(id, at, q, note=""):
    """A pause question. `at` = words from the narration line after which the video pauses."""
    return {"id": id, "at": at, "q": q, "note": note}

def P(q, pts):
    q["pts"] = pts
    return q
