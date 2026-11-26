# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u11 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(11, "11.1")]["book"] = BK(
    keys=[("function", "each input has exactly one output")],
    intro=[], examples=[],
    exercise=[
        Ex("A bike hire costs $6 plus $4 per hour.", ("write C in terms of h", "C = 4h + 6"), ("find C for 5 h", "$26"), ("find h when C = $38", "8 h")),
        Ex("Find the function: x 0, 1, 2, 3; y 7, 5, 3, 1.", ans="y = 7 − 2x"),
        Ex("Describe a real situation for y = 3x + 10.", ans="For example a $10 fee plus $3 per item.", think=True),
    ],
    check=["Can I write and use functions in context?", "Can I find inputs from outputs?"], look=[], note=NOTE)

N[(11, "11.2")]["book"] = BK(
    keys=[("table of values", "x and y pairs from an equation"), ("intersection", "where two lines cross")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw for x = −2 to 3.", ("y = 2x − 3", "line through (0, −3)"), ("y = 4 − x", "line through (0, 4)"), ("x + y = 2", "line through (0, 2) and (2, 0)")),
        Ex("Where do y = 2x − 3 and y = 4 − x cross?", ans="(7/3, 5/3) ≈ (2.3, 1.7)"),
        Ex("Draw x = 3, y = −1 and y = x. What shape do they enclose?", ans="A right-angled isosceles triangle with corners (−1, −1), (3, −1), (3, 3)."),
    ],
    check=["Can I plot straight-line graphs?", "Can I find where two lines cross?"], look=[], note=NOTE)

N[(11, "11.3")]["book"] = BK(
    keys=[("gradient", "steepness: rise ÷ run"), ("y-intercept", "where the line crosses the y-axis")],
    intro=[], examples=[],
    exercise=[
        Ex("State m and c.", ("y = 6x − 1", "6, −1"), ("y = 3 − 2x", "−2, 3"), ("2y = 4x + 10", "2, 5")),
        Ex("Find the equation of the line through", ("(0, 1) and (2, 9)", "y = 4x + 1"), ("(0, 4) and (4, 0)", "y = 4 − x")),
        Ex("Write two lines parallel to y = 3x + 2.", ans="For example y = 3x and y = 3x − 5."),
    ],
    check=["Can I identify gradient and intercept?", "Can I find the equation of a line from its graph?"], look=[], note=NOTE)

N[(11, "11.4")]["book"] = BK(
    keys=[("distance–time graph", "gradient = speed"), ("average speed", "total distance ÷ total time")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw a distance–time graph: 6 km in 30 min, stop 15 min, 6 km home in 45 min. Find each speed.", ans="12 km/h, 0, 8 km/h"),
        Ex("Find the average speed for the whole journey in Question 1.", ans="12 km in 1.5 h = 8 km/h"),
        Ex("Sketch the depth–time graph for filling a glass that is narrow at the bottom and wide at the top.", ans="Rises quickly at first, then more slowly (curve).", think=True),
    ],
    check=["Can I interpret distance–time graphs?", "Can I explain the shape of a real-life graph?"], look=[], note=NOTE)
