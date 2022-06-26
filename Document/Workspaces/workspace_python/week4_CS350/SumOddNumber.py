def SumOddNumber(n) :
	if n == 0 :
		return 0

	elif n % 2 == 1: # Odd
		return n
	return SumOddNumber(n-1)


def printSum(n):
	if n != 0 :
		SumOddNumber(n-1)



n = int(input("Enter here ==> "))

print(SumOddNumber(n))
print(printSum(n))




