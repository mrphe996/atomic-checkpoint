# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 14 Multiplication and division (2) (14.1 Multiplying decimals,
14.2 Multiplying and dividing fractions, 14.3 Dividing decimals). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(14, "Multiplication and Division (2)", "Number",
         "Multiplying and dividing decimals by whole numbers, and multiplying and dividing fractions by whole numbers.",
         {"O1": {"code": "6Nc.07", "sec": "14.1", "codeNote": "", "t": "Estimate and multiply numbers with one or two decimal places by whole numbers."},
          "O2": {"code": "6Nf.05", "sec": "14.2", "codeNote": "", "t": "Multiply and divide proper fractions by whole numbers."},
          "O3": {"code": "6Nc.08", "sec": "14.3", "codeNote": "", "t": "Estimate and divide numbers with one or two decimal places by whole numbers."}})
TOL = 1e-6


def F(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction in its simplest form or a mixed number.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}" + (f" = {frac(v, True)}" if v > 1 and v.denominator > 1 else "")), **kw)


def dec(r, lo, hi, dp): return round(r.randint(lo * 10 ** dp, hi * 10 ** dp) / 10 ** dp, dp)


s = U.section("14.1", "Multiplying decimals", ["O1"])
s.idea("Multiply as whole numbers", ["To work out 2.4 × 3, think 24 × 3 = 72, then put the decimal point back: **7.2**. The answer has the same number of decimal places as the decimal.",
       "Estimate to check: 2.4 × 3 ≈ 2 × 3 = 6."], table={"head": ["×", "2", "0.4"], "rows": [["3", "6", "1.2"]]})
s.check(N("Work out 1.7 × 4.", 6.8, o="O1"))
s.check(MC("Before you read on: what is 0.3 × 4?", "1.2", [("12", "3 tenths × 4 = 12 tenths = 1.2."), ("0.12", "Count the decimal places: one.")], o="O1"))
s.mistake("Decimal places", ["0.3 × 4 = 1.2, not 0.12. Only one decimal place is in the question, so only one in the answer."])


def m1(r):
    a, b = dec(r, 1, 20, 1), r.randint(2, 9)
    return N(f"Work out {fmt(a)} × {b}.", round(a * b, 2), o="O1")
def m2(r):
    a, b = dec(r, 1, 9, 2), r.randint(2, 9)
    return N(f"Work out {fmt(a)} × {b}.", round(a * b, 2), o="O1")
def m3(r):
    a, b = dec(r, 1, 9, 1), r.randint(12, 30)
    return N(f"Work out {fmt(a)} × {b}.", round(a * b, 2), o="O1", d="H")
def m4(r):
    a, b = dec(r, 1, 9, 1), r.randint(2, 9)
    w, d = int(a), round(a - int(a), 1)
    if d == 0: return None
    return TB(f"Complete the grid to work out {fmt(a)} × {b}.", ["×", str(w), fmt(d)], [[str(b), B(w * b), B(round(d * b, 2))]], o="O1")
def m5(r):
    items = ["juice", "bread", "cheese"]; p = [dec(r, 1, 6, 2) for _ in items]; k = r.randrange(3); n = r.randint(2, 6)
    return N(f"How much do {n} lots of {items[k]} cost?", round(p[k] * n, 2), "$", units=["$", "dollars"], o="O1", data={"head": ["Item", *items], "rows": [["Price ($)", *[f"{x:.2f}" for x in p]]]})
def m6(r):
    a, b = dec(r, 2, 9, 1), r.randint(3, 9)
    e = round(a) * b
    return MC(f"Which is the best estimate for {fmt(a)} × {b}?", str(e), [str(e * 10), str(round(e / 10, 1)), str(e + 10)], o="O1")
def m7(r):
    l, n = dec(r, 1, 4, 2), r.randint(3, 8)
    return N(f"A ribbon piece is {fmt(l)} m long. How long are {n} pieces altogether?", round(l * n, 2), "m", units=["m"], o="O1")
def m8(r):
    a, b = dec(r, 1, 9, 2), r.randint(11, 25)
    return N(f"Work out {fmt(a)} × {b}.", round(a * b, 2), o="O1", d="H")


s.std([m4, m5, m1, m2, m6, m7, m3, m8], EX("Explain how to work out 0.6 × 7.", [("6 × 7 = 42", "42"), ("there is one decimal place, so 4.2", "4\\.2|one decimal")], "Work out 6 × 7 = 42. 0.6 has one decimal place, so the answer has one decimal place too: 4.2.", o="O1"))

s = U.section("14.2", "Multiplying and dividing fractions", ["O2"])
s.idea("Fraction × whole number", ["2/5 × 3 means three lots of 2/5: 2/5 + 2/5 + 2/5 = **6/5 = 1 1/5**. Multiply the numerator by the whole number.",
       "To divide a fraction by a whole number, multiply the **denominator**: 3/4 ÷ 2 = **3/8**."], fig={"kind": "pie", "labels": [""] * 5, "values": [1] * 5, "shade": [0, 1]})
s.check(F("Work out 3/8 × 2.", Fr(3, 4), o="O2"))
s.check(MC("Before you read on: what is 1/2 × 1/3?", "1/6", [("2/5", "Multiply the tops and the bottoms."), ("2/6", "1 × 1 = 1 on top.")], o="O2"))
s.mistake("Only the top", ["2/5 × 3 is 6/5, not 6/15. The size of the parts (fifths) does not change."])


def f1(r):
    d = pick(r, [3, 4, 5, 6, 8, 10]); n = r.randint(1, d - 1); k = r.randint(2, 6)
    return F(f"Work out {n}/{d} × {k}.", Fr(n, d) * k, o="O2")
def f2(r):
    d = pick(r, [2, 3, 4, 5]); n = r.randint(1, d - 1); k = r.randint(2, 5)
    return F(f"Work out {n}/{d} ÷ {k}.", Fr(n, d) / k, o="O2")
def f3(r):
    d = pick(r, [3, 4, 5, 6]); n = r.randint(1, d - 1); k = r.randint(2, 4)
    if n * k >= d: return None
    return F(f"The circle shows {n}/{d} shaded. What is {n}/{d} × {k}?", Fr(n * k, d), o="O2", fig={"kind": "pie", "labels": [""] * d, "values": [1] * d, "shade": list(range(n))})
def f4(r):
    d = pick(r, [3, 4, 5]); n = r.randint(1, d - 1)
    return TB(f"Complete the table for {n}/{d} × k. Write numerators over {d}.", ["k", "Numerator"], [[str(k), B(n * k)] for k in (2, 3, 4)], o="O2")
def f5(r):
    d = pick(r, [2, 3, 4]); k = r.randint(2, 5)
    return F(f"A cake is cut. Each child gets 1/{d} of a cake. How much cake do {k} children get?", Fr(k, d), o="O2")
def f6(r):
    k = r.randint(2, 6); d = pick(r, [2, 3, 4])
    return F(f"Half a pizza is shared equally between {k} friends. What fraction of the whole pizza does each get?", Fr(1, 2 * k), o="O2", d="H") if d == 2 else F(f"1/{d} of a bar of chocolate is shared equally between {k} children. What fraction of the bar does each get?", Fr(1, d * k), o="O2", d="H")
def f7(r):
    a = pick(r, [Fr(1, 3), Fr(2, 5), Fr(3, 4), Fr(1, 6)]); k = r.randint(2, 5)
    return MC(f"Which is equal to {frac(a)} × {k}?", frac(a * k), [f"{a.numerator * k}/{a.denominator * k}", frac(a / k), f"{a.numerator + k}/{a.denominator}"], o="O2", d="H")
def f8(r):
    d = pick(r, [4, 5, 8]); n = r.randint(1, d - 1); w = r.randint(2, 4)
    return F(f"A recipe needs {n}/{d} cup of oats per batch. How much for {w} batches?", Fr(n * w, d), o="O2")


s.std([f3, f4, f1, f2, f5, f8, f6, f7], EX("Explain why 1/3 ÷ 2 = 1/6.", [("halving a third splits it into two equal parts", "half|split|two parts|share"), ("each part is 1/6 of the whole", "1/6|sixth")], "Dividing 1/3 by 2 means splitting one third into two equal parts. The whole now has 6 parts, so each part is 1/6.", o="O2"))

s = U.section("14.3", "Dividing decimals", ["O3"])
s.idea("Dividing a decimal", ["Divide as usual and keep the decimal point in line: 8.4 ÷ 4 = **2.1**. Split if it helps: 8.4 = 8 + 0.4, 8 ÷ 4 = 2, 0.4 ÷ 4 = 0.1.",
       "Estimate: 18.6 ÷ 3 ≈ 18 ÷ 3 = 6."], table={"head": ["", "2", ".", "1"], "rows": [["4 )", "8", ".", "4"]]})
s.check(N("Work out 9.6 ÷ 3.", 3.2, o="O3"))
s.check(MC("Before you read on: what is 7.2 ÷ 3?", "2.4", [("24", "Keep the decimal point in line."), ("0.24", "7.2 ÷ 3 is about 2.")], o="O3"))
s.mistake("Point in line", ["7.5 ÷ 5 = 1.5, not 15. The point in the answer sits above the point in the question."])


def v1(r):
    b, q = r.randint(2, 9), dec(r, 1, 9, 1)
    return N(f"Work out {fmt(round(b * q, 2))} ÷ {b}.", q, o="O3")
def v2(r):
    b, q = r.randint(2, 9), dec(r, 1, 9, 2)
    return N(f"Work out {fmt(round(b * q, 2))} ÷ {b}.", q, o="O3", d="H")
def v3(r):
    b, q = r.randint(2, 6), dec(r, 1, 9, 1)
    t = round(b * q, 2)
    return N(f"{b} friends share a bill of ${t:.2f} equally. How much does each pay?", q, "$", units=["$", "dollars"], o="O3")
def v4(r):
    b, q = r.randint(3, 8), dec(r, 2, 15, 1)
    t = round(b * q, 2)
    return N(f"A {fmt(t)} m rope is cut into {b} equal pieces. How long is each piece?", q, "m", units=["m"], o="O3")
def v5(r):
    b = r.randint(2, 6); qs = [dec(r, 1, 9, 1) for _ in range(2)]
    return TB("Complete the table.", ["Division", "Answer"], [[f"{fmt(round(b * q, 2))} ÷ {b}", B(q)] for q in qs], o="O3")
def v6(r):
    b, q = r.randint(3, 9), dec(r, 2, 9, 1)
    t = round(b * q, 1); e = round(t) // b
    return MC(f"Which is the best estimate for {fmt(t)} ÷ {b}?", str(round(q)), [str(round(q) * 10), str(round(q / 10, 1)), str(round(q) + 5)], o="O3")
def v7(r):
    n, w = r.randint(3, 6), dec(r, 1, 4, 2)
    return N(f"The table shows the total mass of {n} identical parcels. What is the mass of one parcel?", w, "kg", units=["kg"], o="O3", data={"head": ["Parcels", "Total mass (kg)"], "rows": [[str(n), fmt(round(n * w, 2))]]})
def v8(r):
    b, q = r.randint(11, 15), dec(r, 1, 5, 1)
    return N(f"Work out {fmt(round(b * q, 2))} ÷ {b}.", q, o="O3", d="H")


s.std([v5, v7, v1, v3, v4, v6, v2, v8], EX("Explain how to work out 6.3 ÷ 3.", [("6 ÷ 3 = 2", "6 ?÷ ?3|\\b2\\b"), ("0.3 ÷ 3 = 0.1, so 2.1", "0\\.1|2\\.1")], "Split 6.3 into 6 + 0.3. 6 ÷ 3 = 2 and 0.3 ÷ 3 = 0.1, so 6.3 ÷ 3 = 2.1.", o="O3"))

U.mindmap(("× decimals", "Multiply as whole numbers • same decimal places", "O1", "14.1"), ("Fractions", "× whole: multiply the top • ÷ whole: multiply the bottom", "O2", "14.2"), ("÷ decimals", "Keep the point in line • estimate", "O3", "14.3"))
