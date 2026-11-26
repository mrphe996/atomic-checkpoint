# -*- coding: utf-8 -*-
"""Stage 7 · Unit 5 – Words to know, Practice on paper and checklists for the lesson documents (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u05 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(5, "5.1")]["book"] = BK(
    keys=[("full turn", "360°"), ("quadrilateral", "a shape with four straight sides"), ("reflex angle", "an angle between 180° and 360°")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the missing angle around a point.", ("110°, 130°, x", "120°"), ("90°, 45°, 75°, y", "150°"), ("z, z, z, 60°", "100°")),
        Ex("Find the missing angle in each quadrilateral.", ("70°, 85°, 105°, a", "100°"), ("90°, 90°, 48°, b", "132°")),
        Ex("A fan has 6 equally spaced blades. What angle is between neighbouring blades?", ans="60°"),
        Ex("Around a point: 2p, 3p, 4p and 90°. Find p.", ans="p = 30"),
        Ex("Smaller angle between clock hands at (a) 1 o'clock (b) 7 o'clock", ("1 o'clock", "30°"), ("7 o'clock", "150°")),
        Ex("Draw any quadrilateral, measure its angles and add them. How close to 360° are you? Why might it not be exact?", ans="About 360°; small measuring errors.", think=True),
    ],
    check=["Can I use angles around a point (360°)?", "Can I find a missing angle in a quadrilateral?", "Can I explain why quadrilateral angles add to 360°?"], look=[], note=NOTE)

N[(5, "5.2")]["book"] = BK(
    keys=[("intersect", "cross or meet"), ("vertically opposite angles", "equal angles opposite each other where two lines cross"), ("transversal", "a line crossing two or more lines"), ("parallel", "always the same distance apart")],
    intro=[], examples=[],
    exercise=[
        Ex("Two lines cross. One angle is given. Find the other three.", ("52°", "128°, 52°, 128°"), ("97°", "83°, 97°, 83°")),
        Ex("Find x.", ("vertically opposite angles 4x and 100°", "25"), ("angles on a line x and x + 40", "70")),
        Ex("Parallel lines: one angle is 63°. Find (a) its corresponding angle (b) its alternate angle (c) the angle on a straight line with it.", ("corresponding", "63°"), ("alternate", "63°"), ("straight line", "117°")),
        Ex("A triangle has angles 48° and 67°. Find the third angle and the outside angle next to it.", ans="65° and 115°"),
        Ex("Explain why the outside angle of a triangle equals the sum of the two opposite inside angles.", ans="Both the outside angle and the two opposite angles make 180° with the third inside angle.", think=True),
    ],
    check=["Can I use vertically opposite angles?", "Can I use corresponding and alternate angles?", "Can I give a reason for each step?"], look=[], note=NOTE)

N[(5, "5.3")]["book"] = BK(
    keys=[("perpendicular", "at right angles (90°)"), ("set square", "a triangle used to draw right angles and parallel lines"), ("protractor", "a tool to measure and draw angles")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw a line 8 cm long. Mark a point 3 cm from one end and draw a perpendicular line through it.", ans="Check the angle is 90°."),
        Ex("Draw a line and a point 4 cm above it. Draw a line through the point parallel to the first line.", ans="Check the gap is 4 cm at both ends."),
        Ex("Draw accurately.", ("a rectangle 6.5 cm by 3 cm", "diagonals ≈ 7.2 cm"), ("a square of side 4.5 cm", "diagonals ≈ 6.4 cm")),
        Ex("Draw parallelogram ABCD: AB = 7 cm, angle A = 55°, AD = 4 cm. Measure angle B.", ans="125°"),
        Ex("Draw a kite with diagonals 8 cm and 5 cm. Describe your method.", ans="Short diagonal cut in half at 90° by the long one, at any point.", think=True),
    ],
    check=["Can I draw perpendicular and parallel lines?", "Can I draw a quadrilateral from given lengths and angles?", "Can I check my drawing?"], look=[], note=NOTE)
