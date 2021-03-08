
with open("Day13/input.txt", "r") as f:
    l = f.read().splitlines()
bus = list(l[1].split(","))
bus_map = {}
for i in range(len(bus)):
    if not bus[i] == "x":
        bus_map[int(bus[i])] = i

print(bus_map)
maxkey = max(bus_map.keys())
print(maxkey)
print((100000000000142 + bus_map[maxkey]) % maxkey)
time = 100000000000142
bmk = list(bus_map.keys())
bmk.sort(reverse=True)
while True:
    corr = True
    for bk in bmk:
        if not ((time + bus_map.get(bk)) % bk == 0):
            corr = False
            break
    if corr:
        print("hurra")
        print(time)
        exit()
    if time % 14200000 == 0:
        print(time)
    time += maxkey