# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 15 Distance, area and volume (15.1 Converting between miles and kilometres, 15.2 The area of a
parallelogram and trapezium, 15.3 Volume of triangular prisms, 15.4 Surface area of triangular prisms and pyramids).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(15, "Distance, Area and Volume", "Geometry and measure",
         "Converting between miles and kilometres, areas of parallelograms and trapezia, and the volume and surface area of triangular prisms and pyramids.",
         {"O1": {"code": "8Gg.07", "sec": "15.1", "codeNote": "", "t": "Convert between miles and kilometres using 5 miles ≈ 8 km."},
          "O2": {"code": "8Gg.08", "sec": "15.2", "codeNote": "", "t": "Use formulae to find the area of parallelograms and trapezia."},
          "O3": {"code": "8Gg.09", "sec": "15.3", "codeNote": "", "t": "Calculate the volume of triangular prisms."},
          "O4": {"code": "8Gg.10", "sec": "15.4", "codeNote": "", "t": "Calculate the surface area of triangular prisms and pyramids from their nets."}})
PARA = lambda b, h: {"kind": "shape", "pts": [[0, 0], [7, 0], [9, 4], [2, 4]], "s": [f"{b} cm", "", "", ""], "note": f"perpendicular height {h} cm"}
TRAP = lambda a, b, h: {"kind": "shape", "pts": [[0, 0], [9, 0], [7, 4], [2, 4]], "s": [f"{b} cm", "", f"{a} cm", ""], "note": f"height {h} cm"}

# ================================================================== 15.1
s = U.section("15.1", "Converting between miles and kilometres", ["O1"])
s.idea("5 miles ≈ 8 km", ["A **mile** is longer than a kilometre. Use **5 miles ≈ 8 km**.",
       "Miles → km: ÷ 5 × 8 (or × 1.6). Km → miles: ÷ 8 × 5 (or × 0.625)."], table={"head": ["Miles", "5", "10", "25", "50"], "rows": [["km", "8", "16", "40", "80"]]})
s.check(N("Change 35 miles to kilometres.", 56, "km", units=["km"], o="O1"))
s.mistake("Which way?", ["The number of km is always bigger than the number of miles for the same distance."])


def k1(r):
    m = r.randint(2, 40) * 5
    return N(f"Change {m} miles to kilometres.", m * 8 // 5, "km", units=["km"], o="O1", reason=f"{m} ÷ 5 × 8 = {m * 8 // 5} km.")
def k2(r):
    k = r.randint(2, 40) * 8
    return N(f"Change {k} km to miles.", k * 5 // 8, "miles", units=["miles"], o="O1", reason=f"{k} ÷ 8 × 5 = {k * 5 // 8} miles.")
def k3(r):
    m = r.randint(3, 60)
    return N(f"Change {m} miles to kilometres using 1 mile ≈ 1.6 km.", round(m * 1.6, 1), "km", units=["km"], o="O1", tol=0.05, reason=f"{m} × 1.6 = {fmt(round(m * 1.6, 1))} km.")
def k4(r):
    ms = r.sample([5, 15, 20, 30, 45, 60], 3)
    return TB("Complete the conversion table (5 miles ≈ 8 km).", ["Miles", "km"], [[str(m), B(m * 8 // 5)] for m in ms], o="O1")
def k5(r):
    a, b = r.randint(10, 60) * 5, r.randint(10, 100) * 8
    am, bk = a * 8 / 5, b
    return MC(f"Which is further: {a} miles or {b} km?", f"{a} miles" if am > bk else f"{b} km", [f"{b} km" if am > bk else f"{a} miles", "they are the same"], o="O1", d="H", reason=f"{a} miles ≈ {fmt(am)} km.") if am != bk else None
def k6(r):
    sp = r.randint(6, 14) * 5
    return N(f"A speed limit is {sp} miles per hour. What is this in km per hour?", sp * 8 // 5, "km/h", units=["km/h"], o="O1", d="H", reason=f"{sp} × 8 ÷ 5 = {sp * 8 // 5} km/h.")
def k7(r):
    k = r.randint(5, 30) * 8; t = r.randint(2, 5)
    return N(f"A cyclist rides {k} km in {t} days. How many miles is that altogether?", k * 5 // 8, "miles", units=["miles"], o="O1", reason=f"{k} ÷ 8 × 5 = {k * 5 // 8} miles.")
def k8(r):
    m = r.randint(2, 20) * 5
    return N(f"A road sign says a town is {m} miles away. Estimate the distance in km using the conversion graph (5 miles ≈ 8 km).", m * 8 // 5, "km", units=["km"], o="O1", fig={"kind": "linegraph", "x": {"min": 0, "max": 100, "step": 10, "label": "Miles"}, "y": {"min": 0, "max": 160, "step": 20, "label": "Kilometres"}, "series": [{"pts": [[0, 0], [100, 160]]}]})
def k9(r):
    a = r.randint(3, 12) * 8
    return N(f"A marathon is about 42 km. Tom has run {a} km of a race. About how many miles is that?", a * 5 // 8, "miles", units=["miles"], o="O1")


s.std([k4, k8, k1, k2, k3, k5, k6, k7, k9], EX("Explain how to change 64 km into miles.", [("8 km ≈ 5 miles", ["8 ?km|5 ?miles"]), ("64 ÷ 8 × 5 = 40 miles", ["40"])], "8 km is about 5 miles. 64 ÷ 8 = 8 lots of 8 km, so 8 × 5 = 40 miles.", o="O1"))

# ================================================================== 15.2
s = U.section("15.2", "The area of a parallelogram and trapezium", ["O2"])
s.idea("Parallelogram", ["**Area of a parallelogram = base × perpendicular height**. Cut off a triangle and move it: it becomes a rectangle.",
       "Use the **perpendicular** (straight up) height, not the sloping side."], fig=PARA(8, 5))
s.idea("Trapezium", ["**Area of a trapezium = ½ (a + b) h**, where a and b are the parallel sides and h is the height between them."], fig=TRAP(4, 9, 5))
s.example("Trapezium", "Find the area of a trapezium with parallel sides 6 cm and 10 cm and height 4 cm.", [("½ × (6 + 10) × 4", ""), ("= ½ × 16 × 4 = 32", "")], "32 cm²")
s.check(N("A parallelogram has base 9 cm and perpendicular height 6 cm. Find its area.", 54, "cm²", units=["cm²"], o="O2"))
s.idea("Why a parallelogram has area base × height", ["Cut the triangle off one end of a parallelogram and slide it to the other end: you get a rectangle with the same base and the same perpendicular height.",
       "A trapezium is half of a parallelogram made from two copies: area = 1/2 (a + b) h."])
s.check(MC("Before you read on: a parallelogram has base 8 cm, sloping side 5 cm and height 4 cm. What is its area?", "32 cm²", [("40 cm²", "Use the perpendicular height, not the sloping side."), ("16 cm²", "There is no 1/2 for a parallelogram.")], o="O2"))
s.mistake("Sloping side", ["Do not use the slanted side for the height."])


def a1(r):
    b, h = r.randint(3, 15), r.randint(2, 12)
    return N("Find the area of the parallelogram.", b * h, "cm²", units=["cm²"], o="O2", fig=PARA(b, h), reason=f"{b} × {h} = {b * h} cm².")
def a2(r):
    a, b, h = r.randint(2, 10), r.randint(5, 15), r.randint(2, 10)
    if a == b: return None
    return N("Find the area of the trapezium.", (a + b) * h / 2, "cm²", units=["cm²"], o="O2", fig=TRAP(a, b, h), reason=f"½ × ({a} + {b}) × {h} = {fmt((a + b) * h / 2)} cm².")
def a3(r):
    b, h = r.randint(3, 15), r.randint(2, 12)
    return N(f"A parallelogram has area {b * h} cm² and base {b} cm. Find its perpendicular height.", h, "cm", units=["cm"], o="O2", d="H", reason=f"{b * h} ÷ {b} = {h} cm.")
def a4(r):
    a, b, h = r.randint(2, 8), r.randint(9, 16), r.randint(2, 10)
    A = (a + b) * h / 2
    return N(f"A trapezium has parallel sides {a} cm and {b} cm and area {fmt(A)} cm². Find its height.", h, "cm", units=["cm"], o="O2", d="VH", reason=f"½ × {a + b} × h = {fmt(A)} → h = {h}.")
def a5(r):
    a, b, h = r.randint(10, 40), r.randint(40, 80), r.randint(10, 30)
    return N(f"A garden is a trapezium with parallel sides {a} m and {b} m, {h} m apart. Find its area.", (a + b) * h / 2, "m²", units=["m²"], o="O2", reason=f"½ × ({a} + {b}) × {h} = {fmt((a + b) * h / 2)} m².")
def a6(r):
    b, h, sl = r.randint(5, 12), r.randint(3, 8), None; sl = h + r.randint(1, 3)
    return MC(f"A parallelogram has base {b} cm, sloping side {sl} cm and perpendicular height {h} cm. Which calculation gives its area?", f"{b} × {h}", [f"{b} × {sl}", f"½ × {b} × {h}", f"{b} + {h}"], o="O2", fig={"kind": "shape", "pts": [[0, 0], [7, 0], [9, 4], [2, 4]], "s": [f"{b} cm", f"{sl} cm", "", ""], "note": f"perpendicular height {h} cm"})
def a7(r):
    a, b, h = r.randint(2, 8), r.randint(9, 14), r.randint(2, 8)
    return TB("Complete the working for the area of this trapezium.", ["Step", "Value"], [["a + b", B(a + b)], ["(a + b) × h", B((a + b) * h)], ["Area (cm²)", B((a + b) * h / 2)]], o="O2", fig=TRAP(a, b, h))
def a8(r):
    b, h = r.randint(3, 10), r.randint(3, 10)
    return N(f"A tile is a parallelogram with base {b} cm and height {h} cm. How much area do 20 tiles cover?", 20 * b * h, "cm²", units=["cm²"], o="O2", reason=f"20 × {b} × {h} = {20 * b * h} cm².")


def m152(r):
    a, b, h = r.randint(3, 8), r.randint(9, 14), r.randint(2, 6) * 2
    return N(f"A trapezium has parallel sides {a} cm and {b} cm and area {(a + b) * h // 2} cm². Find its height.", h, "cm", units=["cm"], o="O2", d="H", reason=f"1/2 × ({a} + {b}) × h = {(a + b) * h // 2}, so h = {h} cm.")


s.std([a1, a2, a3, a5, a6, a8, a4, a7], EX("Explain why the area of a parallelogram is base × perpendicular height.", [("cut a triangle off one end and move it to the other end", ["cut|move|rearrange|triangle"]), ("this makes a rectangle with the same base and height", ["rectangle"])], "Cut the triangle off one end and slide it to the other end. The parallelogram becomes a rectangle with the same base and height, so its area is base × height.", o="O2"),
      deep=[m152])

# ================================================================== 15.3
s = U.section("15.3", "Calculating the volume of triangular prisms", ["O3"])
s.idea("Prisms", ["A **prism** has the same cross-section all along its length. **Volume = area of cross-section × length**.",
       "For a triangular prism: volume = ½ × base × height × length."], fig={"kind": "solid", "solid": "triprism", "a": "6 cm", "b": "4 cm", "c": "10 cm"})
s.example("Triangular prism", "A triangular prism has a cross-section with base 6 cm and height 4 cm. It is 10 cm long. Find its volume.", [("area = ½ × 6 × 4 = 12 cm²", ""), ("volume = 12 × 10 = 120 cm³", "")], "120 cm³")
s.check(N("A prism has cross-section area 15 cm² and length 8 cm. Find its volume.", 120, "cm³", units=["cm³"], o="O3"))
s.idea("Volume of any prism", ["A prism has the same cross-section all the way through, so its volume = area of the cross-section × length. For a triangular prism, find the triangle's area first.",
       "This is the same idea as a cuboid: area of the end (l × w) × height."])
s.mistake("Halve the triangle", ["The triangle's area is ½ × base × height. Forgetting the ½ doubles the volume."])


def v1(r):
    b, h, l = r.randint(2, 12), r.randint(2, 10), r.randint(3, 20)
    return N("Find the volume of the triangular prism.", b * h * l / 2, "cm³", units=["cm³"], o="O3", fig={"kind": "solid", "solid": "triprism", "a": f"{b} cm", "b": f"{h} cm", "c": f"{l} cm"}, reason=f"½ × {b} × {h} × {l} = {fmt(b * h * l / 2)} cm³.")
def v2(r):
    A, l = r.randint(5, 40), r.randint(3, 20)
    return N(f"A prism has cross-section area {A} cm² and length {l} cm. Find its volume.", A * l, "cm³", units=["cm³"], o="O3")
def v3(r):
    b, h, l = r.randint(2, 12), r.randint(2, 10), r.randint(3, 20)
    V = b * h * l / 2
    return N(f"A triangular prism has volume {fmt(V)} cm³. Its triangular cross-section has base {b} cm and height {h} cm. How long is the prism?", l, "cm", units=["cm"], o="O3", d="H", reason=f"Area = {fmt(b * h / 2)}; {fmt(V)} ÷ {fmt(b * h / 2)} = {l} cm.")
def v4(r):
    b, h, l = r.randint(2, 8) * 10, r.randint(2, 6) * 10, r.randint(2, 6) * 10
    return N(f"A tent is a triangular prism: the triangle has base {b} cm and height {h} cm, and the tent is {l} cm long. Find the volume in litres (1000 cm³ = 1 litre).", b * h * l / 2000, "litres", units=["litres", "l"], o="O3", d="H")
def v5(r):
    b, h, l = r.randint(2, 12), r.randint(2, 10), r.randint(3, 20)
    return TB("Complete the working for this triangular prism.", ["Step", "Value"], [["Area of triangle (cm²)", B(b * h / 2)], ["Volume (cm³)", B(b * h * l / 2)]], o="O3", fig={"kind": "solid", "solid": "triprism", "a": f"{b} cm", "b": f"{h} cm", "c": f"{l} cm"})
def v6(r):
    l, w, h = r.randint(2, 10), r.randint(2, 10), r.randint(2, 10)
    return N(f"A cuboid is a prism. Find the volume of a cuboid {l} cm by {w} cm by {h} cm.", l * w * h, "cm³", units=["cm³"], o="O3")
def v7(r):
    return MC("Which of these is NOT a prism?", "a square-based pyramid", ["a cuboid", "a triangular prism", "a cylinder"], o="O3", reason="A pyramid's cross-section gets smaller towards the top.")
def v8(r):
    a, b, l = r.randint(3, 8), r.randint(3, 8), r.randint(5, 15)
    return N(f"A prism has a right-angled triangle cross-section with shorter sides {a} cm and {b} cm. Its length is {l} cm. Find the volume.", a * b * l / 2, "cm³", units=["cm³"], o="O3", fig={"kind": "solid", "solid": "triprism", "right": True, "a": f"{a} cm", "b": f"{b} cm", "c": f"{l} cm"})


def m153(r):
    b, h, l = r.randint(3, 10), r.randint(2, 8) * 2, r.randint(5, 15)
    return N(f"A triangular prism has a triangle end with base {b} cm and height {h} cm. The prism is {l} cm long. Find its volume.", b * h // 2 * l, "cm³", units=["cm³"], o="O3", d="H", reason=f"End area 1/2 × {b} × {h} = {b * h // 2} cm²; × {l} = {b * h // 2 * l} cm³.")


s.std([v1, v5, v2, v3, v4, v6, v7, v8], EX("Explain why you multiply by the length to find the volume of a prism.", [("the cross-section is the same all the way along", ["same all|same cross|constant|layers|slices"]), ("so the volume is the cross-section area repeated along the length", ["stack|repeat|layer|times the length|× ?length"])], "A prism has the same cross-section all along its length, so it is like layers of that area stacked up. Volume = area of cross-section × length.", o="O3"),
      deep=[m153])

# ================================================================== 15.4
s = U.section("15.4", "Calculating the surface area of triangular prisms and pyramids", ["O4"])
s.idea("Use the net", ["The **surface area** is the total area of all the faces. Draw the net and find the area of each face.",
       "A triangular prism: 2 triangles + 3 rectangles. A square-based pyramid: 1 square + 4 triangles."], fig={"kind": "solid", "solid": "pyramid", "a": "6 cm", "l": "5 cm"})
s.example("Pyramid", "A square-based pyramid has base 6 cm and triangular faces of height 5 cm. Find its surface area.", [("base = 6 × 6 = 36", ""), ("4 triangles = 4 × ½ × 6 × 5 = 60", ""), ("total = 96 cm²", "")], "96 cm²")
s.check(N("A cube has edges of 3 cm. Find its surface area.", 54, "cm²", units=["cm²"], o="O4"))
s.mistake("Count every face", ["A triangular prism has 5 faces: do not forget the two triangular ends."])


def s1(r):
    a, l = r.randint(3, 12), r.randint(3, 12)
    return N("Find the surface area of the square-based pyramid.", a * a + 2 * a * l, "cm²", units=["cm²"], o="O4", fig={"kind": "solid", "solid": "pyramid", "a": f"{a} cm", "l": f"{l} cm"}, reason=f"{a}² + 4 × ½ × {a} × {l} = {a * a + 2 * a * l} cm².")
def s2(r):
    a, b, c = pick(r, [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)]); L = r.randint(4, 15)
    return N(f"A triangular prism has a right-angled triangle cross-section with sides {a} cm, {b} cm and {c} cm, and length {L} cm. Find its surface area.", a * b + (a + b + c) * L, "cm²", units=["cm²"], o="O4", d="H", fig={"kind": "solid", "solid": "triprism", "right": True, "a": f"{a} cm", "b": f"{b} cm", "c": f"{L} cm"}, reason=f"2 triangles: {a * b}; 3 rectangles: ({a} + {b} + {c}) × {L} = {(a + b + c) * L}; total {a * b + (a + b + c) * L} cm².")
def s3(r):
    l, w, h = r.randint(2, 10), r.randint(2, 10), r.randint(2, 10)
    return N(f"Find the surface area of a cuboid {l} cm by {w} cm by {h} cm.", 2 * (l * w + l * h + w * h), "cm²", units=["cm²"], o="O4", fig={"kind": "solid", "solid": "cuboid", "a": f"{l} cm", "b": f"{w} cm", "c": f"{h} cm"})
def s4(r):
    rows = [("Cube", "6 squares"), ("Triangular prism", "2 triangles and 3 rectangles"), ("Square-based pyramid", "1 square and 4 triangles"), ("Triangular pyramid", "4 triangles"), ("Cuboid", "6 rectangles")]
    return GD("Which faces make the net of each solid?", "Faces", r.sample(rows, 4), o="O4")
def s5(r):
    a, l = r.randint(3, 10), r.randint(3, 10)
    return TB("Complete the working for the surface area of this pyramid.", ["Part", "Area (cm²)"], [["Square base", B(a * a)], ["One triangle", B(a * l / 2)], ["Total", B(a * a + 2 * a * l)]], o="O4", fig={"kind": "solid", "solid": "pyramid", "a": f"{a} cm", "l": f"{l} cm"})
def s6(r):
    s_, L = r.randint(3, 10), r.randint(4, 15)
    return N(f"A triangular prism has an equilateral triangle cross-section with sides {s_} cm. It is {L} cm long. Find the total area of its three rectangular faces.", 3 * s_ * L, "cm²", units=["cm²"], o="O4", reason=f"3 × {s_} × {L} = {3 * s_ * L} cm².")
def s7(r):
    a = r.randint(2, 9)
    return N(f"A cube has a surface area of {6 * a * a} cm². How long is each edge?", a, "cm", units=["cm"], o="O4", d="H", reason=f"{6 * a * a} ÷ 6 = {a * a}; √{a * a} = {a} cm.")
def s8(r):
    a, l = r.randint(4, 12), r.randint(4, 12); p = pick(r, [2, 3, 5])
    return N(f"A pyramid-shaped box has a square base {a} cm wide and triangular faces of height {l} cm. Card costs {p} cents per cm². How much does the card cost, in cents?", (a * a + 2 * a * l) * p, "cents", units=["cents"], o="O4", d="VH")


s.std([s4, s5, s1, s2, s3, s6, s7, s8], EX("Explain how to find the surface area of a triangular prism.", [("it has 2 triangles and 3 rectangles", ["triangle.*rectangle|2 triangles|3 rectangles|five faces|5 faces"]), ("find each area and add them", ["add|total|sum"])], "A triangular prism has 5 faces: 2 triangles and 3 rectangles. Find the area of each face from the net and add them together.", o="O4"))

U.mindmap(("Miles and km", "5 miles ≈ 8 km • 1 mile ≈ 1.6 km", "O1", "15.1"), ("Areas", "Parallelogram b × h • trapezium ½(a + b)h", "O2", "15.2"),
          ("Prism volume", "Cross-section area × length", "O3", "15.3"), ("Surface area", "Add the faces of the net", "O4", "15.4"))
