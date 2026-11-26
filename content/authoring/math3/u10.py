# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 10 More multiplication and division (10.1 Revisiting multiplication and division,
10.2 Playing with multiplication and division, 10.3 Extending multiplication and division). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(10, "More Multiplication and Division", "Number",
         "Times-table facts for 2, 3, 4, 5, 6, 8, 9 and 10, odd and even numbers, multiplying by 10, and multiplying a 2-digit number by a 1-digit number.",
         {"O1": {"code": "3Nc.09", "sec": "10.1", "codeNote": "", "t": "Recall multiplication and division facts for the 2, 3, 4, 5, 6, 8, 9 and 10 times tables."},
          "O2": {"code": "3Nc.10", "sec": "10.2", "codeNote": "", "t": "Recognise odd and even numbers and patterns in multiples."},
          "O3": {"code": "3Nc.11", "sec": "10.3", "codeNote": "", "t": "Multiply by 10 and multiply 2-digit numbers by 1-digit numbers."}})
T = [2, 3, 4, 5, 6, 8, 9, 10]

s = U.section("10.1", "Revisiting multiplication and division", ["O1"])
s.idea("Facts and inverses", ["If you know **6 × 7 = 42**, you also know 7 × 6 = 42, 42 ÷ 6 = 7 and 42 ÷ 7 = 6.",
       "A **multiplication square** helps you find facts quickly."], table={"head": ["×", "2", "3", "4", "5"], "rows": [["3", "6", "9", "12", "15"], ["4", "8", "12", "16", "20"]]})
s.check(N("What is 42 ÷ 6?", 7, o="O1"))
s.check(MC('Before you read on: 20 sweets are shared between 4 children. How many each?', '5', [('16', 'Sharing means dividing.'), ('80', 'That multiplies.')], o='O1'))
s.mistake("Division order", ["42 ÷ 6 = 7, but 6 ÷ 42 is not 7."])


def f1(r):
    a, b = pick(r, T), r.randint(2, 10)
    return N(f"What is {a} × {b}?", a * b, o="O1")
def f2(r):
    a, b = pick(r, T), r.randint(2, 10)
    return N(f"What is {a * b} ÷ {a}?", b, o="O1")
def f3(r):
    a, b = r.sample(T[:6], 2)
    return TB("Complete the multiplication square.", ["×", str(a), str(b)], [[str(c), B(a * c), B(b * c)] for c in r.sample(range(2, 10), 2)], o="O1")
def f4(r):
    a, b = pick(r, T), r.randint(2, 10)
    return N(f"Find the missing number: ☐ × {a} = {a * b}", b, o="O1")
def f5(r):
    a, b = pick(r, T), r.randint(2, 10)
    return N(f"There are {a} rows of chairs with {b} chairs in each row. How many chairs?", a * b, "chairs", units=["chairs"], o="O1", fig={"kind": "cells", "cells": [[i, j] for i in range(b) for j in range(a)]} if a * b <= 40 else None)
def f6(r):
    a, b = pick(r, T), r.randint(2, 10)
    return N(f"{a * b} stickers are shared equally between {a} children. How many stickers each?", b, "stickers", units=["stickers"], o="O1")
def f7(r):
    a, b = pick(r, T), r.randint(2, 10)
    return MC(f"Which is NOT in the fact family of {a}, {b} and {a * b}?", f"{a} + {b} = {a + b}", [f"{b} × {a} = {a * b}", f"{a * b} ÷ {b} = {a}", f"{a * b} ÷ {a} = {b}"], o="O1")
def f8(r):
    a, b, c = r.randint(2, 5), r.randint(2, 5), r.randint(2, 5)
    return N(f"Work out {a} × {b} × {c}.", a * b * c, o="O1", d="H")


s.std([f3, f5, f1, f2, f4, f6, f7, f8], EX("Explain how knowing 8 × 5 = 40 helps you find 40 ÷ 8.", [("division is the inverse of multiplication", "inverse|opposite|fact family"), ("so 40 ÷ 8 = 5", "\\b5\\b")], "Division undoes multiplication. Since 8 × 5 = 40, we know 40 ÷ 8 = 5.", o="O1"))

s = U.section("10.2", "Playing with multiplication and division", ["O2"])
s.idea("Odd and even", ["**Even** numbers end in 0, 2, 4, 6 or 8 and can be shared into 2 equal groups. **Odd** numbers end in 1, 3, 5, 7 or 9.",
       "Patterns: multiples of 5 end in 0 or 5. Multiples of 10 end in 0. Even × anything is even."], fig={"kind": "cells", "cells": [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1]]})
s.check(MC("Is 37 odd or even?", "odd", [("even", "")], o="O2"))
s.check(MC('Before you read on: 6 × 5 = 30. What is 30 ÷ 5?', '6', [('25', 'Division undoes multiplication.'), ('35', '30 ÷ 5 = 6.')], o='O2'))
s.mistake("Look at the last digit", ["74 is even because it ends in 4, even though 7 is odd."])


def o1(r):
    ns = r.sample(range(10, 999), 4)
    return GD("Is each number odd or even?", "Odd or even", [(str(n), "even" if n % 2 == 0 else "odd") for n in ns], o="O2", extra=["odd", "even"])
def o2(r):
    a, b = r.randint(1, 50), r.randint(1, 50)
    s_ = a + b
    return MC(f"{a} + {b} = {s_}. Is the answer odd or even?", "even" if s_ % 2 == 0 else "odd", ["odd" if s_ % 2 == 0 else "even"], o="O2")
def o3(r):
    k = pick(r, [5, 10]); ns = r.sample(range(10, 200), 4)
    return GD(f"Is each number a multiple of {k}?", "Multiple?", [(str(n), "Yes" if n % k == 0 else "No") for n in ns], o="O2", extra=["Yes", "No"])
def o4(r):
    a = r.randint(10, 90) * 2 + 1
    return N(f"What is the next even number after {a}?", a + 1, o="O2")
def o5(r):
    k = pick(r, [2, 3, 4, 5]); st = k * r.randint(2, 10)
    return N(f"Continue the pattern: {st}, {st + k}, {st + 2 * k}, {st + 3 * k}, ☐", st + 4 * k, o="O2", data={"head": ["1st", "2nd", "3rd", "4th", "5th"], "rows": [[str(st), str(st + k), str(st + 2 * k), str(st + 3 * k), "?"]]})
def o6(r):
    lo = r.randint(10, 90)
    return N(f"How many even numbers are there from {lo} to {lo + 9}?", 5, o="O2")
def o7(r):
    n = r.randint(3, 12) * 2
    return N(f"{n} socks make pairs. How many pairs are there?", n // 2, "pairs", units=["pairs"], o="O2")
def o8(r):
    return MS("Select ALL the true statements.", ["odd + odd = even", "even + even = even"], ["odd + odd = odd", "even + odd = even"], o="O2", d="H")


s.std([o1, o5, o2, o3, o4, o7, o6, o8], EX("Explain why 46 is an even number.", [("it ends in 6", "ends in 6|last digit|6"), ("it can be shared into two equal groups (23 and 23)", "two equal|23|share|halves")], "46 ends in 6, which is even. It can be shared into two equal groups of 23, so it is even.", o="O2"))

s = U.section("10.3", "Extending multiplication and division", ["O3"])
s.idea("× 10 and 2-digit × 1-digit", ["Multiplying by **10** moves every digit one place to the left: 36 × 10 = **360**.",
       "For 23 × 4, split 23 into 20 + 3: 20 × 4 = 80 and 3 × 4 = 12, so 23 × 4 = **92**."], table={"head": ["×", "20", "3"], "rows": [["4", "80", "12"]]})
s.check(N("Work out 45 × 10.", 450, o="O3"))
s.check(MC('Before you read on: what is 3 × 20?', '60', [('23', '3 groups of 20.'), ('600', '3 × 2 = 6, so 3 × 20 = 60.')], o='O3'))
s.mistake("Not just adding 10", ["36 × 10 is 360, not 46."])


def x1(r):
    a = r.randint(11, 99)
    return N(f"Work out {a} × 10.", a * 10, o="O3")
def x2(r):
    a, b = r.randint(11, 49), r.randint(2, 5)
    return N(f"Work out {a} × {b}.", a * b, o="O3")
def x3(r):
    t, o, b = r.randint(1, 4) * 10, r.randint(1, 9), r.randint(2, 5)
    return TB(f"Complete the grid to work out {t + o} × {b}.", ["×", str(t), str(o)], [[str(b), B(t * b), B(o * b)]], o="O3")
def x4(r):
    a = r.randint(11, 99) * 10
    return N(f"Work out {a} ÷ 10.", a // 10, o="O3")
def x5(r):
    a, b = r.randint(11, 30), r.randint(2, 5)
    return N(f"A box holds {a} crayons. How many crayons are in {b} boxes?", a * b, "crayons", units=["crayons"], o="O3")
def x6(r):
    p, n = r.randint(12, 45), r.randint(2, 5)
    items = ["pen", "ruler", "rubber"]; ps = [p, r.randint(12, 45), r.randint(12, 45)]; k = r.randrange(3)
    return N(f"How much do {n} {items[k]}s cost, in cents?", ps[k] * n, "cents", units=["cents"], o="O3", data={"head": ["Item", *items], "rows": [["Price (cents)", *map(str, ps)]]})
def x7(r):
    a, b = r.randint(11, 49), r.randint(2, 5)
    return N(f"Find the missing number: ☐ ÷ {b} = {a}", a * b, o="O3", d="H")
def x8(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out {a} × {b} × 10.", a * b * 10, o="O3", d="H")


s.std([x3, x6, x1, x2, x4, x5, x7, x8], EX("Explain how to work out 34 × 3.", [("split 34 into 30 + 4", "30|split"), ("90 + 12 = 102", "102")], "Split 34 into 30 + 4. 30 × 3 = 90 and 4 × 3 = 12. Add them: 90 + 12 = 102.", o="O3"))

U.mindmap(("Facts", "Times tables • fact families", "O1", "10.1"), ("Odd and even", "Last digit • patterns in multiples", "O2", "10.2"), ("Bigger numbers", "× 10 • 2-digit × 1-digit", "O3", "10.3"))
