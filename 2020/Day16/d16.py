with open("Day16/input.txt", "r") as f:
    l = f.read().splitlines()
fields = {}
for j in l:
    if j == '':
        break
    name = j.split(":")[0]
    rest = j.split(":")[1].strip()
    range1 = rest.split(" ")[0].split("-")
    range2 = rest.split(" ")[2].split("-")
    ra = list(range(int(range1[0]),int(range1[1])+1))
    rb = list(range(int(range2[0]),int(range2[1])+1))
    ra.extend(rb)
    fields[name] = ra

myticket = []
tickets = []
tl = []
for i in range(len(l)):
    if l[i] == "your ticket:":
        myticket = list(map(int,l[i+1].split(",")))
        
    if l[i] == "nearby tickets:":
        tl = l[i+1:]
        break
for t in tl:
    tickets.append(list(map(int,t.split(","))))
"""
print(myticket)
tickets.append(myticket)
print(tickets)
"""

matches = {}
for i in range(len(myticket)):
    #print(myticket[i])
    m = []
    for k in fields.keys():
        if myticket[i] in fields[k]:
            m.append(k)
    matches[i] = m

#print(matches)
valtickets = tickets.copy()
for t in tickets:
    for i in range(len(t)):
        m = []
        for k in fields.keys():
            if t[i] in fields[k]:
                m.append(k)
        if len(m) < 1:
            valtickets.remove(t)
print(len(valtickets))

for t in valtickets:
    for i in range(len(t)):
        for k in matches[i]:
            if not t[i] in fields[k]:
                matches[i].remove(k)


"""
for m in matches.keys():
    ma = []
    for x in matches[m]:
        print(x)
        if str(x).startswith("departure"):
            ma.append(x)
    matches[m] = ma
    print(m,matches[m])
"""

#print(matches)
for z in range(len(matches)):
    for m in matches.keys():
        #print(m,matches[m])
        if len(matches[m]) == 1:
            for k in matches.keys():
                if k != m and matches[m][0] in matches[k]:
                    matches[k].remove(matches[m][0])

print("-"*30)
print("myticket")
dep = 1
for m in matches.keys():
    if str(matches[m][0]).startswith("depar"):
        dep *= myticket[m]
        print(matches[m][0],myticket[m])

print(dep)

