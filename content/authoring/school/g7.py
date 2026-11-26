# -*- coding: utf-8 -*-
"""Stage 7 (school Grade 6) revision sets: Unit 1 Integers, Unit 3 Place value and rounding, Unit 7 Fractions, Unit 13 Probability.
Written by the Camday teaching team."""
from decimal import Decimal as D, ROUND_HALF_UP
from fractions import Fraction as Fr
from math import gcd
from kit import *
from school import Reg
R = Reg(7); K = R.K
NAMES = ["Mai", "Khoa", "Linh", "Minh", "Quang", "Sofia", "Arun", "Zara", "Marcus", "Hana", "Omar", "Lucy"]
def two(r, seq): a = pick(r, seq); b = pick(r, [x for x in seq if x != a]); return a, b
def lcm(a, b): return a * b // gcd(a, b)
def sg(n): return fmt(n) if n >= 0 else f"(−{fmt(-n)})"
def rd(x, n): return D(str(x)).quantize(D(1).scaleb(-n), rounding=ROUND_HALF_UP)
def dstr(d):
    s = format(d.normalize(), "f"); ip, _, fp = s.partition(".")
    if len(ip) > 4: ip = "{:,}".format(int(ip)).replace(",", " ")
    return ip + ("." + fp if fp else "")

# ================================================================= Unit 3 · 3.1 powers of 10
K(3, "3.1", lambda n: N(f"Write 10{sup(n)} as an ordinary number.", 10 ** n, reason=f"10{sup(n)} is 1 followed by {n} zeros: {fmt(10 ** n)}."), [4], lambda r: r.choice([3, 5, 6, 7]))
K(3, "3.1", lambda n: N(f"{fmt(10 ** n)} = 10ⁿ. Write the value of n.", n, reason=f"{fmt(10 ** n)} has {n} zeros, so it is 10{sup(n)}."), [5], lambda r: r.choice([3, 4, 6, 7, 8]))
K(3, "3.1", lambda a, n: N(f"Work out {dstr(D(str(a)))} × 10{sup(n)}.", float(D(str(a)) * 10 ** n), reason=f"Multiplying by 10{sup(n)} moves every digit {n} places to the left: {dstr(D(str(a)) * 10 ** n)}."),
  [(0.736, 2), (3.15, 4)], lambda r: (r.choice([0.482, 0.917, 2.64, 5.08, 0.0563, 7.21, 0.305]), r.choice([2, 3, 4])))
K(3, "3.1", lambda a, n: N(f"Work out {dstr(D(str(a)))} ÷ 10{sup(n)}.", float(D(str(a)) / 10 ** n), reason=f"Dividing by 10{sup(n)} moves every digit {n} places to the right: {dstr(D(str(a)) / 10 ** n)}."),
  [(58.3, 3), (470000, 4), (6, 2)], lambda r: (r.choice([72.4, 9, 36.5, 820000, 5300, 4, 61.7]), r.choice([2, 3, 4])))
K(3, "3.1", lambda a, n: N(f"Find the missing number:  ☐ ÷ 10{sup(n)} = {dstr(D(str(a)) / 10 ** n)}", a, d="H", reason=f"Undo the division: {dstr(D(str(a)) / 10 ** n)} × 10{sup(n)} = {fmt(a)}."),
  [(35, 2)], lambda r: (r.choice([47, 62, 8, 125, 59, 7.3]), r.choice([2, 3])))
K(3, "3.1", lambda a, n: N(f"{dstr(D(str(a)))} × 10ⁿ = {dstr(D(str(a)) * 10 ** n)}. Write the value of n.", n, d="H", reason=f"The digits move {n} places to the left, so the multiplier is 10{sup(n)}."),
  [(0.0927, 4)], lambda r: (r.choice([0.0463, 0.582, 0.00719, 0.0308]), r.choice([3, 4, 5])))
def _ord10(calcs):
    v = sorted(calcs, key=lambda c: c[1])
    return OD("Work out each calculation. Then put the answers in order of size, smallest first.", [c[0] for c in v], d="H", reason="Answers in order: " + ", ".join(fmt(c[1]) for c in v) + ".")
def _ord10r(r):
    out = {}
    while len(out) < 5:
        n = r.choice([1, 2, 3]); mul = r.random() < 0.5; base = r.choice([3, 3.4, 3.7, 4.2, 5, 36, 34.6, 2.8, 4.9, 30, 27])
        a = D(str(base)) * 10 ** n if not mul else D(str(base)) / 10 ** n
        txt = f"{dstr(a.normalize() if a == a.to_integral() else a)} {'×' if mul else '÷'} {fmt(10 ** n)}"
        if float(base) not in [x[1] for x in out.values()]: out[txt] = (txt, float(base))
    return (list(out.values()),)
K(3, "3.1", _ord10, [([("3420 ÷ 100", 34.2), ("0.0346 × 100", 3.46), ("3.6 × 10", 36), ("4270 ÷ 1000", 4.27), ("3000 ÷ 1000", 3), ("0.37 × 10", 3.7)],)], _ord10r)

# ================================================================= Unit 3 · 3.2 rounding
_RD = lambda x, n: N(f"Round {x} to {n} decimal place{'s' if n > 1 else ''}.", float(rd(x, n)), reason=f"Look at decimal place {n + 1}: 5 or more rounds up. {x} = {rd(x, n)} ({n} d.p.).")
def _rdr(r):
    n = r.choice([1, 2, 3, 4]); ip = r.choice([6, 38, 52, 274, 615, 907]); fp = "".join(str(r.randint(0, 9)) for _ in range(n + 2))
    if fp[n] == "0" or set(fp) == {"0"}: return None
    return (f"{ip}.{fp}", n)
K(3, "3.2", _RD, [("47.386", 2), ("83.95", 1), ("729.4048", 3), ("508.009963", 4)], _rdr)
K(3, "3.2", lambda x, n, thing: N(f"{thing} of {x} centimetres. Write this length correct to {n} decimal places.", float(rd(x, n)), "cm", units=["cm", "mm", "m"], d="H", reason=f"{x} = {rd(x, n)} cm ({n} d.p.)."),
  [("0.0438726", 4, "A grain of sand has a diameter")], lambda r: (f"0.0{r.randint(11, 98)}{r.randint(5, 9)}{r.randint(1, 9)}{r.randint(11, 99)}", r.choice([3, 4]), r.choice(["A human hair has a width", "A thin wire has a diameter", "A seed has a length"])))
def _ring(t, right, wrongs):
    return MC(f"Which number does NOT round to {t} correct to 1 decimal place?", right, [(w, f"{w} does round to {t}.") for w in wrongs], d="H", reason=f"{right} rounds to {rd(right, 1)}, not {t}.")
def _ringr(r):
    k = r.randint(2, 8); d = r.randint(2, 8); lo = f"{k}.{d - 1}"
    return (f"{k}.{d}", f"{lo}499", [f"{lo}5", f"{k}.{d}49", f"{k}.{d}499"])
K(3, "3.2", _ring, [("5.6", "5.5499", ["5.55", "5.649", "5.6499"])], _ringr)
def _calc(x):
    right = str(rd(x, 5))
    return MC(f"A calculator shows the answer {x}… Which is this answer correct to 5 decimal places?", right, [(right.rstrip("0"), "This has only 4 decimal places: keep the final zero."), (str(rd(x, 5) + D("0.00001")), "The next digit is less than 5, so do not round up."), (str(rd(x, 4)) + "0" if str(rd(x, 4)) + "0" != right else str(rd(x, 3)) + "00", "This was rounded too early.")], d="H", reason=f"The 6th decimal digit decides. {x}… = {right} (5 d.p.); the final zero must be written.")
K(3, "3.2", _calc, ["1.2538008059"], lambda r: f"{r.randint(1, 8)}.{r.randint(1001, 9998)}{r.choice(['9', '0'])}{r.choice(['96', '02', '71', '04'])}{r.randint(100, 999)}" )

# ================================================================= Unit 1 · integers
def _addsub(a, op, b):
    v = a + b if op == "+" else a - b
    return N(f"Work out {fmt(a)} {op} {sg(b)}.", v, reason=f"{fmt(a)} {op} {sg(b)} = {fmt(v)}." + (" Subtracting a negative is the same as adding." if op == "−" and b < 0 else ""))
K(1, "1.1", _addsub, [(-9, "+", 13), (-5, "−", -8), (6, "+", -15), (-12, "−", 7)], lambda r: (nz(r, -15, 9), r.choice("+−"), nz(r, -16, 16)))
K(1, "1.2", lambda a, b: N(f"Work out {fmt(a)} × {sg(b)}.", a * b, reason=f"Signs different → negative, signs the same → positive: {fmt(a * b)}."), [(6, -9)], lambda r: (nz(r, -9, 9), -r.randint(2, 12)))
K(1, "1.2", lambda q, b: N(f"Work out {fmt(q * b)} ÷ {sg(b)}.", q, reason=f"{fmt(q * b)} ÷ {sg(b)} = {fmt(q)}."), [(4, -9)], lambda r: (nz(r, -9, 9), -r.randint(2, 9)))
K(1, "1.2", lambda x, b: N(f"Fill in the missing integer:  ☐ × {b} = {fmt(x * b)}", x, d="H", reason=f"{fmt(x * b)} ÷ {b} = {fmt(x)}."), [(-6, 7)], lambda r: (-r.randint(3, 12), r.randint(3, 9)))
K(1, "1.2", lambda x, b: N(f"Fill in the missing integer:  ☐ ÷ {b} = {fmt(x // b)}", x, d="H", reason=f"{fmt(x // b)} × {b} = {fmt(x)}."), [(-45, 5)], lambda r: (lambda b, q: (-b * q, b))(r.randint(3, 9), r.randint(3, 12)))
K(1, "1.2", lambda a, b, c: N(f"Work out {fmt(a)} × {b} ÷ {sg(c)}.", a * b // c, d="H", reason=f"{fmt(a)} × {b} = {fmt(a * b)}, then {fmt(a * b)} ÷ {sg(c)} = {fmt(a * b // c)}."), [(-5, 8, -4)],
  lambda r: (lambda c, k, b: (-k, b * c, -c))(r.randint(2, 6), r.randint(2, 9), r.randint(2, 5)))
K(1, "1.2", lambda a, b, c: N(f"Work out {a} + {b} × {c}.", a + b * c, reason=f"Multiply first: {b} × {c} = {b * c}. Then {a} + {b * c} = {a + b * c}."), [(9, 4, 6)], lambda r: (r.randint(3, 15), r.randint(3, 9), r.randint(3, 9)))
K(1, "1.2", lambda q, b, c: N(f"Work out {q * (b + c)} ÷ ({b} + {c}).", q, reason=f"Brackets first: {b} + {c} = {b + c}. Then {q * (b + c)} ÷ {b + c} = {q}."), [(9, 3, 5)], lambda r: (r.randint(4, 12), r.randint(2, 6), r.randint(3, 7)))
def _who(a, b, c, n1, n2):
    wrong, right = (a - b) * c, a - b * c
    return MC(f"Two students calculate {a} − {b} × {c}. {n1} says the answer is {wrong}. {n2} says the answer is {fmt(right)}. Who is correct?", f"{n2}, because multiplication is done before subtraction",
              [(f"{n1}, because you work from left to right", f"{n1} subtracted first. Multiplication comes before subtraction."), (f"{n1}, because subtraction is done before multiplication", "Multiplication comes before subtraction."), ("Neither of them", f"{b} × {c} = {b * c}, then {a} − {b * c} = {fmt(right)}.")],
              d="H", reason=f"Multiply first: {b} × {c} = {b * c}, then {a} − {b * c} = {fmt(right)}. {n1} subtracted first.")
K(1, "1.2", _who, [(15, 3, 4, "Mai", "Khoa")], lambda r: (r.randint(14, 30), r.randint(2, 5), r.randint(3, 6)) + two(r, NAMES))
K(1, "1.2", lambda a, b, n: N(f"Simplify {fmt(a)} ÷ {b}{sup(n)}.", a // b ** n, d="H", reason=f"The power first: {b}{sup(n)} = {b ** n}. Then {fmt(a)} ÷ {b ** n} = {fmt(a // b ** n)}."), [(-32, 2, 3)],
  lambda r: (lambda b, n, k: (-k * b ** n, b, n))(*r.choice([(2, 2), (3, 2), (2, 4), (4, 2), (5, 2), (3, 3)]), r.randint(2, 6)))
def _bidmas(a, b, c, e, f, g, h):
    inner = c - e * f; v = a + b * inner ** 2 - g * h
    return N(f"Calculate {a} + {b} × ({c} − {e} × {f})² − {g} × {h}.", v, d="VH", reason=f"{e} × {f} = {e * f}; {c} − {e * f} = {inner}; {inner}² = {inner ** 2}; {b} × {inner ** 2} = {b * inner ** 2}; {g} × {h} = {g * h}; {a} + {b * inner ** 2} − {g * h} = {fmt(v)}.")
K(1, "1.2", _bidmas, [(4, 2, 7, 2, 2, 3, 9)], lambda r: (r.randint(2, 9), r.randint(2, 4), r.randint(8, 12), 2, r.randint(2, 3), r.randint(3, 6), r.randint(6, 9)))
K(1, "1.3", lambda a, b: N(f"Find the lowest common multiple of {a} and {b}.", lcm(a, b), reason=f"List multiples of each; the first one in both lists is {lcm(a, b)}."), [(6, 10), (9, 12)],
  lambda r: r.choice([(4, 6), (8, 12), (6, 15), (10, 15), (12, 16), (9, 15), (6, 14), (8, 20), (12, 18), (15, 20)]))
K(1, "1.4", lambda a, b: N(f"Find the highest common factor of {a} and {b}.", gcd(a, b), reason=f"The largest number that divides both {a} and {b} is {gcd(a, b)}."), [(18, 27), (28, 42)],
  lambda r: r.choice([(24, 36), (30, 45), (16, 40), (36, 60), (20, 50), (32, 48), (27, 63), (42, 70), (45, 75)]))
def _packs(nm, a, b, c, A, B, C):
    h = gcd(gcd(a, b), c)
    return N(f"{nm} has {a} {A}, {b} {B} and {c} {C}. They are put into identical gift packs with nothing left over. What is the greatest number of gift packs?", h, d="H", reason=f"The greatest number of identical packs is the HCF of {a}, {b} and {c}, which is {h}.")
K(1, "1.4", _packs, [("Ms Linh", 48, 72, 120, "pencils", "erasers", "stickers")],
  lambda r: (lambda h, t: (r.choice(["Mr Arun", "Ms Zara", "Ms Hana", "Mr Omar"]), h * t[0], h * t[1], h * t[2]) + r.choice([("pens", "rulers", "notebooks"), ("apples", "oranges", "bananas"), ("badges", "balloons", "sweets")]))(r.choice([6, 8, 12, 15, 18]), r.choice([(2, 3, 5), (3, 4, 5), (2, 5, 7), (3, 5, 7), (4, 5, 6)])))
def _hl(h, a, b, style):
    L = h * a * b; lo, hi = sorted((h * a, h * b))
    p = (f"Two numbers are both greater than {h}. Their highest common factor (HCF) is {h} and their lowest common multiple (LCM) is {L}. Find the two numbers." if style else
         f"The highest common factor of two numbers is {h}. The lowest common multiple of the two numbers is {L}. Neither number is {h}. Work out the two numbers.")
    return TB(p, ["Smaller number", "Larger number"], [[B(lo), B(hi)]], d="VH", skill="Reasoning", reason=f"Both numbers are multiples of {h} and factors of {L}: {lo} and {hi} (HCF {h}, LCM {L}).")
K(1, "1.4", _hl, [(5, 2, 3, 0), (6, 3, 4, 0), (8, 2, 3, 1)], lambda r: (r.choice([3, 4, 7, 9, 10, 12]),) + r.choice([(2, 3), (3, 4), (2, 5), (3, 5), (4, 5)]) + (r.randint(0, 1),))
def _d49(n):
    ds = sum(int(c) for c in str(n)); last = str(n)[-2:]
    return MC(f"Which pair of facts shows that {n} is divisible by 4 and by 9?", f"{last} is divisible by 4, and the digit sum {ds} is a multiple of 9",
              [(f"{n} is even, and it ends in {str(n)[-1]}", "Being even only shows divisibility by 2."), (f"The digit sum {ds} is divisible by 4 and by 9", "The digit-sum test works for 3 and 9, not for 4."), (f"{last} is divisible by 4 and by 9", "For 9 you must use the sum of all the digits.")],
              d="H", reason=f"Divisible by 4: the last two digits, {last}, are divisible by 4. Divisible by 9: {' + '.join(str(n))} = {ds}, a multiple of 9.")
def _d49r(r):
    n = 36 * r.randint(60, 270)
    return n if n % 100 not in (0, 36, 72) and sum(int(c) for c in str(n)) % 4 else None
K(1, "1.5", _d49, [7416], _d49r)
K(1, "1.5", lambda base, m: N(f"A whole number is greater than {fmt(base)}. The number is also divisible by {m}. Find the smallest whole number with this property.", (base // m + 1) * m, d="H", reason=f"Check the numbers just above {fmt(base)} with the test for {m}: the first one that works is {fmt((base // m + 1) * m)}."),
  [(70000, 6)], lambda r: (r.choice([20000, 40000, 50000, 80000, 31000, 64000]), r.choice([6, 9, 3])))
def _star(ds, pos, m):
    s = sum(ds); x = (-s) % m; shown = "".join(str(d) for d in ds[:pos]) + "*" + "".join(str(d) for d in ds[pos:])
    return N(f"The number {shown} has one digit replaced by *. The number is divisible by {m}. Find the value of *.", x, d="H", reason=f"The digit sum must be a multiple of {m}: {' + '.join(str(d) for d in ds)} = {s}, so * = {x} (total {s + x}).")
def _starr(r):
    ds = [r.randint(1, 9) for _ in range(3)]
    return (ds, r.randint(1, 3), 9) if sum(ds) % 9 else None
K(1, "1.5", _star, [([5, 8, 2], 1, 9)], _starr)
def _last(pre, m):
    s = sum(int(c) for c in pre); c = [d for d in range(10) if (s + d) % m == 0 and d % 2]
    return N(f"{pre}* is a 4-digit number, but the last digit has been covered by *. The number is a multiple of {m} but not a multiple of 2. What is the missing digit?", c[0], d="H", reason=f"{' + '.join(pre)} = {s}. The digit must make the total a multiple of {m} and must be odd: {c[0]}.")
def _lastr(r):
    pre = str(r.randint(101, 989)); s = sum(int(c) for c in pre)
    for m in (r.choice([3, 9]), 9):
        if len([d for d in range(10) if (s + d) % m == 0 and d % 2]) == 1 and len([d for d in range(10) if (s + d) % m == 0]) >= 1: return (pre, m)
    return None
K(1, "1.5", _last, [("253", 3)], _lastr)
def _d6(n):
    ds = sum(int(c) for c in str(n))
    return MC(f"Which working shows that {n} is divisible by 6?", f"{n} is even, and {' + '.join(str(n))} = {ds} is a multiple of 3",
              [(f"{n} ends in {str(n)[-1]}, and {str(n)[-1]} is not 6", "The last digit does not need to be 6."), (f"{' + '.join(str(n))} = {ds} is a multiple of 6", "The digit sum tests 3 (and 9). You must also check the number is even."), (f"{n} is even, so it is divisible by 6", "Even only shows divisibility by 2. Check 3 as well.")],
              d="H", reason=f"A number is divisible by 6 when it is divisible by 2 and by 3. {n} is even; {' + '.join(str(n))} = {ds}, a multiple of 3.")
K(1, "1.5", _d6, [5274], lambda r: (lambda n: n if sum(int(c) for c in str(n)) % 6 and n % 10 != 6 else None)(6 * r.randint(180, 1600)))
K(1, "1.6", lambda a, b, c: N(f"Work out √{a * a} + √{b * b} − √{c * c}.", a + b - c, reason=f"{a} + {b} − {c} = {a + b - c}."), [(9, 6, 7)], lambda r: (r.randint(5, 12), r.randint(2, 9), r.randint(2, 8)))
K(1, "1.6", lambda a, b: N(f"Work out ∛{a ** 3} − ∛{b ** 3}.", a - b, reason=f"∛{a ** 3} = {a} and ∛{b ** 3} = {b}, so the answer is {a - b}."), [(4, 2)], lambda r: r.choice([(5, 2), (5, 3), (3, 1), (4, 3), (10, 4), (10, 3), (5, 1)]))
def _think(nm, lo, hi, m):
    c = [k * k for k in range(1, 60) if lo < k * k < hi and k % m == 0]; assert len(c) == 1, (lo, hi, m, c)
    return N(f"{nm} thinks of a number between {lo} and {hi}. The square root of the number is a multiple of {m}. What is {nm}'s number?", c[0], d="VH", reason=f"Square the multiples of {m}: the only square between {lo} and {hi} is {c[0]} (√{c[0]} = {int(c[0] ** .5)}).")
def _thinkr(r):
    m = r.choice([4, 5, 6, 7, 8]); k = m * r.randint(2, 4); lo = (k * k // 100) * 100 - 100 * r.randint(0, 1); hi = lo + 200
    return (pick(r, NAMES), lo, hi, m) if len([j for j in range(1, 60) if lo < j * j < hi and j % m == 0]) == 1 and lo > 0 else None
K(1, "1.6", _think, [("Quang", 300, 500, 6)], _thinkr)
K(1, "1.6", lambda a, b: N(f"Given that {a}² = {a * a} and {b}³ = {b ** 3}, work out the value of √{a * a} + ∛{b ** 3}.", a + b, d="H", reason=f"√{a * a} = {a} and ∛{b ** 3} = {b}, so the total is {a + b}."), [(24, 7)], lambda r: (r.choice([17, 19, 23, 26, 31, 34]), r.choice([6, 8, 9, 11, 12])))

# ================================================================= Unit 7 · fractions
TOLF = 1e-6
def mx(f): f = Fr(f); return frac(f, True) if f > 1 else frac(f)
def F(prompt, v, **kw):
    v = Fr(v); kw.setdefault("reason", f"= {mx(v)}")
    return N(prompt + " Give your answer as a fraction in its simplest form or a mixed number.", float(v), tol=TOLF, **kw)
def rfr(r, dens=(3, 4, 5, 6, 8, 9, 10, 12)):
    d = pick(r, dens); n = r.randint(1, d - 1); return Fr(n, d)
def _tf(st, ok, why):
    return MC(f"True or false?  {st}", "True" if ok else "False", [("False" if ok else "True", why)], reason=why)
def _tfr(r):
    a, b = rfr(r), rfr(r)
    if a == b: return None
    s = r.choice("<>"); ok = (a < b) if s == "<" else (a > b); L = lcm(a.denominator, b.denominator)
    return (f"{a.numerator}/{a.denominator} {s} {b.numerator}/{b.denominator}", ok, f"{frac(a)} = {a.numerator * L // a.denominator}/{L} and {frac(b)} = {b.numerator * L // b.denominator}/{L}.")
K(7, "7.1", _tf, [("2/5 < 3/5", True, "The denominators are the same and 2 < 3."), ("0.5 ≠ 1/2", False, "0.5 = 1/2, so they are equal."), ("7/4 > 1 1/2", True, "7/4 = 1 3/4, which is greater than 1 1/2.")], _tfr)
def _big(a, b):
    a, b = Fr(*a), Fr(*b); L = lcm(a.denominator, b.denominator); hi, lo = max(a, b), min(a, b); t = lambda f: f"{f.numerator}/{f.denominator}"; e = lambda f: f"{f.numerator * L // f.denominator}/{L}"
    return MC(f"Which is bigger, {t(a)} or {t(b)}?", f"{t(hi)}, because {t(hi)} = {e(hi)} and {t(lo)} = {e(lo)}", [(f"{t(lo)}, because its numerator and denominator are bigger" if lo.denominator > hi.denominator else f"{t(lo)}, because its denominator is smaller", "Compare with a common denominator."), ("They are equal", f"{e(hi)} is not equal to {e(lo)}.")],
              d="H", reason=f"With denominator {L}: {t(hi)} = {e(hi)} and {t(lo)} = {e(lo)}, so {t(hi)} is bigger.")
K(7, "7.1", _big, [((5, 7), (7, 10))], lambda r: r.choice([((3, 4), (7, 9)), ((4, 5), (7, 9)), ((5, 8), (3, 5)), ((2, 3), (7, 10)), ((5, 6), (7, 9)), ((3, 7), (2, 5)), ((5, 9), (4, 7))]))
def _btw(a, b, right, wrongs):
    return MC(f"Which fraction is between {a} and {b}?", right, [(w, "Change the fractions to decimals or use a common denominator to check.") for w in wrongs], d="H", reason=f"{right} lies between {a} and {b}: compare them with a common denominator or as decimals.")
K(7, "7.1", _btw, [("3/5", "4/5", "7/10", ["1/2", "9/10", "5/6"])], lambda r: r.choice([("1/2", "3/4", "5/8", ["2/5", "7/8", "4/5"]), ("2/5", "3/5", "1/2", ["1/3", "7/10", "2/3"]), ("1/4", "1/2", "3/8", ["1/5", "5/8", "3/5"]), ("2/3", "5/6", "3/4", ["1/2", "7/8", "3/5"]), ("1/5", "2/5", "3/10", ["1/10", "1/2", "9/20"])]))
def _least(ns, fs, thing, word):
    v = [Fr(*f) for f in fs]; i = v.index(min(v) if word == "least" else max(v)); t = lambda f: f"{f[0]}/{f[1]}"
    return MC(f"Three classmates each have a {thing} of the same size. {ns[0]} eats {t(fs[0])}, {ns[1]} eats {t(fs[1])} and {ns[2]} eats {t(fs[2])}. Who ate the {word}?", ns[i], [(n, "Change each fraction to a decimal or use a common denominator.") for j, n in enumerate(ns) if j != i],
              d="H", reason="As decimals: " + ", ".join(f"{t(f)} ≈ {fmt(round(float(Fr(*f)), 2))}" for f in fs) + f". So {ns[i]} ate the {word}.")
def _leastr(r):
    fs = r.sample([(8, 12), (3, 5), (7, 10), (5, 8), (3, 4), (5, 6), (4, 7), (11, 15), (9, 14)], 3)
    return (r.sample(NAMES, 3), fs, r.choice(["pizza", "cake", "chocolate bar"]), r.choice(["least", "most"]))
K(7, "7.1", _least, [(["Huy", "Ngoc", "Tuan"], [(8, 12), (3, 5), (7, 10)], "chocolate bar", "least")], _leastr)
def _addm(w1, f1, w2, f2):
    v = w1 + Fr(*f1) + w2 + Fr(*f2)
    return F(f"Work out {w1} {f1[0]}/{f1[1]} + {w2} {f2[0]}/{f2[1]}.", v, reason=f"Add the whole numbers: {w1 + w2}. Add the fractions: {f1[0]}/{f1[1]} + {f2[0]}/{f2[1]} = {mx(Fr(*f1) + Fr(*f2))}. Total {mx(v)}.")
def _addmr(r):
    a, b = rfr(r, (4, 5, 6, 8, 10, 12)), rfr(r, (3, 4, 6, 8))
    if a + b <= 1 or a.denominator == 1 or b.denominator == 1: return None
    return (r.randint(1, 5), (a.numerator, a.denominator), r.randint(1, 4), (b.numerator, b.denominator))
K(7, "7.2", _addm, [(2, (3, 8), 3, (7, 8)), (3, (5, 6), 2, (3, 4))], _addmr)
def _rib(w1, f1, w2, f2, est):
    v = w1 + Fr(*f1) + w2 + Fr(*f2); a, b = f"{w1} {f1[0]}/{f1[1]}", f"{w2} {f2[0]}/{f2[1]}"
    if est: return N(f"A red ribbon is {a} m long. A blue ribbon is {b} m long. Estimate the total length by rounding each length to the nearest whole metre.", round(float(w1 + Fr(*f1)) + 1e-9) + round(float(w2 + Fr(*f2)) + 1e-9), "m", units=["m", "cm"], reason=f"{a} ≈ {round(float(w1 + Fr(*f1)) + 1e-9)} and {b} ≈ {round(float(w2 + Fr(*f2)) + 1e-9)}.")
    return F(f"A red ribbon is {a} m long. A blue ribbon is {b} m long. Work out the exact total length of the two ribbons, in metres.", v, d="H", reason=f"{a} + {b} = {mx(v)} m.")
K(7, "7.2", _rib, [(1, (1, 2), 2, (1, 4), 1), (1, (1, 2), 2, (1, 4), 0)], lambda r: (r.randint(1, 3), r.choice([(3, 4), (2, 3), (5, 8), (4, 5)]), r.randint(1, 4), r.choice([(1, 4), (1, 3), (3, 8), (1, 5), (5, 6)]), r.randint(0, 1)))
def _lam(nm, w1, w2, n1, n2, d):
    v = w1 + w2 + Fr(n1 + n2, d)
    return MC(f"{nm} worked out {w1} {n1}/{d} + {w2} {n2}/{d} = {w1 + w2} {n1 + n2}/{2 * d}. Is {nm} correct?", f"No. The denominators were added. The correct answer is {mx(v)}",
              [("Yes, the answer is correct", f"{n1}/{d} + {n2}/{d} = {n1 + n2}/{d}, not {n1 + n2}/{2 * d}."), (f"No. The correct answer is {w1 + w2} {n1 + n2}/{d} and it cannot be simplified", f"{n1 + n2}/{d} is more than 1, so change it to a mixed number."), (f"No. The whole numbers should be multiplied", "Add the whole numbers and add the fractions.")],
              d="H", reason=f"Keep the denominator: {n1}/{d} + {n2}/{d} = {n1 + n2}/{d} = {mx(Fr(n1 + n2, d))}. So the total is {mx(v)}.")
def _lamr(r):
    d = r.choice([5, 7, 8, 9]); n1 = r.randint(d // 2 + 1, d - 1); n2 = r.randint(d - n1 + 1, d - 1)
    return (pick(r, NAMES), r.randint(1, 4), r.randint(1, 3), n1, n2, d)
K(7, "7.2", _lam, [("Lam", 2, 1, 3, 4, 5)], _lamr)
def _mis(a, b, x, d, op):
    f1, f2 = Fr(a, b), Fr(x, d); v = f1 * f2 if op == "×" else f1 / f2
    return N(f"Write the missing number:  {a}/{b} {op} ☐/{d} = {frac(v)}", x, d="H", reason=f"{a}/{b} {op} {x}/{d} = {frac(v)}, so the missing number is {x}.")
K(7, "7.3", _mis, [(3, 4, 5, 9, "×")], lambda r: (lambda a, b, x, d: (a, b, x, d, "×") if gcd(x, d) == 1 and gcd(a, b) == 1 else None)(r.randint(1, 5), r.choice([4, 5, 6, 7, 8]), r.choice([1, 2, 4, 5, 7]), r.choice([3, 9, 11])))
K(7, "7.4", _mis, [(5, 6, 2, 3, "÷")], lambda r: (lambda a, b, x, d: (a, b, x, d, "÷") if gcd(x, d) == 1 and gcd(a, b) == 1 else None)(r.randint(1, 5), r.choice([4, 6, 7, 8, 9]), r.choice([1, 2, 4]), r.choice([3, 5, 7])))
def _mul(a, b):
    v = Fr(*a) * Fr(*b)
    return F(f"Work out {a[0]}/{a[1]} × {b[0]}/{b[1]}.", v, reason=f"Multiply the numerators and the denominators, cancelling common factors: {mx(v)}.")
def _pairr(r):
    a, b = rfr(r, (5, 6, 8, 9, 10, 12)), rfr(r, (7, 9, 14, 15, 21, 27))
    return ((a.numerator, a.denominator), (b.numerator, b.denominator)) if a.denominator > 1 and b.denominator > 1 and b.numerator > 1 else None
K(7, "7.3", _mul, [((5, 8), (4, 15))], _pairr)
def _div(a, b):
    v = Fr(*a) / Fr(*b)
    return F(f"Work out {a[0]}/{a[1]} ÷ {b[0]}/{b[1]}.", v, reason=f"Multiply by the reciprocal: {a[0]}/{a[1]} × {b[1]}/{b[0]} = {mx(v)}.")
K(7, "7.4", _div, [((7, 9), (14, 27))], _pairr)
K(7, "7.3", lambda n, d, k: N(f"Work out {n}/{d} of {d * k}.", n * k, reason=f"{d * k} ÷ {d} = {k}, then {k} × {n} = {n * k}."), [(3, 8, 7), (5, 6, 14)], lambda r: (lambda d: (r.randint(2, d - 1), d, r.randint(6, 15)))(r.choice([5, 7, 8, 9, 12])))
K(7, "7.4", lambda k, n, d: N(f"Work out {k * n} ÷ {n}/{d}.", k * d, reason=f"{k * n} × {d}/{n} = {k * d}."), [(4, 3, 4)], lambda r: (r.randint(2, 6), r.choice([2, 3, 5]), r.choice([7, 4, 8])) )
K(7, "7.4", lambda n, d: N(f"A jug holds {n}/{d} litre of juice. Each cup holds 1/{d} litre. How many cups can be filled?", n, d="H", reason=f"{n}/{d} ÷ 1/{d} = {n} cups."), [(3, 4)], lambda r: (lambda d: (r.randint(2, d - 1), d))(r.choice([5, 6, 8, 10])))
def _path(nm, a, b):
    v = Fr(*a) * Fr(*b)
    return F(f"A path is {a[0]}/{a[1]} km long. {nm} has walked {b[0]}/{b[1]} of the path. How far has {nm} walked, in km?", v, d="H", reason=f"{b[0]}/{b[1]} × {a[0]}/{a[1]} = {frac(v)} km.")
K(7, "7.3", _path, [("Linh", (3, 4), (2, 3))], lambda r: (pick(r, NAMES), r.choice([(4, 5), (5, 6), (7, 8), (9, 10)]), r.choice([(1, 2), (2, 3), (3, 4), (1, 3)])))
K(7, "7.5", lambda d, n: N(f"Work out 1/{d} × {n}.", n // d, reason=f"1/{d} of {n} = {n} ÷ {d} = {n // d}." + (f" Halve and halve again: {n // 2}, then {n // 4}." if d == 4 else "")), [(4, 800)], lambda r: (lambda d: (d, d * r.choice([30, 50, 70, 120, 150, 250])))(r.choice([4, 5, 8])))
def _ooo(a, b, c):
    v = Fr(*a) + Fr(*b) * Fr(*c)
    return F(f"Use the correct order of operations to work out {a[0]}/{a[1]} + {b[0]}/{b[1]} × {c[0]}/{c[1]}.", v, d="H", reason=f"Multiply first: {b[0]}/{b[1]} × {c[0]}/{c[1]} = {frac(Fr(*b) * Fr(*c))}. Then add {a[0]}/{a[1]}: {mx(v)}.")
K(7, "7.5", _ooo, [((3, 4), (2, 5), (1, 2))], lambda r: (r.choice([(1, 2), (2, 3), (1, 4), (3, 5)]), r.choice([(3, 4), (2, 3), (4, 5), (3, 5)]), r.choice([(1, 2), (1, 3), (1, 4)])))
def _share(ns, fs, fund):
    rest = 1 - sum(Fr(1, d) for d in fs) - Fr(1, fund)
    return F(f"{ns[0]}, {ns[1]} and {ns[2]} share the money raised at a school fair. {ns[0]} receives 1/{fs[0]} of the money and {ns[1]} receives 1/{fs[1]}. 1/{fund} of the money goes to the library fund. Work out the fraction of the money that {ns[2]} receives.", rest, d="VH",
             reason=f"1 − 1/{fs[0]} − 1/{fs[1]} − 1/{fund} = {frac(rest)}.")
K(7, "7.5", _share, [(["Phuong", "Quang", "Thao"], (3, 4), 6)], lambda r: (r.sample(NAMES, 3),) + r.choice([((2, 4), 8), ((3, 6), 4), ((2, 5), 10), ((4, 5), 10), ((2, 6), 12), ((3, 5), 15)]))

# ================================================================= Unit 13 · probability
def P(prompt, v, **kw):
    v = Fr(v); kw.setdefault("reason", f"= {frac(v)}")
    return N(prompt + " Give your answer as a fraction or a decimal.", float(v), tol=TOLF, **kw)
_FDP = [("1/2", 0.5, 50), ("1/4", 0.25, 25), ("1/10", 0.1, 10), ("3/4", 0.75, 75), ("1/5", 0.2, 20), ("3/10", 0.3, 30), ("2/5", 0.4, 40), ("7/10", 0.7, 70), ("3/5", 0.6, 60)]
def _fdp(rows):
    out = [[rows[0][0], B(rows[0][1]), B(rows[0][2])], [B(rows[1][0]), fmt(rows[1][1]), B(rows[1][2])], [B(rows[2][0]), B(rows[2][1]), f"{rows[2][2]}"]]
    return TB("Complete the table. Each row shows the same probability in three ways. Write fractions in their simplest form, like 3/4.", ["Fraction", "Decimal", "Percentage (%)"], out, reason="; ".join(f"{a} = {fmt(b)} = {c}%" for a, b, c in rows) + ".")
K(13, "13.1", _fdp, [(_FDP[:3],)], lambda r: (r.sample(_FDP[3:], 3),))
K(13, "13.1", lambda ok, bad: MS("Select all the numbers that cannot be probabilities.", bad, ok, d="H", reason="A probability must be from 0 to 1 (0% to 100%). " + ", ".join(bad) + " are outside this range."),
  [(["0.3", "0", "1"], ["3/2", "−1", "120%"])], lambda r: (r.sample(["0.45", "0", "1", "3/8", "99%", "0.02"], 3), r.sample(["5/4", "−0.2", "150%", "1.3", "−1/2", "7/6"], 3)))
K(13, "13.1", lambda v: N("The arrow shows a probability on the probability line. Write the value shown by the arrow as a decimal.", v, tol=0.011, fig={"kind": "numline", "min": 0, "max": 1, "mark": v}, reason=f"Each small division is 0.1. The arrow points to {fmt(v)}."),
  [0.35, 0.7], lambda r: r.choice([0.15, 0.2, 0.45, 0.6, 0.85, 0.9, 0.25]))
K(13, "13.1", lambda txt, v, why: P(txt, v, reason=why),
  [("A fair spinner is numbered 1 to 5. Find the probability of spinning a 1.", Fr(1, 5), "1 of the 5 equal sections: 1/5 = 0.2."), ("A fair coin is tossed. Find the probability of getting a head.", Fr(1, 2), "1 of 2 equally likely outcomes: 1/2 = 0.5."), ("A bag contains 8 red balls and 2 blue balls. One ball is taken at random. Find the probability that it is red.", Fr(8, 10), "8 of the 10 balls are red: 8/10 = 0.8.")],
  lambda r: (lambda a, b, c1, c2: (f"A bag contains {a} {c1} balls and {b} {c2} balls. One ball is taken at random. Find the probability that it is {c2}.", Fr(b, a + b), f"{b} of the {a + b} balls are {c2}: {b}/{a + b} = {frac(Fr(b, a + b))}."))(r.randint(2, 9), r.randint(1, 7), *r.sample(["red", "blue", "green", "yellow", "white"], 2)))
def _spin(n, a, b):
    g = n - a - b; lab = ["R"] * a + ["B"] * b + ["?"] * g
    return N(f"A spinner has {n} equal sections coloured red, blue or green. P(red) = {a}/{n} and P(blue) = {b}/{n}. How many sections are green?", g, d="H", reason=f"{n} − {a} − {b} = {g} section{'s' if g > 1 else ''}, so P(green) = {g}/{n}.")
K(13, "13.1", _spin, [(8, 4, 3)], lambda r: (lambda n: (lambda a: (n, a, r.randint(1, n - a - 1)))(r.randint(2, n - 3)))(r.choice([6, 8, 10, 12])))
def _least13(n, a, b):
    g = n - a - b; d = {"red": a, "blue": b, "green": g}; lo = min(d, key=d.get)
    if sorted(d.values())[0] == sorted(d.values())[1]: return None
    return MC(f"A spinner has {n} equal sections. P(red) = {a}/{n}, P(blue) = {b}/{n} and P(green) = {g}/{n}. Which colour is the least likely?", lo, [(c, f"P({c}) = {d[c]}/{n} is larger.") for c in d if c != lo], reason=f"The smallest probability is {d[lo]}/{n}, so {lo} is the least likely.")
K(13, "13.1", _least13, [(8, 4, 3)], lambda r: (lambda n: (lambda a: (n, a, r.randint(1, n - a - 1)))(r.randint(2, n - 3)))(r.choice([8, 10, 12])))
def _sp(labels):
    u = sorted(set(labels)); top = max(u, key=labels.count); n = len(labels)
    return MC(f"A fair spinner has {n} equal sections labelled {', '.join(labels[:-1])} and {labels[-1]}. Are the outcomes {', '.join(u[:-1])} and {u[-1]} equally likely?", f"No. {top} is on {labels.count(top)} of the {n} sections, so it is more likely",
              [("Yes, because the spinner is fair", "The sections are equal, but one letter appears more than once."), (f"Yes, because there are {len(u)} outcomes", "Count how many sections each letter has."), (f"No. {top} is less likely because it is repeated", "A repeated letter is more likely.")],
              d="H", fig={"kind": "spinner", "labels": labels}, reason=f"P({top}) = {labels.count(top)}/{n}; the other letters have 1/{n} each. The outcomes are not equally likely.")
K(13, "13.2", _sp, [(["A", "B", "B", "C"],)], lambda r: (r.choice([["A", "A", "B", "C"], ["X", "Y", "Z", "Z", "Z"], ["P", "Q", "Q", "R", "S"], ["A", "B", "C", "C", "C", "D"]]),))
K(13, "13.2", lambda labels: N(f"A fair spinner has {len(labels)} equal sections labelled {', '.join(labels[:-1])} and {labels[-1]}. How many different possible outcomes are there?", len(set(labels)), fig={"kind": "spinner", "labels": labels}, reason="The possible outcomes are " + ", ".join(sorted(set(labels))) + "."),
  [(["A", "B", "B", "C"],)], lambda r: (r.choice([["A", "A", "B", "C", "D"], ["X", "Y", "Z", "Z", "Z"], ["P", "Q", "Q", "R", "S", "S"], ["A", "B", "C", "C", "C", "D"]]),))
_MX = [("Rolling a 1 on a dice / rolling a 6 on the same roll", "Mutually exclusive"), ("Rolling an even number / rolling a 4 on the same roll", "Not mutually exclusive"), ("Getting a head / getting a tail on the same coin toss", "Mutually exclusive"),
       ("Rolling a prime number / rolling an odd number on the same roll", "Not mutually exclusive"), ("Rolling a number less than 3 / rolling a number more than 4", "Mutually exclusive"), ("Picking a red card / picking a king from a pack of cards", "Not mutually exclusive"),
       ("Rolling a multiple of 3 / rolling a 5 on the same roll", "Mutually exclusive"), ("Rolling a square number / rolling a 4 on the same roll", "Not mutually exclusive")]
K(13, "13.2", lambda rows: GD("Is each pair of events mutually exclusive or not mutually exclusive?", "Events", rows, reason="Mutually exclusive events cannot happen at the same time."), [(_MX[:3],)], lambda r: (r.sample(_MX[3:], 3),))
def _cards(word, ask):
    n = len(word); cs = ", ".join(word)
    if ask.startswith("not "): v = Fr(n - word.count(ask[4:]), n)
    else: v = Fr(word.count(ask), n)
    return P(f"These {n} cards are shuffled and one is taken at random: {cs}. Find the probability of taking {ask}.", v, reason=f"{v * n} of the {n} cards: {v * n}/{n} = {frac(v)}.")
K(13, "13.2", _cards, [("BANANA", "A"), ("BANANA", "N"), ("BANANA", "not B")], lambda r: (lambda w: (w, r.choice([max(set(w), key=w.count), "not " + max(set(w), key=w.count), min(set(w), key=w.count)])))(r.choice(["PEPPER", "COFFEE", "LETTER", "BALLOON", "COOKIE", "PUZZLE"])))
_DICE = [("a 3", Fr(1, 6)), ("an even number", Fr(1, 2)), ("a number less than 3", Fr(1, 3)), ("a 7", 0), ("a number greater than 4", Fr(1, 3)), ("a prime number", Fr(1, 2)), ("a multiple of 3", Fr(1, 3)), ("a number less than 7", 1), ("a factor of 6", Fr(2, 3)), ("a 0", 0)]
K(13, "13.2", lambda e, v: P(f"A fair six-sided dice is rolled once. Find the probability of rolling {e}.", v), _DICE[:4], lambda r: r.choice(_DICE[4:]))
def _fruit(names, fr, ask, cnt):
    tot = sum(fr)
    return N(f"{tot} students were asked to name their favourite fruit. A student is chosen at random. Find the probability that the student {ask}. Write your answer as a decimal.", cnt / tot, tol=1e-6, d="H", data={"caption": "Favourite fruit", "head": ["Fruit"] + names, "rows": [["Frequency"] + [str(f) for f in fr]]}, reason=f"{cnt} ÷ {tot} = {fmt(cnt / tot)}.")
def _fruitr(r):
    names = r.sample(["Mango", "Banana", "Apple", "Dragon fruit", "Orange", "Grapes"], 4); tot = r.choice([20, 25, 40, 50])
    a = r.randint(tot // 5, tot // 3); b = r.randint(tot // 8 + 1, tot // 4); c = r.randint(tot // 6, tot // 3); d = tot - a - b - c
    if d < 2: return None
    k = r.randint(0, 2)
    return (names, [a, b, c, d]) + [(f"chose {names[3].lower()}", d), (f"did not choose {names[0].lower()}", tot - a), (f"chose {names[1].lower()} or {names[2].lower()}", b + c)][k]
K(13, "13.2", _fruit, [(["Mango", "Banana", "Apple", "Dragon fruit"], [18, 9, 15, 8], "chose dragon fruit", 8), (["Mango", "Banana", "Apple", "Dragon fruit"], [18, 9, 15, 8], "did not choose mango", 32), (["Mango", "Banana", "Apple", "Dragon fruit"], [18, 9, 15, 8], "chose banana or apple", 24)], _fruitr)
_FAM = "BGB, GGB, BBB, GBG, GGG, BBG, GBB, BGG, GGG, BBB, GBG, BGB, GGB, BBG, GGG, BGG, BBB, GBB, GGB, BGB".split(", ")
_FQ = {"three girls": lambda x: x == "GGG", "at least one girl": lambda x: "G" in x, "three boys": lambda x: x == "BBB", "at least one boy": lambda x: "B" in x, "exactly two girls": lambda x: x.count("G") == 2, "exactly one girl": lambda x: x.count("G") == 1}
def _fam(nm, res, ask):
    c = sum(1 for x in res if _FQ[ask](x)); n = len(res)
    return N(f"A family has three children. Each child is a boy (B) or a girl (G), oldest first. {nm} surveyed {n} families with three children. The results were: {', '.join(res)}. Find the experimental probability that a family has {ask}. Write your answer as a decimal.", c / n, tol=1e-6, d="H", reason=f"{c} of the {n} families: {c} ÷ {n} = {fmt(c / n)}.")
K(13, "13.3", _fam, [("Mr Long", _FAM, "three girls"), ("Mr Long", _FAM, "at least one girl")], lambda r: (r.choice(["Ms Hana", "Mr Omar", "Ms Zara"]), ["".join(r.choice("BG") for _ in range(3)) for _ in range(20)], r.choice(list(_FQ)[2:])))
K(13, "13.3", lambda n, k, what: N(f"In a survey of {n} students, {k} said they {what}. Estimate the probability that a student chosen at random does NOT {what.replace('bring', 'bring').replace('walk', 'walk')}. Write your answer as a decimal.", (n - k) / n, tol=1e-6, d="H", reason=f"{n} − {k} = {n - k} do not. {n - k} ÷ {n} = {fmt((n - k) / n)}."),
  [(400, 280, "bring a water bottle to school")], lambda r: (lambda n: (n, int(n * r.choice([0.55, 0.6, 0.65, 0.75, 0.8, 0.85])), r.choice(["walk to school", "bring a packed lunch to school", "play a musical instrument", "own a bicycle"])))(r.choice([200, 300, 500, 600, 800])))
