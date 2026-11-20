# -*- coding: utf-8 -*-
"""Stage 7 Unit 11 – Energy and Sound. Written by the Atomic teaching team."""
from c_kit import *

STRAND = "Physics"
BLURB = "Energy stores and transfers, conservation and dissipation of energy, efficiency, sound waves and echoes, and renewable energy."

OBJECTIVES = {
    "O1": {"sec": "11.1", "code": "7Pf.01", "codeNote": "energy stores", "t": "Name and give examples of energy stores, and use joules and kilojoules."},
    "O2": {"sec": "11.2", "code": "7Pf.01", "codeNote": "", "t": "Describe energy transfers (mechanical, electrical, heating, waves) and show them in flow diagrams; energy is conserved."},
    "O3": {"sec": "11.3", "code": "7Pf.02", "codeNote": "", "t": "Explain that energy dissipates to the surroundings and compare the efficiency of devices."},
    "O4": {"sec": "11.4", "code": "7Ps.01, 7Ps.02, 7SIC.05", "codeNote": "", "t": "Explain how sound travels, why it cannot pass through a vacuum, how echoes are used, and why we need renewable energy."},
}

SECTIONS = [
    {"id": "11.1", "title": "Energy stores", "objs": ["O1"]},
    {"id": "11.2", "title": "Transferring energy", "objs": ["O2"]},
    {"id": "11.3", "title": "Efficiency", "objs": ["O3"]},
    {"id": "11.4", "title": "Sound", "objs": ["O4"]},
]

S1_REQ = [
    mt("u11s1r1", "M", "O1", "Match the energy store to an example.", [("Kinetic", "a speeding truck"), ("Gravitational potential", "a book on a high shelf"), ("Chemical", "a battery"), ("Elastic potential", "a stretched trampoline spring"), ("Thermal", "a hot geyser")]),
    mc("u11s1r2", "M", "O1", "Energy is measured in…", ("joules (J)", "Correct."), [("newtons", "Force."), ("watts", "Not in this unit."), ("kilograms", "Mass.")]),
    tb("u11s1r3", "H", "O1", "Energy in foods (kJ). Complete.", ["Food", "Energy (kJ)", "Energy (J)"],
       [["Large apple", "327", B(327000)], ["Bowl of rice", "536", B(536000)]], skill="Data"),
    mc("u11s1r4", "H", "O1", "Two identical books are on shelves of different heights. Which stores more gravitational potential energy?", ("The higher one", "Correct."), [("The lower one", "No."), ("Both the same", "No."), ("Neither", "No.")]),
    ex("u11s1r5", "H", "O1", "Describe the energy stores involved when you bounce on a trampoline.",
       [("elastic potential in stretched springs", ["elastic|spring|stretch"]), ("kinetic as you move / gravitational as you rise", ["kinetic|gravitational|height"])],
       "As you land, the springs stretch and store elastic potential energy. This pushes you back up, giving you kinetic energy, then gravitational potential energy as you rise.", need=2),
    gd("u11s1r6", "M", "O1", "Which energy store?", ["Store"], [("Food", ["Chemical"]), ("Moving bicycle", ["Kinetic"]), ("Squashed spring", ["Elastic potential"]), ("Centre of an atom", ["Nuclear"])], skill="Data"),
    nm("u11s1r7", "H", "O1", "A small chocolate bar stores about 1000 kJ and a large apple 327 kJ. How many kJ more in the chocolate?", 673, "kJ", skill="Data"),
    mc("u11s1r8", "VH", "O1", "Do ice cubes have thermal energy?", ("Yes – their particles still vibrate.", "Correct."), [("No – they are cold.", "Cold things still have some."), ("Only when melting.", "No."), ("Only in sunlight.", "No.")], skill="Reasoning"),
]
S1_PRAC = [
    mc("u11s1p01", "M", "O1", "Moving objects have…", "kinetic energy", [("nuclear energy", "No."), ("elastic energy", "No."), ("chemical energy", "No.")]),
    mc("u11s1p02", "M", "O1", "The faster an object moves, the…", "more kinetic energy it has", [("less kinetic energy", "No."), ("more mass it has", "No."), ("less it weighs", "No.")]),
    mc("u11s1p03", "M", "O1", "Fuels store…", "chemical energy", [("kinetic energy", "No."), ("sound energy", "No."), ("elastic energy", "No.")]),
    mc("u11s1p04", "M", "O1", "1 kilojoule =", "1000 joules", [("100 joules", "No."), ("10 joules", "No."), ("1 000 000 joules", "No.")]),
    mc("u11s1p05", "M", "O1", "The joule is named after…", "James Prescott Joule", [("Isaac Newton", "Newton."), ("Galileo", "No."), ("Marie Curie", "No.")]),
    mc("u11s1p06", "M", "O1", "Nuclear energy is stored in…", "the nucleus of an atom", [("the electrons", "No."), ("springs", "No."), ("food", "No.")]),
    mc("u11s1p07", "H", "O1", "Thermal energy is mostly…", "the vibration of particles in an object", [("light", "No."), ("sound", "No."), ("the mass of the object", "No.")]),
    mc("u11s1p08", "M", "O1", "A stretched rubber band stores…", "elastic potential energy", [("nuclear energy", "No."), ("chemical energy", "No."), ("light energy", "No.")]),
    mc("u11s1p09", "H", "O1", "Water held behind a dam stores…", "gravitational potential energy", [("elastic energy", "No."), ("nuclear energy", "No."), ("sound energy", "No.")]),
    mc("u11s1p10", "H", "O1", "A speeding truck vs a slow bicycle: which has more kinetic energy?", "The speeding truck", [("The bicycle", "No."), ("Same", "No."), ("Neither", "No.")], skill="Reasoning"),
    nm("u11s1p11", "H", "O1", "Convert 2.5 kJ to joules.", 2500, "J"),
    nm("u11s1p12", "H", "O1", "Convert 4500 J to kilojoules.", 4.5, "kJ"),
    mc("u11s1p13", "H", "O1", "Why do people disagree about nuclear power?", "It produces lots of electricity but has risks such as radioactive waste", [("It never works", "No."), ("It uses food", "No."), ("It is a type of wind power", "No.")], skill="Reasoning"),
    gd("u11s1p14", "M", "O1", "Which energy store?", ["Store"], [("Battery", ["Chemical"]), ("Ball rolling", ["Kinetic"]), ("Hot drink", ["Thermal"])], skill="Data"),
    mc("u11s1p15", "M", "O1", "Your body gets energy from…", "the chemical store in food", [("sound", "No."), ("the nucleus of the Sun directly", "No."), ("gravity", "No.")]),
    od("u11s1p16", "M", "O1", "Order the foods from least to most energy.", ["Large apple (327 kJ)", "Bowl of rice (536 kJ)", "Small chocolate bar (1000 kJ)"], skill="Data"),
    mc("u11s1p17", "H", "O1", "A book is lifted from the floor to a high shelf. Its gravitational potential energy…", "increases", [("decreases", "No."), ("stays the same", "No."), ("disappears", "No.")]),
    mc("u11s1p18", "M", "O1", "At a hydroelectric dam, rushing water spins…", "turbines", [("magnets only", "No."), ("solar panels", "No."), ("batteries", "No.")]),
]
S1_ADV = [
    adv(ex("u11s1a1", "VH", "O1", "A 1000 kJ chocolate bar vs a 327 kJ apple: which would give more energy for a long hike, and what else should you consider?",
           [("chocolate stores more energy", ["chocolate|more"]), ("consider nutrition/health / balance", ["vitamin|fibre|health|sugar|balanc|nutri"])],
           "The chocolate stores about three times more energy, but the apple gives vitamins and fibre with less sugar, so a balanced choice matters.", need=2)),
    adv(nm("u11s1a2", "VH", "O1", "How many large apples (327 kJ each) store about the same energy as 3 chocolate bars (1000 kJ each)? Round to the nearest whole apple.", 9, "apples", tol=0.5)),
    adv(mc("u11s1a3", "VH", "O1", "A ball at the top of a hill has 40 J of gravitational potential energy. Halfway down (ignoring losses), what is true?", ("It has 20 J GPE and 20 J kinetic energy.", "Correct."), [("It has 0 J", "No."), ("40 J kinetic and 40 J GPE", "Would be 80 J."), ("It loses all energy", "No.")], skill="Reasoning")),
    adv(mc("u11s1a4", "VH", "O1", "Which object has the MOST thermal energy?", ("A swimming pool of warm water", "Correct – many particles."), [("A cup of boiling water", "Hotter but far fewer particles."), ("An ice cube", "No."), ("A spark", "Tiny.")], skill="Reasoning")),
]

S2_REQ = [
    mc("u11s2r1", "M", "O2", "Energy cannot be…", ("created or destroyed", "Correct – only transferred."), [("stored", "It can."), ("transferred", "It can."), ("measured", "It can.")]),
    gd("u11s2r2", "M", "O2", "How is the energy transferred?", ["Way"],
       [("Lifting a box", ["Mechanically"]), ("A fan plugged in", ["Electrically"]), ("A flame heating a pot", ["By heating"]), ("Sunlight reaching Earth", ["By waves"])], skill="Data"),
    od("u11s2r3", "H", "O2", "Order the stores in a rocket launch.", ["Chemical store of the fuel", "Kinetic store of the rocket", "Gravitational potential store as it climbs"]),
    ex("u11s2r4", "H", "O2", "Describe the energy transfer when you lift a box onto a shelf.",
       [("chemical store in muscles", ["chemical|muscle"]), ("gravitational potential store of box", ["gravitational|potential|height"]), ("mechanical transfer / force", ["mechanical|force"])],
       "Energy is transferred mechanically (by the force you apply) from the chemical store in your muscles to the gravitational potential store of the box.", need=2),
    tb("u11s2r5", "H", "O2", "Flow diagram data for a toy car: total energy in = 100 J. Complete.", ["Output", "Energy (J)"],
       [["Kinetic", "60"], ["Heat to surroundings", "30"], ["Sound", B(10)]], skill="Data"),
    mc("u11s2r6", "M", "O2", "Plants transfer light energy into chemical energy by…", ("photosynthesis", "Correct."), [("respiration", "Other way."), ("evaporation", "No."), ("combustion", "No.")]),
    mc("u11s2r7", "H", "O2", "Lightning is…", ("a huge electrical transfer from storm clouds", "Correct."), [("a sound wave only", "No."), ("a chemical store", "No."), ("elastic energy", "No.")]),
    mc("u11s2r8", "VH", "O2", "A bulb receives 60 J and gives out 9 J of light. How much is transferred as heat?", ("51 J – energy is conserved.", "Correct."), [("0 J", "No."), ("60 J", "No."), ("69 J", "No.")], skill="Data"),
]
S2_PRAC = [
    mc("u11s2p01", "M", "O2", "Energy can only be…", "transferred from one store to another", [("created", "No."), ("destroyed", "No."), ("used up forever", "No.")]),
    mc("u11s2p02", "M", "O2", "Thermal energy is transferred from…", "hotter to colder places", [("colder to hotter", "No."), ("only upwards", "No."), ("only in water", "No.")]),
    mc("u11s2p03", "M", "O2", "Sound and light transfer energy as…", "waves", [("a flow of charge", "Electrical."), ("a force", "Mechanical."), ("matter", "No.")]),
    mc("u11s2p04", "M", "O2", "Electrical transfer happens by…", "a flow of charge", [("heating", "No."), ("light", "No."), ("lifting", "No.")]),
    mc("u11s2p05", "H", "O2", "A fan: energy ends up in the ___ store of the blades.", "kinetic", [("chemical", "No."), ("nuclear", "No."), ("elastic", "No.")]),
    mc("u11s2p06", "H", "O2", "On a stove, energy goes flame → pot → …", "water", [("air only", "No."), ("gas", "No."), ("cooker", "No.")]),
    mc("u11s2p07", "M", "O2", "A flow diagram shows…", "energy stores and transfers", [("forces only", "No."), ("mass", "No."), ("circuits only", "No.")]),
    nm("u11s2p08", "H", "O2", "A kettle gets 2000 J; 1800 J goes into the water. How much is wasted?", 200, "J"),
    mc("u11s2p09", "H", "O2", "Burning rocket fuel also releases energy to the surroundings as…", "heat, light and sound", [("only kinetic", "No."), ("mass", "No."), ("nuclear", "No.")]),
    gd("u11s2p10", "M", "O2", "Starting store?", ["Store"], [("Battery-powered torch", ["Chemical"]), ("Wind turbine", ["Kinetic"]), ("Hydroelectric dam", ["Gravitational potential"])], skill="Data"),
    mc("u11s2p11", "H", "O2", "Power stations burn fuels to…", "generate electricity", [("make food", "No."), ("store sound", "No."), ("create energy", "Transfer, not create.")]),
    mc("u11s2p12", "H", "O2", "A ball thrown upwards slows down because…", "kinetic energy is transferred to gravitational potential energy", [("energy is destroyed", "No."), ("gravity vanishes", "No."), ("it gains mass", "No.")], skill="Reasoning"),
    mc("u11s2p13", "M", "O2", "Energy from the Sun reaches Earth as…", "light", [("electricity", "No."), ("sound", "No."), ("wind only", "No.")]),
    mc("u11s2p14", "H", "O2", "Total energy in = 500 J. Useful out = 350 J. Wasted =", "150 J", [("850 J", "No."), ("350 J", "No."), ("0 J", "No.")], skill="Data"),
    ms("u11s2p15", "H", "O2", "Select ALL ways of transferring energy.", ["Mechanically", "Electrically", "By heating", "By waves"], [("By creating it", "No."), ("By destroying it", "No.")]),
    mc("u11s2p16", "M", "O2", "Your muscles get energy from the ___ store.", "chemical", [("nuclear", "No."), ("elastic", "No."), ("sound", "No.")]),
    od("u11s2p17", "M", "O2", "Order the energy path for food energy reaching a plant-eating animal.", ["Light from the Sun", "Chemical store in the plant (photosynthesis)", "Chemical store in the animal that eats it"]),
    mc("u11s2p18", "H", "O2", "Why does a swing eventually stop if nobody pushes?", "Energy is gradually transferred to the surroundings", [("Energy is destroyed", "No."), ("Gravity stops", "No."), ("It runs out of mass", "No.")], skill="Reasoning"),
]
S2_ADV = [
    adv(ex("u11s2a1", "VH", "O2", "Draw (describe) a flow diagram for a battery-powered torch.",
           [("chemical store in battery", ["chemical|battery"]), ("electrical transfer", ["electric"]), ("light (useful) and heat (wasted)", ["light|heat|thermal"])],
           "Chemical store (battery) → transferred electrically → light (useful) + heat to the surroundings (wasted).", need=2)),
    adv(nm("u11s2a2", "VH", "O2", "A rocket's fuel releases 8000 kJ. 3000 kJ goes to kinetic, 2500 kJ to gravitational potential; the rest to surroundings. How much to surroundings?", 2500, "kJ")),
    adv(mc("u11s2a3", "VH", "O2", "A bouncing ball rises less high each time. Where has the energy gone?", ("To the surroundings as heat and sound", "Correct."), [("Destroyed", "No."), ("Into the ball's mass", "No."), ("Into nuclear energy", "No.")], skill="Reasoning")),
    adv(mc("u11s2a4", "VH", "O2", "Why do we say we 'use up' fuel but not energy?", ("Fuel's chemical store empties, but the energy is transferred, not destroyed.", "Correct."), [("Energy is destroyed", "No."), ("Fuel is created", "No."), ("They mean the same", "No.")], skill="Reasoning")),
]

S3_REQ = [
    tb("u11s3r1", "H", "O3", "Percentage of energy turned into light. Complete the wasted column.", ["Lamp", "Light (%)", "Wasted as heat (%)"],
       [["Tungsten", "15", B(85)], ["Fluorescent", "80", B(20)], ["LED", "90", B(10)]], skill="Data"),
    mc("u11s3r2", "M", "O3", "The most efficient lamp is the…", ("LED", "Correct – 90% light."), [("tungsten bulb", "15%."), ("fluorescent lamp", "80%."), ("candle", "No.")]),
    mc("u11s3r3", "M", "O3", "Wasted energy usually goes to the surroundings as…", ("heat or sound", "Correct."), [("mass", "No."), ("light only", "No."), ("chemical energy", "No.")]),
    ex("u11s3r4", "H", "O3", "Explain what 'dissipates' means for energy.",
       [("spreads out to surroundings", ["spread|surround"]), ("less useful", ["less useful|useless|can't be used|wasted"])],
       "Dissipated energy spreads out into the surroundings, usually as heat, and becomes less useful.", need=2),
    mc("u11s3r5", "M", "O3", "Efficiency tells us…", ("how much input energy is transferred usefully", "Correct."), [("how much energy is created", "No."), ("how heavy a device is", "No."), ("how fast it is", "No.")]),
    gd("u11s3r6", "H", "O3", "Useful or wasted energy?", ["Type"], [("Light from a lamp", ["Useful"]), ("Heat from a lamp", ["Wasted"]), ("Sound from a car engine", ["Wasted"]), ("Kinetic energy of a fan", ["Useful"])], skill="Data"),
    nm("u11s3r7", "H", "O3", "A lamp is given 200 J. It is 90% efficient. How much light energy?", 180, "J", skill="Data"),
    mc("u11s3r8", "VH", "O3", "Why does switching to LED lamps save money?", ("They waste less energy, so need less electricity for the same light.", "Correct."), [("They are brighter only", "Not the reason."), ("They make heat", "Less."), ("They use more electricity", "No.")], skill="Reasoning"),
]
S3_PRAC = [
    mc("u11s3p01", "M", "O3", "A tungsten bulb turns ___ of its energy into light.", "15%", [("90%", "LED."), ("80%", "Fluorescent."), ("50%", "No.")]),
    mc("u11s3p02", "M", "O3", "Holding your hand near a lamp feels warm because…", "some energy is wasted as heat", [("light is cold", "No."), ("lamps make sound", "No."), ("energy is created", "No.")]),
    mc("u11s3p03", "M", "O3", "Most energy transfers…", "waste some energy", [("waste none", "No."), ("create energy", "No."), ("destroy energy", "No.")]),
    mc("u11s3p04", "H", "O3", "Which wastes the least electricity?", "LED", [("Tungsten bulb", "Most waste."), ("Fluorescent", "More waste."), ("All the same", "No.")]),
    nm("u11s3p05", "H", "O3", "A motor gets 400 J and gives 300 J of kinetic energy. Wasted energy?", 100, "J"),
    nm("u11s3p06", "H", "O3", "A motor gets 400 J and gives 300 J useful. Efficiency (%)?", 75, "%"),
    mc("u11s3p07", "M", "O3", "Oiling a squeaky bicycle chain makes it more efficient because…", "less energy is wasted as heat and sound", [("it creates energy", "No."), ("it adds mass", "No."), ("it changes colour", "No.")], skill="Reasoning"),
    mc("u11s3p08", "H", "O3", "Dissipated energy is…", "spread out and less useful", [("destroyed", "No."), ("stored in the device", "No."), ("more useful", "No.")]),
    gd("u11s3p09", "M", "O3", "Efficiency of lamp", ["Light (%)"], [("Tungsten", ["15"]), ("Fluorescent", ["80"]), ("LED", ["90"])], skill="Data"),
    mc("u11s3p10", "H", "O3", "A device can never be more than 100% efficient because…", "energy cannot be created", [("it would be too bright", "No."), ("100 is the biggest number", "No."), ("devices are small", "No.")], skill="Reasoning"),
    mc("u11s3p11", "M", "O3", "Wasted energy in a car engine is mostly…", "heat", [("light", "No."), ("chemical", "No."), ("nuclear", "No.")]),
    nm("u11s3p12", "H", "O3", "A fluorescent lamp (80%) gets 50 J. How much becomes light?", 40, "J"),
    mc("u11s3p13", "H", "O3", "Which change makes a kettle more efficient?", "Insulating its walls", [("Painting it black inside", "No."), ("Leaving the lid off", "Wastes more."), ("Using cold water", "No.")], skill="Reasoning"),
    od("u11s3p14", "M", "O3", "Order the lamps from least to most efficient.", ["Tungsten (15%)", "Fluorescent (80%)", "LED (90%)"], skill="Data"),
    mc("u11s3p15", "M", "O3", "Useful energy from a TV is…", "light and sound", [("heat", "Wasted."), ("vibration of the case", "Wasted."), ("mass", "No.")]),
    mc("u11s3p16", "H", "O3", "Energy wasted as heat warms…", "the surroundings", [("the device's mass", "No."), ("nothing", "No."), ("the Sun", "No.")]),
    mc("u11s3p17", "H", "O3", "Why is a tungsten bulb sometimes used as a small heater?", "85% of its energy becomes heat", [("It is cold", "No."), ("It makes no light", "No."), ("It is efficient at light", "No.")], skill="Reasoning"),
    mc("u11s3p18", "M", "O3", "A more efficient device…", "wastes less energy", [("wastes more energy", "No."), ("creates energy", "No."), ("is always bigger", "No.")]),
]
S3_ADV = [
    adv(ex("u11s3a1", "VH", "O3", "A school replaces 200 tungsten bulbs with LEDs. Give TWO benefits.",
           [("less electricity / lower bills", ["electric|bill|cost|money|cheap"]), ("less wasted heat / fewer fossil fuels burned", ["heat|fossil|carbon|environment|pollut"])],
           "LEDs need far less electricity for the same light, so bills fall. Less electricity means fewer fossil fuels burned at power stations, helping the environment.", need=2)),
    adv(nm("u11s3a2", "VH", "O3", "For 1000 J of light, how much energy must a tungsten bulb (15%) be given? Round to the nearest whole joule.", 6667, "J", tol=1)),
    adv(mc("u11s3a3", "VH", "O3", "A machine is 60% efficient. 240 J is wasted. Total energy input?", ("600 J", "Correct – 40% wasted = 240 J."), [("400 J", "No."), ("240 J", "No."), ("144 J", "No.")], skill="Data")),
    adv(mc("u11s3a4", "VH", "O3", "Why is 'wasted' energy not really lost?", ("It still exists, spread out in the surroundings, but is hard to use.", "Correct."), [("It is destroyed", "No."), ("It becomes mass", "No."), ("It returns to the plug", "No.")], skill="Reasoning")),
]

S4_REQ = [
    mc("u11s4r1", "M", "O4", "Sound is made when objects…", ("vibrate", "Correct."), [("melt", "No."), ("glow", "No."), ("rust", "No.")]),
    ex("u11s4r2", "H", "O4", "Explain why sound cannot travel through a vacuum.",
       [("sound needs particles", ["particle|matter|medium"]), ("vacuum has no particles to pass vibrations", ["no particles|empty|nothing|vibrat"])],
       "Sound travels by particles vibrating and passing the vibrations on. A vacuum has no particles, so the vibrations cannot be passed along.", need=2),
    gd("u11s4r3", "M", "O4", "Where is sound fastest?", ["Speed"], [("Steel (solid)", ["Fastest"]), ("Water (liquid)", ["Middle"]), ("Air (gas)", ["Slowest"])], skill="Data"),
    mc("u11s4r4", "M", "O4", "An echo is…", ("sound reflected from a hard surface", "Correct."), [("sound absorbed by a cushion", "No."), ("a light wave", "No."), ("a vibrating string", "No.")]),
    tb("u11s4r5", "H", "O4", "Hearing ranges (kHz). Complete.", ["Animal", "Top of range (kHz)"],
       [["Human", "20"], ["Bat", "90"], ["Bat minus human", B(70)]], skill="Data"),
    mt("u11s4r6", "M", "O4", "Match the use of echoes.", [("Bats", "finding prey"), ("Sonar", "mapping the seabed"), ("Ultrasound", "pictures inside the body")]),
    nm("u11s4r7", "H", "O4", "Sonar: sound travels 1500 m/s in water. An echo returns after 2 s. How deep is the seabed?", 1500, "m", skill="Data"),
    mc("u11s4r8", "VH", "O4", "Why do recording studios line walls with soft materials?", ("Soft materials absorb sound, reducing echoes.", "Correct."), [("To reflect more sound", "No."), ("For decoration only", "No."), ("To make it warmer", "No.")], skill="Reasoning"),
]
S4_PRAC = [
    mc("u11s4p01", "M", "O4", "Sound travels as…", "a wave of vibrating particles", [("a flow of electrons", "No."), ("light", "No."), ("a solid object", "No.")]),
    mc("u11s4p02", "M", "O4", "Space is silent because…", "it is a vacuum with no particles", [("it is too cold", "No."), ("it is dark", "No."), ("there is no gravity", "No.")]),
    mc("u11s4p03", "M", "O4", "Sound travels fastest in…", "solids", [("gases", "Slowest."), ("liquids", "Middle."), ("a vacuum", "Can't.")]),
    mc("u11s4p04", "M", "O4", "A louder sound transfers…", "more energy", [("less energy", "No."), ("no energy", "No."), ("only light", "No.")]),
    mc("u11s4p05", "M", "O4", "Humans can hear up to about…", "20 kHz", [("90 kHz", "Bats."), ("2 kHz", "No."), ("200 kHz", "No.")]),
    mc("u11s4p06", "H", "O4", "Ultrasound is sound that is…", "too high for humans to hear", [("too quiet", "No."), ("light", "No."), ("too low", "No.")]),
    mc("u11s4p07", "M", "O4", "Echolocation is used by…", "bats, dolphins and whales", [("cats only", "No."), ("plants", "No."), ("fish only", "No.")]),
    mc("u11s4p08", "H", "O4", "Some moths escape bats because their wing scales…", "absorb the bat's calls", [("reflect light", "No."), ("make sound", "No."), ("are magnetic", "No.")]),
    mc("u11s4p09", "M", "O4", "Which is a renewable energy resource?", "Wind", [("Coal", "Fossil fuel."), ("Oil", "Fossil fuel."), ("Natural gas", "Fossil fuel.")]),
    mc("u11s4p10", "M", "O4", "Solar panels transfer the energy of sunlight into…", "electricity", [("sound", "No."), ("coal", "No."), ("wind", "No.")]),
    mc("u11s4p11", "H", "O4", "Hydropower uses the ___ energy of water behind a dam.", "gravitational potential", [("nuclear", "No."), ("chemical", "No."), ("elastic", "No.")]),
    mc("u11s4p12", "H", "O4", "About what share of world electricity came from renewables (as stated in the lesson)?", "About 30%", [("About 3%", "No."), ("About 90%", "No."), ("100%", "No.")]),
    gd("u11s4p13", "M", "O4", "Renewable or non-renewable?", ["Type"], [("Solar", ["Renewable"]), ("Coal", ["Non-renewable"]), ("Tidal", ["Renewable"]), ("Geothermal", ["Renewable"])], skill="Data"),
    mc("u11s4p14", "H", "O4", "Why do we need more renewable energy?", "Burning fossil fuels harms the planet and they will run out", [("Renewables are always cheaper", "Not always."), ("Fossil fuels are renewable", "No."), ("No reason", "No.")], skill="Reasoning"),
    nm("u11s4p15", "H", "O4", "You shout at a cliff 170 m away. Sound travels 340 m/s in air. How long until the echo returns?", 1, "s"),
    mc("u11s4p16", "M", "O4", "A violin makes sound because its…", "strings vibrate", [("wood glows", "No."), ("bow is hot", "No."), ("case is hollow only", "No.")]),
    od("u11s4p17", "M", "O4", "Order how sound reaches your ear.", ["A string vibrates", "Nearby air particles vibrate", "They pass the vibration to neighbours", "Your eardrum vibrates"]),
    mc("u11s4p18", "H", "O4", "Countries agreed to ___ renewable energy capacity by 2030.", "triple", [("halve", "No."), ("stop", "No."), ("keep the same", "No.")]),
]
S4_ADV = [
    adv(ex("u11s4a1", "VH", "O4", "Explain how a ship uses sonar to find the depth of the sea.",
           [("sends sound pulse down", ["send|pulse|sound"]), ("echo reflects from seabed", ["echo|reflect|bounce"]), ("time × speed ÷ 2", ["time|speed|half|÷ ?2|divide"])],
           "The ship sends a pulse of sound down; it reflects off the seabed as an echo. The time for the echo to return is measured: depth = speed × time ÷ 2.", need=2)),
    adv(nm("u11s4a2", "VH", "O4", "A bat hears an echo 0.02 s after calling. Sound travels 340 m/s. How far away is the moth?", 3.4, "m", tol=0.01)),
    adv(mc("u11s4a3", "VH", "O4", "Why can astronauts on a spacewalk still talk by radio but not by shouting?", ("Radio waves can cross a vacuum; sound cannot.", "Correct."), [("Radio is louder", "No."), ("Helmets block sound only", "Not the reason."), ("Space has air", "No.")], skill="Reasoning")),
    adv(mc("u11s4a4", "VH", "O4", "A disadvantage of solar power is…", ("it produces less when it is cloudy or dark", "Correct."), [("it runs out", "No."), ("it burns coal", "No."), ("it releases acid rain gases", "No.")], skill="Reasoning")),
]

POOLS = {"11.1": (S1_REQ, S1_PRAC, S1_ADV), "11.2": (S2_REQ, S2_PRAC, S2_ADV), "11.3": (S3_REQ, S3_PRAC, S3_ADV), "11.4": (S4_REQ, S4_PRAC, S4_ADV)}

STOPS = {
    "11.1": [stop("u11v1a", "including you!", mc("u11v1a_q", "M", "O1", "A book on a high shelf stores…", "gravitational potential energy", [("kinetic energy", "Not moving."), ("elastic energy", "No."), ("sound energy", "No.")])),
             stop("u11v1b", "which then bounces you back up", mc("u11v1b_q", "M", "O1", "How many joules are in 1 kilojoule?", "1000 J", [("100 J", "No."), ("10 J", "No."), ("1 J", "No.")])),
             stop("u11v1c", "even ice cubes all have thermal energy", mc("u11v1c_q", "H", "O1", "Nuclear energy is stored in…", "the nucleus of an atom", [("food", "Chemical."), ("springs", "Elastic."), ("moving cars", "Kinetic.")]))],
    "11.2": [stop("u11v2a", "to cook food", mc("u11v2a_q", "M", "O2", "Lifting a box transfers energy…", "mechanically", [("electrically", "No."), ("by sound", "No."), ("by light", "No.")])),
             stop("u11v2b", "A flow diagram shows all these stores and transfers clearly", mc("u11v2b_q", "H", "O2", "In a rocket launch, energy starts in the…", "chemical store of the fuel", [("kinetic store", "Later."), ("nuclear store", "No."), ("elastic store", "No.")]))],
    "11.3": [stop("u11v3a", "it wastes the least electricity", mc("u11v3a_q", "M", "O3", "What percentage of a tungsten bulb's energy becomes heat?", "85%", [("15%", "That's light."), ("10%", "No."), ("50%", "No.")]))],
    "11.4": [stop("u11v4a", "Space is silent!", mc("u11v4a_q", "M", "O4", "Sound travels fastest through…", "solids", [("gases", "Slowest."), ("a vacuum", "Can't."), ("liquids", "Middle.")])),
             stop("u11v4b", "to build pictures of the inside of the body", mc("u11v4b_q", "M", "O4", "An echo is…", "reflected sound", [("absorbed sound", "No."), ("light", "No."), ("a vibration in a vacuum", "No.")])),
             stop("u11v4c", "biofuels are renewable too", mc("u11v4c_q", "H", "O4", "Which is renewable?", "Wind", [("Coal", "No."), ("Oil", "No."), ("Natural gas", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Energy and sound", "sec": None, "kids": [
    {"id": "st", "t": "Energy stores", "d": "Kinetic • gravitational potential • chemical • elastic • nuclear • thermal • joules and kilojoules.", "obj": "O1", "sec": "11.1"},
    {"id": "tr", "t": "Transfers", "d": "Mechanically, electrically, by heating, by waves • energy conserved • flow diagrams.", "obj": "O2", "sec": "11.2"},
    {"id": "ef", "t": "Efficiency", "d": "Useful vs wasted • dissipation as heat/sound • tungsten 15%, fluorescent 80%, LED 90% light.", "obj": "O3", "sec": "11.3"},
    {"id": "so", "t": "Sound and renewables", "d": "Vibrations through particles • none in a vacuum • echoes: echolocation, sonar, ultrasound • solar, wind, hydro, tidal, geothermal.", "obj": "O4", "sec": "11.4"},
]}
