# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 1 Integers (1.1 Adding and subtracting integers, 1.2 Multiplying and dividing integers,
1.3 Lowest common multiples, 1.4 Highest common factors, 1.5 Tests for divisibility, 1.6 Square roots and cube roots).
Written by the Atomic teaching team."""
from math import gcd
from kit import *

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
NL = lambda lo, hi: {"kind": "numline", "min": lo, "max": hi}

# ================================================================== 1.1
s = U.section("1.1", "Adding and subtracting integers", ["O1"])
s.idea("Integers on a number line", ["**Integers** are whole numbers: …, −3, −2, −1, 0, 1, 2, 3, … Numbers to the right are bigger: −2 > −5.",
       "Adding a positive number moves **right**; subtracting a positive number moves **left**."], fig=NL(-6, 6))
s.idea("Negative numbers", ["**Adding a negative** is the same as subtracting: 5 + (−3) = 5 − 3 = 2.", "**Subtracting a negative** is the same as adding: 4 − (−6) = 4 + 6 = 10."])
s.example("Temperatures", "At midnight it is −4 °C. By noon it is 9 degrees warmer. What is the temperature at noon?", [("−4 + 9", "warmer means add"), ("= 5", "count 9 to the right from −4")], "5 °C")
s.check(N("Work out −7 + 3.", -4, o="O1"))
s.check(N("Work out 2 − (−5).", 7, o="O1"))
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


s.std([a8, a9, a1, a2, a3, a4, a5, a6, a10], EX("Explain why 3 − (−4) = 7.", [("subtracting a negative is the same as adding", ["same as add|becomes \\+|plus|add"]), ("3 + 4 = 7", ["3 ?\\+ ?4"])], "Taking away a negative number is the same as adding the positive: 3 − (−4) = 3 + 4 = 7.", o="O1"))

# ================================================================== 1.2
s = U.section("1.2", "Multiplying and dividing integers", ["O2"])
s.idea("Signs", ["A **positive × a negative** gives a negative: 4 × (−3) = −12. Think of it as 4 lots of −3.",
       "Division works the same way: (−20) ÷ 5 = −4."], table={"head": ["Calculation", "Sign of answer"], "rows": [["positive × positive", "+"], ["positive × negative", "−"], ["negative ÷ positive", "−"]]})
s.check(N("Work out 6 × (−4).", -24, o="O2"))
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


s.std([m5, m6, m1, m2, m3, m4, m7, m8], EX("Explain why 3 × (−5) = −15.", [("3 lots of −5", ["3 lots|three lots|repeated|add −5|−5 ?\\+ ?−5"]), ("−5 + −5 + −5 = −15", ["−15|-15"])], "3 × (−5) means 3 lots of −5: −5 + (−5) + (−5) = −15.", o="O2"))

# ================================================================== 1.3
s = U.section("1.3", "Lowest common multiples", ["O3"])
s.idea("Multiples", ["The **multiples** of 6 are 6, 12, 18, 24, 30, … (the 6 times table).",
       "A **common multiple** of 4 and 6 is in both lists: 12, 24, 36, … The **lowest common multiple** (LCM) is the smallest: 12."], table={"head": ["Number", "Multiples"], "rows": [["4", "4, 8, 12, 16, 20, 24"], ["6", "6, 12, 18, 24, 30"]]})
s.check(N("Find the LCM of 8 and 12.", 24, o="O3"))
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


s.std([l4, l7, l1, l2, l3, l5, l6], EX("Explain how to find the LCM of 6 and 9.", [("list the multiples of each number", ["list|multiples"]), ("the smallest number in both lists is 18", ["18"])], "List the multiples: 6, 12, 18, 24 … and 9, 18, 27 … The smallest number in both lists is 18.", o="O3"))

# ================================================================== 1.4
s = U.section("1.4", "Highest common factors", ["O4"])
s.idea("Factors", ["A **factor** divides exactly into a number. The factors of 18 are 1, 2, 3, 6, 9 and 18 (find them in pairs: 1 × 18, 2 × 9, 3 × 6).",
       "The **highest common factor** (HCF) of two numbers is the biggest number that is a factor of both."], table={"head": ["Number", "Factors"], "rows": [["12", "1, 2, 3, 4, 6, 12"], ["18", "1, 2, 3, 6, 9, 18"]]})
s.check(N("Find the HCF of 12 and 18.", 6, o="O4"))
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


s.std([h4, h7, h1, h2, h3, h5, h6], EX("Explain the difference between a factor and a multiple of 8.", [("a factor divides into 8, e.g. 1, 2, 4, 8", ["divides|goes into|1, ?2, ?4"]), ("a multiple is in the 8 times table, e.g. 16, 24", ["times table|16|24|multiply"])], "A factor of 8 divides into 8 exactly (1, 2, 4 and 8). A multiple of 8 is in the 8 times table (8, 16, 24, …).", o="O4"))

# ================================================================== 1.5
s = U.section("1.5", "Tests for divisibility", ["O5"])
s.idea("Quick tests", ["**2**: last digit even. **5**: ends in 0 or 5. **10**: ends in 0. **25**: ends in 00, 25, 50 or 75.",
       "**3**: digit sum divisible by 3. **9**: digit sum divisible by 9. **6**: divisible by 2 and 3.",
       "**4**: last two digits divisible by 4. **8**: last three digits divisible by 8."],
       table={"head": ["Divisor", "Test"], "rows": [["3", "digit sum ÷ 3"], ["4", "last two digits ÷ 4"], ["6", "÷ 2 and ÷ 3"], ["9", "digit sum ÷ 9"]]})
s.example("Digit sum", "Is 5427 divisible by 9?", [("5 + 4 + 2 + 7 = 18", ""), ("18 is divisible by 9", "")], "Yes")
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


s.std([d5, d3, d1, d2, d4, d6, d7], EX("Explain how to check if 7362 is divisible by 6.", [("it is even, so divisible by 2", ["even|ends in 2|divisible by 2"]), ("digit sum 18 is divisible by 3", ["18|digit sum|divisible by 3"])], "7362 is even, so it is divisible by 2. Its digit sum is 7 + 3 + 6 + 2 = 18, which is divisible by 3. Divisible by 2 and 3 means divisible by 6.", o="O5"))

# ================================================================== 1.6
s = U.section("1.6", "Square roots and cube roots", ["O6"])
s.idea("Squares and cubes", ["A **square number** is a number times itself: 7² = 49. A **cube number** is a number used three times: 4³ = 4 × 4 × 4 = 64.",
       "The **square root** undoes squaring: √49 = 7. The **cube root** undoes cubing: ∛64 = 4."], table={"head": ["n", "1", "2", "3", "4", "5"], "rows": [["n²", "1", "4", "9", "16", "25"], ["n³", "1", "8", "27", "64", "125"]]})
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


s.std([q5, q6, q1, q2, q3, q4, q7, q8], EX("Explain why 64 is both a square number and a cube number.", [("8 × 8 = 64", ["8 ?× ?8|8²"]), ("4 × 4 × 4 = 64", ["4 ?× ?4 ?× ?4|4³"])], "64 = 8 × 8, so it is a square number, and 64 = 4 × 4 × 4, so it is also a cube number.", o="O6"))

U.mindmap(("Adding and subtracting", "Number line • + (−) = − • − (−) = +", "O1", "1.1"), ("Multiplying and dividing", "Positive × negative = negative", "O2", "1.2"),
          ("LCM", "Smallest number in both times tables", "O3", "1.3"), ("HCF", "Biggest factor of both", "O4", "1.4"),
          ("Divisibility tests", "3 and 9: digit sum • 4: last two digits • 6: 2 and 3", "O5", "1.5"), ("Roots", "√ undoes squaring • ∛ undoes cubing", "O6", "1.6"))
