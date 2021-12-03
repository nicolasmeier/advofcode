import os
import sys
import re
import numpy as np
import math
import functools
from itertools import groupby
os.chdir(os.path.dirname(sys.argv[0]))
lines = []
with open("15.txt") as f:
    lines = [x.strip() for x in f.readlines()]
#l = l[0]
sec = 2504


for l in lines:
    print(l.split())
