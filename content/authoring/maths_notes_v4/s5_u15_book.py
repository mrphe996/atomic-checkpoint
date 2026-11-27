# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u15 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(15, "15.1")]["book"] = BK(
    keys=[("improper fraction", "numerator bigger than denominator"), ("mixed number", "a whole number and a fraction")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out. Write improper answers as mixed numbers.", ("3 × 1/4", "3/4"), ("5 × 2/3", "3⅓"), ("4 × 5/8", "2½"), ("6 × 3/4", "4½")),
        Ex("A cake recipe uses ¾ cup of sugar. How much for 6 cakes?", ans="4½ cups"),
    ],
    check=["Can I multiply a fraction by a whole number?"], look=[], note=NOTE)

N[(15, "15.2")]["book"] = BK(
    keys=[("tenth", "one part of 10 equal parts: 0.1")],
    intro=[], examples=[],
    exercise=[
        Ex("Estimate, then work out.", ("2.6 × 4", "10.4"), ("5.3 × 6", "31.8"), ("8.4 ÷ 7", "1.2"), ("4.5 ÷ 9", "0.5")),
        Ex("A box of juice costs $2.40. How much for 5 boxes?", ans="$12"),
    ],
    check=["Can I multiply and divide numbers with one decimal place by a 1-digit number?"], look=[], note=NOTE)
