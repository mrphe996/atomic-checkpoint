# -*- coding: utf-8 -*-
"""Stage 7 · Unit 2 – Words to know, Practice on paper and checklists for the lesson documents (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u02 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(2, "2.1")]["book"] = BK(
    keys=[("variable", "a letter that stands for an unknown number"), ("term", "a single part of an expression, e.g. 3n"), ("expression", "a collection of terms, e.g. 3n + 2, with no equals sign")],
    intro=[], examples=[],
    exercise=[
        Ex("Write an expression for each.", ("6 more than p", "p + 6"), ("4 less than q", "q − 4"), ("r multiplied by 9", "9r"), ("s divided by 5", "s/5")),
        Ex("A box holds b biscuits. Write an expression for the number of biscuits in", ("3 boxes", "3b"), ("3 boxes with 2 biscuits eaten", "3b − 2")),
        Ex("Write in words.", ("2x + 1", "double x and add 1"), ("(y − 3)/4", "subtract 3 from y, then divide by 4")),
        Ex("Tom is t years old. His aunt is 5 times as old minus 2 years. Write her age.", ans="5t − 2"),
        Ex("Match: 'k add 2, then times 3' and 'k times 3, then add 2'. Write each expression. Are they the same?", ans="3(k + 2) and 3k + 2 – not the same (k = 1 gives 9 and 5).", think=True),
        Ex("Write two different expressions that both equal 12 when n = 4.", ans="For example 3n, n + 8, 4n − 4.", think=True),
    ],
    check=["Can I write an expression from words?", "Can I describe an expression in words?", "Can I tell 3(k + 2) from 3k + 2?"], look=[], note=NOTE)

N[(2, "2.2")]["book"] = BK(
    keys=[("substitute", "replace a letter with a number"), ("formula", "a rule linking quantities, e.g. P = 2l + 2w"), ("evaluate", "work out the value")],
    intro=[], examples=[],
    exercise=[
        Ex("Work out the value when a = 5 and b = −2.", ("a + b", "3"), ("3a − b", "17"), ("ab", "−10"), ("a² + b", "23")),
        Ex("The cost in dollars of hiring a bike is C = 6h + 4, where h is the number of hours.", ("Find C when h = 3", "22"), ("Find h when C = 40", "6")),
        Ex("Use P = 2l + 2w to find the perimeter of a rectangle 7 cm by 4.5 cm.", ans="23 cm"),
        Ex("A phone plan costs $12 a month plus $0.05 per text. Write a formula for the cost T of a month with x texts.", ans="T = 12 + 0.05x"),
        Ex("When n = 3, which is larger: 4n − 5 or n² − 1? Explain.", ans="4n − 5 = 7, n² − 1 = 8, so n² − 1 is larger.", think=True),
    ],
    check=["Can I substitute positive and negative numbers?", "Can I use a formula written in words or letters?", "Can I write my own formula?"], look=[], note=NOTE)

N[(2, "2.3")]["book"] = BK(
    keys=[("like terms", "terms with exactly the same letters, e.g. 4x and −x"), ("simplify", "collect like terms to write an expression more simply")],
    intro=[], examples=[],
    exercise=[
        Ex("Simplify.", ("5m + 3m", "8m"), ("9t − 4t + t", "6t"), ("2a + 7 + 4a − 3", "6a + 4"), ("3x + 2y − x + 5y", "2x + 7y")),
        Ex("Write an expression for the perimeter of a triangle with sides 2k, k + 3 and 4k − 1. Simplify it.", ans="7k + 2"),
        Ex("Find the missing term.", ("6p + ☐ = 10p", "4p"), ("5q − ☐ + 2 = 2q + 2", "3q")),
        Ex("Which pairs are like terms? 3ab, 3a, ba, b², 7b", ans="3ab and ba"),
        Ex("Sam says 4n + 3 simplifies to 7n. Show he is wrong using n = 2.", ans="4 × 2 + 3 = 11 but 7 × 2 = 14.", think=True),
    ],
    check=["Can I spot like terms?", "Can I collect terms, keeping their signs?", "Can I check a simplification with a number?"], look=[], note=NOTE)

N[(2, "2.4")]["book"] = BK(
    keys=[("expand", "multiply out a bracket"), ("bracket", "( ) – groups terms that are worked on together")],
    intro=[], examples=[],
    exercise=[
        Ex("Expand.", ("2(x + 8)", "2x + 16"), ("6(y − 3)", "6y − 18"), ("5(3a + 2)", "15a + 10"), ("n(n + 7)", "n² + 7n")),
        Ex("Expand and simplify.", ("3(k + 4) + 2k", "5k + 12"), ("4(m + 1) + 2(m − 5)", "6m − 6")),
        Ex("A rectangle is 6 cm wide and (2x + 1) cm long. Write its area without brackets.", ans="12x + 6 cm²"),
        Ex("Use a bracket to work out 8 × 205 in your head.", ans="8(200 + 5) = 1600 + 40 = 1640"),
        Ex("Fill in the gaps: ☐(x + 5) = 3x + ☐", ans="3 and 15"),
        Ex("Find two different expressions with brackets that expand to 12y + 8.", ans="For example 4(3y + 2) and 2(6y + 4).", think=True),
    ],
    check=["Can I multiply every term in a bracket?", "Can I keep the signs correct?", "Can I expand two brackets and collect like terms?"], look=[], note=NOTE)

N[(2, "2.5")]["book"] = BK(
    keys=[("equation", "a statement that two expressions are equal"), ("solve", "find the value of the letter that makes the equation true"), ("solution", "the value that makes the equation true")],
    intro=[], examples=[],
    exercise=[
        Ex("Solve.", ("x + 14 = 30", "16"), ("y − 6 = 2", "8"), ("7z = 63", "9"), ("w/4 = 11", "44")),
        Ex("Solve. Show each step.", ("3a + 2 = 20", "6"), ("5b − 9 = 26", "7"), ("c/2 + 7 = 12", "10"), ("4(d − 1) = 28", "8")),
        Ex("I think of a number, multiply it by 6 and add 5. The answer is 47. Write an equation and solve it.", ans="6n + 5 = 47, n = 7"),
        Ex("A plumber charges $30 call-out plus $25 per hour. A job cost $130. How many hours?", ans="25h + 30 = 130, h = 4"),
        Ex("The angles on a straight line are 2x and x + 30. Find x.", ans="3x + 30 = 180, x = 50"),
        Ex("Write an equation whose solution is x = 6, using two steps.", ans="For example 2x + 3 = 15.", think=True),
    ],
    check=["Can I solve an equation by doing the same to both sides?", "Can I construct an equation from words?", "Can I check my solution by substituting?"], look=[], note=NOTE)

N[(2, "2.6")]["book"] = BK(
    keys=[("inequality", "a statement using <, >: e.g. x > 3"), ("open circle", "shows the boundary value is not included"), ("integer", "a whole number")],
    intro=[], examples=[],
    exercise=[
        Ex("Write < or > between each pair.", ("−3 ☐ 2", "<"), ("−1 ☐ −6", ">"), ("0.4 ☐ 0.25", ">")),
        Ex("Write an inequality for each.", ("x is greater than 7", "x > 7"), ("the age a is under 16", "a < 16"), ("the mass m is between 2 and 5 kg", "2 < m < 5")),
        Ex("Draw each inequality on a number line.", ("x > −1", "open circle at −1, arrow right"), ("x < 4", "open circle at 4, arrow left"), ("−2 < x < 3", "open circles at −2 and 3, joined")),
        Ex("List the integers that satisfy each.", ("3 < x < 7", "4, 5, 6"), ("−4 < x < 1", "−3, −2, −1, 0")),
        Ex("A number line shows open circles at 0 and 5 joined by a line. Write the inequality and give the largest integer.", ans="0 < x < 5; 4"),
        Ex("Zoe says 'x > 2 includes 2'. Explain why she is wrong.", ans="> means strictly greater than, so 2 is not included (open circle).", think=True),
    ],
    check=["Can I read and write inequalities with < and >?", "Can I show an inequality on a number line?", "Can I list the integers in a range?"], look=[], note=NOTE)
