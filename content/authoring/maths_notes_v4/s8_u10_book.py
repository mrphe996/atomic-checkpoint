# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u10 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(10, "10.1")]["book"] = BK(
    keys=[("percentage change", "change ÷ original × 100%"), ("absolute change", "the actual amount of change")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("increase 240 by 15%", "276"), ("decrease $85 by 20%", "$68")),
        Ex("Find the percentage change.", ("$45 → $54", "20% increase"), ("320 → 272", "15% decrease")),
        Ex("A bus fare rose from $1.60 to $1.80. Find the percentage increase.", ans="12.5%"),
        Ex("Find two prices from shops or websites that have changed. Calculate the percentage change.", ans="Your own answer.", think=True),
    ],
    check=["Can I increase and decrease by a percentage?", "Can I write a change as a percentage of the original?"], look=[], note=NOTE)

N[(10, "10.2")]["book"] = BK(
    keys=[("multiplier", "the decimal you multiply by to make a percentage change")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the multiplier.", ("+ 18%", "1.18"), ("− 18%", "0.82"), ("+ 0.5%", "1.005")),
        Ex("Use a multiplier.", ("increase 640 by 12.5%", "720"), ("decrease $2500 by 7%", "$2325")),
        Ex("$3000 is invested at 4% a year for 3 years. Find the total.", ans="$3374.59"),
        Ex("Explain why a 10% rise followed by a 10% fall leaves you with less than you started.", ans="× 1.1 × 0.9 = × 0.99.", think=True),
    ],
    check=["Can I find and use multipliers?", "Can I combine percentage changes?"], look=[], note=NOTE)
