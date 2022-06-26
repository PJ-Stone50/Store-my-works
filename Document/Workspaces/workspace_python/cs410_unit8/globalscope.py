a = 10
result = 0

# Unknow "result" in block of Method if not declare a global keyword inside function
def tester(e):
  global result
  result += e
  return result

print(tester(a+100))
