# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u16 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(16, "16.1")]["book"] = BK(
    keys=[("certain", "will happen"), ("possible", "might happen"), ("impossible", "will not happen")],
    intro=[], examples=[],
    exercise=[
        Ex("Will happen, might happen or will not happen?", ("rolling a 4 on a dice", "might happen"), ("a dog reading a book", "will not happen"), ("Monday after Sunday", "will happen")),
        Ex("Write one event for each: will happen, might happen, will not happen.", ans="Answers vary.", think=True),
    ],
    check=["Can I use the language of chance?"], look=[], note=NOTE)

N[(16, "16.2")]["book"] = BK(
    keys=[("experiment", "trying something many times and recording what happens")],
    intro=[], examples=[],
    exercise=[
        Ex("Flip a coin 20 times. Record heads and tails with tallies. What do you notice?", ans="Answers vary – about 10 each.", think=True),
        Ex("A spinner gave red 14 times and blue 6 times. Which part is probably bigger?", ans="red"),
    ],
    check=["Can I carry out a chance experiment and record the results?"], look=[], note=NOTE)
