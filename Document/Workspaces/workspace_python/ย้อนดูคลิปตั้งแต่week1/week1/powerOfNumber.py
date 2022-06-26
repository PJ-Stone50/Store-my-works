def powerOfNumber(n, i):
    # ยกกำลัง 0 return 1
    if i >= 0 : 
        if i == 0:
            return 1
        else:
            return n * powerOfNumber(n, i-1)
    else:
        i = (-1)*i
    return -1*powerOfNumber(n,i)
i = 0;
while (True):
    n = int(input("Enter n : "))
    i = int(input("Enter i : "))
    print(powerOfNumber(n,i))

#มีปัญหาเวลายกกำลังติดลบ น่าจะเป็นตอนเช็ค if 