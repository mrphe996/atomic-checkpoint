"""Builds content/src/stage{g}-final.json (end-of-year exam: 10 papers x 50 marks, 60 min, Level 10)
from the practice and advanced pools of the built units. Each paper = one 3-mark block per unit (42)
+ two 4-mark written questions (8). Every unit's 10 blocks use different questions, so no two papers repeat.
Usage: python3 build_final_auto.py 8   (git-ignored output; answer keys stay private)."""
import json, os, sys, random, copy, re
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(H, "..", "src")
g = int(sys.argv[1])
rnd = random.Random(1000 + g)
STRUCT = ("grid", "table", "match", "order")


def clean(q, obj):
    q = copy.deepcopy(q)
    q["prompt"] = re.sub(r"^\*\s*Advanced\.\s*", "", q["prompt"])
    q["obj"] = obj
    for k in ("adv", "fbAll"):
        q.pop(k, None)
    return q


units, W, OBJ = {}, [], {}
for n in range(1, 15):
    d = json.load(open(os.path.join(SRC, f"stage{g}-unit{n:02d}.json")))
    o = f"U{n}"
    OBJ[o] = {"t": f"Unit {n}: {d['unit']['title']}", "code": f"Stage {g} Unit {n}"}
    st, m1, m2 = [], [], []
    for s in d["sections"]:
        for q in s["prac"]:
            if q["type"] in STRUCT: st.append(q)
            elif q["type"] == "mcq": (m2 if q.get("diff") in ("H", "VH") else m1).append(q)
        for q in s["adv"]:
            if q["type"] == "mcq": m2.append(q)
            elif q["type"] == "explain": W.append((o, q))
    for L in (st, m1, m2): rnd.shuffle(L)
    # short units (one section): top up from the Core pool so every paper still gets a different block
    if len(st) < 4:
        extra = [q for s in d["sections"] for q in s["req"] if q["type"] in STRUCT]; rnd.shuffle(extra); st += extra[: 4 - len(st)]
    st.sort(key=lambda q: q["type"] not in ("grid", "table"))  # data questions first
    nst = min(4, len(st))
    need = 10 - nst
    if len(m1) + len(m2) < 2 * need:
        extra = [q for s in d["sections"] for q in s["req"] if q["type"] == "mcq"]; rnd.shuffle(extra); m1 += extra
    allm = m2 + m1  # harder first
    m2, m1 = allm[:need], allm[need:]
    assert len(m1) >= need, (n, "not enough mcq", len(m1), need)
    blocks = [[(clean(q, o), 3)] for q in st[:nst]]
    for i in range(10 - nst):
        blocks.append([(clean(m1[i], o), 1), (clean(m2[i], o), 2)])
    rnd.shuffle(blocks)
    assert len(blocks) == 10, (n, len(blocks))
    units[n] = blocks

# every paper needs at least one diagram/data question: swap blocks between papers until it does
FIG = ("grid", "table", "graph")
isfig = lambda blk: any(q["type"] in FIG for q, _ in blk)
nfig = lambda k: sum(isfig(units[n][k]) for n in units)
for k in range(10):
    for n in units:
        if nfig(k): break
        for j in range(10):
            if j != k and nfig(j) > 1 and isfig(units[n][j]) and not isfig(units[n][k]):
                units[n][j], units[n][k] = units[n][k], units[n][j]; break
    assert nfig(k), ("no data question", k)

# 20 written questions spread across units
byu = {}
for o, q in W: byu.setdefault(o, []).append(q)
for L in byu.values(): rnd.shuffle(L)
order = []
while len(order) < 20:
    for o in sorted(byu, key=lambda x: int(x[1:])):
        if byu[o] and len(order) < 20: order.append((o, byu[o].pop()))
rnd.shuffle(order)


def paper(k):
    out = []
    for n in range(1, 15):
        for j, (q, pts) in enumerate(units[n][k]):
            q = dict(q); q["id"] = f"f{k+1:02d}u{n:02d}{'ab'[j]}"; q["pts"] = pts; out.append(q)
    for j in range(2):
        o, q = order[2 * k + j]
        q = clean(q, o); q["id"] = f"f{k+1:02d}w{j+1}"; q["pts"] = 4; q["diff"] = "VH"; out.append(q)
    return out


PAPERS = {f"{k+1:02d}": paper(k) for k in range(10)}
for k, p in PAPERS.items():
    assert sum(q["pts"] for q in p) == 50, (k, sum(q["pts"] for q in p))
    ids = [q["prompt"] for q in p]
out = {"final": True, "unit": {"title": "End-of-year exam", "stage": g}, "objectives": OBJ,
       "minutes": 60, "max": 50, "pass": 0.6, "level": 10, "papers": PAPERS}
json.dump(out, open(os.path.join(SRC, f"stage{g}-final.json"), "w"), ensure_ascii=False)
allp = [q["prompt"] for p in PAPERS.values() for q in p]
print("stage", g, "papers", len(PAPERS), "questions", len(allp), "distinct", len(set(allp)))
