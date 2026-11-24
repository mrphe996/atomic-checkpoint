# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 11 Fractions and percentages (11.1 Equivalence, comparing and ordering fractions, 11.2 Percentages).
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(11, "Fractions and Percentages", "Number",
         "Equivalent fractions, comparing and ordering fractions, and percentages as parts of 100.",
         {"O1": {"code": "4Nf.03", "sec": "11.1", "codeNote": "", "t": "Recognise equivalent fractions and compare and order fractions."},
          "O2": {"code": "4Nf.04", "sec": "11.2", "codeNote": "", "t": "Understand percentages as parts of 100 and link 50%, 25% and 10% to fractions."}})
EQ = [(Fr(1, 2), 50), (Fr(1, 4), 25), (Fr(3, 4), 75), (Fr(1, 10), 10), (Fr(3, 10), 30), (Fr(7, 10), 70), (Fr(1, 5), 20), (Fr(2, 5), 40), (Fr(1, 100), 1)]

s = U.section("11.1", "Equivalence, comparing and ordering fractions", ["O1"])
s.idea("Equivalent fractions", ["**Equivalent fractions** show the same amount: 1/2 = 2/4 = 4/8. Multiply (or divide) the numerator and denominator by the same number.",
       "To compare fractions, use the same denominator: 3/4 = 6/8, and 6/8 > 5/8."], fig=PIE(8, range(4)))
s.check(N("Find the missing number: 3/4 = ☐/8", 6, o="O1"))
s.mistake("Same number top and bottom", ["2/3 = 4/6 because both 2 and 3 are doubled."])


def e1(r):
    n, d = pick(r, [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5), (2, 5)]); k = r.randint(2, 4)
    return N(f"Find the missing number: {n}/{d} = ☐/{d * k}", n * k, o="O1")
def e2(r):
    d = pick(r, [4, 6, 8, 10])
    return MC("Which fraction is the same as the shaded part?", "1/2", ["1/4", "1/3", "3/4"], o="O1", fig=PIE(d, range(d // 2)))
def e3(r):
    d = pick(r, [5, 6, 8, 10]); a, b = r.sample(range(1, d), 2)
    return CMP(f"{a}/{d}", f"{b}/{d}", "<" if a < b else ">", o="O1")
def e4(r):
    a, b = pick(r, [(2, 4), (2, 8), (4, 8), (3, 6), (5, 10), (2, 6), (4, 10), (6, 8)])
    return S(f"Write {a}/{b} in its simplest form.", [f"{Fr(a, b).numerator}/{Fr(a, b).denominator}"], o="O1")
def e5(r):
    ps = r.sample([("1/2", "4/8"), ("1/3", "2/6"), ("1/4", "2/8"), ("3/4", "6/8"), ("1/5", "2/10")], 4)
    return MT("Match the equivalent fractions.", ps, o="O1")
def e6(r):
    n, d = pick(r, [(1, 4), (3, 8), (2, 6), (6, 8), (2, 3)])
    return S(f"The circle shows {n}/{d} shaded. Write an equivalent fraction with denominator {d * 2}.", [f"{2 * n}/{2 * d}"], o="O1", fig=PIE(d, range(n)))
def e7(r):
    fs = r.sample([(1, 2), (1, 4), (3, 4), (1, 8), (5, 8)], 3)
    return OD("Put these fractions in order, smallest first.", [f"{a}/{b}" for a, b in sorted(fs, key=lambda x: x[0] / x[1])], o="O1", d="H")
def e8(r):
    a, b = r.sample([Fr(1, 2), Fr(1, 4), Fr(3, 4), Fr(3, 8), Fr(5, 8)], 2)
    return MC(f"Which is bigger, {a.numerator}/{a.denominator} or {b.numerator}/{b.denominator}?", f"{max(a, b).numerator}/{max(a, b).denominator}", [f"{min(a, b).numerator}/{min(a, b).denominator}", "they are equal"], o="O1", d="H")


s.std([e2, e6, e1, e3, e4, e5, e7, e8], EX("Explain why 2/4 is the same as 1/2.", [("divide top and bottom by 2", "÷ ?2|divide|halve"), ("the amount stays the same", "same|equal|equivalent")], "Divide the numerator and denominator by 2: 2 ÷ 2 = 1 and 4 ÷ 2 = 2. The amount is the same, so 2/4 = 1/2.", o="O1"))

s = U.section("11.2", "Percentages", ["O2"])
s.idea("Out of 100", ["**Per cent** (%) means 'out of 100'. On a 100 square, 37 shaded squares is **37%**.",
       "**50% = 1/2**, **25% = 1/4**, **10% = 1/10**. 100% is the whole."], fig={"kind": "waffle", "n": 37})
s.check(N("What percentage is the same as 1/2?", 50, "%", units=["%"], o="O2"))
s.mistake("The whole is 100%", ["If 30% are shaded, 70% are not."])


def p1(r):
    p = r.randint(5, 95)
    return N("What percentage of the 100 square is shaded?", p, "%", units=["%"], o="O2", fig={"kind": "waffle", "n": p})
def p2(r):
    p = r.randint(5, 95)
    return N("What percentage of the 100 square is NOT shaded?", 100 - p, "%", units=["%"], o="O2", fig={"kind": "waffle", "n": p})
def p3(r):
    f, pc = pick(r, EQ)
    return N(f"Write {f.numerator}/{f.denominator} as a percentage.", pc, "%", units=["%"], o="O2")
def p4(r):
    fs = r.sample(EQ, 3)
    return TB("Complete the table.", ["Fraction", "Percentage"], [[f"{f.numerator}/{f.denominator}", B(pc)] for f, pc in fs], o="O2")
def p5(r):
    p = r.randint(10, 90)
    return N(f"{p}% of the children in a school walk to school. What percentage do not walk?", 100 - p, "%", units=["%"], o="O2")
def p6(r):
    p, k = pick(r, [(50, 2), (25, 4), (10, 10)]); n = k * r.randint(2, 20)
    return N(f"Find {p}% of {n}.", n // k, o="O2", d="H")
def p7(r):
    ps = r.sample(EQ, 4)
    return MT("Match each fraction to its percentage.", [(f"{f.numerator}/{f.denominator}", f"{pc}%") for f, pc in ps], o="O2")
def p8(r):
    a, b = r.sample(range(5, 95), 2)
    return CMP(f"{a}%", f"{b}%", "<" if a < b else ">", o="O2")


s.std([p1, p4, p2, p3, p5, p7, p6, p8], EX("Explain why 25% is the same as one quarter.", [("25% means 25 out of 100", "25 out of 100|25/100"), ("100 ÷ 4 = 25, so it is a quarter", "quarter|÷ ?4|1/4")], "25% means 25 out of 100. 100 split into 4 equal parts gives 25 in each part, so 25% is one quarter.", o="O2"))

U.mindmap(("Equivalent fractions", "Same amount • × or ÷ top and bottom", "O1", "11.1"), ("Percentages", "Out of 100 • 50% = 1/2 • 25% = 1/4", "O2", "11.2"))
