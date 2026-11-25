from science_v2.k import Unit
U = Unit("s9u12")

U.q("R", "12.1", "O1", "What is electric current?", ("A flow of charge (electrons) round a circuit", "It is measured in amps."), [("A store of energy in the cell", "That is chemical energy."), ("The push from the cell", "That is the voltage.")])
U.q("P", "12.2", "O2", "In a series circuit the current at one point is 0.3 A. What is the current at another point in the same loop?", ("0.3 A", "Current is the same everywhere in a series circuit."), [("0.6 A", "Current is not doubled."), ("0.15 A", "Current is not shared in series.")])
U.q("P", "12.3", "O3", "In a parallel circuit, one lamp breaks. What happens to the other lamp?", ("It stays lit", "It is on its own complete path."), [("It goes out", "That is a series circuit."), ("It explodes", "It keeps working normally.")])
U.q("R", "12.4", "O4", "Two 1.5 V cells are joined in series the same way round. What is the total voltage?", ("3 V", "Voltages add in series."), [("1.5 V", "They add together."), ("0 V", "That would be if they faced opposite ways.")])
U.q("E", "12.5", "O5", "A longer wire is used in a circuit and the lamp dims. Ben says the wire used up the current. What is the better explanation?", ("The longer wire has more resistance, so less current flows", "Current is not used up."), [("He is right", "Current is the same all round a series circuit."), ("The lamp got older", "The wire change caused it.")])
V2 = U.V2
