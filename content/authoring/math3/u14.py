# -*- coding: utf-8 -*-
"""Stage 3 Mathematics (Primary) · Unit 14 Angles and movement (14.1 Angles and turns, 14.2 Direction, position and movement).
Upgraded lesson (v2): why each method works, paired examples that differ in one condition, prediction checks before the reveal,
and Practice built from decisions (test a claim, find all, spot the error, work backwards) rather than repeated routines.
Written by the Camday teaching team."""
from kit import *
from h import *

U = Unit(14, "Angles and Movement", "Geometry and measure",
         "Turns as angles, right angles and quarter, half and whole turns, compass directions, and describing position and movement on a grid.",
         {"O1": {"code": "3Gg.03", "sec": "14.1", "codeNote": "", "t": "Recognise angles as turns, including right angles, and compare angles with a right angle."},
          "O2": {"code": "3Gp.01", "sec": "14.2", "codeNote": "", "t": "Use compass directions and describe position and movement on a grid."}})
DIR = ["North", "East", "South", "West"]

s = U.section("14.1", "Angles and turns", ["O1"])
s.idea("Turning", ["An **angle** is an amount of turn. A **quarter turn** is a **right angle**. Two quarter turns make a **half turn**; four make a **whole turn**.",
       "Angles smaller than a right angle are **acute**; bigger ones (less than a half turn) are **obtuse**."], fig={"kind": "anglept", "line": True, "angles": [90, 90]})
s.check(N("How many right angles make a whole turn?", 4, "right angles", units=["right angles"], o="O1"))
s.check(MC('Before you read on: how many right angles make a full turn?', '4', [('2', '2 right angles make half a turn.'), ('3', '4 quarter turns make a full turn.')], o='O1'))
s.mistake("Clockwise", ["Clockwise means turning the same way as clock hands."])


def a1(r):
    n = r.randint(1, 4)
    w = {1: "quarter turn", 2: "half turn", 3: "three-quarter turn", 4: "whole turn"}[n]
    return N(f"How many right angles are in a {w}?", n, "right angles", units=["right angles"], o="O1")
def a2(r):
    a = pick(r, [30, 45, 60, 120, 135, 150])
    k = "smaller" if a < 90 else "bigger"
    return MC("Is the marked angle smaller or bigger than a right angle?", k, ["smaller" if k == "bigger" else "bigger", "the same"], o="O1", fig={"kind": "anglept", "line": True, "angles": [a, 180 - a], "labels": ["?", ""]})
def a3(r):
    h = pick(r, [3, 9])
    return MC(f"At {h} o'clock, what angle do the clock hands make?", "a right angle", ["a half turn", "no angle", "a whole turn"], o="O1", fig={"kind": "clock", "h": h, "m": 0})
def a4(r):
    k = r.randrange(4); n = r.randint(1, 3)
    return S(f"You face {DIR[k]} and make {n} quarter turn{'s' if n > 1 else ''} clockwise. Which way do you face now?", [DIR[(k + n) % 4]], o="O1")
def a5(r):
    ts = r.sample([("a corner of a book", "right angle"), ("a slice of pizza tip", "smaller than a right angle"), ("an open laptop leaning back", "bigger than a right angle"), ("the corner of a door", "right angle"), ("scissors opened a little", "smaller than a right angle")], 4)
    return GD("Compare each angle with a right angle.", "Angle", ts, o="O1", extra=["right angle", "smaller than a right angle", "bigger than a right angle"])
def a6(r):
    k = r.randrange(4)
    return S(f"You face {DIR[k]} and make a half turn. Which way do you face now?", [DIR[(k + 2) % 4]], o="O1")
def a7(r):
    n = r.randint(1, 3)
    return N(f"A robot makes {n} half turns. How many quarter turns is that?", 2 * n, "quarter turns", units=["quarter turns"], o="O1", d="H")
def a8(r):
    k = r.randrange(4)
    return S(f"You face {DIR[k]} and make a quarter turn anticlockwise. Which way do you face now?", [DIR[(k - 1) % 4]], o="O1", d="H")


s.std([a2, a3, a1, a4, a5, a6, a7, a8], EX("Explain how many right angles are in a half turn.", [("a half turn is two quarter turns", "two quarter|2 quarter"), ("each quarter turn is a right angle, so 2", "\\b2\\b|two right")], "A half turn is two quarter turns, and each quarter turn is a right angle. So a half turn is 2 right angles.", o="O1"))

s = U.section("14.2", "Direction, position and movement", ["O2"])
s.idea("Moving on a grid", ["The four **compass directions** are North, East, South and West.",
       "To describe movement on a grid say how many squares and which way: '3 squares East, then 2 squares North'."], fig=G([{"x": 1, "y": 1, "l": "A"}, {"x": 4, "y": 3, "l": "B"}], rng=6, lo=0))
s.check(S("Which direction is opposite to North?", ["South", "south"], o="O2"))
s.check(MC('Before you read on: you face north and make a half turn. Which way do you face?', 'South', [('East', 'That is a quarter turn clockwise.'), ('North', 'A half turn faces the opposite way.')], o='O2'))
s.mistake("Count squares, not lines", ["Count the jumps from one square to the next."])


def d1(r):
    x, y, dx, dy = r.randint(0, 3), r.randint(0, 3), r.randint(1, 3), r.randint(1, 3)
    return S(f"Start at A. Move {dx} squares East and {dy} squares North. Where do you end? Write it like (3, 2).", PP(x + dx, y + dy), o="O2", fig=G([{"x": x, "y": y, "l": "A"}], rng=6, lo=0))
def d2(r):
    x, y = r.randint(0, 2), r.randint(0, 2); dx, dy = r.randint(1, 4), r.randint(1, 4)
    return S("Describe the move from A to B, like 3 East 2 North.", [f"{dx} East {dy} North", f"{dx} east {dy} north", f"{dx} East, {dy} North", f"{dx} east, {dy} north", f"{dx} East and {dy} North"], o="O2", fig=G([{"x": x, "y": y, "l": "A"}, {"x": x + dx, "y": y + dy, "l": "B"}], rng=6, lo=0))
def d3(r):
    k = r.randrange(4)
    return S(f"Which direction is opposite to {DIR[k]}?", [DIR[(k + 2) % 4], DIR[(k + 2) % 4].lower()], o="O2")
def d4(r):
    k = r.randrange(4)
    return S(f"Which direction is a quarter turn clockwise from {DIR[k]}?", [DIR[(k + 1) % 4], DIR[(k + 1) % 4].lower()], o="O2")
def d5(r):
    a, b = r.randint(1, 5), r.randint(1, 5)
    return N(f"A robot moves {a} squares North, then {b} squares North. How many squares North has it moved?", a + b, "squares", units=["squares"], o="O2")
def d6(r):
    a, b = r.randint(4, 8), r.randint(1, 3)
    return N(f"A robot moves {a} squares East, then {b} squares West. How many squares East of the start is it?", a - b, "squares", units=["squares"], o="O2", d="H")
def d7(r):
    x, y = r.randint(0, 5), r.randint(0, 5)
    return MC("Which describes the position of point P?", f"({x}, {y})", [f"({y}, {x})" if x != y else f"({x + 1}, {y})", f"({x}, {y + 1})"], o="O2", fig=G([{"x": x, "y": y, "l": "P"}], rng=6, lo=0))
def d8(r):
    return OD("Put the directions in clockwise order, starting at North.", ["North", "East", "South", "West"], o="O2")


s.std([d1, d2, d3, d4, d5, d7, d6, d8], EX("Explain how to describe the way from your desk to the door on a grid.", [("say how many squares", "squares|number"), ("and which direction (N, E, S, W)", "north|east|south|west|direction")], "Count how many squares to move and say which direction, for example 4 squares North, then 2 squares East.", o="O2"))

U.mindmap(("Turns", "Quarter = right angle • half • whole", "O1", "14.1"), ("Directions", "North • East • South • West • grids", "O2", "14.2"))
