# -*- coding: utf-8 -*-
"""Stage 8 Unit 12 – Renewable and Non-Renewable Energy Resources. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Physics"
BLURB = "Why we need energy, how fossil fuels and nuclear power produce electricity and their costs, and the advantages and drawbacks of solar, wind, water, geothermal and biomass energy."
OBJECTIVES = {
    "O1": {"sec": "12.1", "code": "8ESp.02, 8SIC.02", "codeNote": "", "t": "Describe what an energy resource is and why every part of society needs energy."},
    "O2": {"sec": "12.2", "code": "8ESp.02, 8SIC.05", "codeNote": "", "t": "Explain how fossil fuels and nuclear fuels generate electricity, why they are non-renewable, and their environmental impacts."},
    "O3": {"sec": "12.3", "code": "8ESp.02, 8SIC.03", "codeNote": "", "t": "Describe renewable energy resources and evaluate their advantages and disadvantages."},
}
SECTIONS = [
    {"id": "12.1", "title": "Energy needs and energy resources", "objs": ["O1"]},
    {"id": "12.2", "title": "Non-renewable energy resources", "objs": ["O2"]},
    {"id": "12.3", "title": "Renewable energy resources", "objs": ["O3"]},
]
u = Unit(8, 12)

# ---------------------------------------------------------------- 12.1
u.sec("12.1", "O1")
u.gd("r", "Which part of society uses energy for each?", "Sector", [("Heating, lighting and cooking", "Homes"), ("Cars, buses and planes", "Transport"), ("Running machines in factories", "Industry"), ("Hospital equipment", "Healthcare")])
u.gd("r", "Which energy resource is each?", "Resource type", [("Coal", "Fossil fuel"), ("Uranium", "Nuclear fuel"), ("Wood", "Biofuel"), ("Battery cells", "Stored electricity")], extra=["Wind"])
u.mc("r", "An energy resource is…", "anything from which we can get energy", [("only electricity", "No."), ("only fuels we burn", "No."), ("a type of machine", "No.")])
u.ex("r", "Describe what would happen to a city if its reliable energy supply failed.", [("homes go dark / no heating or cooking", ["dark|light|heat|cook"]), ("factories / transport stop", ["factor|industry|transport|stop"]), ("economy / healthcare suffers", ["econom|hospital|health|money"])],
     "Homes would have no light, heating or cooking, factories and transport would stop, hospitals could not run equipment, and the economy would suffer.")
u.mc("r", "Most of the energy we use is in the form of…", "electricity", ["sound", "light only", "magnetism"])
u.mc("r", "Solar panels make a current when particles of light, called…, knock electrons out of atoms.", "photons", ["protons", "neutrons", "ions"], d="H")
u.mc("r", "Why do we use more energy today than ever before?", "We use more technology", [("We use fewer machines", "No."), ("The Sun is weaker", "No."), ("Energy is used up faster by itself", "No.")], d="H")
u.mc("r", "When wood burns, which energy store is released as heat?", "Chemical", ["Nuclear", "Elastic", "Magnetic"], d="VH")
for p, r, w in [
    ("Which is an energy resource?", "Natural gas", ["A light bulb", "A wire", "A switch"]),
    ("Fossil fuels include…", "coal and oil", ["uranium and plutonium", "wind and waves", "wood and crops"]),
    ("A nuclear fuel is…", "uranium", ["coal", "wood", "wind"]),
    ("Biofuels come from…", "living things", ["rocks", "the Sun directly", "magnets"]),
    ("Data centres need energy to run…", "computers", ["tractors", "wind farms", "ovens"]),
    ("Farming uses energy for…", "machinery and pumping water", ["nothing", "only sunlight", "only rain"]),
    ("Photovoltaic cells turn light into…", "electricity", ["heat only", "sound", "fuel"]),
    ("Solar panels are…", "clean and renewable", ["polluting fossil fuels", "nuclear", "non-renewable"]),
    ("Electricity can be stored in…", "cells (batteries)", ["wires", "switches", "magnets"]),
    ("Energy for cooking at home is an example of energy for…", "homes", ["industry", "transport", "farming"]),
    ("A reliable energy supply is important for the…", "economy", ["weather", "Moon", "tides"]),
    ("Burning wood releases energy as…", "heat and light", ["sound only", "magnetism", "nothing"]),
    ("Which sector uses energy to move people and goods?", "Transport", ["Homes", "Healthcare", "Data centres"]),
    ("Healthcare uses energy for…", "hospital equipment", ["growing crops", "mining", "nothing"]),
    ("Which energy resource is NOT a fuel?", "Wind", ["Coal", "Oil", "Uranium"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the energy resources.", ["Oil", "Wind", "Biofuel"], ["A kettle", "A wire"])
u.mt("p", "Match the resource to its type.", [("Coal", "fossil fuel"), ("Uranium", "nuclear fuel"), ("Ethanol from crops", "biofuel")])
u.od("p", "Order how a solar panel makes current.", ["Light (photons) hits the panel", "Photons knock electrons out of atoms", "Electrons flow", "An electric current is produced"])
u.ex("a", "* Advanced. Explain why energy demand has grown over the last 50 years.", [("more people / population", ["people|population"]), ("more technology / devices / data centres", ["technolog|device|computer|data"]), ("more transport / industry", ["transport|industr|car|factor"])],
     "There are more people, and each person uses more technology such as phones, computers and data centres, as well as more transport and industry, so demand for energy keeps rising.")
u.mc("a", "Why is electricity the most common form of energy we use?", "It is easy to transfer along wires and convert into many other forms.", ["It is free.", "It never runs out.", "It cannot be stored."], skill="Reasoning")
u.mc("a", "Which is an advantage of storing energy in cells?", "Energy can be used later and moved around.", ["Cells never run out.", "Cells are a fossil fuel.", "Cells make energy from nothing."], skill="Reasoning")
u.gd("a", "Which uses energy most directly in each case?", "Main use", [("Fridge", "Keeping food cold"), ("Street lights", "Lighting"), ("Electric train", "Transport")])
u.stop("It's clean and renewable", "Photovoltaic cells turn light into…", "electricity", ["heat only", "sound", "fuel"])
u.stop("and electricity stored in cells", "An energy resource is…", "anything from which we can get energy", ["only electricity", "only coal", "a machine"])
u.stop("than ever before", "Most of the energy we use is in the form of…", "electricity", ["sound", "magnetism", "light only"])

# ---------------------------------------------------------------- 12.2
u.sec("12.2", "O2")
u.od("r", "Order the steps in a fossil-fuel power station.", ["Fuel is burnt", "Heat turns water into steam", "Steam drives turbines", "Turbines turn generators", "Electricity is produced"])
u.gd("r", "What problem does each pollutant or process cause?", "Effect", [("Carbon dioxide", "Global warming"), ("Sulfur dioxide", "Acid rain"), ("Fracking", "Tremors"), ("Radioactive waste", "Long-term contamination")])
u.mc("r", "Why are fossil fuels non-renewable?", "They took millions of years to form and can only be used once", [("They are made every day", "No."), ("They come from the Sun", "Indirectly, but not the reason."), ("They are too expensive", "No.")])
u.ex("r", "Explain how nuclear fission releases energy in a chain reaction.", [("neutron hits a uranium nucleus", ["neutron"]), ("nucleus splits releasing energy and more neutrons", ["split|energy|more neutrons"]), ("these split more nuclei – chain reaction", ["chain|more nuclei|continue"])],
     "A neutron hits a large uranium nucleus, which splits, releasing energy and more neutrons. These neutrons split more nuclei, which release more neutrons – a chain reaction.")
u.tb("r", "Approximate share of electricity from each source in a country. Complete the table.", ["Source", "Share (%)"], [["Coal", "40"], ["Gas", "25"], ["Nuclear", "10"], ["Renewables", B(25)]])
u.mc("r", "Crude oil and natural gas formed mostly from…", "marine microorganisms", ["dinosaurs only", "volcanic rock", "sand"], d="H")
u.mc("r", "Why is nuclear fuel also non-renewable?", "Uranium is mined and limited", [("It forms quickly", "No."), ("It comes from wind", "No."), ("It can be reused forever", "No.")], d="H")
u.mc("r", "Why is fracking controversial even though it produces gas?", "It can cause tremors, uses lots of water and shale gas is still a fossil fuel", [("It makes renewable energy", "No."), ("It removes carbon dioxide", "No."), ("It cools the Earth", "No.")], d="VH")
for p, r, w in [
    ("Fossil fuels formed from…", "the remains of living things", ["rocks only", "sea water", "sunlight directly"]),
    ("Coal formed from…", "layers of decayed plant matter", ["marine microorganisms", "volcanoes", "ice"]),
    ("Coal is obtained by…", "mining", ["drilling only", "fracking", "photosynthesis"]),
    ("Oil and gas are extracted by…", "drilling deep into rock", ["picking", "filtering sea water", "mining coal"]),
    ("In a power station, turbines turn…", "generators", ["boilers", "chimneys", "cooling towers only"]),
    ("Burning fossil fuels releases…", "carbon dioxide", ["oxygen", "uranium", "water only"]),
    ("Carbon dioxide is a…", "greenhouse gas", ["toxic metal", "fuel", "nuclear waste"]),
    ("Climate change is linked to more…", "extreme weather", ["earthquakes only", "eclipses", "tides"]),
    ("Fracking pumps water, sand and chemicals into…", "shale rock", ["the ocean", "the atmosphere", "rivers"]),
    ("Splitting a large nucleus is called…", "nuclear fission", ["combustion", "fusion only", "photosynthesis"]),
    ("A nuclear power plant boils water using heat from…", "fission", ["burning coal", "the Sun", "wind"]),
    ("Radioactive waste must be stored safely for…", "a very long time", ["one day", "one week", "no time"]),
    ("The Chernobyl accident happened in…", "1986", ["1906", "2006", "1966"]),
    ("Hot cooling water from power plants can harm…", "aquatic life", ["the Moon", "rocks only", "the Sun"]),
    ("Scientists map extreme weather events using…", "keys and classification", ["mirrors", "magnets", "thermometers only"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the non-renewable energy resources.", ["Coal", "Natural gas", "Uranium"], ["Wind", "Sunlight"])
u.mt("p", "Match the fuel to how it is obtained.", [("Coal", "mined"), ("Crude oil", "drilled"), ("Shale gas", "fracked")])
u.gd("p", "Fossil fuel or nuclear fuel?", "Type", [("Coal", "Fossil fuel"), ("Uranium", "Nuclear fuel"), ("Natural gas", "Fossil fuel")])
u.ex("a", "* Advanced. Compare the environmental impacts of a coal power station and a nuclear power station.", [("coal releases CO2 / global warming", ["carbon dioxide|co2|global warming|greenhouse"]), ("coal releases SO2 / acid rain", ["sulfur|acid rain|nitrogen"]), ("nuclear: little CO2 but radioactive waste / accidents", ["radioactive|waste|accident|chernobyl"])],
     "A coal station releases carbon dioxide, causing global warming, and sulfur dioxide, causing acid rain. A nuclear station releases very little carbon dioxide but produces radioactive waste that must be stored for a very long time, and accidents can contaminate land.")
u.nm("a", "A power station produces 500 MW of electricity from 1250 MW of fuel energy. What percentage is converted to electricity?", 40, "%")
u.mc("a", "Why do both coal and nuclear power stations need large amounts of water?", "To make steam to drive turbines and to cool the steam back down.", ["To burn the fuel.", "To store uranium.", "To make electricity directly."], skill="Reasoning")
u.mc("a", "Why does a chain reaction need to be controlled in a nuclear reactor?", "Otherwise it could release energy too quickly and become dangerous.", ["It would stop at once.", "It would make coal.", "It would cool the reactor."], skill="Reasoning")
u.stop("over millions of years", "Fossil fuels formed from…", "the remains of living things", ["volcanic lava", "sea salt", "sunlight"])
u.stop("They can only be used once", "Fossil fuels are non-renewable because…", "they took millions of years to form", ["they are cheap", "they are found everywhere", "they come from wind"])
u.stop("And shale gas is still a fossil fuel", "Burning fossil fuels releases…", "carbon dioxide", ["uranium", "oxygen", "helium"])
u.stop("This is nuclear fission", "Splitting a uranium nucleus to release energy is…", "nuclear fission", ["combustion", "photosynthesis", "fracking"])

# ---------------------------------------------------------------- 12.3
u.sec("12.3", "O3")
u.gd("r", "Renewable or non-renewable?", "Type", [("Solar", "Renewable"), ("Coal", "Non-renewable"), ("Geothermal", "Renewable"), ("Uranium", "Non-renewable")])
u.gd("r", "Match each drawback to the energy resource.", "Resource", [("Stops at night", "Solar"), ("Blades can kill birds", "Wind"), ("Dams flood habitats", "Hydropower"), ("Only renewable if replanted", "Biomass")])
u.mc("r", "Renewable energy resources are…", "in constant supply or replaced as fast as we use them", [("used only once", "That is non-renewable."), ("always cheap", "No."), ("found only underground", "No.")])
u.ex("r", "Evaluate wind energy: give one advantage and two disadvantages.", [("advantage: clean / no pollution / renewable", ["clean|no pollut|renewable|free"]), ("disadvantage: wind not constant", ["not constant|varies|no wind|unreliable"]), ("disadvantage: expensive / noisy / kills birds", ["expensive|noisy|noise|bird"])],
     "Wind energy is clean and renewable. But the wind is not constant, turbines are expensive and noisy, and spinning blades can kill birds.")
u.tb("r", "A solar farm generates electricity during the day. Complete the table.", ["Time", "Output (MW)"], [["06:00", "5"], ["12:00", "40"], ["18:00", "8"], ["00:00 (midnight)", B(0)]])
u.mc("r", "Why is Iceland able to use geothermal energy easily?", "Magma is close to the surface", [("It is very sunny", "No."), ("It has no rocks", "No."), ("It is windless", "No.")], d="H")
u.mc("r", "How can molten salt help solar power?", "It stores the Sun's heat so electricity can be made after sunset", [("It makes panels lighter", "No."), ("It cools the Sun", "No."), ("It produces uranium", "No.")], d="H")
u.mc("r", "Why is burning biomass described as carbon neutral only if crops are replanted?", "New plants take back in the carbon dioxide released by burning", [("Burning releases no carbon dioxide", "It does."), ("Biomass is a fossil fuel", "No."), ("Replanting adds uranium", "No.")], d="VH")
for p, r, w in [
    ("Solar thermal plants use mirrors to…", "focus the Sun's heat", ["make wind", "split atoms", "cool water"]),
    ("Wind turbines convert…", "kinetic energy into electricity", ["chemical energy into heat", "nuclear energy into light", "sound into electricity"]),
    ("A group of wind turbines is a…", "wind farm", ["power cell", "solar farm", "dam"]),
    ("Hydropower uses…", "moving water", ["coal", "uranium", "sunlight only"]),
    ("Tides, waves and ocean currents can turn…", "turbines", ["mirrors", "solar panels", "batteries"]),
    ("Geothermal energy uses heat from…", "hot rock and magma", ["the Moon", "wind", "fossil fuels"]),
    ("Biomass includes…", "wood, crops and animal waste", ["coal and oil", "uranium", "rocks"]),
    ("Ethanol made from crops is a…", "biofuel", ["fossil fuel", "nuclear fuel", "mineral"]),
    ("Bioplastics can be made from…", "corn starch or seaweed", ["crude oil only", "uranium", "sand"]),
    ("Exaggerating how green a company is is called…", "greenwashing", ["recycling", "photosynthesis", "fracking"]),
    ("Some solar panels contain lead and cadmium, which can…", "leak and pollute", ["make them lighter", "make more electricity", "attract birds"]),
    ("Birds sometimes crash into solar panels because they mistake them for…", "lakes", ["trees", "food", "nests"]),
    ("Windmills were used in the past to…", "pump water and grind grain", ["make electricity only", "power cars", "light homes"]),
    ("Dams only work…", "in certain places", ["everywhere", "in deserts", "on flat land with no rivers"]),
    ("Which renewable resource is in constant supply?", "Sunlight", ["Coal", "Natural gas", "Uranium"]),
]:
    u.mc("p", p, r, w)
u.ms("p", "Select ALL the renewable energy resources.", ["Solar", "Wind", "Hydropower", "Geothermal"], ["Oil", "Coal"])
u.mt("p", "Match the energy resource to how it works.", [("Solar PV", "light knocks out electrons"), ("Wind", "moving air turns blades"), ("Geothermal", "Earth's heat makes steam")])
u.od("p", "Order the steps in a hydroelectric power station.", ["Water is held behind a dam", "Water is released", "Water turns turbines", "Generators produce electricity"])
u.ex("a", "* Advanced. A remote island has strong winds, sunny days and no rivers. Recommend an energy mix and justify it.", [("wind turbines – strong winds", ["wind"]), ("solar panels – sunny days", ["solar|sun"]), ("storage / batteries for when no wind or sun", ["store|batter|backup|molten salt"]), ("no hydropower – no rivers", ["no river|hydro"])],
     "Use wind turbines for the strong winds and solar panels for sunny days, with batteries to store energy for calm nights. Hydropower is not possible because there are no rivers.", need=3)
u.mc("a", "Why is it useful to combine different renewable resources?", "When one is not available, another may be, giving a steadier supply.", ["They all stop at the same time.", "It uses more fossil fuels.", "It makes energy free forever."], skill="Reasoning")
u.mc("a", "A company advertises 'eco' bottles made of 5% plant material and 95% oil-based plastic. This may be…", "greenwashing", ["fully sustainable", "a fossil fuel", "geothermal"], skill="Reasoning")
u.gr("a", "* Advanced. Wind farm output against wind speed. Plot the points.", {"label": "Wind speed (m/s)", "min": 0, "max": 20, "step": 5}, {"label": "Output (MW)", "min": 0, "max": 60, "step": 10}, [[0, 0], [5, 10], [10, 35], [15, 55], [20, 55]])
u.stop("That makes them sustainable", "Renewable energy resources are…", "in constant supply or quickly replaced", ["used only once", "always underground", "fossil fuels"])
u.stop("after sunset or on a cloudy day", "Molten salt is used to…", "store the Sun's heat", ["make wind", "split uranium", "cool panels"])
u.stop("and turbines can be noisy", "Give one drawback of wind turbines.", "Blades can kill birds", ["They pollute the air", "They burn coal", "They need uranium"])
u.stop("which is called greenwashing", "Biomass is only renewable if it is…", "replaced as fast as it is used", ["burnt quickly", "kept underground", "mixed with coal"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Energy resources", "sec": None, "kids": [
    {"id": "nd", "t": "Energy needs", "d": "Homes • Transport • Industry • Data centres • Healthcare", "obj": "O1", "sec": "12.1"},
    {"id": "ff", "t": "Fossil fuels", "d": "Coal, oil, gas • Millions of years • Burn → steam → turbine → generator", "obj": "O2", "sec": "12.2"},
    {"id": "im", "t": "Impacts", "d": "CO2 – global warming • SO2 – acid rain • Fracking", "obj": "O2", "sec": "12.2"},
    {"id": "nu", "t": "Nuclear", "d": "Uranium fission • Chain reaction • Radioactive waste", "obj": "O2", "sec": "12.2"},
    {"id": "so", "t": "Solar and wind", "d": "PV panels • Solar thermal • Wind farms • Not constant", "obj": "O3", "sec": "12.3"},
    {"id": "hw", "t": "Water and Earth's heat", "d": "Dams, tides, waves • Geothermal – Iceland", "obj": "O3", "sec": "12.3"},
    {"id": "bm", "t": "Biomass", "d": "Wood, crops, waste • Biofuels • Replant to be renewable • Greenwashing", "obj": "O3", "sec": "12.3"},
]}
