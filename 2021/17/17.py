import re
import numpy as np
import math
import functools
import collections 

import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("17.txt") as f:
    li = [x.strip() for x in f.readlines()]
li = li[0]

print(li)
beg, end = [x for x in li.split(",")]
xes = [x for x in beg.split("=")][1]
yes = [y for y in end.split("=")][1]
xstart, xend = [int(x) for x in xes.split("..")]
ystart, yend = [int(y) for y in yes.split("..")]


x,y = 0,0
def doStep(posx,posy,xvel,yvel,step=0,maxy=0):
    maxy = max(posy,maxy)
    print(posx,posy)
    if step > 1000:
        return [False,0]
    if xstart <= posx <= xend:
        if ystart <= posy <= yend or ystart >= posy >= yend:
            return [True,maxy]
    #The probe's x position increases by its x velocity.
    posx += xvel
    #The probe's y position increases by its y velocity.
    posy += yvel
    #Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    if xvel > 0:
        xvel -= 1
    elif xvel < 0:
        posx += 1
    #Due to gravity, the probe's y velocity decreases by 1.
    yvel -= 1
    return doStep(posx,posy,xvel,yvel,step + 1,maxy)


for a in range(101):
    for b in range(101):
        print(a,b,doStep(0,0,a,b))