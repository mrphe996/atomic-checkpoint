from science_v2.k import Unit
U = Unit("s5u05")
U.q("R", "5.1", "O1", 'A book rests on a table. What force pushes up on it?', ('The normal (support) force from the table', 'It balances gravity.'), [('Gravity', 'Gravity pulls down.'), ('No force', 'The table pushes up.')], d="M")
U.q("R", "5.2", "O2", 'What keeps a satellite moving around the Earth?', ('Gravity', 'Gravity pulls it towards the Earth as it moves.'), [('Wind', 'There is no wind in space.'), ('Magnets', 'Gravity keeps it in orbit.')], d="M")
U.q("P", "5.3", "O3", 'A parachute opens. What happens to the speed of the skydiver?', ('It slows down', 'Air resistance increases.'), [('It speeds up', 'The parachute slows them.'), ('It stops in mid-air', 'It slows, but does not stop.')], d="M")
U.q("P", "5.4", "O4", 'Two teams pull a rope with equal force. What happens?', ('The rope does not move', 'Balanced forces cancel out.'), [('The rope moves left', 'The forces are equal.'), ('The rope breaks', 'Equal forces do not make it move.')], d="M")
U.q("R", "5.5", "O5", 'Which object is attracted to a magnet?', ('An iron nail', 'Iron is magnetic.'), [('A plastic spoon', 'Plastic is not magnetic.'), ('A gold ring', 'Gold is not magnetic.')], d="M")
U.q("F", "5.6", "O6", 'How could you test which magnet is strongest?', ('Count how many paper clips each one holds in a chain', 'More clips means a stronger magnet.'), [('Look at the colour', 'Colour does not show strength.'), ('Weigh the magnets', 'Heavier is not always stronger.')], d="M")
V2 = U.V2
