# -*- coding: utf-8 -*-
"""Stage 7 · Unit 11 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u11 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(11, "11.1")]["book"] = BK(
    keys=[("function", "a rule that turns each input into one output"), ("input, output", "the number in, the number out"), ("equation", "the rule written with an = sign, e.g. y = 3x + 2")],
    intro=[], examples=[],
    exercise=[
        Ex("For y = 2x + 7, find y when", ("x = 0", "7"), ("x = 5", "17"), ("x = −3", "1")),
        Ex("For y = 4x − 6, find x when", ("y = 10", "4"), ("y = −2", "1")),
        Ex("Find the equation for each table.", ("x: 1, 2, 3; y: 6, 9, 12", "y = 3x + 3"), ("x: 0, 1, 2; y: 10, 8, 6", "y = 10 − 2x")),
        Ex("A plumber charges $40 call-out and $25 per hour. Write the cost y for x hours. Find the cost of 3 hours.", ans="y = 25x + 40; $115"),
        Ex("Make up a function and a table of 4 pairs for a partner to solve.", ans="Any correct rule and table.", think=True),
    ],
    check=["Can I use a function rule written in words or as an equation?", "Can I find an input from an output?", "Can I find the rule from a table?"], look=[], note=NOTE)

N[(11, "11.2")]["book"] = BK(
    keys=[("table of values", "pairs of x and y values from a rule"), ("linear", "giving a straight-line graph"), ("coordinates", "(x, y): across, then up")],
    intro=[], examples=[],
    exercise=[
        Ex("Complete a table for x = −1, 0, 1, 2, 3 and draw the graph.", ("y = x + 2", "1, 2, 3, 4, 5"), ("y = 2x − 3", "−5, −3, −1, 1, 3"), ("y = 4 − x", "5, 4, 3, 2, 1")),
        Ex("Which of these points are on y = 3x − 1? (0, −1), (2, 6), (3, 8), (−1, −4)", ans="(0, −1), (3, 8), (−1, −4)"),
        Ex("Where does y = 5x + 2 cross the y-axis?", ans="(0, 2)"),
        Ex("Draw y = x and y = 2x on the same grid. What is the same and what is different?", ans="Both pass through (0, 0); y = 2x is steeper.", think=True),
    ],
    check=["Can I make a table of values?", "Can I plot and draw a straight-line graph?", "Can I check if a point is on a line?"], look=[], note=NOTE)

N[(11, "11.3")]["book"] = BK(
    keys=[("vertical", "straight up and down"), ("horizontal", "straight across"), ("parallel", "always the same distance apart")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the equation of the line through", ("(4, 1) and (4, −3)", "x = 4"), ("(−2, 6) and (5, 6)", "y = 6")),
        Ex("On one grid draw x = −2, x = 3, y = −1 and y = 2. Find the area of the rectangle.", ans="5 × 3 = 15 square units"),
        Ex("Where do these lines cross?", ("x = 5 and y = −4", "(5, −4)"), ("y = 0 and x = −3", "(−3, 0)")),
        Ex("Explain why x = 3 is vertical even though it has an x in it.", ans="Every point has x-coordinate 3, so the points are straight above and below each other.", think=True),
    ],
    check=["Can I recognise x = a as vertical and y = b as horizontal?", "Can I draw these lines?", "Can I find where they cross?"], look=[], note=NOTE)

N[(11, "11.4")]["book"] = BK(
    keys=[("conversion graph", "a graph to change one unit into another"), ("distance–time graph", "shows how far from a place over time")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw a conversion graph for km and miles (8 km = 5 miles) from 0 to 80 km. Use it to convert", ("40 km", "25 miles"), ("30 miles", "48 km"), ("200 km", "125 miles")),
        Ex("A delivery van drives 30 km in 30 minutes, stops 15 minutes, then drives 30 km back in 45 minutes. Draw the distance–time graph. When was it fastest?", ans="On the way out (60 km/h)."),
        Ex("A phone company charges $5 per month plus $2 per GB. Draw a graph from 0 to 10 GB. Why doesn't it start at (0, 0)?", ans="There is a fixed $5 charge."),
        Ex("Write a short story to match a graph that goes up steeply, is flat, then goes down slowly.", ans="Any matching story.", think=True),
    ],
    check=["Can I read a conversion graph both ways?", "Can I interpret a distance–time graph?", "Can I use the scale correctly?"], look=[], note=NOTE)
