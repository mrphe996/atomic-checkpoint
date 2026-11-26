# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 6 3D shapes (6.1 Nets of cubes, 6.2 Describing and drawing 3D shapes).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(6, "3D Shapes", "Geometry and measure",
         "Nets of cubes and other solids, counting faces, edges and vertices, and drawing and recognising 3D shapes from different views.",
         {"O1": {"code": "5Gg.03", "sec": "6.1", "codeNote": "", "t": "Identify and sketch different nets for a cube and other simple 3D shapes."},
          "O2": {"code": "5Gg.04", "sec": "6.2", "codeNote": "", "t": "Describe 3D shapes by their faces, edges and vertices, and recognise them from drawings and views."}})
SOL = {"cube": (6, 12, 8), "cuboid": (6, 12, 8), "triangular prism": (5, 9, 6), "square-based pyramid": (5, 8, 5), "triangular pyramid": (4, 6, 4)}
FIGK = {"cube": "cuboid", "cuboid": "cuboid", "triangular prism": "triprism", "square-based pyramid": "pyramid", "cylinder": "cylinder", "cone": "cone"}
CUBE_NETS = [[[1, 0], [0, 1], [1, 1], [2, 1], [3, 1], [1, 2]], [[0, 0], [0, 1], [1, 1], [2, 1], [3, 1], [3, 2]], [[1, 0], [1, 1], [0, 1], [2, 1], [3, 1], [2, 2]], [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2]]]
NOT_NETS = [[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [2, 1]], [[0, 0], [1, 0], [0, 1], [1, 1], [2, 1], [3, 1]], [[0, 1], [1, 1], [2, 1], [3, 1], [1, 0], [2, 0]]]


def NET(cells):
    return {"kind": "cells", "cells": cells}


s = U.section("6.1", "Nets of cubes", ["O1"])
s.idea("Unfolding a cube", ["A **net** is a flat shape that folds up to make a 3D shape. A cube has **6 square faces**, so every net of a cube is made of 6 squares.",
       "There are **11** different nets of a cube. Some arrangements of 6 squares do NOT fold into a cube because two faces would overlap."], fig=NET(CUBE_NETS[0]))
s.check(N("How many squares are in a net of a cube?", 6, "squares", units=["squares"], o="O1"))
s.check(MC('Before you read on: how many squares are in the net of a cube?', '6', [('4', 'A cube has 6 faces.'), ('8', '8 is the number of vertices.')], o='O1'))
s.mistake("A row of 5", ["Five squares in a row cannot fold into a cube: the end squares overlap."])


def n1(r):
    ok = r.random() < 0.5
    c = pick(r, CUBE_NETS if ok else NOT_NETS)
    return MC("Will this net fold up to make a cube?", "Yes" if ok else "No", ["No" if ok else "Yes"], o="O1", fig=NET(c))
def n2(r):
    n = pick(r, ["cube", "triangular prism", "square-based pyramid", "triangular pyramid"])
    d = {"cube": "6 squares", "triangular prism": "2 triangles and 3 rectangles", "square-based pyramid": "1 square and 4 triangles", "triangular pyramid": "4 triangles"}[n]
    return MC(f"A net is made of {d}. Which shape does it make?", n, [x for x in ["cube", "triangular prism", "square-based pyramid", "triangular pyramid"] if x != n], o="O1")
def n3(r):
    n = pick(r, ["cuboid", "triangular prism", "square-based pyramid"])
    return N(f"How many faces will the net of a {n} have?", SOL[n][0], "faces", units=["faces"], o="O1", fig={"kind": "solid", "solid": FIGK[n]})
def n4(r):
    e = r.randint(2, 9)
    return N(f"Each square in a cube net is {e} cm by {e} cm. What is the total area of the net?", 6 * e * e, "cm²", units=["cm²"], o="O1", d="H")
def n5(r):
    ns = r.sample(["cube", "cuboid", "triangular prism", "square-based pyramid", "triangular pyramid"], 4)
    sh = {"cube": "squares", "cuboid": "rectangles", "triangular prism": "triangles and rectangles", "square-based pyramid": "a square and triangles", "triangular pyramid": "triangles"}
    return GD("What shapes are in the net of each solid?", "Faces", [(n, sh[n]) for n in ns], o="O1", extra=list(set(sh.values())))
def n6(r):
    return MS("Select ALL the true statements about nets of a cube.", ["Every net has 6 squares", "There is more than one net"], ["Any 6 squares joined together make a net", "A net can have 5 squares in a row"], o="O1")
def n7(r):
    return MC("Which 3D shape has a net with 2 circles and a rectangle?", "cylinder", ["cone", "sphere", "cuboid"], o="O1")
def n8(r):
    k = r.randint(2, 5)
    return N(f"Tom makes {k} cubes from card. How many square faces does he need to cut out?", 6 * k, "faces", units=["faces"], o="O1")


s.std([n1, n3, n2, n5, n6, n7, n8, n4], EX("Explain why 6 squares in a row is not a net of a cube.", [("when you fold it the end squares overlap", "overlap|same place|on top"), ("one face of the cube is left open", "open|missing|gap")], "If you fold 6 squares in a row, the squares wrap round and overlap each other, leaving two sides of the cube open. So it is not a net of a cube.", o="O1"))

s = U.section("6.2", "Describing and drawing 3D shapes", ["O2"])
s.idea("Faces, edges and vertices", ["A **face** is a flat or curved surface, an **edge** is where two faces meet and a **vertex** is a corner.",
       "A cuboid has 6 faces, 12 edges and 8 vertices. On isometric (dotty) paper we can draw 3D shapes so they look solid."], fig={"kind": "solid", "solid": "cuboid", "a": "", "b": "", "c": ""})
s.check(N("How many vertices does a square-based pyramid have?", 5, o="O2"))
s.check(MC('Before you read on: which 3D shape has 5 faces: 2 triangles and 3 rectangles?', 'Triangular prism', [('Square-based pyramid', 'That has 1 square and 4 triangles.'), ('Cube', 'A cube has 6 squares.')], o='O2'))
s.mistake("Hidden edges", ["Some edges are hidden at the back. Dashed lines show them."])


def d1(r):
    n = pick(r, ["cube", "triangular prism", "square-based pyramid"])
    p = pick(r, ["faces", "edges", "vertices"]); i = ["faces", "edges", "vertices"].index(p)
    return N(f"How many {p} does this shape have?", SOL[n][i], o="O2", fig={"kind": "solid", "solid": FIGK[n]})
def d2(r):
    ns = r.sample(list(SOL), 3)
    return TB("Complete the table.", ["Shape", "Faces", "Edges", "Vertices"], [[n, B(SOL[n][0]), B(SOL[n][1]), B(SOL[n][2])] for n in ns], o="O2")
def d3(r):
    n = pick(r, ["cylinder", "cone", "cuboid", "triangular prism", "square-based pyramid"])
    return S("Name this 3D shape.", [n, "a " + n], o="O2", fig={"kind": "solid", "solid": FIGK[n]})
def d4(r):
    n = pick(r, list(SOL)); p = pick(r, ["faces", "edges", "vertices"]); i = ["faces", "edges", "vertices"].index(p)
    return N(f"How many {p} does a {n} have?", SOL[n][i], o="O2")
def d5(r):
    return MS("Select ALL the shapes that have at least one curved surface.", ["cylinder", "cone", "sphere"][:r.randint(2, 3)], ["cube", "triangular prism", "square-based pyramid"], o="O2")
def d6(r):
    n = pick(r, ["cylinder", "cone", "cube"])
    v = {"cylinder": "a circle", "cone": "a circle", "cube": "a square"}[n]
    return MC(f"A {n} stands on a table. What shape do you see when you look straight down from above?", v, [x for x in ["a circle", "a square", "a triangle", "a rectangle"] if x != v][:3], o="O2")
def d7(r):
    a, b = r.randint(2, 5), r.randint(2, 4)
    return N(f"A shape is built from cubes: {a} cubes in a row, and {b} rows like that. How many cubes are there?", a * b, "cubes", units=["cubes"], o="O2", fig={"kind": "solid", "solid": "cuboid", "a": f"{a} cubes", "b": f"{b} rows", "c": "1 cube"})
def d8(r):
    k = r.randint(2, 4)
    return N(f"{k} cubes are joined face to face in a row. How many faces of the small cubes are hidden where they join?", 2 * (k - 1), "faces", units=["faces"], o="O2", d="H")


s.std([d1, d3, d7, d2, d4, d5, d6, d8], EX("Explain how a cube and a cuboid are the same and different.", [("both have 6 faces, 12 edges and 8 vertices", "6 faces|12 edges|8 vertices|same number"), ("a cube's faces are all squares, a cuboid's can be rectangles", "square|rectangle")], "Both have 6 faces, 12 edges and 8 vertices. All the faces of a cube are equal squares, but a cuboid can have rectangular faces.", o="O2"))

U.mindmap(("Nets", "6 squares for a cube • 11 nets", "O1", "6.1"), ("3D shapes", "Faces • edges • vertices • views", "O2", "6.2"))
