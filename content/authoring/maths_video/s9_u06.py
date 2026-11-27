# -*- coding: utf-8 -*-
"""Stage 9 · Unit 6 lesson videos (Camday's own script). See tools/maths_video/build.py for the format."""
from .s7_u01 import T, B, MATH, E, GREEN, BLUE, RED
from .s7_u02 import PAUSE, LINES
from .s7_u04 import TBL, ROW

VIDEOS = {}

VIDEOS["6.1"] = [
    dict(kind="hook", title="Phones and sleep", steps=[
        dict(say="A school has 1,200 students. The head wants to know: do students who use phones and screens more, sleep less? Asking everyone would take far too long.",
             do=[E("📱", 90, 170, 100), T("**1200 students** · more screen time → less sleep?", x=230, y=200)]),
        PAUSE("6.1-k1", "What is the best first step: write a clear question and predictions, or ask your friends? Pause the video and choose.", "Best first step?"),
    ]),
    dict(kind="hook", title="Start with a question", steps=[
        dict(say="Write a clear question and predictions first. Then you know exactly what data you need.", do=[B("a clear question and predictions", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Primary and secondary", steps=[
        dict(say="Remember: primary data is data you collect yourself. Secondary data was collected by someone else, like data from a government website.", do=[T("**primary**: you collect it · **secondary**: someone else did", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Planning", steps=[
        dict(say="First, write a statistical question, and a prediction you can test. For example: students with more than 3 hours of screen time sleep less than 8 hours.",
             do=[T("1. a **question** and a **prediction** you can test", x=80, y=170), MATH("> 3 h screen time → < 8 h sleep", x=110, y=230)]),
        dict(say="Then decide what data to collect, how, and how much. Collect it, show it, analyse it, and say whether it supports your prediction.", do=[T("2. what data, how, how much · 3. collect, show, analyse, **conclude**", x=80, y=320)]),
        PAUSE("6.1-k2", "Your turn. A prediction you can test: is it called a hypothesis, or a sample? Pause the video and choose.", "A prediction to test is a …"),
    ]),
    dict(kind="idea", title="Check: hypothesis", steps=[
        dict(say="It is a hypothesis.", do=[B("hypothesis", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="idea", title="Choosing a sample", steps=[
        dict(say="The population is everyone you want to know about. A sample is the part you actually ask. Here are four ways to choose a sample.",
             do=[TBL(["Method", "How"], [["random", "everyone has an equal chance"], ["systematic", "a fixed gap down a list"], ["stratified", "each group in proportion to its size"], ["convenience", "whoever is nearby – often biased"]], y=170), ROW(0, 0.5)]),
        dict(say="Stratified sampling takes each group, like each year group, in proportion to its size. Convenience sampling, like asking your friends, is quick but often unfair.", do=[ROW(2, 0.2), ROW(3, 5)]),
        dict(say="A bigger sample is usually more reliable, but takes longer. For 1,200 students, about 60 to 120 is sensible.", do=[T("bigger → more reliable · about **60–120** here", x=80, y=480)]),
    ]),
    dict(kind="method", title="How do I plan an investigation?", steps=[
        dict(say="Here is the method. Step 1: write the question and your predictions.", do=[T("1. **Question** and predictions", x=80, y=170)]),
        dict(say="Step 2: decide what data to collect, from whom, and how.", do=[T("2. What data, from **whom**, how", x=80, y=260)]),
        dict(say="Step 3: choose a fair sampling method and a sensible size.", do=[T("3. A **fair** sample, a sensible size", x=80, y=350)]),
        dict(say="Step 4: plan how to show and analyse the data, then interpret it.", do=[T("4. Show, analyse, **interpret**", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="A stratified sample", steps=[
        dict(say="A school has 400 students in Year 7, 300 in Year 8 and 500 in Year 9. They choose a sample of 60, in proportion. How many from Year 9? 500 out of 1,200, times 60, is 25.",
             do=[MATH("500/1200 × 60 = 25", x=80, y=180), B("25 from Year 9", x=80, y=290, color=GREEN, at=8)]),
        PAUSE("6.1-k3", "Your turn. Choosing every 20th name on a list: is that systematic sampling, or stratified sampling? Pause and choose.", "Every 20th name is …"),
    ]),
    dict(kind="example", title="Check: systematic", steps=[
        dict(say="It is systematic sampling. To choose 50 from 1,200, divide: 1,200 divided by 50 is 24. Pick a random start, then take every 24th name.", do=[B("systematic", x=80, y=190, color=GREEN), MATH("1200 ÷ 50 = 24 → every 24th", x=80, y=300)]),
        dict(say="Good questions are clear. Not: how much do you use screens? But: yesterday, how many hours did you spend on screens? With answer boxes like 0 to 1, 1 to 2, and so on.", do=[T("✗ How much do you use screens?", x=80, y=390, color=RED), T("✓ **Yesterday**, how many **hours**? 0–1, 1–2, 2–3 …", x=80, y=450, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="Ben wants the favourite sport of all 1,200 students. Which line is wrong?", do=LINES("Ben", "favourite sport of 1200 students", ["ask the 10 people in my football team"])),
        dict(say="Line 1 is wrong. The sample is far too small, and it is biased: they all play football.", do=[dict(a="cross", id="l1")]),
        dict(say="Use a larger random or stratified sample, like 100 students from the whole school.", do=[B("a random sample of about 100", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Opinion polls", steps=[
        dict(say="Opinion polls often ask about 1,000 people to estimate what millions of people think. It works because the sample is chosen very carefully.",
             do=[E("🗳️", 90, 170, 100), T("about **1000** people → the views of **millions**", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("6.1-k4", "One last question. A school has 1,200 students. The sample is 10 percent. How many students are in the sample? Pause the video and answer.", "1200 students, sample 10%. Size?"),
        dict(say="10 percent of 1,200 is 120.", do=[B("10% of 1200 = 120", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: question, predictions, data, analysis, conclusion.", do=[T("• Question → data → analysis → conclusion", x=80, y=170)]),
        dict(say="The population is everyone. The sample is who you ask.", do=[T("• Population vs sample", x=80, y=250)]),
        dict(say="Use random, systematic or stratified samples. Avoid convenience.", do=[T("• Random, systematic, stratified", x=80, y=330)]),
        dict(say="Bigger samples are usually more reliable.", do=[T("• Bigger is usually more reliable", x=80, y=410)]),
    ]),
]

VIDEOS["6.2"] = [
    dict(kind="hook", title="9 out of 10", steps=[
        dict(say="A juice company says: 9 out of 10 people prefer our juice! The survey was done outside its own shop. It asked: don't you agree our juice tastes better?",
             do=[E("🧃", 90, 170, 100), T("**'9 out of 10 prefer our juice!'**", x=230, y=190), T("outside its own shop · 'Don't you agree …?'", x=230, y=260)]),
        PAUSE("6.2-k1", "What are the main problems: a biased sample and a leading question, or nothing? Pause the video and choose.", "The main problems are …"),
    ]),
    dict(kind="hook", title="Two problems", steps=[
        dict(say="A biased sample, because they asked its own customers. And a leading question, which pushes people towards one answer.", do=[B("biased sample · leading question", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="recall", title="Samples", steps=[
        dict(say="Remember: a sample should represent the population. A sample that does not is biased.", do=[T("not representative → **biased**", x=80, y=190)]),
    ]),
    dict(kind="idea", title="Sources of bias", steps=[
        dict(say="Bias makes results lean one way. Here are common sources.",
             do=[TBL(["Source", "Example"], [["unrepresentative sample", "only one shop's customers"], ["too small a sample", "asking 10 people"], ["non-response", "only people with strong views reply"], ["time or place", "a traffic count on a holiday"]], y=170), ROW(0, 0.5), ROW(1, 0.5)]),
        dict(say="Non-response: only some people reply, and they may be different. Time and place: a traffic count on a holiday is not typical.", do=[ROW(2, 0.2), ROW(3, 5)]),
        dict(say="The wording matters too. A question that pushes people towards one answer is biased.", do=[T("wording can push people → bias", x=80, y=480)]),
        PAUSE("6.2-k2", "Your turn. 'Don't you agree …?' Is that a leading question, or a neutral question? Pause the video and choose.", "'Don't you agree…?' is a …"),
    ]),
    dict(kind="idea", title="Check: leading", steps=[
        dict(say="It is a leading question. A neutral question gives fair choices: which juice do you prefer, A, B, or no preference?", do=[B("leading question", x=80, y=190, color=GREEN), T("neutral: A, B or **no preference**?", x=80, y=300)]),
        dict(say="To avoid bias: use a random or stratified sample of a sensible size, ask neutral questions, and collect data at typical times and places.", do=[T("fair sample · neutral questions · typical times", x=80, y=390)]),
    ]),
    dict(kind="method", title="How do I check for bias?", steps=[
        dict(say="Here is the method. Step 1: who was asked? Do they represent everyone?", do=[T("1. **Who** was asked?", x=80, y=170)]),
        dict(say="Step 2: how many were asked?", do=[T("2. How **many**?", x=80, y=260)]),
        dict(say="Step 3: how were the questions worded? When and where?", do=[T("3. **Wording**, when, where", x=80, y=350)]),
        dict(say="Step 4: are the results shown fairly?", do=[T("4. Shown **fairly**?", x=80, y=440), E("✅", 1100, 410, 90, at=0.8)]),
    ]),
    dict(kind="example", title="Place and time", steps=[
        dict(say="A survey about public transport is done at a bus station. Bus users are over-represented, so it is biased.", do=[MATH("at a bus station → too many bus users", x=80, y=180)]),
        dict(say="Counting cars at 3 in the morning to plan for traffic is also biased. Count at several typical times.", do=[MATH("3 am → not typical", x=80, y=280)]),
        dict(say="Now look at a bar chart. Its vertical axis starts at 95, not 0. A value of 98 looks three times as tall as 96.", do=[T("axis starts at **95** → 98 looks 3 × as tall as 96", x=80, y=380)]),
        PAUSE("6.2-k3", "Your turn. A vertical axis that does not start at 0: can it be misleading, or is it always fine? Pause and choose.", "A cut-off vertical axis can be …"),
    ]),
    dict(kind="example", title="Check: misleading", steps=[
        dict(say="It can be misleading. The axis should start at 0, or show a clear break.", do=[B("misleading", x=80, y=190, color=GREEN)]),
    ]),
    dict(kind="error", title="Spot the mistake", steps=[
        dict(say="A poll on a gaming website gets 50,000 votes on: should schools ban games? Zara comments. Which line is wrong?", do=LINES("Zara", "50 000 votes on a gaming website", ["a huge sample, so it must be reliable"])),
        dict(say="Line 1 is wrong. Size does not fix bias. The voters are gamers who chose to vote, so they do not represent everyone.", do=[dict(a="cross", id="l1")]),
        dict(say="Large but unrepresentative is still biased.", do=[B("large but biased", x=110, y=380, color=GREEN)]),
    ]),
    dict(kind="life", title="Adverts and news", steps=[
        dict(say="Adverts and news reports sometimes use biased samples or misleading graphs. Always ask how the data was collected.", do=[E("📰", 90, 170, 100), T("always ask: **how** was the data collected?", x=230, y=200)]),
    ]),
    dict(kind="pause", title="Quick check", steps=[
        PAUSE("6.2-k4", "One last question. A questionnaire is posted to 1,000 homes, and only 80 reply. What does that risk: non-response bias, or no bias? Pause the video and choose.", "80 replies from 1000 letters risks …"),
        dict(say="Non-response bias. The people who reply may be different from those who do not.", do=[B("non-response bias", x=80, y=200, color=GREEN)]),
    ]),
    dict(kind="summary", title="What to remember", steps=[
        dict(say="To remember: bias comes from unfair samples, leading questions, timing and non-response.", do=[T("• Sample, wording, timing, non-response", x=80, y=170)]),
        dict(say="Use fair samples and neutral questions.", do=[T("• Fair samples, neutral questions", x=80, y=250)]),
        dict(say="Check graphs and claims for missing information.", do=[T("• Check graphs and claims", x=80, y=330)]),
        dict(say="A big sample can still be biased.", do=[T("• Big is not the same as unbiased", x=80, y=410)]),
    ]),
]
