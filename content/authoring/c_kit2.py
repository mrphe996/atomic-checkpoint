# -*- coding: utf-8 -*-
"""Compact authoring kit for Stage 8 and 9 units (written by the Atomic teaching team).
Ids are generated: s{stage}u{unit}s{section}{kind}{n}. Kinds: r = Core, p = practice, a = advanced, v = video stop.

    u = Unit(8, 1)
    u.sec("1.1", "O1")
    u.mc("r", "Prompt?", "right answer", ["wrong", ("wrong", "why")])
    ...
    SECTIONS, POOLS, STOPS = u.export(SECTIONS_META)
"""
from c_kit import mc as _mc, ms as _ms, nm as _nm, od as _od, mt as _mt, ex as _ex, gd as _gd, tb as _tb, gr as _gr, adv as _adv, stop as _stop, P, B

def _w(ws):
    return [w if isinstance(w, tuple) else (w, "Not quite – look again at the key idea.") for w in ws]

class Unit:
    def __init__(self, g, n):
        self.g, self.n = g, n
        self.pools, self.stops = {}, {}
        self.k = None

    def sec(self, k, obj):
        self.k, self.o = k, obj
        self.pools[k] = {"r": [], "p": [], "a": []}
        self.stops[k] = []
        self.c = {"r": 0, "p": 0, "a": 0, "v": 0}

    def _id(self, kind):
        self.c[kind] += 1
        return f"s{self.g}u{self.n:02d}s{self.k.split('.')[1]}{kind}{self.c[kind]:02d}"

    def _add(self, kind, q):
        if kind == "a":
            q = _adv(q)
        self.pools[self.k][kind].append(q)
        return q

    def _d(self, kind, d):
        return d or {"r": "M", "p": "M", "a": "VH"}[kind]

    # question makers -------------------------------------------------------
    def mc(self, kind, prompt, right, wrongs, d=None, o=None, skill="Knowledge", reason=""):
        return self._add(kind, _mc(self._id(kind), self._d(kind, d), o or self.o, prompt, right, _w(wrongs), skill=skill, reason=reason))

    def ms(self, kind, prompt, rights, wrongs, d=None, o=None, skill="Knowledge"):
        return self._add(kind, _ms(self._id(kind), self._d(kind, d), o or self.o, prompt, rights, _w(wrongs), skill=skill))

    def nm(self, kind, prompt, ans, unit, d=None, o=None, tol=0.0, skill="Application"):
        return self._add(kind, _nm(self._id(kind), self._d(kind, d) if d else ("H" if kind != "a" else "VH"), o or self.o, prompt, ans, unit, tol=tol, skill=skill))

    def od(self, kind, prompt, items, d=None, o=None, skill="Knowledge"):
        return self._add(kind, _od(self._id(kind), self._d(kind, d), o or self.o, prompt, items, skill=skill))

    def mt(self, kind, prompt, pairs, d=None, o=None):
        return self._add(kind, _mt(self._id(kind), self._d(kind, d), o or self.o, prompt, pairs))

    def ex(self, kind, prompt, rubric, model, d=None, o=None, need=2):
        return self._add(kind, _ex(self._id(kind), self._d(kind, d) if d else ("H" if kind != "a" else "VH"), o or self.o, prompt, rubric, model, need=need))

    def gd(self, kind, prompt, head, rows, d=None, o=None, extra=None):
        """Classify grid: rows = [(label, answer)]"""
        return self._add(kind, _gd(self._id(kind), self._d(kind, d), o or self.o, prompt, [head], [(a, [b]) for a, b in rows], extra=extra, skill="Data"))

    def tb(self, kind, prompt, head, rows, d=None, o=None):
        return self._add(kind, _tb(self._id(kind), self._d(kind, d) if d else "H", o or self.o, prompt, head, rows, skill="Data"))

    def gr(self, kind, prompt, x, y, pts, d=None, o=None):
        return self._add(kind, _gr(self._id(kind), self._d(kind, d) if d else "H", o or self.o, prompt, x, y, pts, skill="Data"))

    # pause question in the video: `at` = words from the narration after which the video stops
    def stop(self, at, prompt, right, wrongs, d="M", o=None):
        i = self._id("v")
        self.stops[self.k].append(_stop(i, at, _mc(i + "q", d, o or self.o, prompt, right, _w(wrongs))))

    def export(self, sections):
        pools = {k: (v["r"], v["p"], v["a"]) for k, v in self.pools.items()}
        for k, (r, p, a) in pools.items():
            assert len(r) == 8, (k, "core", len(r))
            assert len(r) + len(p) + len(a) >= 30, (k, len(r) + len(p) + len(a))
            assert len(a) >= 4, (k, "adv", len(a))
            assert self.stops[k], (k, "no video stop")
        return sections, pools, self.stops


class Test:
    """Unit Test paper: t = Test(8, 1, "A"); t.mc(2, "O1", ...); TEST_A = t.done()"""
    def __init__(self, g, n, form):
        self.g, self.n, self.f, self.i, self.q = g, n, form, 0, []

    def _id(self):
        self.i += 1
        return f"s{self.g}u{self.n:02d}t{self.f}{self.i:02d}"

    def _p(self, q, pts):
        self.q.append(P(q, pts)); return q

    def mc(self, pts, o, prompt, right, wrongs, d="M"): return self._p(_mc(self._id(), d, o, prompt, right, [(w, "") for w in wrongs]), pts)
    def ms(self, pts, o, prompt, rights, wrongs, d="M"): return self._p(_ms(self._id(), d, o, prompt, rights, [(w, "") for w in wrongs]), pts)
    def nm(self, pts, o, prompt, ans, unit, d="H", tol=0.0): return self._p(_nm(self._id(), d, o, prompt, ans, unit, tol=tol), pts)
    def od(self, pts, o, prompt, items, d="M"): return self._p(_od(self._id(), d, o, prompt, items), pts)
    def mt(self, pts, o, prompt, pairs, d="M"): return self._p(_mt(self._id(), d, o, prompt, pairs), pts)
    def gd(self, pts, o, prompt, head, rows, d="M", extra=None): return self._p(_gd(self._id(), d, o, prompt, [head], [(a, [b]) for a, b in rows], extra=extra), pts)
    def tb(self, pts, o, prompt, head, rows, d="H"): return self._p(_tb(self._id(), d, o, prompt, head, rows), pts)
    def ex(self, pts, o, prompt, rubric, model, d="VH", need=2): return self._p(_ex(self._id(), d, o, prompt, rubric, model, need=need), pts)

    def done(self):
        s = sum(q["pts"] for q in self.q)
        assert s == 30, (self.g, self.n, self.f, s)
        return self.q
