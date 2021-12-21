import re
import numpy as np
import math
import functools
import collections 

import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("16t.txt") as f:
    li = [x.strip() for x in f.readlines()]


hex = dict()
hex["0"] = "0000"
hex["1"] = "0001"
hex["2"] = "0010"
hex["3"] = "0011"
hex["4"] = "0100"
hex["5"] = "0101"
hex["6"] = "0110"
hex["7"] = "0111"
hex["8"] = "1000"
hex["9"] = "1001"
hex["A"] = "1010"
hex["B"] = "1011"
hex["C"] = "1100"
hex["D"] = "1101"
hex["E"] = "1110"
hex["F"] = "1111"


def h2b(h):
    r = ""
    for x in h:
        r += hex[x]
    return(r)

b = []
l = li[0]
#print(l)
#print(h2b(l))
bin = h2b(l)

def split_pck(bin):
    print(bin)
    if len(bin) < 11:
        return []
    ret = []
    if bin[3:6] == "100":
        idx = 6
        keep_reading = True
        while keep_reading:
            v = bin[idx:idx+5]
            if v.startswith("0"):
                keep_reading = False
            idx += 5
            ret.append(idx)
            x = split_pck(bin[idx:])
            for y in x:
                ret.append(idx+y)
            return ret
    

def packet(bin):
    vb = bin[0:3]
    tb = bin[3:6]
    packet_version = int(vb,2)
    packet_type = int(tb,2)
    print("version",packet_version)
    keep_reading = True
    if packet_type == 4: 
        idx = 6
        # literal value
        num = ""
        while keep_reading:
            v = bin[idx:idx+5]
            num += v[1:]
            if v.startswith("0"):
                keep_reading = False
            idx += 5
        number = int(num,2)
        #print(number)
    else:
        # operator
        #print(bin)
        i = bin[6]
        if i == "1":
            #a
            print("a")
            num_sub = int(bin[7:7+11],2)
            print(num_sub)
        elif i == "0":
            #next 15 are a numb total lenght in bits
            total_length = int(bin[7:7+15],2)
            #print(total_length)
            #print(bin[7+15:7+15+total_length])
            #print(bin[7+15+3:7+15+6])
            subpckgs = bin[7+15:7+15+total_length]
            print(split_pck(subpckgs))
                
            #packet(bin[7+15:7+15+total_length])


    #b.append([int(x) for x in l])
#b = np.array(b)
packet(bin)
