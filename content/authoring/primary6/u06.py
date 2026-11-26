# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 6 · Unit 6 Light and the Solar System. Written by the Camday teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kit6 import *
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'build', 'p6'))

OBJ = {
 'O1': {'sec': '6.1', 'code': 'Physics', 'codeNote': '', 't': 'Explain that we see objects when reflected light enters our eyes, and compare shiny and dull surfaces.'},
 'O2': {'sec': '6.1', 'code': 'Physics', 'codeNote': '', 't': 'Draw rays to show reflection in a mirror (equal angles), describe mirror images and explain how a periscope works.'},
 'O3': {'sec': '6.2', 'code': 'Physics', 'codeNote': '', 't': 'Describe refraction as the bending of light between materials, and give uses of lenses.'},
 'O4': {'sec': '6.2', 'code': 'Physics', 'codeNote': '', 't': 'Describe how a prism and raindrops split white light into a spectrum.'},
 'O5': {'sec': '6.3', 'code': 'Earth and space', 'codeNote': '', 't': 'Name the planets in order, and describe stars, planets and moons.'},
 'O6': {'sec': '6.3', 'code': 'Earth and space', 'codeNote': '', 't': 'Explain day, night and years, and describe the phases of the Moon.'},
}
U = Unit(6, 'Light and the Solar System', 'Physics and Earth and space: light and space', 'How light reflects and bends, how a prism makes a spectrum, and how the Earth, Moon and planets move.', OBJ)
from vocab_u6 import V, SAY as SAYW
core = core_for(V, SAYW)

# =====================================================================================  6.1
s = U.section('6.1', 'Reflection', ['O1', 'O2']); s.words(V['6.1']); core(s, 'O1', 'O2')
s.stop(MC('Why can we see a book that does not give out light?', 'Light from a light source reflects off the book into our eyes', [('Our eyes send out light onto the book', 'Eyes receive light; they do not send it out.'), ('The book makes its own light', 'A book is not a light source.'), ('We cannot see it at all', 'We can – because of reflection.')], o='O1'),
       MC('Which of these is a light source?', 'A lit candle', [('The Moon', 'The Moon reflects light from the Sun.'), ('A mirror', 'A mirror reflects light.'), ('A white wall', 'It reflects light.')], o='O1'))
s.stop(MC('In a mirror, what is special about the angles of the light rays?', 'The angle the light hits the mirror equals the angle it bounces off', [('The reflected ray is always at a right angle', 'The two angles are equal.'), ('The light goes straight through', 'A mirror reflects light.'), ('The angles are always different', 'They are equal.')], o='O2'),
       MC('A ray hits a mirror at 30°. At what angle does it bounce off?', '30°', [('60°', 'The angles are equal.'), ('90°', 'The angles are equal.')], o='O2'))
s.prac(
 MC('How does light travel?', 'In straight lines', [('In circles', 'Light travels in straight lines.'), ('In wavy curves around corners', 'That is why we cannot see round corners.')], o='O1'),
 GD('Is each one a light source or not?', 'Light source?', [('the Sun', 'yes'), ('a torch that is on', 'yes'), ('a mirror', 'no'), ('the Moon', 'no'), ('a book', 'no')], o='O1'),
 OD('Put the steps in order to show how we see a tree.', ['light comes from the Sun', 'it hits the tree', 'it reflects off the tree', 'it enters our eyes'], o='O1'),
 MC('What is reflection?', 'Light bouncing off a surface', [('Light bending in water', 'That is refraction.'), ('Light being made', 'A light source makes light.')], o='O1'),
 MC('Which surface reflects light best in one direction?', 'A smooth, shiny mirror', [('A rough wooden board', 'Rough surfaces scatter light.'), ('A black cloth', 'Dark, dull surfaces reflect little.')], o='O1'),
 MC('What do rough, dull surfaces do to light?', 'Scatter it in many directions', [('Reflect it all in one direction', 'Mirrors do that.'), ('Make it brighter', 'They scatter it.')], o='O1'),
 MC('Why are road signs and cyclists\' vests often shiny?', 'Shiny surfaces reflect a lot of light, so they are easy to see', [('They make their own light', 'They reflect light.'), ('Shiny things are lighter', 'It is about reflecting light.')], o='O1'),
 MC('What is a ray?', 'A straight line with an arrow that shows the path of light', [('A type of fish', 'In science, it shows light\'s path.'), ('A wavy line', 'Rays are straight.')], o='O2'),
 MT('Match each word to its meaning.', [('incident ray', 'the ray going towards the mirror'), ('reflected ray', 'the ray bouncing off the mirror'), ('plane mirror', 'a flat mirror'), ('image', 'what you see in a mirror')], o='O2'),
 MC('You raise your right hand in front of a mirror. What does your image do?', 'It raises its left hand', [('It raises its right hand', 'The image is reversed.'), ('It does nothing', 'It copies you, reversed.')], o='O2'),
 TK('Tick what is true about the image in a plane mirror.', ['True', 'False'], [('it is the same size as you', ['✓', '✗']), ('it is reversed left to right', ['✓', '✗']), ('it is upside down', ['✗', '✓']), ('it looks as far behind the mirror as you are in front', ['✓', '✗'])], o='O2'),
 MC('Why is "AMBULANCE" written backwards on the front of ambulances?', 'So drivers see it the right way round in their mirrors', [('To look interesting', 'It has a reason.'), ('Because ambulances drive backwards', 'They drive forwards!')], o='O2', d='H'),
 MC('What does a periscope let you do?', 'See over walls or other objects', [('See in the dark', 'It needs light.'), ('Make things bigger', 'That is a magnifying glass.')], o='O2'),
 MC('How many mirrors does a simple periscope have?', 'Two', [('One', 'Light reflects twice.'), ('Four', 'Two are enough.')], o='O2'),
 MC('At what angle are the mirrors in a periscope?', '45°', [('90°', 'They are tilted at 45°.'), ('10°', 'They are tilted at 45°.')], o='O2'),
 OD('Put the path of light through a periscope in order.', ['light comes from the object', 'it reflects off the top mirror', 'it travels down the tube', 'it reflects off the bottom mirror into your eye'], o='O2'),
 CZ('Complete the sentence.', 'In a mirror, the angle of the incident ray is {0} to the angle of the {1} ray.', [['equal', 'the same'], ['reflected']], o='O2'),
 MC('Who might use a periscope?', 'A submarine crew looking above the water', [('A swimmer under a shower', 'They do not need one.'), ('Someone reading a book', 'They can see the book.')], o='O2'),
)
s.adv(
 EX('Explain why you cannot see a friend standing behind a wall, but you can see them using a periscope.', [('light travels in straight lines', ['straight']), ('the wall blocks the light', ['block', 'stop']), ('the mirrors reflect the light over the wall into your eye', ['mirror', 'reflect'])], 'Light travels in straight lines, so the wall blocks the light from your friend. In a periscope, two mirrors reflect the light over the wall and into your eye.', o='O2', d='H'),
 TB('A ray hits a mirror at different angles. Complete the table.', ['Angle in (°)', 'Angle out (°)'], [['20', B(20)], ['35', B(35)], ['50', B(50)]], o='O2', d='M', skill='Data', reason='The angles are always equal.'),
 MC('Why do we see a white wall but not much of a black wall at night in a dim room?', 'White reflects much more light than black', [('Black gives out light', 'Black absorbs light.'), ('White is a light source', 'It reflects light.')], o='O1', d='H'),
 MC('A ray hits a mirror and the angle between the incident and reflected rays is 80°. What is each angle (measured from the line at right angles to the mirror)?', '40°', [('80°', 'The total is 80°, so each is half.'), ('20°', 'Half of 80 is 40.')], o='O2', d='VH'),
)
s.labs('Reflection lab',
 {'kind': 'test', 'title': 'Which surface reflects the most light?', 'intro': 'A torch shines on different surfaces. A light meter shows how much light is reflected (as a percentage). Read the scale for each surface.',
  'change': 'The surface', 'measure': 'Light reflected', 'unit': '%', 'max': 100, 'step': 10, 'instr': '🔦',
  'conds': [{'k': 'mirror', 't': 'Mirror', 'emoji': '🪞', 'val': 90}, {'k': 'foil', 't': 'Smooth foil', 'emoji': '🥈', 'val': 70}, {'k': 'paper', 't': 'White paper', 'emoji': '📄', 'val': 50}, {'k': 'cloth', 't': 'Black cloth', 'emoji': '⬛', 'val': 5}],
  'qs': [MC('Which surface reflected the most light?', 'The mirror', [('The black cloth', 'It reflected the least.'), ('White paper', 'The mirror reflected more.')], o='O1'),
         MC('What do the best reflectors have in common?', 'They are smooth and shiny', [('They are dark and rough', 'Those reflect little light.'), ('They are heavy', 'Weight does not matter.')], o='O1')]},
 {'title': 'Build a periscope', 'intro': 'Make a periscope and use it to see over things.',
  'need': ['a long box (e.g. a juice carton)', '2 small mirrors', 'scissors and tape', 'an adult to help cut'],
  'safety': ['Ask an adult to cut the box.', 'Hold mirrors carefully – they can have sharp edges.'],
  'steps': ['Cut a square window near the top on one side, and one near the bottom on the opposite side.', 'Fix a mirror at each window, tilted at 45°, facing each other.', 'Look into the bottom window – you should see out of the top one.', 'Hide behind a sofa or table and count how many objects you can see over it.'],
  'record': {'head': ['Where I looked', 'Objects I could see'], 'rows': [['Over a table', {'min': 0, 'max': 100}], ['Over a sofa or bed', {'min': 0, 'max': 100}]], 'hint': 'Write 0 if you could not see anything.'},
  'qs': [MC('Your periscope shows nothing. What is most likely wrong?', 'The mirrors are not at 45° facing each other', [('The box is the wrong colour', 'Colour does not matter.'), ('There is too much light', 'It needs light to work.')], o='O2')]})

# =====================================================================================  6.2
s = U.section('6.2', 'Refraction', ['O3', 'O4']); s.words(V['6.2']); core(s, 'O3', 'O4')
s.stop(MC('What is the bending of light called?', 'Refraction', [('Reflection', 'Reflection is bouncing.'), ('Evaporation', 'That is a liquid turning into a gas.'), ('Friction', 'That is a force.')], o='O3'),
       MC('Why does a straw in water look broken?', 'Light bends as it passes from water into air', [('The water breaks the straw', 'The straw is still straight.'), ('The glass is cracked', 'It is refraction.')], o='O3'))
s.stop(MC('What splits sunlight into colours to make a rainbow?', 'Raindrops, which refract the light like tiny prisms', [('Clouds, which paint the sky', 'It is raindrops refracting light.'), ('The Moon', 'The Moon does not make rainbows.'), ('Mirrors in the sky', 'It is raindrops.')], o='O4'),
       MC('Where must the Sun be for you to see a rainbow?', 'Behind you, with the rain in front', [('In front of you', 'The Sun must be behind you.'), ('Directly above, at midday only', 'Rainbows are seen with the Sun behind you.')], o='O4'))
s.prac(
 MC('When does light bend?', 'When it passes from one material into another at an angle', [('Only when it hits a mirror', 'That is reflection.'), ('Never – light is always straight', 'It bends between materials.')], o='O3'),
 MC('Why does light bend between air and water?', 'It travels at different speeds in different materials', [('Water is heavier than air', 'It is about speed.'), ('Water is wet', 'It is about speed.')], o='O3'),
 GD('Is each one reflection or refraction?', 'Light', [('seeing yourself in a mirror', 'reflection'), ('a straw looking bent in water', 'refraction'), ('a magnifying glass making print bigger', 'refraction'), ('a periscope', 'reflection')], o='O3'),
 MC('What is a lens?', 'A curved piece of glass or plastic that refracts light', [('A flat mirror', 'A mirror reflects.'), ('A light source', 'A lens bends light.')], o='O3'),
 MC('What is a convex lens like?', 'Thicker in the middle than at the edges', [('Thinner in the middle', 'That is a concave lens.'), ('Completely flat', 'A lens is curved.')], o='O3'),
 MC('What is the focal point of a convex lens?', 'The point where the light rays meet', [('The thickest part of the lens', 'It is where rays meet.'), ('The edge of the lens', 'It is where rays meet.')], o='O3'),
 MS('Select the things that use lenses.', ['glasses', 'a camera', 'a magnifying glass', 'your eyes'], ['a mirror', 'a spoon'], o='O3'),
 CZ('Complete the sentence.', 'The bending of light is called {0}. A convex lens brings rays together at the {1} point.', [['refraction'], ['focal']], o='O3'),
 MC('In the coin trick, why does the coin appear when water is added?', 'The water refracts light from the coin towards your eyes', [('The water lifts the coin up', 'The coin stays on the bottom.'), ('The coin gets bigger', 'It is refraction.')], o='O3'),
 MC('What is white light?', 'A mixture of many colours', [('One single colour', 'It is a mixture.'), ('No colour at all', 'It contains all the colours.')], o='O4'),
 MC('What does a prism do to white light?', 'It splits it into a spectrum of colours', [('It makes it brighter', 'It splits it.'), ('It turns it into heat only', 'It makes a spectrum.')], o='O4'),
 OD('Put the colours of the spectrum in order.', ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'], o='O4'),
 MC('Why does a prism split white light?', 'It refracts each colour by a slightly different amount', [('It reflects each colour back', 'It refracts them.'), ('It adds colours to the light', 'The colours were already in the white light.')], o='O4'),
 MC('Which colour is refracted the MOST by a prism?', 'Violet', [('Red', 'Red bends the least.'), ('Green', 'Violet bends most.')], o='O4', d='H'),
 MC('Raindrops make a rainbow by…', 'refracting and reflecting sunlight', [('only reflecting it', 'They refract it too.'), ('making their own light', 'They use sunlight.')], o='O4'),
 MC('Why do we not see rainbows at night?', 'There is no sunlight to split', [('Raindrops freeze at night', 'It is about sunlight.'), ('Rainbows only form in winter', 'It is about sunlight.')], o='O4'),
 MC('A mnemonic helps you remember the colours. What does "Richard Of York Gave Battle In Vain" stand for?', 'Red, orange, yellow, green, blue, indigo, violet', [('Rain, ocean, yellow, grass, blue, ice, violet', 'Each first letter is a colour.'), ('The planets in order', 'It is the spectrum.')], o='O4'),
 MC('Which happens when sunlight shines through a glass of water onto white paper?', 'A small spectrum of colours can appear', [('The paper turns black', 'Light makes colours.'), ('Nothing happens at all', 'The water can split the light.')], o='O4', d='H'),
)
s.adv(
 EX('Explain how a rainbow forms.', [('sunlight is white light, a mixture of colours', ['white light', 'mixture', 'colours']), ('raindrops refract (and reflect) the light', ['refract', 'bend', 'raindrop']), ('each colour bends a different amount, so they spread out', ['different', 'spread', 'split'])], 'Sunlight is a mixture of colours. Raindrops refract and reflect the light, and each colour bends by a different amount, so the colours spread out into a rainbow.', o='O4', d='H'),
 MC('A magnifying glass held in sunlight makes a tiny bright spot on paper. What is the spot?', 'The focal point, where the rays meet', [('A reflection', 'The lens refracts the light.'), ('A shadow', 'It is very bright, not dark.')], o='O3', d='H'),
 TB('Asha measured how far she could step back before the coin disappeared. Complete the difference.', ['Cup', 'Distance (cm)'], [['empty', '30'], ['with water', '55'], ['difference', B(25)]], o='O3', d='M', skill='Data', reason='55 − 30 = 25 cm.'),
 MC('Why is it dangerous to look at the Sun through a lens?', 'The lens focuses the Sun\'s light and can damage your eye', [('The lens makes the Sun smaller', 'It focuses the light.'), ('It is not dangerous', 'It can blind you.')], o='O3', d='VH'),
)
s.labs('Light lab',
 {'kind': 'sort', 'title': 'Reflection or refraction?', 'intro': 'Sort each card. Is the light bouncing off (reflection) or bending (refraction)?',
  'groups': ['Reflection (bouncing)', 'Refraction (bending)'],
  'items': [{'t': 'your face in a mirror', 'emoji': '🪞', 'g': 0, 'why': 'Mirrors reflect light.'}, {'t': 'a straw looks broken in water', 'emoji': '🥤', 'g': 1, 'why': 'Light bends between water and air.'},
            {'t': 'a rainbow', 'emoji': '🌈', 'g': 1, 'why': 'Raindrops refract (bend) sunlight.'}, {'t': 'a periscope', 'emoji': '🔭', 'g': 0, 'why': 'It uses two mirrors.'},
            {'t': 'a magnifying glass', 'emoji': '🔍', 'g': 1, 'why': 'A lens bends light.'}, {'t': 'seeing a book', 'emoji': '📖', 'g': 0, 'why': 'Light reflects off the book.'},
            {'t': 'a prism making a spectrum', 'emoji': '🔺', 'g': 1, 'why': 'The prism bends the light.'}, {'t': 'a shiny safety vest', 'emoji': '🦺', 'g': 0, 'why': 'It reflects car lights.'}],
  'qs': [MC('Which word means light bending?', 'Refraction', [('Reflection', 'That is bouncing.'), ('Spectrum', 'That is the band of colours.')], o='O3'),
         MC('Which object in the lab splits white light into colours?', 'The prism', [('The mirror', 'A mirror reflects.'), ('The book', 'A book reflects.')], o='O4')]},
 {'title': 'The appearing coin', 'intro': 'Use refraction to make a coin appear.',
  'need': ['a coin', 'a cup that you cannot see through', 'a jug of water', 'a friend', 'a tape measure'],
  'safety': ['Wipe up any spilled water.', 'Do not put coins in your mouth.'],
  'steps': ['Put the coin in the bottom of the empty cup on a table.', 'Look at the coin and slowly step back until it just disappears behind the rim. Measure your distance from the cup.', 'Keep your head still while your friend slowly pours in water. Watch the coin appear!', 'Now step back again until the coin disappears, and measure the new distance.'],
  'record': {'head': ['Cup', 'Distance when the coin disappears (cm)'], 'rows': [['Empty', {'min': 1, 'max': 500}], ['Full of water', {'min': 1, 'max': 500}]], 'hint': 'Distances are usually between 10 and 150 cm.'},
  'qs': [MC('Why could you see the coin from further away with water?', 'The water refracts light from the coin up towards your eyes', [('The water makes the coin float', 'It stays at the bottom.'), ('The water is a mirror', 'It bends light.')], o='O3')]})

# =====================================================================================  6.3
s = U.section('6.3', 'The Solar System', ['O5', 'O6']); s.words(V['6.3']); core(s, 'O5', 'O6')
s.stop(MC('Which planet is closest to the Sun?', 'Mercury', [('Venus', 'Venus is second.'), ('Earth', 'Earth is third.'), ('Neptune', 'Neptune is furthest.')], o='O5'),
       MC('Which planet is furthest from the Sun?', 'Neptune', [('Mercury', 'Mercury is closest.'), ('Jupiter', 'Jupiter is fifth.')], o='O5'))
s.stop(MC('What do we call it when the lit part of the Moon is getting bigger each night?', 'Waxing', [('Waning', 'Waning is when it gets smaller.'), ('Orbiting', 'The Moon orbits, but the word for growing is waxing.'), ('Spinning', 'That is not the word.')], o='O6'),
       MC('What do we call it when the lit part of the Moon gets smaller?', 'Waning', [('Waxing', 'Waxing is growing.'), ('Full moon', 'That is a phase, not the shrinking.')], o='O6'))
s.prac(
 OD('Put the planets in order from the Sun.', ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'], o='O5', d='H'),
 MC('How many planets orbit the Sun?', 'Eight', [('Nine', 'There are eight planets.'), ('Twelve', 'There are eight planets.')], o='O5'),
 MC('What is at the centre of our Solar System?', 'The Sun', [('The Earth', 'The Earth orbits the Sun.'), ('The Moon', 'The Moon orbits the Earth.')], o='O5'),
 MT('Match each word to its meaning.', [('star', 'gives out its own light'), ('planet', 'orbits a star'), ('moon', 'orbits a planet'), ('orbit', 'the path around another object')], o='O5'),
 GD('Is each one a star, a planet or a moon?', 'Type', [('the Sun', 'star'), ('Mars', 'planet'), ('the Moon', 'moon'), ('Jupiter', 'planet')], o='O5'),
 MC('Why does the Moon shine at night?', 'It reflects light from the Sun', [('It makes its own light', 'The Moon is not a light source.'), ('It is on fire', 'It reflects sunlight.')], o='O5'),
 MC('Which is the largest planet?', 'Jupiter', [('Earth', 'Jupiter is much bigger.'), ('Mercury', 'Mercury is the smallest.')], o='O5'),
 MC('Which planet has bright rings that are easy to see?', 'Saturn', [('Mercury', 'Mercury has no rings.'), ('Mars', 'Mars has no rings.')], o='O5'),
 MC('What is a natural satellite?', 'A moon that orbits a planet', [('A space station', 'That is an artificial satellite.'), ('A star', 'Stars give out light.')], o='O5'),
 MC('What causes day and night?', 'The Earth spinning on its axis', [('The Sun moving around the Earth', 'The Earth spins.'), ('The Moon blocking the Sun', 'That is an eclipse.')], o='O6'),
 MC('How long does the Earth take to spin once?', '24 hours', [('365 days', 'That is one orbit of the Sun.'), ('27 days', 'That is about one orbit of the Moon.')], o='O6'),
 MC('How long does the Earth take to orbit the Sun?', 'About 365¼ days (one year)', [('24 hours', 'That is one spin.'), ('About one month', 'That is about the Moon\'s orbit.')], o='O6'),
 GD('Match each movement to its time.', 'Time', [('Earth spins once', '1 day'), ('Earth orbits the Sun', '1 year'), ('Moon orbits the Earth', 'about 1 month')], o='O6'),
 MC('Why do planets further from the Sun have longer years?', 'They have bigger orbits, so take longer to go around', [('They spin faster', 'A year is about orbiting.'), ('They are hotter', 'Distance makes the orbit longer.')], o='O6'),
 OD('Put the Moon\'s phases in order, starting from new moon.', ['new moon', 'crescent (waxing)', 'first quarter', 'gibbous (waxing)', 'full moon'], o='O6'),
 MC('Why does the Moon seem to change shape?', 'We see different amounts of its lit half as it orbits the Earth', [('Clouds cover parts of it', 'The phases happen on clear nights too.'), ('The Moon really changes shape', 'It is always a ball.')], o='O6'),
 MC('About how long does the cycle of the Moon\'s phases take?', 'About a month', [('One day', 'It takes about four weeks.'), ('One year', 'It takes about four weeks.')], o='O6'),
 MC('To keep a Moon diary, when should you look?', 'At the same time each clear night', [('At a different time each night', 'Keep the time the same.'), ('Only once', 'You need many nights.')], o='O6'),
)
s.adv(
 EX('Explain why it is night in one country while it is day in another.', [('the Earth spins (on its axis)', ['spin', 'rotate', 'axis']), ('the side facing the Sun has day', ['facing', 'towards the Sun', 'day']), ('the side facing away has night', ['away', 'night'])], 'The Earth spins on its axis. The side facing the Sun has day, while the side facing away from the Sun has night.', o='O6', d='H'),
 TB('Complete the table of planet years (in Earth years, rounded).', ['Planet', 'Time to orbit the Sun (years)'], [['Earth', '1'], ['Mars', '2'], ['Jupiter', '12'], ['Saturn', B(29)]], o='O6', d='H', skill='Data', hint='Saturn takes 29 Earth years.', reason='Saturn takes about 29 Earth years to orbit the Sun.'),
 MC('A child looks at a thin crescent Moon, then a week later sees a half Moon. Is the Moon waxing or waning?', 'Waxing – the lit part is growing', [('Waning – the lit part is shrinking', 'It grew from crescent to half.'), ('Neither', 'It changed.')], o='O6', d='H'),
 MC('Which statement is TRUE?', 'The Sun is a star, and the Earth is a planet that orbits it', [('The Sun orbits the Earth', 'The Earth orbits the Sun.'), ('The Moon is a star', 'The Moon is a moon.'), ('Planets give out their own light', 'They reflect light.')], o='O5', d='VH'),
)
s.labs('Space lab',
 {'kind': 'sort', 'title': 'Star, planet or moon?', 'intro': 'Sort each object in space into the right group.',
  'groups': ['Star', 'Planet', 'Moon'],
  'items': [{'t': 'the Sun', 'emoji': '☀️', 'g': 0, 'why': 'The Sun gives out its own light – it is a star.'}, {'t': 'Earth', 'emoji': '🌍', 'g': 1, 'why': 'Earth orbits the Sun.'},
            {'t': 'the Moon', 'emoji': '🌙', 'g': 2, 'why': 'The Moon orbits the Earth.'}, {'t': 'Mars', 'emoji': '🔴', 'g': 1, 'why': 'Mars orbits the Sun.'},
            {'t': 'Saturn', 'emoji': '🪐', 'g': 1, 'why': 'Saturn orbits the Sun.'}, {'t': 'Titan (orbits Saturn)', 'emoji': '🟠', 'g': 2, 'why': 'It orbits a planet, so it is a moon.'},
            {'t': 'Mercury', 'emoji': '⚫', 'g': 1, 'why': 'Mercury orbits the Sun.'}],
  'qs': [MC('What makes the Sun different from the planets?', 'It gives out its own light', [('It orbits the Earth', 'The Earth orbits the Sun.'), ('It is a moon', 'The Sun is a star.')], o='O5'),
         MC('What does a moon orbit?', 'A planet', [('A star directly', 'Moons orbit planets.'), ('Nothing', 'Moons orbit planets.')], o='O5')]},
 {'title': 'Moon diary', 'intro': 'Watch the Moon for four weeks and record how much of it is lit.',
  'need': ['clear night skies', 'the table below or a notebook', 'an adult to go outside with you'],
  'safety': ['Go outside only with an adult.', 'Never look at the Sun.'],
  'steps': ['Once a week, look at the Moon at about the same time.', 'Estimate how much of the Moon is lit: 0% (new moon), 50% (half), 100% (full).', 'Write your estimate in the table. If it is cloudy, try the next clear night.', 'Look for the pattern: is the Moon waxing or waning?'],
  'record': {'head': ['Week', 'Moon lit (%)'], 'rows': [['Week 1', {'min': 0, 'max': 100}], ['Week 2', {'min': 0, 'max': 100}], ['Week 3', {'min': 0, 'max': 100}], ['Week 4', {'min': 0, 'max': 100}]], 'hint': 'Use 0 to 100: 0 = new moon, 50 = half, 100 = full.'},
  'qs': [MC('Your Moon went 25%, 50%, 100%, 50%. When was it waning?', 'After the full moon (100% to 50%)', [('Before the full moon', 'Then it was growing – waxing.'), ('It never waned', 'It went down from 100% to 50%.')], o='O6')]})

U.mindmap(('Seeing objects', 'Reflected light enters our eyes.', 'O1', '6.1'), ('Mirrors', 'Equal angles; reversed images; periscopes.', 'O2', '6.1'),
          ('Refraction', 'Light bends between materials; lenses.', 'O3', '6.2'), ('Spectrum', 'Prisms and raindrops split white light.', 'O4', '6.2'),
          ('Solar System', 'Sun, eight planets, moons.', 'O5', '6.3'), ('Days, years and phases', 'Spin = day; orbit = year; Moon phases.', 'O6', '6.3'))
