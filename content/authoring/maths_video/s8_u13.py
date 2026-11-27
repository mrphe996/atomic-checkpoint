# -*- coding: utf-8 -*-
"""Stage 8 · Unit 13 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u07 import F

DICE = TBL(["+", "1", "2", "3", "4", "5", "6"], [[str(a)] + [str(a + b) for b in range(1, 7)] for a in range(1, 7)], x=700, y=140, id="d")
DROW = lambda i, at=0.3: dict(a="row", id="d", i=i, at=at)

VIDEOS = {}

VIDEOS["13.1"] = [
    dict(kind="hook", title="Two dice", steps=[
        dict(say="In a board game, you roll two dice and add the scores. You need a total of 7 to win.", do=[E("🎲", 90, 170, 100), T("roll **two dice**, add · you need **7**", x=230, y=200)]),
        dict(say="Is a total of 7 more likely than a total of 12?", do=[T("**7** or **12**: which is more likely?", x=230, y=300)]),
        PAUSE("13.1-k1", "Which total is more likely: 7 or 12? Pause the video and choose.", "More likely total?"),
    ]),
    dict(kind="hook", title="Count the ways", steps=[
        dict(say="There is only one way to make 12: 6 and 6. But there are six ways to make 7: 1 and 6, 2 and 5, 3 and 4, 4 and 3, 5 and 2, and 6 and 1. So 7 is much more likely.",
             do=[T("12: **6 + 6** only", x=80, y=180), T("7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1", x=80, y=270, at=4), B("7 is more likely", x=80, y=370, color=GREEN, at=10)]),
    ]),
    dict(kind="recall", title="Equally likely outcomes", steps=[
        dict(say="Remember: when outcomes are equally likely, the probability of an event is the number of favourable outcomes, divided by the total number of outcomes.",
             do=[B("P = favourable ÷ total", x=80, y=170, color=BLUE)]),
        dict(say="On a fair dice, the probability of a number less than 3 is 2 sixths, which is 1 third.", do=[MATH(f"P(less than 3) = {F(2, 6)} = {F(1, 3)}", x=80, y=280)]),
    ]),
    dict(kind="idea", title="Sample space diagrams", steps=[
        dict(say="For two dice, list every combination in a table. This is called a sample space diagram. Each dice has 6 scores, so there are 6 times 6 outcomes.",
             do=[T("a **sample space diagram**", x=80, y=170), DICE, DROW(0, 2), DROW(1, 2.6), DROW(2, 3.2), DROW(3, 3.8), DROW(4, 4.4), DROW(5, 5)]),
        PAUSE("13.1-k2", "Your turn. How many outcomes are there for two dice? Pause the video and work it out.", "How many outcomes for two dice?"),
    ]),
    dict(kind="idea", title="Check: 36 outcomes", steps=[
        dict(say="6 times 6 is 36 outcomes. The 7s lie along a diagonal. There are 6 of them, so the probability of 7 is 6 thirty-sixths, which is 1 sixth.",
             do=[DICE, DROW(0, 0), DROW(1, 0), DROW(2, 0), DROW(3, 0), DROW(4, 0), DROW(5, 0), B("36 outcomes", x=80, y=180, color=GREEN), MATH(f"P(7) = {F(6, 36)} = {F(1, 6)}", x=80, y=290, at=5)]),
    ]),
    dict(kind="idea", title="Complementary events", steps=[
        dict(say="An event and its complement, not the event, cover every outcome. So the probability of not A is 1 minus the probability of A.", do=[B("P(not A) = 1 − P(A)", x=80, y=170, color=BLUE)]),
        dict(say="The probability of a total that is not 7 is 1 minus 1 sixth, which is 5 sixths.", do=[MATH(f"P(not 7) = 1 − {F(1, 6)} = {F(5, 6)}", x=80, y=280)]),
        dict(say="And if outcomes cannot happen together, their probabilities add up to 1.", do=[T("all the outcomes together add up to **1**", x=80, y=390)]),
    ]),
    dict(kind="method", title="How do I calculate combined probabilities?", steps=[
        dict(say="Here is the method. Step 1: list all the equally likely outcomes, in a list or a sample space diagram.", do=[T("1. List **all** outcomes (sample space)", x=80, y=170)]),
        dict(say="Step 2: count the total, and the favourable outcomes.", do=[T("2. Count total and **favourable**", x=80, y=260)]),
        dict(say="Step 3: divide favourable by total, and simplify.", do=[T("3. **P = favourable ÷ total**; simplify", x=80, y=350)]),
        dict(say="Step 4: for not, or at least one, it can be quicker to use 1 minus.", do=[T("4. “not” or “at least one”? Use **1 −**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A coin and a dice", steps=[
        dict(say="A coin is tossed, and a dice is rolled. What is the probability of a head and an even number? There are 2 times 6, which is 12 outcomes.",
             do=[E("🪙", 90, 160, 80), T("H1 … H6, T1 … T6: **12** outcomes", x=230, y=180)]),
        dict(say="The favourable ones are head 2, head 4 and head 6. That is 3 out of 12, which is 1 quarter.", do=[MATH(f"{F(3, 12)} = {F(1, 4)}", x=230, y=290, color=GREEN)]),
        PAUSE("13.1-k3", "Your turn. With two dice, what is the probability of a total of 2? Pause and work it out.", "Two dice: P(total 2)?"),
    ]),
    dict(kind="example", title="Check: a total of 2", steps=[
        dict(say="The only way is 1 and 1. That is 1 outcome out of 36. The probability is 1 thirty-sixth.", do=[MATH(f"P(2) = {F(1, 36)}", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="example", title="A missing probability", steps=[
        dict(say="A spinner lands on red with probability 0.2, blue 0.35, and green 0.15. The rest is yellow. The known ones add up to 0.7. So yellow is 1 minus 0.7, which is 0.3.",
             do=[MATH("0.2 + 0.35 + 0.15 = 0.7", x=80, y=180), B("P(yellow) = 1 − 0.7 = 0.3", x=80, y=290, color=GREEN, at=8)]),
    ]),
    dict(kind="example", title="At least one six", steps=[
        dict(say="With two dice, what is the probability of at least one six? It is quicker to find the probability of no six. Each dice has 5 non-sixes, so 5 times 5 is 25 outcomes with no six.",
             do=[MATH(f"P(no six) = {F(25, 36)}", x=80, y=180)]),
        dict(say="So the probability of at least one six is 1 minus 25 thirty-sixths, which is 11 thirty-sixths.", do=[B(f"1 − {F(25, 36)} = {F(11, 36)}", x=80, y=300, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Lily finds the probability that two dice both show 6. Which line goes wrong first?", do=LINES("Lily", "P(both dice show 6)", ["outcomes: 6 + 6 = 12", "P = 1/12"])),
        dict(say="Line 1 is wrong. Each of the 6 scores on the first dice goes with each of the 6 on the second. That is 6 times 6, which is 36 outcomes.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="So the probability is 1 thirty-sixth.", do=[B(f"P = {F(1, 36)}", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Board game design", steps=[
        dict(say="Game designers use these probabilities. In some board games, the squares or tiles numbered 6 and 8 produce resources most often, because those totals are very likely with two dice.",
             do=[E("🎯", 90, 170, 100), T("totals near **7** come up most often", x=230, y=200)]),
        dict(say="Totals of 2 and 12 are rare, with a probability of only 1 thirty-sixth each.", do=[MATH(f"P(2) = P(12) = {F(1, 36)}", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("13.1-k4", "One last question. The probability of A is 0.45. What is the probability of not A? Pause the video and answer.", "P(A) = 0.45. P(not A)?"),
        dict(say="1 minus 0.45 is 0.55.", do=[B("1 − 0.45 = 0.55", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: list all the equally likely outcomes, with a sample space diagram.", do=[T("• List all outcomes (sample space diagram)", x=80, y=170)]),
        dict(say="The probability is favourable divided by total.", do=[T("• P = favourable ÷ total", x=80, y=250)]),
        dict(say="The probability of not A is 1 minus the probability of A.", do=[T("• P(not A) = 1 − P(A)", x=80, y=330)]),
        dict(say="Outcomes that cannot happen together add up to 1.", do=[T("• All the outcomes add up to 1", x=80, y=410)]),
    ]),
]

VIDEOS["13.2"] = [
    dict(kind="hook", title="A computer experiment", steps=[
        dict(say="A spreadsheet simulates rolling a dice 6,000 times. It gets 1,012 sixes.", do=[E("💻", 90, 170, 100), T("**6000** rolls · **1012** sixes", x=230, y=200)]),
        dict(say="How many sixes would you expect?", do=[T("how many would you **expect**?", x=230, y=300)]),
        PAUSE("13.2-k1", "How many sixes would you expect in 6,000 rolls? Pause the video and work it out.", "Expected sixes in 6000 rolls?"),
    ]),
    dict(kind="hook", title="About 1000", steps=[
        dict(say="The probability of a six is 1 sixth. 1 sixth of 6,000 is 1,000. So 1,012 is very close to what we expect.", do=[MATH(f"{F(1, 6)} × 6000 = 1000", x=80, y=190), B("1012 is very close", x=80, y=300, color=GREEN, at=5)]),
        dict(say="But what if there had only been 60 rolls, with 18 sixes? Would that be strange?", do=[T("60 rolls, 18 sixes?", x=80, y=400)]),
    ]),
    dict(kind="recall", title="Relative frequency", steps=[
        dict(say="Remember: the experimental probability, or relative frequency, is the frequency divided by the number of trials. 23 heads in 50 tosses is 0.46.",
             do=[B("relative frequency = frequency ÷ trials", x=80, y=170, color=BLUE), MATH("23 ÷ 50 = 0.46", x=80, y=280, at=6)]),
    ]),
    dict(kind="idea", title="Theoretical and experimental", steps=[
        dict(say="Theoretical probability comes from equally likely outcomes. The probability of a six is 1 sixth, which is about 0.167.", do=[T(f"**theoretical**: P(six) = {F(1, 6)} ≈ 0.167", x=80, y=170)]),
        dict(say="Experimental probability comes from trials. With only a few trials, the results can be far off. With many trials, they get closer to the theoretical value.",
             do=[T("**experimental**: from trials", x=80, y=270), T("more trials → **closer** to the theory", x=80, y=350, color=BLUE)]),
        PAUSE("13.2-k2", "Your turn. Write 1,012 divided by 6,000 to 3 decimal places. Pause the video and try it.", "1012 / 6000 to 3 d.p.?"),
    ]),
    dict(kind="idea", title="Check: 1012 ÷ 6000", steps=[
        dict(say="1,012 divided by 6,000 is 0.1686, which is 0.169 to 3 decimal places. Very close to 0.167. But 18 sixes in 60 rolls is 0.3, which is far off. With so few rolls, that can still happen by chance.",
             do=[MATH("1012 ÷ 6000 = 0.169", x=80, y=180, color=GREEN), MATH("18 ÷ 60 = 0.3", x=80, y=280, at=8)]),
    ]),
    dict(kind="idea", title="Using relative frequency", steps=[
        dict(say="When outcomes are not equally likely, like a drawing pin landing point up, the relative frequency from many trials is the best estimate of the probability.",
             do=[E("📌", 80, 160, 80), T("not equally likely → use **relative frequency**", x=190, y=190)]),
        dict(say="The expected frequency is the probability times the number of trials. A fair coin tossed 300 times should give about 150 heads.", do=[B("expected = P × trials", x=80, y=300, color=BLUE), MATH("0.5 × 300 = 150", x=80, y=400)]),
    ]),
    dict(kind="method", title="How do I compare them?", steps=[
        dict(say="Here is the method. Step 1: find the theoretical probability, if you can.", do=[T("1. **Theoretical** probability (if possible)", x=80, y=170)]),
        dict(say="Step 2: find the relative frequency: the frequency divided by the trials.", do=[T("2. **Relative frequency** = frequency ÷ trials", x=80, y=260)]),
        dict(say="Step 3: compare them. Think about how many trials there were.", do=[T("3. Compare; how many **trials**?", x=80, y=350)]),
        dict(say="Step 4: a big difference over many trials suggests the dice or spinner is biased.", do=[T("4. Big difference, many trials → **biased**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Is it biased?", steps=[
        dict(say="A dice is rolled 600 times, and lands on 4 a total of 160 times. Is it biased? We would expect 600 divided by 6, which is 100 fours.",
             do=[MATH("expected: 600 ÷ 6 = 100", x=80, y=180)]),
        dict(say="160 is far more than 100, over many trials. So the dice is probably biased towards 4.", do=[B("probably biased", x=80, y=290, color=RED)]),
    ]),
    dict(kind="example", title="More trials", steps=[
        dict(say="A coin gives 7 heads in 10 tosses, 56 in 100, and 503 in 1,000. The relative frequencies are 0.7, 0.56, and 0.503. They get closer to 0.5 as the trials go up.",
             do=[TBL(["Tosses", "10", "100", "1000"], [["Heads", "7", "56", "503"], ["Rel. freq.", "0.7", "0.56", "0.503"]], y=170), ROW(0, 1), ROW(1, 6)]),
        PAUSE("13.2-k3", "Your turn. Where does the most reliable estimate come from? Pause and choose.", "Most reliable estimate comes from …"),
    ]),
    dict(kind="example", title="Check: the most trials", steps=[
        dict(say="The most reliable estimate comes from the most trials. Two groups can also combine their results. 14 reds in 50 spins, and 66 in 250, make 80 reds in 300 spins, which is about 0.27.",
             do=[B("the most trials", x=80, y=180, color=GREEN), MATH("80 ÷ 300 ≈ 0.27", x=80, y=290, at=6)]),
    ]),
    dict(kind="example", title="Estimating from an experiment", steps=[
        dict(say="A pin lands point up 128 times in 400 drops. Estimate how many times it will land point up in 2,500 drops. 128 divided by 400 is 0.32. 0.32 times 2,500 is 800.",
             do=[MATH("128 ÷ 400 = 0.32", x=80, y=180), B("0.32 × 2500 ≈ 800", x=80, y=290, color=GREEN, at=8)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A coin is tossed 8 times and gives 6 heads. Which line is wrong?", do=LINES("Kai", "6 heads in 8 tosses", ["relative frequency of heads = 0.75", "so the coin is biased"])),
        dict(say="Line 2 is wrong. 8 trials is far too few. 6 heads in 8 tosses happens quite often with a fair coin.", do=[dict(a="cross", id="l2")]),
        dict(say="Toss it many more times before deciding.", do=[B("you need many more trials", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Weather forecasts", steps=[
        dict(say="Weather forecasts use experimental probability. A 70 percent chance of rain means that on past days with very similar conditions, it rained on about 70 percent of them.",
             do=[E("🌦️", 90, 170, 100), T("70% chance of rain = rain on about **70%** of similar days", x=230, y=200)]),
        dict(say="The more past data the forecasters have, the more reliable the estimate.", do=[T("more data → more **reliable**", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("13.2-k4", "One last question. The probability is 0.15, and there are 400 trials. What is the expected frequency? Pause the video and answer.", "P = 0.15; 400 trials. Expected?"),
        dict(say="0.15 times 400 is 60.", do=[B("0.15 × 400 = 60", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: theoretical probability comes from equally likely outcomes. Experimental probability is frequency divided by trials.", do=[T("• Theoretical vs experimental (frequency ÷ trials)", x=80, y=170)]),
        dict(say="More trials get closer to the true probability.", do=[T("• More trials → closer to the true probability", x=80, y=250)]),
        dict(say="Expected frequency equals probability times trials.", do=[T("• Expected frequency = P × trials", x=80, y=330)]),
        dict(say="A large difference over many trials suggests bias.", do=[T("• Big difference over many trials → bias", x=80, y=410)]),
    ]),
]
