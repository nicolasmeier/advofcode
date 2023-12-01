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
r = 0
for l in li:
    x = l.lower()
    f=re.findall(r"\d",x) 
    if f:
        r += int(f[0])*10+int(f[-1])

print(r)

r = 0
for l in li:
    x = l.lower()
    x = x.replace("one","o1e")
    x = x.replace("two","t2o")
    x = x.replace("three","t3e")
    x = x.replace("four","f4r")
    x = x.replace("five","f5e")
    x = x.replace("six","s6x")
    x = x.replace("seven","s7n")
    x = x.replace("eight","e8t")
    x = x.replace("nine","n9e")
    f=re.findall(r"\d",x) 
    if f:
        r += int(f[0])*10+int(f[-1])

print(r)