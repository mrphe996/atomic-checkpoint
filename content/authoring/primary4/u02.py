# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 4 · Unit 2 Energy. Written by the Atomic teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit4 import *

OBJ = {
 'O1': {'sec': '2.1', 'code': 'Physics', 'codeNote': '', 't': 'Know that everything that happens needs energy, and name kinds of energy: light, heat, sound and movement.'},
 'O2': {'sec': '2.2', 'code': 'Physics', 'codeNote': '', 't': 'Know that energy can be transferred, and that batteries, fuels and food store energy.'},
 'O3': {'sec': '2.3', 'code': 'Physics', 'codeNote': '', 't': 'Describe simple energy changes, such as electricity to light, heat, sound or movement.'},
 'O4': {'sec': '2.4', 'code': 'Biology', 'codeNote': '', 't': 'Know that plants use sunlight to make food and that animals get energy by eating; read simple food chains.'},
}
U = YUnit(2, 'Energy', 'Physics: energy', 'Light, heat, sound and movement – how energy moves, changes, and keeps every living thing going.', OBJ)

# ============================================================  2.1
s = U.section('2.1', 'Energy around us', ['O1']); s.words(V['2.1']); core(s, 'O1')
s.stop(PM('What kind of energy does a lamp give out?', ('💡', 'Light'), [('🔊', 'Sound', 'A lamp is quiet.'), ('🏃', 'Movement', 'A lamp does not move.')], 'O1'),
       PM('What kind of energy lets us see?', ('💡', 'Light'), [('🔥', 'Heat', 'Heat keeps us warm.'), ('🔊', 'Sound', 'Sound lets us hear.')], 'O1'))
s.stop(PM('What kind of energy do you hear when you hit a drum?', ('🔊', 'Sound'), [('💡', 'Light', 'You see light.'), ('🔥', 'Heat', 'Heat makes things warm.')], 'O1'),
       PM('What kind of energy keeps you warm by a fire?', ('🔥', 'Heat'), [('🔊', 'Sound', 'Sound lets you hear.'), ('🏃', 'Movement', 'Fires do not run!')], 'O1'))
s.prac(
 GD('What energy does each one give out?', 'Energy', [('☀️ the Sun', 'light and heat'), ('🎸 a guitar', 'sound'), ('🚗 a moving car', 'movement')], o='O1'),
 PM('What does a moving car have?', ('🚗', 'Movement energy'), [('🔊', 'Only sound energy', 'It is moving.'), ('🌑', 'No energy', 'Moving things have energy.')], 'O1'),
 YN('Do you need energy to run and play?', True, 'O1', pic='🏃', why='Yes! Your body uses energy from food.'),
 PM('Where does almost all our energy first come from?', ('☀️', 'The Sun'), [('🌙', 'The Moon', 'The Moon gives no energy of its own.'), ('🧊', 'Ice', 'Ice is cold.')], 'O1'),
 PM('Which of these gives out sound?', ('🔔', 'A bell'), [('🪨', 'A rock', 'A rock is quiet.'), ('🧱', 'A brick', 'A brick is quiet.')], 'O1'),
 PM('Which of these gives out heat?', ('🔥', 'A cooker'), [('🧊', 'An ice cube', 'Ice is cold.'), ('📘', 'A book', 'A book is not hot.')], 'O1'),
 TK('Does it need energy?', ['Yes', 'No'], [('a lamp shining', ['✓', '✗']), ('a ball rolling', ['✓', '✗']), ('a radio playing', ['✓', '✗'])], o='O1'),
 MT('Match each energy to what it does.', [('light', 'lets us see'), ('heat', 'keeps us warm'), ('sound', 'lets us hear')], o='O1'),
 PM('In the morning you switch on the TV. What energy does it give out?', ('📺', 'Light and sound'), [('🧊', 'Cold', 'A TV is not cold.'), ('🌑', 'Nothing', 'You can see and hear it.')], 'O1'),
 PM('What stores energy for a torch?', ('🔋', 'A battery'), [('🧦', 'A sock', 'Socks do not store energy.'), ('📄', 'Paper', 'Paper is not a battery.')], 'O1'),
 YN('Does a fire give out light as well as heat?', True, 'O1', pic='🔥', why='Yes, fires are bright and hot.'),
 PM('Which energy does a firework give out?', ('🎆', 'Light, sound and heat'), [('🧊', 'Only cold', 'Fireworks are hot!'), ('🌑', 'No energy', 'Fireworks are bright and loud.')], 'O1', d='H'),
)
s.adv(
 PM('* Advanced. A mobile phone gives out light, sound and movement (it buzzes). Where does its energy come from?', ('🔋', 'Its battery'), [('📶', 'The screen', 'The screen uses energy.'), ('☁️', 'The clouds', 'The battery stores it.')], 'O1', d='H'),
 PM('* Advanced. Why do you feel hungry after a long run?', ('🍎', 'Your body used lots of energy'), [('🌙', 'It is night', 'It is about energy.'), ('💧', 'You drank water', 'Water has no energy for your body.')], 'O1', d='H'),
 OD('* Advanced. Order from least to most energy needed.', ['sitting still', 'walking', 'running fast'], o='O1', d='H'),
)
s.labs('Energy lab',
 sort_lab('What does it give out?', 'Sort each thing by the main energy it gives out.', ['Light', 'Heat', 'Sound'],
  [('lamp', '💡', 0, 'A lamp gives light.'), ('heater', '🔥', 1, 'A heater gives heat.'), ('drum', '🥁', 2, 'A drum gives sound.'), ('torch', '🔦', 0, 'A torch gives light.'), ('bell', '🔔', 2, 'A bell gives sound.'), ('kettle', '🫖', 1, 'A kettle heats water.')],
  [PM('What does a heater give out?', ('🔥', 'Heat'), [('🔊', 'Sound', 'Mostly heat.')], 'O1')]),
 home('Energy hunt', 'Find things at home that use energy.', ['paper and crayons'], ['Do not touch anything hot or plugged in.'],
  ['Walk round your home.', 'Find things that use energy.', 'What do they give out?'],
  ['Thing', 'Main energy'], [('lamp', ['light', 'heat', 'sound']), ('radio', ['light', 'heat', 'sound']), ('oven', ['light', 'heat', 'sound'])],
  [PM('Which thing gives out sound?', ('📻', 'A radio'), [('💡', 'A lamp', 'A lamp gives light.')], 'O1')]))

# ============================================================  2.2
s = U.section('2.2', 'Energy transfers', ['O2']); s.words(V['2.2']); core(s, 'O2')
s.stop(PM('When you kick a ball, where does the energy go?', ('⚽', 'Into the ball'), [('🌙', 'To the Moon', 'It goes to the ball.'), ('👟', 'It disappears', 'It moves to the ball.')], 'O2'),
       PM('What does “transfer” mean?', ('➡️', 'Move from one thing to another'), [('🛑', 'Stop', 'Transfer means move.'), ('🎨', 'Change colour', 'Transfer means move.')], 'O2'))
s.stop(PM('Which of these stores energy?', ('🔋', 'A battery'), [('🪨', 'A pebble', 'A pebble is not an energy store we use.'), ('🧦', 'A sock', 'Socks do not store energy.')], 'O2'),
       PM('Which is a fuel?', ('🪵', 'Wood'), [('💧', 'Water', 'Water does not burn.'), ('🧊', 'Ice', 'Ice does not burn.')], 'O2'))
s.prac(
 PM('What gives your body energy?', ('🍎', 'Food'), [('📺', 'TV', 'TV does not give you energy.'), ('🧸', 'Toys', 'Food gives you energy.')], 'O2'),
 OD('Put the energy transfer in order.', ['food', 'your body', 'the ball'], o='O2'),
 GD('Does it store energy?', 'Stores energy?', [('🔋 battery', 'yes'), ('🍞 bread', 'yes'), ('🪵 wood', 'yes'), ('🧊 ice', 'no')], o='O2'),
 YN('Does a car need fuel to move?', True, 'O2', pic='🚗', why='Yes. Petrol or electricity gives the car energy.'),
 PM('A torch is not working. What is the most likely problem?', ('🔋', 'The battery is flat'), [('🎨', 'It is the wrong colour', 'Colour does not matter.'), ('📏', 'It is too long', 'Size does not matter.')], 'O2'),
 PM('Which ball bounces higher?', ('⬆️', 'A ball dropped from high up'), [('⬇️', 'A ball dropped from low down', 'It has less energy.')], 'O2'),
 PM('What is petrol used for?', ('⛽', 'Fuel for cars'), [('🥤', 'A drink', 'Never drink petrol!'), ('🧼', 'Washing', 'It is a fuel.')], 'O2'),
 MT('Match each store of energy to what uses it.', [('battery', 'toy car'), ('food', 'your body'), ('wood', 'a campfire')], o='O2'),
 YN('Can energy move from your hand to a toy car when you push it?', True, 'O2', pic='🚗', why='Yes. The push transfers energy.'),
 TK('Tick the energy stores.', ['Yes', 'No'], [('a battery', ['✓', '✗']), ('a sandwich', ['✓', '✗']), ('a shadow', ['✗', '✓'])], o='O2'),
 PM('Why do we put batteries in a remote control?', ('🔋', 'They give it energy'), [('⚖️', 'To make it heavy', 'They store energy.'), ('🎨', 'To decorate it', 'They store energy.')], 'O2'),
 PM('When you hit a drum, energy goes from your hand to the drum. What comes out?', ('🔊', 'Sound'), [('💧', 'Water', 'Drums make sound.'), ('🌈', 'A rainbow', 'Drums make sound.')], 'O2'),
)
s.adv(
 PM('* Advanced. A bouncing ball bounces lower each time. Why?', ('📉', 'It loses a little energy each bounce'), [('📈', 'It gains energy', 'It bounces lower.'), ('🧊', 'It gets colder', 'It is about energy.')], 'O2', d='H'),
 OD('* Advanced. Order the energy journey.', ['the Sun', 'grass grows', 'a cow eats grass', 'milk', 'you'], o='O2', d='H'),
 PM('* Advanced. Why do we charge a phone every day?', ('🔋', 'Its battery store gets used up'), [('🌙', 'Phones sleep', 'It is about energy.'), ('🧽', 'To clean it', 'It is about energy.')], 'O2', d='H'),
)
s.labs('Bounce lab',
 test_lab('Bouncing balls', 'Drop a ball from different heights. Read how high it bounces.', 'Drop height', 'Bounce height', 'cm', 100, 10,
  'Tap the number the bar reaches.', [('low drop', '⬇️', 20), ('middle drop', '↔️', 50), ('high drop', '⬆️', 80)],
  [PM('Which drop gave the highest bounce?', ('⬆️', 'The high drop'), [('⬇️', 'The low drop', 'It bounced least.')], 'O2')]),
 home('Ball bounce test', 'Drop a ball from different heights.', ['a ball', 'a ruler or tape measure', 'a partner'], ['Drop the ball, never throw it at people.'],
  ['Drop the ball from knee height.', 'Drop it from waist height.', 'Drop it from shoulder height.'],
  ['Drop from', 'Bounce was'], [('knee', ['low', 'middle', 'high']), ('waist', ['low', 'middle', 'high']), ('shoulder', ['low', 'middle', 'high'])],
  [PM('Which drop gave the ball the most energy?', ('🙋', 'From the shoulder'), [('🦵', 'From the knee', 'That was the lowest.')], 'O2')]))

# ============================================================  2.3
s = U.section('2.3', 'Energy changes', ['O3']); s.words(V['2.3']); core(s, 'O3')
s.stop(PM('What does a kettle change electricity into?', ('🔥', 'Heat'), [('🔊', 'Only sound', 'It heats water.'), ('💡', 'Only light', 'It heats water.')], 'O3'),
       PM('What does a light bulb change electricity into?', ('💡', 'Light'), [('🌀', 'Wind', 'A bulb gives light.'), ('🧊', 'Ice', 'A bulb gives light.')], 'O3'))
s.stop(PM('What does a fan change electricity into?', ('🌀', 'Movement'), [('💡', 'Light', 'A fan spins.'), ('🔥', 'Heat', 'A fan cools you.')], 'O3'),
       PM('What does a speaker change electricity into?', ('🔊', 'Sound'), [('🔥', 'Heat', 'A speaker plays music.'), ('🧊', 'Ice', 'A speaker plays music.')], 'O3'))
s.prac(
 GD('What does each one change electricity into?', 'Changes it into', [('🫖 kettle', 'heat'), ('💡 lamp', 'light'), ('🔊 speaker', 'sound'), ('🌀 fan', 'movement')], o='O3'),
 PM('Rub your hands together fast. What do you feel?', ('🔥', 'Warmth'), [('🧊', 'Cold', 'Rubbing makes heat.'), ('💧', 'Wetness', 'Rubbing makes heat.')], 'O3'),
 YN('Can energy change from one kind to another?', True, 'O3', pic='🔄', why='Yes! A bulb changes electricity into light.'),
 PM('A toaster changes electricity into…', ('🍞', 'heat to make toast'), [('🎵', 'music', 'A toaster toasts bread.'), ('🌀', 'wind', 'A toaster toasts bread.')], 'O3'),
 PM('Which saves more energy?', ('💡', 'A new LED bulb'), [('🔥', 'An old hot bulb', 'It wastes energy as heat.')], 'O3'),
 MT('Match each word to what it means.', [('bulb', 'light'), ('kettle', 'heat'), ('radio', 'sound')], o='O3'),
 YN('Does a hairdryer give out heat and movement (wind)?', True, 'O3', pic='💨', why='Yes, it blows warm air.'),
 PM('In a torch, energy goes from the battery to the…', ('💡', 'bulb'), [('🧦', 'sock', 'It goes to the bulb.'), ('🎒', 'bag', 'It goes to the bulb.')], 'O3'),
 TK('Tick what uses electricity.', ['Yes', 'No'], [('a lamp', ['✓', '✗']), ('a kettle', ['✓', '✗']), ('a bicycle', ['✗', '✓'])], o='O3'),
 OD('Put the torch energy change in order.', ['battery', 'electricity in wires', 'bulb', 'light'], o='O3'),
 PM('Why should you switch off lights you are not using?', ('🌍', 'To save energy'), [('🌙', 'To make night', 'To save energy.'), ('🎨', 'To change colours', 'To save energy.')], 'O3'),
 PM('Which change happens when you clap?', ('👏', 'Movement to sound'), [('💡', 'Light to heat', 'Clapping makes a sound.')], 'O3', d='H'),
)
s.adv(
 PM('* Advanced. An old bulb gets very hot. What does this show?', ('🔥', 'Some energy is wasted as heat'), [('💡', 'It makes more light', 'Heat is wasted energy.'), ('🧊', 'It is cold', 'It gets hot.')], 'O3', d='H'),
 PM('* Advanced. A wind-up toy moves. Where did the energy come from?', ('✋', 'Your hand winding it up'), [('🔋', 'A battery', 'A wind-up toy has no battery.'), ('☀️', 'The Moon', 'You gave it energy.')], 'O3', d='VH'),
 OD('* Advanced. Order the energy changes in a radio.', ['electricity', 'the radio', 'sound'], o='O3', d='H'),
)
s.labs('Energy change lab',
 sort_lab('What does it change electricity into?', 'Sort each machine.', ['Heat', 'Light', 'Sound', 'Movement'],
  [('kettle', '🫖', 0, 'A kettle heats water.'), ('lamp', '💡', 1, 'A lamp lights the room.'), ('radio', '📻', 2, 'A radio plays sound.'), ('fan', '🌀', 3, 'A fan spins.'), ('toaster', '🍞', 0, 'A toaster heats bread.'), ('doorbell', '🔔', 2, 'A doorbell rings.')],
  [PM('What does a fan change electricity into?', ('🌀', 'Movement'), [('🔥', 'Heat', 'A fan spins.')], 'O3')]),
 home('Rub and feel', 'Feel movement change into heat.', ['your hands', 'a ruler'], ['Rub gently. Stop if it hurts.'],
  ['Feel your hands.', 'Rub them fast for 10 seconds.', 'Feel them again.'],
  ['Question', 'My answer'], [('were my hands warmer after rubbing?', ['yes', 'no']), ('did rubbing faster make more heat?', ['yes', 'no'])],
  [PM('Rubbing changes movement into…', ('🔥', 'heat'), [('💡', 'light', 'You felt warmth.')], 'O3')]))

# ============================================================  2.4
s = U.section('2.4', 'Energy and living things', ['O4']); s.words(V['2.4']); core(s, 'O4')
s.stop(PM('Where does a plant get its energy from?', ('☀️', 'Sunlight'), [('🍔', 'Burgers', 'Plants do not eat burgers!'), ('🌙', 'The Moon', 'Plants use sunlight.')], 'O4'),
       PM('What do plants make in their leaves?', ('🍃', 'Their own food'), [('🪨', 'Rocks', 'Plants make food.'), ('💧', 'Rain', 'Plants make food.')], 'O4'))
s.stop(PM('In the food chain grass → rabbit → fox, which animal eats the rabbit?', ('🦊', 'The fox'), [('🌿', 'The grass', 'Grass is a plant.'), ('🐰', 'The rabbit', 'The rabbit is eaten.')], 'O4'),
       PM('In the food chain grass → rabbit → fox, what does the rabbit eat?', ('🌿', 'Grass'), [('🦊', 'The fox', 'The fox eats the rabbit.'), ('🥕', 'Pizza', 'Rabbits eat plants.')], 'O4'))
s.prac(
 PM('What is always first in a food chain?', ('🌱', 'A plant'), [('🦁', 'A lion', 'Lions come at the end.'), ('🧒', 'A person', 'A plant comes first.')], 'O4'),
 OD('Put the food chain in order.', ['leaf', 'caterpillar', 'bird'], o='O4'),
 GD('Producer or consumer?', 'Group', [('🌿 grass', 'producer'), ('🐰 rabbit', 'consumer'), ('🌳 tree', 'producer'), ('🦊 fox', 'consumer')], o='O4'),
 YN('Can animals make their own food from sunlight?', False, 'O4', pic='🐶', why='No. Animals must eat plants or other animals.'),
 PM('What do the arrows in a food chain show?', ('➡️', 'Where the energy goes'), [('🏃', 'Which way animals run', 'They show the energy.'), ('🌬️', 'The wind', 'They show the energy.')], 'O4'),
 PM('You eat bread. Bread is made from wheat. What gave the wheat energy?', ('☀️', 'The Sun'), [('🧈', 'Butter', 'Plants use sunlight.'), ('🌙', 'The Moon', 'Plants use sunlight.')], 'O4'),
 MT('Match each word to what it means.', [('producer', 'makes its own food'), ('consumer', 'eats other living things'), ('sunlight', 'gives plants energy')], o='O4'),
 PM('Which animal eats only plants?', ('🐄', 'A cow'), [('🦁', 'A lion', 'Lions eat meat.'), ('🦈', 'A shark', 'Sharks eat fish.')], 'O4'),
 YN('Do plants need sunlight to grow?', True, 'O4', pic='🌱', why='Yes. They use it to make food.'),
 TK('Tick the consumers.', ['Consumer', 'Producer'], [('cat', ['✓', '✗']), ('apple tree', ['✗', '✓']), ('bee', ['✓', '✗'])], o='O4'),
 PM('A plant is kept in a dark cupboard for weeks. What happens?', ('🥀', 'It gets weak and yellow'), [('🌻', 'It grows big and green', 'It needs light.'), ('🍎', 'It grows fruit', 'It needs light.')], 'O4'),
 PM('Which is a correct food chain?', ('🌿', 'grass → zebra → lion'), [('🦁', 'lion → grass → zebra', 'Plants come first.'), ('🦓', 'zebra → lion → grass', 'Plants come first.')], 'O4', d='H'),
)
s.adv(
 PM('* Advanced. If all the rabbits disappeared, what would happen to the foxes?', ('🦊', 'They would go hungry'), [('🎉', 'They would have more food', 'They eat rabbits.'), ('🌿', 'They would eat sunlight', 'Animals cannot.')], 'O4', d='H'),
 PM('* Advanced. Why is the Sun important to a lion, which eats meat?', ('☀️', 'The Sun helps grass grow, which the zebra eats'), [('🕶️', 'Lions like sunbathing', 'It is about food chains.'), ('🌙', 'It is not important', 'The Sun starts every food chain.')], 'O4', d='VH'),
 OD('* Advanced. Order this food chain.', ['seaweed', 'small fish', 'big fish', 'shark'], o='O4', d='H'),
)
s.labs('Food chain lab',
 sort_lab('Producer or consumer?', 'Sort each living thing.', ['Producer (makes food)', 'Consumer (eats)'],
  [('grass', '🌿', 0, 'Grass makes food from sunlight.'), ('rabbit', '🐰', 1, 'A rabbit eats grass.'), ('tree', '🌳', 0, 'Trees make food.'), ('owl', '🦉', 1, 'Owls eat mice.'), ('sunflower', '🌻', 0, 'It makes food.'), ('caterpillar', '🐛', 1, 'It eats leaves.')],
  [PM('Which one is a producer?', ('🌳', 'Tree'), [('🦉', 'Owl', 'Owls eat other animals.')], 'O4')]),
 home('Plant in the dark', 'Test what happens without light.', ['two small plants', 'a dark cupboard', 'water'], ['Wash your hands after touching soil.'],
  ['Put one plant on a sunny window.', 'Put one in a dark cupboard.', 'Water both the same.', 'Look after one week.'],
  ['Plant', 'How did it look?'], [('sunny window', ['green and strong', 'yellow and weak']), ('dark cupboard', ['green and strong', 'yellow and weak'])],
  [PM('What does a plant need to stay green and strong?', ('☀️', 'Light'), [('🌑', 'Darkness', 'The plant in the dark got weak.')], 'O4')]))

U.mindmap(('Kinds of energy', 'light, heat, sound, movement', 'O1', '2.1'), ('Energy transfers', 'energy moves; batteries, fuel, food', 'O2', '2.2'),
          ('Energy changes', 'electricity to light, heat, sound, movement', 'O3', '2.3'), ('Living things', 'sunlight, producers, consumers, food chains', 'O4', '2.4'))
