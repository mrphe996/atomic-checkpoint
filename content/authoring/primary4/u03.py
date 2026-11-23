# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 4 · Unit 3 Materials. Written by the Atomic teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit4 import *

OBJ = {
 'O1': {'sec': '3.1', 'code': 'Chemistry', 'codeNote': '', 't': 'Name common materials, and sort materials into solids, liquids and gases; know that everything is made of tiny particles.'},
 'O2': {'sec': '3.2', 'code': 'Chemistry', 'codeNote': '', 't': 'Know that solids keep their shape, and liquids flow and take the shape of their container.'},
 'O3': {'sec': '3.3', 'code': 'Chemistry', 'codeNote': '', 't': 'Know that heating can melt solids and cooling can make liquids solidify (freeze).'},
 'O4': {'sec': '3.4', 'code': 'Chemistry', 'codeNote': '', 't': 'Know that a chemical reaction makes a new material, and spot signs of a reaction (bubbles, colour, heat, smell).'},
}
U = YUnit(3, 'Materials', 'Chemistry: materials', 'Solids, liquids and gases, melting and freezing, and fizzy reactions in the kitchen.', OBJ)

# ============================================================  3.1
s = U.section('3.1', 'Materials and particles', ['O1']); s.words(V['3.1']); core(s, 'O1')
s.stop(PM('Is ice a solid, a liquid or a gas?', ('🧊', 'A solid'), [('💧', 'A liquid', 'Ice keeps its shape.'), ('💨', 'A gas', 'Ice keeps its shape.')], 'O1'),
       PM('Is air a solid, a liquid or a gas?', ('💨', 'A gas'), [('🧊', 'A solid', 'Air has no shape.'), ('💧', 'A liquid', 'Air spreads out everywhere.')], 'O1'))
s.stop(PM('Which of these is a liquid?', ('🥛', 'Milk'), [('🪨', 'A stone', 'A stone is solid.'), ('🎈', 'The air in a balloon', 'Air is a gas.')], 'O1'),
       PM('Which of these is a solid?', ('🪑', 'A chair'), [('🧃', 'Juice', 'Juice is a liquid.'), ('💨', 'Steam', 'Steam is a gas.')], 'O1'))
s.prac(
 GD('What is each thing made of?', 'Material', [('🪑 chair', 'wood'), ('🥄 spoon', 'metal'), ('🪟 window', 'glass'), ('🥤 cup', 'plastic')], o='O1'),
 GD('Solid, liquid or gas?', 'State', [('🧱 brick', 'solid'), ('💧 water', 'liquid'), ('💨 air', 'gas'), ('🍯 honey', 'liquid')], o='O1'),
 YN('Is everything made of tiny particles?', True, 'O1', pic='⚪', why='Yes, too small to see!'),
 PM('In which do the particles zoom around far apart?', ('💨', 'A gas'), [('🧊', 'A solid', 'Solid particles are packed tightly.'), ('💧', 'A liquid', 'Liquid particles slide past each other.')], 'O1'),
 PM('What is inside a blown-up balloon?', ('💨', 'Gas (air)'), [('💧', 'Water', 'You blew air into it.'), ('🪨', 'Stones', 'You blew air into it.')], 'O1'),
 PM('Which material is best for a window?', ('🪟', 'Glass – you can see through it'), [('🪵', 'Wood', 'You cannot see through wood.'), ('🧱', 'Brick', 'You cannot see through brick.')], 'O1'),
 PM('Which material is best for a raincoat?', ('🧥', 'Plastic – it keeps water out'), [('📄', 'Paper', 'Paper gets soggy.'), ('🧶', 'Wool', 'Wool soaks up water.')], 'O1'),
 MT('Match each word to what it means.', [('solid', 'keeps its shape'), ('liquid', 'flows'), ('gas', 'spreads out everywhere')], o='O1'),
 YN('Can you see the particles in water with your eyes?', False, 'O1', pic='🔍', why='No, they are far too small.'),
 TK('Tick the solids.', ['Solid', 'Not solid'], [('pencil', ['✓', '✗']), ('orange juice', ['✗', '✓']), ('coin', ['✓', '✗'])], o='O1'),
 PM('You squash a sponge. Is it still a solid?', ('🧽', 'Yes – it is a solid with holes'), [('💧', 'No, it is a liquid', 'A sponge keeps its shape again.'), ('💨', 'No, it is a gas', 'A sponge is a solid.')], 'O1', d='H'),
 PM('Which material is a spoon usually made of?', ('🥄', 'Metal'), [('📄', 'Paper', 'Paper would bend.'), ('🧊', 'Ice', 'Ice would melt.')], 'O1'),
)
s.adv(
 PM('* Advanced. Why can you squash a balloon full of air a little?', ('💨', 'Gas particles are far apart'), [('🧊', 'Air is solid', 'Air is a gas.'), ('💧', 'Air is a liquid', 'Air is a gas.')], 'O1', d='H'),
 PM('* Advanced. Why can you not walk through a wall?', ('🧱', 'Its particles are packed tightly'), [('💨', 'It is a gas', 'A wall is a solid.'), ('🎨', 'It is painted', 'It is about particles.')], 'O1', d='H'),
 OD('* Advanced. Order from particles closest together to furthest apart.', ['solid', 'liquid', 'gas'], o='O1', d='H'),
)
s.labs('Materials lab',
 sort_lab('Solid, liquid or gas?', 'Sort each thing.', ['Solid', 'Liquid', 'Gas'],
  [('stone', '🪨', 0, 'A stone keeps its shape.'), ('milk', '🥛', 1, 'Milk flows.'), ('air', '💨', 2, 'Air spreads out.'), ('ice', '🧊', 0, 'Ice keeps its shape.'), ('juice', '🧃', 1, 'Juice flows.'), ('steam', '♨️', 2, 'Steam is a gas.')],
  [PM('Which is a gas?', ('♨️', 'Steam'), [('🪨', 'Stone', 'A stone is solid.')], 'O1')]),
 home('Material hunt', 'Find what things at home are made of.', ['paper and a pencil'], ['Do not touch sharp or hot things.'],
  ['Find a cup, a spoon, a window and a chair.', 'What is each made of?'],
  ['Thing', 'Made of'], [('spoon', ['metal', 'wood', 'glass', 'plastic']), ('window', ['metal', 'wood', 'glass', 'plastic']), ('chair', ['metal', 'wood', 'glass', 'plastic'])],
  [PM('Why are windows made of glass?', ('👀', 'You can see through glass'), [('🪵', 'Glass is soft', 'Glass is hard and see-through.')], 'O1')]))

# ============================================================  3.2
s = U.section('3.2', 'How solids and liquids behave', ['O2']); s.words(V['3.2']); core(s, 'O2')
s.stop(PM('What happens when you pour a liquid into a glass?', ('🥛', 'It takes the shape of the glass'), [('🧱', 'It keeps its own shape', 'Solids keep their shape.'), ('💨', 'It flies away', 'Liquids stay in the glass.')], 'O2'),
       PM('Which can you pour?', ('🧃', 'Juice'), [('🧱', 'A brick', 'A brick keeps its shape.'), ('📘', 'A book', 'A book keeps its shape.')], 'O2'))
s.stop(PM('You can pour sand. Is sand a solid or a liquid?', ('🏖️', 'A solid – each grain keeps its shape'), [('💧', 'A liquid', 'Look at each grain: it keeps its shape.')], 'O2'),
       PM('Is rice a solid or a liquid?', ('🍚', 'A solid'), [('💧', 'A liquid', 'Each grain keeps its shape.')], 'O2'))
s.prac(
 PM('Which flows most slowly?', ('🍯', 'Honey'), [('💧', 'Water', 'Water flows fast.'), ('🥛', 'Milk', 'Milk flows fast.')], 'O2'),
 YN('Does a solid keep its shape when you move it to a new box?', True, 'O2', pic='📦', why='Yes. Solids keep their shape.'),
 YN('Does a liquid keep its shape when you pour it into a new cup?', False, 'O2', pic='🥤', why='No. It takes the shape of the new cup.'),
 GD('Solid or liquid?', 'State', [('🍚 rice', 'solid'), ('🧂 salt', 'solid'), ('🫒 oil', 'liquid'), ('🍎 apple', 'solid'), ('🧴 shampoo', 'liquid')], o='O2'),
 PM('Why is rice tricky to sort?', ('🍚', 'You can pour it, but each grain is a solid'), [('💧', 'It is wet', 'It is about pouring.'), ('🔥', 'It is hot', 'It is about pouring.')], 'O2'),
 PM('What takes the shape of its container?', ('💧', 'A liquid'), [('🧱', 'A solid', 'Solids keep their own shape.')], 'O2'),
 MT('Match each word to what it means.', [('pour', 'make a liquid flow out'), ('container', 'something that holds things'), ('grain', 'a tiny hard piece')], o='O2'),
 TK('Tick the liquids.', ['Liquid', 'Not liquid'], [('honey', ['✓', '✗']), ('sugar', ['✗', '✓']), ('milk', ['✓', '✗'])], o='O2'),
 PM('You spill water on the floor. What does it do?', ('💦', 'It spreads out into a puddle'), [('🧱', 'It stands up like a tower', 'Liquids flow.'), ('🎈', 'It floats up', 'Water falls and spreads.')], 'O2'),
 PM('Which would make the best pouring race winner (fastest)?', ('💧', 'Water'), [('🍯', 'Honey', 'Honey is very slow.'), ('🧴', 'Shampoo', 'Shampoo is slow.')], 'O2'),
 YN('Does honey flow more slowly when it is cold?', True, 'O2', pic='🍯', why='Yes! Cold honey is thicker.'),
 PM('Which is a solid that you can pour?', ('🧂', 'Salt'), [('🫒', 'Oil', 'Oil is a liquid.'), ('🧃', 'Juice', 'Juice is a liquid.')], 'O2'),
)
s.adv(
 PM('* Advanced. You tip a jar of marbles. They pour out. Are marbles a liquid?', ('⚪', 'No – each marble keeps its shape'), [('💧', 'Yes, they pour', 'Pouring is not enough: each one keeps its shape.')], 'O2', d='H'),
 OD('* Advanced. Order from fastest flowing to slowest.', ['water', 'shampoo', 'honey'], o='O2', d='H'),
 PM('* Advanced. Toothpaste keeps a shape on your brush, but squeezes out of the tube. It is…', ('🪥', 'a thick, tricky material'), [('🪨', 'a hard solid', 'You can squeeze it.'), ('💨', 'a gas', 'It is not a gas.')], 'O2', d='VH'),
)
s.labs('Pouring lab',
 test_lab('Pouring race', 'Tip a spoon of each liquid. Read how many seconds it takes to run off.', 'Liquid', 'Time to run off', 'seconds', 20, 2,
  'Tap the number the bar reaches.', [('water', '💧', 2), ('shampoo', '🧴', 10), ('honey', '🍯', 18)],
  [PM('Which liquid took the longest?', ('🍯', 'Honey'), [('💧', 'Water', 'Water was quickest.')], 'O2')]),
 home('Pouring race at home', 'Find out which liquids flow fastest.', ['three spoons', 'water, honey and shampoo', 'a plate'], ['Wash your hands afterwards. Do not eat the shampoo!'],
  ['Put each liquid on a spoon.', 'Tip the spoons at the same time.', 'Watch which runs off first.'],
  ['Liquid', 'Speed'], [('water', ['fast', 'medium', 'slow']), ('shampoo', ['fast', 'medium', 'slow']), ('honey', ['fast', 'medium', 'slow'])],
  [PM('Which liquid flowed slowest?', ('🍯', 'Honey'), [('💧', 'Water', 'Water is fast.')], 'O2')]))

# ============================================================  3.3
s = U.section('3.3', 'Melting and solidifying', ['O3']); s.words(V['3.3']); core(s, 'O3')
s.stop(PM('What happens to chocolate when you hold it in a hot hand?', ('🍫', 'It melts'), [('🧊', 'It freezes', 'Heat makes it melt.'), ('📏', 'It grows', 'Heat makes it melt.')], 'O3'),
       PM('What makes an ice cream melt?', ('☀️', 'Heat'), [('🥶', 'Cold', 'Cold keeps it frozen.'), ('🌑', 'Darkness', 'Heat makes it melt.')], 'O3'))
s.stop(PM('What do we call a liquid turning into a solid?', ('🧊', 'Solidifying (freezing)'), [('🍫', 'Melting', 'Melting is solid to liquid.'), ('💨', 'Blowing', 'That is not a change of state.')], 'O3'),
       PM('Where would you put juice to make a lolly?', ('🥶', 'In the freezer'), [('🔥', 'In the oven', 'That makes it hot.'), ('☀️', 'In the sun', 'That makes it warm.')], 'O3'))
s.prac(
 GD('Melting or freezing?', 'Change', [('🍦 ice cream in the sun', 'melting'), ('🧃 juice in the freezer', 'freezing'), ('🧈 butter in a hot pan', 'melting'), ('💧 water into ice', 'freezing')], o='O3'),
 YN('Can melting be undone by cooling?', True, 'O3', pic='🔄', why='Yes. Melted chocolate becomes solid again when it cools.'),
 PM('Which melts most quickly on a hot day?', ('🧊', 'An ice cube'), [('🪨', 'A stone', 'Stones need much more heat.'), ('🥄', 'A metal spoon', 'Metal needs much more heat.')], 'O3'),
 PM('What does melted rock come out of?', ('🌋', 'A volcano'), [('🚰', 'A tap', 'Taps give water.'), ('🌳', 'A tree', 'Volcanoes give lava.')], 'O3'),
 OD('Put the ice lolly story in order.', ['juice', 'put in the freezer', 'solid lolly', 'melts in the sun'], o='O3'),
 MT('Match each word to what it means.', [('melt', 'solid to liquid'), ('freeze', 'liquid to solid'), ('heat', 'makes things warmer')], o='O3'),
 PM('Where does an ice cube melt fastest?', ('☀️', 'In a sunny place'), [('⛱️', 'In the shade', 'Shade is cooler.'), ('🥶', 'In the freezer', 'It stays frozen.')], 'O3'),
 TK('Tick what melts when it gets warm.', ['Melts', 'Does not melt'], [('chocolate', ['✓', '✗']), ('candle wax', ['✓', '✗']), ('a wooden block', ['✗', '✓'])], o='O3'),
 YN('Is it safe to play with candles on your own?', False, 'O3', pic='🕯️', why='No! Always ask an adult.'),
 PM('Butter is solid in the fridge. What happens on a hot day?', ('🧈', 'It gets soft and melts'), [('🧊', 'It freezes', 'Heat melts it.'), ('📏', 'It gets harder', 'Heat melts it.')], 'O3'),
 PM('Water freezes into…', ('🧊', 'ice'), [('♨️', 'steam', 'Steam comes from boiling.'), ('🍯', 'honey', 'Water freezes into ice.')], 'O3'),
 PM('Which is NOT melting?', ('🍭', 'Juice turning into a lolly'), [('🍫', 'Chocolate going runny', 'That is melting.'), ('🍦', 'Ice cream dripping', 'That is melting.')], 'O3', d='H'),
)
s.adv(
 PM('* Advanced. Why do people put salt on icy roads?', ('🧂', 'Salt helps the ice melt'), [('🍟', 'To make the road tasty', 'It helps ice melt.'), ('🎨', 'To make it white', 'It helps ice melt.')], 'O3', d='VH'),
 OD('* Advanced. Order from needs least heat to melt to needs most heat.', ['ice', 'chocolate', 'rock'], o='O3', d='H'),
 PM('* Advanced. Melted chocolate is put in a mould in the fridge. What shape will it be?', ('🍫', 'The shape of the mould'), [('💧', 'A puddle', 'It solidifies in the mould.')], 'O3', d='H'),
)
s.labs('Melting lab',
 test_lab('Ice cube race', 'Put ice cubes in different places. Read how many minutes each takes to melt.', 'Place', 'Time to melt', 'minutes', 60, 5,
  'Tap the number the bar reaches.', [('sunny window', '☀️', 15), ('shady room', '⛱️', 35), ('fridge', '🥶', 55)],
  [PM('Where did the ice melt fastest?', ('☀️', 'The sunny window'), [('🥶', 'The fridge', 'It was coldest there.')], 'O3')]),
 home('Melting chocolate', 'Watch chocolate melt and set again, with an adult.', ['two squares of chocolate', 'a small bowl', 'warm water (from an adult)'], ['An adult must handle the warm water.'],
  ['Put the chocolate in a bowl.', 'An adult puts the bowl in warm water.', 'Watch it melt.', 'Put it in the fridge.'],
  ['What happened', 'My answer'], [('in warm water, the chocolate…', ['melted', 'stayed hard']), ('in the fridge, it…', ['became solid', 'stayed runny'])],
  [PM('Can melting be undone?', ('🔄', 'Yes – by cooling'), [('🚫', 'No, never', 'It went solid again in the fridge.')], 'O3')]))

# ============================================================  3.4
s = U.section('3.4', 'Chemical reactions', ['O4']); s.words(V['3.4']); core(s, 'O4')
s.stop(PM('Can you turn a cake back into eggs and flour?', ('🎂', 'No – a new material was made'), [('🥚', 'Yes, easily', 'Baking cannot be undone.')], 'O4'),
       PM('Baking a cake is…', ('🧪', 'a chemical reaction'), [('🧊', 'melting', 'A new material is made.'), ('💧', 'pouring', 'A new material is made.')], 'O4'))
s.stop(PM('Which is a sign that a chemical reaction has happened?', ('🫧', 'Bubbles of gas'), [('📏', 'Nothing changes', 'Look for a change.'), ('🧊', 'It stays the same', 'Look for a change.')], 'O4'),
       PM('Baking soda and vinegar make…', ('🫧', 'lots of fizzy bubbles'), [('🧊', 'ice', 'They fizz.'), ('🍫', 'chocolate', 'They fizz.')], 'O4'))
s.prac(
 GD('Is it a chemical reaction?', 'Reaction?', [('🎂 baking a cake', 'yes'), ('🧊 ice melting', 'no'), ('🔥 wood burning', 'yes'), ('🍌 a banana going brown', 'yes')], o='O4'),
 TK('Tick the signs of a reaction.', ['Sign', 'Not a sign'], [('bubbles', ['✓', '✗']), ('a colour change', ['✓', '✗']), ('a new smell', ['✓', '✗'])], o='O4'),
 YN('Can most chemical reactions be undone?', False, 'O4', pic='🔄', why='No. A new material has been made.'),
 PM('A peeled banana goes brown. What caused it?', ('🌬️', 'A reaction with the air'), [('🎨', 'Someone painted it', 'It is a reaction.'), ('🌙', 'The Moon', 'It is a reaction with air.')], 'O4'),
 PM('What happens when wood burns?', ('🔥', 'It turns into ash and smoke'), [('🪵', 'It stays as wood', 'Burning makes new materials.'), ('🧊', 'It turns into ice', 'Burning makes ash and smoke.')], 'O4'),
 PM('Why must an adult help with a fizzy balloon?', ('👨‍👩‍👧', 'To stay safe'), [('🎈', 'Balloons are scary', 'It is about safety.'), ('🍋', 'Vinegar is a sweet', 'It is about safety.')], 'O4'),
 MT('Match each word to what it means.', [('reaction', 'makes a new material'), ('bubbles', 'balls of gas'), ('burn', 'catch fire')], o='O4'),
 PM('Which change can be undone?', ('🧊', 'Ice melting'), [('🎂', 'Baking a cake', 'That cannot be undone.'), ('🔥', 'Burning paper', 'That cannot be undone.')], 'O4', d='H'),
 YN('Is toasting bread a chemical reaction?', True, 'O4', pic='🍞', why='Yes! The bread turns brown and crispy – a new material.'),
 OD('Put the cake story in order.', ['mix eggs, flour and sugar', 'bake in the oven', 'a cake is made'], o='O4'),
 PM('What gas fills the fizzy balloon?', ('🫧', 'A new gas from the reaction'), [('💧', 'Water', 'It is a gas.'), ('🍋', 'Lemon juice', 'It is a gas.')], 'O4'),
 PM('Frying an egg: the clear part turns white. This is…', ('🍳', 'a chemical reaction'), [('🧊', 'freezing', 'It is cooking: a reaction.')], 'O4'),
)
s.adv(
 PM('* Advanced. Melting ice is NOT a reaction. Why?', ('💧', 'It is still water – no new material'), [('🔥', 'It needs heat', 'Reactions can need heat too.'), ('🫧', 'It makes bubbles', 'Melting ice does not fizz.')], 'O4', d='H'),
 OD('* Advanced. Order a fizzy balloon test.', ['put vinegar in the bottle', 'put baking soda in the balloon', 'fit the balloon on', 'tip it in and watch'], o='O4', d='H'),
 PM('* Advanced. More baking soda is used. What happens?', ('🎈', 'More gas, a bigger balloon'), [('📉', 'Less gas', 'More baking soda makes more gas.')], 'O4', d='H'),
)
s.labs('Reaction lab',
 test_lab('Fizzy balloon', 'Use different spoons of baking soda with the same vinegar. Read how big the balloon gets.', 'Baking soda', 'Balloon size', 'cm', 30, 3,
  'Tap the number the bar reaches.', [('1 spoon', '🥄', 9), ('2 spoons', '🥄🥄', 18), ('3 spoons', '🥄🥄🥄', 27)],
  [PM('Which made the biggest balloon?', ('🥄', '3 spoons'), [('🥄', '1 spoon', 'It made the least gas.')], 'O4')]),
 home('Fizz test', 'Make fizzy bubbles with an adult.', ['baking soda', 'vinegar or lemon juice', 'a cup', 'an adult'], ['An adult must help. Keep it away from your eyes.'],
  ['Put a spoon of baking soda in a cup.', 'Add a little vinegar.', 'Watch and listen.'],
  ['What I saw', 'My answer'], [('were there bubbles?', ['yes', 'no']), ('did I hear fizzing?', ['yes', 'no'])],
  [PM('The bubbles show…', ('🫧', 'a new gas was made'), [('💧', 'water was made', 'Bubbles are gas.')], 'O4')]))

U.mindmap(('Materials', 'solid, liquid, gas; particles', 'O1', '3.1'), ('Solids and liquids', 'shape, pour, flow', 'O2', '3.2'),
          ('Melting and freezing', 'heat melts; cooling solidifies', 'O3', '3.3'), ('Reactions', 'new materials; bubbles, colour, smell', 'O4', '3.4'))
