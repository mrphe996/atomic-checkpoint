# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 3 Multiplication and division (3.1 Exploring multiplication and division,
3.2 Connecting 2×, 4× and 8×, 3.3 Connecting 3×, 6× and 9×). Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(3, "Multiplication and Division", "Number",
         "Multiplication as equal groups and arrays, division as sharing and grouping, and the 2, 4, 8, 3, 6 and 9 times tables.",
         {"O1": {"code": "3Nc.03", "sec": "3.1", "codeNote": "", "t": "Understand multiplication as equal groups or arrays and division as sharing or grouping."},
          "O2": {"code": "3Nc.04", "sec": "3.2", "codeNote": "", "t": "Know the 2, 4 and 8 times tables and how they are connected by doubling."},
          "O3": {"code": "3Nc.05", "sec": "3.3", "codeNote": "", "t": "Know the 3, 6 and 9 times tables and how they are connected."}})
ARR = lambda rows, cols: {"kind": "cells", "cells": [[i, j] for i in range(cols) for j in range(rows)]}

s = U.section("3.1", "Exploring multiplication and division", ["O1"])
s.idea("Equal groups and arrays", ["**3 × 4** means 3 groups of 4. An **array** shows it as 3 rows of 4: 3 × 4 = **12**.",
       "**Division** is sharing equally or making equal groups: 12 ÷ 3 = 4. Multiplication and division are **inverses**."], fig=ARR(3, 4))
s.check(N("There are 4 bags with 5 apples in each. How many apples?", 20, "apples", units=["apples"], o="O1"))
s.mistake("Order does not matter for ×", ["3 × 4 and 4 × 3 both make 12, but 12 ÷ 3 is not the same as 3 ÷ 12."])


def e1(r):
    a, b = r.randint(2, 5), r.randint(2, 6)
    return N("How many squares are in this array?", a * b, "squares", units=["squares"], o="O1", fig=ARR(a, b))
def e2(r):
    a, b = r.randint(2, 5), r.randint(2, 6)
    return MC("Which multiplication matches the array?", f"{a} × {b}", [f"{a} + {b}", f"{a + 1} × {b}", f"{a} × {b + 1}"], o="O1", fig=ARR(a, b))
def e3(r):
    g, n = r.randint(2, 6), r.randint(2, 10)
    return N(f"There are {g} plates with {n} biscuits on each. How many biscuits altogether?", g * n, "biscuits", units=["biscuits"], o="O1")
def e4(r):
    g, n = r.randint(2, 6), r.randint(2, 10)
    return N(f"{g * n} sweets are shared equally between {g} children. How many does each child get?", n, "sweets", units=["sweets"], o="O1")
def e5(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return TB(f"Write the fact family for {a}, {b} and {a * b}.", ["Fact", "Answer"], [[f"{a} × {b}", B(a * b)], [f"{b} × {a}", B(a * b)], [f"{a * b} ÷ {a}", B(b)], [f"{a * b} ÷ {b}", B(a)]], o="O1")
def e6(r):
    n, k = r.randint(2, 5), r.randint(2, 8)
    return N(f"{n * k} children get into teams of {n}. How many teams are there?", k, "teams", units=["teams"], o="O1")
def e7(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"Find the missing number: {a} × ☐ = {a * b}", b, o="O1", d="H")
def e8(r):
    a, b = r.randint(2, 6), r.randint(2, 6)
    return N(f"Write {a} + " + " + ".join([str(a)] * (b - 1)) + " as a multiplication and find the answer.", a * b, o="O1")


s.std([e1, e2, e5, e3, e4, e6, e8, e7], EX("Explain why 4 × 3 gives the same answer as 3 × 4.", [("an array of 3 rows of 4 can be turned to show 4 rows of 3", "turn|array|rows"), ("both are 12", "12")], "An array of 3 rows of 4 can be turned round to make 4 rows of 3. It has the same number of squares, 12, so 4 × 3 = 3 × 4.", o="O1"))

s = U.section("3.2", "Connecting 2×, 4× and 8×", ["O2"])
s.idea("Doubling", ["The **4 times table** is double the 2 times table: 2 × 6 = 12, so 4 × 6 = **24**.",
       "The **8 times table** is double the 4 times table: 4 × 6 = 24, so 8 × 6 = **48**."], table={"head": ["×", "1", "2", "3", "4", "5", "6"], "rows": [["2", "2", "4", "6", "8", "10", "12"], ["4", "4", "8", "12", "16", "20", "24"], ["8", "8", "16", "24", "32", "40", "48"]]})
s.check(N("What is 8 × 4?", 32, o="O2"))
s.mistake("Double, not add 2", ["4 × 7 is double 2 × 7 (14), so 28 – not 14 + 2."])


def t1(r):
    k, n = pick(r, [2, 4, 8]), r.randint(2, 10)
    return N(f"What is {k} × {n}?", k * n, o="O2")
def t2(r):
    k, n = pick(r, [2, 4, 8]), r.randint(2, 10)
    return N(f"What is {k * n} ÷ {k}?", n, o="O2")
def t3(r):
    n = r.randint(2, 10)
    return TB(f"Use doubling to complete the table for {n}.", ["Fact", "Answer"], [[f"2 × {n}", B(2 * n)], [f"4 × {n}", B(4 * n)], [f"8 × {n}", B(8 * n)]], o="O2")
def t4(r):
    n = r.randint(3, 10)
    return N(f"2 × {n} = {2 * n}. Use this to find 4 × {n}.", 4 * n, o="O2")
def t5(r):
    n = r.randint(2, 10)
    return N(f"A spider has 8 legs. How many legs do {n} spiders have?", 8 * n, "legs", units=["legs"], o="O2")
def t6(r):
    k = pick(r, [4, 8]); ns = r.sample(range(1, 90), 4)
    return GD(f"Is each number in the {k} times table (up to {k} × 10)?", "In table?", [(str(x), "Yes" if x % k == 0 and x <= 10 * k else "No") for x in ns], o="O2", extra=["Yes", "No"])
def t7(r):
    n = r.randint(2, 10)
    return N(f"Cars have 4 wheels. How many wheels do {n} cars have?", 4 * n, "wheels", units=["wheels"], o="O2", data={"head": ["Cars", "1", "2", str(n)], "rows": [["Wheels", "4", "8", "?"]]})
def t8(r):
    k = pick(r, [4, 8]); n = r.randint(3, 10)
    return N(f"Count in {k}s: {k}, {2 * k}, {3 * k}, … What is the {n}th number?", k * n, o="O2", d="H")


s.std([t3, t7, t1, t2, t4, t5, t6, t8], EX("Explain how to use 4 × 7 = 28 to find 8 × 7.", [("8 is double 4", "double|twice|× ?2"), ("double 28 is 56", "56")], "8 × 7 is double 4 × 7 because 8 is double 4. Double 28 is 56, so 8 × 7 = 56.", o="O2"))

s = U.section("3.3", "Connecting 3×, 6× and 9×", ["O3"])
s.idea("Linked tables", ["The **6 times table** is double the 3 times table: 3 × 5 = 15, so 6 × 5 = **30**.",
       "The **9 times table** is three times the 3 times table. A trick: 9 × n = 10 × n − n, so 9 × 4 = 40 − 4 = **36**."], table={"head": ["×", "1", "2", "3", "4", "5"], "rows": [["3", "3", "6", "9", "12", "15"], ["6", "6", "12", "18", "24", "30"], ["9", "9", "18", "27", "36", "45"]]})
s.check(N("What is 6 × 7?", 42, o="O3"))
s.mistake("Check with a pattern", ["The digits of answers in the 9 times table add up to 9: 9 × 6 = 54 and 5 + 4 = 9."])


def u1(r):
    k, n = pick(r, [3, 6, 9]), r.randint(2, 10)
    return N(f"What is {k} × {n}?", k * n, o="O3")
def u2(r):
    k, n = pick(r, [3, 6, 9]), r.randint(2, 10)
    return N(f"What is {k * n} ÷ {k}?", n, o="O3")
def u3(r):
    n = r.randint(2, 10)
    return TB(f"Complete the table for {n}.", ["Fact", "Answer"], [[f"3 × {n}", B(3 * n)], [f"6 × {n}", B(6 * n)], [f"9 × {n}", B(9 * n)]], o="O3")
def u4(r):
    n = r.randint(3, 10)
    return N(f"3 × {n} = {3 * n}. Use doubling to find 6 × {n}.", 6 * n, o="O3")
def u5(r):
    n = r.randint(2, 10)
    return N(f"Work out 9 × {n} using 10 × {n} − {n}.", 9 * n, o="O3", d="H")
def u6(r):
    n = r.randint(2, 10)
    return N(f"Eggs come in boxes of 6. How many eggs are in {n} boxes?", 6 * n, "eggs", units=["eggs"], o="O3", data={"head": ["Boxes", "1", "2", str(n)], "rows": [["Eggs", "6", "12", "?"]]})
def u7(r):
    k = pick(r, [3, 6, 9]); ns = r.sample(range(1, 90), 4)
    return GD(f"Is each number in the {k} times table (up to {k} × 10)?", "In table?", [(str(x), "Yes" if x % k == 0 and x <= 10 * k else "No") for x in ns], o="O3", extra=["Yes", "No"])
def u8(r):
    k, n = pick(r, [3, 6, 9]), r.randint(2, 9)
    return N(f"{k * n} pencils are put into pots of {k}. How many pots are needed?", n, "pots", units=["pots"], o="O3")


s.std([u3, u6, u1, u2, u4, u7, u8, u5], EX("Explain how to use 3 × 8 = 24 to find 6 × 8.", [("6 is double 3", "double|twice|× ?2"), ("double 24 is 48", "48")], "6 is double 3, so 6 × 8 is double 3 × 8. Double 24 is 48, so 6 × 8 = 48.", o="O3"))

U.mindmap(("× and ÷", "Groups • arrays • sharing", "O1", "3.1"), ("2, 4, 8", "Double each time", "O2", "3.2"), ("3, 6, 9", "Double 3× for 6× • 9× = 10× − 1×", "O3", "3.3"))
