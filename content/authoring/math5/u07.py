# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 7 Fractions, decimals and percentages (7.1 Understanding fractions,
7.2 Percentages, decimals and fractions, 7.3 Equivalence and comparison). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(7, "Fractions, Decimals and Percentages", "Number",
         "Fractions of shapes and amounts, fractions as division, percentages as parts of 100, and comparing fractions, decimals and percentages.",
         {"O1": {"code": "5Nf.01", "sec": "7.1", "codeNote": "", "t": "Understand that a fraction can be a part of a whole or a division, and find unit and non-unit fractions of amounts."},
          "O2": {"code": "5Nf.02", "sec": "7.2", "codeNote": "", "t": "Understand percentages as parts of 100 and recognise percentages, decimals and fractions with the same value."},
          "O3": {"code": "5Nf.03", "sec": "7.3", "codeNote": "", "t": "Recognise equivalent fractions and compare and order fractions and decimals."}})

s = U.section("7.1", "Understanding fractions", ["O1"])
s.idea("Parts of a whole", ["A fraction shows equal parts of a whole. In **3/5**, the whole is split into **5** equal parts (the denominator) and we have **3** of them (the numerator).",
       "A fraction is also a **division**: 3/5 = 3 ÷ 5."], fig=PIE(5, [0, 1, 2]))
s.check(N("Find 1/4 of 28.", 7, o="O1"))
s.idea("Fractions of amounts", ["To find 3/4 of 20: 20 ÷ 4 = 5 (one quarter), then 5 × 3 = **15**."])
s.check(MC('Before you read on: which is bigger, 3/4 or 3/5?', '3/4', [('3/5', 'Quarters are bigger pieces than fifths.'), ('They are equal', 'The pieces are different sizes.')], o='O1'))
s.mistake("Equal parts", ["A shape split into 4 unequal pieces is not split into quarters."])


def f1(r):
    d = pick(r, [2, 3, 4, 5, 6, 8, 10]); k = r.randint(2, 12)
    return N(f"Find 1/{d} of {d * k}.", k, o="O1")
def f2(r):
    d = pick(r, [3, 4, 5, 6, 8]); n = r.randint(2, d - 1); k = r.randint(2, 10)
    if Fr(n, d).denominator != d: return None
    return N(f"Find {n}/{d} of {d * k}.", n * k, o="O1")
def f3(r):
    d = pick(r, [3, 4, 5, 6, 8]); n = r.randint(1, d - 1)
    return S("What fraction of the circle is shaded?", [f"{n}/{d}"] + ([frac(Fr(n, d))] if Fr(n, d).denominator != d else []), o="O1", fig=PIE(d, range(n)))
def f4(r):
    d = pick(r, [4, 5, 8, 10]); n = r.randint(1, d - 1); k = r.randint(2, 8)
    return TB(f"Complete the table for {d * k} sweets.", ["Fraction", f"1/{d}", f"{n}/{d}"], [["Sweets", B(k), B(n * k)]], o="O1")
def f5(r):
    a, b = r.randint(1, 7), r.randint(2, 9)
    if a >= b: return None
    return S(f"{a} cakes are shared equally between {b} children. What fraction of a cake does each child get?", [f"{a}/{b}"], o="O1")
def f6(r):
    d = pick(r, [3, 4, 5]); n = r.randint(1, d - 1); k = r.randint(3, 10)
    return N(f"A class has {d * k} children. {n}/{d} of them walk to school. How many do not walk?", (d - n) * k, "children", units=["children"], o="O1", d="H")
def f7(r):
    d = pick(r, [2, 3, 4]); k = r.randint(3, 12)
    return N(f"1/{d} of a number is {k}. What is the number?", d * k, o="O1", d="H")
def f8(r):
    d = pick(r, [4, 6, 8]); n = r.randint(1, d - 1)
    return N(f"What fraction of the circle is NOT shaded? Give the numerator when the denominator is {d}.", d - n, o="O1", fig=PIE(d, range(n)))


s.std([f3, f4, f1, f2, f5, f8, f6, f7], EX("Explain how to find 2/3 of 18.", [("divide 18 by 3 to get 6", "18 ?÷ ?3|\\b6\\b|divide by 3"), ("multiply 6 by 2 to get 12", "× ?2|12")], "First find 1/3 of 18: 18 ÷ 3 = 6. Then 2/3 is two of those: 6 × 2 = 12.", o="O1"))

s = U.section("7.2", "Percentages, decimals and fractions", ["O2"])
s.idea("Per cent means out of 100", ["**37%** means 37 out of 100. On a 100 square it is 37 small squares.",
       "50% = 1/2 = 0.5, 25% = 1/4 = 0.25, 10% = 1/10 = 0.1, 1% = 1/100 = 0.01."], fig={"kind": "waffle", "n": 37})
s.check(N("What percentage is 1/2?", 50, "%", units=["%"], o="O2"))
s.check(MC('Before you read on: what is 0.7 as a percentage?', '70%', [('7%', '0.7 = 70 hundredths.'), ('0.7%', 'Multiply by 100.')], o='O2'))
s.mistake("0.3 is 30%", ["0.3 is 3 tenths = 30 hundredths = 30%, not 3%."])
EQ = [(Fr(1, 2), "0.5", 50), (Fr(1, 4), "0.25", 25), (Fr(3, 4), "0.75", 75), (Fr(1, 10), "0.1", 10), (Fr(3, 10), "0.3", 30), (Fr(7, 10), "0.7", 70), (Fr(1, 5), "0.2", 20), (Fr(1, 100), "0.01", 1)]


def c1(r):
    p = r.randint(5, 95)
    return N("What percentage of the 100 square is shaded?", p, "%", units=["%"], o="O2", fig={"kind": "waffle", "n": p})
def c2(r):
    p = r.randint(5, 95)
    return N("What percentage of the 100 square is NOT shaded?", 100 - p, "%", units=["%"], o="O2", fig={"kind": "waffle", "n": p})
def c3(r):
    f = pick(r, EQ)
    return N(f"Write {frac(f[0])} as a percentage.", f[2], "%", units=["%"], o="O2")
def c4(r):
    f = pick(r, EQ)
    return N(f"Write {f[2]}% as a decimal.", float(f[1]), o="O2")
def c5(r):
    fs = r.sample(EQ, 3)
    return TB("Complete the table.", ["Fraction", "Decimal", "Percentage"], [[frac(f[0]), B(float(f[1])), B(f[2])] for f in fs], o="O2")
def c6(r):
    p = r.randint(1, 99)
    return N(f"Write {p}% as a decimal.", p / 100, o="O2")
def c7(r):
    p = r.randint(10, 90)
    return N(f"{p}% of the children in a class have a pet. What percentage do not?", 100 - p, "%", units=["%"], o="O2")
def c8(r):
    fs = r.sample(EQ, 4)
    return MT("Match each fraction to the equal percentage.", [(frac(f[0]), f"{f[2]}%") for f in fs], o="O2", d="H")


s.std([c1, c5, c2, c3, c4, c6, c7, c8], EX("Explain why 0.25 is the same as 25%.", [("0.25 is 25 hundredths", "25 hundredths|25/100"), ("per cent means out of 100", "out of 100|per cent|hundred")], "0.25 is 25 hundredths, which is 25 out of 100. Per cent means out of 100, so 0.25 = 25%.", o="O2"))

s = U.section("7.3", "Equivalence and comparison", ["O3"])
s.idea("Equivalent fractions", ["**Equivalent fractions** have the same value: 1/2 = 2/4 = 3/6 = 4/8. Multiply (or divide) the numerator and denominator by the same number.",
       "To compare fractions, give them the same denominator: 2/3 = 8/12 and 3/4 = 9/12, so 2/3 < 3/4."], fig=PIE(8, range(4)))
s.check(N("Find the missing number: 2/5 = ☐/10", 4, o="O3"))
s.check(MC('Before you read on: which is bigger: 0.3, 1/4 or 35%?', '35%', [('0.3', '0.3 = 30%.'), ('1/4', '1/4 = 25%.')], o='O3'))
s.mistake("More parts, smaller parts", ["1/6 is smaller than 1/4: sixths are smaller pieces than quarters."])


def e1(r):
    n, d = r.randint(1, 4), pick(r, [3, 4, 5, 6]); k = r.randint(2, 5)
    if n >= d: return None
    return N(f"Find the missing number: {n}/{d} = ☐/{d * k}", n * k, o="O3")
def e2(r):
    a, b = r.sample([2, 3, 4, 5, 6, 8, 10], 2)
    return CMP(f"1/{a}", f"1/{b}", "<" if a > b else ">", o="O3")
def e3(r):
    d = pick(r, [6, 8, 10, 12]); a, b = r.sample(range(1, d), 2)
    return CMP(f"{a}/{d}", f"{b}/{d}", "<" if a < b else ">", o="O3")
def e4(r):
    xs = r.sample([0.3, 0.45, 0.5, 0.07, 0.62, 0.9, 0.25, 0.71], 4)
    return OD("Put these decimals in order, smallest first.", [fmt(x) for x in sorted(xs)], o="O3")
def e5(r):
    d = pick(r, [2, 3, 4]); k = r.randint(2, 4)
    return MC(f"Which fraction is equivalent to 1/{d}?", f"{k}/{d * k}", [f"{k}/{d + k}", f"1/{d * k}", f"{d}/{k}"], o="O3")
def e6(r):
    d = pick(r, [4, 6, 8]); n = d // 2
    return MC("The circle is shaded. Which fraction is equal to the shaded part?", "1/2", ["1/4", "3/4", f"1/{d}"], o="O3", fig=PIE(d, range(n)))
def e7(r):
    n, d = pick(r, [(2, 4), (3, 6), (4, 8), (5, 10), (2, 6), (3, 9), (4, 12), (6, 8)])
    return S(f"Write {n}/{d} in its simplest form.", [frac(Fr(n, d))], o="O3", d="H")
def e8(r):
    fs = r.sample([(1, 2), (1, 4), (3, 4), (1, 3), (2, 3)], 3)
    return OD("Put these fractions in order, smallest first.", [f"{a}/{b}" for a, b in sorted(fs, key=lambda x: x[0] / x[1])], o="O3", d="H")

def e9(r):
    n, d = pick(r, [(2, 4), (2, 8), (4, 8), (6, 8), (3, 6), (2, 6), (4, 6), (3, 9), (6, 9)])
    return S("What fraction of the circle is shaded? Give it in its simplest form.", [frac(Fr(n, d))], o="O3", fig=PIE(d, range(n)))


s.std([e6, e9, e1, e2, e3, e4, e5, e7, e8], EX("Explain why 3/4 is bigger than 2/3.", [("change both to twelfths: 9/12 and 8/12", "9/12|8/12|twelfths"), ("9 twelfths is more than 8 twelfths", "9 ?> ?8|more|bigger")], "Give them the same denominator: 3/4 = 9/12 and 2/3 = 8/12. 9 twelfths is more than 8 twelfths, so 3/4 is bigger.", o="O3"))

U.mindmap(("Fractions", "Parts of a whole • fractions of amounts", "O1", "7.1"), ("Percentages", "Out of 100 • 50% = 1/2 = 0.5", "O2", "7.2"), ("Equivalence", "Same value • compare with common denominators", "O3", "7.3"))
