with open("Day14/input.txt", "r") as f:
    l = f.read().splitlines()
mask = ""
andmask = ""
ormask = ""
mem = {}
for j in l:
    if j.startswith("mask"):
        mask = j[7:]
        andmask = mask.lower()
        for l in range(andmask.count("x")):
            andmask = andmask.replace("x","1")
        andmask = int("0b"+andmask,2)
        ormask = mask.lower()
        for l in range(ormask.count("x")):
            ormask = ormask.replace("x","0")
        ormask = int("0b"+ormask,2)
    else:
        num = int(j.split("=")[1].strip())
        addr = j[4:].split("]")[0].strip()
        num = (num & andmask) | ormask
        mem[addr] = num

print(mem)
print(sum(mem.values()))