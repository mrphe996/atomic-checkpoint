# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s6_u02 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(2, "2.1")]["book"] = BK(
    keys=[("term-to-term rule", "how to get from one term to the next"), ("position-to-term rule", "how to get a term from its position")],
    intro=[], examples=[],
    exercise=[
        Ex("Continue for three more terms.", ("1.2, 1.5, 1.8", "2.1, 2.4, 2.7"), ("4, 3¾, 3½", "3¼, 3, 2¾")),
        Ex("Find the rule and the 20th term: 7, 11, 15, 19, …", ans="4 × position + 3; 83"),
    ],
    check=["Can I count in fractions and decimals?", "Can I use position-to-term rules?"], look=[], note=NOTE)

N[(2, "2.2")]["book"] = BK(
    keys=[("square number", "n × n, written n²"), ("cube number", "n × n × n, written n³")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("7²", "49"), ("12²", "144"), ("3³", "27"), ("10³", "1000")),
        Ex("Find two square numbers that add to 100.", ans="36 + 64"),
    ],
    check=["Do I know my square and cube numbers?"], look=[], note=NOTE)

N[(2, "2.3")]["book"] = BK(
    keys=[("common multiple", "a number in both times tables"), ("common factor", "a number that divides into both exactly")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the lowest common multiple.", ("4 and 6", "12"), ("5 and 8", "40")),
        Ex("Find the highest common factor.", ("18 and 24", "6"), ("16 and 40", "8")),
        Ex("Cakes come in boxes of 6 and plates hold 8. Smallest number of cakes that fills whole boxes and whole plates?", ans="24"),
    ],
    check=["Can I find common multiples and common factors?"], look=[], note=NOTE)
