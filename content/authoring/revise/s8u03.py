# -*- coding: utf-8 -*-
"""Stage 8 Unit 3 Ecosystems — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-KEWMSB", "name": "Royal Botanic Gardens, Kew – Freezing seeds for the future (Millennium Seed Bank)", "url": "https://kew.org/read-and-watch/seed-collecting-msb", "use": "Seeds are dried, sealed and stored at −20 °C; over 2.4 billion seeds banked (Challenge question, 3.1)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u03n11p": dict(note="Paused before 12 woodlice are left in a choice chamber (dry and light / damp and dark).",
   q=mc("s8u03n11p_q", "M", "O2", "PREDICT: where will most woodlice be after ten minutes?", ("On the damp, dark side", "Good prediction – now watch."),
        [("On the dry, light side", "Watch carefully."), ("Evenly spread", "Watch carefully."), ("They will not move", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u03n11p_t", "M", "O1", "A habitat is…", "the place where an organism lives", [("a group of one species", ""), ("a food chain", ""), ("a type of adaptation", "")])),
 "s8u03n11e": dict(note="Paused after 10 woodlice were on the damp, dark side.",
   q=ex("s8u03n11e_q", "H", "O2", "EXPLAIN why the woodlice moved to the damp, dark side.",
        [("they lose water easily / dry out in dry places", ["water|dry out|dehydrat|moist|damp"]), ("dark places hide them from predators", ["predator|hide|dark"])],
        "Woodlice lose water easily, so they survive best in damp places, and moving into the dark helps them hide from predators. This behaviour is an adaptation."),
   twin=mc("s8u03n11e_t", "H", "O2", "Moving away from light is an example of a…", "behavioural adaptation", [("physical adaptation", ""), ("population", ""), ("community", "")])),
 "s8u03n12": dict(note="Paused on the chart: daisies per quadrat – full sun 14, part shade 8, under trees 2.",
   q=ex("s8u03n12_q", "H", "O1", "Which non-living factor most likely affects where daisies grow, and why use many random quadrats?",
        [("light (for photosynthesis)", ["light|sun|shade"]), ("many random quadrats make the results fair / reliable / representative", ["fair|reliab|represent|bias|random|accurate|typical"])],
        "Light: daisies need plenty of light for photosynthesis. Using many quadrats placed at random gives a fairer, more reliable picture of the whole area."),
   twin=nm("s8u03n12_t", "M", "O1", "Five quadrats in full sun had 12, 15, 14, 13 and 16 daisies. What is the mean?", 14, "daisies", tol=0, units=["daisies", ""])),
 "s8u03n13p": dict(note="Paused before two jars of pond water (one with fertiliser) are left in sunlight.",
   q=mc("s8u03n13p_q", "M", "O4", "PREDICT: what will happen to the jar with fertiliser?", ("It will turn green with algae", "Good prediction – now watch."),
        [("Nothing will change", "Watch carefully."), ("It will become clearer", "Watch carefully."), ("It will boil", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u03n13p_t", "M", "O4", "Fertilisers contain…", "nutrients that help plants grow", [("poison for algae", ""), ("oxygen for fish", ""), ("plastic", "")])),
 "s8u03n13e": dict(note="Paused after the fertiliser jar turned bright green.",
   q=od("s8u03n13e_q", "H", "O4", "EXPLAIN the effect on a lake: put the events in order.", ["fertiliser washes into the lake", "algae grow very fast", "algae block light and then die", "bacteria decompose them and use up oxygen", "fish die"]),
   twin=mc("s8u03n13e_t", "H", "O4", "Why do fish die after an algal bloom?", "Bacteria decomposing the algae use up the oxygen", [("The algae eat the fish", ""), ("The water gets too cold", ""), ("Fertiliser is food for fish", "")])),
 "s8u03n14": dict(note="Paused on the chart: mercury plankton 0.04, small fish 0.3, large fish 1.5, bird 12 ppm.",
   q=ex("s8u03n14_q", "H", "O4", "Why does the top predator have so much more mercury than the plankton?",
        [("mercury is not broken down or excreted / stays in the body", ["not (broken|excreted)|stays|builds up|accumulat|stored"]), ("each animal eats many of the organisms below it", ["eats many|many|lots"])],
        "Mercury is not broken down or excreted, so it stays in the body. Each animal eats many of the organisms below it, so the mercury builds up at each step: biomagnification."),
   twin=nm("s8u03n14_t", "H", "O4", "How many times more mercury does the bird (12 ppm) have than a large fish (1.5 ppm)?", 8, "", tol=0, units=["", "times"])),
}

DROP = {"3.1": ["s8u03s1p01", "s8u03s1p08", "s8u03s1p14"], "3.2": ["s8u03s2p01", "s8u03s2p04", "s8u03s2p15"]}

PREY = {"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 2, "label": "Year"}, "y": {"min": 0, "max": 100, "step": 20, "label": "Number of animals"},
        "series": [{"pts": [[0, 60], [2, 80], [4, 50], [6, 30], [8, 55], [10, 75]], "label": "rabbits"}, {"pts": [[0, 10], [2, 14], [4, 22], [6, 15], [8, 9], [10, 12]], "label": "foxes", "dash": True}]}
FISH = {"kind": "barchart", "labels": ["1970", "1990", "2010", "2020"], "values": [90, 60, 35, 40], "ymax": 100, "step": 20, "ylabel": "Fish caught per day (index)", "xlabel": "Year"}
NEW_PRAC = {
 "3.1": [
  mc("s8u03s1p21", "M", "O1", "Use the graph. What happened to the fox population after the rabbits increased?", "It increased", [("It decreased", "Look at year 2 to year 4."), ("It stayed the same", "The dashed line rises."), ("It disappeared", "Foxes are still present.")], fig=PREY, skill="Data"),
  ex("s8u03s1p22", "H", "O1", "Use the graph. Explain why the rabbit population fell between years 2 and 6.",
     [("fox numbers increased / more predators", ["fox|predator"]), ("more rabbits were eaten", ["eaten|eat|hunt|prey"])],
     "The fox population increased, so more rabbits were eaten and the rabbit population fell.", fig=PREY),
  gd("s8u03s1p23", "H", "O2", "Physical or behavioural adaptation?", ["Type"],
     [("A polar bear's thick fur", ["Physical"]), ("Birds migrating south in winter", ["Behavioural"]), ("A cactus's spines instead of leaves", ["Physical"]), ("Dolphins hunting in pods", ["Behavioural"])], extra=[]),
 ],
 "3.2": [
  mc("s8u03s2p21", "M", "O3", "Use the bar chart. How did the fish catch change from 1970 to 2010?", "It fell by more than half", [("It doubled", "The bars get shorter."), ("It stayed the same", "The bars change."), ("It rose slightly", "It fell.")], fig=FISH, skill="Data"),
  ex("s8u03s2p22", "H", "O3", "Use the bar chart. Suggest a reason for the fall, and a reason the catch rose slightly by 2020.",
     [("overfishing removed too many fish", ["overfish|too many|caught too"]), ("fishing limits / protected areas / fewer boats let numbers recover", ["limit|quota|protect|ban|recover|rule|fewer"])],
     "Overfishing removed fish faster than they could reproduce, so catches fell. Fishing limits or protected areas may have let numbers recover a little by 2020.", fig=FISH),
  mt("s8u03s2p23", "H", "O3", "Match each human impact to its example.", [("Deforestation", "forest cleared for farms"), ("Invasive species", "Nile perch in Lake Victoria"), ("Overexploitation", "too many fish caught"), ("Pollution", "oil spill at sea")]),
 ],
}
NEW_ADV = {
 "3.1": [adv(ex("s8u03s1a05", "VH", "O1", "Kew's Millennium Seed Bank dries seeds, seals them in containers and stores them at −20 °C. Explain why each of these steps helps the seeds survive for many years, and why seed banks matter.",
     [("drying / low humidity stops germination and decay", ["dry|humid|moisture|germinat|mould|decay"]), ("cold slows down the reactions / ageing in the seed", ["cold|−20|-20|slow"]), ("protects plant species from extinction / for future replanting", ["extinct|future|replant|biodivers|conserv|threat"])],
     "Drying the seeds and keeping humidity low stops them germinating or rotting; the cold slows down the chemical reactions inside so they age very slowly. Seed banks keep species safe from extinction so they can be grown again in the future.", need=2, src=src("SRC-KEWMSB")))],
}

from tests_stage8_unit03_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
