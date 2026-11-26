# -*- coding: utf-8 -*-
"""Stage 8 · Unit 5 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u05 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(5, "5.1")]["book"] = BK(
    keys=[("transversal", "a line crossing parallel lines"), ("corresponding angles", "same position at each crossing (F) – equal"), ("alternate angles", "opposite sides, between the lines (Z) – equal"), ("co-interior angles", "same side, between the lines (C) – add to 180°")],
    intro=[], examples=[],
    exercise=[
        Ex("One angle at a crossing is 74°. Find", ("its corresponding angle", "74°"), ("its alternate angle", "74°"), ("its co-interior angle", "106°")),
        Ex("Alternate angles are 5x − 12 and 3x + 20. Find x and the angle.", ans="x = 16; 68°"),
        Ex("Corresponding angles are 81° and 79°. Are the lines parallel? Explain.", ans="No – corresponding angles would be equal."),
        Ex("Prove that the angles of a triangle add to 180° using a parallel line.", ans="Alternate angles + angles on a straight line.", think=True),
    ],
    check=["Can I use corresponding, alternate and co-interior angles?", "Can I give reasons?"], look=[], note=NOTE)

N[(5, "5.2")]["book"] = BK(
    keys=[("exterior angle", "angle between one side and the extension of the next"), ("interior opposite angles", "the two inside angles not next to it")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the exterior angle.", ("opposite angles 54° and 71°", "125°"), ("opposite angles 90° and 23°", "113°")),
        Ex("Find the missing interior angle.", ("exterior 118°, one opposite 49°", "69°"), ("exterior 155°, one opposite 90°", "65°")),
        Ex("Opposite interior angles x + 15 and 2x; exterior angle 120°. Find x.", ans="35"),
        Ex("Prove the exterior angle fact.", ans="a + b + c = 180 and c + e = 180, so e = a + b.", think=True),
    ],
    check=["Can I find exterior angles?", "Can I prove the exterior angle fact?"], look=[], note=NOTE)

N[(5, "5.3")]["book"] = BK(
    keys=[("construct", "draw accurately with ruler and compasses"), ("perpendicular bisector", "cuts a line in half at 90°"), ("angle bisector", "cuts an angle in half"), ("arc", "part of a circle")],
    intro=[], examples=[],
    exercise=[
        Ex("Construct triangle PQR with PQ = 8 cm, QR = 6 cm, PR = 7 cm. Measure angle Q.", ans="about 58°"),
        Ex("Draw a line 9 cm long and construct its perpendicular bisector. Check with a ruler and protractor.", ans="It crosses at 4.5 cm, at 90°."),
        Ex("Draw an angle of 110° and construct its bisector. Measure both halves.", ans="55° each"),
        Ex("Mark two points 6 cm apart. Shade the region closer to the first point than the second.", ans="One side of the perpendicular bisector.", think=True),
    ],
    check=["Can I construct triangles?", "Can I construct perpendicular and angle bisectors?"], look=[], note=NOTE)
