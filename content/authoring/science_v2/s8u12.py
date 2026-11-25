from science_v2.k import Unit
U = Unit("s8u12")

U.q("R", "12.1", "O1", "Which uses an energy resource that will not run out?", ("A wind turbine", "Wind is renewable."), [("A coal power station", "Coal is non-renewable."), ("A gas boiler", "Natural gas is non-renewable.")])
U.q("E", "12.2", "O2", "Pat says fossil fuels are fine because there is plenty left. Which is the best reply?", ("They will run out, and burning them adds carbon dioxide to the air", "Both are good reasons to reduce their use."), [("He is right", "They are finite."), ("Fossil fuels are renewable", "They take millions of years to form.")])
U.q("E", "12.3", "O3", "Why might a country not rely only on solar power?", ("It produces no electricity at night and less when cloudy", "A mix of resources gives a steady supply."), [("Solar power is non-renewable", "It is renewable."), ("Solar panels pollute the air when running", "They do not burn fuel.")])
V2 = U.V2
