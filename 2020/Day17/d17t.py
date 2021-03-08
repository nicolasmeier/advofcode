with open("Day17/input.txt", "r") as f:
    l = f.read().splitlines()
c = {}
a = {}
cc = {}
for j in range(len(l)):
    b = {}
    for k in range(len(l[j])):
        b[str(k)] = l[j][k]
    a[str(j)] = b
cc["0"] = a
c["0"] = cc
# c[w][z][y][x]
#print(c)

def getxyzw(c,x,y,z,w):
    if c.get(w):
        if c.get(w).get(z):
            if c.get(w).get(z).get(y):
                if c.get(w).get(z).get(y).get(x):
                    return c[w][z][y][x]
    return "."


def checkneighbors(x,y,z,w):
    alive = 0
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            for k in range(-1,2,1):
                for l in range(-1,2,1):
                    if not (i == 0 and j == 0 and k == 0 and l == 0):
                        wl = str(int(w)+l)
                        zk = str(int(z)+k)
                        yj = str(int(y)+j)
                        xi = str(int(x)+i)
                        if (getxyzw(c,xi,yj,zk,wl) == "#"):
                            alive += 1
    return alive

def cycle(c):
    newcw = {}
    wki = list(map(int,c.keys()))
    for w in range(min(wki)-1,max(wki)+2):
        w = str(w)
        newc = {}
        zki = list(map(int,c["0"].keys()))
        for z in range(min(zki)-1,max(zki)+2):
            z = str(z)
            newb = {}
            yki = list(map(int,c["0"]["0"].keys()))
            for y in range(min(yki)-1,max(yki)+2):
                y = str(y)
                newa = {}
                xki = list(map(int,c["0"]["0"]["0"].keys()))
                for x in range(min(xki)-1,max(xki)+2):
                    x = str(x)
                    n = checkneighbors(x,y,z,w)
                    e = getxyzw(c,x,y,z,w)
                    #print(x,y,z,"alive",n)
                    if (e == "#" and (2 <= n <= 3)):
                        newa[x] = "#"
                    elif (e == "." and n == 3):
                        newa[x] = "#"
                    else:
                        newa[x] = "."
                newb[y] = newa
            newc[z] = newb
        newcw[w] = newc
    return newcw.copy()

def map_as_str():
    s = ""
    for w in c.keys():
        for z in c[w].keys():
            s +="\nz="+z+", w="+w+"\n"
            for y in c[w][z].keys():
                row = ""
                for x in c[w][z][y].keys():
                    row += c[w][z][y][x]
                s += row + "\n"
    return s

def count_all_alive():
    return str(map_as_str()).count("#")

print("before")
print(map_as_str())
for cy in range(6):
    c = cycle(c)
    #print(f"after {cy+1} cycle\n{map_as_str()}")

print(count_all_alive())
