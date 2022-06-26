A = [-2,-1,1,2,5,7,14,15,16,19,20]
B = [-4,-3,1,6,5,8,11,13]
target = 7
# B.append(999)
# print(B)



def twoSum(A,B, target):
  count = len(A) - len(B)
  if count < 0:
    count *= -1

  for i in range(count):
    if len(A) < len(B):
      A.append(999)
    elif len(B) < len(A):
      B.append(999)
    # break


  for i in range(len(A)):

    if A[i] + B[i] == target:
      print(str(A[i]) +','+ str(B[i]))
      return True
    
  return False

# twoSum(A,B,target)
# print(A)
# print(B)

print(twoSum(A,B,target))
print(A)
print(B)


