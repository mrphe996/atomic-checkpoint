# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 10 Angles (10.1 Estimating and measuring angles, 10.2 Angles on a straight line).
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(10, "Angles", "Geometry and measure",
         "Acute, right and obtuse angles, estimating and measuring with a protractor, and angles on a straight line.",
         {"O1": {"code": "5Gg.05", "sec": "10.1", "codeNote": "", "t": "Classify, estimate and measure angles in degrees, including acute, right and obtuse angles."},
          "O2": {"code": "5Gg.06", "sec": "10.2", "codeNote": "", "t": "Know that angles on a straight line add up to 180° and use this to find missing angles."}})
KIND = lambda a: "acute" if a < 90 else "right angle" if a == 90 else "obtuse" if a < 180 else "straight"

s = U.section("10.1", "Estimating and measuring angles", ["O1"])
s.idea("Types of angle", ["Angles are measured in **degrees (°)**. A **right angle** is 90°. An **acute** angle is less than 90°. An **obtuse** angle is between 90° and 180°.",
       "To **estimate**, compare with a right angle: is it smaller or bigger? Then measure with a **protractor**."], fig={"kind": "anglept", "line": True, "angles": [60, 120]})
s.check(MC("What type of angle is 110°?", "obtuse", [("acute", ""), ("right angle", "")], o="O1"))
s.mistake("Size of the arms", ["Longer arms do not make a bigger angle. The angle is the amount of turn."])


def a1(r):
    a = r.randint(5, 175)
    if a == 90: return None
    return MC(f"What type of angle is {a}°?", KIND(a), [x for x in ["acute", "right angle", "obtuse"] if x != KIND(a)], o="O1")
def a2(r):
    ang = r.sample([15, 35, 60, 80, 90, 100, 130, 170], 4)
    return GD("Classify each angle.", "Type", [(f"{a}°", KIND(a)) for a in ang], o="O1", extra=["acute", "right angle", "obtuse"])
def a3(r):
    a = r.randint(2, 17) * 10
    return MC("Estimate the size of the marked angle.", f"{a}°", [f"{180 - a}°" if a != 90 else "45°", f"{min(a + 60, 175)}°" if a + 60 != 180 - a else "5°"], o="O1", fig={"kind": "anglept", "line": True, "angles": [a, 180 - a], "labels": ["?", ""]}) if abs(a - 90) >= 20 else None
def a4(r):
    h = pick(r, [3, 9, 6, 12])
    return MC(f"At {h} o'clock, what type of angle do the hands of a clock make?", "right angle" if h in (3, 9) else "straight" if h == 6 else "no angle (0°)", ["acute", "obtuse"], o="O1", fig={"kind": "clock", "h": h, "m": 0})
def a5(r):
    n = r.randint(1, 4)
    return N(f"How many degrees are in {n} right angle{'s' if n > 1 else ''}?", 90 * n, "°", units=["°"], o="O1")
def a6(r):
    h = r.randint(1, 5)
    return MC(f"What type of angle is between the hands of a clock at {h} o'clock?", KIND(30 * h), [x for x in ["acute", "right angle", "obtuse"] if x != KIND(30 * h)], o="O1", fig={"kind": "clock", "h": h, "m": 0})
def a7(r):
    t = pick(r, ["quarter", "half", "three-quarter"])
    return N(f"How many degrees is a {t} turn?", {"quarter": 90, "half": 180, "three-quarter": 270}[t], "°", units=["°"], o="O1")
def a8(r):
    return OD("Put the angles in order, smallest first.", ["acute angle of 40°", "right angle", "obtuse angle of 120°", "straight line (180°)"], o="O1", d="H")
def a9(r):
    a, b = r.randint(20, 80), r.randint(100, 170)
    return N(f"How much bigger is an angle of {b}° than an angle of {a}°?", b - a, "°", units=["°"], o="O1", d="H")


s.std([a3, a4, a1, a2, a5, a6, a7, a9, a8], EX("Explain how you know an angle of 95° is obtuse.", [("it is more than 90°", "more than 90|bigger than 90|> ?90"), ("and less than 180°", "less than 180|< ?180")], "An obtuse angle is bigger than a right angle (90°) but less than 180°. 95° is between them, so it is obtuse.", o="O1"))

s = U.section("10.2", "Angles on a straight line", ["O2"])
s.idea("180° on a line", ["Angles that sit together on a **straight line** add up to **180°** (a half turn).",
       "If one angle is 70°, the other is 180° − 70° = **110°**."], fig={"kind": "anglept", "line": True, "angles": [70, 110], "labels": ["70°", "x"]})
s.check(N("Two angles on a straight line are 45° and x. Find x.", 135, "°", units=["°"], o="O2"))
s.mistake("Check by adding", ["After finding x, add the angles: they must make 180°."])


def b1(r):
    a = r.randint(15, 165)
    return N("Find the missing angle x.", 180 - a, "°", units=["°"], o="O2", fig={"kind": "anglept", "line": True, "angles": [a, 180 - a], "labels": [f"{a}°", "x"]})
def b2(r):
    a = r.randint(15, 165)
    return N(f"Two angles on a straight line are {a}° and x. Find x.", 180 - a, "°", units=["°"], o="O2")
def b3(r):
    a, b = r.randint(20, 70), r.randint(20, 70)
    return N("Three angles on a straight line are shown. Find x.", 180 - a - b, "°", units=["°"], o="O2", d="H", fig={"kind": "anglept", "line": True, "angles": [a, b, 180 - a - b], "labels": [f"{a}°", f"{b}°", "x"]})
def b4(r):
    xs = r.sample(range(20, 160), 3)
    return TB("Each angle is on a straight line with another. Find the other angle.", ["Angle", "Other angle"], [[f"{x}°", B(180 - x)] for x in xs], o="O2")
def b5(r):
    a = r.randint(20, 160)
    return MC(f"Can angles of {a}° and {180 - a + pick(r, [10, -10])}° sit together on a straight line?", "No, they do not add up to 180°", ["Yes", "Only if they are both acute"], o="O2")
def b6(r):
    a = r.randint(5, 85)
    return N(f"Two equal angles and an angle of {2 * a}° make a straight line. How big is each equal angle?", (180 - 2 * a) // 2, "°", units=["°"], o="O2", d="H")
def b7(r):
    a = r.randint(15, 165)
    return MC(f"One angle on a straight line is {a}°. What type is the other angle?", KIND(180 - a), [x for x in ["acute", "right angle", "obtuse"] if x != KIND(180 - a)], o="O2") if a != 90 else None
def b8(r):
    return N("Two angles on a straight line are equal. How big is each one?", 90, "°", units=["°"], o="O2")


s.std([b1, b4, b2, b3, b5, b7, b6, b8], EX("Explain how to find x if x and 130° are on a straight line.", [("angles on a straight line add up to 180°", "180"), ("x = 180 − 130 = 50°", "50")], "Angles on a straight line add up to 180°, so x = 180° − 130° = 50°.", o="O2"))

U.mindmap(("Angle types", "Acute • right • obtuse", "O1", "10.1"), ("Measuring", "Estimate first • protractor", "O1", "10.1"), ("Straight line", "Angles add up to 180°", "O2", "10.2"))
