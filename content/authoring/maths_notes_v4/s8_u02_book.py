# -*- coding: utf-8 -*-
"""Stage 8 · Unit 2 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u02 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(2, "2.1")]["book"] = BK(
    keys=[("coefficient", "the number multiplying a letter, e.g. 5 in 5x²"), ("constant", "a number on its own"), ("linear expression", "no power of the letter above 1"), ("equivalent", "equal for every value of the letter")],
    intro=[], examples=[],
    exercise=[
        Ex("Write an expression.", ("square y, then add 8", "y² + 8"), ("add 8 to y, then square", "(y + 8)²"), ("half the product of m and n", "mn/2")),
        Ex("Shirts cost $s and ties cost $4 less. Write the cost of 3 shirts and 2 ties, simplified.", ans="5s − 8"),
        Ex("Which of these are linear? 4x − 1, x², 7, 3/x, (x + 2)/5", ans="4x − 1, 7 and (x + 2)/5"),
        Ex("Write two different expressions that are equivalent to 6n + 12.", ans="For example 6(n + 2), 2(3n + 6), 3(2n + 4).", think=True),
    ],
    check=["Can I write expressions from words and situations?", "Do I know the words term, coefficient, constant, linear?"], look=[], note=NOTE)

N[(2, "2.2")]["book"] = BK(
    keys=[("formula", "a rule linking variables, with an equals sign"), ("subject", "the variable on its own, e.g. v in v = u + at"), ("derive", "work out a formula from a situation")],
    intro=[], examples=[],
    exercise=[
        Ex("Substitute a = −3, b = 4.", ("a² + 2b", "17"), ("5a − b²", "−31"), ("(a + b)³", "1")),
        Ex("Make x the subject.", ("y = x − 12", "x = y + 12"), ("y = 4x + 3", "x = (y − 3)/4"), ("p = x/5 − 2", "x = 5(p + 2)")),
        Ex("A delivery firm charges $6 plus $0.50 per km. Write a formula for the cost C for d km and find d when C = 21.", ans="C = 6 + 0.5d; d = 30"),
        Ex("Make up a formula from your own life (e.g. bus fares) and rearrange it.", ans="Your own formula.", think=True),
    ],
    check=["Can I substitute negative numbers?", "Can I derive a formula?", "Can I change the subject?"], look=[], note=NOTE)

N[(2, "2.3")]["book"] = BK(
    keys=[("expand", "multiply out the brackets"), ("simplify", "collect like terms")],
    intro=[], examples=[],
    exercise=[
        Ex("Expand.", ("7(2a − 3)", "14a − 21"), ("y(y + 8)", "y² + 8y"), ("−3(4 − 5x)", "−12 + 15x"), ("2p(3p − q)", "6p² − 2pq")),
        Ex("Expand and simplify.", ("4(x + 2) − 3(x − 1)", "x + 11"), ("x(x − 3) + 2(x + 5)", "x² − x + 10"), ("5(2y − 1) − (y + 4)", "9y − 9")),
        Ex("Show that 2(n + 5) + 3(n − 1) − 5n always equals 7.", ans="2n + 10 + 3n − 3 − 5n = 7"),
    ],
    check=["Can I expand with letters and negatives outside?", "Can I expand two brackets and simplify?"], look=[], note=NOTE)

N[(2, "2.4")]["book"] = BK(
    keys=[("factorise", "write as a product, taking out the HCF"), ("fully factorised", "no common factor left inside the bracket")],
    intro=[], examples=[],
    exercise=[
        Ex("Factorise fully.", ("9x + 12", "3(3x + 4)"), ("20y − 30", "10(2y − 3)"), ("t² + 11t", "t(t + 11)"), ("6ab − 9b", "3b(2a − 3)"), ("8m² + 12m", "4m(2m + 3)")),
        Ex("Check your answers to Question 1 by expanding.", ans="Each expands back to the original."),
        Ex("Use factorising to work out 23 × 64 + 23 × 36.", ans="23 × 100 = 2300"),
        Ex("Show that the sum of any 4 consecutive even numbers is a multiple of 4.", ans="2n + (2n + 2) + (2n + 4) + (2n + 6) = 8n + 12 = 4(2n + 3)", think=True),
    ],
    check=["Can I find the HCF of algebraic terms?", "Can I factorise fully and check by expanding?"], look=[], note=NOTE)

N[(2, "2.5")]["book"] = BK(
    keys=[("equation", "two expressions that are equal"), ("construct", "write an equation from a situation")],
    intro=[], examples=[],
    exercise=[
        Ex("Solve.", ("6x + 5 = 2x + 25", "x = 5"), ("3(y − 4) = y + 6", "y = 9"), ("4(2a + 1) = 5(a + 5)", "a = 7"), ("12 − x = 2x + 27", "x = −5")),
        Ex("The sides of an equilateral triangle are 3x + 2, 5x − 6 and 2x + 6. Find x and the perimeter.", ans="x = 4; perimeter 42"),
        Ex("Taxi A: $5 + $2 per km. Taxi B: $2 + $2.50 per km. After how many km do they cost the same?", ans="6 km"),
        Ex("Write an equation with x on both sides whose solution is x = −2.", ans="For example 3x + 5 = x + 1.", think=True),
    ],
    check=["Can I solve equations with brackets?", "Can I solve equations with the unknown on both sides?", "Can I construct equations from problems?"], look=[], note=NOTE)

N[(2, "2.6")]["book"] = BK(
    keys=[("≤, ≥", "less/greater than or equal to: closed circle"), ("<, >", "less/greater than: open circle"), ("interval", "the numbers between two boundaries")],
    intro=[], examples=[],
    exercise=[
        Ex("Write an inequality.", ("at least 18", "x ≥ 18"), ("under 12", "x < 12"), ("between 5 and 10 inclusive", "5 ≤ x ≤ 10")),
        Ex("Draw on a number line.", ("x ≥ −1", "closed at −1, right"), ("−3 < x ≤ 2", "open at −3, closed at 2")),
        Ex("Solve.", ("2x + 5 > 17", "x > 6"), ("4(x − 1) ≤ 20", "x ≤ 6")),
        Ex("List the integers.", ("−2 ≤ n < 3", "−2, −1, 0, 1, 2"), ("9 < 3n ≤ 21", "4, 5, 6, 7")),
        Ex("Write an inequality whose integer solutions are exactly −3, −2, −1.", ans="For example −3 ≤ x < 0.", think=True),
    ],
    check=["Can I use ≤ and ≥ with closed circles?", "Can I write and draw intervals?", "Can I solve inequalities?"], look=[], note=NOTE)
