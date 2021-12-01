import json
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import requests
import browser_cookie3
import pandas as pd

os.chdir(os.path.dirname(sys.argv[0]))



if 1 == 0:
    #Get cookies from the browser
    cj = browser_cookie3.chrome()
    r = requests.get("https://adventofcode.com/2021/leaderboard/private/view/1483124.json", allow_redirects=False,cookies=cj)
    open("leaderboard.json", 'wb').write(r.content)
    print("Updated leaderboard.json")

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
plt.figure(figsize=(16, 9), dpi=300)
plt.grid()
plt.title(f"Advent of Code {year}")
usernames = []
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
                if t <= 86400:
                    time[int(d)] = t
    speed = []
    for day in days:
        if day in time.keys():
            speed.append(time[day])
    if len(speed) > 0:
        plt.scatter(days[:len(speed)],speed)
    else:
        usernames.pop()
plt.legend(usernames)
plt.xlabel("Day")

#plt.xlim(0,26)
plt.xlim(0,int(datetime.today().strftime('%d'))+1)
plt.ylabel("Time to Solve in s")
plt.xticks(days[:int(datetime.today().strftime('%d'))])
plt.savefig("leaderboard.png")


from datetime import datetime
days = range(1,26)
username = ""
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
print(df)

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
print("Done")
