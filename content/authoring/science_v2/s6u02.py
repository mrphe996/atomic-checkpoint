from science_v2.k import Unit
U = Unit("s6u02")
U.q("R", "2.1", "O1", 'Which property tells us a material is hard?', ('It is difficult to scratch', 'Hard materials resist scratching.'), [('It is shiny', 'Shiny is a different property.'), ('It is see-through', 'See-through is a different property.')], d="M")
U.q("P", "2.2", "O3", 'A metal spoon and a plastic spoon are put in hot water. Which handle feels hot first?', ('The metal spoon', 'Metal is a thermal conductor.'), [('The plastic spoon', 'Plastic is an insulator.'), ('Both at once', 'They are different materials.')], d="M")
U.q("E", "2.3", "O5", 'Kim says melting ice is a chemical change. Is she right?', ('No – it is reversible: the water can freeze again', 'No new substance is made.'), [('Yes', 'Melting is reversible.'), ('Yes, because it gets wet', 'Wetness does not make it chemical.')], d="M")
U.q("R", "2.4", "O7", 'Which is a sign of a chemical reaction?', ('Bubbles of a new gas when vinegar meets baking soda', 'A new substance forms.'), [('Ice melting', 'That is a reversible change.'), ('Sugar dissolving', 'That is reversible.')], d="M")
V2 = U.V2
