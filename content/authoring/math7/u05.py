# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 5 Angles and constructions (5.1 A sum of 360°, 5.2 Intersecting lines, 5.3 Drawing lines and
quadrilaterals). Written by the Atomic teaching team."""
from kit import *

U = Unit(5, "Angles and Constructions", "Geometry and measure",
         "Angles at a point, angles on a straight line, vertically opposite angles, angles in a triangle and quadrilateral, and accurate drawing of lines and quadrilaterals.",
         {"O1": {"code": "7Gg.01", "sec": "5.1", "codeNote": "", "t": "Know that angles at a point add up to 360° and use this to find missing angles."},
          "O2": {"code": "7Gg.02", "sec": "5.2", "codeNote": "", "t": "Recognise angles on a straight line, vertically opposite angles and the angles of a triangle, and find missing angles."},
          "O3": {"code": "7Gg.03", "sec": "5.3", "codeNote": "", "t": "Draw parallel and perpendicular lines and construct quadrilaterals accurately with a ruler and protractor."}})
TRI = lambda a, b, c: {"kind": "shape", "pts": [[0, 0], [8, 0], [3, 5]], "ang": [a, b, c]}

# ================================================================== 5.1
s = U.section("5.1", "A sum of 360°", ["O1"])
s.idea("Angles at a point", ["A full turn is **360°**. Angles that meet at a point and fill the full turn **add up to 360°**.",
       "The angles inside any **quadrilateral** also add up to 360° (it splits into two triangles of 180°)."], fig={"kind": "shape", "pts": [[0, 0], [7, 0], [8, 4], [1, 5]], "ang": ["75°", "105°", "80°", "100°"]})
s.example("Missing angle at a point", "Three angles at a point are 120°, 95° and x. Find x.", [("120 + 95 = 215", ""), ("360 − 215 = 145", "")], "x = 145°")
s.check(N("Angles at a point are 90°, 150° and x. Find x.", 120, "°", units=["°"], o="O1"))
s.mistake("180 or 360?", ["Angles on a straight line make 180°; angles all the way round a point make 360°."])


def p1(r):
    a, b = r.randint(40, 150), r.randint(40, 150)
    if a + b >= 340: return None
    return N(f"Three angles meet at a point. Two are {a}° and {b}°. Find the third.", 360 - a - b, "°", units=["°"], o="O1")
def p2(r):
    a, b, c = r.randint(60, 120), r.randint(60, 120), r.randint(60, 120); d = 360 - a - b - c
    if d <= 20: return None
    return N("Find the missing angle x in the quadrilateral.", d, "°", units=["°"], o="O1", fig={"kind": "shape", "pts": [[0, 0], [7, 0], [8, 4], [1, 5]], "ang": [f"{a}°", f"{b}°", f"{c}°", "x"]})
def p3(r):
    n = pick(r, [3, 4, 5, 6, 8, 9, 10, 12])
    return N(f"{n} equal angles meet at a point. How big is each angle?", 360 / n, "°", units=["°"], o="O1")
def p4(r):
    x = r.randint(30, 80); k = r.randint(2, 3)
    rest = 360 - (k + 1) * x
    if rest <= 0: return None
    return N(f"Angles at a point are x, {k}x and {rest}°. Find x.", x, "°", units=["°"], o="O1", d="H", reason=f"{k + 1}x + {rest} = 360 → x = {x}.")
def p5(r):
    a = r.randint(60, 120); b = r.randint(60, 120); c = 360 - a - b
    if not 40 < c < 200: return None
    return TB("Two angles of a kite-shaped quadrilateral are known. Complete the table.", ["Angle", "Size (°)"], [["Sum of all four angles", B(360)], ["Sum of the other two angles", B(c)]], o="O1", data={"head": ["Angle", "A", "B"], "rows": [["Size", f"{a}°", f"{b}°"]]})
def p6(r):
    t = pick(r, [90, 180, 270, 360, 45])
    names = {90: "a quarter turn", 180: "a half turn", 270: "three quarters of a turn", 360: "a full turn", 45: "an eighth of a turn"}
    return N(f"How many degrees are in {names[t]}?", t, "°", units=["°"], o="O1")
def p7(r):
    rows = [("Angles at a point", "360°"), ("Angles on a straight line", "180°"), ("Angles in a triangle", "180°"), ("Angles in a quadrilateral", "360°")]
    return GD("What do the angles add up to?", "Total", rows, o="O1", extra=["90°"])
def p8(r):
    a = r.randint(70, 120)
    return N(f"A quadrilateral has three equal angles of {a}°. Find the fourth angle.", 360 - 3 * a, "°", units=["°"], o="O1", d="H") if 360 - 3 * a > 0 else None


s.std([p2, p7, p1, p3, p4, p5, p6, p8], EX("Explain why the angles in a quadrilateral add up to 360°.", [("a diagonal splits it into two triangles", ["two triangles|2 triangles|diagonal"]), ("2 × 180° = 360°", ["2 ?× ?180|180 ?\\+ ?180|360"])], "A diagonal splits a quadrilateral into two triangles. The angles of each triangle add to 180°, so the total is 2 × 180° = 360°.", o="O1"))

# ================================================================== 5.2
s = U.section("5.2", "Intersecting lines", ["O2"])
s.idea("Straight lines", ["Angles on a **straight line** add up to **180°**.",
       "When two lines cross, the opposite angles are equal: these are **vertically opposite angles**.", "The angles in a **triangle** add up to **180°**."], fig=TRI("60°", "50°", "70°"))
s.check(N("Two angles on a straight line are 65° and x. Find x.", 115, "°", units=["°"], o="O2"))
s.check(N("A triangle has angles 40° and 75°. Find the third angle.", 65, "°", units=["°"], o="O2"))
s.mistake("Opposite, not next to", ["Vertically opposite angles are across the crossing point, not next to each other (those add to 180°)."])


def l1(r):
    a = r.randint(20, 160)
    return N(f"Two angles on a straight line are {a}° and x. Find x.", 180 - a, "°", units=["°"], o="O2")
def l2(r):
    a, b = r.randint(25, 90), r.randint(25, 90)
    return N("Find the missing angle in the triangle.", 180 - a - b, "°", units=["°"], o="O2", fig=TRI(f"{a}°", f"{b}°", "x"))
def l3(r):
    a = r.randint(25, 85)
    return N(f"Two straight lines cross. One angle is {a}°. Find the angle vertically opposite it.", a, "°", units=["°"], o="O2", fig={"kind": "parallel", "labels": {"a": f"{a}°", "c": "x"}})
def l4(r):
    a = r.randint(25, 85)
    return TB(f"Two straight lines cross. One angle is {a}°. Find the other three angles.", ["Angle", "Size (°)"], [["vertically opposite", B(a)], ["next to it (one side)", B(180 - a)], ["next to it (other side)", B(180 - a)]], o="O2", d="H")
def l5(r):
    a = r.randint(30, 80)
    return N(f"An isosceles triangle has two equal angles of {a}°. Find the third angle.", 180 - 2 * a, "°", units=["°"], o="O2", fig=TRI(f"{a}°", f"{a}°", "x"))
def l6(r):
    a = r.randint(20, 160); b = r.randint(10, 170 - a)
    return N(f"Three angles on a straight line are {a}°, {b}° and x. Find x.", 180 - a - b, "°", units=["°"], o="O2") if 180 - a - b > 0 else None
def l7(r):
    a = r.randint(30, 70)
    return N(f"A right-angled triangle has one angle of {a}°. Find the other acute angle.", 90 - a, "°", units=["°"], o="O2", fig={"kind": "shape", "pts": [[0, 0], [7, 0], [0, 5]], "ang": ["", f"{a}°", "x"], "right": [0]})
def l8(r):
    x = r.randint(20, 50)
    return N(f"The angles of a triangle are x, 2x and {180 - 3 * x}°. Find x.", x, "°", units=["°"], o="O2", d="H")
def l9(r):
    a = r.randint(40, 80)
    return MC("Why are the angles in an equilateral triangle each 60°?", "they are equal and add to 180°", ["they are all right angles", "a full turn is 360°", "the sides are 60 cm"], o="O2")


s.std([l2, l4, l1, l3, l5, l6, l7, l8, l9], EX("Explain why vertically opposite angles are equal.", [("each makes 180° with the same angle between them", ["180|straight line"]), ("so they must be the same size", ["same|equal"])], "Each of the two opposite angles lies on a straight line with the same angle between them, so each equals 180° minus that angle. So they are equal.", o="O2"))

# ================================================================== 5.3
s = U.section("5.3", "Drawing lines and quadrilaterals", ["O3"])
s.idea("Parallel and perpendicular", ["**Parallel** lines stay the same distance apart and never meet (marked with arrows). **Perpendicular** lines meet at a **right angle** (90°).",
       "To draw a quadrilateral accurately, use a ruler for lengths (to the nearest mm) and a protractor for angles (to the nearest degree)."], fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]], "s": ["8 cm", "4 cm", "", ""], "right": [0, 1, 2, 3]})
s.check(MC("Which angle do perpendicular lines make?", "90°", ["180°", "45°", "60°"], o="O3"))
s.mistake("Read the right scale", ["A protractor has two scales. Start from 0° on the line you are measuring from."])


def c1(r):
    rows = [("Square", "4 right angles, 4 equal sides"), ("Rectangle", "4 right angles, opposite sides equal"), ("Rhombus", "4 equal sides, no right angles"), ("Parallelogram", "opposite sides equal and parallel"), ("Trapezium", "one pair of parallel sides"), ("Kite", "two pairs of equal adjacent sides")]
    return GD("Match each shape to its description.", "Description", r.sample(rows, 4), o="O3")
def c2(r):
    return MC(pick(r, ["Which shape has exactly one pair of parallel sides?", "Which quadrilateral has only one pair of parallel sides?"]), "trapezium", ["rectangle", "rhombus", "parallelogram"], o="O3")
def c3(r):
    l = r.randint(30, 120)
    return N(f"A line is {l} mm long. How long is it in centimetres?", l / 10, "cm", units=["cm"], o="O3")
def c4(r):
    a = r.randint(55, 85)
    return N(f"A parallelogram has an angle of {a}°. What is the size of the angle next to it?", 180 - a, "°", units=["°"], o="O3", fig={"kind": "shape", "pts": [[0, 0], [7, 0], [9, 4], [2, 4]], "ang": [f"{a}°", "?", "", ""]})
def c5(r):
    rows = [("A rectangle", "Yes"), ("A kite", "No"), ("A square", "Yes"), ("A rhombus (not a square)", "No")]
    return GD("Do the sides meet at right angles (perpendicular)?", "Right angles?", rows, o="O3")
def c6(r):
    l, w = r.randint(3, 12), r.randint(2, 9)
    return N(f"A student draws a rectangle {l} cm by {w} cm. What is its perimeter?", 2 * (l + w), "cm", units=["cm"], o="O3", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": [f"{l} cm", f"{w} cm", "", ""], "right": [0, 1, 2, 3]})
def c7(r):
    steps = ["Draw the base with a ruler", "Measure the angle at one end with a protractor", "Draw the second side to the right length", "Complete the shape and check the last side and angle"]
    return OD("Put the steps for drawing a quadrilateral in order.", steps, o="O3")
def c8(r):
    a = r.randint(60, 120)
    return N(f"A kite has angles of {a}°, {a}°, 70° and x. Find x.", 290 - 2 * a, "°", units=["°"], o="O3", d="H") if 290 - 2 * a > 0 else None


s.std([c1, c4, c2, c3, c5, c6, c7, c8], EX("Explain the difference between parallel and perpendicular lines.", [("parallel lines never meet / stay the same distance apart", ["never meet|same distance|don't meet|do not meet"]), ("perpendicular lines meet at a right angle", ["right angle|90"])], "Parallel lines stay the same distance apart and never meet. Perpendicular lines meet (or cross) at a right angle, 90°.", o="O3"))

U.mindmap(("360°", "Angles at a point • quadrilateral", "O1", "5.1"), ("180°", "Straight line • triangle • vertically opposite are equal", "O2", "5.2"),
          ("Drawing", "Parallel • perpendicular • ruler and protractor", "O3", "5.3"))
