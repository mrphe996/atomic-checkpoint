# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 14 Position and transformation (14.1 Bearings, 14.2 The midpoint of a line segment,
14.3 Translating, 14.4 Reflecting, 14.5 Rotating and 14.6 Enlarging 2D shapes). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(14, "Position and Transformation", "Geometry and measure",
         "Bearings, the midpoint of a line segment, and translations, reflections, rotations and enlargements on a coordinate grid.",
         {"O1": {"code": "8Gp.01", "sec": "14.1", "codeNote": "", "t": "Understand and use bearings as a measure of direction."},
          "O2": {"code": "8Gp.02", "sec": "14.2", "codeNote": "", "t": "Find the midpoint of a line segment from the coordinates of its end points."},
          "O3": {"code": "8Gp.03", "sec": "14.3", "codeNote": "", "t": "Translate shapes using vectors written as column vectors."},
          "O4": {"code": "8Gp.04", "sec": "14.4", "codeNote": "", "t": "Reflect shapes in horizontal, vertical and diagonal mirror lines, including y = x."},
          "O5": {"code": "8Gp.05", "sec": "14.5", "codeNote": "", "t": "Rotate shapes about a centre through 90° and 180°."},
          "O6": {"code": "8Gp.06", "sec": "14.6", "codeNote": "", "t": "Enlarge shapes by a positive scale factor from a centre of enlargement."}})
pt = lambda p: f"({p[0]}, {p[1]})"
PACC = lambda p: [f"({p[0]}, {p[1]})", f"({p[0]},{p[1]})", f"{p[0]}, {p[1]}", f"{p[0]},{p[1]}"]


def tri(r, lo=-3, hi=3):
    x, y = r.randint(lo, hi), r.randint(lo, hi)
    return [[x, y], [x + r.randint(1, 3), y], [x, y + r.randint(1, 3)]]


# ================================================================== 14.1
s = U.section("14.1", "Bearings", ["O1"])
s.idea("Three-figure bearings", ["A **bearing** gives a direction as an angle measured **clockwise from north**. It always has **three figures**: east is 090°, south is 180°, west is 270°.",
       "The bearing of A from B is measured at B."], fig={"kind": "bearing", "bearing": 65, "from": "A", "to": "B"})
s.check(N("What is the bearing of south-west? (Write the number of degrees.)", 225, "°", units=["°"], o="O1"))
s.idea("Back bearings", ["If the bearing of B from A is θ, the bearing of A from B is θ + 180° (or θ − 180° if θ is 180° or more)."])
s.idea("Why bearings use three figures", ["A bearing is measured clockwise from north, always with three figures: east is 090°, south is 180°, west is 270°. Three figures stop 90 and 900 being confused.",
       "The back bearing (from B back to A) differs by 180°."])
s.check(MC("Before you read on: the bearing of B from A is 070°. What is the bearing of A from B?", "250°", [("070°", "Going back is the opposite direction."), ("290°", "Add 180°: 070 + 180 = 250.")], o="O1"))
s.mistake("Three figures", ["Write 45° as a bearing of 045°."])


def b1(r):
    d, v = pick(r, [("north-east", 45), ("east", 90), ("south-east", 135), ("south", 180), ("south-west", 225), ("west", 270), ("north-west", 315)])
    return N(f"Write the three-figure bearing of {d}.", v, "°", units=["°"], o="O1")
def b2(r):
    v = r.randint(10, 350)
    return N(f"The bearing of B from A is {v:03d}°. What is the bearing of A from B?", (v + 180) % 360, "°", units=["°"], o="O1", d="H", fig={"kind": "bearing", "bearing": v, "from": "A", "to": "B"}, reason=f"{v} {'+' if v < 180 else '−'} 180 = {(v + 180) % 360:03d}°.")
def b3(r):
    v = r.randint(20, 340)
    return N("Measure-free: the diagram shows the bearing of B from A. Write it as a number of degrees.", v, "°", units=["°"], o="O1", fig={"kind": "bearing", "bearing": v, "from": "A", "to": "B"}, reason=f"The angle is marked clockwise from north: {v:03d}°.") if False else N(f"A ship sails on a bearing of {v:03d}°. It turns to sail in exactly the opposite direction. What is its new bearing?", (v + 180) % 360, "°", units=["°"], o="O1", d="H", reason=f"Opposite direction: ± 180°.")
def b4(r):
    rows = [("North", "000°"), ("East", "090°"), ("South", "180°"), ("West", "270°"), ("North-east", "045°"), ("South-west", "225°")]
    return GD("Write each direction as a three-figure bearing.", "Bearing", r.sample(rows, 4), o="O1", extra=["135°", "315°"])
def b5(r):
    v = r.randint(5, 85)
    return S(f"Write {v}° as a three-figure bearing.", [f"{v:03d}", f"{v:03d}°"], o="O1")
def b6(r):
    v = r.randint(10, 170); t = r.randint(10, 80)
    return N(f"A plane flies on a bearing of {v:03d}°. It turns {t}° clockwise. What is its new bearing?", (v + t) % 360, "°", units=["°"], o="O1", reason=f"{v} + {t} = {v + t}°.")
def b7(r):
    v = r.randint(190, 350)
    return MC(f"A boat sails on a bearing of {v}°. Roughly which direction is it going?", "north-west" if v > 270 else "south-west", ["north-east", "south-east", "north-west" if v <= 270 else "south-west"], o="O1", fig={"kind": "bearing", "bearing": v})
def b8(r):
    v = r.randint(20, 160)
    return N("The diagram shows a bearing measured clockwise from north. Write the bearing in degrees.", v, "°", units=["°"], o="O1", fig={"kind": "bearing", "bearing": v, "from": "A", "to": "B"})


def k141(r):
    b = r.randint(10, 340)
    return N(f"The bearing of Q from P is {b:03d}°. What is the bearing of P from Q?", (b + 180) % 360, "°", units=["°"], o="O1", d="H", reason=f"{b} {'+' if b < 180 else '−'} 180 = {(b + 180) % 360:03d}°.")


s.std([b4, b8, b1, b2, b3, b5, b6, b7], EX("Explain why the bearing of A from B is 180° more than the bearing of B from A when the first bearing is less than 180°.", [("the two directions are opposite", ["opposite|reverse|back"]), ("opposite directions differ by 180°", ["180"])], "Going from B back to A is the exact opposite direction, and opposite directions differ by 180°. So you add 180° (or subtract it if the bearing is 180° or more).", o="O1"),
      deep=[k141])

# ================================================================== 14.2
s = U.section("14.2", "The midpoint of a line segment", ["O2"])
s.idea("Midpoint", ["The **midpoint** is halfway along a line segment. Find the **mean of the x-coordinates** and the **mean of the y-coordinates**.",
       "The midpoint of (2, 3) and (8, 11) is ((2 + 8) ÷ 2, (3 + 11) ÷ 2) = (5, 7)."], fig={"kind": "coord", "x": [0, 9], "y": [0, 12], "segs": [[2, 3, 8, 11]], "points": [{"x": 2, "y": 3, "l": "A"}, {"x": 8, "y": 11, "l": "B"}, {"x": 5, "y": 7, "l": "M"}]})
s.check(S("Find the midpoint of (−2, 4) and (6, 0).", PACC((2, 2)), o="O2"))
s.idea("Why the midpoint is an average", ["Halfway between x = 2 and x = 8 is 5, the mean of 2 and 8. The midpoint of a line segment takes the mean of the x-coordinates and the mean of the y-coordinates.",
       "Midpoint of (x₁, y₁) and (x₂, y₂) = ((x₁ + x₂)/2, (y₁ + y₂)/2)."])
s.mistake("Add, then halve", ["Add the x-coordinates (do not subtract), then divide by 2."])


def m1(r):
    a, b = [r.randint(-6, 8), r.randint(-6, 8)], [r.randint(-6, 8), r.randint(-6, 8)]
    if (a[0] + b[0]) % 2 or (a[1] + b[1]) % 2: b[0] += (a[0] + b[0]) % 2; b[1] += (a[1] + b[1]) % 2
    m = ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2)
    return S(f"Find the midpoint of {pt(a)} and {pt(b)}.", PACC(m), o="O2", reason=f"(({a[0]} + {b[0]}) ÷ 2, ({a[1]} + {b[1]}) ÷ 2) = {pt(m)}.")
def m2(r):
    a = [r.randint(-5, 5), r.randint(-5, 5)]; m = [r.randint(-5, 5), r.randint(-5, 5)]; b = [2 * m[0] - a[0], 2 * m[1] - a[1]]
    return S(f"M {pt(m)} is the midpoint of AB. A is {pt(a)}. Find B.", PACC(b), o="O2", d="H", reason=f"B = (2 × {m[0]} − {a[0]}, 2 × {m[1]} − {a[1]}) = {pt(b)}.")
def m3(r):
    a, b = [r.randint(0, 4), r.randint(0, 4)], [r.randint(5, 9), r.randint(5, 9)]
    if (a[0] + b[0]) % 2: b[0] += 1
    if (a[1] + b[1]) % 2: b[1] += 1
    m = ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2)
    return TB("Find the midpoint of the line segment AB shown.", ["Coordinate", "Midpoint"], [["x", B(m[0])], ["y", B(m[1])]], o="O2", fig={"kind": "coord", "x": [0, 10], "y": [0, 10], "segs": [[a[0], a[1], b[0], b[1]]], "points": [{"x": a[0], "y": a[1], "l": "A"}, {"x": b[0], "y": b[1], "l": "B"}]})
def m4(r):
    a = r.randint(-8, 2); b = a + 2 * r.randint(2, 8)
    return N(f"Find the x-coordinate of the midpoint of ({a}, 3) and ({b}, 3).", (a + b) // 2, o="O2", reason=f"({a} + {b}) ÷ 2 = {(a + b) // 2}.", fig={"kind": "coord", "x": [min(a, 0) - 1, b + 1], "y": [0, 5], "segs": [[a, 3, b, 3]], "points": [{"x": a, "y": 3, "l": "A"}, {"x": b, "y": 3, "l": "B"}]})
def m5(r):
    a, b = [r.randint(-5, 5), r.randint(-5, 5)], [r.randint(-5, 5), r.randint(-5, 5)]
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    return MC(f"Which is the midpoint of {pt(a)} and {pt(b)}?", f"({fmt(m[0])}, {fmt(m[1])})", [f"({fmt((b[0] - a[0]) / 2)}, {fmt((b[1] - a[1]) / 2)})", f"({a[0] + b[0]}, {a[1] + b[1]})", f"({fmt(m[1])}, {fmt(m[0])})"], o="O2") if m[0] != m[1] else None
def m6(r):
    x1, x2 = r.randint(0, 10), r.randint(12, 30); y = r.randint(1, 9)
    return N(f"Two towns are at ({x1}, {y}) and ({x2}, {y}) on a map grid. A café is exactly halfway between them. What is its x-coordinate?", (x1 + x2) / 2, o="O2", reason=f"({x1} + {x2}) ÷ 2 = {fmt((x1 + x2) / 2)}.")
def m7(r):
    a, b = [r.randint(-4, 4), r.randint(-4, 4)], [r.randint(-4, 4), r.randint(-4, 4)]
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    return S(f"Find the midpoint of {pt(a)} and {pt(b)}. (Use decimals if needed.)", [f"({fmt(m[0])}, {fmt(m[1])})", f"({fmt(m[0])},{fmt(m[1])})", f"{fmt(m[0])}, {fmt(m[1])}"], o="O2", d="H")


def k142(r):
    mx, my, x1, y1 = r.randint(-3, 5), r.randint(-3, 5), r.randint(-6, 2), r.randint(-6, 2)
    return MC(f"M({mx}, {my}) is the midpoint of A({x1}, {y1}) and B. Where is B?", f"({2 * mx - x1}, {2 * my - y1})", [(f"({(mx + x1) / 2:g}, {(my + y1) / 2:g})", "That is the midpoint of A and M."), (f"({mx - x1}, {my - y1})", "B is as far beyond M as A is before it.")], o="O2", d="VH",
              reason=f"From A to M: ({mx - x1}, {my - y1}); add again: B = ({2 * mx - x1}, {2 * my - y1}).") if (mx, my) != (x1, y1) else None


s.std([m3, m4, m5, m1, m2, m6, m7], EX("Explain how to find the midpoint of (1, 2) and (7, 10).", [("add the x-coordinates and halve: (1 + 7) ÷ 2 = 4", ["\\b4\\b|1 ?\\+ ?7"]), ("add the y-coordinates and halve: (2 + 10) ÷ 2 = 6", ["\\b6\\b|2 ?\\+ ?10"])], "Find the mean of each coordinate: (1 + 7) ÷ 2 = 4 and (2 + 10) ÷ 2 = 6. The midpoint is (4, 6).", o="O2"),
      deep=[k142])

# ================================================================== 14.3
s = U.section("14.3", "Translating 2D shapes", ["O3"])
s.idea("Column vectors", ["A **translation** slides a shape without turning it. A **column vector** (a over b) means move **a** right (left if negative) and **b** up (down if negative).",
       "Every point moves the same way, so the image is congruent to the object."])
s.check(S("The point (2, −1) is translated by the vector (3 over 4). Where does it go?", PACC((5, 3)), o="O3"))
s.mistake("Top number is x", ["In (a over b), the TOP number moves left or right; the BOTTOM number moves up or down."])


def tr(p, v): return [p[0] + v[0], p[1] + v[1]]


def t1(r):
    p = [r.randint(-5, 5), r.randint(-5, 5)]; v = [nz(r, -5, 5), nz(r, -5, 5)]
    return S(f"The point {pt(p)} is translated by the vector ({v[0]} over {v[1]}). Write the coordinates of its image.", PACC(tr(p, v)), o="O3", reason=f"{pt(p)} → {pt(tr(p, v))}.")
def t2(r):
    p = [r.randint(-5, 5), r.randint(-5, 5)]; v = [nz(r, -5, 5), nz(r, -5, 5)]; q = tr(p, v)
    return TB(f"A point moves from {pt(p)} to {pt(q)}. Write the translation as a column vector.", ["", "Vector"], [["top (x)", B(v[0])], ["bottom (y)", B(v[1])]], o="O3", fig={"kind": "coord", "x": [-10, 10], "y": [-10, 10], "points": [{"x": p[0], "y": p[1], "l": "P"}, {"x": q[0], "y": q[1], "l": "P′"}]})
def t3(r):
    T = tri(r); v = [nz(r, -4, 4), nz(r, -4, 4)]; I = [tr(p, v) for p in T]
    return MC("Triangle A is translated to triangle B. Which vector describes the translation?", f"({v[0]} over {v[1]})", [f"({v[1]} over {v[0]})", f"({-v[0]} over {-v[1]})", f"({v[0]} over {-v[1]})"], o="O3", fig={"kind": "coord", "x": [-8, 8], "y": [-8, 8], "polys": [{"pts": T, "l": "A"}, {"pts": I, "l": "B"}]}) if v[0] != v[1] else None
def t4(r):
    v = [nz(r, -5, 5), nz(r, -5, 5)]
    return S(f"A shape is translated by ({v[0]} over {v[1]}). Which vector translates it back to where it started?", [f"({-v[0]} over {-v[1]})", f"{-v[0]} over {-v[1]}", f"({-v[0]},{-v[1]})", f"({-v[0]}, {-v[1]})"], o="O3", reason="Reverse both numbers.")
def t5(r):
    v1, v2 = [nz(r, -4, 4), nz(r, -4, 4)], [nz(r, -4, 4), nz(r, -4, 4)]
    return TB(f"A shape is translated by ({v1[0]} over {v1[1]}) and then by ({v2[0]} over {v2[1]}). Write the single vector for both moves.", ["", "Vector"], [["top (x)", B(v1[0] + v2[0])], ["bottom (y)", B(v1[1] + v2[1])]], o="O3", d="H")
def t6(r):
    rows = [("Translation", "Same size, same way round"), ("Reflection", "Flipped over a mirror line"), ("Rotation", "Turned about a point"), ("Enlargement", "Size changes")]
    return GD("What does each transformation do?", "Effect", rows, o="O3")
def t7(r):
    p = [r.randint(-5, 5), r.randint(-5, 5)]; v = [nz(r, -5, 5), nz(r, -5, 5)]
    return N(f"The point {pt(p)} is translated by ({v[0]} over {v[1]}). What is the y-coordinate of its image?", p[1] + v[1], o="O3", reason=f"{p[1]} + ({v[1]}) = {p[1] + v[1]}.")


s.std([t2, t3, t1, t4, t6, t7, t5], EX("Explain why a translated shape is congruent to the original.", [("every point moves the same distance in the same direction", ["same distance|same direction|same way|every point"]), ("so lengths and angles do not change", ["length|angle|size|shape|not change|doesn't change"])], "In a translation every point slides the same distance in the same direction, so the shape is not stretched, turned or flipped: lengths and angles stay the same.", o="O3"))

# ================================================================== 14.4
s = U.section("14.4", "Reflecting shapes", ["O4"])
s.idea("Mirror lines", ["In a **reflection** each image point is the same distance from the mirror line as the object point, on the other side.",
       "Reflect in the **x-axis**: (x, y) → (x, −y). In the **y-axis**: (x, y) → (−x, y). In **y = x**: (x, y) → (y, x)."], fig={"kind": "coord", "x": [-5, 5], "y": [-5, 5], "lines": [{"m": 1, "c": 0, "label": "y = x"}], "polys": [{"pts": [[1, 3], [2, 3], [1, 4]], "l": "A"}, {"pts": [[3, 1], [3, 2], [4, 1]], "l": "B"}]})
s.check(S("Reflect the point (4, −2) in the y-axis.", PACC((-4, -2)), o="O4"))
s.mistake("Measure at right angles", ["Measure distances to the mirror line at right angles to it, especially for diagonal mirror lines."])


def f1(r):
    p = [nz(r, -6, 6), nz(r, -6, 6)]; m = pick(r, [("the x-axis", (p[0], -p[1])), ("the y-axis", (-p[0], p[1])), ("the line y = x", (p[1], p[0]))])
    return S(f"Reflect the point {pt(p)} in {m[0]}.", PACC(m[1]), o="O4", reason=f"{pt(p)} → {pt(m[1])}.")
def f2(r):
    k = nz(r, -4, 4); p = [r.randint(-6, 6), r.randint(-6, 6)]
    if p[0] == k: return None
    return S(f"Reflect the point {pt(p)} in the line x = {k}.", PACC((2 * k - p[0], p[1])), o="O4", d="H", fig={"kind": "coord", "x": [-8, 8], "y": [-8, 8], "lines": [{"x": k, "label": f"x = {k}"}], "points": [{"x": p[0], "y": p[1], "l": "P"}]}, reason=f"{abs(p[0] - k)} units from the line, so x = {2 * k - p[0]}.")
def f3(r):
    T = tri(r, 1, 3); I = [[x, -y] for x, y in T]
    return MC("Shape A is reflected onto shape B. What is the mirror line?", "the x-axis", ["the y-axis", "y = x", "x = 1"], o="O4", fig={"kind": "coord", "x": [-6, 6], "y": [-7, 7], "polys": [{"pts": T, "l": "A"}, {"pts": I, "l": "B"}]})
def f4(r):
    k = nz(r, -4, 4); p = [r.randint(-6, 6), r.randint(-6, 6)]
    if p[1] == k: return None
    return N(f"The point {pt(p)} is reflected in the line y = {k}. What is the y-coordinate of the image?", 2 * k - p[1], o="O4", d="H", reason=f"{abs(p[1] - k)} units from y = {k}: image at y = {2 * k - p[1]}.")
def f5(r):
    T = tri(r, 1, 3); I = [[y, x] for x, y in T]
    return TB("Triangle A is reflected in the line y = x. Write the coordinates of the image of the first vertex.", ["Coordinate", "Value"], [["x", B(I[0][0])], ["y", B(I[0][1])]], o="O4", d="H", fig={"kind": "coord", "x": [-1, 7], "y": [-1, 7], "lines": [{"m": 1, "c": 0, "label": "y = x"}], "polys": [{"pts": T, "l": "A"}]}, data={"head": ["Vertex", "1st"], "rows": [["A", pt(T[0])]]})
def f6(r):
    rows = [("(x, y) → (x, −y)", "x-axis"), ("(x, y) → (−x, y)", "y-axis"), ("(x, y) → (y, x)", "y = x")]
    return GD("Which mirror line gives each rule?", "Mirror line", rows, o="O4", extra=["y = −x"])
def f7(r):
    p = [nz(r, -6, 6), nz(r, -6, 6)]
    return MC(f"Which point is the reflection of {pt(p)} in the x-axis?", pt((p[0], -p[1])), [pt((-p[0], p[1])), pt((-p[0], -p[1])), pt((p[1], p[0]))], o="O4") if len({pt((p[0], -p[1])), pt((-p[0], p[1])), pt((-p[0], -p[1])), pt((p[1], p[0]))}) == 4 else None


s.std([f3, f6, f1, f2, f4, f5, f7], EX("Explain how to reflect a point in the line y = x.", [("swap the x- and y-coordinates", ["swap|switch|exchange|reverse"]), ("e.g. (2, 5) → (5, 2)", ["\\(5, ?2\\)|example|y, x"])], "Reflecting in y = x swaps the coordinates: (x, y) → (y, x). For example, (2, 5) → (5, 2).", o="O4"))

# ================================================================== 14.5
s = U.section("14.5", "Rotating shapes", ["O5"])
s.idea("Rotation", ["A **rotation** turns a shape about a **centre of rotation** through an **angle**, clockwise or anticlockwise. Tracing paper helps.",
       "About the origin: 90° clockwise (x, y) → (y, −x); 180° (x, y) → (−x, −y); 90° anticlockwise (x, y) → (−y, x)."])
s.check(S("Rotate the point (3, 1) through 180° about the origin.", PACC((-3, -1)), o="O5"))
s.mistake("Say all three", ["To describe a rotation give the centre, the angle and the direction."])


def ro1(r):
    p = [nz(r, -6, 6), nz(r, -6, 6)]; k = pick(r, [("90° clockwise", (p[1], -p[0])), ("180°", (-p[0], -p[1])), ("90° anticlockwise", (-p[1], p[0]))])
    return S(f"Rotate the point {pt(p)} {k[0]} about the origin.", PACC(k[1]), o="O5", d="M" if k[0] == "180°" else "H", reason=f"{pt(p)} → {pt(k[1])}.")
def ro2(r):
    return MC("To describe a rotation fully, you must give…", "the centre, the angle and the direction", [("the vector", "That describes a translation."), ("the mirror line", "That describes a reflection."), ("the scale factor", "That describes an enlargement.")], o="O5")
def ro3(r):
    T = tri(r, 1, 3); I = [[-x, -y] for x, y in T]
    return MC("Shape A is rotated onto shape B about the origin. What is the angle of rotation?", "180°", ["90° clockwise", "90° anticlockwise", "360°"], o="O5", fig={"kind": "coord", "x": [-7, 7], "y": [-7, 7], "polys": [{"pts": T, "l": "A"}, {"pts": I, "l": "B"}]})
def ro4(r):
    a = pick(r, [90, 180, 270]); d = pick(r, ["clockwise", "anticlockwise"])
    eq = 360 - a
    return S(f"A rotation of {a}° {d} has the same effect as a rotation of how many degrees {'anticlockwise' if d == 'clockwise' else 'clockwise'}?", [str(eq), f"{eq}°"], o="O5", reason=f"360 − {a} = {eq}.")
def ro5(r):
    T = tri(r, 1, 3); I = [[y, -x] for x, y in T]
    return TB("Triangle A is rotated 90° clockwise about the origin. Write the image of the first vertex.", ["Coordinate", "Value"], [["x", B(I[0][0])], ["y", B(I[0][1])]], o="O5", d="H", fig={"kind": "coord", "x": [-6, 6], "y": [-6, 6], "polys": [{"pts": T, "l": "A"}]}, data={"head": ["Vertex", "1st"], "rows": [["A", pt(T[0])]]})
def ro6(r):
    rows = [("90° clockwise", "(x, y) → (y, −x)"), ("180°", "(x, y) → (−x, −y)"), ("90° anticlockwise", "(x, y) → (−y, x)")]
    return GD("Match each rotation about the origin with its rule.", "Rule", rows, o="O5", d="H")
def ro7(r):
    n = pick(r, [2, 3, 4, 5, 6, 8])
    return N(f"A shape fits onto itself {n} times in a full turn. Through what angle must it be rotated to fit onto itself once?", 360 // n, "°", units=["°"], o="O5", reason=f"360 ÷ {n} = {360 // n}°.")


s.std([ro3, ro5, ro1, ro2, ro4, ro6, ro7], EX("Explain why a rotation of 270° clockwise is the same as 90° anticlockwise.", [("a full turn is 360°", ["360"]), ("360° − 270° = 90° the other way", ["90|other way|opposite direction"])], "A full turn is 360°. Turning 270° clockwise leaves you 90° short of a full turn, which is the same as turning 90° anticlockwise.", o="O5"))

# ================================================================== 14.6
s = U.section("14.6", "Enlarging shapes", ["O6"])
s.idea("Enlargement", ["An **enlargement** changes the size of a shape. Every length is multiplied by the **scale factor**; angles do not change.",
       "From a **centre of enlargement**, each image point is (scale factor) times as far from the centre as the object point."], fig={"kind": "coord", "x": [0, 10], "y": [0, 8], "polys": [{"pts": [[1, 1], [3, 1], [1, 2]], "l": "A"}, {"pts": [[1, 1], [7, 1], [1, 4]], "l": "B"}]})
s.check(N("A rectangle 2 cm by 5 cm is enlarged by scale factor 3. What is the length of the longer side of the image?", 15, "cm", units=["cm"], o="O6"))
s.check(MC("Before you read on: a shape is enlarged by scale factor 1/2. Is the image bigger or smaller?", "Smaller", [("Bigger", "Every length is halved."), ("The same", "Only scale factor 1 keeps the size.")], o="O6"))
s.mistake("Area is not × scale factor", ["Scale factor 2 doubles every length, but the area becomes 4 times as big."])


def n1(r):
    a, b, k = r.randint(2, 9), r.randint(2, 9), r.randint(2, 5)
    return TB(f"A rectangle {a} cm by {b} cm is enlarged by scale factor {k}. Complete the table.", ["", "Image"], [["Width (cm)", B(a * k)], ["Height (cm)", B(b * k)]], o="O6", fig={"kind": "shape", "pts": [[0, 0], [a, 0], [a, b], [0, b]], "s": [f"{a} cm", f"{b} cm", "", ""]})
def n2(r):
    a, k = r.randint(2, 12), r.randint(2, 5)
    return N(f"A shape is enlarged. A side of {a} cm becomes {a * k} cm. What is the scale factor?", k, o="O6", reason=f"{a * k} ÷ {a} = {k}.")
def n3(r):
    p = [r.randint(1, 4), r.randint(1, 4)]; k = r.randint(2, 3)
    return S(f"The point {pt(p)} is enlarged by scale factor {k} with centre the origin. Where is its image?", PACC((p[0] * k, p[1] * k)), o="O6", reason=f"Multiply each coordinate by {k}.")
def n4(r):
    c = [r.randint(0, 3), r.randint(0, 3)]; p = [c[0] + r.randint(1, 3), c[1] + r.randint(1, 3)]; k = r.randint(2, 3)
    q = (c[0] + k * (p[0] - c[0]), c[1] + k * (p[1] - c[1]))
    return S(f"The point {pt(p)} is enlarged by scale factor {k} with centre {pt(c)}. Where is its image?", PACC(q), o="O6", d="H", reason=f"From the centre: ({p[0] - c[0]}, {p[1] - c[1]}) × {k} → {pt(q)}.")
def n5(r):
    a, k = r.randint(30, 120), r.randint(2, 4)
    return N(f"A triangle has an angle of {a}°. It is enlarged by scale factor {k}. What is the size of that angle in the image?", a, "°", units=["°"], o="O6", reason="Enlargement does not change angles.")
def n6(r):
    k = r.randint(2, 4); s_ = r.randint(2, 6)
    return N(f"A square of side {s_} cm is enlarged by scale factor {k}. How many times bigger is its area?", k * k, o="O6", d="H", reason=f"Area: {s_ * s_} → {(s_ * k) ** 2} cm², {k * k} times bigger.")
def n7(r):
    T = [[1, 1], [3, 1], [1, 3]]; k = r.randint(2, 3); I = [[x * k, y * k] for x, y in T]
    return N("Shape A is enlarged to shape B with centre the origin. What is the scale factor?", k, o="O6", fig={"kind": "coord", "x": [0, 10], "y": [0, 10], "polys": [{"pts": T, "l": "A"}, {"pts": I, "l": "B"}]})


def k146(r):
    k = pick(r, [2, 3, 0.5]); a = r.randint(2, 8) * 2
    return N(f"A rectangle {a} cm by 4 cm is enlarged by scale factor {k:g}. What is the new perimeter?", round(2 * (a + 4) * k, 2), "cm", units=["cm"], o="O6", d="H", reason=f"Old perimeter {2 * (a + 4)} cm; every length × {k:g}, so the perimeter × {k:g}.")


s.std([n1, n7, n2, n3, n4, n5, n6], EX("Explain why enlarging a shape by scale factor 2 does not double its area.", [("both the length and the width double", ["both|length and width|each length|every length"]), ("so the area is 2 × 2 = 4 times bigger", ["4|four|2 ?× ?2"])], "Every length doubles, so a rectangle's length and width both double. The area becomes 2 × 2 = 4 times as big.", o="O6"),
      deep=[k146])

U.mindmap(("Bearings", "Clockwise from north • three figures • back bearing ±180°", "O1", "14.1"), ("Midpoint", "Mean of the x's, mean of the y's", "O2", "14.2"),
          ("Translation", "Column vector (right/left over up/down)", "O3", "14.3"), ("Reflection", "x-axis (x, −y) • y-axis (−x, y) • y = x (y, x)", "O4", "14.4"),
          ("Rotation", "Centre, angle, direction", "O5", "14.5"), ("Enlargement", "Scale factor × lengths • angles unchanged • centre", "O6", "14.6"))
