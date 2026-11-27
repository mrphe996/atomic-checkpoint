# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u01 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(1, "1.1")]["book"] = BK(
    keys=[("place value", "what a digit is worth because of its place"), ("thousandths", "the third place after the decimal point")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the value of the red digit.", ("3.586 (the 8)", "0.08"), ("12.307 (the 7)", "0.007")),
        Ex("Work out.", ("6.04 × 100", "604"), ("38 ÷ 1000", "0.038"), ("0.9 × 1000", "900")),
        Ex("Decompose 9.452 in two different ways.", ans="9 + 0.4 + 0.05 + 0.002; 9 + 0.45 + 0.002"),
    ],
    check=["Can I say the value of each digit?", "Can I × and ÷ by 10, 100, 1000?"], look=[], note=NOTE)

N[(1, "1.2")]["book"] = BK(
    keys=[("round", "replace a number with a simpler, nearby value")],
    intro=[], examples=[],
    exercise=[
        Ex("Round to the nearest whole number.", ("6.48", "6"), ("13.51", "14"), ("29.5", "30")),
        Ex("Round to the nearest tenth.", ("4.27", "4.3"), ("8.94", "8.9"), ("0.96", "1.0")),
        Ex("Estimate 7.8 + 4.3 − 2.9 by rounding.", ans="8 + 4 − 3 = 9"),
    ],
    check=["Can I round to the nearest whole number and tenth?"], look=[], note=NOTE)
