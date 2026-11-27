# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u06 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(6, "6.1")]["book"] = BK(
    keys=[("numerator", "the top number"), ("denominator", "the bottom number"), ("improper fraction", "numerator bigger than the denominator")],
    intro=[], examples=[],
    exercise=[
        Ex("Write as a fraction or mixed number.", ("4 ÷ 7", "4/7"), ("17 ÷ 5", "3⅖")),
        Ex("Work out.", ("⅝ of 48", "30"), ("9/4 of 16", "36")),
    ],
    check=["Can I see fractions as divisions?", "Can I find fractions of amounts?"], look=[], note=NOTE)

N[(6, "6.2")]["book"] = BK(
    keys=[("percentage", "a number out of 100")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("30% of 70", "21"), ("15% of 120", "18"), ("75% of 64", "48")),
        Ex("A $45 shirt is 20% off. What is the sale price?", ans="$36"),
    ],
    check=["Can I find percentages of amounts and shapes?"], look=[], note=NOTE)

N[(6, "6.3")]["book"] = BK(
    keys=[("equivalent", "equal in value"), ("simplest form", "a fraction that can't be simplified further")],
    intro=[], examples=[],
    exercise=[
        Ex("Simplify.", ("14/21", "2/3"), ("30/45", "2/3")),
        Ex("Order from smallest: 0.45, 2/5, 42%, 9/20.", ans="2/5, 42%, 0.45 = 9/20"),
    ],
    check=["Can I simplify fractions?", "Can I compare fractions, decimals and percentages?"], look=[], note=NOTE)
