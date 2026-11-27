# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u08 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(8, "8.1")]["book"] = BK(
    keys=[("decimal point", "separates whole numbers from tenths, hundredths, thousandths")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("5.68 + 3.457", "9.137"), ("12 − 4.86", "7.14"), ("0.903 − 0.47", "0.433")),
        Ex("You have $20 and buy items for $6.75 and $8.49. How much is left?", ans="$4.76"),
    ],
    check=["Can I add and subtract decimals with up to 3 decimal places?"], look=[], note=NOTE)

N[(8, "8.2")]["book"] = BK(
    keys=[("common denominator", "the same denominator, used to add or subtract fractions")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("⅖ + ⅓", "11/15"), ("⅞ − ¾", "1/8"), ("2⅓ + 1¾", "4 1/12")),
        Ex("A jug has 1½ litres of juice. ⅔ of a litre is poured out. How much is left?", ans="⅚ litre"),
    ],
    check=["Can I add and subtract fractions with different denominators?"], look=[], note=NOTE)
