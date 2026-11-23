# -*- coding: utf-8 -*-
"""Stage 9 Unit 13 Earth and Climate Change — 2026 revision (written by the Atomic teaching team)."""
from c_kit import *

SOURCES = [
    {"id": "SRC-NASATEMP", "name": "NASA – Global Temperature (Earth indicator, GISTEMP)", "url": "https://climate.nasa.gov/vital-signs/global-temperature", "use": "Global temperature anomalies 1880–2024 for the video graph and the Challenge question (13.4)."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

GT = {"kind": "linegraph", "x": {"min": 1880, "max": 2030, "step": 30, "label": "Year"}, "y": {"min": -0.4, "max": 1.6, "step": 0.4, "label": "Difference from 1951–1980 average (°C)"},
      "series": [{"pts": [[1880, -0.17], [1900, -0.08], [1920, -0.27], [1940, 0.12], [1960, -0.03], [1980, 0.26], [2000, 0.39], [2020, 1.01], [2024, 1.28]], "label": "NASA GISTEMP"}]}

NEW_STOPS = {
 "s9u13n11p": dict(note="Paused before water with a purple crystal is heated under one side.",
   q=mc("s9u13n11p_q", "M", "O1", "PREDICT: where will the purple colour go?", ("Up above the flame, across the top and down the other side", "Good prediction – now watch."),
        [("It will stay at the bottom", "Watch carefully."), ("Straight down", "Watch carefully."), ("It will spread evenly at once", "Watch carefully.")], skill="Prediction"),
   twin=mc("s9u13n11p_t", "M", "O1", "Heated water rises because it…", "expands and becomes less dense", [("becomes heavier", ""), ("gains particles", ""), ("becomes denser", "")])),
 "s9u13n11e": dict(note="Paused after the purple colour moved round in a loop.",
   q=ex("s9u13n11e_q", "H", "O1", "EXPLAIN the loop and link it to tectonic plates.",
        [("heated water expands, is less dense and rises; it cools at the top, becomes denser and sinks: a convection current", ["less dense|rises|sinks|convection"]), ("the mantle moves in convection currents that drag the plates", ["mantle|plate|drag|carr"])],
        "The water above the flame expands, becomes less dense and rises; at the top it cools, becomes denser and sinks, making a convection current. Hot rock in the mantle moves in slow convection currents in the same way, dragging the tectonic plates."),
   twin=mc("s9u13n11e_t", "M", "O1", "What powers the convection currents in Earth's mantle?", "Heat from Earth's hot interior", [("The Moon's gravity", ""), ("Wind", ""), ("Ocean tides", "")])),
 "s9u13n41": dict(note="Paused on NASA's graph: −0.17 °C in 1880, 0.26 °C in 1980, 1.28 °C in 2024.",
   q=ex("s9u13n41_q", "H", "O4", "How has the rate of warming changed since 1980, and what is the main cause?",
        [("warming has become much faster since 1980 (0.26 °C to 1.28 °C)", ["faster|steeper|accelerat|1\\.28|0\\.26|1 ?°c"]), ("caused by more greenhouse gases from human activity, e.g. burning fossil fuels", ["greenhouse|carbon dioxide|fossil|human"])],
        "Since 1980 the temperature has risen much faster, from about 0.26 °C to 1.28 °C above the 1951–1980 average by 2024. The main cause is the extra greenhouse gases, especially carbon dioxide, released by human activities such as burning fossil fuels.", skill="Data"),
   twin=nm("s9u13n41_t", "M", "O4", "Use the graph. By how much did the value rise from 1980 to 2024?", 1.02, "°C", tol=0.02, units=["°C"], fig=GT)),
}

DROP = {"13.1": ["s9u13s1p03", "s9u13s1p04"], "13.2": ["s9u13s2p01", "s9u13s2p02"], "13.3": ["s9u13s3p01", "s9u13s3p05"], "13.4": ["s9u13s4p01", "s9u13s4p04"]}

STORE = {"kind": "barchart", "labels": ["atmosphere", "plants and soils", "fossil fuels", "oceans"], "values": [880, 2500, 1000, 38000], "ymax": 40000, "step": 10000, "ylabel": "Carbon stored (billion tonnes, approx.)"}
NEW_PRAC = {
 "13.1": [
  gd("s9u13s1p21", "M", "O1", "What forms where plates…", ["Feature"],
     [("push together", ["Fold mountains"]), ("slide past each other", ["Earthquakes"]), ("pull apart", ["Volcanoes and new crust"])], extra=["Rivers"]),
 ],
 "13.2": [
  nm("s9u13s2p21", "H", "O2", "The Atlantic widens by about 2.5 cm a year. How many metres wider will it be in 1000 years?", 25, "m", tol=0, units=["m"]),
  ex("s9u13s2p22", "H", "O2", "Explain why fossils of the same land reptile in Africa and South America support the idea of moving plates.",
     [("the reptile could not swim across an ocean", ["could not swim|couldn't swim|cannot swim|ocean"]), ("so the continents must once have been joined, then moved apart", ["joined|together|moved apart|split"])],
     "A small land or freshwater reptile could not have swum across the Atlantic Ocean. Finding the same fossils on both continents suggests they were once joined and have since moved apart."),
 ],
 "13.3": [
  mc("s9u13s3p21", "M", "O3", "Use the chart. Which is the largest carbon store?", "Oceans", [("Atmosphere", "880 is much smaller."), ("Fossil fuels", "1000."), ("Plants and soils", "2500.")], fig=STORE, skill="Data"),
  od("s9u13s3p22", "H", "O3", "Order the path of a carbon atom from the air to a decomposer.", ["carbon dioxide in the air", "glucose in a leaf (photosynthesis)", "body of a rabbit (feeding)", "rabbit dies; decomposers feed", "carbon dioxide released (respiration)"]),
 ],
 "13.4": [
  nm("s9u13s4p21", "M", "O4", "Use the NASA graph. What was the value in 2020?", 1.01, "°C", tol=0.02, units=["°C"], fig=GT, skill="Data"),
  ex("s9u13s4p22", "H", "O4", "Give TWO reasons why sea level rises as the climate warms.",
     [("warmer sea water expands", ["expand"]), ("ice sheets and glaciers on land melt, adding water", ["melt|ice|glacier"])],
     "Warmer sea water expands, taking up more volume, and ice sheets and glaciers on land melt, adding extra water to the oceans."),
 ],
}
NEW_ADV = {
 "13.4": [adv(ex("s9u13s4a05", "VH", "O4", "NASA reports that 2024 was 1.28 °C warmer than the 1951–1980 average, and that the 10 most recent years were the 10 warmest on record. Explain why scientists compare each year with a 30-year average rather than with the year before, and suggest TWO ways people can reduce future warming.",
     [("one year can be unusually hot or cold (weather / natural variation); a 30-year average shows the long-term trend", ["variation|weather|one year|long-term|trend|average"]), ("reduce burning of fossil fuels / use renewable energy", ["renewable|solar|wind|fossil|less (coal|oil|gas)"]), ("plant trees / protect forests / use less energy / transport choices", ["plant|tree|forest|insulat|less energy|public transport|walk|cycle"])],
     "Single years vary because of weather and natural events, so comparing with the year before could be misleading. A 30-year average smooths this out and shows the long-term trend. People can reduce future warming by switching from fossil fuels to renewable energy and by protecting forests and planting trees (or by using less energy and choosing low-carbon transport).", need=2, src=src("SRC-NASATEMP")))],
}

from tests_stage9_unit13_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
