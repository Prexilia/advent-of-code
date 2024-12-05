import re
def getValue(line):
    totalLineValue = 0
    pattern = r"(?:mul\(\d{1,3},\d{1,3}\))"
    matches = re.findall(pattern,line)

    for m in matches:
        nbMaches = re.findall(r"(?:\d{1,3})",m)
        totalLineValue+=(int(nbMaches[0])*int(nbMaches[1]))
    
    return totalLineValue

val=0
try:
  with open('./day3/input.txt') as f:
      for line in f:
        val+=getValue(line)
except(ValueError):
    print(ValueError)

#test total value: 161
print(val)