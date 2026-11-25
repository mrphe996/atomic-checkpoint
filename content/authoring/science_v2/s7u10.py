from science_v2.k import Unit
U = Unit("s7u10")

U.q("P", "10.1", "O1", "A book rests on a table. Which statement is true?", ("Its weight is balanced by the push of the table", "Balanced forces mean it stays still."), [("No forces act on it", "Gravity still pulls it down."), ("Only gravity acts on it", "The table pushes up too.")])
U.q("P", "10.2", "O2", "A hammer and a feather are dropped together on the Moon, where there is no air. Which lands first?", ("They land together", "With no air resistance, gravity speeds them up equally."), [("The hammer", "On Earth air slows the feather; on the Moon there is no air."), ("The feather", "Nothing makes the feather faster.")])
U.q("E", "10.3", "O3", "Lia says 'I weigh 40 kg'. What should she say?", ("'My mass is 40 kg; my weight is about 400 N'", "Weight is a force measured in newtons."), [("'I weigh 40 N'", "That mixes the number for mass with the unit for weight."), ("Nothing – it is correct science", "In science weight is measured in N.")])
U.q("F", "10.4", "O4", "To test how parachute size affects falling time, what must stay the same?", ("The mass hung under the parachute and the drop height", "Only the size should change."), [("The size of the parachute", "That is what you change."), ("The falling time", "That is what you measure.")])
V2 = U.V2
