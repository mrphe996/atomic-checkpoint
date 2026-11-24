# -*- coding: utf-8 -*-
"""Stage 6 Mathematics (Primary) · Unit 2 Numbers and sequences (2.1 Counting and sequences, 2.2 Special numbers,
2.3 Common multiples and factors). Written by the Atomic teaching team."""
from math import gcd
from kit import *

U = Unit(2, "Numbers and Sequences", "Number",
         "Counting on and back in steps, linear sequences and their rules, square and cube numbers, prime numbers, and common multiples and factors.",
         {"O1": {"code": "6Ns.01", "sec": "2.1", "codeNote": "", "t": "Count on and back in steps of constant size, including decimals and negative numbers, and continue sequences."},
          "O2": {"code": "6Ns.02", "sec": "2.2", "codeNote": "", "t": "Recognise square numbers, cube numbers and prime numbers."},
          "O3": {"code": "6Ns.03", "sec": "2.3", "codeNote": "", "t": "Find common multiples and common factors of two numbers."}})
PR = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
lcm = lambda a, b: a * b // gcd(a, b)

# ================================================================== 2.1
s = U.section("2.1", "Counting and sequences", ["O1"])
s.idea("Sequences", ["A **sequence** is a list of numbers that follow a rule. 3, 7, 11, 15, … starts at 3 and the **term-to-term rule** is 'add 4'.",
       "You can count in decimals (0.2, 0.4, 0.6, …) and below zero (5, 2, −1, −4, …)."], fig={"kind": "numline", "min": -4, "max": 6})
s.check(N("What is the next number in the sequence 4, 9, 14, 19, …?", 24, o="O1"))
s.idea("Position", ["The **position-to-term rule** links a term to its position: for 3, 6, 9, 12, … the term is 3 × the position, so the 10th term is 30."])
s.mistake("Going below zero", ["Counting back 3 from 1 gives −2, not 2."])


def c1(r):
    a, d = r.randint(1, 30), r.randint(2, 12); t = [a + i * d for i in range(5)]
    return N(f"What is the next number in the sequence {', '.join(map(str, t[:4]))}, …?", t[4], o="O1")
def c2(r):
    a, d = r.randint(5, 15), r.randint(2, 6); t = [a - i * d for i in range(5)]
    return N(f"Continue the sequence: {', '.join(map(str, t[:4]))}, …", t[4], o="O1", fig={"kind": "numline", "min": min(t) - 1, "max": a + 1} if a - min(t) <= 14 else None)
def c3(r):
    a, d = r.randint(1, 9) / 10, pick(r, [0.1, 0.2, 0.3, 0.5]); t = [round(a + i * d, 1) for i in range(5)]
    return N(f"Continue the sequence: {', '.join(fmt(x) for x in t[:4])}, …", t[4], o="O1")
def c4(r):
    a, d = r.randint(1, 20), r.randint(2, 9); t = [a + i * d for i in range(6)]; k = r.randint(1, 4)
    return N(f"Find the missing number: {', '.join(str(x) if i != k else '☐' for i, x in enumerate(t))}", t[k], o="O1")
def c5(r):
    a, d = r.randint(1, 20), r.randint(2, 9); t = [a + i * d for i in range(4)]
    return S(f"Write the term-to-term rule for {', '.join(map(str, t))}, …", [f"add {d}", f"+{d}", f"+ {d}", f"plus {d}", f"count on {d}", f"goes up by {d}"], o="O1")
def c6(r):
    m = r.randint(2, 9)
    return TB(f"The term is {m} × the position. Complete the table.", ["Position", "Term"], [["1", B(m)], ["5", B(5 * m)], ["10", B(10 * m)]], o="O1")
def c7(r):
    m, k = r.randint(2, 9), r.randint(12, 50)
    return N(f"The sequence {m}, {2 * m}, {3 * m}, {4 * m}, … continues. What is the {k}th term?", m * k, o="O1", d="H")
def c8(r):
    a, d = r.randint(3, 6), r.randint(2, 4); t = [a + i * d for i in range(3)]
    return N(f"Pattern 1 has {t[0]} dots, pattern 2 has {t[1]} and pattern 3 has {t[2]}. How many dots are in pattern 6?", a + 5 * d, "dots", units=["dots"], o="O1", data={"head": ["Pattern", "1", "2", "3"], "rows": [["Dots", *map(str, t)]]})


s.std([c6, c8, c1, c2, c3, c4, c5, c7], EX("Explain how to find the 10th term of 5, 10, 15, 20, …", [("each term is 5 times its position", ["5 times|× ?5|position"]), ("10 × 5 = 50", ["50"])], "Each term is 5 times its position (1st is 5, 2nd is 10). So the 10th term is 10 × 5 = 50.", o="O1"))

# ================================================================== 2.2
s = U.section("2.2", "Special numbers", ["O2"])
s.idea("Squares, cubes and primes", ["A **square number** is a number times itself: 6 × 6 = 6² = 36. A **cube number** is a number used three times: 2 × 2 × 2 = 2³ = 8.",
       "A **prime number** has exactly two factors, 1 and itself: 2, 3, 5, 7, 11, 13, … 1 is not prime."],
       table={"head": ["n", "1", "2", "3", "4", "5"], "rows": [["n²", "1", "4", "9", "16", "25"], ["n³", "1", "8", "27", "64", "125"]]})
s.check(MC("Which number is prime?", "29", [("27", "27 = 3 × 9"), ("21", "21 = 3 × 7"), ("25", "25 = 5 × 5")], o="O2"))
s.mistake("2 is prime", ["2 is the only even prime number."])


def q1(r):
    n = r.randint(2, 12)
    return N(f"Work out {n}².", n * n, o="O2")
def q2(r):
    n = r.randint(1, 5)
    return N(f"Work out {n}³.", n ** 3, o="O2")
def q3(r):
    ns = r.sample(range(2, 60), 5)
    return GD("Is each number prime?", "Prime?", [(str(n), "Prime" if n in PR else "Not prime") for n in ns], o="O2", extra=["Prime", "Not prime"])
def q4(r):
    vals = r.sample([1, 4, 8, 9, 16, 25, 27, 36, 49, 64, 81, 100, 125, 10, 20, 50, 12], 5)
    sq = lambda v: int(v ** 0.5 + 0.5) ** 2 == v; cu = lambda v: round(v ** (1 / 3)) ** 3 == v
    return GD("Is each a square number, a cube number, both or neither?", "Type", [(str(v), "Both" if sq(v) and cu(v) else "Square" if sq(v) else "Cube" if cu(v) else "Neither") for v in vals], o="O2", extra=["Square", "Cube", "Both", "Neither"], d="H")
def q5(r):
    lo = r.randint(10, 80)
    ps = [p for p in PR if lo < p < lo + 10]
    if not ps: return None
    return N(f"Write the smallest prime number between {lo} and {lo + 10}.", ps[0], o="O2")
def q6(r):
    ns = r.sample(range(2, 11), 3)
    return TB("Complete the table.", ["n", "n²"], [[str(n), B(n * n)] for n in ns], o="O2")
def q7(r):
    n = r.randint(4, 10)
    return N(f"A square patio has {n * n} square tiles. How many tiles are along each side?", n, "tiles", units=["tiles"], o="O2")
def q8(r):
    a = r.randint(2, 6)
    return N(f"Work out {a}² + {a}³.", a * a + a ** 3, o="O2", d="H")


s.std([q3, q6, q1, q2, q5, q7, q4, q8], EX("Explain why 9 is not a prime number.", [("9 has the factor 3 (3 × 3 = 9)", ["3|three"]), ("a prime has only two factors, 1 and itself", ["two factors|only 1 and|only factors"])], "A prime number has exactly two factors, 1 and itself. 9 has three factors: 1, 3 and 9 (because 3 × 3 = 9), so it is not prime.", o="O2"))

# ================================================================== 2.3
s = U.section("2.3", "Common multiples and factors", ["O3"])
s.idea("Multiples and factors", ["**Multiples** of 4 are in the 4 times table: 4, 8, 12, 16, … A **common multiple** of 4 and 6 is in both lists: 12, 24, …",
       "**Factors** of 12 divide into 12 exactly: 1, 2, 3, 4, 6, 12. A **common factor** of 12 and 18 divides into both: 1, 2, 3, 6."],
       table={"head": ["Number", "Factors"], "rows": [["12", "1, 2, 3, 4, 6, 12"], ["18", "1, 2, 3, 6, 9, 18"]]})
s.check(N("What is the biggest common factor of 12 and 18?", 6, o="O3"))
s.mistake("Factors and multiples", ["Factors of a number are smaller than or equal to it; multiples are bigger than or equal to it."])


def m1(r):
    a, b = r.sample([2, 3, 4, 5, 6, 8, 9, 10], 2)
    return N(f"What is the smallest common multiple of {a} and {b}?", lcm(a, b), o="O3")
def m2(r):
    a, b = r.sample([12, 16, 18, 20, 24, 30, 36, 40], 2)
    return N(f"What is the biggest common factor of {a} and {b}?", gcd(a, b), o="O3")
def m3(r):
    n = pick(r, [12, 18, 20, 24, 30, 36])
    return MS(f"Select ALL the factors of {n}.", [str(k) for k in r.sample([k for k in range(2, n) if n % k == 0], 2)], [str(k) for k in r.sample([k for k in range(5, n) if n % k], 2)], o="O3")
def m4(r):
    a, b = r.sample([3, 4, 5, 6], 2)
    return GD(f"Is each number a common multiple of {a} and {b}?", "Common multiple?", [(str(x), "Yes" if x % a == 0 and x % b == 0 else "No") for x in r.sample(range(lcm(a, b), lcm(a, b) * 4), 4)], o="O3", extra=["Yes", "No"])
def m5(r):
    n = pick(r, [12, 18, 20, 24, 30])
    pairs = [(k, n // k) for k in range(1, int(n ** 0.5) + 1) if n % k == 0][:3]
    return TB(f"Complete the factor pairs of {n}.", ["Factor", "Pair"], [[str(a), B(b)] for a, b in pairs], o="O3")
def m6(r):
    a, b = r.sample([4, 5, 6, 8, 10], 2)
    return N(f"Two lights flash every {a} and every {b} seconds. They flash together now. After how many seconds do they next flash together?", lcm(a, b), "seconds", units=["seconds"], o="O3", d="H")
def m7(r):
    a, b = r.sample([12, 18, 24, 30], 2)
    return N(f"{a} apples and {b} oranges are put into identical bags with none left over. What is the greatest number of bags?", gcd(a, b), "bags", units=["bags"], o="O3", d="H")
def m8(r):
    n = r.randint(3, 9)
    return TB(f"Write the first four multiples of {n}.", ["1st", "2nd", "3rd", "4th"], [[B(n), B(2 * n), B(3 * n), B(4 * n)]], o="O3")


s.std([m4, m5, m1, m2, m3, m8, m6, m7], EX("Explain the difference between a factor and a multiple of 6.", [("a factor divides into 6: 1, 2, 3, 6", ["divides|1, ?2, ?3"]), ("a multiple is in the 6 times table: 12, 18", ["times table|12|18"])], "A factor of 6 divides into 6 exactly (1, 2, 3, 6). A multiple of 6 is in the 6 times table (6, 12, 18, …).", o="O3"))

U.mindmap(("Sequences", "Term-to-term rule • position-to-term rule", "O1", "2.1"), ("Special numbers", "Squares • cubes • primes", "O2", "2.2"),
          ("Multiples and factors", "Common multiples • common factors", "O3", "2.3"))
