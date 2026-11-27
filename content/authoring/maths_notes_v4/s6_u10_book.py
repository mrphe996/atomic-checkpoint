# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u10 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(10, "10.1")]["book"] = BK(
    keys=[("estimate", "a rounded calculation to check an answer")],
    intro=[], examples=[],
    exercise=[
        Ex("Estimate, then calculate.", ("3726 × 8", "29 808"), ("417 × 36", "15 012"), ("2085 × 24", "50 040")),
        Ex("A theatre has 38 rows of 125 seats. How many seats?", ans="4750"),
    ],
    check=["Can I multiply large numbers?", "Do I estimate first?"], look=[], note=NOTE)

N[(10, "10.2")]["book"] = BK(
    keys=[("remainder", "what is left over after dividing")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("876 ÷ 6", "146"), ("754 ÷ 13", "58"), ("900 ÷ 16", "56 r 4")),
        Ex("Minibuses hold 16 people. How many for 150 people?", ans="10 minibuses"),
    ],
    check=["Can I divide by 1-digit and 2-digit numbers?", "Can I interpret remainders?"], look=[], note=NOTE)

N[(10, "10.3")]["book"] = BK(
    keys=[("divisible", "divides exactly with no remainder"), ("digit sum", "the total of a number's digits")],
    intro=[], examples=[],
    exercise=[
        Ex("Divisible by 3, 6 and/or 9?", ("612", "3, 6, 9"), ("1005", "3"), ("7290", "3, 6, 9")),
        Ex("Find all digits that make 4_8 divisible by 6.", ans="0, 3, 6, 9"),
    ],
    check=["Can I use tests of divisibility for 3, 6 and 9?"], look=[], note=NOTE)
