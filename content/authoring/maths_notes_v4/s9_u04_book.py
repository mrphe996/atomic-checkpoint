# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u04 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(4, "4.1")]["book"] = BK(
    keys=[("construct", "write an equation from a problem"), ("solve", "find the value that makes the equation true")],
    intro=[], examples=[],
    exercise=[
        Ex("Solve.", ("8x − 5 = 3x + 20", "x = 5"), ("4(x − 2) = 2(x + 3)", "x = 7"), ("(x + 3)/4 = (x − 1)/2", "x = 5")),
        Ex("A rectangle is 3 cm longer than it is wide and its perimeter is 46 cm. Write and solve an equation for the width.", ans="2w + 2(w + 3) = 46; w = 10 cm"),
    ],
    check=["Can I construct equations?", "Can I solve equations with brackets and fractions?"], look=[], note=NOTE)

N[(4, "4.2")]["book"] = BK(
    keys=[("simultaneous equations", "two equations true at the same time"), ("elimination", "adding or subtracting to remove a letter"), ("substitution", "replacing a letter with an expression")],
    intro=[], examples=[],
    exercise=[
        Ex("Solve.", ("x + y = 15, x − y = 3", "x = 9, y = 6"), ("2x + 5y = 16, 2x + y = 8", "x = 3, y = 2"), ("y = 4x − 3, x + y = 7", "x = 2, y = 5")),
        Ex("5 notebooks and 2 pens cost $9.50; 3 notebooks and 2 pens cost $6.30. Find the cost of each.", ans="notebook $1.60, pen $0.75"),
    ],
    check=["Can I solve by elimination and substitution?"], look=[], note=NOTE)

N[(4, "4.3")]["book"] = BK(
    keys=[("inequality", "a statement using <, ≤, > or ≥"), ("solution set", "all values that satisfy an inequality")],
    intro=[], examples=[],
    exercise=[
        Ex("Solve.", ("3x + 4 > 19", "x > 5"), ("9 − 2x ≤ 1", "x ≥ 4"), ("4x − 1 < x + 11", "x < 4")),
        Ex("List the integers n with −4 < 2n ≤ 6.", ans="−1, 0, 1, 2, 3"),
    ],
    check=["Can I solve inequalities, including with negatives?", "Can I list integer solutions?"], look=[], note=NOTE)
