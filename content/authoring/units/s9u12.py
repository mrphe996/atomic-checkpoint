# -*- coding: utf-8 -*-
"""Stage 9 Unit 12 – Electrical Circuits. Written by the Camday teaching team."""
from c_kit2 import Unit, B

STRAND = "Physics"
BLURB = "Current and voltage, circuit symbols, series and parallel circuits, combining cells in batteries, and calculating resistance with Ohm's law."
OBJECTIVES = {
    "O1": {"sec": "12.1", "code": "9Pe.02, 9Pe.04", "codeNote": "", "t": "Describe current and voltage, how they are measured, and use standard circuit symbols."},
    "O2": {"sec": "12.2", "code": "9Pe.01, 9Pe.02", "codeNote": "series", "t": "Describe current and voltage in series circuits and how to connect ammeters and voltmeters."},
    "O3": {"sec": "12.3", "code": "9Pe.01, 9SIC.01", "codeNote": "parallel", "t": "Describe current and voltage in parallel circuits and the limits of circuit models."},
    "O4": {"sec": "12.4", "code": "9Pe.02", "codeNote": "cells", "t": "Explain the effect of connecting cells in series and in parallel."},
    "O5": {"sec": "12.5", "code": "9Pe.03", "codeNote": "", "t": "Calculate resistance using resistance = voltage ÷ current."},
}
SECTIONS = [
    {"id": "12.1", "title": "The flow of electric current", "objs": ["O1"]},
    {"id": "12.2", "title": "Series circuits", "objs": ["O2"]},
    {"id": "12.3", "title": "Parallel circuits", "objs": ["O3"]},
    {"id": "12.4", "title": "Electrical cells and batteries", "objs": ["O4"]},
    {"id": "12.5", "title": "Resistance", "objs": ["O5"]},
]
u = Unit(9, 12)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 12.1
u.sec("12.1", "O1")
u.gd("r", "Current or voltage?", "Quantity", [("Flow of electric charge", "Current"), ("The push that drives the charge", "Voltage"), ("Measured in amperes", "Current"), ("Measured in volts", "Voltage")])
u.gd("r", "Which meter measures each?", "Meter", [("Current", "Ammeter"), ("Voltage", "Voltmeter")], extra=["Thermometer"])
u.gd("r", "Name the component from its job.", "Component", [("Opens or closes the circuit", "Switch"), ("Provides the voltage", "Cell"), ("Gives out light", "Lamp"), ("Makes a buzzing sound", "Buzzer")])
u.ex("r", "Use the water-pipe model to explain current and voltage.", [("current like water flowing", ["current.*(flow|water)"]), ("voltage like water pressure / push", ["voltage.*(pressure|push)"]), ("needs a complete loop / closed circuit", ["complete|closed|loop"])],
     "Current is like water flowing through a pipe, and voltage is like the water pressure that pushes it. Water, like current, only keeps flowing round a complete, closed loop.")
u.mc("r", "Electric current is a flow of…", "electric charge (electrons)", ["water", "protons", "heat"])
u.mc("r", "Current only flows around a…", "complete, closed circuit", ["broken circuit", "single wire end", "open switch"])
u.mc("r", "Why do engineers use standard circuit symbols?", "So circuit diagrams are understood everywhere", ["To make circuits work faster", "To save wire", "To change the voltage"], d="H")
u.mc("r", "A switch is opened. What happens to the current?", "It stops, because the circuit is broken", ["It doubles", "It flows backwards", "It stays the same"], d="VH")
mcs("p", [
    ("Current is measured in…", "amperes", ["volts", "ohms", "watts"]),
    ("Voltage is measured in…", "volts", ["amperes", "ohms", "joules"]),
    ("Another name for voltage is…", "potential difference", ["resistance", "current", "power"]),
    ("Voltage is provided by…", "cells, batteries and generators", ["lamps", "switches", "wires only"]),
    ("A circuit is…", "a path for current", ["a type of battery", "a switch", "a magnet"]),
    ("Moving electrons make up…", "an electric current", ["a voltage", "a resistance", "a magnet"]),
    ("An ammeter measures…", "current", ["voltage", "resistance", "temperature"]),
    ("A voltmeter measures…", "voltage", ["current", "mass", "time"]),
    ("Which component turns electrical energy into light?", "Lamp", ["Switch", "Cell", "Resistor"]),
    ("Which component reduces the current?", "Resistor", ["Cell", "Ammeter", "Wire"]),
    ("In the water model, voltage is like…", "water pressure", ["the pipe", "the water", "a tap"]),
    ("In the water model, a closed tap is like…", "an open switch", ["a cell", "a lamp", "a closed switch"]),
    ("Understanding circuits helps us…", "stay safe and save energy", ["make lightning", "see in the dark only", "stop magnets"]),
    ("A buzzer turns electrical energy into…", "sound", ["light", "chemical energy", "magnetism only"]),
    ("A circuit with a gap in it is…", "open (incomplete)", ["closed", "short", "parallel"]),
])
u.mt("p", "Match the quantity to its unit.", [("Current", "amperes (A)"), ("Voltage", "volts (V)"), ("Resistance", "ohms (Ω)")])
u.ms("p", "Select ALL the things that can provide a voltage.", ["Cell", "Battery", "Generator"], ["Lamp", "Switch"])
u.od("p", "Order the journey of current in a simple circuit.", ["Leaves the cell", "Flows through the wire", "Passes through the lamp", "Returns to the cell"])
u.ex("a", "Explain why a torch does not light if the battery is put in the wrong way round, but no current flows at all if a wire is broken.", [("broken wire – circuit incomplete", ["broken|incomplete|gap"]), ("no complete path so no current", ["no current|path|loop"]), ("battery wrong way – contacts/terminals don't connect or push opposes", ["wrong way|terminal|contact|oppos"])],
     "A broken wire leaves a gap, so there is no complete path and no current flows. A battery put in the wrong way round may not make contact with the terminals correctly, so again the circuit is not complete.")
u.mc("a", "A bird can stand on a single power line safely. Why?", "No current flows through it because there is no complete circuit through the bird", ["Birds are insulators", "The line has no voltage", "Birds absorb electricity"], skill="Reasoning")
u.mc("a", "What is a limitation of the water-pipe model?", "Water leaks from a broken pipe, but charge does not leak from a broken wire", ["It explains current", "It explains voltage", "It uses a loop"], skill="Models")
u.mc("a", "Why must circuits be complete for a doorbell to ring?", "Charge must flow all the way round to transfer energy to the buzzer", ["The buzzer stores charge", "Voltage only exists in open circuits", "The bell uses light"], skill="Reasoning")
u.stop("and back again", "A circuit is a path for…", "current", ["light", "water", "sound"])
u.stop("it only flows around a complete, closed circuit", "Current is measured with an…", "ammeter", ["voltmeter", "thermometer", "balance"])
u.stop("Voltage is measured in volts with a voltmeter", "Voltage is the … that drives the charge.", "push", ["flow", "resistance", "wire"])
u.stop("A switch opens or closes the circuit", "Standard circuit symbols are used so that…", "everyone understands the diagram", ["circuits run faster", "lamps are brighter", "wires are shorter"])

# ---------------------------------------------------------------- 12.2
u.sec("12.2", "O2")
u.tb("r", "Two identical lamps in series with a 6 V cell. Complete the table.", ["Lamp", "Voltage (V)", "Current (A)"], [["Lamp 1", B(3), "0.2"], ["Lamp 2", B(3), B(0.2)]])
u.gd("r", "How is each meter connected?", "Connection", [("Ammeter", "In series"), ("Voltmeter", "In parallel, across the component")])
u.gd("r", "In a series circuit with three lamps, what happens?", "Result", [("A third lamp is added", "All dimmer"), ("One lamp breaks", "All go out")], extra=["All brighter"])
u.ex("r", "Explain why all the lamps in a series circuit go out if one breaks.", [("only one path / single loop", ["one path|single|only path|loop"]), ("broken lamp breaks the circuit", ["broken|gap|incomplete"]), ("no current flows anywhere", ["no current|stops"])],
     "In a series circuit there is only one path. If one lamp breaks, the circuit is broken, so no current can flow anywhere and all the lamps go out.")
u.mc("r", "In a series circuit, the current is…", "the same at every point", ["bigger near the cell", "zero in the middle", "different in each lamp"])
u.mc("r", "In a series circuit, the cell's voltage is…", "shared between the components", ["the same across every component", "doubled", "lost"])
u.mc("r", "Why do lamps get dimmer when more are added in series?", "The voltage is shared between more lamps", ["The current increases", "The cell gets bigger", "Each lamp gets more voltage"], d="H")
u.mc("r", "A voltmeter is connected in series by mistake. What is the problem?", "It has very high resistance, so almost no current flows", ["It measures current instead", "It shows double the voltage", "Nothing changes"], d="VH")
mcs("p", [
    ("A series circuit has…", "one single loop", ["several branches", "no loop", "two cells always"]),
    ("A series circuit is like a…", "one-lane road", ["multi-lane highway", "roundabout", "car park"]),
    ("Two identical lamps in series with a 4 V cell get … each.", "2 V", ["4 V", "8 V", "1 V"]),
    ("An ammeter is connected…", "in series", ["in parallel", "across a lamp", "outside the circuit"]),
    ("A voltmeter is connected…", "in parallel", ["in series", "inside the cell", "after the switch only"]),
    ("Adding lamps in series makes the current…", "smaller", ["bigger", "the same", "infinite"]),
    ("If one lamp in series breaks, the others…", "go out", ["get brighter", "stay on", "flash"]),
    ("Fairy lights wired in series all go out when…", "one bulb fails", ["one bulb is brighter", "the switch is closed", "the voltage rises"]),
    ("Readings from ammeters in different places in a series circuit are…", "the same", ["all different", "zero", "higher near the end"]),
    ("A voltmeter across a lamp measures…", "the voltage across that lamp", ["the current", "the total resistance", "the time"]),
    ("The voltages across components in series add up to…", "the cell's voltage", ["zero", "double the cell's voltage", "the current"]),
    ("Electric charge in a series circuit has…", "only one route", ["many routes", "no route", "two routes"]),
    ("A switch in series controls…", "every component", ["only the first lamp", "nothing", "only the cell"]),
    ("Current flows through an ammeter because it is…", "part of the loop", ["across the lamp", "outside the circuit", "a voltmeter"]),
    ("In series, three identical lamps on a 9 V battery get … each.", "3 V", ["9 V", "27 V", "1 V"]),
])
u.mt("p", "Match the meter to how it is connected.", [("Ammeter", "in series"), ("Voltmeter", "in parallel across a component"), ("Switch", "in series to control the loop")])
u.ms("p", "Select ALL the features of a series circuit.", ["Same current everywhere", "Voltage is shared", "One lamp breaking switches all off"], ["Each lamp gets full voltage", "Several branches"])
u.od("p", "Order from brightest to dimmest lamps (identical lamps, same cell, series).", ["One lamp", "Two lamps", "Three lamps"])
u.ex("a", "A 12 V battery is connected in series to lamps A and B. The voltmeter across A reads 8 V. What is the voltage across B, and why might it differ from A?", [("4 V", ["4"]), ("voltages add up to the supply", ["add|total|12"]), ("lamps have different resistance", ["resist|different|not identical"])],
     "B has 12 − 8 = 4 V, because voltages in series add up to the supply. They differ because lamp A has a higher resistance than lamp B.")
u.nm("a", "In a series circuit, a 9 V battery is shared by three identical lamps. What is the voltage across two of them together?", 6, "V")
u.mc("a", "Why are old-style Christmas lights in series annoying?", "One failed bulb makes the whole string go out, and it is hard to find", ["They are too bright", "They use no current", "Each bulb needs its own switch"], skill="Reasoning")
u.mc("a", "An ammeter before the lamps reads 0.3 A. What does one after the lamps read?", "0.3 A", ["0.6 A", "0.15 A", "0 A"], skill="Application")
u.stop("With two identical lamps, each gets half", "In a series circuit, the current is…", "the same everywhere", ["different in each lamp", "zero", "doubled"])
u.stop("just like traffic stopping on a closed one-lane road", "If one lamp in series breaks…", "all the lamps go out", ["the others get brighter", "nothing changes", "only that lamp goes out"])
u.stop("across the component", "A voltmeter is connected…", "in parallel, across a component", ["in series", "inside the cell", "nowhere"])

# ---------------------------------------------------------------- 12.3
u.sec("12.3", "O3")
u.tb("r", "Three 1 A lamps on separate branches. Complete the table.", ["Branch", "Current (A)"], [["1", "1"], ["2", "1"], ["3", "1"], ["Total from cell", B(3)]])
u.gd("r", "Series or parallel?", "Circuit type", [("Each lamp gets the full voltage", "Parallel"), ("Current same everywhere", "Series"), ("One lamp fails, others stay on", "Parallel"), ("Single loop", "Series")])
u.gd("r", "Two identical lamps in parallel with a 6 V cell. What is the voltage across each?", "Voltage", [("Lamp 1", "6 V"), ("Lamp 2", "6 V")], extra=["3 V"])
u.ex("r", "Explain why homes are wired in parallel.", [("each appliance gets full voltage", ["full voltage|same voltage|230"]), ("one fails, others still work", ["fail|still work|stay on"]), ("each can be switched separately", ["switch|separate|independent"])],
     "In parallel, every appliance gets the full mains voltage, each can be switched on and off separately, and if one fails the others keep working.")
u.mc("r", "In a parallel circuit, components are on…", "separate branches", ["one single loop", "no wires", "the same lamp"])
u.mc("r", "Adding identical lamps in parallel makes each lamp…", "stay the same brightness", ["dimmer", "brighter", "go out"])
u.mc("r", "The total current from the cell in a parallel circuit equals…", "the sum of the branch currents", ["the current in one branch", "zero", "the voltage"], d="H")
u.mc("r", "Why do scientists keep developing better circuit models and analogies?", "Every model has limits, and understanding improves over time", ["Old models are always wrong", "Models never change", "Circuits change each year"], d="VH")
mcs("p", [
    ("A parallel circuit is like a…", "multi-lane highway", ["one-lane road", "dead end", "single path"]),
    ("In parallel, each branch gets…", "the full voltage", ["half the voltage", "no voltage", "double the voltage"]),
    ("If one lamp in parallel fails, the others…", "stay on", ["go out", "get dimmer", "explode"]),
    ("Homes are wired in…", "parallel", ["series", "one loop", "no circuit"]),
    ("Three 2 A branches draw a total of…", "6 A", ["2 A", "3 A", "0.67 A"]),
    ("Adding more branches in parallel makes the total current…", "bigger", ["smaller", "the same", "zero"]),
    ("Each branch in parallel can have its own…", "switch", ["cell always", "voltage source", "earth wire only"]),
    ("Road analogies help us picture circuits but have…", "limitations", ["no use", "perfect accuracy", "no meaning"]),
    ("In parallel, lamps are … than the same lamps in series.", "brighter", ["dimmer", "the same", "off"]),
    ("A circuit with two paths for current is…", "parallel", ["series", "open", "broken"]),
    ("Current splits at a…", "junction", ["lamp", "switch only", "cell"]),
    ("Currents in branches … to make the total.", "add up", ["cancel", "multiply", "divide"]),
    ("Turning off one light at home…", "does not turn off the others", ["turns off every light", "doubles the voltage", "breaks the fuse"]),
    ("A parallel circuit drains a battery … than a single lamp.", "faster", ["slower", "at the same rate", "never"]),
    ("Branch currents in parallel with identical lamps are…", "equal", ["different", "zero", "infinite"]),
])
u.mt("p", "Match the circuit to its property.", [("Series", "voltage shared"), ("Parallel", "full voltage on each branch"), ("Junction", "where the current splits")])
u.ms("p", "Select ALL the advantages of parallel circuits.", ["Each lamp gets full voltage", "Lamps can be switched separately", "One failure doesn't stop others"], ["Uses less current from the cell", "Only one path"])
u.od("p", "Order to find the total current in a parallel circuit.", ["Measure the current in each branch", "Write the readings down", "Add them together", "Compare with the ammeter by the cell"])
u.ex("a", "A parallel circuit has branches with currents 0.5 A, 0.3 A and 0.2 A. Find the total current and explain what happens to it if the 0.3 A lamp fails.", [("total 1.0 A", ["1\\.0|1 a|1a\\b|1 amp"]), ("falls to 0.7 A", ["0\\.7"]), ("other branches unchanged / still lit", ["unchanged|still|stay"])],
     "The total is 0.5 + 0.3 + 0.2 = 1.0 A. If the 0.3 A lamp fails, its branch carries no current, so the total falls to 0.7 A, while the other lamps stay lit as before.")
u.nm("a", "The cell supplies 2.4 A to four identical parallel branches. What is the current in each?", 0.6, "A")
u.mc("a", "Why does a battery run down faster with lamps in parallel than in series?", "Parallel lamps draw a bigger total current", ["Parallel lamps use less current", "Series lamps are brighter", "Voltage increases in series"], skill="Reasoning")
u.mc("a", "A limitation of the highway model of parallel circuits is…", "cars can choose lanes and stop, but charge splits by resistance and cannot pile up", ["it shows several paths", "it explains branches", "it helps picture the circuit"], skill="Models")
u.stop("which is why homes are wired in parallel", "If one lamp in parallel fails, the others…", "stay on", ["go out", "flicker off", "get dimmer"])
u.stop("scientists develop better models and analogies", "Three 1 A lamps in parallel draw a total of…", "3 A", ["1 A", "0.33 A", "6 A"])

# ---------------------------------------------------------------- 12.4
u.sec("12.4", "O4")
u.tb("r", "Cells in series. Complete the total voltage.", ["Number of cells", "Voltage of each (V)", "Total (V)"], [["4", "3", B(12)], ["3", "1.5", B(4.5)]])
u.gd("r", "Series or parallel cells?", "Connection", [("Voltages add up", "Series"), ("Lasts longer, same voltage", "Parallel"), ("Positive joined to negative", "Series")])
u.gd("r", "In the cell symbol, which line is the positive terminal?", "Terminal", [("Longer line", "Positive"), ("Shorter line", "Negative")])
u.ex("r", "Compare connecting two 1.5 V cells in series and in parallel.", [("series: 3 V – voltages add", ["3|add"]), ("parallel: 1.5 V – same voltage", ["1\\.5|same voltage"]), ("parallel lasts longer / more capacity", ["longer|capacity"])],
     "In series, the voltages add to give 3 V. In parallel, the voltage stays at 1.5 V, but the capacity increases so the battery lasts longer.")
u.mc("r", "A cell stores energy in…", "chemicals", ["magnets", "light", "water"])
u.mc("r", "A battery is…", "two or more cells joined together", ["one lamp", "a switch", "a single wire"])
u.mc("r", "Why do rechargeable batteries cost more at first but are better over time?", "They can be reused many times, saving money and waste", ["They never run out", "They have higher voltage always", "They don't use chemicals"], d="H")
u.mc("r", "Six 1.5 V cells in parallel give…", "1.5 V, lasting longer", ["9 V", "0.25 V", "6 V"], d="VH")
mcs("p", [
    ("In a closed circuit, the chemicals in a cell…", "react", ["freeze", "stay unchanged", "turn into metal"]),
    ("Cells in series are connected…", "positive to negative", ["positive to positive", "negative to negative", "not at all"]),
    ("Four 3 V cells in series give…", "12 V", ["3 V", "7 V", "0.75 V"]),
    ("Cells in parallel give the same voltage as…", "one cell", ["all cells added", "zero", "half a cell"]),
    ("Cells in parallel make the battery…", "last longer", ["run out faster", "explode", "lighter"]),
    ("Cells in series increase the…", "voltage", ["capacity only", "resistance of the lamp", "mass of wire"]),
    ("The longer line in the cell symbol is…", "positive", ["negative", "the switch", "earth"]),
    ("Used batteries should be…", "recycled safely", ["burned", "buried in gardens", "thrown in rivers"]),
    ("A 9 V battery is usually made of…", "six 1.5 V cells in series", ["one 9 V cell only", "nine 9 V cells", "1.5 V cells in parallel"]),
    ("Rechargeable batteries are…", "greener over time", ["always worse", "single-use", "free"]),
    ("A cell transfers energy by…", "electricity", ["sound", "magnetism only", "wind"]),
    ("Putting one cell the wrong way round in series…", "reduces the total voltage", ["doubles the voltage", "has no effect", "increases capacity"]),
    ("Capacity means how long the battery…", "can supply current", ["weighs", "is", "costs"]),
    ("A torch needs 3 V. Using 1.5 V cells, you connect…", "two in series", ["two in parallel", "one only", "three in parallel"]),
    ("Cells convert chemical energy into…", "electrical energy", ["nuclear energy", "sound only", "light only"]),
])
u.mt("p", "Match the arrangement to the result.", [("Two 1.5 V cells in series", "3 V"), ("Two 1.5 V cells in parallel", "1.5 V, lasts longer"), ("Three 2 V cells in series", "6 V")])
u.ms("p", "Select ALL the true statements about cells in series.", ["Voltages add up", "Positive joins negative", "Capacity stays the same"], ["Voltage stays the same", "Lasts much longer"])
u.od("p", "Order these batteries from lowest to highest voltage.", ["One 1.5 V cell", "Two 1.5 V cells in series", "Four 1.5 V cells in series", "Six 1.5 V cells in series"])
u.ex("a", "A device needs 6 V and must run for a long time. Using 1.5 V cells, suggest an arrangement and explain.", [("4 cells in series for 6 V", ["4|four"]), ("add parallel sets for capacity", ["parallel|another set|two sets"]), ("voltage adds in series, capacity in parallel", ["add|capacity|longer"])],
     "Connect four 1.5 V cells in series to give 6 V. Connect a second set of four in parallel with the first, so the voltage stays 6 V but the capacity doubles and it lasts longer.")
u.nm("a", "Three 1.5 V cells are in series, but one is reversed. What is the total voltage?", 1.5, "V")
u.mc("a", "Why are rechargeable batteries better for the environment?", "Fewer batteries are made and thrown away", ["They contain no chemicals", "They give higher voltage", "They never need charging"], skill="Reasoning")
u.mc("a", "Two identical cells in parallel power a lamp. Compared with one cell, the lamp is…", "the same brightness but stays lit longer", ["twice as bright", "half as bright", "off"], skill="Reasoning")
u.stop("the longer line is the positive terminal", "A battery is…", "two or more cells joined together", ["one cell", "a lamp", "a switch"])
u.stop("The current capacity stays the same", "Four 3 V cells in series give…", "12 V", ["3 V", "7 V", "0.75 V"])
u.stop("but are cheaper and greener over time", "Cells in parallel make a battery…", "last longer", ["give more voltage", "run out faster", "lighter"])

# ---------------------------------------------------------------- 12.5
u.sec("12.5", "O5")
u.tb("r", "Complete the resistance (R = V ÷ I).", ["Voltage (V)", "Current (A)", "Resistance (Ω)"], [["12", "2", B(6)], ["230", "0.5", B(460)], ["6", "0.3", B(20)]])
u.gr("r", "Voltage and current for a resistor. Plot the points.", {"label": "Voltage (V)", "min": 0, "max": 10, "step": 2}, {"label": "Current (A)", "min": 0, "max": 0.5, "step": 0.1}, [[0, 0], [2, 0.1], [4, 0.2], [6, 0.3], [8, 0.4]])
u.mc("r", "From the graph, the resistor's resistance is…", "20 Ω", ["0.05 Ω", "2 Ω", "200 Ω"], skill="Data")
u.ex("r", "State Ohm's law in words and explain what happens to the current if resistance increases with the same voltage.", [("more voltage – more current", ["more voltage|voltage increases|increases with voltage|with (the )?voltage"]), ("R = V ÷ I", ["v ?÷ ?i|v/i|voltage divided|voltage ÷ current|voltage / current"]), ("more resistance – less current", ["less current|current decreases|smaller current|current.{0,15}(smaller|decreas|less|lower)"])],
     "Ohm's law: current increases with voltage and resistance = voltage ÷ current. With the same voltage, increasing the resistance makes the current smaller.")
u.mc("r", "Resistance is measured in…", "ohms", ["amperes", "volts", "joules"])
u.mc("r", "Resistance is how much a component…", "opposes the current", ["stores charge", "pushes charge", "produces voltage"])
u.mc("r", "Electric heaters use resistance to…", "turn electrical energy into heat", ["increase current", "store chemicals", "make light only"], d="H")
u.mc("r", "The voltage across a resistor is doubled. Its resistance stays the same. The current…", "doubles", ["halves", "stays the same", "becomes zero"], d="VH")
mcs("p", [
    ("Resistance =", "voltage ÷ current", ["current ÷ voltage", "voltage × current", "voltage + current"]),
    ("The symbol for ohms is…", "Ω", ["A", "V", "W"]),
    ("More resistance with the same voltage gives…", "less current", ["more current", "the same current", "infinite current"]),
    ("More voltage with the same resistance gives…", "more current", ["less current", "no current", "the same current"]),
    ("A 230 V bulb with 0.5 A has a resistance of…", "460 Ω", ["115 Ω", "230.5 Ω", "0.002 Ω"]),
    ("12 V and 2 A gives a resistance of…", "6 Ω", ["24 Ω", "10 Ω", "14 Ω"]),
    ("Voltage = current ×", "resistance", ["time", "power", "charge"]),
    ("Current = voltage ÷", "resistance", ["time", "current", "power"]),
    ("Thin, long wires have … resistance than thick, short ones.", "more", ["less", "the same", "no"]),
    ("A resistor's job is to…", "limit the current", ["increase the voltage", "store energy", "make sound"]),
    ("Kettles and toasters work because of…", "resistance heating", ["magnetism", "light", "sound"]),
    ("A component with very low resistance lets … current flow.", "a large", ["no", "a tiny", "negative"]),
    ("Copper wires are used because they have…", "low resistance", ["high resistance", "no electrons", "high voltage"]),
    ("A variable resistor can be used to…", "dim a lamp", ["make a lamp brighter than its maximum", "store charge", "measure voltage"]),
    ("Ohm's law was named after…", "Georg Ohm", ["Isaac Newton", "Marie Curie", "Charles Darwin"]),
])
u.mt("p", "Match the quantity to its symbol and unit.", [("Voltage", "V, volts"), ("Current", "I, amperes"), ("Resistance", "R, ohms")])
u.od("p", "Order the steps to find the resistance of a lamp.", ["Connect the lamp to a cell", "Measure current with an ammeter in series", "Measure voltage with a voltmeter in parallel", "Divide voltage by current"])
u.nm("p", "A resistor has 9 V across it and 0.45 A through it. What is its resistance?", 20, "Ω")
u.ex("a", "A 10 Ω resistor is connected to a 6 V battery. Calculate the current, and then the new current if a second 10 Ω resistor is added in series.", [("I = 6 ÷ 10 = 0.6 A", ["0\\.6"]), ("series total 20 Ω", ["20"]), ("new current 0.3 A", ["0\\.3"])],
     "I = V ÷ R = 6 ÷ 10 = 0.6 A. With two 10 Ω resistors in series the total is 20 Ω, so I = 6 ÷ 20 = 0.3 A.")
u.nm("a", "What voltage is needed to push 0.25 A through a 48 Ω resistor?", 12, "V")
u.mc("a", "A lamp's resistance rises as it heats up. What does this mean for its V–I graph?", "It curves, because current rises less than voltage", ["It is a straight line", "Current falls as voltage rises", "It has no shape"], skill="Data")
u.mc("a", "Why is high resistance useful in a heater but wasteful in power cables?", "In a heater the heat is wanted; in cables it is energy lost", ["Heaters need no current", "Cables should get hot", "Resistance creates energy"], skill="Reasoning")
u.stop("Resistance equals voltage divided by current", "Resistance is measured in…", "ohms", ["amperes", "volts", "joules"])
u.stop("Electric heaters use resistance to turn electrical energy into heat", "230 V and 0.5 A gives a resistance of…", "460 Ω", ["115 Ω", "0.002 Ω", "230 Ω"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Electrical circuits", "sec": None, "kids": [
    {"id": "iv", "t": "Current and voltage", "d": "Current: flow of charge, amperes, ammeter • Voltage: push, volts, voltmeter", "obj": "O1", "sec": "12.1"},
    {"id": "sr", "t": "Series", "d": "One loop • Same current • Voltage shared • One fails, all off", "obj": "O2", "sec": "12.2"},
    {"id": "pl", "t": "Parallel", "d": "Branches • Full voltage each • Currents add • Homes", "obj": "O3", "sec": "12.3"},
    {"id": "cl", "t": "Cells", "d": "Series: voltages add • Parallel: same voltage, lasts longer", "obj": "O4", "sec": "12.4"},
    {"id": "rs", "t": "Resistance", "d": "R = V ÷ I • Ohms • Heaters", "obj": "O5", "sec": "12.5"},
]}
