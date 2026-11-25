# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 7 Fractions (7.1 Ordering fractions, 7.2 Adding mixed numbers, 7.3 Multiplying fractions,
7.4 Dividing fractions, 7.5 Making fraction calculations easier). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
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
s.idea("Why multiplying top and bottom keeps the size", ["Cut each third of a bar into 2 equal pieces: there are now 6 pieces, and the 2 shaded thirds have become 4 shaded sixths. The amount shaded has not changed, so 2/3 = 4/6.",
       "Multiplying top and bottom by the same number just cuts every piece into smaller equal pieces."], table={"head": ["", "Pieces", "Shaded"], "rows": [["2/3", "3", "2"], ["4/6", "6", "4"], ["8/12", "12", "8"]]})
s.check(MC("Before you read on: which is bigger, 3/4 or 4/5?", "4/5", [("3/4", "3/4 = 15/20 and 4/5 = 16/20."), ("They are equal", "Write both with denominator 20.")], o="O1", hint="Each is one piece short of a whole. Which missing piece is smaller?"))
s.example("Same numerator, different denominator", "Order 3/5, 3/8 and 3/4.", [("each has 3 pieces", "the numerators are the same"), ("bigger denominator → smaller pieces", "eighths are smaller than fifths, fifths smaller than quarters")], "3/8, 3/5, 3/4",
          p=["When the numerators are equal, you do not need a common denominator."])
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


def x1(r):   # find all equivalent
    f = rf(r, (2, 3, 4, 5)); ks = r.sample(range(2, 7), 2)
    good = [f"{f.numerator * k}/{f.denominator * k}" for k in ks]
    bad = [f"{f.numerator + k}/{f.denominator + k}" for k in r.sample(range(1, 5), 2)]
    return MS(f"Select ALL the fractions equal to {frac(f)}.", good, bad, o="O1", d="H", reason="Equivalent fractions multiply top and bottom by the same number; adding the same number changes the size.")
def x2(r):   # between
    a, b = pick(r, [(Fr(1, 3), Fr(1, 2)), (Fr(2, 5), Fr(1, 2)), (Fr(3, 4), Fr(4, 5)), (Fr(1, 4), Fr(1, 3))])
    good = [frac((a + b) / 2)]; bad = [frac(a / 2), frac(b + Fr(1, 10))]
    return MC(f"Which fraction lies between {frac(a)} and {frac(b)}?", good[0], [(x, "Change all three to a common denominator and compare.") for x in bad], o="O1", d="H",
              reason=f"Halfway between them is {frac((a + b) / 2)}.")
def x3(r):   # spot the error
    return MC("Ben says 1/8 is bigger than 1/6 because 8 is bigger than 6. Is he right?", "No: 1/6 is bigger", [("Yes", "Cutting into 8 pieces makes each piece smaller."), ("They are equal", "1/6 = 4/24 and 1/8 = 3/24.")], o="O1", d="H",
              reason="With the same numerator, the bigger denominator means smaller pieces.")
def x4(r):   # mixed vs improper decision
    w = r.randint(1, 4); f = rf(r, (3, 4, 5)); im = Fr(w) + f
    return MC(f"Which is bigger: {im.numerator}/{im.denominator} or {w + 1}?", str(w + 1), [(f"{im.numerator}/{im.denominator}", f"{im.numerator}/{im.denominator} = {frac(im, True)}, which is less than {w + 1}."), ("They are equal", "Change the improper fraction to a mixed number.")], o="O1", d="H",
              reason=f"{im.numerator}/{im.denominator} = {frac(im, True)} < {w + 1}.")


s.std([o6, o7, o1, o2, o3, o4, o5, o8], EX("Explain how to decide which is bigger, 2/3 or 3/5.", [("write them with a common denominator, 15", ["15|common denominator|same denominator"]), ("10/15 > 9/15, so 2/3 is bigger", ["10/15|9/15|2/3 is"])], "Use a common denominator of 15: 2/3 = 10/15 and 3/5 = 9/15. 10/15 > 9/15, so 2/3 is bigger.", o="O1"),
      deep=[x1, x2, x3, x4])

# ================================================================== 7.2
s = U.section("7.2", "Adding mixed numbers", ["O2"])
s.idea("Adding and subtracting fractions", ["Use a **common denominator**, then add or subtract the numerators: 1/3 + 1/4 = 4/12 + 3/12 = 7/12.",
       "For **mixed numbers**, add the whole numbers, then add the fractions: 2 1/2 + 1 2/3 = 3 + 7/6 = 4 1/6."])
s.check(F("Work out 2/5 + 1/3.", Fr(11, 15), o="O2"))
s.idea("Why we need a common denominator", ["1/2 + 1/4: halves and quarters are different-sized pieces, so we cannot just count them. Change 1/2 into 2/4; now all the pieces are quarters and 2/4 + 1/4 = 3/4.",
       "Adding the denominators would be like saying 2 halves + 1 quarter = 3 sixths: the pieces would change size."])
s.check(MC("Before you read on: is 1/3 + 1/3 equal to 2/6?", "No: 2/3", [("Yes", "2/6 = 1/3, which is less than what we started with."), ("No: 1/9", "Adding should not make it smaller.")], o="O2"))
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


def y1(r):   # spot the error
    a, b = pick(r, [(Fr(1, 2), Fr(1, 3)), (Fr(2, 5), Fr(1, 4)), (Fr(1, 3), Fr(1, 6)), (Fr(3, 4), Fr(1, 8))])
    return MC(f"Kim writes {frac(a)} + {frac(b)} = {a.numerator + b.numerator}/{a.denominator + b.denominator}. What is the correct answer?", frac(a + b),
              [(f"{a.numerator + b.numerator}/{a.denominator + b.denominator}", "The denominators must not be added: the pieces must be the same size first."), (frac(a * b), "That multiplies.")], o="O2", d="H",
              reason=f"Common denominator: {frac(a)} + {frac(b)} = {frac(a + b)}.")
def y2(r):   # missing fraction
    a = rf(r, (3, 4, 6)); t = Fr(1)
    return F(f"Find the missing fraction: {frac(a)} + ☐ = 1.", t - a, o="O2", d="H", reason=f"1 − {frac(a)} = {frac(t - a)}.")
def y3(r):   # bigger or smaller than 1 decision
    rows = r.sample([("1/2 + 1/3", "Less than 1"), ("2/3 + 3/4", "More than 1"), ("1/4 + 3/4", "Exactly 1"), ("3/5 + 2/5", "Exactly 1"), ("1/2 + 5/8", "More than 1"), ("1/3 + 1/4", "Less than 1")], 4)
    return GD("Without adding exactly: is each total less than 1, exactly 1 or more than 1?", "Total", rows, o="O2", d="H", extra=["Less than 1", "Exactly 1", "More than 1"],
              reason="Compare each fraction with 1/2: two fractions bigger than 1/2 make more than 1; two smaller than 1/2 make less than 1.")


s.std([a7, a8, a1, a2, a3, a4, a5, a6], EX("Explain why 1/2 + 1/4 = 3/4 and not 2/6.", [("change 1/2 to 2/4 (a common denominator)", ["2/4|common|same denominator|quarters"]), ("2/4 + 1/4 = 3/4; you do not add denominators", ["3/4|denominator"])], "The fractions need a common denominator: 1/2 = 2/4. Then 2/4 + 1/4 = 3/4. Adding the denominators would change the size of the pieces.", o="O2"),
      deep=[y1, y2, y3])

# ================================================================== 7.3
s = U.section("7.3", "Multiplying fractions", ["O3"])
s.idea("Fraction × whole number", ["3 × 2/5 = 6/5 = 1 1/5: multiply the numerator by the whole number.",
       "**Fraction of an amount**: 3/4 of 20 = 20 ÷ 4 × 3 = 15."])
s.idea("Fraction × fraction", ["Multiply the numerators and multiply the denominators: 2/3 × 3/5 = 6/15 = 2/5."])
s.check(N("Find 2/5 of 35.", 14, o="O3"))
s.idea("Why 'of' means multiply", ["1/2 of 1/3 is half of a third. Cut a third into 2 equal pieces: each piece is 1/6 of the whole. So 1/2 × 1/3 = 1/6.",
       "Multiplying numerators counts the pieces you keep; multiplying denominators counts how many pieces the whole is cut into."])
s.check(MC("Before you read on: is 2/3 × 3/4 bigger or smaller than 3/4?", "Smaller", [("Bigger", "Taking 2/3 of something gives less than all of it."), ("The same", "Only × 1 keeps the same size.")], o="O3"))
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


def z1(r):   # find all products
    t = pick(r, [Fr(1, 6), Fr(1, 4), Fr(1, 3)])
    pairs = {Fr(1, 6): [("1/2 × 1/3", True), ("1/3 × 1/2", True), ("1/2 + 1/3", False), ("2/3 × 1/4", True), ("1/6 × 1/6", False)],
             Fr(1, 4): [("1/2 × 1/2", True), ("1/2 + 1/2", False), ("2/3 × 3/8", True), ("1/8 × 2", True), ("1/4 × 1/4", False)],
             Fr(1, 3): [("2/3 × 1/2", True), ("1/6 × 2", True), ("1/3 × 1/3", False), ("1/2 × 1/6", False), ("3/4 × 4/9", True)]}[t]
    good = [p for p, ok in pairs if ok][:2]; bad = [p for p, ok in pairs if not ok][:2]
    return MS(f"Select ALL the calculations whose answer is {frac(t)}.", good, bad, o="O3", d="H", reason="Multiply the numerators and the denominators, then simplify.")
def z2(r):   # fraction of amount, work backwards
    d = pick(r, [3, 4, 5, 8]); n = r.randint(1, d - 1); whole = d * r.randint(3, 12)
    return N(f"{n}/{d} of a number is {whole // d * n}. What is the number?", whole, o="O3", d="H", reason=f"1/{d} is {whole // d * n} ÷ {n} = {whole // d}, so the whole is {whole // d} × {d} = {whole}.")
def z3(r):   # spot the error
    return MC("Ali says 2/3 × 6 = 12/18. Is he right?", "No: it is 4", [("Yes", "6 is 6/1, not 6/6: multiply only the numerator by 6."), ("No: it is 2/18", "2 × 6 = 12 on top; the bottom stays 3.")], o="O3", d="H",
              reason="2/3 × 6 = 12/3 = 4.")


s.std([m6, m7, m1, m2, m3, m4, m5, m8], EX("Explain how to find 3/5 of 40.", [("divide by 5 to find one fifth: 8", ["÷ ?5|one fifth|= ?8|\\b8\\b"]), ("multiply by 3: 24", ["× ?3|24"])], "First find 1/5 of 40 by dividing by 5: 8. Then 3/5 is 3 × 8 = 24.", o="O3"),
      deep=[z1, z2, z3])

# ================================================================== 7.4
s = U.section("7.4", "Dividing fractions", ["O4"])
s.idea("Fraction ÷ whole number", ["Dividing by 2 is the same as finding half: 3/4 ÷ 2 = 3/8.",
       "In general, multiply the **denominator** by the whole number: a/b ÷ n = a/(b × n). Simplify if you can: 4/5 ÷ 2 = 4/10 = 2/5."])
s.check(F("Work out 2/3 ÷ 4.", Fr(1, 6), o="O4"))
s.idea("Sharing a fraction", ["1/2 ÷ 3 means share half of a bar between 3 people. Each gets one third of a half, which is 1/6 of the whole bar.",
       "So dividing by 3 is the same as finding 1/3 of the fraction: 1/2 ÷ 3 = 1/2 × 1/3 = 1/6."])
s.check(MC("Before you read on: is 3/4 ÷ 2 bigger or smaller than 3/4?", "Smaller: 3/8", [("Bigger: 3/2", "Sharing between 2 gives each person less."), ("The same", "Dividing by 2 halves it.")], o="O4"))
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


def w1(r):   # two ways decision
    f = rf(r, (3, 4, 5)); k = pick(r, [2, 3, 4])
    return MC(f"Which calculation gives the same answer as {frac(f)} ÷ {k}?", f"{frac(f)} × 1/{k}", [(f"{frac(f)} × {k}", "Multiplying by the number makes it bigger."), (f"{k} ÷ {frac(f)}", "The order matters in division.")], o="O4", d="H",
              reason=f"Dividing by {k} means finding 1/{k} of it.")
def w2(r):   # spot the error
    return MC("Zara says 4/5 ÷ 2 = 4/10 = 2/5, and Omar says 4/5 ÷ 2 = 2/5. Who is right?", "Both are right", [("Only Zara", "Omar halved the numerator, which also works."), ("Only Omar", "4/10 simplifies to 2/5."), ("Neither", "Check 2/5 × 2 = 4/5.")], o="O4", d="H",
              reason="Halving the numerator, or doubling the denominator, both halve the fraction.")
def w3(r):   # context
    f = pick(r, [Fr(3, 4), Fr(2, 3), Fr(1, 2)]); k = pick(r, [3, 4, 6])
    return F(f"{frac(f)} of a pizza is shared equally by {k} friends. What fraction of the whole pizza does each get?", f / k, o="O4", d="H", reason=f"{frac(f)} ÷ {k} = {frac(f / k)}.")


s.std([v4, v6, v1, v2, v3, v5, v7], EX("Explain why 1/2 ÷ 3 = 1/6.", [("sharing a half into 3 equal parts", ["share|3 parts|three parts|split"]), ("each part is one sixth of the whole", ["sixth|6"])], "Dividing a half into 3 equal parts makes 6 parts in the whole, so each part is 1/6.", o="O4"),
      deep=[w1, w2, w3])

# ================================================================== 7.5
s = U.section("7.5", "Making fraction calculations easier", ["O5"])
s.idea("Strategies", ["**Re-order** to make wholes: 1/4 + 2/3 + 3/4 = (1/4 + 3/4) + 2/3 = 1 2/3.",
       "**Simplify first**: 4/8 + 1/2 = 1/2 + 1/2 = 1.", "**Use known facts**: 1/2 = 0.5 = 50%."])
s.check(F("Work out 3/5 + 1/2 + 2/5 mentally.", Fr(3, 2), o="O5"))
s.idea("Why the shortcuts work", ["Adding can be done in any order, so group fractions that make whole numbers: 1/3 + 5/8 + 2/3 = (1/3 + 2/3) + 5/8 = 1 5/8.",
       "Simplify before multiplying: 4/9 × 3/8 – the 3 and the 9 share a factor 3, and the 4 and the 8 share 4. This gives 1/3 × 1/2 = 1/6 with smaller numbers."])
s.check(MC("Before you read on: what is the quickest first step for 3/4 + 2/5 + 1/4?", "3/4 + 1/4 = 1", [("3/4 + 2/5", "Possible, but needs a common denominator of 20."), ("2/5 + 1/4", "Possible, but harder.")], o="O5"))
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


def v1_(r):   # choose pairs
    rows = r.sample([("1/5 + 2/3 + 4/5", "1/5 + 4/5 first"), ("3/8 + 1/2 + 5/8", "3/8 + 5/8 first"), ("2/7 + 1/3 + 5/7", "2/7 + 5/7 first"), ("1/6 + 3/4 + 5/6", "1/6 + 5/6 first")], 3)
    return GD("Which pair should you add first?", "First step", rows, o="O5", d="H", extra=["Add left to right"], reason="Look for two fractions with the same denominator that make 1.")
def v2_(r):   # cancel first
    a, b = pick(r, [(Fr(4, 9), Fr(3, 8)), (Fr(5, 6), Fr(3, 10)), (Fr(2, 3), Fr(9, 14)), (Fr(6, 7), Fr(7, 12))])
    return F(f"Simplify first, then work out {frac(a)} × {frac(b)}.", a * b, o="O5", d="H", reason=f"Cancel common factors across the fractions: answer {frac(a * b)}.")


s.std([e3, e5, e1, e2, e4, e6, e7], EX("Explain the quickest way to work out 1/3 + 5/8 + 2/3.", [("add 1/3 and 2/3 first to make 1", ["1/3 ?\\+ ?2/3|make 1|= ?1|whole"]), ("1 + 5/8 = 1 5/8", ["1 ?5/8|13/8"])], "Re-order: 1/3 + 2/3 = 1, then 1 + 5/8 = 1 5/8. No common denominator is needed.", o="O5"),
      deep=[v1_, v2_])

U.mindmap(("Ordering", "Equivalent fractions • common denominator", "O1", "7.1"), ("Adding mixed numbers", "Wholes, then fractions • common denominator", "O2", "7.2"),
          ("Multiplying", "Fraction of an amount • multiply tops and bottoms", "O3", "7.3"), ("Dividing", "a/b ÷ n = a/(b × n)", "O4", "7.4"),
          ("Easier calculations", "Make wholes • simplify first", "O5", "7.5"))
