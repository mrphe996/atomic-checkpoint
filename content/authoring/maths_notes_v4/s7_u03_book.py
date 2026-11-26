# -*- coding: utf-8 -*-
"""Stage 7 · Unit 3 – Words to know, Practice on paper and checklists for the lesson documents (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u03 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(3, "3.1")]["book"] = BK(
    keys=[("power of 10", "10, 100, 1000, … : 10 multiplied by itself"), ("index", "the small raised number in 10³ – how many 10s are multiplied"), ("place value", "the value of a digit from its position")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("6.3 × 10", "63"), ("0.27 × 100", "27"), ("0.5 × 10³", "500"), ("81 ÷ 100", "0.81"), ("4 ÷ 10³", "0.004")),
        Ex("Write as an ordinary number.", ("10²", "100"), ("10⁵", "100 000")),
        Ex("Fill the gaps.", ("3.08 × ☐ = 308", "100"), ("☐ ÷ 10 = 0.65", "6.5"), ("72 ÷ ☐ = 0.072", "1000")),
        Ex("Convert.", ("3.6 km to m", "3600 m"), ("85 cm to m", "0.85 m"), ("0.4 kg to g", "400 g")),
        Ex("A grain of sand is 0.06 cm wide. How long is a line of 10 000 grains, in metres?", ans="600 cm = 6 m"),
        Ex("Pick a decimal. Multiply it by 1000, then divide the answer by 10². What single calculation would give the same result? Explain.", ans="× 10, because × 1000 ÷ 100 = × 10.", think=True),
    ],
    check=["Can I write powers of 10 with an index?", "Can I multiply and divide decimals by 10, 100 and 1000?", "Can I explain why the digits move?"], look=[], note=NOTE)

N[(3, "3.2")]["book"] = BK(
    keys=[("round", "write a number more simply, keeping it close to the original"), ("decimal place (d.p.)", "a digit position after the decimal point"), ("degree of accuracy", "how precise a rounded answer must be")],
    intro=[], examples=[],
    exercise=[
        Ex("Round to the nearest whole number.", ("8.61", "9"), ("23.4", "23"), ("99.5", "100")),
        Ex("Round to 1 decimal place.", ("5.43", "5.4"), ("0.678", "0.7"), ("12.96", "13.0")),
        Ex("Round to 2 decimal places.", ("3.1416", "3.14"), ("0.0751", "0.08"), ("7.995", "8.00")),
        Ex("Work out 17 ÷ 6. Give your answer to 2 d.p.", ans="2.83"),
        Ex("A number with 2 decimal places rounds to 4.6 (1 d.p.). Write the smallest and largest it could be.", ans="4.55 and 4.64"),
        Ex("Explain why 2.40 and 2.4 are equal in value but give different information.", ans="2.40 shows the measurement is accurate to 2 d.p.; 2.4 only to 1 d.p.", think=True),
    ],
    check=["Can I round to the nearest 10, 100 or 1000?", "Can I round to a given number of decimal places?", "Can I avoid rounding in stages?"], look=[], note=NOTE)
