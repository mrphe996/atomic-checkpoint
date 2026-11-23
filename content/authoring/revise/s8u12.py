# -*- coding: utf-8 -*-
"""Stage 8 Unit 12 Renewable and Non-Renewable Energy Resources — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-IPCCLCA", "name": "IPCC (2014) – Climate Change 2014: Mitigation of Climate Change, Annex III: Technology-specific cost and performance parameters (life-cycle emissions)", "url": "https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_annex-iii.pdf", "use": "Life-cycle CO₂ per kWh data scene and Challenge question (12.2)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

CO2 = {"kind": "barchart", "labels": ["coal", "natural gas", "solar PV", "nuclear", "wind"], "values": [820, 490, 48, 12, 11], "ymax": 900, "step": 150, "ylabel": "CO₂ per kWh over whole life (g)"}

NEW_STOPS = {
 "s8u12n11": dict(note="Paused after four places that need energy: home, transport, hospitals and data centres.",
   q=ex("s8u12n11_q", "H", "O1", "Explain why hospitals keep back-up generators.",
        [("they need a reliable / continuous supply of electricity", ["reliable|continuous|all the time|never|power cut|fails"]), ("life-support / medical machines must keep working", ["life|machine|patient|equipment|operation"])],
        "Hospitals need a reliable supply of electricity at all times. If the mains supply fails, back-up generators keep life-support and other medical machines working, so patients stay safe."),
   twin=mc("s8u12n11_t", "M", "O1", "Which is an energy resource?", "Wind", [("A light bulb", ""), ("A wire", ""), ("A switch", "")])),
 "s8u12n21": dict(note="Paused on the chart: coal 820, gas 490, solar 48, nuclear 12, wind 11 g of CO₂ per kWh.",
   q=ex("s8u12n21_q", "H", "O2", "Why do solar, wind and nuclear still release a little carbon dioxide, even though nothing is burnt to make the electricity?",
        [("energy/fuels are used to mine materials, make parts or build the power station", ["mining|mine|manufactur|making|build|construct|transport"]), ("this is counted over the whole life, not just while running", ["whole life|life ?cycle|not (when|while) (running|making)|over (its|the) life"])],
        "Fuels are burnt to mine the materials, manufacture the panels, turbines or fuel rods, transport them and build the power station. These emissions are counted over the whole life, even though no fuel is burnt while it makes electricity.", skill="Data"),
   twin=nm("s8u12n21_t", "M", "O2", "Use the chart. How many times more CO₂ per kWh does coal release than wind (to the nearest whole number)?", 75, "", tol=1, units=[""], fig=CO2)),
 "s8u12n31p": dict(note="Paused before a black can and a shiny can of water are left in sunshine.",
   q=mc("s8u12n31p_q", "M", "O3", "PREDICT: which water will warm up faster?", ("The water in the black can", "Good prediction – now watch."),
        [("The water in the shiny can", "Watch carefully."), ("Both the same", "Watch carefully."), ("Neither will warm up", "Watch carefully.")], skill="Prediction"),
   twin=mc("s8u12n31p_t", "M", "O3", "Solar energy is renewable because…", "the Sun will keep shining for billions of years", [("it is burnt", ""), ("it comes from fossils", ""), ("it can only be used once", "")])),
 "s8u12n31e": dict(note="Paused after 30 minutes: black can 38 °C, shiny can 26 °C.",
   q=ex("s8u12n31e_q", "H", "O3", "EXPLAIN the result and say why solar water heaters have black panels.",
        [("black surfaces absorb more energy from the Sun", ["absorb"]), ("shiny surfaces reflect it, so black panels heat water faster", ["reflect|faster|more heat|hotter"])],
        "The matt black can absorbs more of the Sun's energy, while the shiny can reflects much of it away. Solar water heaters have black panels so they absorb as much energy as possible and heat the water faster."),
   twin=nm("s8u12n31e_t", "M", "O3", "By how much did the water in the black can warm up (20 °C to 38 °C)?", 18, "°C", tol=0, units=["°C"])),
}

DROP = {"12.1": ["s8u12s1p07", "s8u12s1p01"], "12.2": ["s8u12s2p01", "s8u12s2p06", "s8u12s2p10"], "12.3": ["s8u12s3p02", "s8u12s3p04"]}

MIX = {"kind": "barchart", "labels": ["coal", "gas", "nuclear", "hydro", "wind", "solar"], "values": [36, 23, 9, 14, 8, 6], "ymax": 40, "step": 10, "ylabel": "Approximate share of world electricity, 2023 (%)"}
DAY = {"kind": "linegraph", "x": {"min": 0, "max": 24, "step": 4, "label": "Time of day (h)"}, "y": {"min": 0, "max": 5, "step": 1, "label": "Power from a home solar panel (kW)"},
       "series": [{"pts": [[0, 0], [6, 0], [8, 1], [10, 3], [12, 4], [14, 3.6], [16, 2], [18, 0.5], [20, 0], [24, 0]], "label": "sunny day"}]}
NEW_PRAC = {
 "12.1": [
  gd("s8u12s1p21", "M", "O1", "Which sector uses the energy?", ["Sector"],
     [("Heating a classroom", ["Buildings"]), ("Running a bus", ["Transport"]), ("Powering a factory robot", ["Industry"]), ("Pumping water to fields", ["Farming"])], extra=["Space"]),
  ex("s8u12s1p22", "H", "O1", "Suggest TWO reasons why the world uses more energy today than 50 years ago.",
     [("more people / population growth", ["people|population"]), ("more technology / devices / transport / industry", ["technology|device|phone|computer|car|transport|industry|factor"])],
     "The world population has grown, and people use far more technology, such as phones, computers, cars and air conditioning, which all need energy.", need=2),
 ],
 "12.2": [
  nm("s8u12s2p21", "M", "O2", "Use the chart. What percentage of the world's electricity comes from fossil fuels (coal + gas)?", 59, "%", tol=0, units=["%"], fig=MIX, skill="Data"),
  mc("s8u12s2p22", "H", "O2", "Use the CO₂ chart. A town switches its electricity from coal to gas. What happens to the CO₂ released per kWh?", "It falls by about 330 g, but gas still releases a lot", [("It falls to almost zero", "Gas is still a fossil fuel."), ("It goes up", "Gas releases less than coal."), ("It stays the same", "The values are different.")], fig=CO2, skill="Data"),
  ex("s8u12s2p23", "H", "O2", "Give ONE advantage and ONE disadvantage of nuclear power.",
     [("advantage: very little CO₂ / lots of energy from small fuel / reliable", ["little (co2|carbon)|low carbon|no co2|lots of energy|reliable|constant"]), ("disadvantage: radioactive waste / accident risk / mining damage", ["radioactive|waste|accident|chernobyl|mining|expensive"])],
     "Advantage: it releases very little carbon dioxide and gives a reliable supply. Disadvantage: it produces radioactive waste that must be stored safely for a very long time."),
 ],
 "12.3": [
  nm("s8u12s3p21", "M", "O3", "Use the graph. What is the maximum power from the solar panel?", 4, "kW", tol=0, units=["kW"], fig=DAY, skill="Data"),
  ex("s8u12s3p22", "H", "O3", "Use the graph. Explain why a home with solar panels still needs another source of electricity or a battery.",
     [("no power at night (before 6 h / after 20 h)", ["night|dark|evening|0 kW|no power"]), ("power varies / lower in morning and evening or on cloudy days, so storage or the grid is needed", ["vari|cloud|less|lower|battery|store|grid"])],
     "The panel gives no power at night, from about 8 pm to 6 am, and less power in the morning, evening or on cloudy days. The home needs a battery to store energy or electricity from the grid.", fig=DAY, skill="Data"),
 ],
}
NEW_ADV = {
 "12.2": [adv(ex("s8u12s2a05", "VH", "O2", "Use the IPCC life-cycle data (coal 820 g, gas 490 g, solar PV 48 g, nuclear 12 g, wind 11 g of CO₂ per kWh). A family uses 3000 kWh of electricity a year. Calculate how much less CO₂ they would be responsible for each year if their electricity came from wind instead of coal, and give one reason why a country cannot simply switch all of its electricity to wind overnight.",
     [("(820 − 11) × 3000 = 2 427 000 g ≈ 2.4 tonnes", ["2 ?427 ?000|2427000|2427 ?kg|2\\.4"]), ("wind is not constant / need storage or back-up", ["not constant|varies|intermittent|calm|storage|back-?up|battery"]), ("cost / land / time to build turbines and grid", ["cost|expensive|land|time to build|grid|space"])],
     "Saving = (820 − 11) × 3000 = 2 427 000 g, about 2.4 tonnes of CO₂ a year. A country cannot switch overnight because the wind is not constant, so storage or back-up power is needed, and building enough turbines and grid connections takes a lot of money, land and time.", need=2, src=src("SRC-IPCCLCA")))],
}

from tests_stage8_unit12_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
