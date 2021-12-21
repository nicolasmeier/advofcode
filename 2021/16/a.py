
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

d=open("16.txt").read().strip().strip()
data=''
for i in d:
  b = bin(int(i,16))[2:]
  if len(b) < 4:
    data += "0" * (4-len(b))
  data += b

s = 0
def parsepacket(data):
  global s
  if not data: return
  values = []
  version = int(data[:3],2)
  data = data[3:]
  s += version
  typeID = int(data[:3],2)
  data = data[3:]
  number = ""
  #print("version", version)
  #print("type", typeID)
  if typeID == 4:
    while data[0] == '1':
      number += data[1:5]
      data = data[5:]
    number += data[1:5]
    data = data[5:]
    #print("type: literal", int(number,2))
    values.append(int(number,2))
  else:
    #print("type: operator")
    op = None
    if typeID == 0:
      op = sum
    elif typeID == 1:
      def product(a):
        r = 1
        for i in a:
          r *= i
        return r
      op = product
    elif typeID == 2:
      op = min
    elif typeID == 3:
      op = max
    elif typeID == 5:
      op = lambda x:x[0]>x[1]
    elif typeID == 6:
      op = lambda x:x[0]<x[1]
    elif typeID == 7:
      op = lambda x:x[0]==x[1]
    subvalues = []
    if data[0] == '0':
      data = data[1:]
      length = int(data[:15],2)
      #print("mode 0, length", data[:15], length)
      data = data[15:]
      subpackets = data[:length]
      data = data[length:]
      while len(subpackets) and int(subpackets,2):
        subpackets, val = parsepacket(subpackets)
        subvalues.extend(val)
    else:
      data = data[1:]
      length = int(data[:11],2)
      data = data[11:]
      #print("mode 1, length", length)
      for i in range(length):
        data, val = parsepacket(data)
        subvalues.extend(val)
    values.append(op(subvalues))
    #print(typeID, values)
  #print("rest", data)
  return (data, values)

while len(data) and int(data,2):
  data, values = parsepacket(data)
  #print(values)
print(s, values[0])