# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 14 Position and transformation (14.1 Maps and plans, 14.2 Distance between two points,
14.3 Translating, 14.4 Reflecting, 14.5 Rotating and 14.6 Enlarging shapes). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(14, "Position and Transformation", "Geometry and measure",
         "Scale on maps and plans, coordinates in all four quadrants, and translations, reflections, rotations and enlargements.",
         {"O1": {"code": "7Gp.01", "sec": "14.1", "codeNote": "", "t": "Use scales on maps and plans to find real distances."},
          "O2": {"code": "7Gp.02", "sec": "14.2", "codeNote": "", "t": "Use coordinates in all four quadrants and find the distance between points on a horizontal or vertical line."},
          "O3": {"code": "7Gp.03", "sec": "14.3", "codeNote": "", "t": "Translate shapes on a grid, describing the move in squares left/right and up/down."},
          "O4": {"code": "7Gp.04", "sec": "14.4", "codeNote": "", "t": "Reflect shapes in horizontal and vertical mirror lines."},
          "O5": {"code": "7Gp.05", "sec": "14.5", "codeNote": "", "t": "Rotate shapes through 90° and 180° about a vertex or the centre."},
          "O6": {"code": "7Gp.06", "sec": "14.6", "codeNote": "", "t": "Enlarge shapes by a positive whole-number scale factor."}})
pt = lambda p: f"({p[0]}, {p[1]})"
PACC = lambda p: [f"({p[0]}, {p[1]})", f"({p[0]},{p[1]})", f"{p[0]}, {p[1]}", f"{p[0]},{p[1]}"]


def tri(r, lo=1, hi=3):
    x, y = r.randint(lo, hi), r.randint(lo, hi)
    return [[x, y], [x + r.randint(1, 3), y], [x, y + r.randint(1, 3)]]


# ================================================================== 14.1
s = U.section("14.1", "Maps and plans", ["O1"])
s.idea("Scale", ["A **scale** tells you how a length on a map or plan compares with the real length. '1 cm represents 5 m' means every 1 cm on the plan is 5 m in real life.",
       "A scale can also be written as a ratio: 1 : 50 000 means 1 cm on the map is 50 000 cm (500 m) in real life."])
s.check(N("On a plan, 1 cm represents 2 m. A room is 6 cm long on the plan. How long is the real room?", 12, "m", units=["m"], o="O1"))
s.idea("Why a scale is a ratio", ["A scale of 1 : 50 000 means 1 cm on the map is 50 000 cm in real life. Every length is shrunk by the same factor, so shapes keep their angles.",
       "Change units at the end: 50 000 cm = 500 m = 0.5 km."])
s.check(MC("Before you read on: on a 1 : 100 plan, a wall is 4 cm long. How long is the real wall?", "4 m", [("4 cm", "Every 1 cm on the plan is 100 cm in real life."), ("400 m", "4 × 100 = 400 cm, which is 4 m.")], o="O1"))
s.mistake("Use the same units", ["1 : 100 means 1 cm represents 100 cm = 1 m."])


def m1(r):
    k, l = r.randint(2, 10), r.randint(2, 15)
    return N(f"On a map, 1 cm represents {k} km. Two towns are {l} cm apart on the map. How far apart are they really?", k * l, "km", units=["km"], o="O1")
def m2(r):
    k, l = r.randint(2, 10), r.randint(2, 15)
    return N(f"On a plan, 1 cm represents {k} m. A real wall is {k * l} m long. How long is it on the plan?", l, "cm", units=["cm"], o="O1", d="H")
def m3(r):
    l = r.randint(3, 12) / 2; k = pick(r, [2, 4, 5, 10])
    return N(f"On a map, 1 cm represents {k} km. A road is {fmt(l)} cm long on the map. How long is the real road?", l * k, "km", units=["km"], o="O1")
def m4(r):
    k = pick(r, [100, 200, 500]); l = r.randint(2, 12)
    return N(f"A plan has scale 1 : {k}. A garden is {l} cm long on the plan. How long is it in metres?", l * k / 100, "m", units=["m"], o="O1", d="H")
def m5(r):
    k = r.randint(2, 5); a, b = r.randint(2, 8), r.randint(2, 8)
    return TB(f"On a plan of a classroom, 1 cm represents {k} m. Complete the table.", ["Length on plan (cm)", "Real length (m)"], [[str(a), B(a * k)], [str(b), B(b * k)]], o="O1", fig={"kind": "shape", "pts": [[0, 0], [a, 0], [a, b], [0, b]], "s": [f"{a} cm", f"{b} cm", "", ""]})
def m6(r):
    k = r.randint(2, 5); a, b = r.randint(2, 8), r.randint(2, 8)
    return N(f"The plan shows a rectangular field. 1 cm represents {k} m. What is the real perimeter of the field?", 2 * (a + b) * k, "m", units=["m"], o="O1", d="H", fig={"kind": "shape", "pts": [[0, 0], [a, 0], [a, b], [0, b]], "s": [f"{a} cm", f"{b} cm", "", ""]})
def m7(r):
    return MC("A scale of 1 : 1000 means…", "1 cm on the plan is 1000 cm in real life", ["1 cm on the plan is 1000 m", "1 m on the plan is 1000 cm", "the plan is 1000 times bigger"], o="O1")


def mp1(r):   # real to map
    s_ = pick(r, [1000, 5000, 25000]); km = pick(r, [1, 2, 5]) if s_ >= 5000 else None
    m = pick(r, [50, 100, 200]) if s_ == 1000 else km * 1000
    return N(f"A map has scale 1 : {s_:,}. A real distance is {m:,} m. How long is it on the map, in cm?", m * 100 / s_, "cm", units=["cm"], o="O1", d="H",
             reason=f"{m:,} m = {m * 100:,} cm; ÷ {s_:,} = {m * 100 / s_:g} cm.")
def mp2(r):   # spot the error
    return MC("On a 1 : 50 000 map, Ali measures 3 cm and says the real distance is 150 000 km. What is it really?", "1.5 km", [("150 000 km", "150 000 is in cm, not km."), ("15 km", "150 000 cm = 1500 m = 1.5 km.")], o="O1", d="H",
              reason="3 × 50 000 = 150 000 cm = 1500 m = 1.5 km.")


s.std([m5, m6, m1, m2, m3, m4, m7], EX("Explain how to find the real distance for 7 cm on a map with scale 1 cm to 3 km.", [("each centimetre is 3 km", ["each cm|1 cm|3 km"]), ("7 × 3 = 21 km", ["21"])], "Each centimetre on the map represents 3 km, so 7 cm represents 7 × 3 = 21 km.", o="O1"),
      deep=[mp1, mp2])

# ================================================================== 14.2
s = U.section("14.2", "Distance between two points", ["O2"])
s.idea("Four quadrants", ["Coordinates are written (x, y): **across first, then up or down**. Negative x is to the left of the y-axis; negative y is below the x-axis.",
       "On a horizontal line, the distance between (−3, 2) and (4, 2) is 4 − (−3) = 7 units."], fig={"kind": "coord", "x": [-5, 5], "y": [-5, 5], "points": [{"x": -3, "y": 2, "l": "A"}, {"x": 4, "y": 2, "l": "B"}], "segs": [[-3, 2, 4, 2]]})
s.check(N("Find the distance between (1, −2) and (1, 5).", 7, "units", units=["units"], o="O2"))
s.idea("Distance along a grid line", ["If two points have the same x-coordinate, they are on a vertical line: the distance is the difference in their y-coordinates. (2, −3) to (2, 5) is 5 − (−3) = 8 units.",
       "Subtracting a negative coordinate adds: count the units on both sides of the axis."])
s.check(MC("Before you read on: how far apart are (−4, 1) and (3, 1)?", "7 units", [("1 unit", "Subtract the x-coordinates: 3 − (−4)."), ("−1 units", "A distance is never negative.")], o="O2"))
s.mistake("Across first", ["(3, −1) means 3 across and 1 down, not 3 down."])


def d1(r):
    p = [nz(r, -5, 5), nz(r, -5, 5)]
    return S("Write the coordinates of point P.", PACC(p), o="O2", fig={"kind": "coord", "x": [-6, 6], "y": [-6, 6], "points": [{"x": p[0], "y": p[1], "l": "P"}]})
def d2(r):
    a, b = sorted(r.sample(range(-6, 7), 2)); y = nz(r, -5, 5)
    return N(f"Find the distance between ({a}, {y}) and ({b}, {y}).", b - a, "units", units=["units"], o="O2")
def d3(r):
    a, b = sorted(r.sample(range(-6, 7), 2)); x = nz(r, -5, 5)
    return N(f"Find the distance between ({x}, {a}) and ({x}, {b}).", b - a, "units", units=["units"], o="O2", fig={"kind": "coord", "x": [-7, 7], "y": [-7, 7], "segs": [[x, a, x, b]], "points": [{"x": x, "y": a}, {"x": x, "y": b}]})
def d4(r):
    p = [nz(r, -5, 5), nz(r, -5, 5)]
    q = "first" if p[0] > 0 and p[1] > 0 else "second" if p[0] < 0 < p[1] else "third" if p[0] < 0 and p[1] < 0 else "fourth"
    return MC(f"In which quadrant is the point {pt(p)}?", q, [x for x in ["first", "second", "third", "fourth"] if x != q], o="O2")
def d5(r):
    x0, y0, w, h = r.randint(-4, 0), r.randint(-4, 0), r.randint(2, 5), r.randint(2, 5)
    return S(f"Three corners of a rectangle are ({x0}, {y0}), ({x0 + w}, {y0}) and ({x0 + w}, {y0 + h}). Find the fourth corner.", PACC((x0, y0 + h)), o="O2", d="H")
def d6(r):
    a, b = sorted(r.sample(range(-5, 6), 2)); c, d_ = sorted(r.sample(range(-5, 6), 2))
    return N(f"A rectangle has corners ({a}, {c}), ({b}, {c}), ({b}, {d_}) and ({a}, {d_}). Find its perimeter.", 2 * ((b - a) + (d_ - c)), "units", units=["units"], o="O2", d="H", fig={"kind": "coord", "x": [-6, 6], "y": [-6, 6], "polys": [{"pts": [[a, c], [b, c], [b, d_], [a, d_]]}]})
def d7(r):
    a = [r.randint(-5, 5), r.randint(-5, 5)]; v = [nz(r, -4, 4), 0]
    return S(f"Point B is {abs(v[0])} units to the {'right' if v[0] > 0 else 'left'} of A {pt(a)}. Write the coordinates of B.", PACC((a[0] + v[0], a[1])), o="O2")


def ds1(r):   # midpoint
    a, b = r.randint(-6, 2), r.randint(3, 9); y = r.randint(-4, 6)
    if (a + b) % 2: b += 1
    return MC(f"What is the midpoint of ({a}, {y}) and ({b}, {y})?", f"({(a + b) // 2}, {y})", [(f"({(b - a) // 2}, {y})", "That is half the distance, not the midpoint."), (f"({a + b}, {y})", "Divide the sum by 2.")], o="O2", d="H",
              reason=f"Halfway between {a} and {b} is ({a} + {b}) ÷ 2 = {(a + b) // 2}.")


s.std([d1, d3, d2, d4, d5, d6, d7], EX("Explain how to find the distance between (−2, 3) and (5, 3).", [("the points are on a horizontal line (same y)", ["horizontal|same y|y is the same"]), ("5 − (−2) = 7 units", ["\\b7\\b"])], "Both points have y = 3, so they are on a horizontal line. The distance is the difference in x: 5 − (−2) = 7 units.", o="O2"),
      deep=[ds1])

# ================================================================== 14.3
s = U.section("14.3", "Translating 2D shapes", ["O3"])
s.idea("Sliding", ["A **translation** slides a shape without turning or flipping it. Describe it by how many squares it moves **left or right** and **up or down**.",
       "Every vertex moves the same way, so the image is congruent to the original."])
s.check(S("Translate the point (2, 3) 4 right and 1 down. Write its new coordinates.", PACC((6, 2)), o="O3"))
s.idea("Why a translation keeps the shape", ["A translation slides every point by the same amount, for example 3 right and 2 down. Nothing turns or stretches, so the image is congruent to the object.",
       "Describe it with a vector: (3, −2) means 3 right and 2 down."])
s.check(MC("Before you read on: which translation takes (1, 4) to (−2, 6)?", "3 left and 2 up", [("3 right and 2 up", "x went from 1 to −2: that is left."), ("2 left and 3 up", "x changed by 3, y by 2.")], o="O3"))
s.mistake("Same move for every corner", ["Move EVERY vertex the same number of squares."])


def t1(r):
    p = [r.randint(-4, 4), r.randint(-4, 4)]; a, b = nz(r, -5, 5), nz(r, -5, 5)
    return S(f"Translate the point {pt(p)} {abs(a)} {'right' if a > 0 else 'left'} and {abs(b)} {'up' if b > 0 else 'down'}. Write the new coordinates.", PACC((p[0] + a, p[1] + b)), o="O3")
def t2(r):
    T = tri(r); a, b = r.randint(1, 4), r.randint(1, 3); I = [[x + a, y + b] for x, y in T]
    return MC("Shape A has been translated to shape B. Describe the translation.", f"{a} right and {b} up", [f"{b} right and {a} up", f"{a} left and {b} down", f"{a} right and {b} down"], o="O3", fig={"kind": "coord", "x": [0, 10], "y": [0, 9], "polys": [{"pts": T, "l": "A"}, {"pts": I, "l": "B"}]}) if a != b else None
def t3(r):
    T = tri(r); a, b = r.randint(1, 4), r.randint(1, 4)
    return TB(f"Triangle A is translated {a} right and {b} up. Write the new coordinates of its first vertex {pt(T[0])}.", ["Coordinate", "Value"], [["x", B(T[0][0] + a)], ["y", B(T[0][1] + b)]], o="O3", fig={"kind": "coord", "x": [0, 10], "y": [0, 9], "polys": [{"pts": T, "l": "A"}]})
def t4(r):
    return MC("Which is true about a translation?", "the shape stays the same size and the same way round", ["the shape gets bigger", "the shape is flipped over", "the shape is turned"], o="O3")
def t5(r):
    a, b = nz(r, -5, 5), nz(r, -5, 5)
    return S(f"A shape is moved {abs(a)} {'right' if a > 0 else 'left'} and {abs(b)} {'up' if b > 0 else 'down'}. Describe the translation that moves it back.", [f"{abs(a)} {'left' if a > 0 else 'right'} and {abs(b)} {'down' if b > 0 else 'up'}", f"{abs(a)} {'left' if a > 0 else 'right'}, {abs(b)} {'down' if b > 0 else 'up'}"], o="O3", d="H")
def t6(r):
    p = [r.randint(-4, 4), r.randint(-4, 4)]; q = [p[0] + nz(r, -4, 4), p[1] + nz(r, -4, 4)]
    return N(f"Point P {pt(p)} is translated to {pt(q)}. How many squares did it move horizontally? (Write left as negative.)", q[0] - p[0], o="O3")


def t7(r):
    p = [r.randint(-4, 4), r.randint(-4, 4)]; b = nz(r, -4, 4)
    return N(f"Point {pt(p)} is translated {abs(b)} {'up' if b > 0 else 'down'}. What is its new y-coordinate?", p[1] + b, o="O3")


def tr1(r):   # reverse translation
    a, b = r.randint(-5, 5), r.randint(-5, 5)
    if a == 0 and b == 0: return None
    d = lambda v, p, n: (f"{abs(v)} {p}" if v > 0 else f"{abs(v)} {n}" if v < 0 else "")
    fw = ", ".join(x for x in [d(a, "right", "left"), d(b, "up", "down")] if x); bw = ", ".join(x for x in [d(-a, "right", "left"), d(-b, "up", "down")] if x)
    return MC(f"A shape is translated {fw}. Which translation moves it back?", bw, [(fw, "That moves it further away."), (", ".join(x for x in [d(b, "right", "left"), d(a, "up", "down")] if x) or "none", "Do not swap x and y.")], o="O3", d="H", reason="Reverse both parts of the move.") if fw != bw else None


s.std([t2, t3, t1, t4, t5, t6, t7], EX("Explain why the image after a translation is congruent to the original shape.", [("every point moves the same distance in the same direction", ["same distance|same direction|same way|slide"]), ("so the size and shape do not change", ["size|shape|not change|doesn't change"])], "A translation slides every point the same distance in the same direction, so the shape is not stretched, turned or flipped: it stays exactly the same shape and size.", o="O3"),
      deep=[tr1])

# ================================================================== 14.4
s = U.section("14.4", "Reflecting shapes", ["O4"])
s.idea("Mirror lines", ["In a **reflection**, each point of the image is the same distance from the mirror line as the original, but on the other side.",
       "Reflecting in the y-axis: (3, 2) → (−3, 2). Reflecting in the x-axis: (3, 2) → (3, −2)."], fig={"kind": "coord", "x": [-5, 5], "y": [-5, 5], "polys": [{"pts": [[1, 1], [3, 1], [1, 3]], "l": "A"}, {"pts": [[-1, 1], [-3, 1], [-1, 3]], "l": "B"}]})
s.check(S("Reflect (4, −1) in the x-axis.", PACC((4, 1)), o="O4"))
s.idea("Why a reflection flips the shape", ["Every point and its image are the same distance from the mirror line, on opposite sides, along a line at right angles to the mirror.",
       "So the image is congruent but reversed: a clockwise label order becomes anticlockwise."])
s.check(MC("Before you read on: reflect (3, 2) in the x-axis. Where does it go?", "(3, −2)", [("(−3, 2)", "That is a reflection in the y-axis."), ("(2, 3)", "That swaps the coordinates.")], o="O4"))
s.mistake("Same distance", ["Count squares to the mirror line, then the same number on the other side."])


def f1(r):
    p = [nz(r, -5, 5), nz(r, -5, 5)]; m = pick(r, [("the x-axis", (p[0], -p[1])), ("the y-axis", (-p[0], p[1]))])
    return S(f"Reflect the point {pt(p)} in {m[0]}.", PACC(m[1]), o="O4")
def f2(r):
    k = r.randint(1, 4); p = [r.randint(-3, 6), r.randint(-4, 4)]
    if p[0] == k: return None
    return S(f"Reflect {pt(p)} in the line x = {k}.", PACC((2 * k - p[0], p[1])), o="O4", d="H", fig={"kind": "coord", "x": [-6, 10], "y": [-6, 6], "lines": [{"x": k, "label": f"x = {k}"}], "points": [{"x": p[0], "y": p[1], "l": "P"}]})
def f3(r):
    T = tri(r); I = [[-x, y] for x, y in T]
    return MC("Shape A is reflected onto shape B. What is the mirror line?", "the y-axis", ["the x-axis", "y = x", "x = 2"], o="O4", fig={"kind": "coord", "x": [-7, 7], "y": [0, 7], "polys": [{"pts": T, "l": "A"}, {"pts": I, "l": "B"}]})
def f4(r):
    T = tri(r); I = [[x, -y] for x, y in T]
    return TB("Triangle A is reflected in the x-axis. Write the image of its first vertex.", ["Coordinate", "Value"], [["x", B(I[0][0])], ["y", B(I[0][1])]], o="O4", fig={"kind": "coord", "x": [0, 7], "y": [-7, 7], "polys": [{"pts": T, "l": "A"}]}, data={"head": ["Vertex", "1st"], "rows": [["A", pt(T[0])]]})
def f5(r):
    k = r.randint(1, 4); p = [r.randint(-4, 4), r.randint(-3, 7)]
    if p[1] == k: return None
    return N(f"{pt(p)} is reflected in the line y = {k}. What is the y-coordinate of the image?", 2 * k - p[1], o="O4", d="H")
def f6(r):
    p = [nz(r, -5, 5), nz(r, -5, 5)]
    return MC(f"Which point is the reflection of {pt(p)} in the y-axis?", pt((-p[0], p[1])), [pt((p[0], -p[1])), pt((-p[0], -p[1])), pt((p[1], p[0]))], o="O4") if p[0] != p[1] and p[0] != -p[1] else None


def f7(r):
    k = r.randint(1, 4); x = r.randint(k + 1, k + 5)
    return N(f"A point is {x - k} squares to the right of the mirror line x = {k}. How many squares to the left of the line is its image?", x - k, "squares", units=["squares"], o="O4")


def rf1(r):   # which mirror line
    x, y = r.randint(1, 6), r.randint(1, 6)
    if x == y: return None
    return MC(f"({x}, {y}) is reflected to ({-x}, {y}). Which line is the mirror?", "the y-axis (x = 0)", [("the x-axis (y = 0)", f"That would give ({x}, {-y})."), ("y = x", f"That would give ({y}, {x}).")], o="O4", d="H", reason="Only the x-coordinate changed sign, so the mirror is the y-axis.")


s.std([f3, f4, f1, f2, f5, f6, f7], EX("Explain how to reflect a point in the y-axis.", [("the point moves to the same distance on the other side of the y-axis", ["same distance|other side"]), ("the x-coordinate changes sign; y stays the same", ["sign|negative|x changes|y stays"])], "The image is the same distance from the y-axis but on the other side, so the x-coordinate changes sign and the y-coordinate stays the same: (x, y) → (−x, y).", o="O4"),
      deep=[rf1])

# ================================================================== 14.5
s = U.section("14.5", "Rotating shapes", ["O5"])
s.idea("Turning", ["A **rotation** turns a shape about a fixed point (the **centre of rotation**). Give the **angle** (90° or 180°) and the **direction** (clockwise or anticlockwise).",
       "A rotation of 180° about the origin: (x, y) → (−x, −y)."])
s.check(S("Rotate (3, 2) through 180° about the origin.", PACC((-3, -2)), o="O5"))
s.idea("What you need to describe a rotation", ["A rotation needs three facts: the centre, the angle and the direction (clockwise or anticlockwise).",
       "A half turn (180°) is the same clockwise or anticlockwise. A quarter turn clockwise is the same as three quarters anticlockwise."])
s.check(MC("Before you read on: is a 90° clockwise turn the same as 270° anticlockwise?", "Yes", [("No", "Both end facing the same way: 90 + 270 = 360."), ("Only about the origin", "It is true about any centre.")], o="O5"))
s.mistake("Clockwise is like a clock", ["Clockwise means the way the hands of a clock turn."])


def r1(r):
    p = [nz(r, -5, 5), nz(r, -5, 5)]
    return S(f"Rotate {pt(p)} through 180° about the origin.", PACC((-p[0], -p[1])), o="O5")
def r2(r):
    p = [nz(r, -5, 5), nz(r, -5, 5)]; cw = r.random() < 0.5
    q = (p[1], -p[0]) if cw else (-p[1], p[0])
    return S(f"Rotate {pt(p)} through 90° {'clockwise' if cw else 'anticlockwise'} about the origin.", PACC(q), o="O5", d="H")
def r3(r):
    T = tri(r); I = [[-x, -y] for x, y in T]
    return MC("Shape A is rotated onto shape B about the origin. What is the angle?", "180°", ["90° clockwise", "90° anticlockwise", "45°"], o="O5", fig={"kind": "coord", "x": [-7, 7], "y": [-7, 7], "polys": [{"pts": T, "l": "A"}, {"pts": I, "l": "B"}]})
def r4(r):
    a = pick(r, [90, 180, 270])
    return N(f"A rotation of {a}° clockwise is the same as how many degrees anticlockwise?", 360 - a, "°", units=["°"], o="O5")
def r5(r):
    rows = [("Quarter turn", "90°"), ("Half turn", "180°"), ("Three-quarter turn", "270°"), ("Full turn", "360°")]
    return GD("How many degrees is each turn?", "Angle", rows, o="O5")
def r6(r):
    T = tri(r); I = [[-x, -y] for x, y in T]
    return TB("Triangle A is rotated 180° about the origin. Write the image of its first vertex.", ["Coordinate", "Value"], [["x", B(I[0][0])], ["y", B(I[0][1])]], o="O5", fig={"kind": "coord", "x": [-7, 7], "y": [-7, 7], "polys": [{"pts": T, "l": "A"}]}, data={"head": ["Vertex", "1st"], "rows": [["A", pt(T[0])]]})
def r7(r):
    return MC("To describe a rotation you must give…", "the centre, the angle and the direction", ["only the angle", "the mirror line", "how many squares it moves"], o="O5")


def ro1(r):   # equivalent turns
    rows = r.sample([("90° clockwise", "270° anticlockwise"), ("180° clockwise", "180° anticlockwise"), ("270° clockwise", "90° anticlockwise"), ("90° anticlockwise", "270° clockwise")], 3)
    return GD("Which turn ends in the same position?", "Same as", rows, o="O5", d="H", extra=["360° clockwise"], reason="Two turns in opposite directions that add to 360° end in the same place.")


s.std([r5, r6, r1, r2, r3, r4, r7], EX("Explain why a rotation of 180° clockwise is the same as 180° anticlockwise.", [("180° is a half turn", ["half turn|half"]), ("turning half way either way ends in the same place", ["same place|either way|both ways|same position"])], "180° is a half turn. Turning half way round clockwise or anticlockwise ends in exactly the same position.", o="O5"),
      deep=[ro1])

# ================================================================== 14.6
s = U.section("14.6", "Enlarging shapes", ["O6"])
s.idea("Scale factor", ["An **enlargement** makes a shape bigger (or smaller). Every length is multiplied by the **scale factor**. The angles stay the same.",
       "A 2 cm by 3 cm rectangle enlarged by scale factor 2 becomes 4 cm by 6 cm."], fig={"kind": "coord", "x": [0, 10], "y": [0, 7], "polys": [{"pts": [[1, 1], [3, 1], [3, 2], [1, 2]], "l": "A"}, {"pts": [[4, 1], [8, 1], [8, 3], [4, 3]], "l": "B"}]})
s.check(N("A line 5 cm long is enlarged by scale factor 3. How long is it now?", 15, "cm", units=["cm"], o="O6"))
s.idea("Why every length is multiplied", ["An enlargement with scale factor 3 makes every length 3 times as long, so the shape keeps its angles but grows.",
       "Angles do NOT change: a right angle stays a right angle."])
s.check(MC("Before you read on: a triangle with a 40° angle is enlarged by scale factor 2. What happens to the 40° angle?", "It stays 40°", [("It becomes 80°", "Enlargement changes lengths, not angles."), ("It becomes 20°", "Angles do not change.")], o="O6"))
s.mistake("Multiply, do not add", ["Scale factor 2 doubles lengths: 3 cm → 6 cm, not 5 cm."])


def e1(r):
    a, k = r.randint(2, 12), r.randint(2, 5)
    return N(f"A side of {a} cm is enlarged by scale factor {k}. How long is it now?", a * k, "cm", units=["cm"], o="O6")
def e2(r):
    a, k = r.randint(2, 9), r.randint(2, 5)
    return N(f"A shape is enlarged. A side of {a} cm becomes {a * k} cm. What is the scale factor?", k, o="O6")
def e3(r):
    a, b, k = r.randint(2, 6), r.randint(2, 6), r.randint(2, 4)
    return TB(f"A rectangle {a} cm by {b} cm is enlarged by scale factor {k}. Complete the table.", ["", "New length (cm)"], [["Width", B(a * k)], ["Height", B(b * k)]], o="O6", fig={"kind": "shape", "pts": [[0, 0], [a, 0], [a, b], [0, b]], "s": [f"{a} cm", f"{b} cm", "", ""]})
def e4(r):
    a, k = r.randint(30, 120), r.randint(2, 4)
    return N(f"A triangle with an angle of {a}° is enlarged by scale factor {k}. What is the size of that angle in the image?", a, "°", units=["°"], o="O6")
def e5(r):
    T = [[1, 1], [2, 1], [1, 3]]; k = r.randint(2, 3); I = [[x * k, y * k] for x, y in T]
    return N("Shape A is enlarged to make shape B. What is the scale factor?", k, o="O6", fig={"kind": "coord", "x": [0, 10], "y": [0, 10], "polys": [{"pts": T, "l": "A"}, {"pts": I, "l": "B"}]})
def e6(r):
    a, b, k = r.randint(2, 6), r.randint(2, 6), r.randint(2, 4)
    return N(f"A rectangle {a} cm by {b} cm is enlarged by scale factor {k}. What is the perimeter of the image?", 2 * (a + b) * k, "cm", units=["cm"], o="O6", d="H")


def e7(r):
    a, b, k = r.randint(2, 5), r.randint(2, 5), r.randint(2, 3)
    if a == b: return None
    return MC(f"A {a} cm by {b} cm rectangle is enlarged by scale factor {k}. Which is the image?", f"{a * k} cm by {b * k} cm", [f"{a + k} cm by {b + k} cm", f"{a * k} cm by {b} cm", f"{a} cm by {b * k} cm"], o="O6")


def en1(r):   # find scale factor
    a = r.randint(2, 6); k = r.randint(2, 4)
    return N(f"A side of {a} cm becomes {a * k} cm after an enlargement. Another side was 5 cm. How long is it now?", 5 * k, "cm", units=["cm"], o="O6", d="H", reason=f"The scale factor is {a * k} ÷ {a} = {k}; 5 × {k} = {5 * k} cm.")
def en2(r):   # always/sometimes/never
    rows = r.sample([("An enlargement changes the angles", "Never true"), ("An enlarged shape is congruent to the original", "Never true"), ("An enlargement with scale factor 2 doubles the perimeter", "Always true")], 3)
    return GD("Is each statement always true, sometimes true or never true? (scale factor bigger than 1)", "Always / sometimes / never", rows, o="O6", d="H", extra=["Always true", "Sometimes true", "Never true"],
              reason="Every length doubles, so the perimeter doubles; the angles stay the same; the size changes, so the shapes are not congruent.")


s.std([e3, e5, e1, e2, e4, e6, e7], EX("Explain what happens to the angles of a shape when it is enlarged.", [("the angles stay the same", ["same|do not change|don't change|unchanged"]), ("only the lengths are multiplied by the scale factor", ["lengths|sides|scale factor"])], "The angles stay exactly the same. Only the lengths change: each one is multiplied by the scale factor, so the shape keeps its shape but changes size.", o="O6"),
      deep=[en1, en2])

U.mindmap(("Maps and plans", "Scale • 1 : 100 means 1 cm to 1 m", "O1", "14.1"), ("Coordinates", "Four quadrants • distance along a line", "O2", "14.2"),
          ("Translation", "Squares left/right and up/down", "O3", "14.3"), ("Reflection", "Same distance, other side of the mirror", "O4", "14.4"),
          ("Rotation", "Centre, angle, direction", "O5", "14.5"), ("Enlargement", "Lengths × scale factor • angles stay the same", "O6", "14.6"))
