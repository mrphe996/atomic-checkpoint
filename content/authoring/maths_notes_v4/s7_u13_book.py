# -*- coding: utf-8 -*-
"""Stage 7 · Unit 13 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u13 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(13, "13.1")]["book"] = BK(
    keys=[("probability", "how likely something is, from 0 to 1"), ("even chance", "probability 0.5"), ("certain / impossible", "probability 1 / 0")],
    intro=[], examples=[],
    exercise=[
        Ex("Choose a word: impossible, unlikely, even chance, likely, certain.", ("a dice shows a number from 1 to 6", "certain"), ("a coin lands tails", "even chance"), ("a dice shows 6", "unlikely")),
        Ex("Draw a probability scale and mark: 0.2, 3/4, 50%, 9/10.", ans="In order 0.2, 0.5, 0.75, 0.9."),
        Ex("Order from least to most likely: 0.62, 3/5, 65%, 0.6", ans="3/5 = 0.6, 0.62, 65%"),
        Ex("Write an event for each word on the scale.", ans="Any correct examples.", think=True),
    ],
    check=["Can I use the language of chance?", "Can I place probabilities on the scale from 0 to 1?"], look=[], note=NOTE)

N[(13, "13.2")]["book"] = BK(
    keys=[("outcome", "a possible result"), ("equally likely", "each outcome has the same chance"), ("mutually exclusive", "can't happen at the same time")],
    intro=[], examples=[],
    exercise=[
        Ex("A bag has 6 red, 4 blue and 2 white counters. Find", ("P(red)", "1/2"), ("P(white)", "1/6"), ("P(not blue)", "2/3")),
        Ex("A fair 10-sided dice (1–10) is rolled. Find", ("P(a multiple of 3)", "3/10"), ("P(not 7)", "9/10")),
        Ex("P(A) = 0.15 and P(B) = 0.6. A, B and C are the only outcomes. Find P(C).", ans="0.25"),
        Ex("Are 'a number less than 4' and 'an even number' mutually exclusive on one dice roll? Explain.", ans="No – 2 is both.", think=True),
    ],
    check=["Can I find probabilities of equally likely outcomes?", "Can I use P(not A) = 1 − P(A)?", "Can I tell if outcomes are mutually exclusive?"], look=[], note=NOTE)

N[(13, "13.3")]["book"] = BK(
    keys=[("trial", "one go of an experiment"), ("experimental probability", "frequency ÷ number of trials"), ("biased", "not fair – some outcomes are more likely")],
    intro=[], examples=[],
    exercise=[
        Ex("A bottle top was flipped 150 times and landed 'up' 63 times. Find the experimental probability of 'up'.", ans="0.42"),
        Ex("How many would you expect?", ("heads in 500 tosses of a fair coin", "250"), ("fives in 90 rolls of a fair dice", "15")),
        Ex("A dice was rolled 300 times: 1 → 48, 2 → 51, 3 → 49, 4 → 52, 5 → 50, 6 → 50. Is it fair? Explain.", ans="Probably fair – each close to the expected 50."),
        Ex("Do your own experiment: drop a paper cup 50 times. Record how it lands and estimate each probability.", ans="Your own results.", think=True),
    ],
    check=["Can I find an experimental probability?", "Can I calculate an expected number?", "Can I explain why more trials are better?"], look=[], note=NOTE)
