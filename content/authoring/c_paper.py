# -*- coding: utf-8 -*-
"""Atomic authoring kit for exam-style papers (Unit Tests, Checkpoint papers, end-of-year exams).
Questions are written the way Checkpoint papers are: a numbered question opens with a shared context
(an investigation, a diagram drawn by figures2.js, a results table) and has parts (a), (b), (c) ...
Each part is its own auto-marked item; students choose answers or type them – no teacher marking.

    p = Paper("s9u01tA")
    p.q("Mia investigates how light intensity affects photosynthesis in pondweed.",
        fig={"kind": "pondweed", "dist": 10}, data={"head": [...], "rows": [[...]]})
    p.sa(1, "O1", "Name the gas in the bubbles.", ["oxygen"])
    p.nm(2, "O1", "Calculate the mean ...", 12.5, "bubbles per minute")
    TEST_A = p.done(30)
Written by the Atomic teaching team."""
from c_kit import mc as _mc, ms as _ms, nm as _nm, od as _od, mt as _mt, ex as _ex, gd as _gd, tb as _tb, gr as _gr, P, B
from c_base import q as _q

LETTERS = "abcdefghijk"


def _acc(a):
    return [a] if isinstance(a, str) else list(a)


class Paper:
    def __init__(self, prefix):
        self.pre, self.items, self.qn, self.part, self.ctx = prefix, [], 0, 0, None

    # ---- a new numbered question with its shared context -------------------------------------
    def q(self, ctx=None, fig=None, data=None):
        self.qn += 1; self.part = 0
        self.ctx = {"ctx": f"Question {self.qn}. " + ctx if ctx else None, "fig": fig, "data": data}
        return self

    def _id(self):
        self.part += 1
        return f"{self.pre}q{self.qn:02d}{LETTERS[self.part - 1]}"

    def _add(self, q, pts):
        lbl = f"({LETTERS[self.part - 1]}) "
        q["prompt"] = lbl + q["prompt"]
        if self.ctx:
            for k in ("ctx", "fig", "data"):
                if self.ctx.get(k): q[k] = self.ctx[k]
        self.items.append(P(q, pts))
        return q

    # ---- part types (pts first, then objective, then the question) ----------------------------
    def mc(self, pts, o, prompt, right, wrongs, d="H", reason=""):
        return self._add(_mc(self._id(), d, o, prompt, right, [(w, "") if isinstance(w, str) else w for w in wrongs], reason=reason), pts)

    def ms(self, pts, o, prompt, rights, wrongs, d="H"):
        return self._add(_ms(self._id(), d, o, prompt, rights, [(w, "") for w in wrongs]), pts)

    def nm(self, pts, o, prompt, ans, unit, d="H", tol=0.0, units=None):
        units = units or [unit]
        if unit not in units: units = [unit] + units
        return self._add(_nm(self._id(), d, o, prompt, ans, unit, units=units, tol=tol), pts)

    def sa(self, pts, o, prompt, accept, d="H", hint=""):
        """typed short answer: accept = list of accepted answers (first plain one is the model); '/regex/' allowed"""
        return self._add(_q(self._id(), "short", prompt, d, o, "Knowledge", accept=_acc(accept), hint=hint), pts)

    def cz(self, pts, o, prompt, text, blanks, d="H", hint=""):
        """typed gaps: text with {0}, {1} ... and one accepted-answer list per gap"""
        return self._add(_q(self._id(), "cloze", prompt, d, o, "Knowledge", text=text, blanks=[_acc(b) for b in blanks], hint=hint), pts)

    def ex(self, pts, o, prompt, rubric, model, need=None, d="VH"):
        return self._add(_ex(self._id(), d, o, prompt, rubric, model, need=need if need is not None else pts), pts)

    def gd(self, pts, o, prompt, head, rows, d="H", extra=None):
        return self._add(_gd(self._id(), d, o, prompt, [head], [(a, [b]) for a, b in rows], extra=extra), pts)

    def tick(self, pts, o, prompt, cols, rows, d="H"):
        """tick grid: rows = [(label, [✓/✗ per column])]"""
        return self._add(_gd(self._id(), d, o, prompt, cols, rows), pts)

    def tb(self, pts, o, prompt, head, rows, d="H"):
        return self._add(_tb(self._id(), d, o, prompt, head, rows), pts)

    def od(self, pts, o, prompt, items, d="H"):
        return self._add(_od(self._id(), d, o, prompt, items), pts)

    def mt(self, pts, o, prompt, pairs, d="H"):
        return self._add(_mt(self._id(), d, o, prompt, pairs), pts)

    def gr(self, pts, o, prompt, x, y, pts_, follow=None, d="H"):
        g = _gr(self._id(), d, o, prompt, x, y, pts_, follow=follow); g["plot"] = g.pop("pts")  # marks live in "pts"
        return self._add(g, pts)

    def done(self, total):
        s = sum(x["pts"] for x in self.items)
        import os
        if os.environ.get("ATOMIC_COUNT"): print(f"{self.pre}: {s}/{total} marks, {len(self.items)} parts, {self.qn} questions")
        else: assert s == total, (self.pre, s, total)
        return self.items
