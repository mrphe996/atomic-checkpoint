# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u04 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(4, "4.1")]["book"] = BK(
    keys=[("prism", "the same shape all the way through"), ("pyramid", "triangle faces meeting at an apex")],
    intro=[], examples=[],
    exercise=[
        Ex("Name the 3D shape.", ("a football", "sphere"), ("a dice", "cube"), ("a tin", "cylinder"), ("a tent", "triangular prism")),
        Ex("Find five 3D shapes at home and name them.", ans="Answers vary.", think=True),
    ],
    check=["Can I name and sort 3D shapes?"], look=[], note=NOTE)

N[(4, "4.2")]["book"] = BK(
    keys=[("face", "a flat or curved surface"), ("edge", "where two faces meet"), ("vertex", "a corner")],
    intro=[], examples=[],
    exercise=[
        Ex("Faces, edges, vertices?", ("cube", "6, 12, 8"), ("square-based pyramid", "5, 8, 5"), ("triangular prism", "5, 9, 6"), ("cylinder", "3, 2, 0")),
    ],
    check=["Can I count faces, edges and vertices?"], look=[], note=NOTE)
