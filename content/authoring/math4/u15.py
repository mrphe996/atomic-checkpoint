# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 15 Special numbers (15.1 Ordering and comparing numbers, 15.2 Working with special numbers,
15.3 Tests of divisibility). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(15, "Special Numbers", "Number",
         "Ordering and comparing positive and negative numbers, square numbers and multiples, and tests of divisibility by 2, 5, 10, 25, 50 and 100.",
         {"O1": {"code": "4Np.03", "sec": "15.1", "codeNote": "", "t": "Order and compare whole numbers, including negative numbers, using < , > and =."},
          "O2": {"code": "4Ns.02", "sec": "15.2", "codeNote": "", "t": "Recognise square numbers and multiples, and use them to solve problems."},
          "O3": {"code": "4Nc.07", "sec": "15.3", "codeNote": "", "t": "Use tests of divisibility for 2, 5, 10, 25, 50 and 100."}})

s = U.section("15.1", "Ordering and comparing numbers", ["O1"])
s.idea("Using < and >", ["**<** means 'is less than' and **>** means 'is greater than': −6 < −2 and 4250 > 4205.",
       "On a number line, numbers get bigger to the right. Every negative number is less than every positive number."], fig=NL(-8, 8))
s.check(CMP("−5", "−9", ">", o="O1"))
s.check(MC('Before you read on: which is bigger, 1 099 or 1 909?', '1 909', [('1 099', 'Compare the hundreds: 9 hundreds beat 0.'), ('They are equal', 'The digits are in different places.')], o='O1'))
s.mistake("Negative numbers", ["−9 is less than −5, even though 9 is bigger than 5."])


def o1(r):
    a, b = r.sample(range(-20, 20), 2)
    return CMP(sg(a), sg(b), "<" if a < b else ">", o="O1")
def o2(r):
    a, b = r.sample(range(1000, 9999), 2)
    return CMP(str(a), str(b), "<" if a < b else ">", o="O1")
def o3(r):
    xs = r.sample(range(-15, 15), 5)
    return OD("Put these numbers in order, smallest first.", [sg(x) for x in sorted(xs)], o="O1")
def o4(r):
    xs = r.sample(range(-12, 12), 4); k = pick(r, ["smallest", "largest"])
    return N(f"Which is the {k} number: {', '.join(sg(x) for x in xs)}?", min(xs) if k == "smallest" else max(xs), o="O1")
def o5(r):
    a = r.randint(-9, 5)
    return MS(f"Select ALL the numbers less than {sg(a)}.", [sg(a - r.randint(1, 5)), sg(a - 7)], [sg(a + r.randint(1, 5)), sg(a)], o="O1")
def o6(r):
    lo = r.randint(-10, 0); hi = lo + r.randint(6, 12); v = r.randint(lo + 1, hi - 1)
    return N("Which number does the arrow point to?", v, o="O1", fig={"kind": "numline", "min": lo, "max": hi, "mark": v})
def o7(r):
    a, b = r.sample(range(-10, 10), 2)
    return GD("Is each statement true or false?", "True?", [(f"{sg(a)} < {sg(b)}", "true" if a < b else "false"), (f"{sg(a)} > {sg(b)}", "true" if a > b else "false"), (f"{sg(b)} < {sg(a)}", "true" if b < a else "false")], o="O1", extra=["true", "false"])
def o8(r):
    a = r.randint(-8, -1)
    return N(f"Which whole number is exactly halfway between {sg(a)} and {sg(-a)}?", 0, o="O1", d="H")


s.std([o6, o7, o1, o2, o3, o4, o5, o8], EX("Explain why −4 > −10.", [("−4 is to the right of −10 on a number line", "right|closer to 0|nearer"), ("numbers to the right are greater", "greater|bigger|more")], "On a number line −4 is to the right of −10 (closer to zero). Numbers further right are greater, so −4 > −10.", o="O1"))

s = U.section("15.2", "Working with special numbers", ["O2"])
s.idea("Square numbers and multiples", ["A **square number** comes from multiplying a number by itself: 6 × 6 = **36**. Square numbers make square arrays.",
       "A **multiple** is in a times table. A number can be a multiple of several numbers: 12 is a multiple of 2, 3, 4 and 6."], fig={"kind": "cells", "cells": [[i, j] for i in range(4) for j in range(4)]})
s.check(N("What is 7 × 7?", 49, o="O2"))
s.check(MC('Before you read on: is 9 a square number?', 'Yes: 3 × 3', [('No', '3 × 3 = 9.'), ('Only an odd number', 'It is odd AND square.')], o='O2'))
s.mistake("Square, not double", ["5 squared is 5 × 5 = 25, not 10."])


def q1(r):
    n = r.randint(2, 10)
    return N(f"What is {n} × {n}?", n * n, o="O2")
def q2(r):
    n = r.randint(2, 6)
    return N("How many squares are in this square array?", n * n, "squares", units=["squares"], o="O2", fig={"kind": "cells", "cells": [[i, j] for i in range(n) for j in range(n)]})
def q3(r):
    vals = r.sample([4, 9, 16, 25, 36, 49, 64, 81, 100, 12, 20, 30, 45, 50], 4)
    return GD("Is each number a square number?", "Square?", [(str(v), "Yes" if int(v ** 0.5) ** 2 == v else "No") for v in vals], o="O2", extra=["Yes", "No"])
def q4(r):
    ns = r.sample(range(2, 11), 3)
    return TB("Complete the table of square numbers.", ["n", "n × n"], [[str(n), B(n * n)] for n in ns], o="O2")
def q5(r):
    a, b = r.sample([2, 3, 4, 5, 6, 10], 2); lo = r.randint(10, 40)
    m = next(x for x in range(lo + 1, 200) if x % a == 0 and x % b == 0)
    return N(f"What is the first number after {lo} that is a multiple of both {a} and {b}?", m, o="O2", d="H")
def q6(r):
    n = r.randint(3, 10)
    return N(f"A square number is {n * n}. Which number was multiplied by itself?", n, o="O2")
def q7(r):
    k = pick(r, [3, 4, 6, 7, 8, 9]); ns = r.sample(range(10, 100), 4)
    return MS(f"Select ALL the multiples of {k}.", [str(k * r.randint(3, 11)) for _ in range(2)], [str(n) for n in ns if n % k][:2], o="O2")
def q8(r):
    a = r.randint(2, 6)
    return N(f"Work out {a} × {a} + {a + 1} × {a + 1}.", a * a + (a + 1) ** 2, o="O2", d="H")


s.std([q2, q4, q1, q3, q6, q7, q5, q8], EX("Explain why 16 is a square number.", [("4 × 4 = 16", "4 ?× ?4"), ("it makes a 4 by 4 square array", "square|array|4 by 4|itself")], "16 = 4 × 4, a number multiplied by itself. 16 dots make a 4 by 4 square, so 16 is a square number.", o="O2"))

s = U.section("15.3", "Tests of divisibility", ["O3"])
s.idea("Quick tests", ["**÷ 2**: ends in an even digit. **÷ 5**: ends in 0 or 5. **÷ 10**: ends in 0. **÷ 100**: ends in 00.",
       "**÷ 25**: ends in 00, 25, 50 or 75. **÷ 50**: ends in 00 or 50."], table={"head": ["Divisible by", "Last digits"], "rows": [["2", "0, 2, 4, 6, 8"], ["5", "0 or 5"], ["10", "0"], ["25", "00, 25, 50, 75"], ["50", "00 or 50"], ["100", "00"]]})
s.check(MC("Which number is divisible by 25?", "675", [("660", ""), ("640", ""), ("615", "")], o="O3"))
s.check(MC('Before you read on: is 246 divisible by 2?', 'Yes', [('No', 'It ends in 6, an even digit.'), ('Only by 3', 'Even numbers divide by 2.')], o='O3'))
s.mistake("Ends in 5 is not ÷ 25", ["35 ends in 5 but is not divisible by 25."])


def v1(r):
    k = pick(r, [2, 5, 10]); ns = r.sample(range(100, 999), 4)
    return GD(f"Is each number divisible by {k}?", f"÷ {k}?", [(str(n), "Yes" if n % k == 0 else "No") for n in ns], o="O3", extra=["Yes", "No"])
def v2(r):
    n = r.randint(100, 9999)
    return TK("Tick the numbers that divide exactly.", ["2", "5", "10", "25"], [(str(n), ["✓" if n % k == 0 else "✗" for k in (2, 5, 10, 25)])], o="O3")
def v3(r):
    k = pick(r, [25, 50, 100]); m = k * r.randint(3, 80)
    return MC(f"Which number is divisible by {k}?", str(m), [str(m + 5), str(m + 10), str(m - 15)], o="O3")
def v4(r):
    k = pick(r, [25, 50, 100]); lo = r.randint(110, 900)
    return N(f"What is the first number after {lo} that is divisible by {k}?", (lo // k + 1) * k, o="O3")
def v5(r):
    ns = r.sample([100, 150, 175, 200, 225, 250, 310, 405, 500, 625, 120], 4)
    return GD("Choose the biggest of 25, 50 or 100 that divides each number exactly.", "Biggest", [(str(n), "100" if n % 100 == 0 else "50" if n % 50 == 0 else "25" if n % 25 == 0 else "none") for n in ns], o="O3", extra=["25", "50", "100", "none"], d="H")
def v6(r):
    n = r.randint(20, 99) * 10
    return N(f"How many of these divide exactly into {n}: 2, 5, 10, 25, 50, 100?", sum(1 for k in (2, 5, 10, 25, 50, 100) if n % k == 0), o="O3", d="H")
def v7(r):
    n = r.randint(1000, 9999)
    return MC(f"Is {n} divisible by 5?", "Yes" if n % 5 == 0 else "No", ["No" if n % 5 == 0 else "Yes"], o="O3", reason=f"It ends in {n % 10}.")
def v8(r):
    t = pick(r, [125, 150, 175, 225, 250, 275])
    return N(f"How many 25-cent coins make {t} cents?", t // 25, "coins", units=["coins"], o="O3")


s.std([v1, v2, v3, v4, v7, v8, v5, v6], EX("Explain how you know 750 is divisible by 50.", [("it ends in 50", "ends in 50|50"), ("numbers ending in 00 or 50 divide by 50", "00 or 50|divisible by 50")], "750 ends in 50. Numbers that end in 00 or 50 are divisible by 50, so 750 is.", o="O3"))

U.mindmap(("Ordering", "< and > • negatives on the left", "O1", "15.1"), ("Special numbers", "Squares • multiples", "O2", "15.2"), ("Divisibility", "2, 5, 10, 25, 50, 100", "O3", "15.3"))
