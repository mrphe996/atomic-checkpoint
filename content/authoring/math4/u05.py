# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 5 Multiplication, multiples and factors (5.1 Tables, multiples and factors, 5.2 Multiplication).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(5, "Multiplication, Multiples and Factors", "Number",
         "Times tables to 10 × 10, multiples and factors, and multiplying 2-digit numbers by 1-digit numbers and by 10 and 100.",
         {"O1": {"code": "4Nc.03", "sec": "5.1", "codeNote": "", "t": "Know times tables to 10 × 10 and find multiples and factors."},
          "O2": {"code": "4Nc.04", "sec": "5.2", "codeNote": "", "t": "Estimate and multiply 2-digit numbers by 1-digit numbers, and multiply by 10 and 100."}})

s = U.section("5.1", "Tables, multiples and factors", ["O1"])
s.idea("Multiples and factors", ["**Multiples** of 6 are in the 6 times table: 6, 12, 18, 24, …",
       "**Factors** of 12 divide into 12 exactly: 1, 2, 3, 4, 6 and 12. Factors come in **pairs**: 1 × 12, 2 × 6, 3 × 4."], fig={"kind": "cells", "cells": [[i, j] for i in range(4) for j in range(3)]})
s.check(N("What is 7 × 8?", 56, o="O1"))
s.check(MC('Before you read on: is 4 a factor of 30?', 'No', [('Yes', '30 ÷ 4 = 7 remainder 2.'), ('Only a multiple', '4 is not a multiple of 30 either.')], o='O1'))
s.mistake("Factor or multiple?", ["3 is a factor of 12; 12 is a multiple of 3."])


def f1(r):
    a, b = r.randint(2, 10), r.randint(2, 10)
    return N(f"What is {a} × {b}?", a * b, o="O1")
def f2(r):
    a, b = r.randint(2, 10), r.randint(2, 10)
    return N(f"What is {a * b} ÷ {a}?", b, o="O1")
def f3(r):
    n = pick(r, [12, 16, 18, 20, 24, 30])
    return MS(f"Select ALL the factors of {n}.", [str(k) for k in r.sample([k for k in range(2, n) if n % k == 0], 2)], [str(k) for k in r.sample([k for k in range(4, n) if n % k], 2)], o="O1")
def f4(r):
    n = pick(r, [12, 16, 18, 20, 24])
    pr = [(k, n // k) for k in range(1, int(n ** 0.5) + 1) if n % k == 0][:3]
    return TB(f"Complete the factor pairs of {n}.", ["Factor", "Pair"], [[str(a), B(b)] for a, b in pr], o="O1")
def f5(r):
    k = pick(r, [3, 4, 6, 7, 8, 9]); ns = r.sample(range(10, 90), 4)
    return GD(f"Is each number a multiple of {k}?", "Multiple?", [(str(n), "Yes" if n % k == 0 else "No") for n in ns], o="O1", extra=["Yes", "No"])
def f6(r):
    a, b = r.randint(2, 6), r.randint(2, 8)
    return N("How many squares are in the array?", a * b, "squares", units=["squares"], o="O1", fig={"kind": "cells", "cells": [[i, j] for i in range(b) for j in range(a)]})
def f7(r):
    a, b = r.sample([2, 3, 4, 5, 6], 2)
    m = next(x for x in range(1, 61) if x % a == 0 and x % b == 0)
    return N(f"What is the smallest number that is a multiple of both {a} and {b}?", m, o="O1", d="H")
def f8(r):
    n = pick(r, [12, 18, 20, 24, 36])
    return N(f"How many factors does {n} have?", sum(1 for k in range(1, n + 1) if n % k == 0), "factors", units=["factors"], o="O1", d="H")


s.std([f6, f4, f1, f2, f3, f5, f7, f8], EX("Explain the difference between a factor and a multiple of 8.", [("factors divide into 8: 1, 2, 4, 8", "divide|1, ?2, ?4"), ("multiples are in the 8 times table: 16, 24", "times table|16|24")], "A factor of 8 divides into 8 exactly (1, 2, 4, 8). A multiple of 8 is in the 8 times table (8, 16, 24, …).", o="O1"))

s = U.section("5.2", "Multiplication", ["O2"])
s.idea("Partitioning", ["To work out 34 × 6, split 34 into 30 + 4: 30 × 6 = 180 and 4 × 6 = 24, so **34 × 6 = 204**.",
       "× 10 moves digits one place left (23 × 10 = 230); × 100 moves them two places (23 × 100 = 2300). Estimate first: 34 × 6 ≈ 30 × 6 = 180."], table={"head": ["×", "30", "4"], "rows": [["6", "180", "24"]]})
s.check(N("Work out 27 × 4.", 108, o="O2"))
s.check(MC('Before you read on: what is 23 × 4?', '92', [('812', 'That writes 2 × 4 and 3 × 4 side by side.'), ('82', '20 × 4 = 80, 3 × 4 = 12: 92.')], o='O2'))
s.mistake("Multiply both parts", ["34 × 6 is not 30 × 6 + 4. Multiply the 4 by 6 too."])


def m1(r):
    a, b = r.randint(12, 99), r.randint(2, 9)
    return N(f"Work out {a} × {b}.", a * b, o="O2")
def m2(r):
    t, o_, b = r.randint(1, 9) * 10, r.randint(1, 9), r.randint(2, 9)
    return TB(f"Complete the grid to work out {t + o_} × {b}.", ["×", str(t), str(o_)], [[str(b), B(t * b), B(o_ * b)]], o="O2")
def m3(r):
    a, k = r.randint(11, 99), pick(r, [10, 100])
    return N(f"Work out {a} × {k}.", a * k, o="O2")
def m4(r):
    a, b = r.randint(21, 89), r.randint(3, 9); e = round(a, -1) * b
    return MC(f"Which is the best estimate for {a} × {b}?", str(e), [str(e * 10), str(round(a, -1) + b), str(e // 10)], o="O2")
def m5(r):
    p, n = r.randint(12, 49), r.randint(3, 9)
    items = ["pen", "ruler", "notebook"]; ps = [p, r.randint(12, 49), r.randint(12, 49)]; k = r.randrange(3)
    return N(f"How much do {n} {items[k]}s cost, in cents?", ps[k] * n, "cents", units=["cents"], o="O2", data={"head": ["Item", *items], "rows": [["Price (cents)", *map(str, ps)]]})
def m6(r):
    a, b = r.randint(12, 40), r.randint(3, 9)
    return N(f"There are {a} children in each class. How many children are in {b} classes?", a * b, "children", units=["children"], o="O2")
def m7(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out {a} × {b} × 10.", a * b * 10, o="O2", d="H")
def m8(r):
    a, b = r.randint(12, 30), r.randint(3, 6)
    return N(f"Find the missing number: ☐ ÷ {b} = {a}", a * b, o="O2", d="H")


def b52(r):
    return MC('Kai works out 23 × 4 as 20 × 4 + 3 = 83. What is right?', '92', [('83', 'He forgot to multiply the 3 by 4.'), ('27', 'That adds 4.')], o='O2', d="H", reason='Both parts are multiplied: 20 × 4 + 3 × 4 = 80 + 12 = 92.')


s.std([m2, m5, m1, m3, m4, m6, m7, m8], EX("Explain how to work out 46 × 3.", [("split 46 into 40 + 6", "40|split"), ("120 + 18 = 138", "138")], "Split 46 into 40 + 6. 40 × 3 = 120 and 6 × 3 = 18. Add: 120 + 18 = 138.", o="O2"),
      deep=[b52])

U.mindmap(("Tables", "To 10 × 10 • multiples • factor pairs", "O1", "5.1"), ("Multiplication", "Partition • × 10, × 100 • estimate", "O2", "5.2"))
