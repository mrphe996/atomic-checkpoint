# -*- coding: utf-8 -*-
"""Science Stage 9 · Unit 11 Sound – Read the lesson (shown below the video) and the lesson document (PDF).
Camday's own text, examples and questions; scope: Cambridge Lower Secondary Science 0893, Stage 9 (9Ps.01, 9Ps.02)."""
from maths_notes_v4.kit4 import H, I, Y, X, K, L, W, BK, Ex, mcq, grid, num

READ = {}

# =====================================================================================================
# 11.1 Sound production · 9Ps.01
# =====================================================================================================
READ["11.1"] = L(
    H("Feel the sound",
      "Put your fingers lightly on your throat and hum. Then put your hand on a speaker playing loud music.",
      "What do you feel? What does that tell you about where sound comes from?"),
    I("How is sound produced?",
      "All sounds come from **vibrating** objects: a guitar string, a drum skin, your vocal cords, a speaker cone.",
      fig={"kind": "sciSound"},
      then=["As a speaker cone moves forward it squeezes air particles together – a **compression**. As it moves back it spreads them apart – a **rarefaction**.",
            "These travel outwards as a **sound wave**. The particles only vibrate back and forth; it is the **energy** that travels to your ear."]),
    I("Predict, watch, explain: a bell in a jar",
      "An electric bell rings inside a sealed glass jar while a pump removes the air.",
      then=["The ringing gets quieter and quieter until it can hardly be heard – although we can still see the hammer hitting the bell.",
            "Sound needs a **medium** (solid, liquid or gas) – particles to pass on the vibrations. In a **vacuum** there are no particles, so sound cannot travel. Space is silent."]),
    I("Data: the speed of sound in different materials",
      "Typical speeds of sound:",
      fig={"kind": "barchart", "labels": ["air", "water", "wood", "steel"], "values": [340, 1500, 3800, 5900], "ymax": 6000, "step": 1000, "ylabel": "speed (m/s)", "xlabel": "material"},
      then=["Sound is fastest in **solids**, slower in liquids and slowest in gases: closer particles pass on vibrations more quickly."]),
    Y("Sound and media",
      mcq("s9u11r11", "Why can astronauts on a spacewalk not hear each other without radios?",
          [("Space is a vacuum, with no particles to carry sound.", True, "Yes – sound needs a medium."), ("It is too cold for sound.", False, "Temperature is not the reason."),
           ("Their helmets block light.", False, "Light is not sound."), ("Sound is too slow in space.", False, "Sound cannot travel in space at all.")],
          "What does sound need to travel?", "Sound is passed on by particles; space has almost none.")),
    W("Echo distance",
      "A girl claps in front of a cliff and hears the echo 2 s later. Sound travels at 340 m/s in air. How far away is the cliff?",
      [("distance travelled = speed × time", "write the equation"), ("= 340 × 2 = 680 m", "there and back"), ("680 ÷ 2 = 340 m", "halve it: the sound went to the cliff and back")], "340 m"),
    K("Key points",
      "Sound is made by **vibrating** objects.",
      "A sound wave is a series of **compressions** and **rarefactions** passing through a medium.",
      "Sound cannot travel through a **vacuum**; it is fastest in solids and slowest in gases."),
    book=BK(
        [("vibration", "a quick back-and-forth movement"), ("compression", "a region where particles are squeezed together"), ("rarefaction", "a region where particles are spread apart"),
         ("medium", "the material a wave travels through"), ("vacuum", "a space with no particles")],
        [], [],
        [Ex("Describe how a drum produces a sound that reaches your ear.", ans="The skin vibrates, making compressions and rarefactions in the air that travel to the ear."),
         Ex("Explain what happens to the sound of the bell as air is pumped out of the jar.", ans="It fades: there are fewer particles to carry the vibrations."),
         Ex("Why does sound travel faster in steel than in air?", ans="The particles are much closer together, so they pass on vibrations faster."),
         Ex("A boy hears an echo from a wall 0.5 s after shouting. How far away is the wall? (speed 340 m/s)", ans="340 × 0.5 = 170 m there and back, so 85 m", think=True)],
        ["explain how sound is produced", "describe compressions and rarefactions", "explain why sound needs a medium"],
        look=["the bell in a jar", "the speed of sound chart"],
        note="Read it after the video: how sound is made and travels (answers at the back)."),
)

# =====================================================================================================
# 11.2 Sound waves and waveforms · 9Ps.01
# =====================================================================================================
READ["11.2"] = L(
    H("Seeing sound",
      "A microphone connected to an oscilloscope turns sound into a wavy line on a screen.",
      "What could the height and the spacing of the waves tell us about the sound?"),
    I("Parts of a waveform",
      "A waveform shows how the sound wave changes.",
      fig={"kind": "waves", "traces": [{"amp": 2, "cycles": 2}]},
      table=[["Part", "Meaning"], ["**crest**", "the highest point of the wave"], ["**trough**", "the lowest point"], ["**amplitude**", "the height from the middle line to a crest"],
             ["**wavelength**", "the distance from one crest to the next"], ["**frequency**", "the number of waves per second, in **hertz (Hz)**"]],
      then=["To draw a waveform: draw a middle (equilibrium) line, mark the amplitude above and below it, mark the length of one cycle, then draw a smooth curve through the crests and troughs."]),
    I("Loudness and pitch",
      "Compare these waveforms of the same note:",
      fig={"kind": "waves", "traces": [{"amp": 1, "cycles": 2, "label": "A"}, {"amp": 2.5, "cycles": 2, "label": "B"}, {"amp": 1, "cycles": 5, "label": "C"}]},
      then=["**Bigger amplitude → louder** sound (B is louder than A). Loudness is measured in **decibels (dB)**.",
            "**Higher frequency → higher pitch** (C is higher than A). Humans hear about **20 Hz to 20 000 Hz**."]),
    I("Data: how loud are everyday sounds?",
      "Typical sound levels:",
      fig={"kind": "barchart", "labels": ["whisper", "talking", "mower", "concert", "siren", "jet"], "values": [30, 60, 90, 105, 120, 140], "ymax": 150, "step": 30, "ylabel": "sound level (dB)", "xlabel": "sound"},
      then=["Long exposure above about **85 dB** can damage hearing; ear defenders and earplugs help."]),
    Y("Loudness or pitch?",
      grid("s9u11r21", "Which property of the wave changes?", ["Amplitude", "Frequency"],
           [("a song is turned up louder", "Amplitude"), ("a singer sings a higher note", "Frequency"), ("a guitar string is plucked harder", "Amplitude"), ("a shorter, tighter string is plucked", "Frequency")],
           "Loudness ↔ amplitude; pitch ↔ frequency.", "Louder = bigger amplitude; higher pitch = higher frequency.")),
    K("Key points",
      "Waveforms show **crest**, **trough**, **amplitude** and **wavelength**.",
      "Bigger **amplitude** → louder (dB). Higher **frequency** → higher pitch (Hz).",
      "Humans hear about 20–20 000 Hz; loud sounds can damage hearing."),
    book=BK(
        [("amplitude", "the height of a wave from the middle line"), ("wavelength", "the distance from one crest to the next"), ("frequency", "waves per second, in hertz"),
         ("pitch", "how high or low a sound is"), ("decibel (dB)", "the unit of loudness")],
        [], [],
        [Ex("Draw a waveform and label a crest, a trough, the amplitude and the wavelength.", ans="see the diagram in Key idea 1"),
         Ex("Two waveforms have the same frequency; one has double the amplitude. How do the sounds differ?", ans="Same pitch; the bigger-amplitude one is louder."),
         Ex("Which sounds in the chart could damage hearing with long exposure?", ans="mower, concert, siren, jet (over 85 dB)"),
         Ex("A dog whistle makes a 25 000 Hz sound. Why can dogs hear it but people cannot?", ans="It is above the human hearing range (20 000 Hz); dogs hear higher frequencies.", think=True)],
        ["label waveforms", "relate amplitude to loudness and frequency to pitch"],
        look=["the parts of a waveform", "waveforms A, B and C"],
        note="Read it after the video: waveforms, loudness and pitch (answers at the back)."),
)

# =====================================================================================================
# 11.4 Sound wave interference · 9Ps.02
# =====================================================================================================
READ["11.4"] = L(
    H("Silence from sound",
      "Noise-cancelling headphones make a plane cabin seem quiet – by playing extra sound.",
      "How could adding sound make things quieter?"),
    I("Interference",
      "When two sound waves meet, they combine – **interference**.",
      fig={"kind": "waves", "traces": [{"amp": 1.2, "cycles": 2, "label": "1"}, {"amp": 1.2, "cycles": 2, "label": "2"}, {"amp": 2.4, "cycles": 2, "label": "1+2"}]},
      then=["**Constructive interference**: crests meet crests (waves **in phase**). They add up to a bigger amplitude – a **louder** sound."]),
    I("Destructive interference",
      "If the crests of one wave meet the troughs of the other (**out of phase**), they cancel out – **destructive interference** – and the sound is quieter or silent.",
      then=["Noise-cancelling headphones use a microphone to record outside noise, then play the same wave **flipped** so it cancels the noise.",
            "In a hall, loud and quiet spots can form where waves from two speakers meet; sound engineers place speakers to avoid dead spots."]),
    Y("Interference",
      mcq("s9u11r41", "Two identical sound waves meet exactly out of phase. What do you hear?",
          [("almost nothing – they cancel", True, "Yes – destructive interference."), ("a sound twice as loud", False, "That is in phase."),
           ("a higher-pitched sound", False, "Interference changes amplitude, not frequency here."), ("an echo", False, "An echo is a reflection.")],
          "Crest meets trough.", "Out of phase → crests and troughs cancel → destructive interference.")),
    K("Key points",
      "Waves that meet **interfere**.",
      "In phase → **constructive** (louder); out of phase → **destructive** (quieter).",
      "Noise-cancelling headphones use destructive interference."),
    book=BK(
        [("interference", "waves combining when they meet"), ("constructive interference", "waves in phase add up to a bigger amplitude"),
         ("destructive interference", "waves out of phase cancel out")],
        [], [],
        [Ex("Describe the difference between constructive and destructive interference.", ans="Constructive: crests meet crests, louder. Destructive: crests meet troughs, quieter or silent."),
         Ex("Explain how noise-cancelling headphones work.", ans="They record the noise and play an out-of-phase copy that cancels it by destructive interference."),
         Ex("Quick quiz.", ("How is sound produced?", "by vibrating objects"), ("Why can't sound travel through space?", "no particles – a vacuum"),
            ("What decides how loud a sound is?", "its amplitude"), ("What decides the pitch?", "its frequency")),
         Ex("Walking across a hall with two speakers playing the same note, you hear it get loud, quiet, loud. Explain.", ans="In some places the waves arrive in phase (constructive), in others out of phase (destructive).", think=True)],
        ["describe constructive and destructive interference", "explain uses of interference"],
        look=["adding two waves"],
        note="Read it after the video: interference of sound waves, plus a quick quiz (answers at the back)."),
)
