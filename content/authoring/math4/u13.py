# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 13 Addition and subtraction (13.1 Adding and subtracting efficiently,
13.2 Adding and subtracting fractions with the same denominator). Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *
from h import *

U = Unit(13, "Addition and Subtraction", "Number",
         "Mental strategies for adding and subtracting, such as rounding and adjusting, and adding and subtracting fractions with the same denominator.",
         {"O1": {"code": "4Nc.06", "sec": "13.1", "codeNote": "", "t": "Choose efficient mental and written strategies to add and subtract."},
          "O2": {"code": "4Nf.05", "sec": "13.2", "codeNote": "", "t": "Add and subtract fractions with the same denominator."}})

s = U.section("13.1", "Adding and subtracting efficiently", ["O1"])
s.idea("Round and adjust", ["To add 99, add 100 then take away 1: 245 + 99 = 345 − 1 = **344**.",
       "To subtract 49, subtract 50 then add 1: 186 − 49 = 136 + 1 = **137**. Use **number bonds**: 63 + 37 = 100."], fig=NL(0, 10))
s.check(N("Work out 356 + 199.", 555, o="O1"))
s.mistake("Adjust the right way", ["When you subtract 50 instead of 49, you took 1 too many: add it back."])


def a1(r):
    a, k = r.randint(100, 800), pick(r, [9, 19, 29, 99, 199])
    return N(f"Work out {a} + {k}.", a + k, o="O1", reason=f"Add {k + 1}, then take away 1.")
def a2(r):
    a, k = r.randint(200, 900), pick(r, [9, 19, 49, 99, 199])
    return N(f"Work out {a} − {k}.", a - k, o="O1", reason=f"Take away {k + 1}, then add 1.")
def a3(r):
    a = r.randint(11, 89)
    return N(f"What do you add to {a} to make 100?", 100 - a, o="O1")
def a4(r):
    a, k = r.randint(100, 800), pick(r, [99, 199, 299])
    return TB(f"Work out {a} + {k} by rounding and adjusting.", ["Step", "Answer"], [[f"{a} + {k + 1}", B(a + k + 1)], ["then − 1", B(a + k)]], o="O1")
def a5(r):
    a, b, c = r.randint(11, 89), r.randint(11, 89), r.randint(11, 89)
    if (a + c) % 10: c = 100 - a if 0 < 100 - a < 100 else c
    return N(f"Work out {a} + {b} + {c}. Look for numbers that make 100.", a + b + c, o="O1")
def a6(r):
    lab = ["Mon", "Tue", "Wed"]; v = [r.randint(100, 500) for _ in lab]
    return N("The table shows money raised at a fair, in dollars. How much in total?", sum(v), "$", units=["$", "dollars"], o="O1", data={"head": ["Day", *lab], "rows": [["$", *map(str, v)]]})
def a7(r):
    a, b = r.randint(1000, 5000), r.randint(100, 999)
    return N(f"Work out {a} + {b}.", a + b, o="O1", d="H")
def a8(r):
    a, b = r.randint(2000, 9000), r.randint(100, 999)
    return N(f"Work out {a} − {b}.", a - b, o="O1", d="H")


s.std([a4, a6, a1, a2, a3, a5, a7, a8], EX("Explain an easy way to work out 438 − 99.", [("subtract 100 instead", "100"), ("then add 1 back: 338 + 1 = 339", "339|add 1|\\+ ?1")], "Take away 100 instead of 99: 438 − 100 = 338. You took away 1 too many, so add it back: 339.", o="O1"))

s = U.section("13.2", "Adding and subtracting fractions with the same denominator", ["O2"])
s.idea("Same-sized parts", ["When the denominators are the same, add or subtract the **numerators**: 3/7 + 2/7 = **5/7** and 6/8 − 1/8 = **5/8**.",
       "The denominator stays the same because the parts are the same size. One whole is 7/7, 8/8 and so on."], fig=PIE(7, range(5)))
s.check(S("Work out 2/5 + 2/5.", ["4/5"], o="O2"))
s.mistake("Keep the denominator", ["3/7 + 2/7 is 5/7, not 5/14."])


def f1(r):
    d = pick(r, [5, 6, 7, 8, 9, 10, 12]); a, b = r.randint(1, d - 2), r.randint(1, d - 2)
    if a + b >= d: return None
    return S(f"Work out {a}/{d} + {b}/{d}.", [f"{a + b}/{d}"], o="O2")
def f2(r):
    d = pick(r, [5, 6, 7, 8, 9, 10]); a, b = sorted(r.sample(range(1, d), 2), reverse=True)
    return S(f"Work out {a}/{d} − {b}/{d}.", [f"{a - b}/{d}"], o="O2")
def f3(r):
    d = pick(r, [5, 6, 8]); a, b = r.randint(1, d - 2), r.randint(1, d - 2)
    if a + b >= d: return None
    return S(f"The circle shows {a}/{d} + {b}/{d}. What is the total?", [f"{a + b}/{d}"], o="O2", fig=PIE(d, range(a + b)))
def f4(r):
    d = pick(r, [4, 5, 8, 10]); a = r.randint(1, d - 1)
    return N(f"Find the missing number: {a}/{d} + ☐/{d} = 1", d - a, o="O2")
def f5(r):
    d = pick(r, [6, 8, 10]); a, b = r.randint(1, d - 2), r.randint(1, d - 2)
    if a + b >= d: return None
    return TB("Complete the table. Write the numerator.", ["Calculation", f"Answer (over {d})"], [[f"{a}/{d} + {b}/{d}", B(a + b)], [f"1 − {a}/{d}", B(d - a)]], o="O2")
def f6(r):
    d = pick(r, [6, 8, 10, 12]); a, b = r.randint(1, 3), r.randint(1, 3)
    return S(f"A cake is cut into {d} equal slices. Jo eats {a} slices and Lee eats {b}. What fraction of the cake is left?", [f"{d - a - b}/{d}"], o="O2", d="H")
def f7(r):
    d = pick(r, [5, 7, 9]); a, b = r.randint(2, d - 1), r.randint(2, d - 1)
    if a + b <= d: return None
    return MC(f"Is {a}/{d} + {b}/{d} more or less than 1?", "more than 1", ["less than 1", "exactly 1"], o="O2", d="H")
def f8(r):
    d = pick(r, [4, 5, 8]); a = r.randint(2, d - 1); b = r.randint(1, a - 1)
    return S(f"A jug is {a}/{d} full. {b}/{d} is poured out. How full is it now?", [f"{a - b}/{d}"], o="O2")


s.std([f3, f5, f1, f2, f4, f8, f6, f7], EX("Explain why 2/9 + 5/9 = 7/9.", [("the parts are all ninths", "ninths|same size|same denominator"), ("2 + 5 = 7 ninths", "2 ?\\+ ?5|7 ninths|seven")], "Both fractions are ninths, so the parts are the same size. 2 ninths and 5 ninths make 7 ninths: 7/9.", o="O2"))

U.mindmap(("Mental strategies", "Round and adjust • number bonds to 100", "O1", "13.1"), ("Fractions", "Same denominator: add or subtract the numerators", "O2", "13.2"))
