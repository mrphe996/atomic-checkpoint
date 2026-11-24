# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 10 Collecting and recording data (10.1 Planning and collecting data, 10.2 Recording and sorting data).
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(10, "Collecting and Recording Data", "Statistics and probability",
         "Asking questions that can be answered with data, collecting data with tally charts, and recording it in frequency tables, Venn diagrams and Carroll diagrams.",
         {"O1": {"code": "4Ss.01", "sec": "10.1", "codeNote": "", "t": "Plan how to collect data to answer a question, and record it in a tally chart."},
          "O2": {"code": "4Ss.02", "sec": "10.2", "codeNote": "", "t": "Record and sort data in frequency tables, Venn diagrams and Carroll diagrams."}})
SP = ["football", "swimming", "tennis", "dance"]


def tally(n): return ("||||/ " * (n // 5) + "|" * (n % 5)).strip() or "–"


s = U.section("10.1", "Planning and collecting data", ["O1"])
s.idea("Asking a good question", ["Start with a **question** you can answer with data, such as 'Which sport is the most popular in our class?'.",
       "Decide **what** to collect and **who** to ask, then record answers with **tally marks**: ||||/ is a group of five."], table={"head": ["Sport", "Tally", "Frequency"], "rows": [["football", "||||/ |||", "8"], ["swimming", "||||/", "5"]]})
s.check(N("How many is ||||/ ||||/ ||?", 12, o="O1"))
s.mistake("Count in fives", ["Each crossed group is 5 marks, not 4."])


def t1(r):
    n = r.randint(3, 24)
    return N(f"What number does this tally show: {tally(n)}?", n, o="O1")
def t2(r):
    v = [r.randint(2, 15) for _ in range(3)]; it = r.sample(SP, 3); k = r.randrange(3)
    return N(f"The tally chart shows favourite sports. How many chose {it[k]}?", v[k], "children", units=["children"], o="O1", data={"head": ["Sport", "Tally"], "rows": [[s_, tally(x)] for s_, x in zip(it, v)]})
def t3(r):
    v = [r.randint(2, 15) for _ in range(3)]; it = r.sample(SP, 3)
    return TB("Count the tallies and complete the frequencies.", ["Sport", "Tally", "Frequency"], [[s_, tally(x), B(x)] for s_, x in zip(it, v)], o="O1")
def t4(r):
    qs = [("Which fruit do children in our class like best?", "Yes"), ("What is the colour of the sky?", "No"), ("How many pets do children in Year 4 have?", "Yes"), ("Is 5 bigger than 3?", "No")]
    return GD("Can each question be answered by collecting data from people?", "Data question?", r.sample(qs, 4), o="O1", extra=["Yes", "No"])
def t5(r):
    xs = r.choices(SP[:3], k=r.randint(10, 14)); k = r.randrange(3)
    return N(f"Answers: {', '.join(xs)}. How many tally marks go next to {SP[k]}?", xs.count(SP[k]), o="O1")
def t6(r):
    return MC("Kai wants to know the most popular sport in his school. Who should he ask?", "children from every class", ["only his best friend", "only the football team", "only teachers"], o="O1", d="H")
def t7(r):
    g = r.randint(2, 5); s_ = r.randint(0, 4)
    return N(f"A tally has {g} full groups of five and {s_} single marks. What is the total?", 5 * g + s_, o="O1")
def t8(r):
    a = r.randint(3, 15); k = r.randint(1, 4)
    return N(f"A tally shows {tally(a)}. Then {k} more children answer. What is the new frequency?", a + k, o="O1")


s.std([t2, t3, t1, t4, t5, t7, t8, t6], EX("Explain why tally marks are grouped in fives.", [("the fifth mark crosses the other four", "fifth|cross"), ("so you can count quickly in fives", "count|fives|quick")], "The fifth mark is drawn across the other four to make a group of five, so you can count the total quickly in fives.", o="O1"))

s = U.section("10.2", "Recording and sorting data", ["O2"])
s.idea("Tables and sorting diagrams", ["A **frequency table** shows how many times each answer appears.",
       "A **Venn diagram** sorts with overlapping circles; things that fit both rules go in the overlap. A **Carroll diagram** sorts in a table with 'yes' and 'not' for each rule."],
       table={"head": ["", "even", "not even"], "rows": [["more than 20", "24, 30", "25, 31"], ["not more than 20", "12, 18", "7, 15"]]})
s.check(MC("Where does 30 go in a Venn diagram for 'even' and 'multiple of 5'?", "the overlap", [("'even' only", ""), ("'multiple of 5' only", ""), ("outside", "")], o="O2"))
s.mistake("The overlap", ["A number that fits both rules goes in the overlap, not in one circle."])


def v1(r):
    n = r.randint(1, 50)
    a, b = n % 2 == 0, n > 20
    ans = f"{'even' if a else 'not even'}, {'more than 20' if b else 'not more than 20'}"
    opts = [f"{x}, {y}" for x in ("even", "not even") for y in ("more than 20", "not more than 20")]
    return MC(f"Where does {n} go in a Carroll diagram for 'even' and 'more than 20'?", ans, [o for o in opts if o != ans], o="O2")
def v2(r):
    ns = r.sample(range(1, 50), 4)
    lab = lambda n: "both" if n % 2 == 0 and n % 5 == 0 else "even only" if n % 2 == 0 else "multiple of 5 only" if n % 5 == 0 else "neither"
    return GD("Sort into a Venn diagram: circle A 'even', circle B 'multiple of 5'.", "Region", [(str(n), lab(n)) for n in ns], o="O2", extra=["even only", "multiple of 5 only", "both", "neither"])
def v3(r):
    v = [r.randint(2, 15) for _ in range(4)]; k = r.randrange(4)
    return N(f"How many children chose {SP[k]}?", v[k], "children", units=["children"], o="O2", data={"head": ["Sport", *SP], "rows": [["Frequency", *map(str, v)]]})
def v4(r):
    v = [r.randint(2, 15) for _ in range(4)]
    return N("How many children answered altogether?", sum(v), "children", units=["children"], o="O2", data={"head": ["Sport", *SP], "rows": [["Frequency", *map(str, v)]]})
def v5(r):
    ns = r.sample(range(1, 50), 6)
    return TB(f"Sort {', '.join(map(str, ns))} into a Carroll diagram. How many in each box?", ["", "even", "not even"], [["more than 20", B(sum(1 for n in ns if n % 2 == 0 and n > 20)), B(sum(1 for n in ns if n % 2 and n > 20))], ["not more than 20", B(sum(1 for n in ns if n % 2 == 0 and n <= 20)), B(sum(1 for n in ns if n % 2 and n <= 20))]], o="O2", d="H")
def v6(r):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(1, 6)
    return N(f"In a Venn diagram, {a} children are only in 'has a cat', {b} only in 'has a dog' and {c} in the overlap. How many have a dog?", b + c, "children", units=["children"], o="O2", d="H")
def v7(r):
    v = r.sample(range(2, 20), 4); i, j = r.sample(range(4), 2); a, b = (i, j) if v[i] > v[j] else (j, i)
    return N(f"How many more chose {SP[a]} than {SP[b]}?", v[a] - v[b], "children", units=["children"], o="O2", data={"head": ["Sport", *SP], "rows": [["Frequency", *map(str, v)]]})
def v8(r):
    return MC("In a Venn diagram, where do items go that fit neither rule?", "outside the circles", ["in the overlap", "in the first circle", "they are not shown"], o="O2")


s.std([v2, v5, v1, v3, v4, v7, v6, v8], EX("Explain where 15 goes in a Venn diagram for 'odd' and 'multiple of 5'.", [("15 is odd and a multiple of 5", "odd|multiple of 5|both"), ("so it goes in the overlap", "overlap|middle|both circles")], "15 is odd and it is also a multiple of 5, so it fits both rules. It goes in the overlap where the circles cross.", o="O2"))

U.mindmap(("Collecting", "Ask a question • tally in fives", "O1", "10.1"), ("Recording", "Frequency tables • Venn • Carroll", "O2", "10.2"))
