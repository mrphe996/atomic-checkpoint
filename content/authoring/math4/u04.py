# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 4 Probability (4.1 Likelihood, 4.2 Chance experiments).
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(4, "Probability", "Statistics and probability",
         "Describing how likely events are with words like impossible, unlikely, even chance, likely and certain, and carrying out chance experiments.",
         {"O1": {"code": "4Sp.01", "sec": "4.1", "codeNote": "", "t": "Use the language of chance to describe events: impossible, unlikely, even chance, likely, certain."},
          "O2": {"code": "4Sp.02", "sec": "4.2", "codeNote": "", "t": "Carry out chance experiments, record results and discuss whether outcomes are equally likely."}})
W = ["impossible", "unlikely", "even chance", "likely", "certain"]
COL = ["red", "blue", "green", "yellow"]


def word(a, n):
    return "impossible" if a == 0 else "certain" if a == n else "even chance" if 2 * a == n else "unlikely" if 2 * a < n else "likely"


s = U.section("4.1", "Likelihood", ["O1"])
s.idea("Five words for chance", ["Events can be **impossible**, **unlikely**, have an **even chance**, be **likely** or **certain**.",
       "On a spinner with 3 red parts out of 4, red is **likely**. With 2 out of 4 it has an **even chance**."], fig={"kind": "spinner", "labels": ["R", "R", "R", "B"]})
s.check(MC("A bag has 1 red and 9 blue cubes. How likely is picking red?", "unlikely", [("likely", ""), ("certain", ""), ("impossible", "")], o="O1"))
s.mistake("Even chance", ["'Even chance' means exactly as likely to happen as not."])


def l1(r):
    n = pick(r, [4, 6, 8]); k = r.randint(0, n); lab = ["R"] * k + ["B"] * (n - k); r.shuffle(lab)
    return MC(f"The spinner has {k} red sections (R) out of {n}. How likely is red?", word(k, n), [w for w in W if w != word(k, n)][:3], o="O1", fig={"kind": "spinner", "labels": lab})
def l2(r):
    a, b = r.randint(0, 10), r.randint(0, 10)
    if a + b == 0: return None
    return MC(f"A bag has {a} red and {b} blue counters. How likely is picking red?", word(a, a + b), [w for w in W if w != word(a, a + b)][:3], o="O1")
def l3(r):
    evs = [("a dice shows a number less than 7", "certain"), ("a dice shows 8", "impossible"), ("a coin lands on heads", "even chance"), ("a dice shows a 5", "unlikely"), ("a dice shows more than 1", "likely"),
           ("tomorrow comes after today", "certain"), ("a cat speaks English", "impossible"), ("a dice shows an odd number", "even chance")]
    return GD("How likely is each event?", "Likelihood", r.sample(evs, 4), o="O1", extra=W)
def l4(r):
    return OD("Put the words in order from least likely to most likely.", W, o="O1")
def l5(r):
    a, b = r.randint(1, 9), r.randint(1, 9)
    if a == b: return None
    c = "red" if a > b else "blue"
    return MC(f"A box has {a} red and {b} blue pens. Which colour are you more likely to pick?", c, ["blue" if c == "red" else "red", "they are equally likely"], o="O1")
def l6(r):
    lab = r.choices(COL[:3], k=6); cs = sorted([lab.count(x) for x in COL[:3]])
    if cs[-1] == cs[-2]: return None
    k = max(COL[:3], key=lab.count)
    return S("Which colour is the spinner most likely to land on?", [k, k.capitalize()], o="O1", fig={"kind": "spinner", "labels": lab})
def l7(r):
    n = r.randint(4, 10)
    return N(f"A bag has {n} cubes. How many must be green so that picking green has an even chance?", n // 2, "cubes", units=["cubes"], o="O1", d="H") if n % 2 == 0 else None
def l8(r):
    a = r.randint(1, 5); b = r.randint(a + 1, a + 6)
    return N(f"A bag has {a} red and {b} blue counters. How many red counters must be added so that red and blue are equally likely?", b - a, "counters", units=["counters"], o="O1", d="H")


s.std([l1, l6, l2, l3, l4, l5, l7, l8], EX("Explain why picking red from 5 red and 5 blue counters has an even chance.", [("there are the same number of red and blue", "same|equal|5 and 5"), ("so red and blue are equally likely", "equally|half")], "There are 5 red and 5 blue counters, the same number of each. Red and blue are equally likely, so red has an even chance.", o="O1"))

s = U.section("4.2", "Chance experiments", ["O2"])
s.idea("Doing an experiment", ["In a **chance experiment** we repeat something, like spinning a spinner, and **record** what happens in a tally chart or table.",
       "If the outcomes are **equally likely**, they should come up about the same number of times — but not exactly the same."], table={"head": ["Colour", "red", "blue", "green"], "rows": [["Times", "11", "9", "10"]]})
s.check(N("A coin is flipped 30 times. About how many heads would you expect?", 15, "heads", units=["heads"], o="O2"))
s.mistake("Not exactly", ["A fair coin flipped 10 times might give 6 heads. That does not mean it is unfair."])


def x1(r):
    t = pick(r, [20, 40, 50, 60, 100])
    return N(f"A fair coin is flipped {t} times. About how many tails would you expect?", t // 2, "tails", units=["tails"], o="O2")
def x2(r):
    cs = [r.randint(2, 15) for _ in range(3)]; k = r.randrange(3)
    return N(f"The table shows spinner results. How many times did it land on {COL[k]}?", cs[k], o="O2", data={"head": ["Colour", *COL[:3]], "rows": [["Times", *map(str, cs)]]})
def x3(r):
    cs = [r.randint(2, 15) for _ in range(3)]
    return N("How many spins were there altogether?", sum(cs), "spins", units=["spins"], o="O2", data={"head": ["Colour", *COL[:3]], "rows": [["Times", *map(str, cs)]]})
def x4(r):
    xs = r.choices(["H", "T"], k=12)
    return TB(f"Coin results: {' '.join(xs)}. Complete the table.", ["Result", "Frequency"], [["Heads (H)", B(xs.count("H"))], ["Tails (T)", B(xs.count("T"))]], o="O2")
def x5(r):
    cs = r.sample(range(2, 14), 4); k = cs.index(max(cs))
    return S("The bar chart shows the results of spinning a spinner. Which colour came up most?", [COL[k], COL[k].capitalize()], o="O2", fig={"kind": "barchart", "labels": COL, "values": cs, "ymax": 14, "step": 2, "ylabel": "Times"})
def x6(r):
    t = pick(r, [12, 18, 24, 30]); f = r.randint(1, 6)
    return N(f"A fair dice is rolled {t} times. About how many times would you expect a {f}?", t // 6, "times", units=["times"], o="O2", d="H")
def x7(r):
    h = r.randint(5, 15)
    return MC(f"A coin was flipped 20 times and gave {h} heads. Is the coin probably fair?", "Yes, the result is close to 10" if 6 <= h <= 14 else "Maybe not, the result is far from 10", ["No, it must be exactly 10", "Yes, coins always give 20 heads"], o="O2", d="H")
def x8(r):
    cs = r.sample(range(2, 14), 3); i, j = r.sample(range(3), 2); a, b = (i, j) if cs[i] > cs[j] else (j, i)
    return N(f"How many more times did {COL[a]} come up than {COL[b]}?", cs[a] - cs[b], "times", units=["times"], o="O2", data={"head": ["Colour", *COL[:3]], "rows": [["Times", *map(str, cs)]]})


s.std([x2, x5, x1, x3, x4, x8, x6, x7], EX("Explain why a fair spinner with 3 equal colours might not land on each colour the same number of times.", [("each spin is down to chance", "chance|random"), ("results vary, but should be close over many spins", "vary|close|about the same|more spins")], "Each spin is random, so the results vary. Over many spins each colour should come up about the same number of times, but not exactly.", o="O2"))

U.mindmap(("Likelihood", "Impossible → unlikely → even chance → likely → certain", "O1", "4.1"), ("Experiments", "Record results • equally likely outcomes", "O2", "4.2"))
