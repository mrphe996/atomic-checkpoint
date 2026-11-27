# -*- coding: utf-8 -*-
"""Stage 7 · Unit 13 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREY, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW
from .s7_u07 import F

INK = "#1F2A37"
def SCALE(marks=(), x=90, y=420, at=0, w=1100):
    """The probability scale from 0 to 1; marks = [(value, label, colour)] drawn as dots above the line."""
    px = lambda v: 60 + v * 980
    s = f'<line x1="60" y1="90" x2="1040" y2="90" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
    for v, lab, anchor in ((0, "0 · impossible", "start"), (0.5, "0.5 · even chance", "middle"), (1, "1 · certain", "end")):   # end labels stay inside the box
        s += f'<line x1="{px(v)}" y1="74" x2="{px(v)}" y2="106" stroke="{INK}" stroke-width="4"/><text x="{px(v) + (-52 if anchor == "start" else 52 if anchor == "end" else 0)}" y="140" font-size="24" font-weight="700" text-anchor="{anchor}" fill="{INK}">{lab}</text>'
    for v, lab, c in marks:
        s += f'<circle cx="{px(v)}" cy="90" r="13" fill="{c}"/><text x="{px(v)}" y="52" font-size="26" font-weight="700" text-anchor="middle" fill="{c}">{lab}</text>'
    return T(f'<svg viewBox="0 0 1100 160" width="{w}" height="{w * 160 // 1100}">{s}</svg>', x=x, y=y, at=at)
BALLS = lambda s, x=80, y=200, at=0, size=54: T(f'<span style="font-size:{size}px;letter-spacing:6px">{s}</span>', x=x, y=y, at=at)
BAG = "🔴" * 5 + "🟢" * 3 + "🟡" * 2

VIDEOS = {}

VIDEOS["13.1"] = [
    dict(kind="hook", title="Will it rain tomorrow?", steps=[
        dict(say="A weather app says there is a 70 per cent chance of rain tomorrow.", do=[E("🌧️", 90, 150, 110), B("70% chance of rain", x=240, y=180, color=BLUE)]),
        dict(say="Your friend says rain is likely. Your little brother says rain is certain.", do=[T("friend: “**likely**” · brother: “**certain**”", x=240, y=310)]),
        PAUSE("13.1-k1", "Who is right? Is a 70 per cent chance likely, certain, or unlikely? Pause the video and decide.", "A 70% chance of rain is likely, certain or unlikely?"),
    ]),
    dict(kind="hook", title="Likely, but not certain", steps=[
        dict(say="Your friend is right. 70 per cent is more than an even chance, so rain is likely.", do=[B("likely", x=80, y=170, color=GREEN), SCALE([(0.7, "70%", BLUE)])]),
        dict(say="But it is not certain. There is still a 30 per cent chance that it stays dry.", do=[T("30% chance it stays **dry**", x=80, y=290)]),
    ]),
    dict(kind="recall", title="Fractions, decimals, percentages", steps=[
        dict(say="Remember: one half is 0.5, or 50 per cent. One quarter is 0.25, or 25 per cent. And 70 per cent is 0.7.", do=[MATH(f"{F(1, 2)} = 0.5 = 50%", x=80, y=170), MATH(f"{F(1, 4)} = 0.25 = 25%", x=80, y=300, at=3.6), MATH("70% = 0.7", x=80, y=430, at=7.4)]),
    ]),
    dict(kind="idea", title="The language of chance", steps=[
        dict(say="Probability measures how likely something is to happen. Words help, but numbers are more precise.", do=[T("**Probability**: how likely something is", x=80, y=150)]),
        dict(say="Impossible means it cannot happen. Its probability is 0.",
             do=[TBL(["Word", "Meaning", "Probability"], [["impossible", "cannot happen", "0"], ["unlikely", "less than an even chance", "between 0 and 0.5"], ["even chance", "as likely as not", "0.5"], ["likely", "more than an even chance", "between 0.5 and 1"], ["certain", "must happen", "1"]], y=230), ROW(0, 0.3)]),
        dict(say="Unlikely means less than an even chance. An even chance is a probability of 0.5. Likely means more than an even chance.", do=[ROW(1, 0.3), ROW(2, 3), ROW(3, 6)]),
        PAUSE("13.1-k2", "Your turn. What does a probability of 1 mean: certain, or an even chance? Pause the video and decide.", "Probability 1 means certain or even chance?"),
    ]),
    dict(kind="idea", title="Check: probability 1", steps=[
        dict(say="A probability of 1 means certain. The event must happen.", do=[B("1 = certain", x=80, y=180, color=GREEN), SCALE([(1, "certain", GREEN)])]),
    ]),
    dict(kind="idea", title="The probability scale", steps=[
        dict(say="All probabilities sit on a scale from 0 to 1. 0 is impossible, and 1 is certain.", do=[SCALE(), T("from **0** (impossible) to **1** (certain)", x=80, y=160)]),
        dict(say="You can write a probability as a fraction, a decimal or a percentage.", do=[MATH(f"{F(7, 10)} = 0.7 = 70%", x=80, y=250)]),
        dict(say="But a probability is never less than 0, and never more than 1.", do=[T("never below 0, never above 1", x=640, y=280, color=RED)]),
    ]),
    dict(kind="method", title="How do I place an event on the scale?", steps=[
        dict(say="Here is the method. Step 1: ask 3 questions. Can it never happen? Must it happen? Is it 50 50?", do=[T("1. Never (**0**)? Must (**1**)? 50–50 (**0.5**)?", x=80, y=170)]),
        dict(say="Step 2: if not, decide if it is more likely or less likely than an even chance.", do=[T("2. More or less likely than **even**?", x=80, y=260)]),
        dict(say="Step 3: if you have a number, change it to a decimal and place it on the scale.", do=[T("3. A number? Change it to a **decimal**", x=80, y=350)]),
        dict(say="Step 4: to compare probabilities, write them all in the same form.", do=[T("4. To compare: use the **same form**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Placing events", steps=[
        dict(say="Place 3 events on the scale. First: rolling a 7 on a normal dice. A dice only has the numbers 1 to 6, so this is impossible. The probability is 0.", do=[E("🎲", 90, 150, 80), T("rolling a 7: **impossible**", x=200, y=170), SCALE([(0, "a 7", RED)])]),
        dict(say="Second: a coin landing on heads. That is an even chance: 0.5.", do=[E("🪙", 90, 250, 80), T("heads: **even chance**", x=200, y=270), SCALE([(0.5, "heads", BLUE)])]),
        dict(say="Third: the day after Monday being Tuesday. That is certain. The probability is 1.", do=[E("📅", 640, 150, 80), T("Tuesday after Monday: **certain**", x=750, y=170), SCALE([(1, "Tuesday", GREEN)])]),
    ]),
    dict(kind="example", title="Comparing probabilities", steps=[
        dict(say="Which is more likely: an event with probability 7 tenths, or an event with probability 68 per cent?", do=[MATH(f"{F(7, 10)} or 68%", x=80, y=150)]),
        dict(say="Write both as decimals. 7 tenths is 0.7. 68 per cent is 0.68.", do=[MATH("0.7 and 0.68", x=80, y=290, color=BLUE)]),
        dict(say="0.7 is bigger. So 7 tenths is more likely.", do=[MATH(f"0.7 > 0.68 → {F(7, 10)}", x=80, y=380, color=GREEN)]),
        PAUSE("13.1-k3", "Your turn. Which is more likely: 0.45, or 2 fifths? Pause the video and try it.", "More likely: 0.45 or 2/5?"),
    ]),
    dict(kind="example", title="Check: 0.45 or 2/5", steps=[
        dict(say="2 fifths is 0.4. And 0.45 is bigger than 0.4. So 0.45 is more likely.", do=[MATH(f"{F(2, 5)} = 0.4", x=80, y=180), MATH("0.45 > 0.4", x=80, y=310, at=2.6), B("0.45", x=80, y=400, color=GREEN, at=4.6)]),
    ]),
    dict(kind="example", title="An impossible value", steps=[
        dict(say="Ella says the probability of her team winning is 1.3. Can she be right?", do=[E("⚽", 90, 150, 80), T("Ella: “the probability is **1.3**”", x=200, y=170)]),
        dict(say="No. Probabilities are between 0 and 1. And 1.3 is more than 1.", do=[SCALE(), B("No: 1.3 > 1", x=80, y=280, color=RED)]),
    ]),
    dict(kind="example", title="Ordering events", steps=[
        dict(say="Put these events in order, from least likely to most likely. A has probability 0.55. B has probability 3 fifths. C has probability 52 per cent.", do=[MATH(f"A: 0.55 · B: {F(3, 5)} · C: 52%", x=80, y=150)]),
        dict(say="Write them all as decimals: 0.55, 0.6 and 0.52.", do=[MATH("0.55, 0.6, 0.52", x=80, y=290, color=BLUE)]),
        dict(say="The smallest is 0.52, then 0.55, then 0.6. So the order is C, A, B.", do=[B("C, A, B", x=80, y=390, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A bag has 4 red sweets and 7 blue sweets. Find the probability of picking a red one. Here is Ali's working. Which line goes wrong first?",
             do=LINES("Ali", "4 red and 7 blue: the probability of red", ["red : blue = 4 : 7", "P(red) = 7/4"])),
        dict(say="Line 2 is wrong. 7 over 4 is more than 1, so it cannot be a probability. Divide the number of red sweets by the total number of sweets.", do=[dict(a="cross", id="l2")]),
        dict(say="There are 11 sweets altogether. The probability of red is 4 over 11.", do=[MATH(f"P(red) = {F(4, 11)}", x=110, y=400, color=GREEN)]),
    ]),
    dict(kind="life", title="Chance in everyday life", steps=[
        dict(say="Weather forecasters use probability every day. A 70 per cent chance of rain means: on 10 days like this one, it rains on about 7 of them.", do=[E("🌦️", 90, 160, 100), T("70%: rain on about **7 days in 10**", x=230, y=190)]),
        dict(say="A football match starts with a coin toss, because each captain has an even chance. That makes it fair.", do=[E("🪙", 90, 310, 100), T("coin toss: an **even chance** for each captain", x=230, y=340)]),
        dict(say="And doctors talk about risk in the same way: a number between 0 and 1.", do=[E("🩺", 90, 460, 100), T("risk: a number between **0** and **1**", x=230, y=490)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("13.1-k4", "One last question. Which of these is a valid probability: 3 quarters, 4 thirds, or 110 per cent? Pause the video and decide.", "Which is a valid probability: 3/4, 4/3 or 110%?"),
        dict(say="3 quarters. It is between 0 and 1. The other 2 are both more than 1.", do=[MATH(F(3, 4), x=80, y=160, color=GREEN), SCALE([(0.75, "3/4", GREEN)]), T("4/3 and 110% are **more than 1**", x=240, y=200, color=RED, at=3)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: probability goes from 0, impossible, to 1, certain. 0.5 is an even chance.", do=[T("• **0** impossible · **0.5** even chance · **1** certain", x=80, y=170)]),
        dict(say="The words are: impossible, unlikely, even chance, likely and certain.", do=[T("• impossible, unlikely, even chance, likely, certain", x=80, y=250)]),
        dict(say="Write probabilities as fractions, decimals or percentages.", do=[T("• Fractions, decimals or percentages", x=80, y=330)]),
        dict(say="A probability is never below 0, and never above 1.", do=[T("• Never below 0, never above 1", x=80, y=410)]),
    ]),
]

VIDEOS["13.2"] = [
    dict(kind="hook", title="Lucky dip", steps=[
        dict(say="A bag holds 5 red balls, 3 green balls and 2 yellow balls, all the same size. You take 1 without looking.", do=[BALLS(BAG, y=170), T("**5** red · **3** green · **2** yellow", x=80, y=290)]),
        PAUSE("13.2-k1", "What is the probability that the ball is green? Pause the video and work it out.", "5 red, 3 green, 2 yellow. What is the probability of green?"),
    ]),
    dict(kind="hook", title="Three out of ten", steps=[
        dict(say="There are 10 balls altogether, and 3 of them are green. So the probability of green is 3 out of 10: 3 tenths.", do=[BALLS(BAG, y=160), MATH(f"P(green) = {F(3, 10)}", x=80, y=280, color=GREEN)]),
        dict(say="The other 7 balls are not green. So the probability of not green is 7 tenths.", do=[MATH(f"P(not green) = {F(7, 10)}", x=80, y=430, color=BLUE)]),
    ]),
    dict(kind="recall", title="A fraction of a total", steps=[
        dict(say="Remember: 6 out of 15, as a fraction, is 6 over 15. That simplifies to 2 fifths.", do=[MATH(f"6 out of 15 = {F(6, 15)} = {F(2, 5)}", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Equally likely outcomes", steps=[
        dict(say="The outcomes are the possible results. Each ball is 1 outcome. They are all equally likely, because the balls are the same size.", do=[T("**Outcomes**: the possible results", x=80, y=150), T("all **equally likely**", x=80, y=230, at=3)]),
        dict(say="When outcomes are equally likely, the probability of an event is the number of outcomes you want, divided by the total number of outcomes.", do=[MATH("$$P(\\text{event}) = \\dfrac{\\text{outcomes you want}}{\\text{total outcomes}}$$", x=80, y=320, color=BLUE)]),
        dict(say="For red: 5 out of 10, which is one half.", do=[MATH(f"P(red) = {F(5, 10)} = {F(1, 2)}", x=80, y=480)]),
        PAUSE("13.2-k2", "Your turn. You roll a fair dice. What is the probability of a 6? Pause the video and try it.", "A fair dice: what is the probability of a 6?"),
    ]),
    dict(kind="idea", title="Check: rolling a 6", steps=[
        dict(say="A dice has 6 equally likely outcomes, and only 1 of them is a 6. The probability is 1 sixth.", do=[E("🎲", 90, 160, 100), T("6 outcomes · 1 is a six", x=230, y=190), MATH(f"P(6) = {F(1, 6)}", x=80, y=320, color=GREEN, at=3)]),
    ]),
    dict(kind="idea", title="Mutually exclusive outcomes", steps=[
        dict(say="Outcomes are mutually exclusive if they cannot happen at the same time. A ball cannot be red and green together.", do=[T("**Mutually exclusive**: cannot happen together", x=80, y=150), BALLS(BAG, y=220, size=44)]),
        dict(say="Add the probabilities of all the outcomes: 5 tenths, plus 3 tenths, plus 2 tenths. The total is 1.", do=[MATH(f"{F(5, 10)} + {F(3, 10)} + {F(2, 10)} = 1", x=80, y=310)]),
        dict(say="This always happens. So the probability of something not happening is 1, minus the probability that it does happen.", do=[B("P(not A) = 1 − P(A)", x=80, y=470, color=BLUE)]),
        PAUSE("13.2-k3", "Your turn. The probability of winning a game is 0.07. What is the probability of not winning? Pause the video and try it.", "P(win) = 0.07. P(not win)?"),
    ]),
    dict(kind="idea", title="Check: not winning", steps=[
        dict(say="1 minus 0.07 is 0.93. The probability of not winning is 0.93.", do=[MATH("1 − 0.07 = 0.93", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I calculate a probability?", steps=[
        dict(say="Here is the method. Step 1: list all the equally likely outcomes, and count them.", do=[T("1. Count **all** the outcomes", x=80, y=170)]),
        dict(say="Step 2: count the outcomes you want.", do=[T("2. Count the outcomes **you want**", x=80, y=260)]),
        dict(say="Step 3: divide, and simplify the fraction.", do=[T("3. **Divide**, then simplify", x=80, y=350)]),
        dict(say="Step 4: for the word not, subtract from 1.", do=[T("4. “Not”? **Subtract from 1**", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A spinner", steps=[
        dict(say="A fair spinner has 10 equal sections: 3 red, 5 white and 2 black. Find the probability of white, and the probability of not black.", do=[BALLS("🔴" * 3 + "⚪" * 5 + "⚫" * 2, y=150, size=46), T("10 equal sections", x=760, y=170, color=GREY)]),
        dict(say="White is 5 out of 10, which is one half.", do=[MATH(f"P(white) = {F(5, 10)} = {F(1, 2)}", x=80, y=260)]),
        dict(say="Black is 2 out of 10. So not black is 1 minus 2 tenths, which is 8 tenths, or 4 fifths.", do=[MATH(f"P(not black) = 1 − {F(2, 10)} = {F(8, 10)} = {F(4, 5)}", x=80, y=410, color=GREEN)]),
    ]),
    dict(kind="example", title="A missing probability", steps=[
        dict(say="A bag has only red, blue and green counters. The probability of red is 0.45. The probability of blue is 0.3. Find the probability of green.", do=[T("P(red) = **0.45** · P(blue) = **0.3** · P(green) = ?", x=80, y=160)]),
        dict(say="The 3 colours are mutually exclusive, so their probabilities add up to 1.", do=[T("they add up to **1**", x=80, y=260)]),
        dict(say="1 minus 0.45 minus 0.3 is 0.25. The probability of green is 0.25.", do=[MATH("1 − 0.45 − 0.3 = 0.25", x=80, y=360, color=GREEN)]),
    ]),
    dict(kind="example", title="Letters", steps=[
        dict(say="A letter is picked at random from the word MATHEMATICS. Find the probability that it is an M.", do=[B("M A T H E M A T I C S", x=80, y=160)]),
        dict(say="The word has 11 letters, and 2 of them are M. So the probability is 2 over 11.", do=[T("11 letters · 2 are M", x=80, y=280), MATH(f"P(M) = {F(2, 11)}", x=80, y=370, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="Not mutually exclusive", steps=[
        dict(say="You roll a dice. Are the events odd, and less than 4, mutually exclusive?", do=[E("🎲", 90, 150, 80), T("“odd” and “less than 4”", x=200, y=170)]),
        dict(say="The odd numbers are 1, 3 and 5. The numbers less than 4 are 1, 2 and 3.", do=[MATH("odd: 1, 3, 5", x=80, y=290), MATH("less than 4: 1, 2, 3", x=520, y=290, at=3)]),
        dict(say="1 and 3 are in both lists. So both events can happen together. They are not mutually exclusive.", do=[B("not mutually exclusive", x=80, y=410, color=RED)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A box has 3 white pens and 9 black pens. Find the probability of picking a white pen. Here is Nia's working. Which line goes wrong first?",
             do=LINES("Nia", "3 white and 9 black pens: the probability of white", ["pens I want = 3", "total = 9", "P(white) = 3/9 = 1/3"])),
        dict(say="Line 2 is wrong. The total is all the pens: 3 plus 9 is 12, not 9.", do=[dict(a="cross", id="l2"), dict(a="strike", id="l3", at=0.6)]),
        dict(say="The probability of white is 3 over 12, which is 1 quarter.", do=[MATH(f"P(white) = {F(3, 12)} = {F(1, 4)}", x=110, y=470, color=GREEN)]),
    ]),
    dict(kind="life", title="Cards and raffles", steps=[
        dict(say="A standard pack has 52 playing cards, and 13 of them are hearts. So the probability of picking a heart is 13 over 52, which is 1 quarter.", do=[E("🃏", 90, 160, 100), MATH(f"P(heart) = {F(13, 52)} = {F(1, 4)}", x=230, y=160)]),
        dict(say="In a raffle, 200 tickets are sold, and you buy 5. Your probability of winning the prize is 5 over 200, which is 1 in 40.", do=[E("🎟️", 90, 360, 100), MATH(f"P(win) = {F(5, 200)} = {F(1, 40)}", x=230, y=360)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("13.2-k4", "One last question. On 1 roll of a dice, are the events odd, and a 2, mutually exclusive or not? Pause the video and decide.", "On one dice roll, ‘odd’ and ‘a 2’ are mutually exclusive or not?"),
        dict(say="They are mutually exclusive. 2 is an even number, so you cannot roll an odd number and a 2 at the same time.", do=[B("mutually exclusive", x=80, y=190, color=GREEN), T("2 is **even**", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: for equally likely outcomes, probability is the outcomes you want, divided by the total.", do=[T("• P = outcomes you want **÷ total**", x=80, y=170)]),
        dict(say="Mutually exclusive outcomes cannot happen together.", do=[T("• **Mutually exclusive**: cannot happen together", x=80, y=250)]),
        dict(say="The probabilities of all the outcomes add up to 1.", do=[T("• All the outcomes add up to **1**", x=80, y=330)]),
        dict(say="The probability of not A is 1 minus the probability of A.", do=[T("• **P(not A) = 1 − P(A)**", x=80, y=410)]),
    ]),
]

VIDEOS["13.3"] = [
    dict(kind="hook", title="Is the dice fair?", steps=[
        dict(say="Zane rolls a dice 60 times. He gets a six 18 times.", do=[E("🎲", 90, 150, 110), T("**60** rolls · **18** sixes", x=240, y=190)]),
        PAUSE("13.3-k1", "How many sixes would you expect from a fair dice, in 60 rolls? Pause the video and work it out.", "How many sixes would you expect in 60 rolls of a fair dice?"),
    ]),
    dict(kind="hook", title="Expected: 10", steps=[
        dict(say="On a fair dice, the probability of a six is 1 sixth. 1 sixth of 60 is 10. You would expect about 10 sixes.", do=[MATH(f"{F(1, 6)} × 60 = 10", x=80, y=170), B("expect about 10", x=80, y=310, color=GREEN, at=5)]),
        dict(say="Zane got 18. That is a lot more than 10. Perhaps his dice is not fair.", do=[T("Zane got **18** – is the dice **fair**?", x=80, y=430, color=RED)]),
    ]),
    dict(kind="recall", title="A fraction of an amount", steps=[
        dict(say="Remember: to find a fraction of an amount, divide by the denominator. 1 fifth of 150 is 150 divided by 5, which is 30.", do=[MATH(f"{F(1, 5)} of 150 = 150 ÷ 5 = 30", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Experimental probability", steps=[
        dict(say="Sometimes we cannot work out a probability by counting equally likely outcomes. Then we do an experiment. Each go is called a trial.", do=[T("an **experiment** · each go is a **trial**", x=80, y=150)]),
        dict(say="The experimental probability is the number of times the event happens, divided by the number of trials.", do=[MATH("$$\\text{experimental probability} = \\dfrac{\\text{times it happens}}{\\text{number of trials}}$$", x=80, y=240, color=BLUE)]),
        dict(say="For Zane's dice: 18 sixes in 60 rolls. 18 divided by 60 is 0.3.", do=[MATH(f"{F(18, 60)} = 0.3", x=80, y=420)]),
        PAUSE("13.3-k2", "Your turn. A spinner lands on green 12 times in 40 spins. What is the experimental probability of green, as a decimal? Pause the video and try it.", "Green came up 12 times in 40 spins. Experimental P(green) as a decimal?"),
    ]),
    dict(kind="idea", title="Check: 12 greens in 40 spins", steps=[
        dict(say="12 divided by 40 is 0.3. The experimental probability of green is 0.3.", do=[MATH(f"{F(12, 40)} = 0.3", x=80, y=180, color=GREEN)]),
    ]),
    dict(kind="idea", title="Expected results", steps=[
        dict(say="The expected number is the probability, multiplied by the number of trials.", do=[B("expected = probability × trials", x=80, y=160, color=BLUE)]),
        dict(say="Results vary by chance. From a fair dice, 8 sixes or 12 sixes in 60 rolls would not be a surprise.", do=[T("8 or 12 sixes: **no surprise**", x=80, y=290)]),
        dict(say="But 18 is far from 10. Over many trials, a result far from the expected number suggests the dice is biased. Biased means not fair.", do=[T("18 sixes: probably **biased** (not fair)", x=80, y=380, color=RED)]),
        PAUSE("13.3-k3", "Your turn. The probability of red is 0.2. How many reds would you expect in 150 trials? Pause the video and try it.", "P(red) = 0.2. Expected reds in 150 trials?"),
    ]),
    dict(kind="idea", title="Check: expected reds", steps=[
        dict(say="0.2 times 150 is 30. You would expect about 30 reds.", do=[MATH("0.2 × 150 = 30", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="More trials are better", steps=[
        dict(say="With only a few trials, chance has a big effect. Toss a coin 4 times, and you might easily get 3 heads.", do=[E("🪙", 90, 150, 90), T("4 tosses: 3 heads is quite likely", x=220, y=180)]),
        dict(say="With many trials, the experimental probability settles close to the true probability. So more trials give a more reliable estimate.", do=[B("more trials → more reliable", x=80, y=330, color=GREEN)]),
    ]),
    dict(kind="method", title="How do I estimate a probability?", steps=[
        dict(say="Here is the method. Step 1: do many trials, and record the results in a table.", do=[T("1. Do **many trials** · record them", x=80, y=170)]),
        dict(say="Step 2: divide the number of times the event happens by the number of trials.", do=[T("2. **Times it happens ÷ trials**", x=80, y=260)]),
        dict(say="Step 3: to predict, multiply the probability by the number of trials.", do=[T("3. Predict: **probability × trials**", x=80, y=350)]),
        dict(say="Step 4: compare the results with what you expected.", do=[T("4. **Compare** with what you expected", x=80, y=440), E("✅", 1000, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Tossing a coin", steps=[
        dict(say="A coin is tossed 120 times, and it lands on heads 66 times. Find the experimental probability of heads.", do=[E("🪙", 90, 140, 80), T("**120** tosses · **66** heads", x=200, y=160)]),
        dict(say="66 divided by 120 is 0.55. That is the experimental probability.", do=[MATH(f"{F(66, 120)} = 0.55", x=80, y=260)]),
        dict(say="For a fair coin, you would expect 0.5 times 120, which is 60 heads. 66 is a little more than 60. That is not enough to say the coin is biased.", do=[MATH("0.5 × 120 = 60", x=80, y=400), T("66 is close to 60 → probably **fair**", x=80, y=490, color=GREEN, at=6)]),
    ]),
    dict(kind="example", title="Using an estimate", steps=[
        dict(say="A factory tests its phones. 4 in every 250 fail the test. How many would you expect to fail, out of 10,000 phones?", do=[E("📱", 90, 140, 80), T("**4 in 250** fail · out of **10 000**?", x=200, y=160)]),
        dict(say="The experimental probability is 4 divided by 250, which is 0.016.", do=[MATH(f"{F(4, 250)} = 0.016", x=80, y=260)]),
        dict(say="0.016 times 10,000 is 160. You would expect about 160 phones to fail.", do=[MATH("0.016 × 10 000 = 160", x=80, y=400), B("about 160", x=80, y=490, color=GREEN, at=3.6)]),
    ]),
    dict(kind="example", title="Combining results", steps=[
        dict(say="2 groups test a spinner. Group A gets 14 reds in 40 spins. Group B gets 78 reds in 200 spins. Which estimate is better?",
             do=[TBL(["Group", "Reds", "Spins", "Estimate"], [["A", "14", "40", "0.35"], ["B", "78", "200", "0.39"], ["A + B", "92", "240", "0.383…"]], y=160), ROW(0, 3), ROW(1, 6)]),
        dict(say="Group A's estimate is 0.35. Group B's is 0.39. Group B did more trials, so its estimate is more reliable.", do=[T("B: **more trials** → more reliable", x=640, y=230, color=BLUE)]),
        dict(say="Better still, combine them. 92 reds in 240 spins gives about 0.38.", do=[ROW(2, 0.3), B("92 ÷ 240 ≈ 0.38", x=640, y=340, color=GREEN, at=3)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A coin is tossed 20 times, and it lands on heads 13 times. Here is Remi's working. Which line goes wrong first?",
             do=LINES("Remi", "20 tosses, 13 heads", ["Expected heads = 0.5 × 20 = 10", "13 ≠ 10, so the coin must be biased"])),
        dict(say="Line 2 is wrong. Results vary by chance, especially with only a few trials. 13 heads in 20 tosses is quite normal for a fair coin.", do=[dict(a="cross", id="l2")]),
        dict(say="To decide if a coin is biased, you need many more trials.", do=[B("do many more trials", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Predicting from data", steps=[
        dict(say="About 1 person in 10 is left-handed. That probability comes from counting people, not from equally likely outcomes.", do=[E("✍️", 90, 160, 100), T("left-handed: about **1 in 10**", x=230, y=190)]),
        dict(say="So in a school of 900 students, you would expect about 90 to be left-handed.", do=[MATH("0.1 × 900 = 90", x=230, y=300)]),
        dict(say="Weather forecasts work in the same way. Forecasters look at thousands of past days with similar conditions, and count how often it rained.", do=[E("🌦️", 90, 420, 100), T("forecasts: count **past days** like today", x=230, y=450)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("13.3-k4", "One last question. Which estimate is more reliable: one from 500 trials, or one from 20 trials? Pause the video and decide.", "Which estimate is more reliable: from 500 trials or from 20 trials?"),
        dict(say="The estimate from 500 trials. With more trials, chance has less effect.", do=[B("500 trials", x=80, y=190, color=GREEN), T("more trials → chance matters **less**", x=80, y=300)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: experimental probability is the number of times the event happens, divided by the number of trials.", do=[T("• Experimental probability = **times ÷ trials**", x=80, y=170)]),
        dict(say="The expected number is the probability times the number of trials.", do=[T("• Expected number = **probability × trials**", x=80, y=250)]),
        dict(say="More trials give a more reliable estimate.", do=[T("• More trials → **more reliable**", x=80, y=330)]),
        dict(say="Over many trials, results far from the expected number suggest bias.", do=[T("• Far from expected, over many trials → **bias**", x=80, y=410)]),
    ]),
]
