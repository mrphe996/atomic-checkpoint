# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 14 Area and perimeter (14.1 Perimeter, 14.2 Area).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(14, "Area and Perimeter", "Geometry and measure",
         "Finding the perimeter of rectangles and shapes made of rectangles, and the area of rectangles by counting squares and by multiplying.",
         {"O1": {"code": "5Gg.07", "sec": "14.1", "codeNote": "", "t": "Measure and calculate the perimeter of rectangles and simple compound shapes."},
          "O2": {"code": "5Gg.08", "sec": "14.2", "codeNote": "", "t": "Find the area of rectangles and shapes made from rectangles, in square centimetres and square metres."}})
LSH = lambda A, B, c, d: {"kind": "shape", "pts": [[0, 0], [A, 0], [A, B - d], [A - c, B - d], [A - c, B], [0, B]], "s": [f"{A} cm", f"{B - d} cm", f"{c} cm", f"{d} cm", f"{A - c} cm", f"{B} cm"]}

s = U.section("14.1", "Perimeter", ["O1"])
s.idea("The distance round", ["The **perimeter** is the total distance all the way round a shape. Add the lengths of all the sides.",
       "For a rectangle: perimeter = length + width + length + width = **2 × (length + width)**."], fig=RECT(6, 4))
s.check(N("A rectangle is 7 cm long and 3 cm wide. What is its perimeter?", 20, "cm", units=["cm"], o="O1"))
s.check(MC('Before you read on: what is the perimeter of a square with side 6 cm?', '24 cm', [('36 cm', 'That is the area (in cm²).'), ('12 cm', 'A square has 4 sides.')], o='O1'))
s.mistake("All the sides", ["A rectangle has 4 sides: don't just add the two lengths you can see labelled."])


def p1(r):
    l, w = r.randint(3, 15), r.randint(2, 10)
    return N("Find the perimeter of the rectangle.", 2 * (l + w), "cm", units=["cm"], o="O1", fig=RECT(l, w))
def p2(r):
    s_ = r.randint(2, 20)
    return N(f"A square has sides of {s_} cm. What is its perimeter?", 4 * s_, "cm", units=["cm"], o="O1")
def p3(r):
    A, B_, c, d = r.randint(6, 12), r.randint(5, 10), r.randint(2, 4), r.randint(2, 4)
    if c >= A or d >= B_: return None
    return N("Find the perimeter of the shape. All corners are right angles.", 2 * (A + B_), "cm", units=["cm"], o="O1", d="H", fig=LSH(A, B_, c, d))
def p4(r):
    l, w = r.randint(3, 12), r.randint(2, 9)
    return TB("Complete the table for rectangles.", ["Length", "Width", "Perimeter"], [[f"{l} cm", f"{w} cm", B(2 * (l + w))], [f"{w + 1} cm", f"{w + 1} cm", B(4 * (w + 1))]], o="O1")
def p5(r):
    l, w = r.randint(10, 40), r.randint(5, 20)
    return N(f"A garden is {l} m long and {w} m wide. How much fence goes all the way round it?", 2 * (l + w), "m", units=["m"], o="O1")
def p6(r):
    p, w = r.randint(10, 30) * 2, r.randint(2, 6)
    l = p // 2 - w
    if l <= w: return None
    return N(f"A rectangle has a perimeter of {p} cm and a width of {w} cm. How long is it?", l, "cm", units=["cm"], o="O1", d="H")
def p7(r):
    a, b, c = r.randint(3, 9), r.randint(3, 9), r.randint(3, 9)
    return N(f"A triangle has sides {a} cm, {b} cm and {c} cm. What is its perimeter?", a + b + c, "cm", units=["cm"], o="O1") if a + b > c and a + c > b and b + c > a else None
def p8(r):
    s_ = r.randint(2, 9)
    return N(f"A regular hexagon has sides of {s_} cm. What is its perimeter?", 6 * s_, "cm", units=["cm"], o="O1")


s.std([p1, p4, p2, p5, p7, p8, p3, p6], EX("Explain how to find the perimeter of a rectangle 8 cm by 5 cm.", [("add all four sides: 8 + 5 + 8 + 5", "8 ?\\+ ?5|all four|2 ?×"), ("the perimeter is 26 cm", "26")], "Add all four sides: 8 + 5 + 8 + 5 = 26 cm, or 2 × (8 + 5) = 26 cm.", o="O1"))

s = U.section("14.2", "Area", ["O2"])
s.idea("Counting squares", ["The **area** is the space inside a shape. We measure it in **square units**: square centimetres (**cm²**) or square metres (**m²**).",
       "A rectangle 5 cm by 3 cm has 3 rows of 5 squares: **area = length × width = 15 cm²**."], fig={"kind": "cells", "cells": [[i, j] for i in range(5) for j in range(3)]})
s.check(N("A rectangle is 6 cm by 4 cm. What is its area?", 24, "cm²", units=["cm²"], o="O2"))
s.check(MC('Before you read on: two rectangles have the same perimeter. Must they have the same area?', 'No', [('Yes', '2 × 6 and 3 × 5 both have perimeter 16 cm but areas 12 cm² and 15 cm².'), ('Only if they are squares', 'Try 2 × 6 and 3 × 5.')], o='O2'))
s.mistake("Area or perimeter?", ["Area counts the squares inside (cm²); perimeter measures the distance round (cm)."])


def a1(r):
    l, w = r.randint(2, 6), r.randint(2, 4)
    return N("Each square is 1 cm². What is the area of the rectangle?", l * w, "cm²", units=["cm²"], o="O2", fig={"kind": "cells", "cells": [[i, j] for i in range(l) for j in range(w)]})
def a2(r):
    l, w = r.randint(3, 15), r.randint(2, 10)
    return N("Find the area of the rectangle.", l * w, "cm²", units=["cm²"], o="O2", fig=RECT(l, w))
def a3(r):
    s_ = r.randint(2, 12)
    return N(f"A square has sides of {s_} cm. What is its area?", s_ * s_, "cm²", units=["cm²"], o="O2")
def a4(r):
    A, B_, c, d = r.randint(6, 12), r.randint(5, 10), r.randint(2, 4), r.randint(2, 4)
    if c >= A or d >= B_: return None
    return N("Find the area of the shape. Split it into two rectangles.", A * B_ - c * d, "cm²", units=["cm²"], o="O2", d="H", fig=LSH(A, B_, c, d))
def a5(r):
    w, l = r.randint(2, 9), r.randint(3, 12)
    return N(f"A rectangle has an area of {w * l} cm² and a width of {w} cm. How long is it?", l, "cm", units=["cm"], o="O2", d="H")
def a6(r):
    l, w = r.randint(3, 10), r.randint(2, 8)
    return N(f"A rug is {l} m by {w} m. What is its area?", l * w, "m²", units=["m²"], o="O2")
def a7(r):
    l, w = r.randint(3, 9), r.randint(2, 6)
    return TB("Complete the table.", ["Length", "Width", "Area", "Perimeter"], [[f"{l} cm", f"{w} cm", B(l * w), B(2 * (l + w))]], o="O2")
def a8(r):
    cells = []
    while len(cells) < 6:
        c = [r.randint(0, 4), r.randint(0, 3)]
        if c not in cells: cells.append(c)
    return N("Each square is 1 cm². What is the area of the shaded shape?", len(cells), "cm²", units=["cm²"], o="O2", fig={"kind": "cells", "cells": cells, "cols": 5, "rows": 4, "grid": True})


def f142(r):
    rows = r.sample([('A square has a bigger area than its perimeter', 'Sometimes true'), ('Area is measured in square units', 'Always true'), ('Doubling the sides of a square doubles its area', 'Never true')], 3)
    return GD('Is each statement always, sometimes or never true?', "Always / sometimes / never", rows, o='O2', d="H", extra=["Always true", "Sometimes true", "Never true"], reason='A 5 cm square has area 25 and perimeter 20, but a 2 cm square has area 4 and perimeter 8. Doubling the sides makes the area 4 times bigger.')


s.std([a1, a2, a8, a3, a6, a7, a4, a5], EX("Explain why a rectangle 4 cm by 3 cm has an area of 12 cm².", [("it has 3 rows of 4 squares", "rows|3 ?× ?4|4 ?× ?3"), ("3 × 4 = 12 squares of 1 cm²", "12")], "The rectangle can be split into 3 rows of 4 one-centimetre squares. 3 × 4 = 12 squares, so the area is 12 cm².", o="O2"),
      deep=[f142])

U.mindmap(("Perimeter", "Distance round • 2 × (l + w)", "O1", "14.1"), ("Area", "Squares inside • l × w • cm² and m²", "O2", "14.2"))
