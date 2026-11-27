# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u07 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(7, "7.1")]["book"] = BK(
    keys=[("equivalent fractions", "fractions with the same value"), ("improper fraction", "numerator bigger than the denominator"), ("mixed number", "a whole number and a fraction")],
    intro=[], examples=[],
    exercise=[
        Ex("Complete.", ("1/3 = ?/12", "4"), ("3/5 = ?/20", "12"), ("10/16 = 5/?", "8")),
        Ex("Write as a mixed number.", ("9/2", "4½"), ("14/3", "4⅔"), ("21/5", "4⅕")),
        Ex("Write as an improper fraction.", ("2⅓", "7/3"), ("3¾", "15/4")),
    ],
    check=["Can I find equivalent fractions?", "Can I change between mixed numbers and improper fractions?"], look=[], note=NOTE)

N[(7, "7.2")]["book"] = BK(
    keys=[("per cent (%)", "out of 100")],
    intro=[], examples=[],
    exercise=[
        Ex("Write as a percentage.", ("0.45", "45%"), ("3/10", "30%"), ("½", "50%"), ("0.08", "8%")),
        Ex("Write as a decimal.", ("70%", "0.7"), ("4%", "0.04"), ("¾", "0.75")),
        Ex("Write as a fraction in its simplest form.", ("20%", "1/5"), ("75%", "3/4")),
    ],
    check=["Can I change between fractions, decimals and percentages?"], look=[], note=NOTE)

N[(7, "7.3")]["book"] = BK(
    keys=[("common denominator", "the same denominator for both fractions")],
    intro=[], examples=[],
    exercise=[
        Ex("Write < or >.", ("⅖ ☐ ½", "<"), ("0.7 ☐ 0.65", ">"), ("¾ ☐ 0.8", "<")),
        Ex("Order from smallest.", ("0.5, 0.45, 0.54", "0.45, 0.5, 0.54"), ("⅔, ½, ⅚", "½, ⅔, ⅚")),
        Ex("Find a decimal between ¼ and ⅓.", ans="Answers vary, e.g. 0.3.", think=True),
    ],
    check=["Can I compare and order fractions and decimals?"], look=[], note=NOTE)
