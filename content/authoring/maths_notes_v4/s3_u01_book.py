# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u01 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(1, "1.1")]["book"] = BK(
    keys=[("hundreds, tens, ones", "the places in a 3-digit number"), ("partition", "split a number into parts")],
    intro=[], examples=[],
    exercise=[
        Ex("Partition.", ("536", "500 + 30 + 6"), ("804", "800 + 4"), ("270", "200 + 70")),
        Ex("Write in digits.", ("four hundred and sixty-one", "461"), ("nine hundred and six", "906")),
    ],
    check=["Can I read, write and partition 3-digit numbers?"], look=[], note=NOTE)

N[(1, "1.2")]["book"] = BK(
    keys=[("< / >", "less than / greater than")],
    intro=[], examples=[],
    exercise=[
        Ex("Write <, > or =.", ("365 ☐ 356", ">"), ("208 ☐ 280", "<"), ("400 + 9 ☐ 409", "=")),
        Ex("Order from smallest: 712, 127, 271, 172.", ans="127, 172, 271, 712"),
    ],
    check=["Can I compare and order numbers to 1000?"], look=[], note=NOTE)

N[(1, "1.3")]["book"] = BK(
    keys=[("round", "change to the nearest 10 or 100"), ("estimate", "a sensible guess")],
    intro=[], examples=[],
    exercise=[
        Ex("Round to the nearest 10.", ("46", "50"), ("213", "210"), ("385", "390")),
        Ex("Round to the nearest 100.", ("172", "200"), ("639", "600"), ("850", "900")),
    ],
    check=["Can I round to the nearest 10 and 100?"], look=[], note=NOTE)
