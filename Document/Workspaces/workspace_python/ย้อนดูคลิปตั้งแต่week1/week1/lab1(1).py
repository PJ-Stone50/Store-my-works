array = [-110,-503,15,-7,11,13,17,-19,2,29,31,37,41,4,-3,-10]

def findNum(array, n):
    
    if n not in array :
        
        return ("not found %d in array"%n)
    return ("Found %d in array"%n)

n = int(input("Enter n : "))

print(findNum(array,n))