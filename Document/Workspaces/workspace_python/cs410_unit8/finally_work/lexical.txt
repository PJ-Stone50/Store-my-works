class Pupil():
  #Constructure
  def __init__(self):
    self.forename = ""
    self.surname = ""
    self.email = ""
    self.formclass = ""
    self.DOB = ""
    self.test1 = 0
    self.test2 = 0
    self.test3 = 0

def ReadDetails(filename):
  pupils = [Pupil() for x in range(10)]

  items = []
  counter = 0

  with open(filename) as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        pupils[counter].forename = items[0]
        pupils[counter].surname = items[1]
        pupils[counter].email = items[2]
        pupils[counter].formclass = items[3]
        pupils[counter].DOB = items[4]
        pupils[counter].test1 = int(items[5])
        pupils[counter].test2 = int(items[6])
        pupils[counter].test3 = int(items[7])
        counter += 1
        line = readfile.readline().rstrip('\n')
    input("File read please press any key to continue")
    return pupils


def DisplayMin(pupils):
  min = 0
  for counter in range(len(pupils)):
    if pupils[counter].test1 < pupils[min].test1:
      min = counter

  print("The lowest mark in test1 was " + str(pupils[min].test1))
  print("By " + pupils[min].forename + " " + pupils[min].surname)
  print("Email " + pupils[min].email + " Form Class: " + pupils[min].formclass)
  print("DOB : " + pupils[min].DOB)

Pupils = ReadDetails("finally_work/PupilData.csv")
DisplayMin(Pupils)



