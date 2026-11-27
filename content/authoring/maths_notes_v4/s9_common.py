# -*- coding: utf-8 -*-
"""Shared helpers for the Stage 9 v4 lessons."""
import re
from maths_notes_v4.kit4 import num, short, expr

SUP = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
SF_NOTE = " Write it like 3.2 × 10^5."


def sf(id, prompt, a, n, hint, reason, **kw):
    """an answer in standard form a × 10^n, typed as 3.2 × 10^5 (x, *, ^ and superscripts all accepted)"""
    a = str(a); e = re.escape(a); m = str(n).replace("-", "[-−]")
    rx = rf"/^\s*{e}\s*(×|x|X|\*|·)\s*10\s*(\^\s*\(?\s*{m}\s*\)?|{re.escape(str(n).translate(SUP)).replace('⁻', '[⁻]')})\s*$/"
    return short(id, prompt + SF_NOTE, [f"{a} × 10^{n}", rx], hint, reason, skill="Application", **kw)


def fr(id, prompt, n, d, hint, reason, **kw):
    return num(id, prompt + " Give your answer as a fraction in its simplest form.", n / d, hint, reason, tol=1e-6, **kw)


def ex(id, prompt, ans, hint, reason, v="x", lhs=None, **kw):
    return expr(id, prompt, ans, hint, reason, vars=v, lhs=lhs, **kw)


NB = ["^[^()]*$"]


def pt(id, prompt, x, y, hint, reason, **kw):
    """a coordinate answer such as (3, −2)"""
    xs, ys = str(x).replace("-", "[-−]"), str(y).replace("-", "[-−]")
    rx = rf"/^\s*\(?\s*{xs}\s*[,;]\s*{ys}\s*\)?\s*$/"
    return short(id, prompt, [f"({x}, {y})", rx], hint, reason, skill="Application", **kw)


def bg(id, prompt, deg, hint, reason, **kw):
    """a three-figure bearing"""
    return short(id, prompt + " Write three figures, e.g. 045.", [f"{deg:03d}", f"{deg:03d}°"], hint, reason, **kw)


def seq(id, prompt, terms, hint, reason, **kw):
    """a list of numbers typed with commas, e.g. 4, 7, 12"""
    s = ", ".join(str(t) for t in terms)
    rx = r"/^\s*" + r"\s*[,; ]\s*".join(str(t).replace("-", "[-−]").replace(".", r"\.") for t in terms) + r"\s*$/"
    return short(id, prompt + " Separate them with commas.", [s, rx], hint, reason, skill="Application", **kw)
