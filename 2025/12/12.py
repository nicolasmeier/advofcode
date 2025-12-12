import os
import sys
import re
import numpy as np
import math
import functools
from collections import Counter
import itertools
from z3 import *
# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x.replace("\n", "").strip()
    
li = []
with open("12.txt") as f:
    li = [trans(x) for x in f.readlines()]

shapes = dict()
shapes[0] = [li[1], li[2], li[3]]
shapes[1] = [li[6], li[7], li[8]]
shapes[2] = [li[11], li[12], li[13]]
shapes[3] = [li[16], li[17], li[18]]
shapes[4] = [li[21], li[22], li[23]]
shapes[5] = [li[26], li[27], li[28]]

res1 = 0
print(shapes)
for line in li[30:]:
    print(line)
    a, b = line.split(":")
    n,m = a.split("x")
    n = int(n.strip())
    m = int(m.strip())
    c = sum([int(x) for x in b.strip().split(" ")])
    print(n,m,c,n*m, c*8)
    if n * m >= c*9:
        res1 += 1

print(res1)
