# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 9 Sequences and functions (9.1 Generating sequences (1), 9.2 Generating sequences (2),
9.3 Using the nth term, 9.4 Representing simple functions). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Atomic teaching team."""
from kit import *

U = Unit(9, "Sequences and Functions", "Algebra",
         "Term-to-term rules, sequences from patterns, finding terms from a position-to-term rule, and function machines.",
         {"O1": {"code": "7As.01", "sec": "9.1", "codeNote": "", "t": "Generate sequences from a first term and a term-to-term rule, and find missing terms."},
          "O2": {"code": "7As.02", "sec": "9.2", "codeNote": "", "t": "Recognise and extend sequences from spatial patterns and say whether they are linear."},
          "O3": {"code": "7As.03", "sec": "9.3", "codeNote": "", "t": "Use a position-to-term rule (nth term) to generate terms of a sequence."},
          "O4": {"code": "7As.04", "sec": "9.4", "codeNote": "", "t": "Use function machines and mappings to find outputs and inputs of simple functions."}})
lin = lambda a, b: (f"{a}n" if a != 1 else "n") + (f" + {b}" if b > 0 else f" − {-b}" if b < 0 else "")

# ================================================================== 9.1
s = U.section("9.1", "Generating sequences (1)", ["O1"])
s.idea("Term-to-term rules", ["A **sequence** is a list of numbers in order. Each number is a **term**.",
       "A **term-to-term rule** tells you how to get the next term: start at 4 and add 3 → 4, 7, 10, 13, …"])
s.check(N("A sequence starts at 5 and the rule is 'add 4'. What is the 4th term?", 17, o="O1"))
s.idea("Why the term-to-term rule is not enough", ["The rule 'add 4' tells you how to get the next term, but not where to start: 1, 5, 9, … and 3, 7, 11, … both add 4.",
       "To describe a sequence you need the first term AND the rule."])
s.check(MC("Before you read on: a sequence starts 2, 4, … What is the next term?", "It depends on the rule", [("6", "That works for 'add 2'."), ("8", "That works for 'multiply by 2'.")], o="O1", hint="Find two different rules that give 2, 4."))
s.example("Two rules, same start", "Continue 2, 4, … using 'add 2' and using 'multiply by 2'.", [("add 2: 2, 4, 6, 8, 10", "the gap stays 2"), ("multiply by 2: 2, 4, 8, 16, 32", "the gap doubles")], "6, 8, 10 or 8, 16, 32")
s.mistake("Count the terms", ["The 4th term is three steps after the first term, not four."])


def t1(r):
    a, d, k = r.randint(-5, 20), r.randint(2, 9), r.randint(4, 8)
    return N(f"A sequence starts at {a}. The rule is 'add {d}'. What is term {k}?", a + (k - 1) * d, o="O1")
def t2(r):
    a, d, k = r.randint(30, 80), r.randint(2, 9), r.randint(4, 7)
    return N(f"A sequence starts at {a}. The rule is 'subtract {d}'. What is term {k}?", a - (k - 1) * d, o="O1")
def t3(r):
    a, d = r.randint(1, 20), r.randint(2, 9); t = [a + i * d for i in range(5)]
    return N("The table shows the first four terms of a sequence. Find the 5th term.", t[4], o="O1", data={"head": ["Term", "1st", "2nd", "3rd", "4th"], "rows": [["Value", *map(str, t[:4])]]})
def t4(r):
    a, d = r.randint(1, 20), nz(r, -6, 9); t = [a + i * d for i in range(5)]; k = r.randint(1, 3)
    return N(f"Find the missing term: {', '.join(str(x) if i != k else '☐' for i, x in enumerate(t))}", t[k], o="O1")
def t5(r):
    a, m = r.randint(1, 5), r.randint(2, 3)
    return N(f"A sequence starts at {a}. The rule is 'multiply by {m}'. What is the 4th term?", a * m ** 3, o="O1")
def t6(r):
    a, d = r.randint(1, 20), r.randint(2, 9)
    return TB(f"The first term is {a} and the rule is 'add {d}'. Complete the table.", ["Term", "Value"], [["1st", str(a)], ["2nd", B(a + d)], ["3rd", B(a + 2 * d)], ["5th", B(a + 4 * d)]], o="O1")
def t7(r):
    a, d = r.randint(2, 20), r.randint(2, 9); t = [a + i * d for i in range(4)]
    return S(f"Write the term-to-term rule for {', '.join(map(str, t))}, …", [f"add {d}", f"+{d}", f"+ {d}", f"plus {d}", f"increase by {d}", f"goes up by {d}"], o="O1")
def t8(r):
    a, d = r.randint(2, 10), r.randint(2, 9); v = a + r.randint(5, 20) * d + pick(r, [0, 1, 2])
    yes = (v - a) % d == 0
    return MC(f"The sequence {a}, {a + d}, {a + 2 * d}, … goes on. Is {v} in the sequence?", "Yes" if yes else "No", ["No" if yes else "Yes", "Cannot tell"], o="O1", d="H")


def t9(r):   # missing terms in the middle
    a, d = r.randint(1, 20), r.randint(2, 9)
    return TB(f"Fill in the missing terms of this sequence: {a}, ☐, ☐, {a + 3 * d}, …", ["2nd term", "3rd term"], [[B(a + d), B(a + 2 * d)]], o="O1", d="H",
              reason=f"From {a} to {a + 3 * d} is 3 equal steps of {d}.")
def t10(r):   # will this number be in the sequence?
    a, d = r.randint(1, 9), r.randint(3, 7); t = a + d * r.randint(10, 30) + r.choice([0, 0, 1, 2])
    yes = (t - a) % d == 0
    return MC(f"The sequence starts at {a} and goes up by {d} each time. Will {t} be in the sequence?", "Yes" if yes else "No", [("No" if yes else "Yes", f"Check whether {t} − {a} = {t - a} divides exactly by {d}."), ("You can only tell by writing out every term", "Use the steps: (term − first term) ÷ step must be a whole number.")],
              o="O1", d="H", reason=f"{t} − {a} = {t - a}; {t - a} ÷ {d} = {(t - a) / d:g}.")
def t11(r):   # spot the error
    a, d = r.randint(2, 9), r.randint(3, 6)
    return MC(f"A sequence starts {a}, {a + d}, {a + 2 * d}, … Ben says the 10th term is {a + 10 * d}. What is it?", str(a + 9 * d), [(str(a + 10 * d), "From the 1st term to the 10th term there are only 9 steps."), (str(10 * d), "Start from the first term.")], o="O1", d="H",
              reason=f"{a} + 9 × {d} = {a + 9 * d}.")


s.std([t6, t3, t1, t2, t4, t5, t7, t8], EX("Explain how to find the 10th term of the sequence 3, 7, 11, 15, …", [("the rule is add 4", ["add 4|\\+ ?4|goes up by 4"]), ("3 + 9 × 4 = 39", ["39|9 ?× ?4"])], "The rule is add 4. The 10th term is 9 steps after the first: 3 + 9 × 4 = 39.", o="O1"),
      deep=[t9, t10, t11])

# ================================================================== 9.2
s = U.section("9.2", "Generating sequences (2)", ["O2"])
s.idea("Patterns", ["Patterns of shapes make sequences: count the dots, tiles or matchsticks in each pattern.",
       "If the number goes up by the same amount each time, the sequence is **linear**. 1, 4, 9, 16 (square numbers) is **not** linear."])
s.check(MC("Is 2, 5, 8, 11 linear?", "Yes", ["No", "Only after 11"], o="O2"))
s.idea("Why patterns grow steadily", ["In a pattern of squares made from matchsticks, each new square needs 3 more matchsticks because it shares one side with the square before. So the sequence goes 4, 7, 10, … adding 3.",
       "Look at what is added each time and WHY: that explains the term-to-term rule."])
s.check(MC("Before you read on: is 1, 4, 9, 16, … linear (same difference each time)?", "No", [("Yes", "The differences are 3, 5, 7: they change."), ("Only after 9", "The differences keep growing.")], o="O2"))
s.mistake("Check every gap", ["1, 2, 4, 7 goes up by 1, 2, 3 — not the same each time."])


def p1(r):
    a, d = r.randint(3, 8), r.randint(2, 5); t = [a + i * d for i in range(3)]
    return N(f"Pattern 1 has {t[0]} tiles, pattern 2 has {t[1]} and pattern 3 has {t[2]}. How many tiles are in pattern 5?", a + 4 * d, "tiles", units=["tiles"], o="O2", data={"head": ["Pattern", "1", "2", "3"], "rows": [["Tiles", *map(str, t)]]})
def p2(r):
    rows = [("3, 6, 9, 12", "Linear"), ("1, 4, 9, 16", "Not linear"), ("2, 4, 8, 16", "Not linear"), ("20, 17, 14, 11", "Linear"), ("1, 3, 6, 10", "Not linear"), ("5, 10, 15, 20", "Linear")]
    return GD("Is each sequence linear?", "Linear?", r.sample(rows, 4), o="O2")
def p3(r):
    k = r.randint(5, 12)
    return N(f"What is the {k}th square number?", k * k, o="O2")
def p4(r):
    k = r.randint(4, 9)
    return N(f"The triangular numbers are 1, 3, 6, 10, … What is the {k}th triangular number?", k * (k + 1) // 2, o="O2", d="H")
def p5(r):
    a, d = r.randint(3, 6), r.randint(2, 4); t = [a + i * d for i in range(4)]
    return TB("Matchstick patterns: continue the table.", ["Pattern", "Matchsticks"], [["4", B(t[3])], ["5", B(t[3] + d)], ["10", B(a + 9 * d)]], o="O2", data={"head": ["Pattern", "1", "2", "3"], "rows": [["Matchsticks", *map(str, t[:3])]]}, d="H")
def p6(r):
    a, d = r.randint(2, 6), r.randint(2, 5)
    return N(f"Each new pattern adds {d} counters. Pattern 1 has {a} counters. How many counters are in pattern 8?", a + 7 * d, "counters", units=["counters"], o="O2")
def p7(r):
    a = r.randint(1, 4); t = [a * 2 ** i for i in range(5)]
    return N(f"Find the next term: {', '.join(map(str, t[:4]))}, …", t[4], o="O2")


def q1_(r):   # linear or not
    rows = r.sample([("3, 7, 11, 15", "Linear"), ("1, 4, 9, 16", "Not linear"), ("20, 17, 14, 11", "Linear"), ("2, 4, 8, 16", "Not linear"), ("5, 5.5, 6, 6.5", "Linear"), ("1, 3, 6, 10", "Not linear")], 4)
    return GD("Is each sequence linear?", "Linear?", rows, o="O2", d="H", extra=["Linear", "Not linear"], reason="Find the differences between terms. Linear means the difference is the same every time (it can be negative or a decimal).")
def q2_(r):   # matchsticks
    n = r.randint(5, 12)
    return N(f"Pattern 1 uses 4 matchsticks (one square). Each new pattern adds one square in a row, sharing a side. How many matchsticks are in pattern {n}?", 3 * n + 1, o="O2", d="H",
             reason=f"Start with 4, add 3 for each of the {n - 1} extra squares: 4 + 3 × {n - 1} = {3 * n + 1}.")


s.std([p1, p2, p3, p4, p5, p6, p7], EX("Explain why 1, 4, 9, 16, … is not a linear sequence.", [("the differences are 3, 5, 7: not the same", ["3, ?5|differences|not the same"]), ("these are the square numbers", ["square"])], "The differences are 3, 5, 7, so they are not the same each time. These are the square numbers, which do not go up by a fixed amount.", o="O2"),
      deep=[q1_, q2_])

# ================================================================== 9.3
s = U.section("9.3", "Using the nth term", ["O3"])
s.idea("Position-to-term rule", ["The **nth term** gives any term from its position n. For 2n + 3: n = 1 → 5, n = 2 → 7, n = 10 → 23.",
       "You can find the 100th term without listing all the terms before it."])
s.check(N("The nth term is 4n − 1. Find the 5th term.", 19, o="O3"))
s.idea("Why the number in front of n is the difference", ["In 3n + 2, each time n goes up by 1, 3n goes up by 3, so every term is 3 more than the one before. The 3 is the term-to-term difference.",
       "The + 2 shifts every term: 3n is 3, 6, 9, … and 3n + 2 is 5, 8, 11, …"], table={"head": ["n", "1", "2", "3", "4"], "rows": [["3n", "3", "6", "9", "12"], ["3n + 2", "5", "8", "11", "14"]]})
s.check(MC("Before you read on: which nth term gives the sequence 7, 11, 15, 19, …?", "4n + 3", [("3n + 4", "The difference is 4, so it must start 4n."), ("n + 4", "The difference is 4, not 1.")], o="O3"))
s.mistake("Multiply first", ["For 3n + 2 with n = 4: 3 × 4 + 2 = 14, not 3 × 6."])


def n1(r):
    a, b, k = r.randint(2, 9), r.randint(-5, 10), r.randint(3, 20)
    return N(f"The nth term of a sequence is {lin(a, b)}. Find the {k}th term.", a * k + b, o="O3")
def n2(r):
    a, b = r.randint(2, 9), r.randint(-5, 10)
    return TB(f"Write the first three terms of the sequence with nth term {lin(a, b)}.", ["n", "Term"], [[str(n), B(a * n + b)] for n in (1, 2, 3)], o="O3")
def n3(r):
    a, b = r.randint(2, 9), r.randint(-5, 10)
    return N(f"The nth term is {lin(a, b)}. Find the 100th term.", 100 * a + b, o="O3")
def n4(r):
    a, b = r.randint(2, 6), r.randint(0, 6); t = [a * n + b for n in range(1, 5)]
    return MC(f"Which nth term gives the sequence {', '.join(map(str, t))}, …?", lin(a, b), [lin(1, a + b) if a + b != b else lin(1, a), lin(a, b + a), lin(b if b > 1 else a + 1, a)], o="O3", d="H")
def n5(r):
    a, b, k = r.randint(2, 9), r.randint(1, 10), r.randint(5, 20)
    return N(f"The nth term is {lin(a, b)}. Which term is equal to {a * k + b}?", k, o="O3", d="H")
def n6(r):
    a = r.randint(2, 9)
    return N(f"A sequence has nth term {a}n. What is the difference between consecutive terms?", a, o="O3")
def n7(r):
    rows = [("3n", "3, 6, 9"), ("n + 4", "5, 6, 7"), ("2n − 1", "1, 3, 5"), ("5n + 2", "7, 12, 17"), ("10 − n", "9, 8, 7")]
    return GD("Match each nth term to its first three terms.", "First terms", r.sample(rows, 4), o="O3", extra=["2, 4, 6"])


def u1_(r):   # is it a term?
    a, b = r.randint(2, 7), r.randint(-3, 9); n = r.randint(10, 40); t = a * n + b + r.choice([0, 1])
    yes = (t - b) % a == 0
    return MC(f"Is {t} a term of the sequence with nth term {lin(a, b)}?", "Yes" if yes else "No", [("No" if yes else "Yes", f"Solve {lin(a, b)} = {t}: n must be a whole number.")], o="O3", d="H",
              reason=f"{lin(a, b)} = {t} gives n = {(t - b) / a:g}" + (" – a whole number." if yes else " – not a whole number."))
def u2_(r):   # first term above a value
    a, b = r.randint(3, 8), r.randint(1, 9); lim = r.randint(50, 150)
    n = next(k for k in range(1, 200) if a * k + b > lim)
    return N(f"The nth term of a sequence is {lin(a, b)}. Which is the first term bigger than {lim}? Give the term, not its position.", a * n + b, o="O3", d="VH",
             reason=f"n = {n - 1} gives {a * (n - 1) + b}; n = {n} gives {a * n + b}.")
def u3_(r):   # spot the error
    a, b = r.randint(2, 6), r.randint(1, 9)
    return MC(f"Kim says the sequence {a + b}, {2 * a + b}, {3 * a + b}, … has nth term n + {a}. What is wrong?", f"The difference {a} goes in front of n: {lin(a, b)}", [("Nothing", f"n + {a} gives {1 + a}, {2 + a}, … – a difference of 1."), (f"It should be {b}n + {a}", f"The difference is {a}, not {b}.")],
              o="O3", d="H", reason=f"The difference is {a}, so start with {a}n; {a}n gives {a}, {2 * a}, … and adding {b} gives the sequence.")


s.std([n2, n7, n1, n3, n4, n5, n6], EX("Explain how the nth term 5n + 1 gives the sequence 6, 11, 16, …", [("substitute n = 1, 2, 3", ["n ?= ?1|substitute|put n"]), ("5 × 1 + 1 = 6, 5 × 2 + 1 = 11, 5 × 3 + 1 = 16", ["6|11|16"])], "Substitute the positions: n = 1 gives 5 × 1 + 1 = 6, n = 2 gives 11 and n = 3 gives 16.", o="O3"),
      deep=[u1_, u2_, u3_])

# ================================================================== 9.4
s = U.section("9.4", "Representing simple functions", ["O4"])
s.idea("Function machines", ["A **function machine** takes an input, does one or more operations, and gives an output: 3 → × 4 → + 1 → 13.",
       "To find the input from an output, work **backwards** using the inverse operations: 13 → − 1 → ÷ 4 → 3."])
s.check(N("Input 5 → × 3 → − 2 → output. What is the output?", 13, o="O4"))
s.idea("Why we undo in reverse", ["A function machine is like getting dressed: socks then shoes. To undo it, take off the shoes first, then the socks.",
       "For x → × 2 → + 5 → 17, undo + 5 first (17 − 5 = 12), then undo × 2 (12 ÷ 2 = 6)."])
s.check(MC("Before you read on: do x → × 3 → + 1 and x → + 1 → × 3 give the same output for x = 2?", "No", [("Yes", "× 3 then + 1 gives 7; + 1 then × 3 gives 9."), ("Only for x = 0", "Try x = 0: 1 and 3 – still different.")], o="O4"))
s.mistake("Backwards means inverse", ["To undo + 1 you subtract 1; to undo × 4 you divide by 4."])


def f1(r):
    a, b, x = r.randint(2, 9), r.randint(1, 12), r.randint(1, 12)
    return N(f"Input {x} → × {a} → + {b} → output. What is the output?", a * x + b, o="O4")
def f2(r):
    a, b, x = r.randint(2, 9), r.randint(1, 12), r.randint(1, 12)
    return N(f"Input → × {a} → + {b} → output. The output is {a * x + b}. What was the input?", x, o="O4", d="H")
def f3(r):
    a, b = r.randint(2, 6), r.randint(1, 9); xs = r.sample(range(1, 10), 3)
    return TB(f"Complete the table for the function x → × {a} → + {b}.", ["Input", "Output"], [[str(x), B(a * x + b)] for x in sorted(xs)], o="O4")
def f4(r):
    a, b = r.randint(2, 6), r.randint(1, 9)
    return MC(f"Which is the inverse of 'multiply by {a}, then add {b}'?", f"subtract {b}, then divide by {a}", [f"divide by {a}, then subtract {b}", f"add {b}, then multiply by {a}", f"subtract {a}, then divide by {b}"], o="O4")
def f5(r):
    a, b = r.randint(2, 5), r.randint(1, 9); pairs = [(x, a * x + b) for x in r.sample(range(1, 8), 3)]
    return X(f"A function maps {', '.join(f'{x} → {y}' for x, y in pairs)}. Write the function as y = …", f"{a}x+{b}", vars="xy", lhs="y", o="O4", d="H", data={"head": ["x", *[str(x) for x, _ in pairs]], "rows": [["y", *[str(y) for _, y in pairs]]]})
def f6(r):
    a, x = r.randint(2, 9), r.randint(2, 30)
    return N(f"Input → ÷ {a} → output. The output is {x}. What was the input?", a * x, o="O4")
def f7(r):
    a, b = r.randint(2, 9), r.randint(1, 12)
    return X(f"Write the function machine x → × {a} → + {b} → y as an equation.", f"{a}x+{b}", vars="xy", lhs="y", o="O4")


def f8(r):   # order matters
    a, b, x = r.randint(2, 5), r.randint(1, 9), r.randint(2, 9)
    return TB(f"Find each output when the input is {x}.", ["Machine", "Output"], [[f"× {a} then + {b}", B(a * x + b)], [f"+ {b} then × {a}", B((x + b) * a)]], o="O4", d="H",
              reason=f"{x} × {a} + {b} = {a * x + b}; ({x} + {b}) × {a} = {(x + b) * a}. The order of the operations matters.")
def f9(r):   # find the machine
    a, b = r.randint(2, 6), r.randint(1, 9)
    return MC(f"A machine turns 1 into {a + b}, 2 into {2 * a + b} and 5 into {5 * a + b}. What does it do?", f"× {a} then + {b}", [(f"+ {a + b - 1}", f"Try 2: 2 + {a + b - 1} = {a + b + 1}, not {2 * a + b}."), (f"× {a + b}", f"Try 2: 2 × {a + b} = {2 * a + 2 * b}.")],
              o="O4", d="H", reason=f"When the input goes up by 1 the output goes up by {a}, so it multiplies by {a}; then 1 × {a} + {b} = {a + b}.")


s.std([f3, f5, f1, f2, f4, f6, f7], EX("Explain how to find the input when the output of x → × 2 → + 5 is 17.", [("work backwards: subtract 5", ["subtract 5|− ?5|- ?5|take away 5|12"]), ("then divide by 2: 6", ["divide by 2|÷ ?2|\\b6\\b"])], "Work backwards with the inverse operations: 17 − 5 = 12, then 12 ÷ 2 = 6. The input was 6.", o="O4"),
      deep=[f8, f9])

U.mindmap(("Term-to-term", "Start and a rule • next term", "O1", "9.1"), ("Patterns", "Count each pattern • linear or not", "O2", "9.2"),
          ("nth term", "Substitute n • any term directly", "O3", "9.3"), ("Function machines", "Input → operations → output • inverse to go back", "O4", "9.4"))
