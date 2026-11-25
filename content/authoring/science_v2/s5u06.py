from science_v2.k import Unit
U = Unit("s5u06")
U.q("R", "6.1", "O1", 'How long does the Earth take to orbit the Sun?', ('About one year', 'The Earth goes round the Sun once a year.'), [('One day', 'One day is one spin.'), ('One month', 'The Moon orbits the Earth in about a month.')], d="M")
U.q("E", "6.2", "O2", 'Lia says it is summer because the Earth is closest to the Sun. What is the better reason?', ('The Earth is tilted, so our part leans towards the Sun', 'The tilt causes the seasons.'), [('She is right', 'Distance is not the main cause.'), ('The Sun gets bigger', 'The Sun stays the same size.')], d="M")
U.q("R", "6.3", "O4", 'Why do cacti have spines instead of wide leaves?', ('Spines lose less water', 'Deserts are very dry.'), [('To look scary', 'They save water.'), ('To catch rain', 'Spines save water.')], d="M")
U.q("R", "6.4", "O5", 'Why do rabbits have eyes on the sides of their heads?', ('To see predators coming from many directions', 'It helps them escape.'), [('To see colours better', 'It is about seeing all around.'), ('To hunt other animals', 'Rabbits eat plants.')], d="M")
V2 = U.V2
