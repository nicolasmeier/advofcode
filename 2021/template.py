import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("05.txt") as f:
    l = [x.strip() for x in f.readlines()]
print(l)