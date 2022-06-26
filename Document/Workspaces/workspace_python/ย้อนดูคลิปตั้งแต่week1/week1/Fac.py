

# def Fac(n):

#     if n < 0:
#         return # return null
    
#     elif n >= 1 :
#         return n * Fac(n-1) # มั่วๆๆ
#     return Fac(n-1)

# n = int(input("Enter n : "))
# print("สักวันต้องได้ดี !!!")
# print(Fac(n))




# สักวันต้องได้ดีจิงๆๆๆๆๆๆๆๆ

def Fac2(n):
    if n <= 0:
        return 1

    return n * Fac2(n-1)

##บ้าบอไปใหญ่
n = int(input("Enter n : "))

print(Fac2(n))
print(Fac2(n-1))
print(Fac2(n-2))
print(Fac2(n-3))
print(Fac2(n-4))
print(Fac2(n-5))
print(Fac2(n-6))

print("*"*40)

print(Fac2(n-6))
print(Fac2(n-5))
print(Fac2(n-4))
print(Fac2(n-3))
print(Fac2(n-2))
print(Fac2(n-1))
print(Fac2(n-0))

