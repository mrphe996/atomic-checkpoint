# -*- coding: utf-8 -*-
"""Helpers for the Science v2 reasoning questions (written by the Atomic teaching team).
Every question is an Atomic original; feedback explains why each wrong idea is wrong."""
from c_kit import mc, gd
ASN = ["Always true", "Sometimes true", "Never true"]
SKILL = {"P": "Prediction", "E": "Evaluation", "F": "Enquiry", "D": "Data", "R": "Reasoning"}
LEAD = {"P": "PREDICT: ", "E": "", "F": "", "D": "", "R": ""}


class Unit:
    def __init__(self, key): self.key, self.V2, self.n = key, {}, 0

    def _id(self, sec):
        self.n += 1; return f"v2_{self.key}_{sec.replace('.', '_')}_{self.n:02d}"

    def q(self, kind, sec, obj, prompt, right, wrongs, reason="", d="H"):
        """kind: P predict, E evaluate a claim/conclusion, F fair test / method, D data, R reasoning.
        right: (text, feedback); wrongs: [(text, why it is wrong), …]"""
        x = mc(self._id(sec), d, obj, LEAD[kind] + prompt, right, wrongs, reason=reason, skill=SKILL[kind])
        self.V2.setdefault(sec, []).append(x); return self

    def asn(self, sec, obj, prompt, rows, reason, d="H"):
        """always / sometimes / never: rows = [(statement, 'Always true'|'Sometimes true'|'Never true')]"""
        x = gd(self._id(sec), d, obj, prompt, ["Always / sometimes / never"], [(s, [a]) for s, a in rows], reason=reason, skill="Reasoning", extra=ASN)
        self.V2.setdefault(sec, []).append(x); return self
