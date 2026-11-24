# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 15 Data (15.1 Bar charts, dot plots, waffle diagrams and pie charts;
15.2 Frequency diagrams, line graphs and scatter graphs). Written by the Atomic teaching team."""
from kit import *

U = Unit(15, "Data", "Statistics and probability",
         "Reading and drawing bar charts, dot plots, waffle diagrams and pie charts, grouped frequency diagrams, line graphs and scatter graphs.",
         {"O1": {"code": "6Ss.01", "sec": "15.1", "codeNote": "", "t": "Represent and interpret categorical data in bar charts, dot plots, waffle diagrams and pie charts."},
          "O2": {"code": "6Ss.02", "sec": "15.2", "codeNote": "", "t": "Represent and interpret grouped data in frequency diagrams, and data that changes over time in line graphs; read scatter graphs."}})
SPORTS = ["Football", "Tennis", "Swimming", "Cricket", "Basketball"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]


def bars(r, n=4):
    lab = r.sample(SPORTS, n); v = [r.randint(1, 10) * 2 for _ in lab]
    return lab, v


s = U.section("15.1", "Bar charts, dot plots, waffle diagrams and pie charts", ["O1"])
s.idea("Showing categories", ["A **bar chart** uses bars to show how many are in each group. Always read the **scale** on the axis carefully.",
       "A **dot plot** shows each value as a dot. A **waffle diagram** is a 10 × 10 grid: each square is **1%**. A **pie chart** shows each group as a slice of a circle."], fig={"kind": "barchart", "labels": SPORTS[:4], "values": [12, 6, 10, 4], "ymax": 14, "step": 2, "ylabel": "Children"})
s.check(N("In the bar chart, how many more children chose football than tennis?", 6, o="O1"))
s.mistake("Scale steps", ["If the scale goes up in 2s, a bar halfway between 8 and 10 shows 9."])


def b1(r):
    lab, v = bars(r); k = r.randrange(4)
    return N(f"The bar chart shows favourite sports. How many children chose {lab[k].lower()}?", v[k], o="O1", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 22, "step": 2, "ylabel": "Children"})
def b2(r):
    lab, v = bars(r)
    return N("How many children are shown in the bar chart altogether?", sum(v), o="O1", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 22, "step": 2, "ylabel": "Children"})
def b3(r):
    lab, v = bars(r)
    if len(set(v)) < 4: return None
    i, j = v.index(max(v)), v.index(min(v))
    return N(f"How many more chose the most popular sport than the least popular?", v[i] - v[j], o="O1", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 22, "step": 2, "ylabel": "Children"}, d="H")
def b4(r):
    p = r.randint(12, 88)
    return N("The waffle diagram shows the percentage of a class that walk to school. What percentage do NOT walk?", 100 - p, "%", units=["%"], o="O1", fig={"kind": "waffle", "n": p})
def b5(r):
    lab = ["Cat", "Dog", "Fish", "Rabbit"]; v = pick(r, [[50, 25, 15, 10], [40, 30, 20, 10], [25, 25, 40, 10], [30, 45, 15, 10]])
    k = v.index(max(v))
    return S("The pie chart shows favourite pets. Which pet is the most popular?", [lab[k], lab[k].lower()], o="O1", fig={"kind": "pie", "labels": lab, "values": v})
def b6(r):
    lab = ["Cat", "Dog", "Fish", "Rabbit"]; v = pick(r, [[50, 25, 15, 10], [40, 30, 20, 10], [25, 25, 40, 10]]); n = pick(r, [20, 40, 60, 100])
    k = r.randrange(4)
    if (v[k] * n) % 100: return None
    return N(f"{n} children were asked about favourite pets. The pie chart shows {lab[k].lower()} is {v[k]}%. How many chose {lab[k].lower()}?", v[k] * n // 100, "children", units=["children"], o="O1", d="H", fig={"kind": "pie", "labels": [f"{l} {x}%" for l, x in zip(lab, v)], "values": v})
def b7(r):
    xs = sorted(r.choices(range(1, 7), k=12))
    cs = sorted((xs.count(x) for x in set(xs)), reverse=True); m = max(set(xs), key=xs.count)
    if len(cs) > 1 and cs[0] == cs[1]: return None
    return N(f"A dot plot shows the number of pets owned by 12 children: {', '.join(map(str, xs))}. What is the mode?", m, o="O1", data={"head": ["Pets", *map(str, range(1, 7))], "rows": [["Dots", *["●" * xs.count(i) or "–" for i in range(1, 7)]]]})
def b8(r):
    lab, v = bars(r)
    return TB("Use the bar chart to complete the table.", ["Sport", "Children"], [[l, B(x)] for l, x in zip(lab[:3], v[:3])], o="O1", fig={"kind": "barchart", "labels": lab, "values": v, "ymax": 22, "step": 2, "ylabel": "Children"})


s.std([b1, b4, b2, b5, b8, b7, b3, b6], EX("Explain how to read a bar whose top is halfway between 10 and 12 on the scale.", [("the scale goes up in 2s", "2s|twos|step"), ("halfway between 10 and 12 is 11", "11")], "The scale goes up in 2s, so the gap from 10 to 12 is 2. Halfway is 1 more than 10, so the bar shows 11.", o="O1"))

s = U.section("15.2", "Frequency diagrams, line graphs and scatter graphs", ["O2"])
s.idea("Grouped data", ["A **frequency diagram** shows grouped data, such as heights 120–129 cm, 130–139 cm. The bars touch because the groups follow on from each other."],
       fig={"kind": "barchart", "labels": ["120–129", "130–139", "140–149", "150–159"], "values": [3, 8, 11, 5], "ymax": 12, "step": 2, "ylabel": "Frequency"})
s.idea("Line graphs and scatter graphs", ["A **line graph** shows how something changes over time, such as temperature through a day.",
       "A **scatter graph** plots pairs of values. If the points go up from left to right, as one value increases the other tends to increase."],
       fig={"kind": "linegraph", "x": {"min": 0, "max": 6, "step": 1, "label": "Hour"}, "y": {"min": 0, "max": 30, "step": 5, "label": "°C"}, "series": [{"pts": [[0, 10], [1, 14], [2, 19], [3, 24], [4, 22], [5, 18], [6, 15]]}]})
s.check(N("In the frequency diagram, how many children are 140–149 cm tall?", 11, o="O2"))
s.mistake("Read across carefully", ["Use a ruler to read across from a point to the axis."])
GRP = ["0–9", "10–19", "20–29", "30–39"]


def g1(r):
    v = [r.randint(1, 10) for _ in GRP]; k = r.randrange(4)
    return N(f"The frequency diagram shows test scores. How many scored {GRP[k]}?", v[k], o="O2", fig={"kind": "barchart", "labels": GRP, "values": v, "ymax": 12, "step": 2, "ylabel": "Frequency"})
def g2(r):
    v = [r.randint(1, 10) for _ in GRP]
    return N("The frequency diagram shows test scores. How many students scored 20 or more?", v[2] + v[3], o="O2", fig={"kind": "barchart", "labels": GRP, "values": v, "ymax": 12, "step": 2, "ylabel": "Frequency"}, d="H")
def g3(r):
    ys = [r.randint(2, 12) * 2 for _ in range(6)]; k = r.randrange(6)
    return N(f"The line graph shows rainfall each month. How much rain fell in {MONTHS[k]}?", ys[k], "mm", units=["mm"], o="O2", fig={"kind": "linegraph", "x": {"min": 0, "max": 5, "step": 1, "label": "Month (0 = Jan)"}, "y": {"min": 0, "max": 26, "step": 2, "label": "Rain (mm)"}, "series": [{"pts": [[i, y] for i, y in enumerate(ys)]}]})
def g4(r):
    ys = [r.randint(2, 12) * 2 for _ in range(6)]
    if len(set(ys)) < 6: return None
    k = ys.index(max(ys))
    return S("The line graph shows rainfall for January (0) to June (5). In which month was it wettest? Write the month's short name.", [MONTHS[k], MONTHS[k].lower()], o="O2", fig={"kind": "linegraph", "x": {"min": 0, "max": 5, "step": 1, "label": "Month (0 = Jan)"}, "y": {"min": 0, "max": 26, "step": 2, "label": "Rain (mm)"}, "series": [{"pts": [[i, y] for i, y in enumerate(ys)]}]})
def g5(r):
    v = [r.randint(1, 10) for _ in GRP]
    return TB("Complete the frequency table from the diagram.", ["Score", "Frequency"], [[g, B(x)] for g, x in zip(GRP, v)], o="O2", fig={"kind": "barchart", "labels": GRP, "values": v, "ymax": 12, "step": 2, "ylabel": "Frequency"})
def g6(r):
    up = r.random() < 0.5
    pts = [{"x": x, "y": (x * 2 + r.randint(-2, 2)) if up else (20 - x * 2 + r.randint(-2, 2))} for x in range(1, 9)]
    return MC("The scatter graph shows hours of practice and test score. What does it show?", "More practice, higher score" if up else "More practice, lower score", ["More practice, lower score" if up else "More practice, higher score", "No link at all"], o="O2", fig={"kind": "coord", "x": [0, 9], "y": [0, 22], "points": pts})
def g7(r):
    a, b = r.randint(5, 15), r.randint(16, 30)
    return N(f"A line graph shows the temperature rising from {a} °C at 8:00 to {b} °C at 12:00. By how much did it rise?", b - a, "°C", units=["°C", "degrees"], o="O2")
def g8(r):
    hs = [r.randint(120, 159) for _ in range(10)]
    return TB(f"Heights (cm): {', '.join(map(str, hs))}. Complete the frequency table.", ["Height (cm)", "Frequency"], [[f"{a}–{a + 9}", B(sum(1 for h in hs if a <= h <= a + 9))] for a in (120, 130, 140, 150)], o="O2", d="H")


s.std([g1, g3, g5, g6, g4, g7, g2, g8], EX("Explain why the bars in a frequency diagram for heights touch.", [("the data are grouped and continuous", "continuous|grouped|groups"), ("one group follows straight on from the next", "follow|no gap|next")], "Height is measured data that is grouped. Each group follows straight on from the one before, with no gaps, so the bars touch.", o="O2"))

U.mindmap(("Categorical data", "Bar chart • dot plot • waffle • pie chart", "O1", "15.1"), ("Grouped data", "Frequency diagrams • bars touch", "O2", "15.2"), ("Change and links", "Line graphs • scatter graphs", "O2", "15.2"))
