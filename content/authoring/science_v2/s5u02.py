from science_v2.k import Unit
U = Unit("s5u02")
U.q("R", "2.1", "O1", 'All sounds are made by…', ('vibrations', 'Something must vibrate to make sound.'), [('light', 'Light does not make sound.'), ('colours', 'Colours do not make sound.')], d="M")
U.q("R", "2.2", "O2", 'A big drum is hit softly. What changes if it is hit hard?', ('The sound is louder', 'Harder hits make bigger vibrations.'), [('The pitch is higher', 'Pitch depends on size and tightness.'), ('Nothing', 'The volume changes.')], d="M")
U.q("P", "2.3", "O3", 'You walk away from a radio. What happens to the sound?', ('It gets quieter', 'Sound spreads out as it travels.'), [('It gets louder', 'It gets quieter.'), ('It stays the same', 'Distance makes it quieter.')], d="M")
U.q("P", "2.4", "O5", 'A guitar string is made tighter. What happens to the pitch?', ('It gets higher', 'Tighter strings vibrate faster.'), [('It gets lower', 'Looser strings give lower notes.'), ('No change', 'Tightness changes the pitch.')], d="M")
V2 = U.V2
