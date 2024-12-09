import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x:str):
    return list(map(int,[y for y in x]))
    
li = []
with open("09.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]


d = li[0]

b = list()
b2 = list()
empty = False
iii = 0
for m in d:
    if empty:
        b2.append(('.',m))
        for _ in range(m):
            b.append('.')
    else:
        b2.append((str(iii),m))
        for _ in range(m):
            b.append(str(iii))
        iii += 1
    empty = not empty



for i,slot in enumerate(b):
    if slot == '.':
        x = b.pop()
        while x == '.':
            x = b.pop()
        b[i] = x
    
part1 = 0
for i,slot in enumerate(b):
    part1 += i * int(slot)

print(f"Part1= {part1}")


for i,slot in enumerate(b2):
    k,a = slot
    if k == '.':
        pass