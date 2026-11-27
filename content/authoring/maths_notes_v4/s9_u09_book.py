# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u09 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(9, "9.1")]["book"] = BK(
    keys=[("linear sequence", "terms change by the same amount"), ("non-linear sequence", "the change is different each time"), ("term-to-term rule", "how to get the next term from the previous one")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the next two terms.", ("2.4, 3, 3.6, 4.2", "4.8, 5.4"), ("1, 5, 11, 19, 29", "41, 55"), ("200, 100, 50, 25", "12.5, 6.25")),
        Ex("First term 3, rule 'multiply by 2 then add 1'. Write the first five terms.", ans="3, 7, 15, 31, 63"),
    ],
    check=["Can I generate sequences from rules?", "Can I tell linear from non-linear?"], look=[], note=NOTE)

N[(9, "9.2")]["book"] = BK(
    keys=[("nth term", "a rule giving any term from its position n"), ("quadratic sequence", "a sequence based on n²")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the nth term.", ("9, 14, 19, 24", "5n + 4"), ("30, 26, 22, 18", "34 − 4n"), ("4, 7, 12, 19", "n² + 3")),
        Ex("Is 150 a term of 6n − 3? Explain.", ans="No: 6n = 153, n = 25.5"),
    ],
    check=["Can I find and use the nth term?"], look=[], note=NOTE)

N[(9, "9.3")]["book"] = BK(
    keys=[("function", "a rule that turns each input into one output"), ("inverse", "the operations that undo a function")],
    intro=[], examples=[],
    exercise=[
        Ex("Complete a table for x = −2, −1, 0, 1, 2.", ("y = x² − 5", "−1, −4, −5, −4, −1"), ("y = 2x³", "−16, −2, 0, 2, 16")),
        Ex("x → + 3 → square → y. Write the equation and find x when y = 64 (x positive).", ans="y = (x + 3)²; x = 5"),
    ],
    check=["Can I use function machines with powers?", "Can I write them as equations?"], look=[], note=NOTE)
