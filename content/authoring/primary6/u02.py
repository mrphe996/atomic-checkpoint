# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 6 · Unit 2 Materials: properties and changes. Written by the Atomic teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kit6 import *
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'build', 'p6'))

OBJ = {
 'O1': {'sec': '2.1', 'code': 'Chemistry', 'codeNote': '', 't': 'Describe solids, liquids and gases using the particle model, and use melting point and boiling point as properties of a substance.'},
 'O2': {'sec': '2.1', 'code': 'Working scientifically', 'codeNote': '', 't': 'Read a thermometer, and tell the difference between evaporation and boiling.'},
 'O3': {'sec': '2.2', 'code': 'Chemistry', 'codeNote': '', 't': 'Name good thermal and electrical conductors and insulators, and explain how conduction moves heat.'},
 'O4': {'sec': '2.2', 'code': 'Working scientifically', 'codeNote': '', 't': 'Plan a fair test of insulators and use the results to choose the best material.'},
 'O5': {'sec': '2.3', 'code': 'Chemistry', 'codeNote': '', 't': 'Describe dissolving as a reversible change and use the words solute, solvent and solution.'},
 'O6': {'sec': '2.3', 'code': 'Working scientifically', 'codeNote': '', 't': 'Investigate how temperature changes the time a solute takes to dissolve.'},
 'O7': {'sec': '2.4', 'code': 'Chemistry', 'codeNote': '', 't': 'Identify chemical reactions from evidence, name reactants and products, and know most reactions are irreversible.'},
}
U = Unit(2, 'Materials: properties and changes', 'Chemistry: materials and their properties', 'Melting, boiling, conductors, dissolving and chemical reactions – how materials behave and change.', OBJ)
from vocab_u2 import V, SAY as SAYW
core = core_for(V, SAYW)

# =====================================================================================  2.1
s = U.section('2.1', 'Properties of substances', ['O1', 'O2']); s.words(V['2.1']); core(s, 'O1', 'O1')
s.stop(MC('At what temperature does pure water boil?', '100 °C', [('0 °C', 'That is the melting point of ice.'), ('34 °C', 'That is about when chocolate melts.'), ('60 °C', 'Water is hot at 60 °C, but it does not boil yet.')], o='O1', reason='Pure water boils at 100 degrees Celsius.'),
       MC('At what temperature does ice melt?', '0 °C', [('100 °C', 'That is the boiling point of water.'), ('34 °C', 'That is about when chocolate melts.')], o='O1'))
s.stop(MC('How is evaporation different from boiling?', 'Evaporation happens at the surface at any temperature; boiling happens all through the liquid at the boiling point.', [('Evaporation only happens at 100 °C.', 'A puddle evaporates on a warm day, far below 100 °C.'), ('They are exactly the same.', 'Think about where and when each one happens.'), ('Boiling happens only at the surface.', 'Boiling makes bubbles all through the liquid.')], o='O2'),
       MC('A puddle disappears on a sunny day. What happened to the water?', 'It evaporated', [('It boiled', 'The puddle never reached 100 °C.'), ('It melted', 'The water was already a liquid.'), ('It froze', 'It was a sunny day.')], o='O2'))
s.prac(
 GD('Is each one a solid, a liquid or a gas?', 'State', [('ice', 'solid'), ('steam', 'gas'), ('milk', 'liquid'), ('a wooden block', 'solid'), ('the air in a balloon', 'gas')], o='O1'),
 MT('Match each state to how its particles behave.', [('solid', 'packed tightly; they only wobble'), ('liquid', 'close together; they slide past each other'), ('gas', 'far apart; they move fast in all directions')], o='O1'),
 MC('What is a melting point?', 'The temperature at which a solid turns into a liquid', [('The temperature at which a liquid boils', 'That is the boiling point.'), ('The hottest a substance can get', 'Substances can get hotter than their melting point.'), ('The time it takes to melt', 'It is a temperature, not a time.')], o='O1'),
 MC('Why does chocolate melt in your hand?', 'Your hand is warmer than its melting point (about 34 °C)', [('Your hand is wet', 'Water does not melt chocolate.'), ('Chocolate is a gas', 'Chocolate is a solid until it melts.')], o='O1'),
 OD('Put these substances in order of melting point, from lowest to highest.', ['ice (0 °C)', 'chocolate (about 34 °C)', 'candle wax (about 60 °C)', 'iron (about 1500 °C)'], o='O1'),
 CZ('Complete the sentences.', 'Pure water melts at {0} °C and boils at {1} °C. These temperatures are {2} of water.', [['0', 'zero'], ['100', 'one hundred'], ['properties', 'property']], o='O1'),
 MC('Why are melting point and boiling point useful to scientists?', 'They help to identify a substance', [('They make a substance heavier', 'They do not change the mass.'), ('They are the same for every substance', 'Each substance has its own values.')], o='O1'),
 TK('Tick the things that are true about gases.', ['True', 'False'], [('a gas spreads out to fill its container', ['✓', '✗']), ('a gas has a fixed shape', ['✗', '✓']), ('a gas can be squashed', ['✓', '✗']), ('a gas has mass', ['✓', '✗'])], o='O1'),
 MC('A balloon full of air is heavier than an empty balloon. What does this show?', 'Gases have mass', [('Air is a liquid', 'Air is a gas.'), ('Balloons get heavier by themselves', 'The extra mass is the air inside.')], o='O1'),
 MC('What do we use to measure temperature?', 'A thermometer', [('A ruler', 'A ruler measures length.'), ('A forcemeter', 'A forcemeter measures force.'), ('A stopwatch', 'A stopwatch measures time.')], o='O2'),
 MC('How should you read a thermometer?', 'With your eyes level with the top of the red line', [('From above, looking down', 'Your reading will be wrong.'), ('Straight away, before the line stops moving', 'Wait until the line stops moving.')], o='O2'),
 MC('The red line is halfway between 20 °C and 30 °C. What is the temperature?', '25 °C', [('20 °C', 'The line is above 20.'), ('30 °C', 'The line has not reached 30.'), ('50 °C', 'Halfway between 20 and 30 is 25.')], o='O2', skill='Data'),
 MC('Where does evaporation happen?', 'At the surface of a liquid', [('All through the liquid', 'That is boiling.'), ('Only inside a kettle', 'Puddles and wet washing evaporate too.')], o='O2'),
 MC('Which wet towel will dry fastest?', 'One hung outside on a warm, windy day', [('One folded in a cold, dark cupboard', 'Cold and still air slows evaporation.'), ('One left in a plastic bag', 'The water cannot escape from the bag.')], o='O2'),
 GD('Is each one evaporation or boiling?', 'Change', [('a puddle drying in the sun', 'evaporation'), ('bubbles in a pan of water at 100 °C', 'boiling'), ('wet hair drying', 'evaporation'), ('a kettle making lots of steam', 'boiling')], o='O2'),
 MC('Water is heated. Its temperature rises to 100 °C, then stays at 100 °C. Why?', 'The water is boiling, and the temperature stays the same while it boils', [('The thermometer is broken', 'This always happens when water boils.'), ('The heater turned off', 'We kept heating it.')], o='O2', d='H'),
 MC('Why should you ask an adult to help with hot water?', 'Hot water and steam can burn you', [('Hot water is heavy', 'The danger is burns.'), ('Adults like hot water', 'It is about staying safe.')], o='O2'),
 TB('Read the thermometer readings and write each temperature.', ['Substance', 'Temperature (°C)'], [['ice water', B(0)], ['warm bath water', B(40)], ['boiling water', B(100)]], o='O2', reason='Ice melts at 0 °C; a warm bath is about 40 °C; water boils at 100 °C.', hint='Ice water is at its melting point; boiling water is at its boiling point.'),
)
s.adv(
 GR('Water was heated. Plot its temperature.', {'label': 'Time (minutes)', 'min': 0, 'max': 10, 'step': 2}, {'label': 'Temperature (°C)', 'min': 0, 'max': 120, 'step': 20}, [[0, 20], [2, 50], [4, 80], [6, 100], [8, 100], [10, 100]], o='O2', d='H', table_rows=[[0, 20], [2, 50], [4, 80], [6, 100], [8, 100], [10, 100]]),
 MC('Using the data 20, 50, 80, 100, 100, 100 °C (every 2 minutes), when did the water start to boil?', 'At about 6 minutes', [('At 0 minutes', 'It was only 20 °C then.'), ('At 10 minutes', 'It was already at 100 °C before that.'), ('It never boiled', 'It reached 100 °C and stayed there.')], o='O2', d='H'),
 EX('Explain, using particles, what happens when ice melts.', [('the particles get more energy / move more', ['energy', 'move', 'vibrate', 'faster']), ('they can slide past each other', ['slide', 'move past', 'pass']), ('the solid becomes a liquid', ['liquid'])], 'When ice is heated its particles get more energy and move more, until they can slide past each other: the solid becomes a liquid.', o='O1', d='H'),
 MC('A substance melts at 80 °C and boils at 218 °C. What state is it in at 100 °C?', 'Liquid', [('Solid', 'It is above its melting point.'), ('Gas', 'It is below its boiling point.')], o='O1', d='VH', reason='Above 80 °C it has melted; below 218 °C it has not boiled. So at 100 °C it is a liquid.'),
)
s.labs('Melting point lab',
 {'kind': 'test', 'title': 'Find the melting points', 'intro': 'Heat each solid slowly. The thermometer shows the temperature when the solid starts to melt. Read the scale and record its melting point.',
  'change': 'The substance', 'measure': 'Melting point', 'unit': '°C', 'max': 100, 'step': 10, 'instr': '🌡️',
  'conds': [{'k': 'butter', 't': 'Butter', 'emoji': '🧈', 'val': 30}, {'k': 'choc', 't': 'Chocolate', 'emoji': '🍫', 'val': 35}, {'k': 'wax', 't': 'Candle wax', 'emoji': '🕯️', 'val': 60}],
  'qs': [MC('Which substance has the highest melting point?', 'Candle wax', [('Butter', 'Butter melted at about 30 °C.'), ('Chocolate', 'Chocolate melted at about 35 °C.')], o='O1'),
         MC('Which would melt first on a warm day at 32 °C?', 'Butter', [('Candle wax', 'Wax needs about 60 °C.'), ('Chocolate', 'Chocolate needs about 35 °C – close, but not yet.')], o='O1'),
         MC('Why do we say melting point is a property?', 'Each substance always melts at its own temperature', [('All substances melt at the same temperature', 'Look at your table – they are different.'), ('Melting point changes every day', 'It stays the same for a pure substance.')], o='O1')]},
 {'title': 'Which puddle dries first?', 'intro': 'Compare evaporation in a warm place and a cool place.',
  'need': ['two saucers or small plates', 'a measuring spoon or small measuring cup', 'water', 'a sunny windowsill and a shady place'],
  'safety': ['Wipe up spills so nobody slips.', 'Do not use glass in direct sun near anything that could burn.'],
  'steps': ['Put the same amount of water on each saucer – for example, 4 spoons.', 'Put one saucer in a sunny place and one in a shady place.', 'After 3 hours, pour the water left on each saucer back into the spoon and count the spoonfuls.', 'Compare your results.'],
  'record': {'head': ['Place', 'Spoonfuls at the start', 'Spoonfuls left after 3 hours'], 'rows': [['Sunny place', {'min': 1, 'max': 20}, {'min': 0, 'max': 20}], ['Shady place', {'min': 1, 'max': 20}, {'min': 0, 'max': 20}]], 'hint': 'Use whole numbers or halves, such as 4 or 2.5.'},
  'qs': [MC('Where did more water evaporate?', 'In the sunny place', [('In the shady place', 'Warmth makes evaporation faster.'), ('Both lost exactly the same', 'Check your table again.')], o='O2'),
         MC('Why was this a fair test?', 'Both saucers started with the same amount of water', [('The saucers were in different places', 'That was the thing we changed.'), ('We used the sun', 'Fair means only one thing changes.')], o='O2')]})

# =====================================================================================  2.2
s = U.section('2.2', 'Thermal and electrical conductors', ['O3', 'O4']); s.words(V['2.2']); core(s, 'O3', 'O3')
s.stop(MC('Why is a saucepan handle made of plastic, not metal?', 'Plastic is a thermal insulator, so the handle stays cool', [('Plastic is a good conductor of heat', 'Then the handle would get hot.'), ('Plastic is heavier than metal', 'That is not the reason.'), ('Metal handles are too shiny', 'It is about heat.')], o='O3'),
       MC('Why is the pan itself made of metal?', 'Metal conducts heat quickly to the food', [('Metal keeps the food cold', 'Metal passes heat on.'), ('Metal is an insulator', 'Metals are good conductors.')], o='O3'))
s.stop(MC('Which will make the lamp light: a copper wire or a rubber band?', 'A copper wire', [('A rubber band', 'Rubber is an electrical insulator.'), ('Both', 'Only conductors complete the circuit.'), ('Neither', 'Copper is a very good conductor.')], o='O3'),
       MC('Which object in the gap would make the lamp light?', 'A metal key', [('A wooden pencil', 'Wood is an insulator.'), ('A plastic ruler', 'Plastic is an insulator.'), ('A paper card', 'Paper is an insulator.')], o='O3'))
s.prac(
 MC('What is conduction?', 'Heat or electricity passing through a material', [('A type of circuit', 'Conduction is how heat or electricity moves.'), ('Heat leaving as light', 'That is not conduction.')], o='O3'),
 MC('A metal spoon is put in hot tea. Which end gets hot first?', 'The end in the tea', [('The handle', 'Heat travels from the hot end to the cold end.'), ('Both ends at the same time', 'The heat has to travel along the spoon.')], o='O3'),
 OD('Put the steps of conduction in order.', ['particles at the hot end vibrate faster', 'they bump into the particles next to them', 'the energy is passed along', 'the cold end gets warm'], o='O3'),
 GD('Is each material a thermal conductor or a thermal insulator?', 'Type', [('steel', 'conductor'), ('wool', 'insulator'), ('copper', 'conductor'), ('wood', 'insulator'), ('plastic', 'insulator')], o='O3'),
 GD('Is each material an electrical conductor or an electrical insulator?', 'Type', [('aluminium foil', 'conductor'), ('rubber', 'insulator'), ('a steel paper clip', 'conductor'), ('glass', 'insulator')], o='O3'),
 MS('Select the good conductors of electricity.', ['copper', 'iron', 'aluminium'], ['plastic', 'wood', 'rubber'], o='O3', reason='Metals conduct electricity.'),
 MC('Why are electrical wires covered in plastic?', 'Plastic is an insulator, so it keeps us safe from electric shocks', [('Plastic makes electricity flow faster', 'Copper carries the electricity; plastic stops it escaping.'), ('To make the wires colourful', 'Colour is not the main reason.')], o='O3'),
 MC('Why are wires made of copper inside?', 'Copper is a very good electrical conductor', [('Copper is an insulator', 'Copper conducts electricity well.'), ('Copper is soft and squashy', 'It is chosen because it conducts.')], o='O3'),
 MC('What should you never do near electricity?', 'Touch bare wires or play near sockets', [('Turn on a lamp with a switch', 'Using a switch is safe.'), ('Use a torch', 'A torch is safe.')], o='O3'),
 MT('Match each object to the property it needs.', [('cooking pan', 'good thermal conductor'), ('oven glove', 'good thermal insulator'), ('electric wire', 'good electrical conductor'), ('plug case', 'good electrical insulator')], o='O3'),
 MC('Why do people wear woollen jumpers in winter?', 'Wool is a thermal insulator, so it keeps body heat in', [('Wool makes heat', 'Wool does not make heat; it stops it escaping.'), ('Wool is a conductor', 'Conductors would let heat escape.')], o='O3'),
 MC('In the cup test, what did we CHANGE?', 'The material of the cup', [('The amount of hot water', 'That stayed the same to be fair.'), ('The temperature', 'That is what we measured.')], o='O4'),
 MC('In the cup test, what did we MEASURE?', 'The temperature of the water every five minutes', [('The size of the cup', 'Keep the size the same.'), ('The colour of the cup', 'Colour was not measured.')], o='O4'),
 MS('Which things must stay the SAME to keep the cup test fair?', ['the amount of water', 'the starting temperature of the water', 'the size of the cups'], ['the material of the cups'], o='O4', reason='Only the material changes.'),
 TB('Water started at 80 °C in each cup. After 20 minutes: metal 40 °C, plastic 50 °C, foam 60 °C. How much did each cool?', ['Cup', 'Fall in temperature (°C)'], [['metal', B(40)], ['plastic', B(30)], ['foam', B(20)]], o='O4', reason='80 − 40 = 40; 80 − 50 = 30; 80 − 60 = 20.', skill='Data'),
 MC('Using those results, which cup is the best thermal insulator?', 'The foam cup', [('The metal cup', 'It cooled the most – it is the best conductor.'), ('The plastic cup', 'The foam cup kept the water hotter.')], o='O4'),
 MC('Why does a lid help keep a drink hot?', 'It stops heat escaping from the top', [('It makes the drink heavier', 'Weight does not keep a drink hot.'), ('It lets cold air in', 'It stops air moving in and out.')], o='O4', d='H'),
 MC('Which material would make the best tea cosy (cover for a teapot)?', 'Thick wool', [('Thin aluminium foil only', 'Thin foil is a conductor.'), ('Steel', 'Steel is a conductor.')], o='O4'),
)
s.adv(
 GR('Plot the temperature of the water in the foam cup.', {'label': 'Time (minutes)', 'min': 0, 'max': 20, 'step': 5}, {'label': 'Temperature (°C)', 'min': 0, 'max': 100, 'step': 20}, [[0, 80], [5, 75], [10, 70], [15, 65], [20, 60]], o='O4', d='H', table_rows=[[0, 80], [5, 75], [10, 70], [15, 65], [20, 60]]),
 EX('Explain why a metal spoon in hot soup gets hot, but a wooden spoon does not.', [('metal is a good thermal conductor', ['metal', 'conductor', 'conducts']), ('wood is an insulator', ['wood', 'insulator']), ('heat moves along metal by conduction', ['conduction', 'heat moves', 'travels'])], 'Metal is a good thermal conductor, so heat moves along it by conduction. Wood is an insulator, so little heat moves along it.', o='O3', d='H'),
 MC('Arun tested cups but used 100 mL of water in the metal cup and 200 mL in the foam cup. What is wrong?', 'It is not a fair test – the amount of water was different', [('Nothing is wrong', 'Two things changed.'), ('He should have used cold water', 'Hot water is right for this test.')], o='O4', d='H'),
 MC('Why do some saucepans have a copper base?', 'Copper conducts heat even better than many other metals', [('Copper is an insulator', 'Copper is a conductor.'), ('Copper keeps the food cold', 'It passes heat quickly to the food.')], o='O3', d='VH'),
)
s.labs('Insulator lab',
 {'kind': 'test', 'title': 'Which cup keeps water hottest?', 'intro': 'The same amount of water at 80 °C was poured into three cups. After 20 minutes, read the thermometer in each cup.',
  'change': 'The cup material', 'measure': 'Temperature after 20 minutes', 'unit': '°C', 'max': 100, 'step': 10, 'instr': '🌡️',
  'conds': [{'k': 'metal', 't': 'Metal cup', 'emoji': '🥫', 'val': 40}, {'k': 'plastic', 't': 'Plastic cup', 'emoji': '🥤', 'val': 50}, {'k': 'foam', 't': 'Foam cup', 'emoji': '☕', 'val': 60}],
  'qs': [MC('Which cup kept the water hottest?', 'The foam cup', [('The metal cup', 'It was the coolest.'), ('The plastic cup', 'The foam cup was hotter.')], o='O4'),
         MC('Which material is the best thermal conductor?', 'Metal', [('Foam', 'Foam kept the heat in – an insulator.'), ('Plastic', 'Metal let the heat out fastest.')], o='O3'),
         MC('Why was the same amount of water used in each cup?', 'To keep the test fair', [('To make the water hotter', 'It does not change the starting temperature.'), ('Because cups are all the same', 'They are different materials.')], o='O4')]},
 {'title': 'Ice cube race', 'intro': 'Find out which material conducts heat best: put an ice cube on different surfaces and time how long it takes to melt.',
  'need': ['3 ice cubes of the same size', 'a metal tray or baking tin', 'a plastic plate', 'a wooden chopping board', 'a clock or timer'],
  'safety': ['Wipe up the water when you finish.', 'Ask an adult before using kitchen things.'],
  'steps': ['Put the three surfaces side by side in the same room.', 'Put one ice cube on each at the same time.', 'Check every 5 minutes. Write down the time when each ice cube has completely melted.', 'Compare your times.'],
  'record': {'head': ['Surface', 'Time to melt (minutes)'], 'rows': [['Metal', {'min': 1, 'max': 180}], ['Plastic', {'min': 1, 'max': 180}], ['Wood', {'min': 1, 'max': 180}]], 'hint': 'Times are usually between 10 and 90 minutes.'},
  'qs': [MC('In most tests the ice on the metal melts first. Why?', 'Metal conducts heat from the room into the ice quickly', [('Metal is cold', 'Metal feels cold because it takes heat from your hand quickly.'), ('Metal is an insulator', 'Metal is a good conductor.')], o='O3', d='H')]})

# =====================================================================================  2.3
s = U.section('2.3', 'Reversible changes', ['O5', 'O6']); s.words(V['2.3']); core(s, 'O5', 'O5')
s.stop(MC('In salty water, which is the solute and which is the solvent?', 'Salt is the solute; water is the solvent', [('Water is the solute; salt is the solvent', 'The solute is the substance that dissolves.'), ('Both are solvents', 'One dissolves in the other.')], o='O5'),
       MC('Sugar is stirred into tea. What is the solution?', 'The sweet tea', [('The sugar', 'The sugar is the solute.'), ('The spoon', 'The spoon is not part of it.')], o='O5'))
s.stop(MC('Why does sugar dissolve faster in hot water?', 'The water particles move faster and carry the sugar away quicker', [('Hot water has more sugar in it', 'The amount of sugar is the same.'), ('Sugar melts in hot water', 'Sugar dissolves; it does not melt in tea.'), ('Cold water is heavier', 'That is not the reason.')], o='O6'),
       MC('In which glass will sugar dissolve fastest?', 'Hot water at 70 °C', [('Cold water at 10 °C', 'The coldest water is slowest.'), ('Warm water at 30 °C', 'The hottest water is fastest.')], o='O6'))
s.prac(
 MC('What is a reversible change?', 'A change that can be undone', [('A change that makes new substances', 'That is a chemical reaction.'), ('A change that can never be undone', 'That is irreversible.')], o='O5'),
 MS('Select the reversible changes.', ['melting', 'freezing', 'dissolving', 'evaporating'], ['burning', 'cooking an egg'], o='O5'),
 MC('When sugar dissolves, where does it go?', 'Its particles spread out between the water particles', [('It disappears for ever', 'It is still there – the water tastes sweet.'), ('It turns into water', 'The sugar is still sugar.')], o='O5'),
 MT('Match each word to its meaning.', [('solute', 'the substance that dissolves'), ('solvent', 'the liquid it dissolves in'), ('solution', 'the clear mixture made'), ('soluble', 'able to dissolve')], o='O5'),
 GD('Is each substance soluble or insoluble in water?', 'In water', [('salt', 'soluble'), ('sand', 'insoluble'), ('sugar', 'soluble'), ('chalk', 'insoluble')], o='O5'),
 CZ('Complete the sentences.', 'When salt dissolves in water, salt is the {0} and water is the {1}. Together they make a {2}.', [['solute'], ['solvent'], ['solution']], o='O5'),
 MC('How can you get salt back from salty water?', 'Leave it in a warm place so the water evaporates', [('Stir it for a long time', 'Stirring helps it dissolve, not come back.'), ('Put it in the fridge', 'The salt stays dissolved.')], o='O5'),
 MC('What does a solution look like?', 'Clear and the same all the way through', [('Cloudy with bits at the bottom', 'That is a mixture with an insoluble substance.'), ('Always white', 'Solutions can be coloured, like squash.')], o='O5'),
 MC('Why is dissolving a reversible change?', 'We can get the solute back by evaporating the water', [('It makes new substances', 'No new substances are made.'), ('It cannot be undone', 'It can be undone.')], o='O5'),
 MC('Where does sea salt come from?', 'Sea water evaporates and leaves salt crystals', [('It grows on plants', 'It comes from sea water.'), ('It falls with the rain', 'Rain water is not salty.')], o='O5'),
 MC('In the dissolving test, what did we CHANGE?', 'The temperature of the water', [('The amount of sugar', 'That stayed the same.'), ('The way of stirring', 'That stayed the same.')], o='O6'),
 MC('In the dissolving test, what did we MEASURE?', 'The time the sugar took to dissolve', [('The temperature of the water', 'That was what we changed.'), ('The mass of the glass', 'That was not measured.')], o='O6'),
 MS('Which things must stay the SAME to make the dissolving test fair?', ['the amount of water', 'the amount of sugar', 'the way we stir'], ['the temperature of the water'], o='O6'),
 MC('Why do scientists repeat a test?', 'To make the results more reliable', [('To make the test take longer', 'That is not the reason.'), ('To change the answer', 'Repeats help check the results.')], o='O6'),
 TB('Sugar dissolving times at different temperatures. Find the average of each pair of tests.', ['Water temperature', 'Test 1 (s)', 'Test 2 (s)', 'Average (s)'], [['10 °C', '118', '122', B(120)], ['40 °C', '62', '58', B(60)], ['70 °C', '31', '29', B(30)]], o='O6', reason='Add the two times and divide by 2.', skill='Data'),
 MC('What pattern do these results show?', 'The hotter the water, the shorter the time to dissolve', [('The hotter the water, the longer it takes', 'The times got shorter.'), ('Temperature makes no difference', 'The times changed a lot.')], o='O6'),
 MC('What else makes sugar dissolve faster?', 'Stirring', [('Using a bigger glass', 'Glass size does not help much.'), ('Adding more sugar', 'More sugar takes longer.')], o='O6'),
 MC('Mia predicted: "Sugar dissolves faster in hot water." Her results showed this. What can she say?', 'My prediction was correct', [('My prediction was wrong', 'The results agreed with it.'), ('Predictions do not matter', 'Checking predictions is part of science.')], o='O6'),
)
s.adv(
 GR('Plot the dissolving times.', {'label': 'Water temperature (°C)', 'min': 0, 'max': 80, 'step': 20}, {'label': 'Time to dissolve (s)', 'min': 0, 'max': 140, 'step': 20}, [[10, 120], [30, 80], [50, 50], [70, 30]], o='O6', d='H', table_rows=[[10, 120], [30, 80], [50, 50], [70, 30]]),
 MC('Using the times 120 s (10 °C), 80 s (30 °C), 50 s (50 °C) and 30 s (70 °C), predict the time at 60 °C.', 'About 40 seconds', [('About 90 seconds', 'That is slower than at 30 °C.'), ('About 10 seconds', 'That is faster than at 70 °C.'), ('About 60 seconds', 'It should be between 50 s and 30 s.')], o='O6', d='VH'),
 EX('Explain how you could show that dissolving salt is a reversible change.', [('dissolve salt in water to make a solution', ['dissolve', 'solution']), ('leave it to evaporate / heat it', ['evaporat', 'heat', 'warm']), ('salt crystals are left / we get the salt back', ['crystal', 'salt is left', 'back'])], 'Dissolve salt in water, then leave the solution in a warm place. The water evaporates and the salt crystals are left, so the change can be undone.', o='O5', d='H'),
 MC('Sand is stirred into water and then the water is evaporated. What is left?', 'The sand – it never dissolved', [('Nothing', 'The sand stays.'), ('A clear solution', 'Sand is insoluble, so there was no solution.')], o='O5', d='H'),
)
s.labs('Dissolving lab',
 {'kind': 'test', 'title': 'How does temperature change dissolving time?', 'intro': 'One spoon of sugar is stirred into the same amount of water at different temperatures. Read the stopwatch scale to see how long the sugar took to dissolve.',
  'change': 'The water temperature', 'measure': 'Time to dissolve', 'unit': 's', 'max': 140, 'step': 10, 'instr': '⏱️',
  'conds': [{'k': 't10', 't': '10 °C (cold)', 'emoji': '🧊', 'val': 120}, {'k': 't30', 't': '30 °C (warm)', 'emoji': '🥛', 'val': 80}, {'k': 't50', 't': '50 °C (hot)', 'emoji': '☕', 'val': 50}, {'k': 't70', 't': '70 °C (very hot)', 'emoji': '♨️', 'val': 30}],
  'qs': [MC('What happened to the dissolving time as the water got hotter?', 'It got shorter', [('It got longer', 'Look at the bar chart again.'), ('It stayed the same', 'The times changed.')], o='O6'),
         MC('Which variable did you CHANGE?', 'The water temperature', [('The time', 'That was measured.'), ('The amount of sugar', 'That stayed the same.')], o='O6'),
         MC('Which is the solvent in this experiment?', 'Water', [('Sugar', 'Sugar is the solute.'), ('The spoon', 'The spoon is equipment.')], o='O5')]},
 {'title': 'Sugar cube race', 'intro': 'Time how long a sugar cube takes to dissolve in cold and warm water.',
  'need': ['2 sugar cubes (or 2 level teaspoons of sugar)', '2 cups', 'cold tap water and warm tap water (not boiling)', 'a spoon and a timer'],
  'safety': ['Use warm tap water, not boiling water.', 'Do not drink your experiment.'],
  'steps': ['Pour the same amount of cold water into one cup and warm water into the other.', 'Drop a sugar cube into the cold water, start the timer and stir slowly. Stop the timer when you cannot see any sugar.', 'Repeat with the warm water, stirring in the same way.', 'Compare your times.'],
  'record': {'head': ['Water', 'Time to dissolve (seconds)'], 'rows': [['Cold water', {'min': 5, 'max': 900}], ['Warm water', {'min': 5, 'max': 900}]], 'hint': 'Times are usually between 20 and 300 seconds.'},
  'qs': [MC('In which water did the sugar dissolve faster?', 'Warm water', [('Cold water', 'Warm water particles move faster.'), ('They were the same', 'Look at your times again.')], o='O6'),
         MC('Why should you stir both cups the same way?', 'To keep the test fair', [('To make it more fun', 'It is about fairness.'), ('Stirring stops dissolving', 'Stirring speeds it up – so it must be the same.')], o='O6')]})

# =====================================================================================  2.4
s = U.section('2.4', 'Chemical reactions', ['O7']); s.words(V['2.4']); core(s, 'O7', 'O7')
s.stop(MC('What do we call the new substances made in a chemical reaction?', 'Products', [('Reactants', 'Reactants are what we start with.'), ('Solvents', 'A solvent dissolves things.'), ('Solutions', 'A solution is a mixture.')], o='O7'),
       MC('Vinegar and baking soda react. What are vinegar and baking soda called?', 'The reactants', [('The products', 'The products are the new substances made.'), ('The evidence', 'Evidence is what we observe.')], o='O7'))
s.stop(MC('Is rusting a reversible or an irreversible change?', 'Irreversible – rust is a new substance', [('Reversible – rust turns back into iron by itself', 'Rust does not turn back.'), ('It is not a change', 'The iron changes into rust.')], o='O7'),
       MC('Which of these is an irreversible change?', 'Cooking an egg', [('Melting ice', 'Ice can be frozen again.'), ('Dissolving sugar', 'The sugar can be got back.')], o='O7'))
s.prac(
 MC('What is a chemical reaction?', 'A change in which new substances are made', [('A change of state, like melting', 'No new substance is made when ice melts.'), ('Mixing sand and water', 'The sand and water stay the same.')], o='O7'),
 MS('Select the evidence that a chemical reaction may have happened.', ['bubbles of gas', 'a colour change', 'a temperature change', 'light or a smell'], ['the object is moved', 'it is cut into pieces'], o='O7'),
 GD('Is each change reversible or irreversible?', 'Change', [('burning paper', 'irreversible'), ('melting chocolate', 'reversible'), ('baking a cake', 'irreversible'), ('freezing water', 'reversible'), ('rusting', 'irreversible')], o='O7'),
 MC('Baking soda is added to vinegar. It fizzes. What gas is made?', 'Carbon dioxide', [('Oxygen', 'The gas is carbon dioxide.'), ('Steam', 'This reaction does not need heating.')], o='O7'),
 MT('Match each reaction to its evidence.', [('baking soda and vinegar', 'bubbles of gas'), ('a candle burning', 'light and heat'), ('a nail going rusty', 'a colour change to orange-brown'), ('milk going sour', 'a new smell')], o='O7'),
 CZ('Complete the sentence.', 'In a chemical reaction the {0} react together to make new substances called {1}.', [['reactants'], ['products']], o='O7'),
 MC('Which three things react to make rust?', 'Iron, water and oxygen', [('Iron, sand and salt', 'Rust needs water and oxygen.'), ('Plastic, water and air', 'Plastic does not rust.')], o='O7'),
 MC('How can we stop a bicycle chain going rusty?', 'Keep it dry and cover it with oil', [('Leave it out in the rain', 'Water helps rust form.'), ('Paint it with water', 'Water causes rust.')], o='O7'),
 MC('When a candle burns, which part is a reversible change?', 'The wax melting', [('The wick burning', 'Burning makes new substances.'), ('Smoke being made', 'Smoke is a new substance.')], o='O7', d='H'),
 MS('Select the products made when a candle burns.', ['carbon dioxide', 'water', 'soot'], ['iron', 'salt'], o='O7'),
 MC('Why can a cooked egg not be turned back into a raw egg?', 'Cooking is a chemical reaction that makes new substances', [('The egg is too hot', 'Cooling it does not make it raw again.'), ('The shell is broken', 'Even in its shell it cannot be uncooked.')], o='O7'),
 MC('In the balloon experiment, why did the balloon fill up?', 'The reaction made carbon dioxide gas', [('Air was blown into it', 'Nobody blew into it.'), ('Vinegar turned into a gas by boiling', 'The vinegar did not boil.')], o='O7'),
 OD('Put the steps of the balloon experiment in order.', ['pour vinegar into the bottle', 'put baking soda in the balloon', 'stretch the balloon over the bottle neck', 'tip the baking soda into the vinegar'], o='O7'),
 MC('Which of these is NOT evidence of a chemical reaction?', 'Water turning into ice', [('A firework giving out light', 'Light is evidence of a reaction.'), ('Fizzing when an antacid tablet is put in water', 'Gas bubbles are evidence.')], o='O7'),
 TK('Tick the changes that make new substances.', ['New substance', 'No new substance'], [('burning wood', ['✓', '✗']), ('boiling water', ['✗', '✓']), ('toasting bread', ['✓', '✗']), ('cutting paper', ['✗', '✓'])], o='O7'),
 MC('Most chemical reactions are…', 'irreversible', [('reversible', 'Most cannot be undone.'), ('changes of state', 'Changes of state are physical changes.')], o='O7'),
 MC('Which safety rule is most important when doing the vinegar and baking soda reaction?', 'Wear eye protection and keep the mixture away from your eyes', [('Taste the products', 'Never taste experiments.'), ('Shake the bottle with the lid on', 'Gas pressure could make it burst.')], o='O7'),
 MC('Why is burning dangerous to do without an adult?', 'It gives out heat and light, and can start a fire', [('It is too quiet', 'Noise is not the danger.'), ('It makes things wet', 'Burning is hot, not wet.')], o='O7'),
)
s.adv(
 EX('Explain why burning wood is a chemical reaction. Give TWO pieces of evidence.', [('new substances are made (ash/smoke/carbon dioxide)', ['new substance', 'ash', 'smoke', 'carbon dioxide']), ('light / heat is given out', ['light', 'heat']), ('it cannot be undone / irreversible', ['irreversible', 'cannot', 'undone'])], 'Burning makes new substances such as ash, smoke and carbon dioxide; it gives out heat and light; and it cannot be undone.', o='O7', d='H'),
 TB('Lee put 1, 2 and 3 spoons of baking soda into balloons on bottles of vinegar. Complete the table to match his results.', ['Spoons of baking soda', 'Balloon size around (cm)'], [['1', '20'], ['2', '30'], ['3', B(40)]], o='O7', d='H', hint='Each extra spoon added 10 cm.', reason='The pattern adds 10 cm per spoon: 20, 30, 40.', skill='Data'),
 MC('What is the best conclusion from Lee\'s results?', 'More baking soda made more gas', [('Baking soda stops the reaction', 'The balloon got bigger, not smaller.'), ('The vinegar made all the gas on its own', 'Both reactants are needed.')], o='O7', d='H'),
 MC('Is mixing salt and sand a chemical reaction?', 'No – no new substance is made and they can be separated', [('Yes – two substances are mixed', 'Mixing alone does not make new substances.'), ('Yes – the colour changes', 'The colours stay the same.')], o='O7', d='VH'),
)
s.labs('Reversible or not? lab',
 {'kind': 'sort', 'title': 'Sort the changes', 'intro': 'Can each change be undone? Sort the cards into reversible changes and chemical reactions (irreversible).',
  'groups': ['Reversible change', 'Chemical reaction (irreversible)'],
  'items': [{'t': 'ice melting', 'emoji': '🧊', 'g': 0, 'why': 'Water can be frozen again.'}, {'t': 'wood burning', 'emoji': '🔥', 'g': 1, 'why': 'Ash and smoke are new substances.'},
            {'t': 'sugar dissolving', 'emoji': '🥄', 'g': 0, 'why': 'Evaporate the water to get the sugar back.'}, {'t': 'a nail rusting', 'emoji': '🔩', 'g': 1, 'why': 'Rust is a new substance.'},
            {'t': 'cooking an egg', 'emoji': '🍳', 'g': 1, 'why': 'A cooked egg cannot become raw again.'}, {'t': 'water evaporating', 'emoji': '☁️', 'g': 0, 'why': 'The steam can condense back to water.'},
            {'t': 'vinegar and baking soda fizzing', 'emoji': '🫧', 'g': 1, 'why': 'Carbon dioxide gas is made.'}, {'t': 'chocolate melting', 'emoji': '🍫', 'g': 0, 'why': 'It sets again when it cools.'}],
  'qs': [MC('What do all the chemical reactions have in common?', 'They make new substances', [('They are all cold', 'Burning is hot.'), ('They can all be undone', 'They are irreversible.')], o='O7'),
         MC('Which change in the lab gave bubbles as evidence?', 'Vinegar and baking soda', [('Ice melting', 'No gas is made.'), ('Chocolate melting', 'No gas is made.')], o='O7')]},
 {'title': 'Blow up a balloon with a reaction', 'intro': 'Use a reaction to make gas, and see how the amount of baking soda changes the balloon.',
  'need': ['2 small plastic bottles', 'vinegar', 'baking soda', '2 balloons', 'a teaspoon and a funnel (or paper cone)', 'a piece of string and a ruler'],
  'safety': ['Wear glasses or goggles if you have them – keep vinegar away from your eyes.', 'Do this outside or over a sink, with an adult.'],
  'steps': ['Pour the same amount of vinegar (about 3 cm deep) into each bottle.', 'Use the funnel to put 1 teaspoon of baking soda in one balloon and 2 teaspoons in the other.', 'Stretch each balloon over a bottle neck, then lift it so the baking soda falls in.', 'When the fizzing stops, wrap string around each balloon and measure the string with a ruler.'],
  'record': {'head': ['Baking soda', 'Distance around the balloon (cm)'], 'rows': [['1 teaspoon', {'min': 5, 'max': 80}], ['2 teaspoons', {'min': 5, 'max': 80}]], 'hint': 'Balloons are usually between 15 and 50 cm around.'},
  'qs': [MC('What evidence showed a reaction happened?', 'Fizzing bubbles and the balloon filling with gas', [('The bottle stayed the same', 'Something changed – look again.'), ('The vinegar got colder only', 'The main evidence was gas.')], o='O7'),
         MC('Which balloon was usually bigger?', 'The one with 2 teaspoons of baking soda', [('The one with 1 teaspoon', 'More reactant usually makes more gas.'), ('They are always the same', 'More baking soda makes more gas.')], o='O7')]})

U.mindmap(('States of matter', 'Particles in solids, liquids and gases.', 'O1', '2.1'), ('Melting and boiling points', 'Properties that help identify substances.', 'O2', '2.1'),
          ('Conductors and insulators', 'Metals conduct heat and electricity; wood, plastic and wool insulate.', 'O3', '2.2'), ('Fair tests', 'Change one thing, measure one thing.', 'O4', '2.2'),
          ('Dissolving', 'Solute + solvent = solution; a reversible change.', 'O5', '2.3'), ('Dissolving faster', 'Hotter water dissolves sugar faster.', 'O6', '2.3'),
          ('Chemical reactions', 'Reactants make new products; most cannot be undone.', 'O7', '2.4'))
