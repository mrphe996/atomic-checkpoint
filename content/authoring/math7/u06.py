# -*- coding: utf-8 -*-
"""Stage 7 Mathematics · Unit 6 Collecting data (6.1 Conducting an investigation, 6.2 Taking a sample).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *

U = Unit(6, "Collecting Data", "Statistics and probability",
         "Planning a statistical investigation: asking a question, choosing what data to collect, tally charts and frequency tables, and choosing a sample.",
         {"O1": {"code": "7Ss.01", "sec": "6.1", "codeNote": "", "t": "Plan an investigation, record data in tally charts and frequency tables, and recognise categorical, discrete and continuous data."},
          "O2": {"code": "7Ss.02", "sec": "6.2", "codeNote": "", "t": "Understand populations and samples, and choose a sample that represents the population."}})
TAL = lambda x: "|||| " * (x // 5) + "|" * (x % 5)

# ================================================================== 6.1
s = U.section("6.1", "Conducting an investigation", ["O1"])
s.idea("The data cycle", ["1. Ask a **question** you can answer with data. 2. **Collect** the data. 3. **Organise** it in a table or chart. 4. **Interpret** it and answer the question.",
       "**Categorical** data are words (favourite colour). **Discrete** data are counted (number of pets). **Continuous** data are measured (height)."])
s.method("Tally charts", ["Make one mark for each result. Every fifth mark crosses the four before it: |||| , so you can count in fives.", "The **frequency** is the total number of tallies."])
s.check(N("A tally shows |||| |||| |||. What is the frequency?", 13, o="O1"))
s.idea("Why the type of data matters", ["The type of data decides how you collect and show it. Categorical data (colours) cannot be put in number order, so a bar chart with gaps fits.",
       "Continuous data (heights) can take any value, so you group it into classes such as 140 ≤ h < 150, with no gaps and no overlaps, so every value fits exactly one class."])
s.check(MC("Before you read on: is 'shoe size' discrete or continuous?", "Discrete", [("Continuous", "Feet grow continuously, but shoe sizes are only sold in set steps (4, 4½, 5 …)."), ("Categorical", "Shoe sizes are numbers.")], o="O1"))
s.example("A good question or a vague one?", "Compare: 'Do students like sport?' and 'How many hours of sport do Stage 7 students do each week?'", [("the first is vague", "'like' means different things, and the answer is only yes or no"),
          ("the second can be measured", "it names the group and the quantity")], "The second question")
s.mistake("Count in fives", ["Each bundle |||| is 5, not 4."])
FRUIT = ["Apple", "Banana", "Mango", "Orange", "Grape", "Pear"]


def d1(r):
    t = [r.randint(2, 14) for _ in range(4)]; lab = r.sample(FRUIT, 4); k = r.randrange(4)
    return N(f"The tally chart shows favourite fruits. How many people chose {lab[k].lower()}?", t[k], "people", units=["people"], o="O1", data={"head": ["Fruit", "Tally"], "rows": [[lab[i], TAL(t[i])] for i in range(4)]})
def d2(r):
    t = [r.randint(2, 14) for _ in range(4)]; lab = r.sample(FRUIT, 4)
    return TB("Complete the frequency column.", ["Fruit", "Frequency"], [[lab[i], B(t[i])] for i in range(4)], o="O1", data={"head": ["Fruit", "Tally"], "rows": [[lab[i], TAL(t[i])] for i in range(4)]})
def d3(r):
    t = [r.randint(2, 14) for _ in range(4)]; lab = r.sample(FRUIT, 4)
    return N("How many people took part in the survey?", sum(t), "people", units=["people"], o="O1", data={"head": ["Fruit", *lab], "rows": [["Frequency", *map(str, t)]]})
def d4(r):
    rows = [("Number of pets", "Discrete"), ("Height of a plant", "Continuous"), ("Favourite colour", "Categorical"), ("Number of goals", "Discrete"), ("Time to run 100 m", "Continuous"), ("Type of car", "Categorical"), ("Mass of a bag", "Continuous"), ("Number of brothers", "Discrete")]
    return GD("What type of data is each?", "Type", r.sample(rows, 5), o="O1", extra=["Categorical", "Discrete", "Continuous"])
def d5(r):
    t = [r.randint(2, 14) for _ in range(4)]; lab = r.sample(FRUIT, 4)
    k = max(range(4), key=lambda i: t[i])
    if t.count(t[k]) > 1: t[k] += 1
    return MC("Which fruit was the most popular?", lab[k], [x for x in lab if x != lab[k]], o="O1", data={"head": ["Fruit", "Tally"], "rows": [[lab[i], TAL(t[i])] for i in range(4)]})
def d6(r):
    q = pick(r, [("Do older students sleep less?", "the age and hours of sleep of each student"), ("Which flavour of ice cream is most popular?", "each person's favourite flavour"), ("Are boys taller than girls in our class?", "the height and gender of each student")])
    return MC(f"A student wants to answer: “{q[0]}” What data should she collect?", q[1], ["the names of the students", "the number of students in the school", "the colour of their bags"], o="O1")
def d7(r):
    a, b = r.randint(5, 30), r.randint(5, 30)
    if a == b: return None
    return N(f"In a survey {a} people chose football and {b} chose tennis. How many more chose {'football' if a > b else 'tennis'}?", abs(a - b), o="O1")
def d8(r):
    vals = [r.randint(0, 5) for _ in range(20)]; k = r.randint(0, 5)
    return N(f"These are the numbers of pets of 20 students: {', '.join(map(str, vals))}. How many students have {k} pet{'s' if k != 1 else ''}?", vals.count(k), "students", units=["students"], o="O1", d="H")
def d9(r):
    steps = ["Ask a question", "Collect the data", "Organise the data in a table", "Interpret the results and answer the question"]
    return OD("Put the stages of an investigation in order.", steps, o="O1")
def d10(r):
    n = r.randint(20, 40); pc = pick(r, [10, 20, 25, 50])
    if (n * pc) % 100: return None
    return N(f"{n} students answered a survey. {pc}% said yes. How many students said yes?", n * pc // 100, "students", units=["students"], o="O1")
def d11(r):
    t = [r.randint(1, 12) for _ in range(5)]; lab = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    return N("The table shows the number of late students each day. How many were late during the week?", sum(t), o="O1", data={"head": ["Day", *lab], "rows": [["Late", *map(str, t)]]})


def d12(r):
    h = [r.randint(5, 30) for _ in range(6)]
    return N(f"A gardener measured six seedlings (in mm): {', '.join(map(str, h))}. What is the difference between the tallest and the shortest?", max(h) - min(h), "mm", units=["mm"], o="O1")
def d13(r):
    days = r.randint(20, 31); rain = r.randint(3, days - 3)
    return N(f"In a month of {days} days it rained on {rain} days. On how many days did it not rain?", days - rain, "days", units=["days"], o="O1")
def d14(r):
    c = [r.randint(3, 15) for _ in range(3)]
    return N("The table shows how a class travels to school. What fraction of the class comes by car? Give a decimal to 2 d.p.", round(c[0] / sum(c), 2), o="O1", tol=0.006, data={"head": ["Travel", "Car", "Bus", "Walk"], "rows": [["Students", *map(str, c)]]})
def d15(r):
    return MC(pick(r, ["Which question is best for a survey about reading?", "Which is the best survey question about reading habits?"]), "How many books did you read last month?", ["Do you read a lot?", "Don't you agree reading is great?", "Why don't you read more?"], o="O1")


def q1(r):   # classify data types
    rows = r.sample([("eye colour", "Categorical"), ("number of brothers", "Discrete"), ("time to run 100 m", "Continuous"), ("favourite sport", "Categorical"),
                     ("mass of a bag", "Continuous"), ("goals scored", "Discrete"), ("height of a plant", "Continuous")], 4)
    return GD("What type of data is each one?", "Type", rows, o="O1", d="H", extra=["Categorical", "Discrete", "Continuous"],
              reason="Words → categorical; counted → discrete; measured → continuous.")
def q2(r):   # spot the error in classes
    return MC("Lin groups heights as 140–150, 150–160, 160–170 cm. What is wrong?", "A height of exactly 150 cm fits two classes", [("Nothing", "Where does 150 cm go?"), ("The classes are too wide", "Width 10 cm is fine.")], o="O1", d="H",
              reason="Use classes such as 140 ≤ h < 150 so every height belongs to exactly one class.")
def q3(r):   # best question
    return MC("Which is the best question for an investigation about screen time?", "How many minutes did you spend on a screen yesterday?",
              [("Do you use screens too much?", "Too much is an opinion; the answer cannot be compared."), ("Screens are bad, aren't they?", "This is a leading question."), ("Do you have a phone?", "It does not measure screen time.")], o="O1", d="H",
              reason="A good question is clear, not leading, and gives data you can compare.")
def q4(r):   # missing frequency from total
    t = [r.randint(3, 15) for _ in range(4)]; tot = sum(t); k = r.randrange(4)
    return N(f"In a vote with 4 options, the frequency for one option is smudged. The others are " + ", ".join(str(t[i]) for i in range(4) if i != k) + f". The total was {tot}. Find the missing frequency.", t[k], o="O1", d="H",
             reason=f"{tot} − " + " − ".join(str(t[i]) for i in range(4) if i != k) + f" = {t[k]}.")


s.std([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15], EX("Explain why a tally chart groups marks in fives.", [("it makes the tallies easy to count", ["easy|quick|count"]), ("you can count in fives", ["five|5"])], "Crossing every fifth tally makes bundles of 5, so you can count the tallies quickly in fives instead of one by one.", o="O1"),
      deep=[q1, q2, q3, q4])

# ================================================================== 6.2
s = U.section("6.2", "Taking a sample", ["O2"])
s.idea("Population and sample", ["The **population** is everyone you want to know about. A **sample** is a smaller group you ask.",
       "A good sample is **big enough** and **represents** the whole population, for example by choosing people at **random**."])
s.example("Biased sample", "To find out what Stage 7 students think of lunch, Ravi asks his 5 best friends. Why is this a poor sample?", [("5 is a very small sample", ""), ("friends may have similar opinions", "")], "Too small and not random")
s.check(N("A school has 400 students. A 10% sample is taken. How many students is that?", 40, "students", units=["students"], o="O2"))
s.idea("Why a random sample is fairer", ["If every member of the population has the same chance of being chosen, no group is left out on purpose, so the sample tends to look like the population.",
       "A bigger sample gives results that change less from sample to sample, but it costs more time. Choose a size that is practical and big enough."])
s.check(MC("Before you read on: to find out how students travel to school, is it fair to ask only the students at the bus stop?", "No", [("Yes", "Everyone there arrived by bus – walkers and cyclists are left out."), ("Yes, if you ask many of them", "A big biased sample is still biased.")], o="O2"))
s.mistake("Not just friends", ["Asking only your friends, or only people in one place, can give biased results."])


def g1(r):
    pop = r.randint(4, 20) * 50; pc = pick(r, [10, 20, 25, 50])
    return N(f"A club has {pop} members. A {pc}% sample is taken. How many members are in the sample?", pop * pc / 100, "members", units=["members"], o="O2")
def g2(r):
    rows = [("Names picked from a hat", "Random"), ("Asking your friends", "Not random"), ("A computer chooses names from a list", "Random"), ("The first 10 people in the queue", "Not random"), ("People who reply to an advert", "Not random")]
    return GD("Is each way of choosing a sample random?", "Random?", r.sample(rows, 4), o="O2")
def g3(r):
    place, why = pick(r, [("at a football match", "most people there like football"), ("outside a library", "people there probably like reading"), ("at a swimming pool", "people there probably like swimming")])
    return MC(f"A survey about favourite sports is done only {place}. Why could the results be biased?", why, ["the sample is random", "the survey is too long", "the data is continuous"], o="O2")
def g4(r):
    n, k, N_ = pick(r, [(20, 5, 400), (50, 10, 600), (40, 8, 800), (25, 6, 500)])
    return N(f"In a random sample of {n} students, {k} walk to school. Estimate how many of the {N_} students in the school walk.", k * N_ / n, "students", units=["students"], o="O2", d="H")
def g5(r):
    a, b = r.randint(5, 15), r.randint(100, 200)
    return MC(f"Survey A asks {a} people. Survey B asks {b} people chosen at random. Which is likely to be more reliable?", "Survey B", ["Survey A", "Both the same", "Neither"], o="O2")
def g6(r):
    b, g = r.randint(5, 15) * 10, r.randint(5, 15) * 10
    return N(f"A school has {b} boys and {g} girls. What fraction of the students are boys? Give a decimal to 2 d.p.", round(b / (b + g), 2), o="O2", tol=0.006, data={"head": ["", "Boys", "Girls"], "rows": [["Number", str(b), str(g)]]})
def g7(r):
    pop = r.randint(3, 12) * 100; s_ = pick(r, [20, 30, 50, 60])
    return N(f"A sample of {s_} is taken from {pop} people. What percentage of the population is that? Give your answer to 1 d.p.", round(s_ / pop * 100, 1), "%", units=["%"], o="O2", tol=0.05)
def g8(r):
    return MC("Which is the best way to choose a sample of 30 students from a school?", "pick 30 names at random from the whole school list", ["ask 30 students in the football team", "ask the first 30 students to arrive", "ask 30 students in your class"], o="O2")
def g9(r):
    n = pick(r, [100, 200, 300]); k = r.randint(10, 40)
    return N(f"Every {n // k}th name on a list of {n} names is chosen. How many names are chosen?", k, o="O2") if n % k == 0 else None
def g10(r):
    a, b, c = r.randint(5, 20), r.randint(5, 20), r.randint(5, 20)
    return N("In a sample, how many students chose maths or science?", a + b, o="O2", data={"head": ["Subject", "Maths", "Science", "Art"], "rows": [["Students", str(a), str(b), str(c)]]})
def g11(r):
    pop = r.randint(200, 1000)
    return MC(f"A town has {pop} homes. Which sample size is most sensible?", str(pop // 10), ["2", str(pop - 1), "1"], o="O2", d="H")


def g12(r):
    yes, n = r.randint(5, 25), pick(r, [30, 40, 50])
    return N(f"In a sample of {n} shoppers, {yes} said they would buy a new snack. What percentage is that?", yes / n * 100, "%", units=["%"], o="O2", tol=0.05)
def g13(r):
    a = r.randint(150, 400); b = r.randint(150, 400)
    return N(f"Two schools have {a} and {b} students. A 10% sample is taken from each. How many students are sampled in total? (Round each sample to the nearest whole number.)", round(a / 10) + round(b / 10), "students", units=["students"], o="O2", d="H")
def g14(r):
    k = r.randint(2, 6); n = r.randint(20, 40)
    return N(f"A teacher picks one student out of every {k} on the register. There are {n * k} students. How many does she pick?", n, "students", units=["students"], o="O2")


def s1(r):   # biased or fair
    rows = r.sample([("asking every 10th name on the school register", "Fair"), ("asking people leaving a gym about exercise", "Biased"), ("drawing names from a hat", "Fair"),
                     ("asking only Stage 9 students about the Stage 7 menu", "Biased"), ("asking your friends", "Biased"), ("choosing students with a random-number generator", "Fair")], 4)
    return GD("Is each sampling method fair or biased?", "Fair or biased", rows, o="O2", d="H", extra=["Fair", "Biased"], reason="A fair method gives everyone in the population the same chance; a biased one leaves some groups out.")
def s2(r):   # estimate from sample
    pop = pick(r, [400, 500, 600, 800]); n = pick(r, [40, 50]); k = r.randint(5, n // 2)
    return N(f"In a random sample of {n} students from a school of {pop}, {k} walk to school. Estimate how many students in the whole school walk.", k * pop // n, "students", units=["students"], o="O2", d="H",
             reason=f"{k} out of {n} is the same fraction as ? out of {pop}: {k} × {pop // n} = {k * pop // n}.") if pop % n == 0 else None
def s3(r):   # which sample size
    return MC("A town has 20 000 people. Which sample size is most sensible for a quick survey?", "200", [("2", "Too small: two people can easily be unusual."), ("20 000", "That is the whole population – a census, not a sample."), ("19 000", "Almost everyone – too slow and costly.")], o="O2", d="H",
              reason="A few hundred people is big enough to be reliable and small enough to be practical.")


s.std([g2, g6, g1, g3, g4, g5, g7, g8, g9, g10, g11, g12, g13, g14], EX("Explain why choosing a sample at random helps to avoid bias.", [("everyone has the same chance of being chosen", ["same chance|equal chance|anyone"]), ("so no group is left out or favoured", ["left out|favour|represent|fair"])], "In a random sample everyone has the same chance of being picked, so no group is favoured or left out and the sample is more likely to represent the population.", o="O2"),
      deep=[s1, s2, s3])

U.mindmap(("Investigation", "Question • collect • organise • interpret • tally charts", "O1", "6.1"), ("Sampling", "Population • sample • random • big enough", "O2", "6.2"))
