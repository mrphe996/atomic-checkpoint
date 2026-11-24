# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 17 Multiplication and division (17.1 Developing written methods of multiplication,
17.2 Developing written methods of division). Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(17, "Multiplication and Division", "Number",
         "Written methods to multiply 2- and 3-digit numbers by 1-digit numbers, and to divide 2- and 3-digit numbers by 1-digit numbers, with remainders.",
         {"O1": {"code": "4Nc.08", "sec": "17.1", "codeNote": "", "t": "Use written methods to multiply 2- and 3-digit numbers by 1-digit numbers."},
          "O2": {"code": "4Nc.09", "sec": "17.2", "codeNote": "", "t": "Use written methods to divide 2- and 3-digit numbers by 1-digit numbers and interpret remainders."}})

s = U.section("17.1", "Developing written methods of multiplication", ["O1"])
s.idea("Grid and short multiplication", ["**Grid method**: 243 × 4 = 800 + 160 + 12 = **972**.",
       "**Short multiplication**: multiply the ones, then tens, then hundreds, carrying when a product is 10 or more."], table={"head": ["×", "200", "40", "3"], "rows": [["4", "800", "160", "12"]]})
s.check(N("Work out 312 × 3.", 936, o="O1"))
s.mistake("Carry", ["In 47 × 3, 7 × 3 = 21: write 1 and carry 2 tens."])


def m1(r):
    a, b = r.randint(100, 499), r.randint(2, 9)
    return N(f"Work out {a} × {b}.", a * b, o="O1")
def m2(r):
    h, t, o_, b = r.randint(1, 4) * 100, r.randint(1, 9) * 10, r.randint(1, 9), r.randint(2, 6)
    return TB(f"Complete the grid to work out {h + t + o_} × {b}.", ["×", str(h), str(t), str(o_)], [[str(b), B(h * b), B(t * b), B(o_ * b)]], o="O1")
def m3(r):
    a, b = r.randint(110, 490), r.randint(3, 9); e = round(a, -2) * b
    return MC(f"Which is the best estimate for {a} × {b}?", str(e), [str(e * 10), str(e // 10), str(round(a, -2) + b)], o="O1")
def m4(r):
    a, b = r.randint(20, 99), r.randint(3, 9)
    return N(f"Work out {a} × {b}.", a * b, o="O1")
def m5(r):
    p, n = r.randint(105, 250), r.randint(3, 8)
    return N(f"A bike costs ${p}. How much do {n} bikes cost?", p * n, "$", units=["$", "dollars"], o="O1")
def m6(r):
    items = ["tent", "stove", "lamp"]; ps = [r.randint(110, 400) for _ in items]; k = r.randrange(3); n = r.randint(2, 5)
    return N(f"How much do {n} {items[k]}s cost?", ps[k] * n, "$", units=["$", "dollars"], o="O1", data={"head": ["Item", *items], "rows": [["Price ($)", *map(str, ps)]]})
def m7(r):
    a, b = r.randint(100, 300), r.randint(2, 9)
    return N(f"Find the missing number: ☐ ÷ {b} = {a}", a * b, o="O1", d="H")
def m8(r):
    a, b, c = r.randint(11, 40), r.randint(2, 5), r.randint(2, 5)
    return N(f"Work out {a} × {b} × {c}.", a * b * c, o="O1", d="H")


s.std([m2, m6, m1, m3, m4, m5, m7, m8], EX("Explain how to work out 236 × 4.", [("split into 200 + 30 + 6", "200|30|split"), ("800 + 120 + 24 = 944", "944")], "Split 236 into 200 + 30 + 6. 200 × 4 = 800, 30 × 4 = 120 and 6 × 4 = 24. Add: 944.", o="O1"))

s = U.section("17.2", "Developing written methods of division", ["O2"])
s.idea("Short division", ["Divide from the left: 156 ÷ 4 → 15 ÷ 4 = 3 r3, carry the 3 to make 36; 36 ÷ 4 = 9. So **156 ÷ 4 = 39**.",
       "If it doesn't divide exactly, write the **remainder**: 158 ÷ 4 = 39 r2."], table={"head": ["", "0", "3", "9"], "rows": [["4 )", "1", "5", "6"]]})
s.check(N("Work out 135 ÷ 5.", 27, o="O2"))
s.mistake("Check with ×", ["Check: 39 × 4 = 156. If not, look for a mistake."])


def d1(r):
    b, q = r.randint(2, 9), r.randint(12, 110)
    if b * q > 999: return None
    return N(f"Work out {b * q} ÷ {b}.", q, o="O2")
def d2(r):
    b, q = r.randint(3, 9), r.randint(12, 99); rem = r.randint(1, b - 1)
    return TB(f"Work out {b * q + rem} ÷ {b}.", ["Answer", "Remainder"], [[B(q), B(rem)]], o="O2")
def d3(r):
    c, k = r.randint(4, 9), r.randint(100, 300)
    if k % c == 0: return None
    return N(f"{k} people need tables. Each table seats {c}. How many tables are needed?", -(-k // c), "tables", units=["tables"], o="O2", d="H")
def d4(r):
    b, k = r.randint(4, 9), r.randint(100, 400)
    if k % b == 0: return None
    return N(f"Muffins are packed in boxes of {b}. How many full boxes can be made from {k} muffins?", k // b, "boxes", units=["boxes"], o="O2")
def d5(r):
    n = r.randint(3, 8); t = n * r.randint(15, 99)
    return N(f"The table shows {t} stickers shared equally between {n} children. How many each?", t // n, "stickers", units=["stickers"], o="O2", data={"head": ["Stickers", "Children"], "rows": [[str(t), str(n)]]})
def d6(r):
    b, q = r.randint(3, 9), r.randint(12, 99)
    return MC(f"Which multiplication checks that {b * q} ÷ {b} = {q}?", f"{q} × {b}", [f"{q} + {b}", f"{b * q} × {b}"], o="O2")
def d7(r):
    b, q = r.randint(3, 9), r.randint(20, 99)
    return MC(f"Which is the best estimate for {b * q} ÷ {b}?", str(round(q, -1)), [str(round(q, -1) * 10), str(round(q, -1) + 50), str(b * 100)], o="O2")
def d8(r):
    b, q = r.randint(3, 9), r.randint(10, 60); rem = r.randint(1, b - 1)
    return N(f"{b * q + rem} pencils are shared equally between {b} pots. How many pencils are left over?", rem, "pencils", units=["pencils"], o="O2", d="H")


s.std([d2, d5, d1, d4, d6, d7, d3, d8], EX("Explain how to work out 84 ÷ 3.", [("8 ÷ 3 = 2 r2, carry the 2 to make 24", "2 r ?2|carry|24"), ("24 ÷ 3 = 8, so 28", "28")], "Divide the tens first: 8 ÷ 3 = 2 remainder 2. Carry the 2 to make 24 ones. 24 ÷ 3 = 8. So 84 ÷ 3 = 28.", o="O2"))

U.mindmap(("Multiplication", "Grid • short multiplication • carry", "O1", "17.1"), ("Division", "Short division • remainders • check with ×", "O2", "17.2"))
