"""Find near-duplicate questions in a unit: inside each Unit Test paper, between papers A and B,
and between the papers and the unit's practice / video-stop questions.
Usage: python3 dedup_tests.py s7u03 [s7u04 ...]   (reads content/src/stageN-unitUU.json)"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STOP = set("a an the of to in on at for and or is are was were be by with as it its this that these those which what why how who when where "
           "do does did can could would should will from into than then so not no yes your you their they he she his her them each one two "
           "select correct statement following describe explain give use".split())


def words(q):
    t = (q.get("prompt") or "") + " " + " ".join(o.get("t", "") for o in q.get("options", []) if o.get("ok"))
    t = re.sub(r"^\([a-k]\)\s*", "", t.lower())
    return {w for w in re.findall(r"[a-z0-9]+", t) if w not in STOP and len(w) > 2}


def sim(a, b):
    return len(a & b) / max(1, len(a | b))


def check(key, lim_in=0.6, lim_prac=0.75):
    if key.startswith("m"): return check_maths(key)
    st, u = int(key[1]), int(key[3:5])
    d = json.load(open(os.path.join(HERE, "..", "src", f"stage{st}-unit{u:02d}.json"), encoding="utf-8"))
    A, B = d["tests"]["A"], d["tests"]["B"]
    prac = [q for s in d["sections"] for L in ("req", "prac", "adv") for q in s.get(L, [])] + [x["q"] for s in d["sections"] for x in s.get("stops", []) if x.get("q")]
    W = {id(q): words(q) for q in A + B + prac}
    out = []
    for name, P in (("A", A), ("B", B)):
        for i, x in enumerate(P):
            for y in P[i + 1:]:
                if sim(W[id(x)], W[id(y)]) >= lim_in: out.append((f"inside {name}", x["id"], y["id"], x["prompt"], y["prompt"]))
    for x in A:
        for y in B:
            if sim(W[id(x)], W[id(y)]) >= lim_in: out.append(("A vs B", x["id"], y["id"], x["prompt"], y["prompt"]))
    for x in A + B:
        for y in prac:
            if sim(W[id(x)], W[id(y)]) >= lim_prac: out.append(("test vs practice", x["id"], y["id"], x["prompt"], y["prompt"]))
    return out


def check_maths(key):
    """Maths (key m9u03 = Mathematics Stage 9 Unit 3): inside a paper, no two questions of the same kind (words, numbers and
    operation signs compared); papers A and B are parallel papers, so between them, and against practice, only a repeated
    question (same wording and same answer) counts."""
    sys.path.insert(0, os.path.join(HERE, "math9")); import mtest
    st, u = int(key[1:key.index("u")]), int(key[key.index("u") + 1:])
    d = json.load(open(os.path.join(HERE, "..", "src", f"stage{10 + st}-unit{u:02d}.json"), encoding="utf-8"))
    A, B = d["tests"]["A"], d["tests"]["B"]
    prac = [q for s in d["sections"] for L in ("req", "prac", "adv") for q in s.get(L, [])] + [x["q"] for s in d["sections"] for x in s.get("stops", []) if x.get("q")]
    clean = lambda q: re.sub(r"^\*\s*Advanced\.\s*", "", q.get("prompt") or "") + "|" + "|".join(str(q.get(k, "")) for k in ("answer", "rows", "pairs", "items", "text", "data", "fig", "head"))
    out = []
    for name, P in (("A", A), ("B", B)):
        for i, x in enumerate(P):
            for y in P[i + 1:]:
                if mtest.sim(mtest.words(x), mtest.words(y)) >= 0.6: out.append((f"inside {name}", x["id"], y["id"], x["prompt"], y["prompt"]))
    pk = {clean(q): q for q in prac}; ak = {clean(q): q for q in A}
    for y in B:
        if clean(y) in ak: out.append(("A vs B (repeated)", ak[clean(y)]["id"], y["id"], y["prompt"], ""))
    for x in A + B:
        if clean(x) in pk: out.append(("test vs practice (repeated)", x["id"], pk[clean(x)]["id"], x["prompt"], ""))
    return out


if __name__ == "__main__":
    bad = 0
    for k in sys.argv[1:]:
        r = check(k); bad += len(r)
        for w, a, b, pa, pb in r: print(f"{k} {w}: {a} ~ {b}\n   {pa[:90]}\n   {pb[:90]}")
        print(f"{k}: {len(r)} near-duplicates")
    sys.exit(1 if bad else 0)
