with open("Day24/input.txt", "r") as f:
    l = f.read().splitlines()

bl = set()
for j in l:
    j = j.strip()
    x,y = 0, 0
    i = 0
    while j != "":
        if j.startswith("nw"):
            x += 0
            y += 1
            j = j[2:]
        elif j.startswith("ne"):
            x += 1
            y += 1
            j = j[2:]
        elif j.startswith("sw"):
            x += -1
            y += -1
            j = j[2:]
        elif j.startswith("se"):
            x += 0
            y += -1
            j = j[2:]
        elif j.startswith("w"):
            x += -1
            y += 0
            j = j[1:]
        elif j.startswith("e"):
            x += 1
            y += 0
            j = j[1:]
    s = str(x) +"/"+ str(y)
    if s in bl:
        #print("rem",s)
        bl.remove(s)
    else:
        #print("add",s)
        bl.add(s)

#print(bl)
print("part1: ",len(bl))


# -------------------------------------
def getn(t):
    x,y = t.split("/",1)
    x,y = int(x), int(y)
    return [
        str(x+1)+"/"+str(y+1),
        str(x+1)+"/"+str(y),
        str(x)+"/"+str(y+1),
        str(x)+"/"+str(y-1),
        str(x-1)+"/"+str(y),
        str(x-1)+"/"+str(y-1)
    ]


print(getn("0/0"))

for day in range(100):
    newbl = set()
    alln = []
    for b in bl:
        alln.extend(getn(b))
    for b in bl:
        if not (not b in alln or alln.count(b) > 2):
            newbl.add(b)
    sn = set(alln.copy())
    for s in sn:
        alln.remove(s)
    for a in alln:
        if alln.count(a) == 1:
            newbl.add(a)
        
    print(f"Day {day+1}: {len(newbl)}")
    bl = newbl.copy()
