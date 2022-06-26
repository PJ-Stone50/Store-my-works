
A = [4,5,1,4,2,6]
new_A = []
#firstChar = A[0]

def isSorted() :
    
    i = 0
    j = i + 1
    while (i < len(A)): #ทำถึงตัวสุดท้าย

        firstChar = min(A)
        new_A.append(firstChar)
        A.remove(firstChar)
        return new_A

    if (new_A[i]< new_A[j]):
        return 1
    else:
        return 0
        


    i += 1
    print(new_A)
    
        
print(isSorted())

