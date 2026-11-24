# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 13 Probability (13.1 The probability scale, 13.2 Mutually exclusive outcomes,
13.3 Experimental probabilities). Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(13, "Probability", "Statistics and probability",
         "The language of chance and the 0 to 1 probability scale, equally likely outcomes, mutually exclusive outcomes, and probabilities from experiments.",
         {"O1": {"code": "7Sp.01", "sec": "13.1", "codeNote": "", "t": "Use the language of chance and the probability scale from 0 to 1."},
          "O2": {"code": "7Sp.02", "sec": "13.2", "codeNote": "", "t": "Find probabilities of equally likely outcomes and use the fact that mutually exclusive outcomes add up to 1."},
          "O3": {"code": "7Sp.03", "sec": "13.3", "codeNote": "", "t": "Find experimental probabilities from repeated trials and compare them with expected results."}})
TOL = 1e-6


def P(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction or a decimal.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}"), **kw)


COLS = ["red", "blue", "green", "yellow"]

# ================================================================== 13.1
s = U.section("13.1", "The probability scale", ["O1"])
s.idea("From 0 to 1", ["Probability measures how likely something is, on a scale from **0** (impossible) to **1** (certain). **½** is an even chance.",
       "Words: impossible, unlikely, even chance, likely, certain."], fig={"kind": "numline", "min": 0, "max": 1})
s.check(MC("What is the probability of an impossible event?", "0", ["1", "½", "−1"], o="O1"))
s.mistake("Never above 1", ["A probability cannot be bigger than 1 or less than 0."])
EV = [("Rolling a 7 on a normal dice", "Impossible"), ("Rolling a number less than 7 on a normal dice", "Certain"), ("Getting a head when you toss a coin", "Even chance"),
      ("Rolling a 6 on a normal dice", "Unlikely"), ("Rolling a number bigger than 1 on a dice", "Likely"), ("Picking a red sock from a drawer of only blue socks", "Impossible")]


def l1(r):
    return GD("Describe the chance of each event.", "Chance", r.sample(EV, 4), o="O1", extra=["Impossible", "Unlikely", "Even chance", "Likely", "Certain"])
def l2(r):
    e, w = pick(r, EV)
    return MC(f"Which word describes the chance of this event? {e}", w, [x for x in ["Impossible", "Unlikely", "Even chance", "Likely", "Certain"] if x != w][:3], o="O1")
def l3(r):
    v = pick(r, [0.9, 0.1, 0.5, 0.75, 0.25, 0.05, 1, 0])
    w = "Impossible" if v == 0 else "Certain" if v == 1 else "Even chance" if v == 0.5 else "Likely" if v > 0.5 else "Unlikely"
    return MC(f"An event has probability {fmt(v)}. How likely is it?", w, [x for x in ["Impossible", "Unlikely", "Even chance", "Likely", "Certain"] if x != w][:3], o="O1", fig={"kind": "numline", "min": 0, "max": 1})
def l4(r):
    return MS("Select ALL the numbers that could be probabilities.", [fmt(r.randint(1, 9) / 10), "0", "1"], ["1.5", "−0.2"], o="O1")
def l5(r):
    a, b = r.sample([0.1, 0.25, 0.4, 0.5, 0.65, 0.8, 0.95], 2)
    return MC(f"Event A has probability {fmt(a)}. Event B has probability {fmt(b)}. Which is more likely?", "A" if a > b else "B", ["B" if a > b else "A", "They are equally likely"], o="O1")
def l6(r):
    n = r.randint(2, 10)
    return P(f"A bag has {n} red balls and nothing else. What is the probability of picking a red ball?", 1, o="O1")
def l7(r):
    vs = sorted(r.sample([0.05, 0.2, 0.35, 0.5, 0.7, 0.9], 4))
    return OD("Put these probabilities in order, least likely first.", [fmt(v) for v in vs], o="O1")


s.std([l1, l3, l2, l4, l5, l6, l7], EX("Explain why a probability can never be more than 1.", [("1 means certain", ["certain|definitely|always"]), ("nothing can be more likely than certain", ["more than certain|nothing|can't be more|cannot be more"])], "A probability of 1 means the event is certain to happen. Nothing can be more likely than certain, so a probability can never be more than 1.", o="O1"))

# ================================================================== 13.2
s = U.section("13.2", "Mutually exclusive outcomes", ["O2"])
s.idea("Equally likely outcomes", ["When outcomes are equally likely: **P(event) = number of ways it can happen ÷ total number of outcomes**.",
       "Outcomes that cannot happen together are **mutually exclusive**. The probabilities of all of them add up to **1**, so **P(not A) = 1 − P(A)**."])
s.check(P("A fair dice is rolled. What is the probability of an even number?", Fr(1, 2), o="O2"))
s.mistake("Total outcomes", ["Count ALL the outcomes in the bottom of the fraction."])


def m1(r):
    n = [r.randint(1, 9) for _ in range(3)]; c = r.sample(COLS, 3); k = r.randrange(3)
    return P(f"A bag has {n[0]} {c[0]}, {n[1]} {c[1]} and {n[2]} {c[2]} counters. One is picked at random. Find P({c[k]}).", Fr(n[k], sum(n)), o="O2", data={"head": ["Colour", *c], "rows": [["Counters", *map(str, n)]]})
def m2(r):
    p = r.randint(1, 9) / 10
    return N(f"The probability that a bus is late is {fmt(p)}. What is the probability that it is not late?", round(1 - p, 2), o="O2", tol=TOL)
def m3(r):
    ev = pick(r, [("a 3", 1), ("an odd number", 3), ("a number greater than 4", 2), ("a multiple of 3", 2), ("a factor of 4", 3)])
    return P(f"A fair six-sided dice is rolled. Find P({ev[0]}).", Fr(ev[1], 6), o="O2")
def m4(r):
    a, b = r.randint(1, 5) / 10, r.randint(1, 3) / 10; c = round(1 - a - b, 2)
    return TB("A spinner can land on red, blue or green. Find the missing probability.", ["Colour", "Probability"], [["Red", fmt(a)], ["Blue", fmt(b)], ["Green", B(c)]], o="O2")
def m5(r):
    n = r.randint(4, 10); lab = [str(i) for i in range(1, n + 1)]
    return P(f"A fair spinner has {n} equal sections numbered 1 to {n}. Find P(an even number).", Fr(n // 2, n), o="O2", fig={"kind": "spinner", "labels": lab})
def m6(r):
    w = pick(r, ["APPLE", "BANANA", "SCHOOL", "PROBABILITY", "MATHS", "LETTER"]); ch = pick(r, sorted(set(w)))
    return P(f"A letter is picked at random from the word {w}. Find P({ch}).", Fr(w.count(ch), len(w)), o="O2")
def m7(r):
    return MC("Which pair of outcomes is mutually exclusive when you roll one dice?", "getting a 2 and getting a 5", ["getting an even number and getting a 2", "getting a number less than 4 and getting a 3", "getting an odd number and getting a 5"], o="O2", d="H")
def m8(r):
    n = r.randint(20, 50); k = r.randint(1, 5)
    return P(f"There are {n} raffle tickets. Ravi buys {k}. What is the probability he wins?", Fr(k, n), o="O2")


def m9(r):
    n, k = r.randint(10, 30), r.randint(2, 5)
    return P(f"Cards numbered 1 to {n} are shuffled. One card is taken. Find P(a multiple of {k}).", Fr(n // k, n), o="O2")
def m10(r):
    g, b = r.randint(3, 15), r.randint(3, 15)
    return P(f"In a class of {g + b} students, {g} are girls. The teacher chooses one student at random. Find P(boy).", Fr(b, g + b), o="O2")
def m11(r):
    d = pick(r, [("a weekday", 5, 7), ("a day starting with T", 2, 7), ("a month with 31 days", 7, 12), ("a month starting with J", 3, 12)])
    return P(f"A {'day of the week' if d[2] == 7 else 'month of the year'} is chosen at random. Find P({d[0]}).", Fr(d[1], d[2]), o="O2", d="H")


s.std([m1, m4, m2, m3, m5, m6, m7, m8, m9, m10, m11], EX("Explain why P(not red) = 1 − P(red).", [("a counter is either red or not red", ["either|or not"]), ("the two probabilities add up to 1", ["add.*1|total.*1|sum.*1"])], "Every counter picked is either red or not red, and these outcomes are mutually exclusive, so their probabilities add up to 1. So P(not red) = 1 − P(red).", o="O2"))

# ================================================================== 13.3
s = U.section("13.3", "Experimental probabilities", ["O3"])
s.idea("From experiments", ["**Experimental probability** = number of times an event happens ÷ number of trials.",
       "The **expected** number = probability × number of trials. A fair coin tossed 50 times: expect about 25 heads. More trials give a better estimate."])
s.check(N("A coin is tossed 40 times and lands heads 18 times. What is the experimental probability of heads? Give a decimal.", 0.45, o="O3"))
s.mistake("Results vary", ["Experimental results are not always exactly what you expect."])


def x1(r):
    n = pick(r, [20, 25, 40, 50, 100]); k = r.randint(n // 10, n * 9 // 10)
    return N(f"A drawing pin is dropped {n} times and lands point up {k} times. Find the experimental probability of point up. Give a decimal.", round(k / n, 4), o="O3", tol=TOL)
def x2(r):
    n = pick(r, [30, 60, 120, 300])
    return N(f"A fair dice is rolled {n} times. How many 4s would you expect?", n // 6, o="O3")
def x3(r):
    n = pick(r, [20, 50, 100, 200])
    return N(f"A fair coin is tossed {n} times. How many tails would you expect?", n // 2, o="O3")
def x4(r):
    f = [r.randint(5, 25) for _ in range(4)]; c = ["Red", "Blue", "Green", "Yellow"]; k = r.randrange(4)
    return N(f"A spinner was spun {sum(f)} times. Find the experimental probability of {c[k].lower()}. Give a decimal to 2 d.p.", round(f[k] / sum(f), 2), o="O3", tol=0.006, data={"head": ["Colour", *c], "rows": [["Frequency", *map(str, f)]]})
def x5(r):
    f = [r.randint(5, 25) for _ in range(3)]; c = ["Heads", "Tails", "Edge"][:2]
    t = f[0] + f[1]
    return TB(f"A coin was tossed {t} times. Complete the experimental probabilities (2 d.p.).", ["Outcome", "Probability"], [["Heads", B(round(f[0] / t, 2), 0.006)], ["Tails", B(round(f[1] / t, 2), 0.006)]], o="O3", data={"head": ["Outcome", "Heads", "Tails"], "rows": [["Frequency", str(f[0]), str(f[1])]]})
def x6(r):
    a, b = r.randint(10, 20), r.randint(200, 500)
    return MC(f"Lily rolls a dice {a} times; Kofi rolls it {b} times. Whose results are likely to be closer to the expected results?", "Kofi's", ["Lily's", "They will be identical", "Neither"], o="O3")
def x7(r):
    n, k, m = pick(r, [(50, 10, 500), (20, 5, 200), (40, 12, 400), (100, 30, 1000)])
    return N(f"In {n} trials a spinner landed on blue {k} times. Estimate how many times it lands on blue in {m} trials.", k * m // n, o="O3", d="H")


def x8(r):
    n = pick(r, [60, 120, 180]); o = n // 6 + r.randint(-8, 8)
    return N(f"A fair dice was rolled {n} times and showed a 1 {o} times. What is the difference between this and the expected number of 1s?", abs(o - n // 6), o="O3", d="H")
def x9(r):
    k, n = r.randint(3, 17), 20
    return N(f"A basketball player scored {k} out of {n} shots. Estimate the probability that she scores her next shot, as a percentage.", k / n * 100, "%", units=["%"], o="O3", tol=TOL)


s.std([x4, x5, x1, x2, x3, x6, x7, x8, x9], EX("Explain why tossing a coin 10 times might not give 5 heads.", [("each toss is random / chance", ["chance|random|luck"]), ("5 is only the expected number; results vary", ["expect|vary|average"])], "Each toss depends on chance, so results vary. 5 heads is only what you expect on average; with 10 tosses you might get 3, 4, 6 or 7.", o="O3"))

U.mindmap(("Probability scale", "0 impossible • ½ even chance • 1 certain", "O1", "13.1"), ("Equally likely outcomes", "Ways ÷ total • P(not A) = 1 − P(A)", "O2", "13.2"),
          ("Experiments", "Times ÷ trials • expected = P × trials", "O3", "13.3"))
