# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 5 · Unit 2 Sound. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit5 import *

OBJ = {
 'O1': {'sec': '2.1', 'code': 'Physics', 'codeNote': '', 't': 'Explain that sounds are made by vibrations and travel through solids, liquids and gases, but not through empty space.'},
 'O2': {'sec': '2.2', 'code': 'Physics', 'codeNote': '', 't': 'Describe volume and pitch, and link them to the size and speed of vibrations.'},
 'O3': {'sec': '2.3', 'code': 'Physics', 'codeNote': '', 't': 'Describe how distance and sound insulators change the volume of a sound.'},
 'O4': {'sec': '2.3', 'code': 'Working scientifically', 'codeNote': '', 't': 'Plan a fair test of materials as sound insulators and draw a conclusion.'},
 'O5': {'sec': '2.4', 'code': 'Physics', 'codeNote': '', 't': 'Explain how the length, tension and thickness of strings, and the length of tubes and bars, change pitch.'},
}
U = Unit(2, 'Sound', 'Physics: sound', 'Vibrations, volume, pitch and sound insulators – and how musical instruments work.', OBJ)

# =====================================================================================  2.1
s = U.section('2.1', 'How sounds are made', ['O1']); s.words(V['2.1']); core(s, 'O1', 'O1')
s.stop(MC('What must happen to make a sound?', 'Something must vibrate', [('Something must get hot', 'Sound comes from vibrations.'), ('Something must be shiny', 'Shiny things reflect light, not sound.'), ('The lights must be on', 'Sound does not need light.')], o='O1'),
       MC('Why does rice jump on a drum when you hit it?', 'The drum skin is vibrating', [('The rice is scared', 'Ha! It is the vibrations.'), ('The drum is hot', 'It is not hot.')], o='O1'))
s.stop(MC('Can sound travel through a solid?', 'Yes – sound travels well through solids like wood and metal', [('No – only through air', 'Put your ear on a table and tap it!'), ('Only through ice', 'All solids carry sound.')], o='O1'),
       MC('Why is there no sound in space?', 'There is no air (no medium) to carry the vibrations', [('It is too cold', 'It is about having no medium.'), ('It is too dark', 'Light does not affect sound.')], o='O1'))
s.prac(
 MC('What does "vibrate" mean?', 'Move backwards and forwards very quickly', [('Get very hot', 'It is about moving.'), ('Change colour', 'It is about moving.')], o='O1'),
 GD('What vibrates to make each sound?', 'What vibrates', [('a guitar', 'the string'), ('a drum', 'the skin'), ('your voice', 'your voice box'), ('a mosquito', 'its wings')], o='O1'),
 MC('What is a sound source?', 'Anything that makes a sound', [('Only musical instruments', 'Any object that makes a sound.'), ('Our ears', 'Ears receive sound.')], o='O1'),
 MC('How does sound reach your ear?', 'The vibrations travel through the air', [('Light carries it', 'Sound is vibrations.'), ('It jumps straight into your ear', 'It travels through a medium.')], o='O1'),
 GD('Is each medium a solid, a liquid or a gas?', 'State', [('air', 'gas'), ('water', 'liquid'), ('wooden table', 'solid'), ('metal railing', 'solid')], o='O1'),
 MC('You put your ear on a table and tap it. What do you notice?', 'The tap sounds louder through the wood', [('You cannot hear anything', 'Sound travels well through solids.'), ('It sounds exactly the same', 'Solids carry sound well.')], o='O1'),
 MC('How do astronauts talk to each other on a spacewalk?', 'By radio', [('By shouting', 'Sound cannot travel in space.'), ('By tapping helmets only', 'They use radios.')], o='O1'),
 MC('Why can whales hear each other far away?', 'Sound travels well through water', [('Whales have huge ears', 'It is about water carrying sound.'), ('Water is quiet', 'Water carries sound well.')], o='O1'),
 CZ('Complete the sentences.', 'All sounds are made by {0}. Sound needs a {1} to travel through. It cannot travel through empty {2}.', [['vibrations', 'vibration'], ['medium'], ['space']], o='O1'),
 MC('In a string telephone, what carries the sound between the cups?', 'The vibrating string', [('The air only', 'The tight string carries it.'), ('Magic', 'It is vibrations in the string.')], o='O1'),
 MC('What happens if the string of a string telephone is loose?', 'The sound does not travel well', [('It gets louder', 'Loose strings do not pass vibrations well.'), ('Nothing changes', 'It must be tight.')], o='O1'),
 TK('Tick the true statements.', ['True', 'False'], [('a bell vibrates when it rings', ['✓', '✗']), ('sound travels through water', ['✓', '✗']), ('sound travels through empty space', ['✗', '✓'])], o='O1'),
 MC('When you hum, which part of your body vibrates?', 'Your voice box (in your throat)', [('Your knees', 'Feel your throat!'), ('Your hair', 'Feel your throat.')], o='O1'),
 MC('A phone speaker makes music. What is happening inside it?', 'A part vibrates', [('Tiny people sing', 'Ha! A part vibrates.'), ('Light flashes', 'Sound needs vibrations.')], o='O1'),
)
s.adv(
 EX('Explain how you hear a friend clapping across the room.', [('the hands make the air vibrate', ['vibrat']), ('the vibrations travel through the air', ['air', 'travel']), ('they reach your ear', ['ear'])], 'Clapping makes the air vibrate. The vibrations travel through the air (the medium) and reach your ear, so you hear the sound.', o='O1', d='H'),
 MC('An alarm clock rings inside a jar. All the air is pumped out. What happens to the sound?', 'It gets quieter and then cannot be heard', [('It gets louder', 'Less air means less sound travels.'), ('Nothing changes', 'Sound needs a medium.')], o='O1', d='VH'),
 MC('Which is the best way to show that a drum vibrates?', 'Put rice on it and watch the rice jump', [('Look at it in the dark', 'Vibrations are too small to see in the dark.'), ('Paint it', 'Painting does not show vibrations.')], o='O1', d='H'),
 MS('Select the mediums that sound can travel through.', ['air', 'water', 'wood', 'metal'], ['empty space'], o='O1', d='H'),
)
s.labs('Sound travel lab',
 sort_lab('What does the sound travel through?', 'Sort each example by the medium the sound travels through.', ['Solid', 'Liquid', 'Gas'],
  [('ear on a tapped table', '🪑', 0, 'The table is a solid.'), ('whale song in the sea', '🐋', 1, 'Sea water is a liquid.'), ('a friend talking in the room', '🗣️', 2, 'The room is full of air, a gas.'),
   ('a string telephone', '🧵', 0, 'The string is a solid.'), ('swimmers hearing a whistle underwater', '🏊', 1, 'Water is a liquid.'), ('birdsong in the park', '🐦', 2, 'It travels through the air.')],
  [MC('Which can NOT carry sound?', 'Empty space', [('Water', 'Water carries sound well.'), ('Wood', 'Wood carries sound well.')], o='O1'),
   MC('Through which did the tap sound loudest in the table example?', 'The solid table', [('The air', 'Solids carry sound well.'), ('It was the same', 'It was louder through the table.')], o='O1')]),
 home('String telephone', 'Make a telephone and test it.', ['2 paper cups', 'about 5 m of string', 'a sharp pencil and an adult to make holes'],
  ['Ask an adult to make the holes.', 'Do not pull the string near anyone\'s face.'],
  ['Make a small hole in the bottom of each cup and tie the string between them.', 'Stand far apart and pull the string tight.', 'Talk quietly into one cup while your partner listens.', 'Try with the string loose, and count the words your partner hears each time.'],
  ['String', 'Words heard (out of 10)'], [['Tight', {'min': 0, 'max': 10}], ['Loose', {'min': 0, 'max': 10}]], 'Say 10 words each time and count how many your partner heard.',
  [MC('Why does the tight string work better?', 'It vibrates and passes the vibrations along', [('It is longer', 'It is the same string.'), ('It is quieter', 'It carries the sound better.')], o='O1')]))

# =====================================================================================  2.2
s = U.section('2.2', 'Volume and pitch', ['O2']); s.words(V['2.2']); core(s, 'O2', 'O2')
s.stop(MC('How can you make a drum sound louder?', 'Hit it harder to make bigger vibrations', [('Hit it more gently', 'That makes it quieter.'), ('Paint it red', 'Colour does not change volume.'), ('Hit it more slowly', 'It is about how hard you hit.')], o='O2'),
       MC('What is volume?', 'How loud or quiet a sound is', [('How high or low a sound is', 'That is pitch.'), ('How long a sound lasts', 'That is not volume.')], o='O2'))
s.stop(MC('Which makes a higher pitch: a short string or a long string?', 'A short string', [('A long string', 'Long strings vibrate slowly: low pitch.'), ('They are the same', 'Length changes pitch.')], o='O2'),
       MC('What is pitch?', 'How high or low a sound is', [('How loud a sound is', 'That is volume.'), ('How far a sound travels', 'That is not pitch.')], o='O2'))
s.prac(
 GD('Does each change affect the volume or the pitch?', 'Changes the', [('hitting a drum harder', 'volume'), ('using a shorter string', 'pitch'), ('blowing a recorder more gently', 'volume'), ('tightening a guitar string', 'pitch')], o='O2'),
 MC('Big vibrations make a sound that is…', 'loud', [('quiet', 'Small vibrations are quiet.'), ('high', 'Pitch depends on speed.')], o='O2'),
 MC('Fast vibrations make a sound that is…', 'high-pitched', [('low-pitched', 'Slow vibrations are low.'), ('quieter', 'Speed changes pitch.')], o='O2'),
 OD('Put these sounds in order from quietest to loudest.', ['leaves rustling', 'people talking', 'a fire engine siren'], o='O2'),
 OD('Put these animals in order from lowest to highest pitch.', ['elephant', 'dog', 'mouse'], o='O2'),
 MC('Why do workers near loud machines wear ear defenders?', 'Very loud sounds can damage their ears', [('To keep warm', 'They protect hearing.'), ('To hear better', 'They make sounds quieter.')], o='O2'),
 MC('Why can\'t we hear most bat sounds?', 'Their pitch is too high for our ears', [('They are too quiet', 'It is about pitch.'), ('Bats never make sounds', 'They do – very high ones.')], o='O2'),
 MT('Match each sound to its description.', [('a whistle', 'high pitch'), ('a big bass drum', 'low pitch'), ('a whisper', 'quiet'), ('a shout', 'loud')], o='O2'),
 CZ('Complete the sentences.', 'Volume is how {0} or quiet a sound is. Pitch is how {1} or low a sound is.', [['loud'], ['high']], o='O2'),
 MC('On a computer, a high-pitched sound shows waves that are…', 'close together', [('far apart', 'Far apart is low pitch.'), ('very tall', 'Tall waves are loud.')], o='O2'),
 MC('On a computer, a loud sound shows waves that are…', 'tall', [('short', 'Short waves are quiet.'), ('close together', 'That shows pitch.')], o='O2'),
 MC('On a rubber band guitar, which band makes the highest note?', 'The shortest, tightest band', [('The longest, loosest band', 'That makes the lowest note.'), ('They are all the same', 'Length and tension change pitch.')], o='O2'),
 MC('Can a sound be loud AND low?', 'Yes – volume and pitch are different', [('No – loud sounds are always high', 'A big drum is loud and low.'), ('No – low sounds are always quiet', 'They are separate.')], o='O2', d='H'),
 MC('A singer sings the same note louder. What changes?', 'The volume, not the pitch', [('The pitch, not the volume', 'Same note means same pitch.'), ('Both', 'Only volume changes.')], o='O2', d='H'),
)
s.adv(
 EX('Explain the difference between volume and pitch.', [('volume: how loud or quiet', ['loud', 'quiet']), ('pitch: how high or low', ['high', 'low']), ('volume depends on size of vibration, pitch on speed', ['size', 'big', 'speed', 'fast'])], 'Volume is how loud or quiet a sound is and depends on the size of the vibrations. Pitch is how high or low a sound is and depends on how fast the vibrations are.', o='O2', d='H'),
 TB('A sound meter measured a drum hit in three ways. Complete the table.', ['How hard', 'Volume (decibels)'], [['gently', '40'], ['medium', '60'], ['hard', B(80)]], o='O2', skill='Data', hint='Each harder hit added 20.'),
 MC('Which wave picture would show a quiet, high-pitched sound?', 'Short waves close together', [('Tall waves far apart', 'That is loud and low.'), ('Tall waves close together', 'That is loud and high.')], o='O2', d='VH'),
 MC('A big dog and a small dog bark. The small dog barks higher. Why might this be?', 'Its smaller voice box vibrates faster', [('It is angrier', 'Pitch depends on vibration speed.'), ('It is further away', 'Distance changes volume, not pitch.')], o='O2', d='H'),
)
s.labs('Volume lab',
 test_lab('How hard should you hit the drum?', 'A sound meter measures the volume of a drum in decibels. Choose how hard to hit it and read the meter.', 'How hard the drum is hit', 'Volume', 'dB', 100, 10, '🥁',
  [('Tap gently', '🪶', 40), ('Hit medium', '🥁', 60), ('Hit hard', '💥', 80)],
  [MC('What happened to the volume as you hit harder?', 'It went up', [('It went down', 'Look at the bars.'), ('It stayed the same', 'The numbers changed.')], o='O2'),
   MC('Why did hitting harder make a louder sound?', 'The drum skin made bigger vibrations', [('The drum got hotter', 'It is about vibrations.'), ('The pitch went down', 'Volume changed, not pitch.')], o='O2')]),
 home('Rubber band guitar', 'Make a guitar and explore pitch.', ['an empty tissue box or plastic tub', '3 rubber bands of different thickness', 'a pencil'],
  ['Do not stretch bands near your eyes.', 'Do not let go of a stretched band towards anyone.'],
  ['Stretch the three bands around the open box.', 'Pluck each one and listen.', 'Put the pencil under the bands to make the vibrating part shorter.', 'Rank the bands from lowest to highest pitch (1 = lowest).'],
  ['Band', 'Rank (1 = lowest)'], [['Thick band', {'min': 1, 'max': 3}], ['Medium band', {'min': 1, 'max': 3}], ['Thin band', {'min': 1, 'max': 3}]], 'Use 1, 2 and 3.',
  [MC('Which band usually has the highest pitch?', 'The thin band', [('The thick band', 'Thick bands vibrate more slowly.'), ('They are all the same', 'Thickness changes pitch.')], o='O2')]))

# =====================================================================================  2.3
s = U.section('2.3', 'Changing the volume of sound', ['O3', 'O4']); s.words(V['2.3']); core(s, 'O3', 'O3')
s.stop(MC('Why do soft materials make sounds quieter?', 'They absorb the vibrations', [('They make the sound higher', 'They change volume, not pitch.'), ('They reflect all the sound back louder', 'Soft materials absorb sound.'), ('They are heavy', 'It is about absorbing vibrations.')], o='O3'),
       MC('What happens to a sound as you walk away from it?', 'It gets quieter', [('It gets louder', 'Greater distance makes it quieter.'), ('Its pitch gets higher', 'Distance changes volume.')], o='O3'))
s.stop(MC('Which is the best sound insulator: foam, metal or glass?', 'Foam', [('Metal', 'Metal carries sound well.'), ('Glass', 'Glass lets sound through.')], o='O3'),
       MC('What is a sound insulator?', 'A material that stops sound passing through', [('A material that makes sound louder', 'That is an amplifier.'), ('A musical instrument', 'Insulators muffle sound.')], o='O3'))
s.prac(
 GD('Is each material a good or poor sound insulator?', 'Sound insulator', [('foam', 'good'), ('thick wool', 'good'), ('metal sheet', 'poor'), ('egg boxes', 'good')], o='O3'),
 MC('What does "muffle" mean?', 'Make a sound quieter by covering it', [('Make a sound higher', 'Muffling changes volume.'), ('Make a sound louder', 'It makes it quieter.')], o='O3'),
 MC('Why do recording studios have foam on the walls?', 'The foam absorbs sound so there are no echoes', [('To keep warm', 'It is about sound.'), ('To look nice', 'It has a sound job.')], o='O3'),
 MC('How do double windows help people who live near a busy road?', 'They block some of the traffic noise', [('They make the traffic go slower', 'They block sound.'), ('They make the road quieter for drivers', 'They help people inside.')], o='O3'),
 MC('How does a megaphone make your voice louder?', 'It points all the sound in one direction', [('It makes your voice higher', 'It changes volume.'), ('It absorbs the sound', 'That would make it quieter.')], o='O3'),
 MC('Why does cupping your hand behind your ear help you hear?', 'It catches more sound and directs it into your ear', [('It makes the sound higher', 'It collects sound.'), ('It blocks other sounds only', 'It collects more sound.')], o='O3'),
 MC('Why does a guitar have a hollow body?', 'It makes the sound of the strings louder', [('To make it lighter only', 'The hollow body boosts sound.'), ('To store picks', 'It is for sound.')], o='O3'),
 CZ('Complete the sentences.', 'The further you are from a sound, the {0} it is. Soft materials {1} sound. They are good sound {2}.', [['quieter'], ['absorb', 'muffle'], ['insulators']], o='O3'),
 MC('In the sound insulator test, what do you change?', 'The material wrapped around the timer', [('The timer', 'Use the same timer.'), ('The person listening', 'Keep the same listener.')], o='O4'),
 MC('In the sound insulator test, what do you measure?', 'The distance at which you can no longer hear the timer', [('The weight of the material', 'Measure the distance.'), ('The colour of the material', 'Measure the distance.')], o='O4'),
 MS('Which things must stay the SAME to keep the insulator test fair?', ['the same timer', 'the same listener', 'the same thickness of material'], ['the type of material'], o='O4'),
 TB('Results of the insulator test. Which material was best? Complete the table with its rank (1 = best).', ['Material', 'Distance until silent (m)', 'Rank'], [['no material', '10', '4'], ['newspaper', '7', '3'], ['bubble wrap', '5', B(2)], ['foam', '2', B(1)]], o='O4', skill='Data', reason='The shorter the distance, the better the insulator.'),
 MC('What is the conclusion of this test?', 'Foam is the best sound insulator of these materials', [('Newspaper is the best', 'It let sound through to 7 m.'), ('All materials are the same', 'The distances were different.')], o='O4'),
 MC('Why should the listener walk away slowly and stop as soon as the sound disappears?', 'To measure the distance accurately', [('To save time', 'It is about accuracy.'), ('So the timer stops', 'The timer keeps ringing.')], o='O4', d='H'),
)
s.adv(
 EX('Explain why a thick curtain makes a room quieter.', [('soft / thick material', ['soft', 'thick']), ('absorbs the vibrations', ['absorb', 'soak']), ('less sound passes through / reflects', ['less', 'through', 'quieter'])], 'The curtain is soft and thick, so it absorbs the sound vibrations. Less sound passes through it or bounces around the room.', o='O3', d='H'),
 GR('Plot the insulator results as points.', {'label': 'Material (1 none, 2 paper, 3 bubble wrap, 4 foam)', 'min': 0, 'max': 5, 'step': 1}, {'label': 'Distance until silent (m)', 'min': 0, 'max': 12, 'step': 2}, [[1, 10], [2, 7], [3, 5], [4, 2]], o='O4', d='H', table_rows=[[1, 10], [2, 7], [3, 5], [4, 2]]),
 MC('Leo used a thick layer of foam but a thin layer of newspaper. What is wrong with his test?', 'It is not fair – the thickness should be the same', [('Nothing is wrong', 'Two things changed.'), ('He should use a louder timer', 'The problem is the thickness.')], o='O4', d='H'),
 MC('Which room would have the most echoes?', 'An empty room with hard walls and floor', [('A bedroom full of soft furniture', 'Soft things absorb sound.'), ('A recording studio', 'Studios have foam.')], o='O3', d='VH'),
)
s.labs('Sound insulator lab',
 test_lab('Which material muffles sound best?', 'A ringing timer was wrapped in different materials. The listener walked away until it went silent. Read the measuring tape.', 'The material', 'Distance until silent', 'm', 12, 1, '📏',
  [('No material', '⏰', 10), ('Newspaper', '📰', 7), ('Bubble wrap', '🫧', 5), ('Foam', '🧽', 2)],
  [MC('Which material is the best sound insulator?', 'Foam', [('Newspaper', 'It let the sound reach 7 m.'), ('No material', 'That was the loudest.')], o='O4'),
   MC('Why did we test the timer with no material too?', 'To compare the materials with nothing at all', [('To break the timer', 'It is a comparison.'), ('Because it was quieter', 'It was the loudest.')], o='O4')]),
 home('Muffle the alarm', 'Test materials from home as sound insulators.', ['a phone or timer that can ring', 'a box', '3 materials, e.g. a towel, newspaper, a jumper', 'a tape measure'],
  ['Ask before using a phone.', 'Keep the volume at a safe level.'],
  ['Put the ringing timer in the box with no material and walk away until you cannot hear it. Measure the distance.', 'Wrap the box in the first material and repeat.', 'Repeat for the other materials, keeping the volume the same.', 'Compare your distances.'],
  ['Material', 'Distance until silent (m)'], [['No material', {'min': 0.1, 'max': 100}], ['Material 1', {'min': 0.1, 'max': 100}], ['Material 2', {'min': 0.1, 'max': 100}]], 'Distances are usually 1 to 20 m.',
  [MC('Which material is the best insulator in your test?', 'The one with the shortest distance', [('The one with the longest distance', 'Longer means more sound got through.'), ('The heaviest one', 'Use your measurements.')], o='O4')]))

# =====================================================================================  2.4
s = U.section('2.4', 'Changing the pitch of sound', ['O5']); s.words(V['2.4']); core(s, 'O5', 'O5')
s.stop(MC('How can you make a guitar string sound higher?', 'Make it shorter or tighter', [('Make it longer', 'Longer strings sound lower.'), ('Make it looser', 'Looser strings sound lower.'), ('Pluck it more gently', 'That makes it quieter, not higher.')], o='O5'),
       MC('What does a guitar\'s tuning peg change?', 'The tension of the string', [('The colour of the string', 'It changes the tightness.'), ('The length of the guitar', 'It tightens the string.')], o='O5'))
s.stop(MC('Which bar on a xylophone makes the lowest note?', 'The longest bar', [('The shortest bar', 'Short bars make high notes.'), ('The middle bar', 'The longest bar is lowest.')], o='O5'),
       MC('You blow across bottles with different amounts of water. Which makes the lowest note?', 'The bottle with the most air (least water)', [('The bottle with the most water', 'When you blow, the air vibrates.'), ('They all sound the same', 'The air column changes the note.')], o='O5'))
s.prac(
 GD('Does each change make the pitch higher or lower?', 'Pitch', [('shorter string', 'higher'), ('looser string', 'lower'), ('thinner string', 'higher'), ('longer xylophone bar', 'lower'), ('tighter drum skin', 'higher')], o='O5'),
 MC('What does "tension" mean?', 'How tight something is stretched', [('How long something is', 'That is length.'), ('How loud something is', 'That is volume.')], o='O5'),
 MC('Why do guitarists press the strings onto the frets?', 'To make the vibrating part shorter and the note higher', [('To make the strings quieter', 'It changes pitch.'), ('To stop the strings vibrating', 'The string still vibrates.')], o='O5'),
 MC('In a trumpet, what vibrates to make the sound?', 'The air inside the tube', [('The metal bell only', 'The air column vibrates.'), ('The valves', 'The valves change the length.')], o='O5'),
 MC('Which trumpet tube length gives a higher note?', 'A shorter tube', [('A longer tube', 'Longer tubes are lower.'), ('Tube length does not matter', 'It changes pitch.')], o='O5'),
 MC('You TAP bottles with different amounts of water. Which gives the lowest note?', 'The bottle with the most water', [('The bottle with the least water', 'When tapped, more water vibrates more slowly.'), ('They are all the same', 'The water changes the note.')], o='O5', d='H'),
 MT('Match each instrument to how you change its pitch.', [('guitar', 'press the string to make it shorter'), ('drum', 'tighten the skin'), ('xylophone', 'hit a shorter or longer bar'), ('trumpet', 'change the length of the tube')], o='O5'),
 CZ('Complete the sentences.', 'Shorter strings make {0} notes. Tighter strings make {1} notes. Longer bars make {2} notes.', [['higher', 'high'], ['higher', 'high'], ['lower', 'low']], o='O5'),
 OD('Order these xylophone bars from lowest note to highest note.', ['30 cm bar', '25 cm bar', '20 cm bar', '15 cm bar'], o='O5'),
 MC('Why did the singer climb a ladder?', 'To reach the high notes (it is a joke!)', [('To fix the lights', 'It is a joke about pitch.'), ('Because the stage was high', 'It is a joke.')], o='O5'),
 MC('Why does a violin string look blurry when it plays?', 'It vibrates too fast to see', [('It is dirty', 'It is vibrating very fast.'), ('It is melting', 'It is vibrating.')], o='O5'),
 TK('Tick the changes that make a higher note.', ['Higher', 'Not higher'], [('a shorter string', ['✓', '✗']), ('a looser string', ['✗', '✓']), ('a thinner string', ['✓', '✗']), ('plucking harder', ['✗', '✓'])], o='O5'),
 MC('Plucking a string harder makes the sound…', 'louder, but the same pitch', [('higher', 'Plucking harder changes volume.'), ('lower', 'It changes volume.')], o='O5', d='H'),
 MC('Which string on a guitar plays the lowest note?', 'The thickest string', [('The thinnest string', 'Thin strings are higher.'), ('They all play the same note', 'They are different thicknesses.')], o='O5'),
)
s.adv(
 EX('Explain how to tune a guitar string to a higher note.', [('turn the peg to tighten the string', ['tight', 'peg', 'tension']), ('the string vibrates faster', ['faster', 'vibrat']), ('so the pitch is higher', ['higher', 'pitch'])], 'Turn the tuning peg to tighten the string. More tension makes the string vibrate faster, so the pitch is higher.', o='O5', d='H'),
 TB('Bottle xylophone: complete the table (more water = lower note when tapped).', ['Bottle', 'Water (cm)', 'Note order (1 = lowest)'], [['A', '20', B(1)], ['B', '15', B(2)], ['C', '10', B(3)], ['D', '5', B(4)]], o='O5', skill='Data'),
 MC('Two strings are the same length and tension. One is thick and one is thin. Which is lower?', 'The thick string', [('The thin string', 'Thin strings vibrate faster.'), ('They sound the same', 'Thickness changes pitch.')], o='O5', d='H'),
 MC('Why does a big tuba sound lower than a small trumpet?', 'Its tube is much longer, so the air vibrates more slowly', [('It is louder', 'Volume is not pitch.'), ('It is made of different metal', 'Tube length matters most.')], o='O5', d='VH'),
)
s.labs('Pitch lab',
 sort_lab('High or low?', 'Sort each change into the group it makes: a higher pitch or a lower pitch.', ['Higher pitch', 'Lower pitch'],
  [('shorter string', '📏', 0, 'Shorter strings vibrate faster.'), ('longer xylophone bar', '🎹', 1, 'Longer bars vibrate more slowly.'), ('tighter drum skin', '🥁', 0, 'More tension, faster vibrations.'),
   ('looser string', '🪢', 1, 'Less tension, slower vibrations.'), ('thinner string', '🧵', 0, 'Thin strings vibrate faster.'), ('longer trumpet tube', '🎺', 1, 'A longer air column vibrates more slowly.')],
  [MC('What do all the "higher pitch" changes do to the vibrations?', 'Make them faster', [('Make them bigger', 'Bigger vibrations are louder.'), ('Stop them', 'They still vibrate.')], o='O5'),
   MC('Which change would make a guitar note lower?', 'Loosening the string', [('Shortening the string', 'That makes it higher.'), ('Tightening the string', 'That makes it higher.')], o='O5')]),
 home('Bottle xylophone', 'Make music with bottles of water.', ['4 glass bottles or jars the same size', 'water', 'a metal spoon', 'a ruler'],
  ['Tap gently – do not break the glass.', 'Work on a table, not near the edge.'],
  ['Fill the bottles with different amounts of water.', 'Measure the water height in each bottle.', 'Tap each bottle gently with the spoon.', 'Put them in order from lowest to highest note (1 = lowest).'],
  ['Bottle', 'Water height (cm)', 'Note order (1 = lowest)'], [['Bottle 1', {'min': 0, 'max': 40}, {'min': 1, 'max': 4}], ['Bottle 2', {'min': 0, 'max': 40}, {'min': 1, 'max': 4}], ['Bottle 3', {'min': 0, 'max': 40}, {'min': 1, 'max': 4}], ['Bottle 4', {'min': 0, 'max': 40}, {'min': 1, 'max': 4}]], 'Use 1–4 for the order.',
  [MC('When you tapped the bottles, which made the lowest note?', 'The one with the most water', [('The one with the least water', 'More water vibrates more slowly.'), ('The empty one', 'It made a high note.')], o='O5')]))

U.mindmap(('Vibrations', 'Every sound comes from something vibrating.', 'O1', '2.1'), ('Volume and pitch', 'Big vibrations: loud. Fast vibrations: high.', 'O2', '2.2'),
          ('Muffling sound', 'Distance and soft materials make sounds quieter.', 'O3', '2.3'), ('Fair tests', 'Testing sound insulators.', 'O4', '2.3'), ('Instruments', 'Length, tension and thickness change pitch.', 'O5', '2.4'))
