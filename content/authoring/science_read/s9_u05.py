# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 5 Chemical Bonding and Structure of Materials – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9Cm.02–9Cm.05, 9Cp.04)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}
CARD = lambda title, cards, cols=None: dict({"kind": "sciCards", "title": title, "cards": cards}, **({"cols": cols} if cols else {}))

# =====================================================================================================
# 5.1 Chemical bonding · 9Cm.02
# =====================================================================================================
READ["5.1"] = L(
    H("Lonely neon",
      "Neon glows in advertising signs, but it almost never reacts with anything. Sodium, the very next element, reacts violently with water.",
      "What is so different about their atoms? Look at their electronic structures: neon 2, 8; sodium 2, 8, 1."),
    I("Stable outer shells",
      "The **outer shell** decides how an atom reacts. A **full outer shell** (2 for helium, 8 for the others) is a **stable electronic configuration**.",
      fig={"kind": "atom", "shells": [2, 8], "p": 10, "n": 10, "title": "neon 2, 8 – full outer shell"},
      then=["Group 18 atoms (helium, neon, argon) already have full outer shells, so they hardly react.",
            "Other atoms – sodium with 1 outer electron, chlorine with 7 – are not stable, so they react to reach a full outer shell."]),
    I("Two ways to bond",
      "Atoms reach a full outer shell by forming **chemical bonds**.",
      table=[["Bond", "How", "Between"], ["**covalent**", "atoms **share** pairs of outer electrons", "non-metal + non-metal"],
             ["**ionic**", "atoms **lose or gain** electrons, forming charged ions that attract", "metal + non-metal"]]),
    Y("Which bond?",
      grid("s9u05r11", "Will the atoms bond covalently or ionically?", ["Covalent", "Ionic"],
           [("hydrogen + oxygen", "Covalent"), ("sodium + chlorine", "Ionic"), ("carbon + hydrogen", "Covalent"), ("magnesium + oxygen", "Ionic")],
           "Non-metal + non-metal, or metal + non-metal?", "Two non-metals share electrons (covalent); a metal and a non-metal transfer electrons (ionic).")),
    K("Key points",
      "Atoms with a **full outer shell** are stable and unreactive (Group 18).",
      "Other atoms bond to reach a full outer shell.",
      "**Covalent**: sharing electrons (non-metals). **Ionic**: losing/gaining electrons (metal + non-metal)."),
    book=BK(
        [("stable electronic configuration", "a full outer shell of electrons"), ("chemical bond", "a force that holds atoms together"),
         ("covalent bond", "a shared pair of electrons"), ("ionic bond", "attraction between oppositely charged ions")],
        [], [],
        [Ex("Why is argon (2, 8, 8) unreactive?", ans="It has a full outer shell."),
         Ex("How many electrons must each atom gain or lose to get a full outer shell: (a) sodium 2, 8, 1 (b) chlorine 2, 8, 7 (c) oxygen 2, 6?", ans="(a) lose 1 (b) gain 1 (c) gain 2"),
         Ex("Predict the type of bond in: (a) carbon dioxide (b) potassium bromide.", ans="(a) covalent (b) ionic", think=True)],
        ["explain why atoms bond", "describe covalent and ionic bonding in outline"],
        look=["full outer shells", "covalent and ionic"],
        note="Read it after the video: why atoms bond (answers at the back)."),
)

# =====================================================================================================
# 5.2 Covalent bonding · 9Cm.02, 9Cm.03
# =====================================================================================================
READ["5.2"] = L(
    H("Sharing makes both happy",
      "Two friends each have one sweet, but each wants two. If they share – each holding both sweets together – both feel they have two.",
      "Atoms can do something similar with electrons. Read on."),
    I("Covalent bonds: sharing electrons",
      "A **covalent bond** is a **shared pair of electrons** between two non-metal atoms. Both atoms count the shared electrons in their outer shell.",
      fig={"kind": "dotcross", "mol": "H2O"},
      then=["**Dot-and-cross diagrams** show the outer electrons: dots for one atom, crosses for the other. In water, oxygen (6 outer electrons) shares one pair with each of two hydrogen atoms – two covalent bonds, and every atom now has a full shell."]),
    I("More molecules",
      "The number of bonds depends on how many electrons each atom needs.",
      table=[["Molecule", "Formula", "Covalent bonds"], ["hydrogen", "H₂", "1 (single)"], ["hydrogen chloride", "HCl", "1"], ["water", "H₂O", "2"], ["methane", "CH₄", "4"],
             ["oxygen", "O₂", "1 **double** bond (2 shared pairs)"], ["carbon dioxide", "CO₂", "2 double bonds"]],
      fig={"kind": "dotcross", "mol": "CH4"},
      then=["Carbon has 4 outer electrons and can form 4 bonds – that is why it makes millions of different molecules."]),
    Y("How many bonds?",
      num("s9u05r21", "Ammonia is NH₃. Nitrogen has 5 outer electrons. How many covalent bonds does the nitrogen atom form?", 3, "How many more electrons does nitrogen need to reach 8?",
          "5 + 3 = 8, so it shares 3 pairs – one with each hydrogen.")),
    I("Real life: covalent molecules around us",
      "Many everyday substances are small covalent molecules.",
      fig=CARD("Small covalent molecules", [{"t": "Water H₂O", "d": "drinks, rain"}, {"t": "Carbon dioxide CO₂", "d": "fizzy drinks, breath"}, {"t": "Methane CH₄", "d": "natural gas for cooking"},
                                            {"t": "Oxygen O₂", "d": "the air we breathe"}], 4),
      then=["These are gases or liquids at room temperature, because the forces **between** molecules are weak (even though the bonds **inside** them are strong)."]),
    K("Key points",
      "A **covalent bond** is a shared pair of electrons between non-metal atoms.",
      "Dot-and-cross diagrams show the shared outer electrons.",
      "H₂, HCl: 1 bond; H₂O: 2; NH₃: 3; CH₄: 4; O₂ and CO₂ have double bonds.",
      "Small covalent molecules are usually gases or liquids at room temperature."),
    book=BK(
        [("covalent bond", "a shared pair of electrons between two atoms"), ("molecule", "a group of atoms joined by covalent bonds"),
         ("dot-and-cross diagram", "a drawing showing the outer electrons of bonded atoms"), ("double bond", "two shared pairs of electrons")],
        [], [],
        [Ex("Draw dot-and-cross diagrams for: (a) H₂ (b) HCl (c) H₂O.", ans="(a) one shared pair (b) one shared pair, Cl with 3 non-bonding pairs (c) O sharing one pair with each H, 2 non-bonding pairs"),
         Ex("How many covalent bonds are in a methane molecule?", ans="4"),
         Ex("Explain why carbon can form so many compounds.", ans="It has 4 outer electrons, so it can form 4 covalent bonds, including with other carbon atoms."),
         Ex("Why is methane a gas at room temperature, even though its bonds are strong?", ans="The forces between separate molecules are weak, so little energy is needed to separate them.", think=True)],
        ["describe a covalent bond", "draw dot-and-cross diagrams for simple molecules", "explain why small molecules are often gases or liquids"],
        look=["the water dot-and-cross diagram", "the molecules table"],
        note="Read it after the video: covalent bonds and dot-and-cross diagrams (answers at the back)."),
)

# =====================================================================================================
# 5.3 Ionic bonding · 9Cm.04, 9Cm.05
# =====================================================================================================
READ["5.3"] = L(
    H("Give and take",
      "Sodium has one electron too many for a full outer shell; chlorine has one too few.",
      "What is the simplest way for both to end up with full outer shells?"),
    I("Ions",
      "An **ion** is an atom (or group of atoms) that has **lost or gained electrons**, so it has a **charge**.",
      table=[["Atom", "Change", "Ion", "Charge"], ["sodium 2, 8, 1", "loses 1 electron", "Na⁺ (2, 8)", "+1"], ["magnesium 2, 8, 2", "loses 2 electrons", "Mg²⁺ (2, 8)", "+2"],
             ["chlorine 2, 8, 7", "gains 1 electron", "Cl⁻ (2, 8, 8)", "−1"], ["oxygen 2, 6", "gains 2 electrons", "O²⁻ (2, 8)", "−2"]],
      then=["**Metals lose** electrons and form **positive** ions; **non-metals gain** electrons and form **negative** ions."]),
    I("Ionic bonds",
      "When sodium reacts with chlorine, one electron **transfers** from each sodium atom to a chlorine atom.",
      fig={"kind": "atom", "shells": [2, 8], "p": 11, "n": 12, "ion": "+", "title": "sodium ion Na⁺"},
      then=["The positive Na⁺ and negative Cl⁻ ions **attract** each other. This **electrostatic attraction** between oppositely charged ions is an **ionic bond** – forming sodium chloride, table salt.",
            "Magnesium loses two electrons, so one Mg²⁺ ion bonds with **two** Cl⁻ ions: magnesium chloride, MgCl₂."]),
    Y("Charge on the ion",
      grid("s9u05r31", "What charge will each ion have?", ["+1", "+2", "−1", "−2"],
           [("potassium (2, 8, 8, 1)", "+1"), ("calcium (2, 8, 8, 2)", "+2"), ("fluorine (2, 7)", "−1"), ("sulfur (2, 8, 6)", "−2")],
           "Lose electrons → positive; gain → negative.", "K loses 1 (+1); Ca loses 2 (+2); F gains 1 (−1); S gains 2 (−2).")),
    Y("What is an ionic bond?",
      mcq("s9u05r32", "What is an ionic bond?",
          [("The electrostatic attraction between oppositely charged ions.", True, "Yes."), ("A shared pair of electrons.", False, "That is a covalent bond."),
           ("Two metal atoms touching.", False, "Not an ionic bond."), ("A neutron moving between atoms.", False, "Neutrons stay in the nucleus.")],
          "What holds Na⁺ and Cl⁻ together?", "Opposite charges attract.")),
    K("Key points",
      "**Ions** form when atoms lose or gain electrons: metals → positive ions; non-metals → negative ions.",
      "An **ionic bond** is the electrostatic attraction between oppositely charged ions.",
      "Examples: Na⁺Cl⁻ (sodium chloride); Mg²⁺ with two Cl⁻ (magnesium chloride)."),
    book=BK(
        [("ion", "a charged particle formed when an atom loses or gains electrons"), ("ionic bond", "electrostatic attraction between oppositely charged ions"),
         ("electrostatic attraction", "the force between opposite charges")],
        [], [],
        [Ex("Describe what happens to the electrons when sodium reacts with chlorine.", ans="Each sodium atom transfers its one outer electron to a chlorine atom, forming Na⁺ and Cl⁻ ions with full outer shells."),
         Ex("Write the electronic structure of: (a) Na⁺ (b) Cl⁻ (c) Mg²⁺.", ans="(a) 2, 8 (b) 2, 8, 8 (c) 2, 8"),
         Ex("Why does magnesium chloride have the formula MgCl₂?", ans="Mg loses 2 electrons; each Cl gains only 1, so two Cl⁻ ions balance one Mg²⁺."),
         Ex("Lithium (2, 1) reacts with oxygen (2, 6). Predict the formula of lithium oxide. Explain.", ans="Li₂O – each Li loses 1 electron; oxygen needs 2, so two Li⁺ balance one O²⁻.", think=True)],
        ["describe how ions form", "explain an ionic bond", "work out the charges on simple ions"],
        look=["the ions table", "sodium chloride"],
        note="Read it after the video: ions and ionic bonding (answers at the back)."),
)

# =====================================================================================================
# 5.4 Structures and properties · 9Cp.04
# =====================================================================================================
READ["5.4"] = L(
    H("Salt or sugar?",
      "Salt and sugar are both white crystals that dissolve in water. You cannot taste-test in the lab.",
      "How could electricity help you tell them apart?"),
    I("Predict, watch, explain: which conducts electricity?",
      "Electrodes connected to a cell and a bulb are dipped into solid salt, salt solution and sugar solution in turn.",
      table=[["Sample", "Bulb", "Why"], ["solid salt", "off", "ions are fixed in a lattice and cannot move"], ["salt solution", "on", "ions are free to move and carry charge"],
             ["sugar solution", "off", "sugar is made of uncharged covalent molecules"]]),
    I("Structure decides properties",
      "Three kinds of structure:",
      table=[["Structure", "Examples", "Melting point", "Conducts electricity?"],
             ["**simple molecular** (small covalent molecules)", "water, oxygen, carbon dioxide, bromine, sulfur", "low – weak forces between molecules", "no"],
             ["**giant covalent** (huge network of covalent bonds)", "diamond, graphite, silicon dioxide (sand)", "very high – many strong bonds to break", "no (except graphite)"],
             ["**giant ionic lattice**", "sodium chloride, magnesium oxide", "high – strong attraction between ions", "only when **melted or dissolved**"]]),
    I("Diamond and graphite",
      "Both are giant covalent structures of pure carbon.",
      table=[["", "Diamond", "Graphite"], ["bonds per carbon atom", "4", "3 (in flat layers)"], ["hardness", "extremely hard – cutting tools", "soft; layers slide – pencils, lubricants"],
             ["conducts electricity?", "no", "yes – each atom has one free electron"]]),
    I("Real data: melting points of four solids",
      "Melting points:",
      fig={"kind": "barchart", "labels": ["sulfur", "sodium chloride", "silicon dioxide", "magnesium oxide"], "values": [115, 801, 1713, 2852], "ymax": 3000, "step": 500,
           "ylabel": "melting point (°C)", "xlabel": "substance"},
      then=["Sulfur is made of small molecules with weak forces between them, so it melts easily. The other three are giant structures with many strong bonds or ionic attractions to break."]),
    Y("Identify the structure",
      grid("s9u05r41", "Which structure does each substance most likely have?", ["Simple molecular", "Giant covalent", "Giant ionic"],
           [("melts at 1600 °C, never conducts", "Giant covalent"), ("boils at −183 °C", "Simple molecular"), ("melts at 770 °C; conducts only when molten", "Giant ionic"), ("a liquid that does not conduct", "Simple molecular")],
           "Low melting point → small molecules; conducts when molten → ionic.", "Very high mp, no conduction → giant covalent; low mp → simple molecular; conducts only when molten → ionic.")),
    K("Key points",
      "**Simple molecular**: low melting points, do not conduct.",
      "**Giant covalent** (diamond, graphite, sand): very high melting points; only graphite conducts.",
      "**Giant ionic**: high melting points; conduct when melted or dissolved (ions can move).",
      "Diamond (4 bonds) is hard; graphite (3 bonds, layers) is soft and conducts."),
    book=BK(
        [("simple molecular structure", "small separate molecules with weak forces between them"), ("giant covalent structure", "a huge network of atoms joined by covalent bonds"),
         ("ionic lattice", "a regular arrangement of positive and negative ions")],
        [], [],
        [Ex("Explain why solid salt does not conduct electricity but salt solution does.", ans="In the solid the ions are fixed; in solution they are free to move and carry charge."),
         Ex("Why does diamond have a very high melting point?", ans="Every atom is joined by strong covalent bonds to four others; many bonds must be broken."),
         Ex("Give two differences between diamond and graphite and explain them.", ans="Diamond is hard, graphite soft (layers slide); graphite conducts (free electrons), diamond does not."),
         Ex("Quick quiz.", ("Why is neon unreactive?", "full outer shell"), ("What is a covalent bond?", "a shared pair of electrons"),
            ("What charge does a magnesium ion have?", "2+"), ("Why does sulfur melt at a low temperature?", "small molecules with weak forces between them")),
         Ex("A white solid melts at 700 °C and conducts electricity only when molten. What type of structure does it have? Explain.", ans="Giant ionic – high melting point; ions only move when molten.", think=True)],
        ["relate simple molecular, giant covalent and giant ionic structures to their properties"],
        look=["the structures table", "the melting point chart"],
        note="Read it after the video: structures and properties, plus a quick quiz (answers at the back)."),
)
