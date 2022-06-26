# variable number of non keyword arguments passed
 
# function definition
def calculateTotalSum(*arguments):
    totalExponent = 0
    for number in arguments:
        totalExponent += number
    print(totalExponent)
 
# function call
calculateTotalSum(4,2,2,65,8,6432,51,74233)