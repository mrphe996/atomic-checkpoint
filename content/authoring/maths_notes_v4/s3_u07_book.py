# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u07 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(7, "7.1")]["book"] = BK(
    keys=[("tally mark", "a line for each thing counted; the fifth crosses the four")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the number.", ("𝍸 ||", "7"), ("𝍸 𝍸 𝍸", "15"), ("𝍸 𝍸 ||||", "14")),
        Ex("Count the cars that pass your window in 5 minutes using tally marks.", ans="Answers vary.", think=True),
    ],
    check=["Can I record and count tally marks in groups of 5?"], look=[], note=NOTE)

N[(7, "7.2")]["book"] = BK(
    keys=[("frequency", "how many times something happens")],
    intro=[], examples=[],
    exercise=[
        Ex("Pets: cat 9, dog 14, rabbit 3, fish 4.", ("most popular", "dog"), ("total", "30"), ("dog − cat", "5")),
        Ex("Ask 15 people their favourite colour and make a frequency table.", ans="Answers vary.", think=True),
    ],
    check=["Can I complete and read frequency tables?"], look=[], note=NOTE)
