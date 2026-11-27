# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u06 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(6, "6.1")]["book"] = BK(
    keys=[("polygon", "a flat shape with straight sides"), ("regular", "all sides and angles equal"), ("tessellate", "fit together with no gaps or overlaps")],
    intro=[], examples=[],
    exercise=[
        Ex("Name the shape.", ("5 sides", "pentagon"), ("8 sides", "octagon"), ("4 sides", "quadrilateral")),
        Ex("Draw a tessellation with squares and another with triangles.", ans="Answers vary.", think=True),
    ],
    check=["Can I name, describe and sort 2D shapes and spot tessellations?"], look=[], note=NOTE)

N[(6, "6.2")]["book"] = BK(
    keys=[("line of symmetry", "a fold line where the halves match")],
    intro=[], examples=[],
    exercise=[
        Ex("How many lines of symmetry?", ("square", "4"), ("rectangle", "2"), ("regular hexagon", "6"), ("letter S", "0")),
        Ex("On squared paper, draw half a shape next to a mirror line and complete it.", ans="Answers vary.", think=True),
    ],
    check=["Can I find lines of symmetry and complete symmetrical shapes?"], look=[], note=NOTE)
