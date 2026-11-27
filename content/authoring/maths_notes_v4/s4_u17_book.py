# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u17 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(17, "17.1")]["book"] = BK(
    keys=[("grid method", "split a number by place value and multiply each part")],
    intro=[], examples=[],
    exercise=[
        Ex("Estimate, then work out.", ("63 × 7", "441"), ("214 × 4", "856"), ("356 × 6", "2136"), ("508 × 3", "1524")),
        Ex("A packet has 135 stickers. How many in 6 packets?", ans="810"),
    ],
    check=["Can I multiply 2- and 3-digit numbers by 1-digit numbers on paper?"], look=[], note=NOTE)

N[(17, "17.2")]["book"] = BK(
    keys=[("chunking", "taking away multiples you know"), ("remainder", "what is left over")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("92 ÷ 4", "23"), ("195 ÷ 5", "39"), ("252 ÷ 7", "36"), ("100 ÷ 6", "16 r 4")),
        Ex("230 people go on a trip. A bus holds 50. How many buses?", ans="5"),
    ],
    check=["Can I divide 2- and 3-digit numbers by 1-digit numbers and use remainders?"], look=[], note=NOTE)
