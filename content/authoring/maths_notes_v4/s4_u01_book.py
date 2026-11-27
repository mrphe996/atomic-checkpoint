# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u01 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(1, "1.1")]["book"] = BK(
    keys=[("sequence", "numbers in a pattern"), ("term", "one number in a sequence"), ("step", "the amount added or taken away each time")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the next two terms.", ("6, 11, 16, 21", "26, 31"), ("90, 81, 72", "63, 54"), ("7, 4, 1", "−2, −5")),
        Ex("Describe the rule for 3, 10, 17, 24.", ans="Start at 3, add 7."),
        Ex("Make your own sequence that goes below zero. Write its rule.", ans="Answers vary.", think=True),
    ],
    check=["Can I continue and describe sequences?"], look=[], note=NOTE)

N[(1, "1.2")]["book"] = BK(
    keys=[("negative number", "a number less than zero")],
    intro=[], examples=[],
    exercise=[
        Ex("Write < or >.", ("−3 ☐ 2", "<"), ("−1 ☐ −6", ">"), ("0 ☐ −4", ">")),
        Ex("Order from coldest: 6 °C, −9 °C, 0 °C, −1 °C.", ans="−9, −1, 0, 6"),
        Ex("The temperature is −5 °C. It rises 8 degrees. What is it now?", ans="3 °C"),
    ],
    check=["Can I read, order and use negative numbers in context?"], look=[], note=NOTE)

N[(1, "1.3")]["book"] = BK(
    keys=[("place value", "what a digit is worth because of its place"), ("placeholder", "a zero that keeps digits in the right places")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the value of the 6 in…", ("6213", "6000"), ("4627", "600"), ("1960", "60")),
        Ex("Work out.", ("73 × 10", "730"), ("19 × 100", "1900"), ("580 ÷ 10", "58"), ("4200 ÷ 100", "42")),
    ],
    check=["Can I use place value in 4-digit numbers and multiply and divide by 10 and 100?"], look=[], note=NOTE)
