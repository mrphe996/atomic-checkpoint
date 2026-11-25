# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 10 Multiplication and division (1) (10.1 Multiplication, 10.2 Division,
10.3 Tests of divisibility). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *

U = Unit(10, "Multiplication and Division (1)", "Number",
         "Multiplying whole numbers up to 4 digits by 2-digit numbers, dividing by 1- and 2-digit numbers, remainders, and tests of divisibility.",
         {"O1": {"code": "6Nc.04", "sec": "10.1", "codeNote": "", "t": "Estimate and multiply whole numbers up to 10 000 by 1-digit or 2-digit numbers."},
          "O2": {"code": "6Nc.05", "sec": "10.2", "codeNote": "", "t": "Estimate and divide whole numbers up to 1000 by 1-digit or 2-digit numbers, and interpret remainders."},
          "O3": {"code": "6Nc.06", "sec": "10.3", "codeNote": "", "t": "Use tests of divisibility by 3, 6 and 9 (and 2, 4, 5, 10, 100)."}})

s = U.section("10.1", "Multiplication", ["O1"])
s.idea("Long multiplication", ["To work out 346 × 27, multiply by 7 and by 20, then add: 346 × 7 = 2422 and 346 × 20 = 6920, so 346 × 27 = **9342**.",
       "Estimate first: 346 × 27 ≈ 350 × 30 = 10 500."], table={"head": ["×", "300", "40", "6"], "rows": [["20", "6000", "800", "120"], ["7", "2100", "280", "42"]]})
s.check(N("Work out 124 × 13.", 1612, o="O1"))
s.check(MC("Before you read on: what is 25 × 4 × 17?", "1700", [("425", "Multiply 25 × 4 = 100 first."), ("1070", "100 × 17 = 1700.")], o="O1"))
s.mistake("The zero", ["When you multiply by the tens digit, remember it is tens: 346 × 2**0**."])


def m1(r):
    a, b = r.randint(100, 999), r.randint(11, 39)
    return N(f"Work out {a} × {b}.", a * b, o="O1")
def m2(r):
    a, b = r.randint(1000, 4999), r.randint(2, 9)
    return N(f"Work out {a} × {b}.", a * b, o="O1")
def m3(r):
    a, b = r.randint(100, 900) // 10 * 10, r.randint(10, 90) // 10 * 10
    return TB(f"Complete the grid to work out {a + 3} × {b + 4}.", ["×", str(a), "3"], [[str(b), B(a * b), B(3 * b)], ["4", B(4 * a), B(12)]], o="O1")
def m4(r):
    a, b = r.randint(110, 890), r.randint(12, 89)
    e = round(a, -2) * round(b, -1)
    return MC(f"Which is the best estimate for {a} × {b}?", str(e), [str(e * 10), str(e // 10), str(round(a, -2) + round(b, -1))], o="O1")
def m5(r):
    p, n = r.randint(12, 95), r.randint(12, 48)
    return N(f"A school buys {n} boxes of pencils. Each box has {p} pencils. How many pencils is that?", p * n, "pencils", units=["pencils"], o="O1")
def m6(r):
    items = ["bananas", "apples", "pears"]; p = [r.randint(15, 60) for _ in range(3)]; k = r.randrange(3); n = r.randint(12, 30)
    return N(f"The price list shows prices in cents. How much do {n} {items[k]} cost, in cents?", p[k] * n, "cents", units=["cents"], o="O1", data={"head": ["Fruit", *items], "rows": [["Price (cents)", *map(str, p)]]})
def m7(r):
    a, b = r.randint(12, 60), r.randint(11, 30)
    return N(f"Find the missing number: ☐ ÷ {b} = {a}", a * b, o="O1", d="H")
def m8(r):
    a, b, c = r.randint(11, 30), r.randint(11, 25), r.randint(2, 9)
    return N(f"Work out {a} × {b} × {c}.", a * b * c, o="O1", d="H")


def j1_1(r):
    a, b = r.randint(12, 49), r.randint(12, 49)
    return MC(f"Which is the best estimate of {a} × {b}?", f"{round(a, -1) * round(b, -1)}", [(f"{round(a, -1) * round(b, -1) * 10}", "Too big by 10 times."), (f"{round(a, -1) + round(b, -1)}", "That adds.")], o="O1", d="H", reason=f"{round(a, -1)} × {round(b, -1)} = {round(a, -1) * round(b, -1)}.")


s.std([m3, m6, m1, m2, m4, m5, m7, m8], EX("Explain how to estimate 498 × 21.", [("round to 500 × 20", "500|20"), ("500 × 20 = 10 000", "10 ?000|10,000")], "Round each number: 498 ≈ 500 and 21 ≈ 20. Then 500 × 20 = 10 000, so the answer is about 10 000.", o="O1"),
      deep=[j1_1])

s = U.section("10.2", "Division", ["O2"])
s.idea("Short and long division", ["Divide from the left: 756 ÷ 6 → 7 ÷ 6 = 1 r1, 15 ÷ 6 = 2 r3, 36 ÷ 6 = 6, so 756 ÷ 6 = **126**.",
       "A **remainder** is what is left over. In a story, decide whether to **round up** (buses needed) or **round down** (full boxes)."], table={"head": ["", "1", "2", "6"], "rows": [["6 )", "7", "5", "6"]]})
s.check(N("Work out 504 ÷ 4.", 126, o="O2"))
s.check(MC("Before you read on: 50 children go on a trip. Each minibus holds 12. How many minibuses are needed?", "5", [("4", "4 buses hold 48, leaving 2 children behind."), ("4.17", "You cannot have part of a minibus: round up.")], o="O2"))
s.mistake("Remainders in context", ["70 children, 30 per bus: 70 ÷ 30 = 2 r10, so you need 3 buses, not 2."])


def v1(r):
    b, q = r.randint(3, 9), r.randint(21, 140)
    return N(f"Work out {b * q} ÷ {b}.", q, o="O2")
def v2(r):
    b, q = r.randint(11, 25), r.randint(12, 40)
    return N(f"Work out {b * q} ÷ {b}.", q, o="O2")
def v3(r):
    b, q, rem = r.randint(3, 9), r.randint(20, 99), 0
    rem = r.randint(1, b - 1)
    return TB(f"Work out {b * q + rem} ÷ {b}.", ["Quotient", "Remainder"], [[B(q), B(rem)]], o="O2")
def v4(r):
    c, k = r.randint(25, 50), r.randint(100, 400)
    if k % c == 0: return None
    return N(f"{k} people need coaches. Each coach holds {c} people. How many coaches are needed?", -(-k // c), "coaches", units=["coaches"], o="O2", d="H")
def v5(r):
    b, k = r.randint(6, 12), r.randint(100, 500)
    if k % b == 0: return None
    return N(f"Eggs are packed in boxes of {b}. How many full boxes can be made from {k} eggs?", k // b, "boxes", units=["boxes"], o="O2")
def v6(r):
    n = r.randint(3, 8); tot = n * r.randint(15, 90)
    return N(f"The table shows how {tot} stickers are shared equally between {n} friends. How many does each friend get?", tot // n, "stickers", units=["stickers"], o="O2", data={"head": ["Stickers", "Friends"], "rows": [[str(tot), str(n)]]})
def v7(r):
    b, q = r.randint(3, 9), r.randint(15, 80)
    return MC(f"Which is the best estimate for {b * q + r.randint(0, b - 1)} ÷ {b}?", str(round(q, -1)), [str(round(q, -1) * 10), str(round(q, -1) + 30), str(b * 10)], o="O2")
def v8(r):
    b, q = r.randint(11, 19), r.randint(11, 30)
    return N(f"Find the missing number: {b} × ☐ = {b * q}", q, o="O2", d="H")


def j2_1(r):
    n, k = r.randint(40, 99), r.randint(6, 12)
    if n % k == 0: n += 1
    return MC(f"{n} eggs are packed into boxes of {k}. How many boxes can be filled completely?", str(n // k), [(str(n // k + 1), "The last box is not full."), (f"{n / k:.2f}", "You need a whole number of boxes.")], o="O2", d="H", reason=f"{n} ÷ {k} = {n // k} remainder {n % k}.")


s.std([v3, v6, v1, v2, v5, v7, v4, v8], EX("Explain why 100 children need 4 minibuses if each minibus holds 30.", [("100 ÷ 30 = 3 remainder 10", "3 r|remainder|3 ?r ?10"), ("the 10 left over need another bus", "10 left|another|extra|round up")], "100 ÷ 30 = 3 remainder 10. Three buses carry 90 children, and the 10 left over still need a bus, so 4 minibuses are needed.", o="O2"),
      deep=[j2_1])

s = U.section("10.3", "Tests of divisibility", ["O3"])
s.idea("Quick tests", ["A number is divisible by **3** if its **digit sum** is divisible by 3. It is divisible by **9** if its digit sum is divisible by 9.",
       "It is divisible by **6** if it is even and divisible by 3. Divisible by **4** if the last two digits make a multiple of 4."],
       table={"head": ["Divisible by", "Test"], "rows": [["2", "last digit even"], ["3", "digit sum ÷ 3"], ["4", "last two digits ÷ 4"], ["5", "ends in 0 or 5"], ["6", "even and ÷ 3"], ["9", "digit sum ÷ 9"], ["10", "ends in 0"]]})
s.check(MC("Which number is divisible by 9?", "3456", [("3455", ""), ("3454", ""), ("3457", "")], o="O3"))
s.check(MC("Before you read on: is 342 divisible by 9?", "Yes", [("No", "3 + 4 + 2 = 9, which is divisible by 9."), ("Only by 3", "The digit sum 9 is divisible by 9 as well.")], o="O3"))
s.mistake("Even is not enough", ["14 is even but not divisible by 6, because 1 + 4 = 5 is not divisible by 3."])
dsum = lambda n: sum(map(int, str(n)))


def d1(r):
    n = r.randint(100, 9999)
    return N(f"What is the digit sum of {n}?", dsum(n), o="O3")
def d2(r):
    ns = r.sample(range(100, 999), 4); k = pick(r, [3, 9])
    return GD(f"Is each number divisible by {k}?", f"÷ {k}?", [(str(n), "Yes" if n % k == 0 else "No") for n in ns], o="O3", extra=["Yes", "No"])
def d3(r):
    ns = r.sample(range(100, 999), 4)
    return GD("Is each number divisible by 6?", "÷ 6?", [(str(n), "Yes" if n % 6 == 0 else "No") for n in ns], o="O3", extra=["Yes", "No"])
def d4(r):
    k = pick(r, [3, 6, 9]); m = k * r.randint(20, 300)
    ws = [m + 1, m + 2, m + 4]
    return MC(f"Which number is divisible by {k}?", str(m), [str(w) for w in ws], o="O3")
def d5(r):
    n = r.randint(100, 9999)
    return TK("Tick the numbers that divide exactly.", ["2", "3", "5", "9"], [(str(n), ["✓" if n % k == 0 else "✗" for k in (2, 3, 5, 9)])], o="O3", d="H")
def d6(r):
    a, b = r.randint(1, 9), r.randint(0, 9)
    ds = [d for d in range(10) if (a + b + d) % 3 == 0]
    return N(f"Find the smallest digit that makes {a}{b}☐ divisible by 3.", ds[0], o="O3", d="H")
def d7(r):
    n = r.randint(1000, 9999)
    return MC(f"Is {n} divisible by 4?", "Yes" if n % 4 == 0 else "No", ["No" if n % 4 == 0 else "Yes"], o="O3", reason=f"The last two digits are {n % 100:02d}.")
def d8(r):
    k = pick(r, [6, 9]); lo = r.randint(100, 900)
    return N(f"What is the first number after {lo} that is divisible by {k}?", (lo // k + 1) * k, o="O3", d="H")


s.std([d2, d3, d1, d4, d7, d6, d8, d5], EX("Explain how you know 2376 is divisible by 9.", [("the digit sum is 2 + 3 + 7 + 6 = 18", "18|digit sum"), ("18 is divisible by 9", "divisible by 9|18 ?÷ ?9|multiple of 9")], "Add the digits: 2 + 3 + 7 + 6 = 18. 18 is divisible by 9, so 2376 is divisible by 9.", o="O3"))

U.mindmap(("Multiplication", "Grid or long method • estimate first", "O1", "10.1"), ("Division", "Short / long division • remainders in context", "O2", "10.2"), ("Divisibility", "Digit sums for 3 and 9 • even + 3 for 6", "O3", "10.3"))
