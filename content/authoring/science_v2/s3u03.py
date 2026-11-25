from science_v2.k import Unit
U = Unit("s3u03")
U.q("P", "3.1", "O1", 'Where will the shadow of a tree be in the morning, when the Sun is in the east?', ('On the west side of the tree', 'Shadows form on the side away from the light.'), [('On the east side', 'That is the side facing the Sun.'), ('There is no shadow', 'Trees block light.')], d="M")
U.q("P", "3.2", "O2", 'A torch is moved closer to a toy. What happens to the shadow?', ('It gets bigger', 'More light is blocked.'), [('It gets smaller', 'Moving closer makes it bigger.'), ('It disappears', 'It gets bigger.')], d="M")
U.q("R", "3.3", "O3", 'Which material is opaque?', ('Wood', 'No light passes through wood.'), [('Clear glass', 'Glass is transparent.'), ('Clean water', 'Clean water is transparent.')], d="M")
U.q("F", "3.4", "O4", 'How could you test which material is translucent?', ('Shine a torch through each and see if some light gets through', 'Translucent materials let some light through.'), [('Weigh each one', 'Weight does not tell you about light.'), ('Smell each one', 'Smell does not test light.')], d="M")
V2 = U.V2
