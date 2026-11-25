from science_v2.k import Unit
U = Unit("s4u01")
U.q("R", "1.1", "O1", 'Which bone protects the brain?', ('The skull', 'The skull is like a hard helmet.'), [('The ribs', 'Ribs protect the heart and lungs.'), ('The femur', 'The femur is in the leg.')], d="M")
U.q("P", "1.2", "O2", 'What would happen to a person without a skeleton?', ('They could not stand up or keep their shape', 'The skeleton supports the body.'), [('Nothing', 'The skeleton holds us up.'), ('They would be taller', 'They could not stand at all.')], d="M")
U.q("R", "1.3", "O3", 'How do muscles move bones?', ('They contract and pull on the bones', 'Muscles can only pull.'), [('They push bones', 'Muscles pull, they do not push.'), ('They melt', 'Muscles contract and relax.')], d="M")
U.q("E", "1.4", "O4", 'Lin says a snail has a skeleton inside like us. Is she right?', ('No – a snail has a hard shell outside', 'Some animals have an outside skeleton or shell.'), [('Yes', 'Snails do not have bones inside.'), ('No – snails have two skeletons', 'They have one shell.')], d="M")
U.q("R", "1.5", "O5", 'Why should you wash your hands before eating?', ('To remove germs that could make you ill', 'Germs spread on hands.'), [('To make them warm', 'It is to remove germs.'), ('It does not matter', 'Washing stops germs spreading.')], d="M")
V2 = U.V2
