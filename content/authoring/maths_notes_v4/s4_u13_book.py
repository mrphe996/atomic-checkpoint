# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u13 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(13, "13.1")]["book"] = BK(
    keys=[("round and adjust", "use a nearby easy number, then correct"), ("count on", "find a difference by counting up")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out mentally.", ("199 + 64", "263"), ("520 − 98", "422"), ("706 − 699", "7"), ("33 + 48 + 67", "148")),
        Ex("Work out with columns.", ("476 + 357", "833"), ("832 − 569", "263")),
    ],
    check=["Can I choose efficient mental and written strategies?"], look=[], note=NOTE)

N[(13, "13.2")]["book"] = BK(
    keys=[("denominator", "the number of equal parts in the whole")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("2/9 + 5/9", "7/9"), ("1/6 + 4/6", "5/6"), ("7/10 − 3/10", "4/10"), ("1 − 2/5", "3/5")),
        Ex("A jug is 3/8 full. Anna adds 4/8 more. How full is it now?", ans="7/8"),
    ],
    check=["Can I add and subtract fractions with the same denominator?"], look=[], note=NOTE)
