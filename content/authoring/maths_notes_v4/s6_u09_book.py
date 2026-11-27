# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u09 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(9, "9.1")]["book"] = BK(
    keys=[("probability", "how likely something is, from 0 to 1"), ("mutually exclusive", "outcomes that can't happen together")],
    intro=[], examples=[],
    exercise=[
        Ex("A bag has 5 red, 3 green and 2 white beads. Chance of", ("red", "1/2"), ("green", "3/10"), ("not white", "4/5")),
        Ex("Spin a 4-colour spinner 40 times. Compare your results with what you expected.", ans="About 10 of each colour expected.", think=True),
    ],
    check=["Can I describe chance with fractions and percentages?", "Can I predict outcomes?"], look=[], note=NOTE)
