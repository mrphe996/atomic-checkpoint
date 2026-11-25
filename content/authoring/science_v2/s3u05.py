from science_v2.k import Unit
U = Unit("s3u05")
U.q("R", "5.1", "O1", 'Opening a drawer is a…', ('pull', 'You pull it towards you.'), [('push', 'You push to close it.'), ('twist', 'You do not twist a drawer.')], d="M")
U.q("P", "5.2", "O2", 'You drop a ball. Why does it fall?', ('Gravity pulls it down', 'Gravity pulls things towards the Earth.'), [('The air pushes it', 'Gravity pulls it.'), ('It wants to', 'Objects do not choose.')], d="M")
U.q("P", "5.3", "O3", 'A toy car rolls on carpet and on a smooth floor. Where does it go further?', ('On the smooth floor', 'Less friction lets it roll further.'), [('On the carpet', 'Carpet has more friction.'), ('The same distance', 'The surfaces are different.')], d="M")
U.q("P", "5.4", "O4", 'Two magnets are pushed together north to south. What happens?', ('They pull together (attract)', 'Opposite poles attract.'), [('They push apart', 'Like poles push apart.'), ('Nothing', 'Magnets push or pull each other.')], d="M")
U.q("E", "5.5", "O5", 'Sam says all metals stick to magnets. Is he right?', ('No – only some metals, like iron, are magnetic', 'Copper and aluminium are not magnetic.'), [('Yes', 'Many metals are not magnetic.'), ('No – no metals stick', 'Iron sticks to a magnet.')], d="M")
V2 = U.V2
