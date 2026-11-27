# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u04 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(4, "4.1")]["book"] = BK(
    keys=[("integer", "a whole number: positive, negative or zero"), ("difference", "how far apart two numbers are")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("−7 + 3", "−4"), ("4 − 10", "−6"), ("−2 − 5", "−7")),
        Ex("Find the difference between", ("−8 and 5", "13"), ("−15 and −6", "9")),
        Ex("Estimate, then calculate 37 284 − 18 596.", ans="≈ 19 000; 18 688"),
    ],
    check=["Can I add and subtract with negative numbers?"], look=[], note=NOTE)

N[(4, "4.2")]["book"] = BK(
    keys=[("unknown", "a number we don't know yet, shown by a letter")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the value of the letter.", ("a + 15 = 41", "26"), ("7b = 63", "9"), ("c ÷ 6 = 8", "48"), ("3d + 4 = 25", "7")),
        Ex("Make up your own two-step puzzle with a letter and swap with a friend.", ans="Answers vary.", think=True),
    ],
    check=["Can I find the value of a letter?"], look=[], note=NOTE)
