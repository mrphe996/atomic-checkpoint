# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 5 · Unit 3 States and properties of matter. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit5 import *

OBJ = {
 'O1': {'sec': '3.1', 'code': 'Chemistry', 'codeNote': '', 't': 'Describe gases using the particle model and name oxygen and carbon dioxide.'},
 'O2': {'sec': '3.2', 'code': 'Chemistry', 'codeNote': '', 't': 'Describe water as a solid, liquid and gas, and know its melting point (0 °C) and boiling point (100 °C).'},
 'O3': {'sec': '3.3', 'code': 'Chemistry', 'codeNote': '', 't': 'Describe evaporation and condensation and explain the water cycle.'},
 'O4': {'sec': '3.3', 'code': 'Working scientifically', 'codeNote': '', 't': 'Investigate what makes evaporation faster and use measurements to draw a conclusion.'},
 'O5': {'sec': '3.4', 'code': 'Chemistry', 'codeNote': '', 't': 'Describe dissolving, solutions, soluble and insoluble substances, and how to get a solute back.'},
}
U = Unit(3, 'States and properties of matter', 'Chemistry: materials', 'Gases, the three states of water, evaporation, condensation and dissolving.', OBJ)

# =====================================================================================  3.1
s = U.section('3.1', 'Gases', ['O1']); s.words(V['3.1']); core(s, 'O1', 'O1')
s.stop(MC('Why does a gas spread out to fill its container?', 'Its particles are far apart and move fast in all directions', [('Its particles are packed tightly', 'That is a solid.'), ('It is heavier than a liquid', 'It is about moving particles.'), ('It is pushed by light', 'Particles move by themselves.')], o='O1'),
       MC('How did the pizza smell reach your nose in the next room?', 'The gas particles spread out through the air', [('It travelled through the walls only', 'It spread through the air.'), ('Someone carried it', 'Gases spread by themselves.')], o='O1'))
s.stop(MC('Which gas do we breathe out?', 'Carbon dioxide', [('Oxygen', 'We breathe oxygen in.'), ('Helium', 'Helium fills party balloons.')], o='O1'),
       MC('Which gas do all living things need to breathe in?', 'Oxygen', [('Carbon dioxide', 'We breathe that out.'), ('Helium', 'Helium is not needed for breathing.')], o='O1'))
s.prac(
 GD('Is each one a solid, a liquid or a gas?', 'State', [('the air in a balloon', 'gas'), ('juice', 'liquid'), ('a pebble', 'solid'), ('steam', 'gas'), ('milk', 'liquid')], o='O1'),
 MT('Match each state to how its particles behave.', [('solid', 'packed tightly, only wobble'), ('liquid', 'close together, slide around'), ('gas', 'far apart, zoom about')], o='O1'),
 MC('Why can\'t we see air?', 'It is a gas, and its particles are far apart and invisible', [('There is no air in a room', 'Air is all around us.'), ('Air is always dark', 'It is invisible.')], o='O1'),
 MS('Select the things that contain air.', ['a football', 'a sponge', 'bubbles', 'soil'], ['a solid metal bolt'], o='O1'),
 MC('What makes the bubbles in fizzy drinks?', 'Carbon dioxide', [('Oxygen', 'The fizz is carbon dioxide.'), ('Helium', 'Helium is in balloons.')], o='O1'),
 MC('Why do helium balloons float up?', 'Helium is lighter than air', [('Helium is hot', 'It is lighter than air.'), ('The balloon is magnetic', 'It is about helium being light.')], o='O1'),
 MC('Does air have mass?', 'Yes – a pumped-up football weighs more than a flat one', [('No – air weighs nothing', 'Air has a small mass.'), ('Only cold air', 'All air has mass.')], o='O1'),
 CZ('Complete the sentences.', 'We breathe in {0} and breathe out {1}. Air is a mixture of {2}.', [['oxygen'], ['carbon dioxide'], ['gases']], o='O1'),
 MC('In the soil experiment, what did the bubbles show?', 'There was air hiding in the soil', [('The soil was boiling', 'The water was not hot.'), ('The water was fizzy', 'The air came from the soil.')], o='O1'),
 MC('A gas is squashed into a smaller bottle. What happens?', 'Its particles get closer together', [('It turns into a solid', 'It is still a gas.'), ('It disappears', 'Gases can be squashed.')], o='O1'),
 TK('Tick what is true about gases.', ['True', 'False'], [('they spread out to fill a container', ['✓', '✗']), ('they have a fixed shape', ['✗', '✓']), ('they can be squashed', ['✓', '✗']), ('they have mass', ['✓', '✗'])], o='O1'),
 MC('Why does a bike tyre feel hard when it is pumped up?', 'Lots of air is squashed inside it', [('The rubber gets harder', 'It is the air inside.'), ('Air is a solid', 'Air is a gas.')], o='O1'),
 OD('Order the particles from closest together to furthest apart.', ['solid', 'liquid', 'gas'], o='O1'),
 MC('Which is NOT a gas?', 'Water', [('Oxygen', 'Oxygen is a gas.'), ('Steam', 'Steam is water vapour, a gas.')], o='O1'),
)
s.adv(
 EX('Explain why you can smell perfume from across the room.', [('perfume particles become a gas / evaporate', ['gas', 'evaporat']), ('gas particles move fast and spread out', ['spread', 'move']), ('they reach your nose', ['nose'])], 'The perfume becomes a gas, and its particles move fast and spread out through the air until they reach your nose.', o='O1', d='H'),
 TB('A football was weighed. Complete the table.', ['Football', 'Mass (g)'], [['flat', '410'], ['pumped up', '418'], ['mass of the air', B(8)]], o='O1', skill='Data', reason='418 − 410 = 8 g.'),
 MC('Why is it easy to squash a gas but hard to squash a solid?', 'Gas particles have big spaces between them', [('Gas particles are bigger', 'The spaces matter.'), ('Solids have no particles', 'Everything has particles.')], o='O1', d='VH'),
 MC('Why do plants need carbon dioxide?', 'To make their food', [('To make them float', 'Plants use it to make food.'), ('To make them smell nice', 'It is for making food.')], o='O1', d='H'),
)
s.labs('States lab',
 sort_lab('Solid, liquid or gas?', 'Sort each card into its state of matter.', ['Solid', 'Liquid', 'Gas'],
  [('ice cube', '🧊', 0, 'It keeps its shape.'), ('orange juice', '🧃', 1, 'It flows and takes the shape of the cup.'), ('air in a balloon', '🎈', 2, 'Air spreads out to fill the balloon.'),
   ('wooden spoon', '🥄', 0, 'It keeps its shape.'), ('steam from a kettle', '♨️', 2, 'Steam is water vapour, a gas.'), ('honey', '🍯', 1, 'Honey flows slowly, but it is a liquid.'), ('the bubbles in a fizzy drink', '🫧', 2, 'They are carbon dioxide gas.')],
  [MC('Which state spreads out to fill any container?', 'Gas', [('Solid', 'Solids keep their shape.'), ('Liquid', 'Liquids fill the bottom of a container.')], o='O1'),
   MC('Honey flows very slowly. What state is it?', 'Liquid', [('Solid', 'It flows, so it is a liquid.'), ('Gas', 'It does not spread out.')], o='O1')]),
 home('Find the hidden air', 'Show that soil has air in it.', ['a clear jar', 'a cup of dry soil', 'water'],
  ['Wash your hands after touching soil.', 'Do not drink the water.'],
  ['Put the dry soil in the jar.', 'Slowly pour water over the soil.', 'Count the bubbles you see rising in 30 seconds.', 'Try again with sand.'],
  ['Material', 'Bubbles in 30 seconds'], [['Soil', {'min': 0, 'max': 500}], ['Sand', {'min': 0, 'max': 500}]], 'Count roughly – any number from 0 upwards.',
  [MC('Where did the bubbles come from?', 'Air that was in the spaces between the bits of soil', [('From the water', 'The water pushed the air out.'), ('From the jar', 'The air was in the soil.')], o='O1')]))

# =====================================================================================  3.2
s = U.section('3.2', 'Properties of water', ['O2']); s.words(V['3.2']); core(s, 'O2', 'O2')
s.stop(MC('At what temperature does ice melt?', '0 °C', [('100 °C', 'That is when water boils.'), ('37 °C', 'That is body temperature.'), ('20 °C', 'Ice melts at 0 °C.')], o='O2'),
       MC('What is it called when liquid water turns into ice?', 'Freezing', [('Melting', 'Melting is ice turning to water.'), ('Boiling', 'Boiling makes a gas.')], o='O2'))
s.stop(MC('At what temperature does water boil?', '100 °C', [('0 °C', 'That is when ice melts.'), ('50 °C', 'Water is hot at 50 °C but not boiling.')], o='O2'),
       MC('What are the bubbles in boiling water?', 'Water vapour (a gas)', [('Air from the kettle', 'They are water vapour.'), ('Soap', 'There is no soap.')], o='O2'))
s.prac(
 MT('Match each state of water to its name.', [('solid', 'ice'), ('liquid', 'water'), ('gas', 'water vapour')], o='O2'),
 GD('Is each change melting, freezing or boiling?', 'Change', [('an ice lolly in the sun', 'melting'), ('juice in the freezer', 'freezing'), ('a kettle at 100 °C', 'boiling'), ('snow on a warm day', 'melting')], o='O2'),
 MC('Is melting a reversible change?', 'Yes – the water can be frozen again', [('No – it can never be undone', 'Freeze it and it becomes ice again.'), ('Only for chocolate', 'Water too.')], o='O2'),
 MC('Why must you ask an adult when using a kettle?', 'Boiling water and steam can burn you', [('Kettles are heavy', 'The danger is burns.'), ('Water is wet', 'It is about burns.')], o='O2'),
 MC('What is special about ice compared with most solids?', 'It floats on its own liquid', [('It is very hot', 'Ice is cold.'), ('It is a gas', 'Ice is a solid.')], o='O2'),
 MC('Why can fish survive in a frozen lake?', 'The ice floats on top, and there is liquid water underneath', [('Fish freeze too and wake up', 'The water underneath stays liquid.'), ('Lakes never freeze', 'They can freeze on top.')], o='O2'),
 MS('Select the properties of liquid water.', ['it flows', 'it takes the shape of its container', 'many things dissolve in it'], ['it keeps a fixed shape', 'it is invisible gas'], o='O2'),
 CZ('Complete the sentences.', 'Ice melts at {0} °C. Water boils at {1} °C. Water as a gas is called water {2}.', [['0', 'zero'], ['100', 'one hundred'], ['vapour', 'vapor']], o='O2'),
 OD('Put these temperatures in order from coldest to hottest.', ['freezer (−18 °C)', 'ice melting (0 °C)', 'warm bath (40 °C)', 'boiling water (100 °C)'], o='O2'),
 MC('What do we use to measure temperature?', 'A thermometer', [('A ruler', 'Rulers measure length.'), ('A forcemeter', 'Forcemeters measure force.')], o='O2'),
 MC('In the ice cube race, what did you change?', 'The place where the ice cube was put', [('The size of the ice cube', 'Use the same size.'), ('The type of water', 'Use the same water.')], o='O2'),
 TB('Ice cube race results. How many minutes longer did the shade take than the sunny window?', ['Place', 'Time to melt (min)'], [['sunny window', '10'], ['shady room', '25'], ['difference', B(15)]], o='O2', skill='Data'),
 MC('Where will an ice cube melt fastest?', 'In a warm, sunny place', [('In the fridge', 'Cold slows melting.'), ('In the freezer', 'It will not melt there.')], o='O2'),
 MC('Water is at 100 °C and still being heated. What happens to its temperature?', 'It stays at 100 °C while it boils', [('It keeps rising', 'It stays at 100 °C while boiling.'), ('It drops to 0 °C', 'It is boiling.')], o='O2', d='H'),
)
s.adv(
 EX('Explain why melting and freezing are reversible changes.', [('ice melts into water', ['melt']), ('the water can freeze back into ice', ['freez']), ('no new substance is made / it can be undone', ['undone', 'back', 'same', 'no new'])], 'Ice melts into water, and the water can freeze back into ice. It is still water each time, so the change can be undone.', o='O2', d='H'),
 GR('Plot the temperature of ice being warmed.', {'label': 'Time (minutes)', 'min': 0, 'max': 10, 'step': 2}, {'label': 'Temperature (°C)', 'min': -10, 'max': 30, 'step': 10}, [[0, -10], [2, 0], [4, 0], [6, 0], [8, 10], [10, 20]], o='O2', d='H', table_rows=[[0, -10], [2, 0], [4, 0], [6, 0], [8, 10], [10, 20]]),
 MC('In the graph, why does the temperature stay at 0 °C for a while?', 'The ice is melting', [('The thermometer is broken', 'This always happens while ice melts.'), ('The water is boiling', 'Water boils at 100 °C.')], o='O2', d='VH'),
 MC('Salt is put on icy roads. What does it do?', 'It helps the ice melt at a lower temperature', [('It makes the ice thicker', 'It helps melting.'), ('It makes the road hotter', 'It lowers the melting temperature.')], o='O2', d='H'),
)
s.labs('Ice cube race lab',
 test_lab('Where does ice melt fastest?', 'Ice cubes of the same size were put in different places. Read the timer scale to see how long each took to melt.', 'The place', 'Time to melt', 'min', 140, 10, '⏱️',
  [('Sunny window', '☀️', 10), ('Shady room', '🏠', 25), ('Fridge', '🧊', 120)],
  [MC('Where did the ice melt fastest?', 'The sunny window', [('The fridge', 'It took 120 minutes there.'), ('The shady room', 'It took 25 minutes there.')], o='O2'),
   MC('Why did the ice take so long in the fridge?', 'The fridge is cold, so less heat reaches the ice', [('The fridge is dark', 'It is about temperature.'), ('The ice was bigger', 'The cubes were the same.')], o='O2')]),
 home('Ice cube race', 'Find the fastest place for an ice cube to melt.', ['3 ice cubes the same size', '3 small plates', 'a clock or timer'],
  ['Wipe up any water so nobody slips.', 'Do not put ice near electrical things.'],
  ['Put one ice cube on a plate in a sunny place, one in a shady place and one in the fridge.', 'Start the timer.', 'Check every 5 minutes.', 'Write down when each ice cube has completely melted.'],
  ['Place', 'Time to melt (minutes)'], [['Sunny place', {'min': 1, 'max': 600}], ['Shady place', {'min': 1, 'max': 600}], ['Fridge', {'min': 1, 'max': 1440}]], 'Times are usually between 10 and 300 minutes.',
  [MC('What made the ice melt fastest?', 'More warmth', [('Less light', 'Warmth melts ice.'), ('A bigger plate', 'The plates were the same.')], o='O2')]))

# =====================================================================================  3.3
s = U.section('3.3', 'Evaporation and condensation', ['O3', 'O4']); s.words(V['3.3']); core(s, 'O3', 'O3')
s.stop(MC('What is evaporation?', 'A liquid turning into a gas', [('A gas turning into a liquid', 'That is condensation.'), ('A solid turning into a liquid', 'That is melting.'), ('Water falling as rain', 'That is part of the water cycle.')], o='O3'),
       MC('Where did the puddle go on the sunny day?', 'It evaporated into the air as water vapour', [('It sank into the sun', 'It turned into a gas.'), ('Someone mopped it up', 'The sun evaporated it.')], o='O3'))
s.stop(MC('How does a cloud form?', 'Water vapour cools high in the sky and condenses into tiny drops', [('Smoke rises from fires', 'Clouds are water drops.'), ('The Moon makes them', 'Clouds form from water vapour.'), ('Water freezes on the ground', 'Clouds form in the sky.')], o='O3'),
       MC('What is condensation?', 'A gas turning back into a liquid', [('A liquid turning into a gas', 'That is evaporation.'), ('Ice melting', 'That is melting.')], o='O3'))
s.prac(
 GD('Is each one evaporation or condensation?', 'Change', [('wet washing drying', 'evaporation'), ('a steamy bathroom mirror', 'condensation'), ('drops on a cold glass', 'condensation'), ('a puddle disappearing', 'evaporation')], o='O3'),
 MS('Select the things that make evaporation faster.', ['warmth', 'wind', 'spreading the water out'], ['cold', 'covering the water'], o='O4'),
 MC('Why does washing dry faster on a windy day?', 'The wind carries the water vapour away', [('The wind is wet', 'It carries vapour away.'), ('Wind makes the clothes heavier', 'It helps drying.')], o='O4'),
 MC('Why do drops appear on a cold drink?', 'Water vapour in the air condenses on the cold glass', [('The drink leaks through the glass', 'Glass does not leak.'), ('The ice melts outside', 'The water comes from the air.')], o='O3'),
 MC('Why can you see your breath on a cold day?', 'The water vapour in your breath condenses into tiny drops', [('Your breath is smoke', 'It is water drops.'), ('Cold air is white', 'It is condensed water.')], o='O3'),
 OD('Put the water cycle in order.', ['the sun warms the sea', 'water evaporates', 'water vapour cools and condenses into clouds', 'rain falls', 'water flows back to the sea'], o='O3'),
 CZ('Complete the sentences.', 'When a liquid turns into a gas it is called {0}. When a gas turns into a liquid it is called {1}. Together they make the water {2}.', [['evaporation'], ['condensation'], ['cycle']], o='O3'),
 MC('Which is the opposite of evaporation?', 'Condensation', [('Melting', 'The opposite of melting is freezing.'), ('Dissolving', 'That is mixing in a liquid.')], o='O3'),
 MC('In the cloth test, what did you measure?', 'The mass of each cloth', [('The colour of the cloth', 'Measure the mass.'), ('The length of the cloth', 'Measure the mass.')], o='O4'),
 MC('Why does a cloth get lighter as it dries?', 'The water evaporates from it', [('The cloth shrinks', 'Water leaves the cloth.'), ('Gravity gets weaker', 'Water evaporates.')], o='O4'),
 TB('Cloths started with 50 g of water. How much water did each lose in 2 hours?', ['Place', 'Water left (g)', 'Water lost (g)'], [['in the sun', '10', B(40)], ['in the shade', '25', B(25)], ['indoors', '35', B(15)]], o='O4', skill='Data', reason='50 − water left.'),
 MC('What do the cloth results show?', 'Warmth makes water evaporate faster', [('Shade makes water evaporate faster', 'The sunny cloth lost the most.'), ('Nothing changed', 'The results were different.')], o='O4'),
 MC('Why do puddles dry more slowly in winter?', 'It is colder, so evaporation is slower', [('It rains more in summer', 'It is about temperature.'), ('Winter puddles are made of ice', 'They can be liquid too.')], o='O3'),
 MC('Rain falls from clouds. Where did the water in the clouds come from?', 'Water that evaporated from seas, rivers and land', [('From space', 'It comes from Earth.'), ('From the Sun', 'The Sun warms the water.')], o='O3'),
)
s.adv(
 EX('Explain how water from the sea can end up as rain on a mountain.', [('the sun warms the sea and water evaporates', ['evaporat']), ('water vapour rises, cools and condenses into clouds', ['condens', 'cloud']), ('the drops fall as rain', ['rain', 'fall'])], 'The sun warms the sea so water evaporates. The water vapour rises, cools and condenses into clouds, which are blown over the mountain. The drops get heavy and fall as rain.', o='O3', d='H'),
 GR('Plot the mass of a wet cloth in the sun.', {'label': 'Time (minutes)', 'min': 0, 'max': 120, 'step': 30}, {'label': 'Mass of cloth (g)', 'min': 0, 'max': 100, 'step': 20}, [[0, 90], [30, 75], [60, 62], [90, 55], [120, 50]], o='O4', d='H', table_rows=[[0, 90], [30, 75], [60, 62], [90, 55], [120, 50]]),
 MC('Using those results, the cloth stopped losing mass at 50 g. What does this tell you?', 'The cloth was dry: all the water had evaporated', [('The cloth was still very wet', 'Its mass stopped changing.'), ('The sun went out', 'The cloth was dry.')], o='O4', d='VH'),
 MC('Why do people living by the sea collect salt in shallow pans?', 'Shallow water evaporates quickly and leaves the salt', [('Deep water is too heavy', 'Shallow means fast evaporation.'), ('Salt likes shallow pans', 'It is about evaporation.')], o='O3', d='H'),
)
s.labs('Drying lab',
 test_lab('Where does a wet cloth dry fastest?', 'Three cloths each started with 50 g of water. After 2 hours, read the scale to see how much water each lost.', 'The place', 'Water lost in 2 hours', 'g', 50, 5, '⚖️',
  [('In the sun', '☀️', 40), ('In the shade', '🌳', 25), ('Indoors', '🏠', 15)],
  [MC('Where did the cloth lose the most water?', 'In the sun', [('Indoors', 'It lost only 15 g.'), ('In the shade', 'It lost 25 g.')], o='O4'),
   MC('What process made the cloths lose water?', 'Evaporation', [('Condensation', 'Condensation adds water.'), ('Freezing', 'It was not cold.')], o='O3')]),
 home('Steamy spoon', 'See condensation happen.', ['a metal spoon', 'a cup of warm tap water (not boiling)', 'the fridge'],
  ['Use warm tap water, not boiling water.', 'Ask an adult to help.'],
  ['Put the spoon in the fridge for 10 minutes.', 'Hold the cold spoon above the warm water for 30 seconds.', 'Count the drops of water that form on the spoon.', 'Repeat with a spoon at room temperature.'],
  ['Spoon', 'Drops formed'], [['Cold spoon', {'min': 0, 'max': 200}], ['Room-temperature spoon', {'min': 0, 'max': 200}]], 'Count roughly.',
  [MC('Why did more drops form on the cold spoon?', 'Water vapour condenses on cold surfaces', [('The cold spoon was wet already', 'It was dry from the fridge.'), ('Warm spoons attract water', 'Cold surfaces cause condensation.')], o='O3')]))

# =====================================================================================  3.4
s = U.section('3.4', 'Solutions', ['O5']); s.words(V['3.4']); core(s, 'O5', 'O5')
s.stop(MC('What is a solution?', 'A liquid with something dissolved in it', [('A mixture of sand and water', 'Sand does not dissolve.'), ('A solid block', 'A solution is a liquid.'), ('The answer to a maths problem', 'In science, it is a liquid with something dissolved in it.')], o='O5'),
       MC('Sugar is stirred into tea and disappears. Where is it?', 'Still in the tea – its particles have spread out', [('It has vanished for ever', 'Taste it: it is sweet!'), ('It turned into water', 'It is still sugar.')], o='O5'))
s.stop(MC('How can you get salt back from salty water?', 'Leave it somewhere warm so the water evaporates', [('Stir it for a long time', 'Stirring helps dissolving.'), ('Put it in the freezer', 'The salt stays dissolved.'), ('Pour it through paper', 'Dissolved salt goes through.')], o='O5'),
       MC('Is dissolving a reversible change?', 'Yes – the solid can be got back by evaporation', [('No – never', 'Evaporation gets it back.'), ('Only with sand', 'Sand does not dissolve.')], o='O5'))
s.prac(
 GD('Is each substance soluble or insoluble in water?', 'In water', [('salt', 'soluble'), ('sand', 'insoluble'), ('sugar', 'soluble'), ('instant coffee', 'soluble'), ('pebbles', 'insoluble')], o='O5'),
 MC('What happens to oil in water?', 'It does not dissolve – it floats on top', [('It dissolves completely', 'Oil is insoluble.'), ('It sinks and disappears', 'It floats.')], o='O5'),
 MC('What does "soluble" mean?', 'Able to dissolve', [('Able to float', 'It means able to dissolve.'), ('Able to melt', 'Melting is different.')], o='O5'),
 MS('Select the things that make sugar dissolve faster.', ['warmer water', 'stirring', 'smaller pieces'], ['colder water', 'a bigger lump'], o='O5'),
 MC('Why does sugar dissolve faster in hot water?', 'The particles move faster and carry the sugar away', [('Hot water has more sugar', 'The amount is the same.'), ('Sugar melts in hot water', 'It dissolves.')], o='O5'),
 MC('Which dissolves faster: a sugar cube or the same sugar crushed?', 'The crushed sugar', [('The sugar cube', 'Smaller pieces dissolve faster.'), ('Both the same', 'Crushing speeds it up.')], o='O5'),
 CZ('Complete the sentences.', 'Salt {0} in water to make a {1}. Sand is {2}, so it sinks to the bottom.', [['dissolves'], ['solution'], ['insoluble']], o='O5'),
 MC('How is sea salt made?', 'Sea water is left in the sun and the water evaporates', [('Salt is dug up from the sea bed', 'Sea salt comes from evaporating sea water.'), ('Salt grows on plants', 'It comes from sea water.')], o='O5'),
 MC('What is left in the dish after salty water evaporates?', 'Salt crystals', [('Nothing', 'The salt stays.'), ('Sand', 'There was salt, not sand.')], o='O5'),
 MC('In the sugar race, what was changed?', 'The temperature of the water', [('The amount of sugar', 'Keep it the same.'), ('The stirring', 'Stir the same way.')], o='O5'),
 TB('Sugar race results. Complete the table.', ['Water', 'Time to dissolve (s)'], [['cold', '120'], ['warm', '60'], ['hot', B(30)]], o='O5', skill='Data', hint='Each step halved the time.'),
 MC('What is the conclusion of the sugar race?', 'Sugar dissolves faster in hotter water', [('Sugar dissolves faster in cold water', 'Cold was slowest.'), ('Temperature makes no difference', 'The times changed.')], o='O5'),
 MC('A solution looks…', 'clear (see-through)', [('cloudy with lumps', 'That is a mixture with an insoluble solid.'), ('always white', 'Solutions can be clear or coloured.')], o='O5'),
 MC('Why does sea water taste salty?', 'Salt is dissolved in it', [('Fish add salt', 'Salt is dissolved from rocks.'), ('It is a solid', 'Sea water is a solution.')], o='O5'),
)
s.adv(
 EX('Explain how you could separate a mixture of salt and sand.', [('add water: the salt dissolves, the sand does not', ['dissolv', 'water']), ('filter / pour through paper to remove the sand', ['filter', 'paper', 'sieve']), ('evaporate the water to get the salt back', ['evaporat'])], 'Add water so the salt dissolves. Pour it through filter paper to catch the sand. Then leave the salty water to evaporate, and the salt is left behind.', o='O5', d='H'),
 GR('Plot the sugar race results.', {'label': 'Water temperature (°C)', 'min': 0, 'max': 80, 'step': 20}, {'label': 'Time to dissolve (s)', 'min': 0, 'max': 140, 'step': 20}, [[10, 120], [30, 80], [50, 50], [70, 30]], o='O5', d='H', table_rows=[[10, 120], [30, 80], [50, 50], [70, 30]]),
 MC('You keep adding sugar to water, stirring each time. What happens in the end?', 'No more will dissolve, and sugar stays at the bottom', [('It all keeps dissolving for ever', 'There is a limit.'), ('The water turns into sugar', 'It stays a solution.')], o='O5', d='VH'),
 MC('Which is NOT a solution?', 'Sand in water', [('Salty water', 'That is a solution.'), ('Sweet tea', 'That is a solution.')], o='O5', d='H'),
)
s.labs('Dissolving lab',
 sort_lab('Does it dissolve?', 'Stir each substance into water. Sort them into soluble and insoluble.', ['Soluble (dissolves)', 'Insoluble (does not dissolve)'],
  [('salt', '🧂', 0, 'Salt dissolves and disappears.'), ('sand', '🏖️', 1, 'Sand sinks to the bottom.'), ('sugar', '🍬', 0, 'Sugar dissolves.'), ('cooking oil', '🫒', 1, 'Oil floats on top.'),
   ('instant coffee', '☕', 0, 'It dissolves and colours the water.'), ('flour', '🌾', 1, 'Flour makes the water cloudy and settles.'), ('pebbles', '🪨', 1, 'Pebbles stay solid at the bottom.')],
  [MC('How can you tell something has dissolved?', 'You cannot see it, and the liquid is clear', [('It sinks to the bottom', 'That means it did not dissolve.'), ('It floats on top', 'That means it did not dissolve.')], o='O5'),
   MC('How could you get the dissolved salt back?', 'Evaporate the water', [('Freeze the water', 'The salt stays dissolved.'), ('Stir it more', 'Stirring helps it dissolve.')], o='O5')]),
 home('Sugar race', 'Find out how temperature changes dissolving time.', ['3 cups', 'cold, warm and hot tap water (not boiling)', 'sugar and a teaspoon', 'a timer'],
  ['Use hot tap water only, with an adult.', 'Do not drink your experiment.'],
  ['Pour the same amount of cold, warm and hot water into the three cups.', 'Add one level teaspoon of sugar to the cold water, stir and start the timer.', 'Stop the timer when you cannot see any sugar.', 'Repeat with the warm and hot water.'],
  ['Water', 'Time to dissolve (s)'], [['Cold', {'min': 1, 'max': 1200}], ['Warm', {'min': 1, 'max': 1200}], ['Hot', {'min': 1, 'max': 1200}]], 'Times are usually between 10 and 300 seconds.',
  [MC('Which water won the race in your test?', 'The hot water', [('The cold water', 'Hot water usually wins.'), ('They all tied', 'Temperature makes a difference.')], o='O5')]))

U.mindmap(('Gases', 'Particles far apart; oxygen in, carbon dioxide out.', 'O1', '3.1'), ('States of water', 'Ice melts at 0 °C; water boils at 100 °C.', 'O2', '3.2'),
          ('Evaporation and condensation', 'The water cycle.', 'O3', '3.3'), ('Faster drying', 'Warmth, wind and surface area.', 'O4', '3.3'), ('Solutions', 'Soluble and insoluble; evaporate to get it back.', 'O5', '3.4'))
