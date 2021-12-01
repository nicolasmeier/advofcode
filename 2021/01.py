import os
import sys
import re
import numpy as np
import math
import functools
from itertools import groupby
os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("01.txt") as f:
    l = [x.strip() for x in f.readlines()]
#l = l[0]
#print(l)

for i in l:
    print(i)