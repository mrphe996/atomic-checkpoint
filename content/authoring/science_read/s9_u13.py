# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 13 Earth and Climate Change – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9ESp.01, 9ESp.02, 9ESc.01, 9ESc.02, 9SIC.02, 9SIC.05)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}

# =====================================================================================================
# 13.1 Movement of tectonic plates · 9ESp.01
# =====================================================================================================
READ["13.1"] = L(
    H("Mountains from the sea",
      "Fossil seashells are found near the top of the Himalayas, more than 8 km above sea level.",
      "How could rock from the sea floor end up on top of the world's highest mountains?"),
    I("Predict, watch, explain: a convection current in water",
      "A purple crystal sits at the bottom of a beaker of water, at one side. That side is heated gently.",
      fig={"kind": "sciConvection"},
      then=["A purple stream rises above the flame, moves across the top, sinks down the far side and flows back along the bottom – a loop.",
            "Heated water expands, becomes less dense and rises; at the top it cools, becomes denser and sinks: a **convection current**."]),
    I("Moving tectonic plates",
      "Earth's crust is broken into huge rigid **tectonic plates**. Below them, hot rock in the **mantle** moves very slowly in convection currents, dragging the plates along – a few centimetres a year.",
      fig={"kind": "plates", "boundary": "convergent"}),
    I("What happens at plate boundaries",
      "Most mountains, volcanoes and earthquakes are found where plates meet.",
      table=[["Plates…", "Result"], ["push together", "rocks crumple upwards into **fold mountains** (the Himalayas); one plate may slide under the other, forming volcanoes"],
             ["pull apart", "magma rises to fill the gap – **volcanoes** and new crust (Iceland)"], ["slide past each other", "they stick, then suddenly slip – **earthquakes** (California)"]]),
    Y("Boundaries",
      grid("s9u13r11", "What is mainly formed at each plate boundary?", ["Fold mountains", "New crust and volcanoes", "Earthquakes"],
           [("plates push together", "Fold mountains"), ("plates pull apart", "New crust and volcanoes"), ("plates slide past each other", "Earthquakes")],
           "Push, pull or slide?", "Push → fold mountains; pull apart → magma rises; slide → earthquakes.")),
    K("Key points",
      "The crust is made of **tectonic plates**.",
      "**Convection currents** in the mantle move the plates.",
      "Plate boundaries form fold mountains, volcanoes and earthquakes."),
    book=BK(
        [("tectonic plate", "a huge rigid piece of Earth's crust"), ("mantle", "the hot, slowly moving layer under the crust"), ("convection current", "a loop of rising warm and sinking cool fluid"),
         ("fold mountain", "a mountain formed where plates push together")],
        [], [],
        [Ex("Explain how convection currents in the mantle move tectonic plates.", ans="Hot rock rises, spreads under the crust, cools and sinks; this slow loop drags the plates along."),
         Ex("What happens where two plates push together?", ans="Rocks fold upwards into mountains; one plate can sink under the other, forming volcanoes."),
         Ex("Back to 'Start here': explain the seashells on the Himalayas.", ans="Two plates pushed together and folded sea-floor rocks upwards into mountains.", think=True)],
        ["explain how convection currents move plates", "describe what happens at plate boundaries"],
        look=["the convection current", "plate boundaries table"],
        note="Read it after the video: convection in the mantle and plate boundaries (answers at the back)."),
)

# =====================================================================================================
# 13.2 Evidence for tectonic plates · 9ESp.02, 9SIC.02
# =====================================================================================================
READ["13.2"] = L(
    H("A giant jigsaw",
      "Look at a world map: the east coast of South America seems to fit into the west coast of Africa.",
      "Is that just a coincidence?"),
    I("Pangaea",
      "In 1912 Alfred Wegener suggested that all the continents were once joined in one supercontinent, **Pangaea**, which slowly broke apart – **continental drift**.",
      then=["Many scientists rejected it at first because he could not explain **what** moved the continents. Later evidence – and the idea of mantle convection – showed he was right. Scientific ideas change as new evidence appears."]),
    I("Evidence for moving plates",
      "Four pieces of evidence:",
      table=[["Evidence", "What it shows"], ["**fitting coastlines**", "South America and Africa fit together like jigsaw pieces"],
             ["**matching fossils**", "fossils of the same freshwater reptile in South America and Africa – it could not have swum an ocean"],
             ["**volcanoes and earthquakes**", "they lie mainly along plate boundaries, such as the Pacific Ring of Fire"],
             ["**magnetic stripes**", "rocks on each side of the Mid-Atlantic Ridge record Earth's flipping magnetic field in matching stripes – the sea floor is spreading"]]),
    W("How long?",
      "The Atlantic widens by about 2.5 cm a year. How many km does it widen in 1 million years?",
      [("2.5 × 1 000 000 = 2 500 000 cm", "multiply"), ("2 500 000 ÷ 100 = 25 000 m", "cm to m"), ("25 000 ÷ 1000 = 25 km", "m to km")], "25 km"),
    Y("Evidence",
      mcq("s9u13r21", "Why are matching fossils of a small freshwater reptile in Africa and South America evidence for moving plates?",
          [("It could not have crossed an ocean, so the lands were once joined.", True, "Yes."), ("It swam across the Atlantic.", False, "A small freshwater reptile could not cross salt ocean."),
           ("Fossils move with the wind.", False, "Fossils are in rock."), ("All reptiles lived everywhere.", False, "This is one species found in two places.")],
          "How could the same animal live in both places?", "The continents were joined when it lived, then drifted apart.")),
    K("Key points",
      "Wegener proposed **continental drift** from a supercontinent, Pangaea.",
      "Evidence: fitting coastlines, matching fossils, volcano and earthquake locations, magnetic stripes.",
      "Ideas were accepted once evidence and a mechanism were found."),
    book=BK(
        [("Pangaea", "the supercontinent that later broke apart"), ("continental drift", "the slow movement of continents"), ("Mid-Atlantic Ridge", "where two plates move apart under the Atlantic")],
        [], [],
        [Ex("Give three pieces of evidence for moving plates.", ans="any three: fitting coastlines, matching fossils, volcano and earthquake locations, magnetic stripes"),
         Ex("Why did many scientists reject Wegener's idea at first?", ans="He could not explain what force moved the continents."),
         Ex("Two cities on opposite sides of a ridge move apart at 3 cm a year. How far in 1000 years, in m?", ans="3000 cm = 30 m", think=True)],
        ["describe the evidence for plate movement", "explain how scientific ideas change"],
        look=["the evidence table"],
        note="Read it after the video: evidence for tectonic plates (answers at the back)."),
)

# =====================================================================================================
# 13.3 The carbon cycle · 9ESc.01
# =====================================================================================================
READ["13.3"] = L(
    H("The same carbon",
      "Some of the carbon atoms in your body may once have been inside a dinosaur, a tree, or the air above an ancient ocean.",
      "How can carbon keep moving between living things and the air?"),
    I("The carbon cycle",
      "Carbon moves between the air, living things, the oceans and rocks.",
      fig={"kind": "carboncycle"},
      table=[["Process", "What happens to carbon"], ["A **photosynthesis**", "plants take in carbon dioxide from the air"], ["B, D **respiration**", "living things release carbon dioxide"],
             ["C **feeding**", "carbon passes to animals in food"], ["**decomposition**", "decomposers break down dead matter, releasing carbon dioxide"],
             ["F **fossilisation**", "some dead matter is buried and slowly becomes fossil fuels"], ["E **combustion**", "burning fuels releases carbon dioxide"]]),
    I("Humans and the carbon cycle",
      "For millions of years the carbon cycle stayed roughly balanced. By burning fossil fuels and cutting down forests, humans now add carbon dioxide **faster** than photosynthesis and the oceans can remove it, so the amount in the air keeps rising."),
    Y("Processes",
      grid("s9u13r31", "Does each process take carbon dioxide out of the air or put it in?", ["Removes CO₂", "Adds CO₂"],
           [("photosynthesis", "Removes CO₂"), ("respiration", "Adds CO₂"), ("combustion", "Adds CO₂"), ("decomposition", "Adds CO₂")],
           "Only one of these is done by plants to make food.", "Photosynthesis removes CO₂; respiration, combustion and decomposition release it.")),
    K("Key points",
      "**Photosynthesis** removes carbon dioxide from the air.",
      "**Respiration**, **decomposition** and **combustion** release it.",
      "Burning fossil fuels adds carbon faster than the cycle can remove it."),
    book=BK(
        [("carbon cycle", "the movement of carbon between air, living things, oceans and rocks"), ("decomposition", "breakdown of dead matter by decomposers"),
         ("combustion", "burning a fuel"), ("fossil fuel", "coal, oil or gas formed from ancient dead organisms")],
        [], [],
        [Ex("Name the process that removes carbon dioxide from the air.", ans="photosynthesis"),
         Ex("Name three processes that release carbon dioxide.", ans="respiration, decomposition, combustion"),
         Ex("Describe how carbon in a plant can end up back in the air.", ans="e.g. an animal eats the plant and respires; or the plant dies and decomposes; or it is burned."),
         Ex("Explain how cutting down forests affects the carbon cycle in two ways.", ans="Less photosynthesis removes less CO₂; burning or rotting the trees releases more.", think=True)],
        ["describe the carbon cycle", "explain how humans affect it"],
        look=["the carbon cycle diagram"],
        note="Read it after the video: the carbon cycle (answers at the back)."),
)

# =====================================================================================================
# 13.4 What is climate change? · 9ESc.02, 9SIC.05
# =====================================================================================================
READ["13.4"] = L(
    H("Snowball Earth",
      "Rocks show that, long ago, ice may have covered almost the whole planet. At other times there were palm trees near the poles.",
      "If climate has always changed, why are scientists so worried now?"),
    I("Climate change: past and future",
      "**Climate** is the pattern of weather over many years. It has changed naturally in the past – ice ages and warm periods – over thousands to millions of years.",
      fig={"kind": "sciGreenhouse"},
      then=["Today Earth is warming much faster. Extra carbon dioxide from burning fossil fuels strengthens the **greenhouse effect**, trapping more heat."]),
    I("Real data: global temperature since 1880",
      "Difference between each year's global average temperature and the 1951–1980 average (smoothed):",
      fig={"kind": "linegraph", "x": {"min": 1880, "max": 2020, "step": 20, "label": "year"}, "y": {"min": -0.4, "max": 1.2, "step": 0.2, "label": "difference (°C)"},
           "series": [{"pts": [[1880, -0.2], [1900, -0.2], [1920, -0.25], [1940, 0.05], [1960, 0.0], [1980, 0.2], [2000, 0.45], [2020, 1.0]]}]},
      then=["Before 1940 most years were cooler than the average; since 1980 every year has been warmer, and the rate of warming has increased."]),
    I("Impacts",
      "Scientists predict and already observe:",
      table=[["Impact", "Why"], ["rising sea levels", "warmer water expands and ice sheets melt – a few millimetres a year, threatening coastal cities"],
             ["more extreme weather", "more severe storms, droughts and floods"], ["habitat loss", "some species cannot adapt or move fast enough"]]),
    Y("Rate of warming",
      num("s9u13r41", "Use the graph. By how many °C did the difference rise from 1980 to 2020?", 0.8, "Read both values and subtract.", "1.0 − 0.2 = 0.8 °C – much faster than earlier.", tol=0.05)),
    K("Key points",
      "Climate has changed naturally in the past, but slowly.",
      "Since 1880, and especially since 1980, Earth has warmed fast – mainly from burning fossil fuels.",
      "Impacts: rising seas, extreme weather, habitat loss."),
    book=BK(
        [("climate", "the pattern of weather over many years"), ("greenhouse effect", "gases in the atmosphere trapping heat"), ("global warming", "the rise in Earth's average temperature")],
        [], [],
        [Ex("Explain how burning fossil fuels causes global warming.", ans="It releases CO₂, which strengthens the greenhouse effect and traps more heat."),
         Ex("Give two impacts of climate change.", ans="any two: rising sea levels, extreme weather, habitat loss"),
         Ex("Quick quiz.", ("What moves tectonic plates?", "convection currents in the mantle"), ("Two pieces of evidence for plates?", "fitting coastlines, matching fossils"),
            ("Two processes that release CO₂?", "respiration, combustion"), ("Why do sea levels rise as Earth warms?", "water expands and ice melts")),
         Ex("How does the recent change in climate differ from past natural changes?", ans="It is much faster – decades instead of thousands of years – and caused mainly by humans.", think=True)],
        ["describe causes and impacts of climate change", "interpret temperature data"],
        look=["the greenhouse effect", "the temperature graph"],
        note="Read it after the video: climate change past and present, plus a quick quiz (answers at the back)."),
)
