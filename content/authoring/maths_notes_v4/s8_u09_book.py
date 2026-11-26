# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u09 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(9, "9.1")]["book"] = BK(
    keys=[("linear sequence", "constant difference"), ("non-linear sequence", "differences change"), ("term-to-term rule", "how to get the next term from the previous one")],
    intro=[], examples=[],
    exercise=[
        Ex("Write the first five terms.", ("start 6, rule + 7", "6, 13, 20, 27, 34"), ("start 2, rule × 3 − 2", "2, 4, 10, 28, 82"), ("term = n² + 3", "4, 7, 12, 19, 28")),
        Ex("Linear or non-linear?", ("4, 9, 14, 19", "linear"), ("3, 6, 11, 18", "non-linear")),
        Ex("Make up a two-step term-to-term rule and write its first six terms.", ans="Your own sequence.", think=True),
    ],
    check=["Can I generate sequences from both types of rule?", "Can I tell linear from non-linear?"], look=[], note=NOTE)

N[(9, "9.2")]["book"] = BK(
    keys=[("position-to-term rule", "a rule using the position n")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the rule.", ("6, 10, 14, 18", "4n + 2"), ("25, 22, 19, 16", "28 − 3n")),
        Ex("A pattern of pentagons in a row uses 5, 9, 13 matches. Find the rule and the matches for 30 pentagons.", ans="4n + 1; 121"),
        Ex("Draw a pattern for the rule 2n + 3 and explain the 2 and the 3.", ans="Your own pattern.", think=True),
    ],
    check=["Can I find a rule from a pattern?", "Can I explain the rule using the diagram?"], look=[], note=NOTE)

N[(9, "9.3")]["book"] = BK(
    keys=[("nth term", "an algebraic rule for any term, e.g. 3n + 9")],
    intro=[], examples=[],
    exercise=[
        Ex("Find the nth term.", ("8, 11, 14, 17", "3n + 5"), ("−6, −2, 2, 6", "4n − 10"), ("31, 24, 17, 10", "38 − 7n")),
        Ex("For 4n − 3: find the 40th term and which term is 141.", ans="157; 36th"),
        Ex("Is 250 a term of 6n + 4? Explain.", ans="Yes, n = 41."),
        Ex("Write two different sequences that both contain the number 30.", ans="For example 3n and 4n + 2.", think=True),
    ],
    check=["Can I find the nth term?", "Can I use it to find terms and positions?"], look=[], note=NOTE)

N[(9, "9.4")]["book"] = BK(
    keys=[("function", "a rule mapping inputs to outputs"), ("inverse function", "undoes the function"), ("mapping diagram", "arrows from inputs to outputs")],
    intro=[], examples=[],
    exercise=[
        Ex("Write as an equation.", ("× 4 then − 3", "y = 4x − 3"), ("+ 5 then ÷ 2", "y = (x + 5)/2")),
        Ex("Find the inverse.", ("y = 5x + 2", "x = (y − 2)/5"), ("y = 3(x − 4)", "x = y/3 + 4")),
        Ex("Draw a mapping diagram for x → 3x − 1 for x = 0, 1, 2, 3.", ans="0 → −1, 1 → 2, 2 → 5, 3 → 8"),
        Ex("Find a function, other than y = x, that is its own inverse.", ans="For example y = 12 − x or y = 1/x.", think=True),
    ],
    check=["Can I represent functions in different ways?", "Can I find inverse functions?"], look=[], note=NOTE)
