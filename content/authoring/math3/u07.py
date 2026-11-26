# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 7 Statistics: tally charts and frequency tables (7.1 Tally charts, 7.2 Frequency tables).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(7, "Statistics: Tally Charts and Frequency Tables", "Statistics and probability",
         "Collecting data with tally marks, counting tallies, and reading and completing frequency tables to answer questions.",
         {"O1": {"code": "3Ss.01", "sec": "7.1", "codeNote": "", "t": "Record data using tally marks and count tallies in groups of five."},
          "O2": {"code": "3Ss.02", "sec": "7.2", "codeNote": "", "t": "Complete and interpret frequency tables to answer questions."}})
FRUIT = ["apple", "banana", "grape", "mango", "pear"]
COL = ["red", "blue", "green", "yellow"]


def tally(n): return ("||||/ " * (n // 5) + "|" * (n % 5)).strip() or "–"


s = U.section("7.1", "Tally charts", ["O1"])
s.idea("Tally marks", ["When we collect data we make a **tally mark** for each answer: |, ||, |||, ||||.",
       "The fifth mark goes **across** the first four to make a group of five: ||||/ . Then we count in fives."], table={"head": ["Fruit", "Tally", "Total"], "rows": [["apple", "||||/ ||", "7"], ["banana", "||||", "4"]]})
s.check(N("How many is ||||/ ||||/ |?", 11, o="O1"))
s.check(MC('Before you read on: what number does |||| ||| show?', '8', [('7', '|||| is 5; add 3.'), ('4', 'The crossed group is 5.')], o='O1'))
s.mistake("The fifth mark", ["The fifth tally mark crosses the other four, so each group is 5, not 4."])


def t1(r):
    n = r.randint(3, 19)
    return N(f"How many does this tally show: {tally(n)}?", n, o="O1")
def t2(r):
    v = [r.randint(2, 14) for _ in range(3)]; it = r.sample(FRUIT, 3); k = r.randrange(3)
    return N(f"The tally chart shows favourite fruits. How many children chose {it[k]}?", v[k], "children", units=["children"], o="O1", data={"head": ["Fruit", "Tally"], "rows": [[f, tally(x)] for f, x in zip(it, v)]})
def t3(r):
    v = [r.randint(2, 14) for _ in range(3)]; it = r.sample(FRUIT, 3)
    return TB("Count the tallies and complete the totals.", ["Fruit", "Tally", "Total"], [[f, tally(x), B(x)] for f, x in zip(it, v)], o="O1")
def t4(r):
    n = r.randint(2, 4)
    return N(f"How many tally marks are in {n} full groups of five?", 5 * n, o="O1")
def t5(r):
    xs = r.choices(COL[:3], k=r.randint(8, 12))
    k = r.randrange(3)
    return N(f"Colours chosen: {', '.join(xs)}. How many tally marks go next to {COL[k]}?", xs.count(COL[k]), o="O1", d="H")
def t6(r):
    v = r.sample(range(3, 15), 3); it = r.sample(FRUIT, 3); k = v.index(max(v))
    return S("Which fruit got the most tally marks?", [it[k], it[k].capitalize()], o="O1", data={"head": ["Fruit", "Tally"], "rows": [[f, tally(x)] for f, x in zip(it, v)]})
def t7(r):
    return MC("Why do we draw the fifth tally mark across the other four?", "to make groups of 5 that are quick to count", ["to cross out a mistake", "to show it is the biggest", "to start again"], o="O1")
def t8(r):
    a = r.randint(3, 12)
    return N(f"A tally shows {tally(a)}. Two more children answer. What is the new total?", a + 2, o="O1")


s.std([t2, t3, t1, t4, t6, t7, t8, t5], EX("Explain how to count the tally ||||/ ||||/ |||.", [("count the groups in fives: 5, 10", "5, ?10|fives|groups"), ("add the 3 single marks: 13", "13")], "Count the full groups in fives: 5, 10. Then add the 3 single marks: 11, 12, 13. The tally shows 13.", o="O1"))

s = U.section("7.2", "Frequency tables", ["O2"])
s.idea("How many?", ["A **frequency table** shows how many times each answer was given. **Frequency** means 'how many'.",
       "We can use it to answer questions: which was most popular? How many more chose red than blue? How many altogether?"], table={"head": ["Colour", "red", "blue", "green"], "rows": [["Frequency", "8", "5", "11"]]})
s.check(N("In the table above, how many children chose green?", 11, "children", units=["children"], o="O2"))
s.check(MC('Before you read on: in a frequency table, what does the frequency tell you?', 'How many times something happened', [('The name of the group', 'That is the category.'), ('The biggest number', 'It is a count.')], o='O2'))
s.mistake("Read the right row", ["Put your finger on the label first, then read the number next to it."])


def q1(r):
    v = [r.randint(2, 15) for _ in range(4)]; k = r.randrange(4)
    return N(f"How many children chose {COL[k]}?", v[k], "children", units=["children"], o="O2", data={"head": ["Colour", *COL], "rows": [["Frequency", *map(str, v)]]})
def q2(r):
    v = [r.randint(2, 15) for _ in range(4)]
    return N("How many children answered altogether?", sum(v), "children", units=["children"], o="O2", data={"head": ["Colour", *COL], "rows": [["Frequency", *map(str, v)]]})
def q3(r):
    v = r.sample(range(2, 20), 4); i, j = r.sample(range(4), 2)
    a, b = (i, j) if v[i] > v[j] else (j, i)
    return N(f"How many more chose {COL[a]} than {COL[b]}?", v[a] - v[b], o="O2", data={"head": ["Colour", *COL], "rows": [["Frequency", *map(str, v)]]})
def q4(r):
    v = r.sample(range(2, 20), 4); k = v.index(min(v))
    return S("Which colour was the least popular?", [COL[k], COL[k].capitalize()], o="O2", data={"head": ["Colour", *COL], "rows": [["Frequency", *map(str, v)]]})
def q5(r):
    v = [r.randint(2, 12) for _ in range(3)]; t = sum(v) + r.randint(2, 9)
    return N(f"{t} children chose a pet. The table shows cat, dog and fish. The rest chose rabbit. How many chose rabbit?", t - sum(v), "children", units=["children"], o="O2", d="H", data={"head": ["Pet", "cat", "dog", "fish"], "rows": [["Frequency", *map(str, v)]]})
def q6(r):
    xs = r.choices(["cat", "dog", "fish"], k=10)
    return TB(f"Pets: {', '.join(xs)}. Complete the frequency table.", ["Pet", "cat", "dog", "fish"], [["Frequency", B(xs.count("cat")), B(xs.count("dog")), B(xs.count("fish"))]], o="O2")
def q7(r):
    v = r.sample(range(2, 20), 4)
    return OD("Put the colours in order, most popular first.", [COL[i] for i in sorted(range(4), key=lambda k: -v[k])], o="O2", data={"head": ["Colour", *COL], "rows": [["Frequency", *map(str, v)]]}, d="H")
def q8(r):
    return MC("What does 'frequency' mean in a table?", "how many times something happens", ["the biggest number", "the name of the group", "the colour of the bar"], o="O2")


s.std([q1, q2, q3, q4, q6, q8, q5, q7], EX("Explain how to find how many children answered a survey from a frequency table.", [("add up all the frequencies", "add|total"), ("the total is the number of children", "total|altogether|children")], "Add up all the numbers in the frequency row. The total is how many children answered.", o="O2"))

U.mindmap(("Tally charts", "Groups of five • count in fives", "O1", "7.1"), ("Frequency tables", "How many • most and least popular", "O2", "7.2"))
