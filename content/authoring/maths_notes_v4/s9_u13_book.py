# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u13 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(13, "13.1")]["book"] = BK(
    keys=[("scale", "the link between map and real lengths, e.g. 1 : 50 000"), ("bearing", "clockwise angle from north, three figures")],
    intro=[], examples=[],
    exercise=[
        Ex("Convert.", ("1 : 25 000, map 8 cm → real km", "2 km"), ("1 : 200 000, real 30 km → map cm", "15 cm")),
        Ex("A boat sails 5 km on 060°, then 3 km on 150°. Make a scale drawing (1 cm : 1 km) and find its distance and bearing from the start.", ans="≈ 5.8 km on ≈ 091°"),
    ],
    check=["Can I use scales and bearings together?"], look=[], note=NOTE)

N[(13, "13.2")]["book"] = BK(
    keys=[("line segment", "part of a line between two points")],
    intro=[], examples=[],
    exercise=[
        Ex("A(2, 1), B(14, 10). Find the point", ("⅓ of the way from A", "(6, 4)"), ("¾ of the way from A", "(11, 7.75)"), ("dividing AB in 1 : 2", "(6, 4)")),
        Ex("P(4, 5) is ¼ of the way from A(1, 2) to B. Find B.", ans="(13, 14)"),
    ],
    check=["Can I find points a fraction of the way along a segment?"], look=[], note=NOTE)

N[(13, "13.3")]["book"] = BK(
    keys=[("combination of transformations", "one transformation followed by another"), ("congruent", "same shape and size")],
    intro=[], examples=[],
    exercise=[
        Ex("Triangle (1, 1), (4, 1), (1, 3). Find the final image.", ("reflect in the y-axis, then translate (2 over −3)", "(1, −2), (−2, −2), (1, 0)"), ("rotate 180° about (0, 0), then reflect in the x-axis", "(−1, 1), (−4, 1), (−1, 3)")),
        Ex("Describe the single transformation equivalent to reflecting in x = 2 then in x = 5.", ans="translation (6 over 0)"),
    ],
    check=["Can I combine transformations and describe the result?"], look=[], note=NOTE)

N[(13, "13.4")]["book"] = BK(
    keys=[("ray line", "a line through an object vertex and its image vertex, used to find the centre")],
    intro=[], examples=[],
    exercise=[
        Ex("A rectangle 3 cm × 7 cm is enlarged by scale factor 4.", ("new perimeter", "80 cm"), ("new area", "336 cm²")),
        Ex("Enlarge the triangle (1, 2), (3, 2), (1, 5) by scale factor 2, centre (0, 1).", ans="(2, 3), (6, 3), (2, 9)"),
    ],
    check=["Can I enlarge from a centre and describe enlargements?", "Do I know area × k²?"], look=[], note=NOTE)
