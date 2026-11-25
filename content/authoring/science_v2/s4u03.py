from science_v2.k import Unit
U = Unit("s4u03")
U.q("R", "3.1", "O1", 'In which state are the particles closest together?', ('Solid', 'Solid particles are packed tightly.'), [('Gas', 'Gas particles are far apart.'), ('Liquid', 'Liquid particles can slide past each other.')], d="M")
U.q("P", "3.2", "O2", 'Water is poured from a tall glass into a wide bowl. What happens to its shape?', ('It takes the shape of the bowl', 'Liquids flow.'), [('It keeps the glass shape', 'Liquids do not keep their shape.'), ('It turns solid', 'It stays liquid.')], d="M")
U.q("P", "3.3", "O3", 'Chocolate is left in the hot sun. What happens?', ('It melts', 'Heat changes solid to liquid.'), [('It freezes', 'Freezing needs cold.'), ('Nothing', 'Heat melts chocolate.')], d="M")
U.q("E", "3.4", "O4", 'Burnt toast cannot become bread again. Why?', ('Burning is a chemical change that makes new substances', 'It cannot be reversed.'), [('Because it is cold', 'Temperature is not the reason.'), ('It can change back', 'It cannot be reversed.')], d="M")
V2 = U.V2
