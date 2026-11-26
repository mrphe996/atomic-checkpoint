# -*- coding: utf-8 -*-
"""Stage 7 Unit 6 Materials and Their Structure — 2026 revision (written by the Camday teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-RSCPART", "name": "Royal Society of Chemistry – Particle models (Education in Chemistry / Learn Chemistry teaching resources)", "url": "https://edu.rsc.org/", "use": "Idea for the particle-diagram Challenge question (6.1)."},
    {"id": "SRC-AAAS", "name": "AAAS Project 2061 Science Assessment – substances, chemical reactions and conservation of matter", "url": "https://assess.bscs.org/science/pages/faq", "use": "Idea for the conservation-of-mass Challenge question (6.5)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

def P(pr, right, wrongs, obj, note, twin, hint="", skill="Prediction", d="M"):
    return dict(note=note, q=mc(pr[0], d, obj, pr[1], right, wrongs, hint=hint, skill=skill), twin=twin)

NEW_STOPS = {
 "u6n61p": P(("u6n61p_q", "PREDICT: which sealed syringe can be squashed into a smaller volume?"), ("The one with air", "Good prediction – now watch."),
            [("The one with water", "Watch carefully."), ("The one with packed sand", "Watch carefully."), ("All three equally", "Watch – they behave differently.")], "O2",
            "Paused before the plungers are pushed: air, water, packed sand.",
            mc("u6n61p_t", "M", "O1", "Which state of matter can be compressed?", "Gas", [("Solid", ""), ("Liquid", ""), ("None", "")])),
 "u6n61e": dict(note="Paused after the air was squashed and the water and sand were not.",
   q=ex("u6n61e_q", "H", "O2", "EXPLAIN, using particles, why the air could be squashed but the water could not.",
        [("gas particles far apart / empty space between them", ["far apart|space|gap|spread"]), ("liquid particles touching / close together", ["touch|close|packed|no space|no gap"])],
        "In air (a gas) the particles are far apart with empty space between them, so they can be pushed closer. In water (a liquid) the particles are already touching, so there is no space to squash them into."),
   twin=mc("u6n61e_t", "H", "O2", "Why are car brakes filled with a liquid rather than air?", "A liquid cannot be compressed, so the push is passed on straight away", [("Air is too heavy", ""), ("Liquids are cheaper", ""), ("Air would freeze", "")])),
 "u6n62p": P(("u6n62p_q", "PREDICT: what will appear on the outside of an ice-cold can left in a warm room?"), ("Drops of water", "Good prediction – now watch where they come from."),
            [("Nothing", "Watch closely."), ("Ice crystals", "The room is warm."), ("Drink leaking through the metal", "The can is sealed.")], "O3",
            "Paused before the cold can is left on the table.",
            mc("u6n62p_t", "M", "O3", "Changing from a gas to a liquid is called…", "condensation", [("evaporation", ""), ("melting", ""), ("freezing", "")])),
 "u6n62e": dict(note="Paused after water drops formed on the can.",
   q=ex("u6n62e_q", "H", "O3", "EXPLAIN where the water on the outside of the can came from.",
        [("water vapour in the air", ["vapour|vapor|air|gas"]), ("cooled by the cold can and condensed", ["cool|cold|condens|liquid"])],
        "Water vapour in the air touched the cold can, cooled down and condensed into liquid water."),
   twin=mc("u6n62e_t", "H", "O3", "Why do bathroom mirrors steam up after a hot shower?", "Water vapour condenses on the cool mirror", [("The mirror melts", ""), ("Soap evaporates", ""), ("Light reflects water", "")])),
 "u6n63": P(("u6n63_q", "What is the chemical symbol for iron?"), ("Fe", "Yes – from its Latin name, ferrum."),
            [("I", "I is iodine."), ("Ir", "Ir is iridium."), ("FE", "The second letter is always small.")], "O4", "Paused after four everyday elements: Cu, Al, O, He.",
            mc("u6n63_t", "M", "O4", "Which element fills party balloons that float?", "Helium", [("Hydrogen only in schools", ""), ("Oxygen", ""), ("Copper", "")]), skill="Knowledge"),
 "u6n64": P(("u6n64_q", "Use the chart. Which two elements are the non-metals?"), ("Sulfur and phosphorus", "Yes – they have much lower melting points."),
            [("Tungsten and iron", "These are metals with very high melting points."), ("Copper and aluminium", "These are metals."), ("Iron and sulfur", "Iron is a metal.")], "O5",
            "Paused on the bar chart of melting points.",
            mc("u6n64_t", "M", "O5", "Most metals have…", "high melting points", [("low melting points", ""), ("no melting point", ""), ("melting points below 0 °C", "")]), skill="Data"),
 "u6n65p": P(("u6n65p_q", "PREDICT: after the iron and sulfur are heated together, will a magnet still pull out the iron?"), ("No – a new substance forms", "Good prediction – now watch."),
            [("Yes – iron is always magnetic", "Watch carefully."), ("Yes, but only the sulfur", "Sulfur is not magnetic."), ("The mixture will disappear", "Matter does not disappear.")], "O6",
            "Paused before the iron–sulfur mixture is heated.",
            mc("u6n65p_t", "M", "O6", "Before heating, the iron and sulfur are a…", "mixture", [("compound", ""), ("single element", ""), ("molecule", "")])),
 "u6n65e": dict(note="Paused after the black iron sulfide formed.",
   q=ex("u6n65e_q", "H", "O6", "EXPLAIN why the magnet could not pull iron out of the black solid.",
        [("iron and sulfur reacted / joined chemically", ["react|join|chemical|bond|combin"]), ("a new substance / compound (iron sulfide) with different properties", ["new|compound|iron sulfide|different propert"])],
        "The iron and sulfur reacted and joined chemically to make a new substance, iron sulfide. This compound has different properties, so it is not attracted to the magnet."),
   twin=mc("u6n65e_t", "H", "O6", "Which can be separated by a magnet?", "A mixture of iron and sulfur", [("Iron sulfide", ""), ("Water", ""), ("Salt", "")])),
 "u6n66": P(("u6n66_q", "How could you get the salt back from sea water?"), ("Evaporate the water", "Yes – the water leaves as vapour and the salt is left behind."),
            [("Use a magnet", "Salt is not magnetic."), ("Filter it", "Dissolved salt passes through filter paper."), ("Freeze it", "Freezing does not separate the salt easily.")], "O7",
            "Paused after four everyday mixtures: air, sea water, stainless steel, orange juice.",
            mc("u6n66_t", "M", "O7", "Stainless steel is…", "an alloy (a mixture of metals)", [("a pure element", ""), ("a compound", ""), ("a gas", "")]), skill="Knowledge"),
}

DROP = {"6.1": ["u6s1p09", "u6s1p17", "u6s1p03"], "6.2": ["u6s2p04", "u6s2p16"], "6.3": ["u6s3p01", "u6s3p02", "u6s3p13", "u6s3p17"],
        "6.4": ["u6s4p04", "u6s4p16", "u6s4p10"], "6.5": ["u6s5p12", "u6s5p04", "u6s5p13"], "6.6": ["u6s6p02", "u6s6p10", "u6s6p15"]}
STATES = {"kind": "particles", "boxes": [{"state": "gas", "label": "A"}, {"state": "solid", "label": "B"}, {"state": "liquid", "label": "C"}]}
COOL = {"kind": "linegraph", "x": {"min": 0, "max": 14, "step": 2, "label": "Time (min)"}, "y": {"min": 20, "max": 90, "step": 10, "label": "Temperature (°C)"},
        "series": [{"pts": [[0, 85], [2, 74], [4, 69], [6, 69], [8, 69], [10, 60], [12, 48], [14, 40]]}]}
MP = {"kind": "barchart", "labels": ["iron", "copper", "aluminium", "sulfur", "phosphorus"], "values": [1538, 1085, 660, 115, 44], "ymax": 1600, "step": 400, "ylabel": "Melting point (°C)", "xlabel": "Element"}
NEW_PRAC = {
 "6.1": [
  gd("u6s1p21", "M", "O1", "Look at the particle diagrams. Which state is shown in each box?", ["State"], [("Box A", ["Gas"]), ("Box B", ["Solid"]), ("Box C", ["Liquid"])], extra=[], fig=STATES),
  mc("u6s1p22", "H", "O2", "Look at the diagrams. In which box can the particles be pushed closer together?", "Box A", [("Box B", "Particles in a solid are already touching."), ("Box C", "Particles in a liquid are touching."), ("None of them", "One box has big gaps.")], fig=STATES),
  ex("u6s1p23", "H", "O2", "A sealed syringe of air is pushed and its volume halves. A syringe of water hardly changes. Explain the difference using particles.",
     [("gas particles far apart / spaces", ["far apart|space|gap"]), ("liquid particles touching / close", ["touch|close|no space|packed"])],
     "Air particles are far apart, so they can be pushed into the empty spaces between them. Water particles are already touching, so there is nowhere to push them."),
 ],
 "6.2": [
  num("u6s2p21", "The graph shows a liquid cooling. At what temperature does it freeze?", 69, "°C", "M", "O3", skill="Data", tol=1, units=["°C"], fig=COOL, hint="Look for the flat part of the graph."),
  mc("u6s2p22", "H", "O3", "Use the graph. Why is the line flat between 4 and 8 minutes?", "The substance is changing state (freezing), so its temperature stays the same",
     [("The thermometer broke", "The flat part happens for a reason."), ("The liquid stopped cooling because it was empty", "It is still there."), ("The room got warmer", "The room stayed the same.")], fig=COOL, skill="Data"),
  gd("u6s2p23", "H", "O3", "A substance melts at −7 °C and boils at 59 °C. What state is it in at each temperature?", ["State"], [("−20 °C", ["Solid"]), ("25 °C", ["Liquid"]), ("80 °C", ["Gas"])], extra=[]),
 ],
 "6.3": [
  gd("u6s3p21", "M", "O4", "Element or not an element?", ["Element", "Not an element"], [("Gold", ["✓", "✗"]), ("Water", ["✗", "✓"]), ("Oxygen", ["✓", "✗"]), ("Salt", ["✗", "✓"])]),
  nm("u6s3p22", "H", "O4", "How many atoms are in one molecule of phosphorus, P₄?", 4, "atoms", units=["atoms", ""]),
  mc("u6s3p24", "H", "O4", "Neon (Ne) and helium (He) exist as single atoms, but oxygen exists as O₂. What is the difference?", "Oxygen atoms join in pairs to make molecules; neon and helium atoms stay single",
     [("Neon and helium are compounds", "They are elements."), ("Oxygen is a mixture", "O₂ is an element – both atoms are oxygen."), ("There is no difference", "One is made of molecules, the others of single atoms.")]),
  mt("u6s3p23", "M", "O4", "Match each everyday use to the element.", [("Electrical wires", "copper"), ("Drink cans", "aluminium"), ("Floating party balloons", "helium"), ("Breathing support in hospital", "oxygen")]),
 ],
 "6.4": [
  mc("u6s4p21", "M", "O5", "Use the bar chart. Which element has the highest melting point?", "Iron", [("Copper", "Its bar is shorter."), ("Sulfur", "Sulfur melts at only 115 °C."), ("Aluminium", "Its bar is shorter.")], fig=MP, skill="Data"),
  nm("u6s4p22", "H", "O5", "Use the bar chart. How much higher is the melting point of copper than aluminium?", 425, "°C", units=["°C"], fig=MP, skill="Data", tol=5),
  gd("u6s4p23", "H", "O5", "Use the properties to decide: metal or non-metal?", ["Metal", "Non-metal"],
     [("Shiny, conducts electricity, melts at 1455 °C", ["✓", "✗"]), ("Dull yellow powder, brittle, melts at 115 °C", ["✗", "✓"]), ("Green gas at room temperature", ["✗", "✓"]), ("Bends without breaking, conducts heat", ["✓", "✗"])]),
 ],
 "6.5": [
  nm("u6s5p21", "H", "O6", "5.6 g of iron reacts with 3.2 g of sulfur. What mass of iron sulfide is made?", 8.8, "g", errs=[(2.4, "Add the masses – no atoms are lost.")]),
  gd("u6s5p22", "H", "O6", "Mixture of iron and sulfur, or the compound iron sulfide?", ["Mixture", "Compound"],
     [("Can be separated with a magnet", ["✓", "✗"]), ("Is a black solid with new properties", ["✗", "✓"]), ("You can still see yellow and grey bits", ["✓", "✗"]), ("Made by heating, which causes a reaction", ["✗", "✓"])]),
  mc("u6s5p23", "H", "O6", "How many atoms are in one molecule of glucose, C₆H₁₂O₆?", "24", [("3", "That is the number of elements."), ("6", "Add all the small numbers: 6 + 12 + 6."), ("18", "Count the oxygen atoms too.")]),
 ],
 "6.6": [
  nm("u6s6p21", "H", "O7", "Evaporating 200 cm³ of sea water leaves 7 g of salt. How much salt would 1000 cm³ leave?", 35, "g"),
  gd("u6s6p22", "M", "O7", "Element, compound or mixture?", ["Type"], [("Iron", ["Element"]), ("Carbon dioxide", ["Compound"]), ("Air", ["Mixture"]), ("Stainless steel", ["Mixture"]), ("Water", ["Compound"])], extra=[]),
  mc("u6s6p23", "H", "O7", "Pure water boils at exactly 100 °C. A sample boils over a range from 101 to 104 °C. What does this tell you?", "It is a mixture (it contains dissolved substances)",
     [("It is pure water", "Pure substances boil at one fixed temperature."), ("It is an element", "Water is a compound."), ("The thermometer is broken", "A range is what a mixture shows.")]),
 ],
}
NEW_ADV = {
 "6.1": [adv(ex("u6s1a5", "VH", "O2", "A student draws a gas as a few particles in one corner of a box, all touching. Explain TWO things wrong with this particle diagram.",
     [("gas particles should be far apart / spread out", ["far apart|spread|not touching|gap|space"]), ("should fill the whole box / move in all directions", ["fill|whole|everywhere|all directions|random|move"])],
     "Gas particles are far apart, not touching, and they spread out to fill the whole container, moving quickly in all directions.", need=2, src=src("SRC-RSCPART")))],
 "6.5": [adv(ex("u6s5a5", "VH", "O6", "Magnesium ribbon is burned in an open dish. The white ash weighs MORE than the magnesium did. A student says 'mass was created'. Explain the real reason.",
     [("magnesium reacts / joins with oxygen from the air", ["oxygen|air"]), ("so the product (magnesium oxide) includes the oxygen's mass / mass is conserved", ["oxide|conserv|no mass|not created|added|includes"])],
     "Magnesium joins with oxygen from the air to make magnesium oxide. The extra mass is the oxygen; no mass is created – mass is conserved.", need=2, src=src("SRC-AAAS")))],
}

from tests_stage7_unit06_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
