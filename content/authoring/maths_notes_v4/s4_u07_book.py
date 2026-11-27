# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u07 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(7, "7.1")]["book"] = BK(
    keys=[("numerator", "the top number – parts we have"), ("denominator", "the bottom number – equal parts in the whole")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the fraction shaded.", ("6 equal parts, 1 shaded", "1/6"), ("5 equal parts, 4 shaded", "4/5"), ("10 equal parts, 3 shaded", "3/10")),
        Ex("Write as a fraction.", ("2 ÷ 3", "2/3"), ("5 ÷ 8", "5/8")),
        Ex("Fold a paper strip into 8 equal parts and colour 3/8.", ans="Answers vary.", think=True),
    ],
    check=["Can I understand fractions as parts of a whole and as division?"], look=[], note=NOTE)

N[(7, "7.2")]["book"] = BK(
    keys=[("unit fraction", "a fraction with numerator 1")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("⅓ of 18", "6"), ("¼ of 44", "11"), ("⅔ of 24", "16"), ("¾ of 36", "27")),
        Ex("A bag has 40 sweets. ⅝ are red. How many are red?", ans="25"),
    ],
    check=["Can I find a fraction of an amount?"], look=[], note=NOTE)
