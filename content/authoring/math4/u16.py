# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 16 Data display and interpretation (16.1 Pictograms and bar charts, 16.2 Dot plots and interpreting data).
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(16, "Data Display and Interpretation", "Statistics and probability",
         "Reading and drawing pictograms and bar charts with scales, dot plots, and using the mode to describe data.",
         {"O1": {"code": "4Ss.03", "sec": "16.1", "codeNote": "", "t": "Represent and interpret data in pictograms and bar charts with scales in 2s, 5s and 10s."},
          "O2": {"code": "4Ss.04", "sec": "16.2", "codeNote": "", "t": "Represent data in dot plots and use the mode to describe and compare data."}})
FR = ["apple", "banana", "mango", "grape"]


def BC(lab, v, step=2, ylab="Children"):
    return {"kind": "barchart", "labels": lab, "values": v, "ymax": (max(v) // step + 1) * step, "step": step, "ylabel": ylab}


s = U.section("16.1", "Pictograms and bar charts", ["O1"])
s.idea("Keys and scales", ["In a **pictogram**, the **key** tells you what one picture stands for: if ● = 5, then ●●● = 15 and half a picture is 1 when ● = 2.",
       "In a **bar chart**, the **scale** may go up in 2s, 5s or 10s. A bar halfway between 20 and 30 shows 25."], fig=BC(FR, [12, 18, 6, 14]))
s.check(N("In the bar chart, how many children chose banana?", 18, "children", units=["children"], o="O1"))
s.mistake("Read the scale", ["Count how much each grid line is worth before reading a bar."])


def b1(r):
    st = pick(r, [2, 5, 10]); v = [r.randint(1, 8) * st for _ in FR]; k = r.randrange(4)
    return N(f"The bar chart shows favourite fruit. How many chose {FR[k]}?", v[k], "children", units=["children"], o="O1", fig=BC(FR, v, st))
def b2(r):
    st = pick(r, [2, 5, 10]); v = r.sample(range(st, 9 * st, st), 4); i, j = r.sample(range(4), 2); a, b = (i, j) if v[i] > v[j] else (j, i)
    return N(f"How many more chose {FR[a]} than {FR[b]}?", v[a] - v[b], "children", units=["children"], o="O1", fig=BC(FR, v, st))
def b3(r):
    k = pick(r, [2, 5, 10]); n = [r.randint(1, 6) for _ in range(3)]; it = ["cats", "dogs", "fish"]; i = r.randrange(3)
    return N(f"In the pictogram ● = {k} pets. How many {it[i]}?", n[i] * k, "pets", units=["pets"], o="O1", data={"head": ["Pet", "Pictures"], "rows": [[p, "●" * c] for p, c in zip(it, n)]})
def b4(r):
    k = pick(r, [2, 10]); n = [r.randint(1, 5) for _ in range(3)]; it = ["red", "blue", "green"]
    return TB(f"In the pictogram ● = {k} cars. Complete the table.", ["Colour", "Cars"], [[c, B(k * x)] for c, x in zip(it, n)], o="O1", data={"head": ["Colour", "Pictures"], "rows": [[c, "●" * x] for c, x in zip(it, n)]})
def b5(r):
    st = pick(r, [2, 5]); v = [r.randint(1, 8) * st for _ in FR]
    return N("How many children are shown altogether?", sum(v), "children", units=["children"], o="O1", fig=BC(FR, v, st))
def b6(r):
    k = pick(r, [2, 10]); n = r.randint(2, 6)
    return N(f"In a pictogram ● = {k}. How many does {n} and a half pictures show?", n * k + k // 2, o="O1", d="H")
def b7(r):
    k = pick(r, [5, 10]); t = k * r.randint(2, 8)
    return N(f"In a pictogram ● = {k}. How many pictures show {t}?", t // k, "pictures", units=["pictures"], o="O1")
def b8(r):
    v = r.sample(range(2, 20, 2), 4); k = v.index(min(v))
    return S("Which fruit is the least popular?", [FR[k], FR[k].capitalize()], o="O1", fig=BC(FR, v))


s.std([b1, b3, b2, b4, b5, b8, b6, b7], EX("Explain how to read a bar that ends halfway between 40 and 50.", [("the scale goes up in 10s", "10s|tens|steps of 10"), ("halfway is 45", "45")], "The scale goes up in 10s, so halfway between 40 and 50 is 45. The bar shows 45.", o="O1"))

s = U.section("16.2", "Dot plots and interpreting data", ["O2"])
s.idea("Dot plots and the mode", ["A **dot plot** shows each piece of data as a dot above a number line.",
       "The **mode** is the value that appears most often – the tallest column of dots."], table={"head": ["Pets", "0", "1", "2", "3"], "rows": [["Dots", "●●", "●●●●●", "●●●", "●"]]})
s.check(N("In the dot plot above, what is the mode number of pets?", 1, o="O2"))
s.mistake("Mode is a value", ["The mode is the value (1 pet), not how many dots there are (5)."])


def d1(r):
    xs = sorted(r.choices(range(0, 6), k=12)); cs = sorted((xs.count(x) for x in set(xs)), reverse=True)
    if len(cs) > 1 and cs[0] == cs[1]: return None
    m = max(set(xs), key=xs.count)
    return N(f"The dot plot shows how many books 12 children read. What is the mode?", m, o="O2", data={"head": ["Books", *map(str, range(6))], "rows": [["Dots", *["●" * xs.count(i) or "–" for i in range(6)]]]})
def d2(r):
    xs = sorted(r.choices(range(0, 6), k=12)); k = r.randint(1, 4)
    return N(f"The dot plot shows the number of siblings children have. How many children have more than {k} siblings?", sum(1 for x in xs if x > k), "children", units=["children"], o="O2", data={"head": ["Siblings", *map(str, range(6))], "rows": [["Dots", *["●" * xs.count(i) or "–" for i in range(6)]]]})
def d3(r):
    xs = r.sample(range(1, 20), 4); m = pick(r, xs); xs = xs + [m, m]; r.shuffle(xs)
    return N(f"Find the mode of {', '.join(map(str, xs))}.", m, o="O2")
def d4(r):
    xs = r.choices(range(1, 5), k=10)
    return TB(f"Shoe sizes (small to large codes): {', '.join(map(str, xs))}. Count the dots for each.", ["Value", "1", "2", "3", "4"], [["Dots", *[B(xs.count(i)) for i in range(1, 5)]]], o="O2")
def d5(r):
    xs = r.choices(range(0, 6), k=r.randint(8, 14))
    return N(f"A dot plot has these values: {', '.join(map(str, sorted(xs)))}. How many dots are there?", len(xs), "dots", units=["dots"], o="O2")
def d6(r):
    a = r.sample(range(1, 10), 4); b = r.sample(range(1, 10), 4)
    ma, mb = max(a), max(b)
    return MC(f"Class A scored {', '.join(map(str, a))}. Class B scored {', '.join(map(str, b))}. Which class had the highest score?", "Class A" if ma > mb else "Class B" if mb > ma else "both the same", ["Class B" if ma > mb else "Class A", "both the same" if ma != mb else "Class A"], o="O2", d="H")
def d7(r):
    return MC("What does the mode tell you?", "the most common value", ["the biggest value", "the total", "the middle value"], o="O2")
def d8(r):
    xs = sorted(r.choices(range(0, 5), k=10))
    return N(f"The dot plot shows goals scored in 10 matches. How many goals were scored altogether?", sum(xs), "goals", units=["goals"], o="O2", d="H", data={"head": ["Goals", *map(str, range(5))], "rows": [["Dots", *["●" * xs.count(i) or "–" for i in range(5)]]]})


s.std([d1, d2, d3, d4, d5, d7, d6, d8], EX("Explain how to find the mode from a dot plot.", [("find the column with the most dots", "most dots|tallest|highest"), ("its value is the mode", "value|number|label")], "Look for the column with the most dots. The value under that column is the mode.", o="O2"))

U.mindmap(("Pictograms and bar charts", "Keys • scales in 2s, 5s, 10s", "O1", "16.1"), ("Dot plots", "One dot per value • mode", "O2", "16.2"))
