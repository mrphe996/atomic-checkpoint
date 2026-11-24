# -*- coding: utf-8 -*-
"""Atomic Mathematics Stage 9 authoring kit.
A unit file builds Sections. Each Section has a reading lesson (ideas, methods, worked examples, common mistakes),
check questions placed after lesson blocks, and question pools: 8 Core, a large Practice pool and * Advanced.
Most questions come from templates that take random parameters, so every question is different and its
answer and worked solution are calculated, never typed by hand.
Written by the Atomic teaching team."""
import random, math, re
from fractions import Fraction as Fr

DIFFS = ("M", "H", "VH")


# ------------------------------------------------------------------ number formatting
def fmt(v, dp=None):
    """Tidy number for prompts: 12000 → '12 000', 2.50 → '2.5', -3 → '−3'."""
    if isinstance(v, Fr):
        return frac(v)
    if dp is not None:
        v = round(v, dp)
        s = f"{v:.{dp}f}"
    else:
        if abs(v - round(v)) < 1e-9:
            s = str(int(round(v)))
        else:
            s = f"{v:.10f}".rstrip("0").rstrip(".")
    neg = s.startswith("-"); s = s.lstrip("-")
    ip, _, dp_ = s.partition(".")
    if len(ip) > 4:
        ip = "{:,}".format(int(ip)).replace(",", " ")
    s = ip + ("." + dp_ if dp_ else "")
    return ("−" if neg else "") + s


def frac(f, mixed=False):
    f = Fr(f)
    if f.denominator == 1:
        return fmt(f.numerator)
    sign = "−" if f < 0 else ""; f = abs(f)
    if mixed and f > 1:
        w = f.numerator // f.denominator; r = f - w
        return f"{sign}{w} {r.numerator}/{r.denominator}"
    return f"{sign}{f.numerator}/{f.denominator}"


def sf(v, n):
    if v == 0: return 0
    return round(v, -int(math.floor(math.log10(abs(v)))) + (n - 1))


def stdform(v, dp=None):
    """3.2 × 10⁵ style text."""
    e = int(math.floor(math.log10(abs(v)))); m = v / 10 ** e
    m = round(m, 10)
    ms = fmt(m, dp) if dp is not None else fmt(m)
    return f"{ms} × 10{sup(e)}"


SUPD = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
def sup(n): return str(n).translate(SUPD)


def term(c, v, first=False):
    """+ 3x / − x / 3x: one term of an expression."""
    if c == 0: return ""
    a = abs(c); body = (("" if a == 1 and v else fmt(a)) + v) if v else fmt(a)
    if first: return ("−" if c < 0 else "") + body
    return (" − " if c < 0 else " + ") + body


def poly(*pairs):
    """poly((3,'x'),(−2,'')) → '3x − 2'."""
    out = ""; first = True
    for c, v in pairs:
        t = term(c, v, first)
        if t: out += t; first = False
    return out or "0"


def plain(s):
    """typed form of a pretty expression: '3x² − 2' → '3x^2-2'"""
    s = re.sub("[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+", lambda m: (lambda t: "^" + t if t.isdigit() else "^(" + t + ")")(m.group(0).translate(str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-"))), s)
    return s.replace("−", "-").replace("×", "*").replace("÷", "/").replace(" ", "")


# ------------------------------------------------------------------ question builders
def _opts(qid, right, wrongs):
    """mcq options: right answer + wrongs [(text, feedback)] in a stable mixed order."""
    o = [{"t": str(right), "ok": True, "fb": "Correct."}] + [{"t": str(w), "ok": False, "fb": f or "Not quite – work through the method again."} for w, f in wrongs]
    seen = set(); o2 = []
    for x in o:
        if x["t"] in seen: continue
        seen.add(x["t"]); o2.append(x)
    r = random.Random(qid); r.shuffle(o2)
    return o2


class Q:
    """Question factory bound to an objective + difficulty; returns plain dicts (ids filled in by the Section)."""
    @staticmethod
    def base(t, prompt, d, o, skill, **kw):
        assert d in DIFFS, d
        q = {"id": None, "type": t, "prompt": prompt, "diff": d, "obj": o, "skill": skill}
        q.update({k: v for k, v in kw.items() if v is not None})
        return q


def N(prompt, ans, unit="×", d="M", o="O1", tol=0.0, units=None, reason="", hint="", skill="Application", **kw):
    if isinstance(ans, Fr): ans = float(ans)
    units = units or [unit]
    if unit not in units: units = [unit] + list(units)
    q = Q.base("num", prompt, d, o, skill, answer=ans, unit=unit, units=units, tol=tol, errs=[], unitFb="", reason=reason, hint=hint, **kw)
    if unit == "×": q["bare"] = True
    return q


def X(prompt, expr, d="M", o="O1", vars="x", lhs=None, must=None, mustNot=None, show=None, reason="", hint="", formFb=None, skill="Algebra", **kw):
    # the model answer is the final form (show); chk keeps the working expression so the build can confirm they are equal
    model = plain(show) if show else plain(expr)
    return Q.base("expr", prompt, d, o, skill, expr=model, chk=plain(expr) if show and plain(show) != plain(expr) else None, vars=vars, lhs=lhs, must=must, mustNot=mustNot, show=show or expr, reason=reason, hint=hint, formFb=formFb, **kw)


def MC(prompt, right, wrongs, d="M", o="O1", reason="", hint="", skill="Reasoning", **kw):
    q = Q.base("mcq", prompt, d, o, skill, reason=reason, hint=hint, **kw)
    q["_mc"] = (right, [(w, "") if isinstance(w, str) else w for w in wrongs])
    return q


def MS(prompt, rights, wrongs, d="M", o="O1", reason="", skill="Reasoning", **kw):
    q = Q.base("multi", prompt, d, o, skill, reason=reason, **kw)
    q["_ms"] = (rights, wrongs)
    return q


def S(prompt, accept, d="M", o="O1", reason="", hint="", skill="Knowledge", **kw):
    return Q.base("short", prompt, d, o, skill, accept=[accept] if isinstance(accept, str) else list(accept), reason=reason, hint=hint, **kw)


def CMP(a, b, sign, d="M", o="O1", reason="", **kw):
    """which sign goes between a and b: tap <, > or ="""
    return MC(f"Which sign goes between {a} and {b}?  {a} ☐ {b}", sign, [(x, "") for x in ("<", ">", "=") if x != sign], d=d, o=o, reason=reason, **kw)


def CZ(prompt, text, blanks, d="M", o="O1", reason="", hint="", skill="Knowledge", **kw):
    return Q.base("cloze", prompt, d, o, skill, text=text, blanks=[[b] if isinstance(b, str) else list(b) for b in blanks], reason=reason, hint=hint, **kw)


def TB(prompt, head, rows, d="M", o="O1", reason="", hint="", skill="Data", **kw):
    """rows: lists; use B(x) for a blank to fill (numeric unless a string)."""
    return Q.base("table", prompt, d, o, skill, head=head, rows=rows, reason=reason, hint=hint, **kw)


def B(v, tol=None):
    if isinstance(v, Fr): v = float(v)
    b = {"ans": v}
    if tol: b["tol"] = tol
    return b


def GD(prompt, head, rows, d="M", o="O1", extra=None, reason="", skill="Data", **kw):
    """classify grid: rows [(label, answer)] with one heading; choices = all answers + extra"""
    ch = []
    for _, a in rows:
        if a not in ch: ch.append(a)
    ch += [x for x in (extra or []) if x not in ch]
    return Q.base("grid", prompt, d, o, skill, cols=ch, rows=[{"l": l, "a": [a]} for l, a in rows], mode="classify", reason=reason, **kw)


def TK(prompt, cols, rows, d="M", o="O1", reason="", skill="Data", **kw):
    """tick grid: rows [(label, ['✓','✗',…])]"""
    return Q.base("grid", prompt, d, o, skill, cols=cols, rows=[{"l": l, "a": a} for l, a in rows], mode="tick", reason=reason, **kw)


def EX(prompt, rubric, model, d="H", o="O1", need=None, reason="", skill="Reasoning", **kw):
    return Q.base("explain", prompt, d, o, skill, rubric=[{"pt": p, "kw": k} for p, k in rubric], model=model, need=need if need is not None else max(1, (len(rubric) + 1) // 2), reason=reason or model, **kw)


def OD(prompt, items, d="M", o="O1", reason="", skill="Reasoning", **kw):
    return Q.base("order", prompt, d, o, skill, items=items, reason=reason, **kw)


def MT(prompt, pairs, d="M", o="O1", reason="", skill="Knowledge", **kw):
    return Q.base("match", prompt, d, o, skill, pairs=[{"l": a, "r": b} for a, b in pairs], reason=reason, **kw)


def GR(prompt, x, y, pts, d="H", o="O1", reason="", skill="Data", **kw):
    return Q.base("graph", prompt, d, o, skill, x=x, y=y, plot=pts, follow=None, reason=reason, **kw)


# ------------------------------------------------------------------ display clean-up (applied to every string a learner sees)
import re as _re
_SKIP = {"id", "type", "diff", "obj", "skill", "expr", "chk", "must", "mustNot", "accept", "rubric", "blanks", "vars", "lhs", "kind", "unit", "units", "answer", "solid", "part"}
def pretty(t):
    if not isinstance(t, str) or not t: return t
    t = _re.sub(r"\s*\+\s*[-−]\s*(?=[\dA-Za-z(√])", " − ", t)            # a + -b → a − b
    t = _re.sub(r"(?<=[\w)²³])\s*[-−]\s*[-−]\s*(?=[\dA-Za-z(])", " + ", t)  # a - -b → a + b
    t = _re.sub(r"(^|[\s(=,:;\[{])-(?=[\d.]|[a-z]\b|[a-z][²³(]|\()", lambda m: m.group(1) + "−", t)  # ASCII minus → −
    t = _re.sub(r"(?<![\w.,/)²³])1(?=[a-zA-Z](?![a-zA-Z]))(?!x10)", "", t)   # 1x → x, −1x → −x
    t = _re.sub(r"([×÷]\s?)−(\d+(?:\.\d+)?|[a-z]\b)", r"\1(−\2)", t)   # 3 × −4 → 3 × (−4)
    t = _re.sub(r"([+−]) \((\d+(?:\.\d+)?)\)", r"\1 \2", t)                      # x + (1) → x + 1
    t = _re.sub(r"\+ \(−(\d+(?:\.\d+)?)\)", r"− \1", t)                         # x + (−7) → x − 7
    t = _re.sub(r"− \(−(\d+(?:\.\d+)?)\)", r"+ \1", t)                           # x − (−7) → x + 7
    t = _re.sub(r"\d+\.\d{7,}(?![\d…])", lambda m: fmt(float(f"{float(m.group(0)):.10g}")), t)  # float noise 1.1400000000000001 → 1.14
    return t
def prettify(o, key=None):
    if key in _SKIP: return o
    if isinstance(o, str): return pretty(o)
    if isinstance(o, list): return [prettify(v) for v in o]
    if isinstance(o, tuple): return tuple(prettify(v) for v in o)
    if isinstance(o, dict): return {k: prettify(v, k) for k, v in o.items()}
    return o


def finish(q, qid):
    q = dict(q); q["id"] = qid
    if "_mc" in q:
        r, w = q.pop("_mc"); q["options"] = _opts(qid, r, w)
    if "_ms" in q:
        rs, ws = q.pop("_ms")
        o = [{"t": str(t), "ok": True, "fb": "Correct."} for t in rs] + [{"t": str(t), "ok": False, "fb": "This one is not true – check it with a counter-example."} for t in ws]
        random.Random(qid).shuffle(o); q["options"] = o
    if q.get("fig") or q.get("data"):
        if q["skill"] not in ("Data", "Figure"): q["skill"] = "Figure" if q.get("fig") else "Data"
    for k in [k for k, v in q.items() if v in ("", None)]:
        if k not in ("answer",): q.pop(k)
    return prettify(q)


# ------------------------------------------------------------------ sections and units
class Section:
    def __init__(self, unit, sid, title, objs):
        self.u, self.sid, self.title, self.objs = unit, sid, title, objs
        self.lesson, self.stops, self.pools = [], [], {"r": [], "p": [], "a": []}
        self.n = int(sid.split(".")[1])
        self.rng = random.Random(f"m9-{sid}" if unit.stage == 9 else f"m{unit.stage}-{sid}")

    # ---- lesson blocks: text uses **bold**; steps = [(working, why)]
    def _blk(self, k, t, p, **kw):
        b = {"k": k, "t": t, "p": [p] if isinstance(p, str) else list(p or [])}
        b.update({x: y for x, y in kw.items() if y is not None}); self.lesson.append(prettify(b)); return self
    def idea(self, t, p, fig=None, table=None): return self._blk("idea", t, p, fig=fig, table=table)
    def method(self, t, p, steps=None, fig=None): return self._blk("method", t, p, steps=steps, fig=fig)
    def example(self, t, q, steps, a, p=None, fig=None, table=None): return self._blk("example", t, p, q=q, steps=steps, a=a, fig=fig, table=table)
    def tip(self, t, p): return self._blk("tip", t, p)
    def mistake(self, t, p): return self._blk("mistake", t, p)

    def check(self, q):
        """a check question shown after the most recent lesson block"""
        i = len(self.stops) + 1; qid = f"{self.u.pre}s{self.n}k{i:02d}"
        self.stops.append({"id": f"{self.sid}-k{i}", "t": i, "after": len(self.lesson) - 1, "review": [0, 0], "note": "", "q": finish(q, qid)})
        return self

    # ---- pools
    def add(self, pool, q):
        lst = self.pools[pool]; tag = {"r": "r", "p": "p", "a": "a"}[pool]
        qid = f"{self.u.pre}s{self.n}{tag}{len(lst) + 1:02d}"
        q = finish(q, qid)
        if pool == "a" and not q["prompt"].startswith("* Advanced."): q["prompt"] = "* Advanced. " + q["prompt"]
        lst.append(q); return q
    def core(self, *qs):
        for q in qs: self.add("r", q)
        return self
    def adv(self, *qs):
        for q in qs: self.add("a", q)
        return self
    def prac(self, *qs):
        for q in qs: self.add("p", q)
        return self

    def gen(self, pool, n, *templates, unique=True):
        """call templates(rng) in turn until n new questions (distinct prompts) are added"""
        kf = lambda q: q["prompt"] + str(q.get("fig")) + str(q.get("data")) + str(q.get("rows")) + str(q.get("pairs")) + str(q.get("_mc", q.get("options", "")))[:200]
        for t in templates:
            if all(t is not x for _, x in self.u.tpl): self.u.tpl.append((self.sid, t))
        seen = {kf(q) for q in self.pools[pool]}; added = 0; tries = 0
        while added < n and tries < n * 40:
            t = templates[(added + tries) % len(templates)]; tries += 1
            q = t(self.rng)
            if q is None: continue
            key = kf(q)
            if unique and key in seen: continue
            seen.add(key); self.add(pool, q); added += 1
        assert added == n, (self.sid, pool, added, n)
        return self

    def std(self, T, ex, adv=None, n_core=7, n_prac=40, n_adv=8):
        """standard pools: Core = one question from each of the first n_core templates + the written explanation,
        Practice = n_prac from all templates, Advanced = n_adv from adv (or the templates)"""
        vis = lambda q: q.get("type") in ("grid", "table", "graph", "label", "scale") or bool(q.get("fig") or q.get("data"))
        cand = []
        for t in T:
            for _ in range(20):
                q = t(self.rng)
                if q is not None: cand.append(q); break
        V = [q for q in cand if vis(q)][:2]
        assert len(V) == 2, f"{self.sid}: Core needs 2 diagram/data templates"
        rest = [q for q in cand if all(q is not v for v in V)][:n_core - 2]
        self.core(*(V + rest), ex)
        self.gen("p", n_prac, *T); self.gen("a", n_adv, *(adv or T))
        return self

    def export(self, dur):
        return {"id": self.sid, "title": self.title, "objs": self.objs, "lesson": self.lesson,
                "video": {"src": None, "offset": 0, "dur": dur, "range": ""},
                "stops": self.stops, "captions": [], "chapters": [[0.0, dur]],
                "req": self.pools["r"], "prac": self.pools["p"], "adv": self.pools["a"]}


class Unit:
    def __init__(self, n, title, strand, blurb, objectives, stage=None):
        self.n, self.title, self.strand, self.blurb = n, title, strand, blurb
        self.stage = stage or STAGE
        self.pre = f"m{self.stage}u{n:02d}"
        self.tpl, self.tex = [], []      # test templates (from gen) and written test explain questions
        self.objectives = objectives      # {O1: {sec, code, t}}
        self.sections = []; self.mind = []

    def section(self, sid, title, objs):
        s = Section(self, sid, title, objs); self.sections.append(s); return s

    def ttpl(self, sid, *fns):
        """extra question templates used only by the Unit Tests"""
        for t in fns: self.tpl.append((sid, t))
        return self

    def texp(self, *qs):
        """explain questions written for the Unit Tests only (never in practice)"""
        self.tex += list(qs); return self

    def mindmap(self, *kids):
        self.mind = [{"id": f"k{i}", "t": t, "d": d, "obj": o, "sec": s} for i, (t, d, o, s) in enumerate(kids)]

    def export(self, tests, titles):
        secs = []
        for s in self.sections:
            words = sum(len(" ".join(b.get("p", [])).split()) + len(str(b.get("steps", ""))) // 6 for b in s.lesson)
            dur = max(300, int(words / 120 * 60) + 90 * len(s.stops) + 60 * sum(1 for b in s.lesson if b["k"] == "example"))
            secs.append(s.export(dur))
        segs = {}
        for s in secs:
            for o in s["objs"]: segs.setdefault(o, [s["id"], 0.0, s["video"]["dur"], s["title"]])
        st = self.stage; prim = st <= 6
        lvl = "Primary" if prim else "Lower Secondary"; fw = f"Cambridge {lvl} Mathematics ({'0096' if prim else '0862'}), Stage {st}"
        return {"course": {"id": f"s{10 + st}", "title": f"Atomic – Cambridge {lvl} Mathematics — Stage {st}", "units": [{"n": i + 1, "t": t} for i, t in enumerate(titles)]},
                "unit": {"n": self.n, "stage": 10 + st, "title": self.title, "strandShort": self.strand, "blurb": self.blurb, "strand": self.strand,
                         "framework": fw, "lesson": True, "subject": "maths", "read": f"media/read/m{st}u{self.n:02d}.pdf"},
                "objectives": self.objectives, "sections": secs, "segments": segs, "sources": [],
                "tests": {"A": tests[0], "B": tests[1], "pass": 0.7},
                "mindmap": {"id": "root", "t": self.title, "sec": None, "kids": self.mind}}


STAGE = 9
TITLES = ["Number and Calculation", "Expressions and Formulae", "Decimals, Percentages and Rounding", "Equations and Inequalities", "Angles",
          "Statistical Investigations", "Shapes and Measurements", "Fractions", "Sequences and Functions", "Graphs",
          "Ratio and Proportion", "Probability", "Position and Transformation", "Volume, Surface Area and Symmetry", "Interpreting and Discussing Results"]


def pick(r, seq): return seq[r.randrange(len(seq))]
def nz(r, a, b):
    while True:
        v = r.randint(a, b)
        if v: return v


class Paper:
    """Exam paper (Unit Test / end-of-year / Checkpoint): numbered questions with a shared context and parts (a), (b)…
       p.q(ctx, fig=, data=); p.a(pts, question)  ·  p.done(total) checks the marks."""
    L = "abcdefghij"
    def __init__(self, prefix):
        self.pre, self.items, self.qn, self.part, self.ctx = prefix, [], 0, 0, {}
    def q(self, ctx=None, fig=None, data=None):
        self.qn += 1; self.part = 0
        self.ctx = {"ctx": (f"Question {self.qn}. " + ctx) if ctx else None, "fig": fig, "data": data}; return self
    def a(self, pts, q):
        self.part += 1; qid = f"{self.pre}q{self.qn:02d}{self.L[self.part - 1]}"
        q = dict(q); q["prompt"] = f"({self.L[self.part - 1]}) " + q["prompt"]
        for k in ("ctx", "fig", "data"):
            if self.ctx.get(k) and not q.get(k): q[k] = self.ctx[k]
        q = finish(q, qid); q["pts"] = pts; self.items.append(q); return self
    def done(self, total):
        s = sum(x["pts"] for x in self.items)
        import os
        if os.environ.get("ATOMIC_COUNT"): print(f"{self.pre}: {s}/{total} marks, {len(self.items)} parts, {self.qn} questions")
        else: assert s == total, (self.pre, s, total)
        return self.items
