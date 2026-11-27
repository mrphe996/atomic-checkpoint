# -*- coding: utf-8 -*-
"""Stage 9 · Unit 12 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

VIDEOS = {}

VIDEOS["12.1"] = [
    dict(kind="hook", title="A raffle", steps=[
        dict(say="A raffle has tickets numbered 1 to 30. One ticket is drawn. You win a prize if the number is a multiple of 7, or a multiple of 11.",
             do=[E("🎟️", 90, 170, 100), T("tickets **1–30** · win: multiple of **7** or of **11**", x=230, y=200)]),
        PAUSE("12.1-k1", "Can a number from 1 to 30 be a multiple of both 7 and 11? Pause the video and choose: no, or yes.", "Multiple of 7 and 11?"),
    ]),
    dict(kind="hook", title="No", steps=[
        dict(say="No. The first number that is a multiple of both is 77, which is too big.", do=[B("No – the first is 77", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Probability", steps=[
        dict(say="Remember: the probability of an event is the number of favourable outcomes, divided by the total number of outcomes.", do=[MATH("P = favourable ÷ total", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Mutually exclusive", steps=[
        dict(say="Events are mutually exclusive if they cannot happen at the same time. Multiples of 7 up to 30 are 7, 14, 21 and 28. Multiples of 11 are 11 and 22. None is in both.",
             do=[T("**mutually exclusive**: can't both happen", x=80, y=170), MATH("7, 14, 21, 28 · 11, 22", x=80, y=260, at=6)]),
        dict(say="For mutually exclusive events, the probability of A or B is the probability of A plus the probability of B.", do=[B("P(A or B) = P(A) + P(B)", x=80, y=360, color=BLUE)]),
        PAUSE("12.1-k2", "Your turn. What is the probability of winning the raffle? Give your answer as a fraction in its simplest form. Pause the video and try it.", "P(win the raffle)?"),
    ]),
    dict(kind="idea", title="Check: 1/5", steps=[
        dict(say="4 thirtieths plus 2 thirtieths is 6 thirtieths, which is a fifth.", do=[B("4/30 + 2/30 = 6/30 = 1/5", x=80, y=190, color=GREEN)]),
        dict(say="Multiples of 3 and even numbers are not mutually exclusive: 6 and 12 are both. Adding would count them twice.", do=[T("multiples of 3 and evens: **overlap** (6, 12, …)", x=80, y=300)]),
    ]),
    dict(kind="idea", title="Adding to 1", steps=[
        dict(say="If mutually exclusive events cover every outcome, their probabilities add up to 1. Here is a spinner.",
             do=[TBL(["Colour", "Red", "Blue", "Green", "Yellow"], [["Probability", "0.3", "0.25", "0.15", "?"]], y=170), ROW(0, 3)]),
        PAUSE("12.1-k3", "Your turn. What is the probability of yellow? Pause and work it out.", "P(yellow)?"),
    ]),
    dict(kind="idea", title="Check: 0.3", steps=[
        dict(say="The others add up to 0.7. 1 minus 0.7 is 0.3.", do=[B("1 − 0.7 = 0.3", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I combine these events?", steps=[
        dict(say="Here is the method. Step 1: check they cannot happen together.", do=[T("1. Can they **both** happen?", x=80, y=170)]),
        dict(say="Step 2: if not, add their probabilities.", do=[T("2. If not: **add**", x=80, y=260)]),
        dict(say="Step 3: if they overlap, list and count the outcomes instead.", do=[T("3. Overlap: **list and count**", x=80, y=350)]),
        dict(say="Step 4: all outcomes together add up to 1.", do=[T("4. All outcomes total **1**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="On a dice: less than 3, or a 6. That is 2 sixths plus 1 sixth, which is a half.", do=[MATH("2/6 + 1/6 = 1/2", x=80, y=180)]),
        dict(say="A spinner: P of A is 0.42, P of B is 0.18, P of C is X, and P of D is 2 X. 3 X equals 0.4, so X is 2 fifteenths.", do=[MATH("0.6 + 3x = 1 → x = 2/15", x=80, y=280)]),
        dict(say="The probability of winning a game is 0.15. In 200 games, you expect about 30 wins.", do=[MATH("0.15 × 200 = 30", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="On a dice, Ahmed finds the probability of even, or greater than 3. Which line is wrong?", do=LINES("Ahmed", "dice: P(even or greater than 3)", ["3/6 + 3/6 = 1"])),
        dict(say="Line 1 is wrong. 4 and 6 are in both, so the events overlap.", do=[dict(a="cross", id="l1")]),
        dict(say="The outcomes are 2, 4, 5 and 6. That is 4 sixths, or 2 thirds.", do=[B("{2, 4, 5, 6} → 4/6 = 2/3", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Game design", steps=[
        dict(say="Game designers add the probabilities of separate rewards, to make sure all the chances add up to exactly 1.", do=[E("🎮", 90, 170, 100), T("all rewards together = **1**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.1-k4", "One last question. On a dice, are even and odd mutually exclusive, or not mutually exclusive? Pause the video and choose.", "'even' and 'odd' on a dice are …"),
        dict(say="Mutually exclusive. No number is both even and odd.", do=[B("mutually exclusive", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: mutually exclusive events cannot both happen.", do=[T("• Mutually exclusive: can't both happen", x=80, y=170)]),
        dict(say="Then P of A or B is P of A plus P of B.", do=[T("• P(A or B) = P(A) + P(B)", x=80, y=250)]),
        dict(say="All the outcomes add up to 1.", do=[T("• All outcomes total 1", x=80, y=330)]),
        dict(say="If events overlap, count instead of adding.", do=[T("• Overlap: count, don't add", x=80, y=410)]),
    ]),
]

VIDEOS["12.2"] = [
    dict(kind="hook", title="Five heads", steps=[
        dict(say="A coin lands heads five times in a row. A friend says: tails is due next, it is more likely now!",
             do=[E("🪙", 90, 170, 100), T("H H H H H … **'tails is due!'**", x=230, y=200)]),
        PAUSE("12.2-k1", "Is tails more likely now? Pause the video and choose: no, it is still a half, or yes.", "Is tails more likely now?"),
    ]),
    dict(kind="hook", title="Still a half", steps=[
        dict(say="No. The coin has no memory. The probability of tails is still a half.", do=[B("No – still ½", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="One event", steps=[
        dict(say="Remember: for a fair coin, the probability of a head is a half.", do=[MATH("P(head) = ½", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Independent events", steps=[
        dict(say="Two events are independent if one happening does not change the probability of the other. Two spins of a spinner, or two tosses of a coin, are independent.",
             do=[T("**independent**: one doesn't change the other", x=80, y=170)]),
        dict(say="Believing that tails is due is called the gambler's fallacy.", do=[T("'tails is due' = the **gambler's fallacy**", x=80, y=270)]),
        PAUSE("12.2-k2", "Your turn. Taking a counter and putting it back before the next pick. Does that make the events independent, or dependent? Pause the video and choose.", "Picking with replacement makes events …"),
    ]),
    dict(kind="idea", title="Check: independent", steps=[
        dict(say="Independent. With replacement, the bag is the same every time.", do=[B("independent", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Dependent events", steps=[
        dict(say="Events are dependent if one affects the other. A bag has 10 balls, numbered 1 to 10. Take one out, and do not put it back. Now 9 balls are left.",
             do=[T("**dependent**: one changes the other", x=80, y=170), T("10 balls, 1–10 · one taken, **not replaced**", x=80, y=260)]),
        dict(say="If the first ball was odd, 5 even balls are left out of 9. So the chance the second is even is 5 ninths.", do=[MATH("first odd → P(second even) = 5/9", x=80, y=350)]),
        PAUSE("12.2-k3", "Your turn. If the first ball was even, and not replaced, what is the probability the second is even? Give a fraction. Pause and work it out.", "First ball even (not replaced). P(second even)?"),
    ]),
    dict(kind="idea", title="Check: 4/9", steps=[
        dict(say="4 even balls are left, out of 9. The probability is 4 ninths.", do=[B("4/9", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I decide?", steps=[
        dict(say="Here is the method. Step 1: does the first result change what can happen next?", do=[T("1. Does the first **change** the next?", x=80, y=170)]),
        dict(say="Step 2: with replacement: independent.", do=[T("2. Replaced → **independent**", x=80, y=260)]),
        dict(say="Step 3: without replacement: dependent. Recount what is left.", do=[T("3. Not replaced → **dependent**; recount", x=80, y=350)]),
        dict(say="Step 4: in real life, think about whether one event really affects the other.", do=[T("4. Real life: **think** it through", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="A bag has 3 red and 7 blue counters. The first is red, and it is not replaced. 2 red are left, out of 9. The chance the second is red is 2 ninths.", do=[MATH("P(2nd red) = 2/9 – dependent", x=80, y=180)]),
        dict(say="It rains today, and it rains tomorrow: probably dependent, because weather comes in spells.", do=[MATH("rain today, rain tomorrow → probably dependent", x=80, y=280)]),
        dict(say="A fair dice gave three 2s in a row. The chance of a 2 next is still 1 sixth.", do=[MATH("P(2 next) = 1/6", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A roulette wheel has landed on red 6 times. Jack thinks about the next spin. Which line is wrong?", do=LINES("Jack", "red 6 times in a row", ["black is now more likely"])),
        dict(say="Line 1 is wrong. The spins are independent.", do=[dict(a="cross", id="l1")]),
        dict(say="The probability of black has not changed.", do=[B("P(black) is unchanged", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Casinos", steps=[
        dict(say="Casinos make money partly because players believe in the gambler's fallacy, and keep betting on the result that seems due.", do=[E("🎰", 90, 170, 100), T("the **gambler's fallacy**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.2-k4", "One last question. Roll a 6 on a dice, and toss a head on a coin. Independent, or dependent? Pause the video and choose.", "'roll a 6' and 'toss a head' are …"),
        dict(say="Independent. The dice cannot affect the coin.", do=[B("independent", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: independent means one does not affect the other.", do=[T("• Independent: no effect", x=80, y=170)]),
        dict(say="With replacement: independent.", do=[T("• With replacement → independent", x=80, y=250)]),
        dict(say="Without replacement: dependent.", do=[T("• Without replacement → dependent", x=80, y=330)]),
        dict(say="Coins and dice have no memory.", do=[T("• Coins and dice have no memory", x=80, y=410)]),
    ]),
]

VIDEOS["12.3"] = [
    dict(kind="hook", title="Traffic lights", steps=[
        dict(say="On the way to school, Lin passes two sets of traffic lights. They work independently. The chance each one is green when she arrives is 0.4.",
             do=[E("🚦", 90, 170, 100), T("two lights · P(green) = **0.4** each", x=230, y=200)]),
        PAUSE("12.3-k1", "What is the probability that both are green? Pause the video and work it out.", "P(both green)?"),
    ]),
    dict(kind="hook", title="0.16", steps=[
        dict(say="0.4 times 0.4 is 0.16.", do=[B("0.4 × 0.4 = 0.16", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Independent events", steps=[
        dict(say="Remember: independent events do not affect each other.", do=[T("independent: no effect on each other", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Multiply for 'and'", steps=[
        dict(say="For independent events, the probability of A and B is P of A times P of B. A head and more than 2 on a dice: a half times 2 thirds is a third.",
             do=[B("P(A and B) = P(A) × P(B)", x=80, y=170, color=BLUE), MATH("½ × ⅔ = ⅓", x=80, y=280, at=8)]),
        dict(say="A tree diagram shows every outcome. Each light is green, G, or not green, N. Not green has probability 0.6.",
             do=[TBL(["Outcome", "Probability"], [["GG", "0.4 × 0.4 = 0.16"], ["GN", "?"], ["NG", "?"], ["NN", "0.6 × 0.6 = 0.36"]], y=360), ROW(0, 3), ROW(2, 5), ROW(3, 6)]),
        PAUSE("12.3-k2", "Your turn. The first light is green, and the second is not. What is P of G N? Pause the video and try it.", "P(GN)?"),
    ]),
    dict(kind="idea", title="Check: 0.24", steps=[
        dict(say="0.4 times 0.6 is 0.24. Multiply along the branches. The four outcomes add up to 1.", do=[B("0.4 × 0.6 = 0.24", x=80, y=190, color=GREEN), MATH("0.16 + 0.24 + 0.24 + 0.36 = 1 ✓", x=80, y=300)]),
        dict(say="To combine different routes, add.", do=[T("multiply **along**, **add** between routes", x=80, y=400)]),
    ]),
    dict(kind="method", title="How do I combine events?", steps=[
        dict(say="Here is the method. Step 1: draw a tree diagram with all the outcomes.", do=[T("1. Draw a **tree**", x=80, y=170)]),
        dict(say="Step 2: branches from one point add up to 1.", do=[T("2. Branches from a point total **1**", x=80, y=260)]),
        dict(say="Step 3: multiply along each route.", do=[T("3. **Multiply** along", x=80, y=350)]),
        dict(say="Step 4: add the routes you want.", do=[T("4. **Add** the routes you want", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="A spinner has a probability of winning of a fifth. It is spun twice. The chance of winning both is 1 twenty-fifth.", do=[MATH("1/5 × 1/5 = 1/25", x=80, y=180)]),
        dict(say="The bus is late with probability 0.2, and it rains with probability 0.3. They are independent. The chance of neither is 0.8 times 0.7, which is 0.56.", do=[MATH("0.8 × 0.7 = 0.56", x=80, y=280)]),
        PAUSE("12.3-k3", "Your turn. What is the probability that exactly one light is green? Pause and work it out.", "P(exactly one green)?"),
    ]),
    dict(kind="example", title="Check: 0.48", steps=[
        dict(say="Two routes: G N and N G. 0.24 plus 0.24 is 0.48.", do=[B("0.24 + 0.24 = 0.48", x=80, y=190, color=GREEN)]),
        dict(say="Over 50 school days, both lights are green on about 0.16 times 50, which is 8 days.", do=[MATH("0.16 × 50 = 8 days", x=80, y=300)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Each light is green with probability 0.4. Emma finds the probability both are green. Which line is wrong?", do=LINES("Emma", "P(both green), each 0.4", ["0.4 + 0.4 = 0.8"])),
        dict(say="Line 1 is wrong. For and, with independent events, multiply.", do=[dict(a="cross", id="l1")]),
        dict(say="0.4 times 0.4 is 0.16.", do=[B("0.4 × 0.4 = 0.16", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Reliable machines", steps=[
        dict(say="Engineers multiply the chances that independent parts fail, to work out how reliable a whole machine is.", do=[E("⚙️", 90, 170, 100), T("multiply failure chances", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.3-k4", "One last question. What is the probability that at least one light is green? Pause the video and answer.", "P(at least one green)?"),
        dict(say="At least one is everything except none. 1 minus 0.36 is 0.64.", do=[B("1 − 0.36 = 0.64", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: for independent events, and means multiply.", do=[T("• Independent 'and' → multiply", x=80, y=170)]),
        dict(say="Tree diagrams: multiply along, add between routes.", do=[T("• Multiply along, add between", x=80, y=250)]),
        dict(say="Branches from one point add up to 1.", do=[T("• Branches total 1", x=80, y=330)]),
        dict(say="At least one is 1 minus P of none.", do=[T("• At least one = 1 − P(none)", x=80, y=410)]),
    ]),
]

VIDEOS["12.4"] = [
    dict(kind="hook", title="A fair dice?", steps=[
        dict(say="Sami thinks a dice is biased. He rolls it 50 times, and gets 14 sixes. What would you expect from a fair dice?",
             do=[E("🎲", 90, 170, 100), T("**50** rolls · **14** sixes", x=230, y=200)]),
        PAUSE("12.4-k1", "How many sixes would you expect in 50 rolls of a fair dice, to 1 decimal place? Pause the video and work it out.", "Expected sixes in 50 rolls (1 d.p.)?"),
    ]),
    dict(kind="hook", title="About 8.3", steps=[
        dict(say="1 sixth of 50 is about 8.3. He got 14, which is more. But is that enough evidence?", do=[B("50 ÷ 6 ≈ 8.3", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Relative frequency", steps=[
        dict(say="Remember: relative frequency is the frequency divided by the number of trials.", do=[MATH("relative frequency = frequency ÷ trials", x=80, y=190)]),
    ]),
    dict(kind="idea", title="More and more trials", steps=[
        dict(say="Sami keeps rolling, and records the relative frequency as the number of rolls grows.",
             do=[TBL(["Rolls", "10", "50", "100", "500"], [["Sixes", "2", "14", "22", "84"], ["Rel. freq.", "0.2", "0.28", "0.22", "?"]], y=170), ROW(0, 2), ROW(1, 4)]),
        PAUSE("12.4-k2", "Your turn. What is the relative frequency after 500 rolls? Pause the video and try it.", "Relative frequency after 500 rolls?"),
    ]),
    dict(kind="idea", title="Check: 0.168", steps=[
        dict(say="84 divided by 500 is 0.168. That is very close to 1 sixth, about 0.167. The dice looks fair after all.", do=[B("84 ÷ 500 = 0.168 ≈ 1/6", x=80, y=190, color=GREEN)]),
        dict(say="Small samples can mislead. Large samples give better estimates.", do=[T("more trials → a **better** estimate", x=80, y=300, color=BLUE)]),
    ]),
    dict(kind="idea", title="Estimating", steps=[
        dict(say="Sometimes there is no theoretical probability, like a drawing pin landing point up. Then you must experiment.", do=[E("📌", 90, 170, 90), T("no theory → **experiment**", x=230, y=200)]),
        PAUSE("12.4-k3", "Your turn. What is the best estimate of the probability a pin lands point up: the relative frequency from many drops, or a half? Pause and choose.", "Best estimate of P(pin point up)?"),
    ]),
    dict(kind="idea", title="Check: relative frequency", steps=[
        dict(say="The relative frequency from many drops. There is no reason for it to be a half.", do=[B("relative frequency from many drops", x=80, y=190, color=GREEN)]),
        dict(say="Expected frequency is the probability times the number of trials.", do=[MATH("expected = P × trials", x=80, y=300)]),
    ]),
    dict(kind="method", title="How do I analyse an experiment?", steps=[
        dict(say="Here is the method. Step 1: find the relative frequency.", do=[T("1. **Relative frequency**", x=80, y=170)]),
        dict(say="Step 2: compare it with the theoretical probability, if there is one.", do=[T("2. Compare with **theory**", x=80, y=260)]),
        dict(say="Step 3: think about the number of trials. More is more reliable.", do=[T("3. How **many** trials?", x=80, y=350)]),
        dict(say="Step 4: use the best estimate to predict.", do=[T("4. **Predict**: P × trials", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Examples", steps=[
        dict(say="A spinner has 4 equal sections. In 1,000 spins, red comes up 380 times. A fair spinner gives about 250. It is probably biased towards red.", do=[MATH("380 vs 250 → probably biased", x=80, y=180)]),
        dict(say="A pin lands point up 62 times in 200 drops. The estimate is 0.31. In 1,500 drops, expect about 465.", do=[MATH("62 ÷ 200 = 0.31 → 0.31 × 1500 = 465", x=80, y=280)]),
        dict(say="Combine results for a better estimate. 9 sixes in 60, and 41 in 240: 50 in 300, about 0.167.", do=[MATH("50 ÷ 300 ≈ 0.167", x=80, y=380)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Sami got 14 sixes in 50 rolls. Which line is wrong?", do=LINES("Sami", "14 sixes in 50 rolls", ["0.28 is much more than 0.167", "so the dice is definitely biased"])),
        dict(say="Line 2 is wrong. 50 rolls is too few to be sure.", do=[dict(a="cross", id="l2")]),
        dict(say="After 500 rolls, the relative frequency was 0.168, close to fair.", do=[B("500 rolls: 0.168 – close to fair", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Medical trials", steps=[
        dict(say="Medical trials test new treatments on thousands of people, so that the results are reliable.", do=[E("💊", 90, 170, 100), T("**thousands** of people → reliable", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("12.4-k4", "One last question. The probability is 0.31, and there are 1,000 trials. How many do you expect? Pause the video and answer.", "P = 0.31, 1000 trials. Expected?"),
        dict(say="0.31 times 1,000 is 310.", do=[B("0.31 × 1000 = 310", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: relative frequency is frequency divided by trials.", do=[T("• Relative frequency = frequency ÷ trials", x=80, y=170)]),
        dict(say="With many trials, it settles near the true probability.", do=[T("• Many trials → near the true P", x=80, y=250)]),
        dict(say="Expected frequency is P times trials.", do=[T("• Expected = P × trials", x=80, y=330)]),
        dict(say="Do not judge bias from a few trials.", do=[T("• Don't judge from a few trials", x=80, y=410)]),
    ]),
]
