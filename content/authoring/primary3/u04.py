# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 3 · Unit 4 Staying alive. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit3 import *

OBJ = {
 'O1': {'sec': '4.1', 'code': 'Biology', 'codeNote': '', 't': 'Name the heart, lungs, brain and stomach and say what each organ does.'},
 'O2': {'sec': '4.2', 'code': 'Biology', 'codeNote': '', 't': 'Sort animals into groups, and describe simple life cycles (chicken, frog, butterfly).'},
 'O3': {'sec': '4.3', 'code': 'Biology', 'codeNote': '', 't': 'Read and build simple food chains that start with a plant.'},
 'O4': {'sec': '4.4', 'code': 'Biology', 'codeNote': '', 't': 'Know that fossils are remains of living things from long ago, and that extinct means none are left.'},
}
U = YUnit(4, 'Staying alive', 'Biology: humans and animals', 'Our organs, animal groups and life cycles, food chains and fossils.', OBJ)

# ============================================================  4.1
s = U.section('4.1', 'Our organs', ['O1']); s.words(V['4.1']); core(s, 'O1')
s.stop(PM('Which organ pumps blood around your body?', ('❤️', 'The heart'), [('🧠', 'The brain', 'The brain thinks.'), ('🫁', 'The lungs', 'The lungs breathe.')], 'O1'),
       PM('What does your heart do?', ('🩸', 'Pumps blood'), [('😮‍💨', 'Breathes air', 'That is the lungs.'), ('💭', 'Thinks', 'That is the brain.')], 'O1'))
s.stop(PM('Which organ do you think with?', ('🧠', 'The brain'), [('❤️', 'The heart', 'The heart pumps blood.'), ('🥣', 'The stomach', 'The stomach holds food.')], 'O1'),
       PM('Which organ helps you remember your friend\'s name?', ('🧠', 'The brain'), [('🫁', 'The lungs', 'Lungs breathe.'), ('🥣', 'The stomach', 'The stomach holds food.')], 'O1'))
s.prac(
 GD('What does each organ do?', 'Job', [('❤️ heart', 'pumps blood'), ('🫁 lungs', 'breathe air'), ('🧠 brain', 'thinks'), ('🥣 stomach', 'holds food')], o='O1'),
 PM('You run in the playground. What happens to your heartbeat?', ('💓', 'It gets faster'), [('🐢', 'It gets slower', 'Exercise makes it faster.'), ('⏸️', 'It stops', 'It gets faster.')], 'O1'),
 YN('Do your lungs work while you sleep?', True, 'O1', pic='😴', why='Yes. You keep breathing all night.'),
 PM('Where are your lungs?', ('🫁', 'In your chest'), [('🦵', 'In your legs', 'They are in your chest.'), ('👂', 'In your ears', 'They are in your chest.')], 'O1'),
 PM('Your heart is about the size of your…', ('✊', 'fist'), [('⚽', 'football', 'Much smaller!'), ('🐜', 'an ant', 'Much bigger!')], 'O1'),
 MT('Match each word to what it means.', [('organ', 'a body part with a job'), ('lungs', 'what we breathe with'), ('blood', 'red liquid in your body')], o='O1'),
 TK('Tick what is true.', ['True', 'False'], [('the heart pumps blood', ['✓', '✗']), ('the brain digests food', ['✗', '✓']), ('lungs fill with air', ['✓', '✗'])], o='O1'),
 YN('When you breathe in, does your chest get bigger?', True, 'O1', pic='🎈', why='Yes. Your lungs fill with air.'),
 PM('After lunch, where does your food go first after you swallow?', ('🥣', 'To your stomach'), [('🧠', 'To your brain', 'Food goes to the stomach.'), ('🫁', 'To your lungs', 'Food goes to the stomach.')], 'O1'),
 OD('Put in order: a heartbeat test.', ['sit still and feel your heartbeat', 'jump for one minute', 'feel your heartbeat again'], o='O1'),
 PM('Why does your heart beat faster when you run?', ('💪', 'Your muscles need more blood'), [('🎵', 'It likes music', 'Muscles need more blood.'), ('😴', 'It is sleepy', 'Muscles need more blood.')], 'O1', d='H'),
 YN('Is the brain an organ?', True, 'O1', pic='🧠', why='Yes. It has the job of thinking.'),
)
s.adv(
 PM('* Advanced. Why do we wear a helmet when cycling?', ('🧠', 'To protect our brain'), [('❤️', 'To protect our heart', 'A helmet covers your head.'), ('🫁', 'To help us breathe', 'It protects the brain.')], 'O1', d='H'),
 PM('* Advanced. Which two organs work together to get air into your blood?', ('🫁', 'Lungs and heart'), [('🧠', 'Brain and stomach', 'Lungs take in air; the heart pumps blood.'), ('🥣', 'Stomach and ears', 'Lungs and heart.')], 'O1', d='VH'),
 OD('* Advanced. Order the heartbeat from slowest to fastest.', ['sleeping', 'walking', 'running'], o='O1', d='H'),
)
s.labs('Heartbeat lab',
 test_lab('Heartbeat test', 'Count your heartbeats in 15 seconds after doing different things.', 'What I did', 'Heartbeats in 15 seconds', 'beats', 50, 5,
  'Tap the number the bar reaches.', [('sitting still', '🪑', 20), ('walking', '🚶', 25), ('jumping for 1 minute', '🤸', 40)],
  [PM('When was the heart beating fastest?', ('🤸', 'After jumping'), [('🪑', 'Sitting still', 'It was slowest then.')], 'O1')]),
 home('Heartbeat test', 'Feel your heart work harder.', ['a clock or timer', 'space to jump', 'an adult'], ['Stop if you feel dizzy.'],
  ['Sit still and feel your heartbeat.', 'Jump on the spot for one minute.', 'Feel your heartbeat again.'],
  ['When', 'My heartbeat was'], [('sitting still', ['slow', 'fast']), ('after jumping', ['slow', 'fast'])],
  [PM('What did jumping do to your heartbeat?', ('💓', 'Made it faster'), [('🐢', 'Made it slower', 'Exercise makes it faster.')], 'O1')]))

# ============================================================  4.2
s = U.section('4.2', 'Animal groups and life cycles', ['O2']); s.words(V['4.2']); core(s, 'O2')
s.stop(PM('Which animal is a bird?', ('🦜', 'A parrot'), [('🐶', 'A dog', 'A dog is a mammal.'), ('🐟', 'A fish', 'A fish has fins.')], 'O2'),
       PM('Which animal has feathers?', ('🐦', 'A bird'), [('🐍', 'A snake', 'Snakes have scales.'), ('🐱', 'A cat', 'Cats have fur.')], 'O2'))
s.stop(PM('What does a tadpole grow into?', ('🐸', 'A frog'), [('🐟', 'A fish', 'It grows legs and becomes a frog.'), ('🦋', 'A butterfly', 'Caterpillars become butterflies.')], 'O2'),
       PM('What hatches out of a hen\'s egg?', ('🐣', 'A chick'), [('🐸', 'A tadpole', 'Tadpoles come from frogspawn.'), ('🐛', 'A caterpillar', 'A chick hatches.')], 'O2'))
s.prac(
 GD('Which group?', 'Group', [('🐶 dog', 'mammal'), ('🐦 robin', 'bird'), ('🐟 goldfish', 'fish'), ('🐍 snake', 'reptile'), ('🐄 cow', 'mammal')], o='O2'),
 OD('Put the frog life cycle in order.', ['frogspawn eggs', 'tadpole', 'froglet with legs', 'frog'], o='O2'),
 OD('Put the butterfly life cycle in order.', ['egg', 'caterpillar', 'chrysalis', 'butterfly'], o='O2'),
 YN('Is a whale a fish?', False, 'O2', pic='🐳', why='No. A whale is a mammal. It breathes air and feeds its babies milk.'),
 PM('Which animal feeds its babies milk?', ('🐄', 'A cow'), [('🐔', 'A hen', 'Birds do not make milk.'), ('🐟', 'A fish', 'Fish do not make milk.')], 'O2'),
 PM('What covers a mammal\'s body?', ('🦁', 'Fur or hair'), [('🪶', 'Feathers', 'Birds have feathers.'), ('🐟', 'Wet scales', 'Fish have scales.')], 'O2'),
 MT('Match each baby to its grown-up.', [('tadpole', 'frog'), ('chick', 'hen'), ('caterpillar', 'butterfly')], o='O2'),
 TK('Tick the mammals.', ['Mammal', 'Not a mammal'], [('a horse', ['✓', '✗']), ('a parrot', ['✗', '✓']), ('a person', ['✓', '✗'])], o='O2'),
 PM('You find jelly with black dots in a pond in spring. What is it?', ('🫧', 'Frogspawn'), [('🍮', 'Pudding', 'It is frog eggs!'), ('🪨', 'Stones', 'It is frog eggs!')], 'O2'),
 YN('Do people have a life cycle too?', True, 'O2', pic='👶', why='Yes. Baby, child, adult.'),
 PM('Which part of a frog\'s life is spent swimming with a tail?', ('🐟', 'Tadpole'), [('🐸', 'Grown-up frog', 'Tadpoles have tails.'), ('🫧', 'Egg', 'Tadpoles swim.')], 'O2'),
 PM('A caterpillar eats and eats. Why?', ('📈', 'To grow big before it changes'), [('😴', 'To fall asleep forever', 'It is growing.'), ('🎨', 'To change colour', 'It is growing.')], 'O2', d='H'),
)
s.adv(
 PM('* Advanced. A penguin cannot fly but has feathers and lays eggs. It is a…', ('🐧', 'bird'), [('🐟', 'fish', 'Feathers mean bird.'), ('🐶', 'mammal', 'Feathers mean bird.')], 'O2', d='VH'),
 PM('* Advanced. Why is a life cycle drawn as a circle?', ('🔄', 'Grown-ups have young, and it starts again'), [('⚽', 'Animals are round', 'It repeats.'), ('🎨', 'Circles look nice', 'It repeats.')], 'O2', d='H'),
 OD('* Advanced. Order a person\'s life.', ['baby', 'child', 'teenager', 'adult'], o='O2', d='H'),
)
s.labs('Animal lab',
 sort_lab('Animal groups', 'Sort each animal.', ['Mammal', 'Bird'],
  [('dog', '🐶', 0, 'It has fur.'), ('owl', '🦉', 1, 'It has feathers.'), ('cat', '🐱', 0, 'It has fur.'), ('duck', '🦆', 1, 'It has feathers.'), ('cow', '🐄', 0, 'It feeds its calf milk.'), ('hen', '🐔', 1, 'It lays eggs and has feathers.')],
  [PM('Which animal is a mammal?', ('🐱', 'The cat'), [('🦆', 'The duck', 'A duck is a bird.')], 'O2')]),
 home('Life cycle wheel', 'Make a frog life cycle wheel.', ['a paper plate', 'crayons'], ['Keep crayons away from your mouth.'],
  ['Draw four parts round the plate.', 'Egg, tadpole, froglet, frog.', 'Add arrows round the circle.'],
  ['Question', 'My answer'], [('what comes after the egg?', ['tadpole', 'frog']), ('what comes after the froglet?', ['tadpole', 'frog'])],
  [PM('What does a tadpole become?', ('🐸', 'A frog'), [('🐟', 'A fish', 'It becomes a frog.')], 'O2')]))

# ============================================================  4.3
s = U.section('4.3', 'Food chains', ['O3']); s.words(V['4.3']); core(s, 'O3')
s.stop(PM('In this food chain, what does the rabbit eat? (grass → rabbit → fox)', ('🌾', 'Grass'), [('🦊', 'The fox', 'The fox eats the rabbit.'), ('🥩', 'Meat', 'Rabbits eat grass.')], 'O3'),
       PM('In the food chain grass → rabbit → fox, who eats the rabbit?', ('🦊', 'The fox'), [('🌾', 'The grass', 'Grass does not eat.'), ('🐰', 'Another rabbit', 'The fox does.')], 'O3'))
s.stop(PM('What is at the start of every food chain?', ('🌱', 'A plant'), [('🦁', 'A lion', 'Food chains start with a plant.'), ('🐰', 'A rabbit', 'Food chains start with a plant.')], 'O3'),
       PM('Where do plants get the energy to make food?', ('☀️', 'From sunlight'), [('🍔', 'From burgers', 'Plants use sunlight.'), ('🦊', 'From foxes', 'Plants use sunlight.')], 'O3'))
s.prac(
 OD('Put the food chain in order.', ['leaf', 'caterpillar', 'bird'], o='O3'),
 OD('Put this food chain in order.', ['seeds', 'mouse', 'owl'], o='O3'),
 PM('What does the arrow in a food chain mean?', ('➡️', 'Is eaten by'), [('🏃', 'Runs away from', 'It means is eaten by.'), ('🤝', 'Is friends with', 'It means is eaten by.')], 'O3'),
 YN('Do animals need food for energy?', True, 'O3', pic='⚡', why='Yes. Food gives energy to move and grow.'),
 PM('Which animal eats only plants?', ('🐰', 'A rabbit'), [('🦊', 'A fox', 'Foxes eat meat.'), ('🦈', 'A shark', 'Sharks eat fish.')], 'O3'),
 MT('Match each animal to its food.', [('rabbit', 'grass'), ('caterpillar', 'leaves'), ('fox', 'rabbit')], o='O3'),
 TK('Tick what is true.', ['True', 'False'], [('food chains start with a plant', ['✓', '✗']), ('foxes eat grass', ['✗', '✓']), ('plants use sunlight', ['✓', '✗'])], o='O3'),
 PM('Which food chain is the right way round?', ('🌾', 'grass → zebra → lion'), [('🦁', 'lion → zebra → grass', 'Start with the plant.'), ('🦓', 'zebra → grass → lion', 'Start with the plant.')], 'O3'),
 GD('Plant or animal?', 'Type', [('🌾 grass', 'plant'), ('🐛 caterpillar', 'animal'), ('🍃 leaf', 'plant'), ('🦉 owl', 'animal')], o='O3'),
 PM('Your breakfast cereal is made from wheat. In your food chain, you are…', ('🧒', 'eating a plant'), [('🦊', 'eating a fox', 'Wheat is a plant.'), ('☀️', 'eating the Sun', 'Wheat is a plant.')], 'O3'),
 PM('In the sea: tiny plants → small fish → shark. What does the small fish eat?', ('🌿', 'Tiny plants'), [('🦈', 'Sharks', 'Sharks eat the small fish.'), ('🪨', 'Rocks', 'It eats tiny plants.')], 'O3', d='H'),
 YN('Can a plant make its own food?', True, 'O3', pic='🌱', why='Yes. It uses sunlight.'),
)
s.adv(
 PM('* Advanced. All the rabbits leave a field. What happens to the foxes?', ('🦊', 'They have less food'), [('🎉', 'They have more food', 'They eat rabbits.'), ('🌾', 'They eat the grass', 'Foxes do not eat grass.')], 'O3', d='VH'),
 PM('* Advanced. What would happen to a food chain with no Sun?', ('🥀', 'Plants could not make food, so animals would go hungry'), [('🎉', 'Nothing', 'Everything starts with the Sun.'), ('🌳', 'Plants would grow faster', 'Plants need light.')], 'O3', d='VH'),
 OD('* Advanced. Order this sea food chain.', ['seaweed', 'snail', 'crab', 'seagull'], o='O3', d='H'),
)
s.labs('Food chain lab',
 sort_lab('Plant or animal?', 'Every food chain starts with a plant. Sort these.', ['Plant (makes its own food)', 'Animal (eats food)'],
  [('grass', '🌾', 0, 'Grass makes food from sunlight.'), ('rabbit', '🐰', 1, 'A rabbit eats grass.'), ('leaf', '🍃', 0, 'Leaves make food.'), ('fox', '🦊', 1, 'A fox eats rabbits.'), ('seaweed', '🌿', 0, 'Seaweed is a plant.'), ('owl', '🦉', 1, 'An owl eats mice.')],
  [PM('What goes at the start of the food chain?', ('🌾', 'Grass'), [('🦊', 'Fox', 'Start with a plant.')], 'O3')]),
 home('Food chain paper chain', 'Make a food chain from paper loops.', ['paper strips', 'crayons', 'glue or tape'], ['Ask an adult to help with scissors.'],
  ['Draw a plant, a rabbit and a fox.', 'Loop them together in order.', 'Read your chain.'],
  ['Question', 'My answer'], [('what is first?', ['plant', 'fox']), ('what is last?', ['plant', 'fox'])],
  [PM('Which comes in the middle?', ('🐰', 'The rabbit'), [('🌾', 'The grass', 'Grass is first.')], 'O3')]))

# ============================================================  4.4
s = U.section('4.4', 'Fossils', ['O4']); s.words(V['4.4']); core(s, 'O4')
s.stop(PM('What is a fossil?', ('🦴', 'Remains of a living thing kept in rock'), [('🧸', 'A toy dinosaur', 'A fossil is real and very old.'), ('🪨', 'Any stone', 'It shows a living thing.')], 'O4'),
       PM('Where are fossils found?', ('🪨', 'In rocks'), [('☁️', 'In clouds', 'They are in rocks.'), ('🌊', 'Floating in the sea', 'They are in rocks.')], 'O4'))
s.stop(PM('What does extinct mean?', ('🚫', 'None are left alive'), [('🦕', 'Very big', 'It means none are left.'), ('🐣', 'Just born', 'It means none are left.')], 'O4'),
       PM('Which animal is extinct?', ('🦖', 'A dinosaur'), [('🐶', 'A dog', 'Dogs are alive today.'), ('🐦', 'A sparrow', 'Sparrows are alive today.')], 'O4'))
s.prac(
 YN('Did people and dinosaurs live at the same time?', False, 'O4', pic='🦕', why='No. Dinosaurs lived millions of years before people.'),
 OD('Order how a fossil forms.', ['an animal dies', 'mud covers its bones', 'the mud turns to rock', 'people dig it up'], o='O4'),
 PM('How do we know what dinosaurs looked like?', ('🦴', 'From their fossils'), [('📸', 'From photos', 'There were no cameras.'), ('📺', 'From TV', 'From fossils.')], 'O4'),
 GD('Can it be a fossil?', 'Fossil?', [('🐚 a shell in rock', 'yes'), ('👣 a footprint in rock', 'yes'), ('🧸 a plastic dinosaur', 'no'), ('🍃 a leaf shape in rock', 'yes')], o='O4'),
 MT('Match each word to what it means.', [('fossil', 'remains in rock'), ('extinct', 'none left alive'), ('dinosaur', 'big animal from long ago')], o='O4'),
 PM('Scientists dig up a fossil. What tool do they use to clean it gently?', ('🖌️', 'A small brush'), [('🔨', 'A big hammer', 'That could break it.'), ('🧽', 'A wet sponge', 'They brush it gently.')], 'O4'),
 TK('Tick what is true.', ['True', 'False'], [('fossils take a very long time to form', ['✓', '✗']), ('dinosaurs are alive today', ['✗', '✓']), ('a footprint can be a fossil', ['✓', '✗'])], o='O4'),
 YN('Can a fossil form in one day?', False, 'O4', pic='⏳', why='No. It takes millions of years.'),
 PM('You press a shell into play dough and take it out. What did you make?', ('🐚', 'A pretend fossil print'), [('🎂', 'A cake', 'It is like a fossil.'), ('🪨', 'A real rock', 'It is a pretend fossil.')], 'O4'),
 PM('Which is the oldest?', ('🦕', 'A dinosaur fossil'), [('📱', 'A phone', 'Fossils are millions of years old.'), ('🏠', 'Your house', 'Fossils are much older.')], 'O4'),
 PM('Why are fossils found in rock, not in soil on top?', ('🪨', 'The mud turned into rock over a long time'), [('🌧️', 'Rain puts them there', 'Mud turns to rock.'), ('🧑‍🔬', 'Scientists hide them', 'Mud turns to rock.')], 'O4', d='H'),
 YN('Can a fossil be a plant?', True, 'O4', pic='🍃', why='Yes. Leaves can make fossils too.'),
)
s.adv(
 PM('* Advanced. A fossil fish is found on top of a mountain. What does it tell us?', ('🌊', 'Long ago, that place was under water'), [('🐟', 'Fish can climb', 'The land was once under water.'), ('✈️', 'A plane dropped it', 'The land was once under water.')], 'O4', d='VH'),
 PM('* Advanced. Why are there no fossils of jellyfish usually?', ('🪼', 'They have no hard parts'), [('🧊', 'They are too cold', 'Soft bodies rarely make fossils.'), ('🌈', 'They are too colourful', 'Soft bodies rarely make fossils.')], 'O4', d='H'),
 OD('* Advanced. Order from oldest to newest.', ['dinosaurs', 'the first people', 'you'], o='O4', d='H'),
)
s.labs('Fossil lab',
 sort_lab('Real fossil or not?', 'Sort each thing.', ['Fossil', 'Not a fossil'],
  [('shell shape in rock', '🐚', 0, 'It is kept in rock.'), ('plastic dinosaur', '🦖', 1, 'It is a toy.'), ('footprint in rock', '👣', 0, 'It is kept in rock.'), ('a fresh leaf', '🍃', 1, 'It is not in rock.'), ('bone in rock', '🦴', 0, 'It is kept in rock.'), ('a pebble', '🪨', 1, 'It has no living thing in it.')],
  [PM('Which is a fossil?', ('👣', 'A footprint in rock'), [('🦖', 'A plastic dinosaur', 'It is a toy.')], 'O4')]),
 home('Make a fossil', 'Make a pretend fossil.', ['play dough or clay', 'a shell or toy', 'a flat table'], ['Wash your hands afterwards.'],
  ['Flatten the play dough.', 'Press the shell in.', 'Lift it out carefully.'],
  ['Question', 'My answer'], [('did the shape stay?', ['yes', 'no']), ('is it a real fossil?', ['yes', 'no'])],
  [PM('How is a real fossil different?', ('⏳', 'It took millions of years and is in rock'), [('🎨', 'It is more colourful', 'It is in rock and very old.')], 'O4')]))

U.mindmap(('Organs', 'heart, lungs, brain, stomach', 'O1', '4.1'), ('Animal groups', 'mammals, birds, fish; life cycles', 'O2', '4.2'),
          ('Food chains', 'start with a plant', 'O3', '4.3'), ('Fossils', 'remains in rock; extinct', 'O4', '4.4'))
