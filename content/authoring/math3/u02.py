# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 2 Addition, subtraction and money (2.1 Addition, 2.2 Subtraction, 2.3 Money).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(2, "Addition, Subtraction and Money", "Number",
         "Adding and subtracting 2- and 3-digit numbers, checking with the inverse, and using dollars and cents.",
         {"O1": {"code": "3Nc.01", "sec": "2.1", "codeNote": "", "t": "Add 2-digit and 3-digit numbers mentally and with written methods."},
          "O2": {"code": "3Nc.02", "sec": "2.2", "codeNote": "", "t": "Subtract 2-digit and 3-digit numbers, and check using addition."},
          "O3": {"code": "3Nm.01", "sec": "2.3", "codeNote": "", "t": "Use money (dollars and cents) to add, subtract and find change."}})
TOYS = ["ball", "kite", "yo-yo", "car", "puzzle", "book"]

s = U.section("2.1", "Addition", ["O1"])
s.idea("Adding in parts", ["Split numbers into hundreds, tens and ones: 245 + 132 = 300 + 70 + 7 = **377**.",
       "When the ones add to 10 or more, **exchange** 10 ones for 1 ten."], table={"head": ["", "H", "T", "O"], "rows": [["", "2", "4", "5"], ["+", "1", "3", "2"], ["=", "3", "7", "7"]]})
s.check(N("Work out 36 + 47.", 83, o="O1"))
s.check(MC('Before you read on: what is 38 + 5?', '43', [('33', 'Adding makes it bigger.'), ('313', '8 + 5 = 13: write 3 and carry 1 ten.')], o='O1'))
s.mistake("Line up the columns", ["Ones go under ones, tens under tens and hundreds under hundreds."])


def a1(r):
    a, b = r.randint(11, 89), r.randint(11, 89)
    return N(f"Work out {a} + {b}.", a + b, o="O1")
def a2(r):
    a, b = r.randint(100, 600), r.randint(100, 399)
    return N(f"Work out {a} + {b}.", a + b, o="O1")
def a3(r):
    a, b = r.randint(100, 500), r.randint(10, 99)
    return TB(f"Add {a} + {b} in parts.", ["Part", "Answer"], [["hundreds", B(a // 100 * 100)], ["tens", B((a // 10 % 10 + b // 10) * 10)], ["ones", B(a % 10 + b % 10)], ["total", B(a + b)]], o="O1")
def a4(r):
    a, b = r.randint(20, 90), r.randint(20, 90)
    return N(f"Sam has {a} stickers. He gets {b} more. How many stickers does he have now?", a + b, "stickers", units=["stickers"], o="O1")
def a5(r):
    a, b, c = r.randint(10, 50), r.randint(10, 50), r.randint(10, 50)
    return N(f"Work out {a} + {b} + {c}.", a + b + c, o="O1", d="H")
def a6(r):
    a, t = r.randint(10, 80), r.randint(100, 200)
    return N(f"Find the missing number: {a} + ☐ = {t}", t - a, o="O1", d="H")
def a7(r):
    lab = ["Mon", "Tue", "Wed"]; v = [r.randint(10, 60) for _ in lab]
    return N("The table shows how many books were read each day. How many books altogether?", sum(v), "books", units=["books"], o="O1", data={"head": ["Day", *lab], "rows": [["Books", *map(str, v)]]})
def a8(r):
    a = r.randint(1, 9) * 10
    return N(f"What do you add to {a} to make 100?", 100 - a, o="O1")


s.std([a3, a7, a1, a2, a4, a8, a5, a6], EX("Explain how to add 48 + 35.", [("add the tens: 40 + 30 = 70", "70|40 ?\\+ ?30"), ("add the ones: 8 + 5 = 13, then 70 + 13 = 83", "13|83")], "Add the tens: 40 + 30 = 70. Add the ones: 8 + 5 = 13. Then 70 + 13 = 83.", o="O1"))

s = U.section("2.2", "Subtraction", ["O2"])
s.idea("Taking away", ["Subtract the hundreds, tens and ones: 586 − 243 = **343**.",
       "If there are not enough ones, **exchange** 1 ten for 10 ones. Check by adding back: 343 + 243 = 586."], fig=NL(0, 10))
s.check(N("Work out 75 − 28.", 47, o="O2"))
s.check(MC('Before you read on: what is 50 − 7?', '43', [('57', 'Subtracting makes it smaller.'), ('47', '50 − 7: count back 7.')], o='O2'))
s.mistake("Bigger take smaller?", ["In 52 − 17 you cannot do 7 − 2. Exchange a ten: 12 − 7 = 5."])


def b1(r):
    a, b = sorted(r.sample(range(11, 99), 2), reverse=True)
    return N(f"Work out {a} − {b}.", a - b, o="O2")
def b2(r):
    a, b = r.randint(400, 999), r.randint(100, 399)
    return N(f"Work out {a} − {b}.", a - b, o="O2")
def b3(r):
    a, b = r.randint(30, 99), r.randint(5, 25)
    return N(f"There are {a} birds on a roof. {b} fly away. How many are left?", a - b, "birds", units=["birds"], o="O2")
def b4(r):
    a, b = r.randint(50, 99), r.randint(10, 49)
    return MC(f"Which addition checks that {a} − {b} = {a - b}?", f"{a - b} + {b} = {a}", [f"{a} + {b} = {a + b}", f"{a - b} − {b} = {a - 2 * b}"], o="O2")
def b5(r):
    a, b = r.randint(20, 99), r.randint(20, 99)
    if a == b: return None
    return N(f"What is the difference between {a} and {b}?", abs(a - b), o="O2")
def b6(r):
    a = r.randint(200, 900); b = r.randint(10, 90)
    return TB("Complete the table.", ["Calculation", "Answer"], [[f"{a} − {b}", B(a - b)], [f"{a} − 100", B(a - 100)]], o="O2")
def b7(r):
    lab = ["Red", "Blue", "Green"]; v = r.sample(range(10, 60), 3); i, j = sorted(range(3), key=lambda k: -v[k])[:2]
    return N(f"The table shows votes for team colours. How many more votes did {lab[i]} get than {lab[j]}?", v[i] - v[j], "votes", units=["votes"], o="O2", data={"head": ["Colour", *lab], "rows": [["Votes", *map(str, v)]]})
def b8(r):
    t, a = r.randint(60, 99), r.randint(10, 50)
    return N(f"Find the missing number: {t} − ☐ = {a}", t - a, o="O2", d="H")


s.std([b6, b7, b1, b2, b3, b4, b5, b8], EX("Explain how to check that 84 − 29 = 55.", [("add back: 55 + 29", "55 ?\\+ ?29|add"), ("55 + 29 = 84, so it is right", "84")], "Use the inverse: add the answer to the number you took away. 55 + 29 = 84, so 84 − 29 = 55 is right.", o="O2"))

s = U.section("2.3", "Money", ["O3"])
s.idea("Dollars and cents", ["**100 cents = 1 dollar**. We write $3.45 for 3 dollars and 45 cents.",
       "To find **change**, take the cost away from the money you pay: pay $5, cost $3.20, change = **$1.80**."], table={"head": ["Coins", "1c", "5c", "10c", "25c", "50c"], "rows": [["Value (cents)", "1", "5", "10", "25", "50"]]})
s.check(N("How many cents are in $2?", 200, "cents", units=["cents"], o="O3"))
s.check(MC('Before you read on: you pay $1 for something that costs 65c. How much change?', '35c', [('45c', '65 + 35 = 100.'), ('25c', 'Count on from 65c to $1.')], o='O3'))
s.mistake("Dollars and cents", ["$1.5 is not 1 dollar 5 cents. Write $1.05 for 1 dollar 5 cents."])


def m1(r):
    d = r.randint(1, 9); c = r.randint(1, 99)
    return N(f"How many cents is ${d}.{c:02d}?", 100 * d + c, "cents", units=["cents"], o="O3")
def m2(r):
    p = [r.randint(1, 9) * 10 + pick(r, [0, 5]) for _ in range(3)]; it = r.sample(TOYS, 3); i, j = r.sample(range(3), 2)
    return N(f"Use the price list. How much do a {it[i]} and a {it[j]} cost together, in cents?", p[i] + p[j], "cents", units=["cents"], o="O3", data={"head": ["Toy", *it], "rows": [["Price (cents)", *map(str, p)]]})
def m3(r):
    c = r.randint(5, 95)
    return N(f"You pay 1 dollar (100 cents) for a pencil that costs {c} cents. How much change do you get?", 100 - c, "cents", units=["cents"], o="O3")
def m4(r):
    n = r.randint(2, 9); k = pick(r, [5, 10, 20, 50])
    return N(f"How much money is {n} coins of {k} cents?", n * k, "cents", units=["cents"], o="O3")
def m5(r):
    cs = r.sample([1, 5, 10, 25, 50], 3)
    return TB("Count the coins.", ["Coin", "How many", "Value (cents)"], [[f"{c}c", str(n), B(c * n)] for c, n in zip(cs, [r.randint(1, 4) for _ in cs])], o="O3")
def m6(r):
    a, b = r.randint(1, 4), r.randint(1, 4); ca, cb = r.randint(10, 90), r.randint(10, 90)
    return N(f"A book costs ${a}.{ca:02d} and a pen costs ${b}.{cb:02d}. How much is that in cents?", 100 * (a + b) + ca + cb, "cents", units=["cents"], o="O3", d="H")
def m7(r):
    c = r.randint(2, 9) * 50
    return N(f"Mia pays $5 for a toy that costs {c} cents. How much change does she get, in cents?", 500 - c, "cents", units=["cents"], o="O3", d="H")
def m8(r):
    t = r.randint(2, 9) * 10 + 5
    return MC(f"Which coins make {t} cents?", f"{(t - 5) // 10} × 10c and 1 × 5c", [f"{t // 10} × 10c", f"{t // 5 + 1} × 5c", "1 × 50c"], o="O3")


s.std([m2, m5, m1, m3, m4, m8, m6, m7], EX("Explain how to find the change from $2 when you spend $1.35.", [("$2 is 200 cents and $1.35 is 135 cents", "200|135"), ("200 − 135 = 65 cents", "65")], "$2 is 200 cents and $1.35 is 135 cents. Change = 200 − 135 = 65 cents.", o="O3"))

U.mindmap(("Addition", "Split into H, T, O • exchange", "O1", "2.1"), ("Subtraction", "Exchange a ten • check by adding", "O2", "2.2"), ("Money", "100 cents = $1 • change", "O3", "2.3"))
