# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 5 Angles and constructions (5.1 Parallel lines, 5.2 The exterior angle of a triangle,
5.3 Constructions). Written by the Atomic teaching team."""
from kit import *

U = Unit(5, "Angles and Constructions", "Geometry and measure",
         "Corresponding and alternate angles on parallel lines, the exterior angle of a triangle, and ruler-and-compasses constructions.",
         {"O1": {"code": "8Gg.01", "sec": "5.1", "codeNote": "", "t": "Recognise corresponding, alternate and vertically opposite angles on parallel lines and use them to find angles."},
          "O2": {"code": "8Gg.02", "sec": "5.2", "codeNote": "", "t": "Use the fact that the exterior angle of a triangle equals the sum of the two interior opposite angles."},
          "O3": {"code": "8Gg.03", "sec": "5.3", "codeNote": "", "t": "Construct perpendicular bisectors, angle bisectors and triangles with ruler and compasses."}})
ANG = "abcdefgh"
# positions on the parallel-lines figure: a b / d c at the top crossing, e f / h g at the bottom one (a,b,c,d clockwise from top-left)
# with the default slope: a = c = e = g (the acute/obtuse pair) and b = d = f = h
SAME = {"a": "aceg", "b": "bdfh", "c": "aceg", "d": "bdfh", "e": "aceg", "f": "bdfh", "g": "aceg", "h": "bdfh"}
REL = {("a", "e"): "corresponding", ("b", "f"): "corresponding", ("c", "g"): "corresponding", ("d", "h"): "corresponding",
       ("c", "e"): "alternate", ("d", "f"): "alternate", ("a", "c"): "vertically opposite", ("b", "d"): "vertically opposite",
       ("e", "g"): "vertically opposite", ("f", "h"): "vertically opposite", ("c", "f"): "co-interior", ("d", "e"): "co-interior"}

# ================================================================== 5.1
s = U.section("5.1", "Parallel lines", ["O1"])
s.idea("Angles on parallel lines", ["When a line crosses two **parallel** lines (marked with arrows), it makes 8 angles.",
       "**Corresponding** angles are equal (an F shape). **Alternate** angles are equal (a Z shape). **Vertically opposite** angles are equal (an X shape).",
       "Angles on a straight line add up to 180°, so co-interior angles (a C shape) add up to 180°."], fig={"kind": "parallel", "labels": {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h"}})
s.example("Finding angles", "On the diagram, a = 70°. Find c, e and f.", [("c = 70°", "vertically opposite a"), ("e = 70°", "corresponding to a"), ("f = 180° − 70° = 110°", "on a straight line with e")], "c = 70°, e = 70°, f = 110°")
s.check(N("Two parallel lines are crossed by a transversal. One angle is 65°. An alternate angle to it is x. Find x.", 65, "°", units=["°"], o="O1", fig={"kind": "parallel", "labels": {"c": "65°", "e": "x"}}))
s.mistake("Equal or 180?", ["Only angles in matching positions (F, Z or X shapes) are equal. Angles in a C shape add to 180°."])


def a1(r):
    v = r.randint(35, 80); k, t = pick(r, [("a", "e"), ("b", "f"), ("c", "g"), ("d", "h"), ("c", "e"), ("d", "f"), ("a", "c")])
    val = v if k in "aceg" else 180 - v
    return N(f"The angle marked {val}° and the angle x are on parallel lines. Find x.", val, "°", units=["°"], o="O1", fig={"kind": "parallel", "labels": {k: f"{val}°", t: "x"}}, reason=f"x and {val}° are {REL[(k, t)]} angles, so they are equal.")
def a2(r):
    v = r.randint(35, 80); k, t = pick(r, [("c", "f"), ("d", "e"), ("a", "b"), ("e", "f"), ("g", "h")])
    val = v if k in "aceg" else 180 - v
    return N("Find the angle x.", 180 - val, "°", units=["°"], o="O1", fig={"kind": "parallel", "labels": {k: f"{val}°", t: "x"}}, reason=f"These angles add up to 180°: x = 180° − {val}° = {180 - val}°.")
def a3(r):
    k, t = pick(r, list(REL)); kind = REL[(k, t)]
    return MC(f"What type of angle pair are {k} and {t}?", f"{kind}", [x for x in ["corresponding", "alternate", "vertically opposite", "co-interior"] if x != kind][:3], o="O1", fig={"kind": "parallel", "labels": {k: k, t: t}})
def a4(r):
    v = r.randint(35, 80)
    lab = {"a": f"{v}°"}; ts = r.sample("bcdefgh", 3)
    for t in ts: lab[t] = t
    return TB("Find the three labelled angles.", ["Angle", "Size (°)"], [[t, B(v if t in "aceg" else 180 - v)] for t in sorted(ts)], o="O1", fig={"kind": "parallel", "labels": lab}, d="H")
def a5(r):
    rows = [("Corresponding angles", "Equal"), ("Alternate angles", "Equal"), ("Co-interior angles", "Add to 180°"), ("Vertically opposite angles", "Equal"), ("Angles on a straight line", "Add to 180°")]
    return GD("Are these angle pairs equal, or do they add to 180°?", "Rule", r.sample(rows, 4), o="O1")
def a6(r):
    x = r.randint(20, 40); k = r.randint(2, 3)
    return N(f"Alternate angles on parallel lines are {k}x° and {k * x - 10 + 10}°. Find x.", x, "°", units=["°"], o="O1", d="H", reason=f"Alternate angles are equal: {k}x = {k * x}, so x = {x}.") if False else N(f"Corresponding angles on parallel lines are {k}x + 10 and {k * x + 10} degrees. Find x.", x, o="O1", d="H", reason=f"{k}x + 10 = {k * x + 10} → {k}x = {k * x} → x = {x}.")
def a7(r):
    v = r.randint(40, 75)
    return MC(f"A road crosses two parallel railway lines. The angle between the road and the first line is {v}°. Which other angle MUST also be {v}°?", "the corresponding angle at the second line", [("the angle next to it on the straight line", f"That is {180 - v}°."), ("every angle at the second crossing", f"Half of them are {180 - v}°."), ("none of them", "")], o="O1")
def a8(r):
    v = r.randint(100, 140)
    return N(f"Co-interior angles between parallel lines are {v}° and y. Find y.", 180 - v, "°", units=["°"], o="O1", fig={"kind": "parallel", "labels": {"c": f"{180 - v if 180 - v < 90 else v}°", "f": "y"}} if False else None, reason=f"Co-interior angles add to 180°: y = {180 - v}°.")


def a9(r):
    x = r.randint(20, 50); p, q = r.randint(3, 5), r.randint(1, 2); c = r.randint(5, 30); d = (p - q) * x - c
    if d <= 0: return None
    return N(f"Alternate angles on parallel lines are ({p}x − {c})° and ({q}x + {d})°. Find x.", x, o="O1", d="H", reason=f"{p}x − {c} = {q}x + {d} → {p - q}x = {c + d} → x = {x}.")
def a10(r):
    v = r.randint(35, 80)
    return N(f"A ladder leans against a wall. The top and bottom of the wall are parallel lines; the ladder makes an angle of {v}° with the ground. What angle does it make with the top line, on the alternate side?", v, "°", units=["°"], o="O1", d="H", reason="Alternate angles are equal.")


s.std([a1, a4, a2, a3, a5, a7, a8, a6, a9, a10], EX("Explain how you know that alternate angles on parallel lines are equal.", [("an alternate angle is vertically opposite / on a line with a corresponding angle", ["vertically opposite|corresponding|straight line"]), ("so both equal the same angle", ["equal|same|both"])], "Each alternate angle is vertically opposite the corresponding angle of the other. Corresponding angles are equal and vertically opposite angles are equal, so alternate angles are equal.", o="O1"))

# ================================================================== 5.2
s = U.section("5.2", "The exterior angle of a triangle", ["O2"])
s.idea("Exterior angle", ["Extend one side of a triangle. The angle outside the triangle is an **exterior angle**.",
       "**The exterior angle equals the sum of the two interior opposite angles.** It also makes 180° with the interior angle next to it."], fig={"kind": "shape", "pts": [[0, 0], [7, 0], [2, 5]], "ang": ["50°", "", "70°"]})
s.example("Using the rule", "Two interior angles of a triangle are 48° and 67°. Find the exterior angle at the third vertex.", [("exterior = 48° + 67°", "sum of the two interior opposite angles"), ("= 115°", "")], "115°")
s.check(N("A triangle has interior angles 35° and 80°. Find the exterior angle at the third vertex.", 115, "°", units=["°"], o="O2"))
s.mistake("Which angles?", ["Use the two interior angles that are NOT next to the exterior angle."])


def e1(r):
    a, b = r.randint(25, 75), r.randint(25, 75)
    return N(f"A triangle has interior angles {a}° and {b}°. Find the exterior angle at the third vertex.", a + b, "°", units=["°"], o="O2", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [3, 5]], "ang": [f"{a}°", "", f"{b}°"]}, reason=f"{a}° + {b}° = {a + b}°.")
def e2(r):
    a, ex = r.randint(25, 70), r.randint(100, 150)
    return N(f"The exterior angle of a triangle is {ex}°. One interior opposite angle is {a}°. Find the other interior opposite angle.", ex - a, "°", units=["°"], o="O2", reason=f"{ex}° − {a}° = {ex - a}°.")
def e3(r):
    ex = r.randint(95, 160)
    return N(f"An exterior angle of a triangle is {ex}°. Find the interior angle next to it.", 180 - ex, "°", units=["°"], o="O2", reason=f"Angles on a straight line: 180° − {ex}° = {180 - ex}°.")
def e4(r):
    x = r.randint(15, 35); k = r.randint(2, 3)
    return N(f"The two interior opposite angles of a triangle are x and {k}x. The exterior angle is {(k + 1) * x}°. Find x.", x, "°", units=["°"], o="O2", d="H", reason=f"{k + 1}x = {(k + 1) * x}, x = {x}°.")
def e5(r):
    a = r.randint(30, 70)
    return N(f"An isosceles triangle has two equal angles of {a}°. Find the exterior angle next to one of the equal angles.", 180 - a, "°", units=["°"], o="O2", d="H", reason=f"Exterior = the other two interior angles: {180 - 2 * a}° + {a}° = {180 - a}°.")
def e6(r):
    a, b = r.randint(25, 75), r.randint(25, 75)
    return TB("Complete the table for this triangle.", ["Angle", "Size (°)"], [["Third interior angle", B(180 - a - b)], ["Exterior angle at the third vertex", B(a + b)]], o="O2", data={"head": ["Interior angle", "A", "B"], "rows": [["Size", f"{a}°", f"{b}°"]]})
def e7(r):
    return MC("For any triangle, the exterior angle is…", "equal to the sum of the two interior opposite angles", [("equal to the interior angle next to it", "They add to 180°."), ("always 180°", ""), ("always obtuse", "It can be acute if the triangle is obtuse.")], o="O2")
def e8(r):
    a = r.randint(20, 60)
    return N(f"In an equilateral triangle, what is each exterior angle?", 120, "°", units=["°"], o="O2", reason="Each interior angle is 60°; 180° − 60° = 120°.") if a % 2 else N(f"In a right-angled triangle, one acute angle is {a}°. Find the exterior angle next to the right angle.", 90, "°", units=["°"], o="O2", reason="Angles on a straight line: 180° − 90° = 90°.")


def e9(r):
    a, b = r.randint(30, 60), r.randint(30, 60)
    return N(f"A triangle has interior angles {a}°, {b}° and {180 - a - b}°. Find the largest exterior angle.", 180 - min(a, b, 180 - a - b), "°", units=["°"], o="O2", d="H", reason=f"The largest exterior angle is next to the smallest interior angle: 180° − {min(a, b, 180 - a - b)}° = {180 - min(a, b, 180 - a - b)}°.")
def e10(r):
    x = r.randint(10, 30); c = r.randint(20, 60)
    return N(f"The exterior angle of a triangle is (3x + {c})°. The interior opposite angles are 2x° and ({x + c})°. Find x.", x, o="O2", d="VH", reason=f"3x + {c} = 2x + {x + c} → x = {x}.")


s.std([e1, e6, e2, e3, e7, e8, e4, e5, e9, e10], EX("Explain why the exterior angle of a triangle equals the sum of the two interior opposite angles.", [("interior angles add up to 180°", ["180.*triangle|triangle.*180|interior.*180"]), ("the exterior angle and the third interior angle also add to 180°, so they are equal", ["straight line|also.*180|same.*180"])], "The three interior angles add to 180°. The exterior angle and the third interior angle are on a straight line, so they also add to 180°. So the exterior angle equals the other two interior angles added together.", o="O2"))

# ================================================================== 5.3
s = U.section("5.3", "Constructions", ["O3"])
s.idea("Ruler and compasses", ["A **perpendicular bisector** cuts a line in half at right angles. Open the compasses to more than half the line, draw arcs from each end above and below, and join the crossing points.",
       "An **angle bisector** cuts an angle in half. Draw an arc from the vertex across both arms, then equal arcs from those two points; join the vertex to where they cross."])
s.method("Triangle from three sides (SSS)", ["Draw one side with a ruler. Set the compasses to the second length and draw an arc from one end; set them to the third length and draw an arc from the other end. Join the crossing point to both ends."])
s.check(N("A line AB is 10 cm long. Its perpendicular bisector crosses AB at M. How long is AM?", 5, "cm", units=["cm"], o="O3"))
s.mistake("Keep the arcs", ["Leave your construction arcs on the diagram: they show your method."])


def c1(r):
    l = r.randint(6, 18)
    return N(f"A line is {l} cm long. Its perpendicular bisector meets it at M. How far is M from each end?", l / 2, "cm", units=["cm"], o="O3", reason=f"Bisect = cut in half: {fmt(l / 2)} cm.")
def c2(r):
    a = r.randint(40, 150)
    return N(f"An angle of {a}° is bisected. What is the size of each new angle?", a / 2, "°", units=["°"], o="O3", reason=f"{a} ÷ 2 = {fmt(a / 2)}°.")
def c3(r):
    return MC("What angle does a perpendicular bisector make with the line it bisects?", "90°", [("45°", ""), ("180°", ""), ("60°", "")], o="O3")
def c4(r):
    steps = ["Draw the longest side with a ruler", "Set the compasses to the second length and draw an arc from one end", "Set the compasses to the third length and draw an arc from the other end", "Join the point where the arcs cross to both ends"]
    return OD("Put the steps for constructing a triangle from three sides in order.", steps, o="O3")
def c5(r):
    a, b, c = sorted(r.sample(range(3, 14), 3))
    ok = a + b > c
    return MC(f"Can you construct a triangle with sides {a} cm, {b} cm and {c} cm?", "Yes" if ok else "No", [("No" if ok else "Yes", f"{a} + {b} {'>' if ok else '≤'} {c}."), ("Only if it is right-angled", "")], o="O3", d="H", reason=f"The two shorter sides must add to more than the longest: {a} + {b} = {a + b} {'>' if ok else '≤'} {c}.")
def c6(r):
    rows = [("Perpendicular bisector", "Cuts a line in half at 90°"), ("Angle bisector", "Cuts an angle in half"), ("Arc", "Part of a circle drawn with compasses"), ("Perpendicular", "At right angles")]
    return GD("Match each word to its meaning.", "Meaning", r.sample(rows, 4), o="O3")
def c7(r):
    l = r.randint(4, 12)
    return MC(f"To draw the perpendicular bisector of a {l} cm line, the compasses must be opened to…", f"more than {fmt(l / 2)} cm", [(f"exactly {fmt(l / 2)} cm", "The arcs would only just touch."), (f"less than {fmt(l / 2)} cm", "The arcs would not cross."), (f"exactly {l} cm", "This works but is not required; any length over half works.")], o="O3", d="H")
def c8(r):
    a = r.randint(30, 80)
    return N(f"A triangle is constructed with angles {a}° and {a + 20}° at the ends of its base. What is the third angle?", 180 - 2 * a - 20, "°", units=["°"], o="O3", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [3, 4]], "ang": [f"{a}°", f"{a + 20}°", "?"]}, reason=f"180° − {a}° − {a + 20}° = {160 - 2 * a}°.") if 160 - 2 * a > 0 else None
def c9(r):
    a = r.randint(4, 10)
    return N(f"Point P is on the perpendicular bisector of AB. PA = {a} cm. Find PB.", a, "cm", units=["cm"], o="O3", d="H", reason="Every point on the perpendicular bisector is the same distance from A and B.")


def c10(r):
    h = r.randint(15, 80)
    return N(f"An angle is bisected. Each half measures {h}°. What was the size of the original angle?", 2 * h, "°", units=["°"], o="O3", reason=f"2 × {h}° = {2 * h}°.")
def c11(r):
    a = r.randint(3, 9); b = r.randint(3, 9)
    return N(f"A triangle has sides {a} cm and {b} cm. What is the largest whole number of centimetres the third side can be?", a + b - 1, "cm", units=["cm"], o="O3", d="VH", reason=f"The third side must be less than {a} + {b} = {a + b} cm, so at most {a + b - 1} cm.")


s.std([c6, c8, c1, c2, c3, c4, c5, c7, c9, c10, c11], EX("Explain why the compasses must stay the same width when drawing the two arcs of a perpendicular bisector.", [("the crossing points must be the same distance from both ends", ["same distance|equal distance|equidistant"]), ("so the line is exactly in the middle / symmetrical", ["middle|half|symmetr|bisect"])], "The two arcs must be the same radius so that the crossing points are the same distance from both ends. The line through them is then exactly halfway, at right angles.", o="O3"))

U.mindmap(("Parallel lines", "Corresponding (F) and alternate (Z) are equal • co-interior (C) add to 180°", "O1", "5.1"),
          ("Exterior angle", "Exterior = sum of the two interior opposite angles", "O2", "5.2"),
          ("Constructions", "Perpendicular bisector • angle bisector • SSS triangle", "O3", "5.3"))
