with open("Day10/input.txt", "r") as f:
    l = f.read().splitlines()
    l = map(int,l)
    l = list(l)
    l.append(0)
    l.append(max(l) + 3)
    l.sort()
jolt1 = 0
jolt2 = 0
jolt3 = 0

for i in range(1,len(l)):
    if (l[i]-l[i-1] == 1):
        jolt1 += 1
    elif (l[i]-l[i-1] == 2):
        jolt2 += 1
    elif (l[i]-l[i-1] == 3):
        jolt3 += 1
    else:
        print("fucked")

print(jolt1,jolt2,jolt3)
print("res",jolt1 * jolt3)
    