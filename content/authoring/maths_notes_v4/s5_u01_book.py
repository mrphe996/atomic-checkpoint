# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u01 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(1, "1.1")]["book"] = BK(
    keys=[("tenths", "the first place after the decimal point"), ("hundredths", "the second place after the decimal point")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the value of the 7.", ("4.73", "0.7"), ("15.07", "0.07")),
        Ex("Work out.", ("2.6 × 10", "26"), ("0.35 × 100", "35"), ("84 ÷ 10", "8.4"), ("306 ÷ 100", "3.06")),
    ],
    check=["Do I know tenths and hundredths?", "Can I × and ÷ by 10 and 100?"], look=[], note=NOTE)

N[(1, "1.2")]["book"] = BK(
    keys=[("round", "find the nearest simpler number")],
    intro=[], examples=[],
    exercise=[
        Ex("Round to the nearest whole number.", ("5.3", "5"), ("8.5", "9"), ("12.9", "13"), ("0.4", "0")),
        Ex("Estimate 7.8 + 2.4 + 5.1.", ans="8 + 2 + 5 = 15"),
    ],
    check=["Can I round numbers with 1 decimal place?"], look=[], note=NOTE)
