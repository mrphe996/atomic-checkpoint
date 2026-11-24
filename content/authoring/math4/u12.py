# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 12 Investigating 3D shapes and nets (12.1 The properties of 3D shapes, 12.2 Nets of 3D shapes).
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(12, "Investigating 3D Shapes and Nets", "Geometry and measure",
         "Faces, edges and vertices of prisms and pyramids, and nets that fold to make cubes, cuboids, prisms and pyramids.",
         {"O1": {"code": "4Gg.06", "sec": "12.1", "codeNote": "", "t": "Identify, describe and sort 3D shapes by their faces, edges and vertices."},
          "O2": {"code": "4Gg.07", "sec": "12.2", "codeNote": "", "t": "Identify and sketch nets of cubes, cuboids, prisms and pyramids."}})
SOL = {"cube": (6, 12, 8), "cuboid": (6, 12, 8), "triangular prism": (5, 9, 6), "square-based pyramid": (5, 8, 5), "triangular pyramid": (4, 6, 4)}
FIGK = {"cube": "cuboid", "cuboid": "cuboid", "triangular prism": "triprism", "square-based pyramid": "pyramid", "cylinder": "cylinder", "cone": "cone"}
CUBE_NETS = [[[1, 0], [0, 1], [1, 1], [2, 1], [3, 1], [1, 2]], [[0, 0], [0, 1], [1, 1], [2, 1], [3, 1], [3, 2]], [[1, 0], [1, 1], [0, 1], [2, 1], [3, 1], [2, 2]], [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2]]]
NOT_NETS = [[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [2, 1]], [[0, 0], [1, 0], [0, 1], [1, 1], [2, 1], [3, 1]], [[0, 1], [1, 1], [2, 1], [3, 1], [1, 0], [2, 0]]]

s = U.section("12.1", "The properties of 3D shapes", ["O1"])
s.idea("Faces, edges and vertices", ["A **prism** has the same shape at both ends, joined by rectangles. A **pyramid** has a base and triangular faces meeting at a point (the apex).",
       "A triangular prism has 5 faces, 9 edges and 6 vertices."], fig={"kind": "solid", "solid": "triprism"})
s.check(N("How many edges does a cube have?", 12, "edges", units=["edges"], o="O1"))
s.mistake("Count hidden parts", ["Some edges and vertices are at the back. Dashed lines show them."])


def d1(r):
    n = pick(r, ["cube", "triangular prism", "square-based pyramid"]); p = pick(r, ["faces", "edges", "vertices"]); i = ["faces", "edges", "vertices"].index(p)
    return N(f"How many {p} does this shape have?", SOL[n][i], o="O1", fig={"kind": "solid", "solid": FIGK[n]})
def d2(r):
    ns = r.sample(list(SOL), 3)
    return TB("Complete the table.", ["Shape", "Faces", "Edges", "Vertices"], [[n, B(SOL[n][0]), B(SOL[n][1]), B(SOL[n][2])] for n in ns], o="O1")
def d3(r):
    n = pick(r, list(FIGK))
    return S("Name this 3D shape.", [n, "a " + n], o="O1", fig={"kind": "solid", "solid": FIGK[n]})
def d4(r):
    n = pick(r, list(SOL)); p = pick(r, ["faces", "edges", "vertices"]); i = ["faces", "edges", "vertices"].index(p)
    return N(f"How many {p} does a {n} have?", SOL[n][i], o="O1")
def d5(r):
    return GD("Is each shape a prism or a pyramid?", "Type", r.sample([("cube", "prism"), ("cuboid", "prism"), ("triangular prism", "prism"), ("square-based pyramid", "pyramid"), ("triangular pyramid", "pyramid")], 4), o="O1", extra=["prism", "pyramid"])
def d6(r):
    return MC("Which shape has 5 faces and 5 vertices?", "square-based pyramid", ["triangular prism", "cube", "cylinder"], o="O1")
def d7(r):
    a, b = r.randint(2, 5), r.randint(2, 5)
    return N(f"How many faces do {a} cubes and {b} triangular prisms have altogether?", 6 * a + 5 * b, "faces", units=["faces"], o="O1", d="H")
def d8(r):
    n = pick(r, list(SOL)); f, e, v = SOL[n]
    return N(f"A {n} has {f} faces and {v} vertices. Use faces + vertices − 2 to find the number of edges.", e, "edges", units=["edges"], o="O1", d="H")


s.std([d1, d3, d2, d4, d5, d6, d7, d8], EX("Explain the difference between a prism and a pyramid.", [("a prism has the same shape at both ends joined by rectangles", "same shape|both ends|rectangle"), ("a pyramid has triangle faces meeting at a point", "point|apex|triangle")], "A prism has two identical ends joined by rectangular faces. A pyramid has one base and triangular faces that meet at a point.", o="O1"))

s = U.section("12.2", "Nets of 3D shapes", ["O2"])
s.idea("Unfolding solids", ["A **net** is a flat shape that folds up into a 3D shape. A cube has 11 different nets, each of 6 squares.",
       "A net of a square-based pyramid has 1 square and 4 triangles. A net of a triangular prism has 2 triangles and 3 rectangles."], fig={"kind": "cells", "cells": CUBE_NETS[0]})
s.check(N("How many triangles are in the net of a square-based pyramid?", 4, "triangles", units=["triangles"], o="O2"))
s.mistake("Overlaps", ["If two squares fold onto the same place, it is not a net of a cube."])


def n1(r):
    ok = r.random() < 0.5; c = pick(r, CUBE_NETS if ok else NOT_NETS)
    return MC("Will this net fold up to make a cube?", "Yes" if ok else "No", ["No" if ok else "Yes"], o="O2", fig={"kind": "cells", "cells": c})
def n2(r):
    n = pick(r, ["cube", "triangular prism", "square-based pyramid", "triangular pyramid"])
    d = {"cube": "6 squares", "triangular prism": "2 triangles and 3 rectangles", "square-based pyramid": "1 square and 4 triangles", "triangular pyramid": "4 triangles"}[n]
    return MC(f"A net is made of {d}. What shape does it make?", n, [x for x in ["cube", "triangular prism", "square-based pyramid", "triangular pyramid"] if x != n], o="O2")
def n3(r):
    ns = r.sample(["cube", "cuboid", "triangular prism", "square-based pyramid", "triangular pyramid"], 4)
    sh = {"cube": "squares", "cuboid": "rectangles", "triangular prism": "triangles and rectangles", "square-based pyramid": "a square and triangles", "triangular pyramid": "triangles"}
    return GD("What shapes are in each net?", "Faces", [(n, sh[n]) for n in ns], o="O2", extra=list(set(sh.values())))
def n4(r):
    e = r.randint(2, 9)
    return N(f"A cube net is made of squares {e} cm by {e} cm. What is the total area of the net?", 6 * e * e, "cm²", units=["cm²"], o="O2", d="H")
def n5(r):
    k = r.randint(2, 6)
    return N(f"How many squares are needed to make {k} cube nets?", 6 * k, "squares", units=["squares"], o="O2")
def n6(r):
    return MC("Which 3D shape has a net of 2 circles and a rectangle?", "cylinder", ["cone", "cuboid", "sphere"], o="O2")
def n7(r):
    n = pick(r, ["cuboid", "triangular prism", "square-based pyramid"])
    return N(f"How many faces will the net of a {n} have?", SOL[n][0], "faces", units=["faces"], o="O2", fig={"kind": "solid", "solid": FIGK[n]})
def n8(r):
    return MS("Select ALL the true statements about cube nets.", ["every cube net has 6 squares", "there is more than one cube net"], ["any 6 joined squares make a cube", "a cube net can have 5 squares in a row"], o="O2", d="H")


s.std([n1, n7, n2, n3, n5, n6, n4, n8], EX("Explain how you can check whether a net makes a cube.", [("imagine folding the squares up", "fold|imagine"), ("no two faces overlap and none is missing", "overlap|missing|gap|6")], "Imagine folding the squares up around one square as the base. If every side is covered once with no overlap and no gap, it makes a cube.", o="O2"))

U.mindmap(("3D shapes", "Prisms • pyramids • faces, edges, vertices", "O1", "12.1"), ("Nets", "Flat shapes that fold up", "O2", "12.2"))
