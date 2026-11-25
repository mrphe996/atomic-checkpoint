# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 11 More fractions (11.1 Fractions of numbers, 11.2 Ordering and comparing fractions,
11.3 Calculating with fractions). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(11, "More Fractions", "Number",
         "Finding fractions of numbers and amounts, comparing and ordering fractions with the same denominator, and adding and subtracting them.",
         {"O1": {"code": "3Nf.03", "sec": "11.1", "codeNote": "", "t": "Find unit and non-unit fractions of numbers and quantities."},
          "O2": {"code": "3Nf.04", "sec": "11.2", "codeNote": "", "t": "Compare and order fractions with the same denominator, and unit fractions."},
          "O3": {"code": "3Nf.05", "sec": "11.3", "codeNote": "", "t": "Add and subtract fractions with the same denominator within one whole."}})

s = U.section("11.1", "Fractions of numbers", ["O1"])
s.idea("Sharing into equal parts", ["To find **1/4 of 20**, share 20 into 4 equal groups: 20 ÷ 4 = **5**.",
       "To find **3/4 of 20**, find 1/4 (5) and take 3 of them: 5 × 3 = **15**."], fig={"kind": "cells", "cells": [[i, j] for i in range(5) for j in range(4)]})
s.check(N("Find 1/3 of 12.", 4, o="O1"))
s.check(MC('Before you read on: what is 1/2 of 14?', '7', [('28', 'Half means divide by 2.'), ('12', '14 ÷ 2 = 7.')], o='O1'))
s.mistake("Divide by the bottom number", ["1/5 of 30 means 30 ÷ 5 = 6, not 30 ÷ 1."])


def f1(r):
    d, k = pick(r, [2, 3, 4, 5, 10]), r.randint(2, 10)
    return N(f"Find 1/{d} of {d * k}.", k, o="O1")
def f2(r):
    d = pick(r, [3, 4, 5]); n = r.randint(2, d - 1); k = r.randint(2, 6)
    return N(f"Find {n}/{d} of {d * k}.", n * k, o="O1")
def f3(r):
    d, k = pick(r, [2, 3, 4]), r.randint(2, 5)
    return N(f"The grid shows {d * k} squares. How many squares are in 1/{d} of the grid?", k, "squares", units=["squares"], o="O1", fig={"kind": "cells", "cells": [[i, j] for i in range(k) for j in range(d)]})
def f4(r):
    d, k = pick(r, [2, 4, 5, 10]), r.randint(2, 9)
    return TB(f"Complete the table for {d * k} beads.", ["Fraction", f"1/{d}", f"2/{d}"], [["Beads", B(k), B(2 * k)]], o="O1")
def f5(r):
    d, k = pick(r, [2, 3, 4]), r.randint(3, 10)
    return N(f"There are {d * k} children in a class. 1/{d} of them wear glasses. How many wear glasses?", k, "children", units=["children"], o="O1")
def f6(r):
    d, k = pick(r, [2, 4, 10]), r.randint(2, 9)
    return N(f"A ribbon is {d * k} cm long. Mo cuts off 1/{d} of it. How long is the piece?", k, "cm", units=["cm"], o="O1")
def f7(r):
    d, k = pick(r, [3, 4, 5]), r.randint(2, 8)
    return N(f"1/{d} of a number is {k}. What is the number?", d * k, o="O1", d="H")
def f8(r):
    d = pick(r, [3, 4, 5]); n = r.randint(2, d - 1); k = r.randint(2, 6)
    return N(f"A bag has {d * k} sweets. {n}/{d} are red. How many are NOT red?", (d - n) * k, "sweets", units=["sweets"], o="O1", d="H")


s.std([f3, f4, f1, f2, f5, f6, f7, f8], EX("Explain how to find 2/5 of 15.", [("1/5 of 15 is 15 ÷ 5 = 3", "\\b3\\b|15 ?÷ ?5"), ("2/5 is 2 × 3 = 6", "\\b6\\b")], "Find one fifth first: 15 ÷ 5 = 3. Two fifths is two of those: 3 × 2 = 6.", o="O1"))

s = U.section("11.2", "Ordering and comparing fractions", ["O2"])
s.idea("Same bottom number", ["When the denominators are the same, compare the numerators: **3/8 < 5/8**.",
       "For **unit fractions** (top number 1), the bigger the bottom number, the smaller the fraction: 1/10 < 1/4 < 1/2."], fig=PIE(8, range(5)))
s.check(CMP("2/5", "4/5", "<", o="O2"))
s.check(MC('Before you read on: which is bigger, 1/2 or 1/4?', '1/2', [('1/4', 'Halves are bigger pieces than quarters.'), ('They are equal', 'The pieces are different sizes.')], o='O2'))
s.mistake("1/10 is not bigger than 1/2", ["Tenths are tiny pieces. Halves are big pieces."])


def c1(r):
    d = pick(r, [4, 5, 6, 8, 10]); a, b = r.sample(range(1, d), 2)
    return CMP(f"{a}/{d}", f"{b}/{d}", "<" if a < b else ">", o="O2")
def c2(r):
    a, b = r.sample([2, 3, 4, 5, 8, 10], 2)
    return CMP(f"1/{a}", f"1/{b}", "<" if a > b else ">", o="O2")
def c3(r):
    d = pick(r, [5, 8, 10]); ns = r.sample(range(1, d), 3)
    return OD("Put these fractions in order, smallest first.", [f"{n}/{d}" for n in sorted(ns)], o="O2")
def c4(r):
    ds = r.sample([2, 3, 4, 5, 10], 3)
    return OD("Put these unit fractions in order, smallest first.", [f"1/{d}" for d in sorted(ds, reverse=True)], o="O2", d="H")
def c5(r):
    d = pick(r, [4, 6, 8]); a, b = r.sample(range(1, d), 2)
    return MC(f"Circle A has {a}/{d} shaded and circle B has {b}/{d} shaded. Which has more shaded?", "A" if a > b else "B", ["B" if a > b else "A", "the same"], o="O2", fig=PIE(d, range(max(a, b))))
def c6(r):
    d = pick(r, [5, 8, 10]); n = r.randint(1, d - 1)
    return MS(f"Select ALL the fractions bigger than {n}/{d}.", [f"{x}/{d}" for x in r.sample(range(n + 1, d + 1), min(2, d - n))], [f"{x}/{d}" for x in r.sample(range(1, n + 1), min(2, n))], o="O2") if d - n >= 1 else None
def c7(r):
    d = pick(r, [4, 5, 8, 10]); a = r.randint(1, d - 1)
    return CMP(f"{a}/{d}", f"{d - a}/{d}", "<" if a < d - a else ">" if a > d - a else "=", o="O2", d="H")
def c8(r):
    return MC("Which is the biggest?", "1/2", ["1/3", "1/5", "1/10"], o="O2")

def c9(r):
    d = pick(r, [4, 6, 8, 10]); n = r.randint(1, d - 1)
    if 2 * n == d: return None
    return MC(f"The circle shows {n}/{d} shaded. Is that more or less than one half?", "more" if 2 * n > d else "less", ["less" if 2 * n > d else "more", "exactly half"], o="O2", fig=PIE(d, range(n)))


s.std([c5, c9, c3, c1, c2, c4, c6, c8, c7], EX("Explain why 1/3 is bigger than 1/6.", [("thirds are bigger pieces than sixths", "bigger pieces|fewer parts|cut into 3"), ("the whole is shared into fewer parts", "fewer|3 parts|less parts")], "For thirds the whole is cut into 3 equal parts; for sixths into 6. Fewer parts means bigger pieces, so 1/3 > 1/6.", o="O2"))

s = U.section("11.3", "Calculating with fractions", ["O3"])
s.idea("Adding parts", ["With the **same denominator**, add or subtract the top numbers: **2/5 + 1/5 = 3/5** and **4/6 − 1/6 = 3/6**.",
       "One whole is the same as 5/5, 6/6 or 10/10."], fig=PIE(5, range(3)))
s.check(S("Work out 1/4 + 2/4.", ["3/4"], o="O3"))
s.check(MC('Before you read on: what is 1/4 + 2/4?', '3/4', [('3/8', 'The pieces are still quarters.'), ('2/4', '1 + 2 = 3.')], o='O3'))
s.mistake("Keep the bottom number", ["2/5 + 1/5 = 3/5, not 3/10."])


def q1(r):
    d = pick(r, [4, 5, 6, 8, 10]); a, b = r.randint(1, d - 2), r.randint(1, d - 2)
    if a + b >= d: return None
    return S(f"Work out {a}/{d} + {b}/{d}.", [f"{a + b}/{d}"], o="O3")
def q2(r):
    d = pick(r, [4, 5, 6, 8, 10]); a, b = sorted(r.sample(range(1, d), 2), reverse=True)
    return S(f"Work out {a}/{d} − {b}/{d}.", [f"{a - b}/{d}"], o="O3")
def q3(r):
    d = pick(r, [4, 5, 6, 8]); a, b = r.randint(1, d - 2), r.randint(1, d - 2)
    if a + b >= d: return None
    return S(f"The circle shows {a}/{d} + {b}/{d}. What is the total?", [f"{a + b}/{d}"], o="O3", fig=PIE(d, range(a + b)))
def q4(r):
    d = pick(r, [4, 5, 8, 10]); a = r.randint(1, d - 1)
    return N(f"Find the missing number: {a}/{d} + ☐/{d} = 1", d - a, o="O3")
def q5(r):
    d = pick(r, [4, 5, 8, 10]); a = r.randint(1, d - 1)
    return S(f"A cake is cut into {d} equal pieces. {a} pieces are eaten. What fraction is left?", [f"{d - a}/{d}"], o="O3")
def q6(r):
    d = pick(r, [5, 8, 10]); a, b = r.randint(1, d - 2), r.randint(1, d - 2)
    if a + b >= d: return None
    return TB("Complete the table. Write the numerator.", ["Calculation", f"Answer (over {d})"], [[f"{a}/{d} + {b}/{d}", B(a + b)], [f"{d}/{d} − {a}/{d}", B(d - a)]], o="O3")
def q7(r):
    d = pick(r, [6, 8, 10]); a, b, c = r.randint(1, 2), r.randint(1, 2), r.randint(1, 2)
    return S(f"Work out {a}/{d} + {b}/{d} + {c}/{d}.", [f"{a + b + c}/{d}"], o="O3", d="H")
def q8(r):
    d = pick(r, [5, 8, 10]); a, b = r.randint(1, 3), r.randint(1, 3)
    return S(f"Sam ate {a}/{d} of a pizza and Jo ate {b}/{d}. What fraction of the pizza is left?", [f"{d - a - b}/{d}"], o="O3", d="H")


s.std([q3, q6, q1, q2, q4, q5, q7, q8], EX("Explain why 3/8 + 2/8 = 5/8.", [("the pieces are all eighths", "eighths|same size|same bottom"), ("3 + 2 = 5 eighths", "3 ?\\+ ?2|5 eighths|five")], "Both fractions are eighths, so the pieces are the same size. 3 eighths and 2 more eighths make 5 eighths, 5/8.", o="O3"))

U.mindmap(("Fractions of numbers", "Divide by the denominator, × the numerator", "O1", "11.1"), ("Comparing", "Same denominator • unit fractions", "O2", "11.2"), ("Calculating", "Add or subtract the numerators", "O3", "11.3"))
