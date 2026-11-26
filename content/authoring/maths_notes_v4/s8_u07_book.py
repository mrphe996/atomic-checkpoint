# -*- coding: utf-8 -*-
"""Stage 8 · Unit 7 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u07 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(7, "7.1")]["book"] = BK(
    keys=[("terminating decimal", "a decimal that ends"), ("recurring decimal", "a decimal with digits that repeat forever, shown with dots")],
    intro=[], examples=[],
    exercise=[
        Ex("Write as a decimal.", ("5/8", "0.625"), ("4/9", "0.4̇"), ("7/12", "0.583̇"), ("3/11", "0.2̇7̇")),
        Ex("Terminating or recurring? Explain using prime factors.", ("13/40", "terminating – 40 = 2³ × 5"), ("5/18", "recurring – 18 has a 3"), ("14/35", "terminating – 2/5")),
        Ex("Order: 0.45, 0.4̇5̇, 0.45̇, 4/9", ans="4/9 = 0.444…, 0.45, 0.4545…, 0.4555…"),
        Ex("Investigate the decimals of 1/7, 2/7, 3/7. What do you notice?", ans="The same 6 digits 142857 in a different starting place.", think=True),
    ],
    check=["Can I convert fractions to terminating or recurring decimals?", "Can I predict which fractions terminate?"], look=[], note=NOTE)

N[(7, "7.2")]["book"] = BK(
    keys=[("common denominator", "the same denominator for several fractions"), ("negative fraction", "a fraction less than zero")],
    intro=[], examples=[],
    exercise=[
        Ex("Order, smallest first.", ("5/8, 3/5, 7/12", "7/12, 3/5, 5/8"), ("−3/4, −5/7, −0.7", "−3/4, −5/7, −0.7")),
        Ex("Order, largest first: 2 3/8, 19/8, 2.4, 12/5", ans="2.4 = 12/5, 2 3/8 = 19/8 (equal pairs)"),
        Ex("Find a fraction between −5/6 and −4/5.", ans="For example −49/60."),
        Ex("Which method (common denominators or decimals) would you use for 7/13 and 8/15? Why?", ans="Decimals – the common denominator 195 is awkward.", think=True),
    ],
    check=["Can I order positive and negative fractions?", "Can I choose a good method?"], look=[], note=NOTE)

N[(7, "7.3")]["book"] = BK(
    keys=[("regroup", "exchange one whole for fractions, e.g. 5 1/4 = 4 5/4")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("6 3/4 − 2 1/6", "4 7/12"), ("5 1/3 − 2 4/5", "2 8/15"), ("8 − 3 5/9", "4 4/9"), ("2 1/6 − 3 1/2", "−1 1/3")),
        Ex("A tank holds 12 1/2 litres. 4 3/4 litres and 3 2/3 litres are used. How much is left?", ans="4 1/12 litres"),
        Ex("Write a subtraction of two mixed numbers that needs regrouping and has answer 1 3/4.", ans="For example 4 1/4 − 2 1/2.", think=True),
    ],
    check=["Can I subtract mixed numbers, regrouping when needed?"], look=[], note=NOTE)

N[(7, "7.4")]["book"] = BK(
    keys=[("partitioning", "splitting a number into parts, e.g. 2 3/4 = 2 + 3/4")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("5 × 3 2/5", "17"), ("6 × 2 4/9", "14 2/3"), ("9 × 1 7/12", "14 1/4"), ("−4 × 2 3/8", "−9 1/2")),
        Ex("A carpenter cuts 7 pieces of wood, each 1 5/6 m. Total length?", ans="12 5/6 m"),
        Ex("Show that 8 × 2 5/8 = 21 in two different ways.", ans="16 + 5 = 21; 8 × 21/8 = 21.", think=True),
    ],
    check=["Can I multiply an integer by a mixed number by partitioning or improper fractions?"], look=[], note=NOTE)

N[(7, "7.5")]["book"] = BK(
    keys=[("reciprocal", "a fraction turned upside down; n ÷ a/b = n × b/a")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("6 ÷ 1/7", "42"), ("8 ÷ 4/5", "10"), ("5 ÷ 2/3", "7 1/2"), ("12 ÷ 9/10", "13 1/3")),
        Ex("How many 5/8 m ribbons can be cut from 10 m?", ans="16"),
        Ex("A 3 kg bag of sugar is shared into 2/7 kg portions. How many full portions?", ans="10 (10 1/2)"),
        Ex("Explain why dividing by 1/2 doubles a number.", ans="Each whole contains 2 halves.", think=True),
    ],
    check=["Can I divide an integer by a fraction?", "Can I interpret the answer in context?"], look=[], note=NOTE)

N[(7, "7.6")]["book"] = BK(
    keys=[("strategy", "a method chosen to make a calculation easier")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out mentally.", ("2/5 × 13 + 2/5 × 7", "8"), ("9/10 of 380", "342"), ("4/15 × 25/36", "5/27")),
        Ex("Work out.", ("3/4 − 1/2 × 1/3", "7/12"), ("(5/6 − 1/2) ÷ 2/3", "1/2")),
        Ex("Write a calculation with fractions where taking out a common factor makes it easy, and solve it.", ans="Your own example.", think=True),
    ],
    check=["Can I choose a strategy for a fraction calculation?", "Can I use the order of operations with fractions?"], look=[], note=NOTE)
