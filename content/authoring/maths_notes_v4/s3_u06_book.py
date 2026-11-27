# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u06 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(6, "6.1")]["book"] = BK(
    keys=[("unit fraction", "1 on top, e.g. 1/3"), ("non-unit fraction", "more than 1 on top, e.g. 2/3")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the fraction shaded.", ("4 equal parts, 3 shaded", "3/4"), ("5 equal parts, 1 shaded", "1/5"), ("10 equal parts, 9 shaded", "9/10")),
        Ex("Fold a paper square into quarters and colour 3/4.", ans="Answers vary.", think=True),
    ],
    check=["Can I name unit and non-unit fractions of shapes?"], look=[], note=NOTE)

N[(6, "6.2")]["book"] = BK(
    keys=[("equivalent fractions", "fractions that are the same amount")],
    intro=[], examples=[],
    exercise=[
        Ex("Complete.", ("1/2 = ?/4", "2"), ("1/2 = ?/8", "4"), ("1/4 = ?/8", "2"), ("1/5 = ?/10", "2")),
        Ex("Draw two bars to show that 1/2 = 3/6.", ans="Answers vary.", think=True),
    ],
    check=["Can I show equivalent fractions such as 1/2 = 2/4?"], look=[], note=NOTE)
