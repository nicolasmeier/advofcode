i = "yzbqklnj"


# Python 3 code to demonstrate the 
# working of MD5 (byte - byte)
  
import hashlib
  
def hash(i,n) -> str:
    return hashlib.md5(f"{i}{n}".encode('utf-8')).hexdigest()

n = 0
while not hash(i,n).startswith("0"*6):
    n += 1

print(n)