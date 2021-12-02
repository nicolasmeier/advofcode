import json
import matplotlib.pyplot as plt
import os
import sys
import numpy as np
from numpy.ma.core import masked
import pandas as pd
from datetime import datetime
import browser_cookie3
import requests
import time



os.chdir(os.path.dirname(sys.argv[0]))

PLOT_QUALITY = 240*1
markers = ['o', 'x', '+', 'v', '^', '<', '>', 's', 'd','p']
delta = 0
with open("lastrequest.txt","r") as l:
    last = int(l.read())
    delta = int(time.time()) - last
print(f"sec till last update {delta}")
if delta > 15*60:
    print("updated leaderboard.json as it was older than 15 min")
    #Get cookies from the browser
    cj = browser_cookie3.chrome()

    r = requests.get("https://adventofcode.com/2021/leaderboard/private/view/1483124.json", allow_redirects=False,cookies=cj)

    open("leaderboard.json", 'wb').write(r.content)
    open("lastrequest.txt","w").write(str(int(time.time())))


lastupdated = datetime.today().strftime('Last updated at %H:%M %d.%m.')
currentday = int(datetime.today().strftime('%d'))
with open("Advent-of-Code/README.MD","w") as out:
    out.write(lastupdated + "\n")
    with open("README.MD","r") as template:
        out.write(template.read())

j = ""
with open("leaderboard.json") as f:
    l = f.read()
j = json.loads(l)
year = int(j['event'])


members = []
for i in j['members']:
    members.append(dict(j['members'][i]))



from datetime import datetime
days = range(1,26)
fig = plt.figure(figsize=(16, 16), dpi=PLOT_QUALITY)
ax = fig.add_subplot(111)
plt.grid(axis="y")
plt.title(f"Advent of Code {year} Time to solve")
usernames = []
data = dict()
for m in members:
    usernames.append(m["name"])
    time = dict()
    completion_day = dict(m["completion_day_level"])
    for d in completion_day:
        r = dict(completion_day[str(d)])
        star = "1"
        if "2" in r.keys():
            star = "2"
            st = datetime.utcfromtimestamp(r[star]["get_star_ts"]).strftime('%m:%d:%H:%M:%S')
            month,day,h,m,s = [int(y) for y in st.split(":")]
            if month == 12:
                h = h-5
                day = day - int(d)
                t = s + m*60 + h*60*60 + day*60*60*24
                if t <= 7*60*60*24:
                    time[int(d)] = t
    speed = []
    for day in days:
        if day in time.keys():
            speed.append(time[day])
        else:
            speed.append(0)
    
    if len(speed) > 0:
        data[usernames[-1]] = speed
    else:
        usernames.pop()

cm = plt.get_cmap('tab20')
ax.set_prop_cycle(color=[cm(1.*i/20) for i in range(20)])
maxtime = 0
m=0
for un, speed in data.items():
    maxtime = max(maxtime,max(speed))
    if sum(speed) > 0:
        speedmasked = np.ma.array(speed)
        for i in range(len(speed)):
            if speed[i] == 0:
                speedmasked[i] = np.ma.masked
        ax.plot(days[:currentday],speedmasked[:currentday],f":{markers[m]}",label=un)
        m = (m +1) % 9
#plt.legend(usernames)
plt.xlabel("Day")
plt.legend()
plt.ylabel("Time to Solve in s")
plt.xticks(days[:currentday])
plt.yticks([0,600,60*30,3600,3600*2,3600*3,3600*4,3600*5,3600*6,3600*7,3600*8,3600*9,3600*10,3600*11,3600*12,3600*13,3600*14,3600*15,3600*16,3600*17,3600*18,3600*19,3600*20,3600*21,3600*22,3600*23,3600*24],
    ["Start","10min","30min","1h","2h","3h","4h","5h","6h","7h","8h","9h","10h","11h","12h","13h","14h","15h","16h","17h","18h","19h","20h","21h","22h","23h","24h"])
plt.xlim(0,currentday+1)
plt.ylim(-20,maxtime+600)
plt.savefig("Advent-of-Code/leaderboard.png")


days = range(1,26)
usertimes = dict()
userscore = dict()
for m in members:
    username = m["name"]
    localscore = m["local_score"]
    userscore[username] = localscore
    time = dict()
    completion_day = dict(m["completion_day_level"])
    for d in completion_day:
        r = dict(completion_day[str(d)])
        star = "1"
        if "2" in r.keys():
            star = "2"
            st = datetime.utcfromtimestamp(r[star]["get_star_ts"]).strftime('%Y:%m:%d:%H:%M:%S')
            jahr,month,day,h,m,s = [int(y) for y in st.split(":")]
            if month == 12 and jahr == year:
                h = h-5
                day = day - int(d)
                t = s + m*60 + h*60*60 + day*60*60*24 
                time[int(d)] = t
    usertimes[username] = time


table = []
cols = ["username"]
for d in days:
    cols.append(f"day{d}")
cols.append("localscore")
for k,time in usertimes.items():
    row = []
    row.append(k)
    for d in days:
        
        if d in time.keys():
            row.append(time[d])
        else:
            row.append(0)
    # Score
    row.append(userscore[k])
    table.append(row)



df = pd.DataFrame(table,columns=cols)
df = df.sort_values("localscore",ascending=False)
#print(df)
df.to_markdown("Advent-of-Code/tts.md")
df.to_markdown("Advent-of-Code/data/tts.md")
df.to_csv("Advent-of-Code/data/tts.csv")
df.to_excel("Advent-of-Code/data/tts.xlsx")

# Rankings

userrank = dict()
for n in usertimes.keys():
    userrank[n] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for d in range(1,currentday+1):
    ds = df[df[f"day{d}"] > 0]
    ds = ds.sort_values(f"day{d}",ascending=True)
    r = 1
    for n in ds["username"]:
        userrank[n][d-1] = r
        r += 1



fig = plt.figure(figsize=(16, 10), dpi=PLOT_QUALITY)
ax = fig.add_subplot(111)
plt.grid(axis="y")
plt.title(f"Advent of Code {year} Rankings")
numofranks = sum([1 for x in list(userrank.values()) if sum(x)>=1])
cm = plt.get_cmap('tab20')
ax.set_prop_cycle(color=[cm(1.*i/20) for i in range(20)])

m=0
for n,r in userrank.items():
    if sum(r) > 0:
        rmasked = np.ma.array(r)
        for i in range(len(r)):
            if r[i] == 0:
                rmasked[i] = np.ma.masked
        ax.plot(days[:currentday],rmasked[:currentday],f":{markers[m]}",label=n)
        m = (m +1) % 9
        #plt.plot(days,r,":")

plt.xlabel("Day")
plt.legend()
plt.xlim(0,currentday+1)
plt.ylabel("Rank")
plt.ylim(0,numofranks+1)
plt.xticks(days[:currentday])
plt.yticks(range(1,numofranks+1))
plt.savefig("Advent-of-Code/rankings.png")


def intstr(i:int) -> str:
    if i == 0:
        return ""
    return str(i)

rankdata = []
for k,v in userrank.items():
    if sum(v) > 0:
        row = [k]
        [row.append(intstr(x)) for x in v]
        rankdata.append(row)
#print(rankdata)
cols = ["username"]
[cols.append(f"{d}") for d in days]
rf = pd.DataFrame(rankdata,columns=cols)
rf = rf.sort_values("username")
#print(rf)
rf.to_markdown("Advent-of-Code/rankings.md")
rf.to_markdown("Advent-of-Code/data/rankings.md")
rf.to_csv("Advent-of-Code/data/rankings.csv")
rf.to_excel("Advent-of-Code/data/rankings.xlsx")
'''
txt_line = ""
csv_line = "Username;"
# 2678400
unl = max([len(k) for k in usertimes.keys()])
usrl = "Username"
txt_line +="| "+usrl.ljust(unl)+" |"
for q in days:
    txt_line += str(f"Day {q}").rjust(7)+" |"
    csv_line += f"Day {q};"
txt_line += "TotalTime".rjust(9)+" |"
csv_line += f"TotalTime"
for k,time in usertimes.items():
    txt_line += "\n| " + str(k).ljust(unl)+" |"
    csv_line += "\n" + str(k) + ";"
    for d in days:
        if d in time.keys():
            txt_line += str(time[d]).rjust(7)+" |"
            csv_line += str(time[d]).rjust(7) + ";"
        else:
            txt_line += "".rjust(7)+" |"
            csv_line += ";"
    txt_line += str(sum([w for w in time.values()])).rjust(9) + " |"
    csv_line += str(sum([w for w in time.values()]))

csv_line += "\n"

with open("leaderboard.txt","w") as txt_file:
    txt_file.write(txt_line)
with open("leaderboard.csv","w") as csv_file:
    csv_file.write(csv_line)
'''
#print("Done")
