"""Builds content/src/stage19-final.json: Mathematics Stage 9 end-of-year exam, 10 papers x 50 marks, 75 minutes.
Each paper: one 3-mark block per unit (1-mark Medium question + 2-mark Hard question, from different sections) = 45,
plus a 2-mark Very Hard problem and a 3-mark written explanation = 50. Questions are drawn from the practice and
advanced pools of the 15 built units; no question is used twice across the 10 papers.
Usage: python3 build_final_math.py   (git-ignored output; answer keys stay private). Written by the Atomic teaching team."""
import json, os, random, copy, re
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(H, "..", "..", "src")
rnd = random.Random(1919)
AUTO = ("num", "expr", "mcq", "multi", "table", "grid", "match", "order", "short", "cloze")


def clean(q, obj):
    q = copy.deepcopy(q)
    q["prompt"] = re.sub(r"^\*\s*Advanced\.\s*", "", q["prompt"])
    q["obj"] = obj
    for k in ("adv", "fbAll"): q.pop(k, None)
    return q


units, OBJ, VH, W = {}, {}, [], []
for n in range(1, 16):
    d = json.load(open(os.path.join(SRC, f"stage19-unit{n:02d}.json")))
    o = f"U{n}"; OBJ[o] = {"t": f"Unit {n}: {d['unit']['title']}", "code": f"Stage 9 Mathematics Unit {n}"}
    easy, hard = [], []
    for s in d["sections"]:
        for q in s["prac"]:
            if q["type"] not in AUTO: continue
            (hard if q.get("diff") in ("H", "VH") else easy).append((s["id"], q))
        for q in s["adv"]:
            if q["type"] in ("num", "expr", "table"): VH.append((o, q))
            elif q["type"] == "explain": W.append((o, q))
        for q in s["req"]:
            if q["type"] == "explain": W.append((o, q))
    rnd.shuffle(easy); rnd.shuffle(hard)
    blocks, used = [], set()
    for k in range(10):
        h = next(x for x in hard if id(x[1]) not in used); used.add(id(h[1]))
        e = next((x for x in easy if id(x[1]) not in used and x[0] != h[0]), None) or next(x for x in easy if id(x[1]) not in used)
        used.add(id(e[1]))
        blocks.append([(clean(e[1], o), 1), (clean(h[1], o), 2)])
    units[n] = blocks

FIG = lambda q: q["type"] in ("grid", "table", "graph") or q.get("fig") or q.get("data")
for k in range(10):
    assert any(FIG(q) for n in units for q, _ in units[n][k]), ("no data question", k)

rnd.shuffle(VH); rnd.shuffle(W)
def spread(L, m):
    """take m items cycling through units so no unit dominates"""
    by = {}
    for o, q in L: by.setdefault(o, []).append(q)
    out = []
    while len(out) < m:
        for o in sorted(by, key=lambda x: int(x[1:])):
            if by[o] and len(out) < m: out.append((o, by[o].pop()))
    rnd.shuffle(out); return out
VH, W = spread(VH, 10), spread(W, 10)


def paper(k):
    out = []
    for n in range(1, 16):
        for j, (q, pts) in enumerate(units[n][k]):
            q = dict(q); q["id"] = f"m9f{k+1:02d}u{n:02d}{'ab'[j]}"; q["pts"] = pts; out.append(q)
    o, q = VH[k]; q = clean(q, o); q["id"] = f"m9f{k+1:02d}x1"; q["pts"] = 2; q["diff"] = "VH"; out.append(q)
    o, q = W[k]; q = clean(q, o); q["id"] = f"m9f{k+1:02d}w1"; q["pts"] = 3; q["diff"] = "VH"; out.append(q)
    return out


PAPERS = {f"{k+1:02d}": paper(k) for k in range(10)}
for k, p in PAPERS.items(): assert sum(q["pts"] for q in p) == 50, (k, sum(q["pts"] for q in p))
out = {"final": True, "unit": {"title": "End-of-year exam", "stage": 19, "subject": "Mathematics"}, "objectives": OBJ,
       "minutes": 75, "max": 50, "pass": 0.6, "level": 10, "papers": PAPERS}
json.dump(out, open(os.path.join(SRC, "stage19-final.json"), "w"), ensure_ascii=False)
allp = [q["prompt"] + str(q.get("data")) + str(q.get("fig")) for p in PAPERS.values() for q in p]
print("stage 19 papers", len(PAPERS), "questions", len(allp), "distinct", len(set(allp)))
