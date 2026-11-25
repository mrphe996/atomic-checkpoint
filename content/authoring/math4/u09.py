# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 9 Comparing, rounding and dividing (9.1 Rounding, ordering and comparing whole numbers,
9.2 Division of 2-digit numbers). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(9, "Comparing, Rounding and Dividing", "Number",
         "Rounding to the nearest 10, 100 and 1000, ordering and comparing 4-digit numbers, and dividing 2-digit numbers by 1-digit numbers with remainders.",
         {"O1": {"code": "4Np.02", "sec": "9.1", "codeNote": "", "t": "Round numbers to the nearest 10, 100 or 1000, and order and compare 4-digit numbers."},
          "O2": {"code": "4Nc.05", "sec": "9.2", "codeNote": "", "t": "Divide 2-digit numbers by 1-digit numbers, including answers with remainders."}})

s = U.section("9.1", "Rounding, ordering and comparing whole numbers", ["O1"])
s.idea("Rounding", ["To round to the nearest **10**, look at the ones; to the nearest **100**, look at the tens; to the nearest **1000**, look at the hundreds. 5 or more rounds up.",
       "6478 → 6480 (nearest 10), 6500 (nearest 100), 6000 (nearest 1000)."], table={"head": ["Number", "Nearest 10", "Nearest 100", "Nearest 1000"], "rows": [["6478", "6480", "6500", "6000"]]})
s.check(N("Round 3750 to the nearest 1000.", 4000, o="O1"))
s.check(MC('Before you read on: round 4 650 to the nearest hundred.', '4 700', [('4 600', '50 rounds up.'), ('5 000', 'That is the nearest thousand.')], o='O1'))
s.mistake("Look at one digit", ["To round 6478 to the nearest 1000, only the hundreds digit (4) matters."])


def r1(r):
    n = r.randint(101, 9999)
    if n % 10 == 0: return None
    return N(f"Round {n} to the nearest 10.", (n + 5) // 10 * 10, o="O1")
def r2(r):
    n = r.randint(1001, 9949)
    if n % 100 == 0: return None
    return N(f"Round {n} to the nearest 100.", (n + 50) // 100 * 100, o="O1")
def r3(r):
    n = r.randint(1001, 9499)
    return N(f"Round {n} to the nearest 1000.", (n + 500) // 1000 * 1000, o="O1")
def r4(r):
    ns = r.sample(range(1001, 9999), 2)
    return TB("Round each number.", ["Number", "Nearest 10", "Nearest 100", "Nearest 1000"], [[str(n), B((n + 5) // 10 * 10), B((n + 50) // 100 * 100), B((n + 500) // 1000 * 1000)] for n in ns], o="O1")
def r5(r):
    a, b = r.sample(range(1000, 9999), 2)
    return CMP(str(a), str(b), "<" if a < b else ">", o="O1")
def r6(r):
    xs = r.sample(range(1000, 9999), 4)
    return OD("Put these numbers in order, smallest first.", [str(x) for x in sorted(xs)], o="O1")
def r7(r):
    v = r.randint(1001, 9949)
    return N(f"A town has {v} people. About how many is that to the nearest 100?", (v + 50) // 100 * 100, "people", units=["people"], o="O1")
def r8(r):
    t = r.randint(2, 9) * 1000
    return N(f"What is the smallest whole number that rounds to {t} (nearest 1000)?", t - 500, o="O1", d="H")
def r9(r):
    t = r.randint(10, 98); v = t * 10 + r.randint(1, 9)
    return N("The arrow points to a number. Round it to the nearest 10.", (v + 5) // 10 * 10, o="O1", fig={"kind": "numline", "min": t, "max": t + 1, "minor": 10, "ticks": [], "mark": v / 10})


s.std([r4, r9, r1, r2, r3, r5, r6, r7, r8], EX("Explain how to round 4362 to the nearest 1000.", [("look at the hundreds digit, 3", "hundreds|the 3"), ("3 is less than 5, so round down to 4000", "4000|round down")], "Look at the hundreds digit, 3. It is less than 5, so round down: 4362 rounds to 4000.", o="O1"))

s = U.section("9.2", "Division of 2-digit numbers", ["O2"])
s.idea("Dividing and remainders", ["To divide 72 ÷ 4, split 72 into 40 + 32: 40 ÷ 4 = 10 and 32 ÷ 4 = 8, so **72 ÷ 4 = 18**.",
       "If it doesn't divide exactly, there is a **remainder**: 25 ÷ 4 = 6 r1. In a story, decide whether to round up or down."], table={"head": ["Split", "40", "32"], "rows": [["÷ 4", "10", "8"]]})
s.check(N("Work out 84 ÷ 4.", 21, o="O2"))
s.check(MC('Before you read on: what is 84 ÷ 4?', '21', [('24', '80 ÷ 4 = 20 and 4 ÷ 4 = 1.'), ('12', 'Check: 12 × 4 = 48.')], o='O2'))
s.mistake("Remainder too big", ["The remainder must be smaller than the number you divide by: 25 ÷ 4 is 6 r1, not 5 r5."])


def d1(r):
    b, q = r.randint(2, 9), r.randint(11, 30)
    if b * q > 99: return None
    return N(f"Work out {b * q} ÷ {b}.", q, o="O2")
def d2(r):
    b = r.randint(3, 9); q = r.randint(3, 99 // b - 1); rem = r.randint(1, b - 1)
    return TB(f"Work out {b * q + rem} ÷ {b}.", ["Answer", "Remainder"], [[B(q), B(rem)]], o="O2")
def d3(r):
    c, k = r.randint(4, 8), r.randint(20, 99)
    if k % c == 0: return None
    return N(f"{k} children go to a park. Each minibus takes {c} children. How many minibuses are needed?", -(-k // c), "minibuses", units=["minibuses"], o="O2", d="H")
def d4(r):
    b, k = r.randint(3, 9), r.randint(20, 99)
    if k % b == 0: return None
    return N(f"Eggs are packed in boxes of {b}. How many full boxes can be made from {k} eggs?", k // b, "boxes", units=["boxes"], o="O2")
def d5(r):
    n = r.randint(2, 6); t = n * r.randint(11, 99 // n)
    return N(f"The table shows {t} cards shared equally between {n} children. How many cards does each child get?", t // n, "cards", units=["cards"], o="O2", data={"head": ["Cards", "Children"], "rows": [[str(t), str(n)]]})
def d6(r):
    b = r.randint(3, 9); q = r.randint(3, 99 // b - 1); rem = r.randint(1, b - 1)
    return N(f"{b * q + rem} sweets are shared equally between {b} friends. How many are left over?", rem, "sweets", units=["sweets"], o="O2")
def d7(r):
    b, q = r.randint(3, 9), r.randint(4, 11)
    return N(f"Find the missing number: {b} × ☐ = {b * q}", q, o="O2")
def d8(r):
    b, q = r.randint(3, 6), r.randint(12, 33)
    if b * q > 99: return None
    return MC(f"Which is the best estimate for {b * q} ÷ {b}?", str(round(q, -1)), [str(round(q, -1) * 10), str(round(q, -1) + 30), str(b * 10 + 50)], o="O2")


s.std([d2, d5, d1, d4, d6, d7, d3, d8], EX("Explain why 6 cars are needed for 22 children if each car takes 4.", [("22 ÷ 4 = 5 remainder 2", "5 r|remainder|5 ?r ?2"), ("the 2 left over need another car", "2 left|another|extra|round up")], "22 ÷ 4 = 5 remainder 2. Five cars carry 20 children, and the 2 left over still need a car, so 6 cars are needed.", o="O2"))

U.mindmap(("Rounding", "Nearest 10, 100 and 1000", "O1", "9.1"), ("Ordering", "Compare thousands first", "O1", "9.1"), ("Division", "Split the number • remainders", "O2", "9.2"))
