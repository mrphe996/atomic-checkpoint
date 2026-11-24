# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 9 Addition and subtraction of fractions (9.1 Adding fractions, 9.2 Subtracting fractions).
Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(9, "Addition and Subtraction (2)", "Number",
         "Adding and subtracting fractions with the same denominator and with denominators that are multiples of each other.",
         {"O1": {"code": "5Nf.04", "sec": "9.1", "codeNote": "", "t": "Add fractions with the same denominator, or where one denominator is a multiple of the other."},
          "O2": {"code": "5Nf.05", "sec": "9.2", "codeNote": "", "t": "Subtract fractions with the same denominator, or where one denominator is a multiple of the other."}})
PAIRS = [(2, 4), (2, 6), (3, 6), (4, 8), (2, 8), (5, 10), (2, 10), (3, 9), (4, 12), (3, 12)]

s = U.section("9.1", "Adding fractions", ["O1"])
s.idea("Same denominator", ["When the denominators are the **same**, add the numerators: 2/7 + 3/7 = **5/7**. The size of the parts does not change.",
       "If one denominator is a multiple of the other, change one fraction first: 1/2 + 1/4 = 2/4 + 1/4 = **3/4**."], fig=PIE(7, range(5)))
s.check(F("Work out 3/8 + 4/8.", Fr(7, 8), o="O1"))
s.mistake("Don't add the denominators", ["2/7 + 3/7 is 5/7, not 5/14."])


def a1(r):
    d = pick(r, [5, 6, 7, 8, 9, 10, 12]); a, b = r.randint(1, d - 2), r.randint(1, d - 2)
    if a + b >= d: return None
    return F(f"Work out {a}/{d} + {b}/{d}.", Fr(a + b, d), o="O1")
def a2(r):
    a, b = pick(r, PAIRS); x, y = r.randint(1, a - 1), r.randint(1, b - 1)
    return F(f"Work out {x}/{a} + {y}/{b}.", Fr(x, a) + Fr(y, b), o="O1")
def a3(r):
    d = pick(r, [4, 5, 6, 8]); a, b = r.randint(1, d - 2), r.randint(1, d - 2)
    if a + b >= d: return None
    return F(f"The circle shows {a}/{d} and {b}/{d} shaded. What fraction is shaded altogether?", Fr(a + b, d), o="O1", fig=PIE(d, range(a + b)))
def a4(r):
    d = pick(r, [5, 6, 8, 10]); a, b = r.randint(2, d - 1), r.randint(2, d - 1)
    if a + b <= d: return None
    return F(f"Work out {a}/{d} + {b}/{d}. The answer is more than 1.", Fr(a + b, d), o="O1", d="H")
def a5(r):
    a, b = pick(r, PAIRS); x = r.randint(1, a - 1)
    return TB(f"Change {x}/{a} into {b}ths.", ["Fraction", f"In {b}ths"], [[f"{x}/{a}", B(x * b // a)]], o="O1")
def a6(r):
    d = pick(r, [4, 5, 8, 10]); a, b = r.randint(1, d - 2), r.randint(1, d - 2)
    if a + b >= d: return None
    return F(f"Amy ate {a}/{d} of a pizza and Ben ate {b}/{d}. How much did they eat altogether?", Fr(a + b, d), o="O1")
def a7(r):
    d = pick(r, [6, 8, 10, 12]); a, b, c = r.randint(1, 3), r.randint(1, 3), r.randint(1, 3)
    if a + b + c >= d: return None
    return F(f"Work out {a}/{d} + {b}/{d} + {c}/{d}.", Fr(a + b + c, d), o="O1", d="H")
def a8(r):
    d = pick(r, [5, 7, 8, 9]); a = r.randint(1, d - 1)
    return N(f"Find the missing number: {a}/{d} + ☐/{d} = 1", d - a, o="O1")


s.std([a3, a5, a1, a2, a6, a8, a4, a7], EX("Explain why 2/5 + 1/5 = 3/5 and not 3/10.", [("the parts are all fifths", "fifths|same size|same denominator"), ("add the numerators: 2 + 1 = 3", "numerator|2 ?\\+ ?1|top")], "Both fractions are in fifths, so the parts are the same size. Add the number of parts: 2 + 1 = 3 fifths. The denominator stays 5.", o="O1"))

s = U.section("9.2", "Subtracting fractions", ["O2"])
s.idea("Taking away parts", ["With the same denominator, subtract the numerators: 7/9 − 4/9 = **3/9 = 1/3**.",
       "1 whole is d/d, so 1 − 3/8 = 8/8 − 3/8 = **5/8**."], fig=PIE(9, range(3)))
s.check(F("Work out 5/6 − 1/6.", Fr(4, 6), o="O2"))
s.mistake("Change first", ["3/4 − 1/2: change 1/2 into 2/4 first, then 3/4 − 2/4 = 1/4."])


def b1(r):
    d = pick(r, [5, 6, 7, 8, 9, 10]); a, b = sorted(r.sample(range(1, d), 2), reverse=True)
    return F(f"Work out {a}/{d} − {b}/{d}.", Fr(a - b, d), o="O2")
def b2(r):
    a, b = pick(r, PAIRS); y = r.randint(1, b - 1); x = r.randint(1, a - 1)
    if Fr(y, b) <= Fr(x, a): return None
    return F(f"Work out {y}/{b} − {x}/{a}.", Fr(y, b) - Fr(x, a), o="O2")
def b3(r):
    d = pick(r, [3, 4, 5, 8, 10]); a = r.randint(1, d - 1)
    return F(f"Work out 1 − {a}/{d}.", 1 - Fr(a, d), o="O2")
def b4(r):
    d = pick(r, [6, 8]); n = r.randint(3, d - 1); k = r.randint(1, n - 1)
    return F(f"{n}/{d} of the circle is shaded. {k}/{d} is rubbed out. What fraction is still shaded?", Fr(n - k, d), o="O2", fig=PIE(d, range(n)))
def b5(r):
    d = pick(r, [4, 5, 8, 10]); a = r.randint(2, d - 1); b = r.randint(1, a - 1)
    return F(f"A jug was {a}/{d} full. {b}/{d} of a jug was poured out. How full is it now?", Fr(a - b, d), o="O2")
def b6(r):
    d = pick(r, [5, 6, 8]); a, b = r.randint(1, d - 1), r.randint(1, d - 1)
    if a == b: return None
    return TB("Complete the table.", ["Calculation", "Numerator"], [[f"{max(a, b)}/{d} − {min(a, b)}/{d}", B(abs(a - b))], [f"1 − {a}/{d}", B(d - a)]], o="O2")
def b7(r):
    d = pick(r, [6, 8, 10, 12]); a, b, c = r.randint(1, 3), r.randint(1, 3), d
    return F(f"A cake is cut into {d} equal pieces. Sam eats {a} pieces and Lia eats {b}. What fraction of the cake is left?", Fr(d - a - b, d), o="O2", d="H")
def b8(r):
    a, b = pick(r, PAIRS); x = r.randint(1, a - 1)
    return F(f"Work out 1 − {x}/{a} − 1/{b}.", 1 - Fr(x, a) - Fr(1, b), o="O2", d="H") if 1 - Fr(x, a) - Fr(1, b) > 0 else None


s.std([b4, b6, b1, b2, b3, b5, b7, b8], EX("Explain how to work out 1 − 2/7.", [("1 whole is 7/7", "7/7|seven sevenths"), ("7/7 − 2/7 = 5/7", "5/7")], "One whole is 7/7. Taking away 2/7 leaves 7/7 − 2/7 = 5/7.", o="O2"))

U.mindmap(("Adding", "Same denominator: add the numerators", "O1", "9.1"), ("Subtracting", "1 = d/d • change to the same denominator", "O2", "9.2"))
