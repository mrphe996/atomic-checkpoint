# -*- coding: utf-8 -*-
"""Stage 9 Unit 7 Salts — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-RSCSALT", "name": "Royal Society of Chemistry – Preparing salts by neutralisation of oxides and carbonates (class practical)", "url": "https://edu.rsc.org/resources/preparing-salts-by-neutralisation-of-oxides-and-carbonates/1762.article", "use": "Planning the preparation of magnesium sulfate crystals: Challenge question (7.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s9u07n11p": dict(note="Paused before a neutral solution of hydrochloric acid and sodium hydroxide is evaporated.",
   q=mc("s9u07n11p_q", "M", "O2", "PREDICT: what will be left in the evaporating dish?", ("White crystals of a salt", "Good prediction – now watch."),
        [("Nothing at all", "Watch carefully."), ("Drops of acid", "Watch carefully."), ("Solid sodium hydroxide", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u07n11p_t", "M", "O1", "Acid + base →", "salt + water", [("salt + hydrogen", ""), ("acid + water", ""), ("base + carbon dioxide", "")])),
 "s9u07n11e": dict(note="Paused after white crystals of sodium chloride were left.",
   q=ex("s9u07n11e_q", "H", "O2", "EXPLAIN where the crystals came from and name them.",
        [("the acid and alkali reacted to form a salt and water (neutralisation)", ["salt and water|neutralis|react"]), ("sodium chloride: water evaporated, leaving the salt", ["sodium chloride"])],
        "The hydrochloric acid and sodium hydroxide reacted to form sodium chloride and water. When the water evaporated, the sodium chloride was left as crystals."),
   twin=gd("s9u07n11e_t", "H", "O2", "Which part of the salt name comes from each reactant?", ["Comes from"],
        [("sodium", ["the alkali (sodium hydroxide)"]), ("chloride", ["the acid (hydrochloric acid)"])], extra=["the water"])),
 "s9u07n21p": dict(note="Paused before the gases from magnesium + acid and marble + acid are tested.",
   q=mc("s9u07n21p_q", "M", "O3", "PREDICT: is the same gas made in both tubes?", ("No: two different gases", "Good prediction – now watch."),
        [("Yes: both make hydrogen", "Watch carefully."), ("Yes: both make carbon dioxide", "Watch carefully."), ("Yes: both make oxygen", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u07n21p_t", "M", "O3", "Marble chips are mainly…", "calcium carbonate", [("calcium chloride", ""), ("magnesium oxide", ""), ("sodium chloride", "")])),
 "s9u07n21e": dict(note="Paused after a squeaky pop (magnesium) and milky limewater (marble).",
   q=gd("s9u07n21e_q", "H", "O3", "Complete for each reaction.", ["Gas"],
        [("Magnesium + hydrochloric acid", ["Hydrogen"]), ("Calcium carbonate + hydrochloric acid", ["Carbon dioxide"])], extra=["Oxygen", "Chlorine"]),
   twin=mc("s9u07n21e_t", "H", "O3", "Name the salt made from magnesium and hydrochloric acid.", "Magnesium chloride", [("Magnesium sulfate", ""), ("Magnesium carbonate", ""), ("Hydrogen chloride", "")])),
}

DROP = {"7.1": ["s9u07s1p09", "s9u07s1p13", "s9u07s1p08"], "7.2": ["s9u07s2p03", "s9u07s2p04", "s9u07s2p09"]}

GAS = {"kind": "linegraph", "x": {"min": 0, "max": 5, "step": 1, "label": "Time (min)"}, "y": {"min": 0, "max": 60, "step": 10, "label": "Volume of gas (cm³)"},
       "series": [{"pts": [[0, 0], [1, 22], [2, 38], [3, 48], [4, 52], [5, 52]], "label": "marble chips + acid"}]}
NEW_PRAC = {
 "7.1": [
  gd("s9u07s1p21", "H", "O2", "Name the salt made.", ["Salt"],
     [("Sulfuric acid + sodium hydroxide", ["Sodium sulfate"]), ("Nitric acid + potassium hydroxide", ["Potassium nitrate"]), ("Hydrochloric acid + copper oxide", ["Copper chloride"])], extra=["Copper sulfate", "Sodium chloride"]),
  ex("s9u07s1p22", "H", "O1", "Explain what a salt is, using the idea of hydrogen ions.",
     [("acids contain hydrogen ions", ["hydrogen ion"]), ("in a salt the hydrogen ions are replaced by metal (or ammonium) ions", ["replac.{0,30}(metal|ammonium)"])],
     "All acids contain hydrogen ions. A salt is the ionic compound formed when the hydrogen ions of an acid are replaced by metal ions (or ammonium ions)."),
 ],
 "7.2": [
  nm("s9u07s2p21", "M", "O3", "Use the graph. What volume of gas had been made after 2 minutes?", 38, "cm³", tol=1, units=["cm³", "cm3"], fig=GAS, skill="Data"),
  ex("s9u07s2p22", "H", "O3", "Use the graph. Explain why no more gas is made after 4 minutes.",
     [("the reaction has stopped", ["stop|finish|complete|ended"]), ("one reactant (the acid or the marble) has been used up", ["used up|run out|no more acid|all the acid|reactant"])],
     "The reaction has finished because one of the reactants, the acid or the marble chips, has been used up, so no more carbon dioxide is made.", fig=GAS, skill="Data"),
  od("s9u07s2p23", "M", "O4", "Put the steps for making copper sulfate crystals in order.", ["Warm dilute sulfuric acid", "Add copper carbonate until it stops fizzing and some is left over", "Filter off the excess copper carbonate", "Heat the filtrate gently to make it saturated", "Leave to cool and crystallise"]),
 ],
}
NEW_ADV = {
 "7.2": [adv(ex("s9u07s2a05", "VH", "O4", "The RSC class practical makes magnesium sulfate (Epsom salt) from magnesium carbonate and dilute sulfuric acid. Write the word equation and explain why the magnesium carbonate is added in excess and why the mixture is filtered before evaporating.",
     [("magnesium carbonate + sulfuric acid → magnesium sulfate + water + carbon dioxide", ["magnesium sulfate.{0,30}water.{0,30}carbon dioxide|magnesium sulfate \\+ water \\+ carbon dioxide"]), ("excess makes sure all the acid reacts (no acid left in the salt)", ["all the acid|no acid left|acid is used up|react completely"]), ("filtering removes the unreacted solid carbonate, so the crystals are pure", ["remov.{0,30}(excess|unreacted|solid)|pure"])],
     "Magnesium carbonate + sulfuric acid → magnesium sulfate + water + carbon dioxide. The carbonate is added in excess so that all the acid reacts and no acid is left in the product. The mixture is filtered to remove the unreacted solid magnesium carbonate, so that only magnesium sulfate solution is evaporated and the crystals are pure.", need=2, src=src("SRC-RSCSALT")))],
}

from tests_stage9_unit07_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
