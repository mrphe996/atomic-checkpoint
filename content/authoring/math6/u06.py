# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 6 Fractions and percentages (6.1 Understanding fractions, 6.2 Percentages,
6.3 Equivalence and comparison). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(6, "Fractions and Percentages", "Number",
         "Fractions as division, finding fractions of amounts, percentages of shapes and amounts, and comparing fractions, decimals and percentages.",
         {"O1": {"code": "6Nf.01", "sec": "6.1", "codeNote": "", "t": "Understand that a fraction can be a division (3/4 = 3 ÷ 4), and find fractions of quantities."},
          "O2": {"code": "6Nf.02", "sec": "6.2", "codeNote": "", "t": "Understand percentages as parts of 100 and find simple percentages of quantities."},
          "O3": {"code": "6Nf.03", "sec": "6.3", "codeNote": "", "t": "Recognise equivalent fractions, decimals and percentages, and compare and order them."}})
TOL = 1e-6
DEN = [2, 3, 4, 5, 6, 8, 10, 12]


def F(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction in its simplest form or a mixed number.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}" + (f" = {frac(v, True)}" if v > 1 and v.denominator > 1 else "")), **kw)


def PIE(n, d):  # a circle cut into d equal parts, n shaded
    return {"kind": "pie", "labels": [""] * d, "values": [1] * d, "shade": n}


# ================================================================== 6.1
s = U.section("6.1", "Understanding fractions", ["O1"])
s.idea("Fractions as division", ["3/4 means **3 ÷ 4**. If 3 pizzas are shared equally between 4 people, each person gets 3/4 of a pizza.",
       "The **denominator** (bottom) shows how many equal parts; the **numerator** (top) shows how many parts we have."], fig={"kind": "pie", "labels": ["", "", "", ""], "values": [1, 1, 1, 1], "shade": [0, 1, 2]})
s.check(F("5 cakes are shared equally between 8 children. How much cake does each child get?", Fr(5, 8), o="O1"))
s.idea("Fraction of an amount", ["To find 3/5 of 40: divide by the denominator, then multiply by the numerator. 40 ÷ 5 = 8, then 8 × 3 = **24**."])
s.check(MC("Before you read on: which is bigger, 2/3 or 3/5?", "2/3", [("3/5", "2/3 = 10/15 and 3/5 = 9/15."), ("They are equal", "Use a common denominator of 15.")], o="O1"))
s.mistake("Divide first", ["To find 2/3 of 12, do 12 ÷ 3 = 4 then × 2 = 8. Do not divide by 2."])


def f1(r):
    d = pick(r, DEN); n = r.randint(1, d - 1); k = r.randint(2, 12)
    return N(f"Find {frac(Fr(n, d)) if Fr(n, d).denominator == d else f'{n}/{d}'} of {d * k}.", n * k, o="O1")
def f2(r):
    a, b = r.randint(2, 9), r.randint(3, 10)
    if a >= b: return None
    return F(f"{a} pizzas are shared equally between {b} people. How much pizza does each person get?", Fr(a, b), o="O1")
def f3(r):
    a, b = r.randint(7, 25), r.randint(2, 6)
    if a % b == 0: return None
    return S(f"Write {a} ÷ {b} as a mixed number.", [frac(Fr(a, b), True)], o="O1")
def f4(r):
    d = pick(r, [3, 4, 5, 6, 8]); n = r.randint(1, d - 1)
    return F("What fraction of the circle is shaded?", Fr(n, d), o="O1", fig={"kind": "pie", "labels": [""] * d, "values": [1] * d, "shade": list(range(n))})
def f5(r):
    d = pick(r, [3, 4, 5, 8, 10]); n = r.randint(1, d - 1); k = r.randint(3, 15)
    return TB(f"Complete the table.", ["Amount", f"1/{d}", f"{n}/{d}"], [[str(d * k), B(k), B(n * k)]], o="O1")
def f6(r):
    d = pick(r, [4, 5, 8, 10]); n = r.randint(1, d - 1); k = r.randint(5, 20)
    return N(f"A shop has {d * k} T-shirts. {n}/{d} of them are blue. How many are NOT blue?", (d - n) * k, "T-shirts", units=["T-shirts"], o="O1", d="H")
def f7(r):
    d = pick(r, [3, 4, 5]); n = r.randint(1, d - 1); k = r.randint(2, 10)
    return N(f"{n}/{d} of a number is {n * k}. What is the number?", d * k, o="O1", d="H")
def f8(r):
    w, n, d = r.randint(1, 4), r.randint(1, 3), 4
    if n >= d: return None
    return S(f"Write {w} {n}/{d} as an improper fraction.", [f"{w * d + n}/{d}"], o="O1")


def f1_1(r):
    a = pick(r, [Fr(1, 2), Fr(2, 3), Fr(3, 4), Fr(2, 5)]); ks = r.sample(range(2, 6), 2)
    good = [f"{a.numerator * k}/{a.denominator * k}" for k in ks]; bad = [f"{a.numerator + k}/{a.denominator + k}" for k in r.sample(range(1, 4), 2)]
    return MS(f"Select ALL the fractions equal to {frac(a)}.", good, bad, o="O1", d="H", reason="Multiply the top and the bottom by the same number.")


s.std([f4, f5, f1, f2, f3, f6, f8, f7], EX("Explain how to find 3/4 of 20.", [("divide 20 by 4 to get 5", "20 ?÷ ?4|divide by 4|\\b5\\b"), ("multiply 5 by 3 to get 15", "× ?3|times 3|15")], "First find 1/4 of 20 by dividing by 4: 20 ÷ 4 = 5. Then 3/4 is three of those: 5 × 3 = 15.", o="O1"),
      deep=[f1_1])

# ================================================================== 6.2
s = U.section("6.2", "Percentages", ["O2"])
s.idea("Per cent", ["**Per cent** means 'out of 100'. 37% means 37 out of 100. On a **100 square**, 37% is 37 of the small squares.",
       "50% = half, 25% = a quarter, 10% = a tenth, 1% = a hundredth."], table={"head": ["Percentage", "50%", "25%", "10%", "1%"], "rows": [["Fraction", "1/2", "1/4", "1/10", "1/100"]]})
s.check(N("What is 10% of 70?", 7, o="O2"))
s.idea("Percentages of amounts", ["Use 10% to build others: 10% of 60 = 6, so 30% = 18 and 5% = 3."])
s.check(MC("Before you read on: what is 25% of 80?", "20", [("25", "25% is a quarter, not 25."), ("40", "That is 50%.")], o="O2"))
s.mistake("The whole is 100%", ["If 35% of a class are boys, 65% are girls (35 + 65 = 100)."])


def c1(r):
    p, a = pick(r, [10, 20, 25, 50, 30, 40, 75]), r.randint(2, 20) * 20
    return N(f"Find {p}% of {a}.", p * a / 100, o="O2")
def c2(r):
    p = r.randint(11, 89)
    return N(f"{p}% of a 100 square is shaded. What percentage is not shaded?", 100 - p, "%", units=["%"], o="O2", fig={"kind": "waffle", "n": p})
def c3(r):
    lab = ["Walk", "Bus", "Car", "Bike"]; v = pick(r, [[50, 25, 15, 10], [40, 30, 20, 10], [45, 25, 20, 10], [35, 35, 20, 10]]); k = r.randrange(4)
    return N(f"The pie chart shows how children travel to school. What percentage travel by {lab[k].lower()}?", v[k], "%", units=["%"], o="O2", fig={"kind": "pie", "labels": [f"{l} {x}%" if i != k else l for i, (l, x) in enumerate(zip(lab, v))], "values": v})
def c4(r):
    p = pick(r, [10, 20, 25, 50, 75]); a = r.randint(2, 10) * 20
    return TB(f"Complete the table for {a} g.", ["Percentage", "Amount (g)"], [["10%", B(a / 10)], [f"{p}%", B(p * a / 100)]], o="O2")
def c5(r):
    p = pick(r, [10, 20, 25, 50]); pr = r.randint(2, 20) * 20
    return N(f"A jacket costs ${pr}. It has {p}% off. How much is taken off the price?", p * pr / 100, "$", units=["$", "dollars"], o="O2")
def c6(r):
    p = pick(r, [10, 20, 25, 50]); pr = r.randint(2, 20) * 20
    return N(f"A game costs ${pr}. In a sale there is {p}% off. What is the sale price?", pr - p * pr / 100, "$", units=["$", "dollars"], o="O2", d="H")
def c7(r):
    p = r.randint(5, 45) * 2
    return MC(f"{p}% of children in a school are girls. Which is true?", f"{100 - p}% are boys", [f"{p}% are boys", f"{100 - p // 2}% are boys", f"{p // 2}% are boys"], o="O2")
def c8(r):
    p = pick(r, [5, 15, 35, 45]); a = r.randint(2, 10) * 20
    return N(f"Find {p}% of {a}.", p * a / 100, o="O2", d="H", reason="Use 10% and 5%.")


def f2_1(r):
    n = pick(r, [40, 60, 80, 120, 200])
    return MC(f"Which is bigger: 30% of {n} or 1/4 of {n}?", f"30% of {n}", [(f"1/4 of {n}", f"1/4 = 25%, which is less than 30%."), ("They are equal", f"30% of {n} = {n * 3 // 10}; 1/4 of {n} = {n // 4}.")], o="O2", d="H", reason=f"30% of {n} = {n * 3 // 10} and 1/4 of {n} = {n // 4}.")


s.std([c3, c4, c1, c2, c5, c7, c6, c8], EX("Explain how to find 20% of 45.", [("10% of 45 is 4.5", "4\\.5|10%"), ("20% is double: 9", "double|× ?2|\\b9\\b")], "10% of 45 is 45 ÷ 10 = 4.5. 20% is double that: 4.5 × 2 = 9.", o="O2"),
      deep=[f2_1])

# ================================================================== 6.3
s = U.section("6.3", "Equivalence and comparison", ["O3"])
s.idea("Same value, different forms", ["1/2 = 0.5 = 50%. 1/4 = 0.25 = 25%. 3/10 = 0.3 = 30%.",
       "**Equivalent fractions** have the same value: multiply or divide the top and bottom by the same number. 2/3 = 4/6 = 8/12."],
       table={"head": ["Fraction", "1/2", "1/4", "3/4", "1/5", "1/10"], "rows": [["Decimal", "0.5", "0.25", "0.75", "0.2", "0.1"], ["Percentage", "50%", "25%", "75%", "20%", "10%"]]})
s.check(N("Find the missing number: 3/4 = ☐/12", 9, o="O3"))
s.idea("Comparing", ["To compare fractions, change them to the same denominator or to decimals: 3/5 = 0.6 and 2/3 ≈ 0.67, so 3/5 < 2/3."])
s.check(MC("Before you read on: which is biggest: 0.4, 3/8 or 45%?", "45%", [("0.4", "0.4 = 40%."), ("3/8", "3/8 = 37.5%.")], o="O3"))
s.mistake("Bigger denominator, smaller parts", ["1/8 is smaller than 1/5: the more parts the whole is cut into, the smaller each part is."])
EQ = [(Fr(1, 2), "0.5", 50), (Fr(1, 4), "0.25", 25), (Fr(3, 4), "0.75", 75), (Fr(1, 5), "0.2", 20), (Fr(2, 5), "0.4", 40), (Fr(3, 5), "0.6", 60), (Fr(4, 5), "0.8", 80),
      (Fr(1, 10), "0.1", 10), (Fr(3, 10), "0.3", 30), (Fr(7, 10), "0.7", 70), (Fr(9, 10), "0.9", 90), (Fr(1, 20), "0.05", 5), (Fr(1, 100), "0.01", 1)]


def e1(r):
    f = rnd = pick(r, EQ)
    return N(f"Write {frac(f[0])} as a percentage.", f[2], "%", units=["%"], o="O3")
def e2(r):
    f = pick(r, EQ)
    return N(f"Write {f[2]}% as a decimal.", float(f[1]), o="O3")
def e3(r):
    n, d = r.randint(1, 5), pick(r, [3, 4, 5, 6, 7]); k = r.randint(2, 6)
    if n >= d: return None
    return N(f"Find the missing number: {n}/{d} = ☐/{d * k}", n * k, o="O3")
def e4(r):
    fs = r.sample(EQ, 3)
    return TB("Complete the table.", ["Fraction", "Decimal", "Percentage"], [[frac(f[0]), B(float(f[1])), B(f[2])] for f in fs], o="O3")
def e5(r):
    a, b = r.sample(EQ, 2)
    if a[2] == b[2]: return None
    return CMP(frac(a[0]), f"{b[2]}%", "<" if a[2] < b[2] else ">", o="O3")
def e6(r):
    fs = r.sample(EQ[:11], 3); forms = [frac(fs[0][0]), fs[1][1], f"{fs[2][2]}%"]
    order = [x for _, x in sorted(zip([f[2] for f in fs], forms))]
    if len({f[2] for f in fs}) < 3: return None
    return OD("Put these in order, smallest first.", order, o="O3", d="H")
def e7(r):
    n, d = r.randint(2, 8), pick(r, [4, 6, 8, 10, 12])
    f = Fr(n, d)
    if f.denominator == d or n >= d: return None
    return S(f"Write {n}/{d} in its simplest form.", [frac(f)], o="O3")
def e8(r):
    a, b = r.sample([Fr(1, 3), Fr(2, 5), Fr(3, 8), Fr(5, 12), Fr(4, 9), Fr(3, 7)], 2)
    return MC(f"Which is bigger, {frac(a)} or {frac(b)}?", frac(max(a, b)), [frac(min(a, b)), "They are equal"], o="O3", d="H")

def e9(r):
    f = pick(r, EQ[:11])
    return S("What fraction of the 100 square is shaded? Give it in its simplest form.", [frac(f[0])], o="O3", fig={"kind": "waffle", "n": f[2]})


def f3_1(r):
    vals = r.sample([("1/2", 50), ("0.45", 45), ("3/5", 60), ("55%", 55), ("0.3", 30), ("1/4", 25)], 4); vals.sort(key=lambda v: v[1])
    return OD("Put these in order, smallest first.", [v[0] for v in vals], o="O3", d="H", reason="Change them all to percentages: " + ", ".join(f"{v[0]} = {v[1]}%" for v in vals) + ".")


s.std([e4, e9, e5, e1, e2, e3, e7, e8, e6], EX("Explain why 2/5 is the same as 40%.", [("2/5 = 4/10 = 40/100", "40/100|4/10|× ?20"), ("40 out of 100 is 40%", "out of 100|per cent|hundred")], "Multiply the top and bottom by 20: 2/5 = 40/100. 40 out of 100 is 40%.", o="O3"),
      deep=[f3_1])

U.mindmap(("Fractions", "a/b = a ÷ b • fraction of an amount", "O1", "6.1"), ("Percentages", "Out of 100 • 10% builds others", "O2", "6.2"), ("Equivalence", "1/2 = 0.5 = 50% • compare and order", "O3", "6.3"))
