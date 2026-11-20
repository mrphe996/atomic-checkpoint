# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 12 Probability. Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(12, "Probability", "Statistics and probability",
         "Mutually exclusive events, independent events, combined events with sample spaces and tree diagrams, and chance experiments.",
         {"O1": {"sec": "12.1", "code": "9Sp.01", "codeNote": "", "t": "Understand mutually exclusive events and use the fact that their probabilities add to 1 when they cover all outcomes."},
          "O2": {"sec": "12.2", "code": "9Sp.02", "codeNote": "", "t": "Understand independent events and multiply their probabilities."},
          "O3": {"sec": "12.3", "code": "9Sp.03", "codeNote": "", "t": "Find probabilities of combined events using sample-space diagrams, lists and tree diagrams."},
          "O4": {"sec": "12.4", "code": "9Sp.04", "codeNote": "", "t": "Carry out chance experiments, find relative frequency and compare it with theoretical probability."}})

def P(prompt, f, **kw):
    """a probability answer: accepted as a fraction or a decimal"""
    f = Fr(f); kw.setdefault("hint", "Give the probability as a fraction (e.g. 3/8) or a decimal.")
    return N(prompt, float(f), tol=0.0015, **kw)

# ================================================================== 12.1
s = U.section("12.1", "Mutually exclusive events", ["O1"])
s.idea("Mutually exclusive", ["Events are **mutually exclusive** if they **cannot happen at the same time**: rolling a 2 and rolling a 5 on one dice.",
       "For mutually exclusive events, **P(A or B) = P(A) + P(B)**. If the events cover every outcome, their probabilities **add up to 1**, so **P(not A) = 1 − P(A)**."])
s.example("Missing probability", "A bag has red, blue and green counters only. P(red) = 0.35, P(blue) = 0.4. Find P(green).", [("probabilities add to 1", ""), ("1 − 0.35 − 0.4 = 0.25", "")], "0.25")
s.check(P("P(rain tomorrow) = 0.38. Find P(no rain tomorrow).", Fr(62, 100), o="O1"))
s.mistake("Not mutually exclusive", ["Rolling an even number and rolling a number bigger than 3 can happen together (4 or 6), so you cannot just add their probabilities."])
s.check(MC("Which pair of events is mutually exclusive when one card is taken from 1–10?", "an odd number and a multiple of 2", [("an odd number and a prime number", "3, 5 and 7 are both."), ("a multiple of 3 and a multiple of 2", "6 is both."), ("less than 5 and a square number", "1 and 4 are both.")], o="O1"))
def m1(r):
    ps = [r.randint(5, 40) for _ in range(3)]
    if sum(ps) >= 95: return None
    cols = r.sample(["red", "blue", "green", "yellow", "white", "black"], 4)
    tab = {"head": ["Colour"] + cols, "rows": [["Probability"] + [fmt(p / 100) for p in ps] + ["x"]]}
    return N("A spinner can only land on these colours. Find x.", (100 - sum(ps)) / 100, o="O1", data=tab, tol=1e-6)
def m2(r):
    a, b = r.randint(1, 6), r.randint(1, 6); n = a + b + r.randint(2, 8)
    return P(f"A bag has {a} red, {b} blue and {n-a-b} white beads. One is picked at random. Find P(red or blue).", Fr(a + b, n), o="O1")
def m3(r):
    p = r.randint(10, 60); k = r.randint(2, 4)
    rest = 100 - p
    if rest % (k + 1): return None
    return N(f"A spinner lands on A, B or C. P(A) = {p/100}. B is {k} times as likely as C. Find P(C).", rest / (k + 1) / 100, o="O1", d="H", tol=1e-6)
def m4(r):
    rows = [("Rolling a 1 and rolling a 6 on one dice", "Yes"), ("Rolling an even number and a prime number on one dice", "No"), ("Picking a heart and a king from one card", "No"),
            ("Getting heads and tails on one coin", "Yes"), ("Picking a vowel and a consonant from one letter", "Yes"), ("Picking a square number and an odd number from 1–9", "No")]
    return GD("Are the events mutually exclusive?", "Mutually exclusive?", r.sample(rows, 4), o="O1")
def m5(r):
    n = r.randint(20, 60); p = r.randint(10, 45)
    return N(f"The probability that a train is late is {p/100}. Out of {n*5} trains, how many would you expect NOT to be late?", round((1 - p / 100) * n * 5, 2), "trains", units=["trains"], o="O1", tol=0.01)
def m6(r):
    nums = list(range(1, r.choice([10, 12, 15, 20]) + 1)); n = len(nums)
    k1, k2 = pick(r, [(3, 5), (4, 5), (4, 7), (5, 6), (3, 7)])
    both = [x for x in nums if x % k1 == 0 or x % k2 == 0]
    return P(f"A card is picked from cards numbered 1 to {n}. Find P(multiple of {k1} or multiple of {k2}).", Fr(len(both), n), o="O1", d="H")
s.core(m1(s.rng) or m1(s.rng) or m1(s.rng), m2(s.rng), m3(s.rng) or N("A spinner lands on A, B or C. P(A) = 0.4. B is twice as likely as C. Find P(C).", 0.2, o="O1", d="H", tol=1e-6), m4(s.rng), m5(s.rng), m6(s.rng),
       MS("Which statements are true for one roll of a fair six-sided dice?", ["P(even) + P(odd) = 1", "Rolling 2 and rolling 3 are mutually exclusive"], ["P(less than 4) + P(more than 2) = 1", "Rolling even and rolling 6 are mutually exclusive"], o="O1", d="H"),
       EX("Explain why P(not A) = 1 − P(A).", [("A and not A are mutually exclusive / cannot both happen", ["mutually exclusive|cannot both|can't both|not both"]), ("together they cover every outcome so add to 1", ["add|total|sum|1|one"])], "A and not A cannot both happen and together they cover every outcome, so their probabilities add to 1. So P(not A) = 1 − P(A).", o="O1"))
s.gen("p", 44, m1, m2, m3, m4, m5, m6)
s.gen("a", 8, m6, m3, lambda r: (lambda x: N(f"A bag has only red and blue balls. P(red) = 3/8. There are {x} more blue balls than red balls. How many balls are in the bag?", 4 * x, "balls", units=["balls"], o="O1", d="VH"))(r.randint(2, 12)))

# ================================================================== 12.2
s = U.section("12.2", "Independent events", ["O2"])
s.idea("Independent events", ["Events are **independent** if one does **not affect** the other: flipping a coin and rolling a dice.",
       "For independent events, **P(A and B) = P(A) × P(B)**."])
s.example("Multiply", "A fair coin is flipped and a fair dice is rolled. Find P(heads and a 6).", [("P(heads) = 1/2, P(6) = 1/6", ""), ("1/2 × 1/6 = 1/12", "")], "1/12")
s.check(P("P(Ali is late) = 0.2 and P(Bea is late) = 0.3, independently. Find P(both late).", Fr(6, 100), o="O2"))
s.mistake("And means multiply", ["'A and B' for independent events: MULTIPLY. 'A or B' for mutually exclusive events: ADD."])
s.check(MC("A counter is taken from a bag, NOT replaced, then a second is taken. Are the two picks independent?", "No, the first pick changes what is left", [("Yes, always", ""), ("Yes, if the counters are the same size", ""), ("No, because there are two picks", "")], o="O2", d="H"))
def i1(r):
    a, b = r.randint(1, 9) / 10, r.randint(1, 9) / 10
    ev = pick(r, [("it rains on Monday", "the bus is late"), ("Sam wins his match", "Tia wins her match"), ("a seed grows", "a second seed grows")])
    return N(f"P({ev[0]}) = {a} and P({ev[1]}) = {b}. The events are independent. Find P(both happen).", round(a * b, 4), o="O2", tol=1e-6)
def i2(r):
    a, b = r.randint(1, 9) / 10, r.randint(1, 9) / 10
    return N(f"P(A) = {a} and P(B) = {b}, independent. Find P(neither A nor B).", round((1 - a) * (1 - b), 4), o="O2", d="H", tol=1e-6)
def i3(r):
    n1, n2 = pick(r, [4, 5, 6, 8, 10]), pick(r, [2, 4, 6, 8]); x, y = r.randint(1, n1), r.randint(1, n2)
    return P(f"A fair {n1}-sided spinner (1 to {n1}) and a fair {n2}-sided spinner (1 to {n2}) are spun. Find P(first shows {x} and second shows {y}).", Fr(1, n1 * n2), o="O2", fig={"kind": "spinner", "labels": [str(i) for i in range(1, n1 + 1)]})
def i4(r):
    p = r.randint(1, 9) / 10; k = r.randint(2, 4)
    return N(f"The probability a biased coin lands heads is {p}. It is thrown {k} times. Find P(heads every time). (4 d.p.)", round(p ** k, 4), o="O2", d="H", tol=0.00006)
def i5(r):
    rows = [("Rolling a dice twice", "Independent"), ("Taking two cards without replacement", "Not independent"), ("Flipping a coin and spinning a spinner", "Independent"),
            ("Raining today and carrying an umbrella today", "Not independent"), ("Two different people's birthdays being on a Monday", "Independent"), ("Taking two sweets from a bag and eating the first", "Not independent")]
    return GD("Are the events independent?", "Independent?", r.sample(rows, 4), o="O2")
def i6(r):
    a, b = r.randint(2, 8), r.randint(2, 8)
    return P(f"Bag X has {a} red and {b} blue balls. Bag Y has {b} red and {a} blue balls. One ball is taken from each bag. Find P(both red).", Fr(a * b, (a + b) ** 2), o="O2", d="H")
def i7(r):
    a = r.randint(1, 9) / 10; ab = round(a * r.randint(1, 9) / 10, 2)
    return N(f"A and B are independent. P(A) = {a}, P(A and B) = {ab}. Find P(B).", round(ab / a, 4), o="O2", d="H", tol=0.0006)
s.core(i1(s.rng), i2(s.rng), i3(s.rng), i4(s.rng), i5(s.rng), i6(s.rng),
       TB("A fair dice is rolled and a fair coin is flipped. Complete the probabilities.", ["P(6 and heads)", "P(even and tails)", "P(not 6 and heads)"], [[B(1 / 12, 0.0015), B(0.25, 0.0015), B(5 / 12, 0.0015)]], o="O2", hint="Fractions or decimals are both fine."),
       EX("Explain the difference between independent and mutually exclusive events.", [("independent: one does not affect the other", ["affect|influence|depend"]), ("mutually exclusive: cannot happen together", ["cannot|can't|not.*same time|together"])], "Independent events do not affect each other. Mutually exclusive events cannot happen at the same time.", o="O2"))
s.gen("p", 44, i1, i2, i3, i4, i5, i6, i7)
s.gen("a", 8, i4, i7, lambda r: (lambda p: N(f"P(a light bulb fails in a year) = {p}. A lamp has 3 bulbs that fail independently. Find P(at least one fails). (4 d.p.)", round(1 - (1 - p) ** 3, 4), o="O2", d="VH", tol=0.00006))(r.randint(1, 30) / 100))

# ================================================================== 12.3
s = U.section("12.3", "Combined events", ["O3"])
s.idea("Sample spaces", ["A **sample-space diagram** shows every outcome of two events. For two dice there are 6 × 6 = **36** equally likely outcomes.",
       "Count the outcomes you want and divide by the total."],
       table={"caption": "Total of two dice", "head": ["+", "1", "2", "3", "4", "5", "6"], "rows": [[str(a)] + [str(a + b) for b in range(1, 7)] for a in range(1, 7)]})
s.check(P("Two fair dice are rolled. Find P(total is 8).", Fr(5, 36), o="O3"))
s.idea("Tree diagrams", ["On a **tree diagram**, multiply **along** the branches, then **add** the end results you want.",
       "Without replacement, the second-stage probabilities change because there is one fewer item."],
       fig={"kind": "tree", "a": [["R", "3/5"], ["B", "2/5"]], "b": [["R", "3/5"], ["B", "2/5"]], "outcomes": True})
s.example("Tree diagram", "From the tree, find P(one red and one blue).", [("P(RB) = 3/5 × 2/5 = 6/25", ""), ("P(BR) = 2/5 × 3/5 = 6/25", ""), ("add: 12/25", "")], "12/25")
s.check(P("From the tree in the lesson, find P(both blue).", Fr(4, 25), o="O3"))
def c1(r):
    k = r.randint(3, 11); cnt = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == k)
    which = pick(r, ["total is {k}", "total is more than {k}"])
    if "more" in which: cnt = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b > k)
    return P(f"Two fair dice are rolled and the scores added. Find P({which.format(k=k)}).", Fr(cnt, 36), o="O3")
def c2(r):
    k = pick(r, [2, 3, 4, 6, 12]); cnt = sum(1 for a in range(1, 7) for b in range(1, 7) if (a * b) % k == 0)
    return P(f"Two fair dice are rolled and the scores multiplied. Find P(product is a multiple of {k}).", Fr(cnt, 36), o="O3", d="H")
def c3(r):
    a, b = r.randint(2, 7), r.randint(2, 7); n = a + b; rep = r.random() < 0.5
    if rep: f = Fr(a, n) ** 2; txt = "replaced"
    else: f = Fr(a, n) * Fr(a - 1, n - 1); txt = "NOT replaced"
    return P(f"A bag has {a} red and {b} blue balls. A ball is taken and {txt}, then a second ball is taken. Find P(both red).", f, o="O3", d="H",
             fig={"kind": "tree", "a": [["R", f"{a}/{n}"], ["B", f"{b}/{n}"]], "b": [["R", "?"], ["B", "?"]]})
def c4(r):
    p = Fr(r.randint(1, 9), 10); q = Fr(r.randint(1, 9), 10)
    return TB(f"P(pass test 1) = {float(p)}, P(pass test 2) = {float(q)}, independently. Complete the probabilities.", ["Pass both", "Pass exactly one", "Pass neither"],
              [[B(float(p * q), 1e-6), B(float(p * (1 - q) + (1 - p) * q), 1e-6), B(float((1 - p) * (1 - q)), 1e-6)]], o="O3", d="H",
              fig={"kind": "tree", "a": [["P", fmt(float(p))], ["F", fmt(float(1 - p))]], "b": [["P", fmt(float(q))], ["F", fmt(float(1 - q))]]})
def c5(r):
    menu = [r.randint(2, 5), r.randint(2, 5), r.randint(2, 4)]
    return N(f"A café offers {menu[0]} starters, {menu[1]} mains and {menu[2]} desserts. How many different three-course meals are possible?", menu[0] * menu[1] * menu[2], "meals", units=["meals"], o="O3")
def c6(r):
    n = r.randint(3, 6)
    return P(f"Three fair coins are flipped. Find P(exactly {pick(r, ['one', 'two'])} heads).", Fr(3, 8), o="O3")
def c7(r):
    a, b = r.randint(2, 6), r.randint(2, 6); n = a + b
    f = 2 * Fr(a, n) * Fr(b, n - 1)
    return P(f"A box has {a} milk and {b} dark chocolates. Two are eaten at random (no replacement). Find P(one of each type).", f, o="O3", d="VH")
s.core(c1(s.rng), c2(s.rng), c3(s.rng), c4(s.rng), c5(s.rng), c6(s.rng), c1(s.rng),
       EX("Explain why the probabilities change on the second branch of a tree diagram when you do not replace the first item.", [("one fewer item in total", ["fewer|less|one less|total.*(down|smaller|changes)|n ?- ?1"]), ("the number of that colour may also go down", ["colour|that type|same kind|numerator|left"])], "Without replacement there is one fewer item in total, and one fewer of the type taken first, so both the numerator and denominator can change.", o="O3"))
s.gen("p", 44, c1, c2, c3, c4, c5, c7)
s.gen("a", 8, c7, c2, lambda r: (lambda n: P(f"Three fair dice are rolled. Find P(all three show the same number) for dice numbered 1 to {n}.", Fr(1, n * n), o="O3", d="VH"))(pick(r, [4, 6, 8, 10, 12])), lambda r: (lambda a, b: P(f"A bag has {a} red and {b} blue balls. Three are taken without replacement. Find P(all red).", Fr(a, a + b) * Fr(a - 1, a + b - 1) * Fr(a - 2, a + b - 2), o="O3", d="VH"))(r.randint(3, 7), r.randint(2, 6)))

# ================================================================== 12.4
s = U.section("12.4", "Chance experiments", ["O4"])
s.idea("Relative frequency", ["**Relative frequency = number of times the event happened ÷ number of trials.** It is an estimate of the probability.",
       "The **more trials**, the more reliable the estimate. If the relative frequency is far from the theoretical probability after many trials, the object may be **biased**."])
s.example("Expected frequency", "A spinner landed on blue 42 times in 120 spins. Estimate how many blues in 500 spins.", [("relative frequency = 42/120 = 0.35", ""), ("0.35 × 500 = 175", "")], "175")
s.check(N("A dice is rolled 300 times and lands on 6 a total of 81 times. Find the relative frequency of a 6.", 0.27, o="O4"))
s.mistake("Small samples", ["Ten flips giving 7 heads does not prove a coin is biased – the sample is too small. Use many trials before deciding."])
s.check(MC("Which estimate of P(heads) is most reliable?", "Lia: 2000 flips", [("Ari: 10 flips", ""), ("Bo: 50 flips", ""), ("Cy: 200 flips", "")], o="O4"))
def e1(r):
    n = pick(r, [50, 80, 120, 200, 250, 400]); f = r.randint(n // 10, n // 2)
    return N(f"A drawing pin lands point up {f} times in {n} throws. Find the relative frequency of point up (3 d.p.).", round(f / n, 3), o="O4", tol=0.0006)
def e2(r):
    n = pick(r, [40, 50, 60, 80, 100]); f = r.randint(n // 10, n // 2); m = pick(r, [300, 500, 600, 1000, 1200])
    return N(f"In {n} trials an event happens {f} times. Estimate how many times it will happen in {m} trials.", round(f / n * m, 1), "times", units=["times"], o="O4", tol=0.06)
def e3(r):
    counts = [r.randint(40, 70) for _ in range(5)]; six = sum(counts); last = r.choice([r.randint(40, 70), r.randint(95, 140)])
    counts.append(last); tot = sum(counts); biased = abs(last / tot - 1 / 6) > 0.05
    return MC("A dice is rolled many times. Is there evidence that it is biased towards 6?", "Yes, 6 came up much more than 1/6 of the time" if biased else "No, every score is close to 1/6 of the rolls",
              [("No, every score is close to 1/6 of the rolls" if biased else "Yes, 6 came up much more than 1/6 of the time", ""), ("You cannot tell from results", "")], o="O4", d="H",
              data={"head": ["Score", "1", "2", "3", "4", "5", "6"], "rows": [["Frequency"] + [str(c) for c in counts]]})
def e4(r):
    cols = ["red", "blue", "green", "yellow"]; f = [r.randint(10, 60) for _ in cols]; n = sum(f)
    i = r.randrange(4)
    return N(f"A spinner is spun {n} times. Find the relative frequency of {cols[i]} (2 d.p.).", round(f[i] / n, 2), o="O4", tol=0.006, data={"head": ["Colour"] + cols, "rows": [["Frequency"] + [str(x) for x in f]]})
def e5(r):
    n = pick(r, [10, 20, 50, 100]); p = Fr(1, pick(r, [2, 4, 5]))
    return N(f"A fair spinner has P(red) = {frac(p)}. How many reds would you expect in {n * 6} spins?", float(p * n * 6), "reds", units=["reds"], o="O4")
def e6(r):
    rows = [("The more trials, the more reliable the estimate", "True"), ("10 trials are enough to show bias", "False"), ("Relative frequency can be greater than 1", "False"),
            ("Two people doing the same experiment may get different results", "True"), ("Relative frequency estimates probability", "True")]
    return GD("True or false?", "True or false?", r.sample(rows, 4), o="O4")
s.core(e1(s.rng), e2(s.rng), e3(s.rng), e4(s.rng), e5(s.rng), e6(s.rng),
       GR("A coin is flipped. After 10, 20, 30, 40 and 50 flips the relative frequency of heads was 0.6, 0.55, 0.5, 0.525 and 0.5. Plot these points.", {"label": "Number of flips", "min": 0, "max": 50, "step": 10}, {"label": "Relative frequency", "min": 0, "max": 1, "step": 0.1}, [[10, 0.6], [20, 0.55], [30, 0.5], [40, 0.525], [50, 0.5]], o="O4"),
       EX("Explain how you could test whether a coin is biased.", [("flip it many times", ["many|lot|large|100|1000|hundreds"]), ("compare relative frequency of heads with 0.5", ["0\\.5|half|1/2|compare|relative"])], "Flip it many times and work out the relative frequency of heads. If it is far from 0.5 after many flips, the coin is probably biased.", o="O4"))
s.gen("p", 44, e1, e2, e3, e4, e5, e6)
s.gen("a", 8, e3, e2, lambda r: (lambda n, f, g: N(f"Ana spins a spinner {n} times and gets {f} reds. Ben spins it {2*n} times and gets {g} reds. Using all the results, estimate P(red) (3 d.p.).", round((f + g) / (3 * n), 3), o="O4", d="VH", tol=0.0006))(pick(r, [40, 50, 60]), r.randint(8, 20), r.randint(16, 40)))

U.mindmap(("Mutually exclusive", "Cannot happen together • P(A or B) = P(A) + P(B) • P(not A) = 1 − P(A)", "O1", "12.1"), ("Independent", "Do not affect each other • P(A and B) = P(A) × P(B)", "O2", "12.2"),
          ("Combined events", "Sample space • tree diagrams: multiply along, add down", "O3", "12.3"), ("Experiments", "Relative frequency • more trials = more reliable • bias", "O4", "12.4"))
