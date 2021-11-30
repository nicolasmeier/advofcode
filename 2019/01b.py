import numpy as np
import math
import functools

@functools.lru_cache()
def fuel(x:int) -> int:
    return max((int) (math.floor(x/3) - 2),0)
    

with open("./2019/01/input2.txt") as f:
    l = [x.strip() for x in f.readlines()]

a = 0
for m in l:
    x = int(m)
    while fuel(x) > 0:
        x = fuel(x)
        a += x

print(a)
