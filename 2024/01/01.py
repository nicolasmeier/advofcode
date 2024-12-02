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
with open("01.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

l1 = np.array([],dtype=int)
l2 = np.array([],dtype=int)
for l in li:
    a,_,b = l.split(" ",2)
    l1 = np.append(l1,int(a))
    l2 = np.append(l2,int(b))



l1 = np.sort(l1)
l2 = np.sort(l2)


r = np.abs(l1 - l2)

print(sum(r))

unique, counts = np.unique(l1, return_counts=True)
c1 = dict(zip(unique, counts))
unique, counts = np.unique(l2, return_counts=True)
c2 = dict(zip(unique, counts))

sum = 0
for i in range(max(max(l1),max(l2))):
    sum += i * c1.get(i,0) * c2.get(i,0)

print(sum)
