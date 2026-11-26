# -*- coding: utf-8 -*-
"""Stage 7 · Unit 7 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u07 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(7, "7.1")]["book"] = BK(
    keys=[("common denominator", "the same denominator for two or more fractions"), ("improper fraction", "numerator bigger than the denominator, e.g. 9/4"), ("mixed number", "a whole number and a fraction, e.g. 2 1/4")],
    intro=[], examples=[],
    exercise=[
        Ex("Write <, > or =.", ("2/3 ☐ 5/8", ">"), ("3/10 ☐ 1/3", "<"), ("6/9 ☐ 10/15", "=")),
        Ex("Order, smallest first: 5/6, 7/9, 3/4, 2/3", ans="2/3, 3/4, 7/9, 5/6"),
        Ex("Order, largest first: 2 3/8, 19/8, 2 1/3, 12/5", ans="12/5, 2 3/8 = 19/8, 2 1/3"),
        Ex("Find a fraction between 2/5 and 1/2.", ans="For example 9/20."),
        Ex("Three runners finished 4/5, 7/9 and 11/14 of a course. Who ran furthest?", ans="4/5 (0.8 > 0.786 > 0.778)"),
        Ex("Write five different fractions that lie between 0 and 1/10.", ans="For example 1/11, 1/20, 1/50, 2/25, 3/40.", think=True),
    ],
    check=["Can I use a common denominator to compare fractions?", "Can I compare mixed numbers and improper fractions?", "Can I find a fraction between two others?"], look=[], note=NOTE)

N[(7, "7.2")]["book"] = BK(
    keys=[("mixed number", "a whole number and a fraction"), ("simplest form", "numerator and denominator have no common factor other than 1")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out. Simplify.", ("1 1/3 + 2 1/2", "3 5/6"), ("3 3/4 + 1 5/8", "5 3/8"), ("2 4/5 + 3 1/2", "6 3/10")),
        Ex("Work out.", ("5 5/6 − 2 1/3", "3 1/2"), ("4 1/5 − 1 1/2", "2 7/10"), ("6 − 3 3/8", "2 5/8")),
        Ex("A bag of flour weighs 2 1/2 kg. 3/4 kg and 1 1/8 kg are used. How much is left?", ans="5/8 kg"),
        Ex("Find the missing number: 2 2/3 + ☐ = 5 1/4", ans="2 7/12"),
        Ex("Write two mixed numbers with different denominators that add to exactly 5.", ans="For example 2 1/3 + 2 2/3 or 1 1/4 + 3 3/4.", think=True),
    ],
    check=["Can I add and subtract fractions with different denominators?", "Can I add and subtract mixed numbers?", "Can I estimate the answer first?"], look=[], note=NOTE)

N[(7, "7.3")]["book"] = BK(
    keys=[("cancel", "divide a numerator and a denominator by a common factor"), ("product", "the answer to a multiplication")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out. Simplify.", ("2/3 × 5/7", "10/21"), ("3/8 × 4/9", "1/6"), ("5/12 × 9/10", "3/8")),
        Ex("Work out.", ("4 × 3/10", "1 1/5"), ("9 × 5/6", "7 1/2")),
        Ex("Find.", ("5/9 of 108", "60"), ("3/4 of 2/5", "3/10")),
        Ex("A field is 5/8 grass. 2/5 of the grass is used for football. What fraction of the field is that?", ans="1/4"),
        Ex("Is it true that multiplying by a fraction always makes a number smaller? Explain.", ans="Only for proper fractions; × 3/2 makes it bigger.", think=True),
    ],
    check=["Can I multiply two fractions?", "Can I cancel before multiplying?", "Can I find a fraction of a fraction?"], look=[], note=NOTE)

N[(7, "7.4")]["book"] = BK(
    keys=[("reciprocal", "a fraction turned upside down: the reciprocal of 2/3 is 3/2"), ("divisor", "the number you divide by")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("4/5 ÷ 4", "1/5"), ("6/7 ÷ 3", "2/7"), ("3/8 ÷ 6", "1/16")),
        Ex("Work out.", ("2/3 ÷ 1/6", "4"), ("3/4 ÷ 3/8", "2"), ("5/6 ÷ 2/3", "1 1/4")),
        Ex("How many 1/4 hour lessons fit into 2 1/2 hours?", ans="10"),
        Ex("A 3/4 kg bag of nuts is shared equally into 5 bowls. How much in each?", ans="3/20 kg"),
        Ex("Explain why dividing by 1/2 doubles a number.", ans="There are 2 halves in every whole, so n ÷ 1/2 = 2n.", think=True),
    ],
    check=["Can I divide a fraction by a whole number?", "Can I divide by a fraction using the reciprocal?", "Can I check the size of my answer?"], look=[], note=NOTE)

N[(7, "7.5")]["book"] = BK(
    keys=[("factor", "a number that divides exactly into another"), ("order of operations", "brackets, powers, × and ÷, then + and −")],
    intro=[], examples=[],
    exercise=[
        Ex("Use 'whole − small part'.", ("7/8 of 320", "280"), ("9/10 of 650", "585"), ("11/12 of 480", "440")),
        Ex("Split the denominator.", ("1/12 of 2400", "200"), ("1/16 of 800", "50")),
        Ex("Cancel first.", ("21/40 × 16/35", "6/25"), ("27/32 × 8/45", "3/20")),
        Ex("Work out.", ("1/2 + 1/4 × 2/3", "2/3"), ("(2/3 − 1/6) × 4/5", "2/5")),
        Ex("Show two different easy ways to work out 5/6 of 3600.", ans="3600 − 600 = 3000, or 3600 ÷ 6 × 5 = 3000.", think=True),
    ],
    check=["Can I choose an easy method for a fraction calculation?", "Can I cancel before multiplying?", "Can I use the order of operations with fractions?"], look=[], note=NOTE)
