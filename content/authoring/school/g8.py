# -*- coding: utf-8 -*-
"""Stage 8 (school Grade 7) revision sets: Units 1, 2, 3, 4, 5, 8, 10, 12 and 13.
Written by the Camday teaching team."""
from decimal import Decimal as D, ROUND_HALF_UP
from fractions import Fraction as Fr
from math import gcd, log10, floor
from kit import *
from school import Reg
from school.g7 import NAMES, two, lcm, sg, rd, dstr, F, P, mx, rfr, TOLF
R = Reg(8); K = R.K
def pf(n):
    out = {}; p = 2
    while n > 1:
        while n % p == 0: out[p] = out.get(p, 0) + 1; n //= p
        p += 1
    return out
def pfs(d): return " × ".join(f"{p}{sup(e) if e > 1 else ''}" for p, e in sorted(d.items()))
def sfr(x, n):
    d = D(str(x)); e = d.adjusted(); return d.quantize(D(1).scaleb(e - n + 1), rounding=ROUND_HALF_UP)
def sfs(x, n):
    v = sfr(x, n); return dstr(D(format(v, "f")) if v != v.to_integral() or v.adjusted() < n else D(int(v)))

# ================================================================= Unit 1 · 1.1 factors, multiples, primes
def _pf(n):
    d = pf(n); right = pfs(d); ps = sorted(d)
    w1 = dict(d); w1[ps[0]] += 1; w2 = {p: 1 for p in d}; big = ps[-1]; w3 = f"{n // big // ps[0]} × {ps[0]} × {big}"
    wr = [(pfs(w1), f"This makes {eval('*'.join(str(p ** e) for p, e in w1.items()))}, not {n}.")]
    if pfs(w2) != right: wr.append((pfs(w2), "Check how many times each prime divides the number."))
    wr.append((w3, "Not every factor here is prime."))
    return MC(f"Use a factor tree to write {n} as a product of its prime factors.", right, wr, reason=f"{n} = {right}.")
K(1, "1.1", _pf, [84, 126], lambda r: r.choice([60, 90, 72, 120, 150, 168, 196, 132, 180, 140]))
_HL = [(60, 90), (72, 120), (90, 150), (48, 180), (56, 98), (70, 105), (66, 154), (54, 144)]
K(1, "1.1", lambda a, b: N(f"Find the highest common factor (HCF) of {a} and {b}.", gcd(a, b), reason=f"{a} = {pfs(pf(a))} and {b} = {pfs(pf(b))}. Multiply the common prime factors: {gcd(a, b)}."), [(84, 126)], lambda r: r.choice(_HL))
K(1, "1.1", lambda a, b: N(f"Find the lowest common multiple (LCM) of {a} and {b}.", lcm(a, b), d="H", reason=f"{a} = {pfs(pf(a))} and {b} = {pfs(pf(b))}. Take the highest power of every prime: {lcm(a, b)}."), [(84, 126)], lambda r: r.choice(_HL))
def _nidx(n, p):
    d = pf(n); txt = " × ".join(f"{q}ⁿ" if q == p else f"{q}{sup(e) if e > 1 else ''}" for q, e in sorted(d.items()))
    return N(f"{n} = {txt}. Work out the value of n.", d[p], reason=f"{n} = {pfs(d)}, so n = {d[p]}.")
K(1, "1.1", _nidx, [(150, 5)], lambda r: r.choice([(90, 3), (200, 5), (168, 2), (196, 7), (300, 5), (72, 2), (675, 3)]))
def _ridx(a, b, p):
    d = pf(a * b); txt = " × ".join(f"{q}ʳ" if q == p else f"{q}{sup(e) if e > 1 else ''}" for q, e in sorted(d.items()))
    return N(f"{a} × {b} = {txt}. Work out the value of r.", d[p], d="VH", reason=f"{a} = {pfs(pf(a))} and {b} = {pfs(pf(b))}. Add the indices of {p}: r = {d[p]}.")
K(1, "1.1", _ridx, [(96, 150, 2)], lambda r: r.choice([(48, 90, 2), (54, 60, 3), (40, 250, 5), (72, 80, 2), (108, 45, 3)]))
def _use(a, b, what):
    v = gcd(a, b) if what == "HCF" else lcm(a, b)
    return N(f"{a} = {pfs(pf(a))}. Use this fact to find the {what} of {a} and {b}.", v, d="H", reason=f"{b} = {pfs(pf(b))}. " + ("Multiply the common prime factors" if what == "HCF" else "Take the highest power of every prime") + f": {v}.")
K(1, "1.1", _use, [(300, 180, "HCF"), (300, 180, "LCM")], lambda r: r.choice([(200, 120), (360, 150), (126, 210), (240, 100), (450, 60)]) + (r.choice(["HCF", "LCM"]),))
K(1, "1.1", lambda a, h, L: N(f"The HCF of {a} and y is {h}. The LCM of {a} and y is {L}. Find the value of y.", h * L // a, d="VH", reason=f"HCF × LCM = product of the two numbers, so y = {h} × {L} ÷ {a} = {h * L // a}."), [(72, 24, 288)],
  lambda r: (lambda a, y: (a, gcd(a, y), lcm(a, y)))(*r.choice([(48, 80), (60, 84), (45, 120), (54, 90), (56, 140), (36, 120)])))
K(1, "1.1", lambda a, b, c1, c2: N(f"At a school concert, a {c1} stage light flashes every {a} seconds and a {c2} light flashes every {b} seconds. They flash together at the start of the song. After how many seconds will they next flash together?", lcm(a, b), "s", units=["s", "min"], d="H", reason=f"The LCM of {a} and {b} is {lcm(a, b)} seconds."),
  [(12, 18, "red", "blue")], lambda r: r.choice([(8, 12), (10, 15), (9, 12), (15, 20), (12, 20), (14, 21), (16, 24)]) + two(r, ["red", "blue", "green", "yellow", "white"]))
# ================================================================= 1.2 integers
_I = lambda txt, v, why="": N(f"Work out {txt}.", v, reason=why or f"= {fmt(v)}.")
def _ir(r):
    a, b, c = r.randint(2, 9), r.randint(2, 9), r.randint(2, 12); k = r.randint(0, 4)
    if k == 0: return (f"−{a} × (−{b})", a * b, "Negative × negative = positive.")
    if k == 1: return (f"−{a * b} ÷ {b}", -a, "Negative ÷ positive = negative.")
    if k == 2: return (f"−{a} × ({b} + (−{b + c}))", a * c, f"Brackets first: {b} + (−{b + c}) = −{c}. Then −{a} × (−{c}) = {a * c}.")
    if k == 3: return (f"({a} × (−{b * c})) ÷ (−{b})", a * c, f"{a} × (−{b * c}) = −{a * b * c}; −{a * b * c} ÷ (−{b}) = {a * c}.")
    return (f"−{a} × (−{b} − (−{b + c}))", -a * c, f"Brackets first: −{b} − (−{b + c}) = {c}. Then −{a} × {c} = −{a * c}.")
K(1, "1.2", _I, [("−8 × (−6)", 48, "Negative × negative = positive."), ("−42 ÷ 7", -6, "Negative ÷ positive = negative."), ("−4 × (3 + (−10))", 28, "Brackets first: 3 + (−10) = −7. Then −4 × (−7) = 28."), ("(5 × (−6)) ÷ (−3)", 10, "5 × (−6) = −30; −30 ÷ (−3) = 10."), ("−7 × (−3 − (−8))", -35, "Brackets first: −3 − (−8) = 5. Then −7 × 5 = −35.")], _ir)
def _est(a, b, op):
    ra, rb = round(a), round(b); v = ra * rb if op == "×" else ra // rb
    return N(f"Round each number to the nearest whole number to estimate {sg(a) if a < 0 else fmt(a)} {op} {sg(b)}.", v, reason=f"{fmt(ra)} {op} {sg(rb)} = {fmt(v)}.")
K(1, "1.2", _est, [(4.8, -7.3, "×"), (-41.8, -6.9, "÷")], lambda r: (lambda a, b, s: (s * (a - 0.2), -(b + 0.3), "×") if r.random() < .5 else (-(a * b - 0.2), -(b - 0.1), "÷"))(r.randint(3, 9), r.randint(3, 9), r.choice([1, -1])))
K(1, "1.2", lambda q, d: N(f"Solve x ÷ {sg(d)} = {fmt(q)}.", q * d, d="H", reason=f"x = {fmt(q)} × {sg(d)} = {fmt(q * d)}."), [(-9, -4)], lambda r: (nz(r, -12, 12), -r.randint(2, 9)))
K(1, "1.2", lambda c, y: N(f"Solve {fmt(c)}y = {fmt(c * y)}.", y, d="H", reason=f"y = {fmt(c * y)} ÷ {sg(c)} = {fmt(y)}."), [(-6, -9)], lambda r: (-r.randint(2, 9), nz(r, -12, 12)))
_BR = [("3 + 5 × 7 − 2 = 28", "3 + 5 × (7 − 2)", ["(3 + 5) × 7 − 2", "3 + (5 × 7) − 2", "(3 + 5 × 7) − 2"]), ("48 ÷ 10 − 4 + 2 = 6", "48 ÷ (10 − 4 + 2)", ["48 ÷ (10 − 4) + 2", "(48 ÷ 10) − 4 + 2", "48 ÷ 10 − (4 + 2)"]),
       ("4 + 6 × 5 − 3 = 16", "4 + 6 × (5 − 3)", ["(4 + 6) × 5 − 3", "4 + (6 × 5) − 3", "(4 + 6 × 5) − 3"]), ("36 ÷ 9 − 5 + 2 = 6", "36 ÷ (9 − 5 + 2)", ["36 ÷ (9 − 5) + 2", "(36 ÷ 9) − 5 + 2", "36 ÷ 9 − (5 + 2)"]),
       ("2 + 3 × 8 − 4 = 20", "(2 + 3) × (8 − 4)".replace("(2 + 3) × (8 − 4)", "(2 + 3) × 8 − 4 … no"), [])][:4] + [("2 × 9 − 4 + 6 = 16", "2 × (9 − 4) + 6", ["2 × (9 − 4 + 6)", "(2 × 9) − 4 + 6", "2 × 9 − (4 + 6)"]), ("60 ÷ 4 + 6 − 2 = 4", "60 ÷ (4 + 6) − 2", ["60 ÷ (4 + 6 − 2)", "(60 ÷ 4) + 6 − 2", "60 ÷ 4 + (6 − 2)"])]
K(1, "1.2", lambda eq, right, wrongs: MC(f"One set of brackets is needed to make this calculation correct:  {eq}. Which is correct?", right, [(w, "Work this one out: it does not give the answer.") for w in wrongs], d="H", reason=f"{right} = {eq.split('= ')[1]}."), _BR[:2], lambda r: r.choice(_BR[2:]))
# ================================================================= 1.3 roots
K(1, "1.3", lambda a, b, c: N(f"Work out √{a * a} ÷ √{b * b} × √{c * c}.", a // b * c, reason=f"{a} ÷ {b} × {c} = {a // b * c}."), [(10, 5, 3)], lambda r: (lambda b, k: (b * k, b, r.randint(2, 9)))(r.randint(2, 6), r.randint(2, 4)))
K(1, "1.3", lambda a, b, c: N(f"Work out ∛−{a ** 3} × ∛−{b ** 3} − ∛−{c ** 3}.", a * b + c, d="H", reason=f"(−{a}) × (−{b}) − (−{c}) = {a * b} + {c} = {a * b + c}."), [(3, 2, 1)], lambda r: (r.randint(2, 5), r.randint(2, 4), r.randint(1, 5)))
K(1, "1.3", lambda: N("Calculate (8 + √(4² × 9)) ÷ (2 × ((√49 + 3) ÷ 2)) + 5 × 2² ÷ 10. Show each step of your working on paper.", 4, d="VH", reason="√(16 × 9) = √144 = 12, so the first bracket is 20. (7 + 3) ÷ 2 = 5 and 2 × 5 = 10. 20 ÷ 10 = 2. Then 5 × 4 ÷ 10 = 2. Answer 2 + 2 = 4."), [()])
def _six(a, k):
    V = a ** 6; b = a * a
    if k == 0: return N(f"{b}³ = {a}⁶ = {fmt(V)}. Use this fact to find √{fmt(V)}.", a ** 3, d="H", reason=f"√({a}⁶) = {a}³ = {a ** 3}.")
    if k == 1: return N(f"{b}³ = {a}⁶ = {fmt(V)}. Use this fact to find ∛{fmt(V)}.", b, reason=f"{b}³ = {fmt(V)}, so ∛{fmt(V)} = {b}.")
    if k == 2: return N(f"{b}³ = {a}⁶ = {fmt(V)}. Use this fact to find ∛−{fmt(V)}.", -b, d="H", reason=f"(−{b})³ = −{fmt(V)}, so the cube root is −{b}.")
    return MC(f"{b}³ = {a}⁶ = {fmt(V)}. What is √−{fmt(V)}?", "It is not possible: no number squared gives a negative answer", [(f"−{a ** 3}", f"(−{a ** 3})² is positive."), (f"{a ** 3}", f"{a ** 3}² = {fmt(V)}, not −{fmt(V)}."), (f"−{b}", "That is the cube root.")], d="H", reason="A square is never negative, so a negative number has no (real) square root.")
K(1, "1.3", _six, [(5, 0), (5, 1), (5, 2), (5, 3)], lambda r: (r.choice([3, 4, 6, 7]), r.randint(0, 3)))
K(1, "1.3", lambda a: N(f"Work out ∛−{a ** 3}.", -a, reason=f"(−{a}) × (−{a}) × (−{a}) = −{a ** 3}."), [7], lambda r: r.choice([2, 3, 4, 5, 6, 8, 9, 10]))
def _arrow(n, others):
    v = round(n ** 0.5, 1); lo = int(v)
    return MC("The arrow points to a number on the number line. Which number does the arrow point to?", f"√{n}", [(f"√{m}", f"√{m} ≈ {fmt(round(m ** 0.5, 1))}.") for m in others], d="H", fig={"kind": "numline", "min": lo - 1, "max": lo + 2, "mark": v}, reason=f"{lo}² = {lo * lo} and {lo + 1}² = {(lo + 1) ** 2}. {n} is between them, and √{n} ≈ {fmt(v)}.")
K(1, "1.3", _arrow, [(46, [29, 40, 62])], lambda r: r.choice([(30, [20, 39, 45]), (69, [52, 60, 80]), (21, [12, 17, 30]), (88, [70, 79, 97]), (55, [40, 47, 66])]))
def _eq(kind, a):
    if kind == "sq": return MC(f"Solve x² = {a * a}. Give all possible values.", f"x = {a} or x = −{a}", [(f"x = {a} only", f"(−{a})² is also {a * a}."), (f"x = −{a} only", f"{a}² is also {a * a}."), (f"x = {a * a // 2}", "Do not halve: find the square root.")], reason=f"{a}² = {a * a} and (−{a})² = {a * a}.")
    if kind == "sq0": return MC(f"Solve x² + {a * a} = 0. Give all possible values.", "There is no solution", [(f"x = {a} or x = −{a}", f"That gives x² = {a * a}, but the equation needs x² = −{a * a}."), (f"x = −{a}", f"(−{a})² = {a * a}, which is positive."), (f"x = {a}", f"{a}² + {a * a} is not 0.")], d="H", reason=f"x² = −{a * a}, and a square is never negative, so there is no solution.")
    if kind == "cb": return N(f"Solve x³ = {a ** 3}.", a, reason=f"{a}³ = {a ** 3}. A cube root has only one value.")
    return N(f"Solve x³ + {a ** 3} = 0.", -a, d="H", reason=f"x³ = −{a ** 3}, so x = −{a}.")
K(1, "1.3", _eq, [("sq", 7), ("sq0", 8), ("cb", 3), ("cb0", 6)], lambda r: (r.choice(["sq", "sq0", "cb", "cb0"]), r.choice([2, 4, 5, 9, 10, 11, 12])))
def _pw(a, n, up):
    V = a ** n
    return N(f"{a}{sup(n)} = {fmt(V)}. Use this fact to find the value of {a}{sup(n + 1 if up else n - 1)}.", V * a if up else V // a, d="H", reason=f"{fmt(V)} {'×' if up else '÷'} {a} = {fmt(V * a if up else V // a)}.")
K(1, "1.3", _pw, [(6, 4, True), (6, 4, False)], lambda r: (r.choice([3, 4, 7, 8]), r.choice([4, 5]), r.random() < 0.5), o="O4")
# ================================================================= 1.4 indices
K(1, "1.4", lambda a: MC(f"What is the value of {a}⁰?", "1", [("0", "Any non-zero number to the power 0 is 1."), (str(a), f"That is {a}¹."), (f"1/{a}", f"That is {a}⁻¹.")], reason=f"{a}⁰ = 1."), [5], lambda r: r.choice([2, 3, 4, 7, 9, 12]))
def _sp8(a, txt, v, why): return N(f"Write {txt} as a single power of {a}. Type the index.", v, reason=why)
def _sp8r(r):
    a = r.choice([2, 3, 6, 7]); m, n = r.randint(2, 9), r.randint(2, 6); k = r.randint(0, 2)
    if k == 0: return (a, f"{a}{sup(m)} × {a}{sup(n)}", m + n, f"Add the indices: {a}{sup(m + n)}.")
    if k == 1: return (a, f"({a}{sup(m)}){sup(n)}", m * n, f"Multiply the indices: {a}{sup(m * n)}.")
    return (a, f"{a}{sup(m + n)} ÷ {a}{sup(n)}", m, f"Subtract the indices: {a}{sup(m)}.")
K(1, "1.4", _sp8, [(5, "5³ × 5⁴", 7, "Add the indices: 5⁷."), (5, "(5²)⁴", 8, "Multiply the indices: 5⁸."), (5, "5⁹ ÷ 5³", 6, "Subtract the indices: 5⁶."), (5, "5", 1, "5 = 5¹.")], _sp8r)
K(1, "1.4", lambda b, n, a, k: N(f"Write {b}{sup(n)} as a power of {a}. Type the index.", k * n, d="H", reason=f"{b} = {a}{sup(k)}, so {b}{sup(n)} = ({a}{sup(k)}){sup(n)} = {a}{sup(k * n)}."), [(8, 4, 2, 3), (27, 2, 3, 3), (16, 3, 4, 2)],
  lambda r: r.choice([(4, 5, 2, 2), (9, 4, 3, 2), (25, 3, 5, 2), (8, 5, 2, 3), (32, 2, 2, 5), (125, 2, 5, 3), (81, 2, 3, 4)]))
K(1, "1.4", lambda a, m, n, p: N(f"Work out the value of v:  {a}{sup(m)} ÷ {a}{sup(n)} × {a}{sup(p)} = {a}ᵛ", m - n + p, d="H", reason=f"{m} − {n} + {p} = {m - n + p}."), [(3, 8, 2, 4)], lambda r: (r.choice([2, 5, 7]), r.randint(6, 12), r.randint(2, 5), r.randint(2, 6)))
K(1, "1.4", lambda a, m, n: N(f"Find t:  {a}{sup(m)} × {a}ᵗ = {a}{sup(n)}", n - m, d="VH", reason=f"{m} + t = {n}, so t = {n - m}."), [(5, 3, -4)], lambda r: (r.choice([2, 3, 7]), r.randint(2, 6), -r.randint(1, 5)))
K(1, "1.4", lambda a, m, n, p, q: N(f"Simplify ({a}{sup(m)}){sup(n)} × ({a}{sup(p)}){sup(q)}. Give your answer as a power of {a}: type the index.", m * n + p * q, d="H", reason=f"{a}{sup(m * n)} × {a}{sup(p * q)} = {a}{sup(m * n + p * q)}."), [(2, 4, 3, 3, 2)], lambda r: (r.choice([3, 5, 7]), r.randint(2, 5), r.randint(2, 3), r.randint(2, 4), r.randint(2, 3)))
def _ring12(a, t):
    ok = [f"{a}³ × {a}{sup(t - 4)} × {a}", f"{a}{sup(t + 3)} ÷ {a}³", f"({a}³){sup(t // 3)}"] if t % 3 == 0 else [f"{a}³ × {a}{sup(t - 4)} × {a}", f"{a}{sup(t + 3)} ÷ {a}³", f"({a}²){sup(t // 2)}"]
    bad = [f"{a}{sup(2 * t)} ÷ {a}²", f"{a}⁵ × {a}{sup(t - 6)}"]
    return MS(f"Select all the calculations that simplify to {a}{sup(t)}.", ok, bad, d="H", reason=f"Add indices when multiplying, subtract when dividing, multiply for a power of a power. {bad[0]} = {a}{sup(2 * t - 2)} and {bad[1]} = {a}{sup(t - 1)}.")
K(1, "1.4", _ring12, [(4, 12)], lambda r: (r.choice([2, 3, 5, 7]), r.choice([6, 8, 10, 18])))
K(1, "1.4", lambda m, n: N(f"Simplify 10{sup(m)} ÷ 10{sup(n)}. Give your answer as a power of 10: type the index.", m - n, reason=f"{m} − {n} = {m - n}, so the answer is 10{sup(m - n)}."), [(9, 3)], lambda r: (r.randint(7, 12), r.randint(2, 5)))
K(1, "1.4", lambda m, n: N(f"Simplify 2 × 5 × 10{sup(m)} × 10{sup(n)}. Give your answer as a power of 10: type the index.", m + n + 1, d="H", reason=f"2 × 5 = 10¹, so the answer is 10{sup(m + n + 1)}."), [(3, 4)], lambda r: (r.randint(2, 6), r.randint(2, 6)))
# number sets (8Ni.04)
K(1, "1.2", lambda: MC("In a Venn diagram, set R is inside set Q, and set Q is inside set P. The sets are the natural numbers, the integers and the rational numbers. Which is correct?", "P = rational numbers, Q = integers, R = natural numbers",
  [("P = natural numbers, Q = integers, R = rational numbers", "The natural numbers are the smallest set, so they are inside the others."), ("P = integers, Q = rational numbers, R = natural numbers", "Every integer is rational, so the integers are inside the rational numbers."), ("P = rational numbers, Q = natural numbers, R = integers", "Every natural number is an integer, not the other way round.")],
  d="H", reason="Every natural number is an integer and every integer is a rational number."), [()])
_SETS = [("Every integer is a rational number.", "True"), ("−9 is a natural number.", "False"), ("0.25 is an integer.", "False"), ("Every natural number is an integer.", "True"), ("−3 is an integer.", "True"), ("Every rational number is an integer.", "False"), ("2/5 is a rational number.", "True"), ("0 is a negative integer.", "False"), ("−1/2 is a natural number.", "False"), ("7 is a rational number.", "True")]
K(1, "1.2", lambda rows: GD("Is each statement true or false?", "Statement", rows, reason="Natural numbers: 1, 2, 3, … Integers: …, −2, −1, 0, 1, 2, … Rational numbers: any number that can be written as a fraction of integers."), [(_SETS[:4],)], lambda r: (r.sample(_SETS[4:], 4),))

# ================================================================= Unit 3 · 3.1 × and ÷ by 0.1, 0.01
def _p01(a, op, m):
    v = D(str(a)) * D(m) if op == "×" else D(str(a)) / D(m)
    return N(f"Work out {dstr(D(str(a)))} {op} {m}.", float(v), reason=(f"× {m} is the same as ÷ {fmt(1 / float(m))}" if op == "×" else f"÷ {m} is the same as × {fmt(1 / float(m))}") + f": {dstr(v)}.")
K(3, "3.1", _p01, [(370, "×", "0.1"), (9, "×", "0.01"), (6, "÷", "0.1"), (0.48, "÷", "0.01"), (800, "÷", "0.001")], lambda r: (r.choice([240, 7, 5.6, 0.36, 81, 1500, 0.9, 62.5]), r.choice("×÷"), r.choice(["0.1", "0.01", "0.001"])))
def _w01(a, op, m):
    v = D(str(a)) * D(m) if op == "×" else D(str(a)) / D(m); o = "0.01" if m == "0.1" else "0.1"
    return MC(f"Which number makes this correct?  {dstr(D(str(a)))} {op} ☐ = {dstr(v)}", m, [(o, f"Check: {dstr(D(str(a)))} {op} {o} = {dstr(D(str(a)) * D(o) if op == '×' else D(str(a)) / D(o))}."), ("10", "Multiplying by 0.1 or 0.01 makes a number smaller; dividing makes it bigger.")], reason=f"{dstr(D(str(a)))} {op} {m} = {dstr(v)}.")
K(3, "3.1", _w01, [(7.2, "×", "0.1"), (3.8, "÷", "0.01"), (0.9, "×", "0.01"), (56, "÷", "0.1")], lambda r: (r.choice([4.5, 27, 0.6, 8.1, 39, 0.75]), r.choice("×÷"), r.choice(["0.1", "0.01"])))
_MEI = [("Dividing it by 10² will make it smaller.", "True"), ("Multiplying it by 10³ makes it 30 times bigger.", "False"), ("Multiplying it by 0.1 will make it bigger.", "False"), ("Dividing it by 0.01 is the same as × 100.", "True"),
        ("Dividing it by 0.1 will make it bigger.", "True"), ("Multiplying it by 0.01 is the same as ÷ 100.", "True"), ("Multiplying it by 10² makes it 20 times bigger.", "False"), ("Dividing it by 0.1 is the same as ÷ 10.", "False"), ("Multiplying it by 0.01 will make it smaller.", "True")]
K(3, "3.1", lambda nm, rows: GD(f"{nm} thinks of a whole number greater than 0. Is each statement about the number true or false?", "Statement", rows, d="H", reason="× 0.1 = ÷ 10 and × 0.01 = ÷ 100 (smaller). ÷ 0.1 = × 10 and ÷ 0.01 = × 100 (bigger). 10³ means × 1000."), [("Mei", _MEI[:4])], lambda r: (pick(r, NAMES), r.sample(_MEI[4:], 4)))
K(3, "3.1", lambda nm, a, m, thing, bag: N(f"{nm} has {a} kg of {thing}. It is packed into {bag} that each hold {m} kg. How many {bag} can be filled?", float(D(str(a)) / D(m)), d="H", reason=f"{a} ÷ {m} = {dstr(D(str(a)) / D(m))}."),
  [("Mr Tuan", 45, "0.1", "rice", "bags")], lambda r: (r.choice(["Ms Hana", "Mr Omar", "Ms Zara"]), r.choice([12, 30, 7, 2.5, 64]), r.choice(["0.1", "0.01"]), r.choice(["flour", "sugar", "tea", "spice"]), r.choice(["bags", "jars", "packets"])))
# ================================================================= 3.2 significant figures
K(3, "3.2", lambda x, n: N(f"Round {dstr(D(x))} to {n} significant figure{'s' if n > 1 else ''}.", float(sfr(x, n)), reason=f"Count {n} digit{'s' if n > 1 else ''} from the first non-zero digit, then look at the next digit: {sfs(x, n)}."),
  [("586", 2), ("0.004572", 2), ("2.38461", 4), ("654321", 3), ("263.84", 1), ("26438.7", 2)],
  lambda r: (r.choice(["473", "0.006138", "5.27193", "819654", "348.27", "71652.3", "0.08265", "9463", "15.482"]), r.choice([1, 2, 3])))
def _est30(a, b, c, e):
    exact = (a + b) ** 2 / (c - e)
    return N(f"Work out the exact value of ({fmt(a)} + {fmt(b)})² ÷ ({fmt(c)} − {fmt(e)}).", exact, d="H", reason=f"({fmt(a + b)})² ÷ {fmt(c - e)} = {fmt((a + b) ** 2)} ÷ {fmt(c - e)} = {fmt(exact)}.")
K(3, "3.2", _est30, [(2.4, 5.6, 6.5, 4.5)], lambda r: (lambda s, dd: (s - 2.6, 2.6, dd + 3.5, 3.5))(r.choice([6, 8, 10, 12]), r.choice([2, 4])))
def _est30e(a, b, c, e):
    f1 = lambda v: float(sfr(v, 1)); est = (f1(a) + f1(b)) ** 2 / (f1(c) - f1(e))
    return MC(f"Round each number to 1 significant figure. Which calculation estimates ({fmt(a)} + {fmt(b)})² ÷ ({fmt(c)} − {fmt(e)})?", f"({fmt(f1(a))} + {fmt(f1(b))})² ÷ ({fmt(f1(c))} − {fmt(f1(e))})",
              [(f"({fmt(int(a))} + {fmt(int(b))})² ÷ ({fmt(int(c))} − {fmt(int(e))})", "Round, do not just cut off the decimals."), (f"({fmt(f1(a))} + {fmt(f1(b))}) × 2 ÷ ({fmt(f1(c))} − {fmt(f1(e))})", "Squaring is not doubling."), (f"({fmt(f1(a) * 10)} + {fmt(f1(b) * 10)})² ÷ ({fmt(f1(c))} − {fmt(f1(e))})", "Rounding to 1 s.f. keeps the size of the number.")], d="H", reason=f"To 1 s.f. the numbers are {fmt(f1(a))}, {fmt(f1(b))}, {fmt(f1(c))} and {fmt(f1(e))}; the estimate is about {fmt(round(est, 1))}.")
K(3, "3.2", _est30e, [(2.4, 5.6, 6.5, 4.5)], lambda r: (r.choice([3.4, 1.7, 4.3]), r.choice([5.8, 6.7, 2.6]), r.choice([8.6, 9.4, 7.7]), r.choice([2.3, 3.8, 4.2])))
def _pop(v, n, thing):
    e = len(str(v)) - n; h = 10 ** e // 2
    return TB(f"{thing} is {fmt(v)} when rounded to {n} significant figures. Write down the smallest and the largest whole number it could be.", ["Smallest", "Largest"], [[B(v - h), B(v + h - 1)]], d="VH", skill="Reasoning", reason=f"Half of {fmt(10 ** e)} is {h}: from {fmt(v - h)} up to {fmt(v + h - 1)} ({fmt(v + h)} would round up).")
K(3, "3.2", _pop, [(7900, 2, "The population of a town")], lambda r: r.choice([(4600, 2, "The number of people at a match"), (38000, 2, "The population of a town"), (5000, 1, "The number of books in a library"), (12300, 3, "The number of visitors to a museum"), (840, 2, "The number of students in a school")]))

# ================================================================= Unit 4 · decimals
def _ordd(xs, big):
    v = sorted(xs, key=float, reverse=big)
    return OD(f"Write these numbers in order of size, starting with the {'largest' if big else 'smallest'}.", v, reason="Write every number with the same number of decimal places, then compare: " + ", ".join(v) + ".")
def _orddr(r):
    a, b = r.sample(range(1, 10), 2)
    return ([f"0.{a}{b}", f"0.0{a}{b}", f"0.{a}", f"0.{a}0{b}", f"0.{b}{a}"], r.random() < 0.5)
K(4, "4.1", _ordd, [(["0.53", "0.053", "0.5", "0.503", "0.35"], True)], _orddr)
def _ordl(items):
    v = sorted(items, key=lambda t: t[1])
    return OD("Write these lengths in order of size, starting with the shortest.", [t[0] for t in v], d="H", reason="Change every length to the same unit first: " + ", ".join(t[0] for t in v) + ".")
def _ordlr(r):
    a = r.randint(11, 18); out = [(f"{a / 10:g} m", a * 100), (f"{a * 10 - r.randint(15, 40)} cm", 0), (f"{a * 100 - r.choice([150, 180, 230])} mm", 0), (f"{(a - 3) / 10:g} m", (a - 3) * 100), (f"{a * 10 - 5} cm", (a * 10 - 5) * 10)]
    out[1] = (out[1][0], int(out[1][0].split()[0]) * 10); out[2] = (out[2][0], int(out[2][0].split()[0]))
    return (out,) if len({t[1] for t in out}) == 5 else None
K(4, "4.1", _ordl, [([("1.2 m", 1200), ("95 cm", 950), ("1020 mm", 1020), ("0.9 m", 900), ("115 cm", 1150)],)], _ordlr)
def _temp(cs, ts):
    v = sorted(zip(cs, ts), key=lambda t: float(t[1]))
    return OD("The table shows the lowest temperature in four cities one winter night. List the cities from coldest to warmest.", [c for c, _ in v], d="H", data={"caption": "Lowest temperature", "head": ["City"] + cs, "rows": [["Temp (°C)"] + [f"−{t[1:]}" for t in ts]]}, reason="For negative numbers, the one further from zero is colder: " + ", ".join(f"{c} (−{t[1:]})" for c, t in v) + ".")
def _tempr(r):
    a, b = r.sample(range(1, 10), 2); w = r.randint(3, 9)
    return (r.sample(["Oslo", "Helsinki", "Moscow", "Riga", "Tallinn", "Ottawa", "Harbin", "Astana"], 4), [f"-{w}.0{a}", f"-{w}.{a}{b}", f"-{w}.{a}", f"-0.{w}{a}"])
K(4, "4.1", _temp, [(["Oslo", "Helsinki", "Moscow", "Riga"], ["-8.04", "-8.44", "-8.4", "-0.84"])], _tempr)
_TF4 = [("0.6 L = 60 mL", "False"), ("3.05 kg ≠ 3500 g", "True"), ("−0.7 < −0.75", "False"), ("1.8 km > 1080 m", "True"), ("0.09 ≥ 0.1", "False"),
        ("0.4 L = 400 mL", "True"), ("2.07 kg = 2700 g", "False"), ("−0.3 > −0.35", "True"), ("1.5 km < 1050 m", "False"), ("0.2 ≥ 0.08", "True"), ("4.5 m ≠ 450 cm", "False"), ("−1.6 < −1.06", "True")]
K(4, "4.1", lambda rows: GD("Is each statement true or false?", "Statement", rows, d="H", reason="Change measures to the same unit before comparing. For negative numbers, the number further from zero is smaller."), [(_TF4[:5],)], lambda r: (r.sample(_TF4[5:], 5),))
def _btw4(lo, hi, right, wrongs):
    s = "<" if float(lo.replace("−", "-")) < float(hi.replace("−", "-")) else ">"
    return MC(f"Which decimal makes the statement true?  {lo} {s} ☐ {s} {hi}", right, [(w, "This number is not between the two values.") for w in wrongs], d="H", reason=f"{right} lies between {lo} and {hi}.")
K(4, "4.1", _btw4, [("4.27", "4.28", "4.275", ["4.3", "4.207", "4.285"]), ("−3.1", "−3.2", "−3.15", ["−3.05", "−3.25", "−3.01"])],
  lambda r: r.choice([("6.41", "6.42", "6.418", ["6.5", "6.408", "6.428"]), ("−2.6", "−2.7", "−2.64", ["−2.06", "−2.74", "−2.55"]), ("0.83", "0.84", "0.836", ["0.9", "0.803", "0.85"]), ("−5.3", "−5.4", "−5.38", ["−5.03", "−5.41", "−5.29"])]))
K(4, "4.2", lambda a, m: MC(f"Fill in the missing number:  {a} × ☐ = {dstr(D(a) * D(m))}", m, [(x, f"{a} × {x} = {dstr(D(a) * D(x))}.") for x in ("0.1", "0.01", "0.001", "10") if x != m][:3], reason=f"{a} × {m} = {dstr(D(a) * D(m))}."), [("3.6", "0.01")], lambda r: (r.choice(["4.8", "52", "0.7", "9.1"]), r.choice(["0.1", "0.01", "0.001"])))
K(4, "4.3", lambda a, m: MC(f"Fill in the missing number:  {a} ÷ ☐ = {dstr(D(a) / D(m))}", m, [(x, f"{a} ÷ {x} = {dstr(D(a) / D(x))}.") for x in ("0.1", "0.01", "0.001", "10") if x != m][:3], reason=f"{a} ÷ {m} = {dstr(D(a) / D(m))}."), [("52", "0.1")], lambda r: (r.choice(["4.8", "37", "0.6", "9.1"]), r.choice(["0.1", "0.01", "0.001"])))
K(4, "4.2", lambda v, m: N(f"Fill in the missing number:  ☐ × {m} = {v}", float(D(str(v)) / m), d="H", reason=f"{v} ÷ {m} = {dstr(D(str(v)) / m)}."), [(7, 100)], lambda r: (r.choice([3, 9, 4.2, 0.6, 58]), r.choice([10, 100, 1000])))
K(4, "4.3", lambda x, n: N(f"Round {x} correct to {n} significant figure{'s' if n > 1 else ''}.", float(sfr(x, n)), reason=f"Start counting at the first non-zero digit: {sfs(x, n)}."), [("0.04968", 1), ("0.04968", 3)], lambda r: (r.choice(["0.07254", "0.003861", "0.5097", "0.06045"]), r.choice([1, 2, 3])), o=None)
def _fact(a, b, k):
    P_ = a * b
    q = [(f"{a / 10:g} × {b / 10:g}", P_ / 100), (f"{a / 100:g} × {b * 10}", P_ / 10), (f"{P_ / 100:g} ÷ {b / 100:g}", a), (f"{P_} ÷ {a / 10:g}", b * 10)][k]
    return N(f"Use the fact that {a} × {b} = {P_} to work out {q[0]}.", q[1], d="H", reason=f"Compare the place values with {a} × {b} = {P_}: the answer is {fmt(q[1])}.")
K(4, "4.2", _fact, [(64, 17, 0), (64, 17, 1)], lambda r: r.choice([(48, 23), (36, 29), (52, 18), (74, 13)]) + (r.randint(0, 1),))
K(4, "4.3", _fact, [(64, 17, 2), (64, 17, 3)], lambda r: r.choice([(48, 23), (36, 29), (52, 18), (74, 13)]) + (r.randint(2, 3),))
def _hoa(nm, a, b):
    right = D(a) * D(b); wrong = right * 10; ea, eb = round(float(a)), float(sfr(b, 1))
    return MC(f"{nm} says that {a} × {b} = {dstr(wrong)}. Which estimate shows that {nm} is wrong?", f"{ea} × {fmt(eb)} = {fmt(ea * eb)}, so {dstr(wrong)} is far too big", [(f"{ea} × {fmt(eb * 10)} = {fmt(ea * eb * 10)}, so the answer is about right", f"{b} rounds to {fmt(eb)}, not {fmt(eb * 10)}."), (f"{ea} + {fmt(eb)} = {fmt(ea + eb)}, so {dstr(wrong)} is too big", "Estimate with the same operation: multiply."), ("The answer must have 2 decimal places, so it is right", "Counting decimal places does not check the size.")], d="H", reason=f"{a} × {b} ≈ {ea} × {fmt(eb)} = {fmt(ea * eb)}. The correct answer is {dstr(right)}.")
K(4, "4.2", _hoa, [("Hoa", "8.9", "0.52")], lambda r: (pick(r, NAMES), r.choice(["6.8", "7.9", "11.2", "4.9"]), r.choice(["0.31", "0.48", "0.19", "0.72"])))
K(4, "4.2", lambda a, b: N(f"Work out {a} × {b}.", float(D(a) * D(b)), reason=f"Multiply the whole numbers, then put back the decimal places: {dstr(D(a) * D(b))}."), [("0.6", "0.04"), ("13.5", "0.7"), ("2.08", "1.5")], lambda r: (r.choice(["0.8", "12.5", "3.06", "0.07", "24.5", "1.75"]), r.choice(["0.03", "0.6", "1.2", "0.9", "2.4"])))
K(4, "4.2", lambda rate, area: N(f"A painter uses {rate} litres of paint for every square metre of wall. The wall has an area of {area} m². How much paint does the painter need?", float(D(rate) * D(area)), "litres", units=["litres", "ml"], d="H", reason=f"{area} × {rate} = {dstr(D(rate) * D(area))} litres."), [("0.65", "12.4")], lambda r: (r.choice(["0.45", "0.75", "0.35", "0.85"]), r.choice(["14.2", "9.6", "18.4", "22.8"])))
K(4, "4.3", lambda q, b: N(f"Work out {dstr(D(q) * D(b))} ÷ {b}.", float(D(q)), reason=f"Multiply both numbers by {10 ** max(1, -D(b).as_tuple().exponent)} to make the divisor a whole number. Answer {q}."), [("5.7", "0.5"), ("33", "1.2")], lambda r: (r.choice(["4.6", "27", "8.5", "36", "0.95", "140"]), r.choice(["0.4", "1.5", "0.06", "2.5", "0.8"])))
K(4, "4.3", lambda a, x: N(f"{a} × ▲ = {dstr(D(a) * D(x))}. Find the value of ▲.", float(D(x)), d="H", reason=f"▲ = {dstr(D(a) * D(x))} ÷ {a} = {x}."), [("0.7", "6.2")], lambda r: (r.choice(["0.6", "0.9", "0.4", "1.2"]), r.choice(["7.3", "4.5", "8.1", "5.4"])))
K(4, "4.3", lambda kg, price, fruit: N(f"A {kg} kg bag of {fruit} costs {fmt(int(D(kg) * price))} dong. Work out the price of 1 kg of {fruit}.", price, "dong", units=["dong"], d="H", reason=f"{fmt(int(D(kg) * price))} ÷ {kg} = {fmt(price)} dong."), [("2.5", 45000, "mangoes")], lambda r: (r.choice(["1.5", "2.5", "3.5", "0.5"]), r.choice([32000, 48000, 56000, 64000]), r.choice(["oranges", "apples", "lychees", "grapes"])))
_LAW = [("2.5 × 7.3 × 4", 73, "2.5 × 4 = 10, then 10 × 7.3 = 73."), ("9.4 × 0.8 + 0.6 × 0.8", 8, "0.8 × (9.4 + 0.6) = 0.8 × 10 = 8."), ("4.7 × 99", 465.3, "4.7 × 100 − 4.7 = 470 − 4.7 = 465.3."),
        ("0.5 × 8.7 × 2", 8.7, "0.5 × 2 = 1, then 1 × 8.7 = 8.7."), ("6.3 × 0.4 + 3.7 × 0.4", 4, "0.4 × (6.3 + 3.7) = 0.4 × 10 = 4."), ("3.6 × 99", 356.4, "3.6 × 100 − 3.6 = 356.4."), ("1.25 × 9.1 × 8", 91, "1.25 × 8 = 10, then 10 × 9.1 = 91."), ("7.2 × 1.3 + 2.8 × 1.3", 13, "1.3 × (7.2 + 2.8) = 1.3 × 10 = 13."), ("5.2 × 101", 525.2, "5.2 × 100 + 5.2 = 525.2.")]
K(4, "4.4", lambda t, v, why: N(f"Use the laws of arithmetic to work out {t}.", v, d="H", reason=why), _LAW[:3], lambda r: r.choice(_LAW[3:]))
_BR4 = [("2.4 + 0.6 × 5 − 3 = 12", "(2.4 + 0.6) × 5 − 3", ["2.4 + 0.6 × (5 − 3)", "2.4 + (0.6 × 5) − 3", "(2.4 + 0.6 × 5) − 3"]), ("9 − 1.5 × 4 + 2 = 0", "9 − 1.5 × (4 + 2)", ["(9 − 1.5) × 4 + 2", "9 − (1.5 × 4) + 2", "(9 − 1.5 × 4) + 2"]),
        ("1.5 + 0.5 × 6 − 2 = 10", "(1.5 + 0.5) × 6 − 2", ["1.5 + 0.5 × (6 − 2)", "1.5 + (0.5 × 6) − 2", "(1.5 + 0.5 × 6) − 2"]), ("8 − 2.5 × 2 + 1 = 0.5", "8 − 2.5 × (2 + 1)", ["(8 − 2.5) × 2 + 1", "8 − (2.5 × 2) + 1", "(8 − 2.5 × 2) + 1"]), ("3.2 + 0.8 × 4 − 1 = 15", "(3.2 + 0.8) × 4 − 1", ["3.2 + 0.8 × (4 − 1)", "3.2 + (0.8 × 4) − 1", "(3.2 + 0.8 × 4) − 1"])]
K(4, "4.4", lambda eq, right, wrongs: MC(f"One set of brackets is needed to make this calculation correct:  {eq}. Which is correct?", right, [(w, "Work this one out: it does not give the answer.") for w in wrongs], d="H", reason=f"{right} = {eq.split('= ')[1]}."), _BR4[:2], lambda r: r.choice(_BR4[2:]))

# ================================================================= Unit 2 · expressions, formulae, equations
_EFE = [("3t − 7", "Expression"), ("v = u + at", "Formula"), ("2w + 5 = w − 1", "Equation"), ("6(h − 2)", "Expression"), ("A = lw", "Formula"), ("4x − 3 = 9", "Equation"), ("5y + 2", "Expression"), ("P = 2(l + w)", "Formula"), ("3(k + 1) = 12", "Equation"), ("x² − 4x", "Expression"), ("s = d ÷ t", "Formula"), ("7 − 2m = m + 1", "Equation")]
K(2, "2.1", lambda rows: GD("Is each an expression, a formula or an equation?", "", rows, extra=["Expression", "Formula", "Equation"], reason="An expression has no equals sign. A formula is a rule linking two or more variables. An equation can be solved to find an unknown value."), [(_EFE[:4],)], lambda r: (r.sample(_EFE[4:], 4),))
K(2, "2.1", lambda v, a, b: X(f"Write an expression: take {a} from {v}, then divide the result by {b}.", f"({v}-{a})/{b}", vars=v, reason=f"({v} − {a}) ÷ {b}. The brackets show that the subtraction is done first."), [("t", 9, 4)], lambda r: (r.choice("nxyk"), r.randint(2, 12), r.randint(2, 9)))
K(2, "2.1", lambda v, a, b: X(f"Write an expression: add {a} to {v}, then multiply by −{b}.", f"-{b}({v}+{a})", vars=v, d="H", show=f"−{b}({v} + {a})", reason=f"−{b}({v} + {a}), which is also −{b}{v} − {a * b}."), [("h", 7, 2)], lambda r: (r.choice("nxyk"), r.randint(2, 9), r.randint(2, 6)))
def _peri(v, a, b, c):
    return X(f"The shortest side of a triangle is ({a}{v} − {b}) cm. The middle side is {c} cm longer than the shortest side. The longest side is twice the shortest side. Find an expression for the perimeter, in cm. Simplify your answer.", f"{4 * a}{v}+({c - 4 * b})", vars=v, d="VH", mustNot=["\\("], show=poly((4 * a, v), (c - 4 * b, "")),
             reason=f"({a}{v} − {b}) + ({a}{v} − {b} + {c}) + 2({a}{v} − {b}) = {poly((4 * a, v), (c - 4 * b, ''))}.")
K(2, "2.1", _peri, [("p", 2, 1, 4)], lambda r: (r.choice("xnkm"), r.randint(2, 5), r.randint(1, 3), r.randint(2, 9)))
def _sub(r_, s_, k):
    q = [(f"2(s − r)²", 2 * (s_ - r_) ** 2, f"s − r = {s_ - r_}; squared = {(s_ - r_) ** 2}; × 2 = {2 * (s_ - r_) ** 2}."), ("r² − 5s", r_ * r_ - 5 * s_, f"({fmt(r_)})² = {r_ * r_}; 5s = {5 * s_}; {r_ * r_} − {5 * s_} = {fmt(r_ * r_ - 5 * s_)}."), ("rs/6", r_ * s_ / 6, f"rs = {fmt(r_ * s_)}; ÷ 6 = {fmt(r_ * s_ / 6)}.")][k]
    return N(f"Work out the value of {q[0]} when r = {fmt(r_)} and s = {s_}.", q[1], d="H", reason=q[2])
K(2, "2.2", _sub, [(-4, 3, 0), (-4, 3, 1), (-4, 3, 2)], lambda r: r.choice([(-2, 3), (-6, 2), (-3, 4), (-6, 5), (-2, 9)]) + (r.randint(0, 2),))
K(2, "2.2", lambda C: N(f"The formula F = 1.8C + 32 changes a temperature in °C to °F. Work out F when C = {fmt(C)}.", 1.8 * C + 32, reason=f"1.8 × {sg(C)} + 32 = {fmt(1.8 * C + 32)}."), [25, -10], lambda r: r.choice([15, 30, -5, 40, -20, 5, 35]))
def _taxi(a, b, k, part):
    if part == 0: return X(f"A taxi charges {fmt(a)} dong to start a trip plus {fmt(b)} dong for every kilometre. Write a formula for the total cost, T dong, for a trip of k km.", f"{a}+{b}k", vars="k", lhs="T", show=f"{fmt(a)} + {fmt(b)}k", reason=f"T = {fmt(a)} + {fmt(b)}k.")
    return N(f"A taxi charges {fmt(a)} dong to start a trip plus {fmt(b)} dong for every kilometre. Work out the cost of a {k} km trip.", a + b * k, "dong", units=["dong"], d="H", reason=f"T = {fmt(a)} + {fmt(b)} × {k} = {fmt(a + b * k)} dong.")
K(2, "2.2", _taxi, [(15000, 12000, 7.5, 0), (15000, 12000, 7.5, 1)], lambda r: (r.choice([10000, 12000, 20000]), r.choice([9000, 11000, 14000]), r.choice([4.5, 6.5, 8.5, 12.5]), r.randint(0, 1)))
K(2, "2.2", lambda a, b: X(f"Rearrange w = {a}t + {b} to make t the subject.", f"(w-{b})/{a}", vars="tw", lhs="t", d="H", reason=f"Subtract {b}, then divide by {a}: t = (w − {b}) ÷ {a}."), [(5, 3)], lambda r: (r.randint(2, 9), r.randint(1, 9)))
K(2, "2.2", lambda a: X(f"Rearrange v = u + {a}a to make u the subject.", f"v-{a}a", vars="uva", lhs="u", d="H", reason=f"Subtract {a}a from both sides: u = v − {a}a."), [9], lambda r: r.randint(2, 12))
K(2, "2.2", lambda: X("Make C the subject of F = 1.8C + 32.", "(F-32)/1.8", vars="CF", lhs="C", d="VH", reason="Subtract 32, then divide by 1.8: C = (F − 32) ÷ 1.8."), [()])
K(2, "2.3", lambda a, b: X(f"Fill in the missing term:  −{a}({b} − h) = −{a * b} + ☐", f"{a}h", vars="h", d="H", reason=f"−{a} × (−h) = +{a}h."), [(2, 5)], lambda r: (r.randint(3, 9), r.randint(2, 9)))
K(2, "2.3", lambda a, b: X(f"Fill in the missing term:  {a}t(t − {b}) = ☐ − {a * b}t", f"{a}t^2", vars="t", d="H", show=f"{a}t²", reason=f"{a}t × t = {a}t²."), [(4, 3)], lambda r: (r.randint(2, 9), r.randint(2, 9)))
K(2, "2.4", lambda a, b: N(f"Fill in the missing number:  {a}w + {a * b} = {a}(w + ☐)", b, reason=f"{a * b} ÷ {a} = {b}."), [(9, 7)], lambda r: (r.randint(3, 12), r.randint(2, 9)))
def _es(v, a, b, c, d_, e, f):   # a(bv + c) + d(ev + f)
    br = lambda m, k: f"{k} − {abs(m)}{v}".replace(" 1" + v, " " + v) if m < 0 and k > 0 else poly((m, v), (k, ''))
    return X(f"Expand and simplify {'−' if a == -1 else a}({br(b, c)}) {'+' if d_ > 0 else '−'} {abs(d_)}({br(e, f)}).", f"{a * b + d_ * e}{v}+({a * c + d_ * f})", vars=v, d="H", mustNot=["\\("], show=poly((a * b + d_ * e, v), (a * c + d_ * f, "")), reason=f"{poly((a * b, v), (a * c, ''))} and {poly((d_ * e, v), (d_ * f, ''))}; collect like terms: {poly((a * b + d_ * e, v), (a * c + d_ * f, ''))}.")
K(2, "2.3", _es, [("p", 6, 2, -5, 4, -1, 3), ("q", -1, 4, -9, -3, 1, 2)], lambda r: (lambda t: t if t[1] * t[2] + t[4] * t[5] != 0 else None)((r.choice("xyn"), r.randint(2, 7), r.randint(1, 4), nz(r, -6, 6), r.choice([2, 3, 5, -2, -3]), r.randint(1, 3), nz(r, -5, 5))))
def _es2(v, a, b, c, d_):   # av(v + b) + v(cv + d)
    return X(f"Expand and simplify {a}{v}({v} + {b}) + {v}({poly((c, v), (d_, ''))}).", f"{a + c}{v}^2+({a * b + d_}){v}", vars=v, d="H", mustNot=["\\("], show=poly((a + c, v + "²"), (a * b + d_, v)), reason=f"{a}{v}² + {a * b}{v} and {poly((c, v + '²'), (d_, v))}; collect like terms: {poly((a + c, v + '²'), (a * b + d_, v))}.")
K(2, "2.3", _es2, [("h", 2, 4, 5, -3)], lambda r: (lambda t: t if t[1] * t[2] + t[4] != 0 else None)((r.choice("xyn"), r.randint(2, 5), r.randint(2, 6), r.randint(2, 6), nz(r, -7, 7))))
K(2, "2.4", lambda v, k, a, b: X(f"Factorise fully {k * a}{v}² − {k * b}{v}.", f"{k}{v}({a}{v}-{b})", vars=v, must=["\\("], d="H", show=f"{k}{v}({a}{v} − {b})", reason=f"The HCF of the two terms is {k}{v}: {k}{v}({a}{v} − {b})."), [("t", 4, 5, 2), ("q", 7, 2, 3)],
  lambda r: (lambda k, ab: (r.choice("xyn"), k) + ab)(r.choice([2, 3, 5, 6]), r.choice([(3, 2), (5, 3), (4, 3), (7, 2), (5, 4)])))
K(2, "2.4", lambda k, a, b, c: X(f"Factorise fully {k * a}ab + {k * b}a² − {k * c}a.", f"{k}a({a}b+{b}a-{c})", vars="ab", must=["\\("], d="VH", show=f"{k}a({a}b + {b}a − {c})", reason=f"The HCF of all three terms is {k}a: {k}a({a}b + {b}a − {c})."), [(3, 3, 5, 7)], lambda r: (r.choice([2, 4, 5]),) + r.choice([(3, 2, 5), (2, 3, 7), (5, 3, 2), (3, 4, 5)]))
def _kim(nm, v, k, a, b):
    return MC(f"{nm} factorises {k * a}{v}² + {k * b}{v} as {k}({a}{v}² + {b}{v}). Why is the answer not fully factorised?", f"{v} is also a common factor. The correct answer is {k}{v}({a}{v} + {b})", [(f"{k} is not a factor of both terms", f"{k} divides {k * a} and {k * b}."), (f"The correct answer is {v}({k * a}{v} + {k * b}), because numbers stay inside", f"{k} is still a common factor inside the bracket."), (f"The correct answer is {k}{v}²({a} + {b})", f"{k * b}{v} does not contain {v}².")], d="H", reason=f"Both terms contain {k} and {v}, so the HCF is {k}{v}: {k}{v}({a}{v} + {b}).")
K(2, "2.4", _kim, [("Kim", "w", 6, 3, 2)], lambda r: (pick(r, NAMES), r.choice("xyn"), r.choice([4, 5, 7, 8])) + r.choice([(3, 2), (5, 3), (4, 3), (2, 3)]))
K(2, "2.5", lambda a, y: N(f"Solve {a} − y = {fmt(a - y)}.", y, reason=f"y = {a} − {fmt(a - y)} = {fmt(y)}."), [(23, -8)], lambda r: (r.randint(10, 30), -r.randint(2, 12)))
K(2, "2.5", lambda k, a, d_: N(f"Solve (k + {a}) ÷ {d_} = {(k + a) // d_}.", k, reason=f"k + {a} = {k + a}, so k = {k}."), [(7, 5, 4)], lambda r: (lambda d_, q, a: (d_ * q - a, a, d_))(r.randint(2, 6), r.randint(3, 8), r.randint(1, 5)))
K(2, "2.5", lambda a, b, w: N(f"Solve {a}w + {b} = {fmt(a * w + b)}.", w, d="H", reason=f"{a}w = {fmt(a * w)}, so w = {w}."), [(2.5, 1.5, 5)], lambda r: (r.choice([1.5, 2.5, 0.5, 3.5]), r.choice([0.5, 1.5, 2.5]), r.choice([2, 4, 6, 8])))
K(2, "2.5", lambda a, b, c, x: N(f"Solve {a} − {b}r = {c}r − {b * x + c * x - a}.", x, d="H", reason=f"Add {b}r and add {b * x + c * x - a}: {b * x + c * x} = {b + c}r, so r = {x}."), [(11, 3, 2, 7)], lambda r: (lambda t: t if (t[1] + t[2]) * t[3] > t[0] else None)((r.randint(5, 15), r.randint(2, 5), r.randint(2, 4), r.randint(4, 9))))
def _s31(a, b, c, e, f, x):
    rhs = a * (b * x - c) - e * (x + f)
    return N(f"Solve {a}({b}h − {c}) − {e}(h + {f}) = {fmt(rhs)}.", x, d="VH", reason=f"Expand: {a * b}h − {a * c} − {e}h − {e * f} = {fmt(rhs)}. So {a * b - e}h = {fmt(rhs + a * c + e * f)} and h = {x}.")
K(2, "2.5", _s31, [(5, 2, 3, 2, 4, 5)], lambda r: (r.randint(3, 6), r.randint(2, 3), r.randint(1, 5), r.randint(2, 4), r.randint(1, 5), r.randint(2, 8)))
def _iso(a, b, c, d_, x):   # equal sides (a·x − b), base (c·x + d)
    per = 2 * (a * x - b) + c * x + d_
    return TB(f"An isosceles triangle has two equal sides of length ({a}a − {b}) cm and a third side of length ({'' if c == 1 else c}a + {d_}) cm. The perimeter is {per} cm. Find the value of a and the lengths of the sides.", ["a", "Each equal side (cm)", "Third side (cm)"], [[B(x), B(a * x - b), B(c * x + d_)]], d="VH", skill="Algebra", reason=f"2({a}a − {b}) + ({'' if c == 1 else c}a + {d_}) = {per}, so {2 * a + c}a = {per + 2 * b - d_} and a = {x}.")
K(2, "2.5", _iso, [(3, 2, 1, 6, 5)], lambda r: (r.randint(2, 4), r.randint(1, 4), r.randint(1, 2), r.randint(2, 8), r.randint(3, 7)))
def _age(n1, n2, m, y, t):   # n1 = m × n2 now; in y years n1 = t × n2
    b = y * (t - 1) // (m - t)
    return N(f"{n1} is {m} times as old as {n2}. In {y} years' time, {n1} will be {['', '', 'twice', 'three times'][t]} as old as {n2}. Write an equation and solve it to find {n2}'s age now.", b, "years", units=["years"], d="VH", reason=f"Let {n2}'s age be b. {m}b + {y} = {t}(b + {y}), so {m - t}b = {y * (t - 1)} and b = {b}.")
K(2, "2.5", _age, [("Mai", "Bao", 4, 6, 2)], lambda r: two(r, NAMES) + r.choice([(5, 9, 2), (3, 4, 2), (6, 8, 2), (5, 4, 3), (7, 10, 3), (4, 10, 2)]))
def _sq(a, b, c, d_, k):   # sides a·c − b and c·c + d equal
    x = (b + d_) // (a - c); side = c * x + d_
    if k == 0: return N(f"The sides of a square are ({a}c − {b}) cm and ({c}c + {d_}) cm. Write an equation and solve it to find c.", x, d="H", reason=f"{a}c − {b} = {c}c + {d_}, so {a - c}c = {b + d_} and c = {x}.")
    return N(f"The sides of a square are ({a}c − {b}) cm and ({c}c + {d_}) cm. Work out the area of the square.", side * side, "cm²", units=["cm²", "cm"], d="VH", reason=f"{a}c − {b} = {c}c + {d_} gives c = {x}. The side is {side} cm, so the area is {side}² = {side * side} cm².")
K(2, "2.5", _sq, [(7, 12, 3, 8, 0), (7, 12, 3, 8, 1)], lambda r: (lambda a, c, x, d_: (a, (a - c) * x - d_, c, d_, r.randint(0, 1)) if (a - c) * x - d_ > 0 else None)(r.randint(5, 8), r.randint(2, 4), r.randint(3, 7), r.randint(1, 9)))
def _nl(lo, hi, lc, hc, v):
    f = lambda a, c, b: f"{fmt(a)} {'≤' if c else '<'} {v} {'≤' if b else '<'}"
    right = f"{fmt(lo)} {'≤' if lc else '<'} {v} {'≤' if hc else '<'} {fmt(hi)}"
    wr = [f"{fmt(lo)} {'<' if lc else '≤'} {v} {'<' if hc else '≤'} {fmt(hi)}", f"{fmt(lo)} {'≤' if lc else '<'} {v} {'<' if hc else '≤'} {fmt(hi)}", f"{fmt(lo)} {'<' if lc else '≤'} {v} {'≤' if hc else '<'} {fmt(hi)}"]
    return MC(f"Which inequality is shown on the number line? Use the letter {v}.", right, [(w, "A filled circle means the value is included (≤); an open circle means it is not (<).") for w in wr], d="H", fig={"kind": "numline", "min": int(lo) - 2, "max": int(hi) + 2, "minor": 2, "from": {"v": lo, "closed": lc}, "to": {"v": hi, "closed": hc}}, reason=f"Filled circle = included, open circle = not included: {right}.")
K(2, "2.6", _nl, [(-2, 1.5, True, False, "t")], lambda r: (-r.randint(1, 4), r.choice([0.5, 1.5, 2.5, 2, 3]), r.random() < .5, r.random() < .5, r.choice("xnk")))
def _show(lo, hi, lc, hc, v):
    oc = lambda c: "a filled circle" if c else "an open circle"
    return MC(f"How do you show {fmt(lo)} {'≤' if lc else '<'} {v} {'≤' if hc else '<'} {fmt(hi)} on a number line?", f"{oc(lc).capitalize()} at {fmt(lo)}, {oc(hc)} at {fmt(hi)}, and a line joining them", [(f"{oc(not lc).capitalize()} at {fmt(lo)}, {oc(not hc)} at {fmt(hi)}, and a line joining them", "≤ needs a filled circle and < needs an open circle."), (f"{oc(lc).capitalize()} at {fmt(lo)} with an arrow to the left, {oc(hc)} at {fmt(hi)} with an arrow to the right", "The values are between the two numbers."), (f"Filled circles at {fmt(lo)} and {fmt(hi)} only, with no line", "Every value between them is included, so draw the line.")], reason="Open circle: the end value is not included. Filled circle: it is included.")
K(2, "2.6", _show, [(0.5, 4, False, True, "k")], lambda r: (lambda lc: (-r.randint(1, 3) + 0.5, r.randint(1, 5), lc, not lc, r.choice("xnt")))(r.random() < .5))
def _ints(lo, hi, lc, hc):
    import math as _m
    s = _m.ceil(lo) if (lc or lo != int(lo)) else int(lo) + 1; L = _m.floor(hi) if (hc or hi != int(hi)) else int(hi) - 1
    return TB(f"q is an integer and {fmt(lo)} {'≤' if lc else '<'} q {'≤' if hc else '<'} {fmt(hi)}. Complete the table.", ["Smallest integer", "Largest integer", "How many integers"], [[B(s), B(L), B(L - s + 1)]], d="H", skill="Reasoning", reason="The integers are " + ", ".join(fmt(i) for i in range(s, L + 1)) + ".")
K(2, "2.6", _ints, [(-6, -1, True, False), (-1.5, 3.2, False, True)], lambda r: (lambda lo: (lo, lo + r.choice([3.5, 4, 4.7, 6])  , r.random() < .5, r.random() < .5))(r.choice([-5, -3.5, -2.2, -4, -0.5])))

# ================================================================= Unit 5 · angles and constructions
DEG = dict(unit="°", units=["°"])
K(5, "5.1", lambda a, b, k: N(f"Four angles meet at a point. They are {a}°, x°, {k}x° and {b}°. Work out the value of x.", (360 - a - b) // (k + 1), d="H", reason=f"Angles at a point add up to 360°: {a} + x + {k}x + {b} = 360, so {k + 1}x = {360 - a - b} and x = {(360 - a - b) // (k + 1)}."), [(95, 85, 2)],
  lambda r: (lambda k, x, a: (a, 360 - a - (k + 1) * x, k) if 20 < 360 - a - (k + 1) * x < 170 else None)(r.choice([2, 3, 4]), r.randint(25, 50), r.choice([70, 80, 95, 105, 110])))
def _cross(a):
    return TB(f"Two straight lines cross. One of the angles is {a}°. Angle a is vertically opposite this angle and angle b is next to it on a straight line. Work out a and b.", ["a (°)", "b (°)"], [[B(a), B(180 - a)]], reason=f"a = {a}° (vertically opposite angles are equal). b = 180 − {a} = {180 - a}° (angles on a straight line add up to 180°).")
K(5, "5.1", _cross, [47], lambda r: r.choice([38, 52, 64, 71, 109, 126, 143]))
_REL = [("in matching positions at the two crossings (an F shape)", "corresponding angles"), ("between the parallel lines on opposite sides of the transversal (a Z shape)", "alternate angles"), ("opposite each other where two lines cross (an X shape)", "vertically opposite angles")]
K(5, "5.1", lambda i: MC(f"Two parallel lines are crossed by a straight line. Two angles are {_REL[i][0]}. What are they called?", _REL[i][1], [(x[1], "Look at the shape the angles make.") for j, x in enumerate(_REL) if j != i] + [("co-interior angles", "Co-interior angles are between the parallel lines on the same side (a C shape) and add up to 180°.")], reason=f"Angles {_REL[i][0]} are {_REL[i][1]}; they are equal."), [0, 1, 2], lambda r: r.randint(0, 2))
K(5, "5.1", lambda p: N(f"Two parallel lines are crossed by a straight line. Angle p = {p}°. Angle t is corresponding to p, and angle w is vertically opposite t. Work out angle w.", p, d="H", reason=f"t = {p}° (corresponding angles are equal) and w = t = {p}° (vertically opposite angles are equal).", **DEG), [118], lambda r: r.choice([52, 67, 74, 105, 112, 131]))
def _pq(x, k):
    if k == 0: return N(f"PQ is parallel to RS. A straight line crosses PQ at an angle of {x}° and crosses RS at angle x, which is corresponding to it. Write down the value of x.", x, reason=f"Corresponding angles are equal, so x = {x}°.", **DEG)
    return N(f"PQ is parallel to RS. A straight line crosses RS making an angle of {x}°. Angle y is next to this angle on the straight line RS. Work out the value of y.", 180 - x, reason=f"Angles on a straight line add up to 180°: y = 180 − {x} = {180 - x}°.", **DEG)
K(5, "5.1", _pq, [(108, 0), (108, 1)], lambda r: (r.choice([64, 77, 96, 115, 123, 132]), r.randint(0, 1)))
K(5, "5.1", lambda b, c: N(f"A triangle is drawn between two parallel lines, with one vertex on the top line and its base on the bottom line. The base angles of the triangle are {b}° and {c}°. At the top vertex, the straight line is split into three angles: b, a and c, where a is the angle inside the triangle. Work out a.", 180 - b - c, d="H", reason=f"b = {b}° and c = {c}° (alternate angles). Angles on a straight line: a = 180 − {b} − {c} = {180 - b - c}°.", **DEG),
  [(58, 71)], lambda r: (r.randint(40, 65), r.randint(50, 75)))
K(5, "5.2", lambda: MC("In triangle ABC the angles are p, q and r. Side BC is extended to D, and s is the exterior angle next to r. Which working shows that s = p + q?", "r + s = 180° (straight line) and p + q + r = 180° (triangle), so s = p + q",
  [("p + q + r + s = 360° (angles at a point), so s = p + q", "The four angles do not meet at one point."), ("s = r because they are vertically opposite, so s = p + q", "s and r are on a straight line; they are not vertically opposite."), ("s = 180° − p − q because angles in a triangle add up to 180°", "That gives r, not s.")], d="H", reason="r + s = 180° and p + q + r = 180°. Both equal 180°, so s = p + q: the exterior angle equals the sum of the two interior opposite angles."), [()])
def _isos(e, k):
    base = 180 - e
    if k == 0: return N(f"In triangle PQR, PQ = PR. QRS is a straight line and angle PRS = {e}°. Work out the size of angle PRQ.", base, reason=f"Angles on a straight line: 180 − {e} = {base}°.", **DEG)
    return N(f"In triangle PQR, PQ = PR. QRS is a straight line and angle PRS = {e}°. Work out the size of angle QPR.", 180 - 2 * base, d="H", reason=f"PRQ = 180 − {e} = {base}°. The triangle is isosceles, so PQR = {base}°. QPR = 180 − 2 × {base} = {180 - 2 * base}°.", **DEG)
K(5, "5.2", _isos, [(118, 0), (118, 1)], lambda r: (r.choice([104, 110, 122, 126, 131, 137]), r.randint(0, 1)))
def _tri50(a):
    rest = 180 - a
    rows = [("The triangle is equilateral.", "Cannot be true"), ("The triangle is isosceles.", "Might be true"), ("The triangle has at least one other acute angle.", "Must be true"), (f"The other two angles are each greater than {rest // 2 + 5}°.", "Cannot be true")]
    return GD(f"One of the angles in a triangle is {a}°. Decide whether each statement must be true, cannot be true or might be true.", "Statement", rows, extra=["Must be true", "Cannot be true", "Might be true"], d="VH", skill="Reasoning", reason=f"The other two angles add up to {rest}°. An equilateral triangle has three 60° angles. Two angles that add to {rest}° cannot both be more than {rest // 2}°, and they cannot both be 90° or more.")
K(5, "5.2", _tri50, [50], lambda r: r.choice([40, 70, 80, 44, 76]))
K(5, "5.2", lambda a, b, m, n: N(f"The angles of a quadrilateral are {m}x°, {n}x°, {a}° and {b}°. Work out the value of x.", (360 - a - b) // (m + n), d="H", reason=f"Angles in a quadrilateral add up to 360°: {m + n}x = {360 - a - b}, so x = {(360 - a - b) // (m + n)}."), [(85, 95, 2, 3)],
  lambda r: (lambda m, n, x, a: (a, 360 - a - (m + n) * x, m, n) if 40 < 360 - a - (m + n) * x < 160 else None)(2, r.choice([3, 4]), r.randint(22, 40), r.choice([70, 80, 100, 110, 120])))
K(5, "5.2", lambda a: N(f"KLMN is a parallelogram and NPQ is an isosceles triangle with NP = NQ. MNQ and KNP are straight lines. Angle LMN = {a}°. Work out the size of angle NPQ.", a // 2, d="VH", reason=f"Angle MNK = 180 − {a} = {180 - a}° (neighbouring angles of a parallelogram add up to 180°). Angle PNQ = {180 - a}° (vertically opposite). NPQ = (180 − {180 - a}) ÷ 2 = {a // 2}°.", **DEG), [64], lambda r: r.choice([48, 56, 72, 78, 84, 52]))
def _lan(nm, L, rad):
    return MC(f"{nm} wants to construct the perpendicular bisector of a line PQ that is {L} cm long. {nm} draws an arc of radius {rad} cm with centre P and an arc of radius {rad} cm with centre Q. Why does this method not work?", f"The arcs do not meet, because {rad} + {rad} = {2 * rad} cm is less than {L} cm. The radius must be more than {L / 2:g} cm", [("The two arcs must have different radii", "The radii must be equal, so the crossing points are the same distance from P and Q."), (f"The arcs should be drawn from the midpoint of PQ", "The midpoint is what the construction finds."), (f"The radius must be exactly {L / 2:g} cm", "Then the arcs only touch at one point on the line; they must cross above and below it.")], d="H", reason=f"The arcs only cross if the radius is more than half of PQ, that is more than {L / 2:g} cm.")
K(5, "5.3", _lan, [("Lan", 8, 3)], lambda r: (pick(r, NAMES),) + r.choice([(10, 4), (9, 4), (12, 5), (7, 3), (11, 5)]))
K(5, "5.3", lambda L: MC(f"Line AB is {L} cm long. You construct its perpendicular bisector with compasses. Which radius can you use for the arcs from A and from B?", f"{L / 2 + 1:g} cm", [(f"{L / 2:g} cm", "With exactly half the length the arcs only touch."), (f"{L / 2 - 1:g} cm", "Too short: the arcs do not meet."), (f"{L / 2 - 2:g} cm", "Too short: the arcs do not meet.")], reason=f"The radius must be more than half of AB ({L / 2:g} cm). The bisector crosses AB at 90°, {L / 2:g} cm from A."), [7], lambda r: r.choice([6, 8, 9, 10, 11]))
def _sss(a, b, c):
    import math as _m
    ang = _m.degrees(_m.acos((a * a + c * c - b * b) / (2 * a * c)))
    return N(f"Use a ruler and compasses to make an accurate drawing of triangle XYZ with XY = {a} cm, XZ = {b} cm and YZ = {c} cm. Measure angle XYZ on your drawing.", round(ang), tol=2.5, d="H", reason=f"Draw XY = {a} cm, then arcs of radius {b} cm from X and {c} cm from Y. Angle XYZ is about {round(ang)}°.", **DEG)
K(5, "5.3", _sss, [(7, 6, 5)], lambda r: r.choice([(8, 6, 5), (6, 5, 4), (9, 7, 6), (7, 5, 4), (8, 7, 5)]))
def _sas(g, gf, gh):
    import math as _m
    fh = _m.sqrt(gf * gf + gh * gh - 2 * gf * gh * _m.cos(_m.radians(g)))
    return N(f"Use a ruler and a protractor to make an accurate drawing of triangle FGH with GH = {gh} cm, angle G = {g}° and GF = {gf} cm. Measure the length of side FH on your drawing.", round(fh, 1), "cm", units=["cm", "mm"], tol=0.25, d="H", reason=f"Draw GH, measure {g}° at G, mark F {gf} cm from G and join F to H. FH is about {round(fh, 1)} cm.")
K(5, "5.3", _sas, [(42, 6.5, 5.5)], lambda r: (r.choice([35, 50, 55, 64, 70]), r.choice([5, 6, 7.5]), r.choice([4.5, 6, 8])))

# ================================================================= Unit 8 · shapes and symmetry
_QS = [("All squares are rhombuses.", True), ("All rectangles are squares.", False), ("All rhombuses are parallelograms.", True), ("All kites are rhombuses.", False), ("All squares are rectangles.", True), ("All parallelograms are rectangles.", False), ("All rectangles are parallelograms.", True), ("All trapeziums are parallelograms.", False), ("All rhombuses are kites.", True), ("All parallelograms are rhombuses.", False)]
K(8, "8.1", lambda rows: MS("Select every correct statement about quadrilaterals.", [t for t, ok in rows if ok], [t for t, ok in rows if not ok], d="H", reason="A special quadrilateral has all the properties of the more general one: for example a square has four equal sides, so it is a rhombus."), [(_QS[:4],)], lambda r: (r.sample(_QS[4:8], 2) + r.sample(_QS[8:] + _QS[4:6], 2),) if False else (_QS[4:8],) if r.random() < .5 else (_QS[6:10],))
_QN = [("Exactly one pair of parallel sides", "Trapezium"), ("Four equal sides, but the angles are not right angles", "Rhombus"), ("Two pairs of equal adjacent sides, exactly one line of symmetry", "Kite"), ("Equal diagonals and exactly two lines of symmetry", "Rectangle"), ("Four equal sides and four right angles", "Square"), ("Two pairs of parallel sides, no lines of symmetry", "Parallelogram")]
K(8, "8.1", lambda rows: MT("Match each property to the quadrilateral that has it.", rows, reason="; ".join(f"{b}: {a.lower()}" for a, b in rows) + "."), [(_QN[:4],)], lambda r: (r.sample(_QN, 4),))
_POLY = {3: "equilateral triangle", 5: "regular pentagon", 6: "regular hexagon", 8: "regular octagon", 9: "regular nonagon", 10: "regular decagon"}
K(8, "8.1", lambda n, k: [N(f"How many lines of symmetry does a {_POLY[n]} have?", n, reason=f"A regular polygon with {n} sides has {n} lines of symmetry."), N(f"Write down the order of rotational symmetry of a {_POLY[n]}.", n, reason=f"It fits onto itself {n} times in one full turn."), N(f"A regular polygon has exactly {n} lines of symmetry. How many sides does it have?", n, d="H", reason=f"A regular polygon has the same number of lines of symmetry as sides: {n}.")][k],
  [(6, 0), (6, 1), (8, 2)], lambda r: (r.choice([5, 9, 10, 3]), r.randint(0, 2)))
K(8, "8.2", lambda d_: N(f"Work out the circumference of a circle with a diameter of {d_} cm. Use π = 3.14.", round(3.14 * d_, 2), "cm", units=["cm", "cm²"], tol=0.01, reason=f"C = πd = 3.14 × {d_} = {fmt(round(3.14 * d_, 2))} cm."), [15], lambda r: r.choice([12, 25, 8, 35, 45, 6.5]))
def _fount(C, thing):
    import math as _m
    d_ = round(C / _m.pi * 100)
    return N(f"A circular {thing} has a circumference of {C} m. Calculate its diameter. Use the π button on your calculator. Give your answer in centimetres, correct to the nearest centimetre.", d_, "cm", units=["cm", "m"], tol=0.5, d="H", reason=f"d = C ÷ π = {C} ÷ π = {C / _m.pi:.4f} m = {d_} cm.")
K(8, "8.2", _fount, [(6.8, "fountain")], lambda r: (r.choice([5.4, 7.5, 9.2, 4.6, 12.5]), r.choice(["pond", "flower bed", "table", "trampoline"])))
def _fence(nm, d_, rate, day, days):
    import math as _m
    per = _m.pi * d_ / 2 + d_; tot = per * rate + day * days
    return N(f"{nm} has a flower bed in the shape of a semicircle with a diameter of {d_} m. A builder puts a fence around the whole edge of the flower bed. The cost is ${rate:.2f} per metre of fence plus ${day} for each day of work. The builder takes {days} days. Work out the total cost. Use the π button on your calculator.", round(tot, 2), "$", units=["$"], tol=0.06, d="VH", reason=f"Perimeter = π × {d_} ÷ 2 + {d_} = {per:.3f} m. Fence: {per:.3f} × {rate:.2f} = ${per * rate:.2f}. Work: {days} × {day} = ${day * days}. Total ${tot:.2f}.")
K(8, "8.2", _fence, [("Mr Khoa", 24, 9.5, 85, 3)], lambda r: (r.choice(["Ms Hana", "Mr Omar", "Ms Zara"]), r.choice([16, 18, 20, 30]), r.choice([7.5, 8.5, 12.5]), r.choice([70, 90, 95]), r.choice([2, 3, 4])))
K(8, "8.2", lambda s, w: MC(f"A school running track has two straight sections of {s} m and two semicircular ends. The track is {w} m wide. What is the distance around the track, in terms of π?", f"({2 * s} + {w}π) m", [(f"({2 * s} + {2 * w}π) m", f"The two semicircles make one circle of diameter {w} m, so its circumference is {w}π."), (f"({s} + {w}π) m", "There are two straight sections."), (f"({2 * s} + {w // 2}π) m", f"Circumference = π × diameter = {w}π.")], d="H", reason=f"Straight sections: 2 × {s} = {2 * s} m. The two semicircles make one circle of diameter {w} m: {w}π m."), [(95, 40)], lambda r: (r.choice([80, 85, 90, 100, 110]), r.choice([30, 36, 50, 60])))
_FVE = [("Square-based pyramid", 5, 5, 8), ("Pentagonal prism", 7, 10, 15), ("Cuboid", 6, 8, 12), ("Triangular prism", 5, 6, 9), ("Hexagonal prism", 8, 12, 18), ("Triangular-based pyramid", 4, 4, 6), ("Cube", 6, 8, 12), ("Pentagonal-based pyramid", 6, 6, 10)]
K(8, "8.3", lambda rows: TB("Complete the table showing the number of faces, vertices and edges of these 3D shapes.", ["3D shape", "Faces (F)", "Vertices (V)", "Edges (E)"], [[n, B(f), B(v), B(e)] for n, f, v, e in rows], reason="; ".join(f"{n}: {f}, {v}, {e}" for n, f, v, e in rows) + ". In each case E = F + V − 2."), [(_FVE[:3],)], lambda r: (r.sample(_FVE[3:], 3),))
K(8, "8.3", lambda: MC("Which formula connects the number of faces (F), vertices (V) and edges (E) of a 3D shape with flat faces?", "E = F + V − 2", [("E = F + V", "Test it on a cube: 6 + 8 is not 12."), ("E = F × V ÷ 2", "Test it on a cube: 6 × 8 ÷ 2 is not 12."), ("E = F + V + 2", "Test it on a cube: 6 + 8 + 2 is not 12.")], reason="For a cube, F = 6, V = 8 and E = 12: 6 + 8 − 2 = 12. This is Euler's formula."), [()])
K(8, "8.3", lambda v: TB(f"A triangular prism has 6 vertices, 5 faces and 9 edges. A different prism has {v} vertices. Work out its number of edges and faces.", ["Edges", "Faces"], [[B(3 * v // 2), B(v // 2 + 2)]], d="VH", skill="Reasoning", reason=f"{v} vertices means {v // 2} on each end, so the ends have {v // 2} sides. Edges = 3 × {v // 2} = {3 * v // 2}. Faces = {v // 2} + 2 = {v // 2 + 2}."), [16], lambda r: r.choice([10, 12, 14, 18, 20]))

# ================================================================= Unit 10 · percentages
def pc(x): return fmt(float(D(str(x))))
K(10, "10.1", lambda p, a, u: N(f"Find {pc(p)}% of {fmt(a)} {u}.", float(D(str(p)) * D(str(a)) / 100), u, units=[u], reason=f"{pc(p)}% = {pc(D(str(p)) / 100)}; {pc(D(str(p)) / 100)} × {fmt(a)} = {pc(D(str(p)) * D(str(a)) / 100)} {u}."), [(240, 35, "kg"), (0.8, 2500, "mL")], lambda r: (r.choice([130, 250, 0.5, 0.4, 175, 1.5]), r.choice([40, 60, 1200, 3000, 80]), r.choice(["kg", "mL", "m", "g"])))
K(10, "10.1", lambda tot, k, what: N(f"In a park there are {tot} trees. {k} of them are {what} trees. What percentage of the trees are {what} trees?", k / tot * 100, "%", units=["%"], reason=f"{k} ÷ {tot} × 100 = {fmt(k / tot * 100)}%."), [(45, 27, "mango")], lambda r: r.choice([(60, 21), (80, 28), (75, 48), (40, 14), (120, 54)]) + (r.choice(["palm", "apple", "orange", "pine"]),))
K(10, "10.1", lambda a, b, av, bv: N(f"Write {a} as a percentage of {b}.", av / bv * 100, "%", units=["%"], d="H", reason=f"Use the same units: {fmt(av)} ÷ {fmt(bv)} × 100 = {fmt(av / bv * 100)}%."), [("2.4 kg", "800 g", 2400, 800), ("18 minutes", "2 hours", 18, 120)],
  lambda r: r.choice([("1.5 kg", "600 g", 1500, 600), ("45 minutes", "3 hours", 45, 180), ("36 cm", "1.2 m", 36, 120), ("3.6 litres", "900 mL", 3600, 900), ("24 seconds", "2 minutes", 24, 120)]))
K(10, "10.2", lambda p: N(f"To decrease a value by {p}% you multiply by a decimal. Write the decimal.", (100 - p) / 100, reason=f"100% − {p}% = {100 - p}% = {pc((100 - p) / 100)}."), [12], lambda r: r.choice([8, 15, 24, 35, 4, 45]))
K(10, "10.2", lambda m: N(f"Multiplying a value by {m} decreases it by what percentage?", round(100 - m * 100, 6), "%", units=["%"], reason=f"{m} = {fmt(m * 100)}%, and 100% − {fmt(m * 100)}% = {fmt(round(100 - m * 100, 6))}%."), [0.65], lambda r: r.choice([0.85, 0.7, 0.92, 0.55, 0.4]))
K(10, "10.1", lambda a, p: N(f"When {a} is increased by {p}%, what is the absolute change?", a * p / 100, d="H", reason=f"The absolute change is {p}% of {a} = {fmt(a * p / 100)}."), [(450, 60)], lambda r: (r.choice([250, 360, 800, 1200]), r.choice([15, 35, 40, 70])))
def _incdec(a, p, up):
    m = D(100) + D(str(p)) if up else D(100) - D(str(p)); v = D(str(a)) * m / 100
    return N(f"{'Increase' if up else 'Decrease'} {fmt(a)} by {pc(p)}%.", float(v), reason=f"Multiply by {pc(m / 100)}: {fmt(a)} × {pc(m / 100)} = {pc(v)}.")
K(10, "10.2", _incdec, [(1250, 8, True), (96, 62.5, False), (3400, 0.5, True)], lambda r: (r.choice([640, 1500, 2800, 88, 720]), r.choice([6, 12.5, 37.5, 0.5, 15, 2.5]), r.random() < .5))
K(10, "10.2", lambda price, p, thing: N(f"A {thing} costs {fmt(price)} VND. Next month the price will rise by {p}%. Work out the new price.", price * (100 + p) // 100, "VND", units=["VND"], d="H", reason=f"{fmt(price)} × {pc((100 + p) / 100)} = {fmt(price * (100 + p) // 100)} VND."), [(3200000, 7, "bicycle")], lambda r: (r.choice([2400000, 4500000, 1800000, 5600000]), r.choice([4, 6, 9, 12]), r.choice(["phone", "desk", "guitar", "scooter"])))
K(10, "10.1", lambda cost, sell, thing: N(f"A bakery spends ${cost} making a batch of {thing}. It sells the whole batch for ${sell}. Work out the percentage loss.", (cost - sell) / cost * 100, "%", units=["%"], d="H", reason=f"Loss = ${cost - sell}. {cost - sell} ÷ {cost} × 100 = {fmt((cost - sell) / cost * 100)}%."), [(125, 95, "birthday cakes")], lambda r: r.choice([(80, 68), (150, 126), (60, 51), (250, 190), (40, 31)]) + (r.choice(["biscuits", "bread rolls", "muffins"]),))
K(10, "10.1", lambda a, b: N(f"The population of a small town fell from {fmt(a)} to {fmt(b)}. Work out the percentage decrease in the population.", (a - b) / a * 100, "%", units=["%"], d="H", reason=f"Decrease = {fmt(a - b)}. {fmt(a - b)} ÷ {fmt(a)} × 100 = {fmt((a - b) / a * 100)}%."), [(64000, 52800)], lambda r: r.choice([(48000, 42000), (25000, 21500), (80000, 69000), (36000, 30600), (12500, 11000)]))
K(10, "10.2", lambda nm, old, p: N(f"{nm}'s electricity bill increased by {p}%. The new bill is ${old * (100 + p) / 100:.2f}. How much was the bill before the increase?", old, "$", units=["$"], d="VH", reason=f"New = old × {pc((100 + p) / 100)}, so old = {old * (100 + p) / 100:.2f} ÷ {pc((100 + p) / 100)} = ${old}."), [("Phuc", 60, 12)], lambda r: (pick(r, NAMES), r.choice([40, 50, 75, 80, 90]), r.choice([8, 15, 16, 24])))
def _stamp(v, p, yrs):
    out = v * (1 + p / 100) ** yrs
    return N(f"The value of a stamp collection increases by {p}% every year. Its value now is ${fmt(v)}. Find its value after {'one year' if yrs == 1 else 'two years'}.", round(out, 2), "$", units=["$"], tol=0.005, d="H" if yrs == 2 else "M", reason=f"Multiply by {pc(1 + p / 100)} each year: " + (f"${fmt(round(v * (1 + p / 100), 2))}" if yrs == 1 else f"${fmt(round(v * (1 + p / 100), 2))}, then ${fmt(round(out, 2))}") + ".")
K(10, "10.2", _stamp, [(8000, 5, 1), (8000, 5, 2)], lambda r: (r.choice([2000, 5000, 6000, 12000]), r.choice([4, 10, 20, 15]), r.randint(1, 2)))
K(10, "10.1", lambda p, f, k, a, b, c: N(f"In a school library, {p}% of the books are {a} and 1/{f} of the books are {b}. The remaining {k} books are {c}. How many books are in the library altogether?", round(k / (1 - p / 100 - 1 / f)), d="VH", reason=f"{p}% + {fmt(100 / f)}% = {fmt(p + 100 / f)}%, so {fmt(100 - p - 100 / f)}% = {k} books. 100% = {round(k / (1 - p / 100 - 1 / f))} books."), [(45, 4, 270, "novels", "science books", "history books")],
  lambda r: (lambda p, f, tot: (p, f, round(tot * (1 - p / 100 - 1 / f)), "novels", "science books", "history books"))(r.choice([35, 40, 55]), r.choice([4, 5]), r.choice([600, 800, 1200, 400])))
K(10, "10.2", lambda s, p: N(f"A square photo has sides of {s} cm. Each side is reduced by {p}% to fit in a frame. Find the percentage decrease in the area of the photo.", round(100 - (100 - p) ** 2 / 100, 6), "%", units=["%"], d="VH", reason=f"Each side is multiplied by {pc((100 - p) / 100)}, so the area is multiplied by {pc((100 - p) / 100)}² = {pc((100 - p) ** 2 / 10000)}. Decrease = {fmt(round(100 - (100 - p) ** 2 / 100, 6))}%."), [(15, 30)], lambda r: (r.choice([10, 20, 25, 40]), r.choice([10, 20, 40, 50])))

# ================================================================= Unit 12 · ratio and proportion
def RT(prompt, parts, **kw):
    a = ":".join(str(p) for p in parts)
    return S(prompt + " Type your answer like 3:4.", [a, "/^\\s*" + "\\s*:\\s*".join(str(p) for p in parts) + "\\s*$/"], hint="Use the same units, then divide every part by the highest common factor.", **kw)
def _simp(txt, vals, why=""):
    g = 0
    for v in vals: g = gcd(g, v)
    parts = [v // g for v in vals]
    return RT(f"Simplify the ratio {txt}.", parts, d="H" if why else "M", reason=(why + " " if why else "") + f"Divide by {g}: " + " : ".join(str(p) for p in parts) + ".")
K(12, "12.1", _simp, [("35 : 56 : 21", [35, 56, 21]), ("3 hours : 50 minutes", [180, 50], "3 hours = 180 minutes."), ("1.2 kg : 450 g : 75 g", [1200, 450, 75], "1.2 kg = 1200 g."), ("0.25 : 1.5 : 0.75", [25, 150, 75], "Multiply every part by 100 to make whole numbers."), ("2 1/2 litres : 750 mL", [2500, 750], "2 1/2 litres = 2500 mL.")],
  lambda r: r.choice([("24 : 60 : 36", [24, 60, 36]), ("2 hours : 45 minutes", [120, 45], "2 hours = 120 minutes."), ("1.5 kg : 600 g : 150 g", [1500, 600, 150], "1.5 kg = 1500 g."), ("0.4 : 1.2 : 0.6", [4, 12, 6], "Multiply every part by 10."), ("1 1/2 litres : 250 mL", [1500, 250], "1 1/2 litres = 1500 mL."), ("42 : 28 : 70", [42, 28, 70]), ("4 m : 80 cm", [400, 80], "4 m = 400 cm.")]))
def _div(tot, parts, u, thing):
    one = D(str(tot)) / sum(parts)
    return TB(f"Divide {tot} {u} of {thing} in the ratio {' : '.join(str(p) for p in parts)}.", [f"Share {i + 1} ({u})" for i in range(len(parts))], [[B(float(one * p)) for p in parts]], skill="Reasoning", reason=f"{tot} ÷ {sum(parts)} = {pc(one)} for one part: " + ", ".join(f"{pc(one * p)} {u}" for p in parts) + ".")
K(12, "12.2", _div, [(3.5, [3, 4], "kg", "rice"), (2.7, [1, 3, 5], "m", "ribbon")], lambda r: r.choice([(4.5, [2, 7], "kg", "flour"), (3.6, [1, 2, 3], "m", "rope"), (5.6, [3, 5], "litres", "juice"), (4.8, [1, 2, 5], "kg", "sand")]))
def _tri(parts, k):
    one = 180 // sum(parts); ang = [p * one for p in parts]
    if k == 0: return TB(f"The angles in a triangle are in the ratio {' : '.join(map(str, parts))}. Work out the size of each angle.", ["Smallest (°)", "Middle (°)", "Largest (°)"], [[B(a) for a in sorted(ang)]], d="H", skill="Reasoning", reason=f"180° ÷ {sum(parts)} = {one}°: " + ", ".join(f"{a}°" for a in ang) + ".")
    kind = "Right-angled" if max(ang) == 90 else "Obtuse-angled" if max(ang) > 90 else "Acute-angled"
    return MC(f"The angles in a triangle are in the ratio {' : '.join(map(str, parts))}. What type of triangle is it?", f"{kind}, because the largest angle is {max(ang)}°", [(f"{x}, because the largest angle is {max(ang)}°", f"{max(ang)}° is not that kind of angle.") for x in ("Right-angled", "Obtuse-angled", "Acute-angled") if x != kind] + [("Equilateral, because the angles are in a ratio", "An equilateral triangle has angles in the ratio 1 : 1 : 1.")], d="H", reason=f"The angles are {', '.join(f'{a}°' for a in ang)}.")
K(12, "12.2", _tri, [([4, 5, 9], 0), ([4, 5, 9], 1)], lambda r: (r.choice([[2, 3, 4], [1, 2, 3], [2, 3, 5], [1, 3, 5], [3, 4, 5], [1, 1, 4], [2, 5, 11]]), r.randint(0, 1)))
K(12, "12.2", lambda a, b, diff, A, B_: N(f"In a school orchestra the ratio of {A} players to {B_} players is {a} : {b}. There are {diff} more {A} players than {B_} players. How many {A} and {B_} players are there altogether?", diff // (a - b) * (a + b), d="VH", reason=f"The difference is {a - b} parts = {diff}, so 1 part = {diff // (a - b)}. Total = {a + b} × {diff // (a - b)} = {diff // (a - b) * (a + b)}."), [(7, 2, 15, "violin", "cello")],
  lambda r: (lambda a, b, k: (a, b, (a - b) * k) + two(r, ["violin", "cello", "flute", "trumpet", "drum"]))(*r.choice([(5, 2), (7, 3), (8, 3), (9, 4), (5, 3)]), r.randint(2, 6)))
def _fruit12(a, b, lo, hi, A, B_):
    t = [n for n in range(lo + 1, hi) if n % (a + b) == 0]; assert len(t) == 1, (a, b, lo, hi)
    return N(f"A fruit seller has {A} and {B_} in the ratio {a} : {b}. She has more than {lo} but fewer than {hi} fruits altogether. How many {B_} does she have?", t[0] // (a + b) * b, d="VH", reason=f"The total is a multiple of {a + b} between {lo} and {hi}: {t[0]}. {B_.capitalize()} = {t[0]} ÷ {a + b} × {b} = {t[0] // (a + b) * b}.")
K(12, "12.2", _fruit12, [(5, 8, 50, 60, "mangoes", "papayas")], lambda r: r.choice([(4, 7, 40, 50), (3, 8, 60, 70), (5, 9, 50, 60), (7, 10, 60, 70), (4, 11, 40, 50)]) + two(r, ["mangoes", "papayas", "oranges", "pears", "guavas"]))
def _conc(parts, tot, cost, per):
    one = D(str(tot)) / sum(parts); sand = one * parts[1]
    return N(f"Mr Long is making concrete. He mixes cement, sand, gravel and water so that their masses are in the ratio cement : sand : gravel : water = {' : '.join(map(str, parts))}. He needs {tot} kg of concrete altogether. Sand costs ${cost:.2f} for {per} kg. Work out the cost of the sand he needs.", float(sand / per * D(str(cost))), "$", units=["$"], tol=0.005, d="VH", reason=f"{sum(parts)} parts = {tot} kg, so 1 part = {pc(one)} kg. Sand = {pc(sand)} kg. Cost = {pc(sand)} ÷ {per} × ${cost:.2f} = ${float(sand / per * D(str(cost))):.2f}.")
K(12, "12.3", _conc, [([2, 5, 6, 1], 35, 0.9, 5)], lambda r: r.choice([([1, 3, 5, 1], 40, 1.2, 4), ([2, 4, 5, 1], 60, 0.8, 5), ([1, 2, 4, 1], 48, 1.5, 6), ([2, 5, 7, 2], 80, 0.6, 5)]))
K(12, "12.3", lambda sc, L, thing: N(f"A model of a {thing} is made to a scale of 1 : {sc}. The model is {L} cm long. How long is the real {thing}? Give your answer in metres.", float(D(str(L)) * sc / 100), "m", units=["m", "cm"], d="H", reason=f"{L} × {sc} = {pc(D(str(L)) * sc)} cm = {pc(D(str(L)) * sc / 100)} m."), [(40, 11.5, "car")], lambda r: (r.choice([50, 20, 25, 80]), r.choice([12.5, 9.6, 14.5, 18.4]), r.choice(["bus", "boat", "truck", "plane"])))
def _cls(g1, b1, g2, b2, k):
    f1, f2 = Fr(g1, g1 + b1), Fr(g2, g2 + b2)
    if k == 0: return P(f"In Class 7X the ratio of girls to boys is {g1} : {b1}. What fraction of the class are girls?", f1, reason=f"{g1} out of {g1 + b1} parts: {frac(f1)}.")
    w = "7X" if f1 > f2 else "7Y"
    return MC(f"In Class 7X the ratio of girls to boys is {g1} : {b1}. In Class 7Y the ratio of girls to boys is {g2} : {b2}. Which class has the greater proportion of girls?", f"Class {w}", [(f"Class {'7Y' if w == '7X' else '7X'}", "Compare the fractions of each class that are girls."), ("They are the same", "The fractions are not equal.")], d="H", reason=f"7X: {g1}/{g1 + b1} ≈ {float(f1):.3f}. 7Y: {g2}/{g2 + b2} ≈ {float(f2):.3f}. Class {w} has the greater proportion.")
K(12, "12.3", _cls, [(5, 7, 8, 13, 0), (5, 7, 8, 13, 1)], lambda r: r.choice([(3, 5, 4, 7), (4, 5, 7, 9), (5, 6, 9, 11), (2, 3, 5, 8), (7, 8, 6, 7)]) + (r.randint(0, 1),))

# ================================================================= Unit 13 · probability
def _wx(a, b, k):
    A, B_ = D(a), D(b); q = [("not rainy", 1 - A, f"1 − {a} = {1 - A}."), ("rainy or sunny", A + B_, f"{a} + {b} = {A + B_}."), ("cloudy", 1 - A - B_, f"1 − {a} − {b} = {1 - A - B_}.")][k]
    return N(f"The weather tomorrow will be exactly one of rainy, sunny or cloudy. The probability that it is rainy is {a}. The probability that it is sunny is {b}. Find the probability that tomorrow is {q[0]}.", float(q[1]), tol=1e-6, reason=q[2])
K(13, "13.1", _wx, [("0.42", "0.37", 0), ("0.42", "0.37", 1), ("0.42", "0.37", 2)], lambda r: (r.choice(["0.35", "0.28", "0.46", "0.31"]), r.choice(["0.44", "0.39", "0.25", "0.52"]), r.randint(0, 2)))
def _bus(nm, both, neither, k):
    v = 1 - D(both) if k == 0 else 1 - D(neither)
    return N(f"{nm} catches two buses to school. The probability that both buses are late is {both}. The probability that neither bus is late is {neither}. Find the probability that {'at most one bus is late' if k == 0 else 'at least one bus is late'}.", float(v), tol=1e-6, d="H", reason=(f"'At most one late' is the opposite of 'both late': 1 − {both} = {v}." if k == 0 else f"'At least one late' is the opposite of 'neither late': 1 − {neither} = {v}."))
K(13, "13.1", _bus, [("Thao", "0.08", "0.55", 0), ("Thao", "0.08", "0.55", 1)], lambda r: (pick(r, NAMES), r.choice(["0.06", "0.12", "0.05", "0.15"]), r.choice(["0.48", "0.6", "0.52", "0.64"]), r.randint(0, 1)))
def _box(pa, pb, m, k, n):
    rest = 1 - D(pa) - D(pb); kiwi = rest / (m + 1); plum = kiwi * m
    if k == 0: return TB(f"A fruit box contains only apples, pears, plums and kiwis. A fruit is taken at random. The probability of taking a plum is {['', '', 'twice', 'three times', 'four times'][m]} the probability of taking a kiwi. Complete the table.", ["Fruit", "apple", "pear", "plum", "kiwi"], [["Probability", pa, pb, B(float(plum)), B(float(kiwi))]], d="H", reason=f"plum + kiwi = 1 − {pa} − {pb} = {rest}. Kiwi = {rest} ÷ {m + 1} = {kiwi}, plum = {plum}.")
    return N(f"A fruit is taken at random from a box. The probability that it is a pear is {pb}. There are {n} pears in the box. Work out the total number of fruits.", float(n / D(pb)), d="H", reason=f"{n} ÷ {pb} = {pc(n / D(pb))} fruits.")
K(13, "13.1", _box, [("0.32", "0.18", 4, 0, 9), ("0.32", "0.18", 4, 1, 9)], lambda r: r.choice([("0.3", "0.25", 2, 0, 10), ("0.36", "0.24", 3, 0, 12), ("0.28", "0.12", 2, 0, 6), ("0.3", "0.25", 2, 1, 10), ("0.36", "0.24", 3, 1, 12), ("0.28", "0.12", 2, 1, 6)]))
K(13, "13.1", lambda nm, tot, cats, pd: P(f"{nm} has a box of {tot} animal cards showing cats, dogs or rabbits. {cats} cards show cats. The probability of choosing a dog card at random is {pd}. Find the probability of choosing a rabbit card.", Fr(tot - cats - int(D(pd) * tot), tot), d="H", reason=f"Dogs = {pd} × {tot} = {int(D(pd) * tot)}. Rabbits = {tot} − {cats} − {int(D(pd) * tot)} = {tot - cats - int(D(pd) * tot)}. P(rabbit) = {tot - cats - int(D(pd) * tot)}/{tot}."), [("Vy", 40, 14, "0.45")],
  lambda r: (pick(r, NAMES),) + r.choice([(50, 15, "0.4"), (20, 6, "0.35"), (60, 21, "0.25"), (80, 30, "0.45")]))
def _lt(n, d_, tig):
    tot = tig * d_ // (d_ - n)
    return TB("A box has only lion cards and tiger cards. Complete the table.", ["Card", "Number of cards", "Probability"], [["lion", B(tot - tig), f"{n}/{d_}"], ["tiger", str(tig), B(f"{d_ - n}/{d_}")]], d="H", reason=f"P(tiger) = 1 − {n}/{d_} = {d_ - n}/{d_}. {tig} cards are {d_ - n}/{d_} of the box, so there are {tot} cards and {tot - tig} lions.")
K(13, "13.1", _lt, [(7, 20, 26)], lambda r: r.choice([(3, 10, 21), (9, 20, 22), (2, 5, 18), (7, 25, 36), (3, 8, 25)]))
def _club(tot, less):
    s = (tot + less) // 4; chess = s - less
    return P(f"A sports club has football, swimming and chess members. The number of swimmers is half the number of footballers. There are {less} fewer chess players than swimmers. There are {tot} members altogether. One member is chosen at random. Work out the probability that the member does not play chess.", Fr(tot - chess, tot), d="VH", reason=f"Swimmers s, footballers 2s, chess s − {less}: 4s − {less} = {tot}, so s = {s}. Chess = {chess}. P(not chess) = {tot - chess}/{tot} = {frac(Fr(tot - chess, tot))}.")
K(13, "13.1", _club, [(90, 6)], lambda r: r.choice([(70, 10), (60, 4), (100, 8), (50, 6), (120, 8)]))
def _die(nm, fr, k):
    tot = sum(fr); ev = fr[1] + fr[3] + fr[5]
    if k == 0: return N(f"{nm} rolls a six-sided die {tot} times. Calculate the experimental probability of rolling a 4. Write your answer as a decimal.", fr[3] / tot, tol=1e-6, data=_dd(fr), reason=f"{fr[3]} ÷ {tot} = {fmt(fr[3] / tot)}.")
    if k == 1: return N(f"{nm} rolls a six-sided die {tot} times. Calculate the experimental probability of rolling an even number. Write your answer as a decimal.", ev / tot, tol=1e-6, d="H", data=_dd(fr), reason=f"{fr[1]} + {fr[3]} + {fr[5]} = {ev}; {ev} ÷ {tot} = {fmt(ev / tot)}.")
    return MC(f"{nm} rolls a six-sided die {tot} times. Is the die likely to be fair?", "Probably fair: every experimental probability is close to 1/6", [("Not fair: the frequencies are not all exactly the same", "Results of an experiment vary; they do not have to be identical."), (f"Not fair: 4 came up {fr[3]} times, the most", "A small difference like this is expected by chance."), ("You cannot tell anything from an experiment", "With many trials, experimental probabilities are a good guide.")], d="H", data=_dd(fr), reason=f"For a fair die each score is expected about {tot // 6} times. The frequencies are all fairly close to {tot // 6}.")
def _dd(fr): return {"caption": "Results", "head": ["Score", "1", "2", "3", "4", "5", "6"], "rows": [["Frequency"] + [str(f) for f in fr]]}
def _dier(r):
    tot = r.choice([120, 300, 600]); base = tot // 6; fr = [base + r.randint(-base // 6, base // 6) for _ in range(5)]; fr.append(tot - sum(fr))
    return (pick(r, NAMES), fr, r.randint(0, 2)) if abs(fr[5] - base) <= base // 5 else None
K(13, "13.2", _die, [("Hai", [36, 42, 38, 48, 40, 36], 0), ("Hai", [36, 42, 38, 48, 40, 36], 1), ("Hai", [36, 42, 38, 48, 40, 36], 2)], _dier)
def _ss(sp, n, k, t):
    cells = [[abs(a - b) for b in range(1, n + 1)] for a in sp]; tot = len(sp) * n
    if k == 0:
        rows = [[str(a)] + [str(v) if (i + j) % 3 == 0 else B(v) for j, v in enumerate(row)] for i, (a, row) in enumerate(zip(sp, cells))]
        return TB(f"A fair {len(sp)}-sided spinner labelled {', '.join(map(str, sp[:-1]))} and {sp[-1]} is spun and a fair {n}-sided die (numbered 1–{n}) is rolled. The score is the difference between the two numbers (larger − smaller). Complete the sample space diagram.", ["", *map(str, range(1, n + 1))], rows, d="H", reason="Subtract the smaller number from the larger in every cell.")
    c = sum(1 for row in cells for v in row if (v == t if k == 1 else v >= t))
    return P(f"A fair {len(sp)}-sided spinner labelled {', '.join(map(str, sp[:-1]))} and {sp[-1]} is spun and a fair {n}-sided die (numbered 1–{n}) is rolled. The score is the difference between the two numbers (larger − smaller). Find the probability that the difference is {t}{'' if k == 1 else ' or more'}.", Fr(c, tot), d="H" if k == 1 else "VH", reason=f"{c} of the {tot} equally likely outcomes: {c}/{tot} = {frac(Fr(c, tot))}.")
K(13, "13.1", _ss, [([2, 4, 6], 8, 0, 0), ([2, 4, 6], 8, 1, 0), ([2, 4, 6], 8, 2, 4)], lambda r: (r.choice([[1, 3, 5], [2, 3, 5], [1, 4, 6]]), r.choice([6, 8]), r.randint(0, 2), r.choice([1, 2, 3])))
_CD = [("a head and an even number", Fr(3, 12)), ("a tail and a number greater than 4", Fr(2, 12)), ("a head or a 6 (or both)", Fr(7, 12)), ("a tail and an odd number", Fr(3, 12)), ("a head and a number less than 3", Fr(2, 12)), ("a tail or a 1 (or both)", Fr(7, 12)), ("a head and a prime number", Fr(3, 12)), ("a tail and a 5", Fr(1, 12))]
K(13, "13.1", lambda e, v: P(f"A fair coin is flipped and a fair six-sided die is rolled. There are 12 equally likely outcomes, from H1 to T6. Find the probability of getting {e}.", v, d="H", reason=f"{v * 12} of the 12 outcomes: {frac(v)}."), _CD[:3], lambda r: r.choice(_CD[3:]))
_RPS = [("they choose the same", Fr(3, 9)), ("{a} wins", Fr(3, 9)), ("at least one of them chooses rock", Fr(5, 9)), ("{b} wins", Fr(3, 9)), ("neither of them chooses paper", Fr(4, 9)), ("exactly one of them chooses scissors", Fr(4, 9)), ("they choose different things", Fr(6, 9))]
K(13, "13.1", lambda a, b, i: P(f"{a} and {b} play rock–paper–scissors. Each of them chooses rock, paper or scissors at random, so there are 9 equally likely outcomes. Rock beats scissors, scissors beats paper and paper beats rock. Find the probability that {_RPS[i][0].format(a=a, b=b)}.", _RPS[i][1], d="H", reason=f"{_RPS[i][1] * 9} of the 9 outcomes: {frac(_RPS[i][1])}."), [("Quan", "Ngoc", 0), ("Quan", "Ngoc", 1), ("Quan", "Ngoc", 2)], lambda r: two(r, NAMES) + (r.randint(3, 6),))
