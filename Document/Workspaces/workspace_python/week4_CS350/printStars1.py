def SumOddNumber(n) :
	if n == 0 :
		return 0

	elif n % 2 == 1: # Odd
		return n
	return SumOddNumber(n-1)

def printStars1(n):
	if n == 1:
		print(SumOddNumber(n), end=" ")
	else:
		print("*", end=" ")
		printStars1(n-1)

# def printStars2(n):
#     print("*", end=" ")
#     if n != 1:
#         printStars1(n-1)


def printStars3(n, ch):
	print(ch, end=" ")
	if n != 1:
		printStars1(n-1)

n = int(input("Enter here ==> "))

# printStars1(10)
# print("-"*40)

# printStars2(10)
# print("-"*40)

print(printStars3(n-1,(SumOddNumber(n))))
# print("-"*40)