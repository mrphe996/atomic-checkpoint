# -*- coding: utf-8 -*-
"""Stage 8 · Unit 6 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, TEST, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

BOXES = lambda labels, x=80, y=200, at=0, c="#1F2A37": T("".join(f'<span style="display:inline-flex;align-items:center;margin-right:26px"><span style="display:inline-block;width:26px;height:26px;border:3px solid {c};border-radius:4px;margin-right:8px"></span>{l}</span>' for l in labels), x=x, y=y, at=at)
DOTS = lambda n, k, x=80, y=200, at=0, per=40: T("".join(f'<span style="display:inline-block;width:20px;height:20px;border-radius:50%;margin:3px;background:{"#1F9D61" if i % k == 0 else "#CBD5E1"}"></span>' + ("<br>" if (i + 1) % per == 0 else "") for i in range(n)), x=x, y=y, at=at)

VIDEOS = {}

VIDEOS["6.1"] = [
    dict(kind="hook", title="Healthy lunches?", steps=[
        dict(say="The student council wants to know two things. Do students eat enough fruit and vegetables at lunch? And is it different in different year groups?",
             do=[E("🥦", 90, 170, 100), T("enough **fruit and veg** at lunch?", x=230, y=200), T("different for each **year group**?", x=230, y=280)]),
        PAUSE("6.1-k1", "Which data would help to answer the question? Pause the video and choose.", "Which data would help answer the canteen question?"),
    ]),
    dict(kind="hook", title="The right data", steps=[
        dict(say="We need two things for each student: how many portions they eat, and their year group. The canteen menu alone would not tell us what students actually eat.",
             do=[B("portions eaten + year group", x=80, y=200, color=GREEN), T("the menu alone ✗", x=80, y=300, color=RED)]),
    ]),
    dict(kind="recall", title="Types of data", steps=[
        dict(say="Remember the types of data. Categorical data is words, like a favourite fruit. Discrete data is counted, like the number of portions. Continuous data is measured, like a mass.",
             do=[TBL(["Type", "Example"], [["categorical (words)", "favourite fruit"], ["discrete (counted)", "number of portions"], ["continuous (measured)", "mass of food waste"]], y=170), ROW(0, 2), ROW(1, 4.5), ROW(2, 7)]),
    ]),
    dict(kind="idea", title="Linked questions", steps=[
        dict(say="A big question usually splits into smaller linked questions. Each one needs its own data.",
             do=[TBL(["Linked question", "Data", "Method"], [["How many portions does each student eat?", "a count (discrete)", "observe or ask"], ["Which year is each student in?", "categorical", "ask"], ["How much food is wasted?", "mass (continuous)", "weigh plates"]], y=170), ROW(0, 0.5), ROW(1, 2.4), ROW(2, 4)]),
        dict(say="Data you collect yourself is primary data. Data that someone else has already collected, like a website or a report, is secondary data.",
             do=[T("**primary**: you collect it · **secondary**: collected by someone else", x=80, y=460)]),
        PAUSE("6.1-k2", "Your turn. Data that you collect yourself is called what? Pause the video and choose.", "Data you collect yourself is …"),
    ]),
    dict(kind="idea", title="Check: primary data", steps=[
        dict(say="Data you collect yourself is primary data. Rainfall over 30 years, from a weather service, is secondary data.", do=[B("primary", x=80, y=190, color=GREEN), T("rainfall records from a weather service → **secondary**", x=80, y=290)]),
    ]),
    dict(kind="idea", title="Good questions", steps=[
        dict(say="A good question is clear, and it is not personal. It must not be leading. A leading question pushes people towards an answer, like: don't you agree that vegetables are boring?",
             do=[T("clear · not personal · **not leading**", x=80, y=170), T("“Don't you agree vegetables are boring?” ✗", x=80, y=250, color=RED, at=6)]),
        dict(say="Response boxes must cover every possible answer, without overlapping.",
             do=[TBL(["Poor", "Better"], [["Do you eat a lot of fruit?", "How many portions of fruit did you eat yesterday?"], ["□ 0–2  □ 2–4  □ 4–6", "□ 0  □ 1–2  □ 3–4  □ 5 or more"]], y=330), ROW(0, 0.4), ROW(1, 2.5)]),
    ]),
    dict(kind="method", title="How do I plan data collection?", steps=[
        dict(say="Here is the method. Step 1: split the main question into linked questions.", do=[T("1. Split into **linked questions**", x=80, y=170)]),
        dict(say="Step 2: for each one, decide the data, its type, and whether it is primary or secondary.", do=[T("2. Data, **type**, primary or secondary", x=80, y=260)]),
        dict(say="Step 3: choose a method: a questionnaire, an observation, an experiment or a search of records.", do=[T("3. Method: questionnaire, observation, experiment, records", x=80, y=350)]),
        dict(say="Step 4: test your questionnaire on a few people first. This is called a pilot.", do=[T("4. Test it first: a **pilot**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Fixing a leading question", steps=[
        dict(say="Improve this question: most people think our library is too small. Do you agree?", do=[T("“Most people think our library is too small. Do you agree?”", x=80, y=170, color=RED)]),
        dict(say="It is leading, because it tells you what other people think. A better question is neutral, with boxes for every view.",
             do=[T("How would you rate the size of the library?", x=80, y=270, color=GREEN), BOXES(["too small", "about right", "too big"], y=340, at=3)]),
    ]),
    dict(kind="example", title="A vague question", steps=[
        dict(say="Here is another question: do you eat a lot of fruit?", do=[T("“Do you eat a lot of fruit?”", x=80, y=170)]),
        PAUSE("6.1-k3", "Your turn. What is the problem with this question? Pause and choose.", "Which is a problem with 'Do you eat a lot of fruit?'"),
    ]),
    dict(kind="example", title="Check: a lot", steps=[
        dict(say="A lot is vague. It means different things to different people. Ask for a number, over a fixed time: how many portions of fruit did you eat yesterday?",
             do=[B("'a lot' is vague", x=80, y=190, color=GREEN), T("Better: “How many portions of fruit did you eat **yesterday**?”", x=80, y=290)]),
    ]),
    dict(kind="example", title="Groups for continuous data", steps=[
        dict(say="Plates have between 0 and about 300 grams of food waste. Choose groups for the mass, m.", do=[MATH("0 g to about 300 g", x=80, y=170)]),
        dict(say="Use equal widths with no gaps and no overlaps: 0 is less than or equal to m, which is less than 50. Then 50 to 100, and so on, up to 300. That makes 6 groups.",
             do=[MATH("0 ≤ m < 50,  50 ≤ m < 100,  …,  250 ≤ m < 300", x=80, y=270, color=GREEN), T("**6 groups**, equal widths, no gaps", x=80, y=370, at=7)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Leo writes response boxes for the question: how old are you? Which line goes wrong first?", do=LINES("Leo", "“How old are you?”", ["□ 10–12  □ 12–14  □ 14–16", "These cover all students"])),
        dict(say="Line 1 is wrong. A 12 year old could tick two boxes, and a 17 year old has no box to tick.", do=[dict(a="cross", id="l1"), dict(a="strike", id="l2", at=0.6)]),
        dict(say="Better boxes do not overlap, and cover everyone.", do=[BOXES(["10–11", "12–13", "14–15", "16 or over"], x=110, y=420)]),
    ]),
    dict(kind="life", title="The national census", steps=[
        dict(say="Many countries run a census about every 10 years. Every household answers the same questions, about who lives there and how they live.",
             do=[E("🏛️", 90, 170, 100), T("a **census** about every 10 years", x=230, y=200)]),
        dict(say="Before the real census, officials test the questions on a small group first, to find confusing questions. That is a pilot, just like the one in step 4.",
             do=[T("questions are tested first in a **pilot**", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("6.1-k4", "One last question. Testing a questionnaire on a few people first is called what? Pause the video and choose.", "Testing a questionnaire first is a …"),
        dict(say="It is called a pilot. It helps you fix unclear questions and missing boxes before the real survey.", do=[B("a pilot", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: break a big question into linked questions.", do=[T("• Break a big question into **linked questions**", x=80, y=170)]),
        dict(say="Decide the type of data, and whether it is primary or secondary.", do=[T("• Data type; primary or secondary", x=80, y=250)]),
        dict(say="Questions must be clear, and not leading.", do=[T("• Clear questions, **not leading**", x=80, y=330)]),
        dict(say="Response boxes must cover every answer, with no overlaps. And pilot your questionnaire first.", do=[T("• Boxes: complete, no overlaps; **pilot** first", x=80, y=410)]),
    ]),
]

VIDEOS["6.2"] = [
    dict(kind="hook", title="Ask the whole school?", steps=[
        dict(say="A school has 1,200 students. The council has one week to find out what students think of the canteen.", do=[E("🏫", 90, 170, 100), T("**1200** students · **one week**", x=230, y=200)]),
        dict(say="Should they ask every student?", do=[T("ask **everyone**?", x=230, y=300)]),
        PAUSE("6.2-k1", "Is asking all 1,200 students in one week a good plan? Pause the video and choose.", "Asking all 1200 in one week is …"),
    ]),
    dict(kind="hook", title="Take a sample", steps=[
        dict(say="It is possible, but very slow. It is more practical to ask a smaller group, called a sample. The question is how to choose it fairly.",
             do=[B("a sample is more practical", x=80, y=200, color=GREEN), DOTS(120, 10, x=80, y=300, at=3)]),
    ]),
    dict(kind="recall", title="Population and sample", steps=[
        dict(say="Remember: the population is everyone you are interested in. Here it is all 1,200 students. The sample is the group you actually ask.",
             do=[T("**population**: everyone you are interested in (all 1200 students)", x=80, y=170), T("**sample**: the group you actually ask", x=80, y=260, at=6)]),
    ]),
    dict(kind="idea", title="Ways to sample", steps=[
        dict(say="In a simple random sample, every member has an equal chance of being chosen, for example using random numbers.",
             do=[TBL(["Method", "How", "Good", "Problem"], [["simple random", "equal chance (random numbers)", "fair", "needs a full list"], ["systematic", "every kth name on a list", "quick", "a pattern in the list"], ["stratified", "each group in proportion", "represents groups", "more work"], ["convenience", "whoever is easy to ask", "quick", "often biased"]], y=170), ROW(0, 0.4)]),
        dict(say="In a systematic sample, you choose every k-th name on a list, like every 12th name.", do=[ROW(1, 0.3)]),
        dict(say="In a stratified sample, each group, like each year group, is included in proportion to its size.", do=[ROW(2, 0.3)]),
        dict(say="A convenience sample just asks whoever is easy to ask, like your friends. It is quick, but it is often biased.", do=[ROW(3, 0.3)]),
        PAUSE("6.2-k2", "Your turn. Asking your friends is which kind of sampling? Pause the video and choose.", "Asking your friends is …"),
    ]),
    dict(kind="idea", title="Check: asking friends", steps=[
        dict(say="Asking your friends is convenience sampling. Your friends may think alike, so the results may not represent everyone.", do=[B("convenience sampling", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Bias and sample size", steps=[
        dict(say="A sample is biased if some groups are more likely to be included than others. Asking only students in the lunch queue misses everyone who brings a packed lunch.",
             do=[T("**biased**: some groups more likely to be included", x=80, y=170), E("🥪", 80, 240, 70, at=6), T("lunch queue only → packed lunches missed", x=180, y=262, at=6)]),
        dict(say="A larger sample usually gives more reliable results, but it takes more time and costs more.", do=[T("**larger** sample → more reliable, but more time and cost", x=80, y=370)]),
    ]),
    dict(kind="method", title="How do I choose a good sample?", steps=[
        dict(say="Here is the method. Step 1: define the population clearly.", do=[T("1. Define the **population**", x=80, y=170)]),
        dict(say="Step 2: choose a sample size that balances reliability with time and cost.", do=[T("2. Choose a **size**: reliable but practical", x=80, y=260)]),
        dict(say="Step 3: choose a method that gives everyone a fair chance: random, systematic or stratified.", do=[T("3. A fair method: random, systematic, stratified", x=80, y=350)]),
        dict(say="Step 4: check for bias. Ask yourself: who might be left out?", do=[T("4. Check for **bias**: who is left out?", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A stratified sample", steps=[
        dict(say="Years 7, 8 and 9 have 400, 500 and 300 students. Take a stratified sample of 60.", do=[TBL(["Year", "7", "8", "9", "Total"], [["Students", "400", "500", "300", "1200"], ["Sample", "20", "25", "15", "60"]], y=170), ROW(0, 0.4)]),
        dict(say="60 out of 1,200 is 1 in 20. So divide each year by 20. 400 divided by 20 is 20. 500 divided by 20 is 25. 300 divided by 20 is 15.", do=[MATH("60 ÷ 1200 = 1/20", x=80, y=360), ROW(1, 4)]),
        dict(say="Check: 20 plus 25 plus 15 is 60.", do=[T("20 + 25 + 15 = 60 ✓", x=80, y=440, color=GREEN)]),
        PAUSE("6.2-k3", "Your turn. Take a stratified sample of 30 from 200 boys and 100 girls. How many boys? Pause and work it out.", "Stratified sample of 30 from 200 boys and 100 girls: boys?"),
    ]),
    dict(kind="example", title="Check: 200 boys, 100 girls", steps=[
        dict(say="There are 300 students. 30 out of 300 is 1 in 10. 200 divided by 10 is 20 boys, and 100 divided by 10 is 10 girls.",
             do=[MATH("30 ÷ 300 = 1/10", x=80, y=190), B("boys: 200 ÷ 10 = 20", x=80, y=290, color=GREEN, at=4)]),
    ]),
    dict(kind="example", title="A systematic sample", steps=[
        dict(say="Choose a systematic sample of 50 from a list of 1,200 names. 1,200 divided by 50 is 24, so choose every 24th name.", do=[MATH("1200 ÷ 50 = 24", x=80, y=170)]),
        dict(say="Pick a random starting point between 1 and 24, say 7. Then take names 7, 31, 55, and so on.", do=[T("start at **7**: 7, 31, 55, 79 …", x=80, y=270, color=GREEN)]),
    ]),
    dict(kind="example", title="Spotting bias", steps=[
        dict(say="To find out how much exercise adults do, a student asks people leaving a gym. What is wrong?", do=[E("🏋️", 90, 160, 90), T("asking people **leaving a gym**", x=230, y=190)]),
        dict(say="Gym users exercise more than most people, and people who never exercise are missed. The sample is biased, and the results will be too high.", do=[B("biased: results too high", x=230, y=300, color=RED)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Amir wants to find the favourite sport of students in his school. Here is his plan. Which line is wrong?", do=LINES("Amir", "the favourite sport in the school", ["Ask the 30 students in the football club", "This is a fair sample"])),
        dict(say="Line 2 is wrong. Football club members are much more likely to choose football. The sample is biased.", do=[dict(a="cross", id="l2")]),
        dict(say="A fairer plan is a random or stratified sample from the whole school register.", do=[B("random or stratified, from the whole register", x=110, y=420, color=GREEN)]),
    ]),
    dict(kind="life", title="Opinion polls", steps=[
        dict(say="Before an election, polling companies ask about 1,000 to 2,000 people, not millions. They choose them carefully, so that ages, regions and other groups are in proportion.",
             do=[E("🗳️", 90, 170, 100), T("about **1000–2000** people, in proportion", x=230, y=200)]),
        dict(say="A well-chosen sample can be surprisingly accurate. A badly chosen one, even a huge one, can be very wrong.", do=[T("**how** you choose matters more than how many", x=230, y=310, color=BLUE)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("6.2-k4", "One last question. Is a sample of 8 students likely to be reliable? Pause the video and choose.", "Quick check: a sample of 8 is …"),
        dict(say="A sample of 8 is too small. It is likely to be unreliable, because a few unusual answers change the results a lot.", do=[B("likely to be unreliable", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: samples can be random, systematic, stratified or convenience.", do=[T("• Random, systematic, stratified, convenience", x=80, y=170)]),
        dict(say="In a stratified sample, each group is in proportion.", do=[T("• Stratified: each group **in proportion**", x=80, y=250)]),
        dict(say="A biased sample leaves groups out.", do=[T("• Biased samples leave groups out", x=80, y=330)]),
        dict(say="Bigger samples are more reliable, but they cost more time.", do=[T("• Bigger = more reliable, but more time and cost", x=80, y=410)]),
    ]),
]
