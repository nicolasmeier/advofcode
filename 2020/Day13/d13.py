
with open("Day13/input.txt", "r") as f:
    l = f.read().splitlines()
earliest = int(l[0])
bus = list(l[1].split(","))
for i in range(bus.count("x")):
    bus.remove("x")
bus = list(map(int,bus))
bus.sort()
print(bus)

wait = 0
while True:
    for b in bus:
        if ((earliest + wait) % b == 0):
            print(wait,b,wait*b)
            exit()
    wait += 1