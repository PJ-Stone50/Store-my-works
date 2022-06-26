global x,y,z



def sub1():
  a = "1"
  y = "2"
  z = "3"

  print(a,y,z)
  sub2()

def sub2():
  a = "4"
  b = "5"
  z = "6"
  print(a,b,z)
  sub3()

def sub3():
  a = "7"
  x = "8"
  w = "9"
  print(a,x,w)


sub1()