def isSafeReport(line): 
  
  vals = line.strip("\n").split(" ")
  
  isCroissant = 0
  isDescroissant = 0
  isDiffOk = 0
  for i, val in enumerate(vals):
    v = int(val)
    prevVal = int(vals[i-1])
    total = len(vals) - 1
    if i == 0:
      continue
    elif prevVal > v:
      isDescroissant+=1
    elif prevVal < v:
      isCroissant+=1

    if abs(prevVal - v) <= 3:
       isDiffOk+=1
    
  return (isCroissant == total or isDescroissant == total) and isDiffOk == total
   


nbSafeReports = 0
try:
  with open('./day2/input.txt') as f:
      for line in f:
        if isSafeReport(line):
           nbSafeReports+=1
except(ValueError):
    print(ValueError)

# nb safe reports test: 2
print(nbSafeReports)