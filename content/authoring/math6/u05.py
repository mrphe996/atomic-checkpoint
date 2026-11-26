# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 5 2D shapes (5.1 Quadrilaterals, 5.2 Circles, 5.3 Rotational symmetry).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(5, "2D Shapes", "Geometry and measure",
         "Properties of quadrilaterals, the parts of a circle, and rotational symmetry.",
         {"O1": {"code": "6Gg.01", "sec": "5.1", "codeNote": "", "t": "Identify, describe, classify and sketch quadrilaterals, including trapezia and kites, using their properties."},
          "O2": {"code": "6Gg.02", "sec": "5.2", "codeNote": "", "t": "Know the parts of a circle: centre, radius, diameter and circumference."},
          "O3": {"code": "6Gg.03", "sec": "5.3", "codeNote": "", "t": "Identify rotational symmetry in familiar shapes and find the order of rotational symmetry."}})
Q4 = {"square": [[0, 0], [4, 0], [4, 4], [0, 4]], "rectangle": [[0, 0], [7, 0], [7, 4], [0, 4]], "parallelogram": [[0, 0], [6, 0], [8, 4], [2, 4]],
      "rhombus": [[0, 0], [4, 0], [6.4, 3.2], [2.4, 3.2]], "trapezium": [[0, 0], [8, 0], [6, 4], [2, 4]], "kite": [[3, 0], [6, 3], [3, 8], [0, 3]]}
PROPS = {"square": (4, 2, 4, "4"), "rectangle": (0, 2, 4, "2"), "parallelogram": (0, 2, 0, "2"), "rhombus": (4, 2, 0, "2"), "trapezium": (0, 1, 0, "1"), "kite": (0, 0, 0, "1")}

s = U.section("5.1", "Quadrilaterals", ["O1"])
s.idea("Families of quadrilaterals", ["A **quadrilateral** has 4 straight sides. Look at **sides** (equal? parallel?), **angles** (right angles?) and **diagonals**.",
       "A **trapezium** has one pair of parallel sides. A **kite** has two pairs of equal sides next to each other. A **parallelogram** has two pairs of parallel sides; a **rhombus** is a parallelogram with 4 equal sides."], fig={"kind": "shape", "pts": Q4["trapezium"]})
s.check(MC("Which quadrilateral has exactly one pair of parallel sides?", "trapezium", [("kite", ""), ("rectangle", ""), ("rhombus", "")], o="O1"))
s.check(MC("Before you read on: is a square a rectangle?", "Yes", [("No", "A square has 4 right angles and opposite sides equal, so it fits the rectangle rules."), ("Only if it is big", "Size does not matter.")], o="O1"))
s.mistake("A square is a rectangle", ["A square has four right angles, so it is a special rectangle (and a special rhombus too)."])


def g1(r):
    n = pick(r, list(Q4))
    return S("Name this quadrilateral.", [n, n + "s", "a " + n], o="O1", fig={"kind": "shape", "pts": Q4[n]})
def g2(r):
    ns = r.sample(list(Q4), 4)
    return GD("How many pairs of parallel sides does each shape have?", "Pairs", [(n, str(PROPS[n][1])) for n in ns], o="O1", extra=["0", "1", "2"])
def g3(r):
    ns = r.sample(list(Q4), 4)
    return GD("Does each shape always have 4 right angles?", "4 right angles?", [(n, "Yes" if PROPS[n][2] else "No") for n in ns], o="O1", extra=["Yes", "No"])
def g4(r):
    n = pick(r, ["kite", "trapezium", "parallelogram", "rhombus"])
    d = {"kite": "two pairs of equal sides next to each other", "trapezium": "exactly one pair of parallel sides", "parallelogram": "two pairs of parallel sides and no right angles", "rhombus": "four equal sides and no right angles"}[n]
    return MC(f"Which shape has {d}?", n, [x for x in ["kite", "trapezium", "parallelogram", "rhombus", "rectangle"] if x != n][:3], o="O1")
def g5(r):
    p = pick(r, ["square", "rhombus"])
    s_ = r.randint(3, 15)
    return N(f"A {p} has a side of {s_} cm. What is its perimeter?", 4 * s_, "cm", units=["cm"], o="O1")
def g6(r):
    a = r.randint(50, 80)
    return N("In a parallelogram one angle is " + f"{a}°. What is the angle next to it?", 180 - a, "°", units=["°"], o="O1", d="H", fig={"kind": "shape", "pts": Q4["parallelogram"], "ang": [f"{a}°", "x", "", ""]})
def g7(r):
    return MS("Select ALL the shapes that have two pairs of parallel sides.", ["square", "rectangle", "rhombus", "parallelogram"][:r.randint(2, 4)], ["kite", "trapezium"], o="O1")
def g8(r):
    l, w = r.randint(5, 14), r.randint(2, 9)
    if l == w: return None
    return N(f"A rectangle is {l} cm long and {w} cm wide. What is its perimeter?", 2 * (l + w), "cm", units=["cm"], o="O1", fig={"kind": "shape", "pts": [[0, 0], [l, 0], [l, w], [0, w]], "s": [f"{l} cm", f"{w} cm", "", ""]})

def g9(r):
    a, b = r.randint(60, 120), r.randint(40, 90)
    c = 360 - a - 2 * b
    if c < 30: return None
    return N(f"A kite has two equal angles of {b}° each and another angle of {a}°. Find the fourth angle.", c, "°", units=["°"], o="O1", d="H", reason="The angles of a quadrilateral add up to 360°.")
def g10(r):
    p_, s_ = pick(r, ["square", "rhombus"]), r.randint(4, 20)
    return N(f"Lina bends a {4 * s_} cm wire into a {p_}. How long is each side?", s_, "cm", units=["cm"], o="O1", d="H")


def e1_1(r):
    rows = r.sample([("A square is a rhombus", "Always true"), ("A rectangle is a square", "Sometimes true"), ("A trapezium has two pairs of parallel sides", "Sometimes true"), ("A kite has four equal sides", "Sometimes true"), ("A parallelogram has a right angle", "Sometimes true"), ("A rhombus has four equal sides", "Always true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O1", d="H", extra=["Always true", "Sometimes true", "Never true"], reason="Check the properties of each shape; a special case (square, rhombus) can make a 'sometimes' statement true.")


s.std([g1, g2, g3, g4, g5, g7, g8, g6, g9, g10], EX("Explain why a square is also a rhombus.", [("a rhombus has four equal sides", "four equal|4 equal|equal sides"), ("a square also has four equal sides", "square.*equal|also")], "A rhombus is a quadrilateral with four equal sides. A square also has four equal sides, so a square is a special rhombus (with right angles).", o="O1"),
      deep=[e1_1])

s = U.section("5.2", "Circles", ["O2"])
s.idea("Parts of a circle", ["The **centre** is the middle point. The **radius** goes from the centre to the edge. The **diameter** goes all the way across through the centre.",
       "**diameter = 2 × radius**. The distance all the way round is the **circumference**."], fig={"kind": "circle", "r": "radius"})
s.check(N("A circle has radius 6 cm. What is its diameter?", 12, "cm", units=["cm"], o="O2"))
s.check(MC("Before you read on: a circle has radius 6 cm. What is its diameter?", "12 cm", [("3 cm", "The diameter is twice the radius."), ("6 cm", "That is the radius.")], o="O2"))
s.mistake("Radius or diameter", ["The radius is half the diameter. Do not mix them up."])


def c1(r):
    v = r.randint(2, 25)
    return N(f"A circle has radius {v} cm. What is its diameter?", 2 * v, "cm", units=["cm"], o="O2", fig={"kind": "circle", "r": f"{v} cm"})
def c2(r):
    v = r.randint(2, 30) * 2
    return N(f"A circle has diameter {v} cm. What is its radius?", v // 2, "cm", units=["cm"], o="O2", fig={"kind": "circle", "d": f"{v} cm"})
def c3(r):
    return MT("Match each word to its meaning.", [("centre", "the middle point"), ("radius", "centre to the edge"), ("diameter", "across through the centre"), ("circumference", "distance all the way round")], o="O2")
def c4(r):
    rs = r.sample(range(2, 20), 3)
    return TB("Complete the table.", ["Radius (cm)", "Diameter (cm)"], [[str(v), B(2 * v)] for v in rs], o="O2")
def c5(r):
    n, d = r.randint(2, 5), r.randint(2, 10)
    return N(f"{n} circles, each of diameter {d} cm, are placed in a row touching. How long is the row?", n * d, "cm", units=["cm"], o="O2", d="H")
def c6(r):
    rad = r.randint(3, 12)
    return N(f"A square fits exactly around a circle of radius {rad} cm. What is the side length of the square?", 2 * rad, "cm", units=["cm"], o="O2", d="H")
def c7(r):
    w = pick(r, ["radius", "diameter"])
    return MC(f"Which line is a {w}?", "from the centre to the edge" if w == "radius" else "from edge to edge through the centre", ["from edge to edge not through the centre", "all the way round" , "from the centre to the edge" if w != "radius" else "from edge to edge through the centre"], o="O2")
def c8(r):
    rad = r.randint(2, 9)
    return N(f"A circle has radius {rad} cm. How far is it from one side of the circle to the other through the centre, in millimetres?", 20 * rad, "mm", units=["mm"], o="O2", d="H")

def c9(r):
    rad = r.randint(2, 8); n = r.randint(2, 4)
    return N(f"Pipes of radius {rad} cm are stacked {n} high in a straight column. How tall is the stack?", 2 * rad * n, "cm", units=["cm"], o="O2", d="H")
def c10(r):
    L, rad = r.randint(30, 80), r.randint(2, 5)
    if L % (2 * rad): return None
    return N(f"How many coins of radius {rad} cm fit side by side along a {L} cm ruler?", L // (2 * rad), "coins", units=["coins"], o="O2", d="H")


s.std([c1, c4, c2, c3, c5, c7, c6, c8, c9, c10], EX("Explain how to find the radius of a circle with diameter 18 cm.", [("the radius is half the diameter", "half|÷ ?2|divide by 2"), ("18 ÷ 2 = 9 cm", "\\b9\\b")], "The radius is half the diameter, so the radius is 18 ÷ 2 = 9 cm.", o="O2"))

s = U.section("5.3", "Rotational symmetry", ["O3"])
s.idea("Turning symmetry", ["A shape has **rotational symmetry** if it looks exactly the same after a turn of less than a full turn.",
       "The **order** of rotational symmetry is how many times it fits onto itself in one full turn. A square has order 4; a rectangle has order 2."], fig={"kind": "shape", "pts": Q4["square"]})
s.check(N("What is the order of rotational symmetry of an equilateral triangle?", 3, o="O3"))
s.check(MC("Before you read on: what is the order of rotational symmetry of a square?", "4", [("2", "It fits onto itself after each quarter turn."), ("1", "It looks the same more than once in a full turn.")], o="O3"))
s.mistake("Order 1", ["A shape that only fits onto itself after a full turn has order 1 (no rotational symmetry)."])
POLY = {"square": 4, "rectangle": 2, "parallelogram": 2, "rhombus": 2, "kite": 1, "trapezium": 1, "equilateral triangle": 3, "regular hexagon": 6, "regular pentagon": 5, "regular octagon": 8}
TRIPTS = [[0, 0], [6, 0], [3, 5.2]]


def o1(r):
    n = pick(r, list(Q4))
    return N("What is the order of rotational symmetry of this shape?", int(PROPS[n][3]), o="O3", fig={"kind": "shape", "pts": Q4[n]})
def o2(r):
    ns = r.sample(list(POLY), 4)
    return GD("Find the order of rotational symmetry.", "Order", [(n, str(POLY[n])) for n in ns], o="O3", extra=["1", "2", "3", "4"])
def o3(r):
    n = pick(r, ["regular pentagon", "regular hexagon", "regular octagon"])
    return N(f"What is the order of rotational symmetry of a {n}?", POLY[n], o="O3")
def o4(r):
    return MS("Select ALL the shapes that have rotational symmetry of order 2 or more.", r.sample(["square", "rectangle", "rhombus", "parallelogram", "regular hexagon"], 3), ["kite", "trapezium"], o="O3")
def o5(r):
    n = pick(r, [2, 3, 4, 6, 8])
    return N(f"A shape has rotational symmetry of order {n}. What is the smallest turn, in degrees, that makes it fit onto itself?", 360 // n, "°", units=["°"], o="O3", d="H")
def o6(r):
    w = pick(r, ["H", "S", "N", "Z", "A", "T", "X"])
    o = {"H": 2, "S": 2, "N": 2, "Z": 2, "A": 1, "T": 1, "X": 2}[w]
    return N(f"What is the order of rotational symmetry of the capital letter {w}?", o, o="O3")
def o7(r):
    return N("What is the order of rotational symmetry of this triangle?", 3, o="O3", fig={"kind": "shape", "pts": TRIPTS})
def o8(r):
    n = pick(r, [3, 4, 5, 6, 8])
    return MC(f"A regular polygon has rotational symmetry of order {n}. How many sides does it have?", str(n), [str(n + 1), str(2 * n), str(n - 1)], o="O3", d="H")

def o9(r):
    k = r.randint(1, 3); n = pick(r, [4, 6, 8])
    return N(f"A regular shape with order of rotational symmetry {n} is turned {k} × {360 // n}°. Does it look the same? Give the total turn in degrees.", k * 360 // n, "°", units=["°"], o="O3", d="H")
def o10(r):
    n = pick(r, [3, 4, 5, 6])
    return N(f"A windmill has {n} identical sails. What is the order of its rotational symmetry?", n, o="O3", d="H")


s.std([o1, o2, o7, o3, o4, o6, o5, o8, o9, o10], EX("Explain why a rectangle has rotational symmetry of order 2.", [("it looks the same after a half turn", "half|180"), ("it fits onto itself twice in a full turn", "twice|two times|2 times")], "A rectangle looks exactly the same after a half turn (180°) and again after a full turn. It fits onto itself twice, so the order is 2.", o="O3"))

U.mindmap(("Quadrilaterals", "Trapezium • kite • parallelogram • rhombus", "O1", "5.1"), ("Circles", "Radius • diameter = 2 × radius", "O2", "5.2"), ("Rotational symmetry", "Order = times it fits in a full turn", "O3", "5.3"))
