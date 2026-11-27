# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u05 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(5, "5.1")]["book"] = BK(
    keys=[("parallel", "always the same distance apart"), ("diagonal", "a line joining opposite corners")],
    intro=[], examples=[],
    exercise=[
        Ex("Name the quadrilateral.", ("4 equal sides, no right angles", "rhombus"), ("exactly 1 pair of parallel sides", "trapezium"), ("opposite sides equal, 4 right angles, not a square", "rectangle")),
        Ex("True or false: every rhombus is a parallelogram. Explain.", ans="True – both pairs of opposite sides are parallel."),
    ],
    check=["Can I classify quadrilaterals by their properties?"], look=[], note=NOTE)

N[(5, "5.2")]["book"] = BK(
    keys=[("radius", "centre to the circle"), ("diameter", "across the circle through the centre"), ("circumference", "the distance round the circle")],
    intro=[], examples=[],
    exercise=[
        Ex("Copy and complete.", ("r = 6 cm, d = ?", "12 cm"), ("d = 15 cm, r = ?", "7.5 cm")),
        Ex("Use compasses to draw circles with radius 4 cm and diameter 6 cm.", ans="Compasses set to 4 cm and 3 cm."),
    ],
    check=["Do I know the parts of a circle?", "Can I draw circles accurately?"], look=[], note=NOTE)

N[(5, "5.3")]["book"] = BK(
    keys=[("rotational symmetry", "looks the same more than once in a full turn"), ("order", "how many times it fits in a full turn")],
    intro=[], examples=[],
    exercise=[
        Ex("Order of rotational symmetry?", ("square", "4"), ("letter N", "2"), ("regular hexagon", "6"), ("kite", "1")),
        Ex("Draw a pattern with rotational symmetry of order 3.", ans="Answers vary.", think=True),
    ],
    check=["Can I find the order of rotational symmetry?"], look=[], note=NOTE)
