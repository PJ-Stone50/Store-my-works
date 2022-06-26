class Employee:

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = int(pay)
    self.email = first + '.' + last + '@trojan.com'


  def printlist():
    print(emp_1.first)


emp_1 = Employee('Anoy1', 'Stone', 90.56)