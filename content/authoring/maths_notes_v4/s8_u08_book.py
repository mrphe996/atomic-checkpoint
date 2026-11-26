# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u08 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(8, "8.1")]["book"] = BK(
    keys=[("hierarchy", "families of shapes, each inside a bigger family"), ("diagonal", "a line joining opposite corners")],
    intro=[], examples=[],
    exercise=[
        Ex("Name the quadrilateral.", ("diagonals equal and perpendicular", "square"), ("one pair of parallel sides", "trapezium"), ("4 equal sides, angles not 90°", "rhombus")),
        Ex("True or false? Explain.", ("every rectangle is a square", "false"), ("every rhombus is a parallelogram", "true")),
        Ex("Draw a diagram showing the hierarchy of quadrilaterals.", ans="quadrilateral → trapezium → parallelogram → rectangle / rhombus → square; kite → rhombus"),
    ],
    check=["Can I describe the properties of quadrilaterals?", "Can I explain the hierarchy?"], look=[], note=NOTE)

N[(8, "8.2")]["book"] = BK(
    keys=[("π (pi)", "C ÷ d for every circle, ≈ 3.14159"), ("circumference", "the distance around a circle: C = πd = 2πr")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the circumference (1 d.p.).", ("d = 9 cm", "28.3 cm"), ("r = 4 m", "25.1 m"), ("d = 0.6 m", "1.9 m")),
        Ex("A circle has circumference 62.8 cm. Find its radius.", ans="10 cm"),
        Ex("Find the perimeter of a semicircle of radius 5 cm.", ans="25.7 cm"),
        Ex("Measure 3 round objects and work out C ÷ d. How close to π are you?", ans="Your own results.", think=True),
    ],
    check=["Can I use C = πd and C = 2πr?", "Can I find d or r from C?"], look=[], note=NOTE)

N[(8, "8.3")]["book"] = BK(
    keys=[("plan", "view from above"), ("elevation", "view from the front or side"), ("Euler's rule", "F + V − E = 2")],
    intro=[], examples=[],
    exercise=[
        Ex("Use F + V − E = 2.", ("F = 8, V = 12", "E = 18"), ("V = 9, E = 16", "F = 9")),
        Ex("Draw the plan, front and side elevations of a triangular prism lying on a rectangular face.", ans="rectangle, triangle, rectangle"),
        Ex("Build a shape from 6 cubes and draw its three views.", ans="Your own drawing.", think=True),
    ],
    check=["Can I use Euler's rule?", "Can I draw plans and elevations?"], look=[], note=NOTE)
