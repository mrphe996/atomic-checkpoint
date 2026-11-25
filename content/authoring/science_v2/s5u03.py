from science_v2.k import Unit
U = Unit("s5u03")
U.q("E", "3.1", "O1", 'Joe says an empty bottle has nothing in it. Is he right?', ('No – it is full of air', 'Air is a gas and takes up space.'), [('Yes', 'Air fills the bottle.'), ('Yes, until you put water in', 'Air is already there.')], d="M")
U.q("R", "3.2", "O2", 'At what temperature does pure water boil?', ('100 °C', 'Water boils at 100 °C.'), [('0 °C', 'That is when it freezes.'), ('50 °C', 'It boils at 100 °C.')], d="M")
U.q("P", "3.3", "O3", 'Wet clothes hang outside on a warm, windy day. What happens?', ('They dry quickly', 'Warmth and wind speed up evaporation.'), [('They stay wet', 'Water evaporates.'), ('They get wetter', 'They dry.')], d="M")
U.q("R", "3.4", "O5", 'Salt is dissolved in water. How can you get the salt back?', ('Let the water evaporate', 'The salt is left behind.'), [('Filter it', 'Dissolved salt passes through a filter.'), ('Freeze it', 'Freezing does not separate it.')], d="M")
V2 = U.V2
