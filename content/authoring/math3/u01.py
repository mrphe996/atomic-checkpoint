# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 1 Numbers to 1000 (1.1 Hundreds, tens and ones, 1.2 Comparing and ordering,
1.3 Estimating and rounding). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(1, "Numbers to 1000", "Number",
         "Reading, writing and making 3-digit numbers, comparing and ordering them, and rounding to the nearest 10 and 100.",
         {"O1": {"code": "3Np.01", "sec": "1.1", "codeNote": "", "t": "Understand the value of each digit in a 3-digit number: hundreds, tens and ones."},
          "O2": {"code": "3Np.02", "sec": "1.2", "codeNote": "", "t": "Compare and order numbers up to 1000 using the symbols <, > and =."},
          "O3": {"code": "3Np.03", "sec": "1.3", "codeNote": "", "t": "Estimate and round 3-digit numbers to the nearest 10 or 100."}})
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def words(n):
    h, r = divmod(n, 100); t = ""
    if r: t = ONES[r] if r < 20 else TENS[r // 10] + ("-" + ONES[r % 10] if r % 10 else "")
    if not h: return t
    return f"{ONES[h]} hundred" + (f" and {t}" if t else "")


s = U.section("1.1", "Hundreds, tens and ones", ["O1"])
s.idea("Three places", ["A 3-digit number has **hundreds**, **tens** and **ones**. In **472** there are 4 hundreds, 7 tens and 2 ones.",
       "472 = 400 + 70 + 2. The 7 is worth 70."], table={"head": ["Hundreds", "Tens", "Ones"], "rows": [["4", "7", "2"]]})
s.check(N("What is the value of the digit 5 in 356?", 50, o="O1"))
s.check(MC('Before you read on: what does the 5 in 352 mean?', '5 tens (50)', [('5 ones', 'The 5 is in the tens place.'), ('5 hundreds', 'The 3 is in the hundreds place.')], o='O1'))
s.mistake("Zero holds a place", ["In 405 there are no tens. The 0 keeps the 5 in the ones place."])


def p1(r):
    n = r.randint(100, 999); d = str(n); k = r.randrange(3)
    if d.count(d[k]) > 1 or d[k] == "0": return None
    return N(f"What is the value of the digit {d[k]} in {n}?", int(d[k]) * 10 ** (2 - k), o="O1")
def p2(r):
    n = r.randint(100, 999)
    return TB(f"Write {n} in the place value table.", ["Hundreds", "Tens", "Ones"], [[B(n // 100), B(n // 10 % 10), B(n % 10)]], o="O1")
def p3(r):
    h, t, o = r.randint(1, 9), r.randint(0, 9), r.randint(0, 9)
    return N(f"What number is {h} hundreds, {t} tens and {o} ones?", 100 * h + 10 * t + o, o="O1", data={"head": ["Hundreds", "Tens", "Ones"], "rows": [[str(h), str(t), str(o)]]})
def p4(r):
    n = r.randint(100, 999)
    return N(f"Write this number in digits: {words(n)}.", n, o="O1")
def p5(r):
    n = r.randint(100, 999)
    return N(f"Find the missing number: {n} = {n // 100 * 100} + ☐ + {n % 10}", n // 10 % 10 * 10, o="O1")
def p6(r):
    n = r.randint(100, 989); k = pick(r, [1, 10, 100])
    if n + k > 999: return None
    return N(f"What is {k} more than {n}?", n + k, o="O1")
def p7(r):
    n = r.randint(110, 999); k = pick(r, [1, 10, 100])
    return N(f"What is {k} less than {n}?", n - k, o="O1")
def p8(r):
    a = r.randint(10, 96) * 10
    return N(f"Count on in tens: {a}, {a + 10}, {a + 20}, ☐", a + 30, o="O1")
def p9(r):
    h, o = r.randint(1, 9), r.randint(1, 9)
    return N(f"Write the number with {h} hundreds, no tens and {o} ones.", 100 * h + o, o="O1", d="H")


s.std([p2, p3, p1, p4, p5, p6, p7, p8, p9], EX("Explain what the 3 is worth in 238.", [("the 3 is in the tens place", "tens"), ("it is worth 30", "30|thirty")], "In 238 the 3 is in the tens place, so it is worth 3 tens, which is 30.", o="O1"))

s = U.section("1.2", "Comparing and ordering", ["O2"])
s.idea("Which is bigger?", ["To compare, look at the **hundreds** first. If they are the same, look at the **tens**, then the **ones**.",
       "**<** means 'is less than' and **>** means 'is greater than': 345 < 354."], fig={"kind": "numline", "min": 0, "max": 10, "ticks": [[3.45, "345"], [3.54, "354"]]})
s.check(CMP("629", "692", "<", o="O2"))
s.check(MC('Before you read on: which is bigger, 409 or 490?', '490', [('409', 'Compare the tens: 9 tens beat 0 tens.'), ('They are equal', 'The digits are in different places.')], o='O2'))
s.mistake("The mouth eats the bigger number", ["The open side of < or > always faces the bigger number."])


def c1(r):
    a, b = r.sample(range(100, 999), 2)
    return CMP(str(a), str(b), "<" if a < b else ">", o="O2")
def c2(r):
    h = r.randint(1, 9); a, b = r.sample(range(0, 99), 2)
    return CMP(str(h * 100 + a), str(h * 100 + b), "<" if a < b else ">", o="O2")
def c3(r):
    xs = r.sample(range(100, 999), 4)
    return OD("Put these numbers in order, smallest first.", [str(x) for x in sorted(xs)], o="O2")
def c4(r):
    xs = r.sample(range(100, 999), 4)
    return N(f"Which is the largest number: {', '.join(map(str, xs))}?", max(xs), o="O2")
def c5(r):
    ds = r.sample(range(1, 10), 3)
    return N(f"Use the digits {', '.join(map(str, ds))} once each. What is the largest number you can make?", int("".join(map(str, sorted(ds, reverse=True)))), o="O2", d="H")
def c6(r):
    ds = r.sample(range(1, 10), 3)
    return N(f"Use the digits {', '.join(map(str, ds))} once each. What is the smallest number you can make?", int("".join(map(str, sorted(ds)))), o="O2", d="H")
def c7(r):
    a = r.randint(100, 900)
    return MS(f"Select ALL the numbers greater than {a}.", [str(a + r.randint(1, 99)), str(a + 100)], [str(a - r.randint(1, 99)), str(a)], o="O2")
def c8(r):
    a, b = r.sample(range(100, 999), 2)
    return GD("Is each statement true or false?", "True?", [(f"{a} < {b}", "true" if a < b else "false"), (f"{a} > {b}", "true" if a > b else "false"), (f"{a} = {a}", "true")], o="O2", extra=["true", "false"])
def c9(r):
    n = r.randint(1, 8) * 100
    return N(f"Which hundred comes next: {n}, {n + 100}, ☐?", n + 200, o="O2", fig={"kind": "numline", "min": 0, "max": 10, "ticks": [[n / 100, str(n)], [n / 100 + 1, str(n + 100)]], "mark": n / 100 + 2})


def a12(r):
    return MC('Sam says 98 is bigger than 102 because 9 is bigger than 1. Is he right?', 'No: 102 is bigger', [('Yes', '102 has a hundred; 98 does not.'), ('They are equal', 'They are different numbers.')], o='O2', d="H", reason='102 has 1 hundred; 98 has no hundreds, so 102 is bigger.')


s.std([c8, c9, c1, c2, c3, c4, c7, c5, c6], EX("Explain why 512 is greater than 498.", [("compare the hundreds first", "hundreds"), ("5 hundreds is more than 4 hundreds", "5 ?> ?4|more|bigger")], "Compare the hundreds first. 512 has 5 hundreds and 498 has only 4 hundreds, so 512 is greater.", o="O2"),
      deep=[a12])

s = U.section("1.3", "Estimating and rounding", ["O3"])
s.idea("Nearest 10 and 100", ["To round to the nearest **10**, look at the **ones** digit. 5 or more rounds up; less than 5 rounds down. 347 → **350**.",
       "To round to the nearest **100**, look at the **tens** digit. 347 → **300**."], fig={"kind": "numline", "min": 34, "max": 35, "minor": 10, "ticks": [], "mark": 34.7})
s.check(N("Round 68 to the nearest 10.", 70, o="O3"))
s.check(MC('Before you read on: round 65 to the nearest ten.', '70', [('60', '5 rounds up.'), ('65', 'The nearest ten ends in 0.')], o='O3'))
s.mistake("Halfway rounds up", ["45 is exactly halfway between 40 and 50. We round it up to 50."])


def r1(r):
    n = r.randint(11, 999)
    if n % 10 == 0: return None
    return N(f"Round {n} to the nearest 10.", (n + 5) // 10 * 10, o="O3")
def r2(r):
    n = r.randint(101, 949)
    if n % 100 == 0: return None
    return N(f"Round {n} to the nearest 100.", (n + 50) // 100 * 100, o="O3")
def r3(r):
    t = r.randint(10, 98); o = r.randint(1, 9); v = t * 10 + o
    return N("The arrow points to a number. Round it to the nearest 10.", (v + 5) // 10 * 10, o="O3", fig={"kind": "numline", "min": t, "max": t + 1, "minor": 10, "ticks": [], "mark": v / 10})
def r4(r):
    ns = r.sample(range(101, 999), 3)
    return TB("Round each number.", ["Number", "Nearest 10", "Nearest 100"], [[str(n), B((n + 5) // 10 * 10), B((n + 50) // 100 * 100)] for n in ns], o="O3")
def r5(r):
    a, b = r.randint(110, 480), r.randint(110, 480)
    e = (a + 50) // 100 * 100 + (b + 50) // 100 * 100
    return MC(f"Which is the best estimate for {a} + {b}?", str(e), [str(e + 100), str(e - 100), str(e * 10)], o="O3")
def r6(r):
    t = r.randint(2, 9) * 10
    return MS(f"Select ALL the numbers that round to {t} (nearest 10).", [str(t - 3), str(t + 4), str(t - 5)], [str(t + 5), str(t - 6), str(t + 9)], o="O3", d="H")
def r7(r):
    n = r.randint(101, 999)
    return N(f"A school has {n} children. About how many is that to the nearest 100?", (n + 50) // 100 * 100, "children", units=["children"], o="O3")
def r8(r):
    t = r.randint(2, 9) * 100
    return N(f"What is the smallest whole number that rounds to {t} to the nearest 100?", t - 50, o="O3", d="H")


s.std([r3, r4, r1, r2, r5, r7, r6, r8], EX("Explain how to round 263 to the nearest 100.", [("look at the tens digit, 6", "tens|the 6"), ("6 is 5 or more, so round up to 300", "300|round up")], "Look at the tens digit, 6. It is 5 or more, so round up: 263 rounds to 300.", o="O3"))

U.mindmap(("Place value", "Hundreds • tens • ones", "O1", "1.1"), ("Comparing", "< and > • order numbers", "O2", "1.2"), ("Rounding", "Nearest 10 and 100", "O3", "1.3"))
