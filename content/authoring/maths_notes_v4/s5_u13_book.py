# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u13 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(13, "13.1")]["book"] = BK(
    keys=[("ratio", "compares one part with another part – 'for every'")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the ratio.", ("3 forks for every 2 spoons (forks : spoons)", "3 : 2"), ("6 boys, 5 girls (girls : boys)", "5 : 6")),
        Ex("A drink uses 1 cup of syrup for every 5 cups of water.", ("water for 4 cups of syrup", "20 cups"), ("syrup for 35 cups of water", "7 cups")),
        Ex("Make a necklace pattern with a ratio of 3 : 1. How many of each in 24 beads?", ans="18 and 6"),
    ],
    check=["Can I write and use ratios with 'for every'?"], look=[], note=NOTE)

N[(13, "13.2")]["book"] = BK(
    keys=[("proportion", "compares a part with the whole – 'in every', 'out of'")],
    intro=[], examples=[],
    exercise=[
        Ex("What fraction?", ("3 in every 5", "3/5"), ("1 red for every 3 blue – red", "1/4")),
        Ex("2 in every 9 pupils play chess.", ("in 27 pupils", "6"), ("in 45 pupils", "10")),
        Ex("Count the boys and girls in your class. Write the ratio and the proportion of girls.", ans="Answers vary.", think=True),
    ],
    check=["Can I use proportion with 'in every' and 'out of'?"], look=[], note=NOTE)
