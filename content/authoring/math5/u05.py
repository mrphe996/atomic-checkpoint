# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 5 Addition and subtraction (1) (5.1 Addition and subtraction including decimal numbers,
5.2 Addition and subtraction of positive and negative numbers). Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(5, "Addition and Subtraction (1)", "Number",
         "Adding and subtracting whole numbers and decimals with one decimal place, and adding and subtracting with negative numbers.",
         {"O1": {"code": "5Nc.01", "sec": "5.1", "codeNote": "", "t": "Estimate, add and subtract whole numbers and numbers with one decimal place."},
          "O2": {"code": "5Ni.01", "sec": "5.2", "codeNote": "", "t": "Add and subtract positive and negative numbers in context, such as temperature."}})

s = U.section("5.1", "Addition and subtraction including decimal numbers", ["O1"])
s.idea("Columns and points", ["Write numbers in columns with the **decimal points in line**. Then add or subtract as with whole numbers.",
       "Estimate first: 38.6 + 24.7 ≈ 39 + 25 = 64. The answer 63.3 is close."], table={"head": ["", "Tens", "Ones", ".", "Tenths"], "rows": [["", "3", "8", ".", "6"], ["+", "2", "4", ".", "7"], ["=", "6", "3", ".", "3"]]})
s.check(N("Work out 9.4 − 3.5.", 5.9, o="O1"))
s.mistake("Exchange", ["In 9.4 − 3.5 you cannot take 5 tenths from 4 tenths: exchange 1 one for 10 tenths."])


def a1(r):
    a, b = r.randint(100, 9999), r.randint(100, 9999)
    return N(f"Work out {a} + {b}.", a + b, o="O1")
def a2(r):
    a, b = sorted([r.randint(100, 9999), r.randint(100, 9999)])
    return N(f"Work out {b} − {a}.", b - a, o="O1")
def a3(r):
    a, b = dec(r, 1, 80, 1), dec(r, 1, 80, 1)
    return N(f"Work out {fmt(a)} + {fmt(b)}.", round(a + b, 1), o="O1")
def a4(r):
    a, b = sorted([dec(r, 1, 50, 1), dec(r, 1, 50, 1)])
    if a == b: return None
    return N(f"Work out {fmt(b)} − {fmt(a)}.", round(b - a, 1), o="O1")
def a5(r):
    items = ["pen", "rubber", "ruler", "glue"]; p = [dec(r, 1, 9, 1) for _ in items]; i, j = r.sample(range(4), 2)
    return N(f"Use the price list. How much do a {items[i]} and a {items[j]} cost together?", round(p[i] + p[j], 1), "$", units=["$", "dollars"], o="O1", data={"head": ["Item", *items], "rows": [["Price ($)", *[fmt(x) for x in p]]]})
def a6(r):
    a, b = dec(r, 1, 9, 1), dec(r, 1, 9, 1)
    return TB("Complete the table.", ["Calculation", "Answer"], [[f"{fmt(a)} + {fmt(b)}", B(round(a + b, 1))], [f"{fmt(max(a, b))} − {fmt(min(a, b))}", B(round(abs(a - b), 1))]], o="O1")
def a7(r):
    a, b = dec(r, 10, 60, 1), dec(r, 10, 60, 1); e = round(a) + round(b)
    return MC(f"Which is the best estimate for {fmt(a)} + {fmt(b)}?", str(e), [str(e + 10), str(e * 10), str(e - 10)], o="O1")
def a8(r):
    a, t = dec(r, 1, 9, 1), r.randint(10, 20)
    return N(f"Find the missing number: {fmt(a)} + ☐ = {t}", round(t - a, 1), o="O1", d="H")
def a9(r):
    l, c1, c2 = r.randint(10, 20), dec(r, 1, 4, 1), dec(r, 1, 4, 1)
    return N(f"A rope is {l} m long. Two pieces of {fmt(c1)} m and {fmt(c2)} m are cut off. How much is left?", round(l - c1 - c2, 1), "m", units=["m"], o="O1", d="H")


s.std([a5, a6, a1, a2, a3, a4, a7, a8, a9], EX("Explain how to check 46.8 + 21.5 = 68.3 by estimating.", [("round to 47 + 22 or 50 + 20", "47|22|50|20|round"), ("about 69 or 70, so 68.3 is sensible", "69|70|close|sensible")], "Round each number: 46.8 ≈ 47 and 21.5 ≈ 22. 47 + 22 = 69, which is close to 68.3, so the answer is sensible.", o="O1"))

s = U.section("5.2", "Addition and subtraction of positive and negative numbers", ["O2"])
s.idea("Using a number line", ["To **add**, move **right**. To **subtract**, move **left**. −4 + 6 = 2 and 3 − 5 = −2.",
       "On a thermometer, colder temperatures are lower: −8 °C is colder than −3 °C."], fig=NL(-6, 6))
s.check(N("The temperature is −2 °C. It rises by 5 degrees. What is the new temperature?", 3, "°C", units=["°C"], o="O2"))
s.mistake("The difference", ["From −3 to 4 is 7 steps: 3 steps to 0, then 4 more."])


def n1(r):
    a, b = r.randint(-9, -1), r.randint(1, 10)
    return N(f"Work out {sg(a)} + {b}.", a + b, o="O2", fig=NL(min(a, 0) - 1, max(a + b, 0) + 1))
def n2(r):
    a, b = r.randint(1, 6), r.randint(3, 12)
    if b <= a: return None
    return N(f"Work out {a} − {b}.", a - b, o="O2")
def n3(r):
    lo, hi = r.randint(-10, -1), r.randint(1, 12)
    return N(f"The temperature at night was {sg(lo)} °C. In the day it was {hi} °C. How many degrees warmer was the day?", hi - lo, "°C", units=["°C", "degrees"], o="O2", fig={"kind": "numline", "min": lo - 1, "max": hi + 1})
def n4(r):
    xs = r.sample(range(-10, 10), 4)
    return OD("Put these temperatures in order, coldest first.", [sg(x) + " °C" for x in sorted(xs)], o="O2")
def n5(r):
    a, b = r.sample(range(-12, 10), 2)
    return CMP(sg(a), sg(b), "<" if a < b else ">", o="O2")
def n6(r):
    a, d = r.randint(-5, 5), r.randint(3, 9)
    return TB("Complete the table.", ["Start (°C)", "Change", "End (°C)"], [[sg(a), f"falls {d}", B(a - d)], [sg(a), f"rises {d}", B(a + d)]], o="O2")
def n7(r):
    a, b = r.randint(-8, -1), r.randint(-8, -1)
    if a == b: return None
    return N(f"What is the difference between {sg(a)} and {sg(b)}?", abs(a - b), o="O2", d="H")
def n8(r):
    a, t = r.randint(-9, -1), r.randint(1, 9)
    return N(f"What must you add to {sg(a)} to make {t}?", t - a, o="O2", d="H")


s.std([n3, n6, n1, n2, n4, n5, n7, n8], EX("Explain why −2 − 4 = −6.", [("start at −2 and move 4 to the left", "left|count back|move 4"), ("you land on −6", "−6|-6")], "Start at −2 on the number line. Subtracting 4 means moving 4 places left, which lands on −6.", o="O2"))

U.mindmap(("Decimals", "Points in line • estimate first", "O1", "5.1"), ("Negative numbers", "Right to add • left to subtract • temperature", "O2", "5.2"))
