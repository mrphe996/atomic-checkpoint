from science_v2.k import Unit
U = Unit("s5u04")
U.q("P", "4.1", "O1", 'After you swallow food, where does it go next?', ('Down the oesophagus to the stomach', 'The food tube leads to the stomach.'), [('Straight to the lungs', 'Food goes to the stomach.'), ('To the heart', 'Food does not go to the heart.')], d="M")
U.q("E", "4.2", "O3", 'Ben eats only crisps and sweets. Why is this unhealthy?', ('He is not getting a balanced diet', 'He needs protein, vitamins and fibre too.'), [('It is healthy', 'Crisps and sweets lack many nutrients.'), ('Crisps have too much protein', 'They are mostly fat and salt.')], d="M")
V2 = U.V2
