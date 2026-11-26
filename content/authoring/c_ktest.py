"""Unit Test, 2026 format, built from the shared question kit (kit.py / kit6 / kit34): used for Primary Stages 3-6.
25+ separately numbered questions in sections A-D, 30 marks. No (a)/(b) parts: a context may be shared by the next n questions,
but every question stands on its own.   p = KTest('p3u01v3A'); p.sec('A'); p.q(ctx, fig=, data=, n=2); p.a(pts, PM(...)); TEST_A = p.done()
Written by the Camday teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'math9'))
import kit as K

SECS = {"A": "Recall", "B": "Data and graphs", "C": "Investigations", "D": "Explain and apply"}

class KTest:
    def __init__(self, pre):
        self.pre, self.items, self.qn, self.cur, self.ctx, self.left = pre, [], 0, None, {}, 0
    def sec(self, k):
        self.cur = f"{k} · {SECS[k]}"; return self
    def q(self, ctx=None, fig=None, data=None, n=1):
        self.ctx, self.left = {"ctx": ctx, "fig": fig, "data": data}, n; return self
    def a(self, pts, q):
        assert self.cur, "call sec() first"
        self.qn += 1; qid = f"{self.pre}q{self.qn:02d}"; q = dict(q)
        if self.left > 0:
            for k in ("ctx", "fig", "data"):
                if self.ctx.get(k) and not q.get(k): q[k] = self.ctx[k]
            self.left -= 1
        if q.get("type") == "explain" and "need" in q: q["need"] = min(q["need"], pts)
        q = K.finish(q, qid); q["pts"] = pts; q["sec"] = self.cur; self.items.append(q); return self
    def done(self, total=30, min_q=25):
        s = sum(x["pts"] for x in self.items); n = len(self.items); secs = [x["sec"][0] for x in self.items]
        if os.environ.get("ATOMIC_COUNT"):
            print(f"{self.pre}: {s}/{total} marks, {n} questions, sections " + " ".join(f"{k}:{secs.count(k)}q/{sum(x['pts'] for x in self.items if x['sec'][0]==k)}m" for k in "ABCD"))
        else:
            assert s == total, (self.pre, "marks", s, total)
            assert n >= min_q, (self.pre, "questions", n, min_q)
            assert secs == sorted(secs) and set(secs) == set("ABCD"), (self.pre, "sections", secs)
        return self.items
