# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 8 Probability (8.1 Likelihood, 8.2 Experiments and simulations).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(8, "Probability", "Statistics and probability",
         "Describing how likely events are, equally likely outcomes, and carrying out chance experiments and comparing their results with predictions.",
         {"O1": {"code": "5Sp.01", "sec": "8.1", "codeNote": "", "t": "Use the language of chance to describe and compare how likely events are."},
          "O2": {"code": "5Sp.02", "sec": "8.2", "codeNote": "", "t": "Carry out chance experiments and simulations, record the results and compare them with predictions."}})
WORDS = ["impossible", "unlikely", "even chance", "likely", "certain"]
COL = ["red", "blue", "green", "yellow"]


def word(p):
    return "impossible" if p == 0 else "certain" if p == 1 else "even chance" if p == Fr(1, 2) else "unlikely" if p < Fr(1, 2) else "likely"


s = U.section("8.1", "Likelihood", ["O1"])
s.idea("Words for chance", ["We describe how likely something is with words: **impossible, unlikely, even chance, likely, certain**.",
       "Events with an **even chance** are as likely to happen as not, like a coin landing on heads."],
       fig={"kind": "numline", "min": 0, "max": 1, "minor": 4, "ticks": [[0.5, "even chance"]]})
s.check(MC("How likely is it that the sun will rise tomorrow?", "certain", [("likely", ""), ("even chance", "")], o="O1"))
s.check(MC('Before you read on: a bag has 3 red and 1 blue ball. Which colour is more likely?', 'Red', [('Blue', 'There are more red balls.'), ('Equally likely', '3 red, 1 blue.')], o='O1'))
s.mistake("Unlikely is not impossible", ["Rolling a 6 is unlikely, but it can still happen."])


def l1(r):
    n = pick(r, [4, 6, 8]); k = r.randint(0, n); lab = ["R"] * k + ["B"] * (n - k)
    p = Fr(k, n)
    return MC(f"The spinner has {k} red (R) sections out of {n}. How likely is red?", word(p), [w for w in WORDS if w != word(p)][:3], o="O1", fig={"kind": "spinner", "labels": lab})
def l2(r):
    evs = [("a dice shows a number from 1 to 6", "certain"), ("a dice shows 7", "impossible"), ("a coin lands on tails", "even chance"), ("a dice shows a 1", "unlikely"),
           ("a dice shows more than 1", "likely"), ("you pick a blue cube from a bag of only red cubes", "impossible"), ("a dice shows an odd number", "even chance"), ("it will be Monday after Sunday", "certain")]
    return GD("How likely is each event?", "Likelihood", r.sample(evs, 4), o="O1", extra=WORDS)
def l3(r):
    a, b = r.randint(1, 9), r.randint(1, 9)
    if a == b: return None
    c = "red" if a > b else "blue"
    return MC(f"A bag has {a} red and {b} blue counters. Which colour is more likely to be picked?", c, ["blue" if c == "red" else "red", "they are equally likely"], o="O1")
def l4(r):
    a = r.randint(1, 6)
    return MC(f"A bag has {a} red and {a} blue counters. Which is true?", "red and blue are equally likely", ["red is more likely", "blue is more likely", "red is impossible"], o="O1")
def l5(r):
    return OD("Put the events in order from least likely to most likely.", ["rolling 0 on a dice", "rolling a 6 on a dice", "getting heads on a coin", "rolling less than 6 on a dice", "rolling a number from 1 to 6"], o="O1", d="H")
def l6(r):
    n = pick(r, [5, 6, 8]); lab = r.choices(COL[:3], k=n)
    c = max(COL[:3], key=lab.count)
    if sorted([lab.count(x) for x in COL[:3]])[-1] == sorted([lab.count(x) for x in COL[:3]])[-2]: return None
    return S("Which colour is the spinner most likely to land on?", [c, c.capitalize()], o="O1", fig={"kind": "spinner", "labels": lab})
def l7(r):
    k = r.randint(1, 5)
    return MC(f"A bag has {k} green counters and nothing else. How likely is it to pick a green counter?", "certain", ["likely", "even chance", "impossible"], o="O1")
def l8(r):
    t = r.randint(4, 9)
    return N(f"A bag has {t} counters. How many must be red so that picking red has an even chance?", t // 2, "counters", units=["counters"], o="O1", d="H") if t % 2 == 0 else None


s.std([l1, l6, l2, l3, l4, l7, l5, l8], EX("Explain why getting a 1 on a dice is unlikely but not impossible.", [("there is only one 1 out of 6 numbers", "one|1 out of 6|six"), ("it can still happen", "can happen|possible|could")], "A dice has 6 numbers and only one of them is a 1, so it is unlikely. But it can still happen, so it is not impossible.", o="O1"))

s = U.section("8.2", "Experiments and simulations", ["O2"])
s.idea("Testing predictions", ["In a **chance experiment** we repeat something many times and record the results in a **tally chart**.",
       "If you flip a coin 20 times you might predict 10 heads. The real result may be a little different, like 12 heads. The more times you repeat, the closer results usually get to the prediction."],
       table={"head": ["Outcome", "Tally", "Frequency"], "rows": [["Heads", "|||| |||| ||", "12"], ["Tails", "|||| |||", "8"]]})
s.check(N("A coin is flipped 40 times. About how many heads would you expect?", 20, "heads", units=["heads"], o="O2"))
s.check(MC('Before you read on: you flip a coin 10 times. Will you get exactly 5 heads?', 'Not always', [('Yes, always', 'Results vary by chance.'), ('Never', '5 heads can happen.')], o='O2'))
s.mistake("Results vary", ["Getting 7 heads in 10 flips does not mean the coin is unfair. Small experiments vary a lot."])


def x1(r):
    t = pick(r, [20, 30, 40, 60, 100])
    return N(f"A fair coin is flipped {t} times. About how many tails would you expect?", t // 2, "tails", units=["tails"], o="O2")
def x2(r):
    t = pick(r, [12, 18, 30, 60])
    return N(f"A fair dice is rolled {t} times. About how many times would you expect a 4?", t // 6, "times", units=["times"], o="O2", d="H")
def x3(r):
    cs = [r.randint(2, 12) for _ in range(3)]; k = r.randrange(3)
    return N(f"The table shows the results of picking a counter and putting it back. How many times was {COL[k]} picked?", cs[k], o="O2", data={"head": ["Colour", *COL[:3]], "rows": [["Frequency", *map(str, cs)]]})
def x4(r):
    cs = [r.randint(2, 12) for _ in range(3)]
    return N("The table shows the results of an experiment. How many goes were there altogether?", sum(cs), "goes", units=["goes"], o="O2", data={"head": ["Colour", *COL[:3]], "rows": [["Frequency", *map(str, cs)]]})
def x5(r):
    cs = [r.randint(2, 15) for _ in range(4)]
    if len(set(cs)) < 4: return None
    k = cs.index(max(cs))
    return S("A spinner was spun many times. The bar chart shows the results. Which colour came up most?", [COL[k], COL[k].capitalize()], o="O2", fig={"kind": "barchart", "labels": COL, "values": cs, "ymax": 16, "step": 2, "ylabel": "Frequency"})
def x6(r):
    h = r.randint(5, 15)
    return TB(f"A coin was flipped 20 times and landed on heads {h} times. Complete the table.", ["Outcome", "Frequency"], [["Heads", B(h)], ["Tails", B(20 - h)]], o="O2")
def x7(r):
    h = r.randint(6, 14)
    return MC(f"A coin was flipped 20 times and gave {h} heads. Is the coin likely to be fair?", "Yes, the result is close to 10", ["No, it should be exactly 10", "No, coins never land on heads"], o="O2", d="H")
def x8(r):
    t = pick(r, [50, 100]); red = r.randint(5, 45)
    return MC(f"In {t} picks from a bag, red came up {red} times. Which is the best conclusion?", "red is unlikely" if red < t / 2 - 5 else "red is likely" if red > t / 2 + 5 else "red has about an even chance", ["red is impossible", "red is certain"], o="O2", d="H")


s.std([x3, x5, x1, x2, x4, x6, x7, x8], EX("Explain why flipping a coin 10 times might not give exactly 5 heads.", [("each flip is random / down to chance", "random|chance|each flip"), ("results vary; more flips get closer to half", "vary|more flips|closer|not always")], "Each flip happens by chance, so results vary. 5 heads is only what we expect on average. With more flips the results usually get closer to half.", o="O2"))

U.mindmap(("Likelihood", "Impossible • unlikely • even chance • likely • certain", "O1", "8.1"), ("Experiments", "Tally results • compare with predictions", "O2", "8.2"))
