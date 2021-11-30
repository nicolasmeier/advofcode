import numpy as np
import math
import functools

with open("./2019/02/input1.txt") as f:
    l = [x.strip() for x in f.readlines()]

l = l[0]
instr = [int(x) for x in l.split(",")]
print(instr)

instr[1] = 12
instr[2] = 2

ptr = 0

while instr[ptr] != 99:
    c = instr[ptr]
    print(c)
    if c == 1:
        print("add")
        # add
        f1 = instr[ptr+1]
        f2 = instr[ptr+2]
        r = instr[ptr+3]
        print(f1,f2,r)
        instr[r] = instr[f1] + instr[f2]
    elif c == 2:
        print("mul")
        # mul
        f1 = instr[ptr+1]
        f2 = instr[ptr+2]
        r = instr[ptr+3]
        print(f1,f2,r)
        instr[r] = instr[f1] * instr[f2]
    else:
        print("error")
        quit()
    ptr += 4
print("end")
print(instr)