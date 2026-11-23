# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 7 Shapes and measurements. Written by the Atomic teaching team."""
import math
from kit import *

U = Unit(7, "Shapes and Measurements", "Geometry",
         "Circumference and area of circles and parts of circles, areas of compound shapes, and converting between large and small units of area and volume.",
         {"O1": {"sec": "7.1", "code": "9Gg.03", "codeNote": "", "t": "Know and use the formulae for the circumference (C = πd = 2πr) and area (A = πr²) of a circle, including semicircles and quarter circles."},
          "O2": {"sec": "7.2", "code": "9Gg.04", "codeNote": "", "t": "Find the area and perimeter of compound shapes made from rectangles, triangles, trapezia and parts of circles."},
          "O3": {"sec": "7.3", "code": "9Gg.02", "codeNote": "", "t": "Convert between units of length, area (mm², cm², m², km², hectares) and volume (mm³, cm³, m³, litres)."}})
PI = math.pi
def r2(v): return round(v, 2)

# ================================================================== 7.1
s = U.section("7.1", "Circumference and area of a circle", ["O1"])
s.idea("Circle formulae", ["The **circumference** is the distance round a circle: **C = πd = 2πr**.", "The **area** is **A = πr²**. Always use the radius for the area – halve the diameter first.",
       "π ≈ 3.14159… Use the π button and round only at the end."], fig={"kind": "circle", "r": "r"})
s.example("Area from a diameter", "Find the area of a circle with diameter 12 cm, to 1 d.p.", [("r = 6 cm", "halve the diameter"), ("A = π × 6² = 36π", ""), ("= 113.1 cm²", "")], "113.1 cm²")
s.check(N("Find the circumference of a circle with radius 5 cm, to 1 d.p.", 31.4, "cm", units=["cm", "cm²"], tol=0.05, reason="C = 2πr = 2 × π × 5 = 10π ≈ 31.4 cm.", o="O1"))
s.example("Semicircle perimeter", "Find the perimeter of a semicircle with diameter 10 cm.", [("curved part = ½ × π × 10 = 15.71", ""), ("+ diameter 10", "include the straight edge"), ("= 25.71 cm", "")], "25.7 cm", fig={"kind": "circle", "part": "semi", "d": "10 cm"})
s.mistake("Diameter in the area formula", ["A = πr² uses the RADIUS. For d = 8 cm, A = π × 4² = 50.3 cm², not π × 8²."])
s.check(N("Find the area of a semicircle of radius 4 cm, to 1 d.p.", 25.1, "cm²", units=["cm²", "cm"], tol=0.05, reason="½ × π × 4² = 8π ≈ 25.1 cm².", o="O1", d="H"))
def k1(r):
    rad = r.randint(2, 30); usediam = r.random() < 0.5
    return N(f"Find the circumference of a circle with {'diameter ' + str(2*rad) if usediam else 'radius ' + str(rad)} cm, to 1 d.p.", round(2 * PI * rad, 1), "cm", units=["cm", "cm²"], tol=0.05, reason=f"C = 2πr = 2 × π × {rad} = {2 * rad}π ≈ {round(2 * PI * rad, 1)} cm.", o="O1", fig={"kind": "circle", **({"d": f"{2*rad} cm"} if usediam else {"r": f"{rad} cm"})})
def k2(r):
    rad = r.randint(2, 30); usediam = r.random() < 0.5
    return N(f"Find the area of a circle with {'diameter ' + str(2*rad) if usediam else 'radius ' + str(rad)} m, to 1 d.p.", round(PI * rad * rad, 1), "m²", units=["m²", "m"], tol=0.05, reason=f"r = {rad}; A = πr² = π × {rad}² = {rad * rad}π ≈ {round(PI * rad * rad, 1)} m².", o="O1", fig={"kind": "circle", **({"d": f"{2*rad} m"} if usediam else {"r": f"{rad} m"})})
def k3(r):
    rad = r.randint(2, 20); part = pick(r, ["semi", "quarter"]); f = 0.5 if part == "semi" else 0.25
    return N(f"Find the area of a {'semicircle' if part=='semi' else 'quarter circle'} of radius {rad} cm, to 1 d.p.", round(f * PI * rad * rad, 1), "cm²", units=["cm²", "cm"], tol=0.05, reason=f"{'½' if part == 'semi' else '¼'} × π × {rad}² ≈ {round(f * PI * rad * rad, 1)} cm².", o="O1", fig={"kind": "circle", "part": part, "r": f"{rad} cm"})
def k4(r):
    rad = r.randint(2, 20); part = pick(r, ["semi", "quarter"])
    per = PI * rad + 2 * rad if part == "semi" else 0.5 * PI * rad + 2 * rad
    return N(f"Find the perimeter of a {'semicircle' if part=='semi' else 'quarter circle'} of radius {rad} cm, to 1 d.p.", round(per, 1), "cm", units=["cm", "cm²"], tol=0.05, reason=f"Curved part {'½' if part == 'semi' else '¼'} × 2π × {rad} plus the straight edges ({2 * rad} cm): ≈ {round(per, 1)} cm.", o="O1", d="H", fig={"kind": "circle", "part": part, "r": f"{rad} cm"})
def k5(r):
    C = r.randint(20, 200)
    return N(f"A circle has circumference {C} cm. Find its radius, to 1 d.p.", round(C / (2 * PI), 1), "cm", units=["cm"], tol=0.05, reason=f"r = C ÷ (2π) = {C} ÷ (2π) ≈ {round(C / (2 * PI), 1)} cm.", o="O1", d="H")
def k6(r):
    A = r.randint(30, 900)
    return N(f"A circle has area {A} cm². Find its radius, to 1 d.p.", round(math.sqrt(A / PI), 1), "cm", units=["cm"], tol=0.05, reason=f"r = √(A ÷ π) = √({A} ÷ π) ≈ {round(math.sqrt(A / PI), 1)} cm.", o="O1", d="H")
def k7(r):
    rad = r.randint(2, 15)
    return X(f"Write the area of a circle of radius {rad} cm in terms of π (e.g. 9π).", f"{rad*rad}*pi" if False else f"{rad*rad}p", vars="p", reason=f"A = πr² = π × {rad}² = {rad * rad}π.", o="O1", show=f"{rad*rad}π", hint="Type π as p? Type the number then π, e.g. 25π.") if False else S(f"Write the area of a circle of radius {rad} cm in terms of π (e.g. 9π).", [f"{rad*rad}π", f"{rad*rad}pi", f"{rad*rad} π", f"{rad*rad}π cm²"], o="O1")
def k8(r):
    d_ = pick(r, [50, 60, 66, 70]); n = r.randint(50, 500)
    return N(f"A bike wheel has diameter {d_} cm. How far does the bike travel, in metres, when the wheel turns {n} times? (1 d.p.)", round(PI * d_ * n / 100, 1), "m", units=["m", "cm"], tol=0.05, reason=f"One turn = π × {d_} cm; {n} turns = {n} × π × {d_} ≈ {round(PI * d_ * n, 1)} cm = {round(PI * d_ * n / 100, 1)} m.", o="O1", d="H")
def k9(r):
    rows = []
    for _ in range(3):
        rad = r.randint(2, 12); rows.append([str(rad), B(2 * rad), B(round(2 * PI * rad, 1), 0.05), B(round(PI * rad * rad, 1), 0.05)])
    return TB("Complete the table (circumference and area to 1 d.p.).", ["Radius (cm)", "Diameter (cm)", "Circumference (cm)", "Area (cm²)"], rows, reason="d = 2r; C = 2πr; A = πr².", o="O1", d="H")
s.core(k1(s.rng), k2(s.rng), k3(s.rng), k4(s.rng), k5(s.rng), k9(s.rng), k7(s.rng),
       EX("Explain why doubling the radius of a circle multiplies its area by 4.", [("A = πr²", ["πr|pi ?r|r²|r\\^2|r squared"]), ("(2r)² = 4r²", ["4r|2r\\)?²|\\(2r\\)|4 ?(×|x|times)"])], "A = πr². If the radius is doubled, the area is π(2r)² = 4πr², which is 4 times as large.", o="O1", d="H"))
s.gen("p", 44, k1, k2, k3, k4, k5, k6, k7, k8, k9)
s.gen("a", 8, lambda r: (lambda R, rr: N(f"A circular path of width {R-rr} m runs around a circular pond of radius {rr} m. Find the area of the path, to 1 d.p.", round(PI * (R * R - rr * rr), 1), "m²", units=["m²", "m"], tol=0.05, reason=f"π × {R}² − π × {rr}² = π × {R * R - rr * rr} ≈ {round(PI * (R * R - rr * rr), 1)} m².", o="O1", d="VH"))(r.randint(6, 20), r.randint(3, 5)),
      lambda r: (lambda a: N(f"A sector has angle {a}° and radius 9 cm. Find its area, to 1 d.p.", round(a / 360 * PI * 81, 1), "cm²", units=["cm²", "cm"], tol=0.05, reason=f"{a}/360 × π × 9² ≈ {round(a / 360 * PI * 81, 1)} cm².", o="O1", d="VH", fig={"kind": "circle", "part": "sector", "angle": a, "r": "9 cm"}))(pick(r, [40, 60, 72, 100, 120, 150, 200, 240, 300])), k6)

# ================================================================== 7.2
s = U.section("7.2", "Areas of compound shapes", ["O2"])
s.idea("Splitting shapes", ["A **compound shape** is made of simpler shapes. **Split** it into rectangles, triangles, trapezia or parts of circles, find each area, then **add** (or **subtract** a hole).",
       "Useful formulae: rectangle lw; triangle ½bh; parallelogram bh; trapezium ½(a + b)h."])
s.example("L-shape", "An L-shape is a 10 × 8 rectangle with a 4 × 3 rectangle cut from one corner. Find its area.", [("10 × 8 = 80", "whole rectangle"), ("4 × 3 = 12", "missing corner"), ("80 − 12 = 68", "")], "68 cm²",
          fig={"kind": "shape", "pts": [[0, 0], [10, 0], [10, 5], [6, 5], [6, 8], [0, 8]], "s": ["10 cm", "5 cm", "4 cm", "3 cm", "6 cm", "8 cm"]})
s.check(N("A trapezium has parallel sides 6 cm and 10 cm and height 5 cm. Find its area.", 40, "cm²", units=["cm²", "cm"], reason="½ × (6 + 10) × 5 = 40 cm².", o="O2"))
s.example("Rectangle and semicircle", "A window is a 1.2 m by 0.8 m rectangle with a semicircle on top (diameter 0.8 m). Find the area, to 2 d.p.", [("rectangle = 0.96", ""), ("semicircle = ½ × π × 0.4² = 0.251", ""), ("total = 1.21 m²", "")], "1.21 m²")
s.mistake("Perimeter of compound shapes", ["The perimeter is only the OUTSIDE edge – do not include lines inside the shape that you drew to split it."])
s.check(MC("A square of side 10 cm has a circle of radius 3 cm cut out. How do you find the remaining area?", "100 − π × 3²", [("100 − π × 6²", "Use the radius."), ("100 + π × 3²", "The circle is cut OUT."), ("4 × 10 − 2π × 3", "That is a perimeter.")], o="O2"))
def L(r):
    W, H = r.randint(8, 16), r.randint(6, 14); w, h = r.randint(2, W - 3), r.randint(2, H - 3)
    return N("Find the area of this L-shape (lengths in cm).", W * H - w * h, "cm²", units=["cm²", "cm"], o="O2",
             fig={"kind": "shape", "pts": [[0, 0], [W, 0], [W, H - h], [W - w, H - h], [W - w, H], [0, H]], "s": [f"{W}", f"{H-h}", f"{w}", f"{h}", f"{W-w}", f"{H}"]}, reason=f"{W} × {H} − {w} × {h} = {W*H - w*h} cm².")
def Lp(r):
    W, H = r.randint(8, 16), r.randint(6, 14); w, h = r.randint(2, W - 3), r.randint(2, H - 3)
    return N("Find the perimeter of this L-shape (lengths in cm).", 2 * (W + H), "cm", units=["cm", "cm²"], o="O2", d="H",
             fig={"kind": "shape", "pts": [[0, 0], [W, 0], [W, H - h], [W - w, H - h], [W - w, H], [0, H]], "s": [f"{W}", f"{H-h}", f"{w}", f"{h}", f"{W-w}", f"{H}"]}, reason=f"The perimeter of an L-shape equals that of the full rectangle: 2({W} + {H}).")
def T(r):
    a, b, h = r.randint(3, 12), r.randint(8, 20), r.randint(3, 12)
    return N(f"A trapezium has parallel sides {a} cm and {b} cm and height {h} cm. Find its area.", 0.5 * (a + b) * h, "cm²", units=["cm²", "cm"], reason=f"½ × ({a} + {b}) × {h} = {fmt(0.5 * (a + b) * h)} cm².", o="O2", fig={"kind": "shape", "pts": [[0, 0], [b, 0], [(b + a) / 2, h], [(b - a) / 2, h]], "s": [f"{b} cm", "", f"{a} cm", ""], "note": f"height {h} cm"})
def RS(r):
    w, l = r.randint(4, 12), r.randint(6, 20)
    return N(f"A shape is a {l} cm by {w} cm rectangle with a semicircle on the {w} cm side. Find its area, to 1 d.p.", round(l * w + 0.5 * PI * (w / 2) ** 2, 1), "cm²", units=["cm²", "cm"], tol=0.05, reason=f"Rectangle {l} × {w} = {l * w}; semicircle ½ × π × {fmt(w / 2)}² ≈ {round(0.5 * PI * (w / 2) ** 2, 1)}; total ≈ {round(l * w + 0.5 * PI * (w / 2) ** 2, 1)} cm².", o="O2", d="H")
def HOLE(r):
    s_, rad = r.randint(8, 20), r.randint(1, 3)
    return N(f"A square tile of side {s_} cm has a circular hole of radius {rad} cm. Find the area of the tile that remains, to 1 d.p.", round(s_ * s_ - PI * rad * rad, 1), "cm²", units=["cm²", "cm"], tol=0.05, reason=f"{s_}² − π × {rad}² = {s_ * s_} − {round(PI * rad * rad, 1)} ≈ {round(s_ * s_ - PI * rad * rad, 1)} cm².", o="O2", d="H")
def HOUSE(r):
    w, h, t = r.randint(6, 14), r.randint(4, 10), r.randint(2, 6)
    return N(f"A house end is a {w} m by {h} m rectangle with a triangle of height {t} m on top. Find its total area.", w * h + 0.5 * w * t, "m²", units=["m²", "m"], reason=f"{w} × {h} + ½ × {w} × {t} = {fmt(w * h + 0.5 * w * t)} m².", o="O2", fig={"kind": "shape", "pts": [[0, 0], [w, 0], [w, h], [w / 2, h + t], [0, h]], "s": [f"{w} m", f"{h} m", "", "", ""]})
def PARA(r):
    b, h = r.randint(4, 20), r.randint(3, 12)
    return N(f"A parallelogram has base {b} cm and perpendicular height {h} cm. Find its area.", b * h, "cm²", units=["cm²", "cm"], reason=f"Area = base × height = {b} × {h} = {b * h} cm².", o="O2")
def RING(r):
    R = r.randint(5, 15); rr = r.randint(1, R - 2)
    return N(f"A ring is made from a circle of radius {R} cm with a circle of radius {rr} cm removed from its centre. Find the area of the ring, to 1 d.p.", round(PI * (R * R - rr * rr), 1), "cm²", units=["cm²", "cm"], tol=0.05, reason=f"π × ({R}² − {rr}²) ≈ {round(PI * (R * R - rr * rr), 1)} cm².", o="O2", d="H")
def STAD(r):
    l, d_ = r.randint(50, 120), r.randint(30, 70)
    return N(f"A running track is a rectangle {l} m long with a semicircle of diameter {d_} m at each end. Find the distance once round the outside, to 1 d.p.", round(2 * l + PI * d_, 1), "m", units=["m", "m²"], tol=0.05, reason=f"Two straights 2 × {l} plus two semicircles = one circle π × {d_}: ≈ {round(2 * l + PI * d_, 1)} m.", o="O2", d="H")
s.core(L(s.rng), Lp(s.rng), T(s.rng), HOUSE(s.rng), HOLE(s.rng), RS(s.rng), STAD(s.rng),
       EX("Explain two ways to find the area of an L-shape.", [("split into two rectangles and add", ["split|two rectangles|add"]), ("big rectangle subtract the missing piece", ["subtract|take away|minus|missing"])], "Split the L-shape into two rectangles and add their areas, or find the area of the large rectangle around it and subtract the missing corner.", o="O2"))
s.gen("p", 44, L, Lp, T, RS, HOLE, HOUSE, PARA, RING, STAD)
s.gen("a", 8, RING, STAD, lambda r: (lambda a: N(f"A square of side {2*a} cm has a quarter circle of radius {2*a} cm drawn from one corner. Find the area outside the quarter circle, to 1 d.p.", round(4 * a * a - 0.25 * PI * 4 * a * a, 1), "cm²", units=["cm²", "cm"], tol=0.05, reason=f"Square {2 * a}² − ¼ × π × {2 * a}².", o="O2", d="VH"))(r.randint(2, 10)))

# ================================================================== 7.3
s = U.section("7.3", "Large and small units", ["O3"])
s.idea("Area and volume units", ["1 cm = 10 mm, but **1 cm² = 10 × 10 = 100 mm²** and **1 cm³ = 10 × 10 × 10 = 1000 mm³**.",
       "1 m² = 100 × 100 = **10 000 cm²**; 1 m³ = **1 000 000 cm³**; 1 km² = 1 000 000 m²; 1 **hectare** = 10 000 m². For capacity: **1 cm³ = 1 mL** and **1000 cm³ = 1 litre**."])
s.example("Square units", "Convert 3.5 m² to cm².", [("1 m² = 10 000 cm²", ""), ("3.5 × 10 000 = 35 000", "")], "35 000 cm²")
s.check(N("Convert 4 cm² to mm².", 400, "mm²", units=["mm²", "cm²"], reason="1 cm² = 10 × 10 = 100 mm²: 4 × 100 = 400 mm².", o="O3"))
s.example("Volume to capacity", "A tank holds 0.6 m³ of water. How many litres is that?", [("0.6 × 1 000 000 = 600 000 cm³", ""), ("÷ 1000 = 600 litres", "")], "600 litres")
s.mistake("Not just × 100", ["1 m = 100 cm, but 1 m² is NOT 100 cm². Square the conversion factor for area and cube it for volume."])
s.check(MC("How many cm³ are in 1 m³?", "1 000 000", [("100", ""), ("10 000", "That is cm² in 1 m²."), ("1000", "")], o="O3", d="H"))
CONV = [("cm²", "mm²", 100), ("m²", "cm²", 10000), ("km²", "m²", 1e6), ("hectares", "m²", 10000), ("cm³", "mm³", 1000), ("m³", "cm³", 1e6), ("litres", "cm³", 1000), ("m³", "litres", 1000)]
def u1(r):
    a, b, k = pick(r, CONV); v = round(r.uniform(0.2, 90), r.randint(0, 2))
    return N(f"Convert {fmt(v)} {a} to {b}.", round(v * k, 6), b, units=[b, a], o="O3", reason=f"1 {a} = {fmt(k)} {b}; {fmt(v)} × {fmt(k)}.")
def u2(r):
    a, b, k = pick(r, CONV); v = round(r.uniform(1, 9000), 0) * pick(r, [1, 10, 100])
    return N(f"Convert {fmt(v)} {b} to {a}.", round(v / k, 8), a, units=[a, b], reason=f"1 {a} = {fmt(k)} {b}, so divide: {fmt(v)} ÷ {fmt(k)} = {fmt(round(v / k, 8))} {a}.", o="O3", d="H")
def u3(r):
    l, w = r.randint(20, 400), r.randint(20, 300)
    return N(f"A field is {l} m by {w} m. Find its area in hectares.", l * w / 10000, "hectares", units=["hectares", "m²"], reason=f"{l} × {w} = {l * w} m²; 1 hectare = 10 000 m², so {fmt(l * w / 10000)} hectares.", o="O3", d="H")
def u4(r):
    l, w, h = r.randint(20, 80), r.randint(10, 50), r.randint(10, 40)
    return N(f"A fish tank measures {l} cm by {w} cm by {h} cm. How many litres does it hold?", l * w * h / 1000, "litres", units=["litres", "cm³"], reason=f"{l} × {w} × {h} = {l * w * h} cm³; ÷ 1000 = {fmt(l * w * h / 1000)} litres.", o="O3", d="H", fig={"kind": "solid", "solid": "cuboid", "labels": {"a": f"{l} cm", "b": f"{w} cm", "c": f"{h} cm"}})
def u5(r):
    rows = [("1 cm²", "100 mm²"), ("1 m²", "10 000 cm²"), ("1 cm³", "1000 mm³"), ("1 litre", "1000 cm³"), ("1 hectare", "10 000 m²")]
    return MT("Match the equal amounts.", r.sample(rows, 4), o="O3")
def u6(r):
    v = round(r.uniform(0.5, 9), 1)
    return TB(f"Complete the table for {fmt(v)} m².", ["cm²", "mm²"], [[B(round(v * 1e4, 4)), B(round(v * 1e6, 4))]], reason=f"1 m² = 10 000 cm² = 1 000 000 mm².", o="O3", d="H")
def u7(r):
    s_ = r.randint(2, 9)
    return N(f"A cube has side {s_} cm. Find its volume in mm³.", s_ ** 3 * 1000, "mm³", units=["mm³", "cm³"], reason=f"{s_}³ = {s_ ** 3} cm³; × 1000 = {s_ ** 3 * 1000} mm³.", o="O3", d="H")
s.core(u1(s.rng), u2(s.rng), u3(s.rng), u4(s.rng), u5(s.rng), u6(s.rng), u7(s.rng),
       EX("Explain why 1 m² = 10 000 cm².", [("a 1 m square is 100 cm by 100 cm", ["100 ?(cm)? ?(by|×|x) ?100"]), ("100 × 100 = 10 000", ["10 ?000|100 ?(×|x) ?100"])], "A square of side 1 m is 100 cm by 100 cm, so its area is 100 × 100 = 10 000 cm².", o="O3"))
s.gen("p", 44, u1, u2, u3, u4, u5, u6, u7)
s.gen("a", 8, u3, u4, lambda r: (lambda rr, h: N(f"A cylindrical tank has radius {rr} cm and height {h} cm. How many litres does it hold, to 1 d.p.?", round(PI * rr * rr * h / 1000, 1), "litres", units=["litres", "cm³"], tol=0.05, reason=f"π × {rr}² × {h} ≈ {round(PI * rr * rr * h, 1)} cm³; ÷ 1000 ≈ {round(PI * rr * rr * h / 1000, 1)} litres.", o="O3", d="VH"))(r.randint(10, 60), r.randint(20, 120)))

U.mindmap(("Circumference", "C = πd = 2πr", "O1", "7.1"), ("Area of a circle", "A = πr² • use the radius", "O1", "7.1"),
          ("Compound shapes", "Split, find each area, add or subtract", "O2", "7.2"), ("Units", "1 m² = 10 000 cm² • 1 cm³ = 1 mL • 1 ha = 10 000 m²", "O3", "7.3"))
