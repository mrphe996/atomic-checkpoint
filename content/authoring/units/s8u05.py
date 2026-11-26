# -*- coding: utf-8 -*-
"""Stage 8 Unit 5 – Mixtures and Solubility. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Chemistry"
BLURB = "Elements, compounds and mixtures, percentage purity, ways to separate mixtures including chromatography, and concentration, saturation and solubility."
OBJECTIVES = {
    "O1": {"sec": "5.1", "code": "8Cm.04", "codeNote": "", "t": "Classify matter as elements, compounds and homogeneous or heterogeneous mixtures, and name the parts of a solution."},
    "O2": {"sec": "5.1", "code": "8Cm.04", "codeNote": "percentage purity", "t": "Explain purity and calculate the percentage purity of a substance in a mixture."},
    "O3": {"sec": "5.2", "code": "8Cp.02, 8TWSc.02", "codeNote": "", "t": "Choose a method to separate a mixture, and use paper chromatography to separate and identify substances."},
    "O4": {"sec": "5.3", "code": "8Cp.01, 8Cc.05", "codeNote": "", "t": "Calculate concentration, describe saturated solutions and explain how solubility changes with temperature."},
}
SECTIONS = [
    {"id": "5.1", "title": "Pure substances and mixtures", "objs": ["O1", "O2"]},
    {"id": "5.2", "title": "Separating mixtures", "objs": ["O3"]},
    {"id": "5.3", "title": "Solutions", "objs": ["O4"]},
]
u = Unit(8, 5)

# ---------------------------------------------------------------- 5.1
u.sec("5.1", "O1")
u.gd("r", "Element, compound or mixture?", "Type", [("Gold", "Element"), ("Water (H2O)", "Compound"), ("Air", "Mixture"), ("Salt (NaCl)", "Compound")])
u.gd("r", "Homogeneous or heterogeneous mixture?", "Mixture", [("Salt water", "Homogeneous"), ("Sand and water", "Heterogeneous"), ("Steel", "Homogeneous"), ("Oil and water", "Heterogeneous")])
u.mc("r", "In sugar dissolved in water, the sugar is the…", "solute", [("solvent", "Water is the solvent."), ("solution", "That is the mixture."), ("residue", "No.")])
u.ex("r", "Explain how a compound is different from a mixture.", [("compound – elements chemically joined", ["chemically|joined|bond"]), ("fixed ratio / proportions", ["fixed|ratio"]), ("mixture – not joined, separated by physical methods", ["physical|not (chemically )?joined|any proportion"])],
     "In a compound the elements are chemically joined in a fixed ratio and can only be separated by chemical methods. In a mixture the substances are not joined, can be in any proportions and can be separated physically.")
u.nm("r", "A bronze coin has a mass of 75 g, and 62 g of it is copper. What is the percentage purity of copper? (1 decimal place)", 82.7, "%", o="O2", tol=0.1)
u.mc("r", "Why do medicines need to be very pure?", "They must contain exactly the right amount of active ingredient", [("To look shiny", "No."), ("To taste sweet", "No."), ("To be cheaper", "No.")], o="O2")
u.mc("r", "Bottled water with added minerals is…", "a mixture that is still safe to drink", [("a pure element", "No."), ("a compound", "No."), ("unsafe", "No.")], o="O2", d="H")
u.mc("r", "An element cannot be…", "broken down by chemical reactions", [("melted", "Elements can melt."), ("weighed", "No."), ("mixed with others", "No.")], d="VH")
for p, r, w, o in [
    ("Pure substances are elements or…", "compounds", ["mixtures", "solutions", "suspensions"], "O1"),
    ("How many elements are known?", "118", ["18", "1118", "8"], "O1"),
    ("'Hetero' means…", "different", ["the same", "pure", "hot"], "O1"),
    ("'Homo' means…", "the same", ["different", "mixed", "solid"], "O1"),
    ("A solution is a…", "homogeneous mixture", ["heterogeneous mixture", "pure element", "compound"], "O1"),
    ("The substance that does the dissolving is the…", "solvent", ["solute", "residue", "filtrate"], "O1"),
    ("Soil is a…", "heterogeneous mixture", ["pure substance", "compound", "solution"], "O1"),
    ("The properties of a compound are…", "different from its elements", ["the same as its elements", "always like water", "always like metals"], "O1"),
    ("A mixture can contain substances in…", "any proportions", ["a fixed ratio only", "equal amounts only", "one state only"], "O1"),
    ("A pure substance contains only…", "one type of atom or molecule", ["two elements", "dissolved salt", "water"], "O2"),
    ("Percentage purity = mass of pure substance ÷ total mass ×…", "100", ["10", "2", "1000"], "O2"),
    ("Dental implants use very pure metals to…", "avoid allergic reactions", ["look bigger", "be magnetic", "change colour"], "O2"),
    ("A 50 g sample contains 45 g of salt. Its purity is…", "90%", ["45%", "50%", "95%"], "O2"),
    ("Which is a compound?", "Carbon dioxide", ["Neon", "Gold", "Air"], "O1"),
    ("Which is an element?", "Neon", ["Water", "Salt", "Steel"], "O1"),
]:
    u.mc("p", p, r, w, o=o)
u.nm("p", "A 20 g sample of gold jewellery contains 15 g of pure gold. What is its percentage purity?", 75, "%", o="O2")
u.mt("p", "Match the word to its meaning.", [("Solute", "the substance that dissolves"), ("Solvent", "the substance that does the dissolving"), ("Solution", "the mixture formed")])
u.ms("p", "Select ALL the homogeneous mixtures.", ["Air", "Salt water", "Steel"], ["Sand and water", "Oil and water"])
u.ex("a", "* Advanced. A gold ring is labelled '18 carat', meaning 75% gold. Explain why jewellers mix gold with other metals, and what the label tells a buyer.", [("pure gold is soft / mixture is harder", ["soft|hard|strong"]), ("label shows how much gold / purity", ["75|purity|how much gold|proportion"])],
     "Pure gold is very soft, so mixing it with other metals makes it harder. The label tells the buyer the purity – 75% of the ring's mass is gold.", o="O2")
u.nm("a", "A 250 g sample of rock salt contains 230 g of sodium chloride. What is the percentage purity?", 92, "%", o="O2")
u.mc("a", "Why can water not be separated into hydrogen and oxygen by filtering or evaporating?", "It is a compound – the elements are chemically joined.", ["It is a mixture.", "Water is an element.", "Hydrogen is a liquid."], skill="Reasoning")
u.tb("a", "* Advanced. Complete the purity table.", ["Sample", "Mass of pure substance (g)", "Total mass (g)", "Purity (%)"], [["A", "40", "50", B(80)], ["B", "18", "20", B(90)]], o="O2")
u.stop("can't be broken down by chemical reactions", "A substance that cannot be broken down by chemical reactions is…", "an element", ["a compound", "a mixture", "a solution"])
u.stop("you can't tell them apart", "Salt water is a…", "homogeneous mixture", ["heterogeneous mixture", "pure element", "compound"])
u.stop("about 82.7 percent copper", "Percentage purity is mass of pure substance divided by total mass, times…", "100", ["10", "1000", "2"], o="O2")

# ---------------------------------------------------------------- 5.2
u.sec("5.2", "O3")
u.gd("r", "Which method separates each mixture?", "Method", [("Sand from water", "Filtration"), ("Salt from salt water", "Evaporation"), ("Pure water from sea water", "Distillation"), ("Dyes in ink", "Chromatography")])
u.mc("r", "In filtration, the solid left on the filter paper is the…", "residue", [("filtrate", "That is the liquid."), ("distillate", "No."), ("solvent", "No.")])
u.tb("r", "Chromatogram of a brown ink. Count the spots.", ["Ink", "Number of spots"], [["Brown ink (blue, red and yellow dyes)", B(3)], ["Pure red ink", B(1)]])
u.ex("r", "Explain why the start line in chromatography is drawn in pencil and kept above the solvent.", [("pencil does not dissolve / run", ["pencil.*(not|doesn)|graphite|insoluble"]), ("above solvent so ink does not dissolve into the solvent", ["above|wash|dissolve into|not.*solvent"])],
     "Pencil does not dissolve, so the line does not run. The line is kept above the solvent so the ink dots do not dissolve straight into the solvent but are carried up the paper.")
u.mc("r", "How does chromatography separate dyes?", "Each dye travels up the paper at a different speed", [("Heavier dyes evaporate", "No."), ("The paper filters out large dyes", "No."), ("Dyes are separated by colour of light", "No.")])
u.mc("r", "In distillation, the substance with the lowest boiling point…", "evaporates first", [("stays in the flask", "No."), ("freezes", "No."), ("turns into a solid", "No.")], d="H")
u.mc("r", "Which method is best to remove small stones from rice?", "Handpicking", ["Evaporation", "Distillation", "Chromatography"], d="H")
u.mc("r", "A chromatogram of a food colouring shows one spot. What does this tell you?", "It is a pure substance.", [("It is a mixture of dyes.", "No."), ("The test failed.", "Not necessarily."), ("It has no colour.", "No.")], d="VH")
for p, r, w in [
    ("Sieving separates…", "large particles from small ones", ["dissolved salt from water", "dyes in ink", "gases"]),
    ("Filtration separates an insoluble solid from…", "a liquid", ["a gas", "another solid", "a magnet"]),
    ("The liquid collected after filtering is the…", "filtrate", ["residue", "chromatogram", "solute"]),
    ("Evaporation leaves behind the…", "solute", ["solvent", "filter paper", "distillate"]),
    ("Distillation collects the…", "solvent", ["solute only", "residue", "sand"]),
    ("In distillation the vapour cools and…", "condenses", ["evaporates", "freezes", "burns"]),
    ("The liquid collected in distillation is the…", "distillate", ["residue", "filtrate", "solute"]),
    ("Distillation can turn salt water into…", "pure water", ["salt only", "oil", "steam forever"]),
    ("The result of paper chromatography is called a…", "chromatogram", ["filtrate", "residue", "distillate"]),
    ("A suitable solvent for chromatography could be…", "water or alcohol", ["sand", "salt", "oil paint"]),
    ("A mixture of dyes gives…", "more than one spot", ["one spot", "no spots", "a white line"]),
    ("Chromatography can be used to…", "test water for pollution", ["build bridges", "measure mass", "make salt"]),
    ("Forceps are used for…", "handpicking", ["distillation", "evaporation", "chromatography"]),
    ("Tea leaves are separated from tea by…", "filtration", ["evaporation", "distillation", "chromatography"]),
    ("Mixtures can be separated by physical methods because the substances…", "are not chemically joined", ["are elements", "are compounds", "are gases"]),
]:
    u.mc("p", p, r, w)
u.od("p", "Order the steps of paper chromatography.", ["Draw a pencil line near the bottom", "Add a dot of ink on the line", "Dip the paper in solvent with the line above it", "Let the solvent soak up the paper"])
u.mt("p", "Match the method to the mixture.", [("Sieving", "flour and lumps"), ("Evaporation", "salt from sea water"), ("Distillation", "water from ink")])
u.gd("p", "Filtrate or residue?", "Product", [("Water that passes through", "Filtrate"), ("Sand left on the paper", "Residue")])
u.ex("a", "* Advanced. A crime scene note was written in black ink. Explain how chromatography could show which of three suspects' pens was used.", [("make chromatograms of note ink and each pen", ["each pen|compare|three|all"]), ("same solvent / conditions", ["same solvent|same paper|same"]), ("matching pattern of spots identifies the pen", ["match|same spots|same pattern"])],
     "Make chromatograms of the ink from the note and from each suspect's pen using the same paper and solvent. The pen whose spots match the note's pattern is the one that was used.")
u.mc("a", "Why can't filtration separate salt from salt water?", "Salt is dissolved, so its particles pass through the filter paper.", ["Salt is too big.", "Salt is magnetic.", "Water is insoluble."], skill="Reasoning")
u.od("a", "* Advanced. Order the steps to get pure, dry salt from a mixture of sand and salt.", ["Add water and stir to dissolve the salt", "Filter to remove the sand", "Evaporate the water from the filtrate", "Collect the salt crystals"])
u.mc("a", "Why is distillation used instead of evaporation to get drinking water from sea water?", "Distillation collects the water; evaporation lets it escape into the air.", ["Evaporation collects water better.", "Distillation removes only sand.", "They are the same method."], skill="Reasoning")
u.stop("while the solid stays behind as the residue", "The liquid that passes through filter paper is the…", "filtrate", ["residue", "distillate", "solute"])
u.stop("called the distillate", "Distillation can turn salt water into…", "pure water", ["pure salt", "sand", "oil"])
u.stop("blue, red and yellow", "Each dye moves up the paper at…", "a different speed", ["the same speed", "no speed", "the speed of the solvent only"])

# ---------------------------------------------------------------- 5.3
u.sec("5.3", "O4")
u.nm("r", "5 g of sugar is dissolved to make 100 cm³ of solution. What is the concentration in g/cm³?", 0.05, "g/cm³", tol=0.001)
u.gd("r", "Saturated, unsaturated or supersaturated?", "Solution", [("More solute can still dissolve", "Unsaturated"), ("No more solute will dissolve", "Saturated"), ("Holds more than it normally can, unstable", "Supersaturated")])
u.tb("r", "Sugar cubes that dissolve in a cup of water. Complete the pattern (it rises by 1 cube for every 15 °C).", ["Temperature (°C)", "Cubes dissolved"], [["10", "1"], ["25", B(2)], ["40", B(3)]])
u.ex("r", "Explain why it is easier to dissolve sugar in hot tea than in iced tea.", [("solubility increases with temperature", ["solubility|temperature|hotter"]), ("more sugar dissolves in hot water", ["more|faster"])],
     "Solubility of most solids increases with temperature, so more sugar can dissolve in hot tea, and it dissolves faster.")
u.mc("r", "Concentration tells you…", "how much solute is dissolved in a given volume", [("the temperature of a solution", "No."), ("the colour", "No."), ("the boiling point", "No.")])
u.mc("r", "Adding more sugar to the same lemonade makes the concentration…", "higher", ["lower", "stay the same", "zero"])
u.mc("r", "In a fair test of solubility and temperature, what should you change?", "Only the temperature", [("The volume of water and the temperature", "Change only one variable."), ("Nothing", "No."), ("The type of solute each time", "No.")], d="H")
u.mc("r", "Crystals form in a supersaturated solution because…", "it holds more solute than it normally can, so it is unstable", [("it is too cold to dissolve anything", "Not the reason."), ("it has no solute", "No."), ("the solvent evaporates instantly", "No.")], d="VH")
for p, r, w in [
    ("Saline used in hospitals is a…", "solution", ["pure element", "heterogeneous mixture", "solid"]),
    ("Concentration = mass of solute ÷…", "volume of solution", ["temperature", "time", "mass of container"]),
    ("A unit of concentration is…", "g/cm³", ["°C", "kg only", "N"]),
    ("A saturated solution is one where…", "no more solute will dissolve", ["more solute can dissolve", "there is no solvent", "it is boiling"]),
    ("Solubility is…", "how much solute can dissolve in a solvent", ["the colour of a solution", "the speed of stirring", "the mass of water"]),
    ("For most solids, solubility…", "increases as temperature increases", ["decreases with temperature", "never changes", "depends on colour"]),
    ("More solute particles in the same volume means…", "a higher concentration", ["a lower concentration", "a pure substance", "a gas"]),
    ("10 g of salt in 200 cm³ of solution has a concentration of…", "0.05 g/cm³", ["2 g/cm³", "20 g/cm³", "0.5 g/cm³"]),
    ("Which solution is more concentrated?", "10 g in 100 cm³", ["5 g in 100 cm³", "5 g in 500 cm³", "1 g in 100 cm³"]),
    ("Before a solution is saturated it is…", "unsaturated", ["supersaturated", "pure", "insoluble"]),
    ("A solubility graph shows solubility against…", "temperature", ["colour", "time of day", "mass of the beaker"]),
    ("Different substances have…", "different solubilities", ["the same solubility", "no solubility", "solubility only in oil"]),
    ("Diluting a solution with more water makes it…", "less concentrated", ["more concentrated", "saturated", "pure"]),
    ("To dissolve more solute in a saturated solution you could…", "heat it", ["cool it", "add less water", "stop stirring"]),
]:
    u.mc("p", p, r, w)
u.nm("p", "12 g of salt dissolves to make 300 cm³ of solution. Concentration in g/cm³?", 0.04, "g/cm³", tol=0.001)
u.gd("p", "Which solution is more concentrated?", "More concentrated", [("A: 8 g in 100 cm³ or B: 8 g in 200 cm³", "A"), ("A: 3 g in 50 cm³ or B: 9 g in 100 cm³", "B")])
u.od("p", "Order from least to most concentrated.", ["2 g in 100 cm³", "5 g in 100 cm³", "10 g in 100 cm³"])
u.ms("p", "Select ALL the variables to keep the same when testing how temperature affects solubility.", ["Volume of water", "Type of solute", "Amount of stirring"], ["Temperature", "Colour of the beaker only"])
u.gr("a", "* Advanced. Solubility of a salt (g per 100 g water) at different temperatures. Plot the points.", {"label": "Temperature (°C)", "min": 0, "max": 80, "step": 20}, {"label": "Solubility (g/100 g)", "min": 0, "max": 100, "step": 20}, [[0, 14], [20, 32], [40, 64], [60, 90]])
u.mc("a", "From the graph, what happens to solubility between 20 °C and 40 °C?", "It roughly doubles.", ["It halves.", "It stays the same.", "It falls to zero."], skill="Data")
u.nm("a", "A saturated solution at 40 °C holds 64 g in 100 g water. At 20 °C it holds 32 g. How much solid crystallises when it cools to 20 °C?", 32, "g")
u.ex("a", "* Advanced. Explain, using particles, why a solution becomes more concentrated when more solute is added to the same volume.", [("more solute particles", ["more (solute )?particles"]), ("same volume / space", ["same volume|same space|same amount of solvent"]), ("particles closer together / higher concentration", ["closer|more per|higher concentration"])],
     "Adding solute puts more solute particles into the same volume of solvent, so there are more particles per cm³ and the concentration is higher.")
u.stop("it gets sweeter", "More solute in the same volume means a…", "higher concentration", ["lower concentration", "pure solvent", "saturated solid"])
u.stop("so it's unstable, and crystals form", "A solution in which no more solute will dissolve is…", "saturated", ["unsaturated", "dilute", "pure"])
u.stop("to make it a fair test", "For most solids, solubility…", "increases with temperature", ["decreases with temperature", "is not affected", "depends on the beaker"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Mixtures and solubility", "sec": None, "kids": [
    {"id": "ps", "t": "Pure substances", "d": "Elements – 118 • Compounds – fixed ratio, chemically joined", "obj": "O1", "sec": "5.1"},
    {"id": "mx", "t": "Mixtures", "d": "Not joined • Homogeneous – evenly spread • Heterogeneous – parts visible", "obj": "O1", "sec": "5.1"},
    {"id": "pu", "t": "Purity", "d": "% purity = pure mass ÷ total mass × 100 • Medicines, implants", "obj": "O2", "sec": "5.1"},
    {"id": "sp", "t": "Separating", "d": "Handpicking • Sieving • Filtration • Evaporation • Distillation", "obj": "O3", "sec": "5.2"},
    {"id": "ch", "t": "Chromatography", "d": "Pencil line • Solvent carries dyes • One spot = pure", "obj": "O3", "sec": "5.2"},
    {"id": "co", "t": "Concentration", "d": "Mass of solute ÷ volume • g/cm³", "obj": "O4", "sec": "5.3"},
    {"id": "so", "t": "Solubility", "d": "Unsaturated • Saturated • Supersaturated • Rises with temperature", "obj": "O4", "sec": "5.3"},
]}
