def CalA(e):
  result = e * 10
  return result

def MainMethod(*args):
  result = 0
  for arg in args:
    result += arg
  return result

print(MainMethod(2,3,CalA(5)))