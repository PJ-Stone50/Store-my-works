a = [-2,-1,1,2,5,7,14,15]
target = -4

def twoSum(a, target):
  for i in range(len(a)-1):
    for j in range(i+1,len(a)):
      if a[i] + a[j] == target:
        print(a[i] + a[j])
        return True
    
  return False

print(twoSum(a,target))