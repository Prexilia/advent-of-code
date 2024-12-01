firstArray = []
secondArray = []

def insertToArray(line):
    newLine = " ".join(line.split()).split(" ")
    
    firstArray.append(int(newLine[0]))
    secondArray.append(int(newLine[1]))

try:
  with open('./day1/input.txt') as f:
      for line in f:
          insertToArray(line)
except:
    print("file not found")

sum = 0

for val in firstArray:
    nbOfVal = secondArray.count(val)
    newVal = nbOfVal * val
    sum+= newVal

#test sum result: 31
print(sum)