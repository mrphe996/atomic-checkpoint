# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 7 Fractions (7.1 Ordering fractions, 7.2 Adding mixed numbers, 7.3 Multiplying fractions,
7.4 Dividing fractions, 7.5 Making fraction calculations easier). Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(7, "Fractions", "Number",
         "Equivalent fractions and ordering, adding and subtracting fractions and mixed numbers, multiplying and dividing fractions by whole numbers, and shortcuts.",
         {"O1": {"code": "7Nf.06", "sec": "7.1", "codeNote": "", "t": "Use equivalent fractions to compare and order fractions, including improper fractions and mixed numbers."},
          "O2": {"code": "7Nf.07", "sec": "7.2", "codeNote": "", "t": "Add and subtract fractions and mixed numbers with different denominators."},
          "O3": {"code": "7Nf.08", "sec": "7.3", "codeNote": "", "t": "Multiply a fraction by a whole number and by another fraction, and find fractions of amounts."},
          "O4": {"code": "7Nf.09", "sec": "7.4", "codeNote": "", "t": "Divide a proper fraction by a whole number."},
          "O5": {"code": "7Nf.10", "sec": "7.5", "codeNote": "", "t": "Use the laws of arithmetic and simplifying to make fraction calculations easier."}})
TOL = 1e-6


def rf(r, dens=(2, 3, 4, 5, 6, 8, 10, 12)):
    d = pick(r, dens); n = r.randint(1, d - 1); return Fr(n, d)


def F(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction in its simplest form or a mixed number.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}" + (f" = {frac(v, True)}" if v > 1 and v.denominator > 1 else "")), **kw)


# ================================================================== 7.1
s = U.section("7.1", "Ordering fractions", ["O1"])
s.idea("Equivalent fractions", ["Multiply or divide the top and bottom by the same number to get an **equivalent fraction**: 2/3 = 4/6 = 8/12.",
       "To compare fractions, give them a **common denominator**: 3/4 = 9/12 and 5/6 = 10/12, so 3/4 < 5/6."], table={"head": ["Fraction", "×2", "×3", "×4"], "rows": [["2/3", "4/6", "6/9", "8/12"]]})
s.check(N("Find the missing number: 3/5 = ☐/20", 12, o="O1"))
s.idea("Improper fractions", ["An **improper fraction** has a numerator bigger than its denominator: 7/4 = 1 3/4 (a **mixed number**)."])
s.mistake("Same number top and bottom", ["2/3 is not equal to 4/5: you must multiply top AND bottom by the same number."])


def o1(r):
    f = rf(r); k = r.randint(2, 6)
    return N(f"Find the missing number: {frac(f)} = ☐/{f.denominator * k}", f.numerator * k, o="O1")
def o2(r):
    a, b = rf(r), rf(r)
    if a == b: return None
    return CMP(frac(a), frac(b), "<" if a < b else ">", o="O1")
def o3(r):
    fs = sorted({rf(r) for _ in range(6)})[:4]
    if len(fs) < 4: return None
    return OD("Put these fractions in order, smallest first.", [frac(f) for f in fs], o="O1")
def o4(r):
    w, f = r.randint(1, 5), rf(r)
    return N(f"Write {w} {f.numerator}/{f.denominator} as an improper fraction. What is the numerator?", w * f.denominator + f.numerator, o="O1")
def o5(r):
    d = pick(r, [3, 4, 5, 6, 8]); n = r.randint(d + 1, 4 * d)
    if n % d == 0: n += 1
    return S(f"Write {n}/{d} as a mixed number.", [frac(Fr(n, d), True)], o="O1")
def o6(r):
    f = rf(r, (2, 3, 4, 5)); vs = [f * k for k in (2, 3, 4)]
    return TB(f"Write fractions equivalent to {frac(f)}.", ["Denominator", "Numerator"], [[str((f.denominator * k)), B(f.numerator * k)] for k in (2, 3, 5)], o="O1")
def o7(r):
    rows = [("1/2", "4/8"), ("2/3", "6/9"), ("3/4", "9/12"), ("2/5", "4/10"), ("1/3", "5/15")]
    return GD("Find the equivalent fraction.", "Equivalent", r.sample(rows, 4), o="O1", extra=["3/5"])
def o8(r):
    nm = r.sample(["Ana", "Bo", "Cy", "Di"], 3); fs = [rf(r, (4, 5, 8, 10)) for _ in range(3)]
    if len(set(fs)) < 3: return None
    w = nm[fs.index(max(fs))]
    return MC("Who ate the biggest fraction of a pizza?", w, [n for n in nm if n != w], o="O1", data={"head": ["Name", *nm], "rows": [["Fraction eaten", *[frac(f) for f in fs]]]})


s.std([o6, o7, o1, o2, o3, o4, o5, o8], EX("Explain how to decide which is bigger, 2/3 or 3/5.", [("write them with a common denominator, 15", ["15|common denominator|same denominator"]), ("10/15 > 9/15, so 2/3 is bigger", ["10/15|9/15|2/3 is"])], "Use a common denominator of 15: 2/3 = 10/15 and 3/5 = 9/15. 10/15 > 9/15, so 2/3 is bigger.", o="O1"))

# ================================================================== 7.2
s = U.section("7.2", "Adding mixed numbers", ["O2"])
s.idea("Adding and subtracting fractions", ["Use a **common denominator**, then add or subtract the numerators: 1/3 + 1/4 = 4/12 + 3/12 = 7/12.",
       "For **mixed numbers**, add the whole numbers, then add the fractions: 2 1/2 + 1 2/3 = 3 + 7/6 = 4 1/6."])
s.check(F("Work out 2/5 + 1/3.", Fr(11, 15), o="O2"))
s.mistake("Do not add the denominators", ["1/2 + 1/3 is NOT 2/5. Use a common denominator: 3/6 + 2/6 = 5/6."])


def a1(r):
    a, b = rf(r), rf(r)
    return F(f"Work out {frac(a)} + {frac(b)}.", a + b, o="O2")
def a2(r):
    a, b = rf(r), rf(r)
    if a <= b: a, b = b, a
    if a == b: return None
    return F(f"Work out {frac(a)} − {frac(b)}.", a - b, o="O2")
def a3(r):
    a, b = r.randint(1, 5) + rf(r, (2, 3, 4, 5)), r.randint(1, 4) + rf(r, (2, 3, 4, 5))
    return F(f"Work out {frac(a, True)} + {frac(b, True)}.", a + b, o="O2")
def a4(r):
    a, b = r.randint(1, 4) + rf(r, (2, 4, 8)), r.randint(1, 4) + rf(r, (2, 4, 8))
    return F(f"A recipe uses {frac(a, True)} cups of flour and {frac(b, True)} cups of sugar. How many cups is that altogether?", a + b, o="O2", units=["cups"])
def a5(r):
    a = rf(r, (3, 4, 5, 6, 8))
    return F(f"Ali eats {frac(a)} of a cake. What fraction is left?", 1 - a, o="O2")
def a6(r):
    a, b = rf(r, (2, 3, 4, 6)), rf(r, (2, 3, 4, 6))
    if a + b >= 1: return None
    return F(f"Mia spends {frac(a)} of her money on books and {frac(b)} on food. What fraction does she have left?", 1 - a - b, o="O2", d="H")
def a7(r):
    a, b = rf(r, (3, 4, 6)), rf(r, (3, 4, 6))
    d = (a + b).denominator
    return TB(f"Work out {frac(a)} + {frac(b)} with a common denominator.", ["Step", "Value"], [["common denominator", B(a.denominator * b.denominator // __import__('math').gcd(a.denominator, b.denominator))], ["answer (as a decimal)", B(float(a + b), 0.001)]], o="O2")
def a8(r):
    l, c = r.randint(3, 6) + rf(r, (2, 4)), r.randint(1, 2) + rf(r, (2, 4))
    return F(f"A ribbon is {frac(l, True)} m long. {frac(c, True)} m is cut off. How much is left?", l - c, o="O2", units=["m"], d="H", fig={"kind": "shape", "pts": [[0, 0], [10, 0], [10, 0.6], [0, 0.6]], "s": [f"{frac(l, True)} m", "", "", ""]})


s.std([a7, a8, a1, a2, a3, a4, a5, a6], EX("Explain why 1/2 + 1/4 = 3/4 and not 2/6.", [("change 1/2 to 2/4 (a common denominator)", ["2/4|common|same denominator|quarters"]), ("2/4 + 1/4 = 3/4; you do not add denominators", ["3/4|denominator"])], "The fractions need a common denominator: 1/2 = 2/4. Then 2/4 + 1/4 = 3/4. Adding the denominators would change the size of the pieces.", o="O2"))

# ================================================================== 7.3
s = U.section("7.3", "Multiplying fractions", ["O3"])
s.idea("Fraction × whole number", ["3 × 2/5 = 6/5 = 1 1/5: multiply the numerator by the whole number.",
       "**Fraction of an amount**: 3/4 of 20 = 20 ÷ 4 × 3 = 15."])
s.idea("Fraction × fraction", ["Multiply the numerators and multiply the denominators: 2/3 × 3/5 = 6/15 = 2/5."])
s.check(N("Find 2/5 of 35.", 14, o="O3"))
s.mistake("Of means multiply", ["1/2 of 1/3 is 1/2 × 1/3 = 1/6."])


def m1(r):
    f, n = rf(r), r.randint(2, 9)
    return F(f"Work out {n} × {frac(f)}.", n * f, o="O3")
def m2(r):
    f = rf(r); k = f.denominator * r.randint(2, 12)
    return N(f"Find {frac(f)} of {k}.", float(f * k), o="O3")
def m3(r):
    a, b = rf(r, (2, 3, 4, 5)), rf(r, (2, 3, 4, 5))
    return F(f"Work out {frac(a)} × {frac(b)}.", a * b, o="O3")
def m4(r):
    f = rf(r, (3, 4, 5, 8)); k = f.denominator * r.randint(3, 15)
    return N(f"A class has {k} students. {frac(f)} of them walk to school. How many walk?", float(f * k), "students", units=["students"], o="O3")
def m5(r):
    f = rf(r, (2, 4, 5)); p = f.denominator * r.randint(5, 30)
    return N(f"A coat costs ${p}. In a sale the price is reduced by {frac(f)}. How much is taken off?", float(f * p), "$", units=["$"], o="O3")
def m6(r):
    a, b = rf(r, (2, 3, 4)), rf(r, (2, 3, 4))
    return F("Find the area of the rectangle (in m²).", a * b, o="O3", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]], "s": [f"{frac(a)} m", f"{frac(b)} m", "", ""]})
def m7(r):
    f = rf(r, (3, 4, 5)); vals = [f.denominator * k for k in r.sample(range(2, 10), 3)]
    return TB(f"Find {frac(f)} of each amount.", ["Amount", f"{frac(f)} of it"], [[str(v), B(float(f * v))] for v in vals], o="O3")
def m8(r):
    a, b = rf(r, (2, 3, 4)), rf(r, (2, 3, 4))
    return F(f"Find {frac(a)} of {frac(b)}.", a * b, o="O3", d="H")


s.std([m6, m7, m1, m2, m3, m4, m5, m8], EX("Explain how to find 3/5 of 40.", [("divide by 5 to find one fifth: 8", ["÷ ?5|one fifth|= ?8|\\b8\\b"]), ("multiply by 3: 24", ["× ?3|24"])], "First find 1/5 of 40 by dividing by 5: 8. Then 3/5 is 3 × 8 = 24.", o="O3"))

# ================================================================== 7.4
s = U.section("7.4", "Dividing fractions", ["O4"])
s.idea("Fraction ÷ whole number", ["Dividing by 2 is the same as finding half: 3/4 ÷ 2 = 3/8.",
       "In general, multiply the **denominator** by the whole number: a/b ÷ n = a/(b × n). Simplify if you can: 4/5 ÷ 2 = 4/10 = 2/5."])
s.check(F("Work out 2/3 ÷ 4.", Fr(1, 6), o="O4"))
s.mistake("Smaller, not bigger", ["Dividing a fraction by a whole number makes it smaller: 1/2 ÷ 3 = 1/6."])


def v1(r):
    f, n = rf(r), r.randint(2, 6)
    return F(f"Work out {frac(f)} ÷ {n}.", f / n, o="O4")
def v2(r):
    f, n = rf(r, (2, 3, 4, 5)), r.randint(2, 5)
    return F(f"{frac(f)} of a pizza is shared equally between {n} people. What fraction does each person get?", f / n, o="O4")
def v3(r):
    f, n = rf(r, (3, 4, 5)), r.randint(2, 4)
    return F(f"{frac(f)} of a litre of juice is poured equally into {n} glasses. How much is in each glass, in litres?", f / n, o="O4", units=["litres", "l"])
def v4(r):
    rows = [("1/2 ÷ 2", "1/4"), ("1/3 ÷ 2", "1/6"), ("3/4 ÷ 3", "1/4"), ("2/5 ÷ 2", "1/5"), ("4/5 ÷ 4", "1/5")]
    return GD("Find each answer.", "Answer", r.sample(rows, 4), o="O4", extra=["1/8", "2/3"])
def v5(r):
    f, n = rf(r), r.randint(2, 6)
    return MC(f"Which is equal to {frac(f)} ÷ {n}?", frac(f / n), [frac(f * n), frac(Fr(f.numerator, f.denominator + n)), frac(Fr(f.numerator + n, f.denominator)) if f.numerator + n != f.denominator else "1"], o="O4")
def v6(r):
    f = rf(r, (2, 3, 4)); ns = r.sample(range(2, 6), 2)
    return TB(f"Divide {frac(f)} by each number. Give decimals to 3 d.p.", ["Divide by", "Answer"], [[str(n), B(round(float(f / n), 3), 0.001)] for n in ns], o="O4")
def v7(r):
    f, n = rf(r, (2, 3, 4)), r.randint(2, 4)
    return F(f"A plank {frac(f)} m long is cut into {n} equal pieces. How long is each piece?", f / n, o="O4", units=["m"], fig={"kind": "shape", "pts": [[0, 0], [10, 0], [10, 0.6], [0, 0.6]], "s": [f"{frac(f)} m", "", "", ""]})


s.std([v4, v6, v1, v2, v3, v5, v7], EX("Explain why 1/2 ÷ 3 = 1/6.", [("sharing a half into 3 equal parts", ["share|3 parts|three parts|split"]), ("each part is one sixth of the whole", ["sixth|6"])], "Dividing a half into 3 equal parts makes 6 parts in the whole, so each part is 1/6.", o="O4"))

# ================================================================== 7.5
s = U.section("7.5", "Making fraction calculations easier", ["O5"])
s.idea("Strategies", ["**Re-order** to make wholes: 1/4 + 2/3 + 3/4 = (1/4 + 3/4) + 2/3 = 1 2/3.",
       "**Simplify first**: 4/8 + 1/2 = 1/2 + 1/2 = 1.", "**Use known facts**: 1/2 = 0.5 = 50%."])
s.check(F("Work out 3/5 + 1/2 + 2/5 mentally.", Fr(3, 2), o="O5"))
s.mistake("Look for wholes", ["Before you find a common denominator, look for fractions that make a whole."])


def e1(r):
    a = rf(r, (3, 4, 5, 8)); b = 1 - a; c = rf(r, (2, 3))
    return F(f"Work out {frac(a)} + {frac(c)} + {frac(b)} mentally.", a + b + c, o="O5")
def e2(r):
    f = rf(r, (2, 4, 5)); k = r.randint(2, 4)
    return F(f"Simplify {f.numerator * k}/{f.denominator * k} first, then add {frac(f)}.", 2 * f, o="O5")
def e3(r):
    rows = [("1/2", "0.5"), ("1/4", "0.25"), ("3/4", "0.75"), ("1/5", "0.2"), ("1/10", "0.1")]
    return GD("Write each fraction as a decimal.", "Decimal", r.sample(rows, 4), o="O5", extra=["0.4"])
def e4(r):
    f = rf(r, (3, 4, 5)); n = r.randint(2, 8)
    return F(f"Work out {frac(f)} × {n} + {frac(f)} × {f.denominator - n % f.denominator if f.denominator - n % f.denominator else f.denominator}.", f * (n + (f.denominator - n % f.denominator or f.denominator)), o="O5", d="H")
def e5(r):
    a = rf(r, (2, 4)); b = rf(r, (2, 4))
    return TB(f"Show that {frac(a)} + {frac(b)} = {frac(b)} + {frac(a)}.", ["Order", "Answer (decimal)"], [[f"{frac(a)} + {frac(b)}", B(float(a + b))], [f"{frac(b)} + {frac(a)}", B(float(a + b))]], o="O5")
def e6(r):
    w = r.randint(2, 6)
    return F(f"Work out {w} − 1/4 − 3/4.", Fr(w - 1), o="O5")
def e7(r):
    return MC("Which pair of fractions add up to exactly 1?", pick(r, ["3/8 and 5/8", "2/5 and 3/5", "1/6 and 5/6"]), ["1/3 and 1/2", "2/5 and 2/3", "3/4 and 1/2"], o="O5")


s.std([e3, e5, e1, e2, e4, e6, e7], EX("Explain the quickest way to work out 1/3 + 5/8 + 2/3.", [("add 1/3 and 2/3 first to make 1", ["1/3 ?\\+ ?2/3|make 1|= ?1|whole"]), ("1 + 5/8 = 1 5/8", ["1 ?5/8|13/8"])], "Re-order: 1/3 + 2/3 = 1, then 1 + 5/8 = 1 5/8. No common denominator is needed.", o="O5"))

U.mindmap(("Ordering", "Equivalent fractions • common denominator", "O1", "7.1"), ("Adding mixed numbers", "Wholes, then fractions • common denominator", "O2", "7.2"),
          ("Multiplying", "Fraction of an amount • multiply tops and bottoms", "O3", "7.3"), ("Dividing", "a/b ÷ n = a/(b × n)", "O4", "7.4"),
          ("Easier calculations", "Make wholes • simplify first", "O5", "7.5"))
