# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u05 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(5, "5.1")]["book"] = BK(
    keys=[("corresponding / alternate angles", "equal angles at parallel lines"), ("co-interior angles", "add to 180° between parallel lines")],
    intro=[], examples=[],
    exercise=[
        Ex("Find x and give reasons.", ("co-interior angles x and 72°", "108°"), ("isosceles triangle with apex 36°, base angle x", "72°"), ("parallelogram angles 2x + 10 and 3x − 30", "x = 40")),
        Ex("Show that the angles of a triangle add to 180° using a line parallel to one side.", ans="Alternate angles + straight line."),
    ],
    check=["Can I combine several angle facts with reasons?"], look=[], note=NOTE)

N[(5, "5.2")]["book"] = BK(
    keys=[("interior angle", "an angle inside a polygon"), ("regular polygon", "all sides and angles equal")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the interior angle sum.", ("heptagon", "900°"), ("15-gon", "2340°")),
        Ex("Find each interior angle of a regular", ("nonagon", "140°"), ("20-gon", "162°")),
        Ex("A polygon's angles add to 3240°. How many sides?", ans="20"),
    ],
    check=["Can I use (n − 2) × 180°?"], look=[], note=NOTE)

N[(5, "5.3")]["book"] = BK(
    keys=[("exterior angle", "the turn at a vertex; interior + exterior = 180°")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the exterior angle of a regular", ("octagon", "45°"), ("15-gon", "24°")),
        Ex("A regular polygon has exterior angle 12°. How many sides? What is the interior angle?", ans="30 sides; 168°"),
    ],
    check=["Do I know exterior angles total 360°?"], look=[], note=NOTE)

N[(5, "5.4")]["book"] = BK(
    keys=[("inscribe", "draw a shape with its vertices on a circle"), ("construct", "draw accurately with ruler and compasses")],
    intro=[], examples=[],
    exercise=[
        Ex("Construct with ruler and compasses only.", ("an angle of 60°", "equilateral-triangle arcs"), ("an angle of 30°", "bisect 60°"), ("an angle of 45°", "bisect 90°")),
        Ex("Inscribe a regular hexagon in a circle of radius 4 cm. Measure its perimeter.", ans="24 cm"),
        Ex("Inscribe a square and then a regular octagon in a circle.", ans="Perpendicular diameters, then bisect the right angles."),
    ],
    check=["Can I construct 60°, 30°, 45°?", "Can I inscribe regular polygons?"], look=[], note=NOTE)

N[(5, "5.5")]["book"] = BK(
    keys=[("hypotenuse", "the longest side, opposite the right angle"), ("Pythagoras' theorem", "a² + b² = c²")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the missing side (1 d.p. where needed).", ("legs 9 and 12", "15"), ("hypotenuse 20, leg 16", "12"), ("legs 5 and 9", "10.3")),
        Ex("Is a triangle with sides 11, 60, 61 right-angled?", ans="Yes: 121 + 3600 = 3721 = 61²"),
        Ex("Find the distance between (−2, 1) and (4, 9).", ans="10"),
    ],
    check=["Can I find any side of a right-angled triangle?"], look=[], note=NOTE)
