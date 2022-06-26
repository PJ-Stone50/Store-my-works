class Restaurants(object):
  def __init__(self, wk1):
    self._wk1 = wk1

  def __add__(self, other):
    retval = [x + y for x, y in zip(self._wk1, other._wk1)]
    return Restaurants(retval)

  def __str__(self):
    return str(self._wk1)


wk1_city_1 = Restaurants([10, 20, 30, 40, 50])
wk1_city_2 = Restaurants([20, 40, 60, 80, 100])

total = wk1_city_1 + wk1_city_2
print(total)

# Output
# [30, 60, 90, 120, 150]