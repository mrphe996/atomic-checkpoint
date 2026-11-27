# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u18 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(18, "18.1")]["book"] = BK(
    keys=[("coordinates", "(x, y): across, then up"), ("origin", "the point (0, 0)")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw a grid from 0 to 8. Plot and join (1, 1), (6, 1), (6, 4). Write the fourth vertex of the rectangle.", ans="(1, 4)"),
        Ex("Which axis is the point on?", ("(0, 6)", "y-axis"), ("(3, 0)", "x-axis")),
        Ex("Draw a picture by joining points and write its coordinates for a friend to copy.", ans="Answers vary.", think=True),
    ],
    check=["Can I read and plot coordinates?"], look=[], note=NOTE)

N[(18, "18.2")]["book"] = BK(
    keys=[("translation", "a slide: same size, same way round")],
    intro=[], examples=[],
    exercise=[
        Ex("Translate the point.", ("(2, 3) 4 right", "(6, 3)"), ("(5, 6) 2 left 3 down", "(3, 3)"), ("(0, 1) 3 right 5 up", "(3, 6)")),
        Ex("Describe the translation.", ("(1, 2) → (5, 2)", "4 right"), ("(6, 5) → (4, 1)", "2 left, 4 down")),
    ],
    check=["Can I translate shapes and describe translations?"], look=[], note=NOTE)
