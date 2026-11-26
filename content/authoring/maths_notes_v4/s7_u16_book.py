# -*- coding: utf-8 -*-
"""Stage 7 · Unit 16 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u16 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(16, "16.1")]["book"] = BK(
    keys=[("two-way table", "data sorted by two categories, with totals")],
    intro=[], examples=[],
    exercise=[
        Ex("Complete: Glasses yes/no by adults/children. Adults: yes 14, no ?, total 30. Children: yes ?, no 22, total ?. Totals: yes 20, grand total 58.", ans="adults no 16; children yes 6, total 28; no total 38"),
        Ex("From your table: what fraction of the people with glasses are children?", ans="6/20 = 3/10"),
        Ex("Design a two-way table to record 'has a sibling' by 'Year 7 / Year 8' and fill it in for your class.", ans="Your own table.", think=True),
    ],
    check=["Can I complete a two-way table?", "Can I answer questions using the right total?"], look=[], note=NOTE)

N[(16, "16.2")]["book"] = BK(
    keys=[("dual bar chart", "bars side by side to compare two groups"), ("compound bar chart", "parts stacked in one bar")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw a dual bar chart: Books read – Term 1: boys 12, girls 15; Term 2: boys 14, girls 13; Term 3: boys 9, girls 16.", ans="Two bars per term with a key."),
        Ex("Draw a compound bar chart of the same data. What does the top of each bar show?", ans="Total books read each term: 27, 27, 25."),
        Ex("Which chart is better for comparing boys and girls? Which for totals?", ans="Dual for comparing; compound for totals."),
    ],
    check=["Can I draw and read dual and compound bar charts?", "Can I choose between them?"], look=[], note=NOTE)

N[(16, "16.3")]["book"] = BK(
    keys=[("pie chart", "a circle split into sectors in proportion"), ("sector", "a 'slice' of the pie chart"), ("waffle diagram", "a 10 × 10 grid; each square is 1%")],
    intro=[], examples=[],
    exercise=[
        Ex("Draw a pie chart: pets of 36 students – dog 15, cat 12, fish 6, none 3.", ans="Angles 150°, 120°, 60°, 30°."),
        Ex("A pie chart of 90 people has a 'tea' sector of 140°. How many chose tea?", ans="35"),
        Ex("Shade a waffle diagram to show 38%.", ans="38 squares shaded."),
        Ex("Explain why two pie charts can't be compared without knowing their totals.", ans="Sectors show proportions, not numbers.", think=True),
    ],
    check=["Can I calculate pie chart angles?", "Can I read frequencies from a pie chart?", "Can I use waffle diagrams?"], look=[], note=NOTE)

N[(16, "16.4")]["book"] = BK(
    keys=[("infographic", "pictures, numbers and charts combined"), ("pictogram", "a chart using icons with a key")],
    intro=[], examples=[],
    exercise=[
        Ex("1 icon = 25 students. How many icons for", ("100", "4"), ("175", "7"), ("60", "2.4")),
        Ex("'3 in 8 people walk to work.' How many in a town of 12 000?", ans="4500"),
        Ex("Find an infographic in a newspaper or online. Write two things it does well and one way it could mislead.", ans="Your own answer.", think=True),
    ],
    check=["Can I read information from an infographic?", "Can I spot misleading features?"], look=[], note=NOTE)

N[(16, "16.5")]["book"] = BK(
    keys=[("representation", "a way of showing data: table, chart or graph")],
    intro=[], examples=[],
    exercise=[
        Ex("Choose the best chart.", ("rainfall each month for a year", "line graph or bar chart"), ("how a family spends its money", "pie chart"), ("goals by two teams in 5 matches", "dual bar chart")),
        Ex("Collect data on your class's favourite season and present it in two different ways. Which is better? Why?", ans="Your own charts.", think=True),
    ],
    check=["Can I choose a suitable chart for a set of data?", "Can I make a chart clear and fair?"], look=[], note=NOTE)

N[(16, "16.6")]["book"] = BK(
    keys=[("mode, median, mean", "most common; middle when ordered; total ÷ number"), ("range", "largest − smallest")],
    intro=[], examples=[],
    exercise=[
        Ex("For 7, 3, 9, 3, 8, find", ("the mode", "3"), ("the median", "7"), ("the mean", "6"), ("the range", "6")),
        Ex("Runners' times (s): A 12.1, 12.4, 12.0, 12.3; B 11.8, 13.0, 11.9, 12.5. Compare using the mean and range.", ans="A mean 12.2, range 0.4; B mean 12.3, range 1.2. A is faster on average and more consistent."),
        Ex("Write 5 numbers with mean 8 and median 7.", ans="For example 5, 6, 7, 10, 12.", think=True),
    ],
    check=["Can I find the mode, median, mean and range?", "Can I compare two sets of data in context?"], look=[], note=NOTE)
