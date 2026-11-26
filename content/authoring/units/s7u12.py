# -*- coding: utf-8 -*-
"""Stage 7 Unit 12 – Electricity. Written by the Camday teaching team."""
from c_kit import *

STRAND = "Physics"
BLURB = "Electron flow, conductors and insulators, circuit diagrams and symbols, measuring current with an ammeter, and how cells and lamps change the current."

OBJECTIVES = {
    "O1": {"sec": "12.1", "code": "7Pe.01, 7Pe.02", "codeNote": "", "t": "Describe electricity as a flow of electrons and classify materials as conductors or insulators."},
    "O2": {"sec": "12.2", "code": "7Pe.05", "codeNote": "", "t": "Explain open and closed circuits and draw circuit diagrams using standard symbols."},
    "O3": {"sec": "12.3", "code": "7Pe.03", "codeNote": "", "t": "Measure current in amperes with an ammeter in series and recognise that current is the same everywhere in a series circuit."},
    "O4": {"sec": "12.4", "code": "7Pe.04", "codeNote": "", "t": "Predict how adding cells or lamps in series changes the current and lamp brightness."},
}

SECTIONS = [
    {"id": "12.1", "title": "Conductors and insulators", "objs": ["O1"]},
    {"id": "12.2", "title": "Electrical circuits", "objs": ["O2"]},
    {"id": "12.3", "title": "Measuring current", "objs": ["O3"]},
    {"id": "12.4", "title": "Changing the current", "objs": ["O4"]},
]

S1_REQ = [
    gd("u12s1r1", "M", "O1", "Conductor or insulator?", ["Type"],
       [("Copper", ["Conductor"]), ("Plastic", ["Insulator"]), ("Rubber", ["Insulator"]), ("Iron", ["Conductor"]), ("Glass", ["Insulator"])], skill="Data"),
    mc("u12s1r2", "M", "O1", "Electricity is a flow of…", ("electrons", "Correct."), [("protons", "No."), ("neutrons", "No."), ("atoms", "No.")]),
    mc("u12s1r3", "M", "O1", "Electrons have a…", ("negative charge", "Correct."), [("positive charge", "Protons."), ("no charge", "Neutrons."), ("magnetic charge", "No.")]),
    ex("u12s1r4", "H", "O1", "Explain why metals are good electrical conductors.",
       [("free electrons", ["free electron|electrons.*free|move"]), ("can flow / carry charge", ["flow|carry|charge"])],
       "Metals have many free electrons that can leave their atoms and move, so they can flow through the metal carrying charge.", need=2),
    tb("u12s1r5", "H", "O1", "Results: does the lamp light when the material bridges the gap? Count the conductors.", ["Material", "Lamp lit?"],
       [["Coin", "yes"], ["Pencil eraser", "no"], ["Steel paperclip", "yes"], ["Wooden lolly stick", "no"], ["Number of conductors", B(2)]], skill="Data"),
    mc("u12s1r6", "H", "O1", "Why are glass insulators used on pylons?", ("To stop current flowing from the cables into the metal poles", "Correct."), [("For decoration", "No."), ("To conduct better", "No."), ("To make light", "No.")]),
    mc("u12s1r7", "H", "O1", "Long overhead cables use aluminium rather than copper because aluminium is…", ("cheaper and lighter", "Correct."), [("a better conductor", "Copper is better."), ("an insulator", "No."), ("magnetic", "No.")]),
    mc("u12s1r8", "VH", "O1", "Why is touching an exposed live wire dangerous?", ("Electrons can flow through your body to the ground, giving a shock.", "Correct."), [("Wires are hot only", "No."), ("Copper is poisonous", "No."), ("It's not dangerous", "It is.")], skill="Reasoning"),
]
S1_PRAC = [
    mc("u12s1p01", "M", "O1", "Atoms contain protons, neutrons and…", "electrons", [("molecules", "No."), ("cells", "No."), ("ions only", "No.")]),
    mc("u12s1p02", "M", "O1", "Insulators…", "stop electricity flowing", [("let electricity flow freely", "Conductors."), ("make electricity", "No."), ("store electricity", "No.")]),
    mc("u12s1p03", "M", "O1", "Which is the best conductor?", "Copper", [("Plastic", "No."), ("Rubber", "No."), ("Wood", "No.")]),
    mc("u12s1p04", "M", "O1", "A plug's cord is covered in plastic because plastic is…", "an insulator", [("a conductor", "No."), ("magnetic", "No."), ("cheap metal", "No.")]),
    mc("u12s1p05", "M", "O1", "Electricians wear rubber gloves because rubber…", "doesn't conduct electricity", [("conducts well", "No."), ("is warm", "No."), ("is magnetic", "No.")]),
    mc("u12s1p06", "H", "O1", "In insulators, electrons are…", "not free to move", [("free to move", "Conductors."), ("missing", "No."), ("positive", "No.")]),
    mc("u12s1p07", "M", "O1", "To test a material, place it…", "in a gap in a simple circuit", [("in water", "No."), ("in a fire", "No."), ("next to a magnet", "No.")]),
    mc("u12s1p08", "H", "O1", "If the lamp lights when a material bridges the gap, the material is…", "a conductor", [("an insulator", "No."), ("a cell", "No."), ("a switch", "No.")]),
    gd("u12s1p09", "M", "O1", "Conductor or insulator?", ["Type"], [("Gold", ["Conductor"]), ("Wood", ["Insulator"]), ("Aluminium foil", ["Conductor"]), ("Rubber band", ["Insulator"])], skill="Data"),
    mc("u12s1p10", "H", "O1", "Building wiring uses copper because…", "it is one of the best conductors", [("it is cheapest", "No."), ("it is an insulator", "No."), ("it is light", "Aluminium is lighter.")]),
    mc("u12s1p11", "M", "O1", "Electrons can be made to flow in…", "one direction around a circuit", [("all directions randomly only", "No."), ("only in insulators", "No."), ("only in a vacuum", "No.")]),
    mc("u12s1p12", "H", "O1", "Why are kettle plugs safe to touch?", "Metal inside carries current; plastic outside insulates", [("They have no metal", "No."), ("Plastic conducts", "No."), ("Electricity is off always", "No.")]),
    mc("u12s1p13", "H", "O1", "Graphite in a pencil lead conducts. It is…", "a non-metal conductor", [("a metal", "No."), ("an insulator", "It conducts."), ("rubber", "No.")], skill="Reasoning"),
    ms("u12s1p14", "H", "O1", "Select ALL electrical insulators.", ["Plastic", "Glass", "Rubber"], [("Copper", "Conductor."), ("Iron", "Conductor.")]),
    mc("u12s1p15", "M", "O1", "The centre of an atom contains…", "protons and neutrons", [("electrons only", "No."), ("nothing", "No."), ("air", "No.")]),
    mc("u12s1p16", "H", "O1", "Pure water is a poor conductor, but tap water conducts a little. Why must you never touch switches with wet hands?", "Water with dissolved substances can conduct, risking a shock", [("Water is an insulator always", "No."), ("Switches melt", "No."), ("It's fine", "No.")], skill="Reasoning"),
    od("u12s1p17", "M", "O1", "Order the steps to test if a material conducts.", ["Build a circuit with a cell, lamp and a gap", "Place the material across the gap", "Observe the lamp", "Record conductor or insulator"]),
    mc("u12s1p18", "M", "O1", "Electricity carries energy to our…", "homes, schools and cars", [("food only", "No."), ("rocks", "No."), ("clouds", "No.")]),
]
S1_ADV = [
    adv(ex("u12s1a1", "VH", "O1", "Design a safe extension cable. Choose materials for the wire and cover, and explain.",
           [("copper wire – good conductor", ["copper|metal|conduct"]), ("plastic/rubber cover – insulator", ["plastic|rubber|insulat"]), ("safety: no shock", ["safe|shock|touch"])],
           "Use copper for the wire because it is an excellent conductor, and cover it with plastic or rubber, which are insulators, so people can touch it without getting a shock.", need=2)),
    adv(mc("u12s1a2", "VH", "O1", "A material lights the lamp only dimly. Best conclusion?", ("It is a conductor, but a poor one (more resistance).", "Correct."), [("It is a perfect insulator", "Lamp lit."), ("The lamp is broken", "Not likely."), ("It is a cell", "No.")], skill="Reasoning")),
    adv(mc("u12s1a3", "VH", "O1", "Why are birds sitting on a single power line not shocked?", ("Current doesn't flow through them – there is no path to the ground or another wire.", "Correct."), [("Feathers are metal", "No."), ("Birds are conductors", "Not the reason."), ("Power lines carry no current", "They do.")], skill="Reasoning")),
    adv(nm("u12s1a4", "VH", "O1", "A test of 30 classroom objects found 12 conductors. What percentage were insulators?", 60, "%")),
]

S2_REQ = [
    mc("u12s2r1", "M", "O2", "A closed circuit is…", ("a complete path, so the lamp lights", "Correct."), [("a circuit with a gap", "Open."), ("a broken lamp", "No."), ("a circuit with no cell", "No.")]),
    mt("u12s2r2", "M", "O2", "Match the component to what it does.", [("Cell", "drives the electrons"), ("Switch", "opens or closes the circuit"), ("Lamp", "gives out light"), ("Ammeter", "measures current"), ("Buzzer", "makes a sound")]),
    gd("u12s2r3", "H", "O2", "Will the lamp light?", ["Lamp"], [("Closed switch, complete loop", ["On"]), ("Open switch", ["Off"]), ("Wire disconnected", ["Off"]), ("Cell missing", ["Off"])], skill="Figure"),
    mc("u12s2r4", "M", "O2", "In the cell symbol, the long line is the…", ("positive terminal", "Correct."), [("negative terminal", "Short line."), ("switch", "No."), ("wire", "No.")]),
    ex("u12s2r5", "H", "O2", "A doorbell circuit has a cell, wires and a buzzer. What is missing and why?",
       [("a switch", ["switch"]), ("so it can be turned on/off / doesn't ring all the time", ["on|off|stop|control|all the time|never stops"])],
       "A switch, so the circuit is only closed when you press it – otherwise the buzzer would never stop.", need=2),
    mc("u12s2r6", "H", "O2", "Two or more cells joined together make…", ("a battery", "Correct."), [("a lamp", "No."), ("a switch", "No."), ("an ammeter", "No.")]),
    tb("u12s2r7", "H", "O2", "Count the components in this list: cell, cell, lamp, switch, buzzer.", ["Component", "Number"],
       [["Cells", B(2)], ["Total components", B(5)]], skill="Data"),
    mc("u12s2r8", "VH", "O2", "Why do scientists use circuit symbols instead of pictures?", ("Symbols are quick, clear and understood worldwide.", "Correct."), [("Pictures are illegal", "No."), ("Symbols are prettier", "No."), ("Symbols show colour", "No.")], skill="Reasoning"),
]
S2_PRAC = [
    mc("u12s2p01", "M", "O2", "If there is a gap in a circuit, it is…", "an open circuit", [("a closed circuit", "No."), ("a battery", "No."), ("a conductor", "No.")]),
    mc("u12s2p02", "M", "O2", "Turning a light switch off…", "opens the circuit", [("closes the circuit", "No."), ("removes the cell", "No."), ("adds a lamp", "No.")]),
    mc("u12s2p03", "M", "O2", "In circuit diagrams, wires are drawn as…", "straight lines", [("wavy lines", "No."), ("circles", "No."), ("dots", "No.")]),
    mc("u12s2p04", "M", "O2", "The short line in the cell symbol is…", "the negative terminal", [("the positive terminal", "Long line."), ("a lamp", "No."), ("a switch", "No.")]),
    mc("u12s2p05", "H", "O2", "Energy in a circuit is transferred from the cell to the lamp…", "electrically through the wires", [("by sound", "No."), ("by magnets", "No."), ("by heating the cell", "No.")]),
    mc("u12s2p06", "M", "O2", "A switch lets us…", "open or close the circuit", [("measure current", "Ammeter."), ("make light", "Lamp."), ("store charge", "Cell.")]),
    mc("u12s2p07", "H", "O2", "A buzzer sounds the moment you press the switch because…", "electricity travels incredibly fast", [("the buzzer is close", "No."), ("sound is fast", "No."), ("the cell is new", "No.")]),
    gd("u12s2p08", "M", "O2", "Open or closed circuit?", ["Circuit"], [("Lamp lit", ["Closed"]), ("Switch off", ["Open"]), ("Broken wire", ["Open"])], skill="Figure"),
    mc("u12s2p09", "H", "O2", "A circle with a cross inside is the symbol for a…", "lamp", [("cell", "No."), ("switch", "No."), ("buzzer", "No.")]),
    mc("u12s2p10", "H", "O2", "A circle with an A inside is the symbol for…", "an ammeter", [("a lamp", "No."), ("a cell", "No."), ("a switch", "No.")]),
    mc("u12s2p11", "M", "O2", "Which component drives the electrons?", "The cell", [("The lamp", "No."), ("The switch", "No."), ("The wire", "No.")]),
    mc("u12s2p12", "H", "O2", "A circuit has a cell, a lamp and an open switch. The lamp is…", "off", [("on", "No."), ("dim", "No."), ("flashing", "No.")]),
    mc("u12s2p13", "H", "O2", "Which order must components be drawn in a single loop?", "Any order, joined in one complete loop", [("Cell must be last", "No."), ("Lamp must be first", "No."), ("Switch must touch the cell", "No.")]),
    od("u12s2p14", "M", "O2", "Order the steps to draw a doorbell circuit diagram.", ["Draw the cell symbol", "Add the buzzer symbol", "Add a switch symbol", "Join them with straight lines into one loop"]),
    mc("u12s2p15", "H", "O2", "Why might a torch not work even with a new cell?", "There may be a break in the circuit", [("New cells never work", "No."), ("Light is too fast", "No."), ("Torches need two switches", "No.")], skill="Reasoning"),
    mc("u12s2p16", "M", "O2", "A battery is…", "two or more cells joined together", [("a single lamp", "No."), ("a switch", "No."), ("a wire", "No.")]),
    gd("u12s2p17", "M", "O2", "Component → job", ["Job"], [("Lamp", ["Light"]), ("Buzzer", ["Sound"]), ("Ammeter", ["Measure current"])], skill="Data"),
    mc("u12s2p18", "H", "O2", "Pressing a doorbell button…", "closes the circuit", [("opens it", "No."), ("removes the cell", "No."), ("adds a lamp", "No.")]),
]
S2_ADV = [
    adv(ex("u12s2a1", "VH", "O2", "Describe how to find a fault in a circuit where the lamp does not light.",
           [("check connections / wires", ["connect|wire|loose|break"]), ("check cell", ["cell|battery"]), ("check/replace lamp or switch", ["lamp|bulb|switch"])],
           "Check every connection for loose or broken wires, test the cell in another circuit, check the switch is closed, and try a new lamp – one at a time.", need=2)),
    adv(mc("u12s2a2", "VH", "O2", "A switch is drawn open, but the lamp is on in the real circuit. What's wrong?", ("The diagram doesn't match the circuit – it should show a closed switch.", "Correct."), [("The lamp is magic", "No."), ("Open switches let current through", "No."), ("Nothing", "No.")], skill="Reasoning")),
    adv(mc("u12s2a3", "VH", "O2", "Why should a buzzer circuit for a safe have the switch on the door?", ("Opening the door closes the circuit, sounding the alarm.", "Correct."), [("To save batteries only", "No."), ("Switches must be on doors", "No."), ("So it never sounds", "No.")], skill="Reasoning")),
    adv(nm("u12s2a4", "VH", "O2", "A battery has 4 cells of 1.5 V each in series. Total voltage?", 6, "V")),
]

S3_REQ = [
    mc("u12s3r1", "M", "O3", "Current is measured in…", ("amperes (A)", "Correct."), [("newtons", "Force."), ("joules", "Energy."), ("volts only", "Not current.")]),
    mc("u12s3r2", "M", "O3", "Current is measured with…", ("an ammeter", "Correct."), [("a thermometer", "No."), ("a force meter", "No."), ("a ruler", "No.")]),
    mc("u12s3r3", "H", "O3", "An ammeter must be connected…", ("in series, in one line with the component", "Correct."), [("on a branch", "No."), ("not connected", "No."), ("only to the switch", "No.")]),
    tb("u12s3r4", "H", "O3", "A series circuit with three lamps. Ammeter A1 reads 0.3 A. Complete.", ["Ammeter", "Reading (A)"],
       [["A1", "0.3"], ["A2", B(0.3)], ["A3", B(0.3)]], skill="Data"),
    ex("u12s3r5", "H", "O3", "Explain why current is not 'used up' by lamps in a series circuit.",
       [("charge keeps flowing / same current everywhere", ["same|keeps flowing|not used|charge"]), ("energy transferred to light and heat", ["energy|light|heat"])],
       "The charge keeps flowing all the way round, so the current is the same everywhere. It is the energy that is transferred to the lamps as light and heat, not the charge.", need=2),
    mc("u12s3r6", "H", "O3", "Conventional current flows from…", ("positive to negative", "Correct."), [("negative to positive", "Electron flow."), ("lamp to switch", "No."), ("nowhere", "No.")]),
    mc("u12s3r7", "H", "O3", "Electrons actually flow from…", ("negative to positive", "Correct."), [("positive to negative", "Conventional."), ("lamp to cell", "No."), ("top to bottom", "No.")]),
    mc("u12s3r8", "VH", "O3", "Ammeters placed before and after a lamp in series read 0.2 A and 0.2 A. What does this show?", ("Current is the same everywhere in a series circuit.", "Correct."), [("The lamp makes current", "No."), ("The ammeters are broken", "No."), ("Current is used up", "No.")], skill="Data"),
]
S3_PRAC = [
    mc("u12s3p01", "M", "O3", "Current is the flow of…", "charge", [("light", "No."), ("heat", "No."), ("mass", "No.")]),
    mc("u12s3p02", "M", "O3", "The symbol for amperes is…", "A", [("N", "Newtons."), ("J", "Joules."), ("V", "Volts.")]),
    mc("u12s3p03", "M", "O3", "'Amps' is short for…", "amperes", [("amplifiers", "No."), ("ammeters", "No."), ("amplitudes", "No.")]),
    mc("u12s3p04", "H", "O3", "Current tells us how much charge flows past a point…", "every second", [("every hour", "No."), ("in total", "No."), ("in a year", "No.")]),
    mc("u12s3p05", "H", "O3", "The red terminal of an ammeter connects towards…", "the positive end of the cell", [("the negative end", "No."), ("the lamp only", "No."), ("anywhere", "No.")]),
    mc("u12s3p06", "M", "O3", "In series means…", "in one continuous line with no branches", [("on a branch", "No."), ("in a circle drawing", "No."), ("disconnected", "No.")]),
    nm("u12s3p07", "H", "O3", "In a series circuit one ammeter reads 0.45 A. What does a second ammeter in the same circuit read?", 0.45, "A"),
    mc("u12s3p08", "H", "O3", "Why do we still use 'conventional current'?", "Scientists defined it before electrons were discovered", [("It's the electron direction", "No."), ("It is faster", "No."), ("It's a mistake to fix", "Still used.")]),
    gd("u12s3p09", "M", "O3", "Quantity and its unit", ["Unit"], [("Current", ["A"]), ("Force", ["N"]), ("Energy", ["J"])], skill="Data"),
    mc("u12s3p10", "H", "O3", "In a lamp, energy is transferred as…", "light and heat", [("charge", "Charge keeps flowing."), ("mass", "No."), ("sound only", "No.")]),
    mc("u12s3p11", "M", "O3", "Which instrument would you put in series to find the current through a buzzer?", "Ammeter", [("Thermometer", "No."), ("Force meter", "No."), ("Balance", "No.")]),
    nm("u12s3p12", "H", "O3", "Convert 250 mA to amps (1 A = 1000 mA).", 0.25, "A"),
    mc("u12s3p13", "H", "O3", "Electrons flow from negative to positive, which is…", "opposite to conventional current", [("the same as conventional current", "No."), ("not possible", "No."), ("only in insulators", "No.")]),
    mc("u12s3p14", "H", "O3", "An ammeter shows 0 A. The most likely reason is…", "the circuit is open", [("the lamp is very bright", "No."), ("the cell is new", "No."), ("too much current", "No.")], skill="Reasoning"),
    od("u12s3p15", "M", "O3", "Order the steps to measure current through a lamp.", ["Switch off / open the circuit", "Break the circuit next to the lamp", "Connect the ammeter in series in the gap", "Close the switch and read the ammeter"]),
    mc("u12s3p16", "M", "O3", "In a series circuit, the current is…", "the same everywhere", [("biggest near the cell", "No."), ("zero after each lamp", "No."), ("used up by lamps", "No.")]),
    nm("u12s3p17", "H", "O3", "Convert 0.6 A to milliamps.", 600, "mA"),
    mc("u12s3p18", "H", "O3", "An ammeter placed between two lamps in series reads the same as one next to the cell because…", "charge is not used up", [("lamps create charge", "No."), ("the ammeter is broken", "No."), ("current is faster there", "No.")]),
]
S3_ADV = [
    adv(ex("u12s3a1", "VH", "O3", "A student connects an ammeter on a separate branch and gets a strange reading. What did she do wrong and how should she fix it?",
           [("ammeter must be in series", ["series"]), ("one line / no branches / break circuit and insert", ["line|branch|insert|gap|break"])],
           "The ammeter must be in series – in one continuous line with the component. She should break the circuit next to the lamp and connect the ammeter in the gap.", need=2)),
    adv(mc("u12s3a2", "VH", "O3", "Two students read ammeters in the same series circuit: 0.30 A and 0.28 A. Best explanation?", ("Small measurement differences between instruments; the true current is the same.", "Correct."), [("Current was used up", "No."), ("Lamp made current", "No."), ("Both are exact", "No.")], skill="Reasoning")),
    adv(nm("u12s3a3", "VH", "O3", "A current of 2 A flows for 5 s. How many coulombs of charge pass a point? (charge = current × time)", 10, "C")),
    adv(mc("u12s3a4", "VH", "O3", "Why does the direction of conventional current not matter for most circuit calculations?", ("The size of the current is the same either way.", "Correct."), [("Current has no direction", "No."), ("Electrons don't move", "No."), ("It always matters", "No.")], skill="Reasoning")),
]

S4_REQ = [
    mc("u12s4r1", "M", "O4", "Adding a second cell in series makes the lamp…", ("brighter – more current flows", "Correct."), [("dimmer", "No."), ("go out", "No."), ("the same", "No.")]),
    mc("u12s4r2", "M", "O4", "Adding a second lamp in series makes each lamp…", ("dimmer – more resistance, less current", "Correct."), [("brighter", "No."), ("the same", "No."), ("explode", "No.")]),
    gr("u12s4r3", "H", "O4", "Data: number of cells and current. Plot the points.", {"label": "Number of cells", "min": 0, "max": 4, "step": 1}, {"label": "Current (A)", "min": 0, "max": 0.8, "step": 0.2},
       [[1, 0.2], [2, 0.4], [3, 0.6]], skill="Data"),
    tb("u12s4r4", "H", "O4", "Data: lamps in series and current (1 cell). Complete the pattern.", ["Lamps", "Current (A)"],
       [["1", "0.6"], ["2", "0.3"], ["3", B(0.2)]], skill="Data"),
    ex("u12s4r5", "H", "O4", "Explain why adding more lamps in series makes them dimmer.",
       [("more resistance", ["resist"]), ("less current", ["less current|current.*(less|decreas|smaller)"])],
       "Each lamp adds resistance, making it harder for electrons to flow. More resistance means less current, so each lamp is dimmer.", need=2),
    mc("u12s4r6", "H", "O4", "Why can too many cells be a problem?", ("Too much current can damage the lamp.", "Correct."), [("Cells cancel out", "No."), ("Lamps get dimmer", "No."), ("Nothing happens", "No.")]),
    gd("u12s4r7", "H", "O4", "Brighter, dimmer or same than one cell + one lamp?", ["Brightness"],
       [("2 cells, 1 lamp", ["Brighter"]), ("1 cell, 2 lamps", ["Dimmer"]), ("2 cells, 2 lamps", ["Same"])], skill="Data"),
    mc("u12s4r8", "VH", "O4", "How are the ISS's circuits powered?", ("Solar cells absorb energy from sunlight", "Correct."), [("Petrol generators", "No."), ("Wind turbines", "No."), ("Burning coal", "No.")], skill="Knowledge"),
]
S4_PRAC = [
    mc("u12s4p01", "M", "O4", "Cells provide the ___ that moves charges.", "push", [("light", "No."), ("resistance", "No."), ("gap", "No.")]),
    mc("u12s4p02", "M", "O4", "Lamps make it harder for electrons to flow. This is…", "resistance", [("current", "No."), ("voltage", "No."), ("charge", "No.")]),
    mc("u12s4p03", "M", "O4", "More resistance means…", "less current", [("more current", "No."), ("the same current", "No."), ("no lamps", "No.")]),
    mc("u12s4p04", "M", "O4", "More cells in series means…", "more current", [("less current", "No."), ("no change", "No."), ("more resistance", "No.")]),
    nm("u12s4p05", "H", "O4", "1 cell gives 0.25 A. Predict the current with 2 identical cells (same lamp).", 0.5, "A"),
    nm("u12s4p06", "H", "O4", "1 lamp: 0.4 A. Predict with 2 identical lamps in series (same cell).", 0.2, "A"),
    mc("u12s4p07", "H", "O4", "Astronauts lose muscle strength in space because…", "there is no gravity to work against", [("they eat too much", "No."), ("electricity", "No."), ("cold", "No.")]),
    mc("u12s4p08", "H", "O4", "Electrical muscle stimulation uses…", "controlled electric currents to make muscles work", [("magnets", "No."), ("sound", "No."), ("light", "No.")]),
    gd("u12s4p09", "M", "O4", "Current goes up or down?", ["Change"], [("Add a cell", ["Up"]), ("Add a lamp", ["Down"]), ("Remove a lamp", ["Up"])], skill="Data"),
    mc("u12s4p10", "H", "O4", "Doctors already use electrical muscle stimulation to help…", "injured and elderly patients", [("plants grow", "No."), ("fix computers", "No."), ("make food", "No.")]),
    mc("u12s4p11", "M", "O4", "To make a torch brighter, you could…", "add another cell in series", [("add another lamp in series", "Dimmer."), ("remove the cell", "No."), ("open the switch", "No.")]),
    mc("u12s4p12", "H", "O4", "Two lamps in series. One breaks. The other…", "goes out – the circuit is open", [("gets brighter", "No."), ("stays the same", "No."), ("flashes", "No.")], skill="Reasoning"),
    mc("u12s4p13", "H", "O4", "Which gives the brightest lamps?", "3 cells, 1 lamp", [("1 cell, 3 lamps", "Dimmest."), ("1 cell, 1 lamp", "Middle."), ("2 cells, 2 lamps", "Middle.")], skill="Reasoning"),
    od("u12s4p14", "M", "O4", "Order by current, smallest first (same lamps and cells).", ["1 cell, 3 lamps", "1 cell, 2 lamps", "1 cell, 1 lamp", "2 cells, 1 lamp"]),
    mc("u12s4p15", "M", "O4", "Every room on the ISS has circuits for…", "life support and communication", [("cooking only", "No."), ("gravity", "No."), ("making air from rock", "No.")]),
    mc("u12s4p16", "H", "O4", "Why is a dimmer lamp evidence of less current?", "Less charge flows each second, transferring less energy", [("The lamp is bigger", "No."), ("Current is used up", "No."), ("Light is slower", "No.")]),
    nm("u12s4p17", "H", "O4", "With 3 cells, current is 0.9 A. Current with 1 cell (same lamp)?", 0.3, "A"),
    mc("u12s4p18", "M", "O4", "Electric current can do far more than…", "light a lamp", [("exist", "No."), ("flow", "No."), ("be measured", "No.")]),
]
S4_ADV = [
    adv(ex("u12s4a1", "VH", "O4", "Plan an investigation into how the number of lamps in series affects the current.",
           [("change number of lamps", ["lamp"]), ("measure current with ammeter in series", ["ammeter|current"]), ("keep cells/wires same", ["same|control|cells"])],
           "Change the number of identical lamps (1, 2, 3). Measure the current with an ammeter in series each time. Keep the cells and wires the same, and repeat readings.", need=2)),
    adv(mc("u12s4a2", "VH", "O4", "The cells-and-current graph is a straight line through the origin. This means…", ("current is proportional to the number of cells", "Correct."), [("current decreases", "No."), ("there's no pattern", "No."), ("cells add resistance", "No.")], skill="Data")),
    adv(nm("u12s4a3", "VH", "O4", "1 cell + 1 lamp gives 0.6 A. Predict 2 cells + 3 lamps (identical).", 0.4, "A")),
    adv(mc("u12s4a4", "VH", "O4", "Why would extra cells be risky in the electrical muscle stimulation device?", ("More current could harm the body; the current must be controlled.", "Correct."), [("Muscles block current", "No."), ("Cells would be dimmer", "No."), ("No reason", "No.")], skill="Reasoning")),
]

POOLS = {"12.1": (S1_REQ, S1_PRAC, S1_ADV), "12.2": (S2_REQ, S2_PRAC, S2_ADV), "12.3": (S3_REQ, S3_PRAC, S3_ADV), "12.4": (S4_REQ, S4_PRAC, S4_ADV)}

STOPS = {
    "12.1": [stop("u12v1a", "This flow of electrons is electricity", mc("u12v1a_q", "M", "O1", "Electrons carry a…", "negative charge", [("positive charge", "Protons."), ("no charge", "Neutrons."), ("magnetic pole", "No.")])),
             stop("u12v1b", "a metal coin lights the lamp", mc("u12v1b_q", "M", "O1", "Which is an insulator?", "Rubber", [("Copper", "No."), ("Gold", "No."), ("Iron", "No.")])),
             stop("u12v1c", "which is cheaper and lighter", mc("u12v1c_q", "H", "O1", "Why do electricians wear rubber-soled shoes?", "Rubber doesn't conduct electricity", [("Rubber is a conductor", "No."), ("For comfort only", "No."), ("Rubber is magnetic", "No.")]))],
    "12.2": [stop("u12v2a", "opens the circuit", mc("u12v2a_q", "M", "O2", "A complete path for electrons is…", "a closed circuit", [("an open circuit", "No."), ("an insulator", "No."), ("a gap", "No.")])),
             stop("u12v2b", "Wires are drawn as straight lines", mc("u12v2b_q", "H", "O2", "In the cell symbol, the long line is…", "positive", [("negative", "Short line."), ("a switch", "No."), ("a lamp", "No.")]))],
    "12.3": [stop("u12v3a", "from negative to positive!", mc("u12v3a_q", "M", "O3", "Current is measured in…", "amperes", [("newtons", "No."), ("joules", "No."), ("grams", "No.")])),
             stop("u12v3b", "but the charge keeps flowing", mc("u12v3b_q", "H", "O3", "In a series circuit, the current is…", "the same everywhere", [("used up by each lamp", "No."), ("biggest at the end", "No."), ("zero", "No.")]))],
    "12.4": [stop("u12v4a", "each lamp is dimmer than a single lamp", mc("u12v4a_q", "M", "O4", "Adding a second cell in series makes a lamp…", "brighter", [("dimmer", "No."), ("go out", "No."), ("the same", "No.")])),
             stop("u12v4b", "Electric current can do far more than light a lamp!", mc("u12v4b_q", "H", "O4", "What powers the ISS's circuits?", "Solar cells", [("Coal", "No."), ("Wind", "No."), ("Tides", "No.")]))],
}

MINDMAP = {"id": "root", "t": "Electricity", "sec": None, "kids": [
    {"id": "ci", "t": "Conductors and insulators", "d": "Electricity = flow of electrons • metals have free electrons • plastic, glass, rubber insulate • safety.", "obj": "O1", "sec": "12.1"},
    {"id": "cc", "t": "Circuits", "d": "Closed vs open • cell, battery, lamp, switch, ammeter, buzzer symbols • long line = positive.", "obj": "O2", "sec": "12.2"},
    {"id": "mc", "t": "Measuring current", "d": "Amperes (A) • ammeter in series • conventional current + → − • same current everywhere in series.", "obj": "O3", "sec": "12.3"},
    {"id": "ch", "t": "Changing the current", "d": "More cells → more current, brighter • more lamps → more resistance, dimmer • ISS, muscle stimulation.", "obj": "O4", "sec": "12.4"},
]}
