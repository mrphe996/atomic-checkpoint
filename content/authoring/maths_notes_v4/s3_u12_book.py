# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u12 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(12, "12.1")]["book"] = BK(
    keys=[("mass", "how heavy something is"), ("g / kg", "1000 g = 1 kg")],
    intro=[], examples=[],
    exercise=[
        Ex("Convert.", ("4 kg to g", "4000 g"), ("6000 g to kg", "6 kg"), ("1 kg 500 g to g", "1500 g")),
        Ex("Weigh three things at home with kitchen scales and write their masses.", ans="Answers vary.", think=True),
    ],
    check=["Can I measure mass in g and kg and read scales?"], look=[], note=NOTE)

N[(12, "12.2")]["book"] = BK(
    keys=[("capacity", "how much a container holds"), ("ml / l", "1000 ml = 1 l")],
    intro=[], examples=[],
    exercise=[
        Ex("Convert.", ("2 l to ml", "2000 ml"), ("5000 ml to l", "5 l"), ("1 l 250 ml to ml", "1250 ml")),
        Ex("How many 250 ml cups fill a 3 l jug?", ans="12"),
    ],
    check=["Can I measure capacity in ml and l?"], look=[], note=NOTE)

N[(12, "12.3")]["book"] = BK(
    keys=[("°C", "degrees Celsius")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the new temperature.", ("14 °C rises 6 degrees", "20 °C"), ("28 °C falls 9 degrees", "19 °C")),
        Ex("Check the temperature outside each morning for a week and record it.", ans="Answers vary.", think=True),
    ],
    check=["Can I read a thermometer in °C?"], look=[], note=NOTE)
