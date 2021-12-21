import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("09.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
#l = [int(x) for x in li[0].split(",")]
#li = li[0:3]
m = np.zeros((len(li),len(li[0])))
for i in range(len(li)):
    for j in range(len(li[i])):
        m[i][j] = (int)(li[i][j])

su = 0
c = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        n = i-1
        s = i+1
        e = j+1
        w = j-1

        x = m[i][j]

        nr,sr,er,wr = True,True,True,True
        if n >= 0:
            nr = x < m[n][j]
        if s < len(m):
            sr = x < m[s][j]
        if e < len(m[i]):
            er = x < m[i][e]
        if w >= 0:
            wr = x < m[i][w]
        
        if  nr and sr and wr and er:
            #print(x,i,j)
            c += 1
            su += x + 1
#print(m)
print((int)(su))

