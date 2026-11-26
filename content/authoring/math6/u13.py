# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 13 Angles (13.1 Measuring and drawing angles, 13.2 Angles in a triangle).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(13, "Angles", "Geometry and measure",
         "Classifying, estimating, measuring and drawing angles, angles on a straight line and around a point, and the angles in a triangle.",
         {"O1": {"code": "6Gg.07", "sec": "13.1", "codeNote": "", "t": "Classify, estimate, measure and draw angles, and use angles on a straight line and around a point."},
          "O2": {"code": "6Gg.08", "sec": "13.2", "codeNote": "", "t": "Know that the angles in a triangle add up to 180° and use this to find missing angles."}})
KIND = lambda a: "acute" if a < 90 else "right angle" if a == 90 else "obtuse" if a < 180 else "straight" if a == 180 else "reflex"
TRI = lambda a, b, c: {"kind": "shape", "pts": [[0, 0], [9, 0], [3, 5]], "ang": [a, b, c]}

s = U.section("13.1", "Measuring and drawing angles", ["O1"])
s.idea("Types of angle", ["An **acute** angle is less than 90°. A **right angle** is exactly 90°. An **obtuse** angle is between 90° and 180°. A **reflex** angle is more than 180°.",
       "Use a **protractor** to measure angles: put the centre on the vertex and line up 0° with one arm."], fig={"kind": "anglept", "line": True, "angles": [72, 108]})
s.check(MC("What type of angle is 135°?", "obtuse", [("acute", ""), ("reflex", ""), ("right angle", "")], o="O1"))
s.idea("Angles on a line and at a point", ["Angles on a **straight line** add up to **180°**. Angles all the way round a **point** add up to **360°**."])
s.check(MC("Before you read on: an angle measures 130°. What type is it?", "Obtuse", [("Acute", "Acute angles are less than 90°."), ("Reflex", "Reflex angles are more than 180°.")], o="O1"))
s.mistake("Which scale?", ["A protractor has two scales. Start from the 0° that lines up with the arm."])


def a1(r):
    a = r.randint(5, 355)
    if a in (90, 180): return None
    return MC(f"What type of angle is {a}°?", KIND(a), [x for x in ["acute", "obtuse", "reflex", "right angle"] if x != KIND(a)][:3], o="O1")
def a2(r):
    a = r.randint(20, 160)
    return N("Find the missing angle x on the straight line.", 180 - a, "°", units=["°"], o="O1", fig={"kind": "anglept", "line": True, "angles": [a, 180 - a], "labels": [f"{a}°", "x"]})
def a3(r):
    a, b = r.randint(60, 150), r.randint(60, 150)
    return N("Three angles meet at a point. Find x.", 360 - a - b, "°", units=["°"], o="O1", fig={"kind": "anglept", "angles": [a, b, 360 - a - b], "labels": [f"{a}°", f"{b}°", "x"], "start": 20})
def a4(r):
    ang = r.sample([20, 45, 75, 90, 110, 160, 200, 300], 4)
    return GD("Classify each angle.", "Type", [(f"{a}°", KIND(a)) for a in ang], o="O1", extra=["acute", "right angle", "obtuse", "reflex"])
def a6(r):
    a = r.randint(20, 70)
    return N(f"Two angles make a right angle. One is {a}°. Find the other.", 90 - a, "°", units=["°"], o="O1")
def a7(r):
    n = pick(r, [3, 4, 5, 6, 8, 9, 10])
    return N(f"{n} equal angles fit round a point. How big is each one?", 360 / n, "°", units=["°"], o="O1", d="H")
def a8(r):
    h = r.randint(1, 11)
    a = min(h, 12 - h) * 30
    return N(f"What is the smaller angle between the hands of a clock at {h} o'clock?", a, "°", units=["°"], o="O1", d="H", fig={"kind": "clock", "h": h, "m": 0})
def a9(r):
    a = r.randint(200, 340)
    return N(f"A reflex angle is {a}°. What is the angle that makes it up to a full turn?", 360 - a, "°", units=["°"], o="O1")


s.std([a2, a4, a8, a1, a3, a6, a9, a7], EX("Explain how to find x when x and 65° are on a straight line.", [("angles on a straight line add up to 180°", "180"), ("x = 180 − 65 = 115°", "115")], "Angles on a straight line add up to 180°, so x = 180° − 65° = 115°.", o="O1"))

s = U.section("13.2", "Angles in a triangle", ["O2"])
s.idea("Angle sum of a triangle", ["The three angles inside **any triangle** add up to **180°**. If two angles are 50° and 60°, the third is 180 − 110 = **70°**.",
       "An **equilateral** triangle has three 60° angles. An **isosceles** triangle has two equal angles."], fig=TRI("50°", "60°", "x"))
s.check(N("A triangle has angles 40° and 75°. Find the third angle.", 65, "°", units=["°"], o="O2"))
s.idea("Why a triangle's angles add to 180°", ["Tear the three corners off a paper triangle and put them together: they make a straight line, which is 180°.",
       "This works for every triangle."])
s.mistake("180 not 360", ["Triangles: 180°. Quadrilaterals and full turns: 360°."])


def t1(r):
    a, b = r.randint(25, 90), r.randint(25, 90)
    if a + b >= 165: return None
    return N("Find the missing angle x.", 180 - a - b, "°", units=["°"], o="O2", fig=TRI(f"{a}°", f"{b}°", "x"))
def t2(r):
    a = r.randint(15, 75)
    return N(f"A right-angled triangle has one angle of {a}°. Find the third angle.", 90 - a, "°", units=["°"], o="O2", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [0, 5]], "ang": ["", f"{a}°", "x"], "right": [0]})
def t3(r):
    a, b = r.randint(20, 80), r.randint(20, 80)
    if a + b >= 170: return None
    return N(f"A triangle has angles of {a}° and {b}°. Find the third angle.", 180 - a - b, "°", units=["°"], o="O2")
def t4(r):
    a = r.randint(10, 80) * 2
    if a >= 170: return None
    return N(f"An isosceles triangle has a top angle of {a}°. The other two angles are equal. Find one of them.", (180 - a) // 2, "°", units=["°"], o="O2", d="H")
def t5(r):
    b = r.randint(30, 80)
    return N(f"An isosceles triangle has two equal angles of {b}°. Find the third angle.", 180 - 2 * b, "°", units=["°"], o="O2")
def t6(r):
    a, b = r.randint(30, 80), r.randint(30, 80)
    if a + b >= 170: return None
    return TB("Complete the table for triangles.", ["Angle 1", "Angle 2", "Angle 3"], [[f"{a}°", f"{b}°", B(180 - a - b)], ["60°", "60°", B(60)]], o="O2")
def t7(r):
    return MC("Can a triangle have angles of 100°, 50° and 40°?", "No, they add up to 190°", ["Yes", "No, it needs a right angle"], o="O2")
def t8(r):
    a, b = r.randint(30, 70), r.randint(30, 70)
    c = 180 - a - b
    return N(f"In a triangle two angles are {a}° and {b}°. The third angle is next to an outside angle on a straight line. Find the outside angle.", 180 - c, "°", units=["°"], o="O2", d="H")


def m2_1(r):
    rows = r.sample([("A triangle can have two right angles", "Never true"), ("A triangle can have one obtuse angle", "Always true"), ("The angles in a triangle add to 180°", "Always true"), ("An isosceles triangle has a right angle", "Sometimes true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O2", d="H", extra=["Always true", "Sometimes true", "Never true"], reason="Two right angles already make 180°, leaving nothing for the third angle.")


s.std([t1, t2, t3, t4, t5, t6, t7, t8], EX("Explain why each angle of an equilateral triangle is 60°.", [("the three angles are equal", "equal|same"), ("180 ÷ 3 = 60", "180|÷ ?3|60")], "The angles of a triangle add up to 180°. In an equilateral triangle all three angles are equal, so each is 180° ÷ 3 = 60°.", o="O2"),
      deep=[m2_1])

U.mindmap(("Angle types", "Acute • right • obtuse • reflex", "O1", "13.1"), ("Angle facts", "Straight line 180° • point 360°", "O1", "13.1"), ("Triangles", "Angles add up to 180°", "O2", "13.2"))
