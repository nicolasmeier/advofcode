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
with open("06.txt") as f:
    li = [trans(x) for x in f.readlines()]

res1 = 0    
res2 = 0

nums = []
for line in li[:-1]:
    nums.append( [int(x) for x in line.split()] )

nums = np.array(nums).T

for i,o in enumerate(li[-1].split()):
    if o == "*":
        res1 += np.prod(nums[i])
        continue
    elif o == "+":
        res1 += np.sum(nums[i])
        continue
    else:
        print("Unknown operator:", o)
print("res1:", res1)

strange = np.array([list(l) for l in li][:-1]).T

idx = 0
nums = []
for s in strange:
    st = "".join(s).strip()
    if st.isdigit():
        nums.append(int(st))
    else:
        if li[-1].split()[idx] == "*":
            res2 += np.prod(nums)
        elif li[-1].split()[idx] == "+":
            res2 += np.sum(nums)
        idx += 1
        nums = []
if li[-1].split()[idx] == "*":
    res2 += np.prod(nums)
elif li[-1].split()[idx] == "+":
    res2 += np.sum(nums)



print("res2:", res2)