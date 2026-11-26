# -*- coding: utf-8 -*-
"""Stage 7 · Unit 1 – Words to know, Practice on paper and checklists for the lesson documents (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u01 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(1, "1.1")]["book"] = BK(
    keys=[("integer", "a whole number: positive, negative or zero"), ("negative number", "a number less than zero"), ("number line", "a line showing numbers in order"), ("difference", "how far apart two numbers are")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("−7 + 10", "3"), ("2 − 9", "−7"), ("−5 + (−6)", "−11"), ("8 − (−3)", "11"), ("−4 − (−4)", "0")),
        Ex("A freezer is at −18 °C. During a power cut it warms by 11 degrees. What temperature is it now?", ans="−7 °C"),
        Ex("Copy and complete: each number is the sum of the two numbers below it.", ("bottom row −3, 5, −8: middle row?", "2, −3"), ("top number?", "−1")),
        Ex("Find the missing numbers.", ("☐ + 7 = −2", "−9"), ("4 − ☐ = 9", "−5"), ("−6 − ☐ = −1", "−5")),
        Ex("Odd one out: which calculation does NOT equal −4?", ans="(c) 2 − (−6) = 8", *[("−9 + 5", ""), ("1 − 5", ""), ("2 − (−6)", ""), ("−1 + (−3)", "")]),
        Ex("Write three different calculations, each using one negative number, that have the answer −10.", ans="For example −12 + 2, −4 − 6, 5 − 15.", think=True),
        Ex("The lowest temperature ever recorded in a city is −23 °C and the highest is 41 °C. What is the range?", ans="41 − (−23) = 64 degrees"),
    ],
    check=["Can I add and subtract with negative numbers?", "Can I explain why subtracting a negative is like adding?", "Can I find the difference between two temperatures?"], look=[], note=NOTE)

N[(1, "1.2")]["book"] = BK(
    keys=[("product", "the answer to a multiplication"), ("inverse operation", "the operation that undoes another: ÷ undoes ×")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("7 × (−3)", "−21"), ("(−8) × 4", "−32"), ("−45 ÷ 9", "−5"), ("−60 ÷ 12", "−5")),
        Ex("Find the missing numbers.", ("4 × ☐ = −28", "−7"), ("☐ ÷ 3 = −9", "−27"), ("−36 ÷ ☐ = −6", "6")),
        Ex("Complete the grid: rows 5 and −2, columns 3 and 6.", ("row 5", "15, 30"), ("row −2", "−6, −12")),
        Ex("Work out. Do the brackets first.", ("3 × (−4 + 1)", "−9"), ("(2 − 8) × 5", "−30"), ("−20 ÷ (1 + 4)", "−4")),
        Ex("Estimate by rounding to whole numbers.", ("−6.9 × 3.1", "about −21"), ("−39.8 ÷ 4.2", "about −10")),
        Ex("Find all the pairs of integers (one positive, one negative) whose product is −18.", ans="1 & −18, 2 & −9, 3 & −6, 6 & −3, 9 & −2, 18 & −1", think=True, tip="Start with the factor pairs of 18."),
        Ex("A shop's profit changes by −$15 each day for 6 days. What is the total change?", ans="−$90"),
    ],
    check=["Can I multiply a negative number by a positive number?", "Can I divide a negative number by a positive number?", "Can I check with the inverse operation?"], look=[], note=NOTE)

N[(1, "1.3")]["book"] = BK(
    keys=[("multiple", "a number in a times table"), ("common multiple", "a multiple of two or more numbers"), ("lowest common multiple (LCM)", "the smallest common multiple")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the LCM.", ("3 and 7", "21"), ("6 and 9", "18"), ("8 and 20", "40"), ("12 and 15", "60")),
        Ex("Find the LCM of three numbers.", ("2, 3 and 5", "30"), ("4, 6 and 8", "24")),
        Ex("Cups come in packs of 12 and plates in packs of 8. What is the smallest number of each you can buy to have the same number of cups and plates?", ans="24 (2 packs of cups, 3 packs of plates)"),
        Ex("Two alarms ring every 15 minutes and every 20 minutes. They ring together at 7:00. When do they next ring together?", ans="8:00"),
        Ex("Which numbers below 50 have an LCM of 30 with 6?", ans="5, 10, 15, 30"),
        Ex("Is the LCM of two numbers always their product? Give an example where it is, and one where it is not.", ans="No. 4 and 5 → 20 (the product); 4 and 6 → 12 (not 24).", think=True),
    ],
    check=["Can I list multiples and spot common ones?", "Can I find the LCM of two or three numbers?", "Can I use the LCM to solve 'together again' problems?"], look=[], note=NOTE)

N[(1, "1.4")]["book"] = BK(
    keys=[("factor", "a number that divides exactly into another"), ("common factor", "a factor of two or more numbers"), ("highest common factor (HCF)", "the largest common factor")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the HCF.", ("12 and 20", "4"), ("18 and 27", "9"), ("16 and 25", "1"), ("48 and 72", "24")),
        Ex("Find the HCF of three numbers.", ("12, 18 and 24", "6"), ("20, 50 and 70", "10")),
        Ex("A florist has 36 roses and 54 tulips. She makes identical bunches with none left over. What is the greatest number of bunches?", ans="18 (2 roses and 3 tulips each)"),
        Ex("A wall 210 cm by 150 cm is covered with equal square tiles, as large as possible. What size are the tiles?", ans="30 cm"),
        Ex("The HCF of 24 and a number is 8. The number is less than 50. What could it be?", ans="8, 16 or 40"),
        Ex("HCF or LCM? (a) the largest equal groups (b) the next time two events happen together. Explain.", ans="(a) HCF – a factor of both. (b) LCM – a multiple of both.", think=True),
    ],
    check=["Can I list factors in pairs?", "Can I find the HCF of two or three numbers?", "Can I decide when a problem needs the HCF or the LCM?"], look=[], note=NOTE)

N[(1, "1.5")]["book"] = BK(
    keys=[("divisible", "divides with no remainder"), ("digit sum", "the total of the digits of a number"), ("test for divisibility", "a quick check without dividing")],
    intro=[], examples=[],
    exercise=[
        Ex("Is 6 840 divisible by: (a) 4 (b) 8 (c) 9 (d) 25?", ans="(a) yes (b) yes (c) yes (d) no"),
        Ex("Find the missing digit so that the number is divisible by 9.", ("23☐", "4"), ("☐56", "7"), ("4☐02", "2")),
        Ex("Sort these numbers: 375, 1 200, 2 550, 4 105 into 'divisible by 25' and 'not divisible by 25'.", ans="Divisible: 375, 1 200, 2 550. Not: 4 105."),
        Ex("A number is divisible by 6 and by 4. Is it always divisible by 24? Test 12, 36 and 48.", ans="No: 12 and 36 are not divisible by 24 (48 is).", think=True),
        Ex("Write the largest four-digit number divisible by both 5 and 9.", ans="9 990"),
        Ex("Make up a five-digit number that is divisible by 2, 3, 4, 5, 6, 8, 9 and 10. Explain how you built it.", ans="For example 72 000: ends in 000 (2, 4, 5, 8, 10) and digit sum 9 (3, 6, 9).", think=True),
    ],
    check=["Can I use the tests for 2, 3, 4, 5, 6, 8, 9, 10 and 25?", "Can I find missing digits using a test?"], look=[], note=NOTE)

N[(1, "1.6")]["book"] = BK(
    keys=[("square number", "n × n, written n²"), ("cube number", "n × n × n, written n³"), ("square root (√)", "the number that squared gives the starting number"),
          ("cube root (∛)", "the number that cubed gives the starting number"), ("index", "the small number that shows the power")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out.", ("13²", "169"), ("18²", "324"), ("2³", "8"), ("5³", "125")),
        Ex("Find.", ("√256", "16"), ("√324", "18"), ("∛27", "3"), ("∛125", "5")),
        Ex("Write each fact as a root statement.", ("19² = 361", "√361 = 19"), ("4³ = 64", "∛64 = 4")),
        Ex("Which integer is closest to each root?", ("√30", "5"), ("√110", "10"), ("√300", "17")),
        Ex("Work out √225 − ∛64 + 3².", ans="15 − 4 + 9 = 20"),
        Ex("A square field has an area of 3 600 m². How much fence goes round it?", ans="Side 60 m; fence 240 m"),
        Ex("Find a number between 1 and 100 that is both a square number and a cube number, other than 1.", ans="64", think=True),
    ],
    check=["Can I recall squares to 20² and cubes to 5³?", "Can I find square roots and cube roots?", "Can I estimate a square root between two integers?"], look=[], note=NOTE)
