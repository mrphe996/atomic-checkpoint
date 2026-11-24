# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 18 Position, direction and movement (18.1 Position and movement, 18.2 Reflecting 2D shapes).
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(18, "Position, Direction and Movement", "Geometry and measure",
         "Coordinates in the first quadrant, compass directions including NE, NW, SE and SW, translations, and reflecting shapes in mirror lines.",
         {"O1": {"code": "4Gp.01", "sec": "18.1", "codeNote": "", "t": "Read and plot coordinates, use compass directions and describe translations."},
          "O2": {"code": "4Gp.02", "sec": "18.2", "codeNote": "", "t": "Reflect 2D shapes in horizontal and vertical mirror lines."}})
Q = lambda pts=None, polys=None: G(pts, polys, rng=10, lo=0)
DIR8 = ["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"]

s = U.section("18.1", "Position and movement", ["O1"])
s.idea("Coordinates and directions", ["**Coordinates (x, y)**: go across first, then up. (5, 2) is 5 across and 2 up from the origin (0, 0).",
       "The 8 compass directions are N, NE, E, SE, S, SW, W and NW. A **translation** slides a shape: '3 right, 2 up' adds 3 to x and 2 to y."], fig=Q([{"x": 5, "y": 2, "l": "A"}, {"x": 2, "y": 6, "l": "B"}]))
s.check(S("Write the coordinates of a point 4 across and 7 up.", PP(4, 7), o="O1"))
s.mistake("Across first", ["(3, 6) and (6, 3) are different points."])


def p1(r):
    x, y = r.randint(1, 9), r.randint(1, 9)
    return S("Write the coordinates of point A.", PP(x, y), o="O1", fig=Q([{"x": x, "y": y, "l": "A"}]))
def p2(r):
    pts = [(r.randint(0, 9), r.randint(0, 9)) for _ in range(3)]
    return TB("Write the coordinates of each point.", ["Point", "x", "y"], [[l, B(x), B(y)] for l, (x, y) in zip("ABC", pts)], o="O1", fig=Q([{"x": x, "y": y, "l": l} for l, (x, y) in zip("ABC", pts)]))
def p3(r):
    x, y, dx, dy = r.randint(0, 5), r.randint(0, 5), r.randint(1, 4), r.randint(1, 4)
    return S(f"Point ({x}, {y}) is translated {dx} right and {dy} up. Write its new coordinates.", PP(x + dx, y + dy), o="O1")
def p4(r):
    k = r.randrange(8)
    return S(f"Which direction is opposite to {DIR8[k]}?", [DIR8[(k + 4) % 8], DIR8[(k + 4) % 8].lower()], o="O1")
def p5(r):
    k = r.randrange(8); n = pick(r, [1, 2]); e = DIR8[(k + n) % 8]
    return S(f"You face {DIR8[k]} and turn {'45° (an eighth of a turn)' if n == 1 else '90° (a right angle)'} clockwise. Which direction do you face now?", [e, e.lower()], o="O1", d="H")
def p6(r):
    x0, y0, w, h = r.randint(1, 4), r.randint(1, 4), r.randint(2, 4), r.randint(2, 4)
    return S("Three corners of a rectangle are shown. Write the fourth corner D.", PP(x0, y0 + h), o="O1", d="H", fig=Q([{"x": x0, "y": y0, "l": "A"}, {"x": x0 + w, "y": y0, "l": "B"}, {"x": x0 + w, "y": y0 + h, "l": "C"}]))
def p7(r):
    T = [[1, 1], [3, 1], [1, 3]]; dx, dy = r.randint(1, 5), r.randint(1, 5)
    return S("Shape A is translated to shape B. Describe the translation, like 3 right 2 up.", [f"{dx} right {dy} up", f"{dx} right and {dy} up", f"{dx} right, {dy} up"], o="O1", fig=Q(polys=[{"pts": T, "l": "A"}, {"pts": [[a + dx, b + dy] for a, b in T], "l": "B"}]))
def p8(r):
    x, y = r.randint(3, 8), r.randint(3, 8); dx, dy = r.randint(1, 3), r.randint(1, 3)
    return S(f"({x}, {y}) is translated {dx} left and {dy} down. Write the new coordinates.", PP(x - dx, y - dy), o="O1")


s.std([p1, p2, p7, p3, p4, p8, p6, p5], EX("Explain how to plot the point (6, 2).", [("start at the origin and go 6 across", "6 across|across 6|along"), ("then 2 up", "2 up|up 2")], "Start at the origin (0, 0). Go 6 across along the x-axis, then 2 up, and mark the point.", o="O1"))

s = U.section("18.2", "Reflecting 2D shapes", ["O2"])
s.idea("Mirror lines", ["When a shape is **reflected**, each point moves to the same distance on the other side of the **mirror line**.",
       "A reflection flips a shape: it is the same size, but faces the other way."], fig={"kind": "cells", "cells": [[0, 0], [1, 0], [1, 1], [4, 0], [3, 0], [3, 1]], "cols": 5, "rows": 2, "grid": True, "mirror": {"x": 2.5}})
s.check(N("A corner is 3 squares left of a vertical mirror line. How many squares right of the line is its reflection?", 3, "squares", units=["squares"], o="O2"))
s.mistake("Same distance", ["Count the squares to the mirror line, then the same number on the other side."])


def f1(r):
    d = r.randint(1, 3)
    return N("The shaded square is reflected in the red mirror line. How many squares right of the line is its reflection?", d, "squares", units=["squares"], o="O2", fig={"kind": "cells", "cells": [[3 - d, 0]], "cols": 6, "rows": 1, "grid": True, "mirror": {"x": 3}})
def f2(r):
    k = r.randint(1, 4); m = r.randint(5, 8); x, y = m - k, r.randint(1, 8)
    return S(f"The mirror line is the vertical line through x = {m}. Point ({x}, {y}) is reflected. Write its image.", PP(m + k, y), o="O2", d="H")
def f3(r):
    k = r.randint(1, 4); m = r.randint(5, 8); x, y = r.randint(1, 8), m - k
    return S(f"The mirror line is the horizontal line through y = {m}. Point ({x}, {y}) is reflected. Write its image.", PP(x, m + k), o="O2", d="H")
def f4(r):
    return MC("What stays the same when a shape is reflected?", "its size and shape", ["the way it faces", "its position", "nothing"], o="O2")
def f5(r):
    cells = [[0, 0], [1, 1], [0, 2]]
    return N("The shape is reflected in the red mirror line. How many shaded squares will there be altogether?", 6, "squares", units=["squares"], o="O2", fig={"kind": "cells", "cells": cells, "cols": 4, "rows": 3, "grid": True, "mirror": {"x": 2}})
def f6(r):
    ds = r.sample(range(1, 6), 3)
    return TB("A vertical mirror line is drawn. Complete the table.", ["Squares left of the line", "Squares right of the line (image)"], [[str(d), B(d)] for d in ds], o="O2")
def f7(r):
    return MC("Which word describes a reflected shape compared with the original?", "flipped", ["turned", "stretched", "shrunk"], o="O2")
def f8(r):
    d = r.randint(2, 7)
    return N(f"A point is {d} cm from a mirror line. How far is it from its reflection?", 2 * d, "cm", units=["cm"], o="O2", d="H")


s.std([f1, f5, f6, f4, f7, f2, f3, f8], EX("Explain how to reflect a shape in a vertical mirror line.", [("count how far each corner is from the line", "count|distance|how far"), ("plot it the same distance on the other side", "same distance|other side")], "For each corner, count how many squares it is from the mirror line, then mark a point the same distance on the other side. Join the points.", o="O2"))

U.mindmap(("Coordinates", "(x, y) • across then up", "O1", "18.1"), ("Movement", "8 compass points • translations", "O1", "18.1"), ("Reflection", "Same distance from the mirror line", "O2", "18.2"))
