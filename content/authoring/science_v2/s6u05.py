from science_v2.k import Unit
U = Unit("s6u05")
U.q("E", "5.1", "O1", 'Tia says her mass would be smaller on the Moon. Is she right?', ('No – her mass stays the same; her weight is smaller', 'Weight depends on gravity.'), [('Yes', 'Mass does not change.'), ('No – her mass would be bigger', 'Mass does not change.')], d="M")
U.q("P", "5.2", "O3", 'You squeeze a soft ball. What can a force do to it?', ('Change its shape', 'Forces can change shape, speed and direction.'), [('Nothing', 'Forces have effects.'), ('Make it heavier', 'Squeezing does not add mass.')], d="M")
U.q("P", "5.3", "O4", 'A ball of clay sinks. The same clay is made into a boat shape. What happens?', ('It can float', 'A wider shape pushes aside more water, giving more upthrust.'), [('It still sinks', 'The shape changes the upthrust.'), ('It gets heavier', 'Its mass is the same.')], d="M")
U.q("R", "5.4", "O6", 'In a circuit diagram, what does a long line and a short line side by side mean?', ('A cell', 'It is the symbol for a cell.'), [('A bulb', 'A bulb is a circle with a cross.'), ('A switch', 'A switch is a break with a lever.')], d="M")
V2 = U.V2
