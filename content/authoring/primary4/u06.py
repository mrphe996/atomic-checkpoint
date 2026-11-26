# -*- coding: utf-8 -*-
"""Cambridge Primary Science Stage 4 · Unit 6 Electricity. Written by the Camday teaching team."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit4 import *

OBJ = {
 'O1': {'sec': '6.1', 'code': 'Physics', 'codeNote': '', 't': 'Build a simple circuit, and sort materials into electrical conductors and insulators.'},
 'O2': {'sec': '6.2', 'code': 'Physics', 'codeNote': '', 't': 'Know that water can conduct electricity, and follow rules for using electricity safely.'},
 'O3': {'sec': '6.3', 'code': 'Physics', 'codeNote': '', 't': 'Explain why plugs, wires and tools use both conductors and insulators.'},
 'O4': {'sec': '6.4', 'code': 'Physics', 'codeNote': '', 't': 'Know that a switch opens and closes a gap in a circuit to turn it off and on.'},
 'O5': {'sec': '6.5', 'code': 'Physics', 'codeNote': '', 't': 'Predict how adding batteries or bulbs changes how bright bulbs are (or how loud a buzzer is).'},
}
U = YUnit(6, 'Electricity', 'Physics: electricity and magnetism', 'Circuits, conductors and insulators, safety, switches, and brighter or dimmer bulbs.', OBJ)

# ============================================================  6.1
s = U.section('6.1', 'Which materials conduct electricity?', ['O1']); s.words(V['6.1']); core(s, 'O1')
s.stop(PM('What must a circuit be like for the bulb to light?', ('⭕', 'A complete loop with no gaps'), [('↔️', 'It must have a gap', 'A gap stops the electricity.'), ('📏', 'It must be very long', 'It must be a complete loop.')], 'O1'),
       PM('What makes a bulb light in a circuit?', ('🔋', 'A battery'), [('🧦', 'A sock', 'You need a battery.'), ('🍎', 'An apple', 'You need a battery.')], 'O1'))
s.stop(PM('Which material is a conductor?', ('🥄', 'Metal'), [('🧴', 'Plastic', 'Plastic is an insulator.'), ('🪵', 'Wood', 'Wood is an insulator.')], 'O1'),
       PM('Which material is an insulator?', ('🧴', 'Plastic'), [('📎', 'A metal paper clip', 'Metal conducts.'), ('🔑', 'A metal key', 'Metal conducts.')], 'O1'))
s.prac(
 GD('Conductor or insulator?', 'It is a', [('📎 paper clip', 'conductor'), ('🪵 wooden stick', 'insulator'), ('🧴 plastic ruler', 'insulator'), ('🔑 key', 'conductor'), ('🧶 wool', 'insulator')], o='O1'),
 YN('Will the bulb light if there is a gap in the circuit?', False, 'O1', pic='↔️', why='No. Electricity needs a complete loop.'),
 PM('What are wires made of inside?', ('🔩', 'Metal'), [('🪵', 'Wood', 'Metal carries electricity.'), ('📄', 'Paper', 'Metal carries electricity.')], 'O1'),
 PM('You put a coin in the gap of a circuit. What happens?', ('💡', 'The bulb lights'), [('🌑', 'Nothing', 'Coins are metal: they conduct.')], 'O1'),
 PM('You put a crayon in the gap. What happens?', ('🌑', 'The bulb stays off'), [('💡', 'The bulb lights', 'Wax does not conduct.')], 'O1'),
 MT('Match each word to what it means.', [('circuit', 'a loop for electricity'), ('conductor', 'lets electricity flow'), ('insulator', 'stops electricity')], o='O1'),
 TK('Tick the conductors.', ['Conductor', 'Insulator'], [('a metal spoon', ['✓', '✗']), ('a rubber band', ['✗', '✓']), ('a steel nail', ['✓', '✗'])], o='O1'),
 OD('Order how to test a material.', ['make a circuit with a gap', 'put the material in the gap', 'look at the bulb'], o='O1'),
 YN('Are all metals good conductors?', True, 'O1', pic='🔩', why='Yes, metals let electricity flow.'),
 PM('What does a circuit need to work?', ('🔋', 'A battery, wires and no gaps'), [('🎨', 'Lots of colours', 'It needs a complete loop.'), ('🔊', 'A loud noise', 'It needs a complete loop.')], 'O1'),
 PM('Which object will make the bulb light if put in the gap?', ('🔑', 'A key'), [('🧸', 'A teddy', 'Fabric is an insulator.'), ('🎈', 'A balloon', 'Rubber is an insulator.')], 'O1'),
 PM('Which is the best material for the outside of a wire?', ('🧴', 'Plastic'), [('🔩', 'Metal', 'The outside must keep us safe.'), ('🧊', 'Ice', 'Plastic insulates.')], 'O1', d='H'),
)
s.adv(
 PM('* Advanced. A bulb does not light. The battery is new. What should you check first?', ('🔗', 'That there are no gaps in the circuit'), [('🎨', 'The colour of the wires', 'Look for gaps.'), ('📏', 'How long the table is', 'Look for gaps.')], 'O1', d='H'),
 PM('* Advanced. Pencil "lead" is graphite. It makes a bulb glow a little. What does that show?', ('✏️', 'Graphite conducts a little'), [('🚫', 'Graphite is an insulator', 'The bulb glowed.'), ('🔥', 'The pencil is hot', 'It conducts a little.')], 'O1', d='VH'),
 GD('* Advanced. Sort these.', 'It is a', [('🪙 coin', 'conductor'), ('🧱 brick', 'insulator'), ('🥫 steel can', 'conductor')], o='O1', d='H'),
)
s.labs('Circuit lab',
 sort_lab('Conductor tester', 'Put each object in the circuit gap. Does the bulb light?', ['Bulb lights (conductor)', 'Bulb off (insulator)'],
  [('paper clip', '📎', 0, 'Metal conducts.'), ('plastic ruler', '📏', 1, 'Plastic insulates.'), ('coin', '🪙', 0, 'Metal conducts.'), ('wooden lolly stick', '🪵', 1, 'Wood insulates.'), ('key', '🔑', 0, 'Metal conducts.'), ('rubber', '🧽', 1, 'Rubber insulates.')],
  [PM('Which material made the bulb light?', ('🔩', 'Metal'), [('🪵', 'Wood', 'Wood insulates.')], 'O1')]),
 home('Conductor hunt', 'Test materials with a battery circuit, with an adult.', ['a battery, a bulb and wires (a circuit kit)', 'things to test', 'an adult'], ['Use batteries only. Never use mains sockets.'],
  ['Make a circuit with a gap.', 'Put each thing in the gap.', 'Watch the bulb.'],
  ['Thing', 'Did the bulb light?'], [('a spoon', ['yes', 'no']), ('a pencil eraser', ['yes', 'no']), ('foil', ['yes', 'no'])],
  [PM('Which was a conductor?', ('🥄', 'The spoon'), [('🧽', 'The eraser', 'Rubber insulates.')], 'O1')]))

# ============================================================  6.2
s = U.section('6.2', 'Does water conduct electricity?', ['O2']); s.words(V['6.2']); core(s, 'O2')
s.stop(PM('Can water conduct electricity?', ('💧', 'Yes'), [('🚫', 'No', 'Water can conduct, so it is dangerous.')], 'O2'),
       PM('Why are water and electricity dangerous together?', ('⚠️', 'Water can carry electricity to you'), [('🧊', 'Water freezes', 'It can carry electricity.'), ('🎨', 'Water changes colour', 'It can carry electricity.')], 'O2'))
s.stop(PM('Which of these is safe?', ('🙌', 'Drying your hands before touching a switch'), [('💦', 'Touching a plug with wet hands', 'Never with wet hands!'), ('🛁', 'Using a radio in the bath', 'Keep electricity away from water.')], 'O2'),
       PM('Which is dangerous?', ('🔌', 'Putting a fork in a socket'), [('🔋', 'Using batteries in a torch', 'Batteries are safe.'), ('💡', 'Switching on a lamp with dry hands', 'That is safe.')], 'O2'))
s.prac(
 GD('Safe or dangerous?', 'It is', [('🔋 using a battery torch', 'safe'), ('💦 wet hands on a switch', 'dangerous'), ('🔌 poking a socket', 'dangerous'), ('🙌 dry hands on a switch', 'safe')], o='O2'),
 PM('Where does mains electricity come from?', ('🔌', 'Sockets in the wall'), [('🔋', 'Small batteries', 'Batteries are weak.'), ('☁️', 'Clouds', 'It comes from sockets.')], 'O2'),
 YN('Is mains electricity stronger than a battery?', True, 'O2', pic='⚡', why='Yes, much stronger and dangerous.'),
 PM('Which is safe for your experiments?', ('🔋', 'Batteries'), [('🔌', 'Mains sockets', 'Mains is dangerous.'), ('⚡', 'Lightning', 'Lightning is dangerous!')], 'O2'),
 PM('What should you do in a thunderstorm?', ('🏠', 'Stay indoors and away from water'), [('🏊', 'Go swimming', 'Water and lightning are dangerous.'), ('🌳', 'Stand under a tall tree', 'That is dangerous.')], 'O2'),
 MT('Match each word to what it means.', [('mains', 'strong electricity from sockets'), ('danger', 'something that can hurt you'), ('safety', 'keeping safe')], o='O2'),
 TK('Tick the safe rules.', ['Safe', 'Not safe'], [('keep drinks away from computers', ['✓', '✗']), ('pull plugs out by the wire', ['✗', '✓']), ('ask an adult about plugs', ['✓', '✗'])], o='O2'),
 YN('Should you ever put anything into a socket?', False, 'O2', pic='🔌', why='Never!'),
 PM('You spill water near a plugged-in lamp. What should you do?', ('🗣️', 'Tell an adult straight away'), [('🧽', 'Mop it up near the plug yourself', 'Tell an adult.'), ('🙈', 'Ignore it', 'Tell an adult.')], 'O2'),
 PM('What is lightning?', ('⚡', 'A giant spark of electricity'), [('🔥', 'A fire', 'It is electricity.'), ('🌧️', 'Rain', 'It is electricity.')], 'O2'),
 PM('Why do bathrooms have pull-cord light switches?', ('🛁', 'To keep wet hands away from electricity'), [('🎨', 'They look nice', 'It is for safety.'), ('🔊', 'They are louder', 'It is for safety.')], 'O2', d='H'),
 PM('Which is the safest thing to plug in?', ('👨‍👩‍👧', 'Let an adult do it'), [('🧒', 'Do it yourself with wet hands', 'Never with wet hands.')], 'O2'),
)
s.adv(
 PM('* Advanced. Salty water made the bulb glow brighter than pure water. What does this show?', ('🧂', 'Salty water conducts better'), [('🚫', 'Salt is an insulator', 'The bulb glowed brighter.'), ('💡', 'The bulb was new', 'It is about the salt.')], 'O2', d='VH'),
 PM('* Advanced. Why should you never fly a kite near power lines?', ('⚡', 'Electricity could travel down the string'), [('🌬️', 'The wind is too strong', 'It is about electricity.'), ('🐦', 'Birds live there', 'It is about electricity.')], 'O2', d='H'),
 OD('* Advanced. Order from safest to most dangerous.', ['a battery toy', 'a lamp plugged in', 'power lines'], o='O2', d='H'),
)
s.labs('Safety lab',
 sort_lab('Safe or not safe?', 'Sort each picture.', ['Safe', 'Not safe'],
  [('battery torch', '🔦', 0, 'Batteries are safe.'), ('fork in a socket', '🍴', 1, 'Never!'), ('radio next to the bath', '🛁', 1, 'Water and electricity are dangerous.'), ('dry hands on a switch', '🙌', 0, 'Dry hands are safe.'), ('kite near power lines', '🪁', 1, 'Fly kites in open fields.'), ('asking an adult', '🗣️', 0, 'Always ask.')],
  [PM('Which is NOT safe?', ('🍴', 'A fork in a socket'), [('🔦', 'A battery torch', 'That is safe.')], 'O2')]),
 home('Safety poster', 'Make a poster about electricity safety.', ['paper', 'crayons'], ['No experiments with mains electricity!'],
  ['Think of three safety rules.', 'Draw a picture for each.', 'Put the poster up at home.'],
  ['Rule', 'On my poster?'], [('dry hands', ['yes', 'no']), ('nothing in sockets', ['yes', 'no']), ('stay away from water', ['yes', 'no'])],
  [PM('Which rule is most important near water?', ('🙌', 'Dry your hands'), [('🎨', 'Use bright colours', 'Safety first!')], 'O2')]))

# ============================================================  6.3
s = U.section('6.3', 'Using conductors and insulators', ['O3']); s.words(V['6.3']); core(s, 'O3')
s.stop(PM('Why is the outside of a plug made of plastic?', ('🧴', 'Plastic is an insulator, so it keeps us safe'), [('🎨', 'Plastic is colourful', 'It is for safety.'), ('⚡', 'Plastic conducts', 'Plastic is an insulator.')], 'O3'),
       PM('Why are the pins of a plug made of metal?', ('🔩', 'So electricity can flow through them'), [('🧲', 'So they stick to magnets', 'They carry electricity.'), ('🎵', 'So they ring', 'They carry electricity.')], 'O3'))
s.stop(PM('Which part of a wire is the conductor?', ('🔩', 'The metal inside'), [('🧴', 'The plastic outside', 'The plastic is an insulator.')], 'O3'),
       PM('Which part of a wire keeps your hand safe?', ('🧴', 'The plastic outside'), [('🔩', 'The metal inside', 'The metal carries electricity.')], 'O3'))
s.prac(
 PM('Why do electricians wear rubber gloves?', ('🧤', 'Rubber is an insulator'), [('🧊', 'To keep their hands cold', 'It is for safety.'), ('🎨', 'To look smart', 'It is for safety.')], 'O3'),
 GD('Which part is a conductor and which is an insulator?', 'It is a', [('🔩 metal pins of a plug', 'conductor'), ('🧴 plastic case of a plug', 'insulator'), ('〰️ copper inside a wire', 'conductor'), ('🧤 rubber gloves', 'insulator')], o='O3'),
 PM('A pan has a metal bottom and a plastic handle. Why?', ('🍳', 'Metal carries heat to food; plastic keeps your hand cool'), [('🎨', 'It looks nice', 'It is about heat.'), ('⚖️', 'It is lighter', 'It is about heat.')], 'O3'),
 YN('Is rubber a good insulator?', True, 'O3', pic='🧤', why='Yes.'),
 MT('Match each word to what it means.', [('plug', 'goes into a socket'), ('rubber', 'soft insulator'), ('electrician', 'fixes electric things')], o='O3'),
 TK('Tick the insulators.', ['Insulator', 'Conductor'], [('plastic', ['✓', '✗']), ('rubber', ['✓', '✗']), ('copper', ['✗', '✓'])], o='O3'),
 PM('A wire\'s plastic cover is broken. What should you do?', ('🗣️', 'Tell an adult and do not touch it'), [('✋', 'Touch the metal to check', 'Never touch it.'), ('🔌', 'Plug it in anyway', 'It is dangerous.')], 'O3'),
 PM('Why are screwdrivers for electricians given plastic handles?', ('🧴', 'Plastic stops electricity reaching the hand'), [('🎨', 'They are pretty', 'It is for safety.'), ('⚡', 'Plastic conducts', 'Plastic insulates.')], 'O3'),
 YN('Should a torch case be made of an insulator?', True, 'O3', pic='🔦', why='Yes, so it is safe to hold.'),
 OD('Order a plug from the part that carries electricity to the part you hold.', ['metal pin', 'plastic case', 'your hand'], o='O3'),
 PM('Which material would you choose to carry electricity?', ('🔩', 'Copper metal'), [('🪵', 'Wood', 'Wood insulates.'), ('🧶', 'Wool', 'Wool insulates.')], 'O3'),
 PM('Electricians wear rubber boots. Why?', ('👢', 'Rubber stops electricity going through them to the ground'), [('🌧️', 'Only because it rains', 'Rubber insulates.'), ('🏃', 'To run faster', 'Rubber insulates.')], 'O3', d='H'),
)
s.adv(
 PM('* Advanced. Design a safe switch. What should the button be made of?', ('🧴', 'Plastic'), [('🔩', 'Bare metal', 'Your finger touches it.'), ('💧', 'Water', 'Water conducts.')], 'O3', d='H'),
 PM('* Advanced. Why is copper used inside wires and not iron?', ('〰️', 'Copper conducts electricity very well'), [('🧲', 'Iron is magnetic', 'Copper is the better conductor.'), ('🎨', 'Copper is orange', 'Copper conducts best.')], 'O3', d='VH'),
 GD('* Advanced. Label the torch parts.', 'It is a', [('🔋 battery contacts', 'conductor'), ('🔦 plastic case', 'insulator'), ('🔘 rubber button', 'insulator')], o='O3', d='H'),
)
s.labs('Design lab',
 sort_lab('Conductor or insulator part?', 'Sort each part of everyday things.', ['Conductor', 'Insulator'],
  [('metal plug pins', '🔌', 0, 'They carry electricity.'), ('plastic plug case', '🧴', 1, 'It keeps us safe.'), ('copper wire', '〰️', 0, 'It carries electricity.'), ('rubber gloves', '🧤', 1, 'They keep electricians safe.'), ('pan handle', '🍳', 1, 'It keeps your hand cool.')],
  [PM('Which part keeps us safe?', ('🧴', 'Plastic plug case'), [('🔌', 'Metal pins', 'They carry electricity.')], 'O3')]),
 home('Find conductors and insulators', 'Look at things at home (do not unplug anything).', ['an adult', 'paper and pencil'], ['Look only – do not touch plugs or sockets.'],
  ['Look at a plug on a lamp.', 'Look at a pan.', 'Look at a torch.'],
  ['Part', 'Conductor or insulator?'], [('plug pins', ['conductor', 'insulator']), ('pan handle', ['conductor', 'insulator']), ('torch case', ['conductor', 'insulator'])],
  [PM('Why are pan handles insulators?', ('✋', 'So your hand stays cool'), [('🍳', 'So food cooks faster', 'It protects your hand.')], 'O3')]))

# ============================================================  6.4
s = U.section('6.4', 'Switches', ['O4']); s.words(V['6.4']); core(s, 'O4')
s.stop(PM('When a switch is open, is the bulb on or off?', ('🌑', 'Off'), [('💡', 'On', 'An open switch makes a gap.')], 'O4'),
       PM('When a switch is closed, is the bulb on or off?', ('💡', 'On'), [('🌑', 'Off', 'A closed switch makes a complete loop.')], 'O4'))
s.stop(PM('What does a switch do when you turn the light off?', ('↔️', 'It makes a gap in the circuit'), [('🔋', 'It takes out the battery', 'It makes a gap.'), ('💥', 'It breaks the bulb', 'It makes a gap.')], 'O4'),
       PM('What does a switch do?', ('🔘', 'Turns a circuit on and off'), [('🎨', 'Changes the colour', 'It turns it on and off.'), ('🔊', 'Makes music', 'It turns it on and off.')], 'O4'))
s.prac(
 GD('On or off?', 'Bulb', [('🔗 switch closed, no gap', 'on'), ('✂️ switch open, a gap', 'off')], o='O4'),
 PM('Which of these has a switch?', ('🔦', 'A torch'), [('🍎', 'An apple', 'Torches have switches.'), ('🪨', 'A rock', 'Torches have switches.')], 'O4'),
 YN('Does a doorbell use a switch?', True, 'O4', pic='🔔', why='Yes! Pressing it closes the circuit.'),
 PM('Why should you turn off lights when you leave a room?', ('🌍', 'To save energy'), [('🌑', 'To make it scary', 'To save energy.'), ('🔊', 'To make noise', 'To save energy.')], 'O4'),
 MT('Match each word to what it means.', [('on', 'electricity flowing'), ('off', 'no electricity flowing'), ('gap', 'a space in the circuit')], o='O4'),
 OD('Order what happens when you press a light switch on.', ['press the switch', 'the gap closes', 'electricity flows', 'the light comes on'], o='O4'),
 TK('Tick what has a switch.', ['Has a switch', 'No switch'], [('a TV', ['✓', '✗']), ('a lamp', ['✓', '✗']), ('a spoon', ['✗', '✓'])], o='O4'),
 PM('A paper clip switch: the clip touches both pins. The bulb is…', ('💡', 'on'), [('🌑', 'off', 'The circuit is complete.')], 'O4'),
 YN('Can a switch be made from a paper clip?', True, 'O4', pic='📎', why='Yes – the metal clip closes the gap.'),
 PM('Why is the switch button usually plastic?', ('🧴', 'Plastic is an insulator – safe to touch'), [('🔩', 'Plastic conducts', 'Plastic insulates.'), ('🎵', 'It clicks', 'It is for safety.')], 'O4'),
 PM('Which saves the most energy?', ('🔘', 'Switching off things you are not using'), [('💡', 'Leaving everything on', 'That wastes energy.')], 'O4'),
 PM('In a circuit drawing, a switch with a gap means…', ('🌑', 'the circuit is off'), [('💡', 'the circuit is on', 'A gap means off.')], 'O4', d='H'),
)
s.adv(
 PM('* Advanced. Two switches are in one loop. Both must be closed. When does the bulb light?', ('💡', 'Only when both switches are closed'), [('🔘', 'When one is closed', 'Both must be closed.'), ('🌑', 'Never', 'When both are closed it lights.')], 'O4', d='VH'),
 PM('* Advanced. Why might a fridge light have a switch in the door?', ('🚪', 'The light turns on only when the door opens'), [('🧊', 'To keep the food cold', 'It is for the light.'), ('🔊', 'To beep', 'It is for the light.')], 'O4', d='H'),
 OD('* Advanced. Order what happens when you turn off a torch.', ['slide the switch', 'a gap opens', 'electricity stops', 'the bulb goes off'], o='O4', d='H'),
)
s.labs('Switch lab',
 sort_lab('Will the bulb light?', 'Sort each circuit.', ['Bulb on', 'Bulb off'],
  [('switch closed', '🔗', 0, 'No gap: on.'), ('switch open', '✂️', 1, 'A gap: off.'), ('clip touching both pins', '📎', 0, 'The gap is closed.'), ('clip swung away', '↔️', 1, 'There is a gap.'), ('battery missing', '🚫', 1, 'No battery: off.')],
  [PM('An open switch makes the bulb…', ('🌑', 'off'), [('💡', 'on', 'There is a gap.')], 'O4')]),
 home('Paper clip switch', 'Make a switch with an adult.', ['card', 'two drawing pins', 'a paper clip', 'a battery, bulb and wires', 'an adult'], ['An adult should push in the pins.'],
  ['Push two pins into card.', 'Join them into the circuit.', 'Hook the clip on one pin.', 'Swing it to touch the other pin.'],
  ['Clip', 'Bulb'], [('touching both pins', ['on', 'off']), ('swung away', ['on', 'off'])],
  [PM('Why does the paper clip work as a switch?', ('🔩', 'It is metal, so it conducts'), [('🧴', 'It is plastic', 'Paper clips are metal.')], 'O4')]))

# ============================================================  6.5
s = U.section('6.5', 'Changing the number of components', ['O5']); s.words(V['6.5']); core(s, 'O5')
s.stop(PM('What do we call the parts of a circuit?', ('🧩', 'Components'), [('🍽️', 'Dishes', 'They are components.'), ('🧸', 'Toys', 'They are components.')], 'O5'),
       PM('Which of these is a component?', ('🔔', 'A buzzer'), [('🍎', 'An apple', 'A buzzer is a component.'), ('🧦', 'A sock', 'A buzzer is a component.')], 'O5'))
s.stop(PM('What happens to the bulb if you add another battery?', ('🌟', 'It gets brighter'), [('🔅', 'It gets dimmer', 'More batteries: brighter.'), ('🔁', 'Nothing', 'It gets brighter.')], 'O5'),
       PM('What happens to a buzzer with more batteries?', ('🔊', 'It gets louder'), [('🔈', 'It gets quieter', 'More batteries: louder.'), ('🔇', 'It stops', 'It gets louder.')], 'O5'))
s.prac(
 PM('One battery, two bulbs. Compared with one bulb, each bulb is…', ('🔅', 'dimmer'), [('🌟', 'brighter', 'They share the energy.'), ('💥', 'broken', 'They are dimmer.')], 'O5'),
 GD('Brighter or dimmer?', 'Bulb is', [('🔋🔋 add a battery', 'brighter'), ('💡💡 add a bulb', 'dimmer'), ('🔋 take away a battery', 'dimmer')], o='O5'),
 YN('Can too many batteries burn out a bulb?', True, 'O5', pic='💥', why='Yes – it gets too hot.'),
 MT('Match each word to what it means.', [('component', 'a part of a circuit'), ('brighter', 'more light'), ('dimmer', 'less light')], o='O5'),
 OD('Order from dimmest to brightest bulb.', ['1 battery, 3 bulbs', '1 battery, 1 bulb', '2 batteries, 1 bulb'], o='O5'),
 TK('Tick the components.', ['Component', 'Not a component'], [('battery', ['✓', '✗']), ('bulb', ['✓', '✗']), ('pencil case', ['✗', '✓'])], o='O5'),
 PM('Which circuit has the loudest buzzer?', ('🔋', '2 batteries and 1 buzzer'), [('🔕', '1 battery and 1 buzzer', 'More batteries are louder.')], 'O5'),
 PM('Lily wants a brighter torch. What could she add?', ('🔋', 'Another battery'), [('💡', 'Another bulb', 'That makes it dimmer.'), ('🧦', 'A sock', 'Add a battery.')], 'O5'),
 YN('Does adding more bulbs (with the same battery) make each bulb brighter?', False, 'O5', pic='💡', why='No – each one gets dimmer.'),
 PM('Why do two bulbs on one battery look dimmer?', ('🤝', 'They share the battery\'s energy'), [('🌑', 'Bulbs hate sharing', 'They share energy.'), ('🎨', 'They change colour', 'They share energy.')], 'O5'),
 PM('What does a battery do in a circuit?', ('➡️', 'Pushes electricity round'), [('🛑', 'Stops electricity', 'It pushes it round.'), ('🎵', 'Plays music', 'It pushes it round.')], 'O5'),
 PM('Which change makes the buzzer quieter?', ('🔋', 'Taking away a battery'), [('🔋🔋', 'Adding a battery', 'That makes it louder.')], 'O5', d='H'),
)
s.adv(
 PM('* Advanced. 2 batteries and 2 bulbs. Compared with 1 battery and 1 bulb, the bulbs are…', ('⚖️', 'about the same brightness'), [('🌟', 'much brighter', 'More batteries but also more bulbs.'), ('🌑', 'off', 'They light.')], 'O5', d='VH'),
 PM('* Advanced. Why should you not use 10 batteries with one small bulb?', ('💥', 'The bulb could burn out'), [('🌟', 'It would be too beautiful', 'It could burn out.'), ('🔇', 'It would be quiet', 'It could burn out.')], 'O5', d='H'),
 OD('* Advanced. Order from quietest to loudest buzzer.', ['1 battery', '2 batteries', '3 batteries'], o='O5', d='H'),
)
s.labs('Brightness lab',
 test_lab('Brighter or dimmer?', 'Change the number of batteries with one bulb. Read the brightness (0 to 10).', 'Batteries', 'Brightness', 'points', 10, 1,
  'Tap the number the bar reaches.', [('1 battery', '🔋', 3), ('2 batteries', '🔋🔋', 6), ('3 batteries', '🔋🔋🔋', 9)],
  [PM('Which gave the brightest bulb?', ('🔋', '3 batteries'), [('🔋', '1 battery', 'It was the dimmest.')], 'O5')]),
 home('Brighter or dimmer at home', 'Test a circuit kit with an adult.', ['a circuit kit: batteries, bulbs, wires', 'an adult'], ['Use batteries only.'],
  ['Make a circuit with 1 battery and 1 bulb.', 'Add a battery.', 'Then add a bulb.'],
  ['Change', 'Bulb got'], [('added a battery', ['brighter', 'dimmer']), ('added a bulb', ['brighter', 'dimmer'])],
  [PM('Adding a bulb made each bulb…', ('🔅', 'dimmer'), [('🌟', 'brighter', 'They share the energy.')], 'O5')]))

U.mindmap(('Circuits', 'complete loop; conductors and insulators', 'O1', '6.1'), ('Safety', 'water conducts; mains is dangerous', 'O2', '6.2'),
          ('Using materials', 'metal pins, plastic cases, rubber gloves', 'O3', '6.3'), ('Switches', 'open = off, closed = on', 'O4', '6.4'), ('Components', 'more batteries brighter; more bulbs dimmer', 'O5', '6.5'))
