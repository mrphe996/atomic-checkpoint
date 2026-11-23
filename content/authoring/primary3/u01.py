# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 3 · Unit 1 Plants are living things. Written by the Atomic teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit3 import *

OBJ = {
 'O1': {'sec': '1.1', 'code': 'Biology', 'codeNote': '', 't': 'Sort things into living, once living and never alive, and know that plants are living things.'},
 'O2': {'sec': '1.2', 'code': 'Biology', 'codeNote': '', 't': 'Name the roots, stem, leaves and flowers of a plant and say what each part does.'},
 'O3': {'sec': '1.3', 'code': 'Biology', 'codeNote': '', 't': 'Know that plants need light to grow well, and grow towards the light.'},
 'O4': {'sec': '1.4', 'code': 'Biology', 'codeNote': '', 't': 'Know that plants need water and the right temperature to stay healthy.'},
}
U = YUnit(1, 'Plants are living things', 'Biology: plants', 'Alive or not alive, the parts of a plant, and what plants need to grow.', OBJ)

# ============================================================  1.1
s = U.section('1.1', 'Alive or not alive?', ['O1']); s.words(V['1.1']); core(s, 'O1')
s.stop(PM('Which one is alive?', ('🐶', 'A puppy'), [('🧸', 'A teddy', 'A teddy never eats or grows.'), ('🚗', 'A toy car', 'A toy car never eats or grows.')], 'O1'),
       PM('Which one is a living thing?', ('🌳', 'A tree'), [('🪨', 'A rock', 'A rock never grows.'), ('🥄', 'A spoon', 'A spoon never grows.')], 'O1'))
s.stop(PM('Is a rock alive?', ('👎', 'No'), [('👍', 'Yes', 'A rock does not eat, drink or grow.')], 'O1'),
       PM('Is a sunflower alive?', ('👍', 'Yes'), [('👎', 'No', 'A sunflower drinks water and grows.')], 'O1'))
s.prac(
 GD('Alive or not alive?', 'Alive?', [('🐱 a cat', 'yes'), ('🪨 a stone', 'no'), ('🌷 a tulip', 'yes'), ('⚽ a ball', 'no'), ('🐜 an ant', 'yes')], o='O1'),
 PM('Which one can grow?', ('🌱', 'A seedling'), [('🧱', 'A brick', 'Bricks never grow.'), ('📘', 'A book', 'Books never grow.')], 'O1'),
 YN('Does a puppy need food and water?', True, 'O1', pic='🐶', why='Yes. All living things need food and water.'),
 YN('Does a toy robot grow bigger?', False, 'O1', pic='🤖', why='No. A robot is not alive, so it does not grow.'),
 PM('Your little brother has a pet fish. What does the fish need to stay alive?', ('🍤', 'Food and clean water'), [('📺', 'A television', 'Living things need food and water.'), ('🧸', 'A teddy', 'Living things need food and water.')], 'O1'),
 PM('Which is a plant?', ('🌵', 'A cactus'), [('🐸', 'A frog', 'A frog is an animal.'), ('🦋', 'A butterfly', 'A butterfly is an animal.')], 'O1'),
 TK('Tick the living things.', ['Alive', 'Not alive'], [('a bird', ['✓', '✗']), ('a cup', ['✗', '✓']), ('grass', ['✓', '✗'])], o='O1'),
 PM('How do you know a plant is alive?', ('📈', 'It grows'), [('🎨', 'It is green', 'Paint can be green too.'), ('🔊', 'It is noisy', 'Plants are not noisy.')], 'O1'),
 YN('Is your teacher a living thing?', True, 'O1', pic='👩‍🏫', why='Yes. People are living things.'),
 PM('Which was never alive?', ('🪨', 'A pebble'), [('🍎', 'An apple', 'An apple came from a living tree.'), ('🪵', 'A log', 'A log came from a living tree.')], 'O1', d='H'),
 PM('A seed is planted and watered. What will happen?', ('🌱', 'It grows into a plant'), [('🪨', 'It turns into a stone', 'A seed is alive. It grows.'), ('💨', 'It flies away', 'It grows.')], 'O1'),
 MT('Match each word to what it means.', [('alive', 'living'), ('grow', 'get bigger'), ('rock', 'never alive')], o='O1'),
)
s.adv(
 PM('* Advanced. A wooden table was once part of a tree. What is the wood now?', ('🪵', 'Once alive, but not alive now'), [('🌳', 'Still alive', 'Wood cut from a tree is no longer alive.'), ('🪨', 'Never alive', 'It came from a living tree.')], 'O1', d='VH'),
 PM('* Advanced. A plant does not walk. How does it move?', ('🌻', 'It turns slowly towards the light'), [('🏃', 'It runs at night', 'Plants cannot run.'), ('🙅', 'It never moves at all', 'Plants move slowly towards light.')], 'O1', d='H'),
 GD('* Advanced. Sort these.', 'Group', [('🐕 a dog', 'alive'), ('🪵 a log', 'once alive'), ('🪨 a rock', 'never alive')], o='O1', d='H'),
)
s.labs('Alive lab',
 sort_lab('Alive or not alive?', 'Sort each thing into the right group.', ['Alive', 'Not alive'],
  [('tree', '🌳', 0, 'A tree grows.'), ('stone', '🪨', 1, 'A stone never grows.'), ('ant', '🐜', 0, 'An ant eats and moves.'), ('car', '🚗', 1, 'A car never grows.'), ('flower', '🌸', 0, 'A flower drinks water.'), ('spoon', '🥄', 1, 'A spoon never grows.')],
  [PM('Which one is alive?', ('🐜', 'The ant'), [('🚗', 'The car', 'A car is not alive.')], 'O1')]),
 home('Alive hunt', 'Find living and non-living things outside.', ['a garden or park', 'an adult'], ['Do not touch animals you do not know.', 'Wash your hands afterwards.'],
  ['Walk round a garden or park with an adult.', 'Look for living things.', 'Look for things that are not alive.'],
  ['What I found', 'Alive?'], [('a leaf on a tree', ['yes', 'no']), ('a stone', ['yes', 'no']), ('a worm', ['yes', 'no']), ('a bench', ['yes', 'no'])],
  [PM('Which did you find that is alive?', ('🪱', 'The worm'), [('🪑', 'The bench', 'A bench is not alive.')], 'O1')]))

# ============================================================  1.2
s = U.section('1.2', 'Parts of a plant', ['O2']); s.words(V['1.2']); core(s, 'O2')
s.stop(PM('Which part of a plant takes in water?', ('🥕', 'The roots'), [('🌸', 'The flower', 'The roots drink water.'), ('🍃', 'The leaves', 'The roots drink water.')], 'O2'),
       PM('Which part of a plant is under the ground?', ('🥕', 'The roots'), [('🍃', 'The leaves', 'Leaves are in the air.'), ('🌸', 'The flower', 'Flowers are in the air.')], 'O2'))
s.stop(PM('Which part of a plant makes seeds?', ('🌸', 'The flower'), [('🥕', 'The roots', 'Flowers make seeds.'), ('🌿', 'The stem', 'Flowers make seeds.')], 'O2'),
       PM('Which part holds the plant up?', ('🌿', 'The stem'), [('🌸', 'The flower', 'The stem holds it up.'), ('🍃', 'A leaf', 'The stem holds it up.')], 'O2'))
s.prac(
 GD('Which part is it?', 'Part', [('🥕 under the ground', 'root'), ('🌿 holds the plant up', 'stem'), ('🍃 flat and green', 'leaf'), ('🌸 bright and pretty', 'flower')], o='O2'),
 PM('What do roots do?', ('💧', 'Take in water'), [('🌸', 'Make flowers', 'Flowers grow at the top.'), ('🔊', 'Make a noise', 'Roots take in water.')], 'O2'),
 PM('Which part of a plant uses sunlight to make food?', ('🍃', 'The leaves'), [('🥕', 'The roots', 'Roots are in the dark soil.'), ('🌰', 'The seeds', 'Leaves make food.')], 'O2'),
 PM('You eat a carrot. Which part of the plant is it?', ('🥕', 'A root'), [('🍃', 'A leaf', 'A carrot grows under the ground.'), ('🌸', 'A flower', 'A carrot grows under the ground.')], 'O2'),
 PM('You eat lettuce in a sandwich. Which part of the plant is it?', ('🥬', 'Leaves'), [('🥕', 'Roots', 'Lettuce is leaves.'), ('🌰', 'Seeds', 'Lettuce is leaves.')], 'O2'),
 YN('Is a tree trunk a stem?', True, 'O2', pic='🌳', why='Yes. A trunk is a big, woody stem.'),
 OD('Order the parts from the bottom of the plant to the top.', ['roots', 'stem', 'leaves', 'flower'], o='O2'),
 PM('The wind blows hard. What stops the plant blowing away?', ('⚓', 'The roots hold it in the soil'), [('🌸', 'The flower', 'Roots hold the plant.'), ('🍃', 'The leaves', 'Roots hold the plant.')], 'O2'),
 PM('Bees visit which part of a plant?', ('🌸', 'The flower'), [('🥕', 'The roots', 'Bees visit flowers.'), ('🌿', 'The stem', 'Bees visit flowers.')], 'O2'),
 TK('Tick what is true.', ['True', 'False'], [('the stem carries water', ['✓', '✗']), ('flowers grow under the ground', ['✗', '✓']), ('leaves are often green', ['✓', '✗'])], o='O2'),
 PM('Celery stands in coloured water. The colour goes up to the leaves. Which part carried it?', ('🌿', 'The stem'), [('🌸', 'The flower', 'The stem carries water up.'), ('🌰', 'A seed', 'The stem carries water up.')], 'O2', d='H'),
 YN('Can a seed grow into a new plant?', True, 'O2', pic='🌰', why='Yes. Flowers make seeds that grow into new plants.'),
)
s.adv(
 PM('* Advanced. A plant has no leaves. What problem will it have?', ('🍞', 'It cannot make enough food'), [('💧', 'It will drink too much', 'Leaves make food.'), ('🥶', 'It will be too warm', 'Leaves make food.')], 'O2', d='H'),
 PM('* Advanced. Broccoli is a bunch of tiny…', ('🥦', 'flowers'), [('🥕', 'roots', 'Broccoli grows at the top.'), ('🌿', 'stems only', 'Look at the tiny buds.')], 'O2', d='VH'),
 MT('* Advanced. Match each food to the plant part.', [('carrot', 'root'), ('lettuce', 'leaf'), ('celery', 'stem')], o='O2', d='H'),
)
s.labs('Plant parts lab',
 sort_lab('Which part do we eat?', 'Sort each food by the plant part.', ['Root', 'Leaf'],
  [('carrot', '🥕', 0, 'A carrot is a root.'), ('lettuce', '🥬', 1, 'Lettuce is leaves.'), ('radish', '🔴', 0, 'A radish is a root.'), ('spinach', '🍃', 1, 'Spinach is leaves.'), ('beetroot', '🟣', 0, 'Beetroot is a root.'), ('cabbage', '🥬', 1, 'Cabbage is leaves.')],
  [PM('Which food is a root?', ('🥕', 'Carrot'), [('🥬', 'Lettuce', 'Lettuce is leaves.')], 'O2')]),
 home('Thirsty celery', 'See the stem carry water.', ['a celery stick with leaves', 'a jar of water', 'food colouring', 'an adult'], ['Do not drink the coloured water.'],
  ['Put water and food colouring in a jar.', 'Stand the celery in the jar.', 'Wait one day.', 'Look at the leaves.'],
  ['Question', 'My answer'], [('did the colour go up the stem?', ['yes', 'no']), ('did the leaves change colour?', ['yes', 'no'])],
  [PM('Which part carried the coloured water up?', ('🌿', 'The stem'), [('🌸', 'The flower', 'The stem carries water.')], 'O2')]))

# ============================================================  1.3
s = U.section('1.3', 'Plants need light', ['O3']); s.words(V['1.3']); core(s, 'O3')
s.stop(PM('Which plant grew best?', ('🌿', 'The one by the window'), [('🥀', 'The one in the cupboard', 'It was pale and weak without light.')], 'O3'),
       PM('A plant was kept in a dark cupboard. What does it look like?', ('🥀', 'Pale and weak'), [('🌿', 'Green and strong', 'Without light it went pale.')], 'O3'))
s.stop(PM('What happens to a plant kept in the dark?', ('🥀', 'It goes pale and weak'), [('🌳', 'It grows big and strong', 'Plants need light.'), ('🌈', 'It turns rainbow colours', 'It goes pale.')], 'O3'),
       PM('What do plants need to grow green and strong?', ('☀️', 'Light'), [('🌑', 'Darkness', 'Plants need light.'), ('🔊', 'Music', 'Plants need light.')], 'O3'))
s.prac(
 YN('Do plants need light to grow well?', True, 'O3', pic='☀️', why='Yes. Leaves use light to make food.'),
 PM('Where should you put a plant in your classroom?', ('🪟', 'By a sunny window'), [('🗄️', 'In a dark cupboard', 'Plants need light.'), ('🎒', 'In your school bag', 'Plants need light.')], 'O3'),
 PM('A plant on a windowsill bends. Which way does it bend?', ('🪟', 'Towards the window'), [('🚪', 'Towards the door', 'Plants grow towards light.'), ('🔽', 'Down to the floor', 'Plants grow towards light.')], 'O3'),
 PM('Why do leaves need light?', ('🍞', 'To make food'), [('😴', 'To sleep', 'Leaves make food with light.'), ('🎨', 'To change colour', 'Leaves make food with light.')], 'O3'),
 GD('Will the plant grow well?', 'Grows well?', [('☀️ in a sunny garden', 'yes'), ('🌑 in a dark box', 'no'), ('🪟 by a window', 'yes'), ('🗄️ under the bed', 'no')], o='O3'),
 YN('A plant was in a box for 2 weeks. Will its leaves be bright green?', False, 'O3', pic='📦', why='No. Without light, leaves go pale.'),
 PM('Which flower turns to follow the Sun?', ('🌻', 'A young sunflower'), [('🌹', 'A plastic rose', 'A plastic flower is not alive.'), ('🪨', 'A stone', 'A stone is not alive.')], 'O3'),
 MT('Match each word to what it means.', [('sunlight', 'light from the Sun'), ('pale', 'very little colour'), ('healthy', 'strong and well')], o='O3'),
 TK('Tick what plants need.', ['Needs it', 'Does not'], [('light', ['✓', '✗']), ('toys', ['✗', '✓']), ('water', ['✓', '✗'])], o='O3'),
 PM('Grass under a paddling pool for a week turns…', ('🟨', 'yellow'), [('🟩', 'darker green', 'The pool blocked the light.'), ('🟦', 'blue', 'It turns yellow.')], 'O3', d='H'),
 PM('In a fair light test, what should be the same for both plants?', ('💧', 'The water they get'), [('☀️', 'The light they get', 'That is what we change.'), ('🤷', 'Nothing', 'Keep the water the same.')], 'O3', d='H'),
 YN('Can plants grow towards the light?', True, 'O3', pic='↗️', why='Yes. They bend towards the light.'),
)
s.adv(
 PM('* Advanced. Why are plants deep in a thick forest often tall and thin?', ('🌳', 'They grow up to reach the light'), [('💧', 'They have too much water', 'They reach up for light.'), ('🥶', 'It is cold', 'They reach up for light.')], 'O3', d='VH'),
 PM('* Advanced. A plant in a cupboard is put back in the sun. What happens?', ('🌿', 'It slowly turns green again'), [('🥀', 'It stays pale forever', 'Light helps it recover.'), ('🪨', 'It turns into a stone', 'It turns green again.')], 'O3', d='H'),
 OD('* Advanced. Order the light test.', ['get two plants', 'put one in the light and one in the dark', 'give them the same water', 'look after a week'], o='O3', d='H'),
)
s.labs('Light lab',
 test_lab('How tall did it grow?', 'Two bean plants grew for two weeks in different places. Read how tall each one grew.', 'Where it grew', 'Height', 'cm', 20, 2,
  'Tap the number the bar reaches.', [('in a dark cupboard', '🗄️', 4), ('in a shady room', '🌥️', 10), ('by a sunny window', '☀️', 16)],
  [PM('Where did the plant grow best?', ('☀️', 'By a sunny window'), [('🗄️', 'In a dark cupboard', 'It grew least there.')], 'O3')]),
 home('Light test', 'Find out if plants need light.', ['two small plants', 'a big box', 'water'], ['Ask an adult before moving plants.'],
  ['Put both plants in the same room.', 'Cover one plant with a big box.', 'Water both the same.', 'Look after one week.'],
  ['Plant', 'What did it look like?'], [('plant in the light', ['green and strong', 'pale and weak']), ('plant in the box', ['green and strong', 'pale and weak'])],
  [PM('Which plant was pale?', ('📦', 'The one in the box'), [('☀️', 'The one in the light', 'It had light, so it stayed green.')], 'O3')]))

# ============================================================  1.4
s = U.section('1.4', 'Plants need water and warmth', ['O4']); s.words(V['1.4']); core(s, 'O4')
s.stop(PM('What does a plant do when it has no water?', ('🥀', 'It wilts'), [('🌳', 'It grows bigger', 'Without water it wilts.'), ('🌈', 'It changes colour', 'Without water it wilts.')], 'O4'),
       PM('A plant is drooping. What should you give it?', ('💧', 'Some water'), [('🍫', 'Some chocolate', 'Plants need water.'), ('🧸', 'A toy', 'Plants need water.')], 'O4'))
s.stop(PM('Where would a plant grow best?', ('🌤️', 'In a warm, sunny garden'), [('🧊', 'In a freezer', 'Too cold!'), ('🔥', 'Next to a hot oven', 'Too hot!')], 'O4'),
       PM('What temperature do most plants like?', ('🙂', 'Warm: not too hot, not too cold'), [('🥶', 'Freezing cold', 'They can freeze.'), ('🥵', 'Very, very hot', 'They can dry up.')], 'O4'))
s.prac(
 YN('Do plants need water?', True, 'O4', pic='💧', why='Yes. Without water they wilt and die.'),
 PM('You are going on holiday for a week. What should you do for your plant?', ('🧑‍🤝‍🧑', 'Ask a neighbour to water it'), [('🗄️', 'Put it in a cupboard', 'It needs light and water.'), ('🧊', 'Put it in the fridge', 'It is too cold there.')], 'O4'),
 PM('Which plant is wilting?', ('🥀', 'The drooping one'), [('🌷', 'The standing-up one', 'That one is healthy.')], 'O4'),
 GD('Is it good for a plant?', 'Good?', [('💧 a little water every day', 'yes'), ('🧊 a frosty night outside', 'no'), ('🌤️ a warm windowsill', 'yes'), ('🏜️ no water for weeks', 'no')], o='O4'),
 PM('How does a cactus live in the hot desert?', ('🌵', 'It stores water in its stem'), [('🧃', 'It drinks juice', 'It stores water.'), ('☂️', 'It has an umbrella', 'It stores water.')], 'O4'),
 YN('Can too much water hurt a plant?', True, 'O4', pic='🌊', why='Yes. Roots need some air too.'),
 PM('What do roots grow in?', ('🟫', 'Soil'), [('🥛', 'Milk', 'Roots grow in soil.'), ('🧱', 'Brick', 'Roots grow in soil.')], 'O4'),
 MT('Match each word to what it means.', [('wilt', 'droop with no water'), ('warm', 'a little hot'), ('soil', 'brown earth')], o='O4'),
 TK('Tick what a plant needs.', ['Needs', 'Does not need'], [('water', ['✓', '✗']), ('warmth', ['✓', '✗']), ('a hat', ['✗', '✓'])], o='O4'),
 OD('Order what happens to a plant with no water.', ['the soil dries out', 'the leaves droop', 'the plant wilts'], o='O4'),
 PM('Gardeners cover plants with fleece on frosty nights. Why?', ('🥶', 'To keep them from getting too cold'), [('🌙', 'To help them sleep', 'It keeps them warm.'), ('🎨', 'To make them pretty', 'It keeps them warm.')], 'O4', d='H'),
 YN('Does a wilted plant stand up again after a drink?', True, 'O4', pic='🌷', why='Yes, if it is watered in time.'),
)
s.adv(
 PM('* Advanced. Which plant will need watering most often?', ('🌞', 'One on a hot, sunny windowsill'), [('🌥️', 'One in a cool, shady room', 'Heat dries soil faster.'), ('🌧️', 'One outside in the rain', 'The rain waters it.')], 'O4', d='H'),
 PM('* Advanced. A plant needs light, water and…', ('🌡️', 'the right temperature'), [('🔊', 'loud music', 'It needs warmth.'), ('🍬', 'sweets', 'It needs warmth.')], 'O4', d='H'),
 GD('* Advanced. Too much, too little or just right?', 'Water', [('🌊 a flooded pot', 'too much'), ('🏜️ dry, cracked soil', 'too little'), ('💧 damp soil', 'just right')], o='O4', d='VH'),
)
s.labs('Water lab',
 test_lab('Water test', 'Three plants got different amounts of water for a week. Read how many leaves were still healthy.', 'Water each day', 'Healthy leaves', 'leaves', 10, 1,
  'Tap the number the bar reaches.', [('no water', '🏜️', 1), ('a little water', '💧', 9), ('a flood of water', '🌊', 4)],
  [PM('Which plant had the most healthy leaves?', ('💧', 'The one with a little water'), [('🏜️', 'The one with no water', 'It wilted.'), ('🌊', 'The flooded one', 'Too much water hurt it.')], 'O4')]),
 home('Water test', 'Find out if plants need water.', ['two small plants', 'water', 'a sunny place'], ['Wash your hands after touching soil.'],
  ['Put both plants in the same sunny place.', 'Water one plant every day.', 'Do not water the other one.', 'Look after one week.'],
  ['Plant', 'What did it look like?'], [('watered plant', ['standing up', 'wilting']), ('dry plant', ['standing up', 'wilting'])],
  [PM('Which plant wilted?', ('🏜️', 'The dry one'), [('💧', 'The watered one', 'It had water, so it stood up.')], 'O4')]))

U.mindmap(('Alive', 'living things eat, drink and grow', 'O1', '1.1'), ('Plant parts', 'roots, stem, leaves, flower', 'O2', '1.2'),
          ('Light', 'plants need light to grow', 'O3', '1.3'), ('Water and warmth', 'no water: plants wilt', 'O4', '1.4'))
