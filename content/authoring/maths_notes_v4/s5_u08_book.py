# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u08 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(8, "8.1")]["book"] = BK(
    keys=[("likelihood", "how likely something is to happen"), ("equally likely", "having the same chance")],
    intro=[], examples=[],
    exercise=[
        Ex("Choose impossible, unlikely, even chance, likely or certain.", ("rolling a 5 on a 1–6 dice", "unlikely"), ("a coin landing tails", "even chance"), ("picking a red counter from 9 red and 1 blue", "likely"), ("rolling a 9 on a 1–6 dice", "impossible")),
        Ex("Design a spinner with 8 equal parts where green is unlikely but possible.", ans="Answers vary, e.g. 2 green and 6 other colours.", think=True),
    ],
    check=["Can I use the language of chance?", "Can I tell when outcomes are equally likely?"], look=[], note=NOTE)

N[(8, "8.2")]["book"] = BK(
    keys=[("trial", "one try in an experiment"), ("simulation", "acting out a real event with a coin, dice or spinner")],
    intro=[], examples=[],
    exercise=[
        Ex("Predict.", ("a fair coin, 60 flips: heads", "about 30"), ("a fair 1–6 dice, 36 rolls: 3s", "about 6"), ("a spinner ¼ blue, 100 spins: blue", "about 25")),
        Ex("Flip a coin 30 times and record the results in a tally chart. Compare with your prediction.", ans="Answers vary – about 15 heads.", think=True),
    ],
    check=["Can I carry out an experiment and compare the results with a prediction?"], look=[], note=NOTE)
