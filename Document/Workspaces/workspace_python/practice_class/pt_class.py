# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)


people = {}
count_people = 0





for i in range(10):
  count_people += 1
  people[i] = Person("testName")
  print(people[i].name , str(count_people))