# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 14 Volume, surface area and symmetry. Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from math import pi
from kit import *

U = Unit(14, "Volume, surface area and symmetry", "Geometry and measure",
         "Volume of prisms and cylinders, surface area of triangular prisms, pyramids and cylinders, and planes of symmetry in 3D shapes.",
         {"O1": {"sec": "14.1", "code": "9Gg.04", "codeNote": "", "t": "Use V = area of cross-section × length to find the volume of prisms and cylinders, and solve problems."},
          "O2": {"sec": "14.2", "code": "9Gg.05", "codeNote": "", "t": "Find the surface area of triangular prisms, pyramids and cylinders, using nets."},
          "O3": {"sec": "14.3", "code": "9Gg.06", "codeNote": "", "t": "Identify planes of symmetry in 3D shapes."}})
r1 = lambda v: round(v, 1)

# ================================================================== 14.1
s = U.section("14.1", "Volume of prisms", ["O1"])
s.idea("Prisms", ["A **prism** has the same cross-section all the way through. **Volume = area of cross-section × length**.",
       "A **cylinder** is a prism with a circular cross-section: **V = πr²h**."], fig={"kind": "solid", "solid": "triprism", "a": "8 cm", "b": "5 cm", "c": "12 cm"})
s.example("Triangular prism", "A triangular prism has a triangle of base 8 cm and height 5 cm, and length 12 cm. Find its volume.", [("cross-section = ½ × 8 × 5 = 20 cm²", ""), ("V = 20 × 12 = 240 cm³", "")], "240 cm³")
s.check(N("A cylinder has radius 3 cm and height 10 cm. Find its volume to 1 d.p.", r1(pi * 90), "cm³", units=["cm³"], tol=0.06, reason="V = πr²h = π × 3² × 10 = 90π ≈ 282.7 cm³.", o="O1"))
s.idea("Units", ["1 cm³ = 1 ml and 1000 cm³ = 1 litre. 1 m³ = 1 000 000 cm³."])
s.check(MC("Before you read on: a cylinder has radius 2 cm and height 5 cm. Which calculation gives its volume?", "π × 2² × 5", [("2π × 2 × 5", "That is the curved surface area."), ("π × 5² × 2", "The radius is 2, the height 5.")], o="O1"))
s.mistake("Square the radius", ["V = πr²h: square the radius BEFORE multiplying by π and h. Using the diameter instead of the radius gives 4 times the volume."])
s.check(N("A tank holds 24 000 cm³. How many litres is that?", 24, "litres", units=["litres", "l"], reason="1000 cm³ = 1 litre: 24 000 ÷ 1000 = 24 litres.", o="O1"))
def v1(r):
    b, h, l = r.randint(3, 15), r.randint(3, 12), r.randint(5, 25)
    return N(f"A triangular prism has a triangular cross-section with base {b} cm and height {h} cm. Its length is {l} cm. Find its volume.", b * h * l / 2, "cm³", units=["cm³"], reason=f"Cross-section = ½ × {b} × {h} = {fmt(b * h / 2)} cm²; × {l} = {fmt(b * h * l / 2)} cm³.", o="O1", fig={"kind": "solid", "solid": "triprism", "a": f"{b} cm", "b": f"{h} cm", "c": f"{l} cm"})
def v2(r):
    rr, h = r.randint(2, 12), r.randint(3, 20)
    w = r.random() < 0.5
    return N(f"A cylinder has {'radius' if w else 'diameter'} {rr if w else 2*rr} cm and height {h} cm. Find its volume to 1 d.p.", r1(pi * rr * rr * h), "cm³", units=["cm³"], tol=0.06, reason=f"r = {rr} cm. V = π × {rr}² × {h} = {rr * rr * h}π ≈ {r1(pi * rr * rr * h)} cm³.", o="O1", d="M" if w else "H", fig={"kind": "solid", "solid": "cylinder", "r": f"{rr} cm" if w else "", "d": "" if w else f"{2*rr} cm", "h": f"{h} cm"})
def v3(r):
    A, V = r.randint(8, 60), None; l = r.randint(4, 20); V = A * l
    return N(f"A prism has volume {V} cm³ and cross-sectional area {A} cm². Find its length.", l, "cm", units=["cm"], reason=f"Length = volume ÷ area = {V} ÷ {A} = {l} cm.", o="O1")
def v4(r):
    rr = r.randint(2, 10); h = r.randint(4, 30); V = r1(pi * rr * rr * h)
    return N(f"A cylinder has volume {V} cm³ and radius {rr} cm. Find its height to the nearest cm.", h, "cm", units=["cm"], reason=f"h = V ÷ (πr²) = {V} ÷ (π × {rr}²) ≈ {h} cm.", o="O1", d="H", tol=0.5)
def v5(r):
    a, b, c, l = r.randint(2, 6), r.randint(7, 12), r.randint(2, 5), r.randint(5, 20)
    A = a * c + b * c if False else (b * c + a * c)
    return N(f"An L-shaped prism has a cross-section made of a {b} cm × {c} cm rectangle and a {a} cm × {c} cm rectangle. The prism is {l} cm long. Find its volume.", A * l, "cm³", units=["cm³"], reason=f"Cross-section = {b} × {c} + {a} × {c} = {A} cm²; × {l} = {A * l} cm³.", o="O1", d="H")
def v6(r):
    l, w, h = r.randint(20, 80), r.randint(20, 60), r.randint(10, 50)
    return N(f"A fish tank is {l} cm by {w} cm by {h} cm. How many litres of water does it hold when full? (2 d.p.)", round(l * w * h / 1000, 2), "litres", units=["litres", "l"], tol=0.006, reason=f"{l} × {w} × {h} = {l * w * h} cm³ = {fmt(round(l * w * h / 1000, 2))} litres.", o="O1")
def v7(r):
    rr, h, R = r.randint(2, 5), r.randint(8, 20), None; R = rr * 2
    return N(f"Water fills a cylinder of radius {rr} cm to a depth of {h} cm. It is poured into a cylinder of radius {R} cm. How deep is the water now?", h / 4, "cm", units=["cm"], reason=f"The radius doubles, so the base area is 4 times bigger and the depth is 4 times smaller: {h} ÷ 4 = {fmt(h / 4)} cm.", o="O1", d="VH")
s.core(v1(s.rng), v2(s.rng), v3(s.rng), v4(s.rng), v5(s.rng), v6(s.rng),
       TB("Complete the table for prisms.", ["Cross-section area (cm²)", "Length (cm)", "Volume (cm³)"], [[B(15), B(8), B(120)]], o="O1", hint="V = area × length", data={"head": ["Prism", "Area", "Length", "Volume"], "rows": [["P", "15", "8", "?"]]}) if False else
       MC("Which solid is NOT a prism?", "a square-based pyramid", [("a cylinder", "Its cross-section is always a circle."), ("a cuboid", ""), ("a triangular prism", "")], o="O1", fig={"kind": "solid", "solid": "pyramid"}),
       EX("Explain why the volume of a cylinder is πr²h.", [("it is a prism with circular cross-section", ["prism|cross.?section|same all the way"]), ("area of the circle πr² times the height", ["πr²|pi ?r|area of.*circle|times.*h|× ?h"])], "A cylinder is a prism with a circular cross-section. Volume is area of cross-section × length, and the circle's area is πr², so V = πr² × h.", o="O1"))
def n1_1(r):
    rr, h = r.randint(2, 6), r.randint(3, 12)
    return N(f"A cylinder has radius {rr} cm and height {h} cm. Find its volume to 1 decimal place.", round(3.14159265 * rr * rr * h, 1), "cm³", units=["cm³"], o="O1", d="H", tol=0.1, reason=f"π × {rr}² × {h} = {3.14159265 * rr * rr * h:.1f} cm³.")


s.gen("p", 44, v1, v2, v3, v4, v5, v6)
s.capped("p", [1] * 1, [n1_1]).capped("m", [2] * 1, [n1_1])   # v2 reasoning kinds
s.gen("a", 8, v7, v4, lambda r: (lambda a, l: N(f"A prism has a cross-section that is a right-angled triangle with shorter sides {a} cm and {a+1} cm. Its volume is {a*(a+1)*l//2 if a*(a+1)*l % 2 == 0 else a*(a+1)*l/2} cm³. Find its length.", l, "cm", units=["cm"], reason=f"Cross-section = ½ × {a} × {a + 1} = {fmt(a * (a + 1) / 2)} cm²; length = volume ÷ area = {l} cm.", o="O1", d="VH"))(r.randint(3, 12), r.randint(4, 20)))

# ================================================================== 14.2
s = U.section("14.2", "Surface area", ["O2"])
s.idea("Surface area from a net", ["The **surface area** is the total area of all the faces. Sketch the **net** and add up each face.",
       "Triangular prism: 2 triangles + 3 rectangles. Pyramid: base + triangular faces."], fig={"kind": "solid", "solid": "pyramid", "a": "6 cm", "l": "5 cm"})
s.example("Square-based pyramid", "A square-based pyramid has base 6 cm and triangle faces of height 5 cm. Find its surface area.", [("base = 6 × 6 = 36", ""), ("each triangle = ½ × 6 × 5 = 15; four faces = 60", ""), ("total = 96 cm²", "")], "96 cm²")
s.check(N("A cube has side 4 cm. Find its surface area.", 96, "cm²", units=["cm²"], reason="6 faces × 4² = 6 × 16 = 96 cm².", o="O2"))
s.idea("Cylinder", ["A cylinder opens into **two circles** and a **rectangle** whose length is the circumference 2πr. **Surface area = 2πr² + 2πrh**."])
s.mistake("Curved surface", ["The rectangle's width is the CIRCUMFERENCE (2πr), not the radius."])
s.check(N("Find the curved surface area of a cylinder with radius 2 cm and height 7 cm (1 d.p.).", r1(2 * pi * 14), "cm²", units=["cm²"], tol=0.06, reason="2πrh = 2 × π × 2 × 7 = 28π ≈ 88.0 cm².", o="O2", d="H"))
def a1(r):
    a = r.randint(3, 12); l = r.randint(4, 15)
    return N(f"A square-based pyramid has base edge {a} cm. Each triangular face has height {l} cm. Find the total surface area.", a * a + 2 * a * l, "cm²", units=["cm²"], reason=f"Base {a}² = {a * a}; four triangles 4 × ½ × {a} × {l} = {2 * a * l}; total {a * a + 2 * a * l} cm².", o="O2", fig={"kind": "solid", "solid": "pyramid", "a": f"{a} cm", "l": f"{l} cm"})
def a2(r):
    a, b, c = pick(r, [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)]); L = r.randint(5, 20)
    return N(f"A triangular prism has a right-angled triangle cross-section with sides {a} cm, {b} cm and {c} cm. Its length is {L} cm. Find its total surface area.", a * b + (a + b + c) * L, "cm²", units=["cm²"], reason=f"Two triangles: 2 × ½ × {a} × {b} = {a * b}; three rectangles: ({a} + {b} + {c}) × {L} = {(a + b + c) * L}; total {a * b + (a + b + c) * L} cm².", o="O2", d="H", fig={"kind": "solid", "solid": "triprism", "right": True, "a": f"{b} cm", "b": f"{a} cm", "c": f"{L} cm"})
def a3(r):
    rr, h = r.randint(2, 10), r.randint(3, 20)
    return N(f"Find the total surface area of a cylinder with radius {rr} cm and height {h} cm (1 d.p.).", r1(2 * pi * rr * rr + 2 * pi * rr * h), "cm²", units=["cm²"], tol=0.06, reason=f"2πr² + 2πrh = 2π × {rr}² + 2π × {rr} × {h} = {2 * rr * rr + 2 * rr * h}π ≈ {r1(2 * pi * rr * rr + 2 * pi * rr * h)} cm².", o="O2", d="H", fig={"kind": "solid", "solid": "cylinder", "r": f"{rr} cm", "h": f"{h} cm"})
def a4(r):
    l, w, h = r.randint(2, 12), r.randint(2, 12), r.randint(2, 12)
    return N(f"Find the surface area of a cuboid {l} cm by {w} cm by {h} cm.", 2 * (l * w + l * h + w * h), "cm²", units=["cm²"], reason=f"2 × ({l} × {w} + {l} × {h} + {w} × {h}) = 2 × {l * w + l * h + w * h} = {2 * (l * w + l * h + w * h)} cm².", o="O2", fig={"kind": "solid", "solid": "cuboid", "a": f"{l} cm", "b": f"{w} cm", "c": f"{h} cm"})
def a5(r):
    rr, h = r.randint(2, 8), r.randint(5, 20)
    return N(f"A label covers the curved surface of a tin with diameter {2*rr} cm and height {h} cm. Find the area of the label (1 d.p.).", r1(2 * pi * rr * h), "cm²", units=["cm²"], tol=0.06, reason=f"Curved surface = 2πrh with r = {rr}: 2π × {rr} × {h} = {2 * rr * h}π ≈ {r1(2 * pi * rr * h)} cm².", o="O2", d="H")
def a6(r):
    rows = [("Cube", "6 squares"), ("Triangular prism", "2 triangles and 3 rectangles"), ("Square-based pyramid", "1 square and 4 triangles"), ("Cylinder", "2 circles and 1 rectangle")]
    return MT("Match each solid with the faces in its net.", rows, o="O2", skill="Data")
def a7(r):
    s_ = r.randint(2, 9)
    return N(f"A cube has surface area {6*s_*s_} cm². Find its volume.", s_ ** 3, "cm³", units=["cm³"], reason=f"One face = {6 * s_ * s_} ÷ 6 = {s_ * s_} cm², so the side is {s_} cm; volume = {s_}³ = {s_ ** 3} cm³.", o="O2", d="H")
s.core(a1(s.rng), a2(s.rng), a3(s.rng), a4(s.rng), a5(s.rng), a6(s.rng), a7(s.rng),
       EX("Explain why the rectangle in the net of a cylinder has length 2πr.", [("the rectangle wraps round the circle", ["wrap|round|around|curved"]), ("so its length is the circumference", ["circumference|perimeter of the circle|distance round"])], "The rectangle wraps around the circular end, so its length must equal the circumference of the circle, 2πr.", o="O2"))
s.gen("p", 44, a1, a2, a3, a4, a5, a6, a7)
s.gen("a", 8, a2, a7, lambda r: (lambda rr: N(f"A cylinder has radius {rr} cm and total surface area {r1(2*pi*rr*rr + 2*pi*rr*10)} cm². Find its height to the nearest cm.", 10, "cm", units=["cm"], tol=0.5, reason=f"2πr² = {r1(2 * pi * rr * rr)}; the rest, {r1(2 * pi * rr * 10)}, is 2πrh = 2π × {rr} × h, so h ≈ 10 cm.", o="O2", d="VH"))(r.randint(2, 9)))

# ================================================================== 14.3
s = U.section("14.3", "Symmetry in 3D shapes", ["O3"])
s.idea("Planes of symmetry", ["A **plane of symmetry** cuts a solid into two halves that are mirror images.",
       "A cuboid (not a cube) has **3** planes of symmetry. A cube has **9**. A square-based pyramid has **4**. A cylinder has **infinitely many**."], fig={"kind": "solid", "solid": "cuboid", "a": "6 cm", "b": "4 cm", "c": "3 cm"})
s.check(N("How many planes of symmetry does a cuboid with three different edge lengths have?", 3, reason="One plane through the middle of each pair of opposite faces: 3.", o="O3"))
s.check(MC("Before you read on: how many planes of symmetry does a cube have?", "9", [("6", "There are also 6 diagonal planes, through opposite edges… and 3 through the middles: 9."), ("3", "There are more than the three middle planes.")], o="O3"))
s.mistake("Diagonal planes", ["A cube has diagonal planes too (through opposite edges): 3 parallel to the faces + 6 diagonal = 9."])
s.check(MC("How many planes of symmetry does a triangular prism with an equilateral cross-section have?", "4", [("3", "Include the plane across the middle of the length."), ("2", ""), ("6", "")], o="O3", d="H"))
SOL = [("Cube", 9), ("Cuboid with a square end (not a cube)", 5), ("Cuboid with all edges different", 3), ("Square-based pyramid", 4), ("Equilateral triangular prism", 4),
       ("Isosceles (not equilateral) triangular prism", 2), ("Regular hexagonal prism", 7), ("Regular pentagonal prism", 6), ("Cone", "infinitely many")]
def y1(r):
    n, k = pick(r, [x for x in SOL if isinstance(x[1], int)])
    return N(f"How many planes of symmetry does this solid have: {n.lower()}?", k, reason=f"Count the planes that cut it into two mirror-image halves: {k}.", o="O3", d="H" if k > 5 else "M")
def y2(r):
    rows = r.sample([(n, str(k)) for n, k in SOL if isinstance(k, int)], 4)
    return GD("How many planes of symmetry does each solid have?", "Planes", rows, o="O3", d="H", extra=["1", "2", "3", "4", "5", "6", "7", "9"])
def y3(r):
    n = r.randint(5, 12)
    return N(f"How many planes of symmetry does a regular prism with a {n}-sided cross-section have?", n + 1, reason=f"{n} planes along the length (one per line of symmetry of the {n}-gon) + 1 across the middle = {n + 1}.", o="O3", d="H")
def y4(r):
    n = r.randint(3, 10)
    return N(f"How many planes of symmetry does a pyramid with a regular {n}-sided base have?", n, reason=f"Each of the {n} lines of symmetry of the base gives a vertical plane through the top: {n}.", o="O3", d="H")
def y5(r):
    return MC("Which solid has infinitely many planes of symmetry?", pick(r, ["a cylinder", "a cone", "a sphere"]), [("a cube", ""), ("a square-based pyramid", ""), ("a hexagonal prism", "")], o="O3")
s.core(y1(s.rng), y2(s.rng), y3(s.rng), y4(s.rng), y5(s.rng), y1(s.rng),
       MS("Which statements are true?", ["A cube has more planes of symmetry than a cuboid", "Every plane of symmetry of a square-based pyramid passes through its top vertex"], ["A cylinder has exactly 2 planes of symmetry", "A cuboid with a square end has 3 planes of symmetry"], o="O3", d="H", fig={"kind": "solid", "solid": "pyramid"}),
       EX("Explain why a regular hexagonal prism has 7 planes of symmetry.", [("6 vertical planes from the hexagon's lines of symmetry", ["6|six|hexagon"]), ("1 horizontal plane through the middle", ["1|one|horizontal|middle|half"])], "The hexagon has 6 lines of symmetry, giving 6 vertical planes, and there is 1 more plane across the middle of the length: 7 in total.", o="O3"))
s.gen("p", 44, y1, y2, y3, y4, y5)
s.gen("a", 8, y3, y4, y2, lambda r: (lambda n: N(f"A solid is made by joining two identical regular {n}-sided pyramids base to base. How many planes of symmetry does it have?", n + 1, reason=f"{n} vertical planes + 1 plane where the bases meet = {n + 1}.", o="O3", d="VH"))(pick(r, [3, 5, 6, 7, 8, 9, 10])))

U.mindmap(("Volume", "Prism: area × length • cylinder: πr²h • 1000 cm³ = 1 litre", "O1", "14.1"), ("Surface area", "Add the faces of the net • cylinder: 2πr² + 2πrh", "O2", "14.2"),
          ("3D symmetry", "Planes of symmetry • cuboid 3 • cube 9", "O3", "14.3"))
