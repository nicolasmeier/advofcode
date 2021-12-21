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

def getPos(p,x):
    return (p + x -1) % 10 + 1

_detdie = 0
isP1Turn = True
rolls = 0

@functools.lru_cache()
def play(p1s,p2s,player1pos,player2pos,isP1Turn):
    p1w,p2w = 0,0
    if (max(p1s,p2s) < 21):
        if isP1Turn:
            for x in [3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9]:
                y = getPos(player1pos,x)
                w1,w2 = play(p1s + y,p2s,y,player2pos,not isP1Turn)
                p1w += w1
                p2w += w2
        else:
            for x in [3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9]:
                y = getPos(player2pos,x)
                w1,w2 = play(p1s,p2s + y,player1pos,y,not isP1Turn)
                p1w += w1
                p2w += w2
    return (p1w,p2w)
        


x,y = play(0,0,player1pos,player2pos,True)
print(x,y)
print(x*y)