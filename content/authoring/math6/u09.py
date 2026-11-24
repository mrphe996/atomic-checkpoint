# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 9 Probability (9.1 Describing and predicting likelihood).
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(9, "Probability", "Statistics and probability",
         "Describing likelihood with words and on a scale, equally likely outcomes, mutually exclusive events, and predicting from experiments.",
         {"O1": {"code": "6Sp.01", "sec": "9.1", "codeNote": "", "t": "Use the language of chance and place events on a likelihood scale from impossible to certain."},
          "O2": {"code": "6Sp.02", "sec": "9.1", "codeNote": "", "t": "Recognise equally likely outcomes and mutually exclusive events, and predict outcomes from experiments."}})
TOL = 1e-6
WORDS = ["impossible", "unlikely", "even chance", "likely", "certain"]


def P(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}"), **kw)


def word(p):
    return "impossible" if p == 0 else "certain" if p == 1 else "even chance" if p == Fr(1, 2) else "unlikely" if p < Fr(1, 2) else "likely"


s = U.section("9.1", "Describing and predicting likelihood", ["O1", "O2"])
s.idea("The likelihood scale", ["How likely something is can be described as **impossible, unlikely, even chance, likely** or **certain**.",
       "On a scale from 0 to 1, impossible is 0, even chance is 1/2 and certain is 1."], fig={"kind": "numline", "min": 0, "max": 1})
s.check(MC("A normal dice is rolled. How likely is it to show a 7?", "impossible", [("unlikely", ""), ("even chance", "")], o="O1"))
s.idea("Equally likely outcomes", ["A fair spinner with 4 equal sections has 4 **equally likely** outcomes. The chance of landing on one section is 1/4.",
       "**Mutually exclusive** events cannot happen at the same time: a dice cannot show 2 and 5 at once."], fig={"kind": "spinner", "labels": ["A", "B", "C", "D"]})
s.idea("Experiments", ["If you repeat an experiment many times, the results help you **predict**. If a red counter is picked 30 times out of 100, red is probably about 3/10 of the counters."])
s.mistake("Even chance", ["'Even chance' means 1/2 – it is not the same as 'likely'."])
COL = ["red", "blue", "green", "yellow"]


def p1(r):
    n = pick(r, [3, 4, 5, 6, 8]); lab = [str(i + 1) for i in range(n)]
    return P(f"This fair spinner has {n} equal sections. What is the chance of landing on 1?", Fr(1, n), o="O2", fig={"kind": "spinner", "labels": lab})
def p2(r):
    n = pick(r, [4, 6, 8]); k = r.randint(1, n - 1); lab = ["R"] * k + ["B"] * (n - k)
    p = Fr(k, n)
    return MC(f"The spinner has {k} red (R) sections out of {n}. How likely is it to land on red?", word(p), [w for w in WORDS if w != word(p)][:3], o="O1", fig={"kind": "spinner", "labels": lab})
def p3(r):
    evs = [("a dice shows a number less than 7", "certain"), ("a dice shows 0", "impossible"), ("a coin lands on heads", "even chance"), ("a dice shows a 6", "unlikely"), ("a dice shows a number bigger than 1", "likely"),
           ("it gets dark tonight", "certain"), ("you pick a red card from a pack of all blue cards", "impossible"), ("a dice shows an even number", "even chance")]
    ch = r.sample(evs, 4)
    return GD("Describe how likely each event is.", "Likelihood", ch, o="O1", extra=WORDS)
def p4(r):
    a, b = r.randint(1, 6), r.randint(1, 6)
    return P(f"A bag has {a} red and {b} blue counters. One is taken without looking. What is the chance it is red?", Fr(a, a + b), o="O2")
def p5(r):
    n = pick(r, [6, 8, 10]); k = r.randint(1, n - 1)
    return P(f"A bag has {n} cards numbered 1 to {n}. What is the chance of picking a number greater than {k}?", Fr(n - k, n), o="O2", d="H")
def p6(r):
    t = pick(r, [20, 40, 50, 100]); res = r.randint(2, 8); c = t * res // 10
    return N(f"A counter is picked from a bag and put back {t} times. Red came up {c} times. About how many times would you expect red in {t * 5} goes?", c * 5, "times", units=["times"], o="O2", d="H")
def p7(r):
    a = r.sample(range(1, 7), 2)
    return MC(f"A dice is rolled once. Which pair of events are mutually exclusive?", f"getting {a[0]} and getting {a[1]}", [f"getting an even number and getting {2 * (a[0] % 3 + 1)}", "getting more than 2 and getting less than 5", "getting an odd number and getting 3"], o="O2", d="H")
def p8(r):
    n = pick(r, [10, 20, 50]); cs = [r.randint(1, 9) for _ in range(3)]; t = sum(cs)
    k = r.randrange(3)
    return N(f"The table shows {t} picks from a bag. How many times was {COL[k]} picked?", cs[k], o="O2", data={"head": ["Colour", *COL[:3]], "rows": [["Times", *map(str, cs)]]})
def p9(r):
    t = r.randint(3, 10)
    return OD("Put these events in order, least likely first.", ["a dice shows 9", "a dice shows a 3", "a coin lands on tails", "a dice shows a number from 1 to 6"], o="O1")
def p10(r):
    n = pick(r, [4, 5, 6, 8]); lab = [COL[i % 2] for i in range(n)]
    return MC(f"Is this spinner fair for two players, one who wins on red and one on blue?", "Yes, red and blue are equally likely" if n % 2 == 0 else "No, red is more likely", ["No, red is more likely" if n % 2 == 0 else "Yes, red and blue are equally likely", "No, blue is more likely"], o="O2", fig={"kind": "spinner", "labels": lab})


s.std([p1, p8, p2, p3, p4, p5, p6, p9, p7, p10], EX("Explain why the chance of rolling a 3 on a fair dice is 1/6.", [("there are 6 equally likely outcomes", "6|six|equally likely"), ("only one of them is a 3", "one|1 of|only")], "A fair dice has 6 equally likely outcomes (1 to 6) and only one of them is a 3, so the chance is 1/6.", o="O2"), adv=[p5, p6, p7, p4, p10])

U.mindmap(("Likelihood", "Impossible • unlikely • even chance • likely • certain", "O1", "9.1"), ("Equally likely", "Fair spinner • dice • 1/n chance", "O2", "9.1"), ("Experiments", "Results help predict", "O2", "9.1"))
