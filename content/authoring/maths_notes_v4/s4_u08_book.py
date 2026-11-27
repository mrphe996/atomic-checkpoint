# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u08 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(8, "8.1")]["book"] = BK(
    keys=[("angle", "an amount of turn"), ("vertex", "the point where two arms meet")],
    intro=[], examples=[],
    exercise=[
        Ex("Smaller than, equal to or bigger than a right angle?", ("clock hands at 2 o'clock", "smaller"), ("corner of a door", "equal"), ("clock hands at 5 o'clock", "bigger")),
        Ex("Make a right-angle checker by folding paper. Find 3 right angles in your classroom.", ans="Answers vary.", think=True),
    ],
    check=["Can I compare and order angles using a right angle?"], look=[], note=NOTE)

N[(8, "8.2")]["book"] = BK(
    keys=[("acute", "less than 90°"), ("obtuse", "between 90° and 180°")],
    intro=[], examples=[],
    exercise=[
        Ex("Acute, right or obtuse?", ("25°", "acute"), ("90°", "right"), ("145°", "obtuse"), ("95°", "obtuse")),
        Ex("Write a capital letter that has an acute angle and one that has a right angle.", ans="e.g. V (acute), L (right)."),
    ],
    check=["Can I classify angles as acute, right or obtuse?"], look=[], note=NOTE)

N[(8, "8.3")]["book"] = BK(
    keys=[("estimate", "a sensible guess")],
    intro=[], examples=[],
    exercise=[
        Ex("Angle between clock hands at…", ("1 o'clock", "30°"), ("3 o'clock", "90°"), ("4 o'clock", "120°"), ("6 o'clock", "180°")),
        Ex("Draw angles you think are 45°, 90° and 135°. Check with a protractor if you have one.", ans="Answers vary.", think=True),
    ],
    check=["Can I estimate angles using 45°, 90°, 135° and 180°?"], look=[], note=NOTE)
