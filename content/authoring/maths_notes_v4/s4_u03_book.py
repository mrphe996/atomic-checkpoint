# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s4_u03 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(3, "3.1")]["book"] = BK(
    keys=[("inverse", "the opposite operation: + and − undo each other")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the missing number.", ("☐ + 28 = 61", "33"), ("72 − ☐ = 39", "33"), ("☐ − 55 = 45", "100")),
        Ex("Write + or −.", ("48 ○ 12 = 36", "−"), ("27 ○ 33 = 60", "+")),
    ],
    check=["Can I use a symbol for a missing number or operation?"], look=[], note=NOTE)

N[(3, "3.2")]["book"] = BK(
    keys=[("carry", "move a ten or hundred to the next column when adding"), ("exchange", "change 1 ten for 10 ones when subtracting")],
    intro=[], examples=[],
    exercise=[
        Ex("Estimate, then work out.", ("356 + 278", "634"), ("509 + 196", "705"), ("821 − 457", "364"), ("600 − 238", "362")),
        Ex("A farmer has 625 sheep and sells 248. How many are left?", ans="377"),
    ],
    check=["Can I add and subtract 3-digit numbers and check my answers?"], look=[], note=NOTE)

N[(3, "3.3")]["book"] = BK(
    keys=[("generalisation", "a rule that is always true"), ("counter-example", "one example that shows a rule is false")],
    intro=[], examples=[],
    exercise=[
        Ex("Odd or even?", ("147 + 362", "odd"), ("519 + 233", "even"), ("700 − 285", "odd"), ("64 − 18", "even")),
        Ex("Test the rule 'odd − odd = even' with three examples of your own.", ans="Answers vary – all even.", think=True),
    ],
    check=["Can I use odd and even rules to predict and check answers?"], look=[], note=NOTE)
