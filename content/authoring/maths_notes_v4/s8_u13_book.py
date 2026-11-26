# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u13 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(13, "13.1")]["book"] = BK(
    keys=[("sample space diagram", "a table of all possible outcomes"), ("complementary event", "'not A'; P(not A) = 1 − P(A)")],
    intro=[], examples=[],
    exercise=[
        Ex("Two dice are rolled and the scores added. Find", ("P(9)", "1/9"), ("P(odd total)", "1/2"), ("P(total less than 5)", "1/6")),
        Ex("A coin is tossed and a 4-sided spinner (1–4) spun. List the outcomes and find P(head and an even number).", ans="8 outcomes; 2/8 = 1/4"),
        Ex("P(red) = 0.15, P(blue) = 0.4; the rest are white. Find P(white) and P(not blue).", ans="0.45; 0.6"),
        Ex("Design a game with two dice where both players have an equal chance of winning.", ans="For example player 1 wins on an even total, player 2 on an odd total.", think=True),
    ],
    check=["Can I list outcomes for two events?", "Can I use P(not A) = 1 − P(A)?"], look=[], note=NOTE)

N[(13, "13.2")]["book"] = BK(
    keys=[("theoretical probability", "from equally likely outcomes"), ("relative frequency", "experimental probability: frequency ÷ trials"), ("expected frequency", "P × number of trials")],
    intro=[], examples=[],
    exercise=[
        Ex("A dice is rolled 300 times: 1 → 46, 2 → 52, 3 → 48, 4 → 55, 5 → 41, 6 → 58. Find the relative frequency of each and compare with 1/6.", ans="0.153, 0.173, 0.16, 0.183, 0.137, 0.193 – all near 0.167"),
        Ex("A biased coin gave 312 heads in 480 tosses. Estimate P(head) and the number of heads in 1000 tosses.", ans="0.65; 650"),
        Ex("Toss a coin 50 times, recording the relative frequency of heads every 10 tosses. What do you notice?", ans="It moves towards 0.5.", think=True),
    ],
    check=["Can I calculate relative frequencies?", "Can I compare experimental and theoretical probabilities?"], look=[], note=NOTE)
