test = "0,3,6"
input = "7,14,0,17,11,1,2"
l = input.split(",")

spoken = []
for i in range(2020):
    if i < len(l):
        spoken.append(int(l[i]))
    else:
        if spoken.count(spoken[i-1]) == 1:
            spoken.append(0)
        else:
            spoken.reverse()
            num = i - (len(spoken) - spoken.index(spoken[0],1))
            spoken.reverse()
            spoken.append(num)

print(spoken.pop())
