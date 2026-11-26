# -*- coding: utf-8 -*-
"""Stage 7 Unit 4 Classifying Living Things — 2026 revision (written by the Camday teaching team).
Practice: same-reasoning recall out; data, graph, key and experiment questions in. Challenge: outside ideas, sources named."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NSTALIV", "name": "NSTA, Science and Children – Formative Assessment Probes: Is It Living? (Page Keeley)", "url": "https://www.nsta.org/journals/science-and-children/science-and-children-aprilmay-2011/formative-assessment-probes-it", "use": "Idea for the 'is it living?' Challenge question about a seed and a fire (4.1)."},
    {"id": "SRC-NSTALC", "name": "NSTA – Formative Assessment Probe: Does It Have a Life Cycle? (Page Keeley)", "url": "https://www.nsta.org/lesson-plan/does-it-have-life-cycle", "use": "Idea for the life-cycle Challenge question (4.4)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u4n41p": dict(note="Paused before the yeast bottles are kept warm: A yeast + sugar, B yeast without sugar.",
   q=mc("u4n41p_q", "M", "O1", "PREDICT: after one hour in a warm place, what will happen to the balloons?", ("Balloon A (with sugar) will blow up; balloon B will hardly change", "Good prediction – now watch."),
        [("Both balloons will blow up the same amount", "Watch – one bottle is missing something."), ("Balloon B will blow up more", "Think about what yeast needs as food."), ("Neither balloon will change, because yeast is not alive", "Watch closely.")], skill="Prediction"),
   twin=mc("u4n41p_t", "M", "O1", "What does yeast need as food in this experiment?", "Sugar", [("Salt", ""), ("Light", ""), ("Sand", "")])),
 "u4n41e": dict(note="Paused after balloon A inflated.",
   q=ex("u4n41e_q", "H", "O1", "EXPLAIN why balloon A blew up and what this shows about yeast.",
        [("yeast respired / used sugar as food", ["respir|sugar|food|feed"]), ("released carbon dioxide gas", ["carbon dioxide|co2|gas"]), ("so yeast is alive (shows life processes)", ["alive|living|life process"])],
        "The yeast used the sugar as food and respired, releasing carbon dioxide gas that blew up the balloon. This shows nutrition and respiration, so yeast is alive.", need=2),
   twin=mc("u4n41e_t", "H", "O1", "Why was bottle B (no sugar) included?", "As a control, to show that the sugar caused the gas", [("To make the test faster", ""), ("Because yeast hates sugar", ""), ("To use up spare balloons", "")])),
 "u4n42": dict(note="Paused after four real examples: cold, vaccines, antibiotics, plant viruses.",
   q=mc("u4n42_q", "M", "O2", "Why does a doctor NOT give antibiotics for a cold?", ("Colds are caused by viruses, and antibiotics only kill bacteria", "Right – antibiotics have no effect on viruses."),
        [("Colds are caused by bacteria that are too small", "Colds are mostly caused by viruses."), ("Antibiotics make colds last longer", "That is not the reason."), ("Colds are not caused by anything", "Colds are caused by viruses such as rhinoviruses.")]),
   twin=mc("u4n42_t", "M", "O2", "What does a vaccine do?", "Trains the body to recognise a virus before it causes illness", [("Kills bacteria", ""), ("Makes viruses bigger", ""), ("Cures a cold in one day", "")])),
 "u4n43": dict(note="Paused on the bar chart of named species: insects ≈ 1 000 000, plants ≈ 390 000.",
   q=mc("u4n43_q", "H", "O3", "About how many times more named insect species are there than plant species?", "About 2.5 times", [("About 10 times", "1000 ÷ 390 is between 2 and 3."), ("About the same", "The insect bar is much taller."), ("About 100 times", "1000 ÷ 390 is between 2 and 3.")], skill="Data"),
   twin=mc("u4n43_t", "M", "O3", "Which group has the most named species?", "Insects", [("Mammals", ""), ("Birds", ""), ("Fish", "")])),
 "u4n44": dict(note="Paused after bat, starfish, seahorse and spider.",
   q=mc("u4n44_q", "M", "O5", "A whale lives in the sea, breathes air, has hair and feeds its young on milk. Which vertebrate group is it in?", ("Mammals", "Yes – milk and hair make it a mammal."),
        [("Fish", "It lives in the sea, but it has no gills."), ("Amphibians", "Amphibians have moist skin and lay eggs in water."), ("Reptiles", "Reptiles have dry scales.")]),
   twin=mc("u4n44_t", "M", "O5", "A starfish is…", "an invertebrate", [("a fish", ""), ("a mammal", ""), ("an amphibian", "")])),
 "u4n45p": dict(note="Paused before the key for eagle, shark, frog and bee is built.",
   q=mc("u4n45p_q", "H", "O6", "PREDICT: which first yes/no question would split eagle, shark, frog and bee into two groups?", ("Does it have a backbone?", "Good – only the bee has no backbone."),
        [("Is it dangerous?", "People would answer differently – not a clear feature."), ("Is it big?", "Size is not a clear yes/no feature."), ("Does it live on Earth?", "All four do, so it does not split them.")], skill="Prediction"),
   twin=mc("u4n45p_t", "M", "O6", "How many choices are there at each step of a dichotomous key?", "Two", [("Three", ""), ("One", ""), ("Four", "")])),
 "u4n45e": dict(note="Paused after the finished key.",
   q=ex("u4n45e_q", "H", "O6", "EXPLAIN why 'Has it got feathers?' is a better key question than 'Is it pretty?'.",
        [("feathers is a clear / visible feature everyone sees the same way", ["visible|see|clear|observ|same|everyone|fact"]), ("'pretty' is an opinion / people answer differently", ["opinion|different|depends|person|subjective"])],
        "Having feathers is a visible feature – everyone gets the same answer. Being pretty is an opinion, so different people would answer differently."),
   twin=mc("u4n45e_t", "H", "O6", "Which is the BEST key question?", "Does it have six legs?", [("Is it scary?", ""), ("Is it common?", ""), ("Do I like it?", "")])),
}

DROP = {
 "4.1": ["u4s1p01", "u4s1p16", "u4s1p06", "u4s1p15"],
 "4.2": ["u4s2p17", "u4s2p14", "u4s2p12"],
 "4.3": ["u4s3p09", "u4s3p05", "u4s3p11"],
 "4.4": ["u4s4p06", "u4s4p07", "u4s4p16"],
 "4.5": ["u4s5p07", "u4s5p02", "u4s5p18"],
}
YEAST = {"kind": "linegraph", "x": {"min": 0, "max": 60, "step": 10, "label": "Time (min)"}, "y": {"min": 0, "max": 40, "step": 10, "label": "Gas collected (cm³)"},
         "series": [{"pts": [[0, 0], [10, 4], [20, 11], [30, 19], [40, 26], [50, 32], [60, 36]], "label": "with sugar"}, {"pts": [[0, 0], [10, 0], [20, 1], [30, 1], [40, 1], [50, 2], [60, 2]], "label": "no sugar", "dash": True}]}
SPEC = {"kind": "barchart", "labels": ["insects", "plants", "fungi", "fish", "birds"], "values": [1000, 390, 150, 36, 11], "ymax": 1000, "step": 200, "ylabel": "Named species (thousands)", "xlabel": "Group"}
NEW_PRAC = {
 "4.1": [
  num("u4s1p21", "Use the graph. How much gas had the yeast WITH sugar made after 30 minutes?", 19, "cm³", "M", "O1", skill="Data", tol=1, units=["cm³", "cm3", "ml"], fig=YEAST, hint="Find 30 min, go up to the solid line."),
  mc("u4s1p22", "H", "O1", "Use the graph. What conclusion can you make?", "Yeast with sugar respires and makes gas; without sugar it makes almost none",
     [("Yeast makes gas without any food", "The 'no sugar' line stays almost at zero."), ("Sugar makes gas by itself", "Sugar alone does not respire – the yeast does."), ("Time has no effect on the gas made", "With sugar, the gas increases over time.")], fig=YEAST, skill="Data"),
  ex("u4s1p23", "H", "O1", "In the yeast experiment, name TWO variables that must be kept the same in both bottles.",
     [("amount / type of yeast", ["yeast"]), ("temperature", ["temperature|warm|35"]), ("volume of water / size of bottle / balloon / time", ["water|bottle|balloon|time|volume"])],
     "The amount of yeast and the temperature (also the volume of water, the bottle and the time).", need=2),
 ],
 "4.2": [
  od("u4s2p21", "M", "O2", "Put the steps of how a virus copies itself in order.", ["The virus attaches to a host cell", "It releases its genetic material inside", "The host cell makes many new viruses", "The new viruses burst out of the cell", "They infect other cells"]),
  nm("u4s2p22", "H", "O2", "A bacterium is 0.002 mm long. A virus is 0.0001 mm long. How many times longer is the bacterium?", 20, "times", units=["times", ""]),
  gd("u4s2p23", "H", "O2", "Which life processes does a virus particle show on its own, outside a host cell?", ["Yes", "No"],
     [("Respiration", ["✗", "✓"]), ("Nutrition", ["✗", "✓"]), ("Excretion", ["✗", "✓"]), ("Has genetic material", ["✓", "✗"])]),
 ],
 "4.3": [
  nm("u4s3p21", "H", "O3", "Use the bar chart. About how many more named species of insects are there than plants (in thousands)?", 610, "thousand", units=["thousand", ""], fig=SPEC, skill="Data", tol=10),
  od("u4s3p22", "M", "O3", "Put the groups in order from the biggest group to the smallest.", ["Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"]),
  gd("u4s3p23", "H", "O4", "Are these parents the same species?", ["Same species", "Different species"],
     [("Their offspring can have young of their own", ["✓", "✗"]), ("Their offspring are always infertile", ["✗", "✓"]), ("A horse and a donkey (mule offspring)", ["✗", "✓"]), ("A rooster and a hen", ["✓", "✗"])]),
 ],
 "4.4": [
  gd("u4s4p21", "H", "O5", "Use the features to classify each vertebrate.", ["Group"],
     [("Dry scales, lays leathery eggs on land", ["Reptile"]), ("Moist skin, lays jelly-coated eggs in water", ["Amphibian"]), ("Feathers, beak, hard-shelled eggs", ["Bird"]), ("Gills, fins, scales", ["Fish"]), ("Fur or hair, feeds young on milk", ["Mammal"])], extra=[]),
  mc("u4s4p22", "H", "O5", "A plant has seeds inside a fruit. Which group is it in?", "Flowering plants", [("Conifers", "Conifer seeds are in cones."), ("Ferns", "Ferns make spores, not seeds."), ("Mosses", "Mosses make spores, not seeds.")]),
  gd("u4s4p23", "H", "O5", "Insect or arachnid?", ["Group"], [("Six legs, three body sections", ["Insect"]), ("Eight legs, two body sections", ["Arachnid"]), ("Scorpion", ["Arachnid"]), ("Ant", ["Insect"])], extra=[]),
 ],
 "4.5": [
  mc("u4s5p21", "H", "O6", "Use the key. A leaf is simple (not split into leaflets) and has a smooth edge. Which tree is it?", "Mango",
     [("Neem", "Neem leaves are split into leaflets."), ("Hibiscus", "Hibiscus leaves have a toothed edge."), ("Tamarind", "Tamarind leaves are split into leaflets.")],
     data={"caption": "Key to four tree leaves", "head": ["Step", "Statement", "Go to / name"], "rows": [["1a", "leaf split into small leaflets", "2"], ["1b", "simple leaf", "3"], ["2a", "leaflets with toothed edges", "Neem"], ["2b", "leaflets with smooth edges", "Tamarind"], ["3a", "toothed edge", "Hibiscus"], ["3b", "smooth edge", "Mango"]]}, skill="Data"),
  mc("u4s5p22", "H", "O6", "Use the same key. A leaf is split into leaflets with smooth edges. Which tree is it?", "Tamarind",
     [("Neem", "Neem leaflets are toothed."), ("Mango", "Mango has a simple leaf."), ("Hibiscus", "Hibiscus has a simple leaf.")],
     data={"caption": "Key to four tree leaves", "head": ["Step", "Statement", "Go to / name"], "rows": [["1a", "leaf split into small leaflets", "2"], ["1b", "simple leaf", "3"], ["2a", "leaflets with toothed edges", "Neem"], ["2b", "leaflets with smooth edges", "Tamarind"], ["3a", "toothed edge", "Hibiscus"], ["3b", "smooth edge", "Mango"]]}, skill="Data"),
  nm("u4s5p23", "H", "O6", "A dichotomous key identifies 8 different beetles. What is the smallest number of questions (steps) the key can have?", 7, "questions", units=["questions", "steps", ""],
     hint="Each question splits one group into two; you need one fewer question than organisms."),
 ],
}

NEW_ADV = {
 "4.1": [adv(gd("u4s1a5", "VH", "O1", "Decide whether each thing is living, dead (was once living) or never living. Think about cells and the seven life processes.", ["Category"],
     [("A dry bean seed in a packet", ["Living"]), ("A wooden chair", ["Dead (once living)"]), ("A candle flame", ["Never living"]), ("Yeast in a bread packet", ["Living"]), ("A rock", ["Never living"])], extra=[], src=src("SRC-NSTALIV")))],
 "4.4": [adv(ex("u4s4a5", "VH", "O5", "A student says a moss, a fern and a mango tree are classified differently because of their size. Explain the real reason, using how each reproduces.",
     [("moss and fern make spores (no seeds)", ["spore"]), ("mango makes seeds inside fruits / flowers", ["seed.{0,20}fruit|fruit|flower"]), ("classification uses features such as how they reproduce, not size", ["not.{0,20}size|reproduc|feature"])],
     "Size is not the reason. Mosses and ferns reproduce with spores and make no seeds, while a mango is a flowering plant that makes seeds inside fruits. Plants are classified by features such as how they reproduce.", need=2, src=src("SRC-NSTALC")))],
}

from tests_stage7_unit04_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
