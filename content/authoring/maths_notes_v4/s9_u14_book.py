# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u14 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(14, "14.1")]["book"] = BK(
    keys=[("prism", "a solid with a constant cross-section"), ("cylinder", "a prism-like solid with a circular cross-section; V = πr²h")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the volume (1 d.p.).", ("cylinder r = 4 cm, h = 9 cm", "452.4 cm³"), ("trapezium prism: sides 5 and 9, height 4, length 12", "336"), ("cylinder d = 1.5 m, h = 2 m (in litres)", "≈ 3534 L")),
        Ex("A cylinder holds 2 litres and has radius 6 cm. Find its height.", ans="≈ 17.7 cm"),
    ],
    check=["Can I find volumes of prisms and cylinders?"], look=[], note=NOTE)

N[(14, "14.2")]["book"] = BK(
    keys=[("curved surface", "the side of a cylinder; area 2πrh")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the total surface area (1 d.p.).", ("cylinder r = 6, h = 10", "603.2"), ("open-top cylinder r = 3, h = 7", "160.2"), ("square pyramid base 12, slant 10", "384")),
        Ex("Sketch the net of a cylinder with r = 2 cm and h = 5 cm, labelling all lengths.", ans="two circles r = 2; rectangle 12.6 cm × 5 cm"),
    ],
    check=["Can I find surface areas of prisms, pyramids and cylinders?"], look=[], note=NOTE)

N[(14, "14.3")]["book"] = BK(
    keys=[("plane of symmetry", "a flat surface that cuts a solid into two mirror-image halves")],
    intro=[], examples=[],
    exercise=[
        Ex("How many planes of symmetry?", ("cuboid 2 × 4 × 6", "3"), ("cube", "9"), ("regular pentagonal prism", "6"), ("square-based pyramid", "4")),
        Ex("Draw a cuboid on isometric paper and shade one plane of symmetry.", ans="Answers vary.", think=True),
    ],
    check=["Can I identify planes of symmetry in 3D shapes?"], look=[], note=NOTE)
