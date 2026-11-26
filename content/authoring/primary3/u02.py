# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 3 · Unit 2 Mixing materials. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit3 import *

OBJ = {
 'O1': {'sec': '2.1', 'code': 'Chemistry', 'codeNote': '', 't': 'Sort materials into solids, liquids and gases, and describe how each behaves.'},
 'O2': {'sec': '2.2', 'code': 'Chemistry', 'codeNote': '', 't': 'Know what a mixture is, and separate a mixture by picking out or sieving.'},
 'O3': {'sec': '2.3', 'code': 'Chemistry', 'codeNote': '', 't': 'Know that some solids dissolve in water and some do not, and that warmth and stirring help.'},
 'O4': {'sec': '2.4', 'code': 'Chemistry', 'codeNote': '', 't': 'Use a filter to separate an insoluble solid from water, and know filtered water is not safe to drink.'},
 'O5': {'sec': '2.5', 'code': 'Chemistry', 'codeNote': '', 't': 'Know that useful materials come from rocks, and that magnets and evaporation can separate them.'},
}
U = YUnit(2, 'Mixing materials', 'Chemistry: materials', 'Solids, liquids and gases, mixtures, sieving, dissolving, filtering and materials from rocks.', OBJ)

# ============================================================  2.1
s = U.section('2.1', 'Solids, liquids and gases', ['O1']); s.words(V['2.1']); core(s, 'O1')
s.stop(PM('Which one is a liquid?', ('🥛', 'Milk'), [('🧱', 'A brick', 'A brick is a solid.'), ('🎈', 'Air in a balloon', 'Air is a gas.')], 'O1'),
       PM('Which one can you pour?', ('🧃', 'Juice'), [('🪨', 'A stone', 'A stone is a solid.'), ('🧸', 'A teddy', 'A teddy is a solid.')], 'O1'))
s.stop(PM('Which one keeps its own shape?', ('🧱', 'A brick'), [('💧', 'Water', 'Water flows.'), ('🌬️', 'Air', 'Air spreads out.')], 'O1'),
       PM('Which one is a solid?', ('🍎', 'An apple'), [('🥛', 'Milk', 'Milk is a liquid.'), ('♨️', 'Steam', 'Steam is a gas.')], 'O1'))
s.prac(
 GD('Solid, liquid or gas?', 'State', [('🧱 brick', 'solid'), ('💧 water', 'liquid'), ('🎈 air in a balloon', 'gas'), ('🍯 honey', 'liquid'), ('🪨 stone', 'solid')], o='O1'),
 PM('You pour juice into a star-shaped cup. What shape is the juice now?', ('⭐', 'Star-shaped'), [('⚪', 'Round', 'A liquid takes the shape of its cup.'), ('🟦', 'Square', 'A liquid takes the shape of its cup.')], 'O1'),
 YN('Is air a gas?', True, 'O1', pic='🌬️', why='Yes. Air spreads out everywhere.'),
 PM('What is the gas in a fizzy drink?', ('🫧', 'The bubbles'), [('🥤', 'The cup', 'The cup is a solid.'), ('🧊', 'The ice', 'Ice is a solid.')], 'O1'),
 PM('Which is ice?', ('🧊', 'Solid water'), [('♨️', 'Water as a gas', 'That is steam.'), ('💧', 'Runny water', 'That is liquid water.')], 'O1'),
 PM('At breakfast, which one is a gas?', ('♨️', 'Steam from hot tea'), [('🍞', 'Toast', 'Toast is a solid.'), ('🥛', 'Milk', 'Milk is a liquid.')], 'O1'),
 TK('Tick the liquids.', ['Liquid', 'Not liquid'], [('orange juice', ['✓', '✗']), ('a spoon', ['✗', '✓']), ('shampoo', ['✓', '✗'])], o='O1'),
 YN('Can you hold water in your hand like a stone?', False, 'O1', pic='💧', why='No. Water is a liquid, so it flows away.'),
 MT('Match each word to what it means.', [('solid', 'keeps its shape'), ('liquid', 'flows and pours'), ('gas', 'spreads out everywhere')], o='O1'),
 PM('Which is the best thing to fill a beach ball with?', ('🌬️', 'Air'), [('🧱', 'Bricks', 'Too heavy and hard!'), ('🥛', 'Milk', 'It would be heavy and messy.')], 'O1'),
 PM('Sand can be poured, but it is a…', ('🏖️', 'solid: each grain keeps its shape'), [('💧', 'liquid', 'Each grain is a tiny solid.'), ('🎈', 'gas', 'Each grain is a tiny solid.')], 'O1', d='H'),
 YN('Does a teddy bear keep its shape?', True, 'O1', pic='🧸', why='Yes. It is a solid.'),
)
s.adv(
 PM('* Advanced. Why does a smell spread across a room?', ('🌬️', 'It is a gas, so it spreads out'), [('🧱', 'It is a solid', 'Gases spread out.'), ('💧', 'It is a liquid', 'Gases spread out.')], 'O1', d='H'),
 PM('* Advanced. Which can be a solid, a liquid and a gas?', ('💧', 'Water'), [('🪵', 'Wood', 'Wood stays solid.'), ('🧸', 'A teddy', 'A teddy stays solid.')], 'O1', d='VH'),
 OD('* Advanced. Order from the best at keeping its shape.', ['a stone', 'honey', 'air'], o='O1', d='H'),
)
s.labs('States lab',
 sort_lab('Kitchen sort', 'Sort each kitchen thing.', ['Solid', 'Liquid'],
  [('spoon', '🥄', 0, 'A spoon keeps its shape.'), ('milk', '🥛', 1, 'Milk pours.'), ('apple', '🍎', 0, 'An apple keeps its shape.'), ('oil', '🫗', 1, 'Oil pours.'), ('plate', '🍽️', 0, 'A plate keeps its shape.'), ('juice', '🧃', 1, 'Juice pours.')],
  [PM('Which one is a liquid?', ('🥛', 'Milk'), [('🥄', 'The spoon', 'A spoon is a solid.')], 'O1')]),
 home('Pour test', 'Find out which things pour.', ['a cup of water', 'a spoon', 'a few dry rice grains', 'a tray'], ['Do this over a tray or sink.'],
  ['Try to pour each thing onto the tray.', 'Does it keep its shape?', 'Does it flow?'],
  ['Thing', 'Did it flow?'], [('water', ['yes', 'no']), ('a spoon', ['yes', 'no']), ('one rice grain', ['yes', 'no'])],
  [PM('Which one flowed?', ('💧', 'Water'), [('🥄', 'The spoon', 'A spoon keeps its shape.')], 'O1')]))

# ============================================================  2.2
s = U.section('2.2', 'Separating mixtures', ['O2']); s.words(V['2.2']); core(s, 'O2')
s.stop(PM('What is a mixture?', ('🍲', 'Two or more things mixed together'), [('🪨', 'One stone', 'A mixture has two or more things.'), ('💧', 'Just water', 'A mixture has two or more things.')], 'O2'),
       PM('Which one is a mixture?', ('🥗', 'A fruit salad'), [('🍎', 'One apple', 'One thing is not a mixture.'), ('💧', 'A glass of water', 'That is one thing.')], 'O2'))
s.stop(PM('What is the best way to separate sand and pebbles?', ('🕸️', 'Use a sieve'), [('🥄', 'Stir them', 'Stirring mixes them.'), ('🧊', 'Freeze them', 'A sieve separates them.')], 'O2'),
       PM('In a sieve, what stays in?', ('🪨', 'The big bits'), [('🏖️', 'The tiny bits', 'Tiny bits fall through the holes.')], 'O2'))
s.prac(
 PM('You spill beads and paper clips. How can you separate them by hand?', ('🖐️', 'Pick out the paper clips'), [('🥤', 'Pour water on them', 'Just pick them out.'), ('🌀', 'Stir them', 'Stirring mixes them.')], 'O2'),
 YN('Can a sieve separate rice from dried beans?', True, 'O2', pic='🕸️', why='Yes. The small rice falls through, the beans stay.'),
 PM('A colander is a kind of sieve. What do we use it for?', ('🍝', 'Draining water from pasta'), [('🥛', 'Drinking milk', 'It has holes!'), ('✂️', 'Cutting paper', 'It drains pasta.')], 'O2'),
 GD('Falls through the sieve or stays in?', 'Where', [('🏖️ sand', 'falls through'), ('🪨 pebbles', 'stays in'), ('🧂 salt grains', 'falls through'), ('🐚 shells', 'stays in')], o='O2'),
 MT('Match each word to what it means.', [('mix', 'put together'), ('separate', 'take apart'), ('sieve', 'a tool with holes')], o='O2'),
 PM('Mum sieves flour for a cake. What stays in the sieve?', ('🪨', 'The lumps'), [('🌾', 'The fine flour', 'Fine flour goes through.'), ('🍰', 'The cake', 'The lumps stay in.')], 'O2'),
 YN('Is a bowl of cereal and milk a mixture?', True, 'O2', pic='🥣', why='Yes. It has two things mixed together.'),
 OD('Put sieving in order.', ['pour the mixture into the sieve', 'shake gently over a bowl', 'look at what stayed in'], o='O2'),
 TK('Tick the mixtures.', ['Mixture', 'Not a mixture'], [('sand and stones', ['✓', '✗']), ('one marble', ['✗', '✓']), ('peas and carrots', ['✓', '✗'])], o='O2'),
 PM('At the beach you want to find shells in sand. What should you use?', ('🕸️', 'A sieve'), [('🥄', 'A spoon', 'A sieve is faster.'), ('🧲', 'A magnet', 'Shells do not stick to magnets.')], 'O2'),
 PM('Which sieve would let peas through?', ('🕳️', 'One with big holes'), [('▫️', 'One with tiny holes', 'Peas are too big.'), ('🍽️', 'A plate with no holes', 'Nothing gets through.')], 'O2', d='H'),
 YN('Does stirring separate a mixture?', False, 'O2', pic='🥄', why='No. Stirring mixes things together.'),
)
s.adv(
 PM('* Advanced. Rice, peas and stones are mixed. You have one sieve that lets rice through. What is left in the sieve?', ('🫛', 'Peas and stones'), [('🍚', 'Only rice', 'Rice falls through.'), ('🤷', 'Nothing', 'The big things stay in.')], 'O2', d='VH'),
 PM('* Advanced. Why do gold panners shake their pans?', ('🥇', 'To separate heavy gold from mud'), [('🎵', 'To make music', 'They separate gold.'), ('🧊', 'To cool the water', 'They separate gold.')], 'O2', d='H'),
 GD('* Advanced. Best way to separate?', 'Way', [('🫛 peas and potatoes', 'pick out'), ('🏖️ sand and pebbles', 'sieve'), ('🍚 rice and beans', 'sieve')], o='O2', d='H'),
)
s.labs('Sieve lab',
 sort_lab('Sieve challenge', 'Shake the mixture in a sieve. Where does each thing go?', ['Falls through', 'Stays in the sieve'],
  [('sand', '🏖️', 0, 'Sand is tiny.'), ('pebbles', '🪨', 1, 'Pebbles are too big.'), ('rice', '🍚', 0, 'Rice is small.'), ('beans', '🫘', 1, 'Beans are big.'), ('salt', '🧂', 0, 'Salt is tiny.'), ('shells', '🐚', 1, 'Shells are big.')],
  [PM('What stayed in the sieve?', ('🪨', 'The pebbles'), [('🏖️', 'The sand', 'Sand fell through.')], 'O2')]),
 home('Sieve challenge', 'Separate a mixture with a sieve.', ['rice', 'dried beans', 'a sieve', 'two bowls'], ['Do not eat dried beans.'],
  ['Mix rice and beans in a bowl.', 'Pour them into the sieve.', 'Shake over the other bowl.'],
  ['Thing', 'Where did it go?'], [('rice', ['fell through', 'stayed in']), ('beans', ['fell through', 'stayed in'])],
  [PM('What fell through the sieve?', ('🍚', 'The rice'), [('🫘', 'The beans', 'Beans stayed in.')], 'O2')]))

# ============================================================  2.3
s = U.section('2.3', 'Dissolving', ['O3']); s.words(V['2.3']); core(s, 'O3')
s.stop(PM('What happens to sugar when you stir it into water?', ('🫧', 'It dissolves'), [('🪨', 'It turns into a stone', 'It breaks into tiny bits.'), ('🔥', 'It catches fire', 'It dissolves.')], 'O3'),
       PM('You stir sugar into tea. You cannot see it. Is the sugar still there?', ('👍', 'Yes, it is in tiny bits'), [('👎', 'No, it has gone forever', 'The tea tastes sweet, so it is there.')], 'O3'))
s.stop(PM('Which one will dissolve in water?', ('🧂', 'Salt'), [('🏖️', 'Sand', 'Sand sinks.'), ('🪨', 'A pebble', 'A pebble sinks.')], 'O3'),
       PM('Which one will NOT dissolve in water?', ('🏖️', 'Sand'), [('🍬', 'Sugar', 'Sugar dissolves.'), ('🧂', 'Salt', 'Salt dissolves.')], 'O3'))
s.prac(
 GD('Dissolves or not?', 'Dissolves?', [('🍬 sugar', 'yes'), ('🏖️ sand', 'no'), ('🧂 salt', 'yes'), ('🪨 pebble', 'no'), ('☕ instant coffee', 'yes')], o='O3'),
 PM('How can you make sugar dissolve faster?', ('♨️', 'Use warm water and stir'), [('🧊', 'Use ice-cold water', 'Warm water is faster.'), ('🙈', 'Do not touch it', 'Stirring helps.')], 'O3'),
 YN('Does sand dissolve in water?', False, 'O3', pic='🏖️', why='No. It sinks to the bottom.'),
 PM('Why does the sea taste salty?', ('🧂', 'Salt is dissolved in it'), [('🐟', 'The fish are salty', 'Salt is dissolved in the water.'), ('🌧️', 'Rain is salty', 'Salt is dissolved in the sea.')], 'O3'),
 PM('You make lemonade with sugar. Which tool helps it dissolve?', ('🥄', 'A spoon to stir'), [('✂️', 'Scissors', 'Stir with a spoon.'), ('🔨', 'A hammer', 'Stir with a spoon.')], 'O3'),
 MT('Match each word to what it means.', [('dissolve', 'mix into water and seem to disappear'), ('stir', 'move a spoon round'), ('sand', 'tiny bits of rock')], o='O3'),
 OD('Order: making sweet water.', ['pour warm water in a cup', 'add a spoon of sugar', 'stir until it disappears'], o='O3'),
 TK('Tick what is true.', ['True', 'False'], [('sugar dissolves in water', ['✓', '✗']), ('sand dissolves in water', ['✗', '✓']), ('stirring helps', ['✓', '✗'])], o='O3'),
 YN('Can you see sugar after it dissolves?', False, 'O3', pic='👀', why='No. The bits are too tiny to see.'),
 PM('Which cup will dissolve sugar the fastest?', ('♨️', 'Warm water, stirred'), [('🧊', 'Cold water, not stirred', 'Slowest!'), ('🥛', 'Cold water, stirred', 'Warm is faster.')], 'O3', d='H'),
 PM('A bath bomb fizzes and disappears in the bath. What happened?', ('🫧', 'It dissolved'), [('🧊', 'It froze', 'It dissolved.'), ('🔥', 'It burned', 'It dissolved.')], 'O3'),
 YN('Is dissolved salt still in the water?', True, 'O3', pic='🧂', why='Yes. The water tastes salty.'),
)
s.adv(
 PM('* Advanced. How could you get dissolved salt back from salty water?', ('☀️', 'Leave it in the sun so the water dries up'), [('🕸️', 'Use a sieve', 'The bits are too tiny.'), ('🧊', 'Freeze it', 'Let the water dry up.')], 'O3', d='VH'),
 PM('* Advanced. You add more and more sugar to a cup. What happens in the end?', ('🍬', 'Some sugar stops dissolving'), [('🥤', 'The cup gets bigger', 'Some sugar stays at the bottom.'), ('🌈', 'The water changes colour', 'Some sugar stops dissolving.')], 'O3', d='H'),
 OD('* Advanced. Order from fastest to slowest dissolving.', ['warm water, stirred', 'warm water, not stirred', 'cold water, not stirred'], o='O3', d='H'),
)
s.labs('Dissolving lab',
 test_lab('Stir test', 'Stir sugar into water at different temperatures. Read how many seconds it takes to dissolve.', 'Water', 'Time to dissolve', 'seconds', 100, 10,
  'Tap the number the bar reaches.', [('ice-cold water', '🧊', 90), ('room water', '💧', 50), ('warm water', '♨️', 20)],
  [PM('Which water dissolved sugar the fastest?', ('♨️', 'Warm water'), [('🧊', 'Ice-cold water', 'It took longest.')], 'O3')]),
 home('Dissolving test', 'Which things dissolve?', ['three cups of water', 'sugar', 'salt', 'sand', 'a spoon'], ['Do not drink your experiment.'],
  ['Put a spoon of each thing in its own cup.', 'Stir each cup.', 'Look carefully.'],
  ['Thing', 'Did it dissolve?'], [('sugar', ['yes', 'no']), ('salt', ['yes', 'no']), ('sand', ['yes', 'no'])],
  [PM('Which one did not dissolve?', ('🏖️', 'Sand'), [('🍬', 'Sugar', 'Sugar dissolved.')], 'O3')]))

# ============================================================  2.4
s = U.section('2.4', 'Filtering', ['O4']); s.words(V['2.4']); core(s, 'O4')
s.stop(PM('What does a filter take out of muddy water?', ('🟤', 'The mud'), [('💧', 'The water', 'Water goes through.'), ('🧂', 'Dissolved salt', 'Dissolved things go through.')], 'O4'),
       PM('Why can\'t a sieve clean muddy water?', ('🕳️', 'Its holes are too big'), [('🔥', 'It is too hot', 'The holes are too big.'), ('🧊', 'It is too cold', 'The holes are too big.')], 'O4'))
s.stop(PM('Which one is a filter?', ('🫖', 'A tea bag'), [('🥄', 'A spoon', 'A spoon has no tiny holes.'), ('🍽️', 'A plate', 'A plate has no holes.')], 'O4'),
       PM('Which can you use as a filter at home?', ('🧻', 'A paper towel'), [('🪨', 'A stone', 'Use paper with tiny holes.'), ('🧱', 'A brick', 'Use paper with tiny holes.')], 'O4'))
s.prac(
 YN('Is filtered muddy water safe to drink?', False, 'O4', pic='🚫', why='No. Germs can still get through.'),
 OD('Order: filtering muddy water.', ['put paper in a funnel', 'pour in the muddy water', 'clean water drips out'], o='O4'),
 PM('After filtering, where is the mud?', ('🧻', 'On the paper'), [('🫙', 'In the jar', 'The paper caught it.'), ('🌬️', 'In the air', 'The paper caught it.')], 'O4'),
 PM('Grandpa makes coffee. What keeps the coffee bits out of his cup?', ('☕', 'A coffee filter'), [('🥄', 'A spoon', 'A filter does it.'), ('🧊', 'An ice cube', 'A filter does it.')], 'O4'),
 MT('Match each word to what it means.', [('filter', 'has tiny holes to clean liquids'), ('muddy', 'full of mud'), ('funnel', 'helps you pour')], o='O4'),
 TK('Tick the filters.', ['Filter', 'Not a filter'], [('a tea bag', ['✓', '✗']), ('a cup', ['✗', '✓']), ('a fish tank filter', ['✓', '✗'])], o='O4'),
 PM('Which has the smallest holes?', ('🧻', 'A paper filter'), [('🕸️', 'A garden sieve', 'Paper has tinier holes.'), ('🍝', 'A colander', 'Paper has tinier holes.')], 'O4'),
 YN('Does a tea bag keep the tea leaves inside?', True, 'O4', pic='🫖', why='Yes. It is a filter.'),
 GD('Sieve or filter?', 'Use', [('🏖️ sand from pebbles', 'sieve'), ('🟤 mud from water', 'filter'), ('🍝 water from pasta', 'sieve')], o='O4'),
 PM('Why does a fish tank have a filter?', ('🐟', 'To keep the water clean'), [('🔊', 'To make music', 'It cleans the water.'), ('🌈', 'To make colours', 'It cleans the water.')], 'O4'),
 PM('Can a filter take salt out of salty water?', ('🚫', 'No – salt is dissolved'), [('✅', 'Yes – easily', 'Dissolved bits are too tiny.')], 'O4', d='H'),
 YN('Do some whales filter their food from seawater?', True, 'O4', pic='🐋', why='Yes!'),
)
s.adv(
 PM('* Advanced. Which mixture can a filter separate?', ('🏖️', 'Sand and water'), [('🍬', 'Sugar water', 'The sugar is dissolved.'), ('🧂', 'Salty water', 'The salt is dissolved.')], 'O4', d='VH'),
 PM('* Advanced. Your filtered water is still a bit cloudy. What could you do?', ('🔁', 'Filter it again'), [('🥤', 'Drink it', 'Never drink it!'), ('🌀', 'Stir it', 'Filter it again.')], 'O4', d='H'),
 OD('* Advanced. Order by hole size, smallest first.', ['paper filter', 'tea strainer', 'garden sieve'], o='O4', d='H'),
)
s.labs('Filter lab',
 test_lab('Which filter is best?', 'Pour muddy water through different filters. Read how clean the water is (0 to 10).', 'Filter', 'Cleanness', 'points', 10, 1,
  'Tap the number the bar reaches.', [('a garden sieve', '🕸️', 2), ('a cloth', '🧣', 6), ('a paper towel', '🧻', 9)],
  [PM('Which filter made the cleanest water?', ('🧻', 'The paper towel'), [('🕸️', 'The sieve', 'Its holes were too big.')], 'O4')]),
 home('Muddy water filter', 'Make a filter at home.', ['a cup of muddy water', 'a paper towel', 'a funnel or cut bottle', 'a jar', 'an adult'], ['Never drink the water.', 'Wash your hands afterwards.'],
  ['Put the paper towel in the funnel.', 'Stand the funnel in the jar.', 'Pour in the muddy water slowly.'],
  ['Question', 'My answer'], [('was the water cleaner?', ['yes', 'no']), ('was mud on the paper?', ['yes', 'no'])],
  [PM('Where did the mud go?', ('🧻', 'Onto the paper'), [('🫙', 'Into the jar', 'The paper caught it.')], 'O4')]))

# ============================================================  2.5
s = U.section('2.5', 'Separating materials from rocks', ['O5']); s.words(V['2.5']); core(s, 'O5')
s.stop(PM('What can pull iron bits out of sand?', ('🧲', 'A magnet'), [('🧻', 'A paper towel', 'Use a magnet.'), ('🥄', 'A spoon', 'Use a magnet.')], 'O5'),
       PM('Which one sticks to a magnet?', ('⚙️', 'Iron'), [('🏖️', 'Sand', 'Sand is not magnetic.'), ('🪵', 'Wood', 'Wood is not magnetic.')], 'O5'))
s.stop(PM('How do we get salt from seawater?', ('☀️', 'Let the Sun dry up the water'), [('🧲', 'Use a magnet', 'Salt is not magnetic.'), ('🕸️', 'Use a sieve', 'The salt is dissolved.')], 'O5'),
       PM('Seawater dries up in the sun. What is left?', ('🧂', 'Salt'), [('🐟', 'Fish', 'Salt is left behind.'), ('🧊', 'Ice', 'Salt is left behind.')], 'O5'))
s.prac(
 PM('Where do metals like iron come from?', ('🪨', 'Rocks in the ground'), [('🌳', 'Trees', 'They come from rocks.'), ('☁️', 'Clouds', 'They come from rocks.')], 'O5'),
 YN('Can a magnet separate iron from sand?', True, 'O5', pic='🧲', why='Yes. Iron sticks; sand stays.'),
 GD('Best way to separate?', 'Way', [('⚙️ iron bits from sand', 'magnet'), ('🧂 salt from seawater', 'let it dry'), ('🪨 pebbles from sand', 'sieve'), ('🟤 mud from water', 'filter')], o='O5'),
 PM('What can we make from metal?', ('🥄', 'A spoon'), [('📄', 'Paper', 'Paper comes from trees.'), ('🧶', 'Wool', 'Wool comes from sheep.')], 'O5'),
 MT('Match each word to what it means.', [('iron', 'a metal that sticks to magnets'), ('magnet', 'pulls iron'), ('crystal', 'a small sparkly shape')], o='O5'),
 YN('Do sparkly diamonds come from rocks?', True, 'O5', pic='💎', why='Yes. They are dug out of rocks.'),
 OD('Order: making salt crystals.', ['dissolve salt in warm water', 'pour a little on a plate', 'leave it in the sun', 'look at the crystals'], o='O5'),
 TK('Tick what a magnet picks up.', ['Picks up', 'Does not'], [('iron filings', ['✓', '✗']), ('sand', ['✗', '✓']), ('a steel pin', ['✓', '✗'])], o='O5'),
 PM('Your salty water dried up on a plate. What do you see?', ('💎', 'Tiny salt crystals'), [('🌈', 'A rainbow', 'You see crystals.'), ('🐚', 'Shells', 'You see crystals.')], 'O5'),
 PM('Pins fell into the sand pit! What is the fastest way to find them?', ('🧲', 'Use a magnet'), [('🖐️', 'Feel with your hands', 'Ouch! Use a magnet.'), ('💧', 'Pour water on them', 'Use a magnet.')], 'O5'),
 PM('Which way of separating did NOT use a sieve or a filter?', ('🧲', 'Pulling iron out with a magnet'), [('🕸️', 'Shaking out pebbles', 'That used a sieve.'), ('🧻', 'Cleaning muddy water', 'That used a filter.')], 'O5', d='H'),
 YN('Is all the salt we eat dug from the ground?', False, 'O5', pic='🌊', why='No. Lots of salt comes from seawater.'),
)
s.adv(
 PM('* Advanced. A mixture has iron bits, sand and salt. What do you do first to get the iron out?', ('🧲', 'Use a magnet'), [('☀️', 'Let it dry', 'That is for the salt.'), ('🧻', 'Filter it', 'Use a magnet for iron.')], 'O5', d='VH'),
 PM('* Advanced. Why are salt pans by the sea flat and wide?', ('☀️', 'So the Sun dries the water faster'), [('🏊', 'So people can swim', 'Wide pans dry faster.'), ('🐟', 'To catch fish', 'Wide pans dry faster.')], 'O5', d='H'),
 OD('* Advanced. Order the steps to get salt from sandy seawater.', ['filter out the sand', 'pour the water into a dish', 'leave it to dry'], o='O5', d='H'),
)
s.labs('Rock lab',
 sort_lab('Magnet or not?', 'Move a magnet over each thing. Does it stick?', ['Sticks to the magnet', 'Does not stick'],
  [('iron filings', '✨', 0, 'Iron is magnetic.'), ('sand', '🏖️', 1, 'Sand is not magnetic.'), ('steel pin', '📌', 0, 'Steel is magnetic.'), ('salt', '🧂', 1, 'Salt is not magnetic.'), ('nail', '🔩', 0, 'A steel nail is magnetic.'), ('pebble', '🪨', 1, 'A pebble is not magnetic.')],
  [PM('What could the magnet pull out of the sand?', ('✨', 'Iron filings'), [('🧂', 'Salt', 'Salt does not stick.')], 'O5')]),
 home('Salt crystals', 'Get salt back from salty water.', ['salt', 'warm water', 'a dark plate', 'a sunny windowsill', 'an adult'], ['Ask an adult to help with warm water.'],
  ['Dissolve salt in warm water.', 'Pour a little onto a plate.', 'Leave it on a sunny windowsill for a few days.'],
  ['Question', 'My answer'], [('did the water disappear?', ['yes', 'no']), ('was salt left on the plate?', ['yes', 'no'])],
  [PM('What was left on the plate?', ('🧂', 'Salt crystals'), [('💧', 'Water', 'The water dried up.')], 'O5')]))

U.mindmap(('States', 'solid, liquid, gas', 'O1', '2.1'), ('Mixtures', 'pick out or sieve', 'O2', '2.2'), ('Dissolving', 'sugar and salt dissolve', 'O3', '2.3'),
          ('Filtering', 'a filter catches mud', 'O4', '2.4'), ('From rocks', 'magnets and drying', 'O5', '2.5'))
