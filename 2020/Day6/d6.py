f = open("Day6/input.txt", "r")

sum = 0
ans = set()
ng = True

for l in f:
    x = l.strip()
    if x:
        if ng:
            ng = False
            for c in x:
                ans.add(c)
        else:
            a = set()
            for c in x:
                a.add(c)
            ans = ans.intersection(a)
    else:
        print(f"g:{len(ans)} {ans}")
        sum += len(ans)
        ans = set()
        ng = True


print(f"g:{len(ans)} {ans}")
sum += len(ans)

print(sum)
    