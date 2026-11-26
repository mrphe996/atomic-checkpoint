# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 4 · Unit 5 Light. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit4 import *

OBJ = {
 'O1': {'sec': '5.1', 'code': 'Physics', 'codeNote': '', 't': 'Know that we need light to see, name light sources, and know that light bounces off objects into our eyes.'},
 'O2': {'sec': '5.2', 'code': 'Physics', 'codeNote': '', 't': 'Know that light travels in straight lines and cannot bend round corners.'},
 'O3': {'sec': '5.3', 'code': 'Physics', 'codeNote': '', 't': 'Know that light reflects, that shiny surfaces reflect more light, and why reflectors keep us safe.'},
 'O4': {'sec': '5.4', 'code': 'Earth and Space', 'codeNote': '', 't': 'Know that the Sun is a star and a light source, and that planets and moons reflect sunlight.'},
 'O5': {'sec': '5.5', 'code': 'Earth and Space', 'codeNote': '', 't': 'Explain day and night by the spinning of the Earth.'},
 'O6': {'sec': '5.6', 'code': 'Physics', 'codeNote': '', 't': 'Know that shadows form when light is blocked, and that shadow length changes during the day.'},
}
U = YUnit(5, 'Light', 'Physics: light', 'Seeing, straight rays, mirrors, the Sun and the Moon, day and night, and shadows.', OBJ)

# ============================================================  5.1
s = U.section('5.1', 'How we see things', ['O1']); s.words(V['5.1']); core(s, 'O1')
s.stop(PM('Which of these is a light source?', ('🔦', 'A torch'), [('🪞', 'A mirror', 'A mirror only reflects light.'), ('🌙', 'The Moon', 'The Moon reflects sunlight.')], 'O1'),
       PM('Which of these gives out its own light?', ('☀️', 'The Sun'), [('📘', 'A book', 'A book reflects light.'), ('🥄', 'A spoon', 'A spoon reflects light.')], 'O1'))
s.stop(PM('Why can\'t we see anything in a completely dark room?', ('🌑', 'There is no light to go into our eyes'), [('😴', 'Our eyes are asleep', 'Eyes need light.'), ('📏', 'The room is too big', 'Eyes need light.')], 'O1'),
       PM('What do our eyes need to see?', ('💡', 'Light'), [('🔊', 'Sound', 'Ears need sound.'), ('🔥', 'Heat', 'Eyes need light.')], 'O1'))
s.prac(
 GD('Light source or not?', 'Light source?', [('☀️ the Sun', 'yes'), ('💡 a lamp', 'yes'), ('🪞 a mirror', 'no'), ('🕯️ a candle', 'yes'), ('🌙 the Moon', 'no')], o='O1'),
 OD('Put in order: how you see a book.', ['light comes from a lamp', 'it bounces off the book', 'it goes into your eyes'], o='O1'),
 YN('Is the Moon a light source?', False, 'O1', pic='🌙', why='No. It reflects light from the Sun.'),
 PM('Which part of your body do you see with?', ('👀', 'Your eyes'), [('👂', 'Your ears', 'Ears are for hearing.'), ('👃', 'Your nose', 'Your nose is for smelling.')], 'O1'),
 PM('You wake up at night. Your room is dark. What can you do to see your toys?', ('💡', 'Switch on a light'), [('😑', 'Close your eyes', 'You need light.'), ('🔊', 'Make a noise', 'You need light.')], 'O1'),
 MT('Match each word to what it means.', [('light source', 'gives out its own light'), ('dark', 'no light'), ('eye', 'what we see with')], o='O1'),
 TK('Tick the light sources.', ['Yes', 'No'], [('a torch', ['✓', '✗']), ('a TV screen', ['✓', '✗']), ('a white wall', ['✗', '✓'])], o='O1'),
 PM('Why do cars have headlights?', ('🚗', 'So drivers can see in the dark'), [('🎨', 'To look pretty', 'Headlights help drivers see.'), ('🔊', 'To make noise', 'Headlights help drivers see.')], 'O1'),
 YN('Can you see a red ball in total darkness?', False, 'O1', pic='⚽', why='No. Without light, nothing can bounce into your eyes.'),
 PM('Which is NOT a light source?', ('🪙', 'A shiny coin'), [('🔥', 'A fire', 'A fire gives light.'), ('⚡', 'Lightning', 'Lightning gives light.')], 'O1', d='H'),
 PM('Fireflies are tiny insects. Why can we see them at night?', ('✨', 'They make their own light'), [('🌙', 'The Moon lights them', 'They glow by themselves.'), ('🔊', 'They are loud', 'They glow.')], 'O1'),
 PM('Which is the biggest light source for the Earth?', ('☀️', 'The Sun'), [('💡', 'A lamp', 'The Sun is much bigger.'), ('🕯️', 'A candle', 'The Sun is much bigger.')], 'O1'),
)
s.adv(
 PM('* Advanced. Why can you read a book in a room lit by a lamp?', ('💡', 'Light from the lamp reflects off the page into your eyes'), [('👀', 'Light comes out of your eyes', 'Light goes into your eyes.'), ('📘', 'The book makes light', 'The book reflects light.')], 'O1', d='H'),
 PM('* Advanced. Why do cats see better than us at night?', ('🐱', 'Their eyes let in more light'), [('🔦', 'They carry torches', 'Their eyes collect more light.'), ('👂', 'They have big ears', 'It is about their eyes.')], 'O1', d='VH'),
 OD('* Advanced. Order from brightest to dimmest.', ['the Sun', 'a lamp', 'a candle'], o='O1', d='H'),
)
s.labs('Light lab',
 sort_lab('Light source or not?', 'Sort each thing.', ['Light source', 'Not a light source'],
  [('Sun', '☀️', 0, 'The Sun gives out light.'), ('Moon', '🌙', 1, 'The Moon reflects sunlight.'), ('torch', '🔦', 0, 'A torch makes light.'), ('mirror', '🪞', 1, 'A mirror reflects light.'), ('candle', '🕯️', 0, 'A flame gives light.'), ('book', '📘', 1, 'A book reflects light.')],
  [PM('Which is not a light source?', ('🌙', 'The Moon'), [('☀️', 'The Sun', 'The Sun makes light.')], 'O1')]),
 home('Dark box', 'See what happens without light.', ['a shoe box with a lid', 'a small toy', 'a torch'], ['Ask an adult to make a small hole in the box.'],
  ['Put the toy in the box and close the lid.', 'Look through a small hole.', 'Open a flap to let light in.'],
  ['Box', 'Could I see the toy?'], [('closed', ['yes', 'no']), ('with a flap open', ['yes', 'no'])],
  [PM('Why could you see the toy with the flap open?', ('💡', 'Light got in'), [('📦', 'The box got bigger', 'Light got in.')], 'O1')]))

# ============================================================  5.2
s = U.section('5.2', 'Light travels in straight lines', ['O2']); s.words(V['5.2']); core(s, 'O2')
s.stop(PM('How does light travel?', ('📏', 'In straight lines'), [('〰️', 'In wiggly lines', 'Light goes straight.'), ('🌀', 'In circles', 'Light goes straight.')], 'O2'),
       PM('What do we call a straight line of light?', ('➡️', 'A ray'), [('🌧️', 'A rain', 'It is a ray.'), ('🧵', 'A string', 'It is a ray.')], 'O2'))
s.stop(PM('Can light bend round a corner?', ('🚫', 'No'), [('✅', 'Yes', 'Light goes straight, so it cannot.')], 'O2'),
       PM('You hide behind a wall. Can your friend\'s torch light reach you?', ('🙈', 'No – light goes straight'), [('🔦', 'Yes – light bends round', 'Light cannot bend round corners.')], 'O2'))
s.prac(
 YN('Does a torch beam go in a straight line?', True, 'O2', pic='🔦', why='Yes. Light travels in straight lines.'),
 PM('In a forest you can see sunbeams between the trees. What shape are they?', ('📏', 'Straight'), [('〰️', 'Wiggly', 'Light goes straight.'), ('🌀', 'Curly', 'Light goes straight.')], 'O2'),
 PM('Three cards have holes. When can you see the torch light through them?', ('🎯', 'When the holes are in a straight line'), [('↪️', 'When the holes are in a curve', 'Light goes straight.'), ('🙅', 'Never', 'In a line, you can.')], 'O2'),
 PM('Which is the fastest thing there is?', ('⚡', 'Light'), [('🐆', 'A cheetah', 'Light is much faster.'), ('🚀', 'A rocket', 'Light is much faster.')], 'O2'),
 MT('Match each word to what it means.', [('ray', 'a thin line of light'), ('beam', 'light from a torch'), ('straight', 'does not bend')], o='O2'),
 YN('Does light from the Sun reach us in about 8 minutes?', True, 'O2', pic='☀️', why='Yes – it is very fast!'),
 TK('Tick what is true.', ['True', 'False'], [('light goes in straight lines', ['✓', '✗']), ('light bends round corners', ['✗', '✓']), ('light is very fast', ['✓', '✗'])], o='O2'),
 PM('Why do we draw light as straight arrows?', ('➡️', 'Light travels in straight lines'), [('✏️', 'Curves are hard to draw', 'Light really goes straight.'), ('🎨', 'Arrows look nice', 'Light really goes straight.')], 'O2'),
 GD('Will the light reach the eye?', 'Reaches?', [('👀 nothing in the way', 'yes'), ('🧱 a wall in the way', 'no'), ('↪️ light must turn a corner', 'no')], o='O2'),
 PM('A lighthouse beam shines out to sea. What path does it take?', ('📏', 'A straight path'), [('〰️', 'A wavy path', 'Light goes straight.')], 'O2'),
 PM('Why can\'t you see round a corner?', ('📐', 'Light cannot bend round corners'), [('👀', 'Eyes are too small', 'It is about light.'), ('🌑', 'Corners are dark', 'It is about light.')], 'O2', d='H'),
 PM('Which shows a ray of light?', ('➡️', 'A straight arrow'), [('〰️', 'A wiggly line', 'Rays are straight.'), ('⭕', 'A circle', 'Rays are straight.')], 'O2'),
)
s.adv(
 PM('* Advanced. How could you see round a corner?', ('🪞', 'Use a mirror to bounce the light'), [('🔦', 'Shine a brighter torch', 'Light still goes straight.'), ('🙈', 'Close one eye', 'You need a mirror.')], 'O2', d='VH'),
 PM('* Advanced. You move one card out of line. What happens?', ('🌑', 'The light is blocked'), [('💡', 'The light gets brighter', 'It is blocked.'), ('↪️', 'The light bends', 'Light cannot bend.')], 'O2', d='H'),
 OD('* Advanced. Order the path of sunlight to your eye.', ['the Sun', 'space', 'the air', 'your eye'], o='O2', d='H'),
)
s.labs('Ray lab',
 sort_lab('Will the light get through?', 'Sort each set-up.', ['Light gets through', 'Light is blocked'],
  [('holes in a straight line', '🎯', 0, 'Straight holes let light through.'), ('one card moved', '🃏', 1, 'The light hits the card.'), ('a clear window', '🪟', 0, 'Light goes through.'), ('a wall in the way', '🧱', 1, 'The wall blocks it.')],
  [PM('Which set-up lets light through?', ('🎯', 'Holes in a straight line'), [('🃏', 'One card moved', 'It blocks the light.')], 'O2')]),
 home('Three cards', 'Show that light travels in straight lines.', ['three cards with a hole in each', 'modelling clay', 'a torch'], ['Never shine a torch into anyone\'s eyes.'],
  ['Stand the cards in a line with clay.', 'Line up the holes.', 'Shine the torch through.', 'Move one card.'],
  ['Cards', 'Could I see the light?'], [('in a straight line', ['yes', 'no']), ('one card moved', ['yes', 'no'])],
  [PM('What does this show?', ('📏', 'Light travels in straight lines'), [('🌀', 'Light goes round', 'It shows light goes straight.')], 'O2')]))

# ============================================================  5.3
s = U.section('5.3', 'Light reflects off surfaces', ['O3']); s.words(V['5.3']); core(s, 'O3')
s.stop(PM('Which surface reflects the most light?', ('🪞', 'A mirror'), [('🧱', 'A brick', 'Bricks are dull.'), ('🧸', 'A teddy', 'Teddies are dull.')], 'O3'),
       PM('When light bounces off something, we say it…', ('↩️', 'reflects'), [('🧊', 'freezes', 'It reflects.'), ('🍫', 'melts', 'It reflects.')], 'O3'))
s.stop(PM('Why do cyclists wear reflective strips at night?', ('🦺', 'So drivers can see them'), [('🎨', 'To look cool', 'It is for safety.'), ('🔥', 'To stay warm', 'It is for safety.')], 'O3'),
       PM('What colour clothes are best to wear at night near roads?', ('⚪', 'Bright or reflective'), [('⚫', 'Black', 'Drivers cannot see dark clothes.'), ('🟤', 'Brown', 'Drivers cannot see dark clothes.')], 'O3'))
s.prac(
 GD('Shiny or dull?', 'Surface', [('🪞 mirror', 'shiny'), ('🧱 brick', 'dull'), ('🥄 metal spoon', 'shiny'), ('🧶 wool', 'dull')], o='O3'),
 PM('What do you see in a mirror?', ('😀', 'Your reflection'), [('🌑', 'Darkness', 'You see yourself.'), ('📺', 'A TV show', 'You see yourself.')], 'O3'),
 YN('Do smooth, shiny things reflect more light than rough, dull things?', True, 'O3', pic='✨', why='Yes!'),
 PM('Why do cats\' eyes seem to glow at night?', ('🐱', 'A shiny layer inside reflects light'), [('💡', 'They have bulbs inside', 'They reflect light.'), ('🔥', 'They are on fire', 'They reflect light.')], 'O3'),
 MT('Match each word to what it means.', [('reflect', 'bounce light back'), ('shiny', 'smooth and bright'), ('dull', 'not shiny')], o='O3'),
 TK('Tick the shiny things.', ['Shiny', 'Dull'], [('foil', ['✓', '✗']), ('paper', ['✗', '✓']), ('a new coin', ['✓', '✗'])], o='O3'),
 PM('Where would a reflector be most useful?', ('🎒', 'On a school bag for walking at night'), [('🛏️', 'Under your bed', 'It helps at night near roads.'), ('🍽️', 'On your plate', 'It helps at night near roads.')], 'O3'),
 YN('Can you see yourself in a brick wall?', False, 'O3', pic='🧱', why='No. Bricks are dull and rough.'),
 PM('A spoon looks shiny. What material is it?', ('🔩', 'Metal'), [('🧶', 'Wool', 'Wool is dull.'), ('🪵', 'Wood', 'Wood is dull.')], 'O3'),
 PM('Which would make the best mirror?', ('🪙', 'Smooth, shiny metal'), [('🧱', 'A brick', 'Bricks are rough.'), ('📄', 'Paper', 'Paper is dull.')], 'O3'),
 PM('The Moon shines at night because it…', ('↩️', 'reflects sunlight'), [('💡', 'has lights on it', 'It reflects sunlight.'), ('🔥', 'is on fire', 'It reflects sunlight.')], 'O3', d='H'),
 OD('Order from reflects most light to reflects least.', ['mirror', 'white paper', 'black wool'], o='O3'),
)
s.adv(
 PM('* Advanced. Why are road signs covered in reflective paint?', ('🚗', 'Car lights make them shine so drivers see them'), [('🌞', 'To keep them cool', 'It is so they can be seen.'), ('🌧️', 'To keep rain off', 'It is so they can be seen.')], 'O3', d='H'),
 PM('* Advanced. What would happen if you wore dark clothes on a dark road?', ('⚠️', 'Drivers might not see you'), [('✨', 'You would glow', 'Dark clothes are hard to see.'), ('😎', 'Nothing', 'It is dangerous.')], 'O3', d='H'),
 PM('* Advanced. A mirror is bent like a spoon. What happens to your reflection?', ('🙃', 'It looks stretched or upside down'), [('😀', 'It looks the same', 'Curved mirrors change it.'), ('🌑', 'It disappears', 'Curved mirrors change it.')], 'O3', d='VH'),
)
s.labs('Shine lab',
 test_lab('Shine test', 'Shine a torch on different materials. Read how bright each one looks (0 to 10).', 'Material', 'Brightness', 'points', 10, 1,
  'Tap the number the bar reaches.', [('foil', '✨', 9), ('white paper', '📄', 6), ('black wool', '🧶', 1)],
  [PM('Which reflected the most light?', ('✨', 'Foil'), [('🧶', 'Black wool', 'It reflected least.')], 'O3')]),
 home('Shine test', 'Find which materials are shiny.', ['foil, paper, wool and a spoon', 'a torch', 'a dark room'], ['Do not shine the torch in anyone\'s eyes.'],
  ['Go into a dark room.', 'Shine the torch on each material.', 'Which looks brightest?'],
  ['Material', 'Shiny or dull?'], [('foil', ['shiny', 'dull']), ('wool', ['shiny', 'dull']), ('spoon', ['shiny', 'dull'])],
  [PM('Which material would make a good reflector?', ('✨', 'Foil'), [('🧶', 'Wool', 'Wool is dull.')], 'O3')]))

# ============================================================  5.4
s = U.section('5.4', 'Light in the solar system', ['O4']); s.words(V['5.4']); core(s, 'O4')
s.stop(PM('Which of these makes its own light?', ('☀️', 'The Sun'), [('🌙', 'The Moon', 'It reflects sunlight.'), ('🌍', 'The Earth', 'It reflects sunlight.')], 'O4'),
       PM('The Sun is a…', ('⭐', 'star'), [('🪐', 'planet', 'It is a star.'), ('🌙', 'moon', 'It is a star.')], 'O4'))
s.stop(PM('Why can we see the Moon at night?', ('↩️', 'It reflects light from the Sun'), [('💡', 'It makes its own light', 'It reflects sunlight.'), ('🔦', 'People shine torches at it', 'It reflects sunlight.')], 'O4'),
       PM('Do planets make their own light?', ('🚫', 'No – they reflect sunlight'), [('✅', 'Yes, they glow', 'They reflect sunlight.')], 'O4'))
s.prac(
 YN('Is it safe to look straight at the Sun?', False, 'O4', pic='☀️', why='Never! It can hurt your eyes.'),
 GD('Star, planet or moon?', 'It is a', [('☀️ the Sun', 'star'), ('🌍 the Earth', 'planet'), ('🌙 the Moon', 'moon')], o='O4'),
 PM('What goes round the Sun?', ('🌍', 'The Earth and the other planets'), [('⭐', 'All the stars', 'Planets go round the Sun.'), ('☁️', 'The clouds', 'Planets go round the Sun.')], 'O4'),
 PM('Why do stars look tiny at night?', ('🔭', 'They are very, very far away'), [('🐜', 'They are tiny', 'Many are huge!'), ('🌙', 'The Moon hides them', 'They are far away.')], 'O4'),
 MT('Match each word to what it means.', [('Sun', 'our star'), ('Moon', 'goes round the Earth'), ('planet', 'goes round the Sun')], o='O4'),
 TK('Tick what is true.', ['True', 'False'], [('the Sun is a star', ['✓', '✗']), ('the Moon makes its own light', ['✗', '✓']), ('the Earth is a planet', ['✓', '✗'])], o='O4'),
 PM('In a model, a torch is the Sun and a ball is the Moon. Which side of the ball is lit?', ('🌗', 'The side facing the torch'), [('🌑', 'The side facing away', 'Light hits the side facing it.')], 'O4'),
 YN('Is the Sun very hot?', True, 'O4', pic='🔥', why='Yes! It is a huge ball of hot gas.'),
 PM('What is the solar system?', ('🌌', 'The Sun and everything that goes round it'), [('🏠', 'A house', 'It is the Sun and planets.'), ('📺', 'A TV show', 'It is the Sun and planets.')], 'O4'),
 PM('Which planet do we live on?', ('🌍', 'Earth'), [('🪐', 'Saturn', 'We live on Earth.'), ('🔴', 'Mars', 'We live on Earth.')], 'O4'),
 PM('What protects your eyes on a sunny day?', ('🧢', 'A hat and not looking at the Sun'), [('👀', 'Staring at the Sun', 'Never look at the Sun!'), ('🔦', 'A torch', 'Never look at the Sun.')], 'O4'),
 PM('Which of these is the light source for the solar system?', ('☀️', 'The Sun'), [('🌙', 'The Moon', 'The Moon reflects.'), ('🪐', 'Saturn', 'Planets reflect.')], 'O4', d='H'),
)
s.adv(
 PM('* Advanced. Why do we see the Moon in the day sometimes?', ('☀️', 'Sunlight reflects off it in the day too'), [('💡', 'It turns its lights on', 'It reflects sunlight.'), ('🌑', 'It is night', 'It can be daytime.')], 'O4', d='H'),
 PM('* Advanced. Some stars are bigger than the Sun. Why does the Sun look biggest?', ('📏', 'It is much closer to us'), [('🔥', 'It is the hottest', 'It is closest.'), ('⭐', 'It is the only star', 'There are many stars.')], 'O4', d='VH'),
 OD('* Advanced. Order from closest to the Earth to furthest.', ['the Moon', 'the Sun', 'other stars'], o='O4', d='H'),
)
s.labs('Space lab',
 sort_lab('Makes light or reflects light?', 'Sort each thing in space.', ['Makes light', 'Reflects light'],
  [('Sun', '☀️', 0, 'The Sun is a star.'), ('Moon', '🌙', 1, 'It reflects sunlight.'), ('Earth', '🌍', 1, 'It reflects sunlight.'), ('a star', '⭐', 0, 'Stars make light.'), ('Saturn', '🪐', 1, 'Planets reflect sunlight.')],
  [PM('Which makes its own light?', ('⭐', 'A star'), [('🌙', 'The Moon', 'It reflects light.')], 'O4')]),
 home('Model Sun and Moon', 'See how the Moon is lit.', ['a torch', 'a ball', 'a dark room'], ['Never shine the torch in anyone\'s eyes.'],
  ['Go into a dark room.', 'Shine the torch on the ball.', 'Walk round the ball.'],
  ['Question', 'My answer'], [('was half of the ball lit?', ['yes', 'no']), ('did the lit side face the torch?', ['yes', 'no'])],
  [PM('In the model, the torch is…', ('☀️', 'the Sun'), [('🌙', 'the Moon', 'The ball is the Moon.')], 'O4')]))

# ============================================================  5.5
s = U.section('5.5', 'Day and night', ['O5']); s.words(V['5.5']); core(s, 'O5')
s.stop(PM('Why do we have day and night?', ('🌍', 'The Earth spins'), [('☀️', 'The Sun goes round the Earth', 'The Earth spins.'), ('🌙', 'The Moon covers the Sun', 'The Earth spins.')], 'O5'),
       PM('The side of the Earth facing the Sun has…', ('🌞', 'day'), [('🌜', 'night', 'Facing away has night.')], 'O5'))
s.stop(PM('How long does the Earth take to spin round once?', ('🕛', '24 hours (one day)'), [('📅', 'One year', 'That is one trip round the Sun.'), ('⏱️', 'One minute', 'Much longer: one day.')], 'O5'),
       PM('How many hours are in one day?', ('🕛', '24'), [('🔟', '10', 'There are 24.'), ('⏱️', '60', 'There are 24.')], 'O5'))
s.prac(
 OD('Put the day in order.', ['sunrise', 'midday', 'sunset', 'night'], o='O5'),
 YN('Does the Sun really move across the sky?', False, 'O5', pic='☀️', why='No. It only seems to move because the Earth spins.'),
 PM('When it is day in Vietnam, what is it on the other side of the world?', ('🌜', 'Night'), [('🌞', 'Day too', 'The other side faces away.'), ('❄️', 'Winter', 'It is about day and night.')], 'O5'),
 PM('Where does the Sun seem to be at midday?', ('⬆️', 'High in the sky'), [('⬇️', 'Low in the sky', 'At midday it is high.'), ('🌑', 'Gone', 'At midday it is high.')], 'O5'),
 GD('Day or night?', 'Time', [('🌞 our side faces the Sun', 'day'), ('🌜 our side faces away', 'night'), ('⭐ we see stars', 'night')], o='O5'),
 MT('Match each word to what it means.', [('sunrise', 'the Sun seems to come up'), ('sunset', 'the Sun seems to go down'), ('spin', 'turn round and round')], o='O5'),
 TK('Tick what is true.', ['True', 'False'], [('the Earth spins', ['✓', '✗']), ('one spin takes a day', ['✓', '✗']), ('the Sun goes round the Earth each day', ['✗', '✓'])], o='O5'),
 PM('A sticker on a spinning globe faces the torch. It is…', ('🌞', 'daytime there'), [('🌜', 'night there', 'Facing the light is day.')], 'O5'),
 YN('Do we see stars better at night?', True, 'O5', pic='⭐', why='Yes – the sky is dark.'),
 PM('What do most people do at night?', ('😴', 'Sleep'), [('🏊', 'Go swimming at school', 'Most people sleep.'), ('🌞', 'Sunbathe', 'There is no sunlight.')], 'O5'),
 PM('Which shows day and night best?', ('🌐', 'A spinning globe and a torch'), [('🎈', 'A balloon and a cup', 'A globe and torch.'), ('📏', 'A ruler', 'A globe and torch.')], 'O5'),
 PM('Owls and bats are awake at…', ('🌜', 'night'), [('🌞', 'midday', 'They are night animals.')], 'O5', d='H'),
)
s.adv(
 PM('* Advanced. Why does the Sun seem to rise in the east?', ('🌍', 'Because of the way the Earth spins'), [('☀️', 'The Sun likes the east', 'It is the Earth spinning.'), ('🌬️', 'The wind blows it', 'It is the Earth spinning.')], 'O5', d='VH'),
 PM('* Advanced. If the Earth stopped spinning, what would happen?', ('⏸️', 'One side would always have day'), [('🔁', 'Day and night would be faster', 'No more turning.'), ('😴', 'Nothing', 'Day and night would stop changing.')], 'O5', d='VH'),
 OD('* Advanced. Order the shadow of a tree during the day.', ['long (morning)', 'short (midday)', 'long (evening)'], o='O5', d='H'),
)
s.labs('Day and night lab',
 sort_lab('Day or night?', 'Sort each picture.', ['Day', 'Night'],
  [('the Sun is high', '🌞', 0, 'That is day.'), ('stars twinkle', '⭐', 1, 'Stars show at night.'), ('owls hunt', '🦉', 1, 'Owls come out at night.'), ('children at school', '🏫', 0, 'School is in the day.'), ('we sleep', '😴', 1, 'We sleep at night.')],
  [PM('When do owls hunt?', ('🌜', 'At night'), [('🌞', 'In the day', 'Owls are night hunters.')], 'O5')]),
 home('Spin the globe', 'Show day and night with a globe.', ['a globe or ball', 'a sticker', 'a torch'], ['Do not shine the torch in anyone\'s eyes.'],
  ['Put a sticker where you live.', 'Shine the torch at the globe.', 'Spin the globe slowly.'],
  ['Sticker', 'Day or night?'], [('facing the torch', ['day', 'night']), ('facing away', ['day', 'night'])],
  [PM('What makes day and night?', ('🌍', 'The Earth spinning'), [('🔦', 'The torch moving', 'The globe spun.')], 'O5')]))

# ============================================================  5.6
s = U.section('5.6', 'Investigating shadows', ['O6']); s.words(V['5.6']); core(s, 'O6')
s.stop(PM('How is a shadow made?', ('🧍', 'Something blocks the light'), [('💡', 'Light gets brighter', 'Light must be blocked.'), ('💧', 'It rains', 'Light must be blocked.')], 'O6'),
       PM('What do you need to make a shadow?', ('🔦', 'Light and something to block it'), [('🌑', 'Only darkness', 'You need light.'), ('🔊', 'Sound', 'You need light.')], 'O6'))
s.stop(PM('At what time of day is your shadow shortest?', ('🕛', 'Midday'), [('🌅', 'Early morning', 'Shadows are long then.'), ('🌇', 'Evening', 'Shadows are long then.')], 'O6'),
       PM('When is your shadow longest?', ('🌅', 'Early morning or evening'), [('🕛', 'Midday', 'Shadows are shortest at midday.')], 'O6'))
s.prac(
 YN('Can you see your shadow at night with no lights?', False, 'O6', pic='🌑', why='No. You need light to make a shadow.'),
 GD('Opaque (blocks light) or not?', 'Opaque?', [('🪵 wood', 'yes'), ('🪟 clear glass', 'no'), ('🧱 brick', 'yes'), ('📘 a book', 'yes')], o='O6'),
 PM('What shape is your shadow?', ('👤', 'The same shape as you'), [('⭕', 'Always a circle', 'It matches your shape.'), ('🔺', 'Always a triangle', 'It matches your shape.')], 'O6'),
 PM('You make a rabbit with your hands in front of a torch. What do you see on the wall?', ('🐰', 'A rabbit shadow'), [('🐶', 'A dog photo', 'You see a shadow.'), ('🌈', 'A rainbow', 'You see a shadow.')], 'O6'),
 OD('Order the shadow lengths of a stick through the day.', ['long in the morning', 'short at midday', 'long in the evening'], o='O6'),
 MT('Match each word to what it means.', [('shadow', 'dark shape where light is blocked'), ('opaque', 'does not let light through'), ('midday', 'middle of the day')], o='O6'),
 TK('Tick what is true.', ['True', 'False'], [('shadows need light', ['✓', '✗']), ('shadows are short at midday', ['✓', '✗']), ('clear glass makes a dark shadow', ['✗', '✓'])], o='O6'),
 PM('What did people use long ago to tell the time with shadows?', ('🕐', 'A sundial'), [('📱', 'A phone', 'Long ago they used sundials.'), ('⌚', 'A watch', 'Long ago they used sundials.')], 'O6'),
 YN('Does your shadow move when you move?', True, 'O6', pic='🏃', why='Yes – it follows you!'),
 PM('Where is your shadow when the Sun is in front of you?', ('🔙', 'Behind you'), [('🔜', 'In front of you', 'The shadow is on the other side.'), ('⬆️', 'Above you', 'It is on the ground behind.')], 'O6', d='H'),
 PM('Why is it cooler in the shade of a tree?', ('🌳', 'The tree blocks the sunlight'), [('❄️', 'Trees make snow', 'The tree blocks the Sun.'), ('💨', 'Trees make wind', 'The tree blocks the Sun.')], 'O6'),
 PM('Which makes the darkest shadow?', ('🧱', 'A brick (opaque)'), [('🪟', 'Clear glass', 'Glass lets light through.'), ('🫧', 'A bubble', 'Bubbles let light through.')], 'O6'),
)
s.adv(
 PM('* Advanced. Why is your shadow long in the morning?', ('🌅', 'The Sun is low in the sky'), [('🌞', 'The Sun is high', 'High Sun makes short shadows.'), ('🛌', 'You are tired', 'It is about the Sun.')], 'O6', d='H'),
 PM('* Advanced. A torch moves closer to a toy. What happens to the shadow?', ('📈', 'It gets bigger'), [('📉', 'It gets smaller', 'Closer light makes a bigger shadow.'), ('🔁', 'Nothing', 'It changes size.')], 'O6', d='VH'),
 OD('* Advanced. Order the times from shortest shadow to longest.', ['12 o\'clock', '10 o\'clock', '8 o\'clock'], o='O6', d='H'),
)
s.labs('Shadow lab',
 test_lab('Shadow measuring', 'Measure the shadow of a stick at different times. Read the length.', 'Time of day', 'Shadow length', 'cm', 100, 10,
  'Tap the number the bar reaches.', [('9 o\'clock', '🌅', 80), ('12 o\'clock', '🕛', 20), ('3 o\'clock', '🌇', 60)],
  [PM('When was the shadow shortest?', ('🕛', '12 o\'clock'), [('🌅', '9 o\'clock', 'It was long then.')], 'O6')]),
 home('Shadow stick', 'Watch a shadow change during the day.', ['a stick', 'some stones', 'a sunny day'], ['Never look straight at the Sun.'],
  ['Push the stick into the ground.', 'Mark the end of its shadow in the morning.', 'Mark it again at midday and in the afternoon.'],
  ['Time', 'Shadow was'], [('morning', ['long', 'short']), ('midday', ['long', 'short']), ('afternoon', ['long', 'short'])],
  [PM('When was the shadow shortest?', ('🕛', 'Midday'), [('🌅', 'Morning', 'It was long in the morning.')], 'O6')]))

U.mindmap(('Seeing', 'light sources; light into eyes', 'O1', '5.1'), ('Straight lines', 'rays; no bending round corners', 'O2', '5.2'),
          ('Reflection', 'mirrors; shiny and dull; reflectors', 'O3', '5.3'), ('Solar system', 'the Sun is a star; the Moon reflects', 'O4', '5.4'),
          ('Day and night', 'the Earth spins in 24 hours', 'O5', '5.5'), ('Shadows', 'blocked light; long and short', 'O6', '5.6'))
