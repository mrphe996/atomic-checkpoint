# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u15 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(15, "15.1")]["book"] = BK(
    keys=[("mile", "an imperial unit of distance; 5 miles ≈ 8 km"), ("kilometre", "1000 metres")],
    intro=[], examples=[],
    exercise=[
        Ex("Convert.", ("55 miles to km", "88 km"), ("144 km to miles", "90 miles"), ("3 miles to km", "4.8 km")),
        Ex("Which is further, 85 km or 50 miles?", ans="85 km (50 miles = 80 km)"),
        Ex("Make a conversion table for 0–100 miles in steps of 20.", ans="0, 32, 64, 96, 128, 160 km"),
    ],
    check=["Can I convert miles ↔ km?", "Can I compare distances in different units?"], look=[], note=NOTE)

N[(15, "15.2")]["book"] = BK(
    keys=[("perpendicular height", "height at right angles to the base"), ("trapezium", "a quadrilateral with one pair of parallel sides")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the area.", ("parallelogram b 14 cm, h 6 cm", "84 cm²"), ("trapezium a 5 m, b 11 m, h 4 m", "32 m²")),
        Ex("A trapezium has area 50 cm², height 5 cm and one parallel side 7 cm. Find the other.", ans="13 cm"),
        Ex("Draw two different parallelograms with area 24 cm².", ans="For example 6 × 4 and 8 × 3.", think=True),
    ],
    check=["Can I use A = bh and A = ½(a + b)h?", "Can I find a missing length?"], look=[], note=NOTE)

N[(15, "15.3")]["book"] = BK(
    keys=[("prism", "a solid with the same cross-section throughout"), ("cross-section", "the shape you see when you cut across the prism")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the volume of the triangular prism.", ("triangle b 5, h 6, length 9", "135"), ("triangle b 2.4 m, h 1 m, length 5 m", "6 m³")),
        Ex("A prism has volume 360 cm³ and triangle ends with base 8 cm, height 6 cm. Find its length.", ans="15 cm"),
    ],
    check=["Can I find the volume of a triangular prism?", "Can I find a missing length?"], look=[], note=NOTE)

N[(15, "15.4")]["book"] = BK(
    keys=[("surface area", "total area of all the faces"), ("net", "a flat shape that folds into a solid"), ("slant height", "the height of a triangular face of a pyramid")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the surface area.", ("triangular prism, 6-8-10 ends, length 4", "144"), ("square pyramid, base 8, slant 7", "176")),
        Ex("Sketch the net of a triangular prism and label each face's area for ends ½ × 3 × 4 and length 6.", ans="2 × 6 + 18 + 24 + 30 = 84"),
    ],
    check=["Can I find surface areas of prisms and pyramids?", "Can I use nets?"], look=[], note=NOTE)
