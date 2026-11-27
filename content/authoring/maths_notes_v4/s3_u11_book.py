# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u11 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(11, "11.1")]["book"] = BK(
    keys=[("fraction of a number", "divide by the bottom, multiply by the top")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("1/2 of 24", "12"), ("1/4 of 16", "4"), ("2/3 of 12", "8"), ("3/5 of 25", "15")),
    ],
    check=["Can I find unit and non-unit fractions of numbers?"], look=[], note=NOTE)

N[(11, "11.2")]["book"] = BK(
    keys=[("unit fraction", "a fraction with 1 on top")],
    intro=[], examples=[],
    exercise=[
        Ex("Write < or >.", ("1/2 ☐ 1/4", ">"), ("1/10 ☐ 1/5", "<"), ("3/8 ☐ 6/8", "<")),
        Ex("Order from smallest: 1/3, 1/2, 1/6.", ans="1/6, 1/3, 1/2"),
    ],
    check=["Can I compare and order fractions?"], look=[], note=NOTE)

N[(11, "11.3")]["book"] = BK(
    keys=[("denominator", "the bottom number")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("2/7 + 4/7", "6/7"), ("1/5 + 1/5", "2/5"), ("7/8 − 3/8", "4/8"), ("1 − 2/3", "1/3")),
    ],
    check=["Can I add and subtract fractions with the same denominator?"], look=[], note=NOTE)
