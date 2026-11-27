# -*- coding: utf-8 -*-
"""Stage 7 · Unit 2 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, J, JJ, TEST, SQ, GREY, GREEN, BLUE, RED

PAUSE = lambda sid, say, html: dict(say=say, pause=sid, do=[dict(a="pausecard", html=html, at=0.2)])
LINES = lambda who, q, lines: [T(f"{who}'s working for **{q}**:", x=80, y=160)] + [T(f"Line {i + 1}: {l}", x=110, y=240 + 70 * i, id=f"l{i + 1}") for i, l in enumerate(lines)]
BRICK = lambda label, color, w=110: f'<span style="display:inline-flex;align-items:center;justify-content:center;width:{w}px;height:56px;margin-right:6px;border-radius:8px;background:{color};color:#fff;font-weight:700">{label}</span>'
RB, BB = BRICK("x", RED), BRICK("y", BLUE, 150)

VIDEOS = {}

VIDEOS["2.1"] = [
    dict(kind="hook", title="Mystery boxes", steps=[
        dict(say="Here is a box of pencils. We don't know how many pencils are inside, so we call that number n.",
             do=[E("📦", 90, 170, 100), T("one box holds **n** pencils", x=230, y=205)]),
        dict(say="Sara has 3 full boxes, and 2 loose pencils.",
             do=[E("📦", 90, 320, 90), E("📦", 200, 320, 90, at=0.3), E("📦", 310, 320, 90, at=0.6), E("✏️", 450, 335, 60, at=1.8), E("✏️", 520, 335, 60, at=2.1)]),
        PAUSE("2.1-k1", "How could you write the number of pencils she has, without knowing n? Pause the video and choose.",
              "3 boxes of n pencils and 2 loose pencils. Which expression shows the total?"),
    ]),
    dict(kind="hook", title="3 boxes and 2 more", steps=[
        dict(say="Each box holds n pencils. So 3 boxes hold n plus n plus n. That is 3 times n.",
             do=[MATH("n + n + n", x=80, y=180), MATH("= 3 × n", x=380, y=180, at=3.2, color=BLUE)]),
        dict(say="In algebra we write 3 times n as 3 n. The number goes first, and we leave out the times sign.",
             do=[B("3n", x=640, y=172, color=BLUE), T("number first, no × sign", x=760, y=190, color=GREY, at=2)]),
        dict(say="Then add the 2 loose pencils. Sara has 3 n plus 2 pencils.", do=[B("3n + 2", x=80, y=320, color=GREEN), E("✏️", 330, 320, 60, at=1)]),
        dict(say="If a box holds 10 pencils, that is 3 times 10, plus 2, which is 32. The same expression works for any box.",
             do=[T("If n = 10:", x=80, y=450, color=GREY), MATH("3 × 10 + 2 = 32", x=260, y=442, at=1.6)]),
    ]),
    dict(kind="recall", title="Order of operations", steps=[
        dict(say="Remember the order of operations. Multiply and divide before you add and subtract.", do=[T("× and ÷ come **before** + and −", x=80, y=170)]),
        dict(say="3 times 4, plus 2, is 12 plus 2, which is 14.", do=[MATH("3 × 4 + 2 = 14", x=80, y=270)]),
        dict(say="But with brackets, the brackets come first. 3 times, bracket, 4 plus 2, is 3 times 6, which is 18.",
             do=[MATH("3 × (4 + 2) = 18", x=80, y=370, color=BLUE), T("brackets first", x=520, y=378, color=GREY, at=1.6)]),
    ]),
    dict(kind="idea", title="The words of algebra", steps=[
        dict(say="A letter that stands for an unknown number is called a variable.", do=[B("3n + 2", x=80, y=160), T("**n** is a **variable**", x=420, y=178)]),
        dict(say="3 n plus 2 is called an expression. It has numbers and letters, but no equals sign.", do=[T("an **expression**: no equals sign", x=420, y=258)]),
        dict(say="The parts that are added are called terms. Here the terms are 3 n, and 2.", do=[T("**terms**: 3n and 2", x=420, y=338)]),
        dict(say="The number in front of the letter, 3, is the coefficient. A number on its own, like 2, is a constant.",
             do=[T("**coefficient**: 3", x=420, y=418), T("**constant**: 2", x=760, y=418, at=3.4)]),
    ]),
    dict(kind="idea", title="From words to expressions", steps=[
        dict(say="Let's turn words into algebra. 5 more than n is n plus 5.",
             do=[dict(a="table", id="t", head=["Words", "Expression"], x=80, y=150,
                      rows=[["5 more than n", "n + 5"], ["4 less than n", "n − 4"], ["double n", "2n"], ["n divided by 3", "$$\\frac{n}{3}$$"], ["n times itself", "n²"], ["3 more than double n", "2n + 3"], ["double (n plus 3)", "2(n + 3)"]]),
                 dict(a="row", id="t", i=0, at=2)]),
        dict(say="4 less than n is n minus 4. Start with n, then take 4 away.", do=[dict(a="row", id="t", i=1, at=0.2)]),
        dict(say="Double n is 2 n. And n divided by 3 is written as a fraction: n over 3.", do=[dict(a="row", id="t", i=2, at=0.2), dict(a="row", id="t", i=3, at=2)]),
        dict(say="n times itself is n squared.", do=[dict(a="row", id="t", i=4, at=0.2)]),
        dict(say="3 more than double n is 2 n plus 3. But double, bracket, n plus 3, needs brackets, because the adding is done first.",
             do=[dict(a="row", id="t", i=5, at=0.2), dict(a="row", id="t", i=6, at=3.4)]),
        PAUSE("2.1-k2", "Your turn. Which expression means: double y, then add 9? Pause the video and choose.", "Which expression means “double y, then add 9”?"),
    ]),
    dict(kind="idea", title="Check: double y, then add 9", steps=[
        dict(say="Double y is 2 y. Then add 9. The expression is 2 y plus 9. No brackets are needed, because the doubling is done first.",
             do=[MATH("2y", x=80, y=190), MATH("2y + 9", x=80, y=290, at=2.2, color=GREEN), T("doubling first → no brackets", x=420, y=298, color=GREY, at=5)]),
    ]),
    dict(kind="idea", title="Expression or equation?", steps=[
        dict(say="An expression has no equals sign. 4 x plus 1 is an expression.", do=[MATH("4x + 1", x=80, y=170), T("expression", x=420, y=178, color=BLUE)]),
        dict(say="An equation has an equals sign. 4 x plus 1 equals 9 is an equation. It is only true when x is 2.",
             do=[MATH("4x + 1 = 9", x=80, y=270), T("equation: true when x = 2", x=420, y=278, color=RED, at=1.6)]),
        dict(say="Two expressions are equivalent if they are always equal. n plus n plus n is always the same as 3 n.",
             do=[MATH("n + n + n", x=80, y=390), T("is **equivalent** to", x=360, y=398), MATH("3n", x=660, y=390, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I write an expression?", steps=[
        dict(say="Here is the method. Step 1: choose a letter for the unknown, or use the one you are given.", do=[T("1. Choose a **letter** for the unknown", x=80, y=170)]),
        dict(say="Step 2: find the operations in the words. More means add. Less means subtract. Times or double means multiply. Shared means divide.",
             do=[T("2. more → **+**   less → **−**   double → **×**   shared → **÷**", x=80, y=260)]),
        dict(say="Step 3: put them in the right order. Use brackets if something must be done first.", do=[T("3. Right order; **brackets** for what is done first", x=80, y=350)]),
        dict(say="Step 4: test your expression with an easy number.", do=[T("4. **Test** with an easy number", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Cinema tickets", steps=[
        dict(say="A cinema ticket costs t dollars. Popcorn costs 4 dollars. Write an expression for 2 tickets and 1 popcorn.",
             do=[E("🎟️", 90, 165, 80), T("ticket: **$t**", x=200, y=190), E("🍿", 520, 165, 80, at=2.4), T("popcorn: **$4**", x=630, y=190, at=2.4)]),
        dict(say="2 tickets cost 2 times t, which is 2 t.", do=[MATH("2 × t = 2t", x=80, y=310)]),
        dict(say="Add the popcorn. The total is 2 t plus 4 dollars.", do=[B("2t + 4", x=80, y=410, color=GREEN)]),
        dict(say="Test it. If a ticket costs 6 dollars, 2 tickets and popcorn cost 12 plus 4, which is 16 dollars. That makes sense.",
             do=[T("If t = 6:", x=80, y=520, color=GREY), MATH("2 × 6 + 4 = 16", x=260, y=512, at=2.6), E("✅", 640, 500, 50, at=5.6)]),
    ]),
    dict(kind="example", title="Brackets matter", steps=[
        dict(say="Compare two instructions. First: add 5 to x, then multiply by 3.", do=[T("(a) add 5 to x, **then** multiply by 3", x=80, y=170)]),
        dict(say="The adding is done first, so it goes in brackets. We write 3, bracket, x plus 5.", do=[B("3(x + 5)", x=80, y=250, color=BLUE)]),
        dict(say="Second: multiply x by 3, then add 5.", do=[T("(b) multiply x by 3, **then** add 5", x=80, y=370)]),
        dict(say="Multiplying comes first anyway, so no brackets. We write 3 x plus 5.", do=[B("3x + 5", x=80, y=450, color=RED)]),
        dict(say="They are different. When x is 1, the first gives 18 and the second gives 8.",
             do=[T("x = 1 → 18", x=420, y=268, color=GREY), T("x = 1 → 8", x=420, y=468, color=GREY, at=2.4)]),
        PAUSE("2.1-k3", "Your turn. Write an expression for: p shared equally between 4, then add 1. Pause and write it.", "Write an expression for “p shared equally between 4, then add 1”."),
    ]),
    dict(kind="example", title="Check: p shared between 4, then add 1", steps=[
        dict(say="Shared between 4 means divide by 4. That is p over 4. Then add 1. The expression is p over 4, plus 1.",
             do=[MATH("$$\\frac{p}{4}$$", x=80, y=190), MATH("$$\\frac{p}{4} + 1$$", x=80, y=330, at=3.6, color=GREEN)]),
    ]),
    dict(kind="example", title="Perimeter", steps=[
        dict(say="A rectangle is a centimetres long and b centimetres wide. What is its perimeter?",
             do=[T('<span style="display:inline-block;width:300px;height:170px;border:5px solid #2F6FEB;background:#DCE8FF;border-radius:6px"></span>', x=90, y=170),
                 T("a", x=230, y=350, color=BLUE), T("b", x=410, y=240, color=BLUE)]),
        dict(say="Add all four sides: a plus b plus a plus b.", do=[MATH("a + b + a + b", x=560, y=190)]),
        dict(say="There are two a's and two b's. So the perimeter is 2 a plus 2 b.", do=[B("2a + 2b", x=560, y=300, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Tom writes 6 less than p as an expression. Which line goes wrong first?",
             do=LINES("Tom", "6 less than p", ["“less than” means subtract", "start with 6, subtract p", "6 − p"])),
        dict(say="Line 2 is wrong. 6 less than p starts with p, and takes 6 away.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="The correct expression is p minus 6. Test it with p equals 10. 6 less than 10 is 4, and 10 minus 6 is 4.",
             do=[B("p − 6", x=110, y=480, color=GREEN), T("p = 10:  10 − 6 = 4 ✓", x=420, y=498, color=GREY, at=3)]),
    ]),
    dict(kind="life", title="Where the word algebra comes from", steps=[
        dict(say="Algebra is very old. About 1,200 years ago, a scholar in Baghdad called al-Khwarizmi wrote a famous book about solving problems with unknown numbers.",
             do=[E("📜", 90, 170, 100), T("About **1 200 years ago**, in Baghdad: al-Khwarizmi's book", x=220, y=200)]),
        dict(say="Part of the book's title was the Arabic word al-jabr. That is where our word algebra comes from.",
             do=[B("al-jabr → algebra", x=220, y=310, color=BLUE)]),
        dict(say="Today, the same idea is used in every spreadsheet and computer program: a name stands for a number that can change.",
             do=[E("💻", 90, 420, 90), T("spreadsheets and code use **variables** too", x=220, y=445)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.1-k4", "One last question. Which of these is an equation? Pause the video and choose.", "Which of these is an equation?"),
        dict(say="An equation has an equals sign. So 2 x plus 1 equals 7 is the equation. The others are expressions.",
             do=[MATH("2x + 1 = 7", x=80, y=190, color=GREEN), T("it has an **equals sign**", x=420, y=198, at=1.6), E("✅", 800, 180, 56, at=2.6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: a letter stands for an unknown number. 3 n means 3 times n.", do=[T("• A letter is a **variable**; 3n means 3 × n", x=80, y=170)]),
        dict(say="An expression has terms, but no equals sign.", do=[T("• An expression has terms, no equals sign", x=80, y=250)]),
        dict(say="4 less than n is n minus 4. Brackets show what is done first.", do=[T("• “4 less than n” is n − 4; brackets = done first", x=80, y=330)]),
        dict(say="Equivalent expressions are equal for every value of the letter.", do=[T("• Equivalent = equal for **every** value", x=80, y=410)]),
    ]),
]

VIDEOS["2.2"] = [
    dict(kind="hook", title="A phone plan", steps=[
        dict(say="A phone plan costs 12 dollars a month, plus 10 cents for every text you send.",
             do=[E("📱", 90, 170, 100), T("**$12** a month", x=220, y=190), T("+ **$0.10** for every text", x=220, y=260, at=2.2)]),
        dict(say="This month you send 50 texts.", do=[E("💬", 90, 350, 80), T("50 texts", x=220, y=375)]),
        PAUSE("2.2-k1", "How much is the bill? Pause the video and work it out.", "$12 a month plus $0.10 per text. What is the bill for 50 texts, in dollars?"),
    ]),
    dict(kind="hook", title="A rule for any month", steps=[
        dict(say="50 texts at 10 cents each cost 5 dollars. Add the 12 dollars. The bill is 17 dollars.",
             do=[MATH("50 × 0.10 = 5", x=80, y=180), MATH("12 + 5 = 17", x=80, y=280, at=3, color=GREEN), B("$17", x=480, y=272, color=GREEN, at=4.4)]),
        dict(say="We can write one rule that works for any number of texts. Call the number of texts t, and the cost C.",
             do=[T("t = number of texts,  C = cost in dollars", x=80, y=400, color=GREY)]),
        dict(say="C equals 12 plus 0.1 times t. A rule like this is called a formula.", do=[B("C = 12 + 0.1t", x=80, y=480, color=BLUE), T("a **formula**", x=520, y=498, at=3)]),
    ]),
    dict(kind="recall", title="Expressions", steps=[
        dict(say="Remember: 3 n means 3 times n.", do=[MATH("3n = 3 × n", x=80, y=170)]),
        dict(say="In 2 a plus 5, you multiply a by 2 first, then add 5.", do=[MATH("2a + 5", x=80, y=270), T("× first, then +", x=380, y=278, color=GREY, at=1.4)]),
    ]),
    dict(kind="idea", title="Substitution", steps=[
        dict(say="To substitute means to replace a letter with a number, and then work out the value.", do=[T("**Substitute** = replace the letter with a number", x=80, y=160)]),
        dict(say="Take 3 a plus 2, when a is 4. Replace a with 4: 3 times 4, plus 2. That is 14.",
             do=[dict(a="table", id="t", head=["Expression", "a = 4", "a = 10"], x=80, y=250,
                      rows=[["3a + 2", "3 × 4 + 2 = **14**", "3 × 10 + 2 = **32**"], ["a²", "4 × 4 = **16**", "10 × 10 = **100**"], ["5(a − 1)", "5 × 3 = **15**", "5 × 9 = **45**"]]),
                 dict(a="row", id="t", i=0, at=1.6)]),
        dict(say="a squared, when a is 4, is 4 times 4, which is 16. When a is 10, it is 100.", do=[dict(a="row", id="t", i=1, at=0.3)]),
        dict(say="5, bracket, a minus 1. Do the bracket first. When a is 4, that is 5 times 3, which is 15.", do=[dict(a="row", id="t", i=2, at=0.3)]),
        PAUSE("2.2-k2", "Your turn. Find the value of 2 a plus 7, when a is 9. Pause the video and try it.", "Find 2a + 7 when a = 9."),
    ]),
    dict(kind="idea", title="Check: 2a + 7 when a = 9", steps=[
        dict(say="Replace a with 9. 2 times 9 is 18. 18 plus 7 is 25.",
             do=[MATH("2 × 9 + 7", x=80, y=190), MATH("= 18 + 7", x=80, y=280, at=1.8), B("= 25", x=80, y=370, color=GREEN, at=3.4)]),
    ]),
    dict(kind="idea", title="Formulae", steps=[
        dict(say="A formula is a rule that links two or more quantities. It has an equals sign, and one letter on its own, called the subject.",
             do=[B("C = 12 + 0.1t", x=80, y=160, color=BLUE), T("**C** is the **subject**", x=560, y=178, at=4.2)]),
        dict(say="You can write a formula in words, or in letters. Letters are shorter and easier to use.",
             do=[T("cost = 12 + 0.10 × number of texts", x=80, y=280, color=GREY)]),
        dict(say="For 200 texts, substitute t equals 200. C is 12 plus 0.1 times 200. That is 12 plus 20, so 32 dollars.",
             do=[MATH("C = 12 + 0.1 × 200", x=80, y=380, at=1.6), MATH("= 12 + 20 = 32", x=80, y=470, at=5, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I substitute?", steps=[
        dict(say="Here is the method. Step 1: write the expression again, with each letter replaced by its number.", do=[T("1. **Replace** each letter with its number", x=80, y=170)]),
        dict(say="Step 2: put in the times signs that were hidden. 3 a becomes 3 times a.", do=[T("2. Put the hidden **×** back: 3a → 3 × a", x=80, y=260)]),
        dict(say="Step 3: work it out in the right order: brackets, powers, multiply and divide, then add and subtract.",
             do=[T("3. Order: brackets → powers → × ÷ → + −", x=80, y=350)]),
        dict(say="Step 4: write the units, if there are any.", do=[T("4. Write the **units**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Two letters", steps=[
        dict(say="Find the value of 3 x plus 2 y, when x is 5 and y is 4.", do=[B("3x + 2y", x=80, y=160), T("x = 5, y = 4", x=420, y=178, color=GREY)]),
        dict(say="Replace each letter. 3 times 5, plus 2 times 4.", do=[MATH("3 × 5 + 2 × 4", x=80, y=270)]),
        dict(say="Multiply first. 15 plus 8.", do=[MATH("= 15 + 8", x=80, y=360)]),
        dict(say="The answer is 23.", do=[B("= 23", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="example", title="Powers and brackets", steps=[
        dict(say="Be careful with squares. Find 2 m squared, when m is 3.", do=[B("2m²", x=80, y=160), T("m = 3", x=300, y=178, color=GREY)]),
        dict(say="Only the m is squared. 3 squared is 9, and 2 times 9 is 18.", do=[MATH("2 × 3² = 2 × 9 = 18", x=80, y=260, color=BLUE)]),
        dict(say="Now find, bracket, 2 m, all squared. This time the bracket comes first. 2 times 3 is 6, and 6 squared is 36.",
             do=[B("(2m)²", x=80, y=380), MATH("(2 × 3)² = 6² = 36", x=80, y=470, at=3.4, color=RED)]),
        PAUSE("2.2-k3", "Your turn. Find x y minus 5, when x is 3 and y is 7. Pause and work it out.", "Find xy − 5 when x = 3 and y = 7."),
    ]),
    dict(kind="example", title="Check: xy − 5", steps=[
        dict(say="x y means x times y. 3 times 7 is 21. 21 minus 5 is 16.",
             do=[MATH("xy = x × y", x=80, y=190, color=GREY), MATH("3 × 7 − 5", x=80, y=280, at=1.8), B("= 21 − 5 = 16", x=80, y=370, color=GREEN, at=3.2)]),
    ]),
    dict(kind="example", title="Deriving a formula", steps=[
        dict(say="Tickets cost 9 dollars each, and there is a 3 dollar booking fee for each order. Write a formula for the total cost, T, of n tickets.",
             do=[E("🎫", 90, 165, 80), T("**$9** each", x=200, y=190), T("+ **$3** booking fee", x=420, y=190, at=2.4)]),
        dict(say="n tickets cost 9 n. Add the fee. T equals 9 n plus 3.", do=[MATH("9n", x=80, y=310), B("T = 9n + 3", x=80, y=400, color=BLUE, at=2.6)]),
        dict(say="For 6 tickets, T is 9 times 6, plus 3. That is 54 plus 3, so 57 dollars.",
             do=[MATH("T = 9 × 6 + 3 = 57", x=80, y=510, color=GREEN), T("$57", x=560, y=520, at=4.6)]),
    ]),
    dict(kind="example", title="A negative number", steps=[
        dict(say="Find 10 minus 2 k, when k is negative 4.", do=[B("10 − 2k", x=80, y=160), T("k = −4", x=420, y=178, color=GREY)]),
        dict(say="Put the negative number in brackets. 10 minus 2 times negative 4.", do=[MATH("10 − 2 × (−4)", x=80, y=270)]),
        dict(say="2 times negative 4 is negative 8. So we have 10 minus negative 8.", do=[MATH("= 10 − (−8)", x=80, y=360)]),
        dict(say="Subtracting negative 8 is the same as adding 8. The answer is 18.", do=[B("= 10 + 8 = 18", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Maya finds 3 p squared, when p is 4. Which line goes wrong first?", do=LINES("Maya", "3p² when p = 4", ["3p² = (3 × 4)²", "= 12²", "= 144"])),
        dict(say="Line 1 is wrong. The square belongs only to the p, not to the 3.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6), dict(a="strike", id="l3", at=0.9)]),
        dict(say="Square p first. 4 squared is 16, and 3 times 16 is 48.", do=[MATH("3 × 4² = 3 × 16", x=110, y=480, color=BLUE), B("= 48", x=560, y=472, color=GREEN, at=2.6)]),
    ]),
    dict(kind="life", title="Celsius and Fahrenheit", steps=[
        dict(say="Formulas are everywhere. Most countries measure temperature in degrees Celsius, but the United States uses degrees Fahrenheit.",
             do=[E("🌡️", 90, 170, 100), T("°C in most countries, **°F** in the USA", x=220, y=200)]),
        dict(say="This formula changes one into the other. F equals 1.8 times C, plus 32.", do=[B("F = 1.8C + 32", x=220, y=300, color=BLUE)]),
        dict(say="A hot day of 30 degrees Celsius: 1.8 times 30 is 54, plus 32 is 86. So 30 degrees Celsius is 86 degrees Fahrenheit.",
             do=[MATH("1.8 × 30 + 32 = 86", x=220, y=410), B("30 °C = 86 °F", x=220, y=500, color=RED, at=6), E("☀️", 1000, 440, 100, at=6.4)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.2-k4", "One last question. Use the formula v equals u plus 10 t, to find v when u is 4 and t is 3. Pause the video and answer.",
              "Use v = u + 10t to find v when u = 4 and t = 3."),
        dict(say="Substitute. v equals 4, plus 10 times 3. That is 4 plus 30, so v is 34.",
             do=[MATH("v = 4 + 10 × 3", x=80, y=190), MATH("= 4 + 30", x=80, y=280, at=2.4), B("v = 34", x=80, y=370, color=GREEN, at=4)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: to substitute, replace each letter by its number, put in the times signs, and follow the order of operations.",
             do=[T("• Substitute: replace, put × back, right order", x=80, y=170)]),
        dict(say="A formula links quantities, and has a subject.", do=[T("• A formula has a **subject**: C = 12 + 0.1t", x=80, y=250)]),
        dict(say="2 m squared squares only the m.", do=[T("• 2m² squares only m; (2m)² squares 2m", x=80, y=330)]),
        dict(say="To derive a formula, say the rule in words first, then write it in letters.", do=[T("• Derive: words first, then letters", x=80, y=410)]),
    ]),
]

VIDEOS["2.3"] = [
    dict(kind="hook", title="Bricks in a row", steps=[
        dict(say="Red bricks are x centimetres long. Blue bricks are y centimetres long.",
             do=[T(RB, x=90, y=170), T("x cm", x=230, y=185, color=RED), T(BB, x=420, y=170, at=1.8), T("y cm", x=600, y=185, color=BLUE, at=1.8)]),
        dict(say="You join 3 red bricks, then 2 blue bricks, then 1 more red brick.",
             do=[T(RB * 3, x=90, y=320), T(BB * 2, x=438, y=320, at=1.6), T(RB, x=750, y=320, at=3.2)]),
        PAUSE("2.3-k1", "How long is the row? Write it as simply as you can. Pause the video and try.", "3 red bricks (x cm), 2 blue bricks (y cm) and 1 more red brick. Write the total length as simply as possible."),
    ]),
    dict(kind="hook", title="Put the same colours together", steps=[
        dict(say="The row is 3 x, plus 2 y, plus x.", do=[T(RB * 3 + BB * 2 + RB, x=90, y=170), MATH("3x + 2y + x", x=90, y=270)]),
        dict(say="Put the red bricks together. 3 x and 1 more x make 4 x.", do=[T(RB * 4 + BB * 2, x=90, y=390), MATH("3x + x = 4x", x=90, y=490, at=2, color=RED)]),
        dict(say="The blue bricks are a different length, so they stay separate. The row is 4 x plus 2 y.", do=[B("4x + 2y", x=560, y=482, color=GREEN)]),
    ]),
    dict(kind="recall", title="Terms", steps=[
        dict(say="In the expression 4 x plus 3 y minus 2, the terms are 4 x, 3 y, and negative 2.",
             do=[B("4x + 3y − 2", x=80, y=170), T("terms:", x=80, y=290, color=GREY, at=3), MATH("4x", x=220, y=282, at=3.4, color=RED), MATH("+3y", x=360, y=282, at=4.4, color=BLUE), MATH("−2", x=520, y=282, at=5.4)]),
        dict(say="The sign in front of a term belongs to that term.", do=[T("The **sign in front** belongs to the term", x=80, y=400)]),
    ]),
    dict(kind="idea", title="Like terms", steps=[
        dict(say="Like terms have exactly the same letters. 3 x and 5 x are like terms.", do=[MATH("3x and 5x", x=80, y=170), T("like terms ✓", x=420, y=178, color=GREEN, at=3)]),
        dict(say="3 x and 3 y are not like terms. The letters are different.", do=[MATH("3x and 3y", x=80, y=260), T("not like terms ✗", x=420, y=268, color=RED, at=1.6)]),
        dict(say="x and x squared are not like terms either. The powers are different.", do=[MATH("x and x²", x=80, y=350), T("not like terms ✗", x=420, y=358, color=RED, at=1.8)]),
        dict(say="You add or subtract like terms by adding or subtracting the numbers in front. 3 x plus 2 x is 5 x.",
             do=[T(RB * 3, x=80, y=450), T("+", x=440, y=460), T(RB * 2, x=490, y=450, at=0.6), MATH("3x + 2x = 5x", x=780, y=452, at=3.6, color=GREEN)]),
        dict(say="Unlike terms stay separate. 3 x plus 2 y cannot be made any simpler.", do=[T("3x + 2y cannot be simplified", x=80, y=560, color=GREY)]),
    ]),
    dict(kind="idea", title="Simplifying", steps=[
        dict(say="To simplify an expression, collect each kind of like term. Try 6 a plus 4 b, minus 2 a, plus b.", do=[B("6a + 4b − 2a + b", x=80, y=160)]),
        dict(say="The a terms are 6 a and minus 2 a. 6 a minus 2 a is 4 a.", do=[MATH("6a − 2a = 4a", x=80, y=280, color=RED)]),
        dict(say="The b terms are 4 b and b. Remember, b means 1 b. 4 b plus 1 b is 5 b.", do=[MATH("4b + b = 5b", x=80, y=370, color=BLUE), T("b means 1b", x=420, y=378, color=GREY, at=2.4)]),
        dict(say="So the expression simplifies to 4 a plus 5 b.", do=[B("4a + 5b", x=80, y=470, color=GREEN)]),
        PAUSE("2.3-k2", "Your turn. Simplify 7 y, minus 2 y, plus y. Pause the video and try it.", "Simplify 7y − 2y + y."),
    ]),
    dict(kind="idea", title="Check: 7y − 2y + y", steps=[
        dict(say="They are all y terms. 7 minus 2 is 5, and 5 plus 1 is 6. The answer is 6 y.",
             do=[MATH("7 − 2 + 1 = 6", x=80, y=190, color=GREY), B("7y − 2y + y = 6y", x=80, y=290, color=GREEN, at=3.6)]),
    ]),
    dict(kind="method", title="How do I collect like terms?", steps=[
        dict(say="Here is the method. Step 1: mark each kind of like term, together with its sign.", do=[T("1. **Mark** each kind of like term, with its sign", x=80, y=170)]),
        dict(say="Step 2: add or subtract the coefficients of each kind.", do=[T("2. Add or subtract the **coefficients**", x=80, y=260)]),
        dict(say="Step 3: write each kind once. Plain numbers are like terms with each other.", do=[T("3. Write each kind **once**; numbers go together", x=80, y=350)]),
        dict(say="Step 4: check by putting a number into both the question and your answer.", do=[T("4. **Check** with a number", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Two letters", steps=[
        dict(say="Simplify 5 x plus 3 y, plus 2 x, minus y.", do=[B("5x + 3y + 2x − y", x=80, y=160)]),
        dict(say="The x terms: 5 x plus 2 x is 7 x.", do=[MATH("5x + 2x = 7x", x=80, y=270, color=RED)]),
        dict(say="The y terms: 3 y minus y is 2 y.", do=[MATH("3y − y = 2y", x=80, y=360, color=BLUE)]),
        dict(say="The answer is 7 x plus 2 y.", do=[B("7x + 2y", x=80, y=460, color=GREEN)]),
        dict(say="Check with x equals 1 and y equals 1. The question gives 5 plus 3 plus 2 minus 1, which is 9. The answer gives 7 plus 2, which is 9 too.",
             do=[T("x = 1, y = 1:  5 + 3 + 2 − 1 = 9  and  7 + 2 = 9 ✓", x=420, y=478, color=GREY)]),
    ]),
    dict(kind="example", title="With numbers", steps=[
        dict(say="Simplify 8 plus 3 n, minus 5, minus 7 n.", do=[B("8 + 3n − 5 − 7n", x=80, y=160)]),
        dict(say="The n terms: 3 n minus 7 n is negative 4 n. The minus sign belongs to the 7 n.", do=[MATH("3n − 7n = −4n", x=80, y=270, color=RED)]),
        dict(say="The plain numbers: 8 minus 5 is 3.", do=[MATH("8 − 5 = 3", x=80, y=360, color=BLUE)]),
        dict(say="So we get negative 4 n plus 3, which is usually written as 3 minus 4 n.", do=[B("3 − 4n", x=80, y=460, color=GREEN)]),
        PAUSE("2.3-k3", "Your turn. Simplify 2 a plus 5, plus 3 a, minus 1. Pause and work it out.", "Simplify 2a + 5 + 3a − 1."),
    ]),
    dict(kind="example", title="Check: 2a + 5 + 3a − 1", steps=[
        dict(say="The a terms: 2 a plus 3 a is 5 a. The numbers: 5 minus 1 is 4. The answer is 5 a plus 4.",
             do=[MATH("2a + 3a = 5a", x=80, y=190, color=RED), MATH("5 − 1 = 4", x=480, y=190, color=BLUE, at=2.6), B("5a + 4", x=80, y=310, color=GREEN, at=4.8)]),
    ]),
    dict(kind="example", title="Terms with x²", steps=[
        dict(say="Simplify 3 x squared, plus 2 x, minus x squared, plus 5 x.", do=[B("3x² + 2x − x² + 5x", x=80, y=160)]),
        dict(say="The x squared terms: 3 x squared minus x squared is 2 x squared.", do=[MATH("3x² − x² = 2x²", x=80, y=270, color=RED)]),
        dict(say="The x terms: 2 x plus 5 x is 7 x.", do=[MATH("2x + 5x = 7x", x=80, y=360, color=BLUE)]),
        dict(say="The answer is 2 x squared plus 7 x. You cannot combine x squared with x.", do=[B("2x² + 7x", x=80, y=460, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ben simplifies 4 m plus 3 n plus 2 m. Which line is wrong?", do=LINES("Ben", "4m + 3n + 2m", ["4m + 3n + 2m", "= 9mn"])),
        dict(say="Line 2 is wrong. m and n are unlike terms, so they cannot be added together.", do=[dict(a="cross", id="l2")]),
        dict(say="Only 4 m and 2 m combine. They make 6 m. The answer is 6 m plus 3 n.", do=[MATH("4m + 2m = 6m", x=110, y=420, color=BLUE), B("6m + 3n", x=560, y=412, color=GREEN, at=3)]),
    ]),
    dict(kind="life", title="At the shop", steps=[
        dict(say="You collect like terms every time you shop. Imagine you buy 3 apples and 2 bananas, then go back for 2 more apples.",
             do=[E("🍎", 90, 170, 70), E("🍎", 170, 170, 70, at=0.2), E("🍎", 250, 170, 70, at=0.4), E("🍌", 370, 170, 70, at=1.6), E("🍌", 450, 170, 70, at=1.8), E("🍎", 570, 170, 70, at=3.4), E("🍎", 650, 170, 70, at=3.6)]),
        dict(say="The till does not list them one by one. It collects them: 5 apples and 2 bananas.", do=[MATH("3a + 2b + 2a = 5a + 2b", x=90, y=300, color=BLUE)]),
        dict(say="If an apple costs 40 cents and a banana costs 30 cents, the bill is 5 times 40, plus 2 times 30. That is 260 cents.",
             do=[T("a = 40, b = 30", x=90, y=410, color=GREY), MATH("5 × 40 + 2 × 30 = 260", x=90, y=480, at=3.4), E("🧾", 760, 440, 90, at=6)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.3-k4", "One last question. Simplify 6 x plus 2 y, minus 4 x, minus 5 y. Pause the video and answer.", "Simplify 6x + 2y − 4x − 5y."),
        dict(say="The x terms: 6 x minus 4 x is 2 x. The y terms: 2 y minus 5 y is negative 3 y. The answer is 2 x minus 3 y.",
             do=[MATH("6x − 4x = 2x", x=80, y=190, color=RED), MATH("2y − 5y = −3y", x=480, y=190, color=BLUE, at=3), B("2x − 3y", x=80, y=310, color=GREEN, at=6.6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: like terms have the same letters and the same powers.", do=[T("• Like terms: same letters, same powers", x=80, y=170)]),
        dict(say="Collect them by adding or subtracting the coefficients. The sign belongs to the term after it.", do=[T("• Add or subtract the coefficients; the sign stays with its term", x=80, y=250)]),
        dict(say="Unlike terms stay separate.", do=[T("• x and y, or x and x², stay separate", x=80, y=330)]),
        dict(say="Check your answer by substituting a number.", do=[T("• Check by substituting a number", x=80, y=410)]),
    ]),
]

FIG = lambda x, y, w, at=0, **spec: dict(a="fig", fig=spec, x=x, y=y, w=w, at=at)

VIDEOS["2.4"] = [
    dict(kind="hook", title="Two ways to count", steps=[
        dict(say="A school orders 4 packs. Each pack has n pens and 3 pencils.",
             do=[E("📦", 90, 170, 90), T("one pack: **n pens** and **3 pencils**", x=220, y=195), E("📦", 90, 310, 80, at=0.2), E("📦", 190, 310, 80, at=0.4), E("📦", 290, 310, 80, at=0.6), E("📦", 390, 310, 80, at=0.8)]),
        PAUSE("2.4-k1", "How many items is that altogether? Write the total without brackets. Pause the video and try.",
              "4 packs, each with n pens and 3 pencils. Write the total number of items without brackets."),
    ]),
    dict(kind="hook", title="4 lots of (n + 3)", steps=[
        dict(say="One pack holds n plus 3 items. So 4 packs hold 4 lots of n plus 3. We write that with a bracket.", do=[B("4(n + 3)", x=80, y=160, color=BLUE)]),
        dict(say="Count the pens first: 4 packs of n pens is 4 n.", do=[E("🖊️", 80, 280, 60), MATH("4 × n = 4n", x=170, y=280)]),
        dict(say="Then the pencils: 4 packs of 3 pencils is 12.", do=[E("✏️", 80, 380, 60), MATH("4 × 3 = 12", x=170, y=380)]),
        dict(say="Altogether, that is 4 n plus 12. Both ways count the same items.", do=[B("4(n + 3) = 4n + 12", x=80, y=490, color=GREEN)]),
    ]),
    dict(kind="recall", title="Multiplying a sum", steps=[
        dict(say="This already works with numbers. 4 times, bracket, 10 plus 3, is 4 times 13, which is 52.", do=[MATH("4 × (10 + 3) = 4 × 13 = 52", x=80, y=170)]),
        dict(say="You get the same answer if you multiply each part: 4 times 10, plus 4 times 3. That is 40 plus 12, which is 52.",
             do=[MATH("4 × 10 + 4 × 3 = 40 + 12 = 52", x=80, y=280, color=BLUE), E("✅", 760, 266, 50, at=5)]),
    ]),
    dict(kind="idea", title="Expanding a bracket", steps=[
        dict(say="To expand a bracket, multiply every term inside the bracket by the term outside.", do=[T("**Expand**: multiply **every** term inside by the term outside", x=80, y=160)]),
        dict(say="For 4, bracket, n plus 3: 4 times n is 4 n.", do=[B("4(n + 3)", x=80, y=250, id="q"), MATH("4 × n = 4n", x=480, y=258, at=2, color=RED)]),
        dict(say="And 4 times 3 is 12.", do=[MATH("4 × 3 = 12", x=480, y=340, color=BLUE)]),
        dict(say="A multiplication grid helps. Put the outside term at the side, and the inside terms along the top.",
             do=[dict(a="table", id="t", head=["×", "n", "+3"], rows=[["4", "4n", "+12"]], x=80, y=420), dict(a="row", id="t", i=0, at=3)]),
        dict(say="So 4, bracket, n plus 3, expands to 4 n plus 12.", do=[B("= 4n + 12", x=480, y=440, color=GREEN)]),
        PAUSE("2.4-k2", "Your turn. Expand 2, bracket, x plus 9. Pause the video and try it.", "Expand 2(x + 9)."),
    ]),
    dict(kind="idea", title="Check: 2(x + 9)", steps=[
        dict(say="2 times x is 2 x. 2 times 9 is 18. The answer is 2 x plus 18.",
             do=[MATH("2 × x = 2x", x=80, y=190, color=RED), MATH("2 × 9 = 18", x=480, y=190, color=BLUE, at=1.8), B("2(x + 9) = 2x + 18", x=80, y=310, color=GREEN, at=3.6)]),
    ]),
    dict(kind="idea", title="Signs inside the bracket", steps=[
        dict(say="Keep the sign of each term. Expand 5, bracket, x minus 2.", do=[B("5(x − 2)", x=80, y=160)]),
        dict(say="5 times x is 5 x. 5 times negative 2 is negative 10. So the answer is 5 x minus 10.",
             do=[dict(a="table", id="t", head=["×", "x", "−2"], rows=[["5", "5x", "−10"]], x=80, y=270), dict(a="row", id="t", i=0, at=1), B("= 5x − 10", x=480, y=290, color=GREEN, at=5)]),
        dict(say="The term outside can be a letter too. a, bracket, a plus 4. a times a is a squared, and a times 4 is 4 a.",
             do=[B("a(a + 4)", x=80, y=440), B("= a² + 4a", x=480, y=440, color=GREEN, at=5)]),
    ]),
    dict(kind="method", title="How do I expand a bracket?", steps=[
        dict(say="Here is the method. Step 1: multiply the term outside by the first term inside.", do=[T("1. Outside × the **first** term inside", x=80, y=170)]),
        dict(say="Step 2: multiply it by the second term inside, and keep its sign.", do=[T("2. Outside × the **second** term; keep its **sign**", x=80, y=260)]),
        dict(say="Step 3: write the results with their signs. Simplify if there are like terms.", do=[T("3. Write the results; collect like terms", x=80, y=350)]),
        dict(say="Step 4: check with a number.", do=[T("4. **Check** with a number", x=80, y=440), E("✅", 1000, 410, 90, at=0.6)]),
    ]),
    dict(kind="example", title="A minus sign inside", steps=[
        dict(say="Expand 6, bracket, 2 k minus 3.", do=[B("6(2k − 3)", x=80, y=160)]),
        dict(say="6 times 2 k is 12 k.", do=[MATH("6 × 2k = 12k", x=80, y=270, color=RED)]),
        dict(say="6 times negative 3 is negative 18. Keep the minus.", do=[MATH("6 × (−3) = −18", x=80, y=360, color=BLUE)]),
        dict(say="The answer is 12 k minus 18.", do=[B("12k − 18", x=80, y=460, color=GREEN)]),
        dict(say="Check with k equals 2. The bracket gives 6 times 1, which is 6. The answer gives 24 minus 18, which is also 6.",
             do=[T("k = 2:  6 × (4 − 3) = 6  and  24 − 18 = 6 ✓", x=420, y=478, color=GREY)]),
        PAUSE("2.4-k3", "Your turn. Expand 8, bracket, 3 minus p. Pause and work it out.", "Expand 8(3 − p)."),
    ]),
    dict(kind="example", title="Check: 8(3 − p)", steps=[
        dict(say="8 times 3 is 24. 8 times negative p is negative 8 p. The answer is 24 minus 8 p.",
             do=[MATH("8 × 3 = 24", x=80, y=190, color=RED), MATH("8 × (−p) = −8p", x=480, y=190, color=BLUE, at=2), B("8(3 − p) = 24 − 8p", x=80, y=310, color=GREEN, at=4.6)]),
    ]),
    dict(kind="example", title="Expand and simplify", steps=[
        dict(say="Expand and simplify 2, bracket, x plus 5, plus 3, bracket, x minus 1.", do=[B("2(x + 5) + 3(x − 1)", x=80, y=160)]),
        dict(say="The first bracket gives 2 x plus 10.", do=[MATH("2(x + 5) = 2x + 10", x=80, y=270, color=RED)]),
        dict(say="The second bracket gives 3 x minus 3.", do=[MATH("3(x − 1) = 3x − 3", x=80, y=360, color=BLUE)]),
        dict(say="Now collect like terms. 2 x plus 3 x is 5 x. 10 minus 3 is 7. The answer is 5 x plus 7.",
             do=[MATH("2x + 10 + 3x − 3", x=80, y=450), B("= 5x + 7", x=560, y=442, color=GREEN, at=5)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Aisha expands 5, bracket, n plus 4. Which line is wrong?", do=LINES("Aisha", "5(n + 4)", ["5 × n = 5n", "5(n + 4) = 5n + 4"])),
        dict(say="Line 2 is wrong. The 4 must be multiplied by 5 as well.", do=[dict(a="cross", id="l2")]),
        dict(say="5 times 4 is 20. So the answer is 5 n plus 20. Test n equals 1: the bracket gives 25, and 5 plus 20 is 25.",
             do=[MATH("5 × 4 = 20", x=110, y=420, color=BLUE), B("5n + 20", x=480, y=412, color=GREEN, at=2.4), T("n = 1:  5 × 5 = 25  and  5 + 20 = 25 ✓", x=110, y=530, color=GREY, at=5)]),
    ]),
    dict(kind="life", title="Mental maths at the shop", steps=[
        dict(say="You expand brackets in your head when you shop. Suppose you buy 6 notebooks at 99 cents each.",
             do=[E("📓", 90, 170, 90), T("6 notebooks at **99 cents**", x=210, y=195)]),
        dict(say="99 is 100 minus 1. So the cost is 6, bracket, 100 minus 1.", do=[B("6(100 − 1)", x=210, y=300, color=BLUE)]),
        dict(say="That is 600 minus 6, which is 594 cents. Much easier than multiplying 6 by 99.",
             do=[MATH("= 600 − 6 = 594", x=210, y=410, color=GREEN), T("$5.94", x=640, y=420, at=2.6), E("🧠", 1000, 380, 100, at=4)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.4-k4", "One last question. Expand and simplify 3, bracket, y plus 2, plus y. Pause the video and answer.", "Expand and simplify 3(y + 2) + y."),
        dict(say="The bracket gives 3 y plus 6. Then add y. 3 y plus y is 4 y. The answer is 4 y plus 6.",
             do=[MATH("3(y + 2) = 3y + 6", x=80, y=190, color=RED), MATH("3y + 6 + y", x=80, y=280, at=2.6), B("= 4y + 6", x=80, y=370, color=GREEN, at=5)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: expand means multiply every term inside the bracket by the term outside.", do=[T("• Expand = multiply **every** term inside", x=80, y=170)]),
        dict(say="Keep the signs. 5, bracket, x minus 2, is 5 x minus 10.", do=[T("• Keep the signs: 5(x − 2) = 5x − 10", x=80, y=250)]),
        dict(say="A letter outside works the same way.", do=[T("• a(a + 4) = a² + 4a", x=80, y=330)]),
        dict(say="Expand each bracket, then collect like terms, and check with a number.", do=[T("• Expand, collect like terms, check", x=80, y=410)]),
    ]),
]

BAL = lambda left, right, ll, rl, x=640, y=150, w=520, at=0: FIG(x, y, w, at, kind="balance", left=left, right=right, leftLabel=ll, rightLabel=rl)

VIDEOS["2.5"] = [
    dict(kind="hook", title="A balancing act", steps=[
        dict(say="Look at this balance. The left pan holds 2 bags of marbles and 5 loose marbles. Each bag holds the same number, x.",
             do=[BAL([["x", 2], ["1", 5]], [["1", 13]], "2x + 5", "13"), T("left: **2 bags** of x marbles + **5** marbles", x=80, y=190)]),
        dict(say="The right pan holds 13 marbles. The two pans balance.", do=[T("right: **13** marbles", x=80, y=270), T("The pans **balance**", x=80, y=350, color=GREEN, at=1.6)]),
        PAUSE("2.5-k1", "How many marbles are in each bag? Pause the video and work it out.", "2 bags of x marbles and 5 marbles balance 13 marbles. How many marbles are in each bag?"),
    ]),
    dict(kind="hook", title="Keep it balanced", steps=[
        dict(say="Take 5 marbles off both pans. It still balances. Now 2 bags balance 8 marbles.",
             do=[BAL([["x", 2]], [["1", 8]], "2x", "8"), MATH("2x + 5 = 13", x=80, y=180), MATH("2x = 8", x=80, y=280, at=3, color=BLUE)]),
        dict(say="Share both sides into 2 equal parts. One bag balances 4 marbles. So each bag holds 4 marbles.",
             do=[B("x = 4", x=80, y=390, color=GREEN, at=3.6)]),
    ]),
    dict(kind="recall", title="Inverse operations", steps=[
        dict(say="Remember inverse operations. Adding and subtracting undo each other.", do=[B("+ ↔ −", x=80, y=170, color=BLUE)]),
        dict(say="Multiplying and dividing undo each other.", do=[B("× ↔ ÷", x=80, y=280, color=RED)]),
        dict(say="I think of a number, multiply it by 4, and get 36. To find my number, divide 36 by 4. It was 9.", do=[MATH("36 ÷ 4 = 9", x=80, y=400, at=4.6)]),
    ]),
    dict(kind="idea", title="Equations and solutions", steps=[
        dict(say="An equation says that two things are equal. 2 x plus 5 equals 13 is an equation.", do=[B("2x + 5 = 13", x=80, y=160)]),
        dict(say="To solve it means to find the value of x that makes it true. That value is called the solution.", do=[T("**Solve** = find the value that makes it true: the **solution**", x=80, y=270)]),
        dict(say="An equation is like a balance. Whatever you do to one side, you must do to the other side too.",
             do=[E("⚖️", 80, 360, 100), T("Do the **same** to **both sides**", x=210, y=390, color=RED)]),
    ]),
    dict(kind="idea", title="Solving step by step", steps=[
        dict(say="Let's write the working properly. Start with 2 x plus 5 equals 13.", do=[MATH("2x + 5 = 13", x=80, y=160)]),
        dict(say="Subtract 5 from both sides.", do=[MATH("2x + 5 − 5 = 13 − 5", x=80, y=250, color=BLUE), T("− 5 on both sides", x=640, y=258, color=GREY)]),
        dict(say="That leaves 2 x equals 8.", do=[MATH("2x = 8", x=80, y=340)]),
        dict(say="Divide both sides by 2.", do=[MATH("2x ÷ 2 = 8 ÷ 2", x=80, y=430, color=RED), T("÷ 2 on both sides", x=640, y=438, color=GREY)]),
        dict(say="So x equals 4. Check: 2 times 4, plus 5, is 13. Correct.", do=[B("x = 4", x=80, y=520, color=GREEN), T("check: 2 × 4 + 5 = 13 ✓", x=640, y=538, color=GREY, at=2)]),
        PAUSE("2.5-k2", "Your turn. Solve 5 x equals 45. Pause the video and try it.", "Solve 5x = 45."),
    ]),
    dict(kind="idea", title="Check: 5x = 45", steps=[
        dict(say="5 x means 5 times x. Undo it by dividing both sides by 5. 45 divided by 5 is 9. So x equals 9.",
             do=[MATH("5x ÷ 5 = 45 ÷ 5", x=80, y=190, color=RED), B("x = 9", x=80, y=300, color=GREEN, at=5)]),
    ]),
    dict(kind="method", title="How do I solve an equation?", steps=[
        dict(say="Here is the method. Step 1: look at what has been done to the letter, and in what order.", do=[T("1. What has been done to the letter, in what **order**?", x=80, y=170)]),
        dict(say="Step 2: undo the last operation first. Do the same to both sides.", do=[T("2. Undo the **last** operation first, on **both sides**", x=80, y=260)]),
        dict(say="Step 3: keep going until the letter is on its own.", do=[T("3. Keep going until the letter is on its own", x=80, y=350)]),
        dict(say="Step 4: check, by substituting your answer into the equation you started with.", do=[T("4. **Check** in the original equation", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Two steps", steps=[
        dict(say="Solve 3 y minus 4 equals 17.", do=[B("3y − 4 = 17", x=80, y=160)]),
        dict(say="The last thing done to y was subtract 4. Undo it: add 4 to both sides. 3 y equals 21.",
             do=[MATH("3y − 4 + 4 = 17 + 4", x=80, y=270, color=BLUE), MATH("3y = 21", x=80, y=350, at=4)]),
        dict(say="Now undo times 3. Divide both sides by 3. y equals 7.", do=[MATH("3y ÷ 3 = 21 ÷ 3", x=80, y=430, color=RED), B("y = 7", x=80, y=510, color=GREEN, at=3)]),
        dict(say="Check: 3 times 7 is 21, and 21 minus 4 is 17.", do=[T("check: 3 × 7 − 4 = 17 ✓", x=640, y=528, color=GREY)]),
        PAUSE("2.5-k3", "Your turn. Solve 2 m plus 7 equals 19. Pause and work it out.", "Solve 2m + 7 = 19."),
    ]),
    dict(kind="example", title="Check: 2m + 7 = 19", steps=[
        dict(say="Subtract 7 from both sides. 2 m equals 12. Divide both sides by 2. m equals 6.",
             do=[MATH("2m = 19 − 7 = 12", x=80, y=190, color=BLUE), MATH("m = 12 ÷ 2", x=80, y=280, color=RED, at=3), B("m = 6", x=80, y=380, color=GREEN, at=4.6)]),
    ]),
    dict(kind="example", title="Think of a number", steps=[
        dict(say="I think of a number, double it, and add 9. The answer is 31. What was my number?", do=[E("🤔", 90, 160, 90), T("double it, add 9 → **31**", x=210, y=190)]),
        dict(say="Call the number n. Double it and add 9 gives 2 n plus 9. That equals 31.", do=[B("2n + 9 = 31", x=80, y=300, color=BLUE)]),
        dict(say="Subtract 9 from both sides. 2 n equals 22.", do=[MATH("2n = 22", x=80, y=400)]),
        dict(say="Divide both sides by 2. n equals 11. My number was 11.", do=[B("n = 11", x=80, y=490, color=GREEN)]),
    ]),
    dict(kind="example", title="A taxi ride", steps=[
        dict(say="A taxi costs 4 dollars, plus 3 dollars for every kilometre. A ride cost 25 dollars. How far was it?",
             do=[E("🚕", 90, 160, 90), T("**$4** + **$3** per km.  Cost: **$25**", x=210, y=190)]),
        dict(say="Call the distance d kilometres. The cost is 3 d plus 4, and that equals 25.", do=[B("3d + 4 = 25", x=80, y=300, color=BLUE)]),
        dict(say="Subtract 4. 3 d equals 21. Divide by 3. d equals 7. The ride was 7 kilometres.",
             do=[MATH("3d = 21", x=80, y=400), B("d = 7", x=80, y=490, color=GREEN, at=3), T("7 km", x=300, y=508, at=4.6)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Dan solves 4 x plus 8 equals 20. Which line goes wrong first?", do=LINES("Dan", "4x + 8 = 20", ["4x + 8 = 20", "x + 8 = 5", "x = −3"])),
        dict(say="Line 2 is wrong. Dan divided only part of the left side by 4. That breaks the balance.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="Undo plus 8 first. 4 x equals 12. Then divide by 4. x equals 3.", do=[MATH("4x = 12", x=110, y=480, color=BLUE), B("x = 3", x=480, y=472, color=GREEN, at=3)]),
    ]),
    dict(kind="life", title="Equations run the world", steps=[
        dict(say="Every time a map app tells you when you will arrive, it is solving an equation: distance equals speed times time.",
             do=[E("🗺️", 90, 170, 100), B("distance = speed × time", x=220, y=195, color=BLUE)]),
        dict(say="Suppose you have 120 kilometres to go, at 60 kilometres an hour. 60 t equals 120.", do=[MATH("60t = 120", x=220, y=320)]),
        dict(say="Divide both sides by 60. t equals 2. You will arrive in 2 hours.", do=[B("t = 2 hours", x=220, y=430, color=GREEN), E("🚗", 1000, 400, 100, at=1.6)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.5-k4", "One last question. Solve y over 4, minus 1, equals 5. Pause the video and answer.", "Solve y/4 − 1 = 5."),
        dict(say="Add 1 to both sides. y over 4 equals 6. Multiply both sides by 4. y equals 24.",
             do=[MATH("$$\\frac{y}{4} = 6$$", x=80, y=180, color=BLUE), MATH("y = 6 × 4", x=80, y=320, color=RED, at=3), B("y = 24", x=80, y=420, color=GREEN, at=4.6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: an equation is a balance. The solution makes both sides equal.", do=[T("• An equation is a **balance**", x=80, y=170)]),
        dict(say="Do the same to both sides. Undo the operations in reverse order.", do=[T("• Same to both sides; undo in **reverse order**", x=80, y=250)]),
        dict(say="Write each step on a new line.", do=[T("• One step per line", x=80, y=330)]),
        dict(say="To make an equation from words, choose a letter for the unknown. And always check.", do=[T("• Choose a letter for the unknown; always check", x=80, y=410)]),
    ]),
]

INEQ = lambda x, y, w, at=0, **spec: FIG(x, y, w, at, kind="ineq", **spec)

VIDEOS["2.6"] = [
    dict(kind="hook", title="Height limit", steps=[
        dict(say="A ride at a theme park has a sign. You must be taller than 120 centimetres.", do=[E("🎢", 90, 170, 110), T("You must be **taller than 120 cm**", x=240, y=205)]),
        dict(say="Lily is exactly 120 centimetres tall.", do=[E("🧒", 90, 330, 90), T("Lily: exactly **120 cm**", x=240, y=355)]),
        PAUSE("2.6-k1", "Can she go on the ride? Pause the video and decide.", "You must be taller than 120 cm. Can someone who is exactly 120 cm go on?"),
    ]),
    dict(kind="hook", title="Taller than 120", steps=[
        dict(say="The answer is no. Taller than 120 means more than 120. Exactly 120 is not enough.", do=[T("exactly 120 cm", x=80, y=180), E("❌", 360, 166, 56, at=0.6), T("120.5 cm", x=80, y=270, at=3), E("✅", 360, 256, 56, at=3.6)]),
        dict(say="But 120 and a half centimetres is fine. In maths we write the rule like this: h is greater than 120.", do=[B("h > 120", x=80, y=390, color=BLUE, at=3.6)]),
    ]),
    dict(kind="recall", title="Inequality signs", steps=[
        dict(say="This sign means is less than. 3 is less than 8.", do=[B("3 < 8", x=80, y=170, color=BLUE), T("“is less than”", x=320, y=188)]),
        dict(say="This sign means is greater than. 8 is greater than 3.", do=[B("8 > 3", x=80, y=280, color=RED), T("“is greater than”", x=320, y=298)]),
        dict(say="The open side always faces the bigger number. With negative numbers, negative 4 is less than negative 1.",
             do=[T("The **open side** faces the **bigger** number", x=80, y=400), MATH("−4 < −1", x=80, y=480, at=3.4)]),
    ]),
    dict(kind="idea", title="Inequalities with a letter", steps=[
        dict(say="An inequality like h is greater than 120 describes a whole range of values, not just one.", do=[B("h > 120", x=80, y=160, color=BLUE)]),
        dict(say="h could be 121, or 130, or 120 and a half. But not 120 itself.", do=[T("121 ✓   130 ✓   120.5 ✓   120 ✗", x=80, y=260)]),
        dict(say="On a number line, draw an open circle at 120, because 120 is not included.", do=[INEQ(80, 340, 760, min=116, max=126, a=120, dir="right"), T("**open circle**: 120 is not included", x=80, y=560, at=1.6)]),
        dict(say="Then draw an arrow to the right, towards the bigger numbers.", do=[T("arrow → the values that work", x=640, y=560, color=GREEN)]),
        PAUSE("2.6-k2", "Your turn. Which number satisfies x is less than negative 2? Pause the video and choose.", "Which number satisfies x < −2?"),
    ]),
    dict(kind="idea", title="Check: x < −2", steps=[
        dict(say="Less than negative 2 means to the left of negative 2 on the number line. Negative 5 is to the left, so negative 5 works.",
             do=[INEQ(80, 170, 760, min=-7, max=3, a=-2, dir="left"), B("−5 < −2", x=80, y=420, color=GREEN, at=4), E("✅", 360, 414, 56, at=5)]),
    ]),
    dict(kind="idea", title="Between two values", steps=[
        dict(say="You can join two inequalities. This one says x is greater than negative 1, and less than 4. So x is between negative 1 and 4.",
             do=[B("−1 < x < 4", x=80, y=160, color=BLUE), T("x is **between** −1 and 4", x=480, y=178, at=5)]),
        dict(say="Draw open circles at both ends, and join them.", do=[INEQ(80, 270, 760, min=-3, max=6, a=-1, b=4)]),
        dict(say="If x must be an integer, the possible values are 0, 1, 2 and 3. Negative 1 and 4 are not included.",
             do=[T("Integers: **0, 1, 2, 3**", x=80, y=520), T("(−1 and 4 are not included)", x=480, y=520, color=GREY, at=4.4)]),
    ]),
    dict(kind="method", title="How do I write and show an inequality?", steps=[
        dict(say="Here is the method. Step 1: decide whether the letter is greater than, or less than, the boundary.", do=[T("1. Greater than (**>**) or less than (**<**) the boundary?", x=80, y=170)]),
        dict(say="Step 2: draw an open circle at the boundary, because it is not included.", do=[T("2. **Open circle** at the boundary", x=80, y=260)]),
        dict(say="Step 3: draw the line towards the values that work. Right for greater than, left for less than.", do=[T("3. Line to the **right** for >, to the **left** for <", x=80, y=350)]),
        dict(say="Step 4: when you list integers, leave out the boundary values.", do=[T("4. Listing integers? Leave out the boundaries", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="From words", steps=[
        dict(say="Write an inequality for this sentence. The temperature, t, was below negative 3 degrees.", do=[E("🥶", 90, 160, 90), T("The temperature t was **below −3 °C**", x=210, y=190)]),
        dict(say="Below means less than. So t is less than negative 3.", do=[B("t < −3", x=80, y=310, color=GREEN)]),
        dict(say="Now read a number line. There is an open circle at 1, and an arrow to the right.", do=[INEQ(560, 270, 600, min=-5, max=5, a=1, dir="right")]),
        dict(say="The open circle means 1 is not included. The arrow points to bigger numbers. So x is greater than 1.", do=[B("x > 1", x=80, y=470, color=GREEN, at=4.6)]),
    ]),
    dict(kind="example", title="Integers in a range", steps=[
        dict(say="List the integers that satisfy negative 3 is less than x, is less than 2.", do=[B("−3 < x < 2", x=80, y=160), INEQ(560, 150, 600, min=-5, max=4, a=-3, b=2)]),
        dict(say="x is greater than negative 3, so start at negative 2. Negative 3 is not included.", do=[T("greater than −3 → start at **−2**", x=80, y=300)]),
        dict(say="x is less than 2, so stop at 1.", do=[T("less than 2 → stop at **1**", x=80, y=380)]),
        dict(say="The integers are negative 2, negative 1, 0 and 1.", do=[B("−2, −1, 0, 1", x=80, y=470, color=GREEN)]),
        PAUSE("2.6-k3", "Your turn. How many integers satisfy negative 2 is less than x, is less than 3? Pause and count them.", "How many integers satisfy −2 < x < 3?"),
    ]),
    dict(kind="example", title="Check: −2 < x < 3", steps=[
        dict(say="Start just after negative 2, and stop just before 3. The integers are negative 1, 0, 1 and 2. That is 4 integers.",
             do=[INEQ(80, 170, 760, min=-4, max=5, a=-2, b=3), MATH("−1, 0, 1, 2", x=80, y=420, at=3.4), B("4 integers", x=480, y=412, color=GREEN, at=6.4)]),
    ]),
    dict(kind="example", title="The other way round", steps=[
        dict(say="Sometimes the letter is on the right. 10 is greater than y.", do=[B("10 > y", x=80, y=170)]),
        dict(say="Read it starting from the letter. If 10 is greater than y, then y is less than 10. They mean the same thing.",
             do=[B("y < 10", x=80, y=300, color=GREEN, at=3), T("the same inequality", x=360, y=318, color=GREY, at=5.4)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Finn lists the integers that satisfy 4 is less than x, is less than 8. Which line goes wrong first?",
             do=LINES("Finn", "4 < x < 8", ["x is between 4 and 8", "so x = 4, 5, 6, 7, 8", "That is 5 integers."])),
        dict(say="Line 2 is wrong. 4 is not greater than 4, and 8 is not less than 8. The end values are not included.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="The integers are 5, 6 and 7. That is 3 integers.", do=[B("5, 6, 7", x=110, y=480, color=GREEN), T("3 integers", x=420, y=498, at=1.8)]),
    ]),
    dict(kind="life", title="Inequalities on signs", steps=[
        dict(say="Inequalities are all around you. A speed limit sign means your speed must not be more than the number shown.",
             do=[E("🚗", 90, 170, 90), T("Speed limits, height limits, age limits…", x=210, y=195)]),
        dict(say="A lift that carries fewer than 8 people: the number of people, p, is less than 8.", do=[E("🛗", 90, 300, 90), B("p < 8", x=210, y=312, color=BLUE)]),
        dict(say="And water is liquid between its freezing and boiling points. At sea level, that is between 0 and 100 degrees Celsius.",
             do=[E("💧", 90, 430, 90), B("0 < T < 100", x=210, y=442, color=RED, at=4)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("2.6-k4", "One last question. The integer n can be 1, 2, 3 or 4. Which inequality describes it? Pause the video and choose.",
              "Which inequality gives the integers n = 1, 2, 3, 4?"),
        dict(say="n must be greater than 0, so that it starts at 1. And less than 5, so that it stops at 4. The answer is 0 is less than n, is less than 5.",
             do=[INEQ(80, 170, 760, min=-2, max=7, a=0, b=5), B("0 < n < 5", x=80, y=420, color=GREEN, at=6)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: x greater than a, or x less than a. The value a itself is not included.", do=[T("• x > a or x < a: a itself is **not** included", x=80, y=170)]),
        dict(say="On a number line, draw an open circle at the boundary, and a line towards the values that work.", do=[T("• Open circle, then a line towards the values that work", x=80, y=250)]),
        dict(say="A double inequality means x is between two values.", do=[T("• a < x < b: x is **between** a and b", x=80, y=330)]),
        dict(say="When you list integers, leave out the boundary values.", do=[T("• Listing integers: leave out the boundaries", x=80, y=410)]),
    ]),
]
