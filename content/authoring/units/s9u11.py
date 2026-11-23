# -*- coding: utf-8 -*-
"""Stage 9 Unit 11 – Sound. Written by the Atomic teaching team."""
from c_kit2 import Unit, B

STRAND = "Physics"
BLURB = "How vibrations make sound, why sound needs a medium, reading waveforms for amplitude, wavelength and frequency, loudness and pitch, and how sound waves interfere."
OBJECTIVES = {
    "O1": {"sec": "11.1", "code": "9Ps.01", "codeNote": "sound production", "t": "Describe how vibrating objects produce sound as compressions and rarefactions that travel through a medium."},
    "O2": {"sec": "11.2", "code": "9Ps.01", "codeNote": "", "t": "Identify crest, trough, amplitude and wavelength on a waveform and draw waveforms."},
    "O3": {"sec": "11.2", "code": "9Ps.01", "codeNote": "loudness and pitch", "t": "Relate amplitude to loudness and frequency to pitch."},
    "O4": {"sec": "11.4", "code": "9Ps.02", "codeNote": "", "t": "Describe constructive and destructive interference of sound waves and their uses."},
}
SECTIONS = [
    {"id": "11.1", "title": "Sound production", "objs": ["O1"]},
    {"id": "11.2", "title": "Sound waves and waveforms", "objs": ["O2", "O3"]},
    {"id": "11.4", "title": "Sound wave interference", "objs": ["O4"]},
]
u = Unit(9, 11)

def mcs(kind, rows):
    for r in rows:
        p, right, wrongs = r[:3]; o = r[3] if len(r) > 3 else None
        u.mc(kind, p, right, wrongs, o=o)

# ---------------------------------------------------------------- 11.1
u.sec("11.1", "O1")
u.gd("r", "What vibrates to make each sound?", "Vibrating part", [("Guitar", "String"), ("Drum", "Membrane"), ("Saxophone", "Reed"), ("Human voice", "Vocal cords")])
u.od("r", "Order the media from fastest to slowest for sound.", ["Solid", "Liquid", "Gas"])
u.tb("r", "Speed of sound. Complete the time to travel 1500 m.", ["Medium", "Speed (m/s)", "Time for 1500 m (s)"], [["Water", "1500", B(1)], ["Air", "300", B(5)]])
u.ex("r", "Explain why there is no sound in space.", [("sound needs a medium / particles", ["medium|particle"]), ("space is a vacuum – no particles", ["vacuum|no particles|empty"]), ("vibrations cannot be passed on", ["vibrat|pass|travel"])],
     "Sound is vibrations passed from particle to particle, so it needs a medium. Space is a vacuum with no particles, so the vibrations cannot be passed on.")
u.mc("r", "All sounds come from…", "vibrating objects", ["light", "magnets", "heat only"])
u.mc("r", "A region where air particles are squeezed together is a…", "compression", ["rarefaction", "crest", "vacuum"])
u.mc("r", "Why does sound travel fastest in solids?", "The particles are closest together", ["Solids are hottest", "Solids have no particles", "Solids are lightest"], d="H")
u.mc("r", "A sound wave carries … from the source to your ear.", "energy", ["air particles all the way", "light", "mass"], d="VH")
mcs("p", [
    ("Another word for vibrating is…", "oscillating", ["reflecting", "conducting", "radiating"]),
    ("A region where air particles are spread apart is a…", "rarefaction", ["compression", "crest", "medium"]),
    ("A speaker cone moving forward makes a…", "compression", ["rarefaction", "vacuum", "trough"]),
    ("Sound cannot travel through a…", "vacuum", ["solid", "liquid", "gas"]),
    ("Sound travels slowest in…", "gases", ["solids", "liquids", "metals"]),
    ("Space is silent because it is…", "a vacuum", ["too cold", "too dark", "too big"]),
    ("Your voice is made by your…", "vocal cords", ["lungs alone", "teeth", "ears"]),
    ("A drum makes sound when its … vibrates.", "membrane", ["stick", "frame", "floor"]),
    ("Sound reaches your ear as a…", "wave", ["particle stream from the source", "beam of light", "magnet"]),
    ("A medium is…", "a substance sound travels through", ["a vacuum", "a type of light", "a loudness scale"]),
    ("Putting your ear to a table lets you hear tapping clearly because…", "sound travels well through solids", ["solids block sound", "air is a vacuum", "tables amplify light"]),
    ("Whales can communicate over long distances because sound travels well in…", "water", ["a vacuum", "space", "ice only"]),
    ("Particles in a sound wave…", "vibrate back and forth", ["travel all the way to the ear", "stay still", "disappear"]),
    ("Astronauts on a spacewalk talk using…", "radios", ["shouting", "drums", "whistles"]),
    ("If a bell rings in a jar as the air is pumped out, the sound…", "gets quieter", ["gets louder", "stays the same", "gets higher"]),
])
u.mt("p", "Match the term to its meaning.", [("Compression", "particles squeezed together"), ("Rarefaction", "particles spread apart"), ("Medium", "substance sound travels through")])
u.ms("p", "Select ALL the media sound can travel through.", ["Steel", "Water", "Air"], ["A vacuum", "Empty space"])
u.gd("p", "Can sound travel here?", "Answer", [("Through a wall", "Yes"), ("Across empty space", "No"), ("Underwater", "Yes")])
u.ex("a", "Describe what you would hear as air is pumped out of a bell jar containing a ringing bell, and explain.", [("sound gets quieter", ["quieter|fainter|fades"]), ("fewer particles to carry vibrations", ["fewer particles|less air"]), ("silent when vacuum", ["vacuum|silent|no sound"])],
     "The sound gets quieter and quieter, because there are fewer air particles to pass on the vibrations. When nearly all the air is removed, there is almost no sound.")
u.nm("a", "Thunder is heard 6 s after lightning. Sound travels at 340 m/s. How far away is the storm?", 2040, "m")
u.mc("a", "Why do you see a firework before you hear it?", "Light travels much faster than sound", ["Sound travels faster than light", "Fireworks are silent at first", "Your ears are slower"], skill="Reasoning")
u.mc("a", "Why do Native American trackers put their ear to the ground to hear distant horses?", "Sound travels faster and further through the solid ground", ["The ground is a vacuum", "Air blocks sound completely", "Horses make no sound in air"], skill="Reasoning")
u.stop("and how do they reach your ears?", "Which sounds are low?", "A bass drum", ["A bird singing", "A whistle", "A violin's top note"])
u.stop("and a speaker cone all vibrate", "All sounds come from…", "vibrating objects", ["light", "magnets", "heat"])
u.stop("passing energy from particle to particle to your ear", "When a speaker cone moves forward it makes a…", "compression", ["rarefaction", "vacuum", "trough"])
u.stop("Space is silent!", "Sound travels fastest in…", "solids", ["gases", "liquids", "a vacuum"])

# ---------------------------------------------------------------- 11.2
u.sec("11.2", "O2")
u.gd("r", "Label the waveform.", "Part", [("Highest point", "Crest"), ("Lowest point", "Trough"), ("Height from equilibrium to crest", "Amplitude"), ("Length of one cycle", "Wavelength")])
u.gd("r", "Louder/quieter, higher/lower? Compare wave B with wave A.", "Sound of B", [("B has a bigger amplitude", "Louder"), ("B has a higher frequency", "Higher pitch"), ("B has a smaller amplitude", "Quieter")], o="O3")
u.tb("r", "Complete the frequency (waves per second).", ["Waves", "Time (s)", "Frequency (Hz)"], [["500", "1", B(500)], ["600", "2", B(300)]], o="O3")
u.ex("r", "Compare the sound of a violin and a bass guitar using frequency and pitch.", [("violin higher frequency", ["violin.*(higher|high)"]), ("violin higher pitch / bass lower pitch", ["pitch"]), ("frequency = waves per second, Hz", ["hertz|hz|per second"])],
     "A violin produces sound waves with a higher frequency (more waves per second, in hertz) than a bass guitar, so it has a higher pitch; the bass guitar sounds low.", o="O3")
u.mc("r", "An oscilloscope shows sound as a…", "waveform", ["colour", "number only", "magnet"])
u.mc("r", "A bigger amplitude means a sound is…", "louder", ["quieter", "higher", "lower"], o="O3")
u.mc("r", "Humans can hear frequencies from about…", "20 Hz to 20 000 Hz", ["2 Hz to 200 Hz", "200 Hz to 2 million Hz", "0 Hz to 20 Hz"], o="O3", d="H")
u.mc("r", "A waveform's crests get closer together on the screen (same time scale). The sound…", "has a higher pitch", ["is louder", "is quieter", "has a lower pitch"], o="O3", d="VH")
mcs("p", [
    ("Frequency is measured in…", "hertz", ["decibels", "metres", "volts"], "O3"),
    ("Loudness is measured in…", "decibels", ["hertz", "metres", "joules"], "O3"),
    ("Frequency is the number of waves per…", "second", ["metre", "minute always", "hour"], "O3"),
    ("Higher frequency means…", "higher pitch", ["lower pitch", "louder", "quieter"], "O3"),
    ("A bass guitar has a … pitch.", "low", ["high", "silent", "very loud only"], "O3"),
    ("A larger amplitude means the sound carries more…", "energy", ["pitch", "frequency", "wavelength"], "O3"),
    ("Too much noise can cause…", "hearing loss and stress", ["better hearing", "higher pitch", "lower frequency"], "O3"),
    ("Rustling leaves are … on the decibel scale.", "low", ["very high", "above a jet", "the loudest"], "O3"),
    ("The middle line of a waveform is the…", "equilibrium line", ["crest", "amplitude", "trough"]),
    ("Amplitude is measured from the equilibrium line to the…", "crest", ["trough below", "next crest", "end of the screen"]),
    ("Wavelength is the length of…", "one cycle", ["the whole screen", "half a crest", "the amplitude"]),
    ("When drawing a waveform, you should first…", "label the axes", ["draw the curve", "colour it", "guess the amplitude"]),
    ("The waveform curve should be…", "smooth", ["jagged", "straight", "dotted"]),
    ("Sounds above 20 000 Hz are called…", "ultrasound", ["infrasound", "decibels", "echoes"], "O3"),
    ("Dogs can hear … frequencies than humans.", "higher", ["no", "only lower", "exactly the same"], "O3"),
])
u.mt("p", "Match the quantity to its unit.", [("Frequency", "hertz"), ("Loudness", "decibels"), ("Wavelength", "metres")])
u.od("p", "Order these sounds from quietest to loudest.", ["Rustling leaves", "Normal conversation", "Busy traffic", "Jet taking off"], o="O3")
u.ms("p", "Select ALL that make a sound louder.", ["Bigger amplitude", "Hitting a drum harder"], ["Higher frequency only", "Smaller amplitude", "Shorter wavelength only"], o="O3")
u.ex("a", "Sketch-describe how the waveform changes when a guitar string is plucked harder and then tightened.", [("plucked harder – bigger amplitude, louder", ["amplitude|taller|louder"]), ("tightened – higher frequency, waves closer", ["frequency|closer|more waves"]), ("higher pitch", ["pitch"])],
     "Plucking harder gives taller waves (bigger amplitude), so the sound is louder. Tightening the string gives more waves per second (higher frequency), so they are closer together on the screen and the pitch is higher.", o="O3")
u.nm("a", "A wave makes 1760 complete cycles in 4 seconds. What is its frequency?", 440, "Hz", o="O3")
u.mc("a", "Why do workers using jackhammers wear ear defenders?", "Loud, high-amplitude sounds can damage hearing", ["The sound has a low pitch", "Jackhammers are silent", "Ear defenders raise the pitch"], o="O3", skill="Reasoning")
u.mc("a", "On an oscilloscope, a trace has amplitude 2 squares and 4 waves on screen. The new trace has amplitude 2 squares and 8 waves. The new sound is…", "the same loudness but higher pitch", ["louder and higher", "quieter and lower", "the same in every way"], o="O3", skill="Data")
u.stop("the length of one cycle", "The highest point of a wave is the…", "crest", ["trough", "amplitude", "wavelength"])
u.stop("Too much noise can cause stress and hearing loss", "A bigger amplitude makes a sound…", "louder", ["higher", "quieter", "lower"], o="O3")
u.stop("Humans hear from about 20 to 20 thousand hertz", "Higher frequency means…", "higher pitch", ["louder", "lower pitch", "quieter"], o="O3")

# ---------------------------------------------------------------- 11.4
u.sec("11.4", "O4")
u.gd("r", "Constructive or destructive interference?", "Type", [("Crests meet crests", "Constructive"), ("Crests meet troughs", "Destructive"), ("Sound gets louder", "Constructive"), ("Sound cancels out", "Destructive")])
u.tb("r", "Two waves meet in phase. Complete the result.", ["Wave 1 amplitude", "Wave 2 amplitude", "Combined amplitude"], [["2", "3", B(5)], ["4", "4", B(8)]])
u.gd("r", "Which use matches each type of interference?", "Use", [("Constructive", "Some hearing aids"), ("Destructive", "Noise-cancelling headphones")], extra=["Microscopes"])
u.ex("r", "Explain how noise-cancelling headphones work.", [("microphone records outside noise", ["record|microphone|detect"]), ("play reversed / out-of-phase sound", ["revers|out of phase|opposite"]), ("destructive interference cancels noise", ["destructive|cancel"])],
     "A microphone records the outside noise. The headphones play the same sound reversed, out of phase, so crests meet troughs and destructive interference cancels the noise.")
u.mc("r", "When two sound waves meet, they…", "interfere", ["stop forever", "turn into light", "reflect only"])
u.mc("r", "Waves are in phase when…", "crests line up with crests", ["crests meet troughs", "they have different frequencies", "one is silent"])
u.mc("r", "Two identical waves meet exactly out of phase. What do you hear?", "Silence or near-silence", ["Twice as loud", "Higher pitch", "An echo"], d="H")
u.mc("r", "Why are noise-cancelling headphones useful on aeroplanes?", "They cancel the steady engine noise, so less volume is needed", ["They make the engine quieter", "They block all light", "They raise the pitch"], d="VH")
mcs("p", [
    ("Constructive interference makes sound…", "louder", ["quieter", "higher", "slower"]),
    ("Destructive interference makes sound…", "quieter", ["louder", "higher", "faster"]),
    ("Out of phase means…", "crests meet troughs", ["crests meet crests", "same amplitude", "same time"]),
    ("In constructive interference, amplitudes…", "add together", ["cancel out", "halve", "stay the same"]),
    ("In destructive interference, waves…", "cancel out", ["add together", "speed up", "change colour"]),
    ("Noise-cancelling headphones use … interference.", "destructive", ["constructive", "magnetic", "no"]),
    ("Some hearing aids use … interference.", "constructive", ["destructive", "magnetic", "no"]),
    ("Noise-cancelling headphones play outside noise…", "reversed", ["louder", "slower", "unchanged"]),
    ("In a hall with two speakers, some seats sound quieter because of…", "destructive interference", ["constructive interference", "echoes only", "the vacuum"]),
    ("Waves that are in phase…", "reinforce each other", ["cancel each other", "change frequency", "stop"]),
    ("Interference happens when two waves…", "overlap", ["are far apart", "never meet", "are in a vacuum only"]),
    ("A crest meeting a trough of equal size gives…", "zero amplitude", ["double amplitude", "higher frequency", "a louder sound"]),
    ("Engineers use interference in…", "concert hall design", ["baking", "painting", "photosynthesis"]),
    ("If two waves of amplitude 3 and 1 meet out of phase, the result has amplitude…", "2", ["4", "3", "0"]),
    ("Interference is a property of…", "waves", ["solids only", "magnets only", "particles at rest"]),
])
u.mt("p", "Match the description to the type.", [("In phase", "constructive"), ("Out of phase", "destructive"), ("Amplitudes add", "constructive")])
u.od("p", "Order how noise-cancelling headphones work.", ["Microphone picks up outside noise", "Circuit makes the reversed wave", "Speaker plays the reversed wave", "Waves cancel by destructive interference"])
u.ms("p", "Select ALL the results of constructive interference.", ["Bigger amplitude", "Louder sound"], ["Silence", "Smaller amplitude", "Lower frequency"])
u.ex("a", "A student walks in front of two speakers playing the same note and hears it get loud, quiet, loud. Explain.", [("waves from both speakers overlap / interfere", ["interfer|overlap"]), ("loud: in phase, constructive", ["in phase|constructive"]), ("quiet: out of phase, destructive", ["out of phase|destructive"])],
     "The waves from the two speakers overlap and interfere. Where they arrive in phase, constructive interference makes it loud; where they arrive out of phase, destructive interference makes it quiet.")
u.nm("a", "A wave of amplitude 5 meets a wave of amplitude 2 exactly out of phase. What is the resulting amplitude?", 3, "units")
u.mc("a", "Why can't noise-cancelling headphones cancel sudden, unpredictable noises as well as steady hums?", "The circuit needs time to detect and reverse the wave", ["Sudden noises are not waves", "They only work on high pitches", "Steady hums are silent"], skill="Reasoning")
u.mc("a", "Why might a concert hall designer avoid two speakers in positions that cause destructive interference?", "Some seats would hear the music too quietly", ["The music would be too loud everywhere", "The pitch would rise", "The speakers would overheat"], skill="Application")
u.stop("used in some hearing aids", "When crests line up with crests, interference is…", "constructive", ["destructive", "magnetic", "zero"])
u.stop("play it back to cancel the noise", "Noise-cancelling headphones use … interference.", "destructive", ["constructive", "no", "light"])

SECTIONS, POOLS, STOPS = u.export(SECTIONS)

MINDMAP = {"id": "root", "t": "Sound", "sec": None, "kids": [
    {"id": "pr", "t": "Production", "d": "Vibrations • Compressions and rarefactions • Energy passed on", "obj": "O1", "sec": "11.1"},
    {"id": "md", "t": "Medium", "d": "Fastest in solids • Slowest in gases • No sound in a vacuum", "obj": "O1", "sec": "11.1"},
    {"id": "wf", "t": "Waveforms", "d": "Crest • Trough • Amplitude • Wavelength", "obj": "O2", "sec": "11.2"},
    {"id": "lp", "t": "Loudness and pitch", "d": "Amplitude → loudness (dB) • Frequency → pitch (Hz) • 20–20 000 Hz", "obj": "O3", "sec": "11.2"},
    {"id": "in", "t": "Interference", "d": "In phase: constructive, louder • Out of phase: destructive, cancels", "obj": "O4", "sec": "11.4"},
]}
