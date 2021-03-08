input_value = "364289715"
#input_value = "364289715"

cups = input_value
current = 0
lowest = 999
highest = 0
lencups = len(cups)
for c in cups:
    lowest = min(int(c),lowest)
    highest = max(int(c),highest)
#print(cups,lowest,highest)

for m in range(100):
    print(f"-- move {m+1} --")
    ccup = cups[current]
    print(f"cups: {cups} [{ccup}]")
    #print(f"current {ccup}")
    c1 = (current+1) % lencups
    c2 = (current+2) % lencups
    c3 = (current+3) % lencups
    pickup = cups[c1]+cups[c2]+cups[c3]
    print(f"pickup: {pickup}")
    rest = ""
    for i in range(lencups):
        if not (i == c1 or i == c2 or i == c3):
            rest = rest + cups[i]
    #print(f"rest: {rest}")
    num = int(ccup)
    cont = 0
    while cont == 0:
        num = num - 1
        if num < lowest:
            num = highest
        cont = rest.count(str(num))
    dest = rest.index(str(num))
    print(f"dest: {rest[dest]}")
    cups = rest[:dest+1] + pickup + rest[dest+1:]
    current = (cups.index(ccup) + 1) % lencups
    print()

print(f"-- final --\ncups: {cups}\n")
ans_part1 = cups[cups.index("1")+1:]+cups[:cups.index("1")]
print("part1",ans_part1)