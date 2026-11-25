from science_v2.k import Unit
U = Unit("s3u02")
U.q("R", "2.1", "O1", 'Which one is a liquid?', ('Milk', 'Milk pours and takes the shape of its container.'), [('A stone', 'A stone is a solid.'), ('Steam', 'Steam is a gas.')], d="M")
U.q("F", "2.2", "O2", 'How could you separate paper clips from sand?', ('Use a magnet', 'Steel paper clips are magnetic; sand is not.'), [('Add water', 'Neither dissolves.'), ('Shake them', 'They would stay mixed.')], d="M")
U.q("P", "2.3", "O3", 'Sugar is stirred into warm water. What happens?', ('It dissolves and seems to disappear', 'The sugar is still there – the water tastes sweet.'), [('It floats on top', 'Sugar dissolves.'), ('It turns into sand', 'Sugar does not change into sand.')], d="M")
U.q("E", "2.4", "O4", 'Tom pours salty water through a filter paper. He says the salt is caught in the paper. Is he right?', ('No – dissolved salt passes through the filter', 'Filters only catch solid bits that are not dissolved.'), [('Yes', 'Dissolved salt goes through.'), ('Yes, and the water is caught too', 'Water passes through.')], d="M")
U.q("R", "2.5", "O5", 'How can you get salt out of rock salt?', ('Dissolve it, filter out the rock, then let the water evaporate', 'Each step removes something.'), [('Use a magnet', 'Salt is not magnetic.'), ('Put it in the freezer', 'Freezing does not separate it.')], d="M")
V2 = U.V2
