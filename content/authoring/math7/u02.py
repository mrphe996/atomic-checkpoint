# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 2 Expressions, formulae and equations (2.1 Constructing expressions, 2.2 Using expressions and
formulae, 2.3 Collecting like terms, 2.4 Expanding brackets, 2.5 Constructing and solving equations, 2.6 Inequalities).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (find all, test a claim, spot the error, work backwards) rather than repeated routines.
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
TL = lambda *rows: {"kind": "tiles", "rows": list(rows)}
ASN = ["Always true", "Sometimes true", "Never true"]

# ================================================================== 2.1
s = U.section("2.1", "Constructing expressions", ["O1"])
s.idea("A letter is a number you do not know yet", [
    "A box holds some pencils. We do not know how many, so we call the number **n**. The letter is not a word or an object: it stands for **a number**.",
    "Every operation in words becomes an operation on n. Three boxes hold **3n** pencils (3 × n). Three boxes and 2 loose pencils hold **3n + 2**. Share a box between two people and each gets **n/2**.",
    "An expression is a recipe: it tells you what to do to n. It has no '=' sign, because we are not saying what n is."],
    fig=TL(["one box = n", [[["x", 1]]]], ["3 boxes + 2", [[["x", 3]], [["1", 2]]]]))
s.check(X("A bag has b sweets. Write an expression for the number of sweets in 5 bags and 3 loose sweets.", "5b+3", vars="b", o="O1",
          hint="5 bags is 5 lots of b. Then add the loose sweets."))
s.example("Order matters for 'less than'", "Write an expression for '7 less than n'.",
          [("start with n", "the amount we are making smaller"), ("take 7 away from it: n − 7", "'7 less than n' means n made 7 smaller")], "n − 7",
          p=["Compare it with '7 take away n', which is 7 − n. Try n = 10: n − 7 = 3 but 7 − n = −3. The words decide which number comes first."])
s.check(MC("Which expression means '5 less than twice m'?", "2m − 5", [("5 − 2m", "This is 5 take away 2m – the order is the wrong way round."), ("2(m − 5)", "This takes 5 away before doubling."), ("5m − 2", "The 5 and the 2 have swapped jobs.")], o="O1"))
s.method("Turning words into an expression", [
    "Ask: what is the unknown? Give it a letter.", "Ask: what happens to it, and in which order?", "Test your expression with an easy number – if n = 10, does the expression give the answer you expect?"])
s.mistake("3n and n + 3 are different", ["3n means three lots of n; n + 3 means three more than n. With n = 5 they give 15 and 8."])
W = [("y plus 6", "y+6", "y"), ("8 more than t", "t+8", "t"), ("p take away 3", "p-3", "p"), ("double k", "2k", "k"), ("n multiplied by 7", "7n", "n"), ("m divided by 5", "m/5", "m"),
     ("4 less than 3 times x", "3x-4", "x"), ("half of w, plus 1", "w/2+1", "w"), ("the square of a", "a^2", "a"), ("10 minus c", "10-c", "c")]


def c1(r):
    w = pick(r, W)
    return X(f"Write an expression for: {w[0]}.", w[1], vars=w[2], o="O1")
def c2(r):
    n, k = r.randint(2, 9), r.randint(1, 9)
    return X(f"A pack of cards has c cards. Lily has {n} packs and {k} extra cards. Write an expression for how many cards she has.", f"{n}c+{k}", vars="c", o="O1")
def c4(r):
    a = r.randint(2, 9)
    return X("Write an expression for the perimeter of the rectangle.", f"2x+{2 * a}", o="O1", fig=RECT("x cm", f"{a} cm"), reason=f"Add all four sides: x + {a} + x + {a}. Collect them: 2x + {2 * a}.")
def c5(r):
    k = r.randint(2, 9)
    return MC(f"Which expression means 'n divided by {k}'?", f"n/{k}", [(f"{k}/n", "This divides the number by n, not n by the number."), (f"{k}n", "This multiplies."), (f"n − {k}", "This subtracts.")], o="O1")
def c6(r):
    rows = [("3 more than n", "n + 3"), ("3 times n", "3n"), ("n less 3", "n − 3"), ("n divided by 3", "n/3"), ("n squared", "n²")]
    return GD("Match each description to its expression.", "Expression", r.sample(rows, 4), o="O1", extra=["3 − n"])
def c7(r):
    p = r.randint(2, 9); q = r.randint(2, 9)
    return X(f"Pens cost p cents and rulers cost r cents. Write an expression for the cost of {p} pens and {q} rulers.", f"{p}p+{q}r", vars="pr", o="O1")
# --- reasoning: choose the story, test a claim, work backwards
def d1(r):   # which story fits the expression?
    a, b = r.randint(2, 6), r.randint(2, 9)
    right = f"{a} boxes of n pencils, and {b} more pencils"
    return MC(f"Which story matches the expression {a}n + {b}?", right,
              [(f"{a} boxes of n pencils, with {b} pencils taken out", f"Taking out would be {a}n − {b}."), (f"n boxes, each with {a + b} pencils", f"That is {a + b}n."), (f"{b} boxes of n pencils, and {a} more pencils", f"That is {b}n + {a} – the numbers have swapped jobs.")],
              o="O1", d="H", hint=f"Which number multiplies n? That is the number of boxes.",
              reason=f"In {a}n + {b} the {a} multiplies n, so there are {a} lots of n. Then {b} is added on by itself. Only the first story does both.")
def d2(r):   # always / sometimes / never, for whole numbers n ≥ 1
    rows = r.sample([("n + n = 2n", "Always true"), ("3n is bigger than n + 3", "Sometimes true"), ("n + 4 = n", "Never true"), ("2n is an even number", "Always true"),
                     ("n² is bigger than 2n", "Sometimes true"), ("n − n = 0", "Always true"), ("n + 1 is smaller than n", "Never true"), ("n/2 is a whole number", "Sometimes true")], 4)
    return GD("n is a whole number (1, 2, 3, …). Is each statement always true, sometimes true or never true?", "Always / sometimes / never", rows, o="O1", d="H", extra=ASN,
              reason="Try several values of n, including small ones like 1 and 2. One counter-example is enough to show a statement is not always true. For example, 3n > n + 3 is false for n = 1 (3 < 4) but true for n = 2 (6 > 5), so it is sometimes true.")
def d3(r):   # work backwards from a value
    a, b, n = r.randint(2, 6), r.randint(1, 9), r.randint(2, 12)
    return N(f"Kim's expression is {a}n + {b}. When she uses her number she gets {a * n + b}. What number did she use for n?", n, o="O1", d="H",
             hint=f"Undo the steps in reverse order: first undo + {b}, then undo × {a}.",
             reason=f"{a * n + b} − {b} = {a * n}. Then {a * n} ÷ {a} = {n}. Check: {a} × {n} + {b} = {a * n + b}.")
def d4(r):   # spot the error in a student's expression
    k = r.randint(3, 9)
    return MC(f"Sam writes '{k} less than y' as {k} − y. Which is correct?", f"Sam is wrong: it should be y − {k}",
              [(f"Sam is right: {k} − y", f"Test y = 20: '{k} less than 20' is {20 - k}, but {k} − 20 = {k - 20}."), ("Both are the same", "Subtraction depends on the order."), (f"It should be {k}y", "There is no multiplying in 'less than'.")],
              o="O1", d="H", hint="Choose an easy value for y, such as 20, and test both.", reason=f"'{k} less than y' means y made {k} smaller, so y − {k}. Testing with y = 20 gives {20 - k}, which confirms it.")


s.std([c4, c6, c1, c2, c5, c7], EX("Explain the difference between 3n and n + 3. Use a value of n to show they are different.", [("3n means 3 multiplied by n", ["multipl|times|3 lots|3 ?× ?n"]), ("n + 3 means add 3 to n", ["add|plus|3 more"]), ("a value that gives different answers", ["n ?= ?\\d|15|8|\\d+ and \\d+"])], "3n means 3 × n (three lots of n). n + 3 means n with 3 added on. For n = 5: 3n = 15 but n + 3 = 8.", o="O1", need=2),
      deep=[d1, d2, d3, d4])

# ================================================================== 2.2
s = U.section("2.2", "Using expressions and formulae", ["O2"])
s.idea("Substitution: put the number in the letter's place", [
    "To **substitute**, replace each letter with its number, then calculate using the order of operations (brackets, powers, × ÷, then + −).",
    "Write the multiplication sign back in: if x = 4, then 3x means 3 × 4, not 34. So 3x + 1 = 3 × 4 + 1 = 13.",
    "A **formula** is a rule linking quantities, for example the perimeter of a rectangle P = 2l + 2w. Substituting gives one value from the others."], fig=RECT("l", "w"))
s.check(N("Find the value of 5a − 2 when a = 6.", 28, o="O2", hint="Write it as 5 × 6 − 2."))
s.example("Powers before multiplying", "Find 4n² when n = 3.", [("n² = 3² = 9", "only n is squared"), ("4 × 9 = 36", "then multiply by 4")], "36",
          p=["Compare (4n)² when n = 3: the bracket is worked out first, 4 × 3 = 12, then 12² = 144. The bracket changes what is squared."])
s.check(MC("When n = 2, which is larger: 3n² or (3n)²?", "(3n)² = 36", [("3n² = 36", "3n² = 3 × 4 = 12."), ("They are equal", "Work them out: 12 and 36.")], o="O2", hint="Work each one out with n = 2."))
s.mistake("Order of operations", ["In 2 + 3x with x = 4, multiply first: 2 + 12 = 14, not 5 × 4 = 20."])


def u1(r):
    a, b, x = r.randint(2, 9), r.randint(1, 15), r.randint(1, 12)
    return N(f"Find the value of {a}x + {b} when x = {x}.", a * x + b, o="O2")
def u2(r):
    x, y = r.randint(2, 12), r.randint(2, 12)
    return N(f"Find the value of xy when x = {x} and y = {y}.", x * y, o="O2")
def u4(r):
    l, w = r.randint(3, 20), r.randint(2, 15)
    return N(f"Use P = 2l + 2w to find the perimeter when l = {l} and w = {w}.", 2 * l + 2 * w, "cm", units=["cm"], o="O2", fig=RECT("l", "w"))
def u5(r):
    c, h = r.randint(10, 30), r.randint(2, 6); rate = r.randint(5, 15)
    return N(f"A bike costs C = {c} + {rate}h dollars to hire for h hours. Find the cost for {h} hours.", c + rate * h, "$", units=["$"], o="O2")
def u6(r):
    a = r.randint(2, 5); xs = r.sample(range(1, 10), 3)
    return TB(f"Complete the table for the expression {a}n − 1.", ["n", f"{a}n − 1"], [[str(x), B(a * x - 1)] for x in sorted(xs)], o="O2")
def u8(r):
    d, t = r.randint(2, 9) * 10, r.randint(2, 5)
    return N(f"Use the formula s = d ÷ t to find the speed s when d = {d * t} km and t = {t} hours.", d, "km/h", units=["km/h"], o="O2")
# --- reasoning
def v1(r):   # which expression is largest for this value?
    n = r.randint(2, 5)
    ex = [("2n²", 2 * n * n), ("(2n)²", (2 * n) ** 2), ("n² + 2", n * n + 2), ("2n + 2", 2 * n + 2)]
    big = max(ex, key=lambda e: e[1])
    return MC(f"When n = {n}, which expression has the largest value?", big[0], [(e[0], f"{e[0]} = {e[1]}") for e in ex if e is not big], o="O2", d="H",
              hint="Work out every expression. Watch which part is squared.", reason="Values: " + ", ".join(f"{e[0]} = {e[1]}" for e in ex) + f". The largest is {big[0]}.")
def v2(r):   # find the missing input
    l = r.randint(4, 15); w = r.randint(2, 9)
    return N(f"A rectangle has perimeter P = 2l + 2w = {2 * l + 2 * w} cm and width w = {w} cm. Find its length l.", l, "cm", units=["cm"], o="O2", d="H", fig=RECT("l", f"{w} cm"),
             hint=f"Put w = {w} in the formula first. What must 2l be?", reason=f"2l + 2 × {w} = {2 * l + 2 * w}, so 2l = {2 * l + 2 * w} − {2 * w} = {2 * l} and l = {l} cm.")
def v3(r):   # spot the error in a substitution
    x = r.randint(3, 6); a = r.randint(2, 4)
    wrong = (a * x) ** 2
    return MC(f"Lee says that when x = {x}, {a}x² = {wrong}. What did Lee do wrong?", f"He squared {a}x instead of only x; the answer is {a * x * x}",
              [(f"Nothing – {wrong} is right", f"{a}x² means {a} × x², so square {x} first."), (f"He should have added: {a + x * x}", "The number in front multiplies."), (f"He should have doubled x: {a * 2 * x}", "Squaring means multiplying a number by itself.")],
              o="O2", d="H", reason=f"In {a}x² only x is squared: {x}² = {x * x}, then {a} × {x * x} = {a * x * x}. Lee worked out ({a}x)² = {a * x}² = {wrong}.")
def v4(r):   # find all pairs
    t = r.choice([12, 18, 20, 24])
    pairs = [(a, t // a) for a in range(1, t + 1) if t % a == 0 and a < t // a]
    s_ = r.choice(pairs)
    return N(f"x and y are whole numbers with x < y. When you substitute them, xy = {t} and x + y = {s_[0] + s_[1]}. What is x?", s_[0], o="O2", d="VH",
             hint=f"List every pair of whole numbers that multiply to {t}, then check which pair adds to {s_[0] + s_[1]}.",
             reason=f"Pairs with product {t}: " + ", ".join(f"{a} and {b}" for a, b in pairs) + f". Only {s_[0]} + {s_[1]} = {s_[0] + s_[1]}, so x = {s_[0]}. Listing every pair is how we know there is no other answer.")


s.std([u4, u6, u1, u2, u5, u8], EX("Explain why 4n² is 64 when n = 4, not 256.", [("square n first: 4² = 16", ["square.*first|4² ?= ?16|16"]), ("then multiply by 4: 4 × 16 = 64", ["4 ?× ?16|64"])], "Only n is squared: 4² = 16. Then multiply by 4: 4 × 16 = 64. (256 would be (4n)².)", o="O2"),
      deep=[v1, v2, v3, v4])

# ================================================================== 2.3
s = U.section("2.3", "Collecting like terms", ["O3"])
s.idea("Why 3x + 2x = 5x", [
    "Think of x as a rod of unknown length. 3x is three rods and 2x is two more rods of the **same** length. Put them together and you have five rods: **3x + 2x = 5x**, whatever length a rod is.",
    "Terms with exactly the same letter part are **like terms**: 4a and 7a are like terms; 4a and 4b are not; 2 and 5 (plain numbers) are like terms with each other."],
    fig=TL(["3x + 2x", [[["x", 3]], [["x", 2]]]], ["= 5x", [[["x", 5]]]]))
s.check(MC("Ana says 3x + 2 = 5x. Before you read on: is she right?", "Not always – only when x = 1",
           [("Yes, always", "Try x = 4: 3 × 4 + 2 = 14 but 5 × 4 = 20."), ("Never", "Try x = 1: both give 5.")], o="O3", d="H",
           hint="Choose a value for x, such as x = 4, and work out both sides."))
s.example("3x + 2 is not 5x", "Use tiles to explain why 3x + 2 cannot be simplified.",
          [("3x is three rods; 2 is two small squares", "a rod is x long, a square is 1"), ("rods and squares are different sizes, so we cannot count them together", "unless x happens to be 1"),
           ("test x = 4: 3x + 2 = 14 but 5x = 20", "one counter-example shows it is not always true")], "3x + 2 is already as simple as it gets",
          fig=TL(["3x + 2", [[["x", 3]], [["1", 2]]]], ["5x ?", [[["x", 5]]]]))
s.check(X("Simplify 6x + 3 + 2x − 1.", "8x+2", o="O3", mustNot=["\\("], hint="Collect the x rods together, then the numbers together."))
s.method("Collecting like terms", [
    "Underline or colour each kind of term (all the x terms, all the y terms, all the numbers).",
    "Each term keeps the sign in front of it: in 5x − 2y + 3x, the term is −2y.", "Add the numbers in front of like terms; keep the letter part the same."],
    steps=[("5x − 2y + 3x + 6y", "colour the x terms and the y terms"), ("5x + 3x = 8x", "the x terms"), ("−2y + 6y = 4y", "the y terms keep their signs"), ("8x + 4y", "answer")])
s.mistake("Keep the sign with its term", ["The sign belongs to the term after it: in 5x − 2y + 3x the −2y stays negative."])


def l1(r):
    a, b = r.randint(2, 9), r.randint(2, 9)
    return X(f"Simplify {a}y + {b}y.", f"{a + b}y", vars="y", o="O3")
def l2(r):
    a, b, c, d = r.randint(2, 9), r.randint(1, 9), r.randint(1, 9), r.randint(1, 9)
    return X(f"Simplify {a}a + {b}b + {c}a + {d}b.", f"{a + c}a+{b + d}b", vars="ab", o="O3", mustNot=["\\("])
def l4(r):
    rows = [("2x and 5x", "Like"), ("3y and 3z", "Not like"), ("ab and ba", "Like"), ("4 and 4t", "Not like"), ("x² and 2x²", "Like"), ("x and x²", "Not like")]
    return GD("Are these like terms?", "Like terms?", r.sample(rows, 4), o="O3", reason="Like terms have exactly the same letter part (ab and ba are the same, because a × b = b × a). x and x² are different: x² is x × x.")
def l5(r):
    a, b = r.randint(2, 6), r.randint(1, 9)
    return X("Write a simplified expression for the perimeter of this triangle.", f"{3 * a}x+{2 * b}", o="O3", fig={"kind": "shape", "pts": [[0, 0], [8, 0], [4, 6]], "s": [f"{a}x", f"{a}x + {b}", f"{a}x + {b}"]})
def l7(r):
    a, b, c, d = r.randint(3, 9), r.randint(1, 5), r.randint(2, 8), r.randint(1, 5)
    return X(f"Simplify {a}x − {b}y − {c}x + {d}y.", f"{a - c}x+({d - b})y", vars="xy", o="O3", d="H", mustNot=["\\("], show=poly((a - c, 'x'), (d - b, 'y')))
# --- reasoning
def k1(r):   # test a claim with a value
    a, b = r.randint(2, 6), r.randint(2, 6)
    return TB(f"Mo says {a}x + {b} = {a + b}x for every x. Test his claim with x = 1 and x = 3.", ["x", f"{a}x + {b}", f"{a + b}x"], [["1", B(a + b), B(a + b)], ["3", B(3 * a + b), B(3 * (a + b))]], o="O3", d="H",
              hint="Substitute each value into both expressions.", reason=f"With x = 1 both give {a + b}, but with x = 3 they give {3 * a + b} and {3 * (a + b)}. One counter-example (x = 3) shows Mo's claim is false: {a}x and {b} are not like terms.")
def k2(r):   # missing term
    a, c, m, b = r.randint(2, 6), r.randint(2, 6), r.randint(2, 7), r.randint(2, 9)
    return X(f"Find the missing term: {a}a + ☐ + {b}b − a = {a - 1 + m}a + {b}b.", f"{m}a", vars="ab", o="O3", d="H",
             hint=f"Collect the a terms you already have: {a}a − a. How many more a do you need?", reason=f"{a}a − a = {a - 1}a. To make {a - 1 + m}a you need {m}a more, so the missing term is {m}a.")
def k3(r):   # choose the two that add to a target
    p, q, u, v = r.randint(2, 6), r.randint(1, 6), r.randint(2, 6), r.randint(1, 6)
    rights = [f"{p}x + {q}", f"{u}x + {v}"]
    wrongs = [f"{p + u}x", f"{q + v}x + {p}"]
    return MS(f"Choose the TWO expressions that add up to {p + u}x + {q + v}.", rights, wrongs, o="O3", d="H",
              reason=f"({p}x + {q}) + ({u}x + {v}) = {p + u}x + {q + v}. The others do not have both an x part and a number part that match.")
def k4(r):   # spot the error
    a, b, c, d = r.randint(3, 8), r.randint(2, 6), r.randint(2, 6), r.randint(1, 5)
    return MC(f"Jo simplifies {a}x − {b}y + {c}x + {d}y and gets {a + c}x + {b + d}y. Where is her mistake?", f"She lost the minus sign: −{b}y + {d}y = {d - b}y",
              [("She added the x terms wrongly", f"{a}x + {c}x = {a + c}x is right."), ("There is no mistake", f"−{b}y + {d}y is not {b + d}y."), ("x and y are like terms", "Different letters are not like terms.")],
              o="O3", d="H", reason=f"The y terms are −{b}y and +{d}y, so together they make {d - b}y. The right answer is {a + c}x + ({d - b})y.")
def k5(r):   # perimeter with a decision
    a, b = r.randint(2, 5), r.randint(1, 6)
    return MC(f"Two shapes: a square with side {a}x, and a rectangle {a + 1}x by {a - 1}x. Which statement is true?", "They always have the same perimeter",
              [("The square's perimeter is bigger", f"Square: 4 × {a}x = {4 * a}x. Rectangle: 2({a + 1}x) + 2({a - 1}x) = {4 * a}x."), ("It depends on x", "Both simplify to the same expression, so x does not matter.")],
              o="O3", d="VH", hint="Write each perimeter as an expression and simplify.", reason=f"Square: {a}x + {a}x + {a}x + {a}x = {4 * a}x. Rectangle: {a + 1}x + {a - 1}x + {a + 1}x + {a - 1}x = {4 * a}x. Equal expressions mean equal for every x.")


s.std([l4, l5, l1, l2, l7], EX("Explain why 3a + 2b cannot be simplified but 3a + 2a can.", [("3a and 2b have different letters, so they are not like terms", ["different letter|not like|unlike"]), ("3a and 2a are like terms: 5a", ["5a|like terms|same letter"])], "3a and 2b have different letters, so they are not like terms and cannot be added. 3a and 2a are like terms, so 3a + 2a = 5a.", o="O3"),
      deep=[k1, k2, k3, k4, k5])

# ================================================================== 2.4
s = U.section("2.4", "Expanding brackets", ["O4"])
s.idea("Why the number multiplies everything inside", [
    "3(x + 4) means three lots of (x + 4): (x + 4) + (x + 4) + (x + 4). Collect the x terms and the numbers: **3x + 12**.",
    "An area picture shows the same thing: a rectangle 3 high and (x + 4) wide splits into two parts, 3 × x and 3 × 4."], fig=RECT("x + 4", "3"))
s.check(MC("Before you expand: is 2(x + 5) the same as 2x + 5?", "No: 2(x + 5) = 2x + 10",
           [("Yes", "Test x = 1: 2(1 + 5) = 12 but 2 × 1 + 5 = 7."), ("Only when x = 0", "Even then: 2 × 5 = 10, not 5.")], o="O4", hint="Write out two lots of (x + 5)."))
s.example("A minus inside the bracket", "Expand 4(2y − 3).", [("4 × 2y = 8y", "the 4 multiplies the first term"), ("4 × (−3) = −12", "and the second term, keeping its sign")], "8y − 12")
s.check(X("Expand 5(y − 2).", "5y-10", vars="y", o="O4", mustNot=["\\("]))
s.mistake("Multiply both terms", ["2(n + 6) is 2n + 12, not 2n + 6."])


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
def e7(r):
    a, b = r.randint(2, 6), r.randint(1, 9); xs = r.sample(range(1, 6), 2)
    return TB(f"Check that {a}(x + {b}) = {a}x + {a * b} by completing the table.", ["x", f"{a}(x + {b})", f"{a}x + {a * b}"], [[str(x), B(a * (x + b)), B(a * x + a * b)] for x in xs], o="O4")
# --- reasoning
def f1(r):   # work backwards: missing number
    a, b = r.randint(2, 6), r.randint(2, 9)
    return N(f"Fill the gap: {a}(x + ☐) = {a}x + {a * b}. What goes in the box?", b, o="O4", d="H", hint=f"{a} × ☐ must make {a * b}.", reason=f"Expanding gives {a}x + {a} × ☐. So {a} × ☐ = {a * b} and ☐ = {b}.")
def f2(r):   # which are equivalent? (find all)
    a, b = r.randint(2, 4), r.randint(2, 5)
    rights = [f"{a}(x + {b})", f"{a}x + {a * b}", f"{a * b} + {a}x"]
    wrongs = [f"{a}x + {b}", f"{a}(x + {a * b})"]
    return MS(f"Select ALL the expressions that are equal to {a}x + {a * b} for every value of x.", rights, wrongs, o="O4", d="H",
              reason=f"{a}(x + {b}) expands to {a}x + {a * b}, and the order of adding does not matter. {a}x + {b} and {a}(x + {a * b}) give different values (test x = 0).")
def f3(r):   # common factor (reverse)
    a, b = r.choice([2, 3, 4, 5]), r.randint(2, 7)
    return X(f"Write {a}x + {a * b} with a bracket, in the form {a}(x + ☐).", f"{a}(x+{b})", o="O4", d="VH", must=["\\("], hint=f"What do you multiply {a} by to get {a * b}?",
             reason=f"{a}x = {a} × x and {a * b} = {a} × {b}, so {a}x + {a * b} = {a}(x + {b}). Check by expanding.")
def f4(r):   # spot the error
    a, b, c = r.randint(2, 5), r.randint(2, 5), r.randint(1, 6)
    return MC(f"Li expands {a}({b}x − {c}) and gets {a * b}x − {c}. What should she have done?", f"Multiplied the {c} by {a} too: {a * b}x − {a * c}",
              [(f"Added {a}: {a + b}x − {c}", "Expanding multiplies."), ("Nothing – it is right", f"Test x = 1: {a}({b} − {c}) = {a * (b - c)} but {a * b} − {c} = {a * b - c}."), (f"Changed the sign: {a * b}x + {a * c}", "The minus stays a minus.")],
              o="O4", d="H", reason=f"The {a} multiplies every term inside: {a} × {b}x = {a * b}x and {a} × (−{c}) = −{a * c}.")
def f5(r):   # area split, decide the missing length
    a, b = r.randint(2, 6), r.randint(2, 8)
    return N(f"A rectangle is {a} cm high and (x + ☐) cm wide. Its area is {a}x + {a * b} cm². What is the missing number?", b, o="O4", d="H", fig=RECT("x + ?", f"{a} cm"),
             reason=f"The area of the right-hand part is {a} × ☐ = {a * b}, so ☐ = {b}.")


s.std([e4, e7, e1, e2, e3], EX("Explain why 4(x + 5) = 4x + 20.", [("the 4 multiplies every term in the bracket", ["every|both|each"]), ("4 × x = 4x and 4 × 5 = 20", ["4 ?× ?5|20"])], "When you expand, the 4 multiplies each term in the bracket: 4 × x = 4x and 4 × 5 = 20, giving 4x + 20.", o="O4"),
      deep=[f1, f2, f3, f4, f5])

# ================================================================== 2.5
s = U.section("2.5", "Constructing and solving equations", ["O5"])
s.idea("An equation is a balance", [
    "An **equation** says two things are equal, like a balance that is level. 2x + 5 = 13 means two bags of x marbles and 5 marbles weigh the same as 13 marbles.",
    "To find x, keep the balance level: whatever you do to one side, do to the other. Take 5 off both sides → 2x = 8. Halve both sides → x = 4.",
    "Always **check** by putting the answer back in: 2 × 4 + 5 = 13 ✓."], fig={"kind": "balance", "left": [["x", 2], ["1", 5]], "right": [["1", 13]], "leftLabel": "2x + 5", "rightLabel": "13"})
s.check(N("Look at the balance before reading on. What is x?", 4, o="O5", hint="Take 5 squares off both pans. How many squares does each x rod balance?"))
s.method("Undo in reverse order", ["Build the expression step by step: start with x, × 2, then + 5.", "To solve, undo the last step first: − 5, then ÷ 2."],
         steps=[("2x + 5 = 13", ""), ("2x = 8", "subtract 5 from both sides"), ("x = 4", "divide both sides by 2"), ("2 × 4 + 5 = 13 ✓", "check")])
s.example("Make the equation first", "Three friends pay the same for tickets plus a $5 booking fee. The total is $41. What does one ticket cost?",
          [("let t = cost of one ticket", "choose a letter for the unknown"), ("3t + 5 = 41", "write the equation from the story"), ("3t = 36", "subtract 5"), ("t = 12", "divide by 3")], "$12")
s.check(N("Solve 4x − 3 = 25.", 7, o="O5", hint="Undo the − 3 first."))
s.mistake("Undo in reverse", ["For 2x + 7 = 19, undo the + 7 first, then the × 2. Dividing first would give x + 7 = 9.5, which is harder and easy to get wrong."])


def q1(r):
    x, b = r.randint(1, 30), r.randint(1, 30)
    return N(f"Solve x + {b} = {x + b}.", x, o="O5")
def q3(r):
    a, x, b = r.randint(2, 9), r.randint(1, 12), r.randint(1, 20)
    return N(f"Solve {a}x + {b} = {a * x + b}.", x, o="O5")
def q4(r):
    a, x, b = r.randint(2, 9), r.randint(2, 12), r.randint(1, 15)
    return N(f"Solve {a}x − {b} = {a * x - b}.", x, o="O5")
def q5(r):
    k, x = r.randint(2, 6), r.randint(2, 12)
    return N(f"Solve x/{k} = {x}.", k * x, o="O5")
def q7(r):
    w = r.randint(2, 12); l = w + r.randint(1, 6)
    return N(f"The perimeter of this rectangle is {2 * (w + l)} cm. Find x.", w, "cm", units=["cm"], o="O5", d="H", fig=RECT(f"x + {l - w}", "x"), reason=f"The perimeter is x + (x + {l - w}) + x + (x + {l - w}) = 4x + {2 * (l - w)}. So 4x + {2 * (l - w)} = {2 * (w + l)}, 4x = {4 * w} and x = {w}.")
def q9(r):
    a, x, b = r.randint(2, 6), r.randint(1, 10), r.randint(1, 10)
    return TB(f"Solve {a}x + {b} = {a * x + b} step by step.", ["Step", "Value"], [[f"{a}x = ", B(a * x)], ["x = ", B(x)]], o="O5")
# --- reasoning
def g1(r):   # which equations have this solution (find all)
    x = r.randint(2, 6)
    rights = [f"{2}x + {x} = {3 * x}", f"{3}x − 1 = {3 * x - 1}", f"x/{x} = 1"]
    wrongs = [f"{2}x + 1 = {2 * x + 3}", f"{4}x = {4 * x + 4}"]
    return MS(f"Select ALL the equations whose solution is x = {x}.", rights, wrongs, o="O5", d="H",
              reason=f"Substitute x = {x} into each. A true equation balances: for example 2 × {x} + {x} = {3 * x}. Two of them do not balance.")
def g2(r):   # spot the error in a solution
    a, x, b = r.randint(2, 6), r.randint(2, 9), r.randint(2, 9); t = a * x + b
    return MC(f"Rui solves {a}x + {b} = {t} like this: {a}x = {t + b}, so x = {(t + b) / a:g}. Where is the mistake?", f"He added {b} instead of subtracting it; x = {x}",
              [(f"He should have divided by {b}", f"The x is multiplied by {a}, so divide by {a}."), ("There is no mistake", f"Check: {a} × {(t + b) / a:g} + {b} is not {t}."), ("He should multiply both sides by 2", "That does not undo + or ×.")],
              o="O5", d="H", reason=f"To undo + {b}, subtract {b} from both sides: {a}x = {t - b}. Then x = {x}. Check: {a} × {x} + {b} = {t} ✓.")
def g3(r):   # construct and solve from a picture/story with a decision
    n = r.randint(3, 9); d = r.randint(2, 6)
    return N(f"Ella is {d} years older than her brother. Together their ages add up to {2 * n + d}. How old is her brother?", n, "years", units=["years"], o="O5", d="H",
             hint="Let her brother be b years old. Write Ella's age, then an equation for the total.", reason=f"Brother b, Ella b + {d}. b + b + {d} = {2 * n + d}, so 2b = {2 * n} and b = {n}. Check: {n} + {n + d} = {2 * n + d} ✓.")
def g4(r):   # balance picture
    a, x, b = r.randint(2, 3), r.randint(2, 6), r.randint(1, 5)
    return N("The balance is level. Each rod weighs x and each square weighs 1. Find x.", x, o="O5", d="H",
             fig={"kind": "balance", "left": [["x", a], ["1", b]], "right": [["1", a * x + b]]}, hint=f"Remove {b} squares from both pans.",
             reason=f"The balance shows {a}x + {b} = {a * x + b}. Remove {b} from both sides: {a}x = {a * x}. Share between {a} rods: x = {x}.")
def g5(r):   # angles in a triangle: equation with decision
    x = r.randint(20, 40)
    return N(f"The angles of a triangle are x°, 2x° and {180 - 3 * x}°. Find x.", x, "°", units=["°"], o="O5", d="VH",
             hint="What do the angles in a triangle add up to?", reason=f"x + 2x + {180 - 3 * x} = 180, so 3x = {3 * x} and x = {x}.")


s.std([q7, q9, q1, q3, q4, q5], EX("Explain how to check that x = 6 is the solution of 3x − 4 = 14.", [("substitute x = 6", ["substitute|put 6|3 ?× ?6"]), ("3 × 6 − 4 = 14, so it is correct", ["18|= ?14|correct|true"])], "Substitute x = 6: 3 × 6 − 4 = 18 − 4 = 14, which matches the right-hand side, so x = 6 is correct.", o="O5"),
      deep=[g1, g2, g3, g4, g5])

# ================================================================== 2.6
s = U.section("2.6", "Inequalities", ["O6"])
s.idea("Comparing, not equalling", [
    "**<** means 'is less than' and **>** means 'is greater than'. The sign opens towards the bigger number: 3 < 8, 10 > −2.",
    "On a number line, numbers get bigger to the right, so −3 > −7 even though 7 looks bigger: −3 is further right.",
    "An inequality like x > 4 describes many numbers at once. On a number line, an **open circle** at 4 shows that 4 itself is not included, and the arrow shows every number to the right."],
    fig={"kind": "numline", "min": 0, "max": 9, "from": {"v": 4, "closed": False}})
s.check(MC("Which sign goes between −3 and −7?  −3 ☐ −7", ">", [("<", "−3 is to the right of −7, so it is greater."), ("=", "They are different numbers.")], o="O6", hint="Picture a number line or a thermometer."))
s.example("Including the end point", "Show x ≤ 5 on a number line.", [("≤ means 'less than or equal to'", "5 is included"), ("filled circle at 5", "filled = included"), ("arrow to the left", "every smaller number")], "● at 5, arrow to the left",
          fig={"kind": "numline", "min": 0, "max": 9, "to": {"v": 5, "closed": True}})
s.mistake("Open or filled", ["x < 5 does not include 5, so the circle is open. x ≤ 5 includes 5: the circle is filled."])


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
def n5(r):
    rows = [("is less than", "<"), ("is greater than", ">"), ("is less than or equal to", "≤"), ("is greater than or equal to", "≥")]
    return GD("Match each phrase to its sign.", "Sign", rows, o="O6")
def n6(r):
    a = r.randint(10, 18)
    return MC(f"You must be at least {a} years old to join a club. Which inequality shows the age, a, of a member?", f"a ≥ {a}", [(f"a > {a}", f"'At least {a}' includes {a}."), f"a ≤ {a}", f"a < {a}"], o="O6", d="H")
# --- reasoning
def h1(r):   # two conditions: find all integers
    lo = r.randint(-4, 3); hi = lo + r.randint(4, 7)
    sol = list(range(lo + 1, hi + 1))
    return MS(f"x is a whole number (it can be negative). x > {lo} and x ≤ {hi}. Select ALL possible values of x.", [str(v) for v in r.sample(sol, min(3, len(sol)))], [str(lo), str(hi + 1)], o="O6", d="H",
              reason=f"x > {lo} leaves out {lo} itself; x ≤ {hi} includes {hi}. So x can be {', '.join(map(str, sol))}.")
def h2(r):   # must be true
    v = r.randint(3, 9)
    return MC(f"If x > {v}, which statement MUST be true?", f"x > {v - 1}", [(f"x > {v + 1}", f"x could be {v}.5, which is not bigger than {v + 1}."), (f"x = {v + 1}", f"x could be {v + 5}."), (f"x < {v + 10}", f"x could be {v + 20}.")],
              o="O6", d="H", hint="Try to find a number that fits x > " + str(v) + " but breaks the statement.", reason=f"Every number bigger than {v} is also bigger than {v - 1}. For each other statement there is a counter-example.")
def h3(r):   # count integers between
    lo, hi = r.randint(-6, 2), None; hi = lo + r.randint(4, 9)
    return N(f"How many whole numbers x satisfy {lo} < x < {hi}?", hi - lo - 1, o="O6", d="H", hint="Neither end is included. List them if you are unsure.",
             reason=f"The numbers are {', '.join(str(v) for v in range(lo + 1, hi))}: that is {hi - lo - 1}. (Not {hi - lo}, because both ends are left out.)")
def h4(r):   # real context, choose sign and end point
    c = r.randint(6, 12)
    return MC(f"A lift can carry at most {c} people. p is the number of people in the lift. Which inequality is correct?", f"p ≤ {c}", [(f"p < {c}", f"{c} people is allowed."), (f"p ≥ {c}", "That says at least, not at most."), (f"p > {c}", "That is too many people.")],
              o="O6", d="H", reason=f"'At most {c}' means {c} or fewer, so p ≤ {c} (and p is a whole number, at least 0).")
def h5(r):   # spot error on number line
    v = r.randint(2, 8)
    return MC(f"Zara draws x < {v} with a filled circle at {v} and an arrow to the left. What is wrong?", f"The circle should be open, because {v} is not included",
              [("The arrow should point right", f"Numbers less than {v} are to the left."), ("Nothing is wrong", f"A filled circle would include {v}."), (f"The circle should be at {v - 1}", f"The boundary is {v}, even though it is not included.")],
              o="O6", d="H", fig={"kind": "numline", "min": 0, "max": 10, "to": {"v": v, "closed": True}}, reason=f"'<' means strictly less than, so {v} is not part of the answer: use an open circle at {v}.")


s.std([n2, n5, n1, n3, n6], EX("Explain the difference between x > 3 and x ≥ 3.", [("x > 3 does not include 3", ["not include|open|bigger than 3"]), ("x ≥ 3 includes 3", ["includes|can be 3|equal|filled"])], "x > 3 means bigger than 3, so 3 itself is not included (open circle). x ≥ 3 means 3 or bigger, so 3 is included (filled circle).", o="O6"),
      deep=[h1, h2, h3, h4, h5])

U.mindmap(("Expressions", "Letters for numbers • 3n, n + 3, n/2", "O1", "2.1"), ("Substitution", "Replace letters • order of operations", "O2", "2.2"),
          ("Like terms", "Same letters • add their numbers", "O3", "2.3"), ("Expanding", "Multiply every term", "O4", "2.4"),
          ("Equations", "Same to both sides • check", "O5", "2.5"), ("Inequalities", "< > ≤ ≥ • open or filled circle", "O6", "2.6"))
