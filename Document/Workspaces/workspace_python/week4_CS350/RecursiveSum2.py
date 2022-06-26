def SumOddNumber2(n) : # s ไว้เก็บค่าไรสักอย่างอะ งงไปหมดเลยจิง ต้องการเฉลย Goddamn I wanna go to my GameWorld
	if n == 0 :
		return 0

	elif n % 2 == 1: # Odd
		return n
	# sum = (SumOddNumber2(n-1) - 2)
	return SumOddNumber2(n-1)


def RecursiveSum(n):
	if n == 0:
		return 0
	return SumOddNumber2(n-1)



n = int(input("Enter here ==> "))
print(SumOddNumber2(n))
print(RecursiveSum(n))