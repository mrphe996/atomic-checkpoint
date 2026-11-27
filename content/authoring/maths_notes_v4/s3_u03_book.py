# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u03 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(3, "3.1")]["book"] = BK(
    keys=[("array", "objects in equal rows and columns"), ("share", "split equally")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("3 groups of 5", "15"), ("4 × 2", "8"), ("20 ÷ 4", "5"), ("14 shared between 2", "7")),
        Ex("Draw an array for 3 × 6 and write its fact family.", ans="3 × 6 = 18, 6 × 3 = 18, 18 ÷ 3 = 6, 18 ÷ 6 = 3"),
    ],
    check=["Can I multiply with groups and arrays and divide by sharing and grouping?"], look=[], note=NOTE)

N[(3, "3.2")]["book"] = BK(
    keys=[("double", "multiply by 2"), ("halve", "divide by 2")],
    intro=[], examples=[],
    exercise=[
        Ex("Complete.", ("4 × 4", "16"), ("4 × 8", "32"), ("7 × 8", "56"), ("48 ÷ 8", "6")),
        Ex("Write the 8 times table up to 10 × 8 by doubling the 4 times table.", ans="8, 16, 24, 32, 40, 48, 56, 64, 72, 80"),
    ],
    check=["Can I use doubling to link the 2, 4 and 8 times tables?"], look=[], note=NOTE)

N[(3, "3.3")]["book"] = BK(
    keys=[("multiple", "a number in a times table")],
    intro=[], examples=[],
    exercise=[
        Ex("Complete.", ("8 × 3", "24"), ("8 × 6", "48"), ("8 × 9", "72"), ("63 ÷ 9", "7")),
        Ex("Check the 9 times table digit pattern for 9 × 1 to 9 × 10.", ans="The digits of each answer add to 9.", think=True),
    ],
    check=["Can I link the 3, 6 and 9 times tables?"], look=[], note=NOTE)
