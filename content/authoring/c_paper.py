# -*- coding: utf-8 -*-
"""Camday authoring kit for exam-style papers (Unit Tests, Checkpoint papers, end-of-year exams).
Questions are written the way Checkpoint papers are: a numbered question opens with a shared context
(an investigation, a diagram drawn by figures2.js, a results table) and has parts (a), (b), (c) ...
Each part is its own auto-marked item; students choose answers or type them – no teacher marking.

    p = Paper("s9u01tA")
    p.q("Mia investigates how light intensity affects photosynthesis in pondweed.",
        fig={"kind": "pondweed", "dist": 10}, data={"head": [...], "rows": [[...]]})
    p.sa(1, "O1", "Name the gas in the bubbles.", ["oxygen"])
    p.nm(2, "O1", "Calculate the mean ...", 12.5, "bubbles per minute")
    TEST_A = p.done(30)
Written by the Camday teaching team."""
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

    def para(self, q):
        """Add a ready-made 6-mark paragraph question (type 'para', built by the para kits) as its own numbered question."""
        self.qn += 1; self.part = 0; self.ctx = None
        q = dict(q); q["id"] = f"{self.pre}q{self.qn:02d}p"; self.items.append(q)
        return q

    def done(self, total):
        s = sum(x["pts"] for x in self.items)
        import os
        if os.environ.get("ATOMIC_COUNT"): print(f"{self.pre}: {s}/{total} marks, {len(self.items)} parts, {self.qn} questions")
        else: assert s == total, (self.pre, s, total)
        return self.items


class UnitTest(Paper):
    """Unit Test, 2026 format: at least 25 numbered questions in four labelled sections, 30 marks in total.
    Every item is its own numbered question (no (a)/(b) parts). Call p.sec("A") to start a section and
    p.q(ctx, fig, data) just before an item that needs a context, diagram or table.
        A  Recall              short knowledge questions (1 mark each)
        B  Data and graphs     read, calculate from and interpret tables, graphs and diagrams
        C  Investigations      plan, carry out and evaluate experiments
        D  Explain and apply   reasoning in new situations
    """
    SECS = {"A": "Recall", "B": "Data and graphs", "C": "Investigations", "D": "Explain and apply"}

    def __init__(self, prefix):
        super().__init__(prefix); self.cur = None; self._ctx_next = None

    def sec(self, k):
        self.cur = f"{k} · {self.SECS[k]}"; return self

    def q(self, ctx=None, fig=None, data=None, n=1):
        """context, diagram or table for the next n questions (they share it)"""
        self._ctx_next = {"ctx": ctx, "fig": fig, "data": data}; self._ctx_left = n; return self

    def _id(self):
        self.qn += 1; self.part = 1
        return f"{self.pre}q{self.qn:02d}"

    def _add(self, q, pts):
        assert self.cur, "call sec() first"
        q["sec"] = self.cur
        c = self._ctx_next or {}
        self._ctx_left = getattr(self, "_ctx_left", 0) - 1
        if self._ctx_left <= 0: self._ctx_next = None
        for k in ("ctx", "fig", "data"):
            if c.get(k): q[k] = c[k]
        self.items.append(P(q, pts))
        return q

    def para(self, q):
        """A ready-made 6-mark paragraph question (AI-marked against its mark scheme) as its own numbered question in the current section."""
        assert self.cur, "call sec() first"
        q = dict(q); q["id"] = f"{self._id()}p"; q["sec"] = self.cur
        q["prompt"] = __import__("re").sub(r"^\([ab]\) ", "", q["prompt"])
        q.setdefault("pts", 6); self.items.append(q)
        return q

    def done(self, total=30, min_q=25):
        import os
        s = sum(x["pts"] for x in self.items); n = len(self.items)
        secs = [x["sec"][0] for x in self.items]
        if os.environ.get("ATOMIC_COUNT"):
            print(f"{self.pre}: {s}/{total} marks, {n} questions, sections " + " ".join(f"{k}:{secs.count(k)}q/{sum(x['pts'] for x in self.items if x['sec'][0]==k)}m" for k in "ABCD"))
        else:
            assert s == total, (self.pre, "marks", s, total)
            assert n >= min_q, (self.pre, "questions", n, min_q)
            assert secs == sorted(secs) and set(secs) == set("ABCD"), (self.pre, "sections in order A-D", secs)
        return self.items
