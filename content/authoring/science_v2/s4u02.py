from science_v2.k import Unit
U = Unit("s4u02")
U.q("R", "2.1", "O1", 'Which one gives us light energy?', ('A lamp', 'A lamp gives out light.'), [('A stone', 'A stone does not give out light.'), ('A spoon', 'A spoon does not give out light.')], d="M")
U.q("P", "2.2", "O2", 'A hot drink is left on the table. What happens to its energy?', ('It moves to the air around it and the drink cools', 'Energy moves from hot to cold.'), [('It stays in the cup', 'The drink cools down.'), ('It gets hotter', 'It cools.')], d="M")
U.q("R", "2.3", "O3", 'A torch changes energy from the battery into…', ('light (and some heat)', 'The bulb gives out light.'), [('sound only', 'A torch mainly gives light.'), ('food', 'Torches do not make food.')], d="M")
U.q("R", "2.4", "O4", 'Where do plants get their energy from?', ('Sunlight', 'Plants use light to make food.'), [('The soil', 'Soil gives water and minerals, not energy.'), ('Animals', 'Plants make their own food.')], d="M")
V2 = U.V2
