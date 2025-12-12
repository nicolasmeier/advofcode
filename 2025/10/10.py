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
with open("10t.txt") as f:
    li = [trans(x) for x in f.readlines()]


for line in li:
    zlights,rest = line[1:].split("]")
    restl = rest.strip().split(" ")
    zbtn = restl[:-1]
    zjoltage = restl[-1]

    lights = [l == "#" for l in zlights]
    btn = [list(map(int,x[1:-1].split(","))) for x in zbtn]
    lb = [Bool("L"+str(i)) for i in range(len(lights))]

    

x = Int('x')
y = Int('y')
solve(x > 2, y < 10, x + 2*y == 7)

x = Int('x')
y = Int('y')
print (simplify(x + y + 2*x + 3))
print (simplify(x < y + x + 2))
print (simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))



