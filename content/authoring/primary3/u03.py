# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 3 · Unit 3 Light and shadows. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit3 import *

OBJ = {
 'O1': {'sec': '3.1', 'code': 'Physics', 'codeNote': '', 't': 'Know that a shadow forms when an object blocks light, and that we need light to make a shadow.'},
 'O2': {'sec': '3.2', 'code': 'Physics', 'codeNote': '', 't': 'Change the size of a shadow by moving the object or the light, and know shadows change during the day.'},
 'O3': {'sec': '3.3', 'code': 'Physics', 'codeNote': '', 't': 'Sort materials into transparent and opaque, and choose materials for a job.'},
 'O4': {'sec': '3.4', 'code': 'Physics', 'codeNote': '', 't': 'Know that translucent materials let some light through, and sort materials into three groups.'},
}
U = YUnit(3, 'Light and shadows', 'Physics: light', 'How shadows form, changing shadows, and transparent, translucent and opaque materials.', OBJ)

# ============================================================  3.1
s = U.section('3.1', 'Shadows', ['O1']); s.words(V['3.1']); core(s, 'O1')
s.stop(PM('What do you need to make a shadow?', ('🔦', 'Light and something to block it'), [('💧', 'Water and soap', 'You need light.'), ('🔊', 'A loud noise', 'You need light.')], 'O1'),
       PM('How is a shadow made?', ('🧍', 'Something blocks the light'), [('🎨', 'Someone paints it', 'Light is blocked.'), ('🌬️', 'The wind blows', 'Light is blocked.')], 'O1'))
s.stop(PM('Can you see your shadow in a completely dark room?', ('👎', 'No'), [('👍', 'Yes', 'With no light there is no shadow.')], 'O1'),
       PM('Why is there no shadow at night in a dark room?', ('🌑', 'There is no light'), [('😴', 'Shadows are asleep', 'There is no light.'), ('🧊', 'It is too cold', 'There is no light.')], 'O1'))
s.prac(
 YN('Is a shadow dark?', True, 'O1', pic='👤', why='Yes. It is where light cannot reach.'),
 PM('On a sunny day, where is your shadow?', ('👤', 'On the ground, on the side away from the Sun'), [('☀️', 'Up in the sky', 'Shadows fall on the ground.'), ('🎒', 'In your bag', 'Shadows fall on the ground.')], 'O1'),
 PM('Which makes a shadow on the wall?', ('✋', 'Your hand in front of a torch'), [('🔦', 'The torch on its own', 'Something must block the light.'), ('🌑', 'A dark room', 'You need light.')], 'O1'),
 GD('Will there be a shadow?', 'Shadow?', [('☀️ sunny day, you stand outside', 'yes'), ('🌑 dark room, no light', 'no'), ('🔦 torch on a toy', 'yes')], o='O1'),
 MT('Match each word to what it means.', [('shadow', 'dark shape where light is blocked'), ('torch', 'a light you can carry'), ('dark', 'no light')], o='O1'),
 TK('Tick what is true.', ['True', 'False'], [('you need light for a shadow', ['✓', '✗']), ('shadows are bright', ['✗', '✓']), ('your body can block light', ['✓', '✗'])], o='O1'),
 PM('You make a rabbit shape with your hands in front of a torch. What do you see on the wall?', ('🐰', 'A rabbit shadow'), [('🌈', 'A rainbow', 'You see a shadow.'), ('🐟', 'A fish', 'The shadow is the same shape as your hands.')], 'O1'),
 YN('Is it easy to see shadows on a very cloudy day?', False, 'O1', pic='☁️', why='No. Clouds hide the Sun, so shadows are faint.'),
 PM('Why does a tree make shade on a hot day?', ('🌳', 'It blocks the sunlight'), [('💧', 'It sprays water', 'It blocks the light.'), ('🌬️', 'It blows wind', 'It blocks the light.')], 'O1'),
 OD('Put in order: making a shadow puppet.', ['make the room dark', 'shine a torch on the wall', 'hold your hand in the light'], o='O1'),
 PM('Which is NOT needed for a shadow show?', ('🍰', 'A cake'), [('🔦', 'A torch', 'You need light.'), ('✋', 'Your hands', 'You need something to block light.')], 'O1', d='H'),
 YN('Does a shadow show the colours of the object?', False, 'O1', pic='🎨', why='No. A shadow is just dark.'),
)
s.adv(
 PM('* Advanced. Why does your shadow move when you move?', ('🧍', 'You block the light in a new place'), [('🦶', 'It is stuck to your feet with glue', 'You block light in a new place.'), ('🌬️', 'The wind pushes it', 'You block light in a new place.')], 'O1', d='H'),
 PM('* Advanced. Light travels in straight lines. How does that help make a shadow?', ('📏', 'Light cannot bend round you'), [('🌀', 'Light goes round in circles', 'It goes straight.'), ('🧊', 'Light freezes', 'It goes straight.')], 'O1', d='VH'),
 OD('* Advanced. Order the path: torch, toy, shadow.', ['the torch makes light', 'the toy blocks the light', 'a shadow forms behind the toy'], o='O1', d='H'),
)
s.labs('Shadow lab',
 sort_lab('Shadow or no shadow?', 'Will there be a shadow?', ['Shadow', 'No shadow'],
  [('torch on a teddy', '🧸', 0, 'The teddy blocks the light.'), ('a dark cupboard', '🌑', 1, 'No light, no shadow.'), ('sunny playground', '☀️', 0, 'You block the sunlight.'), ('night with no lights', '🌚', 1, 'No light, no shadow.'), ('lamp on a cup', '☕', 0, 'The cup blocks the light.')],
  [PM('Why was there no shadow in the dark cupboard?', ('🌑', 'There was no light'), [('🧸', 'The toy was too small', 'There was no light.')], 'O1')]),
 home('Shadow puppet show', 'Make shadow animals.', ['a torch', 'a wall', 'your hands', 'an adult'], ['Do not shine the torch in anyone\'s eyes.'],
  ['Make the room dark.', 'Shine the torch on the wall.', 'Make animal shapes with your hands.'],
  ['Question', 'My answer'], [('did I see a shadow?', ['yes', 'no']), ('was it the same shape as my hands?', ['yes', 'no'])],
  [PM('What did your hands do to the light?', ('✋', 'They blocked it'), [('🌈', 'They coloured it', 'They blocked it.')], 'O1')]))

# ============================================================  3.2
s = U.section('3.2', 'Changing shadows', ['O2']); s.words(V['3.2']); core(s, 'O2')
s.stop(PM('How can you make a shadow bigger?', ('🔦', 'Move the object closer to the torch'), [('🧱', 'Move it closer to the wall', 'That makes it smaller.'), ('🎨', 'Paint it', 'Move it near the torch.')], 'O2'),
       PM('A teddy is very close to the torch. What is its shadow like?', ('🐘', 'Big'), [('🐭', 'Small', 'Near the torch, the shadow is big.')], 'O2'))
s.stop(PM('When is your shadow shortest?', ('☀️', 'At midday'), [('🌅', 'In the morning', 'Morning shadows are long.'), ('🌇', 'In the evening', 'Evening shadows are long.')], 'O2'),
       PM('In the morning, the Sun is low. What is your shadow like?', ('📏', 'Long'), [('🤏', 'Very short', 'Low Sun, long shadow.')], 'O2'))
s.prac(
 PM('You move a toy far from the torch, close to the wall. Its shadow gets…', ('🐭', 'smaller'), [('🐘', 'bigger', 'Far from the torch, smaller.'), ('🌈', 'colourful', 'Shadows are dark.')], 'O2'),
 YN('Does a star-shaped card make a star-shaped shadow?', True, 'O2', pic='⭐', why='Yes. A shadow has the same outline.'),
 GD('Big or small shadow?', 'Shadow', [('🔦 toy near the torch', 'big'), ('🧱 toy near the wall', 'small'), ('🔦 hand near the torch', 'big')], o='O2'),
 OD('Order your shadow from longest to shortest.', ['early morning', 'mid-morning', 'midday'], o='O2'),
 PM('Where is the Sun at midday?', ('⬆️', 'High in the sky'), [('⬇️', 'Low near the ground', 'It is high at midday.'), ('🌑', 'It has gone', 'It is high at midday.')], 'O2'),
 MT('Match each word to what it means.', [('near', 'close to'), ('far', 'a long way away'), ('long', 'not short')], o='O2'),
 PM('Long ago, people told the time using…', ('🕰️', 'shadows on a sundial'), [('📱', 'phones', 'There were no phones.'), ('📺', 'TV', 'They used shadows.')], 'O2'),
 TK('Tick what is true.', ['True', 'False'], [('shadows change during the day', ['✓', '✗']), ('midday shadows are long', ['✗', '✓']), ('evening shadows are long', ['✓', '✗'])], o='O2'),
 YN('Does your shadow stay the same all day?', False, 'O2', pic='👤', why='No. It changes as the Sun moves across the sky.'),
 PM('You want a HUGE dinosaur shadow for your puppet show. What do you do?', ('🔦', 'Hold the dinosaur near the torch'), [('🧱', 'Hold it against the wall', 'That makes it small.'), ('🌑', 'Turn off the torch', 'Then there is no shadow.')], 'O2'),
 PM('A shadow drawn at 9 o\'clock and again at 12 o\'clock. What changed?', ('📏', 'It got shorter'), [('🎨', 'It changed colour', 'It got shorter.'), ('🤷', 'Nothing', 'It got shorter.')], 'O2', d='H'),
 YN('Can a round ball make a square shadow?', False, 'O2', pic='⚽', why='No. A round ball makes a round shadow.'),
)
s.adv(
 PM('* Advanced. Why are shadows long in the evening?', ('🌇', 'The Sun is low in the sky'), [('🌙', 'The Moon makes them long', 'The low Sun does.'), ('😴', 'Shadows get tired', 'The low Sun does.')], 'O2', d='H'),
 PM('* Advanced. You keep the toy still and move the torch closer. The shadow gets…', ('🐘', 'bigger'), [('🐭', 'smaller', 'Closer light, bigger shadow.'), ('🤷', 'the same', 'It gets bigger.')], 'O2', d='VH'),
 OD('* Advanced. Order the toy\'s shadow from biggest to smallest.', ['toy 10 cm from the torch', 'toy 30 cm from the torch', 'toy 60 cm from the torch'], o='O2', d='H'),
)
s.labs('Shadow size lab',
 test_lab('Shadow size', 'Move a teddy to different places between the torch and the wall. Read how tall the shadow is.', 'Where the teddy is', 'Shadow height', 'cm', 60, 5,
  'Tap the number the bar reaches.', [('near the wall', '🧱', 15), ('in the middle', '↔️', 30), ('near the torch', '🔦', 55)],
  [PM('Where was the shadow biggest?', ('🔦', 'Near the torch'), [('🧱', 'Near the wall', 'It was smallest there.')], 'O2')]),
 home('Shadow drawing', 'See how your shadow changes.', ['chalk or paper', 'a toy', 'a sunny day', 'an adult'], ['Never look straight at the Sun.'],
  ['Stand a toy outside in the morning.', 'Draw round its shadow.', 'Come back at midday and draw again.'],
  ['Time', 'Shadow'], [('morning', ['long', 'short']), ('midday', ['long', 'short'])],
  [PM('When was the shadow shortest?', ('☀️', 'At midday'), [('🌅', 'In the morning', 'It was long then.')], 'O2')]))

# ============================================================  3.3
s = U.section('3.3', 'Transparent and opaque', ['O3']); s.words(V['3.3']); core(s, 'O3')
s.stop(PM('Which material is transparent?', ('🪟', 'Window glass'), [('🪵', 'Wood', 'Wood is opaque.'), ('🧱', 'Brick', 'Brick is opaque.')], 'O3'),
       PM('What does transparent mean?', ('👓', 'See-through'), [('🌑', 'Very dark', 'It means see-through.'), ('🔊', 'Very loud', 'It means see-through.')], 'O3'))
s.stop(PM('Why are windows made of glass?', ('🪟', 'So light comes in and we can see out'), [('🔊', 'To keep noise in', 'Glass is transparent.'), ('🎨', 'To look colourful', 'Glass is transparent.')], 'O3'),
       PM('Which would be a bad window?', ('🪵', 'A wooden window'), [('🪟', 'A glass window', 'Glass is a good window.')], 'O3'))
s.prac(
 GD('Transparent or opaque?', 'Group', [('🪟 glass', 'transparent'), ('🪵 wood', 'opaque'), ('💧 clear water', 'transparent'), ('📘 a thick book', 'opaque'), ('🥄 metal', 'opaque')], o='O3'),
 YN('Can light go through a brick wall?', False, 'O3', pic='🧱', why='No. Brick is opaque.'),
 PM('Which makes the darkest shadow?', ('🪵', 'A wooden block'), [('🫧', 'Cling film', 'Cling film lets light through.'), ('🥛', 'A clear glass', 'Glass lets light through.')], 'O3'),
 PM('Thick curtains at bedtime are…', ('🌑', 'opaque, to keep the light out'), [('🪟', 'transparent, to let light in', 'They keep light out.')], 'O3'),
 MT('Match each word to what it means.', [('transparent', 'see-through'), ('opaque', 'lets no light through'), ('glass', 'a see-through material')], o='O3'),
 PM('A fish tank needs to be…', ('🐟', 'transparent, so we can see the fish'), [('🪵', 'opaque, like wood', 'Then we could not see the fish.')], 'O3'),
 TK('Tick the transparent things.', ['Transparent', 'Opaque'], [('a clear plastic bottle', ['✓', '✗']), ('a cardboard box', ['✗', '✓']), ('spectacle lenses', ['✓', '✗'])], o='O3'),
 YN('Is a door usually opaque?', True, 'O3', pic='🚪', why='Yes. Then nobody can see in.'),
 PM('You shine a torch on cling film. What happens?', ('✨', 'The light goes through'), [('🌑', 'The light is blocked', 'Cling film is transparent.')], 'O3'),
 PM('Which is the best material for a lunch box so you can see your food?', ('🫙', 'Clear plastic'), [('🥫', 'Metal', 'Metal is opaque.'), ('📦', 'Cardboard', 'Cardboard is opaque.')], 'O3'),
 PM('Why do some jellyfish look invisible in water?', ('🪼', 'They are transparent'), [('🌑', 'They are opaque', 'They are see-through.'), ('🎨', 'They are painted', 'They are see-through.')], 'O3', d='H'),
 YN('Do opaque materials make dark shadows?', True, 'O3', pic='👤', why='Yes. They block all the light.'),
)
s.adv(
 PM('* Advanced. Why are car windscreens transparent?', ('🚗', 'So the driver can see the road'), [('🌧️', 'To let rain in', 'So the driver can see.'), ('🎨', 'To look nice', 'So the driver can see.')], 'O3', d='H'),
 PM('* Advanced. Which job needs an opaque material?', ('🕶️', 'A blackout blind for a bedroom'), [('🪟', 'A shop window', 'That needs to be transparent.'), ('🔍', 'A magnifying glass', 'That needs to be transparent.')], 'O3', d='VH'),
 GD('* Advanced. Which material for the job?', 'Material', [('🪟 a window', 'transparent'), ('🚪 a front door', 'opaque'), ('🐟 a fish tank', 'transparent')], o='O3', d='H'),
)
s.labs('Torch test lab',
 sort_lab('Torch test', 'Shine a torch at each material. Does the light go through?', ['Transparent', 'Opaque'],
  [('cling film', '🫧', 0, 'Light goes through.'), ('a book', '📘', 1, 'It blocks light.'), ('a clear glass', '🥛', 0, 'Light goes through.'), ('foil', '✨', 1, 'It blocks light.'), ('clear water', '💧', 0, 'Light goes through.'), ('wood', '🪵', 1, 'It blocks light.')],
  [PM('Which material blocked the light?', ('📘', 'The book'), [('🫧', 'Cling film', 'Light went through.')], 'O3')]),
 home('Torch test', 'Test materials with a torch.', ['a torch', 'cling film', 'a book', 'a glass', 'foil'], ['Do not shine the torch in anyone\'s eyes.', 'Take care with glass.'],
  ['Hold each material in front of the torch.', 'Look at the wall behind.', 'Is there light, or a dark shadow?'],
  ['Material', 'Light through?'], [('cling film', ['yes', 'no']), ('a book', ['yes', 'no']), ('foil', ['yes', 'no'])],
  [PM('Which material was transparent?', ('🫧', 'Cling film'), [('✨', 'Foil', 'Foil blocked the light.')], 'O3')]))

# ============================================================  3.4
s = U.section('3.4', 'Translucent materials', ['O4']); s.words(V['3.4']); core(s, 'O4')
s.stop(PM('What does translucent mean?', ('🌫️', 'Lets some light through'), [('🪟', 'Lets all light through', 'That is transparent.'), ('🧱', 'Lets no light through', 'That is opaque.')], 'O4'),
       PM('Through a translucent material, things look…', ('🌫️', 'blurry'), [('👓', 'very clear', 'That is transparent.'), ('🌑', 'completely black', 'Some light gets through.')], 'O4'))
s.stop(PM('Which material is translucent?', ('📄', 'Tissue paper'), [('🪟', 'Clear glass', 'Clear glass is transparent.'), ('🪵', 'Wood', 'Wood is opaque.')], 'O4'),
       PM('Which is translucent?', ('🏮', 'A paper lantern'), [('🧱', 'A brick', 'A brick is opaque.'), ('💧', 'Clear water', 'Clear water is transparent.')], 'O4'))
s.prac(
 GD('Which group?', 'Group', [('🪟 clear glass', 'transparent'), ('📄 tissue paper', 'translucent'), ('🧱 brick', 'opaque'), ('🛍️ thin plastic bag', 'translucent'), ('🪵 wood', 'opaque')], o='O4'),
 YN('Does a bathroom window with bumpy glass let light in?', True, 'O4', pic='🪟', why='Yes, but you cannot see clearly through it.'),
 PM('Why do bathrooms often have frosted glass?', ('🚿', 'Light comes in but people cannot see in'), [('🔊', 'To keep noise out', 'It stops people seeing in.'), ('🧊', 'To keep it cold', 'It stops people seeing in.')], 'O4'),
 OD('Order from most light through to least.', ['transparent', 'translucent', 'opaque'], o='O4'),
 MT('Match each word to what it means.', [('translucent', 'lets some light through'), ('blurry', 'not clear'), ('lantern', 'a light with a cover')], o='O4'),
 PM('You hold tissue paper up to a window. What do you see?', ('🌫️', 'Light, but things look blurry'), [('🌑', 'Nothing, all dark', 'Some light gets through.'), ('👓', 'Everything very clearly', 'It is blurry.')], 'O4'),
 TK('Tick the translucent things.', ['Translucent', 'Not translucent'], [('baking paper', ['✓', '✗']), ('a metal tray', ['✗', '✓']), ('a frosted window', ['✓', '✗'])], o='O4'),
 YN('Is a lamp shade often translucent?', True, 'O4', pic='💡', why='Yes. It lets soft light through.'),
 PM('Which makes the palest shadow?', ('📄', 'Tissue paper'), [('📘', 'A book', 'A book makes a dark shadow.'), ('🥄', 'A metal spoon', 'Metal makes a dark shadow.')], 'O4'),
 PM('Shine a torch through your fingers in the dark. They glow red. Your skin is a little…', ('✋', 'translucent'), [('🪟', 'transparent', 'You cannot see through your hand.'), ('🌑', 'invisible', 'It lets some light through.')], 'O4', d='H'),
 PM('Which would make the best night light cover so the light is soft?', ('🏮', 'Translucent paper'), [('🪵', 'Wood', 'Wood blocks all light.'), ('🪟', 'Clear glass', 'Clear glass is too bright.')], 'O4'),
 YN('Can you read a book through tissue paper?', False, 'O4', pic='📖', why='No. It is too blurry.'),
)
s.adv(
 PM('* Advanced. You need to see a shape but not the details. Which material?', ('📄', 'A translucent one'), [('🪟', 'A transparent one', 'That shows details.'), ('🧱', 'An opaque one', 'That shows nothing.')], 'O4', d='VH'),
 PM('* Advanced. Wet tissue paper lets more light through. It becomes more…', ('🪟', 'transparent'), [('🧱', 'opaque', 'More light gets through.'), ('🔊', 'noisy', 'More light gets through.')], 'O4', d='H'),
 GD('* Advanced. Sort for a bedroom.', 'Best', [('🪟 window to see the garden', 'transparent'), ('🕶️ blind to sleep', 'opaque'), ('🏮 soft night light', 'translucent')], o='O4', d='H'),
)
s.labs('Light-through lab',
 test_lab('How much light gets through?', 'Shine a torch through each material. A light meter reads how much light gets through (0 to 10).', 'Material', 'Light through', 'points', 10, 1,
  'Tap the number the bar reaches.', [('card', '🪵', 1), ('tissue paper', '📄', 5), ('cling film', '🫧', 9)],
  [PM('Which material is translucent?', ('📄', 'Tissue paper'), [('🫧', 'Cling film', 'Almost all light got through: transparent.'), ('🪵', 'Card', 'Almost no light got through: opaque.')], 'O4')]),
 home('Window sort', 'Sort materials at a window.', ['tissue paper', 'cling film', 'card', 'a window'], ['Never look straight at the Sun.'],
  ['Hold each material up to the window.', 'Is it clear, blurry or dark?'],
  ['Material', 'What I saw'], [('tissue paper', ['clear', 'blurry', 'dark']), ('cling film', ['clear', 'blurry', 'dark']), ('card', ['clear', 'blurry', 'dark'])],
  [PM('Which one looked blurry?', ('📄', 'Tissue paper'), [('🫧', 'Cling film', 'That was clear.')], 'O4')]))

U.mindmap(('Shadows', 'light is blocked', 'O1', '3.1'), ('Changing shadows', 'near the light: big', 'O2', '3.2'),
          ('Transparent and opaque', 'see-through or blocks all light', 'O3', '3.3'), ('Translucent', 'some light, blurry', 'O4', '3.4'))
