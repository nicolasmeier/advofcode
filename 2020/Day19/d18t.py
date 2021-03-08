import re
with open("Day18/input.txt", "r") as f:
    l = f.read().splitlines()

def solve(m):
    #print(m)
    result = 0
    m = str(m).replace(" ","")

    while m.count("(") > 0:
        subm = m[m.index("(")+1:]
        rem = re.match("([0-9\+\*]*(\([0-9\+\*]*\))*)*",subm)
        sub = rem.group(0)
        #print("sub",sub)
        solv = solve(sub)
        m = m[:m.index("(")] + str(solv) + m[m.index("(")+len(sub)+2:]
        #print("sub",sub,"res",solv,"after",m)
        #print(m[:m.index("(")])
        #print(m[m.index("(")+len(sub)+2:])
        #exit()


    num = re.match("[0-9]*",m)
    #print(m)
    result += int(num.group(0))
    m = m[len(num.group(0)):]
    while m != "":
        num = re.match("[0-9]*",m[1:])
        n = num.group(0)
        if m.startswith("*"):
            m = m[1:]
            return result * solve(m)
        elif m.startswith("+"):
            m = m[1:]
            m = m[len(n):]
            result += int(n)
        else:
            print("fuck")
            print(m)
            exit()

    return result

s = 0
for e in l:
    res = solve(e)
    print(f"{e} \t\t=\t{res}")
    s += res
    #exit()

print(s)