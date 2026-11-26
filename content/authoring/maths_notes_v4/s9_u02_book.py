# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u02 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(2, "2.1")]["book"] = BK(
    keys=[("substitute", "replace a letter with its value"), ("counter-example", "one case that shows a statement is false")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the value when a = −3, b = 4.", ("2a² + b", "22"), ("a³ − b", "−31"), ("(b − a)/(b + a)", "7")),
        Ex("Find a counter-example: 'x² is always greater than x'.", ans="x = 0.5 (or 0, or 1)"),
    ],
    check=["Can I substitute negative numbers and powers?", "Can I find counter-examples?"], look=[], note=NOTE)

N[(2, "2.2")]["book"] = BK(
    keys=[("expression", "a combination of letters, numbers and operations, with no equals sign")],
    intro=[], examples=[],
    exercise=[
        Ex("Write an expression.", ("the cost of 5 books at $b and 2 bags at $g", "5b + 2g"), ("the change from $50", "50 − (5b + 2g)"), ("the mean of p, q, r, s", "(p + q + r + s)/4")),
        Ex("A rectangle has length 3x − 1 and width x + 2. Write its perimeter.", ans="8x + 2"),
    ],
    check=["Can I write expressions from words?", "Do I use brackets correctly?"], look=[], note=NOTE)

N[(2, "2.3")]["book"] = BK(
    keys=[("index laws", "add, subtract or multiply indices when multiplying, dividing or raising a power")],
    intro=[], examples=[],
    exercise=[
        Ex("Simplify.", ("5x³ × 4x⁶", "20x⁹"), ("21y⁸ ÷ 7y²", "3y⁶"), ("(2z⁵)⁴", "16z²⁰"), ("w⁻³ × w⁷", "w⁴")),
        Ex("Find n if (a³)ⁿ = a¹⁵.", ans="n = 5"),
    ],
    check=["Can I use the index laws with letters and coefficients?"], look=[], note=NOTE)

N[(2, "2.4")]["book"] = BK(
    keys=[("expand", "multiply out brackets"), ("perfect square", "(x + a)² = x² + 2ax + a²"), ("difference of two squares", "(x + a)(x − a) = x² − a²")],
    intro=[], examples=[],
    exercise=[
        Ex("Expand and simplify.", ("(x + 6)(x − 4)", "x² + 2x − 24"), ("(3x − 1)²", "9x² − 6x + 1"), ("(4y + 7)(4y − 7)", "16y² − 49")),
        Ex("Use a difference of two squares to work out 62 × 58.", ans="3596"),
    ],
    check=["Can I expand two brackets?", "Do I know the special products?"], look=[], note=NOTE)

N[(2, "2.5")]["book"] = BK(
    keys=[("algebraic fraction", "a fraction with letters in it")],
    intro=[], examples=[],
    exercise=[
        Ex("Simplify.", ("x/6 + x/3", "x/2"), ("3a/4 − a/5", "11a/20"), ("(2b/3) × (9/4b)", "3/2"), ("(5c/8) ÷ (c/4)", "5/2")),
        Ex("Simplify (x + 2)/5 + (x − 1)/3.", ans="(8x + 1)/15"),
    ],
    check=["Can I add, subtract, multiply and divide algebraic fractions?"], look=[], note=NOTE)

N[(2, "2.6")]["book"] = BK(
    keys=[("formula", "a rule linking variables"), ("subject", "the variable on its own"), ("changing the subject", "rearranging a formula")],
    intro=[], examples=[],
    exercise=[
        Ex("Make x the subject.", ("y = 7x − 2", "x = (y + 2)/7"), ("y = (x − 3)/4", "x = 4y + 3"), ("y = x² (x > 0)", "x = √y")),
        Ex("A gym charges $25 to join plus $15 per month. Write a formula for the cost C of m months and find m when C = $205.", ans="C = 25 + 15m; m = 12"),
    ],
    check=["Can I write formulae?", "Can I change the subject?"], look=[], note=NOTE)
