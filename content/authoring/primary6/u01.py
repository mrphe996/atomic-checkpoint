# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 6 · Unit 1 The human body. Written by the Camday teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kit6 import *
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'build', 'p6'))

OBJ = {
 'O1': {'sec': '1.1', 'code': 'Biology', 'codeNote': '', 't': 'Describe the parts of the circulatory system (heart, blood vessels and blood) and what each part does.'},
 'O2': {'sec': '1.1', 'code': 'Working scientifically', 'codeNote': '', 't': 'Measure pulse rate, record the results in a table and say how exercise changes pulse rate.'},
 'O3': {'sec': '1.2', 'code': 'Biology', 'codeNote': '', 't': 'Describe the parts of the respiratory system and how we breathe in and breathe out.'},
 'O4': {'sec': '1.2', 'code': 'Working scientifically', 'codeNote': '', 't': 'Explain why we breathe, use a model of the lungs and read a line graph of breathing rate.'},
 'O5': {'sec': '1.3', 'code': 'Biology', 'codeNote': '', 't': 'Describe the body changes of puberty and name the main parts of the reproductive system.'},
 'O6': {'sec': '1.4', 'code': 'Biology', 'codeNote': '', 't': 'Name living things that cause disease and describe how the body defends itself.'},
 'O7': {'sec': '1.4', 'code': 'Science in context', 'codeNote': '', 't': 'Describe how hygiene, clean water and avoiding insect bites stop diseases spreading.'},
}
U = Unit(1, 'The human body', 'Biology: structure and function', 'How your heart, blood, lungs and body systems keep you alive – and how we keep healthy.', OBJ)
from vocab_u1 import V, SAY as SAYW

core = core_for(V, SAYW)

# =====================================================================================  1.1
s = U.section('1.1', 'The circulatory system', ['O1', 'O2']); s.words(V['1.1']); core(s, 'O1', 'O1')
s.stop(MC('Which side of the heart pumps blood to the lungs?', 'The right side', [('The left side', 'The left side pumps oxygen-rich blood to the rest of the body.'), ('Both sides take turns', 'Each side has its own job.'), ('Neither – the lungs pull the blood', 'The heart is the pump.')], o='O1', reason='Right side → lungs (to pick up oxygen). Left side → the rest of the body.'),
       MC('Which side of the heart pumps oxygen-rich blood to the body?', 'The left side', [('The right side', 'The right side sends blood to the lungs.'), ('The top of the heart', 'Think about the two sides, left and right.')], o='O1'))
s.stop(OD('Put the journey of blood in order, starting at the heart.', ['The heart pumps blood to the lungs.', 'The blood picks up oxygen in the lungs.', 'The blood goes back to the heart.', 'The heart pumps the blood to the body.', 'The body uses the oxygen and the blood returns to the heart.'], o='O1', reason='Heart → lungs (oxygen in) → heart → body (oxygen used) → heart, and round again.'),
       MC('Where does the blood pick up oxygen?', 'In the lungs', [('In the heart', 'The heart pumps the blood but does not add oxygen.'), ('In the stomach', 'The stomach digests food.'), ('In the arms and legs', 'The body USES oxygen there.')], o='O1'))
s.stop(MC('Why does the heart beat faster when we run?', 'The muscles need more food and oxygen, so the heart pumps blood faster.', [('Running makes the heart smaller.', 'The heart does not change size.'), ('The blood gets thicker when we run.', 'That is not why.'), ('The heart needs a rest.', 'A faster heart is working harder, not resting.')], o='O2', reason='Exercising muscles need more food and oxygen. The blood brings them, so the heart beats faster.'),
       MC('After a race, Ana\'s pulse rate is 140 beats per minute. What will happen when she rests?', 'It will slowly go back down.', [('It will go up even more.', 'Resting lets the heart slow down.'), ('It will stop.', 'The heart never stops.'), ('It will stay at 140 all day.', 'It goes back to normal after rest.')], o='O2'))
s.prac(
 MC('What is the main job of the heart?', 'To pump blood around the body', [('To breathe in air', 'That is the job of the lungs.'), ('To digest food', 'The stomach and intestines do this.'), ('To think', 'The brain does the thinking.')], o='O1'),
 MS('Select the THREE main parts of the circulatory system.', ['heart', 'blood vessels', 'blood'], ['lungs', 'stomach', 'bones'], o='O1', reason='Heart, blood vessels and blood.'),
 MT('Match each blood vessel to its job.', [('artery', 'carries blood away from the heart'), ('vein', 'carries blood back to the heart'), ('capillary', 'joins arteries to veins; very thin walls')], o='O1'),
 MC('About how big is your heart?', 'About the size of your fist', [('About the size of your head', 'Much smaller than that.'), ('About the size of a pea', 'Much bigger than that.'), ('As long as your arm', 'It is in your chest, about fist-sized.')], o='O1'),
 MC('What protects the heart?', 'The ribs', [('The skin only', 'The skin is thin – bones protect the heart.'), ('The stomach', 'The stomach is below the heart.'), ('The windpipe', 'The windpipe carries air.')], o='O1'),
 CZ('Complete the sentences.', 'The heart is a {0}. Each time it squeezes, it pushes {1} along the blood vessels. We call each squeeze a {2}.', [['muscle'], ['blood'], ['heartbeat', 'beat', 'heart beat']], o='O1'),
 GD('Does each thing travel to the body parts, or away from them in the blood?', 'In the blood', [('oxygen', 'carried TO body parts'), ('food', 'carried TO body parts'), ('carbon dioxide', 'carried AWAY as waste')], o='O1'),
 MC('Which blood vessel has the thickest, stretchiest wall?', 'artery', [('vein', 'Veins have thinner walls.'), ('capillary', 'Capillaries have the thinnest walls of all.')], o='O1', reason='Blood in arteries is pushed hard by the heart, so artery walls are thick and stretchy.'),
 MC('Why do capillaries have very thin walls?', 'So oxygen and food can pass through into the body', [('So they can carry lots of blood fast', 'Capillaries are tiny and narrow.'), ('So they do not break', 'Thin walls break more easily – that is not the reason.'), ('So the blood stays inside', 'The thin walls let things pass OUT.')], o='O1'),
 MC('Which animal has a circulatory system with a heart, blood vessels and blood?', 'All of them: a fish, a frog and a bird', [('Only humans', 'Many animals with a backbone have one.'), ('Only birds', 'Fish and frogs have one too.')], o='O1'),
 MC('Where can you feel your pulse easily?', 'On the inside of your wrist', [('On your knee', 'The pulse is easiest at the wrist or neck.'), ('On the top of your head', 'Try the wrist or the side of your neck.'), ('On your elbow', 'Try the wrist or the side of your neck.')], o='O2'),
 MC('Why should you use two fingers, not your thumb, to find a pulse?', 'Your thumb has its own pulse, which can confuse you', [('Your thumb is too short', 'That is not the reason.'), ('Fingers are warmer', 'That is not the reason.')], o='O2'),
 TB('Tom counted his pulse for 15 seconds. Work out his pulse rate in beats per minute (× 4).', ['Beats in 15 s', 'Beats per minute'], [['20', B(80)], ['25', B(100)], ['30', B(120)]], o='O2', reason='1 minute = 4 × 15 seconds, so multiply by 4: 20 × 4 = 80, 25 × 4 = 100, 30 × 4 = 120.'),
 S('Mia measured her pulse three times: 84, 86 and 85 beats per minute. What is her average pulse rate? (Add them and divide by 3.)', ['85'], o='O2', d='H', reason='84 + 86 + 85 = 255; 255 ÷ 3 = 85 beats per minute.'),
 MC('In a fair test of how exercise affects pulse rate, what do you CHANGE?', 'The type or amount of exercise', [('The person being tested', 'Keep the same person so the test is fair.'), ('The way you count the pulse', 'Keep the counting method the same.'), ('The timer', 'Keep the same timer.')], o='O2'),
 MC('In the same fair test, what do you MEASURE?', 'The pulse rate', [('The time spent exercising', 'You choose that – it is what you change.'), ('The person\'s height', 'Height does not tell us about exercise.')], o='O2'),
 MC('Sam says: "My pulse rate is the same as everyone else\'s." Is he right?', 'No – pulse rates are different for different people.', [('Yes – everyone has exactly the same pulse rate.', 'Look at a class results table: they are different.'), ('Yes – but only for children.', 'Children\'s pulse rates differ too.')], o='O2'),
 OD('Put these in order of pulse rate, from lowest to highest.', ['sleeping', 'sitting', 'walking', 'running'], o='O2', reason='The more active you are, the faster your heart beats.'),
)
s.adv(
 EX('Explain why the heart pumps blood to the lungs before it pumps blood to the rest of the body.', [('the blood picks up oxygen in the lungs', ['oxygen']), ('the body needs oxygen-rich blood', ['body', 'need']), ('the left side then pumps it to the body', ['left', 'body', 'then', 'after'])],
    'The blood must pick up oxygen in the lungs first; then the heart pumps this oxygen-rich blood to the body, which needs the oxygen.', o='O1', d='H'),
 MC('A fish heart sends blood to the gills, then straight to the body. A human heart sends blood to the lungs, back to the heart, then to the body. What is the difference?', 'In humans the blood goes through the heart twice on each trip; in a fish only once.', [('The fish has no blood vessels.', 'A fish has blood vessels.'), ('Human blood never goes to the lungs.', 'It does – to pick up oxygen.'), ('There is no difference.', 'Count how many times the blood passes the heart.')], o='O1', d='VH'),
 GR('Pulse rate of a learner after exercise. Plot the results.', {'label': 'Minutes after stopping', 'min': 0, 'max': 8, 'step': 2}, {'label': 'Pulse (beats per minute)', 'min': 60, 'max': 160, 'step': 20}, [[0, 140], [2, 120], [4, 100], [6, 90], [8, 90]], o='O2', d='H', table_rows=[[0, 140], [2, 120], [4, 100], [6, 90], [8, 90]]),
 MC('Using the results 140, 120, 100, 90, 90 (every 2 minutes after exercise), about how long did the pulse take to get back to normal?', 'About 6 minutes', [('About 2 minutes', 'At 2 minutes it was still 120.'), ('About 10 minutes', 'It was already steady at 90 by 6 minutes.'), ('It never got back to normal', 'It levelled off at 90.')], o='O2', d='H'),
)
s.labs('Pulse rate lab',
 {'kind': 'pulse', 'title': 'How does exercise change pulse rate?', 'intro': 'Choose an activity. Watch the heart and tap “Beat!” every time it beats for 15 seconds. Then work out the pulse rate in beats per minute.',
  'acts': [{'k': 'rest', 't': 'Sitting still', 'bpm': 84}, {'k': 'walk', 't': 'Walking on the spot', 'bpm': 108}, {'k': 'jump', 't': 'Star jumps', 'bpm': 148}],
  'qs': [MC('Look at your results. What happened to the pulse rate as the exercise got harder?', 'It went up', [('It went down', 'Look again at the table: star jumps had the highest pulse rate.'), ('It stayed the same', 'The numbers changed.')], o='O2'),
         MC('Which variable did you CHANGE in this experiment?', 'The activity', [('The pulse rate', 'That is what you measured.'), ('The 15-second counting time', 'You kept that the same to be fair.')], o='O2'),
         MC('Why did we count for 15 seconds every time?', 'To keep the test fair', [('Because the heart stops after 15 seconds', 'It does not stop.'), ('To make the numbers bigger', 'We keep it the same so results can be compared.')], o='O2')]},
 {'title': 'Measure your own pulse rate', 'intro': 'Find out how your pulse rate changes when you exercise. Work with an adult or a friend.',
  'need': ['a clock or timer that shows seconds', 'a pencil (or type your results below)', 'a safe space to do star jumps'],
  'safety': ['Only exercise if you feel well. Stop if you feel dizzy.', 'Do star jumps on a flat floor, away from furniture.'],
  'steps': ['Sit still for 2 minutes. Find your pulse on your wrist with two fingers.', 'Count the beats for 1 minute (or for 15 seconds and multiply by 4). Write it down.', 'Do 1 minute of star jumps. Then count your pulse again straight away.', 'Rest for 3 minutes and count your pulse one more time.'],
  'record': {'head': ['When', 'Pulse rate (beats per minute)'], 'rows': [['Sitting still', {'min': 40, 'max': 140}], ['Just after star jumps', {'min': 60, 'max': 220}], ['After 3 minutes of rest', {'min': 40, 'max': 180}]], 'hint': 'Pulse rates for children are usually between 60 and 200.'},
  'qs': [MC('Compare your results. When was your pulse rate highest?', 'Just after star jumps', [('Sitting still', 'Exercise makes the heart beat faster.'), ('After resting', 'Resting lets it slow down again.')], o='O2'),
         EX('Explain your results. Use the words muscles and oxygen.', [('muscles need more oxygen (and food) during exercise', ['muscle', 'oxygen']), ('the heart beats faster to pump more blood', ['faster', 'pump', 'beat'])], 'During exercise the muscles need more oxygen and food, so the heart beats faster to pump more blood to them.', o='O2', d='H')]})

# =====================================================================================  1.2
s = U.section('1.2', 'The respiratory system', ['O3', 'O4']); s.words(V['1.2']); core(s, 'O3', 'O3')
s.stop(MC('What does the diaphragm do when we breathe in?', 'It tightens and moves down', [('It relaxes and moves up', 'That happens when we breathe OUT.'), ('It fills with air', 'The lungs fill with air; the diaphragm is a muscle.'), ('Nothing', 'It is the main breathing muscle.')], o='O3', reason='Breathing in: diaphragm down, ribs up and out, chest bigger, air in.'),
       MC('When we breathe OUT, the ribs move…', 'down and in', [('up and out', 'That is breathing in.'), ('they do not move', 'The ribs move every time we breathe.')], o='O3'))
s.stop(MC('In the bottle model, which part acts like the diaphragm?', 'The stretchy rubber sheet at the bottom', [('The balloon inside', 'The balloon is a lung.'), ('The straw', 'The straw is the windpipe.'), ('The bottle', 'The bottle is the chest.')], o='O4'),
       MC('In the bottle model, what does the balloon inside the bottle show?', 'A lung', [('The heart', 'The model shows breathing, not the heart.'), ('The windpipe', 'The straw is the windpipe.')], o='O4'))
s.stop(MC('Look at the graph. What was the breathing rate just after running (at 4 minutes)?', '42 breaths per minute', [('16 breaths per minute', 'That was at rest.'), ('30 breaths per minute', 'That was at 2 minutes.'), ('28 breaths per minute', 'That was 2 minutes after stopping.')], o='O4'),
       MC('From the graph, about how long did it take to get back to normal after stopping?', 'About 6 minutes', [('About 1 minute', 'It was still high after 2 minutes of rest.'), ('About 12 minutes', 'It was back to 16 by 10 minutes on the graph.')], o='O4'))
s.prac(
 MS('Select the parts of the respiratory system.', ['lungs', 'windpipe', 'diaphragm'], ['heart', 'kidneys', 'stomach'], o='O3'),
 MC('What protects the lungs?', 'The ribs', [('The diaphragm', 'The diaphragm is under the lungs and helps breathing.'), ('The windpipe', 'The windpipe carries air.')], o='O3'),
 OD('Put the path of air in order when we breathe in.', ['nose or mouth', 'windpipe', 'lungs'], o='O3'),
 MT('Match each part to what it does.', [('lungs', 'fill with air; oxygen moves into the blood'), ('windpipe', 'carries air down to the lungs'), ('diaphragm', 'a muscle that helps air move in and out'), ('ribs', 'protect the lungs and move when we breathe')], o='O3'),
 TK('Tick what happens when we BREATHE IN.', ['Yes', 'No'], [('the diaphragm moves down', ['✓', '✗']), ('the ribs move up and out', ['✓', '✗']), ('the chest gets smaller', ['✗', '✓']), ('air moves into the lungs', ['✓', '✗'])], o='O3'),
 TK('Tick what happens when we BREATHE OUT.', ['Yes', 'No'], [('the diaphragm moves up', ['✓', '✗']), ('the ribs move down and in', ['✓', '✗']), ('the chest gets bigger', ['✗', '✓']), ('air is pushed out of the lungs', ['✓', '✗'])], o='O3'),
 CZ('Complete the sentences.', 'We need {0} to stay alive. In the lungs it moves into the {1}. Our body makes {2} as waste, and we breathe it out.', [['oxygen'], ['blood'], ['carbon dioxide']], o='O4'),
 MC('Why do we breathe?', 'To get oxygen into our body and remove carbon dioxide', [('To cool down our heart', 'That is not why we breathe.'), ('To make our voice work', 'We use breath to talk, but we breathe to get oxygen.'), ('To fill our stomach with air', 'Air goes to the lungs, not the stomach.')], o='O4'),
 MC('Why does a balloon get bigger when you blow into it?', 'Air from your lungs is pushed into it', [('The balloon makes its own air', 'The air comes from you.'), ('Your heart pumps air', 'The heart pumps blood, not air.')], o='O3'),
 MC('What is breathing rate?', 'The number of breaths in one minute', [('How deep one breath is', 'That is not the rate.'), ('How long you can hold your breath', 'That is not the rate.')], o='O4'),
 MC('About how many times do we breathe each minute at rest?', 'About 16 times', [('About 2 times', 'Much more often than that.'), ('About 100 times', 'That is far too many at rest.')], o='O4'),
 MC('What happens to breathing rate during exercise?', 'It goes up', [('It goes down', 'The body needs more oxygen, so we breathe faster.'), ('It stays the same', 'It changes when we are active.')], o='O4'),
 GD('In the bottle model, what does each part represent?', 'Represents', [('balloon', 'a lung'), ('straw', 'the windpipe'), ('rubber sheet', 'the diaphragm'), ('bottle', 'the chest')], o='O4'),
 MC('Which body parts are NOT shown in the bottle model?', 'The ribs', [('The lungs', 'The balloon shows a lung.'), ('The windpipe', 'The straw shows the windpipe.')], o='O4', d='H', reason='The model has a hard bottle instead of ribs that move.'),
 TB('A learner\'s breathing rate was 16 at rest, 30 after 2 minutes of running and 42 after 4 minutes of running. After 2 minutes of rest it was 28. Complete the table.', ['Time (minutes)', 'Breaths per minute'], [['0 (rest)', '16'], ['2 (running)', '30'], ['4 (running)', B(42)], ['6 (resting)', '28']], o='O4', reason='Peak = 42 at 4 minutes.', d='M', hint='Use the line graph from the video: the highest point.'),
 MC('Which type of scientific enquiry is "measuring breathing rate every two minutes after exercise"?', 'Observing over time', [('Identifying and classifying', 'We are not sorting things into groups.'), ('Research', 'We are measuring, not reading books.')], o='O4', d='H'),
 MC('An athlete trains every day. Her breathing rate at rest is likely to be…', 'lower than an untrained person\'s', [('much higher than an untrained person\'s', 'Training makes the body work more efficiently.'), ('zero', 'Everyone breathes.')], o='O4', d='H'),
 MC('Which other body system also changes when you exercise?', 'The circulatory system – the heart beats faster', [('The skeleton – bones get longer', 'Bones do not grow during a run.'), ('None', 'Your heart rate changes too.')], o='O4'),
)
s.adv(
 EX('Explain how breathing in makes air go into the lungs. Use the words diaphragm, ribs and chest.', [('diaphragm tightens / moves down', ['diaphragm']), ('ribs move up and out', ['ribs', 'rib']), ('chest gets bigger so air moves in', ['bigger', 'chest'])],
    'The diaphragm tightens and moves down and the ribs move up and out, so the chest gets bigger and air rushes into the lungs.', o='O3', d='H'),
 GR('Plot this breathing rate data.', {'label': 'Time (minutes)', 'min': 0, 'max': 10, 'step': 2}, {'label': 'Breaths per minute', 'min': 0, 'max': 50, 'step': 10}, [[0, 16], [2, 30], [4, 40], [6, 24], [8, 18], [10, 16]], o='O4', d='H', table_rows=[[0, 16], [2, 30], [4, 40], [6, 24], [8, 18], [10, 16]]),
 MC('Fish do not have lungs. How do they get oxygen?', 'Their gills take oxygen from the water', [('They swim to the surface to breathe air', 'Most fish do not.'), ('They do not need oxygen', 'All animals need oxygen.')], o='O4', d='H'),
 MC('Two learners did the same running test. Ali\'s breathing rate went back to normal after 4 minutes, Ben\'s after 8 minutes. What is the best conclusion?', 'Ali\'s body may be fitter – it recovered faster', [('Ben ran faster', 'We cannot tell that from recovery time.'), ('Ali did not run at all', 'Both did the same test.'), ('Their lungs are the same size', 'The data does not tell us that.')], o='O4', d='VH'),
)
s.labs('Lung model lab',
 {'kind': 'lungs', 'title': 'Make the model breathe', 'intro': 'This is a bottle model of the chest. Pull the rubber sheet down, then let it go back up. Watch the balloon.',
  'qs': [MC('When you pulled the rubber sheet DOWN, the balloon…', 'got bigger – air went in', [('got smaller – air went out', 'That happened when you let go.'), ('did not change', 'Look again while you move the slider.')], o='O4'),
         MT('Match each part of the model to the body.', [('balloon', 'lung'), ('straw', 'windpipe'), ('rubber sheet', 'diaphragm'), ('bottle', 'chest')], o='O4'),
         MC('Pulling the sheet down is like which part of breathing?', 'Breathing in', [('Breathing out', 'Letting go is like breathing out.'), ('Sneezing', 'The model shows normal breathing.')], o='O4')]},
 {'title': 'How much does your chest grow?', 'intro': 'Measure your chest when you breathe in and when you breathe out.',
  'need': ['a soft tape measure (or a piece of string and a ruler)', 'a helper'],
  'safety': ['Keep the tape loose – never pull it tight.', 'Do not hold your breath for a long time.'],
  'steps': ['Put the tape measure around your chest, under your arms.', 'Breathe out fully. Ask your helper to read the tape in centimetres.', 'Now take a deep breath in and hold it for two seconds. Read the tape again.', 'Repeat both measurements once more.'],
  'record': {'head': ['', 'Chest size breathing OUT (cm)', 'Chest size breathing IN (cm)'], 'rows': [['Try 1', {'min': 40, 'max': 130}, {'min': 40, 'max': 140}], ['Try 2', {'min': 40, 'max': 130}, {'min': 40, 'max': 140}]], 'hint': 'Chest sizes are usually between 50 and 100 cm.'},
  'qs': [MC('Was your chest bigger when you breathed in or out?', 'When I breathed in', [('When I breathed out', 'Breathing out makes the chest smaller.'), ('Always the same', 'The ribs move, so the size changes.')], o='O3'),
         MC('Why does the chest get bigger when we breathe in?', 'The ribs move up and out and the diaphragm moves down', [('The heart grows', 'The heart does not change size.'), ('Food enters the chest', 'Food goes to the stomach.')], o='O3')]})

# =====================================================================================  1.3
s = U.section('1.3', 'Growing up and the reproductive system', ['O5']); s.words(V['1.3']); core(s, 'O5', 'O5')
s.stop(MC('What causes the changes in puberty?', 'Hormones – chemical messengers in the body', [('Eating more food', 'Food helps us grow, but hormones cause puberty.'), ('Exercise', 'Exercise does not start puberty.'), ('Going to school', 'Puberty happens to everyone, whatever they do.')], o='O5'),
       MC('Which of these is a change that can happen during puberty?', 'A growth spurt', [('Losing your teeth', 'That happens younger, at about 6–12.'), ('Shrinking', 'You get taller in puberty.')], o='O5'))
s.stop(MC('Where does fertilisation take place?', 'In the oviduct', [('In the ovary', 'The ovary makes the eggs.'), ('In the uterus', 'The baby grows in the uterus.'), ('In the testes', 'The testes make sperm.')], o='O5'),
       MC('Where does a baby grow?', 'In the uterus (womb)', [('In the oviduct', 'Fertilisation happens there.'), ('In the ovary', 'Eggs are made there.')], o='O5'))
s.prac(
 MC('What is reproduction?', 'Making new living things', [('Growing taller', 'That is growth.'), ('Eating food', 'That is feeding.'), ('Breathing', 'That is respiration.')], o='O5'),
 MC('Why do living things need to reproduce?', 'So that their kind of living thing does not die out', [('To grow bigger', 'Reproduction makes NEW living things.'), ('To get more food', 'That is not the reason.')], o='O5'),
 OD('Put the stages of the human life cycle in order.', ['baby', 'child', 'teenager', 'adult'], o='O5'),
 MC('What is puberty?', 'The time when a child\'s body changes into an adult\'s body', [('When a baby is born', 'Puberty happens later, from about 10–14.'), ('Old age', 'Puberty happens in childhood and the teenage years.')], o='O5'),
 MS('Select the changes that can happen during puberty.', ['growing taller quickly', 'more hair on the body', 'oily skin and spots', 'the voice gets deeper'], ['losing baby teeth', 'getting shorter'], o='O5'),
 GD('Which changes are more common in boys, in girls, or in both?', 'Mostly in', [('a growth spurt', 'both'), ('hips get wider', 'girls'), ('shoulders get broader', 'boys'), ('oily skin', 'both')], o='O5'),
 MC('Puberty in girls often starts at about…', '11 years old', [('5 years old', 'That is too young.'), ('20 years old', 'Puberty starts in childhood.')], o='O5'),
 MC('Mai started puberty at 10 and her friend at 13. Is that normal?', 'Yes – puberty starts at different ages for different people', [('No – everyone starts at exactly 12', 'Everyone is different.'), ('No – it must start before 10', 'It often starts between 10 and 14.')], o='O5'),
 MC('What are hormones?', 'Chemical messengers in the body', [('Small bones', 'Hormones are not bones.'), ('A type of food', 'They are made by the body.')], o='O5'),
 MT('Match each sex cell to its description.', [('sperm', 'male sex cell with a tail'), ('egg (ovum)', 'female sex cell, much bigger')], o='O5'),
 MT('Match each part to its job.', [('testes', 'make sperm'), ('sperm duct', 'carries sperm'), ('ovaries', 'make eggs'), ('oviduct', 'where fertilisation happens'), ('uterus', 'where the baby grows')], o='O5', d='H'),
 CZ('Complete the sentences.', 'A sperm cell joins with an {0} cell. This is called {1}. The baby then grows in the {2}.', [['egg', 'ovum'], ['fertilisation', 'fertilization'], ['uterus', 'womb']], o='O5'),
 MC('What is the main job of the reproductive system?', 'To make sex cells for reproduction', [('To pump blood', 'That is the circulatory system.'), ('To digest food', 'That is the digestive system.')], o='O5'),
 MC('Which is bigger?', 'An egg cell', [('A sperm cell', 'Sperm cells are tiny.'), ('They are the same size', 'The egg is much bigger.')], o='O5'),
 MC('Why does a sperm cell have a tail?', 'So it can swim to the egg', [('To look nice', 'It has a job.'), ('To stay still', 'It needs to move.')], o='O5'),
 MC('What is menstruation?', 'When an unfertilised egg and the lining of the uterus leave the body, causing some bleeding', [('When a baby is born', 'That is birth.'), ('When a boy\'s voice changes', 'That is another puberty change.')], o='O5'),
 MC('About how often does menstruation happen?', 'About once a month', [('Once a week', 'It is about once a month.'), ('Once a year', 'It is about once a month.')], o='O5'),
 MC('Who is a good person to talk to if you have questions about growing up?', 'A parent, carer or teacher you trust', [('Nobody – it is a secret', 'It is normal and healthy to ask.'), ('A stranger online', 'Talk to a trusted adult.')], o='O5'),
)
s.adv(
 GR('Plot Lena\'s height from age 8 to 14.', {'label': 'Age (years)', 'min': 8, 'max': 14, 'step': 1}, {'label': 'Height (cm)', 'min': 120, 'max': 170, 'step': 10}, [[8, 128], [9, 133], [10, 138], [11, 146], [12, 154], [13, 160], [14, 163]], o='O5', d='H', table_rows=[[8, 128], [9, 133], [10, 138], [11, 146], [12, 154], [13, 160], [14, 163]]),
 MC('Using Lena\'s heights (128, 133, 138, 146, 154, 160, 163 cm from age 8 to 14), between which ages did she grow fastest?', 'Between 11 and 12', [('Between 8 and 9', 'She grew 5 cm then.'), ('Between 13 and 14', 'She grew only 3 cm then.'), ('Between 9 and 10', 'She grew 5 cm then.')], o='O5', d='VH', reason='The biggest change is 146 → 154 = 8 cm (also 138 → 146 = 8 cm): the growth spurt.'),
 EX('Explain why a girl and a boy of the same age may look very different in height.', [('puberty starts at different ages', ['different age', 'start', 'earlier', 'later']), ('the growth spurt happens at different times', ['growth spurt', 'grow fast'])], 'Puberty often starts earlier in girls, so a girl may have her growth spurt before a boy of the same age.', o='O5', d='H'),
 MC('Which statement about the life cycle is TRUE?', 'Reproduction lets the life cycle start again', [('Adults cannot have children', 'Adults can reproduce.'), ('Only animals have a life cycle', 'Plants have one too.')], o='O5', d='H'),
)
s.labs('Growth lab',
 {'kind': 'growth', 'title': 'Read heights on a ruler', 'intro': 'Here is a family standing next to a height ruler. Read each person\'s height to the nearest 5 cm.',
  'people': [{'n': 'Baby Kim', 'h': 75, 'c': '#FFD6E0'}, {'n': 'Lan, age 6', 'h': 115, 'c': '#7FB3F0'}, {'n': 'Minh, age 12', 'h': 150, 'c': '#9BD2A4'}, {'n': 'Mum', 'h': 160, 'c': '#F3BF69'}],
  'qs': [MC('Who is the tallest in the family?', 'Mum', [('Minh', 'Minh is 150 cm.'), ('Lan', 'Lan is 115 cm.')], o='O5'),
         S('How much taller is Minh than Lan? (in cm)', ['35'], o='O5', reason='150 − 115 = 35 cm.'),
         MC('Minh is 12. What might happen to his height in the next two years?', 'He may grow quickly – a growth spurt', [('He will get shorter', 'Children do not shrink.'), ('He will stop growing at once', 'Most teenagers keep growing.')], o='O5')]},
 {'title': 'Our family heights', 'intro': 'Measure how tall the people in your home are, and compare.',
  'need': ['a tape measure', 'a pencil and a book (to mark the wall safely)', 'family members who agree to be measured'],
  'safety': ['Ask before you mark anything – use a sticky note, not the wall paint.', 'Ask people if they are happy to share their height.'],
  'steps': ['Stand with your back against a wall, heels together, looking straight ahead.', 'A helper rests a book flat on your head and marks the bottom of the book with a sticky note.', 'Measure from the floor to the mark in centimetres.', 'Measure two more people.'],
  'record': {'head': ['Person', 'Height (cm)'], 'rows': [['Me', {'min': 90, 'max': 200}], ['Person 2', {'min': 40, 'max': 220}], ['Person 3', {'min': 40, 'max': 220}]], 'hint': 'Heights are usually between 50 and 200 cm.'},
  'qs': [MC('Do people of the same age always have the same height?', 'No – people grow at different rates', [('Yes – always', 'Look at children in your class.'), ('Only adults do', 'Adults are different heights too.')], o='O5')]})

# =====================================================================================  1.4
s = U.section('1.4', 'Diseases', ['O6', 'O7']); s.words(V['1.4']); core(s, 'O6', 'O7')
s.stop(MC('Which is the smallest: a bacterium, a virus or a fungus?', 'A virus', [('A bacterium', 'Viruses are even smaller than bacteria.'), ('A fungus', 'Many fungi, like mushrooms, can be seen without a microscope.')], o='O6'),
       MC('Which disease is caused by a virus?', 'Flu', [('Athlete\'s foot', 'That is caused by a fungus.'), ('Cholera', 'That is caused by bacteria.')], o='O6'))
s.stop(MC('Why should we wash our hands with soap, not just water?', 'Soap helps to remove germs that water alone leaves behind', [('Soap smells nice', 'That is not the main reason.'), ('Water is dirty', 'Clean water is fine – but soap removes more germs.'), ('Soap makes hands dry', 'That is not why.')], o='O7'),
       MC('When should you wash your hands?', 'Before eating and after using the toilet', [('Only once a week', 'Wash them many times a day.'), ('Only when they look dirty', 'Germs are too small to see.')], o='O7'))
s.prac(
 MC('What is a disease?', 'Something that stops the body working properly', [('A healthy food', 'Food is not a disease.'), ('A type of exercise', 'Exercise keeps us healthy.')], o='O6'),
 MC('What does "infectious" mean?', 'It can pass from one person to another', [('It cannot be caught', 'That is the opposite.'), ('It only affects animals', 'Infectious diseases can affect people.')], o='O6'),
 MT('Match each word to its meaning.', [('parasite', 'lives on or in another living thing and harms it'), ('host', 'the living thing a parasite lives on'), ('vector', 'carries a disease from one person to another')], o='O6'),
 GD('What causes each disease?', 'Caused by', [('flu', 'a virus'), ('chicken pox', 'a virus'), ('cholera', 'bacteria'), ('athlete\'s foot', 'a fungus')], o='O6'),
 MC('Are all bacteria harmful?', 'No – many bacteria are harmless', [('Yes – all bacteria cause disease', 'Many are harmless or even useful.'), ('Bacteria are not living', 'Bacteria are living things.')], o='O6'),
 MC('We use a fungus to make bread rise. What is it called?', 'Yeast', [('Mould', 'Mould is a fungus, but yeast makes bread rise.'), ('A virus', 'Viruses are not used to make bread.')], o='O6'),
 MT('Match each body defence to how it helps.', [('skin', 'a barrier that stops germs getting in'), ('tears', 'contain a chemical that kills some bacteria'), ('mucus', 'traps germs in the nose and windpipe'), ('stomach acid', 'kills germs in food')], o='O6'),
 MC('Why are we not ill all the time, even though germs are all around us?', 'Our body has defences, like skin and mucus', [('Germs cannot live near people', 'They can.'), ('We never touch germs', 'We touch them all the time.')], o='O6'),
 TK('Tick the good hygiene habits.', ['Yes', 'No'], [('wash hands before eating', ['✓', '✗']), ('cover food', ['✓', '✗']), ('drink water from a dirty river', ['✗', '✓']), ('sneeze into your elbow', ['✓', '✗'])], o='O7'),
 MC('How should you sneeze if you have no tissue?', 'Into your elbow', [('Into your hand', 'Then you spread germs with your hand.'), ('Into the air', 'The drops spread germs to others.')], o='O7'),
 MC('Why should food not be left out on a hot day?', 'Bacteria and fungi grow faster when it is warm', [('It gets cold', 'The problem is warmth.'), ('It becomes too sweet', 'That is not the reason.')], o='O7'),
 MC('How can you make river water safe to drink?', 'Boil it', [('Add sugar', 'Sugar does not kill germs.'), ('Leave it in the sun for 1 minute', 'That is not enough.')], o='O7'),
 GD('Is each disease mainly spread in food, in water or by insects?', 'Spread mostly', [('malaria', 'by insects'), ('cholera', 'in water'), ('food poisoning', 'in food')], o='O7', d='H'),
 MC('Which insect spreads malaria?', 'The mosquito', [('The bee', 'Bees do not spread malaria.'), ('The butterfly', 'Butterflies do not bite people.')], o='O7'),
 MS('Select the ways to avoid mosquito bites.', ['sleep under a bed net', 'wear long sleeves', 'use insect repellent'], ['leave windows open at night', 'wear shorts at night'], o='O7'),
 MC('Does a mosquito that spreads malaria get ill with malaria?', 'No – it carries the parasite but is not ill', [('Yes – it always dies', 'It does not get the disease.'), ('Yes – it is the host', 'People are the host.')], o='O7'),
 TB('Class 6 asked people which hygiene habits they use. How many people in total use the two hand-washing habits?', ['Habit', 'Number of people'], [['wash hands after the toilet', '10'], ['wash hands before cooking', '6'], ['total', B(16)]], o='O7'),
 OD('Put the hand-washing steps in order.', ['wet your hands', 'rub with soap for 20 seconds', 'rinse with clean water', 'dry with a clean towel'], o='O7'),
)
s.adv(
 EX('Explain why washing hands before eating helps to stop disease.', [('hands carry germs (bacteria/viruses)', ['germ', 'bacteria', 'virus']), ('soap and water remove the germs', ['soap', 'remove', 'wash away']), ('so germs do not get into our food / mouth', ['food', 'mouth', 'eat'])], 'Our hands pick up germs. Washing with soap and water removes them, so they do not get into our food and mouth.', o='O7', d='H'),
 MC('In the glitter experiment, what was the variable that was CHANGED?', 'The way of washing', [('The amount of glitter', 'Keep the same amount of glitter to be fair.'), ('The person washing', 'Keep the same person.')], o='O7', d='H'),
 MC('In the glitter experiment, glitter left: no wash 240, water only 132, soap and water 20. What is the best conclusion?', 'Washing with soap and water removes the most germs', [('Water alone removes all the germs', '132 pieces were still left.'), ('Washing makes no difference', 'The numbers went down a lot.'), ('Glitter is a real germ', 'Glitter only shows where germs could be.')], o='O7', d='H'),
 MC('Why do scientists use glitter instead of real germs in this experiment?', 'Real germs are too small to see and could make us ill', [('Glitter is cheaper than germs', 'That is not the main reason.'), ('Germs do not stick to hands', 'They do – that is the problem.')], o='O7', d='VH'),
)
s.labs('Glitter germs lab',
 {'kind': 'germs', 'title': 'Which way of washing removes the most germs?', 'intro': 'The glitter shows where germs could be. Wash the hand in each way and record how much glitter is left.',
  'methods': [{'k': 'none', 't': 'No washing', 'left': 1.0}, {'k': 'water', 't': 'Water only', 'left': 0.55}, {'k': 'soap', 't': 'Soap and water', 'left': 0.08}],
  'qs': [MC('Which way of washing left the least glitter?', 'Soap and water', [('Water only', 'Some glitter was still left.'), ('No washing', 'All the glitter stayed.')], o='O7'),
         MC('Which variable did you keep the SAME to make the test fair?', 'The amount of glitter at the start', [('The way of washing', 'That was what you changed.'), ('The number of glitter pieces left', 'That was what you measured.')], o='O7'),
         MC('What does this tell us about real germs?', 'Washing with soap and water is the best way to remove germs', [('Germs cannot be washed off', 'Most can be washed off.'), ('Water alone is always enough', 'Soap removes much more.')], o='O7')]},
 {'title': 'Glitter hand-washing test', 'intro': 'Use glitter as pretend germs and test two ways of washing.',
  'need': ['a small pinch of glitter (or flour)', 'a teaspoon of cooking oil or hand cream', 'soap, water and a towel', 'a paper towel to count on'],
  'safety': ['Keep glitter away from your eyes and mouth.', 'Ask an adult before you start; clean up the sink afterwards.'],
  'steps': ['Rub a little hand cream on your hands, then sprinkle the same small pinch of glitter on them.', 'Rinse with water only for 10 seconds. Pat dry on a white paper towel and estimate how much glitter is left (count the pieces on one finger).', 'Repeat with new glitter, but this time wash with soap and water for 20 seconds.', 'Compare your two results.'],
  'record': {'head': ['How I washed', 'Glitter pieces left on one finger'], 'rows': [['Water only (10 s)', {'min': 0, 'max': 500}], ['Soap and water (20 s)', {'min': 0, 'max': 500}]], 'hint': 'Count the pieces on one finger – any number from 0 upwards.'},
  'qs': [MC('Which way removed more glitter in YOUR test?', 'Soap and water', [('Water only', 'Check your results – in most tests soap and water removes more.'), ('They were exactly the same', 'Look at your numbers again.')], o='O7')]})

U.mindmap(('Circulatory system', 'Heart, blood vessels and blood carry food and oxygen around the body.', 'O1', '1.1'), ('Pulse rate', 'Beats per minute; goes up with exercise.', 'O2', '1.1'),
          ('Respiratory system', 'Lungs, windpipe and the diaphragm let us breathe.', 'O3', '1.2'), ('Breathing rate', 'Breaths per minute; goes up with exercise.', 'O4', '1.2'),
          ('Puberty', 'Hormones change a child\'s body into an adult\'s body.', 'O5', '1.3'), ('Diseases', 'Bacteria, viruses, fungi and other parasites.', 'O6', '1.4'), ('Stopping the spread', 'Hygiene, clean water, bed nets.', 'O7', '1.4'))
