# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 4 Addition and subtraction (1) (4.1 Positive and negative integers,
4.2 Using letters to represent numbers). Written by the Atomic teaching team."""
from kit import *

U = Unit(4, "Addition and Subtraction (1)", "Number",
         "Adding and subtracting positive and negative numbers, and using letters to stand for unknown numbers.",
         {"O1": {"code": "6Ni.01", "sec": "4.1", "codeNote": "", "t": "Add and subtract integers, including negative numbers, using a number line."},
          "O2": {"code": "6Ae.01", "sec": "4.2", "codeNote": "", "t": "Use letters to represent unknown numbers and find their values."}})
sg = lambda v: f"−{-v}" if v < 0 else str(v)
NL = lambda lo, hi: {"kind": "numline", "min": lo, "max": hi}

s = U.section("4.1", "Positive and negative integers", ["O1"])
s.idea("Below zero", ["Numbers below zero are **negative**: −1, −2, −3, … On a number line they are to the left of 0.",
       "To add, move **right**. To subtract, move **left**. −3 + 5 = 2 and 2 − 6 = −4."], fig=NL(-6, 6))
s.check(N("Work out −4 + 7.", 3, o="O1"))
s.idea("Temperature", ["Temperatures below 0 °C are negative. A rise from −5 °C to 3 °C is a change of 8 degrees."])
s.mistake("Left is smaller", ["−7 is smaller than −2, because it is further left on the number line."])


def n1(r):
    a, b = r.randint(-9, -1), r.randint(1, 12)
    return N(f"Work out {sg(a)} + {b}.", a + b, o="O1", fig=NL(min(a, 0) - 1, max(a + b, 0) + 1) if b <= 12 else None)
def n2(r):
    a, b = r.randint(1, 9), r.randint(2, 15)
    if b <= a: return None
    return N(f"Work out {a} − {b}.", a - b, o="O1")
def n3(r):
    a, b = r.randint(-10, -1), r.randint(1, 8)
    return N(f"Work out {sg(a)} − {b}.", a - b, o="O1")
def n4(r):
    lo, hi = r.randint(-12, -1), r.randint(1, 15)
    return N(f"At night the temperature was {sg(lo)} °C. At noon it was {hi} °C. By how many degrees did it rise?", hi - lo, "°C", units=["°C", "degrees"], o="O1", fig={"kind": "numline", "min": lo - 1, "max": hi + 1})
def n5(r):
    xs = r.sample(range(-12, 12), 4)
    return OD("Put these numbers in order, smallest first.", [sg(x) for x in sorted(xs)], o="O1")
def n6(r):
    a, b = r.sample(range(-15, 10), 2)
    return CMP(sg(a), sg(b), "<" if a < b else ">", o="O1")
def n7(r):
    a, b, c = r.randint(-8, -1), r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out {sg(a)} + {b} − {c}.", a + b - c, o="O1", d="H")
def n8(r):
    a = r.randint(-9, -1); b = r.randint(2, 10)
    return TB("Complete the table.", ["Start", "Change", "End"], [[sg(a), f"+{b}", B(a + b)], [sg(a), f"−{b}", B(a - b)]], o="O1")
def n9(r):
    a, t = r.randint(-9, -1), r.randint(-4, 8)
    if t == a: return None
    return N(f"What must you add to {sg(a)} to get {sg(t)}?", t - a, o="O1", d="H")


s.std([n4, n8, n1, n2, n3, n5, n6, n7, n9], EX("Explain why −2 − 5 = −7.", [("start at −2 and move 5 to the left", "left|move 5|count back"), ("you land on −7", "−7|-7")], "Start at −2 on the number line. Subtracting 5 means moving 5 places to the left, which lands on −7.", o="O1"))

s = U.section("4.2", "Using letters to represent numbers", ["O2"])
s.idea("Letters for numbers", ["A letter can stand for an unknown number. In **n + 4 = 11**, n stands for 7 because 7 + 4 = 11.",
       "**3n** means 3 × n. If n = 5, then 3n = 15."], table={"head": ["n", "1", "2", "3", "4"], "rows": [["n + 4", "5", "6", "7", "8"], ["3n", "3", "6", "9", "12"]]})
s.check(N("If a + 9 = 20, what is a?", 11, o="O2"))
s.idea("Inverse operations", ["Use the **inverse** to find the unknown: if n − 6 = 9, then n = 9 + 6 = 15. If 4n = 28, then n = 28 ÷ 4 = 7."])
s.mistake("3n is not 3 + n", ["3n means 3 × n. If n = 2, 3n = 6, not 5."])


def l1(r):
    n, a = r.randint(2, 40), r.randint(2, 30)
    return N(f"Find the value of n: n + {a} = {n + a}", n, o="O2")
def l2(r):
    n, a = r.randint(5, 40), r.randint(2, 20)
    return N(f"Find the value of n: n − {a} = {n - a}", n, o="O2")
def l3(r):
    n, a = r.randint(2, 12), r.randint(2, 9)
    return N(f"Find the value of n: {a}n = {a * n}", n, o="O2")
def l4(r):
    a, n = r.randint(2, 9), r.randint(2, 10)
    return N(f"If n = {n}, what is {a}n + {a}?", a * n + a, o="O2")
def l5(r):
    a = r.randint(2, 9)
    return TB(f"Complete the table for y = n + {a}.", ["n", "y"], [[str(n), B(n + a)] for n in (1, 3, 6)], o="O2")
def l6(r):
    a, b = r.randint(2, 6), r.randint(1, 9)
    return TB(f"Complete the table for y = {a}n + {b}.", ["n", "y"], [[str(n), B(a * n + b)] for n in (1, 2, 5)], o="O2", d="H")
def l7(r):
    a, t = r.randint(3, 9), r.randint(20, 60)
    return N(f"A box holds b pens. {a} boxes hold {a * (t // a)} pens. What is b?", t // a, "pens", units=["pens"], o="O2")
def l8(r):
    x, y = r.randint(2, 20), r.randint(2, 20)
    return GD(f"a + b = {x + y}. Is each pair possible?", "Possible?", [(f"a = {x}, b = {y}", "Yes"), (f"a = {x + 1}, b = {y + 1}", "No"), (f"a = {y}, b = {x}", "Yes"), (f"a = {x + 2}, b = {y - 1}", "No")], o="O2", extra=["Yes", "No"])
def l9(r):
    a, b, n = r.randint(2, 6), r.randint(1, 12), r.randint(2, 10)
    return N(f"Find the value of n: {a}n + {b} = {a * n + b}", n, o="O2", d="H")


s.std([l5, l8, l1, l2, l3, l4, l7, l6, l9], EX("Explain how to find n when n − 8 = 15.", [("use the inverse: add 8", "add 8|\\+ ?8|inverse"), ("n = 23", "23")], "The inverse of subtracting 8 is adding 8. So n = 15 + 8 = 23.", o="O2"))

U.mindmap(("Negative numbers", "Number line • temperature", "O1", "4.1"), ("Letters", "n stands for a number • 3n = 3 × n", "O2", "4.2"))
