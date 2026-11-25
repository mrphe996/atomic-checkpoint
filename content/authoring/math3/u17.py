# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 17 Pattern and symmetry (17.1 Shape and symmetry, 17.2 Pattern and symmetry).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(17, "Pattern and Symmetry", "Geometry and measure",
         "Lines of symmetry in 2D shapes and letters, completing symmetrical shapes, and repeating and symmetrical patterns.",
         {"O1": {"code": "3Gg.04", "sec": "17.1", "codeNote": "", "t": "Identify 2D shapes and lines of symmetry, and complete symmetrical shapes."},
          "O2": {"code": "3Gg.05", "sec": "17.2", "codeNote": "", "t": "Recognise, continue and make repeating and symmetrical patterns."}})
LOS = {"square": 4, "rectangle": 2, "circle": "many", "equilateral triangle": 3, "regular hexagon": 6, "isosceles triangle": 1}
SH = {"square": [[0, 0], [4, 0], [4, 4], [0, 4]], "rectangle": [[0, 0], [7, 0], [7, 4], [0, 4]], "equilateral triangle": [[0, 0], [6, 0], [3, 5.2]], "isosceles triangle": [[0, 0], [5, 0], [2.5, 7]], "regular hexagon": [[2, 0], [6, 0], [8, 3.46], [6, 6.93], [2, 6.93], [0, 3.46]]}

s = U.section("17.1", "Shape and symmetry", ["O1"])
s.idea("Mirror lines", ["A **line of symmetry** splits a shape into two halves that match like a mirror. Fold along it and the halves fit exactly.",
       "A square has 4 lines of symmetry; a rectangle has 2."], fig={"kind": "cells", "cells": [[0, 0], [1, 0], [2, 1], [3, 1], [1, 1], [2, 0]], "cols": 4, "rows": 2, "grid": True, "mirror": {"x": 2}})
s.check(N("How many lines of symmetry does a square have?", 4, o="O1"))
s.check(MC('Before you read on: does a circle have a line of symmetry?', 'Yes – many', [('No', 'Fold a circle through its centre: the halves match.'), ('Only one', 'Any line through the centre works.')], o='O1'))
s.mistake("Diagonals of a rectangle", ["Folding a rectangle along its diagonal does not make the halves match."])


def y1(r):
    n = pick(r, list(SH))
    return N("How many lines of symmetry does this shape have?", LOS[n], o="O1", fig={"kind": "shape", "pts": SH[n]})
def y2(r):
    w = pick(r, "AHMTUVWXOBCDEK")
    v = w in "AHMTUVWXO"
    return MC(f"Does the capital letter {w} have a vertical line of symmetry?", "Yes" if v else "No", ["No" if v else "Yes"], o="O1")
def y3(r):
    ns = r.sample(list(SH), 4)
    return GD("How many lines of symmetry?", "Lines", [(n, str(LOS[n])) for n in ns], o="O1", extra=["1", "2", "3", "4", "6"])
def y4(r):
    k = r.randint(1, 4)
    return N(f"A pattern on squared paper is symmetrical. {k} squares are shaded on the left of the mirror line. How many are shaded altogether?", 2 * k, "squares", units=["squares"], o="O1")
def y5(r):
    d = r.randint(1, 3)
    return N(f"A square is {d} squares to the left of a mirror line. How many squares to the right is its reflection?", d, "squares", units=["squares"], o="O1", fig={"kind": "cells", "cells": [[3 - d, 0]], "cols": 6, "rows": 1, "grid": True, "mirror": {"x": 3}})
def y6(r):
    return MS("Select ALL the shapes with at least one line of symmetry.", ["square", "rectangle", "circle"][:r.randint(2, 3)], ["a scalene triangle (all sides different)"], o="O1")
def y7(r):
    return MC("Which line is a line of symmetry of a rectangle?", "a line down the middle", ["a line from corner to corner", "a line near one edge"], o="O1")
def y8(r):
    w = pick(r, ["MUM", "TOT", "WOW", "DAD", "BOB"])
    v = w in ("MUM", "TOT", "WOW")
    return MC(f"Does the word {w} have a vertical line of symmetry through its middle?", "Yes" if v else "No", ["No" if v else "Yes"], o="O1", d="H")


s.std([y1, y5, y2, y3, y4, y6, y7, y8], EX("Explain how to check whether a shape has a line of symmetry.", [("fold it along the line", "fold|mirror"), ("the two halves must match exactly", "match|same|fit")], "Fold the shape along the line (or use a mirror). If the two halves match exactly, it is a line of symmetry.", o="O1"))

s = U.section("17.2", "Pattern and symmetry", ["O2"])
s.idea("Repeating patterns", ["A **repeating pattern** uses the same group again and again: ▲●■ ▲●■ ▲●■ …",
       "To find what comes next, find the group that repeats. Some patterns are also symmetrical."], table={"head": ["1", "2", "3", "4", "5", "6"], "rows": [["▲", "●", "■", "▲", "●", "■"]]})
s.check(S("What comes next: red, blue, red, blue, red, …?", ["blue", "Blue"], o="O2"))
s.check(MC('Before you read on: a pattern goes red, blue, red, blue, … What colour is the 7th?', 'Red', [('Blue', 'Odd places are red.'), ('Green', 'Only red and blue repeat.')], o='O2'))
s.mistake("Find the whole group", ["In ▲●●▲●● the group is ▲●●, not ▲●."])
SYM = ["triangle", "circle", "square", "star"]


def p1(r):
    g = r.sample(SYM, r.randint(2, 3)); n = r.randint(5, 8); seq = [g[i % len(g)] for i in range(n)]
    return S(f"What comes next: {', '.join(seq)}, …?", [g[n % len(g)], g[n % len(g)].capitalize()], o="O2")
def p2(r):
    g = r.sample(SYM, 3); seq = [g[i % 3] for i in range(12)]; k = r.randint(7, 12)
    return S(f"The pattern {', '.join(seq[:6])}, … continues. What is shape number {k}?", [seq[k - 1], seq[k - 1].capitalize()], o="O2", d="H")
def p3(r):
    g = r.sample(["red", "blue", "green", "yellow"], r.randint(2, 3))
    return N(f"A bead pattern repeats {', '.join(g)}. How many beads are in the repeating group?", len(g), "beads", units=["beads"], o="O2")
def p4(r):
    g = r.sample(SYM, 2); n = r.randint(3, 6)
    return N(f"The group {g[0]}, {g[0]}, {g[1]} repeats {n} times. How many {g[0]}s are there?", 2 * n, o="O2")
def p5(r):
    a = r.randint(2, 5); k = r.randint(2, 4)
    return TB(f"A pattern adds {a} dots each step and starts with {a}. Complete it.", ["Step 1", "Step 2", "Step 3", "Step 4"], [[str(a), B(2 * a), B(3 * a), B(4 * a)]], o="O2")
def p6(r):
    cells = [[0, 0], [1, 1], [0, 2]]; mir = [[3, 0], [2, 1], [3, 2]]
    return N("The pattern is reflected in the red mirror line. How many shaded squares will there be altogether?", 6, "squares", units=["squares"], o="O2", fig={"kind": "cells", "cells": cells, "cols": 4, "rows": 3, "grid": True, "mirror": {"x": 2}})
def p7(r):
    g = r.sample(SYM, 3)
    return OD("Put the shapes in order to continue the pattern " + ", ".join(g * 2) + ", …", g, o="O2")
def p8(r):
    st, a = r.randint(1, 10), r.randint(2, 5)
    return N(f"A number pattern goes {st}, {st + a}, {st + 2 * a}, {st + 3 * a}, … What comes next?", st + 4 * a, o="O2")


s.std([p5, p6, p1, p2, p3, p4, p7, p8], EX("Explain how to find what comes next in ● ■ ■ ● ■ ■ ●.", [("the group ● ■ ■ repeats", "group|repeat|● ?■ ?■"), ("after ● comes ■", "■|square")], "The group ● ■ ■ repeats. The last shape shown is ●, the start of a new group, so the next shape is ■.", o="O2"))

U.mindmap(("Symmetry", "Fold to check • mirror lines", "O1", "17.1"), ("Patterns", "Find the repeating group", "O2", "17.2"))
