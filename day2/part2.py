def isSafeReport(vals):
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
   
def secondChance(vals):
  for i, val in enumerate(vals):
    newVals = vals.copy()
    newVals.pop(i)

    if isSafeReport(newVals):
      return True

nbSafeReports = 0

try:
  with open('./day2/input.txt') as f:
      for line in f:
        vals = line.strip("\n").split(" ")
        if isSafeReport(vals):
          nbSafeReports+=1
        elif secondChance(vals):
          nbSafeReports+=1
except(ValueError):
    print(ValueError)

# nb safe reports test: 4
print(nbSafeReports)