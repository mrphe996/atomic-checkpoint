# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 18 Position and direction (18.1 Coordinates, 18.2 Translation).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(18, "Position and Direction", "Geometry and measure",
         "Reading and plotting coordinates in the first quadrant, finding missing vertices of shapes, and translating points and shapes on a grid.",
         {"O1": {"code": "5Gp.01", "sec": "18.1", "codeNote": "", "t": "Read and plot coordinates in the first quadrant, including vertices of shapes."},
          "O2": {"code": "5Gp.02", "sec": "18.2", "codeNote": "", "t": "Translate points and 2D shapes on coordinate grids and describe translations."}})
Q = lambda pts=None, polys=None: G(pts, polys, rng=10, lo=0)

s = U.section("18.1", "Coordinates", ["O1"])
s.idea("Across, then up", ["**Coordinates** give the position of a point: **(x, y)**. Go **across** the x-axis first, then **up** the y-axis.",
       "The point (0, 0) is called the **origin**. (4, 2) is 4 across and 2 up."], fig=Q([{"x": 4, "y": 2, "l": "A"}, {"x": 1, "y": 6, "l": "B"}]))
s.check(S("Write the coordinates of a point 3 across and 7 up from the origin.", PP(3, 7), o="O1"))
s.check(MC('Before you read on: in the coordinate (2, 5), which number tells you how far across?', '2', [('5', 'The first number is across (x).'), ('Both', 'Across comes first, then up.')], o='O1'))
s.mistake("Order matters", ["(2, 5) and (5, 2) are different points. x comes first."])


def c1(r):
    x, y = r.randint(1, 9), r.randint(1, 9)
    return S("Write the coordinates of point A.", PP(x, y), o="O1", fig=Q([{"x": x, "y": y, "l": "A"}]))
def c2(r):
    pts = [(r.randint(0, 9), r.randint(0, 9)) for _ in range(3)]
    return TB("Write the coordinates of each point.", ["Point", "x", "y"], [[l, B(x), B(y)] for l, (x, y) in zip("ABC", pts)], o="O1", fig=Q([{"x": x, "y": y, "l": l} for l, (x, y) in zip("ABC", pts)]))
def c3(r):
    x0, y0, w, h = r.randint(1, 4), r.randint(1, 4), r.randint(2, 5), r.randint(2, 5)
    return S("Three corners of a rectangle are shown. Write the coordinates of the fourth corner D.", PP(x0, y0 + h), o="O1", d="H", fig=Q([{"x": x0, "y": y0, "l": "A"}, {"x": x0 + w, "y": y0, "l": "B"}, {"x": x0 + w, "y": y0 + h, "l": "C"}]))
def c4(r):
    x, y = r.randint(1, 9), r.randint(1, 9)
    if x == y: return None
    return MC(f"Which point is 'across {x}, up {y}'?", f"({x}, {y})", [f"({y}, {x})", f"({x}, {x})", f"({y}, {y})"], o="O1")
def c5(r):
    y = r.randint(1, 9); a, b = sorted(r.sample(range(0, 10), 2))
    return N(f"How many units apart are ({a}, {y}) and ({b}, {y})?", b - a, "units", units=["units"], o="O1")
def c6(r):
    x0, y0, s_ = r.randint(1, 4), r.randint(1, 4), r.randint(2, 5)
    return S(f"A square has corners at ({x0}, {y0}), ({x0 + s_}, {y0}) and ({x0 + s_}, {y0 + s_}). Write the fourth corner.", PP(x0, y0 + s_), o="O1", d="H")
def c7(r):
    x, y = r.randint(1, 9), r.randint(1, 9)
    return N(f"What is the x-coordinate of the point ({x}, {y})?", x, o="O1")
def c8(r):
    x = r.randint(2, 8)
    if x == 7: x = 6
    return MS(f"Select ALL the points that lie on the line where x = {x}.", [f"({x}, 1)", f"({x}, 7)"], [f"(1, {x})", f"({x + 1}, {x})"], o="O1")


s.std([c1, c2, c4, c5, c7, c8, c3, c6], EX("Explain how to plot the point (6, 3).", [("start at the origin and go 6 across", "6 across|across 6|along"), ("then go 3 up", "3 up|up 3")], "Start at the origin (0, 0). Go 6 across along the x-axis, then 3 up. Mark the point there.", o="O1"))

s = U.section("18.2", "Translation", ["O2"])
s.idea("Sliding a shape", ["A **translation** slides a point or shape without turning or flipping it. Every point moves the same distance in the same direction.",
       "'3 right, 2 up' adds 3 to x and 2 to y: (1, 4) → (4, 6)."], fig=Q(polys=[{"pts": [[1, 1], [3, 1], [1, 3]], "l": "A"}, {"pts": [[5, 3], [7, 3], [5, 5]], "l": "B"}]))
s.check(S("(2, 5) is translated 4 right. Write the new coordinates.", PP(6, 5), o="O2"))
s.check(MC('Before you read on: does a translation change the size of a shape?', 'No', [('Yes', 'A translation only slides the shape.'), ('Only sometimes', 'It never changes the size.')], o='O2'))
s.mistake("Same shape", ["After a translation the shape is the same size and faces the same way."])


def t1(r):
    x, y = r.randint(0, 5), r.randint(0, 5); dx, dy = r.randint(1, 4), r.randint(1, 4)
    return S(f"Point A ({x}, {y}) is translated {dx} right and {dy} up. Write its new coordinates.", PP(x + dx, y + dy), o="O2", fig=Q([{"x": x, "y": y, "l": "A"}]))
def t2(r):
    x, y = r.randint(4, 9), r.randint(4, 9); dx, dy = r.randint(1, 3), r.randint(1, 3)
    return S(f"({x}, {y}) is translated {dx} left and {dy} down. Write the new coordinates.", PP(x - dx, y - dy), o="O2")
def t3(r):
    T = [[1, 1], [3, 1], [1, 3]]; dx, dy = r.randint(1, 5), r.randint(1, 5)
    return S("Shape A is translated to shape B. Describe the translation, like 3 right 2 up.", [f"{dx} right {dy} up", f"{dx} right and {dy} up", f"{dx} right, {dy} up"], o="O2", fig=Q(polys=[{"pts": T, "l": "A"}, {"pts": [[a + dx, b + dy] for a, b in T], "l": "B"}]))
def t4(r):
    pts = [(r.randint(0, 4), r.randint(0, 4)) for _ in range(2)]; dx, dy = r.randint(1, 4), r.randint(1, 4)
    return TB(f"Translate each point {dx} right and {dy} up.", ["Point", "New x", "New y"], [[f"({x}, {y})", B(x + dx), B(y + dy)] for x, y in pts], o="O2")
def t5(r):
    return MC("What changes when a shape is translated?", "its position", ["its size", "the direction it faces", "its shape"], o="O2")
def t6(r):
    x, y = r.randint(0, 5), r.randint(0, 5); dx, dy = r.randint(1, 4), r.randint(1, 4)
    return S(f"Point P moves from ({x}, {y}) to ({x + dx}, {y + dy}). Describe the translation.", [f"{dx} right {dy} up", f"{dx} right and {dy} up", f"{dx} right, {dy} up"], o="O2")
def t7(r):
    x, y = r.randint(1, 6), r.randint(1, 6); dx = r.randint(1, 3)
    return S(f"After a translation of {dx} right, a point is at ({x + dx}, {y}). Where did it start?", PP(x, y), o="O2", d="H")
def t8(r):
    a, b = r.randint(1, 4), r.randint(1, 4); c, d = r.randint(1, 4), r.randint(1, 4)
    return S(f"A point is translated {a} right and {b} up, then {c} right and {d} up. Describe one translation that does the same.", [f"{a + c} right {b + d} up", f"{a + c} right and {b + d} up", f"{a + c} right, {b + d} up"], o="O2", d="H")


s.std([t1, t3, t4, t2, t5, t6, t7, t8], EX("Explain how to translate (3, 2) by 4 right and 1 up.", [("add 4 to the x-coordinate: 7", "\\+ ?4|add 4|\\b7\\b"), ("add 1 to the y-coordinate: 3, so (7, 3)", "\\(7, ?3\\)|\\b3\\b")], "Moving right adds to x: 3 + 4 = 7. Moving up adds to y: 2 + 1 = 3. The new point is (7, 3).", o="O2"))

U.mindmap(("Coordinates", "(x, y) • across then up", "O1", "18.1"), ("Translation", "Slide • right/left changes x • up/down changes y", "O2", "18.2"))
