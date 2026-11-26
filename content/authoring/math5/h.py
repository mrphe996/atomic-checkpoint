# -*- coding: utf-8 -*-
"""Shared helpers for Stage 5 Mathematics units. Written by the Camday teaching team."""
from fractions import Fraction as Fr
from kit import N, frac

TOL = 1e-6


def F(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction in its simplest form or a mixed number.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}" + (f" = {frac(v, True)}" if v > 1 and v.denominator > 1 else "")), **kw)


def P(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}"), **kw)


def sg(v): return f"−{-v}" if v < 0 else str(v)
def PP(x, y): return [f"({x}, {y})", f"({x},{y})", f"({sg(x)}, {sg(y)})", f"({sg(x)},{sg(y)})", f"{sg(x)}, {sg(y)}"]
def dec(r, lo, hi, dp): return round(r.randint(lo * 10 ** dp, hi * 10 ** dp) / 10 ** dp, dp)
def hm(t): return f"{t // 60:02d}:{t % 60:02d}"
def am(t):
    h, m = divmod(t, 60); return f"{(h - 1) % 12 + 1}:{m:02d} {'a.m.' if h < 12 else 'p.m.'}"
def RECT(l, w, u="cm"): return {"kind": "shape", "pts": [[0, 0], [l, 0], [l, w], [0, w]], "s": [f"{l} {u}", f"{w} {u}", "", ""], "right": [0, 1, 2, 3]}
def PIE(d, shade): return {"kind": "pie", "labels": [""] * d, "values": [1] * d, "shade": list(shade)}
NL = lambda lo, hi: {"kind": "numline", "min": lo, "max": hi}
G = lambda pts=None, polys=None, rng=6, lo=None: {"kind": "coord", "x": [lo if lo is not None else -rng, rng], "y": [lo if lo is not None else -rng, rng], **({"points": pts} if pts else {}), **({"polys": polys} if polys else {})}
