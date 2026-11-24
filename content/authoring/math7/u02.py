# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 2 Expressions, formulae and equations (2.1 Constructing expressions, 2.2 Using expressions and
formulae, 2.3 Collecting like terms, 2.4 Expanding brackets, 2.5 Constructing and solving equations, 2.6 Inequalities).
Written by the Atomic teaching team."""
from kit import *

U = Unit(2, "Expressions, Formulae and Equations", "Algebra",
         "Using letters for unknown numbers, substituting into expressions and formulae, collecting like terms, expanding a bracket, solving simple equations and writing inequalities.",
         {"O1": {"code": "7Ae.01", "sec": "2.1", "codeNote": "", "t": "Understand that letters represent unknown numbers and write expressions from words."},
          "O2": {"code": "7Ae.02", "sec": "2.2", "codeNote": "", "t": "Substitute positive integers into expressions and simple formulae."},
          "O3": {"code": "7Ae.03", "sec": "2.3", "codeNote": "", "t": "Simplify expressions by collecting like terms."},
          "O4": {"code": "7Ae.04", "sec": "2.4", "codeNote": "", "t": "Multiply a number over a bracket containing a linear expression."},
          "O5": {"code": "7Ae.05", "sec": "2.5", "codeNote": "", "t": "Construct and solve simple linear equations (one or two steps)."},
          "O6": {"code": "7Ae.06", "sec": "2.6", "codeNote": "", "t": "Understand and use inequality signs, and show simple inequalities on a number line."}})
RECT = lambda a, b: {"kind": "shape", "pts": [[0, 0], [9, 0], [9, 4], [0, 4]], "s": [a, b, "", ""]}

# ================================================================== 2.1
s = U.section("2.1", "Constructing expressions", ["O1"])
s.idea("Letters for numbers", ["A letter can stand for an unknown number. If a box holds n pencils, 3 boxes hold **3n** pencils and 3 boxes plus 2 pencils is **3n + 2**.",
       "Write 3 × n as 3n, n ÷ 2 as n/2 or ½n, and n × n as n²."])
s.example("Ages", "Ali is a years old. His sister is 4 years older. Write an expression for her age.", [("4 years older → add 4", "")], "a + 4")
s.check(X("A bag has b sweets. Write an expression for the number of sweets in 5 bags.", "5b", vars="b", o="O1"))
s.mistake("Less than", ["'7 less than n' is n − 7, not 7 − n."])
W = [("y plus 6", "y+6", "y"), ("8 more than t", "t+8", "t"), ("p take away 3", "p-3", "p"), ("double k", "2k", "k"), ("n multiplied by 7", "7n", "n"), ("m divided by 5", "m/5", "m"),
     ("4 less than 3 times x", "3x-4", "x"), ("half of w, plus 1", "w/2+1", "w"), ("the square of a", "a^2", "a"), ("10 minus c", "10-c", "c")]


def c1(r):
    w = pick(r, W)
    return X(f"Write an expression for: {w[0]}.", w[1], vars=w[2], o="O1")
def c2(r):
    n, k = r.randint(2, 9), r.randint(1, 9)
    return X(f"A pack of cards has c cards. Lily has {n} packs and {k} extra cards. Write an expression for how many cards she has.", f"{n}c+{k}", vars="c", o="O1")
def c3(r):
    s_ = r.randint(2, 9)
    return X(f"Each side of a regular shape is s cm. The shape has {s_ + 2} sides. Write an expression for its perimeter.", f"{s_ + 2}s", vars="s", o="O1", fig={"kind": "shape", "pts": [[0, 0], [4, 0], [5, 3], [2, 5], [-1, 3]] if s_ + 2 == 5 else [[0, 0], [4, 0], [4, 4], [0, 4]], "s": ["s cm"]} if s_ + 2 in (4, 5) else None)
def c4(r):
    a = r.randint(2, 9)
    return X("Write an expression for the perimeter of the rectangle.", f"2x+{2 * a}", o="O1", fig=RECT("x cm", f"{a} cm"), reason=f"x + {a} + x + {a} = 2x + {2 * a}.")
def c5(r):
    k = r.randint(2, 9)
    return MC(f"Which expression means 'n divided by {k}'?", f"n/{k}", [f"{k}/n", f"{k}n", f"n − {k}"], o="O1")
def c6(r):
    rows = [("3 more than n", "n + 3"), ("3 times n", "3n"), ("n less 3", "n − 3"), ("n divided by 3", "n/3"), ("n squared", "n²")]
    return GD("Match each description to its expression.", "Expression", r.sample(rows, 4), o="O1", extra=["3 − n"])
def c7(r):
    p = r.randint(2, 9); q = r.randint(2, 9)
    return X(f"Pens cost p cents and rulers cost r cents. Write an expression for the cost of {p} pens and {q} rulers.", f"{p}p+{q}r", vars="pr", o="O1")
def c8(r):
    a = r.randint(2, 6)
    return X(f"Tom is t years old. His dad is {a} times as old as Tom. Write an expression for the sum of their ages.", f"{a + 1}t", vars="t", o="O1", d="H", reason=f"t + {a}t = {a + 1}t.")


s.std([c4, c6, c1, c2, c5, c7, c3, c8], EX("Explain the difference between 3n and n + 3.", [("3n means 3 multiplied by n", ["multipl|times|3 lots|3 ?× ?n"]), ("n + 3 means add 3 to n", ["add|plus|3 more"])], "3n means 3 × n (three lots of n). n + 3 means n with 3 added on. For n = 5: 3n = 15 but n + 3 = 8.", o="O1"))

# ================================================================== 2.2
s = U.section("2.2", "Using expressions and formulae", ["O2"])
s.idea("Substitution", ["To **substitute**, replace each letter with its number, then calculate. If x = 4: 3x + 1 = 3 × 4 + 1 = 13.",
       "A **formula** shows how quantities are related, e.g. the perimeter of a rectangle P = 2l + 2w."])
s.check(N("Find the value of 5a − 2 when a = 6.", 28, o="O2"))
s.mistake("Order of operations", ["In 2 + 3x with x = 4, multiply first: 2 + 12 = 14, not 5 × 4 = 20."])


def u1(r):
    a, b, x = r.randint(2, 9), r.randint(1, 15), r.randint(1, 12)
    return N(f"Find the value of {a}x + {b} when x = {x}.", a * x + b, o="O2")
def u2(r):
    x, y = r.randint(2, 12), r.randint(2, 12)
    return N(f"Find the value of xy when x = {x} and y = {y}.", x * y, o="O2")
def u3(r):
    x = r.randint(2, 12)
    return N(f"Find the value of x² + 1 when x = {x}.", x * x + 1, o="O2")
def u4(r):
    l, w = r.randint(3, 20), r.randint(2, 15)
    return N(f"Use P = 2l + 2w to find the perimeter when l = {l} and w = {w}.", 2 * l + 2 * w, "cm", units=["cm"], o="O2", fig=RECT("l", "w"))
def u5(r):
    c, h = r.randint(10, 30), r.randint(2, 6); rate = r.randint(5, 15)
    return N(f"A bike costs C = {c} + {rate}h dollars to hire for h hours. Find the cost for {h} hours.", c + rate * h, "$", units=["$"], o="O2")
def u6(r):
    a = r.randint(2, 5); xs = r.sample(range(1, 10), 3)
    return TB(f"Complete the table for the expression {a}n − 1.", ["n", f"{a}n − 1"], [[str(x), B(a * x - 1)] for x in sorted(xs)], o="O2")
def u7(r):
    x = r.randint(2, 10); y = r.randint(2, 10)
    return N(f"Find the value of (x + y) ÷ 2 when x = {2 * x} and y = {2 * y}.", x + y, o="O2", d="H")
def u8(r):
    d, t = r.randint(2, 9) * 10, r.randint(2, 5)
    return N(f"Use the formula s = d ÷ t to find the speed s when d = {d * t} km and t = {t} hours.", d, "km/h", units=["km/h"], o="O2")


s.std([u4, u6, u1, u2, u3, u5, u7, u8], EX("Explain why 4n² is 64 when n = 4, not 256.", [("square n first: 4² = 16", ["square.*first|4² ?= ?16|16"]), ("then multiply by 4: 4 × 16 = 64", ["4 ?× ?16|64"])], "Only n is squared: 4² = 16. Then multiply by 4: 4 × 16 = 64. (256 would be (4n)².)", o="O2"))

# ================================================================== 2.3
s = U.section("2.3", "Collecting like terms", ["O3"])
s.idea("Like terms", ["**Like terms** have exactly the same letters: 4a and 7a are like terms; 4a and 4b are not.",
       "Collect like terms by adding or subtracting their numbers: 4a + 2b + 3a − b = 7a + b."])
s.check(X("Simplify 6x + 3 + 2x − 1.", "8x+2", o="O3", mustNot=["\\("]))
s.mistake("Keep the sign", ["The sign belongs to the term after it: in 5x − 2y + 3x the −2y stays negative."])


def l1(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return X(f"Simplify {a}y + {b}y.", f"{a + b}y", vars="y", o="O3")
def l2(r):
    a, b, c, d = r.randint(2, 9), r.randint(1, 9), r.randint(1, 9), r.randint(1, 9)
    return X(f"Simplify {a}a + {b}b + {c}a + {d}b.", f"{a + c}a+{b + d}b", vars="ab", o="O3", mustNot=["\\("])
def l3(r):
    a, b, c = r.randint(5, 12), r.randint(1, 4), r.randint(1, 9)
    return X(f"Simplify {a}m − {b}m + {c}.", f"{a - b}m+{c}", vars="m", o="O3", mustNot=["\\("])
def l4(r):
    rows = [("2x and 5x", "Like"), ("3y and 3z", "Not like"), ("ab and ba", "Like"), ("4 and 4t", "Not like"), ("x² and 2x²", "Like")]
    return GD("Are these like terms?", "Like terms?", r.sample(rows, 4), o="O3")
def l5(r):
    a, b = r.randint(2, 6), r.randint(1, 9)
    return X("Write a simplified expression for the perimeter of this triangle.", f"{3 * a}x+{2 * b}", o="O3", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [4, 6]], "s": [f"{a}x", f"{a}x + {b}", f"{a}x + {b}"]})
def l6(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return MC(f"Which is {a}p + {b}q + p simplified?", f"{a + 1}p + {b}q", [f"{a + b + 1}pq", f"{a}p + {b + 1}q", f"{a + b}p + q"], o="O3")
def l7(r):
    a, b, c, d = r.randint(3, 9), r.randint(1, 5), r.randint(2, 8), r.randint(1, 5)
    return X(f"Simplify {a}x − {b}y − {c}x + {d}y.", f"{a - c}x+({d - b})y", vars="xy", o="O3", d="H", mustNot=["\\("], show=poly((a - c, 'x'), (d - b, 'y')))


s.std([l4, l5, l1, l2, l3, l6, l7], EX("Explain why 3a + 2b cannot be simplified but 3a + 2a can.", [("3a and 2b have different letters, so they are not like terms", ["different letter|not like|unlike"]), ("3a and 2a are like terms: 5a", ["5a|like terms|same letter"])], "3a and 2b have different letters, so they are not like terms and cannot be added. 3a and 2a are like terms, so 3a + 2a = 5a.", o="O3"))

# ================================================================== 2.4
s = U.section("2.4", "Expanding brackets", ["O4"])
s.idea("Multiply everything inside", ["To **expand** 3(x + 4), multiply each term in the bracket by 3: 3x + 12.",
       "Think of an area: a rectangle 3 by (x + 4) splits into 3 × x and 3 × 4."], fig=RECT("x + 4", "3"))
s.check(X("Expand 5(y − 2).", "5y-10", vars="y", o="O4", mustNot=["\\("]))
s.mistake("Both terms", ["2(n + 6) is 2n + 12, not 2n + 6."])


def e1(r):
    a, b = r.randint(2, 9), r.randint(1, 12)
    return X(f"Expand {a}(x + {b}).", f"{a}x+{a * b}", o="O4", mustNot=["\\("])
def e2(r):
    a, b = r.randint(2, 9), r.randint(1, 12)
    return X(f"Expand {a}(n − {b}).", f"{a}n-{a * b}", vars="n", o="O4", mustNot=["\\("])
def e3(r):
    a, b, c = r.randint(2, 6), r.randint(2, 5), r.randint(1, 9)
    return X(f"Expand {a}({b}y + {c}).", f"{a * b}y+{a * c}", vars="y", o="O4", mustNot=["\\("])
def e4(r):
    a, b = r.randint(2, 9), r.randint(1, 9)
    return X("Write an expanded expression for the area of the rectangle.", f"{a}x+{a * b}", o="O4", fig=RECT(f"x + {b}", str(a)), mustNot=["\\("])
def e5(r):
    a, b, c = r.randint(2, 5), r.randint(1, 6), r.randint(1, 9)
    return X(f"Expand and simplify {a}(x + {b}) + {c}.", f"{a}x+{a * b + c}", o="O4", d="H", mustNot=["\\("])
def e6(r):
    a, b = r.randint(2, 9), r.randint(1, 9)
    return MC(f"Which is the expansion of {a}(m + {b})?", f"{a}m + {a * b}", [f"{a}m + {b}", f"m + {a * b}", f"{a + b}m"], o="O4")
def e7(r):
    a, b = r.randint(2, 6), r.randint(1, 9); xs = r.sample(range(1, 6), 2)
    return TB(f"Check that {a}(x + {b}) = {a}x + {a * b} by completing the table.", ["x", f"{a}(x + {b})", f"{a}x + {a * b}"], [[str(x), B(a * (x + b)), B(a * x + a * b)] for x in xs], o="O4")


s.std([e4, e7, e1, e2, e3, e6, e5], EX("Explain why 4(x + 5) = 4x + 20.", [("the 4 multiplies every term in the bracket", ["every|both|each"]), ("4 × x = 4x and 4 × 5 = 20", ["4 ?× ?5|20"])], "When you expand, the 4 multiplies each term in the bracket: 4 × x = 4x and 4 × 5 = 20, giving 4x + 20.", o="O4"))

# ================================================================== 2.5
s = U.section("2.5", "Constructing and solving equations", ["O5"])
s.idea("Balancing", ["An **equation** is like a balance: do the **same** to both sides to keep it level. To solve 3x + 5 = 20: subtract 5 (3x = 15), then divide by 3 (x = 5).",
       "Check by substituting: 3 × 5 + 5 = 20 ✓."])
s.check(N("Solve x + 9 = 21.", 12, o="O5"))
s.check(N("Solve 4x − 3 = 25.", 7, o="O5"))
s.mistake("Undo in reverse", ["For 2x + 7 = 19, undo the + 7 first, then the × 2."])


def q1(r):
    x, b = r.randint(1, 30), r.randint(1, 30)
    return N(f"Solve x + {b} = {x + b}.", x, o="O5")
def q2(r):
    a, x = r.randint(2, 12), r.randint(1, 12)
    return N(f"Solve {a}x = {a * x}.", x, o="O5")
def q3(r):
    a, x, b = r.randint(2, 9), r.randint(1, 12), r.randint(1, 20)
    return N(f"Solve {a}x + {b} = {a * x + b}.", x, o="O5")
def q4(r):
    a, x, b = r.randint(2, 9), r.randint(2, 12), r.randint(1, 15)
    return N(f"Solve {a}x − {b} = {a * x - b}.", x, o="O5")
def q5(r):
    k, x = r.randint(2, 6), r.randint(2, 12)
    return N(f"Solve x/{k} = {x}.", k * x, o="O5")
def q6(r):
    a, n, b = r.randint(2, 6), r.randint(2, 15), r.randint(1, 12)
    return N(f"I think of a number, multiply it by {a} and add {b}. The answer is {a * n + b}. What is my number?", n, o="O5")
def q7(r):
    w = r.randint(2, 12); l = w + r.randint(1, 6)
    return N(f"The perimeter of this rectangle is {2 * (w + l)} cm. Find x.", w, "cm", units=["cm"], o="O5", d="H", fig=RECT(f"x + {l - w}", "x"), reason=f"4x + {2 * (l - w)} = {2 * (w + l)} → x = {w}.")
def q8(r):
    x = r.randint(10, 50)
    return N(f"Two angles on a straight line are x° and {180 - x}°... find x when the other angle is {180 - x}°.".split("...")[0] + f". Find x.", x, "°", units=["°"], o="O5", reason=f"x + {180 - x} = 180.") if False else N(f"Two angles on a straight line are x° and {180 - x}°. Find x.", x, "°", units=["°"], o="O5", reason=f"x + {180 - x} = 180, so x = {x}.")
def q9(r):
    a, x, b = r.randint(2, 6), r.randint(1, 10), r.randint(1, 10)
    return TB(f"Solve {a}x + {b} = {a * x + b} step by step.", ["Step", "Value"], [[f"{a}x = ", B(a * x)], ["x = ", B(x)]], o="O5")


s.std([q7, q9, q1, q2, q3, q4, q5, q6, q8], EX("Explain how to check that x = 6 is the solution of 3x − 4 = 14.", [("substitute x = 6", ["substitute|put 6|3 ?× ?6"]), ("3 × 6 − 4 = 14, so it is correct", ["18|= ?14|correct|true"])], "Substitute x = 6: 3 × 6 − 4 = 18 − 4 = 14, which matches the right-hand side, so x = 6 is correct.", o="O5"))

# ================================================================== 2.6
s = U.section("2.6", "Inequalities", ["O6"])
s.idea("Signs", ["**<** means 'is less than', **>** means 'is greater than'. 3 < 8 and 10 > −2.",
       "x > 4 means x can be any number bigger than 4. On a number line, use an **open circle** at 4 and an arrow to the right."], fig={"kind": "numline", "min": 0, "max": 9, "from": {"v": 4, "closed": False}})
s.check(MC("Which sign goes between −3 and −7?  −3 ☐ −7", ">", [("<", "−3 is to the right of −7."), ("=", "")], o="O6"))
s.mistake("Open or closed", ["x < 5 does not include 5, so the circle is open. x ≤ 5 includes 5: the circle is filled."])


def n1(r):
    a, b = r.sample(range(-15, 16), 2)
    return CMP(str(a), str(b), "<" if a < b else ">", o="O6")
def n2(r):
    v = r.randint(1, 8); k = pick(r, [(">", False, True), ("<", False, False), ("≥", True, True), ("≤", True, False)])
    fig = {"kind": "numline", "min": -2, "max": 10, "from": {"v": v, "closed": k[1]}} if k[2] else {"kind": "numline", "min": -2, "max": 10, "to": {"v": v, "closed": k[1]}}
    return MC("Which inequality is shown on the number line?", f"x {k[0]} {v}", [f"x {o} {v}" for o in (">", "<", "≥", "≤") if o != k[0]], o="O6", fig=fig)
def n3(r):
    v = r.randint(2, 9)
    return MS(f"Select ALL the whole numbers that satisfy x < {v}.", [str(v - 1), str(v - 2)], [str(v), str(v + 2)], o="O6")
def n4(r):
    lo, hi = r.randint(-3, 3), None; hi = lo + r.randint(3, 7)
    return N(f"How many whole numbers x satisfy {lo} < x < {hi}?", hi - lo - 1, o="O6", d="H")
def n5(r):
    rows = [("is less than", "<"), ("is greater than", ">"), ("is less than or equal to", "≤"), ("is greater than or equal to", "≥")]
    return GD("Match each phrase to its sign.", "Sign", rows, o="O6")
def n6(r):
    a = r.randint(10, 18)
    return MC(f"You must be at least {a} years old to join a club. Which inequality shows the age, a, of a member?", f"a ≥ {a}", [f"a > {a}", f"a ≤ {a}", f"a < {a}"], o="O6", d="H")
def n7(r):
    vs = r.sample(range(-9, 10), 3)
    return TB("Write < or > in each row (type the sign).", ["Pair", "Sign"], [[f"{vs[0]} and {vs[1]}", B("<" if vs[0] < vs[1] else ">")]], o="O6") if False else GD("Is each statement true or false?", "True or false", [(f"{a} < {b}", "True" if a < b else "False") for a, b in [r.sample(range(-9, 10), 2) for _ in range(4)]], o="O6")


s.std([n2, n5, n1, n3, n4, n6, n7], EX("Explain the difference between x > 3 and x ≥ 3.", [("x > 3 does not include 3", ["not include|open|bigger than 3"]), ("x ≥ 3 includes 3", ["includes|can be 3|equal|filled"])], "x > 3 means bigger than 3, so 3 itself is not included (open circle). x ≥ 3 means 3 or bigger, so 3 is included (filled circle).", o="O6"))

U.mindmap(("Expressions", "Letters for numbers • 3n, n + 3, n/2", "O1", "2.1"), ("Substitution", "Replace letters • order of operations", "O2", "2.2"),
          ("Like terms", "Same letters • add their numbers", "O3", "2.3"), ("Expanding", "Multiply every term", "O4", "2.4"),
          ("Equations", "Same to both sides • check", "O5", "2.5"), ("Inequalities", "< > ≤ ≥ • open or filled circle", "O6", "2.6"))
