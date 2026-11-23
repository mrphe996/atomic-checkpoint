# -*- coding: utf-8 -*-
"""Stage 3: the young-learner kit with stage 3 settings (media/s3, ids p3uNN). Written by the Atomic teaching team."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(HERE); sys.path.append(os.path.join(HERE, '..', 'primary4')); sys.path.append(os.path.join(HERE, '..', '..', '..', '..', 'build', 'p3'))
import kit34
kit34.setup(3)
from kit34 import *
TITLES = ['Plants are living things', 'Mixing materials', 'Light and shadows', 'Staying alive', 'Forces and magnets', 'The Earth and the Moon']
from vocab_all import V
core = core_for(V)
