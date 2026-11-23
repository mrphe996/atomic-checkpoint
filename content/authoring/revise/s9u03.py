# -*- coding: utf-8 -*-
"""Stage 9 Unit 3 Variation and Inheritance — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-WHOAMR", "name": "World Health Organization – Antimicrobial resistance (fact sheet)", "url": "https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance", "use": "Misuse and overuse of antibiotics drive resistance: Challenge question (3.4)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

HT = {"kind": "barchart", "labels": ["140–144", "145–149", "150–154", "155–159", "160–164", "165–169"], "values": [2, 5, 9, 8, 4, 2], "ymax": 10, "step": 2, "ylabel": "Number of students"}
RAB = {"kind": "linegraph", "x": {"min": 0, "max": 8, "step": 1, "label": "Years after release"}, "y": {"min": 0, "max": 500, "step": 100, "label": "Number of rabbits"},
       "series": [{"pts": [[0, 20], [1, 45], [2, 110], [3, 240], [4, 380], [5, 450], [6, 470], [7, 460], [8, 470]], "label": "rabbits"}]}

NEW_STOPS = {
 "s9u03n21p": dict(note="Paused before a coin is tossed 100 times to model X or Y sperm.",
   q=mc("s9u03n21p_q", "M", "O2", "PREDICT: about how many of the 100 'babies' will be girls?", ("About 50", "Good prediction – now watch."),
        [("About 25", "Watch carefully."), ("About 75", "Watch carefully."), ("Exactly 100", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u03n21p_t", "M", "O2", "Every human egg cell carries…", "an X chromosome", [("a Y chromosome", ""), ("either an X or a Y", ""), ("no sex chromosome", "")])),
 "s9u03n21e": dict(note="Paused after 100 tosses gave 48 girls and 52 boys.",
   q=ex("s9u03n21e_q", "H", "O2", "EXPLAIN the result and say which parent decides the sex of a baby.",
        [("half of sperm carry X and half carry Y, so equal chance / about half girls", ["half|equal|50|same chance"]), ("the father, because his sperm carries X or Y (egg always X)", ["father|sperm|dad"])],
        "Half of the sperm carry an X and half carry a Y, so there is an equal chance of XX (girl) or XY (boy), giving close to half girls in a large sample. The father decides the sex, because the egg always carries an X but the sperm can carry X or Y."),
   twin=mc("s9u03n21e_t", "H", "O2", "Why were the results after 20 tosses (11 girls, 9 boys) further from half than after 100?", "Small samples are more affected by chance", [("The coin changed", ""), ("Boys are more likely at first", ""), ("The model only works for girls", "")])),
 "s9u03n31": dict(note="Paused on the chart of 30 students' heights in 5 cm groups.",
   q=ex("s9u03n31_q", "H", "O4", "Is height continuous or discontinuous variation, and what causes it?",
        [("continuous: it can take any value in a range", ["continuous|any value|range"]), ("caused by both genes and the environment (e.g. diet)", ["both|genes and|inherited and|diet|nutrition|environment"])],
        "Height is continuous variation: it can have any value within a range. It is caused by both genes (inherited) and the environment, for example diet and health.", skill="Data"),
   twin=nm("s9u03n31_t", "M", "O4", "Use the chart. How many students are between 150 and 159 cm tall?", 17, "students", tol=0, units=["students", ""], fig=HT)),
 "s9u03n41p": dict(note="Paused before 'birds' hunt red and green paper worms on grass.",
   q=mc("s9u03n41p_q", "M", "O5", "PREDICT: which colour of worm will survive better?", ("Green", "Good prediction – now watch."),
        [("Red", "Watch carefully."), ("Both the same", "Watch carefully."), ("Neither will be found", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u03n41p_t", "M", "O5", "Camouflage is…", "colouring that helps an organism blend in with its surroundings", [("a type of food", ""), ("a disease", ""), ("a way of breathing", "")])),
 "s9u03n41e": dict(note="Paused after 1 red and 8 green worms survived.",
   q=od("s9u03n41e_q", "H", "O5", "EXPLAIN by ordering the steps of natural selection.", ["There is variation in colour in the population", "Camouflaged individuals are less likely to be eaten", "They survive and breed", "They pass on their genes, so the variation becomes more common"]),
   twin=mc("s9u03n41e_t", "H", "O5", "If the worms were on bare brown soil, which would survive best?", "Brown worms", [("Green worms", ""), ("Red worms", ""), ("All the same", "")])),
 "s9u03n51": dict(note="Paused on the graph: rabbits rise from 20 to about 470 and level off after 5 years.",
   q=ex("s9u03n51_q", "H", "O6", "Why does the rabbit population stop growing, and what is the maximum number called?",
        [("food / water / space run short (limited resources)", ["food|water|space|resource|grass|compet"]), ("the carrying capacity", ["carrying capacity"])],
        "The island has limited food, water and space, so once there are about 470 rabbits there is not enough for more to survive. This maximum is the carrying capacity.", skill="Data"),
   twin=nm("s9u03n51_t", "M", "O6", "Use the graph. By how much did the population increase between year 2 and year 4?", 270, "rabbits", tol=0, units=["rabbits", ""], fig=RAB)),
}

DROP = {"3.1": ["s9u03s1p02", "s9u03s1p01"], "3.2": ["s9u03s2p04", "s9u03s2p05"], "3.3": ["s9u03s3p02", "s9u03s3p06"],
        "3.4": ["s9u03s4p05", "s9u03s4p06"], "3.5": ["s9u03s5p03", "s9u03s5p07"]}

MOTH = {"kind": "linegraph", "x": {"min": 1850, "max": 2000, "step": 25, "label": "Year"}, "y": {"min": 0, "max": 100, "step": 20, "label": "Dark moths in the population (%)"},
        "series": [{"pts": [[1850, 2], [1875, 40], [1900, 90], [1950, 90], [1970, 80], [1985, 40], [2000, 10]], "label": "near an industrial city (example data)"}]}
NEW_PRAC = {
 "3.1": [
  od("s9u03s1p21", "M", "O1", "Order from largest to smallest.", ["nucleus", "chromosome", "gene", "DNA base"]),
  nm("s9u03s1p22", "H", "O1", "A human body cell has 46 chromosomes. How many chromosomes are in 3 body cells altogether?", 138, "chromosomes", tol=0, units=["chromosomes", ""]),
 ],
 "3.2": [
  mc("s9u03s2p21", "H", "O2", "A couple already have three girls. What is the chance that their next baby is a boy?", "1 in 2 (50 %)", [("1 in 4", "Each baby is independent."), ("Almost certain", "Earlier babies do not change the chance."), ("Zero", "Every pregnancy has an equal chance.")]),
  gd("s9u03s2p22", "M", "O3", "Which structure does each job?", ["Structure"],
     [("Passes oxygen and food to the fetus", ["Placenta"]), ("Cushions the fetus", ["Amniotic fluid"]), ("Joins the fetus to the placenta", ["Umbilical cord"])], extra=["Ovary"]),
 ],
 "3.3": [
  mc("s9u03s3p21", "M", "O4", "Use the chart. Which height group has the most students?", "150–154 cm", [("155–159 cm", "8 students."), ("145–149 cm", "5 students."), ("165–169 cm", "2 students.")], fig=HT, skill="Data"),
  ex("s9u03s3p22", "H", "O4", "Identical twins are raised in different countries. One grows 6 cm taller. Explain what this shows.",
     [("identical twins have the same genes / DNA", ["same (genes|dna)|identical"]), ("so the difference is caused by the environment, e.g. diet or health", ["environment|diet|food|nutrition|health"])],
     "Identical twins have exactly the same genes, so the 6 cm difference must be caused by the environment, such as diet, health or exercise."),
 ],
 "3.4": [
  nm("s9u03s4p21", "M", "O5", "Use the graph. What percentage of moths were dark in 1900?", 90, "%", tol=2, units=["%"], fig=MOTH, skill="Data"),
  ex("s9u03s4p22", "H", "O5", "Use the graph. Soot pollution blackened tree trunks in the 1800s, and clean-air laws reduced it after 1950. Explain the changes using natural selection.",
     [("dark moths were camouflaged on sooty trunks, so fewer were eaten and they bred: % rose", ["dark.{0,40}(camouflag|hidden|less likely|survive)|soot"]), ("after clean-air laws, trunks became lighter, so light moths survived better and dark % fell", ["light.{0,40}(survive|camouflag)|clean|fell|decreas"])],
     "When trunks were black with soot, dark moths were camouflaged, so birds ate fewer of them; they survived, bred and passed on their genes, so the dark percentage rose to 90 %. After clean-air laws the trunks became lighter, so light moths were camouflaged instead and the dark percentage fell.", fig=MOTH, skill="Data"),
 ],
 "3.5": [
  nm("s9u03s5p21", "M", "O6", "Use the rabbit graph. What is the carrying capacity of the island (about)?", 470, "rabbits", tol=10, units=["rabbits", ""], fig=RAB, skill="Data"),
  ex("s9u03s5p22", "H", "O6", "Foxes are introduced to the island. Predict and explain what happens to the rabbit population.",
     [("the rabbit population falls", ["fall|decreas|drop|go down|fewer"]), ("foxes are predators that eat rabbits", ["predat|eat|hunt|kill"])],
     "The rabbit population falls, because foxes are predators that eat rabbits, so more rabbits die than before."),
 ],
}
NEW_ADV = {
 "3.4": [adv(ex("s9u03s4a05", "VH", "O5", "The WHO warns that the misuse and overuse of antibiotics are making resistant bacteria more common. Use natural selection to explain why, and suggest TWO ways people can help slow it down.",
     [("some bacteria have a variation that makes them resistant", ["variation|some bacteria|resistant gene|mutation"]), ("antibiotics kill the others; resistant ones survive and reproduce, passing on resistance", ["survive|reproduce|multiply|pass on|breed"]), ("only use antibiotics when prescribed and finish the course / not for viruses", ["prescri|finish|full course|not for (viruses|colds)|only when"])],
     "In any population of bacteria, a few have a variation that makes them resistant. Each time antibiotics are used, the others are killed but the resistant ones survive, reproduce quickly and pass on the resistance, so resistant bacteria become more common. People can help by using antibiotics only when a doctor prescribes them, never for viral illnesses such as colds, and by finishing the whole course.", need=2, src=src("SRC-WHOAMR")))],
}

from tests_stage9_unit03_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
