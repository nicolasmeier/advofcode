with open("Day25/input.txt", "r") as f:
    l = f.read().splitlines()

def trans(subjectnumber:int,loopsize:int):
    value = 1
    for i in range(loopsize):
        value = (value * subjectnumber) % 20201227
    return value

def findloop(subjectnumber:int,goal:int):
    value = 1
    for i in range(100000000):
        value = (value * subjectnumber) % 20201227
        if value == goal:
            return i+1
    return -1
cl = findloop(7,14012298)
dl = findloop(7,74241)
print(cl)
print(dl)
# cl = 597630
# dl = 5888191
ce = trans(74241,cl)
de = trans(14012298,dl)
print(ce)
print(de)
