# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 6 2D shapes (6.1 2D shapes and tessellation, 6.2 Symmetry).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(6, "2D Shapes", "Geometry and measure",
         "Naming and describing polygons by their sides and angles, regular and irregular shapes, tessellation, and lines of symmetry.",
         {"O1": {"code": "4Gg.01", "sec": "6.1", "codeNote": "", "t": "Identify, describe and sort 2D shapes, including regular and irregular polygons, and recognise shapes that tessellate."},
          "O2": {"code": "4Gg.02", "sec": "6.2", "codeNote": "", "t": "Identify lines of symmetry in 2D shapes and patterns, and complete symmetrical shapes."}})
POLY = {"triangle": 3, "quadrilateral": 4, "pentagon": 5, "hexagon": 6, "heptagon": 7, "octagon": 8}
PTS = {3: [[0, 0], [6, 0], [3, 5.2]], 4: [[0, 0], [5, 0], [5, 5], [0, 5]], 5: [[2, 0], [6, 0], [7.2, 3.8], [4, 6.2], [0.8, 3.8]],
       6: [[2, 0], [6, 0], [8, 3.46], [6, 6.93], [2, 6.93], [0, 3.46]], 8: [[2, 0], [5, 0], [7, 2], [7, 5], [5, 7], [2, 7], [0, 5], [0, 2]]}
IRR = {5: [[0, 0], [7, 0], [8, 3], [3, 6], [0, 4]], 6: [[0, 0], [5, 0], [7, 2], [6, 6], [1, 5], [-1, 2]], 4: [[0, 0], [7, 0], [5, 4], [1, 3]]}
LOS = {"square": 4, "rectangle": 2, "equilateral triangle": 3, "regular pentagon": 5, "regular hexagon": 6, "isosceles triangle": 1, "kite": 1, "regular octagon": 8}

s = U.section("6.1", "2D shapes and tessellation", ["O1"])
s.idea("Polygons", ["A **polygon** is a flat shape with straight sides. A pentagon has 5 sides, a hexagon 6, a heptagon 7, an octagon 8.",
       "A **regular** polygon has all sides and all angles equal. Shapes **tessellate** when they fit together with no gaps or overlaps, like squares on a floor."], fig={"kind": "shape", "pts": PTS[6]})
s.check(N("How many sides does an octagon have?", 8, "sides", units=["sides"], o="O1"))
s.check(MC('Before you read on: do regular hexagons tessellate (fit together with no gaps)?', 'Yes', [('No', 'Each angle is 120°, and 3 × 120° = 360°.'), ('Only squares do', 'Triangles and hexagons do too.')], o='O1'))
s.mistake("Irregular shapes count", ["A shape with 6 sides of different lengths is still a hexagon – an irregular one."])


def g1(r):
    n = pick(r, [3, 4, 5, 6, 8])
    nm = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 8: "octagon"}[n]
    return S("Name this polygon by its number of sides.", [nm, "a " + nm, "square" if n == 4 else nm, "equilateral triangle" if n == 3 else nm, f"regular {nm}"], o="O1", fig={"kind": "shape", "pts": PTS[n]})
def g2(r):
    n = pick(r, list(IRR)); nm = {4: "quadrilateral", 5: "pentagon", 6: "hexagon"}[n]
    return MC("This shape is irregular. What is it called?", f"an irregular {nm}", [f"a regular {nm}", f"an irregular {[k for k, v in POLY.items() if v == n + 1][0]}"], o="O1", fig={"kind": "shape", "pts": IRR[n]})
def g3(r):
    ns = r.sample(list(POLY), 4)
    return GD("How many sides does each polygon have?", "Sides", [(n, str(POLY[n])) for n in ns], o="O1", extra=[str(x) for x in range(3, 9)])
def g4(r):
    n, s_ = pick(r, [3, 4, 5, 6, 8]), r.randint(2, 9)
    nm = {3: "equilateral triangle", 4: "square", 5: "regular pentagon", 6: "regular hexagon", 8: "regular octagon"}[n]
    return N(f"A {nm} has sides of {s_} cm. What is its perimeter?", n * s_, "cm", units=["cm"], o="O1")
def g5(r):
    return MS("Select ALL the shapes that tessellate on their own.", r.sample(["square", "equilateral triangle", "regular hexagon", "rectangle"], 2), ["circle", "regular pentagon", "regular octagon"][:2], o="O1")
def g6(r):
    return MC("What does 'regular' mean for a polygon?", "all sides and angles are equal", ["it has 4 sides", "it has a right angle", "it can roll"], o="O1")
def g7(r):
    a, b = r.sample(list(POLY), 2)
    return N(f"How many sides do a {a} and a {b} have altogether?", POLY[a] + POLY[b], "sides", units=["sides"], o="O1", d="H")
def g8(r):
    p = r.randint(2, 9) * 6
    return N(f"A regular hexagon has a perimeter of {p} cm. How long is each side?", p // 6, "cm", units=["cm"], o="O1", d="H")


s.std([g1, g2, g3, g4, g5, g6, g7, g8], EX("Explain why squares tessellate but circles do not.", [("squares fit together with no gaps", "no gaps|fit"), ("circles leave gaps between them", "gaps|spaces")], "Squares fit together edge to edge with no gaps or overlaps, so they tessellate. Circles always leave gaps between them, so they do not.", o="O1"))

s = U.section("6.2", "Symmetry", ["O2"])
s.idea("Lines of symmetry", ["A **line of symmetry** divides a shape into two halves that are mirror images.",
       "A regular polygon has as many lines of symmetry as it has sides: a regular hexagon has 6."], fig={"kind": "cells", "cells": [[1, 0], [2, 0], [0, 1], [3, 1], [1, 2], [2, 2]], "cols": 4, "rows": 3, "grid": True, "mirror": {"x": 2}})
s.check(N("How many lines of symmetry does a regular pentagon have?", 5, o="O2"))
s.check(MC('Before you read on: how many lines of symmetry does an equilateral triangle have?', '3', [('1', 'There is one from each corner.'), ('0', 'Fold it from any corner to the middle of the opposite side.')], o='O2'))
s.mistake("Diagonals of rectangles", ["A rectangle's diagonals are not lines of symmetry."])


def y1(r):
    n = pick(r, [3, 4, 5, 6, 8])
    return N("How many lines of symmetry does this regular polygon have?", n, o="O2", fig={"kind": "shape", "pts": PTS[n]})
def y2(r):
    ns = r.sample(list(LOS), 4)
    return GD("How many lines of symmetry?", "Lines", [(n, str(LOS[n])) for n in ns], o="O2", extra=["1", "2", "3", "4", "5", "6", "8"])
def y3(r):
    n = pick(r, list(LOS))
    return N(f"How many lines of symmetry does a {n} have?", LOS[n], o="O2")
def y4(r):
    d = r.randint(1, 3)
    return N(f"A square is {d} squares to the left of the mirror line. How far to the right is its reflection, in squares?", d, "squares", units=["squares"], o="O2", fig={"kind": "cells", "cells": [[3 - d, 0]], "cols": 6, "rows": 1, "grid": True, "mirror": {"x": 3}})
def y5(r):
    k = r.randint(2, 7)
    return N(f"A symmetrical pattern has {k} shaded squares on one side of the mirror line and none on the line. How many shaded squares altogether?", 2 * k, "squares", units=["squares"], o="O2")
def y6(r):
    w = pick(r, "AHMTUVWXOBCDEK")
    v, h = w in "AHMTUVWXO", w in "BCDEKXHO"
    ans = "both" if v and h else "vertical" if v else "horizontal"
    return MC(f"Which line of symmetry does the capital letter {w} have?", ans, [x for x in ["vertical", "horizontal", "both", "none"] if x != ans][:3], o="O2")
def y7(r):
    return MC("Which shape has exactly 2 lines of symmetry?", "rectangle", ["square", "kite", "equilateral triangle"], o="O2")
def y8(r):
    a, b = r.sample(["square", "rectangle", "regular hexagon", "equilateral triangle"], 2)
    return N(f"How many lines of symmetry do a {a} and a {b} have altogether?", LOS[a] + LOS[b], "lines", units=["lines"], o="O2", d="H")


s.std([y1, y4, y2, y3, y5, y6, y7, y8], EX("Explain how to check if a line is a line of symmetry.", [("fold along the line / use a mirror", "fold|mirror"), ("the two halves must match exactly", "match|same|fit")], "Fold the shape along the line or put a mirror on it. If the two halves match exactly, it is a line of symmetry.", o="O2"))

U.mindmap(("Polygons", "Sides • regular and irregular • tessellation", "O1", "6.1"), ("Symmetry", "Mirror lines • regular polygons", "O2", "6.2"))
