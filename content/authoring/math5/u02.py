# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 2 2D shapes (2.1 Triangles, 2.2 Symmetry). Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(2, "2D Shapes", "Geometry and measure",
         "Equilateral, isosceles and scalene triangles, and lines of symmetry and reflections in patterns.",
         {"O1": {"code": "5Gg.01", "sec": "2.1", "codeNote": "", "t": "Identify, describe, classify and sketch isosceles, equilateral and scalene triangles."},
          "O2": {"code": "5Gg.02", "sec": "2.2", "codeNote": "", "t": "Identify lines of symmetry in 2D shapes and patterns, and complete symmetrical patterns."}})
TRI = {"equilateral": [[0, 0], [6, 0], [3, 5.2]], "isosceles": [[0, 0], [5, 0], [2.5, 7]], "scalene": [[0, 0], [8, 0], [2, 4]], "right-angled": [[0, 0], [7, 0], [0, 4]]}
TICK = {"equilateral": [1, 1, 1], "isosceles": [0, 1, 1], "scalene": [1, 2, 3], "right-angled": []}
LOS = {"equilateral triangle": 3, "isosceles triangle": 1, "scalene triangle": 0, "square": 4, "rectangle": 2, "regular hexagon": 6, "regular pentagon": 5, "kite": 1, "circle": "infinitely many"}

s = U.section("2.1", "Triangles", ["O1"])
s.idea("Three kinds of triangle", ["An **equilateral** triangle has 3 equal sides and 3 equal angles. An **isosceles** triangle has 2 equal sides and 2 equal angles. A **scalene** triangle has no equal sides.",
       "Little marks called **hatch marks** show which sides are equal."], fig={"kind": "shape", "pts": TRI["isosceles"], "ticks": [0, 1, 1]})
s.check(MC("A triangle has sides 5 cm, 5 cm and 3 cm. What type is it?", "isosceles", [("equilateral", ""), ("scalene", "")], o="O1"))
s.mistake("Right-angled can be isosceles", ["A right-angled triangle can also be isosceles if its two shorter sides are equal."])


def t1(r):
    n = pick(r, ["equilateral", "isosceles", "scalene"])
    return S("What type of triangle is this? Look at the hatch marks.", [n, n + " triangle"], o="O1", fig={"kind": "shape", "pts": TRI[n], "ticks": TICK[n]})
def t2(r):
    a, b, c = r.randint(3, 9), r.randint(3, 9), r.randint(3, 9)
    if a + b <= c or a + c <= b or b + c <= a: return None
    k = "equilateral" if a == b == c else "isosceles" if len({a, b, c}) == 2 else "scalene"
    return MC(f"A triangle has sides {a} cm, {b} cm and {c} cm. What type is it?", k, [x for x in ["equilateral", "isosceles", "scalene"] if x != k], o="O1")
def t3(r):
    ts = []
    while len(ts) < 4:
        a, b, c = r.randint(3, 8), r.randint(3, 8), r.randint(3, 8)
        if a + b > c and a + c > b and b + c > a:
            k = "equilateral" if a == b == c else "isosceles" if len({a, b, c}) == 2 else "scalene"
            ts.append((f"{a} cm, {b} cm, {c} cm", k))
    return GD("Sort the triangles by their side lengths.", "Type", ts, o="O1", extra=["equilateral", "isosceles", "scalene"])
def t4(r):
    s_ = r.randint(3, 15)
    return N(f"An equilateral triangle has sides of {s_} cm. What is its perimeter?", 3 * s_, "cm", units=["cm"], o="O1", fig={"kind": "shape", "pts": TRI["equilateral"], "ticks": [1, 1, 1], "s": [f"{s_} cm", "", ""]})
def t5(r):
    a, b = r.randint(5, 12), r.randint(3, 8)
    if 2 * a <= b: return None
    return N(f"An isosceles triangle has two sides of {a} cm and one side of {b} cm. Find its perimeter.", 2 * a + b, "cm", units=["cm"], o="O1")
def t6(r):
    p = r.randint(4, 15) * 3
    return N(f"An equilateral triangle has a perimeter of {p} cm. How long is each side?", p // 3, "cm", units=["cm"], o="O1", d="H")
def t7(r):
    return MC("How many equal angles does an isosceles triangle have?", "2", ["3", "0", "1"], o="O1")
def t8(r):
    b, p = r.randint(3, 9), r.randint(20, 40)
    if (p - b) % 2 or (p - b) // 2 * 2 <= b: return None
    return N(f"An isosceles triangle has a perimeter of {p} cm. Its odd side is {b} cm. How long is each equal side?", (p - b) // 2, "cm", units=["cm"], o="O1", d="H")


s.std([t1, t4, t2, t3, t5, t7, t6, t8], EX("Explain the difference between an isosceles and a scalene triangle.", [("an isosceles triangle has two equal sides", "two equal|2 equal"), ("a scalene triangle has no equal sides", "no equal|all different|none")], "An isosceles triangle has two equal sides (and two equal angles). A scalene triangle has no equal sides at all.", o="O1"))

s = U.section("2.2", "Symmetry", ["O2"])
s.idea("Lines of symmetry", ["A **line of symmetry** splits a shape into two halves that are mirror images. If you fold along it, the halves match exactly.",
       "A square has 4 lines of symmetry; a rectangle has 2; an equilateral triangle has 3."], fig={"kind": "shape", "pts": [[0, 0], [4, 0], [4, 4], [0, 4]]})
s.check(N("How many lines of symmetry does a rectangle (not a square) have?", 2, o="O2"))
s.idea("Reflecting", ["To complete a symmetrical pattern, **reflect** each square in the mirror line: it lands the same distance away on the other side."])
s.mistake("Diagonals of a rectangle", ["The diagonals of a rectangle are NOT lines of symmetry: the halves do not match when folded."])


def y1(r):
    n = pick(r, [k for k in LOS if k != "circle"])
    return N(f"How many lines of symmetry does a {n} have?", LOS[n], o="O2")
def y2(r):
    ns = r.sample([k for k in LOS if k != "circle"], 4)
    return GD("How many lines of symmetry does each shape have?", "Lines", [(n, str(LOS[n])) for n in ns], o="O2", extra=["0", "1", "2", "3", "4"])
def y3(r):
    n = pick(r, ["equilateral", "isosceles", "scalene"])
    return N("How many lines of symmetry does this triangle have?", {"equilateral": 3, "isosceles": 1, "scalene": 0}[n], o="O2", fig={"kind": "shape", "pts": TRI[n], "ticks": TICK[n]})
def y4(r):
    w = pick(r, "AHMTUVWXOBCDEK")
    v = w in "AHMTUVWXO"; h = w in "BCDEKXHO"
    ans = "both" if v and h else "vertical" if v else "horizontal"
    return MC(f"The capital letter {w} has which line of symmetry?", ans, [x for x in ["vertical", "horizontal", "both", "none"] if x != ans][:3], o="O2")
def y5(r):
    x, y = r.randint(1, 5), r.randint(-4, 4)
    return S(f"The y-axis is a mirror line. Point A is at ({x}, {sg(y)}). Write the coordinates of its reflection.", PP(-x, y), o="O2", fig=G([{"x": x, "y": y, "l": "A"}], rng=6))
def y6(r):
    d = r.randint(1, 6)
    return N(f"A square on a grid is {d} squares to the right of a vertical mirror line. How many squares to the left of the line is its reflection?", d, "squares", units=["squares"], o="O2")
def y7(r):
    return MS("Select ALL the shapes with exactly one line of symmetry.", ["isosceles triangle", "kite"], ["square", "scalene triangle", "rectangle"], o="O2")
def y8(r):
    n = pick(r, [5, 6, 8])
    return N(f"A regular polygon has {n} sides. How many lines of symmetry does it have?", n, o="O2", d="H")
def y9(r):
    T = [[1, 1], [r.randint(3, 5), 1], [1, r.randint(2, 5)]]
    return MC("Shape B is a reflection of shape A. Which line is the mirror line?", "the y-axis", ["the x-axis", "there is no mirror line"], o="O2", fig=G(polys=[{"pts": T, "l": "A"}, {"pts": [[-a, b] for a, b in T], "l": "B"}]))


s.std([y3, y9, y1, y2, y4, y5, y6, y7, y8], EX("Explain why a square has 4 lines of symmetry.", [("it folds in half up-down and across", "vertical|horizontal|across|down"), ("and along both diagonals: 2 + 2 = 4", "diagonal")], "A square can be folded so the halves match along a vertical line, a horizontal line and both diagonals. That makes 4 lines of symmetry.", o="O2"))

U.mindmap(("Triangles", "Equilateral • isosceles • scalene", "O1", "2.1"), ("Symmetry", "Lines of symmetry • reflections", "O2", "2.2"))
