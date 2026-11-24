# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 17 Transformations (17.1 Coordinates, 17.2 Reflections, 17.3 Rotations).
Written by the Atomic teaching team."""
from kit import *

U = Unit(17, "Transformations", "Geometry and measure",
         "Reading and plotting coordinates in all four quadrants, translating, reflecting in horizontal, vertical and diagonal lines, and rotating shapes by 90° about a vertex.",
         {"O1": {"code": "6Gp.01", "sec": "17.1", "codeNote": "", "t": "Read and plot coordinates in all four quadrants, and translate shapes."},
          "O2": {"code": "6Gp.02", "sec": "17.2", "codeNote": "", "t": "Reflect 2D shapes in horizontal, vertical and diagonal mirror lines."},
          "O3": {"code": "6Gp.03", "sec": "17.3", "codeNote": "", "t": "Rotate shapes 90° about a vertex, clockwise or anticlockwise."}})
G = lambda pts=None, polys=None, lines=None, rng=6: {"kind": "coord", "x": [-rng, rng], "y": [-rng, rng], **({"points": pts} if pts else {}), **({"polys": polys} if polys else {}), **({"lines": lines} if lines else {})}
def sg(v): return f"−{-v}" if v < 0 else str(v)
def PP(x, y): return [f"({x}, {y})", f"({x},{y})", f"({sg(x)}, {sg(y)})", f"({sg(x)},{sg(y)})", f"{sg(x)}, {sg(y)}"]

s = U.section("17.1", "Coordinates", ["O1"])
s.idea("Four quadrants", ["A point is written **(x, y)**: go **across** first, then **up or down**. (−3, 2) is 3 left and 2 up.",
       "The axes cross at the **origin** (0, 0). Negative x is left; negative y is down."], fig=G([{"x": -3, "y": 2, "l": "A"}, {"x": 4, "y": -1, "l": "B"}]))
s.check(S("Write the coordinates of a point 5 right and 2 down from the origin.", PP(5, -2), o="O1"))
s.idea("Translation", ["A **translation** slides a shape without turning it. 'Move 3 right and 2 down' adds 3 to x and takes 2 from y."])
s.mistake("Across, then up", ["(2, 5) and (5, 2) are different points: x always comes first."])


def c1(r):
    x, y = r.randint(-5, 5), r.randint(-5, 5)
    if x == 0 or y == 0: return None
    return S("Write the coordinates of point A.", PP(x, y), o="O1", fig=G([{"x": x, "y": y, "l": "A"}]))
def c2(r):
    x, y = r.randint(-5, 5), r.randint(-5, 5); dx, dy = r.randint(-4, 4), r.randint(-4, 4)
    if dx == 0 or dy == 0: return None
    d = f"{abs(dx)} {'right' if dx > 0 else 'left'} and {abs(dy)} {'up' if dy > 0 else 'down'}"
    return S(f"The point ({sg(x)}, {sg(y)}) is translated {d}. Write its new coordinates.", PP(x + dx, y + dy), o="O1")
def c3(r):
    x, y = r.randint(1, 5) * pick(r, [-1, 1]), r.randint(1, 5) * pick(r, [-1, 1])
    q = "first" if x > 0 and y > 0 else "second" if x < 0 < y else "third" if x < 0 and y < 0 else "fourth"
    return MC(f"In which quadrant is ({sg(x)}, {sg(y)})?", q, [w for w in ["first", "second", "third", "fourth"] if w != q], o="O1")
def c4(r):
    x0, y0, w, h = r.randint(-5, 0), r.randint(-5, 0), r.randint(2, 4), r.randint(2, 4)
    return S("Three corners of a rectangle are shown. Write the coordinates of the fourth corner.", PP(x0, y0 + h), o="O1", d="H", fig=G([{"x": x0, "y": y0, "l": "A"}, {"x": x0 + w, "y": y0, "l": "B"}, {"x": x0 + w, "y": y0 + h, "l": "C"}]))
def c5(r):
    pts = [(r.randint(-5, 5), r.randint(-5, 5)) for _ in range(3)]
    return TB("Complete the table for the points.", ["Point", "x", "y"], [[l, B(x), B(y)] for l, (x, y) in zip("ABC", pts)], o="O1", fig=G([{"x": x, "y": y, "l": l} for l, (x, y) in zip("ABC", pts)]))
def c6(r):
    y = r.randint(-5, 5); a, b = sorted(r.sample(range(-6, 7), 2))
    return N(f"How far is it from ({sg(a)}, {sg(y)}) to ({sg(b)}, {sg(y)})?", b - a, "units", units=["units"], o="O1", d="H")
def c7(r):
    x, y = r.randint(-4, 4), r.randint(-4, 4); dx, dy = r.randint(1, 4), r.randint(1, 4)
    return S(f"Point A ({sg(x)}, {sg(y)}) moves to B ({sg(x + dx)}, {sg(y - dy)}). Describe the translation, e.g. 3 right 2 down.", [f"{dx} right {dy} down", f"{dx} right and {dy} down", f"{dx} right, {dy} down"], o="O1")
def c8(r):
    x, y = r.randint(1, 5), r.randint(1, 5)
    return S(f"Point P is at ({x}, {y}). Write the point with the same y-coordinate but on the other side of the y-axis, the same distance away.", PP(-x, y), o="O1")


s.std([c1, c5, c2, c3, c7, c8, c4, c6], EX("Explain how to plot the point (−4, 3).", [("start at the origin and go 4 left", "4 left|left 4|across"), ("then go 3 up", "3 up|up 3")], "Start at the origin (0, 0). The x-coordinate is −4, so go 4 left. The y-coordinate is 3, so go 3 up.", o="O1"))

s = U.section("17.2", "Reflections", ["O2"])
s.idea("Mirror lines", ["When a shape is **reflected**, each point ends up the **same distance** from the mirror line on the other side.",
       "Reflect in the **y-axis**: (x, y) → (−x, y). Reflect in the **x-axis**: (x, y) → (x, −y). Reflect in **y = x**: (x, y) → (y, x)."],
       fig=G(polys=[{"pts": [[1, 1], [4, 1], [1, 3]], "l": "A"}, {"pts": [[-1, 1], [-4, 1], [-1, 3]], "l": "B"}]))
s.check(S("(3, 5) is reflected in the y-axis. Write its new coordinates.", PP(-3, 5), o="O2"))
s.mistake("Same distance", ["A point 2 squares from the mirror line must end up 2 squares from it on the other side."])


def m1(r):
    x, y = r.randint(1, 5) * pick(r, [-1, 1]), r.randint(1, 5) * pick(r, [-1, 1])
    return S(f"Point A ({sg(x)}, {sg(y)}) is reflected in the y-axis. Write its image.", PP(-x, y), o="O2", fig=G([{"x": x, "y": y, "l": "A"}]))
def m2(r):
    x, y = r.randint(1, 5) * pick(r, [-1, 1]), r.randint(1, 5) * pick(r, [-1, 1])
    return S(f"Point A ({sg(x)}, {sg(y)}) is reflected in the x-axis. Write its image.", PP(x, -y), o="O2", fig=G([{"x": x, "y": y, "l": "A"}]))
def m3(r):
    x, y = r.randint(-5, 5), r.randint(-5, 5)
    if x == y: return None
    return S(f"({sg(x)}, {sg(y)}) is reflected in the line y = x. Write its image.", PP(y, x), o="O2", d="H")
def m4(r):
    k = r.randint(1, 4); x, y = r.randint(-5, 5), r.randint(-5, 5)
    if x == k: return None
    return S(f"({sg(x)}, {sg(y)}) is reflected in the line x = {k}. Write its image.", PP(2 * k - x, y), o="O2", d="H", fig=G([{"x": x, "y": y, "l": "A"}], lines=[{"x": k, "label": f"x = {k}"}]))
def m5(r):
    T = [[1, 1], [r.randint(3, 5), 1], [1, r.randint(2, 5)]]
    ax = pick(r, ["x", "y"]); im = [[-a, b] for a, b in T] if ax == "y" else [[a, -b] for a, b in T]
    return MC(f"Shape B is the reflection of shape A. What is the mirror line?", f"the {ax}-axis", ["the x-axis" if ax == "y" else "the y-axis", "the line y = x"], o="O2", fig=G(polys=[{"pts": T, "l": "A"}, {"pts": im, "l": "B"}]))
def m6(r):
    pts = [(r.randint(1, 5), r.randint(1, 5)) for _ in range(2)]
    return TB("Reflect each point in the y-axis.", ["Point", "Image x", "Image y"], [[f"({x}, {y})", B(-x), B(y)] for x, y in pts], o="O2")
def m7(r):
    d = r.randint(1, 5)
    return N(f"A point is {d} squares to the left of a vertical mirror line. How many squares to the right is its image?", d, "squares", units=["squares"], o="O2")
def m8(r):
    return MC("When a shape is reflected, which of these stays the same?", "its size and shape", ["its position", "the direction it faces", "its coordinates"], o="O2")


s.std([m1, m5, m2, m6, m7, m8, m3, m4], EX("Explain how to reflect the point (2, 4) in the x-axis.", [("it is 4 squares above the x-axis", "4 above|4 squares|distance"), ("the image is 4 below: (2, −4)", "\\(2, ?[−-]4\\)|−4|-4")], "(2, 4) is 4 squares above the x-axis. Its image is the same distance below, so it is at (2, −4).", o="O2"))

s = U.section("17.3", "Rotations", ["O3"])
s.idea("Turning a shape", ["A **rotation** turns a shape about a fixed point called the **centre of rotation**. Give the **angle** (90°, 180°) and the **direction** (clockwise or anticlockwise).",
       "Rotating 90° clockwise about the origin: (x, y) → (y, −x). A half turn (180°): (x, y) → (−x, −y)."],
       fig=G(polys=[{"pts": [[0, 0], [3, 0], [0, 2]], "l": "A"}, {"pts": [[0, 0], [0, -3], [2, 0]], "l": "B"}]))
s.check(MC("A shape is rotated 90° clockwise and then 90° clockwise again. What single rotation is this?", "180°", [("90° anticlockwise", ""), ("360°", "")], o="O3"))
s.mistake("Use tracing paper", ["Trace the shape, hold the centre with a pencil, and turn the paper."])


def t1(r):
    x, y = r.randint(1, 5) * pick(r, [-1, 1]), r.randint(1, 5) * pick(r, [-1, 1])
    return S(f"Point A ({sg(x)}, {sg(y)}) is rotated 180° about the origin. Write its image.", PP(-x, -y), o="O3", fig=G([{"x": x, "y": y, "l": "A"}]))
def t2(r):
    x, y = r.randint(1, 5), r.randint(1, 5)
    return S(f"Point A ({x}, {y}) is rotated 90° clockwise about the origin. Write its image.", PP(y, -x), o="O3", d="H", fig=G([{"x": x, "y": y, "l": "A"}]))
def t3(r):
    x, y = r.randint(1, 5), r.randint(1, 5)
    return S(f"({x}, {y}) is rotated 90° anticlockwise about the origin. Write its image.", PP(-y, x), o="O3", d="H")
def t4(r):
    d = pick(r, ["clockwise", "anticlockwise"]); n = pick(r, [1, 2, 3])
    tot = 90 * n
    return N(f"A shape is turned {n} quarter turn{'s' if n > 1 else ''} {d}. How many degrees is that?", tot, "°", units=["°"], o="O3")
def t5(r):
    a, b = r.randint(2, 4), r.randint(2, 4)
    T = [[0, 0], [a, 0], [0, b]]
    return MC("Shape B is a rotation of shape A about the origin. Describe it.", "90° clockwise", ["90° anticlockwise", "180°"], o="O3", fig=G(polys=[{"pts": T, "l": "A"}, {"pts": [[0, 0], [0, -a], [b, 0]], "l": "B"}]))
def t6(r):
    pts = [(r.randint(1, 5), r.randint(1, 5)) for _ in range(2)]
    return TB("Rotate each point 180° about the origin.", ["Point", "Image x", "Image y"], [[f"({x}, {y})", B(-x), B(-y)] for x, y in pts], o="O3")
def t7(r):
    return MC("A shape is rotated 270° clockwise. Which rotation gives the same result?", "90° anticlockwise", ["90° clockwise", "180°", "270° anticlockwise"], o="O3")
def t8(r):
    return MC("Which changes when a shape is rotated?", "the direction it faces", ["its size", "its angles", "the lengths of its sides"], o="O3")


s.std([t1, t5, t6, t4, t7, t8, t2, t3], EX("Explain why a rotation of 270° clockwise is the same as 90° anticlockwise.", [("a full turn is 360°", "360"), ("360 − 270 = 90, turning the other way", "90|other way|opposite")], "A full turn is 360°. Turning 270° clockwise leaves you 90° short of a full turn, which is where 90° anticlockwise ends up.", o="O3"))

U.mindmap(("Coordinates", "(x, y) • four quadrants • translations", "O1", "17.1"), ("Reflections", "Same distance from the mirror line", "O2", "17.2"), ("Rotations", "Centre • angle • direction", "O3", "17.3"))
