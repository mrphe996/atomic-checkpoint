# -*- coding: utf-8 -*-
"""Stage 9 Unit 5 – Chemical Bonding and Structure of Materials. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Chemistry"
BLURB = "Why atoms bond, covalent bonds and molecules, ions and ionic bonds, and how simple, giant covalent and ionic structures decide a substance's properties."
OBJECTIVES = {
    "O1": {"sec": "5.1", "code": "9Cm.02", "codeNote": "stable shells", "t": "Explain that atoms bond to reach a full, stable outer shell."},
    "O2": {"sec": "5.2", "code": "9Cm.02, 9Cm.03", "codeNote": "", "t": "Describe a covalent bond as a shared pair of electrons and draw dot-and-cross diagrams of simple molecules."},
    "O3": {"sec": "5.3", "code": "9Cm.04, 9Cm.05", "codeNote": "", "t": "Describe how ions form and explain an ionic bond as electrostatic attraction."},
    "O4": {"sec": "5.4", "code": "9Cp.04", "codeNote": "", "t": "Relate simple molecular, giant covalent and giant ionic structures to their properties."},
}
SECTIONS = [
    {"id": "5.1", "title": "Chemical bonding", "objs": ["O1"]},
    {"id": "5.2", "title": "Covalent bonding", "objs": ["O2"]},
    {"id": "5.3", "title": "Ionic bonding", "objs": ["O3"]},
    {"id": "5.4", "title": "Structures and properties of covalent and ionic substances", "objs": ["O4"]},
]
u = Unit(9, 5)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 5.1
u.sec("5.1", "O1")
u.gd("r", "Stable (full outer shell) or not?", "Stable?", [("Neon 2, 8", "Stable"), ("Sodium 2, 8, 1", "Not stable"), ("Chlorine 2, 8, 7", "Not stable"), ("Argon 2, 8, 8", "Stable")])
u.tb("r", "How many electrons does each atom need to gain to fill its outer shell of 8?", ["Atom", "Outer electrons", "Electrons needed"], [["Chlorine", "7", B(1)], ["Oxygen", "6", B(2)], ["Nitrogen", "5", B(3)]])
u.gd("r", "Which kind of bond forms?", "Bond", [("Atoms share outer electrons", "Covalent"), ("Atoms lose or gain electrons", "Ionic")], extra=["Metallic"])
u.ex("r", "Explain why Group 18 elements such as neon hardly react.", [("full outer shell", ["full|complete"]), ("stable – no need to gain, lose or share", ["stable|no need|don't need"])],
     "Group 18 atoms already have a full outer shell, a stable arrangement, so they do not need to lose, gain or share electrons.")
u.mc("r", "Electron shells are also called…", "energy levels", ["nuclei", "groups", "periods"])
u.mc("r", "Which part of an atom matters most in bonding?", "The outer shell of electrons", ["The neutrons", "The nucleus", "The inner shell"])
u.mc("r", "Why does sodium react?", "Its outer shell has one electron, so it is not stable", ["It has a full outer shell", "It has no electrons", "It has 8 outer electrons"], d="H")
u.mc("r", "Diamond and coal are both carbon but have very different properties. This is because…", "their atoms are bonded and arranged differently", ["one contains no carbon", "they have different nuclei", "coal has no electrons"], d="VH")
mcs("p", [
    ("Group 18 elements are called…", "noble gases", ["alkali metals", "halogens", "metals"]),
    ("A full outer shell is a … electronic configuration.", "stable", ["reactive", "charged", "broken"]),
    ("Atoms form bonds to get…", "a full outer shell", ["more neutrons", "a bigger nucleus", "fewer protons"]),
    ("Chlorine has … outer electrons.", "seven", ["one", "eight", "two"]),
    ("Sodium has … outer electron(s).", "one", ["seven", "eight", "two"]),
    ("Sharing electrons makes … bonds.", "covalent", ["ionic", "magnetic", "nuclear"]),
    ("Losing or gaining electrons makes … bonds.", "ionic", ["covalent", "hydrogen", "nuclear"]),
    ("Neon's outer shell holds…", "8 electrons", ["1 electron", "7 electrons", "no electrons"]),
    ("Unstable atoms tend to…", "react", ["stay unreacted", "lose protons", "become noble gases"]),
    ("How atoms are joined affects how materials…", "behave", ["are named", "are counted", "smell only"]),
    ("Diamond and coal are both made of…", "carbon", ["silicon", "oxygen", "sodium"]),
    ("Helium is stable with … electrons in its only shell.", "2", ["8", "1", "18"]),
    ("Atoms with nearly full outer shells usually…", "gain electrons", ["lose all electrons", "never react", "share protons"]),
    ("Atoms with one or two outer electrons usually…", "lose them", ["gain six", "never react", "share neutrons"]),
    ("Argon is used in light bulbs because it…", "is unreactive", ["burns easily", "is a metal", "conducts heat best"]),
])
u.mt("p", "Match the atom to its outer electrons.", [("Sodium", "1"), ("Oxygen", "6"), ("Neon", "8")])
u.ms("p", "Select ALL the stable (unreactive) elements.", ["Neon", "Argon", "Helium"], ["Sodium", "Chlorine"])
u.od("p", "Order the atoms by number of outer electrons, fewest first.", ["Sodium", "Carbon", "Oxygen", "Chlorine"])
u.ex("a", "Predict whether magnesium (2, 8, 2) is more likely to lose or gain electrons, and explain.", [("lose", ["lose|give"]), ("two electrons", ["two|2"]), ("easier than gaining six / leaves full shell", ["easier|six|6|full"])],
     "Magnesium is more likely to lose its two outer electrons, because that is easier than gaining six and leaves a full outer shell.")
u.mc("a", "Why is it hard to make neon form compounds?", "Its full outer shell is already stable", ["Neon has no electrons", "Neon is a metal", "Neon's nucleus is negative"], skill="Reasoning")
u.mc("a", "Which pair is most likely to form an ionic bond?", "Potassium and fluorine", ["Hydrogen and chlorine", "Carbon and oxygen", "Neon and argon"], skill="Application")
u.mc("a", "Which pair is most likely to form a covalent bond?", "Nitrogen and hydrogen", ["Sodium and chlorine", "Magnesium and oxygen", "Neon and helium"], skill="Application")
u.stop("That's why they hardly react", "Group 18 atoms hardly react because they have…", "a full outer shell", ["one outer electron", "no nucleus", "seven outer electrons"])
u.stop("making ionic bonds", "Sharing outer electrons makes … bonds.", "covalent", ["ionic", "metallic", "magnetic"])

# ---------------------------------------------------------------- 5.2
u.sec("5.2", "O2")
u.tb("r", "Number of covalent bonds in each molecule. Complete the table.", ["Molecule", "Covalent bonds"], [["Hydrogen, H₂", "1"], ["Water, H₂O", B(2)], ["Methane, CH₄", B(4)]])
u.gd("r", "In a dot-and-cross diagram of hydrogen chloride…", "Shown as", [("Hydrogen's electron", "Cross"), ("Chlorine's electrons", "Dots")], extra=["Circles"])
u.gd("r", "Molecule or not a molecule?", "Type", [("Water, H₂O", "Molecule"), ("Methane, CH₄", "Molecule"), ("A single neon atom", "Not a molecule")])
u.ex("r", "Explain how a water molecule forms using covalent bonds.", [("oxygen has 6 outer electrons, needs 2", ["6|six|needs 2|two more"]), ("shares one pair with each hydrogen", ["share|pair"]), ("all get full outer shells", ["full"])],
     "Oxygen has 6 outer electrons and needs 2 more. It shares one pair of electrons with each of two hydrogen atoms, so all three atoms get full outer shells.")
u.mc("r", "A covalent bond is…", "a shared pair of electrons", ["a lost electron", "a pair of protons", "attraction between ions"])
u.mc("r", "Covalent bonds form between…", "non-metal atoms", ["metal atoms only", "a metal and a non-metal", "noble gas atoms"])
u.mc("r", "Why can carbon form four covalent bonds?", "It has four outer electrons to share", ["It has four protons", "It has four shells", "It is a metal"], d="H")
u.mc("r", "Hydrogen chloride has one covalent bond. Why only one?", "Hydrogen and chlorine each need just one more electron", ["Chlorine has one electron", "Hydrogen has seven electrons", "It is ionic"], d="VH")
mcs("p", [
    ("A group of atoms joined by covalent bonds is a…", "molecule", ["ion", "lattice of ions", "nucleus"]),
    ("In a hydrogen molecule, the two atoms share…", "one pair of electrons", ["two protons", "four electrons", "no electrons"]),
    ("Dot-and-cross diagrams show…", "where electrons come from", ["where neutrons are", "the nucleus size", "the colour of atoms"]),
    ("Methane's formula is…", "CH₄", ["H₂O", "HCl", "CO₂"]),
    ("Water's formula is…", "H₂O", ["CH₄", "HO₂", "H₂"]),
    ("Oxygen needs … more electrons to fill its outer shell.", "2", ["1", "4", "6"]),
    ("Carbon forms many different molecules because it…", "can make four bonds", ["is unreactive", "is a metal", "has one electron"]),
    ("Hydrogen's single shell is full with … electrons.", "2", ["8", "1", "4"]),
    ("Which is a covalent molecule?", "Carbon dioxide", ["Sodium chloride", "Magnesium oxide", "Potassium bromide"]),
    ("In a covalent bond, electrons are…", "shared", ["lost", "gained", "destroyed"]),
    ("A double covalent bond shares…", "two pairs of electrons", ["one electron", "one pair", "two protons"]),
    ("A chlorine molecule, Cl₂, has … covalent bond(s).", "one", ["two", "four", "no"]),
    ("Ammonia, NH₃, has … covalent bonds.", "three", ["one", "two", "four"]),
    ("Nitrogen has … outer electrons.", "5", ["3", "7", "8"]),
    ("Covalent bonds hold atoms together because the shared electrons are attracted to…", "both nuclei", ["neither nucleus", "neutrons only", "other molecules"]),
])
u.mt("p", "Match the molecule to its bonds.", [("H₂", "1 single bond"), ("H₂O", "2 single bonds"), ("CH₄", "4 single bonds")])
u.ms("p", "Select ALL the molecules held by covalent bonds.", ["Water", "Methane", "Hydrogen chloride"], ["Sodium chloride", "Magnesium chloride"])
u.od("p", "Order to describe making a hydrogen molecule.", ["Two hydrogen atoms each have one electron", "They move close together", "They share a pair of electrons", "Both have a full shell"])
u.ex("a", "Explain why the formula of ammonia is NH₃, not NH₂ or NH₄.", [("nitrogen has 5 outer electrons", ["5|five"]), ("needs 3 more", ["3|three"]), ("shares one pair with each of 3 hydrogens", ["share|hydrogen"])],
     "Nitrogen has 5 outer electrons and needs 3 more. It shares one pair with each of three hydrogen atoms, so the formula is NH₃.")
u.mc("a", "Carbon dioxide is O=C=O. How many electrons does carbon share in total?", "4", ["2", "6", "8"], skill="Application")
u.mc("a", "Why don't neon atoms form Ne₂ molecules?", "Each neon atom already has a full outer shell", ["Neon is a metal", "Neon has no electrons", "Neon atoms repel protons"], skill="Reasoning")
u.mc("a", "In a dot-and-cross diagram of methane, how many crosses (hydrogen electrons) are shown?", "4", ["1", "8", "2"], skill="Figure")
u.stop("the other's as crosses", "A covalent bond is a shared pair of…", "electrons", ["protons", "neutrons", "ions"])
u.stop("making a water molecule with two covalent bonds", "How many covalent bonds are in a water molecule?", "Two", ["One", "Three", "Four"])

# ---------------------------------------------------------------- 5.3
u.sec("5.3", "O3")
u.gd("r", "Does the atom lose or gain electrons?", "Change", [("Sodium", "Loses 1"), ("Chlorine", "Gains 1"), ("Magnesium", "Loses 2"), ("Oxygen", "Gains 2")])
u.tb("r", "Metal atoms lose their outer electrons to form ions. Complete the table.", ["Atom", "Electronic structure", "Electrons lost"], [["Sodium", "2, 8, 1", "1"], ["Magnesium", "2, 8, 2", B(2)], ["Aluminium", "2, 8, 3", B(3)]])
u.gd("r", "Cation or anion?", "Ion", [("Sodium ion, Na⁺", "Cation"), ("Chloride ion, Cl⁻", "Anion"), ("Magnesium ion, Mg²⁺", "Cation")])
u.ex("r", "Explain how sodium chloride forms from sodium and chlorine atoms.", [("sodium loses one electron → Na⁺", ["sodium.*los|na\\+|positive"]), ("chlorine gains one electron → Cl⁻", ["chlorine.*gain|cl-|cl⁻|negative"]), ("opposite charges attract – ionic bond", ["attract|ionic bond|electrostatic"])],
     "Sodium loses its one outer electron to chlorine, forming Na⁺; chlorine gains it, forming Cl⁻. The oppositely charged ions attract: this is an ionic bond.")
u.mc("r", "An ion is…", "an atom that has lost or gained electrons", ["an atom that has lost protons", "a neutral molecule", "a nucleus"])
u.mc("r", "Metals form … ions.", "positive", ["negative", "neutral", "no"])
u.mc("r", "An ionic bond is…", "the electrostatic attraction between oppositely charged ions", ["a shared pair of electrons", "attraction between two neutrons", "a magnetic force"], d="H")
u.mc("r", "Why does magnesium chloride have the formula MgCl₂?", "Magnesium loses two electrons, so it needs two chloride ions", ["Magnesium gains two electrons", "Chlorine loses two electrons", "Magnesium has two protons"], d="VH")
mcs("p", [
    ("A positive ion is called a…", "cation", ["anion", "molecule", "neutron"]),
    ("A negative ion is called an…", "anion", ["cation", "atom", "isotope"]),
    ("Non-metals usually … electrons.", "gain", ["lose", "share protons", "destroy"]),
    ("Metals usually … electrons.", "lose", ["gain", "share protons", "destroy"]),
    ("Losing an electron makes an atom…", "positive", ["negative", "neutral", "heavier"]),
    ("Gaining an electron makes an atom…", "negative", ["positive", "neutral", "lighter"]),
    ("Table salt is…", "sodium chloride", ["magnesium chloride", "hydrogen chloride", "sodium hydroxide"]),
    ("The sodium ion is written…", "Na⁺", ["Na⁻", "Na²⁺", "Na"]),
    ("The chloride ion is written…", "Cl⁻", ["Cl⁺", "Cl²⁻", "Cl"]),
    ("Opposite charges…", "attract", ["repel", "ignore each other", "cancel atoms"]),
    ("Ionic bonds usually form between…", "a metal and a non-metal", ["two non-metals", "two noble gases", "two metals"]),
    ("A magnesium ion has a charge of…", "2+", ["1+", "2−", "1−"]),
    ("An oxide ion, O²⁻, has gained … electrons.", "2", ["1", "6", "8"]),
    ("After forming ions, sodium and chlorine both have…", "full outer shells", ["no electrons", "one outer electron", "seven outer electrons"]),
    ("The force holding ions together is…", "electrostatic attraction", ["friction", "gravity", "magnetism"]),
])
u.mt("p", "Match the ion to its charge.", [("Potassium ion", "1+"), ("Calcium ion", "2+"), ("Bromide ion", "1−")])
u.ms("p", "Select ALL the ionic compounds.", ["Sodium chloride", "Magnesium chloride", "Magnesium oxide"], ["Water", "Methane"])
u.od("p", "Order the steps in forming magnesium oxide.", ["Magnesium atom loses 2 electrons", "Oxygen atom gains 2 electrons", "Mg²⁺ and O²⁻ ions form", "Opposite charges attract"])
u.ex("a", "Calcium (2, 8, 8, 2) reacts with fluorine (2, 7). Predict the formula of calcium fluoride and explain it.", [("calcium loses 2 → Ca²⁺", ["ca2|2\\+|loses 2|loses two"]), ("each fluorine gains 1 → F⁻", ["f-|f⁻|gains 1|gains one"]), ("CaF₂", ["caf2|caf₂"])],
     "Calcium loses two electrons to form Ca²⁺. Each fluorine gains one to form F⁻, so two fluoride ions are needed: CaF₂.")
u.mc("a", "Why does sodium form Na⁺ and not Na⁷⁻?", "Losing one electron is much easier than gaining seven", ["Sodium is a non-metal", "Sodium has seven protons", "Na⁷⁻ is a noble gas"], skill="Reasoning")
u.mc("a", "Aluminium (2, 8, 3) forms an ion with charge…", "3+", ["3−", "5−", "1+"], skill="Application")
u.mc("a", "How many electrons does a sodium ion, Na⁺, have?", "10", ["11", "12", "1"], skill="Application")
u.stop("chlorine gains one", "Metals form positive ions called…", "cations", ["anions", "molecules", "neutrons"])
u.stop("to make magnesium chloride", "An ionic bond is the attraction between…", "oppositely charged ions", ["two neutral atoms", "shared electrons", "two neutrons"])

# ---------------------------------------------------------------- 5.4
u.sec("5.4", "O4")
u.gd("r", "Which structure does each substance have?", "Structure", [("Water", "Simple molecular"), ("Diamond", "Giant covalent"), ("Sodium chloride", "Giant ionic"), ("Carbon dioxide", "Simple molecular")])
u.tb("r", "Boiling points. Complete the table.", ["Substance", "Boiling point (°C)", "Gas at 25 °C?"], [["Oxygen", "−183", B("yes")], ["Bromine", "59", B("no")], ["Sodium chloride", "1413", B("no")]])
u.gd("r", "Does it conduct electricity?", "Conducts?", [("Graphite", "Yes"), ("Diamond", "No"), ("Solid sodium chloride", "No"), ("Molten sodium chloride", "Yes")])
u.ex("r", "Explain why graphite is soft and conducts electricity but diamond is hard and does not.", [("diamond: each carbon 4 strong bonds – rigid", ["4|four|rigid|strong"]), ("graphite: 3 bonds, layers slide", ["3|three|layer|slide"]), ("graphite conducts – free electrons", ["electron|conduct|free"])],
     "In diamond, each carbon forms four strong bonds in a rigid network, so it is very hard. In graphite, each carbon bonds to three others in layers that slide, so it is soft, and spare electrons let it conduct.")
u.mc("r", "Simple molecular substances have…", "low melting and boiling points", ["very high melting points", "giant lattices", "always conduct electricity"])
u.mc("r", "Ionic compounds have high melting points because…", "strong electrostatic forces hold the ions together", ["their molecules are small", "they share electrons weakly", "they contain no ions"], d="H")
u.mc("r", "Why does salt conduct electricity only when melted or dissolved?", "Only then can the ions move", ["Only then does it have electrons", "Solid salt has no ions", "Water is a metal"], d="H")
u.mc("r", "A substance melts at 2000 °C and does not conduct when solid or molten. It is most likely…", "giant covalent", ["simple molecular", "ionic", "a metal"], d="VH")
mcs("p", [
    ("Bromine boils at about…", "59 °C", ["590 °C", "5.9 °C", "1413 °C"]),
    ("Diamond is…", "extremely hard", ["soft", "a liquid", "a conductor"]),
    ("Graphite is used in pencils because…", "its layers slide off easily", ["it is very hard", "it is a gas", "it is ionic"]),
    ("In diamond, each carbon bonds to…", "four other carbons", ["three other carbons", "one other carbon", "no other carbons"]),
    ("In graphite, each carbon bonds to…", "three other carbons", ["four", "one", "six"]),
    ("Sodium chloride forms a giant ionic…", "lattice", ["molecule", "gas", "helix"]),
    ("Simple molecular substances do not conduct electricity because…", "they have no charged particles that can move", ["they are too hot", "they are metals", "they have free ions"]),
    ("Oxygen, O₂, has a … structure.", "simple molecular", ["giant ionic", "giant covalent", "metallic"]),
    ("Diamond is used in cutting tools because it is…", "very hard", ["soft", "a conductor", "low melting"]),
    ("Graphite is used for electrodes because it…", "conducts electricity", ["is very hard", "is transparent", "dissolves in water"]),
    ("The forces between simple molecules are…", "weak", ["very strong", "ionic bonds", "covalent bonds"]),
    ("Solid ionic compounds do not conduct because the ions…", "cannot move", ["are missing", "are neutral", "are gases"]),
    ("A giant covalent structure is a huge…", "network of covalent bonds", ["group of ions", "collection of small molecules", "metal"]),
    ("Salt dissolved in water…", "conducts electricity", ["does not conduct", "becomes diamond", "becomes a gas"]),
    ("Water's boiling point is low compared with salt because water is…", "simple molecular", ["giant ionic", "giant covalent", "metallic"]),
])
u.mt("p", "Match the structure to a property.", [("Simple molecular", "low boiling point"), ("Giant ionic", "conducts when molten"), ("Giant covalent", "very high melting point")])
u.ms("p", "Select ALL the properties of diamond.", ["Very hard", "Very high melting point", "Does not conduct"], ["Soft", "Conducts electricity"])
u.od("p", "Order from lowest to highest boiling point.", ["Oxygen", "Water", "Sodium chloride"])
u.ex("a", "Substance X melts at 801 °C, does not conduct when solid, but conducts when molten. Identify its structure and explain.", [("giant ionic", ["ionic"]), ("high melting point – strong forces", ["high|strong"]), ("ions move only when molten", ["ion.*move|move"])],
     "X is giant ionic. Its high melting point shows strong electrostatic forces, and it conducts only when molten because the ions are then free to move.")
u.mc("a", "Why do simple molecular substances have low boiling points even though their covalent bonds are strong?", "Only the weak forces between molecules must be overcome", ["Their covalent bonds break easily", "They have no bonds", "They are ionic"], skill="Reasoning")
u.mc("a", "Graphene is a single layer of graphite. Which property would you expect?", "It conducts electricity", ["It is a gas", "It is ionic", "It melts at room temperature"], skill="Reasoning")
u.mc("a", "Why can't diamond conduct electricity?", "All its outer electrons are used in bonds, so none are free", ["It has free ions", "It is a liquid", "It has free electrons"], skill="Reasoning")
u.stop("Bromine boils at just 59 degrees Celsius", "Simple molecular substances have … boiling points.", "low", ["very high", "no", "infinite"])
u.stop("so it's soft and conducts electricity", "Why is diamond so hard?", "Each carbon bonds strongly to four others", ["It has layers that slide", "It is ionic", "It is a gas"])
u.stop("because then the ions can move", "Sodium chloride conducts electricity when…", "melted or dissolved", ["solid", "cold", "never"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Bonding and structure", "sec": None, "kids": [
    {"id": "why", "t": "Why atoms bond", "d": "Full outer shell = stable • Noble gases unreactive", "obj": "O1", "sec": "5.1"},
    {"id": "cov", "t": "Covalent", "d": "Shared pair of electrons • Non-metals • H₂, H₂O, CH₄", "obj": "O2", "sec": "5.2"},
    {"id": "ion", "t": "Ionic", "d": "Metals lose → cations • Non-metals gain → anions • Electrostatic attraction", "obj": "O3", "sec": "5.3"},
    {"id": "sim", "t": "Simple molecular", "d": "Low melting/boiling points • No conduction", "obj": "O4", "sec": "5.4"},
    {"id": "gnt", "t": "Giant structures", "d": "Diamond hard • Graphite layers, conducts • Ionic lattice: high melting, conducts when molten", "obj": "O4", "sec": "5.4"},
]}
