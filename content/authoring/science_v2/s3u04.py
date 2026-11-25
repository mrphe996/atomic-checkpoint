from science_v2.k import Unit
U = Unit("s3u04")
U.q("R", "4.1", "O1", 'Which organ pumps blood around the body?', ('The heart', 'The heart is a pump.'), [('The lungs', 'Lungs help us breathe.'), ('The brain', 'The brain controls the body.')], d="M")
U.q("E", "4.2", "O2", 'Jo says a frog is a fish because it lives in water when young. Is she right?', ('No – frogs are amphibians', 'They live in water when young and on land as adults.'), [('Yes', 'Fish stay in water all their lives.'), ('No – frogs are reptiles', 'Frogs have moist skin, not scales.')], d="M")
U.q("P", "4.3", "O3", 'In the chain grass → rabbit → fox, what happens to the foxes if all the grass dies?', ('They will have less food and may fall in number', 'The rabbits lose their food first.'), [('Nothing', 'Every link depends on the one before.'), ('More foxes', 'There will be fewer rabbits to eat.')], d="M")
U.q("R", "4.4", "O4", 'What can fossils tell us?', ('What living things were like long ago', 'Fossils are remains of very old life.'), [("Tomorrow's weather", 'Fossils are about the past.'), ('How old you are', 'Fossils are millions of years old.')], d="M")
V2 = U.V2
