# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u12 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(12, "12.1")]["book"] = BK(
    keys=[("mutually exclusive", "events that cannot happen at the same time")],
    intro=[], examples=[],
    exercise=[
        Ex("Cards 1–40. Find", ("P(multiple of 9 or multiple of 10)", "8/40 = 1/5"), ("P(multiple of 4 or multiple of 6)", "13/40")),
        Ex("A spinner has P(A) = 0.15, P(B) = 0.35, P(C) = x, P(D) = 3x. Find x.", ans="x = 0.125"),
    ],
    check=["Can I add probabilities of mutually exclusive events?"], look=[], note=NOTE)

N[(12, "12.2")]["book"] = BK(
    keys=[("independent events", "one doesn't affect the other"), ("dependent events", "one changes the probability of the other")],
    intro=[], examples=[],
    exercise=[
        Ex("Independent or dependent?", ("rolling a dice twice", "independent"), ("taking two socks from a drawer without replacing", "dependent"), ("choosing a card, replacing it, choosing again", "independent")),
        Ex("A box has 6 lemon and 4 orange sweets. One lemon is eaten. Find P(next is lemon).", ans="5/9"),
    ],
    check=["Can I decide whether events are independent?"], look=[], note=NOTE)

N[(12, "12.3")]["book"] = BK(
    keys=[("tree diagram", "a diagram showing all outcomes of combined events")],
    intro=[], examples=[],
    exercise=[
        Ex("P(a team wins) = 0.6 each match, independent. Draw a tree for two matches and find", ("P(win both)", "0.36"), ("P(win exactly one)", "0.48"), ("P(win at least one)", "0.84")),
        Ex("A dice is rolled twice. Find P(no 1s).", ans="25/36"),
    ],
    check=["Can I multiply probabilities and use tree diagrams?"], look=[], note=NOTE)

N[(12, "12.4")]["book"] = BK(
    keys=[("relative frequency", "frequency ÷ number of trials"), ("expected frequency", "probability × number of trials")],
    intro=[], examples=[],
    exercise=[
        Ex("Roll a dice 60 times. Record the relative frequency of a 6 after 10, 20, 30, 60 rolls. What do you notice?", ans="It moves towards 1/6.", think=True),
        Ex("A coin lands heads 138 times in 250 tosses. Estimate P(head) and the number of heads in 1000 tosses.", ans="0.552; about 552"),
    ],
    check=["Can I carry out and analyse chance experiments?"], look=[], note=NOTE)
