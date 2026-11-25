# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 13 Probability (13.1 Calculating probabilities, 13.2 Experimental and theoretical probabilities).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(13, "Probability", "Statistics and probability",
         "Equally likely outcomes, mutually exclusive events, the probability of an event not happening, and comparing experimental with theoretical probability.",
         {"O1": {"code": "8Sp.01", "sec": "13.1", "codeNote": "", "t": "Calculate probabilities of equally likely outcomes and use the fact that probabilities of mutually exclusive outcomes add to 1."},
          "O2": {"code": "8Sp.02", "sec": "13.2", "codeNote": "", "t": "Find experimental probabilities (relative frequencies) and compare them with theoretical probabilities."}})
TOL = 1e-6


def P(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction in its simplest form or a decimal.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}"), **kw)


COLS = ["red", "blue", "green", "yellow", "white"]

# ================================================================== 13.1
s = U.section("13.1", "Calculating probabilities", ["O1"])
s.idea("Equally likely outcomes", ["**P(event) = number of favourable outcomes ÷ total number of outcomes**, when all outcomes are equally likely.",
       "Probabilities go from 0 (impossible) to 1 (certain). **P(not A) = 1 − P(A)**."])
s.example("A bag of counters", "A bag has 3 red, 5 blue and 2 green counters. One is taken at random. Find P(blue) and P(not blue).", [("total = 10", ""), ("P(blue) = 5/10 = 1/2", ""), ("P(not blue) = 1 − 1/2 = 1/2", "")], "1/2 and 1/2")
s.check(P("A fair six-sided dice is rolled. Find P(a number greater than 4).", Fr(1, 3), o="O1"))
s.idea("Mutually exclusive outcomes", ["Outcomes that cannot happen at the same time are **mutually exclusive**. The probabilities of all the mutually exclusive outcomes add up to **1**."])
s.idea("Listing outcomes systematically", ["For two events, list every pair in a table (a sample space). Two coins give HH, HT, TH, TT – four equally likely outcomes, so P(one head and one tail) = 2/4, not 1/3.",
       "A table stops you missing or double-counting outcomes."])
s.check(MC("Before you read on: two fair coins are flipped. What is P(two heads)?", "1/4", [("1/3", "There are 4 outcomes, not 3: HT and TH are different."), ("1/2", "Only HH gives two heads.")], o="O1"))
s.mistake("Add to 1", ["If P(red) = 0.3 and P(blue) = 0.5 and these are the only colours with green, then P(green) = 1 − 0.3 − 0.5 = 0.2."])


def p1(r):
    n = [r.randint(1, 9) for _ in range(3)]; c = r.sample(COLS, 3); k = r.randrange(3)
    return P(f"A bag contains {n[0]} {c[0]}, {n[1]} {c[1]} and {n[2]} {c[2]} counters. One is picked at random. Find P({c[k]}).", Fr(n[k], sum(n)), o="O1", data={"head": ["Colour", *c], "rows": [["Counters", *map(str, n)]]})
def p2(r):
    n = [r.randint(1, 9) for _ in range(3)]; c = r.sample(COLS, 3); k = r.randrange(3)
    return P(f"A bag contains {n[0]} {c[0]}, {n[1]} {c[1]} and {n[2]} {c[2]} balls. One is picked at random. Find P(not {c[k]}).", Fr(sum(n) - n[k], sum(n)), o="O1")
def p3(r):
    ev = pick(r, [("an even number", 3), ("a prime number", 3), ("a multiple of 3", 2), ("a number less than 3", 2), ("a 6", 1), ("a factor of 6", 4)])
    return P(f"A fair six-sided dice is rolled. Find P({ev[0]}).", Fr(ev[1], 6), o="O1")
def p4(r):
    a, b = r.randint(1, 6) / 10, r.randint(1, 3) / 10
    c = round(1 - a - b, 2)
    if c <= 0: return None
    return N(f"A spinner can land on red, blue or green. P(red) = {fmt(a)} and P(blue) = {fmt(b)}. Find P(green).", c, o="O1", tol=TOL, reason=f"1 − {fmt(a)} − {fmt(b)} = {fmt(c)}.")
def p5(r):
    p = r.randint(1, 99) / 100
    return N(f"The probability that it rains tomorrow is {fmt(p)}. What is the probability that it does not rain?", round(1 - p, 2), o="O1", tol=TOL, reason=f"1 − {fmt(p)} = {fmt(round(1 - p, 2))}.")
def p6(r):
    n = r.randint(5, 10); lab = [str(i) for i in range(1, n + 1)]; k = pick(r, ["an odd number", "a number more than 3"])
    good = sum(1 for i in range(1, n + 1) if (i % 2 == 1 if "odd" in k else i > 3))
    return P(f"A fair spinner has {n} equal sections numbered 1 to {n}. Find P({k}).", Fr(good, n), o="O1", fig={"kind": "spinner", "labels": lab})
def p7(r):
    a, b, c = r.randint(1, 4) / 10, r.randint(1, 4) / 10, r.randint(1, 3) / 10; d = round(1 - a - b - c, 2)
    if d <= 0: return None
    return TB("A biased dice has these probabilities. Find the missing probability.", ["Outcome", "Probability"], [["1 or 2", fmt(a)], ["3 or 4", fmt(b)], ["5", fmt(c)], ["6", B(d)]], o="O1", d="H")
def p8(r):
    rows = [("Rolling a 7 on a normal dice", "Impossible"), ("Getting a head or a tail when you toss a coin", "Certain"), ("Rolling an even number", "Even chance"), ("Picking a red card from a normal pack", "Even chance"), ("The sun rising tomorrow", "Certain")]
    return GD("Describe the probability of each event.", "Probability", r.sample(rows, 4), o="O1", extra=["Unlikely", "Likely"])
def p9(r):
    n = r.randint(20, 60); k = r.randint(2, n // 2)
    return MC(f"There are {n} tickets in a raffle. Mia buys {k}. What is the probability that she wins?", frac(Fr(k, n)), [frac(Fr(1, n)), frac(Fr(n - k, n)), f"{k}/{n - k}"], o="O1", reason=f"{k} winning tickets out of {n}: {frac(Fr(k, n))}.")
def p10(r):
    x = r.randint(1, 6); n_r = r.randint(2, 8)
    return N(f"A bag has {n_r} red balls and some blue balls. P(red) = {frac(Fr(n_r, n_r + x))}. How many blue balls are there?", x, "balls", units=["balls"], o="O1", d="VH", reason=f"P(red) = {n_r}/{n_r + x}, so there are {n_r + x} balls and {x} are blue.") if Fr(n_r, n_r + x).numerator == n_r else None


def p11(r):
    w = pick(r, ["MATHEMATICS", "PROBABILITY", "SCIENCE", "BANANA", "ELEPHANT", "CALCULATOR", "TRIANGLE", "EQUATION"])
    v = sum(1 for ch in w if ch in "AEIOU")
    return P(f"One letter is chosen at random from the word {w}. Find P(a vowel).", Fr(v, len(w)), o="O1", reason=f"{v} vowels out of {len(w)} letters.")
def p12(r):
    n, k = r.randint(12, 30), r.randint(3, 5)
    return P(f"Cards numbered 1 to {n} are shuffled and one is picked. Find P(a multiple of {k}).", Fr(n // k, n), o="O1", reason=f"{n // k} multiples of {k} out of {n}.")
def p13(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return P(f"A drawer has black and white socks in the ratio {a} : {b}. One sock is taken at random. Find P(black).", Fr(a, a + b), o="O1", d="H", reason=f"{a} parts out of {a + b}.")
def p14(r):
    n = r.randint(3, 8); p = Fr(1, n)
    return P(f"A fair spinner has {n} equal sections, one of them blue. Find P(not blue).", 1 - p, o="O1", fig={"kind": "spinner", "labels": ["B"] + [str(i) for i in range(2, n + 1)]})


def i131(r):
    t = r.randint(3, 11)
    ways = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == t)
    return MC(f"Two dice are rolled and the scores added. What is P(total = {t})?", frac(Fr(ways, 36)) if True else "", [(frac(Fr(1, 11)), "There are 36 equally likely pairs, not 11 totals."), (frac(Fr(ways + 1, 36)), "Count the pairs carefully.")], o="O1", d="H",
              reason=f"There are {ways} pairs that add to {t}, out of 36.") if frac(Fr(ways, 36)) != frac(Fr(1, 11)) else None


s.std([p1, p7, p2, p3, p4, p5, p6, p8, p9, p10, p11, p12, p13, p14], EX("Explain why P(not A) = 1 − P(A).", [("A either happens or it does not", ["either|happens or|one or the other"]), ("these probabilities add to 1", ["add.*1|total.*1|sum.*1|= ?1"])], "Event A either happens or it does not. These two outcomes are mutually exclusive and cover everything, so their probabilities add to 1. So P(not A) = 1 − P(A).", o="O1"),
      deep=[i131])

# ================================================================== 13.2
s = U.section("13.2", "Experimental and theoretical probabilities", ["O2"])
s.idea("Relative frequency", ["**Experimental probability** (relative frequency) = number of times the event happened ÷ number of trials.",
       "The **theoretical probability** is worked out from equally likely outcomes. With more trials the experimental probability usually gets **closer** to the theoretical one."])
s.example("A coin", "A coin is tossed 80 times and lands heads 46 times. Find the experimental probability of heads.", [("46 ÷ 80", ""), ("= 0.575", "")], "0.575")
s.check(N("A drawing pin lands point up 13 times in 50 drops. Find the relative frequency of 'point up'.", 0.26, o="O2"))
s.idea("Expected frequency", ["**Expected number = probability × number of trials**. A fair dice rolled 120 times: expect 120 × 1/6 = 20 sixes."])
s.check(MC("Before you read on: a coin lands heads 7 times in 10 flips. Is P(heads) for this coin 7/10?", "That is only an estimate from a few trials", [("Yes, exactly", "Ten flips is not enough to be sure."), ("No, it must be 1/2", "It could be a biased coin.")], o="O2"))
s.mistake("Not exactly", ["Experimental results do not have to match the expected number exactly; they vary by chance."])


def e1(r):
    n = pick(r, [20, 40, 50, 80, 100, 200]); k = r.randint(n // 10, n * 9 // 10)
    return N(f"A biased coin is tossed {n} times and lands heads {k} times. Find the relative frequency of heads.", round(k / n, 4), o="O2", tol=TOL, reason=f"{k} ÷ {n} = {fmt(round(k / n, 4))}.")
def e2(r):
    n = pick(r, [60, 120, 180, 300, 600])
    return N(f"A fair dice is rolled {n} times. How many times would you expect to roll a 6?", n // 6, "times", units=["times"], o="O2", reason=f"{n} × 1/6 = {n // 6}.")
def e3(r):
    p = pick(r, [0.1, 0.15, 0.2, 0.25, 0.3, 0.4]); n = pick(r, [40, 80, 200, 500])
    return N(f"The probability that a seed grows is {fmt(p)}. 1 packet has {n} seeds. How many would you expect to grow?", p * n, "seeds", units=["seeds"], o="O2", reason=f"{fmt(p)} × {n} = {fmt(p * n)}.")
def e4(r):
    f = [r.randint(10, 30) for _ in range(4)]; c = ["Red", "Blue", "Green", "Yellow"]; k = r.randrange(4)
    return N(f"A spinner was spun {sum(f)} times. Find the relative frequency of {c[k].lower()}. Give your answer to 2 d.p.", round(f[k] / sum(f), 2), o="O2", tol=0.006, data={"head": ["Colour", *c], "rows": [["Frequency", *map(str, f)]]}, reason=f"{f[k]} ÷ {sum(f)} ≈ {round(f[k] / sum(f), 2)}.")
def e5(r):
    f = [r.randint(10, 30) for _ in range(4)]; c = ["Red", "Blue", "Green", "Yellow"]; t = sum(f)
    return TB(f"A spinner was spun {t} times. Complete the relative frequencies (2 d.p.).", ["Colour", "Relative frequency"], [[c[i], B(round(f[i] / t, 2), 0.006)] for i in range(2)], o="O2", data={"head": ["Colour", *c], "rows": [["Frequency", *map(str, f)]]})
def e6(r):
    n1, n2 = r.randint(10, 30), r.randint(300, 600)
    return MC(f"Lin tosses a coin {n1} times; Max tosses it {n2} times. Whose relative frequency of heads is likely to be closer to 0.5?", "Max's", [("Lin's", "Fewer trials vary more by chance."), ("They will be exactly the same", ""), ("Neither, it is random", "")], o="O2", reason="More trials usually give a more reliable estimate.")
def e7(r):
    n = pick(r, [50, 100, 200]); k = r.randint(n // 4, n * 3 // 4); m = pick(r, [500, 1000, 2000])
    return N(f"In {n} trials a drawing pin landed point up {k} times. Estimate how many times it will land point up in {m} trials.", k / n * m, "times", units=["times"], o="O2", d="H", reason=f"{k}/{n} × {m} = {fmt(k / n * m)}.")
def e8(r):
    n = pick(r, [60, 120, 240]); k = r.randint(2, 6) * (n // 60) + n // 6 + r.randint(5, 15)
    return MC(f"A dice is rolled {n} times and lands on 6 a total of {k} times. You would expect {n // 6}. What does this suggest?", "the dice might be biased towards 6", [("the dice is definitely fair", ""), ("the dice will never land on 6 again", ""), ("the theoretical probability is wrong for all dice", "")], o="O2", d="H")
def e9(r):
    n = pick(r, [20, 25, 40, 50]); k = r.randint(1, n - 1)
    return N(f"In a survey of {n} drivers, {k} were wearing sunglasses. Estimate the probability that the next driver is NOT wearing sunglasses. Give a decimal.", round((n - k) / n, 4), o="O2", tol=TOL, reason=f"({n} − {k}) ÷ {n} = {fmt(round((n - k) / n, 4))}.")


def e10(r):
    n = pick(r, [120, 240, 300, 360]); f = n // 6 + r.randint(-12, 12)
    return N(f"A fair dice is rolled {n} times and lands on 4 a total of {f} times. How many more or fewer 4s than expected is that? (Write a negative number for fewer.)", f - n // 6, o="O2", d="H", reason=f"Expected {n} ÷ 6 = {n // 6}; {f} − {n // 6} = {f - n // 6}.")
def e11(r):
    n = pick(r, [25, 40, 50, 80]); k = r.randint(2, n - 2)
    return N(f"A basketball player scores {k} out of {n} free throws. Write the relative frequency of scoring as a percentage.", k / n * 100, "%", units=["%"], o="O2", tol=TOL, reason=f"{k} ÷ {n} × 100 = {fmt(k / n * 100)}%.")
def e12(r):
    f = [r.randint(5, 25) for _ in range(3)]; c = ["Car", "Bus", "Walk"]; t = sum(f); k = r.randrange(3)
    return N(f"A survey of {t} students recorded how they travel. Estimate the probability that a student chosen at random does NOT {('come by ' + c[k].lower()) if k < 2 else 'walk'}. Give your answer to 2 d.p.", round((t - f[k]) / t, 2), o="O2", tol=0.006, data={"head": ["Travel", *c], "rows": [["Students", *map(str, f)]]})


def i132(r):
    p, n = pick(r, [(Fr(1, 6), 120), (Fr(1, 4), 200), (Fr(2, 5), 150)])
    return N(f"The probability of an event is {frac(p)}. How many times would you expect it in {n} trials?", int(p * n), o="O2", d="H", reason=f"{frac(p)} × {n} = {int(p * n)}.")


s.std([e4, e5, e1, e2, e3, e6, e7, e8, e9, e10, e11, e12], EX("Explain why tossing a fair coin 10 times might not give exactly 5 heads.", [("each toss is random / depends on chance", ["chance|random|luck|independent"]), ("5 is only what you expect on average; results vary", ["expect|average|vary|over many"])], "Each toss is random, so the results vary by chance. 5 heads is only the expected number; with only 10 tosses you could easily get 3, 4, 6 or 7.", o="O2"),
      deep=[i132])

U.mindmap(("Calculating probabilities", "P = favourable ÷ total • P(not A) = 1 − P(A) • mutually exclusive outcomes add to 1", "O1", "13.1"),
          ("Experiments", "Relative frequency = times ÷ trials • expected = P × trials • more trials, better estimate", "O2", "13.2"))
