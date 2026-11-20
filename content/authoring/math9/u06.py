# -*- coding: utf-8 -*-
"""Stage 9 Mathematics · Unit 6 Statistical investigations. Written by the Atomic teaching team."""
from kit import *

U = Unit(6, "Statistical Investigations", "Statistics",
         "Planning an investigation: populations and samples, sampling methods, sample size, data collection, and spotting and reducing bias.",
         {"O1": {"sec": "6.1", "code": "9Ss.01", "codeNote": "", "t": "Select, trial and justify methods to collect data, including sampling a population: random, systematic and proportional (stratified) samples."},
          "O2": {"sec": "6.1", "code": "9Ss.02", "codeNote": "", "t": "Choose a suitable sample size and explain how it affects the reliability of conclusions."},
          "O3": {"sec": "6.2", "code": "9Ss.01", "codeNote": "bias", "t": "Identify sources of bias in sampling and in questions, and suggest how to reduce it."}})

# ================================================================== 6.1
s = U.section("6.1", "Data collection and sampling", ["O1", "O2"])
s.idea("Population and sample", ["The **population** is everyone (or everything) you want to know about. A **sample** is the part you actually ask or measure.",
       "A sample is quicker and cheaper, but it must **represent** the population. Larger samples usually give more **reliable** results."])
s.method("Sampling methods", ["**Random**: every member has the same chance (e.g. numbered names drawn by a computer).",
         "**Systematic**: choose every kᵗʰ member from a list, e.g. every 10ᵗʰ name, starting at a random point.",
         "**Proportional (stratified)**: split the population into groups and sample each group in proportion to its size."])
s.example("Proportional sample", "A school has 360 Stage 7, 300 Stage 8 and 240 Stage 9 students. A sample of 60 is taken in proportion. How many Stage 9 students?", [("total 900", ""), ("240 ÷ 900 × 60 = 16", "")], "16 Stage 9 students")
s.check(N("A list has 800 names. A systematic sample of 40 is taken. Every how many names is one chosen?", 20, o="O1"))
s.idea("Types of data", ["**Primary** data you collect yourself; **secondary** data was collected by someone else. **Discrete** data can be counted (number of pets); **continuous** data is measured (height, time)."])
s.mistake("Sample size", ["A sample of 5 people cannot represent a school of 1000 – the results could change a lot by chance. A common guide is at least 10% for small populations, and never fewer than about 30."])
s.check(MC("Which is the best sample to estimate the average height of 1200 students?", "60 students chosen at random from the whole school", [("the 60 students in the basketball club", "They may be taller than average."), ("5 students chosen at random", "Too small to be reliable."), ("the first 60 students to arrive", "")], o="O2", d="H"))
def g1(r):
    grp = r.sample(["Stage 7", "Stage 8", "Stage 9"], 3); sizes = [r.randint(5, 20) * 20 for _ in range(3)]; tot = sum(sizes)
    n = pick(r, [40, 50, 60, 80, 100]); k = r.randrange(3); ans = round(sizes[k] / tot * n)
    return N(f"A school has {sizes[0]} {grp[0]}, {sizes[1]} {grp[1]} and {sizes[2]} {grp[2]} students. A proportional sample of {n} is taken. How many {grp[k]} students should be in it?", ans, "students", units=["students"], o="O1", d="H", tol=0.5,
             data={"head": ["Group", grp[0], grp[1], grp[2]], "rows": [["Students", str(sizes[0]), str(sizes[1]), str(sizes[2])]]}, reason=f"{sizes[k]} ÷ {tot} × {n} = {sizes[k]/tot*n:.2f} ≈ {ans}.")
def g2(r):
    N_, n = pick(r, [(600, 30), (900, 45), (1200, 60), (500, 25), (2000, 50), (750, 30)])
    return N(f"A systematic sample of {n} is taken from a list of {N_}. How often is a name chosen (every …th)?", N_ // n, o="O1")
def g3(r):
    rows = [("Number of siblings", "Discrete"), ("Time to run 100 m", "Continuous"), ("Mass of a bag", "Continuous"), ("Number of goals", "Discrete"), ("Shoe size", "Discrete"), ("Temperature", "Continuous")]
    return GD("Is each type of data discrete or continuous?", "Type of data", r.sample(rows, 4), o="O1")
def g4(r):
    rows = [("Pick names from a hat", "Random"), ("Every 15th person on the register", "Systematic"), ("Sample each year group in proportion to its size", "Proportional"), ("A computer generates random numbers", "Random")]
    return GD("Name each sampling method.", "Method", r.sample(rows, 3), o="O1")
def g5(r):
    pop = r.randint(4, 30) * 100; pc = pick(r, [5, 10, 20])
    return N(f"A town has {fmt(pop)} households. A researcher wants a {pc}% sample. How many households is that?", pop * pc // 100, "households", units=["households"], o="O2")
def g6(r):
    rows = [("Asking your friends about school lunches", "Primary"), ("Using census results from a government website", "Secondary"), ("Measuring plant heights in an experiment", "Primary"), ("Reading rainfall figures in a newspaper", "Secondary")]
    return GD("Primary or secondary data?", "Type", r.sample(rows, 4), o="O1")
def g7(r):
    a, b = r.randint(10, 40), r.randint(60, 200)
    return MC(f"Survey A asks {a} people and survey B asks {b} people chosen in the same way. Which is likely to be more reliable?", "survey B, because it is larger", [("survey A, because it is quicker", ""), ("they are equally reliable", ""), ("survey A, because it is smaller", "")], o="O2")
def g8(r):
    return OD("Put the stages of a statistical investigation in order.", ["Decide the question and a hypothesis", "Plan how to collect data and choose a sample", "Collect the data", "Process and represent the data", "Interpret the results and write a conclusion"], o="O1", skill="Data")
def g9(r):
    m, f = r.randint(20, 80) * 10, r.randint(20, 80) * 10; n = pick(r, [50, 40, 30])
    return TB(f"A club has {m} male and {f} female members. Complete the proportional sample of {n}.", ["Male", "Female"], [[B(round(m / (m + f) * n), 0.5), B(round(f / (m + f) * n), 0.5)]], o="O1", d="H")
s.core(g1(s.rng), g2(s.rng), g3(s.rng), g4(s.rng), g9(s.rng), g8(s.rng), g7(s.rng),
       EX("Suggest two advantages of using a sample rather than the whole population.", [("quicker / less time", ["quick|time|faster"]), ("cheaper / less cost / easier", ["cheap|cost|money|easier|less work"])], "Taking a sample is quicker than asking everyone, and it is cheaper and easier to organise.", o="O2"))
s.gen("p", 44, g1, g2, g3, g4, g5, g6, g7, g9)
s.gen("a", 8, g1, g9, lambda r: EX("A biologist counts 40 fish, tags them, and later catches 50 fish of which 8 are tagged. Estimate the number of fish in the lake and explain.", [("8/50 of the fish are tagged", ["8 ?/ ?50|8 out of 50|16%"]), ("40 ÷ (8/50) = 250", ["250"])], "In the sample 8 out of 50 fish are tagged, so about 8/50 of the lake is tagged. 40 ÷ (8/50) = 250 fish.", o="O2", d="VH"))

# ================================================================== 6.2
s = U.section("6.2", "Bias", ["O3"])
s.idea("What is bias?", ["A sample or question is **biased** if it makes some answers more likely than they should be, so the results do not represent the population.",
       "Common causes: asking only one type of person (e.g. only people at a gym about exercise), **leading questions** ('Don't you agree that…?'), too small a sample, and people choosing whether to reply."])
s.example("Spot the bias", "A council asks people in a car park whether a new car park is needed.", [("people in a car park drive", ""), ("they are more likely to say yes", ""), ("so the sample is biased", "")], "Biased – ask a random sample of all residents instead.")
s.check(MC("Which question is NOT leading?", "How many hours of sport do you do each week?", [("Don't you agree that sport is good for you?", "It pushes people to agree."), ("Most people love football – do you?", ""), ("Sport is boring, isn't it?", "")], o="O3"))
s.idea("Good questions", ["Use **response boxes** that do not overlap and cover every possible answer, e.g. 0–1, 2–3, 4–5, 6 or more (hours).", "Keep questions short, clear and about one thing only."])
s.mistake("Overlapping boxes", ["Boxes 0–2, 2–4, 4–6 overlap: someone who answers 2 could tick two boxes."])
s.check(MC("Which set of response boxes for 'hours of TV per day' is best?", "0 to less than 1, 1 to less than 2, 2 to less than 3, 3 or more", [("0–1, 1–2, 2–3", "The boxes overlap and do not cover 3+."), ("1–2, 3–4, 5–6", "There are gaps (e.g. 2.5) and no 0."), ("a little, some, a lot", "Too vague.")], o="O3", d="H"))
def b1(r):
    rows = [("Asking people at a gym how often they exercise", "Biased"), ("Choosing 50 names at random from the whole town", "Not biased"), ("Asking only your friends what music is popular", "Biased"), ("Every 20th student on the full school register", "Not biased"), ("An online poll on a football website about sport", "Biased")]
    return GD("Is each sample likely to be biased?", "Biased?", r.sample(rows, 4), o="O3")
def b2(r):
    sit = pick(r, [("a library", "how many books people read"), ("a sports centre", "how often people exercise"), ("a vegetarian restaurant", "how often people eat meat"), ("a train station at 8 a.m.", "how people travel to work")])
    return EX(f"Explain why asking people at {sit[0]} about {sit[1]} could give biased results, and suggest a better method.", [("the people there are not typical / more likely to …", ["not typical|more likely|less likely|not represent|only|already|same type"]), ("choose a random sample of the whole population", ["random|whole|everyone|different places|range"])],
              f"People at {sit[0]} are more likely than others to give a particular answer, so they do not represent everyone. A random sample of the whole population would be better.", o="O3", d="H")
def b3(r):
    return MC(pick(r, ["Which change would most reduce bias in a survey of a school's opinion on uniform?", "How can a student make her survey about the school canteen fairer?"]), "choose students at random from every year group", [("ask only the school council", ""), ("ask students in her own class", ""), ("ask twice as many of her friends", "")], o="O3")
def b4(r):
    q = pick(r, ["Don't you think homework is a waste of time?", "Surely everyone should recycle, shouldn't they?", "Do you agree that our excellent team deserves more money?", "How bad is the traffic in our town?"])
    return MC(f"Why is this a poor question? '{q}'", "it is a leading question", [("it is too short", ""), ("it uses numbers", ""), ("it has response boxes", "")], o="O3")
def b5(r):
    rows = [("0–1 h, 1–2 h, 2–3 h", "Overlapping"), ("1 to 2 h, 3 to 4 h", "Gaps"), ("0 to < 1 h, 1 to < 2 h, 2 h or more", "Good")]
    return GD("Describe each set of response boxes.", "Problem", rows, o="O3", d="H")
def b6(r):
    n, k = r.randint(200, 900), r.randint(10, 40)
    return N(f"A survey is posted to {n} homes and {k}% are returned. How many replies are there? (Low replies can cause bias.)", round(n * k / 100), "replies", units=["replies"], o="O3", tol=0.5)
def b7(r):
    return TK("Which of these can cause bias?", ["Can cause bias", "Does not"], [("A very small sample", ["✓", "✗"]), ("A leading question", ["✓", "✗"]), ("Choosing people at random", ["✗", "✓"]), ("Only asking people who volunteer", ["✓", "✗"])], o="O3")

CTX = [("whether the school day should start later", "students in the library before school", "students from every year group chosen at random"),
       ("how much people spend on clothes", "shoppers outside an expensive shop", "a random sample of adults from the town"),
       ("the most popular sport", "members of the tennis club", "students picked at random from the register"),
       ("how people get to work", "people at the bus station", "every 20th name on the electoral list"),
       ("opinions about a new road", "people who live next to the road", "a random sample of all residents"),
       ("average screen time of teenagers", "an online gaming forum", "a random sample of students from several schools")]
def b8(r):
    t, bad, good = pick(r, CTX)
    return MC(f"A survey asks about {t}. Which sample is least likely to be biased?", good, [(bad, "These people are not typical of the whole population."), ("the researcher's family", ""), ("the first 10 people who reply online", "")], o="O3")
def b9(r):
    t, bad, good = pick(r, CTX); n = r.randint(20, 60); y = r.randint(5, n - 5)
    return N(f"A survey about {t} asked {n} {bad}; {y} gave the answer 'yes'. What percentage is that, to 1 d.p.? (This sample may be biased.)", round(y / n * 100, 1), "%", units=["%"], tol=0.05, o="O3")
def b10(r):
    a, b = r.randint(20, 80), r.randint(20, 80)
    if abs(a - b) < 15: return None
    return EX(f"Two surveys on the same question give {a}% and {b}% 'yes'. Give two reasons why the results could be so different.", [("different samples / one is biased", ["bias|different (people|sample|groups)|who was asked|place"]), ("sample too small / chance / different questions", ["small|size|chance|wording|question|time"])],
              "The samples may be of different kinds of people, so one could be biased, and one sample may be too small or the questions may have been worded differently.", o="O3", d="H")
s.core(b1(s.rng), b2(s.rng), b3(s.rng), b4(s.rng), b5(s.rng), b7(s.rng), b6(s.rng),
       EX("Rewrite the question 'You eat lots of healthy food, don't you?' so that it is not leading, and give suitable response boxes.", [("neutral question about how often / how many portions", ["how many|how often|portions|times"]), ("non-overlapping boxes covering all answers", ["0|or more|none|1–2|1-2|boxes"])], "How many portions of fruit and vegetables do you eat on a typical day? Boxes: 0, 1–2, 3–4, 5 or more.", o="O3", d="H"))
s.gen("p", 44, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10)
s.gen("a", 8, b2, b10, lambda r: (lambda y, t: N(f"In a survey of {t} people chosen at a youth club, {y} said the town needs a skate park. Explain the bias; then, as a percentage, how many said yes? (1 d.p.)", round(y / t * 100, 1), "%", units=["%"], tol=0.05, o="O3", d="VH"))(r.randint(20, 60), r.randint(61, 90)))

U.mindmap(("Population and sample", "A sample must represent the population", "O1", "6.1"), ("Sampling methods", "Random • systematic • proportional", "O1", "6.1"),
          ("Sample size", "Larger samples are more reliable", "O2", "6.1"), ("Bias", "Unrepresentative samples • leading questions • overlapping boxes", "O3", "6.2"))
