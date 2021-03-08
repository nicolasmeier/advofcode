import math
f = open("Day5/input.txt", "r")

maxid = 0
seats = list(range(931))

def row(lo,up,st):
    #print(lo,up,st)
    if (not st or st == ""):
        return up
    if str(st).startswith("F"):
        return row(lo,math.floor((lo+up)/2),st[1:])
    elif str(st).startswith("B"):
        return row(math.ceil((lo+up)/2),up,st[1:])

def col(lo,up,st):
    #print(lo,up,st)
    if (not st or st == ""):
        return up
    if str(st).startswith("L"):
        return col(lo,math.floor((lo+up)/2),st[1:])
    elif str(st).startswith("R"):
        return col(math.ceil((lo+up)/2),up,st[1:])


for l in f:
    x = l.strip()
    r = row(0,127,x[:7])
    c = col(0,7,x[7:])
    sid = r*8+c
    #print(f"{x}: row {r}, colum {c}, seatid {sid}")
    seats.remove(sid)
    maxid = max(maxid,sid)
        
print(seats)
print(maxid)
    