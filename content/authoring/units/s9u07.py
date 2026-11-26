# -*- coding: utf-8 -*-
"""Stage 9 Unit 7 – Salts. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Chemistry"
BLURB = "What salts are, naming the salt made by an acid, and preparing salts from bases, carbonates and metals, including making copper sulfate crystals."
OBJECTIVES = {
    "O1": {"sec": "7.1", "code": "9Cc.03", "codeNote": "salts", "t": "Describe a salt as an ionic compound in which the hydrogen of an acid is replaced by a metal or ammonium ion, and give uses of salts."},
    "O2": {"sec": "7.1", "code": "9Cc.03", "codeNote": "naming", "t": "Write word equations for acid + base and name the salt made by each acid."},
    "O3": {"sec": "7.2", "code": "9Cc.03", "codeNote": "carbonates and metals", "t": "Write word equations for acids with metal carbonates and with metals."},
    "O4": {"sec": "7.2", "code": "9Cc.03, 9TWSp.04", "codeNote": "preparation", "t": "Describe and explain how to prepare a pure, dry sample of a soluble salt."},
}
SECTIONS = [
    {"id": "7.1", "title": "What are salts?", "objs": ["O1", "O2"]},
    {"id": "7.2", "title": "How are salts prepared?", "objs": ["O3", "O4"]},
]
u = Unit(9, 7)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 7.1
u.sec("7.1", "O1")
u.gd("r", "Which type of salt does each acid make?", "Salt", [("Hydrochloric acid", "Chloride"), ("Sulfuric acid", "Sulfate"), ("Nitric acid", "Nitrate")], o="O2")
u.tb("r", "Name the salt. Complete the table.", ["Acid", "Base", "Salt"], [["Hydrochloric acid", "Potassium hydroxide", B("potassium chloride")], ["Sulfuric acid", "Copper oxide", B("copper sulfate")]], o="O2")
u.gd("r", "Match each salt to its use.", "Use", [("Ammonium nitrate", "Fertiliser"), ("Calcium sulfate", "Plaster casts"), ("Sodium hydrogen carbonate", "Baking soda")])
u.ex("r", "Explain what a salt is, using sodium chloride as an example.", [("ionic compound", ["ionic|ions"]), ("positive sodium and negative chloride ions", ["sodium.*chloride|positive.*negative"]), ("hydrogen of acid replaced by metal", ["hydrogen.*replac|replac"])],
     "A salt is an ionic compound formed when the hydrogen ions of an acid are replaced by metal or ammonium ions. Sodium chloride contains positive sodium ions and negative chloride ions.")
u.mc("r", "Acid + base →", "salt + water", ["salt + hydrogen", "salt + carbon dioxide", "acid + water"], o="O2")
u.mc("r", "Every acid contains…", "hydrogen ions", ["metal ions", "hydroxide ions", "chloride ions only"])
u.mc("r", "In a salt, the metal comes from…", "the base", ["the acid", "the water", "the air"], o="O2", d="H")
u.mc("r", "Copper oxide does not dissolve in water. Can it still be used to make a salt?", "Yes, insoluble bases still react with acids", ["No, only alkalis react", "No, it is a metal", "Yes, but only with water"], o="O2", d="VH")
mcs("p", [
    ("Table salt is…", "sodium chloride", ["calcium sulfate", "ammonium nitrate", "copper sulfate"]),
    ("Salt can be obtained by evaporating…", "seawater", ["vinegar", "oil", "milk"]),
    ("Salt is spread on winter roads to…", "melt ice", ["make them dry", "add colour", "make them slippery"]),
    ("Salt preserves food by…", "stopping microbes growing", ["adding vitamins", "freezing it", "adding water"]),
    ("Baking soda is…", "sodium hydrogen carbonate", ["sodium chloride", "calcium sulfate", "ammonium nitrate"]),
    ("Plaster casts for broken bones use…", "calcium sulfate", ["sodium chloride", "copper sulfate", "potassium nitrate"]),
    ("Fertilisers often contain…", "ammonium nitrate", ["sodium hydrogen carbonate", "calcium sulfate", "gold"]),
    ("Bases are metal oxides and metal…", "hydroxides", ["chlorides", "nitrates", "sulfates"], "O2"),
    ("A base that dissolves in water is an…", "alkali", ["acid", "salt", "indicator"], "O2"),
    ("Sodium hydroxide is an example of an…", "alkali", ["acid", "insoluble base", "salt"], "O2"),
    ("Nitric acid makes salts called…", "nitrates", ["sulfates", "chlorides", "carbonates"], "O2"),
    ("Sulfuric acid makes salts called…", "sulfates", ["nitrates", "chlorides", "oxides"], "O2"),
    ("Hydrochloric acid makes salts called…", "chlorides", ["sulfates", "nitrates", "hydroxides"], "O2"),
    ("Hydrochloric acid + sodium hydroxide →", "sodium chloride + water", ["sodium sulfate + water", "sodium chloride + hydrogen", "sodium nitrate + water"], "O2"),
    ("A salt can contain ammonium ions instead of…", "metal ions", ["hydrogen gas", "oxygen atoms", "electrons"]),
])
u.mt("p", "Match the acid and base to the salt.", [("Nitric acid + sodium hydroxide", "sodium nitrate"), ("Sulfuric acid + magnesium oxide", "magnesium sulfate"), ("Hydrochloric acid + calcium hydroxide", "calcium chloride")], o="O2")
u.ms("p", "Select ALL the bases.", ["Copper oxide", "Sodium hydroxide", "Magnesium oxide"], ["Hydrochloric acid", "Sodium chloride"], o="O2")
u.od("p", "Order the ways salt is obtained from least to most energy needed (simplified).", ["Collected from salt pans dried by the Sun", "Pumping water into underground beds", "Mining rock salt with machines"])
u.ex("a", "Name the acid and base you would use to make potassium nitrate, and write the word equation.", [("nitric acid", ["nitric"]), ("potassium hydroxide (or oxide)", ["potassium hydroxide|potassium oxide"]), ("→ potassium nitrate + water", ["potassium nitrate.*water"])],
     "Use nitric acid and potassium hydroxide: nitric acid + potassium hydroxide → potassium nitrate + water.", o="O2")
u.mc("a", "Which acid and base make zinc sulfate?", "Sulfuric acid and zinc oxide", ["Hydrochloric acid and zinc oxide", "Nitric acid and zinc hydroxide", "Sulfuric acid and sodium hydroxide"], o="O2", skill="Application")
u.mc("a", "Why is the reaction of an acid with a base called neutralisation?", "The hydrogen ions of the acid are used up, so the solution becomes neutral", ["It makes the acid stronger", "It produces only hydrogen", "It makes the solution alkaline"], o="O2", skill="Reasoning")
u.mc("a", "Ammonium chloride is a salt that contains no metal. How is this possible?", "The ammonium ion replaces the hydrogen ion instead of a metal", ["Chlorine is a metal", "It is not really a salt", "Ammonium is an acid"], skill="Reasoning")
u.stop("But table salt is just one of many salts!", "Salt is used on winter roads to…", "melt ice", ["make them darker", "add grip by freezing", "dry them"])
u.stop("sodium hydrogen carbonate is baking soda", "Calcium sulfate is used in…", "plaster casts", ["baking soda", "fertiliser", "table salt"])
u.stop("acid plus base gives salt plus water", "Acid + base gives salt +…", "water", ["hydrogen", "carbon dioxide", "oxygen"], o="O2")
u.stop("nitric makes nitrates", "Hydrochloric acid makes salts called…", "chlorides", ["sulfates", "nitrates", "carbonates"], o="O2")

# ---------------------------------------------------------------- 7.2
u.sec("7.2", "O3")
u.gd("r", "Which products form?", "Products", [("Acid + base", "Salt + water"), ("Acid + metal carbonate", "Salt + water + carbon dioxide"), ("Acid + metal", "Salt + hydrogen")])
u.od("r", "Order the steps to make copper sulfate crystals.", ["Warm dilute sulfuric acid", "Add copper carbonate until some is left over", "Filter off the excess", "Heat the filtrate to make a saturated solution", "Leave to cool and crystallise", "Filter and dry the crystals"], o="O4")
u.tb("r", "Name the salt. Complete the table.", ["Acid", "Reacts with", "Salt"], [["Hydrochloric acid", "Zinc", B("zinc chloride")], ["Sulfuric acid", "Magnesium", B("magnesium sulfate")]])
u.ex("r", "Explain why excess copper carbonate is added and then filtered off when making copper sulfate.", [("excess makes sure all the acid reacts / is used up", ["all.*acid|used up|react"]), ("filtering removes unreacted solid", ["filter|remov|unreacted"]), ("leaves pure copper sulfate solution", ["pure|only|solution"])],
     "Adding excess copper carbonate makes sure all the acid is used up. Filtering then removes the unreacted solid, leaving only copper sulfate solution.", o="O4")
u.mc("r", "Acid + metal carbonate →", "salt + water + carbon dioxide", ["salt + hydrogen", "salt + water", "salt + oxygen"])
u.mc("r", "Acid + metal →", "salt + hydrogen", ["salt + water", "salt + carbon dioxide", "metal oxide"])
u.mc("r", "Why don't we make salts by adding sodium to acid?", "Sodium reacts too violently", ["Sodium does not react", "Sodium makes no salt", "Sodium is a non-metal"], d="H")
u.mc("r", "Why is the solution heated only until it is saturated, then left to cool?", "Crystals form slowly as it cools, giving larger, purer crystals", ["To evaporate the salt", "To destroy the crystals", "To make hydrogen"], o="O4", d="VH")
mcs("p", [
    ("A seashell is mainly…", "calcium carbonate", ["sodium chloride", "copper sulfate", "magnesium oxide"]),
    ("A seashell in vinegar…", "fizzes", ["freezes", "turns blue", "glows"]),
    ("The gas made when an acid reacts with a carbonate is…", "carbon dioxide", ["hydrogen", "oxygen", "chlorine"]),
    ("The gas made when an acid reacts with a metal is…", "hydrogen", ["carbon dioxide", "oxygen", "nitrogen"]),
    ("Sulfuric acid + copper carbonate →", "copper sulfate + water + carbon dioxide", ["copper sulfate + hydrogen", "copper chloride + water", "copper + sulfur"]),
    ("Hydrochloric acid + zinc →", "zinc chloride + hydrogen", ["zinc sulfate + hydrogen", "zinc chloride + water", "zinc oxide"]),
    ("Which metal is suitable for making salts with acid?", "Magnesium", ["Gold", "Potassium", "Silver"]),
    ("Copper does not react with dilute acids because it is…", "unreactive", ["too reactive", "a non-metal", "a gas"]),
    ("The liquid that passes through filter paper is the…", "filtrate", ["residue", "solvent", "precipitate"], "O4"),
    ("Copper sulfate solution is…", "blue", ["green", "colourless", "red"], "O4"),
    ("A saturated solution…", "cannot dissolve any more solute", ["has no solute", "is pure water", "is a gas"], "O4"),
    ("Crystals are dried on…", "filter paper", ["a Bunsen flame", "ice", "a magnet"], "O4"),
    ("Copper carbonate is added a little at a time to…", "stop it frothing over", ["make it cold", "change its colour", "make hydrogen"], "O4"),
    ("The test for carbon dioxide is that it turns limewater…", "milky", ["blue", "pink", "clear"]),
    ("The test for hydrogen is a lit splint that…", "makes a squeaky pop", ["relights", "turns green", "goes out silently always"]),
])
u.ms("p", "Select ALL the products of hydrochloric acid + calcium carbonate.", ["Calcium chloride", "Water", "Carbon dioxide"], ["Hydrogen", "Calcium sulfate"])
u.mt("p", "Match the step to its reason.", [("Add excess solid", "use up all the acid"), ("Filter", "remove unreacted solid"), ("Heat gently", "evaporate some water")], o="O4")
u.gd("p", "Which gas is produced?", "Gas", [("Zinc + sulfuric acid", "Hydrogen"), ("Copper carbonate + nitric acid", "Carbon dioxide"), ("Magnesium + hydrochloric acid", "Hydrogen")])
u.ex("a", "Describe how to make a pure, dry sample of zinc chloride from zinc and hydrochloric acid.", [("add excess zinc to acid until fizzing stops", ["excess|fizz|stop"]), ("filter off unreacted zinc", ["filter"]), ("evaporate / crystallise, dry crystals", ["evaporat|heat|crystal|dry"])],
     "Add zinc to hydrochloric acid until no more fizzing and some zinc is left. Filter off the excess zinc, heat the filtrate to make a saturated solution, leave it to crystallise, then filter and dry the crystals.", o="O4")
u.nm("a", "Copper carbonate is added to 50 cm³ of acid. 2.4 g of copper carbonate is added and 0.4 g is left over. What mass reacted?", 2.0, "g", o="O4")
u.mc("a", "Why should a salt not be heated to dryness in the evaporating dish?", "The crystals can spit and may decompose; slow cooling gives better crystals", ["It makes more acid", "It produces hydrogen", "It turns the salt into a metal"], o="O4", skill="Reasoning")
u.mc("a", "A student wants magnesium nitrate. Which reagents are best?", "Magnesium oxide and nitric acid", ["Magnesium and sulfuric acid", "Magnesium chloride and water", "Nitric acid and copper"], skill="Application")
u.stop("Sulfuric acid and copper carbonate make copper sulfate", "Acid + metal carbonate gives salt, water and…", "carbon dioxide", ["hydrogen", "oxygen", "nitrogen"])
u.stop("sodium and potassium are too violent", "Acid + metal gives salt +…", "hydrogen", ["water", "carbon dioxide", "oxygen"])
u.stop("making a saturated solution", "Excess copper carbonate is added to make sure…", "all the acid is used up", ["the solution is red", "hydrogen forms", "the salt evaporates"], o="O4")

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Salts", "sec": None, "kids": [
    {"id": "wh", "t": "What is a salt?", "d": "Ionic compound • H⁺ of acid replaced by metal or ammonium", "obj": "O1", "sec": "7.1"},
    {"id": "us", "t": "Uses", "d": "Fertiliser • Plaster casts • Baking soda • Food", "obj": "O1", "sec": "7.1"},
    {"id": "nm", "t": "Naming", "d": "Hydrochloric → chlorides • Sulfuric → sulfates • Nitric → nitrates", "obj": "O2", "sec": "7.1"},
    {"id": "rx", "t": "Reactions", "d": "Acid + base → salt + water • + carbonate → + CO₂ • + metal → salt + hydrogen", "obj": "O3", "sec": "7.2"},
    {"id": "pr", "t": "Preparing", "d": "Excess solid • Filter • Evaporate • Crystallise • Dry", "obj": "O4", "sec": "7.2"},
]}
