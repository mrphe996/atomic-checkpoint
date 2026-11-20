# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 5 Angles. Written by the Atomic teaching team."""
import math
from kit import *

U = Unit(5, "Angles", "Geometry",
         "Angles with parallel lines and in triangles, interior and exterior angles of polygons, ruler-and-compass constructions and Pythagoras' theorem.",
         {"O1": {"sec": "5.1", "code": "9Gg.07", "codeNote": "", "t": "Calculate angles using angle facts: angles on a line, around a point, in a triangle, and alternate, corresponding and co-interior angles."},
          "O2": {"sec": "5.2", "code": "9Gg.08", "codeNote": "", "t": "Derive and use the sum of the interior angles of a polygon."},
          "O3": {"sec": "5.3", "code": "9Gg.08", "codeNote": "exterior", "t": "Use the sum of exterior angles of a polygon (360°) to find angles and the number of sides of regular polygons."},
          "O4": {"sec": "5.4", "code": "9Gg.11", "codeNote": "", "t": "Describe and use ruler-and-compass constructions: perpendicular bisector, angle bisector and the perpendicular from a point to a line."},
          "O5": {"sec": "5.5", "code": "9Gg.12", "codeNote": "", "t": "Use Pythagoras' theorem to find a missing side of a right-angled triangle and solve problems."}})

# ================================================================== 5.1
s = U.section("5.1", "Calculating angles", ["O1"])
s.idea("Angle facts", ["Angles on a straight line add to **180°**; angles around a point add to **360°**; angles in a triangle add to **180°**.",
       "With **parallel lines**: **alternate** angles (Z shape) are equal, **corresponding** angles (F shape) are equal, **co-interior** angles (C shape) add to 180°."],
       fig={"kind": "parallel", "labels": {"b": "a", "e": "a", "c": "c", "g": "c"}})
s.example("Parallel lines", "Two parallel lines are cut by a transversal. One angle is 65°. Find the alternate angle and the co-interior angle.", [("alternate angle = 65°", "Z shape: equal"), ("co-interior = 180° − 65° = 115°", "C shape: add to 180°")], "65° and 115°", fig={"kind": "parallel", "labels": {"c": "65°", "e": "a", "h": "b"}})
s.check(N("Angles on a straight line are 3x and 2x + 30. Find x.", 30, o="O1", reason="5x + 30 = 180 → x = 30."))
s.example("Exterior angle of a triangle", "A triangle has angles 48° and 67°. Find the exterior angle at the third vertex.", [("third angle = 180 − 48 − 67 = 65°", ""), ("exterior = 180 − 65 = 115°", "it equals 48 + 67")], "115°")
s.mistake("Give reasons", ["In geometry, write the reason with each step, e.g. 'alternate angles are equal'. Marks are given for reasons."])
s.check(MC("Which pair of angles add to 180°?", "co-interior angles", [("alternate angles", "These are equal."), ("corresponding angles", "These are equal."), ("vertically opposite angles", "These are equal.")], o="O1"))
def a1(r):
    a = r.randint(25, 155)
    k = pick(r, [("alternate", a, "alternate angles are equal"), ("corresponding", a, "corresponding angles are equal"), ("co-interior", 180 - a, "co-interior angles add to 180°")])
    lab = {"alternate": {"c": f"{a}°", "e": "x"}, "corresponding": {"b": f"{a}°", "f": "x"}, "co-interior": {"c": f"{a}°", "f": "x"}}[k[0]]
    return N(f"The lines are parallel. Find x.", k[1], "°", units=["°"], o="O1", fig={"kind": "parallel", "labels": lab}, reason=f"{k[2]}: x = {k[1]}°.")
def a2(r):
    a, b = r.randint(20, 90), r.randint(20, 80)
    if a + b >= 170: return None
    return N(f"Two angles of a triangle are {a}° and {b}°. Find the exterior angle at the third vertex.", a + b, "°", units=["°"], o="O1", reason=f"Exterior angle = sum of the two opposite interior angles = {a+b}°.", fig={"kind": "shape", "pts": [[0, 0], [7, 0], [2, 4]], "ang": [f"{a}°", "", f"{b}°"]})
def a3(r):
    k = r.randint(2, 5); c = r.randint(5, 40); x = r.randint(10, 40)
    if k * x + c + x >= 180: return None
    return N(f"Angles on a straight line are {k}x + {c}° and {180 - k*x - c}°. Find x.", x, o="O1")
def a4(r):
    p = [r.randint(40, 110) for _ in range(3)]
    if sum(p) >= 340: return None
    return N(f"Four angles around a point are {p[0]}°, {p[1]}°, {p[2]}° and x. Find x.", 360 - sum(p), "°", units=["°"], o="O1")
def a5(r):
    b = r.randint(30, 80)
    return N(f"An isosceles triangle has a base angle of {b}°. Find the angle at the top (apex).", 180 - 2 * b, "°", units=["°"], o="O1", fig={"kind": "shape", "pts": [[0, 0], [6, 0], [3, 4]], "ang": [f"{b}°", "", "x"], "ticks": [0, 1, 1]})
def a6(r):
    x = r.randint(15, 40)
    return N(f"The angles of a triangle are x, 2x and {180 - 3*x}°. Find x.", x, o="O1")
def a7(r):
    rows = [("Z shape", "Alternate – equal"), ("F shape", "Corresponding – equal"), ("C shape", "Co-interior – add to 180°")]
    return MT("Match each shape with the angle fact.", rows, o="O1")
def a8(r):
    a = r.randint(30, 80); b = r.randint(30, 80)
    return N(f"In triangle ABC, angle A = {a}°, angle B = {b}°. The side BC is extended to D. Find angle ACD.", a + b, "°", units=["°"], o="O1", d="H")
s.core(a1(s.rng), a1(s.rng), a2(s.rng) or a5(s.rng), a4(s.rng) or a6(s.rng), a5(s.rng), a6(s.rng), a7(s.rng),
       EX("Prove that the exterior angle of a triangle equals the sum of the two opposite interior angles.", [("a + b + c = 180 (triangle)", ["triangle|180"]), ("exterior + c = 180 (straight line)", ["straight line|line"]), ("so exterior = a + b", ["= ?a ?\\+ ?b|sum of|equal"])], "The angles of a triangle add to 180°, so a + b + c = 180°. The exterior angle and c lie on a straight line, so exterior + c = 180°. Therefore exterior = a + b.", o="O1", d="VH"))
s.gen("p", 44, a1, a2, a3, a4, a5, a6, a7, a8)
s.gen("a", 8, lambda r: (lambda a: N(f"In the diagram the lines are parallel; one angle is {a}° and x is co-interior to the angle vertically opposite it. Find x.", 180 - a, "°", units=["°"], o="O1", d="VH", fig={"kind": "parallel", "labels": {"a": f"{a}°", "f": "x"}}))(r.randint(40, 140)),
      lambda r: (lambda x: N(f"The angles of a quadrilateral are x, 2x, 3x − 20 and x + 30. Find x.", x, o="O1", d="VH"))(50))

# ================================================================== 5.2
s = U.section("5.2", "Interior angles of polygons", ["O2"])
s.idea("Sum of interior angles", ["A polygon with n sides can be split into **(n − 2) triangles** from one vertex, so the interior angles add to **(n − 2) × 180°**.",
       "A **regular** polygon has equal angles, so each interior angle is **(n − 2) × 180° ÷ n**."], table={"caption": "Angle sums", "head": ["Sides", "3", "4", "5", "6", "8", "10"], "rows": [["Sum of angles", "180°", "360°", "540°", "720°", "1080°", "1440°"]]})
s.example("Regular polygon", "Find the size of each interior angle of a regular octagon.", [("(8 − 2) × 180 = 1080°", ""), ("1080 ÷ 8 = 135°", "")], "135°")
s.check(N("Find the sum of the interior angles of a hexagon.", 720, "°", units=["°"], o="O2"))
s.example("Missing angle", "A pentagon has angles 110°, 95°, 120°, 100° and x. Find x.", [("sum = 540°", ""), ("x = 540 − 425 = 115°", "")], "115°", fig={"kind": "shape", "pts": [[0, 0], [5, 0], [6.5, 3], [2, 4.5], [-1, 2.5]], "ang": ["110°", "x", "95°", "120°", "100°"]})
s.mistake("Use n − 2", ["The number of triangles is n − 2, not n. A hexagon has 6 − 2 = 4 triangles, so its angle sum is 720°."])
s.check(MC("How many triangles can a decagon be split into from one vertex?", "8", [("10", "It is n − 2."), ("9", ""), ("12", "")], o="O2"))
NAMES = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon", 10: "decagon", 12: "dodecagon"}
def p1(r):
    n = pick(r, list(NAMES) + [15, 18, 20])
    return N(f"Find the sum of the interior angles of a {NAMES.get(n, f'{n}-sided polygon')}.", (n - 2) * 180, "°", units=["°"], o="O2")
def p2(r):
    n = pick(r, [5, 6, 8, 9, 10, 12, 15, 18, 20])
    return N(f"Find each interior angle of a regular {NAMES.get(n, f'{n}-sided polygon')}.", (n - 2) * 180 / n, "°", units=["°"], o="O2", d="H")
def p3(r):
    n = pick(r, [5, 6, 7]); tot = (n - 2) * 180; angs = [r.randint(90, 160) for _ in range(n - 1)]; x = tot - sum(angs)
    if not 40 < x < 179: return None
    import math as m
    pts = [[3 * m.cos(2 * m.pi * i / n), 3 * m.sin(2 * m.pi * i / n)] for i in range(n)]
    return N(f"Find x in this {NAMES[n]}.", x, "°", units=["°"], o="O2", fig={"kind": "shape", "pts": pts, "ang": [f"{a}°" for a in angs] + ["x"]})
def p4(r):
    n = pick(r, [5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 36]); ang = (n - 2) * 180 / n
    if ang != int(ang): return None
    return N(f"Each interior angle of a regular polygon is {int(ang)}°. How many sides does it have?", n, "sides", units=["sides"], o="O2", d="H")
def p5(r):
    s_ = pick(r, [540, 720, 900, 1080, 1260, 1440, 1800])
    return N(f"The interior angles of a polygon add to {s_}°. How many sides does it have?", s_ // 180 + 2, "sides", units=["sides"], o="O2")
def p6(r):
    return TB("Complete the table.", ["Polygon", "Sides", "Sum of interior angles", "Each angle if regular"], [["Pentagon", "5", B(540), B(108)], ["Hexagon", "6", B(720), B(120)], ["Decagon", "10", B(1440), B(144)]], o="O2")
def p7(r):
    x = r.randint(20, 40)
    return N(f"The angles of a pentagon are x, 2x, 3x, 4x and 5x... no: x + 60, 2x, 2x, 3x − 20 and 100°. Find x." if False else f"The angles of a hexagon are 2x, 2x, 3x, 3x, 4x and 4x. Find x.", 40, o="O2", d="H")
def p8(r):
    return MC("Can a regular polygon have an interior angle of 130°?", "No – the number of sides would not be a whole number", [("Yes – a 13-sided polygon", "Each angle of a 13-gon is about 152°."), ("Yes – any angle is possible", ""), ("No – angles must be less than 120°", "")], o="O2", d="VH", reason="Exterior = 50°; 360 ÷ 50 = 7.2, not whole.")
s.core(p1(s.rng), p2(s.rng), p3(s.rng) or p3(s.rng) or p1(s.rng), p4(s.rng) or p5(s.rng), p5(s.rng), p6(s.rng), p8(s.rng),
       EX("Explain why the interior angles of a quadrilateral add to 360°.", [("split into two triangles", ["two triangles|2 triangles|diagonal"]), ("2 × 180 = 360", ["2 ?(×|x) ?180|180 ?\\+ ?180"])], "A diagonal splits a quadrilateral into two triangles. Each triangle's angles add to 180°, so the total is 2 × 180° = 360°.", o="O2"))
s.gen("p", 44, p1, p2, p3, p4, p5, p6, p7)
s.gen("a", 8, p8, p4, p2, lambda r: (lambda n: N(f"A polygon has {n} sides. All but one of its interior angles are 150°. Find the remaining angle.", (n - 2) * 180 - 150 * (n - 1), "°", units=["°"], o="O2", d="VH"))(r.randint(8, 11)))

# ================================================================== 5.3
s = U.section("5.3", "Exterior angles of polygons", ["O3"])
s.idea("Exterior angles", ["The **exterior angles** of any polygon add to **360°** (walk round the shape and you turn through one full turn).",
       "For a regular polygon with n sides: **each exterior angle = 360° ÷ n**, and **interior + exterior = 180°**."])
s.example("Number of sides", "Each exterior angle of a regular polygon is 24°. How many sides does it have?", [("n = 360 ÷ 24", ""), ("n = 15", "")], "15 sides")
s.check(N("Find each exterior angle of a regular dodecagon (12 sides).", 30, "°", units=["°"], o="O3"))
s.example("From interior to exterior", "Each interior angle of a regular polygon is 156°. Find n.", [("exterior = 180 − 156 = 24°", ""), ("n = 360 ÷ 24 = 15", "")], "15")
s.mistake("Which angle?", ["Divide 360 by the number of sides to get the EXTERIOR angle, not the interior one."])
s.check(MC("Each exterior angle of a regular polygon is 40°. What is each interior angle?", "140°", [("40°", ""), ("320°", ""), ("9°", "That is the number of sides.")], o="O3"))
def x1(r):
    n = pick(r, [5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45])
    return N(f"Find each exterior angle of a regular polygon with {n} sides.", 360 / n, "°", units=["°"], o="O3")
def x2(r):
    n = pick(r, [5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45])
    return N(f"Each exterior angle of a regular polygon is {fmt(360/n)}°. How many sides does it have?", n, "sides", units=["sides"], o="O3", data={"head": ["Exterior angle", "Number of sides"], "rows": [[f"{fmt(360/n)}°", "?"]]})
def x3(r):
    n = pick(r, [6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36])
    return N(f"Each interior angle of a regular polygon is {fmt(180-360/n)}°. How many sides does it have?", n, "sides", units=["sides"], o="O3", d="H")
def x4(r):
    a = [r.randint(50, 100) for _ in range(4)]
    if sum(a) >= 345: return None
    return N(f"Four of the exterior angles of a pentagon are {a[0]}°, {a[1]}°, {a[2]}° and {a[3]}°. Find the fifth.", 360 - sum(a), "°", units=["°"], o="O3")
def x5(r):
    return TB("Complete the table for regular polygons.", ["Sides", "Exterior angle", "Interior angle"], [["5", B(72), B(108)], [B(9), "40", B(140)], ["18", B(20), B(160)]], o="O3")
def x6(r):
    k = pick(r, [2, 3, 4, 5, 7, 8, 11])
    return N(f"In a regular polygon each interior angle is {k} times each exterior angle. How many sides does it have?", 2 * (k + 1), "sides", units=["sides"], o="O3", d="VH", reason=f"e + {k}e = 180 → e = {180/(k+1):.2f}; n = 360 ÷ e = {2*(k+1)}.")
def x7(r):
    a = pick(r, [7, 11, 13, 17, 25, 50])
    return MC(f"Can a regular polygon have an exterior angle of {a}°?", "No, because 360 is not divisible by " + str(a), [("Yes", f"360 ÷ {a} is not a whole number."), ("Only if it is a triangle", "")], o="O3", d="H")
s.core(x1(s.rng), x2(s.rng), x3(s.rng), x4(s.rng) or x1(s.rng), x5(s.rng), x6(s.rng), x7(s.rng),
       EX("Explain why the exterior angles of a polygon add to 360°.", [("walking round the shape you turn at each corner", ["walk|turn|go round|around"]), ("you make one full turn = 360°", ["full turn|one turn|complete turn|360"])], "If you walk round the edge of the polygon you turn through the exterior angle at each corner. When you get back to the start you have made one full turn, which is 360°.", o="O3", d="H"))
s.gen("p", 44, x1, x2, x3, x4, x5, x6, x7)
s.gen("a", 8, x6, lambda r: (lambda n: N(f"Two regular polygons: A has {n} sides and B has {2*n} sides. How many degrees larger is each interior angle of B than of A?", 180 / n, "°", units=["°"], o="O3", d="VH"))(pick(r, [5, 6, 9, 10, 12])))

# ================================================================== 5.4
s = U.section("5.4", "Constructions", ["O4"])
s.idea("Ruler-and-compass constructions", ["A **perpendicular bisector** cuts a line segment in half at 90°. Every point on it is the **same distance from both ends**.",
       "An **angle bisector** cuts an angle in half. Every point on it is the same distance from both arms of the angle.",
       "Keep your compass arcs: they show your method."])
s.method("Perpendicular bisector of AB", ["Use a compass width more than half of AB."], steps=[("Arc from A above and below AB", ""), ("Same width: arc from B crossing the first arcs", ""), ("Join the two crossing points", "this line is the perpendicular bisector")])
s.check(MC("A point P is on the perpendicular bisector of AB. Which is true?", "PA = PB", [("PA = AB", ""), ("P is the midpoint of AB", "Only one point of the bisector is the midpoint."), ("angle APB = 90°", "")], o="O4"))
s.method("Angle bisector", ["Bisect angle ABC."], steps=[("Arc from B cutting both arms", "points P and Q"), ("Equal arcs from P and from Q that cross", ""), ("Join B to the crossing point", "")])
s.mistake("Change the compass width", ["Do not change the compass width between the two arcs from the ends of the line – the arcs must be the same size."])
s.check(OD("Put the steps for the angle bisector in order.", ["Draw an arc from the vertex to cut both arms", "From each cut, draw equal arcs that cross", "Join the vertex to the crossing point"], o="O4", skill="Data"))
def c1(r):
    L = r.randint(4, 15)
    return N(f"AB is {L} cm long. The perpendicular bisector meets AB at M. Find AM.", L / 2, "cm", units=["cm"], o="O4")
def c2(r):
    a = r.randint(30, 160)
    return N(f"An angle of {a}° is bisected. Find the size of each new angle.", a / 2, "°", units=["°"], o="O4")
def c3(r):
    rows = [("Points the same distance from A and B", "Perpendicular bisector of AB"), ("Points the same distance from two lines that meet", "Angle bisector"), ("Shortest distance from a point to a line", "Perpendicular from the point")]
    return MT("Match each description with the construction.", rows, o="O4", skill="Data")
def c4(r):
    return MC("Which construction makes an angle of 60°?", "an equilateral triangle using the same compass width", [("bisecting a straight line", "That gives 90°."), ("bisecting a right angle", "That gives 45°."), ("drawing a perpendicular", "")], o="O4", d="H")
def c5(r):
    return MC("Which angle can be made by bisecting a 60° angle and then bisecting again?", "15°", [("30°", "That is after one bisection."), ("20°", ""), ("45°", "")], o="O4", d="H")
def c6(r):
    d = r.randint(3, 9)
    return MC(f"A goat is tied to a post with a rope {d} m long. Which shape is the region it can reach?", f"a circle of radius {d} m", [(f"a square of side {d} m", ""), (f"a circle of diameter {d} m", "The rope is the radius."), ("a straight line", "")], o="O4")
def c7(r):
    return TK("Which statements about a perpendicular bisector of AB are true?", ["True", "False"], [("It passes through the midpoint of AB", ["✓", "✗"]), ("It makes an angle of 90° with AB", ["✓", "✗"]), ("It is always horizontal", ["✗", "✓"]), ("Every point on it is equidistant from A and B", ["✓", "✗"])], o="O4")
s.core(c1(s.rng), c2(s.rng), c3(s.rng), c4(s.rng), c5(s.rng), c6(s.rng), c7(s.rng),
       EX("Explain why the perpendicular bisector construction needs a compass width of more than half of AB.", [("arcs would not meet / cross", ["meet|cross|intersect|touch"]), ("they need to overlap to give two points", ["overlap|two points|both sides"])], "If the width were half of AB or less, the arcs from A and B would not cross, so there would be no points to join.", o="O4", d="H"))
s.gen("p", 44, c1, c2, c3, c4, c5, c6, c7)
s.gen("a", 8, lambda r: (lambda a: N(f"An angle of {a}° is bisected, then one half is bisected again, then again. Find the smallest angle.", a / 8, "°", units=["°"], o="O4", d="VH"))(r.randint(30, 170)), lambda r: MC("A treasure is the same distance from two trees A and B and 5 m from tree C. How many places could it be?", "at most 2 – where the bisector of AB meets a circle round C", [("exactly 1", ""), ("infinitely many", ""), ("none", "")], o="O4", d="VH"),
      lambda r: (lambda d: N(f"A and B are {2*d} m apart. Points on the perpendicular bisector of AB that are {d+1} m from A are how far from the midpoint M of AB? Give the answer to 2 d.p.", round(math.sqrt((d + 1) ** 2 - d * d), 2), "m", units=["m"], tol=0.006, o="O4", d="VH"))(r.randint(3, 9)))

# ================================================================== 5.5
s = U.section("5.5", "Pythagoras' theorem", ["O5"])
s.idea("Pythagoras' theorem", ["In a right-angled triangle the longest side, opposite the right angle, is the **hypotenuse** c. **a² + b² = c²**.",
       "To find the hypotenuse: **add** the squares, then square-root. To find a shorter side: **subtract** the squares, then square-root."],
       fig={"kind": "shape", "pts": [[0, 0], [4, 0], [0, 3]], "s": ["a", "c", "b"], "right": [0]})
s.example("Hypotenuse", "Find the hypotenuse when the shorter sides are 9 cm and 12 cm.", [("c² = 9² + 12² = 81 + 144 = 225", ""), ("c = √225 = 15", "")], "15 cm")
s.check(N("The two shorter sides of a right-angled triangle are 5 cm and 12 cm. Find the hypotenuse.", 13, "cm", units=["cm", "cm²"], o="O5"))
s.example("Shorter side", "The hypotenuse is 17 cm and one side is 8 cm. Find the other side.", [("b² = 17² − 8² = 289 − 64 = 225", "subtract"), ("b = 15", "")], "15 cm")
s.mistake("Subtract for a shorter side", ["If the side you want is NOT the hypotenuse, subtract the squares. The hypotenuse must be the longest side."])
s.check(MC("Is a triangle with sides 6, 8 and 11 cm right-angled?", "No, because 6² + 8² = 100 and 11² = 121", [("Yes, because 6 + 8 > 11", ""), ("Yes, because 11 is the longest side", ""), ("No, because it has no 90° label", "")], o="O5", d="H"))
TRIP = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10), (9, 12, 15), (20, 21, 29), (9, 40, 41)]
def h1(r):
    a, b = r.randint(2, 20), r.randint(2, 20); c = math.hypot(a, b)
    return N(f"Find the hypotenuse of a right-angled triangle with shorter sides {a} cm and {b} cm. Give your answer to 1 decimal place.", round(c, 1), "cm", units=["cm", "cm²"], tol=0.05, o="O5", fig={"kind": "shape", "pts": [[0, 0], [a, 0], [0, b]], "s": [f"{a} cm", "x", f"{b} cm"], "right": [0]})
def h2(r):
    c = r.randint(10, 30); a = r.randint(3, c - 2); b = math.sqrt(c * c - a * a)
    return N(f"The hypotenuse of a right-angled triangle is {c} cm and one side is {a} cm. Find the other side to 1 decimal place.", round(b, 1), "cm", units=["cm", "cm²"], tol=0.05, o="O5", d="H", fig={"kind": "shape", "pts": [[0, 0], [b, 0], [0, a]], "s": ["x", f"{c} cm", f"{a} cm"], "right": [0]})
def h3(r):
    a, b, c = pick(r, TRIP); k = r.randint(1, 3)
    return N(f"A ladder {c*k} m long leans against a wall. Its foot is {a*k} m from the wall. How high up the wall does it reach?", b * k, "m", units=["m"], o="O5")
def h4(r):
    a, b = r.randint(10, 60), r.randint(10, 60)
    return N(f"Find the length of the diagonal of a rectangle {a} cm by {b} cm, to 1 d.p.", round(math.hypot(a, b), 1), "cm", units=["cm"], tol=0.05, o="O5")
def h5(r):
    x1, y1, x2, y2 = [r.randint(-6, 8) for _ in range(4)]
    if x1 == x2 or y1 == y2: return None
    return N(f"Find the distance between ({x1}, {y1}) and ({x2}, {y2}), to 2 d.p.", round(math.hypot(x2 - x1, y2 - y1), 2), tol=0.006, o="O5", d="H", fig={"kind": "coord", "x": [-7, 9], "y": [-7, 9], "points": [{"x": x1, "y": y1, "l": "A"}, {"x": x2, "y": y2, "l": "B"}], "segs": [[x1, y1, x2, y2]]})
def h6(r):
    t = pick(r, TRIP + [(4, 5, 6), (5, 6, 8), (7, 8, 11), (2, 3, 4)]); right = t[0] ** 2 + t[1] ** 2 == t[2] ** 2
    return MC(f"Is a triangle with sides {t[0]}, {t[1]} and {t[2]} right-angled?", "Yes" if right else "No", [("No" if right else "Yes", f"{t[0]}² + {t[1]}² = {t[0]**2 + t[1]**2} and {t[2]}² = {t[2]**2}.")], o="O5", d="H")
def h7(r):
    a = r.randint(4, 15)
    return N(f"An isosceles triangle has two sides of {a + 3} cm and a base of {2*a} cm... find its height to 2 d.p." if False else f"An isosceles triangle has equal sides of {a+5} cm and a base of {2*a} cm. Find its height, to 2 d.p.", round(math.sqrt((a + 5) ** 2 - a * a), 2), "cm", units=["cm"], tol=0.006, o="O5", d="H")
def h8(r):
    return TB("Complete the table for right-angled triangles (c is the hypotenuse).", ["a", "b", "c"], [["9", "40", B(41)], ["20", B(21), "29"], [B(12), "35", "37"]], o="O5")
s.core(h1(s.rng), h2(s.rng), h3(s.rng), h4(s.rng), h5(s.rng) or h4(s.rng), h6(s.rng), h8(s.rng),
       EX("Kai finds a side of a right-angled triangle with hypotenuse 10 cm and side 6 cm. He gets √136. Explain his mistake.", [("he added the squares", ["add|added|\\+"]), ("should subtract: 100 − 36 = 64", ["subtract|100 ?- ?36|64"]), ("answer 8 cm", ["\\b8\\b"])], "He added 10² + 6². For a shorter side you subtract: 10² − 6² = 64, so the side is √64 = 8 cm.", o="O5", d="H"))
s.gen("p", 44, h1, h2, h3, h4, h5, h6, h7, h8)
s.gen("a", 8, lambda r: (lambda a: N(f"Find the length of the space diagonal of a cube of side {a} cm, to 2 d.p.", round(a * math.sqrt(3), 2), "cm", units=["cm"], tol=0.006, o="O5", d="VH"))(r.randint(2, 12)),
      lambda r: (lambda e, w: N(f"A ship sails {e} km east then {w} km north. How far is it from its start, to 1 d.p.?", round(math.hypot(e, w), 1), "km", units=["km"], tol=0.05, o="O5", d="VH"))(r.randint(5, 40), r.randint(5, 40)))

U.mindmap(("Angle facts", "Line 180° • point 360° • triangle 180°", "O1", "5.1"), ("Parallel lines", "Alternate and corresponding equal • co-interior 180°", "O1", "5.1"),
          ("Interior angles", "(n − 2) × 180°", "O2", "5.2"), ("Exterior angles", "Add to 360° • regular: 360 ÷ n", "O3", "5.3"),
          ("Constructions", "Perpendicular bisector • angle bisector", "O4", "5.4"), ("Pythagoras", "a² + b² = c²", "O5", "5.5"))
