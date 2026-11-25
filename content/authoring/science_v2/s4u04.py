from science_v2.k import Unit
U = Unit("s4u04")
U.q("R", "4.1", "O1", 'What is the hot middle of the Earth called?', ('The core', 'The core is at the centre.'), [('The crust', 'The crust is the outside.'), ('The sky', "The sky is not part of the Earth's layers.")], d="M")
U.q("R", "4.2", "O2", 'What comes out of an erupting volcano?', ('Hot melted rock (lava), ash and gas', 'These come from deep underground.'), [('Cold water', 'Volcanoes are hot.'), ('Ice', 'Volcanoes erupt hot material.')], d="M")
U.q("E", "4.3", "O3", 'Why do many earthquake-safe buildings have strong, flexible frames?', ('So they can sway without falling down', 'Flexible buildings survive shaking better.'), [('To look nice', 'It is about safety.'), ('To stop earthquakes', 'Buildings cannot stop earthquakes.')], d="M")
U.q("R", "4.4", "O4", 'Why can a polar bear live in the Arctic?', ('It has thick fur and fat to keep warm', 'It is suited to its habitat.'), [('It likes ice cream', 'It is about its body.'), ('It never gets cold', 'It needs fur and fat to stay warm.')], d="M")
V2 = U.V2
