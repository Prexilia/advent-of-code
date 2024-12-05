import re

val=0
enable = True

def getValue(line):
    totalLineValue = 0
    global enable
    pattern = r"(?:mul\(\d{1,3},\d{1,3}\))|(?:do\(\))|(?:don't\(\))"
    matches = re.findall(pattern,line)
    for m in matches:
        if m.find('do()') != -1:
           enable = True
        elif m.find("don't()") != -1:
           enable = False
        elif(enable):
            nbMaches = re.findall(r"(?:\d{1,3})",m)
            totalLineValue+=(int(nbMaches[0])*int(nbMaches[1]))
    
    return totalLineValue


try:
  with open('./day3/input.txt') as f:
      for line in f:
        val+=getValue(line)
except(ValueError):
    print(ValueError)

#test total value: 48
print(val)