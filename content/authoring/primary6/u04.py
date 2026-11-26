# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 6 · Unit 4 Food chains and food webs. Written by the Camday teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kit6 import *
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'build', 'p6'))

OBJ = {
 'O1': {'sec': '4.1', 'code': 'Biology', 'codeNote': '', 't': 'Describe producers and consumers, draw food chains with arrows that show the flow of energy, and use the words predator, prey and herbivore.'},
 'O2': {'sec': '4.1', 'code': 'Biology', 'codeNote': '', 't': 'Read food webs and predict what happens when one population changes.'},
 'O3': {'sec': '4.1', 'code': 'Working scientifically', 'codeNote': '', 't': 'Explain why only a little energy is passed along each step of a food chain.'},
 'O4': {'sec': '4.2', 'code': 'Biology', 'codeNote': '', 't': 'Describe how toxic substances, such as pesticides and metals, accumulate along food chains.'},
 'O5': {'sec': '4.2', 'code': 'Science in context', 'codeNote': '', 't': 'Describe how microplastics, pollution and habitat loss harm food webs, and how people can protect them.'},
}
U = Unit(4, 'Food chains and food webs', 'Biology: ecosystems', 'How energy passes from plants to animals, how food chains join into webs, and how people can harm or protect them.', OBJ)
from vocab_u4 import V, SAY as SAYW
core = core_for(V, SAYW)

# =====================================================================================  4.1
s = U.section('4.1', 'Food chains, food webs and energy', ['O1', 'O2', 'O3']); s.words(V['4.1']); core(s, 'O1', 'O1')
s.stop(MC('In a food chain, which way do the arrows point?', 'From the food to the animal that eats it – the way energy moves', [('From the animal to its food', 'The arrow means "is eaten by".'), ('From the biggest animal to the smallest', 'Follow the energy, from food to eater.'), ('Any way you like', 'The direction matters.')], o='O1', reason='grass → rabbit → fox: the arrows show energy moving from the food to the eater.'),
       MC('In the food chain grass → rabbit → fox, what does the first arrow mean?', 'The grass is eaten by the rabbit', [('The rabbit is eaten by the grass', 'Grass does not eat rabbits!'), ('The grass grows into a rabbit', 'The arrow means "is eaten by".')], o='O1'))
s.stop(MC('Look at the food web: grass is eaten by the grasshopper and the rabbit; the mouse is eaten by the fox and the owl. Which animal eats more than one kind of food?', 'The fox, which eats rabbits and mice', [('The grasshopper, which eats only grass', 'It has one food here.'), ('The grass', 'Grass is a producer – it makes its own food.')], o='O2'),
       MC('In a food web, why might an owl survive if all the mice disappeared?', 'It could eat other animals in the web', [('Owls do not need food', 'All animals need food.'), ('Owls eat grass', 'Owls are predators.')], o='O2'))
s.prac(
 MC('What is a producer?', 'A green plant that makes its own food using sunlight', [('An animal that eats plants', 'That is a herbivore (a consumer).'), ('An animal that hunts', 'That is a predator.')], o='O1'),
 MC('Why are animals called consumers?', 'They eat (consume) other living things for food', [('They make food from sunlight', 'Only plants do that.'), ('They live in water', 'Consumers live everywhere.')], o='O1'),
 GD('Is each living thing a producer or a consumer?', 'Type', [('grass', 'producer'), ('rabbit', 'consumer'), ('oak tree', 'producer'), ('fox', 'consumer'), ('seaweed', 'producer')], o='O1'),
 OD('Put this food chain in order.', ['leaf', 'caterpillar', 'bird', 'cat'], o='O1', reason='A food chain starts with a producer.'),
 MC('Where does the energy in every food chain come from at the start?', 'The Sun', [('The soil', 'Plants get minerals from soil, but energy from sunlight.'), ('The top predator', 'Energy flows up the chain from the Sun.')], o='O1'),
 MT('Match each word to its meaning.', [('herbivore', 'eats only plants'), ('predator', 'hunts other animals'), ('prey', 'is hunted and eaten'), ('producer', 'makes its own food')], o='O1'),
 MC('In grass → rabbit → fox, which animal is the prey?', 'The rabbit', [('The fox', 'The fox is the predator.'), ('The grass', 'Grass is a producer, not prey.')], o='O1'),
 MC('In seaweed → limpet → crab → seagull, what is the crab?', 'Both predator (of the limpet) and prey (of the seagull)', [('Only a producer', 'Crabs do not make food.'), ('Only prey', 'It also eats limpets.')], o='O1', d='H'),
 CZ('Complete the sentences.', 'A food chain always starts with a {0}. Food chains join together to make a food {1}.', [['producer', 'plant', 'green plant'], ['web']], o='O1'),
 MC('Why are food webs more useful than food chains?', 'They show that most animals eat, and are eaten by, more than one living thing', [('They are shorter', 'Food webs are bigger.'), ('They have no arrows', 'Food webs use arrows too.')], o='O2'),
 MC('In a food web the rabbits catch a disease and many die. What may happen to the foxes?', 'Their numbers may fall, because they have less food', [('They will all grow bigger', 'They have less food.'), ('Nothing at all', 'A change in one population affects others.')], o='O2'),
 MC('If many rabbits die, what may happen to the grass?', 'It may grow more, because fewer animals eat it', [('It will die', 'Fewer animals are eating it.'), ('It will turn into rabbits', 'That cannot happen.')], o='O2'),
 TK('A farmer removes all the foxes from a field. Tick what is likely to happen.', ['Likely', 'Not likely'], [('the number of rabbits goes up', ['✓', '✗']), ('the rabbits eat more grass', ['✓', '✗']), ('the grass grows taller', ['✗', '✓'])], o='O2', d='H'),
 MC('What is a population?', 'All the animals or plants of one kind living in one place', [('One single animal', 'A population is many of one kind.'), ('All the people in the world', 'In science, it means one kind in one place.')], o='O2'),
 MC('Why are there fewer foxes than rabbits?', 'Only a little energy is passed on at each step, so there is less energy for foxes', [('Foxes are lazy', 'It is about energy.'), ('Rabbits eat foxes', 'Foxes eat rabbits.')], o='O3'),
 MS('Select what an animal uses most of its energy for.', ['moving', 'growing', 'keeping warm'], ['passing it to the next animal'], o='O3', reason='Only a little energy is passed on.'),
 OD('Put these in order from the most living things to the fewest, in a field.', ['grass plants', 'rabbits', 'foxes'], o='O3'),
 MC('Why are food chains usually short (4 or 5 steps)?', 'There is not enough energy left to support more animals at the top', [('Animals cannot count higher', 'It is about energy.'), ('Plants stop growing', 'It is because energy is lost at each step.')], o='O3', d='H'),
)
s.adv(
 EX('Explain why a food chain must start with a green plant.', [('only plants can make their own food', ['make', 'own food', 'producer']), ('they use energy from sunlight', ['sun', 'light']), ('animals need to eat to get energy', ['animal', 'eat', 'consumer'])], 'Only green plants can make their own food using energy from sunlight. Animals cannot, so they must eat plants (or animals that ate plants) to get energy.', o='O1', d='H'),
 TB('A field has 1000 grass plants, 50 rabbits and 2 foxes. Complete the table.', ['Living thing', 'Number', 'Producer or consumer?'], [['grass', '1000', B('producer')], ['rabbits', '50', B('consumer')], ['foxes', '2', B('consumer')]], o='O1', d='M', reason='Grass is a producer; rabbits and foxes are consumers.'),
 MC('A snake eats frogs and mice. Frogs and mice both eat insects. Insects eat leaves. What happens to the frogs if the snakes eat many more mice?', 'There may be more frogs, because snakes eat fewer frogs', [('There will be fewer frogs', 'The snakes are busy eating mice.'), ('Frogs will eat the snakes', 'Frogs do not eat snakes.')], o='O2', d='VH'),
 MC('About how much energy does a rabbit pass on to the fox that eats it?', 'Only a small part – most was used for moving, growing and keeping warm', [('All of it', 'Most of it was used by the rabbit.'), ('More than it got from the grass', 'Energy cannot increase along a chain.')], o='O3', d='H'),
)
s.labs('Food chain lab',
 {'kind': 'sort', 'title': 'Who is who in the food web?', 'intro': 'This food web is from a meadow. Sort each living thing: producer, herbivore (eats only plants) or predator (hunts animals).',
  'groups': ['Producer', 'Herbivore', 'Predator'],
  'items': [{'t': 'grass', 'emoji': '🌿', 'g': 0, 'why': 'Grass makes its own food from sunlight.'}, {'t': 'rabbit', 'emoji': '🐇', 'g': 1, 'why': 'Rabbits eat only plants.'},
            {'t': 'fox', 'emoji': '🦊', 'g': 2, 'why': 'Foxes hunt rabbits and mice.'}, {'t': 'grasshopper', 'emoji': '🦗', 'g': 1, 'why': 'Grasshoppers eat grass.'},
            {'t': 'owl', 'emoji': '🦉', 'g': 2, 'why': 'Owls hunt mice.'}, {'t': 'clover', 'emoji': '☘️', 'g': 0, 'why': 'Clover is a green plant.'},
            {'t': 'mouse (eats seeds)', 'emoji': '🐭', 'g': 1, 'why': 'This mouse eats only seeds – plants.'}],
  'qs': [MC('What do all the producers have in common?', 'They are green plants that use sunlight to make food', [('They hunt at night', 'Producers do not hunt.'), ('They eat grass', 'Producers make their own food.')], o='O1'),
         OD('Make a food chain from the cards.', ['grass', 'rabbit', 'fox'], o='O1')]},
 {'title': 'Garden food chain hunt', 'intro': 'Find living things outside and build a food chain.',
  'need': ['a garden, park or school field', 'a magnifying glass if you have one', 'an adult'],
  'safety': ['Look, do not touch – some insects sting.', 'Wash your hands afterwards.'],
  'steps': ['Look closely in one small area (about 1 metre square) for 10 minutes.', 'Count the plants, the plant-eating animals (e.g. caterpillars, snails) and the animals that eat animals (e.g. spiders, birds).', 'Write your counts in the table.', 'Use your living things to draw one food chain with arrows.'],
  'record': {'head': ['Group', 'Number I counted'], 'rows': [['Plants (producers)', {'min': 0, 'max': 10000}], ['Plant-eaters (herbivores)', {'min': 0, 'max': 1000}], ['Animal-eaters (predators)', {'min': 0, 'max': 1000}]], 'hint': 'Write 0 if you did not find any.'},
  'qs': [MC('In most hunts, which group has the most living things?', 'Plants', [('Predators', 'There is less energy for predators.'), ('Herbivores', 'Usually there are more plants than herbivores.')], o='O3')]})

# =====================================================================================  4.2
s = U.section('4.2', 'Harm to food chains and food webs', ['O4', 'O5']); s.words(V['4.2']); core(s, 'O4', 'O5')
s.stop(MC('Which animal gets the most poison: the small fish or the big bird?', 'The big bird', [('The small fish', 'The bird eats many fish, so the poison builds up.'), ('Both get the same', 'The poison accumulates along the chain.'), ('Neither', 'Pesticide passes along the chain.')], o='O4', reason='The bird eats lots of small fish, so it takes in all their poison.'),
       MC('Why does the poison build up in the big bird?', 'It eats lots of small fish, and the poison stays in its body', [('It drinks the river water', 'The main source is the fish it eats.'), ('Birds make poison', 'The poison came from the pesticide.')], o='O4'))
s.stop(MC('What are microplastics?', 'Very small pieces of plastic', [('Tiny sea animals', 'Some sea animals eat microplastics by mistake.'), ('A kind of seaweed', 'Microplastics are plastic.'), ('Large plastic bottles', 'Microplastics are tiny.')], o='O5'),
       MC('How can microplastics end up in fish that people eat?', 'Tiny sea animals eat them, then fish eat those animals', [('Fishermen put them there', 'They pass along the food chain.'), ('Fish make plastic', 'Fish cannot make plastic.')], o='O5'))
s.prac(
 MC('Why do some farmers use pesticides?', 'To kill insects that eat their crops', [('To help insects grow', 'Pesticides kill insects.'), ('To water the crops', 'Pesticides are not water.')], o='O4'),
 MC('What does "toxic" mean?', 'Poisonous', [('Healthy', 'The opposite.'), ('Very small', 'That is "tiny".')], o='O4'),
 MC('How do pesticides get into rivers?', 'Rain washes them off the fields', [('Fish carry them', 'Rain carries them.'), ('They are made in rivers', 'They come from farms.')], o='O4'),
 OD('Put the steps in order to show how a pesticide reaches a big bird.', ['pesticide is sprayed on crops', 'rain washes it into a lake', 'tiny water plants take it in', 'small fish eat the plants', 'a big bird eats lots of small fish'], o='O4'),
 MC('What does "accumulate" mean?', 'Build up over time', [('Disappear', 'It is the opposite.'), ('Turn into plastic', 'It means build up.')], o='O4'),
 TB('Scientists measured a pesticide (in tiny units) along a lake food chain. How many times more is in the bird than in the small fish?', ['Living thing', 'Pesticide (units)'], [['water plant', '1'], ['small fish', '10'], ['big bird', '100'], ['times more in the bird than the fish', B(10)]], o='O4', reason='100 ÷ 10 = 10 times more.', skill='Data'),
 MC('Which animal in a food chain is usually harmed most by a toxic substance?', 'The top predator', [('The producer', 'Producers take in only a little.'), ('The herbivore', 'It gets more than the plant, but less than the predator.')], o='O4'),
 MC('Which metal can leak from factories into rivers and harm food chains?', 'Mercury', [('Gold', 'Gold is not the usual problem.'), ('Aluminium foil', 'The problem metal named is mercury.')], o='O4'),
 MC('Where do microplastics come from?', 'Bigger pieces of plastic rubbish breaking up', [('Rocks', 'They come from plastic.'), ('Volcanoes', 'They come from plastic waste.')], o='O5'),
 MC('Why is cutting down forests harmful to food webs?', 'It destroys the homes (habitats) and food of many living things', [('Trees eat animals', 'Trees are producers.'), ('It makes more food', 'It removes food.')], o='O5'),
 MC('What does an oil spill do to sea food webs?', 'It coats and poisons sea animals and plants', [('It feeds the fish', 'Oil harms them.'), ('Nothing – oil floats away', 'Oil causes great harm.')], o='O5'),
 MS('Select ways YOU can help protect food webs.', ['use less plastic', 'reuse and recycle', 'never drop litter', 'plant wild flowers'], ['throw rubbish in rivers', 'cut down trees for fun'], o='O5'),
 MC('Ladybirds eat aphids. Why might a farmer use ladybirds instead of pesticide?', 'It is natural pest control that does not poison other animals', [('Ladybirds eat the crops', 'They eat aphids.'), ('Ladybirds are toxic', 'They are not toxic.')], o='O5'),
 MT('Match each harm to a way to reduce it.', [('plastic in the sea', 'use less plastic and recycle'), ('pesticides in rivers', 'use natural pest control'), ('cutting down forests', 'plant trees')], o='O5'),
 GD('Does each action help or harm food webs?', 'Effect', [('planting trees', 'helps'), ('dropping litter near a river', 'harms'), ('recycling bottles', 'helps'), ('spilling oil', 'harms')], o='O5'),
 MC('What is a habitat?', 'The place where a living thing lives', [('A type of food', 'It is a home.'), ('A poison', 'It is a home.')], o='O5'),
 MC('Why is it important to protect top predators like eagles?', 'If they disappear, the whole food web can change', [('They are the smallest animals', 'They are at the top.'), ('They are producers', 'They are consumers.')], o='O5', d='H'),
 MC('Which of these is pollution?', 'Factory waste flowing into a river', [('Rain falling on a field', 'Rain is natural.'), ('A tree growing', 'That is not pollution.')], o='O5'),
)
s.adv(
 EX('Explain why a pesticide sprayed on a field can harm an eagle that never visits the field.', [('the pesticide is washed into water / taken in by plants', ['wash', 'river', 'lake', 'plant']), ('it passes along the food chain as animals eat each other', ['food chain', 'eat', 'passes']), ('it accumulates / builds up in the top predator', ['accumulat', 'build', 'top'])], 'The pesticide is washed into water and taken in by plants. Animals eat the plants and are eaten in turn, so the pesticide passes along the food chain and accumulates in the eagle at the top.', o='O4', d='H'),
 GR('Plot the pesticide units along the food chain.', {'label': 'Step in the food chain (1 = plant)', 'min': 0, 'max': 4, 'step': 1}, {'label': 'Pesticide (units)', 'min': 0, 'max': 100, 'step': 20}, [[1, 1], [2, 10], [3, 40], [4, 100]], o='O4', d='H', table_rows=[[1, 1], [2, 10], [3, 40], [4, 100]]),
 MC('A class counted plastic items on a beach: 120 bottles, 80 bags, 400 small pieces. What fraction of the 600 items were small pieces?', 'Two thirds', [('One half', '400 out of 600 is more than half.'), ('One quarter', 'That is too small.')], o='O5', d='VH', reason='400 ÷ 600 = 2/3.'),
 MC('Why are microplastics hard to clean up?', 'They are tiny and spread through the whole ocean', [('They sink and turn to rock at once', 'They stay as plastic for a very long time.'), ('They are very large', 'They are tiny.')], o='O5', d='H'),
)
s.labs('Poison build-up lab',
 {'kind': 'test', 'title': 'How much pesticide is in each living thing?', 'intro': 'Scientists tested living things from a lake near a farm. Read the scale to see how much pesticide was found in each one.',
  'change': 'The living thing', 'measure': 'Pesticide found', 'unit': 'units', 'max': 100, 'step': 10, 'instr': '🧪',
  'conds': [{'k': 'plant', 't': 'Water plants', 'emoji': '🌱', 'val': 5}, {'k': 'fish', 't': 'Small fish', 'emoji': '🐟', 'val': 20}, {'k': 'pike', 't': 'Big fish', 'emoji': '🐠', 'val': 50}, {'k': 'bird', 't': 'Fish-eating bird', 'emoji': '🦅', 'val': 90}],
  'qs': [MC('What happens to the amount of pesticide along the food chain?', 'It goes up at each step', [('It goes down at each step', 'Look at your bar chart.'), ('It stays the same', 'The values change a lot.')], o='O4'),
         MC('What is the word for this build-up?', 'Accumulate', [('Evaporate', 'That is a liquid turning into a gas.'), ('Dissolve', 'That is mixing into a liquid.')], o='O4')]},
 {'title': 'My plastic diary', 'intro': 'Count the plastic you throw away, then try to cut it down.',
  'need': ['the table below', 'a family who will help'],
  'safety': ['Do not handle sharp or dirty rubbish – just count.', 'Wash your hands after sorting.'],
  'steps': ['On day 1, count every piece of plastic your family throws away (bottles, bags, wrappers).', 'Think of three ways to use less plastic, e.g. a refillable bottle or cloth bags.', 'On day 2, try your ideas and count again.', 'Compare the two days.'],
  'record': {'head': ['Day', 'Plastic items thrown away'], 'rows': [['Day 1 (normal)', {'min': 0, 'max': 500}], ['Day 2 (trying to cut down)', {'min': 0, 'max': 500}]], 'hint': 'Write a whole number.'},
  'qs': [MC('Why does using less plastic help sea food webs?', 'Less plastic can break into microplastics that animals eat', [('Plastic is food for fish', 'It harms them.'), ('It makes the sea warmer', 'It is about plastic in food chains.')], o='O5')]})

U.mindmap(('Food chains', 'Producer → consumers; arrows show energy.', 'O1', '4.1'), ('Food webs', 'Chains join; a change in one population affects others.', 'O2', '4.1'),
          ('Energy', 'Only a little is passed on at each step.', 'O3', '4.1'), ('Toxic build-up', 'Pesticides and metals accumulate along food chains.', 'O4', '4.2'),
          ('Protecting food webs', 'Less plastic, natural pest control, more habitats.', 'O5', '4.2'))
