# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 6 · Unit 5 Forces and electricity. Written by the Camday teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kit6 import *
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'build', 'p6'))

OBJ = {
 'O1': {'sec': '5.1', 'code': 'Physics', 'codeNote': '', 't': 'Explain the difference between mass (kg) and weight (N), and that weight is the force of gravity.'},
 'O2': {'sec': '5.1', 'code': 'Working scientifically', 'codeNote': '', 't': 'Measure weight with a forcemeter and find the pattern between mass and weight.'},
 'O3': {'sec': '5.2', 'code': 'Physics', 'codeNote': '', 't': 'Draw force arrows, and describe the effects of balanced and unbalanced forces, friction, air resistance and water resistance.'},
 'O4': {'sec': '5.3', 'code': 'Physics', 'codeNote': '', 't': 'Explain floating and sinking using weight, upthrust and displacement.'},
 'O5': {'sec': '5.3', 'code': 'Working scientifically', 'codeNote': '', 't': 'Investigate boat designs and describe the pattern on a scatter graph.'},
 'O6': {'sec': '5.4', 'code': 'Physics', 'codeNote': '', 't': 'Draw circuit diagrams with symbols, and compare series and parallel circuits.'},
 'O7': {'sec': '5.4', 'code': 'Physics', 'codeNote': '', 't': 'Describe how the number of cells (voltage) changes the brightness of a lamp, and use electricity safely.'},
}
U = Unit(5, 'Forces and electricity', 'Physics: forces and electricity', 'Mass and weight, pushes and pulls, floating and sinking, and series and parallel circuits.', OBJ)
from vocab_u5 import V, SAY as SAYW
core = core_for(V, SAYW)

# =====================================================================================  5.1
s = U.section('5.1', 'Mass and weight', ['O1', 'O2']); s.words(V['5.1']); core(s, 'O1', 'O1')
s.stop(MC('What unit do we use to measure weight?', 'Newtons (N)', [('Kilograms (kg)', 'Kilograms measure mass.'), ('Centimetres (cm)', 'Centimetres measure length.'), ('Degrees Celsius', 'That measures temperature.')], o='O1'),
       MC('What do we use to measure weight?', 'A forcemeter', [('A ruler', 'A ruler measures length.'), ('A thermometer', 'A thermometer measures temperature.')], o='O1'))
s.stop(MC('On the Moon, what changes: your mass or your weight?', 'Your weight – the Moon\'s gravity is weaker', [('Your mass', 'You have the same amount of matter everywhere.'), ('Both', 'Only the pull of gravity changes.'), ('Neither', 'Weight does change.')], o='O1'),
       MC('An astronaut has a mass of 60 kg on Earth. What is her mass on the Moon?', '60 kg', [('10 kg', 'That is not right – her mass does not change.'), ('600 kg', 'Mass does not change.')], o='O1'))
s.prac(
 MC('What is mass?', 'The amount of matter (stuff) in an object', [('The pull of gravity on an object', 'That is weight.'), ('How tall an object is', 'That is height.')], o='O1'),
 MC('What is weight?', 'The force of gravity pulling on an object', [('The amount of matter in an object', 'That is mass.'), ('How big an object is', 'That is size or volume.')], o='O1'),
 GD('Which unit goes with each quantity?', 'Unit', [('mass', 'kilograms (kg)'), ('weight', 'newtons (N)'), ('length', 'metres (m)')], o='O1'),
 MC('What is gravity?', 'A force that pulls objects towards the centre of the Earth', [('A push from the wind', 'That is air pushing.'), ('A kind of magnet', 'Gravity pulls everything, not only metals.')], o='O1'),
 MC('On Earth, about how much does a 1 kg bag of rice weigh?', 'About 10 N', [('About 1 N', 'That is about 100 g.'), ('About 100 N', 'That is about 10 kg.')], o='O2'),
 TB('Use "1 kg weighs about 10 N" to complete the table.', ['Mass', 'Weight on Earth'], [['1 kg', '10 N'], ['2 kg', B(20)], ['5 kg', B(50)], ['0.5 kg', B(5)]], o='O2', reason='Multiply the mass in kg by 10.', skill='Data'),
 MC('Why is the Moon\'s gravity weaker than the Earth\'s?', 'The Moon is much smaller than the Earth', [('The Moon is further from the Sun', 'It is about size.'), ('The Moon has no air', 'Air does not cause gravity.')], o='O1'),
 MC('About how strong is gravity on the Moon compared with Earth?', 'About one sixth as strong', [('Twice as strong', 'It is weaker.'), ('Exactly the same', 'It is weaker.')], o='O1'),
 MC('Why can astronauts bounce high on the Moon?', 'Their weight is much less there', [('Their mass is less', 'Their mass is the same.'), ('They have springs in their boots', 'It is the weaker gravity.')], o='O1'),
 MC('How does a forcemeter work?', 'A spring inside stretches more when a heavier object hangs on it', [('It heats up the object', 'It uses a spring.'), ('It counts the object\'s atoms', 'It measures force with a spring.')], o='O2'),
 MC('Which instrument do we use to measure mass?', 'A balance or kitchen scales', [('A forcemeter', 'A forcemeter measures weight.'), ('A stopwatch', 'A stopwatch measures time.')], o='O2'),
 MC('A forcemeter reads 3 N. About what is the mass of the object?', 'About 300 g', [('About 3 g', 'Every 100 g weighs about 1 N.'), ('About 30 kg', 'Far too heavy.')], o='O2'),
 MC('What pattern links mass and weight?', 'The more mass an object has, the more it weighs', [('Heavier objects have less mass', 'It is the other way round.'), ('There is no pattern', 'Weight goes up with mass.')], o='O2'),
 CZ('Complete the sentences.', 'Mass is measured in {0}. Weight is a force, so it is measured in {1}.', [['kilograms', 'kg', 'grams'], ['newtons', 'N']], o='O1'),
 TK('Tick whether each statement is true or false.', ['True', 'False'], [('your mass is the same on the Moon', ['✓', '✗']), ('your weight is the same on the Moon', ['✗', '✓']), ('weight is a force', ['✓', '✗']), ('mass is measured in newtons', ['✗', '✓'])], o='O1'),
 MC('Sam says "My weight is 40 kilograms." What should a scientist say?', 'My mass is 40 kg; my weight is about 400 N', [('That is perfectly correct', 'Kilograms are for mass.'), ('My weight is 4 N', 'Multiply by 10, not divide.')], o='O1', d='H'),
 MC('Which way does gravity pull you?', 'Down, towards the centre of the Earth', [('Up, towards the sky', 'Gravity pulls down.'), ('Sideways', 'It pulls towards the Earth\'s centre.')], o='O1'),
 MC('An apple has a mass of about 100 g. What does it weigh?', 'About 1 N', [('About 10 N', 'That would be 1 kg.'), ('About 100 N', 'That would be 10 kg.')], o='O2'),
)
s.adv(
 GR('Plot the mass and weight results.', {'label': 'Mass (g)', 'min': 0, 'max': 500, 'step': 100}, {'label': 'Weight (N)', 'min': 0, 'max': 6, 'step': 1}, [[0, 0], [100, 1], [200, 2], [300, 3], [400, 4], [500, 5]], o='O2', d='H', table_rows=[[0, 0], [100, 1], [200, 2], [300, 3], [400, 4], [500, 5]]),
 S('An astronaut weighs 600 N on Earth. Gravity on the Moon is one sixth as strong. What does she weigh on the Moon (in N)?', ['100', '100 N', '100N'], o='O1', d='H', reason='600 ÷ 6 = 100 N.'),
 EX('Explain why your mass stays the same on the Moon but your weight changes.', [('mass is the amount of matter, which does not change', ['matter', 'stuff', 'same']), ('weight is the pull of gravity', ['gravity', 'pull']), ('gravity is weaker on the Moon', ['weaker', 'less', 'smaller'])], 'Mass is the amount of matter in you, which does not change. Weight is the pull of gravity, and gravity on the Moon is weaker, so you weigh less.', o='O1', d='H'),
 MC('On a big planet, gravity is 2.5 times as strong as on Earth. What would a 1 kg bag weigh there?', 'About 25 N', [('About 10 N', 'That is on Earth.'), ('About 2.5 N', 'Multiply 10 N by 2.5.')], o='O1', d='VH'),
)
s.labs('Forcemeter lab',
 {'kind': 'test', 'title': 'Weigh objects with a forcemeter', 'intro': 'Hang each object on the forcemeter. Read the scale to find its weight in newtons.',
  'change': 'The object', 'measure': 'Weight', 'unit': 'N', 'max': 10, 'step': 1, 'instr': '⚖️',
  'conds': [{'k': 'apple', 't': 'Apple (100 g)', 'emoji': '🍎', 'val': 1}, {'k': 'book', 't': 'Book (300 g)', 'emoji': '📘', 'val': 3}, {'k': 'shoe', 't': 'Shoe (500 g)', 'emoji': '👟', 'val': 5}, {'k': 'bottle', 't': 'Bottle of water (1 kg)', 'emoji': '🧴', 'val': 10}],
  'qs': [MC('What pattern did you find?', 'Every 100 g weighs about 1 N', [('Every 100 g weighs about 10 N', 'Look at the apple: 100 g weighs 1 N.'), ('Heavier objects weigh less', 'Weight goes up with mass.')], o='O2'),
         MC('Predict the weight of a 700 g bag.', 'About 7 N', [('About 70 N', 'Every 100 g is 1 N.'), ('About 0.7 N', 'Every 100 g is 1 N.')], o='O2')]},
 {'title': 'Kitchen scales challenge', 'intro': 'Weigh objects on kitchen scales, then work out their weight in newtons.',
  'need': ['kitchen scales', '3 objects from home (e.g. a fruit, a book, a shoe)'],
  'safety': ['Ask an adult before using the scales.', 'Do not use anything sharp or breakable.'],
  'steps': ['Put the first object on the scales and read its mass in grams.', 'Work out its weight: divide the grams by 100 to get newtons.', 'Repeat for two more objects.', 'Write your results in the table.'],
  'record': {'head': ['Object', 'Mass (g)', 'Weight (N)'], 'rows': [['Object 1', {'min': 1, 'max': 10000}, {'min': 0, 'max': 100}], ['Object 2', {'min': 1, 'max': 10000}, {'min': 0, 'max': 100}], ['Object 3', {'min': 1, 'max': 10000}, {'min': 0, 'max': 100}]], 'hint': 'Weight in N is about the mass in grams ÷ 100.'},
  'qs': [MC('An object has a mass of 250 g. About what does it weigh?', 'About 2.5 N', [('About 25 N', 'Divide 250 by 100.'), ('About 250 N', 'Divide by 100.')], o='O2')]})

# =====================================================================================  5.2
s = U.section('5.2', 'The effects of forces', ['O3']); s.words(V['5.2']); core(s, 'O3', 'O3')
s.stop(MC('What happens to a still object when the forces on it are balanced?', 'It stays still', [('It starts to move', 'Balanced forces cause no change.'), ('It speeds up', 'That needs unbalanced forces.'), ('It changes shape', 'Not if the forces are balanced and it is still.')], o='O3'),
       MC('In a tug of war, the rope starts to move to the left. What does this tell you?', 'The forces are unbalanced – the left team pulls harder', [('The forces are balanced', 'Then the rope would stay still.'), ('Nobody is pulling', 'Something made it move.')], o='O3'))
s.stop(MC('Why does a parachute fall slowly?', 'Its big surface makes lots of air resistance', [('It has no weight', 'It still has weight.'), ('Gravity does not pull parachutes', 'Gravity pulls everything.'), ('Friction with the ground', 'It is in the air.')], o='O3'),
       MC('Which force slows down a swimmer?', 'Water resistance', [('Air resistance', 'The swimmer is moving through water.'), ('Gravity only', 'Water resistance pushes against the swimmer.')], o='O3'))
s.prac(
 MC('What is a force?', 'A push or a pull', [('A type of energy drink', 'It is a push or a pull.'), ('Only something that makes things fall', 'Forces push and pull in all directions.')], o='O3'),
 MS('Select what forces can do.', ['make things start moving', 'speed things up', 'slow things down', 'change the shape of things'], ['change an object\'s colour'], o='O3'),
 MC('How do we show a bigger force in a force diagram?', 'With a longer arrow', [('With a thinner arrow', 'Length shows size.'), ('With a red arrow', 'Colour does not show size.')], o='O3'),
 MC('What does the direction of a force arrow show?', 'The direction the force acts', [('How long the force lasts', 'Direction shows which way it acts.'), ('The colour of the object', 'It shows direction.')], o='O3'),
 MC('What does "balanced forces" mean?', 'Forces that are equal in size and act in opposite directions', [('Forces that all point the same way', 'Balanced forces are opposite.'), ('Very small forces', 'Size does not matter – they must be equal.')], o='O3'),
 GD('Are the forces balanced or unbalanced?', 'Forces', [('a book resting on a table', 'balanced'), ('a ball speeding up down a hill', 'unbalanced'), ('a car slowing down', 'unbalanced'), ('a lamp hanging still from the ceiling', 'balanced')], o='O3'),
 MC('What is friction?', 'A force between two surfaces that rub together', [('A push from the wind', 'That is air resistance.'), ('The pull of the Earth', 'That is gravity.')], o='O3'),
 MC('Which surface gives the MOST friction?', 'Sandpaper', [('Ice', 'Ice is very smooth.'), ('Polished wood', 'Smooth surfaces give less friction.')], o='O3'),
 MT('Match each force to an example.', [('friction', 'brakes slowing a bicycle'), ('air resistance', 'a parachute falling slowly'), ('water resistance', 'a boat slowing in water'), ('gravity', 'an apple falling')], o='O3'),
 MC('Why do fish have smooth, streamlined shapes?', 'To reduce water resistance', [('To increase friction', 'Fish want to move easily.'), ('To float higher', 'It is about moving through water.')], o='O3'),
 MC('Why do shoes have patterns on their soles?', 'To increase friction so we do not slip', [('To reduce friction', 'We need grip.'), ('To make them lighter', 'It is about grip.')], o='O3'),
 MC('Friction is not always useful. When is it a problem?', 'It wears out the moving parts of a machine', [('It helps us walk', 'That is useful.'), ('It helps brakes work', 'That is useful.')], o='O3', d='H'),
 MC('In the ramp test, what did we CHANGE?', 'The surface at the bottom of the ramp', [('The height of the ramp', 'That stayed the same.'), ('The toy car', 'We used the same car.')], o='O3'),
 MC('In the ramp test, what did we MEASURE?', 'How far the car rolled', [('The colour of the surface', 'That was not measured.'), ('The mass of the car', 'That was not measured.')], o='O3'),
 TB('The car rolled 120 cm on wood, 60 cm on carpet and 30 cm on sandpaper. How much further did it roll on wood than on sandpaper?', ['Surface', 'Distance (cm)'], [['wood', '120'], ['sandpaper', '30'], ['difference', B(90)]], o='O3', skill='Data', reason='120 − 30 = 90 cm.'),
 MC('What is the conclusion of the ramp test?', 'The rougher the surface, the more friction and the shorter the distance', [('Rough surfaces make the car go further', 'They slow it down.'), ('The surface makes no difference', 'The distances were very different.')], o='O3'),
 MC('A cyclist stops pedalling. What slows her down?', 'Friction and air resistance', [('Gravity pushing her forwards', 'Gravity pulls down.'), ('Nothing – she keeps going for ever', 'Forces slow her down.')], o='O3'),
 OD('Order these from LEAST to MOST air resistance.', ['a small pebble', 'a sheet of paper falling flat', 'an open parachute'], o='O3', d='H'),
)
s.adv(
 EX('A box is pushed across a floor and moves at a steady speed. Explain the forces.', [('the push is balanced by friction', ['friction', 'balanced']), ('equal and opposite', ['equal', 'opposite', 'same size']), ('so the speed does not change', ['steady', 'same speed', 'not change'])], 'The push forward is balanced by friction backwards. The forces are equal and opposite, so the speed does not change.', o='O3', d='H'),
 GR('Plot the ramp results.', {'label': 'Surface (1 = wood, 2 = carpet, 3 = sandpaper)', 'min': 0, 'max': 4, 'step': 1}, {'label': 'Distance rolled (cm)', 'min': 0, 'max': 140, 'step': 20}, [[1, 120], [2, 60], [3, 30]], o='O3', d='H', table_rows=[[1, 120], [2, 60], [3, 30]]),
 MC('Two teams pull with 300 N and 250 N. What happens?', 'The rope moves towards the 300 N team', [('Nothing – the forces are balanced', '300 N and 250 N are not equal.'), ('The rope moves towards the 250 N team', 'It moves towards the bigger force.')], o='O3', d='H'),
 MC('Why do skydivers spread their arms and legs?', 'To increase air resistance and fall more slowly', [('To fall faster', 'Spreading out increases air resistance.'), ('To reduce gravity', 'Gravity stays the same.')], o='O3', d='VH'),
)
s.labs('Ramp lab',
 {'kind': 'test', 'title': 'How does the surface change how far the car rolls?', 'intro': 'A toy car is let go from the same point on the same ramp. Read the measuring tape to see how far it rolls on each surface.',
  'change': 'The surface', 'measure': 'Distance rolled', 'unit': 'cm', 'max': 140, 'step': 10, 'instr': '🚗',
  'conds': [{'k': 'wood', 't': 'Smooth wood', 'emoji': '🪵', 'val': 120}, {'k': 'carpet', 't': 'Carpet', 'emoji': '🟥', 'val': 60}, {'k': 'sand', 't': 'Sandpaper', 'emoji': '🟫', 'val': 30}],
  'qs': [MC('On which surface did the car roll furthest?', 'Smooth wood', [('Sandpaper', 'Sandpaper gave the most friction.'), ('Carpet', 'Wood was further.')], o='O3'),
         MC('Why did the car roll the shortest distance on sandpaper?', 'Sandpaper is rough, so there is more friction', [('Sandpaper is smooth', 'It is rough.'), ('Gravity is stronger on sandpaper', 'Gravity is the same.')], o='O3'),
         MC('Which thing did you keep the SAME?', 'The ramp and the starting point', [('The surface', 'That was what you changed.'), ('The distance', 'That was what you measured.')], o='O3')]},
 {'title': 'Book ramp test', 'intro': 'Test how far a toy car rolls on different floors.',
  'need': ['a toy car', 'a tray or board and 3 books to make a ramp', 'a tape measure', 'different floors or cloths (e.g. a towel, a rug, a smooth floor)'],
  'safety': ['Keep the area clear so nobody trips.', 'Do not stand on the ramp.'],
  'steps': ['Make a ramp with the board and books.', 'Let the car go from the top – do not push it.', 'Measure how far it rolls from the bottom of the ramp.', 'Change only the floor surface and repeat.'],
  'record': {'head': ['Surface', 'Distance rolled (cm)'], 'rows': [['Smooth floor', {'min': 1, 'max': 1000}], ['Rug or carpet', {'min': 1, 'max': 1000}], ['Towel', {'min': 1, 'max': 1000}]], 'hint': 'Distances are usually between 10 and 300 cm.'},
  'qs': [MC('Why must you let the car go without pushing it?', 'To keep the test fair', [('Pushing breaks the car', 'It is about fairness.'), ('Cars do not roll if pushed', 'They do – but it changes the result.')], o='O3')]})

# =====================================================================================  5.3
s = U.section('5.3', 'Floating and sinking', ['O4', 'O5']); s.words(V['5.3']); core(s, 'O4', 'O4')
s.stop(MC('What is the name of the upward push of water?', 'Upthrust', [('Gravity', 'Gravity pulls down.'), ('Friction', 'Friction acts between surfaces.'), ('Weight', 'Weight pulls down.')], o='O4'),
       MC('A cork floats. Compare its weight and the upthrust.', 'The upthrust is as big as its weight', [('Its weight is bigger than the upthrust', 'Then it would sink.'), ('There is no upthrust', 'Water always pushes up.')], o='O4'))
s.stop(MC('Why does clay float when it is made into a boat shape?', 'The boat shape displaces more water, so the upthrust is bigger', [('The clay gets lighter', 'Its weight is the same.'), ('The clay turns into wood', 'It is still clay.'), ('Boats have no weight', 'They do have weight.')], o='O4'),
       MC('How can a huge steel ship float?', 'Its shape displaces a lot of water, giving a big upthrust', [('Steel is lighter than water', 'A lump of steel sinks.'), ('Ships are full of water', 'They are full of air.')], o='O4'))
s.prac(
 MC('Which two forces act on an object in water?', 'Weight (down) and upthrust (up)', [('Friction and air resistance', 'In water, the main forces are weight and upthrust.'), ('Only gravity', 'The water pushes up too.')], o='O4'),
 GD('Does each object float or sink in water?', 'In water', [('cork', 'floats'), ('coin', 'sinks'), ('wooden spoon', 'floats'), ('stone', 'sinks'), ('apple', 'floats')], o='O4'),
 MC('An object sinks. What does this tell us?', 'Its weight is bigger than the upthrust', [('The upthrust is bigger than its weight', 'Then it would float.'), ('It has no weight', 'It sinks because of its weight.')], o='O4'),
 MC('What does "displace" mean?', 'To push something out of the way', [('To float on top', 'That is floating.'), ('To fill with air', 'It means push aside.')], o='O4'),
 MC('Why does the water level in a bath rise when you get in?', 'Your body displaces (pushes aside) some water', [('You add water to it', 'You do not add water.'), ('The water gets warmer', 'That is not the reason.')], o='O4'),
 MC('The more water an object displaces, the…', 'bigger the upthrust', [('smaller the upthrust', 'It is the other way round.'), ('heavier the object', 'Weight does not change.')], o='O4'),
 CZ('Complete the sentences.', 'Weight pulls an object {0}. Upthrust pushes it {1}. If they are equal, the object {2}.', [['down', 'downwards'], ['up', 'upwards'], ['floats']], o='O4'),
 MC('A ball of foil sinks, but the same foil shaped as a flat tray floats. What changed?', 'Its shape – the tray displaces more water', [('Its mass', 'Same foil, same mass.'), ('The water', 'Same water.')], o='O4'),
 MC('Why do people wear life jackets in boats?', 'They are full of air or foam, which helps them float', [('They make people heavier', 'They help us float.'), ('They are warm', 'Their main job is floating.')], o='O4'),
 MC('In the boat test, what did we CHANGE?', 'The base area of the boat', [('The type of foil', 'The same foil was used.'), ('The number of marbles', 'That was what we measured.')], o='O5'),
 MC('In the boat test, what did we MEASURE?', 'How many marbles each boat held before it sank', [('The colour of the boats', 'That was not measured.'), ('The temperature of the water', 'That was not measured.')], o='O5'),
 MS('Which must stay the SAME to make the boat test fair?', ['the type and amount of foil', 'the size of the marbles', 'the water'], ['the base area of the boat'], o='O5'),
 MC('What kind of graph did we use for the boat results?', 'A scatter graph', [('A pie chart', 'We plotted points for two numbers.'), ('A pictogram', 'We used points on a scatter graph.')], o='O5'),
 TB('Read the scatter graph from the video and complete the table.', ['Base area (cm²)', 'Marbles held'], [['25', '4'], ['50', B(9)], ['75', '13'], ['100', B(18)]], o='O5', skill='Data'),
 MC('What pattern does the scatter graph show?', 'The bigger the base, the more marbles the boat holds', [('The bigger the base, the fewer marbles', 'The points go up.'), ('No pattern', 'The points go up from left to right.')], o='O5'),
 MC('Predict how many marbles a boat with a 125 cm² base might hold.', 'About 22', [('About 5', 'That is like the smallest boat.'), ('About 50', 'That is far too many – follow the pattern.')], o='O5', d='H'),
 MC('Why does a wider boat hold more marbles?', 'It displaces more water, so it gets more upthrust', [('It weighs much more', 'Same foil, same weight.'), ('Marbles like wide boats', 'It is about upthrust.')], o='O5'),
 MC('What is the best way to make your results more reliable?', 'Repeat each test and look for odd results', [('Do each test only once', 'Repeats make results more reliable.'), ('Change two things at once', 'That is not a fair test.')], o='O5'),
)
s.adv(
 GR('Plot the boat results on a scatter graph.', {'label': 'Base area (cm²)', 'min': 0, 'max': 125, 'step': 25}, {'label': 'Marbles held', 'min': 0, 'max': 25, 'step': 5}, [[25, 4], [50, 9], [75, 13], [100, 18], [125, 22]], o='O5', d='H', table_rows=[[25, 4], [50, 9], [75, 13], [100, 18], [125, 22]]),
 EX('Explain why a ball of clay sinks but a clay boat floats.', [('the ball displaces only a little water', ['little', 'small', 'less']), ('the boat displaces more water', ['more water', 'displace']), ('so the upthrust is big enough to balance the weight', ['upthrust', 'balance', 'equal'])], 'The ball displaces only a little water, so the upthrust is smaller than its weight. The boat shape displaces much more water, so the upthrust is big enough to balance the weight.', o='O4', d='H'),
 MC('One boat result was 3 marbles for 100 cm², when others with 100 cm² held 18. What should Lin do?', 'Repeat that test – it is an odd result', [('Use it – all results are right', 'It does not fit the pattern.'), ('Stop the investigation', 'Repeat the odd test.')], o='O5', d='H'),
 MC('A ship floats lower in the water after loading cargo. Why?', 'Its weight is bigger, so it must displace more water to get enough upthrust', [('Water gets heavier', 'The water is the same.'), ('Upthrust stops working', 'Upthrust increases as it sinks lower.')], o='O4', d='VH'),
)
s.labs('Boat lab',
 {'kind': 'test', 'title': 'Which boat holds the most marbles?', 'intro': 'Foil boats with different base areas are loaded with marbles one at a time. Read the counter to see how many each boat held before it sank.',
  'change': 'The base area of the boat', 'measure': 'Marbles held', 'unit': 'marbles', 'max': 20, 'step': 2, 'instr': '⛵',
  'conds': [{'k': 'b25', 't': '25 cm² base', 'emoji': '⛵', 'val': 4}, {'k': 'b50', 't': '50 cm² base', 'emoji': '🚤', 'val': 9}, {'k': 'b75', 't': '75 cm² base', 'emoji': '🛥️', 'val': 13}, {'k': 'b100', 't': '100 cm² base', 'emoji': '🚢', 'val': 18}],
  'qs': [MC('What happened as the base area got bigger?', 'The boat held more marbles', [('It held fewer marbles', 'Look at your bars.'), ('Nothing changed', 'The numbers went up.')], o='O5'),
         MC('Why did the big boat hold the most?', 'It displaced the most water, so it had the biggest upthrust', [('It was the lightest', 'All were made of the same foil.'), ('The marbles were smaller', 'The marbles were the same.')], o='O4')]},
 {'title': 'Foil boat challenge', 'intro': 'Design two foil boats and test how many coins each holds.',
  'need': ['2 pieces of kitchen foil the same size', 'a bowl or sink of water', 'lots of small coins (all the same)', 'a ruler'],
  'safety': ['Wipe up spills so nobody slips.', 'Wash your hands after handling coins.'],
  'steps': ['Make one boat with a small base and one with a large base, using the same size of foil.', 'Measure the length and width of each base.', 'Float a boat and add coins one at a time until it sinks.', 'Record the number of coins it held before sinking, then test the other boat.'],
  'record': {'head': ['Boat', 'Coins held before sinking'], 'rows': [['Small base', {'min': 0, 'max': 500}], ['Large base', {'min': 0, 'max': 500}]], 'hint': 'Count the coins that stayed afloat.'},
  'qs': [MC('Which boat usually holds more coins?', 'The one with the larger base', [('The one with the smaller base', 'A wider base displaces more water.'), ('They always hold the same', 'Shape changes upthrust.')], o='O5')]})

# =====================================================================================  5.4
s = U.section('5.4', 'Different circuits and circuit diagrams', ['O6', 'O7']); s.words(V['5.4']); core(s, 'O6', 'O6')
s.stop(MC('What do we call a drawing of a circuit made with symbols?', 'A circuit diagram', [('A food web', 'That shows what eats what.'), ('A map', 'A map shows places.'), ('A bar chart', 'A bar chart shows data.')], o='O6'),
       MC('Why do scientists use circuit symbols?', 'They are simple and everyone understands them', [('They look like real photos', 'Symbols are simple drawings.'), ('They make circuits work', 'They only show the circuit.')], o='O6'))
s.stop(MC('In which type of circuit do the other lamps stay on if one lamp breaks?', 'A parallel circuit', [('A series circuit', 'In series, one break turns everything off.'), ('Both types', 'Only parallel circuits.'), ('Neither type', 'Parallel circuits keep the others on.')], o='O6'),
       MC('Why are the lights in your home wired in parallel?', 'So one broken bulb does not turn off all the lights', [('To make all the lights dimmer', 'Parallel keeps lamps bright.'), ('Because it uses fewer wires', 'Parallel uses more wires.')], o='O6'))
s.prac(
 MC('When will a lamp in a circuit light?', 'When the circuit is a complete loop with no gaps', [('When there is a gap in the circuit', 'A gap breaks the circuit.'), ('Only in the daytime', 'Circuits work at any time.')], o='O6'),
 MT('Match each component to its job.', [('cell', 'pushes electricity around the circuit'), ('lamp', 'gives out light'), ('switch', 'opens and closes the circuit'), ('wire', 'connects the components')], o='O6'),
 MC('What is a battery?', 'Two or more cells joined together', [('A single lamp', 'A battery is cells joined.'), ('A kind of switch', 'A battery gives the push.')], o='O6'),
 MC('What is a series circuit?', 'A circuit with all the components in one single loop', [('A circuit with separate loops', 'That is parallel.'), ('A circuit with no cell', 'A circuit needs a cell.')], o='O6'),
 MC('What is a parallel circuit?', 'A circuit where each lamp has its own loop back to the cell', [('A circuit with one loop', 'That is series.'), ('A broken circuit', 'Parallel circuits work.')], o='O6'),
 GD('Is each statement about a series circuit or a parallel circuit?', 'Circuit', [('one single loop', 'series'), ('each lamp has its own loop', 'parallel'), ('if one lamp breaks, the other goes out', 'series'), ('lamps stay bright when you add more', 'parallel')], o='O6'),
 MC('A second lamp is added in series. What happens to the brightness?', 'Both lamps are dimmer', [('Both lamps are brighter', 'In series they share the push.'), ('Only the new lamp lights', 'Both light, but dimmer.')], o='O6'),
 MC('What happens when you open a switch in a series circuit?', 'The circuit is broken and the lamps go out', [('The lamps get brighter', 'An open switch makes a gap.'), ('Nothing happens', 'The circuit is broken.')], o='O6'),
 TK('Tick the circuits in which the lamp will light.', ['Lights', 'Does not light'], [('a complete loop with a cell and a lamp', ['✓', '✗']), ('a loop with a gap in one wire', ['✗', '✓']), ('a loop with a closed switch', ['✓', '✗']), ('a loop with an open switch', ['✗', '✓'])], o='O6'),
 MC('What is voltage?', 'The push of a cell, measured in volts', [('The brightness of a lamp', 'Voltage is the push.'), ('The length of the wire', 'Voltage is not length.')], o='O7'),
 MC('What happens to a lamp when you add more cells?', 'It gets brighter', [('It gets dimmer', 'More cells give more push.'), ('It stays the same', 'More voltage makes it brighter.')], o='O7'),
 MC('Why should you not add too many cells to a small lamp?', 'Too many volts can make the lamp blow', [('The cells will get cold', 'That is not the danger.'), ('The circuit will be quieter', 'It is about too much voltage.')], o='O7'),
 MC('Why must you never use mains electricity for experiments?', 'Mains electricity is very dangerous and can kill', [('It does not work', 'It works – but it is dangerous.'), ('It is too weak', 'It is far too strong.')], o='O7'),
 TB('Each cell gives 1.5 V. Complete the table.', ['Number of cells', 'Voltage (V)'], [['1', '1.5'], ['2', B(3)], ['3', B(4.5)]], o='O7', skill='Data', reason='Add 1.5 V for each cell.'),
 MS('Select the safe ways to use electricity.', ['use cells for experiments', 'keep electrical things away from water', 'ask an adult before using plugs'], ['poke things into sockets', 'touch bare wires'], o='O7'),
 OD('Put these in order of brightness, from dimmest to brightest (same lamp).', ['1 cell', '2 cells', '3 cells'], o='O7'),
 MC('In the cell investigation, what did we CHANGE?', 'The number of cells', [('The lamp', 'We used the same lamp.'), ('The brightness', 'That was what we observed.')], o='O7'),
 MC('A circuit has a cell, a switch and two lamps in parallel. One lamp breaks. What happens?', 'The other lamp stays on', [('Both lamps go out', 'That happens in series.'), ('The switch opens', 'The switch is not affected.')], o='O6', d='H'),
)
s.adv(
 EX('Explain why the lights in a house are wired in parallel and not in series.', [('in parallel each lamp has its own loop', ['own loop', 'separate']), ('if one breaks the others stay on', ['stay on', 'others', 'still work']), ('lamps stay bright', ['bright'])], 'In parallel each lamp has its own loop, so if one breaks the others stay on, and the lamps all stay bright.', o='O6', d='H'),
 MC('A series circuit has two lamps and one cell. How could you make the lamps brighter?', 'Add another cell', [('Add another lamp in series', 'That makes them dimmer.'), ('Use longer wires', 'That does not make them brighter.')], o='O7', d='H'),
 GR('Plot how brightness changes with the number of cells (brightness units from a light meter).', {'label': 'Number of cells', 'min': 0, 'max': 3, 'step': 1}, {'label': 'Brightness (units)', 'min': 0, 'max': 60, 'step': 10}, [[0, 0], [1, 15], [2, 32], [3, 50]], o='O7', d='H', table_rows=[[0, 0], [1, 15], [2, 32], [3, 50]]),
 MC('A circuit diagram shows a cell, an open switch and a lamp in series. Why is the lamp off?', 'The open switch makes a gap, so the circuit is not complete', [('There are too many cells', 'There is only one cell.'), ('The lamp is in parallel', 'It is in series.')], o='O6', d='VH'),
)
s.labs('Circuit lab',
 {'kind': 'sort', 'title': 'Series or parallel?', 'intro': 'Sort each card: does it describe a series circuit or a parallel circuit?',
  'groups': ['Series circuit', 'Parallel circuit'],
  'items': [{'t': 'one single loop', 'emoji': '➰', 'g': 0, 'why': 'A series circuit has one loop.'}, {'t': 'each lamp has its own loop', 'emoji': '🔀', 'g': 1, 'why': 'That is a parallel circuit.'},
            {'t': 'one lamp breaks, all go out', 'emoji': '💥', 'g': 0, 'why': 'In series, one break opens the loop.'}, {'t': 'one lamp breaks, others stay on', 'emoji': '💡', 'g': 1, 'why': 'Parallel loops are separate.'},
            {'t': 'adding lamps makes them dimmer', 'emoji': '🔅', 'g': 0, 'why': 'In series the lamps share the push.'}, {'t': 'lamps stay bright when you add more', 'emoji': '🔆', 'g': 1, 'why': 'Each loop gets the full push.'},
            {'t': 'the lights in a house', 'emoji': '🏠', 'g': 1, 'why': 'Homes are wired in parallel.'}],
  'qs': [MC('Which circuit would you choose for a string of party lights, so one broken bulb does not turn them all off?', 'Parallel', [('Series', 'In series one break turns them all off.'), ('Either', 'Only parallel keeps the others on.')], o='O6'),
         MC('What does the symbol for a cell show?', 'A long line and a short line', [('A circle with a cross', 'That is a lamp.'), ('A wavy line', 'That is not the cell symbol.')], o='O6', d='H')]},
 {'title': 'Battery detective', 'intro': 'Look at battery-powered things at home (with an adult) and find out how many cells each uses.',
  'need': ['3 things that use batteries, e.g. a torch, a TV remote, a toy', 'an adult to help open the battery covers'],
  'safety': ['Never open anything that plugs into the mains.', 'Do not take apart batteries or put them in your mouth.'],
  'steps': ['Ask an adult to open the battery cover of each object.', 'Count the cells inside, and read the voltage printed on one cell (often 1.5 V).', 'Work out the total voltage: number of cells × voltage of one cell.', 'Put the cells back the right way round.'],
  'record': {'head': ['Object', 'Number of cells', 'Total voltage (V)'], 'rows': [['Object 1', {'min': 1, 'max': 12}, {'min': 1, 'max': 24}], ['Object 2', {'min': 1, 'max': 12}, {'min': 1, 'max': 24}], ['Object 3', {'min': 1, 'max': 12}, {'min': 1, 'max': 24}]], 'hint': 'Most cells are 1.5 V, so 2 cells give 3 V.'},
  'qs': [MC('A torch has 3 cells of 1.5 V. What is its total voltage?', '4.5 V', [('1.5 V', 'That is one cell.'), ('3 V', 'That is two cells.')], o='O7')]})

U.mindmap(('Mass and weight', 'Mass in kg; weight is gravity\'s pull in N.', 'O1', '5.1'), ('Forcemeters', '100 g weighs about 1 N.', 'O2', '5.1'),
          ('Forces', 'Balanced or unbalanced; friction and air resistance.', 'O3', '5.2'), ('Floating', 'Weight down, upthrust up; displacement.', 'O4', '5.3'),
          ('Boat designs', 'Bigger base, more upthrust, more marbles.', 'O5', '5.3'), ('Circuits', 'Symbols; series and parallel.', 'O6', '5.4'), ('Voltage', 'More cells, brighter lamps; stay safe.', 'O7', '5.4'))
