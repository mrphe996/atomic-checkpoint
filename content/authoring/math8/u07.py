# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 7 Fractions (7.1 Fractions and recurring decimals, 7.2 Ordering fractions, 7.3 Subtracting
mixed numbers, 7.4 Multiplying an integer by a mixed number, 7.5 Dividing an integer by a fraction, 7.6 Making fraction
calculations easier). Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(7, "Fractions", "Number",
         "Terminating and recurring decimals, ordering fractions, subtracting mixed numbers, multiplying and dividing with fractions, and shortcuts for fraction calculations.",
         {"O1": {"code": "8Nf.05", "sec": "7.1", "codeNote": "", "t": "Recognise fractions that are equivalent to terminating or recurring decimals."},
          "O2": {"code": "8Nf.06", "sec": "7.2", "codeNote": "", "t": "Compare and order fractions, mixed numbers and decimals."},
          "O3": {"code": "8Nf.07", "sec": "7.3", "codeNote": "", "t": "Subtract mixed numbers, including when you need to regroup."},
          "O4": {"code": "8Nf.08", "sec": "7.4", "codeNote": "", "t": "Multiply an integer by a fraction or a mixed number."},
          "O5": {"code": "8Nf.09", "sec": "7.5", "codeNote": "", "t": "Divide an integer by a proper fraction."},
          "O6": {"code": "8Nf.10", "sec": "7.6", "codeNote": "", "t": "Use the laws of arithmetic and simplifying to make fraction calculations easier."}})
TOL = 1e-6


def rf(r, dens=(2, 3, 4, 5, 6, 8, 9, 10, 12)):
    d = pick(r, dens); n = r.randint(1, d - 1); return Fr(n, d)


def F(prompt, v, **kw):
    v = Fr(v)
    return N(prompt + " Give your answer as a fraction in its simplest form or a mixed number.", float(v), tol=TOL,
             reason=kw.pop("reason", f"= {frac(v)}" + (f" = {frac(v, True)}" if v > 1 and v.denominator > 1 else "")), **kw)


def mixed(r, lo=1, hi=6, dens=(2, 3, 4, 5, 6, 8)):
    return r.randint(lo, hi) + rf(r, dens)


def term(d):
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    return d == 1


# ================================================================== 7.1
s = U.section("7.1", "Fractions and recurring decimals", ["O1"])
s.idea("Terminating or recurring?", ["Divide the numerator by the denominator. If the division stops, the decimal **terminates**: 3/8 = 0.375. If digits repeat for ever, it is **recurring**: 2/3 = 0.666… = 0.6̇.",
       "A fraction in its simplest form terminates only if its denominator has **no prime factors other than 2 and 5**. 7/20 terminates (20 = 2² × 5); 5/12 recurs (12 has a factor 3)."])
s.example("Recurring", "Write 5/11 as a decimal.", [("5 ÷ 11 = 0.454545…", "short division"), ("the digits 45 repeat", "")], "0.4̇5̇")
s.check(MC("Which fraction gives a recurring decimal?", "4/15", [("3/16", "16 = 2⁴: terminates."), ("7/25", "25 = 5²: terminates."), ("9/40", "40 = 2³ × 5: terminates.")], o="O1"))
s.mistake("Simplify first", ["3/6 looks like it has a factor 3 in the denominator, but 3/6 = 1/2 = 0.5 terminates. Always simplify first."])


def t1(r):
    d = pick(r, [2, 4, 5, 8, 10, 16, 20, 25, 40]); n = r.randint(1, d - 1)
    return N(f"Write {n}/{d} as a decimal.", n / d, tol=TOL, o="O1", reason=f"{n} ÷ {d} = {fmt(n / d)}.")
def t2(r):
    fr = [Fr(n, d) for d, n in ((r.choice([3, 6, 7, 9, 11, 12, 15]), 1), (r.choice([4, 8, 16, 20, 25]), 3), (r.choice([3, 9, 11]), 2), (r.choice([5, 10, 40, 50]), 7))]
    fr = [f for f in fr if f < 1]
    return GD("Does each fraction give a terminating or a recurring decimal?", "Decimal", [(frac(f), "Terminating" if term(f.denominator) else "Recurring") for f in fr], o="O1", extra=["Terminating", "Recurring"])
def t3(r):
    n = r.randint(1, 8)
    return N(f"Write {n}/9 as a recurring decimal. Give the first 3 decimal places.", round(n / 9, 3), tol=0.0006, o="O1", reason=f"{n}/9 = 0.{n}{n}{n}…")
def t4(r):
    d = pick(r, [3, 6, 7, 9, 11, 12, 13, 15, 18, 30]); n = r.randint(1, d - 1)
    f = Fr(n, d)
    return MC(f"Is {n}/{d} a terminating or a recurring decimal?", "terminating" if term(f.denominator) else "recurring", [("recurring" if term(f.denominator) else "terminating", f"In simplest form the denominator is {f.denominator}."), ("neither", "")], o="O1", d="H", reason=f"{n}/{d} = {frac(f)}; denominator {f.denominator}.")
def t5(r):
    fs = r.sample([(1, 4), (3, 5), (7, 8), (1, 20), (9, 25), (3, 16), (11, 40)], 3)
    return TB("Complete the table.", ["Fraction", "Decimal"], [[f"{n}/{d}", B(n / d)] for n, d in fs], o="O1")
def t6(r):
    a = r.randint(10, 98)
    return N(f"Write {a}/99 as a decimal. Give the first 4 decimal places.", round(a / 99, 4), tol=0.00006, o="O1", d="H", reason=f"{a}/99 = 0.{a:02d}{a:02d}…")
def t7(r):
    d = pick(r, [8, 20, 25, 40, 50]); n = r.randint(1, d - 1)
    return N(f"A recipe uses {n}/{d} of a kilogram of flour. Write this as a decimal number of kilograms.", n / d, "kg", units=["kg"], tol=TOL, o="O1", reason=f"{n} ÷ {d} = {fmt(n / d)}.")
def t8(r):
    ds = r.sample([3, 6, 7, 9, 11, 12, 14, 15, 2, 4, 5, 8, 16, 20, 25], 5)
    return MS("Select ALL the denominators that give a terminating decimal for a fraction 1/d.", [str(d) for d in ds if term(d)] or ["10"], [str(d) for d in ds if not term(d)] or ["3"], o="O1", d="H")


s.std([t2, t5, t1, t3, t4, t7, t6, t8], EX("Explain why 7/40 is a terminating decimal.", [("40 = 2³ × 5", ["2³ ?× ?5|2 ?× ?2 ?× ?2 ?× ?5|only 2 and 5|2s and 5"]), ("so it can be written as a fraction over a power of 10 / only factors 2 and 5", ["power of 10|1000|only.*2.*5|no other"])], "In simplest form the denominator 40 = 2³ × 5 has no prime factors other than 2 and 5, so 7/40 can be written as 175/1000 = 0.175.", o="O1"))

# ================================================================== 7.2
s = U.section("7.2", "Ordering fractions", ["O2"])
s.idea("Common denominators", ["To compare fractions, write them with a **common denominator**: 3/4 = 9/12 and 2/3 = 8/12, so 3/4 > 2/3.",
       "You can also change each fraction to a **decimal**, or compare mixed numbers by looking at the whole numbers first."])
s.example("Order", "Put 5/8, 2/3 and 3/5 in order, smallest first.", [("LCM of 8, 3, 5 = 120", ""), ("75/120, 80/120, 72/120", "")], "3/5, 5/8, 2/3")
s.check(CMP("5/6", "7/9", ">", o="O2", reason="15/18 > 14/18."))
s.mistake("Bigger denominator", ["1/8 is smaller than 1/6: bigger denominators mean smaller pieces."])


def o1(r):
    a, b = rf(r), rf(r)
    if a == b: return None
    return CMP(frac(a), frac(b), "<" if a < b else ">", o="O2", reason=f"{frac(a)} ≈ {fmt(round(float(a), 3))}, {frac(b)} ≈ {fmt(round(float(b), 3))}.")
def o2(r):
    fs = sorted({rf(r) for _ in range(6)})[:4]
    if len(fs) < 4: return None
    return OD("Put these fractions in order, smallest first.", [frac(f) for f in fs], o="O2", reason="Use a common denominator or decimals.")
def o3(r):
    a = r.randint(1, 4) + rf(r); b = a + pick(r, [Fr(1, 12), Fr(1, 10), Fr(-1, 12), Fr(1, 6)])
    return MC("Which is larger?", frac(max(a, b), True), [frac(min(a, b), True), "they are equal"], o="O2", reason=f"{frac(a, True)} and {frac(b, True)}: compare the fractions after the whole numbers.")
def o4(r):
    f = rf(r, (3, 4, 5, 6, 8)); dec = round(float(f) + pick(r, [-0.05, 0.05, 0.02, -0.02]), 2)
    return CMP(frac(f), fmt(dec), "<" if f < dec else ">", o="O2", reason=f"{frac(f)} = {fmt(round(float(f), 4))}.")
def o5(r):
    nm = r.sample(["Ali", "Bea", "Cam", "Dot"], 3); fs = [rf(r, (4, 5, 8, 10)) for _ in range(3)]
    if len(set(fs)) < 3: return None
    w = nm[fs.index(max(fs))]
    return MC("Three friends each ate part of a pizza. Who ate the most?", w, [n for n in nm if n != w], o="O2", data={"head": ["Name", *nm], "rows": [["Fraction eaten", *[frac(f) for f in fs]]]})
def o6(r):
    a, b = sorted(r.sample([Fr(1, 3), Fr(2, 5), Fr(1, 2), Fr(3, 5), Fr(2, 3), Fr(3, 4)], 2))
    m = (a + b) / 2
    return F(f"Find the fraction exactly halfway between {frac(a)} and {frac(b)}.", m, o="O2", d="H", reason=f"({frac(a)} + {frac(b)}) ÷ 2 = {frac(m)}.")
def o7(r):
    fs = r.sample([(Fr(3, 4), "0.75"), (Fr(2, 5), "0.4"), (Fr(1, 8), "0.125"), (Fr(5, 8), "0.625"), (Fr(7, 20), "0.35"), (Fr(4, 5), "0.8")], 4)
    return GD("Write each fraction as a decimal.", "Decimal", [(frac(f), d) for f, d in fs], o="O2", extra=["0.5", "0.25"])
def o8(r):
    a = rf(r); b = rf(r)
    if a == b: return None
    return N(f"How much bigger is {frac(max(a, b))} than {frac(min(a, b))}? Give your answer as a fraction.", float(abs(a - b)), tol=TOL, o="O2", d="H", reason=f"{frac(max(a, b))} − {frac(min(a, b))} = {frac(abs(a - b))}.")


s.std([o5, o7, o1, o2, o3, o4, o6, o8], EX("Explain why 3/7 is less than 1/2.", [("half of 7 is 3.5", ["3\\.5|half of 7|3½"]), ("3 is less than 3.5 / 6/14 < 7/14", ["6/14|less than 3\\.5|3 ?< ?3\\.5|smaller"])], "Half of 7 is 3.5, so 1/2 = 3.5/7. 3/7 is less than 3.5/7 (or 6/14 < 7/14), so 3/7 < 1/2.", o="O2"))

# ================================================================== 7.3
s = U.section("7.3", "Subtracting mixed numbers", ["O3"])
s.idea("Two methods", ["**Method 1**: subtract the whole numbers, then the fractions (using a common denominator). If the first fraction is too small, **regroup**: take 1 from the whole number.",
       "**Method 2**: change both to improper fractions, subtract, then change back."])
s.example("Regrouping", "Work out 4 1/5 − 1 2/3.", [("4 3/15 − 1 10/15", "common denominator 15"), ("3 18/15 − 1 10/15", "regroup: 4 3/15 = 3 18/15"), ("= 2 8/15", "")], "2 8/15")
s.check(F("Work out 5 3/4 − 2 1/3.", Fr(41, 12), o="O3"))
s.mistake("Regroup", ["In 3 1/4 − 1 3/4 you cannot take 3/4 from 1/4: write 3 1/4 as 2 5/4 first."])


def m1(r):
    a = mixed(r, 3, 8); b = mixed(r, 1, 2)
    if b >= a: return None
    return F(f"Work out {frac(a, True)} − {frac(b, True)}.", a - b, o="O3", reason=f"= {frac(a - b, True)}.")
def m2(r):
    while True:
        a, b = mixed(r, 3, 7, (4, 5, 6, 8)), mixed(r, 1, 2, (4, 5, 6, 8))
        if (a - int(a)) < (b - int(b)) and b < a: break
    return F(f"Work out {frac(a, True)} − {frac(b, True)}. (You will need to regroup.)", a - b, o="O3", d="H", reason=f"= {frac(a - b, True)}.")
def m3(r):
    l = mixed(r, 4, 9); c = mixed(r, 1, 3)
    return F(f"A plank is {frac(l, True)} m long. A piece {frac(c, True)} m long is cut off. How long is the rest?", l - c, o="O3", units=["m"], reason=f"{frac(l, True)} − {frac(c, True)} = {frac(l - c, True)} m.")
def m4(r):
    w = r.randint(2, 8); f = rf(r)
    return F(f"Work out {w} − {frac(f)}.", w - f, o="O3", reason=f"{w} = {w - 1} {f.denominator}/{f.denominator}; = {frac(w - f, True)}.")
def m5(r):
    a = mixed(r, 2, 6); b = mixed(r, 1, 1)
    return TB(f"Complete the subtraction {frac(a, True)} − {frac(b, True)} by changing to improper fractions.", ["Step", "Value"], [["first number as an improper fraction: numerator", B(a.numerator)], ["second number as an improper fraction: numerator", B(b.numerator)]], o="O3", data={"head": ["Number", frac(a, True), frac(b, True)], "rows": [["Denominator", str(a.denominator), str(b.denominator)]]})
def m6(r):
    a, b = mixed(r, 3, 6), mixed(r, 1, 2)
    return MC(f"Which is the best estimate of {frac(a, True)} − {frac(b, True)}?", str(round(float(a)) - round(float(b))), [str(round(float(a)) + round(float(b))), str(round(float(a)) - round(float(b)) + 3), "0"], o="O3", reason="Round each mixed number to the nearest whole number.")
def m7(r):
    t, a, b = r.randint(8, 12), mixed(r, 1, 3), mixed(r, 1, 3)
    return F(f"A jug holds {t} litres. {frac(a, True)} litres and then {frac(b, True)} litres are poured out. How much is left?", t - a - b, o="O3", d="H", units=["litres", "l"], reason=f"{t} − {frac(a, True)} − {frac(b, True)} = {frac(t - a - b, True)}.")
def m8(r):
    a, b = mixed(r, 2, 5), mixed(r, 2, 5)
    if a == b: return None
    big, small = max(a, b), min(a, b)
    return F(f"Kai runs {frac(big, True)} km and Lia runs {frac(small, True)} km. How much further does Kai run?", big - small, o="O3", units=["km"], data={"head": ["Runner", "Kai", "Lia"], "rows": [["Distance (km)", frac(big, True), frac(small, True)]]})


s.std([m5, m8, m1, m2, m3, m4, m6, m7], EX("Explain how to work out 3 1/4 − 1 3/4.", [("you cannot take 3/4 from 1/4, so regroup", ["regroup|borrow|exchange|cannot take|can't take"]), ("2 5/4 − 1 3/4 = 1 2/4 = 1 1/2", ["1 ?1/2|1 ?2/4|1½|1\\.5|3/2"])], "You cannot take 3/4 from 1/4, so regroup: 3 1/4 = 2 5/4. Then 2 5/4 − 1 3/4 = 1 2/4 = 1 1/2.", o="O3"))

# ================================================================== 7.4
s = U.section("7.4", "Multiplying an integer by a mixed number", ["O4"])
s.idea("Methods", ["**Split** the mixed number: 4 × 2 3/5 = 4 × 2 + 4 × 3/5 = 8 + 12/5 = 10 2/5.",
       "Or change to an **improper fraction**: 4 × 13/5 = 52/5 = 10 2/5."])
s.example("Improper fractions", "Work out 6 × 1 3/4.", [("1 3/4 = 7/4", ""), ("6 × 7/4 = 42/4 = 10 2/4", ""), ("= 10 1/2", "simplify")], "10 1/2")
s.check(F("Work out 3 × 2 1/4.", Fr(27, 4), o="O4"))
s.mistake("Multiply both parts", ["3 × 2 1/4 is NOT 6 1/4. Multiply the fraction part too: 6 + 3/4 = 6 3/4."])


def x1(r):
    n, m = r.randint(2, 9), mixed(r, 1, 4)
    return F(f"Work out {n} × {frac(m, True)}.", n * m, o="O4")
def x2(r):
    n, f = r.randint(2, 12), rf(r)
    return F(f"Work out {n} × {frac(f)}.", n * f, o="O4")
def x3(r):
    n, m = r.randint(3, 8), mixed(r, 1, 3, (2, 4))
    return F(f"A bag of rice has a mass of {frac(m, True)} kg. Find the mass of {n} bags.", n * m, o="O4", units=["kg"])
def x4(r):
    n, m = r.randint(2, 6), mixed(r, 2, 5, (2, 3, 4))
    return F(f"A rectangle is {frac(m, True)} cm long and {n} cm wide. Find its area.", n * m, o="O4", units=["cm²"], fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": [f"{frac(m, True)} cm", f"{n} cm", "", ""]})
def x5(r):
    n, m = r.randint(2, 9), mixed(r, 1, 4)
    return TB(f"Work out {n} × {frac(m, True)} by splitting.", ["Part", "Value"], [[f"{n} × {int(m)}", B(n * int(m))], [f"{n} × {frac(m - int(m))}", B(float(n * (m - int(m))), TOL)], ["Total", B(float(n * m), TOL)]], o="O4", reason="Multiply the whole number and the fraction separately, then add.")
def x6(r):
    n, m = r.randint(3, 9), mixed(r, 1, 3)
    return MC(f"Which is the best estimate of {n} × {frac(m, True)}?", str(n * round(float(m))), [str(n + round(float(m))), str(n * int(m) + 10), str(n * round(float(m)) * 10)], o="O4")
def x7(r):
    n, m = r.randint(3, 9), mixed(r, 2, 6, (2, 4, 8))
    return F(f"A recipe needs {frac(m, True)} cups of flour for one cake. How much flour is needed for {n} cakes?", n * m, o="O4", units=["cups"])
def x8(r):
    m = mixed(r, 1, 3, (3, 4, 5)); k = m.denominator * r.randint(1, 3)
    return N(f"Work out {k} × {frac(m, True)}.", float(k * m), tol=TOL, o="O4", d="H", reason=f"{k} × {frac(m)} = {fmt(float(k * m))} (a whole number).")


s.std([x4, x5, x1, x2, x3, x6, x7, x8], EX("Explain why 5 × 2 1/3 = 11 2/3.", [("5 × 2 = 10", ["10"]), ("5 × 1/3 = 5/3 = 1 2/3, and 10 + 1 2/3 = 11 2/3", ["5/3|1 ?2/3"])], "Split 2 1/3 into 2 + 1/3. 5 × 2 = 10 and 5 × 1/3 = 5/3 = 1 2/3. 10 + 1 2/3 = 11 2/3.", o="O4"))

# ================================================================== 7.5
s = U.section("7.5", "Dividing an integer by a fraction", ["O5"])
s.idea("How many fit?", ["6 ÷ 1/4 asks 'how many quarters are in 6?'. There are 4 quarters in each whole, so 6 ÷ 1/4 = 6 × 4 = 24.",
       "To divide by a fraction, **multiply by its reciprocal** (turn it upside down): 6 ÷ 3/4 = 6 × 4/3 = 24/3 = 8."])
s.example("Reciprocal", "Work out 5 ÷ 2/3.", [("5 × 3/2", "reciprocal of 2/3 is 3/2"), ("= 15/2 = 7 1/2", "")], "7 1/2")
s.check(N("Work out 3 ÷ 1/5.", 15, o="O5"))
s.mistake("Not smaller", ["Dividing by a proper fraction gives a BIGGER answer: 4 ÷ 1/2 = 8."])


def v1(r):
    n, d = r.randint(2, 12), r.randint(2, 10)
    return N(f"Work out {n} ÷ 1/{d}.", n * d, o="O5", reason=f"{n} × {d} = {n * d}.")
def v2(r):
    n, f = r.randint(2, 12), rf(r, (3, 4, 5, 6, 8))
    return F(f"Work out {n} ÷ {frac(f)}.", n / f, o="O5", reason=f"{n} × {f.denominator}/{f.numerator} = {frac(n / f)}.")
def v3(r):
    n, d = r.randint(2, 9), pick(r, [2, 3, 4, 5, 8])
    return N(f"A jug holds {n} litres. How many 1/{d}-litre glasses can be filled from it?", n * d, "glasses", units=["glasses"], o="O5", reason=f"{n} ÷ 1/{d} = {n} × {d} = {n * d}.")
def v4(r):
    f = pick(r, [Fr(2, 3), Fr(3, 4), Fr(2, 5), Fr(3, 5)]); n = f.numerator * r.randint(2, 6)
    return N(f"A rope is {n} m long. How many pieces {frac(f)} m long can be cut from it?", float(n / f), "pieces", units=["pieces"], o="O5", d="H", reason=f"{n} ÷ {frac(f)} = {n} × {f.denominator}/{f.numerator} = {fmt(float(n / f))}.")
def v5(r):
    rows = [("4 ÷ 1/2", "8"), ("3 ÷ 1/3", "9"), ("2 ÷ 1/5", "10"), ("6 ÷ 2/3", "9"), ("5 ÷ 1/4", "20"), ("8 ÷ 4/5", "10")]
    return GD("Find each answer.", "Answer", r.sample(rows, 4), o="O5", extra=["2", "12"])
def v6(r):
    f = rf(r, (3, 4, 5, 7, 8))
    return S(f"What is the reciprocal of {frac(f)}?", [f"{f.denominator}/{f.numerator}"] + ([str(f.denominator)] if f.numerator == 1 else []), o="O5", reason="Turn the fraction upside down.")
def v7(r):
    n, d = r.randint(2, 9), r.randint(2, 6)
    return MC(f"Which calculation gives the same answer as {n} ÷ 1/{d}?", f"{n} × {d}", [f"{n} ÷ {d}", f"{n} × 1/{d}", f"{d} ÷ {n}"], o="O5")
def v8(r):
    n = r.randint(2, 5); f = pick(r, [Fr(1, 4), Fr(1, 3), Fr(1, 2)])
    return TB(f"Complete the pattern.", ["Calculation", "Answer"], [[f"{n} ÷ {frac(f)}", B(float(n / f))], [f"{2 * n} ÷ {frac(f)}", B(float(2 * n / f))], [f"{n} ÷ {frac(f / 2)}", B(float(n / (f / 2)))]], o="O5", d="H")


s.std([v5, v8, v1, v2, v3, v6, v7, v4], EX("Explain why 2 ÷ 1/3 = 6.", [("how many thirds in 2", ["how many thirds|thirds in"]), ("3 thirds in each whole, so 2 × 3 = 6", ["2 ?× ?3|3 thirds|three thirds|each whole"])], "Dividing by 1/3 asks how many thirds are in 2. Each whole has 3 thirds, so there are 2 × 3 = 6 thirds.", o="O5"))

# ================================================================== 7.6
s = U.section("7.6", "Making fraction calculations easier", ["O6"])
s.idea("Strategies", ["**Re-order** so fractions that make wholes go together: 3/8 + 2 1/2 + 5/8 = (3/8 + 5/8) + 2 1/2 = 3 1/2.",
       "**Simplify before multiplying**: 4/9 × 3/8 — cancel 4 with 8 and 3 with 9: 1/3 × 1/2 = 1/6.",
       "**Distributive law**: 3/4 × 7 + 3/4 × 5 = 3/4 × 12 = 9."])
s.check(N("Work out 2/5 + 1 3/4 + 3/5 mentally.", 2.75, o="O6", reason="2/5 + 3/5 = 1; 1 + 1 3/4 = 2 3/4."))
s.mistake("Cancel across, not within addition", ["You can cancel common factors when multiplying fractions, but not when adding them."])


def e1(r):
    a = rf(r, (5, 7, 8, 9)); b = 1 - a; m = mixed(r, 1, 4, (2, 4))
    return F(f"Work out {frac(a)} + {frac(m, True)} + {frac(b)} mentally.", a + b + m, o="O6", reason=f"{frac(a)} + {frac(b)} = 1 first.")
def e2(r):
    f = rf(r, (3, 4, 5, 8)); x, y = r.randint(2, 9), r.randint(2, 9)
    while (f * (x + y)).denominator != 1: y += 1
    return N(f"Work out {frac(f)} × {x} + {frac(f)} × {y}.", float(f * (x + y)), tol=TOL, o="O6", reason=f"{frac(f)} × ({x} + {y}) = {frac(f)} × {x + y} = {fmt(float(f * (x + y)))}.")
def e3(r):
    a, b = rf(r, (4, 6, 8, 9, 10)), rf(r, (4, 6, 8, 9, 10))
    return F(f"Work out {frac(a)} × {frac(b)}, simplifying first.", a * b, o="O6")
def e4(r):
    f = rf(r, (4, 5, 8)); n = f.denominator * r.randint(2, 9)
    return N(f"Work out {n} × {frac(f)} × {f.denominator}/{f.numerator}.", n, o="O6", reason=f"{frac(f)} × {f.denominator}/{f.numerator} = 1, so the answer is {n}.")
def e5(r):
    rows = [("1/4 + 3/4", "1"), ("2/5 × 5/2", "1"), ("3/8 + 5/8", "1"), ("2/3 × 3/2", "1"), ("1/2 + 1/2", "1"), ("1/2 × 1/2", "1/4"), ("3/4 × 4", "3")]
    return GD("Find each answer.", "Answer", r.sample(rows, 4), o="O6", extra=["2", "1/2"])
def e6(r):
    f = rf(r, (3, 4, 5)); x = r.randint(12, 20); y = r.randint(2, x - 2)
    while (f * (x - y)).denominator != 1: y -= 1
    return N(f"Work out {frac(f)} × {x} − {frac(f)} × {y}.", float(f * (x - y)), tol=TOL, o="O6", d="H", reason=f"{frac(f)} × ({x} − {y}) = {fmt(float(f * (x - y)))}.")
def e7(r):
    a, b, c = rf(r, (3, 4, 6, 8)), rf(r, (3, 4, 6, 8)), rf(r, (3, 4, 6, 8))
    return TB(f"Work out {frac(a)} × {frac(b)} × {frac(c)} in two different orders.", ["Order", "Answer"], [[f"({frac(a)} × {frac(b)}) × {frac(c)}", B(float(a * b * c), TOL)], [f"{frac(a)} × ({frac(b)} × {frac(c)})", B(float(a * b * c), TOL)]], o="O6", d="H", reason="The associative law: the order of multiplying does not change the answer.")
def e8(r):
    return MC("Which law does 3/4 × 6 + 3/4 × 2 = 3/4 × 8 use?", "the distributive law", [("the commutative law", "That is swapping the order."), ("the associative law", "That is changing the grouping."), ("the inverse law", "")], o="O6")


s.std([e5, e7, e1, e2, e3, e4, e8, e6], EX("Explain the quickest way to work out 5/7 × 9 + 5/7 × 5.", [("take out 5/7: 5/7 × (9 + 5)", ["5/7 ?× ?\\(9|distributive|common|14"]), ("5/7 × 14 = 10", ["\\b10\\b"])], "Use the distributive law: 5/7 × 9 + 5/7 × 5 = 5/7 × (9 + 5) = 5/7 × 14 = 10.", o="O6"))

U.mindmap(("Recurring decimals", "Simplest form: only 2s and 5s in the denominator → terminating", "O1", "7.1"), ("Ordering", "Common denominator or decimals", "O2", "7.2"),
          ("Subtracting mixed numbers", "Regroup when the fraction is too small", "O3", "7.3"), ("Integer × mixed number", "Split or use improper fractions", "O4", "7.4"),
          ("Integer ÷ fraction", "Multiply by the reciprocal", "O5", "7.5"), ("Easier calculations", "Re-order • cancel first • distributive law", "O6", "7.6"))
