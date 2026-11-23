# -*- coding: utf-8 -*-
"""Stage 8 Unit 6 Chemical Reactivity — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-RSCDISP", "name": "Royal Society of Chemistry (Nuffield practical collection) – Displacement reactions between metals and their salts", "url": "https://edu.rsc.org/resources/displacement-reactions-between-metals-and-their-salts/720.article", "use": "Idea for the 'unknown metal W' Challenge question (6.4)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "s8u06n11p": dict(note="Paused before magnesium, copper and gold are held in a flame.",
   q=mc("s8u06n11p_q", "M", "O1", "PREDICT: which metal will react most strongly with oxygen?", ("Magnesium", "Good prediction – now watch."),
        [("Copper", "Watch carefully."), ("Gold", "Watch carefully."), ("All the same", "These metals have different reactivity.")], skill="Prediction"),
   twin=mc("s8u06n11p_t", "M", "O1", "Metal + oxygen →", "metal oxide", [("metal hydroxide", ""), ("metal salt + hydrogen", ""), ("nothing", "")])),
 "s8u06n11e": dict(note="Paused after magnesium burned, copper blackened and gold did not change.",
   q=od("s8u06n11e_q", "H", "O1", "EXPLAIN by ordering: put the metals from most to least reactive with oxygen.", ["magnesium", "copper", "gold"]),
   twin=mc("s8u06n11e_t", "H", "O1", "What is the black coating on the heated copper?", "Copper oxide", [("Carbon", ""), ("Copper sulfate", ""), ("Rust", "")])),
 "s8u06n12": dict(note="Paused on the graph: calcium gave 80 cm³ of hydrogen in 5 min; magnesium less than 1 cm³.",
   q=ex("s8u06n12_q", "H", "O2", "Which metal is more reactive with water, and what evidence supports this?",
        [("calcium is more reactive", ["calcium"]), ("it gave much more hydrogen / faster (80 cm³ vs under 1 cm³)", ["80|more (hydrogen|gas)|faster|quick|less than 1|under 1"])],
        "Calcium is more reactive: it gave off about 80 cm³ of hydrogen in five minutes, while the same mass of magnesium gave off less than 1 cm³."),
   twin=nm("s8u06n12_t", "M", "O2", "Use the graph. How much hydrogen had calcium made after 2 minutes?", 55, "cm³", tol=2, units=["cm³", "cm3"])),
 "s8u06n13": dict(note="Paused on the chart: magnesium 18 °C, zinc 6 °C, iron 3 °C, copper 0 °C rise.",
   q=mc("s8u06n13_q", "H", "O3", "Why can the temperature rise be used to order the metals?", ("More reactive metals react more vigorously and release more heat", "Yes."),
        [("All metals release the same heat", "The rises are different."), ("Copper releases the most heat", "Copper gave no rise."), ("Temperature has nothing to do with reactions", "Reactions transfer energy.")], skill="Data"),
   twin=od("s8u06n13_t", "M", "O3", "Order the metals by reactivity with acid, most first.", ["magnesium", "zinc", "iron", "copper"])),
 "s8u06n14p": dict(note="Paused before zinc is put in copper sulfate and copper in zinc sulfate.",
   q=mc("s8u06n14p_q", "M", "O4", "PREDICT: where will a reaction happen?", ("Zinc in copper sulfate", "Good prediction – now watch."),
        [("Copper in zinc sulfate", "Watch carefully."), ("In both beakers", "Watch carefully."), ("In neither beaker", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u06n14p_t", "M", "O4", "Which is more reactive?", "Zinc", [("Copper", ""), ("Gold", ""), ("Silver", "")])),
 "s8u06n14e": dict(note="Paused after the zinc became coated with copper and the blue colour faded.",
   q=ex("s8u06n14e_q", "H", "O4", "EXPLAIN the result and write the word equation.",
        [("zinc is more reactive than copper", ["more reactive"]), ("zinc displaces copper from its compound", ["displac|push"]), ("zinc + copper sulfate → zinc sulfate + copper", ["zinc sulfate"])],
        "Zinc is more reactive than copper, so it displaces copper from copper sulfate: zinc + copper sulfate → zinc sulfate + copper. Copper is less reactive, so it cannot displace zinc.", need=2),
   twin=mc("s8u06n14e_t", "H", "O4", "Which pair would react?", "Magnesium + iron sulfate", [("Copper + magnesium sulfate", ""), ("Gold + zinc sulfate", ""), ("Silver + copper sulfate", "")])),
}

DROP = {"6.1": ["s8u06s1p01", "s8u06s1p14", "s8u06s1p15"], "6.2": ["s8u06s2p09", "s8u06s2p14", "s8u06s2p08"], "6.3": ["s8u06s3p08", "s8u06s3p09", "s8u06s3p04"], "6.4": ["s8u06s4p01", "s8u06s4p10", "s8u06s4p15"]}

H2 = {"kind": "linegraph", "x": {"min": 0, "max": 60, "step": 10, "label": "Time (s)"}, "y": {"min": 0, "max": 60, "step": 10, "label": "Volume of hydrogen (cm³)"},
      "series": [{"pts": [[0, 0], [10, 30], [20, 45], [30, 52], [40, 54], [60, 54]], "label": "magnesium"}, {"pts": [[0, 0], [10, 6], [20, 12], [30, 18], [40, 23], [60, 32]], "label": "zinc", "dash": True}]}
DISP = {"kind": "barchart", "labels": ["Mg in CuSO₄", "Zn in CuSO₄", "Fe in CuSO₄", "Cu in CuSO₄"], "values": [12, 8, 4, 0], "ymax": 14, "step": 2, "ylabel": "Temperature rise (°C)", "xlabel": "Metal in copper sulfate solution"}
NEW_PRAC = {
 "6.1": [
  od("s8u06s1p21", "M", "O1", "A student heats four metals. Order them by how strongly they react with oxygen, most first.", ["sodium", "magnesium", "iron", "gold"]),
  ex("s8u06s1p22", "H", "O1", "Sodium is stored under oil, but gold can be left out in air. Explain why.",
     [("sodium reacts very quickly with oxygen / air (and water)", ["sodium.{0,50}(react|oxygen|air)|very reactive"]), ("oil keeps air and water away", ["oil.{0,40}(keep|stop|away)|keep.{0,20}away"]), ("gold is unreactive / does not react with oxygen", ["gold.{0,40}(unreactive|not react|doesn't react)|inert"])],
     "Sodium is very reactive and reacts quickly with oxygen and water in the air, so it is kept under oil to keep air away. Gold is unreactive and does not react with oxygen.", need=2),
  mc("s8u06s1p23", "H", "O1", "Iron is extracted by heating its ore with carbon, but sodium is not. Why?", "Sodium is more reactive than carbon, so carbon cannot remove oxygen from it", [("Sodium has no ore", "Sodium is found in compounds."), ("Carbon is too expensive", "That is not the reason."), ("Sodium is less reactive than iron", "Sodium is more reactive.")]),
 ],
 "6.2": [
  gd("s8u06s2p21", "M", "O2", "How does each metal react with water?", ["Reaction"],
     [("Potassium", ["Violently with cold water"]), ("Magnesium", ["Slowly with cold water, faster with steam"]), ("Copper", ["No reaction"])], extra=[]),
  mc("s8u06s2p22", "H", "O2", "Universal Indicator is added to the water after calcium has reacted. It turns purple. Why?", "Calcium hydroxide is an alkali", [("Hydrogen is an acid", "Hydrogen gas is not an acid."), ("Calcium is an acid", "Calcium is a metal."), ("The water is neutral", "Purple shows alkaline.")]),
  ex("s8u06s2p23", "H", "O2", "Describe how to test the gas given off when calcium reacts with water.",
     [("collect the gas in a test tube", ["collect|test tube"]), ("hold a lighted splint at the mouth", ["lighted|lit|splint"]), ("squeaky pop shows hydrogen", ["pop"])],
     "Collect the gas in an upside-down test tube, then hold a lighted splint at its mouth. A squeaky pop shows the gas is hydrogen.", need=2),
 ],
 "6.3": [
  mc("s8u06s3p21", "M", "O3", "Use the graph. Which metal reacts faster with the acid?", "Magnesium", [("Zinc", "Zinc's line is less steep."), ("Both the same", "The lines are different."), ("Neither reacts", "Both make hydrogen.")], fig=H2, skill="Data"),
  nm("s8u06s3p22", "H", "O3", "Use the graph. How much more hydrogen had magnesium made than zinc after 20 s?", 33, "cm³", tol=1, units=["cm³", "cm3"], fig=H2, skill="Data"),
  mt("s8u06s3p23", "H", "O3", "Match the reactants to the salt formed.", [("Zinc + sulfuric acid", "zinc sulfate"), ("Magnesium + hydrochloric acid", "magnesium chloride"), ("Iron + hydrochloric acid", "iron chloride"), ("Magnesium + nitric acid", "magnesium nitrate")]),
 ],
 "6.4": [
  mc("s8u06s4p21", "M", "O4", "Use the bar chart. Which metal displaced copper most vigorously?", "Magnesium", [("Zinc", "8 °C is less than 12 °C."), ("Iron", "Only 4 °C."), ("Copper", "Copper cannot displace itself.")], fig=DISP, skill="Data"),
  ex("s8u06s4p22", "H", "O4", "Use the bar chart. Explain why copper in copper sulfate gives no temperature rise.",
     [("no reaction happens", ["no reaction|does not react|doesn't react|nothing"]), ("a metal cannot displace itself / is not more reactive than itself", ["itself|same metal|not more reactive"])],
     "No reaction happens, because copper is not more reactive than itself, so it cannot displace copper from copper sulfate.", fig=DISP),
  gd("s8u06s4p23", "H", "O4", "Will a displacement reaction happen?", ["Reaction?"],
     [("Iron + copper sulfate", ["Yes"]), ("Copper + iron sulfate", ["No"]), ("Magnesium + zinc sulfate", ["Yes"]), ("Silver + copper sulfate", ["No"])], extra=[]),
 ],
}
NEW_ADV = {
 "6.4": [adv(ex("s8u06s4a05", "VH", "O4", "In a class practical, metal W reacts with zinc chloride, iron nitrate and copper sulfate, but not with magnesium nitrate. Place W in the reactivity series of magnesium, zinc, iron and copper, and explain your reasoning.",
     [("W is between magnesium and zinc", ["between magnesium and zinc|below magnesium.{0,20}above zinc|after magnesium"]), ("W displaces zinc, iron and copper, so it is more reactive than them", ["displac|more reactive than (zinc|iron|copper)"]), ("W cannot displace magnesium, so it is less reactive than magnesium", ["less reactive than magnesium|not.{0,20}magnesium"])],
     "W displaces zinc, iron and copper from their salts, so it is more reactive than all three, but it cannot displace magnesium, so it is less reactive than magnesium. W goes between magnesium and zinc.", need=2, src=src("SRC-RSCDISP")))],
}

from tests_stage8_unit06_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
