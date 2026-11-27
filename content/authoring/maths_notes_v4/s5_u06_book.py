# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u06 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(6, "6.1")]["book"] = BK(
    keys=[("net", "a flat shape that folds to make a 3D shape"), ("face", "a flat surface of a 3D shape")],
    intro=[], examples=[],
    exercise=[
        Ex("How many squares are in a net of a cube?", ans="6"),
        Ex("Draw two different nets of a cube on squared paper.", ans="Answers vary – check each folds into a cube.", think=True),
        Ex("A row of 4 squares with one square above and one below the second square. Is it a net of a cube?", ans="Yes"),
    ],
    check=["Can I tell whether a net folds into a cube?"], look=[], note=NOTE)

N[(6, "6.2")]["book"] = BK(
    keys=[("edge", "where two faces meet"), ("vertex", "a corner where edges meet (plural: vertices)")],
    intro=[], examples=[],
    exercise=[
        Ex("Give the number of faces, edges and vertices.", ("cube", "6, 12, 8"), ("square-based pyramid", "5, 8, 5"), ("triangular prism", "5, 9, 6")),
        Ex("Sketch a cuboid on isometric paper.", ans="Answers vary.", think=True),
    ],
    check=["Can I describe 3D shapes using faces, edges and vertices?"], look=[], note=NOTE)
