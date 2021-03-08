input = "7,14,0,17,11,1,2"
test = "0,3,6"
l = input.split(",")

firstspoken = {}
lastspoken = {}
last = 0
for i in range(30000000):
    if i < len(l):
        firstspoken[int(l[i])] = i
        last = int(l[i])
    else:
        num = 0
        if last in lastspoken:
            num = firstspoken[last] - lastspoken[last]
        if num in firstspoken:
            lastspoken[num] = firstspoken[num]
        firstspoken[num] = i
        last = num
    #print(last)

print(last)
