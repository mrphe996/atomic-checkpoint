# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u02 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(2, "2.1")]["book"] = BK(
    keys=[("equilateral", "3 equal sides"), ("isosceles", "2 equal sides"), ("scalene", "no equal sides")],
    intro=[], examples=[],
    exercise=[
        Ex("Name the triangle.", ("9 cm, 9 cm, 9 cm", "equilateral"), ("5 cm, 8 cm, 5 cm", "isosceles"), ("angles 90°, 30°, 60°", "right-angled scalene")),
        Ex("Draw a right-angled isosceles triangle on squared paper.", ans="e.g. two equal sides of 4 squares at a right angle."),
    ],
    check=["Can I name triangles by their sides and angles?"], look=[], note=NOTE)

N[(2, "2.2")]["book"] = BK(
    keys=[("line of symmetry", "a fold line where the two halves match")],
    intro=[], examples=[],
    exercise=[
        Ex("How many lines of symmetry?", ("square", "4"), ("rectangle", "2"), ("letter E", "1"), ("letter S", "0")),
        Ex("Design a symmetrical pattern on squared paper with a diagonal mirror line.", ans="Answers vary.", think=True),
    ],
    check=["Can I find lines of symmetry and complete symmetrical patterns?"], look=[], note=NOTE)
