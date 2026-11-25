from science_v2.k import Unit
U = Unit("s6u03")
U.q("R", "3.1", "O1", 'How is igneous rock formed?', ('Hot melted rock cools and turns solid', 'Lava or magma hardens.'), [('Layers of sand are pressed together', 'That makes sedimentary rock.'), ('Plants rot', 'That makes soil.')], d="M")
U.q("R", "3.2", "O3", 'In which type of rock are fossils usually found?', ('Sedimentary', 'Fossils are trapped in layers of sediment.'), [('Igneous', 'Heat would destroy them.'), ('None', 'Fossils are common in sedimentary rock.')], d="M")
U.q("P", "3.3", "O4", 'Limestone is heated and squeezed deep underground. What does it become?', ('Marble, a metamorphic rock', 'Heat and pressure change rocks.'), [('Lava', 'It changes without melting.'), ('Soil', 'Soil forms at the surface.')], d="M")
U.q("F", "3.4", "O6", 'How could you compare how fast water drains through two soils?', ('Pour the same amount of water through the same amount of each soil and time it', 'Keep everything else the same.'), [('Use different amounts of water', 'That is not fair.'), ('Look at the colours', 'Colour does not measure drainage.')], d="M")
V2 = U.V2
