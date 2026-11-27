# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u05 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(5, "5.1")]["book"] = BK(
    keys=[("centimetre, metre, kilometre", "units of length: 100 cm = 1 m, 1000 m = 1 km")],
    intro=[], examples=[],
    exercise=[
        Ex("Convert.", ("5 m to cm", "500 cm"), ("700 cm to m", "7 m"), ("1 m 45 cm to cm", "145 cm"), ("3 km to m", "3000 m")),
        Ex("Measure three things in your room with a ruler or tape and write the lengths.", ans="Answers vary.", think=True),
    ],
    check=["Can I estimate, measure and convert lengths?"], look=[], note=NOTE)

N[(5, "5.2")]["book"] = BK(
    keys=[("perimeter", "the distance around a shape")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the perimeter.", ("rectangle 7 cm by 3 cm", "20 cm"), ("square side 6 m", "24 m"), ("triangle 4, 5, 6 cm", "15 cm")),
    ],
    check=["Can I find the perimeter by adding the sides?"], look=[], note=NOTE)

N[(5, "5.3")]["book"] = BK(
    keys=[("area", "the surface a shape covers, counted in squares")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the area in squares.", ("3 rows of 5", "15"), ("6 by 2", "12"), ("8 whole + 4 half squares", "10")),
        Ex("Draw three different shapes with an area of 8 squares on squared paper.", ans="Answers vary.", think=True),
    ],
    check=["Can I find area by counting squares?"], look=[], note=NOTE)
