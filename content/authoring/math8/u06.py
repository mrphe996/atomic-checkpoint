# -*- coding: utf-8 -*-
"""Stage 8 Mathematics · Unit 6 Collecting data (6.1 Data collection, 6.2 Sampling). Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(6, "Collecting Data", "Statistics and probability",
         "Planning a statistical investigation: types of data, questionnaires, data-collection sheets, populations and samples.",
         {"O1": {"code": "8Ss.01", "sec": "6.1", "codeNote": "", "t": "Plan an investigation: choose the data to collect, classify data, and design questionnaires and data-collection sheets."},
          "O2": {"code": "8Ss.02", "sec": "6.2", "codeNote": "", "t": "Understand populations and samples, choose a sample size and recognise how sampling can introduce bias."}})

# ================================================================== 6.1
s = U.section("6.1", "Data collection", ["O1"])
s.idea("Types of data", ["**Categorical** data are words or groups (favourite fruit, eye colour). **Discrete** data are counted (number of pets). **Continuous** data are measured (height, time, mass).",
       "**Primary** data you collect yourself; **secondary** data was collected by someone else (a website, a report)."])
s.method("Good questionnaire questions", ["Ask one thing at a time, in clear, neutral words.", "Give a time frame ('in the last week').", "Use response boxes that do not overlap and cover every possible answer."])
s.example("Fixing response boxes", "What is wrong with these boxes for 'How many hours of TV did you watch yesterday?': 0–1, 1–2, 2–3?", [("1 and 2 are in two boxes", "overlapping"), ("there is no box for more than 3 hours", "not every answer is covered")], "Use 0 to less than 1, 1 to less than 2, 2 to less than 3, 3 or more.")
s.check(MC("Which type of data is 'time taken to run 100 m'?", "continuous", [("discrete", "Time is measured, not counted."), ("categorical", ""), ("secondary", "")], o="O1"))
s.idea("Primary or secondary data?", ["Primary data you collect yourself (a survey, an experiment): you control how it is collected. Secondary data comes from someone else (a website, a report): it is quick to get but you must check its source and date.",
       "Choose the method that answers your question reliably."])
s.mistake("Leading questions", ["'Don't you agree that homework is boring?' pushes people towards one answer. Ask 'What do you think about homework?' instead."])


def d1(r):
    rows = [("Number of brothers", "Discrete"), ("Mass of an apple", "Continuous"), ("Favourite sport", "Categorical"), ("Shoe size", "Discrete"), ("Temperature at noon", "Continuous"),
            ("Colour of a car", "Categorical"), ("Number of goals scored", "Discrete"), ("Time to walk to school", "Continuous"), ("Type of pet", "Categorical")]
    return GD("What type of data is each?", "Type of data", r.sample(rows, 5), o="O1", extra=["Discrete", "Continuous", "Categorical"])
def d2(r):
    rows = [("Your own traffic count", "Primary"), ("Weather records from a website", "Secondary"), ("A questionnaire you hand out", "Primary"), ("Census results", "Secondary"), ("Measuring classmates' heights", "Primary"), ("A table in a newspaper", "Secondary")]
    return GD("Is each source primary or secondary data?", "Source", r.sample(rows, 4), o="O1")
def d3(r):
    q, why = pick(r, [("Don't you think school starts too early?", "it is a leading question"), ("Do you eat a lot of fruit?", "'a lot' is vague"), ("How old are you and where do you live?", "it asks two things at once"),
                      ("How much do your parents earn?", "it is too personal")])
    return MC(f"Why is this a poor survey question? “{q}”", why, [x for x in ["it is a leading question", "'a lot' is vague", "it asks two things at once", "it is too personal"] if x != why], o="O1")
def d4(r):
    a = r.randint(1, 3)
    return MC("Which set of response boxes is best for 'How many books did you read last month?'", f"0, 1–{a + 1}, {a + 2}–{a + 4}, more than {a + 4}", [(f"0–{a + 1}, {a + 1}–{a + 4}, {a + 4}+", "The boxes overlap."), (f"1–{a + 1}, {a + 2}–{a + 4}", "There is no box for 0 or for more than " + str(a + 4) + "."), ("a few, some, lots", "These words are vague.")], o="O1")
def d5(r):
    t = [r.randint(2, 12) for _ in range(4)]; lab = ["Bus", "Car", "Walk", "Bike"]
    k = r.randrange(4)
    return N(f"A data-collection sheet shows how students travel to school. How many students {'walk' if k == 2 else 'come by ' + lab[k].lower()}?", t[k], "students", units=["students"], o="O1", data={"head": ["Travel", *lab], "rows": [["Tally", *["|||| " * (x // 5) + "|" * (x % 5) for x in t]]]}, reason="Count the tally: each |||| is 5.")
def d6(r):
    t = [r.randint(2, 15) for _ in range(4)]; lab = ["Red", "Blue", "Green", "Yellow"]
    return N("How many people took part in the survey?", sum(t), "people", units=["people"], o="O1", data={"head": ["Colour", *lab], "rows": [["Frequency", *map(str, t)]]}, reason=f"Add the frequencies: {sum(t)}.")
def d7(r):
    topic, ans = pick(r, [("Do taller students have longer arm spans?", "height and arm span of each student"), ("Is it warmer in the city than the countryside?", "temperatures in both places at the same times"),
                          ("Do students who sleep more get higher test scores?", "hours of sleep and test score for each student")])
    return MC(f"An investigation asks: “{topic}” Which data should be collected?", ans, ["the favourite colour of each student", "only one measurement", "the names of the students"], o="O1", d="H")
def d8(r):
    rows = [("0 ≤ t < 10", "OK"), ("10 ≤ t < 20", "OK"), ("20 ≤ t ≤ 30", "Overlaps the next group"), ("30 ≤ t < 40", "OK")]
    return MC("A student uses these groups for times in minutes: 0 ≤ t < 10, 10 ≤ t < 20, 20 ≤ t ≤ 30, 30 ≤ t < 40. What is wrong?", "30 is in two groups", [("10 is in two groups", "10 is only in 10 ≤ t < 20."), ("there is a gap between 20 and 30", ""), ("nothing is wrong", "")], o="O1", d="H")
def d9(r):
    a, b = r.randint(10, 40), r.randint(10, 40)
    return N(f"A survey of {a + b} people found {a} like football. What percentage is that? Give your answer to 1 d.p.", round(a / (a + b) * 100, 1), "%", units=["%"], o="O1", tol=0.05, reason=f"{a} ÷ {a + b} × 100 ≈ {round(a / (a + b) * 100, 1)}%.")
def d10(r):
    return MC("Which question is best for finding out how much exercise people do?", "In the last 7 days, on how many days did you exercise for 30 minutes or more?", ["Do you exercise a lot?", "Don't you agree exercise is important?", "How fit are you?"], o="O1", d="H")
def d11(r):
    rows = [("Length of a leaf", "Measure"), ("Number of cars passing", "Count"), ("Favourite subject", "Ask"), ("Mass of a bag", "Measure"), ("Number of red sweets", "Count"), ("Opinion about lunch", "Ask")]
    return GD("How would you collect each type of data?", "Method", r.sample(rows, 4), o="O1")


def d12(r):
    t = [r.randint(3, 14) for _ in range(3)]; lab = r.sample(["Apple", "Banana", "Mango", "Orange", "Grape"], 3)
    k = max(range(3), key=lambda i: t[i])
    if t.count(t[k]) > 1: t[k] += 1
    return MC("Which fruit was the most popular?", lab[k], [x for x in lab if x != lab[k]] + ["they are equal"], o="O1", data={"head": ["Fruit", *lab], "rows": [["Tally", *["|||| " * (x // 5) + "|" * (x % 5) for x in t]]]}, reason="Count each tally.")
def d13(r):
    a, b = r.randint(5, 25), r.randint(5, 25)
    return N(f"In a survey, {a} people chose cats and {b} chose dogs. How many more chose {'cats' if a > b else 'dogs'} than {'dogs' if a > b else 'cats'}?", abs(a - b), "people", units=["people"], o="O1", reason=f"{max(a, b)} − {min(a, b)} = {abs(a - b)}.") if a != b else None
def d14(r):
    lo, w = pick(r, [(0, 5), (0, 10), (10, 10), (100, 20)]); n = 4
    groups = [f"{lo + i * w} ≤ t < {lo + (i + 1) * w}" for i in range(n)]; v = lo + r.randint(0, n * w - 1)
    k = (v - lo) // w
    return MC(f"These groups are used to record times: {', '.join(groups)}. Which group does {v} go in?", groups[k], [g for g in groups if g != groups[k]][:3], o="O1", reason=f"{lo + k * w} ≤ {v} < {lo + (k + 1) * w}.")
def d15(r):
    n = r.randint(20, 60); pc = pick(r, [10, 20, 25, 50])
    return N(f"{n} students were asked how they travel to school. {pc}% walk. How many students walk?", n * pc / 100, "students", units=["students"], o="O1", reason=f"{pc}% of {n} = {fmt(n * pc / 100)}.") if (n * pc) % 100 == 0 else None
def d16(r):
    vals = [r.randint(120, 180) for _ in range(6)]
    return N(f"Heights (cm) collected in a survey: {', '.join(map(str, vals))}. What is the range of the heights?", max(vals) - min(vals), "cm", units=["cm"], o="O1", reason=f"{max(vals)} − {min(vals)} = {max(vals) - min(vals)}.")


def b61(r):
    rows = r.sample([("measuring the heights of students in your class", "Primary"), ("population figures from a government website", "Secondary"), ("a survey you hand out at school", "Primary"), ("weather records from a newspaper", "Secondary")], 4)
    return GD("Is each source primary or secondary data?", "Type", rows, o="O1", d="H", extra=["Primary", "Secondary"], reason="Primary: you collect it. Secondary: someone else collected it.")


s.std([d1, d5, d2, d3, d4, d6, d9, d7, d8, d10, d11, d12, d13, d14, d15, d16], EX("Explain why the response boxes 0–5, 5–10, 10–15 are badly designed.", [("5 and 10 appear in two boxes / overlap", ["overlap|two boxes|both boxes|5 and 10"]), ("no box for more than 15", ["more than 15|over 15|above 15|not every|missing"])], "The boxes overlap: 5 and 10 are each in two boxes. Also there is no box for answers above 15.", o="O1"),
      deep=[b61])

# ================================================================== 6.2
s = U.section("6.2", "Sampling", ["O2"])
s.idea("Population and sample", ["The **population** is the whole group you want to find out about. A **sample** is the smaller group you actually ask.",
       "A **random sample** gives everyone the same chance of being picked. A bigger sample usually gives more **reliable** results, but takes longer and costs more."])
s.example("A biased sample", "To find out how students get to school, Mia asks 20 students at the bus stop. Why is this biased?", [("everyone at the bus stop is likely to take the bus", ""), ("the sample does not represent all students", "")], "Biased towards bus users")
s.check(N("A school has 800 students. Ali surveys 10% of them. How many students is that?", 80, "students", units=["students"], o="O2"))
s.idea("Why sample size matters", ["A small sample can be unrepresentative just by chance. A bigger random sample gives results that are more likely to be close to the whole population.",
       "But a biased method stays biased however big the sample is."])
s.mistake("Too small", ["Asking 3 people cannot tell you what a whole school thinks."])


def g1(r):
    pop = r.randint(4, 30) * 50; pc = pick(r, [5, 10, 20, 25])
    return N(f"A club has {pop} members. A {pc}% sample is chosen. How many members is that?", pop * pc / 100, "members", units=["members"], o="O2", reason=f"{pc}% of {pop} = {fmt(pop * pc / 100)}.")
def g2(r):
    place, why = pick(r, [("outside a sports centre", "people there probably do more sport"), ("in a library", "people there probably read more"), ("at a vegan café", "people there probably eat less meat"),
                          ("on a school bus", "they all travel by bus")])
    return MC(f"A survey is carried out only {place}. Why might the sample be biased?", why, ["the sample is random", "the questions are too short", "the data is continuous"], o="O2")
def g3(r):
    rows = [("Names picked from a hat", "Random"), ("Asking your friends", "Not random"), ("A computer picks 30 numbers from the register", "Random"), ("The first 20 people to arrive", "Not random"), ("Volunteers who reply to an email", "Not random")]
    return GD("Is each sample random?", "Random?", r.sample(rows, 4), o="O2")
def g4(r):
    n, f = pick(r, [(20, 4), (40, 6), (50, 9), (25, 3), (80, 12)]); N_ = r.randint(4, 12) * 100
    return N(f"In a random sample of {n} students, {f} wear glasses. Estimate how many of the {N_} students in the school wear glasses.", f * N_ / n, "students", units=["students"], o="O2", d="H", reason=f"{f}/{n} × {N_} = {fmt(f * N_ / n)}.")
def g5(r):
    return MC("Why do researchers use samples instead of asking the whole population?", "it is quicker and cheaper", [("samples are always more accurate", ""), ("the population is never known", ""), ("it removes all bias", "")], o="O2")
def g6(r):
    sizes = [pick(r, [5, 10]), r.randint(40, 80), r.randint(150, 250)]
    return MC(f"A school has 600 students. Which sample size is most likely to give reliable results?", str(sizes[2]), [str(sizes[0]), str(sizes[1]), "1"], o="O2", reason="A larger random sample is usually more reliable.")
def g7(r):
    a, b, c = r.randint(5, 30), r.randint(5, 30), r.randint(5, 30)
    return N("A random sample of students was asked their favourite season. What fraction chose summer? Give your answer as a decimal to 2 d.p.", round(a / (a + b + c), 2), o="O2", tol=0.006, data={"head": ["Season", "Summer", "Winter", "Spring"], "rows": [["Students", str(a), str(b), str(c)]]}, reason=f"{a} ÷ {a + b + c} ≈ {round(a / (a + b + c), 2)}.")
def g8(r):
    pop, k = pick(r, [(500, 25), (1200, 60), (900, 45), (2000, 80)])
    return N(f"A factory makes {pop} light bulbs a day. A quality check tests every {pop // k}th bulb. How many bulbs are tested each day?", k, "bulbs", units=["bulbs"], o="O2", reason=f"{pop} ÷ {pop // k} = {k}.")
def g9(r):
    rows = [("Asking only Stage 9 students about school lunches", "Biased"), ("Choosing students at random from every year group", "Fair"), ("An online poll on a cat website about favourite pets", "Biased"), ("Picking every 10th name on the full register", "Fair")]
    return GD("Is each sample fair or biased?", "Sample", rows, o="O2", d="H")
def g10(r):
    s1, s2 = r.randint(10, 30), r.randint(100, 200); p1, p2 = r.randint(20, 80), r.randint(40, 60)
    return MC(f"Survey A asked {s1} people and found {p1}% liked a new drink. Survey B asked {s2} people and found {p2}%. Which result is more reliable?", "Survey B", [("Survey A", "A smaller sample is less reliable."), ("both are equally reliable", ""), ("neither, they disagree", "")], o="O2", d="H")
def g11(r):
    b, g = r.randint(8, 20) * 10, r.randint(8, 20) * 10; n = pick(r, [20, 30, 50])
    k = round(b / (b + g) * n)
    return N(f"A school has {b} boys and {g} girls. A sample of {n} should have boys and girls in the same proportion. How many boys should be in the sample?", k, "boys", units=["boys"], o="O2", d="H", tol=0.5, reason=f"{b} ÷ {b + g} × {n} ≈ {k}.")


def g12(r):
    n = pick(r, [40, 50, 80, 100]); y = r.randint(5, n // 2); N_ = r.randint(5, 20) * 100
    return N(f"A random sample of {n} adults in a town of {fmt(N_)} adults found that {y} cycle to work. Estimate the number of adults in the town who cycle to work.", y * N_ / n, "adults", units=["adults"], o="O2", d="H", reason=f"{y}/{n} × {fmt(N_)} = {fmt(y * N_ / n)}.") if (y * N_) % n == 0 else None
def g13(r):
    N_ = r.randint(3, 12) * 100; s_ = pick(r, [30, 40, 50, 60])
    return N(f"A sample of {s_} is taken from a population of {N_}. What percentage of the population is in the sample? Give your answer to 1 d.p.", round(s_ / N_ * 100, 1), "%", units=["%"], o="O2", tol=0.05, reason=f"{s_} ÷ {N_} × 100 ≈ {round(s_ / N_ * 100, 1)}%.")
def g14(r):
    a, b = r.randint(60, 200), r.randint(60, 200); n = pick(r, [20, 25, 40])
    k = round(a / (a + b) * n)
    return TB(f"A sports club has {a} junior and {b} senior members. Complete the proportional sample of {n} members.", ["Group", "Members", "In sample"], [["Junior", str(a), B(k, 0.5)], ["Senior", str(b), B(n - k, 0.5)]], o="O2", d="H", reason=f"{a} ÷ {a + b} × {n} ≈ {k}.")
def g15(r):
    pop = r.randint(5, 20) * 100; k = pick(r, [10, 20, 25, 50])
    return N(f"Every {k}th name on a list of {pop} names is chosen. How many names are chosen?", pop // k, "names", units=["names"], o="O2", reason=f"{pop} ÷ {k} = {pop // k}.")


def b62(r):
    pop, n, k = pick(r, [(800, 40, 6), (1200, 60, 9), (500, 50, 12)])
    return N(f"A random sample of {n} students from a school of {pop} finds that {k} play chess. Estimate how many students in the school play chess.", k * pop // n, "students", units=["students"], o="O2", d="H", reason=f"{k}/{n} of {pop} = {k * pop // n}.")


s.std([g3, g7, g1, g2, g4, g5, g6, g8, g9, g10, g11, g12, g13, g14, g15], EX("Explain why a random sample is less likely to be biased than asking your friends.", [("everyone has the same chance of being chosen", ["same chance|equal chance|anyone"]), ("friends are likely to be similar to you / not representative", ["similar|like you|same opinions|represent"])], "In a random sample everyone has the same chance of being chosen. Your friends are likely to be similar to you, so they do not represent the whole population.", o="O2"),
      deep=[b62])

U.mindmap(("Types of data", "Categorical • discrete (count) • continuous (measure) • primary/secondary", "O1", "6.1"), ("Sampling", "Population vs sample • random • bigger is more reliable • bias", "O2", "6.2"))
