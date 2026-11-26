# -*- coding: utf-8 -*-
"""Stage 8 · Unit 4 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u04 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(4, "4.1")]["book"] = BK(
    keys=[("negative decimal", "a decimal less than zero, e.g. −2.45"), ("≠", "is not equal to")],
    intro=[], examples=[],
    exercise=[
        Ex("Write <, > or =.", ("−4.6 ☐ −4.06", "<"), ("−0.30 ☐ −0.3", "="), ("−1.99 ☐ −2", ">")),
        Ex("Order, smallest first: −3.05, −3.5, 3.05, −3.505, 0", ans="−3.505, −3.5, −3.05, 0, 3.05"),
        Ex("Write three numbers between −0.2 and −0.21.", ans="For example −0.201, −0.205, −0.209."),
        Ex("Explain how a number line helps to order negative decimals.", ans="Numbers further left are smaller.", think=True),
    ],
    check=["Can I order decimals including negatives?", "Can I use =, ≠, <, >?"], look=[], note=NOTE)

N[(4, "4.2")]["book"] = BK(
    keys=[("decimal places", "digits after the point; count them in both numbers")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("0.7 × 0.8", "0.56"), ("2.6 × 1.4", "3.64"), ("0.03 × 0.09", "0.0027"), ("15.2 × 0.25", "3.8")),
        Ex("Use 63 × 47 = 2961 to find", ("6.3 × 4.7", "29.61"), ("0.63 × 0.047", "0.029 61")),
        Ex("Paint costs $9.45 per litre. How much for 2.6 litres?", ans="$24.57"),
        Ex("Find two decimals with 1 d.p. whose product is 0.12.", ans="For example 0.3 × 0.4, 0.2 × 0.6.", think=True),
    ],
    check=["Can I multiply decimals by decimals?", "Can I place the decimal point by counting decimal places?"], look=[], note=NOTE)

N[(4, "4.3")]["book"] = BK(
    keys=[("equivalent calculation", "multiply both numbers by the same power of 10")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("7.2 ÷ 0.9", "8"), ("0.56 ÷ 0.07", "8"), ("3.15 ÷ 0.5", "6.3"), ("12 ÷ 0.04", "300")),
        Ex("A 2.88 m shelf is cut into pieces of 0.36 m. How many pieces?", ans="8"),
        Ex("0.35 kg of tea costs $5.25. Find the price per kg.", ans="$15"),
        Ex("Explain why 4 ÷ 0.8 is bigger than 4.", ans="There are 5 lots of 0.8 in 4 – dividing by less than 1 gives more.", think=True),
    ],
    check=["Can I divide by a decimal using an equivalent calculation?", "Can I predict the size of the answer?"], look=[], note=NOTE)

N[(4, "4.4")]["book"] = BK(
    keys=[("compensation", "round, calculate, then adjust"), ("distributive law", "a × b + a × c = a × (b + c)")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out mentally.", ("40 × 2.99", "119.6"), ("0.25 × 8.4", "2.1"), ("6.8 × 25", "170"), ("1.9 × 7 + 1.9 × 3", "19")),
        Ex("Work out.", ("5.5 ÷ 0.25", "22"), ("0.125 × 6.4 × 8", "6.4")),
        Ex("Show two different easy methods for 4.8 × 15.", ans="4.8 × 10 + 4.8 × 5 = 72; 4.8 × 30 ÷ 2 = 72.", think=True),
    ],
    check=["Can I choose an easier method for a decimal calculation?", "Can I explain my method?"], look=[], note=NOTE)
