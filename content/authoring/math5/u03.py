# -*- coding: utf-8 -*-
"""Stage 5 Mathematics (Primary) · Unit 3 Numbers and sequences (3.1 Counting and sequences, 3.2 Square and triangular numbers,
3.3 Prime and composite numbers). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(3, "Numbers and Sequences", "Number",
         "Counting on and back in steps, including through zero, linear sequences, square and triangular numbers, and prime and composite numbers.",
         {"O1": {"code": "5Ns.01", "sec": "3.1", "codeNote": "", "t": "Count on and back in steps of constant size, including through zero, and continue linear sequences."},
          "O2": {"code": "5Ns.02", "sec": "3.2", "codeNote": "", "t": "Recognise and use square numbers and triangular numbers."},
          "O3": {"code": "5Ns.03", "sec": "3.3", "codeNote": "", "t": "Recognise prime and composite numbers and find factors of numbers up to 100."}})
PR = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
TRIS = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

s = U.section("3.1", "Counting and sequences", ["O1"])
s.idea("Steps of the same size", ["A **linear sequence** goes up or down by the same amount each time. 50, 42, 34, 26, … counts back in **eights**.",
       "You can count back past zero: 9, 5, 1, −3, −7, …"], fig=NL(-8, 10))
s.check(N("What is the next number: 45, 38, 31, 24, …?", 17, o="O1"))
s.check(MC('Before you read on: the sequence is 4, 7, 10, 13, … What is the next term?', '16', [('17', 'The rule is add 3.'), ('15', '13 + 3 = 16.')], o='O1'))
s.mistake("Through zero", ["Counting back 4 from 2 gives −2."])


def c1(r):
    a, d = r.randint(1, 50), r.randint(3, 25); t = [a + i * d for i in range(5)]
    return N(f"What is the next number in the sequence {', '.join(map(str, t[:4]))}, …?", t[4], o="O1")
def c2(r):
    a, d = r.randint(4, 12), r.randint(2, 5); t = [a - i * d for i in range(5)]
    return N(f"Continue the sequence: {', '.join(sg(x) for x in t[:4])}, …", t[4], o="O1", fig=NL(min(t) - 1, a + 1) if a - min(t) < 16 else None)
def c3(r):
    a, d = r.randint(1, 20), r.randint(2, 9); t = [a + i * d for i in range(6)]; k = r.randint(1, 4)
    return N(f"Find the missing number: {', '.join(str(x) if i != k else '☐' for i, x in enumerate(t))}", t[k], o="O1")
def c4(r):
    a, d = r.randint(2, 6), r.randint(2, 4); t = [a + i * d for i in range(3)]
    return N(f"Pattern 1 has {t[0]} sticks, pattern 2 has {t[1]} and pattern 3 has {t[2]}. How many sticks are in pattern 5?", a + 4 * d, "sticks", units=["sticks"], o="O1", data={"head": ["Pattern", "1", "2", "3"], "rows": [["Sticks", *map(str, t)]]})
def c5(r):
    a, d = r.randint(1, 20), r.randint(2, 9); t = [a + i * d for i in range(4)]
    return S(f"Write the term-to-term rule for {', '.join(map(str, t))}, …", [f"add {d}", f"+{d}", f"+ {d}", f"plus {d}", f"count on {d}", f"goes up by {d}", f"add {d} each time"], o="O1")
def c6(r):
    a, d = r.randint(1, 9), r.randint(2, 6)
    return TB(f"A sequence starts at {a} and the rule is 'add {d}'. Complete it.", ["1st", "2nd", "3rd", "4th"], [[str(a), B(a + d), B(a + 2 * d), B(a + 3 * d)]], o="O1")
def c7(r):
    a, d = r.randint(1, 9), r.randint(3, 9); lim = r.randint(60, 150)
    n = next(i for i in range(200) if a + i * d > lim)
    return N(f"A sequence starts {a}, {a + d}, {a + 2 * d}, … What is the first term greater than {lim}?", a + n * d, o="O1", d="H")
def c8(r):
    a, d = r.randint(2, 8), r.randint(2, 6)
    return N(f"A sequence starts at {a} and adds {d} each time. What is the 10th term?", a + 9 * d, o="O1", d="H")


s.std([c4, c6, c1, c2, c3, c5, c7, c8], EX("Explain how to find the next term of 3, 7, 11, 15, …", [("the rule is add 4", "add 4|\\+ ?4|4 more|goes up by 4"), ("15 + 4 = 19", "19")], "The numbers go up by 4 each time, so the rule is 'add 4'. The next term is 15 + 4 = 19.", o="O1"))

s = U.section("3.2", "Square and triangular numbers", ["O2"])
s.idea("Square numbers", ["A **square number** is made by multiplying a number by itself: 4 × 4 = **16**. Dots for a square number make a square.",
       "Square numbers: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100."], table={"head": ["n", "1", "2", "3", "4", "5"], "rows": [["n × n", "1", "4", "9", "16", "25"]]})
s.idea("Triangular numbers", ["**Triangular numbers** make a triangle of dots: 1, 3, 6, 10, 15, 21, … Each time, add one more than last time: +2, +3, +4, …"])
s.check(N("What is the next triangular number after 10?", 15, o="O2"))
s.check(MC('Before you read on: is 10 a triangular number?', 'Yes: 1 + 2 + 3 + 4', [('No', 'Add 1 + 2 + 3 + 4.'), ('Only a square number', '10 is not square, but it is triangular.')], o='O2'))
s.mistake("Not doubling", ["5 squared is 5 × 5 = 25, not 5 × 2 = 10."])


def q1(r):
    n = r.randint(2, 10)
    return N(f"What is {n} × {n}?", n * n, o="O2")
def q2(r):
    k = r.randint(2, 7); t = TRIS[:k]
    return N(f"Continue the triangular numbers: {', '.join(map(str, t))}, …", TRIS[k], o="O2")
def q3(r):
    vals = r.sample([1, 3, 4, 6, 9, 10, 15, 16, 21, 25, 28, 36, 12, 20, 14, 18], 4)
    lab = lambda v: "both" if v in TRIS and int(v ** 0.5) ** 2 == v else "square" if int(v ** 0.5) ** 2 == v else "triangular" if v in TRIS else "neither"
    return GD("Is each number square, triangular, both or neither?", "Type", [(str(v), lab(v)) for v in vals], o="O2", extra=["square", "triangular", "both", "neither"], d="H")
def q4(r):
    ns = r.sample(range(2, 11), 3)
    return TB("Complete the table of square numbers.", ["n", "n × n"], [[str(n), B(n * n)] for n in ns], o="O2")
def q5(r):
    n = r.randint(3, 9)
    return N(f"The dots make a square with {n} dots on each side. How many dots are there?", n * n, "dots", units=["dots"], o="O2", data={"head": ["Dots on a side", str(n)], "rows": [["Total dots", "?"]]})
def q6(r):
    n = r.randint(3, 10)
    return N(f"A square number is {n * n}. What number was multiplied by itself?", n, o="O2")
def q7(r):
    a = r.randint(2, 6)
    return N(f"Work out {a} × {a} + {a + 1} × {a + 1}.", a * a + (a + 1) ** 2, o="O2", d="H")
def q8(r):
    k = r.randint(4, 9)
    return N(f"What is the {k}th triangular number?", TRIS[k - 1], o="O2", d="H")


s.std([q4, q5, q1, q2, q6, q3, q7, q8], EX("Explain why 16 is a square number.", [("4 × 4 = 16", "4 ?× ?4"), ("16 dots make a 4 by 4 square", "square|4 by 4|itself")], "16 = 4 × 4, a number multiplied by itself. 16 dots can be arranged in a 4 by 4 square.", o="O2"))

s = U.section("3.3", "Prime and composite numbers", ["O3"])
s.idea("Factors", ["A **factor** divides exactly into a number. The factors of 12 are 1, 2, 3, 4, 6 and 12.",
       "A **prime number** has exactly **two** factors: 1 and itself (2, 3, 5, 7, 11, …). A **composite number** has more than two factors. 1 is neither."],
       table={"head": ["Number", "Factors", "Type"], "rows": [["7", "1, 7", "prime"], ["8", "1, 2, 4, 8", "composite"]]})
s.check(MC("Which number is prime?", "13", [("15", ""), ("21", ""), ("9", "")], o="O3"))
s.check(MC('Before you read on: is 21 prime?', 'No: 3 × 7', [('Yes', '21 = 3 × 7.'), ('Only odd numbers are prime', 'Many odd numbers, like 9 and 21, are not prime.')], o='O3'))
s.mistake("Odd is not prime", ["9 is odd but composite: 9 = 3 × 3."])


def f1(r):
    ns = r.sample(range(2, 50), 4)
    return GD("Is each number prime or composite?", "Type", [(str(n), "prime" if n in PR else "composite") for n in ns], o="O3", extra=["prime", "composite"])
def f2(r):
    n = pick(r, [12, 16, 18, 20, 24, 30, 36])
    return N(f"How many factors does {n} have?", sum(1 for k in range(1, n + 1) if n % k == 0), o="O3")
def f3(r):
    n = pick(r, [12, 18, 20, 24, 30])
    return MS(f"Select ALL the factors of {n}.", [str(k) for k in r.sample([k for k in range(2, n) if n % k == 0], 2)], [str(k) for k in r.sample([k for k in range(4, n) if n % k], 2)], o="O3")
def f4(r):
    n = pick(r, [12, 16, 18, 20, 24])
    pr = [(k, n // k) for k in range(1, int(n ** 0.5) + 1) if n % k == 0][:3]
    return TB(f"Complete the factor pairs of {n}.", ["Factor", "Pair"], [[str(a), B(b)] for a, b in pr], o="O3")
def f5(r):
    lo = r.randint(20, 85); ps = [p for p in PR if p > lo]
    return N(f"What is the first prime number after {lo}?", ps[0], o="O3")
def f6(r):
    a, b = r.sample([p for p in PR if p < 12], 2)
    return MC(f"{a * b} = {a} × {b}. Is {a * b} prime or composite?", "composite", ["prime", "neither"], o="O3")
def f7(r):
    lo = r.randint(1, 8) * 10
    return N(f"How many prime numbers are there between {lo} and {lo + 10}?", sum(1 for p in PR if lo < p < lo + 10), o="O3", d="H")
def f9(r):
    ps = [p for p in PR if p < 30]; a, b = r.sample(ps, 2)
    return N(f"Two prime numbers add up to {a + b}. One is {a}. What is the other?", b, o="O3", d="H")


def c53(r):
    rows = r.sample([('A prime number is odd', 'Sometimes true'), ('An even number bigger than 2 is prime', 'Never true'), ('A composite number has more than two factors', 'Always true'), ('A number ending in 5 is prime', 'Sometimes true')], 4)
    return GD('Is each statement always, sometimes or never true?', "Always / sometimes / never", rows, o='O3', d="H", extra=["Always true", "Sometimes true", "Never true"], reason='2 is an even prime; 5 is prime but 15 is not.')


s.std([f1, f4, f2, f3, f5, f6, f7, f9], EX("Explain why 2 is the only even prime number.", [("2 has only two factors, 1 and 2", "1 and 2|two factors"), ("every other even number divides by 2 as well", "divide by 2|divisible by 2|factor of 2|2 is a factor")], "2 has only two factors, 1 and 2, so it is prime. Every other even number can also be divided by 2, so it has more than two factors and is composite.", o="O3"),
      deep=[c53])

U.mindmap(("Sequences", "Count on and back • through zero", "O1", "3.1"), ("Special numbers", "Square • triangular", "O2", "3.2"), ("Primes", "Exactly two factors • composite has more", "O3", "3.3"))
