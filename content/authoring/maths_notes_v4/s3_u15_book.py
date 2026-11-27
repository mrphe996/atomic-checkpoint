# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u15 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(15, "15.1")]["book"] = BK(
    keys=[("key", "what one picture stands for"), ("scale", "the numbers on a bar chart")],
    intro=[], examples=[],
    exercise=[
        Ex("Key ⭐ = 5. How many?", ("⭐⭐", "10"), ("⭐⭐⭐⭐", "20"), ("⭐⭐⭐", "15")),
        Ex("Draw a bar chart: red 6, blue 10, green 4, yellow 8 (scale in 2s).", ans="Check the bars."),
    ],
    check=["Can I draw and read pictograms and bar charts?"], look=[], note=NOTE)

N[(15, "15.2")]["book"] = BK(
    keys=[("Venn diagram", "circles for sorting; overlap = both"), ("Carroll diagram", "a grid for sorting with 'not'")],
    intro=[], examples=[],
    exercise=[
        Ex("Venn (even / more than 10): where does it go?", ("16", "overlap"), ("8", "even only"), ("11", "more than 10 only"), ("3", "outside")),
    ],
    check=["Can I sort with Venn and Carroll diagrams?"], look=[], note=NOTE)
