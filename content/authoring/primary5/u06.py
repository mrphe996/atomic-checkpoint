# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 5 · Unit 6 Seasons and adaptations. Written by the Atomic teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit5 import *

OBJ = {
 'O1': {'sec': '6.1', 'code': 'Earth and space', 'codeNote': '', 't': 'Describe how the Earth spins on a tilted axis (day and night) and orbits the Sun (a year).'},
 'O2': {'sec': '6.2', 'code': 'Earth and space', 'codeNote': '', 't': 'Explain how the tilt of the Earth causes the seasons, and describe seasonal changes, including near the equator.'},
 'O3': {'sec': '6.2', 'code': 'Working scientifically', 'codeNote': '', 't': 'Use shadow measurements to track the height of the Sun through the year.'},
 'O4': {'sec': '6.3', 'code': 'Biology', 'codeNote': '', 't': 'Describe how plants and animals are adapted to their environments and to seasonal changes.'},
 'O5': {'sec': '6.4', 'code': 'Biology', 'codeNote': '', 't': 'Describe adaptations of predators and prey, including camouflage and warning colours.'},
}
U = Unit(6, 'Seasons and adaptations', 'Earth and space; Biology', 'Why we have days, years and seasons, and how living things are adapted to survive.', OBJ)

# =====================================================================================  6.1
s = U.section('6.1', 'The Earth moving around the Sun', ['O1']); s.words(V['6.1']); core(s, 'O1', 'O1')
s.stop(MC('How long does the Earth take to orbit the Sun?', 'About 365 days (one year)', [('24 hours', 'That is one spin.'), ('About one month', 'That is about the Moon\'s orbit.'), ('One week', 'Much longer.')], o='O1'),
       MC('What is the path of the Earth around the Sun called?', 'Its orbit', [('Its axis', 'The axis is what it spins around.'), ('Its season', 'Seasons are parts of the year.')], o='O1'))
s.stop(MC('What causes day and night?', 'The Earth spinning on its axis', [('The Sun moving around the Earth', 'The Earth spins.'), ('The Moon covering the Sun', 'That is an eclipse.'), ('Clouds', 'Clouds do not cause night.')], o='O1'),
       MC('How long does the Earth take to spin once?', '24 hours', [('365 days', 'That is one orbit.'), ('One hour', 'Much longer.')], o='O1'))
s.prac(
 GD('Is each caused by the Earth spinning or the Earth orbiting the Sun?', 'Caused by', [('day and night', 'spinning'), ('a year', 'orbiting'), ('the Sun seeming to rise and set', 'spinning'), ('your birthday coming round again', 'orbiting')], o='O1'),
 MC('What is the Earth\'s axis?', 'An imaginary line the Earth spins around', [('The path around the Sun', 'That is the orbit.'), ('The equator', 'The axis goes through the poles.')], o='O1'),
 MC('What is special about the Earth\'s axis?', 'It is tilted', [('It is perfectly straight up', 'It leans over.'), ('It changes every day', 'It stays tilted the same way.')], o='O1'),
 MC('Why don\'t we feel the Earth moving?', 'Everything around us moves with us', [('The Earth is not moving', 'It spins and orbits.'), ('We are too heavy', 'Everything moves together.')], o='O1'),
 MC('If you are 10 years old, how many times have you travelled around the Sun?', '10', [('3650', 'That is about the number of days.'), ('1', 'Once a year, every year.')], o='O1'),
 MC('Why do we have a leap year every 4 years?', 'A year is about 365 and a quarter days', [('The Earth stops for a day', 'It is about quarter days.'), ('February gets tired', 'It is about the extra quarter day.')], o='O1'),
 CZ('Complete the sentences.', 'The Earth spins on its {0} once every {1} hours. It {2} the Sun once a year.', [['axis'], ['24', 'twenty-four'], ['orbits']], o='O1'),
 MC('When it is day in Vietnam, what is it like on the opposite side of the Earth?', 'Night', [('Also day', 'The other side faces away from the Sun.'), ('Winter', 'It is about day and night.')], o='O1'),
 MC('In the torch and globe model, what does the torch represent?', 'The Sun', [('The Moon', 'The torch is the Sun.'), ('A star far away', 'It is our Sun.')], o='O1'),
 MC('Which way does the Sun seem to move across the sky each day?', 'It rises in the east and sets in the west', [('It rises in the west', 'It rises in the east.'), ('It stays still', 'It seems to move because the Earth spins.')], o='O1'),
 TK('Tick the true statements.', ['True', 'False'], [('the Sun orbits the Earth', ['✗', '✓']), ('the Earth spins on its axis', ['✓', '✗']), ('a year is one orbit of the Sun', ['✓', '✗']), ('the Earth\'s axis is tilted', ['✓', '✗'])], o='O1'),
 MC('How fast does the Earth travel around the Sun?', 'About 30 kilometres every second', [('About 30 kilometres every year', 'Much faster!'), ('It does not move', 'It moves very fast.')], o='O1'),
 OD('Order from shortest to longest time.', ['one spin of the Earth', 'one orbit of the Moon', 'one orbit of the Earth around the Sun'], o='O1'),
 MC('About how many times does the Earth spin in one orbit of the Sun?', 'About 365', [('About 12', 'That is months.'), ('1', 'It spins every day.')], o='O1', d='H'),
)
s.adv(
 EX('Explain why the Sun seems to move across the sky during the day.', [('the Earth spins on its axis', ['spin', 'rotat']), ('the Sun does not really move', ['not move', 'still', 'stays']), ('so it seems to rise in the east and set in the west', ['east', 'west', 'rise', 'set'])], 'The Sun does not really move across the sky. The Earth spins on its axis, so the Sun seems to rise in the east, move across the sky and set in the west.', o='O1', d='H'),
 TB('Complete the table.', ['Time', 'Number of days'], [['1 year', '365'], ['2 years', B(730)], ['4 years (including a leap day)', B(1461)]], o='O1', skill='Data'),
 MC('A planet spins very slowly. What would its days be like?', 'Very long days and very long nights', [('Very short days', 'Slow spinning gives long days.'), ('No change', 'Spin speed sets day length.')], o='O1', d='VH'),
 MC('Which model best shows a year?', 'Walking a globe all the way around a torch', [('Spinning a globe once in front of a torch', 'That shows one day.'), ('Switching the torch off', 'That shows nothing.')], o='O1', d='H'),
)
s.labs('Earth model lab',
 sort_lab('Spin or orbit?', 'Is each thing caused by the Earth spinning on its axis, or by the Earth orbiting the Sun?', ['Spinning (24 hours)', 'Orbiting the Sun (1 year)'],
  [('day and night', '🌗', 0, 'One spin gives one day and night.'), ('a year', '🗓️', 1, 'One orbit is one year.'), ('sunrise and sunset', '🌅', 0, 'They happen as the Earth spins.'),
   ('your birthday coming round', '🎂', 1, 'One lap of the Sun each year.'), ('the seasons changing', '🍂', 1, 'Seasons come round once per orbit (with the tilt).'), ('shadows moving during the day', '🕰️', 0, 'They move as the Earth spins.')],
  [MC('What causes the seasons as well as the orbit?', 'The tilt of the Earth\'s axis', [('The Earth spinning faster', 'It is the tilt.'), ('The Moon', 'It is the tilt.')], o='O1'),
   MC('How long does one spin take?', '24 hours', [('One year', 'That is one orbit.'), ('One week', 'It is one day.')], o='O1')]),
 home('Torch and globe', 'Model day, night and a year.', ['a torch', 'a ball or globe', 'a pencil pushed through the ball (ask an adult)', 'a dark room'],
  ['Ask an adult to push the pencil through the ball.', 'Do not shine the torch into anyone\'s eyes.'],
  ['Shine the torch at the ball in a dark room.', 'Tilt the pencil a little and slowly spin the ball. Watch day and night move around it.', 'Count how many spins you make while you walk the ball once around the torch.', 'Record your counts.'],
  ['Model', 'Number'], [['Spins in one walk around the torch', {'min': 1, 'max': 400}], ['Times I walked around', {'min': 1, 'max': 20}]], 'The real Earth spins about 365 times in one orbit!',
  [MC('In your model, what did one walk around the torch show?', 'One year', [('One day', 'One spin is one day.'), ('One hour', 'One orbit is one year.')], o='O1')]))

# =====================================================================================  6.2
s = U.section('6.2', 'Seasonal changes', ['O2', 'O3']); s.words(V['6.2']); core(s, 'O2', 'O2')
s.stop(MC('In summer, is the Sun high or low in the sky?', 'High', [('Low', 'In winter it stays low.'), ('It does not rise', 'It rises high in summer.')], o='O2'),
       MC('Why are summer days warm?', 'Your half of the Earth leans towards the Sun, so the sunlight is stronger and the days are longer', [('The Earth is much closer to the Sun', 'It is the tilt that matters.'), ('There are fewer clouds every summer', 'It is the tilt.')], o='O2'))
s.stop(MC('When it is summer in the north, what season is it in the south?', 'Winter', [('Summer too', 'The halves have opposite seasons.'), ('Spring', 'It is the opposite season: winter.')], o='O2'),
       MC('In December it is winter in the UK. What season is it in Australia?', 'Summer', [('Winter', 'Australia is in the south.'), ('Autumn', 'It is summer.')], o='O2'))
s.prac(
 OD('Put the seasons in order, starting with spring.', ['spring', 'summer', 'autumn', 'winter'], o='O2'),
 MT('Match each season to what happens.', [('spring', 'new leaves and flowers grow'), ('summer', 'hot, long days'), ('autumn', 'many trees drop their leaves'), ('winter', 'cold, short days')], o='O2'),
 GD('Is each a feature of summer or winter (in places with four seasons)?', 'Season', [('long days', 'summer'), ('Sun low in the sky', 'winter'), ('long shadows at midday', 'winter'), ('warm weather', 'summer')], o='O2'),
 MC('What causes the seasons?', 'The tilt of the Earth as it orbits the Sun', [('The Earth spinning', 'That causes day and night.'), ('The Moon', 'The tilt causes seasons.')], o='O2'),
 MC('What are the seasons like near the equator?', 'Warm all year, with a wet season and a dry season', [('Four very different seasons', 'Near the equator it is warm all year.'), ('Always snowy', 'It is warm all year.')], o='O2'),
 MC('Why do some families in Australia eat Christmas lunch on the beach?', 'December is summer there', [('They live on the beach', 'It is summer in December.'), ('It is a rule', 'It is summer.')], o='O2'),
 CZ('Complete the sentences.', 'In summer the Sun is {0} and the days are {1}. In winter the Sun is {2} and the days are short.', [['high'], ['long'], ['low']], o='O2'),
 MC('What season is it when you\'re on a trampoline? (the joke)', 'Spring time!', [('Winter', 'It is a joke about bouncing.'), ('Fall', 'It is spring!')], o='O2'),
 MC('In the shadow stick experiment, what do you measure?', 'The length of the shadow at midday', [('The length of the stick', 'The stick stays the same.'), ('The temperature', 'Measure the shadow.')], o='O3'),
 MC('Why must the shadow be measured at the same time each month?', 'To keep the test fair', [('Because shadows are lazy', 'It is about fairness.'), ('Because the stick moves', 'The stick stays still.')], o='O3'),
 MC('A short shadow at midday means the Sun is…', 'high in the sky', [('low in the sky', 'Low Sun makes long shadows.'), ('behind a cloud', 'Then there would be no shadow.')], o='O3'),
 TB('Midday shadow of a 1 m stick in a northern country. Complete the table.', ['Month', 'Shadow (cm)', 'Sun high or low?'], [['June', '20', B('high')], ['March', '50', 'medium'], ['December', '90', B('low')]], o='O3', skill='Data', reason='Short shadow = high Sun; long shadow = low Sun.'),
 MC('In which season are there the most hours of daylight?', 'Summer', [('Winter', 'Winter days are short.'), ('Autumn', 'Summer has the most.')], o='O2'),
 MC('Why do many trees drop their leaves in autumn?', 'To save water during the cold winter', [('Because leaves get tired', 'It helps them survive winter.'), ('To make the ground colourful', 'It is to save water.')], o='O2', d='H'),
)
s.adv(
 EX('Explain why it is summer in the northern half of the Earth in June.', [('the Earth\'s axis is tilted', ['tilt']), ('in June the north leans towards the Sun', ['lean', 'towards', 'facing']), ('so the Sun is higher, days are longer and sunlight is stronger', ['high', 'long', 'strong', 'warm'])], 'The Earth\'s axis is tilted. In June the northern half leans towards the Sun, so the Sun is higher in the sky, the days are longer and the sunlight is stronger, making it summer.', o='O2', d='H'),
 GR('Plot the midday shadow length through the year.', {'label': 'Month (1 = January)', 'min': 0, 'max': 12, 'step': 2}, {'label': 'Shadow length (cm)', 'min': 0, 'max': 100, 'step': 20}, [[1, 85], [3, 50], [6, 20], [9, 50], [12, 90]], o='O3', d='H', table_rows=[[1, 85], [3, 50], [6, 20], [9, 50], [12, 90]]),
 MC('Using the graph, in which month was the Sun highest at midday?', 'June', [('December', 'The longest shadow means the lowest Sun.'), ('March', 'The shadow was medium.')], o='O3', d='H'),
 MC('The Earth is actually a little closer to the Sun in January. Why is January still winter in the north?', 'The tilt matters more than the distance', [('January is summer in the north', 'It is winter there.'), ('The Sun is colder in January', 'The tilt causes seasons.')], o='O2', d='VH'),
)
s.labs('Shadow lab',
 test_lab('How long is the midday shadow?', 'A 1 metre stick stands in the ground in a northern country. Read the tape to measure its midday shadow in different months.', 'The month', 'Shadow length', 'cm', 100, 10, '📏',
  [('June', '☀️', 20), ('March', '🌸', 50), ('September', '🍂', 50), ('December', '❄️', 90)],
  [MC('In which month was the shadow longest?', 'December', [('June', 'June had the shortest shadow.'), ('March', 'It was medium.')], o='O3'),
   MC('What does the long December shadow tell you?', 'The Sun is low in the sky in winter', [('The Sun is high', 'High Sun makes short shadows.'), ('The stick grew', 'The stick stays the same.')], o='O2')]),
 home('Shadow stick', 'Track the Sun with a shadow.', ['a stick or pencil', 'a sunny spot', 'a ruler', 'chalk or small stones to mark the shadow'],
  ['Never look directly at the Sun.', 'Ask an adult before pushing a stick into the ground.'],
  ['Stand the stick upright in a sunny spot.', 'Measure the shadow at 9 am, 12 noon and 3 pm.', 'Mark the tip of the shadow each time.', 'Record the lengths.'],
  ['Time', 'Shadow length (cm)'], [['9 am', {'min': 0, 'max': 500}], ['12 noon', {'min': 0, 'max': 500}], ['3 pm', {'min': 0, 'max': 500}]], 'Shadows are usually between 5 and 200 cm.',
  [MC('When was the shadow shortest?', 'At 12 noon, when the Sun is highest', [('At 9 am', 'The Sun is lower then.'), ('At 3 pm', 'The Sun is lower then.')], o='O3')]))

# =====================================================================================  6.3
s = U.section('6.3', 'Plants and animals adapted to their environments', ['O4']); s.words(V['6.3']); core(s, 'O4', 'O4')
s.stop(MC('What is an adaptation?', 'A feature that helps a living thing survive in its habitat', [('A type of habitat', 'It is a feature of a living thing.'), ('Moving to a new house', 'It is a feature that helps survival.'), ('A kind of food', 'It is a helpful feature.')], o='O4'),
       MC('Which is an adaptation of a polar bear?', 'Thick fur and a layer of fat', [('Big ears to lose heat', 'That suits a hot desert.'), ('Gills', 'Fish have gills.')], o='O4'))
s.stop(MC('Why do some birds migrate?', 'To fly to warmer places with more food in winter', [('Because they are bored', 'It helps them survive.'), ('To hibernate', 'Migrating is travelling.'), ('To change colour', 'Migrating is travelling.')], o='O4'),
       MC('What does "hibernate" mean?', 'Sleep through the winter', [('Fly to a warmer place', 'That is migrate.'), ('Change colour', 'That is a different adaptation.')], o='O4'))
s.prac(
 MT('Match each living thing to an adaptation.', [('polar bear', 'thick fur and fat to keep warm'), ('camel', 'wide feet that do not sink in sand'), ('fish', 'gills to breathe underwater'), ('cactus', 'a fat stem that stores water')], o='O4'),
 GD('Is each adaptation for a hot desert or a cold polar place?', 'Habitat', [('thick layer of fat', 'polar'), ('big ears that let heat out', 'desert'), ('white fur', 'polar'), ('stores water in its stem', 'desert')], o='O4'),
 MC('Why does a cactus have spines instead of big leaves?', 'Spines lose less water and stop animals eating it', [('Spines catch insects for food', 'They save water and protect it.'), ('Spines make it grow faster', 'They save water.')], o='O4'),
 MC('Why does a fennec fox have huge ears?', 'To let heat escape and keep cool', [('To keep warm', 'They help it lose heat.'), ('To swim', 'Foxes live in the desert.')], o='O4'),
 MC('Why does a polar bear have white fur?', 'To hide in the snow', [('To keep cool', 'It needs to keep warm.'), ('To attract other bears', 'It is camouflage.')], o='O4'),
 MC('How does an Arctic hare change with the seasons?', 'It grows white fur in winter and brown fur in summer', [('It grows wings', 'It changes fur colour.'), ('It hibernates in summer', 'It changes colour.')], o='O4'),
 MS('Select the ways animals cope with winter.', ['hibernate', 'migrate', 'grow thicker fur'], ['grow gills', 'drop their leaves'], o='O4'),
 CZ('Complete the sentences.', 'A feature that helps a living thing survive is an {0}. The place where it lives is its {1}. Bears {2} in winter.', [['adaptation'], ['habitat'], ['hibernate']], o='O4'),
 MC('What amazing thing does the wood frog do in winter?', 'It freezes almost solid and thaws out in spring', [('It flies south', 'Frogs do not fly.'), ('It grows thick fur', 'Frogs have no fur.')], o='O4'),
 MC('In the blubber glove test, which hand stayed warm longer?', 'The hand in the fat glove', [('The bare hand', 'Fat is a good insulator.'), ('They were the same', 'The fat insulated the hand.')], o='O4'),
 TB('Blubber glove results. How many seconds longer did the fat glove hand last?', ['Hand', 'Time comfortable in ice water (s)'], [['bare hand', '15'], ['fat glove', '90'], ['difference', B(75)]], o='O4', skill='Data'),
 MC('What does the blubber glove test show about polar animals?', 'Their fat keeps them warm in icy water', [('Fat makes them faster', 'It insulates them.'), ('They do not feel cold', 'Fat keeps heat in.')], o='O4'),
 MC('Why does a camel store fat in its hump?', 'So it can survive a long time without food', [('To keep cool', 'It stores energy.'), ('To float', 'It stores energy.')], o='O4', d='H'),
 MC('A plant has tiny leaves, deep roots and a thick, waxy stem. Where does it probably live?', 'A dry desert', [('A rainforest', 'It is adapted to save water.'), ('Under the sea', 'It is adapted to dry places.')], o='O4', d='H'),
)
s.adv(
 EX('Explain two ways a camel is adapted to life in the desert.', [('wide feet do not sink in sand', ['feet', 'sand']), ('stores fat in its hump / survives without food or water', ['hump', 'fat', 'store']), ('other: long eyelashes keep out sand', ['eyelash', 'eyelashes'])], 'Its wide feet stop it sinking into soft sand, and it stores fat in its hump so it can survive a long time without food.', o='O4', d='H'),
 GR('Plot the blubber glove results.', {'label': 'Test (1 bare hand, 2 fat glove)', 'min': 0, 'max': 3, 'step': 1}, {'label': 'Time comfortable (s)', 'min': 0, 'max': 100, 'step': 20}, [[1, 15], [2, 90]], o='O4', d='H', table_rows=[[1, 15], [2, 90]]),
 MC('Why might a polar bear struggle if the Arctic got much warmer?', 'Its thick fur and fat are adapted to the cold, and there would be less ice to hunt on', [('It would grow bigger ears', 'Adaptations take a very long time.'), ('Nothing would change', 'Its habitat would change.')], o='O4', d='VH'),
 MC('Which is NOT an adaptation to winter?', 'Growing bright flowers', [('Hibernating', 'That helps in winter.'), ('Migrating', 'That helps in winter.')], o='O4', d='H'),
)
s.labs('Blubber lab',
 test_lab('Does fat keep you warm?', 'Hands were put into ice water with and without a "blubber glove". Read the stopwatch: how long did each hand stay comfortable?', 'The glove', 'Time comfortable', 's', 100, 10, '⏱️',
  [('Bare hand', '✋', 15), ('Glove of cooking fat', '🧤', 90)],
  [MC('Which hand stayed comfortable longer?', 'The one in the fat glove', [('The bare hand', 'It lasted only 15 s.'), ('Both the same', 'The fat glove lasted much longer.')], o='O4'),
   MC('Which animal uses this adaptation?', 'A polar bear (and seals and whales)', [('A camel', 'Camels live in hot deserts.'), ('A cactus', 'A cactus is a plant.')], o='O4')]),
 home('Adaptation detective', 'Look for adaptations in plants and animals near you.', ['a notebook or the table below', 'a park, garden or a nature book'],
  ['Look, do not touch wild animals.', 'Go outside only with an adult.'],
  ['Find 3 living things.', 'For each, write one adaptation (e.g. a duck\'s webbed feet).', 'Count how many adaptations you can spot in 10 minutes.', 'Share your best one with your family.'],
  ['What I counted', 'Number'], [['Living things I looked at', {'min': 0, 'max': 100}], ['Adaptations I spotted', {'min': 0, 'max': 100}]], 'Write a whole number.',
  [MC('A duck has webbed feet. What are they adapted for?', 'Swimming', [('Climbing trees', 'Webbed feet push water.'), ('Digging', 'They are for swimming.')], o='O4')]))

# =====================================================================================  6.4
s = U.section('6.4', 'Adaptations of predators and prey', ['O5']); s.words(V['6.4']); core(s, 'O5', 'O5')
s.stop(MC('Why do many prey animals have eyes on the sides of their heads?', 'To see danger all around them', [('To see colours better', 'It gives a wide view.'), ('To judge distances when hunting', 'That is predators with front eyes.'), ('To look pretty', 'It helps them spot danger.')], o='O5'),
       MC('Why do predators like lions have eyes at the front?', 'To judge distances when they hunt', [('To see behind them', 'Front eyes judge distance.'), ('To sleep better', 'It helps hunting.')], o='O5'))
s.stop(MC('Why does a wasp have yellow and black stripes?', 'They are warning colours that say: I sting!', [('To hide in flowers', 'They stand out, not hide.'), ('To keep warm', 'They warn predators.'), ('To attract food', 'They are a warning.')], o='O5'),
       MC('What does camouflage do?', 'Helps an animal hide', [('Makes an animal faster', 'It helps it hide.'), ('Makes an animal poisonous', 'It is about hiding.')], o='O5'))
s.prac(
 GD('Is each animal mainly a predator or prey?', 'Role', [('lion', 'predator'), ('zebra', 'prey'), ('owl', 'predator'), ('mouse', 'prey'), ('shark', 'predator')], o='O5'),
 GD('Is each a predator adaptation or a prey adaptation?', 'Adaptation for', [('sharp teeth and claws', 'predator'), ('eyes on the sides of the head', 'prey'), ('silent flight', 'predator'), ('long legs for running away', 'prey')], o='O5'),
 MT('Match each animal to its adaptation.', [('chameleon', 'changes colour to match its surroundings'), ('stick insect', 'looks like a twig'), ('poison frog', 'bright warning colours'), ('puffer fish', 'puffs up to be too big to swallow')], o='O5'),
 MC('How do a tiger\'s stripes help it?', 'They hide it in tall grass so it can sneak up on prey', [('They warn other animals', 'Stripes camouflage the tiger.'), ('They keep it cool', 'They are camouflage.')], o='O5'),
 MC('Why are owls good at catching mice in the dark?', 'They fly almost silently and have excellent eyes and hearing', [('They glow in the dark', 'They fly silently.'), ('Mice cannot run', 'Mice are fast.')], o='O5'),
 MC('What are warning colours?', 'Bright colours that tell predators "don\'t eat me"', [('Colours that help an animal hide', 'That is camouflage.'), ('Colours for keeping warm', 'They are a warning.')], o='O5'),
 CZ('Complete the sentences.', 'A {0} hunts other animals. The animal it hunts is its {1}. Colours that help an animal hide are called {2}.', [['predator'], ['prey'], ['camouflage']], o='O5'),
 MS('Select the camouflage examples.', ['a stick insect on a twig', 'a white Arctic hare in snow', 'a green caterpillar on a leaf'], ['a bright red poison frog'], o='O5'),
 MC('I\'m green, on a leaf, and you can\'t see me. What am I? (the riddle)', 'A camouflaged caterpillar', [('A red apple', 'It is green and hidden.'), ('A poison frog', 'Poison frogs are bright.')], o='O5'),
 MC('In the wool worm hunt, which colour worms were found most?', 'The red ones, because they stood out on the grass', [('The green ones', 'Green worms were camouflaged.'), ('Both the same', 'Red stood out.')], o='O5'),
 TB('Wool worm hunt: 20 of each colour were hidden. How many were NOT found?', ['Colour', 'Found', 'Not found'], [['green', '4', B(16)], ['red', '16', B(4)]], o='O5', skill='Data'),
 MC('What does the worm hunt show?', 'Camouflage helps prey survive', [('Red is the best colour for hiding on grass', 'Red worms were found most.'), ('Birds like wool', 'It shows camouflage works.')], o='O5'),
 MC('Why might a harmless hoverfly have yellow and black stripes like a wasp?', 'Predators think it can sting, so they leave it alone', [('It is a wasp', 'It is a different insect.'), ('To keep warm', 'It copies the warning colours.')], o='O5', d='H'),
 MC('Why do zebras live in big herds?', 'Many eyes can spot predators, and it is harder to catch one', [('They like noise', 'It helps them stay safe.'), ('To hunt lions', 'Zebras are prey.')], o='O5', d='H'),
)
s.adv(
 EX('Explain how a chameleon\'s colour change helps it to survive.', [('it matches its surroundings / camouflage', ['match', 'camouflage', 'blend']), ('predators cannot see it easily', ['predator', 'see', 'hide']), ('it can also sneak up on insects to eat', ['insect', 'prey', 'catch', 'food'])], 'By changing colour to match its surroundings, the chameleon is camouflaged: predators cannot see it easily, and it can sneak up on insects to eat.', o='O5', d='H'),
 GR('Plot the worm hunt results.', {'label': 'Colour (1 green, 2 red)', 'min': 0, 'max': 3, 'step': 1}, {'label': 'Worms found', 'min': 0, 'max': 20, 'step': 4}, [[1, 4], [2, 16]], o='O5', d='H', table_rows=[[1, 4], [2, 16]]),
 MC('A predator and its prey both get faster over many, many years. Why?', 'Faster predators catch more food, and faster prey escape more often', [('They practise every day', 'It happens over generations.'), ('The weather gets warmer', 'It is about survival.')], o='O5', d='VH'),
 MC('Why is it useful for a poison frog to be easy to see?', 'Predators learn to avoid it, so it is not attacked', [('So it can find food', 'It is a warning.'), ('So it can hide', 'It wants to be seen.')], o='O5', d='H'),
)
s.labs('Camouflage lab',
 test_lab('Which worms are better hidden?', '20 green and 20 red wool worms were scattered on grass. A "bird" had one minute to find them. Read the counter.', 'The worm colour', 'Worms found', 'worms', 20, 2, '🐦',
  [('Green worms', '🟩', 4), ('Red worms', '🟥', 16)],
  [MC('Which worms were better camouflaged on grass?', 'The green worms', [('The red worms', 'Most red worms were found.'), ('Neither', 'Green hid much better.')], o='O5'),
   MC('Where would red worms be better hidden?', 'On red autumn leaves', [('On green grass', 'They stand out there.'), ('On white snow', 'They would stand out.')], o='O5')]),
 home('Camouflage hunt', 'Hide coloured paper "bugs" and test how well they are camouflaged.', ['10 paper squares of one colour and 10 of a bright colour', 'a garden, carpet or patterned rug', 'a helper and a timer'],
  ['Pick up all the paper afterwards.', 'Play somewhere safe.'],
  ['Choose a colour that matches the place, and a bright colour that does not.', 'Scatter 10 of each while your helper looks away.', 'Your helper has 30 seconds to collect bugs.', 'Count how many of each colour were found.'],
  ['Bug colour', 'Found (out of 10)'], [['Matching colour', {'min': 0, 'max': 10}], ['Bright colour', {'min': 0, 'max': 10}]], 'Each number is from 0 to 10.',
  [MC('Which bugs survived better?', 'The ones that matched the place', [('The bright ones', 'They were easy to find.'), ('Both the same', 'Camouflage helps.')], o='O5')]))

U.mindmap(('Days and years', 'Spin = day; orbit = year; tilted axis.', 'O1', '6.1'), ('Seasons', 'The tilt gives summer and winter.', 'O2', '6.2'),
          ('Shadow sticks', 'Short shadow: Sun high.', 'O3', '6.2'), ('Adaptations', 'Fur, fat, spines; hibernate and migrate.', 'O4', '6.3'), ('Predators and prey', 'Camouflage and warning colours.', 'O5', '6.4'))
