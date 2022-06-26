class MyClass:
  # I Got ya Mr.Default
  # Don't forget to set None in paramether 
  def __init__(self,name,price=None):
    self.name = name
    self.price = price
    if price is None:
      self.price = 999
    

  def __add__(self,other):
    result = (self.name + other.name,self.price + other.price)
    return result

Object1 = MyClass('a',100)
Object2 = MyClass('b')
print(Object1+Object2)
print('น่าจะเข้าใจตั้งแต่เทอมที่แล้ว แล้ว')

  