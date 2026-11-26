# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 8 Shapes and symmetry (8.1 Quadrilaterals and polygons, 8.2 The circumference of a circle,
8.3 3D shapes). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from math import pi
from kit import *

U = Unit(8, "Shapes and Symmetry", "Geometry and measure",
         "Properties of quadrilaterals and regular polygons, the circumference of a circle, and 3D shapes: nets, plans and elevations.",
         {"O1": {"code": "8Gg.04", "sec": "8.1", "codeNote": "", "t": "Identify and describe the properties of quadrilaterals and regular polygons, including symmetry."},
          "O2": {"code": "8Gg.05", "sec": "8.2", "codeNote": "", "t": "Know and use the formula for the circumference of a circle."},
          "O3": {"code": "8Gg.06", "sec": "8.3", "codeNote": "", "t": "Use nets, plans and elevations of 3D shapes, and count faces, edges and vertices."}})
r1 = lambda v: round(v, 1)
QUAD = {"square": (4, 4, "Yes", "Yes"), "rectangle": (2, 2, "Yes", "Yes"), "rhombus": (2, 2, "Yes", "No"), "parallelogram": (0, 2, "Yes", "No"), "kite": (1, 1, "No", "No"), "isosceles trapezium": (1, 1, "No", "No")}
# name: (lines of symmetry, rotational order, diagonals bisect each other, diagonals equal)
POLY = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon", 10: "decagon", 12: "dodecagon"}

# ================================================================== 8.1
s = U.section("8.1", "Quadrilaterals and polygons", ["O1"])
s.idea("Quadrilaterals", ["Square, rectangle, rhombus, parallelogram, kite and trapezium are the special quadrilaterals. Describe them by their **sides**, **angles**, **diagonals** and **symmetry**.",
       "A **parallelogram** has two pairs of parallel sides and rotational symmetry of order 2 but no lines of symmetry. A **kite** has one line of symmetry."],
       table={"head": ["Shape", "Lines of symmetry", "Rotational order"], "rows": [[k, str(v[0]), str(v[1])] for k, v in QUAD.items()]})
s.check(N("How many lines of symmetry does a rhombus have?", 2, o="O1"))
s.idea("Regular polygons", ["A **regular** polygon has all sides equal and all angles equal. A regular n-sided polygon has **n lines of symmetry** and **rotational symmetry of order n**."], fig={"kind": "shape", "pts": [[1, 0], [3, 0], [4, 1.7], [3, 3.4], [1, 3.4], [0, 1.7]]})
s.check(N("A regular octagon has how many lines of symmetry?", 8, o="O1"))
s.idea("Why the interior angles of a polygon add to (n − 2) × 180°", ["From one corner of an n-sided polygon you can draw diagonals that split it into n − 2 triangles. Each triangle gives 180°.",
       "A pentagon splits into 3 triangles: 3 × 180° = 540°."])
s.check(MC("Before you read on: what do the interior angles of a hexagon add up to?", "720°", [("1080°", "A hexagon splits into 4 triangles, not 6."), ("360°", "That is a quadrilateral.")], o="O1"))
s.mistake("Diagonals are not always lines of symmetry", ["A rectangle's diagonals are NOT lines of symmetry: folding along one does not match the halves."])


def q1(r):
    n = pick(r, list(QUAD)); k = r.randint(0, 1)
    return N(f"How many {'lines of symmetry' if k == 0 else 'is the order of rotational symmetry of'} {'does a' if k == 0 else 'a'} {n}{' have' if k == 0 else ''}?".replace("How many is the order", "What is the order"), QUAD[n][k], o="O1", reason=f"A {n}: {QUAD[n][0]} lines of symmetry, rotational order {QUAD[n][1]}.")
def q2(r):
    rows = r.sample(list(QUAD), 4)
    return GD("How many lines of symmetry does each shape have?", "Lines", [(n, str(QUAD[n][0])) for n in rows], o="O1", extra=["0", "1", "2", "4"])
def q3(r):
    n = pick(r, [5, 6, 7, 8, 9, 10, 12])
    return N(f"What is the order of rotational symmetry of a regular {POLY[n]}?", n, o="O1", fig={"kind": "shape", "pts": [[round(__import__('math').cos(2 * pi * i / n), 3), round(__import__('math').sin(2 * pi * i / n), 3)] for i in range(n)]}, reason=f"A regular {n}-sided polygon has rotational order {n}.")
def q4(r):
    c = pick(r, [("has diagonals that bisect each other at right angles but are not equal", "rhombus"), ("has one line of symmetry and one pair of equal angles", "kite"), ("has two pairs of parallel sides and no lines of symmetry", "parallelogram"), ("has four right angles but only two lines of symmetry", "rectangle")])
    return MC(f"Which quadrilateral {c[0]}?", c[1], [x for x in ["rhombus", "kite", "parallelogram", "rectangle", "square"] if x != c[1]][:3], o="O1", d="H")
def q5(r):
    n = pick(r, [5, 6, 8, 9, 10, 12]); s_ = r.randint(3, 15)
    return N(f"A regular {POLY[n]} has sides of {s_} cm. Find its perimeter.", n * s_, "cm", units=["cm"], o="O1", reason=f"{n} × {s_} = {n * s_} cm.")
def q6(r):
    n = pick(r, [5, 6, 8, 9, 10, 12]); P = n * r.randint(3, 12)
    return N(f"A regular {POLY[n]} has a perimeter of {P} cm. How long is each side?", P // n, "cm", units=["cm"], o="O1", reason=f"{P} ÷ {n} = {P // n} cm.")
def q7(r):
    rows = [("All sides equal", "Rhombus"), ("Diagonals equal and bisect each other", "Rectangle"), ("One line of symmetry, diagonals cross at 90°", "Kite"), ("Only rotational symmetry of order 2", "Parallelogram")]
    return GD("Which shape is described? (Choose the most likely shape that is not a square.)", "Shape", rows, o="O1", d="H")
def q8(r):
    a = r.randint(55, 80)
    return N(f"A parallelogram has one angle of {a}°. Find the size of the angle next to it.", 180 - a, "°", units=["°"], o="O1", fig={"kind": "shape", "pts": [[0, 0], [7, 0], [9, 4], [2, 4]], "ang": [f"{a}°", "?", "", ""]}, reason=f"Next angles in a parallelogram add to 180°: {180 - a}°.")
def q9(r):
    n = pick(r, [5, 6, 8, 9, 10])
    return MS(f"Select ALL the true statements about a regular {POLY[n]}.", [f"It has {n} lines of symmetry", f"It has rotational symmetry of order {n}", "All its angles are equal"], [f"It has {n - 1} lines of symmetry", "Its diagonals are all equal"] if n > 4 else [f"It has {n + 1} lines of symmetry"], o="O1", d="H")


def q10(r):
    a = r.randint(40, 80)
    return N(f"A rhombus has one angle of {a}°. Find the size of the largest angle.", 180 - a, "°", units=["°"], o="O1", d="H", reason=f"Next angles add to 180°: {180 - a}°.")
def q11(r):
    a, b = r.randint(50, 80), r.randint(90, 130); c = 360 - a - 2 * b
    if c <= 20: return None
    return N(f"A kite has two equal angles of {b}°, and its other angles are {a}° and x°. Find x.", c, "°", units=["°"], o="O1", d="H", fig={"kind": "shape", "pts": [[0, 0], [3, -2], [9, 0], [3, 2]], "ang": [f"{a}°", f"{b}°", "x", f"{b}°"]}, reason=f"360° − {a}° − 2 × {b}° = {c}°.")


def d81(r):
    n = r.randint(5, 12)
    return N(f"What is each interior angle of a regular polygon with {n} sides?" + ("" if (n - 2) * 180 % n == 0 else " Give your answer to 1 decimal place."), round((n - 2) * 180 / n, 1), "°", units=["°"], o="O1", d="H", tol=0.05,
             reason=f"Total ({n} − 2) × 180 = {(n - 2) * 180}°; ÷ {n} = {(n - 2) * 180 / n:.1f}°.")


s.std([q2, q8, q1, q3, q4, q5, q6, q7, q9, q10, q11], EX("Explain why a parallelogram has rotational symmetry but no lines of symmetry.", [("a half turn about its centre fits it onto itself", ["half turn|180|order 2|turn"]), ("folding along any line does not match the two halves", ["fold|mirror|does not match|doesn't match|not symmetr"])], "Turning a parallelogram through 180° about its centre makes it fit exactly onto itself, so it has rotational symmetry of order 2. But no fold line makes the two halves match, so it has no lines of symmetry.", o="O1"),
      deep=[d81])

# ================================================================== 8.2
s = U.section("8.2", "The circumference of a circle", ["O2"])
s.idea("Circle words and π", ["The **circumference** is the distance round a circle. The **diameter** goes across through the centre; the **radius** is half the diameter.",
       "For every circle, circumference ÷ diameter is the same number, **π** (pi) ≈ 3.14159…  So **C = πd = 2πr**."], fig={"kind": "circle", "d": "d"})
s.example("Using the formula", "Find the circumference of a circle with radius 6 cm, to 1 decimal place.", [("C = 2πr = 2 × π × 6", ""), ("= 12π = 37.699…", "")], "37.7 cm")
s.check(N("Find the circumference of a circle with diameter 10 cm, to 1 d.p.", r1(pi * 10), "cm", units=["cm"], tol=0.06, o="O2"))
s.idea("Why π appears", ["For every circle, the circumference divided by the diameter is the same number, about 3.14. We call it π. So C = πd, or C = 2πr.",
       "Try it: a lid with diameter 10 cm has a circumference of about 31.4 cm – a bit more than 3 diameters."])
s.check(MC("Before you read on: a wheel has diameter 50 cm. About how far does it roll in one turn?", "About 157 cm", [("About 50 cm", "One turn rolls the whole circumference, not the diameter."), ("About 314 cm", "That uses 2πd; use πd.")], o="O2"))
s.mistake("Radius or diameter?", ["If you are given the radius, double it (or use 2πr). Using πr gives half the circumference."])


def c1(r):
    d = r.randint(3, 40)
    return N(f"Find the circumference of a circle with diameter {d} cm. Give your answer to 1 d.p.", r1(pi * d), "cm", units=["cm"], tol=0.06, o="O2", fig={"kind": "circle", "d": f"{d} cm"}, reason=f"C = π × {d} ≈ {r1(pi * d)} cm.")
def c2(r):
    rr = r.randint(2, 25)
    return N(f"Find the circumference of a circle with radius {rr} cm. Give your answer to 1 d.p.", r1(2 * pi * rr), "cm", units=["cm"], tol=0.06, o="O2", fig={"kind": "circle", "r": f"{rr} cm"}, reason=f"C = 2 × π × {rr} ≈ {r1(2 * pi * rr)} cm.")
def c3(r):
    d = r.randint(5, 40); C = r1(pi * d)
    return N(f"A circle has circumference {C} cm. Find its diameter to the nearest cm.", d, "cm", units=["cm"], tol=0.5, o="O2", d="H", reason=f"d = C ÷ π = {C} ÷ π ≈ {d} cm.")
def c4(r):
    d = r.randint(40, 80)
    return N(f"A bicycle wheel has diameter {d} cm. How far does it travel in one complete turn? Give your answer to the nearest cm.", round(pi * d), "cm", units=["cm"], tol=0.5, o="O2", reason=f"π × {d} ≈ {round(pi * d)} cm.")
def c5(r):
    d = r.randint(4, 20)
    return N(f"Find the perimeter of a semicircle with diameter {d} cm (the curved part and the straight edge). Give your answer to 1 d.p.", r1(pi * d / 2 + d), "cm", units=["cm"], tol=0.06, o="O2", d="H", fig={"kind": "circle", "part": "semi", "d": f"{d} cm"}, reason=f"π × {d} ÷ 2 + {d} ≈ {r1(pi * d / 2 + d)} cm.")
def c6(r):
    rr = r.randint(2, 12)
    return TB("Complete the table for the circle.", ["Measurement", "Value (1 d.p.)"], [["Diameter (cm)", B(2 * rr)], ["Circumference (cm)", B(r1(2 * pi * rr), 0.06)]], o="O2", data={"head": ["", "Radius"], "rows": [["Circle", f"{rr} cm"]]})
def c7(r):
    rows = [("The distance round a circle", "Circumference"), ("From the centre to the edge", "Radius"), ("Across the circle through the centre", "Diameter"), ("C ÷ d for any circle", "π")]
    return GD("Name each part.", "Word", rows, o="O2")
def c8(r):
    d = r.randint(10, 60); n = r.randint(5, 20)
    return N(f"A wheel of diameter {d} cm turns {n} times. How far does it travel? Give your answer in metres to 2 d.p.", round(pi * d * n / 100, 2), "m", units=["m"], tol=0.006, o="O2", d="H", reason=f"π × {d} × {n} ≈ {r1(pi * d * n)} cm = {round(pi * d * n / 100, 2)} m.")
def c9(r):
    rr = r.randint(3, 15)
    return MC(f"Which is the best estimate of the circumference of a circle with radius {rr} cm?", str(6 * rr), [str(3 * rr), str(rr * rr * 3), str(2 * rr)], o="O2", reason=f"C = 2πr ≈ 2 × 3 × {rr} = {6 * rr}.")


def c10(r):
    rr = r.randint(3, 15)
    return N(f"Find the perimeter of a quarter circle with radius {rr} cm (the curved edge and the two straight edges). Give your answer to 1 d.p.", r1(pi * rr / 2 + 2 * rr), "cm", units=["cm"], tol=0.06, o="O2", d="VH", fig={"kind": "circle", "part": "quarter", "r": f"{rr} cm"}, reason=f"2π × {rr} ÷ 4 + 2 × {rr} ≈ {r1(pi * rr / 2 + 2 * rr)} cm.")
def c11(r):
    l, d = r.randint(60, 100), r.randint(40, 70)
    return N(f"A running track has two straight sides of {l} m and two semicircular ends of diameter {d} m. Find the length of one lap, to the nearest metre.", round(2 * l + pi * d), "m", units=["m"], tol=0.5, o="O2", d="H", reason=f"2 × {l} + π × {d} ≈ {round(2 * l + pi * d)} m.")


def d82(r):
    d = r.randint(4, 30)
    return MC(f"A circle has radius {d} cm. Jo says its circumference is π × {d} cm. What is right?", f"2π × {d} = {2 * d}π cm", [(f"π × {d} cm", "That uses the radius in C = πd; the diameter is twice the radius."), (f"π × {d * d} cm", "That squares the radius (area uses r²).")], o="O2", d="H",
              reason=f"d = 2 × {d} = {2 * d} cm, so C = {2 * d}π ≈ {2 * d * 3.14159:.1f} cm.")


s.std([c1, c6, c2, c3, c4, c7, c9, c5, c8, c10, c11], EX("Explain why the circumference of a circle is a bit more than 3 times its diameter.", [("C = πd", ["πd|pi ?× ?d|π ?×"]), ("π is about 3.14, a bit more than 3", ["3\\.14|more than 3|about 3"])], "C = π × d and π ≈ 3.14, which is a bit more than 3. So the circumference is a bit more than 3 diameters.", o="O2"),
      deep=[d82])

# ================================================================== 8.3
s = U.section("8.3", "3D shapes", ["O3"])
s.idea("Faces, edges and vertices", ["A cuboid has 6 faces, 12 edges and 8 vertices. A triangular prism has 5 faces, 9 edges and 6 vertices. A square-based pyramid has 5 faces, 8 edges and 5 vertices.",
       "For these shapes, **faces + vertices − edges = 2** (Euler's rule)."], fig={"kind": "solid", "solid": "triprism"})
s.idea("Plans and elevations", ["A **plan** is the view from above. A **front elevation** is the view from the front and a **side elevation** is the view from the side.",
       "A cylinder's plan is a circle; its front elevation is a rectangle."])
s.check(N("How many edges does a cuboid have?", 12, o="O3"))
s.check(MC("Before you read on: a solid has 5 faces, 6 vertices and 9 edges. What could it be?", "A triangular prism", [("A square-based pyramid", "That has 5 vertices and 8 edges."), ("A cube", "A cube has 6 faces.")], o="O3"))
s.mistake("Count carefully", ["Hidden edges and faces still count. Use Euler's rule to check: F + V − E = 2."])
SOL = [("cube", 6, 12, 8), ("cuboid", 6, 12, 8), ("triangular prism", 5, 9, 6), ("square-based pyramid", 5, 8, 5), ("triangular pyramid", 4, 6, 4), ("pentagonal prism", 7, 15, 10), ("hexagonal prism", 8, 18, 12)]


def d1(r):
    n, F_, E_, V_ = pick(r, SOL); k = r.randrange(3)
    return N(f"How many {['faces', 'edges', 'vertices'][k]} does a {n} have?", [F_, E_, V_][k], o="O3", reason=f"A {n}: {F_} faces, {E_} edges, {V_} vertices.")
def d2(r):
    sols = r.sample(SOL, 3)
    return TB("Complete the table.", ["Shape", "Faces", "Edges", "Vertices"], [[n, B(F_), B(E_), B(V_)] for n, F_, E_, V_ in sols], o="O3", d="H")
def d3(r):
    rows = [("Cylinder", "Circle"), ("Cube", "Square"), ("Square-based pyramid", "Square with diagonals"), ("Cone", "Circle with a dot in the centre"), ("Triangular prism (lying on a rectangle)", "Rectangle")]
    return GD("What is the plan view (from above) of each solid standing on its base?", "Plan", r.sample(rows, 4), o="O3", d="H")
def d4(r):
    F_, V_ = pick(r, [(6, 8), (5, 6), (7, 10), (8, 12), (5, 5), (4, 4)])
    return N(f"A solid has {F_} faces and {V_} vertices. Use F + V − E = 2 to find the number of edges.", F_ + V_ - 2, o="O3", d="H", reason=f"E = F + V − 2 = {F_ + V_ - 2}.")
def d5(r):
    n = r.randint(5, 10)
    return N(f"A prism has a cross-section with {n} sides. How many faces does it have?", n + 2, o="O3", d="H", reason=f"{n} rectangles + 2 ends = {n + 2}.")
def d6(r):
    return MC("Which net folds to make a cube?", "a cross shape of 6 squares (4 in a column, one on each side of the second)", ["6 squares in a straight line", "5 squares in a cross", "a 2 × 3 rectangle of squares"], o="O3")
def d7(r):
    l, w, h = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    return N(f"A cuboid is {l} cm by {w} cm by {h} cm. What is the total length of all its edges?", 4 * (l + w + h), "cm", units=["cm"], o="O3", fig={"kind": "solid", "solid": "cuboid", "a": f"{l} cm", "b": f"{w} cm", "c": f"{h} cm"}, reason=f"4 × ({l} + {w} + {h}) = {4 * (l + w + h)} cm.")
def d8(r):
    n = r.randint(4, 9)
    return N(f"A pyramid has a base with {n} sides. How many vertices does it have?", n + 1, o="O3", reason=f"{n} on the base + 1 at the top = {n + 1}.")
def d9(r):
    rows = [("Cube", "Square"), ("Cylinder lying on its side", "Rectangle"), ("Cone standing on its base", "Triangle"), ("Sphere", "Circle")]
    return GD("What is the front elevation of each solid?", "Front elevation", r.sample(rows, 4), o="O3", extra=["Pentagon"])


def d10(r):
    n = r.randint(5, 12)
    return N(f"A prism has a cross-section with {n} sides. How many edges does it have?", 3 * n, o="O3", d="H", reason=f"{n} on each end + {n} along the length = {3 * n}.")
def d11(r):
    n = r.randint(5, 12)
    return N(f"A pyramid has a base with {n} sides. How many edges does it have?", 2 * n, o="O3", d="H", reason=f"{n} round the base + {n} up to the top = {2 * n}.")


def d83(r):
    F, V = pick(r, [(6, 8), (5, 6), (5, 5), (7, 10), (8, 12), (4, 4)])
    return N(f"A solid has {F} faces and {V} vertices. How many edges does it have?", F + V - 2, o="O3", d="H", reason=f"F + V − E = 2, so E = {F} + {V} − 2 = {F + V - 2}.")


s.std([d2, d7, d1, d3, d4, d5, d6, d8, d9, d10, d11], EX("Explain how Euler's rule can check that a triangular prism has 9 edges.", [("faces 5 and vertices 6", ["5.*6|6.*5|faces.*vertices"]), ("F + V − E = 2: 5 + 6 − 9 = 2", ["5 ?\\+ ?6|11 ?− ?9|11 ?- ?9|= ?2"])], "A triangular prism has 5 faces and 6 vertices. F + V − E = 5 + 6 − 9 = 2, which fits Euler's rule, so 9 edges is correct.", o="O3"),
      deep=[d83])

U.mindmap(("Quadrilaterals and polygons", "Sides, angles, diagonals, symmetry • regular n-gon: n lines, order n", "O1", "8.1"),
          ("Circumference", "C = πd = 2πr • π ≈ 3.14", "O2", "8.2"), ("3D shapes", "Faces, edges, vertices • F + V − E = 2 • plans and elevations", "O3", "8.3"))
