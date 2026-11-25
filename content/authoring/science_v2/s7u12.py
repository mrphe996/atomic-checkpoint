from science_v2.k import Unit
U = Unit("s7u12")

U.q("R", "12.1", "O1", "Why are electric wires covered in plastic?", ("Plastic is an insulator, so it stops current reaching us", "The copper inside conducts; the plastic protects."), [("Plastic helps the current flow", "Plastic does not conduct."), ("To make the wires heavier", "Safety is the reason.")])
U.q("P", "12.2", "O2", "In a series circuit with two lamps, one lamp breaks. What happens to the other?", ("It goes out", "A series circuit has only one path; a break stops all current."), [("It gets brighter", "No current can flow."), ("It stays the same", "The circuit is broken.")])
U.q("F", "12.3", "O3", "How should an ammeter be connected to measure the current through a lamp?", ("In series with the lamp", "All the current must flow through the ammeter."), [("In parallel with the lamp", "That is how a voltmeter is connected."), ("Anywhere, not connected to the circuit", "It must be part of the circuit.")])
U.q("P", "12.4", "O4", "A second cell is added to a series circuit with one lamp. What happens?", ("The current increases and the lamp is brighter", "More cells push more current."), [("The lamp is dimmer", "More cells give more current."), ("Nothing changes", "The current changes.")])
V2 = U.V2
