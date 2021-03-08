f = open("Day8/corr.txt", "r")
l = f.readlines()
ints = {}
vis = []
ac = 0
i = 0
lasti = 0
while not i in vis:
    if i >= len(l):
        print(ac)
        exit()
    lasti = i
    vis.append(i)
    x = l[i].strip().split(" ")
    if x[0] == "acc":
        ac += int(x[1])
        i += 1
    elif x[0] == "jmp":
        i += int(x[1])
    elif x[0] == "nop":
        i += 1
        



print(ac)
print(lasti)
    