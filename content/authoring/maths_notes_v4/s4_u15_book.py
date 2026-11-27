# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u15 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(15, "15.1")]["book"] = BK(
    keys=[("<", "is less than"), (">", "is greater than")],
    intro=[], examples=[],
    exercise=[
        Ex("Write <, > or =.", ("−4 ☐ −1", "<"), ("3060 ☐ 3006", ">"), ("200 + 5 ☐ 205", "=")),
        Ex("Order from smallest: 4, −7, 0, −2, 9.", ans="−7, −2, 0, 4, 9"),
    ],
    check=["Can I order and compare numbers, including negative numbers?"], look=[], note=NOTE)

N[(15, "15.2")]["book"] = BK(
    keys=[("square number", "a number multiplied by itself"), ("common multiple", "a multiple of two numbers")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("7 × 7", "49"), ("8 × 8", "64"), ("10 × 10", "100")),
        Ex("Find the first common multiple.", ("4 and 5", "20"), ("6 and 9", "18")),
        Ex("Draw the first five square numbers as dot patterns.", ans="1, 4, 9, 16, 25", think=True),
    ],
    check=["Can I recognise square numbers and use multiples?"], look=[], note=NOTE)

N[(15, "15.3")]["book"] = BK(
    keys=[("divisible", "can be divided exactly, with no remainder")],
    intro=[], examples=[],
    exercise=[
        Ex("Divisible by 25?", ("625", "yes"), ("640", "no"), ("1075", "yes")),
        Ex("Divisible by 2, 5 and 10?", ("380", "yes"), ("385", "no")),
    ],
    check=["Can I use tests of divisibility for 2, 5, 10, 25, 50 and 100?"], look=[], note=NOTE)
