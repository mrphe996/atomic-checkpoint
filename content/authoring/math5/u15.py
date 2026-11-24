# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 15 Multiplying and dividing fractions and decimals (15.1 Multiplying a fraction by a whole number,
15.2 Multiplying and dividing decimals). Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(15, "Multiplying and Dividing Fractions and Decimals", "Number",
         "Multiplying a unit or non-unit fraction by a whole number, and multiplying and dividing numbers with one decimal place by single-digit numbers.",
         {"O1": {"code": "5Nf.06", "sec": "15.1", "codeNote": "", "t": "Multiply a unit or non-unit fraction by a whole number."},
          "O2": {"code": "5Nc.07", "sec": "15.2", "codeNote": "", "t": "Estimate, multiply and divide numbers with one decimal place by 1-digit whole numbers."}})

s = U.section("15.1", "Multiplying a fraction by a whole number", ["O1"])
s.idea("Repeated addition", ["1/5 × 3 means three lots of 1/5: 1/5 + 1/5 + 1/5 = **3/5**.",
       "2/7 × 3 = 6/7. Multiply the **numerator** only: the parts are still sevenths."], fig=PIE(5, range(3)))
s.check(F("Work out 1/8 × 5.", Fr(5, 8), o="O1"))
s.mistake("Not the denominator", ["1/4 × 3 = 3/4, not 3/12."])


def f1(r):
    d = pick(r, [3, 4, 5, 6, 8, 10]); k = r.randint(2, d - 1)
    return F(f"Work out 1/{d} × {k}.", Fr(k, d), o="O1")
def f2(r):
    d = pick(r, [5, 7, 9, 10]); n = r.randint(2, 3); k = r.randint(2, 3)
    if n * k >= d: return None
    return F(f"Work out {n}/{d} × {k}.", Fr(n * k, d), o="O1")
def f3(r):
    d = pick(r, [4, 5, 6, 8]); k = r.randint(2, d - 1)
    return F(f"The circle shows 1/{d} × {k}. What is the answer?", Fr(k, d), o="O1", fig=PIE(d, range(k)))
def f4(r):
    d = pick(r, [5, 8, 10])
    return TB(f"Complete the table for 1/{d} × k. Write the numerator.", ["k", f"Numerator (over {d})"], [[str(k), B(k)] for k in (2, 3, 4)], o="O1")
def f5(r):
    d = pick(r, [2, 3, 4]); k = r.randint(3, 9)
    return F(f"Each child drinks 1/{d} of a litre of milk. How much do {k} children drink, in litres?", Fr(k, d), o="O1", d="H")
def f6(r):
    d = pick(r, [3, 4, 5]); n = r.randint(1, d - 1); k = r.randint(2, 4)
    return F(f"A recipe needs {n}/{d} of a cup of sugar. How much for {k} batches?", Fr(n * k, d), o="O1")
def f7(r):
    d = pick(r, [6, 8, 10]); k = r.randint(2, 5)
    return MC(f"Which is equal to 1/{d} × {k}?", f"{k}/{d}", [f"{k}/{d * k}", f"1/{d * k}", f"{k + 1}/{d}"], o="O1")
def f8(r):
    d = pick(r, [3, 4, 5]); k = d * r.randint(1, 3)
    return N(f"Work out 1/{d} × {k}. Give a whole number.", k // d, o="O1", d="H")


s.std([f3, f4, f1, f2, f6, f7, f5, f8], EX("Explain why 2/9 × 4 = 8/9.", [("it means four lots of 2/9", "four lots|4 lots|2/9 ?\\+"), ("2 × 4 = 8 ninths; the denominator stays 9", "8|ninths|numerator")], "2/9 × 4 means 2/9 + 2/9 + 2/9 + 2/9. That is 2 × 4 = 8 ninths. The parts are still ninths, so the answer is 8/9.", o="O1"))

s = U.section("15.2", "Multiplying and dividing decimals", ["O2"])
s.idea("Use whole numbers", ["To work out 3.4 × 2, think 34 × 2 = 68, then make it 10 times smaller: **6.8**.",
       "To divide 8.4 ÷ 4, split it: 8 ÷ 4 = 2 and 0.4 ÷ 4 = 0.1, so **2.1**. Estimate to check."], table={"head": ["×", "3", "0.4"], "rows": [["2", "6", "0.8"]]})
s.check(N("Work out 1.3 × 3.", 3.9, o="O2"))
s.mistake("The point", ["0.6 × 3 = 1.8, not 18."])


def d1(r):
    a, b = dec(r, 1, 9, 1), r.randint(2, 9)
    return N(f"Work out {fmt(a)} × {b}.", round(a * b, 1), o="O2")
def d2(r):
    b, q = r.randint(2, 9), dec(r, 1, 9, 1)
    return N(f"Work out {fmt(round(b * q, 1))} ÷ {b}.", q, o="O2")
def d3(r):
    a, b = dec(r, 1, 9, 1), r.randint(2, 9)
    w, dd = int(a), round(a - int(a), 1)
    if dd == 0: return None
    return TB(f"Complete the grid to work out {fmt(a)} × {b}.", ["×", str(w), fmt(dd)], [[str(b), B(w * b), B(round(dd * b, 1))]], o="O2")
def d4(r):
    a, b = dec(r, 2, 9, 1), r.randint(3, 9); e = round(a) * b
    return MC(f"Which is the best estimate for {fmt(a)} × {b}?", str(e), [str(e * 10), str(round(e / 10, 1)), str(e + 20)], o="O2")
def d5(r):
    p, n = dec(r, 1, 5, 1), r.randint(2, 6)
    items = ["apple", "pear", "lemon"]; ps = [p, dec(r, 1, 5, 1), dec(r, 1, 5, 1)]; k = r.randrange(3)
    return N(f"How much do {n} {items[k]}s cost?", round(ps[k] * n, 1), "$", units=["$", "dollars"], o="O2", data={"head": ["Fruit", *items], "rows": [["Price ($)", *[fmt(x) for x in ps]]]})
def d6(r):
    b, q = r.randint(2, 6), dec(r, 1, 6, 1)
    return N(f"A {fmt(round(b * q, 1))} m ribbon is cut into {b} equal pieces. How long is each piece?", q, "m", units=["m"], o="O2")
def d7(r):
    b, q = r.randint(3, 9), dec(r, 2, 9, 1)
    return N(f"Find the missing number: ☐ × {b} = {fmt(round(b * q, 1))}", q, o="O2", d="H")
def d8(r):
    a, b, c = dec(r, 1, 5, 1), r.randint(2, 5), r.randint(2, 5)
    return N(f"Work out {fmt(a)} × {b} × {c}.", round(a * b * c, 1), o="O2", d="H")


s.std([d3, d5, d1, d2, d4, d6, d7, d8], EX("Explain how to work out 4.2 × 3.", [("42 × 3 = 126", "126|4 ?× ?3|12"), ("make it 10 times smaller: 12.6", "12\\.6")], "Work out 42 × 3 = 126, then make the answer 10 times smaller because 4.2 is 42 tenths: 12.6. (Check: 4 × 3 = 12.)", o="O2"))

U.mindmap(("Fraction × whole", "Multiply the numerator", "O1", "15.1"), ("Decimals", "Use whole-number facts • estimate", "O2", "15.2"))
