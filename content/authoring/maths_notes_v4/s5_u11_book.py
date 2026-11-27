# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u11 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(11, "11.1")]["book"] = BK(
    keys=[("estimate", "a rough answer from rounded numbers"), ("product", "the answer to a multiplication")],
    intro=[], examples=[],
    exercise=[
        Ex("Estimate, then work out.", ("236 × 4", "944"), ("508 × 6", "3048"), ("27 × 14", "378"), ("46 × 32", "1472")),
        Ex("A school orders 28 packs of 36 pencils. How many pencils?", ans="1008"),
    ],
    check=["Can I estimate and multiply 3-digit × 1-digit and 2-digit × 2-digit numbers?"], look=[], note=NOTE)

N[(11, "11.2")]["book"] = BK(
    keys=[("remainder", "what is left after dividing equally")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("168 ÷ 4", "42"), ("435 ÷ 5", "87"), ("200 ÷ 6", "33 r 2"), ("719 ÷ 8", "89 r 7")),
        Ex("145 people go on a trip. Each van carries 9. How many vans?", ans="17"),
        Ex("145 stickers are put in packs of 9. How many full packs?", ans="16"),
    ],
    check=["Can I divide and decide what to do with a remainder?"], look=[], note=NOTE)

N[(11, "11.3")]["book"] = BK(
    keys=[("divisible", "can be divided with no remainder")],
    intro=[], examples=[],
    exercise=[
        Ex("Is the number divisible by 4?", ("528", "yes"), ("634", "no"), ("1096", "yes")),
        Ex("Is the number divisible by 25?", ("775", "yes"), ("860", "no"), ("1350", "yes")),
        Ex("Write a 4-digit number divisible by 2, 4, 5, 10, 25, 50 and 100.", ans="Any number ending in 00, e.g. 3400.", think=True),
    ],
    check=["Can I use tests of divisibility for 2, 4, 5, 10, 25, 50 and 100?"], look=[], note=NOTE)
