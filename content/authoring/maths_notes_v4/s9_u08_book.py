# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u08 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(8, "8.1")]["book"] = BK(
    keys=[("terminating decimal", "a decimal that ends"), ("recurring decimal", "a decimal with digits that repeat for ever")],
    intro=[], examples=[],
    exercise=[
        Ex("Terminating or recurring?", ("13/40", "terminating"), ("4/21", "recurring"), ("18/45", "terminating (2/5)")),
        Ex("Write as a fraction in its simplest form.", ("0.6̇", "2/3"), ("0.2̇7̇", "3/11"), ("0.36̇", "11/30")),
    ],
    check=["Can I predict terminating decimals?", "Can I convert recurring decimals to fractions?"], look=[], note=NOTE)

N[(8, "8.2")]["book"] = BK(
    keys=[("order of operations", "brackets, indices, × ÷, + −")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("2/3 + 1/3 × 3/5", "13/15"), ("(1½ + 2¼) ÷ 3", "1¼"), ("4 − (3/4)² × 8/3", "2½")),
        Ex("Estimate, then calculate 3⅞ × 2⅕ − 1½.", ans="Estimate ≈ 7; exact 281/40 = 7 1/40"),
    ],
    check=["Can I use the order of operations with fractions?"], look=[], note=NOTE)

N[(8, "8.3")]["book"] = BK(
    keys=[("cancel", "divide a numerator and a denominator by a common factor")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out, cancelling first.", ("14/15 × 25/28", "5/6"), ("24 × 7/16", "10½"), ("2⅖ × 3¾", "9")),
        Ex("Find 5/9 of 4½ kg.", ans="2½ kg"),
    ],
    check=["Can I cancel before multiplying?"], look=[], note=NOTE)

N[(8, "8.4")]["book"] = BK(
    keys=[("reciprocal", "a fraction turned upside down; n and 1/n")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("5/8 ÷ 15/16", "2/3"), ("12 ÷ 3/5", "20"), ("4⅖ ÷ 1⅗", "2¾")),
        Ex("How many 3/4-hour lessons fit into 6 hours?", ans="8"),
    ],
    check=["Can I divide fractions and mixed numbers?"], look=[], note=NOTE)

N[(8, "8.5")]["book"] = BK(
    keys=[("strategy", "a method chosen to make a calculation easier")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out mentally, showing your strategy.", ("0.25 × 7.2 × 40", "72"), ("6.8 × 13 − 6.8 × 3", "68"), ("0.125 × 56", "7"), ("5.98 × 5", "29.9")),
        Ex("Invent a calculation that becomes easy with the distributive law.", ans="Answers vary.", think=True),
    ],
    check=["Can I choose a strategy to make a calculation easier?"], look=[], note=NOTE)
