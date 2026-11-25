from science_v2.k import Unit
U = Unit("s4u06")
U.q("R", "6.1", "O1", 'Which material conducts electricity?', ('Copper', 'Metals are conductors.'), [('Plastic', 'Plastic is an insulator.'), ('Wood', 'Wood is an insulator.')], d="M")
U.q("E", "6.2", "O2", 'Why should you never touch a switch with wet hands?', ('Water with things dissolved in it can conduct electricity', 'You could get a shock.'), [('Water is an insulator', 'Tap water can conduct.'), ('It makes the switch rusty', 'The danger is a shock.')], d="M")
U.q("R", "6.3", "O3", 'Why are plugs covered in plastic?', ('Plastic is an insulator, so it keeps us safe', 'Electricity cannot pass through plastic easily.'), [('Plastic conducts', 'Plastic is an insulator.'), ('To make them heavy', 'It is for safety.')], d="M")
U.q("P", "6.4", "O4", 'The switch in a circuit is opened. What happens to the bulb?', ('It goes out', 'The circuit is broken.'), [('It gets brighter', 'No current flows.'), ('It stays on', 'An open switch breaks the circuit.')], d="M")
U.q("P", "6.5", "O5", 'A second bulb is added in a line with the first. What happens?', ('Both bulbs are dimmer', 'The same cell is shared by more bulbs.'), [('Both are brighter', 'More bulbs make them dimmer.'), ('Nothing', 'Adding a bulb changes the brightness.')], d="M")
V2 = U.V2
