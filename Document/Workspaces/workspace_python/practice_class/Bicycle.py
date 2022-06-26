class Bicycle:

  def __init__(self, gear, speed):
    self.gear = gear
    self.speed = speed

  def speedUp(self, increase):
    self.speed += increase

  def changeGear(self,newGear):
    self.gear = newGear

  def applyBrake(self, decrease):
    self.speed -= decrease


bike1 = Bicycle(gear=1, speed=30)

print(bike1.gear)
print(bike1.speed)

bike1.speedUp(50)

print(bike1.speed)