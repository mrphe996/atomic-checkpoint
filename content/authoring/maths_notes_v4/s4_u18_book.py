# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u18 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(18, "18.1")]["book"] = BK(
    keys=[("coordinates", "(across, up)"), ("translation", "a slide with no turning")],
    intro=[], examples=[],
    exercise=[
        Ex("Where does the point end up?", ("(2, 3) 3 east", "(5, 3)"), ("(4, 5) 2 south", "(4, 3)"), ("(6, 1) 4 west 2 north", "(2, 3)")),
        Ex("Draw a map of your classroom on a grid. Write the coordinates of the door and your desk.", ans="Answers vary.", think=True),
    ],
    check=["Can I use coordinates, compass directions and translations?"], look=[], note=NOTE)

N[(18, "18.2")]["book"] = BK(
    keys=[("reflection", "a flip over a mirror line"), ("mirror line", "the line a shape is reflected in")],
    intro=[], examples=[],
    exercise=[
        Ex("Reflect in the vertical line x = 5.", ("(3, 2)", "(7, 2)"), ("(6, 4)", "(4, 4)"), ("(5, 1)", "(5, 1)")),
        Ex("On squared paper, draw a shape next to a mirror line and reflect it.", ans="Answers vary.", think=True),
    ],
    check=["Can I reflect shapes in horizontal and vertical mirror lines?"], look=[], note=NOTE)
