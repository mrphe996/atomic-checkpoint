# -*- coding: utf-8 -*-
"""Stage 7 Unit 7 Properties of Materials — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-AAAS", "name": "AAAS Project 2061 Science Assessment – substances and their properties", "url": "https://assess.bscs.org/science/pages/faq", "use": "Idea for the density/floating Challenge question (7.1)."},
    {"id": "SRC-HSEGHS", "name": "Health and Safety Executive – Hazard pictograms (symbols)", "url": "https://www.hse.gov.uk/chemical-classification/labelling-packaging/hazard-symbols-hazard-pictograms.htm", "use": "Idea for the corrosive/toxic label Challenge question (7.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

NEW_STOPS = {
 "u7n71p": dict(note="Paused before the spoons warm up: steel, wood, plastic, each with a bead of butter.",
   q=mc("u7n71p_q", "M", "O1", "PREDICT: which butter bead will melt and fall first?", ("The one on the steel spoon", "Good prediction – now watch."),
        [("The one on the wooden spoon", "Watch carefully."), ("The one on the plastic spoon", "Watch carefully."), ("All at the same time", "The materials are different.")], skill="Prediction"),
   twin=mc("u7n71p_t", "M", "O1", "A material that lets heat pass through easily is a…", "thermal conductor", [("thermal insulator", ""), ("electrical insulator", ""), ("magnet", "")])),
 "u7n71e": dict(note="Paused after only the steel bead fell.",
   q=ex("u7n71e_q", "H", "O1", "EXPLAIN the result, and say why saucepans have plastic handles.",
        [("steel / metal is a good thermal conductor", ["metal|steel|conduct"]), ("wood / plastic are thermal insulators", ["insulat|wood|plastic"]), ("handles stay cool so you don't burn your hand", ["cool|burn|hold|safe|hand"])],
        "Steel is a metal and a good thermal conductor, so heat reached the butter quickly. Wood and plastic are insulators. Saucepan handles are plastic so they stay cool enough to hold.", need=2),
   twin=mc("u7n71e_t", "H", "O1", "Why are saucepan bases made of metal?", "Metal conducts heat well to the food", [("Metal is a thermal insulator", ""), ("Metal is light", ""), ("Metal is flammable", "")])),
 "u7n72": dict(note="Paused on the density bar chart.",
   q=mc("u7n72_q", "M", "O1", "A solid block of aluminium (density 2.7 g/cm³) is put in water (1.0 g/cm³). What happens?", ("It sinks", "Yes – it is denser than water."),
        [("It floats", "Only materials less dense than water float."), ("It dissolves", "Aluminium does not dissolve in water."), ("It floats halfway", "It is much denser than water.")], skill="Data"),
   twin=mc("u7n72_t", "M", "O1", "Why does ice float on water?", "It is slightly less dense than liquid water", [("It is colder", ""), ("It is a solid", ""), ("It has air holes only", "")])),
 "u7n73p": dict(note="Paused before the nails are left for a week: A air + water, B dry air, C water without air.",
   q=mc("u7n73p_q", "M", "O2", "PREDICT: which nail will rust?", ("A – air and water", "Good prediction – now watch."),
        [("B – dry air", "Watch carefully."), ("C – water but no air", "Watch carefully."), ("All three", "The conditions are different.")], skill="Prediction"),
   twin=mc("u7n73p_t", "M", "O2", "Rusting is a…", "chemical change", [("physical change", ""), ("change of state", ""), ("type of melting", "")])),
 "u7n73e": dict(note="Paused after only nail A rusted.",
   q=ex("u7n73e_q", "H", "O2", "EXPLAIN what the experiment shows about the conditions iron needs to rust.",
        [("needs oxygen / air", ["oxygen|air"]), ("needs water", ["water|moist|wet"]), ("both together (B had no water, C had no air)", ["both|and|together|B.{0,30}water|C.{0,30}air"])],
        "Iron needs both oxygen (from air) and water to rust: tube B had air but no water and tube C had water but no air, so only nail A rusted.", need=2),
   twin=mc("u7n73e_t", "H", "O2", "Which is the best way to stop a bicycle chain rusting?", "Cover it with oil or grease", [("Keep it wet", ""), ("Paint it with water", ""), ("Leave it in the rain", "")])),
 "u7n74": dict(note="Paused after four objects: saucepan, cable, pencil, drill tip.",
   q=mc("u7n74_q", "H", "O3", "Why are window frames often made of plastic or aluminium instead of iron?", ("They do not rust", "Yes – iron would rust outdoors."),
        [("They conduct electricity", "That is not needed for a window frame."), ("They are magnetic", "That is not why they are chosen."), ("They melt easily", "That would be a problem, not a reason.")]),
   twin=mc("u7n74_t", "M", "O3", "Which property makes copper good for wires?", "It conducts electricity and is ductile", [("It is brittle", ""), ("It is an insulator", ""), ("It is flammable", "")])),
 "u7n75": dict(note="Paused on the strength chart: each alloy is stronger than its pure metal.",
   q=ex("u7n75_q", "H", "O4", "Use the particle model to explain why an alloy is stronger than the pure metal.",
        [("alloy has atoms of different sizes", ["different size|different-sized|bigger|smaller|mixed"]), ("layers cannot slide easily", ["layer|slide|slip"])],
        "An alloy contains atoms of different sizes, which disrupt the regular layers, so the layers cannot slide over each other easily."),
   twin=mc("u7n75_t", "M", "O4", "Steel is an alloy of iron with…", "carbon (and sometimes other metals)", [("oxygen", ""), ("water", ""), ("sulfur only", "")])),
}

DROP = {"7.1": ["u7s1p03", "u7s1p09", "u7s1p15"], "7.2": ["u7s2p05", "u7s2p16", "u7s2p12"], "7.3": ["u7s3p01", "u7s3p08", "u7s3p13"], "7.4": ["u7s4p02", "u7s4p11", "u7s4p15"]}
HEATS = {"kind": "barchart", "labels": ["copper", "steel", "glass", "wood", "plastic"], "values": [24, 61, 180, 300, 300], "ymax": 320, "step": 80, "ylabel": "Time for butter to fall (s)", "xlabel": "Rod material (300 = had not fallen after 5 min)"}
RUST = {"kind": "barchart", "labels": ["dry air", "tap water", "salt water"], "values": [0, 12, 31], "ymax": 40, "step": 10, "ylabel": "Mass of rust after 2 weeks (mg)", "xlabel": "Condition"}
NEW_PRAC = {
 "7.1": [
  mc("u7s1p21", "M", "O1", "Use the bar chart. Which material is the best thermal conductor?", "Copper", [("Steel", "Steel took longer than copper."), ("Glass", "Glass took much longer."), ("Wood", "Butter on wood had not fallen.")], fig=HEATS, skill="Data"),
  mc("u7s1p22", "H", "O1", "Use the bar chart. Which TWO materials are thermal insulators?", "Wood and plastic", [("Copper and steel", "These conduct heat well."), ("Glass and copper", "Copper is a good conductor."), ("Steel and wood", "Steel is a conductor.")], fig=HEATS, skill="Data"),
  nm("u7s1p23", "H", "O1", "A stone has a mass of 52 g and a volume of 20 cm³. What is its density?", 2.6, "g/cm³", units=["g/cm³", "g/cm3"], hint="density = mass ÷ volume"),
 ],
 "7.2": [
  mc("u7s2p21", "M", "O2", "Use the bar chart. Under which condition did the nail rust most?", "Salt water", [("Tap water", "Less rust formed than in salt water."), ("Dry air", "No rust formed."), ("All the same", "The bars are different heights.")], fig=RUST, skill="Data"),
  ex("u7s2p22", "H", "O2", "Use the bar chart. Why do cars rust faster in places where salt is spread on icy roads?",
     [("salt water makes iron rust faster", ["salt.{0,40}(faster|more|quick)|more rust"]), ("uses data (31 mg vs 12 mg)", ["31|12|more than"])],
     "Salt water speeds up rusting: 31 mg of rust formed in salt water compared with 12 mg in tap water, so salty road spray makes cars rust faster.", fig=RUST),
  gd("u7s2p23", "H", "O2", "Physical or chemical property?", ["Type"], [("Melting point", ["Physical"]), ("Flammability", ["Chemical"]), ("Density", ["Physical"]), ("Reacts with water", ["Chemical"])], extra=[]),
 ],
 "7.3": [
  gd("u7s3p21", "H", "O3", "Use the data to decide: metal or non-metal?", ["Metal", "Non-metal"],
     [("Shiny, melts at 1455 °C, conducts electricity", ["✓", "✗"]), ("Dull, brittle, melts at 44 °C", ["✗", "✓"]), ("Colourless gas, does not conduct", ["✗", "✓"]), ("Malleable, dense, conducts heat", ["✓", "✗"])]),
  mt("u7s3p22", "H", "O3", "Match each use to the property that makes the material suitable.", [("Copper wires", "conducts electricity"), ("Diamond drill tip", "very hard"), ("Graphite pencil", "layers slide off easily"), ("Aluminium foil", "malleable")]),
  mc("u7s3p23", "H", "O3", "Graphite and diamond are both pure carbon. Why are their properties so different?", "Their carbon atoms are joined together in different ways", [("Diamond contains metal", "Both are pure carbon."), ("Graphite is a mixture", "It is pure carbon."), ("They have different-sized atoms", "All the atoms are carbon atoms.")]),
 ],
 "7.4": [
  mc("u7s4p21", "M", "O4", "Use the bar chart in the video data: how many times stronger is the aluminium alloy (470 MPa) than pure aluminium (90 MPa), roughly?", "About 5 times", [("About 2 times", "470 ÷ 90 is about 5."), ("About 10 times", "470 ÷ 90 is about 5."), ("The same", "The alloy is much stronger.")], skill="Data"),
  gd("u7s4p22", "H", "O4", "Choose the best alloy for each job.", ["Alloy"], [("Hip implant (not toxic, strong, light)", ["Titanium alloy"]), ("Kitchen sink (does not rust)", ["Stainless steel"]), ("Statue that lasts outdoors", ["Bronze"])], extra=["Pure iron"]),
  ex("u7s4p23", "H", "O4", "Pure gold is too soft for jewellery that is worn every day. Explain why jewellers mix it with other metals.",
     [("alloy is harder / stronger", ["hard|strong|tough|scratch"]), ("different-sized atoms stop layers sliding", ["different size|layer|slide|atoms"])],
     "Mixing gold with other metals makes an alloy. The different-sized atoms stop the layers sliding, so the jewellery is harder and does not bend or scratch as easily."),
 ],
}
NEW_ADV = {
 "7.1": [adv(ex("u7s1a5", "VH", "O1", "A large log floats but a small steel nail sinks. A student says 'big things float and small things sink'. Use density to explain why the student is wrong.",
     [("floating depends on density, not size", ["density|dense"]), ("wood is less dense than water; steel is denser", ["wood.{0,40}less|less dense|steel.{0,40}(dens|more)"])],
     "Floating depends on density, not size. Wood is less dense than water, so even a large log floats; steel is denser than water, so even a small nail sinks.", src=src("SRC-AAAS")))],
 "7.2": [adv(ex("u7s2a5", "VH", "O2", "A drain cleaner label shows the corrosive and the toxic pictograms. Give TWO chemical properties these show and one precaution for each.",
     [("corrosive: destroys skin / materials", ["corros|burn|destroy|skin"]), ("toxic: poisonous if swallowed / breathed", ["toxic|poison|swallow|breath"]), ("precautions: gloves / goggles / store locked away / ventilate", ["glove|goggle|lock|child|ventil|away"])],
     "It is corrosive – it can destroy skin and eyes, so wear gloves and goggles. It is toxic – it can poison you if swallowed or breathed, so store it locked away from children and use it with a window open.", need=2, src=src("SRC-HSEGHS")))],
}

from tests_stage7_unit07_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
