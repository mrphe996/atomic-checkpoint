# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u13 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(13, "13.1")]["book"] = BK(
    keys=[("protractor", "a tool for measuring and drawing angles"), ("reflex angle", "an angle between 180° and 360°")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw these angles with a protractor.", ("65°", "acute"), ("140°", "obtuse"), ("235°", "draw 125°, mark the reflex angle")),
        Ex("Find the missing angle.", ("on a line with 72°", "108°"), ("around a point with 150° and 95°", "115°")),
    ],
    check=["Can I measure and draw angles accurately?"], look=[], note=NOTE)

N[(13, "13.2")]["book"] = BK(
    keys=[("angle sum of a triangle", "180°")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the missing angle.", ("54° and 81°", "45°"), ("right-angled with 38°", "52°"), ("isosceles with top angle 44°", "68° each")),
        Ex("Draw three different triangles, measure their angles and add them. What do you notice?", ans="Each total is about 180°.", think=True),
    ],
    check=["Can I find missing angles in triangles?"], look=[], note=NOTE)
