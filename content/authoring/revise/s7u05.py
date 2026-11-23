# -*- coding: utf-8 -*-
"""Stage 7 Unit 5 Food Chains and Food Webs — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-AAAS", "name": "AAAS Project 2061 Science Assessment – items on matter and energy in living systems", "url": "https://assess.bscs.org/science/pages/faq", "use": "Idea for the food-web Challenge question about what happens when a species is removed (5.2)."},
]
src = lambda k: {"id": k, "name": SOURCES[0]["name"], "url": SOURCES[0]["url"]}

NEW_STOPS = {
 "u5n51p": dict(note="Paused before the three bread slices are left for five days.",
   q=mc("u5n51p_q", "M", "O1", "PREDICT: which slice will grow the most mould?", ("A – damp and warm", "Good prediction – now watch."),
        [("B – damp, in the fridge", "Cold slows microorganisms down."), ("C – dry and warm", "Think about what mould needs to grow."), ("All the same", "The conditions are different.")], skill="Prediction"),
   twin=mc("u5n51p_t", "M", "O1", "Mould on bread is a kind of…", "fungus", [("bacterium", ""), ("virus", ""), ("plant", "")])),
 "u5n51e": dict(note="Paused after the result: A lots of mould, B a little, C none.",
   q=ex("u5n51e_q", "H", "O1", "EXPLAIN the results, and say how this helps us keep food fresh.",
        [("mould grows best when warm and moist", ["warm|moist|damp|wet"]), ("cold slows it / no water stops it", ["cold|fridge|slow|dry|no water"]), ("so keep food cold / dry it", ["fridge|cold|dry|freez"])],
        "Mould grows fastest in warm, moist conditions. Cold slows it down and without water it cannot grow, so we keep food in a fridge or dry it.", need=2),
   twin=mc("u5n51e_t", "H", "O1", "Why does a fridge keep milk fresh for longer?", "The cold slows down the growth of microorganisms", [("The cold kills all microorganisms", ""), ("The light in the fridge stops mould", ""), ("Milk cannot go bad", "")])),
 "u5n52": dict(note="Paused after the rice-field food chain: rice → grasshopper → frog → heron.",
   q=mc("u5n52_q", "H", "O4", "A farmer kills all the frogs with poison. What will probably happen to the rice plants?", ("They will be eaten more, because grasshoppers increase", "Yes – with no frogs, grasshoppers increase and eat more rice."),
        [("They will grow better, because there are fewer frogs", "Frogs do not eat rice."), ("Nothing will change", "Food chains are linked – a change spreads."), ("The herons will eat the rice", "Herons do not eat rice.")]),
   twin=mc("u5n52_t", "M", "O3", "In rice → grasshopper → frog → heron, which is the secondary consumer?", "Frog", [("Grasshopper", ""), ("Heron", ""), ("Rice", "")])),
 "u5n53p": dict(note="Paused on the food web before the frogs are removed.",
   q=mc("u5n53p_q", "H", "O4", "PREDICT: if all the frogs die, what happens to the grasshoppers?", ("They increase", "Good prediction – now watch."),
        [("They decrease", "Frogs eat grasshoppers – think what happens with fewer predators."), ("They stay the same", "Removing a predator affects its prey."), ("They become eagles' only food", "Eagles do not eat grasshoppers in this web.")], skill="Prediction"),
   twin=mc("u5n53p_t", "M", "O4", "In the web, which animal eats frogs?", "Eagle", [("Owl", ""), ("Rabbit", ""), ("Mouse", "")])),
 "u5n53e": dict(note="Paused after the web changes: grasshoppers up, grass down, eagles eat more rabbits.",
   q=ex("u5n53e_q", "H", "O4", "EXPLAIN why removing the frogs also affects the rabbits.",
        [("eagles have no frogs so eat more rabbits", ["eagle.{0,40}(more|rabbit)|more rabbit"]), ("more grasshoppers eat more grass, less grass for rabbits", ["grass|food"])],
        "Without frogs, eagles eat more rabbits. Also more grasshoppers eat more grass, so there is less food for the rabbits. Changes ripple through the web."),
   twin=mc("u5n53e_t", "H", "O4", "Why are food webs a better model than a single food chain?", "Most animals eat, and are eaten by, more than one kind of organism", [("Food chains are too long", ""), ("Webs leave out producers", ""), ("Animals only eat one thing", "")])),
}

DROP = {"5.1": ["u5s1p01", "u5s1p16", "u5s1p05"], "5.2": ["u5s2p02", "u5s2p04", "u5s2p06"]}
LEAVES = {"kind": "linegraph", "x": {"min": 0, "max": 9, "step": 1, "label": "Time (months)"}, "y": {"min": 0, "max": 80, "step": 20, "label": "Mass lost (%)"},
          "series": [{"pts": [[0, 0], [1, 20], [3, 45], [6, 61], [9, 70]]}]}
MOULD = {"kind": "barchart", "labels": ["4 °C", "15 °C", "25 °C", "35 °C"], "values": [5, 30, 70, 85], "ymax": 100, "step": 20, "ylabel": "Bread covered by mould after 5 days (%)", "xlabel": "Temperature"}
WEB = {"caption": "What eats what in a pond", "head": ["Organism", "Eats"], "rows": [["water plants", "– (producer)"], ["water snail", "water plants"], ["mayfly larva", "water plants"], ["small fish", "water snail, mayfly larva"], ["kingfisher", "small fish"], ["frog", "mayfly larva"]]}
NEW_PRAC = {
 "5.1": [
  num("u5s1p21", "Use the graph. What percentage of their mass had the leaves lost after 3 months?", 45, "%", "M", "O2", skill="Data", tol=2, units=["%"], fig=LEAVES),
  mc("u5s1p22", "H", "O2", "Use the graph. How does the rate of decomposition change over the nine months?", "It is fastest at the start, then slows down",
     [("It speeds up over time", "The line gets less steep, not steeper."), ("It stays the same all the time", "The slope changes."), ("It stops after one month", "Mass keeps being lost.")], fig=LEAVES, skill="Data"),
  num("u5s1p23", "Use the bar chart. How much more of the bread was covered at 25 °C than at 4 °C?", 65, "%", "M", "O1", skill="Data", tol=1, units=["%"], fig=MOULD),
  ex("u5s1p24", "H", "O1", "Use the bar chart to describe how temperature affects mould growth, and explain the pattern.",
     [("more mould at higher temperature", ["more|increas|higher|warmer"]), ("microorganisms grow / respire faster when warm", ["faster|quick|warm|grow|respir|active"])],
     "The higher the temperature, the more mould grew. Microorganisms grow and reproduce faster when it is warm.", fig=MOULD),
 ],
 "5.2": [
  mc("u5s2p21", "M", "O3", "Use the table. Which organism is the producer?", "Water plants", [("Water snail", "It eats water plants."), ("Small fish", "It eats other animals."), ("Kingfisher", "It eats fish.")], data=WEB, skill="Data"),
  gd("u5s2p22", "H", "O3", "Use the table. Give the role of each organism.", ["Role"],
     [("Water snail", ["Primary consumer"]), ("Small fish", ["Secondary consumer"]), ("Kingfisher", ["Tertiary consumer"]), ("Water plants", ["Producer"])], extra=[], data=WEB),
  mc("u5s2p23", "H", "O4", "Use the table. If the small fish all died, which animal would lose its only food?", "Kingfisher",
     [("Frog", "Frogs eat mayfly larvae."), ("Water snail", "Snails eat water plants."), ("Mayfly larva", "Larvae eat water plants.")], data=WEB, skill="Data"),
  od("u5s2p24", "M", "O3", "Build the food chain from the table, starting with the producer.", ["water plants", "water snail", "small fish", "kingfisher"], data=WEB),
 ],
}
NEW_ADV = {
 "5.2": [adv(ex("u5s2a5", "VH", "O4", "In a grassland web, grass is eaten by rabbits and grasshoppers; rabbits are eaten by foxes and eagles; grasshoppers are eaten by birds; birds are eaten by eagles. A disease kills most rabbits. Predict and explain the effect on the foxes AND on the grasshoppers.",
     [("foxes decrease / have less food", ["fox.{0,40}(decreas|less|fewer|die|starv|hungry)"]), ("eagles eat more birds", ["eagle.{0,40}(bird|more)"]), ("so fewer birds and grasshoppers increase (also more grass)", ["grasshopper.{0,40}(increas|more)|more grasshopper|more grass"])],
     "Foxes have less food, so their numbers fall. Eagles eat more birds instead, so there are fewer birds to eat grasshoppers; with more grass left uneaten, the grasshoppers increase.", need=2, src=src("SRC-AAAS")))],
}

from tests_stage7_unit05_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
