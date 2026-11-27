# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u09 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(9, "9.1")]["book"] = BK(
    keys=[("round", "change a number to a nearby, simpler one"), ("< / >", "less than / greater than")],
    intro=[], examples=[],
    exercise=[
        Ex("Round 5368 to the nearest…", ("10", "5370"), ("100", "5400"), ("1000", "5000")),
        Ex("Write < or >.", ("4082 ☐ 4028", ">"), ("6999 ☐ 7000", "<")),
        Ex("Order from smallest: 3021, 3201, 3012, 3210.", ans="3012, 3021, 3201, 3210"),
    ],
    check=["Can I round, order and compare 4-digit numbers?"], look=[], note=NOTE)

N[(9, "9.2")]["book"] = BK(
    keys=[("remainder", "the amount left over after dividing")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("84 ÷ 4", "21"), ("78 ÷ 6", "13"), ("47 ÷ 5", "9 r 2"), ("59 ÷ 8", "7 r 3")),
        Ex("70 eggs are packed in boxes of 6. How many full boxes? How many eggs left?", ans="11 boxes, 4 left"),
    ],
    check=["Can I divide 2-digit numbers by 1-digit numbers, with remainders?"], look=[], note=NOTE)
