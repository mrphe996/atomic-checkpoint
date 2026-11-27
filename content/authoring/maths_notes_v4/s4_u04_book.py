# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u04 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(4, "4.1")]["book"] = BK(
    keys=[("impossible", "can never happen"), ("certain", "must happen"), ("even chance", "as likely as not")],
    intro=[], examples=[],
    exercise=[
        Ex("Choose a word: impossible, unlikely, even chance, likely or certain.", ("rolling a 3 on a 1–6 dice", "unlikely"), ("a coin landing heads", "even chance"), ("picking a red counter from a bag of only red", "certain"), ("rolling a 10 on a 1–6 dice", "impossible")),
        Ex("Write one event for each word on the likelihood scale.", ans="Answers vary.", think=True),
    ],
    check=["Can I use the language of chance?"], look=[], note=NOTE)

N[(4, "4.2")]["book"] = BK(
    keys=[("equally likely", "having the same chance"), ("tally", "marks in groups of 5 to count results")],
    intro=[], examples=[],
    exercise=[
        Ex("Flip a coin 30 times. Record heads and tails with tallies. Are they equally likely?", ans="Answers vary – about 15 each.", think=True),
        Ex("A spinner gave: red 40, blue 10. Is it likely that the colours have equal sections?", ans="No – red is probably much bigger."),
    ],
    check=["Can I carry out a chance experiment and decide if outcomes are equally likely?"], look=[], note=NOTE)
