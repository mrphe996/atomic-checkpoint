# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 8 Shapes and symmetry (8.1 Identifying the symmetry of 2D shapes, 8.2 Circles and polygons,
8.3 Recognising congruent shapes, 8.4 3D shapes). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
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
s.idea("Why a regular polygon has as many lines as sides", ["In a regular polygon every side and every angle is the same, so a mirror line through any corner (or the middle of any side) gives two matching halves.",
       "A regular hexagon has 6 lines of symmetry and rotational symmetry of order 6: turning it by 360° ÷ 6 = 60° looks identical."], fig=REG(6))
s.check(MC("Before you read on: how many lines of symmetry does a rectangle (not a square) have?", "2", [("4", "The diagonals are not mirror lines – folding along one does not match the corners."), ("0", "Folding along the middle lines works.")], o="O1", hint="Imagine folding a sheet of paper."))
s.example("Same shape, different symmetry", "Compare a square and a rhombus that is not a square.", [("square: 4 lines, order 4", "all sides and angles equal"), ("rhombus: 2 lines (the diagonals), order 2", "the angles are not all equal")], "4 and 2 lines")
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


def h1(r):   # always / sometimes / never
    rows = r.sample([("A regular polygon has line symmetry", "Always true"), ("A triangle has rotational symmetry", "Sometimes true"), ("A shape with 2 lines of symmetry has rotational symmetry of order 2", "Always true"),
                     ("A parallelogram has a line of symmetry", "Sometimes true"), ("A shape has rotational symmetry of order 1", "Always true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O1", d="H", extra=["Always true", "Sometimes true", "Never true"],
              reason="Test examples: an equilateral triangle has order 3 but a scalene triangle has order 1; a rhombus is a parallelogram with 2 lines, but most parallelograms have none. Every shape fits onto itself after a full turn, so every shape has order at least 1.")
def h2(r):   # angle of turn
    n = pick(r, [3, 4, 5, 6, 8, 10])
    return N(f"A regular {NAMES[n]} is turned about its centre. What is the smallest angle of turn that makes it look the same?", 360 // n if 360 % n == 0 else round(360 / n, 1), "°", units=["°"], o="O1", d="H", fig=REG(n),
             reason=f"It has rotational symmetry of order {n}, so the smallest turn is 360° ÷ {n}.")
def h3(r):   # spot the error
    return MC("Leo says a parallelogram has 2 lines of symmetry, along its diagonals. Is he right?", "No – it has none, but rotational symmetry of order 2", [("Yes", "Fold along a diagonal: the halves do not match."), ("No – it has 4", "It has no mirror lines at all.")], o="O1", d="H",
              reason="A parallelogram (not a rhombus or rectangle) has no lines of symmetry. A half turn fits it onto itself, so its order of rotational symmetry is 2.")


s.std([y3, y4, y1, y2, y5, y6, y7, y8], EX("Explain why an equilateral triangle has rotational symmetry of order 3.", [("it looks the same after a turn of 120°", ["120|third of a turn"]), ("this happens 3 times in a full turn", ["3 times|three times|360"])], "Turning an equilateral triangle through 120° makes it look exactly the same, and this happens 3 times in one full turn (3 × 120° = 360°).", o="O1"),
      deep=[h1, h2, h3])

# ================================================================== 8.2
s = U.section("8.2", "Circles and polygons", ["O2"])
s.idea("Parts of a circle", ["The **centre** is the middle. The **radius** goes from the centre to the edge. The **diameter** goes across through the centre: **diameter = 2 × radius**. The **circumference** is the distance all the way round."], fig={"kind": "circle", "r": "radius"})
s.idea("Polygons", ["A **polygon** is a flat shape with straight sides. A **regular polygon** has all sides equal and all angles equal."])
s.check(N("A circle has radius 7 cm. What is its diameter?", 14, "cm", units=["cm"], o="O2"))
s.idea("Why the diameter is twice the radius", ["The diameter goes from the edge, through the centre, to the edge on the other side. It is made of two radii end to end, so d = 2r.",
       "Every radius of a circle is the same length – that is what makes it a circle: every point on the edge is the same distance from the centre."])
s.check(MC("Before you read on: a chord passes through the centre of a circle. What else is it called?", "A diameter", [("A radius", "A radius stops at the centre."), ("A tangent", "A tangent only touches the circle.")], o="O2"))
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


def k1(r):   # regular or not
    rows = r.sample([("a square", "Regular"), ("a rectangle that is not a square", "Not regular"), ("an equilateral triangle", "Regular"), ("a rhombus that is not a square", "Not regular"), ("a hexagon with equal sides and equal angles", "Regular")], 4)
    return GD("Is each polygon regular?", "Regular?", rows, o="O2", d="H", extra=["Regular", "Not regular"], reason="Regular means ALL sides equal AND all angles equal. A rhombus has equal sides but unequal angles; a rectangle has equal angles but unequal sides.")
def k2(r):   # radius from diameter in context
    d = r.randint(6, 40) * 2
    return N(f"A round table has a diameter of {d} cm. A cloth hangs 10 cm over the edge all the way round. What is the radius of the cloth?", d // 2 + 10, "cm", units=["cm"], o="O2", d="H",
             reason=f"Table radius {d // 2} cm, plus 10 cm overhang = {d // 2 + 10} cm.")
def k3(r):   # spot the error
    return MC("Sara says a regular polygon with 6 sides has all angles equal to 60°. Is she right?", "No – each angle is 120°", [("Yes", "60° is the angle at the centre, not the interior angle."), ("No – each angle is 90°", "That is a square.")], o="O2", d="VH",
              reason="A hexagon splits into 6 equilateral triangles from the centre; each interior angle is made of two 60° angles: 120°.")


s.std([c4, c1, c2, c3, c5, c6, c7, c8], EX("Explain why the diameter of a circle is twice the radius.", [("the diameter goes from edge to edge through the centre", ["through the centre|across"]), ("it is made of two radii", ["two radii|2 radii|two radius|2 ?×"])], "The diameter goes across the circle through the centre, so it is made of two radii end to end: diameter = 2 × radius.", o="O2"),
      deep=[k1, k2, k3])

# ================================================================== 8.3
s = U.section("8.3", "Recognising congruent shapes", ["O3"])
s.idea("Congruent", ["Shapes are **congruent** if they are exactly the same shape and size. One may be turned or flipped.",
       "**Corresponding** sides and angles are equal: if triangle ABC is congruent to PQR, then AB = PQ and angle A = angle P."], fig={"kind": "coord", "x": [0, 12], "y": [0, 6], "polys": [{"pts": [[1, 1], [5, 1], [1, 4]], "l": "A"}, {"pts": [[11, 1], [7, 1], [11, 4]], "l": "B"}]})
s.check(MC("Are two squares with sides 5 cm and 5 cm congruent?", "Yes", ["No", "Only if they are the same colour"], o="O3"))
s.idea("How to test for congruence", ["Congruent shapes match exactly when one is placed on the other – after turning or flipping if needed. Matching sides must be equal and matching angles must be equal.",
       "An enlarged copy is NOT congruent: the shape is the same but the size is not."])
s.check(MC("Before you read on: a triangle is flipped over. Is the new triangle congruent to the old one?", "Yes", [("No", "Flipping does not change any length or angle."), ("Only if it is isosceles", "Every triangle stays the same size when flipped.")], o="O3"))
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


def m1_(r):   # always/sometimes/never
    rows = r.sample([("Two squares with the same side length are congruent", "Always true"), ("Two rectangles with the same area are congruent", "Sometimes true"),
                     ("A shape and its enlargement (scale factor 2) are congruent", "Never true"), ("Two circles with the same radius are congruent", "Always true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O3", d="H", extra=["Always true", "Sometimes true", "Never true"],
              reason="A 2 × 6 rectangle and a 3 × 4 rectangle both have area 12 but are not congruent. An enlargement changes the size.")
def m2_(r):   # matching side
    a, b, c = r.sample(range(4, 15), 3)
    return N(f"Triangle ABC is congruent to triangle PQR, with A matching P, B matching Q and C matching R. AB = {a} cm, BC = {b} cm, CA = {c} cm. How long is QR?", b, "cm", units=["cm"], o="O3", d="H",
             reason=f"QR matches BC, so QR = {b} cm.")


s.std([g4, g5, g1, g2, g3, g6, g7], EX("Explain how you can tell if two triangles are congruent.", [("they have the same shape and size", ["same shape|same size"]), ("all corresponding sides (and angles) are equal; one may be turned or flipped", ["sides|angles|turned|flipped|rotat|reflect"])], "Two triangles are congruent if they are exactly the same shape and size: all corresponding sides and angles are equal, even if one is turned or flipped.", o="O3"),
      deep=[m1_, m2_])

# ================================================================== 8.4
s = U.section("8.4", "3D shapes", ["O4"])
s.idea("Faces, edges and vertices", ["A **face** is a flat surface, an **edge** is where two faces meet, and a **vertex** is a corner.",
       "A cube has 6 faces, 12 edges and 8 vertices. A **net** is a flat shape that folds up to make the solid."], fig={"kind": "solid", "solid": "cuboid", "a": "", "b": "", "c": ""})
s.check(N("How many faces does a triangular prism have?", 5, o="O4"))
s.idea("A check that always works", ["For a prism or pyramid made of flat faces, count: faces + vertices − edges. A cube gives 6 + 8 − 12 = 2. A square-based pyramid gives 5 + 5 − 8 = 2.",
       "This is Euler's rule (F + V − E = 2). If your count gives any other number, you have missed or double-counted something."], table={"head": ["Shape", "F", "V", "E", "F + V − E"], "rows": [["Cube", "6", "8", "12", "2"], ["Triangular prism", "5", "6", "9", "2"], ["Square-based pyramid", "5", "5", "8", "2"]]})
s.check(MC("Before you read on: how many edges does a triangular prism have?", "9", [("6", "That is the number of vertices."), ("5", "That is the number of faces.")], o="O4", hint="3 edges on each triangle, plus 3 joining them."))
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


def p1_(r):   # use Euler
    F, V = pick(r, [(6, 8), (5, 6), (5, 5), (7, 10), (8, 12)])
    return N(f"A solid has {F} faces and {V} vertices. Use F + V − E = 2 to find how many edges it has.", F + V - 2, o="O4", d="H", reason=f"E = F + V − 2 = {F} + {V} − 2 = {F + V - 2}.")
def p2_(r):   # spot the error
    return MC("Nia counts a cuboid: 6 faces, 8 vertices, 8 edges. Which number is wrong?", "The edges: there are 12", [("The faces", "A cuboid has 6 faces."), ("The vertices", "A cuboid has 8 corners.")], o="O4", d="H",
              reason="Check with F + V − E = 2: 6 + 8 − 8 = 6, not 2. A cuboid has 12 edges.")
def p3_(r):   # prism pattern
    n = r.randint(5, 9)
    return TB(f"A prism has a {n}-sided polygon as its end. Complete the table.", ["", "Number"], [["Faces", B(n + 2)], ["Vertices", B(2 * n)], ["Edges", B(3 * n)]], o="O4", d="VH",
              reason=f"2 ends + {n} side faces; {n} vertices on each end; {n} edges on each end + {n} joining them.")


s.std([d2, d3, d1, d4, d5, d6, d7], EX("Explain the difference between a face, an edge and a vertex.", [("a face is a flat surface", ["flat|surface"]), ("an edge is where two faces meet; a vertex is a corner", ["meet|corner|point"])], "A face is a flat surface of the solid. An edge is a line where two faces meet. A vertex is a corner where edges meet.", o="O4"),
      deep=[p1_, p2_, p3_])

U.mindmap(("Symmetry", "Lines of symmetry • order of rotational symmetry", "O1", "8.1"), ("Circles and polygons", "Radius × 2 = diameter • regular polygons", "O2", "8.2"),
          ("Congruent shapes", "Same shape and size • corresponding sides and angles", "O3", "8.3"), ("3D shapes", "Faces, edges, vertices • nets", "O4", "8.4"))
