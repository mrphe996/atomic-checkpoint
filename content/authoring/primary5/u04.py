# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 5 · Unit 4 The digestive system. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit5 import *

OBJ = {
 'O1': {'sec': '4.1', 'code': 'Biology', 'codeNote': '', 't': 'Name the parts of the digestive system and describe what each part does.'},
 'O2': {'sec': '4.1', 'code': 'Biology', 'codeNote': '', 't': 'Describe the jobs of incisors, canines and molars, and how to look after teeth.'},
 'O3': {'sec': '4.2', 'code': 'Biology', 'codeNote': '', 't': 'Describe a balanced diet and what carbohydrates, proteins, vitamins, minerals and fibre do.'},
 'O4': {'sec': '4.2', 'code': 'Science in context', 'codeNote': '', 't': 'Use a food diary to judge whether a diet is balanced and suggest healthy swaps.'},
}
U = Unit(4, 'The digestive system', 'Biology: humans', 'The amazing journey of food through your body, your teeth, and how to eat a balanced diet.', OBJ)

# =====================================================================================  4.1
s = U.section('4.1', 'Parts of the digestive system', ['O1', 'O2']); s.words(V['4.1']); core(s, 'O1', 'O1')
s.stop(MC('Where do nutrients pass into the blood?', 'In the small intestine', [('In the mouth', 'Digestion starts there, but nutrients pass into the blood later.'), ('In the oesophagus', 'It is just a tube to the stomach.'), ('In the large intestine', 'It takes back water.')], o='O1'),
       MC('What does the stomach do?', 'Churns the food with acid', [('Takes water back from waste', 'That is the large intestine.'), ('Chops food with teeth', 'Teeth are in the mouth.')], o='O1'))
s.stop(MC('Which teeth grind and chew food?', 'Molars', [('Incisors', 'Incisors cut and bite.'), ('Canines', 'Canines tear.')], o='O2'),
       MC('Which teeth are sharp and at the front, for cutting?', 'Incisors', [('Molars', 'Molars are at the back.'), ('Canines', 'Canines are pointy, for tearing.')], o='O2'))
s.prac(
 OD('Put the journey of food in order.', ['mouth', 'oesophagus', 'stomach', 'small intestine', 'large intestine'], o='O1'),
 MT('Match each part to its job.', [('mouth', 'teeth chop food; saliva makes it soft'), ('oesophagus', 'a tube that carries food to the stomach'), ('stomach', 'churns food with acid'), ('small intestine', 'nutrients pass into the blood'), ('large intestine', 'takes water back from waste')], o='O1'),
 MC('What is digestion?', 'Breaking food down so the body can use it', [('Breathing in oxygen', 'That is breathing.'), ('Pumping blood', 'That is the heart\'s job.')], o='O1'),
 MC('What does saliva do?', 'Makes food soft and slippery so it is easy to swallow', [('Makes food hot', 'It softens food.'), ('Turns food into blood', 'It softens food.')], o='O1'),
 MC('About how long is the whole digestive tube?', 'About 9 metres – as long as a bus', [('About 9 centimetres', 'Much longer!'), ('About 90 metres', 'Not that long.')], o='O1'),
 MC('What are nutrients?', 'The useful parts of food that the body needs', [('The waste from food', 'Waste leaves the body.'), ('The teeth', 'Teeth chew food.')], o='O1'),
 MC('Why does your tummy sometimes gurgle?', 'Gas and liquid are being squeezed through the intestines', [('You swallowed a frog', 'Ha! It is gas and liquid moving.'), ('Your heart is loud', 'It is your intestines.')], o='O1'),
 CZ('Complete the sentences.', 'Food goes down the {0} to the {1}. Nutrients pass into the blood in the small {2}.', [['oesophagus', 'esophagus'], ['stomach'], ['intestine']], o='O1'),
 GD('Which type of tooth does each job?', 'Tooth', [('cutting a bite of apple', 'incisors'), ('tearing meat', 'canines'), ('grinding nuts', 'molars')], o='O2'),
 MC('How often should you brush your teeth?', 'Twice a day', [('Once a week', 'Brush twice a day.'), ('Only when they hurt', 'Brush every day.')], o='O2'),
 MS('Select the ways to keep teeth healthy.', ['brush twice a day', 'eat fewer sugary snacks', 'visit the dentist'], ['drink lots of fizzy drinks', 'never brush'], o='O2'),
 MC('Why are a lion\'s canines so long and sharp?', 'To grip and tear meat', [('To grind grass', 'Molars grind.'), ('To look friendly', 'They are for eating meat.')], o='O2'),
 MC('Why does a cow have lots of big, flat molars?', 'To grind tough grass', [('To tear meat', 'Cows eat plants.'), ('To bite people', 'Cows eat grass.')], o='O2', d='H'),
 MC('How big is an empty stomach?', 'About the size of your fist', [('As big as a football', 'It stretches after a meal.'), ('As small as a pea', 'It is about fist-sized.')], o='O1'),
)
s.adv(
 EX('Explain what happens to a piece of bread from your mouth to your stomach.', [('teeth chop it and saliva softens it', ['teeth', 'saliva', 'chew']), ('it is swallowed down the oesophagus', ['oesophagus', 'swallow', 'esophagus']), ('the stomach churns it with acid', ['stomach', 'acid', 'churn'])], 'Teeth chop the bread and saliva makes it soft. You swallow it and it slides down the oesophagus to the stomach, which churns it with acid.', o='O1', d='H'),
 TB('Lengths of parts of the digestive system in an adult. Complete the total.', ['Part', 'Length (m)'], [['oesophagus', '0.25'], ['small intestine', '6'], ['large intestine', '1.5'], ['total of these three', B(7.75, 0.01)]], o='O1', skill='Data'),
 MC('Why is the small intestine so long?', 'It gives lots of space for nutrients to pass into the blood', [('So food moves very fast', 'Length gives more time and space.'), ('Because it stores waste', 'The large intestine handles waste.')], o='O1', d='VH'),
 MC('In the stocking model of the gut, what does the liquid that seeps out represent?', 'Nutrients passing into the blood', [('Saliva', 'Saliva is in the mouth.'), ('Waste', 'Waste is what is left inside.')], o='O1', d='H'),
)
s.labs('Gut length lab',
 test_lab('How long is each part?', 'Measure the parts of an adult digestive system with the tape. Read the scale for each part.', 'The part', 'Length', 'm', 7, 0.5, '📏',
  [('Oesophagus', '⬇️', 0.25), ('Large intestine', '🌀', 1.5), ('Small intestine', '〰️', 6)],
  [MC('Which part is the longest?', 'The small intestine', [('The oesophagus', 'It is only 0.25 m.'), ('The large intestine', 'It is 1.5 m.')], o='O1'),
   MC('What happens in the longest part?', 'Nutrients pass into the blood', [('Food is chewed', 'That is in the mouth.'), ('Water is taken back', 'That is the large intestine.')], o='O1')]),
 home('Teeth detective', 'Use a mirror to count your different teeth.', ['a mirror', 'clean hands'],
  ['Do not poke your gums.', 'Wash your hands first.'],
  ['Open wide and look in the mirror.', 'Count your front cutting teeth (incisors).', 'Count your pointy teeth (canines).', 'Count your big back teeth (molars) – ask for help if needed.'],
  ['Teeth', 'How many I have'], [['Incisors', {'min': 0, 'max': 12}], ['Canines', {'min': 0, 'max': 6}], ['Molars (and premolars)', {'min': 0, 'max': 24}]], 'Children often have 8 incisors and 4 canines.',
  [MC('Which teeth do you use to bite into an apple?', 'Incisors', [('Molars', 'Molars grind.'), ('Canines', 'Canines tear.')], o='O2')]))

# =====================================================================================  4.2
s = U.section('4.2', 'Balanced diets', ['O3', 'O4']); s.words(V['4.2']); core(s, 'O3', 'O3')
s.stop(MC('Which food group gives us lots of energy?', 'Carbohydrates', [('Vitamins', 'Vitamins keep us healthy.'), ('Fibre', 'Fibre helps digestion.'), ('Dairy', 'Dairy helps bones.')], o='O3'),
       MC('About how much of your plate should be fruit and vegetables?', 'About a third', [('None', 'We need lots of fruit and vegetables.'), ('All of it', 'We need other food groups too.')], o='O3'))
s.stop(MC('Why do we need protein?', 'To grow and repair our bodies', [('To keep food moving', 'That is fibre.'), ('To give a little sweetness', 'Protein is for growth.')], o='O3'),
       MC('Which food is rich in protein?', 'Fish', [('Rice', 'Rice is a carbohydrate.'), ('Apple', 'Apples give vitamins and fibre.')], o='O3'))
s.prac(
 GD('Which food group is each food mostly in?', 'Food group', [('bread', 'carbohydrates'), ('chicken', 'proteins'), ('broccoli', 'fruit and vegetables'), ('cheese', 'dairy'), ('rice', 'carbohydrates'), ('beans', 'proteins')], o='O3'),
 MT('Match each nutrient to its job.', [('carbohydrates', 'give energy'), ('proteins', 'help growth and repair'), ('vitamins and minerals', 'keep us healthy'), ('fibre', 'keeps food moving through the gut')], o='O3'),
 MC('What is a balanced diet?', 'Eating the right amounts of different kinds of food', [('Eating only fruit', 'We need all food groups.'), ('Eating as much as possible', 'It is about the right amounts.')], o='O3'),
 MC('Which should we eat only a little of?', 'Fats and sugars', [('Fruit and vegetables', 'Eat lots of these.'), ('Water', 'Drink plenty of water.')], o='O3'),
 MC('Why is dairy food good for us?', 'It helps build strong bones and teeth', [('It gives most of our energy', 'Carbohydrates do that.'), ('It is full of fibre', 'Dairy has little fibre.')], o='O3'),
 MC('About how much of your body is water?', 'About 60%', [('About 6%', 'Much more!'), ('100%', 'Not all of it.')], o='O3'),
 CZ('Complete the sentences.', 'Carbohydrates give us {0}. Proteins help us {1}. Fibre keeps food {2} through the gut.', [['energy'], ['grow', 'grow and repair'], ['moving']], o='O3'),
 MC('Sam ate chips and doughnuts and felt tired. What would be a healthy swap?', 'Swap the doughnut for an apple and add a salad', [('Add more doughnuts', 'More sugar will not help.'), ('Skip lunch', 'He needs a balanced lunch.')], o='O4'),
 MS('Select the healthy swaps.', ['fizzy drink → water', 'sweets → fruit', 'white bread → brown bread'], ['salad → chips', 'water → fizzy drink'], o='O4'),
 MC('Which food contains the most fibre?', 'Brown bread', [('Butter', 'Butter has no fibre.'), ('Sweets', 'Sweets have no fibre.')], o='O3'),
 TB('A food diary for one day. How many portions of fruit and vegetables?', ['Meal', 'Fruit and veg portions'], [['breakfast', '1'], ['lunch', '2'], ['snack', '1'], ['dinner', '2'], ['total', B(6)]], o='O4', skill='Data'),
 MC('Why do athletes eat lots of carbohydrates before a race?', 'For energy', [('For strong bones', 'That is dairy.'), ('To repair muscles only', 'Carbohydrates give energy.')], o='O3', d='H'),
 MC('Why did the banana go to the doctor?', 'It wasn\'t peeling well! (a joke)', [('It was too yellow', 'It is a joke about peeling.'), ('It needed vitamins', 'It is a joke.')], o='O3'),
 MC('Which meal is the most balanced?', 'Rice, fish, vegetables and a glass of milk', [('Chips, cake and cola', 'Too much fat and sugar.'), ('Only bread', 'Missing many food groups.')], o='O4'),
)
s.adv(
 EX('Explain why a diet of only sweets and crisps is unhealthy.', [('too much fat / sugar / salt', ['fat', 'sugar', 'salt']), ('missing protein / vitamins / fibre', ['protein', 'vitamin', 'fibre', 'fiber']), ('the body cannot grow / stay healthy', ['grow', 'healthy', 'ill', 'energy'])], 'It has too much fat, sugar and salt, and is missing proteins, vitamins, minerals and fibre, so the body cannot grow, repair itself or stay healthy.', o='O3', d='H'),
 GR('Plot Mia\'s fruit and vegetable portions each day.', {'label': 'Day (1 = Monday)', 'min': 0, 'max': 6, 'step': 1}, {'label': 'Portions', 'min': 0, 'max': 8, 'step': 2}, [[1, 3], [2, 5], [3, 2], [4, 6], [5, 5]], o='O4', d='H', table_rows=[[1, 3], [2, 5], [3, 2], [4, 6], [5, 5]]),
 MC('Using those results, on which day did Mia eat the fewest portions?', 'Day 3 (Wednesday)', [('Day 4', 'She ate 6 then.'), ('Day 2', 'She ate 5 then.')], o='O4', d='H'),
 MC('Why do growing children need plenty of protein?', 'Their bodies are building new muscle, skin and bone', [('They need to stay small', 'Protein helps growth.'), ('Protein gives most energy', 'Carbohydrates give most energy.')], o='O3', d='VH'),
)
s.labs('Healthy plate lab',
 sort_lab('Sort the food', 'Sort each food into its main food group.', ['Carbohydrates (energy)', 'Proteins (growth)', 'Fruit and vegetables (vitamins)'],
  [('rice', '🍚', 0, 'Rice is a carbohydrate.'), ('egg', '🥚', 1, 'Eggs are rich in protein.'), ('carrot', '🥕', 2, 'Carrots are vegetables.'), ('pasta', '🍝', 0, 'Pasta is a carbohydrate.'),
   ('fish', '🐟', 1, 'Fish is rich in protein.'), ('orange', '🍊', 2, 'Oranges give vitamins.'), ('bread', '🍞', 0, 'Bread is a carbohydrate.'), ('beans', '🫘', 1, 'Beans are a protein.')],
  [MC('Which group gives us most of our energy?', 'Carbohydrates', [('Proteins', 'Proteins help growth.'), ('Fruit and vegetables', 'They give vitamins.')], o='O3'),
   MC('Which food would you add to a lunch of bread and fish to make it balanced?', 'A vegetable, like carrots', [('More bread', 'It needs vegetables.'), ('Sweets', 'Too much sugar.')], o='O4')]),
 home('My food diary', 'Record a day of eating and check if it is balanced.', ['the table below', 'a pencil'],
  ['Be honest – no one else needs to see it!', 'Do not change your meals without asking an adult.'],
  ['Write down everything you eat and drink for one day.', 'Count your portions of fruit and vegetables.', 'Count your sugary snacks and drinks.', 'Count your glasses of water.'],
  ['Food', 'Number in one day'], [['Fruit and vegetable portions', {'min': 0, 'max': 20}], ['Sugary snacks or drinks', {'min': 0, 'max': 20}], ['Glasses of water', {'min': 0, 'max': 20}]], 'Try for at least 5 portions of fruit and vegetables.',
  [MC('What is one good healthy swap?', 'A sugary drink for a glass of water', [('An apple for a doughnut', 'That swap is the wrong way round.'), ('Vegetables for chips', 'That is the wrong way round.')], o='O4')]))

U.mindmap(('Digestive system', 'Mouth → oesophagus → stomach → intestines.', 'O1', '4.1'), ('Teeth', 'Incisors cut, canines tear, molars grind.', 'O2', '4.1'),
          ('Balanced diet', 'Carbohydrates, proteins, vitamins, minerals, fibre.', 'O3', '4.2'), ('Healthy swaps', 'Food diaries help us choose better.', 'O4', '4.2'))
