# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u12 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(12, "12.1")]["book"] = BK(
    keys=[("frequency", "how many times something happens"), ("key", "shows what one symbol stands for")],
    intro=[], examples=[],
    exercise=[
        Ex("Key ● = 4 people. How many people?", ("●●●", "12"), ("●●◐", "10"), ("●●●●●◐", "22")),
        Ex("Favourite sports: football 11, swimming 7, tennis 5, cricket 9. Draw a bar chart. Which is the mode?", ans="football"),
        Ex("Collect the shoe sizes of 10 people and draw a dot plot.", ans="Answers vary.", think=True),
    ],
    check=["Can I draw and read bar charts, pictograms and dot plots?"], look=[], note=NOTE)

N[(12, "12.2")]["book"] = BK(
    keys=[("grouped data", "data sorted into equal, non-overlapping groups"), ("line graph", "points joined to show change over time")],
    intro=[], examples=[],
    exercise=[
        Ex("Times (seconds) to run 50 m: 9, 12, 15, 11, 8, 14, 10, 13, 9, 16. How many in each group?", ("8–9", "3"), ("10–11", "2"), ("12–13", "2"), ("14–16", "3")),
        Ex("Temperatures at 6 am, 9 am, 12 pm, 3 pm, 6 pm: 12°C, 16°C, 21°C, 23°C, 18°C. Draw a line graph. When was it warmest?", ans="3 pm"),
    ],
    check=["Can I group data and read line graphs?"], look=[], note=NOTE)
