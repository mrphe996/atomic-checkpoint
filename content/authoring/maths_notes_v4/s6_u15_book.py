# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u15 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(15, "15.1")]["book"] = BK(
    keys=[("dot plot", "one dot for each piece of data"), ("waffle diagram", "a 10 × 10 grid; each square 1%"), ("pie chart", "a circle split into parts of a whole")],
    intro=[], examples=[],
    exercise=[
        Ex("Favourite fruit of 25 children: apple 10, banana 8, mango 5, grape 2. Draw a bar chart and a waffle diagram.", ans="Waffle: 40, 32, 20, 8 squares"),
        Ex("What fraction of the pie chart is mango?", ans="1/5"),
    ],
    check=["Can I read and draw bar charts, dot plots, waffle diagrams and pie charts?"], look=[], note=NOTE)

N[(15, "15.2")]["book"] = BK(
    keys=[("line graph", "shows change over time"), ("scatter graph", "shows pairs of data")],
    intro=[], examples=[],
    exercise=[
        Ex("Temperatures at 8 am, 10 am, 12 pm, 2 pm, 4 pm: 12, 16, 21, 23, 19 °C. Draw a line graph. When was it warmest?", ans="2 pm"),
        Ex("Measure the height and hand span of 8 people and draw a scatter graph. Is there a link?", ans="Answers vary.", think=True),
    ],
    check=["Can I draw and read line graphs and scatter graphs?"], look=[], note=NOTE)
