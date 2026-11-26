# -*- coding: utf-8 -*-
"""Stage 9 Unit 10 – Transfer of Thermal Energy. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Physics"
BLURB = "The difference between heat and temperature, conservation of energy and efficiency, heat dissipation, conduction, convection and radiation, and cooling by evaporation."
OBJECTIVES = {
    "O1": {"sec": "10.1", "code": "9Pf.02", "codeNote": "", "t": "Distinguish between heat (thermal energy transferred) and temperature (average kinetic energy of particles)."},
    "O2": {"sec": "10.2", "code": "9Pf.03", "codeNote": "", "t": "Use the law of conservation of energy, energy diagrams and efficiency."},
    "O3": {"sec": "10.3", "code": "9Pf.04", "codeNote": "", "t": "Describe heat dissipation from hotter to cooler regions and how insulation slows it."},
    "O4": {"sec": "10.4", "code": "9Pf.05", "codeNote": "", "t": "Explain conduction, convection and radiation using the particle model and waves."},
    "O5": {"sec": "10.5", "code": "9Pf.06", "codeNote": "", "t": "Explain cooling by evaporation and the factors that affect the rate of evaporation."},
}
SECTIONS = [
    {"id": "10.1", "title": "Heat and temperature", "objs": ["O1"]},
    {"id": "10.2", "title": "Energy conservation", "objs": ["O2"]},
    {"id": "10.3", "title": "Heat dissipation", "objs": ["O3"]},
    {"id": "10.4", "title": "How is thermal energy transferred?", "objs": ["O4"]},
    {"id": "10.5", "title": "Cooling by evaporation", "objs": ["O5"]},
]
u = Unit(9, 10)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 10.1
u.sec("10.1", "O1")
u.gd("r", "Heat or temperature?", "Quantity", [("Measured in joules", "Heat"), ("Measured in degrees Celsius", "Temperature"), ("Energy flowing from hot to cold", "Heat"), ("Average kinetic energy of particles", "Temperature")])
u.gd("r", "A bathtub and a cup of water are both at 20 °C. Which has more…", "Answer", [("Thermal energy", "Bathtub"), ("Temperature", "Same")], extra=["Cup"])
u.tb("r", "Equal masses of water are mixed and no energy is lost. Complete the final temperature.", ["Hot water (°C)", "Cold water (°C)", "Final temperature (°C)"], [["80", "20", B(50)], ["60", "40", B(50)]])
u.ex("r", "Explain the difference between heat and temperature.", [("heat = thermal energy transferred from hot to cold", ["heat.*(energy|transfer|flow)"]), ("temperature = how hot / average kinetic energy", ["temperature.*(average|how hot|kinetic)"]), ("units joules vs °C", ["joule|°c|celsius"])],
     "Heat is thermal energy transferred from a hotter to a cooler object, measured in joules. Temperature is how hot something is, the average kinetic energy of its particles, measured in °C.")
u.mc("r", "Thermal energy is…", "the total kinetic and potential energy of all the particles", ["the temperature of one particle", "light energy", "the mass of an object"])
u.mc("r", "Heat flows…", "from hotter to cooler objects", ["from cooler to hotter objects", "only upwards", "only in metals"])
u.mc("r", "Count Rumford's cannon-drilling observation showed that…", "heat is a form of energy", ["heat is a substance", "cannons are cold", "metal creates matter"], d="H")
u.mc("r", "When a kettle heats water, the temperature rises because…", "the particles move faster", ["the particles get bigger", "particles are added", "the water loses energy"], d="VH")
mcs("p", [
    ("Our planet's main source of thermal energy is…", "the Sun", ["the Moon", "volcanoes", "the oceans"]),
    ("Heat is measured in…", "joules", ["degrees Celsius", "newtons", "metres"]),
    ("Temperature is measured with a…", "thermometer", ["balance", "ruler", "voltmeter"]),
    ("Temperature is measured in…", "degrees Celsius", ["joules", "kilograms", "watts"]),
    ("Heat stops flowing when…", "both objects reach the same temperature", ["one object melts", "the hotter one is colder", "after one minute always"]),
    ("A bathtub at 20 °C holds more thermal energy than a cup at 20 °C because it has…", "more particles", ["faster particles", "a higher temperature", "less water"]),
    ("Thermal energy is the energy of…", "moving, vibrating particles", ["light waves only", "sound only", "magnets"]),
    ("Heating particles makes them…", "move faster", ["stop", "shrink", "disappear"]),
    ("Temperature is the … kinetic energy of the particles.", "average", ["total", "maximum", "minimum"]),
    ("Water boils at…", "100 °C", ["0 °C", "50 °C", "212 °C"]),
    ("Count Rumford studied heat in the…", "1790s", ["1950s", "1500s", "2000s"]),
    ("A hot drink left in a room…", "cools to room temperature", ["heats up", "stays hot forever", "freezes"]),
    ("Thermal energy depends on temperature and the … of particles.", "number", ["colour", "shape", "name"]),
    ("Ice in your hand melts because heat flows…", "from your hand to the ice", ["from the ice to your hand", "nowhere", "from the air to your hand"]),
    ("Two objects at the same temperature…", "have no heat flow between them", ["always swap heat", "must have the same mass", "must be made of the same material"]),
])
u.mt("p", "Match the term to its meaning.", [("Heat", "thermal energy transferred"), ("Temperature", "how hot something is"), ("Thermal energy", "total energy of particles")])
u.od("p", "Order what happens when a kettle heats water.", ["Electric element heats up", "Heat flows into the water", "Particles move faster", "Temperature rises", "Water boils"])
u.ms("p", "Select ALL the true statements.", ["Heat is measured in joules", "Heat flows from hot to cold", "A larger object can hold more thermal energy at the same temperature"], ["Temperature is measured in joules", "Heat flows from cold to hot"])
u.ex("a", "A sparkler is at 1000 °C but a spark landing on your hand rarely burns you. A pan of water at 100 °C would. Explain.", [("spark has very high temperature", ["temperature|1000|hot"]), ("but very few particles / tiny mass – little thermal energy", ["few|small|tiny|little"]), ("pan of water has much more thermal energy to transfer", ["more thermal energy|more energy|lots of"])],
     "The spark has a very high temperature but is tiny, so it contains very little thermal energy. The pan of water has a lower temperature but far more particles, so it holds and transfers much more thermal energy.")
u.mc("a", "1 kg of water at 50 °C and 2 kg of water at 50 °C. Which statement is correct?", "The 2 kg has twice the thermal energy but the same temperature", ["They have the same thermal energy", "The 2 kg is hotter", "The 1 kg has more thermal energy"], skill="Reasoning")
u.mc("a", "Why did drilling cannons seem to produce 'endless' heat?", "Work done by drilling was continuously transferred into thermal energy", ["The metal contained a hidden fluid", "The cannons were already hot", "Drilling creates new atoms"], skill="Reasoning")
u.mc("a", "Equal masses of water at 20 °C and 60 °C are mixed. The final temperature is about…", "40 °C", ["80 °C", "20 °C", "60 °C"], skill="Application")
u.stop("how many gadgets work", "Our main source of thermal energy is…", "the Sun", ["the Moon", "the ocean", "the wind"])
u.stop("it has far more particles", "Which has more thermal energy at room temperature?", "A bathtub of water", ["A cup of water", "They are equal", "Neither has any"])
u.stop("showing that heat is a form of energy", "Heat flows from…", "hotter to cooler objects", ["cooler to hotter objects", "small to large objects", "nowhere"])

# ---------------------------------------------------------------- 10.2
u.sec("10.2", "O2")
u.tb("r", "Energy for every 100 J supplied. Complete the table.", ["Lamp", "Light (J)", "Heat (J)", "Efficiency (%)"], [["Incandescent", "10", B(90), B(10)], ["LED", "75", B(25), B(75)]])
u.gd("r", "Useful or wasted energy?", "Type", [("Light from a lamp", "Useful"), ("Heat from a lamp", "Wasted"), ("Sound from a car engine", "Wasted"), ("Kinetic energy of a fan's blades", "Useful")])
u.gd("r", "Pendulum: which energy store is largest?", "Largest store", [("At the highest point", "Potential"), ("At the lowest point", "Kinetic")])
u.ex("r", "State the law of conservation of energy and use it to explain where the 'lost' energy from a lamp goes.", [("energy cannot be created or destroyed", ["created|destroyed"]), ("only transferred between stores", ["transfer"]), ("wasted mostly as heat to surroundings", ["heat|surround|wasted"])],
     "Energy cannot be created or destroyed, only transferred between stores, so the total stays the same. The 'lost' energy from a lamp is transferred to the surroundings, mostly as heat.")
u.mc("r", "Efficiency measures…", "how much of the input energy becomes useful output", ["how bright a lamp is", "how much energy is created", "the total energy supplied"])
u.mc("r", "Which lamp is more efficient?", "LED", ["Incandescent", "They are equal", "Neither"])
u.mc("r", "A motor is supplied with 200 J and gives 150 J of useful kinetic energy. How much is wasted?", "50 J", ["350 J", "150 J", "0 J"], d="H")
u.mc("r", "Why do efficient devices help the environment?", "They waste less energy, so less fuel is burned to generate electricity", ["They create energy", "They destroy wasted energy", "They need no energy"], d="VH")
mcs("p", [
    ("Energy can be … from one store to another.", "transferred", ["created", "destroyed", "lost from the Universe"]),
    ("A swinging pendulum swaps … and kinetic energy.", "potential", ["sound", "nuclear", "light"]),
    ("Total energy in a closed system…", "stays the same", ["increases", "decreases", "disappears"]),
    ("Energy diagrams show…", "where the energy goes", ["the colour of the device", "the mass", "the speed of light"]),
    ("An incandescent lamp wastes most energy as…", "heat", ["light", "sound", "kinetic energy"]),
    ("Efficiency is usually given as a…", "percentage", ["mass", "temperature", "length"]),
    ("Efficiency = useful output ÷ … × 100%", "total input", ["wasted energy", "time", "mass"]),
    ("A device that is 100% efficient would waste…", "no energy", ["all its energy", "half its energy", "only light"]),
    ("Real devices are never 100% efficient because some energy is…", "wasted, usually as heat", ["destroyed", "created", "stored in the plug"]),
    ("LED lamps give 75 J of light for every … J supplied.", "100", ["75", "25", "1000"]),
    ("The wasted energy from devices spreads into the…", "surroundings", ["battery", "plug", "wire only"]),
    ("Energy is measured in…", "joules", ["watts", "volts", "newtons"]),
    ("A car engine transfers chemical energy into kinetic energy and…", "heat and sound", ["more chemical energy", "mass", "light only"]),
    ("A pendulum eventually stops because energy is transferred to…", "heat in the air and pivot", ["nothing", "more kinetic energy", "the Moon"]),
    ("Switching to LEDs saves money because they…", "waste less energy", ["create light energy", "use no electricity", "are heavier"]),
])
u.mt("p", "Match the device to its main useful output.", [("Lamp", "light"), ("Speaker", "sound"), ("Electric heater", "heat")])
u.od("p", "Order the lamps from least to most efficient.", ["Incandescent (10%)", "Halogen (15%)", "Compact fluorescent (25%)", "LED (75%)"])
u.nm("p", "A kettle uses 2000 J and transfers 1800 J to the water. What is its efficiency?", 90, "%")
u.ex("a", "An electric motor is 60% efficient. It is supplied with 500 J. Calculate the useful and wasted energy and suggest where the waste goes.", [("useful = 300 J", ["300"]), ("wasted = 200 J", ["200"]), ("heat / sound from friction", ["heat|sound|friction"])],
     "Useful energy = 60% of 500 J = 300 J, so 200 J is wasted, mostly as heat and sound caused by friction in the motor.")
u.nm("a", "A lamp is 25% efficient and gives 50 J of light. How much energy was supplied?", 200, "J")
u.mc("a", "Why does a bouncing ball bounce lower each time?", "Some energy is transferred to heat and sound at each bounce", ["Energy is destroyed", "Gravity gets stronger", "The ball gains mass"], skill="Reasoning")
u.mc("a", "A claim says a machine gives out 120 J for every 100 J put in. Why must it be wrong?", "Energy cannot be created", ["Machines always lose mass", "120 J is too small", "It is allowed if the machine is new"], skill="Reasoning")
u.stop("so the total stays the same", "Energy can be…", "transferred but not created or destroyed", ["created", "destroyed", "used up completely"])
u.stop("only 25 of heat", "Which lamp wastes more energy as heat?", "Incandescent", ["LED", "They are equal", "Neither"])
u.stop("which helps protect the environment", "Efficiency measures how much input energy becomes…", "useful output", ["wasted heat", "mass", "new energy"])

# ---------------------------------------------------------------- 10.3
u.sec("10.3", "O3")
u.gd("r", "Open or closed system?", "System", [("Pan of soup without a lid (steam escapes)", "Open"), ("Sealed can of drink (only heat passes)", "Closed")], extra=["Isolated"])
u.tb("r", "A pie cools in a room at 20 °C. Complete the temperature drop.", ["Time (min)", "Temperature (°C)", "Drop since start (°C)"], [["0", "90", "0"], ["10", "65", B(25)], ["20", "48", B(42)]])
u.gr("r", "Cooling of the pie. Plot the points.", {"label": "Time (min)", "min": 0, "max": 40, "step": 10}, {"label": "Temperature (°C)", "min": 0, "max": 100, "step": 20}, [[0, 90], [10, 65], [20, 48], [30, 37], [40, 30]])
u.ex("r", "Explain how an ice pack helps an injury.", [("ice pack is cooler than skin", ["cool|cold|lower temperature"]), ("heat flows from skin to ice pack", ["heat.*(flow|transfer)|absorb"]), ("skin cools / reduces swelling", ["cool|swelling|pain"])],
     "The ice pack is colder than the skin, so heat flows from the injured skin into the ice pack. This cools the area, reducing swelling and pain.")
u.mc("r", "Heat dissipation is…", "thermal energy spreading from a hotter region to a cooler one", ["heat being created", "cold flowing into objects", "energy being destroyed"])
u.mc("r", "A vacuum flask keeps drinks hot because it…", "slows the flow of heat", ["creates heat", "stops time", "makes the drink denser"])
u.mc("r", "Why does the pie cool quickly at first and then more slowly?", "The temperature difference with the room gets smaller", ["The pie gets more thermal energy", "The room gets colder", "Heat flows into the pie"], d="H")
u.mc("r", "Why do elephants' huge, thin ears help them keep cool?", "Their large surface area lets heat dissipate from the blood quickly", ["They store water", "They block the Sun's heat completely", "They make sound to cool the air"], d="VH")
mcs("p", [
    ("A freshly baked pie cools because heat flows into the…", "cooler air", ["oven", "pie dish only", "hotter air"]),
    ("An open system exchanges…", "energy and matter", ["only energy", "nothing", "only matter"]),
    ("A closed system exchanges…", "only energy", ["energy and matter", "nothing", "only matter"]),
    ("Insulation…", "slows the flow of heat", ["speeds up heat flow", "creates heat", "destroys heat"]),
    ("A vacuum flask can keep drinks…", "hot or cold", ["only hot", "only cold", "neither"]),
    ("Phones and laptops are designed to … heat.", "dissipate", ["store", "create", "trap"]),
    ("Overheating can … electronic devices.", "damage", ["improve", "charge", "cool"]),
    ("A large surface area makes heat dissipate…", "faster", ["slower", "not at all", "only at night"]),
    ("A cool drink on a hot day warms up because heat flows…", "from the air into the drink", ["from the drink into the air", "nowhere", "from the ice into the air"]),
    ("Heat sinks on computer chips have many fins to…", "increase surface area", ["add weight", "store heat forever", "make noise"]),
    ("When the pie reaches room temperature, heat flow…", "stops", ["speeds up", "reverses", "doubles"]),
    ("Wearing layers of clothes in winter helps by…", "trapping air that insulates", ["creating heat", "letting cold in", "removing body heat faster"]),
    ("Which material is a good insulator?", "Wool", ["Copper", "Iron", "Aluminium"]),
    ("A lid on a pan makes it more like a … system.", "closed", ["open", "isolated forever", "empty"]),
    ("Heat always dissipates from … regions.", "hotter to cooler", ["cooler to hotter", "small to large", "dark to light"]),
])
u.mt("p", "Match the example to how it controls heat flow.", [("Vacuum flask", "slows heat flow"), ("Elephant ears", "large surface area dissipates heat"), ("Laptop fan", "removes heat to prevent overheating")])
u.od("p", "Order the cups from fastest to slowest cooling.", ["Thin metal cup, no lid", "Plastic cup, no lid", "Plastic cup with lid", "Vacuum flask"])
u.ms("p", "Select ALL the ways to slow heat loss from a drink.", ["Put a lid on it", "Use an insulated cup", "Use a vacuum flask"], ["Pour it into a wide, shallow dish", "Blow on it"])
u.ex("a", "Explain how the design of a vacuum flask reduces heat transfer.", [("vacuum stops conduction and convection", ["vacuum.*(conduct|convect)|no particles"]), ("silvered walls reflect radiation", ["silver|shiny|reflect|radiation"]), ("stopper reduces convection / evaporation", ["stopper|lid|cap"])],
     "The vacuum between the walls has no particles, so it stops conduction and convection. The silvered surfaces reflect radiation, and the stopper stops warm air and vapour escaping.")
u.mc("a", "Using the cooling graph, about what temperature would the pie reach after a very long time?", "20 °C, room temperature", ["0 °C", "90 °C", "−20 °C"], skill="Data")
u.mc("a", "Why does a large, thin copper fin cool a computer chip better than a small cube of copper?", "It has a larger surface area for heat to dissipate", ["It has more mass", "It is a different metal", "It traps more heat"], skill="Reasoning")
u.mc("a", "Arctic foxes have small ears compared with desert foxes. Why?", "Small ears reduce surface area, so less heat is lost", ["Small ears dissipate more heat", "Cold air shrinks ears", "Ears produce heat"], skill="Reasoning")
u.stop("absorbs heat from the skin", "A pie cools because heat flows into the…", "cooler air", ["hotter oven", "pie itself", "nothing"])
u.stop("keeping drinks hot or cold for longer", "A closed system exchanges…", "only energy", ["energy and matter", "only matter", "nothing"])
u.stop("so they don't overheat", "Elephants' large ears help them…", "lose heat quickly", ["keep warm", "store food", "hear underwater"])

# ---------------------------------------------------------------- 10.4
u.sec("10.4", "O4")
u.gd("r", "Conduction, convection or radiation?", "Transfer", [("Heat through a metal spoon", "Conduction"), ("Warm air rising from a heater", "Convection"), ("The Sun's heat reaching Earth", "Radiation"), ("Hot water rising in a pan", "Convection")])
u.gd("r", "Conductor or insulator?", "Type", [("Copper", "Conductor"), ("Wool", "Insulator"), ("Air", "Insulator"), ("Steel", "Conductor")])
u.gd("r", "Which surface is best at each job?", "Surface", [("Absorbing radiation", "Dull black"), ("Reflecting radiation", "Shiny silver")], extra=["Rough grey"])
u.ex("r", "Explain how a convection current warms a whole room from one heater.", [("air near heater warms, expands, less dense", ["expand|less dense|warm"]), ("warm air rises", ["rise"]), ("cooler denser air sinks and replaces it – current", ["sink|cool|replace|current"])],
     "Air next to the heater warms, expands and becomes less dense, so it rises. Cooler, denser air sinks to take its place and is heated in turn, setting up a convection current round the room.")
u.mc("r", "Conduction happens mainly in…", "solids", ["gases", "a vacuum", "light"])
u.mc("r", "Radiation transfers heat by…", "infrared waves", ["moving particles", "direct contact", "sound waves"])
u.mc("r", "Why can't convection happen in a solid?", "The particles cannot move from place to place", ["Solids have no particles", "Solids are always cold", "Solids are too light"], d="H")
u.mc("r", "How does conduction pass heat along a spoon?", "Particles at the hot end vibrate faster and pass the vibrations on", ["Hot particles flow to the other end", "Infrared waves only", "Air rises along it"], d="VH")
mcs("p", [
    ("Convection happens in…", "liquids and gases", ["solids only", "a vacuum", "metals"]),
    ("Radiation needs…", "no medium", ["a solid", "a liquid", "air"]),
    ("Metals are good…", "conductors", ["insulators", "absorbers of sound", "convectors"]),
    ("Plastic and wood are…", "insulators", ["conductors", "metals", "radiators"]),
    ("Heated fluid becomes … dense.", "less", ["more", "equally", "infinitely"]),
    ("Cooler fluid…", "sinks", ["rises", "evaporates instantly", "stays still always"]),
    ("Dull black surfaces are good at … radiation.", "absorbing and emitting", ["reflecting", "blocking all", "making"]),
    ("Shiny white or silver surfaces … radiation.", "reflect", ["absorb", "emit best", "create"]),
    ("The Sun's heat crosses space by…", "radiation", ["conduction", "convection", "evaporation"]),
    ("Saucepan handles are made of plastic because plastic is…", "an insulator", ["a conductor", "shiny", "dense"]),
    ("Heaters are placed low in a room because…", "warm air rises", ["warm air sinks", "floors are cold", "radiation goes down"]),
    ("Fridges have the freezer at the top because…", "cold air sinks", ["cold air rises", "heat rises in fridges", "it looks better"]),
    ("Emergency blankets are shiny to…", "reflect body heat back", ["absorb sunlight", "conduct heat away", "look bright"]),
    ("In hot countries houses are often painted white to…", "reflect radiation", ["absorb more heat", "conduct heat in", "make convection"]),
    ("A convection current is…", "the circulation of a fluid as warm parts rise and cool parts sink", ["heat moving through a solid", "infrared waves", "evaporation"]),
])
u.mt("p", "Match the transfer to how it works.", [("Conduction", "vibrations passed between particles"), ("Convection", "warm fluid rises, cool fluid sinks"), ("Radiation", "infrared waves")])
u.ms("p", "Select ALL the insulators.", ["Wool", "Air", "Plastic", "Wood"], ["Copper", "Iron"])
u.tb("p", "Cans of hot water cool for 10 minutes. Complete the drop.", ["Can surface", "Start (°C)", "End (°C)", "Drop (°C)"], [["Dull black", "80", "58", B(22)], ["Shiny silver", "80", "70", B(10)]])
u.ex("a", "Explain why a double-glazed window reduces heat loss from a house.", [("trapped air/gas layer between panes", ["air|gas|gap|layer"]), ("air is a poor conductor / insulator", ["insulat|poor conductor"]), ("narrow gap limits convection", ["convect|narrow|small gap"])],
     "Double glazing traps a thin layer of air or gas between two panes. Air is a poor conductor, and the narrow gap stops much convection, so less heat is lost.")
u.mc("a", "Why do solar water heaters on roofs have black panels?", "Black absorbs radiation best, heating the water more", ["Black reflects heat", "Black conducts electricity", "Black is cheaper only"], skill="Application")
u.mc("a", "Why does a metal bench feel colder than a wooden bench at the same temperature?", "Metal conducts heat away from your hand faster", ["The metal is colder", "Wood creates heat", "Metal radiates cold"], skill="Reasoning")
u.mc("a", "Using the can results, which surface emits radiation better?", "Dull black, because it cooled more", ["Shiny silver, because it cooled less", "They are the same", "Neither emitted any"], skill="Data")
u.stop("plastic, wood, wool and air are insulators", "Conduction happens mainly in…", "solids", ["gases", "a vacuum", "light"])
u.stop("That's how a heater warms a whole room", "Hot fluid rises because it is…", "less dense", ["denser", "heavier", "colder"])
u.stop("shiny white or silver surfaces reflect it", "Heat from the Sun crosses space by…", "radiation", ["conduction", "convection", "evaporation"])

# ---------------------------------------------------------------- 10.5
u.sec("10.5", "O5")
u.gd("r", "Does each change make evaporation faster or slower?", "Effect", [("Higher temperature", "Faster"), ("Windy day", "Faster"), ("Humid (damp) air", "Slower"), ("Larger surface area", "Faster")])
u.tb("r", "Temperature of a thermometer bulb wrapped in wet cotton. Complete the drop.", ["Bulb", "Start (°C)", "After 5 min (°C)", "Drop (°C)"], [["Dry", "22", "22", B(0)], ["Wet", "22", "17", B(5)]])
u.gd("r", "Washing on a line: which dries fastest?", "Speed", [("Warm, windy, dry day", "Fastest"), ("Cold, still, damp day", "Slowest")], extra=["Same"])
u.ex("r", "Explain why sweating cools you down.", [("fastest particles escape as vapour", ["fastest|most energy|escape"]), ("particles left have less energy on average", ["left|less energy|average"]), ("so temperature drops / heat carried from skin", ["temperature drop|cool|carr"])],
     "The fastest-moving particles in sweat escape as vapour. The particles left behind have less energy on average, so the sweat's temperature drops and heat is taken from your skin.")
u.mc("r", "Evaporation can happen…", "below the boiling point", ["only at the boiling point", "only in solids", "only above 100 °C"])
u.mc("r", "Particles that escape first from a liquid's surface are…", "the fastest ones", ["the slowest ones", "the heaviest ones", "random only"])
u.mc("r", "Why does wind increase evaporation?", "It carries vapour away so more particles can escape", ["It adds water", "It cools the liquid", "It increases humidity"], d="H")
u.mc("r", "Why does a wet thermometer bulb read lower than a dry one?", "Evaporation removes the most energetic particles, cooling the bulb", ["Water is always colder than air", "The cotton blocks heat", "The dry bulb is broken"], d="VH")
mcs("p", [
    ("Evaporation causes the remaining liquid to…", "cool down", ["heat up", "freeze instantly", "become denser always"]),
    ("Evaporation is faster in…", "dry air", ["damp air", "still, cold air", "a sealed jar"]),
    ("A puddle dries faster when it is…", "spread out over a large area", ["deep and narrow", "covered", "in the shade at night"]),
    ("Dogs pant to…", "cool down by evaporation", ["warm up", "smell better", "drink water"]),
    ("Clay water pots keep water cool because water…", "evaporates through the clay", ["freezes in the clay", "is heated by the Sun", "stops moving"]),
    ("After swimming, you feel cold because water…", "evaporates from your skin", ["is heavier", "conducts heat in", "makes you wet only"]),
    ("Evaporation happens at the … of a liquid.", "surface", ["bottom", "centre", "container walls only"]),
    ("Boiling happens…", "throughout the liquid at its boiling point", ["only at the surface", "below 0 °C", "at any temperature"]),
    ("A higher temperature means more particles have…", "enough energy to escape", ["less energy", "no energy", "the same energy"]),
    ("Humid air already contains a lot of…", "water vapour", ["oxygen", "smoke", "dust only"]),
    ("Sweat evaporates more slowly on a … day.", "humid", ["dry", "windy", "hot and dry"]),
    ("Fanning yourself helps you cool because it…", "speeds up evaporation of sweat", ["makes air hotter", "adds water", "stops sweating"]),
    ("Perfume smells spread because it…", "evaporates quickly", ["freezes", "sinks", "conducts"]),
    ("Evaporation needs energy, which it takes from…", "the liquid and its surroundings", ["nowhere", "the Moon", "the container only"]),
    ("A wet cloth around a bottle keeps the drink…", "cooler", ["hotter", "the same", "frozen solid"]),
])
u.ms("p", "Select ALL the conditions that speed up evaporation.", ["Wind", "Warmth", "Dry air", "Large surface area"], ["Humid air", "Cold, still air"])
u.mt("p", "Match the example to the factor.", [("Washing dries faster in a breeze", "wind"), ("Puddle dries faster in the sun", "temperature"), ("Tea cools faster in a saucer", "surface area")])
u.od("p", "Order to explain cooling by evaporation.", ["Particles in the liquid have different energies", "The fastest particles escape from the surface", "The remaining particles have less energy on average", "The liquid's temperature falls"])
u.ex("a", "Plan an investigation into how surface area affects the rate of evaporation.", [("same volume of water in containers of different widths", ["same volume|different width|different surface|dish"]), ("keep temperature, wind, humidity same", ["same|control|temperature"]), ("measure volume/mass left after set time", ["measure|mass|volume|time"])],
     "Put the same volume of water into containers with different surface areas. Keep them in the same place so temperature, wind and humidity are the same. Measure the mass or volume left after a set time.")
u.nm("a", "A dish of water had a mass of 120 g. After 4 hours it was 96 g. What was the average rate of evaporation?", 6, "g/h")
u.mc("a", "Why is sweating less effective at cooling you in a humid rainforest?", "Humid air slows evaporation of sweat", ["Rainforests are cold", "Sweat cannot form there", "Humid air speeds up evaporation"], skill="Reasoning")
u.mc("a", "Why does a liquid left in a sealed jar stop losing volume after a while?", "The air in the jar becomes saturated with vapour", ["Evaporation only happens in wind", "The liquid freezes", "Particles stop moving"], skill="Reasoning")
u.stop("This is cooling by evaporation", "When the fastest particles evaporate, the liquid left behind…", "cools down", ["heats up", "boils", "freezes instantly"])
u.stop("and with a larger surface area", "Which makes evaporation faster?", "Wind", ["Damp air", "Cold temperature", "Small surface area"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Thermal energy", "sec": None, "kids": [
    {"id": "ht", "t": "Heat vs temperature", "d": "Heat: energy transferred, joules • Temperature: average kinetic energy, °C", "obj": "O1", "sec": "10.1"},
    {"id": "cn", "t": "Conservation", "d": "Not created or destroyed • Energy diagrams • Efficiency", "obj": "O2", "sec": "10.2"},
    {"id": "ds", "t": "Dissipation", "d": "Hot → cold • Open and closed systems • Insulation", "obj": "O3", "sec": "10.3"},
    {"id": "tr", "t": "Transfer", "d": "Conduction: solids • Convection: fluids • Radiation: infrared, no medium", "obj": "O4", "sec": "10.4"},
    {"id": "ev", "t": "Evaporation", "d": "Fastest particles escape • Liquid cools • Faster with heat, wind, dry air, large area", "obj": "O5", "sec": "10.5"},
]}
