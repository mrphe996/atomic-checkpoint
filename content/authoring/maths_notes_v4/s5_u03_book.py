# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u03 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(3, "3.1")]["book"] = BK(
    keys=[("term-to-term rule", "how to get from one term to the next"), ("linear sequence", "the same step every time")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the next two terms.", ("1.4, 1.8, 2.2", "2.6, 3"), ("7, 4.5, 2", "−0.5, −3"), ("⅓, ⅔, 1", "1⅓, 1⅔")),
    ],
    check=["Can I count on and back in any step?"], look=[], note=NOTE)

N[(3, "3.2")]["book"] = BK(
    keys=[("square number", "a number times itself"), ("triangular number", "1 + 2 + 3 + …")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the first 8 square numbers and the first 8 triangular numbers.", ans="1, 4, 9, 16, 25, 36, 49, 64; 1, 3, 6, 10, 15, 21, 28, 36"),
        Ex("Add pairs of neighbouring triangular numbers. What do you notice?", ans="They make square numbers.", think=True),
    ],
    check=["Do I know square and triangular numbers?"], look=[], note=NOTE)

N[(3, "3.3")]["book"] = BK(
    keys=[("prime number", "exactly two factors"), ("composite number", "more than two factors")],
    intro=[], examples=[],
    exercise=[
        Ex("Prime or composite?", ("37", "prime"), ("39", "composite"), ("41", "prime"), ("49", "composite")),
        Ex("Find all the primes between 50 and 70.", ans="53, 59, 61, 67"),
    ],
    check=["Can I identify prime and composite numbers?"], look=[], note=NOTE)
