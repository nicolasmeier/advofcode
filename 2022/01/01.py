import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

l = []
with open("01.txt") as f:
    l = [x.strip() for x in f.readlines()]

print("Good luck")