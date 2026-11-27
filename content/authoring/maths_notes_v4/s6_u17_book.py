# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u17 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(17, "17.1")]["book"] = BK(
    keys=[("quadrant", "one of the four parts of a coordinate grid"), ("translation", "a slide without turning")],
    intro=[], examples=[],
    exercise=[
        Ex("Plot and join (−3, 1), (2, 1), (2, −2), (−3, −2). What shape is it?", ans="a rectangle"),
        Ex("Translate the rectangle 4 right and 3 up. Give the new vertices.", ans="(1, 4), (6, 4), (6, 1), (1, 1)"),
    ],
    check=["Can I use coordinates in four quadrants and translate shapes?"], look=[], note=NOTE)

N[(17, "17.2")]["book"] = BK(
    keys=[("mirror line", "the line a shape is reflected in")],
    intro=[], examples=[],
    exercise=[
        Ex("Reflect the triangle (1, 2), (4, 2), (1, 5)", ("in the y-axis", "(−1, 2), (−4, 2), (−1, 5)"), ("in the x-axis", "(1, −2), (4, −2), (1, −5)")),
    ],
    check=["Can I reflect shapes in horizontal and vertical lines?"], look=[], note=NOTE)

N[(17, "17.3")]["book"] = BK(
    keys=[("centre of rotation", "the point a shape turns about"), ("clockwise", "the way clock hands turn")],
    intro=[], examples=[],
    exercise=[
        Ex("Rotate the triangle (0, 0), (3, 0), (0, 2) about (0, 0)", ("90° clockwise", "(0, 0), (0, −3), (2, 0)"), ("90° anticlockwise", "(0, 0), (0, 3), (−2, 0)")),
    ],
    check=["Can I rotate shapes 90° about a vertex?"], look=[], note=NOTE)
