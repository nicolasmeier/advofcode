import itertools
from z3 import *
import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
from collections import defaultdict
from itertools import permutations
file = "08"
#file = "8small"
ret = 0
def getlines(day):
    with open(f"{day}.txt") as f:
        return [line.strip() for line in f.readlines() if len(line) > 1]

def getblankseparated(day):
    with open(f"{day}.txt") as f:
        return f.read().split("\n\n")

def tokenedlines(day):
    lines = getlines(day)
    ret = []
    for line in lines:
        parts = line.strip().split(' ')
        parsed_parts = []
        for part in parts:
            try:
                parsed_parts.append(int(part))
            except:
                try:
                    parsed_parts.append(float(part))
                except:
                    parsed_parts.append(part)
        ret.append(parsed_parts)
    return ret

NUMS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
NUMS_LOOKUP = {pattern: i for i, pattern in enumerate(NUMS)}

ALL = list("abcdefg")
def generate_permutations(remain=ALL):
    if remain == []:
        return ['']
    ret = []
    for i in range(len(remain)):
        children = generate_permutations(remain[:i] + remain[i+1:])
        for c in children:
            ret.append(remain[i] + c)
    return ret

def transform(s, perm):
    ret = []
    for c in s:
        ret.append(perm[ord(c) - ord('a')])
    return ''.join(sorted(ret))

def check_permutation(permutation, nums):
    for num in nums:
        if transform(num, permutation) not in NUMS:
            return False
    return True


lines = tokenedlines(file)
part1 = 0
for line in lines:
    #for permutation in generate_permutations():
    for permutation in permutations(ALL):
        if check_permutation(permutation, line[:10]):
            x = 0
            for i in range(11, 15):
                val = NUMS_LOOKUP[transform(line[i], permutation)]
                if val in [1,4,7,8]:
                    part1 += 1
                x = 10 * x + val
            ret += x


#print(f"all perms are {generate_permutations()}")
print(f"Answers are {part1}, {ret}")