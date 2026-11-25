from science_v2.k import Unit
U = Unit("s8u13")

U.q("R", "13.1", "O1", "Which statement is about CLIMATE, not weather?", ("This region has hot, dry summers most years", "Climate is the pattern over many years."), [("It is raining today", "That is weather."), ("It will be windy tomorrow", "That is weather.")])
U.q("E", "13.1", "O2", "One winter is very cold. Kim says this proves the climate is not warming. What is wrong?", ("One season is weather; climate is about long-term averages", "A single cold winter does not show a trend."), [("Nothing", "Climate is measured over many years."), ("Cold winters cannot happen any more", "Cold winters still occur in a warming climate.")])
U.q("R", "13.2", "O3", "What has caused ice ages in Earth's past?", ("Natural changes such as changes in Earth's orbit", "These change how much sunlight reaches Earth."), [("Burning fossil fuels", "Ice ages happened long before humans."), ("Earthquakes", "Earthquakes do not cause ice ages.")])
U.q("P", "13.2", "O4", "If the amount of carbon dioxide in the atmosphere keeps rising, what is the likely effect?", ("Average global temperatures rise", "More greenhouse gas traps more heat."), [("Temperatures fall", "Carbon dioxide traps heat."), ("No effect", "It is a greenhouse gas.")])
V2 = U.V2
