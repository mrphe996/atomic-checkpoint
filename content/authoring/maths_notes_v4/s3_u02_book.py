# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u02 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(2, "2.1")]["book"] = BK(
    keys=[("total", "the answer when you add")],
    intro=[], examples=[],
    exercise=[
        Ex("Add.", ("46 + 37", "83"), ("214 + 153", "367"), ("158 + 126", "284"), ("59 + 32", "91")),
        Ex("A farmer has 136 sheep and 47 goats. How many animals?", ans="183"),
    ],
    check=["Can I add 2- and 3-digit numbers?"], look=[], note=NOTE)

N[(2, "2.2")]["book"] = BK(
    keys=[("difference", "the answer when you subtract"), ("inverse", "addition undoes subtraction")],
    intro=[], examples=[],
    exercise=[
        Ex("Subtract, then check by adding.", ("87 − 34", "53"), ("463 − 241", "222"), ("71 − 28", "43"), ("500 − 275", "225")),
    ],
    check=["Can I subtract and check with addition?"], look=[], note=NOTE)

N[(2, "2.3")]["book"] = BK(
    keys=[("cent", "100 cents = $1"), ("change", "money you get back")],
    intro=[], examples=[],
    exercise=[
        Ex("Add.", ("$1.40 + $2.30", "$3.70"), ("$2.60 + $1.80", "$4.40")),
        Ex("Find the change from $5.", ("$3.20", "$1.80"), ("$4.55", "$0.45"), ("$1.99", "$3.01")),
    ],
    check=["Can I add money and find change?"], look=[], note=NOTE)
