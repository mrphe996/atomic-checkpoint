# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s5_u05 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(5, "5.1")]["book"] = BK(
    keys=[("decimal point", "separates whole numbers from tenths and hundredths"), ("line up", "write digits of the same place value in the same column")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("3.4 + 2.5", "5.9"), ("6.75 + 1.3", "8.05"), ("9.2 − 4.6", "4.6"), ("10 − 3.45", "6.55")),
        Ex("A bag weighs 2.35 kg and a box weighs 1.8 kg. Find the total mass.", ans="4.15 kg"),
        Ex("Make up a decimal subtraction with the answer 1.25.", ans="Answers vary, e.g. 3.5 − 2.25.", think=True),
    ],
    check=["Can I line up the decimal points?", "Can I add and subtract decimals with different numbers of places?"], look=[], note=NOTE)

N[(5, "5.2")]["book"] = BK(
    keys=[("negative number", "a number less than zero"), ("integer", "a whole number, positive, negative or zero")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("−3 + 5", "2"), ("4 − 7", "−3"), ("−2 − 6", "−8"), ("−9 + 9", "0")),
        Ex("The temperature is −4 °C and rises by 6 degrees. What is the new temperature?", ans="2 °C"),
        Ex("Order from smallest: 3, −5, 0, −1.", ans="−5, −1, 0, 3"),
    ],
    check=["Can I use a number line to add and subtract across zero?"], look=[], note=NOTE)
