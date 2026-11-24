# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 12 Measure (12.1 Mass, 12.2 Capacity, 12.3 Temperature).
Written by the Atomic teaching team."""
from kit import *
from h import *

U = Unit(12, "Measure", "Geometry and measure",
         "Measuring mass in grams and kilograms, capacity in millilitres and litres, and temperature in degrees Celsius, reading scales.",
         {"O1": {"code": "3Gm.04", "sec": "12.1", "codeNote": "", "t": "Estimate and measure mass in grams and kilograms, and read scales."},
          "O2": {"code": "3Gm.05", "sec": "12.2", "codeNote": "", "t": "Estimate and measure capacity in millilitres and litres."},
          "O3": {"code": "3Gm.06", "sec": "12.3", "codeNote": "", "t": "Read temperatures in degrees Celsius on a thermometer."}})
HEAVY = [("an apple", "g"), ("a bag of potatoes", "kg"), ("a pencil", "g"), ("a dog", "kg"), ("a letter", "g"), ("a bike", "kg")]

s = U.section("12.1", "Mass", ["O1"])
s.idea("Grams and kilograms", ["**Mass** tells us how heavy something is. Light things are measured in **grams (g)**; heavier things in **kilograms (kg)**.",
       "**1000 g = 1 kg**. Read the scale carefully: work out what each small mark is worth."], fig={"kind": "numline", "min": 0, "max": 5, "minor": 2, "ticks": [], "mark": 3.5})
s.check(N("How many grams are in 2 kg?", 2000, "g", units=["g"], o="O1"))
s.mistake("Half-way marks", ["If marks go 0, 1, 2 kg with a mark between each, that mark shows a half."])


def m1(r):
    v = r.randint(1, 9)
    return N("The arrow shows a mass on a kilogram scale. What is the mass?", v, "kg", units=["kg"], o="O1", fig={"kind": "numline", "min": 0, "max": 10, "ticks": [], "mark": v})
def m2(r):
    k = r.randint(1, 9)
    return N(f"How many grams are in {k} kg?", 1000 * k, "g", units=["g"], o="O1")
def m3(r):
    th, u = pick(r, HEAVY)
    return MC(f"Would you measure the mass of {th} in grams or kilograms?", u, ["kg" if u == "g" else "g"], o="O1")
def m4(r):
    a, b = r.randint(100, 500), r.randint(100, 400)
    return N(f"A bag of rice is {a} g and a bag of pasta is {b} g. What is the total mass?", a + b, "g", units=["g"], o="O1")
def m5(r):
    v = r.randint(1, 9) * 100
    return N("The scale goes up in 100 g. What mass does the arrow show?", v, "g", units=["g"], o="O1", fig={"kind": "numline", "min": 0, "max": 10, "ticks": [], "mark": v / 100}, hint="Each number on the scale is 100 g.")
def m6(r):
    ts = r.sample(HEAVY, 4)
    return GD("Choose the best unit for each mass.", "Unit", ts, o="O1", extra=["g", "kg"])
def m7(r):
    t, a = r.randint(2, 5) * 1000, r.randint(1, 9) * 100
    return N(f"A box weighs {t // 1000} kg. You take out {a} g. How many grams are left?", t - a, "g", units=["g"], o="O1", d="H")
def m8(r):
    xs = r.sample(range(100, 900, 50), 3); nm = ["box A", "box B", "box C"]; k = xs.index(max(xs))
    return S("The table shows three masses. Which box is heaviest?", [nm[k], nm[k].capitalize(), nm[k][-1]], o="O1", data={"head": ["Box", *nm], "rows": [["Mass (g)", *map(str, xs)]]})


s.std([m1, m8, m2, m3, m4, m6, m5, m7], EX("Explain how many grams are in 3 kg.", [("1 kg is 1000 g", "1000"), ("3 × 1000 = 3000 g", "3000")], "1 kilogram is 1000 grams, so 3 kg is 3 × 1000 = 3000 g.", o="O1"))

s = U.section("12.2", "Capacity", ["O2"])
s.idea("Millilitres and litres", ["**Capacity** is how much a container holds. Small amounts are measured in **millilitres (ml)**; larger amounts in **litres (l)**.",
       "**1000 ml = 1 l**. A spoon holds about 5 ml; a big bottle holds about 2 l."], fig={"kind": "numline", "min": 0, "max": 10, "ticks": [], "mark": 6})
s.check(N("How many millilitres are in 1 litre?", 1000, "ml", units=["ml"], o="O2"))
s.mistake("Read the top of the liquid", ["Read the level where the top of the water is, looking straight at it."])


def c1(r):
    v = r.randint(1, 9) * 100
    return N("The jug goes up in 100 ml. How much water does the arrow show?", v, "ml", units=["ml"], o="O2", fig={"kind": "numline", "min": 0, "max": 10, "ticks": [], "mark": v / 100})
def c2(r):
    l = r.randint(1, 9)
    return N(f"How many millilitres are in {l} litres?", 1000 * l, "ml", units=["ml"], o="O2")
def c3(r):
    a, b = r.randint(100, 500), r.randint(100, 400)
    return N(f"Lea pours {a} ml of juice and then {b} ml more. How much juice is that?", a + b, "ml", units=["ml"], o="O2")
def c4(r):
    ts = r.sample([("a teaspoon", "ml"), ("a bath", "l"), ("a cup", "ml"), ("a bucket", "l"), ("a fish tank", "l"), ("a medicine spoon", "ml")], 4)
    return GD("Choose the best unit for each capacity.", "Unit", ts, o="O2", extra=["ml", "l"])
def c5(r):
    t, a = 1000, r.randint(1, 9) * 100
    return N(f"A 1 litre bottle is full. {a} ml is poured out. How much is left?", t - a, "ml", units=["ml"], o="O2")
def c6(r):
    a, n = pick(r, [100, 200, 250]), r.randint(2, 5)
    return N(f"A glass holds {a} ml. How much do {n} glasses hold?", a * n, "ml", units=["ml"], o="O2")
def c7(r):
    a = pick(r, [100, 200, 250, 500])
    return N(f"How many {a} ml cups can be filled from a 1 litre jug?", 1000 // a, "cups", units=["cups"], o="O2", d="H")
def c8(r):
    xs = r.sample(range(200, 900, 100), 3)
    return TB("Complete the table.", ["Water in jug (ml)", "More needed to make 1 litre (ml)"], [[str(x), B(1000 - x)] for x in xs], o="O2", d="H")


s.std([c1, c8, c2, c3, c4, c5, c6, c7], EX("Explain why we measure a bath in litres, not millilitres.", [("a bath holds a lot of water", "a lot|lots|large|big"), ("litres are for larger amounts", "litre|larger|bigger")], "A bath holds a lot of water. Litres are used for large amounts, so the number is easier to use than thousands of millilitres.", o="O2"))

s = U.section("12.3", "Temperature", ["O3"])
s.idea("Degrees Celsius", ["**Temperature** tells us how hot or cold something is. We measure it in **degrees Celsius (°C)** with a **thermometer**.",
       "Water freezes at 0 °C and boils at 100 °C. A warm day might be 25 °C."], fig={"kind": "thermometer", "min": 0, "max": 50, "value": 25, "minor": 5, "major": 10})
s.check(N("What temperature does water freeze at?", 0, "°C", units=["°C"], o="O3"))
s.mistake("Count the marks", ["On a thermometer each mark might be 2 °C or 5 °C. Check before you read."])


def t1(r):
    v = r.randint(1, 9) * 5
    return N("What temperature does the thermometer show?", v, "°C", units=["°C"], o="O3", fig={"kind": "thermometer", "min": 0, "max": 50, "value": v, "minor": 5, "major": 10})
def t2(r):
    a, b = r.randint(10, 25), r.randint(2, 10)
    return N(f"It is {a} °C in the morning. It gets {b} degrees warmer. What is the temperature now?", a + b, "°C", units=["°C"], o="O3")
def t3(r):
    a, b = r.randint(15, 35), r.randint(2, 10)
    return N(f"It is {a} °C. It gets {b} degrees colder. What is the temperature now?", a - b, "°C", units=["°C"], o="O3")
def t4(r):
    xs = r.sample(range(5, 35), 4); cs = ["London", "Cairo", "Oslo", "Lima"]
    return OD("The table shows temperatures. Put the cities in order, coldest first.", [cs[i] for i in sorted(range(4), key=lambda k: xs[k])], o="O3", data={"head": ["City", *cs], "rows": [["°C", *map(str, xs)]]})
def t5(r):
    xs = r.sample(range(5, 35), 3); cs = ["Mon", "Tue", "Wed"]; i, j = sorted(range(3), key=lambda k: -xs[k])[:2]
    return N(f"How much warmer was {cs[i]} than {cs[j]}?", xs[i] - xs[j], "°C", units=["°C", "degrees"], o="O3", data={"head": ["Day", *cs], "rows": [["°C", *map(str, xs)]]})
def t6(r):
    return MC("Which is the best estimate for a hot drink?", "70 °C", ["7 °C", "0 °C", "200 °C"], o="O3")
def t7(r):
    ts = r.sample([("ice", "cold"), ("boiling water", "hot"), ("snow", "cold"), ("a hot oven", "hot"), ("a freezer", "cold"), ("soup on the stove", "hot")], 4)
    return GD("Is each one hot or cold?", "Hot or cold", ts, o="O3", extra=["hot", "cold"])
def t8(r):
    a = r.randint(2, 8)
    return N(f"The temperature rose by {a} °C every hour for 3 hours. It started at 10 °C. What is it now?", 10 + 3 * a, "°C", units=["°C"], o="O3", d="H")


s.std([t1, t4, t2, t3, t5, t6, t7, t8], EX("Explain how to read a thermometer.", [("look at the top of the red line / liquid", "top|line|level|liquid"), ("read the number on the scale next to it", "scale|number|marks")], "Find where the top of the coloured liquid is, then read the number on the scale next to it, counting the small marks.", o="O3"))

U.mindmap(("Mass", "g and kg • 1000 g = 1 kg", "O1", "12.1"), ("Capacity", "ml and l • 1000 ml = 1 l", "O2", "12.2"), ("Temperature", "°C • thermometers", "O3", "12.3"))
