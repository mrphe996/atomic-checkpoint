# -*- coding: utf-8 -*-
"""Stage 7 · Unit 6 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u06 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(6, "6.1")]["book"] = BK(
    keys=[("categorical data", "words or categories"), ("discrete data", "counted values"), ("continuous data", "measured values"), ("frequency", "how many times something happens")],
    intro=[], examples=[],
    exercise=[
        Ex("Categorical, discrete or continuous?", ("type of phone", "categorical"), ("number of apps installed", "discrete"), ("screen width", "continuous"), ("battery life in hours", "continuous")),
        Ex("Make a frequency table for the number of letters in these words: cat, house, tree, sun, garden, map, river, dog, apple, sky.", ans="3: 5, 4: 1, 5: 3, 6: 1"),
        Ex("Write suitable groups (no gaps or overlaps) for times between 0 and 30 seconds.", ans="0 ≤ t < 5, 5 ≤ t < 10, … 25 ≤ t < 30"),
        Ex("Plan an investigation into: 'Students who eat breakfast run faster.' What data, what types, how collected?", ans="Breakfast yes/no (categorical); sprint time (continuous) by experiment; enough students; compare averages.", think=True),
    ],
    check=["Can I write a statistical question or prediction?", "Can I identify the type of data?", "Can I design a data-collection sheet and frequency table?"], look=[], note=NOTE)

N[(6, "6.2")]["book"] = BK(
    keys=[("population", "everyone or everything the question is about"), ("sample", "the part of the population you collect data from"), ("biased", "unfairly favouring some members"), ("random", "every member has the same chance")],
    intro=[], examples=[],
    exercise=[
        Ex("Name the population and suggest a sample.", ("How long do phone batteries of one model last?", "all phones of that model; e.g. 50 tested"), ("What music do students at my school like?", "all students; e.g. 10 from each class at random")),
        Ex("Is each sample biased? Explain.", ("asking people at a bookshop how often they read", "biased – readers"), ("choosing 40 names at random from the school register", "not biased")),
        Ex("A school has 200 Y7, 300 Y8 and 100 Y9. Choose a sample of 60 with the same mix.", ans="20, 30, 10"),
        Ex("In a random sample of 50 students, 18 walk to school. Estimate how many of the 750 students walk.", ans="270"),
        Ex("Explain why a sample of 5 is not enough to decide the favourite snack of a school.", ans="Too small – results could easily be due to chance.", think=True),
    ],
    check=["Can I name the population and the sample?", "Can I spot and avoid bias?", "Can I explain the effect of sample size?"], look=[], note=NOTE)
