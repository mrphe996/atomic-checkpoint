# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 12 Electrical Circuits – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9Pe.01–9Pe.04, 9SIC.01)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}

# =====================================================================================================
# 12.1 The flow of electric current · 9Pe.02, 9Pe.04
# =====================================================================================================
READ["12.1"] = L(
    H("Instant light",
      "Flick a switch and the light comes on immediately, even though the power station is many kilometres away.",
      "What is flowing in the wires, and what makes it flow?"),
    I("Current",
      "An **electric current** is a flow of electric **charge** – moving **electrons** in a metal wire.",
      then=["Think of water flowing in a pipe: the current is how much flows past each second.",
            "Current is measured in **amperes (A)** with an **ammeter**. It flows only around a **complete (closed) circuit**."]),
    I("Voltage",
      "**Voltage** (potential difference) is the 'push' that drives the charge round – like water pressure from a pump.",
      then=["Cells, batteries and generators provide voltage. It is measured in **volts (V)** with a **voltmeter**."]),
    I("Circuit symbols",
      "Engineers everywhere draw circuits with the same standard symbols.",
      fig={"kind": "symbols"},
      then=["A **switch** opens (breaks) or closes (completes) the circuit."]),
    Y("Which meter?",
      grid("s9u12r11", "Which is measured by each meter or in each unit?", ["Current", "Voltage"],
           [("amperes (A)", "Current"), ("volts (V)", "Voltage"), ("an ammeter", "Current"), ("a voltmeter", "Voltage"), ("the push from the battery", "Voltage")],
           "Flow or push?", "Current = flow (A, ammeter); voltage = push (V, voltmeter).")),
    K("Key points",
      "**Current**: flow of charge; amperes; ammeter; needs a complete circuit.",
      "**Voltage**: the push; volts; voltmeter; provided by cells.",
      "Use standard circuit symbols."),
    book=BK(
        [("electric current", "a flow of electric charge"), ("ampere (A)", "the unit of current"), ("voltage", "the push that drives a current"), ("volt (V)", "the unit of voltage")],
        [], [],
        [Ex("What is an electric current, and what unit is it measured in?", ans="a flow of charge (electrons); amperes"),
         Ex("Draw the symbols for a cell, a lamp, a switch, an ammeter and a voltmeter.", ans="see the symbol key"),
         Ex("Use the water-pipe model to explain the difference between current and voltage.", ans="Current is the amount of water flowing; voltage is the pressure from the pump pushing it.", think=True)],
        ["describe current and voltage", "use circuit symbols"],
        look=["the symbol key"],
        note="Read it after the video: current, voltage and circuit symbols (answers at the back)."),
)

# =====================================================================================================
# 12.2 Series circuits · 9Pe.01, 9Pe.02
# =====================================================================================================
READ["12.2"] = L(
    H("Old fairy lights",
      "On some old strings of fairy lights, when one bulb breaks, every bulb goes dark.",
      "Why would one broken bulb switch off all the others?"),
    I("Series circuits",
      "In a **series circuit** the components are connected one after another in a **single loop** – there is only one path.",
      fig={"kind": "circuit", "type": "series", "top": ["cell", "switch"], "right": ["lamp"], "bottom": ["lamp"]},
      then=["The **current is the same** everywhere in a series circuit.",
            "The battery's **voltage is shared** between the components. Add more lamps and each gets less voltage, so they are all **dimmer**.",
            "If one lamp breaks, the only path is broken and **all** go out."]),
    I("Connecting meters",
      "How to connect the meters:",
      fig={"kind": "circuit", "type": "series", "top": ["battery", {"k": "ammeter", "l": "A"}], "right": ["resistor"], "bottom": [{"k": "voltmeter", "l": "V"}]},
      table=[["Meter", "How it is connected"], ["**ammeter**", "in **series** – the current flows through it"], ["**voltmeter**", "in **parallel** – across the component"]]),
    W("Sharing voltage",
      "Two identical lamps are in series with a 6 V battery. What is the voltage across each lamp?",
      [("the voltage is shared", "series rule"), ("6 ÷ 2 = 3 V", "identical lamps share equally")], "3 V each"),
    Y("Series",
      num("s9u12r21", "Three identical lamps are in series with a 9 V battery. What is the voltage across each lamp in V?", 3, "The voltage is shared equally.", "9 ÷ 3 = 3 V.")),
    K("Key points",
      "Series: one loop; the **current is the same** everywhere.",
      "The voltage is **shared**; more lamps → dimmer.",
      "One break stops everything. Ammeter in series; voltmeter in parallel."),
    book=BK(
        [("series circuit", "components in a single loop"), ("ammeter", "measures current; connected in series"), ("voltmeter", "measures voltage; connected in parallel")],
        [], [],
        [Ex("Describe what happens to the brightness of lamps in series as more are added.", ans="They get dimmer, because the voltage is shared between more lamps."),
         Ex("A series circuit has an ammeter reading 0.3 A next to the cell. What does an ammeter between two lamps read?", ans="0.3 A – the current is the same everywhere"),
         Ex("Back to 'Start here': explain the fairy lights.", ans="They are in series; a broken bulb breaks the only path, so the current stops.", think=True)],
        ["describe current and voltage in series circuits", "connect ammeters and voltmeters"],
        look=["the series circuit", "where to put the meters"],
        note="Read it after the video: series circuits and meters (answers at the back)."),
)

# =====================================================================================================
# 12.3 Parallel circuits · 9Pe.01, 9SIC.01
# =====================================================================================================
READ["12.3"] = L(
    H("Separate switches",
      "At home you can switch the kitchen light off and the bedroom light stays on.",
      "How must the house be wired for that to work?"),
    I("Predict, watch, explain: removing one lamp",
      "Two lamps are wired in series, and another two in parallel. One lamp is removed from each circuit.",
      then=["In series, the other lamp goes out. In parallel, the other lamp stays on, just as bright.",
            "In series there is only one path. In parallel each lamp is on its own **branch** with the full voltage, so the other branch is still a complete circuit."]),
    I("Parallel circuits",
      "In a **parallel circuit** the components are on **separate branches**.",
      fig={"kind": "circuit", "type": "parallel", "main": ["cell", {"k": "ammeter", "l": "A1"}], "branches": [["lamp", {"k": "ammeter", "l": "A2"}], ["lamp", {"k": "ammeter", "l": "A3"}]]},
      then=["Each branch gets the **full voltage**, so adding identical lamps does not make them dimmer.",
            "The **total current is the sum** of the branch currents: A1 = A2 + A3.",
            "If one lamp fails, the others stay on – that is why homes are wired in parallel."]),
    W("Adding branch currents",
      "Three lamps are in parallel. Each branch carries 0.5 A. What is the current from the cell?",
      [("total = sum of branches", "parallel rule"), ("0.5 + 0.5 + 0.5 = 1.5 A", "add")], "1.5 A"),
    Y("Parallel",
      num("s9u12r31", "In a parallel circuit, A2 reads 0.4 A and A3 reads 0.6 A. What does A1 (next to the cell) read in A?", 1.0, "Add the branch currents.", "0.4 + 0.6 = 1.0 A.")),
    X("Models have limits",
      "Water-pipe or road models help us picture circuits, but they are not perfect: electrons do not leak out of a broken wire the way water leaks from a pipe. Scientists improve models as understanding grows."),
    Y("Series or parallel?",
      grid("s9u12r32", "Is each statement true of series or parallel circuits?", ["Series", "Parallel"],
           [("current is the same everywhere", "Series"), ("each lamp gets the full voltage", "Parallel"), ("one broken lamp turns them all off", "Series"), ("used for house lighting", "Parallel")],
           "One path or many?", "Series: one loop; parallel: separate branches.")),
    K("Key points",
      "Parallel: separate branches; each gets the full voltage.",
      "Total current = sum of the branch currents.",
      "One lamp failing does not affect the others; every model has limitations."),
    book=BK(
        [("parallel circuit", "components on separate branches"), ("branch", "one of the separate paths in a parallel circuit"), ("model", "a simple way of picturing how something works")],
        [], [],
        [Ex("A parallel circuit has branch currents of 0.2 A, 0.3 A and 0.5 A. Find the total current.", ans="1.0 A"),
         Ex("Why are the lamps in a house wired in parallel?", ans="Each can be switched separately, each gets the full voltage, and one failing does not turn off the others."),
         Ex("Give one limitation of the water-pipe model of a circuit.", ans="e.g. water leaks from a broken pipe, but charge does not leak from a broken wire.", think=True)],
        ["describe current and voltage in parallel circuits", "compare series and parallel", "recognise the limits of models"],
        look=["the parallel circuit with three ammeters"],
        note="Read it after the video: parallel circuits and models (answers at the back)."),
)

# =====================================================================================================
# 12.4 Electrical cells and batteries · 9Pe.02
# =====================================================================================================
READ["12.4"] = L(
    H("Cells in a torch",
      "A torch needs four 1.5 V cells, all facing the same way. Put one in backwards and the torch hardly glows.",
      "Why does the direction of each cell matter?"),
    I("Cells in series",
      "A **battery** is two or more cells joined together. Joined in **series** (positive to negative), their **voltages add up**.",
      then=["Four 1.5 V cells in series give 4 × 1.5 = **6 V**. The current capacity stays the same as one cell.",
            "A cell put in backwards pushes the other way and cancels out the voltage of one of the others."]),
    I("Cells in parallel",
      "Joined in **parallel**, the voltage is the **same as one cell**, but the battery **lasts longer** – its capacity increases.",
      table=[["Connection", "Voltage", "How long it lasts"], ["one 1.5 V cell", "1.5 V", "1 ×"], ["two in series", "3 V", "1 ×"], ["two in parallel", "1.5 V", "about 2 ×"]],
      then=["Rechargeable batteries cost more at first, but are cheaper and produce less waste over time."]),
    Y("Batteries",
      num("s9u12r41", "Four 3 V cells are connected in series. What is the total voltage in V?", 12, "In series, voltages add.", "4 × 3 = 12 V.")),
    K("Key points",
      "Cells in **series**: voltages add up.",
      "Cells in **parallel**: same voltage as one cell, but lasts longer.",
      "Cells must face the same way in series."),
    book=BK(
        [("cell", "a single source of voltage"), ("battery", "two or more cells joined together")],
        [], [],
        [Ex("What voltage do three 1.5 V cells in series give?", ans="4.5 V"),
         Ex("Why would you connect two cells in parallel rather than in series?", ans="To keep the same voltage but make the battery last longer."),
         Ex("Three 1.5 V cells are in series but one is backwards. What is the total voltage?", ans="1.5 + 1.5 − 1.5 = 1.5 V", think=True)],
        ["explain the effect of cells in series and parallel"],
        look=["the batteries table"],
        note="Read it after the video: combining cells (answers at the back)."),
)

# =====================================================================================================
# 12.5 Resistance · 9Pe.03
# =====================================================================================================
READ["12.5"] = L(
    H("Glowing wire",
      "Inside a toaster, thin wires glow red-hot when a current flows. The copper wires in the cable stay cool.",
      "What is different about the toaster wire?"),
    I("Resistance",
      "**Resistance** is how much a component **opposes** the flow of current. It is measured in **ohms (Ω)**.",
      table=[["", ""], ["**resistance = voltage ÷ current**", "R = V ÷ I"]],
      then=["For the same voltage, a higher resistance means a smaller current.",
            "Long, thin wires have more resistance than short, thick ones. Resistance turns electrical energy into heat – used in heaters, toasters and kettles."]),
    W("Calculating resistance",
      "A kettle works on 230 V and draws 10 A. What is its resistance?",
      [("R = V ÷ I", "write the equation"), ("= 230 ÷ 10", "substitute"), ("= 23", "calculate")], "23 Ω"),
    I("Class data: current through a resistor at different voltages",
      "A student measures the current through a resistor:",
      fig={"kind": "linegraph", "x": {"min": 0, "max": 8, "step": 2, "label": "voltage (V)"}, "y": {"min": 0, "max": 0.5, "step": 0.1, "label": "current (A)"},
           "series": [{"pts": [[0, 0], [2, 0.1], [4, 0.2], [6, 0.3], [8, 0.4]]}]},
      then=["A straight line through the origin: doubling the voltage doubles the current. R = 4 ÷ 0.2 = **20 Ω** at every point, so the resistance stays the same."]),
    Y("Resistance",
      num("s9u12r51", "Calculate the resistance when the voltage is 12 V and the current is 2 A (in Ω).", 6, "R = V ÷ I.", "12 ÷ 2 = 6 Ω.", errs=[(24, "Divide voltage by current.")])),
    K("Key points",
      "Resistance opposes current; measured in ohms (Ω).",
      "**R = V ÷ I**.",
      "For a fixed resistor, current is proportional to voltage."),
    book=BK(
        [("resistance", "how much a component opposes current"), ("ohm (Ω)", "the unit of resistance")],
        [], [],
        [Ex("Calculate the resistance: (a) 6 V, 0.5 A (b) 9 V, 3 A.", ans="(a) 12 Ω (b) 3 Ω"),
         Ex("A 20 Ω resistor has 10 V across it. What current flows?", ans="I = V ÷ R = 0.5 A"),
         Ex("Quick quiz.", ("What measures current, and how is it connected?", "an ammeter, in series"), ("What happens to the other lamps if one breaks in series?", "they all go out"),
            ("Four 3 V cells in series: total voltage?", "12 V"), ("Resistance for 12 V and 2 A?", "6 Ω")),
         Ex("Explain why the heating wire in a toaster has a much higher resistance than the copper cable.", ans="High resistance turns more electrical energy into heat; the cable should waste as little as possible.", think=True)],
        ["calculate resistance", "interpret a current–voltage graph"],
        look=["R = V ÷ I", "the class data graph"],
        note="Read it after the video: resistance and R = V ÷ I, plus a quick quiz (answers at the back)."),
)
