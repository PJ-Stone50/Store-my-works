#Convert to Dictionary by using method
def ConvertDict():
  myDict = {i+1:fruits[i] for i in range(4)}
  return myDict

fruits = ["Apple", "Pear", "Peach", "Banana"]


print(ConvertDict())


