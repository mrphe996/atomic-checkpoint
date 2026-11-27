# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u11 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(11, "11.1")]["book"] = BK(
    keys=[("equivalent fractions", "fractions that are the same amount")],
    intro=[], examples=[],
    exercise=[
        Ex("Complete.", ("1/2 = ?/10", "5"), ("3/4 = ?/8", "6"), ("2/5 = ?/10", "4")),
        Ex("Write < or >.", ("2/9 ☐ 7/9", "<"), ("1/3 ☐ 1/6", ">"), ("1/2 ☐ 3/8", ">")),
        Ex("Order from smallest: 3/4, 1/4, 1/2.", ans="1/4, 1/2, 3/4"),
    ],
    check=["Can I find equivalent fractions and compare and order fractions?"], look=[], note=NOTE)

N[(11, "11.2")]["book"] = BK(
    keys=[("per cent (%)", "out of 100")],
    intro=[], examples=[],
    exercise=[
        Ex("Write as a percentage.", ("1/2", "50%"), ("1/4", "25%"), ("1/10", "10%"), ("37 out of 100", "37%")),
        Ex("Find.", ("50% of 60", "30"), ("25% of 40", "10"), ("10% of 90", "9")),
        Ex("Shade 45% of a 10 × 10 grid. What % is not shaded?", ans="55%"),
    ],
    check=["Can I use percentages and link 50%, 25% and 10% to fractions?"], look=[], note=NOTE)
