# -*- coding: utf-8 -*-
"""Stage 7 · Unit 14 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u14 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(14, "14.1")]["book"] = BK(
    keys=[("scale", "how map or plan distances relate to real ones"), ("plan", "a scale drawing seen from above")],
    intro=[], examples=[],
    exercise=[
        Ex("Scale 1 cm represents 4 km. Find the real distance for", ("3 cm", "12 km"), ("8.5 cm", "34 km")),
        Ex("Scale 1 : 50 000. Find the real distance in km for", ("4 cm", "2 km"), ("11 cm", "5.5 km")),
        Ex("A garden 18 m by 12 m is drawn at 1 : 200. What size is the drawing?", ans="9 cm by 6 cm"),
        Ex("Draw a plan of your bedroom at a scale of your choice. State the scale.", ans="Your own plan.", think=True),
    ],
    check=["Can I use a scale written in words or as a ratio?", "Can I convert map ↔ real distances?"], look=[], note=NOTE)

N[(14, "14.2")]["book"] = BK(
    keys=[("quadrant", "one of the four parts of a coordinate grid"), ("horizontal / vertical line", "same y / same x")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the distance between", ("(−4, 3) and (5, 3)", "9"), ("(2, −6) and (2, 1)", "7"), ("(−8, −2) and (−3, −2)", "5")),
        Ex("A rectangle has corners (−2, −3), (5, −3), (5, 1), (−2, 1). Find its perimeter and area.", ans="22 and 28"),
        Ex("Point M is 6 units left of (1, −4). Write its coordinates.", ans="(−5, −4)"),
        Ex("Explain why the distance from (−3, 0) to (4, 0) is not 4 − 3.", ans="It crosses zero: 3 + 4 = 7.", think=True),
    ],
    check=["Can I use coordinates in all four quadrants?", "Can I find horizontal and vertical distances?"], look=[], note=NOTE)

N[(14, "14.3")]["book"] = BK(
    keys=[("translation", "a slide: no turning, no flipping"), ("object / image", "the shape before / after")],
    intro=[], examples=[],
    exercise=[
        Ex("Translate the triangle (0, 0), (3, 0), (0, 2) by", ("4 right, 1 up", "(4, 1), (7, 1), (4, 3)"), ("2 left, 3 down", "(−2, −3), (1, −3), (−2, −1)")),
        Ex("Describe the translation.", ("(1, 2) → (6, −1)", "5 right, 3 down"), ("(−3, −3) → (−7, 2)", "4 left, 5 up")),
        Ex("Describe the translation that takes the image back to the object in Question 2.", ans="5 left 3 up; 4 right 5 down"),
        Ex("Design a border pattern using one shape and a repeated translation.", ans="Your own design.", think=True),
    ],
    check=["Can I translate a shape?", "Can I describe a translation?"], look=[], note=NOTE)

N[(14, "14.4")]["book"] = BK(
    keys=[("reflection", "a flip in a mirror line"), ("mirror line", "the line a shape is reflected in")],
    intro=[], examples=[],
    exercise=[
        Ex("Reflect the point in the given line.", ("(3, 5) in the x-axis", "(3, −5)"), ("(−2, 4) in the y-axis", "(2, 4)"), ("(4, 1) in x = 2", "(0, 1)"), ("(1, −1) in y = 2", "(1, 5)")),
        Ex("Find the mirror line.", ("(−5, 2) → (3, 2)", "x = −1"), ("(4, 7) → (4, −1)", "y = 3")),
        Ex("Reflect the triangle (1, 1), (4, 1), (4, 3) in the y-axis, then in the x-axis.", ans="(−1, 1), (−4, 1), (−4, 3) then (−1, −1), (−4, −1), (−4, −3)"),
        Ex("Write your name in capitals and reflect it in a vertical mirror line. Which letters look the same?", ans="Letters with a vertical line of symmetry, e.g. A, H, M, O, T.", think=True),
    ],
    check=["Can I reflect in horizontal and vertical lines?", "Can I find the mirror line?"], look=[], note=NOTE)

N[(14, "14.5")]["book"] = BK(
    keys=[("rotation", "a turn about a centre"), ("centre of rotation", "the point that stays still"), ("clockwise / anticlockwise", "the way clock hands turn / the opposite way")],
    intro=[], examples=[],
    exercise=[
        Ex("Rotate about (0, 0).", ("(4, 2) through 180°", "(−4, −2)"), ("(3, 0) 90° clockwise", "(0, −3)"), ("(0, 5) 90° anticlockwise", "(−5, 0)")),
        Ex("Rotate the triangle (2, 1), (5, 1), (2, 3) through 180° about (2, 1).", ans="(2, 1), (−1, 1), (2, −1)"),
        Ex("Describe the rotation that takes an arrow pointing left to pointing up.", ans="90° clockwise"),
        Ex("Use tracing paper to rotate a shape of your own 90° about one corner.", ans="Your own drawing.", think=True),
    ],
    check=["Can I rotate a shape 90° or 180°?", "Can I describe a rotation fully?"], look=[], note=NOTE)

N[(14, "14.6")]["book"] = BK(
    keys=[("enlargement", "a change of size, keeping the shape"), ("scale factor", "the number every length is multiplied by"), ("similar", "same shape, different size")],
    intro=[], examples=[],
    exercise=[
        Ex("Enlarge by the scale factor. Give the new lengths.", ("a 3 × 2 rectangle, sf 3", "9 × 6"), ("a triangle 2, 3, 4, sf 2.5", "5, 7.5, 10")),
        Ex("Find the scale factor.", ("4 cm → 28 cm", "7"), ("6 cm → 9 cm", "1.5")),
        Ex("On squared paper, draw a shape and enlarge it by scale factor 2. Compare the perimeters and the areas.", ans="Perimeter doubles; area × 4."),
        Ex("Is every square an enlargement of every other square? Explain.", ans="Yes – all angles are 90° and all sides are multiplied by the same factor.", think=True),
    ],
    check=["Can I enlarge a shape by a scale factor?", "Can I find a scale factor?", "Can I tell if a shape is an enlargement?"], look=[], note=NOTE)
