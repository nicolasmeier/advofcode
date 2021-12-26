import numpy as np
import math
import functools
import collections 
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("23.txt") as f:
    li = [x.replace("#","").strip() for x in f.readlines()]
#li = li[0]

cost = dict()
cost["A"] = 1
cost["B"] = 10
cost["C"] = 100
cost["D"] = 1000

pos = dict()
pos["A"] = 2
pos["B"] = 3
pos["C"] = 4
pos["D"] = 5

hallway = ["","","","","","",""]
pod = dict()
pod["A"] = []
pod["B"] = []
pod["C"] = []
pod["D"] = []
for l in li[2:-1]:
    for i,p in enumerate(["A","B","C","D"]):
        pod[p].append(l[i])

print(pod)

def move(pod:dict,hallway:list,c:int):
    for k,v in pod.items():
        if not (v[1] == k and v[0] == k):
            if v[0] != "":
                value = v[0]
                # pod to hallway
                hcost = 0
                for i in range(pos[k]-1,-1,-1):
                    hcost += 1
                    if hallway[i] == "":
                        nc = c + cost[value] * (1 + hcost)
                        hc = hallway.copy()
                        hc[i] = value
                        pc = pod.copy()
                        pc[k][0] = ""
                        move(pc,hc,nc)
                    else:
                        break
                hcost = 0
                for i in range(pos[k],len(hallway)):
                    hcost += 1
                    if hallway[i] == "":
                        print(value+"-")
                        nc = c + cost[value] * (1 + hcost)
                        hc = hallway.copy()
                        hc[i] = value
                        pc = pod.copy()
                        pc[k][0] = ""
                        move(pc,hc,nc)
                    else:
                        break
            elif v[1] != "" or v[1] != k:
                
                value = v[1]
                # pod to hallway
                hcost = 0
                for i in range(pos[k]-1,-1,-1):
                    hcost += 1
                    if hallway[i] == "":
                        nc = c + cost[value] * (2 + hcost)
                        hc = hallway.copy()
                        hc[i] = value
                        pc = pod.copy()
                        pc[k][1] = ""
                        move(pc,hc,nc)
                    else:
                        break
                hcost = 0
                for i in range(pos[k],len(hallway)):
                    hcost += 1
                    if hallway[i] == "":
                        nc = c + cost[value] * (2 + hcost)
                        hc = hallway.copy()
                        hc[i] = value
                        pc = pod.copy()
                        pc[k][1] = ""
                        move(pc,hc,nc)
                    else:
                        break
    for i in range(len(hallway)):
        value = hallway[i]
        if value != "":
            podcost = 0
            if pod[value][1] == "" and pod[value][0] == "":
                podcost = 2
            elif pod[value][1] == value and pod[value][0] == "":
                podcost = 1
            if podcost > 0:
                if i == pos[value]:
                    nc = c + cost[value] * (1 + podcost)
                    hc = hallway.copy()
                    hc[i] = ""
                    pc = pod.copy()
                    if podcost == 2:
                        pc[value][1] = value
                    elif podcost == 1:
                        pc[value][0] = value
                    move(pc,hc,nc)
                elif i < pos[value]:
                    if sum([1 for x in hallway[i:pos[value]] if x != ""]) == 1:
                        nc = c + cost[value] * ((pos[value] - i) + podcost)
                        hc = hallway.copy()
                        hc[i] = ""
                        pc = pod.copy()
                        if podcost == 2:
                            pc[value][1] = value
                        elif podcost == 1:
                            pc[value][0] = value
                        move(pc,hc,nc)
                elif i > pos[value]:
                    if sum([1 for x in hallway[pos[value]:i] if x != ""]) == 1:
                        nc = c + cost[value] * ((i-pos[value]) + podcost)
                        hc = hallway.copy()
                        hc[i] = ""
                        pc = pod.copy()
                        if podcost == 2:
                            pc[value][1] = value
                        elif podcost == 1:
                            pc[value][0] = value
                        move(pc,hc,nc)
    for k,v in pod.items():
        if not (v[0] == k and v[1] == k):
            return
    print(c)
    return


move(pod,hallway,0)






    