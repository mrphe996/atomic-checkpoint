# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u17 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(17, "17.1")]["book"] = BK(
    keys=[("order of operations", "brackets, then × and ÷, then + and −")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("3 + 4 × 6", "27"), ("(3 + 4) × 6", "42"), ("40 − 15 ÷ 5", "37"), ("8 × (10 − 7) + 2", "26")),
        Ex("Put brackets in to make it true: 12 − 4 × 2 = 16.", ans="(12 − 4) × 2 = 16"),
    ],
    check=["Can I use the order of operations, including brackets?"], look=[], note=NOTE)

N[(17, "17.2")]["book"] = BK(
    keys=[("commutative", "order can be swapped"), ("associative", "grouping can change"), ("distributive", "split a number and multiply each part")],
    intro=[], examples=[],
    exercise=[
        Ex("Calculate mentally.", ("2 × 47 × 50", "4700"), ("38 + 26 + 62", "126"), ("8 × 23", "184"), ("4 × 49", "196")),
        Ex("Explain a quick way to work out 125 × 16.", ans="125 × 8 × 2 = 1000 × 2 = 2000", think=True),
    ],
    check=["Can I use the laws of arithmetic to calculate mentally?"], look=[], note=NOTE)
