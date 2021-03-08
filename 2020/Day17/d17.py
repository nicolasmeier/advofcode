with open("Day17/test.txt", "r") as f:
    l = f.read().splitlines()
c = {}
a = {}
for j in range(len(l)):
    b = {}
    for k in range(len(l[j])):
        b[str(k)] = l[j][k]
    a[str(j)] = b
c["0"] = a

print(c)

def getxyz(c,x,y,z):
    if c.get(z):
        if c.get(z).get(y):
            if c.get(z).get(y).get(x):
                return c[z][y][x]
    return "."


def checkneighbors(x,y,z):
    alive = 0
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            for k in range(-1,2,1):
                if not (i == 0 and j == 0 and k == 0):
                    zk = str(int(z)+k)
                    yj = str(int(y)+j)
                    xi = str(int(x)+i)
                    if (getxyz(c,xi,yj,zk) == "#"):
                        alive += 1
    return alive

def cycle(c):
    newc = {}
    zki = list(map(int,c.keys()))
    for z in range(min(zki)-1,max(zki)+2):
        z = str(z)
        newb = {}
        yki = list(map(int,c["0"].keys()))
        for y in range(min(yki)-1,max(yki)+2):
            y = str(y)
            newa = {}
            xki = list(map(int,c["0"]["0"].keys()))
            for x in range(min(xki)-1,max(xki)+2):
                x = str(x)
                n = checkneighbors(x,y,z)
                e = getxyz(c,x,y,z)
                #print(x,y,z,"alive",n)
                if (e == "#" and (2 <= n <= 3)):
                    newa[x] = "#"
                elif (e == "." and n == 3):
                    newa[x] = "#"
                else:
                    newa[x] = "."
            newb[y] = newa
        newc[z] = newb
    return newc.copy()

def map_as_str():
    s = ""
    for z in c.keys():
        s +="\nz="+z+"\n"
        for y in c[z].keys():
            row = ""
            for x in c[z][y].keys():
                row += c[z][y][x]
            s += row + "\n"
    return s

def count_all_alive():
    return str(map_as_str()).count("#")

print("before")
print(map_as_str())
for cy in range(6):
    c = cycle(c)
    print(f"after {cy+1} cycle\n{map_as_str()}")

print(count_all_alive())
