# -*- coding: utf-8 -*-
"""Stage 9 Unit 8 – Rate of Reaction. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Chemistry"
BLURB = "Physical and chemical changes, conservation of mass and energy, measuring rate of reaction, collision theory, and how temperature, concentration and surface area change the rate."
OBJECTIVES = {
    "O1": {"sec": "8.1", "code": "9Cc.05", "codeNote": "", "t": "Explain why mass and energy are conserved in chemical reactions."},
    "O2": {"sec": "8.2", "code": "9Cc.04, 9TWSm.01", "codeNote": "measuring rate", "t": "Describe ways to measure rate of reaction and interpret rate graphs."},
    "O3": {"sec": "8.2", "code": "9Cc.04", "codeNote": "collision theory", "t": "Explain reactions using collision theory and activation energy."},
    "O4": {"sec": "8.3", "code": "9Cc.04, 9TWSa.03", "codeNote": "factors", "t": "Explain how temperature, concentration and surface area affect the rate of reaction, and identify anomalous results."},
}
SECTIONS = [
    {"id": "8.1", "title": "Chemical reactions", "objs": ["O1"]},
    {"id": "8.2", "title": "What is rate of reaction?", "objs": ["O2", "O3"]},
    {"id": "8.3", "title": "What factors affect the rate of reaction?", "objs": ["O4"]},
]
u = Unit(9, 8)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 8.1
u.sec("8.1", "O1")
u.gd("r", "Physical or chemical change?", "Change", [("Melting ice", "Physical"), ("Rusting", "Chemical"), ("Dissolving sugar", "Physical"), ("Frying an egg", "Chemical")])
u.tb("r", "Magnesium burns in a sealed flask. Complete the table.", ["", "Mass (g)"], [["Before reaction", "152.4"], ["After reaction", B(152.4)]])
u.gd("r", "Energy transfer in each change.", "Energy stored", [("Burning charcoal", "Chemical → heat and light"), ("Photosynthesis", "Light → chemical")], extra=["Sound → chemical"])
u.ex("r", "Explain why burnt wood seems lighter even though mass is conserved.", [("gases (carbon dioxide, water vapour) made", ["gas|carbon dioxide|water vapour|smoke"]), ("gases escape into the air", ["escape|air|leave"]), ("atoms not destroyed – mass conserved", ["not destroyed|conserv|same atoms"])],
     "Burning makes gases such as carbon dioxide and water vapour, which escape into the air. No atoms are destroyed, so the total mass is conserved; we just don't weigh the gases.")
u.mc("r", "In a chemical change…", "new substances are made", ["no new substance forms", "it is always easy to reverse", "atoms are destroyed"])
u.mc("r", "Mass is conserved in a reaction because…", "atoms are rearranged, not created or destroyed", ["atoms get heavier", "atoms disappear", "gases have no mass"])
u.mc("r", "Energy in a reaction is…", "transferred, not created or destroyed", ["created", "destroyed", "always lost forever"], d="H")
u.mc("r", "In 2H₂ + O₂ → 2H₂O, how many hydrogen atoms are on each side?", "Four", ["Two", "Six", "Eight"], d="VH")
mcs("p", [
    ("Which is a physical change?", "Melting chocolate", ["Burning paper", "Rusting iron", "Cooking an egg"]),
    ("Which is a chemical change?", "Burning wood", ["Melting ice", "Dissolving salt", "Boiling water"]),
    ("Physical changes can usually be…", "reversed", ["never undone", "seen as fire", "used to make new substances"]),
    ("In rusting, iron reacts with…", "oxygen and water", ["nitrogen", "salt only", "carbon"]),
    ("Fireworks are an example of a … reaction.", "very fast", ["very slow", "physical", "reversible"]),
    ("Rusting is a … reaction.", "slow", ["very fast", "physical", "nuclear"]),
    ("Photosynthesis stores the Sun's energy in…", "glucose", ["oxygen", "water", "carbon dioxide"]),
    ("Burning transfers chemical energy to…", "heat and light", ["mass", "atoms", "water only"]),
    ("If a reaction happens in an open flask and a gas forms, the mass on the balance…", "decreases", ["increases", "stays the same", "doubles"]),
    ("If magnesium burns in air and gains oxygen, the solid's mass…", "increases", ["decreases", "stays the same", "becomes zero"]),
    ("The law of conservation of mass says…", "total mass before = total mass after", ["mass doubles", "mass disappears", "products are lighter"]),
    ("Atoms in a reaction are…", "rearranged", ["created", "destroyed", "split into protons"]),
    ("Dissolving sugar in tea is a … change.", "physical", ["chemical", "nuclear", "irreversible"]),
    ("A sign of a chemical change is…", "a gas given off or a colour change", ["a change of shape only", "melting", "being cut"]),
    ("Energy can be … but not created or destroyed.", "transferred", ["multiplied", "stored as mass", "lost from the Universe"]),
])
u.mt("p", "Match the example to the energy transfer.", [("Burning charcoal", "chemical to heat and light"), ("Photosynthesis", "light to chemical"), ("Battery-powered torch", "chemical to light")])
u.od("p", "Order what happens when wood burns in an open fire.", ["Wood and oxygen react", "Atoms rearrange", "Carbon dioxide and water vapour form", "Gases escape, ash is left"])
u.ms("p", "Select ALL the chemical changes.", ["Burning", "Rusting", "Cooking an egg"], ["Melting ice", "Dissolving sugar"])
u.ex("a", "Describe an experiment to show that mass is conserved when two solutions react to form a precipitate.", [("measure mass of both solutions before", ["before|weigh|measure"]), ("mix in a closed container / on balance", ["mix|closed|sealed|balance"]), ("mass after is the same", ["same|equal|unchanged"])],
     "Weigh both solutions in their containers, mix them on the balance (or in a closed container), and weigh again. The total mass stays the same.")
u.nm("a", "6.0 g of magnesium reacts with oxygen to make 10.0 g of magnesium oxide. What mass of oxygen reacted?", 4.0, "g")
u.mc("a", "Why does a balloon over a flask stop the mass changing when chalk reacts with acid?", "It traps the carbon dioxide so no mass escapes", ["It adds mass", "It stops the reaction", "It cools the flask"], skill="Reasoning")
u.mc("a", "Why is it hard to reverse frying an egg?", "New substances with different properties have formed", ["The egg has lost atoms", "The egg is only melted", "Energy was destroyed"], skill="Reasoning")
u.stop("What controls how fast a reaction happens?", "Which reaction is fast?", "A firework exploding", ["Rust forming on a bike", "Food slowly decaying", "Iron rusting"])
u.stop("atoms rearrange to make new substances", "Melting ice is a … change.", "physical", ["chemical", "nuclear", "irreversible"])
u.stop("because gases escape", "Mass is conserved because atoms are…", "rearranged, not created or destroyed", ["destroyed", "created", "turned into energy"])

# ---------------------------------------------------------------- 8.2
u.sec("8.2", "O2")
u.gr("r", "Volume of gas collected in a gas syringe. Plot the points.", {"label": "Time (s)", "min": 0, "max": 60, "step": 10}, {"label": "Gas (cm³)", "min": 0, "max": 60, "step": 10}, [[0, 0], [10, 25], [20, 40], [30, 48], [40, 50], [50, 50], [60, 50]])
u.gd("r", "Using the graph: when is the reaction…", "Time (s)", [("Fastest", "0–10"), ("Stopped", "40–60")], extra=["20–30"])
u.tb("r", "Mass lost as gas escapes. Complete the table.", ["Time (s)", "Mass (g)", "Mass lost (g)"], [["0", "85.0", "0"], ["30", "84.2", B(0.8)], ["60", "83.9", B(1.1)]])
u.ex("r", "Use collision theory to explain why not every collision makes products.", [("particles must collide the right way round", ["right way|orient|direction"]), ("need enough energy – activation energy", ["enough energy|activation"]), ("only effective collisions react", ["effective"])],
     "Particles must collide the right way round and with at least the activation energy to break bonds. Only these effective collisions make products.", o="O3")
u.mc("r", "The rate of reaction is…", "how fast or slowly a reaction happens", ["the mass of product", "the temperature of the reaction", "the colour change"])
u.mc("r", "Activation energy is…", "the minimum energy particles need to react", ["the energy given out", "the energy of the products", "the maximum energy"], o="O3")
u.mc("r", "Why does vinegar and baking soda fizz fast at first, then slow down?", "Reactants are used up, so there are fewer collisions", ["The vinegar gets colder", "More reactants are made", "The fizzing makes particles faster"], o="O3", d="H")
u.mc("r", "On a rate graph, the line becomes flat. This means…", "the reaction has stopped", ["the reaction is fastest", "the reaction is speeding up", "gas is being absorbed"], d="VH")
mcs("p", [
    ("An airbag inflates in about…", "30 milliseconds", ["30 seconds", "3 minutes", "3 hours"]),
    ("Food decaying is a … reaction.", "slow", ["very fast", "explosive", "physical"]),
    ("Gas made in a reaction can be collected in a…", "gas syringe", ["test tube rack", "Bunsen burner", "evaporating dish"]),
    ("Another way to measure rate is to measure the…", "mass lost as gas escapes", ["colour of the flask", "size of the beaker", "number of atoms"]),
    ("On a rate graph, the steepest part shows…", "the fastest rate", ["the slowest rate", "the end", "no reaction"]),
    ("Reactions happen when particles…", "collide", ["stop moving", "freeze", "repel forever"], "O3"),
    ("A collision that makes products is called…", "effective", ["useless", "elastic", "neutral"], "O3"),
    ("Particles must collide with enough energy to…", "break bonds", ["make atoms", "destroy mass", "change colour"], "O3"),
    ("A reaction stops when…", "a reactant runs out", ["the gas syringe is full always", "the temperature rises", "it starts fizzing"], "O3"),
    ("Some medicines are designed to react…", "slowly, over many hours", ["only in fire", "never", "only in cold water"]),
    ("Measurements of gas volume are taken…", "at regular time intervals", ["once only", "at random times", "after the reaction only"]),
    ("Rate of reaction can be calculated as…", "amount of product ÷ time", ["time ÷ product", "product × time", "mass + time"]),
    ("Collision theory compares reacting particles meeting the right way to…", "puzzle pieces fitting", ["cars parking", "magnets repelling", "balls bouncing"], "O3"),
    ("Fewer particles left means…", "fewer collisions", ["more collisions", "faster reaction", "more products"], "O3"),
    ("In a gas syringe experiment, the total volume of gas at the end depends on…", "the amount of reactants", ["the shape of the syringe", "the colour of the flask", "the time of day"]),
])
u.mt("p", "Match the reaction to its speed.", [("Firework", "very fast"), ("Rusting", "slow"), ("Baking a cake", "medium")])
u.od("p", "Order the events in a reaction from start to finish.", ["Many particles collide", "Products form quickly", "Reactants get used up", "Collisions become fewer", "Reaction stops"], o="O3")
u.ms("p", "Select ALL the conditions for an effective collision.", ["Particles collide", "Correct orientation", "At least the activation energy"], ["Particles stay still", "Particles are the same colour"], o="O3")
u.ex("a", "Using the gas syringe graph (25 cm³ in the first 10 s, 15 cm³ in the next 10 s), explain how the rate changes.", [("rate fastest at start", ["fastest|start|first"]), ("rate slows as reactants used up", ["slow|used up|fewer"]), ("calculation e.g. 2.5 cm³/s then 1.5 cm³/s", ["2\\.5|1\\.5"])],
     "The rate is fastest at the start (25 ÷ 10 = 2.5 cm³/s) and slows to 1.5 cm³/s in the next 10 s, because reactants are used up so there are fewer collisions.")
u.nm("a", "40 cm³ of gas is collected in 16 s. What is the average rate?", 2.5, "cm³/s")
u.mc("a", "Why does a lit match need to be struck before it burns?", "Striking supplies the activation energy", ["Striking adds oxygen atoms", "It makes the match heavier", "It removes the activation energy"], o="O3", skill="Reasoning")
u.mc("a", "Why should the gas syringe be connected before adding the acid?", "Otherwise gas escapes before it can be measured", ["To heat the acid", "To stop the reaction", "To change the volume"], skill="Enquiry")
u.stop("an airbag inflates in 30 milliseconds!", "Rate of reaction means…", "how fast a reaction happens", ["how much product forms", "how hot it gets", "how big the flask is"])
u.stop("when it's flat, the reaction has stopped", "On a rate graph, the fastest part is…", "the steepest part", ["the flat part", "the end", "the lowest point"])
u.stop("This minimum energy is the activation energy", "The minimum energy needed to react is the…", "activation energy", ["kinetic energy", "light energy", "nuclear energy"], o="O3")

# ---------------------------------------------------------------- 8.3
u.sec("8.3", "O4")
u.gd("r", "Does each change make the reaction faster or slower?", "Effect", [("Raising the temperature", "Faster"), ("Using more dilute acid", "Slower"), ("Using powder instead of lumps", "Faster"), ("Cooling the mixture", "Slower")])
u.gr("r", "Gas from marble chips (A) and powder (B). Plot powder B.", {"label": "Time (s)", "min": 0, "max": 50, "step": 10}, {"label": "Gas (cm³)", "min": 0, "max": 60, "step": 10}, [[0, 0], [10, 40], [20, 55], [30, 60], [40, 60], [50, 60]])
u.tb("r", "Time for a tablet to dissolve. One result is anomalous. Complete the mean of the other two.", ["Temperature (°C)", "Trial 1 (s)", "Trial 2 (s)", "Trial 3 (s)", "Mean of reliable results (s)"], [["40", "30", "62", "32", B(31)]])
u.ex("r", "Use collision theory to explain why raising the temperature speeds up a reaction.", [("particles gain kinetic energy / move faster", ["kinetic|faster|move"]), ("collide more often", ["more often|more frequent|more collisions"]), ("more collisions have activation energy / effective", ["activation|effective|harder|enough energy"])],
     "At a higher temperature particles have more kinetic energy and move faster, so they collide more often and harder. More collisions have the activation energy, so there are more effective collisions.")
u.mc("r", "Increasing concentration speeds up a reaction because…", "there are more particles in the same volume, so more collisions", ["particles get bigger", "particles slow down", "the activation energy rises"])
u.mc("r", "Powdered calcium carbonate reacts faster than marble chips because…", "it has a larger surface area", ["it is a different substance", "it is hotter", "it has fewer particles"])
u.mc("r", "Powder and chips of the same mass give the same total volume of gas because…", "the same amount of reactant makes the same amount of product", ["powder makes less gas", "chips make more gas", "the gas escapes"], d="H")
u.mc("r", "One result is far from the others. What should you do?", "Repeat that measurement to check it", ["Ignore all the results", "Change the method completely", "Make up a new value"], d="VH")
mcs("p", [
    ("An effervescent tablet fizzes faster in…", "hot water", ["cold water", "ice", "no water"]),
    ("Higher concentration is like a…", "crowded room", ["empty room", "frozen lake", "closed door"]),
    ("Breaking a lump into small pieces increases its…", "surface area", ["mass", "concentration", "temperature"]),
    ("A larger surface area means more particles are…", "exposed to collide", ["hidden", "destroyed", "cooled"]),
    ("Raising temperature gives particles more…", "kinetic energy", ["mass", "protons", "colour"]),
    ("On a graph, the faster reaction's line is…", "steeper at the start", ["flatter at the start", "lower at the end", "a straight horizontal line"]),
    ("A result that doesn't fit the pattern is…", "anomalous", ["average", "reliable", "accurate"]),
    ("An anomalous result might be caused by…", "a measuring error", ["the law of conservation", "a perfect method", "a fair test"]),
    ("Food lasts longer in a fridge because…", "low temperature slows reactions", ["cold kills all atoms", "fridges remove oxygen", "food gets heavier"]),
    ("Which reacts fastest with acid?", "Magnesium powder", ["One magnesium lump", "Magnesium ribbon in cold dilute acid", "A large magnesium block"]),
    ("More dilute acid has … particles in the same volume.", "fewer", ["more", "the same", "no"]),
    ("Chewing food helps digestion by…", "increasing surface area", ["lowering temperature", "reducing concentration", "removing enzymes"]),
    ("Flour dust can explode because it has…", "a huge surface area", ["a small surface area", "no particles", "low energy"]),
    ("To make a fair test of temperature, you must keep … the same.", "concentration and surface area", ["temperature", "nothing", "only the time"]),
    ("Two lines end at the same height. This shows…", "the same amount of product formed", ["one reaction made no product", "both stopped instantly", "the lines are wrong"]),
])
u.ms("p", "Select ALL the changes that increase the rate.", ["Higher temperature", "Higher concentration", "Larger surface area"], ["Lower temperature", "Bigger lumps"])
u.mt("p", "Match the change to the reason it speeds up the reaction.", [("Higher temperature", "particles move faster"), ("Higher concentration", "more particles in the same volume"), ("Powder", "more particles exposed")])
u.od("p", "Order from slowest to fastest reaction with acid.", ["One large marble chip", "Several small marble chips", "Marble powder"])
u.ex("a", "Plan an investigation into how acid concentration affects the rate of reaction with magnesium.", [("change concentration only", ["concentration"]), ("keep temperature, magnesium mass/length, acid volume same", ["same|control|temperature|volume|length"]), ("measure gas volume or time / repeat", ["gas syringe|time|measure|repeat"])],
     "Use several concentrations of acid. Keep the volume of acid, temperature and length of magnesium ribbon the same. Measure the time for the magnesium to disappear or the gas made in a gas syringe, and repeat each test.")
u.mc("a", "A 10 °C rise roughly doubles a rate. A reaction takes 80 s at 20 °C. Estimate the time at 30 °C.", "40 s", ["160 s", "80 s", "20 s"], skill="Application")
u.mc("a", "Why does a 1 cm cube cut into 1 mm cubes react much faster?", "Its total surface area is ten times greater", ["Its mass is ten times greater", "It becomes a different substance", "It is hotter"], skill="Reasoning")
u.mc("a", "Results for 20, 30, 40, 50 °C were 64 s, 33 s, 70 s, 9 s. Which is anomalous?", "70 s at 40 °C", ["64 s at 20 °C", "33 s at 30 °C", "9 s at 50 °C"], skill="Data")
u.stop("much faster in hot water than in cold", "Raising the temperature makes particles…", "move faster", ["move slower", "get bigger", "stop"])
u.stop("More collisions means a faster reaction", "Higher concentration means…", "more particles in the same volume", ["bigger particles", "slower particles", "no collisions"])
u.stop("both make the same total amount of gas", "Powder reacts faster than lumps because it has a larger…", "surface area", ["mass", "volume of acid", "temperature"])
u.stop("so repeat that measurement to check", "A result that does not fit the pattern is…", "anomalous", ["reliable", "accurate", "average"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Rate of reaction", "sec": None, "kids": [
    {"id": "ch", "t": "Changes", "d": "Physical: reversible, no new substance • Chemical: new substances", "obj": "O1", "sec": "8.1"},
    {"id": "cs", "t": "Conservation", "d": "Mass: atoms rearranged • Energy: transferred", "obj": "O1", "sec": "8.1"},
    {"id": "ms", "t": "Measuring rate", "d": "Gas syringe • Mass lost • Steepest = fastest, flat = stopped", "obj": "O2", "sec": "8.2"},
    {"id": "ct", "t": "Collision theory", "d": "Right way round • Activation energy • Effective collisions", "obj": "O3", "sec": "8.2"},
    {"id": "fc", "t": "Factors", "d": "Temperature • Concentration • Surface area • Anomalous results", "obj": "O4", "sec": "8.3"},
]}
