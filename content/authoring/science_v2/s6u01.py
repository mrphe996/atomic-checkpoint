from science_v2.k import Unit
U = Unit("s6u01")
U.q("R", "1.1", "O1", "What does blood carry to the body's cells?", ('Oxygen and food', 'Blood delivers what cells need.'), [('Only water', 'Blood carries much more.'), ('Bones', 'Bones do not travel in blood.')], d="M")
U.q("P", "1.2", "O3", 'You run fast for two minutes. What happens to your breathing?', ('It gets faster and deeper', 'Your muscles need more oxygen.'), [('It slows down', 'Exercise speeds up breathing.'), ('It stops', 'You keep breathing.')], d="M")
U.q("R", "1.3", "O5", 'Which changes happen during puberty?', ('The body grows and starts to become an adult', 'Puberty prepares the body for adulthood.'), [('You get shorter', 'You grow.'), ('Nothing changes', 'Many changes happen.')], d="M")
U.q("E", "1.4", "O6", 'Max says you can catch every disease from other people. Is he right?', ('No – some diseases are not infectious, such as some caused by an unhealthy diet', 'Only infectious diseases spread.'), [('Yes', 'Some diseases do not spread.'), ('No – no disease spreads', 'Colds and flu spread.')], d="M")
V2 = U.V2
