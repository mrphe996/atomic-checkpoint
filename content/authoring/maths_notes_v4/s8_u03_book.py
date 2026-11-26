# -*- coding: utf-8 -*-
"""Stage 8 · Unit 3 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u03 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(3, "3.1")]["book"] = BK(
    keys=[("equivalent calculation", "a different calculation with the same answer, e.g. × 0.1 and ÷ 10")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("47 × 0.1", "4.7"), ("47 × 0.01", "0.47"), ("0.8 ÷ 0.1", "8"), ("0.8 ÷ 0.01", "80")),
        Ex("Find the missing number.", ("☐ × 0.1 = 0.35", "3.5"), ("6.2 ÷ ☐ = 620", "0.01")),
        Ex("Sort into 'bigger than 12' and 'smaller than 12': 12 × 0.1, 12 ÷ 0.1, 12 × 0.01, 12 ÷ 0.01", ans="Bigger: 12 ÷ 0.1, 12 ÷ 0.01. Smaller: 12 × 0.1, 12 × 0.01."),
        Ex("Explain to a friend why dividing by 0.01 makes a number 100 times bigger.", ans="There are 100 hundredths in every whole.", think=True),
    ],
    check=["Can I multiply and divide by 0.1 and 0.01?", "Can I predict whether the answer is bigger or smaller?"], look=[], note=NOTE)

N[(3, "3.2")]["book"] = BK(
    keys=[("significant figures (s.f.)", "digits counted from the first non-zero digit"), ("decimal places (d.p.)", "digits after the decimal point"), ("estimate", "an approximate answer using rounded numbers")],
    intro=[], examples=[],
    exercise=[
        Ex("Round to 1 s.f.", ("8472", "8000"), ("0.067", "0.07"), ("349.9", "300")),
        Ex("Round to 2 s.f.", ("63 580", "64 000"), ("0.008 274", "0.0083"), ("9.96", "10")),
        Ex("Round to 3 s.f.", ("2.0461", "2.05"), ("0.30049", "0.300")),
        Ex("Estimate using 1 s.f.", ("38.6 × 5.2", "≈ 200"), ("812 ÷ 19.7", "≈ 40")),
        Ex("Find a news article with large numbers. Which have been rounded, and to how many s.f.?", ans="Your own answer.", think=True),
    ],
    check=["Can I round to decimal places?", "Can I round to significant figures?", "Can I estimate with 1 s.f.?"], look=[], note=NOTE)
