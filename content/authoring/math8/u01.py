# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 1 Integers (1.1 Factors, multiples and primes, 1.2 Multiplying and dividing integers,
1.3 Square roots and cube roots, 1.4 Indices). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from math import gcd, isqrt
from kit import *
import kit as _kit
_kit.RAW_SIGNS = True   # this unit teaches the signs: keep them as written

U = Unit(1, "Integers", "Number",
         "Prime factors, HCF and LCM, multiplying and dividing negative numbers, square and cube roots, and index notation.",
         {"O1": {"code": "8Ni.01", "sec": "1.1", "codeNote": "", "t": "Write a number as a product of its prime factors and use this to find the HCF and LCM."},
          "O2": {"code": "8Ni.02", "sec": "1.2", "codeNote": "", "t": "Multiply and divide integers, including negative integers, and use the order of operations."},
          "O3": {"code": "8Ni.03", "sec": "1.3", "codeNote": "", "t": "Use positive and negative square roots and cube roots, and estimate roots."},
          "O4": {"code": "8Ni.04", "sec": "1.4", "codeNote": "", "t": "Use index notation, including zero and negative powers of 10, and the laws for multiplying and dividing powers."}})

PR = [2, 3, 5, 7, 11, 13]


def pf(n):
    f, d = [], 2
    while n > 1:
        while n % d == 0: f.append(d); n //= d
        d += 1
    return f


def pfs(n):
    f = pf(n); out = []
    for p in sorted(set(f)):
        k = f.count(p); out.append(f"{p}{sup(k) if k > 1 else ''}")
    return " × ".join(out)


def lcm(a, b): return a * b // gcd(a, b)


def comp(r, lo=24, hi=400):
    while True:
        n = r.randint(lo, hi)
        if len(pf(n)) >= 3 and max(pf(n)) <= 13: return n


# ================================================================== 1.1
s = U.section("1.1", "Factors, multiples and primes", ["O1"])
s.idea("Primes and factors", ["A **prime number** has exactly two factors: 1 and itself. 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 are the primes below 30. 1 is **not** prime.",
       "Every whole number greater than 1 can be written as a **product of prime factors** in exactly one way, e.g. 60 = 2 × 2 × 3 × 5 = 2² × 3 × 5."])
s.method("Factor tree", ["Split the number into any two factors, then keep splitting until every branch ends in a prime. Write the primes in order, using index notation."],
         steps=[("72 = 8 × 9", "any factor pair"), ("8 = 2 × 2 × 2, 9 = 3 × 3", "split until prime"), ("72 = 2³ × 3²", "write with powers")])
s.check(S("Write 90 as a product of prime factors, using index notation.", ["2 × 3² × 5", "2×3²×5", "2 x 3^2 x 5", "2*3^2*5", "2 × 3^2 × 5"], o="O1", reason="90 = 2 × 45 = 2 × 3 × 3 × 5 = 2 × 3² × 5."))
s.idea("HCF and LCM", ["The **highest common factor** (HCF) is the biggest number that divides into both. Multiply the prime factors that the numbers **share**.",
       "The **lowest common multiple** (LCM) is the smallest number both divide into. Take every prime factor, using the **highest power** that appears."])
s.example("HCF and LCM of 60 and 72", "Find the HCF and LCM of 60 and 72.", [("60 = 2² × 3 × 5, 72 = 2³ × 3²", "prime factors"), ("HCF = 2² × 3 = 12", "shared primes, lowest powers"), ("LCM = 2³ × 3² × 5 = 360", "all primes, highest powers")], "HCF 12, LCM 360")
s.check(N("Find the HCF of 36 and 84.", 12, o="O1", reason="36 = 2² × 3², 84 = 2² × 3 × 7; HCF = 2² × 3 = 12."))
s.idea("Why prime factors find the HCF and LCM", ["Every factor of 60 is built from some of its prime factors 2, 2, 3, 5. A common factor of 60 and 72 can only use primes both numbers have – so the HCF takes the shared primes.",
       "A common multiple must contain every prime of both numbers, so the LCM takes each prime at its highest power. That is also why HCF × LCM = the two numbers multiplied: 12 × 360 = 60 × 72."])
s.check(MC("Before you read on: is 51 prime?", "No: 51 = 3 × 17", [("Yes", "Check the digit sum: 5 + 1 = 6, so 3 divides it."), ("No: 51 = 7 × 7 + 2", "That does not show a factor pair.")], o="O1", hint="Try dividing by 3."))
s.mistake("HCF or LCM?", ["The HCF can be no bigger than the smaller number; the LCM can be no smaller than the bigger number. Use this to check your answer."])


def f1(r):
    n = comp(r)
    return S(f"Write {n} as a product of its prime factors, using index notation.", [pfs(n), pfs(n).replace(" ", ""), pfs(n).replace("×", "x")], o="O1", reason=f"{n} = {' × '.join(map(str, pf(n)))} = {pfs(n)}.", d="M")
def f2(r):
    a, b = r.sample([12, 18, 20, 24, 28, 30, 36, 40, 42, 45, 48, 54, 56, 60, 72, 84, 90, 96], 2)
    return N(f"Find the highest common factor (HCF) of {a} and {b}.", gcd(a, b), o="O1", reason=f"{a} = {pfs(a)}, {b} = {pfs(b)}; HCF = {gcd(a, b)}.")
def f3(r):
    a, b = r.sample([4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25], 2)
    return N(f"Find the lowest common multiple (LCM) of {a} and {b}.", lcm(a, b), o="O1", reason=f"{a} = {pfs(a)}, {b} = {pfs(b)}; LCM = {lcm(a, b)}.")
def f4(r):
    a, b = r.sample([6, 8, 9, 10, 12, 15, 16, 18, 20], 2)
    thing = pick(r, [("buses", "minutes", "leave the bus station together at 8 a.m."), ("lighthouses", "seconds", "flash together"), ("alarms", "minutes", "ring together")])
    return N(f"Two {thing[0]} repeat every {a} and every {b} {thing[1]}. They {thing[2]}. After how many {thing[1]} do they next do this together?", lcm(a, b), thing[1], units=[thing[1]], o="O1", d="H", reason=f"LCM of {a} and {b} = {lcm(a, b)}.")
def f5(r):
    a, b = r.sample([24, 30, 36, 42, 48, 54, 60, 72, 84, 90], 2)
    g = gcd(a, b)
    return N(f"A florist has {a} roses and {b} tulips. She makes identical bunches using all the flowers. What is the largest number of bunches she can make?", g, "bunches", units=["bunches"], o="O1", d="H", reason=f"HCF of {a} and {b} = {g}.")
def f6(r):
    ps = [x for x in range(20, 80) if len(pf(x)) == 1]
    p = pick(r, ps); others = r.sample([x for x in range(20, 80) if len(pf(x)) > 1], 3)
    return MC("Which of these is a prime number?", str(p), [(str(o), f"{o} = {pfs(o)}") for o in others], o="O1")
def f7(r):
    n = comp(r, 40, 300); f = pf(n); k = r.choice(sorted(set(f)))
    good = sorted({n // k, k * f[0] if n % (k * f[0]) == 0 else k}); bad = [x for x in (n // k + 1, n // k - 1, 2 * n, k * 7 + 1) if n % x][:2]
    return MS(f"{n} = {pfs(n)}. Select ALL the numbers that are factors of {n}.", [str(x) for x in good], [str(x) for x in bad], o="O1", d="H", reason=f"A factor of {n} is made from some of its prime factors {pfs(n)}.")
def f8(r):
    a = pick(r, [(2, 3, 2), (2, 2, 5), (3, 3, 2), (2, 5, 5), (2, 2, 7)]); n = a[0] * a[1] * a[2] * r.choice([1, 3, 11])
    return N(f"A number is {pfs(n)}. What is the number?", n, o="O1", reason=f"{' × '.join(map(str, pf(n)))} = {n}.")
def fa(r):
    a, b, c = r.sample([6, 8, 10, 12, 15, 18, 20], 3)
    l = lcm(lcm(a, b), c)
    return N(f"Find the LCM of {a}, {b} and {c}.", l, o="O1", d="VH", reason=f"{a} = {pfs(a)}, {b} = {pfs(b)}, {c} = {pfs(c)}; take the highest power of each prime: {pfs(l)} = {l}.")


def f9(r):
    ns = r.sample(range(20, 100), 5)
    return GD("Is each number prime?", "Prime?", [(str(n), "Prime" if len(pf(n)) == 1 else "Not prime") for n in ns], o="O1", extra=["Prime", "Not prime"], reason="A prime has exactly two factors.")
def f10(r):
    a, b = r.sample([8, 12, 15, 18, 20, 24, 30, 36], 2)
    return TB(f"Complete the table for {a} and {b}.", ["", "Value"], [["HCF", B(gcd(a, b))], ["LCM", B(lcm(a, b))]], o="O1", d="M", data={"head": ["Number", str(a), str(b)], "rows": [["Prime factors", pfs(a), pfs(b)]]}, reason=f"HCF {gcd(a, b)}, LCM {lcm(a, b)}.")


T1 = [f9, f10, f1, f2, f3, f4, f5, f6, f8, f7]
def v11(r):   # always/sometimes/never
    rows = r.sample([("The product of two primes is prime", "Never true"), ("An odd number is prime", "Sometimes true"), ("Two different primes have HCF 1", "Always true"),
                     ("The LCM of two numbers is bigger than both", "Sometimes true"), ("HCF × LCM equals the product of the two numbers", "Always true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O1", d="H", extra=["Always true", "Sometimes true", "Never true"],
              reason="Test examples: 9 is odd and not prime; the LCM of 4 and 12 is 12, not bigger than 12; a product of two primes always has those primes as extra factors.")
def v12(r):   # work backwards from prime factors
    a, b, c = r.randint(1, 3), r.randint(0, 2), r.randint(0, 1)
    n = 2 ** a * 3 ** b * 5 ** c * 7
    return N(f"A number is 2{sup(a) if a > 1 else ''} × " + (f"3{sup(b) if b > 1 else ''} × " if b else "") + (f"5 × " if c else "") + "7. What is the number?", n, o="O1", d="H", reason=f"Multiply out: {n}.")
def v13(r):   # spot the error
    return MC("Ravi says the HCF of 2³ × 3 and 2² × 3² is 2³ × 3² because you take the highest powers. What is wrong?", "That is the LCM: the HCF uses the lowest powers, 2² × 3 = 12",
              [("Nothing", "2³ × 3² = 72 is bigger than 24, so it cannot divide 24."), ("The HCF is 2 × 3", "2² × 3 = 12 divides both, and it is bigger than 6.")], o="O1", d="H",
              reason="Shared primes at their LOWEST powers give the HCF: 2² × 3 = 12. Highest powers give the LCM: 2³ × 3² = 72.")


s.std(T1, EX("Explain why the HCF of two different prime numbers is always 1.", [("a prime only has factors 1 and itself", ["only.*1 and itself|two factors|only factors"]), ("so the only common factor is 1", ["only common|share only 1|nothing else|no other common"])], "A prime number has only two factors: 1 and itself. Two different primes therefore share only the factor 1, so their HCF is 1.", o="O1"), adv=[fa, f4, f5],
      deep=[v11, v12, v13])

# ================================================================== 1.2
s = U.section("1.2", "Multiplying and dividing integers", ["O2"])
s.idea("Signs", ["When you multiply or divide two integers: **same signs give a positive** answer, **different signs give a negative** answer.",
       "(−4) × (−3) = 12,  (−4) × 3 = −12,  (−20) ÷ (−5) = 4,  20 ÷ (−5) = −4."],
       table={"head": ["×", "+", "−"], "rows": [["+", "+", "−"], ["−", "−", "+"]]})
s.check(N("Work out (−6) × (−7).", 42, o="O2", reason="Same signs: positive. 6 × 7 = 42."))
s.idea("Order of operations", ["Brackets first, then indices, then × and ÷ from left to right, then + and − from left to right.",
       "With several negative factors, count them: an **even** number of negatives gives a positive product, an **odd** number gives a negative."])
s.example("Mixed calculation", "Work out −3 × (4 − 9) + (−12) ÷ 4.", [("4 − 9 = −5", "brackets"), ("−3 × −5 = 15", "multiply"), ("−12 ÷ 4 = −3", "divide"), ("15 + (−3) = 12", "add")], "12")
s.check(N("Work out (−2) × (−3) × (−5).", -30, o="O2", reason="Three negatives: an odd number, so the answer is negative. 2 × 3 × 5 = 30 → −30."))
s.idea("Why a negative × a negative is positive", ["Look at the pattern: 3 × (−2) = −6, 2 × (−2) = −4, 1 × (−2) = −2, 0 × (−2) = 0. Each time the first number goes down by 1, the answer goes UP by 2.",
       "Carry on: (−1) × (−2) = 2, (−2) × (−2) = 4. The pattern forces a negative times a negative to be positive."],
       table={"head": ["Calculation", "Answer"], "rows": [["2 × (−2)", "−4"], ["1 × (−2)", "−2"], ["0 × (−2)", "0"], ["(−1) × (−2)", "2"], ["(−2) × (−2)", "4"]]})
s.mistake("Squaring a negative", ["(−5)² = (−5) × (−5) = 25. But −5² means −(5²) = −25. Use brackets on your calculator."])


def m1(r):
    a, b = nz(r, -12, 12), nz(r, -12, 12)
    if a > 0 and b > 0: a = -a
    return N(f"Work out {a if a > 0 else f'({a})'} × {b if b > 0 else f'({b})'}.", a * b, o="O2", reason=f"{'Same' if (a < 0) == (b < 0) else 'Different'} signs: {a * b}.")
def m2(r):
    a, b = nz(r, -12, 12), r.randint(2, 12); p = a * b * pick(r, [1, -1]); d = p // a
    return N(f"Work out {p if p > 0 else f'({p})'} ÷ {a if a > 0 else f'({a})'}.", d, o="O2", reason=f"{p} ÷ {a} = {d}.")
def m3(r):
    a, b, c = nz(r, -9, 9), nz(r, -9, 9), nz(r, -6, 6)
    w = lambda v: f"({v})" if v < 0 else str(v)
    return N(f"Work out {w(a)} × {w(b)} − {w(c)}.", a * b - c, o="O2", reason=f"{a} × {b} = {a * b}; {a * b} − ({c}) = {a * b - c}.")
def m4(r):
    t = r.randint(2, 9); h = r.randint(2, 8)
    return N(f"The temperature falls by {t} °C every hour for {h} hours. What is the total change in temperature? (Write a negative number for a fall.)", -t * h, "°C", units=["°C"], o="O2", reason=f"{h} × (−{t}) = {-t * h} °C.")
def m5(r):
    a = r.randint(2, 9); b = -a * r.randint(2, 9)
    return N(f"Find the missing number: ☐ × ({-a}) = {b}", b // -a, o="O2", d="M", reason=f"{b} ÷ ({-a}) = {b // -a}.")
def m6(r):
    rows = [("(−3) × (−4)", "Positive"), ("(−20) ÷ 5", "Negative"), ("(−2)³", "Negative"), ("(−1) × (−1) × (−1) × (−1)", "Positive"), ("6 ÷ (−3)", "Negative"), ("(−5)²", "Positive")]
    return GD("Is each answer positive or negative?", "Sign", r.sample(rows, 4), o="O2")
def m7(r):
    a, b, c = r.randint(2, 6), r.randint(2, 9), r.randint(10, 20)
    return N(f"Work out −{a} × ({b} − {c}).", -a * (b - c), o="O2", d="H", reason=f"{b} − {c} = {b - c}; −{a} × {b - c} = {-a * (b - c)}.")
def m8(r):
    a = nz(r, -8, -2); b = r.randint(2, 5)
    return N(f"Work out ({a})² − {b} × ({a}).", a * a - b * a, o="O2", d="H", reason=f"({a})² = {a * a}; {b} × ({a}) = {b * a}; {a * a} − ({b * a}) = {a * a - b * a}.")
def ma(r):
    n = r.randint(3, 8); v = -r.randint(2, 5)
    return N(f"Work out ({v}){sup(n)} without a calculator.", v ** n, o="O2", d="VH", reason=f"{n} negative factors: {'even' if n % 2 == 0 else 'odd'}, so the answer is {'positive' if n % 2 == 0 else 'negative'}: {v ** n}.")
def mb(r):
    s_, p = r.choice([(3, 2), (5, 6), (2, -8), (-1, -12), (4, -5), (-7, 12)])
    a = [(x, s_ - x) for x in range(-12, 13) if x * (s_ - x) == p]
    x, y = a[0]
    good = {x, y}; wr = []
    for a_, b_ in ((-x, -y), (x + 1, y - 1), (x - 1, y + 1), (-x, y), (x, -y), (x + 2, y - 2)):
        if {a_, b_} != good and f"{a_} and {b_}" not in wr: wr.append(f"{a_} and {b_}")
    return MC(f"Two integers have a sum of {s_} and a product of {p}. Which pair is it?", f"{x} and {y}", wr[:3], o="O2", d="VH", reason=f"{x} + {y} = {s_} and {x} × {y} = {p}.")


def m9(r):
    a, b = nz(r, -9, -2), r.randint(2, 9); c, d = r.randint(2, 9), nz(r, -9, -2)
    return TB("Complete the multiplication grid.", ["×", str(c), str(d)], [[str(a), B(a * c), B(a * d)], [str(b), B(b * c), B(b * d)]], o="O2", reason="Same signs → positive; different signs → negative.")


T2 = [m6, m9, m1, m2, m3, m4, m5, m7, m8]
def v21(r):   # sign of a long product (decision)
    k = r.randint(2, 6); nums = [-r.randint(1, 5) for _ in range(k)] + [r.randint(1, 5) for _ in range(r.randint(0, 2))]
    r.shuffle(nums); p = 1
    for x in nums: p *= x
    return MC("Without working it out: is " + " × ".join(f"({x})" if x < 0 else str(x) for x in nums) + " positive or negative?", "Positive" if p > 0 else "Negative", [("Negative" if p > 0 else "Positive", "Count the negative numbers."), ("It depends on the sizes", "Only the number of negatives decides the sign.")],
              o="O2", d="H", reason=f"There are {sum(1 for x in nums if x < 0)} negative numbers: an {'even' if sum(1 for x in nums if x < 0) % 2 == 0 else 'odd'} number, so the answer is {'positive' if p > 0 else 'negative'}.")
def v22(r):   # spot the error: (−3)² vs −3²
    a = r.randint(2, 9)
    return MC(f"Kim says −{a}² = {a * a}. What is −{a}²?", str(-a * a), [(str(a * a), f"Only {a} is squared, then the minus is applied. ({-a})² would be {a * a}."), (str(-2 * a), "Squaring is not doubling.")], o="O2", d="VH",
              reason=f"The power comes before the minus sign: −({a}²) = −{a * a}. With brackets, (−{a})² = {a * a}.")
def v23(r):   # missing number
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"Find the missing number: ☐ × ({-a}) = {a * b}", -b, o="O2", d="H", reason=f"The answer is positive and {-a} is negative, so ☐ is negative: {a * b} ÷ ({-a}) = {-b}.")


s.std(T2, EX("Explain why (−1) × (−1) × (−1) is negative.", [("(−1) × (−1) = 1", ["= ?1\\b|positive|two negatives"]), ("1 × (−1) = −1: an odd number of negatives", ["odd|three|−1|-1"])], "(−1) × (−1) = 1, because two negatives make a positive. Then 1 × (−1) = −1. An odd number of negative factors gives a negative answer.", o="O2"), adv=[ma, mb, m8],
      deep=[v21, v22, v23])

# ================================================================== 1.3
s = U.section("1.3", "Square roots and cube roots", ["O3"])
s.idea("Roots", ["A **square root** undoes squaring. Every positive number has **two** square roots: √49 = 7, but (−7)² = 49 too, so the square roots of 49 are **±7**.",
       "A **cube root** undoes cubing: ∛64 = 4 because 4³ = 64. Negative numbers have a negative cube root: ∛−27 = −3."])
s.check(N("Find ∛−125.", -5, o="O3", reason="(−5)³ = −125."))
s.idea("Estimating roots", ["Find the square (or cube) numbers either side. 50 is between 49 and 64, so √50 is between 7 and 8, and close to 7."])
s.example("Between two integers", "Between which two whole numbers does √130 lie?", [("11² = 121 and 12² = 144", ""), ("121 < 130 < 144", "")], "Between 11 and 12")
s.check(N("√90 lies between two consecutive whole numbers. Write the smaller one.", 9, o="O3", reason="81 < 90 < 100, so 9 < √90 < 10."))
s.idea("Why a square root has two answers but a cube root has one", ["Both 6 × 6 and (−6) × (−6) equal 36, so 36 has two square roots: 6 and −6 (written ±6). The symbol √36 means the positive one.",
       "For cubes the sign survives: (−5)³ = −125, so ∛−125 = −5. Each number has exactly one cube root."])
s.check(MC("Before you read on: what are the solutions of x² = 49?", "7 and −7", [("7 only", "(−7)² = 49 as well."), ("−7 only", "7² = 49 too.")], o="O3"))
s.mistake("Roots are not halves", ["√64 is 8, not 32. A root asks which number multiplied by itself gives 64."])
SQ = [n * n for n in range(1, 16)]; CU = [n ** 3 for n in range(1, 11)]


def r1(r):
    n = r.randint(4, 15)
    return N(f"Find √{n * n}.", n, o="O3", reason=f"{n} × {n} = {n * n}.")
def r2(r):
    n = r.randint(2, 10)
    return N(f"Find ∛{n ** 3}.", n, o="O3", reason=f"{n} × {n} × {n} = {n ** 3}.")
def r3(r):
    n = r.randint(2, 6)
    return N(f"Find ∛−{n ** 3}.", -n, o="O3", reason=f"(−{n})³ = −{n ** 3}.")
def r4(r):
    n = r.randint(3, 14); v = r.randint(n * n + 1, (n + 1) ** 2 - 1)
    return N(f"√{v} lies between two consecutive whole numbers. Write the larger one.", n + 1, o="O3", reason=f"{n * n} < {v} < {(n + 1) ** 2}.")
def r5(r):
    n = r.randint(2, 9); v = r.randint(n ** 3 + 1, (n + 1) ** 3 - 1)
    return N(f"∛{v} lies between two consecutive whole numbers. Write the smaller one.", n, o="O3", d="H", reason=f"{n ** 3} < {v} < {(n + 1) ** 3}.")
def r6(r):
    n = r.randint(4, 12)
    return MS(f"Select ALL the square roots of {n * n}.", [str(n), str(-n)], [str(n * n // 2) if n * n // 2 != n else str(n + 2), str(2 * n)], o="O3")
def r7(r):
    a = r.randint(6, 15)
    return N(f"A square garden has an area of {a * a} m². How long is each side?", a, "m", units=["m"], o="O3", reason=f"√{a * a} = {a} m.")
def r8(r):
    a = r.randint(2, 9)
    return N(f"A cube has a volume of {a ** 3} cm³. How long is each edge?", a, "cm", units=["cm"], o="O3", reason=f"∛{a ** 3} = {a} cm.")
def ra(r):
    a, b = r.randint(2, 6), r.randint(2, 9)
    return N(f"Work out √{a * a * b * b} − ∛{b ** 3}.", a * b - b, o="O3", d="VH", reason=f"√{a * a * b * b} = {a * b}; ∛{b ** 3} = {b}; {a * b} − {b} = {a * b - b}.")
def rb(r):
    v = pick(r, [x for x in range(20, 140) if x not in SQ]); e = round(v ** 0.5, 1)
    return N(f"Use a calculator to find √{v} to 1 decimal place.", e, o="O3", d="H", tol=0.05, reason=f"√{v} ≈ {v ** 0.5:.3f} → {e}.")


def r9(r):
    ns = r.sample(range(2, 10), 3)
    return TB("Complete the table.", ["n", "n²", "n³"], [[str(n), B(n * n), B(n ** 3)] for n in ns], o="O3")
def r10(r):
    rows = [("64", "Both"), ("1", "Both"), ("49", "Square only"), ("27", "Cube only"), ("125", "Cube only"), ("81", "Square only"), ("50", "Neither"), ("8", "Cube only"), ("36", "Square only"), ("20", "Neither")]
    return GD("Is each a square number, a cube number, both or neither?", "Type", r.sample(rows, 5), o="O3", extra=["Square only", "Cube only", "Both", "Neither"], d="H")


T3 = [r9, r10, r1, r2, r3, r4, r7, r8, r6, r5, rb]
def v31(r):   # estimate to 1 dp decision
    n = r.randint(3, 12); v = n * n + r.randint(1, n)
    return MC(f"Which is the best estimate of √{v}?", f"{n}.{min(9, round((v - n * n) / (2 * n) * 10))}" , [(f"{n + 1}.{r.randint(1, 4)}", f"{n + 1}² = {(n + 1) ** 2}, which is more than {v}."), (f"{v / 2:g}", "Square-rooting is not halving.")], o="O3", d="H",
              reason=f"{n}² = {n * n} and {n + 1}² = {(n + 1) ** 2}; {v} is just above {n * n}, so √{v} is a little more than {n}.")
def v32(r):   # always/sometimes/never
    rows = r.sample([("A negative number has a square root (in whole or decimal numbers)", "Never true"), ("A negative number has a cube root", "Always true"), ("√n is smaller than n", "Sometimes true"), ("The cube of a negative number is negative", "Always true")], 4)
    return GD("Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O3", d="H", extra=["Always true", "Sometimes true", "Never true"],
              reason="Any number squared is 0 or positive, so −9 has no square root; (−2)³ = −8, so negatives have cube roots. √0.25 = 0.5 is bigger than 0.25.")


s.std(T3, EX("Explain why 64 has two square roots but only one cube root.", [("8 × 8 = 64 and (−8) × (−8) = 64", ["−8|-8|negative"]), ("only 4³ = 64; (−4)³ = −64", ["4|−64|-64|negative cube"])], "Both 8² and (−8)² equal 64, so the square roots are ±8. But 4³ = 64 while (−4)³ = −64, so the only cube root of 64 is 4.", o="O3"), adv=[ra, rb, r5],
      deep=[v31, v32])

# ================================================================== 1.4
s = U.section("1.4", "Indices", ["O4"])
s.idea("Index notation", ["5⁴ means 5 × 5 × 5 × 5. The small number is the **index** (or power).",
       "**Powers of 10**: 10³ = 1000, 10⁰ = 1, 10⁻¹ = 1/10 = 0.1, 10⁻² = 1/100 = 0.01. Any number to the power 0 is 1."])
s.check(N("Write 10⁻³ as a decimal.", 0.001, o="O4", reason="10⁻³ = 1/1000 = 0.001."))
s.idea("Laws of indices", ["To **multiply** powers of the same number, **add** the indices: 3⁴ × 3² = 3⁶.",
       "To **divide** powers of the same number, **subtract** the indices: 7⁵ ÷ 7² = 7³."])
s.example("Simplify", "Simplify 2⁵ × 2³ ÷ 2⁴, leaving your answer as a power of 2.", [("2⁵ × 2³ = 2⁸", "add 5 + 3"), ("2⁸ ÷ 2⁴ = 2⁴", "subtract 8 − 4")], "2⁴")
s.check(S("Simplify 5⁶ ÷ 5², giving your answer as a power of 5.", ["5⁴", "5^4"], o="O4", reason="6 − 2 = 4."))
s.idea("Why the index laws work", ["2³ × 2⁴ = (2 × 2 × 2) × (2 × 2 × 2 × 2) = seven 2s = 2⁷. Multiplying powers of the same number ADDS the indices.",
       "5⁶ ÷ 5² cancels two 5s from the top: four 5s are left, 5⁴. Dividing SUBTRACTS the indices. Then 10² ÷ 10² = 10⁰ must be 1, and 10⁰ ÷ 10¹ = 10⁻¹ = 1/10."])
s.check(MC("Before you read on: what is 3² × 3⁴?", "3⁶", [("3⁸", "Add the indices, do not multiply them."), ("9⁶", "The base stays 3.")], o="O4"))
s.mistake("Don't multiply the base", ["3² × 3⁴ is 3⁶, not 9⁶. The base stays the same; only the indices change."])


def i1(r):
    b, n = r.randint(2, 6), r.randint(2, 4)
    return N(f"Work out {b}{sup(n)}.", b ** n, o="O4", reason=f"{' × '.join([str(b)] * n)} = {b ** n}.")
def i2(r):
    b, m, n = r.randint(2, 9), r.randint(2, 9), r.randint(2, 9)
    return S(f"Simplify {b}{sup(m)} × {b}{sup(n)}, leaving your answer as a power of {b}.", [f"{b}{sup(m + n)}", f"{b}^{m + n}"], o="O4", reason=f"Add the indices: {m} + {n} = {m + n}.")
def i3(r):
    b, m = r.randint(2, 9), r.randint(6, 12); n = r.randint(2, m - 2)
    return S(f"Simplify {b}{sup(m)} ÷ {b}{sup(n)}, leaving your answer as a power of {b}.", [f"{b}{sup(m - n)}", f"{b}^{m - n}"], o="O4", reason=f"Subtract the indices: {m} − {n} = {m - n}.")
def i4(r):
    k = r.randint(1, 4)
    return N(f"Write 10{sup(-k)} as a decimal.", round(10 ** -k, k), o="O4", reason=f"10{sup(-k)} = 1/{10 ** k} = {fmt(round(10 ** -k, k))}.")
def i5(r):
    b = r.randint(2, 99)
    return N(f"What is the value of {b}⁰?", 1, o="O4", reason="Any number (except 0) to the power 0 is 1.")
def i6(r):
    m, n, k = r.randint(2, 6), r.randint(2, 6), r.randint(1, 5)
    return N(f"Find the missing index: 4{sup(m)} × 4☐ = 4{sup(m + n + k)} ÷ 4{sup(k)}", n, o="O4", d="H", reason=f"The right side is 4{sup(m + n)}, so ☐ = {m + n} − {m} = {n}.")
def i7(r):
    rows = [("10³", "1000"), ("10⁰", "1"), ("10⁻¹", "0.1"), ("10⁻²", "0.01"), ("10²", "100"), ("10⁻³", "0.001")]
    return GD("Write the value of each power of 10.", "Value", r.sample(rows, 4), o="O4", extra=["10", "0.0001"])
def i8(r):
    k = r.randint(2, 6); a = r.randint(2, 9)
    return N(f"{a} × 10{sup(k)} = ?", a * 10 ** k, o="O4", reason=f"10{sup(k)} = {10 ** k}; {a} × {10 ** k} = {a * 10 ** k}.")
def ia(r):
    a, b = r.randint(2, 5), r.randint(2, 5)
    return N(f"Find n if 2{sup(a)} × 2{sup(b)} = 4ⁿ.", (a + b) / 2, o="O4", d="VH", reason=f"2{sup(a + b)} = (2²)ⁿ = 2{sup('2n')}... 2n = {a + b}, n = {fmt((a + b) / 2)}.") if (a + b) % 2 == 0 else None
def ib(r):
    m, n = r.randint(5, 9), r.randint(2, 4)
    return MC(f"Which is equal to 3{sup(m)} ÷ 3{sup(n)}?", f"3{sup(m - n)}", [f"3{sup(m + n)}", f"1{sup(m - n)}", f"3{sup(m * n)}"], o="O4", d="H")


def i9(r):
    b = r.randint(2, 5); ks = r.sample(range(0, 5), 3)
    return TB(f"Complete the table of powers of {b}.", ["Power", "Value"], [[f"{b}{sup(k)}", B(b ** k)] for k in sorted(ks)], o="O4")


T4 = [i7, i9, i1, i2, i3, i4, i5, i8, i6, ib]
def v41(r):   # spot the error
    a, b = r.randint(2, 5), r.randint(2, 5)
    return MC(f"Leo says 2{sup(a)} × 2{sup(b)} = 4{sup(a + b)}. What is right?", f"2{sup(a + b)}", [(f"4{sup(a + b)}", "The base stays 2: you are counting 2s."), (f"2{sup(a * b)}", "Add the indices, do not multiply.")], o="O4", d="H",
              reason=f"{a} twos times {b} twos is {a + b} twos: 2{sup(a + b)}.")
def v42(r):   # missing index
    a, c = r.randint(2, 6), r.randint(7, 12)
    return N(f"Find the missing index: 7{sup(a)} × 7^☐ = 7{sup(c)}", c - a, o="O4", d="H", reason=f"{a} + ☐ = {c}, so ☐ = {c - a}.")
def v43(r):   # order powers of 10
    vals = r.sample([("10⁻²", -2), ("10⁰", 0), ("10³", 3), ("10⁻¹", -1), ("10¹", 1)], 4); vals.sort(key=lambda v: v[1])
    return OD("Put these in order, smallest first.", [v[0] for v in vals], o="O4", d="H", reason="10⁻² = 0.01, 10⁻¹ = 0.1, 10⁰ = 1, 10¹ = 10, 10³ = 1000.")


s.std(T4, EX("Explain why 6⁰ = 1.", [("6² ÷ 6² = 6²⁻² = 6⁰", ["÷|divide|subtract|2 ?− ?2|2 ?- ?2"]), ("any number divided by itself is 1", ["itself|= ?1|is 1"])], "Using the law for division, 6² ÷ 6² = 6⁰. But any number divided by itself is 1, so 6⁰ = 1.", o="O4"), adv=[ia, i6, ib],
      deep=[v41, v42, v43])

U.mindmap(("Primes and factors", "Prime factors with indices • HCF: shared primes • LCM: all primes, highest powers", "O1", "1.1"),
          ("Negative numbers", "Same signs → positive • different signs → negative", "O2", "1.2"),
          ("Roots", "√ has ± answers • ∛ of a negative is negative • estimate between squares", "O3", "1.3"),
          ("Indices", "Multiply: add indices • divide: subtract • 10⁰ = 1, 10⁻¹ = 0.1", "O4", "1.4"))
