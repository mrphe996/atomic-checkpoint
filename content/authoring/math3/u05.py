# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 5 Measurement, area and perimeter (5.1 Measurement, 5.2 Perimeter, 5.3 Introducing area).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(5, "Measurement, Area and Perimeter", "Geometry and measure",
         "Measuring length in centimetres, metres and kilometres, finding the perimeter of shapes, and finding area by counting squares.",
         {"O1": {"code": "3Gm.01", "sec": "5.1", "codeNote": "", "t": "Estimate and measure lengths in centimetres, metres and kilometres, and convert between cm and m."},
          "O2": {"code": "3Gm.02", "sec": "5.2", "codeNote": "", "t": "Find the perimeter of 2D shapes by adding the lengths of the sides."},
          "O3": {"code": "3Gm.03", "sec": "5.3", "codeNote": "", "t": "Find the area of 2D shapes by counting squares."}})
OBJ = [("a pencil", "cm"), ("a football pitch", "m"), ("the distance between two towns", "km"), ("a finger", "cm"), ("a classroom", "m"), ("a long road", "km"), ("a book", "cm"), ("a swimming pool", "m")]

s = U.section("5.1", "Measurement", ["O1"])
s.idea("Units of length", ["We measure short things in **centimetres (cm)**, longer things in **metres (m)** and long distances in **kilometres (km)**.",
       "**100 cm = 1 m** and **1000 m = 1 km**. Line up the 0 on a ruler with the end of the object."], fig={"kind": "numline", "min": 0, "max": 10, "ticks": [], "mark": 7})
s.check(N("How many centimetres are in 2 metres?", 200, "cm", units=["cm"], o="O1"))
s.check(MC('Before you read on: which is longer, 1 m or 90 cm?', '1 m', [('90 cm', '1 m = 100 cm.'), ('They are equal', '100 cm is more than 90 cm.')], o='O1'))
s.mistake("Start at zero", ["Measure from the 0 mark, not from the end of the ruler."])


def m1(r):
    l = r.randint(2, 9)
    return N("The pencil reaches the arrow on the ruler. How long is it?", l, "cm", units=["cm"], o="O1", fig={"kind": "numline", "min": 0, "max": 10, "ticks": [], "mark": l})
def m2(r):
    m = r.randint(1, 9)
    return N(f"How many centimetres are in {m} metres?", 100 * m, "cm", units=["cm"], o="O1")
def m3(r):
    th, u = pick(r, OBJ)
    return MC(f"Which unit would you use to measure {th}?", u, [x for x in ["cm", "m", "km"] if x != u], o="O1")
def m4(r):
    ts = r.sample(OBJ, 4)
    return GD("Which unit is best for each length?", "Unit", ts, o="O1", extra=["cm", "m", "km"])
def m5(r):
    a, b = r.randint(10, 60), r.randint(10, 40)
    return N(f"A ribbon is {a} cm long. Another is {b} cm long. How long are they together?", a + b, "cm", units=["cm"], o="O1")
def m6(r):
    c = r.randint(1, 9) * 100
    return N(f"How many metres is {c} cm?", c // 100, "m", units=["m"], o="O1")
def m7(r):
    ls = r.sample(range(3, 30), 3); nm = ["red", "blue", "green"]
    k = ls.index(max(ls))
    return S("The table shows the lengths of three ribbons. Which ribbon is the longest?", [nm[k], nm[k].capitalize()], o="O1", data={"head": ["Ribbon", *nm], "rows": [["Length (cm)", *map(str, ls)]]})
def m8(r):
    m, c = r.randint(1, 5), r.randint(10, 90)
    return N(f"Write {m} m {c} cm in centimetres.", 100 * m + c, "cm", units=["cm"], o="O1", d="H")


s.std([m1, m7, m2, m3, m4, m5, m6, m8], EX("Explain how to measure a pencil with a ruler.", [("put the end of the pencil at 0", "0|zero"), ("read the number at the other end", "read|other end|tip")], "Line up one end of the pencil with the 0 on the ruler, then read the number at the other end. That is its length in centimetres.", o="O1"))

s = U.section("5.2", "Perimeter", ["O2"])
s.idea("Around the edge", ["The **perimeter** is the distance all the way around the edge of a shape.",
       "Add the lengths of all the sides: a rectangle 5 cm by 3 cm has perimeter 5 + 3 + 5 + 3 = **16 cm**."], fig=RECT(5, 3))
s.check(N("A square has sides of 4 cm. What is its perimeter?", 16, "cm", units=["cm"], o="O2"))
s.check(MC('Before you read on: a square has sides of 3 cm. What is its perimeter?', '12 cm', [('9 cm', 'That multiplies 3 by 3. Add all 4 sides.'), ('6 cm', 'There are 4 sides.')], o='O2'))
s.mistake("Count every side", ["A rectangle has 4 sides even if only 2 lengths are written."])


def p1(r):
    l, w = r.randint(2, 9), r.randint(1, 6)
    if l == w: return None
    return N("Find the perimeter of the rectangle.", 2 * (l + w), "cm", units=["cm"], o="O2", fig=RECT(l, w))
def p2(r):
    a, b, c = r.randint(3, 8), r.randint(3, 8), r.randint(3, 8)
    if a + b <= c or a + c <= b or b + c <= a: return None
    return N("Find the perimeter of the triangle.", a + b + c, "cm", units=["cm"], o="O2", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [3, 5]], "s": [f"{a} cm", f"{b} cm", f"{c} cm"]})
def p3(r):
    s_ = r.randint(2, 10)
    return N(f"A square has sides of {s_} cm. What is its perimeter?", 4 * s_, "cm", units=["cm"], o="O2")
def p4(r):
    l, w = r.randint(2, 6), r.randint(1, 4)
    return N("Each square is 1 cm long. What is the perimeter of the shaded rectangle?", 2 * (l + w), "cm", units=["cm"], o="O2", fig={"kind": "cells", "cells": [[i, j] for i in range(l) for j in range(w)]})
def p5(r):
    l, w = r.randint(5, 20), r.randint(3, 15)
    return N(f"A garden is {l} m long and {w} m wide. How much fence goes all the way round?", 2 * (l + w), "m", units=["m"], o="O2")
def p6(r):
    l, w = r.randint(2, 9), r.randint(1, 6)
    return TB("Complete the table for rectangles.", ["Length", "Width", "Perimeter"], [[f"{l} cm", f"{w} cm", B(2 * (l + w))]], o="O2")
def p7(r):
    n, s_ = r.randint(5, 6), r.randint(2, 6)
    return N(f"A shape has {n} sides, each {s_} cm long. What is its perimeter?", n * s_, "cm", units=["cm"], o="O2", d="H")
def p8(r):
    p = r.randint(3, 10) * 4
    return N(f"A square has a perimeter of {p} cm. How long is each side?", p // 4, "cm", units=["cm"], o="O2", d="H")


s.std([p1, p4, p2, p3, p5, p6, p7, p8], EX("Explain how to find the perimeter of a rectangle 6 cm by 2 cm.", [("add all four sides", "four|all|6 ?\\+ ?2"), ("6 + 2 + 6 + 2 = 16 cm", "16")], "Add the lengths of all four sides: 6 + 2 + 6 + 2 = 16 cm.", o="O2"))

s = U.section("5.3", "Introducing area", ["O3"])
s.idea("Counting squares", ["The **area** is the amount of space inside a shape. We can find it by **counting squares**.",
       "If each square is 1 square centimetre (**1 cm²**), a shape covering 8 squares has an area of **8 cm²**."], fig={"kind": "cells", "cells": [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1, 1], [2, 1], [3, 1]]})
s.check(N("A rectangle covers 3 rows of 4 squares. How many squares is that?", 12, "squares", units=["squares"], o="O3"))
s.check(MC('Before you read on: a shape covers 6 squares. What is its area?', '6 squares', [('4 squares', 'Count every square inside.'), ('12 squares', 'Count each square once.')], o='O3'))
s.mistake("Count each square once", ["Mark each square as you count so you don't count it twice."])


def a1(r):
    l, w = r.randint(2, 6), r.randint(2, 4)
    return N("Each square is 1 cm². What is the area of the shape?", l * w, "cm²", units=["cm²", "squares"], o="O3", fig={"kind": "cells", "cells": [[i, j] for i in range(l) for j in range(w)]})
def a2(r):
    cells = []
    while len(cells) < r.randint(5, 9):
        c = [r.randint(0, 4), r.randint(0, 3)]
        if c not in cells: cells.append(c)
    return N("Each square is 1 cm². What is the area of the shaded shape?", len(cells), "cm²", units=["cm²", "squares"], o="O3", fig={"kind": "cells", "cells": cells, "cols": 5, "rows": 4, "grid": True})
def a3(r):
    l, w = r.randint(2, 6), r.randint(2, 5)
    return N(f"A rectangle is made of {w} rows of {l} squares. What is its area in squares?", l * w, "squares", units=["squares", "cm²"], o="O3")
def a4(r):
    a, b = r.sample(range(4, 15), 2)
    return MC(f"Shape A covers {a} squares and shape B covers {b} squares. Which has the bigger area?", "A" if a > b else "B", ["B" if a > b else "A", "they are the same"], o="O3")
def a5(r):
    l, w = r.randint(2, 5), r.randint(2, 4)
    return TB("Complete the table.", ["Rows", "Squares in a row", "Area (squares)"], [[str(w), str(l), B(l * w)]], o="O3")
def a6(r):
    return MC("Which unit is used for area?", "square centimetres (cm²)", ["centimetres (cm)", "kilograms (kg)", "litres (l)"], o="O3")
def a7(r):
    l, w = r.randint(3, 6), r.randint(2, 4); k = r.randint(1, w * l - 2)
    return N(f"A rectangle of {w} rows of {l} squares has {k} squares coloured red. How many squares are not red?", l * w - k, "squares", units=["squares"], o="O3", d="H")
def a8(r):
    n = r.randint(2, 6)
    return N(f"A square has {n} squares along each side. What is its area in squares?", n * n, "squares", units=["squares", "cm²"], o="O3", d="H")


s.std([a1, a2, a3, a4, a5, a6, a7, a8], EX("Explain how to find the area of a shape on squared paper.", [("count the squares inside the shape", "count"), ("each square is 1 cm², so the number of squares is the area", "cm²|square centimetre|each square")], "Count the squares inside the shape. Each square is 1 cm², so the number of squares tells you the area in cm².", o="O3"))

U.mindmap(("Length", "cm • m • km • 100 cm = 1 m", "O1", "5.1"), ("Perimeter", "Add all the sides", "O2", "5.2"), ("Area", "Count squares • cm²", "O3", "5.3"))
