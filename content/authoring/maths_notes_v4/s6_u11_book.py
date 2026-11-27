# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u11 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(11, "11.1")]["book"] = BK(
    keys=[("net", "a flat shape that folds to make a 3D shape"), ("surface area", "total area of all the faces")],
    intro=[], examples=[],
    exercise=[
        Ex("Sketch two different nets of a cube.", ans="e.g. a cross and a T shape."),
        Ex("Find the surface area.", ("cube edge 7 cm", "294 cm²"), ("cuboid 6 × 4 × 3 cm", "108 cm²")),
    ],
    check=["Can I sketch nets?", "Can I find surface area from a net?"], look=[], note=NOTE)

N[(11, "11.2")]["book"] = BK(
    keys=[("volume", "space taken up, in cm³ or m³"), ("capacity", "how much a container can hold, in mL or L")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the volume.", ("cuboid 7 × 5 × 3 cm", "105 cm³"), ("cube edge 9 cm", "729 cm³")),
        Ex("A box is 30 cm × 20 cm × 15 cm. What is its capacity in litres?", ans="9 L"),
    ],
    check=["Do I know the difference between volume and capacity?"], look=[], note=NOTE)
