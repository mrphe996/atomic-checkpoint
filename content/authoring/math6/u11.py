# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 11 3D shapes (11.1 Shapes and nets, 11.2 Capacity and volume).
Written by the Atomic teaching team."""
from kit import *

U = Unit(11, "3D Shapes", "Geometry and measure",
         "Faces, edges and vertices of 3D shapes, nets of cubes, prisms and pyramids, and the difference between capacity and volume.",
         {"O1": {"code": "6Gg.05", "sec": "11.1", "codeNote": "", "t": "Identify and describe 3D shapes by their faces, edges and vertices, and recognise their nets."},
          "O2": {"code": "6Gg.06", "sec": "11.2", "codeNote": "", "t": "Understand the difference between capacity and volume, and find the volume of cuboids by counting cubes."}})
SOL = {"cube": (6, 12, 8), "cuboid": (6, 12, 8), "triangular prism": (5, 9, 6), "square-based pyramid": (5, 8, 5), "triangular pyramid": (4, 6, 4), "pentagonal prism": (7, 15, 10)}
FIGK = {"cube": "cuboid", "cuboid": "cuboid", "triangular prism": "triprism", "square-based pyramid": "pyramid"}
CUB = lambda a, b, c: {"kind": "solid", "solid": "cuboid", "a": a, "b": b, "c": c}

s = U.section("11.1", "Shapes and nets", ["O1"])
s.idea("Faces, edges and vertices", ["A **face** is a flat surface. An **edge** is where two faces meet. A **vertex** is a corner (plural **vertices**).",
       "A cube has 6 faces, 12 edges and 8 vertices."], fig=CUB("", "", ""))
s.check(N("How many faces does a triangular prism have?", 5, o="O1"))
s.idea("Nets", ["A **net** is a flat shape that folds up to make a 3D shape. A cube has 11 different nets, each made of 6 squares.",
       "A **prism** has the same cross-section all the way through. A **pyramid** has a base and triangular faces meeting at a point."], fig={"kind": "solid", "solid": "triprism"})
s.mistake("Six squares are not enough", ["Not every arrangement of 6 squares folds into a cube: check that no two faces overlap."])


def s1(r):
    n = pick(r, list(FIGK))
    p = pick(r, ["faces", "edges", "vertices"]); i = ["faces", "edges", "vertices"].index(p)
    return N(f"How many {p} does this shape have?", SOL[n][i], o="O1", fig={"kind": "solid", "solid": FIGK[n]})
def s2(r):
    ns = r.sample(list(SOL), 3)
    return TB("Complete the table.", ["Shape", "Faces", "Edges", "Vertices"], [[n, B(SOL[n][0]), B(SOL[n][1]), B(SOL[n][2])] for n in ns], o="O1")
def s3(r):
    n = pick(r, list(SOL)); p = pick(r, ["faces", "edges", "vertices"]); i = ["faces", "edges", "vertices"].index(p)
    return N(f"How many {p} does a {n} have?", SOL[n][i], o="O1")
def s4(r):
    n = pick(r, ["cube", "triangular prism", "square-based pyramid", "triangular pyramid"])
    d = {"cube": "6 squares", "triangular prism": "2 triangles and 3 rectangles", "square-based pyramid": "1 square and 4 triangles", "triangular pyramid": "4 triangles"}[n]
    return MC(f"A net is made of {d}. Which shape does it fold into?", n, [x for x in ["cube", "triangular prism", "square-based pyramid", "triangular pyramid"] if x != n], o="O1")
def s5(r):
    return MS("Select ALL the shapes that are prisms.", r.sample(["cube", "cuboid", "triangular prism", "pentagonal prism"], 2), r.sample(["square-based pyramid", "triangular pyramid", "cone", "sphere"], 2), o="O1")
def s6(r):
    n = pick(r, list(SOL)); f, e, v = SOL[n]
    return N(f"A {n} has {f} faces and {v} vertices. Use faces + vertices − edges = 2 to find the number of edges.", e, o="O1", d="H")
def s7(r):
    e = r.randint(2, 9)
    return N(f"A cube has edges of {e} cm. What is the total length of all its edges?", 12 * e, "cm", units=["cm"], o="O1", d="H", fig=CUB(f"{e} cm", f"{e} cm", f"{e} cm"))
def s8(r):
    n = pick(r, ["cube", "cuboid", "triangular prism", "square-based pyramid"])
    f = {"cube": "squares only", "cuboid": "rectangles", "triangular prism": "triangles and rectangles", "square-based pyramid": "a square and triangles"}[n]
    return S(f"Which shape has faces that are {f}? Choose from cube, cuboid, triangular prism or square-based pyramid.", [n], o="O1")


s.std([s1, s2, s3, s4, s5, s8, s6, s7], EX("Explain why a cube has 8 vertices.", [("there are 4 corners on the top face", "4|four|top"), ("and 4 on the bottom face: 4 + 4 = 8", "bottom|4 ?\\+ ?4|8")], "A cube has 4 corners on its top face and 4 corners on its bottom face, so it has 4 + 4 = 8 vertices.", o="O1"))

s = U.section("11.2", "Capacity and volume", ["O2"])
s.idea("Capacity and volume", ["**Capacity** is how much a container can hold, usually in **millilitres (ml)** and **litres (l)**: 1 l = 1000 ml.",
       "**Volume** is how much space a solid takes up. It can be measured by counting **cubes**, in **cm³**. A cuboid 4 cm × 3 cm × 2 cm holds 4 × 3 × 2 = **24 cm³**."], fig=CUB("4 cm", "3 cm", "2 cm"))
s.check(N("How many millilitres are in 2.5 litres?", 2500, "ml", units=["ml"], o="O2"))
s.mistake("Count every layer", ["A cuboid of cubes has more than one layer: count one layer, then multiply by the number of layers."])


def v1(r):
    a, b, c = r.randint(2, 8), r.randint(2, 6), r.randint(2, 5)
    return N("The cuboid is made of 1 cm cubes. What is its volume?", a * b * c, "cm³", units=["cm³"], o="O2", fig=CUB(f"{a} cm", f"{b} cm", f"{c} cm"))
def v2(r):
    l = round(r.randint(5, 95) / 10, 1)
    return N(f"Change {fmt(l)} litres into millilitres.", round(l * 1000), "ml", units=["ml"], o="O2")
def v3(r):
    m = r.randint(2, 99) * 50
    return N(f"Change {m} ml into litres.", m / 1000, "l", units=["l", "litres"], o="O2")
def v4(r):
    a, b, c = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
    return TB("Complete the table for cuboids made of 1 cm cubes.", ["Length", "Width", "Height", "Volume (cm³)"], [[str(a), str(b), str(c), B(a * b * c)], [str(b), str(c), "1", B(b * c)]], o="O2")
def v5(r):
    cap, g = r.randint(2, 9) * 250, pick(r, [100, 200, 250])
    if cap % g: return None
    return N(f"A jug holds {cap} ml. How many {g} ml glasses can it fill?", cap // g, "glasses", units=["glasses"], o="O2")
def v6(r):
    a, b, h = r.randint(2, 6), r.randint(2, 6), r.randint(2, 5)
    return N(f"A box is {a} cubes long and {b} cubes wide. It holds {a * b * h} cubes when full. How many layers are there?", h, "layers", units=["layers"], o="O2", d="H")
def v7(r):
    return MC("Which word describes how much liquid a bottle can hold?", "capacity", ["volume of the plastic", "area", "perimeter"], o="O2")
def v8(r):
    l1, m = r.randint(1, 4), r.randint(2, 8) * 100
    return N(f"A tank has {l1} litres of water. {m} ml is poured out. How much is left in millilitres?", l1 * 1000 - m, "ml", units=["ml"], o="O2", d="H")


s.std([v1, v4, v2, v3, v5, v7, v6, v8], EX("Explain the difference between capacity and volume.", [("capacity is how much a container can hold", "hold|container|liquid"), ("volume is the space a solid takes up", "space|takes up|solid")], "Capacity is how much a container can hold (e.g. litres of water). Volume is how much space an object takes up (e.g. cm³).", o="O2"))

U.mindmap(("3D shapes", "Faces • edges • vertices • prisms and pyramids", "O1", "11.1"), ("Nets", "Flat shapes that fold into solids", "O1", "11.1"), ("Capacity and volume", "1 l = 1000 ml • count cubes in cm³", "O2", "11.2"))
