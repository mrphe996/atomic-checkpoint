# -*- coding: utf-8 -*-
"""Stage 7 Unit 1 Introducing Science — 2026 revision (written by the Camday teaching team).
Practice: same-reasoning recall questions out; data, graph, apparatus and experiment questions in.
Challenge: one question per section adapted from an outside source (named under the question)."""
from c_kit import *
from c_base import scale

SOURCES = [
    {"id": "SRC-UNDSCI", "name": "Understanding Science (UC Museum of Paleontology) – The Science Checklist", "url": "https://undsci.berkeley.edu/for-educators/find-lessons-and-tools/understanding-science-infographics-and-tools/", "use": "Idea for the 'is it science?' checklist question (1.1)."},
    {"id": "SRC-SBVAR", "name": "Science Buddies – Variables in your science fair project", "url": "https://www.sciencebuddies.org/science-fair-projects/science-fair/variables", "use": "Idea for the variables table question (1.2)."},
    {"id": "SRC-HSEGHS", "name": "Health and Safety Executive – Hazard pictograms (symbols)", "url": "https://www.hse.gov.uk/chemical-classification/labelling-packaging/hazard-symbols-hazard-pictograms.htm", "use": "Idea for the label with two pictograms question (1.3)."},
    {"id": "SRC-NOAACO2", "name": "NOAA Global Monitoring Laboratory – Trends in atmospheric carbon dioxide", "url": "https://gml.noaa.gov/ccgg/trends/", "use": "Real Mauna Loa yearly averages used in the video and in 1.4 questions."},
]
S = {x["id"]: x for x in SOURCES}
src = lambda k: {"id": k, "name": S[k]["name"], "url": S[k]["url"]}

# ---------------------------------------------------------------- pause questions for the new video scenes
NEW_STOPS = {
 "u1n11": dict(note="Paused after four scientists at work: forecaster, engineer, medical researcher, chemist.",
   q=mc("u1n11_q", "M", "O1", "Which area of science studies why the Moon looks different each night?", ("Astronomy", "Yes – astronomy studies space, including the Moon and how it moves."),
        [("Meteorology", "Meteorology studies the weather, not the Moon."), ("Chemistry", "Chemistry studies what things are made of."), ("Biology", "Biology studies living things.")],
        hint="Which area studies planets, moons and stars?"),
   twin=mc("u1n11_t", "M", "O1", "A scientist tests which fertiliser makes tomato plants grow tallest. Which area is this mainly?", "Biology", [("Astronomy", ""), ("Meteorology", ""), ("Physics", "")])),
 "u1n12p": dict(note="Paused before the salt is added: beaker A plain ice, beaker B ice + salt.",
   q=mc("u1n12p_q", "M", "O3", "PREDICT: after 10 minutes, which beaker will contain more liquid water?", ("Beaker B, the ice with salt", "Good prediction – now watch to see if you are right."),
        [("Beaker A, the plain ice", "Watch what happens – salt changes how ice melts."), ("Both the same, because they are in the same room", "The room is the same, but one thing is different."), ("Neither – ice cannot melt in 10 minutes", "Ice in a warm room starts melting quickly.")],
        hint="Think about why salt is spread on icy roads in winter.", skill="Prediction"),
   twin=mc("u1n12p_t", "M", "O3", "In the salt-and-ice test, what was the independent variable?", "Whether salt was added", [("The size of the beaker", ""), ("The time", ""), ("How much ice melted", "")])),
 "u1n12e": dict(note="Paused after the result: salted ice melted much faster.",
   q=ex("u1n12e_q", "H", "O3", "EXPLAIN the result, and say why it was a fair test.",
        [("salt makes ice melt faster / lowers the freezing point", ["salt.*(faster|quick|lower)|freezing point|melt.*faster"]),
         ("only the salt was changed", ["only.*salt|salt.*only|one (thing|variable)|independent"]),
         ("other things kept the same (number of cubes, beaker, room, time)", ["same|control|kept"])],
        "Salt lowers the freezing point of water, so the salted ice melted faster. It was a fair test because only the salt was changed; the number of ice cubes, the beakers, the room and the time were kept the same.", need=2),
   twin=mc("u1n12e_t", "M", "O3", "Why is salt spread on icy roads?", "It makes the ice melt at a lower temperature", [("It makes the road warmer", ""), ("It stops rain", ""), ("It makes tyres grip less", "")])),
 "u1n13": dict(note="Paused after four lab risks: loose hair, drink at bench, test tube pointed at a friend, unlabelled bottle.",
   q=ms("u1n13_q", "M", "O5", "Select ALL the actions that make these risks safe.", ["Tie back long hair before lighting a Bunsen burner", "Point a heated test tube away from everyone", "Tell the teacher about a bottle with no label"],
        [("Smell the unlabelled bottle to find out what it is", "Never smell or taste an unknown substance."), ("Finish the drink quickly before starting the experiment", "Food and drink must not be in the lab at all.")]),
   twin=mc("u1n13_t", "M", "O5", "Why must food and drink stay out of the lab?", "Chemicals could get into them and be swallowed", [("They make the room too warm", ""), ("They are too expensive", ""), ("Teachers might be hungry", "")])),
 "u1n14": dict(note="Paused on the real carbon dioxide graph, 1960–2020.",
   q=nm("u1n14_q", "H", "O6", "PREDICT: use the graph trend to estimate carbon dioxide in the air in 2030 (parts per million). Give a whole number.", 435, "ppm", units=["ppm", "parts per million"], tol=12,
        hint="From 2010 to 2020 it rose by about 24 ppm. It is rising a little faster each decade.", reason="414 + about 20–25 = roughly 435–440 ppm (answers from about 423 to 447 are reasonable).", skill="Data"),
   twin=mc("u1n14_t", "M", "O6", "What is the main cause of the rise in carbon dioxide on the graph?", "Burning fossil fuels such as coal, oil and gas", [("More trees growing", ""), ("Volcanoes only", ""), ("The Moon's gravity", "")])),
}

# ---------------------------------------------------------------- Practice: same-reasoning recall out, data/graph/experiment in
DROP = {
 "1.1": ["u1s1p01", "u1s1p11", "u1s1p13", "u1s1p14"],   # area definitions and scientist recall already asked by p02, p10, p08
 "1.2": ["u1s2p05", "u1s2p16", "u1s2p14"],              # dependent-variable definition (p04), reliable (p10), attitude (p15 match)
 "1.3": ["u1s3p14", "u1s3p11", "u1s3p09"],              # three more 'symbol → meaning' recalls (p02, p03 remain)
 "1.4": ["u1s4p01", "u1s4p18", "u1s4p16"],              # ICT acronym, Dubai share trivia, food technology (p11 asks the same idea)
}
SURVEY = {"kind": "barchart", "labels": ["Physics", "Chemistry", "Biology", "Astronomy", "Weather"], "values": [32, 24, 46, 58, 20], "ymax": 60, "step": 10,
          "ylabel": "Number of pupils", "xlabel": "Favourite area of science"}
HEAT = {"kind": "linegraph", "x": {"min": 0, "max": 10, "step": 2, "label": "Heating time (min)"}, "y": {"min": 20, "max": 100, "step": 20, "label": "Temperature of water (°C)"},
        "series": [{"pts": [[0, 22], [2, 38], [4, 53], [6, 68], [8, 82], [10, 95]]}]}
CO2 = {"kind": "linegraph", "x": {"min": 1960, "max": 2020, "step": 10, "label": "Year"}, "y": {"min": 300, "max": 420, "step": 20, "label": "CO2 in air (parts per million)"},
       "series": [{"pts": [[1960, 317], [1970, 326], [1980, 339], [1990, 354], [2000, 370], [2010, 390], [2020, 414]]}]}
NEW_PRAC = {
 "1.1": [
  mc("u1s1p21", "M", "O1", "The bar chart shows the favourite area of science of 180 pupils. Which area was chosen by the most pupils?", "Astronomy",
     [("Biology", "Biology has 46 pupils; one bar is taller."), ("Physics", "Physics has 32 pupils."), ("Weather", "Weather has the shortest bar.")], fig=SURVEY, skill="Data", hint="Find the tallest bar."),
  nm("u1s1p22", "M", "O1", "Use the same bar chart. How many more pupils chose biology than chemistry?", 22, "pupils", units=["pupils", ""], fig=SURVEY, skill="Data",
     errs=[(70, "You added the two bars. 'How many more' means subtract.")], hint="Biology 46, chemistry 24.", reason="46 − 24 = 22."),
  ex("u1s1p23", "H", "O1", "Observation: on cold mornings, drops of water appear on the grass. Write one scientific question about it, and name the area of science that would study it.",
     [("a question that can be investigated (why/how/when does dew form …)", ["why|how|when|what|does|do"]), ("names meteorology (weather) or physics", ["meteorolog|weather|physics"])],
     "Why does water form on grass on cold mornings? This would be studied in meteorology (the weather) – it also uses physics.", need=2),
  gd("u1s1p24", "H", "O1", "Is each question one that science can answer by collecting evidence?", ["Yes", "No"],
     [("Does a plant grow taller with more light?", ["✓", "✗"]), ("Is red a more beautiful colour than blue?", ["✗", "✓"]), ("How long does ice take to melt at 25 °C?", ["✓", "✗"]), ("Should everyone like football?", ["✗", "✓"])],
     hint="Science answers questions about the natural world using evidence that can be measured or observed."),
 ],
 "1.2": [
  num("u1s2p21", "From the graph, what is the temperature of the water after 4 minutes of heating?", 53, "°C", "M", "O4", skill="Data", tol=2, units=["°C"], fig=HEAT,
      hint="Go up from 4 on the time axis to the line, then across.", reason="The line passes through about 53 °C at 4 minutes."),
  mc("u1s2p22", "H", "O3", "In the heating investigation shown in the graph, which is a control variable?", "The volume of water in the beaker",
     [("The heating time", "That is the independent variable – it is changed on purpose."), ("The temperature of the water", "That is the dependent variable – it is measured."), ("The number on the thermometer", "That is the reading of the dependent variable.")], fig=HEAT),
  tb("u1s2p23", "H", "O4", "A student times how long sugar takes to dissolve, three times at each temperature. Complete the mean column (to 1 decimal place).", ["Water temperature (°C)", "Trial 1 (s)", "Trial 2 (s)", "Trial 3 (s)", "Mean (s)"],
     [["20", "92", "88", "90", {"ans": 90.0, "tol": 0.1}], ["40", "61", "59", "63", {"ans": 61.0, "tol": 0.1}], ["60", "34", "37", "34", {"ans": 35.0, "tol": 0.1}]],
     hint="Add the three trials and divide by 3."),
  gd("u1s2p24", "H", "O3", "A pendulum investigation: does the length of the string change how long one swing takes? Classify each variable.", ["Variable type"],
     [("Length of the string", ["Independent"]), ("Time for one swing", ["Dependent"]), ("Mass of the bob", ["Control"]), ("How far the bob is pulled back", ["Control"])], extra=[]),
  gr("u1s2p25", "H", "O4", "Plot the results: how far a toy car rolls (cm) for different ramp heights.", {"label": "Ramp height (cm)", "min": 0, "max": 50, "step": 10},
     {"label": "Distance rolled (cm)", "min": 0, "max": 200, "step": 40}, [[10, 38], [20, 77], [30, 118], [40, 152], [50, 190]],
     follow=mc("u1s2p25f", "H", "O4", "What does the graph show?", "The higher the ramp, the further the car rolls", [("The car always rolls the same distance", ""), ("Higher ramps make the car roll less far", ""), ("There is no pattern", "")])),
 ],
 "1.3": [
  scale("u1s3p21", "Read the volume of water in the measuring cylinder. Read from the bottom of the meniscus.", {"kind": "cylinder", "min": 0, "max": 50, "major": 10, "minor": 2, "value": 26, "unit": "cm³"},
        26, "cm³", "M", "O5", tol=0.5, units=["cm³", "cm3", "ml", "mL"], hint="Each small mark is 2 cm³."),
  gd("u1s3p22", "M", "O5", "Is each action safe or unsafe in the laboratory?", ["Safe", "Unsafe"],
     [("Wearing goggles while heating", ["✓", "✗"]), ("Pouring leftover chemicals down the sink", ["✗", "✓"]), ("Reporting a broken beaker straight away", ["✓", "✗"]), ("Running between benches", ["✗", "✓"]), ("Smelling a gas by sniffing straight from the tube", ["✗", "✓"])]),
  mc("u1s3p23", "H", "O5", "A student needs exactly 18 cm³ of water. Which apparatus gives the most accurate measurement?", "A 25 cm³ measuring cylinder with 0.5 cm³ marks",
     [("A 250 cm³ beaker", "Beaker marks are far apart and only approximate."), ("A 100 cm³ measuring cylinder with 2 cm³ marks", "It would work, but each mark is 2 cm³ – less accurate."), ("A 500 cm³ conical flask", "Flasks are for holding and mixing, not measuring.")],
     skill="Measurement", hint="Choose the smallest measuring cylinder that holds the volume, with the closest marks."),
 ],
 "1.4": [
  num("u1s4p21", "Use the graph of carbon dioxide in the air. By how many parts per million did it rise from 1960 to 2020?", 97, "ppm", "M", "O6", skill="Data", tol=3, units=["ppm", "parts per million"], fig=CO2,
      hint="Read 1960 and 2020 from the graph, then subtract.", reason="About 414 − 317 = 97 ppm."),
  mc("u1s4p22", "H", "O6", "Use the graph. In which 10 years did carbon dioxide rise the most?", "2010–2020",
     [("1960–1970", "That is the smallest rise (about 9 ppm)."), ("1980–1990", "About 15 ppm – a later decade rose more."), ("1990–2000", "About 16 ppm – a later decade rose more.")], fig=CO2, skill="Data", hint="Look for the steepest part of the line."),
  mc("u1s4p23", "H", "O6", "Three sources write about a new energy drink. Which is LEAST likely to be biased?", "A study by a university, checked by other scientists (peer reviewed)",
     [("An advert by the company that makes the drink", "The company wants to sell it, so it may tell only one side."), ("A post by a famous athlete who is paid by the company", "Being paid gives a reason to tell only one side."), ("A comment on a fan page with no name", "We cannot check who wrote it or what evidence they used.")]),
 ],
}

# ---------------------------------------------------------------- Challenge: ideas adapted from outside sources
NEW_ADV = {
 "1.1": [adv(gd("u1s1a5", "VH", "O1", "A science checklist asks: does it focus on the natural world, use testable ideas, rely on evidence, and get checked by others? Decide whether each activity passes the checklist.", ["Passes", "Does not pass"],
     [("Measuring how fast ice melts at different temperatures and sharing the results", ["✓", "✗"]), ("Reading a horoscope to predict next week", ["✗", "✓"]), ("Counting birds in a park every month for a year", ["✓", "✗"]), ("Choosing the best painting in a competition", ["✗", "✓"])],
     src={"id": "SRC-UNDSCI", "name": S["SRC-UNDSCI"]["name"], "url": S["SRC-UNDSCI"]["url"]}))],
 "1.2": [adv(tb("u1s2a5", "VH", "O3", "Plan the variables for this question: 'Does the temperature of water change how quickly a sugar cube dissolves?' Complete the table with ONE answer per box: independent, dependent, or control.", ["Thing in the investigation", "Type of variable"],
     [["Temperature of the water", {"ans": "independent"}], ["Time for the sugar cube to dissolve", {"ans": "dependent"}], ["Volume of water", {"ans": "control"}], ["Size of the sugar cube", {"ans": "control"}]],
     src=src("SRC-SBVAR")))],
 "1.3": [adv(ex("u1s3a5", "VH", "O5", "A bottle of oven cleaner shows two hazard pictograms: corrosive and moderate hazard (exclamation mark). Explain what each warns about and give one precaution for each.",
     [("corrosive: damages / burns skin, eyes or materials", ["burn|destroy|damage|eat|dissolv"]), ("precaution for corrosive: gloves / goggles", ["glove|goggle|eye protect"]),
      ("moderate hazard: irritates or harms if touched, breathed or swallowed", ["irritat|harm|cough|rash|breath|swallow"]), ("precaution: use in a ventilated place / avoid breathing it / wash hands", ["ventilat|window|fresh air|wash|don.?t breathe|avoid breath|mask"])],
     "Corrosive means it can burn and destroy skin, eyes and other materials, so wear gloves and goggles. The exclamation mark means it can irritate or harm you if it touches skin or is breathed in, so use it with a window open and wash your hands afterwards.", need=3,
     src=src("SRC-HSEGHS")))],
 "1.4": [adv(ex("u1s4a5", "VH", "O6", "Between 1960 and 2020, carbon dioxide measured at Mauna Loa rose from about 317 to about 414 parts per million, and each decade it rose faster than the one before. Describe the trend and suggest TWO ways science and technology could slow it down.",
     [("rising / increasing", ["ris|increas|went up|goes up|higher"]), ("rising faster / steeper over time", ["faster|steeper|accelerat|more each|quicker"]),
      ("solar / wind / renewable electricity", ["solar|wind|renewable|hydro"]), ("electric vehicles / use less fuel / plant trees / efficiency", ["electric car|electric vehicle|less fuel|tree|efficien|insulat|public transport|bike"])],
     "Carbon dioxide has risen every decade and it is rising faster and faster. Solar panels and wind turbines can make electricity without burning fossil fuels, and electric vehicles or better public transport can cut the fuel we burn.", need=3,
     src=src("SRC-NOAACO2")))],
}

# ---------------------------------------------------------------- Unit Tests (keys in content/private)
from tests_stage7_unit01_v2 import TEST_A, TEST_B
TESTS = (TEST_A, TEST_B)
