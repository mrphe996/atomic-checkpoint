# -*- coding: utf-8 -*-
"""Stage 7 · Unit 12 – Words to know, Practice on paper and checklists (Camday's own questions)."""
from maths_notes_v4.kit4 import BK, Ex
from maths_notes_v4.s7_u12 import NOTES as N

NOTES = {}
NOTE = "The whole lesson as a document you can print, then Practice on paper with answers at the back."

N[(12, "12.1")]["book"] = BK(
    keys=[("ratio", "a comparison of quantities, e.g. 3 : 2"), ("simplest form", "no common factor except 1")],
    intro=[], examples=[],
    exercise=[
        Ex("Simplify.", ("16 : 24", "2 : 3"), ("45 : 18", "5 : 2"), ("12 : 30 : 42", "2 : 5 : 7"), ("2.4 : 6", "2 : 5")),
        Ex("Simplify, using the same units.", ("40 cm : 2 m", "1 : 5"), ("300 g : 1.2 kg", "1 : 4"), ("45 min : 2 h", "3 : 8")),
        Ex("In a car park there are 36 cars and 8 vans. Write cars : vans in simplest form.", ans="9 : 2"),
        Ex("Write three different ratios that simplify to 3 : 5.", ans="For example 6 : 10, 9 : 15, 30 : 50.", think=True),
    ],
    check=["Can I write a ratio in the right order?", "Can I simplify ratios, including three parts and different units?"], look=[], note=NOTE)

N[(12, "12.2")]["book"] = BK(
    keys=[("share in a ratio", "split an amount into unequal parts in a given ratio"), ("part", "one share of the ratio")],
    intro=[], examples=[],
    exercise=[
        Ex("Share.", ("$80 in the ratio 3 : 5", "$30, $50"), ("63 kg in 2 : 7", "14 kg, 49 kg"), ("150 in 1 : 2 : 3", "25, 50, 75")),
        Ex("Paint is mixed blue : white = 2 : 9. There are 18 litres of white. How much blue? How much paint in total?", ans="4 litres; 22 litres"),
        Ex("A bag has red : green counters in the ratio 5 : 3. There are 10 more red than green. How many counters?", ans="40"),
        Ex("Make up a sharing problem whose answer is $45 and $75.", ans="For example share $120 in the ratio 3 : 5.", think=True),
    ],
    check=["Can I share an amount in a ratio?", "Can I find the total from one share?", "Can I solve 'difference' problems?"], look=[], note=NOTE)

N[(12, "12.3")]["book"] = BK(
    keys=[("direct proportion", "both quantities change by the same factor"), ("unitary method", "find the value of one, then multiply"), ("best buy", "the cheapest price for the same amount")],
    intro=[], examples=[],
    exercise=[
        Ex("Use the unitary method.", ("7 notebooks cost $10.50. Find the cost of 4.", "$6"), ("A car travels 135 km on 9 litres. How far on 14 litres?", "210 km")),
        Ex("A cake for 8 people uses 240 g butter and 3 eggs. Write the amounts for 12 people.", ans="360 g butter and 4.5 eggs (in practice 4 or 5)"),
        Ex("Which is better value: 330 ml for $0.99 or 500 ml for $1.40?", ans="500 ml ($0.28 per 100 ml vs $0.30)"),
        Ex("Give one example of two quantities that are in direct proportion and one that are not.", ans="Cost of identical items / number of items; a taxi with a fixed fee.", think=True),
    ],
    check=["Can I recognise direct proportion?", "Can I use the unitary method?", "Can I find the best buy?"], look=[], note=NOTE)
