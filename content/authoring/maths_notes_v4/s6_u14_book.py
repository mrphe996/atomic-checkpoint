# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u14 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(14, "14.1")]["book"] = BK(
    keys=[("decimal places", "digits after the decimal point")],
    intro=[], examples=[],
    exercise=[
        Ex("Estimate, then calculate.", ("5.38 × 7", "37.66"), ("2.4 × 15", "36"), ("0.65 × 32", "20.8")),
        Ex("A box of juice costs $1.85. Find the cost of 24 boxes.", ans="$44.40"),
    ],
    check=["Can I multiply decimals by whole numbers?"], look=[], note=NOTE)

N[(14, "14.2")]["book"] = BK(
    keys=[("proper fraction", "numerator smaller than the denominator")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("⅗ × 4", "2⅖"), ("⅞ × 2", "1¾"), ("⅘ ÷ 2", "⅖"), ("⅔ ÷ 5", "2/15")),
        Ex("Each lap is ⅜ km. How far is 6 laps?", ans="2¼ km"),
    ],
    check=["Can I multiply and divide fractions by whole numbers?"], look=[], note=NOTE)

N[(14, "14.3")]["book"] = BK(
    keys=[("divide", "share equally or find how many groups")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("8.46 ÷ 3", "2.82"), ("9.1 ÷ 5", "1.82"), ("16.8 ÷ 14", "1.2")),
        Ex("Six friends share a $40.50 bill. How much each?", ans="$6.75"),
    ],
    check=["Can I divide decimals by whole numbers?"], look=[], note=NOTE)
