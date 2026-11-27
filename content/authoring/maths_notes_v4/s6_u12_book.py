# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u12 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(12, "12.1")]["book"] = BK(
    keys=[("ratio", "a comparison of two or more amounts, e.g. 2 : 3"), ("simplest form", "parts with no common factor except 1")],
    intro=[], examples=[],
    exercise=[
        Ex("Simplify.", ("16 : 24", "2 : 3"), ("35 : 15", "7 : 3"), ("8 : 12 : 20", "2 : 3 : 5")),
        Ex("Squash : water = 1 : 5. How much water for 150 mL squash?", ans="750 mL"),
    ],
    check=["Can I find equivalent ratios and simplify them?"], look=[], note=NOTE)

N[(12, "12.2")]["book"] = BK(
    keys=[("in proportion", "two quantities that change at the same rate")],
    intro=[], examples=[],
    exercise=[
        Ex("Solve.", ("5 kg of potatoes cost $4. Cost of 8 kg?", "$6.40"), ("A recipe for 4 needs 300 mL milk. For 10?", "750 mL")),
        Ex("Is the cost of a phone plan ($10 + $2 per GB) in proportion to the data used? Explain.", ans="No – the fixed $10 means doubling the data doesn't double the cost."),
    ],
    check=["Can I solve direct proportion problems?"], look=[], note=NOTE)
