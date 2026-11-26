# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 3 · Unit 6 The Earth and the Moon. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit3 import *

OBJ = {
 'O1': {'sec': '6.1', 'code': 'Earth and Space', 'codeNote': '', 't': 'Know that the Earth, the Sun and the Moon are spheres, and compare their sizes.'},
 'O2': {'sec': '6.2', 'code': 'Earth and Space', 'codeNote': '', 't': 'Know that the Moon orbits the Earth, describe its surface, and know that moonlight is reflected sunlight.'},
 'O3': {'sec': '6.3', 'code': 'Earth and Space', 'codeNote': '', 't': 'Name the phases of the Moon and know that the pattern repeats about every month.'},
}
U = YUnit(6, 'The Earth and the Moon', 'Earth and Space', 'The shapes and sizes of the Earth, the Sun and the Moon, the Moon\'s surface and its phases.', OBJ)

# ============================================================  6.1
s = U.section('6.1', 'The Earth, the Sun and the Moon', ['O1']); s.words(V['6.1']); core(s, 'O1')
s.stop(PM('What shape is the Earth?', ('⚽', 'A sphere, like a ball'), [('📄', 'Flat, like paper', 'The Earth is round like a ball.'), ('📦', 'A cube, like a box', 'The Earth is round like a ball.')], 'O1'),
       PM('Which shape is a sphere?', ('🏀', 'A ball'), [('📘', 'A book', 'A book is flat.'), ('🔺', 'A triangle', 'A sphere is a ball shape.')], 'O1'))
s.stop(PM('Which is the biggest?', ('☀️', 'The Sun'), [('🌍', 'The Earth', 'The Sun is much bigger.'), ('🌕', 'The Moon', 'The Moon is the smallest.')], 'O1'),
       PM('Which is the smallest?', ('🌕', 'The Moon'), [('☀️', 'The Sun', 'The Sun is the biggest.'), ('🌍', 'The Earth', 'The Earth is bigger than the Moon.')], 'O1'))
s.prac(
 OD('Order from smallest to biggest.', ['the Moon', 'the Earth', 'the Sun'], o='O1'),
 YN('Is the Sun a star?', True, 'O1', pic='☀️', why='Yes. It is the closest star to the Earth.'),
 PM('Why does the Sun look small in the sky?', ('🔭', 'It is very far away'), [('🤏', 'It is really tiny', 'It is huge, but far away.'), ('☁️', 'Clouds shrink it', 'It is far away.')], 'O1'),
 GD('Is it a sphere?', 'Sphere?', [('🌍 the Earth', 'yes'), ('🌕 the Moon', 'yes'), ('☀️ the Sun', 'yes'), ('📘 a book', 'no')], o='O1'),
 MT('Match each word to what it means.', [('sphere', 'a ball shape'), ('star', 'a ball of hot gas that shines'), ('space', 'where the planets are')], o='O1'),
 PM('What is the Sun made of?', ('🔥', 'Very hot gas'), [('🧀', 'Cheese', 'It is very hot gas.'), ('🪨', 'Cold rock', 'It is very hot gas.')], 'O1'),
 TK('Tick what is true.', ['True', 'False'], [('the Earth is round', ['✓', '✗']), ('the Moon is bigger than the Sun', ['✗', '✓']), ('the Sun is a star', ['✓', '✗'])], o='O1'),
 PM('Astronauts looked back at the Earth from space. What did they see?', ('🌍', 'A round, blue and green ball'), [('📄', 'A flat square', 'It is a sphere.'), ('⭐', 'A star shape', 'It is a sphere.')], 'O1'),
 YN('Could more than a million Earths fit inside the Sun?', True, 'O1', pic='☀️', why='Yes! The Sun is enormous.'),
 PM('A ball is held near your eyes, then carried far away. It looks…', ('🤏', 'smaller'), [('🐘', 'bigger', 'Far things look smaller.'), ('🌈', 'colourful', 'It looks smaller.')], 'O1'),
 PM('In a space model, which ball should be the Earth?', ('🔵', 'A small ball'), [('🟡', 'The biggest ball', 'That is the Sun.'), ('⚪', 'The tiniest ball', 'That is the Moon.')], 'O1', d='H'),
 YN('Do we live on the Moon?', False, 'O1', pic='🌕', why='No. We live on the Earth.'),
)
s.adv(
 PM('* Advanced. The Sun and the Moon look about the same size in the sky. Why?', ('🔭', 'The Sun is much bigger but much further away'), [('🟰', 'They are the same size', 'The Sun is far bigger.'), ('☁️', 'Clouds make them match', 'The Sun is much further away.')], 'O1', d='VH'),
 PM('* Advanced. Which is closest to the Earth?', ('🌕', 'The Moon'), [('☀️', 'The Sun', 'The Moon is much closer.'), ('⭐', 'Other stars', 'They are very far.')], 'O1', d='H'),
 OD('* Advanced. Order from closest to the Earth to furthest.', ['the Moon', 'the Sun', 'other stars'], o='O1', d='H'),
)
s.labs('Space model lab',
 sort_lab('Sphere or not?', 'Sort each thing by its shape.', ['Sphere', 'Not a sphere'],
  [('the Earth', '🌍', 0, 'It is a ball shape.'), ('a book', '📘', 1, 'It is flat.'), ('the Moon', '🌕', 0, 'It is a ball shape.'), ('a box', '📦', 1, 'It is a cube.'), ('the Sun', '☀️', 0, 'It is a ball shape.'), ('a pencil', '✏️', 1, 'It is long and thin.')],
  [PM('What shape are the Earth, Sun and Moon?', ('⚽', 'Spheres'), [('📦', 'Cubes', 'They are ball shapes.')], 'O1')]),
 home('Space models', 'Make a model with three balls.', ['three balls of different sizes'], ['Do not throw the balls indoors.'],
  ['Find three balls.', 'Choose one for the Sun, Earth and Moon.', 'Line them up from smallest to biggest.'],
  ['Ball', 'Which one is it?'], [('the biggest ball', ['Sun', 'Earth', 'Moon']), ('the smallest ball', ['Sun', 'Earth', 'Moon'])],
  [PM('Which ball was the Sun?', ('🟡', 'The biggest'), [('⚪', 'The smallest', 'That is the Moon.')], 'O1')]))

# ============================================================  6.2
s = U.section('6.2', 'The Moon', ['O2']); s.words(V['6.2']); core(s, 'O2')
s.stop(PM('What does the Moon travel around?', ('🌍', 'The Earth'), [('🌕', 'Itself only', 'It goes round the Earth.'), ('🚀', 'A rocket', 'It goes round the Earth.')], 'O2'),
       PM('How long does the Moon take to go round the Earth?', ('📅', 'About a month'), [('⏰', 'One hour', 'About a month.'), ('🎂', 'Ten years', 'About a month.')], 'O2'))
s.stop(PM('Does the Moon make its own light?', ('👎', 'No – it reflects sunlight'), [('👍', 'Yes – it glows like a lamp', 'Sunlight bounces off it.')], 'O2'),
       PM('Why does the Moon shine at night?', ('☀️', 'Sunlight bounces off it'), [('💡', 'It has lamps', 'Sunlight bounces off it.'), ('🔥', 'It is on fire', 'Sunlight bounces off it.')], 'O2'))
s.prac(
 PM('What are the big round holes on the Moon called?', ('🕳️', 'Craters'), [('🌊', 'Oceans', 'They are craters.'), ('🏠', 'Houses', 'They are craters.')], 'O2'),
 YN('Is there air to breathe on the Moon?', False, 'O2', pic='😮‍💨', why='No. Astronauts need space suits.'),
 GD('True for the Moon?', 'True?', [('🪨 rocks and dust', 'yes'), ('🌳 trees and grass', 'no'), ('🕳️ craters', 'yes'), ('💧 rivers of water', 'no')], o='O2'),
 PM('Why do astronauts wear space suits on the Moon?', ('😮‍💨', 'There is no air to breathe'), [('🎨', 'To look nice', 'There is no air.'), ('🌧️', 'It rains a lot', 'There is no air.')], 'O2'),
 MT('Match each word to what it means.', [('orbit', 'travel round something'), ('crater', 'round hole on the Moon'), ('astronaut', 'person who goes to space')], o='O2'),
 TK('Tick what is true.', ['True', 'False'], [('the Moon orbits the Earth', ['✓', '✗']), ('animals live on the Moon', ['✗', '✓']), ('people have walked on the Moon', ['✓', '✗'])], o='O2'),
 PM('Why are astronauts\' footprints still on the Moon?', ('🌬️', 'There is no wind to blow them away'), [('🧊', 'They are frozen in ice', 'There is no wind.'), ('🧹', 'Nobody sweeps there', 'There is no wind.')], 'O2'),
 OD('Order how moonlight reaches you.', ['the Sun shines', 'light hits the Moon', 'light bounces to your eyes'], o='O2'),
 YN('Is the Moon covered in grey dust?', True, 'O2', pic='🌕', why='Yes. Grey rocks and dust.'),
 PM('What colour is most of the Moon\'s ground?', ('🩶', 'Grey'), [('💚', 'Green', 'No plants grow there.'), ('💙', 'Blue', 'It is grey.')], 'O2'),
 PM('You drop marbles into flour. What do you make?', ('🕳️', 'Pretend craters'), [('🎂', 'A cake', 'They look like craters.'), ('🌊', 'Waves', 'They look like craters.')], 'O2', d='H'),
 YN('Could you live on the Moon without help?', False, 'O2', pic='🧑‍🚀', why='No. There is no air, water or food.'),
)
s.adv(
 PM('* Advanced. What made most of the Moon\'s craters?', ('☄️', 'Space rocks crashing into it'), [('🐇', 'Moon rabbits digging', 'Space rocks did.'), ('🌧️', 'Rain', 'There is no rain.')], 'O2', d='VH'),
 PM('* Advanced. On the Moon, you would feel…', ('🪶', 'much lighter'), [('🏋️', 'much heavier', 'Its gravity is weaker.'), ('🤷', 'exactly the same', 'Its gravity is weaker.')], 'O2', d='H'),
 OD('* Advanced. Order a trip to the Moon.', ['blast off in a rocket', 'travel through space', 'land on the Moon', 'walk in a space suit'], o='O2', d='H'),
)
s.labs('Crater lab',
 test_lab('Crater test', 'Drop a marble into flour from different heights. Read how wide the crater is.', 'Drop height', 'Crater width', 'cm', 10, 1,
  'Tap the number the bar reaches.', [('low (10 cm)', '⬇️', 2), ('middle (50 cm)', '↕️', 5), ('high (1 metre)', '⬆️', 8)],
  [PM('Which drop made the widest crater?', ('⬆️', 'The highest drop'), [('⬇️', 'The lowest drop', 'That made the smallest crater.')], 'O2')]),
 home('Make craters', 'Make Moon craters in flour.', ['a tray of flour', 'a little cocoa', 'marbles', 'an adult'], ['Do this outside or over newspaper.', 'Do not throw marbles at anyone.'],
  ['Fill the tray with flour and sprinkle cocoa on top.', 'Drop marbles into the flour.', 'Lift them out carefully.'],
  ['Question', 'My answer'], [('did I make craters?', ['yes', 'no']), ('did a higher drop make a bigger crater?', ['yes', 'no'])],
  [PM('What are your holes like?', ('🕳️', 'Moon craters'), [('🌋', 'Volcanoes', 'They are like craters.')], 'O2')]))

# ============================================================  6.3
s = U.section('6.3', 'Phases of the Moon', ['O3']); s.words(V['6.3']); core(s, 'O3')
s.stop(PM('Does the Moon really change shape?', ('👎', 'No – we see different amounts of its lit half'), [('👍', 'Yes – it gets bitten', 'It is always round.')], 'O3'),
       PM('What shape is the Moon really?', ('⚽', 'Always a round ball'), [('🌙', 'Always a thin slice', 'It is always round.'), ('🍕', 'A triangle', 'It is always round.')], 'O3'))
s.stop(PM('What do we call the Moon when it is a big, bright circle?', ('🌕', 'A full moon'), [('🌑', 'A new moon', 'A new moon is dark.'), ('🌙', 'A crescent', 'A crescent is a thin slice.')], 'O3'),
       PM('What do we call the Moon when we cannot see it?', ('🌑', 'A new moon'), [('🌕', 'A full moon', 'A full moon is bright.'), ('🌓', 'A half moon', 'We see half of it.')], 'O3'))
s.prac(
 GD('Name the phase.', 'Phase', [('🌕 a bright circle', 'full moon'), ('🌑 nothing to see', 'new moon'), ('🌙 a thin slice', 'crescent'), ('🌓 half a circle', 'half moon')], o='O3'),
 PM('How long does the whole pattern of phases take?', ('📅', 'About a month'), [('⏰', 'One day', 'About a month.'), ('🎂', 'One year', 'About a month.')], 'O3'),
 YN('Does the Sun always light up half of the Moon?', True, 'O3', pic='☀️', why='Yes. We see different amounts of that half.'),
 OD('Order the phases from new moon.', ['new moon', 'crescent', 'half moon', 'full moon'], o='O3'),
 MT('Match each word to what it means.', [('phase', 'the shape the Moon seems to have'), ('crescent', 'a thin curved slice'), ('month', 'about four weeks')], o='O3'),
 PM('Which phase looks like a banana?', ('🌙', 'A crescent'), [('🌕', 'A full moon', 'That is a circle.'), ('🌑', 'A new moon', 'We cannot see it.')], 'O3'),
 TK('Tick what is true.', ['True', 'False'], [('the phases repeat', ['✓', '✗']), ('the Moon is sometimes square', ['✗', '✓']), ('a full moon is bright', ['✓', '✗'])], o='O3'),
 YN('Does the word "month" come from the word "Moon"?', True, 'O3', pic='📅', why='Yes!'),
 PM('Tonight is a full moon. About when will the next full moon be?', ('📅', 'In about a month'), [('⏰', 'Tomorrow', 'About a month later.'), ('🎂', 'Next year', 'About a month later.')], 'O3'),
 PM('Why do we see the Moon\'s phases?', ('🔄', 'The Moon moves round the Earth'), [('🍪', 'Someone eats it', 'It moves round the Earth.'), ('☁️', 'Clouds cut it', 'It moves round the Earth.')], 'O3'),
 PM('About two weeks after a new moon, you see…', ('🌕', 'a full moon'), [('🌑', 'another new moon', 'Two weeks after new comes full.'), ('🌙', 'nothing ever again', 'It keeps changing.')], 'O3', d='H'),
 YN('Can a Moon diary show the phases changing?', True, 'O3', pic='📔', why='Yes. Draw the Moon each night.'),
)
s.adv(
 PM('* Advanced. After a full moon, the bright part…', ('📉', 'gets smaller each night'), [('📈', 'keeps getting bigger', 'It gets smaller after full.'), ('⏸️', 'stays the same', 'It gets smaller after full.')], 'O3', d='H'),
 PM('* Advanced. Why can\'t we see a new moon?', ('🌑', 'Its lit side faces away from us'), [('💤', 'It is asleep', 'Its lit side faces away.'), ('🚫', 'It has gone away', 'It is still there.')], 'O3', d='VH'),
 OD('* Advanced. Order the whole pattern.', ['new moon', 'growing half moon', 'full moon', 'shrinking half moon', 'new moon again'], o='O3', d='VH'),
)
s.labs('Moon diary lab',
 sort_lab('Getting bigger or smaller?', 'Sort each Moon phase picture.', ['Lit part getting bigger', 'Lit part getting smaller'],
  [('new moon to crescent', '🌒', 0, 'The lit part grows.'), ('full moon to half', '🌗', 1, 'The lit part shrinks.'), ('crescent to half', '🌓', 0, 'The lit part grows.'), ('half to thin crescent', '🌘', 1, 'The lit part shrinks.')],
  [PM('What comes between a crescent and a full moon?', ('🌓', 'A half moon'), [('🌑', 'A new moon', 'Half moon comes next.')], 'O3')]),
 home('Moon diary', 'Watch the Moon for two weeks.', ['a notebook', 'a pencil', 'a window', 'an adult'], ['Only go outside at night with an adult.'],
  ['Find the Moon each night.', 'Draw its shape.', 'Do this for two weeks.'],
  ['Night', 'Moon shape'], [('first night', ['crescent', 'half', 'full']), ('one week later', ['crescent', 'half', 'full']), ('two weeks later', ['crescent', 'half', 'full'])],
  [PM('Did the Moon seem to change shape?', ('👍', 'Yes'), [('👎', 'No', 'The phases changed.')], 'O3')]))

U.mindmap(('Spheres', 'Earth, Sun and Moon are round', 'O1', '6.1'), ('The Moon', 'orbits the Earth; craters', 'O2', '6.2'), ('Phases', 'new, crescent, half, full', 'O3', '6.3'))
