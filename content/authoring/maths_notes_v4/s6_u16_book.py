# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u16 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(16, "16.1")]["book"] = BK(
    keys=[("commutative", "order can be swapped for + and ×"), ("associative", "grouping can change for + and ×"), ("distributive", "a × (b + c) = a × b + a × c")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out the easy way.", ("2 × 63 × 5", "630"), ("38 + 47 + 62", "147"), ("9 × 48", "432"), ("6 × 27 + 6 × 73", "600")),
        Ex("Work out.", ("4 + 6 × 3", "22"), ("(4 + 6) × 3", "30")),
    ],
    check=["Can I use the laws of arithmetic and the order of operations?"], look=[], note=NOTE)
