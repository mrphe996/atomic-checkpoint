# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 1 Number and calculation (1.1 Irrational numbers, 1.2 Standard form, 1.3 Indices). Written by the Atomic teaching team."""
import math
from fractions import Fraction as Fr
from kit import *

U = Unit(1, "Number and Calculation", "Number",
         "Rational and irrational numbers, estimating roots, standard form for very large and very small numbers, and the laws of indices.",
         {"O1": {"sec": "1.1", "code": "9Ni.01", "codeNote": "", "t": "Tell rational numbers from irrational numbers and explain why a number is irrational."},
          "O2": {"sec": "1.1", "code": "9Ni.04", "codeNote": "", "t": "Estimate square roots and cube roots, and say which two whole numbers a surd lies between."},
          "O3": {"sec": "1.2", "code": "9Ni.03", "codeNote": "", "t": "Write and order numbers in standard form, and calculate with numbers in standard form."},
          "O4": {"sec": "1.3", "code": "9Ni.02", "codeNote": "", "t": "Use positive, zero and negative indices and the laws of indices for multiplication, division and powers."}})

SQ = [n * n for n in range(1, 21)]; CU = [n ** 3 for n in range(1, 11)]

# ================================================================== 1.1 Irrational numbers
s = U.section("1.1", "Irrational numbers", ["O1", "O2"])
s.idea("Rational and irrational numbers", ["A **rational number** can be written as a fraction a/b where a and b are integers and b is not 0. Every integer, every fraction, every terminating decimal (0.375 = 3/8) and every recurring decimal (0.333… = 1/3) is rational.",
       "An **irrational number** cannot be written as a fraction. Its decimal goes on for ever **without repeating**. Examples: √2 = 1.41421356…, √10, ∛5 and π = 3.14159…",
       "The square root of a whole number is rational only if the number is a **square number**: √49 = 7 is rational, √50 is irrational. In the same way, a cube root of a whole number is rational only for cube numbers."])
s.method("Is it rational?", ["Ask: can it be written exactly as a fraction of two integers?"],
         steps=[("Integer or fraction?", "→ rational"), ("Decimal that stops or repeats?", "→ rational"), ("√n with n a square number, ∛n with n a cube?", "→ rational"), ("Any other root, or π?", "→ irrational")])
s.example("Sorting numbers", "Which of these are irrational? 0.7, √36, √20, 2/9, ∛27, π, 0.121212…",
          [("√36 = 6, ∛27 = 3", "square and cube numbers give whole numbers"), ("0.7 = 7/10, 2/9, 0.1212… = 12/99", "fractions and recurring decimals are rational"), ("√20, π", "20 is not a square number; π never repeats")],
          "√20 and π are irrational.")
s.check(MS("Select ALL the irrational numbers.", ["√7", "π", "∛10"], ["√64", "0.25", "4/11"], d="M", o="O1"))
s.idea("Estimating roots", ["To find the two whole numbers a root lies between, find the **square numbers either side**. 40 lies between 36 and 49, so √40 lies between √36 = 6 and √49 = 7.",
       "√40 is closer to 6 than to 7, because 40 is much closer to 36 than to 49. A good estimate is about 6.3."])
s.example("Between which whole numbers?", "Between which two consecutive whole numbers does ∛90 lie?",
          [("4³ = 64, 5³ = 125", "find the cube numbers either side of 90"), ("64 < 90 < 125", ""), ("4 < ∛90 < 5", "take cube roots")], "∛90 lies between 4 and 5.")
s.check(N("√75 lies between two consecutive whole numbers. What is the smaller one?", 8, d="M", o="O2", reason="64 < 75 < 81, so 8 < √75 < 9."))
s.mistake("Halving instead of rooting", ["√50 is NOT 25. A square root asks which number multiplied by ITSELF gives 50. 7 × 7 = 49, so √50 is just over 7."])
s.check(MC("Which is the best estimate of √50?", "7.1", [("25", "25 is half of 50, not its square root."), ("5", "5 × 5 = 25, not 50."), ("7.9", "7.9² is about 62, too big.")], d="M", o="O2"))

def t_between(r):
    k = r.choice(["square", "cube"])
    if k == "square":
        n = r.randint(2, 18); v = r.randint(n * n + 1, (n + 1) ** 2 - 1)
        return N(f"√{v} lies between two consecutive whole numbers. Write the larger one.", n + 1, o="O2", d="M", reason=f"{n}² = {n*n} and {n+1}² = {(n+1)**2}. {n*n} < {v} < {(n+1)**2}, so {n} < √{v} < {n+1}.")
    n = r.randint(2, 9); v = r.randint(n ** 3 + 1, (n + 1) ** 3 - 1)
    return N(f"∛{v} lies between two consecutive whole numbers. Write the smaller one.", n, o="O2", d="M", reason=f"{n}³ = {n**3} and {n+1}³ = {(n+1)**3}, so {n} < ∛{v} < {n+1}.")

def t_rational(r):
    pool_r = [f"√{pick(r, SQ[3:])}", f"∛{pick(r, CU[1:])}", f"{r.randint(2, 9)}/{r.randint(11, 19)}", f"0.{r.randint(1, 9)}{r.randint(1, 9)}", f"{r.randint(-9, -1)}", f"0.{r.randint(1,9)}{r.randint(1,9)}{r.randint(1,9)}…(repeating)"]
    nonsq = [x for x in range(2, 99) if x not in SQ]; noncu = [x for x in range(2, 99) if x not in CU]
    pool_i = [f"√{pick(r, nonsq)}", f"∛{pick(r, noncu)}", "π", f"2π", f"√{pick(r, nonsq)} + 1"]
    ri = r.sample(pool_i, 2); rr = r.sample(pool_r, 3)
    rows = [(x, "Irrational") for x in ri] + [(x, "Rational") for x in rr]; r.shuffle(rows)
    return GD("Is each number rational or irrational?", "Type", rows, o="O1", d="M", reason="Square roots of non-square numbers, cube roots of non-cube numbers and π are irrational; integers, fractions and terminating or recurring decimals are rational.")

def t_est(r):
    v = pick(r, [x for x in range(10, 200) if x not in SQ]); a = math.sqrt(v)
    return N(f"Estimate √{v} to 1 decimal place without a calculator, then check with one. Give √{v} correct to 1 decimal place.", round(a, 1), o="O2", d="H", tol=0.05,
             reason=f"{int(a)}² = {int(a)**2} and {int(a)+1}² = {(int(a)+1)**2}; √{v} ≈ {a:.3f} → {a:.1f}.")

def t_which_rational(r):
    n = r.randint(2, 12); good = f"√{n*n}"; bads = [f"√{n*n + d}" for d in (1, 2)] + [f"√{2*n}"]
    return MC("Which of these numbers is rational?", good, [(b, "This is the square root of a non-square number, so it is irrational.") for b in bads], o="O1", d="M", reason=f"{n*n} is a square number, so √{n*n} = {n}.")

def t_order(r):
    nums = sorted(r.sample([x for x in range(5, 120) if x not in SQ], 3))
    items = [f"√{nums[0]}", f"√{nums[1]}", f"√{nums[2]}"]; whole = r.randint(int(math.sqrt(nums[0])) + 1, 11)
    allv = sorted([(math.sqrt(n), f"√{n}") for n in nums] + [(whole, str(whole))])
    if len({round(v, 6) for v, _ in allv}) < 4: return None
    return OD("Put these numbers in order, smallest first.", [t for _, t in allv], o="O2", d="H", reason="Compare the squares: " + ", ".join(f"{t}² = {round(v*v)}" for v, t in allv) + ".")

def t_product(r):
    a = pick(r, [2, 3, 5, 6, 7]); b = a * pick(r, [4, 9, 16])
    return MC(f"Is √{a} × √{b} rational or irrational?", "rational", [("irrational", "Multiply first: √a × √b = √(ab).")], o="O1", d="H", reason=f"√{a} × √{b} = √{a*b} = {int(math.sqrt(a*b))}, a whole number, so it is rational.")

def t_side(r):
    a = pick(r, [x for x in range(8, 150) if x not in SQ])
    return N(f"A square has an area of {a} cm². Find its side length correct to 2 decimal places.", round(math.sqrt(a), 2), "cm", units=["cm", "cm²"], o="O2", d="H", tol=0.006, reason=f"side = √{a} = {math.sqrt(a):.4f}… ≈ {math.sqrt(a):.2f} cm. The side is irrational because {a} is not a square number.")

def t_recur(r):
    a = r.randint(1, 8); d = pick(r, [3, 9, 11])
    f = Fr(a, d); dec = f"{float(f):.6f}"
    return MC(f"{a}/{d} = {dec}… What type of number is {a}/{d}?", "rational – it is a fraction of two integers", [("irrational – its decimal does not stop", "A decimal that repeats is still rational."), ("irrational – it has many decimal places", "Many decimal places does not make a number irrational.")], o="O1", d="M")

def t_cube(r):
    n = r.randint(2, 10)
    return N(f"Work out ∛{n**3}.", n, o="O2", d="M", reason=f"{n} × {n} × {n} = {n**3}.")

s.core(t_rational(s.rng), MS("Select ALL the rational numbers.", ["√121", "0.8", "−5/6"], ["√12", "π", "∛20"], o="O1"),
       N("√90 lies between two consecutive whole numbers. Write the smaller one.", 9, o="O2", reason="81 < 90 < 100 so 9 < √90 < 10."),
       N("∛200 lies between two consecutive whole numbers. Write the larger one.", 6, o="O2", reason="125 < 200 < 216 so 5 < ∛200 < 6."),
       TB("Complete the table. Write the two whole numbers that each root lies between.", ["Root", "Lower whole number", "Upper whole number"], [["√30", B(5), B(6)], ["√130", B(11), B(12)], ["∛50", B(3), B(4)]], o="O2", reason="25 < 30 < 36; 121 < 130 < 144; 27 < 50 < 64."),
       MC("Which is the best estimate of √110?", "10.5", [("55", "That is half of 110."), ("11.5", "11.5² = 132.25 – too big."), ("10", "10² = 100, a little small.")], o="O2", d="H"),
       EX("Sam says '√2 × √2 is irrational because √2 is irrational.' Is Sam right? Explain.", [("no / Sam is wrong", ["\\bno\\b|wrong|not right|incorrect"]), ("√2 × √2 = 2", ["= ?2\\b|equals 2|is 2"]), ("2 is an integer / a fraction, so rational", ["rational|integer|whole number|fraction"])],
          "No, Sam is wrong. √2 × √2 = 2, and 2 is an integer, so it is rational.", o="O1", d="H"),
       t_side(s.rng))
s.gen("p", 44, t_between, t_rational, t_est, t_which_rational, t_order, t_product, t_side, t_recur, t_cube)
s.gen("a", 8,
      lambda r: (lambda a: N(f"√{a} = {math.sqrt(a):.6f}… Use a calculator to find the integer n such that n < √{a}·√{a+1} < n + 1.", int(math.sqrt(a * (a + 1))), o="O2", d="VH", reason=f"√{a}·√{a+1} = √{a*(a+1)} ≈ {math.sqrt(a*(a+1)):.3f}."))(r.randint(10, 60)),
      lambda r: EX("Explain why √n is irrational when n lies strictly between two consecutive square numbers.", [("√n lies between two consecutive integers", ["between|integer|whole number"]), ("so √n is not an integer", ["not (an )?(integer|whole)"]), ("square root of a whole number is either an integer or irrational", ["irrational|cannot be a fraction|not a fraction"])],
                   "If k² < n < (k+1)², then k < √n < k+1, so √n is not an integer. The square root of a whole number is either an integer or irrational, so √n is irrational.", o="O1", d="VH"),
      lambda r: (lambda k: N(f"How many whole numbers n make √n lie between {k} and {k+1} (not including the ends)?", 2 * k, o="O2", d="VH", reason=f"n can be {k*k+1} to {(k+1)**2-1}: that is {2*k} numbers."))(r.randint(4, 20)),
      lambda r: MC("Which statement is always true?", "rational × rational is rational", [("irrational × irrational is irrational", "√3 × √3 = 3 is rational."), ("irrational + rational can be rational", "An irrational plus a rational is always irrational."), ("√(irrational) is rational", "It cannot become rational.")], o="O1", d="VH"),
      lambda r: (lambda a: N(f"A circle has area {a}π cm². Its radius is irrational. Write the radius correct to 2 decimal places.", round(math.sqrt(a), 2), "cm", units=["cm", "cm²"], tol=0.006, o="O2", d="VH", reason=f"πr² = {a}π → r² = {a} → r = √{a} ≈ {math.sqrt(a):.3f} cm."))(pick(r, [x for x in range(5, 80) if x not in SQ])))

# ================================================================== 1.2 Standard form
s = U.section("1.2", "Standard form", ["O3"])
s.idea("Writing numbers in standard form", ["A number in **standard form** is written **A × 10ⁿ** where **1 ≤ A < 10** and n is an integer.",
       "Large numbers have a positive power: 4 300 000 = 4.3 × 10⁶ (the decimal point moves 6 places).",
       "Small numbers have a negative power: 0.000 072 = 7.2 × 10⁻⁵ (the point moves 5 places to the right, so the power is −5)."])
s.example("Large number", "Write 58 000 000 in standard form.", [("5.8", "put the point after the first non-zero digit"), ("count the places: 7", "58 000 000 = 5.8 × 10 000 000"), ("5.8 × 10⁷", "")], "5.8 × 10⁷")
s.check(MC("Which is 360 000 written in standard form?", "3.6 × 10⁵", [("36 × 10⁴", "A must be between 1 and 10."), ("3.6 × 10⁴", "Count again: 3.6 × 10 000 = 36 000."), ("0.36 × 10⁶", "A must be at least 1.")], o="O3"))
s.example("Small number", "Write 0.000 504 in standard form.", [("5.04", "first non-zero digit is 5"), ("the point moves 4 places right", "0.000 504 → 5.04"), ("5.04 × 10⁻⁴", "moving right means a negative power")], "5.04 × 10⁻⁴")
s.method("Calculating in standard form", ["Multiply: multiply the A parts and **add** the powers. Divide: divide the A parts and **subtract** the powers. Then make sure A is between 1 and 10."],
         steps=[("(3 × 10⁴) × (5 × 10⁶) = 15 × 10¹⁰", "3 × 5 = 15, 4 + 6 = 10"), ("15 × 10¹⁰ = 1.5 × 10¹¹", "adjust so that 1 ≤ A < 10")])
s.check(N("Work out (2 × 10³) × (4 × 10⁵). Give the answer as an ordinary number.", 800000000, o="O3", d="M", reason="8 × 10⁸ = 800 000 000."))
s.mistake("A must be between 1 and 10", ["23 × 10⁴ is NOT standard form. Write 23 as 2.3 × 10¹ and add the powers: 2.3 × 10⁵."])
s.check(MC("Write 23 × 10⁴ correctly in standard form.", "2.3 × 10⁵", [("2.3 × 10³", "23 = 2.3 × 10, so the power goes UP by 1."), ("23 × 10⁴", "A must be less than 10.")], o="O3", d="H"))

def big(r):
    m = r.randint(11, 99) / 10; e = r.randint(4, 9); return m, e, round(m * 10 ** e)
def t_to_sf(r):
    m, e, v = big(r)
    return MC(f"Write {fmt(v)} in standard form.", f"{fmt(m)} × 10{sup(e)}", [(f"{fmt(m)} × 10{sup(e-1)}", "Count the places the point moves."), (f"{fmt(m*10)} × 10{sup(e-1)}", "A must be less than 10."), (f"{fmt(m)} × 10{sup(e+1)}", "Count the places again.")], o="O3", reason=f"{fmt(v)} = {fmt(m)} × {fmt(10**e)} = {fmt(m)} × 10{sup(e)}.")
def t_small(r):
    m = r.randint(11, 99) / 10; e = -r.randint(2, 7); v = m * 10 ** e
    return N(f"Write {stdform(v)} as an ordinary number.", round(v, 12), o="O3", d="M", reason=f"A negative power moves the point {-e} places left: {fmt(round(v, 12))}.")
def t_from_sf(r):
    m, e, v = big(r)
    return N(f"Write {fmt(m)} × 10{sup(e)} as an ordinary number.", v, o="O3", reason=f"Move the point {e} places right: {fmt(v)}.")
def t_small_to(r):
    m = r.randint(11, 99) / 10; e = -r.randint(3, 7); v = round(m * 10 ** e, 12)
    return N(f"Write {fmt(v)} in standard form. Type it like 3.2 × 10^-5.", v, o="O3", d="M", reason=f"{fmt(v)} = {stdform(v)}.")
def t_mul(r):
    a, b = r.randint(2, 9), r.randint(2, 9); e1, e2 = r.randint(2, 8), r.randint(2, 8); v = a * b * 10 ** (e1 + e2)
    return N(f"Work out ({a} × 10{sup(e1)}) × ({b} × 10{sup(e2)}). Give your answer in standard form, typed like 4.5 × 10^9.", v, o="O3", d="H", reason=f"{a} × {b} = {a*b}; 10{sup(e1)} × 10{sup(e2)} = 10{sup(e1+e2)}; {a*b} × 10{sup(e1+e2)} = {stdform(v)}.")
def t_div(r):
    b = r.randint(2, 5); c = r.randint(2, 9); a = b * c; e1, e2 = r.randint(6, 12), r.randint(1, 5); v = c * 10 ** (e1 - e2)
    return N(f"Work out ({a} × 10{sup(e1)}) ÷ ({b} × 10{sup(e2)}). Give your answer in standard form.", v, o="O3", d="H", reason=f"{a} ÷ {b} = {c}; 10{sup(e1)} ÷ 10{sup(e2)} = 10{sup(e1-e2)}; answer {stdform(v)}.")
def t_order_sf(r):
    vals = set()
    while len(vals) < 4: vals.add((r.randint(11, 99) / 10, r.randint(-6, 7)))
    vals = sorted(vals, key=lambda t: t[0] * 10 ** t[1])
    return OD("Put these numbers in order, smallest first.", [f"{fmt(m)} × 10{sup(e)}" for m, e in vals], o="O3", d="H", skill="Data", reason="Compare the powers of 10 first; if the powers are equal, compare the A parts.")
def t_table(r):
    rows = []
    for _ in range(3):
        m, e, v = big(r); rows.append([fmt(v), B(m), B(e)])
    return TB("Complete the table: write each number as A × 10ⁿ.", ["Number", "A", "n"], rows, o="O3", reason="A is between 1 and 10; n counts the places the point moves.")
def t_context(r):
    ctx = pick(r, [("The mass of a grain of sand is about", "g", -r.randint(3, 6)), ("The thickness of a sheet of paper is about", "mm", -1), ("The diameter of a red blood cell is about", "m", -6), ("The distance from Earth to the Sun is about", "km", 8), ("The population of a large country is about", "people", 8)])
    m = r.randint(11, 99) / 10; v = m * 10 ** ctx[2]
    return N(f"{ctx[0]} {stdform(v)} {ctx[1]}. Write this as an ordinary number.", round(v, 12), o="O3", d="M", reason=f"{stdform(v)} = {fmt(round(v, 12))}.")
def t_compare(r):
    m1, e1 = r.randint(11, 99) / 10, r.randint(3, 8); m2, e2 = r.randint(11, 99) / 10, e1 - r.randint(1, 2); k = (m1 * 10 ** e1) / (m2 * 10 ** e2)
    return N(f"How many times bigger is {fmt(m1)} × 10{sup(e1)} than {fmt(m2)} × 10{sup(e2)}? Give your answer to 1 decimal place.", round(k, 1), o="O3", d="VH", tol=0.05, reason=f"Divide: {fmt(m1)} ÷ {fmt(m2)} × 10{sup(e1-e2)} ≈ {k:.2f}.")
def t_add(r):
    a, b = r.randint(2, 9), r.randint(2, 9); e = r.randint(3, 6); v = a * 10 ** e + b * 10 ** (e - 1)
    return N(f"Work out {a} × 10{sup(e)} + {b} × 10{sup(e-1)}. Give your answer in standard form.", v, o="O3", d="H", reason=f"Write both as ordinary numbers: {fmt(a*10**e)} + {fmt(b*10**(e-1))} = {fmt(v)} = {stdform(v)}. You cannot just add the powers when adding.")

s.core(t_to_sf(s.rng), t_from_sf(s.rng), t_small_to(s.rng), t_mul(s.rng), t_table(s.rng), t_order_sf(s.rng),
       EX("Explain why 0.75 × 10⁶ is not in standard form, and write it correctly.", [("A must be at least 1 / between 1 and 10", ["1 and 10|at least 1|less than 1|between 1|bigger than (or equal to )?1"]), ("7.5 × 10⁵", ["7\\.5 ?(×|x|\\*) ?10\\^?5|7\\.5 × 10⁵"])],
          "In standard form A must be between 1 and 10, and 0.75 is less than 1. 0.75 × 10⁶ = 7.5 × 10⁵.", o="O3", d="H"),
       t_div(s.rng))
s.gen("p", 44, t_to_sf, t_small, t_from_sf, t_small_to, t_mul, t_div, t_order_sf, t_table, t_context, t_add)
s.gen("a", 8, t_compare,
      lambda r: (lambda n: N(f"Light travels about 3 × 10⁵ km in one second. How far does it travel in {n} hours? Give your answer in standard form.", 3e5 * 3600 * n, "km", units=["km", "m"], o="O3", d="VH", reason=f"{n} h = {3600*n} s; 3 × 10⁵ × {3600*n} = {stdform(3e5*3600*n)} km."))(r.randint(2, 9)),
      lambda r: (lambda m, e: N(f"Find the square of {fmt(m)} × 10{sup(e)}. Give your answer in standard form, correct to 3 significant figures.", sf((m * 10 ** e) ** 2, 3), o="O3", d="VH", tol=abs(sf((m*10**e)**2, 3)) * 0.002, reason=f"({fmt(m)})² = {m*m:.4f}, (10{sup(e)})² = 10{sup(2*e)} → {stdform(sf((m*10**e)**2,3))}."))(r.randint(11, 99) / 10, r.randint(-5, 6)))

# ================================================================== 1.3 Indices
s = U.section("1.3", "Indices", ["O4"])
s.idea("The laws of indices", ["For any number a (not 0): **aᵐ × aⁿ = aᵐ⁺ⁿ**, **aᵐ ÷ aⁿ = aᵐ⁻ⁿ** and **(aᵐ)ⁿ = aᵐⁿ**.",
       "These laws only work when the **base is the same**: 2³ × 2⁴ = 2⁷, but 2³ × 3⁴ cannot be combined this way."])
s.idea("Zero and negative indices", ["Dividing a power by itself gives 1, so **a⁰ = 1**.", "A negative index means 'one over': **a⁻ⁿ = 1/aⁿ**. So 5⁻² = 1/25 and 10⁻³ = 1/1000 = 0.001."])
s.example("Simplify", "Simplify 7⁵ × 7⁻² ÷ 7⁶, leaving your answer as a power of 7.", [("7⁵ × 7⁻² = 7³", "add the indices: 5 + (−2) = 3"), ("7³ ÷ 7⁶ = 7⁻³", "subtract: 3 − 6 = −3")], "7⁻³ (which equals 1/343)")
s.check(X("Simplify x⁴ × x³. Type your answer like x^7.", "x^7", o="O4", d="M", reason="Add the indices: 4 + 3 = 7."))
s.example("Powers of powers with numbers", "Simplify (3a²)³.", [("3³ × (a²)³", "cube every part of the bracket"), ("27a⁶", "3³ = 27 and 2 × 3 = 6")], "27a⁶")
s.check(N("Work out 4⁻². Give your answer as a fraction or a decimal.", 0.0625, o="O4", d="M", reason="4⁻² = 1/4² = 1/16 = 0.0625."))
s.mistake("Do not multiply the bases", ["2³ × 2⁴ is 2⁷, NOT 4⁷. The base stays the same; only the indices change."])
s.check(MC("Simplify 5³ × 5⁶.", "5⁹", [("25⁹", "Do not multiply the bases."), ("5¹⁸", "Add the indices when multiplying, do not multiply them."), ("25¹⁸", "The base stays 5.")], o="O4"))

def t_mulp(r):
    b = pick(r, ["x", "y", "a", "n", "2", "3", "7"]); m, n = r.randint(-4, 9), r.randint(-4, 9)
    if b.isdigit(): return MC(f"Simplify {b}{sup(m)} × {b}{sup(n)}, leaving your answer as a power of {b}.", f"{b}{sup(m+n)}", [(f"{b}{sup(m*n)}", "Add the indices, do not multiply them."), (f"{int(b)**2}{sup(m+n)}", "The base stays the same."), (f"{b}{sup(m-n)}", "Multiplying means ADD the indices.")], o="O4")
    return X(f"Simplify {b}{sup(m)} × {b}{sup(n)}. Type powers with ^ (e.g. {b}^5).", f"{b}^({m+n})", vars=b, o="O4", reason=f"{m} + {n} = {m+n}.", mustNot=["\\*"], show=f"{b}{sup(m+n)}")
def t_divp(r):
    b = pick(r, ["x", "y", "p", "k"]); m, n = r.randint(2, 12), r.randint(-3, 11)
    return X(f"Simplify {b}{sup(m)} ÷ {b}{sup(n)}.", f"{b}^({m-n})", vars=b, o="O4", reason=f"Subtract the indices: {m} − ({n}) = {m-n}.", show=f"{b}{sup(m-n)}", mustNot=["/"])
def t_powp(r):
    c = r.randint(2, 5); m, n = r.randint(2, 5), r.randint(2, 4); b = pick(r, ["x", "a", "y"])
    return X(f"Simplify ({c}{b}{sup(m)}){sup(n)}.", f"{c**n}{b}^{m*n}", vars=b, o="O4", d="H", reason=f"{c}{sup(n)} = {c**n}; ({b}{sup(m)}){sup(n)} = {b}{sup(m*n)}.", show=f"{c**n}{b}{sup(m*n)}", mustNot=["\\("])
def t_neg(r):
    a = r.randint(2, 10); n = r.randint(1, 3)
    return N(f"Work out {a}{sup(-n)} as a fraction. Type it like 1/8.", 1 / a ** n, o="O4", d="M", tol=1e-9, reason=f"{a}{sup(-n)} = 1/{a}{sup(n)} = 1/{a**n}.")
def t_zero(r):
    a = pick(r, ["17", "0.5", "(−3)", "1 000 000", "x"])
    return N(f"What is {a}⁰ ?", 1, o="O4", d="M", reason="Any non-zero number to the power 0 is 1.")
def t_find_n(r):
    b = pick(r, [2, 3, 5, 10]); m = r.randint(2, 8); n = r.randint(-3, 9); v = m + n
    return N(f"{b}{sup(m)} × {b}ⁿ = {b}{sup(v)}. Find n.", n, o="O4", d="H", reason=f"{m} + n = {v}, so n = {n}.")
def t_mixed(r):
    b = pick(r, ["a", "x", "m"]); p, q, t = r.randint(2, 8), r.randint(2, 8), r.randint(1, 9)
    return X(f"Simplify {b}{sup(p)} × {b}{sup(q)} ÷ {b}{sup(t)}.", f"{b}^({p+q-t})", vars=b, o="O4", d="H", reason=f"{p} + {q} − {t} = {p+q-t}.", show=f"{b}{sup(p+q-t)}", mustNot=["/"])
def t_coef(r):
    a, c = r.randint(2, 9), r.randint(2, 9); m, n = r.randint(1, 6), r.randint(1, 6)
    return X(f"Simplify {a}x{sup(m)} × {c}x{sup(n)}.", f"{a*c}x^{m+n}", o="O4", d="M", reason=f"Multiply the numbers ({a} × {c} = {a*c}) and add the indices ({m} + {n} = {m+n}).", show=f"{a*c}x{sup(m+n)}", mustNot=["\\*", "\\("])
def t_value(r):
    b = pick(r, [2, 3, 10]); m, n = r.randint(2, 6), r.randint(1, 4)
    return N(f"Work out ({b}{sup(m)} × {b}{sup(n)}) ÷ {b}{sup(m+n-2)} without a calculator.", b ** 2, o="O4", d="H", reason=f"{b}{sup(m+n)} ÷ {b}{sup(m+n-2)} = {b}² = {b*b}.")
def t_tf(r):
    rows = [("2³ × 2² = 2⁵", "True"), ("3⁴ × 3² = 9⁶", "False"), ("10⁰ = 0", "False"), ("5⁻¹ = 0.2", "True"), ("(x²)³ = x⁵", "False"), ("x⁶ ÷ x² = x⁴", "True"), ("2⁻³ = −8", "False"), ("a¹ = a", "True")]
    return GD("Is each statement true or false?", "True or false?", r.sample(rows, 4), o="O4", d="M")

s.core(t_mulp(s.rng), t_divp(s.rng), t_neg(s.rng), t_tf(s.rng),
       TB("Complete the table of powers of 2.", ["Power", "2³", "2²", "2¹", "2⁰", "2⁻¹", "2⁻²"], [["Value", "8", "4", "2", B(1), B(0.5), B(0.25)]], o="O4", reason="Each step to the right halves the value: 2⁰ = 1, 2⁻¹ = 1/2, 2⁻² = 1/4."),
       t_powp(s.rng), t_find_n(s.rng),
       EX("Use the law aᵐ ÷ aⁿ = aᵐ⁻ⁿ to explain why a⁰ = 1.", [("aⁿ ÷ aⁿ = aⁿ⁻ⁿ = a⁰", ["a\\^?n ?÷ ?a\\^?n|a⁰|a\\^?0|n ?- ?n|same power"]), ("any number divided by itself is 1", ["divided by itself|itself|= ?1\\b|equals 1|is 1"])],
          "aⁿ ÷ aⁿ = aⁿ⁻ⁿ = a⁰. But any non-zero number divided by itself is 1, so a⁰ = 1.", o="O4", d="H"))
s.gen("p", 44, t_mulp, t_divp, t_powp, t_neg, t_zero, t_find_n, t_mixed, t_coef, t_value, t_tf)
s.gen("a", 8,
      lambda r: (lambda k: N(f"2ˣ = {2**k} × 2⁻⁵. Find x.", k - 5, o="O4", d="VH", reason=f"{2**k} = 2{sup(k)}, so 2ˣ = 2{sup(k-5)} and x = {k-5}."))(r.randint(3, 10)),
      lambda r: (lambda a, b: N(f"Find the value of n if {a}ⁿ = 1/{a**b}.", -b, o="O4", d="VH", reason=f"1/{a**b} = 1/{a}{sup(b)} = {a}{sup(-b)}."))(pick(r, [2, 3, 4, 5]), r.randint(2, 4)),
      lambda r: (lambda m, n: X(f"Simplify (x{sup(m)} × x{sup(n)})² ÷ x{sup(m)}.", f"x^({2*(m+n)-m})", o="O4", d="VH", show=f"x{sup(2*(m+n)-m)}", reason=f"(x{sup(m+n)})² = x{sup(2*(m+n))}; ÷ x{sup(m)} gives x{sup(2*(m+n)-m)}."))(r.randint(2, 5), r.randint(1, 5)),
      lambda r: (lambda a: N(f"Which power of 4 is equal to 8{sup(a*2)}? Find n in 4ⁿ = 8{sup(a*2)}.", 3 * a, o="O4", d="VH", reason=f"8{sup(2*a)} = 2{sup(6*a)} and 4ⁿ = 2{sup('2n')}, so 2n = {6*a}, n = {3*a}."))(r.randint(1, 3)))

U.mindmap(("Rational or irrational", "Fractions, terminating and recurring decimals are rational • √ of non-squares and π are irrational", "O1", "1.1"),
          ("Estimating roots", "Find the square or cube numbers either side", "O2", "1.1"),
          ("Standard form", "A × 10ⁿ with 1 ≤ A < 10 • large: n positive • small: n negative", "O3", "1.2"),
          ("Laws of indices", "aᵐ × aⁿ = aᵐ⁺ⁿ • aᵐ ÷ aⁿ = aᵐ⁻ⁿ • (aᵐ)ⁿ = aᵐⁿ", "O4", "1.3"),
          ("Zero and negative indices", "a⁰ = 1 • a⁻ⁿ = 1/aⁿ", "O4", "1.3"))
