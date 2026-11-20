# -*- coding: utf-8 -*-
"""Stage 8 Unit 4 – The Structure of an Atom. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Chemistry"
BLURB = "Protons, neutrons and electrons, the electrostatic force that holds atoms together, electron shells and atomic number, and how the model of the atom developed."
OBJECTIVES = {
    "O1": {"sec": "4.1", "code": "8Cm.02", "codeNote": "", "t": "Describe the particles in an atom and state the charges of protons, neutrons and electrons."},
    "O2": {"sec": "4.1", "code": "8Cm.03", "codeNote": "", "t": "Explain that the electrostatic attraction between the nucleus and electrons holds an atom together."},
    "O3": {"sec": "4.1", "code": "8Cm.01, 8TWSm.03", "codeNote": "", "t": "Use atomic number to work out protons and electrons, arrange electrons in shells and use element symbols."},
    "O4": {"sec": "4.2", "code": "8Cm.01, 8SIC.01, 8TWSp.02", "codeNote": "", "t": "Describe how the model of the atom developed, including the Rutherford model and the gold foil experiment."},
}
SECTIONS = [
    {"id": "4.1", "title": "Structure of an atom", "objs": ["O1", "O2", "O3"]},
    {"id": "4.2", "title": "Development of the atomic model", "objs": ["O4"]},
]
u = Unit(8, 4)

# ---------------------------------------------------------------- 4.1
u.sec("4.1", "O1")
u.gd("r", "What is the charge on each particle?", "Charge", [("Proton", "Positive"), ("Neutron", "No charge"), ("Electron", "Negative")])
u.tb("r", "Complete the table for atoms (atomic number = protons = electrons).", ["Element", "Atomic number", "Protons", "Electrons"], [["Carbon", "6", B(6), B(6)], ["Oxygen", "8", B(8), B(8)]], o="O3")
u.mc("r", "Where are the protons and neutrons in an atom?", "In the nucleus at the centre", [("Orbiting in shells", "That is electrons."), ("Spread evenly through the atom", "That was an old model."), ("Outside the atom", "No.")])
u.mc("r", "Why is an atom neutral overall?", "It has equal numbers of protons and electrons", [("It has no particles", "No."), ("Neutrons cancel all charges", "Neutrons have no charge."), ("Electrons are positive", "No.")], o="O2")
u.ex("r", "Explain what stops the electrons flying away from the nucleus.", [("protons positive, electrons negative", ["positive|negative|opposite"]), ("opposite charges attract", ["attract"]), ("electrostatic force", ["electrostatic"])],
     "The positive protons in the nucleus attract the negative electrons, because opposite charges attract. This electrostatic force holds the electrons in the atom.", o="O2")
u.gd("r", "How many electrons are in each shell?", "Electrons", [("Carbon – first shell", "2"), ("Carbon – second shell", "4"), ("Oxygen – second shell", "6")], o="O3", extra=["8"])
u.mc("r", "The atomic number of an element tells you…", "the number of protons in each atom", [("the number of neutrons", "No."), ("the mass of the atom", "No."), ("the number of shells", "No.")], o="O3", d="H")
u.mc("r", "Why is sodium very reactive?", "It has 1 outer electron that is held weakly and lost easily.", [("It has a full outer shell.", "No – full shells are stable."), ("It has no electrons.", "No."), ("Its nucleus is negative.", "No.")], o="O3", d="VH")
for p, r, w, o in [
    ("Atoms are the smallest particles of an…", "element that can exist", ["mixture", "organ", "cell"], "O1"),
    ("'Atomos' means…", "uncuttable", ["tiny ball", "charged", "empty"], "O1"),
    ("An atom is mostly…", "empty space", ["solid metal", "liquid", "neutrons"], "O1"),
    ("Protons and neutrons have…", "the same mass", ["the same charge", "no mass", "different numbers always"], "O1"),
    ("Compared with a proton, an electron is…", "about 1836 times lighter", ["the same mass", "heavier", "twice as heavy"], "O1"),
    ("Like charges…", "repel", ["attract", "do nothing", "disappear"], "O2"),
    ("The force that holds protons together in the nucleus is the…", "nuclear force", ["electrostatic force", "friction", "gravity only"], "O2"),
    ("Rubbing a balloon on hair moves…", "electrons onto the balloon", ["protons onto the balloon", "neutrons onto the hair", "nothing"], "O2"),
    ("A negatively charged balloon makes an empty can…", "roll towards it", ["roll away", "melt", "stay still always"], "O2"),
    ("Hydrogen has how many protons?", "1", ["2", "6", "0"], "O3"),
    ("Helium has how many neutrons?", "2", ["1", "6", "8"], "O3"),
    ("The first shell holds up to how many electrons?", "2", ["8", "1", "18"], "O3"),
    ("The symbol for chlorine is…", "Cl", ["C", "Ch", "Co"], "O3"),
    ("The symbol for helium is…", "He", ["H", "Hm", "E"], "O3"),
    ("Two hydrogen atoms share electrons to form…", "H2", ["He", "H", "O2"], "O3"),
]:
    u.mc("p", p, r, w, o=o)
u.mt("p", "Match the element to its atomic number.", [("Hydrogen", "1"), ("Carbon", "6"), ("Nitrogen", "7"), ("Oxygen", "8")], o="O3")
u.ms("p", "Select ALL the particles found in the nucleus.", ["Protons", "Neutrons"], ["Electrons", "Shells"])
u.gd("p", "Attract or repel?", "Result", [("Positive and negative", "Attract"), ("Negative and negative", "Repel"), ("Positive and positive", "Repel")], o="O2")
u.ex("a", "* Advanced. Explain why carbon is the building block of living things.", [("4 outer electrons", ["4|four"]), ("needs 4 more / forms many bonds", ["needs 4|bonds|share"]), ("bonds with carbon and other elements easily", ["other (carbon|element)|chains|easily"])],
     "Carbon has 4 outer electrons and needs 4 more for a full shell, so it forms bonds easily with other carbon atoms and many other elements, building large molecules.", o="O3")
u.mc("a", "Carbon-12 and carbon-14 are isotopes. How are they different?", "Carbon-14 has 2 more neutrons.", ["Carbon-14 has 2 more protons.", "Carbon-14 has more electrons.", "They are different elements."], o="O3")
u.nm("a", "An atom has 11 protons and 12 neutrons. How many particles are in its nucleus?", 23, "particles", o="O1")
u.gd("a", "Draw the electron arrangement: how many electrons in each shell?", "Shells", [("Nitrogen (7)", "2, 5"), ("Sodium (11)", "2, 8, 1"), ("Neon (10)", "2, 8")], o="O3", extra=["2, 6"])
u.stop("meaning uncuttable", "Atoms are the smallest particles of…", "an element", ["a mixture", "a cell", "a compound only"])
u.stop("so the charges balance and the atom is neutral", "What is the charge on a neutron?", "No charge", ["Positive", "Negative", "It changes"])
u.stop("stopping the electrons flying away", "Electrons are held in an atom by…", "the electrostatic force", ["friction", "magnetism", "the nuclear force"], o="O2")
u.stop("and helium is He", "The atomic number tells you the number of…", "protons", ["neutrons", "shells", "isotopes"], o="O3")

# ---------------------------------------------------------------- 4.2
u.sec("4.2", "O4")
u.od("r", "Put the atomic models in the order they were suggested.", ["Dalton – solid balls", "Thomson – plum pudding", "Rutherford – nuclear model", "Bohr – electron shells"])
u.gd("r", "Which scientist made each discovery?", "Scientist", [("Discovered electrons", "Thomson"), ("Found the nucleus", "Rutherford"), ("Discovered the neutron", "Chadwick")])
u.gd("r", "Gold foil results: what did each observation show?", "Shows", [("Most alpha particles passed straight through", "Atom is mostly empty space"), ("A few bounced straight back", "Tiny dense nucleus"), ("Some were deflected", "Nucleus is positive")])
u.ex("r", "Explain why the gold foil results did not support the plum pudding model.", [("plum pudding predicted all particles pass straight through", ["straight through|all pass|expected"]), ("some bounced back / deflected", ["bounce|deflect"]), ("needs a tiny dense positive nucleus", ["nucleus|dense|concentrat"])],
     "The plum pudding model predicted that all alpha particles would pass straight through. Some were deflected and a few bounced back, which needs a tiny, dense, positive nucleus.")
u.mc("r", "Why do scientists use models of the atom?", "Atoms are far too small to see, so models help explain how they behave", [("Models are the real atom", "No."), ("Atoms are big", "No."), ("To make atoms bigger", "No.")])
u.mc("r", "In the plum pudding model, electrons were…", "stuck in a positive 'soup'", [("in shells", "Bohr."), ("in a nucleus", "No."), ("a cloud", "Schrödinger.")], d="H")
u.mc("r", "Bohr improved Rutherford's model by suggesting that electrons…", "move in fixed shells", [("are inside the nucleus", "No."), ("are positive", "No."), ("do not exist", "No.")], d="H")
u.mc("r", "What does the history of the atomic model show about science?", "Models change when new evidence contradicts them.", [("Models never change.", "No."), ("The first idea is always right.", "No."), ("Evidence is not needed.", "No.")], d="VH")
for p, r, w in [
    ("Dalton imagined atoms as…", "tiny solid balls", ["clouds", "plum puddings", "empty space"]),
    ("Dalton's model was suggested in…", "1803", ["1911", "1932", "1926"]),
    ("Thomson's model is called the…", "plum pudding model", ["solar system model", "cloud model", "solid ball model"]),
    ("Rutherford compared electrons moving around the nucleus to…", "planets around the Sun", ["raisins in a cake", "balls in a box", "water in a cup"]),
    ("Rutherford's experiment was in…", "1911", ["1803", "1904", "1932"]),
    ("Schrödinger described electrons as…", "a cloud around the nucleus", ["solid balls", "inside the nucleus", "stuck in pudding"]),
    ("Chadwick discovered the neutron in…", "1932", ["1803", "1913", "1904"]),
    ("Rutherford fired alpha particles at…", "thin gold foil", ["a magnet", "a balloon", "a glass prism"]),
    ("Alpha particles have a…", "positive charge", ["negative charge", "no charge", "changing charge"]),
    ("Rutherford expected the alpha particles to…", "pass straight through", ["all bounce back", "stop", "turn into gold"]),
    ("Most alpha particles passing through shows that atoms are…", "mostly empty space", ["solid", "liquid", "negative"]),
    ("A few bouncing back shows the nucleus is…", "tiny and dense", ["huge and soft", "empty", "negative"]),
    ("The discovery of the neutron explained the…", "mass of the atom", ["colour of gold", "charge of electrons", "size of planets"]),
    ("Each scientist…", "built on the work of those before", ["ignored earlier work", "worked alone without evidence", "copied the same model"]),
    ("Evidence that contradicts a model means…", "the model must be changed", ["the evidence is ignored", "the model is proved", "nothing happens"]),
]:
    u.mc("p", p, r, w)
u.gd("p", "Which scientist suggested each model?", "Scientist", [("Solid balls", "Dalton"), ("Plum pudding", "Thomson"), ("Electron shells", "Bohr")], extra=["Rutherford"])
u.ms("p", "Select ALL the observations from the gold foil experiment.", ["Most particles passed straight through", "A few bounced straight back"], ["All particles stopped", "The foil melted"])
u.od("p", "Order these discoveries by date.", ["Electron (Thomson, 1904 model)", "Nucleus (1911)", "Electron shells (1913)", "Neutron (1932)"], d="H")
u.ex("a", "* Advanced. Explain why it is useful that scientific models can be changed.", [("new evidence / experiments", ["new evidence|experiment|results"]), ("model improved to explain observations", ["improve|better|explain|accurate"])],
     "New experiments can give evidence the old model cannot explain, so changing the model lets scientists build a more accurate explanation of how atoms behave.")
u.mc("a", "If atoms were solid balls, what would Rutherford have seen?", "Alpha particles bouncing back or stopping much more often", ["Exactly the same results", "Particles passing through more easily", "The foil disappearing"], skill="Reasoning")
u.nm("a", "How many years passed between Dalton's model (1803) and Chadwick's discovery (1932)?", 129, "years")
u.mc("a", "Why did a few alpha particles bounce straight back?", "They hit or came very close to the tiny positive nucleus and were repelled.", ["They hit electrons.", "They were attracted by the nucleus.", "The foil was too thick."], skill="Reasoning")
u.stop("negative electrons stuck in a positive 'soup'", "Who suggested the plum pudding model?", "Thomson", ["Dalton", "Rutherford", "Chadwick"])
u.stop("explaining the mass of the atom", "Who discovered the neutron?", "Chadwick", ["Bohr", "Dalton", "Schrödinger"])
u.stop("our understanding of the atom changed forever", "Most alpha particles passed through gold foil. This showed that atoms are…", "mostly empty space", ["solid", "negatively charged", "liquid"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "The atom", "sec": None, "kids": [
    {"id": "pt", "t": "Particles", "d": "Proton + • Neutron 0 • Electron − • Nucleus in the centre", "obj": "O1", "sec": "4.1"},
    {"id": "ef", "t": "Electrostatic force", "d": "Opposite charges attract • Holds electrons in the atom • Balloon and can", "obj": "O2", "sec": "4.1"},
    {"id": "sh", "t": "Shells", "d": "First shell 2 • Next shells 8 • Full outer shell = stable", "obj": "O3", "sec": "4.1"},
    {"id": "an", "t": "Atomic number", "d": "Number of protons = number of electrons • Decides the element • Symbols C, Cl, He", "obj": "O3", "sec": "4.1"},
    {"id": "md", "t": "Models of the atom", "d": "Dalton • Thomson • Rutherford • Bohr • Schrödinger • Chadwick", "obj": "O4", "sec": "4.2"},
    {"id": "gf", "t": "Gold foil experiment", "d": "Most pass through – empty space • Some bounce back – dense nucleus", "obj": "O4", "sec": "4.2"},
]}
