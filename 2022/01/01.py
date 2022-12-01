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
elf = []
li = []
with open("01.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]
#li = li[0]
cal = 0
for l in li:
    if l != "":
        c = int(l)
        cal += c
    else:
        elf.append(cal)
        cal=0

print(max(elf))
print(sum(sorted(elf)[-3:]))
