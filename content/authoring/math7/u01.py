# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 1 Integers (1.1 Adding and subtracting integers, 1.2 Multiplying and dividing integers,
1.3 Lowest common multiples, 1.4 Highest common factors, 1.5 Tests for divisibility, 1.6 Square roots and cube roots).
Upgraded lesson (v2): why each rule works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from math import gcd
from kit import *
import kit as _kit
_kit.RAW_SIGNS = True   # this unit teaches the signs: show "5 − (−3)" exactly as written

U = Unit(1, "Integers", "Number",
         "Adding, subtracting, multiplying and dividing positive and negative integers, multiples and factors, tests for divisibility, and square and cube roots.",
         {"O1": {"code": "7Ni.01", "sec": "1.1", "codeNote": "", "t": "Add and subtract positive and negative integers, using a number line."},
          "O2": {"code": "7Ni.02", "sec": "1.2", "codeNote": "", "t": "Multiply and divide integers, including negative integers by positive integers."},
          "O3": {"code": "7Ni.03", "sec": "1.3", "codeNote": "", "t": "Find the lowest common multiple of two or more numbers."},
          "O4": {"code": "7Ni.04", "sec": "1.4", "codeNote": "", "t": "Find the highest common factor of two or more numbers."},
          "O5": {"code": "7Ni.05", "sec": "1.5", "codeNote": "", "t": "Use tests for divisibility by 2, 3, 4, 5, 6, 8, 9, 10 and 25."},
          "O6": {"code": "7Ni.06", "sec": "1.6", "codeNote": "", "t": "Know squares to 20 × 20 and cubes to 5 × 5 × 5, and find the matching square and cube roots."}})
sg = lambda v: f"({v})" if v < 0 else str(v)
lcm = lambda a, b: a * b // gcd(a, b)
NL = lambda lo, hi, **k: dict({"kind": "numline", "min": lo, "max": hi}, **k)
MV = lambda a, b, lo=None, hi=None: NL(lo if lo is not None else min(a, b) - 1, hi if hi is not None else max(a, b) + 1, **{"from": {"v": a, "closed": True}, "to": {"v": b, "closed": True}, "mark": b})
ASN = ["Always true", "Sometimes true", "Never true"]

# ================================================================== 1.1
s = U.section("1.1", "Adding and subtracting integers", ["O1"])
s.idea("Integers live on a number line", ["**Integers** are whole numbers: …, −3, −2, −1, 0, 1, 2, 3, … The further right, the bigger: −2 > −5, because −2 is warmer than −5 on a thermometer.",
       "Adding a positive number moves **right**; subtracting a positive number moves **left**. So −4 + 9 starts at −4 and moves 9 to the right, ending at 5."], fig=MV(-4, 5, -6, 6))
s.check(MC("Before you read on: which is bigger, −8 or −3?", "−3", [("−8", "8 is bigger than 3, but −8 is further left – it is colder."), ("They are equal", "They are at different places on the line.")], o="O1", hint="Picture a thermometer. Which is warmer?"))
s.idea("Why subtracting a negative means adding", ["Look at a pattern: 5 − 2 = 3, 5 − 1 = 4, 5 − 0 = 5. Each time we take away 1 less, the answer goes up by 1.",
       "Carry on the pattern: 5 − (−1) = 6, 5 − (−2) = 7. So **taking away a negative is the same as adding**.",
       "Adding a negative is like adding a debt: 5 + (−3) means you gain a debt of 3, so 5 + (−3) = 5 − 3 = 2."],
       table={"head": ["Calculation", "Answer"], "rows": [["5 − 2", "3"], ["5 − 1", "4"], ["5 − 0", "5"], ["5 − (−1)", "6"], ["5 − (−2)", "7"]]})
s.example("One sign changes everything", "Work out 3 + (−7) and 3 − (−7).", [("3 + (−7) = 3 − 7 = −4", "adding a negative moves left"), ("3 − (−7) = 3 + 7 = 10", "taking away a negative moves right")], "−4 and 10",
          p=["The numbers are the same; only one sign is different, and the answers are 14 apart."])
s.check(N("Work out −2 − (−9).", 7, o="O1", hint="Taking away −9 is the same as adding 9."))
s.example("Temperatures", "At midnight it is −4 °C. By noon it is 9 degrees warmer. What is the temperature at noon?", [("−4 + 9", "warmer means add"), ("= 5", "count 9 to the right from −4")], "5 °C")
s.method("Adding and subtracting integers", ["Change any two signs side by side into one: + (−) becomes −, and − (−) becomes +.", "Start at the first number on the number line.", "Move right for +, left for −. Check: is the answer sensible on the line?"])
s.mistake("Two signs together", ["− (−) means subtract a negative: it becomes + . But + (−) becomes − ."])


def a1(r):
    a, b = r.randint(-12, 12), r.randint(1, 12)
    return N(f"Work out {a} + {b}.", a + b, o="O1", fig=NL(min(a, 0) - 1, max(a + b, 0) + 1) if abs(a) < 9 and a + b < 12 else None)
def a2(r):
    a, b = r.randint(-10, 10), r.randint(1, 15)
    return N(f"Work out {a} − {b}.", a - b, o="O1")
def a3(r):
    a, b = r.randint(-10, 10), r.randint(-10, -1)
    return N(f"Work out {a} + ({b}).", a + b, o="O1", reason=f"Adding {b} is the same as subtracting {-b}.")
def a4(r):
    a, b = r.randint(-10, 10), r.randint(-10, -1)
    return N(f"Work out {a} − ({b}).", a - b, o="O1", d="H", reason=f"Subtracting {b} is the same as adding {-b}.")
def a5(r):
    t, c = r.randint(-12, -1), r.randint(3, 15)
    return N(f"The temperature is {t} °C. It rises by {c} degrees. What is the new temperature?", t + c, "°C", units=["°C"], o="O1")
def a6(r):
    a, b = r.randint(-15, -1), r.randint(-15, 15)
    if a == b: return None
    return N(f"What is the difference between {a} °C and {b} °C?", abs(a - b), "°C", units=["°C", "degrees"], o="O1", d="H", reason=f"{max(a, b)} − ({min(a, b)}) = {abs(a - b)}.")
def a7(r):
    vs = sorted(r.sample(range(-12, 12), 5))
    return OD("Put these integers in order, smallest first.", [str(v) for v in vs], o="O1", fig=NL(-12, 12) if False else None)
def a8(r):
    a, b, c = r.randint(-9, 9), r.randint(-9, 9), r.randint(1, 9)
    return TB("Complete the table.", ["Calculation", "Answer"], [[f"{a} + {sg(b)}", B(a + b)], [f"{a} − {sg(b)}", B(a - b)], [f"{b} − {c}", B(b - c)]], o="O1")
def a9(r):
    rows = [("−5 + 8", "3"), ("3 − 7", "−4"), ("−2 − 4", "−6"), ("6 + (−9)", "−3"), ("−1 − (−5)", "4"), ("−8 + 8", "0")]
    return GD("Find each answer.", "Answer", r.sample(rows, 4), o="O1", extra=["−2", "5"])
def a10(r):
    f, d = r.randint(2, 15), r.randint(3, 20)
    return N(f"A lift is on floor {f}. It goes down {d} floors. Floor 0 is the ground floor and floors below are negative. Which floor is it on now?", f - d, o="O1")


def b1(r):   # always / sometimes / never
    rows = r.sample([("a negative number + a negative number is negative", "Always true"), ("a positive number + a negative number is positive", "Sometimes true"),
                     ("a negative number − a positive number is positive", "Never true"), ("subtracting a negative makes a number bigger", "Always true"),
                     ("adding a negative makes a number bigger", "Never true"), ("the difference between two negative numbers is negative", "Never true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O1", d="H", extra=ASN,
              reason="Test with numbers. For example 5 + (−2) = 3 is positive but 2 + (−5) = −3 is negative, so 'positive + negative is positive' is only sometimes true. A difference is a distance, so it is never negative.")
def b2(r):   # spot the error
    a, b = r.randint(2, 9), r.randint(2, 9)
    return MC(f"Mia says {-a} − ({-b}) = {-a - b}. Is she right?", f"No: it is {-a + b}",
              [(f"Yes: {-a - b}", f"She has treated − (−{b}) as − {b}. Taking away a negative means adding."), (f"No: it is {a + b}", "The answer starts from −" + str(a) + ", not " + str(a) + "."), (f"No: it is {a - b}", "Check the starting number: it is negative.")],
              o="O1", d="H", hint="Replace − (−) with + first.", reason=f"{-a} − ({-b}) = {-a} + {b} = {-a + b}.")
def b3(r):   # work backwards: missing number
    a, x = r.randint(-9, 9), r.randint(-9, -1)
    return N(f"Find the missing number: {a} − ☐ = {a - x}", x, o="O1", d="H", hint=f"Is the answer bigger or smaller than {a}? Taking away a negative makes it bigger.",
             reason=f"{a - x} is {-x} more than {a}, so we took away −{-x}: {a} − ({x}) = {a - x}.")
def b4(r):   # find all pairs
    t = r.randint(-5, 3)
    fmt = lambda p, q: f"{sg(p)} + {q}"
    ok = [(p, t - p) for p in range(-8, 0) if t - p > 0]
    good = [fmt(*x) for x in r.sample(ok, 2)]
    near = [(p, t - p + d) for p in range(-8, 0) for d in (1, -1, 2) if t - p + d > 0]
    bad = list(dict.fromkeys(fmt(*x) for x in r.sample(near, 4)))[:2]
    return MS(f"Select ALL the calculations whose answer is {t}.", good, bad, o="O1", d="H", reason=f"Work out each one; keep those equal to {t}.")
def b5(r):   # which change is bigger (decision)
    a, b, c = r.randint(-12, -2), r.randint(2, 10), r.randint(-15, -3)
    return MC(f"At 6 a.m. it was {a} °C. By noon it was {b} °C, and by midnight it was {c} °C. Which change was bigger?", "6 a.m. to noon" if b - a > b - c else "noon to midnight" if b - c > b - a else "They were the same",
              [x for x in [("6 a.m. to noon", f"That rise was {b - a} degrees."), ("noon to midnight", f"That fall was {b - c} degrees."), ("They were the same", f"{b - a} and {b - c} degrees.")] if x[0] != ("6 a.m. to noon" if b - a > b - c else "noon to midnight" if b - c > b - a else "They were the same")],
              o="O1", d="H", reason=f"Rise: {b} − ({a}) = {b - a}. Fall: {b} − ({c}) = {b - c}.")


s.std([a8, a9, a1, a2, a3, a4, a5, a6, a10], EX("Explain why 3 − (−4) = 7.", [("subtracting a negative is the same as adding", ["same as add|becomes \\+|plus|add"]), ("3 + 4 = 7", ["3 ?\\+ ?4"])], "Taking away a negative number is the same as adding the positive: 3 − (−4) = 3 + 4 = 7.", o="O1"),
      deep=[b1, b2, b3, b4, b5])

# ================================================================== 1.2
s = U.section("1.2", "Multiplying and dividing integers", ["O2"])
s.idea("Why 4 × (−3) is negative", ["Multiplying is repeated adding. 4 × (−3) means 4 lots of −3: (−3) + (−3) + (−3) + (−3) = −12. Four debts of 3 make a debt of 12.",
       "On the number line: start at 0 and take 4 jumps of 3 to the **left**. You land on −12."], fig=MV(0, -12, -13, 1))
s.check(MC("Before you read on: what is the sign of 7 × (−2)?", "Negative", [("Positive", "7 lots of −2 is −2 added seven times – a bigger debt."), ("It depends on the numbers", "Any positive number of negative lots is negative.")], o="O2"))
s.idea("Division undoes multiplication", ["Because 4 × (−3) = −12, it must be true that (−12) ÷ 4 = −3: sharing a debt of 12 between 4 gives each a debt of 3.",
       "So the sign rules for dividing match the rules for multiplying."], table={"head": ["Calculation", "Sign of answer"], "rows": [["positive × positive", "+"], ["positive × negative", "−"], ["negative ÷ positive", "−"]]})
s.example("Same numbers, one sign different", "Work out 24 ÷ 6 and (−24) ÷ 6.", [("24 ÷ 6 = 4", "both positive"), ("(−24) ÷ 6 = −4", "a debt of 24 shared between 6")], "4 and −4",
          p=["The size of the answer is the same; only the sign changes."])
s.check(N("Work out 6 × (−4).", -24, o="O2"))
s.method("Multiplying and dividing integers", ["Work out the size of the answer, ignoring signs.", "Decide the sign: a positive and a negative give a negative.", "Check with a picture: lots of debts, or sharing a debt."])
s.mistake("Do the numbers first", ["Multiply the numbers as normal, then decide the sign."])


def m1(r):
    a, b = r.randint(2, 12), r.randint(-12, -2)
    return N(f"Work out {a} × ({b}).", a * b, o="O2")
def m2(r):
    a, b = r.randint(2, 12), r.randint(2, 12)
    return N(f"Work out ({-a * b}) ÷ {b}.", -a, o="O2")
def m3(r):
    a, t = r.randint(2, 9), r.randint(2, 8)
    return N(f"The temperature falls by {a} °C each hour. What is the total change after {t} hours? (Write a fall as a negative number.)", -a * t, "°C", units=["°C"], o="O2")
def m4(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"Find the missing number: {a} × ☐ = {-a * b}", -b, o="O2", d="H")
def m5(r):
    a, b = r.randint(2, 9), r.randint(-9, -2); c, d = r.randint(2, 9), r.randint(-9, -2)
    return TB("Complete the multiplication grid.", ["×", str(b), str(d)], [[str(a), B(a * b), B(a * d)], [str(c), B(c * b), B(c * d)]], o="O2")
def m6(r):
    rows = [("5 × (−2)", "Negative"), ("(−12) ÷ 3", "Negative"), ("4 × 3", "Positive"), ("(−30) ÷ 6", "Negative"), ("7 × 8", "Positive")]
    return GD("Is each answer positive or negative?", "Sign", r.sample(rows, 4), o="O2")
def m7(r):
    a, b, c = r.randint(2, 6), r.randint(-6, -2), r.randint(1, 9)
    return N(f"Work out {a} × ({b}) + {c}.", a * b + c, o="O2", d="H", reason=f"Multiply first: {a * b}; then + {c}.")
def m8(r):
    d, n = r.randint(-30, -6), r.randint(2, 3)
    while d % n: d -= 1
    return N(f"A diver goes down to {d} m in {n} equal stages. How far does she go in each stage? (Write down as a negative number.)", d // n, "m", units=["m"], o="O2")


def n1(r):   # missing number with decision
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"Find the missing number: ☐ ÷ {a} = {-b}", -a * b, o="O2", d="H", hint="Undo the division by multiplying.", reason=f"☐ = {-b} × {a} = {-a * b}. Check: {-a * b} ÷ {a} = {-b}.")
def n2(r):   # find all products
    t = -pick(r, [12, 18, 20, 24, 30, 36])
    good = [f"{k} × ({t // k})" for k in r.sample([k for k in range(2, 10) if t % k == 0], 2)]
    bad = [f"{-t // 2} × 2", f"({t // 3 - 1}) × 3"]
    return MS(f"Select ALL the calculations that equal {t}.", good, bad, o="O2", d="H", reason=f"A positive times a negative is negative, and the sizes must multiply to {-t}.")
def n3(r):   # spot the error
    a, b = r.randint(3, 9), r.randint(3, 9)
    return MC(f"Leo writes {a} × ({-b}) = {a * b} because 'two signs make a plus'. What is the right answer?", f"{-a * b}",
              [(f"{a * b}", f"There is only one negative number here. {a} lots of −{b} is a debt."), (f"{a - b}", "That subtracts instead of multiplying."), (f"{-a - b}", "That adds instead of multiplying.")],
              o="O2", d="H", reason=f"{a} × ({-b}) means {a} lots of −{b}, so the answer is −{a * b}.")
def n4(r):   # order the results
    vals = r.sample([(f"3 × (−4)", -12), ("(−20) ÷ 4", -5), ("2 × 3", 6), ("(−18) ÷ 2", -9), ("7 × (−1)", -7), ("(−8) ÷ 8", -1)], 4)
    vals.sort(key=lambda v: v[1])
    return OD("Put these calculations in order of their answers, smallest first.", [v[0] for v in vals], o="O2", d="H", reason="Work out each one: " + ", ".join(f"{v[0]} = {round(v[1])}" for v in vals) + ".")


s.std([m5, m6, m1, m2, m3, m4, m7, m8], EX("Explain why 3 × (−5) = −15.", [("3 lots of −5", ["3 lots|three lots|repeated|add −5|−5 ?\\+ ?−5"]), ("−5 + −5 + −5 = −15", ["−15|-15"])], "3 × (−5) means 3 lots of −5: −5 + (−5) + (−5) = −15.", o="O2"),
      deep=[n1, n2, n3, n4])

# ================================================================== 1.3
s = U.section("1.3", "Lowest common multiples", ["O3"])
s.idea("Multiples", ["The **multiples** of 6 are 6, 12, 18, 24, 30, … (the 6 times table).",
       "A **common multiple** of 4 and 6 is in both lists: 12, 24, 36, … The **lowest common multiple** (LCM) is the smallest: 12."], table={"head": ["Number", "Multiples"], "rows": [["4", "4, 8, 12, 16, 20, 24"], ["6", "6, 12, 18, 24, 30"]]})
s.check(MC("Before you read on: is the LCM of two numbers always the two numbers multiplied together?", "No – sometimes it is smaller",
          [("Yes, always", "4 × 6 = 24, but 12 is already in both times tables."), ("Yes, if both are even", "4 and 6 are both even and their LCM is 12, not 24.")], o="O3", hint="Try 4 and 6."))
s.example("Product or not?", "Find the LCM of 4 and 5, and the LCM of 4 and 6.", [("4, 8, 12, 16, 20 and 5, 10, 15, 20: LCM = 20", "4 and 5 share no factor except 1, so the LCM is 4 × 5"),
          ("4, 8, 12 and 6, 12: LCM = 12", "4 and 6 share the factor 2, so the product 24 counts it twice")], "20 and 12",
          p=["The LCM is the product only when the numbers have no common factor bigger than 1."])
s.check(N("Find the LCM of 8 and 12.", 24, o="O3"))
s.method("Finding the LCM", ["Write the multiples of the larger number: they are the only candidates.", "Stop at the first one the smaller number divides into.", "Check: does each number divide into your answer?"])
s.mistake("Not always the product", ["The LCM of 4 and 6 is 12, not 24. Check the lists."])


def l1(r):
    a, b = r.sample([2, 3, 4, 5, 6, 8, 9, 10, 12, 15], 2)
    return N(f"Find the lowest common multiple of {a} and {b}.", lcm(a, b), o="O3")
def l2(r):
    a, b, c = r.sample([2, 3, 4, 5, 6, 8, 10], 3)
    return N(f"Find the LCM of {a}, {b} and {c}.", lcm(lcm(a, b), c), o="O3", d="H")
def l3(r):
    a, b = r.sample([6, 8, 10, 12, 15], 2)
    return N(f"Hot dogs come in packs of {a} and buns in packs of {b}. What is the smallest number of each you can buy to have the same number of hot dogs and buns?", lcm(a, b), o="O3", d="H")
def l4(r):
    n = r.randint(3, 12)
    return TB(f"Write the first four multiples of {n}.", ["1st", "2nd", "3rd", "4th"], [[B(n), B(2 * n), B(3 * n), B(4 * n)]], o="O3")
def l5(r):
    a, b = r.sample([3, 4, 5, 6, 8], 2); x = lcm(a, b) * r.randint(1, 4)
    return MS(f"Select ALL the common multiples of {a} and {b}.", [str(lcm(a, b)), str(x if x != lcm(a, b) else 2 * x)], [str(a * b + a), str(lcm(a, b) + b)] if (a * b + a) % b and (lcm(a, b) + b) % a else [str(lcm(a, b) + 1), str(lcm(a, b) - 1)], o="O3")
def l6(r):
    a, b = r.sample([5, 6, 8, 10, 12, 15, 20], 2)
    return N(f"Two runners go round a track. One takes {a} minutes a lap and the other {b} minutes. They start together. After how many minutes are they next at the start together?", lcm(a, b), "minutes", units=["minutes"], o="O3", d="H")
def l7(r):
    a, b = r.sample([4, 6, 9, 10, 12], 2)
    return GD(f"Is each number a common multiple of {a} and {b}?", "Common multiple?", [(str(x), "Yes" if x % a == 0 and x % b == 0 else "No") for x in r.sample(range(lcm(a, b), lcm(a, b) * 4), 4)], o="O3", extra=["Yes", "No"])


def p1(r):   # work backwards: LCM × HCF = product
    a, b = pick(r, [(6, 8), (6, 9), (4, 10), (10, 15), (8, 12), (9, 12)])
    return N(f"Two numbers have HCF {gcd(a, b)} and LCM {lcm(a, b)}. One of the numbers is {a}. What is the other?", b, o="O3", d="VH",
             hint=f"The other number must be a factor of {lcm(a, b)} and a multiple of {gcd(a, b)}. Test them.",
             reason=f"Test multiples of {gcd(a, b)} that divide {lcm(a, b)}: only {b} gives HCF {gcd(a, b)} and LCM {lcm(a, b)} with {a}. (Also {a} × {b} = {a * b} = {gcd(a, b)} × {lcm(a, b)}.)")
def p2(r):   # always / sometimes / never
    rows = r.sample([("The LCM of two numbers is bigger than or equal to both numbers", "Always true"), ("The LCM of two numbers is their product", "Sometimes true"),
                     ("The LCM of 2 and an odd number is double the odd number", "Always true"), ("The LCM of two different numbers is one of the numbers", "Sometimes true"),
                     ("The LCM of two numbers is smaller than both", "Never true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O3", d="H", extra=ASN,
              reason="Test pairs such as 4 and 5 (LCM 20 = product), 4 and 6 (LCM 12, not the product) and 3 and 6 (LCM 6, one of the numbers).")
def p3(r):   # three buses: decision
    a, b = r.sample([10, 12, 15, 20], 2); h = r.choice([7, 8])
    L = lcm(a, b)
    return N(f"Two buses leave the station together at {h}:00. One leaves every {a} minutes and the other every {b} minutes. How many minutes after {h}:00 do they next leave together?", L, "minutes", units=["minutes"], o="O3", d="H",
             reason=f"Multiples of {a}: {', '.join(str(a * k) for k in range(1, L // a + 1))}. The first one that {b} divides into is {L}.")
def p4(r):   # spot the error
    a, b = pick(r, [(6, 8), (6, 9), (10, 15), (4, 10), (12, 18)])
    return MC(f"Ravi says the LCM of {a} and {b} is {a * b}. Is he right?", f"No: it is {lcm(a, b)}",
              [(f"Yes: {a * b}", f"{lcm(a, b)} is already a multiple of both, and it is smaller."), (f"No: it is {gcd(a, b)}", "That is the highest common FACTOR."), (f"No: it is {a + b}", "Adding does not give a common multiple.")],
              o="O3", d="H", reason=f"{a} and {b} share the factor {gcd(a, b)}, so the LCM is {a * b} ÷ {gcd(a, b)} = {lcm(a, b)}.")


s.std([l4, l7, l1, l2, l3, l5, l6], EX("Explain how to find the LCM of 6 and 9.", [("list the multiples of each number", ["list|multiples"]), ("the smallest number in both lists is 18", ["18"])], "List the multiples: 6, 12, 18, 24 … and 9, 18, 27 … The smallest number in both lists is 18.", o="O3"),
      deep=[p2, p3, p4, p1])

# ================================================================== 1.4
s = U.section("1.4", "Highest common factors", ["O4"])
s.idea("Factors", ["A **factor** divides exactly into a number. The factors of 18 are 1, 2, 3, 6, 9 and 18 (find them in pairs: 1 × 18, 2 × 9, 3 × 6).",
       "The **highest common factor** (HCF) of two numbers is the biggest number that is a factor of both."], table={"head": ["Number", "Factors"], "rows": [["12", "1, 2, 3, 4, 6, 12"], ["18", "1, 2, 3, 6, 9, 18"]]})
s.idea("Why factors come in pairs", ["If 3 divides into 18, then 18 = 3 × 6, so 6 is a factor too. Every factor has a partner.",
       "That is why you only need to test numbers up to the middle: once the pairs start repeating (6 × 3 after 3 × 6) you have them all."])
s.check(MC("Before you read on: can the HCF of two numbers be bigger than the smaller number?", "No", [("Yes", "A factor of 12 cannot be bigger than 12."), ("Only for even numbers", "No factor of a number is bigger than the number.")], o="O4"))
s.example("When one number divides the other", "Find the HCF of 6 and 18, and the HCF of 8 and 18.", [("6 divides into 18, so HCF(6, 18) = 6", "the smaller number is itself a common factor"),
          ("factors of 8: 1, 2, 4, 8; of 18: 1, 2, 3, 6, 9, 18 → HCF = 2", "8 does not divide 18")], "6 and 2")
s.check(N("Find the HCF of 12 and 18.", 6, o="O4"))
s.method("Finding the HCF", ["List the factors of the smaller number in pairs.", "Start with the biggest and test whether it divides the other number.", "The first one that works is the HCF."])
s.mistake("Factors are not multiples", ["Factors of 12 are 12 or smaller; multiples of 12 are 12 or bigger."])


def h1(r):
    a, b = r.sample([12, 16, 18, 20, 24, 28, 30, 32, 36, 40, 42, 45, 48], 2)
    return N(f"Find the highest common factor of {a} and {b}.", gcd(a, b), o="O4")
def h2(r):
    n = pick(r, [12, 16, 18, 20, 24, 28, 30, 36])
    return N(f"How many factors does {n} have?", sum(1 for k in range(1, n + 1) if n % k == 0), o="O4", reason="List the factor pairs.")
def h3(r):
    a, b = r.sample([24, 30, 36, 40, 42, 48, 60], 2)
    return N(f"A teacher has {a} pencils and {b} rulers. She puts them into identical packs with nothing left over. What is the largest number of packs she can make?", gcd(a, b), "packs", units=["packs"], o="O4", d="H")
def h4(r):
    n = pick(r, [12, 18, 20, 24, 30])
    pairs = [(k, n // k) for k in range(1, int(n ** 0.5) + 1) if n % k == 0][:3]
    return TB(f"Complete the factor pairs of {n}.", ["Factor", "Pair"], [[str(a), B(b)] for a, b in pairs], o="O4")
def h5(r):
    n = pick(r, [24, 30, 36, 40, 48])
    return MS(f"Select ALL the factors of {n}.", [str(k) for k in r.sample([k for k in range(2, n) if n % k == 0], 2)], [str(k) for k in r.sample([k for k in range(5, n) if n % k], 2)], o="O4")
def h6(r):
    a, b, c = r.sample([12, 18, 24, 30, 36, 42], 3)
    return N(f"Find the HCF of {a}, {b} and {c}.", gcd(gcd(a, b), c), o="O4", d="H")
def h7(r):
    a = pick(r, [12, 16, 20, 24]); ns = r.sample(range(2, 25), 5)
    return GD(f"Is each number a factor of {a}?", "Factor?", [(str(x), "Yes" if a % x == 0 else "No") for x in ns], o="O4", extra=["Yes", "No"])


def f1(r):   # HCF or LCM? (decide)
    rows = r.sample([("Cutting two ribbons into equal pieces as long as possible", "HCF"), ("Two lights flashing together again", "LCM"),
                     ("Sharing sweets and apples into identical bags", "HCF"), ("Buying equal numbers of cups and plates sold in packs", "LCM"),
                     ("Tiling a rectangle with the largest equal squares", "HCF"), ("Two runners meeting at the start line", "LCM")], 4)
    return GD("Does each problem need the HCF or the LCM?", "HCF or LCM", rows, o="O4", d="H", extra=["HCF", "LCM"],
              reason="Splitting into the biggest equal groups uses a common FACTOR (HCF). Waiting until things line up again uses a common MULTIPLE (LCM).")
def f2(r):   # find all: numbers with a given HCF with 12
    a = pick(r, [12, 18, 20]); h = pick(r, [k for k in [2, 3, 4, 6] if a % k == 0])
    cand = list(range(h * 2, h * 2 + 30, h))
    good = [str(x) for x in cand if gcd(a, x) == h][:2]; bad = [str(x) for x in cand if gcd(a, x) != h][:2]
    if len(good) < 2 or len(bad) < 1: return None
    return MS(f"Select ALL the numbers whose HCF with {a} is exactly {h}.", good, bad, o="O4", d="VH", reason=f"Work out the HCF of {a} with each number; it must be {h}, not more.")
def f3(r):   # tiling: largest square
    a, b = r.sample([24, 30, 36, 40, 42, 48, 60], 2)
    return N(f"A floor is {a} m by {b} m. It is covered exactly with equal square tiles, as large as possible. How long is each tile?", gcd(a, b), "m", units=["m"], o="O4", d="H",
             fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 5], [0, 5]], "s": [f"{a} m", f"{b} m", "", ""]},
             reason=f"The side must divide both {a} and {b}, and be as big as possible: HCF({a}, {b}) = {gcd(a, b)} m.")
def f4(r):   # spot the error
    a, b = pick(r, [(12, 18), (16, 24), (20, 30), (18, 27)])
    return MC(f"Zoe says the HCF of {a} and {b} is {gcd(a, b) // 2 if gcd(a, b) % 2 == 0 else 3} because it divides both. What is wrong?", f"It is a common factor but not the highest: the HCF is {gcd(a, b)}",
              [("Nothing – she is right", f"{gcd(a, b)} also divides both, and it is bigger."), (f"The HCF is {lcm(a, b)}", "That is the LCM."), ("The HCF is 1", f"{gcd(a, b)} divides both.")],
              o="O4", d="H", reason=f"Common factors of {a} and {b}: " + ", ".join(str(k) for k in range(1, a + 1) if a % k == 0 and b % k == 0) + f". The highest is {gcd(a, b)}.")


s.std([h4, h7, h1, h2, h3, h5, h6], EX("Explain the difference between a factor and a multiple of 8.", [("a factor divides into 8, e.g. 1, 2, 4, 8", ["divides|goes into|1, ?2, ?4"]), ("a multiple is in the 8 times table, e.g. 16, 24", ["times table|16|24|multiply"])], "A factor of 8 divides into 8 exactly (1, 2, 4 and 8). A multiple of 8 is in the 8 times table (8, 16, 24, …).", o="O4"),
      deep=[f1, f3, f4, f2])

# ================================================================== 1.5
s = U.section("1.5", "Tests for divisibility", ["O5"])
s.idea("Quick tests", ["**2**: last digit even. **5**: ends in 0 or 5. **10**: ends in 0. **25**: ends in 00, 25, 50 or 75.",
       "**3**: digit sum divisible by 3. **9**: digit sum divisible by 9. **6**: divisible by 2 and 3.",
       "**4**: last two digits divisible by 4. **8**: last three digits divisible by 8."],
       table={"head": ["Divisor", "Test"], "rows": [["3", "digit sum ÷ 3"], ["4", "last two digits ÷ 4"], ["6", "÷ 2 and ÷ 3"], ["9", "digit sum ÷ 9"]]})
s.idea("Why the digit-sum test works", ["Every 10 is 9 + 1, every 100 is 99 + 1, every 1000 is 999 + 1. The 9s, 99s and 999s always divide by 3 and 9.",
       "So 5427 = 5 × 999 + 4 × 99 + 2 × 9 + (5 + 4 + 2 + 7). Only the digit sum is left to check.",
       "For 4, only the last two digits matter because 100 divides by 4. For 8, the last three, because 1000 divides by 8."])
s.check(MC("Before you read on: 6 divides 12 and 3 divides 12. Does 'divisible by 2 and by 4' mean 'divisible by 8'?", "No", [("Yes", "12 divides by 2 and by 4 but not by 8."), ("Only for even numbers", "12 is even, and it still fails.")], o="O5", hint="Try 12."))
s.example("Digit sum", "Is 5427 divisible by 9?", [("5 + 4 + 2 + 7 = 18", ""), ("18 is divisible by 9", "")], "Yes",
          p=["Compare 5428: the digit sum is 19, which is not divisible by 9, so 5428 is not – changing one digit by 1 breaks it."])
s.check(MC("Which number is divisible by 4?", "3716", [("3714", "14 is not divisible by 4."), ("2310", "10 is not divisible by 4."), ("5122", "22 is not divisible by 4.")], o="O5"))
s.mistake("6 needs both", ["A number is divisible by 6 only if it passes the tests for BOTH 2 and 3."])
DIV = [2, 3, 4, 5, 6, 8, 9, 10, 25]


def d1(r):
    k = pick(r, DIV); n = r.randint(100, 9999)
    return MC(f"Is {n} divisible by {k}?", "Yes" if n % k == 0 else "No", ["No" if n % k == 0 else "Yes", "Only if it is even"], o="O5")
def d2(r):
    k = pick(r, [3, 9]); n = k * r.randint(100, 1000)
    return N(f"Find the digit sum of {n}. ", sum(map(int, str(n))), o="O5", reason="Add the digits.")
def d3(r):
    n = r.randint(1000, 99999)
    return TK(f"Which of these divide exactly into {n}?", ["✓", "✗"], [(str(k), ["✓" if n % k == 0 else "✗"]) for k in r.sample(DIV, 4)], o="O5", d="H")
def d4(r):
    k = pick(r, [3, 9]); base = r.randint(10, 99) * 10
    ans = [d for d in range(10) if (sum(map(int, str(base))) + d) % k == 0][0]
    return N(f"{str(base)[:-1]}☐ is divisible by {k}. What is the smallest digit that can go in the box?", ans, o="O5", d="H")
def d5(r):
    rows = [("Ends in 0 or 5", "5"), ("Digit sum divisible by 9", "9"), ("Last two digits divisible by 4", "4"), ("Even and digit sum divisible by 3", "6"), ("Ends in 00, 25, 50 or 75", "25")]
    return GD("Which number does each test check for?", "Divisible by", r.sample(rows, 4), o="O5", extra=["2", "3"])
def d6(r):
    k = pick(r, [4, 6, 8, 9]); ns = [r.randint(100, 999) for _ in range(3)] + [k * r.randint(20, 120)]
    good = [str(x) for x in ns if x % k == 0]; bad = [str(x) for x in ns if x % k]
    if not bad: return None
    return MS(f"Select ALL the numbers divisible by {k}.", good, bad, o="O5")
def d7(r):
    n = 25 * r.randint(4, 200)
    return N(f"How many groups of 25 are there in {n}?", n // 25, o="O5")


def t1(r):   # find all digits
    k = pick(r, [3, 9, 4, 6]); a, b = r.randint(1, 9), r.randint(0, 9)
    good = [d for d in range(10) if int(f"{a}{b}{d}" if k != 4 else f"{a}{d}{b if b % 2 == 0 else b - 1}") % k == 0]
    if not good: return None
    num = lambda d: f"{a}{b}{d}" if k != 4 else f"{a}{d}{b if b % 2 == 0 else b - 1}"
    shape = f"{a}{b}☐" if k != 4 else f"{a}☐{b if b % 2 == 0 else b - 1}"
    return N(f"{shape} is divisible by {k}. How many different digits (0–9) could go in the box?", len(good), o="O5", d="VH",
             hint="Test each digit from 0 to 9 with the quick test.", reason=f"The digits that work are {', '.join(map(str, good))}: " + ", ".join(num(d) for d in good) + ".")
def t2(r):   # always / sometimes / never
    rows = r.sample([("A number divisible by 9 is divisible by 3", "Always true"), ("A number divisible by 3 is divisible by 9", "Sometimes true"),
                     ("An odd number is divisible by 4", "Never true"), ("A number ending in 5 is divisible by 25", "Sometimes true"),
                     ("A number divisible by 2 and 3 is divisible by 6", "Always true"), ("A number divisible by 2 and 4 is divisible by 8", "Sometimes true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O5", d="H", extra=ASN,
              reason="9 = 3 × 3, so anything divisible by 9 is divisible by 3, but 6 is divisible by 3 and not 9. 12 is divisible by 2 and 4 but not by 8.")
def t3(r):   # spot the error
    n = pick(r, [124, 316, 532, 748, 1012])
    return MC(f"Jo says {n} is divisible by 8 because its last two digits, {n % 100}, are divisible by 4… and 4 × 2 = 8. Is she right?", "No – for 8 you must test the last three digits",
              [("Yes", f"{n} ÷ 8 = {n / 8} – not a whole number."), ("No – 8 needs the digit sum", "The digit sum tests 3 and 9.")],
              o="O5", d="H", reason=f"The test for 8 uses the last three digits: {n % 1000} ÷ 8 = {n % 1000 / 8}, which is not whole, so {n} is not divisible by 8.")
def t4(r):   # sharing with no remainder (decision)
    n = pick(r, [216, 324, 420, 540, 630, 756, 840, 945])
    ks = [k for k in [4, 5, 6, 8, 9] if n % k == 0]; nk = [k for k in [4, 5, 6, 8, 9] if n % k]
    if not ks or not nk: return None
    return MS(f"{n} stickers are shared equally with none left over. Select ALL the group sizes that work.", [str(k) for k in ks][:3], [str(k) for k in nk][:2], o="O5", d="H",
              reason=f"Use the tests: digit sum {sum(map(int, str(n)))}; last two digits {n % 100}; last digit {n % 10}.")


s.std([d5, d3, d1, d2, d4, d6, d7], EX("Explain how to check if 7362 is divisible by 6.", [("it is even, so divisible by 2", ["even|ends in 2|divisible by 2"]), ("digit sum 18 is divisible by 3", ["18|digit sum|divisible by 3"])], "7362 is even, so it is divisible by 2. Its digit sum is 7 + 3 + 6 + 2 = 18, which is divisible by 3. Divisible by 2 and 3 means divisible by 6.", o="O5"),
      deep=[t2, t3, t4, t1])

# ================================================================== 1.6
s = U.section("1.6", "Square roots and cube roots", ["O6"])
s.idea("Squares and cubes", ["A **square number** is a number times itself: 7² = 49. A **cube number** is a number used three times: 4³ = 4 × 4 × 4 = 64.",
       "The **square root** undoes squaring: √49 = 7. The **cube root** undoes cubing: ∛64 = 4."], table={"head": ["n", "1", "2", "3", "4", "5"], "rows": [["n²", "1", "4", "9", "16", "25"], ["n³", "1", "8", "27", "64", "125"]]})
s.idea("Squares are areas, cubes are volumes", ["A square with side 7 cm has area 7 × 7 = 49 cm². That is why 7² is called '7 squared'. The square root asks: which side gives this area?",
       "A cube with edge 4 cm has volume 4 × 4 × 4 = 64 cm³. The cube root asks: which edge gives this volume?"],
       fig={"kind": "shape", "pts": [[0, 0], [6, 0], [6, 6], [0, 6]], "s": ["7 cm", "7 cm", "", ""]})
s.check(MC("Before you read on: which is bigger, 2³ or 3²?", "3² = 9", [("2³ = 8", "2³ = 2 × 2 × 2 = 8, and 3² = 3 × 3 = 9."), ("They are equal", "Work them out: 8 and 9.")], o="O6"))
s.example("Estimate a root", "Between which two whole numbers is √50?", [("7² = 49 and 8² = 64", "find the squares either side of 50"), ("49 < 50 < 64", "so √50 is between 7 and 8, very close to 7")], "7 and 8")
s.check(N("Find √144.", 12, o="O6"))
s.mistake("Not times 2", ["5² is 5 × 5 = 25, not 5 × 2 = 10."])


def q1(r):
    n = r.randint(2, 20)
    return N(f"Work out {n}².", n * n, o="O6")
def q2(r):
    n = r.randint(2, 20)
    return N(f"Find √{n * n}.", n, o="O6")
def q3(r):
    n = r.randint(2, 5)
    return N(f"Find ∛{n ** 3}.", n, o="O6")
def q4(r):
    n = r.randint(2, 5)
    return N(f"Work out {n}³.", n ** 3, o="O6")
def q5(r):
    ns = r.sample(range(2, 16), 3)
    return TB("Complete the table.", ["n", "n²"], [[str(n), B(n * n)] for n in ns], o="O6")
def q6(r):
    vals = r.sample([1, 4, 8, 9, 16, 25, 27, 36, 49, 64, 81, 100, 125, 10, 20, 50, 30], 5)
    sq = lambda v: int(v ** 0.5 + 0.5) ** 2 == v; cu = lambda v: round(v ** (1 / 3)) ** 3 == v
    return GD("Is each a square number, a cube number, both or neither?", "Type", [(str(v), "Both" if sq(v) and cu(v) else "Square" if sq(v) else "Cube" if cu(v) else "Neither") for v in vals], o="O6", extra=["Square", "Cube", "Both", "Neither"], d="H")
def q7(r):
    a = r.randint(4, 15)
    return N(f"A square tablecloth has an area of {a * a} m². How long is each side?", a, "m", units=["m"], o="O6")
def q8(r):
    a, b = r.randint(2, 10), r.randint(2, 4)
    return N(f"Work out {a}² + {b}³.", a * a + b ** 3, o="O6", d="H")


def r1(r):   # estimate between
    n = r.randint(5, 18); v = n * n + r.randint(1, 2 * n)
    return N(f"√{v} is between two whole numbers. What is the smaller one?", n, o="O6", d="H", hint="Find the square numbers either side.", reason=f"{n}² = {n * n} and {n + 1}² = {(n + 1) ** 2}; {v} is between them.")
def r2(r):   # spot the error
    n = r.randint(3, 9)
    return MC(f"Kai says {n}³ = {3 * n}. What is the right answer?", str(n ** 3), [(str(3 * n), f"That is 3 × {n}. Cubing means {n} × {n} × {n}."), (str(n * n), f"That is {n}², only two {n}s."), (str(n + 3), "That adds 3.")], o="O6", d="H",
              reason=f"{n}³ = {n} × {n} × {n} = {n ** 3}.")
def r3(r):   # find all
    lo, hi = pick(r, [(10, 70), (20, 110), (30, 130)])
    sq = [str(k * k) for k in range(1, 12) if lo <= k * k <= hi]
    no = [str(x) for x in r.sample([x for x in range(lo, hi) if int(x ** 0.5) ** 2 != x], 2)]
    return MS(f"Select ALL the square numbers between {lo} and {hi}.", sq[:4], no, o="O6", d="H", reason="Square numbers: " + ", ".join(sq) + ".")
def r4(r):   # work backwards with a cube
    n = r.randint(2, 5)
    return N(f"A cube-shaped box holds exactly {n ** 3} small cubes of side 1 cm. How long is each edge of the box?", n, "cm", units=["cm"], o="O6", d="H",
             fig={"kind": "solid", "solid": "cuboid", "a": "? cm", "b": "? cm", "c": "? cm"}, reason=f"Volume = edge³, so the edge is ∛{n ** 3} = {n} cm.")
def r5(r):   # always / sometimes / never
    rows = r.sample([("A square number is even", "Sometimes true"), ("The square of an odd number is odd", "Always true"), ("A square number ends in 7", "Never true"),
                     ("√n is smaller than n (n a whole number bigger than 1)", "Always true"), ("A cube number is a square number", "Sometimes true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O6", d="H", extra=ASN,
              reason="Check the last digits of 1², 2², … 9²: 1, 4, 9, 6, 5, 6, 9, 4, 1 – never 7. 64 is both a cube and a square, but 8 is only a cube.")


s.std([q5, q6, q1, q2, q3, q4, q7, q8], EX("Explain why 64 is both a square number and a cube number.", [("8 × 8 = 64", ["8 ?× ?8|8²"]), ("4 × 4 × 4 = 64", ["4 ?× ?4 ?× ?4|4³"])], "64 = 8 × 8, so it is a square number, and 64 = 4 × 4 × 4, so it is also a cube number.", o="O6"),
      deep=[r1, r2, r3, r4, r5])

U.mindmap(("Adding and subtracting", "Number line • + (−) = − • − (−) = +", "O1", "1.1"), ("Multiplying and dividing", "Positive × negative = negative", "O2", "1.2"),
          ("LCM", "Smallest number in both times tables", "O3", "1.3"), ("HCF", "Biggest factor of both", "O4", "1.4"),
          ("Divisibility tests", "3 and 9: digit sum • 4: last two digits • 6: 2 and 3", "O5", "1.5"), ("Roots", "√ undoes squaring • ∛ undoes cubing", "O6", "1.6"))
