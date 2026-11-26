# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u16 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(16, "16.1")]["book"] = BK(
    keys=[("class interval", "the width of a group"), ("continuous data", "measured data that can take any value"), ("frequency diagram", "bars with no gaps for grouped continuous data")],
    intro=[], examples=[],
    exercise=[
        Ex("Masses (kg) of 16 parcels: 2.4, 5.1, 3.8, 1.2, 4.6, 2.9, 3.3, 0.8, 4.1, 2.2, 3.7, 1.9, 2.6, 3.0, 4.9, 1.5. Make a grouped table with classes 0 ≤ m < 1, 1 ≤ m < 2 … and draw a frequency diagram.", ans="1, 3, 4, 4, 3, 1"),
        Ex("Write the modal class and the number of parcels of at least 3 kg.", ans="2 ≤ m < 3 and 3 ≤ m < 4 (both 4); 8"),
    ],
    check=["Can I group continuous data?", "Can I draw and read frequency diagrams?"], look=[], note=NOTE)

N[(16, "16.2")]["book"] = BK(
    keys=[("time series graph", "points at regular times joined by straight lines"), ("trend", "the general direction of change")],
    intro=[], examples=[],
    exercise=[
        Ex("Monthly visitors (thousands) Jan–Jun: 12, 14, 19, 25, 31, 36. Draw a time series graph and describe the trend.", ans="Increasing steadily"),
        Ex("Estimate the visitors halfway through April–May and predict July.", ans="about 28 thousand; about 41–42 thousand"),
    ],
    check=["Can I draw time series graphs?", "Can I describe trends and estimate?"], look=[], note=NOTE)

N[(16, "16.3")]["book"] = BK(
    keys=[("stem", "the leading digit(s)"), ("leaf", "the last digit"), ("key", "explains how to read the values")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw an ordered stem-and-leaf diagram: 43, 57, 38, 49, 51, 36, 44, 60, 47, 52, 39, 55.", ans="3 | 6 8 9; 4 | 3 4 7 9; 5 | 1 2 5 7; 6 | 0"),
        Ex("Find the median, range and mean of that data.", ans="median 48, range 24, mean ≈ 47.6"),
    ],
    check=["Can I draw stem-and-leaf diagrams with a key?", "Can I find statistics from them?"], look=[], note=NOTE)

N[(16, "16.4")]["book"] = BK(
    keys=[("proportion", "a fraction of the whole"), ("sector", "a slice of a pie chart")],
    intro=[], examples=[],
    exercise=[
        Ex("Town A (90 people): 'park' sector 120°. Town B (240 people): 'park' sector 75°. Which town has", ("the greater proportion choosing park?", "A"), ("the greater number?", "B (50 vs 30)")),
        Ex("A sector of 135° represents 21 people. Find the total.", ans="56"),
    ],
    check=["Can I compare pie charts by proportion and by number?"], look=[], note=NOTE)

N[(16, "16.5")]["book"] = BK(
    keys=[("justify", "give a reason for a choice")],
    intro=[], examples=[],
    exercise=[
        Ex("Choose and justify a chart.", ("weekly sales over a year", "time series graph"), ("hand span vs height", "scatter graph"), ("share of energy sources", "pie chart")),
        Ex("Collect your own small data set and represent it two ways. Which is clearer?", ans="Answers vary.", think=True),
    ],
    check=["Can I choose a suitable chart and justify it?"], look=[], note=NOTE)

N[(16, "16.6")]["book"] = BK(
    keys=[("mean, median, mode", "averages"), ("range", "a measure of spread")],
    intro=[], examples=[],
    exercise=[
        Ex("Long jumps (m). Kay: 4.2, 4.5, 4.3, 4.4, 4.6. Lee: 3.9, 5.1, 4.0, 4.8, 4.7. Compare using the mean and range.", ans="Kay mean 4.4, range 0.4; Lee mean 4.5, range 1.2 – Lee further on average, Kay more consistent"),
        Ex("Which average should be used for incomes in a small town with one billionaire? Why?", ans="Median – not affected by the outlier"),
    ],
    check=["Can I compare data sets using an average and the range?", "Can I choose the best average?"], look=[], note=NOTE)
