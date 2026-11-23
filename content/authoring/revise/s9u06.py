# -*- coding: utf-8 -*-
"""Stage 9 Unit 6 Displacement Reactions — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-RSCTHERM", "name": "Royal Society of Chemistry – The thermite reaction (demonstration)", "url": "https://edu.rsc.org/resources/the-thermite-reaction/724.article", "use": "Aluminium displacing iron from iron(III) oxide: Challenge question (6.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s9u06n11p": dict(note="Paused before magnesium ribbon (25.24 g with crucible) is heated.",
   q=mc("s9u06n11p_q", "M", "O1", "PREDICT: after heating, the mass of the crucible and contents will be…", ("higher", "Good prediction – now watch."),
        [("lower", "Watch carefully."), ("the same", "Watch carefully."), ("zero", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u06n11p_t", "M", "O1", "The formula of oxygen gas is…", "O₂", [("O", ""), ("O₃", ""), ("2O", "")])),
 "s9u06n11e": dict(note="Paused after the mass rose from 25.24 g to 25.40 g and a white powder formed.",
   q=ex("s9u06n11e_q", "H", "O1", "EXPLAIN the increase in mass and write the word equation.",
        [("magnesium + oxygen → magnesium oxide", ["magnesium \\+ oxygen.{0,10}(→|->|gives|makes|forms).{0,10}magnesium oxide"]), ("oxygen atoms from the air joined the magnesium, so the solid gained mass", ["oxygen.{0,40}(join|combin|added|from the air)|gained|added"])],
        "Magnesium + oxygen → magnesium oxide. Oxygen atoms from the air combined with the magnesium, so the solid product contains extra atoms and has a greater mass."),
   twin=nm("s9u06n11e_t", "M", "O1", "What mass of oxygen joined the magnesium (25.24 g to 25.40 g)?", 0.16, "g", tol=0, units=["g"])),
 "s9u06n21": dict(note="Paused after four uses of displacement: rail welding, copper from waste, cleaning water and jewellery.",
   q=mc("s9u06n21_q", "H", "O3", "Will copper displace iron from iron sulfate solution?", ("No: copper is less reactive than iron", "Yes."),
        [("Yes: copper is more reactive than iron", "Check the reactivity series."), ("Yes: all metals displace each other", "Only more reactive ones do."), ("No: iron sulfate is not a solution", "It dissolves in water.")]),
   twin=mc("s9u06n21_t", "M", "O3", "Scrap iron is used to recover copper from waste solutions because…", "iron is more reactive than copper", [("iron is less reactive than copper", ""), ("iron is magnetic", ""), ("copper is a gas", "")])),
}

DROP = {"6.1": ["s9u06s1p01", "s9u06s1p02", "s9u06s1p07"], "6.2": ["s9u06s2p06", "s9u06s2p11", "s9u06s2p07"]}

GRID = {"kind": "barchart", "labels": ["Mg in CuSO₄", "Zn in CuSO₄", "Fe in CuSO₄", "Cu in CuSO₄"], "values": [42, 14, 7, 0], "ymax": 45, "step": 5, "ylabel": "Temperature rise (°C)"}
NEW_PRAC = {
 "6.1": [
  gd("s9u06s1p21", "H", "O1", "Count the atoms in 2H₂ + O₂ → 2H₂O.", ["Number"],
     [("Hydrogen atoms on the left", ["4"]), ("Oxygen atoms on the left", ["2"]), ("Hydrogen atoms on the right", ["4"]), ("Oxygen atoms on the right", ["2"])], extra=["1", "3"]),
  ex("s9u06s1p22", "H", "O1", "Iron wool is heated in air on a balance and its mass increases. A student says 'mass was created'. Explain why this is wrong.",
     [("iron reacts with oxygen from the air (forming iron oxide)", ["oxygen|iron oxide"]), ("atoms are not created; oxygen atoms were added, so total mass is conserved", ["not created|conserv|added|joined|no atoms"])],
     "Mass was not created. The iron reacted with oxygen from the air to form iron oxide. The oxygen atoms that joined the iron add to its mass; the total mass of iron plus oxygen is conserved."),
 ],
 "6.2": [
  od("s9u06s2p21", "M", "O2", "Use the chart. Order the metals by reactivity, most reactive first.", ["magnesium", "zinc", "iron", "copper"], fig=GRID, skill="Data"),
  ex("s9u06s2p22", "H", "O3", "Use the chart. Explain why copper in copper sulfate gave no temperature rise.",
     [("copper cannot displace itself / same metal", ["same|itself|cannot displace"]), ("no reaction, so no energy (heat) released", ["no reaction|no energy|no heat|nothing happens"])],
     "Copper is the same metal as in the compound, so it cannot displace itself. No reaction happens, so no heat is released and the temperature does not rise.", fig=GRID, skill="Data"),
  mc("s9u06s2p23", "H", "O3", "Use the chart. What controls should be used to make the comparison fair?", "Same volume and concentration of copper sulfate and the same mass of each metal powder", [("Different volumes for each metal", "That is unfair."), ("Use larger pieces for less reactive metals", "Keep the mass and size the same."), ("Start at different temperatures", "Use the same starting temperature.")], fig=GRID),
 ],
}
NEW_ADV = {
 "6.2": [adv(ex("s9u06s2a05", "VH", "O3", "The RSC thermite demonstration mixes aluminium powder with iron(III) oxide. A white-hot glow is seen and molten iron forms. Write the word equation, explain why the reaction happens, and suggest why copper powder would NOT react with iron(III) oxide.",
     [("aluminium + iron(III) oxide → aluminium oxide + iron", ["aluminium \\+ iron.{0,20}oxide.{0,15}(→|->|gives|makes).{0,10}aluminium oxide.{0,10}iron"]), ("aluminium is more reactive than iron, so it takes the oxygen / displaces iron", ["more reactive|displac|takes the oxygen"]), ("copper is less reactive than iron, so it cannot take the oxygen", ["copper.{0,30}less reactive|less reactive than iron|below iron"])],
     "Aluminium + iron(III) oxide → aluminium oxide + iron. Aluminium is more reactive than iron, so it takes the oxygen from the iron oxide and displaces the iron. Copper is less reactive than iron, so it cannot take the oxygen and no reaction happens.", need=2, src=src("SRC-RSCTHERM")))],
}

from tests_stage9_unit06_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
