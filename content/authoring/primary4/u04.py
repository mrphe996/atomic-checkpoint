# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 4 · Unit 4 Earth and its habitats. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit4 import *

OBJ = {
 'O1': {'sec': '4.1', 'code': 'Earth and Space', 'codeNote': '', 't': 'Know that the Earth has layers: crust, mantle and core.'},
 'O2': {'sec': '4.2', 'code': 'Earth and Space', 'codeNote': '', 't': 'Know what a volcano is, and the difference between magma and lava.'},
 'O3': {'sec': '4.3', 'code': 'Earth and Space', 'codeNote': '', 't': 'Know that earthquakes happen when plates of the crust move, and how to stay safe.'},
 'O4': {'sec': '4.4', 'code': 'Biology', 'codeNote': '', 't': 'Know that a habitat gives a living thing food, water and shelter, and name some habitats.'},
}
U = YUnit(4, 'Earth and its habitats', 'Earth and Space: planet Earth', 'Inside the Earth, volcanoes, earthquakes, and the many habitats where plants and animals live.', OBJ)

# ============================================================  4.1
s = U.section('4.1', 'The structure of the Earth', ['O1']); s.words(V['4.1']); core(s, 'O1')
s.stop(PM('Which layer of the Earth do we live on?', ('🟫', 'The crust'), [('🔴', 'The core', 'The core is in the middle.'), ('🟧', 'The mantle', 'The mantle is under the crust.')], 'O1'),
       PM('What is the crust like?', ('🪨', 'Thin and rocky'), [('🔥', 'The hottest part', 'That is the core.'), ('💧', 'Made of water', 'The crust is rock.')], 'O1'))
s.stop(PM('Which layer is in the very middle of the Earth?', ('🔴', 'The core'), [('🟫', 'The crust', 'The crust is outside.'), ('🟧', 'The mantle', 'The mantle is between.')], 'O1'),
       PM('Which layer is the hottest?', ('🔴', 'The core'), [('🟫', 'The crust', 'We live on the cool crust.'), ('🟧', 'The mantle', 'The core is even hotter.')], 'O1'))
s.prac(
 OD('Order the layers from the outside to the middle.', ['crust', 'mantle', 'core'], o='O1'),
 PM('A peach is like the Earth. Which part is like the crust?', ('🍑', 'The thin skin'), [('🟤', 'The stone', 'The stone is like the core.'), ('🟠', 'The soft fruit', 'That is like the mantle.')], 'O1'),
 YN('Has anyone ever dug right through the crust?', False, 'O1', pic='⛏️', why='No! The crust is far too thick.'),
 PM('What is the mantle made of?', ('🔥', 'Very hot rock'), [('🧊', 'Ice', 'It is very hot.'), ('🌊', 'Sea water', 'It is hot rock.')], 'O1'),
 GD('Which layer?', 'Layer', [('🏡 where we live', 'crust'), ('🔥 hot rock that moves slowly', 'mantle'), ('☀️ the hottest middle', 'core')], o='O1'),
 PM('What shape is the Earth?', ('🌍', 'A ball (sphere)'), [('📄', 'Flat', 'The Earth is round.'), ('📦', 'A box', 'The Earth is round.')], 'O1'),
 MT('Match each word to what it means.', [('crust', 'thin rocky outside'), ('mantle', 'hot rock under the crust'), ('core', 'hot middle')], o='O1'),
 YN('Do the rocks get hotter as you go deeper into the Earth?', True, 'O1', pic='⛏️', why='Yes – deeper is hotter.'),
 PM('Which of these is on the crust?', ('🏔️', 'Mountains'), [('🔴', 'The core', 'The core is deep inside.'), ('🟧', 'The mantle', 'The mantle is underneath.')], 'O1'),
 TK('Tick what is true.', ['True', 'False'], [('the Earth has layers', ['✓', '✗']), ('the core is cold', ['✗', '✓']), ('we live on the crust', ['✓', '✗'])], o='O1'),
 PM('The Earth is a…', ('🌍', 'planet'), [('⭐', 'star', 'The Sun is our star.'), ('🌙', 'moon', 'The Earth has a moon.')], 'O1'),
 PM('How hot is the core?', ('☀️', 'About as hot as the surface of the Sun'), [('🧊', 'Cold like ice', 'It is extremely hot.'), ('🛁', 'Warm like a bath', 'Much, much hotter!')], 'O1', d='H'),
)
s.adv(
 PM('* Advanced. Why can we not visit the core?', ('🔥', 'It is far too deep and hot'), [('🔒', 'It is locked', 'It is too deep and hot.'), ('🌊', 'It is underwater', 'It is too deep and hot.')], 'O1', d='H'),
 PM('* Advanced. A play-dough Earth is cut in half. What do you see?', ('🍰', 'Layers'), [('⚪', 'One colour', 'The model has layers.'), ('🕳️', 'A hollow middle', 'The middle is the core.')], 'O1', d='H'),
 OD('* Advanced. Order from coolest to hottest.', ['crust', 'mantle', 'core'], o='O1', d='H'),
)
s.labs('Earth lab',
 sort_lab('Which layer?', 'Sort each clue into the right layer.', ['Crust', 'Mantle', 'Core'],
  [('we live here', '🏡', 0, 'We live on the crust.'), ('the hottest part', '🔥', 2, 'The core is hottest.'), ('hot rock that moves slowly', '🟧', 1, 'That is the mantle.'), ('mountains and seas', '🏔️', 0, 'They are on the crust.'), ('the very middle', '🎯', 2, 'The core is in the middle.')],
  [PM('Where are the mountains?', ('🟫', 'On the crust'), [('🔴', 'In the core', 'They are on the crust.')], 'O1')]),
 home('Play-dough Earth', 'Make a model of the Earth\'s layers.', ['red, orange and brown play-dough', 'a plastic knife (with an adult)'], ['An adult should cut the model.'],
  ['Make a red ball: the core.', 'Cover it in orange: the mantle.', 'Add a thin brown layer: the crust.', 'Cut it in half.'],
  ['Layer', 'Thick or thin?'], [('crust', ['thick', 'thin']), ('mantle', ['thick', 'thin'])],
  [PM('Which layer is the thinnest?', ('🟫', 'The crust'), [('🟧', 'The mantle', 'The mantle is thick.')], 'O1')]))

# ============================================================  4.2
s = U.section('4.2', 'Volcanoes', ['O2']); s.words(V['4.2']); core(s, 'O2')
s.stop(PM('What do we call melted rock that comes out of a volcano?', ('🔥', 'Lava'), [('🟠', 'Magma', 'Magma is inside the Earth.'), ('💧', 'Water', 'It is melted rock.')], 'O2'),
       PM('What do we call melted rock inside the Earth?', ('🟠', 'Magma'), [('🔥', 'Lava', 'Lava is outside.'), ('🪨', 'Sand', 'It is melted rock.')], 'O2'))
s.stop(PM('Why do some farmers like to live near volcanoes?', ('🌾', 'The soil is very good for growing food'), [('🔥', 'It is warm for sleeping', 'It is about the soil.'), ('🌋', 'They like loud bangs', 'It is about the soil.')], 'O2'),
       PM('Who watches volcanoes to keep people safe?', ('🧑‍🔬', 'Scientists'), [('🧑‍🍳', 'Cooks', 'Scientists watch volcanoes.'), ('🧑‍🎨', 'Artists', 'Scientists watch volcanoes.')], 'O2'))
s.prac(
 PM('What does “erupt” mean?', ('💥', 'Burst out suddenly'), [('😴', 'Sleep', 'Erupt means burst out.'), ('🧊', 'Freeze', 'Erupt means burst out.')], 'O2'),
 OD('Put the eruption in order.', ['magma pushes up', 'the volcano erupts', 'lava flows down'], o='O2'),
 YN('Is lava hot?', True, 'O2', pic='🌋', why='Yes! Much hotter than boiling water.'),
 PM('What can a volcano blow out besides lava?', ('🌫️', 'Ash and smoke'), [('🍬', 'Sweets', 'Ash and smoke.'), ('❄️', 'Snow', 'Ash and smoke.')], 'O2'),
 GD('Magma or lava?', 'Name', [('🟠 melted rock inside the Earth', 'magma'), ('🔥 melted rock flowing outside', 'lava')], o='O2'),
 PM('What should people do if a volcano might erupt?', ('🚗', 'Move to a safe place'), [('📸', 'Go closer to take photos', 'Stay away!'), ('🏊', 'Go swimming', 'Move to safety.')], 'O2'),
 MT('Match each word to what it means.', [('volcano', 'mountain where melted rock comes out'), ('magma', 'melted rock inside'), ('lava', 'melted rock outside')], o='O2'),
 YN('When lava cools down, does it become solid rock?', True, 'O2', pic='🪨', why='Yes. Cooled lava turns into rock.'),
 PM('Which is a model volcano made with?', ('🍋', 'Baking soda and vinegar'), [('🍫', 'Chocolate and milk', 'Baking soda and vinegar fizz.'), ('🧊', 'Ice and water', 'Baking soda and vinegar fizz.')], 'O2'),
 TK('Tick what is true.', ['True', 'False'], [('lava is very hot', ['✓', '✗']), ('volcano soil is good for farms', ['✓', '✗']), ('volcanoes erupt every day', ['✗', '✓'])], o='O2'),
 PM('Where does magma come from?', ('🟧', 'Deep inside the Earth'), [('☁️', 'The clouds', 'It comes from inside the Earth.'), ('🌊', 'The sea', 'It comes from inside the Earth.')], 'O2'),
 PM('Lava cools and becomes…', ('🪨', 'rock'), [('💧', 'water', 'Cooled lava is rock.'), ('🍬', 'sugar', 'Cooled lava is rock.')], 'O2', d='H'),
)
s.adv(
 PM('* Advanced. Why is lava ten times hotter than boiling water dangerous for houses?', ('🔥', 'It burns and covers them'), [('❄️', 'It freezes them', 'It is extremely hot.'), ('💧', 'It washes them', 'It is melted rock.')], 'O2', d='H'),
 PM('* Advanced. A volcano has not erupted for 1000 years. What do we call it?', ('😴', 'Dormant (sleeping)'), [('💥', 'Erupting', 'It is quiet.'), ('🧊', 'Frozen', 'It is quiet, not frozen.')], 'O2', d='VH'),
 OD('* Advanced. Order the path of melted rock.', ['magma in the mantle', 'magma rises', 'lava comes out', 'lava cools to rock'], o='O2', d='H'),
)
s.labs('Volcano lab',
 test_lab('Model volcano', 'Use different spoons of baking soda with the same vinegar. Read how high the foam goes.', 'Baking soda', 'Foam height', 'cm', 20, 2,
  'Tap the number the bar reaches.', [('1 spoon', '🥄', 4), ('2 spoons', '🥄🥄', 10), ('3 spoons', '🥄🥄🥄', 16)],
  [PM('Which gave the biggest eruption?', ('🥄', '3 spoons'), [('🥄', '1 spoon', 'It gave the least foam.')], 'O2')]),
 home('Model volcano', 'Make a fizzing volcano with an adult.', ['a small bottle', 'sand or play-dough', 'baking soda', 'vinegar', 'an adult'], ['Do it outside or on a tray.', 'Keep it away from your eyes.'],
  ['Build sand round the bottle.', 'Put baking soda in the bottle.', 'Pour in vinegar.'],
  ['Question', 'My answer'], [('did it fizz over?', ['yes', 'no']), ('did more vinegar make more foam?', ['yes', 'no'])],
  [PM('In a real volcano, what comes out instead of foam?', ('🔥', 'Lava'), [('🫧', 'Bubble bath', 'Real volcanoes give lava.')], 'O2')]))

# ============================================================  4.3
s = U.section('4.3', 'Earthquakes', ['O3']); s.words(V['4.3']); core(s, 'O3')
s.stop(PM('What are the big pieces of the Earth\'s crust called?', ('🧩', 'Plates'), [('🍽️', 'Dishes', 'They are called plates – but not dinner plates!'), ('🪨', 'Pebbles', 'They are huge plates.')], 'O3'),
       PM('What happens in an earthquake?', ('🫨', 'The ground shakes'), [('🌧️', 'It rains a lot', 'The ground shakes.'), ('❄️', 'It snows', 'The ground shakes.')], 'O3'))
s.stop(PM('What should you do first in an earthquake?', ('🧎', 'Drop to the floor'), [('🏃', 'Run outside fast', 'Drop, cover and hold on.'), ('🪜', 'Climb up high', 'Drop, cover and hold on.')], 'O3'),
       PM('Where should you take cover in an earthquake?', ('🪑', 'Under a strong table'), [('🪟', 'Next to a window', 'Glass can break.'), ('🛗', 'In a lift', 'Lifts can stop.')], 'O3'))
s.prac(
 OD('Put the safety steps in order.', ['drop', 'cover', 'hold on'], o='O3'),
 PM('Why does the ground shake?', ('🧩', 'Plates of the crust slip suddenly'), [('🐘', 'Elephants are running', 'It is the plates moving.'), ('🌬️', 'The wind blows hard', 'It is the plates moving.')], 'O3'),
 YN('Do the plates move very slowly most of the time?', True, 'O3', pic='🐌', why='Yes – about as fast as your fingernails grow!'),
 PM('Which building is best in an earthquake?', ('🏢', 'One built to sway gently'), [('🧱', 'One built of loose bricks', 'It may fall down.'), ('🃏', 'A house of cards', 'It falls easily.')], 'O3'),
 GD('Safe or not safe in an earthquake?', 'Safe?', [('🪑 under a strong table', 'safe'), ('🪟 next to a window', 'not safe'), ('🧎 on the floor, covering your head', 'safe')], o='O3'),
 MT('Match each word to what it means.', [('earthquake', 'the ground shakes'), ('plates', 'pieces of the crust'), ('crack', 'a thin line where something breaks')], o='O3'),
 PM('After an earthquake, what might you see on walls?', ('⚡', 'Cracks'), [('🌈', 'Rainbows', 'Look for cracks.'), ('🌸', 'Flowers', 'Look for cracks.')], 'O3'),
 YN('Should you use the lift during an earthquake?', False, 'O3', pic='🛗', why='No – it might stop. Use the stairs after the shaking stops.'),
 TK('Tick the safe things to do.', ['Safe', 'Not safe'], [('drop, cover, hold on', ['✓', '✗']), ('stand by a window', ['✗', '✓']), ('listen to adults', ['✓', '✗'])], o='O3'),
 PM('Which tower stays up best when shaken?', ('🔺', 'A wide, low tower'), [('🗼', 'A tall, thin tower', 'Tall, thin towers fall more easily.')], 'O3'),
 PM('Who studies earthquakes?', ('🧑‍🔬', 'Scientists'), [('🧑‍🍳', 'Cooks', 'Scientists study them.'), ('💇', 'Hairdressers', 'Scientists study them.')], 'O3'),
 PM('What covers your head in an earthquake?', ('🙌', 'Your arms'), [('🎒', 'Nothing', 'Always protect your head.'), ('🍽️', 'A plate', 'Use your arms or a table.')], 'O3', d='H'),
)
s.adv(
 PM('* Advanced. Why do earthquakes happen more in some countries?', ('🧩', 'They are where plates meet'), [('🌧️', 'It rains more there', 'It is about plates.'), ('🏙️', 'They have more cities', 'It is about plates.')], 'O3', d='VH'),
 PM('* Advanced. Why are tall buildings made to sway?', ('🌳', 'So they bend instead of breaking'), [('🎢', 'For fun', 'It keeps them safe.'), ('🌬️', 'To make wind', 'It keeps them safe.')], 'O3', d='H'),
 OD('* Advanced. Order what happens.', ['plates get stuck', 'pressure builds up', 'plates slip suddenly', 'the ground shakes'], o='O3', d='H'),
)
s.labs('Earthquake lab',
 test_lab('Shaky towers', 'Build towers of different widths on a tray and shake it. Read how many seconds each tower stays up.', 'Tower', 'Time standing', 'seconds', 30, 3,
  'Tap the number the bar reaches.', [('tall and thin', '🗼', 6), ('medium', '🏠', 15), ('low and wide', '🔺', 27)],
  [PM('Which tower stood up longest?', ('🔺', 'Low and wide'), [('🗼', 'Tall and thin', 'It fell first.')], 'O3')]),
 home('Shaky towers', 'Test towers on a tray.', ['building blocks', 'a tray'], ['Shake gently. Keep blocks away from little children.'],
  ['Build a tall thin tower.', 'Shake the tray.', 'Build a wide tower and shake again.'],
  ['Tower', 'Did it fall?'], [('tall and thin', ['fell', 'stayed up']), ('low and wide', ['fell', 'stayed up'])],
  [PM('Which shape is safer?', ('🔺', 'Low and wide'), [('🗼', 'Tall and thin', 'It falls more easily.')], 'O3')]))

# ============================================================  4.4
s = U.section('4.4', 'Different habitats', ['O4']); s.words(V['4.4']); core(s, 'O4')
s.stop(PM('What is a habitat?', ('🏞️', 'The place where a plant or animal lives'), [('🍽️', 'A kind of food', 'It is a home.'), ('🎨', 'A colour', 'It is a home.')], 'O4'),
       PM('What does a habitat give animals?', ('🏠', 'Food, water and shelter'), [('📺', 'Television', 'Food, water and shelter.'), ('🎁', 'Toys', 'Food, water and shelter.')], 'O4'))
s.stop(PM('Which animal\'s habitat is the hot desert?', ('🐪', 'A camel'), [('🐻‍❄️', 'A polar bear', 'It lives in the icy Arctic.'), ('🐠', 'A fish', 'It lives in water.')], 'O4'),
       PM('Which animal lives in the icy Arctic?', ('🐻‍❄️', 'A polar bear'), [('🐪', 'A camel', 'It lives in the desert.'), ('🐒', 'A monkey', 'It lives in the rainforest.')], 'O4'))
s.prac(
 GD('Where does each animal live?', 'Habitat', [('🐪 camel', 'desert'), ('🐠 fish', 'ocean'), ('🐒 monkey', 'rainforest'), ('🐻‍❄️ polar bear', 'Arctic')], o='O4'),
 PM('Where might you find woodlice?', ('🪨', 'Under a stone'), [('☁️', 'In the clouds', 'They like dark, damp places.'), ('🔥', 'In a fire', 'They like dark, damp places.')], 'O4'),
 YN('Is a pond a habitat?', True, 'O4', pic='🐸', why='Yes – for frogs, fish and insects.'),
 PM('What is shelter?', ('🏠', 'A safe place to rest'), [('🍎', 'Food', 'Shelter keeps you safe.'), ('💧', 'Water', 'Shelter keeps you safe.')], 'O4'),
 PM('Which habitat is hot and wet with tall trees?', ('🌴', 'A rainforest'), [('🏜️', 'A desert', 'Deserts are dry.'), ('❄️', 'The Arctic', 'The Arctic is cold.')], 'O4'),
 MT('Match each word to what it means.', [('desert', 'very dry'), ('ocean', 'big salty water'), ('rainforest', 'hot and wet forest')], o='O4'),
 PM('A tree is a habitat for…', ('🐦', 'birds and insects'), [('🐟', 'fish', 'Fish live in water.'), ('🐪', 'camels', 'Camels live in deserts.')], 'O4'),
 YN('Should you put stones back after looking under them?', True, 'O4', pic='🪨', why='Yes, so the minibeasts keep their home.'),
 TK('What does a good habitat give?', ['Yes', 'No'], [('food', ['✓', '✗']), ('water', ['✓', '✗']), ('shelter', ['✓', '✗']), ('noise', ['✗', '✓'])], o='O4'),
 PM('Why could a polar bear not live in a desert?', ('🔥', 'It would be far too hot'), [('🏖️', 'It hates sand castles', 'It is about heat.'), ('🌙', 'There is no Moon', 'It is about heat.')], 'O4'),
 PM('Where do most kinds of animals and plants live?', ('🌴', 'Rainforests'), [('🏜️', 'Deserts', 'Rainforests have the most.'), ('❄️', 'Ice caps', 'Rainforests have the most.')], 'O4', d='H'),
 PM('A camel can go a long time without water. Why is that useful?', ('🏜️', 'Deserts have very little water'), [('🌊', 'It lives in the sea', 'Deserts are dry.'), ('🌧️', 'It rains every day', 'Deserts are dry.')], 'O4'),
)
s.adv(
 PM('* Advanced. People cut down a forest. What happens to the animals?', ('🏚️', 'They lose their habitat'), [('🎉', 'They get more food', 'They lose their home.'), ('🏠', 'Nothing changes', 'They lose their home.')], 'O4', d='H'),
 PM('* Advanced. Why do fish need water in their habitat?', ('🐟', 'They breathe with gills in water'), [('🚿', 'To keep clean', 'They breathe in water.'), ('🎨', 'To stay colourful', 'They breathe in water.')], 'O4', d='H'),
 GD('* Advanced. Match the plant to its habitat.', 'Habitat', [('🌵 cactus', 'desert'), ('🌴 palm tree', 'rainforest'), ('🪸 seaweed', 'ocean')], o='O4', d='H'),
)
s.labs('Habitat lab',
 sort_lab('Who lives where?', 'Sort each animal into its habitat.', ['Desert', 'Ocean', 'Rainforest'],
  [('camel', '🐪', 0, 'Camels live in dry deserts.'), ('whale', '🐋', 1, 'Whales live in the ocean.'), ('monkey', '🐒', 2, 'Monkeys live in rainforests.'), ('octopus', '🐙', 1, 'Octopuses live in the ocean.'), ('parrot', '🦜', 2, 'Parrots live in rainforests.'), ('scorpion', '🦂', 0, 'Scorpions live in deserts.')],
  [PM('Which animal lives in the ocean?', ('🐋', 'Whale'), [('🐪', 'Camel', 'Camels live in deserts.')], 'O4')]),
 home('Minibeast hunt', 'Find small animals near your home, with an adult.', ['a magnifying glass', 'an adult'], ['Do not touch animals that sting.', 'Wash your hands afterwards.'],
  ['Look under stones and leaves.', 'Look on a tree.', 'Put everything back gently.'],
  ['Where I looked', 'Did I find animals?'], [('under a stone', ['yes', 'no']), ('on a tree', ['yes', 'no']), ('in the grass', ['yes', 'no'])],
  [PM('Why do woodlice live under stones?', ('🪨', 'It is dark and damp'), [('☀️', 'It is hot and sunny', 'They like dark, damp places.')], 'O4')]))

U.mindmap(('Earth\'s layers', 'crust, mantle, core', 'O1', '4.1'), ('Volcanoes', 'magma, lava, eruptions', 'O2', '4.2'),
          ('Earthquakes', 'plates, shaking, drop-cover-hold on', 'O3', '4.3'), ('Habitats', 'food, water, shelter; desert, ocean, rainforest', 'O4', '4.4'))
