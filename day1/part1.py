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


firstArray.sort()
secondArray.sort()

sum = 0

for i, val in enumerate(firstArray):
    diffVal = val-secondArray[i]
    if diffVal < 0: 
        diffVal = -1*diffVal
    sum+= diffVal

#test sum result: 11
print(sum)