# -*- coding: utf-8 -*-
"""Stage 7 · Unit 8 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u08 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(8, "8.1")]["book"] = BK(
    keys=[("line of symmetry", "a fold line where the two halves match"), ("rotational symmetry", "the shape looks the same after a turn of less than 360°"), ("order", "how many times it looks the same in a full turn")],
    intro=[], examples=[],
    exercise=[
        Ex("Give the number of lines of symmetry and the order of rotational symmetry.", ("rectangle", "2, 2"), ("kite", "1, 1"), ("regular hexagon", "6, 6"), ("parallelogram", "0, 2")),
        Ex("Which capital letters have rotational symmetry of order 2: H, I, N, O, S, X, Z?", ans="H, I, N, S, Z have order 2; O and X have even higher orders."),
        Ex("Draw a shape with exactly 2 lines of symmetry and order 2.", ans="For example a rectangle or an ellipse."),
        Ex("A shape first looks the same after a 72° turn. What is its order?", ans="5"),
        Ex("Design a logo with rotational symmetry of order 3 but no lines of symmetry.", ans="For example a three-armed swirl.", think=True),
    ],
    check=["Can I find lines of symmetry?", "Can I find the order of rotational symmetry?", "Can I use the rule for regular polygons?"], look=[], note=NOTE)

N[(8, "8.2")]["book"] = BK(
    keys=[("chord", "a line joining two points on the circumference"), ("tangent", "a line touching the circle at one point"), ("regular polygon", "all sides and all angles equal")],
    intro=[], examples=[],
    exercise=[
        Ex("Name the part of the circle.", ("centre to edge", "radius"), ("distance all the way round", "circumference"), ("chord through the centre", "diameter")),
        Ex("A circle has diameter 15 cm. Write its radius.", ans="7.5 cm"),
        Ex("Name a polygon with", ("7 sides", "heptagon"), ("9 sides", "nonagon"), ("10 sides", "decagon")),
        Ex("A regular polygon has perimeter 63 cm and sides of 7 cm. Name it.", ans="nonagon (9 sides)"),
        Ex("Sketch an irregular hexagon and a regular hexagon. Explain the difference.", ans="Regular: equal sides and angles.", think=True),
    ],
    check=["Can I name the parts of a circle, including chord and tangent?", "Can I name polygons up to 10 sides?", "Can I tell regular from irregular?"], look=[], note=NOTE)

N[(8, "8.3")]["book"] = BK(
    keys=[("congruent", "exactly the same shape and size"), ("corresponding", "matching sides or angles in congruent shapes")],
    intro=[], examples=[],
    exercise=[
        Ex("Triangles ABC and DEF are congruent (in order). AB = 6 cm, BC = 8 cm, angle A = 53°, angle B = 90°.", ("DE", "6 cm"), ("EF", "8 cm"), ("angle D", "53°"), ("angle F", "37°")),
        Ex("Are these congruent? (a) two circles of radius 4 cm (b) squares of side 3 cm and 4 cm", ("(a)", "yes"), ("(b)", "no")),
        Ex("Draw a 4 × 4 grid. Divide it into 4 congruent shapes in two different ways.", ans="For example four 2 × 2 squares; four 1 × 4 strips."),
        Ex("Explain why two triangles with the same three angles need not be congruent.", ans="One could be an enlargement of the other.", think=True),
    ],
    check=["Can I recognise congruent shapes when turned or flipped?", "Can I match corresponding sides and angles?", "Can I find missing lengths and angles?"], look=[], note=NOTE)

N[(8, "8.4")]["book"] = BK(
    keys=[("face, edge, vertex", "surface, line where faces meet, corner"), ("prism", "same cross-section all the way through"), ("net", "a flat shape that folds into a 3D shape"), ("plan", "the view from above")],
    intro=[], examples=[],
    exercise=[
        Ex("Copy and complete: faces, edges, vertices.", ("cuboid", "6, 12, 8"), ("triangular prism", "5, 9, 6"), ("square-based pyramid", "5, 8, 5"), ("hexagonal prism", "8, 18, 12")),
        Ex("Sketch the front, side and top views of a square-based pyramid.", ans="triangle, triangle, square with diagonals"),
        Ex("Draw two different nets of a cube.", ans="For example the cross and the 'T' shape."),
        Ex("A shape has 6 vertices and 9 edges. How many faces?", ans="5"),
        Ex("Why do you think tennis balls come in cylinders rather than cuboids?", ans="A cylinder fits round balls closely with less wasted space and material.", think=True),
    ],
    check=["Can I name 3D shapes?", "Can I count faces, edges and vertices?", "Can I draw views and nets?"], look=[], note=NOTE)
