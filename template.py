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
#li = li[0]

for l in li:
    print(l)

print()
