# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s3_u10 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(10, "10.1")]["book"] = BK(
    keys=[("fact family", "four facts made from the same three numbers")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("7 × 3", "21"), ("6 × 8", "48"), ("45 ÷ 9", "5"), ("32 ÷ 4", "8")),
        Ex("Write the fact family for 5 × 6 = 30.", ans="5 × 6, 6 × 5, 30 ÷ 5 = 6, 30 ÷ 6 = 5"),
    ],
    check=["Can I recall and use multiplication and division facts?"], look=[], note=NOTE)

N[(10, "10.2")]["book"] = BK(
    keys=[("odd", "has 1 left over when paired"), ("even", "can be split into pairs")],
    intro=[], examples=[],
    exercise=[
        Ex("Odd or even?", ("58", "even"), ("143", "odd"), ("700", "even")),
        Ex("Multiple of 5? Multiple of 10?", ("65", "5 yes, 10 no"), ("120", "both yes")),
    ],
    check=["Can I recognise odd and even numbers and patterns in multiples?"], look=[], note=NOTE)

N[(10, "10.3")]["book"] = BK(
    keys=[("partition", "split a number into tens and ones")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("24 × 10", "240"), ("31 × 4", "124"), ("26 × 3", "78"), ("17 × 5", "85")),
    ],
    check=["Can I multiply by 10 and multiply 2-digit numbers by 1-digit numbers?"], look=[], note=NOTE)
