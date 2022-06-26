
def createEmailRecursive1(email, name, last, i, n):
    if i <= n:
        size = len(last[i])
        if size >= 3:
            st = name[i]+'.'+ last[i][:3]
        else:
            st = name[i]+'.'+ last[i]
        st = st+'@bumail.net'
        email.append(st)
        createEmailRecursive1(email, name, last, i+1, n)

createEmailRecursive1(email, name, last, 0, len(name)-1)
print(email)

#บ้าบอชะมัด