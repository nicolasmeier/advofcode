import numpy as np
import math

with open("./2019/01/input1.txt") as f:
    l = [x.strip() for x in f.readlines()]

a = 0
for m in l:
    x = int(m)
    x = (int) (math.floor(x/3) - 2)
    a += x

print(a)
