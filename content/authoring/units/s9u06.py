# -*- coding: utf-8 -*-
"""Stage 9 Unit 6 – Displacement Reactions. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Chemistry"
BLURB = "Writing word and symbol equations, the reactivity series, and predicting and explaining displacement reactions such as iron in copper sulfate and thermite welding."
OBJECTIVES = {
    "O1": {"sec": "6.1", "code": "9Cc.01", "codeNote": "", "t": "Describe a chemical reaction as a rearrangement of atoms and write word and symbol equations."},
    "O2": {"sec": "6.2", "code": "9Cc.02", "codeNote": "reactivity series", "t": "Use the reactivity series and explain reactivity in terms of losing outer electrons."},
    "O3": {"sec": "6.2", "code": "9Cc.02, 9TWSp.01", "codeNote": "", "t": "Predict and explain displacement reactions and describe their uses."},
}
SECTIONS = [
    {"id": "6.1", "title": "Describing chemical reactions", "objs": ["O1"]},
    {"id": "6.2", "title": "Displacement reactions", "objs": ["O2", "O3"]},
]
u = Unit(9, 6)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 6.1
u.sec("6.1", "O1")
u.gd("r", "Reactant or product? (hydrogen + oxygen → water)", "Role", [("Hydrogen", "Reactant"), ("Oxygen", "Reactant"), ("Water", "Product")])
u.tb("r", "Count the atoms in 2H₂ + O₂ → 2H₂O.", ["Atom", "Left side", "Right side"], [["Hydrogen", "4", B(4)], ["Oxygen", "2", B(2)]])
u.gd("r", "How many atoms of each element are in the formula?", "Number", [("H in H₂O", "2"), ("O in CO₂", "2"), ("C in CH₄", "1"), ("H in CH₄", "4")])
u.ex("r", "Explain what happens to atoms during a chemical reaction.", [("atoms rearrange / bond in new ways", ["rearrang|new way|bond"]), ("no atoms made or destroyed", ["not made|destroy|same atoms|conserv"]), ("products have different properties", ["different|new substance|propert"])],
     "The atoms of the reactants rearrange and bond in new ways to form products with different properties. No atoms are made or destroyed.")
u.mc("r", "In a word equation, reactants are written…", "on the left of the arrow", ["on the right", "above the arrow", "only in symbols"])
u.mc("r", "The arrow in an equation shows…", "the direction of the reaction", ["that the substances are equal", "heat only", "a mixture"])
u.mc("r", "Why are symbol equations useful?", "Chemists all over the world can understand them", ["They use long names", "They show colours", "They are only for metals"], d="H")
u.mc("r", "What does the '2' in front of H₂O in 2H₂ + O₂ → 2H₂O mean?", "Two water molecules", ["Two hydrogen atoms in each molecule", "Two oxygen atoms", "Twice the mass"], d="VH")
mcs("p", [
    ("Substances at the start of a reaction are…", "reactants", ["products", "catalysts", "solvents"]),
    ("Substances made in a reaction are…", "products", ["reactants", "elements only", "mixtures"]),
    ("The formula of water is…", "H₂O", ["HO", "H₂O₂", "OH₂"]),
    ("The formula of oxygen gas is…", "O₂", ["O", "O₃", "2O"]),
    ("The formula of hydrogen gas is…", "H₂", ["H", "2H", "H₂O"]),
    ("Water has … hydrogen atoms for every oxygen atom.", "two", ["one", "three", "four"]),
    ("A word equation uses…", "names of substances", ["only symbols", "diagrams", "numbers only"]),
    ("A symbol equation uses…", "chemical symbols and formulae", ["names only", "pictures", "colours"]),
    ("Products have … properties from the reactants.", "different", ["identical", "no", "the same"]),
    ("In 2H₂ + O₂ → 2H₂O, how many oxygen molecules react?", "One", ["Two", "Four", "None"]),
    ("Which is a word equation?", "magnesium + oxygen → magnesium oxide", ["2Mg + O₂ → 2MgO", "Mg → O", "MgO₂"]),
    ("Carbon + oxygen → …", "carbon dioxide", ["carbon monoxide only", "water", "oxygen"]),
    ("The formula of carbon dioxide is…", "CO₂", ["CO", "C₂O", "O₂C₂"]),
    ("In a balanced equation, the number of each type of atom on both sides is…", "the same", ["different", "doubled", "zero"]),
    ("H₂ + Cl₂ → …", "2HCl", ["HCl", "H₂Cl", "2H + 2Cl"]),
])
u.mt("p", "Match the name to its formula.", [("Water", "H₂O"), ("Carbon dioxide", "CO₂"), ("Methane", "CH₄")])
u.od("p", "Order to write a word equation.", ["Name the reactants", "Put them on the left with +", "Draw the arrow", "Name the products on the right"])
u.ms("p", "Select ALL the reactants in: methane + oxygen → carbon dioxide + water.", ["Methane", "Oxygen"], ["Carbon dioxide", "Water"])
u.ex("a", "Write the word and symbol equations for magnesium burning in oxygen to make magnesium oxide (MgO).", [("magnesium + oxygen → magnesium oxide", ["magnesium.*oxygen.*magnesium oxide"]), ("2Mg + O₂ → 2MgO", ["2mg|o2|o₂|2mgo"])],
     "Magnesium + oxygen → magnesium oxide. 2Mg + O₂ → 2MgO.")
u.tb("a", "Check the balance of CH₄ + 2O₂ → CO₂ + 2H₂O.", ["Atom", "Left", "Right"], [["C", "1", B(1)], ["H", "4", B(4)], ["O", "4", B(4)]])
u.mc("a", "Why must a symbol equation be balanced?", "Atoms are not created or destroyed in a reaction", ["To make it look neat", "Because molecules change size", "Because products weigh more"], skill="Reasoning")
u.mc("a", "Which equation is balanced?", "N₂ + 3H₂ → 2NH₃", ["N₂ + H₂ → NH₃", "N + H₃ → NH₃", "N₂ + 3H₂ → NH₃"], skill="Application")
u.stop("That's a displacement reaction!", "Adding a more reactive metal to remove a toxic metal from water is a … reaction.", "displacement", ["neutralisation", "combustion", "decomposition"])
u.stop("to form two water molecules", "In a reaction, the atoms of the reactants…", "rearrange to form products", ["disappear", "are created", "stay bonded the same way"])
u.stop("the arrow shows the direction of the reaction", "In a word equation, products go…", "on the right", ["on the left", "above the arrow", "nowhere"])

# ---------------------------------------------------------------- 6.2
u.sec("6.2", "O2")
u.od("r", "Order these metals from most to least reactive.", ["Potassium", "Magnesium", "Iron", "Copper", "Gold"])
u.gd("r", "Will a displacement reaction happen?", "Reaction?", [("Copper in silver nitrate", "Yes"), ("Silver in copper nitrate", "No"), ("Magnesium in copper sulfate", "Yes"), ("Zinc in calcium chloride", "No")], o="O3")
u.gd("r", "Iron nail in copper sulfate solution: what do you see?", "Observation", [("On the nail", "Brown coating"), ("Colour of solution", "Turns green")], extra=["Turns blue"], o="O3")
u.ex("r", "Explain why copper displaces silver from silver nitrate solution but silver does not displace copper from copper nitrate.", [("copper more reactive than silver", ["copper.*more reactive|silver.*less reactive"]), ("more reactive element pushes out less reactive", ["push|displace"]), ("silver less reactive – no reaction", ["no reaction|nothing|cannot"])],
     "Copper is more reactive than silver, so it pushes silver out of silver nitrate. Silver is less reactive than copper, so it cannot displace copper and nothing happens.", o="O3")
u.mc("r", "A displacement reaction is when…", "a more reactive element pushes a less reactive one out of its compound", ["two metals mix", "a metal dissolves in water", "an acid reacts with a base"], o="O3")
u.mc("r", "Why does gold jewellery stay shiny?", "Gold is very unreactive", ["Gold is very reactive", "Gold is coated in oil", "Gold is a non-metal"])
u.mc("r", "Why is potassium more reactive than sodium?", "Its outer electron is further from the nucleus, so it is lost more easily", ["It has fewer shells", "It has more outer electrons", "It is smaller"], d="H")
u.mc("r", "In thermite welding, aluminium reacts with iron oxide because…", "aluminium is more reactive than iron, so it takes the oxygen", ["iron is more reactive than aluminium", "aluminium is a non-metal", "iron oxide is a gas"], o="O3", d="VH")
mcs("p", [
    ("The reactivity series lists metals from…", "most to least reactive", ["lightest to heaviest", "cheapest to dearest", "A to Z"]),
    ("Which reacts violently with cold water?", "Potassium", ["Iron", "Copper", "Gold"]),
    ("Gold does not react even with…", "acids", ["air only", "water only", "nothing"]),
    ("A metal's reactivity depends on how easily it…", "loses its outer electrons", ["gains protons", "melts", "conducts heat"]),
    ("Iron reacts with water…", "slowly", ["violently", "explosively", "not at all"]),
    ("If A is more reactive than B, then A + BC →", "AC + B", ["AB + C", "no reaction", "ABC"], "O3"),
    ("Copper in silver nitrate makes the solution turn…", "blue", ["green", "colourless", "red"], "O3"),
    ("The solution turns green when iron displaces copper because … forms.", "iron sulfate", ["copper sulfate", "silver nitrate", "iron oxide"], "O3"),
    ("Thermite welding joins…", "railway rails", ["glass panes", "plastic pipes", "wooden beams"], "O3"),
    ("Thermite produces … iron.", "molten", ["frozen", "powdered", "gaseous"], "O3"),
    ("Which metal can displace copper from copper sulfate?", "Zinc", ["Silver", "Gold", "Platinum"], "O3"),
    ("Which metal cannot displace iron from iron sulfate?", "Copper", ["Magnesium", "Zinc", "Aluminium"], "O3"),
    ("Toxic heavy metals include…", "lead, cadmium and mercury", ["sodium and potassium", "iron and calcium", "oxygen and nitrogen"], "O3"),
    ("Silver crystals appear when … is placed in silver nitrate.", "copper", ["gold", "platinum", "silver"], "O3"),
    ("Calcium is … reactive than zinc.", "more", ["less", "equally", "not"], ),
])
u.ms("p", "Select ALL the metals that would displace copper from copper sulfate.", ["Magnesium", "Zinc", "Iron"], ["Silver", "Gold"], o="O3")
u.mt("p", "Match the reaction to the observation.", [("Copper in silver nitrate", "silver crystals, blue solution"), ("Iron in copper sulfate", "brown coating, green solution"), ("Silver in copper nitrate", "no change")], o="O3")
u.tb("p", "Temperature rise when metals are added to copper sulfate. Complete the table.", ["Metal", "Start (°C)", "End (°C)", "Rise (°C)"], [["Magnesium", "20", "45", B(25)], ["Zinc", "20", "32", B(12)], ["Silver", "20", "20", B(0)]], o="O3")
u.ex("a", "Using the temperature results (magnesium 25 °C rise, zinc 12 °C, silver 0 °C), explain what they show about reactivity.", [("magnesium most reactive – biggest rise", ["magnesium.*(most|biggest|largest)"]), ("zinc less reactive than magnesium", ["zinc"]), ("silver no reaction – less reactive than copper", ["silver.*(no|less)"])],
     "Magnesium gave the biggest rise, so it is the most reactive. Zinc reacted less, so it is less reactive than magnesium. Silver gave no rise because it is less reactive than copper and does not displace it.", o="O3")
u.mc("a", "Scrap iron is used to extract copper from copper sulfate solutions in mines. Why?", "Iron is cheap and more reactive than copper, so it displaces it", ["Iron is less reactive than copper", "Copper is more reactive than iron", "Iron dissolves copper ore"], o="O3", skill="Application")
u.mc("a", "Metal X displaces zinc but not magnesium. Where is X in the reactivity series?", "Between magnesium and zinc", ["Above magnesium", "Below zinc", "Below copper"], skill="Reasoning")
u.mc("a", "Which equation is correct?", "zinc + copper sulfate → zinc sulfate + copper", ["copper + zinc sulfate → copper sulfate + zinc", "zinc + copper sulfate → no reaction", "silver + copper sulfate → silver sulfate + copper"], o="O3", skill="Application")
u.stop("That's why gold and silver jewellery stays shiny", "Which is the least reactive of these?", "Gold", ["Potassium", "Iron", "Sodium"])
u.stop("so its outer electron is further from the nucleus and easier to lose", "A metal's reactivity depends on how easily it loses its…", "outer electrons", ["protons", "neutrons", "nucleus"])
u.stop("because silver is less reactive", "Copper in silver nitrate: what forms?", "Silver crystals and blue copper nitrate", ["Nothing", "Gold", "Copper crystals only"], o="O3")
u.stop("Iron is above copper in the reactivity series", "An iron nail in copper sulfate becomes coated with…", "copper", ["iron oxide", "silver", "sulfur"], o="O3")

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Displacement reactions", "sec": None, "kids": [
    {"id": "rx", "t": "Reactions", "d": "Atoms rearrange • Reactants → products", "obj": "O1", "sec": "6.1"},
    {"id": "eq", "t": "Equations", "d": "Word: hydrogen + oxygen → water • Symbol: 2H₂ + O₂ → 2H₂O", "obj": "O1", "sec": "6.1"},
    {"id": "rs", "t": "Reactivity series", "d": "K > Na > Ca > Mg > Al > Zn > Fe > Cu > Ag > Au • Easier to lose outer electron", "obj": "O2", "sec": "6.2"},
    {"id": "dp", "t": "Displacement", "d": "More reactive pushes out less reactive • A + BC → AC + B", "obj": "O3", "sec": "6.2"},
    {"id": "us", "t": "Uses", "d": "Iron in copper sulfate • Thermite welding • Removing toxic metals", "obj": "O3", "sec": "6.2"},
]}
