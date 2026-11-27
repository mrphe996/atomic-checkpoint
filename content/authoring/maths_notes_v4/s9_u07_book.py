# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u07 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(7, "7.1")]["book"] = BK(
    keys=[("circumference", "the distance round a circle, C = πd"), ("area of a circle", "A = πr²")],
    intro=[], examples=[],
    exercise=[
        Ex("Find C and A (1 d.p.).", ("r = 8 cm", "C = 50.3 cm, A = 201.1 cm²"), ("d = 15 m", "C = 47.1 m, A = 176.7 m²")),
        Ex("A circle has area 154 cm². Find its radius (1 d.p.).", ans="7.0 cm"),
        Ex("Find the perimeter of a semicircle with radius 9 cm (1 d.p.).", ans="46.3 cm"),
    ],
    check=["Can I find C and A, and work backwards?"], look=[], note=NOTE)

N[(7, "7.2")]["book"] = BK(
    keys=[("compound shape", "a shape made of simpler shapes")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the area (1 d.p.).", ("rectangle 12 × 8 with a semicircle of diameter 8 on one end", "121.1"), ("square of side 14 with a circle of radius 5 removed", "117.5")),
        Ex("A path 1 m wide goes round a 10 m × 6 m lawn. Find the area of the path.", ans="36 m²"),
    ],
    check=["Can I split shapes and add or subtract areas?"], look=[], note=NOTE)

N[(7, "7.3")]["book"] = BK(
    keys=[("prefix", "a word start showing a power of 10, e.g. micro = 10⁻⁶"), ("tonne", "1000 kg")],
    intro=[], examples=[],
    exercise=[
        Ex("Convert.", ("6.4 tonnes to kg", "6400 kg"), ("45 µm to mm", "0.045 mm"), ("3.2 GB to MB", "3200 MB"), ("750 mg to g", "0.75 g")),
        Ex("Order: 0.4 mm, 350 µm, 0.0005 m.", ans="350 µm, 0.4 mm, 0.0005 m"),
    ],
    check=["Do I know the prefixes giga to nano?", "Can I convert units?"], look=[], note=NOTE)
