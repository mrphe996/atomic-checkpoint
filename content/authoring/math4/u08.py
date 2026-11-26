# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 8 Angles (8.1 Comparing angles, 8.2 Acute and obtuse, 8.3 Estimating angles).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(8, "Angles", "Geometry and measure",
         "Comparing angles, right angles, acute and obtuse angles, and estimating the size of angles in degrees.",
         {"O1": {"code": "4Gg.03", "sec": "8.1", "codeNote": "", "t": "Compare angles with a right angle and order angles by size."},
          "O2": {"code": "4Gg.04", "sec": "8.2", "codeNote": "", "t": "Classify angles as acute, right or obtuse."},
          "O3": {"code": "4Gg.05", "sec": "8.3", "codeNote": "", "t": "Estimate the size of angles in degrees."}})
KIND = lambda a: "acute" if a < 90 else "right" if a == 90 else "obtuse"
ANG = lambda a, lab="?": {"kind": "anglept", "line": True, "angles": [a, 180 - a], "labels": [lab, ""]}

s = U.section("8.1", "Comparing angles", ["O1"])
s.idea("Amount of turn", ["An **angle** is an amount of turn. A **right angle** is a quarter turn, **90°**. A straight line is two right angles, **180°**.",
       "To compare angles, look at how far one arm turns from the other – not at how long the arms are."], fig=ANG(90, "90°"))
s.check(N("How many degrees are in a right angle?", 90, "°", units=["°"], o="O1"))
s.check(MC('Before you read on: is a right angle bigger than half a turn?', 'No – it is a quarter turn', [('Yes', 'A right angle is 90°; half a turn is 180°.'), ('They are equal', 'Two right angles make half a turn.')], o='O1'))
s.mistake("Long arms", ["Longer arms do not make a bigger angle."])


def c1(r):
    a, b = r.sample([20, 35, 50, 70, 100, 120, 150], 2)
    return MC(f"Angle A is {a}° and angle B is {b}°. Which is bigger?", "A" if a > b else "B", ["B" if a > b else "A", "they are equal"], o="O1")
def c2(r):
    xs = r.sample([15, 40, 65, 90, 110, 140, 170], 4)
    return OD("Put the angles in order, smallest first.", [f"{x}°" for x in sorted(xs)], o="O1")
def c3(r):
    a = pick(r, [30, 45, 60, 120, 135, 150])
    k = "smaller" if a < 90 else "bigger"
    return MC("Is the marked angle smaller or bigger than a right angle?", k, ["smaller" if k == "bigger" else "bigger", "the same"], o="O1", fig=ANG(a))
def c4(r):
    n = r.randint(1, 4)
    return N(f"How many degrees are in {n} right angle{'s' if n > 1 else ''}?", 90 * n, "°", units=["°"], o="O1")
def c5(r):
    h = pick(r, [3, 9, 6])
    return MC(f"At {h} o'clock, what angle do the clock hands make?", "a right angle" if h in (3, 9) else "a straight angle (180°)", ["an acute angle", "an obtuse angle"], o="O1", fig={"kind": "clock", "h": h, "m": 0})
def c6(r):
    t = pick(r, ["quarter", "half", "three-quarter", "whole"])
    return N(f"How many degrees is a {t} turn?", {"quarter": 90, "half": 180, "three-quarter": 270, "whole": 360}[t], "°", units=["°"], o="O1")
def c7(r):
    a = r.randint(20, 70)
    return N(f"Two angles together make a right angle. One is {a}°. What is the other?", 90 - a, "°", units=["°"], o="O1", d="H")
def c8(r):
    a, b = r.randint(20, 80), r.randint(100, 170)
    return N(f"How many degrees bigger is an angle of {b}° than an angle of {a}°?", b - a, "°", units=["°"], o="O1", d="H")


s.std([c3, c5, c1, c2, c4, c6, c7, c8], EX("Explain how to tell if an angle is bigger than a right angle.", [("compare it with a square corner", "square corner|right angle|corner"), ("if it opens wider, it is bigger", "wider|bigger|more")], "Put a square corner (a right angle) against it. If the angle opens wider than the corner, it is bigger than a right angle.", o="O1"))

s = U.section("8.2", "Acute and obtuse", ["O2"])
s.idea("Naming angles", ["An **acute** angle is less than 90°. A **right** angle is exactly 90°. An **obtuse** angle is more than 90° but less than 180°."],
       table={"head": ["Angle", "Size"], "rows": [["acute", "less than 90°"], ["right", "90°"], ["obtuse", "between 90° and 180°"]]})
s.check(MC("What type of angle is 125°?", "obtuse", [("acute", ""), ("right", "")], o="O2"))
s.check(MC('Before you read on: is 100° acute or obtuse?', 'Obtuse', [('Acute', 'Acute angles are less than 90°.'), ('Right', 'A right angle is exactly 90°.')], o='O2'))
s.mistake("Acute is small", ["Remember: 'a cute little angle' is small – less than 90°."])


def k1(r):
    a = r.randint(5, 175)
    if a == 90: return None
    return MC(f"What type of angle is {a}°?", KIND(a), [x for x in ["acute", "right", "obtuse"] if x != KIND(a)], o="O2")
def k2(r):
    ang = r.sample([15, 40, 75, 90, 100, 130, 160, 85], 4)
    return GD("Classify each angle.", "Type", [(f"{a}°", KIND(a)) for a in ang], o="O2", extra=["acute", "right", "obtuse"])
def k3(r):
    a = pick(r, [30, 45, 60, 120, 135, 150, 90])
    return MC("What type is the marked angle?", KIND(a), [x for x in ["acute", "right", "obtuse"] if x != KIND(a)], o="O2", fig=ANG(a))
def k4(r):
    return MS("Select ALL the obtuse angles.", r.sample(["100°", "135°", "170°", "95°"], 2), r.sample(["45°", "90°", "60°", "10°"], 2), o="O2")
def k5(r):
    a = r.randint(20, 160)
    if a == 90: return None
    return MC(f"One angle on a straight line is {a}°. What type is the other angle?", KIND(180 - a), [x for x in ["acute", "right", "obtuse"] if x != KIND(180 - a)], o="O2", d="H")
def k6(r):
    h = r.randint(1, 5)
    a = 30 * h
    return MC(f"What type of angle do the clock hands make at {h} o'clock?", KIND(a), [x for x in ["acute", "right", "obtuse"] if x != KIND(a)], o="O2", fig={"kind": "clock", "h": h, "m": 0})
def k7(r):
    xs = r.sample(range(10, 170, 5), 6)
    return N(f"How many of these angles are acute: {', '.join(f'{x}°' for x in xs)}?", sum(1 for x in xs if x < 90), "angles", units=["angles"], o="O2")
def k8(r):
    return MC("Which shape has an obtuse angle?", "a regular hexagon", ["a square", "a rectangle", "an equilateral triangle"], o="O2", d="H")


s.std([k3, k6, k1, k2, k4, k7, k5, k8], EX("Explain the difference between acute and obtuse angles.", [("acute is less than 90°", "less than 90|smaller than 90"), ("obtuse is more than 90° and less than 180°", "more than 90|bigger than 90|between 90")], "An acute angle is less than a right angle (90°). An obtuse angle is more than 90° but less than 180°.", o="O2"))

s = U.section("8.3", "Estimating angles", ["O3"])
s.idea("Use known angles", ["Use angles you know to estimate: **90°** (right angle), **45°** (half a right angle), **180°** (straight line).",
       "An angle a bit less than a right angle might be about 80°; halfway between 90° and 180° is about 135°."], fig=ANG(45, "45°"))
s.check(MC("Which is the best estimate for half a right angle?", "45°", [("90°", ""), ("10°", ""), ("150°", "")], o="O3"))
s.check(MC('Before you read on: which is the best estimate for an angle a little bigger than a right angle?', '100°', [('45°', 'That is half a right angle.'), ('180°', 'That is a straight line.')], o='O3'))
s.mistake("Check with a right angle", ["If an angle is obtuse, your estimate must be more than 90°."])


def e1(r):
    a = pick(r, [30, 45, 60, 120, 135, 150])
    return MC("Estimate the size of the marked angle.", f"{a}°", [f"{180 - a}°", f"{a // 3}°" if a > 60 else f"{a + 90}°"], o="O3", fig=ANG(a))
def e2(r):
    a = pick(r, [20, 45, 70, 110, 160])
    return MC("Which is the best estimate for this angle?", f"about {a}°", [f"about {min(a + 70, 175)}°" if a < 100 else f"about {a - 70}°", "about 270°"], o="O3", fig=ANG(a), d="H")
def e3(r):
    return MC("A door is opened a little, less than half of a right angle. Which estimate fits best?", "30°", ["90°", "60°", "120°"], o="O3")
def e4(r):
    xs = r.sample([("half a right angle", 45), ("a right angle", 90), ("a straight line", 180), ("a whole turn", 360), ("a third of a right angle", 30)], 3)
    return TB("Complete the table.", ["Angle", "Degrees"], [[t, B(v)] for t, v in xs], o="O3")
def e5(r):
    a = pick(r, [40, 50, 60, 120, 130, 140]); k = KIND(a)
    return MC(f"Ravi estimates an {k} angle as {180 - a if k == 'acute' else 180 - a}°. Is that sensible?", "No, an " + k + " angle must be " + ("less" if k == "acute" else "more") + " than 90°", ["Yes, it is close", "Yes, any estimate is fine"], o="O3", d="H")
def e6(r):
    h = pick(r, [1, 2, 4, 5])
    return N(f"Each hour on a clock is 30°. Estimate the angle between the hands at {h} o'clock.", 30 * h, "°", units=["°"], o="O3", fig={"kind": "clock", "h": h, "m": 0}, tol=0)
def e7(r):
    a = pick(r, [30, 60, 120, 150])
    return N(f"An angle is {a}°. How many degrees away from a right angle is it?", abs(90 - a), "°", units=["°"], o="O3")
def e8(r):
    n = pick(r, [2, 3, 4, 6])
    return N(f"A right angle is split into {n} equal angles. Estimate each one in degrees.", 90 // n if 90 % n == 0 else round(90 / n), "°", units=["°"], o="O3", tol=1, d="H")


s.std([e1, e4, e3, e6, e7, e2, e5, e8], EX("Explain how to estimate an angle that is a bit more than a right angle.", [("start from 90°", "90|right angle"), ("add a little: about 100°", "100|110|more")], "Start from a right angle, 90°. It is only a little more, so a good estimate is about 100°.", o="O3"))

U.mindmap(("Comparing", "Right angle = 90° • amount of turn", "O1", "8.1"), ("Types", "Acute < 90° • right • obtuse > 90°", "O2", "8.2"), ("Estimating", "Use 45°, 90°, 180°", "O3", "8.3"))
