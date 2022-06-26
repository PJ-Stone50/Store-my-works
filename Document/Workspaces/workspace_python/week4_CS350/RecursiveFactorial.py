def RecursiveFactorial(n):
    if n == 0:
        return 1
    return n * RecursiveFactorial(n-1)


print(RecursiveFactorial(4))
# 1+2+3+4+5 = 15