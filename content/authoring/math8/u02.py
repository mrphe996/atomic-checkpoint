# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 2 Expressions, formulae and equations. Written by the Atomic teaching team."""
from math import gcd
from kit import *

U = Unit(2, "Expressions, Formulae and Equations", "Algebra",
         "Writing and simplifying expressions, substituting into formulae, expanding brackets and factorising, and solving equations and inequalities.",
         {"O1": {"code": "8Ae.01", "sec": "2.1", "codeNote": "", "t": "Write expressions from words and situations, using letters for unknowns."},
          "O2": {"code": "8Ae.02", "sec": "2.2", "codeNote": "", "t": "Substitute positive and negative numbers into expressions and formulae, and change the subject of a simple formula."},
          "O3": {"code": "8Ae.03", "sec": "2.3", "codeNote": "", "t": "Expand a single bracket and simplify, including negative terms."},
          "O4": {"code": "8Ae.04", "sec": "2.4", "codeNote": "", "t": "Factorise an expression by taking out the highest common factor."},
          "O5": {"code": "8Ae.05", "sec": "2.5", "codeNote": "", "t": "Construct and solve linear equations, including with brackets and unknowns on both sides."},
          "O6": {"code": "8Ae.06", "sec": "2.6", "codeNote": "", "t": "Write, solve and show inequalities on a number line."}})
sg = lambda v: f"({v})" if v < 0 else str(v)

# ================================================================== 2.1
s = U.section("2.1", "Constructing expressions", ["O1"])
s.idea("Expressions", ["An **expression** is made of terms and has **no equals sign**: 3n + 5, 4(a − 2), x².",
       "Write multiplication without ×: 3 × n = **3n**, n × n = **n²**. Write division as a fraction: n ÷ 4 = **n/4**."])
s.example("From words", "Write an expression for 'six less than double a number n'.", [("double n → 2n", ""), ("six less than → − 6", "")], "2n − 6")
s.check(X("Write an expression for 'four more than the square of k'. Use k.", "k^2+4", vars="k", o="O1"))
s.idea("Like terms", ["**Like terms** have exactly the same letters and powers: 3x and −5x are like terms; 3x and 3x² are not. Collect like terms by adding their numbers."])
s.check(X("Simplify 5a + 3b − 2a + b.", "3a+4b", vars="ab", o="O1", mustNot=["\\("]))
s.mistake("Order matters", ["'5 less than n' is n − 5, not 5 − n."])
WORDS = [("three more than x", "x+3", "x"), ("five less than y", "y-5", "y"), ("double n, then add 7", "2n+7", "n"), ("n multiplied by itself", "n^2", "n"), ("a divided by 4", "a/4", "a"),
         ("the sum of p and q, then multiplied by 3", "3(p+q)", "pq"), ("eight less than three times m", "3m-8", "m"), ("half of t", "t/2", "t"), ("the product of a and b", "ab", "ab"), ("ten take away twice k", "10-2k", "k")]


def c1(r):
    w = pick(r, WORDS)
    return X(f"Write an expression for: {w[0]}.", w[1], vars=w[2], o="O1", reason=f"{w[0]} → {w[1]}.")
def c2(r):
    a, b, c, d = nz(r, -6, 9), nz(r, -6, 9), nz(r, -6, 9), nz(r, -6, 9)
    if a + c == 0: c += 1
    if b + d == 0: d += 1
    return X(f"Simplify {poly((a, 'x'), (b, 'y'), (c, 'x'), (d, 'y'))}.", f"{a + c}x+({b + d})y", vars="xy", o="O1", mustNot=["\\("], show=poly((a + c, 'x'), (b + d, 'y')), reason=f"x: {a} + {c} = {a + c}; y: {b} + {d} = {b + d}.")
def c3(r):
    p, q = r.randint(2, 9), r.randint(2, 9)
    return X(f"Apples cost {p} cents each and pears cost {q} cents each. Write an expression for the cost, in cents, of a apples and b pears.", f"{p}a+{q}b", vars="ab", o="O1", reason=f"{p} × a + {q} × b.")
def c4(r):
    k = r.randint(2, 9)
    return X(f"Sara is n years old. Her mother is {k} times as old as Sara, plus 4 years. Write an expression for her mother's age.", f"{k}n+4", vars="n", o="O1", reason=f"{k} × n + 4 = {k}n + 4.")
def c5(r):
    a, b = r.randint(2, 9), r.randint(1, 9)
    return X(f"A rectangle has length {a}x and width x + {b}. Write a simplified expression for its perimeter.", f"{2 * a + 2}x+{2 * b}", o="O1", d="H", mustNot=["\\("], reason=f"2 × {a}x + 2(x + {b}) = {2 * a + 2}x + {2 * b}.", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": [f"{a}x", f"x + {b}", "", ""]})
def c6(r):
    rows = [("3x and 5x", "Like"), ("2y and 2y²", "Not like"), ("ab and 4ba", "Like"), ("7p and 7q", "Not like"), ("−x² and 3x²", "Like"), ("5 and 5n", "Not like")]
    return GD("Are these like terms?", "Like terms?", r.sample(rows, 4), o="O1")
def c7(r):
    a, b = r.randint(2, 6), r.randint(2, 6)
    return X(f"Simplify {a}x² + {b}x + {a + 1}x² − {b}x.", f"{2 * a + 1}x^2", o="O1", d="H", mustNot=["\\("], reason=f"x² terms: {a} + {a + 1} = {2 * a + 1}; x terms: {b} − {b} = 0.")
def c8(r):
    n = r.randint(3, 9)
    return X(f"A pack holds p pencils. Ali buys {n} packs and gives away 5 pencils. Write an expression for the number of pencils he has left.", f"{n}p-5", vars="p", o="O1", reason=f"{n}p − 5.")


def c9(r):
    a, b = r.randint(2, 7), r.randint(1, 9)
    return X("Write a simplified expression for the perimeter of this triangle.", f"{3 * a}x+{2 * b}", o="O1", mustNot=["\\("], fig={"kind": "shape", "pts": [[0, 0], [8, 0], [4, 6]], "s": [f"{a}x", f"{a}x + {b}", f"{a}x + {b}"]}, reason=f"{a}x + 2({a}x + {b}) = {3 * a}x + {2 * b}.")


s.std([c6, c9, c1, c2, c3, c4, c8, c5, c7], EX("Explain why 3x + 2y cannot be simplified.", [("3x and 2y are not like terms", ["not like|different letters|different variables|unlike"]), ("you can only add like terms", ["only.*like|same letter|cannot add|can't add"])], "3x and 2y have different letters, so they are not like terms. Only like terms can be added together.", o="O1"))

# ================================================================== 2.2
s = U.section("2.2", "Using expressions and formulae", ["O2"])
s.idea("Substitution", ["To **substitute**, replace each letter with its value, using brackets for negative numbers, then follow the order of operations.",
       "If a = −3: 2a² = 2 × (−3)² = 2 × 9 = 18. Square first, then multiply."])
s.example("A formula", "Use v = u + at to find v when u = 4, a = −2 and t = 5.", [("v = 4 + (−2) × 5", "substitute"), ("= 4 − 10 = −6", "multiply first")], "v = −6")
s.check(N("Find the value of 3x − 2y when x = 5 and y = −4.", 23, o="O2", reason="3 × 5 − 2 × (−4) = 15 + 8 = 23."))
s.idea("Changing the subject", ["The **subject** is the letter on its own. To make another letter the subject, undo the operations, doing the same to both sides.",
       "From P = 4s: s = P/4. From y = x + 7: x = y − 7."])
s.check(X("Make x the subject of y = 3x − 5.", "(y+5)/3", vars="xy", lhs="x", o="O2", d="H"))
s.mistake("Negative squares", ["When x = −5, x² = 25, but −x² = −25. Always put negative numbers in brackets before squaring."])


def u1(r):
    a, b, x, y = r.randint(2, 6), r.randint(2, 6), nz(r, -6, 8), nz(r, -6, 8)
    return N(f"Find the value of {a}x + {b}y when x = {x} and y = {y}.", a * x + b * y, o="O2", reason=f"{a} × {sg(x)} + {b} × {sg(y)} = {a * x + b * y}.")
def u2(r):
    a, x = r.randint(2, 5), r.randint(-6, -2)
    return N(f"Find the value of {a}x² when x = {x}.", a * x * x, o="O2", reason=f"{a} × ({x})² = {a} × {x * x} = {a * x * x}.")
def u3(r):
    u, a, t = r.randint(0, 20), r.randint(-4, 6), r.randint(2, 9)
    return N(f"Use the formula v = u + at to find v when u = {u}, a = {a} and t = {t}.", u + a * t, o="O2", reason=f"{u} + {sg(a)} × {t} = {u + a * t}.")
def u4(r):
    l, w = r.randint(3, 20), r.randint(2, 15)
    return N(f"The perimeter of a rectangle is P = 2l + 2w. Find P when l = {l} cm and w = {w} cm.", 2 * l + 2 * w, "cm", units=["cm"], o="O2", reason=f"2 × {l} + 2 × {w} = {2 * l + 2 * w}.", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": ["l", "w", "", ""]})
def u5(r):
    h, rate = r.randint(2, 9), r.randint(8, 20)
    c = r.randint(10, 40)
    return N(f"A plumber charges C = {c} + {rate}h dollars, where h is the number of hours. How much does a {h}-hour job cost?", c + rate * h, "$", units=["$"], o="O2", reason=f"{c} + {rate} × {h} = {c + rate * h}.")
def u6(r):
    a, b = r.randint(2, 9), r.randint(1, 20)
    return X(f"Make x the subject of y = {a}x + {b}.", f"(y-{b})/{a}", vars="xy", lhs="x", o="O2", d="H", reason=f"Subtract {b}, then divide by {a}.")
def u7(r):
    k = r.randint(2, 9)
    return X(f"Make r the subject of C = {k}r.", f"C/{k}", vars="Cr", lhs="r", o="O2", reason=f"Divide both sides by {k}.")
def u8(r):
    x, y = nz(r, -5, 5), nz(r, -5, 5)
    return N(f"Find the value of x² − 2xy when x = {x} and y = {y}.", x * x - 2 * x * y, o="O2", d="H", reason=f"({x})² − 2 × {sg(x)} × {sg(y)} = {x * x} − ({2 * x * y}) = {x * x - 2 * x * y}.")
def u9(r):
    c = r.randint(-10, 35)
    return N(f"Use F = 1.8C + 32 to convert {c} °C to degrees Fahrenheit.", round(1.8 * c + 32, 1), "°F", units=["°F"], o="O2", d="H", reason=f"1.8 × {sg(c)} + 32 = {fmt(round(1.8 * c + 32, 1))}.")


def u10(r):
    a, b = r.randint(2, 5), r.randint(-6, 6); xs = r.sample(range(-3, 5), 3)
    return TB(f"Complete the table of values for y = {a}x {'+' if b >= 0 else '−'} {abs(b)}.", ["x", "y"], [[str(x), B(a * x + b)] for x in sorted(xs)], o="O2", reason="Substitute each x value.")


s.std([u4, u10, u1, u2, u3, u5, u7, u8, u6, u9], EX("Explain why 2x² and (2x)² have different values when x = 3.", [("2x² = 2 × 9 = 18", ["18"]), ("(2x)² = 6² = 36: the 2 is squared too", ["36|6²|6 ?× ?6"])], "In 2x² only x is squared: 2 × 3² = 18. In (2x)² the whole bracket is squared: 6² = 36.", o="O2"))

# ================================================================== 2.3
s = U.section("2.3", "Expanding brackets", ["O3"])
s.idea("Expanding", ["To **expand** a bracket, multiply **every** term inside by the term outside: 4(2x − 3) = 8x − 12.",
       "A negative outside changes every sign: −3(x − 5) = −3x + 15."])
s.example("Expand and simplify", "Expand and simplify 3(2x + 4) − 2(x − 5).", [("6x + 12 − 2x + 10", "−2 × −5 = +10"), ("4x + 22", "collect like terms")], "4x + 22")
s.check(X("Expand 5(3y − 2).", "15y-10", vars="y", o="O3", mustNot=["\\("]))
s.idea("Letters outside", ["x(x + 4) = x² + 4x. Multiply x by x to get x²."])
s.mistake("Every term", ["3(x + 4) is NOT 3x + 4. The 3 multiplies the 4 as well: 3x + 12."])
s.check(X("Expand x(x − 7).", "x^2-7x", o="O3", mustNot=["\\("]))


def e1(r):
    a, b, c = r.randint(2, 9), r.randint(1, 9), nz(r, -9, 9)
    return X(f"Expand {a}({b}x {'+' if c > 0 else '−'} {abs(c)}).", f"{a * b}x+({a * c})", o="O3", mustNot=["\\("], show=poly((a * b, 'x'), (a * c, '')), reason=f"{a} × {b}x = {a * b}x; {a} × {c} = {a * c}.")
def e2(r):
    a, b = r.randint(2, 9), r.randint(1, 9)
    return X(f"Expand −{a}(x − {b}).", f"-{a}x+{a * b}", o="O3", mustNot=["\\("], reason=f"−{a} × x = −{a}x; −{a} × −{b} = +{a * b}.")
def e3(r):
    a, b, c, d = r.randint(2, 6), r.randint(1, 9), r.randint(2, 6), r.randint(1, 9)
    return X(f"Expand and simplify {a}(x + {b}) + {c}(x + {d}).", f"{a + c}x+{a * b + c * d}", o="O3", mustNot=["\\("], reason=f"{a}x + {a * b} + {c}x + {c * d} = {a + c}x + {a * b + c * d}.")
def e4(r):
    a, b, c, d = r.randint(2, 6), r.randint(1, 9), r.randint(2, 5), r.randint(1, 9)
    return X(f"Expand and simplify {a}(2x + {b}) − {c}(x − {d}).", f"{2 * a - c}x+{a * b + c * d}", o="O3", d="H", mustNot=["\\("], show=poly((2 * a - c, 'x'), (a * b + c * d, '')), reason=f"{2 * a}x + {a * b} − {c}x + {c * d}.")
def e5(r):
    b = nz(r, -9, 9)
    return X(f"Expand x(x {'+' if b > 0 else '−'} {abs(b)}).", f"x^2+({b})x", o="O3", mustNot=["\\("], show=poly((1, 'x²'), (b, 'x')))
def e6(r):
    a, b = r.randint(2, 6), r.randint(2, 9)
    return X(f"Expand {a}y({b} − y).", f"{a * b}y-{a}y^2", vars="y", o="O3", d="H", mustNot=["\\("], reason=f"{a}y × {b} = {a * b}y; {a}y × y = {a}y².")
def e7(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return MC(f"Which is the correct expansion of {a}(x + {b})?", f"{a}x + {a * b}", [(f"{a}x + {b}", "The number outside multiplies BOTH terms."), (f"x + {a * b}", "Multiply x by the number outside too."), (f"{a + 1}x + {a * b}", "")], o="O3")
def e8(r):
    w, a, b = r.randint(2, 9), r.randint(1, 5), r.randint(1, 9)
    return X(f"A rectangle has width {w} cm and length ({a}x + {b}) cm. Write an expanded expression for its area.", f"{w * a}x+{w * b}", o="O3", mustNot=["\\("], reason=f"{w}({a}x + {b}) = {w * a}x + {w * b}.", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": [f"{a}x + {b}", f"{w}", "", ""]})


def e9(r):
    rows = [("3(x + 2) = 3x + 6", "True"), ("2(y − 4) = 2y − 4", "False"), ("−(a − 5) = −a + 5", "True"), ("x(x + 3) = x² + 3", "False"), ("−4(p + 1) = −4p − 4", "True"), ("5(2 − t) = 10 − t", "False")]
    return GD("Is each expansion true or false?", "True or false", r.sample(rows, 4), o="O3")


s.std([e8, e9, e1, e2, e3, e5, e7, e4, e6], EX("Explain the mistake in −2(x − 3) = −2x − 6.", [("−2 × −3 should be +6", ["\\+ ?6|positive 6|plus 6|−2 ?× ?−3|-2 ?\\* ?-3"]), ("negative × negative = positive", ["negative.*positive|two negatives|minus times minus"])], "−2 × −3 = +6, because a negative multiplied by a negative is positive. The answer should be −2x + 6.", o="O3"))

# ================================================================== 2.4
s = U.section("2.4", "Factorising", ["O4"])
s.idea("Factorising", ["**Factorising** is the reverse of expanding. Find the **highest common factor** of the terms and write it outside a bracket.",
       "12x + 18 = 6(2x + 3), because 6 is the HCF of 12 and 18. Check by expanding."])
s.example("Letters too", "Factorise fully 8x² − 12x.", [("HCF of 8 and 12 is 4; both terms contain x", ""), ("8x² − 12x = 4x(2x − 3)", "check: 4x × 2x = 8x², 4x × 3 = 12x")], "4x(2x − 3)")
s.check(X("Factorise fully 10a + 15.", "5(2a+3)", vars="a", must=["\\("], o="O4"))
s.mistake("Factorise fully", ["4x + 8 = 2(2x + 4) is not fully factorised: 2x + 4 still has a common factor 2. The full answer is 4(x + 2)."])


def g1(r):
    k, a, b = r.randint(2, 9), r.randint(1, 7), r.randint(1, 9)
    while gcd(a, b) != 1: b += 1
    return X(f"Factorise fully {k * a}x + {k * b}.", f"{k}({a}x+{b})", must=["\\("], o="O4", reason=f"HCF = {k}: {k}({a}x + {b}).")
def g2(r):
    k, a, b = r.randint(2, 9), r.randint(2, 7), r.randint(1, 9)
    while gcd(a, b) != 1: b += 1
    return X(f"Factorise fully {k * a}y − {k * b}.", f"{k}({a}y-{b})", vars="y", must=["\\("], o="O4")
def g3(r):
    a = r.randint(2, 9)
    return X(f"Factorise x² + {a}x.", f"x(x+{a})", must=["\\("], o="O4", reason=f"Both terms contain x: x(x + {a}).")
def g4(r):
    k, a, b = r.randint(2, 6), r.randint(1, 5), r.randint(1, 7)
    while gcd(a, b) != 1: b += 1
    return X(f"Factorise fully {k * a}x² + {k * b}x.", f"{k}x({a}x+{b})", must=["\\("], o="O4", d="H", reason=f"HCF = {k}x.")
def g5(r):
    k = r.randint(2, 9); a, b = r.randint(1, 5), r.randint(1, 5)
    return N(f"What is the highest common factor of {k * a * 2}p and {k * b * 2 + k * 2}?", gcd(k * a * 2, k * b * 2 + k * 2), o="O4", reason="Find the HCF of the numbers (p is not in both terms).")
def g6(r):
    k = r.randint(2, 6)
    return MC(f"Which is {4 * k}x + {8 * k} factorised fully?", f"{4 * k}(x + 2)", [(f"{2 * k}(2x + 4)", "2x + 4 still has a common factor of 2."), (f"4(x + {2 * k})", f"4 is not the HCF; check {k}x."), (f"{4 * k}(x + 8)", "Expand it to check.")], o="O4")
def g7(r):
    a, b, c = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
    return X(f"Factorise fully {a * c}ab + {b * c}a.", f"{c}a({a}b+{b})" if gcd(a, b) == 1 else f"{c * gcd(a, b)}a({a // gcd(a, b)}b+{b // gcd(a, b)})", vars="ab", must=["\\("], o="O4", d="H")
def g8(r):
    k, a, b, c = r.randint(2, 5), r.randint(1, 4), r.randint(1, 4), r.randint(1, 4)
    while gcd(gcd(a, b), c) != 1: c += 1
    return X(f"Factorise fully {k * a}x + {k * b}y + {k * c}.", f"{k}({a}x+{b}y+{c})", vars="xy", must=["\\("], o="O4", d="H")


def g9(r):
    rows = [("6x + 9 = 3(2x + 3)", "Yes"), ("8x + 12 = 2(4x + 6)", "No"), ("10y − 5 = 5(2y − 1)", "Yes"), ("x² + 4x = x(x + 4)", "Yes"), ("12a + 18 = 3(4a + 6)", "No"), ("4t² + 6t = 2(2t² + 3t)", "No")]
    return GD("Is each expression factorised fully?", "Fully factorised?", r.sample(rows, 4), o="O4", d="H")
def g10(r):
    k, a = r.randint(2, 9), r.randint(2, 9)
    return X(f"A rectangle has area ({k * a}x + {k * 2 * a + k}) cm² and width {k} cm. Write an expression for its length.", f"{a}x+{2 * a + 1}", o="O4", d="H", mustNot=["\\("], fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": ["?", f"{k} cm", "", ""]}, reason=f"{k * a}x + {k * (2 * a + 1)} = {k}({a}x + {2 * a + 1}).")


s.std([g9, g10, g1, g2, g3, g5, g6, g4, g7, g8], EX("Explain how to check that 6x + 9 = 3(2x + 3) is correct.", [("expand the bracket", ["expand|multiply out|multiply.*bracket"]), ("3 × 2x = 6x and 3 × 3 = 9", ["6x|= ?9|3 ?× ?3"])], "Expand the bracket: 3 × 2x = 6x and 3 × 3 = 9, which gives 6x + 9, the original expression.", o="O4"))

# ================================================================== 2.5
s = U.section("2.5", "Constructing and solving equations", ["O5"])
s.idea("Solving equations", ["An **equation** has an equals sign and an unknown. Solve it by doing the **same to both sides** until the letter is on its own.",
       "With unknowns on both sides, first move the smaller x-term: 5x + 3 = 2x + 18 → 3x + 3 = 18 → 3x = 15 → x = 5."])
s.example("With brackets", "Solve 4(x − 2) = 2x + 6.", [("4x − 8 = 2x + 6", "expand"), ("2x − 8 = 6", "subtract 2x"), ("2x = 14", "add 8"), ("x = 7", "divide by 2")], "x = 7")
s.check(N("Solve 3x + 7 = 31.", 8, "×", o="O5", reason="3x = 24, x = 8."))
s.idea("Constructing", ["Write an equation from the information, then solve it. Check your answer in the original problem."])
s.mistake("Same to both sides", ["If you subtract 5 from the left, subtract 5 from the right too."])


def q1(r):
    a, x, b = r.randint(2, 9), r.randint(-5, 12), r.randint(1, 20)
    return N(f"Solve {a}x + {b} = {a * x + b}.", x, o="O5", reason=f"{a}x = {a * x}, x = {x}.")
def q2(r):
    a, x, b = r.randint(2, 9), r.randint(1, 12), r.randint(1, 20)
    return N(f"Solve {a}x − {b} = {a * x - b}.", x, o="O5", reason=f"{a}x = {a * x}, x = {x}.")
def q3(r):
    a, c = r.sample(range(2, 10), 2); x = r.randint(1, 10); b = r.randint(1, 20); d = a * x + b - c * x
    if a < c: a, c = c, a; d = a * x + b - c * x
    return N(f"Solve {a}x + {b} = {c}x {'+' if d >= 0 else '−'} {abs(d)}.", x, o="O5", d="H", reason=f"{a - c}x + {b} = {d} → {a - c}x = {d - b} → x = {x}.")
def q4(r):
    a, x, b = r.randint(2, 6), r.randint(2, 10), r.randint(1, 9)
    return N(f"Solve {a}(x − {b}) = {a * (x - b)}.", x, o="O5", reason=f"x − {b} = {x - b}, x = {x}.")
def q5(r):
    x, k = r.randint(3, 20), r.randint(2, 6)
    return N(f"Solve x/{k} + 3 = {x // k + 3 if x % k == 0 else 0}.".replace(f" = 0.", "."), x if x % k == 0 else 0, o="O5") if x % k == 0 else None
def q6(r):
    x, d = r.randint(3, 15), r.randint(2, 9)
    return N(f"I think of a number, double it and subtract {d}. The answer is the same as when I add {x - d} to the number. What is my number?", x, o="O5", d="H", reason=f"2n − {d} = n + {x - d} → n = {x}.")
def q7(r):
    w, d = r.randint(3, 12), r.randint(2, 8)
    return N(f"A rectangle is {d} cm longer than it is wide. Its perimeter is {4 * w + 2 * d} cm. Find its width.", w, "cm", units=["cm"], o="O5", d="H", reason=f"2w + 2(w + {d}) = {4 * w + 2 * d} → 4w = {4 * w} → w = {w}.", fig={"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": [f"w + {d}", "w", "", ""]})
def q8(r):
    x = r.randint(20, 60); k = r.randint(2, 3)
    return N(f"The angles of a triangle are x°, {k}x° and {180 - (k + 1) * x}°. Find x.", x, "°", units=["°"], o="O5", d="H", reason=f"{k + 1}x + {180 - (k + 1) * x} = 180 → x = {x}.", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [3, 5]], "ang": ["x°", f"{k}x°", f"{180 - (k + 1) * x}°"]}) if 180 - (k + 1) * x > 0 else None
def q9(r):
    a, x = r.randint(2, 6), r.randint(2, 9); b, c = r.randint(1, 5), r.randint(1, 5)
    rhs = a * (x + b) - c
    return N(f"Solve {a}(x + {b}) − {c} = {rhs}.", x, o="O5", reason=f"{a}x + {a * b - c} = {rhs} → x = {x}.")


s.std([q7, q8, q1, q2, q4, q9, q3, q6], EX("Explain why the equation x + 5 = x + 7 has no solution.", [("subtracting x leaves 5 = 7", ["5 ?= ?7|subtract x|take away x"]), ("which is never true", ["never|false|not true|impossible"])], "Subtracting x from both sides gives 5 = 7, which is never true, so no value of x works.", o="O5"))

# ================================================================== 2.6
s = U.section("2.6", "Inequalities", ["O6"])
s.idea("Inequality signs", ["**<** less than, **>** greater than, **≤** less than or equal to, **≥** greater than or equal to.",
       "On a number line, an **open circle** ○ means the number is not included (< or >); a **filled circle** ● means it is included (≤ or ≥)."],
       fig={"kind": "numline", "min": -3, "max": 6, "from": {"v": -1, "closed": True}, "to": {"v": 4, "closed": False}})
s.check(N("x is an integer and −1 ≤ x < 4. How many possible values of x are there?", 5, o="O6", reason="−1, 0, 1, 2, 3: five integers."))
s.idea("Solving inequalities", ["Solve like an equation: 3x + 2 > 14 → 3x > 12 → x > 4."])
s.mistake("Open or closed?", ["x < 3 does NOT include 3, so its circle is open."])


def n1(r):
    a, x, b = r.randint(2, 9), r.randint(-3, 10), r.randint(1, 15)
    sgn = pick(r, ["<", ">", "≤", "≥"])
    return S(f"Solve {a}x + {b} {sgn} {a * x + b}.", [f"x {sgn} {x}", f"x{sgn}{x}", f"x {sgn}{x}", f"x{sgn} {x}"] + ([f"x <= {x}"] if sgn == "≤" else [f"x >= {x}"] if sgn == "≥" else []), o="O6", reason=f"{a}x {sgn} {a * x} → x {sgn} {x}.")
def n2(r):
    lo, hi = r.randint(-5, 3), None; hi = lo + r.randint(3, 7)
    a, b = pick(r, [("≤", "<"), ("<", "≤"), ("<", "<"), ("≤", "≤")])
    n = (hi - lo + 1) - (1 if a == "<" else 0) - (1 if b == "<" else 0)
    return N(f"x is an integer and {lo} {a} x {b} {hi}. How many possible values of x are there?", n, o="O6", reason=f"Count the integers from {lo + (1 if a == '<' else 0)} to {hi - (1 if b == '<' else 0)}.")
def n3(r):
    v = r.randint(-3, 5); c = pick(r, [("x > ", False, "right"), ("x ≥ ", True, "right"), ("x < ", False, "left"), ("x ≤ ", True, "left")])
    fig = {"kind": "numline", "min": -5, "max": 8, "from": {"v": v, "closed": c[1]} if c[2] == "right" else None, "to": {"v": v, "closed": c[1]} if c[2] == "left" else None}
    return S("Write the inequality shown on the number line, using x.", [f"{c[0]}{v}", f"{c[0].replace(' ', '')}{v}"], o="O6", fig=fig, reason=f"{'Filled' if c[1] else 'Open'} circle at {v}, arrow to the {c[2]}: {c[0]}{v}.")
def n4(r):
    v = r.randint(2, 9)
    return MS(f"Select ALL the integers that satisfy x > {v}.", [str(v + 1), str(v + 4)], [str(v), str(v - 2)], o="O6")
def n5(r):
    a, b, c = r.randint(2, 5), r.randint(1, 9), r.randint(2, 9)
    return N(f"The smallest integer that satisfies {a}x − {b} > {a * c - b} is…", c + 1, o="O6", d="H", reason=f"{a}x > {a * c} → x > {c}, so the smallest integer is {c + 1}.")
def n6(r):
    p, k = r.randint(2, 9), r.randint(15, 60)
    return N(f"Pens cost ${p}. Tom has ${k}. Write and solve an inequality to find the greatest number of pens he can buy.", k // p, "pens", units=["pens"], o="O6", d="H", reason=f"{p}n ≤ {k} → n ≤ {fmt(k / p)} → {k // p} pens.")
def n7(r):
    rows = [("x < 4", "Open circle"), ("x ≥ −2", "Filled circle"), ("x ≤ 0", "Filled circle"), ("x > 7", "Open circle")]
    return GD("Which circle would you draw on a number line?", "Circle", rows, o="O6")


s.std([n3, n7, n1, n2, n4, n5, n6], EX("Explain the difference between x < 5 and x ≤ 5.", [("x < 5 does not include 5", ["not include|less than 5|excludes|not 5"]), ("x ≤ 5 includes 5", ["includes 5|can be 5|or equal|equal to 5"])], "x < 5 means x is less than 5, so 5 is not included (open circle). x ≤ 5 means less than or equal to 5, so 5 is included (filled circle).", o="O6"))

U.mindmap(("Expressions", "No equals sign • collect like terms • 2n − 6", "O1", "2.1"), ("Formulae", "Substitute with brackets for negatives • change the subject", "O2", "2.2"),
          ("Expanding", "Multiply every term • −(−) = +", "O3", "2.3"), ("Factorising", "Take out the HCF • check by expanding", "O4", "2.4"),
          ("Equations", "Same to both sides • unknowns on both sides", "O5", "2.5"), ("Inequalities", "< > ≤ ≥ • open or filled circle", "O6", "2.6"))
