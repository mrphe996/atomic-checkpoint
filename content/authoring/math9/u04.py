# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 4 Equations and inequalities. Written by the Atomic teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(4, "Equations and Inequalities", "Algebra",
         "Constructing and solving linear equations (including brackets and fractions), simultaneous equations, and inequalities on a number line.",
         {"O1": {"sec": "4.1", "code": "9Ae.07", "codeNote": "", "t": "Construct and solve linear equations with unknowns on both sides, brackets and fractions."},
          "O2": {"sec": "4.2", "code": "9Ae.08", "codeNote": "", "t": "Solve a pair of simultaneous linear equations by substitution or elimination, and link the solution to where two lines meet."},
          "O3": {"sec": "4.3", "code": "9Ae.09", "codeNote": "", "t": "Construct and solve linear inequalities, show solutions on a number line and list integer solutions."}})

def lin(a, b, v="x"): return poly((a, v), (b, ""))

# ================================================================== 4.1
s = U.section("4.1", "Constructing and solving equations", ["O1"])
s.idea("Balancing", ["An equation stays true if you do **the same thing to both sides**. Collect the unknown on one side and the numbers on the other.",
       "With brackets, **expand first**. With fractions, **multiply every term** by the denominator (or the lowest common multiple of the denominators)."])
s.example("Unknowns on both sides", "Solve 5x − 7 = 2x + 11.", [("3x − 7 = 11", "subtract 2x from both sides"), ("3x = 18", "add 7"), ("x = 6", "divide by 3")], "x = 6")
s.check(N("Solve 4x + 3 = x + 21.", 6, o="O1", reason="3x = 18, x = 6."))
s.example("Fractions", "Solve (x + 4)/3 = (x − 2)/2.", [("2(x + 4) = 3(x − 2)", "multiply both sides by 6"), ("2x + 8 = 3x − 6", ""), ("x = 14", "")], "x = 14")
s.example("Constructing", "The angles of a triangle are x, 2x + 10 and 3x − 40 degrees. Find x.", [("x + 2x + 10 + 3x − 40 = 180", "angles in a triangle"), ("6x − 30 = 180", ""), ("x = 35", "")], "x = 35")
s.check(N("The perimeter of a square of side 2x − 3 is 36 cm. Find x.", 6, o="O1", d="H", reason="4(2x − 3) = 36 → 8x − 12 = 36 → x = 6."))
s.mistake("Multiply every term", ["When you clear fractions, multiply EVERY term: x/2 + 3 = 7 → x + 6 = 14, not x + 3 = 14."])
def e1(r):
    x = nz(r, -9, 12); a, c = r.sample(range(2, 10), 2); b = r.randint(-15, 15); d = (a - c) * x + b
    return N(f"Solve {lin(a, b)} = {lin(c, d)}.", x, o="O1", reason=f"({a} − {c})x = {d} − ({b}) → x = {x}.")
def e2(r):
    x = nz(r, -8, 10); a, b, c = r.randint(2, 6), r.randint(-6, 6), r.randint(2, 5); k = a * (x + b) - c * x
    return N(f"Solve {a}(x {'+ ' + str(b) if b >= 0 else '− ' + str(-b)}) = {c}x {'+ ' + str(k) if k >= 0 else '− ' + str(-k)}." if a != c else f"Solve {a}(x + {b}) = 2.", x if a != c else None, o="O1", d="H") if a != c else None
def e3(r):
    x = r.randint(-6, 20); a, b = pick(r, [2, 3, 4, 5]), pick(r, [2, 3, 5, 6]); p, q = r.randint(-5, 5), None
    if a == b: return None
    # (x + p)/a = (x + q)/b → b(x+p) = a(x+q) → q = (b(x+p) − a x)/a must be integer
    if (b * (x + p) - a * x) % a: return None
    q = (b * (x + p) - a * x) // a
    return N(f"Solve (x {'+ ' + str(p) if p >= 0 else '− ' + str(-p)})/{a} = (x {'+ ' + str(q) if q >= 0 else '− ' + str(-q)})/{b}.", x, o="O1", d="H", reason=f"Multiply by {a*b}: {b}(x + {p}) = {a}(x + {q}) → x = {x}.")
def e4(r):
    x = r.randint(10, 50); k = r.randint(5, 40)
    return N(f"I think of a number, multiply it by 3 and subtract {k}. The answer is the same as when I add {2*x - k} to the number. What is my number?", x, o="O1", d="H", reason=f"3n − {k} = n + {2*x-k} → 2n = {2*x} → n = {x}.")
def e5(r):
    x = r.randint(15, 40); a, b = r.randint(1, 3), r.randint(5, 30); c = 180 - x - (a * x + b)
    if c <= 0: return None
    return N(f"The angles of a triangle are x°, ({a}x + {b})° and {c}°. Find x.", x, o="O1", fig={"kind": "shape", "pts": [[0, 0], [7, 0], [2.5, 4]], "ang": ["x°", f"({a}x + {b})°", f"{c}°"]}, reason=f"x + {a}x + {b} + {c} = 180 → {a+1}x = {180-b-c} → x = {x}.")
def e6(r):
    w = r.randint(3, 15); d_ = r.randint(2, 9)
    return N(f"A rectangle is {d_} cm longer than it is wide. Its perimeter is {4*w + 2*d_} cm. Find its width.", w, "cm", units=["cm", "cm²"], o="O1", reason=f"2w + 2(w + {d_}) = {4*w+2*d_} → 4w = {4*w} → w = {w}.")
def e7(r):
    x = Fr(r.randint(1, 19), pick(r, [2, 4, 5])); a, b = r.randint(2, 9), r.randint(1, 9); c = a * x + b
    if c.denominator != 1: return None
    return N(f"Solve {a}x + {b} = {c}. Give your answer as a fraction or decimal.", float(x), o="O1", tol=1e-6)
def e8(r):
    x = nz(r, -5, 9); a = r.randint(2, 5)
    return MC(f"Which equation has the solution x = {x}?", f"{a}(x − 1) = {a*(x-1)}", [(f"{a}x − 1 = {a*(x-1)}", ""), (f"{a}(x + 1) = {a*(x-1)}", ""), (f"x/{a} = {a*x}", "")], o="O1", d="M")
def e9(r):
    x = r.randint(2, 12)
    return OD(f"Put the steps in order to solve 3(x + 2) = {3*(x+2)}... wait", [], o="O1") if False else OD("Put the steps in order to solve (2x − 1)/3 = 5.", ["Multiply both sides by 3: 2x − 1 = 15", "Add 1 to both sides: 2x = 16", "Divide both sides by 2: x = 8"], o="O1", skill="Data")
s.core(e1(s.rng), e3(s.rng) or e1(s.rng), e4(s.rng), e5(s.rng) or e6(s.rng), e6(s.rng), e9(s.rng),
       TB("Complete the table: each equation's solution.", ["Equation", "x"], [["7x − 4 = 3x + 20", B(6)], ["2(x + 5) = 3(x − 1)", B(13)], ["x/4 + 3 = 8", B(20)]], o="O1", d="H"),
       EX("Jo solves 2(x + 3) = 14 and writes 2x + 3 = 14, x = 5.5. Explain her mistake and find the correct solution.", [("she did not multiply the 3 by 2 / expand both terms", ["3 by 2|2 × 3|both terms|6|expand"]), ("x = 4", ["x ?= ?4"])], "She only multiplied x by 2. It should be 2x + 6 = 14, so 2x = 8 and x = 4.", o="O1", d="H"))
s.gen("p", 44, e1, e2, e3, e4, e5, e6, e7, e8)
s.gen("a", 8, lambda r: (lambda x: N(f"Solve (2x + 1)/3 − (x − 2)/4 = {Fr(2*x+1,3) - Fr(x-2,4)}." if (Fr(2*x+1,3) - Fr(x-2,4)).denominator == 1 else f"Solve 2(3x − 1) − 3(x − 4) = {2*(3*x-1)-3*(x-4)}.", x, o="O1", d="VH"))(r.randint(-5, 20)),
      lambda r: (lambda x: N(f"Consecutive odd numbers: the sum of three consecutive odd numbers is {3*x+6}. Find the smallest.", x, o="O1", d="VH", reason="n + (n + 2) + (n + 4) = 3n + 6."))(r.randrange(5, 99, 2)))

# ================================================================== 4.2
s = U.section("4.2", "Simultaneous equations", ["O2"])
s.idea("Two equations, two unknowns", ["**Simultaneous equations** are two equations that are true at the same time. The solution is the pair (x, y) that fits both – it is where the two **lines cross**.",
       "**Substitution:** if one equation says y = …, put that expression into the other equation. **Elimination:** add or subtract the equations so that one unknown disappears."])
s.example("Substitution", "Solve y = 2x + 1 and 3x + y = 21.", [("3x + (2x + 1) = 21", "substitute"), ("5x = 20, x = 4", ""), ("y = 2 × 4 + 1 = 9", "")], "x = 4, y = 9")
s.check(TB("Solve y = x + 3 and y = 3x − 5.", ["x", "y"], [[B(4), B(7)]], o="O2", reason="x + 3 = 3x − 5 → x = 4, y = 7."))
s.example("Elimination", "Solve 3x + 2y = 16 and 5x − 2y = 8.", [("add: 8x = 24", "the y terms cancel"), ("x = 3", ""), ("3 × 3 + 2y = 16 → y = 3.5", "")], "x = 3, y = 3.5")
s.idea("Graphs", ["Draw both lines on the same grid. The coordinates of the crossing point are the solution."], fig={"kind": "coord", "x": [-1, 6], "y": [-1, 10], "lines": [{"m": 1, "c": 3, "label": "y = x + 3"}, {"m": 3, "c": -5, "label": "y = 3x − 5"}], "points": [{"x": 4, "y": 7, "l": "(4, 7)"}]})
s.mistake("Check in both", ["Always check your answer in BOTH original equations – if it only fits one, something went wrong."])
s.check(MC("The lines y = 2x and y = x + 4 cross at…", "(4, 8)", [("(2, 4)", "This is on y = 2x but not y = x + 4."), ("(4, 4)", ""), ("(8, 4)", "x comes first.")], o="O2", d="H"))
def sim(r):
    x, y = nz(r, -6, 9), nz(r, -6, 9)
    while True:
        a, b, c, d = nz(r, -5, 6), nz(r, -5, 6), nz(r, -5, 6), nz(r, -5, 6)
        if a * d - b * c: break
    return x, y, a, b, c, d
def eq(a, b, k): return f"{poly((a,'x'),(b,'y'))} = {fmt(k)}"
def s1(r):
    x, y, a, b, c, d = sim(r)
    return TB(f"Solve the simultaneous equations {eq(a,b,a*x+b*y)} and {eq(c,d,c*x+d*y)}.", ["x", "y"], [[B(x), B(y)]], o="O2", d="H", reason=f"Solution x = {x}, y = {y}. Check: {a*x+b*y} and {c*x+d*y} ✓.")
def s2(r):
    x, y = nz(r, -6, 8), nz(r, -6, 12); m = nz(r, -4, 4); c = y - m * x; p, q = nz(r, -4, 5), nz(r, -3, 4)
    return TB(f"Solve y = {lin(m, c)} and {eq(p, q, p*x+q*y)} by substitution.", ["x", "y"], [[B(x), B(y)]], o="O2", d="H") if p + q * m else None
def s3(r):
    x, y = r.randint(1, 9), r.randint(1, 9); a, b = r.randint(1, 5), r.randint(1, 5)
    return TB(f"Solve x + y = {x+y} and x − y = {x-y}.", ["x", "y"], [[B(x), B(y)]], o="O2", d="M", reason="Add the equations: 2x = …")
def s4(r):
    a, c = r.randint(2, 9), r.randint(2, 9); p1, p2 = r.randint(2, 6), r.randint(1, 5)
    if p1 == p2: return None
    n1, n2 = r.randint(2, 6), r.randint(2, 6)
    if n1 * p2 == n2 * p1: return None
    return TB(f"{n1} pens and {p1} pencils cost ${n1*a + p1*c}. {n2} pens and {p2} pencils cost ${n2*a + p2*c}. Find the cost of one pen and one pencil.", ["Pen ($)", "Pencil ($)"], [[B(a), B(c)]], o="O2", d="H", reason=f"Pen ${a}, pencil ${c}.")
def s5(r):
    m1, c1 = nz(r, -3, 3), r.randint(-4, 6); m2 = m1 + nz(r, -2, 2); x = r.randint(-2, 4); c2 = m1 * x + c1 - m2 * x; y = m1 * x + c1
    if abs(y) > 9 or abs(c2) > 12: return None
    return TB(f"The graph shows y = {lin(m1, c1)} and y = {lin(m2, c2)}. Use it to solve the equations.", ["x", "y"], [[B(x), B(y)]], o="O2", fig={"kind": "coord", "x": [-4, 6], "y": [-10, 10], "sy": 2, "lines": [{"m": m1, "c": c1}, {"m": m2, "c": c2}]}, reason=f"The lines cross at ({x}, {y}).")
def s6(r):
    x, y = r.randint(2, 9), r.randint(2, 9)
    return MC(f"Which pair of equations has the solution x = {x}, y = {y}?", f"x + y = {x+y} and 2x − y = {2*x-y}", [(f"x + y = {x+y} and 2x − y = {2*x-y+1}", ""), (f"x − y = {x+y} and 2x + y = {2*x-y}", ""), (f"x + 2y = {x+y} and x − y = {x-y}", "")], o="O2")
def s7(r):
    a, b = r.randint(10, 40), r.randint(10, 40); t = a + b; dif = abs(a - b)
    if a == b: return None
    return TB(f"Two numbers add to {t} and differ by {dif}. Find the larger and the smaller number.", ["Larger", "Smaller"], [[B(max(a, b)), B(min(a, b))]], o="O2", d="M")
s.core(s1(s.rng), s2(s.rng) or s3(s.rng), s3(s.rng), s4(s.rng) or s7(s.rng), s5(s.rng) or s5(s.rng) or s3(s.rng), s6(s.rng), s7(s.rng),
       EX("Explain how a graph can be used to solve the simultaneous equations y = 2x + 1 and y = 7 − x.", [("draw both lines on the same axes", ["draw|plot|both lines|same axes|graph"]), ("read the point where they cross / intersect", ["cross|intersect|meet"]), ("solution x = 2, y = 5", ["2.{0,10}5|\\(2, ?5\\)"])], "Draw both lines on the same axes. The point where they cross gives the solution; they meet at (2, 5), so x = 2 and y = 5.", o="O2", d="H"))
s.gen("p", 44, s1, s2, s3, s4, s5, s6, s7)
s.gen("a", 8, s1, lambda r: (lambda c, a: TB(f"Adult tickets cost ${a} and child tickets ${c}. 120 tickets were sold for ${a*70 + c*50}. How many of each were sold?", ["Adult", "Child"], [[B(70), B(50)]], o="O2", d="VH"))(r.randint(3, 8), r.randint(9, 15)))

# ================================================================== 4.3
s = U.section("4.3", "Inequalities", ["O3"])
s.idea("Inequality signs", ["< less than, ≤ less than or equal to, > greater than, ≥ greater than or equal to.",
       "On a number line, an **open circle** ○ means the end value is **not included** (< or >). A **filled circle** ● means it **is included** (≤ or ≥)."],
       fig={"kind": "numline", "min": -3, "max": 6, "from": {"v": -1, "closed": True}, "to": {"v": 4}})
s.example("Solving", "Solve 3x − 5 > 13.", [("3x > 18", "add 5"), ("x > 6", "divide by 3")], "x > 6")
s.check(N("x is an integer and 2x + 1 ≤ 15. What is the largest possible value of x?", 7, o="O3"))
s.idea("Multiplying by a negative", ["If you multiply or divide both sides by a **negative** number, **reverse the inequality sign**: −2x < 8 → x > −4."])
s.example("Double inequality", "List the integers n with −4 < 2n ≤ 6.", [("−2 < n ≤ 3", "divide every part by 2"), ("n = −1, 0, 1, 2, 3", "")], "−1, 0, 1, 2, 3")
s.mistake("The open circle", ["x > 2 does NOT include 2: draw an open circle at 2."])
s.check(MC("Solve −3x ≥ 12.", "x ≤ −4", [("x ≥ −4", "Dividing by −3 reverses the sign."), ("x ≤ 4", ""), ("x ≥ 4", "")], o="O3", d="H"))
def i1(r):
    a, b = r.randint(2, 9), r.randint(-20, 20); k = r.randint(-5, 12); c = a * k + b; sgn = pick(r, ["<", "≤", ">", "≥"])
    largest = sgn in "<≤"; ans = (k - 1 if sgn == "<" else k) if largest else (k + 1 if sgn == ">" else k)
    return N(f"x is an integer and {lin(a, b)} {sgn} {c}. Find the {'largest' if largest else 'smallest'} possible value of x.", ans, o="O3", reason=f"{a}x {sgn} {c - b} → x {sgn} {k}.")
def i2(r):
    lo, hi = r.randint(-6, 2), r.randint(3, 9); a = r.randint(2, 4)
    ints = [n for n in range(lo + 1, hi + 1)]
    return N(f"How many integers n satisfy {a*lo} < {a}n ≤ {a*hi}?", len(ints), o="O3", d="H", reason=f"{lo} < n ≤ {hi}: " + ", ".join(map(str, ints)) + ".")
def i3(r):
    v = r.randint(-3, 5); sgn = pick(r, ["<", "≤", ">", "≥"])
    lab = {"<": ("x <", False, "left"), "≤": ("x ≤", True, "left"), ">": ("x >", False, "right"), "≥": ("x ≥", True, "right")}[sgn]
    fig = {"kind": "numline", "min": -5, "max": 8, "from": None if lab[2] == "left" else {"v": v, "closed": lab[1]}, "to": {"v": v, "closed": lab[1]} if lab[2] == "left" else None}
    fig = {k: x for k, x in fig.items() if x is not None}
    opts = [f"x {o} {v}" for o in ["<", "≤", ">", "≥"]]
    return MC("Which inequality is shown on the number line?", f"x {sgn} {v}", [(o, "Check the circle (open or filled) and the direction.") for o in opts if o != f"x {sgn} {v}"], o="O3", fig=fig)
def i4(r):
    a = r.randint(2, 6); k = r.randint(-8, 8); b = r.randint(-10, 10)
    return MC(f"Solve {b} − {a}x < {b - a*k}.", f"x > {k}", [(f"x < {k}", f"Subtracting gives −{a}x < …; dividing by a negative reverses the sign."), (f"x > {-k}", ""), (f"x < {-k}", "")], o="O3", d="H")
def i5(r):
    lo, hi = r.randint(-5, 1), r.randint(2, 7)
    return TB(f"Write the smallest and largest integers that satisfy {lo} ≤ n < {hi}.", ["Smallest", "Largest"], [[B(lo), B(hi - 1)]], o="O3")
def i6(r):
    cost, budget = r.randint(3, 15), r.randint(40, 120); fee = r.randint(2, 12)
    return N(f"Tickets cost ${cost} each plus a ${fee} booking fee. Lan has ${budget}. Write and solve an inequality to find the greatest number of tickets she can buy.", (budget - fee) // cost, "tickets", units=["tickets", "$"], o="O3", d="H", reason=f"{cost}n + {fee} ≤ {budget} → n ≤ {(budget-fee)/cost:.2f} → {(budget-fee)//cost}.")
def i7(r):
    rows = [("x > 3", "Open circle at 3, arrow right"), ("x ≤ −1", "Filled circle at −1, arrow left"), ("x ≥ 0", "Filled circle at 0, arrow right"), ("x < 5", "Open circle at 5, arrow left")]
    return MT("Match each inequality to its number line.", rows, o="O3")
def i8(r):
    a = r.randint(2, 5); k = r.randint(1, 6); b = r.randint(1, 9)
    return N(f"Solve {a}(x − {b}) ≥ {a*(k-b)} + x and give the smallest integer x." if a > 1 else "", None, o="O3") if False else N(f"Solve {a}x + {b} ≥ x + {(a-1)*k + b}. What is the smallest possible integer value of x?", k, o="O3", d="H")
s.core(i1(s.rng), i2(s.rng), i3(s.rng), i4(s.rng), i5(s.rng), i6(s.rng), i7(s.rng),
       EX("Explain why 5 is not a solution of x < 5 but is a solution of x ≤ 5.", [("< means less than / does not include 5", ["less than|not included|not include|strictly"]), ("≤ includes 5 / equal to", ["equal|include"])], "x < 5 means x is less than 5, so 5 itself is not included. x ≤ 5 means less than OR equal to 5, so 5 is included.", o="O3"))
s.gen("p", 44, i1, i2, i3, i4, i5, i6, i7, i8)
s.gen("a", 8, lambda r: (lambda a, b: N(f"How many integers satisfy both 3x − 2 > {3*a-2} and 2x + 5 ≤ {2*b+5}?", max(0, b - a), o="O3", d="VH", reason=f"x > {a} and x ≤ {b}."))(r.randint(-4, 3), r.randint(4, 10)),
      lambda r: (lambda k: N(f"The sides of a triangle are x, x + 3 and {k} cm. The perimeter is less than {2*k+20} cm. Find the largest integer x.", max(x for x in range(1, 100) if 2 * x + 3 + k < 2 * k + 20), "cm", units=["cm"], o="O3", d="VH"))(r.randint(6, 20)))

U.mindmap(("Solving equations", "Same to both sides • expand brackets • clear fractions", "O1", "4.1"), ("Constructing", "Words or diagrams → equation", "O1", "4.1"),
          ("Simultaneous equations", "Substitution or elimination • lines cross at the solution", "O2", "4.2"), ("Inequalities", "○ not included, ● included • reverse the sign when × or ÷ by a negative", "O3", "4.3"))
