with open("Day14/input.txt", "r") as f:
    l = f.read().splitlines()
mask = ""
ormask = ""
mem = {}

def floating(addr):
    ret = []
    am = ""
    addr = bin(int(addr) | ormask)
    addr = str(addr[2:])
    addr = (len(mask)-len(addr))*"0"+addr
    #print(mask)
    #print(addr)
    for i in range(len(mask)):
        if mask[i] == "X":
            am += "X"
        else:
            am += addr[i]
    #print(am)
    for i in range(2**am.count("X")):
        amc = am.upper()
        b = str(bin(i))[2:]
        b = (am.count("X")-len(b))*"0"+b
        #print(b)
        for j in range(len(b)):
            amc = amc.replace("X",b[j],1)
            #print(j,b[j],amc)
        #print(amc)
        ret.append(int(amc,2))
    return ret


for j in l:
    if j.startswith("mask"):
        mask = j[7:]
        ormask = mask.lower()
        for l in range(ormask.count("x")):
            ormask = ormask.replace("x","0")
        ormask = int("0b"+ormask,2)
    else:
        num = int(j.split("=")[1].strip())
        addr = j[4:].split("]")[0].strip()
        addrs = floating(addr)
        for a in addrs:
            mem[a] = num

print(mem)
print(sum(mem.values()))