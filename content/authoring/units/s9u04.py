# -*- coding: utf-8 -*-
"""Stage 9 Unit 4 – The Structure of the Atom and the Periodic Table. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Chemistry"
BLURB = "Protons, neutrons and electrons, atomic and mass numbers, electron shells, and how groups, periods and Group 1 trends are shown in the Periodic Table."
OBJECTIVES = {
    "O1": {"sec": "4.1", "code": "9Cm.01", "codeNote": "atomic structure", "t": "Describe the nuclear model of the atom and use atomic and mass numbers to find protons, neutrons and electrons."},
    "O2": {"sec": "4.1", "code": "9Cm.01", "codeNote": "electronic structure", "t": "Write the electronic structure of the first 20 elements."},
    "O3": {"sec": "4.2", "code": "9Cm.01", "codeNote": "groups and periods", "t": "Explain that elements in the same group have the same number of outer electrons and similar properties."},
    "O4": {"sec": "4.2", "code": "9Cp.01", "codeNote": "", "t": "Describe and explain the trends in Group 1 and the reaction of alkali metals with water."},
}
SECTIONS = [
    {"id": "4.1", "title": "The Periodic Table", "objs": ["O1", "O2"]},
    {"id": "4.2", "title": "More about the Periodic Table", "objs": ["O3", "O4"]},
]
u = Unit(9, 4)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 4.1
u.sec("4.1", "O1")
u.tb("r", "Complete the table for each atom.", ["Element", "Atomic number", "Mass number", "Protons", "Neutrons", "Electrons"], [["Carbon", "6", "12", "6", B(6), B(6)], ["Sodium", "11", "23", B(11), B(12), B(11)]])
u.gd("r", "Where is each particle and what is its charge?", "Charge", [("Proton (in nucleus)", "Positive"), ("Neutron (in nucleus)", "Neutral"), ("Electron (in shells)", "Negative")])
u.gd("r", "Electronic structures.", "Structure", [("Carbon (6 electrons)", "2, 4"), ("Nitrogen (7 electrons)", "2, 5"), ("Magnesium (12 electrons)", "2, 8, 2"), ("Phosphorus (15 electrons)", "2, 8, 5")], o="O2")
u.ex("r", "Explain what Rutherford's gold foil experiment showed about atoms.", [("most alpha particles passed through – mostly empty space", ["most|empty space|through"]), ("some bounced back", ["bounce|back|deflect"]), ("tiny dense (positive) nucleus", ["nucleus|dense"])],
     "Most alpha particles passed straight through, so the atom is mostly empty space. A few bounced back, so there must be a tiny, dense, positive nucleus.")
u.mc("r", "The atomic number is the number of…", "protons", ["neutrons", "protons plus neutrons", "shells"])
u.mc("r", "The mass number is the number of…", "protons plus neutrons", ["protons only", "electrons only", "electrons plus neutrons"])
u.mc("r", "Why is an atom electrically neutral?", "It has equal numbers of protons and electrons", ["It has no particles", "Neutrons cancel electrons", "It has more neutrons than protons"], d="H")
u.mc("r", "The first shell holds up to 2 electrons and the second up to 8. What is the structure of an atom with 11 electrons?", "2, 8, 1", ["2, 9", "8, 3", "2, 2, 7"], o="O2", d="VH")
mcs("p", [
    ("The nucleus contains…", "protons and neutrons", ["electrons only", "protons and electrons", "neutrons and electrons"]),
    ("Electrons move around the nucleus in…", "shells", ["the nucleus", "groups", "periods"]),
    ("Most of an atom is…", "empty space", ["solid nucleus", "electrons", "neutrons"]),
    ("Protons and neutrons together are called…", "nucleons", ["electrons", "ions", "isotopes only"]),
    ("Before Rutherford, the atom was pictured as a…", "plum pudding", ["solar system", "double helix", "empty box"]),
    ("Rutherford fired … at gold foil.", "alpha particles", ["electrons", "light", "neutrons"]),
    ("There are over … elements.", "100", ["10", "1000", "20"]),
    ("Each element on the Periodic Table shows its symbol, name, atomic number and…", "mass number", ["colour", "boiling point only", "price"]),
    ("The number of electrons in an atom equals the number of…", "protons", ["neutrons", "nucleons", "shells"]),
    ("To see individual atoms, scientists use…", "electron microscopes", ["light microscopes", "magnifying glasses", "telescopes"]),
    ("The first electron shell holds up to … electrons.", "2", ["8", "18", "1"], "O2"),
    ("The second shell holds up to … electrons.", "8", ["2", "4", "18"], "O2"),
    ("The last number in an electronic structure tells you…", "the number of outer-shell electrons", ["the mass number", "the number of neutrons", "the period"], "O2"),
    ("Neutrons have … charge.", "no", ["positive", "negative", "double"]),
    ("Hydrogen fuel burns to release only…", "water vapour and heat", ["carbon dioxide", "smoke", "sulfur dioxide"]),
])
u.nm("p", "An atom has atomic number 9 and mass number 19. How many neutrons does it have?", 10, "neutrons")
u.mt("p", "Match the element to its electronic structure.", [("Oxygen (8)", "2, 6"), ("Neon (10)", "2, 8"), ("Aluminium (13)", "2, 8, 3")], o="O2")
u.od("p", "Order the models of the atom in time.", ["Plum pudding model", "Rutherford's nuclear model", "Model with electron shells"])
u.ex("a", "Chlorine has atomic number 17 and mass number 35. Give its numbers of protons, neutrons and electrons, and its electronic structure.", [("17 protons and 17 electrons", ["17"]), ("18 neutrons", ["18"]), ("2, 8, 7", ["2,? ?8,? ?7"])],
     "Chlorine has 17 protons and 17 electrons, 35 − 17 = 18 neutrons, and electronic structure 2, 8, 7.", o="O2")
u.nm("a", "Calcium has atomic number 20 and mass number 40. How many electrons are in its outer shell? (Structure 2, 8, 8, …)", 2, "electrons", o="O2")
u.mc("a", "Why did Rutherford conclude the nucleus is positive?", "Positive alpha particles were repelled and bounced back from it", ["Alpha particles were attracted", "Gold is a metal", "Electrons are positive"], skill="Reasoning")
u.mc("a", "Two atoms both have 6 protons but 6 and 8 neutrons. They are…", "atoms of the same element, carbon, with different mass numbers", ["different elements", "ions", "molecules"], skill="Reasoning")
u.stop("Atoms must have a tiny, dense nucleus", "Rutherford's experiment showed that atoms have…", "a tiny, dense nucleus", ["no nucleus", "a plum pudding", "no empty space"])
u.stop("so it's electrically neutral", "The nucleus contains…", "protons and neutrons", ["electrons", "protons and electrons", "only neutrons"])
u.stop("which is 6 neutrons", "Mass number is the number of…", "protons plus neutrons", ["protons only", "electrons", "shells"])
u.stop("Nitrogen, with 7 electrons, is 2, 5", "The first shell can hold up to … electrons.", "2", ["8", "4", "18"], o="O2")

# ---------------------------------------------------------------- 4.2
u.sec("4.2", "O3")
u.gd("r", "Group 1 electronic structures.", "Structure", [("Lithium", "2, 1"), ("Sodium", "2, 8, 1"), ("Potassium", "2, 8, 8, 1")])
u.tb("r", "Group 1 melting points (°C). Complete the differences.", ["Metal", "Melting point (°C)", "Drop from the metal above (°C)"], [["Lithium", "181", "–"], ["Sodium", "98", B(83)], ["Potassium", "63", B(35)]], o="O4")
u.gd("r", "How does each alkali metal react with water?", "Reaction", [("Lithium", "Fizzes gently"), ("Sodium", "Fizzes vigorously"), ("Potassium", "Lilac flame")], o="O4")
u.ex("r", "Explain why sodium and potassium have similar chemical properties.", [("same group / Group 1", ["group"]), ("same number of outer electrons / one", ["one|1|outer"])],
     "Sodium and potassium are both in Group 1, so they both have one electron in their outer shell, which gives them similar chemical properties.")
u.mc("r", "Rows in the Periodic Table are called…", "periods", ["groups", "shells", "families of metals only"])
u.mc("r", "Columns in the Periodic Table are called…", "groups", ["periods", "rows", "nucleons"])
u.mc("r", "Sodium + water →", "sodium hydroxide + hydrogen", ["sodium oxide + oxygen", "sodium chloride + water", "sodium + oxygen"], o="O4", d="H")
u.mc("r", "Going down Group 1, reactivity…", "increases", ["decreases", "stays the same", "drops to zero"], o="O4", d="VH")
mcs("p", [
    ("Group 1 metals are also called…", "alkali metals", ["noble gases", "halogens", "transition metals"], "O4"),
    ("Group 1 metals have … outer electron(s).", "one", ["two", "eight", "no"], "O4"),
    ("Going down Group 1, the atoms get…", "bigger", ["smaller", "the same size", "lighter"], "O4"),
    ("Going down Group 1, melting points…", "decrease", ["increase", "stay the same", "double"], "O4"),
    ("The gas made when an alkali metal reacts with water is…", "hydrogen", ["oxygen", "carbon dioxide", "chlorine"], "O4"),
    ("Metal hydroxide solutions are…", "alkaline", ["acidic", "neutral", "pure water"], "O4"),
    ("Potassium reacting with water gives a … flame.", "lilac", ["green", "blue-black", "yellow-green"], "O4"),
    ("Which is the least reactive alkali metal of these?", "Lithium", ["Sodium", "Potassium", "They are all equal"], "O4"),
    ("Elements in the same group have similar…", "chemical properties", ["mass numbers", "colours always", "numbers of neutrons"]),
    ("Elements in the same group have the same number of…", "outer-shell electrons", ["neutrons", "shells", "protons"]),
    ("Lithium, sodium and potassium are in…", "Group 1", ["Group 2", "Group 7", "Period 1"]),
    ("Elements in the same period have the same number of…", "occupied electron shells", ["outer electrons", "protons", "neutrons"]),
    ("The number of the period an element is in tells you…", "how many shells its atoms have", ["its group", "its mass", "its charge"]),
    ("Alkali metals are stored under oil because…", "they react with air and water", ["they are heavy", "they are gases", "they melt in water only"], "O4"),
    ("Boiling points going down Group 1…", "decrease", ["increase", "stay the same", "double"], "O4"),
])
u.ms("p", "Select ALL the products when potassium reacts with water.", ["Potassium hydroxide", "Hydrogen"], ["Oxygen", "Carbon dioxide", "Potassium chloride"], o="O4")
u.mt("p", "Match the term to its meaning.", [("Group", "column of elements"), ("Period", "row of elements"), ("Alkali metal", "Group 1 element")])
u.od("p", "Order the alkali metals from least to most reactive.", ["Lithium", "Sodium", "Potassium"], o="O4")
u.ex("a", "Rubidium is below potassium in Group 1. Predict how it reacts with water and its melting point, and explain.", [("reacts more violently / explosively", ["more|violent|explos|faster"]), ("lower melting point", ["lower|less"]), ("trend continues down group", ["trend|down the group|further down"])],
     "Rubidium reacts even more violently than potassium, and its melting point is lower, because reactivity increases and melting points decrease going down Group 1.", o="O4")
u.mc("a", "Why does reactivity increase down Group 1?", "The outer electron is further from the nucleus, so it is lost more easily", ["Atoms get smaller", "There are more outer electrons", "The nucleus gets weaker charge"], o="O4", skill="Reasoning")
u.mc("a", "An element has structure 2, 8, 2. Which group and period is it in?", "Group 2, Period 3", ["Group 3, Period 2", "Group 8, Period 2", "Group 2, Period 2"], skill="Application")
u.mc("a", "Universal indicator is added after sodium reacts with water. What colour does it turn?", "Purple or blue, because sodium hydroxide is alkaline", ["Red, because it is acidic", "Green, because it is neutral", "Colourless"], o="O4", skill="Reasoning")
u.stop("so they have similar chemical properties", "Columns in the Periodic Table are called…", "groups", ["periods", "shells", "rows"])
u.stop("the atoms get bigger down the group", "How many outer electrons does a Group 1 atom have?", "One", ["Two", "Eight", "None"], o="O4")
u.stop("Reactivity increases down the group", "Sodium reacting with water makes sodium hydroxide and…", "hydrogen", ["oxygen", "chlorine", "carbon dioxide"], o="O4")

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "The atom and the Periodic Table", "sec": None, "kids": [
    {"id": "md", "t": "Model of the atom", "d": "Plum pudding → Rutherford's nucleus • Mostly empty space", "obj": "O1", "sec": "4.1"},
    {"id": "pt", "t": "Particles", "d": "Protons +, neutrons 0, electrons − • Atomic number • Mass number", "obj": "O1", "sec": "4.1"},
    {"id": "es", "t": "Electron shells", "d": "2, then 8, then 8 • e.g. Mg 2, 8, 2", "obj": "O2", "sec": "4.1"},
    {"id": "gp", "t": "Groups and periods", "d": "Same group = same outer electrons • Similar properties", "obj": "O3", "sec": "4.2"},
    {"id": "g1", "t": "Group 1", "d": "Metal + water → hydroxide + hydrogen • More reactive down • Lower melting points", "obj": "O4", "sec": "4.2"},
]}
