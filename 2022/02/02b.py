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


# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# A for Rock, B for Paper, and C for Scissors

li = []
with open("02.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]
# li = li[0]

 # X means you need to lose, Y means you need to end the round in a draw, and Z win
def play(e,m):
    s = 0
    if m == "X":
        s += 0
    elif m == "Y":
        s += 3
    elif m == "Z":
        s += 6

    if e == "A":
        if m == "X":
            s += 3
        elif m == "Y":
            s += 1
        elif m == "Z":
            s += 2

    if e == "B":
        if m == "X":
            s += 1
        elif m == "Y":
            s += 2
        elif m == "Z":
            s += 3

    if e == "C":
        if m == "X":
            s += 2
        elif m == "Y":
            s += 3
        elif m == "Z":
            s += 1
    return s


score = 0
for l in li:
    e,m = l.split(" ",2)
    score += play(e,m)

print(score)
