
# key = {1,2,3}
# val = ['1','2','3']
# arraylist = []

# for i in range(3):
#   arraylist.append({i+1:val[i]})
#   #  = ({1:'1'},{2:'2'})
  
arraylist = {1:'1',2:'2',3:'3'}

print(arraylist)
print(type(arraylist))
print(arraylist[1])

update_var = {3:'999'}

arraylist.update(update_var)
print(arraylist)