# -*- coding: utf-8 -*-
"""Stage 9 Unit 4 The Structure of the Atom and the Periodic Table — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-RSCPT", "name": "Royal Society of Chemistry – Periodic Table (element data, e.g. caesium)", "url": "https://periodic-table.rsc.org/element/55/Caesium", "use": "Group 1 melting points for the video chart and the Challenge question (4.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

MP = {"kind": "barchart", "labels": ["Li", "Na", "K", "Rb", "Cs"], "values": [181, 98, 64, 39, 28.5], "ymax": 200, "step": 40, "ylabel": "Melting point (°C)"}

NEW_STOPS = {
 "s9u04n11": dict(note="Paused after four elements and their uses: helium, lithium, silicon and hydrogen.",
   q=gd("s9u04n11_q", "H", "O1", "Which property makes each element useful?", ["Property"],
        [("Helium in balloons", ["Less dense than air and unreactive"]), ("Lithium in batteries", ["Lightest metal; loses its outer electron easily"]), ("Hydrogen as a fuel", ["Burns to make only water"])], extra=["Conducts heat very well"]),
   twin=mc("s9u04n11_t", "M", "O1", "Hydrogen is called a clean fuel because…", "it burns to make only water", [("it makes carbon dioxide", ""), ("it is a solid", ""), ("it is found in coal", "")])),
 "s9u04n21p": dict(note="Paused before lithium, sodium and potassium are dropped into water.",
   q=mc("s9u04n21p_q", "M", "O4", "PREDICT: which metal will react most violently with water?", ("Potassium", "Good prediction – now watch."),
        [("Lithium", "Watch carefully."), ("Sodium", "Watch carefully."), ("All the same", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u04n21p_t", "M", "O4", "Lithium, sodium and potassium all have … electron(s) in their outer shell.", "1", [("2", ""), ("7", ""), ("8", "")])),
 "s9u04n21e": dict(note="Paused after lithium fizzed gently, sodium whizzed around and potassium burst into a lilac flame.",
   q=ex("s9u04n21e_q", "H", "O4", "EXPLAIN why potassium reacts more violently than lithium.",
        [("potassium atoms are bigger / outer electron further from the nucleus", ["bigger|larger|further|more shells"]), ("so the outer electron is held less strongly and lost more easily", ["less strongly|weaker|lost more easily|easier to lose|more easily"])],
        "A potassium atom is bigger than a lithium atom, so its single outer electron is further from the nucleus and held less strongly. It is lost more easily, so potassium reacts more violently."),
   twin=mc("s9u04n21e_t", "M", "O4", "The gas given off when an alkali metal reacts with water is…", "hydrogen", [("oxygen", ""), ("carbon dioxide", ""), ("chlorine", "")])),
 "s9u04n22": dict(note="Paused on the chart: Li 181, Na 98, K 64, Rb 39, Cs 28.5 °C.",
   q=ex("s9u04n22_q", "H", "O4", "Describe the trend in melting point down Group 1 and predict the melting point of francium.",
        [("melting point decreases down the group", ["decreas|lower|falls|goes down"]), ("francium below about 28 °C (e.g. about 20–27 °C)", ["2[0-7]|below 28|less than 28|lower than (caesium|28)"])],
        "The melting point decreases down Group 1, from 181 °C for lithium to 28.5 °C for caesium. Francium, further down, should melt below 28 °C, perhaps around 20–27 °C.", skill="Data"),
   twin=nm("s9u04n22_t", "M", "O4", "Use the chart. What is the difference between the melting points of lithium and sodium?", 83, "°C", tol=0, units=["°C"], fig=MP)),
}

DROP = {"4.1": ["s9u04s1p01", "s9u04s1p11", "s9u04s1p12"], "4.2": ["s9u04s2p01", "s9u04s2p02", "s9u04s2p05"]}

ATOM = {"kind": "barchart", "labels": ["protons", "neutrons", "electrons"], "values": [11, 12, 11], "ymax": 14, "step": 2, "ylabel": "Number in one atom of element X"}
DEN = {"kind": "barchart", "labels": ["Li", "Na", "K"], "values": [0.53, 0.97, 0.86], "ymax": 1.2, "step": 0.2, "ylabel": "Density (g/cm³)"}
NEW_PRAC = {
 "4.1": [
  nm("s9u04s1p21", "M", "O1", "Use the chart. What is the mass number of element X?", 23, "", tol=0, units=[""], fig=ATOM, skill="Data"),
  mc("s9u04s1p22", "H", "O2", "Use the chart. What is the electronic structure of element X?", "2, 8, 1", [("2, 8, 2", "11 electrons in total."), ("2, 9", "The second shell holds up to 8."), ("8, 2, 1", "The first shell fills first.")], fig=ATOM, skill="Data"),
  gd("s9u04s1p23", "H", "O2", "Write the electronic structure.", ["Structure"],
     [("Oxygen (8 electrons)", ["2, 6"]), ("Aluminium (13 electrons)", ["2, 8, 3"]), ("Argon (18 electrons)", ["2, 8, 8"])], extra=["2, 8, 4", "2, 7"]),
 ],
 "4.2": [
  ex("s9u04s2p21", "H", "O3", "Use the chart. Explain why lithium, sodium and potassium all float on water.",
     [("their densities are less than 1 g/cm³", ["less than 1|below 1|0\\.5|0\\.9|0\\.8"]), ("water has a density of 1 g/cm³, so less dense objects float", ["water.{0,20}1|less dense|lower density"])],
     "Their densities (0.53, 0.97 and 0.86 g/cm³) are all less than water's density of 1 g/cm³, so they float.", fig=DEN, skill="Data"),
  mc("s9u04s2p22", "M", "O3", "Elements in the same period have the same number of…", "occupied electron shells", [("outer electrons", "That is the group."), ("neutrons", "Not related."), ("protons", "Each element has its own number.")]),
  od("s9u04s2p23", "H", "O4", "Order these Group 1 metals by reactivity, least reactive first.", ["lithium", "sodium", "potassium", "rubidium"]),
 ],
}
NEW_ADV = {
 "4.2": [adv(ex("s9u04s2a05", "VH", "O4", "The RSC Periodic Table gives caesium's melting point as 28.5 °C. Explain why caesium can melt in your hand, and why it is far too dangerous to hold.",
     [("body / hand temperature (about 37 °C) is above 28.5 °C", ["37|body temperature|hand.{0,20}(warmer|hotter)|above 28"]), ("caesium is the most reactive Group 1 metal shown: it loses its outer electron very easily", ["reactive|loses|outer electron"]), ("it reacts explosively with water (e.g. moisture on skin), making hydrogen and an alkali / heat", ["water|moisture|sweat|explos|hydrogen|alkali|burn"])],
     "Your hand is at about 37 °C, which is above caesium's melting point of 28.5 °C, so it would melt. But caesium is very far down Group 1: its single outer electron is very easily lost, so it reacts explosively with the moisture on your skin, producing hydrogen, heat and a strong alkali that would cause serious burns.", need=2, src=src("SRC-RSCPT")))],
}

from tests_stage9_unit04_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
