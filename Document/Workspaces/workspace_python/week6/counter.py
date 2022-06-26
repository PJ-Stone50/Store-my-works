from itertools import permutations, product
import math

def generate_all_combinations(num_list, operators):
    all_combi = []
    for n,o in product(sorted(set(permutations(num_list))),
                       product(operators, repeat=3)): 
        x = [None]*(len(n)+len(o))
        x[::2] = n
        x[1::2] = o
        all_combi.append(x)
    return all_combi
#--------------------------------------------------------- 
def calc(num1,op,num2):
    if op == '+':
        r = num1 + num2
    elif op == '-':
        r = num1 - num2
    elif op == '*':
        r = num1 * num2
    elif op == '/':
        r = num1 / num2
    return r
#---------------------------------------------------------
nums = input('Enter 4 integers: ')
num_list = nums.split()
num1 = num_list[0]
num2 = num_list[1]
num3 = num_list[2]
num4 = num_list[3]
operators = "+","-","*","/"
...
...
cases = generate_all_combinations(num_list,  '+-*/' )
...
while r == 24:
    
    
    
    r = calc(num1)
#while 
#if all_combi == 24:
    #print(+"= 24")
#else :
#    print("No Solutions")
#print(all_combi)
print("("+"("+cases[1][0]+cases[1][1]+cases[1][2]+")"+cases[1][3]+cases[1][4]+")"+cases[1][5]+cases[1][6])
print("("+cases[1][0]+cases[1][1]+"("+cases[1][2]+cases[1][3]+cases[1][4]+")"+")"+cases[1][5]+cases[1][6])
print("("+cases[1][0]+cases[1][1]+cases[1][2]+")"+cases[1][3]+"("+cases[1][4]+cases[1][5]+cases[1][6])+")"
print(cases[1][0]+cases[1][1]+"("+"("+cases[1][2]+cases[1][3]+cases[1][4]+cases[1][5]+")"+cases[1][6])+")"
print(cases[1][0]+cases[1][1]+"("+cases[1][2]+cases[1][3]+"("+cases[1][4]+cases[1][5]+cases[1][6])+")"+")"