# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 8 Fractions. Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(8, "Fractions", "Number",
         "Recurring decimals as fractions, the order of operations with fractions, multiplying and dividing fractions and mixed numbers, and using number laws to make calculations easier.",
         {"O1": {"sec": "8.1", "code": "9Nf.01", "codeNote": "", "t": "Recognise fractions that give terminating or recurring decimals and convert recurring decimals to fractions."},
          "O2": {"sec": "8.2", "code": "9Nf.02", "codeNote": "", "t": "Use the order of operations with fractions, including powers and brackets."},
          "O3": {"sec": "8.3", "code": "9Nf.03", "codeNote": "", "t": "Multiply fractions and mixed numbers, simplifying and cancelling."},
          "O4": {"sec": "8.4", "code": "9Nf.04", "codeNote": "", "t": "Divide fractions and mixed numbers by multiplying by the reciprocal."},
          "O5": {"sec": "8.5", "code": "9Nf.06", "codeNote": "", "t": "Use the commutative, associative and distributive laws and simplifying to make calculations with fractions easier."}})
TOL = 1e-6
def rf(r, dens=(2, 3, 4, 5, 6, 8, 9, 10, 12)):
    d = pick(r, dens); n = r.randint(1, d - 1); return Fr(n, d)
def F(prompt, v, **kw):
    return N(prompt + " Give your answer as a fraction in its simplest form or a mixed number.", float(v), tol=TOL, reason=kw.pop("reason", f"= {frac(v)}" + (f" = {frac(v, True)}" if v > 1 and v.denominator > 1 else "")), **kw)

# ================================================================== 8.1
s = U.section("8.1", "Fractions and recurring decimals", ["O1"])
s.idea("Terminating or recurring?", ["Write the fraction in its simplest form. If the denominator has **only the prime factors 2 and 5**, the decimal **terminates** (stops): 3/8 = 0.375, 7/20 = 0.35.",
       "Any other prime factor gives a **recurring** decimal: 1/3 = 0.333…, 5/12 = 0.41666… A dot (or bar) shows the repeating digits: 0.4̇5̇ = 0.454545…"])
s.example("Recurring decimal to a fraction", "Write 0.272727… as a fraction.", [("x = 0.2727…", ""), ("100x = 27.2727…", "two digits repeat, so × 100"), ("99x = 27", "subtract"), ("x = 27/99 = 3/11", "")], "3/11")
s.check(MC("Which fraction gives a terminating decimal?", "7/40", [("2/3", "3 is not 2 or 5."), ("5/6", "6 = 2 × 3."), ("4/7", "")], o="O1"))
s.example("One digit repeating", "Write 0.7777… as a fraction.", [("10x = 7.777…", ""), ("9x = 7", ""), ("x = 7/9", "")], "7/9")
s.mistake("Simplify first", ["3/12 terminates, because it simplifies to 1/4. Always simplify before looking at the denominator."])
s.check(N("Write 0.4̇ (0.444…) as a fraction.", 4 / 9, tol=TOL, reason="x = 0.444…, 10x = 4.444…; subtract: 9x = 4, so x = 4/9.", o="O1"))
def r1(r):
    d = pick(r, [3, 6, 7, 9, 11, 12, 15, 4, 8, 16, 20, 25, 40, 50, 30]); n = r.randint(1, d - 1); f = Fr(n, d); den = f.denominator
    k = den
    for p_ in (2, 5):
        while k % p_ == 0: k //= p_
    return MC(f"Does {n}/{d} give a terminating or a recurring decimal?", "terminating" if k == 1 else "recurring", [("recurring" if k == 1 else "terminating", f"Simplify to {frac(f)}; look at the prime factors of {den}.")], o="O1")
def r2(r):
    a = r.randint(1, 98)
    return N(f"Write 0.{a:02d}{a:02d}{a:02d}… (the digits {a:02d} repeat) as a fraction in its simplest form.", a / 99, tol=TOL, o="O1", d="H", reason=f"x = {a}/99 = {frac(Fr(a,99))}.")
def r3(r):
    a = r.randint(1, 8)
    return N(f"Write 0.{a}{a}{a}… as a fraction.", a / 9, tol=TOL, reason=f"x = 0.{a}{a}…, 10x = {a}.{a}…; 9x = {a}, so x = {a}/9{' = ' + frac(Fr(a, 9)) if Fr(a, 9).denominator != 9 else ''}.", o="O1")
def r4(r):
    a, b = r.randint(1, 9), r.randint(1, 9)
    v = Fr(a, 10) + Fr(b, 90)
    return N(f"Write 0.{a}{b}{b}{b}… (only the {b} repeats) as a fraction in its simplest form.", float(v), tol=TOL, o="O1", d="VH", reason=f"10x = {a}.{b}{b}…, 100x = {a}{b}.{b}…; 90x = {10*a+b-a}; x = {frac(v)}.")
def r5(r):
    d = pick(r, [8, 16, 20, 25, 40, 32, 125]); n = r.randint(1, d - 1)
    return N(f"Write {n}/{d} as a decimal.", n / d, tol=TOL, reason=f"{n} ÷ {d} = {fmt(round(n / d, 6))}.", o="O1")
def r6(r):
    rows = []
    for d in r.sample([3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 16, 20, 24, 25], 4):
        f = Fr(1, d); k = d
        for p_ in (2, 5):
            while k % p_ == 0: k //= p_
        rows.append((f"1/{d}", "Terminating" if k == 1 else "Recurring"))
    return GD("Terminating or recurring?", "Decimal", rows, o="O1")
def r7(r):
    return OD("Put the steps in order to write 0.363636… as a fraction.", ["Let x = 0.3636…", "Multiply by 100: 100x = 36.3636…", "Subtract: 99x = 36", "Divide and simplify: x = 36/99 = 4/11"], o="O1", skill="Data")
s.core(r1(s.rng), r2(s.rng), r3(s.rng), r5(s.rng), r6(s.rng), r7(s.rng), r4(s.rng),
       EX("Explain how you can tell, without dividing, that 9/40 is a terminating decimal.", [("40 = 2 × 2 × 2 × 5", ["2 ?(×|x) ?2|2³|prime factors|2s and 5|2 and 5"]), ("only factors 2 and 5 give a terminating decimal", ["only|terminat"])], "40 = 2³ × 5 has only the prime factors 2 and 5, and 9/40 is in its simplest form, so its decimal terminates.", o="O1", d="H"))
s.gen("p", 44, r1, r2, r3, r4, r5, r6)
s.gen("a", 8, r4, lambda r: (lambda a: N(f"Write 1.{a:03d}{a:03d}… (the three digits {a:03d} repeat) as a fraction (or mixed number).", 1 + a / 999, tol=TOL, reason=f"x = 0.{a:03d}…: 1000x − x = {a}, so 0.{a:03d}… = {a}/999; the number is 1 + {frac(Fr(a, 999))}.", o="O1", d="VH"))(r.randint(1, 998)))

# ================================================================== 8.2
s = U.section("8.2", "Fractions and the order of operations", ["O2"])
s.idea("Order of operations", ["Brackets, then **powers and roots**, then **× and ÷**, then **+ and −** – the same rules as whole numbers.", "(2/3)² = 4/9: square the numerator and the denominator."])
s.example("Mixed operations", "Work out 1/2 + 3/4 × 2/3.", [("3/4 × 2/3 = 1/2", "multiply first"), ("1/2 + 1/2 = 1", "")], "1")
s.check(N("Work out (1/2)³.", 0.125, tol=TOL, reason="1/2 × 1/2 × 1/2 = 1/8 = 0.125.", o="O2"))
s.example("Brackets and powers", "Work out (1/3 + 1/6)² × 8.", [("1/3 + 1/6 = 1/2", "brackets"), ("(1/2)² = 1/4", "power"), ("1/4 × 8 = 2", "")], "2")
s.mistake("Left to right is not always right", ["2/5 + 1/5 × 10 = 2/5 + 2 = 2 2/5, not (3/5) × 10 = 6."])
s.check(MC("Work out 3/4 − 1/4 ÷ 1/2.", "1/4", [("1", "Divide before subtracting."), ("1/2", ""), ("1/8", "")], o="O2", d="H"))
def o1(r):
    a, b, c = rf(r), rf(r), rf(r)
    return F(f"Work out {frac(a)} + {frac(b)} × {frac(c)}.", a + b * c, o="O2", d="M")
def o2(r):
    a, b = rf(r), rf(r); n = r.randint(2, 3)
    return F(f"Work out ({frac(a)} + {frac(b)}){sup(n)}.", (a + b) ** n, o="O2", d="H")
def o3(r):
    a, b, c = rf(r), rf(r), rf(r)
    return F(f"Work out {frac(a)} × ({frac(b)} − {frac(c)}).", a * (b - c), o="O2", d="H")
def o4(r):
    a = rf(r, (2, 3, 4, 5)); k = r.randint(2, 12)
    return F(f"Work out {k} − ({frac(a)})² × {k}.", k - a * a * k, o="O2", d="H")
def o5(r):
    a, b, c = rf(r), rf(r), rf(r)
    return F(f"Work out {frac(a)} ÷ {frac(b)} − {frac(c)}.", a / b - c, o="O2", d="H")
def o6(r):
    a = rf(r, (2, 3, 4, 5, 9))
    return F(f"Work out √({frac(a*a)}) + {frac(a)}².", a + a * a, o="O2", d="H") if (a * a).denominator <= 100 else None
def o7(r):
    a, b, c = rf(r, (2, 3, 4)), rf(r, (2, 3, 4)), rf(r, (2, 3, 4))
    good = a + b * c; wrong = (a + b) * c
    if good == wrong: return None
    return MC(f"Work out {frac(a)} + {frac(b)} × {frac(c)}.", frac(good), [(frac(wrong), "Multiply before adding."), (frac(a + b + c), ""), (frac(a * b * c), "")], o="O2")
def o8(r):
    return TB("Complete the table.", ["Calculation", "Answer"], [["1/2 + 1/4 × 2", B(1)], ["(1/2 + 1/4) × 2", B(1.5)], ["(2/3)² − 1/9", B(1 / 3, 1e-6)]], reason="Multiply before adding: 1/2 + 1/2 = 1. Brackets first: 3/4 × 2 = 3/2. Powers first: 4/9 − 1/9 = 1/3.", o="O2", d="H")
s.core(o1(s.rng), o2(s.rng), o3(s.rng), o5(s.rng), o7(s.rng) or o1(s.rng), o8(s.rng),
       GD("Which operation is done first?", "First step", [("1/2 + 1/3 × 6", "×"), ("(1/2 + 1/3) × 6", "+"), ("1/2 ÷ (1/4)²", "power"), ("3/4 − 1/2 ÷ 2", "÷")], o="O2"),
       EX("Explain why (1/2)² is smaller than 1/2.", [("(1/2)² = 1/4", ["1/4|0\\.25|quarter"]), ("multiplying by a number less than 1 makes it smaller", ["less than 1|smaller than 1|half of a half|makes it smaller"])], "(1/2)² = 1/2 × 1/2 = 1/4. Multiplying by a number less than 1 makes the result smaller, so 1/4 < 1/2.", o="O2"))
s.gen("p", 44, o1, o2, o3, o4, o5, o6, o7)
s.gen("a", 8, lambda r: (lambda a, b: F(f"Work out (1 − {frac(a)})² ÷ ({frac(b)} + 1/2).", (1 - a) ** 2 / (b + Fr(1, 2)), o="O2", d="VH"))(rf(r), rf(r)), o2)

# ================================================================== 8.3
s = U.section("8.3", "Multiplying fractions", ["O3"])
s.idea("Multiplying fractions", ["Multiply the numerators and multiply the denominators. **Cancel first** to keep numbers small: 4/9 × 3/8 = (1 × 1)/(3 × 2) = 1/6.",
       "For **mixed numbers**, change them to improper fractions first: 2 1/3 = 7/3."])
s.example("Mixed numbers", "Work out 2 1/3 × 1 4/5.", [("7/3 × 9/5", "improper fractions"), ("cancel 3 with 9: 7/1 × 3/5", ""), ("21/5 = 4 1/5", "")], "4 1/5")
s.check(N("Work out 3/4 × 8/9.", 2 / 3, tol=TOL, reason="Cancel first: 3/4 × 8/9 = (1 × 2)/(1 × 3) = 2/3.", o="O3"))
s.example("Fraction of an amount", "Find 5/8 of 3 1/5 kg.", [("5/8 × 16/5", ""), ("= 2", "cancel 5 and 8")], "2 kg")
s.mistake("Mixed numbers", ["2 1/2 × 3 1/3 is NOT 6 1/6. Change to 5/2 × 10/3 = 50/6 = 8 1/3."])
s.check(MC("Work out 1 1/2 × 2 1/2.", "3 3/4", [("2 1/4", "Change to improper fractions first."), ("3 1/4", ""), ("4", "")], o="O3", d="H"))
def mx(r): w = r.randint(1, 4); f = rf(r); return w + f
def m1(r):
    a, b = rf(r), rf(r); return F(f"Work out {frac(a)} × {frac(b)}.", a * b, o="O3")
def m2(r):
    a, b = mx(r), mx(r); return F(f"Work out {frac(a, True)} × {frac(b, True)}.", a * b, o="O3", d="H")
def m3(r):
    a = rf(r); q = r.randint(2, 20) * a.denominator; return N(f"Find {frac(a)} of {q}.", float(a * q), tol=TOL, reason=f"{q} ÷ {a.denominator} × {a.numerator} = {fmt(float(a * q))}.", o="O3")
def m4(r):
    a, b = mx(r), rf(r); return F(f"Find {frac(b)} of {frac(a, True)} metres.", a * b, unit="m", units=["m"], o="O3", d="H")
def m5(r):
    a, b, c = rf(r), rf(r), rf(r); return F(f"Work out {frac(a)} × {frac(b)} × {frac(c)}.", a * b * c, o="O3", d="H")
def m6(r):
    l, w = mx(r), mx(r); return F(f"A rectangle measures {frac(l, True)} m by {frac(w, True)} m. Find its area.", l * w, unit="m²", units=["m²", "m"], o="O3", d="H", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]], "s": [f"{frac(l, True)} m", f"{frac(w, True)} m", "", ""]})
def m7(r):
    a, b = rf(r), rf(r)
    return MC(f"Which is the best estimate of {frac(a, True)} × {frac(b + 3, True)}?", fmt(round(float(a) * round(float(b + 3)), 1)), [(fmt(round(float(b + 3)) + 1), ""), (fmt(round(float(a) + float(b + 3))), ""), ("0", "")], o="O3") if round(float(a) * round(float(b + 3)), 1) not in (round(float(b + 3)) + 1, round(float(a) + float(b + 3)), 0) else None
def m8(r):
    a, b = Fr(r.randint(2, 7), 1), rf(r); x = a * b
    return TB("Complete the table.", ["×", frac(b), "1 1/2"], [[frac(a), B(float(x), 1e-6), B(float(a * Fr(3, 2)), 1e-6)]], reason=f"Multiply numerators and denominators: {frac(a)} × {frac(b)} = {frac(x)}; 1 1/2 = 3/2, so {frac(a)} × 3/2 = {frac(a * Fr(3, 2))}.", o="O3")
s.core(m1(s.rng), m2(s.rng), m3(s.rng), m4(s.rng), m6(s.rng), m8(s.rng), m5(s.rng),
       EX("Explain why 2/3 × 3/4 is smaller than both 2/3 and 3/4.", [("multiplying by a fraction less than 1 makes it smaller", ["less than 1|smaller|part of"]), ("answer is 1/2", ["1/2|half|0\\.5"])], "Multiplying by a number less than 1 gives a smaller answer. 2/3 × 3/4 = 1/2, which is smaller than both.", o="O3"))
s.gen("p", 44, m1, m2, m3, m4, m5, m6, m8)
s.gen("a", 8, m2, m5, lambda r: (lambda a: F(f"Work out (1 + {frac(a)})(1 − {frac(a)}).", 1 - a * a, o="O3", d="VH"))(rf(r)))

# ================================================================== 8.4
s = U.section("8.4", "Dividing fractions", ["O4"])
s.idea("Dividing fractions", ["To divide by a fraction, **multiply by its reciprocal** (turn it upside down): 3/4 ÷ 2/5 = 3/4 × 5/2 = 15/8.", "Change mixed numbers to improper fractions first. Dividing by a fraction less than 1 gives a **bigger** answer."])
s.example("Mixed numbers", "Work out 3 1/2 ÷ 1 3/4.", [("7/2 ÷ 7/4", ""), ("7/2 × 4/7", "reciprocal"), ("= 2", "")], "2")
s.check(N("Work out 2/3 ÷ 4/9.", 1.5, tol=TOL, reason="2/3 × 9/4 = 18/12 = 3/2 = 1.5.", o="O4"))
s.example("How many fit?", "How many 3/8 kg bags can be filled from 6 kg?", [("6 ÷ 3/8", ""), ("6 × 8/3 = 16", "")], "16 bags")
s.mistake("Flip the second fraction only", ["2/3 ÷ 4/5 = 2/3 × 5/4. Do not turn the first fraction upside down."])
s.check(MC("Work out 5 ÷ 1/4.", "20", [("5/4", "Dividing by 1/4 means how many quarters in 5."), ("1 1/4", ""), ("4/5", "")], o="O4"))
def d1(r):
    a, b = rf(r), rf(r); return F(f"Work out {frac(a)} ÷ {frac(b)}.", a / b, o="O4")
def d2(r):
    a, b = Fr(r.randint(1, 5)) + rf(r), Fr(r.randint(1, 3)) + rf(r); return F(f"Work out {frac(a, True)} ÷ {frac(b, True)}.", a / b, o="O4", d="H")
def d3(r):
    b = rf(r, (2, 3, 4, 5, 8)); k = r.randint(2, 12) * b.numerator
    return N(f"How many pieces of length {frac(b)} m can be cut from {k} m of wire?", float(k / b), "pieces", units=["pieces", "m"], reason=f"{k} ÷ {frac(b)} = {k} × {b.denominator}/{b.numerator} = {fmt(float(k / b))}.", o="O4")
def d4(r):
    a = Fr(r.randint(1, 4)) + rf(r); n = r.randint(2, 9); return F(f"Work out {frac(a, True)} ÷ {n}.", a / n, o="O4")
def d5(r):
    a, b = rf(r), rf(r); return F(f"A rectangle has area {frac(a*b)} m² and width {frac(b)} m. Find its length.", a, unit="m", units=["m", "m²"], o="O4", d="H", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]], "s": ["length", f"{frac(b)} m", "", ""], "note": f"area {frac(a*b)} m²"})
def d6(r):
    a = rf(r); return MC(f"Which is equal to 6 ÷ {frac(a)}?", f"6 × {a.denominator}/{a.numerator}", [(f"6 × {frac(a)}", "Use the reciprocal."), (f"{a.denominator}/{6*a.numerator}" , ""), (f"6/{a.denominator}", "")], o="O4")
def d7(r):
    a, b = rf(r), rf(r)
    return GD(f"Is the answer bigger or smaller than 10?", "Answer", [(f"10 ÷ {frac(a)}", "Bigger"), (f"10 × {frac(a)}", "Smaller"), (f"10 ÷ {frac(b + 1, True)}", "Smaller")], o="O4", d="H")
s.core(d1(s.rng), d2(s.rng), d3(s.rng), d4(s.rng), d5(s.rng), d6(s.rng), d7(s.rng),
       EX("Explain why 4 ÷ 1/2 = 8.", [("how many halves in 4", ["how many halves|halves in|half"]), ("there are 2 halves in each whole: 4 × 2 = 8", ["4 ?(×|x) ?2|2 in each|two in each|8"])], "Dividing by 1/2 asks how many halves fit into 4. There are 2 halves in each whole, so 4 × 2 = 8 halves.", o="O4"))
s.gen("p", 44, d1, d2, d3, d4, d5, d6, d7)
s.gen("a", 8, d2, lambda r: (lambda a, b, c: F(f"Work out ({frac(a)} ÷ {frac(b)}) ÷ {frac(c)}.", a / b / c, o="O4", d="VH"))(rf(r), rf(r), rf(r)))

# ================================================================== 8.5
s = U.section("8.5", "Making calculations easier", ["O5"])
s.idea("Number laws", ["**Commutative**: order does not matter for + and × (a × b = b × a). **Associative**: grouping does not matter for + and × ((a × b) × c = a × (b × c)). **Distributive**: a × (b + c) = a × b + a × c.",
       "Use them to group 'nice' numbers: 3/7 × 5 × 7/3 = (3/7 × 7/3) × 5 = 1 × 5 = 5."])
s.example("Distributive law", "Work out 3/4 × 17 + 3/4 × 3.", [("3/4 × (17 + 3)", "take out the common factor"), ("3/4 × 20 = 15", "")], "15")
s.check(N("Work out 2/5 × 13 − 2/5 × 3.", 4, tol=TOL, reason="2/5 × (13 − 3) = 2/5 × 10 = 4.", o="O5"))
s.example("Reorder", "Work out 2/3 + 4/5 + 1/3.", [("(2/3 + 1/3) + 4/5", "commutative and associative laws"), ("1 + 4/5 = 1 4/5", "")], "1 4/5")
s.mistake("Not for − and ÷", ["Subtraction and division are NOT commutative: 1/2 − 1/4 ≠ 1/4 − 1/2."])
s.check(MC("Which law is used in 5/6 × 12 = 12 × 5/6?", "commutative", [("associative", ""), ("distributive", ""), ("inverse", "")], o="O5"))
def e1(r):
    a = rf(r); x, y = r.randint(3, 30), r.randint(1, 20); s_ = x + y
    if (a * s_).denominator != 1: return None
    return N(f"Use the distributive law to work out {frac(a)} × {x} + {frac(a)} × {y}.", float(a * s_), tol=TOL, reason=f"{frac(a)} × ({x} + {y}) = {frac(a)} × {s_} = {fmt(float(a * s_))}.", o="O5")
def e2(r):
    a = rf(r); k = r.randint(2, 15)
    return N(f"Work out {frac(a)} × {k} × {a.denominator}/{a.numerator} without a calculator.", k, tol=TOL, reason=f"{frac(a)} × {a.denominator}/{a.numerator} = 1, so the answer is {k}.", o="O5", d="M")
def e3(r):
    a = rf(r); b = 1 - a; c = rf(r)
    return F(f"Work out {frac(a)} + {frac(c)} + {frac(b)} by grouping.", 1 + c, o="O5")
def e4(r):
    rows = [("a + b = b + a", "Commutative"), ("(a × b) × c = a × (b × c)", "Associative"), ("a(b + c) = ab + ac", "Distributive")]
    return MT("Match each law with its example.", rows, o="O5", skill="Data")
def e5(r):
    a = rf(r); k = r.randint(11, 99); m = a.denominator
    return N(f"Work out {frac(a)} × {k * m} using a quick method.", float(a * k * m), tol=TOL, reason=f"{k * m} ÷ {m} = {k}, then × {a.numerator} = {fmt(float(a * k * m))}.", o="O5")
def e6(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return N(f"Work out {a} 1/2 × 4 − 1/2 × 4.", a * 4, tol=TOL, o="O5", d="H", reason=f"(({a} 1/2) − 1/2) × 4 = {a} × 4.")
def e7(r):
    return TK("Is each statement always true?", ["True", "False"], [("1/2 × 3/4 = 3/4 × 1/2", ["✓", "✗"]), ("1/2 ÷ 3/4 = 3/4 ÷ 1/2", ["✗", "✓"]), ("(1/2 + 1/3) + 1/6 = 1/2 + (1/3 + 1/6)", ["✓", "✗"]), ("1/2 − 1/3 = 1/3 − 1/2", ["✗", "✓"])], o="O5")
s.core(e1(s.rng) or e2(s.rng), e2(s.rng), e3(s.rng), e4(s.rng), e5(s.rng), e6(s.rng), e7(s.rng),
       EX("Show a quick way to work out 7/9 × 45 + 2/9 × 45.", [("(7/9 + 2/9) × 45", ["7/9 ?\\+ ?2/9|common factor|distributive|take out 45"]), ("= 1 × 45 = 45", ["\\b45\\b"])], "Take out the common factor 45: (7/9 + 2/9) × 45 = 1 × 45 = 45.", o="O5", d="H"))
s.gen("p", 44, e1, e2, e3, e5, e6)
s.gen("a", 8, e5, lambda r: (lambda a: N(f"Work out 99 × {frac(a)} + {frac(a)} using a quick method.", float(100 * a), tol=TOL, reason=f"99 × {frac(a)} + 1 × {frac(a)} = 100 × {frac(a)} = {fmt(float(100 * a))}.", o="O5", d="VH"))(rf(r)))

U.mindmap(("Recurring decimals", "Denominator with only 2s and 5s terminates • 0.ȧ = a/9", "O1", "8.1"), ("Order of operations", "Brackets, powers, × ÷, + −", "O2", "8.2"),
          ("Multiplying", "Cancel first • mixed numbers → improper", "O3", "8.3"), ("Dividing", "× the reciprocal", "O4", "8.4"), ("Number laws", "Commutative, associative, distributive", "O5", "8.5"))
