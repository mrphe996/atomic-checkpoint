# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 8 Shapes and symmetry (8.1 Identifying the symmetry of 2D shapes, 8.2 Circles and polygons,
8.3 Recognising congruent shapes, 8.4 3D shapes). Written by the Atomic teaching team."""
from math import cos, sin, pi
from kit import *

U = Unit(8, "Shapes and Symmetry", "Geometry and measure",
         "Line and rotational symmetry, parts of a circle, regular and irregular polygons, congruent shapes, and 3D shapes with their nets.",
         {"O1": {"code": "7Gg.04", "sec": "8.1", "codeNote": "", "t": "Identify lines of symmetry and the order of rotational symmetry of 2D shapes."},
          "O2": {"code": "7Gg.05", "sec": "8.2", "codeNote": "", "t": "Know the parts of a circle and classify polygons, including regular polygons."},
          "O3": {"code": "7Gg.06", "sec": "8.3", "codeNote": "", "t": "Recognise congruent shapes and identify corresponding sides and angles."},
          "O4": {"code": "7Gg.07", "sec": "8.4", "codeNote": "", "t": "Identify and describe 3D shapes, their faces, edges and vertices, and match them to nets."}})
NAMES = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon", 10: "decagon"}
REG = lambda n: {"kind": "shape", "pts": [[round(cos(2 * pi * i / n + pi / 2), 3), round(sin(2 * pi * i / n + pi / 2), 3)] for i in range(n)]}
SYM = {"square": (4, 4), "rectangle": (2, 2), "equilateral triangle": (3, 3), "isosceles triangle": (1, 1), "rhombus": (2, 2), "parallelogram": (0, 2), "kite": (1, 1), "regular hexagon": (6, 6)}

# ================================================================== 8.1
s = U.section("8.1", "Identifying the symmetry of 2D shapes", ["O1"])
s.idea("Line symmetry", ["A **line of symmetry** splits a shape into two halves that are mirror images. If you fold along it, the halves match exactly.",
       "A rectangle has 2 lines of symmetry; a square has 4."], fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]]})
s.idea("Rotational symmetry", ["A shape has **rotational symmetry** if it looks the same after a turn of less than 360°. The **order** is how many times it fits onto itself in one full turn."])
s.check(N("What is the order of rotational symmetry of a square?", 4, o="O1"))
s.mistake("Diagonals of a rectangle", ["The diagonals of a rectangle are NOT lines of symmetry."])


def y1(r):
    n = pick(r, list(SYM))
    return N(f"How many lines of symmetry does a {n} have?", SYM[n][0], o="O1")
def y2(r):
    n = pick(r, list(SYM))
    return N(f"What is the order of rotational symmetry of a {n}?", SYM[n][1], o="O1")
def y3(r):
    rows = r.sample(list(SYM), 4)
    return GD("How many lines of symmetry does each shape have?", "Lines", [(n, str(SYM[n][0])) for n in rows], o="O1", extra=["0", "1", "2", "3", "4", "6"])
def y4(r):
    n = r.randint(5, 10)
    return N(f"How many lines of symmetry does this regular {NAMES[n]} have?", n, o="O1", fig=REG(n))
def y5(r):
    n = r.randint(3, 10)
    return N(f"What is the order of rotational symmetry of this regular polygon?", n, o="O1", fig=REG(n))
def y6(r):
    w = pick(r, ["H", "X", "O", "N", "S", "Z", "A", "M", "E"])
    lines = {"H": 2, "X": 2, "O": 2, "N": 0, "S": 0, "Z": 0, "A": 1, "M": 1, "E": 1}
    return N(f"How many lines of symmetry does the capital letter {w} have? (Use plain block letters.)", lines[w], o="O1")
def y7(r):
    n = pick(r, list(SYM))
    return TB(f"Complete the table for a {n}.", ["Symmetry", "Number"], [["Lines of symmetry", B(SYM[n][0])], ["Order of rotational symmetry", B(SYM[n][1])]], o="O1")
def y8(r):
    return MC("Which shape has rotational symmetry of order 2 but no lines of symmetry?", "a parallelogram", ["a rectangle", "a kite", "an isosceles triangle"], o="O1", d="H")


s.std([y3, y4, y1, y2, y5, y6, y7, y8], EX("Explain why an equilateral triangle has rotational symmetry of order 3.", [("it looks the same after a turn of 120°", ["120|third of a turn"]), ("this happens 3 times in a full turn", ["3 times|three times|360"])], "Turning an equilateral triangle through 120° makes it look exactly the same, and this happens 3 times in one full turn (3 × 120° = 360°).", o="O1"))

# ================================================================== 8.2
s = U.section("8.2", "Circles and polygons", ["O2"])
s.idea("Parts of a circle", ["The **centre** is the middle. The **radius** goes from the centre to the edge. The **diameter** goes across through the centre: **diameter = 2 × radius**. The **circumference** is the distance all the way round."], fig={"kind": "circle", "r": "radius"})
s.idea("Polygons", ["A **polygon** is a flat shape with straight sides. A **regular polygon** has all sides equal and all angles equal."])
s.check(N("A circle has radius 7 cm. What is its diameter?", 14, "cm", units=["cm"], o="O2"))
s.mistake("Radius or diameter?", ["The radius is HALF the diameter."])


def c1(r):
    rr = r.randint(2, 30)
    return N(f"A circle has radius {rr} cm. What is its diameter?", 2 * rr, "cm", units=["cm"], o="O2", fig={"kind": "circle", "r": f"{rr} cm"})
def c2(r):
    d = 2 * r.randint(2, 30)
    return N(f"A circle has diameter {d} cm. What is its radius?", d // 2, "cm", units=["cm"], o="O2", fig={"kind": "circle", "d": f"{d} cm"})
def c3(r):
    n = r.randint(3, 10)
    return S(f"What is the name of a polygon with {n} sides?", [NAMES[n]] + (["quadrilateral", "quadrilateral"] if n == 4 else []), o="O2")
def c4(r):
    rows = [("From the centre to the edge", "Radius"), ("Across through the centre", "Diameter"), ("The distance round the outside", "Circumference"), ("The middle point", "Centre")]
    return GD("Name each part of a circle.", "Part", rows, o="O2")
def c5(r):
    n, l = r.randint(5, 10), r.randint(2, 12)
    return N(f"A regular {NAMES[n]} has sides of {l} cm. What is its perimeter?", n * l, "cm", units=["cm"], o="O2", fig=REG(n))
def c6(r):
    n = r.randint(5, 10); P = n * r.randint(2, 9)
    return N(f"A regular {NAMES[n]} has a perimeter of {P} cm. How long is each side?", P // n, "cm", units=["cm"], o="O2")
def c7(r):
    return MC("What makes a polygon regular?", "all its sides and all its angles are equal", ["it has four sides", "it has a right angle", "it has at least one line of symmetry"], o="O2")
def c8(r):
    rr = r.randint(3, 10)
    return N(f"Two circles of radius {rr} cm touch in a row inside a rectangle. How long is the rectangle?", 4 * rr, "cm", units=["cm"], o="O2", d="H", reason=f"Two diameters: 2 × {2 * rr} = {4 * rr} cm.")


s.std([c4, c1, c2, c3, c5, c6, c7, c8], EX("Explain why the diameter of a circle is twice the radius.", [("the diameter goes from edge to edge through the centre", ["through the centre|across"]), ("it is made of two radii", ["two radii|2 radii|two radius|2 ?×"])], "The diameter goes across the circle through the centre, so it is made of two radii end to end: diameter = 2 × radius.", o="O2"))

# ================================================================== 8.3
s = U.section("8.3", "Recognising congruent shapes", ["O3"])
s.idea("Congruent", ["Shapes are **congruent** if they are exactly the same shape and size. One may be turned or flipped.",
       "**Corresponding** sides and angles are equal: if triangle ABC is congruent to PQR, then AB = PQ and angle A = angle P."], fig={"kind": "coord", "x": [0, 12], "y": [0, 6], "polys": [{"pts": [[1, 1], [5, 1], [1, 4]], "l": "A"}, {"pts": [[11, 1], [7, 1], [11, 4]], "l": "B"}]})
s.check(MC("Are two squares with sides 5 cm and 5 cm congruent?", "Yes", ["No", "Only if they are the same colour"], o="O3"))
s.mistake("Same shape is not enough", ["Two squares of different sizes are similar, not congruent."])


def g1(r):
    a, b = r.randint(3, 10), r.randint(3, 10)
    return N(f"Triangles ABC and PQR are congruent. AB = {a} cm and BC = {b} cm. How long is PQ?", a, "cm", units=["cm"], o="O3")
def g2(r):
    a = r.randint(30, 80)
    return N(f"Triangles ABC and DEF are congruent. Angle B = {a}°. What is angle E?", a, "°", units=["°"], o="O3")
def g3(r):
    a, b = r.randint(2, 6), r.randint(2, 6)
    return MC("Rectangle A is shown. Which rectangle is congruent to it?", f"{b} cm by {a} cm", [f"{a + 1} cm by {b} cm", f"{2 * a} cm by {2 * b} cm", f"{a} cm by {b + 2} cm"], o="O3", fig={"kind": "shape", "pts": [[0, 0], [a, 0], [a, b], [0, b]], "s": [f"{a} cm", f"{b} cm", "", ""]})
def g4(r):
    rows = [("Same shape and same size", "Congruent"), ("Same shape, different size", "Not congruent"), ("One is a reflection of the other", "Congruent"), ("One is twice as big", "Not congruent")]
    return GD("Are the shapes congruent?", "Congruent?", rows, o="O3")
def g5(r):
    a, b, c = r.randint(3, 9), r.randint(3, 9), r.randint(3, 9)
    if a + b <= c or a + c <= b or b + c <= a: return None
    return TB(f"Triangle ABC (AB = {a} cm, BC = {b} cm, CA = {c} cm) is congruent to triangle XYZ. Find the sides of XYZ.", ["Side", "Length (cm)"], [["XY", B(a)], ["YZ", B(b)], ["ZX", B(c)]], o="O3")
def g6(r):
    a, b = r.randint(3, 8), r.randint(3, 8)
    T = [[1, 1], [1 + a, 1], [1, 1 + b]]
    return MC("Shape B is a copy of shape A that has been flipped. Are they congruent?", "Yes", ["No", "Only if they are the same colour"], o="O3", fig={"kind": "coord", "x": [0, 2 * a + 4], "y": [0, b + 2], "polys": [{"pts": T, "l": "A"}, {"pts": [[2 * a + 3 - x, y] for x, y in T], "l": "B"}]})
def g7(r):
    a = r.randint(3, 10); p = 4 * a
    return N(f"Two squares are congruent. One has a perimeter of {p} cm. What is the side length of the other?", a, "cm", units=["cm"], o="O3")


s.std([g4, g5, g1, g2, g3, g6, g7], EX("Explain how you can tell if two triangles are congruent.", [("they have the same shape and size", ["same shape|same size"]), ("all corresponding sides (and angles) are equal; one may be turned or flipped", ["sides|angles|turned|flipped|rotat|reflect"])], "Two triangles are congruent if they are exactly the same shape and size: all corresponding sides and angles are equal, even if one is turned or flipped.", o="O3"))

# ================================================================== 8.4
s = U.section("8.4", "3D shapes", ["O4"])
s.idea("Faces, edges and vertices", ["A **face** is a flat surface, an **edge** is where two faces meet, and a **vertex** is a corner.",
       "A cube has 6 faces, 12 edges and 8 vertices. A **net** is a flat shape that folds up to make the solid."], fig={"kind": "solid", "solid": "cuboid", "a": "", "b": "", "c": ""})
s.check(N("How many faces does a triangular prism have?", 5, o="O4"))
s.mistake("Count hidden edges", ["Remember the edges and corners you cannot see in the picture."])
SOL = [("cube", 6, 12, 8), ("cuboid", 6, 12, 8), ("triangular prism", 5, 9, 6), ("square-based pyramid", 5, 8, 5), ("tetrahedron (triangular pyramid)", 4, 6, 4)]


def d1(r):
    n, F_, E_, V_ = pick(r, SOL); k = r.randrange(3)
    return N(f"How many {['faces', 'edges', 'vertices'][k]} does a {n} have?", [F_, E_, V_][k], o="O4")
def d2(r):
    sols = r.sample(SOL, 3)
    return TB("Complete the table.", ["Shape", "Faces", "Edges", "Vertices"], [[n, B(F_), B(E_), B(V_)] for n, F_, E_, V_ in sols], o="O4", d="H")
def d3(r):
    rows = [("6 squares", "Cube"), ("2 triangles and 3 rectangles", "Triangular prism"), ("1 square and 4 triangles", "Square-based pyramid"), ("4 triangles", "Tetrahedron")]
    return GD("Which solid does each net make?", "Solid", rows, o="O4")
def d4(r):
    return MC("Which solid has a curved surface?", pick(r, ["a cylinder", "a cone", "a sphere"]), ["a cube", "a pyramid", "a prism"], o="O4")
def d5(r):
    n = pick(r, ["cylinder", "cuboid", "cone"]); plan = {"cylinder": "a circle", "cuboid": "a rectangle", "cone": "a circle"}[n]
    return MC(f"What is the view from directly above (the plan) of a {n} standing on its base?", plan, [x for x in ["a circle", "a rectangle", "a triangle", "a square"] if x != plan][:3], o="O4", fig={"kind": "solid", "solid": n})
def d6(r):
    l = r.randint(2, 9)
    return N(f"A cube has edges of {l} cm. What is the total length of all its edges?", 12 * l, "cm", units=["cm"], o="O4", fig={"kind": "solid", "solid": "cuboid", "a": f"{l} cm", "b": f"{l} cm", "c": f"{l} cm"})
def d7(r):
    n = r.randint(4, 9)
    return N(f"A pyramid has a base with {n} sides. How many faces does it have?", n + 1, o="O4", d="H")


s.std([d2, d3, d1, d4, d5, d6, d7], EX("Explain the difference between a face, an edge and a vertex.", [("a face is a flat surface", ["flat|surface"]), ("an edge is where two faces meet; a vertex is a corner", ["meet|corner|point"])], "A face is a flat surface of the solid. An edge is a line where two faces meet. A vertex is a corner where edges meet.", o="O4"))

U.mindmap(("Symmetry", "Lines of symmetry • order of rotational symmetry", "O1", "8.1"), ("Circles and polygons", "Radius × 2 = diameter • regular polygons", "O2", "8.2"),
          ("Congruent shapes", "Same shape and size • corresponding sides and angles", "O3", "8.3"), ("3D shapes", "Faces, edges, vertices • nets", "O4", "8.4"))
