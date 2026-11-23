# -*- coding: utf-8 -*-
"""Stage 4: the young-learner kit with stage 4 settings (media/s4, ids p4uNN). Written by the Atomic teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(HERE); sys.path.append(os.path.join(HERE, '..', '..', '..', '..', 'build', 'p4'))
import kit34
kit34.setup(4)
from kit34 import *
TITLES = ['Living things', 'Energy', 'Materials', 'Earth and its habitats', 'Light', 'Electricity']
from vocab_all import V
core = core_for(V)
