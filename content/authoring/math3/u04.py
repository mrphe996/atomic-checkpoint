# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 4 3D shapes (4.1 Naming 3D shapes, 4.2 Faces, edges and vertices).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(4, "3D Shapes", "Geometry and measure",
         "Naming cubes, cuboids, cylinders, cones, spheres, pyramids and prisms, and counting their faces, edges and vertices.",
         {"O1": {"code": "3Gg.01", "sec": "4.1", "codeNote": "", "t": "Identify, describe and sort 3D shapes, including prisms and pyramids, and find them in everyday objects."},
          "O2": {"code": "3Gg.02", "sec": "4.2", "codeNote": "", "t": "Count the faces, edges and vertices of 3D shapes."}})
FIGK = {"cube": "cuboid", "cuboid": "cuboid", "cylinder": "cylinder", "cone": "cone", "square-based pyramid": "pyramid", "triangular prism": "triprism"}
SOL = {"cube": (6, 12, 8), "cuboid": (6, 12, 8), "square-based pyramid": (5, 8, 5), "triangular prism": (5, 9, 6), "cylinder": (3, 2, 0), "cone": (2, 1, 1)}
THINGS = [("a tin of beans", "cylinder"), ("a football", "sphere"), ("a dice", "cube"), ("a cereal box", "cuboid"), ("an ice-cream cone", "cone"), ("a tent", "triangular prism"), ("a party hat", "cone"), ("a brick", "cuboid"), ("a marble", "sphere"), ("a drinking straw", "cylinder")]

s = U.section("4.1", "Naming 3D shapes", ["O1"])
s.idea("Solid shapes", ["3D shapes are solid. Some have **flat faces** (cube, cuboid, pyramid, prism) and some have **curved surfaces** (sphere, cylinder, cone).",
       "A **prism** is the same shape all the way through. A **pyramid** has faces that meet at a point."], fig={"kind": "solid", "solid": "cylinder"})
s.check(MC("Which shape is a football?", "sphere", [("cylinder", ""), ("cube", ""), ("cone", "")], o="O1"))
s.check(MC('Before you read on: which shape rolls: a cube or a cylinder?', 'A cylinder', [('A cube', 'A cube has only flat faces.'), ('Both', 'Only shapes with a curved surface roll.')], o='O1'))
s.mistake("Square or cube?", ["A square is flat (2D). A cube is solid (3D) and has 6 square faces."])


def n1(r):
    n = pick(r, list(FIGK))
    return S("Name this 3D shape.", [n, "a " + n], o="O1", fig={"kind": "solid", "solid": FIGK[n]})
def n2(r):
    th, sh = pick(r, THINGS)
    return MC(f"What shape is {th}?", sh, [x for x in ["cylinder", "sphere", "cube", "cuboid", "cone", "triangular prism"] if x != sh][:3], o="O1")
def n3(r):
    ts = r.sample(THINGS, 4)
    return GD("Match each object to its shape.", "Shape", [(t, s_) for t, s_ in ts], o="O1", extra=["cylinder", "sphere", "cube", "cuboid", "cone", "triangular prism"])
def n4(r):
    return MS("Select ALL the shapes that can roll.", ["sphere", "cylinder", "cone"][:r.randint(2, 3)], ["cube", "cuboid", "square-based pyramid"], o="O1")
def n5(r):
    n = pick(r, ["cube", "cuboid", "triangular prism", "square-based pyramid"])
    return MC("Is this shape a prism or a pyramid?", "pyramid" if "pyramid" in n else "prism", ["prism" if "pyramid" in n else "pyramid", "neither"], o="O1", fig={"kind": "solid", "solid": FIGK[n]}, d="H")
def n6(r):
    return MC("Which shape has no flat faces at all?", "sphere", ["cylinder", "cone", "cube"], o="O1")
def n7(r):
    n = pick(r, ["cube", "square-based pyramid"])
    return MC(f"Which 2D shape is the base of a {n}?", "square", ["circle", "triangle", "rectangle" if n == "square-based pyramid" else "pentagon"], o="O1")
def n8(r):
    n = pick(r, ["cylinder", "cone"])
    return MC(f"What shape is the flat face of a {n}?", "circle", ["square", "triangle", "rectangle"], o="O1", fig={"kind": "solid", "solid": n})


s.std([n1, n5, n2, n3, n4, n6, n7, n8], EX("Explain how a cube and a sphere are different.", [("a cube has flat square faces", "flat|square|faces"), ("a sphere is curved all over / can roll", "curved|round|roll")], "A cube has 6 flat square faces, corners and straight edges. A sphere is curved all over, with no flat faces or corners, so it can roll.", o="O1"))

s = U.section("4.2", "Faces, edges and vertices", ["O2"])
s.idea("Counting parts", ["A **face** is a surface. An **edge** is where two faces meet. A **vertex** is a corner (more than one: **vertices**).",
       "A cube has 6 faces, 12 edges and 8 vertices."], fig={"kind": "solid", "solid": "cuboid", "a": "", "b": "", "c": ""})
s.check(N("How many faces does a cube have?", 6, "faces", units=["faces"], o="O2"))
s.check(MC('Before you read on: how many faces does a cube have?', '6', [('4', 'Count top, bottom and 4 sides.'), ('8', '8 is the number of corners.')], o='O2'))
s.mistake("Hidden parts", ["Some faces, edges and corners are at the back. Count those too."])


def f1(r):
    n = pick(r, ["cube", "square-based pyramid", "triangular prism"]); p = pick(r, ["faces", "edges", "vertices"]); i = ["faces", "edges", "vertices"].index(p)
    return N(f"How many {p} does this shape have?", SOL[n][i], o="O2", fig={"kind": "solid", "solid": FIGK[n]})
def f2(r):
    ns = r.sample(["cube", "square-based pyramid", "triangular prism", "cuboid"], 3)
    return TB("Complete the table.", ["Shape", "Faces", "Vertices"], [[n, B(SOL[n][0]), B(SOL[n][2])] for n in ns], o="O2")
def f3(r):
    n = pick(r, list(SOL)); p = pick(r, ["faces", "vertices"]); i = ["faces", "edges", "vertices"].index(p)
    return N(f"How many {p} does a {n} have?", SOL[n][i], o="O2")
def f4(r):
    k = r.randint(2, 5)
    return N(f"How many vertices do {k} cubes have altogether?", 8 * k, "vertices", units=["vertices"], o="O2", d="H")
def f5(r):
    return MC("Which shape has 5 faces and 5 vertices?", "square-based pyramid", ["cube", "triangular prism", "cylinder"], o="O2")
def f6(r):
    return MC("How many of a cube's faces are squares?", "6", ["4", "5", "8"], o="O2")
def f7(r):
    k = r.randint(2, 4)
    return N(f"How many faces do {k} square-based pyramids have altogether?", 5 * k, "faces", units=["faces"], o="O2", d="H")
def f8(r):
    return MC("Which word means a corner of a 3D shape?", "vertex", ["face", "edge", "side"], o="O2")


s.std([f1, f2, f3, f5, f6, f8, f4, f7], EX("Explain why a cube has 8 vertices.", [("4 corners on the top", "4|four|top"), ("4 corners on the bottom: 4 + 4 = 8", "bottom|4 ?\\+ ?4|\\b8\\b")], "A cube has 4 corners on its top face and 4 on its bottom face, so it has 4 + 4 = 8 vertices.", o="O2"))

U.mindmap(("3D shapes", "Cube • cuboid • sphere • cylinder • cone • prism • pyramid", "O1", "4.1"), ("Parts", "Faces • edges • vertices", "O2", "4.2"))
