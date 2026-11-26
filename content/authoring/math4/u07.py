# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 7 Fractions (7.1 Understanding fractions, 7.2 Fractions as operators).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(7, "Fractions", "Number",
         "Fractions as parts of a whole and as division, unit and non-unit fractions, and finding fractions of numbers and quantities.",
         {"O1": {"code": "4Nf.01", "sec": "7.1", "codeNote": "", "t": "Understand fractions as parts of a whole and as the result of a division."},
          "O2": {"code": "4Nf.02", "sec": "7.2", "codeNote": "", "t": "Use fractions as operators to find fractions of numbers and quantities."}})

s = U.section("7.1", "Understanding fractions", ["O1"])
s.idea("Parts of a whole", ["The **denominator** tells you how many equal parts the whole is split into; the **numerator** tells you how many parts you have. **3/8** = 3 of 8 equal parts.",
       "A fraction can be a **division**: 3 pizzas shared by 4 children gives each child 3 ÷ 4 = **3/4** of a pizza."], fig=PIE(8, range(3)))
s.check(S("4 cakes are shared equally between 5 children. What fraction of a cake does each child get?", ["4/5"], o="O1"))
s.check(MC('Before you read on: which is bigger, 1/3 or 1/5?', '1/3', [('1/5', 'Cutting into 5 pieces makes smaller pieces than cutting into 3.'), ('They are equal', 'The pieces are different sizes.')], o='O1'))
s.mistake("Equal parts", ["Only equal parts can be called eighths."])


def f1(r):
    d = pick(r, [3, 4, 5, 6, 8, 10]); n = r.randint(1, d - 1)
    return S("What fraction of the circle is shaded?", [f"{n}/{d}"], o="O1", fig=PIE(d, range(n)))
def f2(r):
    a, b = r.randint(1, 7), r.randint(2, 10)
    if a >= b: return None
    return S(f"{a} pizzas are shared equally between {b} children. What fraction of a pizza does each child get?", [f"{a}/{b}"], o="O1")
def f3(r):
    d = pick(r, [4, 5, 6, 8, 10]); n = r.randint(1, d - 1)
    return TB(f"A bar has {d} equal pieces. {n} are eaten. Complete the table.", ["Eaten (pieces)", "Left (pieces)"], [[B(n), B(d - n)]], o="O1")
def f4(r):
    d = pick(r, [3, 4, 5, 8, 10])
    return N(f"How many {('thirds' if d == 3 else 'quarters' if d == 4 else 'fifths' if d == 5 else 'eighths' if d == 8 else 'tenths')} make one whole?", d, o="O1")
def f5(r):
    a, b = r.sample([2, 3, 4, 5, 6, 8, 10], 2)
    return CMP(f"1/{a}", f"1/{b}", "<" if a > b else ">", o="O1")
def f6(r):
    d = pick(r, [4, 5, 8, 10]); n = r.randint(1, d - 1)
    return MC(f"Which fraction is shaded, and which is not shaded, if {n} of {d} equal parts are shaded?", f"{n}/{d} shaded, {d - n}/{d} not shaded", [f"{d - n}/{d} shaded, {n}/{d} not shaded", f"{n}/{d - n} shaded, {d - n}/{n} not shaded"], o="O1")
def f7(r):
    d = pick(r, [5, 8, 10]); ns = r.sample(range(1, d), 3)
    return OD("Put these fractions in order, smallest first.", [f"{n}/{d}" for n in sorted(ns)], o="O1", d="H")
def f8(r):
    d = pick(r, [4, 5, 8]); n = r.randint(1, d - 1); k = r.randint(1, d - n)
    return S(f"Mo eats {n}/{d} of a bar and Ana eats {k}/{d}. What fraction of the bar have they eaten?", [f"{n + k}/{d}"], o="O1", d="H")


def d71(r):
    return MC('Ben says 1/8 is bigger than 1/4 because 8 is bigger than 4. Is he right?', 'No: 1/4 is bigger', [('Yes', 'More pieces means smaller pieces.'), ('They are equal', '1/4 = 2/8.')], o='O1', d="H", reason='1/4 = 2/8, which is more than 1/8.')


s.std([f1, f3, f2, f4, f5, f6, f7, f8], EX("Explain why 3 ÷ 4 = 3/4.", [("a fraction is a division", "division|divide|÷"), ("3 shared equally between 4 gives 3/4 each", "share|each|equal")], "A fraction is a division: 3/4 means 3 ÷ 4. If 3 cakes are shared equally between 4 children, each gets 3/4 of a cake.", o="O1"),
      deep=[d71])

s = U.section("7.2", "Fractions as operators", ["O2"])
s.idea("Finding a fraction of an amount", ["To find **1/5 of 30**, divide by 5: 30 ÷ 5 = **6**.",
       "To find **3/5 of 30**, find 1/5 (6), then multiply by 3: **18**."], fig={"kind": "cells", "cells": [[i, j] for i in range(6) for j in range(5)]})
s.check(N("Find 2/3 of 18.", 12, o="O2"))
s.check(MC('Before you read on: what is 1/4 of 20?', '5', [('80', 'Divide by 4.'), ('16', '1/4 means one of four equal parts.')], o='O2'))
s.mistake("Divide by the denominator", ["1/4 of 20 means 20 ÷ 4, not 20 ÷ 1."])


def o1(r):
    d, k = pick(r, [2, 3, 4, 5, 6, 8, 10]), r.randint(2, 12)
    return N(f"Find 1/{d} of {d * k}.", k, o="O2")
def o2(r):
    d = pick(r, [3, 4, 5, 6, 8]); n = r.randint(2, d - 1); k = r.randint(2, 10)
    if Fr(n, d).denominator != d: return None
    return N(f"Find {n}/{d} of {d * k}.", n * k, o="O2")
def o3(r):
    d, k = pick(r, [2, 3, 4, 5]), r.randint(2, 6)
    return N(f"The grid has {d * k} squares. How many squares are in 1/{d} of the grid?", k, "squares", units=["squares"], o="O2", fig={"kind": "cells", "cells": [[i, j] for i in range(k) for j in range(d)]})
def o4(r):
    d, k = pick(r, [4, 5, 10]), r.randint(3, 9)
    return TB(f"Complete the table for {d * k} beads.", ["Fraction", f"1/{d}", f"2/{d}", f"3/{d}"], [["Beads", B(k), B(2 * k), B(3 * k)]], o="O2")
def o5(r):
    d, k = pick(r, [2, 4, 5, 10]), r.randint(5, 30)
    return N(f"A ribbon is {d * k} cm long. 1/{d} of it is cut off. How long is the piece cut off?", k, "cm", units=["cm"], o="O2")
def o6(r):
    d = pick(r, [3, 4, 5]); n = r.randint(1, d - 1); k = r.randint(4, 10)
    return N(f"There are {d * k} children. {n}/{d} of them walk to school. How many do NOT walk?", (d - n) * k, "children", units=["children"], o="O2", d="H")
def o7(r):
    d, k = pick(r, [3, 4, 5]), r.randint(3, 12)
    return N(f"1/{d} of a number is {k}. What is the number?", d * k, o="O2", d="H")
def o8(r):
    m = pick(r, [100, 200, 500, 1000]); d = pick(r, [2, 4, 5, 10])
    return N(f"A jug holds {m} ml. How much is 1/{d} of the jug?", m // d, "ml", units=["ml"], o="O2")


s.std([o3, o4, o1, o2, o5, o8, o6, o7], EX("Explain how to find 3/4 of 24.", [("1/4 of 24 is 24 ÷ 4 = 6", "\\b6\\b|24 ?÷ ?4"), ("3/4 is 3 × 6 = 18", "18")], "Find one quarter: 24 ÷ 4 = 6. Three quarters is three of those: 6 × 3 = 18.", o="O2"))

U.mindmap(("Fractions", "Numerator • denominator • division", "O1", "7.1"), ("Fractions of amounts", "÷ by the denominator, × by the numerator", "O2", "7.2"))
