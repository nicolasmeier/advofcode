f = open("Day1/input.txt", "r")
n = list(map(int, f.readlines()))
for x in n:
    for y in n:
        for z in n:
            if (x+y+z == 2020):
                print(f"{x} * {y} * {z} = {x*y*z}")
