# -*- coding: utf-8 -*-
"""Stage 9 Unit 5 Chemical Bonding and Structure of Materials — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-PUBMGO", "name": "PubChem (US National Library of Medicine) – Magnesium oxide", "url": "https://pubchem.ncbi.nlm.nih.gov/compound/magnesium%20oxide", "use": "Melting point of magnesium oxide for the video chart and the Challenge question (5.4)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

MP = {"kind": "barchart", "labels": ["sulfur", "sodium chloride", "silicon dioxide", "magnesium oxide"], "values": [115, 801, 1713, 2852], "ymax": 3000, "step": 500, "ylabel": "Melting point (°C)"}

NEW_STOPS = {
 "s9u05n21": dict(note="Paused after four covalent molecules: water, carbon dioxide, methane and oxygen.",
   q=gd("s9u05n21_q", "H", "O2", "How many covalent bonds (shared pairs) are in each molecule?", ["Shared pairs"],
        [("H₂O", ["2"]), ("CH₄", ["4"]), ("O₂", ["2"]), ("H₂", ["1"])], extra=["3"]),
   twin=mc("s9u05n21_t", "M", "O2", "Why are small covalent substances such as methane gases at room temperature?", "The forces between their molecules are weak", [("Their covalent bonds are weak", ""), ("They contain ions", ""), ("They are metals", "")])),
 "s9u05n41p": dict(note="Paused before solid salt, salt solution and sugar solution are tested with a bulb circuit.",
   q=ms("s9u05n41p_q", "M", "O4", "PREDICT: select ALL the samples that will light the bulb.", ["Salt solution"], [("Solid salt", "Watch carefully."), ("Sugar solution", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u05n41p_t", "M", "O3", "Sodium chloride is held together by…", "ionic bonds", [("covalent bonds between molecules", ""), ("metallic bonds", ""), ("hydrogen only", "")])),
 "s9u05n41e": dict(note="Paused after only the salt solution lit the bulb.",
   q=ex("s9u05n41e_q", "H", "O4", "EXPLAIN why only the salt solution conducted.",
        [("in solution the ions are free to move (and carry charge)", ["ions.{0,30}(free|move)|free.{0,20}ions|mobile"]), ("in solid salt ions are fixed; sugar has no ions / is covalent", ["fixed|cannot move|can't move|lattice|no ions|covalent|no charge|uncharged"])],
        "In the salt solution the ions are free to move and carry charge, so it conducts. In solid salt the ions are fixed in the lattice and cannot move, and sugar is made of covalent molecules with no charge, so neither conducts."),
   twin=mc("s9u05n41e_t", "H", "O4", "Molten (melted) salt would…", "conduct, because the ions can move", [("not conduct, because it is a liquid", ""), ("conduct, because electrons move through it like a metal", ""), ("explode", "")])),
 "s9u05n42": dict(note="Paused on the chart: sulfur 115, sodium chloride 801, silicon dioxide 1713, magnesium oxide 2852 °C.",
   q=ex("s9u05n42_q", "H", "O4", "Why does sulfur melt at a much lower temperature than the other three?",
        [("sulfur is made of small (simple) molecules", ["molecul|simple"]), ("only weak forces between molecules need to be overcome; the others have giant structures with strong bonds", ["weak|giant|strong bonds|lattice|network"])],
        "Sulfur is made of small molecules with only weak forces between them, so little energy is needed to separate them. The other three have giant ionic or covalent structures held by many strong bonds, which need much more energy to break.", skill="Data"),
   twin=nm("s9u05n42_t", "M", "O4", "Use the chart. How much higher is the melting point of magnesium oxide than sodium chloride?", 2051, "°C", tol=0, units=["°C"], fig=MP)),
}

DROP = {"5.1": ["s9u05s1p06", "s9u05s1p07"], "5.2": ["s9u05s2p02", "s9u05s2p10"], "5.3": ["s9u05s3p01", "s9u05s3p02"], "5.4": ["s9u05s4p01", "s9u05s4p04"]}

NEW_PRAC = {
 "5.1": [
  gd("s9u05s1p21", "M", "O1", "Will each atom lose, gain or share electrons to bond?", ["Behaviour"],
     [("Sodium with chlorine", ["Sodium loses one"]), ("Chlorine with sodium", ["Chlorine gains one"]), ("Hydrogen with hydrogen", ["They share"])], extra=["Nothing happens"]),
  mc("s9u05s1p22", "H", "O1", "Argon is used inside some light bulbs because…", "its full outer shell makes it unreactive, so the hot filament does not burn", [("it glows by itself", "It is unreactive."), ("it is a good conductor", "It is a gas."), ("it reacts with the filament", "It does not react.")]),
 ],
 "5.2": [
  nm("s9u05s2p21", "M", "O2", "Ammonia, NH₃: how many electrons does nitrogen share in total in the molecule?", 3, "electrons", tol=0, units=["electrons", ""]),
  ex("s9u05s2p22", "H", "O2", "Explain why carbon can form so many different molecules.",
     [("carbon has 4 outer electrons", ["4|four"]), ("so it forms 4 covalent bonds, including chains and rings with other carbon atoms", ["4 (covalent )?bonds|four bonds|chains|rings|other carbon"])],
     "Carbon has four outer electrons, so it forms four covalent bonds. It can bond to other carbon atoms in long chains and rings, and to many other elements, so a huge number of different molecules are possible."),
 ],
 "5.3": [
  gd("s9u05s3p21", "H", "O3", "Write the charge on each ion.", ["Charge"],
     [("Sodium ion", ["1+"]), ("Magnesium ion", ["2+"]), ("Chloride ion", ["1−"]), ("Oxide ion", ["2−"])], extra=["3+"]),
  od("s9u05s3p22", "H", "O3", "Order the steps in forming sodium chloride.", ["Sodium loses its outer electron", "Chlorine gains the electron", "Na⁺ and Cl⁻ ions form", "Opposite charges attract in a giant lattice"]),
 ],
 "5.4": [
  gd("s9u05s4p21", "H", "O4", "Four solids A–D were tested. Which structure is most likely for each?", ["Structure"],
     [("A: melts at −182 °C, never conducts", ["Simple molecular"]), ("B: melts at 801 °C, conducts only when molten or dissolved", ["Giant ionic"]), ("C: melts at about 3550 °C, does not conduct", ["Giant covalent"]), ("D: melts at 1538 °C, conducts as a solid", ["Metal"])], extra=[], skill="Data"),
 ],
}
NEW_ADV = {
 "5.4": [adv(ex("s9u05s4a05", "VH", "O4", "PubChem gives the melting point of magnesium oxide as 2852 °C, much higher than sodium chloride (801 °C), though both are giant ionic lattices. Suggest why, and give one use that depends on this property.",
     [("magnesium oxide has ions with larger charges (Mg²⁺ and O²⁻ v Na⁺ and Cl⁻)", ["2\\+|2−|2-|double|larger charge|bigger charge|higher charge"]), ("so the attraction / ionic bonds are much stronger, needing more energy to break", ["stronger|more energy|stronger attraction"]), ("use: lining furnaces / heat-resistant bricks", ["furnace|kiln|lining|heat.?resist|brick|refractor"])],
     "Magnesium oxide is made of Mg²⁺ and O²⁻ ions, which have double the charges of Na⁺ and Cl⁻. The attraction between them is much stronger, so far more energy is needed to break up the lattice. Because it does not melt even at very high temperatures, it is used to line furnaces and kilns.", need=2, src=src("SRC-PUBMGO")))],
}

from tests_stage9_unit05_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
