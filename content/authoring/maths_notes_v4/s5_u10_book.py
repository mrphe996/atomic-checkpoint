# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u10 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(10, "10.1")]["book"] = BK(
    keys=[("acute", "less than 90°"), ("obtuse", "between 90° and 180°"), ("protractor", "a tool for measuring angles")],
    intro=[], examples=[],
    exercise=[
        Ex("Classify each angle.", ("38°", "acute"), ("90°", "right"), ("146°", "obtuse"), ("180°", "straight")),
        Ex("Draw angles of 30°, 75° and 130° with a protractor. Estimate first.", ans="Check with a protractor.", think=True),
    ],
    check=["Can I classify, estimate and measure angles?"], look=[], note=NOTE)

N[(10, "10.2")]["book"] = BK(
    keys=[("angles on a straight line", "add up to 180°")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the missing angle on a straight line.", ("55°", "125°"), ("142°", "38°"), ("20° and 90°", "70°"), ("three equal angles", "60° each")),
    ],
    check=["Can I find missing angles on a straight line?"], look=[], note=NOTE)
