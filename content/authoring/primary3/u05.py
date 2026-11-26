# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 3 · Unit 5 Forces and magnets. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit3 import *

OBJ = {
 'O1': {'sec': '5.1', 'code': 'Physics', 'codeNote': '', 't': 'Know that a force is a push or a pull, what forces can do, and that a forcemeter measures forces.'},
 'O2': {'sec': '5.2', 'code': 'Physics', 'codeNote': '', 't': 'Know that gravity pulls things down towards the Earth.'},
 'O3': {'sec': '5.3', 'code': 'Physics', 'codeNote': '', 't': 'Know that friction slows things down, and is bigger on rough surfaces.'},
 'O4': {'sec': '5.4', 'code': 'Physics', 'codeNote': '', 't': 'Know that magnets attract and repel, and have north and south poles.'},
 'O5': {'sec': '5.5', 'code': 'Physics', 'codeNote': '', 't': 'Sort materials into magnetic and non-magnetic, and know that not all metals are magnetic.'},
}
U = YUnit(5, 'Forces and magnets', 'Physics: forces', 'Pushes and pulls, gravity, friction, magnets and magnetic materials.', OBJ)

# ============================================================  5.1
s = U.section('5.1', 'Pushes and pulls', ['O1']); s.words(V['5.1']); core(s, 'O1')
s.stop(PM('When you open a drawer, is that a push or a pull?', ('🪢', 'A pull'), [('🫸', 'A push', 'You move it towards you.')], 'O1'),
       PM('When you close a drawer, is that a push or a pull?', ('🫸', 'A push'), [('🪢', 'A pull', 'You move it away from you.')], 'O1'))
s.stop(PM('Which one is a push?', ('🛒', 'Moving a shopping trolley forwards'), [('🪢', 'Tug of war', 'That is a pull.'), ('🐕', 'A dog on a lead pulling', 'That is a pull.')], 'O1'),
       PM('Which one is a pull?', ('🚪', 'Opening a door towards you'), [('⚽', 'Kicking a ball', 'That is a push.'), ('🛝', 'Pushing a swing', 'That is a push.')], 'O1'))
s.prac(
 GD('Push or pull?', 'Force', [('⚽ kicking a ball', 'push'), ('🪢 tug of war', 'pull'), ('🛒 moving a trolley', 'push'), ('🧦 pulling on a sock', 'pull'), ('🔔 pressing a doorbell', 'push')], o='O1'),
 PM('You squash play dough. What did the force do?', ('🫓', 'Changed its shape'), [('🌈', 'Changed its colour', 'Forces can change shape.'), ('🔊', 'Made it sing', 'Forces can change shape.')], 'O1'),
 PM('What does a forcemeter measure?', ('⚖️', 'Forces'), [('🌡️', 'Temperature', 'It measures forces.'), ('📏', 'Length only', 'It measures forces.')], 'O1'),
 YN('Can a force make a moving ball stop?', True, 'O1', pic='⚽', why='Yes. A goalkeeper uses a force to stop the ball.'),
 PM('You throw a ball to a friend. Which force did you use?', ('🫸', 'A push'), [('🪢', 'A pull', 'You pushed it away.'), ('🤷', 'No force', 'You pushed it.')], 'O1'),
 MT('Match each word to what it means.', [('push', 'move something away'), ('pull', 'move something towards you'), ('force', 'a push or a pull')], o='O1'),
 TK('Tick what forces can do.', ['Can', 'Cannot'], [('start something moving', ['✓', '✗']), ('change its shape', ['✓', '✗']), ('make it invisible', ['✗', '✓'])], o='O1'),
 PM('A football hits a wall and bounces back. What changed?', ('↪️', 'Its direction'), [('🎨', 'Its colour', 'Its direction changed.'), ('📏', 'Its size', 'Its direction changed.')], 'O1'),
 YN('Is a bigger pull shown by a bigger number on a forcemeter?', True, 'O1', pic='⚖️', why='Yes. The spring stretches more.'),
 OD('Order from the smallest pull to the biggest.', ['lifting a feather', 'lifting a book', 'lifting a full school bag'], o='O1'),
 PM('How do you make a swing go higher?', ('🫸', 'Push it harder'), [('🪢', 'Pull it backwards and let go softly', 'A harder push makes it go higher.'), ('😴', 'Wait', 'Push harder.')], 'O1', d='H'),
 YN('Does a fridge door need a pull to open?', True, 'O1', pic='🧊', why='Yes. You pull it towards you.'),
)
s.adv(
 PM('* Advanced. Two teams pull a rope with the same force. What happens?', ('⏸️', 'The rope does not move'), [('➡️', 'It moves left', 'Equal pulls balance.'), ('💥', 'It breaks at once', 'Equal pulls balance.')], 'O1', d='VH'),
 PM('* Advanced. Why does a heavy bag pull the forcemeter spring down further?', ('🎒', 'It needs a bigger force to hold it'), [('🎨', 'It is more colourful', 'It needs more force.'), ('🌬️', 'Wind pushes it', 'It needs more force.')], 'O1', d='H'),
 OD('* Advanced. Order the forcemeter readings, smallest first.', ['a pencil', 'an apple', 'a dictionary'], o='O1', d='H'),
)
s.labs('Forcemeter lab',
 test_lab('Forcemeter test', 'Hook different things on a forcemeter. Read the pull in newtons.', 'Thing', 'Pull', 'newtons', 10, 1,
  'Tap the number the bar reaches.', [('a pencil case', '✏️', 2), ('a lunch box', '🍱', 5), ('a school bag', '🎒', 9)],
  [PM('Which needed the biggest pull?', ('🎒', 'The school bag'), [('✏️', 'The pencil case', 'It was the lightest.')], 'O1')]),
 home('Push or pull hunt', 'Find pushes and pulls at home.', ['your home', 'an adult'], ['Be careful near hot ovens and doors.'],
  ['Open and close things at home.', 'Decide: push or pull?'],
  ['Action', 'Push or pull?'], [('open the fridge', ['push', 'pull']), ('close a drawer', ['push', 'pull']), ('press a light switch', ['push', 'pull'])],
  [PM('Opening the fridge is a…', ('🪢', 'pull'), [('🫸', 'push', 'You move the door towards you.')], 'O1')]))

# ============================================================  5.2
s = U.section('5.2', 'Gravity', ['O2']); s.words(V['5.2']); core(s, 'O2')
s.stop(PM('What force pulls things down to the ground?', ('🌍', 'Gravity'), [('🧲', 'Magnetism', 'Gravity pulls everything down.'), ('🌬️', 'Wind', 'Gravity pulls everything down.')], 'O2'),
       PM('Why does an apple fall from a tree?', ('⬇️', 'Gravity pulls it down'), [('🌙', 'The Moon pushes it', 'Gravity pulls it.'), ('🐦', 'Birds push it', 'Gravity pulls it.')], 'O2'))
s.stop(PM('What happens to a ball when you let go of it?', ('⬇️', 'It falls down'), [('⬆️', 'It floats up', 'Gravity pulls it down.'), ('⏸️', 'It stays in the air', 'Gravity pulls it down.')], 'O2'),
       PM('You jump up. What brings you back down?', ('🌍', 'Gravity'), [('🧲', 'A magnet', 'Gravity pulls you.'), ('🌬️', 'The air', 'Gravity pulls you.')], 'O2'))
s.prac(
 YN('Does gravity pull things down?', True, 'O2', pic='⬇️', why='Yes. Towards the Earth.'),
 GD('Is gravity at work?', 'Gravity?', [('🌧️ rain falling', 'yes'), ('🍂 leaves falling', 'yes'), ('🛝 sliding down a slide', 'yes')], o='O2'),
 PM('Where is gravity weaker than on the Earth?', ('🌙', 'On the Moon'), [('🏠', 'In your house', 'Gravity is the same at home.'), ('🏫', 'At school', 'Gravity is the same at school.')], 'O2'),
 PM('Why can astronauts jump very high on the Moon?', ('🌙', 'The Moon\'s gravity is weaker'), [('👟', 'They have springy shoes', 'Gravity is weaker.'), ('🌬️', 'It is very windy', 'Gravity is weaker.')], 'O2'),
 MT('Match each word to what it means.', [('gravity', 'pulls things down'), ('fall', 'drop down'), ('float', 'stay up')], o='O2'),
 TK('Tick what is true.', ['True', 'False'], [('gravity keeps us on the ground', ['✓', '✗']), ('gravity pushes things up', ['✗', '✓']), ('a dropped cup falls', ['✓', '✗'])], o='O2'),
 PM('You drop a ball and a flat sheet of paper. Which lands first?', ('⚽', 'The ball'), [('📄', 'The flat paper', 'Air slows the paper.')], 'O2'),
 PM('Now you scrunch the paper into a ball. What happens?', ('⚡', 'It falls faster'), [('🐢', 'It falls slower', 'Less air pushes on it.'), ('⬆️', 'It floats up', 'Gravity still pulls it.')], 'O2'),
 YN('Does water run downhill because of gravity?', True, 'O2', pic='💧', why='Yes.'),
 OD('Order what happens when you throw a ball up.', ['it goes up', 'it slows down', 'it stops at the top', 'it falls down'], o='O2'),
 PM('Why do we hold a cup carefully over the table?', ('⬇️', 'If we let go, gravity pulls it down'), [('🧲', 'The table is a magnet', 'Gravity pulls it.'), ('🎵', 'Cups like music', 'Gravity pulls it.')], 'O2', d='H'),
 YN('Do things float in a spaceship far out in space?', True, 'O2', pic='🧑‍🚀', why='Yes, they seem to float.'),
)
s.adv(
 PM('* Advanced. A parachute makes a person fall more slowly. Why?', ('🪂', 'Air pushes up on the big canopy'), [('🧲', 'It is magnetic', 'Air pushes up on it.'), ('🌍', 'It turns gravity off', 'Gravity still pulls.')], 'O2', d='VH'),
 PM('* Advanced. Which way does gravity pull for children on the other side of the world?', ('🌍', 'Towards the middle of the Earth'), [('⬆️', 'Up into space', 'Towards the Earth.'), ('➡️', 'Sideways', 'Towards the Earth.')], 'O2', d='VH'),
 OD('* Advanced. Order the jumps, highest first.', ['on the Moon', 'on the Earth', 'with a heavy bag on the Earth'], o='O2', d='H'),
)
s.labs('Drop lab',
 test_lab('Drop test', 'Drop things from the same height. Count slowly until each one lands.', 'Thing dropped', 'Time to land', 'counts', 10, 1,
  'Tap the number the bar reaches.', [('a ball', '⚽', 1), ('scrunched paper', '🧻', 2), ('flat paper', '📄', 5)],
  [PM('Which took the longest to land?', ('📄', 'The flat paper'), [('⚽', 'The ball', 'It landed first.')], 'O2')]),
 home('Drop test', 'Drop things and watch gravity.', ['a ball', 'two sheets of paper', 'an adult'], ['Only drop soft, safe things.'],
  ['Drop a ball and a flat sheet together.', 'Scrunch one sheet into a ball.', 'Drop both sheets together.'],
  ['Test', 'Which landed first?'], [('ball or flat paper', ['ball', 'flat paper']), ('scrunched or flat paper', ['scrunched', 'flat paper'])],
  [PM('What pulled everything down?', ('🌍', 'Gravity'), [('🧲', 'A magnet', 'Gravity did.')], 'O2')]))

# ============================================================  5.3
s = U.section('5.3', 'Friction', ['O3']); s.words(V['5.3']); core(s, 'O3')
s.stop(PM('Which surface has the most friction?', ('🟫', 'A rough carpet'), [('🧊', 'Smooth ice', 'Ice is slippery.'), ('🪞', 'A glass mirror', 'Glass is smooth.')], 'O3'),
       PM('A toy car rolls furthest on…', ('🧊', 'a smooth floor'), [('🟫', 'a rough carpet', 'Carpet slows it more.'), ('🌱', 'long grass', 'Grass slows it more.')], 'O3'))
s.stop(PM('Why do shoes have bumpy bottoms?', ('👟', 'To grip the floor so we do not slip'), [('🎨', 'To look nice', 'They give grip.'), ('🔊', 'To be noisy', 'They give grip.')], 'O3'),
       PM('Which shoe would be best on a slippery path?', ('🥾', 'A boot with deep bumps'), [('🩰', 'A smooth ballet shoe', 'You need grip.'), ('🧦', 'Just socks', 'You need grip.')], 'O3'))
s.prac(
 YN('Does friction slow things down?', True, 'O3', pic='🛑', why='Yes.'),
 GD('Lots of friction or little?', 'Friction', [('🧊 ice', 'little'), ('🟫 carpet', 'lots'), ('🪨 sandpaper', 'lots'), ('🪞 glass', 'little')], o='O3'),
 PM('You rub your hands together fast. What happens?', ('🔥', 'They get warm'), [('🧊', 'They get cold', 'Friction makes heat.'), ('🌈', 'They change colour', 'Friction makes heat.')], 'O3'),
 PM('What do bike brakes use to stop the bike?', ('🛑', 'Friction'), [('🧲', 'Magnets', 'They rub on the wheel.'), ('🎈', 'Balloons', 'They rub on the wheel.')], 'O3'),
 MT('Match each word to what it means.', [('friction', 'slows things down'), ('rough', 'bumpy'), ('smooth', 'flat and even')], o='O3'),
 TK('Tick where friction helps us.', ['Helps', 'Does not'], [('shoes on the floor', ['✓', '✗']), ('holding a pencil', ['✓', '✗']), ('slipping on ice', ['✗', '✓'])], o='O3'),
 PM('Why is it easy to slide on ice?', ('🧊', 'Ice is smooth: little friction'), [('🔥', 'Ice is hot', 'Ice is smooth.'), ('🟫', 'Ice is rough', 'Ice is smooth.')], 'O3'),
 OD('Order from the furthest roll to the shortest.', ['smooth wood', 'thin carpet', 'thick towel'], o='O3'),
 YN('Would it be easy to walk with no friction at all?', False, 'O3', pic='🚶', why='No. You would slip everywhere!'),
 PM('Why do people put grit on icy roads?', ('🪨', 'To make them rougher, with more friction'), [('🍬', 'To make them sweet', 'For more friction.'), ('🎨', 'To make them pretty', 'For more friction.')], 'O3'),
 PM('A ramp is covered with a towel. The toy car goes…', ('🐢', 'slower'), [('⚡', 'faster', 'The towel adds friction.'), ('⬆️', 'up the ramp', 'It goes slower.')], 'O3', d='H'),
 YN('Does a slide need to be smooth to be fun?', True, 'O3', pic='🛝', why='Yes. Smooth means less friction.'),
)
s.adv(
 PM('* Advanced. Why do racing cyclists wear smooth suits?', ('🚴', 'Less air rubbing, so they go faster'), [('🎨', 'They look shiny', 'Less friction with the air.'), ('🧲', 'Smooth suits are magnetic', 'Less friction with the air.')], 'O3', d='VH'),
 PM('* Advanced. Why does a ball rolling on grass stop sooner than on a path?', ('🌱', 'Grass gives more friction'), [('🌍', 'Gravity is stronger on grass', 'Friction is bigger.'), ('💨', 'The wind is stronger', 'Friction is bigger.')], 'O3', d='H'),
 GD('* Advanced. Do we want more or less friction?', 'Want', [('👟 football boots', 'more'), ('⛸️ ice skates', 'less'), ('🛑 bike brakes', 'more')], o='O3', d='H'),
)
s.labs('Ramp lab',
 test_lab('Ramp race', 'Roll a toy car down a ramp onto different floors. Read how far it rolls.', 'Floor', 'Distance', 'cm', 100, 10,
  'Tap the number the bar reaches.', [('towel', '🧺', 20), ('carpet', '🟫', 50), ('smooth wood', '🪵', 90)],
  [PM('Which floor had the most friction?', ('🧺', 'The towel'), [('🪵', 'Smooth wood', 'The car rolled furthest there.')], 'O3')]),
 home('Ramp race', 'Test friction with a toy car.', ['a toy car', 'a board', 'some books', 'a towel'], ['Keep the ramp low and steady.'],
  ['Make a ramp with the board and books.', 'Roll the car down.', 'Cover the ramp with a towel and roll again.'],
  ['Ramp', 'How far did it go?'], [('plain board', ['far', 'not far']), ('with a towel', ['far', 'not far'])],
  [PM('Why did the car go less far with the towel?', ('🧺', 'More friction'), [('🌍', 'Less gravity', 'More friction slowed it.')], 'O3')]))

# ============================================================  5.4
s = U.section('5.4', 'Amazing magnets', ['O4']); s.words(V['5.4']); core(s, 'O4')
s.stop(PM('What does attract mean?', ('🧲', 'Pull towards'), [('↔️', 'Push away', 'That is repel.'), ('🎨', 'Change colour', 'It means pull towards.')], 'O4'),
       PM('A magnet attracts a paper clip. The clip…', ('📎', 'moves towards the magnet'), [('🏃', 'moves away', 'Attract means pull towards.'), ('🧊', 'freezes', 'It moves towards it.')], 'O4'))
s.stop(PM('What happens when two north poles meet?', ('↔️', 'They push apart'), [('🤝', 'They snap together', 'Same poles repel.'), ('🔥', 'They get hot', 'Same poles repel.')], 'O4'),
       PM('A north pole and a south pole come close. What happens?', ('🤝', 'They pull together'), [('↔️', 'They push apart', 'Different poles attract.')], 'O4'))
s.prac(
 GD('Attract or repel?', 'What happens', [('N + S', 'attract'), ('N + N', 'repel'), ('S + S', 'repel'), ('S + N', 'attract')], o='O4'),
 PM('Where is a magnet strongest?', ('🔴', 'At its poles (ends)'), [('⚪', 'In the middle', 'The ends are strongest.'), ('🤷', 'The same everywhere', 'The ends are strongest.')], 'O4'),
 YN('Can a magnet pull a paper clip without touching it?', True, 'O4', pic='📎', why='Yes. Magnets work from a distance.'),
 PM('What does a compass needle point to?', ('⬆️', 'North'), [('⬇️', 'Always down', 'It points north.'), ('🌙', 'The Moon', 'It points north.')], 'O4'),
 MT('Match each word to what it means.', [('attract', 'pull towards'), ('repel', 'push away'), ('pole', 'an end of a magnet')], o='O4'),
 TK('Tick what is true.', ['True', 'False'], [('a magnet has two poles', ['✓', '✗']), ('same poles attract', ['✗', '✓']), ('fridge magnets hold up pictures', ['✓', '✗'])], o='O4'),
 PM('Why does a fridge door stay shut?', ('🧲', 'There is a magnet in the seal'), [('🧊', 'Ice glues it', 'A magnet holds it.'), ('🔑', 'It is locked', 'A magnet holds it.')], 'O4'),
 PM('You go magnet fishing. Paper fish need a… to be caught.', ('📎', 'paper clip'), [('🧻', 'tissue', 'Tissue is not magnetic.'), ('🧽', 'sponge', 'A sponge is not magnetic.')], 'O4'),
 YN('Do two south poles repel?', True, 'O4', pic='↔️', why='Yes. The same poles repel.'),
 OD('Order magnet fishing steps.', ['cut out paper fish', 'put a paper clip on each', 'tie a magnet to a string', 'go fishing'], o='O4'),
 PM('Which is the strongest magnet? It picks up the most…', ('📎', 'paper clips'), [('🧸', 'teddies', 'Count paper clips.'), ('🍎', 'apples', 'Count paper clips.')], 'O4', d='H'),
 YN('Is the Earth like a giant magnet?', True, 'O4', pic='🌍', why='Yes! That is why compasses work.'),
)
s.adv(
 PM('* Advanced. You hold two magnets and feel a push. What is facing?', ('🔴', 'Two of the same pole'), [('🤝', 'A north and a south', 'They would attract.'), ('🤷', 'Nothing', 'Same poles repel.')], 'O4', d='VH'),
 PM('* Advanced. A magnet picks up 3 clips at its end but 0 in its middle. Why?', ('🔴', 'The poles are strongest'), [('🌍', 'Gravity is stronger in the middle', 'Poles are strongest.'), ('🎨', 'The middle is painted', 'Poles are strongest.')], 'O4', d='H'),
 OD('* Advanced. Order the magnets by strength, weakest first.', ['picks up 2 clips', 'picks up 6 clips', 'picks up 11 clips'], o='O4', d='H'),
)
s.labs('Magnet strength lab',
 test_lab('Magnet strength', 'Count how many paper clips each magnet can hold in a chain.', 'Magnet', 'Paper clips', 'clips', 12, 1,
  'Tap the number the bar reaches.', [('fridge magnet', '🧊', 2), ('bar magnet', '🧲', 6), ('horseshoe magnet', '🧲', 10)],
  [PM('Which magnet was the strongest?', ('🧲', 'The horseshoe magnet'), [('🧊', 'The fridge magnet', 'It held the fewest.')], 'O4')]),
 home('Magnet fishing', 'Catch paper fish with a magnet.', ['paper', 'paper clips', 'a magnet', 'string', 'a stick'], ['Keep magnets away from phones and small children.'],
  ['Cut out paper fish and add a paper clip to each.', 'Tie the magnet to the string and stick.', 'Go fishing!'],
  ['Question', 'My answer'], [('did the magnet catch the fish?', ['yes', 'no']), ('did it work without the clip?', ['yes', 'no'])],
  [PM('What did the magnet attract?', ('📎', 'The paper clips'), [('📄', 'The paper', 'Paper is not magnetic.')], 'O4')]))

# ============================================================  5.5
s = U.section('5.5', 'Magnetic materials', ['O5']); s.words(V['5.5']); core(s, 'O5')
s.stop(PM('Which one will stick to a magnet?', ('🔩', 'A steel nail'), [('🪵', 'A wooden block', 'Wood is not magnetic.'), ('🧴', 'A plastic bottle', 'Plastic is not magnetic.')], 'O5'),
       PM('Which material is magnetic?', ('⚙️', 'Iron'), [('📄', 'Paper', 'Paper is not magnetic.'), ('🧶', 'Wool', 'Wool is not magnetic.')], 'O5'))
s.stop(PM('Are all metals magnetic?', ('👎', 'No'), [('👍', 'Yes', 'Gold and aluminium are not magnetic.')], 'O5'),
       PM('Which metal is NOT magnetic?', ('🥤', 'Aluminium (drinks cans)'), [('⚙️', 'Iron', 'Iron is magnetic.'), ('🔩', 'Steel', 'Steel is magnetic.')], 'O5'))
s.prac(
 GD('Magnetic or not?', 'Magnetic?', [('📎 paper clip', 'yes'), ('🪵 wood', 'no'), ('🥫 steel food can', 'yes'), ('🧴 plastic', 'no'), ('🥇 gold ring', 'no')], o='O5'),
 YN('Does a plastic ruler stick to a magnet?', False, 'O5', pic='📏', why='No. Plastic is non-magnetic.'),
 PM('Can a magnet pull a paper clip through a sheet of paper?', ('👍', 'Yes'), [('👎', 'No', 'Magnets work through paper.')], 'O5'),
 PM('Recycling centres pull out steel cans with…', ('🧲', 'giant magnets'), [('🧹', 'brooms', 'Steel is magnetic.'), ('🕸️', 'sieves', 'Steel is magnetic.')], 'O5'),
 MT('Match each word to what it means.', [('magnetic', 'sticks to a magnet'), ('steel', 'a metal made from iron'), ('non-magnetic', 'does not stick')], o='O5'),
 TK('Tick the magnetic things.', ['Magnetic', 'Not magnetic'], [('a steel spoon', ['✓', '✗']), ('a glass marble', ['✗', '✓']), ('an iron nail', ['✓', '✗'])], o='O5'),
 PM('You drop pins on the carpet. What is best to pick them up?', ('🧲', 'A magnet'), [('🧻', 'A tissue', 'Use a magnet.'), ('🥄', 'A plastic spoon', 'Use a magnet.')], 'O5'),
 OD('Order the magnet test.', ['guess: will it stick?', 'hold the magnet near it', 'write magnetic or not'], o='O5'),
 YN('Is a copper coin magnetic?', False, 'O5', pic='🟤', why='No. Copper is not magnetic.'),
 PM('A drinks can does not stick to a magnet. What is it made of?', ('🥤', 'Aluminium'), [('🔩', 'Steel', 'Steel would stick.'), ('⚙️', 'Iron', 'Iron would stick.')], 'O5'),
 PM('Can a magnet pull through water?', ('💧', 'Yes'), [('🚫', 'No', 'It can pull through water.')], 'O5', d='H'),
 YN('Is every shiny thing magnetic?', False, 'O5', pic='✨', why='No. You have to test it.'),
)
s.adv(
 PM('* Advanced. How could you separate steel and aluminium cans?', ('🧲', 'Use a magnet: steel sticks'), [('🕸️', 'Use a sieve', 'They are the same size.'), ('💧', 'Put them in water', 'Use a magnet.')], 'O5', d='H'),
 PM('* Advanced. A magnet holds a paper clip through 1 sheet but not through 30 sheets. Why?', ('📚', 'The pull gets weaker further away'), [('🔥', 'The paper got hot', 'It is further away.'), ('🧊', 'Paper is magnetic', 'It is further away.')], 'O5', d='VH'),
 GD('* Advanced. Metal: magnetic or not?', 'Magnetic?', [('⚙️ iron', 'yes'), ('🥇 gold', 'no'), ('🔩 steel', 'yes')], o='O5', d='H'),
)
s.labs('Magnet sort lab',
 sort_lab('Magnet sort', 'Test each thing with a magnet.', ['Magnetic', 'Not magnetic'],
  [('steel spoon', '🥄', 0, 'Steel is magnetic.'), ('pencil', '✏️', 1, 'Wood is not.'), ('key', '🔑', 0, 'This key is steel.'), ('sock', '🧦', 1, 'Cloth is not.'), ('nail', '🔩', 0, 'Iron is magnetic.'), ('drinks can', '🥤', 1, 'Aluminium is not.')],
  [PM('Which metal thing was NOT magnetic?', ('🥤', 'The drinks can'), [('🔩', 'The nail', 'The nail stuck.')], 'O5')]),
 home('Magnet sort', 'Test things at home.', ['a magnet', 'ten small things', 'an adult'], ['Keep magnets away from phones and computers.'],
  ['Guess if each thing will stick.', 'Test it with the magnet.', 'Sort into two groups.'],
  ['Thing', 'Did it stick?'], [('a spoon', ['yes', 'no']), ('a pencil', ['yes', 'no']), ('a coin', ['yes', 'no'])],
  [PM('What do magnetic things have in them?', ('⚙️', 'Iron'), [('🪵', 'Wood', 'Iron makes them magnetic.')], 'O5')]))

U.mindmap(('Forces', 'pushes and pulls', 'O1', '5.1'), ('Gravity', 'pulls things down', 'O2', '5.2'), ('Friction', 'slows things down', 'O3', '5.3'),
          ('Magnets', 'attract and repel', 'O4', '5.4'), ('Magnetic materials', 'iron and steel', 'O5', '5.5'))
