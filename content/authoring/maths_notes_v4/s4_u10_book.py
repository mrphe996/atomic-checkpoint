# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u10 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(10, "10.1")]["book"] = BK(
    keys=[("survey", "asking people a question to collect data"), ("frequency", "how many times something happens")],
    intro=[], examples=[],
    exercise=[
        Ex("Write as tallies.", ("6", "𝍸 |"), ("13", "𝍸 𝍸 |||"), ("20", "𝍸 𝍸 𝍸 𝍸")),
        Ex("Plan and carry out a survey of 20 people about their favourite season. Record with tallies.", ans="Answers vary.", think=True),
    ],
    check=["Can I plan a survey and record data in a tally chart?"], look=[], note=NOTE)

N[(10, "10.2")]["book"] = BK(
    keys=[("Venn diagram", "overlapping circles for sorting"), ("Carroll diagram", "a grid that sorts with 'rule' and 'not rule'")],
    intro=[], examples=[],
    exercise=[
        Ex("Sort into a Venn diagram (odd / more than 10): where does each go?", ("13", "overlap"), ("7", "odd only"), ("14", "more than 10 only"), ("8", "outside")),
        Ex("Draw a Carroll diagram for 'has wheels / not' and 'has an engine / not'. Sort: bicycle, car, boat, horse.", ans="bicycle: wheels, no engine; car: wheels, engine; boat: no wheels, engine; horse: neither"),
    ],
    check=["Can I sort data in Venn and Carroll diagrams?"], look=[], note=NOTE)
