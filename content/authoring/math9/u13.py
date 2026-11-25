# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 13 Position and transformation. Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(13, "Position and transformation", "Geometry and measure",
         "Bearings and scale drawings, midpoints and points dividing a line segment, combined transformations and enlargement.",
         {"O1": {"sec": "13.1", "code": "9Gp.01", "codeNote": "", "t": "Use bearings (three figures, measured clockwise from north) and scale drawings, including back bearings."},
          "O2": {"sec": "13.2", "code": "9Gp.02", "codeNote": "", "t": "Find the midpoint of a line segment and the point that divides it in a given ratio."},
          "O3": {"sec": "13.3", "code": "9Gp.03", "codeNote": "", "t": "Describe and carry out reflections, rotations and translations, including combinations."},
          "O4": {"sec": "13.4", "code": "9Gp.04", "codeNote": "", "t": "Enlarge shapes using a positive scale factor and a centre; find scale factors and centres."}})

def br(v): return f"{int(v) % 360:03d}°"

# ================================================================== 13.1
s = U.section("13.1", "Bearings and scale drawings", ["O1"])
s.idea("Bearings", ["A **bearing** is an angle measured **clockwise from north**, written with **three figures**: 045°, 230°.",
       "The **back bearing** (from B back to A) is the bearing **± 180°**."], fig={"kind": "bearing", "bearing": 65, "from": "A", "to": "B"})
s.example("Back bearing", "The bearing of B from A is 065°. Find the bearing of A from B.", [("065 + 180 = 245", "")], "245°")
s.check(N("The bearing of Q from P is 310°. Find the bearing of P from Q, in degrees.", 130, "°", units=["°"], reason="310 − 180 = 130, so the bearing is 130°.", o="O1"))
s.idea("Scale drawings", ["A scale such as **1 cm : 5 km** means every 1 cm on the drawing is 5 km in real life. Multiply to get the real length; divide to get the drawing length."])
s.check(MC("Before you read on: B is on a bearing of 120° from A. What is the bearing of A from B?", "300°", [("120°", "Going back is the opposite direction."), ("060°", "Add 180°.")], o="O1"))
s.mistake("Three figures", ["A bearing of 45° is written 045°. Always measure from NORTH and go CLOCKWISE."])
s.check(N("A plan uses 1 cm : 2.5 m. A wall is 7.4 cm on the plan. How long is the real wall in metres?", 18.5, "m", units=["m"], reason="7.4 × 2.5 = 18.5 m.", o="O1"))
def b1(r):
    v = r.randint(5, 355)
    return N(f"The bearing of B from A is {br(v)}. Find the bearing of A from B.", (v + 180) % 360, "°", units=["°"], reason=f"Back bearing = {v} {'+' if v < 180 else '−'} 180 = {br((v + 180) % 360)}.", o="O1", fig={"kind": "bearing", "bearing": v})
def b2(r):
    d = pick(r, [("north", 0), ("east", 90), ("south", 180), ("west", 270), ("north-east", 45), ("south-west", 225), ("south-east", 135), ("north-west", 315)])
    return N(f"What is the three-figure bearing of {d[0]}? Give the number of degrees.", d[1], "°", units=["°"], reason=f"Measure clockwise from north: {d[0]} is {br(d[1])}.", o="O1")
def b3(r):
    sc, d = pick(r, [(2, "km"), (5, "km"), (10, "km"), (50, "m"), (20, "m")]), round(r.uniform(2, 12), 1)
    sc, u = sc
    return N(f"A map uses the scale 1 cm : {sc} {u}. Two points are {d} cm apart on the map. Find the real distance.", round(d * sc, 2), u, units=[u], reason=f"{d} × {sc} = {fmt(round(d * sc, 2))} {u}.", o="O1")
def b4(r):
    sc = pick(r, [4, 5, 8, 20, 25]); real = r.randint(3, 40) * sc / 5
    return N(f"A scale drawing uses 1 cm : {sc} m. A field is {fmt(real)} m long. How long is it on the drawing, in cm?", round(real / sc, 3), "cm", units=["cm"], reason=f"{fmt(real)} ÷ {sc} = {fmt(round(real / sc, 3))} cm.", o="O1", tol=0.006)
def b5(r):
    v = r.randint(10, 170)
    return MC(f"A ship sails on a bearing of {br(v)}. Which direction is it roughly heading?", "east of north" if v < 90 else ("east" if v == 90 else "east of south"),
              [("west of north", ""), ("west of south", ""), ("due north", "")], o="O1", d="M") if v != 90 else None
def b6(r):
    v = r.randint(20, 160); w = r.randint(v + 20, 340)
    return N(f"From a lighthouse L, ship A is on a bearing of {br(v)} and ship B on {br(w)}. Find the angle ALB.", min(w - v, 360 - (w - v)), "°", units=["°"], reason=f"{w} − {v} = {w - v}°" + (f"; the angle is the smaller side: 360 − {w - v} = {360 - (w - v)}°." if w - v > 180 else "."), o="O1", d="H")
def b7(r):
    a, b = r.randint(3, 12), r.randint(3, 12)
    return N(f"A boat sails {a} km due north, then {b} km due east. How far is it from the start? (1 d.p.)", round((a * a + b * b) ** 0.5, 1), "km", units=["km"], tol=0.06, reason=f"Pythagoras: √({a}² + {b}²) = √{a * a + b * b} = {round((a * a + b * b) ** 0.5, 1)} km.", o="O1", d="H")
s.core(b1(s.rng), b2(s.rng), b3(s.rng), b4(s.rng), b6(s.rng), b7(s.rng),
       OD("Order these bearings from north going clockwise.", ["030°", "095°", "180°", "265°", "340°"], o="O1", skill="Data"),
       EX("Explain how to find a back bearing.", [("add or subtract 180°", ["180"]), ("keep it between 000° and 360°", ["less than 360|subtract if|over 360|between|three figures|if .*more"])], "Add 180° to the bearing. If the answer is 360° or more, subtract 180° instead (or subtract 360°).", o="O1"))
def m1_1(r):
    b = r.randint(10, 350)
    return N(f"The bearing of Y from X is {b:03d}°. Find the bearing of X from Y.", (b + 180) % 360, "°", units=["°"], o="O1", d="H", reason=f"{b} ± 180 = {(b + 180) % 360:03d}°.")


s.gen("p", 44, b1, b2, b3, b4, b5, b6, b7)
s.capped("p", [1] * 1, [m1_1]).capped("m", [2] * 1, [m1_1])   # v2 reasoning kinds
s.gen("a", 8, b7, b6, lambda r: (lambda a: N(f"Town B is {a} km due east of A. Town C is due north of B and on a bearing of 045° from A. How far is A from C? (1 d.p.)", round(a * 2 ** 0.5, 1), "km", units=["km"], tol=0.06, reason=f"Bearing 045° makes a right-angled isosceles triangle, so BC = {a} km and AC = √({a}² + {a}²) = {round(a * 2 ** 0.5, 1)} km.", o="O1", d="VH"))(r.randint(4, 30)))

# ================================================================== 13.2
s = U.section("13.2", "Points on a line segment", ["O2"])
s.idea("Midpoints", ["The **midpoint** of (x₁, y₁) and (x₂, y₂) is **((x₁ + x₂)/2, (y₁ + y₂)/2)** – the mean of the coordinates."],
       fig={"kind": "coord", "x": [-1, 9], "y": [-1, 8], "points": [{"x": 1, "y": 2, "l": "A"}, {"x": 7, "y": 6, "l": "B"}, {"x": 4, "y": 4, "l": "M"}], "segs": [[1, 2, 7, 6]]})
s.example("Midpoint", "Find the midpoint of A(1, 2) and B(7, 6).", [("x: (1 + 7) ÷ 2 = 4", ""), ("y: (2 + 6) ÷ 2 = 4", "")], "(4, 4)")
s.check(TB("Find the midpoint of (−3, 5) and (9, −1).", ["x", "y"], [[B(3), B(2)]], reason="x: (−3 + 9) ÷ 2 = 3; y: (5 + (−1)) ÷ 2 = 2.", o="O2"))
s.idea("Dividing in a ratio", ["To find P on AB with **AP : PB = m : n**, go the fraction **m/(m + n)** of the way from A: P = A + m/(m + n) × (B − A)."])
s.mistake("Fraction of the way", ["For AP : PB = 1 : 3, P is 1/4 of the way along, not 1/3."])
s.check(TB("A(0, 0), B(12, 8). P is on AB with AP : PB = 1 : 3. Find P.", ["x", "y"], [[B(3), B(2)]], reason="P is 1/4 of the way: (12 ÷ 4, 8 ÷ 4) = (3, 2).", o="O2", d="H"))
def d1(r):
    x1, y1, x2, y2 = [r.randint(-9, 9) for _ in range(4)]
    return TB(f"Find the midpoint of ({x1}, {y1}) and ({x2}, {y2}).", ["x", "y"], [[B((x1 + x2) / 2), B((y1 + y2) / 2)]], reason=f"x: ({x1} + {x2}) ÷ 2 = {fmt((x1 + x2) / 2)}; y: ({y1} + {y2}) ÷ 2 = {fmt((y1 + y2) / 2)}.", o="O2")
def d2(r):
    x1, y1, mx, my = [r.randint(-6, 6) for _ in range(4)]
    return TB(f"M({mx}, {my}) is the midpoint of AB. A is ({x1}, {y1}). Find B.", ["x", "y"], [[B(2 * mx - x1), B(2 * my - y1)]], reason=f"B is as far beyond M as A is before it: x = 2 × {mx} − {x1} = {2 * mx - x1}, y = 2 × {my} − {y1} = {2 * my - y1}.", o="O2", d="H")
def d3(r):
    m, n = pick(r, [(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 4)]); k = m + n
    x1, y1 = r.randint(-5, 5), r.randint(-5, 5); dx, dy = k * r.randint(-3, 4), k * r.randint(-3, 4)
    if dx == 0 and dy == 0: return None
    x2, y2 = x1 + dx, y1 + dy
    return TB(f"A({x1}, {y1}), B({x2}, {y2}). P is on AB with AP : PB = {m} : {n}. Find P.", ["x", "y"], [[B(x1 + dx * m // k), B(y1 + dy * m // k)]], reason=f"P is {m}/{k} of the way from A: x = {x1} + {m}/{k} × {dx} = {x1 + dx * m // k}, y = {y1} + {m}/{k} × {dy} = {y1 + dy * m // k}.", o="O2", d="H",
              fig={"kind": "coord", "x": [min(x1, x2) - 1, max(x1, x2) + 1], "y": [min(y1, y2) - 1, max(y1, y2) + 1], "points": [{"x": x1, "y": y1, "l": "A"}, {"x": x2, "y": y2, "l": "B"}], "segs": [[x1, y1, x2, y2]]})
def d4(r):
    x1, y1 = r.randint(-5, 5), r.randint(-5, 5); a, b = pick(r, [(3, 4), (6, 8), (5, 12), (8, 6), (12, 5)])
    return N(f"Find the length of the line segment from ({x1}, {y1}) to ({x1+a}, {y1+b}).", (a * a + b * b) ** 0.5, "units", units=["units"], reason=f"Across {a}, up {b}: √({a}² + {b}²) = √{a * a + b * b} = {fmt((a * a + b * b) ** 0.5)}.", o="O2", d="H")
def d5(r):
    x1, y1, x2, y2 = [r.randint(-8, 8) for _ in range(4)]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    wrong = (x2 - x1) / 2, (y2 - y1) / 2
    if wrong == (mx, my): return None
    return MC(f"Which is the midpoint of ({x1}, {y1}) and ({x2}, {y2})?", f"({fmt(mx)}, {fmt(my)})", [(f"({fmt(wrong[0])}, {fmt(wrong[1])})", "Add the coordinates, not subtract."), (f"({x1 + x2}, {y1 + y2})", "Remember to halve."), (f"({fmt(my)}, {fmt(mx)})" if mx != my else f"({fmt(mx+1)}, {fmt(my)})", "")], o="O2")
s.core(d1(s.rng), d2(s.rng), d3(s.rng) or d3(s.rng), d4(s.rng), d5(s.rng) or d5(s.rng), d1(s.rng),
       TB("A(2, 1), B(10, 5). Points P and Q divide AB into three equal parts (P nearer A). Find P and Q.", ["P x", "P y", "Q x", "Q y"], [[B(14 / 3, 0.01), B(7 / 3, 0.01), B(22 / 3, 0.01), B(11 / 3, 0.01)]], reason="Each third is (8 ÷ 3, 4 ÷ 3) along. P = (2 + 8/3, 1 + 4/3) = (14/3, 7/3); Q = (2 + 16/3, 1 + 8/3) = (22/3, 11/3).", o="O2", d="VH", hint="Give answers to 2 d.p. or as fractions."),
       EX("Explain how to find the midpoint of two points.", [("add the x-coordinates and halve", ["add|sum|mean|average"]), ("do the same for the y-coordinates", ["y|same|both"])], "Add the two x-coordinates and halve, then add the two y-coordinates and halve. These give the midpoint.", o="O2"))
s.gen("p", 44, d1, d2, d3, d4, d5)
s.gen("a", 8, d3, d2, lambda r: (lambda k: TB(f"A(0, 0), B({5*k}, {5*k}). P is on AB extended beyond B so that AB : BP = 5 : 2. Find P.", ["x", "y"], [[B(7 * k), B(7 * k)]], reason=f"BP is 2/5 of AB, so P = B + 2/5 of ({5 * k}, {5 * k}) = ({7 * k}, {7 * k}).", o="O2", d="VH"))(r.randint(1, 6)))

# ================================================================== 13.3
s = U.section("13.3", "Transformations", ["O3"])
s.idea("Describing transformations", ["**Reflection**: give the mirror line (e.g. y = x). **Rotation**: give the **angle, direction and centre**. **Translation**: give the **column vector** (right, up).",
       "Reflections and rotations keep size and shape: the image is **congruent**."],
       fig={"kind": "coord", "x": [-6, 6], "y": [-6, 6], "polys": [{"pts": [[1, 1], [4, 1], [1, 3]], "l": "A"}, {"pts": [[-1, 1], [-4, 1], [-1, 3]], "l": "B"}], "lines": [{"x": 0}]})
s.example("Reflection in y = x", "Reflect the point (3, −2) in the line y = x.", [("swap the coordinates", "")], "(−2, 3)")
s.check(TB("Rotate the point (4, 1) by 90° anticlockwise about the origin.", ["x", "y"], [[B(-1), B(4)]], reason="Anticlockwise 90° about the origin: (x, y) → (−y, x), so (−1, 4).", o="O3", d="H"))
s.mistake("Complete descriptions", ["'A rotation' scores nothing on its own. Say: rotation, 90°, clockwise, centre (0, 0)."])
s.check(MC("A shape is translated by the vector (3, −2). Where does the point (1, 5) go?", "(4, 3)", [("(−2, 7)", "That subtracts the vector."), ("(4, 7)", ""), ("(3, 3)", "")], o="O3"))
T = {"refl x-axis": lambda x, y: (x, -y), "refl y-axis": lambda x, y: (-x, y), "refl y = x": lambda x, y: (y, x), "refl y = −x": lambda x, y: (-y, -x),
     "rot 90 cw": lambda x, y: (y, -x), "rot 90 acw": lambda x, y: (-y, x), "rot 180": lambda x, y: (-x, -y)}
TXT = {"refl x-axis": "reflected in the x-axis", "refl y-axis": "reflected in the y-axis", "refl y = x": "reflected in the line y = x", "refl y = −x": "reflected in the line y = −x",
       "rot 90 cw": "rotated 90° clockwise about the origin", "rot 90 acw": "rotated 90° anticlockwise about the origin", "rot 180": "rotated 180° about the origin"}
RULE = {"refl x-axis": "(x, −y)", "refl y-axis": "(−x, y)", "refl y = x": "(y, x)", "refl y = −x": "(−y, −x)", "rot 90 cw": "(y, −x)", "rot 90 acw": "(−y, x)", "rot 180": "(−x, −y)"}
def t1(r):
    k = pick(r, list(T)); x, y = nz(r, -7, 7), nz(r, -7, 7)
    a = T[k](x, y)
    return TB(f"The point ({x}, {y}) is {TXT[k]}. Find its image.", ["x", "y"], [[B(a[0]), B(a[1])]], reason=f"Rule for this transformation: (x, y) → {RULE[k]}. ({x}, {y}) → ({a[0]}, {a[1]}).", o="O3", d="M" if "refl" in k else "H")
def t2(r):
    x, y, a, b = nz(r, -6, 6), nz(r, -6, 6), nz(r, -5, 5), nz(r, -5, 5)
    return TB(f"The point ({x}, {y}) is translated by the vector ({a}, {b}). Find its image.", ["x", "y"], [[B(x + a), B(y + b)]], reason=f"Add the vector: ({x} + {a}, {y} + {b}) = ({x + a}, {y + b}).", o="O3")
def t3(r):
    k1, k2 = r.sample(list(T), 2); x, y = nz(r, -6, 6), nz(r, -6, 6)
    a = T[k2](*T[k1](x, y))
    return TB(f"The point ({x}, {y}) is {TXT[k1]}, then the image is {TXT[k2]}. Find the final image.", ["x", "y"], [[B(a[0]), B(a[1])]], reason=f"First {RULE[k1]} gives {T[k1](x, y)}; then {RULE[k2]} gives ({a[0]}, {a[1]}).", o="O3", d="H")
def t4(r):
    x, y, a, b = r.randint(-5, 5), r.randint(-5, 5), r.randint(-6, 6), r.randint(-6, 6)
    return TB(f"A translation maps ({x}, {y}) to ({x+a}, {y+b}). Write the column vector.", ["right (x)", "up (y)"], [[B(a), B(b)]], reason=f"Right: {x + a} − {x} = {a}; up: {y + b} − {y} = {b}.", o="O3")
def t5(r):
    pts = [[1, 1], [4, 1], [1, 3]]; k = pick(r, ["refl x-axis", "refl y-axis", "rot 180", "rot 90 acw", "refl y = x"])
    img = [list(T[k](*p)) for p in pts]
    names = {"refl x-axis": "Reflection in the x-axis", "refl y-axis": "Reflection in the y-axis", "rot 180": "Rotation 180° about (0, 0)", "rot 90 acw": "Rotation 90° anticlockwise about (0, 0)", "refl y = x": "Reflection in y = x"}
    wr = [v for kk, v in names.items() if kk != k][:3]
    return MC("Describe fully the single transformation that maps A onto B.", names[k], [(w, "") for w in wr], o="O3", d="H", fig={"kind": "coord", "x": [-5, 5], "y": [-5, 5], "polys": [{"pts": pts, "l": "A"}, {"pts": img, "l": "B"}]})
def t6(r):
    rows = [("Reflection", "a mirror line"), ("Rotation", "angle, direction and centre"), ("Translation", "a column vector"), ("Enlargement", "scale factor and centre")]
    return MT("Match each transformation with what you must give to describe it fully.", rows, o="O3", skill="Data")
s.core(t1(s.rng), t2(s.rng), t3(s.rng), t4(s.rng), t5(s.rng), t6(s.rng), t1(s.rng),
       EX("Explain why a reflection followed by a translation gives a congruent shape.", [("neither changes size", ["size|length"]), ("neither changes shape / angles", ["shape|angle"])], "Neither a reflection nor a translation changes lengths or angles, so the final shape has the same size and shape: it is congruent.", o="O3"))
s.gen("p", 44, t1, t2, t3, t4, t5, t6)
s.gen("a", 8, t3, lambda r: (lambda x, y: MC(f"A reflection in the x-axis followed by a reflection in the y-axis is the same as which single transformation? (Test with ({x}, {y}).)", "Rotation 180° about (0, 0)", [("Reflection in y = x", ""), ("Rotation 90° clockwise about (0, 0)", ""), ("Translation", "")], o="O3", d="VH"))(nz(r, -5, 5), nz(r, -5, 5)),
      lambda r: (lambda x, y, k: TB(f"The point ({x}, {y}) is rotated 90° clockwise about the point ({k}, 0). Find its image.", ["x", "y"], [[B(k + y), B(-(x - k))]], reason=f"Move the centre to the origin: ({x - k}, {y}). Clockwise 90°: (x, y) → (y, −x) gives ({y}, {-(x - k)}). Move back: ({k + y}, {-(x - k)}).", o="O3", d="VH"))(r.randint(-5, 6), r.randint(-5, 6), r.randint(-3, 3)))

# ================================================================== 13.4
s = U.section("13.4", "Enlarging shapes", ["O4"])
s.idea("Enlargement", ["An **enlargement** changes size but not shape. Every length is multiplied by the **scale factor**.",
       "From the **centre of enlargement**, each image point is scale factor × as far away, in the same direction. Image = centre + k × (point − centre)."],
       fig={"kind": "coord", "x": [0, 10], "y": [0, 8], "polys": [{"pts": [[1, 1], [3, 1], [3, 2]], "l": "A"}, {"pts": [[1, 1], [7, 1], [7, 4]], "l": "B"}], "points": [{"x": 1, "y": 1, "l": "C"}]})
s.example("Enlarge a point", "Enlarge (4, 3) by scale factor 2, centre (1, 1).", [("vector from centre: (3, 2)", ""), ("× 2: (6, 4)", ""), ("add to centre: (7, 5)", "")], "(7, 5)")
s.check(TB("Enlarge (5, 2) by scale factor 3, centre (0, 0).", ["x", "y"], [[B(15), B(6)]], reason="Multiply each coordinate by 3: (15, 6).", o="O4"))
s.idea("Areas and enlargement", ["If lengths are multiplied by k, **areas are multiplied by k²**."])
s.idea("Why area grows by the square of the scale factor", ["Enlarge a square of side 1 by scale factor 3: its side is 3, so its area is 9 – three times as long AND three times as wide.",
       "Lengths × k, areas × k², volumes × k³."])
s.check(MC("Before you read on: a shape is enlarged by scale factor 2. Its area was 5 cm². What is it now?", "20 cm²", [("10 cm²", "Area grows by 2² = 4."), ("40 cm²", "That is the volume factor 2³.")], o="O4"))
s.mistake("Area scale factor", ["Doubling lengths does NOT double area – it multiplies area by 4."])
s.check(N("A shape of area 6 cm² is enlarged by scale factor 3. Find the new area.", 54, "cm²", units=["cm²"], reason="Areas multiply by 3² = 9: 6 × 9 = 54 cm².", o="O4", d="H"))
def g1(r):
    cx, cy, x, y, k = r.randint(-3, 3), r.randint(-3, 3), r.randint(-4, 6), r.randint(-4, 6), pick(r, [2, 3, 4])
    return TB(f"Enlarge ({x}, {y}) by scale factor {k}, centre ({cx}, {cy}).", ["x", "y"], [[B(cx + k * (x - cx)), B(cy + k * (y - cy))]], reason=f"From the centre: ({x - cx}, {y - cy}); × {k} = ({k * (x - cx)}, {k * (y - cy)}); add the centre: ({cx + k * (x - cx)}, {cy + k * (y - cy)}).", o="O4", d="H")
def g2(r):
    a, k = r.randint(2, 12), pick(r, [1.5, 2, 2.5, 3, 4])
    return N(f"A side of {a} cm is enlarged by scale factor {fmt(k)}. Find the new length.", a * k, "cm", units=["cm"], reason=f"{a} × {fmt(k)} = {fmt(a * k)} cm.", o="O4")
def g3(r):
    a, b = r.randint(2, 9), r.randint(2, 9); k = pick(r, [2, 3, 4])
    return N(f"A rectangle {a} cm by {b} cm is enlarged to {a*k} cm by {b*k} cm. What is the scale factor?", k, reason=f"{a * k} ÷ {a} = {k}.", o="O4")
def g4(r):
    A, k = r.randint(3, 20), pick(r, [2, 3, 4, 5])
    return N(f"A triangle has area {A} cm². It is enlarged by scale factor {k}. Find the area of the image.", A * k * k, "cm²", units=["cm²"], reason=f"Areas multiply by {k}² = {k * k}: {A} × {k * k} = {A * k * k} cm².", o="O4", d="H")
def g5(r):
    cx, cy, k = r.randint(0, 3), r.randint(0, 3), pick(r, [2, 3])
    pts = [[cx + 1, cy + 1], [cx + 2, cy + 1], [cx + 1, cy + 2]]; img = [[cx + k * (p[0] - cx), cy + k * (p[1] - cy)] for p in pts]
    return TB("Shape A is enlarged to give shape B. Find the scale factor and the centre of enlargement.", ["Scale factor", "Centre x", "Centre y"], [[B(k), B(cx), B(cy)]], reason=f"B's sides are {k} times A's. Lines through matching corners meet at ({cx}, {cy}).", o="O4", d="VH",
              fig={"kind": "coord", "x": [0, 10], "y": [0, 10], "polys": [{"pts": pts, "l": "A"}, {"pts": img, "l": "B"}]}, hint="Draw lines through matching corners back to where they meet.")
def g6(r):
    p, k = r.randint(10, 40), pick(r, [2, 3, 1.5])
    return N(f"A shape has perimeter {p} cm. It is enlarged by scale factor {fmt(k)}. Find the new perimeter.", p * k, "cm", units=["cm"], reason=f"Lengths multiply by {fmt(k)}: {p} × {fmt(k)} = {fmt(p * k)} cm.", o="O4")
def g7(r):
    rows = [("Lengths", "× k"), ("Angles", "stay the same"), ("Areas", "× k²"), ("Perimeter", "× k")]
    return MT("When a shape is enlarged by scale factor k, what happens to each?", rows, o="O4")
s.core(g1(s.rng), g2(s.rng), g3(s.rng), g4(s.rng), g5(s.rng), g6(s.rng), g7(s.rng),
       EX("Explain why the angles in a shape do not change when it is enlarged.", [("all lengths multiplied by the same factor", ["same|all|every|scale factor"]), ("so the shape (and angles) stay the same / similar", ["shape|similar|same angle|angles stay"])], "Every length is multiplied by the same scale factor, so the shape stays the same and only the size changes. The angles stay the same.", o="O4"))
def m4_1(r):
    k, a = r.randint(2, 4), r.randint(2, 9)
    return N(f"A shape with area {a} cm² is enlarged by scale factor {k}. Find the new area.", a * k * k, "cm²", units=["cm²"], o="O4", d="H", reason=f"Area × {k}² = × {k * k}: {a * k * k} cm².")


s.gen("p", 44, g1, g2, g3, g4, g5, g6, g7)
s.capped("p", [1] * 1, [m4_1]).capped("m", [2] * 1, [m4_1])   # v2 reasoning kinds
s.gen("a", 8, g5, g4, lambda r: (lambda A, B_: N(f"Two similar shapes have areas {A} cm² and {A*B_*B_} cm². What is the scale factor of the enlargement?", B_, reason=f"Area factor {A * B_ * B_} ÷ {A} = {B_ * B_} = k², so k = {B_}.", o="O4", d="VH"))(r.randint(3, 15), pick(r, [2, 3, 4, 5])))

U.mindmap(("Bearings", "Clockwise from north • three figures • back bearing ± 180°", "O1", "13.1"), ("Line segments", "Midpoint = mean of coordinates • m : n → m/(m + n) of the way", "O2", "13.2"),
          ("Transformations", "Reflection: line • rotation: angle, direction, centre • translation: vector", "O3", "13.3"), ("Enlargement", "Scale factor and centre • areas × k²", "O4", "13.4"))
