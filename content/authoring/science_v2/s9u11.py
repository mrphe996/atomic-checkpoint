from science_v2.k import Unit
U = Unit("s9u11")

U.q("R", "11.1", "O1", "All sounds are produced by…", ("vibrations", "A vibrating object makes the particles around it vibrate."), [("light", "Light does not make sound."), ("magnetism", "Sounds come from vibrations.")])
U.q("P", "11.2", "O2", "A guitar string is plucked harder. What changes in the waveform?", ("The amplitude increases (it is louder)", "Harder plucking gives bigger vibrations."), [("The frequency increases", "Pitch stays about the same."), ("Nothing", "The loudness changes.")])
U.q("R", "11.2", "O3", "A sound wave has more waves per second. What do you hear?", ("A higher pitch", "Higher frequency means higher pitch."), [("A louder sound", "Loudness depends on amplitude."), ("A quieter sound", "Frequency changes pitch.")])
U.q("P", "11.4", "O4", "Two identical sound waves meet exactly out of step (peak meets trough). What is heard?", ("Very quiet sound or silence", "The waves cancel out (destructive interference)."), [("A sound twice as loud", "That happens when they meet in step."), ("A higher pitch", "Interference changes loudness, not pitch.")])
V2 = U.V2
