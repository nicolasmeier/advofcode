import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x
    
li = []
with open("02.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

save = 0
save2 = 0

for l in li:
    lvl = [int(x) for x in l.split(" ")]
    s = False
    ea = sum([1 for a,b in zip(lvl[:-1],lvl[1:]) if not (a < b <= a+3)])
    ed = sum([1 for a,b in zip(lvl[:-1],lvl[1:]) if not (a > b >= a-3)])
    if  (ea*ed) == 0:
        save += 1
        save2 += 1
        s = True
    else:
        for i in range(len(lvl)):
            nlvl = lvl[:i] + lvl[i+1:]
            nea = sum([1 for a,b in zip(nlvl[:-1],nlvl[1:]) if not (a < b <= a+3)])
            ned = sum([1 for a,b in zip(nlvl[:-1],nlvl[1:]) if not (a > b >= a-3)])
            if  (nea*ned) == 0:
                save2 += 1
                break

print(save)
print(save2)
