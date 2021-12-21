from datetime import date
from datetime import datetime
import os
from  time import sleep
import requests
import browser_cookie3

import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))


today = date.today()
year = "2021"
day = date.today().strftime("%d").lstrip("0")

print(f"Day {day} Y={year}")

timenow = int(datetime.now().strftime("%H%M%S"))
exectime = 60002
if timenow < exectime:
    print(f"now = {timenow},run at {exectime}")
    h = int(exectime/10000) - int(datetime.now().strftime("%H"))
    m = int((exectime%10000)/100) - int(datetime.now().strftime("%M"))
    s = int(exectime%100) - int(datetime.now().strftime("%S"))
    sleeptime = h*60*60 + m*60 + s
    print(f"sleep for {sleeptime}s")
    sleep(sleeptime)

print(f"do work at {datetime.now()}")
print(f"Day {day} Y={year}")

if not year in os.listdir():
    os.mkdir(year)

out_fn = f"{day.zfill(2)}.txt"
out_fp = f"{year}/{out_fn}"
inputurl = f"https://adventofcode.com/{year}/day/{day}/input"

if out_fn in os.listdir(year):
    os.remove(out_fp)

#Get cookies from the browser
cj = browser_cookie3.firefox()

r = requests.get(inputurl, allow_redirects=False,cookies=cj)

open(out_fp, 'wb').write(r.content)