# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 16 The laws of arithmetic (16.1 The laws of arithmetic).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *

U = Unit(16, "The Laws of Arithmetic", "Number",
         "The order of operations with brackets, and using the commutative, associative and distributive laws to calculate efficiently.",
         {"O1": {"code": "6Ni.04", "sec": "16.1", "codeNote": "", "t": "Use the order of operations, including brackets, to work out calculations."},
          "O2": {"code": "6Ni.05", "sec": "16.1", "codeNote": "", "t": "Use the commutative, associative and distributive laws to simplify calculations."}})

s = U.section("16.1", "The laws of arithmetic", ["O1", "O2"])
s.idea("Order of operations", ["Work out **brackets** first, then **× and ÷**, then **+ and −**.",
       "2 + 3 × 4 = 2 + 12 = **14**, but (2 + 3) × 4 = 5 × 4 = **20**."], table={"head": ["Step", "1st", "2nd", "3rd"], "rows": [["Do", "Brackets", "× ÷", "+ −"]]})
s.check(N("Work out 20 − 3 × 5.", 5, o="O1"))
s.idea("Laws that help", ["**Commutative**: order does not matter for + and ×: 7 × 25 = 25 × 7.",
       "**Associative**: grouping does not matter for + and ×: (4 × 25) × 3 = 4 × (25 × 3).",
       "**Distributive**: 6 × 47 = 6 × 40 + 6 × 7 = 240 + 42 = 282."])
s.idea("Why the laws make calculating easier", ["Adding and multiplying can be done in any order (commutative) and grouped any way (associative): 4 × 17 × 25 = 4 × 25 × 17 = 100 × 17.",
       "Multiplying spreads over adding (distributive): 6 × 23 = 6 × 20 + 6 × 3."])
s.mistake("Not left to right", ["5 + 4 × 2 is 13, not 18. Multiply before you add."])


def o1(r):
    a, b, c = r.randint(2, 20), r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out {a} + {b} × {c}.", a + b * c, o="O1")
def o2(r):
    a, b, c = r.randint(2, 20), r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out ({a} + {b}) × {c}.", (a + b) * c, o="O1")
def o3(r):
    b, c = r.randint(2, 9), r.randint(2, 9); a = b * c + r.randint(1, 30)
    return N(f"Work out {a} − {b} × {c}.", a - b * c, o="O1")
def o4(r):
    c = r.randint(2, 9); q = r.randint(2, 9); a = r.randint(1, 20)
    return N(f"Work out {a} + {c * q} ÷ {c}.", a + q, o="O1")
def o5(r):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    return TB("Complete the table.", ["Calculation", "Answer"], [[f"{a} + {b} × {c}", B(a + b * c)], [f"({a} + {b}) × {c}", B((a + b) * c)]], o="O1")
def o6(r):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    t = (a + b) * c
    return MC(f"Where do the brackets go to make {a} + {b} × {c} = {t}?", f"({a} + {b}) × {c}", [f"{a} + ({b} × {c})", f"({a} + {b} × {c})"], o="O1", d="H")
def l1(r):
    k = r.randint(12, 99)
    return N(f"Use the distributive law to work out {k} × 6.", k * 6, o="O2", reason=f"{k // 10 * 10} × 6 + {k % 10} × 6")
def l2(r):
    a = r.randint(3, 19)
    return N(f"Work out 4 × {a} × 25 in your head.", 100 * a, o="O2", reason="4 × 25 = 100 first.")
def l3(r):
    laws = [("7 + 8 = 8 + 7", "commutative"), ("(2 × 5) × 9 = 2 × (5 × 9)", "associative"), ("6 × 13 = 6 × 10 + 6 × 3", "distributive"),
            ("15 × 4 = 4 × 15", "commutative"), ("(3 + 6) + 4 = 3 + (6 + 4)", "associative"), ("8 × 21 = 8 × 20 + 8 × 1", "distributive")]
    return GD("Which law does each statement show?", "Law", r.sample(laws, 4), o="O2", extra=["commutative", "associative", "distributive"])
def l4(r):
    a, b = r.randint(11, 39), r.randint(2, 9)
    return TB(f"Use the distributive law to work out {a} × {b}.", ["Part", "Answer"], [[f"{a // 10 * 10} × {b}", B(a // 10 * 10 * b)], [f"{a % 10} × {b}", B(a % 10 * b)], ["Total", B(a * b)]], o="O2")
def l5(r):
    a, b = r.randint(11, 99), r.randint(2, 9)
    if a % 10 == 0: return None
    return N(f"Find the missing number: {b} × {a} = {b} × {a - a % 10} + {b} × ☐", a % 10, o="O2")
def l6(r):
    a = r.randint(15, 45)
    return N(f"Work out {a} × 99 using {a} × 100 − {a}.", a * 99, o="O2", d="H")
def l7(r):
    n = r.randint(3, 9)
    return MC(f"Which is the same as {n} × (10 + 4)?", f"{n} × 10 + {n} × 4", [f"{n} × 10 + 4", f"{n} + 10 × 4", f"{n} × 14 × 4"], o="O2")
def l8(r):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out ({a} + {b}) × ({c} + 1).", (a + b) * (c + 1), o="O1", d="H")


def p1_1(r):
    rows = r.sample([("25 × 13 × 4", "Make 100 first"), ("38 + 47 + 2", "Make a ten first"), ("6 × 98", "Round and adjust"), ("7 × 24", "Split one number")], 4)
    return GD("Choose the best strategy for each.", "Strategy", rows, o="O1", d="H", extra=["Column method"], reason="Look for pairs that make 10 or 100, or numbers close to a round number.")


s.std([o5, l3, o1, o2, o3, o4, l1, l2, l4, l5, l7, o6, l6, l8], EX("Explain why 3 + 4 × 5 = 23 and not 35.", [("multiply before you add", "multipl.* before|× before|first"), ("4 × 5 = 20, then 3 + 20 = 23", "20|23")], "Multiplication comes before addition. 4 × 5 = 20 first, then 3 + 20 = 23. Working left to right gives the wrong answer, 35.", o="O1"), adv=[o6, l6, l8, l2, l1],
      deep=[p1_1])

U.mindmap(("Order of operations", "Brackets • × ÷ • + −", "O1", "16.1"), ("Laws", "Commutative • associative • distributive", "O2", "16.1"))
