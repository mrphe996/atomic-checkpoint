# -*- coding: utf-8 -*-
"""Stage 7 · Unit 9 – Camday book pages (the 'Read the PDF' step). Camday's own text, numbers, examples and drawings:
topics and question types follow the Stage 7 curriculum; nothing is copied from any published book."""
from maths_notes_v4.kit4 import BK, Ex, tiles
from maths_notes_v4.s7_u09 import NOTES as N

NOTES = {}

N[(9, "9.1")]["book"] = BK(
    keys=[("sequence", "a list of numbers in a set order"), ("term", "each number in a sequence"), ("consecutive terms", "terms next to each other"),
          ("term-to-term rule", "how to get from one term to the next"), ("infinite sequence", "goes on forever (ends with …)"), ("finite sequence", "stops after a number of terms")],
    intro=["A sunflower seedling is 4 cm tall. It grows 3 cm every week. Its height each week makes the list 4, 7, 10, 13, … This list is a **sequence**, and each number in it is a **term**.",
           "4 and 7 are **consecutive terms**, so are 7 and 10. Each term is 3 more than the one before, so the **term-to-term rule** is 'add 3'.",
           "The three dots show that the sequence carries on forever: it is an **infinite sequence**. A list such as 4, 7, 10, 13 with no dots stops after four terms: it is a **finite sequence**.",
           "A rule can have **two steps**, for example 'divide by 2, then add 6'. Always do the steps in the order given, and always start from the term you have just found."],
    examples=[("Example 1 – a lift going down", "A lift stops at floors 25, 22, 19, … It goes down the same number of floors each time. Write the rule and the next two stops.",
               [("Rule: subtract 3", "22 − 25 = −3 and 19 − 22 = −3"), ("19 − 3 = 16, 16 − 3 = 13", "keep subtracting 3"), ("Next two stops: 16 and 13", "")]),
              ("Example 2 – a two-step rule", "The first term is 10. The rule is 'divide by 2, then add 6'. Write the first three terms.",
               [("1st term = 10", "given"), ("2nd term = 10 ÷ 2 + 6 = 5 + 6 = 11", "divide first, then add"), ("3rd term = 11 ÷ 2 + 6 = 5.5 + 6 = 11.5", "start from the 2nd term, 11"),
                ("10, 11, 11.5", "terms do not have to be whole numbers")])],
    exercise=[
        Ex("Odd one out. Two of these sequences follow the rule 'add 4'. Which one does not, and which term breaks the rule?", ans="(b) 20, 24, 28, 33: 28 + 4 = 32, not 33.",
           *[("3, 7, 11, 15", ""), ("20, 24, 28, 33", ""), ("−2, 2, 6, 10", "")]),
        Ex("A bus leaves the station at 6:10 and then every 25 minutes. Write the times of the next four buses.", ans="6:35, 7:00, 7:25, 7:50"),
        Ex("For each sequence, write the term-to-term rule and the 6th term.", ("0.5, 1, 1.5, 2, …", "add 0.5; 3"), ("81, 27, 9, 3, …", "divide by 3; 1/9"),
           ("−10, −7, −4, −1, …", "add 3; 5"), ("1000, 100, 10, 1, …", "divide by 10; 0.01")),
        Ex("Build a sequence of five terms that fits each description.", ("The rule is 'subtract 6' and the 3rd term is 0.", "12, 6, 0, −6, −12"),
           ("The rule is 'multiply by 2' and the 5th term is 48.", "3, 6, 12, 24, 48"), ("The rule is 'multiply by 2, then subtract 3' and the 1st term is 4.", "4, 5, 7, 11, 19"),
           tip="Start where you know a term, then go right with the rule and left with its inverse."),
        Ex("Is each list finite or infinite?", ("the number of seats in each row of a theatre with 12 rows", "finite"), ("the even numbers", "infinite"),
           ("the dates in March", "finite"), ("the multiples of 7", "infinite")),
        Ex("A sequence starts 1, 4, … Find a rule that makes the 3rd term 7, a rule that makes it 16, and a rule that makes it 13.",
           ans="add 3 → 7; multiply by 4 → 16; multiply by 3, then add 1 → 13 (1 × 3 + 1 = 4, 4 × 3 + 1 = 13).", think=True),
        Ex("Work backwards.", ("The rule is 'add 9' and the 5th term is 50. What is the 1st term?", "14"),
           ("The rule is 'multiply by 3, then add 1' and the 3rd term is 40. What is the 1st term?", "4 (40 − 1 = 39, 39 ÷ 3 = 13; 13 − 1 = 12, 12 ÷ 3 = 4)"),
           tip="With a two-step rule, undo the last step first."),
        Ex("Invent a two-step rule. Give a partner the 1st term, the 2nd term and the 3rd term, and ask them to find your rule. Can they find a different rule that also fits?",
           ans="Answers will vary. Three terms usually fix a simple rule; two terms do not.", think=True),
    ],
    check=["Can I find and use a term-to-term rule, including a two-step rule?", "Can I tell a finite sequence from an infinite one?", "Can I work backwards to an earlier term?"],
    look=["Example 2 shows that terms do not have to be whole numbers.", "In Question 4, decide first which way you are moving: right with the rule, left with its inverse."],
    note="Read the words to know and both examples, then do the practice on paper.")

N[(9, "9.2")]["book"] = BK(
    keys=[("pattern", "a picture made of shapes, dots or sticks"), ("sequence of patterns", "patterns that grow by the same rule"), ("term-to-term rule", "how the count changes from one pattern to the next")],
    intro=["In a school canteen, square tables are pushed together in a row. One table seats 6 people, two tables seat 10 and three tables seat 14. Each extra table adds 4 seats: 2 on each long side.",
           "Counting the pieces in a sequence of patterns gives a number sequence: 6, 10, 14, … Look at the **picture** to explain the rule: here each new table adds 4 places.",
           "To find a pattern far along the sequence, you do not need to draw every pattern. Count how many steps it is from Pattern 1 and add the same amount each step."],
    examples=[("Example – squares of matchsticks", "Squares are made from matchsticks in a row: Pattern 1 uses 4, Pattern 2 uses 7, Pattern 3 uses 10. How many matchsticks are in Pattern 4, and why?",
               [("Pattern 4: 13 matchsticks", "one more square on the end"), ("Rule: add 3", "4, 7, 10, 13"),
                ("Each new square shares a side with the last one, so it needs only 3 new matchsticks.", "explain with the picture")])],
    exercise=[
        Ex("A garden fence is built in sections. 1 section uses 2 posts and 3 rails (5 pieces). Each new section adds 1 post and 3 rails.", ("Write the number of pieces for 1, 2, 3, 4 and 5 sections.", "5, 9, 13, 17, 21"),
           ("Write the term-to-term rule and explain it using the fence.", "add 4: each section adds 1 post and 3 rails"), ("How many pieces are needed for 12 sections?", "5 + 11 × 4 = 49")),
        Ex("Hexagons made from matchsticks are joined in a chain, sharing one side each time: 6, 11, 16, … matchsticks.", ("How many matchsticks does each new hexagon add? Why?", "5 – one of its 6 sides is shared"),
           ("How many hexagons are in a chain that uses 51 matchsticks?", "10 (51 − 6 = 45, 45 ÷ 5 = 9 more hexagons)")),
        Ex("This tile pattern is 2 tiles high.", ("Write the number of tiles in Patterns 1 to 4.", "4, 6, 8, 10"), ("Without drawing it, find the number of tiles in Pattern 20.", "42 (a 2 by 21 rectangle)"),
           fig=tiles([(c, r) for c in range(2) for r in range(2)], [(c, r) for c in range(3) for r in range(2)], [(c, r) for c in range(4) for r in range(2)])),
        Ex("Square patterns of tiles have 1, 4, 9, 16, … tiles. Explain why this sequence does not have an 'add' rule.", ans="The differences are 3, 5, 7: each new square adds a bigger border than the last, so the amount added is not the same each time."),
        Ex("Pattern 3 of a sequence has 7 tiles and Pattern 7 has 19 tiles. The same number of tiles is added each time. How many tiles are in Pattern 1?",
           ans="From Pattern 3 to Pattern 7 is 4 steps adding 12, so each step adds 3. Pattern 1 = 7 − 2 × 3 = 1 tile.", think=True),
        Ex("A pattern starts with 6 pieces and adds 4 each time. Can a pattern ever have 100 pieces? Explain.", ans="No. 100 − 6 = 94 and 94 ÷ 4 = 23.5, not a whole number of steps.", think=True),
        Ex("Design your own growing pattern from a shape you choose. Draw the first four patterns, write the sequence, and find the number of shapes in Pattern 15.", ans="Answers will vary."),
    ],
    check=["Can I write the sequence for a growing pattern?", "Can I explain the rule using the picture?", "Can I find a pattern far along without drawing every one?"],
    look=["In the example, notice WHY only 3 matchsticks are added each time.", "Questions 5 and 6 can be solved by counting steps – no drawing needed."],
    note="Read the canteen example and the matchstick example, then do the practice on paper.")

N[(9, "9.3")]["book"] = BK(
    keys=[("position number", "where a term is in the sequence: 1st, 2nd, 3rd, …"), ("nth term", "the term in position n"), ("nth term rule", "a rule that gives any term from its position")],
    intro=["Kofi saves $5 every week. After week 1 he has $5, after week 2 $10, after week 3 $15. After week n he has **5 × n** dollars. You can write this as **nth term = 5n**.",
           "In a table, put the position numbers 1, 2, 3, … above the terms. If the terms are a times table, the rule multiplies: 6, 12, 18, … has nth term 6n.",
           "If each term is a fixed amount more than its position, the rule adds: 9, 10, 11, … is 8 more than 1, 2, 3, …, so the nth term is n + 8. If the terms are less than the positions, the rule subtracts: −2, −1, 0, … has nth term n − 3.",
           "To find any term, replace n by its position. To find which position a number has, undo the rule."],
    examples=[("Example 1 – a times table", "Find the nth term rule of 11, 22, 33, 44, … and its 30th term.",
               [("Positions 1, 2, 3, 4 → 11, 22, 33, 44", "the 11 times table"), ("nth term = 11n", "term = 11 × position"), ("30th term = 11 × 30 = 330", "replace n by 30")]),
              ("Example 2 – a fixed amount more", "Find the nth term rule of 6, 7, 8, 9, … and its 40th term.",
               [("6 − 1 = 5, 7 − 2 = 5, 8 − 3 = 5", "each term is 5 more than its position"), ("nth term = n + 5", ""), ("40th term = 40 + 5 = 45", "")])],
    exercise=[
        Ex("Notebooks cost $4 each.", ("Write the cost of n notebooks as an nth term rule.", "4n"), ("How much do 25 notebooks cost?", "$100"), ("How many notebooks can you buy for exactly $68?", "17")),
        Ex("Find the nth term rule of each sequence. Check it with two positions.", ("14, 28, 42, 56, …", "14n"), ("21, 22, 23, 24, …", "n + 20"), ("−7, −6, −5, −4, …", "n − 8"), ("100, 200, 300, 400, …", "100n")),
        Ex("Copy and complete the grid.", ("n + 30: terms for n = 1, 12, 40", "31, 42, 70"), ("n − 12: terms for n = 1, 12, 40", "−11, 0, 28"), ("9n: terms for n = 1, 12, 40", "9, 108, 360")),
        Ex("Find the position of each term.", ("9n = 108", "12th"), ("n + 30 = 75", "45th"), ("n − 12 = 0", "12th")),
        Ex("Sort the numbers 30, 41, 55, 66, 90, 121.", ("Which are terms of 11n?", "55, 66, 121"), ("Which are terms of n + 40?", "41, 55, 66, 90, 121"), ("Which are terms of 3n?", "30, 66, 90"),
           tip="For an: is it a multiple of a? For n + a: is it bigger than a?"),
        Ex("Two sequences have nth terms 5n and n + 20. At which position are their terms equal? After that, which sequence is bigger?", ans="n = 5 (both 25). After that 5n is bigger, because it grows by 5 each step and n + 20 grows by 1.", think=True),
        Ex("A sequence has nth term n − 9. Which is the first positive term, and what is its position?", ans="The 10th term, 1."),
        Ex("Kai writes the nth term of 30, 31, 32, 33, … as 30n. Show that he is wrong and write the correct rule.", ans="30n gives 30, 60, 90 – it goes up in 30s. Each term is 29 more than its position, so the rule is n + 29.", think=True),
    ],
    check=["Can I find the nth term rule of a sequence like 7, 14, 21, … or 9, 10, 11, …?", "Can I use an nth term rule to find any term?", "Can I find the position of a term?"],
    look=["Compare Examples 1 and 2: which one is a times table, and which one goes up by 1?", "Question 5: think about what every term of 11n has in common."],
    note="Read the two examples, then do the practice on paper.")

N[(9, "9.4")]["book"] = BK(
    keys=[("function", "a rule that links inputs to outputs"), ("function machine", "a diagram of the rule in a box"), ("input / output", "the number that goes in / comes out"),
          ("inverse operation", "the operation that undoes another"), ("mapping diagram", "two number lines with arrows from inputs to outputs"), ("maps to", "an input maps to its output")],
    intro=["A pancake recipe uses 3 eggs for each batch. Batches → × 3 → eggs is a **function machine**: 2 batches need 6 eggs, 5 batches need 15 eggs.",
           "The numbers going in are **inputs** and the numbers coming out are **outputs**. A machine with one operation is a **one-step** function machine. We say 2 **maps to** 6.",
           {"fig": {"kind": "mapping", "min": 0, "max": 10, "pairs": [[1, 3], [2, 6], [3, 9]]}},
           "A **mapping diagram** shows the same function with arrows from the input line to the output line.",
           "To find an input from an output, use the **inverse operation**: to undo × 3, divide by 3. 12 eggs → 12 ÷ 3 = 4 batches."],
    examples=[("Example 1 – forwards and backwards", "Input → + 6 → output. Find the outputs for inputs 2 and 5, and the input for output 15.",
               [("2 + 6 = 8, 5 + 6 = 11", "outputs: put the inputs through the machine"), ("15 − 6 = 9", "input: the inverse of + 6 is − 6"), ("2 → 8, 5 → 11, 9 → 15", "")]),
              ("Example 2 – one inverse machine for many outputs", "Input → × 5 → output. The outputs are 15, 35 and 50. Find the inputs.",
               [("Inverse machine: output → ÷ 5 → input", "write it once"), ("15 ÷ 5 = 3, 35 ÷ 5 = 7, 50 ÷ 5 = 10", "use it for each output")])],
    exercise=[
        Ex("Input → − 4 → output. Copy and complete the table.", ("inputs 10 and 7: outputs?", "6, 3"), ("outputs 11 and 0: inputs?", "15, 4")),
        Ex("Metres → × 100 → centimetres.", ("Convert 3 m and 0.5 m.", "300 cm, 50 cm"), ("Which input gives 250 cm?", "2.5 m")),
        Ex("The mapping diagram shows a one-step function: 2 → 7, 3 → 8, 6 → 11.", ("Write the function.", "+ 5"), ("Where does the arrow from 0 end?", "at 5"),
           fig={"kind": "mapping", "min": 0, "max": 12, "pairs": [[2, 7], [3, 8], [6, 11]]}),
        Ex("Odd one out: three of these pairs come from '× 3'. Which pair does not?", ans="5 → 16 (5 × 3 = 15)", *[("2 → 6", ""), ("4 → 12", ""), ("5 → 16", ""), ("7 → 21", "")]),
        Ex("A one-step machine changes 6 into 2.", ("Give two possible machines.", "÷ 3 or − 4"), ("Which extra pair would decide between them? Explain.", "e.g. 9 → 3 shows ÷ 3, because 9 − 4 = 5"), think=True),
        Ex("Design a one-step machine that maps 0 to 0 and 5 to 20. Is there more than one answer?", ans="× 4. Only one: + or − cannot keep 0 at 0 unless they add 0, and ÷ would make 5 smaller.", think=True),
        Ex("A bakery packs buns by the dozen: dozens → × 12 → buns.", ("How many buns are in 6 dozen?", "72"), ("How many dozen is 84 buns?", "7")),
    ],
    check=["Can I find outputs of a function machine?", "Can I find inputs using the inverse operation?", "Can I read and draw a mapping diagram?", "Can I find a one-step function from inputs and outputs?"],
    look=["In Example 2, notice that one inverse machine is used for all three outputs.", "Question 5: why is one pair not enough?"],
    note="Read the pancake example and both examples, then do the practice on paper.")
