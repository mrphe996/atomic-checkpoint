# -*- coding: utf-8 -*-
"""Stage 8 Unit 1 Diet and Growth — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-WHODIET", "name": "World Health Organization – Healthy diet (fact sheet)", "url": "https://www.who.int/news-room/fact-sheets/detail/healthy-diet", "use": "Free sugars should be less than 10% of total energy intake; at least 400 g of fruit and vegetables a day (Challenge questions, 1.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u01n11p": dict(note="Paused before iodine is dropped on bread, sugar, potato and cheese.",
   q=ms("s8u01n11p_q", "M", "O1", "PREDICT: which TWO foods will turn blue-black with iodine?", ["bread", "potato"], [("sugar", "Watch carefully."), ("cheese", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u01n11p_t", "M", "O1", "Iodine solution is used to test for…", "starch", [("protein", ""), ("fat", ""), ("vitamin C", "")])),
 "s8u01n11e": dict(note="Paused after bread and potato turned blue-black.",
   q=ex("s8u01n11e_q", "H", "O1", "EXPLAIN why sugar stayed orange-brown even though it is a carbohydrate.",
        [("iodine tests only for starch", ["starch"]), ("sugar is a simple carbohydrate, not starch", ["not starch|simple|different|isn't starch|is not starch"])],
        "Iodine only turns blue-black with starch. Sugar is a simple carbohydrate, not starch, so the iodine stayed orange-brown."),
   twin=mc("s8u01n11e_t", "M", "O1", "Which food would turn iodine blue-black?", "Rice", [("Butter", ""), ("Egg white", ""), ("Salt", "")])),
 "s8u01n12": dict(note="Paused on the chart: carbohydrate 17, protein 17, fat 37, fibre 8 kJ per gram.",
   q=mc("s8u01n12_q", "H", "O1", "Why do hibernating animals store most of their energy as fat?", ("Fat stores more than twice as much energy per gram", "Yes – it is a compact store."),
        [("Fat contains no energy", "Fat has 37 kJ per gram."), ("Fat is a vitamin", "Fat is a nutrient, not a vitamin."), ("Fat is easier to digest than water", "That is not the reason.")], skill="Data"),
   twin=nm("s8u01n12_t", "H", "O1", "How much energy is in 10 g of fat (37 kJ per gram)?", 370, "kJ", tol=0, units=["kJ"])),
 "s8u01n13": dict(note="Paused after the balanced lunch box.",
   q=ms("s8u01n13_q", "H", "O3", "A lunch of crisps, chocolate and a fizzy drink is missing which TWO things most?", ["protein", "vitamins and fibre from fruit and vegetables"], [("sugar", "It has plenty of sugar."), ("fat", "Crisps and chocolate contain a lot of fat.")]),
   twin=mc("s8u01n13_t", "M", "O3", "Half of a healthy plate should be…", "fruit and vegetables", [("meat", ""), ("sweets", ""), ("oil", "")])),
 "s8u01n14": dict(note="Paused on the graph: resting heart rate fell from 78 to 69 beats per minute in 8 weeks.",
   q=ex("s8u01n14_q", "H", "O4", "Why does a stronger heart need fewer beats per minute at rest?",
        [("a stronger heart pumps more blood with each beat", ["more blood|each beat|per beat|stronger"]), ("so fewer beats supply the same oxygen / blood the body needs", ["fewer|same|enough|supply|oxygen"])],
        "A stronger heart pumps more blood with each beat, so it needs fewer beats per minute to supply the body with the oxygen it needs at rest."),
   twin=nm("s8u01n14_t", "M", "O4", "By how many beats per minute did her resting heart rate fall (78 → 69)?", 9, "beats per minute", tol=0, units=["beats per minute", "bpm", ""])),
}

DROP = {"1.1": ["s8u01s1p01", "s8u01s1p12", "s8u01s1p15"], "1.2": ["s8u01s2p01", "s8u01s2p03", "s8u01s2p11"], "1.3": ["s8u01s3p02", "s8u01s3p03", "s8u01s3p14"]}

LABEL = {"kind": "barchart", "labels": ["cereal A", "cereal B", "cereal C"], "values": [35, 8, 18], "ymax": 40, "step": 5, "ylabel": "Sugar (g per 100 g)", "xlabel": "Breakfast cereal"}
GROW = {"kind": "linegraph", "x": {"min": 0, "max": 18, "step": 3, "label": "Age (years)"}, "y": {"min": 0, "max": 180, "step": 30, "label": "Height (cm)"},
        "series": [{"pts": [[0, 50], [3, 95], [6, 115], [9, 133], [12, 150], [15, 168], [18, 175]], "label": "one person"}]}
SLEEP = {"kind": "barchart", "labels": ["5 h", "6 h", "7 h", "8 h", "9 h"], "values": [52, 60, 68, 75, 76], "ymax": 80, "step": 10, "ylabel": "Mean memory test score (%)", "xlabel": "Hours of sleep the night before"}
NEW_PRAC = {
 "1.1": [
  gd("s8u01s1p21", "M", "O1", "Which food test gives each result?", ["Nutrient"],
     [("Iodine turns blue-black", ["Starch"]), ("Paper goes see-through and greasy", ["Fat"]), ("Biuret solution turns purple", ["Protein"])], extra=["Water"]),
  od("s8u01s1p22", "H", "O2", "Order the steps to test a food for starch.", ["Put a small piece of food on a white tile", "Add two drops of iodine solution", "Wait a few seconds", "Look for a blue-black colour"]),
  nm("s8u01s1p23", "H", "O1", "A snack has 5 g of fat (37 kJ/g) and 20 g of carbohydrate (17 kJ/g). What is its total energy?", 525, "kJ", tol=0, units=["kJ"], hint="5 × 37 + 20 × 17"),
 ],
 "1.2": [
  mc("s8u01s2p21", "M", "O3", "Use the bar chart. Which cereal is the healthiest choice for sugar?", "Cereal B", [("Cereal A", "Cereal A has the most sugar."), ("Cereal C", "Cereal C has more sugar than B."), ("They are the same", "The bars are different.")], fig=LABEL, skill="Data"),
  nm("s8u01s2p22", "H", "O3", "Use the bar chart. How much sugar is in a 40 g bowl of cereal A?", 14, "g", tol=0, units=["g"], fig=LABEL, skill="Data"),
  mc("s8u01s2p23", "H", "O3", "Use the graph of height. During which period does this person grow fastest?", "From birth to 3 years", [("From 15 to 18 years", "The line is almost flat then."), ("From 6 to 9 years", "Growth is steady then."), ("Growth is the same at all ages", "The line is steeper at the start.")], fig=GROW, skill="Data"),
 ],
 "1.3": [
  mc("s8u01s3p21", "M", "O4", "Use the bar chart. After how many hours of sleep did students score highest?", "9 hours", [("5 hours", "That is the lowest score."), ("7 hours", "Scores were higher with more sleep."), ("6 hours", "Scores were higher with more sleep.")], fig=SLEEP, skill="Data"),
  ex("s8u01s3p22", "H", "O4", "Use the bar chart. What does it suggest about sleep and learning? Give one reason why you should be careful about the conclusion.",
     [("more sleep → higher scores (up to about 8 h)", ["more sleep|higher|better|increase"]), ("caution: other variables / sample size / correlation not cause", ["other (variable|factor)|sample|correlat|cause|only one|repeat"])],
     "Students who slept more scored higher, with little extra benefit after 8 hours. But other factors (such as how much they revised) could also affect scores, so this does not prove that sleep causes the difference.", fig=SLEEP),
  gd("s8u01s3p23", "H", "O4", "Healthy or unhealthy habit?", ["Habit"],
     [("Walking or cycling to school", ["Healthy"]), ("Drinking sugary fizzy drinks every day", ["Unhealthy"]), ("Getting about 8 hours of sleep", ["Healthy"]), ("Vaping", ["Unhealthy"])], extra=[]),
 ],
}
NEW_ADV = {
 "1.2": [adv(nm("s8u01s2a05", "VH", "O3", "The WHO says free sugars should be less than 10% of total energy intake. A student takes in 8500 kJ a day. Sugar gives about 17 kJ per gram. What is the most free sugar she should eat in a day? (nearest gram)", 50, "g", tol=1, units=["g"],
     hint="10% of 8500 kJ, then divide by 17.", src=src("SRC-WHODIET")))],
}

from tests_stage8_unit01_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
