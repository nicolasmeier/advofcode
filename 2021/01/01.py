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
    l = [int(x.strip()) for x in f.readlines()]
#l = l[0]
#print(l)
n=0
m = 0
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        n += 1
for i in range(len(l)-3):
    if (l[i] + l[i+1] +l[i+2]) < (l[i+1] +l[i+2] +l[i+3]):
        m += 1

print(n)
print(m)