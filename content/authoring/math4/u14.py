# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 14 Area and perimeter (14.1 Estimating and measuring area and perimeter,
14.2 Area and perimeter of rectangles). Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(14, "Area and Perimeter", "Geometry and measure",
         "Finding area by counting whole and half squares, measuring perimeter, and calculating the area and perimeter of rectangles.",
         {"O1": {"code": "4Gm.01", "sec": "14.1", "codeNote": "", "t": "Estimate and measure the area and perimeter of 2D shapes on squared paper."},
          "O2": {"code": "4Gm.02", "sec": "14.2", "codeNote": "", "t": "Calculate the area and perimeter of rectangles."}})
LSH = lambda A, B_, c, d: {"kind": "shape", "pts": [[0, 0], [A, 0], [A, B_ - d], [A - c, B_ - d], [A - c, B_], [0, B_]], "s": [f"{A} cm", f"{B_ - d} cm", f"{c} cm", f"{d} cm", f"{A - c} cm", f"{B_} cm"]}

s = U.section("14.1", "Estimating and measuring area and perimeter", ["O1"])
s.idea("Squares and edges", ["**Area** is the space inside a shape, measured in **square centimetres (cm²)**. Count the whole squares inside.",
       "**Perimeter** is the distance around the edge. On squared paper, count the edges of the squares all the way round."], fig={"kind": "cells", "cells": [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1]], "cols": 4, "rows": 3, "grid": True})
s.check(N("A shape covers 9 whole squares of 1 cm². What is its area?", 9, "cm²", units=["cm²"], o="O1"))
s.mistake("Area or perimeter?", ["Area counts squares inside; perimeter counts the edges around."])


def m1(r):
    cells = []
    while len(cells) < r.randint(5, 10):
        c = [r.randint(0, 4), r.randint(0, 3)]
        if c not in cells: cells.append(c)
    return N("Each square is 1 cm². What is the area of the shaded shape?", len(cells), "cm²", units=["cm²"], o="O1", fig={"kind": "cells", "cells": cells, "cols": 5, "rows": 4, "grid": True})
def m2(r):
    l, w = r.randint(2, 6), r.randint(1, 4)
    return N("Each square has sides of 1 cm. What is the perimeter of the shaded rectangle?", 2 * (l + w), "cm", units=["cm"], o="O1", fig={"kind": "cells", "cells": [[i, j] for i in range(l) for j in range(w)]})
def m3(r):
    a, b, c = r.randint(3, 9), r.randint(3, 9), r.randint(3, 9)
    if a + b <= c or a + c <= b or b + c <= a: return None
    return N("Find the perimeter of the triangle.", a + b + c, "cm", units=["cm"], o="O1", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [3, 5]], "s": [f"{a} cm", f"{b} cm", f"{c} cm"]})
def m4(r):
    w, h = r.randint(4, 12), r.randint(1, 4)
    return N(f"A leaf covers {w} whole squares and {2 * h} half squares on 1 cm² paper. Two halves make one square. What is its area?", w + h, "cm²", units=["cm²"], o="O1", d="H")
def m5(r):
    return MC("Which unit is used to measure area?", "cm²", ["cm", "kg", "ml"], o="O1")
def m6(r):
    n, s_ = r.randint(5, 8), r.randint(2, 6)
    return N(f"A shape has {n} sides, each {s_} cm long. What is its perimeter?", n * s_, "cm", units=["cm"], o="O1")
def m7(r):
    a, b = r.sample(range(4, 15), 2)
    return MC(f"Shape A covers {a} squares and shape B covers {b} squares. Which has the larger area?", "A" if a > b else "B", ["B" if a > b else "A", "they are equal"], o="O1")
def m8(r):
    l, w = r.randint(2, 6), r.randint(2, 4)
    return TB("The rectangle is drawn on 1 cm squares. Complete the table.", ["Area (cm²)", "Perimeter (cm)"], [[B(l * w), B(2 * (l + w))]], o="O1", fig={"kind": "cells", "cells": [[i, j] for i in range(l) for j in range(w)]})


s.std([m1, m2, m8, m3, m5, m6, m7, m4], EX("Explain how to find the perimeter of a shape on squared paper.", [("count the edges all the way round", "edges|around|round"), ("each edge is 1 cm", "1 cm|each")], "Start at a corner and count every square edge along the outside, all the way round. Each edge is 1 cm, so the total is the perimeter in cm.", o="O1"))

s = U.section("14.2", "Area and perimeter of rectangles", ["O2"])
s.idea("Formulas for rectangles", ["**Area of a rectangle = length × width**. A 7 cm by 4 cm rectangle has area 28 cm².",
       "**Perimeter = length + width + length + width**, or 2 × (length + width) = 22 cm."], fig=RECT(7, 4))
s.check(N("A rectangle is 6 cm by 5 cm. What is its area?", 30, "cm²", units=["cm²"], o="O2"))
s.mistake("Units", ["Area is in cm², perimeter in cm."])


def r1(r):
    l, w = r.randint(3, 12), r.randint(2, 9)
    return N("Find the area of the rectangle.", l * w, "cm²", units=["cm²"], o="O2", fig=RECT(l, w))
def r2(r):
    l, w = r.randint(3, 12), r.randint(2, 9)
    return N("Find the perimeter of the rectangle.", 2 * (l + w), "cm", units=["cm"], o="O2", fig=RECT(l, w))
def r3(r):
    l, w = r.randint(3, 12), r.randint(2, 9)
    return TB("Complete the table for rectangles.", ["Length", "Width", "Area", "Perimeter"], [[f"{l} cm", f"{w} cm", B(l * w), B(2 * (l + w))]], o="O2")
def r4(r):
    s_ = r.randint(2, 12)
    return N(f"A square has sides of {s_} cm. What is its area?", s_ * s_, "cm²", units=["cm²"], o="O2")
def r5(r):
    w, l = r.randint(2, 9), r.randint(3, 12)
    return N(f"A rectangle has an area of {w * l} cm² and a width of {w} cm. How long is it?", l, "cm", units=["cm"], o="O2", d="H")
def r6(r):
    l, w = r.randint(5, 20), r.randint(3, 15)
    return N(f"A playground is {l} m by {w} m. How much fencing goes all the way round it?", 2 * (l + w), "m", units=["m"], o="O2")
def r7(r):
    A, B_, c, d = r.randint(6, 12), r.randint(5, 10), r.randint(2, 4), r.randint(2, 4)
    if c >= A or d >= B_: return None
    return N("Find the area of the L-shape. Split it into two rectangles.", A * B_ - c * d, "cm²", units=["cm²"], o="O2", d="H", fig=LSH(A, B_, c, d))
def r8(r):
    l, w = r.randint(3, 9), r.randint(2, 6)
    return N(f"A rug is {l} m by {w} m. What is its area?", l * w, "m²", units=["m²"], o="O2")


s.std([r1, r2, r3, r4, r6, r8, r5, r7], EX("Explain why the area of a rectangle is length × width.", [("the rectangle has rows of squares", "rows|squares"), ("rows × squares in each row = length × width", "×|times|multiply")], "A rectangle is made of equal rows of 1 cm squares. The number of rows is the width and each row has 'length' squares, so the area is length × width.", o="O2"))

U.mindmap(("Measuring", "Count squares (area) • count edges (perimeter)", "O1", "14.1"), ("Rectangles", "Area = l × w • perimeter = 2 × (l + w)", "O2", "14.2"))
