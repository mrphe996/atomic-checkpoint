from science_v2.k import Unit
U = Unit("s5u01")
U.q("R", "1.1", "O1", 'Which plant does NOT have flowers?', ('A fern', 'Ferns use spores.'), [('A sunflower', 'Sunflowers have flowers.'), ('An apple tree', 'Apple trees flower.')], d="M")
U.q("R", "1.2", "O2", 'Why do bees help plants?', ('They carry pollen from flower to flower', 'This is pollination.'), [('They water the plants', 'Bees do not water plants.'), ('They eat the seeds', 'They help make seeds.')], d="M")
U.q("P", "1.3", "O3", 'A seed has hooks on it. How is it most likely spread?', ('It sticks to animal fur', 'Hooks catch on fur.'), [('By the wind', 'Wind seeds are light with wings or fluff.'), ('By water', 'Water seeds float.')], d="M")
U.q("F", "1.4", "O5", 'To test whether seeds need water to germinate, what is fair?', ('Two dishes of the same seeds in the same place, only one watered', 'Only water is changed.'), [('Different seeds in each dish', 'That changes two things.'), ('One dish in the dark and dry, one in light and wet', 'That changes two things.')], d="M")
V2 = U.V2
