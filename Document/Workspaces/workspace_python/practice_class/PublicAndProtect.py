class PublicEmp:

  def __init__(self, salary):
    self.salary = salary
  
class ProtectedEmp:
  
  def __init__(self, salary):
    self._salary = salary



class Emp(ProtectedEmp): # class Emp เป็น child class of ProtectedEmp

  def getsalary(self):
    return self._salary


class PrivateEmp:
  
  def __init__(self, salary):
    self.__salary = salary

  def getsalary(self):
    return self.__salary


ob1 = PublicEmp(10000)
print("PublicEmp : {0:,.2f}".format(ob1.salary))

ob2 = Emp(20000)
print("Emp : {0:,.2f}".format(ob2.getsalary()))

ob3 = PrivateEmp(30000)
print("PrivateEmp : {0:,.2f}".format(ob3.getsalary()))
