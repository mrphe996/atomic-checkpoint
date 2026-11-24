# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 15 Graphs (15.1 Pictograms and bar charts, 15.2 Venn and Carroll diagrams).
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(15, "Graphs", "Statistics and probability",
         "Reading and drawing pictograms and bar charts, and sorting data with Venn and Carroll diagrams.",
         {"O1": {"code": "3Ss.03", "sec": "15.1", "codeNote": "", "t": "Represent and interpret data in pictograms (where one picture stands for 2, 5 or 10) and bar charts."},
          "O2": {"code": "3Ss.04", "sec": "15.2", "codeNote": "", "t": "Sort numbers and objects using Venn and Carroll diagrams."}})
SP = ["Swim", "Run", "Dance", "Football"]


def BC(lab, v, top=None, step=2):
    return {"kind": "barchart", "labels": lab, "values": v, "ymax": top or (max(v) // step + 1) * step, "step": step, "ylabel": "Children"}


s = U.section("15.1", "Pictograms and bar charts", ["O1"])
s.idea("Pictures and bars", ["In a **pictogram**, one picture can stand for more than one: if ● = 2 children, then ●●● = 6 children and half a picture is 1.",
       "In a **bar chart**, read the top of each bar across to the scale."], fig=BC(SP, [6, 10, 4, 8]))
s.check(N("In the bar chart, how many children chose Run?", 10, "children", units=["children"], o="O1"))
s.mistake("Check the key", ["Always read the key: one picture might stand for 2, 5 or 10."])


def b1(r):
    v = [r.randint(1, 9) * 2 for _ in SP]; k = r.randrange(4)
    return N(f"How many children chose {SP[k]}?", v[k], "children", units=["children"], o="O1", fig=BC(SP, v))
def b2(r):
    v = r.sample(range(2, 20, 2), 4); i, j = r.sample(range(4), 2); a, b = (i, j) if v[i] > v[j] else (j, i)
    return N(f"How many more chose {SP[a]} than {SP[b]}?", v[a] - v[b], "children", units=["children"], o="O1", fig=BC(SP, v))
def b3(r):
    k = pick(r, [2, 5, 10]); n = [r.randint(1, 6) for _ in range(3)]; it = ["cats", "dogs", "fish"]; i = r.randrange(3)
    return N(f"In the pictogram, ● = {k} pets. How many {it[i]} are there?", n[i] * k, "pets", units=["pets"], o="O1", data={"head": ["Pet", "Pictures"], "rows": [[p, "●" * c] for p, c in zip(it, n)]})
def b4(r):
    n = [r.randint(1, 5) for _ in range(3)]; it = ["red", "blue", "green"]
    return TB("In the pictogram ● = 2 cars. Complete the table.", ["Colour", "Cars"], [[c, B(2 * x)] for c, x in zip(it, n)], o="O1", data={"head": ["Colour", "Pictures"], "rows": [[c, "●" * x] for c, x in zip(it, n)]})
def b5(r):
    v = [r.randint(1, 9) * 2 for _ in SP]
    return N("How many children are shown altogether?", sum(v), "children", units=["children"], o="O1", fig=BC(SP, v))
def b6(r):
    v = r.sample(range(2, 20, 2), 4); k = v.index(min(v))
    return S("Which activity is the least popular?", [SP[k], SP[k].lower()], o="O1", fig=BC(SP, v))
def b7(r):
    k = pick(r, [2, 10]); n = r.randint(2, 6)
    return N(f"In a pictogram ● = {k} children. How many children do {n} and a half pictures show?", n * k + k // 2, "children", units=["children"], o="O1", d="H")
def b8(r):
    k = pick(r, [2, 5]); t = k * r.randint(2, 8)
    return N(f"In a pictogram ● = {k}. How many pictures show {t}?", t // k, "pictures", units=["pictures"], o="O1", d="H")


s.std([b1, b3, b2, b4, b5, b6, b7, b8], EX("Explain how to read a pictogram where ● = 5 children and a row shows ●●●.", [("each picture is 5 children", "each|5"), ("3 × 5 = 15 children", "15")], "Each picture stands for 5 children. There are 3 pictures, so 3 × 5 = 15 children.", o="O1"))

s = U.section("15.2", "Venn and Carroll diagrams", ["O2"])
s.idea("Sorting", ["A **Venn diagram** uses circles to sort. Things that fit both rules go in the **overlap**. Things that fit neither go outside.",
       "A **Carroll diagram** uses a table: one rule across the top, the other down the side."], table={"head": ["", "even", "not even"], "rows": [["less than 10", "2, 6", "3, 7"], ["not less than 10", "12, 18", "11, 15"]]})
s.check(MC("In a Carroll diagram for 'even' and 'less than 10', where does 8 go?", "even and less than 10", [("not even and less than 10", ""), ("even and not less than 10", "")], o="O2"))
s.mistake("The overlap", ["A number that fits both rules goes in the overlap, not in just one circle."])


def v1(r):
    n = r.randint(1, 30)
    a, b = n % 2 == 0, n < 10
    ans = f"{'even' if a else 'not even'} and {'less than 10' if b else 'not less than 10'}"
    opts = [f"{x} and {y}" for x in ("even", "not even") for y in ("less than 10", "not less than 10")]
    return MC(f"Where does {n} go in a Carroll diagram for 'even' and 'less than 10'?", ans, [o for o in opts if o != ans], o="O2")
def v2(r):
    ns = r.sample(range(1, 40), 4)
    lab = lambda n: "both" if n % 2 == 0 and n % 5 == 0 else "even only" if n % 2 == 0 else "multiple of 5 only" if n % 5 == 0 else "neither"
    return GD("Sort into a Venn diagram: circle A 'even', circle B 'multiple of 5'.", "Region", [(str(n), lab(n)) for n in ns], o="O2", extra=["even only", "multiple of 5 only", "both", "neither"])
def v3(r):
    k = pick(r, [10, 20, 30])
    return MC(f"Which number goes in the overlap of 'even' and 'more than {k}'?", str(k + 2 * r.randint(1, 5)), [str(k - 2), str(k + 1), str(k - 3)], o="O2")
def v4(r):
    ns = r.sample(range(1, 30), 6)
    return N(f"Numbers: {', '.join(map(str, ns))}. How many go in the 'even' circle?", sum(1 for n in ns if n % 2 == 0), "numbers", units=["numbers"], o="O2")
def v5(r):
    ns = r.sample(range(1, 40), 6)
    return TB(f"Sort {', '.join(map(str, ns))} into a Carroll diagram. How many in each box?", ["", "even", "not even"], [["less than 20", B(sum(1 for n in ns if n % 2 == 0 and n < 20)), B(sum(1 for n in ns if n % 2 and n < 20))], ["not less than 20", B(sum(1 for n in ns if n % 2 == 0 and n >= 20)), B(sum(1 for n in ns if n % 2 and n >= 20))]], o="O2", d="H")
def v6(r):
    sh = r.sample([("square", "has 4 sides"), ("triangle", "not 4 sides"), ("rectangle", "has 4 sides"), ("circle", "not 4 sides"), ("pentagon", "not 4 sides"), ("kite", "has 4 sides")], 4)
    return GD("Sort the shapes for a Carroll diagram: 'has 4 sides' or 'not 4 sides'.", "Box", sh, o="O2", extra=["has 4 sides", "not 4 sides"])
def v7(r):
    a, b, c = r.randint(2, 8), r.randint(2, 8), r.randint(1, 5)
    return N(f"In a Venn diagram, {a} children are only in 'likes cats', {b} are only in 'likes dogs' and {c} are in the overlap. How many like cats?", a + c, "children", units=["children"], o="O2", d="H")
def v8(r):
    return MC("In a Venn diagram, where do things go that fit neither rule?", "outside the circles", ["in the overlap", "in the first circle", "they are left out"], o="O2")


s.std([v2, v5, v1, v3, v4, v6, v7, v8], EX("Explain where 15 goes in a Venn diagram with circles 'odd' and 'more than 10'.", [("15 is odd and more than 10", "odd|more than 10|both"), ("so it goes in the overlap", "overlap|middle|both circles")], "15 is odd and it is more than 10, so it fits both rules. It goes in the overlap where the circles cross.", o="O2"))

U.mindmap(("Pictograms", "Check the key • half pictures", "O1", "15.1"), ("Bar charts", "Read across to the scale", "O1", "15.1"), ("Sorting", "Venn • Carroll", "O2", "15.2"))
