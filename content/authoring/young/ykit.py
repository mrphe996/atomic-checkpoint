# -*- coding: utf-8 -*-
"""Authoring kit for Cambridge Primary Stages 1 and 2 (ages 5-7), Science and Mathematics.
Builds on math9/kit.py (lessons, check questions, Core / Practice / More practice / Advanced pools) and adds:
  * picture answers (tap a picture card) and a big picture above a question
  * a word bank per lesson (used by the word games and the lesson word drawer)
  * tap-only Unit Tests (no typing at this age): 2 papers × 15 questions × 2 marks
  * course metadata for Science (keys 1, 2) and Mathematics (keys 11, 12)
Every question is tap-only: mcq / multi / grid / match / order. Written by the Atomic teaching team."""
import os, sys, random, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "math9"))
import kit
from kit import *   # noqa: F401,F403

TAP = {"mcq", "multi", "grid", "match", "order"}


def PIC(prompt, right, wrongs, pics=None, d="M", o="O1", reason="", hint="", pic=None, fig=None, **kw):
    """multiple choice; every option gets a picture when pics = {text: emoji} covers them all; pic = big emoji above"""
    q = MC(prompt, right, wrongs, d=d, o=o, reason=reason, hint=hint, fig=fig, **kw)
    if pics: q["_pics"] = dict(pics)
    if pic: q["pic"] = pic
    return q


def NUMS(prompt, right, wrongs, **kw):
    """choose a number (tap): options are numbers, shown smallest first"""
    q = MC(prompt, str(right), [str(w) for w in wrongs], **kw)
    q["_sortnum"] = True
    return q


_finish = kit.finish
def finish(q, qid):
    pics = q.pop("_pics", None) if isinstance(q, dict) else None
    srt = q.pop("_sortnum", None) if isinstance(q, dict) else None
    out = _finish(q, qid)
    if pics and out.get("options") and all(o["t"] in pics for o in out["options"]):
        for o in out["options"]: o["e"] = pics[o["t"]]
    if srt and out.get("options"):
        try: out["options"].sort(key=lambda o: float(o["t"]))
        except ValueError: pass
    if out["type"] == "multi":
        for o in out["options"]:
            if not o["ok"]: o["fb"] = "Look again – this one does not fit."
    assert out["type"] in TAP or out["type"] == "explain" and False, f"{qid}: young learners cannot type ({out['type']})"
    return out
kit.finish = finish


def ykey(q):
    """the same question, raw or finished: prompt + picture + answers (option order ignored)"""
    q = kit.prettify(dict(q))
    if q.get("options"): ans = sorted(o["t"] for o in q["options"])
    elif "_mc" in q: r, w = q["_mc"]; ans = sorted([str(r)] + [str(x[0]) for x in w])
    elif "_ms" in q: rs, ws = q["_ms"]; ans = sorted(map(str, list(rs) + list(ws)))
    else: ans = []
    return "|".join([q["prompt"].replace("* Advanced. ", ""), json.dumps(q.get("fig"), sort_keys=True, ensure_ascii=False), str(q.get("pic")), str(q.get("rows")), str(q.get("pairs")), str(q.get("items")), str(ans)])


class YSection(kit.Section):
    def __init__(self, unit, sid, title, objs):
        super().__init__(unit, sid, title, objs); self.vocab = []
        self.rng = random.Random(f"y{unit.subj}{unit.stage}-{sid}")
    def words(self, *ws):
        """word bank: (word, child-friendly meaning, emoji)"""
        self.vocab += [{"w": w, "def": d, "emoji": e} for w, d, e in ws]; return self
    def export(self, dur):
        x = super().export(dur); x["vocab"] = self.vocab; return x
    def _std2(self, T, ex, adv, n_core, n_adv, deep, cap, n_more):
        """as kit._std2, but at this age a picture-card question counts as a picture question, and no question repeats anywhere"""
        vis = lambda q: q.get("type") in ("grid", "match", "order") or bool(q.get("fig") or q.get("pic") or q.get("_pics"))
        seen = {ykey(ex)} | {ykey(x["q"]) for x in self.stops}
        allT = list(T) + list(deep); cand = []
        for rnd in range(6):                      # one of each kind first, more rounds only if a kind keeps repeating
            for t in allT:
                if len(cand) >= 3 * n_core: break
                for _ in range(20):
                    q = t(self.rng)
                    if q is not None and ykey(q) not in seen: seen.add(ykey(q)); cand.append(q); break
            if len(cand) >= len(allT): break
        V = [q for q in cand if vis(q)][:2]
        assert len(V) == 2, f"{self.sid}: Core needs 2 picture questions"
        rest = [q for q in cand if all(q is not v for v in V)]
        assert len(V) + len(rest) >= n_core, f"{self.sid}: only {len(V) + len(rest)} different Core questions"
        self.core(*(V + rest[:n_core - 2]), ex)
        self.capped("p", [1] * len(allT), allT)
        src = list(adv or deep); self.capped("a", [-(-n_adv // len(src))] * len(src), src)
        self.pools["a"] = self.pools["a"][:n_adv]
        self.capped("m", [3] * len(allT), allT)
        return self

    def capped(self, pool, per, templates):
        """per[i] new questions from templates[i]; a question already in any pool (or a check) is never repeated"""
        seen = {ykey(q) for p in self.pools.values() for q in p} | {ykey(x["q"]) for x in self.stops}; buckets = []
        for t, n in zip(templates, per):
            if all(t is not x for _, x in self.u.tpl): self.u.tpl.append((self.sid, t))
            got, tries = [], 0
            while len(got) < n and tries < 80:
                tries += 1; q = t(self.rng)
                if q is None: continue
                k = ykey(q)
                if k in seen: continue
                seen.add(k); got.append(q)
            buckets.append(got)
        i = 0
        while any(buckets):
            b = buckets[i % len(buckets)]
            if b: self.add(pool, b.pop(0))
            i += 1
        return self

    def young(self, T, ex, deep, n_adv=6):
        """Core = 2 picture/table questions + routine + reasoning + ex; Practice = one of each kind; More practice = the variants"""
        return self.std(T, ex, deep=deep, n_adv=n_adv)


class YUnit(kit.Unit):
    def __init__(self, n, title, strand, blurb, objectives, stage, subj):
        super().__init__(n, title, strand, blurb, objectives, stage=stage)
        self.subj = subj; self.pre = f"{'y' if subj == 'science' else 'k'}{stage}u{n:02d}"
    def section(self, sid, title, objs):
        s = YSection(self, sid, title, objs); self.sections.append(s); return s

    def tests(self):
        """two tap-only papers: 15 fresh questions × 2 marks = 30, every section represented, never a practice question"""
        key = ykey
        banned = {key(q) for s in self.sections for p in s.pools.values() for q in p} | {key(x["q"]) for s in self.sections for x in s.stops}
        papers = []
        for P in "AB":
            rng = random.Random(f"ytest-{self.pre}-{P}"); items = []; order = list(self.tpl); rng.shuffle(order)
            by_sec = {}
            for sid, t in order: by_sec.setdefault(sid, []).append(t)
            secs = list(by_sec); i = 0; guard = 0
            while len(items) < 15 and guard < 4000:
                guard += 1; sid = secs[i % len(secs)]; i += 1
                t = by_sec[sid][(i // len(secs)) % len(by_sec[sid])]
                q = t(rng)
                if q is None or key(q) in banned or q["type"] not in TAP: continue
                banned.add(key(q)); q = dict(q); q["prompt"] = q["prompt"].replace("* Advanced. ", "")
                q = finish(q, f"{self.pre}t{P}q{len(items) + 1:02d}"); q["pts"] = 2; items.append(q)
            assert len(items) == 15, (self.pre, P, len(items))
            if not any(x["type"] in ("grid", "match") or x.get("fig") or x.get("pic") or any(o.get("e") for o in x.get("options", [])) for x in items):
                raise AssertionError(f"{self.pre}{P}: no picture question")
            papers.append(items)
        return papers

    def yexport(self, titles):
        tests = self.tests()
        secs = []
        for s in self.sections:
            words = sum(len(" ".join(b.get("p", [])).split()) for b in s.lesson)
            secs.append(s.export(max(240, int(words / 80 * 60) + 90 * len(s.stops))))
        segs = {}
        for s in secs:
            for o in s["objs"]: segs.setdefault(o, [s["id"], 0.0, s["video"]["dur"], s["title"]])
        st = self.stage
        if self.subj == "science":
            course = {"id": f"s{st}", "title": f"Atomic – Cambridge Primary Science — Stage {st}", "units": [{"n": i + 1, "t": t} for i, t in enumerate(titles)]}
            unit = {"n": self.n, "stage": st, "title": self.title, "strandShort": self.strand, "blurb": self.blurb, "strand": f"{self.strand}",
                    "framework": f"Cambridge Primary Science (0097), Stage {st}", "lesson": True, "subject": "science", "young": True, "tiny": True}
        else:
            course = {"id": f"s{10 + st}", "title": f"Atomic – Cambridge Primary Mathematics — Stage {st}", "units": [{"n": i + 1, "t": t} for i, t in enumerate(titles)]}
            unit = {"n": self.n, "stage": 10 + st, "title": self.title, "strandShort": self.strand, "blurb": self.blurb, "strand": self.strand,
                    "framework": f"Cambridge Primary Mathematics (0096), Stage {st}", "lesson": True, "subject": "maths", "young": True, "tiny": True}
        return {"course": course, "unit": unit, "objectives": self.objectives, "sections": secs, "segments": segs, "sources": [],
                "tests": {"A": tests[0], "B": tests[1], "pass": 0.7}, "mindmap": {"id": "root", "t": self.title, "sec": None, "kids": self.mind}}


def EXQ(t, seed=7):
    """a fixed worked question from a template (first variant that works)"""
    r = random.Random(seed)
    for _ in range(50):
        q = t(r)
        if q is not None: return q
    raise AssertionError("no example question")


def pick(r, seq): return seq[r.randrange(len(seq))]
def others(r, pool, right, n=2):
    c = [x for x in pool if x != right]; r.shuffle(c); return c[:n]
