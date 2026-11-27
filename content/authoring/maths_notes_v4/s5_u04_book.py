# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u04 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(4, "4.1")]["book"] = BK(
    keys=[("mode", "the most common value")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the mode.", ("6, 2, 6, 8, 6", "6"), ("red, blue, blue, green", "blue"), ("4, 4, 7, 7, 9", "4 and 7")),
        Ex("Ask 10 people their favourite fruit and find the mode.", ans="Answers vary.", think=True),
    ],
    check=["Can I find the mode?"], look=[], note=NOTE)

N[(4, "4.2")]["book"] = BK(
    keys=[("median", "the middle value when data is in order")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the median.", ("12, 5, 9, 3, 7", "7"), ("4, 10, 6, 8", "7"), ("1.2, 0.8, 1.5", "1.2")),
    ],
    check=["Can I find the median of odd and even sets?"], look=[], note=NOTE)
