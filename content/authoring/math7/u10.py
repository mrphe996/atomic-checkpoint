# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 10 Percentages (10.1 Fractions, decimals and percentages, 10.2 Percentages large and small).
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(10, "Percentages", "Number",
         "Converting between fractions, decimals and percentages, finding percentages of amounts, and percentages greater than 100% and less than 1%.",
         {"O1": {"code": "7Nf.11", "sec": "10.1", "codeNote": "", "t": "Recognise and convert between fractions, decimals and percentages, and compare them."},
          "O2": {"code": "7Nf.12", "sec": "10.2", "codeNote": "", "t": "Find percentages of amounts, including percentages greater than 100% and less than 1%."}})
EQ = [(Fr(1, 2), 0.5, 50), (Fr(1, 4), 0.25, 25), (Fr(3, 4), 0.75, 75), (Fr(1, 5), 0.2, 20), (Fr(2, 5), 0.4, 40), (Fr(3, 5), 0.6, 60), (Fr(4, 5), 0.8, 80),
      (Fr(1, 10), 0.1, 10), (Fr(3, 10), 0.3, 30), (Fr(7, 10), 0.7, 70), (Fr(9, 10), 0.9, 90), (Fr(1, 20), 0.05, 5), (Fr(3, 20), 0.15, 15), (Fr(1, 25), 0.04, 4), (Fr(1, 8), 0.125, 12.5)]

# ================================================================== 10.1
s = U.section("10.1", "Fractions, decimals and percentages", ["O1"])
s.idea("Per cent means out of 100", ["**Per cent** means 'out of 100': 37% = 37/100 = 0.37.",
       "To change a percentage to a decimal, divide by 100. To change a decimal to a percentage, multiply by 100. To change a fraction, make the denominator 100 or divide."],
       table={"head": ["Fraction", "Decimal", "Percentage"], "rows": [["1/2", "0.5", "50%"], ["1/4", "0.25", "25%"], ["1/5", "0.2", "20%"], ["1/10", "0.1", "10%"]]})
s.check(N("Write 3/5 as a percentage.", 60, "%", units=["%"], o="O1"))
s.mistake("0.5 is not 5%", ["0.5 = 50%. Multiply by 100: 0.5 × 100 = 50."])


def f1(r):
    f, d, p = pick(r, EQ)
    return N(f"Write {frac(f)} as a percentage.", p, "%", units=["%"], o="O1")
def f2(r):
    p = r.randint(1, 99)
    return N(f"Write {p}% as a decimal.", p / 100, o="O1")
def f3(r):
    d = r.randint(1, 99) / 100
    return N(f"Write {fmt(d)} as a percentage.", round(d * 100), "%", units=["%"], o="O1")
def f4(r):
    f, d, p = pick(r, EQ)
    return S(f"Write {fmt(p)}% as a fraction in its simplest form.", [frac(f)], o="O1")
def f5(r):
    rows = r.sample(EQ, 4)
    return TB("Complete the table.", ["Fraction", "Decimal", "Percentage"], [[frac(f), B(d), B(p)] for f, d, p in rows[:2]], o="O1")
def f6(r):
    rows = r.sample(EQ, 4)
    return GD("Match each fraction to its percentage.", "Percentage", [(frac(f), f"{fmt(p)}%") for f, d, p in rows], o="O1", extra=["33%"])
def f7(r):
    a, b = r.sample(EQ, 2)
    if a[2] == b[2]: return None
    return MC(f"Which is bigger: {frac(a[0])} or {fmt(b[1])}?", frac(a[0]) if a[2] > b[2] else fmt(b[1]), [fmt(b[1]) if a[2] > b[2] else frac(a[0]), "they are equal"], o="O1", reason=f"{frac(a[0])} = {fmt(a[2])}% and {fmt(b[1])} = {fmt(b[2])}%.")
def f8(r):
    vs = r.sample(EQ, 3)
    items = sorted([(p, x) for (f, d, p), x in zip(vs, [frac(vs[0][0]), fmt(vs[1][1]), f"{fmt(vs[2][2])}%"])])
    if len({p for p, _ in items}) < 3: return None
    return OD("Put these in order, smallest first.", [x for _, x in items], o="O1", d="H")
def f9(r):
    n, k = r.randint(10, 40), None; k = r.randint(1, n - 1)
    return N(f"{k} out of {n} students wear glasses. What percentage is that? Give your answer to 1 d.p.", round(k / n * 100, 1), "%", units=["%"], o="O1", d="H", tol=0.05)


s.std([f5, f6, f1, f2, f3, f4, f7, f8, f9], EX("Explain why 0.4 = 40%.", [("per cent means out of 100", ["out of 100|hundred"]), ("0.4 = 40/100 (multiply by 100)", ["40/100|× ?100|multiply by 100"])], "Per cent means out of 100. 0.4 = 4 tenths = 40 hundredths = 40/100, which is 40%.", o="O1"))

# ================================================================== 10.2
s = U.section("10.2", "Percentages large and small", ["O2"])
s.idea("Percentages of amounts", ["Use 10% (÷ 10) and 1% (÷ 100) to build other percentages: 35% of 80 = 30% + 5% = 24 + 4 = 28.",
       "Or use a decimal: 35% of 80 = 0.35 × 80 = 28."])
s.idea("Over 100% and under 1%", ["**150%** of an amount is more than the whole amount: 150% of 40 = 60.", "**0.5%** is half of 1%: 0.5% of 200 = 1."])
s.check(N("Find 15% of 60.", 9, o="O2"))
s.mistake("Bigger than the whole", ["A percentage over 100% gives an answer bigger than the starting amount."])


def p1(r):
    p = pick(r, [10, 20, 25, 30, 40, 50, 75, 5, 15, 35, 60]); a = r.randint(2, 40) * 20
    return N(f"Find {p}% of {a}.", p * a / 100, o="O2")
def p2(r):
    p = pick(r, [110, 120, 125, 150, 200, 250]); a = r.randint(2, 30) * 4
    return N(f"Find {p}% of {a}.", p * a / 100, o="O2", d="H")
def p3(r):
    p = pick(r, [0.5, 0.1, 0.2, 0.25]); a = r.randint(1, 20) * 400
    return N(f"Find {fmt(p)}% of {a}.", p * a / 100, o="O2", d="H")
def p4(r):
    p = pick(r, [10, 15, 20, 25]); c = r.randint(4, 40) * 4
    return N(f"A jacket costs ${c}. There is {p}% off. How much is taken off the price?", p * c / 100, "$", units=["$"], o="O2")
def p5(r):
    a = r.randint(2, 20) * 10
    return TB(f"Find percentages of {a}.", ["Percentage", "Value"], [["10%", B(a / 10)], ["5%", B(a / 20)], ["15%", B(a * 0.15)], ["1%", B(a / 100)]], o="O2")
def p6(r):
    a = r.randint(10, 60) * 10; p = pick(r, [10, 20, 25, 50])
    return N(f"A plant was {a} mm tall. It grew to {100 + p}% of its height. How tall is it now?", a * (100 + p) / 100, "mm", units=["mm"], o="O2", d="H")
def p7(r):
    rows = [("10% of 80", "8"), ("50% of 30", "15"), ("25% of 40", "10"), ("1% of 600", "6"), ("200% of 7", "14"), ("75% of 20", "15")]
    return GD("Find each value.", "Answer", r.sample(rows, 4), o="O2", extra=["12", "4"])
def p8(r):
    n = r.randint(20, 60) * 10; p = pick(r, [10, 20, 30, 40, 60])
    return N(f"A school has {n} students. {p}% of them have a pet. How many students have a pet?", n * p // 100, "students", units=["students"], o="O2", data={"head": ["", "Students", "With a pet"], "rows": [["School", str(n), f"{p}%"]]})
def p9(r):
    return MC("Which is the same as 150% of a number?", "1.5 times the number", ["half the number", "the number plus 150", "15 times the number"], o="O2")


s.std([p5, p7, p1, p2, p3, p4, p6, p8, p9], EX("Explain how to find 35% of 60 using 10% and 5%.", [("10% is 6 and 5% is 3", ["10% ?(of 60)? ?(is|=) ?6|\\b6\\b.*\\b3\\b|5% ?(is|=) ?3"]), ("35% = 30% + 5% = 18 + 3 = 21", ["21"])], "10% of 60 is 6, so 30% is 18 and 5% is 3. 35% = 30% + 5% = 18 + 3 = 21.", o="O2"))

U.mindmap(("FDP", "Per cent = out of 100 • ÷ 100 and × 100", "O1", "10.1"), ("Percentages of amounts", "Build from 10% and 1% • over 100% is more than the whole", "O2", "10.2"))
