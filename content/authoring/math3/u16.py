# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 16 Chance (16.1 Describing chance, 16.2 Chance experiments).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(16, "Chance", "Statistics and probability",
         "Using words such as 'will happen', 'might happen' and 'will not happen' to describe chance, and doing simple chance experiments.",
         {"O1": {"code": "3Sp.01", "sec": "16.1", "codeNote": "", "t": "Use the language of chance: will happen, might happen, will not happen."},
          "O2": {"code": "3Sp.02", "sec": "16.2", "codeNote": "", "t": "Carry out simple chance experiments and record the results."}})
W = ["will happen", "might happen", "will not happen"]
COL = ["red", "blue", "green", "yellow"]

s = U.section("16.1", "Describing chance", ["O1"])
s.idea("Will, might, will not", ["Some things **will happen** (the sun will set today). Some things **might happen** (it might rain). Some things **will not happen** (a cat will fly).",
       "If a bag has only red cubes, you **will** pick red. If it has red and blue, you **might** pick red."], fig={"kind": "spinner", "labels": ["R", "B", "R", "B"]})
s.check(MC("A bag has only blue counters. Will you pick a blue one?", "will happen", [("might happen", ""), ("will not happen", "")], o="O1"))
s.check(MC('Before you read on: is it certain that a dice will show a 7?', 'No – it is impossible', [('Yes', 'A normal dice only has 1 to 6.'), ('It is likely', '7 is not on the dice.')], o='O1'))
s.mistake("Might is not will", ["If there are other colours in the bag, red only might happen."])


def c1(r):
    a, b = r.randint(0, 5), r.randint(0, 5)
    if a == 0 and b == 0: return None
    w = "will happen" if b == 0 else "will not happen" if a == 0 else "might happen"
    return MC(f"A bag has {a} red and {b} blue cubes. Will you pick a red cube?", w, [x for x in W if x != w], o="O1")
def c2(r):
    ev = [("the sun will rise tomorrow", "will happen"), ("you will grow 10 metres tall today", "will not happen"), ("it will rain tomorrow", "might happen"), ("a dog will talk", "will not happen"), ("you will see a bird today", "might happen"), ("Monday will come after Sunday", "will happen")]
    return GD("Sort the events.", "Chance", r.sample(ev, 4), o="O1", extra=W)
def c3(r):
    lab = r.choices(["R", "B"], k=4)
    w = "will happen" if lab.count("R") == 4 else "will not happen" if lab.count("R") == 0 else "might happen"
    return MC("Will the spinner land on R?", w, [x for x in W if x != w], o="O1", fig={"kind": "spinner", "labels": lab})
def c4(r):
    n = pick(r, [3, 4, 6])
    return MC(f"A dice is rolled. Will you roll a {n}?", "might happen", ["will happen", "will not happen"], o="O1")
def c5(r):
    return MC("A dice is rolled. Will you roll a 9?", "will not happen", ["might happen", "will happen"], o="O1")
def c6(r):
    a, b = r.randint(1, 8), r.randint(1, 8)
    if a == b: return None
    return MC(f"A bag has {a} red and {b} blue cubes. Which colour are you more likely to pick?", "red" if a > b else "blue", ["blue" if a > b else "red", "they are equally likely"], o="O1", d="H")
def c7(r):
    lab = r.choices(COL[:3], k=6)
    k = max(COL[:3], key=lab.count)
    cs = sorted([lab.count(x) for x in COL[:3]])
    if cs[-1] == cs[-2]: return None
    return S("Which colour is the spinner most likely to land on?", [k, k.capitalize()], o="O1", fig={"kind": "spinner", "labels": lab}, d="H")
def c8(r):
    return MS("Select ALL the events that might happen.", ["it snows tomorrow", "you get a head when you flip a coin"], ["a fish climbs a tree", "you roll a 0 on a dice"], o="O1")


s.std([c3, c2, c1, c4, c5, c8, c6, c7], EX("Explain why picking red from a bag of 3 red and 3 blue 'might happen'.", [("there are red cubes in the bag", "red|some red"), ("but there are blue cubes too, so you might get blue", "blue|might|not sure")], "There are red cubes in the bag, so you could pick red. But there are blue cubes too, so you might pick blue instead. Red might happen.", o="O1"))

s = U.section("16.2", "Chance experiments", ["O2"])
s.idea("Try it and record", ["In a **chance experiment** we try something many times and **record** what happens, often with tally marks.",
       "If you flip a coin 10 times, you might get 4 heads and 6 tails. The results can change each time you try."], table={"head": ["Result", "Tally", "Total"], "rows": [["Heads", "||||", "4"], ["Tails", "||||/ |", "6"]]})
s.check(N("A coin was flipped 10 times. It landed on heads 3 times. How many tails?", 7, "tails", units=["tails"], o="O2"))
s.check(MC('Before you read on: you flip a coin 4 times. Must you get 2 heads?', 'No', [('Yes', 'Results vary by chance.'), ('Only on a new coin', 'Any coin can give different results.')], o='O2'))
s.mistake("Results change", ["If you try again, you may get different results."])


def x1(r):
    t = pick(r, [10, 20]); h = r.randint(2, t - 2)
    return N(f"A coin was flipped {t} times. It landed on heads {h} times. How many tails?", t - h, "tails", units=["tails"], o="O2")
def x2(r):
    cs = [r.randint(1, 9) for _ in range(3)]; k = r.randrange(3)
    return N(f"The table shows spinner results. How many times did it land on {COL[k]}?", cs[k], o="O2", data={"head": ["Colour", *COL[:3]], "rows": [["Times", *map(str, cs)]]})
def x3(r):
    cs = [r.randint(1, 9) for _ in range(3)]
    return N("How many spins were there altogether?", sum(cs), "spins", units=["spins"], o="O2", data={"head": ["Colour", *COL[:3]], "rows": [["Times", *map(str, cs)]]})
def x4(r):
    xs = r.choices(["H", "T"], k=10)
    return TB(f"Coin results: {' '.join(xs)}. Complete the table.", ["Result", "Total"], [["Heads (H)", B(xs.count("H"))], ["Tails (T)", B(xs.count("T"))]], o="O2")
def x5(r):
    cs = r.sample(range(2, 12), 4); k = cs.index(max(cs))
    return S("The bar chart shows spinner results. Which colour came up most?", [COL[k], COL[k].capitalize()], o="O2", fig={"kind": "barchart", "labels": COL, "values": cs, "ymax": 12, "step": 2, "ylabel": "Times"})
def x6(r):
    return MC("Ana flips a coin 10 times and gets 6 heads. Ben flips it 10 times and gets 4 heads. Why are they different?", "results can change by chance", ["Ben did it wrong", "the coin changed", "heads is impossible"], o="O2")
def x7(r):
    xs = r.choices([1, 2, 3, 4, 5, 6], k=12); k = r.randint(1, 6)
    return N(f"Dice rolls: {', '.join(map(str, xs))}. How many times was {k} rolled?", xs.count(k), "times", units=["times"], o="O2", d="H")
def x8(r):
    cs = r.sample(range(2, 12), 3); i, j = r.sample(range(3), 2); a, b = (i, j) if cs[i] > cs[j] else (j, i)
    return N(f"How many more times did {COL[a]} come up than {COL[b]}?", cs[a] - cs[b], "times", units=["times"], o="O2", data={"head": ["Colour", *COL[:3]], "rows": [["Times", *map(str, cs)]]})


s.std([x2, x5, x1, x3, x4, x6, x7, x8], EX("Explain how to record the results of spinning a spinner 20 times.", [("make a tally mark each spin", "tally|mark"), ("count the marks for each colour at the end", "count|total")], "Draw a table with a row for each colour. Make a tally mark each time you spin, then count the marks to find the total for each colour.", o="O2"))

U.mindmap(("Chance words", "Will happen • might happen • will not happen", "O1", "16.1"), ("Experiments", "Try many times • tally • results change", "O2", "16.2"))
