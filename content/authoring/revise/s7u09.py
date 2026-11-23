# -*- coding: utf-8 -*-
"""Stage 7 Unit 9 Chemical Reactions — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-SHILAV", "name": "Science History Institute – Antoine-Laurent Lavoisier", "url": "https://www.sciencehistory.org/historical-profile/antoine-laurent-lavoisier", "use": "History behind the conservation-of-mass Challenge question (9.2): metals gain mass when they burn."},
    {"id": "SRC-NOAAOA", "name": "NOAA Education – Ocean acidification", "url": "https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-acidification", "use": "Pteropod-shell finding used in the Challenge question (9.3)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u9n91": dict(note="Paused after four kitchen changes: ice melting, sugar dissolving, frying an egg, baking a cake.",
   q=ex("u9n91_q", "M", "O1", "Is milk going sour a physical or a chemical change? Give a reason.",
        [("chemical", ["chemical"]), ("a new substance forms / new smell or taste / cannot be reversed", ["new|smell|taste|sour|acid|revers|undo|back"])],
        "Chemical – new substances (such as lactic acid) form, giving a new smell and taste, and it cannot be reversed."),
   twin=mc("u9n91_t", "M", "O1", "Which change is physical?", "Butter melting in a pan", [("Wood burning", ""), ("Milk going sour", ""), ("A cake baking", "")])),
 "u9n92p": dict(note="Paused before the baking soda drops into the vinegar in the sealed flask (152.4 g).",
   q=mc("u9n92p_q", "M", "O2", "PREDICT: in the sealed flask, what will happen to the mass?", ("It will stay the same", "Good prediction – now watch."),
        [("It will go up", "Watch carefully."), ("It will go down", "Watch carefully – can anything escape?"), ("It will drop to zero", "The substances do not vanish.")], skill="Prediction"),
   twin=mc("u9n92p_t", "M", "O2", "In a reaction, the starting substances are called the…", "reactants", [("products", ""), ("indicators", ""), ("mixtures", "")])),
 "u9n92e": dict(note="Paused after the balance still read 152.4 g.",
   q=ex("u9n92e_q", "H", "O2", "EXPLAIN why the mass stayed the same even though a gas was made.",
        [("atoms are rearranged, not created or destroyed", ["rearrang|not (created|destroyed)|cannot be (created|destroyed)|conserv"]), ("the gas was trapped in the balloon / sealed / nothing escaped", ["trap|balloon|seal|escape|closed"])],
        "In a reaction atoms are only rearranged, not created or destroyed. The carbon dioxide was trapped in the balloon, so nothing escaped and the total mass stayed the same."),
   twin=mc("u9n92e_t", "M", "O2", "Conservation of mass means…", "the total mass before and after a reaction is the same", [("mass always goes up", ""), ("gases have no mass", ""), ("atoms disappear", "")])),
 "u9n93": dict(note="Paused on the graph: the open flask's mass fell from 150.0 g to 148.7 g.",
   q=mc("u9n93_q", "H", "O2", "Atoms cannot be destroyed, so why did the mass of the open flask go down?", ("Carbon dioxide gas escaped into the air", "Yes – the gas left the flask."),
        [("Some atoms were destroyed", "Atoms are never destroyed in a reaction."), ("The balance was faulty", "The sealed flask shows the balance is fine."), ("The acid evaporated instantly", "The fizzing gas is carbon dioxide.")], skill="Data"),
   twin=nm("u9n93_t", "M", "O2", "The flask was 150.0 g at the start and 148.7 g at the end. What mass of gas escaped?", 1.3, "g", tol=0.05, units=["g"])),
 "u9n94": dict(note="Paused on the bar chart: bare 30 mg, oiled 6 mg, painted 3 mg, galvanised 1 mg of rust.",
   q=ex("u9n94_q", "H", "O3", "Why does a layer of paint or oil slow down rusting?",
        [("it keeps air / oxygen out", ["air|oxygen"]), ("it keeps water out", ["water|moist|damp"])],
        "The layer is a barrier that stops oxygen and water reaching the iron, and iron needs both to rust."),
   twin=mc("u9n94_t", "M", "O3", "Which treatment protected the nail best in the class results?", "Galvanising (zinc coating)", [("Oiling", ""), ("Painting", ""), ("No treatment", "")])),
 "u9n95p": dict(note="Paused before green copper carbonate is heated, with the gas bubbled through limewater.",
   q=mc("u9n95p_q", "M", "O4", "PREDICT: what signs of a reaction might you see?", ("A colour change and a gas that turns limewater milky", "Good prediction – now watch."),
        [("Nothing will change", "Watch carefully."), ("The powder will melt into a green liquid", "Watch carefully."), ("A squeaky pop", "That is the test for hydrogen.")], skill="Prediction"),
   twin=mc("u9n95p_t", "M", "O4", "Which is a sign of a chemical reaction?", "A colour change", [("A change of shape", ""), ("Melting", ""), ("Dissolving", "")])),
 "u9n95e": dict(note="Paused after the powder turned black and the limewater turned milky.",
   q=ex("u9n95e_q", "H", "O4", "EXPLAIN what the observations show, and write the word equation.",
        [("colour change shows a new substance (copper oxide)", ["colour|black|copper oxide|new substance"]), ("limewater milky shows carbon dioxide was given off", ["carbon dioxide|co2|limewater"]), ("copper carbonate → copper oxide + carbon dioxide", ["copper oxide.{0,30}carbon dioxide|carbon dioxide.{0,30}copper oxide"])],
        "The green powder turned into a new black substance, copper oxide, and the gas turned limewater milky, so it was carbon dioxide. Copper carbonate → copper oxide + carbon dioxide.", need=2),
   twin=mc("u9n95e_t", "H", "O4", "What is the black powder left in the tube?", "Copper oxide", [("Copper carbonate", ""), ("Carbon", ""), ("Rust", "")])),
}

DROP = {"9.1": ["u9s1p02", "u9s1p04", "u9s1p16"], "9.2": ["u9s2p01", "u9s2p11", "u9s2p15"], "9.3": ["u9s3p01", "u9s3p06", "u9s3p16"], "9.4": ["u9s4p01", "u9s4p08", "u9s4p13"]}

MG = {"kind": "linegraph", "x": {"min": 0, "max": 6, "step": 1, "label": "Heating time (min)"}, "y": {"min": 2.0, "max": 3.0, "step": 0.2, "label": "Mass of crucible contents (g)"},
      "series": [{"pts": [[0, 2.40], [1, 2.62], [2, 2.80], [3, 2.92], [4, 2.98], [5, 3.00], [6, 3.00]], "label": "magnesium heated in air"}]}
TEMP = {"kind": "barchart", "labels": ["acid + magnesium", "acid + alkali", "baking soda + vinegar", "sugar + water"], "values": [29, 26, 16, 20], "ymax": 30, "step": 5, "ylabel": "Temperature after mixing (°C)", "xlabel": "Mixture (all started at 20 °C)"}
GASV = {"kind": "linegraph", "x": {"min": 0, "max": 60, "step": 10, "label": "Time (s)"}, "y": {"min": 0, "max": 50, "step": 10, "label": "Volume of hydrogen (cm³)"},
        "series": [{"pts": [[0, 0], [10, 18], [20, 30], [30, 38], [40, 42], [50, 43], [60, 43]], "label": "magnesium + acid"}]}
NEW_PRAC = {
 "9.1": [
  gd("u9s1p21", "M", "O1", "Physical or chemical change? Use the evidence.", ["Type"],
     [("Wax melts, then sets again", ["Physical"]), ("A match burns and leaves black ash", ["Chemical"]), ("Salt dissolves, and is left behind when the water evaporates", ["Physical"]), ("Milk goes sour and smells different", ["Chemical"])], extra=[]),
  mc("u9s1p22", "H", "O1", "Use the bar chart. Which mixture shows NO evidence of a chemical change from temperature?", "Sugar + water", [("Acid + magnesium", "It rose from 20 °C to 29 °C."), ("Baking soda + vinegar", "It got colder, which is also evidence."), ("Acid + alkali", "It rose from 20 °C to 26 °C.")], fig=TEMP, skill="Data"),
  mc("u9s1p23", "H", "O1", "Use the bar chart. A student says 'only reactions that get hot are chemical'. Which result shows she is wrong?", "Baking soda + vinegar got colder but is a reaction", [("Acid + magnesium got hotter", "That agrees with her."), ("Sugar + water did not change", "Dissolving is not a reaction."), ("Acid + alkali got hotter", "That agrees with her.")], fig=TEMP, skill="Data"),
 ],
 "9.2": [
  nm("u9s2p21", "H", "O2", "Magnesium is heated in a crucible. Use the graph. What mass of oxygen joined the magnesium altogether?", 0.6, "g", tol=0.02, units=["g"], fig=MG, skill="Data"),
  mc("u9s2p22", "H", "O2", "Use the graph. Why does the mass stop increasing after 5 minutes?", "All the magnesium has reacted", [("The oxygen in the air has run out", "There is plenty of air."), ("Atoms are being destroyed", "Atoms are never destroyed."), ("The crucible has melted", "Crucibles survive high temperatures.")], fig=MG, skill="Data"),
  mt("u9s2p23", "H", "O2", "Match each word to its meaning.", [("Reactant", "a substance you start with"), ("Product", "a new substance made"), ("Molecule", "atoms joined together"), ("Word equation", "reactants → products")]),
 ],
 "9.3": [
  gd("u9s3p21", "M", "O3", "Useful or harmful reaction?", ["Type"],
     [("Burning petrol in a car engine", ["Useful"]), ("Iron railings rusting", ["Harmful"]), ("Making ammonia for fertilisers", ["Useful"]), ("Acid rain eating a limestone statue", ["Harmful"])], extra=[]),
  ex("u9s3p22", "H", "O3", "Combustion of fuels is both useful and harmful. Give one way it is useful and one way it is harmful.",
     [("useful: releases energy (to power vehicles / heat / electricity)", ["energy|power|heat|electric|cook"]), ("harmful: carbon dioxide / greenhouse gases / acid rain / pollution", ["carbon dioxide|greenhouse|acid rain|pollut|climate|smoke"])],
     "It is useful because it releases energy to power vehicles and generate electricity, but it is harmful because it makes carbon dioxide (a greenhouse gas) and gases that cause acid rain."),
  od("u9s3p23", "H", "O3", "Put the steps of a rust-prevention investigation in order.", ["Clean four identical iron nails", "Coat three nails with oil, paint or zinc; leave one bare", "Leave all four in damp air for two weeks", "Weigh the rust that forms on each nail"]),
 ],
 "9.4": [
  nm("u9s4p21", "M", "O4", "Magnesium reacts with acid. Use the graph. What volume of hydrogen was made in the first 20 seconds?", 30, "cm³", tol=1, units=["cm³", "cm3"], fig=GASV, skill="Data"),
  mc("u9s4p22", "H", "O4", "Use the graph. When was the reaction fastest?", "In the first 10 seconds", [("Between 40 and 50 s", "The line is almost flat then."), ("After 50 s", "No more gas is made."), ("It was the same speed all the time", "The line gets less steep.")], fig=GASV, skill="Data"),
  gd("u9s4p23", "H", "O4", "Which gas does each test show?", ["Gas"],
     [("Lighted splint gives a squeaky pop", ["Hydrogen"]), ("Glowing splint relights", ["Oxygen"]), ("Limewater turns milky", ["Carbon dioxide"])], extra=["Nitrogen"]),
 ],
}
NEW_ADV = {
 "9.2": [adv(ex("u9s2a5", "VH", "O2", "In the 1700s, many chemists were puzzled that metals such as tin get HEAVIER when they are heated in air. Lavoisier weighed everything carefully, in closed containers. Use the idea of conservation of mass to explain the result.",
     [("the metal reacts / combines with oxygen from the air", ["oxygen|air"]), ("the oxide product contains the metal atoms plus oxygen atoms, so it is heavier", ["oxide|combine|join|add"]), ("in a closed container the total mass does not change", ["closed|total|conserv|same"])],
     "When the tin is heated it combines with oxygen from the air to make tin oxide, so the product contains extra oxygen atoms and weighs more than the tin. In a closed container the air loses the same mass, so the total mass stays the same.", need=2, src=src("SRC-SHILAV")))],
 "9.3": [adv(ex("u9s3a5", "VH", "O3", "NOAA scientists put tiny sea-snail shells in sea water with the pH expected in the year 2100. The shells slowly dissolved over 45 days. Explain this result.",
     [("sea water becomes more acidic (lower pH) as it absorbs carbon dioxide", ["acid|ph|carbon dioxide|co2"]), ("shells are calcium carbonate", ["calcium carbonate|carbonate"]), ("acids react with carbonates, so the shell dissolves", ["react|dissolv|break"])],
     "The ocean absorbs carbon dioxide, which makes the sea water more acidic. The shells are made of calcium carbonate, and acids react with carbonates, so the shells slowly dissolved.", need=2, src=src("SRC-NOAAOA")))],
}

from tests_stage7_unit09_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
