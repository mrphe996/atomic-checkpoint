# -*- coding: utf-8 -*-
"""Mathematics Unit Tests, 2026 format: two parallel papers (A and B), 25 separately numbered questions, 30 marks.
  A · Fluency          8 questions × 1 mark   quick recall and one-step calculation
  B · Methods          6 questions, 7 marks   standard methods (one 2-mark table / grid question)
  C · Problem solving  6 questions, 7 marks   multi-step problems in context (one 2-mark problem)
  D · Reasoning        5 questions, 8 marks   2 written explanations (2 marks each) + 3 hard problems (2 + 1 + 1)
Questions come from the unit's own question templates (each template used at most once per paper, a fresh question that is
never word-for-word a practice question) plus the explanations written for the tests only (U.texp). Paper B is a parallel
paper: the same skills with different numbers and, where the template has them, different contexts.
Written by the Atomic teaching team."""
import os, random, re
from kit import finish, prettify
# the papers are drawn with a private salt, so the public templates cannot reproduce them
SALT = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "private", "maths_seed.txt")).read().strip()

SECS = {"A": "Fluency", "B": "Methods", "C": "Problem solving", "D": "Reasoning"}
MULTI = ("table", "grid", "match", "order", "cloze", "multi")
STOP = set("a an the of to in on at for and or is are was were be by with as it its this that these those which what why how who when where "
           "do does did can could would should will from into than then so not no yes your you their they he she his her them each one two "
           "select correct statement following describe explain give use answer fraction decimal simplest form mixed number places nearest".split())


def words(q):
    t = (q.get("prompt") or "").lower()
    return {w for w in re.findall(r"[a-z]+|[0-9][0-9.,/]*|[+−×÷²³√%=<>π]", t) if w not in STOP and (len(w) > 2 or not w.isalpha())}


def sim(a, b):
    return len(a & b) / max(1, len(a | b))


def key(q):
    q = prettify(dict(q))
    return re.sub(r"^\*\s*Advanced\.\s*", "", q.get("prompt") or "") + "|" + "|".join(str(q.get(k, "")) for k in ("answer", "rows", "pairs", "items", "text", "data", "fig", "head"))


def practice_keys(U):
    ks = set()
    for s in U.sections:
        for L in s.pools.values():
            for q in L: ks.add(key(q))
        for x in s.stops: ks.add(key(x["q"]))
    return ks


def assemble(U):
    banned = practice_keys(U); used = set(); papers = []
    tex = list(U.tex)
    for P in "AB":
        rng = random.Random(f"{SALT}-{U.pre}-test-{P}")
        # one fresh candidate per template
        cands = []
        for i, (sid, t) in enumerate(U.tpl):
            for _ in range(60):
                q = t(rng)
                if q is None: continue
                if q.get("type") == "explain": q = None; break
                if key(q) in banned or key(q) in used: q = None; continue
                break
            if q: cands.append({"sid": sid, "q": q, "w": words(prettify(dict(q))), "i": i, "t": t})
        rng.shuffle(cands)
        secs = list(dict.fromkeys(c["sid"] for c in cands))
        ex = tex[:2]; tex = tex[2:]
        assert len(ex) == 2, f"{U.pre}: write at least 4 test explanations with U.texp()"
        chosen = [{"sid": None, "q": q, "w": words(q), "i": -1} for q in ex]

        def ok(c):
            return all(sim(c["w"], x["w"]) < 0.6 for x in chosen) and c not in chosen

        def take(pred, n, prefer=None):
            got = []
            for _ in range(n):
                # round-robin over sections: the section with fewest picks first
                cnt = {s: sum(1 for x in chosen if x["sid"] == s) for s in secs}
                pool = [c for c in cands if ok(c) and pred(c)]
                if prefer:
                    pp = [c for c in pool if prefer(c)]
                    pool = pp or pool
                if not pool: pool = [c for c in cands if ok(c)]
                if not pool:   # few templates (short units): a second, different question from the least-used template
                    use = {}
                    for x in chosen:
                        for k_, (sd, tt) in enumerate(U.tpl):
                            if x.get("t") is tt: use[k_] = use.get(k_, 0) + 1
                    order = sorted(range(len(U.tpl)), key=lambda k_: (use.get(k_, 0), rng.random()))
                    for strict in (True, False):
                        for k_ in order:
                            sid_, t_ = U.tpl[k_]
                            for _ in range(30):
                                q = t_(rng)
                                if q is None or q.get("type") == "explain" or key(q) in banned or key(q) in used: continue
                                c = {"sid": sid_, "q": q, "w": words(prettify(dict(q))), "i": -2, "t": t_}
                                if ok(c) and (pred(c) or not strict): pool = [c]; cands.append(c); break
                            if pool: break
                        if pool: break
                if not pool: raise AssertionError(f"{U.pre}{P}: ran out of templates ({len(chosen)} chosen, {len(cands)} candidates)")
                pool.sort(key=lambda c: cnt[c["sid"]])
                c = pool[0]; chosen.append(c); got.append(c)
            return got

        d = lambda c: c["q"].get("diff")
        single = lambda c: c["q"]["type"] not in MULTI
        A = take(lambda c: d(c) == "M" and single(c), 8)
        B = take(lambda c: d(c) == "M", 6, prefer=None)
        C = take(lambda c: d(c) == "H", 6)
        D = take(lambda c: d(c) in ("VH", "H"), 3, prefer=lambda c: d(c) == "VH")
        items = []

        def put(sec, pts, q):
            qid = f"{U.pre}v3{P}q{len(items) + 1:02d}"
            q = dict(q)
            if q.get("type") == "explain" and "need" in q: q["need"] = min(q["need"], pts)
            q["prompt"] = re.sub(r"^\*\s*Advanced\.\s*", "", q["prompt"])
            q = finish(q, qid); q["pts"] = pts; q["sec"] = f"{sec} · {SECS[sec]}"
            items.append(q); used.add(key(q))

        for c in A: put("A", 1, c["q"])
        two = next((c for c in B if c["q"]["type"] in MULTI), B[-1])
        for c in B: put("B", 2 if c is two else 1, c["q"])
        two = next((c for c in C if d(c) == "H" and c["q"]["type"] == "num"), C[-1])
        for c in C: put("C", 2 if c is two else 1, c["q"])
        for q in ex: put("D", 2, q)
        for j, c in enumerate(D): put("D", 2 if j == 0 else 1, c["q"])
        assert sum(x["pts"] for x in items) == 30 and len(items) == 25
        assert any(x["type"] in ("grid", "table", "graph", "label", "scale") or x.get("fig") or x.get("data") for x in items), f"{U.pre}{P}: no diagram/data question"
        papers.append(items)
    return papers
