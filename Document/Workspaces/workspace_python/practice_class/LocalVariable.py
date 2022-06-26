# Global scope
s = "I love Geeksforgeeks"

# This function uses global variable s
def f():
    print("Inside Function", s)
 
f()
print("Outside Function", s)