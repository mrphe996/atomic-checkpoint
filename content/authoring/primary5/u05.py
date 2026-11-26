# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 5 · Unit 5 Forces and magnetism. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit5 import *

OBJ = {
 'O1': {'sec': '5.1', 'code': 'Physics', 'codeNote': '', 't': 'Describe gravity, normal forces and applied forces, and measure forces in newtons.'},
 'O2': {'sec': '5.2', 'code': 'Earth and space', 'codeNote': '', 't': 'Explain that gravity keeps the Moon and artificial satellites in orbit.'},
 'O3': {'sec': '5.3', 'code': 'Physics', 'codeNote': '', 't': 'Describe friction, air resistance, water resistance and upthrust.'},
 'O4': {'sec': '5.4', 'code': 'Physics', 'codeNote': '', 't': 'Describe balanced and unbalanced forces and their effects on movement.'},
 'O5': {'sec': '5.5', 'code': 'Physics', 'codeNote': '', 't': 'Sort materials into magnetic and non-magnetic, and know that most metals are not magnetic.'},
 'O6': {'sec': '5.6', 'code': 'Physics', 'codeNote': '', 't': 'Describe magnetic poles, attraction and repulsion, and magnetic fields; compare magnet strength fairly.'},
}
U = Unit(5, 'Forces and magnetism', 'Physics: forces', 'Gravity, satellites, friction, balanced forces and magnets that attract and repel.', OBJ)

# =====================================================================================  5.1
s = U.section('5.1', 'Gravity, normal forces and applied forces', ['O1']); s.words(V['5.1']); core(s, 'O1', 'O1')
s.stop(MC('What is the push of a surface on an object called?', 'The normal force', [('Gravity', 'Gravity pulls down.'), ('Friction', 'Friction acts along surfaces.'), ('Air resistance', 'That acts in air.')], o='O1'),
       MC('Why don\'t you sink through the floor?', 'The floor pushes up on you with a normal force', [('Gravity switches off indoors', 'Gravity is always on.'), ('You are too light', 'The floor pushes back.')], o='O1'))
s.stop(MC('Which way does gravity pull?', 'Down, towards the centre of the Earth', [('Up, towards the sky', 'Things fall down.'), ('Sideways', 'It pulls towards the Earth\'s centre.')], o='O1'),
       MC('What is the pull of gravity on an object called?', 'Its weight', [('Its mass', 'Mass is the amount of matter.'), ('Its speed', 'Weight is the pull of gravity.')], o='O1'))
s.prac(
 GD('Is each force gravity, a normal force or an applied force?', 'Force', [('an apple falling from a tree', 'gravity'), ('a table holding up a book', 'normal force'), ('pushing a shopping trolley', 'applied force'), ('pulling a door open', 'applied force')], o='O1'),
 MC('What unit are forces measured in?', 'Newtons (N)', [('Kilograms (kg)', 'That is for mass.'), ('Metres (m)', 'That is for length.')], o='O1'),
 MC('What do we use to measure a force?', 'A forcemeter', [('A thermometer', 'That measures temperature.'), ('A ruler', 'That measures length.')], o='O1'),
 MC('What does a longer force arrow show?', 'A bigger force', [('A slower object', 'Arrow length shows force size.'), ('A heavier arrow', 'It shows force size.')], o='O1'),
 MC('Why does a kicked ball always come back down?', 'Gravity pulls it towards the Earth', [('The air pushes it down', 'Gravity does it.'), ('It runs out of energy and stops in the air', 'Gravity pulls it down.')], o='O1'),
 MS('Select the applied forces.', ['lifting a box', 'kicking a ball', 'squeezing a sponge'], ['an apple falling', 'a chair holding you up'], o='O1'),
 CZ('Complete the sentences.', 'Gravity pulls things {0}. A surface pushes back with a {1} force. Forces are measured in {2}.', [['down', 'downwards'], ['normal'], ['newtons', 'N']], o='O1'),
 MC('A book rests on a table. Which two forces act on it?', 'Gravity down and the normal force up', [('Only gravity', 'The table pushes back.'), ('Friction and air resistance', 'It is not moving.')], o='O1'),
 MC('How does a forcemeter work?', 'A spring inside stretches when a force pulls on it', [('It weighs the air', 'It has a spring.'), ('It uses magnets to guess', 'It uses a spring.')], o='O1'),
 TB('Forcemeter readings. Which object needed the biggest force? Complete the ranks (1 = biggest).', ['Object', 'Force (N)', 'Rank'], [['school bag', '20', B(1)], ['book', '5', B(2)], ['shoe', '4', B(3)], ['pencil case', '2', B(4)]], o='O1', skill='Data'),
 MC('Why should you lift heavy boxes by bending your knees?', 'To protect your back', [('To make the box lighter', 'It protects your back.'), ('To increase gravity', 'Gravity does not change.')], o='O1'),
 MC('What is the most "attractive" thing on Earth (the riddle)?', 'Gravity', [('A magnet', 'Gravity pulls on everything.'), ('A flower', 'It is a riddle about gravity.')], o='O1'),
 OD('Order these from smallest to biggest weight.', ['pencil (1 N)', 'apple (2 N)', 'book (5 N)', 'bag (20 N)'], o='O1'),
 MC('Does gravity pull on the Moon?', 'Yes – the Earth\'s gravity pulls on the Moon', [('No – there is no gravity in space', 'Gravity works across space.'), ('Only at night', 'Gravity is always there.')], o='O1', d='H'),
)
s.adv(
 EX('Explain why a cup on a table does not move.', [('gravity pulls it down', ['gravity', 'weight']), ('the table pushes it up (normal force)', ['normal', 'table', 'push']), ('the forces are balanced', ['balanced', 'equal'])], 'Gravity pulls the cup down and the table pushes it up with the normal force. The forces are balanced, so the cup does not move.', o='O1', d='H'),
 GR('Plot the forcemeter readings.', {'label': 'Object (1 pencil case, 2 shoe, 3 book, 4 bag)', 'min': 0, 'max': 5, 'step': 1}, {'label': 'Force (N)', 'min': 0, 'max': 24, 'step': 4}, [[1, 2], [2, 4], [3, 5], [4, 20]], o='O1', d='H', table_rows=[[1, 2], [2, 4], [3, 5], [4, 20]]),
 MC('A forcemeter reads 0 N with nothing on it. Why is this important?', 'So the readings start from zero and are correct', [('So it looks tidy', 'It is about accurate readings.'), ('So the spring is broken', 'Zero is the correct start.')], o='O1', d='VH'),
 MC('You stand on bathroom scales. What does the normal force from the scales equal?', 'Your weight', [('Zero', 'The scales push back.'), ('Twice your weight', 'It equals your weight.')], o='O1', d='H'),
)
s.labs('Forcemeter lab',
 test_lab('How much force to lift it?', 'Hook each object onto the forcemeter and lift it slowly. Read the scale in newtons.', 'The object', 'Force', 'N', 24, 2, '⚖️',
  [('Pencil case', '✏️', 2), ('Shoe', '👟', 4), ('Book', '📘', 5), ('School bag', '🎒', 20)],
  [MC('Which object needed the biggest force?', 'The school bag', [('The shoe', 'It needed 4 N.'), ('The pencil case', 'It needed only 2 N.')], o='O1'),
   MC('Which force were you working against when you lifted?', 'Gravity', [('Friction', 'You lifted straight up.'), ('Magnetism', 'Gravity pulls down.')], o='O1')]),
 home('Push and pull hunt', 'Find forces around your home.', ['the table below', 'a pencil'],
  ['Do not push or pull anything heavy without an adult.'],
  ['Walk around your home.', 'Count the pushes you see or make in 10 minutes (e.g. closing a door).', 'Count the pulls (e.g. opening a drawer).', 'Count things held up by a normal force (e.g. a cup on a table).'],
  ['Force', 'Number I found'], [['Pushes', {'min': 0, 'max': 200}], ['Pulls', {'min': 0, 'max': 200}], ['Normal forces', {'min': 0, 'max': 200}]], 'Write a whole number.',
  [MC('Opening a drawer is a…', 'pull (an applied force)', [('push of gravity', 'You pull it towards you.'), ('normal force', 'You apply a pull.')], o='O1')]))

# =====================================================================================  5.2
s = U.section('5.2', 'Gravity and satellites', ['O2']); s.words(V['5.2']); core(s, 'O2', 'O2')
s.stop(MC('What keeps a satellite in its orbit?', 'Gravity pulling it towards the Earth while it moves fast', [('Its engines pushing all the time', 'Gravity does the work.'), ('A long rope', 'There is no rope!'), ('Wind in space', 'There is no wind in space.')], o='O2'),
       MC('Why doesn\'t a satellite fall to the ground?', 'It moves forwards so fast that it keeps falling around the Earth', [('There is no gravity in space', 'Gravity keeps it in orbit.'), ('It is too light', 'Its speed keeps it in orbit.')], o='O2'))
s.stop(MC('What is the Earth\'s natural satellite?', 'The Moon', [('The Sun', 'The Earth orbits the Sun.'), ('The International Space Station', 'That is an artificial satellite.')], o='O2'),
       MC('What is an orbit?', 'The path of an object around another object', [('A type of rocket', 'It is a path.'), ('A planet\'s light', 'It is a path.')], o='O2'))
s.prac(
 GD('Is each satellite natural or artificial?', 'Satellite', [('the Moon', 'natural'), ('the International Space Station', 'artificial'), ('a weather satellite', 'artificial'), ('a moon of Jupiter', 'natural')], o='O2'),
 MS('Select the jobs artificial satellites do.', ['help phones and TV', 'forecast the weather', 'help maps and navigation'], ['make the tides', 'make the Sun shine'], o='O2'),
 MC('What holds the planets in their orbits around the Sun?', 'The Sun\'s gravity', [('The Moon', 'The Sun\'s gravity does.'), ('Magnets', 'It is gravity.')], o='O2'),
 MC('What causes the tides?', 'The Moon\'s gravity pulling on the sea', [('Wind only', 'The Moon\'s gravity causes tides.'), ('Fish swimming', 'It is the Moon\'s pull.')], o='O2'),
 MC('In the ball-on-a-string model, what does the string represent?', 'Gravity', [('The Sun', 'The string pulls like gravity.'), ('The orbit path', 'The pull is the string.')], o='O2'),
 MC('What happens if you let go of the string?', 'The ball flies off in a straight line', [('It keeps going in a circle', 'Without the pull it goes straight.'), ('It falls straight to the centre', 'It flies off.')], o='O2'),
 MC('How many times a day does the International Space Station go around the Earth?', 'About 16', [('About 1', 'It is much faster.'), ('About 365', 'Too many.')], o='O2'),
 CZ('Complete the sentences.', 'A satellite moves in an {0} around a planet. The {1} is the Earth\'s natural satellite. {2} keeps it in orbit.', [['orbit'], ['Moon', 'moon'], ['Gravity', 'gravity']], o='O2'),
 MC('How can you tell a satellite from a plane in the night sky?', 'A satellite moves smoothly and does not flash', [('A satellite flashes red', 'Planes flash.'), ('A satellite is always green', 'It looks like a moving star.')], o='O2'),
 MC('What does an artificial satellite need to get into orbit?', 'A rocket to launch it', [('A balloon', 'It needs a rocket.'), ('A long ladder', 'It needs a rocket.')], o='O2'),
 TK('Tick what is true.', ['True', 'False'], [('the Moon orbits the Earth', ['✓', '✗']), ('there is no gravity in space', ['✗', '✓']), ('weather satellites help forecasts', ['✓', '✗'])], o='O2'),
 OD('Order these from smallest to biggest orbit.', ['a satellite around the Earth', 'the Moon around the Earth', 'the Earth around the Sun'], o='O2', d='H'),
 MC('Astronauts on the ISS see about how many sunrises each day?', 'About 16', [('1', 'They go round 16 times.'), ('None', 'They see many.')], o='O2'),
 MC('Why do astronauts use radios to talk in space?', 'Sound cannot travel through empty space', [('Space is too noisy', 'There is no air for sound.'), ('Radios are fun', 'Sound needs a medium.')], o='O2', d='H'),
)
s.adv(
 EX('Explain why the Moon does not fly off into space or crash into the Earth.', [('the Earth\'s gravity pulls the Moon', ['gravity', 'pull']), ('the Moon is moving forwards fast', ['moving', 'fast', 'speed', 'forward']), ('together these keep it in orbit', ['orbit', 'around'])], 'The Earth\'s gravity pulls the Moon towards it, but the Moon is moving forwards very fast. Together these keep it travelling around the Earth in an orbit.', o='O2', d='H'),
 TB('Satellite spotting results. Find the total.', ['Night', 'Satellites seen in 15 min'], [['Monday', '3'], ['Tuesday', '5'], ['Wednesday', '4'], ['total', B(12)]], o='O2', skill='Data'),
 MC('Why are satellites easier to see just after sunset?', 'They are still lit by the Sun while the sky is dark', [('They switch on their lights', 'They reflect sunlight.'), ('They come closer', 'Their orbits do not change.')], o='O2', d='VH'),
 MC('If the Sun\'s gravity suddenly vanished, what would the Earth do?', 'Move off in a straight line into space', [('Keep orbiting', 'Without gravity it would not orbit.'), ('Fall into the Sun', 'There would be no pull.')], o='O2', d='H'),
)
s.labs('Satellite lab',
 sort_lab('Natural or artificial?', 'Sort each satellite.', ['Natural satellite', 'Artificial satellite'],
  [('the Moon', '🌙', 0, 'The Moon formed naturally.'), ('the International Space Station', '🛰️', 1, 'People built it.'), ('a weather satellite', '🌦️', 1, 'People built it.'),
   ('a GPS satellite for maps', '🗺️', 1, 'People built it.'), ('Titan, a moon of Saturn', '🪐', 0, 'It is a natural moon.'), ('a TV satellite', '📺', 1, 'People built it.')],
  [MC('What keeps all of these satellites in orbit?', 'Gravity', [('Rockets firing all the time', 'Gravity does it.'), ('Magnets', 'It is gravity.')], o='O2'),
   MC('Which satellite helps you find your way with a map app?', 'A GPS satellite', [('The Moon', 'GPS satellites do that.'), ('Titan', 'Titan is far away.')], o='O2')]),
 home('Satellite spotting', 'Look for satellites on a clear evening.', ['a clear evening sky', 'an adult', 'a watch or timer'],
  ['Go outside only with an adult.', 'Never look at the Sun.'],
  ['About an hour after sunset, go outside and let your eyes get used to the dark.', 'Look for a bright dot moving smoothly across the sky.', 'Count how many you see in 15 minutes.', 'Try again on another night.'],
  ['Night', 'Satellites seen in 15 minutes'], [['Night 1', {'min': 0, 'max': 50}], ['Night 2', {'min': 0, 'max': 50}]], 'Write 0 if you saw none.',
  [MC('How did you know it was not a plane?', 'It did not flash and moved smoothly', [('It made a loud noise', 'Satellites are silent to us.'), ('It was green', 'Look for smooth movement.')], o='O2')]))

# =====================================================================================  5.3
s = U.section('5.3', 'Friction, air resistance, water resistance and upthrust', ['O3']); s.words(V['5.3']); core(s, 'O3', 'O3')
s.stop(MC('Which makes more friction on a floor: socks or trainers?', 'Trainers', [('Socks', 'Socks slide easily.'), ('They are the same', 'Trainers grip.')], o='O3'),
       MC('What is friction?', 'A force between two surfaces rubbing together', [('The pull of the Earth', 'That is gravity.'), ('The push of water upwards', 'That is upthrust.')], o='O3'))
s.stop(MC('What is the upward push of water called?', 'Upthrust', [('Gravity', 'Gravity pulls down.'), ('Friction', 'Friction acts along surfaces.'), ('Air resistance', 'That acts in air.')], o='O3'),
       MC('Why do fish have streamlined shapes?', 'To reduce water resistance', [('To increase friction', 'They want to slip through.'), ('To sink faster', 'It is about moving easily.')], o='O3'))
s.prac(
 GD('Which force is mainly acting?', 'Force', [('a parachute falling slowly', 'air resistance'), ('brakes slowing a bike', 'friction'), ('a duck floating', 'upthrust'), ('a swimmer slowing down', 'water resistance')], o='O3'),
 MC('Why does a flat sheet of paper fall more slowly than a scrunched one?', 'It has a bigger surface, so more air resistance', [('It is heavier', 'Same paper, same weight.'), ('It has less gravity', 'Gravity is the same.')], o='O3'),
 MC('Why does a parachute have a huge canopy?', 'To catch lots of air and make lots of air resistance', [('To look colourful', 'It is about air resistance.'), ('To reduce air resistance', 'It increases it.')], o='O3'),
 MC('Which surface gives the most friction?', 'A rough rubber mat', [('Smooth ice', 'Ice is slippery.'), ('A polished floor', 'Smooth floors have little friction.')], o='O3'),
 MC('Why does a slide work well?', 'Its smooth surface has low friction', [('It has lots of friction', 'Low friction lets you slide.'), ('It pushes you up', 'Gravity pulls you down it.')], o='O3'),
 MS('Select the times when friction is useful.', ['shoes gripping the ground', 'bike brakes stopping you', 'holding a pencil'], ['sliding down a water slide'], o='O3'),
 CZ('Complete the sentences.', '{0} slows things moving through air. {1} slows things moving through water. Water pushes up with {2}.', [['Air resistance', 'air resistance'], ['Water resistance', 'water resistance'], ['upthrust']], o='O3'),
 MC('How do a cheetah\'s claws help it?', 'They grip the ground, giving more friction for fast turns', [('They reduce friction', 'They increase grip.'), ('They make it float', 'They are for grip.')], o='O3'),
 MC('In the shoe slide test, what did you measure?', 'The height of the tray when the shoe started to slide', [('The colour of the shoe', 'Measure the height.'), ('The size of the tray', 'Measure the height.')], o='O3'),
 TB('Shoe slide test results. Which shoe has the most grip?', ['Shoe', 'Height when it slid (cm)'], [['sock', '10'], ['smooth shoe', '15'], ['trainer', '30'], ['difference between trainer and sock', B(20)]], o='O3', skill='Data'),
 MC('What does a higher tray height mean in the shoe test?', 'More friction (more grip)', [('Less friction', 'It held on longer.'), ('A heavier shoe', 'It is about grip.')], o='O3'),
 MC('Why is it hard to run in a swimming pool?', 'Water resistance pushes back on you', [('Upthrust pulls you down', 'Upthrust pushes up.'), ('There is no friction', 'Water resistance slows you.')], o='O3'),
 MC('Why are boats pointed at the front?', 'To be streamlined and reduce water resistance', [('To look scary', 'It is about moving easily.'), ('To increase water resistance', 'It reduces it.')], o='O3'),
 MC('Why are parachutes always so calm? (the joke)', 'They never rush – they take it slow!', [('They are made of silk', 'It is a joke.'), ('They are asleep', 'It is a joke about slowing down.')], o='O3'),
)
s.adv(
 EX('Explain why a skydiver falls much more slowly once the parachute opens.', [('the parachute has a large surface', ['large', 'big', 'surface']), ('so there is much more air resistance', ['air resistance']), ('which pushes up against gravity / slows the fall', ['slow', 'gravity', 'push'])], 'The open parachute has a large surface, so it creates much more air resistance. This pushes up against gravity and slows the fall.', o='O3', d='H'),
 GR('Plot the shoe slide results.', {'label': 'Shoe (1 sock, 2 smooth shoe, 3 trainer)', 'min': 0, 'max': 4, 'step': 1}, {'label': 'Height when it slid (cm)', 'min': 0, 'max': 40, 'step': 10}, [[1, 10], [2, 15], [3, 30]], o='O3', d='H', table_rows=[[1, 10], [2, 15], [3, 30]]),
 MC('Why do racing cyclists crouch low and wear tight clothes?', 'To reduce air resistance', [('To increase friction', 'It is about air resistance.'), ('To get more upthrust', 'They are not in water.')], o='O3', d='H'),
 MC('Why do machines need oil?', 'Oil reduces friction between moving parts', [('Oil increases friction', 'It reduces it.'), ('Oil makes them heavier', 'It is about friction.')], o='O3', d='VH'),
)
s.labs('Grip lab',
 test_lab('Which shoe grips best?', 'Each shoe was put on a tray and one end was lifted slowly. Read the ruler: how high was the tray when the shoe slid?', 'The shoe', 'Height when it slid', 'cm', 40, 5, '📐',
  [('Sock', '🧦', 10), ('Smooth shoe', '👞', 15), ('Trainer', '👟', 30)],
  [MC('Which shoe has the most friction?', 'The trainer', [('The sock', 'It slid at only 10 cm.'), ('The smooth shoe', 'It slid at 15 cm.')], o='O3'),
   MC('What did you keep the same to make it fair?', 'The tray and the way you lifted it', [('The shoe', 'That was what you changed.'), ('The height', 'That was what you measured.')], o='O3')]),
 home('Paper drop race', 'Test air resistance with paper.', ['2 identical sheets of paper', 'a timer', 'a helper'],
  ['Drop from a safe height – do not climb on furniture.'],
  ['Scrunch one sheet into a tight ball. Keep the other flat.', 'Hold both at the same height and let go together.', 'Time how long each takes to land.', 'Repeat three times.'],
  ['Paper', 'Average time to land (s)'], [['Flat sheet', {'min': 0.1, 'max': 20}], ['Scrunched ball', {'min': 0.1, 'max': 20}]], 'Times are usually between 0.5 and 4 seconds.',
  [MC('Why did the flat sheet fall more slowly?', 'It had more air resistance', [('It was heavier', 'They were the same paper.'), ('Gravity was weaker on it', 'Gravity was the same.')], o='O3')]))

# =====================================================================================  5.4
s = U.section('5.4', 'Multiple forces', ['O4']); s.words(V['5.4']); core(s, 'O4', 'O4')
s.stop(MC('What happens when the forces on an object are unbalanced?', 'It speeds up, slows down or changes direction', [('Nothing changes', 'That is balanced forces.'), ('It disappears', 'Its movement changes.'), ('It always stops', 'It could speed up too.')], o='O4'),
       MC('In a tug of war, one team pulls harder. What happens?', 'The rope moves towards the stronger team', [('Nothing', 'The forces are unbalanced.'), ('The rope moves to the weaker team', 'It moves towards the bigger force.')], o='O4'))
s.stop(MC('A boat floats still on a lake. Are the forces on it balanced or unbalanced?', 'Balanced', [('Unbalanced', 'It is not changing its movement.'), ('There are no forces on it', 'Gravity and upthrust act on it.')], o='O4'),
       MC('Which two forces balance on a floating boat?', 'Gravity (down) and upthrust (up)', [('Friction and air resistance', 'It is floating still.'), ('Only gravity', 'Upthrust pushes up.')], o='O4'))
s.prac(
 GD('Are the forces balanced or unbalanced?', 'Forces', [('a car speeding up', 'unbalanced'), ('a lamp hanging still', 'balanced'), ('a bike braking', 'unbalanced'), ('a book on a shelf', 'balanced')], o='O4'),
 MC('You pedal hard and speed up. Which force is bigger?', 'The forward force from your pedalling', [('Friction and air resistance', 'Then you would slow down.'), ('They are equal', 'You are speeding up.')], o='O4'),
 MC('You pedal steadily at the same speed. The forces are…', 'balanced', [('unbalanced', 'Your speed is not changing.'), ('zero', 'Forces still act.')], o='O4'),
 MC('Why does a rocket stay on the launch pad at first?', 'Its engines are not yet pushing harder than gravity', [('It is tied down', 'It is about forces.'), ('There is no gravity on the pad', 'Gravity pulls it down.')], o='O4'),
 MC('What happens to a boat if too much cargo is added?', 'Gravity becomes bigger than upthrust, and it sinks', [('It floats higher', 'More weight pushes it down.'), ('Nothing', 'The forces become unbalanced.')], o='O4'),
 MC('What do force arrows show?', 'The size and direction of forces', [('The colour of the object', 'They show size and direction.'), ('How heavy the arrow is', 'They show forces.')], o='O4'),
 CZ('Complete the sentences.', 'When forces are {0}, nothing changes. When forces are {1}, an object can speed up, slow {2} or change direction.', [['balanced'], ['unbalanced'], ['down']], o='O4'),
 MC('Two teams pull with 300 N and 300 N. What happens?', 'Nothing – the forces are balanced', [('The rope moves left', 'The forces are equal.'), ('The rope breaks', 'It stays still.')], o='O4'),
 MC('A football rolls along the grass and slows down. Why?', 'Friction is an unbalanced force slowing it', [('Gravity pushes it backwards', 'Friction slows it.'), ('Forces are balanced', 'Its speed changes.')], o='O4'),
 TB('Work out the total force in each tug of war (left team minus right team).', ['Left team (N)', 'Right team (N)', 'Total force (N)'], [['500', '300', B(200)], ['400', '400', B(0)], ['250', '350', B(-100)]], o='O4', skill='Data', hint='A negative answer means the rope moves right.'),
 MC('When the forcemeters in the mini tug of war read the same, what does this show?', 'The forces are balanced', [('The forces are unbalanced', 'Equal readings mean balanced.'), ('The forcemeters are broken', 'They are working.')], o='O4'),
 OD('Put the bike ride in order.', ['pedal hard: speed up', 'pedal steadily: same speed', 'squeeze the brakes: slow down', 'stop'], o='O4'),
 MC('An object is still. The forces on it become unbalanced. What happens?', 'It starts to move', [('It stays still', 'Unbalanced forces cause a change.'), ('It gets heavier', 'Its movement changes.')], o='O4'),
 MC('Which is an example of a force changing direction?', 'A footballer heading the ball', [('A book resting on a table', 'Nothing changes there.'), ('A lamp hanging still', 'Nothing changes there.')], o='O4'),
)
s.adv(
 EX('Explain, using forces, why a skydiver falls at a steady speed after a while.', [('gravity pulls down', ['gravity']), ('air resistance pushes up and grows as speed increases', ['air resistance']), ('when they are equal the forces are balanced, so speed stays the same', ['balanced', 'equal', 'same speed', 'steady'])], 'Gravity pulls the skydiver down and air resistance pushes up. As the skydiver speeds up, air resistance grows until it equals gravity. The forces are then balanced, so the speed stays the same.', o='O4', d='H'),
 MC('A box is pushed with 30 N to the right. Friction is 10 N to the left. What happens?', 'It speeds up to the right (20 N unbalanced force)', [('It stays still', 'The forces are not equal.'), ('It moves left', 'The bigger force is to the right.')], o='O4', d='H'),
 MC('A truck moves at a steady speed on a flat road. Which is true?', 'The forward force equals friction and air resistance', [('There are no forces on it', 'Forces act but balance.'), ('The forward force is much bigger', 'Then it would speed up.')], o='O4', d='VH'),
 MS('Select all the effects unbalanced forces can have.', ['speed up', 'slow down', 'change direction'], ['make an object invisible'], o='O4', d='H'),
)
s.labs('Balanced or not? lab',
 sort_lab('Balanced or unbalanced?', 'Sort each situation.', ['Balanced forces', 'Unbalanced forces'],
  [('a book resting on a table', '📘', 0, 'Nothing is changing.'), ('a rocket lifting off', '🚀', 1, 'It is speeding up.'), ('a boat floating still', '⛵', 0, 'Gravity and upthrust are equal.'),
   ('a bike braking', '🚲', 1, 'It is slowing down.'), ('a tug of war with equal teams', '🪢', 0, 'The rope stays still.'), ('a ball being kicked', '⚽', 1, 'It starts moving.')],
  [MC('What do all the "balanced" situations have in common?', 'Their movement does not change', [('They are all moving fast', 'Balanced means no change.'), ('They have no forces', 'Forces act but balance.')], o='O4'),
   MC('A rocket lifts off. Which force is bigger?', 'The push of the engines', [('Gravity', 'Then it would not lift.'), ('They are equal', 'It is speeding up.')], o='O4')]),
 home('Tug of war with a ruler', 'Use two forcemeters or elastic bands to explore balanced forces.', ['2 forcemeters (or 2 identical elastic bands and a ruler)', 'a partner'],
  ['Pull gently – do not let go suddenly.', 'Keep elastic bands away from faces.'],
  ['Hook the two forcemeters (or bands) together.', 'Pull gently in opposite directions so nothing moves.', 'Read both forcemeters (or measure how long each band stretches).', 'Repeat with a bit more force.'],
  ['Try', 'Reading A', 'Reading B'], [['Try 1', {'min': 0, 'max': 100}, {'min': 0, 'max': 100}], ['Try 2', {'min': 0, 'max': 100}, {'min': 0, 'max': 100}]], 'Use newtons, or centimetres of stretch.',
  [MC('When nothing moved, how did the two readings compare?', 'They were the same – the forces were balanced', [('One was zero', 'Both pulled.'), ('One was always double', 'Balanced forces are equal.')], o='O4')]))

# =====================================================================================  5.5
s = U.section('5.5', 'Magnets and magnetic materials', ['O5']); s.words(V['5.5']); core(s, 'O5', 'O5')
s.stop(MC('Is every metal magnetic?', 'No – most metals, like copper and aluminium, are not magnetic', [('Yes – all metals are magnetic', 'Copper and aluminium are not.'), ('Only gold is magnetic', 'Gold is not magnetic.')], o='O5'),
       MC('Which metal is magnetic?', 'Iron', [('Copper', 'Copper is not magnetic.'), ('Aluminium', 'Aluminium is not magnetic.')], o='O5'))
s.stop(MC('Which of these is magnetic: copper, iron or plastic?', 'Iron', [('Copper', 'Copper is not magnetic.'), ('Plastic', 'Plastic is not magnetic.')], o='O5'),
       MC('What does a compass needle do?', 'It points north because it is a tiny magnet', [('It points to the nearest shop', 'It points north.'), ('It spins all the time', 'It settles pointing north.')], o='O5'))
s.prac(
 GD('Is each object magnetic or non-magnetic?', 'Group', [('iron nail', 'magnetic'), ('plastic ruler', 'non-magnetic'), ('steel paper clip', 'magnetic'), ('copper coin', 'non-magnetic'), ('wooden pencil', 'non-magnetic'), ('aluminium foil', 'non-magnetic')], o='O5'),
 MS('Select the magnetic materials.', ['iron', 'steel', 'nickel', 'cobalt'], ['copper', 'gold', 'plastic'], o='O5'),
 MC('What does "attract" mean?', 'Pull towards', [('Push away', 'That is repel.'), ('Melt', 'Attract means pull.')], o='O5'),
 MC('Can a magnet pull a paper clip without touching it?', 'Yes – magnetic force works across a gap', [('No – it must touch', 'It works across a gap.'), ('Only underwater', 'It works in air too.')], o='O5'),
 MC('How do fridge doors stay shut?', 'Magnetic strips pull the door to the fridge', [('Glue', 'They use magnets.'), ('Gravity', 'Magnets hold them.')], o='O5'),
 MC('How are steel cans separated at a recycling centre?', 'A giant magnet pulls them out', [('By colour', 'Magnets do it.'), ('By smell', 'Magnets sort steel.')], o='O5'),
 MC('Why are aluminium drink cans not picked up by the magnet?', 'Aluminium is not magnetic', [('They are too light', 'It is about the material.'), ('They are empty', 'Aluminium is non-magnetic.')], o='O5'),
 CZ('Complete the sentences.', 'A magnet {0} iron and steel. Copper is {1}. A {2} needle points north.', [['attracts'], ['non-magnetic', 'not magnetic'], ['compass']], o='O5'),
 TK('Tick the true statements.', ['True', 'False'], [('all metals are magnetic', ['✗', '✓']), ('steel is magnetic', ['✓', '✗']), ('magnets work through paper', ['✓', '✗']), ('wood is magnetic', ['✗', '✓'])], o='O5'),
 MC('Some birds find their way using…', 'the Earth\'s magnetism', [('the smell of the sea only', 'They sense magnetism.'), ('maps', 'Birds do not read maps!')], o='O5'),
 MC('What did one magnet say to the other? (the joke)', 'I find you very attractive!', [('Let\'s stick to the plan', 'Ha! The joke is about attraction.'), ('You repel me', 'The joke is about attraction.')], o='O5'),
 MC('In the magnet hunt, why should you predict before testing?', 'So you can check if your ideas were right', [('So the magnet works', 'Predicting is for learning.'), ('To save time', 'It helps you learn.')], o='O5'),
 TB('Magnet hunt: how many predictions were correct?', ['Object', 'Predicted', 'Result', 'Correct? (yes/no)'], [['key', 'magnetic', 'magnetic', 'yes'], ['coin', 'magnetic', 'non-magnetic', B('no')], ['pencil', 'non-magnetic', 'non-magnetic', B('yes')]], o='O5', skill='Data'),
 MC('A tin can is attracted to a magnet. What is it probably made of?', 'Steel', [('Aluminium', 'Aluminium is not magnetic.'), ('Plastic', 'Plastic is not magnetic.')], o='O5', d='H'),
)
s.adv(
 EX('Explain how you could separate a mixture of steel and aluminium cans.', [('use a magnet', ['magnet']), ('steel is magnetic and is pulled out', ['steel']), ('aluminium is not magnetic and is left behind', ['aluminium', 'aluminum', 'left', 'not magnetic'])], 'Pass a magnet over the cans. The steel cans are magnetic and are pulled out; the aluminium cans are not magnetic and are left behind.', o='O5', d='H'),
 MC('A metal spoon is not attracted to a magnet. What can you conclude?', 'It is made of a non-magnetic metal, such as aluminium or silver', [('It is made of iron', 'Iron would be attracted.'), ('All spoons are non-magnetic', 'Steel spoons are magnetic.')], o='O5', d='H'),
 MC('Why are some coins magnetic and others not?', 'Some coins contain steel or nickel, and others do not', [('Old coins are tired', 'It is about the metals.'), ('Coins change in the cold', 'It is about the metals.')], o='O5', d='VH'),
 MS('Select the everyday uses of magnets.', ['fridge door seals', 'compasses', 'recycling steel cans'], ['making bread rise'], o='O5', d='H'),
)
s.labs('Magnet hunt lab',
 sort_lab('Magnetic or not?', 'Test each object with the magnet and sort it.', ['Magnetic', 'Non-magnetic'],
  [('paper clip (steel)', '📎', 0, 'Steel is magnetic.'), ('copper coin', '🪙', 1, 'Copper is not magnetic.'), ('iron nail', '🔩', 0, 'Iron is magnetic.'), ('plastic spoon', '🥄', 1, 'Plastic is not magnetic.'),
   ('aluminium can', '🥫', 1, 'Aluminium is a non-magnetic metal.'), ('steel scissors', '✂️', 0, 'Steel is magnetic.'), ('wooden block', '🪵', 1, 'Wood is not magnetic.'), ('gold ring', '💍', 1, 'Gold is not magnetic.')],
  [MC('Which surprised many people: a metal that is NOT magnetic?', 'The aluminium can', [('The iron nail', 'Iron is magnetic.'), ('The paper clip', 'Steel is magnetic.')], o='O5'),
   MC('What do all the magnetic objects contain?', 'Iron (or steel, which is mostly iron)', [('Plastic', 'Plastic is not magnetic.'), ('Copper', 'Copper is not magnetic.')], o='O5')]),
 home('Fridge magnet hunt', 'Find magnetic things around your kitchen.', ['a fridge magnet', '10 small objects from the kitchen (ask first!)'],
  ['Keep magnets away from phones, cards and computers.', 'Do not use sharp objects.'],
  ['Collect 10 small objects.', 'Predict: magnetic or not?', 'Test each one with the magnet.', 'Count how many were magnetic.'],
  ['Result', 'Number of objects'], [['Magnetic', {'min': 0, 'max': 10}], ['Non-magnetic', {'min': 0, 'max': 10}], ['Correct predictions', {'min': 0, 'max': 10}]], 'The first two numbers should add up to 10.',
  [MC('Were all the metal objects magnetic?', 'No – some metals are not magnetic', [('Yes, always', 'Aluminium and copper are not.'), ('None of them were', 'Steel things are magnetic.')], o='O5')]))

# =====================================================================================  5.6
s = U.section('5.6', 'Magnetic force', ['O6']); s.words(V['5.6']); core(s, 'O6', 'O6')
s.stop(MC('What happens when two north poles meet?', 'They repel (push apart)', [('They attract (pull together)', 'Like poles repel.'), ('Nothing', 'They push apart.'), ('They stick forever', 'They repel.')], o='O6'),
       MC('What happens when a north pole meets a south pole?', 'They attract', [('They repel', 'Opposite poles attract.'), ('They both turn south', 'They attract.')], o='O6'))
s.stop(MC('Where is a magnet\'s force strongest?', 'At the poles', [('In the middle', 'It is weakest in the middle.'), ('It is the same everywhere', 'It is strongest at the poles.')], o='O6'),
       MC('What is the magnetic field?', 'The space around a magnet where it pushes or pulls', [('A field where magnets grow', 'Ha! It is the space around a magnet.'), ('The middle of a magnet', 'It is around the magnet.')], o='O6'))
s.prac(
 GD('Will the two poles attract or repel?', 'Result', [('north + south', 'attract'), ('south + south', 'repel'), ('north + north', 'repel'), ('south + north', 'attract')], o='O6'),
 MC('What are the two ends of a magnet called?', 'Poles', [('Tips', 'They are called poles.'), ('Corners', 'They are poles.')], o='O6'),
 MC('Why do the ring magnets float on the pencil?', 'Like poles face each other and repel', [('They are lighter than air', 'They repel.'), ('They are glued', 'They repel.')], o='O6'),
 MC('What do iron filings show around a magnet?', 'The shape of its magnetic field', [('Where the magnet is hot', 'They show the field.'), ('The magnet\'s weight', 'They show the field.')], o='O6'),
 MC('Can a magnet pull a paper clip through a sheet of paper?', 'Yes – magnetic force works through paper', [('No – paper blocks it', 'It works through paper.'), ('Only through metal', 'It works through many materials.')], o='O6'),
 MS('Select what magnetic force can work through.', ['paper', 'water', 'plastic'], ['nothing at all'], o='O6'),
 CZ('Complete the sentences.', 'Opposite poles {0}. Like poles {1}. The force is strongest at the {2}.', [['attract'], ['repel'], ['poles']], o='O6'),
 MC('How do some very fast trains float above their tracks?', 'Magnets repel each other', [('Wings lift them', 'Magnets do it.'), ('Wheels made of jelly', 'Magnets repel.')], o='O6'),
 MC('In the strongest magnet test, what did you count?', 'The number of paper clips the magnet held in a chain', [('The colour of the magnet', 'Count clips.'), ('The magnet\'s length', 'Count clips.')], o='O6'),
 MS('Which must stay the SAME to test magnet strength fairly?', ['the type of paper clip', 'using the same pole each time', 'adding clips one at a time'], ['the magnet being tested'], o='O6'),
 TB('Strongest magnet results. Complete the ranks (1 = strongest).', ['Magnet', 'Paper clips held', 'Rank'], [['fridge magnet', '2', B(4)], ['bar magnet', '8', B(3)], ['horseshoe magnet', '14', B(2)], ['super magnet', '20', B(1)]], o='O6', skill='Data'),
 MC('Is a bigger magnet always stronger?', 'No – you must test it to find out', [('Yes – always', 'Size does not always decide.'), ('No – smaller is always stronger', 'You must test.')], o='O6', d='H'),
 OD('Put the magnet test steps in order.', ['hang one paper clip from the magnet', 'add clips one at a time', 'count when the chain falls', 'repeat with another magnet'], o='O6'),
 MC('A magnet is cut in half. What happens?', 'Each half becomes a magnet with its own north and south poles', [('One half is north and one is south only', 'Each piece gets two poles.'), ('It stops being magnetic', 'Each half is still a magnet.')], o='O6', d='VH'),
)
s.adv(
 EX('Explain how you could find out which end of an unlabelled magnet is north.', [('use a labelled magnet / compass', ['labelled', 'compass', 'another magnet']), ('like poles repel, opposite attract', ['repel', 'attract']), ('the end repelled by a north pole is north', ['north'])], 'Bring the north pole of a labelled magnet near one end. If they repel, that end is north (like poles repel); if they attract, it is south.', o='O6', d='H'),
 GR('Plot the magnet strength results.', {'label': 'Magnet (1 fridge, 2 bar, 3 horseshoe, 4 super)', 'min': 0, 'max': 5, 'step': 1}, {'label': 'Paper clips held', 'min': 0, 'max': 24, 'step': 4}, [[1, 2], [2, 8], [3, 14], [4, 20]], o='O6', d='H', table_rows=[[1, 2], [2, 8], [3, 14], [4, 20]]),
 MC('A magnet held 8 clips, then 9, then 7 in three tries. What is the average?', '8 clips', [('7 clips', 'Add them and divide by 3.'), ('24 clips', 'That is the total.')], o='O6', d='H', reason='8 + 9 + 7 = 24; 24 ÷ 3 = 8.'),
 MC('Why do the iron filings bunch up at the ends of a bar magnet?', 'The magnetic field is strongest at the poles', [('The middle is hot', 'It is about field strength.'), ('Filings like the ends', 'The field is strongest there.')], o='O6', d='VH'),
)
s.labs('Magnet strength lab',
 test_lab('Which magnet is strongest?', 'Paper clips were hung in a chain from each magnet until they fell. Read the counter for each magnet.', 'The magnet', 'Paper clips held', 'clips', 24, 2, '📎',
  [('Fridge magnet', '🧲', 2), ('Bar magnet', '🧲', 8), ('Horseshoe magnet', '🧲', 14), ('Super magnet', '🧲', 20)],
  [MC('Which magnet was strongest?', 'The super magnet', [('The fridge magnet', 'It held only 2.'), ('The bar magnet', 'It held 8.')], o='O6'),
   MC('Why use the same kind of paper clip every time?', 'To keep the test fair', [('To save money', 'It is about fairness.'), ('Because they are shiny', 'It is a fair test.')], o='O6')]),
 home('Poles: push or pull?', 'Explore what happens when magnet poles meet.', ['2 magnets (fridge magnets or bar magnets)', 'a smooth table'],
  ['Keep magnets away from phones and cards.', 'Small magnets can be swallowed – keep away from young children.'],
  ['Put one magnet on the table.', 'Slowly push the other magnet towards it end first.', 'Does it attract or repel? Turn it round and try again.', 'Count how many times each happens in 6 tries.'],
  ['What happened', 'Number of times (out of 6)'], [['Attracted', {'min': 0, 'max': 6}], ['Repelled', {'min': 0, 'max': 6}]], 'The two numbers should add up to 6.',
  [MC('When the magnets repelled, which poles were facing?', 'Like poles (north-north or south-south)', [('Opposite poles', 'Opposite poles attract.'), ('No poles', 'Every magnet has poles.')], o='O6')]))

U.mindmap(('Forces', 'Gravity, normal and applied forces in newtons.', 'O1', '5.1'), ('Satellites', 'Gravity keeps the Moon and satellites in orbit.', 'O2', '5.2'),
          ('Slowing forces', 'Friction, air and water resistance; upthrust.', 'O3', '5.3'), ('Balanced forces', 'Balanced: no change. Unbalanced: change.', 'O4', '5.4'),
          ('Magnetic materials', 'Iron and steel; most metals are not magnetic.', 'O5', '5.5'), ('Poles', 'Opposites attract, likes repel.', 'O6', '5.6'))
