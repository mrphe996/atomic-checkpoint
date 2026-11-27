# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u07 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(7, "7.1")]["book"] = BK(
    keys=[("area", "the space inside a flat shape, in square units"), ("height of a triangle", "the distance at right angles from the base to the top corner")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the area.", ("triangle base 14 cm, height 6 cm", "42 cm²"), ("triangle base 5 m, height 9 m", "22.5 m²")),
        Ex("A triangle has area 30 cm² and height 10 cm. Find its base.", ans="6 cm"),
    ],
    check=["Can I find the area of a triangle?"], look=[], note=NOTE)

N[(7, "7.2")]["book"] = BK(
    keys=[("decimal hours", "time written like 2.5 h")],
    intro=[], examples=[],
    exercise=[
        Ex("Write in hours and minutes.", ("3.25 h", "3 h 15 min"), ("1.8 h", "1 h 48 min")),
        Ex("Write as decimal hours.", ("2 h 45 min", "2.75 h"), ("4 h 6 min", "4.1 h")),
    ],
    check=["Can I convert between decimal and mixed time units?"], look=[], note=NOTE)
