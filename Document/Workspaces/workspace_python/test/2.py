a     = [12,0,39,50,1]
kk    = len(a)
new_a = []
i     = 0

while i < kk:
    xx = min(a)      ## This would retreive the minimum value from the list (a)
    new_a.append(xx) ## You store this minimum number in your new list (new_a)
    a.remove(xx)     ## Now you have to delete that minimum number from the list a
    i += 1           ## This starts the whole process again.
print(new_a)