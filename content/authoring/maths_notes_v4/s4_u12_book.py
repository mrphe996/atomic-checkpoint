# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u12 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(12, "12.1")]["book"] = BK(
    keys=[("face", "a flat or curved surface"), ("edge", "where two faces meet"), ("vertex", "a corner")],
    intro=[], examples=[],
    exercise=[
        Ex("Faces, edges, vertices?", ("cube", "6, 12, 8"), ("square-based pyramid", "5, 8, 5"), ("triangular prism", "5, 9, 6")),
        Ex("Find three 3D shapes at home. Name them and count their faces.", ans="Answers vary.", think=True),
    ],
    check=["Can I describe 3D shapes by their faces, edges and vertices?"], look=[], note=NOTE)

N[(12, "12.2")]["book"] = BK(
    keys=[("net", "a flat shape that folds into a 3D shape")],
    intro=[], examples=[],
    exercise=[
        Ex("Which 3D shape?", ("6 squares", "cube"), ("1 square + 4 triangles", "square-based pyramid"), ("2 triangles + 3 rectangles", "triangular prism")),
        Ex("Draw two different nets of a cube on squared paper. Cut them out and fold to check.", ans="Answers vary.", think=True),
    ],
    check=["Can I identify and sketch nets of 3D shapes?"], look=[], note=NOTE)
