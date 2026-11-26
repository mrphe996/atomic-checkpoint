# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 9 Sequences and functions. Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from fractions import Fraction as Fr
from kit import *

U = Unit(9, "Sequences and Functions", "Algebra",
         "Generating linear and non-linear sequences, finding and using the nth term, and representing functions with machines, mappings and inverses.",
         {"O1": {"sec": "9.1", "code": "9As.01", "codeNote": "", "t": "Generate linear and quadratic sequences from term-to-term and position-to-term rules."},
          "O2": {"sec": "9.2", "code": "9As.02", "codeNote": "", "t": "Find and use the nth term of a linear sequence, and decide whether a number is in a sequence."},
          "O3": {"sec": "9.3", "code": "9As.03", "codeNote": "", "t": "Represent functions with function machines, mappings and algebra, and find inverse functions."}})

def seq(f, n=5, s0=1): return [f(k) for k in range(s0, s0 + n)]
def nth(a, b): return poly((a, "n"), (b, ""))

# ================================================================== 9.1
s = U.section("9.1", "Generating sequences", ["O1"])
s.idea("Two kinds of rule", ["A **term-to-term rule** tells you how to get from one term to the next, e.g. 'start at 5, add 3': 5, 8, 11, 14, …",
       "A **position-to-term rule** (the nth term) gives any term from its position n, e.g. Tₙ = 3n + 2 gives T₁ = 5, T₁₀ = 32.",
       "In a **quadratic** sequence, such as Tₙ = n² + 1 (2, 5, 10, 17, …), the differences change but the **second differences** are constant."])
s.example("From an nth term", "Write the first four terms of Tₙ = n² − 2n.", [("n = 1: 1 − 2 = −1", ""), ("n = 2: 4 − 4 = 0", ""), ("n = 3: 9 − 6 = 3", ""), ("n = 4: 16 − 8 = 8", "")], "−1, 0, 3, 8")
s.check(N("Tₙ = 4n − 7. Find the 20th term.", 73, reason="4 × 20 − 7 = 73.", o="O1"))
s.example("Second differences", "Find the next term of 3, 6, 11, 18, 27, …", [("differences 3, 5, 7, 9", ""), ("second differences 2", "the next difference is 11"), ("27 + 11 = 38", "")], "38")
s.mistake("Position or value?", ["In Tₙ = 2n + 1 the n is the POSITION. The 5th term is 2 × 5 + 1 = 11, not 2 × (the 4th term) + 1."])
s.check(MC("Which sequence is quadratic?", "1, 4, 9, 16, 25", [("2, 4, 6, 8, 10", "Constant difference: linear."), ("3, 6, 12, 24, 48", "Multiplied each time: geometric."), ("10, 7, 4, 1, −2", "")], o="O1"))
def g1(r):
    a, b = nz(r, -6, 9), r.randint(-15, 15); k = r.randint(10, 60)
    return N(f"The nth term of a sequence is {nth(a, b)}. Find the {k}th term.", a * k + b, reason=f"Substitute n = {k}: {a} × {k} + ({b}) = {a * k + b}.", o="O1")
def g2(r):
    a, c = r.choice([1, 1, 2, -1]), r.randint(-5, 6); b = r.randint(-4, 4); f = lambda n: a * n * n + b * n + c
    t = seq(f, 4)
    return TB(f"Write the first four terms of the sequence with nth term {poly((a,'n²'),(b,'n'),(c,''))}.", ["1st", "2nd", "3rd", "4th"], [[B(x) for x in t]], reason=f"Substitute n = 1, 2, 3, 4: {t[0]}, {t[1]}, {t[2]}, {t[3]}.", o="O1", d="H")
def g3(r):
    a, b = nz(r, 2, 8) * pick(r, [1, -1]), r.randint(-10, 30); t = seq(lambda n: a * n + b, 4)
    return N(f"A sequence starts {', '.join(fmt(x) for x in t)}, … Find the next term.", a * 5 + b, reason=f"The terms go up by {a} each time: {fmt(t[-1])} + {a} = {a * 5 + b}.", o="O1")
def g4(r):
    a, c = 1, r.randint(-5, 9); b = r.randint(-3, 4); t = seq(lambda n: a * n * n + b * n + c, 5)
    return N(f"Find the next term of the sequence {', '.join(fmt(x) for x in t)}, …", 36 + 6 * b + c, o="O1", d="H", reason="Second differences are 2; the next difference is 2 more than the last.")
def g5(r):
    st, m = r.randint(1, 5), pick(r, [2, 3, -2])
    t = [st * m ** k for k in range(5)]
    return N(f"A sequence starts at {st} and the rule is 'multiply by {fmt(m)}'. Find the 6th term.", st * m ** 5, reason=f"Multiply by {fmt(m)} five times: {st} × {fmt(m)}⁵ = {fmt(st * m ** 5)}.", o="O1")
def g6(r):
    rows = [("5, 9, 13, 17", "Linear"), ("2, 5, 10, 17", "Quadratic"), ("3, 6, 12, 24", "Geometric"), ("20, 14, 8, 2", "Linear"), ("0, 3, 8, 15", "Quadratic"), ("81, 27, 9, 3", "Geometric")]
    return GD("What type of sequence is each?", "Type", r.sample(rows, 4), o="O1")
def g7(r):
    st, d_ = r.randint(-10, 20), nz(r, -7, 9)
    return S(f"Write the term-to-term rule for {', '.join(fmt(st + d_ * k) for k in range(5))}, …", [f"add {d_}" if d_ > 0 else f"subtract {-d_}", f"+{d_}" if d_ > 0 else f"-{-d_}", f"/(add|plus|\\+) ?{d_}/" if d_ > 0 else f"/(subtract|minus|take away|-|−) ?{-d_}/"], o="O1")
def g8(r):
    k = r.randint(2, 6)
    return N(f"A pattern of squares: pattern n has n² + {k} squares. How many squares are in pattern 12?", 144 + k, "squares", units=["squares"], reason=f"12² + {k} = 144 + {k} = {144 + k}.", o="O1")
s.core(g1(s.rng), g2(s.rng), g3(s.rng), g4(s.rng), g5(s.rng), g6(s.rng), g7(s.rng),
       EX("Explain how you know 2, 6, 12, 20, 30, … is a quadratic sequence.", [("first differences 4, 6, 8, 10", ["4, ?6, ?8|differences increase|go up by 2"]), ("second differences are constant (2)", ["second difference|constant|always 2|same"])], "The first differences are 4, 6, 8, 10 and the second differences are all 2. Constant second differences show the sequence is quadratic.", o="O1", d="H"))
s.gen("p", 44, g1, g2, g3, g4, g5, g6, g7, g8)
s.gen("a", 8, lambda r: (lambda c: N(f"Tₙ = n² + {c}. Which term is the first to be more than 500?", next(n for n in range(1, 100) if n * n + c > 500), reason=f"Solve n² + ({c}) > 500: n² > {500 - c}, so the first whole n is {next(n for n in range(1, 100) if n * n + c > 500)}.", o="O1", d="VH"))(r.randint(-50, 80)),
      lambda r: (lambda a, b: N(f"Two sequences: Aₙ = {a}n + 1 and Bₙ = n² . For which positive n are they first equal or does B first overtake A? Give the smallest n with Bₙ > Aₙ.", next(n for n in range(1, 99) if n * n > a * n + 1), reason=f"Try values of n: the first n with n² > {a}n + 1.", o="O1", d="VH"))(r.randint(3, 15), 0))

# ================================================================== 9.2
s = U.section("9.2", "Using the nth term", ["O2"])
s.idea("Finding the nth term of a linear sequence", ["The **common difference** d gives the multiple of n. Then adjust: Tₙ = dn + (first term − d).",
       "For 7, 11, 15, 19: d = 4, so Tₙ = 4n + 3 (because 4 × 1 = 4 and we need 7)."], table={"caption": "7, 11, 15, 19", "head": ["n", "1", "2", "3", "4"], "rows": [["4n", "4", "8", "12", "16"], ["Tₙ", "7", "11", "15", "19"]]})
s.example("Decreasing", "Find the nth term of 20, 17, 14, 11, …", [("d = −3", ""), ("−3n: −3, −6, −9", ""), ("add 23", "−3 + 23 = 20"), ("Tₙ = 23 − 3n", "")], "23 − 3n")
s.check(X("Find the nth term of 5, 9, 13, 17, …", "4n+1", vars="n", o="O2", show="4n + 1"))
s.example("Is it in the sequence?", "Is 150 a term of Tₙ = 4n + 3?", [("4n + 3 = 150", ""), ("4n = 147, n = 36.75", ""), ("not a whole number", "")], "No, 150 is not a term.")
s.idea("Quadratic sequences", ["If the first differences are not equal but the second differences are, the sequence has an n² term. 2, 5, 10, 17, …: differences 3, 5, 7; second differences 2, 2. Compare with the square numbers 1, 4, 9, 16: every term is 1 more, so the nth term is n² + 1.",
       "For sequences of the form n² ± a, compare each term with the square numbers."])
s.mistake("Do not use the first term as the multiplier", ["For 7, 11, 15, … the nth term is 4n + 3, not 7n + 4. The difference goes with n."])
s.check(MC("Is 101 a term of the sequence 3n − 1?", "No, because 3n = 102 gives n = 34 — wait, that is whole, so yes" if False else "Yes, it is the 34th term", [("No, because 101 is odd", ""), ("Yes, it is the 33rd term", "Solve 3n − 1 = 101."), ("No, because 101 is prime", "")], o="O2", d="H"))
def n1(r):
    d_, b = nz(r, -9, 12), r.randint(-20, 20); t = [d_ * n + b for n in range(1, 5)]
    return X(f"Find the nth term of {', '.join(fmt(x) for x in t)}, …", f"{d_}n+({b})", vars="n", o="O2", show=nth(d_, b), reason=f"Difference {d_}; {d_} × 1 + ({b}) = {t[0]}.")
def n2(r):
    d_, b = nz(r, 2, 9), r.randint(-10, 15); v = r.randint(80, 400)
    ok = (v - b) % d_ == 0
    return MC(f"Is {v} a term of the sequence {nth(d_, b)}?", f"Yes, it is term {(v-b)//d_}" if ok else "No", [("No" if ok else f"Yes, it is term {(v-b)//d_}", f"Solve {nth(d_, b)} = {v}: n = {fmt((v-b)/d_)}.")], o="O2", d="H")
def n3(r):
    d_, b = nz(r, 2, 9), r.randint(-10, 15); v = r.randint(100, 900)
    k = next(n for n in range(1, 2000) if d_ * n + b > v)
    return N(f"Which is the first term of {nth(d_, b)} that is greater than {v}? Give its position n.", k, reason=f"{nth(d_, b)} > {v} gives n > {fmt((v - b) / d_)}, so n = {k}.", o="O2", d="H")
def n4(r):
    d_, b = nz(r, 2, 6), r.randint(-3, 6)
    return X(f"Pattern n is made of {d_}n + {b} sticks... Pattern 1 has {d_+b} sticks, pattern 2 has {2*d_+b}, pattern 3 has {3*d_+b}. Write an expression for the number of sticks in pattern n." if b >= 0 else f"Pattern 1 has {d_+b} tiles, pattern 2 has {2*d_+b}, pattern 3 has {3*d_+b}. Write an expression for the number of tiles in pattern n.", f"{d_}n+({b})", vars="n", o="O2", show=nth(d_, b), data={"head": ["Pattern", "1", "2", "3"], "rows": [["Number", str(d_ + b), str(2 * d_ + b), str(3 * d_ + b)]]})
def n5(r):
    d_, b = nz(r, -8, 9), r.randint(-20, 20)
    return TB(f"The nth term is {nth(d_, b)}. Complete the table.", ["n", "1", "5", "10", B((60 - b) / d_) if (60 - b) % d_ == 0 else "100"], [["Tₙ", B(d_ + b), B(5 * d_ + b), B(10 * d_ + b), "60" if (60 - b) % d_ == 0 else B(100 * d_ + b)]], reason=f"Substitute each n into {nth(d_, b)}; for Tₙ = 60 solve {nth(d_, b)} = 60.", o="O2")
def n6(r):
    d_, b = nz(r, 2, 9), r.randint(-10, 10); t = [d_ * n + b for n in range(1, 5)]
    return MC(f"Which is the nth term of {', '.join(fmt(x) for x in t)}, …?", nth(d_, b), [(nth(t[0], d_), "The difference goes with n."), (nth(d_, -b), ""), (nth(d_ + 1, b - 1), "")], o="O2")
def n7(r):
    d1, b1, d2, b2 = r.randint(2, 7), r.randint(-5, 10), r.randint(2, 7), r.randint(-5, 10)
    if d1 == d2: return None
    n = (b2 - b1) / (d1 - d2)
    if n != int(n) or n < 1: return None
    return N(f"For which n do the sequences {nth(d1, b1)} and {nth(d2, b2)} have the same term?", int(n), reason=f"{nth(d1, b1)} = {nth(d2, b2)} gives {d1 - d2}n = {b2 - b1}, so n = {int(n)}.", o="O2", d="VH")
s.core(n1(s.rng), n2(s.rng), n3(s.rng), n4(s.rng), n5(s.rng), n6(s.rng), n1(s.rng),
       EX("Explain why the nth term of 6, 10, 14, 18, … is 4n + 2 and not 6n + 4.", [("difference is 4 so 4n", ["difference|goes up by 4|adds 4|4n"]), ("4 × 1 + 2 = 6", ["4 ?(×|x) ?1|\\+ ?2|first term"]), ("6n + 4 gives 10 for n = 1", ["10|does not|doesn't|wrong"])], "The terms go up by 4, so the nth term starts 4n. When n = 1, 4n = 4 and we need 6, so add 2: 4n + 2. 6n + 4 would give 10 for the first term.", o="O2", d="H"))
def i2_1(r):
    a, c = 1, r.randint(-3, 9)   # Stage 9 framework: n² ± a
    seq = [a * n * n + c for n in range(1, 5)]
    return MC(f"What is the nth term of {', '.join(map(str, seq))}, …?", f"{'' if a == 1 else a}n² {'+' if c >= 0 else '−'} {abs(c)}", [(f"{2 * a}n² {'+' if c >= 0 else '−'} {abs(c)}", "The coefficient of n² is HALF the second difference."), (f"{seq[1] - seq[0]}n {'+' if seq[0] - (seq[1] - seq[0]) >= 0 else '−'} {abs(seq[0] - (seq[1] - seq[0]))}", "The first differences are not constant, so it is not linear.")], o="O2", d="VH",
              reason=f"Second differences are {2 * a}, so {a}n²; then add {c}.")


s.gen("p", 44, n1, n2, n3, n4, n5, n6, n7)
s.capped("p", [1] * 1, [i2_1]).capped("m", [2] * 1, [i2_1])   # v2 reasoning kinds
s.gen("a", 8, n7, n3, lambda r: (lambda d_, b: X(f"The 5th term of a linear sequence is {5*d_+b} and the 12th term is {12*d_+b}. Find the nth term.", f"{d_}n+({b})", vars="n", reason=f"7 steps from the 5th to the 12th term add {7 * d_}, so d = {d_}; then {5 * d_ + b} − 5 × {d_} = {b}.", o="O2", d="VH", show=nth(d_, b)))(nz(r, -6, 9), r.randint(-20, 20)))

# ================================================================== 9.3
s = U.section("9.3", "Representing functions", ["O3"])
s.idea("Functions", ["A **function** turns each input x into exactly one output y. It can be shown as a **function machine**, a **mapping** x → 3x − 1, an **equation** y = 3x − 1 or a table.",
       "The **inverse function** undoes it: do the inverse operations in **reverse order**. The inverse of x → 3x − 1 is x → (x + 1)/3."])
s.example("Inverse", "Find the inverse of x → (x + 4)/5.", [("machine: + 4, then ÷ 5", ""), ("inverse: × 5, then − 4", "reverse order"), ("x → 5x − 4", "")], "x → 5x − 4")
s.check(N("The function is x → 2x² − 3. Find the output when the input is −4.", 29, reason="2 × (−4)² − 3 = 2 × 16 − 3 = 29.", o="O3"))
s.example("Finding the rule from a table", "Inputs 1, 2, 3, 4 give outputs 5, 8, 11, 14. Find the function.", [("outputs go up by 3", "so 3x"), ("3 × 1 = 3, need 5: + 2", ""), ("x → 3x + 2", "")], "x → 3x + 2")
s.mistake("Reverse the order", ["For x → 2x + 6 the inverse is NOT x → x/2 − 6. Undo the LAST step first: x → (x − 6)/2."])
s.check(X("Find the inverse of x → 4x + 1. Write the output in terms of x.", "(x-1)/4", o="O3", show="(x − 1)/4", d="H"))
def f1(r):
    a, b = nz(r, -6, 7), r.randint(-10, 10); x = r.randint(-6, 9)
    return N(f"The function is x → {lin(a, b)}. Find the output when the input is {x}.", a * x + b, reason=f"{a} × {x} + ({b}) = {a * x + b}.", o="O3")
def lin(a, b): return poly((a, "x"), (b, ""))
def f2(r):
    a, b = nz(r, 2, 7), r.randint(-10, 10); y = a * r.randint(-6, 9) + b
    return N(f"The function is x → {lin(a, b)}. Find the input that gives the output {y}.", (y - b) / a, reason=f"Work backwards: ({y} − ({b})) ÷ {a} = {fmt((y - b) / a)}.", o="O3", d="H")
def f3(r):
    a, b = nz(r, 2, 7), r.randint(-10, 10)
    return X(f"Find the inverse of the function x → {lin(a, b)}.", f"(x-({b}))/{a}", reason=f"Reverse the steps: {'subtract' if b >= 0 else 'add'} {abs(b)}, then divide by {a}.", o="O3", d="H", show=f"(x {'−' if b >= 0 else '+'} {abs(b)})/{a}" if b else f"x/{a}")
def f4(r):
    a, b = nz(r, 2, 6), r.randint(-6, 8); xs = [1, 2, 3, 4]
    return X(f"A function maps 1 → {a+b}, 2 → {2*a+b}, 3 → {3*a+b}, 4 → {4*a+b}. Find the function: x → ?", f"{a}x+({b})", reason=f"The output goes up by {a} each time, so {a}x; then 1 → {a + b} means + ({b}).", o="O3", show=lin(a, b), data={"head": ["x", "1", "2", "3", "4"], "rows": [["y", str(a + b), str(2 * a + b), str(3 * a + b), str(4 * a + b)]]})
def f5(r):
    a, b = r.randint(2, 6), r.randint(1, 9)
    return X(f"A function machine does '+ {b}' then '× {a}'. Write the function as x → ?", f"{a}(x+{b})", reason=f"Add {b} first, then multiply the whole by {a}: {a}(x + {b}).", o="O3", show=f"{a}(x + {b})")
def f6(r):
    a, c = r.randint(1, 3), r.randint(-6, 6); xs = r.sample(range(-3, 5), 3)
    return TB(f"Complete the table for y = {a}x² {'+ ' + str(c) if c >= 0 else '− ' + str(-c)}.", ["x"] + [str(x) for x in xs], [["y"] + [B(a * x * x + c) for x in xs]], reason=f"Square x first, then × {a}, then {'+ ' + str(c) if c >= 0 else '− ' + str(-c)}.", o="O3")
def f7(r):
    a, b = r.randint(2, 6), r.randint(1, 9)
    return OD(f"Put the steps of the inverse of x → {a}x + {b} in order.", [f"Start with the output", f"Subtract {b}", f"Divide by {a}"], o="O3", skill="Data")
def f8(r):
    a, b = r.randint(2, 5), r.randint(1, 9); x = r.randint(1, 9); y = a * x + b
    return MC(f"f(x) = {a}x + {b}. Which statement is true?", f"the inverse maps {y} to {x}", [(f"the inverse maps {x} to {y}", ""), (f"f maps {y} to {x}", ""), (f"the inverse is x → {a}x − {b}", "Undo ×, then −: reverse order.")], o="O3", d="H")
s.core(f1(s.rng), f2(s.rng), f3(s.rng), f4(s.rng), f5(s.rng), f6(s.rng), f8(s.rng),
       EX("Explain how to check that x → (x − 3)/2 is the inverse of x → 2x + 3.", [("put a value through the function", ["value|number|e\\.g|for example|input"]), ("then the inverse gives back the start number", ["back|original|start|same number|undo"])], "Choose an input, e.g. 5: 2 × 5 + 3 = 13. Then (13 − 3)/2 = 5. The inverse gives back the starting number, so it undoes the function.", o="O3"))
s.gen("p", 44, f1, f2, f3, f4, f5, f6, f7, f8)
s.gen("a", 8, f3, lambda r: (lambda a, b: X(f"Find the inverse of x → {a}(x − {b}) + 1.", f"(x-1)/{a}+{b}", reason=f"Reverse: subtract 1, divide by {a}, add {b}.", o="O3", d="VH", show=f"(x − 1)/{a} + {b}"))(r.randint(2, 6), r.randint(1, 9)))

U.mindmap(("Term-to-term", "Rule from one term to the next", "O1", "9.1"), ("Quadratic sequences", "Constant second differences", "O1", "9.1"),
          ("nth term", "dn + (first term − d)", "O2", "9.2"), ("Functions", "Machines, mappings, tables", "O3", "9.3"), ("Inverses", "Inverse operations in reverse order", "O3", "9.3"))
