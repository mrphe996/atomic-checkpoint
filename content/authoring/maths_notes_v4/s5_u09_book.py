# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u09 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(9, "9.1")]["book"] = BK(
    keys=[("denominator", "the bottom number – how many equal parts in a whole"), ("numerator", "the top number – how many parts")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out. Simplify your answer.", ("2/9 + 4/9", "2/3"), ("1/4 + 3/8", "5/8"), ("1/2 + 3/10", "4/5"), ("5/6 + 2/3", "1½")),
        Ex("A recipe uses ½ cup of milk and ¼ cup of water. How much liquid?", ans="¾ cup"),
    ],
    check=["Can I add fractions when one denominator is a multiple of the other?"], look=[], note=NOTE)

N[(9, "9.2")]["book"] = BK(
    keys=[("simplest form", "numerator and denominator cannot be divided by the same number")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out. Simplify your answer.", ("7/8 − 3/8", "1/2"), ("3/4 − 1/8", "5/8"), ("1 − 2/7", "5/7"), ("9/10 − 1/5", "7/10")),
        Ex("A runner has finished 5/8 of a race. What fraction is left?", ans="3/8"),
    ],
    check=["Can I subtract fractions, including from 1?"], look=[], note=NOTE)
