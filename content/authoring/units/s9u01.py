# -*- coding: utf-8 -*-
"""Stage 9 Unit 1 – Photosynthesis and Transport in Plants. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Biology"
BLURB = "How plants make glucose by photosynthesis, how leaves are adapted for it, testing a leaf for starch, and how water and mineral salts travel from roots to leaves."
OBJECTIVES = {
    "O1": {"sec": "1.1", "code": "9Bp.07", "codeNote": "", "t": "Describe photosynthesis using its word equation and explain where the energy in food chains comes from."},
    "O2": {"sec": "1.1", "code": "9Bp.06, 9TWSp.04", "codeNote": "", "t": "Describe how leaves and chloroplasts are adapted for photosynthesis and test a leaf for starch."},
    "O3": {"sec": "1.2", "code": "9Bp.05", "codeNote": "", "t": "Explain why plants need water, nitrates and magnesium."},
    "O4": {"sec": "1.2", "code": "9Bs.01", "codeNote": "", "t": "Describe how root hairs absorb water and how xylem and transpiration move water up a plant."},
}
SECTIONS = [
    {"id": "1.1", "title": "Photosynthesis", "objs": ["O1", "O2"]},
    {"id": "1.2", "title": "Absorption and transport of water and mineral salts", "objs": ["O3", "O4"]},
]
u = Unit(9, 1)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 1.1
u.sec("1.1", "O1")
u.gd("r", "Reactant or product of photosynthesis?", "Role", [("Carbon dioxide", "Reactant"), ("Water", "Reactant"), ("Glucose", "Product"), ("Oxygen", "Product")])
u.gd("r", "Starch test results. Which colour does iodine show?", "Colour", [("Leaf kept in bright light", "Blue-black"), ("Leaf kept in the dark for 48 hours", "Brown"), ("Covered half of a leaf in light", "Brown"), ("Uncovered half of the same leaf", "Blue-black")], o="O2")
u.od("r", "Order the steps of testing a leaf for starch.", ["Boil the leaf in water", "Heat it in ethanol in a hot water bath", "Soften it in hot water", "Add iodine solution"], o="O2")
u.ex("r", "Explain why a leaf is boiled in ethanol before testing it for starch.", [("removes the chlorophyll / green colour", ["chlorophyll|green|colour|decolou"]), ("so the colour change is easy to see", ["see|colour change|blue-black|clear"])],
     "Ethanol removes the green chlorophyll, so the leaf turns pale and the iodine colour change can be seen clearly.", o="O2")
u.mc("r", "Which is the word equation for photosynthesis?", "carbon dioxide + water → glucose + oxygen", ["glucose + oxygen → carbon dioxide + water", "oxygen + water → glucose + carbon dioxide", "glucose + water → carbon dioxide + oxygen"])
u.mc("r", "Photosynthesis takes place in…", "chloroplasts", ["mitochondria", "the nucleus", "the cell wall"], o="O2")
u.mc("r", "Why are leaves thin?", "So gases diffuse in and out quickly", [("To store more starch", "No."), ("To keep out light", "No."), ("To hold more water", "No.")], o="O2", d="H")
u.mc("r", "Why is the plant kept in the dark for 48 hours before the light experiment?", "To use up the starch already in its leaves", ["To make more chlorophyll", "To kill the plant", "To make the leaf thinner"], o="O2", d="VH")
mcs("p", [
    ("Plants are called producers because they…", "make their own food", ["eat other plants", "break down dead matter", "only absorb food from soil"]),
    ("The energy for photosynthesis comes from…", "light", ["the soil", "oxygen", "glucose"]),
    ("Plants take in carbon dioxide from…", "the air", ["the soil", "the roots only", "water"]),
    ("Plants take in water from…", "the soil", ["the air", "sunlight", "chlorophyll"]),
    ("'Photo' means…", "from light", ["putting together", "green", "water"]),
    ("'Synthesis' means…", "putting together", ["breaking down", "light", "sugar"]),
    ("The sugar made in photosynthesis is…", "glucose", ["starch", "protein", "fat"]),
    ("New plant cells and tissues are called…", "biomass", ["chlorophyll", "stomata", "xylem"]),
    ("Extra glucose is stored as…", "starch", ["oxygen", "chlorophyll", "nitrates"]),
    ("Chlorophyll is…", "a green pigment that absorbs light", ["a type of sugar", "a gas", "a mineral salt"], "O2"),
    ("Tiny openings that let gases in and out of a leaf are…", "stomata", ["root hairs", "xylem", "chloroplasts"], "O2"),
    ("Stomata are mostly found on…", "the underside of leaves", ["the roots", "the flowers", "the top of the stem"], "O2"),
    ("Leaves have a large surface area to…", "capture more sunlight", ["store water", "keep out gases", "make roots grow"], "O2"),
    ("Iodine solution is normally…", "brown", ["blue-black", "green", "colourless"], "O2"),
    ("Why must you be careful heating ethanol?", "It is flammable", ["It is radioactive", "It freezes", "It turns blue"], "O2"),
])
u.ms("p", "Select ALL the places a plant can store starch.", ["Leaves", "Roots", "Stems", "Fruits"], ["Stomata", "Chlorophyll"])
u.mt("p", "Match the part to its job in photosynthesis.", [("Chlorophyll", "absorbs light"), ("Stomata", "let gases in and out"), ("Root hairs", "absorb water")], o="O2")
u.od("p", "Order the energy flow.", ["Sun", "Plant (producer)", "Herbivore", "Carnivore"])
u.ex("a", "Explain how cutting down forests could affect the amount of carbon dioxide and oxygen in the air.", [("fewer trees photosynthesise", ["fewer|less photosynth|photosynth"]), ("less carbon dioxide removed / more stays", ["carbon dioxide|co2"]), ("less oxygen released", ["oxygen"])],
     "With fewer trees, less photosynthesis happens, so less carbon dioxide is taken out of the air and less oxygen is released.")
u.ex("a", "A variegated leaf has green and white parts. After testing for starch, only the green parts turn blue-black. Explain what this shows.", [("white parts have no chlorophyll", ["no chlorophyll|white.*chlorophyll|chlorophyll"]), ("photosynthesis needs chlorophyll", ["need|requires"])],
     "The white parts have no chlorophyll, so they cannot photosynthesise or make starch. This shows photosynthesis needs chlorophyll.", o="O2")
u.mc("a", "Why should the light experiment use a control, such as the uncovered half of the leaf?", "To show that light is the only factor that differs", ["To make the leaf grow faster", "To use up starch", "To remove chlorophyll"], o="O2", skill="Enquiry")
u.mc("a", "Why do we say the energy in every food chain comes from the Sun?", "Producers capture light energy and store it in glucose, which passes along the chain", ["Animals absorb sunlight directly", "Glucose is made in the Sun", "Soil contains sunlight"], skill="Reasoning")
u.stop("which uses carbon dioxide", "Plants are producers because they…", "make their own food", ["eat animals", "decompose waste", "live in soil"])
u.stop("makes glucose plus oxygen", "The products of photosynthesis are…", "glucose and oxygen", ["carbon dioxide and water", "starch and nitrogen", "oxygen and water"])
u.stop("Root hairs give roots a huge surface area for absorbing water", "Photosynthesis happens in…", "chloroplasts", ["mitochondria", "root hairs", "stomata"], o="O2")
u.stop("turns blue-black when starch is present", "Iodine turns blue-black when … is present.", "starch", ["glucose", "oxygen", "water"], o="O2")

# ---------------------------------------------------------------- 1.2
u.sec("1.2", "O3")
u.gd("r", "Which mineral salt is needed for each job?", "Mineral", [("Making proteins", "Nitrates"), ("Making chlorophyll (the central atom)", "Magnesium")], extra=["Iron"])
u.gd("r", "Turgid or flaccid?", "State", [("Vacuole full of water pushing on the cell wall", "Turgid"), ("Cell short of water, plant wilting", "Flaccid"), ("Firm, upright stem", "Turgid")], o="O4")
u.od("r", "Order the path of water through a plant.", ["Soil", "Root hair cell", "Xylem in the root", "Xylem in the stem", "Leaf", "Evaporates out of stomata"], o="O4")
u.ex("r", "Explain how transpiration helps move water up a plant.", [("water evaporates from leaves", ["evaporat"]), ("escapes through stomata", ["stomata"]), ("pulls more water up the xylem", ["pull|xylem|straw|draws"])],
     "Water evaporates in the leaves and escapes through the stomata. This pulls more water up the xylem from the roots, like drinking through a straw.", o="O4")
u.mc("r", "Without nitrates, a plant's leaves turn…", "pale or yellow", ["blue-black", "red", "darker green"])
u.mc("r", "Water moves into root hair cells because…", "the soil has a higher water concentration than the cells", ["the cells have more water than the soil", "light pulls it in", "the xylem pushes it"], o="O4", d="H")
u.mc("r", "Xylem vessels are…", "hollow tubes of dead cells with thick, stiff walls", ["living cells full of chlorophyll", "tiny holes in leaves", "root hairs"], o="O4", d="H")
u.mc("r", "Why do farmers add fertilisers to fields?", "To replace mineral salts like nitrates that crops need", ["To kill insects", "To make the soil acidic", "To stop photosynthesis"], d="VH")
mcs("p", [
    ("Water is a raw material for…", "photosynthesis", ["respiration only", "digestion", "fertilisation"]),
    ("Seeds need water to…", "germinate", ["photosynthesise", "flower", "die"]),
    ("Transpiration helps a plant control its…", "temperature", ["colour", "height", "flowers"]),
    ("A plant short of water…", "wilts", ["grows faster", "turns blue", "makes more starch"]),
    ("Magnesium is needed to make…", "chlorophyll", ["starch", "xylem", "oxygen"]),
    ("Nitrates are needed to make proteins and…", "chlorophyll", ["glucose only", "water", "oxygen"]),
    ("Roots anchor the plant and…", "absorb water and mineral salts", ["make glucose", "release oxygen", "absorb light"], "O4"),
    ("Root hairs give the root…", "a huge surface area", ["a waxy coat", "chloroplasts", "stomata"], "O4"),
    ("Water and mineral salts travel up the plant in the…", "xylem", ["stomata", "chloroplasts", "root hairs"], "O4"),
    ("Xylem cells have lost their…", "contents and end walls", ["walls completely", "water", "roots"], "O4"),
    ("The loss of water vapour from leaves is called…", "transpiration", ["photosynthesis", "respiration", "germination"], "O4"),
    ("Water vapour leaves through the…", "stomata", ["roots", "xylem", "flowers"], "O4"),
    ("A turgid cell is…", "firm and full of water", ["empty and floppy", "dead", "dry"], "O4"),
    ("Mineral salts enter the root…", "dissolved in water", ["as gases", "through the leaves", "as solid crystals"], "O4"),
    ("The thick walls of xylem help to…", "support the plant", ["make glucose", "absorb light", "store starch"], "O4"),
])
u.ms("p", "Select ALL the reasons plants need water.", ["Raw material for photosynthesis", "Carries dissolved mineral salts", "Keeps cells turgid", "Helps control temperature"], ["Makes chlorophyll green", "Absorbs light"])
u.mt("p", "Match the structure to its adaptation.", [("Root hair", "large surface area"), ("Xylem", "hollow tube"), ("Leaf", "thin with stomata")], o="O4")
u.tb("p", "A plant's mass was recorded as it lost water by transpiration. Complete the table.", ["Time (h)", "Mass (g)", "Water lost since start (g)"], [["0", "250", "0"], ["4", "238", B(12)]], o="O4")
u.ex("a", "Predict and explain what happens to the rate of transpiration on a hot, windy day.", [("rate increases", ["increase|faster|more"]), ("more evaporation in heat", ["heat|hot|evaporat"]), ("wind carries water vapour away", ["wind|carr|away"])],
     "Transpiration increases: heat makes water evaporate faster and wind carries water vapour away from the leaf, so more water leaves the stomata.", o="O4")
u.nm("a", "A plant lost 18 g of water in 6 hours. What was the average rate of water loss?", 3, "g/h", o="O4")
u.mc("a", "Why do plants with yellow leaves grow slowly?", "Without enough chlorophyll they photosynthesise less, so make less glucose", ["Yellow leaves make too much glucose", "Yellow leaves have more stomata", "They absorb too much water"], skill="Reasoning")
u.mc("a", "A cut celery stalk is put in coloured water. After a few hours the colour appears in thin tubes in the stalk. These tubes are…", "xylem", ["stomata", "root hairs", "chloroplasts"], o="O4", skill="Evidence")
u.stop("seeds need it to germinate", "Which is a use of water in a plant?", "A raw material for photosynthesis", ["Making magnesium", "Absorbing light", "Making iodine"])
u.stop("so farmers add fertilisers", "Nitrates are used to make…", "proteins and chlorophyll", ["starch only", "oxygen", "xylem walls"])
u.stop("forming long hollow tubes with thick, stiff walls", "Water travels up a plant in the…", "xylem", ["stomata", "chloroplasts", "root hairs"], o="O4")

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Photosynthesis and transport", "sec": None, "kids": [
    {"id": "eq", "t": "Photosynthesis", "d": "Carbon dioxide + water → glucose + oxygen • Light and chlorophyll • Makes biomass", "obj": "O1", "sec": "1.1"},
    {"id": "lf", "t": "Leaf adaptations", "d": "Large surface area • Thin • Stomata • Chloroplasts", "obj": "O2", "sec": "1.1"},
    {"id": "st", "t": "Starch test", "d": "Boil • Ethanol • Iodine: brown → blue-black • Needs light", "obj": "O2", "sec": "1.1"},
    {"id": "mn", "t": "Water and minerals", "d": "Turgid cells • Nitrates for proteins • Magnesium for chlorophyll", "obj": "O3", "sec": "1.2"},
    {"id": "tr", "t": "Transport", "d": "Root hairs absorb • Xylem carries • Transpiration pulls", "obj": "O4", "sec": "1.2"},
]}
