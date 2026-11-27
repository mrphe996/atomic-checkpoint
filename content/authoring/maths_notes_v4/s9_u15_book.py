# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u15 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(15, "15.1")]["book"] = BK(
    keys=[("frequency polygon", "frequencies plotted at class midpoints and joined with straight lines")],
    intro=[], examples=[],
    exercise=[
        Ex("Masses (g) of two apple varieties: classes 100–120, 120–140, 140–160, 160–180. Variety P: 3, 8, 10, 4. Variety Q: 7, 11, 5, 2. Draw both frequency polygons on one grid and compare.", ans="P is generally heavier."),
    ],
    check=["Can I draw and compare frequency polygons?"], look=[], note=NOTE)

N[(15, "15.2")]["book"] = BK(
    keys=[("correlation", "a relationship between two variables"), ("line of best fit", "a straight line showing the trend of the points")],
    intro=[], examples=[],
    exercise=[
        Ex("Hours of practice (x) and quiz score (y): (1, 35), (2, 42), (3, 50), (4, 52), (5, 61), (6, 66), (7, 70), (8, 79). Draw a scatter graph and a line of best fit. Describe the correlation and estimate the score for 4.5 hours.", ans="Strong positive; about 57"),
        Ex("Why should you not use the line to predict the score for 20 hours?", ans="It is outside the data range – extrapolation."),
    ],
    check=["Can I draw and interpret scatter graphs?"], look=[], note=NOTE)

N[(15, "15.3")]["book"] = BK(
    keys=[("back-to-back stem-and-leaf diagram", "two data sets sharing one stem column")],
    intro=[], examples=[],
    exercise=[
        Ex("Pulse rates. Before exercise: 62, 68, 71, 73, 74, 77, 80, 85. After: 88, 94, 97, 101, 103, 108, 110, 116. Draw a back-to-back diagram, then compare medians and ranges.", ans="Before: median 73.5, range 23; after: median 102, range 28"),
    ],
    check=["Can I draw and compare back-to-back diagrams?"], look=[], note=NOTE)

N[(15, "15.4")]["book"] = BK(
    keys=[("estimated mean", "Σ(midpoint × frequency) ÷ Σ frequency"), ("modal class", "the class with the highest frequency")],
    intro=[], examples=[],
    exercise=[
        Ex("Times (s): 0–10: 4, 10–20: 9, 20–30: 12, 30–40: 5.", ("estimated mean", "21 s"), ("modal class", "20–30"), ("median class", "20–30")),
    ],
    check=["Can I estimate the mean and find the modal and median classes?"], look=[], note=NOTE)

N[(15, "15.5")]["book"] = BK(
    keys=[("infographic", "a poster-style display of data with charts, icons and key facts")],
    intro=[], examples=[],
    exercise=[
        Ex("Choose a chart and justify it.", ("daily temperatures for a month", "time series graph"), ("heights of 2 classes", "frequency polygons or back-to-back stem-and-leaf"), ("arm span vs height", "scatter graph")),
        Ex("Design an infographic about how your class travels to school.", ans="Answers vary.", think=True),
    ],
    check=["Can I choose, justify and criticise representations?"], look=[], note=NOTE)
