def Sumation (dataArray, n):
 if n == 0:
  return dataArray[0]
 return dataArray[n] + Sumation(dataArray, n-1)

dataArray = [1,2,3,4,5,6,7,8,9,10,11]
print("sum of array = ", Sumation(dataArray, len(dataArray)-1))