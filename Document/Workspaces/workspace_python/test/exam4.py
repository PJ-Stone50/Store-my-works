def test(n,j):
    if(n==0): # เช็คว่า i เป็น 0 หรือเปล่า
        return j
    elif(n>=0):
        return j*3
    elif (n > 5):
        return    
    return test(n-1,n+j) # i-1 คือ
print(test(4,7))

