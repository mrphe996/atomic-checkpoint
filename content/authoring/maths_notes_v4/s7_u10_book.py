# -*- coding: utf-8 -*-
"""Stage 7 · Unit 10 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u10 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(10, "10.1")]["book"] = BK(
    keys=[("per cent (%)", "out of 100"), ("equivalent", "equal in value, written differently")],
    intro=[], examples=[],
    exercise=[
        Ex("Copy and complete: fraction, decimal, percentage.", ("3/10", "0.3, 30%"), ("0.64", "16/25, 64%"), ("45%", "9/20, 0.45"), ("5/8", "0.625, 62.5%")),
        Ex("Order, smallest first: 0.31, 3/10, 32%, 5/16", ans="3/10 (30%), 0.31, 5/16 (31.25%), 32%"),
        Ex("A basketball player scores 18 out of 24 shots; another scores 72%. Who is more accurate?", ans="18/24 = 75%, the first player"),
        Ex("Write 2/3 as a percentage to 1 d.p.", ans="66.7%"),
        Ex("Explain how to change any fraction into a percentage.", ans="Divide the numerator by the denominator, then × 100.", think=True),
    ],
    check=["Can I convert between fractions, decimals and percentages?", "Can I compare amounts in different forms?"], look=[], note=NOTE)

N[(10, "10.2")]["book"] = BK(
    keys=[("percentage increase", "the original amount plus a percentage of it"), ("interest", "money paid on savings, often a small percentage")],
    intro=[], examples=[],
    exercise=[
        Ex("Write as a decimal.", ("130%", "1.3"), ("0.4%", "0.004"), ("12.5%", "0.125")),
        Ex("Work out.", ("160% of 45", "72"), ("250% of 18", "45"), ("0.5% of 3200", "16"), ("0.2% of 750", "1.5")),
        Ex("A plant was 40 cm tall. Now it is 185% of that. How tall is it?", ans="74 cm"),
        Ex("A savings account pays 0.75% a year. How much interest on $2400?", ans="$18"),
        Ex("Write 0.25% and 112.5% as fractions in simplest form.", ("0.25%", "1/400"), ("112.5%", "9/8 = 1 1/8")),
        Ex("Find two different ways to work out 115% of 80.", ans="1.15 × 80 = 92; 80 + 8 + 4 = 92.", think=True),
    ],
    check=["Can I use percentages greater than 100%?", "Can I use percentages less than 1%?", "Can I check the size of my answer?"], look=[], note=NOTE)
