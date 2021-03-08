import time

input_value = "389125467"
#input_value = "364289715"

cups = []
for i in range(1000000):
    if i < len(input_value):
        cups.append(input_value[i])
    else:
        cups.append(str(i+1))
current = 0
lowest = 1
highest = 1000000
lencups = len(cups)
#print(cups,lowest,highest)

tottime = 0
for m in range(10000000):
    s = time.perf_counter()
    #print(f"-- move {m+1} --")
    ccup = cups[current]
    #print(f"cups: {cups} [{ccup}]")
    #print(f"current {ccup}")
    c1 = (current+1) % lencups
    c2 = (current+2) % lencups
    c3 = (current+3) % lencups
    pickup = [cups[c1],cups[c2],cups[c3]]
    #print(f"pickup: {pickup}")
    rest = cups.copy()
    rest.remove(cups[c1])
    rest.remove(cups[c2])
    rest.remove(cups[c3])
    num = int(ccup)
    cont = 0
    while cont == 0:
        num = num - 1
        if num < lowest:
            num = highest
        if str(num) in rest:
            cont = 1
    dest = rest.index(str(num))
    #print(f"dest: {rest[dest]}")
    cups = rest[:dest+1] + pickup + rest[dest+1:]
    current = (cups.index(ccup) + 1) % lencups
    #print()
    tottime += time.perf_counter() -s
    print(tottime/(m+1))

#print(f"-- final --\ncups: {cups}\n")
#ans_part1 = cups[cups.index("1")+1:]+cups[:cups.index("1")]
ans_part2 = cups[cups.index("1")+1] + " and "+cups[cups.index("1")+2]
answer = int(cups[cups.index("1")+1]) * int(cups[cups.index("1")+2])
print("part2",ans_part2,answer)