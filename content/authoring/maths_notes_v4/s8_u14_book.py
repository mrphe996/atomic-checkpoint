# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u14 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(14, "14.1")]["book"] = BK(
    keys=[("bearing", "a direction measured clockwise from north, written with three figures")],
    intro=[], examples=[],
    exercise=[
        Ex("Write as bearings.", ("east", "090°"), ("south-west", "225°"), ("12° clockwise from north", "012°")),
        Ex("Find the back bearing.", ("055°", "235°"), ("260°", "080°")),
        Ex("A boat sails 6 km on a bearing of 120°. Make a scale drawing with 1 cm : 1 km.", ans="A 6 cm line at 120° clockwise from north."),
    ],
    check=["Can I write and measure bearings?", "Can I find back bearings?"], look=[], note=NOTE)

N[(14, "14.2")]["book"] = BK(
    keys=[("midpoint", "the point halfway along a line segment"), ("line segment", "part of a line with two ends")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the midpoint.", ("(2, 8) and (6, 2)", "(4, 5)"), ("(−5, 3) and (1, −1)", "(−2, 1)"), ("(0, 0) and (3, 7)", "(1.5, 3.5)")),
        Ex("M(2, −1) is the midpoint of AB and A is (−3, 4). Find B.", ans="(7, −6)"),
    ],
    check=["Can I find a midpoint, including with negatives?", "Can I find a missing end?"], look=[], note=NOTE)

N[(14, "14.3")]["book"] = BK(
    keys=[("column vector", "top: across; bottom: up/down"), ("congruent", "same shape and size")],
    intro=[], examples=[],
    exercise=[
        Ex("Translate the point.", ("(4, 1) by (−3 over 5)", "(1, 6)"), ("(−2, −2) by (6 over 1)", "(4, −1)")),
        Ex("Write the vector that moves (5, −1) to (−1, 3).", ans="(−6 over 4)"),
        Ex("Translate the triangle (0, 0), (2, 0), (0, 3) by (3 over −2) on squared paper.", ans="(3, −2), (5, −2), (3, 1)"),
    ],
    check=["Can I translate using column vectors?", "Can I describe a translation?"], look=[], note=NOTE)

N[(14, "14.4")]["book"] = BK(
    keys=[("mirror line", "the line of reflection, e.g. x = 2, y = −1, y = x")],
    intro=[], examples=[],
    exercise=[
        Ex("Reflect the point.", ("(5, 2) in x = 3", "(1, 2)"), ("(−1, −4) in y = −2", "(−1, 0)"), ("(6, −1) in y = x", "(−1, 6)")),
        Ex("(1, 2) → (7, 2) and (3, 5) → (5, 5). Find the mirror line.", ans="x = 4"),
    ],
    check=["Can I reflect in lines x = a, y = b and y = x?", "Can I find a mirror line?"], look=[], note=NOTE)

N[(14, "14.5")]["book"] = BK(
    keys=[("centre of rotation", "the fixed point a shape turns about"), ("clockwise / anticlockwise", "the direction of turn")],
    intro=[], examples=[],
    exercise=[
        Ex("Rotate about (0, 0).", ("(4, 2) 90° clockwise", "(2, −4)"), ("(−3, 1) 90° anticlockwise", "(−1, −3)"), ("(5, −5) 180°", "(−5, 5)")),
        Ex("Rotate (3, 4) 90° clockwise about (1, 2).", ans="(3, 0)"),
        Ex("Describe the rotation that maps (2, 0), (4, 0), (4, 1) onto (0, 2), (0, 4), (−1, 4).", ans="90° anticlockwise about (0, 0)"),
    ],
    check=["Can I rotate shapes?", "Can I describe a rotation fully?"], look=[], note=NOTE)

N[(14, "14.6")]["book"] = BK(
    keys=[("enlargement", "a copy with lengths multiplied and angles kept"), ("scale factor", "image length ÷ object length"), ("centre of enlargement", "the point the enlargement is measured from")],
    intro=[], examples=[],
    exercise=[
        Ex("Enlarge the point.", ("(3, 1) by 4, centre (0, 0)", "(12, 4)"), ("(5, 4) by 2, centre (1, 2)", "(9, 6)")),
        Ex("Enlarge the square (1, 1), (2, 1), (2, 2), (1, 2) by scale factor 3, centre (0, 0). Find the new side and area.", ans="(3, 3), (6, 3), (6, 6), (3, 6); side 3, area 9"),
        Ex("Why do the lines through matching vertices meet at the centre?", ans="Each image point lies on the ray from the centre through the object point.", think=True),
    ],
    check=["Can I enlarge shapes from a centre?", "Can I find a scale factor and centre?"], look=[], note=NOTE)
