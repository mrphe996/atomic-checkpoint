# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u16 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(16, "16.1")]["book"] = BK(
    keys=[("key", "what one symbol stands for"), ("scale", "the numbers up the side of a bar chart")],
    intro=[], examples=[],
    exercise=[
        Ex("Key ● = 10. How many?", ("●●●", "30"), ("●●●●●", "50"), ("●● and half a ●", "25")),
        Ex("Draw a bar chart with a scale in 5s: apples 15, pears 10, plums 25, figs 5.", ans="Check bars reach 15, 10, 25, 5."),
    ],
    check=["Can I draw and read pictograms and bar charts with scales?"], look=[], note=NOTE)

N[(16, "16.2")]["book"] = BK(
    keys=[("dot plot", "one dot above a number line for each value"), ("mode", "the most common value")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the mode.", ("3, 4, 4, 6, 4", "4"), ("9, 7, 7, 9, 9", "9"), ("cat, dog, cat", "cat")),
        Ex("Ask 12 people how many pets they have. Draw a dot plot and find the mode.", ans="Answers vary.", think=True),
    ],
    check=["Can I draw a dot plot and use the mode?"], look=[], note=NOTE)
