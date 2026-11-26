# -*- coding: utf-8 -*-
"""School revision sets for Mathematics Stages 7-9 (school Grades 6-8).
Each KIND is one type of question from the school's revision papers, support packs and practice papers:
    K(unit, sid, build, doc, rand)
  build(*params) -> question          the question, written once
  doc  = [params, ...]                the numbers used on the school papers   -> Practice + printed Worksheet
  rand = rng -> params                fresh numbers of the same kind          -> Unit Test templates (never the practice numbers)
Written by the Camday teaching team."""
import importlib

class Reg:
    def __init__(self, stage): self.stage, self.kinds = stage, []
    def K(self, unit, sid, build, doc, rand=None, o=None, ws=True):
        self.kinds.append((unit, sid, build, doc, rand, o, ws)); return self


def apply(U):
    try: R = importlib.import_module(f"school.g{U.stage}").R
    except ModuleNotFoundError: return 0
    n = 0; secs = {s.sid: s for s in U.sections}
    kf = lambda q: q["prompt"] + str(q.get("rows", "")) + str(q.get("items", "")) + str(q.get("_mc", ""))
    for unit, sid, build, doc, rand, o, ws in R.kinds:
        if unit != U.n: continue
        s = secs[sid]; obj = o or s.objs[0]
        seen = {kf(q) for p in s.pools.values() for q in p}
        for p in doc:
            q = build(*p) if isinstance(p, tuple) else build(p)
            q["obj"] = obj; q["set"] = "school"
            if ws: q["ws"] = 1
            if kf(q) in seen: continue
            seen.add(kf(q)); s.add("p", q); n += 1
        if rand:
            def t(r, build=build, rand=rand, obj=obj):
                p = rand(r)
                if p is None: return None
                q = build(*p) if isinstance(p, tuple) else build(p)
                q["obj"] = obj; q["set"] = "school"; return q
            t.school = True; U.tpl.append((sid, t))
    return n
