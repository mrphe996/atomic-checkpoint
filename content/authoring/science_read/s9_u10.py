# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 10 Transfer of Thermal Energy – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9Pf.02–9Pf.06)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}
CARD = lambda title, cards, cols=None: dict({"kind": "sciCards", "title": title, "cards": cards}, **({"cols": cols} if cols else {}))

# =====================================================================================================
# 10.1 Heat and temperature · 9Pf.02
# =====================================================================================================
READ["10.1"] = L(
    H("A spark and a bath",
      "A sparkler's sparks are over 1000 °C, yet they barely hurt when they land on your hand. A bath of water at 45 °C would scald you badly.",
      "How can the cooler bath be more dangerous?"),
    I("Thermal energy",
      "**Thermal energy** is the total energy of all the moving, vibrating particles in an object.",
      then=["A bathtub and a cup of water at the same temperature feel the same, but the bathtub holds far more thermal energy – it has far more particles. A spark is very hot but has so few particles that it has very little thermal energy."]),
    I("Heat and temperature",
      "These two words mean different things in science.",
      table=[["", "Heat", "Temperature"], ["what it is", "thermal energy **transferred** from a hotter object to a cooler one", "how hot or cold something is – the **average kinetic energy** of its particles"],
             ["unit", "joules (J)", "degrees Celsius (°C) or kelvin"], ["measured with", "calculated from energy transfers", "a thermometer"]],
      then=["Heat flows from hot to cold until both reach the **same temperature**.",
            "In the 1790s Count Rumford noticed that drilling cannons produced endless heat – evidence that heat is a form of energy, not a substance."]),
    Y("Heat or temperature?",
      grid("s9u10r11", "Does each statement describe heat or temperature?", ["Heat", "Temperature"],
           [("measured in °C", "Temperature"), ("measured in joules", "Heat"), ("energy flowing from a radiator to the room", "Heat"), ("the average kinetic energy of the particles", "Temperature")],
           "Energy transferred, or how hot?", "Heat is energy transferred (J); temperature is how hot (°C), the average particle energy.")),
    Y("More thermal energy",
      mcq("s9u10r12", "Which has the most thermal energy?",
          [("a swimming pool at 26 °C", True, "Yes – a huge number of particles, even at a lower temperature."), ("a cup of tea at 80 °C", False, "Hotter, but far fewer particles."),
           ("a spark at 1000 °C", False, "Very hot, but tiny."), ("a candle flame", False, "Hot but very small.")],
          "Thermal energy depends on the number of particles too.", "The pool's enormous mass gives it far more thermal energy.")),
    K("Key points",
      "**Thermal energy**: total energy of all the particles; depends on temperature **and** amount of material.",
      "**Heat**: thermal energy transferred from hot to cold (J).",
      "**Temperature**: average kinetic energy of the particles (°C)."),
    book=BK(
        [("thermal energy", "the total energy of the particles in an object"), ("heat", "thermal energy transferred from a hotter to a cooler object"),
         ("temperature", "a measure of how hot something is; the average kinetic energy of its particles")],
        [], [],
        [Ex("Explain the difference between heat and temperature.", ans="Heat is energy transferred (J); temperature measures how hot something is – the average kinetic energy of its particles (°C)."),
         Ex("A cup of tea at 70 °C is left in a room at 20 °C. Which way does heat flow, and when does it stop?", ans="from the tea to the room, until both are at the same temperature"),
         Ex("Back to 'Start here': explain why the bath is more dangerous than the sparks.", ans="The bath has vastly more thermal energy to transfer to your skin, even though its temperature is lower.", think=True)],
        ["distinguish heat and temperature", "explain thermal energy using particles"],
        look=["the heat and temperature table"],
        note="Read it after the video: heat, temperature and thermal energy (answers at the back)."),
)

# =====================================================================================================
# 10.2 Energy conservation · 9Pf.03
# =====================================================================================================
READ["10.2"] = L(
    H("Where did it go?",
      "You charge your phone fully. A day later the battery is empty, and nothing seems to have been made.",
      "Has the energy been used up and destroyed? Where has it gone?"),
    I("Energy is conserved",
      "**Law of conservation of energy**: energy cannot be created or destroyed – only **transferred** from one store to another. The total stays the same.",
      then=["Your phone's energy went to light, sound and – mostly – thermal energy that spread into the surroundings."]),
    I("Energy diagrams and efficiency",
      "For every 100 J supplied to a lamp:",
      fig={"kind": "barchart", "labels": ["filament: light", "filament: heat", "LED: light", "LED: heat"], "values": [10, 90, 75, 25], "ymax": 100, "step": 20, "ylabel": "energy (J per 100 J supplied)", "xlabel": "output"},
      then=["The 'lost' energy has not vanished; it has gone to stores that are not useful, mostly heat.",
            "**Efficiency = useful energy out ÷ total energy in** (× 100 for %). The filament lamp is 10% efficient; the LED 75%."]),
    W("Efficiency",
      "A motor is supplied with 500 J and gives 350 J of useful kinetic energy. What is its efficiency?",
      [("efficiency = useful ÷ total", "write the equation"), ("= 350 ÷ 500 = 0.7", "calculate"), ("0.7 × 100 = 70%", "as a percentage")], "70%",
      check="Wasted energy = 500 − 350 = 150 J, so total out = 350 + 150 = 500 J – energy is conserved."),
    Y("Efficiency",
      num("s9u10r21", "A kettle is supplied with 2000 J and 1800 J heats the water. What is its efficiency in %?", 90, "useful ÷ total × 100.", "1800 ÷ 2000 × 100 = 90%.")),
    K("Key points",
      "Energy is **conserved**: never created or destroyed, only transferred.",
      "Wasted energy usually ends up as heat in the surroundings.",
      "**Efficiency** = useful energy out ÷ total energy in; efficient devices waste less."),
    book=BK(
        [("conservation of energy", "energy cannot be created or destroyed"), ("efficiency", "useful energy out ÷ total energy in"), ("wasted energy", "energy transferred to stores that are not useful")],
        [], [],
        [Ex("A TV uses 200 J and gives 60 J of light and sound. How much is wasted, and what is its efficiency?", ans="140 J wasted; 30%"),
         Ex("Why can a machine never be more than 100% efficient?", ans="It cannot give out more energy than is put in – energy cannot be created."),
         Ex("Explain why changing to LED lamps helps the environment.", ans="They are more efficient, so less electricity is needed for the same light, and less fuel is burned.", think=True)],
        ["use the law of conservation of energy", "calculate efficiency"],
        look=["the lamp energy chart"],
        note="Read it after the video: conservation of energy and efficiency (answers at the back)."),
)

# =====================================================================================================
# 10.3 Heat dissipation · 9Pf.04
# =====================================================================================================
READ["10.3"] = L(
    H("Why does tea go cold?",
      "A hot cup of tea always cools down to room temperature. A cold drink always warms up. Neither ever goes the other way by itself.",
      "Describe what you think is happening to the energy."),
    I("Heat dissipation",
      "Thermal energy always spreads from **hotter** regions to **cooler** ones until everything is at the same temperature. This spreading out is **dissipation**.",
      then=["An **open system** exchanges energy and matter with its surroundings (an open cup of tea loses heat and steam); a **closed system** exchanges only energy.",
            "**Insulation** slows the flow of heat – a vacuum flask keeps drinks hot or cold for hours."]),
    I("Class data: a cup of tea cooling",
      "Tea cooling in a room at 22 °C:",
      fig={"kind": "linegraph", "x": {"min": 0, "max": 60, "step": 10, "label": "time (minutes)"}, "y": {"min": 20, "max": 90, "step": 10, "label": "temperature (°C)"},
           "series": [{"pts": [[0, 85], [5, 70], [10, 59], [20, 45], [30, 36], [40, 31], [50, 27], [60, 25]]}]},
      then=["The tea cools fastest at first, when the temperature difference with the room is biggest. The curve gets less steep and the tea will end at **22 °C**, room temperature."]),
    Y("Cooling",
      num("s9u10r31", "Use the graph. How many degrees did the tea cool in the first 10 minutes?", 26, "Subtract the temperature at 10 min from the starting temperature.", "85 − 59 = 26 °C.")),
    I("Dissipation in nature and technology",
      "Sometimes we want heat to dissipate quickly.",
      fig=CARD("Getting rid of heat", [{"t": "Elephant ears", "d": "large, thin, full of blood vessels: lose heat fast"}, {"t": "Laptop fans and heat sinks", "d": "metal fins with a large surface area"},
                                       {"t": "Car radiators", "d": "thin metal fins cool the engine water"}], 3)),
    K("Key points",
      "Heat dissipates from hotter to cooler regions until temperatures are equal.",
      "Objects cool fastest when the temperature difference is biggest.",
      "Insulation slows dissipation; large surface areas speed it up."),
    book=BK(
        [("dissipation", "energy spreading out into the surroundings"), ("insulation", "material that slows the transfer of heat"),
         ("open system", "exchanges energy and matter with its surroundings"), ("closed system", "exchanges only energy")],
        [], [],
        [Ex("Explain why the tea cools more slowly as time goes on.", ans="The temperature difference with the room gets smaller, so heat flows out more slowly."),
         Ex("What temperature will the tea finally reach? Why?", ans="22 °C – room temperature; then there is no temperature difference."),
         Ex("How does an elephant's ear help it keep cool?", ans="Its large thin surface with many blood vessels lets heat dissipate quickly."),
         Ex("Suggest how to keep soup hot for longer on a school trip.", ans="Use an insulated (vacuum) flask with a lid to reduce heat loss.", think=True)],
        ["describe heat dissipation", "interpret cooling curves", "describe how insulation slows heat loss"],
        look=["the cooling curve"],
        note="Read it after the video: heat dissipation and cooling curves (answers at the back)."),
)

# =====================================================================================================
# 10.4 How is thermal energy transferred? · 9Pf.05
# =====================================================================================================
READ["10.4"] = L(
    H("Three journeys",
      "A metal spoon in hot soup gets hot. The whole room warms up from one heater. You feel the Sun's warmth across 150 million kilometres of empty space.",
      "These are three different ways heat travels. Can you name them?"),
    I("Predict, watch, explain: which rod conducts best?",
      "Rods of copper, steel and glass are heated at one end, with pins stuck on by wax along each. The copper pins fall first, then steel; the glass pins stay.",
      fig={"kind": "rods", "metals": ["copper", "steel", "glass"], "fallen": [3, 1, 0]},
      then=["Particles at the hot end vibrate faster and pass the vibrations along – **conduction**. Metals also have **free electrons** that carry energy quickly, so copper conducts best. Glass is a poor conductor – an **insulator**."]),
    I("Conduction",
      "**Conduction**: heat passes through a material by particles vibrating and passing energy to their neighbours (plus free electrons in metals). It happens mainly in **solids**.",
      then=["Good conductors: metals. Insulators: plastic, wood, wool, air. Trapped air makes good insulation – feathers, fleece, double glazing."]),
    I("Convection",
      "**Convection** happens in **liquids and gases**. Heated fluid expands, becomes **less dense** and **rises**; cooler, denser fluid sinks to take its place – a **convection current**.",
      fig={"kind": "sciConvection"}),
    I("Radiation",
      "**Radiation**: heat travels as **infrared waves**. It needs **no medium** – that is how the Sun's heat crosses empty space.",
      table=[["Surface", "Absorbing and emitting infrared"], ["dull, black", "best absorber and best emitter"], ["shiny, white or silver", "poor absorber (reflects) and poor emitter"]],
      then=["That is why emergency blankets are shiny and houses in hot countries are painted white."]),
    Y("Which transfer?",
      grid("s9u10r41", "How is heat mainly transferred?", ["Conduction", "Convection", "Radiation"],
           [("the handle of a metal pan gets hot", "Conduction"), ("warm air rises from a heater", "Convection"), ("you feel the warmth of a fire across the room", "Radiation"),
            ("the Sun warms the Earth", "Radiation"), ("water circulates in a heated pan", "Convection")],
           "Solid contact, moving fluid, or waves?", "Through solid = conduction; moving fluid = convection; infrared waves = radiation.")),
    K("Key points",
      "**Conduction**: vibrating particles (and free electrons) pass energy through solids; metals conduct best.",
      "**Convection**: hot fluid rises, cool fluid sinks – convection currents in liquids and gases.",
      "**Radiation**: infrared waves; no medium needed; dull black surfaces absorb and emit best."),
    book=BK(
        [("conduction", "heat transfer through a material by particle vibrations"), ("convection", "heat transfer by the movement of a liquid or gas"),
         ("radiation", "heat transfer by infrared waves"), ("insulator", "a poor conductor of heat")],
        [], [],
        [Ex("Explain why copper conducts heat better than glass.", ans="Copper has free electrons that carry energy quickly; glass has none."),
         Ex("Explain how a heater on one wall warms a whole room.", ans="Air near it is heated, becomes less dense and rises; cooler air sinks and moves in – a convection current spreads the heat."),
         Ex("Why are kettles often shiny and saucepans' bases dark?", ans="Shiny surfaces emit less heat (keep water hot); dark bases absorb heat well."),
         Ex("Why can heat reach us from the Sun by radiation but not by conduction or convection?", ans="Space is a vacuum; conduction and convection need particles, radiation does not.", think=True)],
        ["explain conduction, convection and radiation", "use the particle model and waves to explain heat transfer"],
        look=["the conducting rods", "the convection current"],
        note="Read it after the video: conduction, convection and radiation (answers at the back)."),
)

# =====================================================================================================
# 10.5 Cooling by evaporation · 9Pf.06
# =====================================================================================================
READ["10.5"] = L(
    H("Wet and cold",
      "Step out of a swimming pool on a breezy day and you shiver – even though the air is warm.",
      "Why do you feel colder when you are wet?"),
    I("Cooling by evaporation",
      "Particles in a liquid move at different speeds. The **fastest** ones at the surface have enough energy to escape as a gas – **evaporation**.",
      then=["The particles left behind have a **lower average kinetic energy**, so the liquid **cools**. It then takes heat from your skin.",
            "This is why sweating cools you down, why a wet cloth round a clay pot keeps water cool, and why hand sanitiser feels cold."]),
    I("Factors affecting the rate of evaporation",
      "Evaporation – and cooling – is faster when:",
      table=[["Factor", "Why"], ["**higher temperature**", "more particles have enough energy to escape"], ["**wind (moving air)**", "carries vapour away so more can escape"],
             ["**dry air (low humidity)**", "the air can take up more water vapour"], ["**larger surface area**", "more particles are at the surface"]]),
    Y("Fastest drying",
      mcq("s9u10r51", "Where will wet washing dry fastest?",
          [("spread out on a line on a warm, dry, windy day", True, "Yes – heat, wind, dry air and a large surface area."), ("folded in a basket on a cold, still day", False, "Small surface, cold, no wind."),
           ("on a line on a cold, humid, still day", False, "Cold, humid, no wind."), ("in a closed bathroom", False, "Humid air and no wind.")],
          "Use all four factors.", "Warm, windy, dry and spread out → fastest evaporation.")),
    K("Key points",
      "Evaporation removes the most energetic particles, so the remaining liquid **cools**.",
      "Sweating cools the body by evaporation.",
      "Faster evaporation: higher temperature, wind, dry air, larger surface area."),
    book=BK(
        [("evaporation", "particles escaping from the surface of a liquid as a gas"), ("humidity", "the amount of water vapour in the air")],
        [], [],
        [Ex("Explain, using particles, why evaporation cools a liquid.", ans="The fastest particles escape, so the average kinetic energy of those left falls – the liquid is cooler."),
         Ex("Give four factors that increase the rate of evaporation.", ans="higher temperature, wind, low humidity, larger surface area"),
         Ex("Quick quiz.", ("Difference between heat and temperature?", "heat is energy transferred; temperature is average particle energy"), ("Can energy be created or destroyed?", "no"),
            ("How does heat travel from the Sun to the Earth?", "by radiation"), ("Why does sweating cool you?", "the fastest particles evaporate, leaving cooler sweat")),
         Ex("Why do you feel hotter on a humid day than on a dry day at the same temperature?", ans="Sweat evaporates more slowly in humid air, so it cools you less.", think=True)],
        ["explain cooling by evaporation", "describe factors that affect the rate of evaporation"],
        look=["why evaporation cools", "the factors table"],
        note="Read it after the video: cooling by evaporation, plus a quick quiz (answers at the back)."),
)
