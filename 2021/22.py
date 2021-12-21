import numpy as np
import math
import functools
import collections 
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("22.txt") as f:
    li = [x.strip() for x in f.readlines()]
#li = li[0]

print(li)
