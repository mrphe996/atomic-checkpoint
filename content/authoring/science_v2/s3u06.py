from science_v2.k import Unit
U = Unit("s3u06")
U.q("R", "6.1", "O1", 'Which one is a star?', ('The Sun', 'The Sun is our closest star.'), [('The Moon', 'The Moon goes round the Earth.'), ('The Earth', 'The Earth is a planet.')], d="M")
U.q("E", "6.2", "O2", 'Ali says the Moon makes its own light. Is he right?', ('No – it reflects light from the Sun', 'The Moon has no light of its own.'), [('Yes', 'The Moon reflects sunlight.'), ('Yes, only at night', 'It always reflects sunlight.')], d="M")
U.q("P", "6.3", "O3", 'The Moon looks full tonight. About how long until it looks full again?', ('About a month (about 29 days)', 'The phases repeat each month.'), [('One day', 'The phases change slowly.'), ('One year', 'It is much faster than a year.')], d="M")
V2 = U.V2
