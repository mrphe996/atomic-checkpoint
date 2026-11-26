# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 9 More addition and subtraction (9.1 Addition, 9.2 Subtraction, 9.3 Complements).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(9, "More Addition and Subtraction", "Number",
         "Adding and subtracting 3-digit numbers with exchanging, estimating answers, and number pairs that make 100 and 1000.",
         {"O1": {"code": "3Nc.06", "sec": "9.1", "codeNote": "", "t": "Estimate and add 3-digit numbers, including exchanging."},
          "O2": {"code": "3Nc.07", "sec": "9.2", "codeNote": "", "t": "Estimate and subtract 3-digit numbers, including exchanging, and check with the inverse."},
          "O3": {"code": "3Nc.08", "sec": "9.3", "codeNote": "", "t": "Know complements: pairs of multiples of 10 that make 100 and multiples of 100 that make 1000."}})

s = U.section("9.1", "Addition", ["O1"])
s.idea("Column addition", ["Add the **ones**, then the **tens**, then the **hundreds**. If a column makes 10 or more, **exchange**: 10 ones = 1 ten, 10 tens = 1 hundred.",
       "Estimate first: 368 + 257 ≈ 370 + 260 = 630. The answer is 625."], table={"head": ["", "H", "T", "O"], "rows": [["", "3", "6", "8"], ["+", "2", "5", "7"], ["=", "6", "2", "5"]]})
s.check(N("Work out 245 + 168.", 413, o="O1"))
s.check(MC('Before you read on: what is 45 + 30?', '75', [('48', 'Add 3 tens, not 3 ones.'), ('85', '40 + 30 = 70, plus 5.')], o='O1'))
s.mistake("Carry the 1", ["When 8 + 7 = 15, write 5 and exchange the ten into the tens column."])


def a1(r):
    a, b = r.randint(100, 600), r.randint(100, 399)
    return N(f"Work out {a} + {b}.", a + b, o="O1")
def a2(r):
    a, b = r.randint(105, 499), r.randint(15, 99)
    return N(f"Work out {a} + {b}.", a + b, o="O1")
def a3(r):
    a, b = r.randint(110, 490), r.randint(110, 490)
    e = round(a, -1) + round(b, -1)
    return MC(f"Which is the best estimate for {a} + {b}?", str(e), [str(e + 100), str(e - 100), str(round(a, -1) + b)], o="O1")
def a4(r):
    a, b = r.randint(100, 500), r.randint(100, 400)
    return TB(f"Work out {a} + {b} in columns.", ["H", "T", "O"], [[B((a + b) // 100), B((a + b) // 10 % 10), B((a + b) % 10)]], o="O1")
def a5(r):
    a, b = r.randint(150, 450), r.randint(150, 450)
    return N(f"A farm has {a} sheep and {b} goats. How many animals altogether?", a + b, "animals", units=["animals"], o="O1")
def a6(r):
    lab = ["Mon", "Tue", "Wed"]; v = [r.randint(100, 300) for _ in lab]
    return N("The table shows visitors to a museum. How many visitors came altogether?", sum(v), "visitors", units=["visitors"], o="O1", data={"head": ["Day", *lab], "rows": [["Visitors", *map(str, v)]]})
def a7(r):
    a, t = r.randint(100, 500), r.randint(600, 999)
    return N(f"Find the missing number: {a} + ☐ = {t}", t - a, o="O1", d="H")
def a8(r):
    a, b, c = r.randint(100, 300), r.randint(100, 300), r.randint(10, 99)
    return N(f"Work out {a} + {b} + {c}.", a + b + c, o="O1", d="H")


s.std([a4, a6, a1, a2, a3, a5, a7, a8], EX("Explain how to add 356 + 278.", [("ones: 6 + 8 = 14, exchange a ten", "14|exchange|carry"), ("the answer is 634", "634")], "Add the ones: 6 + 8 = 14, write 4 and exchange 1 ten. Tens: 5 + 7 + 1 = 13, write 3 and exchange 1 hundred. Hundreds: 3 + 2 + 1 = 6. The answer is 634.", o="O1"))

s = U.section("9.2", "Subtraction", ["O2"])
s.idea("Column subtraction", ["Subtract the ones, then the tens, then the hundreds. If the top digit is smaller, **exchange** from the next column.",
       "Check with the inverse: if 532 − 178 = 354, then 354 + 178 = 532."], table={"head": ["", "H", "T", "O"], "rows": [["", "5", "3", "2"], ["−", "1", "7", "8"], ["=", "3", "5", "4"]]})
s.check(N("Work out 463 − 128.", 335, o="O2"))
s.check(MC('Before you read on: what is 82 − 9?', '73', [('71', '82 − 10 = 72, then add 1 back.'), ('91', 'Subtracting makes it smaller.')], o='O2'))
s.mistake("Top minus bottom", ["In 532 − 178, the ones are 2 − 8, not 8 − 2. Exchange first."])


def b1(r):
    a, b = r.randint(400, 999), r.randint(100, 399)
    return N(f"Work out {a} − {b}.", a - b, o="O2")
def b2(r):
    a, b = r.randint(200, 999), r.randint(11, 99)
    return N(f"Work out {a} − {b}.", a - b, o="O2")
def b3(r):
    a, b = r.randint(400, 900), r.randint(110, 390)
    return MC(f"Which addition checks {a} − {b} = {a - b}?", f"{a - b} + {b} = {a}", [f"{a} + {b} = {a + b}", f"{a} − {a - b} = {b + 1}"], o="O2")
def b4(r):
    a, b = r.randint(300, 900), r.randint(100, 290)
    return TB(f"Work out {a} − {b} in columns.", ["H", "T", "O"], [[B((a - b) // 100), B((a - b) // 10 % 10), B((a - b) % 10)]], o="O2")
def b5(r):
    a, b = r.randint(300, 900), r.randint(100, 290)
    return N(f"A library has {a} books. {b} are borrowed. How many are left on the shelves?", a - b, "books", units=["books"], o="O2")
def b6(r):
    a, b = r.randint(300, 900), r.randint(100, 290)
    e = round(a, -2) - round(b, -2)
    return MC(f"Which is the best estimate for {a} − {b}?", str(e), [str(e + 200), str(e - 100) if e > 100 else str(e + 300), str(round(a, -2) + round(b, -2))], o="O2")
def b7(r):
    v = r.sample(range(150, 600), 3); nm = ["Ali", "Bo", "Cy"]; i, j = sorted(range(3), key=lambda k: -v[k])[:2]
    return N(f"The table shows points scored in a game. How many more did {nm[i]} score than {nm[j]}?", v[i] - v[j], "points", units=["points"], o="O2", data={"head": ["Name", *nm], "rows": [["Points", *map(str, v)]]})
def b8(r):
    t, a = r.randint(500, 999), r.randint(100, 400)
    return N(f"Find the missing number: {t} − ☐ = {a}", t - a, o="O2", d="H")


s.std([b4, b7, b1, b2, b3, b5, b6, b8], EX("Explain how to check 641 − 275 = 366.", [("add the answer to the number taken away", "add|366 ?\\+ ?275|inverse"), ("366 + 275 = 641, so it is right", "641")], "Use the inverse: 366 + 275 = 641. This is the number we started with, so the subtraction is right.", o="O2"))

s = U.section("9.3", "Complements", ["O3"])
s.idea("Pairs that make 100 and 1000", ["Pairs of tens that make 100: 30 + 70, 40 + 60, 80 + 20.",
       "Pairs of hundreds that make 1000: 300 + 700, 600 + 400. Use what you know: 3 + 7 = 10, so 30 + 70 = 100 and 300 + 700 = 1000."], table={"head": ["", "", ""], "rows": [["3 + 7 = 10", "30 + 70 = 100", "300 + 700 = 1000"]]})
s.check(N("What do you add to 60 to make 100?", 40, o="O3"))
s.check(MC('Before you read on: what goes with 37 to make 100?', '63', [('73', '37 + 63 = 100.'), ('67', 'Check: 37 + 67 = 104.')], o='O3'))
s.mistake("Not 1000 − 10", ["The partner of 400 to make 1000 is 600."])


def k1(r):
    a = r.randint(1, 9) * 10
    return N(f"What do you add to {a} to make 100?", 100 - a, o="O3")
def k2(r):
    a = r.randint(1, 9) * 100
    return N(f"What do you add to {a} to make 1000?", 1000 - a, o="O3")
def k3(r):
    xs = r.sample(range(1, 10), 3)
    return TB("Complete the pairs that make 100.", ["Number", "Partner"], [[str(10 * x), B(100 - 10 * x)] for x in xs], o="O3")
def k4(r):
    a = r.randint(1, 9) * 10
    return N("The bar shows 100. One part is shown. Find the missing part.", 100 - a, o="O3", data={"head": ["Whole", "100"], "rows": [["Parts", f"{a} + ?"]]})
def k5(r):
    a = r.randint(1, 9) * 100
    return MC(f"Which pair makes 1000?", f"{a} + {1000 - a}", [f"{a} + {100 - a // 10}", f"{a} + {900 - a if a < 900 else 200}", f"{a} + {1000 - a + 100}"], o="O3")
def k6(r):
    a = r.randint(11, 99)
    return N(f"What do you add to {a} to make 100?", 100 - a, o="O3", d="H")
def k7(r):
    a = r.randint(1, 9) * 10
    return N(f"A box holds 100 pens. There are {a} pens in it. How many more pens fit?", 100 - a, "pens", units=["pens"], o="O3")
def k8(r):
    a = r.randint(1, 9) * 100
    return N(f"Lily needs 1000 points to win. She has {a}. How many more does she need?", 1000 - a, "points", units=["points"], o="O3", d="H")


def c93(r):
    return MC('Tom says 46 + 64 = 100. Is he right?', 'No: 46 + 54 = 100', [('Yes', '46 + 64 = 110.'), ('No: 46 + 44 = 100', '46 + 44 = 90.')], o='O3', d="H", reason='The ones must make 10 and the tens must make 90: 46 + 54.')


s.std([k3, k4, k1, k2, k5, k7, k6, k8], EX("Explain how knowing 4 + 6 = 10 helps you find 400 + 600.", [("400 is 4 hundreds and 600 is 6 hundreds", "hundreds|4 hundreds"), ("4 + 6 = 10 hundreds = 1000", "1000|10 hundreds")], "400 is 4 hundreds and 600 is 6 hundreds. 4 + 6 = 10, so together they make 10 hundreds, which is 1000.", o="O3"),
      deep=[c93])

U.mindmap(("Addition", "Columns • exchange • estimate", "O1", "9.1"), ("Subtraction", "Exchange • check with adding", "O2", "9.2"), ("Complements", "Pairs to 100 and 1000", "O3", "9.3"))
