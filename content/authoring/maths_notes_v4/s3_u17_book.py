# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u17 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(17, "17.1")]["book"] = BK(
    keys=[("line of symmetry", "a fold line where both halves match")],
    intro=[], examples=[],
    exercise=[
        Ex("How many lines of symmetry?", ("square", "4"), ("rectangle", "2"), ("letter A", "1"), ("letter J", "0")),
        Ex("Fold and cut a symmetrical shape from paper. Mark its line of symmetry.", ans="Answers vary.", think=True),
    ],
    check=["Can I name 2D shapes and find lines of symmetry?"], look=[], note=NOTE)

N[(17, "17.2")]["book"] = BK(
    keys=[("repeating unit", "the part of a pattern that repeats"), ("symmetrical pattern", "the same on both sides of a line")],
    intro=[], examples=[],
    exercise=[
        Ex("Continue the pattern.", ("● ■ ● ■", "● ■"), ("1 2 3 1 2 3", "1 2 3"), ("A A B A A B", "A A B")),
        Ex("Pattern red, yellow, yellow. What colour is the 12th bead?", ans="yellow"),
    ],
    check=["Can I continue repeating patterns and make symmetrical ones?"], look=[], note=NOTE)
