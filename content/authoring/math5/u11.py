# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 11 Multiplication and division (11.1 Multiplication, 11.2 Division, 11.3 Tests of divisibility).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(11, "Multiplication and Division", "Number",
         "Multiplying 3-digit numbers by 1-digit numbers and 2-digit by 2-digit numbers, dividing with remainders, and tests of divisibility by 2, 4, 5, 10, 25, 50 and 100.",
         {"O1": {"code": "5Nc.04", "sec": "11.1", "codeNote": "", "t": "Estimate and multiply whole numbers up to 1000 by 1-digit numbers, and 2-digit numbers by 2-digit numbers."},
          "O2": {"code": "5Nc.05", "sec": "11.2", "codeNote": "", "t": "Estimate and divide whole numbers up to 1000 by 1-digit numbers, and decide what to do with remainders."},
          "O3": {"code": "5Nc.06", "sec": "11.3", "codeNote": "", "t": "Use tests of divisibility by 2, 4, 5, 10, 25, 50 and 100."}})

s = U.section("11.1", "Multiplication", ["O1"])
s.idea("Grid method", ["Split numbers into hundreds, tens and ones and multiply each part. 236 × 4 = 800 + 120 + 24 = **944**.",
       "For 2-digit × 2-digit, split both: 34 × 26 = 600 + 80 + 180 + 24 = **884**."], table={"head": ["×", "30", "4"], "rows": [["20", "600", "80"], ["6", "180", "24"]]})
s.check(N("Work out 213 × 3.", 639, o="O1"))
s.check(MC('Before you read on: what is 40 × 30?', '1200', [('120', '4 × 3 = 12, and there are two zeros.'), ('70', 'That adds.')], o='O1'))
s.mistake("Place value", ["30 × 20 is 600, not 60."])


def m1(r):
    a, b = r.randint(100, 999), r.randint(2, 9)
    return N(f"Work out {a} × {b}.", a * b, o="O1")
def m2(r):
    a, b = r.randint(11, 99), r.randint(11, 39)
    return N(f"Work out {a} × {b}.", a * b, o="O1")
def m3(r):
    t1, o1, t2, o2 = r.randint(1, 9) * 10, r.randint(1, 9), r.randint(1, 4) * 10, r.randint(1, 9)
    return TB(f"Complete the grid to work out {t1 + o1} × {t2 + o2}.", ["×", str(t1), str(o1)], [[str(t2), B(t1 * t2), B(o1 * t2)], [str(o2), B(t1 * o2), B(o1 * o2)]], o="O1")
def m4(r):
    a, b = r.randint(110, 890), r.randint(3, 9); e = round(a, -2) * b
    return MC(f"Which is the best estimate for {a} × {b}?", str(e), [str(e * 10), str(e // 10), str(round(a, -2) + b)], o="O1")
def m5(r):
    items = ["notebook", "pen pack", "folder"]; p = [r.randint(12, 99) for _ in items]; k = r.randrange(3); n = r.randint(12, 25)
    return N(f"The price list is in cents. How much do {n} of the {items[k]}s cost, in cents?", p[k] * n, "cents", units=["cents"], o="O1", data={"head": ["Item", *items], "rows": [["Price (cents)", *map(str, p)]]})
def m6(r):
    a, b = r.randint(12, 60), r.randint(12, 30)
    return N(f"A theatre has {a} rows with {b} seats in each. How many seats are there?", a * b, "seats", units=["seats"], o="O1")
def m7(r):
    a, b, c = r.randint(2, 9), r.randint(11, 30), r.randint(2, 5)
    return N(f"Work out {a} × {b} × {c}.", a * b * c, o="O1", d="H")
def m8(r):
    a, b = r.randint(11, 40), r.randint(2, 9)
    return N(f"Find the missing number: ☐ ÷ {b} = {a}", a * b, o="O1", d="H")


s.std([m3, m5, m1, m2, m4, m6, m7, m8], EX("Explain how to work out 23 × 15 with the grid method.", [("split into 20 + 3 and 10 + 5", "20|10|split"), ("200 + 100 + 30 + 15 = 345", "345")], "Split 23 into 20 + 3 and 15 into 10 + 5. Multiply: 20 × 10 = 200, 20 × 5 = 100, 3 × 10 = 30, 3 × 5 = 15. Add: 345.", o="O1"))

s = U.section("11.2", "Division", ["O2"])
s.idea("Sharing and grouping", ["Divide using known facts: 96 ÷ 4 → 80 ÷ 4 = 20 and 16 ÷ 4 = 4, so **24**.",
       "A **remainder** is what is left over. 50 ÷ 6 = 8 r2. In a problem, decide whether to round up or down."], table={"head": ["Split", "80", "16"], "rows": [["÷ 4", "20", "4"]]})
s.check(N("Work out 84 ÷ 4.", 21, o="O2"))
s.check(MC('Before you read on: 47 children, 5 to a table. How many tables are needed?', '10', [('9', '9 tables seat 45; 2 children would have no table.'), ('9.4', 'You need a whole number of tables: round up.')], o='O2'))
s.mistake("Rounding up", ["30 children, 4 per table: 30 ÷ 4 = 7 r2, so 8 tables are needed."])


def d1(r):
    b, q = r.randint(2, 9), r.randint(11, 110)
    return N(f"Work out {b * q} ÷ {b}.", q, o="O2")
def d2(r):
    b, q = r.randint(3, 9), r.randint(12, 99); rem = r.randint(1, b - 1)
    return TB(f"Work out {b * q + rem} ÷ {b}.", ["Answer", "Remainder"], [[B(q), B(rem)]], o="O2")
def d3(r):
    c, k = r.randint(4, 8), r.randint(20, 90)
    if k % c == 0: return None
    return N(f"{k} children go on a trip. Each car takes {c} children. How many cars are needed?", -(-k // c), "cars", units=["cars"], o="O2", d="H")
def d4(r):
    b, k = r.randint(4, 9), r.randint(30, 99)
    if k % b == 0: return None
    return N(f"Muffins are packed in boxes of {b}. How many full boxes can be made from {k} muffins?", k // b, "boxes", units=["boxes"], o="O2")
def d5(r):
    n = r.randint(3, 8); t = n * r.randint(12, 40)
    return N(f"The table shows {t} cards shared equally between {n} players. How many cards does each player get?", t // n, "cards", units=["cards"], o="O2", data={"head": ["Cards", "Players"], "rows": [[str(t), str(n)]]})
def d6(r):
    b, q = r.randint(3, 9), r.randint(12, 60)
    return MC(f"Which is the best estimate for {b * q + r.randint(0, b - 1)} ÷ {b}?", str(round(q, -1)), [str(round(q, -1) * 10), str(round(q, -1) + 30), str(b * 100)], o="O2")
def d7(r):
    b, q = r.randint(3, 9), r.randint(12, 60)
    return N(f"Find the missing number: {b} × ☐ = {b * q}", q, o="O2")
def d8(r):
    b, q, rem = r.randint(3, 9), r.randint(10, 30), 0
    rem = r.randint(1, b - 1)
    return N(f"{b * q + rem} sweets are shared equally between {b} children. How many sweets are left over?", rem, "sweets", units=["sweets"], o="O2", d="H")


s.std([d2, d5, d1, d4, d6, d7, d3, d8], EX("Explain why 7 vans are needed for 50 people if each van holds 8.", [("50 ÷ 8 = 6 remainder 2", "6 r|remainder|6 ?r ?2"), ("the 2 left over need another van", "2 left|another|extra|round up")], "50 ÷ 8 = 6 remainder 2. Six vans carry 48 people, and the 2 left over still need a van, so 7 vans are needed.", o="O2"))

s = U.section("11.3", "Tests of divisibility", ["O3"])
s.idea("Quick checks", ["**÷ 2**: the last digit is even. **÷ 5**: ends in 0 or 5. **÷ 10**: ends in 0. **÷ 100**: ends in 00.",
       "**÷ 4**: the last two digits make a multiple of 4. **÷ 25**: ends in 00, 25, 50 or 75. **÷ 50**: ends in 00 or 50."],
       table={"head": ["Divisible by", "Test"], "rows": [["2", "even last digit"], ["4", "last two digits ÷ 4"], ["5", "ends in 0 or 5"], ["25", "ends 00, 25, 50, 75"], ["50", "ends 00 or 50"], ["100", "ends 00"]]})
s.check(MC("Which number is divisible by 25?", "375", [("360", ""), ("410", ""), ("385", "")], o="O3"))
s.check(MC('Before you read on: is 135 divisible by 5?', 'Yes', [('No', 'It ends in 5.'), ('Only by 3', 'It ends in 5, so 5 divides it.')], o='O3'))
s.mistake("Even is not enough", ["34 is even but not divisible by 4: 34 is not a multiple of 4."])


def v1(r):
    k = pick(r, [2, 4, 5, 10]); ns = r.sample(range(100, 999), 4)
    return GD(f"Is each number divisible by {k}?", f"÷ {k}?", [(str(n), "Yes" if n % k == 0 else "No") for n in ns], o="O3", extra=["Yes", "No"])
def v2(r):
    n = r.randint(100, 9999)
    return TK("Tick the numbers that divide exactly.", ["2", "4", "5", "10"], [(str(n), ["✓" if n % k == 0 else "✗" for k in (2, 4, 5, 10)])], o="O3")
def v3(r):
    k = pick(r, [4, 25, 50]); m = k * r.randint(5, 80)
    return MC(f"Which number is divisible by {k}?", str(m), [str(m + 1), str(m + 2), str(m + 10 if k != 10 else m + 3)], o="O3")
def v4(r):
    n = r.randint(1000, 9999)
    return MC(f"Is {n} divisible by 4?", "Yes" if n % 4 == 0 else "No", ["No" if n % 4 == 0 else "Yes"], o="O3", reason=f"The last two digits are {n % 100:02d}.")
def v5(r):
    a = r.randint(1, 9) * 10 + r.randint(0, 9)
    ds = [d for d in range(10) if (a * 10 + d) % 4 == 0]
    return N(f"Find the smallest digit that makes {a}☐ divisible by 4.", ds[0], o="O3", d="H")
def v6(r):
    k = pick(r, [25, 50, 100]); lo = r.randint(110, 900)
    return N(f"What is the first number after {lo} that is divisible by {k}?", (lo // k + 1) * k, o="O3", d="H")
def v7(r):
    ns = r.sample([100, 150, 175, 200, 225, 250, 310, 405, 500, 625], 4)
    return GD("Is each number divisible by 25, 50 or 100? Choose the biggest that works.", "Biggest", [(str(n), "100" if n % 100 == 0 else "50" if n % 50 == 0 else "25" if n % 25 == 0 else "none") for n in ns], o="O3", extra=["25", "50", "100", "none"], d="H")
def v8(r):
    n = r.randint(20, 99) * 2
    return N(f"How many of these divide exactly into {n}: 2, 4, 5, 10?", sum(1 for k in (2, 4, 5, 10) if n % k == 0), o="O3")


s.std([v1, v2, v3, v4, v8, v5, v6, v7], EX("Explain how you know 316 is divisible by 4.", [("the last two digits are 16", "16|last two"), ("16 is a multiple of 4", "multiple of 4|16 ?÷ ?4|4 ?× ?4")], "Look at the last two digits: 16. 16 is a multiple of 4 (4 × 4), so 316 is divisible by 4.", o="O3"))

U.mindmap(("Multiplication", "Grid method • estimate first", "O1", "11.1"), ("Division", "Known facts • remainders in context", "O2", "11.2"), ("Divisibility", "2, 4, 5, 10, 25, 50, 100", "O3", "11.3"))
