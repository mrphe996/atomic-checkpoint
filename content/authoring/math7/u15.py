# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 15 Shapes, area and volume (15.1 Converting between units for area, 15.2 Using hectares,
15.3 The area of a triangle, 15.4 Volume of cubes and cuboids, 15.5 Surface area of cubes and cuboids).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(15, "Shapes, Area and Volume", "Geometry and measure",
         "Converting area units, hectares, the area of a triangle, and the volume and surface area of cubes and cuboids.",
         {"O1": {"code": "7Gg.08", "sec": "15.1", "codeNote": "", "t": "Convert between area units: mm², cm² and m²."},
          "O2": {"code": "7Gg.09", "sec": "15.2", "codeNote": "", "t": "Know that 1 hectare = 10 000 m² and convert between hectares and square metres."},
          "O3": {"code": "7Gg.10", "sec": "15.3", "codeNote": "", "t": "Use the formula area = ½ × base × height for triangles."},
          "O4": {"code": "7Gg.11", "sec": "15.4", "codeNote": "", "t": "Calculate the volume of cubes and cuboids."},
          "O5": {"code": "7Gg.12", "sec": "15.5", "codeNote": "", "t": "Calculate the surface area of cubes and cuboids from their nets."}})
CUB = lambda a, b, c: {"kind": "solid", "solid": "cuboid", "a": f"{a} cm", "b": f"{b} cm", "c": f"{c} cm"}
TRI = lambda b, h: {"kind": "shape", "pts": [[0, 0], [8, 0], [3, 5]], "s": [f"{b} cm", "", ""], "note": f"height {h} cm"}

# ================================================================== 15.1
s = U.section("15.1", "Converting between units for area", ["O1"])
s.idea("Square units", ["1 cm = 10 mm, so 1 cm² = 10 × 10 = **100 mm²**. 1 m = 100 cm, so 1 m² = 100 × 100 = **10 000 cm²**.",
       "To change to a smaller unit, multiply; to change to a bigger unit, divide."], table={"head": ["", "Length", "Area"], "rows": [["cm → mm", "× 10", "× 100"], ["m → cm", "× 100", "× 10 000"]]})
s.check(N("Change 3 cm² to mm².", 300, "mm²", units=["mm²"], o="O1"))
s.idea("Why 1 m² is 10 000 cm²", ["A square 1 m by 1 m is 100 cm by 100 cm. Its area is 100 × 100 = 10 000 cm², not 100 cm².",
       "Area has two lengths multiplied, so the conversion factor is squared: 1 cm² = 10 × 10 = 100 mm²."], fig={"kind": "shape", "pts": [[0, 0], [5, 0], [5, 5], [0, 5]], "s": ["1 m = 100 cm", "1 m = 100 cm", "", ""]})
s.check(MC("Before you read on: how many cm² are in 3 m²?", "30 000", [("300", "1 m² = 10 000 cm², not 100 cm²."), ("3000", "Multiply by 10 000.")], o="O1"))
s.mistake("Square the factor", ["1 m² is NOT 100 cm². It is 100 × 100 = 10 000 cm²."])


def u1(r):
    a = r.randint(2, 50)
    return N(f"Change {a} cm² to mm².", a * 100, "mm²", units=["mm²"], o="O1")
def u2(r):
    a = r.randint(2, 90) * 100
    return N(f"Change {fmt(a)} mm² to cm².", a // 100, "cm²", units=["cm²"], o="O1")
def u3(r):
    a = r.randint(2, 20)
    return N(f"Change {a} m² to cm².", a * 10000, "cm²", units=["cm²"], o="O1")
def u4(r):
    a = r.randint(1, 40) * 5000
    return N(f"Change {fmt(a)} cm² to m².", a / 10000, "m²", units=["m²"], o="O1", d="H")
def u5(r):
    rows = [("1 cm²", "100 mm²"), ("1 m²", "10 000 cm²"), ("5 cm²", "500 mm²"), ("2 m²", "20 000 cm²")]
    return GD("Match each area to its equal value.", "Equal to", rows, o="O1", extra=["10 mm²", "100 cm²"])
def u6(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"A rectangle is {a} cm by {b} cm. What is its area in mm²?", a * b * 100, "mm²", units=["mm²"], o="O1", d="H", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": [f"{a} cm", f"{b} cm", "", ""]})
def u7(r):
    a = r.randint(2, 9)
    return TB(f"Complete the table for an area of {a} m².", ["Unit", "Area"], [["m²", str(a)], ["cm²", B(a * 10000)]], o="O1")


def ar1(r):   # spot the error
    a = r.randint(2, 9)
    return MC(f"Lia says {a} cm² = {a * 10} mm² because 1 cm = 10 mm. What is the correct answer?", f"{a * 100} mm²", [(f"{a * 10} mm²", "Area uses two lengths: 10 × 10 = 100."), (f"{a * 1000} mm²", "That uses 10 × 10 × 10, which is for volume.")], o="O1", d="H",
              reason=f"1 cm² = 10 mm × 10 mm = 100 mm², so {a} cm² = {a * 100} mm².")


s.std([u5, u6, u1, u2, u3, u4, u7], EX("Explain why 1 m² = 10 000 cm².", [("1 m = 100 cm", ["100 ?cm"]), ("a 1 m square is 100 cm by 100 cm: 100 × 100 = 10 000", ["100 ?× ?100|10 ?000"])], "1 m = 100 cm, so a square 1 m by 1 m is 100 cm by 100 cm. Its area is 100 × 100 = 10 000 cm².", o="O1"),
      deep=[ar1])

# ================================================================== 15.2
s = U.section("15.2", "Using hectares", ["O2"])
s.idea("Hectares", ["A **hectare** (ha) is used for large areas such as fields and parks. **1 hectare = 10 000 m²** – a square 100 m by 100 m."])
s.check(N("A field is 3 hectares. How many square metres is that?", 30000, "m²", units=["m²"], o="O2"))
s.idea("Picturing a hectare", ["A hectare is a square 100 m by 100 m, so 1 ha = 10 000 m². A football pitch is a little under 1 hectare.",
       "Hectares are used for fields and parks because square metres give very large numbers."])
s.check(MC("Before you read on: a field is 200 m by 300 m. Is it more or less than 1 hectare?", "More: 6 ha", [("Less", "200 × 300 = 60 000 m²."), ("Exactly 1 ha", "1 ha is 10 000 m².")], o="O2"))
s.mistake("Not 100", ["1 hectare is 10 000 m², not 100 m²."])


def h1(r):
    a = r.randint(2, 20)
    return N(f"Change {a} hectares to m².", a * 10000, "m²", units=["m²"], o="O2")
def h2(r):
    a = r.randint(1, 30) * 5000
    return N(f"Change {fmt(a)} m² to hectares.", a / 10000, "ha", units=["ha", "hectares"], o="O2")
def h3(r):
    l, w = r.randint(2, 8) * 50, r.randint(2, 8) * 50
    return N(f"A field is {l} m by {w} m. What is its area in hectares?", l * w / 10000, "ha", units=["ha", "hectares"], o="O2", d="H", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 5], [0, 5]], "s": [f"{l} m", f"{w} m", "", ""]})
def h4(r):
    a = pick(r, [0.5, 1.5, 2.5, 0.25])
    return N(f"A park has an area of {fmt(a)} hectares. How many m² is that?", a * 10000, "m²", units=["m²"], o="O2")
def h5(r):
    rows = [("A football pitch", "Hectares"), ("A book cover", "cm²"), ("A bedroom floor", "m²"), ("A farm", "Hectares"), ("A stamp", "mm²")]
    return GD("Which unit is best for each area?", "Unit", r.sample(rows, 4), o="O2", extra=["m²", "cm²"])
def h6(r):
    a = r.randint(2, 9)
    return TB(f"Complete the table.", ["Hectares", "Square metres"], [[str(a), B(a * 10000)], [B(a * 2), str(a * 20000)]], o="O2")
def h7(r):
    a, p = r.randint(2, 10), r.randint(20, 90) * 100
    return N(f"A farmer sells land at ${p} per hectare. How much does {a} hectares cost?", a * p, "$", units=["$"], o="O2")


def ha1(r):   # decision: field size
    a, b = r.randint(1, 5) * 100, r.randint(1, 5) * 100
    return N(f"A field is {a} m by {b} m. How many hectares is it?", a * b / 10000, "ha", units=["ha", "hectares"], o="O2", d="H", reason=f"{a} × {b} = {a * b:,} m²; ÷ 10 000 = {a * b / 10000:g} ha.")


s.std([h5, h6, h1, h2, h3, h4, h7], EX("Explain why a square 100 m by 100 m has an area of 1 hectare.", [("100 × 100 = 10 000 m²", ["10 ?000|100 ?× ?100"]), ("1 hectare = 10 000 m²", ["hectare"])], "The square's area is 100 × 100 = 10 000 m², and 1 hectare is defined as 10 000 m².", o="O2"),
      deep=[ha1])

# ================================================================== 15.3
s = U.section("15.3", "The area of a triangle", ["O3"])
s.idea("Half a rectangle", ["A triangle is **half** of a rectangle with the same base and height: **Area = ½ × base × height**.",
       "The height is **perpendicular** (at 90°) to the base."], fig=TRI(8, 5))
s.check(N("Find the area of a triangle with base 10 cm and height 6 cm.", 30, "cm²", units=["cm²"], o="O3"))
s.idea("Why a triangle is half a rectangle", ["Draw a rectangle around a triangle using its base and height. The triangle fills exactly half of it, so Area = 1/2 × base × height.",
       "The height must be at right angles to the base – not the length of a sloping side."])
s.check(MC("Before you read on: a triangle has base 10 cm and height 6 cm. What is its area?", "30 cm²", [("60 cm²", "That is the whole rectangle; the triangle is half of it."), ("16 cm²", "Multiply, then halve.")], o="O3"))
s.mistake("Halve it", ["base × height gives the rectangle; divide by 2 for the triangle."])


def t1(r):
    b, h = r.randint(2, 20), r.randint(2, 16)
    return N("Find the area of the triangle.", b * h / 2, "cm²", units=["cm²"], o="O3", fig=TRI(b, h))
def t2(r):
    b, h = r.randint(2, 20), r.randint(2, 16)
    return N(f"A triangle has area {fmt(b * h / 2)} cm² and base {b} cm. Find its height.", h, "cm", units=["cm"], o="O3", d="H")
def t3(r):
    a, b = r.randint(3, 12), r.randint(3, 12)
    return N("Find the area of this right-angled triangle.", a * b / 2, "cm²", units=["cm²"], o="O3", fig={"kind": "shape", "pts": [[0, 0], [a, 0], [0, b]], "s": [f"{a} cm", "", f"{b} cm"], "right": [0]})
def t4(r):
    b, h = r.randint(2, 12) * 2, r.randint(2, 12)
    return TB("Complete the working for the area of a triangle.", ["Step", "Value"], [["base × height", B(b * h)], ["÷ 2", B(b * h // 2)]], o="O3", data={"head": ["Base", "Height"], "rows": [[f"{b} cm", f"{h} cm"]]})
def t5(r):
    b, h, sl = r.randint(4, 12), r.randint(3, 9), None; sl = h + r.randint(1, 3)
    return MC(f"A triangle has base {b} cm, height {h} cm and a sloping side of {sl} cm. Which calculation gives its area?", f"½ × {b} × {h}", [f"½ × {b} × {sl}", f"{b} × {h}", f"{b} + {h}"], o="O3")
def t6(r):
    l, w = r.randint(4, 12), r.randint(4, 12)
    return N(f"A rectangle {l} cm by {w} cm is cut along a diagonal. What is the area of one of the triangles?", l * w / 2, "cm²", units=["cm²"], o="O3")
def t7(r):
    b, h = r.randint(2, 8), r.randint(2, 8)
    return N(f"A flag is made of two identical triangles, each with base {b} cm and height {h} cm. What is the total area?", b * h, "cm²", units=["cm²"], o="O3")


def tg1(r):   # find base from area
    h = r.randint(2, 10); b = r.randint(2, 12) * 2
    return N(f"A triangle has area {b * h // 2} cm² and height {h} cm. What is its base?", b, "cm", units=["cm"], o="O3", d="H", reason=f"1/2 × base × {h} = {b * h // 2}, so base × {h} = {b * h} and base = {b} cm.")
def tg2(r):   # spot the error: slant
    return MC("A triangle has a base of 8 cm, a sloping side of 5 cm and a height of 4 cm. Jo works out 1/2 × 8 × 5 = 20 cm². What is the area?", "16 cm²", [("20 cm²", "Use the height at right angles to the base, not the sloping side."), ("32 cm²", "Remember the 1/2.")], o="O3", d="H",
              reason="1/2 × 8 × 4 = 16 cm².")


s.std([t1, t4, t2, t3, t5, t6, t7], EX("Explain why the area of a triangle is ½ × base × height.", [("a triangle is half of a rectangle with the same base and height", ["half.*rectangle|rectangle.*half|two triangles"]), ("the rectangle's area is base × height", ["base ?× ?height|b ?× ?h"])], "Two identical triangles fit together to make a rectangle with the same base and height. The rectangle's area is base × height, so one triangle is half of that.", o="O3"),
      deep=[tg1, tg2])

# ================================================================== 15.4
s = U.section("15.4", "Calculating the volume of cubes and cuboids", ["O4"])
s.idea("Volume", ["**Volume** is the space inside a 3D shape, measured in cubic units such as cm³.",
       "**Volume of a cuboid = length × width × height.** A cube with edge a has volume a³."], fig=CUB(5, 3, 4))
s.check(N("Find the volume of a cuboid 5 cm by 3 cm by 4 cm.", 60, "cm³", units=["cm³"], o="O4"))
s.idea("Why volume is length × width × height", ["A cuboid 4 cm by 3 cm by 2 cm holds layers of 1 cm cubes: each layer has 4 × 3 = 12 cubes and there are 2 layers, so 24 cm³.",
       "Volume counts cubes, so it is measured in cubic units: cm³, m³."], fig=CUB(4, 3, 2))
s.check(MC("Before you read on: if you double every edge of a cube, what happens to its volume?", "It is 8 times bigger", [("It doubles", "Each of the three lengths doubles: 2 × 2 × 2 = 8."), ("It is 4 times bigger", "That is what happens to the area of a face.")], o="O4"))
s.mistake("Cubic units", ["Volume is in cm³ (cubic), not cm²."])


def v1(r):
    a, b, c = r.randint(2, 12), r.randint(2, 10), r.randint(2, 10)
    return N("Find the volume of the cuboid.", a * b * c, "cm³", units=["cm³"], o="O4", fig=CUB(a, b, c))
def v2(r):
    a = r.randint(2, 10)
    return N(f"Find the volume of a cube with edges of {a} cm.", a ** 3, "cm³", units=["cm³"], o="O4")
def v3(r):
    a, b, c = r.randint(2, 10), r.randint(2, 10), r.randint(2, 10)
    return N(f"A cuboid has volume {a * b * c} cm³, length {a} cm and width {b} cm. Find its height.", c, "cm", units=["cm"], o="O4", d="H")
def v4(r):
    a, b, c = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
    return N(f"How many 1 cm cubes fit inside a box {a} cm by {b} cm by {c} cm?", a * b * c, "cubes", units=["cubes"], o="O4")
def v5(r):
    a = r.randint(2, 9)
    return N(f"A cube has a volume of {a ** 3} cm³. How long is each edge?", a, "cm", units=["cm"], o="O4", d="H")
def v6(r):
    dims = [(r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)) for _ in range(2)]
    return TB("Complete the table.", ["Length", "Width", "Height", "Volume (cm³)"], [[str(a), str(b), str(c), B(a * b * c)] for a, b, c in dims], o="O4")
def v7(r):
    l, w, h = r.randint(2, 6) * 10, r.randint(2, 5) * 10, r.randint(2, 5) * 10
    return N(f"A fish tank is {l} cm by {w} cm by {h} cm. How many litres does it hold? (1000 cm³ = 1 litre)", l * w * h / 1000, "litres", units=["litres", "l"], o="O4", d="H")


def vo1(r):   # missing edge
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    return N(f"A cuboid has volume {a * b * c} cm³. Its length is {a} cm and its width is {b} cm. Find its height.", c, "cm", units=["cm"], o="O4", d="H", fig=CUB(a, b, "?"), reason=f"{a} × {b} = {a * b}; {a * b * c} ÷ {a * b} = {c} cm.")
def vo2(r):   # find all cuboids with volume
    v = pick(r, [24, 36, 48])
    good = [f"{a} × {b} × {v // (a * b)}" for a, b in r.sample([(1, 2), (2, 3), (2, 2), (1, 3), (3, 4)], 5) if v % (a * b) == 0][:2]
    bad = [f"{v // 4} × 2 × 3", f"{v // 6} × 3 × 1"]
    bad = [x for x in bad if eval(x.replace("×", "*")) != v][:2]
    if len(good) < 2 or not bad: return None
    return MS(f"Select ALL the cuboids (lengths in cm) with a volume of {v} cm³.", good, bad, o="O4", d="H", reason="Multiply the three lengths of each one.")


s.std([v1, v6, v2, v3, v4, v5, v7], EX("Explain why the volume of a cuboid is length × width × height.", [("length × width gives the number of cubes in one layer", ["layer|base|bottom"]), ("multiply by the height for the number of layers", ["height|layers|stack"])], "Length × width tells you how many 1 cm cubes cover the bottom layer. The height tells you how many layers there are, so multiply by the height.", o="O4"),
      deep=[vo1, vo2])

# ================================================================== 15.5
s = U.section("15.5", "Calculating the surface area of cubes and cuboids", ["O5"])
s.idea("Surface area", ["The **surface area** is the total area of all the faces. A cuboid has 6 rectangular faces in 3 matching pairs.",
       "**Surface area = 2(lw + lh + wh).** A cube with edge a has surface area 6a²."], fig=CUB(4, 3, 2))
s.check(N("Find the surface area of a cube with edges of 3 cm.", 54, "cm²", units=["cm²"], o="O5"))
s.idea("Why the faces come in pairs", ["A cuboid has 6 faces in 3 matching pairs: top and bottom, front and back, left and right. Find the 3 different areas and double their total.",
       "Surface area is a flat area wrapped around the solid, so it is measured in cm², not cm³."])
s.check(MC("Before you read on: a cube has edges of 2 cm. What is its surface area?", "24 cm²", [("8 cm²", "That is its volume, 2 × 2 × 2 (in cm³)."), ("4 cm²", "That is one face; there are 6.")], o="O5"))
s.mistake("All six faces", ["Remember the faces you cannot see in the picture."])


def s1(r):
    a = r.randint(2, 10)
    return N(f"Find the surface area of a cube with edges of {a} cm.", 6 * a * a, "cm²", units=["cm²"], o="O5")
def s2(r):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    return N("Find the surface area of the cuboid.", 2 * (a * b + a * c + b * c), "cm²", units=["cm²"], o="O5", fig=CUB(a, b, c))
def s3(r):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    return TB("Find the area of each pair of faces of the cuboid.", ["Faces", "Area of one (cm²)"], [["Top and bottom", B(a * b)], ["Front and back", B(a * c)], ["Two ends", B(b * c)]], o="O5", fig=CUB(a, b, c))
def s4(r):
    a = r.randint(2, 9)
    return N(f"A cube has a surface area of {6 * a * a} cm². What is the area of one face?", a * a, "cm²", units=["cm²"], o="O5")
def s5(r):
    return MC("How many faces does a cuboid have?", "6", ["4", "8", "12"], o="O5")
def s6(r):
    a, b, c = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
    return N(f"A box {a} cm by {b} cm by {c} cm has no lid. Find the area of card needed to make it.", 2 * (a * c + b * c) + a * b, "cm²", units=["cm²"], o="O5", d="VH")
def s7(r):
    a = r.randint(2, 9)
    return N(f"A cube has a surface area of {6 * a * a} cm². How long is each edge?", a, "cm", units=["cm"], o="O5", d="H")


def sa1(r):   # spot the error: volume vs SA
    a = r.randint(2, 6)
    return MC(f"Sam says a cube with edge {a} cm has surface area {a ** 3} cm². What is the right answer?", f"{6 * a * a} cm²", [(f"{a ** 3} cm²", "That is the volume (in cm³)."), (f"{a * a} cm²", "That is one face.")], o="O5", d="H", reason=f"6 faces × {a} × {a} = {6 * a * a} cm².")
def sa2(r):   # compare two boxes decision
    return MC("Box A is 4 × 4 × 4 cm and box B is 8 × 4 × 2 cm. Both hold 64 cm³. Which needs less card to make?", "Box A", [("Box B", "B: 2(32 + 16 + 8) = 112 cm²; A: 6 × 16 = 96 cm²."), ("They need the same", "Equal volumes can have different surface areas.")], o="O5", d="VH",
              reason="A cube uses the least surface area for its volume: 96 cm² for A, 112 cm² for B.")


s.std([s2, s3, s1, s4, s5, s6, s7], EX("Explain how to find the surface area of a cuboid.", [("find the area of each face (3 pairs of equal rectangles)", ["each face|pairs|rectangle"]), ("add all 6 areas together", ["add|total|six|6"])], "A cuboid has 6 faces in 3 matching pairs. Find the area of each rectangle and add all six areas together: 2(lw + lh + wh).", o="O5"),
      deep=[sa1, sa2])

U.mindmap(("Area units", "1 cm² = 100 mm² • 1 m² = 10 000 cm²", "O1", "15.1"), ("Hectares", "1 ha = 10 000 m²", "O2", "15.2"),
          ("Triangles", "½ × base × height", "O3", "15.3"), ("Volume", "l × w × h • cube a³", "O4", "15.4"), ("Surface area", "Add all six faces", "O5", "15.5"))
