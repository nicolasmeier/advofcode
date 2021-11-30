import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("08.txt") as f:
    l = [x.strip() for x in f.readlines()]

lx = ['""','"abc"','"aaa\\"aaa"','"\\x27"']

r = 0
a = 0
b = 0
m = 0
n = 0
for i in l:
    y = i.encode('utf-8').decode('unicode_escape')
    #print(i, len(i), len(y[1:1]))
    e = i.replace('\\','\\\\')
    e = e.replace('"','\\"')
    e = f'"{e}"'
    print(e,len(e))
    r += len(i)- len(y[1:-1])
    m += len(e)-len(i)
    n += len(e)
    a += len(i)
    b += len(y[1:-1])

print(a,b,r,n,m)