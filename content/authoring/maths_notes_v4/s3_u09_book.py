# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u09 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(9, "9.1")]["book"] = BK(
    keys=[("exchange", "swap 10 ones for 1 ten, or 10 tens for 1 hundred")],
    intro=[], examples=[],
    exercise=[
        Ex("Estimate, then add.", ("238 + 145", "383"), ("364 + 172", "536"), ("479 + 256", "735")),
    ],
    check=["Can I add 3-digit numbers with exchanging?"], look=[], note=NOTE)

N[(9, "9.2")]["book"] = BK(
    keys=[("inverse", "addition checks subtraction")],
    intro=[], examples=[],
    exercise=[
        Ex("Subtract, then check by adding.", ("452 − 127", "325"), ("634 − 281", "353"), ("500 − 268", "232")),
    ],
    check=["Can I subtract 3-digit numbers with exchanging and check?"], look=[], note=NOTE)

N[(9, "9.3")]["book"] = BK(
    keys=[("complement", "the number that makes a total such as 100 or 1000")],
    intro=[], examples=[],
    exercise=[
        Ex("Complete.", ("60 + ? = 100", "40"), ("90 + ? = 100", "10"), ("200 + ? = 1000", "800"), ("? + 500 = 1000", "500")),
    ],
    check=["Can I find complements to 100 and 1000?"], look=[], note=NOTE)
