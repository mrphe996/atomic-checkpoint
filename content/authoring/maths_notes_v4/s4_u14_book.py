# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u14 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(14, "14.1")]["book"] = BK(
    keys=[("area", "the surface a shape covers (cm²)"), ("perimeter", "the distance around a shape (cm)")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw on squared paper and find the area and perimeter.", ("a 5 × 2 rectangle", "10 cm², 14 cm"), ("a 3 × 3 square", "9 cm², 12 cm")),
        Ex("Draw around your hand on squared paper and estimate its area.", ans="Answers vary.", think=True),
    ],
    check=["Can I estimate and measure area and perimeter on squared paper?"], look=[], note=NOTE)

N[(14, "14.2")]["book"] = BK(
    keys=[("length × width", "the area of a rectangle")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the area and perimeter.", ("7 cm by 3 cm", "21 cm², 20 cm"), ("9 m by 4 m", "36 m², 26 m"), ("square of side 6 cm", "36 cm², 24 cm")),
        Ex("A rectangle has area 40 cm² and length 8 cm. Find the width and the perimeter.", ans="5 cm, 26 cm"),
    ],
    check=["Can I calculate the area and perimeter of rectangles?"], look=[], note=NOTE)
