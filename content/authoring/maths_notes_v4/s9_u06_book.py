# -*- coding: utf-8 -*-
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s9_u06 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(6, "6.1")]["book"] = BK(
    keys=[("population", "everyone you want to find out about"), ("sample", "the part you collect data from"), ("hypothesis", "a prediction you can test")],
    intro=[], examples=[],
    exercise=[
        Ex("A school has Year 7: 240, Year 8: 210, Year 9: 150. Find a stratified sample of 40.", ans="16, 14, 10"),
        Ex("Plan an investigation into 'Do students who read more get higher English marks?': question, predictions, data, sample, analysis.", ans="Answers vary.", think=True),
    ],
    check=["Can I plan an investigation?", "Can I choose and justify a sampling method?"], look=[], note=NOTE)

N[(6, "6.2")]["book"] = BK(
    keys=[("bias", "something that makes results lean one way"), ("misleading", "giving a false impression")],
    intro=[], examples=[],
    exercise=[
        Ex("Give the source of bias.", ("a survey about cycling at a bike shop", "unrepresentative place"), ("'You agree that uniforms are smart, don't you?'", "leading question"), ("10 people asked about a city of 1 million", "sample too small")),
        Ex("Find an advert or news graph that could be misleading. Explain why.", ans="Answers vary.", think=True),
    ],
    check=["Can I identify sources of bias?", "Can I spot misleading information?"], look=[], note=NOTE)
