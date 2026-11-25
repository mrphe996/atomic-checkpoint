# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 12 Data (12.1 Representing and interpreting data, 12.2 Frequency diagrams and line graphs).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(12, "Data", "Statistics and probability",
         "Tally charts, frequency tables, bar charts, dot plots and pictograms, frequency diagrams for grouped data, and line graphs showing change.",
         {"O1": {"code": "5Ss.01", "sec": "12.1", "codeNote": "", "t": "Record, organise, represent and interpret data in tables, bar charts, dot plots and pictograms."},
          "O2": {"code": "5Ss.02", "sec": "12.2", "codeNote": "", "t": "Represent and interpret grouped data in frequency diagrams and data that changes over time in line graphs."}})
PETS = ["Cat", "Dog", "Fish", "Bird", "Rabbit"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]


def BC(lab, v, ylab="Children", top=None):
    return {"kind": "barchart", "labels": lab, "values": v, "ymax": top or (max(v) // 2 + 2) * 2, "step": 2, "ylabel": ylab}


s = U.section("12.1", "Representing and interpreting data", ["O1"])
s.idea("Charts and tables", ["A **tally chart** records data as you collect it. A **frequency table** shows the totals. A **bar chart** shows each total as a bar.",
       "Always check the **scale**: if it goes up in 2s, a bar between 6 and 8 shows 7."], fig=BC(PETS[:4], [8, 12, 4, 6]))
s.check(N("In the bar chart, how many children chose dog?", 12, o="O1"))
s.check(MC("Before you read on: which graph best shows how a plant's height changes over 4 weeks?", 'A line graph', [('A pie chart', 'Pie charts show parts of a whole.'), ('A Venn diagram', 'Venn diagrams sort into groups.')], o='O1'))
s.mistake("Labels", ["Read the label under the bar you need, then read across to the scale."])


def b1(r):
    lab = r.sample(PETS, 4); v = [r.randint(1, 9) * 2 for _ in lab]; k = r.randrange(4)
    return N(f"The bar chart shows favourite pets. How many children chose {lab[k].lower()}?", v[k], o="O1", fig=BC(lab, v))
def b2(r):
    lab = r.sample(PETS, 4); v = [r.randint(1, 9) * 2 for _ in lab]; i, j = r.sample(range(4), 2)
    if v[i] == v[j]: return None
    a, b = (i, j) if v[i] > v[j] else (j, i)
    return N(f"How many more children chose {lab[a].lower()} than {lab[b].lower()}?", v[a] - v[b], o="O1", fig=BC(lab, v))
def b3(r):
    lab = r.sample(PETS, 4); v = [r.randint(1, 9) for _ in lab]
    return TB("Complete the frequency table from the tally marks.", ["Pet", "Tally", "Frequency"], [[l, "|" * x if x < 5 else "||||/ " + "|" * (x - 5), B(x)] for l, x in zip(lab, v)], o="O1")
def b4(r):
    lab = r.sample(PETS, 4); v = [r.randint(1, 9) * 2 for _ in lab]
    return N("How many children are shown in the bar chart altogether?", sum(v), "children", units=["children"], o="O1", fig=BC(lab, v))
def b5(r):
    xs = sorted(r.choices(range(0, 6), k=12))
    return N(f"A dot plot shows how many siblings 12 children have: {', '.join(map(str, xs))}. How many children have more than 2 siblings?", sum(1 for x in xs if x > 2), "children", units=["children"], o="O1", data={"head": ["Siblings", *map(str, range(6))], "rows": [["Dots", *["●" * xs.count(i) or "–" for i in range(6)]]]})
def b6(r):
    k = pick(r, [2, 4, 5, 10]); n = r.randint(2, 6)
    return N(f"In a pictogram one symbol stands for {k} children. How many children do {n} and a half symbols show?", n * k + k // 2, "children", units=["children"], o="O1", d="H") if k % 2 == 0 else N(f"In a pictogram one symbol stands for {k} children. How many children do {n} symbols show?", n * k, "children", units=["children"], o="O1")
def b7(r):
    lab = r.sample(PETS, 4); v = r.sample(range(2, 18, 2), 4); k = v.index(max(v))
    return S("Which pet is the most popular?", [lab[k], lab[k].lower()], o="O1", fig=BC(lab, v))
def b8(r):
    lab = r.sample(PETS, 3); v = [r.randint(2, 12) for _ in lab]
    return N(f"The table shows votes for class pets. How many votes were there altogether?", sum(v), "votes", units=["votes"], o="O1", data={"head": ["Pet", *lab], "rows": [["Votes", *map(str, v)]]})


s.std([b1, b3, b2, b4, b5, b7, b8, b6], EX("Explain how to read a bar that ends halfway between 6 and 8.", [("the scale goes up in 2s", "2s|twos|steps of 2"), ("halfway between 6 and 8 is 7", "\\b7\\b")], "The scale goes up in 2s, so halfway between 6 and 8 is 7. The bar shows 7.", o="O1"))

s = U.section("12.2", "Frequency diagrams and line graphs", ["O2"])
s.idea("Grouped data", ["When there are lots of different values, put them into **groups** such as 0–9, 10–19, 20–29. A **frequency diagram** shows how many are in each group.",
       "A **line graph** shows how something changes over time, like temperature through a day. Read across from a point to the scale."],
       fig={"kind": "linegraph", "x": {"min": 0, "max": 6, "step": 1, "label": "Hour"}, "y": {"min": 0, "max": 30, "step": 5, "label": "°C"}, "series": [{"pts": [[0, 12], [1, 15], [2, 20], [3, 24], [4, 23], [5, 19], [6, 16]]}]})
s.check(N("In the line graph, what was the temperature at hour 3?", 24, "°C", units=["°C"], o="O2"))
s.check(MC('Before you read on: in a frequency diagram, what does the height of a bar show?', 'How many are in that group', [('The size of the group', 'The width shows the group; the height shows how many.'), ('The average', 'It shows the frequency.')], o='O2'))
s.mistake("Between points", ["The line between two points gives an estimate of values in between."])
GRP = ["0–9", "10–19", "20–29", "30–39"]


def g1(r):
    v = [r.randint(1, 10) for _ in GRP]; k = r.randrange(4)
    return N(f"The frequency diagram shows quiz scores. How many children scored {GRP[k]}?", v[k], o="O2", fig=BC(GRP, v, "Frequency", 12))
def g2(r):
    v = [r.randint(1, 10) for _ in GRP]
    return N("The frequency diagram shows quiz scores. How many children scored less than 20?", v[0] + v[1], o="O2", fig=BC(GRP, v, "Frequency", 12), d="H")
def g3(r):
    ys = [r.randint(2, 14) * 2 for _ in range(5)]; k = r.randrange(5)
    return N(f"The line graph shows the temperature each day. What was it on {DAYS[k]}?", ys[k], "°C", units=["°C"], o="O2", fig={"kind": "linegraph", "x": {"min": 0, "max": 4, "step": 1, "label": "Day (0 = Mon)"}, "y": {"min": 0, "max": 30, "step": 2, "label": "°C"}, "series": [{"pts": [[i, y] for i, y in enumerate(ys)]}]})
def g4(r):
    ys = sorted(r.sample(range(2, 30), 5))
    return N("The line graph shows a plant's height each week. How much did it grow from week 1 to week 5?", ys[4] - ys[0], "cm", units=["cm"], o="O2", fig={"kind": "linegraph", "x": {"min": 1, "max": 5, "step": 1, "label": "Week"}, "y": {"min": 0, "max": 30, "step": 2, "label": "Height (cm)"}, "series": [{"pts": [[i + 1, y] for i, y in enumerate(ys)]}]})
def g5(r):
    xs = [r.randint(0, 39) for _ in range(12)]
    return TB(f"Scores: {', '.join(map(str, xs))}. Complete the grouped frequency table.", ["Score", "Frequency"], [[g, B(sum(1 for x in xs if 10 * i <= x <= 10 * i + 9))] for i, g in enumerate(GRP)], o="O2", d="H")
def g6(r):
    return MC("Which graph is best for showing how the temperature changes during a day?", "a line graph", ["a pictogram", "a tally chart", "a dot plot"], o="O2")
def g7(r):
    v = [r.randint(1, 10) for _ in GRP]
    if len(set(v)) < 4: return None
    k = v.index(max(v))
    return S("Which group has the most children? Write it like 10–19.", [GRP[k], GRP[k].replace("–", "-")], o="O2", fig=BC(GRP, v, "Frequency", 12))
def g8(r):
    a, b = r.randint(5, 15), r.randint(16, 28)
    return N(f"A line graph shows the temperature was {a} °C at 9 a.m. and {b} °C at 2 p.m. How much warmer was it at 2 p.m.?", b - a, "°C", units=["°C", "degrees"], o="O2")


s.std([g1, g3, g4, g7, g5, g6, g2, g8], EX("Explain why we put quiz scores into groups like 0–9 and 10–19.", [("there are lots of different values", "lots|many|different values"), ("groups make the data easier to show and read", "easier|clearer|simpler|fewer bars")], "There are lots of different scores, so a bar for each would be hard to read. Putting them into groups makes a frequency diagram with fewer bars that is easier to understand.", o="O2"))

U.mindmap(("Charts", "Tally • frequency table • bar chart • dot plot • pictogram", "O1", "12.1"), ("Grouped data", "Frequency diagrams", "O2", "12.2"), ("Line graphs", "Change over time", "O2", "12.2"))
