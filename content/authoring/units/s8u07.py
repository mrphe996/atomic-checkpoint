# -*- coding: utf-8 -*-
"""Stage 8 Unit 7 – Exothermic and Endothermic Changes. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Chemistry"
BLURB = "Reactions and processes that release heat or take it in: combustion, neutralisation, freezing and heat packs; decomposition, photosynthesis, melting and cold packs."
OBJECTIVES = {
    "O1": {"sec": "7.1", "code": "8Cc.02, 8Cc.01", "codeNote": "", "t": "Identify exothermic reactions from a temperature rise and give examples such as combustion, neutralisation and respiration."},
    "O2": {"sec": "7.1", "code": "8Cc.02, 8Cc.04", "codeNote": "", "t": "Describe exothermic processes such as freezing, dissolving and crystallisation, and their uses."},
    "O3": {"sec": "7.2", "code": "8Cc.02", "codeNote": "", "t": "Identify endothermic reactions from a temperature fall and give examples such as thermal decomposition and photosynthesis."},
    "O4": {"sec": "7.2", "code": "8Cc.02, 8TWSc.04", "codeNote": "", "t": "Describe endothermic processes such as melting, evaporation and dissolving some salts, and measure temperature changes."},
}
SECTIONS = [
    {"id": "7.1", "title": "Exothermic changes", "objs": ["O1", "O2"]},
    {"id": "7.2", "title": "Endothermic changes", "objs": ["O3", "O4"]},
]
u = Unit(8, 7)

# ---------------------------------------------------------------- 7.1
u.sec("7.1", "O1")
u.gd("r", "Which type of exothermic reaction is each?", "Type", [("Burning methane", "Combustion"), ("Acid + alkali", "Neutralisation"), ("Cement setting", "Hydration"), ("Iron slowly reacting in damp air", "Rusting")])
u.tb("r", "Temperature before and after mixing. Complete the change.", ["Reaction", "Start (°C)", "End (°C)", "Change (°C)"], [["Acid + alkali", "21", "29", B(8)], ["Plaster of Paris + water", "20", "34", B(14)]])
u.mc("r", "In an exothermic reaction the temperature of the surroundings…", "goes up", [("goes down", "That is endothermic."), ("stays the same", "No."), ("becomes zero", "No.")])
u.ex("r", "Explain why a setting plaster cast feels warm.", [("plaster reacts with water", ["react|water|gypsum"]), ("exothermic", ["exothermic"]), ("releases heat to the surroundings / skin", ["release|give.*heat|heat"])],
     "Plaster of Paris reacts with water to form gypsum. This reaction is exothermic, so it releases heat to the surroundings and the cast feels warm.")
u.mc("r", "Why is freezing water an exothermic process?", "Particles lose energy as they lock into place, releasing heat", [("Particles gain energy", "That is melting."), ("New substances are made", "No – it is a physical change."), ("It takes in heat", "No.")], o="O2")
u.mc("r", "How does an instant heat pack work?", "A substance dissolves exothermically and releases heat", [("It takes in heat from the skin", "That is a cold pack."), ("It burns fuel", "No."), ("It contains ice", "No.")], o="O2", d="H")
u.mc("r", "In an exothermic reaction the products have…", "less energy than the reactants", [("more energy than the reactants", "That is endothermic."), ("no energy", "No."), ("the same energy", "No.")], d="H")
u.mc("r", "Why might a biogas digester help families without clean fuel?", "Bacteria turn waste into biogas, a cleaner fuel that burns exothermically for cooking", [("It makes electricity from ice", "No."), ("It cools food", "No."), ("It turns biogas into manure", "Reversed.")], d="VH")
for p, r, w, o in [
    ("'Exo' means…", "out", ["in", "cold", "slow"], "O1"),
    ("'Thermic' means…", "heat", ["light", "sound", "water"], "O1"),
    ("When wood burns, chemical energy is released as…", "heat and light", ["only sound", "cold", "water"], "O1"),
    ("A sparkler gives off…", "heat and light", ["only cold", "only sound", "nothing"], "O1"),
    ("Combustion is…", "burning fuel in oxygen", ["dissolving salt", "freezing water", "melting ice"], "O1"),
    ("Neutralisation makes a salt and…", "water", ["oxygen", "hydrogen only", "carbon"], "O1"),
    ("Hydration is a substance reacting with…", "water", ["oxygen", "acid", "metal"], "O1"),
    ("Sodium reacting with water is…", "exothermic", ["endothermic", "not a reaction", "a physical change"], "O1"),
    ("Rusting releases heat…", "slowly", ["very fast", "never", "only at night"], "O1"),
    ("Aerobic respiration releases energy from…", "glucose", ["carbon dioxide", "water", "salt"], "O1"),
    ("A reaction often makes…", "a mixture of substances", ["only one pure product", "no products", "only gases"], "O1"),
    ("Freezing is a…", "physical change", ["chemical reaction", "new substance", "combustion"], "O2"),
    ("Dissolving calcium chloride in water makes the solution…", "warm", ["cold", "freeze", "boil instantly"], "O2"),
    ("A reusable hand warmer heats up when it…", "crystallises", ["melts", "evaporates", "dissolves in ice"], "O2"),
    ("A reusable hand warmer reaches about…", "54 °C", ["0 °C", "100 °C", "−20 °C"], "O2"),
]:
    u.mc("p", p, r, w, o=o)
u.gd("p", "Chemical reaction or physical process? (both exothermic)", "Type", [("Combustion", "Chemical reaction"), ("Freezing", "Physical process"), ("Neutralisation", "Chemical reaction"), ("Crystallisation", "Physical process")], o="O2")
u.ms("p", "Select ALL the exothermic changes.", ["Burning wood", "Water freezing", "Respiration"], ["Ice melting", "Photosynthesis"])
u.mt("p", "Match the use to the exothermic change.", [("Instant heat pack", "dissolving releases heat"), ("Reusable hand warmer", "crystallisation"), ("Cooking stove", "combustion")], o="O2")
u.ex("a", "* Advanced. Explain, in terms of particles, why water releases heat as it freezes.", [("particles lose energy", ["lose energy|less energy"]), ("slow down / lock into fixed positions", ["slow|fixed|lock"]), ("energy transferred to surroundings as heat", ["surroundings|release|give"])],
     "As water freezes its particles lose energy, slow down and lock into fixed positions. The energy they lose is transferred to the surroundings as heat.", o="O2")
u.nm("a", "A reaction starts at 18.5 °C and reaches 31.0 °C. What is the temperature rise?", 12.5, "°C", tol=0.05)
u.mc("a", "Why is a thermometer reading more useful than touching a beaker to decide if a reaction is exothermic?", "It measures the change accurately instead of guessing.", ["Touch is always more accurate.", "Thermometers measure mass.", "There is no difference."], skill="Reasoning")
u.mc("a", "Why do the products of combustion have less energy than the fuel and oxygen?", "Energy was transferred to the surroundings as heat and light.", ["Energy was destroyed.", "Products always weigh less.", "Oxygen absorbs all the energy."], skill="Reasoning")
u.stop("so the temperature goes up", "In an exothermic reaction, the temperature…", "goes up", ["goes down", "stays the same", "falls to zero"])
u.stop("to make a salt and water", "Neutralisation is an acid reacting with…", "an alkali", ["a metal only", "oxygen", "ice"])
u.stop("heating up to about 54 degrees Celsius", "Freezing water is…", "an exothermic process", ["an endothermic process", "a chemical reaction", "combustion"], o="O2")

# ---------------------------------------------------------------- 7.2
u.sec("7.2", "O3")
u.gd("r", "Exothermic or endothermic?", "Type", [("Photosynthesis", "Endothermic"), ("Combustion", "Exothermic"), ("Thermal decomposition", "Endothermic"), ("Ice melting", "Endothermic")])
u.tb("r", "Temperature change when dissolving. Complete the table.", ["Substance", "Start (°C)", "End (°C)", "Change (°C)"], [["Ammonium chloride", "20", "12", B(-8)], ["Calcium chloride", "20", "31", B(11)]], o="O4")
u.mc("r", "In an endothermic reaction the mixture feels…", "cold, because it takes in heat", [("warm", "That is exothermic."), ("the same", "No."), ("sticky", "No.")])
u.ex("r", "Explain why hand sanitiser makes your hands feel cold.", [("it evaporates", ["evaporat"]), ("evaporation takes in heat", ["take.*heat|absorb|endothermic"]), ("heat from your skin", ["skin|hand"])],
     "The sanitiser evaporates, and evaporation is endothermic – the liquid takes in heat from your skin to escape as a gas, so your hands feel cold.", o="O4")
u.mc("r", "Heating green copper carbonate gives black copper oxide and…", "carbon dioxide", ["oxygen", "water only", "copper"])
u.mc("r", "Photosynthesis is endothermic because plants…", "take in light energy and store it in glucose", [("give out heat", "No."), ("burn sugar", "No."), ("release oxygen as heat", "No.")], d="H")
u.mc("r", "In an endothermic reaction the products have…", "more energy than the reactants", [("less energy", "That is exothermic."), ("no energy", "No."), ("the same energy", "No.")], d="H")
u.mc("r", "Why is baking bread endothermic?", "The dough absorbs heat from the oven to drive the reactions", [("Bread gives out heat", "No."), ("It freezes", "No."), ("The oven absorbs heat from bread", "Reversed.")], d="VH")
for p, r, w, o in [
    ("'Endo' means…", "in", ["out", "hot", "fast"], "O3"),
    ("Sherbet with water feels…", "cold and fizzy", ["hot", "sticky", "salty only"], "O3"),
    ("Sherbet contains citric acid and…", "baking soda", ["salt", "sugar only", "iron"], "O3"),
    ("Thermal decomposition means…", "breaking down a substance using heat", ["burning in oxygen", "freezing", "dissolving"], "O3"),
    ("Photosynthesis stores energy as chemical energy in…", "glucose", ["oxygen", "water", "carbon dioxide"], "O3"),
    ("When ice melts its particles…", "take in heat and vibrate faster", ["lose heat", "stop moving", "become new substances"], "O4"),
    ("Evaporation is…", "endothermic", ["exothermic", "a combustion reaction", "freezing"], "O4"),
    ("Cold packs often contain…", "ammonium chloride", ["calcium chloride", "sodium", "plaster"], "O4"),
    ("The Sun evaporates seawater in salt ponds by…", "providing heat", ["removing heat", "adding salt", "freezing it"], "O4"),
    ("A temperature fall shows a change is…", "endothermic", ["exothermic", "neutral", "pure"], "O4"),
    ("Melting is a…", "physical change", ["chemical reaction", "combustion", "neutralisation"], "O4"),
    ("Which is endothermic?", "Dissolving ammonium chloride", ["Burning wood", "Respiration", "Freezing water"], "O4"),
    ("To measure a temperature change accurately, use…", "a thermometer", ["your hand", "a ruler", "a balance"], "O4"),
    ("When a liquid evaporates its particles…", "gain enough energy to escape as a gas", ["lose energy", "lock into place", "become solid"], "O4"),
    ("Cold packs are used for…", "sports injuries", ["cooking", "lighting", "heating rooms"], "O4"),
]:
    u.mc("p", p, r, w, o=o)
u.gd("p", "Does the temperature go up or down?", "Temperature", [("Exothermic reaction", "Up"), ("Endothermic reaction", "Down"), ("Dissolving ammonium chloride", "Down"), ("Dissolving calcium chloride", "Up")], o="O4")
u.ms("p", "Select ALL the endothermic changes.", ["Melting", "Evaporation", "Photosynthesis"], ["Freezing", "Combustion"])
u.mt("p", "Match the change to its opposite.", [("Melting (endothermic)", "freezing (exothermic)"), ("Evaporating (endothermic)", "condensing (exothermic)")], o="O4")
u.ex("a", "* Advanced. Design an investigation to find out whether dissolving a new salt is exothermic or endothermic.", [("measure start temperature of water", ["start|initial|before"]), ("add salt, stir, measure end temperature", ["after|end|final|stir"]), ("rise = exothermic, fall = endothermic", ["rise|fall|up|down"])],
     "Measure the starting temperature of some water, add the salt, stir and measure the lowest or highest temperature. A rise means exothermic; a fall means endothermic.", o="O4")
u.nm("a", "A cold pack starts at 22 °C and falls by 15 °C. What is its final temperature?", 7, "°C", o="O4")
u.mc("a", "Why are melting and freezing opposite in energy terms?", "Melting takes in heat; freezing releases the same amount of heat.", ["Both release heat.", "Both take in heat.", "Neither involves energy."], o="O4", skill="Reasoning")
u.gr("a", "* Advanced. Temperature of a mixture during an endothermic reaction. Plot the points.", {"label": "Time (s)", "min": 0, "max": 120, "step": 30}, {"label": "Temperature (°C)", "min": 0, "max": 25, "step": 5}, [[0, 21], [30, 15], [60, 11], [90, 9], [120, 9]])
u.stop("The products end up with more energy than the reactants", "In an endothermic reaction the temperature…", "falls", ["rises", "stays the same", "doubles"])
u.stop("into black copper oxide and carbon dioxide", "Thermal decomposition is…", "endothermic", ["exothermic", "combustion", "freezing"])
u.stop("in salt ponds", "Dissolving ammonium chloride makes a pack feel…", "cold", ["hot", "heavy", "sticky"], o="O4")

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Energy changes", "sec": None, "kids": [
    {"id": "exo", "t": "Exothermic reactions", "d": "Release heat • Temperature rises • Combustion, neutralisation, respiration, rusting", "obj": "O1", "sec": "7.1"},
    {"id": "exp", "t": "Exothermic processes", "d": "Freezing • Dissolving CaCl2 • Crystallisation – hand warmers", "obj": "O2", "sec": "7.1"},
    {"id": "endo", "t": "Endothermic reactions", "d": "Take in heat • Temperature falls • Sherbet, decomposition, photosynthesis, baking", "obj": "O3", "sec": "7.2"},
    {"id": "enp", "t": "Endothermic processes", "d": "Melting • Evaporating • Dissolving NH4Cl – cold packs", "obj": "O4", "sec": "7.2"},
    {"id": "bio", "t": "Biogas", "d": "Bacteria turn waste into fuel • Cleaner cooking", "obj": "O1", "sec": "7.1"},
]}
