# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u03 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(3, "3.1")]["book"] = BK(
    keys=[("mode", "most common value"), ("median", "middle value in order"), ("mean", "total ÷ number of values"), ("range", "largest − smallest")],
    intro=[], examples=[],
    exercise=[
        Ex("For 6, 9, 4, 9, 7, 3 find", ("the mode", "9"), ("the median", "6.5"), ("the mean", "6.33…"), ("the range", "6")),
        Ex("Record how long 6 friends can stand on one leg. Find the averages and range.", ans="Answers vary.", think=True),
    ],
    check=["Can I find the mode, median, mean and range?", "Can I compare sets of data?"], look=[], note=NOTE)
