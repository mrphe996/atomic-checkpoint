# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u12 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(12, "12.1")]["book"] = BK(
    keys=[("ratio", "a comparison of quantities in order"), ("1 : n form", "ratio scaled so the first part is 1")],
    intro=[], examples=[],
    exercise=[
        Ex("Simplify.", ("1.2 kg : 300 g", "4 : 1"), ("2.5 : 7.5", "1 : 3"), ("⅓ : ¼", "4 : 3"), ("36 : 48 : 60", "3 : 4 : 5")),
        Ex("Write in the form 1 : n.", ("4 : 18", "1 : 4.5"), ("5 cm : 2 km", "1 : 40 000")),
        Ex("Which drink is stronger: squash : water 1 : 5 or 2 : 9? Explain.", ans="2 : 9 = 1 : 4.5, so 2 : 9 is stronger."),
    ],
    check=["Can I simplify ratios with units, decimals and fractions?", "Can I compare ratios using 1 : n?"], look=[], note=NOTE)

N[(12, "12.2")]["book"] = BK(
    keys=[("share in a ratio", "divide an amount into parts in a given ratio")],
    intro=[], examples=[],
    exercise=[
        Ex("Share.", ("$450 in 4 : 5", "$200, $250"), ("96 in 1 : 3 : 4", "12, 36, 48")),
        Ex("A : B = 7 : 2 and A gets $60 more than B. Find each share.", ans="A $84, B $24"),
        Ex("Three friends invest $1500, $2500, $1000 and make $600 profit. Share it fairly.", ans="$180, $300, $120"),
    ],
    check=["Can I share amounts, including with three parts?", "Can I use one share or a difference to find the rest?"], look=[], note=NOTE)

N[(12, "12.3")]["book"] = BK(
    keys=[("direct proportion", "quantities in a constant ratio"), ("unit price", "the cost of one unit, used to compare value")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the missing value.", ("5 : 8 = 20 : ?", "32"), ("? : 9 = 14 : 21", "6")),
        Ex("Concrete is cement : sand = 1 : 3. How much cement for 75 kg of sand?", ans="25 kg"),
        Ex("Which is better value: 2.5 kg rice for $4.75 or 4 kg for $7.40?", ans="4 kg ($1.85/kg vs $1.90/kg)"),
        Ex("Find two quantities in your life that are in direct proportion.", ans="For example cost and number of identical items.", think=True),
    ],
    check=["Can I solve proportion problems with ratios?", "Can I find the best buy?"], look=[], note=NOTE)
