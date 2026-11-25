from science_v2.k import Unit
U = Unit("s3u01")
U.q("E", "1.1", "O1", 'Ella says a car is alive because it moves. Is she right?', ('No – a car does not grow, feed or have young', 'Living things do all of these.'), [('Yes', 'Moving is not enough to be alive.'), ('Yes, because it makes a noise', 'Noise does not make something alive.')], d="M")
U.q("P", "1.2", "O2", 'Which part of a plant takes in water from the soil?', ('The roots', 'Roots take in water.'), [('The flower', 'Flowers make seeds.'), ('The leaves', 'Leaves make food using light.')], d="M")
U.q("P", "1.3", "O3", 'A plant is kept in a dark cupboard for two weeks. What will it look like?', ('Pale and weak', 'Plants need light to stay healthy and green.'), [('Greener and stronger', 'Plants need light.'), ('Exactly the same', 'Light makes a difference.')], d="M")
U.q("F", "1.4", "O4", 'To test if plants need water, what should be different for the two plants?', ('Only the amount of water', 'Everything else stays the same to make it fair.'), [('The amount of light and water', 'Two changes make it unfair.'), ('Nothing', 'Then there is nothing to compare.')], d="M")
V2 = U.V2
