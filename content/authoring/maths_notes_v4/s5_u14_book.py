# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u14 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(14, "14.1")]["book"] = BK(
    keys=[("perimeter", "the total distance around a shape"), ("compound shape", "a shape made of rectangles")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the perimeter.", ("rectangle 9 cm by 4 cm", "26 cm"), ("square side 11 m", "44 m"), ("L-shape sides 7, 2, 4, 3, 3, 5 m", "24 m")),
        Ex("Measure the perimeter of your desk or a book.", ans="Answers vary.", think=True),
    ],
    check=["Can I find the perimeter of rectangles and compound shapes?"], look=[], note=NOTE)

N[(14, "14.2")]["book"] = BK(
    keys=[("area", "the surface a shape covers, in square units")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the area.", ("rectangle 7 cm by 5 cm", "35 cm²"), ("square side 12 m", "144 m²"), ("L-shape: 4 × 3 and 2 × 2", "16 cm²")),
        Ex("A rectangle has area 54 cm² and length 9 cm. Find its width.", ans="6 cm"),
    ],
    check=["Can I find the area of rectangles and shapes made from rectangles?"], look=[], note=NOTE)
