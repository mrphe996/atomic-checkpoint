# -*- coding: utf-8 -*-
"""Stage 8 · Unit 6 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s8_u06 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(6, "6.1")]["book"] = BK(
    keys=[("primary data", "data you collect yourself"), ("secondary data", "data that already exists"), ("leading question", "a question that suggests an answer"), ("pilot", "a small test of a questionnaire")],
    intro=[], examples=[],
    exercise=[
        Ex("Primary or secondary?", ("measuring classmates' arm spans", "primary"), ("a country's population from a website", "secondary")),
        Ex("Rewrite so it is not leading: 'Surely you agree school should start later?'", ans="What time would you like school to start? □ before 8:00 □ 8:00–8:29 □ 8:30–8:59 □ 9:00 or later"),
        Ex("Design response boxes for 'minutes spent reading yesterday'.", ans="0, 1–15, 16–30, 31–60, more than 60"),
        Ex("Plan an investigation into 'Do taller students jump further?'", ans="Height and jump distance (both continuous), measured; enough students; compare.", think=True),
    ],
    check=["Can I plan data for linked questions?", "Can I design fair questions and response boxes?"], look=[], note=NOTE)

N[(6, "6.2")]["book"] = BK(
    keys=[("simple random sample", "every member has an equal chance"), ("systematic sample", "every k-th member of a list"), ("stratified sample", "each group sampled in proportion"), ("bias", "unfairly favouring some members")],
    intro=[], examples=[],
    exercise=[
        Ex("Name the method.", ("every 10th ticket sold", "systematic"), ("names from a hat", "simple random"), ("asking people nearby", "convenience")),
        Ex("A company has 150 managers and 450 workers. Take a stratified sample of 40.", ans="10 managers, 30 workers"),
        Ex("Explain why asking people in a library about reading habits is biased.", ans="Library users read more than average."),
        Ex("Design a fair sample of 60 for your school. Describe your method.", ans="Your own plan.", think=True),
    ],
    check=["Can I describe different sampling methods?", "Can I spot bias?", "Can I take a stratified sample?"], look=[], note=NOTE)
