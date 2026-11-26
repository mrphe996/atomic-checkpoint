# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 5 · Unit 1 Life cycles of flowering plants. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit5 import *

OBJ = {
 'O1': {'sec': '1.1', 'code': 'Biology', 'codeNote': '', 't': 'Sort plants into flowering and non-flowering plants, and name the parts of a flower and their jobs.'},
 'O2': {'sec': '1.2', 'code': 'Biology', 'codeNote': '', 't': 'Describe pollination by insects and wind, fertilisation, and how the ovary becomes a fruit with seeds.'},
 'O3': {'sec': '1.3', 'code': 'Biology', 'codeNote': '', 't': 'Explain why seeds are dispersed and describe dispersal by wind, animals, water and exploding pods.'},
 'O4': {'sec': '1.3', 'code': 'Working scientifically', 'codeNote': '', 't': 'Plan a fair test with model seeds, repeat measurements and find an average.'},
 'O5': {'sec': '1.4', 'code': 'Biology', 'codeNote': '', 't': 'Describe the conditions seeds need to germinate and the life cycle of a flowering plant.'},
}
U = Unit(1, 'Life cycles of flowering plants', 'Biology: life processes', 'Flowers, bees, fruits, flying seeds and germination – the whole life cycle of a flowering plant.', OBJ)

# =====================================================================================  1.1
s = U.section('1.1', 'Flowering and non-flowering plants', ['O1']); s.words(V['1.1']); core(s, 'O1', 'O1')
s.stop(MC('Is a fern a flowering plant or a non-flowering plant?', 'A non-flowering plant', [('A flowering plant', 'A fern never grows flowers.'), ('It is not a plant', 'Ferns are plants.')], o='O1', reason='Ferns never grow flowers. They make spores.'),
       MC('Which of these is a non-flowering plant?', 'Moss', [('Sunflower', 'A sunflower has a huge flower.'), ('Apple tree', 'Apple trees grow flowers.')], o='O1'))
s.stop(MC('Which part of a flower makes pollen?', 'The stamen', [('The petal', 'Petals attract insects.'), ('The sepal', 'Sepals protect the bud.'), ('The carpel', 'Seeds grow in the carpel.')], o='O1'),
       MC('What is the job of the bright petals?', 'To attract insects', [('To make seeds', 'Seeds grow in the carpel.'), ('To make pollen', 'Stamens make pollen.')], o='O1'))
s.prac(
 GD('Is each plant a flowering plant or a non-flowering plant?', 'Group', [('rose', 'flowering plant'), ('fern', 'non-flowering plant'), ('grass', 'flowering plant'), ('moss', 'non-flowering plant'), ('mango tree', 'flowering plant')], o='O1'),
 MC('What do ferns and mosses make instead of seeds?', 'Spores', [('Fruits', 'Fruits come from flowers.'), ('Cones', 'Pine trees make cones.'), ('Pollen', 'Pollen comes from flowers.')], o='O1'),
 MC('Grass is a flowering plant. Why do many people think it is not?', 'Its flowers are small and green, so they are hard to notice', [('It never grows flowers', 'Grass does have flowers.'), ('It grows spores', 'Grass makes seeds.')], o='O1', d='H'),
 MT('Match each part of a flower to its job.', [('petal', 'attracts insects'), ('stamen', 'makes pollen'), ('carpel', 'where seeds grow'), ('sepal', 'protects the bud')], o='O1'),
 MC('Which part of the flower is the female part?', 'The carpel', [('The stamen', 'The stamen is the male part.'), ('The petal', 'Petals are not male or female parts.')], o='O1'),
 MC('Which part protected the flower when it was a bud?', 'The sepals', [('The roots', 'Roots are under the ground.'), ('The pollen', 'Pollen is made by stamens.')], o='O1'),
 MC('What does a pine tree make instead of flowers?', 'Cones', [('Spores', 'Ferns and mosses make spores.'), ('Petals', 'Petals are part of flowers.')], o='O1'),
 CZ('Complete the sentences.', 'Flowering plants grow {0}, which make {1}. Ferns make tiny {2}.', [['flowers'], ['seeds'], ['spores']], o='O1'),
 MC('Where can you find a fern\'s spores?', 'In brown dots under its leaves', [('Inside a fruit', 'Ferns do not make fruits.'), ('In its flowers', 'Ferns have no flowers.')], o='O1'),
 MC('Why does the biggest flower in the world smell like rotten meat?', 'To attract flies that carry its pollen', [('To scare away bees', 'It wants insects to visit.'), ('Because it is dying', 'The smell has a job.')], o='O1'),
 TK('Tick what is true about flowering plants.', ['True', 'False'], [('they make seeds', ['✓', '✗']), ('all of them have big, bright flowers', ['✗', '✓']), ('trees can be flowering plants', ['✓', '✗']), ('they make spores', ['✗', '✓'])], o='O1'),
 MC('Why should you wash your hands after taking a flower apart?', 'Some plants can irritate skin or be poisonous', [('Flowers are hot', 'That is not the reason.'), ('To make the flower grow', 'It is about staying safe.')], o='O1'),
 OD('Order the parts of a flower from the outside to the middle.', ['sepals', 'petals', 'stamens', 'carpel'], o='O1', d='H'),
 MC('A plant has spores under its leaves and no flowers. What is it most likely to be?', 'A fern', [('A rose', 'Roses have flowers.'), ('A bean plant', 'Bean plants have flowers.')], o='O1'),
)
s.adv(
 EX('Explain how you would decide if a plant is a flowering or non-flowering plant.', [('look for flowers (or fruits/seeds)', ['flower', 'fruit', 'seed']), ('look for spores or cones', ['spore', 'cone'])], 'Look for flowers, fruits or seeds: then it is a flowering plant. If it has spores or cones instead and never flowers, it is a non-flowering plant.', o='O1', d='H'),
 TB('Ana counted the parts of a lily. Complete the table: a lily has 6 petals, 6 stamens and 1 carpel.', ['Part', 'Number'], [['petals', B(6)], ['stamens', B(6)], ['carpel', B(1)]], o='O1', skill='Data'),
 MC('Why do wind-pollinated flowers not need bright petals?', 'They do not need to attract insects', [('They have no pollen', 'They make lots of pollen.'), ('Wind likes dull colours', 'The wind does not see colours.')], o='O1', d='VH'),
 MC('A plant makes cones. Which group is it in?', 'Non-flowering plants', [('Flowering plants', 'Cones are not flowers.'), ('Mosses', 'Mosses make spores, not cones.')], o='O1', d='H'),
)
s.labs('Plant sorting lab',
 sort_lab('Flowering or non-flowering?', 'Sort each plant into the right group.', ['Flowering plant', 'Non-flowering plant'],
  [('sunflower', '🌻', 0, 'It grows a big flower.'), ('fern', '🌿', 1, 'Ferns make spores, not flowers.'), ('apple tree', '🍎', 0, 'Apple trees flower before they make apples.'), ('moss', '🟩', 1, 'Moss makes spores.'),
   ('rose', '🌹', 0, 'Roses are flowers!'), ('pine tree', '🌲', 1, 'Pine trees make cones, not flowers.'), ('grass', '🌾', 0, 'Grass has tiny green flowers.')],
  [MC('Which plant surprised you by being a flowering plant?', 'Grass', [('Fern', 'Ferns never flower.'), ('Moss', 'Moss never flowers.')], o='O1'),
   MC('What do the non-flowering plants make instead of seeds?', 'Spores or cones', [('Fruits', 'Fruits come from flowers.'), ('Nectar', 'Nectar is in flowers.')], o='O1')]),
 home('Take a flower apart', 'Find out what is inside a flower.', ['a large flower (e.g. a lily or hibiscus) – ask first!', 'a white sheet of paper and sticky tape', 'a magnifying glass if you have one'],
  ['Ask an adult before you pick any flower.', 'Wash your hands afterwards – some plants can irritate skin.'],
  ['Gently pull off the sepals and the petals.', 'Find the stamens with pollen on the top.', 'Find the carpel in the middle.', 'Count each part and stick them on paper.'],
  ['Part', 'How many I found'], [['Petals', {'min': 0, 'max': 60}], ['Stamens', {'min': 0, 'max': 200}], ['Carpels', {'min': 0, 'max': 20}]], 'Write 0 if you could not find a part.',
  [MC('Which part had yellow powder on it?', 'The stamens – it was pollen', [('The petals', 'Pollen is made by the stamens.'), ('The sepals', 'Sepals are the green outer parts.')], o='O1')]))

# =====================================================================================  1.2
s = U.section('1.2', 'Pollination, fruits and seeds', ['O2']); s.words(V['1.2']); core(s, 'O2', 'O2')
s.stop(MC('What is pollination?', 'Moving pollen from a stamen to a stigma', [('A seed starting to grow', 'That is germination.'), ('Seeds being spread', 'That is seed dispersal.'), ('Petals falling off', 'That happens after fertilisation.')], o='O2'),
       MC('Which animal often carries pollen?', 'A bee', [('A fish', 'Fish do not visit flowers.'), ('A worm', 'Worms live in soil.')], o='O2'))
s.stop(MC('Which part of the flower becomes the fruit?', 'The ovary', [('The petals', 'Petals fall off.'), ('The stamen', 'Stamens make pollen.'), ('The roots', 'Roots are under the ground.')], o='O2'),
       MC('What happens to the petals after fertilisation?', 'They fall off', [('They turn into seeds', 'Seeds grow in the ovary.'), ('They grow bigger', 'The flower no longer needs them.')], o='O2'))
s.prac(
 OD('Put the steps in order.', ['a bee drinks nectar', 'pollen sticks to the bee', 'the bee visits another flower', 'pollen lands on the stigma'], o='O2'),
 MC('Why do flowers make sweet nectar?', 'To attract insects that will carry their pollen', [('To feed the seeds', 'Nectar is for visiting insects.'), ('To make the petals bright', 'Nectar is a sweet liquid.')], o='O2'),
 GD('Is each flower more likely to be pollinated by insects or by the wind?', 'Pollinated by', [('big, bright, sweet-smelling flower', 'insects'), ('small, plain, green grass flower', 'wind'), ('flower full of nectar', 'insects')], o='O2'),
 MC('What is fertilisation?', 'When pollen joins with an egg cell', [('When pollen lands on a petal', 'Pollen must join an egg cell.'), ('When a seed grows', 'That is germination.')], o='O2'),
 MC('To a scientist, why is a tomato a fruit?', 'It grew from a flower and has seeds inside', [('It is sweet', 'Not all fruits are sweet.'), ('It is red', 'Colour does not make a fruit.')], o='O2'),
 MS('Select all the fruits.', ['tomato', 'cucumber', 'pepper', 'apple'], ['carrot', 'potato'], o='O2', reason='A fruit holds seeds. Carrots and potatoes are roots and stems.'),
 MC('Where are a strawberry\'s seeds?', 'On the outside', [('Inside, in the middle', 'Strawberries wear them outside.'), ('It has no seeds', 'It has about 200!')], o='O2'),
 MC('Where does pollen land in pollination?', 'On the stigma', [('On the petals', 'It must reach the stigma.'), ('On the leaves', 'Leaves are not part of the flower.')], o='O2'),
 CZ('Complete the sentences.', 'Moving pollen to the stigma is called {0}. When pollen joins an egg cell, it is called {1}. The {2} then becomes the fruit.', [['pollination'], ['fertilisation', 'fertilization'], ['ovary']], o='O2'),
 MC('Why are bees important to farmers?', 'They pollinate crops so fruits and seeds can form', [('They eat pests', 'Bees drink nectar.'), ('They water plants', 'They carry pollen.')], o='O2'),
 MC('Why do wind-pollinated plants make lots of pollen?', 'Most of the pollen blows away and is lost', [('Insects eat it', 'Wind flowers rely on wind.'), ('Pollen is heavy', 'Wind pollen is light.')], o='O2', d='H'),
 TK('Tick the things a fruit does.', ['Yes', 'No'], [('protects the seeds', ['✓', '✗']), ('helps spread the seeds', ['✓', '✗']), ('makes pollen', ['✗', '✓'])], o='O2'),
 MC('Which comes first?', 'Pollination', [('Fertilisation', 'Pollen must arrive first.'), ('A fruit forms', 'That is last.')], o='O2'),
 MC('Bella the bee visits a sunflower, then a rose. Can she pollinate the rose with sunflower pollen?', 'No – pollen must go to a flower of the same kind', [('Yes – any pollen works', 'Pollen only works on the same kind of plant.'), ('Yes, but only in the morning', 'Time does not matter.')], o='O2', d='H'),
)
s.adv(
 EX('Explain how a flower becomes a fruit.', [('pollination: pollen reaches the stigma', ['pollinat', 'stigma']), ('fertilisation: pollen joins an egg cell', ['fertilis', 'fertiliz', 'egg']), ('the ovary swells into a fruit with seeds', ['ovary', 'swell', 'fruit'])], 'Pollen reaches the stigma (pollination), then joins an egg cell (fertilisation). The petals fall off and the ovary swells into a fruit with seeds inside.', o='O2', d='H'),
 TB('Lily counted seeds in fruits. Find the total number of seeds.', ['Fruit', 'Seeds'], [['apple', '10'], ['orange', '15'], ['pepper', '90'], ['total', B(115)]], o='O2', skill='Data'),
 MC('Some farmers keep beehives next to their apple trees. Why?', 'More bees means more flowers are pollinated, so there are more apples', [('Bees protect the trees from rain', 'Bees pollinate.'), ('Bees eat the apples', 'Bees drink nectar.')], o='O2', d='VH'),
 MC('Which is NOT needed for a fruit to form?', 'Roots touching the flower', [('Pollination', 'Pollination is needed.'), ('Fertilisation', 'Fertilisation is needed.')], o='O2', d='H'),
)
s.labs('Seed count lab',
 test_lab('How many seeds?', 'Each fruit was cut in half and its seeds counted. Read the counter for each fruit.', 'The fruit', 'Number of seeds', 'seeds', 100, 10, '🔢',
  [('Apple', '🍎', 10), ('Orange', '🍊', 15), ('Tomato', '🍅', 80), ('Pepper', '🫑', 90)],
  [MC('Which fruit had the most seeds?', 'Pepper', [('Apple', 'The apple had about 10.'), ('Orange', 'The orange had about 15.')], o='O2'),
   MC('Where did all these seeds come from?', 'The ovary of the flower, after fertilisation', [('From the soil', 'Seeds form inside the fruit.'), ('From the leaves', 'Seeds form in the ovary.')], o='O2')]),
 home('Fruit seed hunt', 'Count the seeds in fruits from your kitchen.', ['3 different fruits (e.g. apple, orange, tomato)', 'a plate', 'an adult to cut the fruits'],
  ['Only an adult should use the knife.', 'Wash your hands afterwards.'],
  ['Ask an adult to cut each fruit in half.', 'Pick out the seeds and count them.', 'Write the numbers in the table.', 'Eat the fruit!'],
  ['Fruit', 'Number of seeds'], [['Fruit 1', {'min': 0, 'max': 1000}], ['Fruit 2', {'min': 0, 'max': 1000}], ['Fruit 3', {'min': 0, 'max': 1000}]], 'Write 0 if a fruit had no seeds.',
  [MC('Why do you think some fruits have many seeds?', 'More seeds give more chances for new plants to grow', [('Seeds make the fruit heavy', 'Think about new plants.'), ('It does not matter', 'Seeds make new plants.')], o='O2')]))

# =====================================================================================  1.3
s = U.section('1.3', 'How seeds are spread', ['O3', 'O4']); s.words(V['1.3']); core(s, 'O3', 'O3')
s.stop(MC('Why do plants need to spread their seeds?', 'So the new plants have enough light, water and space', [('So the seeds stay warm', 'It is about space and resources.'), ('So animals cannot find them', 'Animals often help spread them.'), ('Because seeds are heavy', 'That is not the reason.')], o='O3'),
       MC('What is seed dispersal?', 'Spreading seeds away from the parent plant', [('Seeds starting to grow', 'That is germination.'), ('Pollen joining an egg cell', 'That is fertilisation.')], o='O3'))
s.stop(MC('How are burrs spread?', 'Their hooks catch on animal fur', [('By the wind', 'Burrs are too heavy and hooked.'), ('By floating on water', 'Coconuts float.'), ('By exploding', 'Pods explode.')], o='O3'),
       MC('How are dandelion seeds spread?', 'By the wind', [('By animals eating them', 'They float on tiny parachutes.'), ('By water', 'They fly.')], o='O3'))
s.prac(
 GD('How is each seed spread?', 'Spread by', [('dandelion', 'wind'), ('sycamore', 'wind'), ('cherry eaten by a bird', 'animals'), ('burr', 'animals'), ('coconut', 'water'), ('pea pod', 'exploding')], o='O3'),
 MC('What helps a sycamore seed travel far?', 'Wings that make it spin', [('Hooks', 'Burrs have hooks.'), ('A juicy fruit', 'Berries are eaten.')], o='O3'),
 MC('Why are wind-dispersed seeds usually light?', 'So the wind can carry them far', [('So animals can eat them', 'They travel by wind.'), ('So they sink', 'They need to fly.')], o='O3'),
 MC('Why are many berries bright and juicy?', 'To attract animals to eat them and spread the seeds', [('To scare animals away', 'They want to be eaten!'), ('To float on water', 'Berries are eaten.')], o='O3'),
 MC('How does a seed eaten by a bird reach a new place?', 'It passes through the bird and comes out in its droppings', [('The bird plants it with its beak', 'Birds do not plant seeds.'), ('It is digested completely', 'Many seeds survive.')], o='O3'),
 MC('Why can a coconut be dispersed by water?', 'It is light enough to float for weeks', [('It has wings', 'Coconuts have no wings.'), ('It has hooks', 'Burrs have hooks.')], o='O3'),
 MT('Match each seed feature to the way it is spread.', [('parachute of hairs', 'wind'), ('tiny hooks', 'animal fur'), ('juicy fruit', 'eaten by animals'), ('pod that dries and twists', 'exploding')], o='O3'),
 CZ('Complete the sentences.', 'Spreading seeds is called seed {0}. Dandelions use {1} dispersal. Burrs use {2} dispersal.', [['dispersal'], ['wind'], ['animal']], o='O3'),
 MC('In the paper helicopter test, what should you change?', 'The length of the wings', [('The height you drop from', 'Keep that the same.'), ('The paper', 'Use the same paper.')], o='O4'),
 MC('In the paper helicopter test, what should you measure?', 'The time it takes to land', [('The colour of the paper', 'Measure the time.'), ('The weight of the timer', 'Measure the falling time.')], o='O4'),
 MS('What should stay the SAME in the helicopter test?', ['the height of the drop', 'the type of paper', 'the person timing'], ['the wing length'], o='O4'),
 TB('Each helicopter was dropped three times. Find the average time.', ['Wings', 'Drop 1 (s)', 'Drop 2 (s)', 'Drop 3 (s)', 'Average (s)'], [['short', '1.1', '0.9', '1.0', B(1.0, 0.05)], ['long', '2.4', '2.6', '2.5', B(2.5, 0.05)]], o='O4', skill='Data', reason='Add the three times and divide by 3.'),
 MC('Why do scientists repeat each drop three times?', 'To make the results more reliable', [('To tire out the helicopter', 'Repeats check the results.'), ('Because three is lucky', 'It is about reliable results.')], o='O4'),
 MC('What do the helicopter results show?', 'Longer wings make the seed fall more slowly', [('Longer wings make it fall faster', 'The times got longer.'), ('Wing length does not matter', 'The times changed.')], o='O4'),
)
s.adv(
 EX('Explain why a seed that falls slowly is likely to travel further.', [('it stays in the air longer', ['longer', 'more time', 'air']), ('so the wind can carry it further', ['wind', 'carry', 'blow'])], 'A seed that falls slowly stays in the air for longer, so the wind has more time to carry it further away.', o='O4', d='H'),
 GR('Plot the helicopter results.', {'label': 'Wing length (cm)', 'min': 0, 'max': 10, 'step': 2}, {'label': 'Average fall time (s)', 'min': 0, 'max': 4, 'step': 1}, [[2, 1.0], [4, 1.5], [6, 2.0], [8, 2.5]], o='O4', d='H', table_rows=[[2, 1.0], [4, 1.5], [6, 2.0], [8, 2.5]]),
 MC('A seed has a hard shell and can float. Where does its parent plant probably grow?', 'Near water, like a beach or river', [('In a dry desert', 'Floating seeds need water.'), ('High on a mountain with no rivers', 'It needs water to travel.')], o='O3', d='H'),
 MC('Why might it be bad if all of a tree\'s seeds landed under it?', 'They would compete with each other and the tree for light, water and space', [('They would be too warm', 'It is about competition.'), ('Birds could not see them', 'That is not the main problem.')], o='O3', d='VH'),
)
s.labs('Helicopter seed lab',
 test_lab('How does wing length change falling time?', 'Paper helicopters with different wing lengths were dropped from 2 metres. Read the stopwatch scale to find the average time to land.', 'The wing length', 'Time to land', 's', 4, 0.5, '⏱️',
  [('Short wings (2 cm)', '🚁', 1.0), ('Medium wings (4 cm)', '🚁', 1.5), ('Long wings (8 cm)', '🚁', 2.5)],
  [MC('What happened as the wings got longer?', 'The seed took longer to land', [('It landed faster', 'Look at your bars.'), ('Nothing changed', 'The times changed.')], o='O4'),
   MC('Which real seed is most like the long-winged helicopter?', 'A sycamore seed', [('A coconut', 'Coconuts float on water.'), ('A burr', 'Burrs hook onto fur.')], o='O3')]),
 home('Paper helicopter seeds', 'Make your own spinning seeds and test them.', ['paper', 'scissors', 'a paper clip', 'a timer', 'a safe place to drop from (ask an adult)'],
  ['Never lean out of windows or climb on furniture.', 'Use scissors carefully.'],
  ['Make two paper helicopters: one with short wings and one with long wings.', 'Add a paper clip to the bottom of each.', 'Drop each from the same height and time how long it takes to land.', 'Repeat three times and work out the average.'],
  ['Helicopter', 'Average time to land (s)'], [['Short wings', {'min': 0.1, 'max': 20}], ['Long wings', {'min': 0.1, 'max': 20}]], 'Times are usually between 0.5 and 5 seconds.',
  [MC('Which helicopter usually takes longer to land?', 'The one with long wings', [('The one with short wings', 'Longer wings catch more air.'), ('They always take the same time', 'Wing length matters.')], o='O4')]))

# =====================================================================================  1.4
s = U.section('1.4', 'Seed germination', ['O5']); s.words(V['1.4']); core(s, 'O5', 'O5')
s.stop(MC('What three things does a seed need to germinate?', 'Water, warmth and air', [('Light, soil and sugar', 'Seeds do not need light to start.'), ('Water, light and wind', 'Seeds need warmth and air, not light.'), ('Soil, music and water', 'Not music!')], o='O5'),
       MC('Does a seed need light to germinate?', 'No – it uses its food store', [('Yes – always', 'Seeds germinate in the dark.'), ('Only red light', 'No light is needed to start.')], o='O5'))
s.stop(MC('In the life cycle, what comes after pollination?', 'Fertilisation, then fruit and seeds', [('Germination', 'Germination starts the cycle again later.'), ('Flowering', 'Flowering comes before pollination.')], o='O5'),
       OD('Put the life cycle in order, starting with a seed.', ['seed', 'germination', 'young plant', 'flowering', 'pollination', 'fruit and seeds'], o='O5'))
s.prac(
 MC('What is germination?', 'When a seed starts to grow', [('When a flower opens', 'That is flowering.'), ('When seeds are spread', 'That is dispersal.')], o='O5'),
 MC('Which grows first when a seed germinates?', 'The root', [('The flower', 'Flowers come much later.'), ('The fruit', 'Fruits come much later.')], o='O5'),
 MC('Which way does a root always grow?', 'Down, towards water', [('Up, towards the light', 'That is the shoot.'), ('Sideways only', 'Roots grow down.')], o='O5'),
 MC('Which way does a shoot grow?', 'Up, towards the light', [('Down into the soil', 'That is the root.'), ('It does not grow', 'Shoots grow up.')], o='O5'),
 MS('Select the conditions a seed needs to germinate.', ['water', 'warmth', 'air'], ['light', 'fertiliser', 'music'], o='O5'),
 MC('What is inside a seed?', 'A baby plant and a store of food', [('Only water', 'There is a baby plant inside.'), ('Pollen', 'Pollen is made by stamens.')], o='O5'),
 MC('Why does a young plant need light once its leaves open?', 'To make its own food', [('To keep warm', 'Leaves use light to make food.'), ('To grow roots', 'Light is used by the leaves.')], o='O5'),
 MT('Match each stage to what happens.', [('germination', 'the seed starts to grow'), ('flowering', 'the plant grows flowers'), ('pollination', 'pollen reaches the stigma'), ('dispersal', 'seeds are spread')], o='O5'),
 MC('In the cress test, what was changed?', 'Whether the seeds had water', [('The type of seed', 'Both dishes had cress.'), ('The temperature', 'Both were kept warm.')], o='O5'),
 TB('Cress seeds were tested for a week. 20 seeds were in each dish. Complete the table.', ['Dish', 'Seeds that germinated', 'Seeds that did not'], [['watered, warm', '18', B(2)], ['dry, warm', '0', B(20)], ['watered, in fridge', '3', B(17)]], o='O5', skill='Data', reason='20 − number that germinated.'),
 MC('What do the cress results show?', 'Seeds need water and warmth to germinate', [('Seeds need cold to germinate', 'Few grew in the fridge.'), ('Seeds need no water', 'None grew in the dry dish.')], o='O5'),
 CZ('Complete the life cycle.', 'seed → {0} → young plant → {1} → pollination → fruit and {2}', [['germination'], ['flowering'], ['seeds']], o='O5'),
 MC('A bean is planted upside down. What will its root do?', 'Turn and grow downwards', [('Grow upwards', 'Roots always turn down.'), ('Stop growing', 'It keeps growing.')], o='O5'),
 MC('How old were the date palm seeds that still germinated?', 'About 2000 years old', [('About 2 years old', 'Much, much older.'), ('About 20 years old', 'Much older.')], o='O5'),
)
s.adv(
 EX('Explain why seeds can germinate in a dark cupboard, but seedlings soon need light.', [('the seed has a food store', ['food store', 'stored food', 'food']), ('after the leaves open the plant must make its own food', ['make', 'own food']), ('using light', ['light'])], 'A seed uses its own food store to start growing, so it does not need light. Once the leaves open and the food runs out, the young plant needs light to make its own food.', o='O5', d='H'),
 GR('Plot how many seeds germinated each day (out of 20).', {'label': 'Day', 'min': 0, 'max': 6, 'step': 1}, {'label': 'Seeds germinated', 'min': 0, 'max': 20, 'step': 4}, [[1, 0], [2, 4], [3, 10], [4, 16], [5, 18]], o='O5', d='H', table_rows=[[1, 0], [2, 4], [3, 10], [4, 16], [5, 18]]),
 MC('Why should both dishes in the cress test be kept in the same place?', 'So that warmth is the same – only water changes', [('So they look tidy', 'It is about a fair test.'), ('So the seeds can talk', 'Fair tests change one thing only.')], o='O5', d='H'),
 MC('Why is the life cycle called a cycle?', 'It goes round and round: new seeds start it again', [('It has wheels', 'A cycle repeats.'), ('It happens only once', 'It repeats.')], o='O5', d='VH'),
)
s.labs('Germination lab',
 test_lab('What do seeds need to germinate?', '20 cress seeds were kept in different conditions for one week. Read the counter: how many germinated?', 'The conditions', 'Seeds germinated', 'seeds', 20, 2, '🌱',
  [('Water + warm + dark', '🌑', 18), ('Water + warm + light', '☀️', 18), ('No water + warm', '🏜️', 0), ('Water + cold (fridge)', '🧊', 3)],
  [MC('Did light make a difference to germination?', 'No – the same number germinated in the dark and the light', [('Yes – none grew in the dark', '18 grew in the dark.'), ('Yes – more grew in the dark', 'They were the same.')], o='O5'),
   MC('Which condition stopped all the seeds germinating?', 'No water', [('The dark', 'Seeds germinated in the dark.'), ('The light', 'Seeds germinated in the light.')], o='O5')]),
 home('Cress test', 'Find out if seeds need water to germinate.', ['cress or mustard seeds', '2 saucers', 'cotton wool or kitchen paper', 'water'],
  ['Do not eat seeds from packets that may be treated.', 'Wash your hands after handling seeds.'],
  ['Put cotton wool on two saucers and sprinkle 20 seeds on each.', 'Water one saucer every day. Keep the other one dry.', 'Keep both in the same warm place.', 'After 5 days, count the seeds that have germinated.'],
  ['Saucer', 'Seeds that germinated (out of 20)'], [['Watered', {'min': 0, 'max': 20}], ['Dry', {'min': 0, 'max': 20}]], 'Count seeds with a root or shoot.',
  [MC('What does your test show?', 'Seeds need water to germinate', [('Seeds need no water', 'Check the dry saucer.'), ('Water stops germination', 'The watered seeds grew.')], o='O5')]))

U.mindmap(('Flowering plants', 'Flowers make seeds; ferns and mosses make spores.', 'O1', '1.1'), ('Pollination', 'Insects and wind carry pollen; the ovary becomes a fruit.', 'O2', '1.2'),
          ('Seed dispersal', 'Wind, animals, water and exploding pods.', 'O3', '1.3'), ('Fair tests', 'Model seeds; repeat and average.', 'O4', '1.3'), ('Germination and life cycle', 'Water, warmth and air.', 'O5', '1.4'))
