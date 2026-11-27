# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u05 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(5, "5.1")]["book"] = BK(
    keys=[("multiple", "a number in a times table"), ("factor", "a number that divides exactly")],
    intro=[], examples=[],
    exercise=[
        Ex("List the factors.", ("15", "1, 3, 5, 15"), ("20", "1, 2, 4, 5, 10, 20"), ("36", "1, 2, 3, 4, 6, 9, 12, 18, 36")),
        Ex("Write the first five multiples.", ("7", "7, 14, 21, 28, 35"), ("12", "12, 24, 36, 48, 60")),
    ],
    check=["Can I find multiples and factors?"], look=[], note=NOTE)

N[(5, "5.2")]["book"] = BK(
    keys=[("partition", "split a number into tens and ones")],
    intro=[], examples=[],
    exercise=[
        Ex("Estimate, then work out.", ("34 × 6", "204"), ("58 × 3", "174"), ("76 × 9", "684")),
        Ex("Work out.", ("47 × 10", "470"), ("8 × 100", "800"), ("9 × 50", "450")),
    ],
    check=["Can I multiply 2-digit numbers by 1-digit numbers and by 10 and 100?"], look=[], note=NOTE)
