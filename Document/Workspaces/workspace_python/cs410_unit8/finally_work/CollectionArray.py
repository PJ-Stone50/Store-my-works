

# tuple1 = ({1:'1'},2,3)
# print(tuple1[0])
# print(type(tuple1))


# lst1 = [[1,'str1'],[2]]
# print(lst1[0])
# print(type(lst1))



# str1 = "1-2-3-4-5"
# arr = str1.split("-")
# print(arr)
# for i in range(len(arr)):
#   arr[i] = int(arr[i])
#   print(arr[i])

# print(arr)

# --------------------------------------------------------

def underline():
  print("-"*40)


tuple_array = (7,4,3,7,2,2,2,2)
convertSet = set(tuple_array)
print(convertSet)
print(type(convertSet))
underline()

string2 = "74372222"
convertList = list(string2)
print(convertList)
print(type(convertList))
print(convertList[0])
convertList[0] = 999
print(convertList)
underline()


string3 = "74372222"
convertTuple = tuple(string3)
print(convertTuple)
print(type(convertTuple))
print(convertTuple[0])
convertTuple[3] = 999
print(convertTuple)
underline()

# ----------------------------------------

# arr = (6,4,2,1,8,15)
# lst = set(arr)
# print(lst)
# print(type(lst))


arrlst = {1:["str1",10],2:["str2",20]}
print(arrlst[1][0])



arr = {1,2,3}
print(type(arr))
# print(arr[1])