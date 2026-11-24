# -*- coding: utf-8 -*-
"""Stage 4 Mathematics (Primary) · Unit 1 Numbers and the number system (1.1 Counting and sequences, 1.2 Negative numbers,
1.3 Understanding place value). Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(1, "Numbers and the Number System", "Number",
         "Counting on and back in steps, sequences, negative numbers on a number line and in temperatures, and place value in 4-digit numbers.",
         {"O1": {"code": "4Ns.01", "sec": "1.1", "codeNote": "", "t": "Count on and back in steps of constant size, and continue and describe linear sequences."},
          "O2": {"code": "4Ni.01", "sec": "1.2", "codeNote": "", "t": "Read, write and order negative numbers in context, such as temperature."},
          "O3": {"code": "4Np.01", "sec": "1.3", "codeNote": "", "t": "Understand the value of each digit in 4-digit numbers, and multiply and divide by 10 and 100."}})

s = U.section("1.1", "Counting and sequences", ["O1"])
s.idea("Steps of the same size", ["A **sequence** follows a rule. 10, 40, 70, 100, … goes up in **30s**: the **term-to-term rule** is 'add 30'.",
       "Sequences can count back too: 95, 80, 65, … takes away 15 each time."], fig=NL(0, 10))
s.check(N("What is the next number: 25, 50, 75, 100, …?", 125, o="O1"))
s.mistake("Check every step", ["Look at more than two numbers to find the rule: it must work for every step."])


def c1(r):
    a, d = r.randint(1, 100), pick(r, [3, 4, 5, 6, 7, 8, 9, 15, 20, 25, 30, 50]); t = [a + i * d for i in range(5)]
    return N(f"What is the next number in the sequence {', '.join(map(str, t[:4]))}, …?", t[4], o="O1")
def c2(r):
    a, d = r.randint(60, 200), pick(r, [5, 6, 7, 9, 11, 15, 25]); t = [a - i * d for i in range(5)]
    return N(f"Continue the sequence: {', '.join(map(str, t[:4]))}, …", t[4], o="O1")
def c3(r):
    a, d = r.randint(1, 50), pick(r, [4, 6, 8, 12, 15, 20]); t = [a + i * d for i in range(6)]; k = r.randint(1, 4)
    return N(f"Find the missing number: {', '.join(str(x) if i != k else '☐' for i, x in enumerate(t))}", t[k], o="O1")
def c4(r):
    a, d = r.randint(3, 6), r.randint(2, 5); t = [a + i * d for i in range(3)]
    return N(f"Pattern 1 has {t[0]} tiles, pattern 2 has {t[1]} and pattern 3 has {t[2]}. How many tiles in pattern 6?", a + 5 * d, "tiles", units=["tiles"], o="O1", data={"head": ["Pattern", "1", "2", "3"], "rows": [["Tiles", *map(str, t)]]})
def c5(r):
    a, d = r.randint(1, 30), pick(r, [3, 4, 6, 7, 9, 11, 25]); t = [a + i * d for i in range(4)]
    return S(f"Write the term-to-term rule for {', '.join(map(str, t))}, …", [f"add {d}", f"+{d}", f"+ {d}", f"plus {d}", f"count on {d}", f"goes up by {d}", f"add {d} each time"], o="O1")
def c6(r):
    a, d = r.randint(1, 20), pick(r, [5, 9, 11, 12])
    return TB(f"A sequence starts at {a}. The rule is 'add {d}'. Complete it.", ["1st", "2nd", "3rd", "4th", "5th"], [[str(a), B(a + d), B(a + 2 * d), B(a + 3 * d), B(a + 4 * d)]], o="O1")
def c7(r):
    a, d, lim = r.randint(1, 20), pick(r, [6, 7, 8, 9, 30]), r.randint(100, 300)
    n = next(i for i in range(500) if a + i * d > lim)
    return N(f"The sequence {a}, {a + d}, {a + 2 * d}, … continues. What is the first number greater than {lim}?", a + n * d, o="O1", d="H")
def c8(r):
    a, d = r.randint(2, 9), pick(r, [3, 4, 5, 6])
    return N(f"A sequence starts at {a} and adds {d} each time. What is the 10th number?", a + 9 * d, o="O1", d="H")


s.std([c4, c6, c1, c2, c3, c5, c7, c8], EX("Explain how to find the rule for 7, 19, 31, 43, …", [("find the difference between neighbouring numbers", "difference|between|subtract"), ("it goes up by 12 each time", "12")], "Find the difference between neighbouring numbers: 19 − 7 = 12, 31 − 19 = 12. The rule is 'add 12'.", o="O1"))

s = U.section("1.2", "More on negative numbers", ["O2"])
s.idea("Below zero", ["**Negative numbers** are less than zero. On a number line they are to the left of 0: −5 is less than −2.",
       "A thermometer shows them: −3 °C is 3 degrees below freezing. To find a change, count the steps between the two numbers."], fig=NL(-6, 6))
s.check(N("The temperature is −4 °C. It rises by 6 degrees. What is it now?", 2, "°C", units=["°C"], o="O2"))
s.mistake("Further left is smaller", ["−8 is smaller than −3 even though 8 is bigger than 3."])


def n1(r):
    a, b = r.randint(-9, -1), r.randint(2, 12)
    return N(f"Work out {sg(a)} + {b}.", a + b, o="O2", fig=NL(min(a, 0) - 1, max(a + b, 0) + 1))
def n2(r):
    a, b = r.randint(1, 8), r.randint(3, 14)
    if b <= a: return None
    return N(f"Work out {a} − {b}.", a - b, o="O2")
def n3(r):
    lo, hi = r.randint(-12, -1), r.randint(1, 15)
    return N(f"At 6 a.m. it was {sg(lo)} °C. At midday it was {hi} °C. How many degrees did it rise?", hi - lo, "°C", units=["°C", "degrees"], o="O2", fig={"kind": "numline", "min": lo - 1, "max": hi + 1})
def n4(r):
    xs = r.sample(range(-15, 10), 4)
    return OD("Put these numbers in order, smallest first.", [sg(x) for x in sorted(xs)], o="O2")
def n5(r):
    a, b = r.sample(range(-20, 10), 2)
    return CMP(sg(a), sg(b), "<" if a < b else ">", o="O2")
def n6(r):
    xs = r.sample(range(-10, 15), 3); cs = ["Oslo", "Paris", "Cairo"]
    k = xs.index(min(xs))
    return S("The table shows night temperatures. Which city was coldest?", [cs[k]], o="O2", data={"head": ["City", *cs], "rows": [["°C", *map(sg, xs)]]})
def n7(r):
    a, b = r.randint(-12, -1), r.randint(-12, -1)
    if a == b: return None
    return N(f"What is the difference between {sg(a)} °C and {sg(b)} °C?", abs(a - b), "°C", units=["°C", "degrees"], o="O2", d="H")
def n8(r):
    a = r.randint(-9, -1); b = r.randint(2, 9)
    return TB("Complete the table.", ["Start (°C)", "Change", "End (°C)"], [[sg(a), f"rises {b}", B(a + b)], [sg(a), f"falls {b}", B(a - b)]], o="O2")


s.std([n3, n6, n1, n2, n4, n5, n8, n7], EX("Explain why −7 is less than −2.", [("−7 is further left on the number line", "left|further|below"), ("numbers to the left are smaller", "smaller|less")], "On a number line −7 is further to the left than −2, and numbers further left are smaller. So −7 < −2.", o="O2"))

s = U.section("1.3", "Understanding place value", ["O3"])
s.idea("Thousands, hundreds, tens and ones", ["In **4627** the 4 is worth 4000, the 6 is worth 600, the 2 is worth 20 and the 7 is worth 7.",
       "× 10 moves every digit one place left: 46 × 10 = 460. × 100 moves two places: 46 × 100 = 4600. ÷ 10 moves digits one place right."], table={"head": ["Th", "H", "T", "O"], "rows": [["4", "6", "2", "7"]]})
s.check(N("What is the value of the digit 8 in 3851?", 800, o="O3"))
s.mistake("Zero as a place holder", ["5060 has no hundreds and no ones; the zeros keep the other digits in place."])


def p1(r):
    n = r.randint(1000, 9999); d = str(n); k = r.randrange(4)
    if d.count(d[k]) > 1 or d[k] == "0": return None
    return N(f"What is the value of the digit {d[k]} in {n}?", int(d[k]) * 10 ** (3 - k), o="O3")
def p2(r):
    n = r.randint(1000, 9999)
    return TB(f"Write {n} in the place value table.", ["Th", "H", "T", "O"], [[B(n // 1000), B(n // 100 % 10), B(n // 10 % 10), B(n % 10)]], o="O3")
def p3(r):
    a = r.randint(11, 99); k = pick(r, [10, 100])
    return N(f"Work out {a} × {k}.", a * k, o="O3")
def p4(r):
    a = r.randint(11, 99) * pick(r, [10, 100]); k = 10 if a % 100 else pick(r, [10, 100])
    return N(f"Work out {a} ÷ {k}.", a // k, o="O3")
def p5(r):
    n = r.randint(1000, 9999)
    return N(f"Find the missing number: {n} = {n // 1000 * 1000} + {n // 100 % 10 * 100} + ☐ + {n % 10}", n // 10 % 10 * 10, o="O3")
def p6(r):
    n = r.randint(1000, 8999); k = pick(r, [10, 100, 1000])
    return N(f"What is {k} more than {n}?", n + k, o="O3")
def p7(r):
    th, h, t, o_ = r.randint(1, 9), r.randint(0, 9), r.randint(0, 9), r.randint(0, 9)
    return N(f"Write the number with {th} thousands, {h} hundreds, {t} tens and {o_} ones.", 1000 * th + 100 * h + 10 * t + o_, o="O3", data={"head": ["Th", "H", "T", "O"], "rows": [[str(th), str(h), str(t), str(o_)]]})
def p8(r):
    a = r.randint(11, 99)
    return N(f"Find the missing number: {a} × ☐ = {a * 100}", 100, o="O3", d="H")


s.std([p2, p7, p1, p3, p4, p5, p6, p8], EX("Explain why 34 × 100 = 3400.", [("multiplying by 100 makes it 100 times bigger", "100 times|bigger"), ("each digit moves two places left", "two places|2 places|left")], "Multiplying by 100 makes a number 100 times bigger, so each digit moves two places to the left: 34 becomes 3400.", o="O3"))

U.mindmap(("Sequences", "Term-to-term rule • count on and back", "O1", "1.1"), ("Negative numbers", "Number line • temperature", "O2", "1.2"), ("Place value", "Th H T O • × and ÷ by 10, 100", "O3", "1.3"))
