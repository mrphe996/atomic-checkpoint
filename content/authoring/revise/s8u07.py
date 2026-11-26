# -*- coding: utf-8 -*-
"""Stage 8 Unit 7 Exothermic and Endothermic Changes — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-ACSEXO", "name": "American Chemical Society – Exothermic, Endothermic, & Chemical Change (lab investigation)", "url": "https://highschoolenergy.acs.org/how-can-energy-change/exothermic-endothermic-chemical-change.html", "use": "Idea for the 'is a temperature change always a chemical reaction?' Challenge question (7.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u07n11p": dict(note="Paused before calcium chloride is stirred into water at 20 °C.",
   q=mc("s8u07n11p_q", "M", "O2", "PREDICT: what will happen to the temperature?", ("It will go up", "Good prediction – now watch."),
        [("It will go down", "Watch carefully."), ("It will stay the same", "Watch carefully."), ("It will drop to 0 °C", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u07n11p_t", "M", "O1", "'Exo' means…", "out", [("in", ""), ("heat", ""), ("cold", "")])),
 "s8u07n11e": dict(note="Paused after the temperature rose from 20 °C to 38 °C.",
   q=ex("s8u07n11e_q", "H", "O2", "EXPLAIN the result using the word exothermic.",
        [("heat is released / given out to the surroundings", ["releas|give.{0,10}out|to the surroundings|transferred out"]), ("so the temperature rises; it is exothermic", ["exothermic"])],
        "Dissolving calcium chloride releases heat to the surroundings (the water), so the temperature rises. It is an exothermic process."),
   twin=nm("s8u07n11e_t", "M", "O2", "By how many degrees did the temperature rise (20 °C to 38 °C)?", 18, "°C", tol=0, units=["°C"])),
 "s8u07n12p": dict(note="Paused before citric acid and baking soda are added to water at 20 °C.",
   q=mc("s8u07n12p_q", "M", "O3", "PREDICT: what will happen to the temperature?", ("It will go down", "Good prediction – now watch."),
        [("It will go up", "Watch carefully."), ("It will stay the same", "Watch carefully."), ("It will boil", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u07n12p_t", "M", "O3", "'Endo' means…", "in", [("out", ""), ("fast", ""), ("hot", "")])),
 "s8u07n12e": dict(note="Paused after the temperature fell from 20 °C to 14 °C.",
   q=ex("s8u07n12e_q", "H", "O3", "EXPLAIN the result using the word endothermic.",
        [("heat is taken in from the surroundings", ["taken in|absorb|take.{0,10}in|from the surroundings"]), ("so the temperature falls; it is endothermic", ["endothermic"])],
        "The reaction takes in heat from its surroundings, so the temperature of the water falls. It is an endothermic reaction."),
   twin=mc("s8u07n12e_t", "M", "O3", "Which gas makes the sherbet fizz?", "Carbon dioxide", [("Oxygen", ""), ("Hydrogen", ""), ("Nitrogen", "")])),
 "s8u07n13": dict(note="Paused on the chart: final temperatures 38, 27, 8 and 12 °C (all started at 20 °C).",
   q=gd("s8u07n13_q", "H", "O4", "Exothermic or endothermic?", ["Type"],
        [("Calcium chloride dissolving (38 °C)", ["Exothermic"]), ("Acid + alkali (27 °C)", ["Exothermic"]), ("Ice melting in a drink (8 °C)", ["Endothermic"]), ("Ammonium chloride dissolving (12 °C)", ["Endothermic"])], extra=[], skill="Data"),
   twin=nm("s8u07n13_t", "M", "O4", "By how many degrees did the temperature fall when ammonium chloride dissolved (20 °C to 12 °C)?", 8, "°C", tol=0, units=["°C"])),
}

DROP = {"7.1": ["s8u07s1p01", "s8u07s1p02", "s8u07s1p11"], "7.2": ["s8u07s2p01", "s8u07s2p10", "s8u07s2p11"]}

NEUT = {"kind": "linegraph", "x": {"min": 0, "max": 25, "step": 5, "label": "Volume of alkali added (cm³)"}, "y": {"min": 18, "max": 30, "step": 2, "label": "Temperature (°C)"},
        "series": [{"pts": [[0, 20], [5, 22.5], [10, 25], [15, 27.5], [20, 28], [25, 27]], "label": "acid + alkali"}]}
PACK = {"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 2, "label": "Time (min)"}, "y": {"min": 0, "max": 25, "step": 5, "label": "Temperature (°C)"},
        "series": [{"pts": [[0, 20], [1, 8], [2, 5], [4, 6], [6, 9], [8, 12], [10, 15]], "label": "cold pack"}]}
NEW_PRAC = {
 "7.1": [
  nm("s8u07s1p21", "M", "O2", "Alkali is added to acid in a polystyrene cup. Use the graph. What is the highest temperature?", 28, "°C", tol=0.3, units=["°C"], fig=NEUT, skill="Data"),
  ex("s8u07s1p22", "H", "O2", "Use the graph. Explain why the temperature rises and then starts to fall after 20 cm³.",
     [("neutralisation is exothermic: heat released while acid and alkali react", ["exothermic|releas|react"]), ("after 20 cm³ the acid is used up / reaction stops, and cooler alkali (or heat loss) lowers the temperature", ["used up|neutralised|stops|no more|cool|heat (lost|loss)"])],
     "Neutralisation is exothermic, so heat is released as the acid reacts with the alkali. After about 20 cm³ all the acid has reacted, so no more heat is released, and the extra cool alkali (and heat loss to the air) makes the temperature fall.", fig=NEUT),
  mc("s8u07s1p23", "H", "O2", "Why is a polystyrene cup used for this experiment rather than a glass beaker?", "Polystyrene is a good insulator, so less heat is lost", [("Polystyrene reacts with the acid", "It does not react."), ("Glass is too heavy", "Mass is not the issue."), ("Polystyrene conducts heat well", "It is an insulator.")]),
 ],
 "7.2": [
  nm("s8u07s2p21", "M", "O4", "A cold pack is squeezed at 0 min. Use the graph. What is its lowest temperature?", 5, "°C", tol=0.3, units=["°C"], fig=PACK, skill="Data"),
  ex("s8u07s2p22", "H", "O4", "Use the graph. Explain why the cold pack slowly warms up again after 2 minutes.",
     [("the endothermic dissolving has finished / stopped", ["finish|stop|complete|no more|used up"]), ("heat is transferred from the warmer surroundings into the pack", ["surround|warmer|air|absorb|transfer"])],
     "Once the endothermic dissolving has finished, no more heat is taken in, and heat flows into the cold pack from the warmer surroundings, so it warms up.", fig=PACK),
  gd("s8u07s2p23", "H", "O3", "Exothermic or endothermic?", ["Type"],
     [("Burning wood", ["Exothermic"]), ("Photosynthesis", ["Endothermic"]), ("Water freezing", ["Exothermic"]), ("Sweat evaporating", ["Endothermic"])], extra=[]),
 ],
}
NEW_ADV = {
 "7.2": [adv(ex("s8u07s2a05", "VH", "O4", "A student says: 'Dissolving ammonium chloride made the water cold, so it must be a chemical reaction.' Evaluate this claim.",
     [("a temperature change alone does not prove a chemical reaction", ["not (always|necessarily|enough)|alone|doesn't prove|does not prove|physical (changes|processes) also"]), ("dissolving / melting are physical changes that can be endothermic", ["dissolv|physical|melt|no new substance"]), ("evidence of a reaction needs a new substance (e.g. gas, precipitate)", ["new substance|gas|precipitate|colour"])],
     "The claim is wrong. Physical changes such as dissolving and melting can also take in or give out heat. Dissolving ammonium chloride is an endothermic physical process: no new substance is made, so a temperature change on its own does not prove a chemical reaction.", need=2, src=src("SRC-ACSEXO")))],
}

from tests_stage8_unit07_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
