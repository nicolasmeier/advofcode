import re
import numpy as np
import math
import functools
import collections 

import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("21.txt") as f:
    li = [x.strip() for x in f.readlines()]
#li = li[0]

#print(li)
player1pos = int(li[0].split()[-1])
player2pos = int(li[1].split()[-1])
p1s = 0
p2s = 0

#print(player1pos,player2pos)

_detdie = 0
isP1Turn = True
rolls = 0
while(max(p1s,p2s) < 1000):
    _detdie = _detdie %100 + 1
    a = _detdie
    _detdie = _detdie %100 + 1
    b = _detdie
    _detdie = _detdie %100 + 1
    c = _detdie
    rolls += 3
    if isP1Turn:
        isP1Turn = False
        player1pos = (player1pos + a + b + c -1) % 10 + 1
        p1s += player1pos
    else:
        isP1Turn = True
        player2pos = (player2pos + a + b + c -1) % 10 + 1
        p2s += player2pos

print(rolls,p1s,p2s)
print(rolls*p1s)
print(rolls*p2s)
