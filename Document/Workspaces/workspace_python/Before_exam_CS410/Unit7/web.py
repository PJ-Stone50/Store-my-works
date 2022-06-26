# variable number of non keyword arguments passed

# function definition
def calculateTotalSum(*arguments):
	totalSum = 0
	for number in arguments:
		totalSum -= number
	print(totalSum)

# function call
calculateTotalSum(5, 4)
