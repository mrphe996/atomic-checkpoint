# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u10 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(10, "10.1")]["book"] = BK(
    keys=[("linear function", "a rule like 2c + 6k = 30 with a constant rate"), ("inverse function", "a rule like xy = 24")],
    intro=[], examples=[],
    exercise=[
        Ex("Notebooks cost $3 and folders $4. Mia spends $36. Write a function and list the whole-number solutions.", ans="3n + 4f = 36: (12, 0), (8, 3), (4, 6), (0, 9)"),
        Ex("xy = 30. Find y when x =", ("5", "6"), ("0.5", "60")),
    ],
    check=["Can I write and use functions of two variables?"], look=[], note=NOTE)

N[(10, "10.2")]["book"] = BK(
    keys=[("table of values", "pairs of x and y used to plot a graph")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw the graph.", ("3x + 2y = 12", "through (0, 6) and (4, 0)"), ("y = x² − 4 for −3 ≤ x ≤ 3", "U-shaped curve through (0, −4)")),
        Ex("Use your graph of y = x² − 4 to estimate where y = 2.", ans="x ≈ ±2.4"),
    ],
    check=["Can I plot straight lines and simple curves?"], look=[], note=NOTE)

N[(10, "10.3")]["book"] = BK(
    keys=[("gradient", "change in y ÷ change in x"), ("y-intercept", "where a line crosses the y-axis")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the gradient and y-intercept.", ("5x + y = 7", "−5, 7"), ("2x + 4y = 12", "−½, 3"), ("x − 2y = 8", "½, −4")),
        Ex("Find the equation of the line through (1, −1) and (4, 8).", ans="y = 3x − 4"),
    ],
    check=["Can I rearrange to y = mx + c?", "Can I find a line from two points?"], look=[], note=NOTE)

N[(10, "10.4")]["book"] = BK(
    keys=[("rate", "how fast one quantity changes compared with another"), ("distance–time graph", "its gradient is the speed")],
    intro=[], examples=[],
    exercise=[
        Ex("A walker goes 6 km in 1.5 h, rests 30 min, then returns home in 2 h. Draw the distance–time graph and find each speed.", ans="4 km/h, 0, 3 km/h"),
        Ex("A plumber's charge graph passes through (0, 40) and (3, 115). Find the hourly rate and the equation.", ans="$25 per hour; C = 25h + 40"),
    ],
    check=["Can I interpret real-life graphs?", "Do I know that the gradient is a rate?"], look=[], note=NOTE)
