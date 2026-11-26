# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 8 Addition and subtraction (2) (8.1 Adding and subtracting decimal numbers,
8.2 Adding and subtracting fractions). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from fractions import Fraction as Fr
from math import gcd
from kit import *

U = Unit(8, "Addition and Subtraction (2)", "Number",
         "Adding and subtracting decimals with up to two decimal places, and adding and subtracting fractions with different denominators.",
         {"O1": {"code": "6Nc.01", "sec": "8.1", "codeNote": "", "t": "Estimate, add and subtract numbers with the same or different number of decimal places."},
          "O2": {"code": "6Nf.04", "sec": "8.2", "codeNote": "", "t": "Add and subtract fractions with different denominators, including mixed numbers."}})
TOL = 1e-6


def F(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction in its simplest form or a mixed number.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}" + (f" = {frac(v, True)}" if v > 1 and v.denominator > 1 else "")), **kw)


def dec(r, lo=1, hi=99, dp=2): return round(r.randint(lo * 10 ** dp, hi * 10 ** dp) / 10 ** dp, dp)


s = U.section("8.1", "Adding and subtracting decimal numbers", ["O1"])
s.idea("Line up the points", ["When you add or subtract decimals, **line up the decimal points** so tenths are under tenths and hundredths under hundredths.",
       "Fill gaps with zeros: 6.4 − 2.75 → 6.40 − 2.75 = **3.65**."], table={"head": ["", "Tens", "Ones", ".", "Tenths", "Hundredths"], "rows": [["", "", "6", ".", "4", "0"], ["−", "", "2", ".", "7", "5"], ["=", "", "3", ".", "6", "5"]]})
s.check(N("Work out 4.6 + 2.35.", 6.95, o="O1"))
s.idea("Estimate first", ["Round to whole numbers to check: 12.8 + 7.15 ≈ 13 + 7 = 20."])
s.check(MC("Before you read on: what is 3.5 + 1.25?", "4.75", [("4.30", "Line up the decimal points: 3.50 + 1.25."), ("1.60", "Line up the points, not the last digits.")], o="O1"))
s.mistake("Points in line", ["3.5 + 1.25 is 4.75, not 1.60. Line up the decimal points, not the last digits."])


def d1(r):
    a, b = dec(r, 1, 50, 1), dec(r, 1, 50, 2)
    return N(f"Work out {fmt(a)} + {fmt(b)}.", round(a + b, 2), o="O1")
def d2(r):
    a, b = dec(r, 10, 90, 1), dec(r, 1, 9, 2)
    return N(f"Work out {fmt(a)} − {fmt(b)}.", round(a - b, 2), o="O1")
def d3(r):
    a = r.randint(5, 30); b = dec(r, 1, 4, 2)
    return N(f"Work out {a} − {fmt(b)}.", round(a - b, 2), o="O1")
def d4(r):
    p = [dec(r, 1, 9, 2) for _ in range(3)]; items = ["pen", "ruler", "notebook"]
    return N("Sara buys one of each item in the price list. How much does she spend altogether?", round(sum(p), 2), "$", units=["$", "dollars"], o="O1", data={"head": ["Item", *items], "rows": [["Price ($)", *[f"{x:.2f}" for x in p]]]})
def d5(r):
    a, b = dec(r, 1, 9, 2), dec(r, 1, 9, 2)
    return TB("Complete the table.", ["", "Answer"], [[f"{fmt(a)} + {fmt(b)}", B(round(a + b, 2))], [f"{fmt(max(a, b))} − {fmt(min(a, b))}", B(round(abs(a - b), 2))]], o="O1")
def d6(r):
    a, b = dec(r, 10, 60, 1), dec(r, 10, 60, 2)
    e = round(a) + round(b)
    return MC(f"Which is the best estimate for {fmt(a)} + {fmt(b)}?", str(e), [str(e + 10), str(e - 10), str(e * 10)], o="O1")
def d7(r):
    t = dec(r, 5, 20, 2); a = dec(r, 1, 4, 2)
    return N(f"A plank is {fmt(t)} m long. {fmt(a)} m is cut off. How long is the rest?", round(t - a, 2), "m", units=["m"], o="O1", d="H")
def d8(r):
    a, t = dec(r, 1, 9, 2), dec(r, 10, 20, 1)
    return N(f"Find the missing number: {fmt(a)} + ☐ = {fmt(t)}", round(t - a, 2), o="O1", d="H")
def d9(r):
    a, b, c = dec(r, 1, 9, 1), dec(r, 1, 9, 2), dec(r, 1, 5, 2)
    return N(f"Work out {fmt(a)} + {fmt(b)} − {fmt(c)}.", round(a + b - c, 2), o="O1", d="H")


def h1_1(r):
    a, b = pick(r, [(5.4, 2.35), (3.6, 1.25), (8.2, 0.45)])
    return MC(f"Sam writes {a} + {b} = {round(int(a * 10) / 100 + b, 2)}. What is the right answer?", f"{a + b:.2f}", [(f"{round(int(a * 10) / 100 + b, 2)}", "He lined up the last digits instead of the decimal points."), (f"{a + b + 1:.2f}", "Check by estimating.")], o="O1", d="H", reason=f"{a:.2f} + {b:.2f} = {a + b:.2f}.")


s.std([d4, d5, d1, d2, d3, d6, d7, d8, d9], EX("Explain how to work out 7 − 2.45.", [("write 7 as 7.00", "7\\.00|zeros"), ("7.00 − 2.45 = 4.55", "4\\.55")], "Write 7 as 7.00 so the decimal places line up, then subtract: 7.00 − 2.45 = 4.55.", o="O1"),
      deep=[h1_1])

s = U.section("8.2", "Adding and subtracting fractions", ["O2"])
s.idea("Common denominators", ["You can only add fractions when the **denominators are the same**. 1/3 + 1/6 = 2/6 + 1/6 = **3/6 = 1/2**.",
       "Find a **common multiple** of the denominators, change each fraction, then add or subtract the numerators."], fig={"kind": "pie", "labels": [""] * 6, "values": [1] * 6, "shade": [0, 1, 2]})
s.check(F("Work out 1/4 + 1/2.", Fr(3, 4), o="O2"))
s.idea("Mixed numbers", ["Add the whole numbers, then the fractions: 1 1/2 + 2 1/4 = 3 + 3/4 = **3 3/4**."])
s.idea("Why we need the same denominator", ["You can only add pieces of the same size. 1/2 + 1/4: change 1/2 into 2/4, then 2/4 + 1/4 = 3/4.",
       "Adding the denominators would change the size of the pieces: 1/2 + 1/4 is NOT 2/6."])
s.mistake("Don't add the bottoms", ["1/2 + 1/3 is not 2/5. Change to sixths: 3/6 + 2/6 = 5/6."])
PAIRS = [(2, 4), (2, 6), (3, 6), (4, 8), (2, 8), (3, 9), (5, 10), (2, 10), (4, 12), (3, 12), (6, 12), (2, 3), (3, 4), (2, 5), (4, 5)]


def g1(r):
    a, b = pick(r, PAIRS); x, y = Fr(r.randint(1, a - 1), a), Fr(r.randint(1, b - 1), b)
    return F(f"Work out {x.numerator}/{a} + {y.numerator}/{b}.", x + y, o="O2")
def g2(r):
    a, b = pick(r, PAIRS); x, y = Fr(r.randint(1, a - 1), a), Fr(r.randint(1, b - 1), b)
    if x <= y: x, y = y, x; a, b = b, a
    if x == y: return None
    return F(f"Work out {x.numerator}/{x.denominator} − {y.numerator}/{y.denominator}.", x - y, o="O2")
def g3(r):
    d = pick(r, [4, 6, 8]); n1, n2 = r.randint(1, d - 1), r.randint(1, d - 1)
    if n1 + n2 >= d: return None
    return F(f"The circle shows {n1}/{d} + {n2}/{d} shaded. What is {n1}/{d} + {n2}/{d}?", Fr(n1 + n2, d), o="O2", fig={"kind": "pie", "labels": [""] * d, "values": [1] * d, "shade": list(range(n1 + n2))})
def g4(r):
    w1, w2 = r.randint(1, 4), r.randint(1, 4); a, b = pick(r, [(2, 4), (4, 8), (3, 6), (2, 8)])
    x, y = Fr(1, a), Fr(1, b)
    return F(f"Work out {w1} 1/{a} + {w2} 1/{b}.", w1 + w2 + x + y, o="O2")
def g5(r):
    a, b = pick(r, PAIRS); n, m = r.randint(1, a - 1), r.randint(1, b - 1); L = a * b // gcd(a, b)
    return TB(f"Change both fractions to {L}ths, then add.", ["Fraction", f"In {L}ths"], [[f"{n}/{a}", B(n * L // a)], [f"{m}/{b}", B(m * L // b)], ["Total", B(n * L // a + m * L // b)]], o="O2")
def g6(r):
    a, b = pick(r, [(2, 4), (3, 6), (4, 8), (2, 6)]); x, y = Fr(1, a), Fr(1, b)
    return F(f"Amy ate {frac(x)} of a cake and Ben ate {frac(y)}. How much was left?", 1 - x - y, o="O2", d="H")
def g7(r):
    w = r.randint(2, 6); d = pick(r, [3, 4, 5, 8]); n = r.randint(1, d - 1)
    return F(f"Work out {w} − {n}/{d}.", w - Fr(n, d), o="O2")
def g8(r):
    a, b = r.sample([Fr(1, 2), Fr(1, 3), Fr(1, 4), Fr(2, 3), Fr(3, 4), Fr(1, 6)], 2)
    t = a + b
    return MC(f"Which is equal to {frac(a)} + {frac(b)}?", frac(t), [f"{a.numerator + b.numerator}/{a.denominator + b.denominator}", frac(t + Fr(1, 12)), frac(abs(a - b)) if a != b else "1"], o="O2", d="H")


def h2_1(r):
    a, b = pick(r, [(Fr(1, 2), Fr(1, 3)), (Fr(1, 4), Fr(1, 2)), (Fr(2, 3), Fr(1, 6))])
    return MC(f"Lia writes {frac(a)} + {frac(b)} = {a.numerator + b.numerator}/{a.denominator + b.denominator}. What is right?", frac(a + b), [(f"{a.numerator + b.numerator}/{a.denominator + b.denominator}", "Do not add the denominators."), (frac(a * b), "That multiplies.")], o="O2", d="H", reason=f"Use a common denominator: {frac(a + b)}.")


s.std([g3, g5, g1, g2, g4, g7, g8, g6], EX("Explain how to work out 2/3 + 1/6.", [("change 2/3 to 4/6", "4/6|sixths"), ("4/6 + 1/6 = 5/6", "5/6")], "The denominators are different, so change 2/3 into sixths: 2/3 = 4/6. Then 4/6 + 1/6 = 5/6.", o="O2"),
      deep=[h2_1])

U.mindmap(("Decimals", "Line up the points • estimate first", "O1", "8.1"), ("Fractions", "Common denominator • mixed numbers", "O2", "8.2"))
