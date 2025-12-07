import os
import sys
import re
import numpy as np
import math
import functools
from collections import Counter
import itertools
# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x.replace("\n", "")
    
li = []
with open("07.txt") as f:
    li = [trans(x) for x in f.readlines()]

res1 = 0    
res2 = 0

start = (None,None)
beams = set()
splitters = set()

realsplits = set()

for y in range(len(li)):
    for x in range(len(li[y])):
        if li[y][x] == "S":
            start = (x,y)
        elif li[y][x] == "^":
            splitters.add((x,y))



def move_beam(pos):
    beams.add(pos)
    x,y = pos
    while True:
        y += 1
        if y >= len(li[y]):
            return
        elif (x,y) in beams:
            return
        elif (x,y) in splitters:
            realsplits.add((x,y))
            move_beam((x-1,y))
            move_beam((x+1,y))
            return
        beams.add((x,y))

move_beam(start)

@functools.lru_cache()
def move_beam2(pos):
    x,y = pos
    if y >= len(li[y]):
        return 1
    elif (x,y) in splitters:
        lb = move_beam2((x-1,y))
        rb = move_beam2((x+1,y))
        return lb + rb
    else:
        return move_beam2((x,y+1))

print("start:", start)
print("res1:", len(realsplits))
print("res2:", move_beam2(start))