import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("08.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
#l = [int(x) for x in li[0].split(",")]
#li = li[0:3]

for l in li:
    print(l)