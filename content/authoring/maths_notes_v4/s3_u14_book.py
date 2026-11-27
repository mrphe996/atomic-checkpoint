# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u14 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(14, "14.1")]["book"] = BK(
    keys=[("right angle", "a quarter turn"), ("clockwise", "the way clock hands turn")],
    intro=[], examples=[],
    exercise=[
        Ex("Name the turn.", ("minute hand 12 to 3", "quarter turn"), ("12 to 6", "half turn"), ("12 to 9", "three-quarter turn")),
        Ex("Find three right angles in your room with a paper checker.", ans="Answers vary.", think=True),
    ],
    check=["Can I describe turns and compare angles with a right angle?"], look=[], note=NOTE)

N[(14, "14.2")]["book"] = BK(
    keys=[("compass directions", "north, east, south, west")],
    intro=[], examples=[],
    exercise=[
        Ex("Where do you end up?", ("(2, 1) then 3 north", "(2, 4)"), ("(5, 3) then 4 west", "(1, 3)"), ("(0, 0) then 2 east, 2 north", "(2, 2)")),
        Ex("Draw a grid map of your street or school and write directions from one place to another.", ans="Answers vary.", think=True),
    ],
    check=["Can I use compass directions and describe position and movement on a grid?"], look=[], note=NOTE)
