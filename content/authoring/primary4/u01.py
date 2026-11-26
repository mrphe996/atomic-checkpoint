# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 4 · Unit 1 Living things. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit4 import *

OBJ = {
 'O1': {'sec': '1.1', 'code': 'Biology', 'codeNote': '', 't': 'Know that some animals have a skeleton of bones, and name some bones (skull, ribs, spine).'},
 'O2': {'sec': '1.2', 'code': 'Biology', 'codeNote': '', 't': 'Describe the jobs of a skeleton: support, protection and movement.'},
 'O3': {'sec': '1.3', 'code': 'Biology', 'codeNote': '', 't': 'Know that muscles pull on bones to move them, and that muscles work in pairs.'},
 'O4': {'sec': '1.4', 'code': 'Biology', 'codeNote': '', 't': 'Sort animals into vertebrates and invertebrates, and know that some animals have a skeleton outside.'},
 'O5': {'sec': '1.5', 'code': 'Biology', 'codeNote': '', 't': 'Know that germs can spread infections, how to stop them spreading, and how to use medicines safely.'},
}
U = YUnit(1, 'Living things', 'Biology: structure and function', 'Bones, skeletons, muscles, animals with and without a backbone, and staying healthy.', OBJ)

# ============================================================  1.1
s = U.section('1.1', 'Bones and skeletons', ['O1']); s.words(V['1.1']); core(s, 'O1')
s.stop(PM('What do all your bones together make?', ('🧍', 'A skeleton'), [('💪', 'A muscle', 'Muscles move bones.'), ('🧠', 'A brain', 'The brain is soft, inside the skull.')], 'O1'),
       PM('What are the hard parts inside your body called?', ('🦴', 'Bones'), [('🩸', 'Blood', 'Blood is a liquid.'), ('💨', 'Air', 'Air is in your lungs.')], 'O1'))
s.stop(PM('Which bone protects your brain?', ('🧠', 'The skull'), [('🫁', 'The ribs', 'Ribs protect your heart and lungs.'), ('🦵', 'The leg bone', 'Your leg bone helps you stand.')], 'O1'),
       PM('Which bones make a cage around your heart?', ('🫁', 'The ribs'), [('🧠', 'The skull', 'The skull is around the brain.'), ('✋', 'The hand bones', 'Hand bones help you hold things.')], 'O1'))
s.prac(
 PM('Squeeze your arm gently. What hard part can you feel?', ('🦴', 'A bone'), [('💧', 'Water', 'Water is not hard.'), ('🎈', 'Air', 'Air is not hard.')], 'O1'),
 PM('Where is the longest bone in your body?', ('🦵', 'In your leg'), [('👂', 'In your ear', 'The smallest bone is in your ear.'), ('✋', 'In your hand', 'Hand bones are small.')], 'O1'),
 PM('Where is the smallest bone in your body?', ('👂', 'In your ear'), [('🦵', 'In your leg', 'The leg bone is the longest.'), ('🫁', 'In your chest', 'Your ribs are in your chest.')], 'O1'),
 YN('Does a baby have more bones than a grown-up?', True, 'O1', pic='👶', why='Yes! Some of a baby\'s bones join together as it grows.'),
 PM('Which part of your body is like a helmet?', ('⛑️', 'Your skull'), [('🦶', 'Your feet', 'Feet help you stand.'), ('🫁', 'Your ribs', 'Ribs are like a cage.')], 'O1'),
 PM('Which bones run down the middle of your back?', ('🔗', 'The spine'), [('🫁', 'The ribs', 'Ribs are in your chest.'), ('🧠', 'The skull', 'The skull is in your head.')], 'O1'),
 GD('Where is each bone?', 'Where', [('🧠 skull', 'head'), ('🫁 ribs', 'chest'), ('🔗 spine', 'back')], o='O1'),
 PM('Mia fell off her bike and her arm hurts a lot. Who should check if a bone is broken?', ('👩‍⚕️', 'A doctor'), [('🧑‍🍳', 'A cook', 'A cook makes food.'), ('🧑‍🚒', 'A firefighter', 'A firefighter puts out fires.')], 'O1'),
 YN('Can you see your bones without an X-ray?', False, 'O1', pic='🩻', why='No. Bones are inside your body. An X-ray photo lets doctors see them.'),
 PM('How many bones does a grown-up have?', ('🔢', 'About 206'), [('2️⃣', 'About 2', 'We have many more!'), ('🔟', 'About 10', 'We have many more!')], 'O1', d='H'),
 TK('Tick what is true.', ['True', 'False'], [('bones are hard', ['✓', '✗']), ('bones are inside your body', ['✓', '✗']), ('your skull is in your foot', ['✗', '✓'])], o='O1'),
 PM('Which food helps your bones grow strong?', ('🥛', 'Milk'), [('🍬', 'Sweets', 'Sweets are not good for bones.'), ('🥤', 'Fizzy drinks', 'Fizzy drinks are not good for bones.')], 'O1'),
)
s.adv(
 PM('* Advanced. Why can a baby bend more easily than a grown-up?', ('👶', 'Its bones are softer and have not all joined'), [('🦴', 'It has no bones', 'Babies do have bones.'), ('💪', 'It has bigger muscles', 'Babies have small muscles.')], 'O1', d='H'),
 PM('* Advanced. An X-ray shows a crack in a bone. What happened?', ('🩻', 'The bone is broken'), [('😊', 'The bone is healthy', 'A crack means it is broken.'), ('🧊', 'The bone is frozen', 'Bones do not freeze inside us.')], 'O1', d='H'),
 OD('* Advanced. Put these bones in order from the top of your body to the bottom.', ['skull', 'ribs', 'leg bone'], o='O1', d='H'),
)
s.labs('Bone lab',
 sort_lab('Hard or soft?', 'Sort each body part: is it hard like bone, or soft?', ['Hard (bone)', 'Soft'],
  [('skull', '🧠', 0, 'The skull is a hard bone.'), ('ribs', '🫁', 0, 'Ribs are bones.'), ('tongue', '👅', 1, 'Your tongue is soft – it is a muscle.'), ('spine', '🔗', 0, 'The spine is made of bones.'), ('ear lobe', '👂', 1, 'Your ear lobe is soft.'), ('knee cap', '🦵', 0, 'Your knee cap is a bone.')],
  [PM('Which of these is soft?', ('👅', 'Your tongue'), [('🧠', 'Your skull', 'The skull is hard.'), ('🔗', 'Your spine', 'The spine is hard.')], 'O1')]),
 home('Bone hunt', 'Find bones you can feel in your body.', ['a partner', 'paper and crayons'], ['Press gently. Never press hard on anyone.'],
  ['Feel your arm. Can you feel a bone?', 'Feel your knee.', 'Feel your head.', 'Feel your back.'],
  ['Where I felt', 'Hard bone or soft?'], [('my arm', ['hard bone', 'soft']), ('my knee', ['hard bone', 'soft']), ('my head', ['hard bone', 'soft']), ('my nose tip', ['hard bone', 'soft'])],
  [PM('The tip of your nose is soft. Is it a bone?', ('🙅', 'No'), [('🦴', 'Yes', 'Bones are hard. The tip of your nose is soft.')], 'O1')]))

# ============================================================  1.2
s = U.section('1.2', 'Why we need a skeleton', ['O2']); s.words(V['1.2']); core(s, 'O2')
s.stop(PM('What would happen to your body without a skeleton?', ('🪼', 'It would be floppy'), [('🏃', 'It would run faster', 'Without bones you could not stand.'), ('📏', 'It would be taller', 'Bones hold you up.')], 'O2'),
       PM('What holds up a tent, like a skeleton holds you up?', ('⛺', 'The poles'), [('🎒', 'The bag', 'The bag carries the tent.'), ('🧵', 'The string', 'String ties the tent down.')], 'O2'))
s.stop(PM('Your skull covers your brain. Which job is it doing?', ('🛡️', 'Protecting'), [('🏃', 'Moving', 'The skull does not help you move.'), ('🍎', 'Eating', 'Bones do not eat.')], 'O2'),
       PM('Your ribs cover your heart and lungs. Which job are they doing?', ('🛡️', 'Protecting'), [('🏗️', 'Holding up a tent', 'That is not a body job.'), ('🎵', 'Singing', 'Ribs do not sing.')], 'O2'))
s.prac(
 GD('Which job is each part of the skeleton doing?', 'Job', [('🧠 skull covers the brain', 'protect'), ('🦵 leg bones let you stand', 'support'), ('💪 arm bones help you throw', 'move')], o='O2'),
 PM('Which job of the skeleton helps you stand up tall?', ('🏗️', 'Support'), [('🛡️', 'Protect', 'Protecting keeps soft parts safe.'), ('🎨', 'Colour', 'That is not a job of the skeleton.')], 'O2'),
 PM('What is another name for the spine?', ('🦴', 'Backbone'), [('🫁', 'Rib', 'Ribs are in your chest.'), ('👂', 'Ear bone', 'That is in your ear.')], 'O2'),
 YN('Can you bend down to touch your toes because your spine has many small bones?', True, 'O2', pic='🙇', why='Yes! The small bones can move a little, so your back can bend.'),
 PM('A jellyfish has no bones. What is its body like?', ('🪼', 'Soft and floppy'), [('🧱', 'Hard and stiff', 'No bones means it is soft.'), ('🌳', 'Tall like a tree', 'It cannot stand up.')], 'O2'),
 PM('Why do footballers and cyclists wear helmets and pads?', ('⛑️', 'To protect their bones'), [('🎨', 'To look colourful', 'They are for safety.'), ('🌧️', 'To stay dry', 'They are for safety.')], 'O2'),
 YN('Does a giraffe have more neck bones than you?', False, 'O2', pic='🦒', why='No! It has seven neck bones, like you. Each one is just very long.'),
 MT('Match each job to what it means.', [('support', 'hold the body up'), ('protect', 'keep soft parts safe'), ('move', 'help the body go from place to place')], o='O2'),
 TK('Tick the jobs of your skeleton.', ['Yes', 'No'], [('supports your body', ['✓', '✗']), ('protects your brain', ['✓', '✗']), ('helps you move', ['✓', '✗']), ('digests your food', ['✗', '✓'])], o='O2'),
 PM('What gives your body its shape?', ('🧍', 'Your skeleton'), [('👕', 'Your clothes', 'Clothes do not hold you up.'), ('💇', 'Your hair', 'Hair does not hold you up.')], 'O2'),
 PM('What has a spine but no bones?', ('📚', 'A book'), [('🐟', 'A fish', 'A fish has bones.'), ('🐕', 'A dog', 'A dog has bones.')], 'O2'),
 PM('Leo jumps on a trampoline. Which job of his skeleton is helping him?', ('🏃', 'Moving'), [('🧠', 'Thinking', 'Your brain thinks.'), ('🍽️', 'Eating', 'Your teeth help you eat.')], 'O2'),
)
s.adv(
 PM('* Advanced. Why are the bones that protect the brain joined tightly together?', ('🛡️', 'So they make a strong, hard case'), [('🏃', 'So the head can bend', 'The skull does not need to bend.'), ('🎵', 'So we can hear', 'Hearing is not the skull\'s job.')], 'O2', d='H'),
 PM('* Advanced. Which job would be hardest without leg bones?', ('🧍', 'Standing up'), [('👀', 'Seeing', 'Eyes help you see.'), ('👂', 'Hearing', 'Ears help you hear.')], 'O2', d='H'),
 OD('* Advanced. Order from softest to hardest.', ['jellyfish body', 'your tongue', 'your skull'], o='O2', d='H'),
)
s.labs('Skeleton lab',
 sort_lab('What is the job?', 'Sort each picture by the job the skeleton is doing.', ['Support', 'Protect', 'Move'],
  [('standing tall', '🧍', 0, 'Bones hold you up.'), ('skull around the brain', '🧠', 1, 'The skull keeps the brain safe.'), ('running', '🏃', 2, 'Bones and muscles move you.'), ('ribs around the heart', '❤️', 1, 'Ribs protect the heart.'), ('kicking a ball', '⚽', 2, 'Your leg bones move.'), ('sitting up straight', '🪑', 0, 'Your spine holds you up.')],
  [PM('The ribs keep the heart safe. Which job is this?', ('🛡️', 'Protect'), [('🏃', 'Move', 'Ribs do not help you run.'), ('🏗️', 'Support', 'This is about keeping safe.')], 'O2')]),
 home('Paper skeleton', 'Make a skeleton that moves.', ['card', 'scissors (ask an adult)', 'paper pins'], ['Ask an adult to help with the scissors.'],
  ['Cut out a head, body, arms and legs.', 'Join them with paper pins.', 'Move the arms and legs.', 'Find where it bends.'],
  ['Part', 'Can it bend?'], [('arms', ['yes', 'no']), ('legs', ['yes', 'no']), ('head', ['yes', 'no'])],
  [PM('Where does your real arm bend?', ('💪', 'At the elbow'), [('✋', 'At the fingernails', 'Nails do not bend.'), ('👂', 'At the ear', 'Your ear is on your head.')], 'O2')]))

# ============================================================  1.3
s = U.section('1.3', 'Skeletons and muscles', ['O3']); s.words(V['1.3']); core(s, 'O3')
s.stop(PM('What do muscles do to move your bones?', ('💪', 'They pull'), [('🫸', 'They push', 'Muscles can only pull.'), ('😴', 'They sleep', 'Working muscles pull.')], 'O3'),
       PM('Bend your arm. What gets hard and fat?', ('💪', 'A muscle'), [('🦴', 'A bone', 'Bones stay the same.'), ('💇', 'Your hair', 'Hair does not move your arm.')], 'O3'))
s.stop(PM('What is the place where two bones meet?', ('🦵', 'A joint'), [('💪', 'A muscle', 'Muscles pull bones.'), ('🧠', 'A brain', 'The brain is in your head.')], 'O3'),
       PM('Which of these is a joint?', ('🦵', 'Your knee'), [('👃', 'Your nose', 'Your nose does not bend.'), ('💇', 'Your hair', 'Hair is not a joint.')], 'O3'))
s.prac(
 PM('When a muscle contracts, what does it do?', ('🤏', 'Gets shorter and fatter'), [('📏', 'Gets longer', 'That is relaxing.'), ('💤', 'Goes to sleep', 'It is working!')], 'O3'),
 PM('Muscles work in…', ('👯', 'pairs'), [('1️⃣', 'ones', 'Each muscle has a partner.'), ('🔟', 'tens', 'They work in twos.')], 'O3'),
 GD('Is it a joint?', 'Joint?', [('🦵 knee', 'yes'), ('💪 elbow', 'yes'), ('👃 nose', 'no'), ('🤚 wrist', 'yes')], o='O3'),
 YN('Does exercise make your muscles stronger?', True, 'O3', pic='🤸', why='Yes! Muscles get stronger when you use them.'),
 PM('You use muscles to smile. Where are they?', ('😁', 'In your face'), [('🦶', 'In your feet', 'You smile with your face.'), ('💇', 'In your hair', 'Hair has no muscles.')], 'O3'),
 PM('After running, which muscles feel tired?', ('🦵', 'Leg muscles'), [('👂', 'Ear muscles', 'You run with your legs.'), ('👃', 'Nose muscles', 'You run with your legs.')], 'O3'),
 OD('Put the steps in order to bend your arm.', ['your brain sends a message', 'the top muscle contracts', 'your arm bends'], o='O3'),
 YN('Can a bone move on its own, without a muscle?', False, 'O3', pic='🦴', why='No. Bones need muscles to pull them.'),
 PM('What should you do after lots of exercise?', ('🥤', 'Rest and drink water'), [('🍬', 'Eat lots of sweets', 'Water is better.'), ('🏃', 'Run even faster', 'Muscles need rest.')], 'O3'),
 MT('Match each word to what it means.', [('contract', 'get short and fat'), ('relax', 'get long and soft'), ('joint', 'where bones meet')], o='O3'),
 PM('Which animal has very strong leg muscles for jumping?', ('🦘', 'A kangaroo'), [('🐌', 'A snail', 'Snails do not jump.'), ('🐟', 'A fish', 'Fish swim.')], 'O3'),
 TK('Tick what is true.', ['True', 'False'], [('muscles pull bones', ['✓', '✗']), ('muscles work in pairs', ['✓', '✗']), ('bones move by themselves', ['✗', '✓'])], o='O3'),
)
s.adv(
 PM('* Advanced. To straighten your arm, what happens?', ('🔄', 'The top muscle relaxes and the bottom one contracts'), [('💪', 'The top muscle contracts again', 'They must swap jobs.'), ('🦴', 'The bone pushes itself', 'Bones cannot move alone.')], 'O3', d='H'),
 PM('* Advanced. Why can muscles only pull, never push?', ('🤏', 'They can only get shorter to pull'), [('🫸', 'They are too weak to push', 'It is about getting shorter.'), ('🦴', 'Bones stop them', 'Bones are what they pull.')], 'O3', d='VH'),
 OD('* Advanced. Order these from the shortest muscle to the longest: when you bend your arm, the top muscle is…', ['contracted (short)', 'normal', 'relaxed (long)'], o='O3', d='H'),
)
s.labs('Muscle lab',
 test_lab('Jumping and heartbeat', 'Jump for different times. Count how tired your legs feel on a scale of 0 to 10.', 'How long I jumped', 'Tiredness', 'points', 10, 1,
  'Tap the number the bar reaches.', [('10 seconds', '🐇', 2), ('30 seconds', '🦘', 5), ('1 minute', '🏃', 8)],
  [PM('Which made the legs most tired?', ('🏃', 'Jumping for 1 minute'), [('🐇', 'Jumping for 10 seconds', 'That was the shortest time.')], 'O3')]),
 home('Feel your muscles', 'Feel your muscles working.', ['a chair'], ['Do not lift anything heavy.'],
  ['Bend your arm and feel the top.', 'Stand on tiptoe and feel your leg.', 'Smile and feel your cheeks.'],
  ['What I did', 'Did the muscle get hard?'], [('bend my arm', ['yes', 'no']), ('stand on tiptoe', ['yes', 'no']), ('smile', ['yes', 'no'])],
  [PM('When you stand on tiptoe, where do muscles work?', ('🦵', 'In your legs'), [('👂', 'In your ears', 'You stand with your legs.')], 'O3')]))

# ============================================================  1.4
s = U.section('1.4', 'Different kinds of skeletons', ['O4']); s.words(V['1.4']); core(s, 'O4')
s.stop(PM('What do we call animals with a backbone?', ('🐶', 'Vertebrates'), [('🐛', 'Invertebrates', 'Invertebrates have no backbone.'), ('🌱', 'Plants', 'Plants are not animals.')], 'O4'),
       PM('Which animal has a backbone?', ('🐟', 'A fish'), [('🐛', 'A worm', 'Worms have no bones.'), ('🐌', 'A snail', 'Snails have no backbone.')], 'O4'))
s.stop(PM('Which animal has no backbone?', ('🐛', 'A worm'), [('🐸', 'A frog', 'Frogs have a backbone.'), ('🐦', 'A bird', 'Birds have a backbone.')], 'O4'),
       PM('Which animal is an invertebrate?', ('🐌', 'A snail'), [('🐶', 'A dog', 'Dogs have a backbone.'), ('🐟', 'A fish', 'Fish have a backbone.')], 'O4'))
s.prac(
 GD('Does it have a backbone?', 'Backbone?', [('🐶 dog', 'yes'), ('🐛 worm', 'no'), ('🐟 fish', 'yes'), ('🐜 ant', 'no'), ('🐸 frog', 'yes')], o='O4'),
 PM('Which animal wears its skeleton on the outside?', ('🦀', 'A crab'), [('🐕', 'A dog', 'A dog\'s bones are inside.'), ('🐛', 'A worm', 'A worm has no skeleton.')], 'O4'),
 PM('What protects a snail\'s soft body?', ('🐚', 'Its shell'), [('🦴', 'Bones', 'Snails have no bones.'), ('🧥', 'A coat', 'Snails do not wear coats!')], 'O4'),
 YN('Is a butterfly an invertebrate?', True, 'O4', pic='🦋', why='Yes. Insects have no backbone.'),
 YN('Is a person a vertebrate?', True, 'O4', pic='🧒', why='Yes! You have a backbone.'),
 PM('An octopus can squeeze through a tiny hole. Why?', ('🐙', 'It has no bones'), [('🦴', 'Its bones are small', 'It has no bones at all.'), ('🧊', 'It is very cold', 'That is not the reason.')], 'O4'),
 PM('How many legs does an insect have?', ('6️⃣', 'Six'), [('8️⃣', 'Eight', 'Spiders have eight.'), ('4️⃣', 'Four', 'Dogs have four.')], 'O4'),
 PM('Which animal is NOT a vertebrate?', ('🐞', 'A ladybird'), [('🐦', 'A bird', 'Birds have a backbone.'), ('🐍', 'A snake', 'Snakes have a long backbone!')], 'O4', d='H'),
 MT('Match each animal to its skeleton.', [('dog', 'bones inside'), ('crab', 'hard outside'), ('worm', 'no skeleton')], o='O4'),
 YN('Does a snake have a backbone?', True, 'O4', pic='🐍', why='Yes! A snake has a very long backbone with lots of bones.'),
 PM('You find a small animal under a stone. It has 6 legs and a hard outside. What is it?', ('🐜', 'An insect'), [('🐟', 'A fish', 'Fish live in water.'), ('🐶', 'A dog', 'Dogs are much bigger.')], 'O4'),
 TK('Tick what is true.', ['True', 'False'], [('insects are invertebrates', ['✓', '✗']), ('fish are vertebrates', ['✓', '✗']), ('a crab has bones inside', ['✗', '✓'])], o='O4'),
)
s.adv(
 PM('* Advanced. Why does a crab need a hard outside?', ('🛡️', 'To protect its soft body'), [('🎨', 'To look pretty', 'It is for protection.'), ('🏊', 'To swim faster', 'It is for protection.')], 'O4', d='H'),
 PM('* Advanced. A snail grows bigger. What happens to its shell?', ('🐚', 'It grows with the snail'), [('🗑️', 'It falls off', 'The shell grows too.'), ('🔄', 'It finds a new one', 'Snails keep their shell.')], 'O4', d='VH'),
 GD('* Advanced. Sort these animals.', 'Group', [('🐍 snake', 'vertebrate'), ('🐙 octopus', 'invertebrate'), ('🦋 butterfly', 'invertebrate'), ('🐢 tortoise', 'vertebrate')], o='O4', d='H'),
)
s.labs('Animal lab',
 sort_lab('Backbone or no backbone?', 'Sort each animal into the right group.', ['Vertebrate (backbone)', 'Invertebrate (no backbone)'],
  [('cat', '🐱', 0, 'Cats have a backbone.'), ('worm', '🐛', 1, 'Worms have no bones.'), ('fish', '🐟', 0, 'Fish have a backbone.'), ('snail', '🐌', 1, 'Snails have a shell, not a backbone.'), ('bird', '🐦', 0, 'Birds have a backbone.'), ('spider', '🕷️', 1, 'Spiders have no backbone.')],
  [PM('Which group had the snail?', ('🐛', 'Invertebrate'), [('🐱', 'Vertebrate', 'A snail has no backbone.')], 'O4')]),
 home('Minibeast count', 'Look for small animals outside, with an adult.', ['a magnifying glass', 'an adult'], ['Do not touch animals that sting.', 'Wash your hands afterwards.'],
  ['Look under leaves and stones.', 'Look at each animal carefully.', 'Put stones back gently.'],
  ['Animal', 'Did I find it?'], [('ant', ['yes', 'no']), ('snail', ['yes', 'no']), ('worm', ['yes', 'no']), ('ladybird', ['yes', 'no'])],
  [PM('Ants, snails and worms are all…', ('🐛', 'invertebrates'), [('🐶', 'vertebrates', 'They have no backbone.')], 'O4')]))

# ============================================================  1.5
s = U.section('1.5', 'Medicines and germs', ['O5']); s.words(V['1.5']); core(s, 'O5')
s.stop(PM('What is the best way to get rid of germs on your hands?', ('🧼', 'Wash with soap and water'), [('👕', 'Wipe them on your clothes', 'That spreads germs.'), ('💨', 'Blow on them', 'That does not remove germs.')], 'O5'),
       PM('When you sneeze, what should you use?', ('🤧', 'A tissue or your elbow'), [('✋', 'Your hand', 'Then germs go on your hand.'), ('🙅', 'Nothing', 'Germs fly out.')], 'O5'))
s.stop(PM('Who should give you medicine?', ('👨‍👩‍👧', 'A trusted adult'), [('🧒', 'A friend', 'Only a trusted adult.'), ('🙋', 'Yourself', 'Never take medicine on your own.')], 'O5'),
       PM('You find some tablets on the table. What should you do?', ('🗣️', 'Tell an adult'), [('😋', 'Eat them', 'Never! They may be medicine.'), ('🎒', 'Put them in your bag', 'Tell an adult.')], 'O5'))
s.prac(
 PM('Germs are…', ('🦠', 'tiny living things'), [('🐘', 'big animals', 'Germs are too small to see.'), ('🍬', 'sweets', 'Germs can make us ill.')], 'O5'),
 YN('Can you see germs with just your eyes?', False, 'O5', pic='🦠', why='No. Germs are far too small to see.'),
 TK('When should you wash your hands?', ['Yes', 'No'], [('before eating', ['✓', '✗']), ('after the toilet', ['✓', '✗']), ('after playing outside', ['✓', '✗'])], o='O5'),
 PM('How long should you wash your hands?', ('🎂', 'As long as singing Happy Birthday twice'), [('⚡', 'One second', 'Too short to remove germs.'), ('🕐', 'One hour', 'Much too long!')], 'O5'),
 PM('Which illness is caught from germs?', ('🤧', 'A cold'), [('🦴', 'A broken bone', 'That comes from a fall.'), ('☀️', 'Sunburn', 'That comes from the Sun.')], 'O5'),
 YN('Are medicines the same as sweets?', False, 'O5', pic='💊', why='No! Medicines can be dangerous if you take them wrongly.'),
 PM('What does a vaccine do?', ('💉', 'Helps stop you catching an illness'), [('🍬', 'Gives you a treat', 'It protects you from illness.'), ('🦷', 'Cleans your teeth', 'That is a toothbrush.')], 'O5'),
 OD('Put the steps for washing hands in order.', ['wet your hands', 'rub with soap', 'rinse with water', 'dry your hands'], o='O5'),
 GD('Does it stop germs spreading?', 'Stops germs?', [('🧼 washing hands', 'yes'), ('🤧 sneezing into a tissue', 'yes'), ('🥤 sharing a cup', 'no'), ('🗑️ binning tissues', 'yes')], o='O5'),
 PM('Your friend has a cold. What is kind and safe?', ('👋', 'Wave instead of hugging'), [('🥤', 'Share their drink', 'That spreads germs.'), ('🤧', 'Sneeze at them', 'That spreads germs.')], 'O5'),
 MT('Match each word to what it means.', [('germs', 'can make us ill'), ('soap', 'washes germs away'), ('medicine', 'helps an ill person get better')], o='O5'),
 YN('Should you always tell an adult if you feel ill?', True, 'O5', pic='🤒', why='Yes. An adult can help you get better.'),
)
s.adv(
 PM('* Advanced. Why does soap work better than water alone?', ('🧼', 'Soap lifts the germs off your skin'), [('💧', 'Soap is colder', 'Temperature is not the reason.'), ('🎨', 'Soap is a nice colour', 'Colour does not matter.')], 'O5', d='H'),
 PM('* Advanced. Why do doctors wear masks and gloves?', ('😷', 'To stop germs spreading'), [('🎭', 'To look scary', 'They are for safety.'), ('🧊', 'To stay cold', 'They stop germs.')], 'O5', d='H'),
 OD('* Advanced. Order how a cold spreads.', ['Sam has germs', 'Sam sneezes', 'germs fly into the air', 'his friend breathes them in'], o='O5', d='H'),
)
s.labs('Germ lab',
 test_lab('Glitter germs', 'Pretend glitter is germs. Wash your hands in different ways and count the glitter left.', 'How I washed', 'Glitter left', 'pieces', 20, 2,
  'Tap the number the bar reaches.', [('no washing', '🙌', 20), ('water only', '💧', 12), ('soap and water', '🧼', 2)],
  [PM('Which way left the least glitter?', ('🧼', 'Soap and water'), [('💧', 'Water only', 'Some glitter was still there.'), ('🙌', 'No washing', 'All the glitter was still there.')], 'O5')]),
 home('Glitter hands', 'See how germs spread, using glitter.', ['a little glitter', 'soap and water', 'a towel'], ['Keep glitter away from your eyes.'],
  ['Put a little glitter on your hand.', 'Shake hands with a friend.', 'Look at their hand.', 'Wash with soap and water.'],
  ['Question', 'My answer'], [('did glitter get on my friend?', ['yes', 'no']), ('did soap remove the glitter?', ['yes', 'no'])],
  [PM('What does the glitter show?', ('🦠', 'Germs can spread from hand to hand'), [('✨', 'Hands are shiny', 'It shows how germs spread.')], 'O5')]))

U.mindmap(('Bones and skeleton', 'skull, ribs, spine; 206 bones', 'O1', '1.1'), ('Jobs of the skeleton', 'support, protect, move', 'O2', '1.2'),
          ('Muscles', 'pull bones; work in pairs; joints', 'O3', '1.3'), ('Animal skeletons', 'vertebrates and invertebrates', 'O4', '1.4'), ('Staying healthy', 'germs, washing, medicines', 'O5', '1.5'))
