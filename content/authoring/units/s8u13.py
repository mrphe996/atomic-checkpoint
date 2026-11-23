# -*- coding: utf-8 -*-
"""Stage 8 Unit 13 – Weather and Climate. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Earth and Space"
BLURB = "The difference between weather and climate, climate zones and what affects them, ice ages and warm periods, and how the greenhouse effect drives climate change."
OBJECTIVES = {
    "O1": {"sec": "13.1", "code": "8ESc.03, 8TWSc.02", "codeNote": "", "t": "Distinguish weather from climate and describe how weather is measured and forecast."},
    "O2": {"sec": "13.1", "code": "8ESc.03", "codeNote": "climate zones", "t": "Describe climate zones and how latitude, altitude, relief and water mass affect climate."},
    "O3": {"sec": "13.2", "code": "8ESc.01", "codeNote": "", "t": "Describe the long-term cycle of ice ages and warm periods and the evidence for it."},
    "O4": {"sec": "13.2", "code": "8ESc.02, 8SIC.05", "codeNote": "", "t": "Explain how changes in the atmosphere, including greenhouse gases, change Earth's climate."},
}
SECTIONS = [
    {"id": "13.1", "title": "Climate and weather", "objs": ["O1", "O2"]},
    {"id": "13.2", "title": "Earth's climate cycles and climate change", "objs": ["O3", "O4"]},
]
u = Unit(8, 13)

# ---------------------------------------------------------------- 13.1
u.sec("13.1", "O1")
u.gd("r", "Weather or climate?", "Type", [("It rained heavily this morning", "Weather"), ("The region has hot, wet summers every year", "Climate"), ("Strong winds are forecast for tomorrow", "Weather"), ("Average January temperature over 30 years", "Climate")])
u.mt("r", "Match the instrument to what it measures.", [("Thermometer", "temperature"), ("Rain gauge", "rainfall"), ("Anemometer", "wind speed"), ("Hygrometer", "humidity")])
u.tb("r", "Average monthly rainfall over 30 years. Complete the table.", ["Month", "Total over 30 years (mm)", "Average per year (mm)"], [["January", "2400", B(80)], ["July", "600", B(20)]], o="O2")
u.ex("r", "Explain why places near the equator are hotter than places near the poles.", [("Earth is a sphere / curved", ["sphere|curved|round"]), ("rays hit head-on / concentrated near equator", ["head-on|direct|concentrat"]), ("spread over larger area near poles – less heating", ["spread|larger area|less"])],
     "Earth is a sphere, so near the equator the Sun's rays hit almost head-on and are concentrated on a small area. Near the poles the same rays are spread over a larger area, so the ground heats up less.", o="O2")
u.mc("r", "Climate is…", "the usual weather pattern of a region over several decades", [("the weather today", "That is weather."), ("only rainfall", "No."), ("the temperature this week", "No.")])
u.mc("r", "Which is NOT one of the four main factors that affect climate?", "The colour of the soil", ["Latitude", "Altitude", "Water mass"], o="O2", d="H")
u.mc("r", "Why is Death Valley so hot?", "It is below sea level and mountains trap rising hot air", [("It is near the poles", "No."), ("It is high in the mountains", "No."), ("It is by the sea", "No.")], o="O2", d="H")
u.mc("r", "A very hot day during the cold season is an example of…", "weather, not climate", [("climate change proved", "One day is not climate."), ("a climate zone", "No."), ("an ice age", "No.")], d="VH")
for p, r, w, o in [
    ("Weather is…", "the temporary state of the atmosphere in an area", ["the average over decades", "the shape of the land", "the Earth's orbit"], "O1"),
    ("Precipitation includes…", "rain, snow, sleet and hail", ["only fog", "only wind", "sunshine"], "O1"),
    ("People who study and forecast weather are…", "meteorologists", ["geologists", "biologists", "astronomers"], "O1"),
    ("A wind vane shows…", "wind direction", ["wind speed", "rainfall", "temperature"], "O1"),
    ("Weather data is collected by…", "satellites, weather stations, balloons and buoys", ["only thermometers at home", "magnets", "microscopes"], "O1"),
    ("Climate is based on averages taken over…", "several decades", ["one day", "one week", "one month"], "O1"),
    ("Climate zones are arranged in bands depending on…", "distance from the equator", ["distance from the Moon", "population", "time of day"], "O2"),
    ("Equatorial regions are…", "warm all year with lots of rain", ["freezing", "dry and cold", "covered in snow"], "O2"),
    ("Temperate regions have…", "four seasons", ["one season", "no rain", "snow all year"], "O2"),
    ("Polar regions are…", "freezing, with snow that never melts", ["hot and wet", "tropical", "desert-hot"], "O2"),
    ("Latitude means…", "how far a place is from the equator", ["how high it is", "how flat it is", "how near the sea it is"], "O2"),
    ("Altitude means…", "how high a place is", ["how far from the equator", "how rainy", "how windy"], "O2"),
    ("Relief describes…", "how flat or mountainous a place is", ["the temperature", "the latitude", "the rainfall"], "O2"),
    ("Places near a large body of water often have…", "milder climates", ["no weather", "more earthquakes", "no seasons"], "O2"),
    ("The hottest temperature ever measured was about…", "56.7 °C", ["100 °C", "30 °C", "−56.7 °C"], "O2"),
]:
    u.mc("p", p, r, w, o=o)
u.od("p", "Order the climate zones from the equator to the pole.", ["Equatorial", "Tropical", "Temperate", "Polar"], o="O2")
u.gd("p", "Which factor affecting climate does each describe?", "Factor", [("A town high in the mountains", "Altitude"), ("A city near the equator", "Latitude"), ("A village by the ocean", "Water mass")], o="O2", extra=["Relief"])
u.ms("p", "Select ALL the weather measurements.", ["Temperature", "Wind speed", "Rainfall"], ["Population", "Latitude"])
u.ex("a", "* Advanced. Two cities are at the same latitude, but one is on the coast and one is far inland. Predict how their climates differ and explain why.", [("coastal city milder / smaller range", ["milder|smaller range|less extreme"]), ("inland city hotter summers / colder winters", ["hotter summer|colder winter|more extreme"]), ("water heats and cools slowly", ["water.*(slow|heat|cool)"])],
     "The coastal city has a milder climate with a smaller temperature range, while the inland city has hotter summers and colder winters, because large bodies of water heat up and cool down slowly.", o="O2")
u.nm("a", "Temperature falls by about 6.5 °C for every 1000 m of altitude. A town at sea level is 25 °C. What is the temperature on a mountain 2000 m high nearby?", 12, "°C", o="O2")
u.mc("a", "Why do meteorologists use satellites as well as weather stations?", "Satellites see large areas, including oceans where there are few stations.", ["Satellites measure soil type.", "Weather stations are in space.", "Satellites change the weather."], skill="Reasoning")
u.mc("a", "Why must climate be based on decades of data, not one year?", "One year could be unusual; long-term averages show the real pattern.", ["One year is too long.", "Climate changes every day.", "Data older than a year is lost."], skill="Reasoning")
u.stop("It can change from day to day", "Weather can change…", "from day to day", ["only every 30 years", "never", "only at the equator"])
u.stop("an anemometer for wind speed", "An anemometer measures…", "wind speed", ["rainfall", "humidity", "temperature"])
u.stop("so the ground heats up less", "The further from the equator, the climate is…", "cooler", ["hotter", "wetter always", "the same"], o="O2")
u.stop("trap the hot air rising from the valley", "Which is a factor that affects climate?", "Altitude", ["Population", "Soil colour", "Time of day"], o="O2")

# ---------------------------------------------------------------- 13.2
u.sec("13.2", "O3")
u.gd("r", "Glacial or interglacial period?", "Period", [("Glaciers spread and sea levels fall", "Glacial"), ("Ice melts and sea levels rise", "Interglacial"), ("Climate drier and colder", "Glacial")])
u.gd("r", "Which is evidence for past climates?", "Evidence", [("Rocks carried far from home by ice", "Glacial erratics"), ("Piles of rock left by melting glaciers", "Moraines"), ("Layers of ancient ice", "Ice cores"), ("Growth rings in old trees", "Tree rings")])
u.mc("r", "Greenhouse gases keep Earth warm by…", "trapping heat that would otherwise escape to space", [("making the Sun hotter", "No."), ("blocking all sunlight", "No."), ("reflecting heat away", "No.")], o="O4")
u.ex("r", "Explain how human activities have increased global warming since the industrial revolution.", [("burning fossil fuels releases CO2", ["fossil|burn|carbon dioxide|co2"]), ("deforestation – fewer trees absorb CO2", ["forest|tree"]), ("more greenhouse gases trap more heat", ["trap|more heat|greenhouse"])],
     "Burning fossil fuels releases carbon dioxide, cutting down forests means less is absorbed, and farm animals release methane. More greenhouse gases trap more heat, so Earth warms.", o="O4")
u.tb("r", "Average global temperature has cycled between about 4.5 °C and 12 °C. Complete the table.", ["Lowest (°C)", "Highest (°C)", "Range (°C)"], [["4.5", "12", B(7.5)]])
u.mc("r", "How many major ice ages has Earth had, including the present one?", "Five", ["One", "Two", "Twenty"], d="H")
u.mc("r", "Earth's early atmosphere was mostly…", "carbon dioxide from volcanoes", ["oxygen", "nitrogen only", "methane only"], o="O4", d="H")
u.mc("r", "Why did oxygen in the atmosphere increase over time?", "Photosynthesis used carbon dioxide and released oxygen", [("Volcanoes made oxygen", "No."), ("Oceans released oxygen", "No."), ("Ice cores trapped carbon dioxide", "Not the main reason.")], o="O4", d="VH")
for p, r, w, o in [
    ("Cold periods in Earth's history are called…", "ice ages", ["heatwaves", "interglacials", "droughts"], "O3"),
    ("We are currently in the…", "fifth ice age", ["first ice age", "tenth ice age", "no ice age"], "O3"),
    ("During a glacial, sea levels…", "fall", ["rise", "stay the same", "disappear"], "O3"),
    ("During an interglacial, ice…", "melts", ["spreads", "stays the same", "turns to rock"], "O3"),
    ("Glacials and interglacials can each last…", "tens of thousands of years", ["a few days", "one year", "a century only"], "O3"),
    ("Ocean sediments contain…", "microfossils", ["glaciers", "tree rings", "volcanoes"], "O3"),
    ("Twenty thousand years ago ice covered about…", "a quarter of the Earth", ["all of the Earth", "none of the Earth", "half of the oceans"], "O3"),
    ("Ice cores show that Earth has…", "warmed and cooled naturally", ["always been the same", "never had ice", "no atmosphere"], "O3"),
    ("Which gas is a greenhouse gas?", "Methane", ["Oxygen", "Nitrogen", "Argon"], "O4"),
    ("Farm animals release…", "methane", ["oxygen", "nitrogen", "helium"], "O4"),
    ("Global warming can cause…", "melting ice, floods and droughts", ["more ice ages", "colder summers everywhere", "no change"], "O4"),
    ("Long-term changes in climate are called…", "climate change", ["weather", "a forecast", "relief"], "O4"),
    ("A greenhouse traps the Sun's heat to keep…", "plants warm", ["animals cold", "water frozen", "the Sun cool"], "O4"),
    ("Without any greenhouse gases, Earth would be…", "too cold for most life", ["hotter", "the same", "covered in forests"], "O4"),
    ("Reducing greenhouse gas emissions can…", "help limit the effects of climate change", ["stop all weather", "cause an ice age at once", "increase global warming"], "O4"),
]:
    u.mc("p", p, r, w, o=o)
u.ms("p", "Select ALL the human activities that increase greenhouse gases.", ["Burning fossil fuels", "Cutting down forests", "Keeping large herds of cattle"], ["Planting trees", "Using solar panels"], o="O4")
u.od("p", "Order the events in Earth's atmosphere.", ["Volcanoes release mostly carbon dioxide", "Carbon dioxide dissolves in oceans", "Photosynthesis begins", "Oxygen increases"], o="O4")
u.mt("p", "Match the evidence to what it is.", [("Glacial erratic", "rock moved far by ice"), ("Moraine", "pile of rock left by a glacier"), ("Ice core", "column of ancient ice")])
u.ex("a", "* Advanced. Explain how scientists can use ice cores to learn about past climates.", [("ice layers build up each year", ["layer|each year|annual"]), ("trapped air bubbles show past atmosphere / CO2", ["bubble|air|carbon dioxide|gas"]), ("deeper ice is older", ["deeper|older"])],
     "Snow builds up in layers each year and turns to ice, so deeper ice is older. Air bubbles trapped in the ice show what the atmosphere and its carbon dioxide level were like when that layer formed.")
u.gr("a", "* Advanced. Carbon dioxide in the atmosphere (parts per million). Plot the points.", {"label": "Year", "min": 1800, "max": 2020, "step": 40}, {"label": "CO2 (ppm)", "min": 250, "max": 450, "step": 50}, [[1800, 280], [1900, 296], [1960, 317], [2000, 370], [2020, 412]])
u.mc("a", "What does the CO2 graph show since 1960?", "Carbon dioxide has risen faster and faster.", ["It has fallen.", "It has stayed the same.", "It has risen more slowly."], o="O4", skill="Data")
u.mc("a", "Why is today's warming of concern even though Earth's climate has always changed?", "It is happening much faster, and human activity is the cause.", ["It is slower than ever.", "It is natural only.", "It will cause an ice age tomorrow."], o="O4", skill="Reasoning")
u.stop("and we're in the fifth", "Cold periods in Earth's history are called…", "ice ages", ["heatwaves", "seasons", "interglacials"])
u.stop("all record past climates", "Rocks carried far from home by glaciers are…", "glacial erratics", ["moraines", "ice cores", "tree rings"])
u.stop("keeping Earth warm enough for life", "Greenhouse gases keep Earth warm by…", "trapping heat", ["blocking sunlight", "making oxygen", "reflecting all heat away"], o="O4")
u.stop("causing melting ice, floods and droughts", "Global warming is caused by…", "more greenhouse gases trapping more heat", ["less sunlight", "fewer volcanoes", "more ice"], o="O4")

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Weather and climate", "sec": None, "kids": [
    {"id": "we", "t": "Weather", "d": "Day to day • Temperature, wind, cloud, precipitation • Instruments", "obj": "O1", "sec": "13.1"},
    {"id": "cl", "t": "Climate", "d": "Averages over decades • Climate zones from equator to poles", "obj": "O2", "sec": "13.1"},
    {"id": "fa", "t": "Factors", "d": "Latitude • Altitude • Relief • Water mass", "obj": "O2", "sec": "13.1"},
    {"id": "ia", "t": "Ice ages", "d": "Five major ice ages • Glacials and interglacials", "obj": "O3", "sec": "13.2"},
    {"id": "ev", "t": "Evidence", "d": "Erratics • Moraines • Ice cores • Sediments • Tree rings", "obj": "O3", "sec": "13.2"},
    {"id": "gh", "t": "Greenhouse effect", "d": "CO2 and methane trap heat • Fossil fuels, deforestation • Global warming", "obj": "O4", "sec": "13.2"},
]}
