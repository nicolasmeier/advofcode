import numpy as np
import math
import functools

with open("./2019/02/input2.txt") as f:
    l = [x.strip() for x in f.readlines()]

def run(l,noun, verb):
    l = l[0]
    instr = [int(x) for x in l.split(",")]

    instr[1] = noun
    instr[2] = verb

    ptr = 0

    while instr[ptr] != 99:
        c = instr[ptr]
        if c == 1:
            # add
            f1 = instr[ptr+1]
            f2 = instr[ptr+2]
            r = instr[ptr+3]
            instr[r] = instr[f1] + instr[f2]
        elif c == 2:
            # mul
            f1 = instr[ptr+1]
            f2 = instr[ptr+2]
            r = instr[ptr+3]
            instr[r] = instr[f1] * instr[f2]
        else:
            return -1
        ptr += 4
    return instr[0]

for n in range(99):
    for v in range(99):
        if run(l.copy(),n,v) == 19690720:
            print(n,v)
            print(100 * n + v)
            