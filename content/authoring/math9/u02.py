# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 2 Expressions and formulae. Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(2, "Expressions and Formulae", "Algebra",
         "Substituting into expressions, writing expressions, indices in algebra, expanding double brackets, algebraic fractions and rearranging formulae.",
         {"O1": {"sec": "2.1", "code": "9Ae.03", "codeNote": "", "t": "Substitute positive and negative numbers, fractions and decimals into expressions and formulae, including powers."},
          "O2": {"sec": "2.2", "code": "9Ae.02", "codeNote": "", "t": "Write expressions from a situation and simplify them."},
          "O3": {"sec": "2.3", "code": "9Ae.01", "codeNote": "", "t": "Use the laws of indices to simplify algebraic expressions."},
          "O4": {"sec": "2.4", "code": "9Ae.04", "codeNote": "", "t": "Expand the product of two linear expressions, such as (x + 3)(x − 5)."},
          "O5": {"sec": "2.5", "code": "9Ae.05", "codeNote": "", "t": "Simplify algebraic fractions by adding, subtracting, multiplying and dividing."},
          "O6": {"sec": "2.6", "code": "9Ae.06", "codeNote": "", "t": "Derive formulae, use them and change the subject of a formula."}})

V = ["x", "y", "a", "b", "n", "p", "t"]

# ================================================================== 2.1 Substituting
s = U.section("2.1", "Substituting into expressions", ["O1"])
s.idea("Substitution", ["To **substitute** means to replace each letter with its value. Put negative numbers in **brackets** so the signs stay correct.",
       "Use the order of operations: brackets, then **powers**, then × and ÷, then + and −. So in 3x² the power is done first: if x = −2, 3x² = 3 × (−2)² = 3 × 4 = 12."])
s.example("Negative values", "Find the value of 2a² − 5b when a = −3 and b = −4.", [("2 × (−3)² − 5 × (−4)", "brackets round negative values"), ("2 × 9 − (−20)", "power first: (−3)² = 9"), ("18 + 20 = 38", "subtracting a negative is adding")], "38")
s.check(N("Work out 4x² when x = −3.", 36, o="O1", reason="x² = 9, 4 × 9 = 36."))
s.example("Fractions", "Find the value of (p + q)/(2p) when p = 1/2 and q = 3/4.", [("p + q = 1/2 + 3/4 = 5/4", ""), ("2p = 1", ""), ("5/4 ÷ 1 = 5/4", "")], "5/4 = 1.25")
s.check(MC("Before you read on: when x = −3, what is x²?", "9", [("−9", "(−3) × (−3) = 9."), ("−6", "Squaring is not doubling.")], o="O1"))
s.mistake("−x² is not (−x)²", ["When x = 3, −x² = −(3²) = −9, but (−x)² = (−3)² = 9. The power only applies to what is directly before it."])
s.check(MC("What is the value of −a² when a = 5?", "−25", [("25", "Square first, then apply the minus sign."), ("−10", "a² means a × a, not 2a."), ("10", "")], o="O1", d="H"))

def t_sub1(r):
    a, b = nz(r, -6, 6), nz(r, -6, 6); c1, c2 = r.randint(2, 6), r.randint(2, 9)
    v = c1 * a * a - c2 * b
    return N(f"Find the value of {c1}a² − {c2}b when a = {fmt(a)} and b = {fmt(b)}.", v, o="O1", d="M", reason=f"{c1} × ({fmt(a)})² − {c2} × ({fmt(b)}) = {c1*a*a} − ({c2*b}) = {fmt(v)}.")
def t_sub2(r):
    x, y = nz(r, -5, 5), nz(r, -5, 5); v = x ** 3 - 2 * x * y + y * y
    return N(f"Find the value of x³ − 2xy + y² when x = {fmt(x)} and y = {fmt(y)}.", v, o="O1", d="H", reason=f"{x**3} − {2*x*y} + {y*y} = {fmt(v)}.")
def t_sub3(r):
    p = Fr(r.randint(1, 5), pick(r, [2, 3, 4, 5])); q = Fr(r.randint(1, 5), pick(r, [2, 3, 4, 6])); v = (p + q) / (2 * p)
    return N(f"Find the value of (p + q) ÷ 2p when p = {frac(p)} and q = {frac(q)}. Give your answer as a fraction or decimal.", float(v), o="O1", d="H", tol=1e-6, reason=f"p + q = {frac(p+q)}, 2p = {frac(2*p)}, so the value is {frac(v)}.")
def t_sub4(r):
    m, u, t = r.randint(2, 20), r.randint(-5, 15), r.randint(2, 9); a = r.randint(-4, 6)
    return N(f"The formula v = u + at gives speed. Find v when u = {u}, a = {a} and t = {t}.", u + a * t, "m/s", units=["m/s", "m", "s"], o="O1", d="M", reason=f"v = {u} + {a} × {t} = {u + a*t} m/s.")
def t_sub5(r):
    x = r.randint(2, 9) / 10 * pick(r, [1, -1])
    return N(f"Find the value of 5x² − 3x + 1 when x = {fmt(x)}.", round(5 * x * x - 3 * x + 1, 6), o="O1", d="H", tol=1e-6, reason=f"5 × {fmt(round(x*x,4))} − 3 × {fmt(x)} + 1 = {fmt(round(5*x*x-3*x+1,4))}.")
def t_table(r):
    xs = r.sample([-3, -2, -1, 0, 1, 2, 3], 4); xs.sort(); c = r.randint(-5, 5)
    return TB(f"Complete the table of values for y = x² + {c}x." if c >= 0 else f"Complete the table of values for y = x² − {-c}x.", ["x"] + [fmt(x) for x in xs], [["y"] + [B(x * x + c * x) for x in xs]], o="O1", d="M", reason="Substitute each x value: " + ", ".join(f"x = {fmt(x)} → {x*x+c*x}" for x in xs) + ".")
def t_sqrt(r):
    a, b = r.choice([(3, 4), (6, 8), (5, 12), (8, 15), (9, 12), (7, 24)])
    return N(f"c = √(a² + b²). Find c when a = {a} and b = {b}.", (a * a + b * b) ** 0.5, o="O1", d="H", reason=f"a² + b² = {a*a} + {b*b} = {a*a+b*b}; √{a*a+b*b} = {int((a*a+b*b)**0.5)}.")
def t_compare(r):
    x = nz(r, -4, -1)
    return MC(f"When x = {x}, which expression has the greatest value?", f"x²", [(f"x³", f"x³ = {x**3}."), (f"2x", f"2x = {2*x}."), (f"x − 1", f"x − 1 = {x-1}.")], o="O1", d="H", reason=f"x² = {x*x}, which is positive; the others are negative.")
def t_find(r):
    k = r.randint(2, 9); x = nz(r, -6, 6); v = k * x + 3
    return N(f"When x = ?, the expression {k}x + 3 has the value {v}. Find x.", x, o="O1", d="M", reason=f"{k}x + 3 = {v} → {k}x = {v-3} → x = {x}.")

s.core(t_sub1(s.rng), t_sub2(s.rng), t_table(s.rng), t_sub4(s.rng), t_sub3(s.rng), t_compare(s.rng),
       EX("Ana says that when x = −4, 3x² = −48. Explain her mistake and give the correct value.", [("square first / power before multiplying", ["square|power|first|before"]), ("(−4)² = 16 is positive", ["16|positive"]), ("3 × 16 = 48", ["\\b48\\b"])],
          "She multiplied before squaring or forgot that (−4)² is positive. (−4)² = 16, so 3x² = 3 × 16 = 48.", o="O1", d="H"),
       TB("Complete the table for P = 2l + 2w.", ["l", "w", "P"], [["4.5", "3", B(15)], ["7", "2.5", B(19)], ["1/2", "3/4", B(2.5)]], reason="P = 2 × 4.5 + 2 × 3 = 15; 2 × 7 + 2 × 2.5 = 19; 2 × 1/2 + 2 × 3/4 = 2.5.", o="O1"))
def b1_1(r):
    x = -r.randint(2, 5)
    return MC(f"When x = {x}, which expression has the smallest value?", "x³", [("x²", f"x² = {x * x}."), ("2x", f"2x = {2 * x}."), ("−x", f"−x = {-x}.")], o="O1", d="H", reason=f"x³ = {x ** 3}, x² = {x * x}, 2x = {2 * x}, −x = {-x}.")


s.gen("p", 44, t_sub1, t_sub2, t_sub3, t_sub4, t_sub5, t_table, t_sqrt, t_compare, t_find)
s.capped("p", [1] * 1, [b1_1]).capped("m", [2] * 1, [b1_1])   # v2 reasoning kinds
s.gen("a", 8,
      lambda r: (lambda x: N(f"Find the value of (2x − 1)²(x + 3) when x = {fmt(x)}.", (2 * x - 1) ** 2 * (x + 3), o="O1", d="VH", reason=f"(2 × {fmt(x)} − 1)² = {(2*x-1)**2}; × ({fmt(x)} + 3) = {fmt((2*x-1)**2*(x+3))}."))(nz(r, -5, 5)),
      lambda r: (lambda a, b: N(f"Find the value of (a² − b²) ÷ (a − b) when a = {a} and b = {b}.", a + b, o="O1", d="VH", reason=f"a² − b² = {a*a-b*b}, a − b = {a-b}; {a*a-b*b} ÷ {a-b} = {a+b}. (In general it equals a + b.)"))(r.randint(5, 15), nz(r, -6, 4)),
      lambda r: (lambda T: N(f"F = 9C/5 + 32 converts Celsius to Fahrenheit. Find C when F = {T}.", round((T - 32) * 5 / 9, 1), "°C", units=["°C", "°F"], tol=0.05, o="O1", d="VH", reason=f"{T} − 32 = {T-32}; × 5 ÷ 9 = {(T-32)*5/9:.1f} °C."))(r.randint(-10, 120)))

# ================================================================== 2.2 Constructing
s = U.section("2.2", "Constructing expressions", ["O2"])
s.idea("Writing expressions", ["Choose a letter for the unknown, then build the expression step by step. 'Three more than twice n' is **2n + 3**. 'Twice the sum of n and 3' is **2(n + 3)** – the brackets matter.",
       "Simplify by **collecting like terms**: 4x + 3y − x + 5y = 3x + 8y."])
s.example("Perimeter", "A rectangle has length 3x + 2 and width x − 1. Write and simplify an expression for its perimeter.", [("2(3x + 2) + 2(x − 1)", "two lengths and two widths"), ("6x + 4 + 2x − 2", "expand"), ("8x + 2", "collect like terms")], "8x + 2")
s.check(X("Write an expression for 'five less than three times n'. Use n.", "3n-5", vars="n", o="O2"))
s.example("Ages", "Mia is m years old. Her brother is 4 years younger, and her mother is three times Mia's age. Write an expression for their total age.", [("m + (m − 4) + 3m", ""), ("5m − 4", "collect like terms")], "5m − 4")
s.mistake("Order matters for subtraction", ["'7 less than x' is x − 7, not 7 − x."])
s.check(MC("Which expression means 'the square of the sum of a and b'?", "(a + b)²", [("a² + b²", "That is the sum of the squares."), ("a + b²", "Only b is squared here."), ("2(a + b)", "That is double, not squared.")], o="O2", d="H"))

def t_words(r):
    k, c = r.randint(2, 9), r.randint(1, 12); v = pick(r, V)
    w = r.choice([(f"{c} more than {k} times {v}", f"{k}{v}+{c}"), (f"{c} less than {k} times {v}", f"{k}{v}-{c}"), (f"{k} times the sum of {v} and {c}", f"{k}({v}+{c})"), (f"{v} divided by {k}, then add {c}", f"{v}/{k}+{c}"), (f"the square of {v}, minus {c}", f"{v}^2-{c}"), (f"{c} subtracted from the square of {v}", f"{v}^2-{c}")])
    return X(f"Write an expression for: {w[0]}.", w[1], vars=v, o="O2", reason=f"{w[0]} → {w[1]}")
def t_simp(r):
    a, b, c, d = [nz(r, -9, 9) for _ in range(4)]
    return X(f"Simplify {poly((a,'x'),(b,'y'),(c,'x'),(d,'y'))}.", f"{a+c}x+({b+d})y", vars="xy", o="O2", reason=f"x terms: {a} + {c} = {a+c}; y terms: {b} + {d} = {b+d}.", mustNot=["\\("], show=poly((a+c,'x'),(b+d,'y')))
def t_perim(r):
    a, b, c, d = r.randint(2, 6), r.randint(1, 9), r.randint(1, 4), r.randint(-6, 6)
    w = poly((c, 'x'), (d, ''))
    return X(f"A rectangle has length {a}x + {b} and width {w}. Write a simplified expression for its perimeter.", f"{2*(a+c)}x+{2*(b+d)}", o="O2", d="M", reason=f"2({a}x + {b}) + 2({w}) = {poly((2*(a+c),'x'),(2*(b+d),''))}.", mustNot=["\\("], fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]], "s": [f"{a}x + {b}", w, "", ""]})
def t_cost(r):
    p1, p2 = r.randint(2, 9), r.randint(10, 30)
    return X(f"Pens cost ${p1} each and folders cost ${p2} each. Write an expression for the cost in dollars of p pens and f folders.", f"{p1}p+{p2}f", vars="pf", o="O2", reason=f"{p1} × p + {p2} × f.")
def t_angles(r):
    a, b, c = r.randint(1, 4), r.randint(5, 30), r.randint(1, 3)
    return X(f"Two angles of a triangle are {a}x + {b}° and {c}x°. Write an expression, in degrees, for the third angle.", f"{180-b}-{a+c}x", o="O2", d="H", reason=f"180 − ({a}x + {b}) − {c}x = {180-b} − {a+c}x.", fig={"kind": "shape", "pts": [[0, 0], [6, 0], [2, 4]], "ang": [f"{a}x + {b}°", f"{c}x°", "?"]})
def t_age(r):
    k, d = r.randint(2, 4), r.randint(2, 12)
    return X(f"Kai is k years old. His sister is {d} years older than him and his father is {k} times as old as his sister. Write a simplified expression for his father's age.", f"{k}(k+{d})", vars="k", o="O2", d="H", reason=f"Sister: k + {d}. Father: {k}(k + {d}) = {k}k + {k*d}.")
def t_match(r):
    pairs = [("n + 2 more than double n", "3n + 2"), ("double n, then add 2", "2n + 2"), ("double the sum of n and 2", "2n + 4"), ("n squared, then double", "2n²")]
    return MT("Match each description with the simplified expression.", [(a, b) for a, b in pairs], o="O2", d="M")
def t_area(r):
    a, b = r.randint(2, 7), r.randint(1, 6)
    return X(f"A square has side {a}x. A smaller square of side {b}x is cut from it. Write a simplified expression for the area that is left.", f"{a*a-b*b}x^2", o="O2", d="H", reason=f"({a}x)² − ({b}x)² = {a*a}x² − {b*b}x² = {a*a-b*b}x².", show=f"{a*a-b*b}x²")

s.core(t_words(s.rng), t_simp(s.rng), t_perim(s.rng), t_cost(s.rng), t_angles(s.rng),
       GD("Is each statement true for every value of n?", "Always true?", [("n + n = 2n", "Yes"), ("n × n = 2n", "No"), ("3(n + 1) = 3n + 3", "Yes"), ("(n + 2)² = n² + 4", "No")], o="O2", d="H"),
       EX("Write an expression for the perimeter of a square of side 2x + 3. Explain why the perimeter is always odd-free (always even) when x is a whole number.", [("4(2x + 3) = 8x + 12", ["8x ?\\+ ?12|4\\(2x ?\\+ ?3\\)"]), ("8x and 12 are both even / multiple of 4", ["even|multiple of (2|4)|divisible"])],
          "Perimeter = 4(2x + 3) = 8x + 12. 8x and 12 are both multiples of 4, so the perimeter is always even (a multiple of 4).", o="O2", d="H"),
       t_area(s.rng))
s.gen("p", 44, t_words, t_simp, t_perim, t_cost, t_angles, t_age, t_area, t_match)
s.gen("a", 8,
      lambda r: (lambda n: X(f"The sum of {n} consecutive whole numbers starting at m. Write a simplified expression for the sum.", f"{n}m+{n*(n-1)//2}", vars="m", o="O2", d="VH", reason="m + (m+1) + … + (m+" + str(n - 1) + f") = {n}m + {n*(n-1)//2}."))(r.randint(3, 7)),
      lambda r: (lambda a: X(f"A cuboid measures x by {a}x by (x + {a}). Write an expression for its volume, expanded and simplified.", f"{a}x^3+{a*a}x^2", o="O2", d="VH", show=f"{a}x³ + {a*a}x²", reason=f"x × {a}x × (x + {a}) = {a}x²(x + {a}) = {a}x³ + {a*a}x²."))(r.randint(2, 6)))

# ================================================================== 2.3 Expressions and indices
s = U.section("2.3", "Expressions and indices", ["O3"])
s.idea("Indices with letters", ["The laws of indices work for letters too: x³ × x⁵ = x⁸, y⁷ ÷ y² = y⁵, (a²)⁴ = a⁸.",
       "With numbers in front: **multiply or divide the numbers**, and **add or subtract the indices** of each letter separately: 3a²b × 4ab³ = 12a³b⁴."])
s.example("Mixed letters", "Simplify 18x⁵y² ÷ 6x²y.", [("18 ÷ 6 = 3", "numbers"), ("x⁵ ÷ x² = x³", "subtract indices"), ("y² ÷ y = y", "y = y¹")], "3x³y")
s.check(X("Simplify 2p³ × 5p⁴.", "10p^7", vars="p", o="O3", mustNot=["\\*"], show="10p⁷"))
s.example("Brackets", "Simplify (2m³n)⁴.", [("2⁴ = 16", ""), ("(m³)⁴ = m¹²", "multiply indices"), ("n⁴", "")], "16m¹²n⁴")
s.mistake("Adding unlike powers", ["x² + x³ cannot be simplified: they are not like terms. Only multiplication and division combine powers."])
s.check(MC("Simplify x² + x² .", "2x²", [("x⁴", "x² + x² is two lots of x², not x² × x²."), ("2x⁴", ""), ("x²", "")], o="O3", d="H"))

def t_m(r):
    a, b = r.randint(2, 9), r.randint(2, 9); m, n, k = r.randint(1, 6), r.randint(1, 6), r.randint(1, 4)
    return X(f"Simplify {a}x{sup(m)}y × {b}x{sup(n)}y{sup(k)}.", f"{a*b}x^{m+n}y^{k+1}", vars="xy", o="O3", show=f"{a*b}x{sup(m+n)}y{sup(k+1)}", mustNot=["\\*"], reason=f"{a} × {b} = {a*b}; x: {m}+{n}; y: 1+{k}.")
def t_d(r):
    b = r.randint(2, 6); c = r.randint(2, 6); a = b * c; m, n = r.randint(4, 9), r.randint(1, 3); p, q = r.randint(3, 6), r.randint(1, 2)
    return X(f"Simplify {a}a{sup(m)}b{sup(p)} ÷ {b}a{sup(n)}b{sup(q)}.", f"{c}a^{m-n}b^{p-q}", vars="ab", o="O3", d="M", show=f"{c}a{sup(m-n)}b{sup(p-q)}", mustNot=["/"], reason=f"{a} ÷ {b} = {c}; a: {m}−{n}; b: {p}−{q}.")
def t_p(r):
    c, m, n, k = r.randint(2, 4), r.randint(2, 5), r.randint(1, 3), r.randint(2, 4)
    return X(f"Simplify ({c}m{sup(m)}n{sup(n)}){sup(k)}.", f"{c**k}m^{m*k}n^{n*k}", vars="mn", o="O3", d="H", show=f"{c**k}m{sup(m*k)}n{sup(n*k)}", mustNot=["\\("], reason=f"{c}{sup(k)} = {c**k}; m: {m}×{k}; n: {n}×{k}.")
def t_neg(r):
    a, m, n = r.randint(2, 9), r.randint(1, 4), r.randint(5, 9)
    return X(f"Simplify {a}x{sup(m)} ÷ x{sup(n)}. You may leave a negative index.", f"{a}x^({m-n})", o="O3", d="H", show=f"{a}x{sup(m-n)}", reason=f"{m} − {n} = {m-n}, so {a}x{sup(m-n)} = {a}/x{sup(n-m)}.")
def t_missing(r):
    a, m, n = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
    return N(f"{a}x{sup(m)} × □ = {a*3}x{sup(m+n)}. The box is 3xᵏ. Find k.", n, o="O3", d="M", reason=f"{m} + k = {m+n} → k = {n}.")
def t_area(r):
    a, b = r.randint(2, 6), r.randint(2, 6)
    return X(f"A rectangle measures {a}x² by {b}x³. Write its area in its simplest form.", f"{a*b}x^5", reason=f"Multiply the numbers and add the powers: {a} × {b} = {a * b}, x² × x³ = x⁵.", o="O3", show=f"{a*b}x⁵", mustNot=["\\*"], fig={"kind": "shape", "pts": [[0, 0], [8, 0], [8, 4], [0, 4]], "s": [f"{a}x²", f"{b}x³", "", ""]})
def t_like(r):
    rows = [("3x² + 4x²", "7x²"), ("3x² × 4x²", "12x⁴"), ("12x⁴ ÷ 4x²", "3x²"), ("(3x²)²", "9x⁴")]
    return MT("Match each expression with its simplified form.", r.sample(rows, 4), o="O3", d="H")
def t_frac(r):
    a, b = r.randint(2, 6), r.randint(2, 6); m, n = r.randint(3, 8), r.randint(1, 2)
    return X(f"Simplify ({a}x{sup(m)} × {b}x{sup(n)}) ÷ {a*b}x{sup(m+n-1)}.", "x", o="O3", d="H", reason=f"Numerator {a*b}x{sup(m+n)}; ÷ {a*b}x{sup(m+n-1)} = x.")

s.core(t_m(s.rng), t_d(s.rng), t_p(s.rng), t_area(s.rng), t_like(s.rng),
       TK("Tick the expressions that are equal to 6x⁶.", ["Equal", "Not equal"], [("2x² × 3x³", ["✗", "✓"]), ("3x³ × 2x³", ["✓", "✗"]), ("12x⁸ ÷ 2x²", ["✓", "✗"]), ("(√6x³)²", ["✓", "✗"])], o="O3", d="H"),
       EX("Explain why (2x³)² is not equal to 2x⁶.", [("the 2 is squared as well", ["2 (is )?squared|both|everything|4x"]), ("(2x³)² = 4x⁶", ["4x\\^?6|4x⁶"])], "Everything in the bracket is squared, including the 2: (2x³)² = 2² × x⁶ = 4x⁶.", o="O3", d="H"),
       t_neg(s.rng))
s.gen("p", 44, t_m, t_d, t_p, t_neg, t_missing, t_area, t_like, t_frac)
s.gen("a", 8,
      lambda r: (lambda a, b: X(f"Simplify √({a*a}x{sup(2*b)}).", f"{a}x^{b}", o="O3", d="VH", show=f"{a}x{sup(b)}", reason=f"({a}x{sup(b)})² = {a*a}x{sup(2*b)}."))(r.randint(2, 9), r.randint(2, 6)),
      lambda r: (lambda a: X(f"A cube has volume {a**3}y⁶. Write its side length.", f"{a}y^2", vars="y", o="O3", d="VH", show=f"{a}y²", reason=f"({a}y²)³ = {a**3}y⁶."))(r.randint(2, 6)))

# ================================================================== 2.4 Expanding the product
s = U.section("2.4", "Expanding the product of two expressions", ["O4"])
s.idea("Double brackets", ["To expand (x + a)(x + b), multiply **every term in the first bracket by every term in the second** – four multiplications.",
       "A grid helps: write x and +a along the top, x and +b down the side, fill in the four products, then collect like terms."],
       table={"caption": "(x + 3)(x + 5)", "head": ["×", "x", "+3"], "rows": [["x", "x²", "3x"], ["+5", "5x", "15"]]})
s.example("With negatives", "Expand and simplify (x − 4)(x + 7).", [("x × x = x²", ""), ("x × 7 = 7x,  −4 × x = −4x", ""), ("−4 × 7 = −28", ""), ("x² + 3x − 28", "7x − 4x = 3x")], "x² + 3x − 28")
s.check(X("Expand and simplify (x + 2)(x + 6).", "x^2+8x+12", o="O4", mustNot=["\\("], show="x² + 8x + 12"))
s.example("Squaring a bracket", "Expand (2x − 3)².", [("(2x − 3)(2x − 3)", "write it twice"), ("4x² − 6x − 6x + 9", ""), ("4x² − 12x + 9", "")], "4x² − 12x + 9")
s.idea("Why (a + b)² is not a² + b²", ["A square of side (a + b) splits into four parts: a², b² and two rectangles ab. So (a + b)² = a² + 2ab + b².",
       "Check with numbers: (3 + 4)² = 49, but 3² + 4² = 25. The missing 24 is 2 × 3 × 4."], table={"head": ["×", "a", "+b"], "rows": [["a", "a²", "ab"], ["+b", "ab", "b²"]]})
s.check(MC("Before you read on: expand (x − 5)².", "x² − 10x + 25", [("x² − 25", "There are two −5x parts."), ("x² + 25", "Expand (x − 5)(x − 5).")], o="O4"))
s.mistake("(x + 5)² is not x² + 25", ["You must include the two middle terms: (x + 5)² = x² + 10x + 25."])
s.check(MC("Expand (x + 5)².", "x² + 10x + 25", [("x² + 25", "Do not forget the middle terms 5x + 5x."), ("x² + 5x + 25", "There are two 5x terms."), ("2x + 10", "")], o="O4", d="H"))

def pr(a, b, c, d):  # (ax + b)(cx + d)
    return a * c, a * d + b * c, b * d
def t_e1(r):
    a, b = nz(r, -9, 9), nz(r, -9, 9); A, Bc, C = pr(1, a, 1, b)
    return X(f"Expand and simplify (x {('+ ' + str(a)) if a > 0 else ('− ' + str(-a))})(x {('+ ' + str(b)) if b > 0 else ('− ' + str(-b))}).", f"x^2+({Bc})x+({C})", o="O4", mustNot=["\\("], show=poly((1, 'x²'), (Bc, 'x'), (C, '')), reason=f"x² + ({a} + {b})x + ({a} × {b}) = {poly((1,'x²'),(Bc,'x'),(C,''))}.")
def br(a, b): return f"({poly((a, 'x'), (b, ''))})"
def t_e2(r):
    a, b, c, d = r.randint(2, 5), nz(r, -7, 7), r.randint(1, 4), nz(r, -7, 7); A, Bc, C = pr(a, b, c, d)
    return X(f"Expand and simplify {br(a,b)}{br(c,d)}.", f"{A}x^2+({Bc})x+({C})", o="O4", d="H", mustNot=["\\("], show=poly((A, 'x²'), (Bc, 'x'), (C, '')), reason=f"{a*c}x² + {a*d}x + {b*c}x + {b*d} = {poly((A,'x²'),(Bc,'x'),(C,''))}.")
def t_sq(r):
    a, b = r.randint(1, 4), nz(r, -9, 9)
    return X(f"Expand and simplify {br(a,b)}².", f"{a*a}x^2+({2*a*b})x+({b*b})", reason=f"({br(a, b)})({br(a, b)}): square the first term, double the product, square the last.", o="O4", d="H", mustNot=["\\("], show=poly((a * a, 'x²'), (2 * a * b, 'x'), (b * b, '')))
def t_dop(r):
    a = r.randint(1, 12)
    return X(f"Expand and simplify (x + {a})(x − {a}).", f"x^2-{a*a}", o="O4", mustNot=["\\("], show=f"x² − {a*a}", reason=f"The middle terms cancel: {a}x − {a}x = 0.")
def t_grid(r):
    a, b = nz(r, -8, 8), nz(r, -8, 8)
    return TB(f"Complete the grid to expand (x {('+ ' + str(a)) if a > 0 else ('− ' + str(-a))})(x {('+ ' + str(b)) if b > 0 else ('− ' + str(-b))}). Write the number part of each term.", ["×", "x", fmt(a)], [["x", "x²", B(a)], [fmt(b), B(b), B(a * b)]], o="O4", d="M", hint="Each cell is (top) × (side). Write only the number in front of x, or the constant.", reason=f"x × {a} = {a}x, {b} × x = {b}x, {a} × {b} = {a*b}.")
def t_coef(r):
    a, b = nz(r, -9, 9), nz(r, -9, 9)
    return N(f"When (x + {a})(x + {b}) is expanded, what is the coefficient of x?".replace("+ -", "− "), a + b, o="O4", d="M", reason=f"{a} + {b} = {a+b}.")
def t_area(r):
    a, b = r.randint(1, 9), r.randint(1, 9)
    return X(f"A rectangle has sides x + {a} and x + {b}. Write its area, expanded and simplified.", f"x^2+{a+b}x+{a*b}", reason=f"(x + {a})(x + {b}) = x² + {b}x + {a}x + {a * b}.", o="O4", mustNot=["\\("], show=f"x² + {a+b}x + {a*b}", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 5], [0, 5]], "s": [f"x + {a}", f"x + {b}", "", ""]})
def t_find(r):
    a, b = r.randint(1, 9), r.randint(1, 9)
    return N(f"(x + {a})(x + k) = x² + {a+b}x + {a*b}. Find k.", b, o="O4", d="H", reason=f"{a} + k = {a+b}, so k = {b} (check {a} × {b} = {a*b}).")
def t_err(r):
    return MC("Lin expands (x − 3)(x − 4) and gets x² − 7x − 12. Which part is wrong?", "the constant: −3 × −4 = +12", [("the x² term", ""), ("the x term", "−3x − 4x = −7x is correct."), ("nothing is wrong", "")], o="O4", d="H")

s.core(t_e1(s.rng), t_e2(s.rng), t_sq(s.rng), t_dop(s.rng), t_grid(s.rng), t_area(s.rng), t_err(s.rng),
       EX("Explain why (x + 4)(x − 4) has no x term when expanded.", [("4x and −4x", ["4x"]), ("they cancel / add to zero", ["cancel|zero|0x|add to 0"]), ("x² − 16", ["x\\^?2 ?- ?16|x² ?− ?16"])],
          "Expanding gives x² − 4x + 4x − 16. The terms −4x and +4x cancel, so the result is x² − 16 with no x term.", o="O4", d="H"))
def b4_1(r):
    a, b = r.randint(1, 7), r.randint(1, 7)
    return MC(f"Which is the expansion of (x + {a})(x − {b})?", f"x² {'+' if a - b > 0 else '−'} {abs(a - b)}x − {a * b}" if a != b else f"x² − {a * b}", [(f"x² + {a + b}x − {a * b}", "The x parts are +" + str(a) + "x and −" + str(b) + "x."), (f"x² − {a * b}x + {a + b}", "Multiply the numbers for the last term; add them for the x term.")], o="O4", d="H",
              reason=f"x² − {b}x + {a}x − {a * b}.")


s.gen("p", 44, t_e1, t_e2, t_sq, t_dop, t_grid, t_coef, t_area, t_find, t_err)
s.capped("p", [1] * 1, [b4_1]).capped("m", [2] * 1, [b4_1])   # v2 reasoning kinds
s.gen("a", 8,
      lambda r: (lambda a, b: X(f"Expand and simplify (x + {a})(x + {b}) − (x + {a+b})².", f"-{a+b}x-{(a+b)**2-a*b}", o="O4", d="VH", show=f"−{a+b}x − {(a+b)**2 - a*b}", reason=f"x² + {a+b}x + {a*b} − (x² + {2*(a+b)}x + {(a+b)**2}) = −{a+b}x − {(a+b)**2-a*b}."))(r.randint(1, 5), r.randint(1, 5)),
      lambda r: (lambda a: N(f"Use (100 + {a})(100 − {a}) = 100² − {a}² to work out {100+a} × {100-a} without a calculator.", 10000 - a * a, reason=f"100² − {a}² = 10 000 − {a * a} = {10000 - a * a}.", o="O4", d="VH"))(r.randint(2, 9)),
      lambda r: (lambda a, b: X(f"Expand and simplify (x + {a})(x² + {b}).", f"x^3+{a}x^2+{b}x+{a*b}", reason=f"x × x² + x × {b} + {a} × x² + {a} × {b}.", o="O4", d="VH", show=f"x³ + {a}x² + {b}x + {a*b}"))(r.randint(1, 6), r.randint(1, 6)))

# ================================================================== 2.5 Algebraic fractions
s = U.section("2.5", "Simplifying algebraic fractions", ["O5"])
s.idea("Algebraic fractions", ["Algebraic fractions follow the same rules as number fractions.",
       "**Add or subtract**: use a common denominator. x/3 + x/4 = 4x/12 + 3x/12 = 7x/12.",
       "**Multiply**: multiply tops and bottoms, then cancel. **Divide**: multiply by the reciprocal."])
s.example("Adding", "Write (2x)/5 − (x − 1)/3 as a single fraction.", [("3(2x)/15 − 5(x − 1)/15", "common denominator 15"), ("(6x − 5x + 5)/15", "careful: −5 × −1 = +5"), ("(x + 5)/15", "")], "(x + 5)/15")
s.check(X("Write x/2 + x/3 as a single fraction.", "5x/6", o="O5", show="5x/6"))
s.example("Dividing", "Simplify (3a/4) ÷ (9a²/8).", [("3a/4 × 8/(9a²)", "multiply by the reciprocal"), ("24a/(36a²)", ""), ("2/(3a)", "cancel 12a")], "2/(3a)")
s.idea("Why you can only cancel factors", ["(x + 2)/2 is NOT x + 1: the 2 divides the whole top, so (x + 2)/2 = x/2 + 1. You may cancel only a factor of the whole numerator and the whole denominator.",
       "Factorise first: (3x + 6)/3 = 3(x + 2)/3 = x + 2."])
s.check(MC("Before you read on: simplify (4x + 8)/4.", "x + 2", [("x + 8", "Both terms are divided by 4."), ("4x + 2", "Divide the 4x by 4 as well.")], o="O5"))
s.mistake("Cancel factors, not terms", ["(x + 6)/6 is NOT x + 1. You can only cancel a common FACTOR of the whole top and bottom."])
s.check(MC("Which simplification is correct?", "6x/9 = 2x/3", [("(x + 3)/3 = x", "3 is not a factor of the whole numerator."), ("(x + 4)/(x + 2) = 2", ""), ("x/(x + 1) = 1/1", "")], o="O5", d="H"))

def t_add(r):
    a, b = pick(r, [2, 3, 4, 5, 6]), pick(r, [3, 4, 5, 7, 8])
    if a == b: return None
    return X(f"Write x/{a} + x/{b} as a single fraction.", f"x/{a}+x/{b}", o="O5", show=f"{a+b}x/{a*b}", must=["^[^/]*/[^/]*$"], mustNot=["\\+"], reason=f"Common denominator {a*b}: {b}x/{a*b} + {a}x/{a*b} = {a+b}x/{a*b} (simplify if possible).", formFb="Write it as ONE fraction.")
def t_sub(r):
    a, b, c = pick(r, [2, 3, 4]), pick(r, [3, 5, 7]), r.randint(1, 5)
    if a == b: return None
    return X(f"Write (2x)/{a} − (x − {c})/{b} as a single fraction.", f"2x/{a}-(x-{c})/{b}", o="O5", d="H", must=["^[^/]*/[^/]*$"], show=f"({2*b-a}x + {a*c})/{a*b}", reason=f"Common denominator {a*b}: ({2*b}x − {a}(x − {c}))/{a*b} = ({2*b-a}x + {a*c})/{a*b}.", formFb="Write it as ONE fraction.")
def t_mul(r):
    a, b, c, d = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
    return X(f"Simplify ({a}x/{b}) × ({c}/{d}x²).", f"({a}x/{b})*({c}/({d}x^2))", o="O5", d="H", must=["^[^/]*/[^/]*$"], mustNot=["\\*"], show=f"{Fr(a*c, b*d).numerator}/({Fr(a*c, b*d).denominator}x)", reason=f"{a*c}x/{b*d}x² = {frac(Fr(a*c, b*d))} ÷ x.")
def t_div(r):
    a, b, c, d = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
    return X(f"Simplify (a/{b}) ÷ ({c}a/{d}).", f"(a/{b})/({c}a/{d})", vars="a", o="O5", d="H", mustNot=["a"], show=frac(Fr(d, b * c)), reason=f"a/{b} × {d}/({c}a) = {d}/{b*c}.")
def t_cancel(r):
    k, a = r.randint(2, 9), r.randint(1, 9)
    return X(f"Simplify ({k}x + {k*a})/{k}.", f"x+{a}", o="O5", mustNot=["/"], show=f"x + {a}", reason=f"Factorise the top: {k}(x + {a}); cancel {k}.")
def t_val(r):
    a, b = pick(r, [2, 3, 4]), pick(r, [5, 6, 8]); x = r.randint(1, 12)
    return N(f"Find the value of x/{a} + x/{b} when x = {x}.", x / a + x / b, o="O5", tol=1e-6, reason=f"{x}/{a} + {x}/{b} = {frac(Fr(x,a)+Fr(x,b))}.")
def t_tf(r):
    rows = [("x/4 + x/4 = x/2", "True"), ("x/3 × 3 = x", "True"), ("(x + 2)/2 = x + 1", "False"), ("1/x + 1/x = 2/x", "True"), ("1/x + 1/y = 2/(x + y)", "False"), ("2x/x = 2", "True")]
    return GD("Is each statement true or false (x and y not 0)?", "True or false?", r.sample(rows, 4), o="O5", d="H")

s.core(t_add(s.rng) or t_add(s.rng), t_sub(s.rng) or t_sub(s.rng), t_mul(s.rng), t_div(s.rng), t_tf(s.rng),
       TB("Complete the table for x = 6.", ["Expression", "x/2 + x/3", "x/2 − x/3", "x/2 × x/3", "x/2 ÷ x/3"], [["Value", B(5), B(1), B(6), B(1.5)]], reason="x/2 = 3 and x/3 = 2: 3 + 2 = 5, 3 − 2 = 1, 3 × 2 = 6, 3 ÷ 2 = 1.5.", o="O5"),
       EX("Explain why (x + 9)/3 is not equal to x + 3.", [("only 9 is divided / x is not divided by 3", ["x is not|only|both|whole|every term"]), ("it equals x/3 + 3", ["x/3"])], "Every term of the numerator must be divided by 3: (x + 9)/3 = x/3 + 3, not x + 3.", o="O5", d="H"),
       t_cancel(s.rng))
def b5_1(r):
    a = r.randint(2, 6)
    return MC(f"Jo simplifies (x + {a})/{a} to x + 1. What is right?", f"x/{a} + 1", [("x + 1", f"Only the {a} was divided by {a}."), (f"x/{a} + {a}", f"{a} ÷ {a} = 1.")], o="O5", d="H", reason=f"(x + {a})/{a} = x/{a} + {a}/{a} = x/{a} + 1.")


s.gen("p", 44, t_add, t_sub, t_mul, t_div, t_cancel, t_val, t_tf)
s.capped("p", [1] * 1, [b5_1]).capped("m", [2] * 1, [b5_1])   # v2 reasoning kinds
s.gen("a", 8,
      lambda r: (lambda a: X(f"Write 1/x + 1/(x + {a}) as a single fraction.", f"1/x+1/(x+{a})", o="O5", d="VH", must=["^[^/]*/[^/]*$"], show=f"(2x + {a})/(x(x + {a}))", formFb="Write it as ONE fraction.", reason=f"Common denominator x(x + {a}): (x + {a} + x)/(x(x + {a}))."))(r.randint(1, 6)),
      lambda r: (lambda a: X(f"Simplify (x² − {a*a})/(x + {a}).", f"x-{a}", o="O5", d="VH", mustNot=["/"], show=f"x − {a}", reason=f"x² − {a*a} = (x + {a})(x − {a}); cancel (x + {a})."))(r.randint(2, 9)))

# ================================================================== 2.6 Formulae
s = U.section("2.6", "Deriving and using formulae", ["O6"])
s.idea("Changing the subject", ["The **subject** of a formula is the letter on its own on one side, e.g. A in A = lw.",
       "To make another letter the subject, **undo the operations** in reverse order, doing the same to both sides."])
s.example("Two steps", "Make u the subject of v = u + at.", [("v − at = u", "subtract at from both sides"), ("u = v − at", "")], "u = v − at")
s.check(X("Make w the subject of A = lw.", "A/l", vars="Al", lhs="w", o="O6", show="A/l"))
s.example("With a square", "Make r the subject of A = πr².", [("A/π = r²", "divide by π"), ("r = √(A/π)", "square root")], "r = √(A/π)")
s.example("Deriving a formula", "A taxi charges $3 plus $2 for every km. Write a formula for the cost C dollars of a journey of d km, then find C for 7.5 km.", [("C = 3 + 2d", ""), ("C = 3 + 2 × 7.5 = 18", "")], "C = 2d + 3; $18")
s.check(N("Use C = 2d + 3 to find the distance d when the cost is $26.", 11.5, "km", units=["km", "$"], o="O6", d="M", reason="26 = 2d + 3 → 2d = 23 → d = 11.5 km."))
s.check(MC("Before you read on: make r the subject of A = πr².", "r = √(A/π)", [("r = A/π", "That gives r², not r."), ("r = √A/π", "Divide by π before taking the square root.")], o="O6"))
s.mistake("Undo in the right order", ["To make x the subject of y = 3x + 5, subtract 5 first, then divide by 3: x = (y − 5)/3, not y/3 − 5."])

def t_s1(r):
    a, b = r.randint(2, 9), r.randint(1, 12)
    return X(f"Make x the subject of y = {a}x + {b}.", f"(y-{b})/{a}", vars="xy", lhs="x", o="O6", show=f"(y − {b})/{a}", reason=f"y − {b} = {a}x → x = (y − {b})/{a}.")
def t_s2(r):
    a = r.randint(2, 9)
    return X(f"Make t the subject of s = {a}t − u.", f"(s+u)/{a}", vars="stu", lhs="t", reason=f"Add u: s + u = {a}t; divide by {a}.", o="O6", d="H", show=f"(s + u)/{a}")
def t_s3(r):
    k = r.randint(2, 6)
    return X(f"Make b the subject of P = {k}(a + b).", f"P/{k}-a", vars="Pab", lhs="b", reason=f"Divide by {k}: P/{k} = a + b; subtract a.", o="O6", d="H", show=f"P/{k} − a")
def t_s4(r):
    return X("Make h the subject of V = (1/3)Ah.", "3V/A", vars="VAh", lhs="h", o="O6", d="H", show="3V/A")
def t_use(r):
    l, w, h = r.randint(2, 15), r.randint(2, 12), r.randint(2, 10)
    return N(f"The volume of a cuboid is V = lwh. Find h when V = {l*w*h} cm³, l = {l} cm and w = {w} cm.", h, "cm", units=["cm", "cm²", "cm³"], o="O6", reason=f"h = V ÷ (lw) = {l*w*h} ÷ {l*w} = {h} cm.")
def t_derive(r):
    f, p = r.randint(5, 30), r.randint(2, 9)
    return X(f"A gym charges a joining fee of ${f} and ${p} per visit. Write a formula for the total cost C dollars for n visits.", f"{p}n+{f}", vars="nC", lhs="C", reason=f"{p} for each of n visits plus the {f} fee: C = {p}n + {f}.", o="O6", show=f"{p}n + {f}")
def t_rev(r):
    f, p, n = r.randint(5, 30), r.randint(2, 9), r.randint(3, 20)
    return N(f"A gym charges ${f} to join and ${p} per visit. Lin paid ${f + p*n} in total. How many visits did she make?", n, "visits", units=["visits", "$"], o="O6", reason=f"({f+p*n} − {f}) ÷ {p} = {n}.")
def t_sq(r):
    A = pick(r, [50, 78.5, 120, 200, 314]); rr = (A / 3.14159265) ** 0.5
    return N(f"A circle has area {fmt(A)} cm². Use r = √(A/π) to find the radius, correct to 1 decimal place.", round(rr, 1), "cm", units=["cm", "cm²"], reason=f"√({fmt(A)} ÷ π) ≈ {round(rr, 1)} cm.", o="O6", d="H", tol=0.05)
def t_order(r):
    return OD("Put the steps in order to make x the subject of y = (3x − 2)/5.", ["Multiply both sides by 5: 5y = 3x − 2", "Add 2: 5y + 2 = 3x", "Divide by 3: x = (5y + 2)/3"], o="O6", d="M", skill="Data")

s.core(t_s1(s.rng), t_s2(s.rng), t_use(s.rng), t_derive(s.rng), t_rev(s.rng), t_order(s.rng),
       TB("Use F = 1.8C + 32 to complete the table.", ["C (°C)", "0", "25", B(-10), B(100)], [["F (°F)", B(32), B(77), "14", "212"]], reason="F = 1.8 × 0 + 32 = 32; 1.8 × 25 + 32 = 77; C = (14 − 32) ÷ 1.8 = −10; (212 − 32) ÷ 1.8 = 100.", o="O6", d="H", hint="To find C from F, work backwards: subtract 32, then divide by 1.8."),
       EX("Kim makes x the subject of y = 4x − 7 and writes x = y/4 + 7. Explain her mistake and give the correct formula.", [("undo in reverse order / add 7 first", ["add 7 first|first add|reverse|order|before dividing"]), ("x = (y + 7)/4", ["\\(y ?\\+ ?7\\) ?/ ?4|y/4 ?\\+ ?7/4|y ?\\+ ?7 all over 4"])],
          "She did the steps in the wrong order. Add 7 first: y + 7 = 4x, then divide by 4: x = (y + 7)/4.", o="O6", d="H"))
def b6_1(r):
    return MC("Make t the subject of v = u + at.", "t = (v − u)/a", [("t = v − u − a", "a multiplies t, so divide by a."), ("t = (v − u)a", "Undo × a by dividing.")], o="O6", d="H", reason="Subtract u: v − u = at. Divide by a: t = (v − u)/a.")


s.gen("p", 44, t_s1, t_s2, t_s3, t_s4, t_use, t_derive, t_rev, t_sq, t_order)
s.capped("p", [1] * 1, [b6_1]).capped("m", [2] * 1, [b6_1])   # v2 reasoning kinds
s.gen("a", 8,
      lambda r: X("Make x the subject of y = √(x + a).", "y^2-a", vars="xya", lhs="x", o="O6", d="VH", show="y² − a", reason="Square both sides: y² = x + a, so x = y² − a."),
      lambda r: X("Make a the subject of v² = u² + 2as.", "(v^2-u^2)/(2s)", vars="vuas", lhs="a", o="O6", d="VH", show="(v² − u²)/(2s)"),
      lambda r: (lambda k: X(f"Make x the subject of {k}x + y = ax + b.", f"(b-y)/({k}-a)", vars="xyab", lhs="x", o="O6", d="VH", show=f"(b − y)/({k} − a)", reason=f"{k}x − ax = b − y → x({k} − a) = b − y."))(r.randint(2, 7)))

U.mindmap(("Substitution", "Brackets round negatives • powers before × and ÷", "O1", "2.1"),
          ("Writing expressions", "Words → algebra • collect like terms", "O2", "2.2"),
          ("Indices in algebra", "Multiply numbers, add indices • (2x³)² = 4x⁶", "O3", "2.3"),
          ("Double brackets", "Every term × every term • (x + a)² = x² + 2ax + a²", "O4", "2.4"),
          ("Algebraic fractions", "Common denominators • cancel factors, not terms", "O5", "2.5"),
          ("Formulae", "Derive, substitute, change the subject by undoing in reverse", "O6", "2.6"))
