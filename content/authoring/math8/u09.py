# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 9 Sequences and functions (9.1 Generating sequences, 9.2 Finding rules for sequences,
9.3 Using the nth term, 9.4 Representing simple functions). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *

U = Unit(9, "Sequences and Functions", "Algebra",
         "Term-to-term and position-to-term rules, finding and using the nth term of a linear sequence, and function machines and mappings.",
         {"O1": {"code": "8As.01", "sec": "9.1", "codeNote": "", "t": "Generate sequences from term-to-term and position-to-term rules, including non-linear sequences."},
          "O2": {"code": "8As.02", "sec": "9.2", "codeNote": "", "t": "Find term-to-term rules and recognise linear and non-linear sequences from patterns and diagrams."},
          "O3": {"code": "8As.03", "sec": "9.3", "codeNote": "", "t": "Find and use the nth term of a linear sequence."},
          "O4": {"code": "8As.04", "sec": "9.4", "codeNote": "", "t": "Represent simple functions with function machines, mappings and equations, and find inverses."}})
lin = lambda a, b: f"{'' if a == 1 else a}n {'+' if b >= 0 else '−'} {abs(b)}" if b else f"{a}n"


def seq(a, b, k=5): return [a * n + b for n in range(1, k + 1)]


# ================================================================== 9.1
s = U.section("9.1", "Generating sequences", ["O1"])
s.idea("Two kinds of rule", ["A **term-to-term rule** tells you how to get from one term to the next: 'start at 5, add 3' gives 5, 8, 11, 14, …",
       "A **position-to-term rule** uses the position n: '3n + 2' gives 5, 8, 11, 14, … (n = 1, 2, 3, 4).",
       "Sequences can also multiply (2, 6, 18, 54, …) or use squares (1, 4, 9, 16, …): these are **non-linear**."])
s.check(N("The first term of a sequence is 4. The rule is 'multiply by 3, then subtract 2'. What is the third term?", 28, o="O1", reason="4 → 10 → 28."))
s.example("Position-to-term", "Write the first three terms of the sequence with nth term 5n − 3.", [("n = 1: 5 − 3 = 2", ""), ("n = 2: 10 − 3 = 7", ""), ("n = 3: 15 − 3 = 12", "")], "2, 7, 12")
s.check(MC("Before you read on: a sequence has term-to-term rule 'multiply by 2, then subtract 1' and first term 3. What is the third term?", "9", [("5", "That is the second term."), ("11", "3 → 5 → 9.")], o="O1"))
s.mistake("Start at n = 1", ["The first term uses n = 1, not n = 0."])


def g1(r):
    a, d = r.randint(-10, 20), nz(r, -7, 9); k = r.randint(4, 7)
    rule = f"add {d}" if d > 0 else f"subtract {-d}"
    return N(f"A sequence starts at {a}. The term-to-term rule is '{rule}'. What is term {k}?", a + (k - 1) * d, o="O1", reason=f"{a} + {k - 1} × {d} = {a + (k - 1) * d}.")
def g2(r):
    a, b = r.randint(2, 9), r.randint(-6, 10); n = r.randint(5, 30)
    return N(f"Find the {n}th term of the sequence with nth term {lin(a, b)}.", a * n + b, o="O1", reason=f"{a} × {n} {'+' if b >= 0 else '−'} {abs(b)} = {a * n + b}.")
def g3(r):
    a, b = r.randint(2, 9), r.randint(-6, 10)
    return TB(f"Complete the table for the sequence with nth term {lin(a, b)}.", ["n", "Term"], [[str(n), B(a * n + b)] for n in (1, 2, 3, 10)], o="O1")
def g4(r):
    a, m = r.randint(1, 5), r.randint(2, 4)
    return N(f"A sequence starts at {a}. The rule is 'multiply by {m}'. What is the 4th term?", a * m ** 3, o="O1", reason=f"{a} → {a * m} → {a * m * m} → {a * m ** 3}.")
def g5(r):
    a, m, c = r.randint(1, 6), r.randint(2, 3), r.randint(1, 5)
    t = [a]
    for _ in range(3): t.append(t[-1] * m - c)
    return N(f"The first term of a sequence is {a}. The rule is 'multiply by {m}, then subtract {c}'. What is the 4th term?", t[3], o="O1", d="H", reason=" → ".join(map(str, t)) + ".")
def g6(r):
    k = r.randint(5, 12)
    return N(f"Find the {k}th term of the sequence with nth term n² + 1.", k * k + 1, o="O1", reason=f"{k}² + 1 = {k * k + 1}.")
def g7(r):
    a, b = r.randint(2, 6), r.randint(-5, 8)
    t = seq(a, b, 4)
    return MC(f"Which sequence has nth term {lin(a, b)}?", ", ".join(map(str, t)), [", ".join(map(str, seq(a, b + a, 4))), ", ".join(map(str, seq(b, a, 4))) if b > 0 else ", ".join(map(str, seq(a + 1, b, 4))), ", ".join(map(str, seq(a, b - 1, 4)))], o="O1")
def g8(r):
    rows = [("2, 5, 8, 11", "Linear"), ("1, 4, 9, 16", "Non-linear"), ("3, 6, 12, 24", "Non-linear"), ("20, 16, 12, 8", "Linear"), ("1, 3, 6, 10", "Non-linear"), ("−5, −2, 1, 4", "Linear")]
    return GD("Is each sequence linear or non-linear?", "Type", r.sample(rows, 4), o="O1")


def e91(r):
    a, d = r.randint(2, 9), r.randint(2, 5)
    return MC(f"A sequence starts {a} and the rule is 'add {d}'. Will every term be odd?", "Sometimes – it depends on a and d" if False else ("Yes" if a % 2 and d % 2 == 0 else "No"), [("No" if a % 2 and d % 2 == 0 else "Yes", f"Write out a few terms: {a}, {a + d}, {a + 2 * d}, …"), ("You cannot tell", "Look at whether you start odd and add an even number.")], o="O1", d="H",
              reason=f"{a}, {a + d}, {a + 2 * d}, {a + 3 * d}: " + ("adding an even number to an odd number keeps it odd." if a % 2 and d % 2 == 0 else "the parity changes or starts even."))


s.std([g3, g8, g1, g2, g4, g6, g7, g5], EX("Explain the difference between a term-to-term rule and a position-to-term rule.", [("term-to-term: from one term to the next", ["next|previous|one term to"]), ("position-to-term: uses the position n to find any term directly", ["position|n|directly|any term"])], "A term-to-term rule tells you how to get from one term to the next. A position-to-term rule uses the term's position n, so you can find any term directly.", o="O1"),
      deep=[e91])

# ================================================================== 9.2
s = U.section("9.2", "Finding rules for sequences", ["O2"])
s.idea("Differences", ["Find the **difference** between terms. If it is always the same, the sequence is **linear**: 7, 11, 15, 19 has difference +4.",
       "Patterns of shapes often make sequences: count the matchsticks or tiles in each pattern number."])
s.check(S("Write the term-to-term rule for 23, 18, 13, 8, …", ["subtract 5", "minus 5", "−5", "-5", "take away 5"], o="O2"))
s.idea("Why the nth term starts with the difference", ["In 5, 8, 11, 14, … each term is 3 more than the last, so the sequence grows like the 3 times table: 3n gives 3, 6, 9, 12. Each term is 2 more than 3n, so the nth term is 3n + 2.",
       "Check with n = 1: 3 × 1 + 2 = 5 ✓."])
s.mistake("Check every gap", ["2, 4, 8, 14 does not have a constant difference (2, 4, 6), so it is not linear."])


def f1(r):
    a, d = r.randint(-5, 20), nz(r, -8, 9); t = [a + i * d for i in range(5)]
    return N(f"What is the next term of the sequence {', '.join(map(str, t[:4]))}, …?", t[4], o="O2", reason=f"The difference is {d:+d}.")
def f2(r):
    a, d = r.randint(-5, 20), nz(r, -8, 9); t = [a + i * d for i in range(4)]
    return N(f"What is the common difference of {', '.join(map(str, t))}, …?", d, o="O2", reason=f"{t[1]} − {t[0]} = {d}.")
def f3(r):
    a, d = r.randint(3, 6), r.randint(2, 4)
    t = [a + i * d for i in range(4)]
    return N("Matchstick patterns: pattern 1 uses " + str(t[0]) + ", pattern 2 uses " + str(t[1]) + " and pattern 3 uses " + str(t[2]) + " matchsticks. How many matchsticks are in pattern 6?", a + 5 * d, "matchsticks", units=["matchsticks"], o="O2", data={"head": ["Pattern", "1", "2", "3"], "rows": [["Matchsticks", *map(str, t[:3])]]}, reason=f"Add {d} each time: {a + 5 * d}.")
def f4(r):
    a = r.randint(1, 5); t = [a + i * i for i in range(1, 6)]
    return N(f"Find the next term: {', '.join(map(str, t[:4]))}, …", t[4], o="O2", d="H", reason=f"The differences are {', '.join(str(t[i + 1] - t[i]) for i in range(3))}: they go up by 2. Next difference {t[4] - t[3]}.")
def f5(r):
    a, m = r.randint(1, 5), r.randint(2, 3); t = [a * m ** i for i in range(5)]
    return S(f"Write the term-to-term rule for {', '.join(map(str, t[:4]))}, …", [f"multiply by {m}", f"times {m}", f"× {m}", f"×{m}", f"x{m}", f"x {m}", f"double" if m == 2 else f"triple"], o="O2", reason=f"Each term is {m} times the one before.")
def f6(r):
    a, d = r.randint(-5, 20), nz(r, -8, 9); t = [a + i * d for i in range(6)]; k = r.randint(1, 4)
    shown = [str(x) if i != k else "☐" for i, x in enumerate(t[:5])]
    return N(f"Find the missing term: {', '.join(shown)}", t[k], o="O2", reason=f"The difference is {d:+d}.")
def f7(r):
    a, d = r.randint(1, 10), r.randint(2, 6); t = [a + i * d for i in range(4)]
    return TB("Continue the pattern of tiles.", ["Pattern", "Tiles"], [["4", str(t[3])], ["5", B(t[3] + d)], ["6", B(t[3] + 2 * d)]], o="O2", data={"head": ["Pattern", "1", "2", "3"], "rows": [["Tiles", *map(str, t[:3])]]})
def f8(r):
    a, d = r.randint(2, 20), r.randint(2, 9); t = [a + i * d for i in range(4)]; v = a + r.randint(6, 30) * d + pick(r, [0, 1])
    yes = (v - a) % d == 0
    return MC(f"Is {v} a term of the sequence {', '.join(map(str, t))}, …?", "Yes" if yes else "No", [("No" if yes else "Yes", ""), ("It cannot be decided", "")], o="O2", d="H", reason=f"Terms are {a} + a multiple of {d}. {v} − {a} = {v - a}, which is {'' if yes else 'not '}a multiple of {d}.")


def e92(r):
    a, b = r.randint(2, 7), r.randint(-6, 9)
    seq = [a * n + b for n in range(1, 5)]
    return MC(f"Which is the nth term of {', '.join(map(str, seq))}, …?", lin(a, b), [(lin(a + 1, b - 1) if a + 1 != a else lin(a, b + 1), "Check n = 2."), (lin(b if b > 0 else 1, a), "The difference goes in front of n.")], o="O2", d="H",
              reason=f"The difference is {a}, so {a}n; {a}n gives {a}, {2 * a}, …; add {b}.") if lin(b if b > 0 else 1, a) != lin(a, b) and lin(a + 1, b - 1) != lin(a, b) else None


s.std([f3, f7, f1, f2, f5, f6, f4, f8], EX("Explain how you know that 3, 7, 11, 15, … is a linear sequence.", [("the difference is always 4", ["4|same difference|constant|common difference"]), ("a constant difference means linear", ["constant|same.*each time|linear"])], "The difference between consecutive terms is always +4. A constant difference means the sequence is linear.", o="O2"),
      deep=[e92])

# ================================================================== 9.3
s = U.section("9.3", "Using the nth term", ["O3"])
s.idea("Finding the nth term", ["For a linear sequence, the **difference** tells you the number in front of n.",
       "7, 11, 15, 19: difference 4 → 4n. 4n gives 4, 8, 12, … — each term is 3 more, so the nth term is **4n + 3**."])
s.example("Decreasing", "Find the nth term of 20, 17, 14, 11, …", [("difference −3 → −3n", ""), ("−3n gives −3, −6, −9; add 23", ""), ("nth term = 23 − 3n", "")], "23 − 3n")
s.check(X("Find the nth term of 5, 9, 13, 17, …", "4n+1", vars="n", o="O3"))
s.check(MC("Before you read on: is 100 a term of the sequence 3n + 1?", "Yes – n = 33", [("No", "Solve 3n + 1 = 100: n = 33, a whole number."), ("Yes – n = 100", "Substitute: 3 × 100 + 1 = 301.")], o="O3"))
s.mistake("Not n + 4", ["For 5, 9, 13 the difference 4 goes in FRONT of n: 4n + 1, not n + 4."])


def n1(r):
    a, b = r.randint(2, 9), r.randint(-8, 10); t = seq(a, b, 4)
    return X(f"Find the nth term of {', '.join(map(str, t))}, …", f"{a}n+({b})", vars="n", o="O3", show=lin(a, b), reason=f"Difference {a} → {a}n; adjust by {b:+d}.")
def n2(r):
    a, b = r.randint(2, 6), r.randint(20, 40); t = [b - a * n for n in range(1, 5)]
    return X(f"Find the nth term of {', '.join(map(str, t))}, …", f"{b}-{a}n", vars="n", o="O3", d="H", reason=f"Difference −{a} → −{a}n; first term {b - a} → {b} − {a}n.")
def n3(r):
    a, b = r.randint(2, 9), r.randint(-5, 10); k = r.randint(8, 25); v = a * k + b
    return N(f"Which term of the sequence {lin(a, b)} is equal to {v}?", k, o="O3", d="H", reason=f"{lin(a, b)} = {v} → n = {k}.")
def n4(r):
    a, b = r.randint(2, 9), r.randint(-5, 10)
    t = seq(a, b, 4)
    return MC(f"What is the nth term of {', '.join(map(str, t))}, …?", lin(a, b), [lin(1, a) if a != b else lin(1, a + 1), lin(a, b + a), lin(a + 1, b - 1)], o="O3")
def n5(r):
    a, b = r.randint(2, 6), r.randint(1, 4)
    t = seq(a, b, 3)
    return X(f"Squares are joined in a row. 1 square uses {t[0]} sticks, 2 squares use {t[1]}, 3 squares use {t[2]}. Write an expression for the number of sticks for n squares.", f"{a}n+{b}", vars="n", o="O3", data={"head": ["Squares", "1", "2", "3"], "rows": [["Sticks", *map(str, t)]]}, show=lin(a, b))
def n6(r):
    a, b = r.randint(2, 9), r.randint(-5, 10)
    return TB(f"The nth term of a sequence is {lin(a, b)}. Complete the table.", ["n", "Term"], [["1", B(a + b)], ["5", B(5 * a + b)], ["20", B(20 * a + b)]], o="O3")
def n7(r):
    a, b = r.randint(2, 9), r.randint(1, 10); v = r.randint(60, 200)
    k = (v - b) // a
    return N(f"A sequence has nth term {lin(a, b)}. What is the largest term that is less than {v}?", a * k + b if a * k + b < v else a * (k - 1) + b, o="O3", d="VH", reason=f"Solve {lin(a, b)} < {v}.")
def n8(r):
    a, b = r.randint(2, 9), r.randint(-5, 10)
    return N(f"A sequence has nth term {lin(a, b)}. What is the difference between the 10th and 11th terms?", a, o="O3", reason=f"Consecutive terms differ by {a}.")


def e93(r):
    a, b = r.randint(3, 8), r.randint(1, 9); t = a * r.randint(10, 30) + b + r.choice([0, 1, 2])
    ok = (t - b) % a == 0
    return MC(f"Is {t} a term of the sequence with nth term {lin(a, b)}?", "Yes" if ok else "No", [("No" if ok else "Yes", f"Solve {lin(a, b)} = {t}.")], o="O3", d="H", reason=f"n = ({t} − {b}) ÷ {a} = {(t - b) / a:g}" + (", a whole number." if ok else ", not a whole number."))


s.std([n5, n6, n1, n2, n3, n4, n8, n7], EX("Explain why the nth term of 6, 11, 16, 21, … is 5n + 1.", [("the difference is 5, so 5n", ["difference.*5|5n|goes up by 5"]), ("5n gives 5, 10, 15 … each 1 less, so add 1", ["\\+ ?1|add 1|one more|1 more"])], "The terms go up by 5, so the nth term starts with 5n. 5n gives 5, 10, 15, 20, which are each 1 less than the sequence, so the nth term is 5n + 1.", o="O3"),
      deep=[e93])

# ================================================================== 9.4
s = U.section("9.4", "Representing simple functions", ["O4"])
s.idea("Function machines", ["A **function** turns each input into exactly one output: x → × 3 → + 2 → y, so y = 3x + 2.",
       "A **mapping** x → 3x + 2 shows the same thing. To find an input from an output, use the **inverse**: undo the operations in reverse order (− 2, then ÷ 3)."])
s.example("Inverse", "The function is y = 4x − 5. Find x when y = 23.", [("+ 5: 28", "undo − 5"), ("÷ 4: 7", "undo × 4")], "x = 7")
s.check(N("x → × 5 → − 1 → y. Find y when x = 6.", 29, o="O4"))
s.check(MC("Before you read on: the inverse of 'multiply by 4 then add 3' is…", "subtract 3 then divide by 4", [("divide by 4 then subtract 3", "Undo in reverse order: the last step first."), ("add 3 then multiply by 4", "That is the same machine.")], o="O4"))
s.mistake("Reverse order", ["For the inverse of 'multiply by 2, then add 3', subtract 3 FIRST, then divide by 2."])


def m1(r):
    a, b, x = r.randint(2, 9), nz(r, -9, 12), r.randint(-4, 10)
    return N(f"A function machine is: input → × {a} → {'+' if b > 0 else '−'} {abs(b)} → output. Find the output when the input is {x}.", a * x + b, o="O4", reason=f"{x} × {a} {'+' if b > 0 else '−'} {abs(b)} = {a * x + b}.")
def m2(r):
    a, b, x = r.randint(2, 9), r.randint(1, 15), r.randint(1, 12)
    return N(f"A function machine is: input → × {a} → + {b} → output. The output is {a * x + b}. What was the input?", x, o="O4", reason=f"({a * x + b} − {b}) ÷ {a} = {x}.")
def m3(r):
    a, b = r.randint(2, 9), r.randint(-9, 12); xs = r.sample(range(-3, 8), 3)
    return TB(f"Complete the table for y = {a}x {'+' if b >= 0 else '−'} {abs(b)}.", ["x", "y"], [[str(x), B(a * x + b)] for x in sorted(xs)], o="O4")
def m4(r):
    a, b = r.randint(2, 9), r.randint(1, 12)
    return X(f"Write the function x → × {a} → + {b} → y as an equation for y.", f"{a}x+{b}", vars="xy", lhs="y", o="O4", reason=f"y = {a}x + {b}.")
def m5(r):
    a, b = r.randint(2, 9), r.randint(1, 12)
    return MC(f"What is the inverse of the function x → × {a} → + {b}?", f"− {b}, then ÷ {a}", [f"÷ {a}, then − {b}", f"− {a}, then ÷ {b}", f"× {a}, then − {b}"], o="O4")
def m6(r):
    a, b = r.randint(2, 6), r.randint(1, 9); pairs = [(x, a * x + b) for x in r.sample(range(1, 9), 3)]
    return X(f"A function maps {', '.join(f'{x} → {y}' for x, y in pairs)}. Write the function as y = …", f"{a}x+{b}", vars="xy", lhs="y", o="O4", d="H", data={"head": ["Input", *[str(x) for x, _ in pairs]], "rows": [["Output", *[str(y) for _, y in pairs]]]})
def m7(r):
    a, b = r.randint(2, 9), r.randint(1, 12)
    return X(f"Find the inverse of y = {a}x + {b}. Write it as x = …", f"(y-{b})/{a}", vars="xy", lhs="x", o="O4", d="H")
def m8(r):
    a, x = r.randint(2, 5), r.randint(2, 9)
    return N(f"A function machine is: input → square → × {a} → output. Find the output when the input is {x}.", a * x * x, o="O4", reason=f"{x}² × {a} = {a * x * x}.")


def e94(r):
    a, b = r.randint(2, 6), r.randint(1, 9); y = a * r.randint(2, 9) + b
    return N(f"A function is x → {a}x + {b}. Which input gives the output {y}?", (y - b) // a, o="O4", d="H", reason=f"Inverse: ({y} − {b}) ÷ {a} = {(y - b) // a}.")


s.std([m3, m6, m1, m2, m4, m5, m8, m7], EX("Explain how to find the input of the function y = 3x − 4 when the output is 11.", [("work backwards / use the inverse: add 4, then divide by 3", ["inverse|backwards|add 4|\\+ ?4|divide by 3|÷ ?3"]), ("(11 + 4) ÷ 3 = 5", ["\\b5\\b|15"])], "Use the inverse function: add 4, then divide by 3. (11 + 4) ÷ 3 = 15 ÷ 3 = 5.", o="O4"),
      deep=[e94])

U.mindmap(("Generating sequences", "Term-to-term • position-to-term • linear and non-linear", "O1", "9.1"), ("Finding rules", "Constant difference → linear • patterns", "O2", "9.2"),
          ("nth term", "Difference in front of n, then adjust", "O3", "9.3"), ("Functions", "Function machines • mappings • inverse: undo in reverse", "O4", "9.4"))
