# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 15 Shapes, area and volume (15.1 Converting between units for area, 15.2 Using hectares,
15.3 The area of a triangle, 15.4 Volume of cubes and cuboids, 15.5 Surface area of cubes and cuboids).
Written by the Atomic teaching team."""
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


s.std([u5, u6, u1, u2, u3, u4, u7], EX("Explain why 1 m² = 10 000 cm².", [("1 m = 100 cm", ["100 ?cm"]), ("a 1 m square is 100 cm by 100 cm: 100 × 100 = 10 000", ["100 ?× ?100|10 ?000"])], "1 m = 100 cm, so a square 1 m by 1 m is 100 cm by 100 cm. Its area is 100 × 100 = 10 000 cm².", o="O1"))

# ================================================================== 15.2
s = U.section("15.2", "Using hectares", ["O2"])
s.idea("Hectares", ["A **hectare** (ha) is used for large areas such as fields and parks. **1 hectare = 10 000 m²** – a square 100 m by 100 m."])
s.check(N("A field is 3 hectares. How many square metres is that?", 30000, "m²", units=["m²"], o="O2"))
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


s.std([h5, h6, h1, h2, h3, h4, h7], EX("Explain why a square 100 m by 100 m has an area of 1 hectare.", [("100 × 100 = 10 000 m²", ["10 ?000|100 ?× ?100"]), ("1 hectare = 10 000 m²", ["hectare"])], "The square's area is 100 × 100 = 10 000 m², and 1 hectare is defined as 10 000 m².", o="O2"))

# ================================================================== 15.3
s = U.section("15.3", "The area of a triangle", ["O3"])
s.idea("Half a rectangle", ["A triangle is **half** of a rectangle with the same base and height: **Area = ½ × base × height**.",
       "The height is **perpendicular** (at 90°) to the base."], fig=TRI(8, 5))
s.check(N("Find the area of a triangle with base 10 cm and height 6 cm.", 30, "cm²", units=["cm²"], o="O3"))
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


s.std([t1, t4, t2, t3, t5, t6, t7], EX("Explain why the area of a triangle is ½ × base × height.", [("a triangle is half of a rectangle with the same base and height", ["half.*rectangle|rectangle.*half|two triangles"]), ("the rectangle's area is base × height", ["base ?× ?height|b ?× ?h"])], "Two identical triangles fit together to make a rectangle with the same base and height. The rectangle's area is base × height, so one triangle is half of that.", o="O3"))

# ================================================================== 15.4
s = U.section("15.4", "Calculating the volume of cubes and cuboids", ["O4"])
s.idea("Volume", ["**Volume** is the space inside a 3D shape, measured in cubic units such as cm³.",
       "**Volume of a cuboid = length × width × height.** A cube with edge a has volume a³."], fig=CUB(5, 3, 4))
s.check(N("Find the volume of a cuboid 5 cm by 3 cm by 4 cm.", 60, "cm³", units=["cm³"], o="O4"))
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


s.std([v1, v6, v2, v3, v4, v5, v7], EX("Explain why the volume of a cuboid is length × width × height.", [("length × width gives the number of cubes in one layer", ["layer|base|bottom"]), ("multiply by the height for the number of layers", ["height|layers|stack"])], "Length × width tells you how many 1 cm cubes cover the bottom layer. The height tells you how many layers there are, so multiply by the height.", o="O4"))

# ================================================================== 15.5
s = U.section("15.5", "Calculating the surface area of cubes and cuboids", ["O5"])
s.idea("Surface area", ["The **surface area** is the total area of all the faces. A cuboid has 6 rectangular faces in 3 matching pairs.",
       "**Surface area = 2(lw + lh + wh).** A cube with edge a has surface area 6a²."], fig=CUB(4, 3, 2))
s.check(N("Find the surface area of a cube with edges of 3 cm.", 54, "cm²", units=["cm²"], o="O5"))
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


s.std([s2, s3, s1, s4, s5, s6, s7], EX("Explain how to find the surface area of a cuboid.", [("find the area of each face (3 pairs of equal rectangles)", ["each face|pairs|rectangle"]), ("add all 6 areas together", ["add|total|six|6"])], "A cuboid has 6 faces in 3 matching pairs. Find the area of each rectangle and add all six areas together: 2(lw + lh + wh).", o="O5"))

U.mindmap(("Area units", "1 cm² = 100 mm² • 1 m² = 10 000 cm²", "O1", "15.1"), ("Hectares", "1 ha = 10 000 m²", "O2", "15.2"),
          ("Triangles", "½ × base × height", "O3", "15.3"), ("Volume", "l × w × h • cube a³", "O4", "15.4"), ("Surface area", "Add all six faces", "O5", "15.5"))
